"""
Book 5: Senior-Friendly Password Log Book
KDP Interior - 6x9 inches (432x648 points)
WHITE background, BLACK text
"""
from pdf_utils import PDFDoc

def create_password_log_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "LARGE PRINT", font='F2', size=18)
    pdf.add_centered_text(485, "PASSWORD", font='F2', size=38)
    pdf.add_centered_text(440, "LOG BOOK", font='F2', size=38)
    pdf.add_line(110, 420, 322, 420, 2)
    pdf.add_centered_text(390, "Internet Address & Password Organizer", font='F1', size=13)
    pdf.add_centered_text(360, "Senior-Friendly Edition", font='F1', size=13)
    pdf.add_centered_text(320, "Alphabetical Tabs | Extra-Large Text Areas", font='F1', size=10)
    pdf.add_centered_text(295, "Security Tips Included", font='F1', size=10)
    pdf.add_centered_text(230, "By", font='F1', size=11)
    pdf.add_centered_text(207, "Daniel Tesfamariam", font='F2', size=15)
    pdf.add_centered_text(160, "KEEP THIS BOOK IN A SAFE PLACE", font='F2', size=11)
    pdf.add_rect(115, 150, 202, 25, line_width=1.5)
    pdf.add_centered_text(110, "This book belongs to:", font='F1', size=12)
    pdf.add_line(130, 95, 302, 95, 0.8)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "Large Print Password Log Book", font='F2', size=13)
    pdf.add_centered_text(495, "Senior-Friendly Edition", font='F1', size=11)
    pdf.add_centered_text(470, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(440, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(418, "No part of this publication may be reproduced.", font='F1', size=8)
    pdf.add_centered_text(390, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(368, "Published via Amazon KDP", font='F1', size=9)

    # --- SECURITY TIPS ---
    pdf.new_page()
    pdf.add_centered_text(600, "PASSWORD SECURITY TIPS", font='F2', size=18)
    pdf.add_line(80, 583, 352, 583, 1)
    tips = [
        "CREATING STRONG PASSWORDS:", "",
        "1. Use at least 8-12 characters",
        "2. Mix uppercase and lowercase letters",
        "3. Include numbers (0-9)",
        "4. Add special characters (!@#$%)",
        "5. Avoid using your name or birthday",
        "6. Don't use the same password twice", "",
        "EXAMPLES OF WEAK PASSWORDS:",
        "  password123  (too common)",
        "  john1950  (uses personal info)", "",
        "EXAMPLES OF STRONG PASSWORDS:",
        "  Sunset#Beach42!",
        "  My3Cats&ADog!",
        "  Garden$Rose_2024",
    ]
    y = 555
    for line in tips:
        bold = line.endswith(':')
        font = 'HelveticaBold' if bold else 'Helvetica'
        pdf.add_text(60, y, line, font=font, size=12)
        y -= 24

    # --- HOW TO USE ---
    pdf.new_page()
    pdf.add_centered_text(600, "HOW TO USE THIS BOOK", font='F2', size=18)
    pdf.add_line(80, 583, 352, 583, 1)
    how_to = [
        "This book is organized alphabetically (A-Z).",
        "", "Each letter section has space for multiple",
        "accounts. For each account, write down:", "",
        "  - Website Name (e.g., Amazon, Gmail)",
        "  - Website Address (www.example.com)",
        "  - Username or Email",
        "  - Password",
        "  - Security Question & Answer",
        "  - Notes (phone number on file, etc.)", "",
        "TIP: Use pencil so you can erase and",
        "update when you change passwords!",
    ]
    y = 555
    for line in how_to:
        pdf.add_text(60, y, line, font='F1', size=12)
        y -= 26

    # --- ALPHABETICAL ENTRY PAGES (A-Z, 2 pages each) ---
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        for page_num in range(2):
            pdf.new_page()
            # Letter tab
            pdf.add_filled_rect(355, 610, 50, 30, gray=0.85)
            pdf.add_text(367, 617, letter, font='F2', size=20)
            # Header
            pdf.add_text(60, 620, f"Letter: {letter}", font='F2', size=16)
            pdf.add_line(60, 608, 350, 608, 0.8)

            # 3 account entries per page
            y_start = 570
            for entry in range(3):
                y = y_start - entry * 185
                # Light gray background box
                pdf.add_filled_rect(55, y - 160, 322, 170, gray=0.96)
                pdf.add_rect(55, y - 160, 322, 170, line_width=0.5)

                fields = [
                    ("Website Name:", 0),
                    ("Web Address:", -30),
                    ("Username/Email:", -60),
                    ("Password:", -90),
                    ("Security Q:", -120),
                    ("Notes:", -150),
                ]
                for field_name, offset in fields:
                    fy = y + offset
                    pdf.add_text(62, fy, field_name, font='F2', size=10)
                    pdf.add_line(165, fy - 3, 370, fy - 3, 0.4, gray=0.4)

            pdf.add_centered_text(35, f"{letter}-{page_num + 1}", font='F1', size=8)

    # --- NOTES PAGES ---
    for n in range(3):
        pdf.new_page()
        pdf.add_centered_text(610, "NOTES", font='F2', size=14)
        for i in range(18):
            y_line = 575 - i * 28
            pdf.add_line(60, y_line, 372, y_line, 0.3, gray=0.5)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(480, "Thank You!", font='F2', size=22)
    pdf.add_centered_text(445, "for choosing this Password Log Book.", font='F1', size=12)
    pdf.add_line(130, 425, 302, 425, 1)
    pdf.add_centered_text(395, "REMEMBER:", font='F2', size=13)
    pdf.add_centered_text(370, "Keep this book in a safe, private location.", font='F1', size=11)
    pdf.add_centered_text(348, "Update passwords regularly.", font='F1', size=11)
    pdf.add_centered_text(326, "Never share your passwords by email.", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book5_Password_Log_Book_Seniors.pdf')
    print("Book 5 created: Book5_Password_Log_Book_Seniors.pdf")

if __name__ == '__main__':
    create_password_log_book()
