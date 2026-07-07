"""
Book 55: My Retirement Planner & Journal - Plan Your Best Chapter
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "MY RETIREMENT", font='F2', size=24)
    pdf.add_centered_text(485, "PLANNER & JOURNAL", font='F2', size=22)
    pdf.add_line(100, 460, 332, 460, 2)
    pdf.add_centered_text(430, "Plan Your Best Chapter", font='F4', size=16)
    pdf.add_centered_text(395, "Goals | Activities | Health | Reflections", font='F1', size=12)
    pdf.add_centered_text(300, "By", font='F1', size=12)
    pdf.add_centered_text(275, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "My Retirement Planner & Journal", font='F2', size=12)
    pdf.add_centered_text(470, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(445, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(415, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(390, "Published via Amazon KDP", font='F1', size=10)

    # --- VISION PAGE ---
    pdf.new_page()
    pdf.add_centered_text(610, "MY RETIREMENT VISION", font='F2', size=18)
    pdf.add_line(80, 595, 352, 595, 1)

    pdf.add_text(50, 565, "My Dreams & Goals:", font='F5', size=12)
    y = 540
    for i in range(5):
        pdf.add_text(60, y, f"{i+1}.", font='F1', size=11)
        pdf.add_line(80, y - 2, 380, y - 2, 0.5, gray=0.5)
        y -= 30

    pdf.add_text(50, y - 10, "My Bucket List:", font='F5', size=12)
    y -= 35
    for i in range(10):
        pdf.add_rect(55, y - 3, 10, 10, line_width=0.5)
        pdf.add_line(80, y - 2, 380, y - 2, 0.5, gray=0.5)
        y -= 25

    # --- FINANCIAL OVERVIEW PAGE ---
    pdf.new_page()
    pdf.add_centered_text(610, "FINANCIAL OVERVIEW", font='F2', size=18)
    pdf.add_line(80, 595, 352, 595, 1)

    pdf.add_text(50, 565, "Income Sources:", font='F5', size=12)
    y = 540
    sources = ["Social Security:", "Pension:", "Investments/401k:", "Part-time work:", "Other:"]
    for src in sources:
        pdf.add_text(60, y, src, font='F4', size=11)
        pdf.add_text(200, y, "$ _______________", font='F1', size=11)
        y -= 25

    y -= 15
    pdf.add_text(50, y, "Monthly Expenses:", font='F5', size=12)
    y -= 25
    expenses = ["Housing:", "Healthcare:", "Food:", "Transportation:", "Utilities:", "Insurance:", "Entertainment:", "Other:"]
    for exp in expenses:
        pdf.add_text(60, y, exp, font='F4', size=11)
        pdf.add_text(200, y, "$ _______________", font='F1', size=11)
        y -= 22

    y -= 15
    pdf.add_text(50, y, "Total Monthly Income: $ _______________", font='F2', size=11)
    y -= 22
    pdf.add_text(50, y, "Total Monthly Expenses: $ _______________", font='F2', size=11)
    y -= 22
    pdf.add_text(50, y, "Savings Goal: $ _______________", font='F2', size=11)

    # --- 12 MONTHLY ACTIVITY PLANNER PAGES ---
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    for month in months:
        pdf.new_page()
        pdf.add_centered_text(610, f"{month} Activity Planner", font='F2', size=16)
        pdf.add_line(80, 595, 352, 595, 1)

        categories = ["Hobbies:", "Social Activities:", "Health & Fitness:", "Volunteer Work:", "Learning Goals:"]
        y = 565
        for cat in categories:
            pdf.add_text(50, y, cat, font='F5', size=11)
            y -= 20
            pdf.add_line(50, y, 380, y, 0.5, gray=0.5)
            y -= 18
            pdf.add_line(50, y, 380, y, 0.5, gray=0.5)
            y -= 22

        # Weekly boxes
        y -= 10
        pdf.add_text(50, y, "Weekly Goals:", font='F5', size=11)
        y -= 20
        weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
        for week in weeks:
            pdf.add_rect(50, y - 30, 170, 35, line_width=0.5)
            pdf.add_text(55, y, week, font='F1', size=9)
            pdf.add_rect(230, y - 30, 152, 35, line_width=0.5)
            y -= 42

    # --- HEALTH TRACKER (5 pages) ---
    # Page 1: Medications
    pdf.new_page()
    pdf.add_centered_text(610, "HEALTH TRACKER - Medications", font='F2', size=16)
    pdf.add_line(80, 595, 352, 595, 1)

    pdf.add_text(50, 570, "Medication", font='F2', size=10)
    pdf.add_text(170, 570, "Dose", font='F2', size=10)
    pdf.add_text(240, 570, "Time", font='F2', size=10)
    pdf.add_text(310, 570, "Notes", font='F2', size=10)
    pdf.add_line(50, 562, 390, 562, 0.5)

    y = 545
    for i in range(15):
        pdf.add_line(50, y, 390, y, 0.3, gray=0.6)
        y -= 28

    # Page 2: Appointments
    pdf.new_page()
    pdf.add_centered_text(610, "HEALTH TRACKER - Appointments", font='F2', size=16)
    pdf.add_line(80, 595, 352, 595, 1)

    pdf.add_text(50, 570, "Date", font='F2', size=10)
    pdf.add_text(130, 570, "Doctor/Specialist", font='F2', size=10)
    pdf.add_text(270, 570, "Reason/Notes", font='F2', size=10)
    pdf.add_line(50, 562, 390, 562, 0.5)

    y = 545
    for i in range(15):
        pdf.add_line(50, y, 390, y, 0.3, gray=0.6)
        y -= 28

    # Pages 3-5: Exercise Log
    for week_set in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(610, f"HEALTH TRACKER - Exercise Log (Set {week_set})", font='F2', size=14)
        pdf.add_line(80, 595, 352, 595, 1)

        y = 565
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in days:
            pdf.add_text(50, y, day, font='F2', size=10)
            pdf.add_text(120, y, "Activity: ________________", font='F1', size=9)
            pdf.add_text(120, y - 15, "Duration: ______  Feeling: ______", font='F1', size=9)
            pdf.add_line(50, y - 25, 390, y - 25, 0.3, gray=0.6)
            y -= 40

    # --- BUCKET LIST TRACKER (2 pages) ---
    for page in range(1, 3):
        pdf.new_page()
        start = (page - 1) * 13 + 1
        end = min(start + 12, 26)
        pdf.add_centered_text(610, f"BUCKET LIST TRACKER (Page {page})", font='F2', size=16)
        pdf.add_line(80, 595, 352, 595, 1)

        pdf.add_text(50, 575, "#", font='F2', size=10)
        pdf.add_text(70, 575, "Goal/Dream", font='F2', size=10)
        pdf.add_text(280, 575, "Date Done", font='F2', size=10)
        pdf.add_text(350, 575, "Done?", font='F2', size=10)

        y = 555
        for i in range(start, end):
            pdf.add_text(50, y, f"{i}.", font='F1', size=10)
            pdf.add_line(70, y - 2, 270, y - 2, 0.3, gray=0.5)
            pdf.add_line(280, y - 2, 340, y - 2, 0.3, gray=0.5)
            pdf.add_rect(355, y - 5, 10, 10, line_width=0.5)
            y -= 25

    # --- REFLECTION PAGES (5 pages) ---
    reflections = [
        "What Retirement Means to Me",
        "My Legacy - What I Want to Be Remembered For",
        "Letters to My Loved Ones",
        "Wisdom I Want to Share",
        "Gratitude - What I Am Thankful For",
    ]

    for title in reflections:
        pdf.new_page()
        pdf.add_centered_text(610, title, font='F2', size=14)
        pdf.add_line(80, 595, 352, 595, 1)

        y = 565
        for i in range(18):
            pdf.add_line(50, y, 380, y, 0.5, gray=0.5)
            y -= 28

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book55_Retirement_Planner.pdf')
    print("Book 55 created: Book55_Retirement_Planner.pdf")

if __name__ == '__main__':
    create_book()
