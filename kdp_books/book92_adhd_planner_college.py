"""Book 92: ADHD College Planner"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.18)
    pdf.add_centered_text(420, "ADHD COLLEGE", 'F2', 26, 1)
    pdf.add_centered_text(385, "PLANNER", 'F2', 26, 1)
    pdf.add_centered_text(340, "Stay on Track When Your", 'F4', 14, 0.9)
    pdf.add_centered_text(318, "Brain Won't Cooperate", 'F4', 14, 0.9)
    pdf.add_centered_text(270, "Weekly Planning | Assignment Tracking", 'F1', 10, 0.8)
    pdf.add_centered_text(252, "Executive Function Support | Self-Care", 'F1', 10, 0.8)
    pdf.add_centered_text(150, author, 'F2', 12, 0.9)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(420, "ADHD College Planner", 'F2', 13)
    pdf.add_centered_text(398, "Stay on Track When Your Brain Won't Cooperate", 'F4', 10)
    pdf.add_centered_text(365, f"Copyright 2024 {author}. All rights reserved.", 'F1', 9)
    pdf.add_centered_text(345, "No part of this book may be reproduced without permission.", 'F1', 8)
    pdf.add_centered_text(315, "Designed for college students with ADHD.", 'F1', 9)
    pdf.add_centered_text(295, "Not a substitute for professional support.", 'F1', 8)


    # 50 weekly planner pages
    for week in range(1, 51):
        pdf.new_page()
        pdf.add_centered_text(620, f"WEEK {week}", 'F2', 16)
        pdf.add_line(36, 612, 396, 612, 1, 0.3)

        # Class Schedule Grid
        pdf.add_text(36, 595, "CLASS SCHEDULE", 'F2', 9)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        times = ["8am", "10am", "12pm", "2pm", "4pm"]
        col_w = 62
        # Headers
        pdf.add_text(36, 580, "Time", 'F2', 7)
        for i, d in enumerate(days):
            pdf.add_text(80 + i * col_w, 580, d, 'F2', 7)
        y = 568
        for t in times:
            pdf.add_text(36, y, t, 'F3', 7)
            for i in range(5):
                pdf.add_rect(80 + i * col_w, y - 5, col_w - 4, 16, 0.3, 0.5)
            y -= 20

        # Assignment Tracker
        y -= 5
        pdf.add_text(36, y, "ASSIGNMENT TRACKER", 'F2', 9)
        y -= 14
        pdf.add_text(36, y, "Due Date", 'F2', 7)
        pdf.add_text(100, y, "Class", 'F2', 7)
        pdf.add_text(180, y, "Assignment", 'F2', 7)
        pdf.add_text(340, y, "Status", 'F2', 7)
        y -= 12
        for i in range(5):
            pdf.add_line(36, y, 90, y, 0.5, 0.5)
            pdf.add_line(100, y, 170, y, 0.5, 0.5)
            pdf.add_line(180, y, 330, y, 0.5, 0.5)
            pdf.add_rect(340, y - 4, 8, 8, 0.5, 0.3)
            y -= 16

        # Non-negotiables
        y -= 5
        pdf.add_text(36, y, "THIS WEEK'S NON-NEGOTIABLES (pick only 3!):", 'F2', 8)
        y -= 14
        for i in range(3):
            pdf.add_text(36, y, f"{i+1}.", 'F2', 8)
            pdf.add_line(50, y - 2, 396, y - 2, 0.5, 0.5)
            y -= 15

        # Study Session Planner
        y -= 5
        pdf.add_text(36, y, "STUDY SESSION PLANNER", 'F2', 9)
        y -= 14
        pdf.add_text(36, y, "Subject", 'F2', 7)
        pdf.add_text(130, y, "Location", 'F2', 7)
        pdf.add_text(220, y, "Duration", 'F2', 7)
        pdf.add_text(300, y, "Break Reward", 'F2', 7)
        y -= 12
        for i in range(3):
            pdf.add_line(36, y, 120, y, 0.5, 0.5)
            pdf.add_line(130, y, 210, y, 0.5, 0.5)
            pdf.add_line(220, y, 290, y, 0.5, 0.5)
            pdf.add_line(300, y, 396, y, 0.5, 0.5)
            y -= 15

        # Exam Countdown
        y -= 5
        pdf.add_text(36, y, "EXAM COUNTDOWN:", 'F2', 8)
        pdf.add_text(150, y, "Next exam: _____________ in ____ days", 'F1', 8)
        y -= 18


        # Executive Function Check
        pdf.add_text(36, y, "EXECUTIVE FUNCTION CHECK (did I...):", 'F2', 8)
        y -= 14
        checks = [
            "Check syllabus for upcoming deadlines",
            "Email/message professor if confused",
            "Start assignment at least 2 days before due",
        ]
        for ch in checks:
            pdf.add_rect(36, y - 3, 8, 8, 0.5, 0.3)
            pdf.add_text(50, y, ch, 'F1', 7)
            y -= 13

        # Self-Care Check
        y -= 5
        pdf.add_text(36, y, "SELF-CARE CHECK:", 'F2', 8)
        y -= 13
        care = ["Sleep (7+ hrs)", "Meals (3/day)", "Social (talked to someone)", "Movement (any exercise)"]
        for c in care:
            pdf.add_rect(36, y - 3, 8, 8, 0.5, 0.3)
            pdf.add_text(50, y, c, 'F1', 7)
            y -= 13

        # Weekly Wins
        y -= 5
        pdf.add_text(36, y, "WEEKLY WINS (celebrate ANY progress):", 'F2', 8)
        y -= 13
        for i in range(3):
            pdf.add_text(36, y, f"{i+1}.", 'F1', 7)
            pdf.add_line(50, y - 2, 396, y - 2, 0.5, 0.5)
            y -= 13

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book92_ADHD_Planner_College.pdf')
    print("Book92_ADHD_Planner_College.pdf created successfully!")

if __name__ == "__main__":
    create_book()
