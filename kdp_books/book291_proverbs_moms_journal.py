"""Book 291: SHE SPEAKS WISDOM - A 31-Day Proverbs Journal for Mothers"""
import random
from pdf_utils import PDFDoc

random.seed(291)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    proverbs = [
        ("Day 1", "Proverbs 1:7", "The fear of the Lord is the beginning of knowledge.", "Starting with Reverence"),
        ("Day 2", "Proverbs 2:6", "For the Lord giveth wisdom: out of his mouth cometh knowledge.", "God-Given Wisdom"),
        ("Day 3", "Proverbs 3:5-6", "Trust in the Lord with all thine heart; lean not unto thine own understanding.", "Total Trust"),
        ("Day 4", "Proverbs 3:13", "Happy is the man that findeth wisdom, and getteth understanding.", "Finding Joy"),
        ("Day 5", "Proverbs 4:23", "Keep thy heart with all diligence; for out of it are the issues of life.", "Heart Guard"),
        ("Day 6", "Proverbs 6:20-21", "My son, keep thy father's commandment, and forsake not the law of thy mother.", "Teaching Persists"),
        ("Day 7", "Proverbs 8:11", "For wisdom is better than rubies.", "True Value"),
        ("Day 8", "Proverbs 10:12", "Love covereth all sins.", "Love Covers"),
        ("Day 9", "Proverbs 11:25", "The liberal soul shall be made fat: he that watereth shall be watered also.", "Generosity"),
        ("Day 10", "Proverbs 12:25", "Heaviness in the heart maketh it stoop: but a good word maketh it glad.", "Encouraging Words"),
        ("Day 11", "Proverbs 13:12", "Hope deferred maketh the heart sick: but when the desire cometh, it is a tree of life.", "Hope Fulfilled"),
        ("Day 12", "Proverbs 14:1", "Every wise woman buildeth her house; but the foolish plucketh it down.", "Building Daily"),
        ("Day 13", "Proverbs 14:26", "In the fear of the Lord is strong confidence: his children shall have a place of refuge.", "Safe Haven"),
        ("Day 14", "Proverbs 15:1", "A soft answer turneth away wrath: but grievous words stir up anger.", "Gentle Response"),
        ("Day 15", "Proverbs 15:13", "A merry heart maketh a cheerful countenance.", "Joyful Spirit"),
        ("Day 16", "Proverbs 16:3", "Commit thy works unto the Lord, and thy thoughts shall be established.", "Committing Plans"),
        ("Day 17", "Proverbs 16:24", "Pleasant words are as an honeycomb, sweet to the soul, and health to the bones.", "Healing Words"),
        ("Day 18", "Proverbs 17:22", "A merry heart doeth good like a medicine.", "Joy as Medicine"),
        ("Day 19", "Proverbs 19:21", "There are many devices in a man's heart; but the counsel of the Lord shall stand.", "His Plans Win"),
        ("Day 20", "Proverbs 20:7", "The just man walketh in his integrity: his children are blessed.", "Integrity Blesses"),
        ("Day 21", "Proverbs 22:6", "Train up a child in the way he should go: and when he is old, he will not depart.", "Faithful Training"),
        ("Day 22", "Proverbs 23:24-25", "The father of the righteous shall greatly rejoice.", "Righteous Children"),
        ("Day 23", "Proverbs 24:3-4", "Through wisdom is an house builded; and by understanding it is established.", "Wisdom Builds"),
        ("Day 24", "Proverbs 25:11", "A word fitly spoken is like apples of gold in pictures of silver.", "Right Words"),
        ("Day 25", "Proverbs 27:17", "Iron sharpeneth iron; so a man sharpeneth the countenance of his friend.", "Mom Community"),
        ("Day 26", "Proverbs 29:17", "Correct thy son, and he shall give thee rest; yea, he shall give delight.", "Consistent Correction"),
        ("Day 27", "Proverbs 31:10", "Who can find a virtuous woman? for her price is far above rubies.", "Beyond Rubies"),
        ("Day 28", "Proverbs 31:25", "Strength and honour are her clothing; she shall rejoice in time to come.", "Clothed in Strength"),
        ("Day 29", "Proverbs 31:26", "She openeth her mouth with wisdom; and in her tongue is the law of kindness.", "Wisdom & Kindness"),
        ("Day 30", "Proverbs 31:28", "Her children arise up, and call her blessed; her husband also.", "Called Blessed"),
        ("Day 31", "Proverbs 31:30", "A woman that feareth the Lord, she shall be praised.", "True Praise"),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(30, 30, 552, 732, 2, 0.3)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_filled_rect(80, 530, 452, 170, 0.88)
    doc.add_rect(80, 530, 452, 170, 2, 0.3)
    doc.add_centered_text(670, "SHE SPEAKS WISDOM", 'F2', 26, 0.1)
    doc.add_centered_text(635, "A 31-Day Proverbs Journal", 'F4', 16, 0.25)
    doc.add_centered_text(610, "for Mothers", 'F4', 16, 0.25)
    doc.add_centered_text(570, "[ILLUSTRATION: elegant journal with", 'F3', 9, 0.4)
    doc.add_centered_text(555, "pressed flowers and open Bible]", 'F3', 9, 0.4)
    doc.add_centered_text(250, "Daily Wisdom. Practical Application.", 'F4', 13, 0.3)
    doc.add_centered_text(225, "Prayers for Your Children.", 'F4', 13, 0.3)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "SHE SPEAKS WISDOM", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    doc.add_text(72, 560, "For the woman who juggles everything and still seeks God.", 'F4', 11, 0.2)
    
    # Introduction
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "A NOTE TO YOU, MAMA", 'F2', 16, 0.1)
    doc.add_line(180, 715, 432, 715, 1, 0.4)
    y = 680
    intro = [
        "The book of Proverbs was written by a king - but much of it was",
        "first taught to him by his MOTHER (Proverbs 31:1).",
        "",
        "As mothers, we are wisdom-keepers. We are the ones who shape",
        "hearts, build homes, and speak life into the next generation.",
        "",
        "This journal walks you through 31 Proverbs - one for each day",
        "of the month. Unlike a coloring devotional, this is a pure",
        "JOURNAL experience. Each day gives you:",
        "",
        "  * The verse in full",
        "  * A reflection: 'What this means for my motherhood'",
        "  * A prompt: 'One way I'll apply this today'",
        "  * Space for: 'Prayer for my children'",
        "  * An evening reflection check-in",
        "",
        "You can use this journal month after month. The wisdom of",
        "Proverbs meets you differently in every season.",
        "",
        "Pour yourself a cup of something warm. Breathe. Begin.",
    ]
    for line in intro:
        if line.startswith("As mothers") or line.startswith("Pour"):
            doc.add_text(72, y, line, 'F5', 10, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 10, 0.25)
        y -= 17
    
    # 31 daily journal pages (each 2 pages to hit 72+)
    for i, (day, ref, verse, theme) in enumerate(proverbs):
        # Page 1
        doc.new_page()
        fill = 0.92 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        
        # Header
        doc.add_filled_rect(40, 740, 532, 35, 0.88)
        doc.add_rect(40, 740, 532, 35, 1, 0.3)
        doc.add_text(55, 752, f"{day}: {theme}", 'F2', 13, 0.1)
        doc.add_text(420, 752, ref, 'F4', 10, 0.3)
        
        # Verse box
        doc.add_filled_rect(55, 670, 502, 55, 0.95)
        doc.add_rect(55, 670, 502, 55, 1, 0.4)
        words = verse.split()
        line1 = ""
        line2 = ""
        for w in words:
            if len(line1 + " " + w) <= 65 and not line2:
                line1 = (line1 + " " + w).strip()
            else:
                line2 = (line2 + " " + w).strip()
        doc.add_text(70, 705, f'"{line1}', 'F4', 10, 0.2)
        if line2:
            doc.add_text(70, 688, f'{line2}"', 'F4', 10, 0.2)
        else:
            pass
        doc.add_text(70, 675, f"  - {ref} (KJV)", 'F1', 8, 0.4)
        
        y = 645
        # What this means for my motherhood
        doc.add_text(72, y, "WHAT THIS MEANS FOR MY MOTHERHOOD:", 'F2', 11, 0.15)
        y -= 20
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        y -= 10
        # One way I'll apply this
        doc.add_text(72, y, "ONE WAY I'LL APPLY THIS TODAY:", 'F2', 11, 0.15)
        y -= 20
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        y -= 10
        # Prayer for my children
        doc.add_text(72, y, "PRAYER FOR MY CHILDREN:", 'F2', 11, 0.15)
        y -= 20
        for _ in range(6):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        # Page 2: Evening reflection
        doc.new_page()
        fill2 = 0.94 + random.uniform(0, 0.03)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"{day} - Evening Reflection", 'F2', 12, 0.15)
        doc.add_line(55, 745, 557, 745, 1, 0.4)
        
        y = 720
        doc.add_text(72, y, "HOW DID I SEE THIS PROVERB PLAY OUT TODAY?", 'F2', 10, 0.15)
        y -= 20
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        y -= 10
        doc.add_text(72, y, "SOMETHING MY CHILD DID/SAID THAT MADE ME THINK:", 'F2', 10, 0.15)
        y -= 20
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        y -= 10
        doc.add_text(72, y, "WHERE I NEED WISDOM TOMORROW:", 'F2', 10, 0.15)
        y -= 20
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        y -= 10
        doc.add_text(72, y, "MY HONEST MOMENT WITH GOD:", 'F2', 10, 0.15)
        y -= 20
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        # Rating box
        y -= 15
        doc.add_filled_rect(55, y-50, 502, 60, 0.88)
        doc.add_rect(55, y-50, 502, 60, 1, 0.3)
        doc.add_text(70, y, "Today's motherhood rating: 1  2  3  4  5  6  7  8  9  10", 'F1', 9, 0.3)
        doc.add_text(70, y-18, "I felt closest to God when: ________________________________", 'F1', 9, 0.3)
        doc.add_text(70, y-36, "Tomorrow's focus: ________________________________________", 'F1', 9, 0.3)
    
    # Bonus pages
    bonus_titles = ["MY CHILDREN'S PRAYER NEEDS", "WISDOM I WANT THEM TO KNOW", "MONTHLY REFLECTION", "FAVORITE PROVERBS", "LETTERS TO MY CHILDREN", "WHAT MOTHERHOOD TAUGHT ME", "GOALS FOR NEXT MONTH"]
    for title in bonus_titles:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.91)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, title, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book291_Proverbs_Moms_Journal.pdf')
    print("Book291_Proverbs_Moms_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
