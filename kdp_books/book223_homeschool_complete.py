"""Book 223: The Complete Homeschool Planner K-8"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.15)
    doc.add_centered_text(755, "THE COMPLETE", 'F2', 24, 1)
    doc.add_centered_text(722, "HOMESCHOOL PLANNER", 'F2', 24, 1)
    doc.add_centered_text(660, "K-8 All Subjects, All Year", 'F4', 14, 0.3)
    doc.add_centered_text(620, "Lesson Plans | Attendance | Grades | Activities", 'F1', 11, 0.4)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    # Copyright
    doc.new_page()
    doc.add_centered_text(700, "THE COMPLETE HOMESCHOOL PLANNER", 'F2', 14)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # Student Profiles (4 students)
    doc.new_page()
    doc.add_centered_text(755, "STUDENT PROFILES", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    for s in range(1, 5):
        doc.add_text(72, y, f"STUDENT {s}", 'F2', 10)
        y -= 16
        doc.add_text(90, y, "Name: _______________ Grade: ___ Age: ___", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Learning Style: [ ] Visual [ ] Auditory [ ] Kinesthetic [ ] Read/Write", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Goals: ________________________________", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Accommodations: ________________________________", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Curriculum: ________________________________", 'F1', 9)
        y -= 25

    # Year-at-a-Glance
    doc.new_page()
    doc.add_centered_text(755, "YEAR AT A GLANCE", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    for m in ["Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr","May","Jun","Jul"]:
        doc.add_text(72, y, f"{m}: ________________________________", 'F1', 9)
        y -= 14
        doc.add_text(100, y, "Focus/Theme: __________________ Days off: __________", 'F1', 8)
        y -= 18


    # 36 Weekly Lesson Plan Pages
    for week in range(1, 37):
        doc.new_page()
        doc.add_text(72, 765, f"WEEK {week}", 'F2', 11)
        doc.add_text(200, 765, "Dates: ___/___ to ___/___", 'F1', 9)
        doc.add_text(400, 765, f"Theme: __________", 'F1', 9)
        doc.add_line(72, 758, 540, 758, 0.5, 0.3)
        
        subjects = ["Math", "Language Arts", "Science", "History", "Bible", "Elective"]
        days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        
        y = 745
        # Header row
        doc.add_text(72, y, "Subject", 'F2', 7)
        x_positions = [135, 215, 295, 375, 455]
        for d, x in zip(days, x_positions):
            doc.add_text(x, y, d, 'F2', 7)
        y -= 5
        doc.add_line(72, y, 540, y, 0.5, 0.3)
        
        for subj in subjects:
            y -= 14
            doc.add_text(72, y, subj, 'F2', 7)
            for x in x_positions:
                doc.add_line(x, y+8, x, y-30, 0.3, 0.7)
                doc.add_line(x, y-2, x+75, y-2, 0.5, 0.6)
            y -= 35
            doc.add_line(72, y+3, 540, y+3, 0.3, 0.5)
        
        y -= 10
        doc.add_text(72, y, "Notes: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(72, y, "Field trip/special: ________________________________", 'F1', 8)

    # Monthly Goals (4 pages)
    for month_set in range(1, 5):
        doc.new_page()
        doc.add_centered_text(755, f"MONTHLY GOALS - MONTHS {(month_set-1)*3+1}-{month_set*3}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        for m in range(3):
            doc.add_text(72, y, f"Month {(month_set-1)*3+m+1}: __________", 'F2', 10)
            y -= 16
            doc.add_text(90, y, "Academic goals: ________________________________", 'F1', 9)
            y -= 14
            doc.add_text(90, y, "Character goals: ________________________________", 'F1', 9)
            y -= 14
            doc.add_text(90, y, "Life skills: ________________________________", 'F1', 9)
            y -= 14
            doc.add_text(90, y, "Achieved? [ ] Yes [ ] Partially [ ] Carry forward", 'F1', 9)
            y -= 25


    # Attendance Record
    doc.new_page()
    doc.add_centered_text(755, "ATTENDANCE RECORD", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    doc.add_text(72, y, "Month", 'F2', 8)
    doc.add_text(130, y, "Days Required", 'F2', 8)
    doc.add_text(230, y, "Days Completed", 'F2', 8)
    doc.add_text(340, y, "Hours", 'F2', 8)
    doc.add_text(400, y, "Notes", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    months = ["Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr","May","Jun"]
    for m in months:
        y -= 20
        doc.add_text(72, y, m, 'F1', 9)
        doc.add_line(130, y-2, 225, y-2, 0.5, 0.5)
        doc.add_line(230, y-2, 335, y-2, 0.5, 0.5)
        doc.add_line(340, y-2, 395, y-2, 0.5, 0.5)
        doc.add_line(400, y-2, 540, y-2, 0.5, 0.5)
    y -= 25
    doc.add_text(72, y, "Total days: ___  Total hours: ___  State requirement met? [ ] Yes", 'F2', 9)

    # Grade Tracker
    doc.new_page()
    doc.add_centered_text(755, "GRADE TRACKER", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    for s in range(1, 5):
        doc.add_text(72, y, f"Student {s}: ______________", 'F2', 9)
        y -= 14
        subjects = ["Math", "LA", "Science", "History", "Bible", "Elective"]
        for subj in subjects:
            doc.add_text(90, y, f"{subj}: Q1___ Q2___ Q3___ Q4___ Final___", 'F1', 8)
            y -= 12
        y -= 15

    # Reading Log
    doc.new_page()
    doc.add_centered_text(755, "READING LOG", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    doc.add_text(72, y, "Title", 'F2', 8)
    doc.add_text(230, y, "Author", 'F2', 8)
    doc.add_text(350, y, "Pages", 'F2', 8)
    doc.add_text(400, y, "Date Finished", 'F2', 8)
    doc.add_text(490, y, "Rating", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for _ in range(28):
        y -= 18
        doc.add_line(72, y, 540, y, 0.5, 0.5)

    # Field Trip Planner
    doc.new_page()
    doc.add_centered_text(755, "FIELD TRIP PLANNER", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    for t in range(1, 6):
        doc.add_text(72, y, f"FIELD TRIP {t}", 'F2', 10)
        y -= 16
        doc.add_text(90, y, "Destination: ________________________________", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Date: ___/___/___  Subject tie-in: _______________", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Cost: $___  Reservations needed? [ ] Yes  Packed lunch? [ ] Yes", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "What we learned: ________________________________", 'F1', 9)
        y -= 25

    # Curriculum Tracker + Standardized Test + Portfolio + Co-op + Extra-curricular
    doc.new_page()
    doc.add_centered_text(755, "CURRICULUM & RESOURCES", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    subjects = ["Math", "Language Arts", "Science", "History", "Bible", "Elective"]
    for subj in subjects:
        doc.add_text(72, y, f"{subj}:", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Curriculum: _________________ Supplement: _________________", 'F1', 8)
        y -= 14
        doc.add_text(90, y, "Online resource: _________________ Cost: $_____", 'F1', 8)
        y -= 20
    y -= 10
    doc.add_text(72, y, "STANDARDIZED TESTING:", 'F2', 9)
    y -= 14
    doc.add_text(90, y, "Test used: ____________ Date: ___/___ Results: _______________", 'F1', 9)

    doc.new_page()
    doc.add_centered_text(755, "PORTFOLIO & EXTRA-CURRICULARS", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "END-OF-YEAR PORTFOLIO CHECKLIST:", 'F2', 10)
    y -= 16
    portfolio = ["[ ] Writing samples (3+ per student)", "[ ] Math assessments",
        "[ ] Science projects/labs", "[ ] Art samples", "[ ] Reading list",
        "[ ] Attendance record", "[ ] Grade summary", "[ ] Standardized test results",
        "[ ] Field trip documentation", "[ ] Photos of learning activities"]
    for item in portfolio:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 14
    y -= 15
    doc.add_text(72, y, "CO-OP SCHEDULE:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "Group: _____________ Day: _______ Time: _______", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Subjects covered: ________________________________", 'F1', 9)
    y -= 20
    doc.add_text(72, y, "EXTRA-CURRICULAR TRACKER:", 'F2', 10)
    y -= 16
    for _ in range(4):
        doc.add_text(90, y, "Activity: _____________ Day: ___ Time: ___ Cost: $___", 'F1', 9)
        y -= 16

    doc.save("Book223_Homeschool_Complete_Planner.pdf")
    print("Created: Book223_Homeschool_Complete_Planner.pdf")

if __name__ == "__main__":
    create_book()
