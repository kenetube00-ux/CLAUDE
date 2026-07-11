"""Book 205: JOY COMES IN THE MORNING - A Scripture-Based CBT Workbook for Depression"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.95)
    pdf.add_centered_text(620, "JOY COMES IN THE MORNING", 'F2', 24)
    pdf.add_centered_text(585, "A Scripture-Based CBT Workbook", 'F4', 14, 0.2)
    pdf.add_centered_text(560, "for Depression", 'F4', 14, 0.2)
    pdf.add_centered_text(510, "Psalm 30:5 - Weeping may stay for the night,", 'F4', 11, 0.3)
    pdf.add_centered_text(492, "but joy comes in the morning.", 'F4', 11, 0.3)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "JOY COMES IN THE MORNING", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "This workbook does not replace professional treatment.", 'F1', 9)
    pdf.add_text(72, 615, "If you are in crisis: 988 Suicide & Crisis Lifeline", 'F2', 9)
    pdf.add_text(72, 590, "Published by KIDLYTICAL Books", 'F1', 9)

    # Understanding Depression
    pdf.new_page()
    pdf.add_centered_text(750, "UNDERSTANDING DEPRESSION", 'F2', 18)
    pdf.add_centered_text(728, "Faith + Science", 'F5', 12)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    content = [
        "Depression is more than sadness. It's a medical condition that affects:",
        "  - Your mood (persistent sadness, emptiness, hopelessness)",
        "  - Your body (fatigue, sleep changes, appetite changes)",
        "  - Your thinking (concentration, decision-making, self-worth)",
        "  - Your spirit (feeling distant from God, loss of meaning)",
        "",
        "Biblical figures who likely experienced depression:",
        "  - Elijah: 'I've had enough, LORD. Take my life.' (1 Kings 19:4)",
        "  - David: 'How long will you forget me?' (Psalm 13:1)",
        "  - Jeremiah: 'Why did I come from the womb?' (Jeremiah 20:18)",
        "  - Jonah: 'It is better for me to die.' (Jonah 4:3)",
        "",
        "God did not condemn them. He MET them where they were.",
        "He sent an angel with food to Elijah (1 Kings 19:5-7).",
        "He invited honest lament from David (the Psalms).",
    ]
    y = 690
    for line in content:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Is Depression a Faith Problem?
    pdf.new_page()
    pdf.add_centered_text(750, "IS DEPRESSION A FAITH PROBLEM?", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_centered_text(710, "NO.", 'F2', 24)
    content2 = [
        "",
        "Depression is not:",
        "  - A sign of weak faith",
        "  - God's punishment",
        "  - Something you can 'pray away' (though prayer helps)",
        "  - Your fault",
        "",
        "Depression IS:",
        "  - A real medical condition (brain chemistry matters)",
        "  - Something faithful people experience",
        "  - Treatable with therapy, medication, and support",
        "  - Something God cares deeply about (Psalm 34:18)",
        "",
        "Getting help is WISE, not weak (Proverbs 12:15).",
        "Taking medication is not lack of faith -",
        "  just as a diabetic takes insulin, you may need support.",
        "",
        "'The LORD is close to the brokenhearted and saves",
        " those who are crushed in spirit.' - Psalm 34:18",
    ]
    y = 690
    for line in content2:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Behavioral Activation
    pdf.new_page()
    pdf.add_centered_text(750, "BEHAVIORAL ACTIVATION WITH SCRIPTURE", 'F2', 15)
    pdf.add_centered_text(728, "Doing brings feeling (not the other way around)", 'F1', 10, 0.4)
    pdf.add_line(72, 718, 540, 718, 1, 0.5)
    content3 = [
        "When depressed, we WAIT to feel better before doing things.",
        "CBT teaches: DO the thing, and feelings often follow.",
        "",
        "James 1:22 - 'Be doers of the word, not hearers only.'",
        "",
        "Small steps count! Rate each activity (0-10) for:",
        "  M = Mastery (sense of accomplishment)",
        "  P = Pleasure (even small enjoyment)",
    ]
    y = 695
    for line in content3:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    y -= 10
    pdf.add_text(72, y, "MY ACTIVATION LIST:", 'F2', 11)
    activities = [
        "Walk outside (even 5 min)", "Text a friend", "Read 1 Psalm",
        "Shower/get dressed", "Listen to worship music", "Cook a simple meal",
        "Call someone", "Attend church", "Journal 3 sentences"
    ]
    y -= 5
    for act in activities:
        y -= 16
        pdf.add_rect(72, y - 8, 8, 8, 0.5, 0.5)
        pdf.add_text(86, y - 6, act, 'F1', 10)

    # Activity Scheduling with God
    pdf.new_page()
    pdf.add_centered_text(750, "ACTIVITY SCHEDULE WITH GOD", 'F2', 15)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 715, "Plan your week. Include spiritual disciplines. Rate M/P after.", 'F1', 10)
    times = ["Morning", "Midday", "Afternoon", "Evening"]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # Header
    y = 690
    pdf.add_text(72, y, "Time", 'F2', 9)
    for i, day in enumerate(days):
        pdf.add_text(130 + i * 60, y, day, 'F2', 9)
    y -= 5
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    for time_slot in times:
        y -= 18
        pdf.add_text(72, y, time_slot, 'F1', 8)
        for i in range(7):
            pdf.add_rect(130 + i * 60, y - 10, 50, 15, 0.3, 0.7)
        y -= 10

    y -= 25
    pdf.add_text(72, y, "Spiritual disciplines to include: Prayer, Scripture, Worship, Fellowship", 'F5', 10, 0.3)

    # Thought Records for Hopelessness (5 pages)
    for tr in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"THOUGHT RECORD: HOPELESSNESS #{tr}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        fields = [
            ("Situation:", 1),
            ("Hopeless thought:", 2),
            ("Evidence this is TRUE:", 2),
            ("Evidence this is NOT completely true:", 2),
            ("What would I tell a friend?:", 2),
            ("What does God say? (Scripture):", 2),
            ("More balanced thought:", 2),
            ("Hopelessness before (0-100): ___  After: ___", 0),
        ]
        y = 710
        for label, lines in fields:
            pdf.add_text(72, y, label, 'F2', 10)
            y -= 5
            for _ in range(lines):
                y -= 16
                pdf.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 15

    # Psalms of Lament
    pdf.new_page()
    pdf.add_centered_text(750, "PSALMS OF LAMENT", 'F2', 18)
    pdf.add_centered_text(728, "It's okay to grieve before God", 'F5', 12)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    content4 = [
        "Over 1/3 of the Psalms are laments - cries of pain to God.",
        "God INVITES our honest grief. He is not threatened by our pain.",
        "",
        "Lament Psalms to read when you're struggling:",
        "  Psalm 13 - How long, O LORD?",
        "  Psalm 22 - My God, why have you forsaken me?",
        "  Psalm 42 - Why so downcast, O my soul?",
        "  Psalm 88 - The darkest Psalm (no resolution - and that's okay)",
        "  Psalm 130 - Out of the depths I cry to you",
        "",
        "Pattern of lament: Cry out -> Trust -> Ask -> Praise",
        "You can start at 'cry out' and stay there. God hears.",
        "",
        "WRITE YOUR OWN LAMENT:",
        "God, I feel...",
    ]
    y = 690
    for line in content4:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16
    for _ in range(5):
        y -= 3
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 14

    # Values Identification
    pdf.new_page()
    pdf.add_centered_text(750, "MY VALUES - WHAT MATTERS TO GOD AND ME", 'F2', 14)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 715, "Depression makes us forget what matters. Let's remember.", 'F1', 10)
    values = [
        "Faith/Spiritual Growth", "Family", "Friendships", "Health",
        "Education/Learning", "Creativity", "Service to Others", "Work/Career",
        "Nature/Outdoors", "Community/Church"
    ]
    y = 690
    for v in values:
        pdf.add_text(72, y, f"- {v}:", 'F2', 10)
        pdf.add_text(240, y, "Importance (1-10): ___", 'F1', 9)
        pdf.add_text(380, y, "Current effort (1-10): ___", 'F1', 9)
        y -= 22

    y -= 15
    pdf.add_text(72, y, "Where is the biggest gap? That's where to start.", 'F5', 10, 0.3)

    # Weekly Mood + Activity + Faith Tracker (8 pages)
    for week in range(1, 9):
        pdf.new_page()
        pdf.add_centered_text(750, f"WEEKLY TRACKER - WEEK {week}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        pdf.add_text(72, 712, "Day", 'F2', 9)
        pdf.add_text(110, 712, "Mood", 'F2', 9)
        pdf.add_text(155, 712, "Activity", 'F2', 9)
        pdf.add_text(270, 712, "M/P", 'F2', 9)
        pdf.add_text(310, 712, "Faith Practice", 'F2', 9)
        pdf.add_text(440, 712, "Sleep", 'F2', 9)
        y = 695
        for day in days:
            pdf.add_text(72, y, day, 'F1', 9)
            pdf.add_line(100, y - 2, 140, y - 2, 0.5, 0.7)
            pdf.add_line(155, y - 2, 260, y - 2, 0.5, 0.7)
            pdf.add_line(270, y - 2, 300, y - 2, 0.5, 0.7)
            pdf.add_line(310, y - 2, 430, y - 2, 0.5, 0.7)
            pdf.add_line(440, y - 2, 500, y - 2, 0.5, 0.7)
            y -= 22
        y -= 10
        pdf.add_text(72, y, "Best moment this week:", 'F2', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 20
        pdf.add_text(72, y, "Something I'm grateful for:", 'F2', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Relapse Warning Signs
    pdf.new_page()
    pdf.add_centered_text(750, "RELAPSE WARNING SIGNS", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "Know your early warning signs so you can act quickly:", 'F1', 11)
    signs = [
        "Withdrawing from people", "Sleeping too much or too little",
        "Skipping meals", "Negative self-talk increasing",
        "Avoiding church/community", "Losing interest in activities",
        "Feeling worthless", "Difficulty concentrating"
    ]
    y = 685
    for s in signs:
        pdf.add_rect(72, y - 8, 8, 8, 0.5, 0.5)
        pdf.add_text(88, y - 6, s, 'F1', 10)
        y -= 20

    y -= 15
    pdf.add_text(72, y, "MY personal warning signs:", 'F2', 10)
    for _ in range(3):
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    y -= 25
    pdf.add_text(72, y, "When I notice these, I will:", 'F2', 10)
    for _ in range(3):
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Building Support Team
    pdf.new_page()
    pdf.add_centered_text(750, "BUILDING MY SUPPORT TEAM", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "You were not meant to do this alone. (Ecclesiastes 4:9-10)", 'F1', 11)
    team = [
        ("Professional (therapist/counselor):", "Name: ___________ Phone: ___________"),
        ("Pastor/Church leader:", "Name: ___________ Phone: ___________"),
        ("Trusted friend:", "Name: ___________ Phone: ___________"),
        ("Family member:", "Name: ___________ Phone: ___________"),
        ("Small group/Bible study:", "Meeting time: ___________"),
        ("Doctor:", "Name: ___________ Phone: ___________"),
    ]
    y = 680
    for role, detail in team:
        pdf.add_text(72, y, role, 'F2', 10)
        y -= 16
        pdf.add_text(92, y, detail, 'F1', 9)
        y -= 25

    # When to Seek Help
    pdf.new_page()
    pdf.add_centered_text(750, "WHEN TO SEEK PROFESSIONAL HELP", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    content5 = [
        "Seek help immediately if you:",
        "  - Have thoughts of hurting yourself",
        "  - Have a plan to end your life",
        "  - Feel hopeless for more than 2 weeks straight",
        "  - Cannot function (work, eat, sleep, care for family)",
        "",
        "CALL 988 if you are in crisis.",
        "",
        "Seek help soon if:",
        "  - Depression lasts more than 2 weeks",
        "  - Your daily life is significantly affected",
        "  - You are self-medicating with alcohol or substances",
        "  - Prayer and community are not enough",
        "",
        "Remember: Seeking help is STRENGTH, not weakness.",
        "Jesus said the sick need a doctor (Mark 2:17).",
        "God uses therapists, doctors, and community to heal.",
    ]
    y = 710
    for line in content5:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book205_CBT_Depression_Christian.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
