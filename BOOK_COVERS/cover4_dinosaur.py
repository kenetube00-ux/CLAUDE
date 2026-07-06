"""
Cover 4: Awesome Dinosaur Activity Book (Ages 7-10)
KDP Cover - 8.5x11 (612x792 points) - Bold, fun, kid-friendly
"""
import sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def draw_cover_trex(pdf, x, y, scale=1):
    s = scale
    pdf.add_rect(x, y, int(120*s), int(80*s), line_width=2.5)
    pdf.add_rect(x + int(100*s), y + int(60*s), int(80*s), int(50*s), line_width=2.5)
    pdf.add_rect(x + int(105*s), y + int(45*s), int(70*s), int(18*s), line_width=2)
    for t in range(5):
        tx = x + int(110*s) + t * int(13*s)
        pdf.add_line(tx, y + int(45*s), tx + int(6*s), y + int(38*s), 1.5)
    pdf.add_rect(x + int(140*s), y + int(85*s), int(15*s), int(15*s), line_width=2)
    pdf.add_line(x, y + int(50*s), x - int(50*s), y + int(70*s), 2.5)
    pdf.add_line(x - int(50*s), y + int(70*s), x - int(60*s), y + int(55*s), 2.5)
    pdf.add_rect(x + int(20*s), y - int(40*s), int(20*s), int(40*s), line_width=2)
    pdf.add_rect(x + int(70*s), y - int(40*s), int(20*s), int(40*s), line_width=2)
    pdf.add_line(x + int(95*s), y + int(60*s), x + int(100*s), y + int(40*s), 2)

def draw_star(pdf, x, y, size):
    for angle in range(0, 360, 72):
        import math
        rad = math.radians(angle)
        px = x + math.cos(rad) * size
        py = y + math.sin(rad) * size
        pdf.add_line(x, y, px, py, 1)

def create_cover():
    pdf = PDFDoc(612, 792)
    pdf.new_page()

    # Top gray band for title
    pdf.add_filled_rect(0, 650, 612, 142, gray=0.9)

    # Main title
    pdf.add_centered_text(755, "AWESOME", font='F2', size=34)
    pdf.add_centered_text(705, "DINOSAUR", font='F2', size=48)
    pdf.add_centered_text(660, "ACTIVITY BOOK", font='F2', size=34)

    # Age badge
    pdf.add_rect(460, 590, 100, 45, line_width=2.5)
    pdf.add_text(475, 605, "AGES", font='F2', size=12)
    pdf.add_text(510, 595, "7-10", font='F2', size=20)

    # Subtitle
    pdf.add_centered_text(615, "Word Search | Mazes | Puzzles | Coloring | Trivia", font='F1', size=13)

    # Big T-Rex
    draw_cover_trex(pdf, 180, 320, 2.0)

    # Stars scattered
    star_positions = [(80, 500), (530, 480), (100, 370), (520, 350), (540, 260)]
    for sx, sy in star_positions:
        draw_star(pdf, sx, sy, 12)

    # 50+ badge
    pdf.add_rect(60, 440, 100, 45, line_width=2.5)
    pdf.add_text(75, 453, "50+", font='F2', size=26)
    pdf.add_text(70, 425, "Activities!", font='F2', size=12)

    # Ground line with plants
    pdf.add_line(50, 290, 562, 290, 1.5)
    for px in range(70, 560, 40):
        pdf.add_line(px, 290, px, 305, 0.8)
        pdf.add_line(px, 305, px - 5, 315, 0.5)
        pdf.add_line(px, 305, px + 5, 315, 0.5)

    # Feature banner
    pdf.add_filled_rect(70, 195, 472, 35, gray=0.9)
    pdf.add_centered_text(205, "Hours of Screen-Free Fun for Young Dino Fans!", font='F2', size=13)

    # Author
    pdf.add_centered_text(140, "Daniel Tesfamariam", font='F2', size=20)

    # Bottom band
    pdf.add_filled_rect(0, 0, 612, 45, gray=0.9)
    pdf.add_centered_text(15, "Educational & Entertaining", font='F1', size=13)

    # Border
    pdf.add_rect(10, 50, 592, 730, line_width=2)

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover4_Dinosaur_Activity_Book.pdf')
    print("Cover 4 created: Cover4_Dinosaur_Activity_Book.pdf")

if __name__ == '__main__':
    create_cover()
