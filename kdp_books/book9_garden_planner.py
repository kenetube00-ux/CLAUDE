"""
Book 9: Backyard Garden Planner & Log
KDP Interior - 8.5x11 inches (612x792 points)
"""
from pdf_utils import PDFDoc

def create_garden_planner():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "BACKYARD", font='F2', size=36)
    pdf.add_centered_text(570, "GARDEN PLANNER", font='F2', size=36)
    pdf.add_centered_text(525, "& LOG BOOK", font='F2', size=28)
    pdf.add_line(150, 505, 462, 505, 2)
    pdf.add_centered_text(475, "Plan, Plant, Grow & Track Your Garden", font='F1', size=14)
    pdf.add_centered_text(445, "Seasonal Layouts | Plant Profiles | Harvest Log", font='F1', size=12)
    pdf.add_centered_text(415, "Watering Schedule | Pest Tracker | Seed Inventory", font='F1', size=12)
    pdf.add_centered_text(300, "By", font='F1', size=12)
    pdf.add_centered_text(275, "Daniel Tesfamariam", font='F2', size=18)
    pdf.add_centered_text(200, "Garden Year: 20_____", font='F1', size=14)
    pdf.add_centered_text(170, "Gardener: _________________________", font='F1', size=13)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(550, "Backyard Garden Planner & Log Book", font='F2', size=14)
    pdf.add_centered_text(525, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(490, "Copyright 2026 Daniel Tesfamariam.", font='F1', size=9)
    pdf.add_centered_text(465, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(440, "Published via Amazon KDP", font='F1', size=9)


    # --- GARDEN ZONE INFO ---
    pdf.new_page()
    pdf.add_centered_text(750, "My Garden Information", font='F2', size=18)
    pdf.add_line(72, 735, 540, 735, 1)
    fields = [
        "USDA Hardiness Zone:", "Last Frost Date:",
        "First Frost Date:", "Growing Season Length:",
        "Garden Size:", "Soil Type:",
        "Sun Exposure:", "Water Source:",
    ]
    y = 700
    for field in fields:
        pdf.add_text(72, y, field, font='F2', size=12)
        pdf.add_line(260, y - 3, 500, y - 3, 0.4, gray=0.5)
        y -= 40

    # --- GARDEN GRID LAYOUT (4 pages) ---
    seasons = ["Spring", "Summer", "Fall", "Winter"]
    for season in seasons:
        pdf.new_page()
        pdf.add_centered_text(760, f"{season} Garden Layout", font='F2', size=18)
        pdf.add_centered_text(735, "Draw your garden bed layout below", font='F1', size=11)
        # Grid for drawing
        grid_x, grid_y = 72, 150
        grid_w, grid_h = 468, 540
        pdf.add_rect(grid_x, grid_y, grid_w, grid_h, line_width=1.5)
        # Grid lines
        for gx in range(1, 12):
            x = grid_x + gx * (grid_w // 12)
            pdf.add_line(x, grid_y, x, grid_y + grid_h, 0.3, gray=0.7)
        for gy in range(1, 14):
            y = grid_y + gy * (grid_h // 14)
            pdf.add_line(grid_x, y, grid_x + grid_w, y, 0.3, gray=0.7)
        # Legend area
        pdf.add_text(72, 120, "Legend: ___________________________________________", font='F1', size=10)


    # --- PLANT PROFILE PAGES (12 pages) ---
    for i in range(12):
        pdf.new_page()
        pdf.add_centered_text(760, f"Plant Profile #{i+1}", font='F2', size=16)
        pdf.add_line(72, 745, 540, 745, 0.8)
        plant_fields = [
            ("Plant Name:", 715), ("Variety:", 685), ("Category (Veggie/Herb/Flower):", 655),
            ("Date Planted:", 625), ("Planting Method (Seed/Transplant):", 595),
            ("Spacing:", 565), ("Sun Needs:", 535), ("Water Needs:", 505),
            ("Days to Harvest:", 475), ("Companion Plants:", 445),
        ]
        for label, fy in plant_fields:
            pdf.add_text(72, fy, label, font='F2', size=10)
            pdf.add_line(280, fy - 3, 540, fy - 3, 0.4, gray=0.5)
        pdf.add_text(72, 410, "Growth Notes:", font='F2', size=10)
        for ln in range(6):
            pdf.add_line(72, 385 - ln * 25, 540, 385 - ln * 25, 0.3, gray=0.5)
        pdf.add_text(72, 220, "Harvest Notes:", font='F2', size=10)
        for ln in range(4):
            pdf.add_line(72, 195 - ln * 25, 540, 195 - ln * 25, 0.3, gray=0.5)
        pdf.add_centered_text(40, f"- {i + 8} -", font='F1', size=8)

    # --- WEEKLY WATERING LOG (8 weeks) ---
    for week in range(1, 9):
        pdf.new_page()
        pdf.add_centered_text(760, f"Watering & Care Log - Week {week}", font='F2', size=14)
        pdf.add_line(72, 745, 540, 745, 0.8)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        y = 715
        for day in days:
            pdf.add_text(72, y, day, font='F2', size=11)
            pdf.add_text(160, y, "Watered: Y/N", font='F1', size=10)
            pdf.add_text(270, y, "Fertilized: Y/N", font='F1', size=10)
            pdf.add_text(390, y, "Notes:", font='F1', size=10)
            y -= 20
            pdf.add_line(72, y + 5, 540, y + 5, 0.3, gray=0.5)
            y -= 20
        pdf.add_text(72, y - 10, "Weather This Week: _______________________________________", font='F1', size=10)
        pdf.add_text(72, y - 35, "Pests Noticed: ___________________________________________", font='F1', size=10)


    # --- HARVEST LOG (4 pages) ---
    for page in range(4):
        pdf.new_page()
        pdf.add_centered_text(760, f"Harvest Log (Page {page+1})", font='F2', size=14)
        pdf.add_line(72, 745, 540, 745, 0.8)
        # Table header
        pdf.add_text(72, 720, "Date", font='F2', size=10)
        pdf.add_text(140, 720, "Plant", font='F2', size=10)
        pdf.add_text(240, 720, "Amount", font='F2', size=10)
        pdf.add_text(330, 720, "Quality", font='F2', size=10)
        pdf.add_text(420, 720, "Notes", font='F2', size=10)
        pdf.add_line(72, 712, 540, 712, 0.5)
        y = 695
        for row in range(20):
            pdf.add_line(72, y, 540, y, 0.3, gray=0.5)
            y -= 30

    # --- NOTES ---
    for n in range(2):
        pdf.new_page()
        pdf.add_centered_text(760, "Garden Notes", font='F2', size=14)
        for ln in range(24):
            pdf.add_line(72, 720 - ln * 28, 540, 720 - ln * 28, 0.3, gray=0.5)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(500, "Happy Gardening!", font='F2', size=24)
    pdf.add_centered_text(460, "May your garden grow abundantly.", font='F1', size=14)
    pdf.add_centered_text(410, "If this planner helped you,", font='F1', size=11)
    pdf.add_centered_text(388, "please leave a review on Amazon!", font='F1', size=11)
    pdf.add_centered_text(340, "Also available:", font='F2', size=12)
    pdf.add_centered_text(315, "- Vegetable Garden Planner", font='F1', size=11)
    pdf.add_centered_text(293, "- Container Garden Planner", font='F1', size=11)
    pdf.add_centered_text(271, "- Herb Garden Planner", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book9_Garden_Planner.pdf')
    print("Book 9 created: Book9_Garden_Planner.pdf")

if __name__ == '__main__':
    create_garden_planner()
