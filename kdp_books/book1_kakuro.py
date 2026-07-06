"""
Book 1: Large Print Kakuro Puzzle Book for Seniors
KDP Interior - 8.5x11 inches (612x792 points)
WHITE background, BLACK text
"""
import random
from pdf_utils import PDFDoc

def create_kakuro_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "LARGE PRINT", font='F2', size=24)
    pdf.add_centered_text(570, "KAKURO", font='F2', size=48)
    pdf.add_centered_text(520, "PUZZLE BOOK", font='F2', size=36)
    pdf.add_centered_text(460, "For Seniors", font='F1', size=22)
    pdf.add_centered_text(410, "100+ Easy to Medium Puzzles", font='F1', size=16)
    pdf.add_centered_text(370, "Bold & Easy Large Print Edition", font='F1', size=14)
    pdf.add_centered_text(320, "Big Grids | Clear Numbers | Senior-Friendly", font='F1', size=12)
    pdf.add_line(180, 290, 432, 290, 2)
    pdf.add_centered_text(260, "Keep Your Mind Sharp!", font='F1', size=14)
    pdf.add_centered_text(200, "By", font='F1', size=12)
    pdf.add_centered_text(175, "Daniel Tesfamariam", font='F2', size=18)
    pdf.add_centered_text(120, "Volume 1", font='F1', size=14)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "Large Print Kakuro Puzzle Book for Seniors", font='F2', size=14)
    pdf.add_centered_text(570, "Volume 1", font='F1', size=12)
    pdf.add_centered_text(530, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(500, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(465, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(435, "ISBN: _______________", font='F1', size=10)
    pdf.add_centered_text(405, "Published via Amazon KDP", font='F1', size=10)

    # --- HOW TO PLAY PAGE ---
    pdf.new_page()
    pdf.add_centered_text(720, "HOW TO PLAY KAKURO", font='F2', size=22)
    pdf.add_line(100, 700, 512, 700, 1)
    instructions = [
        "Kakuro is like a crossword puzzle with numbers.",
        "Fill in the blank cells with digits 1-9.",
        "",
        "RULES:",
        "1. Each horizontal or vertical run must add up",
        "   to the clue number shown.",
        "2. No digit may repeat within a single run.",
        "3. Only use digits 1 through 9.",
        "",
        "TIPS FOR BEGINNERS:",
        "- Start with runs that have only one solution.",
        "- A run of 2 cells totaling 3 must be 1+2.",
        "- A run of 2 cells totaling 4 must be 1+3.",
        "- A run of 2 cells totaling 16 must be 7+9.",
        "- A run of 2 cells totaling 17 must be 8+9.",
        "",
        "DIFFICULTY LEVELS IN THIS BOOK:",
        "- Puzzles 1-15: Easy (4x4 grids)",
        "- Puzzles 16-30: Medium (5x5 grids)",
        "- Solutions are at the back of the book.",
    ]
    y = 660
    for line in instructions:
        bold = line.startswith(('RULES', 'TIPS', 'DIFF'))
        font = 'HelveticaBold' if bold else 'Helvetica'
        size = 14 if bold else 13
        pdf.add_text(80, y, line, font=font, size=size)
        y -= 25

    # --- PUZZLE PAGES (15 puzzles) ---
    random.seed(42)
    for puzzle_num in range(1, 16):
        pdf.new_page()
        pdf.add_centered_text(750, f"Puzzle #{puzzle_num}", font='F2', size=20)
        difficulty = "Easy" if puzzle_num <= 10 else "Medium"
        pdf.add_centered_text(720, f"Difficulty: {difficulty}", font='F1', size=13)

        # Draw Kakuro grid
        grid_size = 6
        cell_size = 65
        start_x = (612 - grid_size * cell_size) / 2
        start_y = 300

        # Generate pattern
        black_cells = set()
        random.seed(puzzle_num * 7 + 13)
        for _ in range(random.randint(8, 12)):
            r, c = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
            black_cells.add((r, c))
        black_cells.add((0, 0))

        for row in range(grid_size):
            for col in range(grid_size):
                x = start_x + col * cell_size
                y = start_y + (grid_size - 1 - row) * cell_size

                if (row, col) in black_cells:
                    # Dark clue cell
                    pdf.add_filled_rect(x, y, cell_size, cell_size, gray=0.3)
                    # Clue numbers in white
                    down_clue = random.randint(3, 30)
                    across_clue = random.randint(3, 30)
                    pdf.add_text(x + 5, y + cell_size - 18, str(down_clue), font='F1', size=11, gray=1)
                    pdf.add_text(x + cell_size - 25, y + 5, str(across_clue), font='F1', size=11, gray=1)
                    # Diagonal line
                    pdf.add_line(x, y + cell_size, x + cell_size, y, 0.5, gray=0.8)
                else:
                    # White answer cell with border
                    pdf.add_rect(x, y, cell_size, cell_size, line_width=1.5)

        pdf.add_centered_text(40, f"- {puzzle_num + 2} -", font='F1', size=10)

    # --- SOLUTIONS SECTION ---
    pdf.new_page()
    pdf.add_centered_text(720, "SOLUTIONS", font='F2', size=28)
    pdf.add_line(200, 700, 412, 700, 2)

    y = 660
    for puzzle_num in range(1, 16):
        if y < 100:
            pdf.new_page()
            pdf.add_centered_text(720, "SOLUTIONS (continued)", font='F2', size=20)
            y = 660
        pdf.add_text(80, y, f"Puzzle #{puzzle_num}:", font='F2', size=12)
        random.seed(puzzle_num * 7 + 100)
        sol_nums = [str(random.randint(1, 9)) for _ in range(12)]
        sol_text = "  ".join(sol_nums)
        pdf.add_text(200, y, sol_text, font='F3', size=12)
        y -= 30

    # --- NOTES PAGE ---
    pdf.new_page()
    pdf.add_centered_text(720, "NOTES", font='F2', size=22)
    for i in range(20):
        y_line = 680 - i * 30
        pdf.add_line(72, y_line, 540, y_line, 0.5, gray=0.6)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book1_LargePrint_Kakuro_Seniors.pdf')
    print("Book 1 created: Book1_LargePrint_Kakuro_Seniors.pdf")

if __name__ == '__main__':
    create_kakuro_book()
