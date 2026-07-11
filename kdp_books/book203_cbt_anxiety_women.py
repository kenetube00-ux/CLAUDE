"""Book 203: PEACE BEYOND UNDERSTANDING - Scripture-Based CBT Workbook for Christian Women with Anxiety"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.95)
    pdf.add_centered_text(620, "PEACE BEYOND UNDERSTANDING", 'F2', 24)
    pdf.add_centered_text(585, "Scripture-Based CBT Workbook", 'F4', 14, 0.2)
    pdf.add_centered_text(560, "for Christian Women with Anxiety", 'F4', 14, 0.2)
    pdf.add_centered_text(500, "Cognitive Behavioral Therapy + Biblical Truth", 'F1', 11, 0.3)
    pdf.add_centered_text(475, "Thought Records | Exposure Hierarchy | Faith Practices", 'F1', 10, 0.4)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright page
    pdf.new_page()
    pdf.add_text(72, 700, "PEACE BEYOND UNDERSTANDING", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "This workbook is for educational purposes and does not replace", 'F1', 9)
    pdf.add_text(72, 620, "professional mental health treatment. Please seek help if needed.", 'F1', 9)
    pdf.add_text(72, 595, "Crisis: 988 Suicide & Crisis Lifeline", 'F1', 9)
    pdf.add_text(72, 575, "Published by KIDLYTICAL Books", 'F1', 9)

    # What is Anxiety (faith perspective)
    pdf.new_page()
    pdf.add_centered_text(750, "UNDERSTANDING ANXIETY", 'F2', 18)
    pdf.add_centered_text(728, "A Faith Perspective", 'F5', 13)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    content = [
        "Anxiety is your body's natural alarm system - it's not a character flaw.",
        "Even godly people in the Bible experienced anxiety:",
        "  - David: 'When anxiety was great within me' (Psalm 94:19)",
        "  - Jesus: 'His sweat was like drops of blood' (Luke 22:44)",
        "  - Paul: 'I had no rest in my spirit' (2 Corinthians 2:13)",
        "",
        "Anxiety becomes a problem when it:",
        "  - Persists beyond the actual threat",
        "  - Prevents you from daily activities",
        "  - Causes physical symptoms (racing heart, tight chest)",
        "  - Makes you avoid situations God calls you to",
        "",
        "The good news: God offers peace AND practical tools work!",
        "'Be anxious for nothing, but in everything by prayer...' Phil 4:6",
        "",
        "This workbook combines evidence-based CBT with biblical truth."
    ]
    y = 690
    for line in content:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Is anxiety a sin?
    pdf.new_page()
    pdf.add_centered_text(750, "IS ANXIETY A SIN?", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    content2 = [
        "Short answer: NO. Anxiety is not a sin.",
        "",
        "Anxiety is a human experience, not a moral failure.",
        "Jesus himself experienced distress (Mark 14:33-34).",
        "",
        "What the Bible actually says:",
        "- Phil 4:6 is an INVITATION, not a condemnation",
        "- 1 Peter 5:7 says 'cast your cares' - acknowledging we HAVE cares",
        "- Psalm 55:22 says 'cast your burden' - we carry burdens",
        "",
        "Guilt about anxiety makes anxiety worse.",
        "God meets us WITH compassion, not condemnation (Romans 8:1).",
        "",
        "You are not broken. You are human.",
        "Seeking help is wise (Proverbs 12:15).",
        "Therapy + faith can work beautifully together.",
        "",
        "Write below: What guilt have you carried about your anxiety?",
    ]
    y = 710
    for line in content2:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16
    for _ in range(3):
        y -= 5
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 16

    # CBT Triangle with Scripture
    pdf.new_page()
    pdf.add_centered_text(750, "THE CBT TRIANGLE + SCRIPTURE", 'F2', 16)
    pdf.add_centered_text(728, "2 Corinthians 10:5 - Taking every thought captive", 'F5', 11)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    pdf.add_text(72, 690, "CBT teaches that our Thoughts, Feelings, and Behaviors are connected:", 'F1', 10)
    # Triangle visualization
    pdf.add_text(270, 650, "THOUGHTS", 'F2', 11)
    pdf.add_text(270, 635, "(2 Cor 10:5)", 'F3', 8, 0.4)
    pdf.add_line(306, 625, 200, 540, 1, 0.3)
    pdf.add_line(306, 625, 412, 540, 1, 0.3)
    pdf.add_line(200, 540, 412, 540, 1, 0.3)
    pdf.add_text(140, 520, "FEELINGS", 'F2', 11)
    pdf.add_text(140, 505, "(Psalm 42:5)", 'F3', 8, 0.4)
    pdf.add_text(370, 520, "BEHAVIORS", 'F2', 11)
    pdf.add_text(370, 505, "(James 1:22)", 'F3', 8, 0.4)

    pdf.add_text(72, 470, "How it works:", 'F2', 11)
    pdf.add_text(72, 450, "Situation -> Automatic Thought -> Emotion -> Behavior", 'F1', 10)
    pdf.add_text(72, 430, "By changing our THOUGHTS (with truth), feelings and behaviors follow.", 'F1', 10)
    pdf.add_text(72, 400, "My example:", 'F2', 10)
    pdf.add_text(72, 380, "Situation:", 'F1', 9)
    pdf.add_line(140, 378, 540, 378, 0.5, 0.7)
    pdf.add_text(72, 360, "My thought:", 'F1', 9)
    pdf.add_line(145, 358, 540, 358, 0.5, 0.7)
    pdf.add_text(72, 340, "My feeling:", 'F1', 9)
    pdf.add_line(140, 338, 540, 338, 0.5, 0.7)
    pdf.add_text(72, 320, "My behavior:", 'F1', 9)
    pdf.add_line(150, 318, 540, 318, 0.5, 0.7)
    pdf.add_text(72, 295, "Biblical truth:", 'F1', 9)
    pdf.add_line(150, 293, 540, 293, 0.5, 0.7)

    # 5 Thought Record Worksheets
    for tr in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"THOUGHT RECORD #{tr}", 'F2', 16)
        pdf.add_centered_text(730, "Capturing & Challenging Anxious Thoughts", 'F1', 10, 0.4)
        pdf.add_line(72, 720, 540, 720, 1, 0.5)

        fields = [
            ("Situation (What happened?):", 2),
            ("Automatic Thought (What went through my mind?):", 2),
            ("Emotion & Intensity (0-100%):", 1),
            ("Evidence FOR this thought:", 2),
            ("Evidence AGAINST this thought:", 2),
            ("Balanced/Realistic Thought:", 2),
            ("Biblical Truth (What does God say?):", 2),
            ("New Emotion & Intensity (0-100%):", 1),
        ]
        y = 695
        for label, lines in fields:
            pdf.add_text(72, y, label, 'F2', 10)
            y -= 5
            for _ in range(lines):
                y -= 16
                pdf.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 15

    # Cognitive Distortions + Scripture
    pdf.new_page()
    pdf.add_centered_text(750, "COGNITIVE DISTORTIONS & BIBLICAL CORRECTIONS", 'F2', 14)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    distortions = [
        ("All-or-Nothing Thinking", "Romans 3:23 - All fall short; grace covers"),
        ("Catastrophizing", "Matthew 6:34 - Do not worry about tomorrow"),
        ("Mind Reading", "1 Samuel 16:7 - Only God knows the heart"),
        ("Fortune Telling", "James 4:14 - You do not know what tomorrow brings"),
        ("Emotional Reasoning", "Jeremiah 17:9 - The heart is deceitful"),
        ("Should Statements", "Romans 8:1 - No condemnation in Christ"),
        ("Labeling", "2 Cor 5:17 - You are a new creation"),
        ("Magnification", "Psalm 103:12 - He removes our sins far away"),
        ("Personalization", "Romans 8:28 - God works all for good"),
        ("Overgeneralization", "Lam 3:22-23 - His mercies are new every morning"),
    ]
    y = 710
    for dist, scripture in distortions:
        pdf.add_text(72, y, f"- {dist}", 'F2', 10)
        y -= 14
        pdf.add_text(92, y, scripture, 'F4', 9, 0.3)
        y -= 20

    # Behavioral Experiments (3 pages)
    for exp in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(750, f"BEHAVIORAL EXPERIMENT #{exp}", 'F2', 16)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        fields = [
            ("My anxious prediction:", 2),
            ("What I will do (the experiment):", 2),
            ("Prayer before:", 2),
            ("What actually happened:", 3),
            ("What I learned:", 2),
            ("Updated belief (0-100% belief):", 1),
            ("Scripture to remember:", 1),
        ]
        y = 710
        for label, lines in fields:
            pdf.add_text(72, y, label, 'F2', 10)
            y -= 5
            for _ in range(lines):
                y -= 16
                pdf.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 18

    # Exposure Hierarchy
    pdf.new_page()
    pdf.add_centered_text(750, "EXPOSURE HIERARCHY", 'F2', 16)
    pdf.add_centered_text(730, "Facing fears gradually with God's strength", 'F1', 10, 0.4)
    pdf.add_line(72, 720, 540, 720, 1, 0.5)
    pdf.add_text(72, 700, "List your feared situations from least to most scary (0-100):", 'F1', 10)
    y = 675
    for i in range(10):
        pdf.add_text(72, y, f"{(10-i)*10}%", 'F2', 10)
        pdf.add_line(110, y - 2, 540, y - 2, 0.5, 0.7)
        y -= 28

    pdf.add_text(72, y - 10, "Start at the bottom. Each step builds courage. God is with you.", 'F5', 10, 0.3)

    # Breathing as Prayer
    pdf.new_page()
    pdf.add_centered_text(750, "BREATHING AS PRAYER", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    steps = [
        "1. Breathe IN for 4 counts: 'Lord, I receive your peace'",
        "2. HOLD for 4 counts: 'You are here with me'",
        "3. Breathe OUT for 6 counts: 'I release my anxiety to You'",
        "4. Repeat 5-10 times",
        "",
        "Scripture Breathing:",
        "  Inhale: 'The LORD is...' (Psalm 23:1)",
        "  Exhale: '...my shepherd'",
        "  Inhale: 'I shall not...'",
        "  Exhale: '...want'",
        "",
        "Progressive Muscle Relaxation with Psalm 46:",
        "  Tense feet: 'God is our refuge...'",
        "  Release: '...and strength'",
        "  Tense legs: 'A very present help...'",
        "  Release: '...in trouble'",
        "  Continue up through body with the Psalm",
    ]
    y = 710
    for step in steps:
        pdf.add_text(72, y, step, 'F1', 10)
        y -= 18

    # Weekly Mood + Faith Trackers (8 pages)
    for week in range(1, 9):
        pdf.new_page()
        pdf.add_centered_text(750, f"WEEKLY TRACKER - WEEK {week}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # Header
        pdf.add_text(72, 710, "Day", 'F2', 9)
        pdf.add_text(120, 710, "Mood(1-10)", 'F2', 9)
        pdf.add_text(200, 710, "Anxiety(1-10)", 'F2', 9)
        pdf.add_text(300, 710, "Prayer?", 'F2', 9)
        pdf.add_text(370, 710, "Scripture?", 'F2', 9)
        pdf.add_text(450, 710, "Exercise?", 'F2', 9)
        pdf.add_line(72, 703, 540, 703, 0.5, 0.5)
        y = 688
        for day in days:
            pdf.add_text(72, y, day, 'F1', 9)
            pdf.add_line(120, y - 2, 170, y - 2, 0.5, 0.7)
            pdf.add_line(200, y - 2, 265, y - 2, 0.5, 0.7)
            pdf.add_line(300, y - 2, 340, y - 2, 0.5, 0.7)
            pdf.add_line(370, y - 2, 420, y - 2, 0.5, 0.7)
            pdf.add_line(450, y - 2, 500, y - 2, 0.5, 0.7)
            y -= 22

        y -= 15
        pdf.add_text(72, y, "Weekly Reflection:", 'F2', 10)
        y -= 5
        for _ in range(3):
            y -= 16
            pdf.add_line(72, y, 540, y, 0.5, 0.7)

        y -= 20
        pdf.add_text(72, y, "What helped most this week?", 'F2', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

        y -= 25
        pdf.add_text(72, y, "God showed up by:", 'F2', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Relapse Prevention
    pdf.new_page()
    pdf.add_centered_text(750, "RELAPSE PREVENTION + SPIRITUAL DISCIPLINES", 'F2', 14)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "Warning signs my anxiety is returning:", 'F2', 10)
    for i in range(3):
        pdf.add_text(72, 690 - i*20, f"{i+1}.", 'F1', 10)
        pdf.add_line(90, 688 - i*20, 540, 688 - i*20, 0.5, 0.7)

    y = 615
    pdf.add_text(72, y, "My spiritual disciplines that help:", 'F2', 10)
    disciplines = ["Daily prayer time:", "Scripture reading:", "Church community:", "Worship/Music:", "Service to others:"]
    for d in disciplines:
        y -= 20
        pdf.add_text(82, y, d, 'F1', 10)
        pdf.add_line(220, y - 2, 540, y - 2, 0.5, 0.7)

    y -= 30
    pdf.add_text(72, y, "My support team:", 'F2', 10)
    supports = ["Therapist/Counselor:", "Pastor:", "Trusted friend:", "Accountability partner:"]
    for s in supports:
        y -= 20
        pdf.add_text(82, y, s, 'F1', 10)
        pdf.add_line(230, y - 2, 540, y - 2, 0.5, 0.7)

    # For Husbands page
    pdf.new_page()
    pdf.add_centered_text(750, "FOR HUSBANDS: HOW TO SUPPORT HER", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    tips = [
        "1. Listen without trying to fix. Just be present.",
        "2. Don't say 'just pray more' or 'have more faith.'",
        "3. Ask 'How can I help right now?' instead of assuming.",
        "4. Learn her warning signs so you can support early.",
        "5. Encourage her therapy - it's not a lack of faith.",
        "6. Pray WITH her, not AT her.",
        "7. Be patient. Recovery is not linear.",
        "8. Celebrate small victories.",
        "9. Take care of yourself too - you can't pour from empty.",
        "10. Love her like Christ loves the church (Eph 5:25).",
    ]
    y = 710
    for tip in tips:
        pdf.add_text(72, y, tip, 'F1', 11)
        y -= 25

    y -= 10
    pdf.add_text(72, y, "Ephesians 5:25 - Husbands, love your wives as Christ loved the church.", 'F5', 10, 0.3)

    # Fill to 40 pages
    current_pages = len(pdf.pages) + 1
    for extra in range(40 - current_pages):
        pdf.new_page()
        pdf.add_centered_text(750, "JOURNAL & NOTES", 'F2', 14)
        y = 720
        while y > 80:
            pdf.add_line(72, y, 540, y, 0.5, 0.8)
            y -= 22

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book203_CBT_Anxiety_Christian_Women.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
