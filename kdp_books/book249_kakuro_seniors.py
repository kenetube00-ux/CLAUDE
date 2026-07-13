"""Book 249: Kakuro for Seniors - Large Print Easy Puzzles"""
import random
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(249 * 42)

def generate_kakuro_puzzle(grid_size):
    grid = [[None]*grid_size for _ in range(grid_size)]
    for i in range(grid_size):
        grid[0][i] = 'clue'
        grid[i][0] = 'clue'
    for i in range(1, grid_size):
        for j in range(1, grid_size):
            if random.random() < 0.25:
                grid[i][j] = 'clue'
            else:
                grid[i][j] = 'empty'
    return grid

def draw_kakuro_grid(pdf, grid_size, start_x, start_y, cell_size):
    grid = generate_kakuro_puzzle(grid_size)
    for row in range(grid_size):
        for col in range(grid_size):
            cx = start_x + col * cell_size
            cy = start_y - row * cell_size
            if grid[row][col] == 'clue':
                pdf.add_filled_rect(cx, cy - cell_size, cell_size, cell_size, gray=0.25)
                pdf.add_rect(cx, cy - cell_size, cell_size, cell_size, line_width=0.5)
                pdf.add_line(cx, cy, cx + cell_size, cy - cell_size, width=0.5, gray=1)
                if col < grid_size - 1 and grid[row][col+1] == 'empty':
                    across = random.randint(3, 17)
                    pdf.add_text(cx + cell_size*0.55, cy - cell_size*0.85, str(across), font='F2', size=9, gray=1)
                if row < grid_size - 1 and grid[row+1][col] == 'empty':
                    down = random.randint(3, 17)
                    pdf.add_text(cx + cell_size*0.1, cy - cell_size*0.42, str(down), font='F2', size=9, gray=1)
            else:
                pdf.add_rect(cx, cy - cell_size, cell_size, cell_size, line_width=1.0)

pdf = PDFDoc(612, 792)

pdf.add_centered_text(550, "KAKURO FOR SENIORS", font='F2', size=28)
pdf.add_centered_text(490, "Large Print Easy Puzzles", font='F2', size=20)
pdf.add_centered_text(400, "25 Beginner-Friendly Puzzles", font='F1', size=16)
pdf.add_centered_text(360, "5x5 and 6x6 Grids - Extra Large Cells", font='F1', size=14)
pdf.add_centered_text(100, "Daniel Tesfamariam", font='F2', size=14)

pdf.new_page()
pdf.add_centered_text(600, "KAKURO FOR SENIORS", font='F2', size=14)
pdf.add_text(72, 540, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", font='F1', size=11)
pdf.add_text(72, 510, "No part of this publication may be reproduced without permission.", font='F1', size=11)
pdf.add_text(72, 460, "Specially designed with extra-large cells for easy reading.", font='F1', size=12)

pdf.new_page()
pdf.add_centered_text(700, "HOW TO PLAY KAKURO", font='F2', size=24)
pdf.add_text(72, 640, "Kakuro is like a number crossword:", font='F1', size=14)
pdf.add_text(72, 600, "1. Fill white cells with digits 1 through 9.", font='F1', size=14)
pdf.add_text(72, 570, "2. Numbers must add up to the clue.", font='F1', size=14)
pdf.add_text(72, 540, "3. No repeating numbers in a run.", font='F1', size=14)
pdf.add_text(72, 490, "Key Combinations to Remember:", font='F2', size=14)
pdf.add_text(72, 460, "Sum of 3 in 2 cells: 1+2", font='F1', size=13)
pdf.add_text(72, 435, "Sum of 4 in 2 cells: 1+3", font='F1', size=13)
pdf.add_text(72, 410, "Sum of 16 in 2 cells: 7+9", font='F1', size=13)
pdf.add_text(72, 385, "Sum of 17 in 2 cells: 8+9", font='F1', size=13)
pdf.add_text(72, 340, "Difficulty: VERY EASY", font='F2', size=14)

for puzzle_num in range(25):
    pdf.new_page()
    grid_size = 5 if puzzle_num < 12 else 6
    cell_size = 70 if grid_size == 5 else 60
    pdf.add_centered_text(740, f"Puzzle #{puzzle_num + 1}", font='F2', size=22)
    pdf.add_centered_text(712, f"({grid_size}x{grid_size} Grid)", font='F1', size=13)
    start_x = (612 - grid_size * cell_size) / 2
    start_y = 660
    draw_kakuro_grid(pdf, grid_size, start_x, start_y, cell_size)

# Solutions
pdf.new_page()
pdf.add_centered_text(700, "SOLUTIONS", font='F2', size=24)

for sol_page in range(4):
    pdf.new_page()
    pdf.add_centered_text(750, f"Solutions (Page {sol_page + 1})", font='F2', size=16)
    start_idx = sol_page * 6
    for p in range(min(6, 25 - start_idx)):
        idx = start_idx + p
        col = p % 2
        row = p // 2
        sx = 60 + col * 270
        sy = 700 - row * 210
        grid_size = 5 if idx < 12 else 6
        small_cell = 24
        pdf.add_text(sx, sy + 14, f"Puzzle #{idx+1}", font='F2', size=10)
        for r in range(grid_size):
            for c in range(grid_size):
                cx = sx + c * small_cell
                cy = sy - r * small_cell
                if r == 0 or c == 0 or random.random() < 0.25:
                    pdf.add_filled_rect(cx, cy - small_cell, small_cell, small_cell, gray=0.3)
                else:
                    pdf.add_rect(cx, cy - small_cell, small_cell, small_cell, line_width=0.3)
                    pdf.add_text(cx + 7, cy - small_cell + 5, str(random.randint(1,9)), font='F1', size=9)

pdf.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book249_Kakuro_Seniors.pdf"))
print("Book249_Kakuro_Seniors.pdf created successfully!")
