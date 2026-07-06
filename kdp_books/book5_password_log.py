"""
Book 5: Senior-Friendly Password Log Book
KDP Interior - 6x9 inches (432x648 points)
Alphabetical tabs, large print, extra-wide writing spaces, security tips
"""
from pdf_utils import PDFDoc

def create_password_log_book():
    pdf = PDFDoc(432, 648)  # 6x9 inches

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "LARGE PRINT", font='HelveticaBold', size=18)
    pdf.add_centered_text(485, "PASSWORD", font='HelveticaBold', size=38)
    pdf.add_centered_text(440, "LOG BOOK", font='HelveticaBold', size=38)
    pdf.add_line(110, 420, 322, 420, 2)
    pdf.add_centered_text(390, "Internet Address & Password Organizer", font='Helvetica', size=13)
    pdf.add_centered_text(360, "Senior-Friendly Edition", font='Helvetica', size=13)
    pdf.add_centered_text(320, "Alphabetical Tabs | Extra-Large Text Areas", font='Helvetica', size=10)
    pdf.add_centered_text(295, "Security Tips Included", font='Helvetica', size=10)
    pdf.add_centered_text(200, "KEEP THIS BOOK IN A SAFE PLACE", font='HelveticaBold', size=11)
    pdf.add_rect(90, 185, 252, 30, line_width=1.5)
    pdf.add_centered_text(130, "This book belongs to:", font='Helvetica', size=12)
    pdf.add_line(130, 112, 302, 112, 0.8)


    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "Large Print Password Log Book", font='HelveticaBold', size=13)
    pdf.add_centered_text(495, "Senior-Friendly Edition", font='Helvetica', size=11)
    pdf.add_centered_text(460, "Copyright 2026. All Rights Reserved.", font='Helvetica', size=9)
    pdf.add_centered_text(435, "No part of this publication may be reproduced without permission.", font='Helvetica', size=8)
    pdf.add_centered_text(400, "ISBN: _______________", font='Helvetica', size=9)
    pdf.add_centered_text(375, "Published via Amazon KDP", font='Helvetica', size=9)
    pdf.add_centered_text(330, "DISCLAIMER:", font='HelveticaBold', size=10)
    pdf.add_centered_text(310, "Keep this book in a secure location.", font='Helvetica', size=9)
    pdf.add_centered_text(290, "Do not share this book with anyone you do not trust.", font='Helvetica', size=9)

    # --- SECURITY TIPS PAGES (2 pages) ---
    pdf.new_page()
    pdf.add_centered_text(600, "PASSWORD SECURITY TIPS", font='HelveticaBold', size=18)
    pdf.add_line(80, 583, 352, 583, 1)
    tips_page1 = [
        "CREATING STRONG PASSWORDS:",
        "",
        "1. Use at least 8-12 characters",
        "2. Mix uppercase and lowercase letters",
        "3. Include numbers (0-9)",
        "4. Add special characters (!@#$%)",
        "5. Avoid using your name or birthday",
        "6. Don't use the same password twice",
        "",
        "EXAMPLES OF WEAK PASSWORDS:",
        "  password123  (too common)",
        "  john1950  (uses personal info)",
        "  123456  (too simple)",
        "",
        "EXAMPLES OF STRONG PASSWORDS:",
        "  Sunset#Beach42!",
        "  My3Cats&ADog!",
        "  Garden$Rose_2024",
    ]
    y = 555
    for line in tips_page1:
        bold = line.endswith(':') or line.startswith('EX')
        font = 'HelveticaBold' if bold else 'Helvetica'
        size = 13 if bold else 12
        pdf.add_text(60, y, line, font=font, size=size)
        y -= 24


    pdf.new_page()
    pdf.add_centered_text(600, "STAYING SAFE ONLINE", font='HelveticaBold', size=18)
    pdf.add_line(80, 583, 352, 583, 1)
    tips_page2 = [
        "PROTECTING YOURSELF:",
        "",
        "1. Never share passwords by email",
        "2. Don't click links in suspicious emails",
        "3. Look for the lock icon in your browser",
        "4. Update passwords every 6-12 months",
        "5. Log out when using public computers",
        "6. Keep this book locked away safely",
        "",
        "IF YOU FORGET A PASSWORD:",
        "",
        "1. Click 'Forgot Password' on the website",
        "2. Check your email for a reset link",
        "3. Create a NEW strong password",
        "4. Write it in this book immediately",
        "",
        "WHAT IS TWO-FACTOR AUTHENTICATION?",
        "  A code sent to your phone for extra safety.",
        "  Always turn it on when available!",
    ]
    y = 555
    for line in tips_page2:
        bold = line.endswith(':') or line.endswith('?')
        font = 'HelveticaBold' if bold else 'Helvetica'
        size = 13 if bold else 12
        pdf.add_text(60, y, line, font=font, size=size)
        y -= 24

    # --- HOW TO USE THIS BOOK ---
    pdf.new_page()
    pdf.add_centered_text(600, "HOW TO USE THIS BOOK", font='HelveticaBold', size=18)
    pdf.add_line(80, 583, 352, 583, 1)
    how_to = [
        "This book is organized alphabetically (A-Z).",
        "",
        "Each letter section has space for multiple",
        "accounts. For each account, write down:",
        "",
        "  - Website Name (e.g., Amazon, Gmail)",
        "  - Website Address (www.example.com)",
        "  - Username or Email",
        "  - Password",
        "  - Security Question & Answer",
        "  - Notes (phone number on file, etc.)",
        "",
        "TIP: Use pencil so you can erase and",
        "update when you change passwords!",
        "",
        "The tabs on each page help you find",
        "the right letter section quickly.",
    ]
    y = 555
    for line in how_to:
        pdf.add_text(60, y, line, font='Helvetica', size=12)
        y -= 26


    # --- ALPHABETICAL PASSWORD ENTRY PAGES ---
    # Each letter gets 2 pages with 3 entry slots per page
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in alphabet:
        for page_num in range(2):  # 2 pages per letter
            pdf.new_page()

            # Letter tab at top right
            pdf.add_filled_rect(360, 610, 45, 30, gray=0.15)
            pdf.set_gray(1)
            pdf.add_text(372, 617, letter, font='HelveticaBold', size=20)
            pdf.reset_color()

            # Header
            pdf.add_text(60, 620, f"Letter: {letter}", font='HelveticaBold', size=16)
            pdf.add_line(60, 608, 350, 608, 0.8)

            # 3 account entry blocks per page
            y_start = 570
            for entry in range(3):
                y = y_start - entry * 185

                # Entry box with light background
                pdf.add_filled_rect(55, y - 160, 322, 170, gray=0.96)
                pdf.add_rect(55, y - 160, 322, 170, line_width=0.5)

                # Fields with large writing lines
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
                    pdf.add_text(62, fy, field_name, font='HelveticaBold', size=10)
                    # Writing line
                    pdf.add_line(165, fy - 3, 370, fy - 3, 0.4)

            # Page indicator
            pg_text = f"{letter}-{page_num + 1}"
            pdf.add_centered_text(35, pg_text, font='Helvetica', size=8)


    # --- IMPORTANT CONTACTS PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "IMPORTANT CONTACTS", font='HelveticaBold', size=16)
    pdf.add_line(80, 585, 352, 585, 0.8)
    pdf.add_text(60, 560, "Tech support numbers & contacts to keep handy:", font='Helvetica', size=10)

    contacts = [
        "Internet Provider:",
        "Phone Company:",
        "Bank:",
        "Credit Card Company:",
        "Computer Repair:",
        "Family Tech Helper:",
        "Email Provider Support:",
        "Other:",
    ]
    y = 520
    for contact in contacts:
        pdf.add_text(60, y, contact, font='HelveticaBold', size=11)
        pdf.add_line(60, y - 18, 372, y - 18, 0.4)
        pdf.add_text(60, y - 30, "Phone:", font='Helvetica', size=9)
        pdf.add_line(105, y - 33, 372, y - 33, 0.3)
        y -= 58

    # --- WIFI INFORMATION PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "HOME WIFI INFORMATION", font='HelveticaBold', size=16)
    pdf.add_line(80, 585, 352, 585, 0.8)
    pdf.add_text(60, 555, "Keep your WiFi details here for easy reference.", font='Helvetica', size=10)

    wifi_fields = [
        ("Network Name (SSID):", 510),
        ("WiFi Password:", 470),
        ("Router Brand/Model:", 430),
        ("Router Login URL:", 390),
        ("Router Username:", 350),
        ("Router Password:", 310),
        ("Internet Provider:", 270),
        ("Account Number:", 230),
        ("Support Phone:", 190),
    ]
    for field, fy in wifi_fields:
        pdf.add_text(60, fy, field, font='HelveticaBold', size=11)
        pdf.add_line(60, fy - 16, 372, fy - 16, 0.4)


    # --- NOTES PAGES (3 pages) ---
    for n in range(3):
        pdf.new_page()
        pdf.add_centered_text(610, "NOTES", font='HelveticaBold', size=14)
        for i in range(18):
            y_line = 575 - i * 28
            pdf.add_line(60, y_line, 372, y_line, 0.3)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(480, "Thank You!", font='HelveticaBold', size=22)
    pdf.add_centered_text(445, "for choosing this Password Log Book.", font='Helvetica', size=12)
    pdf.add_line(130, 425, 302, 425, 1)
    pdf.add_centered_text(395, "REMEMBER:", font='HelveticaBold', size=13)
    pdf.add_centered_text(370, "Keep this book in a safe, private location.", font='Helvetica', size=11)
    pdf.add_centered_text(348, "Update passwords regularly.", font='Helvetica', size=11)
    pdf.add_centered_text(326, "Never share your passwords by email.", font='Helvetica', size=11)
    pdf.add_centered_text(280, "If you found this book helpful,", font='Helvetica', size=11)
    pdf.add_centered_text(258, "please leave a review on Amazon!", font='Helvetica', size=11)
    pdf.add_centered_text(218, "Also available:", font='HelveticaBold', size=12)
    pdf.add_centered_text(195, "- Large Print Address Book for Seniors", font='Helvetica', size=10)
    pdf.add_centered_text(175, "- Large Print Phone Number Organizer", font='Helvetica', size=10)
    pdf.add_centered_text(155, "- Large Print Medical Information Log", font='Helvetica', size=10)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book5_Password_Log_Book_Seniors.pdf')
    print("Book 5 created: Book5_Password_Log_Book_Seniors.pdf")

if __name__ == '__main__':
    create_password_log_book()
