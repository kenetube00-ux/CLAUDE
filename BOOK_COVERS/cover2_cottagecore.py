"""
Cover 2: Cottagecore Coloring Book
KDP Cover - 8.5x11 inches with bleed = 8.75x11.25 (630x810 points)
Front cover only - Elegant nature/cottage aesthetic
"""
import sys
import math
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def draw_cover_flower(pdf, x, y, size, petal_gray=0.75):
    """Draw decorative flower for cover."""
    pdf.set_gray(petal_gray)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        px = x + math.cos(rad) * size
        py = y + math.sin(rad) * size
        pdf.add_line(x, y, px, py, 1.2)
        # Petal tips
        px2 = x + math.cos(math.radians(angle + 15)) * (size * 0.7)
        py2 = y + math.sin(math.radians(angle + 15)) * (size * 0.7)
        pdf.add_line(px, py, px2, py2, 0.8)
    pdf.reset_color()
    # Center
    pdf.set_gray(petal_gray - 0.15)
    s = size // 4
    pdf.add_filled_rect(x - s, y - s, s * 2, s * 2, gray=petal_gray - 0.1)
    pdf.reset_color()

def draw_leaf(pdf, x, y, angle_deg, size):
    """Draw a simple leaf shape."""
    rad = math.radians(angle_deg)
    ex = x + math.cos(rad) * size
    ey = y + math.sin(rad) * size
    pdf.set_gray(0.6)
    pdf.add_line(x, y, ex, ey, 1.5)
    # Leaf sides
    mx = (x + ex) / 2
    my = (y + ey) / 2
    perp = math.radians(angle_deg + 90)
    lx = mx + math.cos(perp) * (size * 0.3)
    ly = my + math.sin(perp) * (size * 0.3)
    pdf.add_line(x, y, lx, ly, 0.8)
    pdf.add_line(lx, ly, ex, ey, 0.8)
    lx2 = mx + math.cos(perp + math.pi) * (size * 0.3)
    ly2 = my + math.sin(perp + math.pi) * (size * 0.3)
    pdf.add_line(x, y, lx2, ly2, 0.8)
    pdf.add_line(lx2, ly2, ex, ey, 0.8)
    pdf.reset_color()

def create_cover():
    pdf = PDFDoc(630, 810)
    pdf.new_page()

    # === CREAM/WARM BACKGROUND ===
    pdf.add_filled_rect(0, 0, 630, 810, gray=0.92)

    # === ELEGANT DOUBLE BORDER ===
    pdf.set_gray(0.45)
    pdf.add_rect(20, 20, 590, 770, line_width=2.5)
    pdf.add_rect(28, 28, 574, 754, line_width=0.5)
    pdf.reset_color()

    # === CORNER FLORAL DECORATIONS ===
    corners = [(60, 760), (570, 760), (60, 50), (570, 50)]
    for cx, cy in corners:
        draw_cover_flower(pdf, cx, cy, 22, 0.55)
        draw_leaf(pdf, cx, cy, 45 if cx < 300 else 135, 30)

    # === FLORAL WREATH AROUND TITLE (top arc) ===
    for angle in range(150, 400, 25):
        rad = math.radians(angle)
        fx = 315 + math.cos(rad) * 180
        fy = 580 + math.sin(rad) * 80
        if 50 < fx < 600 and fy > 530:
            draw_cover_flower(pdf, fx, fy, 14, 0.6)

    # === MAIN TITLE ===
    pdf.set_gray(0.2)
    pdf.add_text(135, 610, "Cottagecore", font='TimesBold', size=54)
    pdf.reset_color()

    pdf.set_gray(0.3)
    pdf.add_text(120, 555, "COLORING BOOK", font='TimesRoman', size=34)
    pdf.reset_color()

    # === SUBTITLE ===
    pdf.set_gray(0.35)
    pdf.add_text(140, 510, "A Peaceful Escape into Nature", font='TimesRoman', size=17)
    pdf.reset_color()

    # === DECORATIVE DIVIDER ===
    pdf.set_gray(0.5)
    pdf.add_line(180, 495, 450, 495, 1.5)
    # Small diamond in center
    pdf.add_line(310, 495, 315, 502, 1)
    pdf.add_line(315, 502, 320, 495, 1)
    pdf.add_line(320, 495, 315, 488, 1)
    pdf.add_line(315, 488, 310, 495, 1)
    pdf.reset_color()

    # === CENTRAL ILLUSTRATION - Cottage Scene ===
    # Cottage
    pdf.set_gray(0.35)
    # Main structure
    pdf.add_rect(230, 280, 170, 120, line_width=2)
    # Roof
    pdf.add_line(220, 400, 315, 470, 2)
    pdf.add_line(315, 470, 410, 400, 2)
    # Door
    pdf.add_rect(285, 280, 40, 65, line_width=1.5)
    pdf.add_rect(300, 310, 4, 4)  # doorknob
    # Windows
    pdf.add_rect(240, 340, 35, 35, line_width=1.5)
    pdf.add_line(257, 340, 257, 375, 0.8)
    pdf.add_line(240, 357, 275, 357, 0.8)
    pdf.add_rect(345, 340, 35, 35, line_width=1.5)
    pdf.add_line(362, 340, 362, 375, 0.8)
    pdf.add_line(345, 357, 380, 357, 0.8)
    # Chimney
    pdf.add_rect(350, 435, 25, 40, line_width=1.5)
    # Smoke curls
    pdf.add_line(362, 475, 358, 485, 0.8)
    pdf.add_line(358, 485, 365, 495, 0.8)
    # Path
    pdf.add_line(295, 280, 280, 230, 1.2)
    pdf.add_line(330, 280, 345, 230, 1.2)
    pdf.reset_color()

    # Garden flowers around cottage
    flower_positions = [
        (180, 300), (200, 270), (160, 260), (430, 300),
        (450, 280), (470, 260), (220, 240), (400, 240),
    ]
    for fx, fy in flower_positions:
        draw_cover_flower(pdf, fx, fy, 12, 0.55)
        draw_leaf(pdf, fx, fy - 12, 270, 15)

    # Ground line
    pdf.set_gray(0.5)
    pdf.add_line(120, 230, 510, 230, 1)
    pdf.reset_color()

    # === FEATURES TEXT ===
    pdf.set_gray(0.3)
    pdf.add_text(155, 190, "30 Relaxing Illustrations | Single-Sided Pages", font='TimesRoman', size=13)
    pdf.add_text(160, 168, "Wildflowers | Cottages | Gardens | Animals", font='TimesRoman', size=13)
    pdf.reset_color()

    # === FOR ADULTS & TEENS ===
    pdf.add_filled_rect(220, 125, 190, 30, gray=0.45)
    pdf.set_gray(1)
    pdf.add_text(245, 133, "For Adults & Teens", font='TimesBold', size=16)
    pdf.reset_color()

    # === AUTHOR NAME ===
    pdf.set_gray(0.2)
    pdf.add_text(185, 75, "Daniel Tesfamariam", font='TimesBold', size=22)
    pdf.reset_color()

    # === BOTTOM DECORATIVE FLOURISH ===
    pdf.set_gray(0.5)
    pdf.add_line(250, 60, 380, 60, 1)
    pdf.reset_color()

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover2_Cottagecore_Coloring.pdf')
    print("Cover 2 created: Cover2_Cottagecore_Coloring.pdf")

if __name__ == '__main__':
    create_cover()
