"""
Cover 1: Large Print Kakuro Puzzle Book for Seniors
KDP Cover - 8.5x11 (612x792 points) - White background with accent elements
"""
import sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def create_cover():
    pdf = PDFDoc(612, 792)
    pdf.new_page()

    # White background (default) with decorative border
    pdf.add_rect(20, 20, 572, 752, line_width=3)
    pdf.add_rect(25, 25, 562, 742, line_width=1)

    # Top accent bar
    pdf.add_filled_rect(40, 700, 532, 45, gray=0.85)
    pdf.add_text(175, 715, "LARGE PRINT EDITION", font='HelveticaBold', size=20)

    # Main title
    pdf.add_centered_text(640, "KAKURO", font='HelveticaBold', size=56)
    pdf.add_centered_text(585, "PUZZLE BOOK", font='HelveticaBold', size=38)
    pdf.add_centered_text(535, "For Seniors", font='Helvetica', size=22)

    # Decorative line
    pdf.add_line(100, 515, 512, 515, 2)

    # Sample puzzle grid
    grid_x, grid_y = 180, 260
    cell = 48
    for row in range(5):
        for col in range(5):
            x = grid_x + col * cell
            y = grid_y + row * cell
            if (row + col) % 3 == 0:
                pdf.add_filled_rect(x, y, cell, cell, gray=0.3)
                pdf.add_text(x + 5, y + cell - 14, "12", font='Helvetica', size=9, gray=1)
                pdf.add_line(x, y + cell, x + cell, y, 0.5, gray=0.7)
            else:
                pdf.add_rect(x, y, cell, cell, line_width=0.8)

    # Features
    pdf.add_centered_text(230, "100+ Puzzles | Bold & Easy | Big Grids", font='Helvetica', size=13)
    pdf.add_centered_text(205, "Clear Numbers | Senior-Friendly Format", font='Helvetica', size=13)

    # Volume
    pdf.add_centered_text(160, "Volume 1", font='Helvetica', size=14)

    # Author
    pdf.add_line(180, 110, 432, 110, 1)
    pdf.add_centered_text(80, "Daniel Tesfamariam", font='HelveticaBold', size=20)

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover1_Kakuro_Puzzle_Book.pdf')
    print("Cover 1 created: Cover1_Kakuro_Puzzle_Book.pdf")

if __name__ == '__main__':
    create_cover()
