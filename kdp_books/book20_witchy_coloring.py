"""
Book 20: WITCHY COLORING BOOK - Magical Illustrations for Adults
KDP Interior - 8.5x11 inches (612x792 points)
Title page + copyright + 15 coloring pages with alternating blank back pages
"""
from pdf_utils import PDFDoc
import math

def draw_circle(pdf, cx, cy, r, segments=24, width=1, gray=0):
    """Draw a circle approximated with line segments."""
    for i in range(segments):
        a1 = 2 * math.pi * i / segments
        a2 = 2 * math.pi * (i + 1) / segments
        x1 = cx + r * math.cos(a1)
        y1 = cy + r * math.sin(a1)
        x2 = cx + r * math.cos(a2)
        y2 = cy + r * math.sin(a2)
        pdf.add_line(x1, y1, x2, y2, width, gray)

def draw_star(pdf, cx, cy, outer_r, inner_r, points=5, width=1):
    """Draw a star shape."""
    coords = []
    for i in range(points * 2):
        angle = math.pi / 2 + 2 * math.pi * i / (points * 2)
        r = outer_r if i % 2 == 0 else inner_r
        coords.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    for i in range(len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % len(coords)]
        pdf.add_line(x1, y1, x2, y2, width)

def draw_crescent(pdf, cx, cy, r, width=1.5):
    """Draw a crescent moon."""
    draw_circle(pdf, cx, cy, r, 30, width)
    draw_circle(pdf, cx + r * 0.4, cy, r * 0.8, 30, width)


def draw_crystal_ball(pdf):
    """Page 1: Crystal ball on a stand."""
    cx, cy = 306, 440
    # Ball
    draw_circle(pdf, cx, cy, 120, 36, 2)
    # Stand base
    pdf.add_line(236, 310, 376, 310, 2)
    pdf.add_line(256, 310, 276, 280, 2)
    pdf.add_line(356, 310, 336, 280, 2)
    pdf.add_line(276, 280, 336, 280, 2)
    # Inner mystical lines
    draw_circle(pdf, cx - 20, cy + 20, 15, 12, 1)
    draw_circle(pdf, cx + 30, cy - 10, 10, 12, 1)
    draw_star(pdf, cx, cy, 30, 12, 5, 1)
    # Sparkles
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        sx = cx + 90 * math.cos(rad)
        sy = cy + 90 * math.sin(rad)
        pdf.add_line(sx - 5, sy, sx + 5, sy, 0.8)
        pdf.add_line(sx, sy - 5, sx, sy + 5, 0.8)

def draw_moon_phases(pdf):
    """Page 2: Moon phases in a row."""
    y = 450
    phases = 7
    spacing = 72
    start_x = 306 - (phases - 1) * spacing / 2
    for i in range(phases):
        cx = start_x + i * spacing
        draw_circle(pdf, cx, y, 30, 24, 1.5)
    # Full moon in center
    draw_circle(pdf, 306, y, 32, 24, 2)
    # Decorative arc above
    for i in range(20):
        a1 = math.pi * 0.1 + math.pi * 0.8 * i / 20
        a2 = math.pi * 0.1 + math.pi * 0.8 * (i + 1) / 20
        pdf.add_line(306 + 200 * math.cos(a1), y + 120 + 80 * math.sin(a1),
                     306 + 200 * math.cos(a2), y + 120 + 80 * math.sin(a2), 1.5)
    # Stars scattered
    for sx, sy in [(150, 600), (460, 580), (200, 350), (420, 340), (306, 650)]:
        draw_star(pdf, sx, sy, 12, 5, 5, 1)


