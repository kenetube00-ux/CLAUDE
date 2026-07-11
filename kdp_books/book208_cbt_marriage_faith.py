"""Book 208: LOVE THAT LASTS - A Scripture-Based Communication Workbook for Christian Couples"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.95)
    pdf.add_centered_text(620, "LOVE THAT LASTS", 'F2', 28)
    pdf.add_centered_text(580, "A Scripture-Based Communication Workbook", 'F4', 14, 0.2)
    pdf.add_centered_text(558, "for Christian Couples", 'F4', 14, 0.2)
    pdf.add_centered_text(510, "Better communication = Stronger marriage", 'F1', 11, 0.3)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "LOVE THAT LASTS", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "This workbook is for educational purposes.", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)

    # God's Design
    pdf.new_page()
    pdf.add_centered_text(750, "GOD'S DESIGN FOR MARRIAGE COMMUNICATION", 'F2', 14)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    content = [
        "God created marriage for companionship (Genesis 2:18).",
        "Communication is the lifeblood of this companionship.",
        "",
        "Key principles from Scripture:",
        "  - Be quick to listen (James 1:19)",
        "  - Speak truth in love (Ephesians 4:15)",
        "  - Build each other up (1 Thessalonians 5:11)",
        "  - Be kind and tenderhearted (Ephesians 4:32)",
        "  - Do not let the sun go down on anger (Ephesians 4:26)",
        "",
        "God's goal is not conflict-free marriage -",
        "it's a marriage where conflict leads to growth.",
        "",
        "This workbook will help you:",
        "  1. Understand each other's communication style",
        "  2. Learn to listen with love",
        "  3. Express needs without attacking",
        "  4. Resolve conflict the biblical way",
        "  5. Build a lasting communication covenant",
    ]
    y = 710
    for line in content:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Communication Styles Assessment (both partners)
    for partner in ["PARTNER 1", "PARTNER 2"]:
        pdf.new_page()
        pdf.add_centered_text(750, f"COMMUNICATION STYLE - {partner}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        pdf.add_text(72, 715, "Rate yourself 1-5 (1=never, 5=always):", 'F1', 10)
        questions = [
            "I express my feelings openly",
            "I listen without interrupting",
            "I raise my voice when frustrated",
            "I shut down during conflict (withdraw)",
            "I bring up past issues in arguments",
            "I apologize when I'm wrong",
            "I ask clarifying questions",
            "I assume I know what my partner thinks",
            "I express appreciation daily",
            "I pray with/for my spouse regularly",
        ]
        y = 690
        for q in questions:
            pdf.add_text(72, y, q, 'F1', 10)
            pdf.add_text(450, y, "1  2  3  4  5", 'F3', 9)
            y -= 20

        y -= 10
        pdf.add_text(72, y, "My communication strength:", 'F2', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 20
        pdf.add_text(72, y, "Area I most need to grow:", 'F2', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Active Listening as Love
    pdf.new_page()
    pdf.add_centered_text(750, "ACTIVE LISTENING AS LOVE", 'F2', 16)
    pdf.add_centered_text(728, "James 1:19 - Be quick to listen", 'F5', 11)
    pdf.add_line(72, 718, 540, 718, 1, 0.5)
    content2 = [
        "ACTIVE LISTENING means:",
        "  - Put down your phone",
        "  - Make eye contact",
        "  - Don't formulate your response while they talk",
        "  - Reflect back: 'What I hear you saying is...'",
        "  - Ask: 'Did I understand that correctly?'",
        "  - Validate: 'That makes sense that you'd feel that way'",
        "",
        "LISTENING KILLERS:",
        "  - Defending yourself before they finish",
        "  - Minimizing: 'It's not that bad'",
        "  - Problem-solving before they ask for solutions",
        "  - Bringing up your own issue in response",
        "",
        "Practice: Take turns sharing for 3 minutes each.",
        "The listener can ONLY reflect back. No responding.",
    ]
    y = 695
    for line in content2:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    # I-Statement Practice (5 pages)
    for page in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"I-STATEMENT PRACTICE #{page}", 'F2', 14)
        pdf.add_centered_text(730, "Ephesians 4:15 - Speaking truth in love", 'F5', 10)
        pdf.add_line(72, 718, 540, 718, 1, 0.5)
        pdf.add_text(72, 698, "Formula: 'When [situation], I feel [emotion] because [reason].", 'F3', 9)
        pdf.add_text(72, 682, "I need [request].'", 'F3', 9)

        for i in range(3):
            y_base = 650 - i * 170
            pdf.add_text(72, y_base, f"Situation {i+1}:", 'F2', 10)
            fields = [
                "When (what happened):",
                "I feel (emotion):",
                "Because (why it matters):",
                "I need (specific request):",
            ]
            y = y_base - 18
            for f in fields:
                pdf.add_text(82, y, f, 'F1', 9)
                pdf.add_line(230, y - 2, 540, y - 2, 0.5, 0.7)
                y -= 18

    # Cognitive Distortions in Marriage
    pdf.new_page()
    pdf.add_centered_text(750, "THINKING TRAPS IN MARRIAGE", 'F2', 15)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    distortions = [
        ("Mind Reading", "'She's angry because she hates me'", "Ask, don't assume! (Proverbs 18:13)"),
        ("Catastrophizing", "'One fight means our marriage is over'", "One conflict is not the end (Love bears all - 1 Cor 13:7)"),
        ("All-or-Nothing", "'He NEVER helps' / 'She ALWAYS nags'", "Avoid always/never. Be specific. (Eph 4:25)"),
        ("Scorekeeper", "'I did X so she should do Y'", "Love doesn't keep score (1 Cor 13:5)"),
        ("Negative Filter", "Only seeing what's wrong", "Think on what is good (Phil 4:8)"),
    ]
    y = 710
    for trap, example, correction in distortions:
        pdf.add_text(72, y, f"{trap}:", 'F2', 10)
        y -= 14
        pdf.add_text(92, y, f"Example: {example}", 'F3', 9, 0.3)
        y -= 14
        pdf.add_text(92, y, f"Correction: {correction}", 'F4', 9)
        y -= 22

    # Conflict De-Escalation
    pdf.new_page()
    pdf.add_centered_text(750, "CONFLICT DE-ESCALATION WITH PRAYER PAUSE", 'F2', 14)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    steps = [
        "1. RECOGNIZE: 'We're escalating' (watch for raised voices, blame)",
        "2. PAUSE: 'I need 20 minutes. I love you and I'll come back.'",
        "3. PRAY: Separately. 'God, help me see their heart, not just words.'",
        "4. SELF-SOOTHE: Breathe, walk, journal. Don't rehearse arguments.",
        "5. RETURN: Come back calmer. Start with 'I love you.'",
        "6. REPAIR: 'I'm sorry for my part. Can we try again?'",
        "",
        "RULES OF ENGAGEMENT (agree on these together):",
        "  - No name-calling",
        "  - No bringing up the past",
        "  - No 'always' or 'never'",
        "  - Either can call a timeout (not avoidance!)",
        "  - Pray before resuming",
        "  - Touch if possible (hold hands during hard talks)",
    ]
    y = 710
    for step in steps:
        pdf.add_text(72, y, step, 'F1', 10)
        y -= 17

    # Repair Attempts
    pdf.new_page()
    pdf.add_centered_text(750, "REPAIR ATTEMPTS", 'F2', 16)
    pdf.add_centered_text(728, "Matthew 5:23-24 - Seek reconciliation", 'F5', 10)
    pdf.add_line(72, 718, 540, 718, 1, 0.5)
    pdf.add_text(72, 698, "Repair attempts are bids to de-escalate. They work!", 'F1', 10)
    repairs = [
        "'I'm sorry. That came out wrong.'",
        "'Can we start over?'",
        "'You're right about that part.'",
        "'I love you even when we disagree.'",
        "'Let me try to say that better.'",
        "'I can see this from your side.'",
        "'We're on the same team.'",
        "'Can I have a do-over?'",
        "'I hear you. I'm listening.'",
        "'Let's pray about this together.'",
    ]
    y = 675
    for r in repairs:
        pdf.add_text(82, y, r, 'F4', 10)
        y -= 18

    y -= 10
    pdf.add_text(72, y, "Our favorite repair phrases:", 'F2', 10)
    for _ in range(3):
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Weekly Couples Check-In (5 pages)
    for week in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"WEEKLY COUPLES CHECK-IN - WEEK {week}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        sections = [
            ("ROSES (What went well this week?):", 3),
            ("THORNS (What was hard?):", 3),
            ("PRAYERS (What do we need God's help with?):", 3),
            ("APPRECIATION (Something I love about you):", 2),
            ("NEXT WEEK (What can we do better?):", 2),
        ]
        y = 710
        for label, lines in sections:
            pdf.add_text(72, y, label, 'F2', 10)
            for _ in range(lines):
                y -= 16
                pdf.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 20

    # Date Night Questions
    pdf.new_page()
    pdf.add_centered_text(750, "DATE NIGHT CONVERSATION STARTERS", 'F2', 14)
    pdf.add_centered_text(730, "20 Faith-Based Questions", 'F1', 10, 0.4)
    pdf.add_line(72, 720, 540, 720, 1, 0.5)
    questions_list = [
        "1. What's one way God has grown us as a couple?",
        "2. What's your favorite memory of us this year?",
        "3. How can I pray for you this week?",
        "4. What dream do you have that we haven't talked about?",
        "5. What's something I do that makes you feel loved?",
        "6. If we could serve together somewhere, where would it be?",
        "7. What does your ideal Saturday look like?",
        "8. What Bible verse describes our marriage right now?",
        "9. What are you most grateful for about our family?",
        "10. What's one thing you'd like us to do more of?",
        "11. How do you feel closest to God?",
        "12. What's a goal you want us to work toward?",
        "13. When do you feel most loved by me?",
        "14. What's something new you'd like to try together?",
        "15. What legacy do we want to leave our family?",
        "16. What's your love language this season?",
        "17. How can I support your calling/gifts?",
        "18. What's one thing I could improve as a spouse?",
        "19. What couple do you admire and why?",
        "20. Let's pray together right now about _______.",
    ]
    y = 697
    for q in questions_list:
        pdf.add_text(72, y, q, 'F1', 9)
        y -= 16

    # Communication Covenant
    pdf.new_page()
    pdf.add_centered_text(750, "OUR COMMUNICATION COVENANT", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "We, the undersigned, commit before God to:", 'F1', 11)
    commitments = [
        "Listen with our full attention",
        "Speak truth in love, not anger",
        "Never use words as weapons",
        "Seek to understand before being understood",
        "Pray together when conflict arises",
        "Forgive as Christ forgave us",
        "Assume the best about each other's motives",
        "Never threaten divorce in an argument",
        "Build each other up, not tear down",
        "Keep growing in communication together",
    ]
    y = 685
    for c in commitments:
        pdf.add_rect(72, y - 8, 8, 8, 0.5, 0.5)
        pdf.add_text(88, y - 6, c, 'F1', 10)
        y -= 20

    y -= 20
    pdf.add_text(72, y, "Partner 1: ________________________  Date: ________", 'F1', 10)
    y -= 25
    pdf.add_text(72, y, "Partner 2: ________________________  Date: ________", 'F1', 10)
    y -= 30
    pdf.add_text(72, y, "'Above all, love each other deeply.' - 1 Peter 4:8", 'F5', 11, 0.3)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book208_CBT_Marriage_Christian.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
