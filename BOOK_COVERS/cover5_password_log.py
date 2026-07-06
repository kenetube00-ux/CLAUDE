"""
Cover 5: Large Print Password Log Book (Senior-Friendly)
KDP Cover - 6x9 (432x648 points) - Clean, professional, trustworthy
"""
import sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

def draw_lock_icon(pdf, x, y, scale=1):
    s = scale
    pdf.add_rect(x - int(20*s), y, int(40*s), int(30*s), line_width=2.5)
    pdf.add_line(x - int(12*s), y + int(30*s), x - int(12*s), y + int(45*s), 2.5)
    pdf.add_line(x - int(12*s), y + int(45*s), x + int(12*s), y + int(45*s), 2.5)
    pdf.add_line(x + int(12*s), y + int(45*s), x + int(12*s), y + int(30*s), 2.5)
    pdf.add_rect(x - int(4*s), y + int(10*s), int(8*s), int(12*s), line_width=1.5)

def create_cover():
    pdf = PDFDoc(432, 648)
    pdf.new_page()

    # Light header band
    pdf.add_filled_rect(50, 580, 332, 40, gray=0.88)
    pdf.add_text(115, 593, "LARGE PRINT EDITION", font='HelveticaBold', size=16)

    # Main title
    pdf.add_centered_text(545, "PASSWORD", font='HelveticaBold', size=38)
    pdf.add_centered_text(500, "LOG BOOK", font='HelveticaBold', size=38)

    # Decorative line
    pdf.add_line(80, 485, 352, 485, 2)

    # Subtitle
    pdf.add_centered_text(455, "Internet Address & Password Organizer", font='Helvetica', size=13)
    pdf.add_centered_text(432, "Senior-Friendly Edition", font='Helvetica', size=13)

    # Lock icon (central visual)
    draw_lock_icon(pdf, 216, 330, 3)

    # Feature list
    features = [
        "Alphabetical A-Z Tabs",
        "Extra-Large Writing Spaces",
        "156 Account Entry Slots",
        "Security Tips Included",
        "WiFi & Contact Pages",
    ]
    y = 280
    for feat in features:
        pdf.add_centered_text(y, f">> {feat}", font='Helvetica', size=11)
        y -= 20

    # "Keep Safe" badge
    pdf.add_rect(130, 148, 172, 28, line_width=1.5)
    pdf.add_centered_text(155, "KEEP IN A SAFE PLACE", font='HelveticaBold', size=11)

    # Author
    pdf.add_centered_text(100, "Daniel Tesfamariam", font='HelveticaBold', size=18)

    # Border
    pdf.add_rect(18, 18, 396, 612, line_width=2)
    pdf.add_rect(22, 22, 388, 604, line_width=0.5)

    # Bottom accent
    pdf.add_line(80, 55, 352, 55, 1)

    pdf.save('/projects/sandbox/CLAUDE/BOOK_COVERS/Cover5_Password_Log_Book.pdf')
    print("Cover 5 created: Cover5_Password_Log_Book.pdf")

if __name__ == '__main__':
    create_cover()
