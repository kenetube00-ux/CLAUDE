"""Book 50: Fun Math Workbook for Kids Ages 5-7"""
import random
from pdf_utils import PDFDoc

random.seed(42)  # Reproducible problems

pdf = PDFDoc(612, 792)

# Title page
pdf.new_page()
pdf.add_centered_text(500, "FUN MATH WORKBOOK", 'F2', 26)
pdf.add_centered_text(460, "For Kids Ages 5-7", 'F4', 16, 0.3)
pdf.add_line(180, 440, 432, 440, 1, 0.5)
pdf.add_centered_text(250, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(500, "Fun Math Workbook - For Kids Ages 5-7", 'F2', 14)
pdf.add_centered_text(470, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(450, "All rights reserved.", 'F1', 10)

page_count = 0

# Activity 1: Counting objects (8 pages)
for pg in range(8):
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(740, f"Counting Objects - Page {pg+1}", 'F2', 14)
    pdf.add_text(50, 710, "Count the shapes and write the number.", 'F1', 12)
    y = 670
    for row in range(5):
        count = random.randint(1, 10)
        # Draw shapes in a row
        for s in range(count):
            x = 80 + s * 30
            pdf.add_rect(x, y - 10, 15, 15, 1.5, 0)
        # Answer blank
        pdf.add_text(420, y - 5, "= _____", 'F1', 14)
        y -= 55


# Activity 2: Simple addition (8 pages, 10 problems each)
for pg in range(8):
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(740, f"Addition - Page {pg+1}", 'F2', 14)
    pdf.add_text(50, 710, "Solve each addition problem.", 'F1', 12)
    y = 670
    for prob in range(10):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        pdf.add_text(80, y, f"{a}  +  {b}  =  _____", 'F2', 16)
        y -= 50

# Activity 3: Simple subtraction (8 pages, 10 problems each)
for pg in range(8):
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(740, f"Subtraction - Page {pg+1}", 'F2', 14)
    pdf.add_text(50, 710, "Solve each subtraction problem.", 'F1', 12)
    y = 670
    for prob in range(10):
        a = random.randint(3, 10)
        b = random.randint(0, a)
        pdf.add_text(80, y, f"{a}  -  {b}  =  _____", 'F2', 16)
        y -= 50

# Activity 4: Number tracing (4 pages, 1-20)
for pg in range(4):
    pdf.new_page()
    page_count += 1
    start_num = pg * 5 + 1
    end_num = min(start_num + 4, 20)
    pdf.add_centered_text(740, f"Number Tracing - {start_num} to {end_num}", 'F2', 14)
    pdf.add_text(50, 710, "Trace each number and practice writing it.", 'F1', 12)
    y = 660
    for num in range(start_num, end_num + 1):
        # Large number to trace
        pdf.add_text(60, y, str(num), 'F2', 36, 0.6)
        # Practice line
        pdf.add_line(130, y, 550, y, 0.5, 0.6)
        pdf.add_line(130, y + 20, 550, y + 20, 0.5, 0.8)
        y -= 80


# Activity 5: Greater than / less than (4 pages)
for pg in range(4):
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(740, f"Greater Than / Less Than - Page {pg+1}", 'F2', 14)
    pdf.add_text(50, 710, "Write > or < or = in the circle.", 'F1', 12)
    y = 660
    for prob in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        pdf.add_text(80, y, f"{a}", 'F2', 18)
        pdf.add_rect(130, y - 5, 30, 25, 1.5, 0)
        pdf.add_text(180, y, f"{b}", 'F2', 18)
        y -= 50

# Activity 6: Fill in the missing number (4 pages)
for pg in range(4):
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(740, f"Missing Numbers - Page {pg+1}", 'F2', 14)
    pdf.add_text(50, 710, "Fill in the missing number in each sequence.", 'F1', 12)
    y = 660
    for prob in range(8):
        start = random.randint(1, 10)
        seq = list(range(start, start + 5))
        blank_pos = random.randint(0, 4)
        display = ""
        for i, n in enumerate(seq):
            if i == blank_pos:
                display += " ___ "
            else:
                display += f" {n} "
            if i < 4:
                display += ","
        pdf.add_text(80, y, display, 'F2', 14)
        y -= 55

# Activity 7: Match number to dots (4 pages)
for pg in range(4):
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(740, f"Match the Number - Page {pg+1}", 'F2', 14)
    pdf.add_text(50, 710, "Count the dots and draw a line to the number.", 'F1', 12)
    y = 660
    numbers = random.sample(range(1, 11), 5)
    shuffled = numbers[:]
    random.shuffle(shuffled)
    for i, num in enumerate(numbers):
        # Draw dots on left
        for d in range(num):
            dx = 60 + (d % 5) * 18
            dy = y + (d // 5) * 15
            pdf.add_rect(dx, dy, 8, 8, 1, 0)
        # Number on right
        pdf.add_text(450, y + 5, str(shuffled[i]), 'F2', 18)
        y -= 80

# Great Job! certificate page
pdf.new_page()
page_count += 1
pdf.add_rect(50, 200, 512, 450, 3, 0)
pdf.add_rect(60, 210, 492, 430, 1.5, 0.4)
pdf.add_centered_text(580, "GREAT JOB!", 'F2', 36)
pdf.add_centered_text(520, "Certificate of Achievement", 'F2', 18)
pdf.add_centered_text(470, "This certifies that", 'F4', 14)
pdf.add_line(180, 430, 432, 430, 1, 0)
pdf.add_centered_text(410, "(write your name)", 'F1', 9, 0.5)
pdf.add_centered_text(380, "has completed the", 'F4', 14)
pdf.add_centered_text(350, "Fun Math Workbook!", 'F2', 16)
pdf.add_centered_text(300, "Date: _______________", 'F4', 12)
pdf.add_centered_text(260, "You are a Math Star!", 'F2', 14)

pdf.save("Book50_Kids_Math_Workbook.pdf")
print("Created Book50_Kids_Math_Workbook.pdf")
