"""Book 292: REMEMBER HIS WORD - Large Print Scripture Memory for Seniors (52 Weeks)"""
import random
from pdf_utils import PDFDoc

random.seed(292)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    verses = [
        ("Week 1", "Psalm 23:1", "The Lord is my shepherd; I shall not want."),
        ("Week 2", "Proverbs 3:5", "Trust in the Lord with all thine heart."),
        ("Week 3", "Isaiah 41:10", "Fear thou not; for I am with thee."),
        ("Week 4", "Philippians 4:13", "I can do all things through Christ which strengtheneth me."),
        ("Week 5", "Romans 8:28", "All things work together for good to them that love God."),
        ("Week 6", "Psalm 46:1", "God is our refuge and strength, a very present help in trouble."),
        ("Week 7", "John 3:16", "For God so loved the world, that he gave his only begotten Son."),
        ("Week 8", "Jeremiah 29:11", "For I know the thoughts that I think toward you, saith the Lord."),
        ("Week 9", "Psalm 118:24", "This is the day which the Lord hath made; we will rejoice in it."),
        ("Week 10", "Isaiah 40:31", "They that wait upon the Lord shall renew their strength."),
        ("Week 11", "Psalm 27:1", "The Lord is my light and my salvation; whom shall I fear?"),
        ("Week 12", "Romans 15:13", "Now the God of hope fill you with all joy and peace in believing."),
        ("Week 13", "Psalm 91:1", "He that dwelleth in the secret place of the most High."),
        ("Week 14", "Matthew 11:28", "Come unto me, all ye that labour and are heavy laden."),
        ("Week 15", "Psalm 119:105", "Thy word is a lamp unto my feet, and a light unto my path."),
        ("Week 16", "Joshua 1:9", "Be strong and of a good courage; be not afraid."),
        ("Week 17", "Psalm 34:8", "O taste and see that the Lord is good."),
        ("Week 18", "2 Timothy 1:7", "God hath not given us the spirit of fear; but of power and love."),
        ("Week 19", "Psalm 100:5", "For the Lord is good; his mercy is everlasting."),
        ("Week 20", "Hebrews 13:5", "I will never leave thee, nor forsake thee."),
        ("Week 21", "Psalm 37:4", "Delight thyself in the Lord; he shall give thee the desires of thine heart."),
        ("Week 22", "1 John 4:19", "We love him, because he first loved us."),
        ("Week 23", "Psalm 145:18", "The Lord is nigh unto all them that call upon him."),
        ("Week 24", "Philippians 4:6", "Be careful for nothing; but in every thing by prayer."),
        ("Week 25", "Psalm 139:14", "I am fearfully and wonderfully made."),
        ("Week 26", "Romans 12:2", "Be ye transformed by the renewing of your mind."),
        ("Week 27", "Psalm 46:10", "Be still, and know that I am God."),
        ("Week 28", "Galatians 5:22", "The fruit of the Spirit is love, joy, peace."),
        ("Week 29", "Psalm 103:1", "Bless the Lord, O my soul: and all that is within me."),
        ("Week 30", "Matthew 6:33", "Seek ye first the kingdom of God."),
        ("Week 31", "Psalm 121:1-2", "I will lift up mine eyes unto the hills."),
        ("Week 32", "1 Peter 5:7", "Casting all your care upon him; for he careth for you."),
        ("Week 33", "Psalm 19:14", "Let the words of my mouth be acceptable in thy sight."),
        ("Week 34", "Ephesians 2:8", "For by grace are ye saved through faith."),
        ("Week 35", "Psalm 30:5", "Weeping may endure for a night, but joy cometh in the morning."),
        ("Week 36", "Colossians 3:23", "Whatsoever ye do, do it heartily, as to the Lord."),
        ("Week 37", "Psalm 55:22", "Cast thy burden upon the Lord, and he shall sustain thee."),
        ("Week 38", "James 1:5", "If any of you lack wisdom, let him ask of God."),
        ("Week 39", "Psalm 147:3", "He healeth the broken in heart, and bindeth up their wounds."),
        ("Week 40", "1 Thessalonians 5:18", "In every thing give thanks."),
        ("Week 41", "Psalm 150:6", "Let every thing that hath breath praise the Lord."),
        ("Week 42", "Deuteronomy 31:6", "Be strong; he will not fail thee, nor forsake thee."),
        ("Week 43", "Psalm 23:4", "Though I walk through the valley of the shadow of death."),
        ("Week 44", "John 14:27", "Peace I leave with you, my peace I give unto you."),
        ("Week 45", "Psalm 62:1", "Truly my soul waiteth upon God; from him cometh my salvation."),
        ("Week 46", "Matthew 28:20", "Lo, I am with you always, even unto the end of the world."),
        ("Week 47", "Psalm 73:26", "God is the strength of my heart, and my portion for ever."),
        ("Week 48", "2 Corinthians 12:9", "My grace is sufficient for thee."),
        ("Week 49", "Psalm 90:12", "Teach us to number our days."),
        ("Week 50", "Hebrews 12:1", "Let us run with patience the race that is set before us."),
        ("Week 51", "Psalm 23:6", "Surely goodness and mercy shall follow me all the days of my life."),
        ("Week 52", "Revelation 21:4", "God shall wipe away all tears from their eyes."),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(30, 30, 552, 732, 3, 0.3)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_centered_text(680, "REMEMBER HIS WORD", 'F2', 28, 0.1)
    doc.add_centered_text(640, "Large Print Scripture Memory", 'F4', 18, 0.25)
    doc.add_centered_text(610, "for Seniors", 'F4', 18, 0.25)
    doc.add_centered_text(570, "(52 Weeks)", 'F2', 16, 0.3)
    doc.add_filled_rect(150, 350, 312, 150, 0.90)
    doc.add_rect(150, 350, 312, 150, 2, 0.3)
    doc.add_centered_text(460, "[ILLUSTRATION: open Bible with", 'F3', 10, 0.4)
    doc.add_centered_text(445, "reading glasses and warm light]", 'F3', 10, 0.4)
    doc.add_centered_text(200, "One Verse Per Week", 'F4', 16, 0.3)
    doc.add_centered_text(175, "Write It. Learn It. Live It.", 'F2', 14, 0.2)
    doc.add_centered_text(110, author, 'F2', 18, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "REMEMBER HIS WORD", 'F2', 16, 0.2)
    doc.add_text(72, 640, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 12, 0.2)
    doc.add_text(72, 610, "Scripture from King James Version (Public Domain).", 'F1', 11, 0.3)
    doc.add_text(72, 580, "All text is in LARGE PRINT (14pt minimum) for easy reading.", 'F1', 12, 0.2)
    doc.add_text(72, 550, "Published by KDP Amazon", 'F1', 12, 0.3)
    
    # How to use
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "HOW TO USE THIS BOOK", 'F2', 20, 0.1)
    doc.add_line(170, 714, 442, 714, 1, 0.3)
    y = 680
    instructions = [
        "This book helps you memorize one Bible verse per week.",
        "",
        "EACH WEEK HAS THREE EXERCISES:",
        "",
        "1. READ & WRITE - The verse is printed in large type.",
        "   Copy it out in your own handwriting below.",
        "",
        "2. FILL IN THE BLANKS - The same verse with key words",
        "   removed. Fill them in from memory.",
        "",
        "3. FIRST LETTER PROMPTS - Only the first letter of each",
        "   word is given. Recite the verse using these hints.",
        "",
        "TIPS FOR SUCCESS:",
        "  - Read the verse aloud 3 times each morning",
        "  - Write it on a card for your refrigerator",
        "  - Ask a friend to quiz you on weekends",
        "  - Don't worry about perfect recall - progress counts!",
        "  - Review previous weeks often",
    ]
    for line in instructions:
        if "EACH WEEK" in line or "TIPS" in line:
            doc.add_text(72, y, line, 'F2', 14, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 14, 0.25)
        y -= 24
    
    # 52 weekly entries
    for i, (week, ref, verse) in enumerate(verses):
        doc.new_page()
        fill = 0.92 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        
        # Week header
        doc.add_filled_rect(40, 740, 532, 35, 0.88)
        doc.add_rect(40, 740, 532, 35, 1, 0.3)
        doc.add_text(55, 752, f"{week}", 'F2', 16, 0.1)
        doc.add_text(400, 752, ref, 'F4', 14, 0.3)
        
        # LARGE verse display
        y = 705
        doc.add_text(72, y, "THIS WEEK'S VERSE:", 'F2', 14, 0.15)
        y -= 30
        # Split verse for large display
        words = verse.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) > 40:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        for ln in lines:
            doc.add_text(90, y, ln, 'F5', 16, 0.1)
            y -= 26
        doc.add_text(90, y, f"  - {ref}", 'F4', 14, 0.3)
        y -= 35
        
        # Write it out section
        doc.add_text(72, y, "WRITE IT OUT:", 'F2', 14, 0.15)
        y -= 25
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 28
        
        # Fill in the blanks
        y -= 15
        doc.add_text(72, y, "FILL IN THE BLANKS:", 'F2', 14, 0.15)
        y -= 25
        # Create blanked version
        blank_words = words[:]
        blank_positions = random.sample(range(len(blank_words)), min(len(blank_words)//3 + 1, len(blank_words)))
        blanked = []
        for j, w in enumerate(blank_words):
            if j in blank_positions:
                blanked.append("_" * len(w))
            else:
                blanked.append(w)
        blank_text = " ".join(blanked)
        blines = []
        cur = ""
        for w in blank_text.split():
            if len(cur + " " + w) > 45:
                blines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            blines.append(cur)
        for ln in blines:
            doc.add_text(90, y, ln, 'F4', 14, 0.2)
            y -= 24
        
        # First letter prompts
        y -= 20
        doc.add_text(72, y, "FIRST LETTER PROMPTS:", 'F2', 14, 0.15)
        y -= 25
        first_letters = " ".join([w[0].upper() + "___" for w in words])
        fl_lines = []
        cur = ""
        for w in first_letters.split():
            if len(cur + " " + w) > 50:
                fl_lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            fl_lines.append(cur)
        for ln in fl_lines:
            doc.add_text(90, y, ln, 'F3', 14, 0.3)
            y -= 24
        
        # Review reminder
        if i > 0:
            y -= 15
            doc.add_filled_rect(55, y-25, 502, 30, 0.88)
            doc.add_rect(55, y-25, 502, 30, 1, 0.4)
            prev_ref = verses[i-1][1]
            doc.add_text(70, y-10, f"REVIEW: Can you still recite last week's verse? ({prev_ref})", 'F1', 10, 0.3)

        # Practice page for this week
        if i % 4 == 0:  # Every 4 weeks, add a review/practice page
            doc.new_page()
            rfill = 0.91 + random.uniform(0, 0.04)
            doc.add_filled_rect(0, 0, 612, 792, rfill)
            doc.add_rect(40, 40, 532, 712, 2, 0.3)
            doc.add_centered_text(730, f"REVIEW: WEEKS {max(1,i-2)} to {i+1}", 'F2', 16, 0.1)
            ry = 695
            doc.add_text(72, ry, "Write each verse from memory:", 'F2', 14, 0.15)
            ry -= 30
            for rv_idx in range(max(0,i-2), i+1):
                doc.add_text(72, ry, f"{verses[rv_idx][1]}:", 'F2', 12, 0.2)
                ry -= 25
                for _ in range(2):
                    doc.add_line(72, ry, 540, ry, 0.5, 0.5)
                    ry -= 22
                ry -= 10
    
    # Final review page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "52-WEEK REVIEW CHECKLIST", 'F2', 16, 0.1)
    y = 700
    for i in range(26):
        w = i + 1
        doc.add_text(72, y, f"[ ] Week {w}: {verses[i][1]}", 'F1', 10, 0.3)
        doc.add_text(330, y, f"[ ] Week {w+26}: {verses[i+26][1]}", 'F1', 10, 0.3)
        y -= 22
    
    # Extra practice page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "MY FAVORITE VERSES TO REVIEW", 'F2', 16, 0.1)
    y = 695
    for _ in range(28):
        doc.add_line(72, y, 540, y, 0.5, 0.6)
        y -= 22

    # Notes page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "MEMORY JOURNEY NOTES", 'F2', 16, 0.1)
    y = 695
    for _ in range(28):
        doc.add_line(72, y, 540, y, 0.5, 0.6)
        y -= 22
    
    # Certificate
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(50, 100, 512, 600, 3, 0.2)
    doc.add_rect(60, 110, 492, 580, 1, 0.4)
    doc.add_centered_text(630, "CERTIFICATE OF COMPLETION", 'F2', 20, 0.1)
    doc.add_centered_text(580, "This certifies that", 'F4', 16, 0.3)
    doc.add_line(180, 550, 432, 550, 1, 0.3)
    doc.add_centered_text(530, "has memorized 52 Scripture verses", 'F4', 16, 0.3)
    doc.add_centered_text(500, "over the course of one year!", 'F4', 16, 0.3)
    doc.add_centered_text(440, "\"Thy word have I hid in mine heart.\"", 'F5', 14, 0.2)
    doc.add_centered_text(415, "- Psalm 119:11", 'F4', 12, 0.3)
    doc.add_text(150, 250, "Date: _______________", 'F1', 14, 0.3)
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book292_Scripture_Memory_Seniors.pdf')
    print("Book292_Scripture_Memory_Seniors.pdf created successfully!")

if __name__ == "__main__":
    create_book()
