from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "DBT FOR ANGER"
subtitle = "Skills to Manage Rage Without Destroying Relationships"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 20)
pdf.add_centered_text(510, subtitle, 'F4', 13)
pdf.add_centered_text(420, "Dialectical Behavior Therapy Skills", 'F4', 12)
pdf.add_centered_text(400, "for Anger Management", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 13)
pdf.add_centered_text(560, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(540, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: Understanding Anger in DBT Framework
pdf.new_page()
pdf.add_centered_text(750, "UNDERSTANDING ANGER IN DBT", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
lines = [
    "DBT (Dialectical Behavior Therapy) views anger as a valid emotion",
    "that becomes problematic when it leads to destructive behavior.",
    "",
    "THE DBT PERSPECTIVE ON ANGER:",
    "- Anger is not 'bad' - it carries information",
    "- The problem is not the emotion but the behavioral response",
    "- You can feel intensely angry AND choose skillful behavior",
    "- Both things are true: your anger is valid AND your actions matter",
    "",
    "THE FOUR DBT SKILL MODULES FOR ANGER:",
    "",
    "1. MINDFULNESS - Observing anger without being controlled by it",
    "   Noticing urges without acting on them",
    "",
    "2. DISTRESS TOLERANCE - Surviving anger crises without making",
    "   things worse (when you can't fix the situation right now)",
    "",
    "3. EMOTION REGULATION - Reducing vulnerability to anger and",
    "   changing unwanted emotional responses",
    "",
    "4. INTERPERSONAL EFFECTIVENESS - Expressing anger in ways",
    "   that maintain relationships and self-respect",
    "",
    "WHY ANGER IS ESPECIALLY CHALLENGING:",
    "- Anger feels justified (so we resist changing it)",
    "- Anger provides temporary power/control",
    "- Anger masks vulnerable emotions (hurt, fear, shame)",
    "- Anger creates short-term relief but long-term damage",
    "- Others may reinforce our anger (agree we're 'right')",
]
for line in lines:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 17

# Page 4: Emotion Regulation Model for Anger
pdf.new_page()
pdf.add_centered_text(750, "EMOTION REGULATION MODEL FOR ANGER", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
model = [
    "Understanding the COMPONENTS of your anger gives you multiple",
    "intervention points. Each component can be changed:",
    "",
    "VULNERABILITY FACTORS (what makes anger more likely):",
    "- Physical illness or pain",
    "- Sleep deprivation",
    "- Hunger or poor nutrition",
    "- Substance use (alcohol lowers threshold)",
    "- Accumulated stress without relief",
    "- Unresolved emotional pain",
    "My top vulnerability factors: ________________________________",
    "",
    "PROMPTING EVENT (what triggers the anger):",
    "- External: something someone does or says",
    "- Internal: a thought, memory, or physical sensation",
    "My common prompting events: _________________________________",
    "",
    "INTERPRETATIONS (what you tell yourself about the event):",
    "- 'They did it on purpose'",
    "- 'This is unfair / They should know better'",
    "- 'I'm being disrespected'",
    "My typical interpretations: __________________________________",
    "",
    "BODY SENSATIONS: Heat, tension, heart rate, adrenaline",
    "ACTION URGES: Hit, yell, throw, slam, leave, retaliate",
    "EXPRESSIONS: Yelling, sarcasm, silent treatment, aggression",
    "AFTEREFFECTS: Guilt, shame, damaged relationships, consequences",
    "",
    "INTERVENTION: You can change ANY component to change the emotion."
]
for line in model:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 5: Opposite Action for Anger
pdf.new_page()
pdf.add_centered_text(750, "OPPOSITE ACTION FOR ANGER", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
opp = [
    "Opposite Action is the #1 DBT skill for anger. When anger urges",
    "say DO something destructive, you do the OPPOSITE instead.",
    "",
    "WHEN TO USE OPPOSITE ACTION:",
    "- When acting on anger would make things WORSE",
    "- When anger is not justified by the facts",
    "- When anger is justified but acting on it is ineffective",
    "",
    "ANGER'S ACTION URGES vs OPPOSITE ACTIONS:",
    "",
    "Urge: Attack/criticize  -->  Opposite: Gently avoid or be kind",
    "Urge: Yell/raise voice  -->  Opposite: Speak softly and slowly",
    "Urge: Slam/throw things -->  Opposite: Relax hands, unclench",
    "Urge: Storm out         -->  Opposite: Stay (or leave calmly)",
    "Urge: Give silent treat -->  Opposite: Communicate directly",
    "Urge: Seek revenge      -->  Opposite: Let go or problem-solve",
    "Urge: Ruminate/obsess   -->  Opposite: Distract, do something else",
    "",
    "HOW TO DO OPPOSITE ACTION FULLY:",
    "1. Identify the action urge (what does anger want me to do?)",
    "2. Identify the opposite (what would a calm person do?)",
    "3. Do the opposite ALL THE WAY (body, face, words, posture)",
    "4. Repeat until the emotion changes intensity",
    "",
    "IMPORTANT: Do this with WILLINGNESS, not white-knuckling.",
    "Opposite action done resentfully doesn't work as well.",
    "",
    "MY PRACTICE:",
    "My typical anger urge: ____________________________________",
    "My opposite action: _______________________________________",
]
for line in opp:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 6: TIPP Skills for Rage Moments
pdf.new_page()
pdf.add_centered_text(750, "TIPP SKILLS FOR RAGE MOMENTS", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
tipp = [
    "TIPP is for CRISIS moments when anger is at 8-10/10 and you",
    "need to change your body chemistry FAST before you do damage.",
    "",
    "T = TEMPERATURE",
    "  Dunk your face in ice water for 30 seconds (or hold ice on face)",
    "  This triggers the dive reflex and immediately slows heart rate",
    "  HOW: Bowl of ice water, lean face in. Or ice pack on eyes/cheeks",
    "  SCIENCE: Activates parasympathetic nervous system instantly",
    "",
    "I = INTENSE EXERCISE",
    "  Do vigorous exercise for 15-20 minutes to burn off adrenaline",
    "  Sprint, jump rope, climb stairs, pushups - anything HARD",
    "  HOW: Immediately start moving. Don't think, just move.",
    "  SCIENCE: Metabolizes stress hormones, releases endorphins",
    "",
    "P = PACED BREATHING",
    "  Breathe out LONGER than you breathe in",
    "  Inhale 4 counts, exhale 6-8 counts. Repeat 10+ times",
    "  HOW: Breathe from belly, not chest. Slow way down.",
    "  SCIENCE: Activates vagus nerve, reduces fight-or-flight",
    "",
    "P = PAIRED MUSCLE RELAXATION",
    "  Tense muscles while breathing in, relax while breathing out",
    "  Start with fists, then arms, shoulders, face, whole body",
    "  HOW: Hold tension 5 sec, release. Notice the contrast.",
    "  SCIENCE: Releases physical holding patterns of anger",
    "",
    "USE TIPP WHEN: You are about to explode. These are EMERGENCY tools.",
    "Use them BEFORE trying to talk or make decisions.",
]
for line in tipp:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 7: Interpersonal Effectiveness When Angry (DEAR MAN)
pdf.new_page()
pdf.add_centered_text(750, "DEAR MAN WHILE FURIOUS", 'F2', 15)
pdf.add_centered_text(732, "Interpersonal Effectiveness When Angry", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 700
dear_man = [
    "DEAR MAN is the DBT skill for asking for what you want effectively.",
    "Here's how to use it when anger makes you want to DEMAND:",
    "",
    "D = DESCRIBE (just the facts, no interpretation)",
    "  'When I got home, the dishes were still in the sink.'",
    "  NOT: 'You never do anything around here!'",
    "  Practice: _____________________________________________",
    "",
    "E = EXPRESS (how you feel, using I-statements)",
    "  'I feel frustrated and overwhelmed.'",
    "  NOT: 'You make me so angry!'",
    "  Practice: _____________________________________________",
    "",
    "A = ASSERT (what you want, specifically)",
    "  'I need us to split chores evenly.'",
    "  NOT: 'Figure it out!' or 'You should know!'",
    "  Practice: _____________________________________________",
    "",
    "R = REINFORCE (why they'd want to help)",
    "  'If we share the load, we'll both be less stressed and fight less.'",
    "  Practice: _____________________________________________",
    "",
    "M = MINDFUL (stay on topic, don't get derailed)",
    "  If they deflect: 'I hear that, and I want to stay on this topic.'",
    "",
    "A = APPEAR CONFIDENT (even when shaking inside)",
    "  Eye contact, steady voice, upright posture",
    "",
    "N = NEGOTIATE (be willing to give to get)",
    "  'What would work for both of us?'",
]
for line in dear_man:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 8: Mindfulness of Anger
pdf.new_page()
pdf.add_centered_text(750, "MINDFULNESS OF ANGER", 'F2', 15)
pdf.add_centered_text(732, "Observing Without Acting", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 700
mindful = [
    "Mindfulness means OBSERVING your anger without becoming it.",
    "You are not your anger. Anger is something passing through you.",
    "",
    "THE OBSERVE SKILL:",
    "Notice anger as it arises. Watch it like weather:",
    "'I notice a sensation of heat in my chest.'",
    "'I notice the thought that this is unfair.'",
    "'I notice the urge to raise my voice.'",
    "You are the observer, not the anger itself.",
    "",
    "THE DESCRIBE SKILL:",
    "Put words on your experience without judgment:",
    "'Anger is here. It feels hot and tight.'",
    "NOT: 'I'm so angry I could explode!' (this escalates)",
    "",
    "THE PARTICIPATE SKILL:",
    "Fully feel the anger without adding to it:",
    "- Don't suppress it (makes it worse)",
    "- Don't amplify it (rehearsing why you're right)",
    "- Just let it BE without acting on it",
    "",
    "PRACTICE: Next time anger arises, try this:",
    "1. Pause. Don't speak or act for 3 breaths.",
    "2. Name it: 'Anger is here.'",
    "3. Notice where it is in your body: ________________",
    "4. Rate it 1-10: ___",
    "5. Watch it. Does it stay the same? Grow? Shrink?",
    "6. Remind yourself: 'I can feel this AND choose my action.'",
    "",
    "IMPORTANT: Emotions are like waves. If you don't feed them,",
    "they WILL peak and then decrease. Every single time.",
]
for line in mindful:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 9: Distress Tolerance for Explosive Moments
pdf.new_page()
pdf.add_centered_text(750, "DISTRESS TOLERANCE FOR EXPLOSIVE MOMENTS", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
dt = [
    "When anger is at crisis level and you cannot resolve the situation",
    "right now, use these skills to SURVIVE without making things worse:",
    "",
    "STOP SKILL:",
    "S - Stop. Freeze. Don't move.",
    "T - Take a step back (physically or mentally)",
    "O - Observe what's happening inside and outside you",
    "P - Proceed mindfully (choose, don't react)",
    "",
    "DISTRACTION (ACCEPTS):",
    "A - Activities (go DO something physical)",
    "C - Contributing (help someone else, get out of your head)",
    "C - Comparisons (is this really the worst thing?)",
    "E - Emotions (watch something funny to change the channel)",
    "P - Pushing away (mentally put it in a box for later)",
    "T - Thoughts (count backwards, do math, name states)",
    "S - Sensations (ice, strong taste, loud music)",
    "",
    "SELF-SOOTHE (5 senses):",
    "Sight: Look at something calming (nature, art)",
    "Sound: Listen to music, nature sounds, silence",
    "Smell: Essential oils, fresh air, coffee",
    "Taste: Mint, chocolate, sour candy, hot tea",
    "Touch: Soft blanket, pet an animal, warm shower",
    "",
    "RADICAL ACCEPTANCE:",
    "'This situation is what it is right now. Fighting reality",
    "causes MORE suffering. I can accept AND work to change things.'",
]
for line in dt:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Pages 10-14: Anger Chain Analysis Worksheets (5 pages)
for i in range(5):
    pdf.new_page()
    pdf.add_centered_text(750, f"ANGER CHAIN ANALYSIS #{i+1}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 715
    pdf.add_text(50, y, "Date: ___/___/___  Anger intensity (1-10): ___", 'F1', 10)
    y -= 22
    chain = [
        "PROMPTING EVENT (What happened? Just the facts):",
        "___________________________________________________",
        "___________________________________________________",
        "",
        "VULNERABILITY FACTORS (What made me more susceptible?):",
        "[ ] Tired  [ ] Hungry  [ ] Stressed  [ ] In pain  [ ] Used substances",
        "[ ] Already upset about something else  [ ] Other: __________",
        "",
        "INTERPRETATIONS (What did I tell myself about the event?):",
        "___________________________________________________",
        "___________________________________________________",
        "",
        "BODY SENSATIONS (What did I feel physically?):",
        "___________________________________________________",
        "",
        "ACTION URGES (What did anger want me to do?):",
        "___________________________________________________",
        "",
        "WHAT I ACTUALLY DID (My behavior):",
        "___________________________________________________",
        "___________________________________________________",
        "",
        "CONSEQUENCES (What happened as a result?):",
        "Short-term: ________________________________________",
        "Long-term: _________________________________________",
        "",
        "WHAT I COULD HAVE DONE DIFFERENTLY:",
        "Skill I could have used: ______________________________",
        "At what point in the chain: ____________________________",
        "",
        "REPAIR NEEDED: [ ] Apology  [ ] Amends  [ ] Conversation  [ ] None",
    ]
    for line in chain:
        pdf.add_text(50, y, line, 'F4', 10)
        y -= 15

# Page 15: Building Mastery to Reduce Anger Baseline
pdf.new_page()
pdf.add_centered_text(750, "BUILDING MASTERY", 'F2', 15)
pdf.add_centered_text(732, "Reduce Your Anger Baseline Through Competence", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 700
mastery = [
    "Building Mastery means doing things that make you feel competent",
    "and in control. This reduces baseline anger and frustration.",
    "",
    "WHY IT WORKS: Much anger comes from feeling powerless or inadequate.",
    "When you regularly accomplish things, your threshold for anger rises.",
    "",
    "MASTERY ACTIVITIES (choose ones slightly challenging but doable):",
    "[ ] Exercise goals (building strength, endurance, skill)",
    "[ ] Learning something new (language, instrument, skill)",
    "[ ] Completing tasks you've been avoiding",
    "[ ] Work/career development (courses, certifications)",
    "[ ] Creative projects (writing, art, building)",
    "[ ] Relationship skills (having hard conversations well)",
    "[ ] Home improvement (fixing, organizing, creating)",
    "",
    "MY WEEKLY MASTERY PLAN:",
    "Monday: ____________________________________________",
    "Tuesday: ___________________________________________",
    "Wednesday: _________________________________________",
    "Thursday: __________________________________________",
    "Friday: ____________________________________________",
    "Saturday: __________________________________________",
    "Sunday: ____________________________________________",
    "",
    "KEY: Activities should be SLIGHTLY challenging. Too easy = no mastery",
    "feeling. Too hard = frustration (more anger). Find the sweet spot.",
]
for line in mastery:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 16: Accumulating Positive Emotions
pdf.new_page()
pdf.add_centered_text(750, "ACCUMULATING POSITIVE EMOTIONS", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
pos = [
    "If your life is all stress and obligation, anger becomes your",
    "default emotion. You NEED positive experiences to balance it.",
    "",
    "SHORT-TERM: Build pleasant events into EVERY day",
    "(Even 5-10 minutes counts. Non-negotiable daily.)",
    "",
    "My pleasant activities list (things that genuinely feel good):",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "4. _________________________________________________",
    "5. _________________________________________________",
    "6. _________________________________________________",
    "7. _________________________________________________",
    "8. _________________________________________________",
    "9. _________________________________________________",
    "10. ________________________________________________",
    "",
    "LONG-TERM: Build a life worth living",
    "What values do I want to live by? _______________________",
    "What goals align with my values? ________________________",
    "One step I can take this week: __________________________",
    "",
    "MINDFULNESS OF POSITIVE EMOTIONS:",
    "When something good happens, NOTICE it. Don't minimize it.",
    "Don't think about when it will end. Just be in it fully.",
    "",
    "My daily pleasant event this week: ______________________",
]
for line in pos:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Pages 17-21: Weekly Anger Diary Cards (5 pages)
for week in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEKLY DIARY CARD - WEEK {week}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # Header
    pdf.add_text(50, y, "Day", 'F2', 8)
    pdf.add_text(80, y, "Anger(0-5)", 'F2', 8)
    pdf.add_text(150, y, "Urge(0-5)", 'F2', 8)
    pdf.add_text(215, y, "Acted on?", 'F2', 8)
    pdf.add_text(285, y, "Skill Used", 'F2', 8)
    pdf.add_text(420, y, "Effective?", 'F2', 8)
    y -= 4
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 16
    for day in days:
        pdf.add_text(50, y, day, 'F3', 9)
        pdf.add_text(80, y, "___", 'F3', 9)
        pdf.add_text(150, y, "___", 'F3', 9)
        pdf.add_text(215, y, "Y / N", 'F3', 9)
        pdf.add_text(285, y, "_______________", 'F3', 9)
        pdf.add_text(420, y, "Y / N", 'F3', 9)
        y -= 18
    y -= 10
    pdf.add_text(50, y, "SKILLS PRACTICED THIS WEEK:", 'F2', 10)
    y -= 16
    skills_list = ["[ ] Opposite Action", "[ ] TIPP", "[ ] Mindfulness", "[ ] DEAR MAN",
                   "[ ] Distress Tolerance", "[ ] Chain Analysis", "[ ] Building Mastery"]
    for s in skills_list:
        pdf.add_text(50, y, s, 'F4', 9)
        y -= 14
    y -= 10
    pdf.add_text(50, y, "Biggest anger trigger this week: ______________________________", 'F4', 10)
    y -= 16
    pdf.add_text(50, y, "Best skill use this week: _____________________________________", 'F4', 10)
    y -= 16
    pdf.add_text(50, y, "What I want to improve next week: _____________________________", 'F4', 10)
    y -= 25
    pdf.add_text(50, y, "NOTES:", 'F2', 10)
    y -= 14
    for _ in range(6):
        pdf.add_line(50, y, 562, y, 0.3, 0.7)
        y -= 16

# Page 22: My Anger Crisis Plan
pdf.new_page()
pdf.add_centered_text(750, "MY ANGER CRISIS PLAN", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
crisis = [
    "When my anger reaches 8/10 or higher, I will follow this plan:",
    "",
    "STEP 1: STOP (Do not speak. Do not act. Freeze.)",
    "",
    "STEP 2: USE TIPP (circle which one I'll try first):",
    "  Temperature / Intense Exercise / Paced Breathing / Muscle Relax",
    "",
    "STEP 3: REMOVE MYSELF IF POSSIBLE",
    "  I will go to: ________________________________________",
    "  I will say: 'I need [time] to calm down. I'll be back.'",
    "",
    "STEP 4: AFTER 20 MINUTES, RE-ASSESS",
    "  Current anger level: ___/10",
    "  Am I ready to re-engage? [ ] Yes [ ] Need more time",
    "",
    "STEP 5: IF STILL HIGH, CALL MY SUPPORT:",
    "  Person 1: _________________ Phone: ________________",
    "  Person 2: _________________ Phone: ________________",
    "",
    "STEP 6: WHEN CALM, DO A CHAIN ANALYSIS (pages 10-14)",
    "",
    "RED FLAGS (situations where I need to LEAVE immediately):",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "",
    "MY COMMITMENT:",
    "I commit to using this plan before I act on anger.",
    "Even if I fail sometimes, I will try again every time.",
    "",
    "Signed: _________________________ Date: ___/___/___",
]
for line in crisis:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book159_DBT_Anger_Management.pdf')
print("Book159_DBT_Anger_Management.pdf created successfully!")
