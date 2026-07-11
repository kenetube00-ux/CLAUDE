"""Book 206: SLOW TO ANGER - A Scripture-Based Workbook for Managing Anger God's Way"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.95)
    pdf.add_centered_text(620, "SLOW TO ANGER", 'F2', 28)
    pdf.add_centered_text(580, "A Scripture-Based Workbook for", 'F4', 14, 0.2)
    pdf.add_centered_text(558, "Managing Anger God's Way", 'F4', 14, 0.2)
    pdf.add_centered_text(510, "James 1:19 - Be quick to listen, slow to speak, slow to anger", 'F4', 11, 0.3)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "SLOW TO ANGER", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "This workbook is educational and does not replace counseling.", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)

    # What the Bible says about anger
    pdf.new_page()
    pdf.add_centered_text(750, "WHAT THE BIBLE SAYS ABOUT ANGER", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    content = [
        "Anger itself is NOT always sin. Even God gets angry (at injustice).",
        "",
        "RIGHTEOUS ANGER (acceptable):",
        "  - Jesus overturning tables (John 2:15) - anger at exploitation",
        "  - God's anger at oppression (Exodus 3:7-9)",
        "  - Anger at injustice, abuse, evil",
        "",
        "SINFUL ANGER (what we need to manage):",
        "  - Anger that leads to harm (Cain - Genesis 4:5-8)",
        "  - Anger held too long (Ephesians 4:26 - don't let sun go down)",
        "  - Anger that destroys relationships",
        "  - Anger rooted in pride, selfishness, or control",
        "",
        "KEY SCRIPTURES:",
        "  James 1:19-20 - Be slow to anger; human anger does not produce",
        "     the righteousness that God desires.",
        "  Proverbs 15:1 - A gentle answer turns away wrath.",
        "  Ephesians 4:26 - Be angry and do not sin.",
    ]
    y = 710
    for line in content:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    # James 1:19-20 Deep Dive
    pdf.new_page()
    pdf.add_centered_text(750, "JAMES 1:19-20 DEEP DIVE", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "'My dear brothers and sisters, take note of this:", 'F4', 11)
    pdf.add_text(72, 692, " Everyone should be quick to listen, slow to speak", 'F4', 11)
    pdf.add_text(72, 674, " and slow to become angry, because human anger does not", 'F4', 11)
    pdf.add_text(72, 656, " produce the righteousness that God desires.'", 'F4', 11)

    y = 625
    parts = [
        ("QUICK TO LISTEN", "Before reacting, truly hear the other person.", "Am I listening to understand or to respond?"),
        ("SLOW TO SPEAK", "Pause before words leave your mouth.", "What am I about to say? Is it helpful or hurtful?"),
        ("SLOW TO ANGER", "Create space between trigger and response.", "Can I wait 10 seconds before reacting?"),
    ]
    for title, explain, question in parts:
        pdf.add_text(72, y, title, 'F2', 12)
        y -= 16
        pdf.add_text(92, y, explain, 'F1', 10)
        y -= 16
        pdf.add_text(92, y, question, 'F3', 9, 0.4)
        y -= 16
        pdf.add_line(92, y, 540, y, 0.5, 0.7)
        y -= 25

    # Anger Triggers
    pdf.new_page()
    pdf.add_centered_text(750, "MY ANGER TRIGGERS", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "Identify what sets you off. Check all that apply:", 'F1', 11)
    triggers = [
        "Being disrespected", "Feeling controlled", "Injustice/unfairness",
        "Being interrupted", "Feeling ignored", "Traffic/delays",
        "Messy house", "Money stress", "Being lied to",
        "Feeling overwhelmed", "Parenting challenges", "Work pressure"
    ]
    y = 685
    for t in triggers:
        pdf.add_rect(72, y - 8, 8, 8, 0.5, 0.5)
        pdf.add_text(88, y - 6, t, 'F1', 10)
        y -= 20

    y -= 15
    pdf.add_text(72, y, "My TOP 3 triggers:", 'F2', 10)
    for i in range(3):
        y -= 18
        pdf.add_text(72, y, f"{i+1}.", 'F1', 10)
        pdf.add_line(90, y - 2, 540, y - 2, 0.5, 0.7)

    # Physical Warning Signs
    pdf.new_page()
    pdf.add_centered_text(750, "MY BODY'S WARNING SIGNS", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "Anger shows up in your body before your words. Notice:", 'F1', 11)
    signs = [
        "Jaw clenching", "Fists tightening", "Heart racing",
        "Face getting hot", "Chest tightening", "Rapid breathing",
        "Muscle tension (shoulders/neck)", "Stomach churning",
    ]
    y = 685
    for s in signs:
        pdf.add_rect(72, y - 8, 8, 8, 0.5, 0.5)
        pdf.add_text(88, y - 6, s, 'F1', 10)
        y -= 20

    y -= 15
    pdf.add_text(72, y, "When I notice these signs, I can:", 'F2', 10)
    y -= 18
    pdf.add_text(82, y, "1. STOP - Don't react yet", 'F1', 10)
    y -= 16
    pdf.add_text(82, y, "2. BREATHE - 4 deep breaths", 'F1', 10)
    y -= 16
    pdf.add_text(82, y, "3. PRAY - 'Lord, help me respond not react'", 'F1', 10)
    y -= 16
    pdf.add_text(82, y, "4. CHOOSE - What does love look like here?", 'F1', 10)

    # The Anger Cycle
    pdf.new_page()
    pdf.add_centered_text(750, "THE ANGER CYCLE", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "Trigger -> Thought -> Feeling -> Response", 'F2', 11)
    pdf.add_text(72, 685, "Example:", 'F2', 10)
    pdf.add_text(92, 665, "Trigger: Spouse criticizes my cooking", 'F1', 10)
    pdf.add_text(92, 648, "Thought: 'Nothing I do is ever good enough!'", 'F1', 10)
    pdf.add_text(92, 631, "Feeling: Anger (8/10), hurt (7/10)", 'F1', 10)
    pdf.add_text(92, 614, "Response: Yell back, slam door", 'F1', 10)

    pdf.add_text(72, 585, "MY ANGER CYCLE:", 'F2', 11)
    fields = ["Trigger:", "Thought:", "Feeling:", "Response:", "Better response with God's help:"]
    y = 565
    for f in fields:
        pdf.add_text(72, y, f, 'F1', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 20

    # Cognitive Restructuring with Proverbs (6 pages)
    proverbs_lessons = [
        ("Proverbs 15:1", "A gentle answer turns away wrath, but a harsh word stirs up anger.",
         "When I want to respond harshly, I can choose gentle words instead."),
        ("Proverbs 14:29", "Whoever is slow to anger has great understanding.",
         "Pausing before reacting shows wisdom, not weakness."),
        ("Proverbs 19:11", "Good sense makes one slow to anger, and it is his glory to overlook an offense.",
         "Not every offense deserves a response. I can choose to let go."),
        ("Proverbs 29:11", "A fool gives full vent to his spirit, but a wise man quietly holds it back.",
         "Controlling my anger is strength, not suppression."),
        ("Proverbs 16:32", "Whoever is slow to anger is better than the mighty.",
         "Self-control is more powerful than physical strength."),
        ("Proverbs 22:24-25", "Make no friendship with a man given to anger.",
         "My anger affects others. I choose to be safe for people I love."),
    ]
    for ref, verse, application in proverbs_lessons:
        pdf.new_page()
        pdf.add_centered_text(750, f"RESTRUCTURING WITH {ref.upper()}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        pdf.add_text(72, 710, f'"{verse}"', 'F4', 11)
        pdf.add_text(72, 680, "Application:", 'F2', 10)
        pdf.add_text(82, 662, application, 'F1', 10)

        pdf.add_text(72, 630, "WORKSHEET:", 'F2', 11)
        fields = [
            ("Angry thought I had recently:", 2),
            ("What Proverbs says about this:", 2),
            ("A wiser response would be:", 2),
            ("How I felt after choosing wisdom:", 2),
        ]
        y = 610
        for label, lines in fields:
            pdf.add_text(72, y, label, 'F1', 10)
            for _ in range(lines):
                y -= 16
                pdf.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 20

    # Communication Scripts (Eph 4:15)
    pdf.new_page()
    pdf.add_centered_text(750, "SPEAKING TRUTH IN LOVE", 'F2', 16)
    pdf.add_centered_text(728, "Ephesians 4:15", 'F5', 11)
    pdf.add_line(72, 718, 540, 718, 1, 0.5)
    pdf.add_text(72, 695, "Instead of attacking, try this formula:", 'F2', 11)
    pdf.add_text(72, 670, "'When [situation], I feel [emotion] because [reason].", 'F3', 10)
    pdf.add_text(72, 652, " I need [request]. Can we work on this together?'", 'F3', 10)

    pdf.add_text(72, 620, "Example:", 'F2', 10)
    pdf.add_text(82, 600, "Instead of: 'You NEVER help around the house!'", 'F1', 10)
    pdf.add_text(82, 580, "Try: 'When dishes pile up, I feel overwhelmed because", 'F1', 10)
    pdf.add_text(82, 562, "I need support. Can we divide chores together?'", 'F1', 10)

    pdf.add_text(72, 530, "MY PRACTICE:", 'F2', 11)
    for i in range(3):
        y = 510 - i * 80
        pdf.add_text(72, y, f"Situation {i+1}:", 'F1', 9)
        pdf.add_text(72, y - 16, "My old response:", 'F1', 9)
        pdf.add_line(170, y - 18, 540, y - 18, 0.5, 0.7)
        pdf.add_text(72, y - 32, "My new response:", 'F1', 9)
        pdf.add_line(170, y - 34, 540, y - 34, 0.5, 0.7)
        pdf.add_line(170, y - 50, 540, y - 50, 0.5, 0.7)

    # Conflict Resolution - Matthew 18
    pdf.new_page()
    pdf.add_centered_text(750, "CONFLICT RESOLUTION - THE MATTHEW 18 MODEL", 'F2', 14)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    steps = [
        ("Step 1: Go Directly (v.15)", "Talk to the person privately first. Not to others."),
        ("Step 2: Bring a Witness (v.16)", "If unresolved, bring a trusted mediator."),
        ("Step 3: Involve Leadership (v.17)", "If still unresolved, seek pastoral counsel."),
        ("Step 4: Set Boundaries", "Protect yourself while pursuing reconciliation."),
    ]
    y = 710
    for title, desc in steps:
        pdf.add_text(72, y, title, 'F2', 11)
        y -= 16
        pdf.add_text(92, y, desc, 'F1', 10)
        y -= 25

    # Forgiveness
    pdf.new_page()
    pdf.add_centered_text(750, "FORGIVENESS", 'F2', 18)
    pdf.add_centered_text(728, "Not condoning, but releasing", 'F5', 12)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    content2 = [
        "Forgiveness IS:",
        "  - Releasing the debt someone owes you",
        "  - Choosing not to seek revenge",
        "  - Trusting God with justice",
        "  - Freedom for YOUR heart",
        "",
        "Forgiveness is NOT:",
        "  - Saying what happened was okay",
        "  - Trusting the person again immediately",
        "  - Forgetting (you may always remember)",
        "  - Staying in an abusive situation",
        "",
        "Colossians 3:13 - Forgive as the Lord forgave you.",
        "",
        "Who do I need to forgive?",
    ]
    y = 690
    for line in content2:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16
    for _ in range(3):
        y -= 5
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 14

    # Weekly Anger + Prayer Log (5 pages)
    for week in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"ANGER + PRAYER LOG - WEEK {week}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        pdf.add_text(72, 712, "Day", 'F2', 9)
        pdf.add_text(110, 712, "Anger(1-10)", 'F2', 9)
        pdf.add_text(195, 712, "Trigger", 'F2', 9)
        pdf.add_text(340, 712, "Response", 'F2', 9)
        pdf.add_text(470, 712, "Prayer?", 'F2', 9)
        y = 695
        for day in days:
            pdf.add_text(72, y, day, 'F1', 9)
            pdf.add_line(110, y - 2, 180, y - 2, 0.5, 0.7)
            pdf.add_line(195, y - 2, 330, y - 2, 0.5, 0.7)
            pdf.add_line(340, y - 2, 460, y - 2, 0.5, 0.7)
            pdf.add_line(470, y - 2, 540, y - 2, 0.5, 0.7)
            y -= 22
        y -= 10
        pdf.add_text(72, y, "Progress I noticed:", 'F2', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Accountability Partner Agreement
    pdf.new_page()
    pdf.add_centered_text(750, "ACCOUNTABILITY PARTNER AGREEMENT", 'F2', 15)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    content3 = [
        "I, _________________________, commit to:",
        "",
        "1. Being honest about my anger struggles",
        "2. Meeting regularly with my partner for check-ins",
        "3. Calling my partner BEFORE I react in anger",
        "4. Being open to feedback without defensiveness",
        "5. Praying for my partner as they pray for me",
        "",
        "My accountability partner: _______________________",
        "We will meet: (day/time) _______________________",
        "Our check-in questions:",
        "  - Did you lose your temper this week?",
        "  - What triggered you?",
        "  - How did you respond?",
        "  - What would you do differently?",
        "  - How can I pray for you?",
        "",
        "Signed: ________________  Date: ________________",
    ]
    y = 710
    for line in content3:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 18

    # My Commitment
    pdf.new_page()
    pdf.add_centered_text(750, "MY COMMITMENT TO CHANGE", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "With God's help and the power of the Holy Spirit, I commit to:", 'F1', 11)
    y = 685
    commitments = [
        "Being slow to anger (James 1:19)",
        "Using gentle words (Proverbs 15:1)",
        "Forgiving others as God forgave me (Colossians 3:13)",
        "Not going to bed angry (Ephesians 4:26)",
        "Seeking help when I need it (Proverbs 12:15)",
    ]
    for c in commitments:
        pdf.add_rect(72, y - 8, 8, 8, 0.5, 0.5)
        pdf.add_text(88, y - 6, c, 'F1', 10)
        y -= 22

    y -= 20
    pdf.add_text(72, y, "Signed: ________________________", 'F1', 11)
    y -= 25
    pdf.add_text(72, y, "Date: ________________________", 'F1', 11)
    y -= 35
    pdf.add_text(72, y, "'He who is slow to anger is better than the mighty.' - Proverbs 16:32", 'F5', 11, 0.3)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book206_CBT_Anger_Christian.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
