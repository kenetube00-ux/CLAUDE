"""
Cover 1: Large Print Kakuro Puzzle Book for Seniors
KDP Cover - 8.5x11 inches with bleed = 8.75x11.25 (630x810 points)
Front cover only
"""
import sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def create_cover():
    # 8.75 x 11.25 inches with bleed (630 x 810 points)
    pdf = PDFDoc(630, 810)
    pdf.new_page()

    # === BACKGROUND ===
    # Dark navy/blue-gray background
    pdf.add_filled_rect(0, 0, 630, 810, gray=0.15)

    # === DECORATIVE BORDER ===
    # Outer gold-like border (lighter gray to simulate)
    pdf.set_gray(0.7)
    pdf.add_rect(25, 25, 580, 760, line_width=3)
    pdf.add_rect(30, 30, 570, 750, line_width=1)
    pdf.reset_color()

    # === TOP BANNER ===
    pdf.add_filled_rect(40, 700, 550, 60, gray=0.85)
    pdf.set_gray(0.1)
    pdf.add_text(180, 720, "LARGE PRINT EDITION", font='HelveticaBold', size=22)
    pdf.reset_color()

    # === MAIN TITLE ===
    pdf.set_gray(1)
    pdf.add_text(155, 640, "KAKURO", font='HelveticaBold', size=60)
    pdf.add_text(105, 585, "PUZZLE BOOK", font='HelveticaBold', size=42)
    pdf.reset_color()

    # === SUBTITLE ===
    pdf.set_gray(0.8)
    pdf.add_text(200, 545, "For Seniors", font='Helvetica', size=24)
    pdf.reset_color()

    # === DECORATIVE LINE ===
    pdf.set_gray(0.7)
    pdf.add_line(100, 525, 530, 525, 2)
    pdf.reset_color()

    # === SAMPLE PUZZLE GRID (visual element) ===
    grid_x, grid_y = 165, 250
    cell = 50
    grid_size = 5

    for row in range(grid_size):
        for col in range(grid_size):
            x = grid_x + col * cell
            y = grid_y + row * cell

            if (row + col) % 3 == 0:
                # Dark cells (clue cells)
                pdf.add_filled_rect(x, y, cell, cell, gray=0.35)
                pdf.set_gray(0.9)
                pdf.add_text(x + 5, y + cell - 15, "12", font='Helvetica', size=10)
                pdf.add_text(x + cell - 18, y + 3, "8", font='Helvetica', size=10)
                pdf.reset_color()
                # Diagonal
                pdf.set_gray(0.6)
                pdf.add_line(x, y + cell, x + cell, y, 0.5)
                pdf.reset_color()
            else:
                # White cells
                pdf.set_gray(0.95)
                pdf.add_filled_rect(x, y, cell, cell, gray=0.95)
                pdf.reset_color()
                pdf.set_gray(0.4)
                pdf.add_rect(x, y, cell, cell, line_width=0.8)
                pdf.reset_color()

    # === FEATURES BOX ===
    pdf.add_filled_rect(100, 160, 430, 70, gray=0.25)
    pdf.set_gray(0.9)
    pdf.add_text(120, 205, "100+ Puzzles | Bold & Easy | Big Grids", font='Helvetica', size=14)
    pdf.add_text(140, 178, "Clear Numbers | Senior-Friendly Format", font='Helvetica', size=14)
    pdf.reset_color()

    # === VOLUME ===
    pdf.set_gray(0.7)
    pdf.add_text(275, 130, "Volume 1", font='Helvetica', size=16)
    pdf.reset_color()

    # === AUTHOR NAME ===
    pdf.set_gray(1)
    pdf.add_text(185, 70, "Daniel Tesfamariam", font='HelveticaBold', size=20)
    pdf.reset_color()

    # === BOTTOM DECORATIVE LINE ===
    pdf.set_gray(0.7)
    pdf.add_line(100, 100, 530, 100, 1)
    pdf.reset_color()

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover1_Kakuro_Puzzle_Book.pdf')
    print("Cover 1 created: Cover1_Kakuro_Puzzle_Book.pdf")

if __name__ == '__main__':
    create_cover()