def draw_potion_bottles(pdf):
    """Page 3: Potion bottles."""
    # Bottle 1 - tall
    pdf.add_rect(180, 350, 60, 150, 2)
    pdf.add_rect(195, 500, 30, 30, 2)
    draw_circle(pdf, 210, 540, 12, 12, 1.5)
    # Bubble inside
    draw_circle(pdf, 200, 400, 8, 10, 1)
    draw_circle(pdf, 215, 380, 5, 10, 1)
    # Bottle 2 - round
    draw_circle(pdf, 350, 400, 60, 30, 2)
    pdf.add_rect(335, 460, 30, 35, 2)
    pdf.add_line(335, 495, 365, 495, 2)
    draw_circle(pdf, 345, 390, 6, 10, 1)
    draw_circle(pdf, 360, 410, 4, 10, 1)
    # Bottle 3 - small flask
    pdf.add_line(430, 350, 430, 480, 2)
    pdf.add_line(490, 350, 490, 480, 2)
    pdf.add_line(430, 350, 490, 350, 2)
    pdf.add_line(430, 480, 450, 510, 2)
    pdf.add_line(490, 480, 470, 510, 2)
    pdf.add_line(450, 510, 470, 510, 2)
    # Shelf
    pdf.add_line(140, 340, 530, 340, 2)
    # Labels
    draw_star(pdf, 210, 425, 15, 6, 5, 1)
    draw_circle(pdf, 350, 400, 20, 16, 1)

def draw_black_cat(pdf):
    """Page 4: Black cat sitting."""
    cx, cy = 306, 380
    # Body - oval
    draw_circle(pdf, cx, cy - 30, 70, 30, 2)
    # Head
    draw_circle(pdf, cx, cy + 80, 45, 24, 2)
    # Ears
    pdf.add_line(cx - 30, cy + 110, cx - 15, cy + 145, 2)
    pdf.add_line(cx - 15, cy + 145, cx - 5, cy + 115, 2)
    pdf.add_line(cx + 30, cy + 110, cx + 15, cy + 145, 2)
    pdf.add_line(cx + 15, cy + 145, cx + 5, cy + 115, 2)
    # Eyes
    draw_circle(pdf, cx - 15, cy + 85, 8, 12, 1.5)
    draw_circle(pdf, cx + 15, cy + 85, 8, 12, 1.5)
    # Nose
    pdf.add_line(cx - 4, cy + 70, cx, cy + 65, 1)
    pdf.add_line(cx + 4, cy + 70, cx, cy + 65, 1)
    # Whiskers
    pdf.add_line(cx - 45, cy + 75, cx - 15, cy + 72, 0.8)
    pdf.add_line(cx - 45, cy + 68, cx - 15, cy + 68, 0.8)
    pdf.add_line(cx + 45, cy + 75, cx + 15, cy + 72, 0.8)
    pdf.add_line(cx + 45, cy + 68, cx + 15, cy + 68, 0.8)
    # Tail
    for i in range(20):
        t = i / 20
        x1 = cx + 70 + 40 * math.sin(t * math.pi)
        y1 = cy - 80 + t * 100
        t2 = (i + 1) / 20
        x2 = cx + 70 + 40 * math.sin(t2 * math.pi)
        y2 = cy - 80 + t2 * 100
        pdf.add_line(x1, y1, x2, y2, 2)
    # Paws
    draw_circle(pdf, cx - 25, cy - 90, 12, 10, 1.5)
    draw_circle(pdf, cx + 25, cy - 90, 12, 10, 1.5)


def draw_cauldron(pdf):
    """Page 5: Bubbling cauldron."""
    cx, cy = 306, 350
    # Cauldron body (wide ellipse)
    draw_circle(pdf, cx, cy, 100, 30, 2)
    # Rim
    pdf.add_line(cx - 105, cy + 30, cx + 105, cy + 30, 2.5)
    pdf.add_line(cx - 100, cy + 40, cx + 100, cy + 40, 2.5)
    # Legs
    pdf.add_line(cx - 60, cy - 100, cx - 70, cy - 130, 2)
    pdf.add_line(cx + 60, cy - 100, cx + 70, cy - 130, 2)
    pdf.add_line(cx, cy - 105, cx, cy - 135, 2)
    # Bubbles
    for bx, by, br in [(cx - 30, cy + 70, 15), (cx + 20, cy + 80, 12),
                        (cx - 10, cy + 100, 8), (cx + 40, cy + 95, 10),
                        (cx - 50, cy + 90, 7), (cx + 10, cy + 120, 6)]:
        draw_circle(pdf, bx, by, br, 12, 1)
    # Fire underneath
    for i in range(5):
        fx = cx - 50 + i * 25
        pdf.add_line(fx, cy - 130, fx + 8, cy - 100, 1.5)
        pdf.add_line(fx + 8, cy - 100, fx + 16, cy - 130, 1.5)
    # Handle
    pdf.add_line(cx - 100, cy + 35, cx - 120, cy + 60, 2)
    pdf.add_line(cx + 100, cy + 35, cx + 120, cy + 60, 2)

