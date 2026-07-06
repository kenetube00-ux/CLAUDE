"""
Book 2: Cottagecore Coloring Book
KDP Interior - 8.5x11 inches (612x792 points)
Single-sided coloring pages with decorative line art frames
"""
import math
from pdf_utils import PDFDoc

def create_cottagecore_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "Cottagecore", font='TimesBold', size=48)
    pdf.add_centered_text(590, "COLORING BOOK", font='TimesRoman', size=28)
    pdf.add_centered_text(540, "A Peaceful Escape into Nature", font='TimesRoman', size=16)
    # Decorative border
    pdf.add_rect(50, 50, 512, 692, line_width=2)
    pdf.add_rect(55, 55, 502, 682, line_width=0.5)
    pdf.add_centered_text(470, "30 Relaxing Illustrations", font='TimesRoman', size=14)
    pdf.add_centered_text(440, "Wildflowers | Cottages | Gardens | Animals", font='TimesRoman', size=12)
    pdf.add_centered_text(400, "Single-Sided Pages for Easy Removal", font='TimesRoman', size=11)
    pdf.add_centered_text(360, "Printed on Premium Quality Paper", font='TimesRoman', size=11)
    # Small decorative element
    pdf.add_line(250, 330, 362, 330, 1)
    pdf.add_centered_text(300, "For Adults & Teens", font='TimesRoman', size=13)
    pdf.add_centered_text(120, "Volume 1", font='TimesRoman', size=14)


    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "Cottagecore Coloring Book - Volume 1", font='TimesBold', size=14)
    pdf.add_centered_text(570, "Copyright 2026. All Rights Reserved.", font='TimesRoman', size=10)
    pdf.add_centered_text(540, "No part of this book may be reproduced without written permission.", font='TimesRoman', size=9)
    pdf.add_centered_text(500, "ISBN: _______________", font='TimesRoman', size=10)
    pdf.add_centered_text(470, "Published via Amazon KDP", font='TimesRoman', size=10)
    pdf.add_centered_text(420, "Tips for Best Results:", font='TimesBold', size=12)
    tips = [
        "- Use colored pencils, gel pens, or fine markers",
        "- Place a blank sheet behind the page to prevent bleed-through",
        "- Start with lighter colors and layer darker shades",
        "- Each coloring page is single-sided for easy framing",
    ]
    y = 390
    for tip in tips:
        pdf.add_centered_text(y, tip, font='TimesRoman', size=11)
        y -= 22

    # --- COLORING PAGES (15 themed illustrations as line art) ---
    themes = [
        ("A Cozy Cottage in the Meadow", "cottage"),
        ("Wildflower Bouquet", "flowers"),
        ("Mushroom Forest", "mushroom"),
        ("Garden Tea Party", "teapot"),
        ("Rustic Kitchen Herbs", "herbs"),
        ("Honeybee & Lavender", "bee"),
        ("Winding Garden Path", "path"),
        ("Vintage Watering Can with Flowers", "can"),
        ("Woodland Fox in Flowers", "fox"),
        ("Butterflies & Daisies", "butterfly"),
        ("Stone Bridge Over Stream", "bridge"),
        ("Herb Garden Window Box", "window"),
        ("Basket of Fresh Vegetables", "basket"),
        ("Sunflower Field at Sunset", "sunflower"),
        ("Cozy Reading Nook", "reading"),
    ]


    for i, (title, theme) in enumerate(themes):
        # Blank back page (single-sided)
        pdf.new_page()
        pdf.add_centered_text(396, "This page intentionally left blank.", font='TimesRoman', size=9)

        # Coloring page
        pdf.new_page()
        # Decorative border frame
        pdf.add_rect(50, 50, 512, 692, line_width=1.5)

        # Corner decorations (small L-shapes)
        for cx, cy in [(55, 735), (555, 735), (55, 57), (555, 57)]:
            pdf.add_line(cx, cy, cx + 15, cy, 1)
            pdf.add_line(cx, cy, cx, cy - 15, 1)

        # Title at bottom
        pdf.add_centered_text(65, title, font='TimesRoman', size=11)

        # Draw themed line art illustration based on theme
        draw_illustration(pdf, theme, i)

        # Page number
        pdf.add_centered_text(35, f"{i + 1}", font='TimesRoman', size=9)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(500, "Thank You!", font='TimesBold', size=28)
    pdf.add_centered_text(450, "Thank you for purchasing this coloring book.", font='TimesRoman', size=14)
    pdf.add_centered_text(420, "If you enjoyed it, please leave a review on Amazon.", font='TimesRoman', size=12)
    pdf.add_centered_text(380, "Your feedback helps create more books like this!", font='TimesRoman', size=12)
    pdf.add_centered_text(320, "Check out our other titles:", font='TimesBold', size=13)
    pdf.add_centered_text(290, "- Dark Academia Coloring Book", font='TimesRoman', size=12)
    pdf.add_centered_text(265, "- Botanical Garden Coloring Book", font='TimesRoman', size=12)
    pdf.add_centered_text(240, "- Cozy Autumn Coloring Book", font='TimesRoman', size=12)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book2_Cottagecore_Coloring_Book.pdf')
    print("Book 2 created: Book2_Cottagecore_Coloring_Book.pdf")


