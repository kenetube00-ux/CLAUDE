"""Book 41: Mom's Self-Care Journal"""
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)

# Title page
pdf.new_page()
pdf.add_centered_text(400, "MOM'S SELF-CARE JOURNAL", 'F2', 22)
pdf.add_centered_text(360, "Because You Matter Too", 'F4', 16, 0.3)
pdf.add_line(116, 340, 316, 340, 1, 0.5)
pdf.add_centered_text(200, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(400, "Mom's Self-Care Journal", 'F2', 14)
pdf.add_centered_text(370, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(350, "All rights reserved.", 'F1', 10)
pdf.add_centered_text(320, "No part of this book may be reproduced without permission.", 'F1', 9)

# 60 daily pages
for day in range(1, 61):
    pdf.new_page()
    pdf.add_text(50, 610, f"Day {day}", 'F2', 14)
    pdf.add_text(300, 610, "Date: _______________", 'F1', 10)
    pdf.add_line(50, 600, 382, 600, 0.5, 0.5)

    y = 575
    pdf.add_text(50, y, "Hours of sleep: ________", 'F1', 11)
    y -= 30
    pdf.add_text(50, y, "How I feel today (1-10): ________", 'F1', 11)
    y -= 35
    pdf.add_text(50, y, "One thing just for ME today:", 'F2', 11)
    y -= 20
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 30
    pdf.add_text(50, y, "I am proud of myself for:", 'F2', 11)
    y -= 20
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 30
    pdf.add_text(50, y, "I need to let go of:", 'F2', 11)
    y -= 20
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 35
    pdf.add_text(50, y, "Gratitude - 3 things I am thankful for:", 'F2', 11)
    y -= 20
    pdf.add_text(50, y, "1. ________________________________________________", 'F1', 10)
    y -= 18
    pdf.add_text(50, y, "2. ________________________________________________", 'F1', 10)
    y -= 18
    pdf.add_text(50, y, "3. ________________________________________________", 'F1', 10)
    y -= 35
    pdf.add_text(50, y, "Evening wind-down (circle what I did):", 'F2', 11)
    y -= 20
    pdf.add_text(60, y, "Bath    /    Read    /    Walk    /    Tea    /    Other: _______", 'F1', 10)
    y -= 35
    pdf.add_text(50, y, "Tomorrow I will prioritize:", 'F2', 11)
    y -= 20
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

pdf.save("Book41_Mom_Self_Care_Journal.pdf")
print("Created Book41_Mom_Self_Care_Journal.pdf")
