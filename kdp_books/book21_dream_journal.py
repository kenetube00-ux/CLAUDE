"""
Book 21: DREAM JOURNAL - Capture & Interpret Your Dreams
KDP Interior - 6x9 inches (432x648 points)
Title page + copyright + 60 dream log pages
"""
from pdf_utils import PDFDoc

def create_dream_journal():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "DREAM JOURNAL", font='F2', size=28)
    pdf.add_line(100, 500, 332, 500, 2)
    pdf.add_centered_text(470, "Capture & Interpret Your Dreams", font='F4', size=14)
    pdf.add_centered_text(400, "Record your nightly adventures", font='F1', size=11)
    pdf.add_centered_text(378, "Discover patterns & symbols", font='F1', size=11)
    pdf.add_centered_text(356, "Unlock your subconscious mind", font='F1', size=11)
    pdf.add_centered_text(270, "By", font='F1', size=11)
    pdf.add_centered_text(248, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "DREAM JOURNAL", font='F2', size=12)
    pdf.add_centered_text(498, "Capture & Interpret Your Dreams", font='F1', size=10)
    pdf.add_centered_text(470, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(435, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(415, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(395, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(360, "Sweet dreams and deep insights!", font='F4', size=10)

    # --- 60 DREAM LOG PAGES ---
    for entry in range(1, 61):
        pdf.new_page()
        pdf.add_text(60, 615, f"DREAM #{entry}", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 580
        # Date
        pdf.add_text(60, y, "Date:", font='F2', size=10)
        pdf.add_line(95, y - 2, 220, y - 2, 0.3, gray=0.5)
        # Time woke up
        pdf.add_text(235, y, "Time Woke Up:", font='F2', size=10)
        pdf.add_line(318, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Dream title
        pdf.add_text(60, y, "Dream Title:", font='F2', size=10)
        pdf.add_line(130, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 30

        # Describe your dream
        pdf.add_text(60, y, "Describe your dream:", font='F2', size=10)
        y -= 18
        for i in range(8):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 20

        y -= 8
        # Emotions felt
        pdf.add_text(60, y, "Emotions Felt:", font='F2', size=10)
        pdf.add_line(140, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Recurring symbols
        pdf.add_text(60, y, "Recurring Symbols:", font='F2', size=10)
        pdf.add_line(160, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Possible meaning
        pdf.add_text(60, y, "Possible Meaning:", font='F2', size=10)
        y -= 18
        for i in range(3):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 20

        y -= 8
        # Lucidity level
        pdf.add_text(60, y, "Lucidity Level (1-5):", font='F2', size=10)
        pdf.add_text(185, y, "1", font='F1', size=10)
        pdf.add_text(210, y, "2", font='F1', size=10)
        pdf.add_text(235, y, "3", font='F1', size=10)
        pdf.add_text(260, y, "4", font='F1', size=10)
        pdf.add_text(285, y, "5", font='F1', size=10)
        for i in range(5):
            pdf.add_rect(183 + i * 25, y - 3, 10, 12, 0.4)

        # Page number
        pdf.add_centered_text(30, f"- {entry + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book21_Dream_Journal.pdf')
    print("Book 21 created: Book21_Dream_Journal.pdf")

if __name__ == '__main__':
    create_dream_journal()
