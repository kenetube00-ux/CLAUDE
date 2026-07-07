"""Book 49: Women's Prayer Journal - 90 Days of Grace"""
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)

# Title page
pdf.new_page()
pdf.add_centered_text(420, "A WOMAN'S PRAYER JOURNAL", 'F5', 20)
pdf.add_centered_text(380, "90 Days of Grace", 'F4', 16, 0.3)
pdf.add_line(130, 360, 302, 360, 1, 0.5)
pdf.add_centered_text(200, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(400, "A Woman's Prayer Journal", 'F5', 14)
pdf.add_centered_text(370, "90 Days of Grace", 'F4', 12)
pdf.add_centered_text(340, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(320, "All rights reserved.", 'F1', 10)

# 90 daily pages
for day in range(1, 91):
    pdf.new_page()
    pdf.add_text(50, 610, f"Day {day}", 'F5', 14)
    pdf.add_text(300, 610, "Date: _______________", 'F4', 10)
    pdf.add_line(50, 598, 382, 598, 0.5, 0.5)

    y = 572
    pdf.add_text(50, y, "Today's Scripture:", 'F5', 11)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 28
    pdf.add_text(50, y, "Lord, I pray for:", 'F5', 11)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 28
    pdf.add_text(50, y, "I surrender:", 'F5', 11)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 28
    pdf.add_text(50, y, "I am grateful for:", 'F5', 11)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 28
    pdf.add_text(50, y, "God is showing me:", 'F5', 11)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 28
    pdf.add_text(50, y, "My prayer for my family:", 'F5', 11)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 30
    pdf.add_centered_text(y, "Amen", 'F4', 12, 0.4)

pdf.save("Book49_Womens_Prayer_Journal.pdf")
print("Created Book49_Womens_Prayer_Journal.pdf")
