"""Book 224: The All-in-One Teacher Planner"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.2)
    doc.add_centered_text(755, "THE ALL-IN-ONE", 'F2', 24, 1)
    doc.add_centered_text(722, "TEACHER PLANNER", 'F2', 24, 1)
    doc.add_centered_text(660, "Lessons, Grades, Communication & Professional Growth", 'F4', 13, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    doc.new_page()
    doc.add_centered_text(700, "THE ALL-IN-ONE TEACHER PLANNER", 'F2', 14)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # Class Info
    doc.new_page()
    doc.add_centered_text(755, "CLASS INFORMATION", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 710
    fields = ["School: ________________________________", "Room #: ___ Grade/Subject: ________________________________",
        "School year: ________", "Principal: _________________ Phone: ______________",
        "Secretary: _________________ Email: ______________",
        "Counselor: _________________ Phone: ______________", "",
        "CLASS SCHEDULE:", "Period 1: ___ to ___  Subject: ________________",
        "Period 2: ___ to ___  Subject: ________________",
        "Period 3: ___ to ___  Subject: ________________",
        "Period 4: ___ to ___  Subject: ________________",
        "Period 5: ___ to ___  Subject: ________________",
        "Period 6: ___ to ___  Subject: ________________",
        "Lunch: ___ to ___", "Planning: ___ to ___",
        "Duty: _________________ Time: ___ to ___"]
    for f in fields:
        doc.add_text(72, y, f, 'F1', 10)
        y -= 18


    # Student Roster (2 pages)
    for pg in range(1, 3):
        doc.new_page()
        doc.add_centered_text(755, f"STUDENT ROSTER - PAGE {pg}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 725
        doc.add_text(72, y, "#", 'F2', 7)
        doc.add_text(88, y, "Student Name", 'F2', 7)
        doc.add_text(200, y, "Parent/Guardian", 'F2', 7)
        doc.add_text(320, y, "Phone", 'F2', 7)
        doc.add_text(400, y, "Email", 'F2', 7)
        doc.add_text(500, y, "Notes", 'F2', 7)
        doc.add_line(72, y-4, 540, y-4, 0.5, 0.3)
        start = (pg-1)*18 + 1
        for i in range(start, start+18):
            y -= 20
            doc.add_text(72, y, f"{i}", 'F3', 7)
            doc.add_line(88, y-2, 195, y-2, 0.5, 0.5)
            doc.add_line(200, y-2, 315, y-2, 0.5, 0.5)
            doc.add_line(320, y-2, 395, y-2, 0.5, 0.5)
            doc.add_line(400, y-2, 495, y-2, 0.5, 0.5)
            doc.add_line(500, y-2, 540, y-2, 0.5, 0.5)

    # 36 Weekly Lesson Plans
    for week in range(1, 37):
        doc.new_page()
        doc.add_text(72, 765, f"WEEK {week}", 'F2', 10)
        doc.add_text(160, 765, "Dates: ___/___ to ___/___", 'F1', 8)
        doc.add_text(360, 765, "Unit: ________________", 'F1', 8)
        doc.add_line(72, 758, 540, 758, 0.5, 0.3)
        
        days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
        y = 745
        for day in days:
            doc.add_text(72, y, day, 'F2', 8)
            y -= 13
            doc.add_text(80, y, "Standard: _________ Objective: _________________________________", 'F1', 7)
            y -= 11
            doc.add_text(80, y, "Materials: _________________ Procedure: _______________________", 'F1', 7)
            y -= 11
            doc.add_text(80, y, "Differentiation: _____________ Assessment: ____________________", 'F1', 7)
            y -= 15
            doc.add_line(72, y+3, 540, y+3, 0.3, 0.6)

    # Grade Book (4 pages)
    for period in range(1, 5):
        doc.new_page()
        doc.add_centered_text(760, f"GRADE BOOK - MARKING PERIOD {period}", 'F2', 12)
        doc.add_line(72, 750, 540, 750, 0.5, 0.3)
        y = 735
        doc.add_text(72, y, "Student", 'F2', 7)
        for a in range(1, 11):
            doc.add_text(140 + (a-1)*40, y, f"A{a}", 'F2', 7)
        doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
        for s in range(1, 21):
            y -= 18
            doc.add_text(72, y, f"{s}.", 'F3', 7)
            doc.add_line(85, y-2, 135, y-2, 0.5, 0.5)
            for a in range(10):
                doc.add_line(140+a*40, y-2, 175+a*40, y-2, 0.5, 0.5)


    # Parent Communication Log (3 pages)
    for pg in range(1, 4):
        doc.new_page()
        doc.add_centered_text(755, f"PARENT COMMUNICATION LOG - PAGE {pg}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        for _ in range(8):
            doc.add_text(72, y, "Date: ___/___  Student: ______________ Parent: ______________", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Method: [ ] Phone [ ] Email [ ] Conference [ ] Note", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Topic: ________________________________", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Follow-up needed: ________________________________", 'F1', 9)
            y -= 22

    # IEP/504 Tracking
    doc.new_page()
    doc.add_centered_text(755, "IEP/504 ACCOMMODATION TRACKING", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    for s in range(1, 8):
        doc.add_text(72, y, f"Student {s}: ______________  Plan: [ ] IEP [ ] 504", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Accommodations: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Implementation notes: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Annual review date: ___/___/___", 'F1', 8)
        y -= 22

    # Meeting Notes (3 pages)
    for pg in range(1, 4):
        doc.new_page()
        doc.add_centered_text(755, f"MEETING NOTES - PAGE {pg}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        for _ in range(4):
            doc.add_text(72, y, "Date: ___/___  Type: [ ] Staff [ ] PLC [ ] IEP [ ] Parent [ ] Admin", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Attendees: ________________________________", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Key Points: ________________________________", 'F1', 9)
            y -= 14
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 14
            doc.add_text(72, y, "Action Items: ________________________________", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Due: ___/___  Completed: [ ]", 'F1', 9)
            y -= 25

    # Professional Development
    doc.new_page()
    doc.add_centered_text(755, "PROFESSIONAL DEVELOPMENT LOG", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    for _ in range(6):
        doc.add_text(72, y, "Date: ___/___  Title: ________________________________", 'F1', 9)
        y -= 14
        doc.add_text(72, y, "Provider: _____________ Hours: ___  Credit type: __________", 'F1', 9)
        y -= 14
        doc.add_text(72, y, "Key takeaway: ________________________________", 'F1', 9)
        y -= 14
        doc.add_text(72, y, "How I'll apply it: ________________________________", 'F1', 9)
        y -= 25

    # Observation Prep
    doc.new_page()
    doc.add_centered_text(755, "OBSERVATION PREPARATION", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 710
    items = ["Observation date: ___/___  Observer: ______________",
        "Period/Class: ___  Lesson topic: ________________", "",
        "Lesson objective: ________________________________",
        "Standard addressed: ________________________________",
        "Engagement strategies planned: ________________________________",
        "Differentiation: ________________________________",
        "Assessment method: ________________________________",
        "Technology used: ________________________________", "",
        "POST-OBSERVATION NOTES:",
        "Feedback received: ________________________________",
        "________________________________",
        "Strengths noted: ________________________________",
        "Areas for growth: ________________________________",
        "Goal set: ________________________________"]
    for item in items:
        doc.add_text(72, y, item, 'F1', 10)
        y -= 18

    # Self-Evaluation + Sub Info + Reflection
    doc.new_page()
    doc.add_centered_text(755, "SELF-EVALUATION & SUBSTITUTE INFO", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "SELF-EVALUATION:", 'F2', 10)
    y -= 16
    areas = ["Classroom management", "Student engagement", "Differentiation",
             "Assessment practices", "Parent communication", "Professional growth"]
    for area in areas:
        doc.add_text(90, y, f"{area}: 1  2  3  4  5  Goal: __________", 'F1', 9)
        y -= 16
    y -= 15
    doc.add_text(72, y, "SUBSTITUTE TEACHER INFO:", 'F2', 10)
    y -= 16
    sub_items = ["Emergency sub plans location: ________________________________",
        "Seating chart location: ________________________________",
        "Behavior system: ________________________________",
        "Students with medical needs: ________________________________",
        "Key helpers (student names): ________________________________",
        "Nearest teacher for help: ________________________________"]
    for item in sub_items:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 16
    y -= 15
    doc.add_text(72, y, "END-OF-YEAR REFLECTION:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "Greatest success: ________________________________", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Biggest challenge: ________________________________", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "What I'll do differently: ________________________________", 'F1', 9)

    doc.save("Book224_Teacher_Complete_Planner.pdf")
    print("Created: Book224_Teacher_Complete_Planner.pdf")

if __name__ == "__main__":
    create_book()
