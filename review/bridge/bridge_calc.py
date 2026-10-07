"""저하–회복 통합 평가(LMDI) 계산.

순효율 = 보일러효율(직접법) × 사이클효율 × (1 − 소내동력비)  [본문 식 (3b)]
두 상태 간 순효율 차이를 로그평균 Divisia 지수(LMDI)로 세 인자에 정확히 배분한다.
저하(석탄→혼소 기본)의 보일러 항은 PTC 4 손실분해(Table S5)의 조성·온도·크레딧 비율로 다시 나눈다.
  - LHV 기준: 온도·크레딧 기여(HHV 입열 대비 %p)에 혼합연료 HHV/LHV 비 κ를 곱해 LHV 입열 기준으로 환산하고,
    나머지를 조성(잠열 제외) 항으로 둔다.
  - HHV 기준: Table S5의 조성·온도·크레딧 비율을 그대로 적용한다.
사용법: python bridge_calc.py 튜닝최적화_v6b.xlsx  →  bridge_results.csv
"""
import csv
import math
import sys
from pathlib import Path

import openpyxl

XLSX = Path(sys.argv[1])
HERE = Path(__file__).parent

wb = openpyxl.load_workbook(XLSX, data_only=True)
rows = list(wb["18_전체프로파일"].iter_rows(values_only=True))
P = {r[0]: dict(zip(rows[0], r)) for r in rows[1:]}

KC, KA = 23.463 / 22.190, 22.415 / 18.548          # HHV/LHV, 보충자료 S1
X_ACT = {20: 0.19969, 50: 0.49952, 100: 1.0}        # 25°C 기준 실제 LHV 입열분율
S5 = {20: (2.554, 0.245, 0.016), 50: (6.127, 0.669, 0.038), 100: (11.483, 1.451, 0.068)}  # 조성, 온도, 크레딧 %p


def kappa(x):
    """혼합연료 HHV/LHV 입열비 (보충자료 식 S13). x는 실제 LHV 입열분율."""
    return x * KA + (1 - x) * KC


def factors(name, x, basis):
    d = P[name]
    k = kappa(x) if basis == "HHV" else 1.0
    return {"B": d["blr_LHV"] / 100 / k, "C": d["cyc"] / 100, "A": d["net"] / d["gross"]}


def lmdi(n1, x1, n2, x2, basis):
    a, b = factors(n1, x1, basis), factors(n2, x2, basis)
    na, nb = (math.prod(a.values()), math.prod(b.values()))
    w = (nb - na) / math.log(nb / na) * 100
    return {f: w * math.log(b[f] / a[f]) for f in a}, (nb - na) * 100


out = []
for r in (20, 50, 100):
    base = f"NR_NH3_{r}%"
    tun = "_Tuning" if r == 50 else "_tuning"
    chain = [base, base + "_PH by FG", base + "_PH by FG,EXT7", base + "_PH by FG,EXT7" + tun]
    x = X_ACT[r]
    for basis in ("LHV", "HHV"):
        c, tot = lmdi("NR", 0.0, base, x, basis)
        comp, temp, cred = S5[r]
        if basis == "LHV":
            dB = P["NR"]["blr_LHV"] - P[base]["blr_LHV"]
            sT, sCr = temp * kappa(x) / dB, cred * kappa(x) / dB
        else:
            s = comp + temp + cred
            sT, sCr = temp / s, cred / s
        out.append(dict(ratio=r, basis=basis, kind="저하", item="보일러·배가스온도", value=c["B"] * sT))
        out.append(dict(ratio=r, basis=basis, kind="저하", item="보일러·조성·기타", value=c["B"] * (1 - sT)))
        out.append(dict(ratio=r, basis=basis, kind="저하", item="증기사이클", value=c["C"]))
        out.append(dict(ratio=r, basis=basis, kind="저하", item="소내동력", value=c["A"]))
        out.append(dict(ratio=r, basis=basis, kind="저하", item="합계", value=tot))
        rec = {"B": 0.0, "C": 0.0, "A": 0.0}
        rtot = 0.0
        for n1, n2, step in zip(chain[:-1], chain[1:], ("배가스 열회수", "추기예열", "운전튜닝")):
            c, t = lmdi(n1, x, n2, x, basis)
            for f in rec:
                rec[f] += c[f]
            rtot += t
            for f, lab in (("B", "보일러"), ("C", "증기사이클"), ("A", "소내동력")):
                out.append(dict(ratio=r, basis=basis, kind=f"회복:{step}", item=lab, value=c[f]))
        for f, lab in (("B", "보일러"), ("C", "증기사이클"), ("A", "소내동력")):
            out.append(dict(ratio=r, basis=basis, kind="회복", item=lab, value=rec[f]))
        out.append(dict(ratio=r, basis=basis, kind="회복", item="합계", value=rtot))

with open(HERE / "bridge_results.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=["ratio", "basis", "kind", "item", "value"])
    w.writeheader()
    for o in out:
        w.writerow({**o, "value": f"{o['value']:.4f}"})

for o in out:
    if o["kind"] in ("저하", "회복"):
        print(o["ratio"], o["basis"], o["kind"], o["item"], f"{o['value']:+.3f}")
