"""
Book 24: BIRD WATCHING LOG & Field Journal
KDP Interior - 8.5x11 inches (612x792 points)
Title page + copyright + 50 bird sighting entries + Life List page + gear checklist
"""
from pdf_utils import PDFDoc

def create_bird_watching_log():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "BIRD WATCHING LOG", font='F2', size=30)
    pdf.add_centered_text(610, "& Field Journal", font='F4', size=18)
    pdf.add_line(150, 590, 462, 590, 2)
    pdf.add_centered_text(540, "Document Every Sighting", font='F1', size=12)
    pdf.add_centered_text(515, "Species | Location | Behavior | Habitat", font='F1', size=11)
    pdf.add_centered_text(490, "Includes Life List & Gear Checklist", font='F1', size=11)
    pdf.add_centered_text(370, "By", font='F1', size=11)
    pdf.add_centered_text(345, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "BIRD WATCHING LOG & Field Journal", font='F2', size=13)
    pdf.add_centered_text(625, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(590, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(570, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(550, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(510, "Happy birding!", font='F4', size=10)

    # --- 50 BIRD SIGHTING ENTRIES ---
    for entry in range(1, 51):
        pdf.new_page()
        pdf.add_text(72, 750, f"SIGHTING #{entry}", font='F2', size=14)
        pdf.add_line(72, 738, 540, 738, 0.8)

        y = 715

        # Date & Time
        pdf.add_text(72, y, "Date:", font='F2', size=10)
        pdf.add_line(105, y - 2, 230, y - 2, 0.3, gray=0.5)
        pdf.add_text(260, y, "Time:", font='F2', size=10)
        pdf.add_line(293, y - 2, 400, y - 2, 0.3, gray=0.5)
        y -= 26

        # Location
        pdf.add_text(72, y, "Location:", font='F2', size=10)
        pdf.add_line(125, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 26

        # Species
        pdf.add_text(72, y, "Species:", font='F2', size=10)
        pdf.add_line(120, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 26

        # Male/Female/Juvenile
        pdf.add_text(72, y, "Sex/Age:", font='F2', size=10)
        pdf.add_text(130, y, "Male", font='F1', size=10)
        pdf.add_rect(127, y - 3, 10, 12, 0.4)
        pdf.add_text(180, y, "Female", font='F1', size=10)
        pdf.add_rect(177, y - 3, 10, 12, 0.4)
        pdf.add_text(240, y, "Juvenile", font='F1', size=10)
        pdf.add_rect(237, y - 3, 10, 12, 0.4)
        y -= 26

        # Behavior
        pdf.add_text(72, y, "Behavior:", font='F2', size=10)
        pdf.add_line(128, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 26

        # Habitat
        pdf.add_text(72, y, "Habitat:", font='F2', size=10)
        pdf.add_line(120, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 26

        # Weather
        pdf.add_text(72, y, "Weather:", font='F2', size=10)
        pdf.add_line(125, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 26

        # How identified
        pdf.add_text(72, y, "How Identified:", font='F2', size=10)
        pdf.add_line(155, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 30

        # Sketch area
        pdf.add_text(72, y, "Sketch:", font='F2', size=10)
        y -= 10
        pdf.add_rect(72, y - 150, 468, 150, 0.5, gray=0.3)
        y -= 165

        # Notes
        pdf.add_text(72, y, "Notes:", font='F2', size=10)
        y -= 16
        for i in range(3):
            pdf.add_line(72, y, 540, y, 0.3, gray=0.5)
            y -= 20

        # Page number
        pdf.add_centered_text(40, f"- {entry + 2} -", font='F1', size=8)


    # --- LIFE LIST PAGE ---
    pdf.new_page()
    pdf.add_text(72, 750, "LIFE LIST", font='F2', size=14)
    pdf.add_line(72, 738, 540, 738, 0.8)

    # Headers
    pdf.add_text(72, 715, "Species", font='F2', size=9)
    pdf.add_text(250, 715, "Date First Seen", font='F2', size=9)
    pdf.add_text(400, 715, "Location", font='F2', size=9)
    pdf.add_line(72, 710, 540, 710, 0.5)

    y = 692
    for i in range(30):
        pdf.add_text(72, y, f"{i+1}.", font='F1', size=8)
        pdf.add_line(88, y - 2, 240, y - 2, 0.3, gray=0.5)
        pdf.add_line(250, y - 2, 390, y - 2, 0.3, gray=0.5)
        pdf.add_line(400, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 21

    # --- GEAR CHECKLIST PAGE ---
    pdf.new_page()
    pdf.add_text(72, 750, "BIRDING GEAR CHECKLIST", font='F2', size=14)
    pdf.add_line(72, 738, 540, 738, 0.8)

    gear_col1 = [
        "Binoculars", "Spotting Scope", "Tripod", "Field Guide",
        "Notebook & Pencil", "Camera", "Telephoto Lens", "Bird Call App",
        "GPS Device", "Backpack", "Water Bottle", "Snacks",
        "Sunscreen", "Insect Repellent", "Hat"
    ]
    gear_col2 = [
        "Rain Gear", "Comfortable Shoes", "Layered Clothing",
        "Binocular Harness", "Lens Cleaning Kit", "Portable Chair",
        "Camouflage Cover", "First Aid Kit", "Flashlight/Headlamp",
        "Bird Feeder (portable)", "Zip-lock Bags", "Magnifying Glass",
        "Whistle", "Map of Area", "Membership Cards"
    ]

    y = 715
    for i, item in enumerate(gear_col1):
        pdf.add_rect(72, y - 3, 8, 8, 0.4)
        pdf.add_text(87, y, item, font='F1', size=9)
        y -= 22

    y = 715
    for i, item in enumerate(gear_col2):
        pdf.add_rect(310, y - 3, 8, 8, 0.4)
        pdf.add_text(325, y, item, font='F1', size=9)
        y -= 22

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book24_Bird_Watching_Log.pdf')
    print("Book 24 created: Book24_Bird_Watching_Log.pdf")

if __name__ == '__main__':
    create_bird_watching_log()