def draw_tarot_cards(pdf):
    """Page 6: Tarot cards spread."""
    # Card 1 - left tilted
    x, y = 170, 300
    pdf.add_rect(x, y, 100, 160, 2)
    draw_star(pdf, x + 50, y + 80, 30, 12, 5, 1.5)
    draw_circle(pdf, x + 50, y + 130, 15, 12, 1)
    # Card 2 - center
    x, y = 260, 320
    pdf.add_rect(x, y, 100, 160, 2)
    # Sun design
    draw_circle(pdf, x + 50, y + 90, 25, 20, 1.5)
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        pdf.add_line(x + 50 + 25 * math.cos(rad), y + 90 + 25 * math.sin(rad),
                     x + 50 + 38 * math.cos(rad), y + 90 + 38 * math.sin(rad), 1)
    # Card 3 - right tilted
    x, y = 350, 290
    pdf.add_rect(x, y, 100, 160, 2)
    draw_crescent(pdf, x + 50, y + 90, 25, 1.5)
    # Decorative border around all
    pdf.add_rect(130, 260, 360, 260, 1, gray=0.3)

def draw_pentagram_mandala(pdf):
    """Page 7: Pentagram inside mandala circles."""
    cx, cy = 306, 420
    # Outer circles
    draw_circle(pdf, cx, cy, 180, 40, 1.5)
    draw_circle(pdf, cx, cy, 160, 36, 1)
    draw_circle(pdf, cx, cy, 140, 36, 1.5)
    # Pentagram
    points = []
    for i in range(5):
        angle = math.pi / 2 + 2 * math.pi * i / 5
        points.append((cx + 120 * math.cos(angle), cy + 120 * math.sin(angle)))
    # Draw star connecting every other point
    order = [0, 2, 4, 1, 3, 0]
    for i in range(5):
        pdf.add_line(points[order[i]][0], points[order[i]][1],
                     points[order[i+1]][0], points[order[i+1]][1], 2)
    # Inner pentagon
    for i in range(5):
        pdf.add_line(points[i][0], points[i][1],
                     points[(i+1) % 5][0], points[(i+1) % 5][1], 1)
    # Decorative dots (small circles) at points
    for px, py in points:
        draw_circle(pdf, px, py, 5, 8, 1.5)
    # Center circle
    draw_circle(pdf, cx, cy, 20, 16, 1)


def draw_spell_book(pdf):
    """Page 8: Open spell book."""
    cx, cy = 306, 380
    # Left page
    pdf.add_rect(130, 300, 160, 220, 2)
    # Right page
    pdf.add_rect(310, 300, 160, 220, 2)
    # Spine
    pdf.add_line(290, 295, 290, 525, 2.5)
    pdf.add_line(310, 295, 310, 525, 2.5)
    # Text lines on left
    for i in range(8):
        pdf.add_line(145, 490 - i * 24, 270, 490 - i * 24, 0.8)
    # Mystical symbol on right page
    draw_circle(pdf, 390, 420, 40, 20, 1.5)
    draw_star(pdf, 390, 420, 35, 14, 5, 1.2)
    # Bookmark ribbon
    pdf.add_line(300, 525, 280, 560, 1.5)
    pdf.add_line(280, 560, 270, 555, 1)
    pdf.add_line(280, 560, 275, 550, 1)
    # Sparkles around book
    for sx, sy in [(160, 550), (440, 545), (250, 570), (380, 560)]:
        pdf.add_line(sx - 6, sy, sx + 6, sy, 0.8)
        pdf.add_line(sx, sy - 6, sx, sy + 6, 0.8)

