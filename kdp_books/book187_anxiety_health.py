#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "HEALTH ANXIETY WORKBOOK", 'F2', 22)
pdf.add_centered_text(480, "Stop Googling Symptoms & Start Living", 'F4', 14)
pdf.add_centered_text(440, f"By {author}", 'F4', 12)
pdf.add_line(150, 420, 462, 420, 2)

# Page 2 - Copyright
pdf.new_page()
pdf.add_centered_text(500, f"Copyright - {author}", 'F1', 10)
pdf.add_centered_text(480, "All rights reserved. Not a substitute for medical care.", 'F1', 10)

# Page 3 - What is Health Anxiety
pdf.new_page()
pdf.add_centered_text(740, "WHAT IS HEALTH ANXIETY?", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Health anxiety (formerly hypochondria/Illness Anxiety Disorder) is:", 'F1', 11)
pdf.add_text(50, 685, "An intense fear that you have or will develop a serious illness,", 'F1', 11)
pdf.add_text(50, 665, "despite medical reassurance that you're healthy.", 'F1', 11)
pdf.add_text(50, 635, "COMMON PATTERNS:", 'F2', 12)
patterns = [
    "Googling symptoms repeatedly", "Checking body for signs of illness",
    "Seeking reassurance from doctors/loved ones", "Avoiding medical info OR obsessively consuming it",
    "Interpreting normal body sensations as dangerous",
    "Believing the worst-case scenario is happening",
    "Brief relief after reassurance, then anxiety returns"
]
y = 615
for p in patterns:
    pdf.add_text(60, y, f"- {p}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-10, "Which patterns do I relate to?", 'F2', 11)
y -= 30
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20

# Page 4 - The Reassurance-Seeking Cycle
pdf.new_page()
pdf.add_centered_text(740, "THE REASSURANCE-SEEKING CYCLE", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "This is the trap that keeps health anxiety alive:", 'F1', 11)
cycle = [
    "1. TRIGGER: Notice a body sensation or hear about an illness",
    "2. THOUGHT: 'What if this is something serious?'",
    "3. ANXIETY: Fear/panic rises, body produces MORE symptoms",
    "4. BEHAVIOR: Google, check body, call doctor, ask partner",
    "5. BRIEF RELIEF: 'Okay maybe I'm fine...'",
    "6. DOUBT RETURNS: 'But what if they missed something?'",
    "7. REPEAT: The cycle starts over, often worse"
]
y = 680
for c in cycle:
    pdf.add_text(60, y, c, 'F1', 10)
    y -= 20
pdf.add_text(50, y-10, "WHY REASSURANCE DOESN'T WORK:", 'F2', 11)
y -= 30
reasons = ["Each reassurance teaches your brain it NEEDED reassurance",
           "Tolerance builds - you need more reassurance each time",
           "It prevents you from learning you can tolerate uncertainty",
           "It keeps the anxiety alive instead of letting it naturally pass"]
for r in reasons:
    pdf.add_text(60, y, f"- {r}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-15, "My most common reassurance-seeking behavior:", 'F1', 11)
pdf.add_line(50, y-33, 540, y-33, 0.5, 0.7)


# Page 5 - Body Scanning & Misinterpretation
pdf.new_page()
pdf.add_centered_text(740, "BODY SCANNING & MISINTERPRETATION", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Your anxious brain is HYPER-AWARE of body sensations.", 'F1', 11)
pdf.add_text(50, 685, "Normal sensations get catastrophic interpretations:", 'F1', 11)
misinterp = [
    ("Headache", "Brain tumor", "Tension, dehydration, screen time"),
    ("Heart racing", "Heart attack", "Anxiety, caffeine, exercise"),
    ("Stomach pain", "Cancer", "Stress, diet, gas"),
    ("Dizziness", "Stroke", "Anxiety, standing up fast, hunger"),
    ("Tingling", "MS/nerve damage", "Sitting position, anxiety, cold"),
    ("Fatigue", "Chronic illness", "Poor sleep, stress, normal variation"),
]
y = 660
pdf.add_text(60, y, "Sensation", 'F2', 9)
pdf.add_text(200, y, "Anxious Thought", 'F2', 9)
pdf.add_text(380, y, "More Likely Cause", 'F2', 9)
y -= 5
pdf.add_line(50, y, 562, y, 0.5)
y -= 15
for sens, anx, likely in misinterp:
    pdf.add_text(60, y, sens, 'F1', 9)
    pdf.add_text(200, y, anx, 'F1', 9)
    pdf.add_text(380, y, likely, 'F1', 9)
    y -= 16
pdf.add_text(50, y-15, "MY misinterpretations:", 'F2', 11)
y -= 35
for i in range(3):
    pdf.add_text(50, y, "Sensation:__________ Anxious thought:__________ Likely cause:__________", 'F1', 9)
    y -= 22

# Page 6 - Cognitive Distortions
pdf.new_page()
pdf.add_centered_text(740, "COGNITIVE DISTORTIONS IN HEALTH ANXIETY", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
distortions = [
    ("Catastrophizing:", "Jumping to the worst possible outcome"),
    ("Probability overestimation:", "Believing rare illnesses are likely for YOU"),
    ("Confirmation bias:", "Noticing only info that confirms your fear"),
    ("Emotional reasoning:", "'I FEEL sick, so I must BE sick'"),
    ("Mind reading:", "'The doctor looked concerned, something must be wrong'"),
    ("Discounting positives:", "Ignoring normal test results, clean bills of health"),
]
y = 705
for name, desc in distortions:
    pdf.add_text(60, y, name, 'F2', 10)
    pdf.add_text(250, y, desc, 'F1', 10)
    y -= 20
pdf.add_text(50, y-10, "My most common distortion: _________________________________", 'F1', 11)
pdf.add_text(50, y-35, "Evidence AGAINST my health fear:", 'F2', 11)
y -= 55
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y-5, "What a friend would say to me:", 'F1', 11)
y -= 22
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20

# Pages 7-11 - Thought Records (5 pages)
for pg in range(5):
    pdf.new_page()
    pdf.add_centered_text(740, f"THOUGHT RECORD - HEALTH WORRY #{pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, "Date: ________  Symptom/trigger: ________________________________", 'F1', 10)
    pdf.add_text(50, 688, "Anxious thought: _______________________________________________", 'F1', 10)
    pdf.add_line(50, 670, 562, 670, 0.5, 0.7)
    pdf.add_text(50, 650, "Anxiety level (0-100): ______", 'F1', 10)
    pdf.add_text(50, 628, "What illness am I afraid of? _________________________________", 'F1', 10)
    pdf.add_text(50, 606, "Evidence FOR this fear:", 'F2', 10)
    y = 586
    for i in range(3):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "Evidence AGAINST this fear:", 'F2', 10)
    y -= 22
    for i in range(3):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "More balanced thought:", 'F2', 10)
    y -= 22
    for i in range(2):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "Anxiety level AFTER (0-100): ______", 'F1', 10)
    pdf.add_text(50, y-25, "Did I seek reassurance? Y / N  If yes, what happened?", 'F1', 10)
    pdf.add_line(50, y-42, 540, y-42, 0.5, 0.7)
    pdf.add_text(50, y-60, "Alternative action I took instead:", 'F1', 10)
    pdf.add_line(50, y-77, 540, y-77, 0.5, 0.7)


# Page 12 - Behavioral Experiments
pdf.new_page()
pdf.add_centered_text(740, "BEHAVIORAL EXPERIMENTS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Test your beliefs! What actually happens when you DON'T check?", 'F1', 11)
experiments = [
    "Don't Google symptoms for 24 hours",
    "Don't check your body for 1 day",
    "Don't ask anyone for reassurance for 48 hours",
    "Wait 1 week before calling the doctor about a new symptom",
    "Notice a symptom and do NOTHING about it"
]
y = 680
for exp in experiments:
    pdf.add_text(60, y, f"- {exp}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-15, "MY EXPERIMENT:", 'F2', 12)
y -= 35
pdf.add_text(50, y, "What I'll do differently: __________________________________", 'F1', 10)
y -= 22
pdf.add_text(50, y, "What I predict will happen: _________________________________", 'F1', 10)
y -= 22
pdf.add_text(50, y, "What ACTUALLY happened: _____________________________________", 'F1', 10)
y -= 22
pdf.add_line(50, y, 540, y, 0.5, 0.7)
y -= 20
pdf.add_text(50, y, "Anxiety level during (0-100): ______", 'F1', 10)
y -= 22
pdf.add_text(50, y, "What I learned: ____________________________________________", 'F1', 10)
y -= 22
pdf.add_line(50, y, 540, y, 0.5, 0.7)

# Page 13 - Interoceptive Exposure
pdf.new_page()
pdf.add_centered_text(740, "INTEROCEPTIVE EXPOSURE", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Learn that body sensations are NOT dangerous by creating them on purpose:", 'F1', 10)
exercises_ie = [
    ("Spin in a chair (30 sec)", "Dizziness", "___/10"),
    ("Run in place (60 sec)", "Heart racing, breathlessness", "___/10"),
    ("Hold breath (30 sec)", "Chest tightness", "___/10"),
    ("Stare at a light then read", "Visual disturbance", "___/10"),
    ("Tense all muscles (60 sec)", "Muscle ache, tingling", "___/10"),
    ("Breathe through a straw (30 sec)", "Breathlessness", "___/10"),
    ("Shake head side to side (30 sec)", "Dizziness, disorientation", "___/10"),
]
y = 680
pdf.add_text(50, y, "Exercise", 'F2', 9)
pdf.add_text(250, y, "Sensation Created", 'F2', 9)
pdf.add_text(450, y, "Fear", 'F2', 9)
y -= 5
pdf.add_line(50, y, 562, y, 0.5)
y -= 15
for ex, sens, fear in exercises_ie:
    pdf.add_text(50, y, ex, 'F1', 9)
    pdf.add_text(250, y, sens, 'F1', 9)
    pdf.add_text(450, y, fear, 'F1', 9)
    y -= 18
pdf.add_text(50, y-15, "KEY INSIGHT: The sensation passed. Nothing bad happened.", 'F2', 10, 0.3)
pdf.add_text(50, y-35, "What I learned: ___________________________________________", 'F1', 10)
pdf.add_line(50, y-52, 540, y-52, 0.5, 0.7)

# Page 14 - Reducing Reassurance
pdf.new_page()
pdf.add_centered_text(740, "REDUCING REASSURANCE-SEEKING", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Gradual plan to stop seeking reassurance:", 'F2', 11)
steps_rr = [
    "Step 1: Notice every time you seek reassurance (tally it)",
    "Step 2: Delay reassurance by 30 minutes (sit with uncertainty)",
    "Step 3: Delay by 2 hours",
    "Step 4: Delay until next day",
    "Step 5: Don't seek it at all - use coping skill instead"
]
y = 680
for s in steps_rr:
    pdf.add_text(60, y, s, 'F1', 10)
    y -= 18
pdf.add_text(50, y-10, "INSTEAD OF REASSURANCE, I WILL:", 'F2', 11)
y -= 30
alternatives = ["Say to myself: 'I can tolerate this uncertainty.'",
                "Do a grounding exercise (5-4-3-2-1 senses)",
                "Accept the thought without engaging: 'There's that thought again.'",
                "Remind myself: 'Anxiety is not evidence.'",
                "Do an activity that requires focus"]
for a in alternatives:
    pdf.add_text(60, y, f"- {a}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-15, "My reassurance-seeking tally this week: ______", 'F1', 11)
pdf.add_text(50, y-35, "Times I resisted seeking reassurance: ______", 'F1', 11)

# Pages 15-19 - Weekly Symptom Worry Tracker (5 pages)
for week in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(740, f"WEEKLY SYMPTOM WORRY TRACKER - WEEK {week}", 'F2', 13)
    pdf.add_line(50, 730, 562, 730, 1)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    y = 712
    for day in days:
        pdf.add_text(50, y, day, 'F2', 8)
        pdf.add_text(80, y, "Symptom:__________", 'F1', 7)
        pdf.add_text(195, y, "Fear:__________", 'F1', 7)
        pdf.add_text(300, y, "Anx:__/10", 'F1', 7)
        pdf.add_text(365, y, "Googled? Y/N", 'F1', 7)
        pdf.add_text(450, y, "Checked? Y/N", 'F1', 7)
        pdf.add_line(50, y-10, 562, y-10, 0.3, 0.8)
        y -= 28
    pdf.add_text(50, y-5, "Times I Googled: ___  Times I checked body: ___", 'F1', 9)
    pdf.add_text(50, y-22, "Times I asked for reassurance: ___", 'F1', 9)
    pdf.add_text(50, y-39, "Times I resisted & coped: ___", 'F2', 9)
    pdf.add_text(50, y-56, "What helped most: ______________________________________", 'F1', 9)

# Pages 20-30 remaining
titles_rest = ["WHEN TO SEE A DOCTOR VS ANXIETY", "MINDFULNESS OF BODY SENSATIONS",
               "RESPONSE PREVENTION PLAN", "MY HEALTH ANXIETY ACTION PLAN",
               "UNCERTAINTY TOLERANCE PRACTICE", "COGNITIVE DEFUSION EXERCISES",
               "MY SAFETY BEHAVIORS TO ELIMINATE", "SELF-COMPASSION FOR HEALTH ANXIETY",
               "EXPOSURE HIERARCHY", "VALUES-BASED LIVING", "MY RECOVERY PROGRESS"]
for pg, t in enumerate(titles_rest):
    pdf.new_page()
    pdf.add_centered_text(740, t, 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 0:  # When to see doctor
        pdf.add_text(50, 710, "SEE A DOCTOR IF:", 'F2', 11)
        see_doc = ["New symptom that lasts more than 2 weeks",
                   "Sudden severe pain", "High fever that won't break",
                   "Blood in stool/urine", "Unexplained weight loss (10+ lbs)",
                   "A lump that's growing"]
        y = 690
        for s in see_doc:
            pdf.add_text(60, y, f"- {s}", 'F1', 10)
            y -= 16
        pdf.add_text(50, y-15, "IT'S PROBABLY ANXIETY IF:", 'F2', 11)
        y -= 35
        anxiety_signs = ["You've been reassured by a doctor already",
                         "Symptoms come and go with stress",
                         "You've had similar fears before that resolved",
                         "Dr. Google is your main source of concern",
                         "Symptoms shift to whatever you read about last"]
        for s in anxiety_signs:
            pdf.add_text(60, y, f"- {s}", 'F1', 10)
            y -= 16
    else:
        y = 710
        for i in range(28):
            pdf.add_line(50, y, 562, y, 0.5, 0.7)
            y -= 22

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book187_Health_Anxiety_Workbook.pdf')
print("Book187_Health_Anxiety_Workbook.pdf created successfully!")
