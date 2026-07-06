"""
Book 27: WINE TASTING JOURNAL
KDP Interior - 6x9 inches (432x648 points)
Title page + copyright + 50 wine log entries
"""
from pdf_utils import PDFDoc

def create_wine_tasting_journal():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "WINE TASTING", font='F2', size=28)
    pdf.add_centered_text(495, "JOURNAL", font='F2', size=28)
    pdf.add_line(100, 475, 332, 475, 2)
    pdf.add_centered_text(445, "A Connoisseur's Log Book", font='F4', size=14)
    pdf.add_centered_text(390, "50 Detailed Wine Entries", font='F1', size=11)
    pdf.add_centered_text(368, "Aroma | Taste | Body | Rating", font='F1', size=11)
    pdf.add_centered_text(346, "Food Pairings & Tasting Notes", font='F1', size=11)
    pdf.add_centered_text(270, "By", font='F1', size=11)
    pdf.add_centered_text(248, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "WINE TASTING JOURNAL", font='F2', size=12)
    pdf.add_centered_text(498, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(440, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(420, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(385, "Cheers to great wine!", font='F4', size=10)

    # --- 50 WINE LOG ENTRIES ---
    for entry in range(1, 51):
        pdf.new_page()
        pdf.add_text(60, 615, f"WINE #{entry}", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 580

        # Wine Name
        pdf.add_text(60, y, "Wine Name:", font='F2', size=10)
        pdf.add_line(128, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Winery/Region
        pdf.add_text(60, y, "Winery/Region:", font='F2', size=10)
        pdf.add_line(148, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Vintage Year
        pdf.add_text(60, y, "Vintage Year:", font='F2', size=10)
        pdf.add_line(140, y - 2, 220, y - 2, 0.3, gray=0.5)
        # Grape/Varietal
        pdf.add_text(235, y, "Grape/Varietal:", font='F2', size=10)
        pdf.add_line(320, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Color
        pdf.add_text(60, y, "Color:", font='F2', size=10)
        pdf.add_line(98, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Aroma
        pdf.add_text(60, y, "Aroma:", font='F2', size=10)
        pdf.add_line(102, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Taste
        pdf.add_text(60, y, "Taste:", font='F2', size=10)
        pdf.add_line(95, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Finish
        pdf.add_text(60, y, "Finish:", font='F2', size=10)
        pdf.add_line(100, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Body & Acidity
        pdf.add_text(60, y, "Body:", font='F2', size=10)
        pdf.add_line(93, y - 2, 200, y - 2, 0.3, gray=0.5)
        pdf.add_text(215, y, "Acidity:", font='F2', size=10)
        pdf.add_line(262, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Tannins
        pdf.add_text(60, y, "Tannins:", font='F2', size=10)
        pdf.add_line(110, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Rating
        pdf.add_text(60, y, "Rating (1-5):", font='F2', size=10)
        for i in range(5):
            pdf.add_text(145 + i * 20, y, "*", font='F1', size=14)
        y -= 22

        # Price
        pdf.add_text(60, y, "Price: $", font='F2', size=10)
        pdf.add_line(108, y - 2, 200, y - 2, 0.3, gray=0.5)
        pdf.add_text(215, y, "Occasion:", font='F2', size=10)
        pdf.add_line(272, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Food pairing
        pdf.add_text(60, y, "Food Pairing:", font='F2', size=10)
        pdf.add_line(138, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Would buy again
        pdf.add_text(60, y, "Would Buy Again:", font='F2', size=10)
        pdf.add_text(165, y, "Y  /  N", font='F1', size=10)
        y -= 24

        # Notes
        pdf.add_text(60, y, "Notes:", font='F2', size=10)
        y -= 16
        for i in range(3):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 18

        # Page number
        pdf.add_centered_text(30, f"- {entry + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book27_Wine_Tasting_Journal.pdf')
    print("Book 27 created: Book27_Wine_Tasting_Journal.pdf")

if __name__ == '__main__':
    create_wine_tasting_journal()
