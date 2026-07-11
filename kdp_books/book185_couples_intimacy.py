#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(420, "REBUILDING INTIMACY", 'F2', 18)
pdf.add_centered_text(390, "A Workbook for Couples Reconnecting", 'F4', 12)
pdf.add_centered_text(355, f"By {author}", 'F4', 11)
pdf.add_line(80, 335, 352, 335, 2)

# Page 2 - Copyright + What is Intimacy
pdf.new_page()
pdf.add_centered_text(620, f"Copyright - {author}", 'F1', 9)
pdf.add_centered_text(605, "All rights reserved.", 'F1', 9)
pdf.add_centered_text(570, "WHAT IS INTIMACY?", 'F2', 14)
pdf.add_line(40, 558, 392, 558, 1)
pdf.add_text(40, 540, "Intimacy is much more than physical connection.", 'F1', 10)
pdf.add_text(40, 520, "TRUE INTIMACY HAS 5 DIMENSIONS:", 'F2', 10)
dims = [
    ("Emotional:", "Sharing feelings, being vulnerable, feeling understood"),
    ("Physical:", "Touch, affection, sexual connection"),
    ("Intellectual:", "Sharing ideas, learning together, stimulating conversation"),
    ("Spiritual:", "Shared values, meaning-making, purpose together"),
    ("Experiential:", "Shared adventures, creating memories, trying new things"),
]
y = 500
for name, desc in dims:
    pdf.add_text(45, y, name, 'F2', 9)
    pdf.add_text(110, y, desc, 'F1', 8)
    y -= 18
pdf.add_text(40, y-10, "Which dimension needs the most attention in your relationship?", 'F4', 9, 0.3)
pdf.add_text(40, y-25, "Partner 1: ___________________", 'F1', 9)
pdf.add_text(40, y-40, "Partner 2: ___________________", 'F1', 9)

# Page 3 - Intimacy Assessment
pdf.new_page()
pdf.add_centered_text(620, "INTIMACY ASSESSMENT", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 593, "Both partners rate each area 1-10 (1=disconnected, 10=deeply connected):", 'F1', 9)
areas = ["Emotional safety/vulnerability", "Physical affection (non-sexual touch)",
         "Sexual satisfaction", "Intellectual stimulation",
         "Spiritual connection", "Fun & adventure together",
         "Communication quality", "Trust level",
         "Feeling prioritized", "Overall relationship satisfaction"]
y = 573
pdf.add_text(40, y, "AREA", 'F2', 8)
pdf.add_text(260, y, "P1", 'F2', 8)
pdf.add_text(300, y, "P2", 'F2', 8)
pdf.add_text(340, y, "Gap", 'F2', 8)
y -= 5
pdf.add_line(40, y, 392, y, 0.5)
y -= 14
for a in areas:
    pdf.add_text(40, y, a, 'F1', 8)
    pdf.add_text(260, y, "___", 'F1', 8)
    pdf.add_text(300, y, "___", 'F1', 8)
    pdf.add_text(340, y, "___", 'F1', 8)
    y -= 16
pdf.add_text(40, y-10, "Biggest gap to address first:", 'F2', 9)
pdf.add_line(40, y-25, 392, y-25, 0.5, 0.7)

