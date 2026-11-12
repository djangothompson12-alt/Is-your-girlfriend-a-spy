# Is Your Girlfriend a Spy? (joke paper, 12 Nov 2026)

- paper/paper.pdf, paper/paper.tex: the paper (5 pages)
- code/model.py: model + 100k-draw Monte Carlo, writes code/results.json
- code/figs.py: figures into figures/

Run: `cd code && python3 model.py && python3 figs.py`, then `cd ../paper && pdflatex paper.tex` twice.

Real inputs: FBI ~5,000 active CI cases (Wray, 2020), 258.3M US adults (Census 2020), 4.03M clearance holders (ODNI FY2017), NWS lightning odds, Epic token odds.
Assumed inputs (labelled in paper): romance share of cases (5%), split across tiers, CEO inner-circle sizes (9 execs, 5 family, 2 assistants per CEO), red-flag likelihood ratios.

Safety notes: the news story is cited only as unconfirmed reporting (AP via Boston Globe). The woman named in reports is NOT named in the paper. Keep it that way in any TikTok captions too.

AI (Claude) helped write the code, check sources and draft the text.
