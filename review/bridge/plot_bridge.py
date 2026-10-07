"""저하–회복 인자 분해 그림 (Fig. 7 개편안의 (b)·(c) 패널).

입력: bridge_calc.py가 만든 bridge_results.csv
출력: fig7_bridge.png / .pdf / .svg
"""
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).parent
plt.rcParams.update({
    "font.family": ["DejaVu Sans", "WenQuanYi Zen Hei"],
    "font.size": 8.5, "axes.titlesize": 9, "axes.labelsize": 8.5,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": "#52514e", "xtick.color": "#52514e", "ytick.color": "#52514e",
    "axes.grid": True, "axes.grid.axis": "y", "grid.color": "#e6e5e0", "grid.linewidth": 0.6,
    "axes.unicode_minus": True,
})
TEXT, MUTED = "#0b0b0b", "#52514e"
COL = {"보일러·배가스온도": "#2a78d6", "보일러·조성·기타": "#9cc3f0", "보일러": "#2a78d6",
       "증기사이클": "#eb6834", "소내동력": "#eda100"}

D = defaultdict(dict)
with open(HERE / "bridge_results.csv", encoding="utf-8-sig") as fh:
    for r in csv.DictReader(fh):
        if r["kind"] in ("저하", "회복"):
            D[(int(r["ratio"]), r["basis"], r["kind"])][r["item"]] = float(r["value"])

LOSS = ["보일러·배가스온도", "보일러·조성·기타", "증기사이클", "소내동력"]
REC = ["보일러", "증기사이클", "소내동력"]

fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.3), gridspec_kw=dict(wspace=0.28))
for ax, basis, title in ((axes[0], "LHV", "(b) LHV 기준"), (axes[1], "HHV", "(c) HHV 기준")):
    xt, xl = [], []
    for i, r in enumerate((20, 50, 100)):
        for j, (kind, items) in enumerate((("저하", LOSS), ("회복", REC))):
            x = i * 2.6 + j * 1.0
            vals = D[(r, basis, kind)]
            pos = neg = 0.0
            for it in items:
                v = vals[it]
                bottom = pos if v >= 0 else neg
                ax.bar(x, v, 0.78, bottom=bottom, color=COL[it], edgecolor="white", linewidth=0.8)
                if v >= 0:
                    pos += v
                else:
                    neg += v
            tot = vals["합계"]
            ax.plot(x, tot, "D", ms=5, mfc="white", mec=TEXT, mew=1.1, zorder=5)
            ax.annotate(f"{tot:+.2f}".replace("-", "−"), (x, pos if tot >= 0 else neg), xytext=(0, 3 if tot >= 0 else -3),
                        textcoords="offset points", ha="center", va="bottom" if tot >= 0 else "top",
                        fontsize=7.5, color=TEXT)
            xt.append(x); xl.append(kind)
        ax.text(i * 2.6 + 0.5, 1.0, f"NH₃ {r}%", transform=ax.get_xaxis_transform(),
                ha="center", va="bottom", fontsize=8, color=TEXT)
    ax.axhline(0, color=MUTED, lw=0.8)
    ax.set_xticks(xt); ax.set_xticklabels(xl)
    ax.set_title(title, loc="left", color=TEXT, pad=14)
    ax.set_ylabel(f"순효율 변화 ({basis}, %p)")

axes[0].set_ylim(-1.75, 2.15)
axes[1].set_ylim(-6.9, 2.4)
handles = [plt.Rectangle((0, 0), 1, 1, color=COL[k]) for k in
           ("보일러·배가스온도", "보일러·조성·기타", "증기사이클", "소내동력")]
labels = ["보일러: 배가스온도 (회복 막대는 보일러 전체)", "보일러: 조성·기타", "증기사이클", "소내동력"]
handles.append(plt.Line2D([], [], marker="D", ls="", mfc="white", mec=TEXT, ms=5))
labels.append("합계")
fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, fontsize=7.5,
           bbox_to_anchor=(0.5, -0.12))
for ext in ("png", "pdf", "svg"):
    fig.savefig(HERE / f"fig7_bridge.{ext}", dpi=400, bbox_inches="tight")
print("saved")
