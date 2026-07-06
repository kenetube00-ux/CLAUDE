"""
Book 19: THE 5-MINUTE JOURNAL FOR MEN
KDP Interior - 6x9 inches (432x648 points)
90 daily pages with morning and evening gratitude prompts
"""
from pdf_utils import PDFDoc

def create_gratitude_journal_men():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "THE", font='F2', size=16)
    pdf.add_centered_text(495, "5-MINUTE JOURNAL", font='F2', size=26)
    pdf.add_centered_text(458, "FOR MEN", font='F2', size=22)
    pdf.add_line(100, 438, 332, 438, 2)
    pdf.add_centered_text(405, "Daily Gratitude & Reflection", font='F1', size=13)
    pdf.add_centered_text(380, "90 Days to a Better Mindset", font='F1', size=12)
    pdf.add_centered_text(345, "Morning Intentions | Evening Reflections", font='F1', size=11)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(238, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(520, "The 5-Minute Journal for Men", font='F2', size=12)
    pdf.add_centered_text(495, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(435, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(410, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(370, "Five minutes a day. Real results. No fluff.", font='F1', size=10)

    # --- 90 DAILY PAGES ---
    for day in range(1, 91):
        pdf.new_page()
        pdf.add_text(60, 615, f"DAY {day}", font='F2', size=14)
        pdf.add_text(280, 615, "Date: ___/___/______", font='F1', size=10)
        pdf.add_line(60, 600, 372, 600, 0.8)

        y = 575

        # === MORNING SECTION ===
        pdf.add_text(60, y, "MORNING", font='F2', size=11)
        pdf.add_line(60, y - 5, 115, y - 5, 0.5)
        y -= 25

        # I am grateful for (3 lines)
        pdf.add_text(60, y, "I am grateful for:", font='F4', size=10)
        y -= 18
        for i in range(1, 4):
            pdf.add_text(65, y, f"{i}.", font='F1', size=9)
            pdf.add_line(78, y - 2, 372, y - 2, 0.3, gray=0.5)
            y -= 20
        y -= 8

        # What would make today great (2 lines)
        pdf.add_text(60, y, "What would make today great:", font='F4', size=10)
        y -= 18
        for i in range(1, 3):
            pdf.add_text(65, y, f"{i}.", font='F1', size=9)
            pdf.add_line(78, y - 2, 372, y - 2, 0.3, gray=0.5)
            y -= 20
        y -= 8

        # Daily affirmation
        pdf.add_text(60, y, "Daily affirmation:", font='F4', size=10)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
        y -= 35

        # === EVENING SECTION ===
        pdf.add_text(60, y, "EVENING", font='F2', size=11)
        pdf.add_line(60, y - 5, 118, y - 5, 0.5)
        y -= 25

        # 3 amazing things that happened (3 lines)
        pdf.add_text(60, y, "3 amazing things that happened:", font='F4', size=10)
        y -= 18
        for i in range(1, 4):
            pdf.add_text(65, y, f"{i}.", font='F1', size=9)
            pdf.add_line(78, y - 2, 372, y - 2, 0.3, gray=0.5)
            y -= 20
        y -= 8

        # How could I have made today better (2 lines)
        pdf.add_text(60, y, "How could I have made today better:", font='F4', size=10)
        y -= 18
        for i in range(1, 3):
            pdf.add_text(65, y, f"{i}.", font='F1', size=9)
            pdf.add_line(78, y - 2, 372, y - 2, 0.3, gray=0.5)
            y -= 20

        # Page number
        pdf.add_centered_text(30, f"- {day + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book19_Gratitude_Journal_Men.pdf')
    print("Book 19 created: Book19_Gratitude_Journal_Men.pdf")

if __name__ == '__main__':
    create_gratitude_journal_men()
