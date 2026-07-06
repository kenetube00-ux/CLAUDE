"""
Book 29: CAMPING LOG BOOK - Record Your Adventures
KDP Interior - 6x9 inches (432x648 points)
Title page + copyright + 40 trip log entries + 2 gear checklist pages + campground contacts page
"""
from pdf_utils import PDFDoc

def create_camping_log():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "CAMPING", font='F2', size=30)
    pdf.add_centered_text(493, "LOG BOOK", font='F2', size=28)
    pdf.add_line(100, 473, 332, 473, 2)
    pdf.add_centered_text(443, "Record Your Adventures", font='F4', size=14)
    pdf.add_centered_text(390, "40 Trip Logs | Gear Checklist", font='F1', size=11)
    pdf.add_centered_text(368, "Campground Contacts & Notes", font='F1', size=11)
    pdf.add_centered_text(270, "By", font='F1', size=11)
    pdf.add_centered_text(248, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "CAMPING LOG BOOK", font='F2', size=12)
    pdf.add_centered_text(498, "Record Your Adventures", font='F1', size=10)
    pdf.add_centered_text(470, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(435, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(415, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(395, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(360, "Adventure awaits!", font='F4', size=10)

    # --- 40 TRIP LOG ENTRIES ---
    for entry in range(1, 41):
        pdf.new_page()
        pdf.add_text(60, 615, f"TRIP #{entry}", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 580

        # Trip name
        pdf.add_text(60, y, "Trip Name:", font='F2', size=10)
        pdf.add_line(125, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Campground
        pdf.add_text(60, y, "Campground:", font='F2', size=10)
        pdf.add_line(132, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Location/GPS
        pdf.add_text(60, y, "Location/GPS:", font='F2', size=10)
        pdf.add_line(140, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Date arrived / departed
        pdf.add_text(60, y, "Date Arrived:", font='F2', size=10)
        pdf.add_line(135, y - 2, 225, y - 2, 0.3, gray=0.5)
        pdf.add_text(235, y, "Departed:", font='F2', size=10)
        pdf.add_line(292, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Site number
        pdf.add_text(60, y, "Site Number:", font='F2', size=10)
        pdf.add_line(132, y - 2, 220, y - 2, 0.3, gray=0.5)
        y -= 22

        # Weather
        pdf.add_text(60, y, "Weather:", font='F2', size=10)
        pdf.add_line(112, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Activities
        pdf.add_text(60, y, "Activities:", font='F2', size=10)
        pdf.add_line(118, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Wildlife seen
        pdf.add_text(60, y, "Wildlife Seen:", font='F2', size=10)
        pdf.add_line(140, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Meals cooked
        pdf.add_text(60, y, "Meals Cooked:", font='F2', size=10)
        pdf.add_line(142, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Best moment
        pdf.add_text(60, y, "Best Moment:", font='F2', size=10)
        pdf.add_line(138, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22

        # Would return & Rating
        pdf.add_text(60, y, "Would Return:", font='F2', size=10)
        pdf.add_text(142, y, "Y  /  N", font='F1', size=10)
        pdf.add_text(220, y, "Rating (1-5):", font='F2', size=10)
        for i in range(5):
            pdf.add_text(300 + i * 15, y, "*", font='F1', size=14)
        y -= 26

        # Notes
        pdf.add_text(60, y, "Notes:", font='F2', size=10)
        y -= 16
        for i in range(4):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 18

        # Page number
        pdf.add_centered_text(30, f"- {entry + 2} -", font='F1', size=8)


    # --- GEAR CHECKLIST PAGES (2 pages) ---
    gear_page1 = [
        "Tent", "Sleeping Bag", "Sleeping Pad", "Pillow", "Tarp/Groundsheet",
        "Camp Chairs", "Lantern/Headlamp", "Flashlight", "Firewood/Fire Starter",
        "Matches/Lighter", "Camp Stove", "Fuel", "Cooler", "Pots & Pans",
        "Plates/Bowls/Cups", "Utensils", "Can Opener", "Cutting Board/Knife",
        "Water Bottles", "Water Filter", "Trash Bags", "Paper Towels"
    ]
    gear_page2 = [
        "First Aid Kit", "Sunscreen", "Bug Spray", "Map/GPS", "Compass",
        "Multi-tool/Knife", "Rope/Paracord", "Duct Tape", "Rain Gear",
        "Extra Clothing", "Hiking Boots", "Sandals", "Towels", "Soap/Hygiene",
        "Toilet Paper", "Shovel", "Ax/Hatchet", "Bear Spray/Canister",
        "Camera", "Binoculars", "Cards/Games", "Books"
    ]

    for page_num, items in enumerate([gear_page1, gear_page2]):
        pdf.new_page()
        pdf.add_text(60, 615, f"GEAR CHECKLIST (Page {page_num + 1})", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 578
        for item in items:
            pdf.add_rect(60, y - 3, 8, 8, 0.4)
            pdf.add_text(75, y, item, font='F1', size=9)
            y -= 22

        # Blank lines for custom items
        y -= 10
        pdf.add_text(60, y, "Additional Items:", font='F2', size=9)
        y -= 18
        for i in range(3):
            pdf.add_rect(60, y - 3, 8, 8, 0.4)
            pdf.add_line(75, y - 2, 372, y - 2, 0.3, gray=0.5)
            y -= 22

    # --- CAMPGROUND CONTACTS PAGE ---
    pdf.new_page()
    pdf.add_text(60, 615, "CAMPGROUND CONTACTS", font='F2', size=14)
    pdf.add_line(60, 603, 372, 603, 0.8)

    pdf.add_text(60, 580, "Name", font='F2', size=9)
    pdf.add_text(180, 580, "Phone", font='F2', size=9)
    pdf.add_text(290, 580, "Website/Notes", font='F2', size=9)
    pdf.add_line(60, 574, 372, 574, 0.5)

    y = 555
    for i in range(20):
        pdf.add_line(60, y, 170, y, 0.3, gray=0.5)
        pdf.add_line(180, y, 280, y, 0.3, gray=0.5)
        pdf.add_line(290, y, 372, y, 0.3, gray=0.5)
        y -= 24

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book29_Camping_Log_Book.pdf')
    print("Book 29 created: Book29_Camping_Log_Book.pdf")

if __name__ == '__main__':
    create_camping_log()
