"""
Book 10: Dark Academia Coloring Book
KDP Interior - 8.5x11 inches (612x792 points)
Gothic library, vintage aesthetics, scholarly motifs
"""
import math
from pdf_utils import PDFDoc

def draw_book_stack(pdf, x, y):
    for i in range(5):
        pdf.add_rect(x - 20 + i*5, y + i*18, 100 - i*8, 15, line_width=1.2)

def draw_candle(pdf, x, y):
    pdf.add_rect(x - 8, y, 16, 50, line_width=1.2)
    pdf.add_line(x, y + 50, x - 5, y + 65, 1)
    pdf.add_line(x, y + 50, x + 5, y + 65, 1)
    pdf.add_line(x - 5, y + 65, x, y + 75, 0.8)
    pdf.add_line(x + 5, y + 65, x, y + 75, 0.8)
    pdf.add_rect(x - 12, y - 5, 24, 8, line_width=1)

def draw_skull(pdf, x, y, s=1):
    pdf.add_rect(x - int(20*s), y, int(40*s), int(35*s), line_width=1.5)
    pdf.add_rect(x - int(15*s), y + int(35*s), int(30*s), int(20*s), line_width=1.2)
    pdf.add_rect(x - int(8*s), y + int(10*s), int(6*s), int(6*s))
    pdf.add_rect(x + int(2*s), y + int(10*s), int(6*s), int(6*s))
    pdf.add_line(x - int(3*s), y, x - int(3*s), y + int(8*s), 0.8)
    pdf.add_line(x + int(3*s), y, x + int(3*s), y + int(8*s), 0.8)

def draw_key(pdf, x, y):
    pdf.add_rect(x, y, 12, 12, line_width=1.2)
    pdf.add_line(x + 12, y + 6, x + 45, y + 6, 1.5)
    pdf.add_line(x + 35, y + 6, x + 35, y, 1)
    pdf.add_line(x + 40, y + 6, x + 40, y + 2, 1)

def draw_illustration(pdf, theme):
    cx = 306
    if theme == "library":
        for shelf_y in range(250, 600, 80):
            pdf.add_line(100, shelf_y, 512, shelf_y, 2)
            for bx in range(110, 500, 30):
                bh = 50 + (bx % 20)
                pdf.add_rect(bx, shelf_y + 5, 22, bh, line_width=1)
        draw_candle(pdf, 150, 620)
        draw_candle(pdf, 462, 620)

    elif theme == "desk":
        pdf.add_rect(130, 250, 352, 20, line_width=2)
        pdf.add_line(150, 250, 150, 180, 1.5)
        pdf.add_line(462, 250, 462, 180, 1.5)
        draw_book_stack(pdf, 170, 280)
        pdf.add_rect(300, 280, 80, 55, line_width=1.2)
        pdf.add_line(340, 280, 340, 335, 0.8)
        draw_candle(pdf, 430, 275)
        pdf.add_rect(200, 400, 212, 160, line_width=1.5)
        pdf.add_line(200, 480, 412, 480, 0.8)
        pdf.add_line(306, 400, 306, 560, 0.8)

    elif theme == "skull":
        draw_skull(pdf, 306, 350, 3)
        draw_book_stack(pdf, 150, 300)
        draw_book_stack(pdf, 380, 300)
        draw_candle(pdf, 180, 430)
        draw_candle(pdf, 430, 430)
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            lx = 306 + math.cos(rad) * 150
            ly = 420 + math.sin(rad) * 100
            pdf.add_line(lx, ly, lx + 10, ly + 15, 0.5)

    elif theme == "clock":
        r = 100
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x1 = cx + math.cos(rad) * r
            y1 = 430 + math.sin(rad) * r
            x2 = cx + math.cos(rad) * (r - 10)
            y2 = 430 + math.sin(rad) * (r - 10)
            pdf.add_line(x1, y1, x2, y2, 1.5)
        pdf.add_rect(cx - r - 5, 430 - r - 5, r*2 + 10, r*2 + 10, line_width=2)
        pdf.add_line(cx, 430, cx + 40, 430 + 60, 2)
        pdf.add_line(cx, 430, cx - 20, 430 + 80, 1.5)
        draw_book_stack(pdf, 150, 280)
        draw_key(pdf, 250, 280)

    elif theme == "window":
        pdf.add_rect(180, 250, 252, 380, line_width=2.5)
        pdf.add_line(306, 250, 306, 630, 1.5)
        pdf.add_line(180, 440, 432, 440, 1.5)
        for wy in range(260, 620, 20):
            pdf.add_line(185, wy, 303, wy, 0.2, gray=0.5)
            pdf.add_line(309, wy, 429, wy, 0.2, gray=0.5)
        pdf.add_rect(150, 235, 312, 20, line_width=1.5)
        draw_candle(pdf, 130, 260)
        draw_candle(pdf, 490, 260)

    elif theme == "potion":
        pdf.add_rect(270, 300, 72, 120, line_width=1.5)
        pdf.add_rect(285, 420, 42, 20, line_width=1.2)
        pdf.add_rect(295, 440, 22, 12, line_width=1)
        for by in range(310, 410, 15):
            pdf.add_line(275, by, 337, by, 0.3, gray=0.4)
        pdf.add_rect(160, 300, 50, 80, line_width=1.2)
        pdf.add_rect(400, 320, 60, 100, line_width=1.2)
        draw_skull(pdf, 306, 500, 1.5)
        draw_book_stack(pdf, 420, 440)

    elif theme == "raven":
        pdf.add_rect(250, 400, 112, 70, line_width=2)
        pdf.add_line(250, 470, 230, 500, 1.5)
        pdf.add_line(362, 470, 380, 500, 1.5)
        pdf.add_line(230, 500, 210, 490, 1.5)
        pdf.add_line(250, 400, 280, 350, 1.5)
        pdf.add_line(362, 400, 332, 350, 1.5)
        pdf.add_line(280, 350, 332, 350, 1.5)
        pdf.add_rect(290, 440, 8, 8)
        draw_book_stack(pdf, 150, 300)
        draw_key(pdf, 400, 380)

    elif theme == "arch":
        pdf.add_line(180, 200, 180, 550, 2)
        pdf.add_line(432, 200, 432, 550, 2)
        pdf.add_line(180, 550, 250, 630, 2)
        pdf.add_line(250, 630, 362, 630, 2)
        pdf.add_line(362, 630, 432, 550, 2)
        for sy in range(210, 540, 25):
            pdf.add_line(185, sy, 190, sy, 0.8)
            pdf.add_line(427, sy, 432, sy, 0.8)
        draw_candle(pdf, 220, 210)
        draw_candle(pdf, 392, 210)

    else:
        draw_book_stack(pdf, 200, 350)
        draw_book_stack(pdf, 350, 380)
        draw_candle(pdf, 306, 420)
        draw_key(pdf, 250, 300)