def draw_mushroom_circle(pdf):
    """Page 9: Fairy mushroom circle."""
    cx, cy = 306, 380
    # Draw mushrooms in a circle
    num_mushrooms = 8
    for i in range(num_mushrooms):
        angle = 2 * math.pi * i / num_mushrooms
        mx = cx + 150 * math.cos(angle)
        my = cy + 150 * math.sin(angle)
        # Stem
        pdf.add_rect(mx - 8, my - 20, 16, 30, 1.5)
        # Cap (half circle approximation)
        for j in range(12):
            a1 = math.pi * j / 12
            a2 = math.pi * (j + 1) / 12
            pdf.add_line(mx + 22 * math.cos(a1), my + 10 + 18 * math.sin(a1),
                         mx + 22 * math.cos(a2), my + 10 + 18 * math.sin(a2), 1.5)
        # Dots on cap
        draw_circle(pdf, mx - 5, my + 18, 3, 8, 0.8)
        draw_circle(pdf, mx + 7, my + 15, 2, 8, 0.8)
    # Center fairy ring
    draw_circle(pdf, cx, cy, 150, 30, 0.5)
    # Small stars in center
    draw_star(pdf, cx, cy, 20, 8, 5, 1)
    draw_star(pdf, cx - 30, cy + 20, 10, 4, 5, 0.8)
    draw_star(pdf, cx + 25, cy - 15, 12, 5, 5, 0.8)

def draw_witch_hat(pdf):
    """Page 10: Decorative witch hat."""
    cx, cy = 306, 350
    # Brim (ellipse-like)
    pdf.add_line(cx - 140, cy, cx + 140, cy, 2)
    for i in range(20):
        a1 = math.pi + math.pi * i / 20
        a2 = math.pi + math.pi * (i + 1) / 20
        pdf.add_line(cx + 140 * math.cos(a1), cy + 25 * math.sin(a1),
                     cx + 140 * math.cos(a2), cy + 25 * math.sin(a2), 2)
    # Cone
    pdf.add_line(cx - 80, cy, cx, cy + 250, 2)
    pdf.add_line(cx + 80, cy, cx, cy + 250, 2)
    # Tip curl
    pdf.add_line(cx, cy + 250, cx + 25, cy + 240, 1.5)
    pdf.add_line(cx + 25, cy + 240, cx + 20, cy + 225, 1.5)
    # Band
    pdf.add_line(cx - 78, cy + 20, cx + 78, cy + 20, 1.5)
    pdf.add_line(cx - 75, cy + 40, cx + 75, cy + 40, 1.5)
    # Buckle
    pdf.add_rect(cx - 15, cy + 18, 30, 25, 2)
    pdf.add_rect(cx - 8, cy + 25, 16, 11, 1)
    # Stars around
    for sx, sy in [(160, 500), (450, 480), (180, 250), (430, 270)]:
        draw_star(pdf, sx, sy, 15, 6, 5, 1)


def draw_herbs_bundle(pdf):
    """Page 11: Bundle of hanging herbs."""
    cx, cy = 306, 600
    # Rope/string at top
    pdf.add_line(cx - 100, cy, cx + 100, cy, 2)
    # Hanging bundles
    positions = [cx - 80, cx - 40, cx, cx + 40, cx + 80]
    for px in positions:
        # String
        pdf.add_line(px, cy, px, cy - 30, 1)
        # Bundle of leaves
        for j in range(5):
            leaf_y = cy - 50 - j * 30
            pdf.add_line(px, leaf_y, px - 12, leaf_y - 20, 1)
            pdf.add_line(px, leaf_y, px + 12, leaf_y - 20, 1)
            pdf.add_line(px - 12, leaf_y - 20, px, leaf_y - 30, 1)
            pdf.add_line(px + 12, leaf_y - 20, px, leaf_y - 30, 1)
        # Tie
        pdf.add_line(px - 8, cy - 35, px + 8, cy - 35, 1.5)
    # Bow on center bundle
    pdf.add_line(cx - 10, cy - 30, cx - 20, cy - 20, 1)
    pdf.add_line(cx + 10, cy - 30, cx + 20, cy - 20, 1)

