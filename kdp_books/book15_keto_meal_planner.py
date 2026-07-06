"""
Book 15: KETO Meal Planner & Macro Tracker
KDP Interior - 6x9 inches (432x648 points)
12 weekly meal plan pages, 8 grocery list pages, 3 notes pages
"""
from pdf_utils import PDFDoc

def create_keto_planner():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "KETO", font='F2', size=32)
    pdf.add_centered_text(478, "Meal Planner", font='F2', size=24)
    pdf.add_centered_text(448, "& Macro Tracker", font='F2', size=20)
    pdf.add_line(100, 428, 332, 428, 2)
    pdf.add_centered_text(398, "12 Weeks of Meal Planning", font='F1', size=12)
    pdf.add_centered_text(375, "Breakfast | Lunch | Dinner | Snacks", font='F1', size=11)
    pdf.add_centered_text(352, "Fat | Protein | Carbs | Calories", font='F1', size=11)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(238, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(520, "KETO Meal Planner & Macro Tracker", font='F2', size=12)
    pdf.add_centered_text(495, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(435, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(410, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(370, "Track your macros. Reach your goals.", font='F1', size=10)

    # --- 12 WEEKLY MEAL PLAN PAGES ---
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for week in range(1, 13):
        pdf.new_page()
        pdf.add_text(60, 615, f"WEEK {week}", font='F2', size=14)
        pdf.add_text(220, 615, "Dates: ___/___  to  ___/___", font='F1', size=9)
        pdf.add_line(60, 603, 372, 603, 0.8)

        # Column headers
        pdf.add_text(60, 587, "Day", font='F2', size=7)
        pdf.add_text(95, 587, "Meal", font='F2', size=7)
        pdf.add_text(215, 587, "Fat", font='F2', size=7)
        pdf.add_text(250, 587, "Pro", font='F2', size=7)
        pdf.add_text(285, 587, "Carb", font='F2', size=7)
        pdf.add_text(325, 587, "Cal", font='F2', size=7)
        pdf.add_line(60, 583, 372, 583, 0.5)

        y = 572
        meals = ["B:", "L:", "D:", "S:"]
        for d_idx, day in enumerate(days):
            pdf.add_text(60, y, day, font='F2', size=7)
            for m_idx, meal in enumerate(meals):
                row_y = y - m_idx * 11
                pdf.add_text(95, row_y, meal, font='F3', size=6)
                pdf.add_line(107, row_y - 2, 205, row_y - 2, 0.2, gray=0.5)
                pdf.add_line(215, row_y - 2, 240, row_y - 2, 0.2, gray=0.5)
                pdf.add_line(250, row_y - 2, 275, row_y - 2, 0.2, gray=0.5)
                pdf.add_line(285, row_y - 2, 315, row_y - 2, 0.2, gray=0.5)
                pdf.add_line(325, row_y - 2, 360, row_y - 2, 0.2, gray=0.5)
            y -= 52
            if d_idx < 6:
                pdf.add_line(60, y + 6, 372, y + 6, 0.3, gray=0.4)

        # Weekly totals
        pdf.add_text(60, 50, "Weekly Goal - Fat:___g  Protein:___g  Carbs:___g  Calories:____", font='F1', size=8)
        pdf.add_centered_text(30, f"- {week + 2} -", font='F1', size=8)

    # --- 8 GROCERY LIST PAGES ---
    for g_page in range(1, 9):
        pdf.new_page()
        pdf.add_text(60, 615, f"GROCERY LIST", font='F2', size=14)
        pdf.add_text(240, 615, f"Week: ___", font='F1', size=10)
        pdf.add_line(60, 603, 372, 603, 0.8)

        # Two columns of items
        y = 580
        for i in range(22):
            # Left column
            pdf.add_rect(60, y - 3, 8, 8, 0.4)
            pdf.add_line(75, y, 205, y, 0.3, gray=0.5)
            # Right column
            pdf.add_rect(220, y - 3, 8, 8, 0.4)
            pdf.add_line(235, y, 372, y, 0.3, gray=0.5)
            y -= 25

        pdf.add_centered_text(30, f"- {14 + g_page} -", font='F1', size=8)

    # --- 3 NOTES PAGES ---
    for n_page in range(1, 4):
        pdf.new_page()
        pdf.add_text(60, 615, "NOTES & RECIPES", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 580
        while y > 60:
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 22

        pdf.add_centered_text(30, f"- {22 + n_page} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book15_Keto_Meal_Planner.pdf')
    print("Book 15 created: Book15_Keto_Meal_Planner.pdf")

if __name__ == '__main__':
    create_keto_planner()