# Page 4 - Communication About Desires
pdf.new_page()
pdf.add_centered_text(620, "COMMUNICATING ABOUT DESIRES", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Use these sentence starters to express needs safely:", 'F1', 9)
starters = [
    "'I feel most connected to you when...'",
    "'Something I'd love more of is...'",
    "'I feel disconnected when...'",
    "'A way you could help me feel safe is...'",
    "'Something I've been wanting to try...'",
    "'What I need right now is...'",
]
y = 570
for s in starters:
    pdf.add_text(50, y, s, 'F4', 9)
    y -= 14
pdf.add_text(40, y-10, "PARTNER 1 - My desires & needs:", 'F2', 10)
y -= 28
for i in range(4):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14
pdf.add_text(40, y-5, "PARTNER 2 - My desires & needs:", 'F2', 10)
y -= 22
for i in range(4):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14


# Page 5 - Barriers to Intimacy
pdf.new_page()
pdf.add_centered_text(620, "BARRIERS TO INTIMACY", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Common barriers (check all that apply to your relationship):", 'F1', 9)
barriers = ["Unresolved conflict/resentment", "Stress (work, finances, parenting)",
            "Past trauma (individual or relational)", "Trust broken (infidelity, lies)",
            "Different desire levels", "Body image issues",
            "Poor communication", "Lack of time/energy",
            "Emotional walls/avoidance", "Feeling like roommates not partners"]
y = 570
for b in barriers:
    pdf.add_rect(45, y-7, 9, 9)
    pdf.add_text(58, y-5, b, 'F1', 8)
    y -= 14
pdf.add_text(40, y-10, "Our #1 barrier right now:", 'F2', 9)
pdf.add_line(40, y-25, 392, y-25, 0.5, 0.7)
pdf.add_text(40, y-38, "One step we can take to address it:", 'F2', 9)
pdf.add_line(40, y-52, 392, y-52, 0.5, 0.7)
pdf.add_line(40, y-66, 392, y-66, 0.5, 0.7)

# Pages 6-10 - Vulnerability Exercises (5 pages)
vuln_exercises = [
    ("36 QUESTIONS - PART 1", [
        "What would constitute a perfect day for you?",
        "When did you last sing to yourself? To someone else?",
        "If you could change anything about how you were raised, what?",
        "Share something you consider a positive quality of your partner.",
        "What do you value most in a friendship?",
    ]),
    ("36 QUESTIONS - PART 2", [
        "What is your most treasured memory?",
        "What is your most terrible memory?",
        "What roles do love and affection play in your life?",
        "Share an embarrassing moment in your life.",
        "When did you last cry? In front of another person? Alone?",
    ]),
    ("VULNERABILITY PROMPTS", [
        "Something I've been afraid to tell you...",
        "I feel most loved when you...",
        "A fear I have about our relationship...",
        "Something I admire about you that I don't say enough...",
        "The hardest thing about being vulnerable with you...",
    ]),
    ("DEEPER CONNECTION", [
        "How have I hurt you that I haven't fully acknowledged?",
        "What do you need from me that you're not getting?",
        "What dream have you given up that I could support?",
        "When do you feel most alone in our relationship?",
        "What would make you feel completely safe with me?",
    ]),
    ("GRATITUDE & APPRECIATION", [
        "Three things I'm grateful you do that I overlook...",
        "A moment this week when I felt proud of you...",
        "How you've helped me grow as a person...",
        "What I love about our life together...",
        "A quality you have that first attracted me to you...",
    ]),
]
for title, questions in vuln_exercises:
    pdf.new_page()
    pdf.add_centered_text(620, title, 'F2', 12)
    pdf.add_line(40, 610, 392, 610, 1)
    y = 590
    for q in questions:
        pdf.add_text(40, y, q, 'F4', 9)
        y -= 14
        pdf.add_text(40, y, "Partner 1:", 'F2', 8)
        pdf.add_line(85, y-2, 392, y-2, 0.5, 0.7)
        y -= 14
        pdf.add_line(45, y-2, 392, y-2, 0.5, 0.7)
        y -= 16
        pdf.add_text(40, y, "Partner 2:", 'F2', 8)
        pdf.add_line(85, y-2, 392, y-2, 0.5, 0.7)
        y -= 14
        pdf.add_line(45, y-2, 392, y-2, 0.5, 0.7)
        y -= 20

# Page 11 - Non-Sexual Touch
pdf.new_page()
pdf.add_centered_text(620, "NON-SEXUAL TOUCH RECONNECTION", 'F2', 12)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Rebuild physical connection WITHOUT the pressure of sex:", 'F1', 9)
touch_ideas = [
    "Hold hands while watching TV", "6-second kiss goodbye (not a peck!)",
    "20-second hug daily", "Massage each other's hands/feet",
    "Sit close, touching, while talking", "Dance together in the kitchen",
    "Play with each other's hair", "Walk arm in arm",
    "Cuddle for 10 minutes before sleep", "Touch their arm when talking",
]
y = 570
for t in touch_ideas:
    pdf.add_rect(45, y-7, 9, 9)
    pdf.add_text(58, y-5, t, 'F1', 8)
    y -= 14
pdf.add_text(40, y-10, "This week we will try:", 'F2', 9)
y -= 28
for i in range(3):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14

# Pages 12-19 - Weekly Emotional Intimacy Prompts (8 weeks)
for week in range(1, 9):
    pdf.new_page()
    pdf.add_centered_text(620, f"WEEKLY CONNECTION - WEEK {week}", 'F2', 12)
    pdf.add_line(40, 610, 392, 610, 1)
    prompts_weekly = [
        "What was the best part of your week?",
        "What stressed you most this week?",
        "When did you feel most connected to me?",
        "Is there anything you need from me this week?",
        "One thing I appreciate about you this week:",
    ]
    y = 590
    for p in prompts_weekly:
        pdf.add_text(40, y, p, 'F4', 9)
        y -= 14
        pdf.add_text(40, y, "P1:", 'F2', 8)
        pdf.add_line(55, y-2, 392, y-2, 0.5, 0.7)
        y -= 14
        pdf.add_text(40, y, "P2:", 'F2', 8)
        pdf.add_line(55, y-2, 392, y-2, 0.5, 0.7)
        y -= 18
    pdf.add_text(40, y-5, "Date night idea: ___________________________", 'F1', 9)
    pdf.add_text(40, y-20, "Touch goal: ___________________________", 'F1', 9)


# Pages 20-25 - Remaining content
titles_rem = ["CREATING SAFETY FOR VULNERABILITY", "SCHEDULING CONNECTION",
              "LOVE MAPS UPDATE", "REPAIR AFTER DISCONNECTION",
              "OUR INTIMACY GOALS TOGETHER", "OUR LOVE STORY RENEWED"]
for pg, t in enumerate(titles_rem):
    pdf.new_page()
    pdf.add_centered_text(620, t, 'F2', 12)
    pdf.add_line(40, 610, 392, 610, 1)
    if pg == 2:  # Love Maps
        pdf.add_text(40, 590, "How well do you know your partner? (Gottman Love Maps)", 'F4', 9, 0.3)
        questions = ["Partner's biggest current worry:", "Partner's favorite way to relax:",
                     "Partner's best friend right now:", "Partner's current dream/goal:",
                     "Partner's favorite meal:", "What stresses partner most at work:",
                     "Partner's love language:"]
        y = 570
        for q in questions:
            pdf.add_text(40, y, q, 'F1', 9)
            y -= 12
            pdf.add_text(40, y, "My answer:", 'F1', 8)
            pdf.add_line(90, y-2, 392, y-2, 0.5, 0.7)
            y -= 12
            pdf.add_text(40, y, "Correct answer:", 'F1', 8)
            pdf.add_line(105, y-2, 392, y-2, 0.5, 0.7)
            y -= 18
    elif pg == 4:  # Goals
        pdf.add_text(40, 590, "Together, we commit to:", 'F2', 10)
        goals = ["Our emotional intimacy goal:", "Our physical intimacy goal:",
                 "Our communication goal:", "Our weekly ritual:",
                 "Our date night frequency:", "What we'll do when we feel disconnected:"]
        y = 570
        for g in goals:
            pdf.add_text(40, y, g, 'F2', 9)
            y -= 14
            pdf.add_line(45, y, 392, y, 0.5, 0.7)
            y -= 14
            pdf.add_line(45, y, 392, y, 0.5, 0.7)
            y -= 20
        pdf.add_text(40, y-10, "Signed:", 'F2', 9)
        pdf.add_text(40, y-28, "Partner 1: _________________ Date: _______", 'F1', 9)
        pdf.add_text(40, y-44, "Partner 2: _________________ Date: _______", 'F1', 9)
    else:
        y = 585
        for i in range(30):
            pdf.add_line(40, y, 392, y, 0.5, 0.7)
            y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book185_Intimacy_Workbook_Couples.pdf')
print("Book185_Intimacy_Workbook_Couples.pdf created successfully!")