def draw_crescent_moon_page(pdf):
    """Page 12: Large crescent moon with details."""
    cx, cy = 306, 420
    # Outer circle
    draw_circle(pdf, cx, cy, 150, 40, 2)
    # Inner circle offset to create crescent
    draw_circle(pdf, cx + 60, cy, 130, 36, 2)
    # Stars around
    star_positions = [(150, 600), (460, 580), (130, 300), (480, 320),
                     (200, 680), (420, 680), (306, 200)]
    for sx, sy in star_positions:
        draw_star(pdf, sx, sy, 15, 6, 5, 1)
    # Small dots
    for sx, sy in [(180, 500), (440, 450), (250, 250), (380, 250)]:
        draw_circle(pdf, sx, sy, 3, 8, 1)

def draw_candle_altar(pdf):
    """Page 13: Candle altar with three candles."""
    # Altar table
    pdf.add_rect(150, 250, 312, 20, 2)
    pdf.add_line(160, 250, 160, 200, 2)
    pdf.add_line(452, 250, 452, 200, 2)
    pdf.add_line(160, 200, 452, 200, 2)
    # Three candles
    candle_positions = [230, 306, 382]
    heights = [180, 200, 160]
    for i, (cx, h) in enumerate(zip(candle_positions, heights)):
        # Candle body
        pdf.add_rect(cx - 15, 270, 30, h, 1.5)
        # Flame
        top = 270 + h
        pdf.add_line(cx - 8, top, cx, top + 25, 1.5)
        pdf.add_line(cx + 8, top, cx, top + 25, 1.5)
        pdf.add_line(cx - 8, top, cx, top + 5, 0.8)
        pdf.add_line(cx + 8, top, cx, top + 5, 0.8)
        # Dripping wax
        pdf.add_line(cx - 10, top - 5, cx - 12, top - 20, 0.8)
        pdf.add_line(cx + 10, top - 5, cx + 12, top - 20, 0.8)
    # Pentacle on altar
    draw_circle(pdf, 306, 230, 15, 12, 1)
    draw_star(pdf, 306, 230, 12, 5, 5, 0.8)
    # Crystals on sides
    pdf.add_line(175, 270, 185, 300, 1)
    pdf.add_line(185, 300, 195, 270, 1)
    pdf.add_line(175, 270, 195, 270, 1)
    pdf.add_line(420, 270, 430, 295, 1)
    pdf.add_line(430, 295, 440, 270, 1)
    pdf.add_line(420, 270, 440, 270, 1)


def draw_broomstick(pdf):
    """Page 14: Decorative broomstick."""
    cx, cy = 306, 400
    # Handle (diagonal)
    pdf.add_line(cx - 150, cy + 200, cx + 100, cy - 150, 2.5)
    # Bristles
    bx, by = cx - 150, cy + 200
    for i in range(15):
        angle = -math.pi / 4 + (i - 7) * 0.08
        pdf.add_line(bx, by, bx + 80 * math.cos(angle - math.pi/2),
                     by + 80 * math.sin(angle - math.pi/2), 1.5)
    # Binding
    pdf.add_line(bx + 5, by - 5, bx - 15, by + 15, 2)
    pdf.add_line(bx + 10, by - 10, bx - 10, by + 10, 2)
    # Stars and sparkles
    for sx, sy in [(200, 300), (420, 500), (450, 300), (180, 550)]:
        draw_star(pdf, sx, sy, 15, 6, 5, 1)
    # Trailing sparkle dots
    for i in range(6):
        sx = cx + 100 - i * 20
        sy = cy - 150 + i * 15
        draw_circle(pdf, sx, sy, 3 + i * 0.5, 8, 0.8)

