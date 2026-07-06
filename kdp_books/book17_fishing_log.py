"""
Book 17: FISHING LOG BOOK
KDP Interior - 6x9 inches (432x648 points)
50 catch log entries, personal best records, gear checklist
"""
from pdf_utils import PDFDoc

def create_fishing_log():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "FISHING", font='F2', size=32)
    pdf.add_centered_text(478, "LOG BOOK", font='F2', size=28)
    pdf.add_line(100, 458, 332, 458, 2)
    pdf.add_centered_text(425, "Record Every Catch", font='F1', size=13)
    pdf.add_centered_text(400, "Date | Location | Weather | Species | Size", font='F1', size=11)
    pdf.add_centered_text(378, "Personal Best Records & Gear Checklist", font='F1', size=11)
    pdf.add_centered_text(270, "By", font='F1', size=11)
    pdf.add_centered_text(248, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(520, "FISHING LOG BOOK", font='F2', size=12)
    pdf.add_centered_text(495, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(435, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(410, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(370, "Tight lines and big catches!", font='F1', size=10)

    # --- 50 CATCH LOG ENTRIES ---
    for entry in range(1, 51):
        pdf.new_page()
        pdf.add_text(60, 615, f"CATCH #{entry}", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 580
        # Date
        pdf.add_text(60, y, "Date:", font='F2', size=10)
        pdf.add_line(95, y - 2, 200, y - 2, 0.3, gray=0.5)
        pdf.add_text(220, y, "Time:", font='F2', size=10)
        pdf.add_line(255, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Location
        pdf.add_text(60, y, "Location:", font='F2', size=10)
        pdf.add_line(115, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Weather
        pdf.add_text(60, y, "Weather:", font='F2', size=10)
        pdf.add_line(115, y - 2, 250, y - 2, 0.3, gray=0.5)
        pdf.add_text(260, y, "Wind:", font='F2', size=10)
        pdf.add_line(295, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Water conditions
        pdf.add_text(60, y, "Water Temp:", font='F2', size=10)
        pdf.add_line(130, y - 2, 200, y - 2, 0.3, gray=0.5)
        pdf.add_text(210, y, "Water Clarity:", font='F2', size=10)
        pdf.add_line(290, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Bait/Lure
        pdf.add_text(60, y, "Bait/Lure:", font='F2', size=10)
        pdf.add_line(120, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Species
        pdf.add_text(60, y, "Species:", font='F2', size=10)
        pdf.add_line(110, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Size & Weight
        pdf.add_text(60, y, "Size:", font='F2', size=10)
        pdf.add_line(90, y - 2, 200, y - 2, 0.3, gray=0.5)
        pdf.add_text(220, y, "Weight:", font='F2', size=10)
        pdf.add_line(265, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Kept/Released
        pdf.add_text(60, y, "Kept  /  Released", font='F2', size=10)
        pdf.add_text(220, y, "Depth:", font='F2', size=10)
        pdf.add_line(260, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 35

        # Notes
        pdf.add_text(60, y, "Notes:", font='F2', size=10)
        y -= 18
        for i in range(5):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 22

        # Page number
        pdf.add_centered_text(30, f"- {entry + 2} -", font='F1', size=8)

    # --- PERSONAL BEST RECORDS PAGE ---
    pdf.new_page()
    pdf.add_text(60, 615, "PERSONAL BEST RECORDS", font='F2', size=14)
    pdf.add_line(60, 603, 372, 603, 0.8)

    # Table headers
    pdf.add_text(60, 580, "Species", font='F2', size=9)
    pdf.add_text(160, 580, "Size", font='F2', size=9)
    pdf.add_text(210, 580, "Weight", font='F2', size=9)
    pdf.add_text(270, 580, "Date", font='F2', size=9)
    pdf.add_text(330, 580, "Location", font='F2', size=9)
    pdf.add_line(60, 575, 372, 575, 0.5)

    y = 555
    for i in range(20):
        pdf.add_line(60, y, 150, y, 0.3, gray=0.5)
        pdf.add_line(160, y, 200, y, 0.3, gray=0.5)
        pdf.add_line(210, y, 260, y, 0.3, gray=0.5)
        pdf.add_line(270, y, 320, y, 0.3, gray=0.5)
        pdf.add_line(330, y, 372, y, 0.3, gray=0.5)
        y -= 25

    # --- GEAR CHECKLIST PAGE ---
    pdf.new_page()
    pdf.add_text(60, 615, "GEAR CHECKLIST", font='F2', size=14)
    pdf.add_line(60, 603, 372, 603, 0.8)

    gear_items = [
        "Rods & Reels", "Tackle Box", "Hooks (various sizes)", "Sinkers/Weights",
        "Bobbers/Floats", "Lures", "Live Bait", "Line (extra spools)",
        "Pliers/Multi-tool", "Knife/Scissors", "Net", "Cooler/Ice",
        "Bucket", "Sunscreen", "Polarized Sunglasses", "Hat",
        "Rain Gear", "First Aid Kit", "Fishing License", "Measuring Tape",
        "Scale", "Camera", "Snacks/Water", "Stringer"
    ]

    y = 580
    for i, item in enumerate(gear_items):
        if i < 12:
            pdf.add_rect(60, y - 3, 8, 8, 0.4)
            pdf.add_text(75, y, item, font='F1', size=9)
        else:
            pdf.add_rect(220, y + (12 * 22) - 3, 8, 8, 0.4)
            pdf.add_text(235, y + (12 * 22), gear_items[i], font='F1', size=9)
        if i < 12:
            y -= 22

    # Additional gear lines
    y = 580 - 12 * 22 - 20
    pdf.add_text(60, y, "Additional Gear:", font='F2', size=10)
    y -= 18
    for i in range(5):
        pdf.add_rect(60, y - 3, 8, 8, 0.4)
        pdf.add_line(75, y, 372, y, 0.3, gray=0.5)
        y -= 22

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book17_Fishing_Log_Book.pdf')
    print("Book 17 created: Book17_Fishing_Log_Book.pdf")

if __name__ == '__main__':
    create_fishing_log()