def create_dark_academia():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "DARK", font='F5', size=48)
    pdf.add_centered_text(565, "ACADEMIA", font='F5', size=48)
    pdf.add_centered_text(510, "COLORING BOOK", font='F4', size=24)
    pdf.add_rect(60, 60, 492, 700, line_width=2.5)
    pdf.add_rect(65, 65, 482, 690, line_width=0.5)
    pdf.add_line(200, 490, 412, 490, 1.5)
    pdf.add_centered_text(455, "Gothic Libraries | Vintage Desks | Ancient Keys", font='F4', size=12)
    pdf.add_centered_text(430, "Candles | Skulls | Ravens | Archways", font='F4', size=12)
    pdf.add_centered_text(395, "30 Illustrations for Adults", font='F4', size=12)
    pdf.add_centered_text(290, "By", font='F4', size=12)
    pdf.add_centered_text(265, "Daniel Tesfamariam", font='F5', size=18)
    pdf.add_centered_text(160, "Single-Sided Pages", font='F4', size=11)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(550, "Dark Academia Coloring Book", font='F5', size=14)
    pdf.add_centered_text(525, "By Daniel Tesfamariam", font='F5', size=12)
    pdf.add_centered_text(490, "Copyright 2026 Daniel Tesfamariam.", font='F4', size=10)
    pdf.add_centered_text(465, "ISBN: _______________", font='F4', size=10)
    pdf.add_centered_text(440, "Published via Amazon KDP", font='F4', size=10)

    # --- COLORING PAGES ---
    themes = [
        ("The Forbidden Library", "library"),
        ("Scholar's Desk at Midnight", "desk"),
        ("Memento Mori", "skull"),
        ("The Grandfather Clock", "clock"),
        ("Rain on the Gothic Window", "window"),
        ("The Apothecary's Shelf", "potion"),
        ("The Raven's Perch", "raven"),
        ("The Stone Archway", "arch"),
        ("Candlelit Study", "desk"),
        ("Secrets & Keys", "clock"),
        ("The Old Bookshop", "library"),
        ("Alchemist's Table", "potion"),
        ("The Tower Window", "window"),
        ("Whispers of the Past", "skull"),
        ("The Hidden Passage", "arch"),
    ]

    for i, (title, theme) in enumerate(themes):
        pdf.new_page()
        pdf.add_centered_text(396, "This page intentionally left blank.", font='F4', size=9, gray=0.5)

        pdf.new_page()
        pdf.add_rect(50, 50, 512, 692, line_width=1.5)
        pdf.add_centered_text(65, title, font='F4', size=11)
        draw_illustration(pdf, theme)
        pdf.add_centered_text(35, f"{i + 1}", font='F4', size=9)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(500, "Thank You", font='F5', size=26)
    pdf.add_centered_text(460, "for exploring the shadows with us.", font='F4', size=13)
    pdf.add_centered_text(420, "If you enjoyed this book, please leave a review.", font='F4', size=11)
    pdf.add_centered_text(370, "Also available:", font='F5', size=12)
    pdf.add_centered_text(345, "- Cottagecore Coloring Book", font='F4', size=11)
    pdf.add_centered_text(323, "- Gothic Architecture Coloring Book", font='F4', size=11)
    pdf.add_centered_text(301, "- Witchy Coloring Book", font='F4', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book10_Dark_Academia_Coloring.pdf')
    print("Book 10 created: Book10_Dark_Academia_Coloring.pdf")

if __name__ == '__main__':
    create_dark_academia()
