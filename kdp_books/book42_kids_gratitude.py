"""Book 42: Kids Gratitude Journal"""
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)

# Title page
pdf.new_page()
pdf.add_centered_text(420, "MY GRATITUDE JOURNAL", 'F2', 22)
pdf.add_centered_text(385, "FOR KIDS", 'F2', 18)
pdf.add_centered_text(350, "Ages 5-10", 'F4', 14, 0.3)
pdf.add_line(130, 330, 302, 330, 1, 0.5)
pdf.add_centered_text(200, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(400, "My Gratitude Journal for Kids", 'F2', 14)
pdf.add_centered_text(370, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(350, "All rights reserved.", 'F1', 10)

# How to Use page
pdf.new_page()
pdf.add_centered_text(580, "How to Use This Journal", 'F2', 16)
pdf.add_text(50, 540, "Every day, take a few minutes to fill in one page.", 'F1', 12)
pdf.add_text(50, 510, "Think about the good things that happened today.", 'F1', 12)
pdf.add_text(50, 480, "Write or draw what made you smile!", 'F1', 12)
pdf.add_text(50, 450, "Remember: there is ALWAYS something to be thankful for.", 'F1', 12)
pdf.add_text(50, 410, "Tips:", 'F2', 12)
pdf.add_text(60, 385, "- It can be something big or small", 'F1', 11)
pdf.add_text(60, 363, "- A person, a pet, food, sunshine, a hug!", 'F1', 11)
pdf.add_text(60, 341, "- Draw pictures if you like!", 'F1', 11)
pdf.add_text(60, 319, "- Have fun with it!", 'F1', 11)

# 90 daily pages
for day in range(1, 91):
    pdf.new_page()
    pdf.add_text(50, 610, f"Day {day}", 'F2', 14)
    pdf.add_text(300, 610, "Date: ___________", 'F1', 10)
    pdf.add_line(50, 600, 382, 600, 0.5, 0.5)

    y = 570
    pdf.add_text(50, y, "Today I am thankful for:", 'F2', 12)
    y -= 25
    pdf.add_text(60, y, "1. ____________________________________________", 'F1', 11)
    y -= 22
    pdf.add_text(60, y, "2. ____________________________________________", 'F1', 11)
    y -= 22
    pdf.add_text(60, y, "3. ____________________________________________", 'F1', 11)

    y -= 35
    pdf.add_text(50, y, "Someone who made me happy today:", 'F2', 12)
    y -= 20
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 35
    pdf.add_text(50, y, "Draw a happy moment:", 'F2', 12)
    y -= 10
    pdf.add_rect(116, y - 150, 200, 150, 1, 0.4)

    y -= 170
    pdf.add_text(50, y, "One kind thing I did today:", 'F2', 12)
    y -= 20
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 35
    pdf.add_text(50, y, "Tomorrow I look forward to:", 'F2', 12)
    y -= 20
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

pdf.save("Book42_Kids_Gratitude_Journal.pdf")
print("Created Book42_Kids_Gratitude_Journal.pdf")
