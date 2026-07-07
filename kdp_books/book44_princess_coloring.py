"""Book 44: Princess Coloring Book"""
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)

# Title page
pdf.new_page()
pdf.add_centered_text(500, "PRINCESS COLORING BOOK", 'F2', 26)
pdf.add_centered_text(460, "For Girls Ages 4-8", 'F4', 16, 0.3)
pdf.add_line(180, 440, 432, 440, 1, 0.5)
pdf.add_centered_text(250, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(500, "Princess Coloring Book", 'F2', 14)
pdf.add_centered_text(470, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(450, "All rights reserved.", 'F1', 10)


# Drawing functions for princess-themed illustrations
def draw_castle(pdf):
    """Castle with towers"""
    cx, cy = 306, 400
    # Main wall
    pdf.add_rect(206, 300, 200, 180, 2, 0)
    # Left tower
    pdf.add_rect(186, 350, 40, 180, 2, 0)
    # Right tower
    pdf.add_rect(386, 350, 40, 180, 2, 0)
    # Tower tops (triangle via lines)
    pdf.add_line(186, 530, 206, 570, 2, 0)
    pdf.add_line(206, 570, 226, 530, 2, 0)
    pdf.add_line(386, 530, 406, 570, 2, 0)
    pdf.add_line(406, 570, 426, 530, 2, 0)
    # Door
    pdf.add_rect(281, 300, 50, 80, 2, 0)
    # Windows
    pdf.add_rect(230, 400, 30, 30, 1.5, 0)
    pdf.add_rect(350, 400, 30, 30, 1.5, 0)
    pdf.add_centered_text(260, "Castle", 'F2', 14)

def draw_dress(pdf):
    """Princess dress/gown outline"""
    cx = 306
    # Bodice
    pdf.add_line(276, 500, 276, 420, 2, 0)
    pdf.add_line(336, 500, 336, 420, 2, 0)
    pdf.add_line(276, 500, 336, 500, 2, 0)
    # Skirt (flared)
    pdf.add_line(276, 420, 216, 280, 2, 0)
    pdf.add_line(336, 420, 396, 280, 2, 0)
    pdf.add_line(216, 280, 396, 280, 2, 0)
    # Neckline
    pdf.add_line(276, 500, 296, 520, 1.5, 0)
    pdf.add_line(336, 500, 316, 520, 1.5, 0)
    # Waist bow
    pdf.add_rect(286, 415, 40, 15, 1.5, 0)
    pdf.add_centered_text(250, "Princess Dress", 'F2', 14)

def draw_crown(pdf):
    """Tiara/crown"""
    cx = 306
    # Base
    pdf.add_rect(236, 380, 140, 30, 2, 0)
    # Points
    for i in range(5):
        x = 250 + i * 30
        pdf.add_line(x, 410, x + 15, 460, 2, 0)
        pdf.add_line(x + 15, 460, x + 30, 410, 2, 0)
    # Jewels (small rects)
    for i in range(5):
        x = 258 + i * 30
        pdf.add_rect(x, 385, 8, 8, 1, 0)
    pdf.add_centered_text(340, "Crown", 'F2', 14)


def draw_wand(pdf):
    """Magic wand with star"""
    # Wand stick
    pdf.add_line(270, 300, 340, 520, 2, 0)
    # Star at top
    pdf.add_line(330, 520, 350, 560, 2, 0)
    pdf.add_line(350, 560, 370, 520, 2, 0)
    pdf.add_line(370, 520, 330, 540, 2, 0)
    pdf.add_line(330, 540, 370, 540, 2, 0)
    pdf.add_line(370, 540, 330, 520, 2, 0)
    pdf.add_centered_text(260, "Magic Wand", 'F2', 14)

def draw_unicorn(pdf):
    """Simple unicorn"""
    # Body (oval-ish via rect)
    pdf.add_rect(230, 350, 150, 80, 2, 0)
    # Head
    pdf.add_rect(360, 400, 60, 50, 2, 0)
    # Horn
    pdf.add_line(390, 450, 390, 510, 2, 0)
    # Legs
    pdf.add_line(250, 350, 250, 290, 2, 0)
    pdf.add_line(290, 350, 290, 290, 2, 0)
    pdf.add_line(340, 350, 340, 290, 2, 0)
    pdf.add_line(360, 350, 360, 290, 2, 0)
    # Tail
    pdf.add_line(230, 400, 200, 430, 2, 0)
    pdf.add_line(200, 430, 210, 380, 1.5, 0)
    # Mane
    pdf.add_line(370, 450, 360, 470, 1.5, 0)
    pdf.add_line(380, 450, 375, 475, 1.5, 0)
    pdf.add_centered_text(250, "Unicorn", 'F2', 14)

def draw_fairy(pdf):
    """Fairy with wings"""
    cx = 306
    # Body
    pdf.add_line(cx, 500, cx, 380, 2, 0)
    # Head circle (approx with rect)
    pdf.add_rect(cx - 15, 500, 30, 30, 2, 0)
    # Arms
    pdf.add_line(cx, 470, cx - 40, 440, 1.5, 0)
    pdf.add_line(cx, 470, cx + 40, 440, 1.5, 0)
    # Skirt
    pdf.add_line(cx, 420, cx - 40, 360, 2, 0)
    pdf.add_line(cx, 420, cx + 40, 360, 2, 0)
    pdf.add_line(cx - 40, 360, cx + 40, 360, 1.5, 0)
    # Wings
    pdf.add_rect(cx - 60, 430, 40, 60, 1.5, 0)
    pdf.add_rect(cx + 20, 430, 40, 60, 1.5, 0)
    pdf.add_centered_text(320, "Fairy", 'F2', 14)

def draw_mirror(pdf):
    """Magic mirror"""
    # Oval frame (rect approximation)
    pdf.add_rect(236, 340, 140, 200, 2, 0)
    # Inner mirror
    pdf.add_rect(250, 360, 112, 160, 1.5, 0.3)
    # Handle
    pdf.add_rect(286, 290, 40, 50, 2, 0)
    # Decorations
    pdf.add_rect(246, 530, 20, 20, 1, 0)
    pdf.add_rect(346, 530, 20, 20, 1, 0)
    pdf.add_centered_text(260, "Magic Mirror", 'F2', 14)


def draw_slipper(pdf):
    """Glass slipper"""
    # Shoe body
    pdf.add_line(200, 380, 350, 380, 2, 0)
    pdf.add_line(200, 380, 200, 420, 2, 0)
    pdf.add_line(200, 420, 250, 440, 2, 0)
    pdf.add_line(250, 440, 350, 430, 2, 0)
    pdf.add_line(350, 430, 380, 400, 2, 0)
    pdf.add_line(380, 400, 350, 380, 2, 0)
    # Heel
    pdf.add_line(220, 380, 210, 340, 2, 0)
    pdf.add_line(210, 340, 240, 340, 2, 0)
    pdf.add_line(240, 340, 240, 380, 2, 0)
    # Bow
    pdf.add_rect(280, 430, 30, 15, 1.5, 0)
    pdf.add_centered_text(300, "Glass Slipper", 'F2', 14)

def draw_carriage(pdf):
    """Pumpkin carriage"""
    # Pumpkin body (large rect with curves implied)
    pdf.add_rect(200, 380, 200, 140, 2, 0)
    # Vertical lines on pumpkin
    for x in [240, 280, 320, 360]:
        pdf.add_line(x, 380, x, 520, 1, 0.3)
    # Wheels
    pdf.add_rect(210, 340, 50, 50, 2, 0)
    pdf.add_rect(340, 340, 50, 50, 2, 0)
    # Door
    pdf.add_rect(270, 400, 50, 70, 1.5, 0)
    # Stem
    pdf.add_line(300, 520, 300, 550, 2, 0)
    pdf.add_centered_text(300, "Pumpkin Carriage", 'F2', 14)

def draw_garden(pdf):
    """Flower garden"""
    # Ground
    pdf.add_line(100, 350, 512, 350, 1.5, 0)
    # Flowers (stem + circle top)
    positions = [160, 230, 306, 380, 450]
    for x in positions:
        # Stem
        pdf.add_line(x, 350, x, 450, 1.5, 0)
        # Flower head (rect as petals)
        pdf.add_rect(x - 15, 450, 30, 30, 1.5, 0)
        # Center
        pdf.add_rect(x - 5, 460, 10, 10, 1, 0)
        # Leaves
        pdf.add_line(x, 400, x - 20, 390, 1, 0)
        pdf.add_line(x, 400, x + 20, 390, 1, 0)
    pdf.add_centered_text(300, "Flower Garden", 'F2', 14)

def draw_rainbow(pdf):
    """Rainbow with clouds"""
    # Rainbow arcs (lines at different heights)
    for i in range(7):
        y_start = 380 + i * 12
        pdf.add_line(180, y_start, 200, y_start + 60, 2, 0)
        pdf.add_line(200, y_start + 60, 306, y_start + 90, 1.5, 0)
        pdf.add_line(306, y_start + 90, 412, y_start + 60, 1.5, 0)
        pdf.add_line(412, y_start + 60, 432, y_start, 2, 0)
    # Clouds (rect groups)
    pdf.add_rect(140, 370, 60, 30, 1.5, 0)
    pdf.add_rect(160, 385, 50, 25, 1.5, 0)
    pdf.add_rect(400, 370, 60, 30, 1.5, 0)
    pdf.add_rect(410, 385, 50, 25, 1.5, 0)
    pdf.add_centered_text(300, "Rainbow", 'F2', 14)


def draw_butterfly(pdf):
    """Butterfly princess"""
    cx = 306
    # Body
    pdf.add_line(cx, 350, cx, 500, 2, 0)
    # Head
    pdf.add_rect(cx - 10, 500, 20, 20, 2, 0)
    # Antennae
    pdf.add_line(cx - 5, 520, cx - 20, 545, 1.5, 0)
    pdf.add_line(cx + 5, 520, cx + 20, 545, 1.5, 0)
    # Wings (4 wing shapes using rects)
    pdf.add_rect(cx - 80, 430, 70, 60, 2, 0)
    pdf.add_rect(cx + 10, 430, 70, 60, 2, 0)
    pdf.add_rect(cx - 60, 370, 50, 50, 2, 0)
    pdf.add_rect(cx + 10, 370, 50, 50, 2, 0)
    # Wing decorations
    pdf.add_rect(cx - 60, 445, 20, 20, 1, 0.3)
    pdf.add_rect(cx + 40, 445, 20, 20, 1, 0.3)
    pdf.add_centered_text(310, "Butterfly Princess", 'F2', 14)

def draw_mermaid(pdf):
    """Mermaid tail"""
    cx = 306
    # Upper body
    pdf.add_rect(cx - 20, 440, 40, 70, 2, 0)
    # Head
    pdf.add_rect(cx - 15, 510, 30, 30, 2, 0)
    # Hair
    pdf.add_line(cx - 15, 530, cx - 35, 480, 1.5, 0)
    pdf.add_line(cx + 15, 530, cx + 35, 480, 1.5, 0)
    # Tail
    pdf.add_line(cx - 20, 440, cx - 10, 350, 2, 0)
    pdf.add_line(cx + 20, 440, cx + 10, 350, 2, 0)
    # Tail fin
    pdf.add_line(cx - 10, 350, cx - 40, 320, 2, 0)
    pdf.add_line(cx + 10, 350, cx + 40, 320, 2, 0)
    pdf.add_line(cx - 40, 320, cx, 340, 1.5, 0)
    pdf.add_line(cx + 40, 320, cx, 340, 1.5, 0)
    pdf.add_centered_text(280, "Mermaid", 'F2', 14)

def draw_tower(pdf):
    """Princess tower"""
    # Tower body
    pdf.add_rect(256, 280, 100, 280, 2, 0)
    # Cone top
    pdf.add_line(256, 560, 306, 620, 2, 0)
    pdf.add_line(356, 560, 306, 620, 2, 0)
    # Window at top
    pdf.add_rect(281, 500, 50, 40, 1.5, 0)
    # Window at middle
    pdf.add_rect(281, 400, 50, 40, 1.5, 0)
    # Door
    pdf.add_rect(281, 280, 50, 60, 2, 0)
    # Bricks pattern
    for y in range(300, 560, 30):
        pdf.add_line(256, y, 356, y, 0.5, 0.4)
    pdf.add_centered_text(240, "Princess Tower", 'F2', 14)

def draw_tea_party(pdf):
    """Tea party set"""
    # Table
    pdf.add_rect(180, 350, 250, 10, 2, 0)
    # Table legs
    pdf.add_line(200, 350, 200, 300, 2, 0)
    pdf.add_line(410, 350, 410, 300, 2, 0)
    # Teapot
    pdf.add_rect(220, 360, 60, 50, 2, 0)
    pdf.add_line(220, 385, 200, 385, 1.5, 0)  # Spout
    pdf.add_line(280, 385, 300, 400, 1.5, 0)  # Handle
    pdf.add_line(300, 400, 280, 395, 1.5, 0)
    # Cups
    pdf.add_rect(320, 360, 30, 25, 1.5, 0)
    pdf.add_rect(370, 360, 30, 25, 1.5, 0)
    # Cake
    pdf.add_rect(250, 410, 50, 30, 1.5, 0)
    pdf.add_rect(255, 440, 40, 5, 1, 0)
    pdf.add_centered_text(270, "Tea Party", 'F2', 14)


def draw_princess_cat(pdf):
    """Princess cat"""
    cx = 306
    # Body
    pdf.add_rect(cx - 30, 350, 60, 80, 2, 0)
    # Head
    pdf.add_rect(cx - 25, 430, 50, 50, 2, 0)
    # Ears (triangles)
    pdf.add_line(cx - 25, 480, cx - 15, 500, 2, 0)
    pdf.add_line(cx - 15, 500, cx - 5, 480, 2, 0)
    pdf.add_line(cx + 5, 480, cx + 15, 500, 2, 0)
    pdf.add_line(cx + 15, 500, cx + 25, 480, 2, 0)
    # Crown on head
    pdf.add_rect(cx - 15, 490, 30, 10, 1.5, 0)
    # Tail
    pdf.add_line(cx + 30, 380, cx + 50, 420, 1.5, 0)
    pdf.add_line(cx + 50, 420, cx + 40, 440, 1.5, 0)
    # Whiskers
    pdf.add_line(cx - 25, 450, cx - 45, 455, 1, 0)
    pdf.add_line(cx - 25, 445, cx - 45, 445, 1, 0)
    pdf.add_line(cx + 25, 450, cx + 45, 455, 1, 0)
    pdf.add_line(cx + 25, 445, cx + 45, 445, 1, 0)
    pdf.add_centered_text(310, "Princess Cat", 'F2', 14)

def draw_treasure_chest(pdf):
    """Treasure chest"""
    # Chest body
    pdf.add_rect(216, 350, 180, 100, 2, 0)
    # Lid (slightly wider)
    pdf.add_rect(210, 450, 192, 40, 2, 0)
    # Lid curve
    pdf.add_line(210, 490, 306, 510, 1.5, 0)
    pdf.add_line(306, 510, 402, 490, 1.5, 0)
    # Lock
    pdf.add_rect(291, 430, 30, 30, 2, 0)
    # Bands
    pdf.add_line(216, 400, 396, 400, 1, 0.3)
    # Jewels spilling out
    pdf.add_rect(250, 490, 10, 10, 1, 0)
    pdf.add_rect(300, 500, 10, 10, 1, 0)
    pdf.add_rect(340, 490, 10, 10, 1, 0)
    pdf.add_centered_text(310, "Treasure Chest", 'F2', 14)

def draw_magic_book(pdf):
    """Magic book"""
    # Book covers
    pdf.add_rect(216, 350, 180, 200, 2, 0)
    # Spine
    pdf.add_line(216, 350, 216, 550, 3, 0)
    # Pages
    pdf.add_rect(222, 356, 168, 188, 1, 0.4)
    # Star on cover
    pdf.add_line(306, 480, 316, 450, 1.5, 0)
    pdf.add_line(316, 450, 326, 480, 1.5, 0)
    pdf.add_line(326, 480, 296, 460, 1.5, 0)
    pdf.add_line(296, 460, 326, 460, 1.5, 0)
    # Sparkles
    pdf.add_line(260, 510, 265, 515, 1, 0)
    pdf.add_line(350, 510, 355, 515, 1, 0)
    pdf.add_line(280, 400, 285, 405, 1, 0)
    pdf.add_centered_text(310, "Magic Book", 'F2', 14)

def draw_dancing_princess(pdf):
    """Dancing princess"""
    cx = 306
    # Head
    pdf.add_rect(cx - 12, 510, 24, 24, 2, 0)
    # Body
    pdf.add_line(cx, 510, cx, 430, 2, 0)
    # Arms (dancing pose)
    pdf.add_line(cx, 480, cx - 50, 500, 1.5, 0)
    pdf.add_line(cx, 480, cx + 50, 510, 1.5, 0)
    # Skirt (wide, flowing)
    pdf.add_line(cx, 430, cx - 60, 340, 2, 0)
    pdf.add_line(cx, 430, cx + 60, 340, 2, 0)
    pdf.add_line(cx - 60, 340, cx + 60, 340, 1.5, 0)
    # Crown
    pdf.add_line(cx - 10, 534, cx, 545, 1.5, 0)
    pdf.add_line(cx, 545, cx + 10, 534, 1.5, 0)
    # Skirt details
    pdf.add_line(cx - 30, 430, cx - 50, 340, 1, 0.3)
    pdf.add_line(cx + 30, 430, cx + 50, 340, 1, 0.3)
    pdf.add_centered_text(300, "Dancing Princess", 'F2', 14)

def draw_dragon_friend(pdf):
    """Friendly dragon"""
    cx = 306
    # Body
    pdf.add_rect(cx - 50, 360, 100, 70, 2, 0)
    # Head
    pdf.add_rect(cx + 40, 400, 50, 40, 2, 0)
    # Tail
    pdf.add_line(cx - 50, 390, cx - 90, 420, 2, 0)
    pdf.add_line(cx - 90, 420, cx - 100, 400, 2, 0)
    # Wings
    pdf.add_line(cx - 20, 430, cx - 40, 490, 2, 0)
    pdf.add_line(cx - 40, 490, cx + 10, 470, 2, 0)
    pdf.add_line(cx + 10, 430, cx + 20, 490, 2, 0)
    pdf.add_line(cx + 20, 490, cx + 40, 460, 2, 0)
    # Legs
    pdf.add_line(cx - 30, 360, cx - 30, 330, 2, 0)
    pdf.add_line(cx + 20, 360, cx + 20, 330, 2, 0)
    # Smile on head
    pdf.add_line(cx + 50, 410, cx + 70, 410, 1.5, 0)
    # Eye
    pdf.add_rect(cx + 60, 420, 8, 8, 1.5, 0)
    pdf.add_centered_text(290, "Dragon Friend", 'F2', 14)


# List of all drawing functions and their titles
drawings = [
    (draw_castle, "Castle with Towers"),
    (draw_dress, "Princess Dress"),
    (draw_crown, "Tiara & Crown"),
    (draw_wand, "Magic Wand"),
    (draw_unicorn, "Unicorn"),
    (draw_fairy, "Fairy with Wings"),
    (draw_mirror, "Magic Mirror"),
    (draw_slipper, "Glass Slipper"),
    (draw_carriage, "Pumpkin Carriage"),
    (draw_garden, "Flower Garden"),
    (draw_rainbow, "Rainbow with Clouds"),
    (draw_butterfly, "Butterfly Princess"),
    (draw_mermaid, "Mermaid Tail"),
    (draw_tower, "Princess Tower"),
    (draw_tea_party, "Tea Party Set"),
    (draw_princess_cat, "Princess Cat"),
    (draw_treasure_chest, "Treasure Chest"),
    (draw_magic_book, "Magic Book"),
    (draw_dancing_princess, "Dancing Princess"),
    (draw_dragon_friend, "Dragon Friend"),
]

# Create coloring pages (blank back + illustration)
for draw_func, title in drawings:
    # Blank back page
    pdf.new_page()
    pdf.add_centered_text(396, "This page intentionally left blank", 'F1', 10, 0.7)
    # Illustration page
    pdf.new_page()
    pdf.add_centered_text(730, title, 'F2', 14)
    draw_func(pdf)

pdf.save("Book44_Princess_Coloring_Book.pdf")
print("Created Book44_Princess_Coloring_Book.pdf")
