"""Book 148: The Substitute Teacher Survival Binder"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(520, "THE SUBSTITUTE TEACHER", 'F2', 24, 0)
    doc.add_centered_text(485, "SURVIVAL BINDER", 'F2', 24, 0)
    doc.add_centered_text(430, "Everything a Sub Needs in One Place", 'F4', 16, 0.2)
    doc.add_centered_text(350, "Templates | Schedules | Procedures", 'F1', 13, 0.3)
    doc.add_centered_text(325, "Lesson Plans | Communication Forms", 'F1', 13, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(600, "THE SUBSTITUTE TEACHER SURVIVAL BINDER", 'F2', 12, 0)
    doc.add_text(72, 500, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.3)

    # Page 3: Welcome Letter Template
    doc.new_page()
    doc.add_centered_text(740, "WELCOME LETTER TEMPLATE", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Dear Substitute,", 'F4', 12, 0.2)
    y = 672
    doc.add_text(72, y, "Welcome to my classroom! Thank you for being here. Below is everything", 'F1', 11, 0.2)
    y -= 18
    doc.add_text(72, y, "you need to have a successful day.", 'F1', 11, 0.2)
    y -= 30
    fields = [
        "Teacher Name: _____________________________________________________",
        "Grade/Subject: ____________________________________________________",
        "Room Number: ______________________________________________________",
        "School Phone: _____________________________________________________",
        "Principal: ________________________________________________________",
        "Nearest Teacher for Help: _________________________________________",
        "Prep Period: ______________________________________________________",
        "Duty Assignment: __________________________________________________",
        "Lunch Time: _______________________________________________________",
        "End of Day Dismissal: _____________________________________________"
    ]
    for f in fields:
        doc.add_text(72, y, f, 'F1', 11, 0.2)
        y -= 25
    y -= 15
    doc.add_text(72, y, "Special Notes: ____________________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)

    # Page 4: Daily Schedule Template
    doc.new_page()
    doc.add_centered_text(740, "DAILY SCHEDULE", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 705
    doc.add_filled_rect(72, y-2, 468, 20, 0.85)
    doc.add_text(75, y+2, "Time", 'F2', 10, 0)
    doc.add_text(170, y+2, "Subject/Activity", 'F2', 10, 0)
    doc.add_text(370, y+2, "Notes/Location", 'F2', 10, 0)
    y -= 25
    for i in range(16):
        doc.add_rect(72, y, 468, 30)
        doc.add_line(165, y, 165, y+30, 0.5, 0.7)
        doc.add_line(365, y, 365, y+30, 0.5, 0.7)
        y -= 32

    # Page 5: Classroom Rules
    doc.new_page()
    doc.add_centered_text(740, "CLASSROOM RULES & EXPECTATIONS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    doc.add_text(72, y, "Classroom Rules:", 'F2', 12, 0)
    y -= 22
    for i in range(6):
        doc.add_text(72, y, f"{i+1}. _____________________________________________________________", 'F1', 11, 0.2)
        y -= 25
    y -= 15
    doc.add_text(72, y, "Positive Reinforcement System: _______________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
    y -= 30
    doc.add_text(72, y, "Consequences for Rule Breaking:", 'F2', 12, 0)
    y -= 22
    doc.add_text(72, y, "1st offense: _______________________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "2nd offense: _______________________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "3rd offense: _______________________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "Send to office: ____________________________________________________", 'F1', 11, 0.2)

    # Page 6: Seating Chart Template
    doc.new_page()
    doc.add_centered_text(740, "SEATING CHART", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 710, "Class Period: ___  Date: ___________", 'F1', 10, 0.3)
    doc.add_text(250, 680, "[FRONT OF ROOM / BOARD]", 'F2', 10, 0.5)
    doc.add_line(180, 672, 432, 672, 1, 0.3)
    # Grid for seating
    y = 640
    for row in range(6):
        x = 82
        for col in range(5):
            doc.add_rect(x, y, 90, 35)
            x += 95
        y -= 45

    # Page 7: Emergency Procedures
    doc.new_page()
    doc.add_centered_text(740, "EMERGENCY PROCEDURES", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    emergencies = [
        ("FIRE:", "Exit route: ___________________________________________________"),
        ("", "Assembly point: _______________________________________________"),
        ("LOCKDOWN:", "Procedure: ___________________________________________________"),
        ("", "Lock door? [ ] Yes  Hide location: ____________________________"),
        ("EARTHQUAKE:", "Procedure: ___________________________________________________"),
        ("TORNADO:", "Shelter location: _____________________________________________"),
        ("MEDICAL:", "Nurse location: _______  Phone ext: ______"),
        ("", "AED location: ________________________________________________"),
        ("INTRUDER:", "Code word: ____  Action: _____________________________________")
    ]
    for label, detail in emergencies:
        if label:
            doc.add_text(72, y, label, 'F2', 11, 0)
        doc.add_text(160, y, detail, 'F1', 10, 0.2)
        y -= 22
    y -= 15
    doc.add_text(72, y, "Emergency contacts:", 'F2', 11, 0)
    y -= 20
    doc.add_text(72, y, "Office: _________  Principal: _________  Nurse: _________", 'F1', 10, 0.2)

    # Page 8: Medical/Allergy Alerts
    doc.new_page()
    doc.add_centered_text(740, "STUDENT MEDICAL / ALLERGY ALERTS", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 710, "CRITICAL - Please review before class begins!", 'F2', 11, 0)
    y = 680
    doc.add_filled_rect(72, y-2, 468, 18, 0.85)
    doc.add_text(75, y, "Student Name", 'F2', 9, 0)
    doc.add_text(200, y, "Condition/Allergy", 'F2', 9, 0)
    doc.add_text(360, y, "Action Required", 'F2', 9, 0)
    y -= 22
    for i in range(15):
        doc.add_rect(72, y, 468, 28)
        doc.add_line(195, y, 195, y+28, 0.5, 0.7)
        doc.add_line(355, y, 355, y+28, 0.5, 0.7)
        y -= 30
    doc.add_text(72, y-5, "EpiPen location: ____________  Inhaler students: ____________", 'F1', 10, 0.2)

    # Page 9: Behavior Management
    doc.new_page()
    doc.add_centered_text(740, "BEHAVIOR MANAGEMENT PLAN SUMMARY", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    doc.add_text(72, y, "Reward System: _____________________________________________________", 'F1', 11, 0.2)
    y -= 25
    doc.add_text(72, y, "Class Currency/Points: ______________________________________________", 'F1', 11, 0.2)
    y -= 25
    doc.add_text(72, y, "Signal for Quiet (e.g., hand raise, clap pattern): ___________________", 'F1', 11, 0.2)
    y -= 25
    doc.add_text(72, y, "Transition Signal: __________________________________________________", 'F1', 11, 0.2)
    y -= 30
    doc.add_text(72, y, "Students who may need extra support:", 'F2', 11, 0)
    y -= 22
    for i in range(4):
        doc.add_text(72, y, "Name: ___________________  Strategy: ____________________________", 'F1', 10, 0.2)
        y -= 22
    y -= 15
    doc.add_text(72, y, "If a student is HIGHLY disruptive: ___________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)

    # Page 10: Reliable Student Helpers
    doc.new_page()
    doc.add_centered_text(740, "RELIABLE STUDENT HELPERS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "These students can help with routines, directions, and questions:", 'F1', 11, 0.2)
    y = 675
    doc.add_filled_rect(72, y-2, 468, 18, 0.85)
    doc.add_text(75, y, "Student Name", 'F2', 9, 0)
    doc.add_text(220, y, "Period/Class", 'F2', 9, 0)
    doc.add_text(340, y, "How They Can Help", 'F2', 9, 0)
    y -= 22
    for i in range(12):
        doc.add_rect(72, y, 468, 25)
        doc.add_line(215, y, 215, y+25, 0.5, 0.7)
        doc.add_line(335, y, 335, y+25, 0.5, 0.7)
        y -= 27

    # Page 11: Technology Instructions
    doc.new_page()
    doc.add_centered_text(740, "TECHNOLOGY INSTRUCTIONS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    tech_items = [
        "Computer login - Username: _____________ Password: _____________",
        "WiFi network: _________________ Password: _____________________",
        "Projector: [ ] Remote  [ ] Button  Location: __________________",
        "SmartBoard instructions: ________________________________________",
        "Student devices: [ ] Chromebooks [ ] iPads  Cart location: _____",
        "Student login instructions: _____________________________________",
        "Classroom phone: Dial ___ for office, ___ for nurse",
        "Printer location: ______________________________________________",
        "Document camera: [ ] Yes  How to use: __________________________",
        "Classroom website/LMS: __________________________________________"
    ]
    for t in tech_items:
        doc.add_text(72, y, t, 'F1', 10, 0.2)
        y -= 28

    # Page 12: Where to Find Supplies
    doc.new_page()
    doc.add_centered_text(740, "WHERE TO FIND SUPPLIES", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    supplies = ["Extra pencils/pens:", "Paper:", "Scissors/glue:", "Tissues/hand sanitizer:",
                "Band-aids:", "Hall passes:", "Referral forms:", "Grade book/attendance:",
                "Textbooks:", "Worksheets for today:", "Early finisher activities:",
                "Sub folder/binder:", "Keys (if needed):"]
    for s in supplies:
        doc.add_text(72, y, f"{s} ____________________________________", 'F1', 11, 0.2)
        y -= 28

    # Pages 13-22: Lesson Plan Templates (10 pages)
    for period in range(10):
        doc.new_page()
        doc.add_centered_text(740, f"LESSON PLAN - Period/Block {period+1}", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        doc.add_text(72, y, f"Subject: ________________________  Time: _______ to _______", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Objective (what students should learn/do): ____________________________", 'F1', 10, 0.2)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Materials needed: __________________________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "INSTRUCTIONS:", 'F2', 11, 0)
        y -= 20
        for i in range(6):
            doc.add_text(72, y, f"{i+1}. _____________________________________________________________", 'F1', 10, 0.2)
            y -= 22
        y -= 10
        doc.add_text(72, y, "Early finishers should: ____________________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Homework (if any): _________________________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Collect at end of class: [ ] Yes  [ ] No", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Notes: _____________________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)

    # Pages 23-27: End-of-Day Report Template (5 pages)
    for day in range(5):
        doc.new_page()
        doc.add_centered_text(740, f"END-OF-DAY REPORT - Day {day+1}", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        doc.add_text(72, y, f"Date: ______________  Sub Name: ___________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Overall how did the day go? [ ] Great  [ ] Good  [ ] Challenging", 'F1', 10, 0.2)
        y -= 28
        doc.add_text(72, y, "Lessons completed:", 'F2', 11, 0)
        y -= 20
        for i in range(4):
            doc.add_text(72, y, f"Period {i+1}: [ ] Completed  [ ] Partially  [ ] Not started  Notes: ______", 'F1', 9, 0.2)
            y -= 20
        y -= 10
        doc.add_text(72, y, "Behavior issues:", 'F2', 11, 0)
        y -= 20
        doc.add_text(72, y, "Student: ________________  Issue: __________________________________", 'F1', 10, 0.2)
        y -= 20
        doc.add_text(72, y, "Student: ________________  Issue: __________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Positive highlights: ________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Messages/questions for returning teacher: ___________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)

    # Page 28: Important Contacts
    doc.new_page()
    doc.add_centered_text(740, "IMPORTANT CONTACTS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 705
    contacts = ["Principal:", "Vice Principal:", "Office Secretary:", "School Nurse:",
                "Counselor:", "Special Ed. Teacher:", "Librarian:", "IT Support:",
                "Custodian:", "Teacher Next Door:", "Department Head:", "Parent Contact (urgent):"]
    for c in contacts:
        doc.add_text(72, y, f"{c} _____________________  Phone/Ext: ______________", 'F1', 10, 0.2)
        y -= 28

    # Page 29: Feedback Form
    doc.new_page()
    doc.add_centered_text(740, "FEEDBACK FORM FOR RETURNING TEACHER", 'F2', 13, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    doc.add_text(72, y, "Dear Returning Teacher,", 'F4', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "Here is a summary of what happened while you were away:", 'F1', 11, 0.2)
    y -= 30
    doc.add_text(72, y, "What went well: ____________________________________________________", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
    y -= 28
    doc.add_text(72, y, "What was challenging: _______________________________________________", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
    y -= 28
    doc.add_text(72, y, "Students who were especially helpful: ________________________________", 'F1', 10, 0.2)
    y -= 28
    doc.add_text(72, y, "Students who may need follow-up: ____________________________________", 'F1', 10, 0.2)
    y -= 28
    doc.add_text(72, y, "Assignments collected: [ ] Yes  [ ] No  Location: ___________________", 'F1', 10, 0.2)
    y -= 28
    doc.add_text(72, y, "Suggestions for future sub plans: ___________________________________", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)

    # Page 30: Tips for Successful Sub Days
    doc.new_page()
    doc.add_centered_text(740, "TIPS FOR SUCCESSFUL SUBSTITUTE DAYS", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    tips = [
        "Arrive 15-20 minutes early to review plans",
        "Introduce yourself and write your name on the board",
        "Review emergency procedures FIRST",
        "Check for medical alerts before students arrive",
        "Follow the teacher's routines as closely as possible",
        "Be firm but fair - students test subs",
        "Use the reliable student helpers",
        "Don't take behavior personally",
        "Leave detailed notes for the teacher",
        "Keep your phone number for the teacher to follow up",
        "If plans run short: read-aloud, silent reading, or journal writing",
        "If technology fails: have a backup paper activity ready",
        "Stay positive - your attitude sets the tone!"
    ]
    for t in tips:
        doc.add_text(90, y, f"- {t}", 'F1', 11, 0.2)
        y -= 22

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book148_Substitute_Teacher_Binder.pdf')
    print("Book148_Substitute_Teacher_Binder.pdf created successfully!")

if __name__ == "__main__":
    create_book()