def draw_illustration(pdf, theme, index):
    """Draw cottagecore-themed line art illustrations using geometric shapes."""
    cx, cy = 306, 420  # Center of drawing area

    if theme == "cottage":
        # Simple cottage shape
        pdf.add_rect(200, 250, 212, 180)  # Main body
        pdf.add_line(200, 430, 306, 530, 1.5)  # Roof left
        pdf.add_line(306, 530, 412, 430, 1.5)  # Roof right
        pdf.add_rect(260, 250, 40, 70)  # Door
        pdf.add_rect(340, 330, 45, 45)  # Window
        pdf.add_line(340, 352, 385, 352, 0.5)  # Window cross h
        pdf.add_line(362, 330, 362, 375, 0.5)  # Window cross v
        # Chimney
        pdf.add_rect(360, 480, 25, 50)
        # Path
        pdf.add_line(270, 250, 250, 150, 1)
        pdf.add_line(310, 250, 330, 150, 1)
        # Flowers along path
        for fx in range(220, 400, 30):
            draw_flower(pdf, fx, 230 + (fx % 20), 8)

    elif theme == "flowers":
        # Bouquet of flowers
        for angle in range(0, 360, 40):
            rad = math.radians(angle)
            fx = cx + math.cos(rad) * 80
            fy = cy + math.sin(rad) * 80
            draw_flower(pdf, fx, fy, 20)
        # Stems
        for angle in range(0, 360, 40):
            rad = math.radians(angle)
            fx = cx + math.cos(rad) * 80
            fy = cy + math.sin(rad) * 80
            pdf.add_line(cx, cy - 100, fx, fy, 1)
        # Ribbon
        pdf.add_rect(cx - 15, cy - 120, 30, 40)

    elif theme == "mushroom":
        # Cluster of mushrooms
        for mx, my, sz in [(250, 300, 40), (306, 320, 55), (370, 290, 35)]:
            # Stem
            pdf.add_rect(mx - sz//4, my - sz, sz//2, sz)
            # Cap (triangle-ish)
            pdf.add_line(mx - sz, my, mx, my + sz, 1.5)
            pdf.add_line(mx + sz, my, mx, my + sz, 1.5)
            pdf.add_line(mx - sz, my, mx + sz, my, 1.5)
            # Dots on cap
            for dot in range(3):
                dx = mx - sz//2 + dot * (sz//2)
                pdf.add_rect(dx, my + sz//3, 5, 5)
        # Ground line with grass
        pdf.add_line(150, 250, 462, 250, 1)
        for gx in range(160, 460, 15):
            pdf.add_line(gx, 250, gx + 5, 265, 0.5)


    elif theme == "teapot":
        # Teapot shape
        pdf.add_rect(240, 350, 132, 100)  # Body
        pdf.add_line(240, 450, 306, 480, 1)  # Top left
        pdf.add_line(372, 450, 306, 480, 1)  # Top right
        pdf.add_rect(280, 480, 52, 15)  # Lid
        pdf.add_line(240, 400, 210, 420, 1.5)  # Spout
        pdf.add_line(210, 420, 200, 410, 1.5)
        pdf.add_line(372, 410, 400, 440, 1.5)  # Handle
        pdf.add_line(400, 440, 400, 380, 1.5)
        pdf.add_line(400, 380, 372, 390, 1.5)
        # Teacups
        pdf.add_rect(180, 280, 60, 40)
        pdf.add_rect(370, 280, 60, 40)
        # Table line
        pdf.add_line(140, 275, 472, 275, 1.5)
        # Flowers in vase
        draw_flower(pdf, 306, 520, 15)

    elif theme == "herbs":
        # Herb pots on shelf
        pdf.add_line(120, 350, 492, 350, 2)  # Shelf
        for px, label in [(170, "Basil"), (270, "Mint"), (370, "Thyme")]:
            pdf.add_rect(px, 355, 60, 80)  # Pot
            # Leaves/stems going up
            for s in range(4):
                pdf.add_line(px + 30, 435, px + 15 + s*12, 500 + s*15, 1)
                pdf.add_line(px + 15 + s*12, 500 + s*15, px + 20 + s*12, 510 + s*15, 0.5)
            pdf.add_text(px + 10, 360, label, font='TimesRoman', size=9)

    elif theme == "bee":
        # Bee body
        pdf.add_rect(280, 420, 52, 30)  # Body
        pdf.add_rect(270, 420, 15, 30)  # Head
        # Stripes
        for s in range(3):
            pdf.add_line(285 + s*15, 420, 285 + s*15, 450, 1)
        # Wings
        pdf.add_line(295, 450, 280, 480, 1)
        pdf.add_line(280, 480, 310, 470, 1)
        pdf.add_line(310, 450, 320, 480, 1)
        pdf.add_line(320, 480, 330, 460, 1)
        # Lavender stems
        for lx in range(180, 440, 50):
            pdf.add_line(lx, 200, lx + 10, 400, 1)
            for ly in range(280, 400, 15):
                pdf.add_rect(lx + 5, ly, 12, 8)


    elif theme == "path":
        # Winding garden path
        pdf.add_line(250, 150, 220, 300, 1.5)
        pdf.add_line(220, 300, 280, 450, 1.5)
        pdf.add_line(280, 450, 250, 600, 1.5)
        pdf.add_line(350, 150, 380, 300, 1.5)
        pdf.add_line(380, 300, 320, 450, 1.5)
        pdf.add_line(320, 450, 350, 600, 1.5)
        # Flowers along sides
        for fy in range(200, 580, 60):
            draw_flower(pdf, 180, fy, 12)
            draw_flower(pdf, 420, fy, 12)
        # Fence
        pdf.add_line(100, 550, 180, 550, 1)
        pdf.add_line(430, 550, 512, 550, 1)

    elif theme == "can":
        # Watering can
        pdf.add_rect(230, 300, 120, 100)  # Body
        pdf.add_line(230, 350, 190, 380, 1.5)  # Spout
        pdf.add_line(190, 380, 180, 370, 1)
        pdf.add_line(350, 370, 380, 420, 1.5)  # Handle
        pdf.add_line(380, 420, 370, 400, 1.5)
        pdf.add_line(370, 400, 350, 400, 1)
        # Flowers coming out
        for fx in range(240, 350, 25):
            draw_flower(pdf, fx, 430 + (fx % 30), 15)
            pdf.add_line(fx, 400, fx, 430 + (fx % 30) - 15, 0.8)

    elif theme == "fox":
        # Simple fox shape
        # Body
        pdf.add_rect(240, 300, 130, 80)
        # Head
        pdf.add_rect(270, 380, 70, 60)
        # Ears
        pdf.add_line(280, 440, 275, 470, 1.5)
        pdf.add_line(275, 470, 295, 450, 1.5)
        pdf.add_line(320, 440, 335, 470, 1.5)
        pdf.add_line(335, 470, 325, 450, 1.5)
        # Tail
        pdf.add_line(370, 340, 420, 380, 1.5)
        pdf.add_line(420, 380, 400, 350, 1.5)
        # Legs
        for lx in [255, 285, 330, 355]:
            pdf.add_line(lx, 300, lx, 260, 1.5)
        # Surrounding flowers
        for fx in range(160, 460, 40):
            draw_flower(pdf, fx, 250, 10)


    elif theme == "butterfly":
        # Multiple butterflies
        for bx, by, sz in [(220, 450, 40), (350, 500, 35), (280, 350, 45), (400, 380, 30)]:
            # Wings
            pdf.add_rect(bx - sz, by, sz, sz * 2 // 3)
            pdf.add_rect(bx, by, sz, sz * 2 // 3)
            # Body
            pdf.add_line(bx, by - 5, bx, by + sz * 2 // 3 + 5, 2)
            # Antennae
            pdf.add_line(bx, by + sz * 2 // 3 + 5, bx - 8, by + sz, 0.5)
            pdf.add_line(bx, by + sz * 2 // 3 + 5, bx + 8, by + sz, 0.5)
        # Daisies at bottom
        for dx in range(160, 460, 35):
            draw_flower(pdf, dx, 250, 12)

    elif theme == "bridge":
        # Stone arch bridge
        pdf.add_line(150, 350, 250, 450, 2)  # Left arch
        pdf.add_line(250, 450, 362, 450, 2)  # Top
        pdf.add_line(362, 450, 462, 350, 2)  # Right arch
        pdf.add_line(150, 350, 150, 300, 1.5)  # Left wall
        pdf.add_line(462, 350, 462, 300, 1.5)  # Right wall
        # Stone pattern
        for sy in range(310, 440, 20):
            for sx in range(180, 440, 40):
                if sy < 430:
                    pdf.add_rect(sx, sy, 30, 15)
        # Water
        for wy in range(250, 300, 12):
            pdf.add_line(130, wy, 480, wy, 0.3)
        # Trees
        pdf.add_rect(100, 350, 20, 100)
        pdf.add_rect(490, 350, 20, 100)

    elif theme == "window":
        # Window frame
        pdf.add_rect(180, 280, 252, 320, line_width=3)
        pdf.add_line(306, 280, 306, 600, 2)  # Vertical divider
        pdf.add_line(180, 440, 432, 440, 2)  # Horizontal divider
        # Window box
        pdf.add_rect(170, 250, 272, 35, line_width=2)
        # Flowers in box
        for fx in range(190, 430, 30):
            draw_flower(pdf, fx, 310 + (fx % 25), 12)
            pdf.add_line(fx, 285, fx, 310 + (fx % 25) - 12, 0.5)
        # Curtains
        pdf.add_line(185, 595, 220, 285, 0.8)
        pdf.add_line(427, 595, 392, 285, 0.8)


    elif theme == "basket":
        # Basket shape
        pdf.add_rect(210, 300, 192, 100)  # Basket body
        # Weave pattern
        for wy in range(310, 395, 15):
            pdf.add_line(215, wy, 397, wy, 0.5)
        for wx in range(225, 400, 20):
            pdf.add_line(wx, 300, wx, 400, 0.5)
        # Handle
        pdf.add_line(250, 400, 306, 500, 1.5)
        pdf.add_line(362, 400, 306, 500, 1.5)
        # Vegetables poking out
        for vx in range(230, 390, 35):
            pdf.add_rect(vx, 400, 20, 40)  # Vegetables
            pdf.add_line(vx + 10, 440, vx + 10, 460, 0.5)  # Stems

    elif theme == "sunflower":
        # Large sunflower
        r = 60
        for angle in range(0, 360, 20):
            rad = math.radians(angle)
            px = cx + math.cos(rad) * r
            py = 430 + math.sin(rad) * r
            # Petal
            pdf.add_line(cx, 430, px, py, 1.5)
            pdf.add_line(px, py, cx + math.cos(math.radians(angle+10)) * (r+20),
                        430 + math.sin(math.radians(angle+10)) * (r+20), 1)
        # Center
        pdf.add_rect(cx - 30, 400, 60, 60)
        # Stem
        pdf.add_line(cx, 370, cx, 200, 2)
        # Leaves
        pdf.add_line(cx, 300, cx - 50, 320, 1)
        pdf.add_line(cx - 50, 320, cx - 30, 290, 1)
        pdf.add_line(cx, 260, cx + 50, 280, 1)
        pdf.add_line(cx + 50, 280, cx + 30, 250, 1)
        # More sunflowers smaller
        draw_flower(pdf, 180, 350, 25)
        draw_flower(pdf, 430, 380, 20)

    elif theme == "reading":
        # Armchair
        pdf.add_rect(200, 250, 212, 180)  # Seat back
        pdf.add_rect(180, 250, 30, 120)  # Left arm
        pdf.add_rect(402, 250, 30, 120)  # Right arm
        # Cushion
        pdf.add_rect(210, 250, 192, 50)
        # Book
        pdf.add_rect(260, 450, 92, 60)
        pdf.add_line(306, 450, 306, 510, 1)  # Book spine
        # Lamp
        pdf.add_line(460, 250, 460, 520, 1.5)
        pdf.add_line(440, 520, 480, 520, 1.5)
        pdf.add_rect(440, 525, 40, 30)  # Lampshade
        # Cat on chair
        pdf.add_rect(280, 305, 50, 35)
        # Rug
        pdf.add_rect(160, 220, 292, 20)

    else:
        # Generic floral pattern
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            fx = cx + math.cos(rad) * 120
            fy = 420 + math.sin(rad) * 120
            draw_flower(pdf, fx, fy, 18)


def draw_flower(pdf, x, y, size):
    """Draw a simple flower at given position."""
    # Petals (4 lines radiating out)
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        px = x + math.cos(rad) * size
        py = y + math.sin(rad) * size
        pdf.add_line(x, y, px, py, 0.8)
    # Center dot
    s = size // 4
    pdf.add_rect(x - s, y - s, s * 2, s * 2)


if __name__ == '__main__':
    create_cottagecore_book()
