"""Book 243: Large Print Sudoku - Mixed Difficulty Volume 1"""
import random
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(243 * 42)

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

def draw_sudoku_grid(pdf, puzzle, start_x, start_y, cell_size, font_size=16):
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

pdf.add_centered_text(550, "LARGE PRINT SUDOKU", font='F2', size=28)
pdf.add_centered_text(500, "Mixed Difficulty", font='F2', size=22)
pdf.add_centered_text(460, "(Easy to Hard) Volume 1", font='F1', size=18)
pdf.add_centered_text(380, "30 Puzzles - Progressive Challenge", font='F1', size=16)
pdf.add_centered_text(340, "10 Easy + 10 Medium + 10 Hard", font='F1', size=14)
pdf.add_centered_text(100, "Daniel Tesfamariam", font='F2', size=14)

pdf.new_page()
pdf.add_centered_text(600, "LARGE PRINT SUDOKU - Mixed Difficulty Volume 1", font='F2', size=14)
pdf.add_text(72, 540, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", font='F1', size=11)
pdf.add_text(72, 510, "No part of this publication may be reproduced without permission.", font='F1', size=11)

pdf.new_page()
pdf.add_centered_text(700, "HOW TO PLAY SUDOKU", font='F2', size=22)
pdf.add_text(72, 640, "Fill every row, column, and 3x3 box with digits 1-9.", font='F1', size=13)
pdf.add_text(72, 590, "This book features increasing difficulty:", font='F2', size=13)
pdf.add_text(72, 560, "Puzzles 1-10: EASY (35-40 given numbers)", font='F1', size=12)
pdf.add_text(72, 535, "Puzzles 11-20: MEDIUM (28-33 given numbers)", font='F1', size=12)
pdf.add_text(72, 510, "Puzzles 21-30: HARD (22-27 given numbers)", font='F1', size=12)
pdf.add_text(72, 460, "Start easy and work your way up!", font='F2', size=13)

solutions = []
puzzles = []
difficulties = []
for i in range(30):
    grid = generate_sudoku_grid()
    solutions.append(grid)
    if i < 10:
        num_filled = random.randint(35, 40)
        difficulties.append("Easy")
    elif i < 20:
        num_filled = random.randint(28, 33)
        difficulties.append("Medium")
    else:
        num_filled = random.randint(22, 27)
        difficulties.append("Hard")
    puzzle = create_puzzle(grid, num_filled)
    puzzles.append(puzzle)

cell_size = 48
start_x = (612 - cell_size*9) / 2
start_y = 640

for i, puzzle in enumerate(puzzles):
    pdf.new_page()
    pdf.add_centered_text(740, f"Puzzle #{i+1}", font='F2', size=20)
    pdf.add_centered_text(715, f"Difficulty: {difficulties[i]}", font='F1', size=12)
    draw_sudoku_grid(pdf, puzzle, start_x, start_y, cell_size, font_size=18)

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
    pdf.add_text(sx, sy + 15, f"#{idx+1} ({difficulties[idx]})", font='F2', size=9)
    for li in range(10):
        lw = 1.5 if li % 3 == 0 else 0.3
        pdf.add_line(sx, sy - li*small_cell, sx + 9*small_cell, sy - li*small_cell, width=lw)
        pdf.add_line(sx + li*small_cell, sy, sx + li*small_cell, sy - 9*small_cell, width=lw)
    for r in range(9):
        for c in range(9):
            nx = sx + c*small_cell + 5
            ny = sy - r*small_cell - 14
            pdf.add_text(nx, ny, str(sol[r][c]), font='F1', size=8)

pdf.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book243_Sudoku_Mixed_Difficulty.pdf"))
print("Book243_Sudoku_Mixed_Difficulty.pdf created successfully!")
