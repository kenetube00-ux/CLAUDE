"""
Book 2: Cottagecore Coloring Book
KDP Interior - 8.5x11 inches (612x792 points)
WHITE background, BLACK line art
"""
import math
from pdf_utils import PDFDoc

def draw_flower(pdf, x, y, size):
    """Draw a simple flower at given position."""
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        px = x + math.cos(rad) * size
        py = y + math.sin(rad) * size
        pdf.add_line(x, y, px, py, 0.8)
    s = size // 4
    pdf.add_rect(x - s, y - s, s * 2, s * 2)

def draw_illustration(pdf, theme, index):
    """Draw cottagecore-themed line art illustrations."""
    cx = 306

    if theme == "cottage":
        pdf.add_rect(200, 280, 212, 180)
        pdf.add_line(200, 460, 306, 560, 1.5)
        pdf.add_line(306, 560, 412, 460, 1.5)
        pdf.add_rect(270, 280, 40, 70)
        pdf.add_rect(340, 360, 45, 45)
        pdf.add_line(340, 382, 385, 382, 0.5)
        pdf.add_line(362, 360, 362, 405, 0.5)
        pdf.add_rect(360, 500, 25, 50)
        pdf.add_line(270, 280, 250, 180, 1)
        pdf.add_line(310, 280, 330, 180, 1)
        for fx in range(220, 400, 30):
            draw_flower(pdf, fx, 260, 8)

    elif theme == "flowers":
        for angle in range(0, 360, 40):
            rad = math.radians(angle)
            fx = cx + math.cos(rad) * 80
            fy = 420 + math.sin(rad) * 80
            draw_flower(pdf, fx, fy, 20)
            pdf.add_line(cx, 320, fx, fy, 1)
        pdf.add_rect(cx - 15, 300, 30, 40)

    elif theme == "mushroom":
        for mx, my, sz in [(250, 320, 40), (306, 340, 55), (370, 310, 35)]:
            pdf.add_rect(mx - sz//4, my - sz, sz//2, sz)
            pdf.add_line(mx - sz, my, mx, my + sz, 1.5)
            pdf.add_line(mx + sz, my, mx, my + sz, 1.5)
            pdf.add_line(mx - sz, my, mx + sz, my, 1.5)
        pdf.add_line(150, 270, 462, 270, 1)
        for gx in range(160, 460, 15):
            pdf.add_line(gx, 270, gx + 5, 285, 0.5)

    elif theme == "teapot":
        pdf.add_rect(240, 370, 132, 100)
        pdf.add_rect(280, 470, 52, 15)
        pdf.add_line(240, 420, 210, 440, 1.5)
        pdf.add_line(372, 420, 400, 450, 1.5)
        pdf.add_line(400, 450, 400, 400, 1.5)
        pdf.add_line(400, 400, 372, 410, 1.5)
        pdf.add_rect(200, 300, 60, 40)
        pdf.add_rect(350, 300, 60, 40)
        pdf.add_line(140, 295, 472, 295, 1.5)

    elif theme == "herbs":
        pdf.add_line(120, 370, 492, 370, 2)
        for px, label in [(170, "Basil"), (270, "Mint"), (370, "Thyme")]:
            pdf.add_rect(px, 375, 60, 80)
            for s in range(4):
                pdf.add_line(px + 30, 455, px + 15 + s*12, 500 + s*15, 1)
            pdf.add_text(px + 10, 380, label, font='F4', size=9)

    elif theme == "bee":
        pdf.add_rect(280, 440, 52, 30)
        pdf.add_rect(270, 440, 15, 30)
        for s in range(3):
            pdf.add_line(285 + s*15, 440, 285 + s*15, 470, 1)
        pdf.add_line(295, 470, 280, 500, 1)
        pdf.add_line(310, 470, 320, 500, 1)
        for lx in range(180, 440, 50):
            pdf.add_line(lx, 220, lx + 10, 420, 1)
            for ly in range(300, 420, 15):
                pdf.add_rect(lx + 5, ly, 12, 8)

    elif theme == "path":
        pdf.add_line(250, 170, 220, 320, 1.5)
        pdf.add_line(220, 320, 280, 470, 1.5)
        pdf.add_line(280, 470, 250, 600, 1.5)
        pdf.add_line(350, 170, 380, 320, 1.5)
        pdf.add_line(380, 320, 320, 470, 1.5)
        pdf.add_line(320, 470, 350, 600, 1.5)
        for fy in range(220, 580, 60):
            draw_flower(pdf, 180, fy, 12)
            draw_flower(pdf, 420, fy, 12)

    elif theme == "can":
        pdf.add_rect(230, 320, 120, 100)
        pdf.add_line(230, 370, 190, 400, 1.5)
        pdf.add_line(350, 390, 380, 430, 1.5)
        for fx in range(240, 350, 25):
            draw_flower(pdf, fx, 450 + (fx % 30), 15)
            pdf.add_line(fx, 420, fx, 450 + (fx % 30) - 15, 0.8)

    elif theme == "fox":
        pdf.add_rect(240, 320, 130, 80)
        pdf.add_rect(270, 400, 70, 60)
        pdf.add_line(280, 460, 275, 490, 1.5)
        pdf.add_line(275, 490, 295, 470, 1.5)
        pdf.add_line(320, 460, 335, 490, 1.5)
        pdf.add_line(335, 490, 325, 470, 1.5)
        pdf.add_line(370, 360, 420, 400, 1.5)
        pdf.add_line(420, 400, 400, 370, 1.5)
        for lx in [255, 285, 330, 355]:
            pdf.add_line(lx, 320, lx, 280, 1.5)
        for fx in range(160, 460, 40):
            draw_flower(pdf, fx, 270, 10)

    elif theme == "butterfly":
        for bx, by, sz in [(220, 450, 40), (350, 500, 35), (280, 370, 45)]:
            pdf.add_rect(bx - sz, by, sz, sz * 2 // 3)
            pdf.add_rect(bx, by, sz, sz * 2 // 3)
            pdf.add_line(bx, by - 5, bx, by + sz * 2 // 3 + 5, 2)
        for dx in range(160, 460, 35):
            draw_flower(pdf, dx, 270, 12)

    elif theme == "bridge":
        pdf.add_line(150, 370, 250, 470, 2)
        pdf.add_line(250, 470, 362, 470, 2)
        pdf.add_line(362, 470, 462, 370, 2)
        for wy in range(270, 320, 12):
            pdf.add_line(130, wy, 480, wy, 0.3, gray=0.4)

    elif theme == "window":
        pdf.add_rect(180, 300, 252, 320, line_width=3)
        pdf.add_line(306, 300, 306, 620, 2)
        pdf.add_line(180, 460, 432, 460, 2)
        pdf.add_rect(170, 270, 272, 35, line_width=2)
        for fx in range(190, 430, 30):
            draw_flower(pdf, fx, 330, 12)
            pdf.add_line(fx, 305, fx, 318, 0.5)

    elif theme == "basket":
        pdf.add_rect(210, 320, 192, 100)
        for wy in range(330, 415, 15):
            pdf.add_line(215, wy, 397, wy, 0.5)
        for wx in range(225, 400, 20):
            pdf.add_line(wx, 320, wx, 420, 0.5)
        pdf.add_line(250, 420, 306, 520, 1.5)
        pdf.add_line(362, 420, 306, 520, 1.5)

    elif theme == "sunflower":
        r = 60
        for angle in range(0, 360, 20):
            rad = math.radians(angle)
            px = cx + math.cos(rad) * r
            py = 450 + math.sin(rad) * r
            pdf.add_line(cx, 450, px, py, 1.5)
        pdf.add_rect(cx - 30, 420, 60, 60)
        pdf.add_line(cx, 390, cx, 220, 2)
        pdf.add_line(cx, 320, cx - 50, 340, 1)
        pdf.add_line(cx, 280, cx + 50, 300, 1)

    else:  # "reading"
        pdf.add_rect(200, 280, 212, 180)
        pdf.add_rect(260, 470, 92, 60)
        pdf.add_line(306, 470, 306, 530, 1)
        pdf.add_line(460, 270, 460, 540, 1.5)
        pdf.add_rect(440, 545, 40, 30)
        pdf.add_rect(160, 240, 292, 20)

def create_cottagecore_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "Cottagecore", font='F5', size=48)
    pdf.add_centered_text(590, "COLORING BOOK", font='F4', size=28)
    pdf.add_centered_text(540, "A Peaceful Escape into Nature", font='F4', size=16)
    pdf.add_rect(50, 50, 512, 692, line_width=2)
    pdf.add_centered_text(470, "30 Relaxing Illustrations", font='F4', size=14)
    pdf.add_centered_text(440, "Wildflowers | Cottages | Gardens | Animals", font='F4', size=12)
    pdf.add_centered_text(400, "Single-Sided Pages", font='F4', size=11)
    pdf.add_line(250, 370, 362, 370, 1)
    pdf.add_centered_text(340, "For Adults & Teens", font='F4', size=13)
    pdf.add_centered_text(240, "By", font='F4', size=12)
    pdf.add_centered_text(215, "Daniel Tesfamariam", font='F5', size=18)
    pdf.add_centered_text(150, "Volume 1", font='F4', size=14)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(600, "Cottagecore Coloring Book - Volume 1", font='F5', size=14)
    pdf.add_centered_text(575, "By Daniel Tesfamariam", font='F5', size=12)
    pdf.add_centered_text(545, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F4', size=10)
    pdf.add_centered_text(510, "ISBN: _______________", font='F4', size=10)
    pdf.add_centered_text(485, "Published via Amazon KDP", font='F4', size=10)

    # --- COLORING PAGES ---
    themes = [
        ("A Cozy Cottage in the Meadow", "cottage"),
        ("Wildflower Bouquet", "flowers"),
        ("Mushroom Forest", "mushroom"),
        ("Garden Tea Party", "teapot"),
        ("Rustic Kitchen Herbs", "herbs"),
        ("Honeybee & Lavender", "bee"),
        ("Winding Garden Path", "path"),
        ("Vintage Watering Can", "can"),
        ("Woodland Fox in Flowers", "fox"),
        ("Butterflies & Daisies", "butterfly"),
        ("Stone Bridge Over Stream", "bridge"),
        ("Herb Garden Window Box", "window"),
        ("Basket of Fresh Vegetables", "basket"),
        ("Sunflower Field", "sunflower"),
        ("Cozy Reading Nook", "reading"),
    ]

    for i, (title, theme) in enumerate(themes):
        # Blank back page
        pdf.new_page()
        pdf.add_centered_text(396, "This page intentionally left blank.", font='F4', size=9, gray=0.5)

        # Coloring page
        pdf.new_page()
        pdf.add_rect(50, 50, 512, 692, line_width=1.5)
        pdf.add_centered_text(65, title, font='F4', size=11)
        draw_illustration(pdf, theme, i)
        pdf.add_centered_text(35, f"{i + 1}", font='F4', size=9)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(500, "Thank You!", font='F5', size=28)
    pdf.add_centered_text(450, "If you enjoyed this book, please leave a review.", font='F4', size=12)
    pdf.add_centered_text(420, "Your feedback helps create more books like this!", font='F4', size=12)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book2_Cottagecore_Coloring_Book.pdf')
    print("Book 2 created: Book2_Cottagecore_Coloring_Book.pdf")

if __name__ == '__main__':
    create_cottagecore_book()
