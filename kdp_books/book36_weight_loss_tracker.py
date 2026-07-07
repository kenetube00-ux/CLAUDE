"""
Book 36: Weight Loss Tracker & Fitness Journal
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(540, "WEIGHT LOSS", font='F2', size=28)
    pdf.add_centered_text(500, "TRACKER &", font='F2', size=20)
    pdf.add_centered_text(465, "FITNESS JOURNAL", font='F2', size=26)
    pdf.add_line(100, 445, 332, 445, 2)
    pdf.add_centered_text(415, "12-Week Body Transformation Log", font='F1', size=12)
    pdf.add_centered_text(390, "Daily Weight | Meals | Exercise | Progress", font='F1', size=10)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(235, "Daniel Tesfamariam", font='F2', size=16)


    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "Weight Loss Tracker & Fitness Journal", font='F2', size=13)
    pdf.add_centered_text(475, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(395, "Published via Amazon KDP", font='F1', size=9)

    # --- GOAL SETTING PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "MY WEIGHT LOSS GOALS", font='F2', size=16)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 570
    goals = [
        "Start Weight: _____________ lbs/kg",
        "Goal Weight: ______________ lbs/kg",
        "Weight to Lose: ___________ lbs/kg",
        "Timeline: _________________ weeks",
        "Start Date: ___/___/______",
        "Target Date: ___/___/______",
        "",
        "My Motivation:",
        "________________________________________",
        "________________________________________",
        "",
        "Weekly Goal: Lose ______ lbs/kg per week",
        "Daily Calorie Target: _________ cal",
        "Daily Water Goal: _________ glasses",
        "Exercise Goal: _________ min/day",
    ]
    for line in goals:
        if line == "":
            y -= 15
        else:
            pdf.add_text(70, y, line, font='F1', size=11)
            y -= 28


    # --- 12 WEEKLY TRACKER PAGES ---
    for week in range(1, 13):
        pdf.new_page()
        pdf.add_text(60, 615, f"Week {week}", font='F2', size=14)
        pdf.add_text(240, 615, "Dates: ___/___  to  ___/___", font='F1', size=9)
        pdf.add_line(60, 603, 372, 603, 0.8)

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        y = 580
        for day in days:
            pdf.add_text(60, y, day, font='F2', size=9)
            y -= 15
            pdf.add_text(70, y, "Weight:____", font='F1', size=8)
            pdf.add_text(145, y, "Cals:____", font='F1', size=8)
            pdf.add_text(210, y, "Water:____", font='F1', size=8)
            pdf.add_text(285, y, "Sleep:__hr", font='F1', size=8)
            y -= 14
            pdf.add_text(70, y, "Exercise:___________________", font='F1', size=8)
            pdf.add_text(250, y, "___min", font='F1', size=8)
            pdf.add_text(300, y, "Mood: ___", font='F1', size=8)
            y -= 14
            pdf.add_text(70, y, "Meals: B:_________ L:_________ D:_________", font='F1', size=7)
            y -= 8
            pdf.add_line(60, y, 372, y, 0.2, gray=0.5)
            y -= 10

        # Weekly summary
        y -= 5
        pdf.add_text(60, y, "Weekly Summary:", font='F2', size=9)
        y -= 16
        pdf.add_text(70, y, "Start Weight: _______  End Weight: _______  Lost: _______", font='F1', size=8)
        pdf.add_centered_text(35, f"- {week + 3} -", font='F1', size=8)


    # --- PROGRESS CHART PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "12-WEEK PROGRESS CHART", font='F2', size=14)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 570
    pdf.add_text(60, y, "Week", font='F2', size=9)
    pdf.add_text(110, y, "Weight", font='F2', size=9)
    pdf.add_text(175, y, "Change", font='F2', size=9)
    pdf.add_text(240, y, "Total Lost", font='F2', size=9)
    pdf.add_text(320, y, "Notes", font='F2', size=9)
    y -= 5
    pdf.add_line(60, y, 372, y, 0.5)
    for w in range(1, 13):
        y -= 28
        pdf.add_text(65, y, f"{w}", font='F1', size=9)
        pdf.add_text(110, y, "________", font='F1', size=9)
        pdf.add_text(175, y, "________", font='F1', size=9)
        pdf.add_text(240, y, "________", font='F1', size=9)
        pdf.add_text(320, y, "________", font='F1', size=9)
        y -= 3
        pdf.add_line(60, y, 372, y, 0.2, gray=0.5)

    # --- BODY MEASUREMENTS PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "BODY MEASUREMENTS", font='F2', size=14)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 565
    pdf.add_text(60, y, "Measurement", font='F2', size=10)
    pdf.add_text(200, y, "Before", font='F2', size=10)
    pdf.add_text(290, y, "After", font='F2', size=10)
    y -= 5
    pdf.add_line(60, y, 372, y, 0.5)
    measurements = ["Neck", "Chest", "Waist", "Hips", "Right Thigh", "Left Thigh", "Right Arm", "Left Arm"]
    for m in measurements:
        y -= 32
        pdf.add_text(60, y, m, font='F1', size=10)
        pdf.add_text(200, y, "____________", font='F1', size=10)
        pdf.add_text(290, y, "____________", font='F1', size=10)
        y -= 3
        pdf.add_line(60, y, 372, y, 0.2, gray=0.5)

    y -= 30
    pdf.add_text(60, y, "Before Photo Date: ___/___/______", font='F1', size=9)
    y -= 20
    pdf.add_text(60, y, "After Photo Date: ___/___/______", font='F1', size=9)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book36_Weight_Loss_Tracker.pdf')
    print("Book 36 created: Book36_Weight_Loss_Tracker.pdf")

if __name__ == '__main__':
    create_book()
