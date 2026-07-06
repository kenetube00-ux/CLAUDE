"""
Book 28: THE 90-DAY HABIT TRACKER - Build Better Habits
KDP Interior - 6x9 inches (432x648 points)
Title page + copyright + habit setup page + 12 weekly tracker pages
+ 12 weekly reflection pages + final review page
"""
from pdf_utils import PDFDoc

def create_habit_tracker():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "THE 90-DAY", font='F2', size=26)
    pdf.add_centered_text(495, "HABIT TRACKER", font='F2', size=26)
    pdf.add_line(100, 475, 332, 475, 2)
    pdf.add_centered_text(445, "Build Better Habits", font='F4', size=14)
    pdf.add_centered_text(390, "Track 10 Habits Over 90 Days", font='F1', size=11)
    pdf.add_centered_text(368, "Weekly Reflections & Streak Tracking", font='F1', size=11)
    pdf.add_centered_text(346, "Transform Your Daily Routine", font='F1', size=11)
    pdf.add_centered_text(270, "By", font='F1', size=11)
    pdf.add_centered_text(248, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "THE 90-DAY HABIT TRACKER", font='F2', size=12)
    pdf.add_centered_text(498, "Build Better Habits", font='F1', size=10)
    pdf.add_centered_text(470, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(435, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(415, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(395, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(360, "Small habits, big results.", font='F4', size=10)

    # --- HABIT SETUP PAGE ---
    pdf.new_page()
    pdf.add_text(60, 615, "MY 10 HABITS TO TRACK", font='F2', size=14)
    pdf.add_line(60, 603, 372, 603, 0.8)
    pdf.add_text(60, 580, "List the habits you want to build:", font='F1', size=10)

    y = 555
    for i in range(10):
        pdf.add_text(60, y, f"{i+1}.", font='F2', size=11)
        pdf.add_line(80, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 35

    pdf.add_text(60, y - 20, "Start Date: ______________", font='F1', size=10)
    pdf.add_text(60, y - 45, "End Date: ______________", font='F1', size=10)
    pdf.add_text(60, y - 70, "My WHY:", font='F2', size=10)
    pdf.add_line(60, y - 88, 372, y - 88, 0.3, gray=0.5)
    pdf.add_line(60, y - 108, 372, y - 108, 0.3, gray=0.5)


    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # --- 12 WEEKLY TRACKER PAGES ---
    for week in range(1, 13):
        pdf.new_page()
        pdf.add_text(60, 615, f"WEEK {week} - HABIT TRACKER", font='F2', size=13)
        pdf.add_text(60, 595, f"Dates: _______________", font='F1', size=9)
        pdf.add_line(60, 585, 372, 585, 0.8)

        # Column headers (days)
        y = 565
        pdf.add_text(60, y, "Habit", font='F2', size=8)
        for di, day in enumerate(days):
            pdf.add_text(145 + di * 32, y, day, font='F2', size=7)
        pdf.add_line(60, y - 8, 372, y - 8, 0.5)
        y -= 22

        # 10 habit rows with checkboxes
        for h in range(10):
            pdf.add_text(60, y, f"{h+1}.", font='F1', size=8)
            pdf.add_line(72, y - 2, 138, y - 2, 0.3, gray=0.5)
            for di in range(7):
                pdf.add_rect(147 + di * 32, y - 4, 10, 10, 0.3)
            y -= 28

        # Weekly total
        pdf.add_text(60, y, "Days completed:", font='F2', size=9)
        pdf.add_line(155, y - 2, 200, y - 2, 0.3, gray=0.5)
        pdf.add_text(210, y, "/ 70", font='F1', size=9)

        pdf.add_centered_text(30, f"- {week + 3} -", font='F1', size=8)

    # --- 12 WEEKLY REFLECTION PAGES ---
    for week in range(1, 13):
        pdf.new_page()
        pdf.add_text(60, 615, f"WEEK {week} - REFLECTION", font='F2', size=13)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 578
        # What went well
        pdf.add_text(60, y, "What went well this week:", font='F2', size=10)
        y -= 18
        for i in range(4):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 20
        y -= 12

        # What needs improvement
        pdf.add_text(60, y, "What needs improvement:", font='F2', size=10)
        y -= 18
        for i in range(4):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 20
        y -= 12

        # Streak count
        pdf.add_text(60, y, "Current Streak Count:", font='F2', size=10)
        y -= 22
        for h in range(10):
            pdf.add_text(70, y, f"Habit {h+1}:", font='F1', size=9)
            pdf.add_line(120, y - 2, 180, y - 2, 0.3, gray=0.5)
            if h < 5:
                pdf.add_text(220, y, f"Habit {h+6}:", font='F1', size=9)
                pdf.add_line(270, y - 2, 330, y - 2, 0.3, gray=0.5)
            if h >= 5:
                break
            y -= 18
        y -= 20

        # Reward earned
        pdf.add_text(60, y, "Reward Earned:", font='F2', size=10)
        pdf.add_line(145, y - 2, 372, y - 2, 0.3, gray=0.5)

        pdf.add_centered_text(30, f"- {week + 15} -", font='F1', size=8)


    # --- FINAL REVIEW PAGE ---
    pdf.new_page()
    pdf.add_text(60, 615, "90-DAY FINAL REVIEW", font='F2', size=14)
    pdf.add_line(60, 603, 372, 603, 0.8)

    y = 575
    pdf.add_text(60, y, "Habits I successfully built:", font='F2', size=10)
    y -= 18
    for i in range(5):
        pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
        y -= 20
    y -= 12

    pdf.add_text(60, y, "Habits I struggled with:", font='F2', size=10)
    y -= 18
    for i in range(3):
        pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
        y -= 20
    y -= 12

    pdf.add_text(60, y, "Biggest lesson learned:", font='F2', size=10)
    y -= 18
    for i in range(3):
        pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
        y -= 20
    y -= 12

    pdf.add_text(60, y, "Next 90-day goals:", font='F2', size=10)
    y -= 18
    for i in range(4):
        pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
        y -= 20
    y -= 12

    pdf.add_text(60, y, "Overall rating of my 90 days (1-10):", font='F2', size=10)
    pdf.add_line(265, y - 2, 300, y - 2, 0.5)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book28_Habit_Tracker.pdf')
    print("Book 28 created: Book28_Habit_Tracker.pdf")

if __name__ == '__main__':
    create_habit_tracker()
