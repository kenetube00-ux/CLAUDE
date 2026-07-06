"""
Book 14: ADHD-Friendly Daily Planner
KDP Interior - 6x9 inches (432x648 points)
Priority tasks, brain dump, time blocks, mood check, meds tracker, water tracker
"""
from pdf_utils import PDFDoc

def create_adhd_planner():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "ADHD-Friendly", font='F2', size=26)
    pdf.add_centered_text(480, "Daily Planner", font='F2', size=26)
    pdf.add_line(100, 460, 332, 460, 2)
    pdf.add_centered_text(425, "Designed for the ADHD Brain", font='F1', size=13)
    pdf.add_centered_text(400, "Priority Tasks | Brain Dump | Time Blocks", font='F1', size=11)
    pdf.add_centered_text(378, "Mood Check | Meds Tracker | Water Tracker", font='F1', size=11)
    pdf.add_centered_text(280, "By", font='F1', size=11)
    pdf.add_centered_text(258, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(520, "ADHD-Friendly Daily Planner", font='F2', size=12)
    pdf.add_centered_text(495, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(435, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(410, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(370, "This planner is designed to work with your brain, not against it.", font='F1', size=9)

    # --- 30 DAILY PLANNER PAGES ---
    for day in range(1, 31):
        pdf.new_page()
        pdf.add_text(60, 615, f"Day {day}", font='F2', size=14)
        pdf.add_text(280, 615, "Date: ___/___/______", font='F1', size=10)
        pdf.add_line(60, 603, 372, 603, 0.8)

        # Priority Tasks (Top 3)
        pdf.add_text(60, 582, "TOP 3 PRIORITIES", font='F2', size=11)
        y = 560
        for i in range(1, 4):
            pdf.add_rect(60, y - 3, 10, 10, 0.5)
            pdf.add_line(80, y, 372, y, 0.3, gray=0.5)
            y -= 22

        # Brain Dump Section
        y -= 8
        pdf.add_text(60, y, "BRAIN DUMP", font='F2', size=11)
        pdf.add_rect(60, y - 85, 312, 75, 0.5)
        y -= 100

        # Time Blocks
        pdf.add_text(60, y, "TIME BLOCKS", font='F2', size=11)
        y -= 18
        blocks = ["Morning", "Afternoon", "Evening"]
        for block in blocks:
            pdf.add_text(65, y, f"{block}:", font='F2', size=9)
            pdf.add_line(130, y - 2, 372, y - 2, 0.3, gray=0.5)
            y -= 16
            pdf.add_line(130, y - 2, 372, y - 2, 0.3, gray=0.5)
            y -= 20

        # Mood Check
        y -= 5
        pdf.add_text(60, y, "MOOD CHECK:", font='F2', size=10)
        pdf.add_text(160, y, "1  2  3  4  5  6  7  8  9  10", font='F1', size=10)
        y -= 20

        # Did I take meds
        pdf.add_text(60, y, "Did I take meds:  Y  /  N", font='F2', size=10)
        y -= 25

        # Water Tracker (8 glasses)
        pdf.add_text(60, y, "WATER TRACKER:", font='F2', size=10)
        y -= 5
        for g in range(8):
            gx = 65 + g * 35
            pdf.add_rect(gx, y - 18, 25, 15, 0.5)
        y -= 30

        # Win of the Day
        pdf.add_text(60, y, "WIN OF THE DAY:", font='F2', size=10)
        y -= 3
        pdf.add_line(60, y - 15, 372, y - 15, 0.3, gray=0.5)

        # Page number
        pdf.add_centered_text(30, f"- {day + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book14_ADHD_Daily_Planner.pdf')
    print("Book 14 created: Book14_ADHD_Daily_Planner.pdf")

if __name__ == '__main__':
    create_adhd_planner()
