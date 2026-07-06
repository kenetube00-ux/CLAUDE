"""
Book 16: HOME MAINTENANCE Log & Planner
KDP Interior - 8.5x11 inches (612x792 points)
Monthly checklists, contractor contacts, warranty tracker, appliance info, repair logs
"""
from pdf_utils import PDFDoc

def create_home_maintenance():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "HOME MAINTENANCE", font='F2', size=30)
    pdf.add_centered_text(575, "Log & Planner", font='F2', size=26)
    pdf.add_line(150, 555, 462, 555, 2)
    pdf.add_centered_text(520, "Monthly Checklists | Repair Logs | Warranty Tracker", font='F1', size=13)
    pdf.add_centered_text(495, "Contractor Contacts | Appliance Information", font='F1', size=13)
    pdf.add_centered_text(380, "By", font='F1', size=12)
    pdf.add_centered_text(355, "Daniel Tesfamariam", font='F2', size=18)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(620, "HOME MAINTENANCE Log & Planner", font='F2', size=14)
    pdf.add_centered_text(590, "By Daniel Tesfamariam", font='F2', size=12)
    pdf.add_centered_text(550, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(525, "ISBN: _______________", font='F1', size=10)
    pdf.add_centered_text(500, "Published via Amazon KDP", font='F1', size=10)
    pdf.add_centered_text(455, "Keep your home running smoothly all year long.", font='F1', size=11)

    # --- 12 MONTHLY CHECKLIST PAGES ---
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    monthly_tasks = {
        "January": ["Check smoke/CO detectors", "Inspect pipes for freezing", "Clean range hood filter",
                    "Test sump pump", "Check weather stripping", "Inspect attic for ice dams"],
        "February": ["Service HVAC system", "Clean dryer vent", "Check fire extinguishers",
                     "Inspect caulking around tubs", "Test garage door auto-reverse", "Deep clean carpets"],
        "March": ["Replace HVAC filter", "Clean gutters", "Inspect roof for winter damage",
                  "Service lawn mower", "Check outdoor faucets", "Power wash deck/patio"],
        "April": ["Test irrigation system", "Inspect foundation for cracks", "Clean windows",
                  "Check deck/porch for rot", "Fertilize lawn", "Service AC unit"],
        "May": ["Check attic ventilation", "Inspect siding", "Clean ceiling fans",
                "Test outdoor GFCI outlets", "Trim trees from house", "Seal driveway cracks"],
        "June": ["Replace HVAC filter", "Check grout/caulking", "Inspect plumbing for leaks",
                 "Clean garbage disposal", "Check window screens", "Inspect garage door hardware"],
        "July": ["Deep clean kitchen appliances", "Check water heater", "Inspect electrical panel",
                 "Clean drains", "Check exterior paint", "Test home security system"],
        "August": ["Inspect roof", "Clean and inspect chimney", "Back-to-school prep home check",
                   "Check weatherstripping", "Service sprinkler system", "Inspect fencing"],
        "September": ["Replace HVAC filter", "Clean gutters", "Seal gaps around doors/windows",
                      "Drain outdoor hoses", "Test heating system", "Check insulation"],
        "October": ["Winterize irrigation", "Reverse ceiling fans", "Inspect/clean fireplace",
                    "Check smoke detectors", "Rake leaves from yard", "Store outdoor furniture"],
        "November": ["Protect pipes from freezing", "Check roof for loose shingles",
                     "Clean dryer vent", "Service snow blower", "Test sump pump", "Check CO detectors"],
        "December": ["Replace HVAC filter", "Check holiday light circuits", "Inspect water heater",
                     "Clean refrigerator coils", "Check exterior lights", "Year-end maintenance review"],
    }

    for month in months:
        pdf.new_page()
        pdf.add_text(72, 740, f"{month.upper()} CHECKLIST", font='F2', size=16)
        pdf.add_text(400, 740, "Year: _______", font='F1', size=11)
        pdf.add_line(72, 728, 540, 728, 0.8)

        tasks = monthly_tasks[month]
        y = 700
        for task in tasks:
            pdf.add_rect(72, y - 3, 10, 10, 0.5)
            pdf.add_text(90, y, task, font='F1', size=11)
            pdf.add_text(360, y, "Done: ___/___", font='F1', size=9)
            pdf.add_text(450, y, "Notes:", font='F1', size=9)
            pdf.add_line(480, y - 2, 540, y - 2, 0.3, gray=0.5)
            y -= 28

        # Additional custom tasks section
        y -= 15
        pdf.add_text(72, y, "Additional Tasks:", font='F2', size=11)
        y -= 20
        for i in range(5):
            pdf.add_rect(72, y - 3, 10, 10, 0.5)
            pdf.add_line(90, y, 540, y, 0.3, gray=0.5)
            y -= 25

        # Notes section
        y -= 15
        pdf.add_text(72, y, "Monthly Notes:", font='F2', size=11)
        y -= 18
        for i in range(4):
            pdf.add_line(72, y, 540, y, 0.3, gray=0.5)
            y -= 22

    # --- CONTRACTOR CONTACT PAGE ---
    pdf.new_page()
    pdf.add_text(72, 740, "CONTRACTOR CONTACTS", font='F2', size=16)
    pdf.add_line(72, 728, 540, 728, 0.8)

    categories = ["Plumber", "Electrician", "HVAC Tech", "Roofer", "Handyman",
                  "Landscaper", "Pest Control", "Painter", "Locksmith", "Appliance Repair"]
    y = 700
    for cat in categories:
        pdf.add_text(72, y, f"{cat}:", font='F2', size=10)
        pdf.add_text(170, y, "Name:", font='F1', size=9)
        pdf.add_line(200, y - 2, 330, y - 2, 0.3, gray=0.5)
        pdf.add_text(340, y, "Phone:", font='F1', size=9)
        pdf.add_line(375, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 18
        pdf.add_text(170, y, "Email:", font='F1', size=9)
        pdf.add_line(200, y - 2, 400, y - 2, 0.3, gray=0.5)
        pdf.add_text(410, y, "Rating:", font='F1', size=9)
        pdf.add_line(450, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 30

    # --- WARRANTY TRACKER PAGE ---
    pdf.new_page()
    pdf.add_text(72, 740, "WARRANTY TRACKER", font='F2', size=16)
    pdf.add_line(72, 728, 540, 728, 0.8)

    # Table headers
    pdf.add_text(72, 705, "Item", font='F2', size=9)
    pdf.add_text(190, 705, "Brand/Model", font='F2', size=9)
    pdf.add_text(310, 705, "Purchase Date", font='F2', size=9)
    pdf.add_text(410, 705, "Warranty Exp", font='F2', size=9)
    pdf.add_text(505, 705, "Notes", font='F2', size=9)
    pdf.add_line(72, 700, 540, 700, 0.5)

    y = 682
    for i in range(20):
        pdf.add_line(72, y, 180, y, 0.3, gray=0.5)
        pdf.add_line(190, y, 300, y, 0.3, gray=0.5)
        pdf.add_line(310, y, 400, y, 0.3, gray=0.5)
        pdf.add_line(410, y, 495, y, 0.3, gray=0.5)
        pdf.add_line(505, y, 540, y, 0.3, gray=0.5)
        y -= 28

    # --- APPLIANCE INFO PAGE ---
    pdf.new_page()
    pdf.add_text(72, 740, "APPLIANCE INFORMATION", font='F2', size=16)
    pdf.add_line(72, 728, 540, 728, 0.8)

    appliances = ["Refrigerator", "Dishwasher", "Oven/Range", "Washer", "Dryer",
                  "Water Heater", "Furnace/Boiler", "AC Unit", "Microwave", "Garbage Disposal"]
    y = 700
    for app in appliances:
        pdf.add_text(72, y, f"{app}:", font='F2', size=10)
        y -= 16
        pdf.add_text(85, y, "Brand:", font='F1', size=8)
        pdf.add_line(115, y - 2, 210, y - 2, 0.3, gray=0.5)
        pdf.add_text(220, y, "Model#:", font='F1', size=8)
        pdf.add_line(260, y - 2, 370, y - 2, 0.3, gray=0.5)
        pdf.add_text(380, y, "Serial#:", font='F1', size=8)
        pdf.add_line(420, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 16
        pdf.add_text(85, y, "Purchased:", font='F1', size=8)
        pdf.add_line(135, y - 2, 210, y - 2, 0.3, gray=0.5)
        pdf.add_text(220, y, "Filter/Part#:", font='F1', size=8)
        pdf.add_line(280, y - 2, 400, y - 2, 0.3, gray=0.5)
        y -= 28

    # --- 15 REPAIR LOG PAGES ---
    for r_page in range(1, 16):
        pdf.new_page()
        pdf.add_text(72, 740, f"REPAIR LOG", font='F2', size=16)
        pdf.add_text(400, 740, f"Entry #{r_page}", font='F1', size=11)
        pdf.add_line(72, 728, 540, 728, 0.8)

        pdf.add_text(72, 700, "Date: ___/___/______", font='F1', size=11)
        pdf.add_text(250, 700, "Priority:  High  |  Medium  |  Low", font='F1', size=11)

        pdf.add_text(72, 670, "Location/Room:", font='F2', size=11)
        pdf.add_line(180, 668, 540, 668, 0.3, gray=0.5)

        pdf.add_text(72, 640, "Issue Description:", font='F2', size=11)
        for i in range(3):
            pdf.add_line(72, 618 - i * 22, 540, 618 - i * 22, 0.3, gray=0.5)

        pdf.add_text(72, 545, "Repaired By:  Self  |  Contractor: ___________________", font='F1', size=11)

        pdf.add_text(72, 515, "Parts/Materials Used:", font='F2', size=11)
        for i in range(2):
            pdf.add_line(72, 493 - i * 22, 540, 493 - i * 22, 0.3, gray=0.5)

        pdf.add_text(72, 440, "Cost: $________", font='F1', size=11)
        pdf.add_text(220, 440, "Time Spent: _______hrs", font='F1', size=11)

        pdf.add_text(72, 410, "Resolution Notes:", font='F2', size=11)
        for i in range(4):
            pdf.add_line(72, 388 - i * 22, 540, 388 - i * 22, 0.3, gray=0.5)

        pdf.add_text(72, 300, "Follow-up Needed:  Yes  |  No", font='F1', size=11)
        pdf.add_text(72, 275, "Follow-up Date: ___/___/______", font='F1', size=11)
        pdf.add_text(72, 250, "Notes:", font='F1', size=11)
        pdf.add_line(72, 230, 540, 230, 0.3, gray=0.5)
        pdf.add_line(72, 208, 540, 208, 0.3, gray=0.5)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book16_Home_Maintenance_Log.pdf')
    print("Book 16 created: Book16_Home_Maintenance_Log.pdf")

if __name__ == '__main__':
    create_home_maintenance()
