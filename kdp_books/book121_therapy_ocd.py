from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "OCD THERAPY WORKBOOK"
subtitle = "ERP Exercises for Breaking the Cycle"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 20)
pdf.add_centered_text(510, subtitle, 'F4', 14)
pdf.add_centered_text(440, "Evidence-Based Exposure & Response Prevention", 'F4', 12)
pdf.add_centered_text(420, "Exercises to Reclaim Your Life from OCD", 'F4', 12)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 12)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(520, "No part of this publication may be reproduced without permission.", 'F4', 9)
pdf.add_centered_text(490, "This workbook is for educational purposes and is not a substitute", 'F4', 9)
pdf.add_centered_text(476, "for professional mental health treatment.", 'F4', 9)

# Page 3: What is OCD
pdf.new_page()
pdf.add_centered_text(750, "WHAT IS OCD?", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
lines = [
    "Obsessive-Compulsive Disorder (OCD) is a neurobiological condition",
    "affecting approximately 1 in 40 adults. It is NOT about being neat",
    "or organized. OCD involves:",
    "",
    "OBSESSIONS: Unwanted, intrusive thoughts, images, or urges that",
    "cause significant distress. These feel 'sticky' - you cannot simply",
    "dismiss them. They are EGO-DYSTONIC, meaning they go AGAINST your",
    "values and desires.",
    "",
    "COMPULSIONS: Repetitive behaviors or mental acts performed to",
    "reduce the anxiety caused by obsessions. They provide temporary",
    "relief but STRENGTHEN the OCD cycle long-term.",
    "",
    "KEY FACTS:",
    "- OCD is NOT your fault - it is a brain-based condition",
    "- Having a thought does NOT mean you want it or will act on it",
    "- Thought = just a thought, NOT a fact or prediction",
    "- ERP (Exposure & Response Prevention) is the gold-standard treatment",
    "- Recovery is possible - most people improve significantly with ERP",
    "",
    "THIS WORKBOOK WILL HELP YOU:",
    "1. Understand your specific OCD patterns",
    "2. Build an ERP hierarchy (fear ladder)",
    "3. Practice systematic exposures",
    "4. Track your progress over 12 weeks",
    "5. Develop relapse prevention strategies",
    "",
    "IMPORTANT: This workbook works best alongside a therapist trained",
    "in ERP. If you do not have one, look for an OCD specialist at",
    "iocdf.org or nocd.com."
]
for line in lines:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 4: The OCD Cycle Diagram
pdf.new_page()
pdf.add_centered_text(750, "THE OCD CYCLE", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 710
pdf.add_text(50, y, "Understanding the cycle is the first step to breaking it:", 'F4', 11)
y -= 40
# Draw cycle as text-based diagram
pdf.add_centered_text(y, "TRIGGER", 'F2', 13)
y -= 20
pdf.add_centered_text(y, "(Internal or external event)", 'F4', 9)
y -= 30
pdf.add_centered_text(y, "|", 'F1', 14)
pdf.add_centered_text(y-12, "v", 'F1', 14)
y -= 40
pdf.add_centered_text(y, "OBSESSION (Intrusive thought/image/urge)", 'F2', 12)
y -= 20
pdf.add_centered_text(y, "Causes intense ANXIETY / DISTRESS", 'F4', 10)
y -= 30
pdf.add_centered_text(y, "|", 'F1', 14)
pdf.add_centered_text(y-12, "v", 'F1', 14)
y -= 40
pdf.add_centered_text(y, "COMPULSION (Ritual / avoidance / reassurance)", 'F2', 12)
y -= 20
pdf.add_centered_text(y, "Provides TEMPORARY relief", 'F4', 10)
y -= 30
pdf.add_centered_text(y, "|", 'F1', 14)
pdf.add_centered_text(y-12, "v", 'F1', 14)
y -= 40
pdf.add_centered_text(y, "RELIEF (Short-term anxiety reduction)", 'F2', 12)
y -= 20
pdf.add_centered_text(y, "But REINFORCES the cycle - OCD grows stronger", 'F4', 10)
y -= 30
pdf.add_centered_text(y, "|", 'F1', 14)
pdf.add_centered_text(y-12, "v", 'F1', 14)
y -= 40
pdf.add_centered_text(y, "CYCLE REPEATS (obsession returns, often worse)", 'F2', 12)
y -= 40
pdf.add_line(50, y, 562, y, 0.5, 0.5)
y -= 25
pdf.add_text(50, y, "ERP BREAKS THE CYCLE by:", 'F2', 11)
y -= 20
pdf.add_text(50, y, "- Facing the trigger/obsession WITHOUT performing the compulsion", 'F4', 10)
y -= 16
pdf.add_text(50, y, "- Allowing anxiety to NATURALLY decrease (habituation)", 'F4', 10)
y -= 16
pdf.add_text(50, y, "- Teaching your brain: 'I can handle uncertainty and discomfort'", 'F4', 10)

# Page 5: Types of OCD
pdf.new_page()
pdf.add_centered_text(750, "TYPES OF OCD", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
types_text = [
    "OCD can latch onto ANY theme. Common subtypes include:",
    "",
    "CONTAMINATION OCD",
    "  - Fear of germs, illness, bodily fluids, chemicals",
    "  - Compulsions: excessive washing, avoiding 'contaminated' objects",
    "",
    "HARM OCD",
    "  - Intrusive thoughts about hurting yourself or others",
    "  - Compulsions: checking, avoiding sharp objects, reassurance seeking",
    "  - NOTE: Having these thoughts does NOT mean you are dangerous",
    "",
    "SYMMETRY / 'JUST RIGHT' OCD",
    "  - Need for things to feel 'even' or 'just right'",
    "  - Compulsions: arranging, counting, repeating until it feels right",
    "",
    "RELIGIOUS / SCRUPULOSITY OCD",
    "  - Fear of sinning, blasphemy, or offending God",
    "  - Compulsions: excessive prayer, confessing, seeking reassurance",
    "",
    "RELATIONSHIP OCD (ROCD)",
    "  - Constant doubt about love/attraction to partner",
    "  - Compulsions: comparing, testing feelings, seeking reassurance",
    "",
    "OTHER COMMON THEMES:",
    "  - Pedophilia OCD (fear of being attracted to children - you are NOT)",
    "  - Existential OCD (obsessing about reality, consciousness)",
    "  - Health anxiety (fear of having a serious illness)",
    "  - Perfectionism OCD (fear of making mistakes)",
    "",
    "MY OCD THEME(S): ________________________________________",
    "My main obsessions: _____________________________________",
    "My main compulsions: ____________________________________"
]
for line in types_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Pages 6-10: ERP Hierarchy Builder (5 pages)
for page_num in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(750, f"ERP HIERARCHY BUILDER - PAGE {page_num}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 715
    if page_num == 1:
        pdf.add_text(50, y, "List feared situations from LEAST to MOST anxiety-provoking (0-100 SUDS).", 'F4', 10)
        y -= 14
        pdf.add_text(50, y, "SUDS = Subjective Units of Distress Scale (0=no anxiety, 100=worst ever)", 'F4', 10)
        y -= 25
    # Each page has entries for hierarchy items
    items_per_page = 5
    for i in range(items_per_page):
        item_num = (page_num - 1) * 5 + i + 1
        pdf.add_filled_rect(50, y - 5, 512, 105, 0.95)
        pdf.add_rect(50, y - 5, 512, 105, 0.5, 0.5)
        pdf.add_text(55, y + 85, f"EXPOSURE #{item_num}", 'F2', 10)
        pdf.add_text(55, y + 68, "Fear/Obsession:", 'F1', 9)
        pdf.add_line(145, y + 66, 555, y + 66, 0.3, 0.5)
        pdf.add_text(55, y + 52, "Anxiety Rating (SUDS 0-100):", 'F1', 9)
        pdf.add_rect(240, y + 48, 40, 14, 0.5)
        pdf.add_text(55, y + 36, "Exposure Task (what I will DO):", 'F1', 9)
        pdf.add_line(230, y + 34, 555, y + 34, 0.3, 0.5)
        pdf.add_text(55, y + 20, "Duration (how long I will stay in the exposure):", 'F1', 9)
        pdf.add_line(300, y + 18, 555, y + 18, 0.3, 0.5)
        pdf.add_text(55, y + 4, "SUDS During: Start ___ | 5 min ___ | 10 min ___ | 15 min ___ | End ___", 'F1', 9)
        y -= 120

# Pages 11-20: Exposure Practice Logs (10 pages)
for log_page in range(1, 11):
    pdf.new_page()
    pdf.add_centered_text(750, f"EXPOSURE PRACTICE LOG - PAGE {log_page}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 718
    for entry in range(3):
        pdf.add_text(50, y, f"Date: ___/___/___    Time: _______    Duration: _______", 'F1', 9)
        y -= 16
        pdf.add_text(50, y, "Trigger/Obsession:", 'F2', 9)
        pdf.add_line(155, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 16
        pdf.add_text(50, y, "Exposure Done:", 'F2', 9)
        pdf.add_line(135, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 16
        pdf.add_text(50, y, "Compulsion Resisted:", 'F2', 9)
        pdf.add_line(170, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 18
        pdf.add_text(50, y, "Anxiety BEFORE (0-100): ___", 'F1', 9)
        pdf.add_text(230, y, "DURING (peak): ___", 'F1', 9)
        pdf.add_text(370, y, "AFTER (end): ___", 'F1', 9)
        y -= 16
        pdf.add_text(50, y, "Rituals resisted?  YES / NO    If no, what did I do?", 'F1', 9)
        pdf.add_line(340, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 16
        pdf.add_text(50, y, "What I learned:", 'F1', 9)
        pdf.add_line(130, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 16
        pdf.add_line(50, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 20
        pdf.add_line(50, y, 562, y, 0.8, 0.7)
        y -= 20

# Pages 21-24: Cognitive Restructuring for Intrusive Thoughts (4 pages)
cog_titles = [
    "CHALLENGING INTRUSIVE THOUGHTS - Part 1",
    "CHALLENGING INTRUSIVE THOUGHTS - Part 2",
    "DEFUSION TECHNIQUES FOR OCD",
    "BUILDING TOLERANCE FOR UNCERTAINTY"
]
cog_content = [
    [
        "Intrusive thoughts are NORMAL. Everyone has them. The difference",
        "with OCD is that you get STUCK on them and assign them meaning.",
        "",
        "EXERCISE: Thought Record",
        "",
        "Intrusive thought #1: _________________________________________",
        "What OCD says this means: _____________________________________",
        "What the EVIDENCE says: ________________________________________",
        "Probability this thought is true (0-100%): ____",
        "What I would tell a friend with this thought: __________________",
        "",
        "Intrusive thought #2: _________________________________________",
        "What OCD says this means: _____________________________________",
        "What the EVIDENCE says: ________________________________________",
        "Probability this thought is true (0-100%): ____",
        "What I would tell a friend with this thought: __________________",
        "",
        "Intrusive thought #3: _________________________________________",
        "What OCD says this means: _____________________________________",
        "What the EVIDENCE says: ________________________________________",
        "Probability this thought is true (0-100%): ____",
        "What I would tell a friend with this thought: __________________",
        "",
        "REMINDER: The goal is NOT to make the thought go away.",
        "The goal is to change your RELATIONSHIP to the thought."
    ],
    [
        "COMMON COGNITIVE DISTORTIONS IN OCD:",
        "",
        "1. THOUGHT-ACTION FUSION: Believing thinking = doing",
        "   'If I think about hurting someone, I might do it.'",
        "   REALITY: Thoughts are NOT actions. Period.",
        "",
        "2. OVERESTIMATION OF THREAT: Believing danger is very likely",
        "   'If I touch that doorknob, I WILL get sick and die.'",
        "   REALITY: Your brain overestimates probability.",
        "",
        "3. INTOLERANCE OF UNCERTAINTY: Needing 100% certainty",
        "   'I need to KNOW for sure that I locked the door.'",
        "   REALITY: 100% certainty is impossible about anything.",
        "",
        "4. OVERIMPORTANCE OF THOUGHTS: 'If I think it, it matters'",
        "   'Having this thought means I am a terrible person.'",
        "   REALITY: Thoughts are mental noise, not identity.",
        "",
        "5. NEED TO CONTROL THOUGHTS: Believing you should stop them",
        "   'Normal people do not have these thoughts.'",
        "   REALITY: Everyone has bizarre/disturbing thoughts.",
        "",
        "MY MOST COMMON DISTORTION: _________________________________",
        "My rational response: _______________________________________",
        "________________________________________________________________"
    ],
    [
        "DEFUSION = Creating distance between YOU and your thoughts.",
        "You are NOT your thoughts. You are the one OBSERVING them.",
        "",
        "TECHNIQUE 1: Label It",
        "Say: 'I notice I am having the thought that...'",
        "Or: 'There is my OCD again, telling me...'",
        "Practice: ___________________________________________________",
        "",
        "TECHNIQUE 2: Sing It",
        "Sing your obsessive thought to 'Happy Birthday' or 'Jingle Bells'",
        "This removes the emotional charge without suppressing the thought.",
        "",
        "TECHNIQUE 3: Thank Your OCD",
        "'Thank you, OCD, for trying to protect me. I do not need your",
        "help right now. I can handle this uncertainty.'",
        "",
        "TECHNIQUE 4: The Leaves on a Stream",
        "Imagine placing each thought on a leaf floating down a stream.",
        "Watch it pass. Do not grab it. Do not push it away.",
        "",
        "TECHNIQUE 5: Agree with OCD (Paradox)",
        "'Maybe I DID leave the stove on. Maybe the house WILL burn down.'",
        "Agreeing sarcastically takes away OCD's power.",
        "",
        "TECHNIQUE 6: The Bully Metaphor",
        "OCD is like a bully. The more you react, the more it bothers you.",
        "Responding with 'Maybe, maybe not' starves the bully.",
        "",
        "My favorite defusion technique: ______________________________"
    ],
    [
        "OCD thrives on your NEED FOR CERTAINTY. Recovery means learning",
        "to live with 'maybe' and 'I don't know for sure.'",
        "",
        "UNCERTAINTY PRACTICE STATEMENTS (read daily):",
        "",
        "'Maybe I did, maybe I didn't. I can handle not knowing.'",
        "'I cannot be 100% sure, and that is okay.'",
        "'Uncertainty is uncomfortable, not dangerous.'",
        "'I choose to live my life even without certainty.'",
        "'My need to know is the OCD talking, not reality.'",
        "",
        "DAILY UNCERTAINTY EXPOSURES:",
        "Practice tolerating uncertainty in LOW-stakes situations first:",
        "",
        "- Leave a cabinet door slightly open. Do not check it.",
        "- Send a text without re-reading it 5 times.",
        "- Leave the house without checking the lock extra times.",
        "- Make a decision without researching exhaustively.",
        "- Say 'I don't know' when asked a question.",
        "",
        "MY UNCERTAINTY PRACTICE LOG:",
        "Day 1: ______________________ Anxiety (0-10): ___",
        "Day 2: ______________________ Anxiety (0-10): ___",
        "Day 3: ______________________ Anxiety (0-10): ___",
        "Day 4: ______________________ Anxiety (0-10): ___",
        "Day 5: ______________________ Anxiety (0-10): ___",
        "Day 6: ______________________ Anxiety (0-10): ___",
        "Day 7: ______________________ Anxiety (0-10): ___"
    ]
]

for i in range(4):
    pdf.new_page()
    pdf.add_centered_text(750, cog_titles[i], 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 715
    for line in cog_content[i]:
        pdf.add_text(50, y, line, 'F4', 10)
        y -= 16

# Page 25: Relapse Prevention Plan
pdf.new_page()
pdf.add_centered_text(750, "RELAPSE PREVENTION PLAN", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
relapse = [
    "OCD is a chronic condition. Flare-ups are NORMAL, not failure.",
    "Having a plan helps you respond quickly when OCD tries to return.",
    "",
    "MY WARNING SIGNS THAT OCD IS FLARING UP:",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "3. ____________________________________________________________",
    "",
    "COMMON RELAPSE TRIGGERS:",
    "- Stress / major life changes",
    "- Sleep deprivation",
    "- Illness / hormonal changes",
    "- Stopping ERP practice ('I am cured now')",
    "- Starting compulsions 'just this once'",
    "",
    "MY PLAN WHEN I NOTICE A FLARE-UP:",
    "1. Acknowledge it: 'My OCD is acting up. This is temporary.'",
    "2. Resume daily ERP exercises immediately",
    "3. Re-read this workbook (especially pages 3-5)",
    "4. Contact my therapist: _______________________________________",
    "5. Reach out to support: _______________________________________",
    "",
    "MAINTENANCE PLAN (even when doing well):",
    "- Weekly: Do at least 1 planned exposure from my hierarchy",
    "- Daily: Practice defusion when intrusive thoughts appear",
    "- Monthly: Review this workbook and update my hierarchy",
    "- Ongoing: Continue therapy as recommended"
]
for line in relapse:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 26: My Support Team
pdf.new_page()
pdf.add_centered_text(750, "MY SUPPORT TEAM", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 710
pdf.add_text(50, y, "Recovery is not a solo journey. List your support system:", 'F4', 11)
y -= 30
supports = [
    ("THERAPIST/COUNSELOR", ["Name:", "Phone:", "Email:", "Next appointment:"]),
    ("PSYCHIATRIST (if applicable)", ["Name:", "Phone:", "Medication:", "Next appointment:"]),
    ("TRUSTED FAMILY MEMBER", ["Name:", "Phone:", "What they know about my OCD:"]),
    ("TRUSTED FRIEND", ["Name:", "Phone:", "How they can help:"]),
    ("SUPPORT GROUP", ["Group name:", "Meeting time:", "Contact:"]),
    ("CRISIS RESOURCES", ["IOCDF: iocdf.org", "NOCD App: nocd.com", "Crisis line: 988", "My emergency plan:"])
]
for title_s, fields in supports:
    pdf.add_text(50, y, title_s, 'F2', 10)
    y -= 16
    for field in fields:
        pdf.add_text(60, y, field, 'F4', 9)
        pdf.add_line(180, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 14
    y -= 12

# Page 27: Progress Tracker
pdf.new_page()
pdf.add_centered_text(750, "MY PROGRESS TRACKER", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Track your SUDS ratings over time to see improvement!", 'F4', 11)
y -= 25
pdf.add_text(50, y, "Rate your OVERALL OCD severity each week (0-100):", 'F2', 10)
y -= 20
for week in range(1, 13):
    pdf.add_text(50, y, f"Week {week:2d}:  SUDS ____  Exposures completed: ____  Compulsions resisted: ____", 'F1', 9)
    y -= 18
y -= 15
pdf.add_text(50, y, "MILESTONES TO CELEBRATE:", 'F2', 11)
y -= 18
milestones = [
    "[ ] Completed my first exposure without ritualizing",
    "[ ] SUDS dropped below 50 for a previously feared situation",
    "[ ] Went a full day without compulsions",
    "[ ] Told someone about my OCD",
    "[ ] Recognized OCD in real-time and chose not to engage",
    "[ ] Completed all items on my hierarchy",
    "[ ] Had a flare-up and recovered using my plan"
]
for m in milestones:
    pdf.add_text(60, y, m, 'F4', 10)
    y -= 16

# Pages 28-30: 12-Week ERP Schedule (spread over 3 pages, 4 weeks each)
for sched_page in range(3):
    pdf.new_page()
    start_week = sched_page * 4 + 1
    end_week = start_week + 3
    pdf.add_centered_text(750, f"12-WEEK ERP SCHEDULE - WEEKS {start_week}-{end_week}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 715
    week_plans = [
        ("Foundation: Learn about OCD, complete hierarchy, start lowest item",
         "Daily: Read about OCD cycle | 3x/week: Practice lowest hierarchy item"),
        ("Building momentum: Continue lowest items, add next level",
         "Daily: Defusion practice | 3x/week: Exposure to items rated 20-35"),
        ("Increasing challenge: Move up hierarchy, reduce safety behaviors",
         "Daily: Uncertainty tolerance | 4x/week: Exposure to items rated 35-50"),
        ("Pushing through: Tackle moderate items, resist all compulsions",
         "Daily: No compulsions | 4x/week: Exposure to items rated 50-60"),
        ("Harder exposures: Face fears that feel very challenging",
         "Daily: Imaginal exposure | 4x/week: Exposure to items rated 60-70"),
        ("High difficulty: Tackle items you thought impossible",
         "Daily: Agree with OCD | 5x/week: Exposure to items rated 70-80"),
        ("Near the top: Face highest hierarchy items",
         "Daily: Full uncertainty acceptance | 5x/week: Items rated 80-90"),
        ("Peak challenge: Hardest items on your list",
         "Daily: Live as if OCD is lying | 5x/week: Items rated 90-100"),
        ("Consolidation: Repeat peak items, vary contexts",
         "Daily: Generalize exposures | Review and update hierarchy"),
        ("Maintenance: Continued practice, reduce frequency",
         "3x/week: Varied exposures | Build relapse prevention plan"),
        ("Independence: Self-directed ERP, handle flare-ups",
         "2x/week: Maintenance exposures | Practice responding to new triggers"),
        ("Graduation: Celebrate progress, plan ongoing maintenance",
         "Weekly: One planned exposure | Monthly: Review and adjust plan")
    ]
    for w in range(4):
        week_idx = sched_page * 4 + w
        week_num = week_idx + 1
        plan_title, plan_detail = week_plans[week_idx]
        pdf.add_filled_rect(50, y - 5, 512, 75, 0.95)
        pdf.add_rect(50, y - 5, 512, 75, 0.5, 0.5)
        pdf.add_text(55, y + 55, f"WEEK {week_num}", 'F2', 11)
        pdf.add_text(55, y + 38, f"Focus: {plan_title}", 'F4', 9)
        pdf.add_text(55, y + 22, f"Schedule: {plan_detail}", 'F4', 9)
        pdf.add_text(55, y + 6, "Notes: _______________________________________________________________", 'F1', 9)
        y -= 100

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book121_OCD_Therapy_Workbook.pdf')
print("Book121_OCD_Therapy_Workbook.pdf created successfully!")
