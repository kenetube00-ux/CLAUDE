"""
Cover 3: The Nurse's Guided Journal
KDP Cover - 6x9 inches with bleed = 6.25x9.25 (450x666 points)
Front cover only - Professional, warm, calming design
"""
import sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def draw_heart(pdf, x, y, size):
    """Draw a simple heart shape using lines."""
    s = size
    # Left bump
    pdf.add_line(x, y, x - s, y + s * 0.8, 1.5)
    pdf.add_line(x - s, y + s * 0.8, x - s * 0.5, y + s * 1.4, 1.5)
    pdf.add_line(x - s * 0.5, y + s * 1.4, x, y + s, 1.5)
    # Right bump
    pdf.add_line(x, y, x + s, y + s * 0.8, 1.5)
    pdf.add_line(x + s, y + s * 0.8, x + s * 0.5, y + s * 1.4, 1.5)
    pdf.add_line(x + s * 0.5, y + s * 1.4, x, y + s, 1.5)

def draw_stethoscope(pdf, x, y, scale=1):
    """Draw stethoscope icon."""
    s = scale
    # Earpieces
    pdf.add_line(x - int(20*s), y + int(80*s), x - int(15*s), y + int(60*s), 1.5)
    pdf.add_line(x + int(20*s), y + int(80*s), x + int(15*s), y + int(60*s), 1.5)
    # Bridge
    pdf.add_line(x - int(15*s), y + int(60*s), x - int(5*s), y + int(50*s), 1.5)
    pdf.add_line(x + int(15*s), y + int(60*s), x + int(5*s), y + int(50*s), 1.5)
    # Tube down
    pdf.add_line(x - int(5*s), y + int(50*s), x, y + int(45*s), 1.5)
    pdf.add_line(x + int(5*s), y + int(50*s), x, y + int(45*s), 1.5)
    pdf.add_line(x, y + int(45*s), x, y, 2)
    # Chest piece (circle)
    pdf.add_rect(x - int(12*s), y - int(12*s), int(24*s), int(24*s), line_width=2)

def create_cover():
    # 6.25 x 9.25 inches (450 x 666 points)
    pdf = PDFDoc(450, 666)
    pdf.new_page()

    # === BACKGROUND - Soft teal/calming tone ===
    pdf.add_filled_rect(0, 0, 450, 666, gray=0.88)

    # === TOP COLORED BANNER ===
    pdf.add_filled_rect(0, 560, 450, 106, gray=0.3)

    # === "THE" in banner ===
    pdf.set_gray(0.85)
    pdf.add_text(200, 630, "THE", font='Helvetica', size=16)
    pdf.reset_color()

    # === MAIN TITLE ===
    pdf.set_gray(1)
    pdf.add_text(130, 590, "NURSE'S", font='HelveticaBold', size=40)
    pdf.reset_color()

    pdf.set_gray(1)
    pdf.add_text(80, 567, "GUIDED JOURNAL", font='HelveticaBold', size=28)
    pdf.reset_color()

    # === SUBTITLE SECTION ===
    pdf.set_gray(0.25)
    pdf.add_text(85, 525, "Reflections, Gratitude & Self-Care", font='Helvetica', size=16)
    pdf.add_text(115, 502, "for Healthcare Heroes", font='Helvetica', size=16)
    pdf.reset_color()

    # === DECORATIVE DIVIDER ===
    pdf.set_gray(0.4)
    pdf.add_line(100, 485, 350, 485, 1.5)
    pdf.reset_color()

    # === CENTRAL ILLUSTRATION - Stethoscope + Heart ===
    pdf.set_gray(0.3)
    draw_stethoscope(pdf, 225, 350, 2.5)
    pdf.reset_color()

    # Heart at bottom of stethoscope
    pdf.set_gray(0.4)
    draw_heart(pdf, 225, 300, 20)
    pdf.reset_color()

    # === FEATURE BULLETS ===
    pdf.set_gray(0.3)
    features = [
        "Daily Reflection Prompts",
        "Gratitude & Affirmation Pages",
        "Self-Care Wellness Tracker",
        "120 Pages of Guided Journaling",
    ]
    y = 260
    for feat in features:
        pdf.add_text(130, y, f"* {feat}", font='Helvetica', size=11)
        y -= 20
    pdf.reset_color()

    # === DECORATIVE BOX ===
    pdf.set_gray(0.5)
    pdf.add_rect(80, 165, 290, 25, line_width=1)
    pdf.reset_color()
    pdf.set_gray(0.25)
    pdf.add_text(95, 172, "Because you deserve care too.", font='HelveticaBold', size=13)
    pdf.reset_color()

    # === AUTHOR NAME ===
    pdf.set_gray(0.2)
    pdf.add_text(120, 110, "Daniel Tesfamariam", font='HelveticaBold', size=20)
    pdf.reset_color()

    # === BOTTOM ACCENT BAR ===
    pdf.add_filled_rect(0, 0, 450, 40, gray=0.3)
    pdf.set_gray(0.85)
    pdf.add_text(130, 15, "A Gift for Every Nurse", font='Helvetica', size=13)
    pdf.reset_color()

    # === SIDE ACCENT LINES ===
    pdf.set_gray(0.5)
    pdf.add_line(40, 80, 40, 545, 0.5)
    pdf.add_line(410, 80, 410, 545, 0.5)
    pdf.reset_color()

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover3_Nurse_Guided_Journal.pdf')
    print("Cover 3 created: Cover3_Nurse_Guided_Journal.pdf")

if __name__ == '__main__':
    create_cover()