def draw_starry_night(pdf):
    """Page 15: Starry night sky with landscape."""
    # Ground/horizon
    pdf.add_line(50, 250, 562, 250, 2)
    # Hills
    for i in range(15):
        a1 = math.pi * i / 15
        a2 = math.pi * (i + 1) / 15
        pdf.add_line(50 + 512 * i / 15, 250 + 40 * math.sin(a1),
                     50 + 512 * (i + 1) / 15, 250 + 40 * math.sin(a2), 1.5)
    # Large stars
    star_data = [(150, 550, 25), (300, 620, 30), (450, 560, 22),
                 (200, 450, 18), (400, 480, 20), (100, 650, 15),
                 (500, 650, 18), (306, 500, 15)]
    for sx, sy, sr in star_data:
        draw_star(pdf, sx, sy, sr, sr * 0.4, 5, 1.5)
    # Swirling pattern (like Van Gogh)
    for i in range(30):
        angle = i * 0.3
        r = 60 + i * 2
        x1 = 306 + r * math.cos(angle) * 0.8
        y1 = 480 + r * math.sin(angle) * 0.4
        x2 = 306 + (r + 5) * math.cos(angle + 0.3) * 0.8
        y2 = 480 + (r + 5) * math.sin(angle + 0.3) * 0.4
        if 50 < x1 < 562 and 260 < y1 < 740 and 50 < x2 < 562 and 260 < y2 < 740:
            pdf.add_line(x1, y1, x2, y2, 1)
    # Moon
    draw_circle(pdf, 480, 650, 40, 24, 2)
    draw_circle(pdf, 495, 655, 35, 20, 2)
    # Small scattered dots
    for sx, sy in [(130, 380), (250, 680), (370, 700), (520, 400), (80, 500)]:
        draw_circle(pdf, sx, sy, 2, 6, 1)

def create_witchy_coloring_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "WITCHY", font='F2', size=34)
    pdf.add_centered_text(575, "COLORING BOOK", font='F2', size=28)
    pdf.add_line(150, 555, 462, 555, 2)
    pdf.add_centered_text(520, "Magical Illustrations for Adults", font='F4', size=16)
    pdf.add_centered_text(485, "15 Enchanting Pages to Color", font='F1', size=13)
    pdf.add_centered_text(380, "By", font='F1', size=12)
    pdf.add_centered_text(355, "Daniel Tesfamariam", font='F2', size=18)
    # Decorative stars on title
    draw_star(pdf, 200, 450, 20, 8, 5, 1.5)
    draw_star(pdf, 412, 450, 20, 8, 5, 1.5)
    draw_crescent(pdf, 306, 280, 30, 1.5)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(620, "Witchy Coloring Book", font='F2', size=14)
    pdf.add_centered_text(590, "Magical Illustrations for Adults", font='F4', size=12)
    pdf.add_centered_text(555, "By Daniel Tesfamariam", font='F2', size=12)
    pdf.add_centered_text(520, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(495, "ISBN: _______________", font='F1', size=10)
    pdf.add_centered_text(470, "Published via Amazon KDP", font='F1', size=10)
    pdf.add_centered_text(420, "For personal use only. Do not reproduce.", font='F1', size=9)

    # --- 15 COLORING PAGES with blank backs ---
    themes = [
        ("Crystal Ball", draw_crystal_ball),
        ("Moon Phases", draw_moon_phases),
        ("Potion Bottles", draw_potion_bottles),
        ("Black Cat", draw_black_cat),
        ("Cauldron", draw_cauldron),
        ("Tarot Cards", draw_tarot_cards),
        ("Pentagram Mandala", draw_pentagram_mandala),
        ("Spell Book", draw_spell_book),
        ("Mushroom Circle", draw_mushroom_circle),
        ("Witch Hat", draw_witch_hat),
        ("Herbs Bundle", draw_herbs_bundle),
        ("Crescent Moon", draw_crescent_moon_page),
        ("Candle Altar", draw_candle_altar),
        ("Broomstick", draw_broomstick),
        ("Starry Night", draw_starry_night),
    ]

    for i, (title, draw_func) in enumerate(themes):
        # Blank back page
        pdf.new_page()
        pdf.add_centered_text(396, "This page intentionally left blank", font='F1', size=9, gray=0.7)

        # Illustration page
        pdf.new_page()
        draw_func(pdf)
        pdf.add_centered_text(50, title, font='F1', size=10, gray=0.3)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book20_Witchy_Coloring_Book.pdf')
    print("Book 20 created: Book20_Witchy_Coloring_Book.pdf")

if __name__ == '__main__':
    create_witchy_coloring_book()
