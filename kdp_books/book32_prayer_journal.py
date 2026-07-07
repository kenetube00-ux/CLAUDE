"""
Book 32: My Daily Prayer Journal - 90 Days of Faith & Gratitude
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(540, "MY DAILY", font='F2', size=24)
    pdf.add_centered_text(500, "PRAYER JOURNAL", font='F2', size=28)
    pdf.add_line(100, 480, 332, 480, 2)
    pdf.add_centered_text(450, "90 Days of Faith & Gratitude", font='F4', size=16)
    pdf.add_centered_text(415, "A Guided Devotional for Daily", font='F1', size=12)
    pdf.add_centered_text(395, "Prayer, Scripture & Reflection", font='F1', size=12)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(235, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(150, "This journal belongs to:", font='F4', size=12)
    pdf.add_centered_text(125, "________________________", font='F1', size=12)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "My Daily Prayer Journal", font='F2', size=14)
    pdf.add_centered_text(475, "90 Days of Faith & Gratitude", font='F1', size=11)
    pdf.add_centered_text(450, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(420, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(395, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(370, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(330, "\"Be joyful in hope, patient in affliction,", font='F4', size=10)
    pdf.add_centered_text(315, "faithful in prayer.\" - Romans 12:12", font='F4', size=10)

    # --- 90 DAILY PAGES ---
    for day in range(1, 91):
        pdf.new_page()
        pdf.add_text(60, 615, f"Day {day}", font='F2', size=14)
        pdf.add_text(280, 615, "Date: ___/___/______", font='F1', size=10)
        pdf.add_line(60, 605, 372, 605, 1)

        y = 580
        # Today I pray for
        pdf.add_text(60, y, "Today I pray for:", font='F5', size=11)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 28

        # Scripture/Verse of the day
        pdf.add_text(60, y, "Scripture / Verse of the Day:", font='F5', size=11)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 28

        # What God is teaching me
        pdf.add_text(60, y, "What God is teaching me:", font='F5', size=11)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 28

        # I am thankful for
        pdf.add_text(60, y, "I am thankful for:", font='F5', size=11)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 28

        # Prayer answered
        pdf.add_text(60, y, "Prayer answered:", font='F5', size=11)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 28

        # Evening reflection
        pdf.add_text(60, y, "Evening Reflection:", font='F5', size=11)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)

        pdf.add_centered_text(35, f"- {day + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book32_Prayer_Journal.pdf')
    print("Book 32 created: Book32_Prayer_Journal.pdf")

if __name__ == '__main__':
    create_book()
