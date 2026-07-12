"""Book 217: The Complete DBT Skills Workbook"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.15)
    doc.add_centered_text(755, "THE COMPLETE DBT SKILLS", 'F2', 24, 1)
    doc.add_centered_text(725, "WORKBOOK", 'F2', 24, 1)
    doc.add_centered_text(665, "All 4 Modules in One Book", 'F4', 16, 0.3)
    doc.add_centered_text(620, "Mindfulness | Distress Tolerance", 'F1', 12, 0.4)
    doc.add_centered_text(600, "Emotion Regulation | Interpersonal Effectiveness", 'F1', 12, 0.4)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(700, "THE COMPLETE DBT SKILLS WORKBOOK", 'F2', 14)
    doc.add_centered_text(675, "All 4 Modules in One Book", 'F1', 11)
    doc.add_centered_text(620, f"Copyright {author}", 'F1', 10)
    doc.add_centered_text(600, "All rights reserved.", 'F1', 10)
    doc.add_centered_text(560, "This workbook is for educational purposes and personal growth.", 'F1', 10)
    doc.add_centered_text(540, "It is not a replacement for professional DBT therapy.", 'F1', 10)


    # Page 3: What is DBT
    doc.new_page()
    doc.add_centered_text(750, "WHAT IS DBT?", 'F2', 18)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    intro_lines = [
        "Dialectical Behavior Therapy (DBT) was developed by Dr. Marsha Linehan.",
        "It combines cognitive-behavioral techniques with mindfulness practices.",
        "",
        "DBT teaches four core skill sets:",
        "  1. MINDFULNESS - Being present and aware without judgment",
        "  2. DISTRESS TOLERANCE - Surviving crisis without making it worse",
        "  3. EMOTION REGULATION - Understanding and managing emotions",
        "  4. INTERPERSONAL EFFECTIVENESS - Getting needs met in relationships",
        "",
        "The Dialectic: Two things can be true at the same time.",
        "  - I am doing my best AND I can do better.",
        "  - I can accept myself AND want to change.",
        "  - This is painful AND I can cope with it.",
        "",
        "How to use this workbook:",
        "  - Work through each module in order or as directed by your therapist",
        "  - Practice skills daily, not just during crisis",
        "  - Use the diary cards to track your progress",
        "  - Be patient with yourself - skills take time to master",
    ]
    for line in intro_lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 18


    # Module 1: Mindfulness (5 pages)
    mindfulness_pages = [
        ("WISE MIND", ["Reasonable Mind: logical, factual, task-focused", "Emotion Mind: feelings-driven, reactive, hot",
         "Wise Mind: the overlap - intuition + logic", "", "Exercise: Think of a recent decision.",
         "What did Reasonable Mind say?", "________________________________",
         "What did Emotion Mind say?", "________________________________",
         "What does Wise Mind say?", "________________________________"]),
        ("OBSERVE", ["Notice without getting caught up in the experience.", "Just notice. Don't push away or hold on.",
         "", "Exercise: Set a timer for 3 minutes.", "Observe your breath without changing it.",
         "What did you notice?", "________________________________",
         "What pulled your attention away?", "________________________________",
         "How many times did you return to observing?", "________________________________"]),
        ("DESCRIBE", ["Put words on the experience. Label what you observe.", "Stick to facts - no interpretations.",
         "", "Exercise: Describe your current emotional state using ONLY facts:",
         "Body sensations:", "________________________________",
         "Thoughts present:", "________________________________",
         "Urges:", "________________________________",
         "Label the emotion:", "________________________________"]),
        ("PARTICIPATE", ["Throw yourself completely into the current activity.", "Become one with what you are doing.",
         "", "Exercise: Choose an activity today to fully participate in:",
         "Activity chosen:", "________________________________",
         "How long did you maintain full presence?", "________________________________",
         "What brought you back when you drifted?", "________________________________",
         "How did it feel to be fully present?", "________________________________"]),
        ("NON-JUDGMENTAL STANCE", ["See but don't evaluate. Take a non-judgmental stance.",
         "Replace judgments with facts.", "",
         "Judgmental thought:", "________________________________",
         "Rewritten without judgment:", "________________________________",
         "Judgmental thought:", "________________________________",
         "Rewritten without judgment:", "________________________________",
         "Judgmental thought:", "________________________________",
         "Rewritten without judgment:", "________________________________"]),
    ]
    for title, content in mindfulness_pages:
        doc.new_page()
        doc.add_centered_text(755, "MODULE 1: MINDFULNESS", 'F2', 12, 0.4)
        doc.add_centered_text(730, title, 'F2', 16)
        doc.add_line(72, 718, 540, 718, 0.5, 0.3)
        y = 695
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 20


    # Module 2: Distress Tolerance (8 pages)
    dt_pages = [
        ("TIPP - Change Body Chemistry", ["T - Temperature: Cold water on face (dive reflex)", "I - Intense Exercise: 20 min to reduce emotional arousal",
         "P - Paced Breathing: exhale longer than inhale", "P - Progressive Relaxation: tense & release muscles",
         "", "My TIPP plan:", "When distress is at 7+, I will:", "________________________________",
         "Cold items I keep available:", "________________________________"]),
        ("STOP SKILL", ["S - Stop. Don't react. Freeze.", "T - Take a step back. Breathe.",
         "O - Observe. What's happening inside and outside?", "P - Proceed mindfully. Act with awareness.",
         "", "Recent situation I could have used STOP:", "________________________________",
         "What happened instead:", "________________________________",
         "How STOP could have changed the outcome:", "________________________________"]),
        ("PROS AND CONS", ["Crisis urge I'm having:", "________________________________",
         "", "ACTING on urge - PROS:", "________________________________",
         "ACTING on urge - CONS:", "________________________________",
         "NOT acting on urge - PROS:", "________________________________",
         "NOT acting on urge - CONS:", "________________________________",
         "", "My decision:", "________________________________"]),
        ("SELF-SOOTHE WITH 5 SENSES", ["Vision - What I can look at:", "________________________________",
         "Hearing - What I can listen to:", "________________________________",
         "Smell - What scents comfort me:", "________________________________",
         "Taste - What flavors help:", "________________________________",
         "Touch - What textures soothe:", "________________________________",
         "", "My personalized self-soothe kit:", "________________________________"]),
        ("IMPROVE THE MOMENT", ["I - Imagery (safe place visualization)", "M - Meaning (find purpose in pain)",
         "P - Prayer/meditation", "R - Relaxation", "O - One thing in the moment",
         "V - Vacation (brief mental escape)", "E - Encouragement (self-talk)",
         "", "My go-to IMPROVE skills:", "________________________________",
         "________________________________"]),
        ("RADICAL ACCEPTANCE", ["What I'm resisting accepting:", "________________________________",
         "Evidence it IS reality:", "________________________________",
         "Causes that led to this:", "________________________________",
         "Can I change this? (yes/no):", "________________________________",
         "What life is worth living looks like even with this:", "________________________________",
         "", "Acceptance statement: I accept that _______________",
         "even though I don't like it or approve of it."]),
        ("TURNING THE MIND", ["Acceptance is not a one-time choice - it must be made again and again.",
         "", "Situation requiring acceptance:", "________________________________",
         "Times today I turned AWAY from acceptance:", "________________________________",
         "What pulled me away:", "________________________________",
         "My commitment to turn back:", "________________________________",
         "Reminder I can post where I'll see it:", "________________________________"]),
        ("WILLINGNESS VS. WILLFULNESS", ["Willingness: doing what is needed, being open",
         "Willfulness: refusing to accept, sitting on hands, giving up",
         "", "Where am I being willful?", "________________________________",
         "What would willingness look like?", "________________________________",
         "One willing action I can take today:", "________________________________",
         "What's blocking my willingness?", "________________________________"]),
    ]
    for title, content in dt_pages:
        doc.new_page()
        doc.add_centered_text(755, "MODULE 2: DISTRESS TOLERANCE", 'F2', 12, 0.4)
        doc.add_centered_text(730, title, 'F2', 14)
        doc.add_line(72, 718, 540, 718, 0.5, 0.3)
        y = 695
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 20


    # Module 3: Emotion Regulation (8 pages)
    er_pages = [
        ("NAMING EMOTIONS", ["What am I feeling right now?", "Primary emotion:", "________________________________",
         "Secondary emotion (what came after):", "________________________________",
         "Body sensation:", "________________________________",
         "Intensity (0-10):", "___", "Urge that comes with this emotion:", "________________________________",
         "Is this emotion justified by the facts?", "________________________________"]),
        ("EMOTION MYTHS", ["Myth: There is a right way to feel in every situation.",
         "Reality:", "________________________________",
         "Myth: Letting others know I am feeling bad is weakness.",
         "Reality:", "________________________________",
         "Myth: Negative feelings are bad and destructive.",
         "Reality:", "________________________________",
         "Myth: Being emotional means being out of control.",
         "Reality:", "________________________________",
         "My personal emotion myth:", "________________________________",
         "The truth:", "________________________________"]),
        ("OPPOSITE ACTION", ["Emotion I want to change:", "________________________________",
         "Is it justified by the facts? (yes/no):", "___",
         "Action urge that goes with this emotion:", "________________________________",
         "OPPOSITE action:", "________________________________",
         "Did I act opposite ALL THE WAY?", "________________________________",
         "Result:", "________________________________"]),
        ("ABC PLEASE", ["A - Accumulate positives (short-term):", "________________________________",
         "A - Accumulate positives (long-term goals):", "________________________________",
         "B - Build mastery (what did I do well?):", "________________________________",
         "C - Cope ahead (upcoming difficult situation):", "________________________________",
         "Plan:", "________________________________",
         "", "PL - treat PhysicaL illness", "E - balanced Eating",
         "A - avoid mood-Altering substances", "S - balanced Sleep", "E - get Exercise"]),
        ("BUILDING MASTERY", ["Do one thing each day to feel competent and in control.",
         "", "Day 1 mastery activity:", "________________________________",
         "Day 2:", "________________________________", "Day 3:", "________________________________",
         "Day 4:", "________________________________", "Day 5:", "________________________________",
         "Day 6:", "________________________________", "Day 7:", "________________________________",
         "", "How did building mastery affect my mood?", "________________________________"]),
        ("COPE AHEAD", ["Describe the situation:", "________________________________",
         "________________________________",
         "Emotions/actions I want to AVOID:", "________________________________",
         "Skills I will use:", "________________________________",
         "Step-by-step plan:", "1. ________________________________",
         "2. ________________________________", "3. ________________________________",
         "Potential obstacles:", "________________________________",
         "How I'll handle obstacles:", "________________________________",
         "Rehearsal: I visualized this (date):", "___________"]),
        ("CHECK THE FACTS", ["Emotion:", "___________  Intensity (0-10): ___",
         "Prompting event (facts only):", "________________________________",
         "My interpretation:", "________________________________",
         "Other possible interpretations:", "________________________________",
         "________________________________",
         "Am I assuming a threat?", "________________________________",
         "What's the actual probability?", "________________________________",
         "If it happens, can I cope?", "________________________________",
         "Does my emotion fit the FACTS?", "________________________________"]),
        ("EMOTION REGULATION PLAN", ["My most problematic emotion:", "________________________________",
         "Triggers:", "________________________________",
         "Early warning signs:", "________________________________",
         "Skills that work for this emotion:", "________________________________",
         "________________________________",
         "People who can help:", "________________________________",
         "Self-care that prevents this emotion:", "________________________________",
         "My commitment:", "________________________________"]),
    ]
    for title, content in er_pages:
        doc.new_page()
        doc.add_centered_text(755, "MODULE 3: EMOTION REGULATION", 'F2', 12, 0.4)
        doc.add_centered_text(730, title, 'F2', 14)
        doc.add_line(72, 718, 540, 718, 0.5, 0.3)
        y = 695
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 20


    # Module 4: Interpersonal Effectiveness (8 pages)
    ie_pages = [
        ("DEAR MAN - Getting What You Want", ["D - Describe the situation (facts only)",
         "E - Express how you feel (I statements)", "A - Assert what you need (ask clearly)",
         "R - Reinforce (explain benefits to them)", "", "M - Mindful (stay on topic, broken record)",
         "A - Appear confident (eye contact, tone)", "N - Negotiate (be willing to give to get)",
         "", "Situation:", "________________________________",
         "My DEAR MAN script:", "________________________________",
         "________________________________", "________________________________"]),
        ("GIVE - Keeping the Relationship", ["G - Gentle (no attacks, threats, or judging)",
         "I - Interested (listen, appear interested)", "V - Validate (acknowledge their feelings)",
         "E - Easy manner (smile, be light, humor)", "",
         "Person:", "________________________________",
         "How I will be Gentle:", "________________________________",
         "How I will show Interest:", "________________________________",
         "How I will Validate:", "________________________________",
         "How I will keep it Easy:", "________________________________"]),
        ("FAST - Keeping Self-Respect", ["F - Fair (be fair to yourself AND others)",
         "A - Apologies (no over-apologizing)", "S - Stick to values (don't sell out)",
         "T - Truthful (no lying, no helplessness act)", "",
         "Value at stake:", "________________________________",
         "What I will NOT apologize for:", "________________________________",
         "Where I am being unfair to myself:", "________________________________",
         "Truth I need to tell:", "________________________________"]),
        ("PRIORITIES - What Matters Most?", ["In this interaction, what matters MOST?",
         "[ ] Getting what I want (DEAR MAN focus)",
         "[ ] Keeping the relationship (GIVE focus)",
         "[ ] Keeping my self-respect (FAST focus)", "",
         "Why this is my priority:", "________________________________",
         "What I'm willing to sacrifice:", "________________________________",
         "What I'm NOT willing to sacrifice:", "________________________________",
         "Ideal outcome:", "________________________________"]),
        ("SAYING NO", ["Saying no is not selfish - it is self-respecting.", "",
         "Request I need to decline:", "________________________________",
         "Why I'm saying no:", "________________________________",
         "My NO script:", "________________________________",
         "________________________________",
         "If they push back, I will:", "________________________________",
         "I have a right to say no because:", "________________________________",
         "", "Broken record technique: repeat your no calmly and briefly."]),
        ("BUILDING RELATIONSHIPS", ["Relationships need investment. What am I investing?", "",
         "Relationship I want to strengthen:", "________________________________",
         "What they need from me:", "________________________________",
         "What I need from them:", "________________________________",
         "One thing I can do this week:", "________________________________",
         "Barriers to connection:", "________________________________",
         "Skills I need to use:", "________________________________",
         "", "My relationship maintenance plan:",
         "Daily:", "________________________________",
         "Weekly:", "________________________________"]),
        ("INTERPERSONAL PATTERNS", ["My common patterns in relationships:", "",
         "Pattern 1:", "________________________________",
         "How it hurts me:", "________________________________",
         "Skill to change it:", "________________________________", "",
         "Pattern 2:", "________________________________",
         "How it hurts me:", "________________________________",
         "Skill to change it:", "________________________________", "",
         "Pattern 3:", "________________________________",
         "How it hurts me:", "________________________________",
         "Skill to change it:", "________________________________"]),
        ("VALIDATION", ["6 Levels of Validation:", "1. Pay attention (be present)",
         "2. Reflect back (repeat what they said)", "3. Mind-read (guess their feelings)",
         "4. Understand causes (makes sense given history)", "5. Acknowledge the valid (find kernel of truth)",
         "6. Radical genuineness (treat as equal)", "",
         "Person I want to validate better:", "________________________________",
         "Level I usually reach:", "___",
         "Level I want to practice:", "___",
         "How I will practice:", "________________________________"]),
    ]
    for title, content in ie_pages:
        doc.new_page()
        doc.add_centered_text(755, "MODULE 4: INTERPERSONAL EFFECTIVENESS", 'F2', 12, 0.4)
        doc.add_centered_text(730, title, 'F2', 14)
        doc.add_line(72, 718, 540, 718, 0.5, 0.3)
        y = 695
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 20


    # Weekly Diary Cards (8 pages)
    for week in range(1, 9):
        doc.new_page()
        doc.add_centered_text(760, f"WEEKLY DIARY CARD - WEEK {week}", 'F2', 13)
        doc.add_line(72, 748, 540, 748, 0.5, 0.3)
        y = 725
        doc.add_text(72, y, "Rate each 0-5 (0=not at all, 5=extremely)", 'F1', 8)
        y -= 20
        # Header
        doc.add_text(72, y, "Day", 'F2', 8)
        headers = ["Joy", "Sad", "Anger", "Shame", "Fear", "Urges", "Skills Used"]
        x_pos = [140, 175, 210, 250, 290, 330, 385]
        for h, x in zip(headers, x_pos):
            doc.add_text(x, y, h, 'F2', 8)
        y -= 5
        doc.add_line(72, y, 540, y, 0.5, 0.3)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in days:
            y -= 22
            doc.add_text(72, y, day, 'F1', 9)
            for x in x_pos[:6]:
                doc.add_text(x+5, y, "___", 'F1', 9)
            doc.add_line(385, y-2, 540, y-2, 0.5, 0.5)
        y -= 30
        doc.add_text(72, y, "Skills practiced this week:", 'F2', 9)
        y -= 15
        doc.add_text(72, y, "[ ] Mindfulness  [ ] Distress Tolerance  [ ] Emotion Regulation  [ ] Interpersonal", 'F1', 8)
        y -= 25
        doc.add_text(72, y, "Highest distress level (0-10): ___  Skills used in crisis:", 'F1', 9)
        doc.add_line(355, y-2, 540, y-2, 0.5, 0.4)
        y -= 25
        doc.add_text(72, y, "Wise Mind moments:", 'F1', 9)
        doc.add_line(175, y-2, 540, y-2, 0.5, 0.4)

    # Crisis Survival Plan
    doc.new_page()
    doc.add_centered_text(755, "MY CRISIS SURVIVAL PLAN", 'F2', 16)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 710
    sections = [
        "Warning signs that a crisis is building:",
        "________________________________",
        "________________________________",
        "",
        "My distress tolerance skills (in order of use):",
        "1. ________________________________",
        "2. ________________________________",
        "3. ________________________________",
        "4. ________________________________",
        "5. ________________________________",
        "",
        "People I can call for support:",
        "1. ______________ Phone: ______________",
        "2. ______________ Phone: ______________",
        "3. ______________ Phone: ______________",
        "",
        "Professional resources:",
        "Therapist: ______________ Phone: ______________",
        "Crisis line: 988",
        "Emergency: 911",
        "",
        "Reasons to stay alive / things worth living for:",
        "1. ________________________________",
        "2. ________________________________",
        "3. ________________________________",
    ]
    for line in sections:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 20

    # Skills I've Mastered
    doc.new_page()
    doc.add_centered_text(755, "SKILLS I'VE MASTERED", 'F2', 16)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Check off skills as you master them:", 'F1', 10)
    y -= 25
    modules = {
        "MINDFULNESS": ["Wise Mind", "Observe", "Describe", "Participate", "Non-judgmental"],
        "DISTRESS TOLERANCE": ["TIPP", "STOP", "Pros/Cons", "Self-Soothe", "IMPROVE", "Radical Acceptance"],
        "EMOTION REGULATION": ["Naming Emotions", "Opposite Action", "ABC PLEASE", "Check the Facts", "Cope Ahead"],
        "INTERPERSONAL": ["DEAR MAN", "GIVE", "FAST", "Saying No", "Validation"],
    }
    for mod, skills in modules.items():
        doc.add_text(72, y, mod, 'F2', 10)
        y -= 18
        for skill in skills:
            doc.add_text(90, y, f"[ ] {skill}", 'F1', 9)
            y -= 15
        y -= 10

    # My DBT Journey Reflection
    doc.new_page()
    doc.add_centered_text(755, "MY DBT JOURNEY REFLECTION", 'F2', 16)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 710
    prompts = [
        "When I started DBT, I was:", "________________________________", "________________________________", "",
        "The hardest module for me was:", "________________________________",
        "Because:", "________________________________", "",
        "The skill that changed my life:", "________________________________",
        "How it changed things:", "________________________________", "",
        "My biggest growth:", "________________________________", "________________________________", "",
        "What I want to keep working on:", "________________________________", "________________________________", "",
        "My commitment to myself:", "________________________________", "________________________________",
    ]
    for line in prompts:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 22

    doc.save("Book217_DBT_Complete_Workbook.pdf")
    print("Created: Book217_DBT_Complete_Workbook.pdf")

if __name__ == "__main__":
    create_book()
