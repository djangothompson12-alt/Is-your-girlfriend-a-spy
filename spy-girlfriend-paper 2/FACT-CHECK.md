# Final fact + plagiarism check (12 Nov 2026), on Django's exported PDF

## Must fix
1. **Clearance numbers (ODNI FY2017, Table 1.3).** Total eligible 4,030,625 = 2,720,832 Confidential/Secret + 1,309,793 Top Secret. The paper said 2.8M / 1.3M and the model used 2.77M / 1.26M. Model rerun with 2.72M / 1.31M. Text changes:
   - "about 2.8 million at Confidential or Secret" -> "about 2.7 million at Confidential or Secret"
   - Abstract: "1 in 12,600 with Top Secret clearance" -> "1 in 13,100"
   - Table 1, Secret row: 2.8 million | 1 in 31,000 | 1 in 156,000 to 1 in 6,300 -> 2.7 million | 1 in 30,000 | 1 in 154,000 to 1 in 6,200
   - Table 1, Top Secret row: 1 in 12,600 | 1 in 62,000 to 1 in 2,600 -> 1 in 13,100 | 1 in 65,000 to 1 in 2,700
   - Red flags: "Top Secret clearance ends up at 28%" -> "27%"
   - Swap Figure 1 and Figure 2 for the new figures/fig_ladder.png and figures/fig_flags.png (old Fig 1 shows 1 in 30,778 and 1 in 12,600).
   - Nothing else moves (regular, exec, family, assistant, CEO, sensitivity claims all unchanged).
2. **AI disclosure.** PDF says "I used AI to help with the code and checking sources." AI also drafted most of the text, so for a preprint it should say drafting too, e.g. "I used AI (Claude) to help with the code, checking sources and drafting the text."

## Should fix
3. Figure captions lost their "Figure 1:" / "Figure 2:" labels in the Google Doc export, but the text refers to "Figure 1" and "Figure 2". Add the labels back.
4. Table captions also lost "Table 1"/"Table 2" labels; text refers to "Table 1".
5. Abstract grammar: "1 in 333 if you're a CEO's family" -> "if you're in a CEO's family".
6. "CEOs at least get warned" is a claim with no source. Suggest "CEOs at least have security teams" (already said earlier in the paper).
7. "He also does every product launch in the same black leather jacket": hyperbole is fine in satire; "almost every" is safer.

## Checked and fine
- AP via Boston Globe, 12 Nov 2026: headline, NYT attribution and "could not independently confirm" all match. Paper's wording (reports, unconfirmed, nobody charged, China denies) matches the article. Note: other outlets report Huang has admitted an affair; the paper doesn't claim otherwise.
- CompaniesMarketCap: Nvidia #2 worldwide, $4.195T at 11 Nov 2026 close; Apple #1 (Motley Fool agrees).
- Wray, Hudson Institute, 7 Jul 2020: "nearly 5,000 active FBI counterintelligence cases", almost half China-related. Confirmed by NBC, Nextgov, Defense One and others (FBI page itself blocked automated reading).
- Census 2020 adults: 258.3M. Correct.
- NWS: 1 in 1,222,000 per year (2009-2018 averages). Correct.
- Epic token 1 in 137,500: matches the Fortnite paper's sources.
- Kahneman & Tversky 1973, Psych Review 80(4):237-251; Gigerenzer et al. 2007, PSPI 8(2):53-96: correct.
- CSIS "Survey of Chinese Espionage in the United States Since 2000": exists.
- Arithmetic: 7x lightning (6.9), 62x token (61.6), 254M regular, 25,000x CEO's son (25,450), 1 in 5.2M / 1 in 1,700 / >90% red-flag figures, sensitivity claims (10x min, ~300x median, 91%) all re-run and match.

## Plagiarism / originality
- All prose was written new in this project. The only quoted text is Wray's phrase, which is in quotes and cited.
- Web searches for a paper or post estimating "probability your girlfriend is a spy" with base rates found nothing similar, only news coverage of the Huang story and generic honey-trap explainers.
- The method (base rates + likelihood ratios / Bayes) is standard textbook stats and is credited via Kahneman & Tversky and Gigerenzer.
- I can't run Turnitin. If the preprint server runs a similarity check, expect hits only on the reference list and the Wray quote.
