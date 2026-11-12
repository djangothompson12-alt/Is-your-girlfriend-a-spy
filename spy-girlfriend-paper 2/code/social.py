"""9:16 carousel slides for TikTok / Instagram.   python social.py"""
import json, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.serif":["cmr10"],"mathtext.fontset":"cm","axes.unicode_minus":False})
r = json.load(open("results.json")); P = r["point"]
BG, RED, BLUE, GREY = "#fbfaf6", "#b3262b", "#1f3b5a", "0.35"
OUT = "../social/"

def slide(n, name):
    fig = plt.figure(figsize=(5.4, 9.6), dpi=200, facecolor=BG)
    fig.text(0.94, 0.03, f"{n}/7", ha="right", fontsize=10, color=GREY)
    fig.text(0.06, 0.03, "Thompson (2026), Is Your Girlfriend a Spy?", fontsize=8.5, color=GREY, style="italic")
    return fig, OUT + f"{n:02d}_{name}.png"

def save(fig, path): fig.savefig(path, facecolor=BG); plt.close(fig)
def one_in(p):
    n = 1/p
    if n >= 1e6: return f"1 in {n/1e6:.1f} million"
    if n >= 10000: return f"1 in {round(n, -2):,.0f}"
    if n >= 1000: return f"1 in {round(n, -2):,.0f}"
    return f"1 in {n:,.0f}"

# 1 hook
fig, p = slide(1, "hook")
fig.text(0.5, 0.72, "Is your\ngirlfriend\na spy?", ha="center", va="center", fontsize=58, family="cmb10", linespacing=1.05)
fig.text(0.5, 0.47, "I wrote an actual 5-page\nresearch paper on it.", ha="center", fontsize=19, linespacing=1.4)
fig.text(0.5, 0.33, "Spoiler: it depends\nwho your dad is.", ha="center", fontsize=21, color=RED, family="cmb10", linespacing=1.3)
fig.text(0.5, 0.15, "real FBI, Census and clearance data\n100,000 simulations", ha="center", fontsize=12.5, color=GREY, style="italic", linespacing=1.5)
save(fig, p)

# 2 regular person
fig, p = slide(2, "you")
fig.text(0.5, 0.86, "If you're just a normal guy", ha="center", fontsize=22, family="cmb10")
fig.text(0.5, 0.70, "1 in", ha="center", fontsize=30)
fig.text(0.5, 0.58, f"{1/P['Regular person']/1e6:.1f} million", ha="center", fontsize=50, family="cmb10", color=BLUE)
fig.text(0.5, 0.42, "You're 7x more likely to get\nstruck by lightning this year.", ha="center", fontsize=18, linespacing=1.4)
fig.text(0.5, 0.25, "She's not a spy bro.\nYou're just not that interesting.", ha="center", fontsize=20, color=RED, family="cmb10", linespacing=1.35)
save(fig, p)

# 3 ladder
fig, p = slide(3, "ladder")
fig.text(0.5, 0.88, "Now it gets bad", ha="center", fontsize=26, family="cmb10")
fig.text(0.5, 0.845, "odds your partner is a spy, by who you are", ha="center", fontsize=12, style="italic", color=GREY)
rows = [("Normal person", "Regular person"), ("Secret clearance", "Secret clearance"),
        ("Top Secret clearance", "Top Secret clearance"), ("Fortune 500 exec", "Fortune 500 senior exec"),
        ("CEO's family", "Family of a Fortune 500 CEO"), ("CEO's assistant", "CEO's assistant / chief of staff"),
        ("The CEO", "Fortune 500 CEO")]
for i, (lab, k) in enumerate(rows):
    y = 0.76 - i * 0.085; hot = i >= 4
    fig.text(0.08, y, lab, fontsize=17, family="cmb10" if hot else "cmr10")
    fig.text(0.92, y, one_in(P[k]), fontsize=18, ha="right", family="cmb10", color=RED if hot else BLUE)
fig.text(0.5, 0.11, "Being NEAR power is nearly\nas bad as having it.", ha="center", fontsize=18, linespacing=1.35)
save(fig, p)

# 4 the assistant
fig, p = slide(4, "assistant")
fig.text(0.5, 0.80, "Why are the CEO's kids\nso cooked?", ha="center", fontsize=26, family="cmb10", linespacing=1.2)
fig.text(0.5, 0.48, "They hear the calls.\nThey're on the home Wi-Fi.\nThey know where the laptop lives.\n\nNobody ever trained them to be suspicious.\nThe CEO has a whole security team.", ha="center", fontsize=17, linespacing=1.5)
fig.text(0.5, 0.20, "Being a CEO's kid is about 25,000x\nriskier than being a normal kid.\nTough luck, rich kids.", ha="center", fontsize=17.5, color=RED, family="cmb10", linespacing=1.35)
save(fig, p)

# 5 red flags
fig, p = slide(5, "red_flags")
fig.text(0.5, 0.88, "But she has red flags...", ha="center", fontsize=26, family="cmb10")
fig.text(0.5, 0.74, "She's mysterious and uses a VPN", ha="center", fontsize=16)
fig.text(0.5, 0.685, f"normal you: {one_in(r['posterior_weak_flags']['Regular person'])}", ha="center", fontsize=19, color=BLUE, family="cmb10")
fig.text(0.5, 0.56, "She has two phones, asks about your\nclearance AND wanted your laptop\npassword on the first date", ha="center", fontsize=16, linespacing=1.35)
fig.text(0.5, 0.48, f"normal you: {one_in(r['posterior_all_flags']['Regular person'])}", ha="center", fontsize=19, color=BLUE, family="cmb10")
fig.text(0.5, 0.42, f"CEO's kid: {r['posterior_all_flags']['Family of a Fortune 500 CEO']:.0%}", ha="center", fontsize=24, color=RED, family="cmb10")
fig.text(0.5, 0.29, "Same red flags.\nCompletely different answer.", ha="center", fontsize=17, linespacing=1.4)
fig.text(0.5, 0.13, "It's not her passport.\nIt's your dad's job.", ha="center", fontsize=20, family="cmb10", color=RED, linespacing=1.35)
save(fig, p)

# 6 conclusion
fig, p = slide(6, "conclusion")
fig.text(0.5, 0.80, "Conclusion", ha="center", fontsize=30, family="cmb10")
fig.text(0.5, 0.55, "Do not go through her phone.", ha="center", fontsize=22, family="cmb10")
fig.text(0.5, 0.42, "Your odds of ruining the relationship\nare way higher than 1 in 8.5 million.", ha="center", fontsize=17, linespacing=1.4)
fig.text(0.5, 0.25, "Unless your mum runs a\nFortune 500 company.\nThen maybe ask a few questions.", ha="center", fontsize=18, color=RED, linespacing=1.4)
save(fig, p)

# 7 CTA
fig, p = slide(7, "comment")
fig.text(0.5, 0.70, "Comment your job\n(or your mum's)", ha="center", fontsize=28, family="cmb10", linespacing=1.2)
fig.text(0.5, 0.56, "and I'll tell you the odds\nyour partner is a spy.", ha="center", fontsize=19, linespacing=1.4)
fig.text(0.5, 0.30, "A joke with real numbers. Not about\nany real person. Some inputs are guesses,\nall labelled in the paper.\nMade with help from AI.", ha="center", fontsize=11.5, color=GREY, linespacing=1.5)
save(fig, p)
