from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "THE SLEEP WORKBOOK"
subtitle = "CBT-I Techniques for Better Sleep Without Medication"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, title, 'F2', 18)
pdf.add_centered_text(450, subtitle, 'F4', 11)
pdf.add_centered_text(350, "Evidence-Based Strategies for", 'F4', 11)
pdf.add_centered_text(335, "Overcoming Insomnia Naturally", 'F4', 11)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(520, title, 'F2', 12)
pdf.add_centered_text(490, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(470, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(440, "No part of this publication may be reproduced without permission.", 'F4', 8)

# Page 3: Understanding Insomnia (CBT-I approach)
pdf.new_page()
pdf.add_centered_text(610, "UNDERSTANDING INSOMNIA", 'F2', 14)
pdf.add_line(40, 600, 392, 600)
y = 580
lines = [
    "CBT-I (Cognitive Behavioral Therapy for Insomnia) is the #1",
    "recommended treatment for chronic insomnia - even above medication.",
    "",
    "WHY CBT-I WORKS:",
    "- Addresses the ROOT CAUSES of insomnia, not just symptoms",
    "- Effects last long after treatment (unlike sleeping pills)",
    "- No side effects, no dependency",
    "- Recommended by the American Academy of Sleep Medicine",
    "",
    "THE 3P MODEL OF INSOMNIA:",
    "Predisposing: You may be naturally lighter sleeper",
    "Precipitating: A stressful event triggered the insomnia",
    "Perpetuating: HABITS you developed that now maintain it",
    "",
    "COMMON PERPETUATING HABITS:",
    "- Going to bed too early (lying awake builds anxiety)",
    "- Staying in bed when not sleeping (bed = awake place)",
    "- Napping during the day (reduces sleep drive)",
    "- Clock watching (increases frustration)",
    "- Compensating (caffeine, sleeping in on weekends)",
    "- Worrying about sleep (creates hyperarousal)",
    "",
    "THIS WORKBOOK COVERS:",
    "1. Sleep diary (track your actual patterns)",
    "2. Sleep restriction (counterintuitive but powerful)",
    "3. Stimulus control (retrain your brain about bed)",
    "4. Cognitive restructuring (stop worry about sleep)",
    "5. Relaxation techniques",
    "6. Sleep hygiene optimization",
]
for line in lines:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Pages 4-17: Sleep Diary (14 pages)
for day in range(1, 15):
    pdf.new_page()
    pdf.add_centered_text(610, f"SLEEP DIARY - DAY {day}", 'F2', 13)
    pdf.add_text(40, 595, f"Date: ___/___/___", 'F1', 10)
    pdf.add_line(40, 588, 392, 588)
    y = 572
    diary_fields = [
        "EVENING:",
        "What time did you get into bed? ___:___ am/pm",
        "What time did you try to fall asleep? ___:___ am/pm",
        "Did you take any sleep medication? [ ] Yes: _______ [ ] No",
        "Caffeine today? [ ] No [ ] Yes - last at ___:___",
        "Alcohol today? [ ] No [ ] Yes - amount: ___",
        "Exercise today? [ ] No [ ] Yes - type/time: ___",
        "Nap today? [ ] No [ ] Yes - duration: ___ min",
        "",
        "MORNING (fill in when you wake up):",
        "How long did it take to fall asleep? ___ minutes",
        "How many times did you wake up? ___",
        "Total time awake during night? ___ minutes",
        "What time was your final wake-up? ___:___ am/pm",
        "What time did you get out of bed? ___:___ am/pm",
        "",
        "CALCULATIONS:",
        "Time in bed (TIB): ___ hours ___ min",
        "Total sleep time (TST): ___ hours ___ min",
        "Sleep efficiency: TST / TIB x 100 = ___%",
        "(Goal: 85% or higher)",
        "",
        "RATINGS:",
        "Sleep quality (1-5): ___",
        "Daytime fatigue (1-5): ___",
        "Daytime functioning (1-5): ___",
        "Mood today (1-5): ___",
        "",
        "Notes: ______________________________________",
    ]
    for field in diary_fields:
        pdf.add_text(40, y, field, 'F4', 9)
        y -= 14

# Page 18: Sleep Restriction Therapy Calculator
pdf.new_page()
pdf.add_centered_text(610, "SLEEP RESTRICTION THERAPY", 'F2', 14)
pdf.add_line(40, 600, 392, 600)
y = 580
sr = [
    "Sleep restriction SOUNDS scary but it's the most powerful CBT-I",
    "tool. You temporarily limit time in bed to match actual sleep.",
    "",
    "STEP 1: Calculate your average sleep time from diary",
    "Week 1 average TST: ___ hours ___ min",
    "(Add up 7 days of total sleep time, divide by 7)",
    "",
    "STEP 2: Set your sleep window",
    "Your time in bed = average TST (minimum 5.5 hours)",
    "My sleep window: ___ hours ___ min",
    "",
    "STEP 3: Choose a fixed wake time (7 days/week)",
    "My wake time: ___:___ am (non-negotiable, even weekends)",
    "",
    "STEP 4: Calculate bedtime",
    "Wake time minus sleep window = bedtime",
    "My bedtime: ___:___ pm (do NOT get in bed before this)",
    "",
    "STEP 5: Adjust weekly",
    "If sleep efficiency > 90%: add 15 min (earlier bedtime)",
    "If sleep efficiency 85-90%: keep same window",
    "If sleep efficiency < 85%: reduce 15 min (later bedtime)",
    "",
    "WEEKLY ADJUSTMENTS:",
    "Week 1 efficiency: ___% -> New bedtime: ___:___",
    "Week 2 efficiency: ___% -> New bedtime: ___:___",
    "Week 3 efficiency: ___% -> New bedtime: ___:___",
    "Week 4 efficiency: ___% -> New bedtime: ___:___",
    "",
    "NOTE: You WILL feel tired at first. This is temporary.",
    "The sleep pressure you build = deeper, better sleep.",
]
for line in sr:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 19: Stimulus Control Instructions
pdf.new_page()
pdf.add_centered_text(610, "STIMULUS CONTROL", 'F2', 14)
pdf.add_line(40, 600, 392, 600)
y = 580
sc = [
    "Your brain has learned to associate bed with WAKEFULNESS.",
    "Stimulus control retrains the bed = sleep connection.",
    "",
    "THE RULES (follow them strictly for 4+ weeks):",
    "",
    "1. Use the bed ONLY for sleep and intimacy",
    "   No TV, phone, reading, eating, worrying in bed",
    "   Rate your compliance (1-5): ___",
    "",
    "2. Only go to bed when sleepy (not just tired)",
    "   Sleepy = eyes heavy, head nodding, yawning",
    "   NOT: 'I should go to bed because it's late'",
    "   Rate your compliance (1-5): ___",
    "",
    "3. If you can't sleep after ~15-20 min, GET UP",
    "   Go to another room. Do something boring/calming.",
    "   Return ONLY when sleepy again. Repeat as needed.",
    "   Rate your compliance (1-5): ___",
    "",
    "4. Wake at the same time EVERY morning",
    "   Regardless of how much you slept. No sleeping in.",
    "   Including weekends. (This anchors your rhythm.)",
    "   Rate your compliance (1-5): ___",
    "",
    "5. No napping during the day",
    "   If desperate: maximum 20 min before 2pm",
    "   Rate your compliance (1-5): ___",
    "",
    "WHAT TO DO WHEN UP AT NIGHT:",
    "Dim lights, boring book, gentle stretching, knitting",
    "Do NOT use screens, eat, exercise, or do work",
]
for line in sc:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 20: Cognitive Restructuring for Sleep Anxiety
pdf.new_page()
pdf.add_centered_text(610, "COGNITIVE RESTRUCTURING", 'F2', 14)
pdf.add_centered_text(593, "Challenging Worried Thoughts About Sleep", 'F1', 10)
pdf.add_line(40, 585, 392, 585)
y = 568
cog = [
    "Worrying about sleep CAUSES poor sleep. Challenge these thoughts:",
    "",
    "COMMON SLEEP WORRY: 'I won't function tomorrow if I don't sleep'",
    "Challenge: You've functioned on bad sleep before. You can cope.",
    "Balanced thought: ____________________________________",
    "",
    "COMMON SLEEP WORRY: 'I need 8 hours or I'll get sick'",
    "Challenge: Sleep needs vary. Quality > quantity.",
    "Balanced thought: ____________________________________",
    "",
    "COMMON SLEEP WORRY: 'Something is seriously wrong with me'",
    "Challenge: Insomnia is common and treatable. Not dangerous.",
    "Balanced thought: ____________________________________",
    "",
    "COMMON SLEEP WORRY: 'I'll never sleep normally again'",
    "Challenge: CBT-I works for 70-80% of people. Be patient.",
    "Balanced thought: ____________________________________",
    "",
    "MY TOP SLEEP WORRIES:",
    "1. _______________________________________________",
    "   Challenge: _____________________________________",
    "2. _______________________________________________",
    "   Challenge: _____________________________________",
    "3. _______________________________________________",
    "   Challenge: _____________________________________",
]
for line in cog:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 21: Progressive Muscle Relaxation
pdf.new_page()
pdf.add_centered_text(610, "PROGRESSIVE MUSCLE RELAXATION", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pmr = [
    "Do this in bed when trying to sleep. Takes 10-15 minutes.",
    "Tense each muscle group 5 seconds, release 15 seconds.",
    "",
    "SEQUENCE (go slowly through each):",
    "1. Feet: Curl toes tightly... release",
    "2. Calves: Point toes toward face... release",
    "3. Thighs: Squeeze thighs together... release",
    "4. Buttocks: Clench... release",
    "5. Stomach: Pull belly button to spine... release",
    "6. Chest: Take deep breath, hold... release",
    "7. Hands: Make tight fists... release",
    "8. Arms: Flex biceps... release",
    "9. Shoulders: Shrug to ears... release",
    "10. Neck: Gently press head into pillow... release",
    "11. Face: Scrunch all facial muscles... release",
    "12. Whole body: Tense everything at once... release",
    "",
    "TIPS:",
    "- Focus on the CONTRAST between tense and relaxed",
    "- Breathe in while tensing, out while releasing",
    "- If your mind wanders, gently come back to the muscle",
    "- Don't worry about doing it 'perfectly'",
    "- Practice daily, even on good sleep nights",
    "",
    "EFFECTIVENESS LOG:",
    "Date: ___ Relaxation level after (1-10): ___",
    "Date: ___ Relaxation level after (1-10): ___",
    "Date: ___ Relaxation level after (1-10): ___",
]
for line in pmr:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 22: Sleep Hygiene Checklist
pdf.new_page()
pdf.add_centered_text(610, "SLEEP HYGIENE CHECKLIST", 'F2', 14)
pdf.add_line(40, 600, 392, 600)
y = 580
hygiene = [
    "ENVIRONMENT (your bedroom should be a sleep cave):",
    "[ ] Room is dark (blackout curtains, no LEDs)",
    "[ ] Room is cool (65-68F / 18-20C ideal)",
    "[ ] Room is quiet (earplugs or white noise)",
    "[ ] Comfortable mattress and pillows",
    "[ ] No TV in bedroom",
    "[ ] Phone charges OUTSIDE bedroom (or far from bed)",
    "",
    "TIMING:",
    "[ ] Consistent wake time 7 days/week",
    "[ ] No caffeine after 2pm (or 8 hours before bed)",
    "[ ] No alcohol within 3 hours of bedtime",
    "[ ] No heavy meals within 2 hours of bedtime",
    "[ ] No vigorous exercise within 3 hours of bed",
    "[ ] Wind-down routine 30-60 min before bed",
    "",
    "DAYTIME:",
    "[ ] Get bright light exposure within 30 min of waking",
    "[ ] Exercise regularly (but not too late)",
    "[ ] Limit naps (none or <20 min before 2pm)",
    "[ ] Manage stress during the day",
    "",
    "MY SLEEP HYGIENE IMPROVEMENTS TO MAKE:",
    "This week I'll fix: ________________________________",
    "Next week I'll fix: ________________________________",
]
for line in hygiene:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 23: Caffeine/Alcohol/Screen Audit
pdf.new_page()
pdf.add_centered_text(610, "CAFFEINE / ALCOHOL / SCREEN AUDIT", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
audit = [
    "These three sabotage sleep more than anything else. Be honest:",
    "",
    "CAFFEINE AUDIT:",
    "Sources I consume: [ ] Coffee [ ] Tea [ ] Soda [ ] Energy drinks",
    "  [ ] Chocolate [ ] Pre-workout [ ] Other: ________",
    "Total daily caffeine: approximately ___ mg",
    "My last caffeine of the day is at: ___:___ pm",
    "Caffeine half-life is 5-7 hours. If bed at 10pm,",
    "last caffeine should be: ___ pm at latest",
    "My caffeine change plan: ___________________________",
    "",
    "ALCOHOL AUDIT:",
    "Drinks per week: ___",
    "Do I use alcohol to help me sleep? [ ] Yes [ ] No",
    "TRUTH: Alcohol causes lighter sleep, more waking, less REM",
    "My alcohol change plan: ____________________________",
    "",
    "SCREEN AUDIT:",
    "Last screen use before bed: ___ min before",
    "Screens in bedroom: [ ] Phone [ ] TV [ ] Tablet [ ] Laptop",
    "Blue light suppresses melatonin for 2+ hours after use",
    "My screen change plan: _____________________________",
    "",
    "ONE CHANGE I'LL MAKE THIS WEEK:",
    "__________________________________________________",
]
for line in audit:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 24: Worry Journal
pdf.new_page()
pdf.add_centered_text(610, "WORRY JOURNAL", 'F2', 14)
pdf.add_centered_text(593, "Dump Worries Before Bed (Not IN Bed)", 'F1', 10)
pdf.add_line(40, 585, 392, 585)
y = 568
pdf.add_text(40, y, "30 minutes before bed, spend 10 min writing worries HERE.", 'F4', 9.5)
y -= 12
pdf.add_text(40, y, "When they pop up in bed: 'I already dealt with that. It can wait.'", 'F4', 9.5)
y -= 18
for entry in range(4):
    pdf.add_text(40, y, f"Date: ___/___/___", 'F2', 9)
    y -= 14
    pdf.add_text(40, y, "What's on my mind:", 'F4', 9)
    y -= 12
    for _ in range(3):
        pdf.add_line(40, y, 392, y, 0.3, 0.7)
        y -= 13
    pdf.add_text(40, y, "Can I solve this tonight? [ ] No (let it go) [ ] Yes (action: ________)", 'F4', 9)
    y -= 18
    pdf.add_line(40, y+8, 392, y+8, 0.5, 0.5)
    y -= 10

# Page 25: My Personalized Sleep Plan
pdf.new_page()
pdf.add_centered_text(610, "MY PERSONALIZED SLEEP PLAN", 'F2', 14)
pdf.add_line(40, 600, 392, 600)
y = 580
plan = [
    "MY FIXED WAKE TIME: ___:___ am (every day, no exceptions)",
    "",
    "MY CURRENT BEDTIME: ___:___ pm",
    "",
    "MY WIND-DOWN ROUTINE (30-60 min before bed):",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "",
    "IF I CAN'T SLEEP, I WILL:",
    "Get up after 15-20 min and: ______________________",
    "Return to bed only when: _________________________",
    "",
    "CAFFEINE CUTOFF: ___:___ pm",
    "SCREEN CUTOFF: ___:___ pm",
    "LAST MEAL BY: ___:___ pm",
    "",
    "MY RELAXATION TECHNIQUE: ________________________",
    "",
    "MY SLEEP WORRY CHALLENGE:",
    "Old thought: ____________________________________",
    "New thought: ____________________________________",
    "",
    "I WILL TRACK PROGRESS IN THIS WORKBOOK FOR ___ WEEKS",
    "",
    "MY GOAL: To sleep ___hours with ___% efficiency",
]
for line in plan:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 16

# Page 26-29: 4-Week Sleep Improvement Tracker
for week in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(610, f"4-WEEK TRACKER - WEEK {week}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 585
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    pdf.add_text(40, y, "Day", 'F2', 8)
    pdf.add_text(70, y, "TST", 'F2', 8)
    pdf.add_text(105, y, "TIB", 'F2', 8)
    pdf.add_text(135, y, "Eff%", 'F2', 8)
    pdf.add_text(170, y, "Quality", 'F2', 8)
    pdf.add_text(210, y, "Fatigue", 'F2', 8)
    pdf.add_text(255, y, "Techniques Used", 'F2', 8)
    pdf.add_line(40, y-3, 392, y-3, 0.5)
    y -= 16
    for d in days:
        pdf.add_text(40, y, d, 'F3', 8)
        pdf.add_text(70, y, "___", 'F3', 8)
        pdf.add_text(105, y, "___", 'F3', 8)
        pdf.add_text(135, y, "___%", 'F3', 8)
        pdf.add_text(170, y, "1-5:_", 'F3', 8)
        pdf.add_text(210, y, "1-5:_", 'F3', 8)
        pdf.add_text(255, y, "_________________", 'F3', 8)
        y -= 16
    y -= 10
    pdf.add_text(40, y, f"Week {week} Average Sleep Efficiency: ___%", 'F2', 10)
    y -= 16
    pdf.add_text(40, y, f"Adjustment for next week: ________________________", 'F4', 9.5)
    y -= 25
    pdf.add_text(40, y, "What went well this week:", 'F2', 9)
    y -= 13
    pdf.add_line(40, y, 392, y, 0.3, 0.7)
    y -= 18
    pdf.add_text(40, y, "What was challenging:", 'F2', 9)
    y -= 13
    pdf.add_line(40, y, 392, y, 0.3, 0.7)
    y -= 18
    pdf.add_text(40, y, "Commitment for next week:", 'F2', 9)
    y -= 13
    pdf.add_line(40, y, 392, y, 0.3, 0.7)

# Page 30: When to See a Sleep Specialist
pdf.new_page()
pdf.add_centered_text(610, "WHEN TO SEE A SLEEP SPECIALIST", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
specialist = [
    "CBT-I works for most people, but see a doctor if:",
    "",
    "[ ] You've tried CBT-I consistently for 6+ weeks with no help",
    "[ ] You snore loudly or have been told you stop breathing",
    "[ ] You have restless legs that prevent sleep",
    "[ ] You fall asleep uncontrollably during the day",
    "[ ] You have unusual behaviors during sleep (acting out dreams)",
    "[ ] Your insomnia started after a medication change",
    "[ ] You have significant depression or anxiety with insomnia",
    "",
    "POSSIBLE SLEEP DISORDERS TO RULE OUT:",
    "- Sleep Apnea (breathing stops during sleep)",
    "- Restless Leg Syndrome (irresistible urge to move legs)",
    "- Narcolepsy (excessive daytime sleepiness)",
    "- Circadian Rhythm Disorders (body clock misaligned)",
    "- Parasomnias (sleepwalking, sleep talking)",
    "",
    "HOW TO FIND A SLEEP SPECIALIST:",
    "- Ask your primary care doctor for a referral",
    "- Look for board-certified sleep medicine physicians",
    "- Check if CBT-I therapists are available in your area",
    "- Online CBT-I programs (Insomnia Coach app is free)",
    "",
    "REMEMBER:",
    "You deserve good sleep. It's not a luxury. It's a",
    "fundamental health need. Keep working at it.",
]
for line in specialist:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book161_Sleep_Hygiene_Workbook.pdf')
print("Book161_Sleep_Hygiene_Workbook.pdf created successfully!")
