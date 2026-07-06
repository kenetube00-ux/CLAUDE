"""
Cover 3: The Nurse's Guided Journal
KDP Cover - 6x9 (432x648 points) - Clean, professional
"""
import sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def create_cover():
    pdf = PDFDoc(432, 648)
    pdf.new_page()

    # Light gray header band
    pdf.add_filled_rect(0, 545, 432, 103, gray=0.88)

    # Title
    pdf.add_text(155, 618, "THE", font='F1', size=14)
    pdf.add_centered_text(580, "NURSE'S", font='F2', size=36)
    pdf.add_centered_text(548, "GUIDED JOURNAL", font='F2', size=22)

    # Subtitle
    pdf.add_centered_text(510, "Reflections, Gratitude & Self-Care", font='F1', size=14)
    pdf.add_centered_text(488, "for Healthcare Heroes", font='F1', size=14)

    # Decorative line
    pdf.add_line(100, 470, 332, 470, 1.5)

    # Stethoscope icon
    pdf.add_line(195, 420, 200, 390, 1.5)
    pdf.add_line(237, 420, 232, 390, 1.5)
    pdf.add_line(200, 390, 210, 375, 1.5)
    pdf.add_line(232, 390, 222, 375, 1.5)
    pdf.add_line(210, 375, 216, 370, 1.5)
    pdf.add_line(222, 375, 216, 370, 1.5)
    pdf.add_line(216, 370, 216, 290, 2)
    # Chest piece
    pdf.add_rect(200, 270, 32, 25, line_width=2)

    # Heart shape
    pdf.add_line(216, 255, 205, 265, 1.5)
    pdf.add_line(205, 265, 210, 270, 1.5)
    pdf.add_line(210, 270, 216, 260, 1.5)
    pdf.add_line(216, 255, 227, 265, 1.5)
    pdf.add_line(227, 265, 222, 270, 1.5)
    pdf.add_line(222, 270, 216, 260, 1.5)

    # Feature bullets
    features = [
        "Daily Reflection Prompts",
        "Gratitude & Affirmation Pages",
        "Self-Care Wellness Tracker",
        "120 Pages of Guided Journaling",
    ]
    y = 220
    for feat in features:
        pdf.add_centered_text(y, f"* {feat}", font='F1', size=11)
        y -= 20

    # Bottom quote
    pdf.add_rect(80, 120, 272, 25, line_width=1)
    pdf.add_centered_text(128, "Because you deserve care too.", font='F2', size=12)

    # Author
    pdf.add_centered_text(80, "Daniel Tesfamariam", font='F2', size=18)

    # Bottom accent
    pdf.add_filled_rect(0, 0, 432, 35, gray=0.88)
    pdf.add_centered_text(12, "A Gift for Every Nurse", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover3_Nurse_Guided_Journal.pdf')
    print("Cover 3 created: Cover3_Nurse_Guided_Journal.pdf")

if __name__ == '__main__':
    create_cover()
