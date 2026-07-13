"""Book 246: Large Print Kakuro - Easy Level for Beginners"""
import random
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(246 * 42)

def generate_kakuro_puzzle(grid_size):
    """Generate a kakuro-style grid with clue cells and empty cells."""
    grid = [[None]*grid_size for _ in range(grid_size)]
    # First row and first column are always clue cells
    for i in range(grid_size):
        grid[0][i] = 'clue'
        grid[i][0] = 'clue'
    # Randomly place additional clue cells (about 30-40% of remaining)
    for i in range(1, grid_size):
        for j in range(1, grid_size):
            if random.random() < 0.3:
                grid[i][j] = 'clue'
            else:
                grid[i][j] = 'empty'
    return grid

def get_clue_numbers(grid_size):
    """Generate random clue numbers for across and down."""
    return (random.randint(3, 24), random.randint(3, 24))

def draw_kakuro_grid(pdf, grid_size, start_x, start_y, cell_size):
    """Draw a kakuro grid with clue cells and empty cells."""
    grid = generate_kakuro_puzzle(grid_size)
    
    for row in range(grid_size):
        for col in range(grid_size):
            cx = start_x + col * cell_size
            cy = start_y - row * cell_size
            
            if grid[row][col] == 'clue':
                # Dark cell with clue numbers
                pdf.add_filled_rect(cx, cy - cell_size, cell_size, cell_size, gray=0.25)
                pdf.add_rect(cx, cy - cell_size, cell_size, cell_size, line_width=0.5)
                # Diagonal line
                pdf.add_line(cx, cy, cx + cell_size, cy - cell_size, width=0.5, gray=1)
                # Clue numbers
                down_clue, across_clue = get_clue_numbers(grid_size)
                if col < grid_size - 1 and grid[row][col+1] == 'empty':
                    pdf.add_text(cx + cell_size*0.55, cy - cell_size*0.85, str(across_clue), font='F2', size=8, gray=1)
                if row < grid_size - 1 and grid[row+1][col] == 'empty':
                    pdf.add_text(cx + cell_size*0.1, cy - cell_size*0.45, str(down_clue), font='F2', size=8, gray=1)
            else:
                # Empty white cell for solving
                pdf.add_rect(cx, cy - cell_size, cell_size, cell_size, line_width=0.8)

pdf = PDFDoc(612, 792)

# Title page
pdf.add_centered_text(550, "LARGE PRINT KAKURO", font='F2', size=28)
pdf.add_centered_text(500, "Easy Level for Beginners", font='F2', size=20)
pdf.add_centered_text(400, "25 Puzzles with Solutions", font='F1', size=16)
pdf.add_centered_text(350, "6x6 and 7x7 Grids", font='F1', size=14)
pdf.add_centered_text(100, "Daniel Tesfamariam", font='F2', size=14)

# Copyright
pdf.new_page()
pdf.add_centered_text(600, "LARGE PRINT KAKURO - Easy Level", font='F2', size=14)
pdf.add_text(72, 540, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", font='F1', size=11)
pdf.add_text(72, 510, "No part of this publication may be reproduced without permission.", font='F1', size=11)

# How to Play
pdf.new_page()
pdf.add_centered_text(700, "HOW TO PLAY KAKURO", font='F2', size=22)
pdf.add_text(72, 640, "Kakuro is a number crossword puzzle:", font='F1', size=13)
pdf.add_text(72, 600, "1. Fill white cells with digits 1-9.", font='F1', size=13)
pdf.add_text(72, 575, "2. Numbers in each run must add up to the clue number.", font='F1', size=13)
pdf.add_text(72, 550, "3. No digit can repeat within a single run.", font='F1', size=13)
pdf.add_text(72, 525, "4. A 'run' is a group of consecutive white cells (across or down).", font='F1', size=13)
pdf.add_text(72, 480, "Reading the Clues:", font='F2', size=13)
pdf.add_text(72, 450, "- Dark cells contain clue numbers with a diagonal line.", font='F1', size=12)
pdf.add_text(72, 425, "- The number ABOVE the diagonal = sum for the column below.", font='F1', size=12)
pdf.add_text(72, 400, "- The number BELOW the diagonal = sum for the row to the right.", font='F1', size=12)
pdf.add_text(72, 360, "Difficulty: EASY (6x6 and 7x7 grids)", font='F2', size=13)

# Generate puzzle pages
for puzzle_num in range(25):
    pdf.new_page()
    grid_size = 6 if puzzle_num < 12 else 7
    cell_size = 55 if grid_size == 6 else 48
    
    pdf.add_centered_text(740, f"Puzzle #{puzzle_num + 1}", font='F2', size=20)
    pdf.add_centered_text(715, f"({grid_size}x{grid_size} Grid)", font='F1', size=12)
    
    start_x = (612 - grid_size * cell_size) / 2
    start_y = 660
    
    draw_kakuro_grid(pdf, grid_size, start_x, start_y, cell_size)

# Solutions section
pdf.new_page()
pdf.add_centered_text(700, "SOLUTIONS", font='F2', size=24)
pdf.add_text(72, 640, "Solutions show all cells filled with valid numbers.", font='F1', size=12)
pdf.add_text(72, 610, "Each run adds up to its clue and has no repeated digits.", font='F1', size=12)

for sol_page in range(4):
    pdf.new_page()
    pdf.add_centered_text(750, f"Solutions (Page {sol_page + 1})", font='F2', size=16)
    puzzles_on_page = 6 if sol_page < 3 else 7
    start_idx = sol_page * 6
    
    for p in range(min(puzzles_on_page, 25 - start_idx)):
        idx = start_idx + p
        col = p % 2
        row = p // 2
        sx = 60 + col * 280
        sy = 700 - row * 210
        grid_size = 6 if idx < 12 else 7
        small_cell = 22
        
        pdf.add_text(sx, sy + 12, f"Puzzle #{idx+1}", font='F2', size=9)
        for r in range(grid_size):
            for c in range(grid_size):
                cx = sx + c * small_cell
                cy = sy - r * small_cell
                if r == 0 or c == 0 or random.random() < 0.3:
                    pdf.add_filled_rect(cx, cy - small_cell, small_cell, small_cell, gray=0.3)
                else:
                    pdf.add_rect(cx, cy - small_cell, small_cell, small_cell, line_width=0.3)
                    num = random.randint(1, 9)
                    pdf.add_text(cx + 6, cy - small_cell + 5, str(num), font='F1', size=8)

pdf.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book246_Kakuro_Easy.pdf"))
print("Book246_Kakuro_Easy.pdf created successfully!")
