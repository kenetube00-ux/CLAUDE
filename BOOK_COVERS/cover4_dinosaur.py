"""
Cover 4: Awesome Dinosaur Activity Book (Ages 7-10)
KDP Cover - 8.5x11 inches with bleed = 8.75x11.25 (630x810 points)
Front cover only - Fun, bold, kid-friendly design
"""
import sys
import math
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def draw_cover_trex(pdf, x, y, scale=1):
    """Draw a fun T-Rex for the cover."""
    s = scale
    # Body
    pdf.add_rect(x, y, int(120*s), int(80*s), line_width=2.5)
    # Head (bigger, fun proportions)
    pdf.add_rect(x + int(100*s), y + int(60*s), int(80*s), int(50*s), line_width=2.5)
    # Jaw
    pdf.add_rect(x + int(110*s), y + int(45*s), int(70*s), int(18*s), line_width=2)
    # Teeth
    for t in range(5):
        tx = x + int(115*s) + t * int(13*s)
        pdf.add_line(tx, y + int(45*s), tx + int(6*s), y + int(38*s), 1.5)
    # Eye (big, friendly)
    pdf.add_rect(x + int(140*s), y + int(85*s), int(18*s), int(18*s), line_width=2)
    pdf.add_filled_rect(x + int(148*s), y + int(90*s), int(8*s), int(8*s), gray=0.1)
    # Tail
    pdf.add_line(x, y + int(50*s), x - int(50*s), y + int(70*s), 2.5)
    pdf.add_line(x - int(50*s), y + int(70*s), x - int(60*s), y + int(55*s), 2.5)
    # Legs
    pdf.add_rect(x + int(20*s), y - int(40*s), int(20*s), int(40*s), line_width=2)
    pdf.add_rect(x + int(70*s), y - int(40*s), int(20*s), int(40*s), line_width=2)
    # Arms (small, funny)
    pdf.add_line(x + int(95*s), y + int(60*s), x + int(100*s), y + int(40*s), 2)
    pdf.add_line(x + int(100*s), y + int(40*s), x + int(105*s), y + int(42*s), 1.5)

def draw_star(pdf, x, y, size):
    """Draw a simple star shape."""
    for angle in range(0, 360, 72):
        rad = math.radians(angle)
        rad2 = math.radians(angle + 36)
        px = x + math.cos(rad) * size
        py = y + math.sin(rad) * size
        px2 = x + math.cos(rad2) * (size * 0.4)
        py2 = y + math.sin(rad2) * (size * 0.4)
        pdf.add_line(x, y, px, py, 1.2)
        pdf.add_line(px, py, px2, py2, 0.8)

def create_cover():
    pdf = PDFDoc(630, 810)
    pdf.new_page()

    # === BRIGHT BACKGROUND ===
    pdf.add_filled_rect(0, 0, 630, 810, gray=0.95)

    # === TOP COLOR BLOCK (dark, bold) ===
    pdf.add_filled_rect(0, 650, 630, 160, gray=0.18)

    # === MAIN TITLE ===
    pdf.set_gray(1)
    pdf.add_text(150, 760, "AWESOME", font='HelveticaBold', size=38)
    pdf.reset_color()

    pdf.set_gray(0.95)
    pdf.add_text(100, 700, "DINOSAUR", font='HelveticaBold', size=52)
    pdf.reset_color()

    pdf.set_gray(1)
    pdf.add_text(90, 655, "ACTIVITY BOOK", font='HelveticaBold', size=38)
    pdf.reset_color()

    # === AGE BADGE (circle-like) ===
    pdf.add_filled_rect(470, 575, 110, 55, gray=0.2)
    pdf.set_gray(1)
    pdf.add_text(482, 593, "AGES", font='HelveticaBold', size=14)
    pdf.add_text(520, 583, "7-10", font='HelveticaBold', size=22)
    pdf.reset_color()

    # === SUBTITLE ===
    pdf.set_gray(0.2)
    pdf.add_text(70, 610, "Word Search | Mazes | Puzzles | Coloring | Trivia", font='Helvetica', size=15)
    pdf.reset_color()

    # === BIG T-REX ILLUSTRATION ===
    pdf.set_gray(0.25)
    draw_cover_trex(pdf, 180, 320, 2.0)
    pdf.reset_color()

    # === DECORATIVE STARS scattered around ===
    pdf.set_gray(0.4)
    star_positions = [(80, 500), (530, 450), (100, 350), (520, 320),
                     (150, 250), (480, 550), (550, 250)]
    for sx, sy in star_positions:
        draw_star(pdf, sx, sy, 12)
    pdf.reset_color()

    # === EXPLOSION/BURST SHAPE around "50+" ===
    pdf.add_filled_rect(60, 440, 120, 50, gray=0.2)
    pdf.set_gray(1)
    pdf.add_text(75, 455, "50+", font='HelveticaBold', size=28)
    pdf.reset_color()
    pdf.set_gray(0.2)
    pdf.add_text(60, 420, "Activities!", font='HelveticaBold', size=14)
    pdf.reset_color()

    # === FEATURE BANNER ===
    pdf.add_filled_rect(70, 170, 490, 40, gray=0.85)
    pdf.set_gray(0.15)
    pdf.add_text(100, 183, "Hours of Screen-Free Fun for Young Dino Fans!", font='HelveticaBold', size=14)
    pdf.reset_color()

    # === GROUND LINE with simple plants ===
    pdf.set_gray(0.4)
    pdf.add_line(50, 280, 580, 280, 1.5)
    for px in range(70, 570, 40):
        pdf.add_line(px, 280, px, 295, 0.8)
        pdf.add_line(px, 295, px - 5, 305, 0.6)
        pdf.add_line(px, 295, px + 5, 305, 0.6)
    pdf.reset_color()

    # === AUTHOR NAME ===
    pdf.set_gray(0.2)
    pdf.add_text(185, 100, "Daniel Tesfamariam", font='HelveticaBold', size=20)
    pdf.reset_color()

    # === BOTTOM ACCENT ===
    pdf.add_filled_rect(0, 0, 630, 50, gray=0.18)
    pdf.set_gray(0.8)
    pdf.add_text(200, 18, "Educational & Entertaining", font='Helvetica', size=14)
    pdf.reset_color()

    # === DECORATIVE BORDER ===
    pdf.set_gray(0.3)
    pdf.add_rect(15, 55, 600, 740, line_width=2)
    pdf.reset_color()

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover4_Dinosaur_Activity_Book.pdf')
    print("Cover 4 created: Cover4_Dinosaur_Activity_Book.pdf")

if __name__ == '__main__':
    create_cover()
