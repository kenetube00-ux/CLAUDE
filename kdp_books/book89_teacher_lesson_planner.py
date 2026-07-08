"""Book 89: Teacher Lesson Planner"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.1)
    pdf.add_centered_text(530, "THE UNDATED", 'F2', 22, 1)
    pdf.add_centered_text(490, "TEACHER PLANNER", 'F2', 28, 1)
    pdf.add_centered_text(440, "Lesson Plans, Grade Book & Classroom Organizer", 'F4', 14, 0.9)
    pdf.add_centered_text(400, "For Any School Year | Any Grade Level", 'F1', 12, 0.8)
    pdf.add_centered_text(370, "40 Weekly Lesson Plans + Grade Tracker + More", 'F1', 11, 0.7)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "The Undated Teacher Planner", 'F2', 13)
    pdf.add_centered_text(478, "Lesson Plans, Grade Book & Classroom Organizer", 'F4', 11)
    pdf.add_centered_text(448, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(428, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(398, "This planner is undated so you can start any time of year.", 'F1', 9)
    pdf.add_centered_text(378, "Designed by a teacher, for teachers.", 'F4', 10)


    # Classroom Info Page
    pdf.new_page()
    pdf.add_centered_text(750, "CLASSROOM INFORMATION", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 710
    info_fields = [
        "School Name:", "School Address:", "School Phone:", "Room Number:",
        "Grade Level:", "Subject(s):", "Principal:", "Vice Principal:",
        "Department Head:", "Mentor Teacher:", "School Counselor:",
        "Nurse:", "IT Support:"
    ]
    for field in info_fields:
        pdf.add_text(72, y, field, 'F2', 10)
        pdf.add_line(200, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 24
    y -= 15
    pdf.add_text(72, y, "MY DAILY SCHEDULE:", 'F2', 11)
    y -= 18
    pdf.add_text(72, y, "Period/Time", 'F2', 9)
    pdf.add_text(200, y, "Subject/Class", 'F2', 9)
    pdf.add_text(380, y, "Room", 'F2', 9)
    y -= 15
    for i in range(8):
        pdf.add_line(72, y, 190, y, 0.5, 0.5)
        pdf.add_line(200, y, 370, y, 0.5, 0.5)
        pdf.add_line(380, y, 450, y, 0.5, 0.5)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "Prep Period:", 'F1', 9)
    pdf.add_line(145, y - 2, 300, y - 2, 0.5, 0.5)
    pdf.add_text(310, y, "Lunch:", 'F1', 9)
    pdf.add_line(350, y - 2, 500, y - 2, 0.5, 0.5)

    # Student Roster (2 pages, 30 students)
    for pg in range(1, 3):
        pdf.new_page()
        pdf.add_centered_text(750, f"STUDENT ROSTER - Page {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 718
        pdf.add_text(72, y, "#", 'F2', 7)
        pdf.add_text(88, y, "Student Name", 'F2', 7)
        pdf.add_text(210, y, "Parent/Guardian", 'F2', 7)
        pdf.add_text(340, y, "Phone", 'F2', 7)
        pdf.add_text(430, y, "Email/Notes", 'F2', 7)
        y -= 14
        start = (pg - 1) * 15 + 1
        for i in range(15):
            num = start + i
            pdf.add_text(72, y, str(num), 'F1', 7)
            pdf.add_line(88, y - 2, 200, y - 2, 0.5, 0.5)
            pdf.add_line(210, y - 2, 330, y - 2, 0.5, 0.5)
            pdf.add_line(340, y - 2, 420, y - 2, 0.5, 0.5)
            pdf.add_line(430, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 22
            # Second line for notes
            pdf.add_text(88, y, "Notes:", 'F1', 6)
            pdf.add_line(115, y - 2, 540, y - 2, 0.3, 0.6)
            y -= 20

    # 40 Weekly Lesson Plan Pages
    for week in range(1, 41):
        pdf.new_page()
        pdf.add_filled_rect(50, 752, 512, 26, 0.85)
        pdf.add_text(60, 760, f"WEEK {week} LESSON PLAN", 'F2', 12)
        pdf.add_text(300, 760, "Dates: ___/___  to  ___/___", 'F1', 9)
        
        # 5-day grid
        days_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        y = 735
        row_h = 130
        for day_idx, day_name in enumerate(days_names):
            pdf.add_filled_rect(52, y - row_h + 5, 508, 14, 0.92)
            pdf.add_text(56, y - row_h + 8, day_name, 'F2', 8)
            pdf.add_text(56, y - row_h + 8 + 14, "Standard:", 'F1', 7)
            pdf.add_line(100, y - row_h + 8 + 12, 300, y - row_h + 8 + 12, 0.3, 0.6)
            pdf.add_text(310, y - row_h + 8 + 14, "Objective:", 'F1', 7)
            pdf.add_line(355, y - row_h + 8 + 12, 555, y - row_h + 8 + 12, 0.3, 0.6)
            pdf.add_text(56, y - row_h + 8 + 28, "Materials:", 'F1', 7)
            pdf.add_line(100, y - row_h + 8 + 26, 555, y - row_h + 8 + 26, 0.3, 0.6)
            pdf.add_text(56, y - row_h + 8 + 42, "Procedure:", 'F1', 7)
            pdf.add_line(100, y - row_h + 8 + 40, 555, y - row_h + 8 + 40, 0.3, 0.6)
            pdf.add_line(56, y - row_h + 8 + 54, 555, y - row_h + 8 + 54, 0.3, 0.6)
            pdf.add_text(56, y - row_h + 8 + 68, "Assessment:", 'F1', 7)
            pdf.add_line(108, y - row_h + 8 + 66, 555, y - row_h + 8 + 66, 0.3, 0.6)
            y -= row_h


    # Grade Tracker Pages (4 pages, 30 students)
    for pg in range(1, 5):
        pdf.new_page()
        pdf.add_centered_text(750, f"GRADE TRACKER - Page {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        pdf.add_text(72, 722, "Subject:", 'F1', 9)
        pdf.add_line(115, 720, 250, 720, 0.5, 0.5)
        pdf.add_text(260, 722, "Quarter:", 'F1', 9)
        pdf.add_line(300, 720, 380, 720, 0.5, 0.5)
        
        y = 700
        # Assignment headers
        pdf.add_text(72, y, "#", 'F2', 6)
        pdf.add_text(84, y, "Student Name", 'F2', 6)
        # 10 assignment columns
        for a in range(10):
            pdf.add_text(190 + a * 35, y, f"A{a+1}", 'F2', 6)
        pdf.add_text(540, y, "Avg", 'F2', 6)
        y -= 12
        
        start_student = 1
        for s in range(30):
            num = start_student + s
            pdf.add_text(72, y, str(num), 'F1', 6)
            pdf.add_line(84, y - 2, 185, y - 2, 0.3, 0.5)
            for a in range(10):
                pdf.add_line(190 + a * 35, y - 2, 218 + a * 35, y - 2, 0.3, 0.5)
            pdf.add_line(540, y - 2, 560, y - 2, 0.3, 0.5)
            y -= 18
            if y < 80:
                break

    # Parent Communication Log (2 pages)
    for pg in range(1, 3):
        pdf.new_page()
        pdf.add_centered_text(750, f"PARENT COMMUNICATION LOG - Page {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 718
        pdf.add_text(72, y, "Date", 'F2', 8)
        pdf.add_text(130, y, "Student", 'F2', 8)
        pdf.add_text(230, y, "Parent/Guardian", 'F2', 8)
        pdf.add_text(360, y, "Method", 'F2', 8)
        pdf.add_text(420, y, "Topic/Notes", 'F2', 8)
        y -= 15
        for _ in range(20):
            pdf.add_line(72, y, 125, y, 0.5, 0.5)
            pdf.add_line(130, y, 225, y, 0.5, 0.5)
            pdf.add_line(230, y, 355, y, 0.5, 0.5)
            pdf.add_line(360, y, 415, y, 0.5, 0.5)
            pdf.add_line(420, y, 540, y, 0.5, 0.5)
            y -= 18
            pdf.add_line(420, y, 540, y, 0.3, 0.6)
            y -= 15

    # Meeting Notes (3 pages)
    for pg in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(750, f"MEETING NOTES - Page {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 715
        pdf.add_text(72, y, "Date:", 'F1', 10)
        pdf.add_line(105, y - 2, 220, y - 2, 0.5, 0.5)
        pdf.add_text(230, y, "Type:", 'F1', 10)
        pdf.add_line(265, y - 2, 420, y - 2, 0.5, 0.5)
        y -= 22
        pdf.add_text(72, y, "Attendees:", 'F1', 10)
        pdf.add_line(135, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22
        pdf.add_text(72, y, "Agenda/Topics:", 'F2', 10)
        y -= 18
        for _ in range(5):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        pdf.add_text(72, y, "Key Decisions:", 'F2', 10)
        y -= 18
        for _ in range(4):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        pdf.add_text(72, y, "Action Items:", 'F2', 10)
        y -= 18
        for _ in range(5):
            pdf.add_rect(72, y - 2, 7, 7, 0.5, 0.3)
            pdf.add_line(85, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        pdf.add_text(72, y, "Follow-up needed by (date):", 'F1', 10)
        pdf.add_line(240, y - 2, 400, y - 2, 0.5, 0.5)

    # Professional Development Log
    pdf.new_page()
    pdf.add_centered_text(750, "PROFESSIONAL DEVELOPMENT LOG", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    for i in range(6):
        pdf.add_text(72, y, f"PD #{i+1}", 'F2', 9)
        y -= 16
        pd_fields = ["Title/Topic:", "Date:", "Provider:", "Hours:", "Key Takeaways:", "How I will apply this:"]
        for pf in pd_fields:
            pdf.add_text(72, y, pf, 'F1', 8)
            pdf.add_line(175, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 14
        y -= 12

    # Substitute Teacher Info Page
    pdf.new_page()
    pdf.add_centered_text(750, "SUBSTITUTE TEACHER INFORMATION", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    sub_fields = [
        ("Class Schedule:", 3),
        ("Classroom Rules:", 3),
        ("Seating Chart Location:", 1),
        ("Emergency Procedures:", 3),
        ("Students with Medical Needs:", 3),
        ("Students with Behavioral Plans:", 3),
        ("Helpful Students (class helpers):", 2),
        ("Where to find supplies:", 2),
        ("Neighbor Teacher for Help:", 1),
        ("End-of-Day Procedures:", 3),
    ]
    for label, lines in sub_fields:
        pdf.add_text(72, y, label, 'F2', 9)
        y -= 14
        for _ in range(lines):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 13
        y -= 6

    # End-of-Year Reflection
    pdf.new_page()
    pdf.add_centered_text(750, "END-OF-YEAR REFLECTION", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 710
    reflection_prompts = [
        ("What were my biggest successes this year?", 4),
        ("What would I do differently?", 3),
        ("Which lessons/units worked best?", 3),
        ("Which students showed the most growth?", 3),
        ("What professional goals did I meet?", 3),
        ("Goals for next year:", 4),
        ("Resources I want to find/create:", 3),
        ("Note to my future self:", 3),
    ]
    for prompt, lines in reflection_prompts:
        pdf.add_text(72, y, prompt, 'F2', 10)
        y -= 16
        for _ in range(lines):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 15
        y -= 8

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book89_Teacher_Lesson_Planner.pdf')
    print("Book89_Teacher_Lesson_Planner.pdf created successfully!")

if __name__ == "__main__":
    create_book()
