"""Book 46: Kids Handwriting Practice"""
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)

# Title page
pdf.new_page()
pdf.add_centered_text(500, "HANDWRITING PRACTICE", 'F2', 26)
pdf.add_centered_text(460, "FOR KIDS", 'F2', 20)
pdf.add_centered_text(420, "Ages 4-7", 'F4', 16, 0.3)
pdf.add_line(180, 400, 432, 400, 1, 0.5)
pdf.add_centered_text(250, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(500, "Handwriting Practice for Kids", 'F2', 14)
pdf.add_centered_text(470, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(450, "All rights reserved.", 'F1', 10)


# Words starting with each letter
words = [
    "Apple", "Ball", "Cat", "Dog", "Egg", "Fish", "Goat", "Hat",
    "Ice", "Jar", "Kite", "Lion", "Moon", "Nest", "Owl", "Pen",
    "Queen", "Rain", "Sun", "Tree", "Umbrella", "Van", "Water",
    "X-ray", "Yarn", "Zebra"
]

# 26 letter pages (A-Z)
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    pdf.new_page()
    lower = letter.lower()
    word = words[i]

    # Large uppercase letter
    pdf.add_text(80, 700, letter, 'F2', 72)
    # Large lowercase letter
    pdf.add_text(200, 700, lower, 'F2', 72)

    # Dotted trace line for uppercase (simulated with gray text)
    pdf.add_text(80, 620, f"{letter}  {letter}  {letter}  {letter}", 'F1', 36, 0.7)

    # Practice lines for uppercase
    y = 580
    for _ in range(2):
        pdf.add_line(60, y, 552, y, 0.5, 0.6)
        y -= 30
        pdf.add_line(60, y, 552, y, 0.5, 0.8)
        y -= 20

    # Dotted trace line for lowercase
    y -= 10
    pdf.add_text(80, y, f"{lower}  {lower}  {lower}  {lower}  {lower}", 'F1', 36, 0.7)

    # Practice lines for lowercase
    y -= 40
    for _ in range(2):
        pdf.add_line(60, y, 552, y, 0.5, 0.6)
        y -= 30
        pdf.add_line(60, y, 552, y, 0.5, 0.8)
        y -= 20

    # Word example
    y -= 20
    pdf.add_text(60, y, f"{letter} is for {word}", 'F2', 18)
    y -= 30
    # Word trace
    pdf.add_text(60, y, word, 'F1', 24, 0.7)
    y -= 35
    pdf.add_line(60, y, 552, y, 0.5, 0.6)
    y -= 30
    pdf.add_line(60, y, 552, y, 0.5, 0.6)

pdf.save("Book46_Kids_Handwriting_Practice.pdf")
print("Created Book46_Kids_Handwriting_Practice.pdf")
