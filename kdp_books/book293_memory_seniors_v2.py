"""Book 293: HIDE IT IN YOUR HEART - Large Print Bible Memory Workbook for Seniors Vol 2"""
import random
from pdf_utils import PDFDoc

random.seed(293)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    topics = {
        "PEACE": [
            ("Isaiah 26:3", "Thou wilt keep him in perfect peace, whose mind is stayed on thee."),
            ("John 14:27", "Peace I leave with you, my peace I give unto you."),
            ("Philippians 4:7", "The peace of God shall keep your hearts and minds."),
            ("Psalm 4:8", "I will both lay me down in peace, and sleep."),
            ("Isaiah 9:6", "His name shall be called the Prince of Peace."),
            ("Colossians 3:15", "Let the peace of God rule in your hearts."),
            ("Numbers 6:26", "The Lord lift up his countenance upon thee, and give thee peace."),
            ("Romans 5:1", "Being justified by faith, we have peace with God."),
        ],
        "STRENGTH": [
            ("Isaiah 40:29", "He giveth power to the faint; and to them that have no might he increaseth strength."),
            ("Psalm 18:2", "The Lord is my rock, and my fortress, and my deliverer."),
            ("Nehemiah 8:10", "The joy of the Lord is your strength."),
            ("Psalm 28:7", "The Lord is my strength and my shield; my heart trusted in him."),
            ("Isaiah 41:10", "I will strengthen thee; yea, I will help thee."),
            ("Psalm 73:26", "God is the strength of my heart, and my portion for ever."),
            ("2 Corinthians 12:9", "My grace is sufficient for thee: for my strength is made perfect in weakness."),
            ("Philippians 4:13", "I can do all things through Christ which strengtheneth me."),
        ],
        "HOPE": [
            ("Romans 15:13", "The God of hope fill you with all joy and peace in believing."),
            ("Jeremiah 29:11", "I know the thoughts I think toward you; thoughts of peace and not of evil."),
            ("Psalm 42:11", "Hope thou in God: for I shall yet praise him."),
            ("Hebrews 6:19", "Which hope we have as an anchor of the soul, both sure and stedfast."),
            ("Romans 8:24", "We are saved by hope."),
            ("Psalm 31:24", "Be of good courage, and he shall strengthen your heart, all ye that hope in the Lord."),
            ("Lamentations 3:25", "The Lord is good unto them that wait for him."),
            ("1 Peter 1:3", "Hath begotten us again unto a lively hope by the resurrection."),
        ],
        "LOVE": [
            ("1 John 4:8", "God is love."),
            ("John 3:16", "For God so loved the world, that he gave his only begotten Son."),
            ("Romans 8:38-39", "Nothing shall separate us from the love of God."),
            ("1 Corinthians 13:4", "Love suffereth long, and is kind."),
            ("1 John 4:19", "We love him, because he first loved us."),
            ("Psalm 136:1", "O give thanks unto the Lord; for his mercy endureth for ever."),
            ("Ephesians 3:19", "To know the love of Christ, which passeth knowledge."),
            ("Zephaniah 3:17", "He will rejoice over thee with singing."),
        ],
        "FAITH": [
            ("Hebrews 11:1", "Faith is the substance of things hoped for, the evidence of things not seen."),
            ("Romans 10:17", "Faith cometh by hearing, and hearing by the word of God."),
            ("Mark 11:22", "Have faith in God."),
            ("2 Corinthians 5:7", "We walk by faith, not by sight."),
            ("Hebrews 11:6", "Without faith it is impossible to please him."),
            ("Galatians 2:20", "I live by the faith of the Son of God, who loved me."),
            ("Matthew 17:20", "If ye have faith as a grain of mustard seed."),
            ("Ephesians 2:8", "By grace are ye saved through faith."),
        ],
        "COMFORT": [
            ("Psalm 23:4", "Yea, though I walk through the valley of the shadow of death, I will fear no evil."),
            ("2 Corinthians 1:3", "The God of all comfort."),
            ("Matthew 5:4", "Blessed are they that mourn: for they shall be comforted."),
            ("Psalm 34:18", "The Lord is nigh unto them that are of a broken heart."),
            ("Isaiah 49:13", "The Lord hath comforted his people."),
            ("Psalm 119:50", "This is my comfort in my affliction: for thy word hath quickened me."),
        ],
        "JOY": [
            ("Psalm 16:11", "In thy presence is fulness of joy."),
            ("John 15:11", "That your joy might be full."),
            ("Psalm 30:5", "Joy cometh in the morning."),
            ("Romans 14:17", "The kingdom of God is righteousness, and peace, and joy."),
            ("Psalm 126:5", "They that sow in tears shall reap in joy."),
            ("Habakkuk 3:18", "Yet I will rejoice in the Lord, I will joy in the God of my salvation."),
        ],
    }
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(30, 30, 552, 732, 3, 0.3)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_centered_text(680, "HIDE IT IN YOUR HEART", 'F2', 26, 0.1)
    doc.add_centered_text(645, "Large Print Bible Memory Workbook", 'F4', 16, 0.25)
    doc.add_centered_text(620, "for Seniors - Volume 2", 'F4', 16, 0.25)
    doc.add_filled_rect(150, 380, 312, 150, 0.88)
    doc.add_rect(150, 380, 312, 150, 2, 0.3)
    doc.add_centered_text(490, "[ILLUSTRATION: heart shape filled", 'F3', 10, 0.4)
    doc.add_centered_text(475, "with Scripture words, elegant style]", 'F3', 10, 0.4)
    doc.add_centered_text(250, "52 Verses Organized by Topic", 'F4', 14, 0.3)
    doc.add_centered_text(220, "Peace | Strength | Hope | Love | Faith | Comfort | Joy", 'F1', 11, 0.35)
    doc.add_centered_text(110, author, 'F2', 18, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "HIDE IT IN YOUR HEART - Vol. 2", 'F2', 14, 0.2)
    doc.add_text(72, 640, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 12, 0.2)
    doc.add_text(72, 610, "Scripture from King James Version (Public Domain).", 'F1', 11, 0.3)
    doc.add_text(72, 580, "ALL text minimum 14pt for comfortable reading.", 'F2', 12, 0.2)
    doc.add_text(72, 550, "Published by KDP Amazon", 'F1', 12, 0.3)
    
    # How to use
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "HOW TO USE THIS BOOK", 'F2', 20, 0.1)
    y = 680
    instr = [
        "Welcome to Volume 2! This book organizes 52 verses",
        "by TOPIC so you can memorize what you need most.",
        "",
        "TOPICS COVERED:",
        "  Peace (8 verses)    Strength (8 verses)",
        "  Hope (8 verses)     Love (8 verses)",
        "  Faith (8 verses)    Comfort (6 verses)",
        "  Joy (6 verses)",
        "",
        "EACH VERSE INCLUDES:",
        "  1. The verse in LARGE PRINT",
        "  2. WRITE IT OUT - copy in your handwriting",
        "  3. FILL IN THE BLANKS - test your recall",
        "  4. FIRST LETTER PROMPTS - final challenge",
        "",
        "MEMORY TIPS FOR SENIORS:",
        "  - Say the verse aloud morning and evening",
        "  - Associate it with a daily activity",
        "  - Teach it to a grandchild (teaching = learning!)",
        "  - Don't rush. Take your time with each verse.",
    ]
    for line in instr:
        if "TOPICS" in line or "EACH" in line or "MEMORY" in line:
            doc.add_text(72, y, line, 'F2', 14, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 14, 0.25)
        y -= 24
    
    # Content pages
    week_num = 1
    for topic, topic_verses in topics.items():
        # Topic divider page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.88)
        doc.add_rect(50, 200, 512, 400, 3, 0.2)
        doc.add_rect(60, 210, 492, 380, 1, 0.4)
        doc.add_centered_text(480, topic, 'F2', 32, 0.1)
        doc.add_centered_text(430, f"{len(topic_verses)} Verses to Memorize", 'F4', 18, 0.3)
        doc.add_centered_text(370, f"Weeks {week_num}-{week_num + len(topic_verses) - 1}", 'F1', 14, 0.4)
        
        for j, (ref, verse) in enumerate(topic_verses):
            doc.new_page()
            fill = 0.93 + random.uniform(0, 0.04)
            doc.add_filled_rect(0, 0, 612, 792, fill)
            doc.add_rect(40, 40, 532, 712, 2, 0.3)
            
            # Header
            doc.add_filled_rect(40, 740, 532, 35, 0.88)
            doc.add_rect(40, 740, 532, 35, 1, 0.3)
            doc.add_text(55, 752, f"Week {week_num} - {topic}", 'F2', 14, 0.1)
            doc.add_text(400, 752, ref, 'F4', 12, 0.3)
            
            y = 705
            # Large verse
            doc.add_text(72, y, "THIS WEEK'S VERSE:", 'F2', 14, 0.15)
            y -= 30
            words = verse.split()
            lines = []
            cur = ""
            for w in words:
                if len(cur + " " + w) > 38:
                    lines.append(cur)
                    cur = w
                else:
                    cur = (cur + " " + w).strip()
            if cur:
                lines.append(cur)
            for ln in lines:
                doc.add_text(90, y, ln, 'F5', 16, 0.1)
                y -= 28
            doc.add_text(90, y, f"  - {ref}", 'F4', 14, 0.3)
            y -= 35
            
            # Write it out
            doc.add_text(72, y, "WRITE IT OUT:", 'F2', 14, 0.15)
            y -= 28
            for _ in range(3):
                doc.add_line(72, y, 540, y, 0.5, 0.5)
                y -= 28
            
            # Fill in blanks
            y -= 12
            doc.add_text(72, y, "FILL IN THE BLANKS:", 'F2', 14, 0.15)
            y -= 28
            blank_positions = random.sample(range(len(words)), min(len(words)//3 + 1, len(words)))
            blanked = []
            for k, w in enumerate(words):
                if k in blank_positions:
                    blanked.append("_" * max(len(w), 4))
                else:
                    blanked.append(w)
            blank_text = " ".join(blanked)
            blines = []
            cur = ""
            for w in blank_text.split():
                if len(cur + " " + w) > 42:
                    blines.append(cur)
                    cur = w
                else:
                    cur = (cur + " " + w).strip()
            if cur:
                blines.append(cur)
            for ln in blines:
                doc.add_text(90, y, ln, 'F4', 14, 0.2)
                y -= 26
            
            # First letters
            y -= 12
            doc.add_text(72, y, "FIRST LETTER PROMPTS:", 'F2', 14, 0.15)
            y -= 28
            firsts = " ".join([w[0].upper() + "___" for w in words])
            fl_lines = []
            cur = ""
            for w in firsts.split():
                if len(cur + " " + w) > 45:
                    fl_lines.append(cur)
                    cur = w
                else:
                    cur = (cur + " " + w).strip()
            if cur:
                fl_lines.append(cur)
            for ln in fl_lines:
                doc.add_text(90, y, ln, 'F3', 14, 0.3)
                y -= 26
            
            week_num += 1
    
    # Review checklist
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "MASTERY CHECKLIST", 'F2', 16, 0.1)
    y = 700
    wk = 1
    for topic, tv in topics.items():
        doc.add_text(72, y, f"{topic}:", 'F2', 11, 0.15)
        y -= 16
        for ref, _ in tv:
            doc.add_text(90, y, f"[ ] Week {wk}: {ref}", 'F1', 9, 0.3)
            y -= 14
            wk += 1
        y -= 8
    
    # Bonus review pages - one per topic
    for topic, tv in topics.items():
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.92)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, f"REVIEW: {topic}", 'F2', 16, 0.1)
        ry = 695
        doc.add_text(72, ry, "Write each verse from memory:", 'F2', 14, 0.15)
        ry -= 30
        for ref, verse in tv:
            doc.add_text(72, ry, f"{ref}:", 'F2', 11, 0.2)
            ry -= 22
            for _ in range(2):
                doc.add_line(72, ry, 540, ry, 0.5, 0.5)
                ry -= 22
            ry -= 10
    
    # Certificate
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.91)
    doc.add_rect(50, 100, 512, 600, 3, 0.2)
    doc.add_rect(60, 110, 492, 580, 1, 0.4)
    doc.add_centered_text(630, "CERTIFICATE OF ACHIEVEMENT", 'F2', 20, 0.1)
    doc.add_centered_text(580, "This certifies that", 'F4', 16, 0.3)
    doc.add_line(180, 550, 432, 550, 1, 0.3)
    doc.add_centered_text(510, "has hidden God's Word in their heart", 'F4', 16, 0.3)
    doc.add_centered_text(480, "through 52 weeks of faithful memorization.", 'F4', 14, 0.3)
    doc.add_centered_text(420, "\"Thy word have I hid in mine heart,", 'F5', 14, 0.2)
    doc.add_centered_text(395, "that I might not sin against thee.\"", 'F5', 14, 0.2)
    doc.add_centered_text(365, "- Psalm 119:11", 'F4', 12, 0.35)
    doc.add_text(150, 220, "Date: _______________", 'F1', 14, 0.3)

    # Extra notes page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "MEMORY NOTES & REFLECTIONS", 'F2', 14, 0.1)
    doc.add_line(130, 725, 482, 725, 1, 0.4)
    y = 695
    for _ in range(28):
        doc.add_line(72, y, 540, y, 0.5, 0.6)
        y -= 22
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book293_Scripture_Memory_Seniors_V2.pdf')
    print("Book293_Scripture_Memory_Seniors_V2.pdf created successfully!")

if __name__ == "__main__":
    create_book()
