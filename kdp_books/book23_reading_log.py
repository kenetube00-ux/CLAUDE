"""
Book 23: MY READING LOG - A Book Lover's Journal
KDP Interior - 6x9 inches (432x648 points)
Title page + copyright + 50 book log entries + 3 "Books to Read Next" pages
"""
from pdf_utils import PDFDoc

def create_reading_log():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "MY READING LOG", font='F2', size=26)
    pdf.add_line(100, 510, 332, 510, 2)
    pdf.add_centered_text(480, "A Book Lover's Journal", font='F4', size=14)
    pdf.add_centered_text(410, "Track the books you read", font='F1', size=11)
    pdf.add_centered_text(388, "Record your thoughts & ratings", font='F1', size=11)
    pdf.add_centered_text(366, "Build your personal library list", font='F1', size=11)
    pdf.add_centered_text(270, "By", font='F1', size=11)
    pdf.add_centered_text(248, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "MY READING LOG", font='F2', size=12)
    pdf.add_centered_text(498, "A Book Lover's Journal", font='F1', size=10)
    pdf.add_centered_text(470, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(435, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(415, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(395, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(360, "Happy reading!", font='F4', size=10)

    # --- 50 BOOK LOG ENTRIES ---
    for entry in range(1, 51):
        pdf.new_page()
        pdf.add_text(60, 615, f"BOOK #{entry}", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 580
        # Title
        pdf.add_text(60, y, "Title:", font='F2', size=10)
        pdf.add_line(95, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 24

        # Author
        pdf.add_text(60, y, "Author:", font='F2', size=10)
        pdf.add_line(105, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 24

        # Dates
        pdf.add_text(60, y, "Date Started:", font='F2', size=10)
        pdf.add_line(138, y - 2, 220, y - 2, 0.3, gray=0.5)
        pdf.add_text(230, y, "Date Finished:", font='F2', size=10)
        pdf.add_line(315, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 24

        # Pages & Genre
        pdf.add_text(60, y, "Pages:", font='F2', size=10)
        pdf.add_line(98, y - 2, 160, y - 2, 0.3, gray=0.5)
        pdf.add_text(175, y, "Genre:", font='F2', size=10)
        pdf.add_line(213, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 24

        # Rating
        pdf.add_text(60, y, "Rating (1-5):", font='F2', size=10)
        for i in range(5):
            pdf.add_text(145 + i * 20, y, "*", font='F1', size=14)
        y -= 28

        # Favorite Quote
        pdf.add_text(60, y, "Favorite Quote:", font='F2', size=10)
        y -= 16
        pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
        y -= 24

        # Key Takeaways
        pdf.add_text(60, y, "Key Takeaways:", font='F2', size=10)
        y -= 16
        for i in range(3):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 18
        y -= 8

        # Review
        pdf.add_text(60, y, "Review:", font='F2', size=10)
        y -= 16
        for i in range(5):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 18
        y -= 8

        # Would recommend to
        pdf.add_text(60, y, "Would recommend to:", font='F2', size=10)
        pdf.add_line(175, y - 2, 372, y - 2, 0.3, gray=0.5)

        # Page number
        pdf.add_centered_text(30, f"- {entry + 2} -", font='F1', size=8)

    # --- 3 "BOOKS TO READ NEXT" PAGES ---
    for page in range(3):
        pdf.new_page()
        pdf.add_text(60, 615, "BOOKS TO READ NEXT", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 580
        start_num = page * 17 + 1
        for i in range(17):
            num = start_num + i
            pdf.add_text(60, y, f"{num}.", font='F2', size=9)
            pdf.add_line(80, y - 2, 280, y - 2, 0.3, gray=0.5)
            pdf.add_text(290, y, "by", font='F1', size=9)
            pdf.add_line(305, y - 2, 372, y - 2, 0.3, gray=0.5)
            y -= 30

        pdf.add_centered_text(30, f"- {53 + page} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book23_Reading_Log.pdf')
    print("Book 23 created: Book23_Reading_Log.pdf")

if __name__ == '__main__':
    create_reading_log()
