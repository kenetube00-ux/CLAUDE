"""Book 198: DAILY PRAYER JOURNAL - Bilingual (Tigrinya-English)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.93)
    pdf.add_centered_text(500, "DAILY PRAYER JOURNAL", 'F2', 20)
    pdf.add_centered_text(472, "Bilingual (Tigrinya-English)", 'F4', 13, 0.2)
    pdf.add_centered_text(430, "30 Days of Guided Prayer", 'F1', 11, 0.3)
    pdf.add_centered_text(180, f"By {author}", 'F2', 12, 0.2)

    # Copyright page
    pdf.new_page()
    pdf.add_text(50, 580, "DAILY PRAYER JOURNAL - Bilingual", 'F2', 11)
    pdf.add_text(50, 560, f"By {author}", 'F1', 10)
    pdf.add_text(50, 535, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(50, 510, "Published by KIDLYTICAL Books", 'F1', 9)

    # How to Pray guide page
    pdf.new_page()
    pdf.add_centered_text(600, "HOW TO PRAY", 'F2', 16)
    pdf.add_centered_text(578, "ብኸመይ ንጽሊ", 'F2', 13)
    pdf.add_line(50, 568, 382, 568, 1, 0.5)
    steps = [
        ("Praise / Halaletay", "Begin by praising God for who He is"),
        ("Confess / Nsihat", "Confess your sins and ask forgiveness"),
        ("Pray for Others / Tsalot nKalot", "Lift up the needs of others"),
        ("Pray for Yourself / Tsalot nNafsey", "Bring your own needs to God"),
        ("Listen / Semae", "Be still and listen for God's voice"),
    ]
    y = 540
    for title, desc in steps:
        pdf.add_text(50, y, title, 'F2', 11)
        y -= 16
        pdf.add_text(70, y, desc, 'F1', 10, 0.3)
        y -= 28

    pdf.add_text(50, y - 10, "Scripture: 'Be still and know that I am God.' - Psalm 46:10", 'F4', 10, 0.2)

    # Daily scripture promises for each day
    promises = [
        "Jeremiah 29:12 - You will call on me and pray, and I will listen.",
        "Matthew 7:7 - Ask and it will be given to you.",
        "1 John 5:14 - If we ask according to his will, he hears us.",
        "Psalm 145:18 - The LORD is near to all who call on him.",
        "James 5:16 - The prayer of a righteous person is powerful.",
        "Philippians 4:6 - In everything by prayer, let your requests be known.",
        "Romans 8:26 - The Spirit helps us in our weakness.",
        "Psalm 34:17 - The righteous cry out, and the LORD hears them.",
        "Isaiah 65:24 - Before they call I will answer.",
        "Mark 11:24 - Whatever you ask in prayer, believe you have received it.",
        "Psalm 66:19 - God has listened to my prayer.",
        "1 Thessalonians 5:17 - Pray without ceasing.",
        "Hebrews 4:16 - Let us approach the throne of grace with confidence.",
        "Psalm 55:17 - Evening, morning and noon I cry out.",
        "Matthew 6:6 - Go into your room, close the door, and pray.",
        "Colossians 4:2 - Devote yourselves to prayer.",
        "Psalm 91:15 - He will call on me and I will answer him.",
        "2 Chronicles 7:14 - If my people pray, I will heal their land.",
        "John 15:7 - If you remain in me, ask whatever you wish.",
        "Psalm 86:6 - Hear my prayer, LORD; listen to my cry.",
        "Romans 12:12 - Be faithful in prayer.",
        "Ephesians 6:18 - Pray in the Spirit on all occasions.",
        "Psalm 102:17 - He will respond to the prayer of the destitute.",
        "Luke 18:1 - They should always pray and not give up.",
        "Psalm 5:3 - Morning by morning I lay my requests before you.",
        "1 Peter 5:7 - Cast all your anxiety on him because he cares.",
        "Psalm 4:1 - Answer me when I call, O God of my righteousness.",
        "Matthew 18:20 - Where two or three gather, there am I.",
        "Psalm 116:1-2 - I love the LORD, for he heard my voice.",
        "Lamentations 3:22-23 - His mercies are new every morning."
    ]

    # 30 daily pages
    for day in range(1, 31):
        pdf.new_page()
        pdf.add_filled_rect(40, 598, 352, 30, 0.88)
        pdf.add_centered_text(608, f"DAY {day}", 'F2', 14)
        pdf.add_text(50, 580, "Date: ____________", 'F1', 9)

        y = 555
        sections = [
            ("Today I praise God for / Halaletay:", 2),
            ("I confess / Nsihat:", 2),
            ("I pray for others / Tsalot nKalot:", 3),
            ("I pray for myself / Tsalot nNafsey:", 2),
        ]
        for title, lines in sections:
            pdf.add_text(50, y, title, 'F2', 10)
            y -= 5
            for _ in range(lines):
                y -= 16
                pdf.add_line(50, y, 382, y, 0.5, 0.7)
            y -= 20

        # God's promise today
        pdf.add_text(50, y, "God's promise today:", 'F2', 10)
        y -= 16
        promise = promises[day - 1]
        pdf.add_text(60, y, promise, 'F4', 9, 0.3)

        y -= 30
        pdf.add_centered_text(y, "Amen.", 'F5', 12)

    # Monthly Prayer Review
    pdf.new_page()
    pdf.add_centered_text(600, "MONTHLY PRAYER REVIEW", 'F2', 16)
    pdf.add_line(50, 588, 382, 588, 1, 0.5)
    review_qs = [
        "What pattern do I see in my prayers?",
        "How has my relationship with God grown?",
        "Which prayer was hardest to pray? Why?",
        "What am I most grateful for this month?",
    ]
    y = 560
    for q in review_qs:
        pdf.add_text(50, y, q, 'F1', 10)
        for _ in range(3):
            y -= 17
            pdf.add_line(50, y, 382, y, 0.5, 0.7)
        y -= 22

    # Answered Prayers Tracker
    pdf.new_page()
    pdf.add_centered_text(600, "ANSWERED PRAYERS TRACKER", 'F2', 16)
    pdf.add_line(50, 588, 382, 588, 1, 0.5)
    pdf.add_text(50, 565, "Record God's faithfulness:", 'F1', 10)
    y = 540
    for i in range(12):
        pdf.add_text(50, y, f"{i+1}. Date: _____  Prayer: ", 'F1', 9)
        pdf.add_line(190, y - 2, 382, y - 2, 0.5, 0.7)
        y -= 15
        pdf.add_text(70, y, "Answer:", 'F1', 9)
        pdf.add_line(115, y - 2, 382, y - 2, 0.5, 0.7)
        y -= 25

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book198_Tigrinya_Prayer_Journal.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
