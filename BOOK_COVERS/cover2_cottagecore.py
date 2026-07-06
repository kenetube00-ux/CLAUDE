"""
Cover 2: Cottagecore Coloring Book
KDP Cover - 8.5x11 (612x792 points) - Elegant, white background with line art
"""
import sys
import math
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def draw_cover_flower(pdf, x, y, size):
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        px = x + math.cos(rad) * size
        py = y + math.sin(rad) * size
        pdf.add_line(x, y, px, py, 1)
    s = size // 4
    pdf.add_rect(x - s, y - s, s * 2, s * 2)

def create_cover():
    pdf = PDFDoc(612, 792)
    pdf.new_page()

    # Elegant double border
    pdf.add_rect(20, 20, 572, 752, line_width=2.5)
    pdf.add_rect(28, 28, 556, 736, line_width=0.5)

    # Corner flowers
    for cx, cy in [(60, 740), (552, 740), (60, 52), (552, 52)]:
        draw_cover_flower(pdf, cx, cy, 18)

    # Floral arc above title
    for angle in range(160, 380, 25):
        rad = math.radians(angle)
        fx = 306 + math.cos(rad) * 160
        fy = 620 + math.sin(rad) * 60
        if 50 < fx < 570 and fy > 580:
            draw_cover_flower(pdf, fx, fy, 12)

    # Main title
    pdf.add_centered_text(640, "Cottagecore", font='F5', size=50)
    pdf.add_centered_text(580, "COLORING BOOK", font='F4', size=30)
    pdf.add_centered_text(535, "A Peaceful Escape into Nature", font='F4', size=16)

    # Divider
    pdf.add_line(180, 515, 432, 515, 1.5)

    # Cottage illustration
    pdf.add_rect(220, 300, 172, 140)
    pdf.add_line(210, 440, 306, 520, 1.5)
    pdf.add_line(306, 520, 402, 440, 1.5)
    pdf.add_rect(275, 300, 35, 60)
    pdf.add_rect(340, 370, 35, 35)
    pdf.add_line(340, 387, 375, 387, 0.5)
    pdf.add_line(357, 370, 357, 405, 0.5)
    # Path
    pdf.add_line(280, 300, 265, 240, 1)
    pdf.add_line(320, 300, 335, 240, 1)
    # Garden flowers
    for fx in range(180, 440, 35):
        draw_cover_flower(pdf, fx, 265, 10)

    # Ground
    pdf.add_line(130, 240, 482, 240, 1)

    # Features text
    pdf.add_centered_text(200, "30 Relaxing Illustrations | Single-Sided Pages", font='F4', size=12)
    pdf.add_centered_text(180, "Wildflowers | Cottages | Gardens | Animals", font='F4', size=12)

    # For Adults badge
    pdf.add_rect(225, 130, 162, 28, line_width=1.5)
    pdf.add_centered_text(138, "For Adults & Teens", font='F5', size=14)

    # Author
    pdf.add_centered_text(80, "Daniel Tesfamariam", font='F5', size=20)
    pdf.add_line(200, 70, 412, 70, 1)

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover2_Cottagecore_Coloring.pdf')
    print("Cover 2 created: Cover2_Cottagecore_Coloring.pdf")

if __name__ == '__main__':
    create_cover()
