"""Book 88: Christian Grief Journal for Loss of a Spouse"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"
    
    # 30 comfort scriptures
    scriptures = [
        "Psalm 34:18 - The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
        "Isaiah 41:10 - Fear not, for I am with you; be not dismayed, for I am your God.",
        "Psalm 147:3 - He heals the brokenhearted and binds up their wounds.",
        "Matthew 5:4 - Blessed are those who mourn, for they will be comforted.",
        "Psalm 23:4 - Even though I walk through the valley of the shadow of death, I will fear no evil.",
        "2 Corinthians 1:3-4 - The God of all comfort, who comforts us in all our troubles.",
        "Revelation 21:4 - He will wipe every tear from their eyes. There will be no more death.",
        "Romans 8:28 - All things work together for good to those who love God.",
        "Psalm 46:1 - God is our refuge and strength, an ever-present help in trouble.",
        "Isaiah 43:2 - When you pass through the waters, I will be with you.",
        "John 14:27 - Peace I leave with you; my peace I give you.",
        "Psalm 73:26 - My flesh and heart may fail, but God is the strength of my heart.",
        "Deuteronomy 31:8 - The Lord himself goes before you and will never leave you.",
        "Psalm 116:15 - Precious in the sight of the Lord is the death of his faithful servants.",
        "1 Thessalonians 4:13 - We do not grieve as those who have no hope.",
        "Psalm 30:5 - Weeping may stay for the night, but rejoicing comes in the morning.",
        "Isaiah 57:1-2 - The righteous are taken away to be spared from evil; they enter into peace.",
        "Romans 8:38-39 - Nothing can separate us from the love of God.",
        "Psalm 56:8 - You have kept count of my tossings; put my tears in your bottle.",
        "John 11:25 - I am the resurrection and the life. The one who believes in me will live.",
        "Psalm 62:1-2 - Truly my soul finds rest in God; my salvation comes from him.",
        "Lamentations 3:22-23 - His mercies are new every morning; great is your faithfulness.",
        "Philippians 4:7 - The peace of God, which transcends all understanding, will guard your hearts.",
        "Psalm 121:1-2 - I lift up my eyes to the mountains; my help comes from the Lord.",
        "2 Samuel 12:23 - I will go to him, but he will not return to me.",
        "Isaiah 40:31 - Those who hope in the Lord will renew their strength.",
        "Psalm 139:16 - All the days ordained for me were written in your book.",
        "John 16:22 - Now is your time of grief, but I will see you again and your heart will rejoice.",
        "Nahum 1:7 - The Lord is good, a refuge in times of trouble.",
        "Psalm 91:4 - He will cover you with his feathers; under his wings you will find refuge.",
    ]
    
    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.08)
    pdf.add_centered_text(420, "THROUGH THE VALLEY", 'F5', 22, 1)
    pdf.add_centered_text(380, "A Christian Grief Journal", 'F4', 14, 0.9)
    pdf.add_centered_text(358, "for Loss of a Spouse", 'F4', 14, 0.9)

    pdf.add_centered_text(310, "90 Days of Scripture, Prayer & Reflection", 'F1', 10, 0.8)
    pdf.add_centered_text(290, "For those walking through grief with faith", 'F1', 10, 0.7)
    pdf.add_centered_text(180, author, 'F2', 12, 0.9)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(430, "Through the Valley", 'F2', 12)
    pdf.add_centered_text(410, "A Christian Grief Journal for Loss of a Spouse", 'F4', 10)
    pdf.add_centered_text(380, f"Copyright 2024 {author}. All rights reserved.", 'F1', 9)
    pdf.add_centered_text(360, "No part of this book may be reproduced without permission.", 'F1', 8)
    pdf.add_centered_text(330, "Scripture quotations are from the NIV unless otherwise noted.", 'F1', 8)
    pdf.add_centered_text(295, "Dear friend,", 'F4', 10)
    pdf.add_centered_text(275, "I am so sorry for your loss. There are no words adequate", 'F4', 9)
    pdf.add_centered_text(260, "for the pain of losing your life partner. This journal is a", 'F4', 9)
    pdf.add_centered_text(245, "companion for your journey - not a fix, but a faithful friend.", 'F4', 9)
    pdf.add_centered_text(225, "There is no timeline for grief. Use these pages however", 'F4', 9)
    pdf.add_centered_text(210, "you need them. God is with you in this valley.", 'F4', 9)
    pdf.add_centered_text(180, "With love and prayers,", 'F4', 9)
    pdf.add_centered_text(165, author, 'F4', 9)

    # 90 Daily Pages
    for day in range(1, 91):
        pdf.new_page()
        scripture_idx = (day - 1) % 30
        verse = scriptures[scripture_idx]
        
        # Header
        pdf.add_filled_rect(25, 608, 382, 22, 0.9)
        pdf.add_text(32, 614, f"DAY {day}", 'F2', 11)
        pdf.add_text(250, 614, "Date: ___/___/______", 'F1', 8)
        
        # How I feel
        pdf.add_text(32, 590, "Today I feel (1-10):", 'F2', 9)
        pdf.add_text(160, 590, "1  2  3  4  5  6  7  8  9  10", 'F3', 8)
        
        # Scripture
        pdf.add_text(32, 568, "Scripture for today:", 'F2', 8)
        # Word-wrap the scripture
        words = verse.split()
        lines = []
        current = ""
        for w in words:
            if len(current + " " + w) > 58:
                lines.append(current)
                current = w
            else:
                current = current + " " + w if current else w
        if current:
            lines.append(current)
        y = 554
        for line in lines:
            pdf.add_text(32, y, line, 'F4', 8)
            y -= 12
        
        y -= 8
        # Prayer
        pdf.add_text(32, y, "Lord, I bring before you:", 'F2', 8)
        y -= 14
        for _ in range(3):
            pdf.add_line(32, y, 400, y, 0.5, 0.5)
            y -= 14
        
        y -= 6
        # Memory
        pdf.add_text(32, y, "A memory I want to hold onto:", 'F2', 8)
        y -= 14
        for _ in range(3):
            pdf.add_line(32, y, 400, y, 0.5, 0.5)
            y -= 14
        
        y -= 6
        # What is hardest
        pdf.add_text(32, y, "What is hardest today:", 'F2', 8)
        y -= 14
        for _ in range(2):
            pdf.add_line(32, y, 400, y, 0.5, 0.5)
            y -= 14
        
        y -= 6
        # God's grace
        pdf.add_text(32, y, "Where I saw God's grace:", 'F2', 8)
        y -= 14
        for _ in range(2):
            pdf.add_line(32, y, 400, y, 0.5, 0.5)
            y -= 14
        
        y -= 6
        # Grateful
        pdf.add_text(32, y, "I am grateful for:", 'F2', 8)
        y -= 14
        pdf.add_text(32, y, "1.", 'F1', 8)
        pdf.add_line(45, y - 2, 400, y - 2, 0.5, 0.5)
        y -= 14
        pdf.add_text(32, y, "2.", 'F1', 8)
        pdf.add_line(45, y - 2, 400, y - 2, 0.5, 0.5)
        y -= 18
        
        # Evening prayer
        pdf.add_text(32, y, "Evening prayer:", 'F2', 8)
        pdf.add_line(115, y - 2, 400, y - 2, 0.5, 0.5)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book88_Christian_Grief_Spouse.pdf')
    print("Book88_Christian_Grief_Spouse.pdf created successfully!")

if __name__ == "__main__":
    create_book()
