"""Book 196: THE WORD OF GOD - A Bilingual Bible Study Workbook (Tigrinya-English) Volume 1"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    title = "THE WORD OF GOD"
    subtitle = "A Bilingual Bible Study Workbook (Tigrinya-English) Volume 1"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.95)
    pdf.add_centered_text(620, title, 'F2', 28, 0)
    pdf.add_centered_text(580, subtitle, 'F4', 14, 0.2)
    pdf.add_centered_text(520, "12 Weekly Studies with Prayer Journal", 'F1', 12, 0.3)
    pdf.add_centered_text(480, "Scripture Memory & Group Discussion", 'F1', 12, 0.3)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)
    pdf.add_centered_text(160, "Bilingual Edition", 'F1', 11, 0.4)

    # Copyright page
    pdf.new_page()
    pdf.add_text(72, 700, f"THE WORD OF GOD - Volume 1", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 650, "Copyright 2025. All rights reserved.", 'F1', 10)
    pdf.add_text(72, 630, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_text(72, 600, "Scripture quotations from World English Bible (WEB) - Public Domain", 'F1', 9)
    pdf.add_text(72, 580, "Tigrinya text sections are provided for bilingual study.", 'F1', 9)
    pdf.add_text(72, 540, "Published by KIDLYTICAL Books", 'F1', 10)
    pdf.add_text(72, 520, "First Edition", 'F1', 10)

    # How to Use page
    pdf.new_page()
    pdf.add_centered_text(720, "HOW TO USE THIS BOOK", 'F2', 18)
    pdf.add_centered_text(695, "ነዚ መጽሓፍ ብኸመይ ትጥቀመሉ", 'F2', 14)
    pdf.add_line(72, 685, 540, 685, 1, 0.5)
    instructions = [
        "1. Set aside time each week for study - ideally 30-45 minutes",
        "2. Read the scripture passage in both languages",
        "3. Answer the Read & Observe questions first",
        "4. Then move to Understand & Interpret",
        "5. Finally, Apply to My Life - make it personal",
        "6. Close with prayer - use the lines provided",
        "7. Copy the memory verse at the end of each week",
        "8. Use the group discussion guide for small groups"
    ]
    y = 650
    for inst in instructions:
        pdf.add_text(72, y, inst, 'F1', 11)
        y -= 22
    pdf.add_text(72, y - 20, "May God bless your study of His Word!", 'F5', 12)

    # 12 Weekly Studies
    scriptures = [
        ("John 3:16", "For God so loved the world, that he gave his one and only Son, that whoever believes in him should not perish, but have eternal life."),
        ("Psalm 23:1-3", "The LORD is my shepherd; I shall not want. He makes me lie down in green pastures. He leads me beside still waters. He restores my soul."),
        ("Romans 8:28", "We know that all things work together for good for those who love God, for those who are called according to his purpose."),
        ("Philippians 4:6-7", "In nothing be anxious, but in everything by prayer with thanksgiving let your requests be made known to God. And the peace of God will guard your hearts."),
        ("Isaiah 40:31", "But those who wait for the LORD shall renew their strength. They shall mount up with wings as eagles. They shall run and not be weary."),
        ("Proverbs 3:5-6", "Trust in the LORD with all your heart and do not lean on your own understanding. In all your ways acknowledge him, and he will make your paths straight."),
        ("Jeremiah 29:11", "For I know the thoughts that I think toward you, says the LORD, thoughts of peace and not of evil, to give you hope and a future."),
        ("Matthew 11:28-30", "Come to me, all you who labor and are heavily burdened, and I will give you rest. Take my yoke upon you and learn from me."),
        ("2 Timothy 1:7", "For God did not give us a spirit of fear, but of power, love, and self-control."),
        ("Joshua 1:9", "Have I not commanded you? Be strong and courageous. Do not be afraid. Do not be dismayed, for the LORD your God is with you wherever you go."),
        ("Ephesians 2:8-9", "For by grace you have been saved through faith, and that not of yourselves; it is the gift of God, not of works, that no one would boast."),
        ("Romans 12:2", "Do not be conformed to this world, but be transformed by the renewing of your mind, so that you may prove what is the good and acceptable and perfect will of God.")
    ]

    for week_num, (ref, verse) in enumerate(scriptures, 1):
        # Week page
        pdf.new_page()
        pdf.add_filled_rect(50, 730, 512, 40, 0.85)
        pdf.add_centered_text(745, f"WEEK {week_num}", 'F2', 20)
        pdf.add_centered_text(710, ref, 'F5', 14)
        pdf.add_line(72, 700, 540, 700, 1, 0.6)

        # English verse
        pdf.add_text(72, 675, "English (WEB):", 'F2', 11)
        # Wrap verse text
        words = verse.split()
        line = ""
        y = 655
        for w in words:
            if len(line + " " + w) > 80:
                pdf.add_text(72, y, line, 'F4', 10)
                y -= 14
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(72, y, line, 'F4', 10)
            y -= 14

        # Tigrinya placeholder
        y -= 10
        pdf.add_text(72, y, "Tigrinya:", 'F2', 11)
        y -= 18
        pdf.add_text(72, y, "[Tigrinya scripture text here]", 'F3', 10, 0.4)

        # Read & Observe
        y -= 35
        pdf.add_text(72, y, "READ & OBSERVE", 'F2', 12)
        y -= 5
        pdf.add_line(72, y, 350, y, 0.5, 0.6)
        for i in range(3):
            y -= 20
            pdf.add_text(72, y, f"Q{i+1}: What do you notice in this passage?", 'F1', 9, 0.4)
            y -= 18
            pdf.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 16
            pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Understand & Interpret
        y -= 25
        pdf.add_text(72, y, "UNDERSTAND & INTERPRET", 'F2', 12)
        y -= 5
        pdf.add_line(72, y, 350, y, 0.5, 0.6)
        for i in range(3):
            y -= 18
            pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Apply to My Life
        y -= 25
        pdf.add_text(72, y, "APPLY TO MY LIFE", 'F2', 12)
        y -= 5
        pdf.add_line(72, y, 350, y, 0.5, 0.6)
        for i in range(3):
            y -= 18
            pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Prayer
        y -= 25
        pdf.add_text(72, y, "PRAYER", 'F2', 12)
        for i in range(3):
            y -= 18
            pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Memory Verse
        y -= 30
        pdf.add_text(72, y, "MEMORY VERSE - Copy the verse here:", 'F2', 10)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Notes
        y -= 25
        pdf.add_text(72, y, "NOTES:", 'F2', 10)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Prayer Journal Pages (5 pages)
    for pj in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, "PRAYER JOURNAL", 'F2', 16)
        pdf.add_centered_text(730, f"Page {pj}", 'F1', 10, 0.4)
        pdf.add_line(72, 720, 540, 720, 1, 0.6)

        pdf.add_text(72, 695, "Date: ____________", 'F1', 10)
        sections = ["Praise & Thanksgiving:", "Confession:", "Prayers for Others:", "Prayers for Myself:", "What God is Saying:"]
        y = 665
        for sec in sections:
            pdf.add_text(72, y, sec, 'F2', 11)
            for _ in range(3):
                y -= 18
                pdf.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 25

    # Scripture Memory Cards page
    pdf.new_page()
    pdf.add_centered_text(750, "SCRIPTURE MEMORY CARDS", 'F2', 16)
    pdf.add_text(72, 720, "Cut along the dotted lines. Carry these cards with you.", 'F1', 10)
    y = 690
    for i in range(4):
        pdf.add_rect(72, y - 90, 460, 85, 0.5, 0.5)
        ref_text = scriptures[i][0] if i < len(scriptures) else "Your Verse"
        pdf.add_text(82, y - 20, ref_text, 'F2', 11)
        pdf.add_text(82, y - 40, "Write the verse here:", 'F1', 9, 0.4)
        pdf.add_line(82, y - 55, 520, y - 55, 0.5, 0.7)
        pdf.add_line(82, y - 70, 520, y - 70, 0.5, 0.7)
        y -= 105

    # Group Discussion Guide
    pdf.new_page()
    pdf.add_centered_text(750, "GROUP DISCUSSION GUIDE", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "Use these questions for your small group or Bible study:", 'F1', 11)
    questions = [
        "1. What stood out to you from this week's passage?",
        "2. How does this scripture apply to your daily life?",
        "3. What did you learn about God's character?",
        "4. How has God been speaking to you this week?",
        "5. What is one thing you will do differently because of this study?",
        "6. How can we pray for each other?",
        "7. What was the hardest question to answer? Why?",
        "8. Share your memory verse with the group."
    ]
    y = 680
    for q in questions:
        pdf.add_text(72, y, q, 'F1', 11)
        y -= 30
        pdf.add_line(100, y, 540, y, 0.5, 0.7)
        y -= 25

    pdf.add_text(72, y - 20, "Leader's Tip: Allow silence after questions. Let the Spirit work.", 'F5', 10, 0.3)

    # Fill to 40 pages - additional notes pages
    current_pages = len(pdf.pages) + 1
    for extra in range(40 - current_pages):
        pdf.new_page()
        pdf.add_centered_text(750, "NOTES", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 0.5, 0.6)
        y = 710
        while y > 80:
            pdf.add_line(72, y, 540, y, 0.5, 0.8)
            y -= 22

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book196_Tigrinya_Bible_Study_V1.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
