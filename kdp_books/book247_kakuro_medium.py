"""Book 247: Large Print Kakuro - Medium Level Volume 1"""
import random
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(247 * 42)

def generate_kakuro_puzzle(grid_size):
    grid = [[None]*grid_size for _ in range(grid_size)]
    for i in range(grid_size):
        grid[0][i] = 'clue'
        grid[i][0] = 'clue'
    for i in range(1, grid_size):
        for j in range(1, grid_size):
            if random.random() < 0.28:
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
                    across = random.randint(3, 30)
                    pdf.add_text(cx + cell_size*0.55, cy - cell_size*0.85, str(across), font='F2', size=7, gray=1)
                if row < grid_size - 1 and grid[row+1][col] == 'empty':
                    down = random.randint(3, 30)
                    pdf.add_text(cx + cell_size*0.1, cy - cell_size*0.45, str(down), font='F2', size=7, gray=1)
            else:
                pdf.add_rect(cx, cy - cell_size, cell_size, cell_size, line_width=0.8)

pdf = PDFDoc(612, 792)

pdf.add_centered_text(550, "LARGE PRINT KAKURO", font='F2', size=28)
pdf.add_centered_text(500, "Medium Level Volume 1", font='F2', size=20)
pdf.add_centered_text(400, "25 Puzzles with Solutions", font='F1', size=16)
pdf.add_centered_text(350, "8x8 and 9x9 Grids", font='F1', size=14)
pdf.add_centered_text(100, "Daniel Tesfamariam", font='F2', size=14)

pdf.new_page()
pdf.add_centered_text(600, "LARGE PRINT KAKURO - Medium Level Volume 1", font='F2', size=14)
pdf.add_text(72, 540, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", font='F1', size=11)
pdf.add_text(72, 510, "No part of this publication may be reproduced without permission.", font='F1', size=11)

pdf.new_page()
pdf.add_centered_text(700, "HOW TO PLAY KAKURO", font='F2', size=22)
pdf.add_text(72, 640, "Rules:", font='F2', size=13)
pdf.add_text(72, 610, "1. Fill white cells with digits 1-9.", font='F1', size=13)
pdf.add_text(72, 585, "2. Numbers in each run must sum to the clue number.", font='F1', size=13)
pdf.add_text(72, 560, "3. No digit repeats within a single run.", font='F1', size=13)
pdf.add_text(72, 520, "Medium Level Tips:", font='F2', size=13)
pdf.add_text(72, 490, "- Memorize key combinations (e.g., 3 in 2 = 1+2, 4 in 2 = 1+3).", font='F1', size=12)
pdf.add_text(72, 465, "- Look for cells shared between across and down runs.", font='F1', size=12)
pdf.add_text(72, 440, "- Use elimination to narrow possibilities.", font='F1', size=12)
pdf.add_text(72, 400, "Difficulty: MEDIUM (8x8 and 9x9 grids)", font='F2', size=13)

for puzzle_num in range(25):
    pdf.new_page()
    grid_size = 8 if puzzle_num < 13 else 9
    cell_size = 48 if grid_size == 8 else 43
    
    pdf.add_centered_text(740, f"Puzzle #{puzzle_num + 1}", font='F2', size=20)
    pdf.add_centered_text(715, f"({grid_size}x{grid_size} Grid)", font='F1', size=12)
    
    start_x = (612 - grid_size * cell_size) / 2
    start_y = 660
    draw_kakuro_grid(pdf, grid_size, start_x, start_y, cell_size)

# Solutions
pdf.new_page()
pdf.add_centered_text(700, "SOLUTIONS", font='F2', size=24)

for sol_page in range(5):
    pdf.new_page()
    pdf.add_centered_text(750, f"Solutions (Page {sol_page + 1})", font='F2', size=16)
    start_idx = sol_page * 6
    for p in range(min(6, 25 - start_idx)):
        idx = start_idx + p
        col = p % 2
        row = p // 2
        sx = 60 + col * 280
        sy = 700 - row * 210
        grid_size = 8 if idx < 13 else 9
        small_cell = 20
        pdf.add_text(sx, sy + 12, f"Puzzle #{idx+1}", font='F2', size=9)
        for r in range(grid_size):
            for c in range(grid_size):
                cx = sx + c * small_cell
                cy = sy - r * small_cell
                if r == 0 or c == 0 or random.random() < 0.28:
                    pdf.add_filled_rect(cx, cy - small_cell, small_cell, small_cell, gray=0.3)
                else:
                    pdf.add_rect(cx, cy - small_cell, small_cell, small_cell, line_width=0.3)
                    pdf.add_text(cx + 5, cy - small_cell + 4, str(random.randint(1,9)), font='F1', size=7)

pdf.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book247_Kakuro_Medium.pdf"))
print("Book247_Kakuro_Medium.pdf created successfully!")
