"""
Cover 5: Large Print Password Log Book (Senior-Friendly)
KDP Cover - 6x9 inches with bleed = 6.25x9.25 (450x666 points)
Front cover only - Clean, professional, trustworthy design
"""
import sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def draw_lock_icon(pdf, x, y, scale=1):
    """Draw a padlock icon."""
    s = scale
    # Lock body
    pdf.add_rect(x - int(20*s), y, int(40*s), int(30*s), line_width=2.5)
    # Shackle (top arc)
    pdf.add_line(x - int(12*s), y + int(30*s), x - int(12*s), y + int(45*s), 2.5)
    pdf.add_line(x - int(12*s), y + int(45*s), x - int(5*s), y + int(52*s), 2.5)
    pdf.add_line(x - int(5*s), y + int(52*s), x + int(5*s), y + int(52*s), 2.5)
    pdf.add_line(x + int(5*s), y + int(52*s), x + int(12*s), y + int(45*s), 2.5)
    pdf.add_line(x + int(12*s), y + int(45*s), x + int(12*s), y + int(30*s), 2.5)
    # Keyhole
    pdf.add_rect(x - int(4*s), y + int(10*s), int(8*s), int(12*s), line_width=1.5)

def draw_key_icon(pdf, x, y, scale=1):
    """Draw a key icon."""
    s = scale
    # Key head (circle area)
    pdf.add_rect(x, y, int(16*s), int(16*s), line_width=2)
    # Key shaft
    pdf.add_line(x + int(16*s), y + int(8*s), x + int(50*s), y + int(8*s), 2)
    # Key teeth
    pdf.add_line(x + int(40*s), y + int(8*s), x + int(40*s), y, 1.5)
    pdf.add_line(x + int(45*s), y + int(8*s), x + int(45*s), y + int(2*s), 1.5)
    pdf.add_line(x + int(35*s), y + int(8*s), x + int(35*s), y + int(2*s), 1.5)

def create_cover():
    # 6.25 x 9.25 inches (450 x 666 points)
    pdf = PDFDoc(450, 666)
    pdf.new_page()

    # === CLEAN DARK BACKGROUND ===
    pdf.add_filled_rect(0, 0, 450, 666, gray=0.12)

    # === TOP BANNER - "LARGE PRINT" ===
    pdf.add_filled_rect(50, 600, 350, 35, gray=0.75)
    pdf.set_gray(0.1)
    pdf.add_text(130, 609, "LARGE PRINT EDITION", font='HelveticaBold', size=17)
    pdf.reset_color()

    # === MAIN TITLE ===
    pdf.set_gray(1)
    pdf.add_text(80, 550, "PASSWORD", font='HelveticaBold', size=42)
    pdf.add_text(90, 500, "LOG BOOK", font='HelveticaBold', size=42)
    pdf.reset_color()

    # === DECORATIVE LINE ===
    pdf.set_gray(0.6)
    pdf.add_line(80, 485, 370, 485, 2)
    pdf.reset_color()

    # === SUBTITLE ===
    pdf.set_gray(0.75)
    pdf.add_text(70, 455, "Internet Address & Password Organizer", font='Helvetica', size=14)
    pdf.add_text(115, 432, "Senior-Friendly Edition", font='Helvetica', size=14)
    pdf.reset_color()

    # === LOCK ICON (central visual) ===
    pdf.set_gray(0.8)
    draw_lock_icon(pdf, 225, 320, 3)
    pdf.reset_color()

    # === KEY ICONS on sides ===
    pdf.set_gray(0.5)
    draw_key_icon(pdf, 80, 360, 1.5)
    draw_key_icon(pdf, 310, 360, 1.5)
    pdf.reset_color()

    # === FEATURE LIST ===
    pdf.set_gray(0.85)
    features = [
        "Alphabetical A-Z Tabs",
        "Extra-Large Writing Spaces",
        "156 Account Entry Slots",
        "Security Tips Included",
        "WiFi & Contact Pages",
    ]
    y = 275
    for feat in features:
        pdf.add_text(140, y, f">> {feat}", font='Helvetica', size=12)
        y -= 22
    pdf.reset_color()

    # === BADGE: "KEEP SAFE" ===
    pdf.add_filled_rect(140, 130, 170, 30, gray=0.7)
    pdf.set_gray(0.1)
    pdf.add_text(155, 138, "KEEP IN A SAFE PLACE", font='HelveticaBold', size=11)
    pdf.reset_color()

    # === AUTHOR NAME ===
    pdf.set_gray(1)
    pdf.add_text(115, 85, "Daniel Tesfamariam", font='HelveticaBold', size=20)
    pdf.reset_color()

    # === BORDER ===
    pdf.set_gray(0.5)
    pdf.add_rect(18, 18, 414, 630, line_width=1.5)
    pdf.add_rect(22, 22, 406, 622, line_width=0.5)
    pdf.reset_color()

    # === BOTTOM ACCENT ===
    pdf.set_gray(0.6)
    pdf.add_line(80, 50, 370, 50, 1)
    pdf.reset_color()

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover5_Password_Log_Book.pdf')
    print("Cover 5 created: Cover5_Password_Log_Book.pdf")

if __name__ == '__main__':
    create_cover()
