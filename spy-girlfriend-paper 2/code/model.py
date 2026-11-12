"""Probability your girlfriend is a spy. Access-weighted base-rate model.

Real inputs (cited in the paper):
  ~5,000 active FBI counterintelligence cases (Wray, 7 Jul 2020)
  258.3M US adults (Census 2020)
  ~2.8M Confidential/Secret + ~1.3M Top Secret clearance holders (ODNI FY2017, 4.03M total)
  500 Fortune 500 CEOs
Assumed inputs (labelled ASSUMED, varied in the Monte Carlo):
  share of cases that run through a romantic relationship
  how those romance cases are split across access tiers
"""
import json, numpy as np

rng = np.random.default_rng(2026)

CASES = 5000
TIERS = {               # population, assumed share of romance cases
    "Regular person":            (258.3e6 - 4.03e6 - 8000, 0.12),
    "Secret clearance":          (2.72e6, 0.36),
    "Top Secret clearance":      (1.31e6, 0.40),
    "Fortune 500 senior exec":   (4500,   0.04),   # ~9 C-suite per firm, ASSUMED
    "Family of a Fortune 500 CEO": (2500, 0.03),   # ~5 close family per CEO, ASSUMED
    "CEO's assistant / chief of staff": (1000, 0.03),  # ~2 per CEO, ASSUMED
    "Fortune 500 CEO":           (500,    0.02),
}
ROMANCE_SHARE = 0.05    # ASSUMED

def point():
    out = {}
    for k, (pop, share) in TIERS.items():
        out[k] = CASES * ROMANCE_SHARE * share / pop
    return out

def mc(n=100_000):
    names = list(TIERS)
    pops = np.array([TIERS[k][0] for k in names])
    base = np.array([TIERS[k][1] for k in names])
    cases = rng.uniform(2500, 10000, n)                  # cases != people; wide band
    romance = np.exp(rng.uniform(np.log(0.01), np.log(0.20), n))  # 1% to 20%, log-uniform
    shares = rng.dirichlet(base * 20, n)                 # jitter the tier split
    p = (cases * romance)[:, None] * shares / pops[None, :]
    return {k: {"median": float(np.median(p[:, i])),
                "lo": float(np.percentile(p[:, i], 5)),
                "hi": float(np.percentile(p[:, i], 95))} for i, k in enumerate(names)}

# Red flags: ASSUMED likelihood ratios P(flag | spy) / P(flag | not spy).
FLAGS = {
    "Asks what you do at work":            1.05,
    "Uses a VPN":                          1.3,
    "Is 'mysterious'":                     1.2,
    "Has two phones":                      3.0,
    "Very interested in your security clearance": 25.0,
    "Asked for your laptop password on date one": 40.0,
}

def posterior(prior, lrs):
    odds = prior / (1 - prior)
    for lr in lrs:
        odds *= lr
    return odds / (1 + odds)

if __name__ == "__main__":
    pt, m = point(), mc()
    all_lr = list(FLAGS.values())
    post = {k: posterior(pt[k], all_lr) for k in pt}
    weak = {k: posterior(pt[k], all_lr[:3]) for k in pt}
    res = {"point": pt, "mc": m, "flags": FLAGS,
           "posterior_all_flags": post, "posterior_weak_flags": weak,
           "comparisons": {"Lightning strike in a year (NWS)": 1/1_222_000,
                           "Fortnite Pirate Token per chest (Epic)": 1/137_500}}
    for k in pt:
        print(f"{k:24s} 1 in {1/pt[k]:>13,.0f}   90% 1 in {1/m[k]['hi']:,.0f} to 1 in {1/m[k]['lo']:,.0f}"
              f"   weak flags 1 in {1/weak[k]:,.0f}   all flags {post[k]:.2%}")
    json.dump(res, open("results.json", "w"), indent=2)
