"""Book 86: Multi-Child Homeschool Planner"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.1)
    pdf.add_centered_text(520, "THE MULTI-CHILD", 'F2', 26, 1)
    pdf.add_centered_text(480, "HOMESCHOOL PLANNER", 'F2', 26, 1)
    pdf.add_centered_text(430, "Organize Every Student, Every Subject", 'F4', 15, 0.9)
    pdf.add_centered_text(380, "4 Students | Weekly Plans | Attendance | Grades", 'F1', 12, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "The Multi-Child Homeschool Planner", 'F2', 13)
    pdf.add_centered_text(478, "Organize Every Student, Every Subject", 'F4', 11)

    pdf.add_centered_text(448, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(428, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(398, "This planner accommodates up to 4 students across all subjects.", 'F1', 9)
    pdf.add_centered_text(378, "Customize it to fit YOUR family's homeschool style.", 'F1', 9)

    # Student Profile Pages (4 students)
    students = ["Student 1", "Student 2", "Student 3", "Student 4"]
    for student in students:
        pdf.new_page()
        pdf.add_filled_rect(50, 740, 512, 30, 0.88)
        pdf.add_text(60, 748, f"STUDENT PROFILE: {student.upper()}", 'F2', 14)
        y = 710
        profile_fields = [
            ("Name:", 1), ("Grade Level:", 1), ("Age:", 1),
            ("Learning Style (visual/auditory/kinesthetic):", 1),
            ("Strengths:", 2), ("Areas for Growth:", 2),
            ("Goals for This Year:", 3),
            ("Special Accommodations/Notes:", 3),
            ("Favorite Subjects:", 2),
            ("Extracurricular Activities:", 2),
            ("Testing/Assessment Schedule:", 2),
        ]
        for label, lines in profile_fields:
            pdf.add_text(72, y, label, 'F2', 10)
            y -= 16
            for _ in range(lines):
                pdf.add_line(90, y, 540, y, 0.5, 0.5)
                y -= 16
            y -= 6

    # 36 Weekly Planning Pages
    subjects = ["Math", "Lang Arts", "Science", "History", "Elective"]
    for week in range(1, 37):
        pdf.new_page()
        pdf.add_filled_rect(50, 750, 512, 28, 0.85)
        pdf.add_text(60, 758, f"WEEK {week}", 'F2', 13)
        pdf.add_text(200, 758, "Dates: ___/___  to  ___/___", 'F1', 9)
        
        # 4 student columns
        col_w = 120
        start_x = 72
        y = 730
        # Header row
        pdf.add_text(start_x, y, "SUBJECT", 'F2', 8)
        for i, s in enumerate(students):
            pdf.add_text(start_x + 70 + i * col_w, y, s, 'F2', 7)
        y -= 14
        pdf.add_line(start_x, y + 2, 540, y + 2, 0.5, 0.3)
        
        for subj in subjects:
            pdf.add_text(start_x, y, subj, 'F2', 8)
            for i in range(4):
                x = start_x + 70 + i * col_w
                pdf.add_line(x, y - 2, x + 105, y - 2, 0.5, 0.5)
            y -= 15
            # Completion checkboxes
            pdf.add_text(start_x, y, "  Done?", 'F1', 7)
            for i in range(4):
                x = start_x + 70 + i * col_w
                pdf.add_rect(x, y - 2, 7, 7, 0.5, 0.3)
            y -= 18
        
        y -= 10
        pdf.add_text(72, y, "FIELD TRIPS / ACTIVITIES THIS WEEK:", 'F2', 9)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 22
        pdf.add_text(72, y, "NOTES / OBSERVATIONS:", 'F2', 9)
        y -= 16
        for _ in range(3):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 12
        pdf.add_text(72, y, "Next week priorities:", 'F2', 9)
        pdf.add_line(190, y - 2, 540, y - 2, 0.5, 0.5)


    # Monthly Overview Pages (4 months)
    for month in range(1, 5):
        pdf.new_page()
        pdf.add_centered_text(750, f"MONTHLY OVERVIEW - Month {month}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        pdf.add_text(72, 715, "Month: _______________   Year: _______", 'F1', 10)
        y = 690
        pdf.add_text(72, y, "GOALS FOR THIS MONTH:", 'F2', 11)
        y -= 18
        for s in students:
            pdf.add_text(72, y, f"{s}:", 'F1', 9)
            pdf.add_line(135, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 20
        y -= 10
        pdf.add_text(72, y, "FIELD TRIPS / SPECIAL ACTIVITIES:", 'F2', 11)
        y -= 18
        for i in range(4):
            pdf.add_text(72, y, "Date:", 'F1', 9)
            pdf.add_line(105, y - 2, 180, y - 2, 0.5, 0.5)
            pdf.add_text(190, y, "Activity:", 'F1', 9)
            pdf.add_line(230, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 22
        y -= 10
        pdf.add_text(72, y, "CURRICULUM ADJUSTMENTS NEEDED:", 'F2', 11)
        y -= 18
        for _ in range(4):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        pdf.add_text(72, y, "MONTH-END REFLECTION:", 'F2', 11)
        y -= 18
        pdf.add_text(72, y, "What worked well:", 'F1', 9)
        pdf.add_line(170, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
        pdf.add_text(72, y, "What to change:", 'F1', 9)
        pdf.add_line(160, y - 2, 540, y - 2, 0.5, 0.5)

    # Attendance Log (full year grid)
    pdf.new_page()
    pdf.add_centered_text(750, "ATTENDANCE LOG", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    pdf.add_text(72, 720, "Mark each school day: P=Present, A=Absent, F=Field Trip, H=Holiday", 'F1', 9)
    y = 700
    months = ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    pdf.add_text(72, y, "Student:", 'F2', 8)
    pdf.add_line(120, y - 2, 250, y - 2, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Month", 'F2', 7)
    for d in range(1, 24):
        pdf.add_text(110 + (d-1) * 18, y, str(d), 'F3', 6)
    y -= 12
    for m in months:
        pdf.add_text(72, y, m, 'F1', 7)
        for d in range(1, 24):
            pdf.add_rect(110 + (d-1) * 18, y - 3, 12, 10, 0.3, 0.5)
        y -= 15
    y -= 15
    pdf.add_text(72, y, "Total Days: _____  Present: _____  Absent: _____  Required: _____", 'F1', 9)

    # Grade Tracker Pages (4 students)
    for student in students:
        pdf.new_page()
        pdf.add_centered_text(750, f"GRADE TRACKER: {student.upper()}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 715
        for subj in subjects:
            pdf.add_text(72, y, f"{subj}:", 'F2', 10)
            y -= 16
            pdf.add_text(72, y, "Assignment", 'F2', 7)
            pdf.add_text(220, y, "Date", 'F2', 7)
            pdf.add_text(290, y, "Grade", 'F2', 7)
            pdf.add_text(350, y, "Notes", 'F2', 7)
            y -= 12
            for _ in range(4):
                pdf.add_line(72, y, 210, y, 0.5, 0.5)
                pdf.add_line(220, y, 280, y, 0.5, 0.5)
                pdf.add_line(290, y, 340, y, 0.5, 0.5)
                pdf.add_line(350, y, 540, y, 0.5, 0.5)
                y -= 15
            pdf.add_text(72, y, "Quarter Average:", 'F1', 8)
            pdf.add_line(165, y - 2, 230, y - 2, 0.5, 0.5)
            y -= 22

    # Book List / Reading Log
    pdf.new_page()
    pdf.add_centered_text(750, "READING LOG / BOOK LIST", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 718
    pdf.add_text(72, y, "#", 'F2', 8)
    pdf.add_text(90, y, "Title", 'F2', 8)
    pdf.add_text(260, y, "Author", 'F2', 8)
    pdf.add_text(380, y, "Student", 'F2', 8)
    pdf.add_text(450, y, "Done", 'F2', 8)
    pdf.add_text(490, y, "Rating", 'F2', 8)
    y -= 14
    for i in range(1, 31):
        pdf.add_text(72, y, str(i), 'F1', 7)
        pdf.add_line(90, y - 2, 250, y - 2, 0.5, 0.5)
        pdf.add_line(260, y - 2, 370, y - 2, 0.5, 0.5)
        pdf.add_line(380, y - 2, 440, y - 2, 0.5, 0.5)
        pdf.add_rect(455, y - 3, 7, 7, 0.5, 0.3)
        pdf.add_line(490, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 19

    # Curriculum Tracker
    pdf.new_page()
    pdf.add_centered_text(750, "CURRICULUM TRACKER", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    for subj in subjects:
        pdf.add_text(72, y, f"{subj}:", 'F2', 11)
        y -= 18
        pdf.add_text(72, y, "Curriculum/Textbook:", 'F1', 9)
        pdf.add_line(185, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 16
        pdf.add_text(72, y, "Publisher:", 'F1', 9)
        pdf.add_line(130, y - 2, 300, y - 2, 0.5, 0.5)
        pdf.add_text(310, y, "Cost:", 'F1', 9)
        pdf.add_line(345, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 16
        pdf.add_text(72, y, "Total Lessons/Chapters:", 'F1', 9)
        pdf.add_line(205, y - 2, 300, y - 2, 0.5, 0.5)
        pdf.add_text(310, y, "Completed:", 'F1', 9)
        pdf.add_line(375, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22

    # Year-End Assessment
    pdf.new_page()
    pdf.add_centered_text(750, "YEAR-END ASSESSMENT", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    for student in students:
        pdf.add_text(72, y, f"{student}:", 'F2', 11)
        y -= 16
        pdf.add_text(72, y, "Achievements:", 'F1', 9)
        pdf.add_line(150, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 16
        pdf.add_text(72, y, "Areas to improve:", 'F1', 9)
        pdf.add_line(170, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 16
        pdf.add_text(72, y, "Next year plan:", 'F1', 9)
        pdf.add_line(155, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 25
    y -= 10
    pdf.add_text(72, y, "FAMILY HOMESCHOOL REFLECTIONS:", 'F2', 11)
    y -= 18
    pdf.add_text(72, y, "What worked best this year:", 'F1', 10)
    y -= 16
    for _ in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16
    y -= 8
    pdf.add_text(72, y, "What we will change:", 'F1', 10)
    y -= 16
    for _ in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16
    y -= 8
    pdf.add_text(72, y, "Our favorite memory:", 'F1', 10)
    y -= 16
    for _ in range(2):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book86_Homeschool_Multi_Planner.pdf')
    print("Book86_Homeschool_Multi_Planner.pdf created successfully!")

if __name__ == "__main__":
    create_book()
