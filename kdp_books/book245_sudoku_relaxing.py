"""Book 245: Relaxing Sudoku - Gentle Puzzles for Stress Relief"""
import random
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(245 * 42)

QUOTES = [
    "Take your time. There is no rush.",
    "Every puzzle solved is a small victory.",
    "Breathe deeply and enjoy the moment.",
    "Progress, not perfection.",
    "You are doing wonderfully.",
    "One number at a time.",
    "Peace comes from within.",
    "Enjoy the journey, not just the destination.",
    "Be patient with yourself.",
    "Quiet the mind and the soul will speak.",
    "Relax. You have all the time you need.",
    "Small steps lead to big achievements.",
    "Find joy in the simple things.",
    "Let your mind wander and wonder.",
    "Today is a gift. Enjoy it.",
    "Celebrate every small win.",
    "The best things happen slowly.",
    "Be gentle with yourself today.",
    "Focus on progress, not speed.",
    "You are stronger than you think.",
    "Every moment is a fresh beginning.",
    "Slow down and appreciate the now.",
    "Your mind is a beautiful thing.",
    "Puzzles are food for the soul.",
    "Calm mind, sharp thinking.",
    "Patience is a superpower.",
    "One step at a time gets you there.",
    "Embrace the challenge with a smile.",
    "Rest your worries, exercise your mind.",
    "You have everything you need within you.",
]

def generate_sudoku_grid():
    grid = [[0]*9 for _ in range(9)]
    def is_valid(grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        box_r, box_c = 3*(row//3), 3*(col//3)
        for i in range(box_r, box_r+3):
            for j in range(box_c, box_c+3):
                if grid[i][j] == num:
                    return False
        return True
    def solve(grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    nums = list(range(1,10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(grid, i, j, num):
                            grid[i][j] = num
                            if solve(grid):
                                return True
                            grid[i][j] = 0
                    return False
        return True
    solve(grid)
    return grid

def create_puzzle(grid, num_filled):
    puzzle = [row[:] for row in grid]
    positions = [(i,j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    to_remove = 81 - num_filled
    for i in range(to_remove):
        r, c = positions[i]
        puzzle[r][c] = 0
    return puzzle

def draw_sudoku_grid(pdf, puzzle, start_x, start_y, cell_size, font_size=18):
    grid_size = cell_size * 9
    for i in range(10):
        lw = 2.5 if i % 3 == 0 else 0.5
        pdf.add_line(start_x, start_y - i*cell_size, start_x + grid_size, start_y - i*cell_size, width=lw)
        pdf.add_line(start_x + i*cell_size, start_y, start_x + i*cell_size, start_y - grid_size, width=lw)
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] != 0:
                num_str = str(puzzle[row][col])
                nx = start_x + col*cell_size + cell_size*0.35
                ny = start_y - row*cell_size - cell_size*0.7
                pdf.add_text(nx, ny, num_str, font='F2', size=font_size)

pdf = PDFDoc(612, 792)

pdf.add_centered_text(550, "RELAXING SUDOKU", font='F2', size=28)
pdf.add_centered_text(490, "Gentle Puzzles for Stress Relief", font='F4', size=20)
pdf.add_centered_text(400, "30 Easy Puzzles with Calming Quotes", font='F1', size=16)
pdf.add_centered_text(350, "Unwind, Relax, and Solve", font='F4', size=14)
pdf.add_centered_text(100, "Daniel Tesfamariam", font='F2', size=14)

pdf.new_page()
pdf.add_centered_text(600, "RELAXING SUDOKU", font='F2', size=14)
pdf.add_text(72, 540, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", font='F1', size=11)
pdf.add_text(72, 510, "No part of this publication may be reproduced without permission.", font='F1', size=11)
pdf.add_text(72, 460, "This book is designed for relaxation and stress relief.", font='F4', size=12)
pdf.add_text(72, 435, "Take your time with each puzzle and enjoy the calming quotes.", font='F4', size=12)

pdf.new_page()
pdf.add_centered_text(700, "HOW TO PLAY SUDOKU", font='F2', size=22)
pdf.add_text(72, 640, "Fill every row, column, and 3x3 box with digits 1-9.", font='F1', size=13)
pdf.add_text(72, 600, "No number repeats in any row, column, or box.", font='F1', size=13)
pdf.add_text(72, 550, "These are EASY puzzles - perfect for relaxing.", font='F2', size=13)
pdf.add_text(72, 510, "Each puzzle includes a calming quote at the bottom.", font='F4', size=13)
pdf.add_text(72, 470, "No timer. No pressure. Just you and the puzzle.", font='F4', size=13)

solutions = []
puzzles = []
for i in range(30):
    grid = generate_sudoku_grid()
    solutions.append(grid)
    num_filled = random.randint(38, 44)
    puzzle = create_puzzle(grid, num_filled)
    puzzles.append(puzzle)

cell_size = 46
start_x = (612 - cell_size*9) / 2
start_y = 650

for i, puzzle in enumerate(puzzles):
    pdf.new_page()
    pdf.add_centered_text(740, f"Puzzle #{i+1}", font='F2', size=18)
    draw_sudoku_grid(pdf, puzzle, start_x, start_y, cell_size, font_size=17)
    # Calming quote at bottom
    quote = QUOTES[i % len(QUOTES)]
    pdf.add_centered_text(80, f'"{quote}"', font='F4', size=12, gray=0.3)

# Solutions
pdf.new_page()
pdf.add_centered_text(750, "SOLUTIONS", font='F2', size=24)

sol_per_page = 6
small_cell = 18
for idx, sol in enumerate(solutions):
    if idx > 0 and idx % sol_per_page == 0:
        pdf.new_page()
    pos_in_page = idx % sol_per_page
    col = pos_in_page % 2
    row = pos_in_page // 2
    sx = 50 + col * 290
    sy = 700 - row * 220
    pdf.add_text(sx, sy + 15, f"Puzzle #{idx+1}", font='F2', size=9)
    for li in range(10):
        lw = 1.5 if li % 3 == 0 else 0.3
        pdf.add_line(sx, sy - li*small_cell, sx + 9*small_cell, sy - li*small_cell, width=lw)
        pdf.add_line(sx + li*small_cell, sy, sx + li*small_cell, sy - 9*small_cell, width=lw)
    for r in range(9):
        for c in range(9):
            nx = sx + c*small_cell + 5
            ny = sy - r*small_cell - 14
            pdf.add_text(nx, ny, str(sol[r][c]), font='F1', size=8)

pdf.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book245_Sudoku_Relaxing.pdf"))
print("Book245_Sudoku_Relaxing.pdf created successfully!")
