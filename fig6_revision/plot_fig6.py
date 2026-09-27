"""Fig. 6 수정안.

(a) 과잉공기율 응답, (b) 기수분리기 출구 온도 바이어스 응답,
(c) BZR에 따른 순효율 변화, (d) BZR에 따른 분무비.

사용법: python plot_fig6.py [Figure_6_data.csv] [BZR_20_50_100_results.csv]
출력: fig6_revised.png / .pdf / .svg (스크립트와 같은 폴더)
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
CSV = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "Figure_6_data.csv"
BZR_CSV = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "BZR_20_50_100_results.csv"

# 논문 본문 글꼴로 바꿀 때는 두 번째 항목(한글 글꼴)만 교체 (예: "Malgun Gothic")
plt.rcParams.update({
    "font.family": ["DejaVu Sans", "WenQuanYi Zen Hei"],
    "font.size": 8.5,
    "axes.titlesize": 9,
    "axes.labelsize": 8.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#52514e",
    "axes.linewidth": 0.8,
    "xtick.color": "#52514e",
    "ytick.color": "#52514e",
    "axes.grid": True,
    "grid.color": "#e6e5e0",
    "grid.linewidth": 0.6,
    "axes.unicode_minus": True,
})

TEXT = "#0b0b0b"
MUTED = "#52514e"
# 혼소율 → (범례명, 색, 과잉공기율 하한 %, 대표 ΔT K, 대표점 분무비 %)
CASES = {
    "NH₃ 20%":  dict(pct=20, color="#2a78d6", xmin=12.08, dt_rep=-3.20,  spray=6.65, panel="(b)"),
    "NH₃ 50%":  dict(pct=50, color="#eb6834", xmin=9.42,  dt_rep=-7.80,  spray=6.63, panel="(c)"),
    "NH₃ 100%": dict(pct=100, color="#1baf7a", xmin=5.00,  dt_rep=-16.75, spray=6.42, panel="(d)"),
}

df = pd.read_csv(CSV)
bzr = pd.read_csv(BZR_CSV)
BZR_REP = 0.95

fig, ((ax_a, ax_b), (ax_c, ax_d)) = plt.subplots(
    2, 2, figsize=(7.2, 6.2),
    gridspec_kw=dict(width_ratios=[1, 1.15], wspace=0.42, hspace=0.42),
)

# ---------------------------------------------------------------- (a)
line = df[df.panel.str.startswith("(a)") & (df.kind == "line")]
for name, c in CASES.items():
    g = line[line.series == name].sort_values("x")
    below = g[g.x <= c["xmin"] + 1e-6]
    above = g[g.x >= c["xmin"] - 1e-6]
    ax_a.plot(below.x, below.y, color=c["color"], lw=1.6, ls=(0, (2.5, 2)))
    ax_a.plot(above.x, above.y, color=c["color"], lw=2.0)
    rep = g.loc[(g.x - c["xmin"]).abs().idxmin()]
    ax_a.plot(rep.x, rep.y, "s", ms=6.5, mfc="white", mec=c["color"], mew=1.6, zorder=5)
    end = g.iloc[-1]
    ax_a.annotate(name, (end.x, end.y), xytext=(4, 0), textcoords="offset points",
                  va="center", fontsize=8, color=TEXT)

ax_a.set_xlim(1.5, 16.2)
ax_a.set_xticks([2, 5, 8, 11, 14])
ax_a.set_xlabel("과잉공기율 (%)")
ax_a.set_ylabel("LHV 순효율 (%)")
ax_a.set_title("(a) 과잉공기율 응답", loc="left", color=TEXT)
ax_a.text(0.97, 0.97, "실선: 하한 이상 · 점선: 하한 미만(민감도)\n□ 대표 운전점(=혼소율별 하한)",
          transform=ax_a.transAxes, fontsize=7, color=MUTED, va="top", ha="right")

# ---------------------------------------------------------------- (b)
for name, c in CASES.items():
    sub = df[df.panel.str.startswith(c["panel"]) & df.series.str.startswith("제약 충족")]
    col = sub[(sub.x - c["xmin"]).abs() < 1e-3].sort_values("y")
    eta_rep = col.loc[(col.y - c["dt_rep"]).abs().idxmin(), "z"]
    d = (col.z - eta_rep) * 1e3  # 10^-3 %p
    ax_b.plot(col.y, d, "-o", color=c["color"], lw=1.6, ms=4.5, mec="white", mew=0.8)
    ax_b.plot(c["dt_rep"], 0, "s", ms=7.5, mfc="white", mec=c["color"], mew=1.6, zorder=5)
    best = col.loc[col.z.idxmax()]
    ax_b.plot(best.y, (best.z - eta_rep) * 1e3, "*", ms=11, mfc="white", mec=c["color"],
              mew=1.2, zorder=6)
    right = c["pct"] == 100  # 100%는 y축에 붙으므로 별 오른쪽에 표기
    ax_b.annotate(name, (best.y, (best.z - eta_rep) * 1e3),
                  xytext=(9, 0) if right else (0, 9), textcoords="offset points",
                  ha="left" if right else "center", va="center" if right else "bottom",
                  fontsize=8, color=TEXT)

ax_b.axhline(0, color=MUTED, lw=0.8, zorder=1)
ax_b.set_xlim(-19, -1)
ax_b.set_ylim(-5, 10.5)
ax_b.set_yticks(range(-4, 11, 2))
ax_b.set_xticks([-18, -16, -14, -12, -10, -8, -6, -4, -2])
ax_b.set_xlabel("기수분리기 출구 온도 바이어스 ΔT (K)")
ax_b.set_ylabel("대표점 대비 순효율 차 (10⁻³ %p)")
ax_b.set_title("(b) 온도 바이어스 응답 (과잉공기율 하한, BZR 0.95)", loc="left", color=TEXT)

# ---------------------------------------------------------------- (c), (d)
for ax in (ax_c, ax_d):
    ax.axvspan(BZR_REP, 1.0125, color="#f0efeb", zorder=0, lw=0)
    ax.axvline(BZR_REP, color=MUTED, lw=0.8, ls=(0, (3, 2)), zorder=1)
    ax.set_xlim(0.8375, 1.0125)
    ax.set_xticks([0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1.0])
    ax.set_xticklabels(["0.85", "", "0.90", "", "0.95", "", "1.00"])
    ax.set_xlabel("버너존 공기비 BZR (–)")
    ax.text(0.9815, 0.03, "민감도\n(BZR > 0.95)", transform=ax.get_xaxis_transform(),
            ha="center", va="bottom", fontsize=7, color=MUTED)

ax_d.axhspan(6.0, 7.0, color="#dcdad3", alpha=0.6, zorder=0, lw=0)
ax_d.text(0.8425, 6.05, "분무 목표 6–7%", fontsize=7, color=MUTED, va="bottom")

for name, c in CASES.items():
    g = bzr[bzr.NH3_LHV_pct == c["pct"]].sort_values("BZR")
    rep = g[(g.BZR - BZR_REP).abs() < 1e-6].iloc[0]
    d = g.delta_LHV_vs_BZR095_pp * 1e3
    kw = dict(color=c["color"], lw=1.6, ms=4.5, mec="white", mew=0.8)
    ax_c.plot(g.BZR, d, "-o", **kw)
    ax_d.plot(g.BZR, g.spray_pct, "-o", **kw)
    ax_c.plot(BZR_REP, 0, "s", ms=7, mfc="white", mec=c["color"], mew=1.6, zorder=5)
    ax_d.plot(BZR_REP, rep.spray_pct, "s", ms=7, mfc="white", mec=c["color"], mew=1.6, zorder=5)
    last = g.iloc[-1]
    dy = {20: 5, 50: -5}.get(c["pct"], 0)
    ax_d.annotate(name, (last.BZR, last.spray_pct), xytext=(5, dy), textcoords="offset points",
                  va="center", fontsize=7.5, color=TEXT, annotation_clip=False)

# (c) 우측 라벨: BZR 1.00 값이 세 혼소율 모두 28–31이라 겹치므로 범례로 대신
ax_c.legend([plt.Line2D([], [], color=c["color"], lw=1.6, marker="o", ms=4, mec="white")
             for c in CASES.values()], list(CASES), loc="upper left", fontsize=7,
            frameon=False, handlelength=1.8)
ax_c.axhline(0, color=MUTED, lw=0.8, zorder=1)
ax_c.set_ylabel("BZR 0.95 대비 순효율 차 (10⁻³ %p)")
ax_c.set_title("(c) BZR 응답: 순효율", loc="left", color=TEXT)
ax_d.set_ylabel("과열기 분무비 (주증기 대비, %)")
ax_d.set_ylim(5.2, 7.8)
ax_d.set_title("(d) BZR 응답: 분무비", loc="left", color=TEXT)
ax_b.text(0.97, 0.04, "□ 대표 운전점 (분무비 6–7%)\n☆ 제약 내 격자 최고점",
          transform=ax_b.transAxes, ha="right", va="bottom", fontsize=7, color=MUTED)

for ext in ("png", "pdf", "svg"):
    fig.savefig(HERE / f"fig6_revised.{ext}", dpi=400, bbox_inches="tight")
print("saved", HERE / "fig6_revised.png")
