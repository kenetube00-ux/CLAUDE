"""
Book 18: MY PREGNANCY JOURNAL - Week by Week
KDP Interior - 6x9 inches (432x648 points)
40 weekly pages tracking pregnancy journey
"""
from pdf_utils import PDFDoc

def create_pregnancy_journal():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "MY", font='F2', size=18)
    pdf.add_centered_text(495, "PREGNANCY", font='F2', size=28)
    pdf.add_centered_text(458, "JOURNAL", font='F2', size=28)
    pdf.add_line(100, 438, 332, 438, 2)
    pdf.add_centered_text(408, "Week by Week", font='F4', size=16)
    pdf.add_centered_text(375, "How I Feel | Baby Size | Symptoms | Cravings", font='F1', size=10)
    pdf.add_centered_text(353, "Doctor Visits | Weight | Questions | Memories", font='F1', size=10)
    pdf.add_centered_text(270, "By", font='F1', size=11)
    pdf.add_centered_text(248, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(180, "Baby's Name: ________________________", font='F1', size=12)
    pdf.add_centered_text(155, "Due Date: ___/___/______", font='F1', size=12)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(520, "My Pregnancy Journal - Week by Week", font='F2', size=12)
    pdf.add_centered_text(495, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(435, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(410, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(370, "Congratulations on your journey to motherhood!", font='F4', size=11)

    # --- 40 WEEKLY PAGES ---
    for week in range(1, 41):
        pdf.new_page()
        pdf.add_text(60, 615, f"WEEK {week}", font='F2', size=16)
        pdf.add_text(250, 615, "Date: ___/___/______", font='F1', size=10)
        pdf.add_line(60, 600, 372, 600, 0.8)

        y = 575

        # How I Feel
        pdf.add_text(60, y, "How I Feel:", font='F2', size=10)
        pdf.add_line(135, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 20
        pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
        y -= 25

        # Baby Size This Week
        pdf.add_text(60, y, "Baby Size This Week:", font='F2', size=10)
        pdf.add_line(185, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 25

        # Symptoms
        pdf.add_text(60, y, "Symptoms:", font='F2', size=10)
        pdf.add_line(125, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 20
        pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
        y -= 25

        # Cravings
        pdf.add_text(60, y, "Cravings:", font='F2', size=10)
        pdf.add_line(115, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 25

        # Doctor Visit Notes
        pdf.add_text(60, y, "Doctor Visit Notes:", font='F2', size=10)
        y -= 18
        for i in range(3):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 20
        y -= 5

        # Weight
        pdf.add_text(60, y, "Weight:", font='F2', size=10)
        pdf.add_line(105, y - 2, 180, y - 2, 0.3, gray=0.5)
        pdf.add_text(200, y, "Blood Pressure:", font='F2', size=10)
        pdf.add_line(290, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 25

        # Questions for Doctor
        pdf.add_text(60, y, "Questions for Doctor:", font='F2', size=10)
        y -= 18
        for i in range(2):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 20
        y -= 5

        # Photo/Belly Measurement Section
        pdf.add_text(60, y, "BELLY MEASUREMENT:", font='F2', size=10)
        pdf.add_line(195, y - 2, 290, y - 2, 0.3, gray=0.5)
        y -= 25
        pdf.add_text(60, y, "Photo/Memory:", font='F2', size=10)
        y -= 10
        pdf.add_rect(60, y - 80, 312, 80, 0.5)
        pdf.add_centered_text(y - 40, "Attach photo or sketch here", font='F1', size=9, gray=0.5)

        # Page number
        pdf.add_centered_text(30, f"- {week + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book18_Pregnancy_Journal.pdf')
    print("Book 18 created: Book18_Pregnancy_Journal.pdf")

if __name__ == '__main__':
    create_pregnancy_journal()
