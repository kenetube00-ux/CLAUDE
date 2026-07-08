"""Book 95: DBT Skills Workbook for Adults - BPD Focus"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.14)
    pdf.add_centered_text(520, "DBT SKILLS WORKBOOK", 'F2', 28, 1)
    pdf.add_centered_text(480, "FOR ADULTS", 'F2', 28, 1)
    pdf.add_centered_text(430, "Managing Intense Emotions & Relationships", 'F4', 15, 0.9)
    pdf.add_centered_text(380, "Distress Tolerance | Emotion Regulation", 'F1', 12, 0.8)
    pdf.add_centered_text(358, "Interpersonal Effectiveness | Mindfulness", 'F1', 12, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    pdf.add_centered_text(170, "Evidence-Based DBT Skills & Worksheets", 'F1', 11, 0.7)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "DBT Skills Workbook for Adults", 'F2', 14)
    pdf.add_centered_text(478, "Managing Intense Emotions & Relationships", 'F4', 11)
    pdf.add_centered_text(445, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(425, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(395, "This workbook is for educational purposes only.", 'F1', 9)
    pdf.add_centered_text(375, "It is not a substitute for professional DBT treatment.", 'F1', 9)
    pdf.add_centered_text(345, "If you are in crisis, call 988 Suicide & Crisis Lifeline.", 'F2', 9)


    # Page 1: Understanding Emotional Dysregulation
    pdf.new_page()
    pdf.add_centered_text(740, "UNDERSTANDING EMOTIONAL DYSREGULATION", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Emotional dysregulation means your emotions are MORE INTENSE, come on",
        "FASTER, and take LONGER to return to baseline than other people's.",
        "",
        "This is not a character flaw. It is a biological difference in how",
        "your nervous system processes emotional stimuli.",
        "",
        "THE BIOSOCIAL THEORY:",
        "  Biology: You were born with a more sensitive emotional system",
        "  + Environment: Your emotions were invalidated ('You're overreacting')",
        "  = Difficulty regulating emotions as an adult",
        "",
        "WHAT DYSREGULATION LOOKS LIKE:",
        "  - Emotions go from 0 to 100 in seconds",
        "  - Small events trigger overwhelming reactions",
        "  - Difficulty calming down once upset",
        "  - Impulsive behaviors to escape pain (spending, substances, self-harm)",
        "  - Relationships feel all-or-nothing (idealize/devalue)",
        "  - Chronic feelings of emptiness",
        "  - Identity confusion ('Who am I really?')",
        "",
        "DBT teaches four skill sets to manage this:",
        "  1. MINDFULNESS - Being present without judgment",
        "  2. DISTRESS TOLERANCE - Surviving crisis without making it worse",
        "  3. EMOTION REGULATION - Reducing vulnerability & changing emotions",
        "  4. INTERPERSONAL EFFECTIVENESS - Getting needs met in relationships",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17

    # Page 2: Wise Mind Meditation Scripts
    pdf.new_page()
    pdf.add_centered_text(740, "WISE MIND MEDITATION", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Wise Mind is the overlap of EMOTION MIND and REASONABLE MIND.",
        "",
        "EMOTION MIND: Ruled by feelings. Hot, reactive, impulsive.",
        "REASONABLE MIND: Ruled by logic. Cold, rational, disconnected.",
        "WISE MIND: Both. Intuitive knowing. Calm certainty.",
        "",
        "MEDITATION SCRIPT 1: FINDING WISE MIND",
        "",
        "Close your eyes. Take three slow breaths.",
        "Imagine walking down a spiral staircase, going deeper with each step.",
        "At the bottom is a pool of still water - this is your Wise Mind.",
        "Look into the water. What do you see? What do you know to be true?",
        "Your Wise Mind already has the answer. Listen.",
        "When ready, slowly walk back up the staircase.",
        "",
        "MEDITATION SCRIPT 2: STONE ON THE LAKE",
        "",
        "Imagine you are a flat stone thrown onto a lake.",
        "You skim the surface (Emotion Mind - reactive, choppy).",
        "Then you begin to sink slowly, gently, down through the water.",
        "Deeper... quieter... calmer...",
        "You settle on the bottom of the lake. Still. Clear. Certain.",
        "This is Wise Mind. Rest here.",
        "",
        "Today I am in: [ ] Emotion Mind  [ ] Reasonable Mind  [ ] Wise Mind",
        "What does my Wise Mind say about my current situation?",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)


    # Page 3: Observe & Describe (Non-Judgmental Stance)
    pdf.new_page()
    pdf.add_centered_text(740, "OBSERVE & DESCRIBE: NON-JUDGMENTAL STANCE", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "OBSERVE = Notice without reacting. See it like a camera.",
        "DESCRIBE = Put words on it without adding judgment.",
        "",
        "JUDGMENTAL: 'He's a terrible person for ignoring me'",
        "NON-JUDGMENTAL: 'He did not respond to my text within 2 hours'",
        "",
        "PRACTICE: Rewrite these judgments as non-judgmental observations:",
        "",
        "'I'm such an idiot' -->",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "'She's so selfish' -->", 'F4', 10)
    y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "'This day is ruined' -->", 'F4', 10)
    y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "'I can't handle anything' -->", 'F4', 10)
    y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 25
    pdf.add_text(72, y, "MY JUDGMENTS TODAY:", 'F2', 10)
    y -= 18
    pdf.add_text(72, y, "Judgment:", 'F1', 9)
    pdf.add_line(140, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Non-judgmental rewrite:", 'F1', 9)
    pdf.add_line(200, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 25
    pdf.add_text(72, y, "Judgment:", 'F1', 9)
    pdf.add_line(140, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Non-judgmental rewrite:", 'F1', 9)
    pdf.add_line(200, y - 2, 540, y - 2, 0.5, 0.5)

    # Page 4: Distress Tolerance - TIPP Skills
    pdf.new_page()
    pdf.add_centered_text(740, "DISTRESS TOLERANCE: TIPP SKILLS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "When emotions are at 7+ out of 10, use TIPP to bring them down FAST.",
        "These work with your body's nervous system to reduce arousal.",
        "",
        "T = TEMPERATURE (Ice Diving)",
        "  Hold ice cubes in hands, splash ice water on face, or hold a frozen",
        "  bag on cheeks/neck. This triggers the dive reflex and slows heart rate.",
        "  Duration: 30-60 seconds. Intensity drops 2-3 points quickly.",
        "",
        "I = INTENSE EXERCISE",
        "  Sprint, jump, do burpees, run stairs - anything to burn adrenaline.",
        "  Duration: 10-20 minutes of vigorous movement.",
        "  This metabolizes stress hormones your body released.",
        "",
        "P = PACED BREATHING",
        "  Breathe out LONGER than you breathe in.",
        "  In for 4... Out for 6... In for 4... Out for 6...",
        "  This activates the parasympathetic (calming) nervous system.",
        "  Duration: 5-10 minutes minimum.",
        "",
        "P = PAIRED MUSCLE RELAXATION",
        "  Tense each muscle group while breathing in.",
        "  Release tension while breathing out and saying 'relax' silently.",
        "  Work through: hands, arms, shoulders, face, chest, stomach, legs, feet.",
        "",
        "MY TIPP PLAN (fill in before a crisis happens):",
        "  Ice location: _______________________________________________",
        "  Exercise I can do quickly: ___________________________________",
        "  Breathing technique I'll use: _________________________________",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17


    # Page 5: STOP Skill & Reality Acceptance
    pdf.new_page()
    pdf.add_centered_text(740, "THE STOP SKILL & REALITY ACCEPTANCE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "THE STOP SKILL (use BEFORE you react impulsively):",
        "",
        "S = STOP. Freeze. Do not move. Do not react.",
        "T = TAKE A STEP BACK. Remove yourself physically or mentally.",
        "O = OBSERVE. What am I feeling? What happened? What are the facts?",
        "P = PROCEED MINDFULLY. Ask Wise Mind: What action will I not regret?",
        "",
        "PRACTICE: Last time I reacted impulsively:",
        "What happened: _______________________________________________",
        "What I did: __________________________________________________",
        "What STOP would have looked like: ______________________________",
        "",
        "REALITY ACCEPTANCE WORKSHEET:",
        "",
        "Radical Acceptance does NOT mean approval. It means acknowledging",
        "what IS, so you can respond effectively instead of fighting reality.",
        "",
        "The reality I am struggling to accept:",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "What I wish were true instead:", 'F4', 10)
    y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "The cost of NOT accepting (how does fighting reality hurt me?):", 'F4', 10)
    y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "I can accept this reality AND still:", 'F4', 10)
    y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "Turning the Mind: I choose to accept (even if I have to choose again):", 'F4', 10)
    y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)

    # Page 6: Turning the Mind & Willingness
    pdf.new_page()
    pdf.add_centered_text(740, "TURNING THE MIND EXERCISE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Acceptance is not a one-time choice. You may need to 'turn the mind'",
        "toward acceptance 100 times a day. Each time you notice you've drifted",
        "back into non-acceptance, gently turn back. Like training a puppy.",
        "",
        "WILLINGNESS vs WILLFULNESS:",
        "  WILLINGNESS: Doing what works. Responding to the situation as it is.",
        "  WILLFULNESS: Refusing to accept. Sitting on your hands. Giving up.",
        "",
        "Signs I am being WILLFUL right now:",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    for i in range(3):
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, ["Refusing to do what I know works", "Giving up / 'What's the point'", "Trying to control what I cannot control"][i], 'F1', 9)
        y -= 18
    y -= 10
    pdf.add_text(72, y, "What willingness would look like in this situation:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 10
    pdf.add_text(72, y, "HALF-SMILE & WILLING HANDS (body-based acceptance):", 'F2', 10)
    y -= 16
    pdf.add_text(72, y, "Turn palms UP. Relax fingers. Slightly lift corners of mouth.", 'F4', 10)
    y -= 16
    pdf.add_text(72, y, "This posture sends signals to your brain: 'I am open. I accept.'", 'F4', 10)
    y -= 16
    pdf.add_text(72, y, "Practice for 2 minutes while thinking about the difficult reality.", 'F4', 10)
    y -= 25
    pdf.add_text(72, y, "After practicing, distress level (0-10): _____", 'F1', 10)


    # Page 7: Emotion Regulation - Building Mastery
    pdf.new_page()
    pdf.add_centered_text(740, "EMOTION REGULATION: BUILDING MASTERY", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Building Mastery means doing something DIFFICULT each day to build",
        "confidence and a sense of competence. Start small, increase gradually.",
        "",
        "Rules: 1) It should be slightly challenging 2) Match to current mood",
        "3) It does NOT have to be productive - learning counts!",
        "",
        "MASTERY IDEAS BY DIFFICULTY LEVEL:",
        "  Easy: Make bed, send one email, cook a simple meal, organize one drawer",
        "  Medium: Exercise 20 min, learn something new, complete work task",
        "  Hard: Have a difficult conversation, try something scary, set a boundary",
        "",
        "MY BUILDING MASTERY PLAN THIS WEEK:",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for d in days:
        pdf.add_text(72, y, f"{d}:", 'F2', 9)
        pdf.add_line(140, y - 2, 400, y - 2, 0.5, 0.5)
        pdf.add_text(410, y, "Done?", 'F1', 8)
        pdf.add_rect(445, y - 3, 8, 8, 0.5, 0.3)
        y -= 20

    # Page 8: Cope Ahead Worksheet
    pdf.new_page()
    pdf.add_centered_text(740, "COPE AHEAD WORKSHEET", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Cope Ahead means rehearsing how you will handle a difficult situation",
        "BEFORE it happens. Like a mental fire drill.",
        "",
        "STEP 1: Describe the situation (who, what, where, when):",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    for i in range(2):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 5
    pdf.add_text(72, y, "STEP 2: What emotions am I likely to feel?", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "STEP 3: What urges might I have (that I want to avoid)?", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "STEP 4: What DBT skills will I use?", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 5
    pdf.add_text(72, y, "STEP 5: Imagine the scene going WELL. Visualize yourself:", 'F2', 10)
    y -= 16
    pdf.add_text(72, y, "  - Using your skills", 'F4', 10)
    y -= 14
    pdf.add_text(72, y, "  - Managing emotions without making things worse", 'F4', 10)
    y -= 14
    pdf.add_text(72, y, "  - Feeling the emotion AND still acting effectively", 'F4', 10)
    y -= 22
    pdf.add_text(72, y, "STEP 6: After the event - what actually happened?", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18

    # Page 9: Accumulating Positives
    pdf.new_page()
    pdf.add_centered_text(740, "ACCUMULATING POSITIVES", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "SHORT-TERM: Do one pleasant thing each day. Build a life worth living.",
        "",
        "My pleasant activities list (things that bring even small joy):",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    for i in range(8):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 5
    pdf.add_text(72, y, "LONG-TERM: Work toward goals that give life MEANING.", 'F2', 10)
    y -= 18
    pdf.add_text(72, y, "Values I want to live by:", 'F4', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "One long-term goal aligned with my values:", 'F4', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Next small step toward this goal:", 'F4', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "When will I take this step?", 'F4', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)


    # Page 10: Interpersonal Effectiveness - DEAR MAN
    pdf.new_page()
    pdf.add_centered_text(740, "INTERPERSONAL EFFECTIVENESS: DEAR MAN", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "DEAR MAN = Getting what you NEED while keeping self-respect.",
        "",
        "D = DESCRIBE the situation (facts only, no judgments)",
        "E = EXPRESS how you feel ('I feel...when...because...')",
        "A = ASSERT what you want (ask clearly, say no clearly)",
        "R = REINFORCE (explain the positive outcome for them too)",
        "",
        "M = MINDFUL (stay on topic, don't get distracted)",
        "A = APPEAR CONFIDENT (eye contact, steady voice, stand tall)",
        "N = NEGOTIATE (be willing to give to get)",
        "",
        "MY DEAR MAN SCRIPT (fill in for your situation):",
        "",
        "Describe:",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Express:", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Assert:", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Reinforce:", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "What I am willing to negotiate on:", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)

    # Page 11: GIVE Skill
    pdf.new_page()
    pdf.add_centered_text(740, "INTERPERSONAL EFFECTIVENESS: GIVE", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "GIVE = Building and maintaining RELATIONSHIPS.",
        "",
        "G = GENTLE (no attacks, threats, or judging)",
        "  - No 'you always' or 'you never'",
        "  - No name-calling, even in your head",
        "  - No physical intimidation or door-slamming",
        "",
        "I = INTERESTED (listen! ask questions, lean in)",
        "  - Put phone down. Make eye contact.",
        "  - Reflect back: 'So what you're saying is...'",
        "",
        "V = VALIDATE (acknowledge their feelings are real)",
        "  - 'I can see why you'd feel that way'",
        "  - 'That makes sense given your experience'",
        "  - Validation does NOT mean agreement",
        "",
        "E = EASY MANNER (lighten up, smile, use humor)",
        "  - Not everything has to be heavy",
        "  - Softening your approach gets better results",
        "",
        "PRACTICE: A relationship I want to improve:",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "One GIVE skill I will practice this week:", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "What happened when I used it:", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)

    # Page 12: FAST Skill (Saying No)
    pdf.new_page()
    pdf.add_centered_text(740, "INTERPERSONAL EFFECTIVENESS: FAST", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "FAST = Maintaining SELF-RESPECT in interactions.",
        "",
        "F = FAIR (be fair to yourself AND the other person)",
        "  - Don't over-apologize. Don't be a doormat.",
        "  - Don't bully. Both people matter equally.",
        "",
        "A = APOLOGIES (no unnecessary apologizing)",
        "  - Stop saying sorry for existing, having needs, or taking space",
        "  - Only apologize when you've actually done wrong",
        "",
        "S = STICK TO VALUES (don't compromise your integrity)",
        "  - Don't agree to things that violate your values",
        "  - Don't lie or act helpless to get what you want",
        "",
        "T = TRUTHFUL (don't exaggerate, lie, or manipulate)",
        "  - Be honest even when it's uncomfortable",
        "  - State your truth calmly and directly",
        "",
        "SAYING NO WITH FAST:",
        "  Situation requiring no: _______________________________________",
        "  My honest, fair response: _____________________________________",
        "  _______________________________________________________________",
        "  Did I apologize unnecessarily? [ ] Yes [ ] No",
        "  Did I stay true to my values? [ ] Yes [ ] No",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17


    # Page 13: Walking the Middle Path
    pdf.new_page()
    pdf.add_centered_text(740, "WALKING THE MIDDLE PATH", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Black-and-white thinking creates suffering. The middle path is BOTH/AND.",
        "",
        "Instead of ALL or NOTHING, find the synthesis:",
        "",
        "  'People are either good or bad'",
        "  MIDDLE: People are complex and can be both caring AND hurtful",
        "",
        "  'If they loved me they'd never hurt me'",
        "  MIDDLE: People can love you AND still make mistakes",
        "",
        "  'I either have total control or no control'",
        "  MIDDLE: I can influence some things while accepting others",
        "",
        "MY BLACK-AND-WHITE THOUGHTS:",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    for i in range(3):
        pdf.add_text(72, y, f"Extreme thought {i+1}:", 'F2', 9)
        pdf.add_line(180, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
        pdf.add_text(72, y, "Middle path:", 'F1', 9)
        pdf.add_line(150, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 25

    # Page 14: Validation Exercises
    pdf.new_page()
    pdf.add_centered_text(740, "VALIDATION EXERCISES", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Validation = communicating that someone's experience makes sense.",
        "6 LEVELS OF VALIDATION:",
        "",
        "Level 1: BE PRESENT (put phone down, make eye contact, listen)",
        "Level 2: REFLECT (repeat back what they said accurately)",
        "Level 3: MIND-READ (guess the emotion: 'Sounds like you're frustrated')",
        "Level 4: UNDERSTAND CAUSES ('Given what happened, that makes sense')",
        "Level 5: NORMALIZE ('Anyone would feel that way in this situation')",
        "Level 6: RADICAL GENUINENESS (treat them as capable, not fragile)",
        "",
        "SELF-VALIDATION PRACTICE:",
        "My emotion right now: ___________________________________________",
        "Level 4 (understanding causes): This makes sense because:",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Level 5 (normalizing): Anyone would feel this way because:", 'F4', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 25
    pdf.add_text(72, y, "VALIDATING OTHERS PRACTICE:", 'F2', 10)
    y -= 18
    pdf.add_text(72, y, "Person: _____________ What they expressed: _______________________", 'F1', 9)
    y -= 18
    pdf.add_text(72, y, "My validating response:", 'F1', 9)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Their reaction when I validated:", 'F1', 9)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)

    # Pages 15-19: Weekly Diary Cards (5 pages)
    for wk in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"DBT WEEKLY DIARY CARD - Week {wk}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 720
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # Emotions section
        pdf.add_text(72, y, "EMOTIONS (rate 0-5):", 'F2', 9)
        y -= 14
        pdf.add_text(72, y, "", 'F2', 7)
        for i, d in enumerate(days):
            pdf.add_text(150 + i * 52, y, d, 'F2', 7)
        y -= 12
        emotions = ["Sadness", "Anger", "Fear", "Shame", "Joy"]
        for em in emotions:
            pdf.add_text(72, y, em, 'F1', 7)
            for i in range(7):
                pdf.add_line(150 + i * 52, y - 2, 150 + i * 52 + 35, y - 2, 0.5, 0.5)
            y -= 14
        y -= 5
        # Urges section
        pdf.add_text(72, y, "URGES (rate 0-5):", 'F2', 9)
        y -= 14
        pdf.add_text(72, y, "", 'F2', 7)
        for i, d in enumerate(days):
            pdf.add_text(150 + i * 52, y, d, 'F2', 7)
        y -= 12
        urges = ["Self-harm", "Substance", "Binge/purge", "Quit therapy"]
        for u in urges:
            pdf.add_text(72, y, u, 'F1', 7)
            for i in range(7):
                pdf.add_line(150 + i * 52, y - 2, 150 + i * 52 + 35, y - 2, 0.5, 0.5)
            y -= 14
        y -= 5
        # Skills used
        pdf.add_text(72, y, "SKILLS USED (check):", 'F2', 9)
        y -= 14
        pdf.add_text(72, y, "", 'F2', 7)
        for i, d in enumerate(days):
            pdf.add_text(150 + i * 52, y, d, 'F2', 7)
        y -= 12
        skills = ["Mindfulness", "Distress Tol.", "Emotion Reg.", "Interpersonal"]
        for s in skills:
            pdf.add_text(72, y, s, 'F1', 7)
            for i in range(7):
                pdf.add_rect(150 + i * 52, y - 4, 8, 8, 0.5, 0.3)
            y -= 14
        y -= 8
        pdf.add_text(72, y, "Most helpful skill this week:", 'F2', 9)
        pdf.add_line(250, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18
        pdf.add_text(72, y, "Biggest challenge:", 'F2', 9)
        pdf.add_line(190, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18
        pdf.add_text(72, y, "What I want to work on next week:", 'F2', 9)
        pdf.add_line(280, y - 2, 540, y - 2, 0.5, 0.5)


    # Pages 20-25: Additional worksheets
    # Page 20: DEAR MAN Script 2
    pdf.new_page()
    pdf.add_centered_text(740, "DEAR MAN PRACTICE SCRIPT #2", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "Situation:", 'F2', 10)
    pdf.add_line(135, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 25
    pdf.add_text(72, y, "Person I need to talk to:", 'F2', 10)
    pdf.add_line(230, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 25
    pdf.add_text(72, y, "My goal (what do I want to happen?):", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 25
    sections = [
        ("DESCRIBE (facts only):", 3),
        ("EXPRESS (I feel...when...because...):", 3),
        ("ASSERT (what I specifically want/need):", 2),
        ("REINFORCE (benefit to them/relationship):", 2),
        ("NEGOTIATE (what I'm willing to compromise on):", 2),
    ]
    for label, lines in sections:
        pdf.add_text(72, y, label, 'F2', 10)
        y -= 16
        for _ in range(lines):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 10
    pdf.add_text(72, y, "After the conversation - how did it go?", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16

    # Page 21: Distress Tolerance Toolkit
    pdf.new_page()
    pdf.add_centered_text(740, "MY DISTRESS TOLERANCE TOOLKIT", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Fill this out NOW, before a crisis. When emotions are at 9/10,",
        "you cannot think clearly. Have your plan READY.",
        "",
        "When my distress is at 5-6/10, I will:",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 5
    pdf.add_text(72, y, "When my distress is at 7-8/10, I will:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 5
    pdf.add_text(72, y, "When my distress is at 9-10/10, I will:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 5
    pdf.add_text(72, y, "People I can call in crisis:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_text(72, y, f"{i+1}. Name: __________________ Phone: __________________", 'F1', 9)
        y -= 18
    y -= 5
    pdf.add_text(72, y, "Things that have helped me survive past crises:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18

    # Pages 22-25: Additional Cope Ahead & Skills Practice
    for pg in range(2, 6):
        pdf.new_page()
        pdf.add_centered_text(740, f"COPE AHEAD WORKSHEET #{pg}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        y = 705
        fields = [
            ("Upcoming difficult situation:", 2),
            ("Emotions I expect to feel:", 2),
            ("Urges I might have:", 2),
            ("Skills I will use (be specific):", 3),
            ("Visualize success - what does 'effective' look like?", 3),
            ("Backup plan if first skills don't work:", 2),
            ("After the event - what happened?", 3),
            ("What worked? What would I do differently?", 2),
        ]
        for label, lines in fields:
            pdf.add_text(72, y, label, 'F2', 10)
            y -= 14
            for _ in range(lines):
                pdf.add_line(72, y, 540, y, 0.5, 0.5)
                y -= 14
            y -= 8

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book95_DBT_Workbook_BPD.pdf')
    print("Book95_DBT_Workbook_BPD.pdf created successfully!")

if __name__ == "__main__":
    create_book()
