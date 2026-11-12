import json, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from model import posterior
plt.rcParams.update({"font.family":"serif","font.serif":["cmr10"],"mathtext.fontset":"cm",
                     "axes.formatter.use_mathtext":True,"font.size":10,
                     "axes.spines.top":False,"axes.spines.right":False})
r = json.load(open("results.json"))
names = list(r["point"]); y = np.arange(len(names))[::-1]
pt = np.array([r["point"][k] for k in names])
lo = np.array([r["mc"][k]["lo"] for k in names]); hi = np.array([r["mc"][k]["hi"] for k in names])
fig, ax = plt.subplots(figsize=(6.4,3.8))
ax.hlines(y, lo, hi, color="#7a8fa6", lw=4, alpha=.6)
ax.plot(pt, y, "o", color="#1f3b5a", ms=6, zorder=3)
for yy, p in zip(y, pt): ax.annotate(f"1 in {1/p:,.0f}", (p, yy), xytext=(0,7), textcoords="offset points", ha="center", fontsize=8)
for lab, v, c, ty, ha in [("Struck by lightning this year", r["comparisons"]["Lightning strike in a year (NWS)"], "#b5651d", y.max()+0.5, "right"),
                  ("Pirate Token, per chest", r["comparisons"]["Fortnite Pirate Token per chest (Epic)"], "#2e7d32", y.max()+0.5, "left")]:
    ax.axvline(v, ls="--", lw=1, color=c); ax.text(v*(0.85 if ha=="right" else 1.15), ty, lab, color=c, fontsize=7.5, ha=ha)
ax.set_xscale("log"); ax.set_yticks(y); ax.set_yticklabels(names); ax.set_ylim(-0.6, y.max()+0.8)
ax.set_xlabel("P(your girlfriend is a spy)  [dot: point estimate; bar: 90% interval]")
fig.tight_layout(); fig.savefig("../figures/fig_ladder.pdf"); fig.savefig("../figures/fig_ladder.png", dpi=200)

flags = list(r["flags"].items())
fig, ax = plt.subplots(figsize=(6.2,2.8))
for k, c in [("Regular person","#1f3b5a"),("Top Secret clearance","#b5651d"),("Family of a Fortune 500 CEO","#2e7d32")]:
    ps = [r["point"][k]] + [posterior(r["point"][k], [v for _,v in flags[:i+1]]) for i in range(len(flags))]
    ax.plot(range(len(ps)), ps, "o-", color=c, lw=1.6, ms=4, label=k)
ax.set_yscale("log"); ax.set_xticks(range(len(flags)+1))
ax.set_xticklabels(["Prior"]+[f"+{i+1}" for i in range(len(flags))])
ax.set_xlabel("Red flags added, in the order of Table 2"); ax.set_ylabel("Posterior P(spy)")
ax.axhline(0.5, color="grey", lw=.8, ls=":"); ax.text(0,0.25,"coin flip",fontsize=7.5,color="grey")
ax.legend(frameon=False, fontsize=8, loc="lower center", bbox_to_anchor=(0.5,1.0), ncol=3)
fig.tight_layout(); fig.savefig("../figures/fig_flags.pdf"); fig.savefig("../figures/fig_flags.png", dpi=200)
