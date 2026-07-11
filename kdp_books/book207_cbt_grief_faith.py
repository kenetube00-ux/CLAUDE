"""Book 207: BLESSED ARE THOSE WHO MOURN - A Scripture-Integrated Grief Workbook"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.94)
    pdf.add_centered_text(490, "BLESSED ARE THOSE", 'F2', 20)
    pdf.add_centered_text(465, "WHO MOURN", 'F2', 20)
    pdf.add_centered_text(430, "A Scripture-Integrated Grief Workbook", 'F4', 12, 0.2)
    pdf.add_centered_text(390, "Matthew 5:4 - For they will be comforted.", 'F4', 10, 0.3)
    pdf.add_centered_text(160, f"By {author}", 'F2', 12, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(40, 580, "BLESSED ARE THOSE WHO MOURN", 'F2', 11)
    pdf.add_text(40, 560, f"By {author}", 'F1', 10)
    pdf.add_text(40, 535, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(40, 515, "If in crisis: 988 Suicide & Crisis Lifeline", 'F2', 9)
    pdf.add_text(40, 490, "Published by KIDLYTICAL Books", 'F1', 9)

    # Understanding Grief
    pdf.new_page()
    pdf.add_centered_text(600, "UNDERSTANDING GRIEF", 'F2', 16)
    pdf.add_line(40, 588, 392, 588, 1, 0.5)
    content = [
        "Grief is love with nowhere to go.",
        "",
        "The 5 stages (not linear - you may go back and forth):",
        "  1. Denial - This can't be real",
        "  2. Anger - Why did this happen?",
        "  3. Bargaining - What if I had...",
        "  4. Depression - The weight of loss",
        "  5. Acceptance - Learning to live with loss",
        "",
        "Biblical model of grief:",
        "  - Lament (cry out to God honestly)",
        "  - Remember (hold onto memories)",
        "  - Hope (trust in God's promises)",
        "  - Comfort others (2 Corinthians 1:3-4)",
        "",
        "There is no timeline for grief. Give yourself grace.",
    ]
    y = 565
    for line in content:
        pdf.add_text(40, y, line, 'F1', 9)
        y -= 14

    # It's Okay to Grieve
    pdf.new_page()
    pdf.add_centered_text(600, "IT'S OKAY TO GRIEVE", 'F2', 16)
    pdf.add_centered_text(580, "Jesus Wept - John 11:35", 'F5', 12)
    pdf.add_line(40, 568, 392, 568, 1, 0.5)
    content2 = [
        "Jesus stood at the tomb of his friend Lazarus and WEPT.",
        "He knew He was about to raise Lazarus from the dead.",
        "He wept anyway. Grief is not a lack of faith.",
        "",
        "You have permission to:",
        "  - Cry as long as you need",
        "  - Feel angry (even at God - He can handle it)",
        "  - Not be okay for a while",
        "  - Miss them every single day",
        "  - Say 'I'm not fine' when people ask",
        "",
        "You do NOT have to:",
        "  - 'Be strong' for everyone else",
        "  - 'Get over it' on anyone's timeline",
        "  - Pretend faith makes grief disappear",
        "  - Feel guilty for moments of joy",
    ]
    y = 548
    for line in content2:
        pdf.add_text(40, y, line, 'F1', 9)
        y -= 14

    # Complicated Grief Assessment
    pdf.new_page()
    pdf.add_centered_text(600, "COMPLICATED GRIEF - DO I NEED EXTRA HELP?", 'F2', 13)
    pdf.add_line(40, 588, 392, 588, 1, 0.5)
    pdf.add_text(40, 570, "Check if you experience these for more than 6 months:", 'F1', 9)
    checks = [
        "Intense longing that doesn't lessen at all",
        "Inability to accept the death",
        "Feeling life has no purpose without them",
        "Difficulty trusting others since the loss",
        "Feeling numb or detached from life",
        "Bitterness or anger about the death",
        "Avoiding reminders of the person",
        "Wishing you had died instead",
    ]
    y = 548
    for c in checks:
        pdf.add_rect(40, y - 7, 7, 7, 0.5, 0.5)
        pdf.add_text(54, y - 5, c, 'F1', 9)
        y -= 18

    y -= 15
    pdf.add_text(40, y, "If 4+ checked: Please seek grief counseling.", 'F2', 9)
    pdf.add_text(40, y - 14, "This is not weakness - it's wisdom.", 'F1', 9)

    # Continuing Bonds
    pdf.new_page()
    pdf.add_centered_text(600, "CONTINUING BONDS", 'F2', 16)
    pdf.add_centered_text(580, "Not 'moving on' but 'moving forward'", 'F5', 10)
    pdf.add_line(40, 570, 392, 570, 1, 0.5)
    content3 = [
        "You don't have to 'let go' of your loved one.",
        "Your relationship continues - it just changes form.",
        "",
        "Ways to maintain connection:",
        "  - Talk to them (it's not crazy!)",
        "  - Keep traditions that honor them",
        "  - Share stories with others",
        "  - Write them letters",
        "  - Do something they would have loved",
        "",
        "My favorite memory of them:",
    ]
    y = 550
    for line in content3:
        pdf.add_text(40, y, line, 'F1', 9)
        y -= 14
    for _ in range(3):
        y -= 5
        pdf.add_line(40, y, 392, y, 0.5, 0.7)
        y -= 12

    # Cognitive Processing
    pdf.new_page()
    pdf.add_centered_text(600, "STUCK POINTS + SCRIPTURE", 'F2', 14)
    pdf.add_line(40, 588, 392, 588, 1, 0.5)
    stuck_points = [
        ("'God took them to punish me'", "Romans 8:1 - No condemnation in Christ"),
        ("'I should have done more'", "Psalm 139:16 - All days are written in His book"),
        ("'I'll never be happy again'", "Psalm 30:5 - Joy comes in the morning"),
        ("'God doesn't care'", "Psalm 34:18 - The LORD is near to the brokenhearted"),
    ]
    y = 565
    for stuck, truth in stuck_points:
        pdf.add_text(40, y, f"Stuck point: {stuck}", 'F2', 9)
        y -= 14
        pdf.add_text(50, y, f"Truth: {truth}", 'F4', 9)
        y -= 20

    y -= 10
    pdf.add_text(40, y, "MY stuck point:", 'F2', 9)
    y -= 14
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 16
    pdf.add_text(40, y, "Scripture that speaks to this:", 'F2', 9)
    y -= 14
    pdf.add_line(40, y, 392, y, 0.5, 0.7)

    # Meaning-Making
    pdf.new_page()
    pdf.add_centered_text(600, "MEANING-MAKING THROUGH FAITH", 'F2', 14)
    pdf.add_line(40, 588, 392, 588, 1, 0.5)
    content4 = [
        "Meaning-making doesn't mean the loss 'makes sense.'",
        "It means finding purpose even in the pain.",
        "",
        "Questions to explore:",
        "  - How has this loss changed me?",
        "  - What have I learned about what matters?",
        "  - How can my pain help others? (2 Cor 1:3-4)",
        "  - What would my loved one want for me?",
        "  - Where have I seen God in this darkness?",
    ]
    y = 565
    for line in content4:
        pdf.add_text(40, y, line, 'F1', 9)
        y -= 14
    y -= 10
    pdf.add_text(40, y, "My reflections:", 'F2', 9)
    for _ in range(5):
        y -= 14
        pdf.add_line(40, y, 392, y, 0.5, 0.7)

    # Holiday/Anniversary Coping
    pdf.new_page()
    pdf.add_centered_text(600, "HOLIDAY & ANNIVERSARY COPING PLAN", 'F2', 13)
    pdf.add_line(40, 588, 392, 588, 1, 0.5)
    pdf.add_text(40, 568, "Holidays and anniversaries can be especially hard.", 'F1', 9)
    pdf.add_text(40, 550, "Plan ahead so you're not caught off guard:", 'F1', 9)
    fields = [
        "Difficult dates: _______________",
        "What I'll do to honor them: _______________",
        "Who will be with me: _______________",
        "My permission to leave if overwhelmed: YES",
        "Scripture to hold onto: _______________",
        "A new tradition that honors them: _______________",
    ]
    y = 525
    for f in fields:
        pdf.add_text(40, y, f, 'F1', 9)
        y -= 22

    y -= 10
    pdf.add_text(40, y, "'He will wipe every tear from their eyes.' - Rev 21:4", 'F5', 9, 0.3)

    # 30 Daily Grief Journal Pages
    for day in range(1, 31):
        pdf.new_page()
        pdf.add_filled_rect(35, 598, 362, 28, 0.88)
        pdf.add_centered_text(607, f"GRIEF JOURNAL - DAY {day}", 'F2', 12)
        pdf.add_text(40, 580, "Date: ____________", 'F1', 9)

        y = 555
        entries = [
            ("Grief level today (1-10):", 0),
            ("Where I found God today:", 2),
            ("One thing I'm grateful for:", 1),
            ("Scripture that held me:", 1),
            ("My prayer:", 3),
        ]
        for label, lines in entries:
            pdf.add_text(40, y, label, 'F2', 9)
            if lines == 0:
                pdf.add_line(200, y - 2, 392, y - 2, 0.5, 0.7)
                y -= 18
            else:
                for _ in range(lines):
                    y -= 14
                    pdf.add_line(40, y, 392, y, 0.5, 0.7)
                y -= 16

    # Memory Preservation
    pdf.new_page()
    pdf.add_centered_text(600, "MEMORY PRESERVATION", 'F2', 16)
    pdf.add_line(40, 588, 392, 588, 1, 0.5)
    fields2 = [
        "Their name:", "What I called them:", "Their laugh was like:",
        "Their favorite food:", "A phrase they always said:",
        "What they taught me:", "My happiest memory with them:",
        "What I wish I'd said:", "What I know they'd say to me now:",
    ]
    y = 565
    for f in fields2:
        pdf.add_text(40, y, f, 'F2', 9)
        y -= 14
        pdf.add_line(40, y, 392, y, 0.5, 0.7)
        y -= 18

    # Hope - Reunion Promises
    pdf.new_page()
    pdf.add_centered_text(600, "HOPE: REUNION PROMISES", 'F2', 16)
    pdf.add_line(40, 588, 392, 588, 1, 0.5)
    promises = [
        "John 14:2-3 - I go to prepare a place for you.",
        "1 Thess 4:13-14 - We do not grieve as those without hope.",
        "Revelation 21:4 - No more death, mourning, crying, or pain.",
        "John 11:25 - I am the resurrection and the life.",
        "Psalm 116:15 - Precious in the sight of the LORD is the death of his saints.",
        "2 Corinthians 5:8 - Absent from body, present with the Lord.",
    ]
    y = 565
    for p in promises:
        pdf.add_text(40, y, p, 'F4', 9)
        y -= 20

    y -= 10
    pdf.add_text(40, y, "The promise that gives me most hope:", 'F2', 9)
    y -= 14
    pdf.add_line(40, y, 392, y, 0.5, 0.7)

    # Support Resources
    pdf.new_page()
    pdf.add_centered_text(600, "SUPPORT RESOURCES", 'F2', 16)
    pdf.add_line(40, 588, 392, 588, 1, 0.5)
    resources = [
        "988 Suicide & Crisis Lifeline",
        "GriefShare (church-based grief support groups)",
        "Celebrate Recovery",
        "Your church pastoral care team",
        "Christian grief counselor",
        "Hospice bereavement services (free)",
    ]
    y = 565
    for r in resources:
        pdf.add_text(40, y, f"- {r}", 'F1', 10)
        y -= 18

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book207_CBT_Grief_Christian.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
