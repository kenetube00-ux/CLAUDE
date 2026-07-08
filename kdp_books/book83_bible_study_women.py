"""Book 83: Bible Study Workbook for Women - Proverbs 31"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Proverbs 31 verses (10-31) for 12 weeks
    verses = [
        ("Week 1: Proverbs 31:10", "A wife of noble character who can find? She is worth far more than rubies."),
        ("Week 2: Proverbs 31:13-14", "She selects wool and flax and works with eager hands. She is like the merchant ships, bringing her food from afar."),
        ("Week 3: Proverbs 31:15-16", "She gets up while it is still night; she provides food for her family. She considers a field and buys it; out of her earnings she plants a vineyard."),
        ("Week 4: Proverbs 31:17-18", "She sets about her work vigorously; her arms are strong for her tasks. She sees that her trading is profitable."),
        ("Week 5: Proverbs 31:20", "She opens her arms to the poor and extends her hands to the needy."),
        ("Week 6: Proverbs 31:21-22", "She has no fear for her household; for all of them are clothed in scarlet. She makes coverings for her bed; she is clothed in fine linen and purple."),
        ("Week 7: Proverbs 31:23-24", "Her husband is respected at the city gate. She makes linen garments and sells them, and supplies the merchants with sashes."),
        ("Week 8: Proverbs 31:25", "She is clothed with strength and dignity; she can laugh at the days to come."),
        ("Week 9: Proverbs 31:26", "She speaks with wisdom, and faithful instruction is on her tongue."),
        ("Week 10: Proverbs 31:27", "She watches over the affairs of her household and does not eat the bread of idleness."),
        ("Week 11: Proverbs 31:28-29", "Her children arise and call her blessed; her husband also, and he praises her: Many women do noble things, but you surpass them all."),
        ("Week 12: Proverbs 31:30-31", "Charm is deceptive, and beauty is fleeting; but a woman who fears the Lord is to be praised. Honor her for all that her hands have done."),
    ]
    
    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.1)
    pdf.add_centered_text(520, "SHE IS STRONG", 'F5', 30, 1)
    pdf.add_centered_text(475, "A Proverbs 31 Bible Study", 'F4', 18, 0.9)
    pdf.add_centered_text(448, "Workbook for Women", 'F4', 18, 0.9)
    pdf.add_centered_text(390, "12 Weeks of Scripture, Reflection & Growth", 'F1', 12, 0.8)
    pdf.add_centered_text(360, "Read - Observe - Interpret - Apply", 'F1', 11, 0.7)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "She Is Strong: A Proverbs 31 Bible Study Workbook for Women", 'F2', 12)
    pdf.add_centered_text(475, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(450, "Scripture quotations are from the New International Version (NIV).", 'F1', 9)
    pdf.add_centered_text(430, "Holy Bible, New International Version. Copyright 1973, 1978, 1984, 2011", 'F1', 8)
    pdf.add_centered_text(415, "by Biblica, Inc. Used by permission. All rights reserved worldwide.", 'F1', 8)
    pdf.add_centered_text(380, "HOW TO USE THIS STUDY:", 'F2', 11)
    how_to = [
        "Each week focuses on a portion of Proverbs 31:10-31.",
        "Spend time reading the verse, then work through each section.",
        "This study works for individual or group settings.",
        "There are no wrong answers - let the Holy Spirit guide you.",
    ]
    y = 355
    for line in how_to:
        pdf.add_centered_text(y, line, 'F4', 10)
        y -= 18
    
    # 12 Weekly Study Pages
    for week_idx, (week_title, verse_text) in enumerate(verses):
        pdf.new_page()
        # Header
        pdf.add_filled_rect(50, 740, 512, 35, 0.88)
        pdf.add_text(60, 752, week_title, 'F2', 14)
        
        # Verse text
        pdf.add_text(60, 715, "SCRIPTURE:", 'F2', 10)
        # Split long verse text
        words = verse_text.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line + " " + word) > 75:
                lines.append(current_line)
                current_line = word
            else:
                current_line = current_line + " " + word if current_line else word
        if current_line:
            lines.append(current_line)
        
        y = 698
        for line in lines:
            pdf.add_text(72, y, line, 'F4', 10)
            y -= 14
        
        y -= 15
        # Read & Observe
        pdf.add_text(60, y, "READ & OBSERVE (What does the text say?)", 'F2', 11)
        y -= 18
        pdf.add_text(60, y, "What key words or phrases stand out to you?", 'F1', 9)
        y -= 15
        for i in range(3):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 20
        
        y -= 8
        # Interpret
        pdf.add_text(60, y, "INTERPRET (What does it mean?)", 'F2', 11)
        y -= 18
        pdf.add_text(60, y, "What was the original meaning? What does this reveal about God's design for women?", 'F1', 9)
        y -= 15
        for i in range(3):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 20
        
        y -= 8
        # Apply
        pdf.add_text(60, y, "APPLY (How does this apply to my life?)", 'F2', 11)
        y -= 18
        pdf.add_text(60, y, "What is one specific way you can live this out this week?", 'F1', 9)
        y -= 15
        for i in range(3):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 20
        
        y -= 8
        # Prayer prompt
        pdf.add_text(60, y, "PRAYER:", 'F2', 10)
        pdf.add_text(105, y, "Lord, help me to...", 'F4', 10)
        y -= 15
        for i in range(2):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 20
        
        y -= 8
        # Scripture memory
        pdf.add_text(60, y, "SCRIPTURE MEMORY (Copy the verse below):", 'F2', 10)
        y -= 15
        for i in range(2):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 20
        
        y -= 8
        # Reflection journal
        pdf.add_text(60, y, "REFLECTION JOURNAL:", 'F2', 10)
        y -= 15
        for i in range(6):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 8
        # Group discussion
        pdf.add_text(60, y, "GROUP DISCUSSION QUESTIONS:", 'F2', 10)
        y -= 15
        questions = [
            f"1. What aspect of this week's verse is most challenging for you?",
            f"2. How have you seen this quality in other women you admire?",
            f"3. What is one barrier to living this out, and how can the group support you?",
        ]
        for q in questions:
            pdf.add_text(72, y, q, 'F1', 9)
            y -= 15
        
        y -= 10
        # Action step
        pdf.add_text(60, y, "ACTION STEP FOR THE WEEK:", 'F2', 10)
        y -= 15
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 20
        
        # Weekly challenge
        pdf.add_text(60, y, "WEEKLY CHALLENGE:", 'F2', 10)
        pdf.add_line(180, y - 2, 540, y - 2, 0.5, 0.5)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book83_Bible_Study_Women.pdf')
    print("Book83_Bible_Study_Women.pdf created successfully!")

if __name__ == "__main__":
    create_book()
