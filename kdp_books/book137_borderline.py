"""Book 137: BPD Recovery Workbook - Skills for Emotional Stability & Healthier Relationships"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(520, "BPD RECOVERY WORKBOOK", 'F2', 26, 0)
    doc.add_centered_text(485, "Skills for Emotional Stability", 'F4', 18, 0.2)
    doc.add_centered_text(460, "& Healthier Relationships", 'F4', 18, 0.2)
    doc.add_centered_text(380, "DBT-Informed Exercises Including:", 'F1', 13, 0.3)
    doc.add_centered_text(355, "Wise Mind | STOP Skill | Radical Acceptance", 'F1', 12, 0.3)
    doc.add_centered_text(335, "DEAR MAN | Opposite Action | Diary Cards", 'F1', 12, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(600, "BPD RECOVERY WORKBOOK", 'F2', 14, 0)
    doc.add_text(72, 500, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.3)
    doc.add_text(72, 480, "This workbook is for educational purposes only.", 'F1', 10, 0.3)
    doc.add_text(72, 460, "It is not a substitute for professional DBT therapy or mental health treatment.", 'F1', 10, 0.3)
    doc.add_text(72, 430, "If you are in crisis, call 988 (Suicide & Crisis Lifeline).", 'F2', 10, 0.3)

    # Page 3: Understanding BPD
    doc.new_page()
    doc.add_centered_text(740, "UNDERSTANDING BPD", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Borderline Personality Disorder is characterized by:", 'F1', 11, 0.2)
    features = ["Intense and unstable emotions that change rapidly",
                "Fear of abandonment (real or imagined)",
                "Unstable relationships (idealization/devaluation)",
                "Unstable sense of self/identity",
                "Impulsive behaviors (spending, substances, risky behavior)",
                "Chronic feelings of emptiness",
                "Intense anger that is hard to control",
                "Dissociation under stress",
                "Self-harm or suicidal thoughts"]
    y = 675
    for f in features:
        doc.add_text(90, y, f"- {f}", 'F1', 11, 0.2)
        y -= 20
    y -= 15
    doc.add_text(72, y, "IMPORTANT: BPD is NOT a life sentence. With skills training (like DBT),", 'F2', 11, 0)
    y -= 18
    doc.add_text(72, y, "many people achieve significant recovery.", 'F2', 11, 0)

    # Page 4: Emotional Intensity Scale
    doc.new_page()
    doc.add_centered_text(740, "EMOTIONAL INTENSITY SCALE", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Rate your emotional intensity to choose the right skill:", 'F1', 11, 0.2)
    levels = [
        ("1-2: Calm", "Practice mindfulness, build positive experiences"),
        ("3-4: Mild distress", "Use Wise Mind, check the facts"),
        ("5-6: Moderate distress", "Opposite Action, TIPP skills"),
        ("7-8: High distress", "STOP skill, crisis survival strategies"),
        ("9-10: Crisis", "TIP (Temperature/Intense exercise/Paced breathing), call support")
    ]
    y = 670
    for level, skill in levels:
        doc.add_filled_rect(72, y-3, 468, 22, 0.9)
        doc.add_text(75, y, level, 'F2', 11, 0)
        doc.add_text(250, y, skill, 'F1', 10, 0.3)
        y -= 35
    y -= 20
    doc.add_text(72, y, "MY INTENSITY LOG:", 'F2', 12, 0)
    y -= 25
    doc.add_filled_rect(72, y-2, 468, 18, 0.85)
    doc.add_text(75, y, "Date/Time", 'F2', 9, 0)
    doc.add_text(170, y, "Emotion", 'F2', 9, 0)
    doc.add_text(270, y, "Intensity (1-10)", 'F2', 9, 0)
    doc.add_text(380, y, "Skill Used", 'F2', 9, 0)
    y -= 25
    for i in range(10):
        doc.add_rect(72, y, 468, 25)
        y -= 27

    # Pages 5-7: Wise Mind Exercises (3 pages)
    wise_mind_exercises = [
        ("WISE MIND MEDITATION",
         ["Find a comfortable position and close your eyes",
          "Breathe in... imagine breathing in wisdom",
          "Breathe out... release judgment",
          "Ask yourself: What does my Wise Mind know right now?",
          "Wait for the answer to come - don't force it",
          "Wise Mind speaks quietly. It doesn't argue or justify."]),
        ("WISE MIND PRACTICE: Stone on the Lake",
         ["Imagine you are a lake... vast, deep, calm",
          "Emotions are stones thrown into your surface",
          "They create ripples (Emotion Mind) but do not change the depths",
          "Your depths remain still and knowing (Wise Mind)",
          "Let the stone sink... observe it... let the surface settle"]),
        ("WISE MIND WORKSHEET",
         ["What does EMOTION MIND say? ________________________________",
          "What does REASONABLE MIND say? _____________________________",
          "What does WISE MIND say? ___________________________________",
          "How do I know this is Wise Mind? ____________________________",
          "What action aligns with Wise Mind? __________________________"])
    ]
    for title, content in wise_mind_exercises:
        doc.new_page()
        doc.add_centered_text(740, title, 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 700
        for line in content:
            doc.add_text(90, y, line, 'F1', 11, 0.2)
            y -= 25
        y -= 20
        doc.add_text(72, y, "Reflections:", 'F2', 12, 0)
        y -= 25
        for i in range(8):
            doc.add_text(72, y, "_" * 70, 'F1', 11, 0.3)
            y -= 25

    # Pages 8-12: STOP Skill Practice (5 pages)
    for page_num in range(5):
        doc.new_page()
        doc.add_centered_text(740, f"STOP SKILL PRACTICE ({page_num+1}/5)", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 700
        doc.add_text(72, y, "S - STOP: Don't react. Freeze.", 'F2', 12, 0)
        y -= 22
        doc.add_text(72, y, "T - TAKE A STEP BACK: Breathe. Don't act on impulse.", 'F2', 12, 0)
        y -= 22
        doc.add_text(72, y, "O - OBSERVE: What is happening? What am I feeling?", 'F2', 12, 0)
        y -= 22
        doc.add_text(72, y, "P - PROCEED MINDFULLY: Act with Wise Mind.", 'F2', 12, 0)
        y -= 35
        doc.add_text(72, y, f"Situation {page_num*2+1}:", 'F2', 11, 0.1)
        y -= 22
        doc.add_text(72, y, "What happened: ____________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "My urge/impulse: __________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "S - I stopped by: _________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "T - I stepped back by: ____________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "O - I observed: ___________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "P - I proceeded by: _______________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "Outcome: __________________________________________________________", 'F1', 11, 0.2)
        y -= 40
        doc.add_text(72, y, f"Situation {page_num*2+2}:", 'F2', 11, 0.1)
        y -= 22
        doc.add_text(72, y, "What happened: ____________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "My urge/impulse: __________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "S - I stopped by: _________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "T - I stepped back by: ____________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "O - I observed: ___________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "P - I proceeded by: _______________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "Outcome: __________________________________________________________", 'F1', 11, 0.2)

    # Pages 13-16: Radical Acceptance (4 pages)
    for page_num in range(4):
        doc.new_page()
        doc.add_centered_text(740, f"RADICAL ACCEPTANCE WORKSHEET ({page_num+1}/4)", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        if page_num == 0:
            doc.add_text(72, 700, "Radical Acceptance means:", 'F2', 12, 0)
            doc.add_text(90, 675, "- Accepting reality AS IT IS (not approving of it)", 'F1', 11, 0.2)
            doc.add_text(90, 655, "- Letting go of fighting against what already happened", 'F1', 11, 0.2)
            doc.add_text(90, 635, "- Choosing to stop adding suffering to pain", 'F1', 11, 0.2)
            doc.add_text(72, 600, "Pain + Non-Acceptance = SUFFERING", 'F2', 12, 0)
            doc.add_text(72, 578, "Pain + Acceptance = PAIN (just pain, which passes)", 'F2', 12, 0)
            y = 540
        else:
            y = 700
        doc.add_text(72, y, "What I need to accept: ____________________________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "Ways I am fighting reality: ________________________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "The cost of non-acceptance (how is fighting making things worse?):", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "Turning the mind statement (I choose to accept...): _________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "Half-smile practice: Can I relax my face and half-smile? ____________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "Willing hands: Can I unclench and open my palms? ___________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "How I feel after practicing acceptance: ____________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)

    # Pages 17-21: DEAR MAN Scripts (5 pages)
    scenarios = [
        "Asking for a raise/promotion at work",
        "Setting a boundary with a family member",
        "Expressing needs to a romantic partner",
        "Saying no to an unreasonable request",
        "Addressing a conflict with a friend"
    ]
    for i, scenario in enumerate(scenarios):
        doc.new_page()
        doc.add_centered_text(740, f"DEAR MAN: {scenario}", 'F2', 12, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 700
        steps = [
            ("D - DESCRIBE:", "State the facts of the situation (no judgments):"),
            ("E - EXPRESS:", "Share how you feel about it (use 'I' statements):"),
            ("A - ASSERT:", "Ask clearly for what you want/need:"),
            ("R - REINFORCE:", "Explain the positive effects if they cooperate:"),
            ("M - MINDFUL:", "Stay focused, don't get sidetracked. Broken record:"),
            ("A - APPEAR CONFIDENT:", "Eye contact, steady voice, stand tall:"),
            ("N - NEGOTIATE:", "Be willing to give to get. My compromise:")
        ]
        for step_title, step_desc in steps:
            doc.add_text(72, y, step_title, 'F2', 11, 0)
            y -= 18
            doc.add_text(72, y, step_desc, 'F1', 10, 0.3)
            y -= 20
            doc.add_text(72, y, "_______________________________________________________________", 'F1', 10, 0.3)
            y -= 18
            doc.add_text(72, y, "_______________________________________________________________", 'F1', 10, 0.3)
            y -= 28

    # Pages 22-25: Opposite Action (4 pages)
    emotions = [
        ("ANGER", "Urge: Attack, yell, slam things", "Opposite: Gently avoid, be kind, take space"),
        ("SHAME", "Urge: Hide, isolate, keep secrets", "Opposite: Share with safe person, hold head up"),
        ("FEAR", "Urge: Avoid, escape, freeze", "Opposite: Approach what you fear (if safe)"),
        ("SADNESS", "Urge: Withdraw, stay in bed, isolate", "Opposite: Get active, reach out, engage")
    ]
    for emotion, urge, opposite in emotions:
        doc.new_page()
        doc.add_centered_text(740, f"OPPOSITE ACTION: {emotion}", 'F2', 16, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        doc.add_text(72, 700, urge, 'F1', 11, 0.2)
        doc.add_text(72, 678, opposite, 'F2', 11, 0)
        y = 640
        doc.add_text(72, y, "Situation: __________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Emotion intensity before (0-10): ___", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Is my emotion JUSTIFIED by the facts? (Check the facts first)", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Even if justified, is ACTING on the urge EFFECTIVE? ________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "My opposite action plan: ____________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Did I act ALL THE WAY opposite? (half measures don't work): _________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Emotion intensity after (0-10): ___", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "What I noticed: _____________________________________________________", 'F1', 11, 0.2)

    # Page 26: Building a Life Worth Living
    doc.new_page()
    doc.add_centered_text(740, "BUILDING A LIFE WORTH LIVING", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "VALUES - What matters most to me:", 'F2', 12, 0)
    y = 675
    values_cats = ["Relationships:", "Work/Purpose:", "Health:", "Fun/Leisure:", "Spirituality:"]
    for v in values_cats:
        doc.add_text(72, y, f"{v} _______________________________________________________", 'F1', 11, 0.2)
        y -= 28
    y -= 10
    doc.add_text(72, y, "GOALS aligned with my values:", 'F2', 12, 0)
    y -= 25
    doc.add_text(72, y, "Short-term (this week): _____________________________________________", 'F1', 11, 0.2)
    y -= 25
    doc.add_text(72, y, "Medium-term (this month): ___________________________________________", 'F1', 11, 0.2)
    y -= 25
    doc.add_text(72, y, "Long-term (this year): ______________________________________________", 'F1', 11, 0.2)
    y -= 35
    doc.add_text(72, y, "POSITIVE EXPERIENCES to build into my life:", 'F2', 12, 0)
    y -= 25
    for i in range(5):
        doc.add_text(72, y, f"{i+1}. _______________________________________________________________", 'F1', 11, 0.2)
        y -= 22

    # Page 27: My Crisis Plan
    doc.new_page()
    doc.add_centered_text(740, "MY CRISIS PLAN", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Warning signs I'm heading toward crisis:", 'F2', 12, 0)
    y = 675
    for i in range(3):
        doc.add_text(72, y, f"{i+1}. _______________________________________________________________", 'F1', 11, 0.2)
        y -= 22
    y -= 15
    doc.add_text(72, y, "Distress tolerance skills to try FIRST:", 'F2', 12, 0)
    y -= 22
    skills = ["TIPP (Temperature, Intense exercise, Paced breathing, Paired relaxation)",
              "Self-soothe with 5 senses", "IMPROVE the moment", "Pros and cons of acting on urge"]
    for s in skills:
        doc.add_text(90, y, f"- {s}", 'F1', 10, 0.3)
        y -= 18
    y -= 15
    doc.add_text(72, y, "People I can call:", 'F2', 12, 0)
    y -= 22
    for i in range(3):
        doc.add_text(72, y, f"Name: ___________________  Phone: ___________________", 'F1', 11, 0.2)
        y -= 22
    y -= 15
    doc.add_text(72, y, "Professional support:", 'F2', 12, 0)
    y -= 22
    doc.add_text(72, y, "Therapist: ________________________  Phone: ___________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "Crisis line: 988 Suicide & Crisis Lifeline", 'F2', 11, 0)
    y -= 22
    doc.add_text(72, y, "Crisis Text Line: Text HOME to 741741", 'F1', 11, 0.2)

    # Pages 28-32: Daily Diary Card (5 pages)
    for page_num in range(5):
        doc.new_page()
        doc.add_centered_text(740, f"DAILY DIARY CARD - Week {page_num+1}", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # Header
        doc.add_filled_rect(72, 695, 468, 18, 0.85)
        doc.add_text(75, 698, "Category", 'F2', 8, 0)
        x = 145
        for d in days:
            doc.add_text(x, 698, d, 'F2', 8, 0)
            x += 57
        y = 675
        categories = ["Emotions (0-5)", "Urges to self-harm", "Urges to use substances",
                      "Mindfulness practice", "Interpersonal skill", "Emotion regulation",
                      "Distress tolerance", "Skills used (list)", "Medications taken"]
        for cat in categories:
            doc.add_text(75, y+3, cat, 'F3', 7, 0.2)
            x = 145
            for d in days:
                doc.add_rect(x-5, y-2, 52, 18)
                x += 57
            y -= 22
        y -= 10
        doc.add_text(72, y, "Notes: _____________________________________________________________", 'F1', 10, 0.2)

    # Page 33: Recovery Milestones
    doc.new_page()
    doc.add_centered_text(740, "MY BPD RECOVERY MILESTONES", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Celebrate every step forward, no matter how small:", 'F1', 11, 0.2)
    y = 670
    milestones = [
        "Used a skill instead of acting on an urge",
        "Went a full day without self-harm",
        "Expressed a need without exploding",
        "Accepted something I couldn't change",
        "Stayed in Wise Mind during conflict",
        "Asked for help appropriately",
        "Completed a full week of diary cards",
        "Repaired a relationship after conflict",
        "Recognized an emotion before it escalated",
        "Chose opposite action successfully"
    ]
    for m in milestones:
        doc.add_rect(72, y-3, 15, 15)
        doc.add_text(95, y, m, 'F1', 11, 0.2)
        doc.add_text(430, y, "Date: ___________", 'F1', 10, 0.3)
        y -= 28
    y -= 20
    doc.add_text(72, y, "You are NOT your diagnosis. You are a whole person learning new skills.", 'F2', 11, 0)
    y -= 22
    doc.add_text(72, y, "Recovery is possible. You deserve a life worth living.", 'F2', 11, 0)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book137_BPD_Recovery_Workbook.pdf')
    print("Book137_BPD_Recovery_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
