"""Book 290: WISDOM FOR MOMS - A Proverbs Coloring Devotional"""
import random
from pdf_utils import PDFDoc

random.seed(290)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    proverbs = [
        ("Day 1", "Proverbs 1:7", "The fear of the Lord is the beginning of knowledge.", "Starting with Wisdom"),
        ("Day 2", "Proverbs 3:5-6", "Trust in the Lord with all thine heart; lean not unto thine own understanding.", "Trusting God's Plan"),
        ("Day 3", "Proverbs 4:23", "Keep thy heart with all diligence; for out of it are the issues of life.", "Guarding Your Heart"),
        ("Day 4", "Proverbs 11:16", "A gracious woman retaineth honour.", "Grace in Motherhood"),
        ("Day 5", "Proverbs 12:4", "A virtuous woman is a crown to her husband.", "Strength at Home"),
        ("Day 6", "Proverbs 13:24", "He that spareth his rod hateth his son: but he that loveth him chasteneth him.", "Loving Discipline"),
        ("Day 7", "Proverbs 14:1", "Every wise woman buildeth her house.", "Building Your Home"),
        ("Day 8", "Proverbs 15:1", "A soft answer turneth away wrath.", "Words That Heal"),
        ("Day 9", "Proverbs 15:13", "A merry heart maketh a cheerful countenance.", "Choosing Joy"),
        ("Day 10", "Proverbs 16:3", "Commit thy works unto the Lord, and thy thoughts shall be established.", "Committing Daily Tasks"),
        ("Day 11", "Proverbs 16:24", "Pleasant words are as an honeycomb, sweet to the soul.", "Speaking Life"),
        ("Day 12", "Proverbs 17:6", "Children's children are the crown of old men; and the glory of children are their fathers.", "Legacy"),
        ("Day 13", "Proverbs 18:10", "The name of the Lord is a strong tower.", "Finding Refuge"),
        ("Day 14", "Proverbs 19:21", "The counsel of the Lord, that shall stand.", "God's Plans Prevail"),
        ("Day 15", "Proverbs 20:7", "The just man walketh in his integrity: his children are blessed after him.", "Integrity's Legacy"),
        ("Day 16", "Proverbs 21:5", "The thoughts of the diligent tend only to plenteousness.", "Diligent Planning"),
        ("Day 17", "Proverbs 22:6", "Train up a child in the way he should go.", "Training Children"),
        ("Day 18", "Proverbs 22:29", "Seest thou a man diligent in his business? he shall stand before kings.", "Excellence in Work"),
        ("Day 19", "Proverbs 23:24", "The father of the righteous shall greatly rejoice.", "Raising the Righteous"),
        ("Day 20", "Proverbs 24:3-4", "Through wisdom is an house builded; and by understanding it is established.", "Wisdom Builds"),
        ("Day 21", "Proverbs 25:11", "A word fitly spoken is like apples of gold.", "Perfect Timing"),
        ("Day 22", "Proverbs 27:17", "Iron sharpeneth iron; so a man sharpeneth his friend.", "Mom Friends"),
        ("Day 23", "Proverbs 29:15", "The rod and reproof give wisdom.", "Consistent Teaching"),
        ("Day 24", "Proverbs 29:25", "The fear of man bringeth a snare: but whoso putteth his trust in the Lord shall be safe.", "Freedom from Fear"),
        ("Day 25", "Proverbs 30:8", "Give me neither poverty nor riches; feed me with food convenient for me.", "Contentment"),
        ("Day 26", "Proverbs 31:10", "Who can find a virtuous woman? for her price is far above rubies.", "Your Worth"),
        ("Day 27", "Proverbs 31:25", "Strength and honour are her clothing; she shall rejoice in time to come.", "Clothed in Strength"),
        ("Day 28", "Proverbs 31:26", "She openeth her mouth with wisdom; and in her tongue is the law of kindness.", "Kind Words"),
        ("Day 29", "Proverbs 31:28", "Her children arise up, and call her blessed.", "Blessed Mother"),
        ("Day 30", "Proverbs 31:30", "A woman that feareth the Lord, she shall be praised.", "True Beauty"),
        ("Day 31", "Proverbs 3:13", "Happy is the man that findeth wisdom.", "Finding Wisdom"),
    ]
    
    floral = [
        "roses and morning glory vines",
        "sunflowers and daisies in a garden",
        "lavender sprigs and butterflies",
        "cherry blossoms on branches",
        "wildflower meadow with bees",
        "peonies and ferns arrangement",
        "tulips and lily of the valley",
        "magnolia branch with birds",
        "hydrangeas and baby's breath",
        "olive branch with fruit",
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(30, 30, 552, 732, 2, 0.3)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_filled_rect(100, 520, 412, 180, 0.90)
    doc.add_rect(100, 520, 412, 180, 2, 0.3)
    doc.add_centered_text(670, "WISDOM FOR MOMS", 'F2', 26, 0.1)
    doc.add_centered_text(635, "A Proverbs Coloring Devotional", 'F4', 16, 0.3)
    doc.add_centered_text(570, "[ILLUSTRATION: mother reading to child", 'F3', 9, 0.4)
    doc.add_centered_text(555, "surrounded by floral border with open Bible]", 'F3', 9, 0.4)
    doc.add_centered_text(300, "31 Days of Wisdom for Every Season", 'F4', 14, 0.3)
    doc.add_centered_text(270, "of Motherhood", 'F4', 14, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "WISDOM FOR MOMS", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    doc.add_text(72, 560, "For every mama doing her best with God's help.", 'F4', 11, 0.2)
    
    # TOC
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "TABLE OF CONTENTS", 'F2', 16, 0.1)
    doc.add_line(180, 725, 432, 725, 1, 0.3)
    y = 695
    for i, (day, ref, _, theme) in enumerate(proverbs[:16]):
        doc.add_text(72, y, f"{day}: {theme} ({ref}) ......... {5+i*2}", 'F1', 9, 0.3)
        y -= 16
    
    # TOC page 2
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "TABLE OF CONTENTS (cont.)", 'F2', 16, 0.1)
    y = 695
    for i, (day, ref, _, theme) in enumerate(proverbs[16:]):
        doc.add_text(72, y, f"{day}: {theme} ({ref}) ......... {37+i*2}", 'F1', 9, 0.3)
        y -= 16
    
    # Intro/How to use
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "DEAR MAMA", 'F2', 18, 0.1)
    y = 685
    intro = [
        "You are doing an incredible job.",
        "",
        "In the chaos of motherhood - the laundry piles, the tantrums,",
        "the school runs, the sleepless nights - it's easy to forget",
        "that God has wisdom specifically for YOU in this season.",
        "",
        "The book of Proverbs is packed with practical, daily wisdom",
        "that applies directly to the beautiful, exhausting work",
        "of raising humans.",
        "",
        "This devotional gives you 31 days (one for each day of the month).",
        "Each day includes:",
        "  * A coloring page with the verse beautifully illustrated",
        "  * A devotional page with application for moms",
        "",
        "HOW TO USE:",
        "  - Color while the kids nap (or while they color beside you!)",
        "  - Read the devotional during your quiet time",
        "  - Journal your thoughts in the spaces provided",
        "  - Use colored pencils, markers, or crayons",
        "  - There's no wrong way to do this",
        "",
        "You are seen. You are loved. You are enough.",
    ]
    for line in intro:
        if line.startswith("You are doing") or line.startswith("You are seen"):
            doc.add_text(72, y, line, 'F5', 11, 0.1)
        elif line.startswith("HOW"):
            doc.add_text(72, y, line, 'F2', 11, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 10, 0.25)
        y -= 17
    
    # 31 days - coloring + devotional
    for i, (day, ref, verse, theme) in enumerate(proverbs):
        # Coloring page
        doc.new_page()
        fill = 0.90 + random.uniform(0, 0.07)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(30, 30, 552, 732, 2, 0.3)
        doc.add_rect(40, 40, 532, 712, 1, 0.5)
        
        # Floral frame
        fl = floral[i % len(floral)]
        doc.add_filled_rect(50, 600, 512, 140, 0.94)
        doc.add_rect(50, 600, 512, 140, 1, 0.4)
        doc.add_centered_text(710, f"[ILLUSTRATION: {fl}]", 'F3', 9, 0.4)
        doc.add_centered_text(630, "Color this frame as you meditate", 'F3', 8, 0.5)
        
        # Verse in decorative center
        doc.add_filled_rect(70, 320, 472, 250, 0.97)
        doc.add_rect(70, 320, 472, 250, 2, 0.3)
        doc.add_rect(80, 330, 452, 230, 1, 0.5)
        
        doc.add_centered_text(535, ref, 'F2', 13, 0.1)
        words = verse.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) > 45:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        vy = 490
        for ln in lines:
            doc.add_centered_text(vy, ln, 'F5', 12, 0.15)
            vy -= 22
        
        doc.add_centered_text(345, theme, 'F4', 11, 0.3)
        
        # Bottom floral
        doc.add_filled_rect(50, 50, 512, 240, 0.93)
        doc.add_rect(50, 50, 512, 240, 1, 0.4)
        fl2 = floral[(i+5) % len(floral)]
        doc.add_centered_text(240, f"[ILLUSTRATION: {fl2}]", 'F3', 9, 0.4)
        doc.add_centered_text(85, "Color and pray, mama", 'F4', 10, 0.4)
        
        # Devotional/application page
        doc.new_page()
        fill2 = 0.93 + random.uniform(0, 0.04)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(740, f"{day}: {theme}", 'F2', 14, 0.1)
        doc.add_centered_text(718, ref, 'F4', 10, 0.3)
        doc.add_line(150, 710, 462, 710, 1, 0.4)
        
        y = 690
        doc.add_text(72, y, "FOR MOMS: How this applies to your motherhood today:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "ONE WAY I'LL APPLY THIS TODAY:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "PRAYER FOR MY CHILDREN:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "WHAT I'M GRATEFUL FOR TODAY:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "EVENING REFLECTION:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 18
    
    # Bonus: Journal pages
    for title in ["MY PRAYERS FOR EACH CHILD", "WISDOM I WANT TO PASS DOWN", "MY MOTHERHOOD TESTIMONY", "NOTES & REFLECTIONS"]:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.92)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, title, 'F2', 14, 0.1)
        doc.add_line(100, 725, 512, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22
    
    # Certificate
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(50, 100, 512, 600, 3, 0.2)
    doc.add_rect(60, 110, 492, 580, 1, 0.4)
    doc.add_centered_text(630, "WELL DONE, MAMA", 'F2', 20, 0.1)
    doc.add_centered_text(590, "You completed 31 days of Proverbs wisdom!", 'F4', 13, 0.3)
    doc.add_line(180, 560, 432, 560, 1, 0.3)
    doc.add_centered_text(540, "(your name)", 'F1', 9, 0.5)
    doc.add_centered_text(490, "\"She openeth her mouth with wisdom;", 'F4', 12, 0.25)
    doc.add_centered_text(470, "and in her tongue is the law of kindness.\"", 'F4', 12, 0.25)
    doc.add_centered_text(445, "- Proverbs 31:26", 'F4', 11, 0.35)
    doc.add_text(150, 250, "Date: _______________", 'F1', 11, 0.3)
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book290_Proverbs_Moms_Coloring.pdf')
    print("Book290_Proverbs_Moms_Coloring.pdf created successfully!")

if __name__ == "__main__":
    create_book()
