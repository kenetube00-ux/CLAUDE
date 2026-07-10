"""Book 151: School Counselor Planner & Data Tracker"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(520, "SCHOOL COUNSELOR", 'F2', 26, 0)
    doc.add_centered_text(485, "PLANNER & DATA TRACKER", 'F2', 26, 0)
    doc.add_centered_text(430, "For K-12 Counselors", 'F4', 16, 0.2)
    doc.add_centered_text(350, "Session Notes | Group Logs | Crisis Documentation", 'F1', 12, 0.3)
    doc.add_centered_text(325, "Lesson Plans | Data Tracking | Self-Care", 'F1', 12, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0)

    doc.new_page()
    doc.add_centered_text(600, "SCHOOL COUNSELOR PLANNER & DATA TRACKER", 'F2', 11, 0)
    doc.add_text(72, 500, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.3)

    # Page 3: Caseload Overview
    doc.new_page()
    doc.add_centered_text(740, "CASELOAD OVERVIEW", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 710, "School Year: ___________  Total Caseload: ___", 'F1', 10, 0.2)
    y = 685
    doc.add_filled_rect(72, y-2, 468, 18, 0.85)
    doc.add_text(75, y, "Student", 'F2', 8, 0)
    doc.add_text(175, y, "Grade", 'F2', 8, 0)
    doc.add_text(220, y, "Concern", 'F2', 8, 0)
    doc.add_text(340, y, "IEP/504?", 'F2', 8, 0)
    doc.add_text(405, y, "Frequency", 'F2', 8, 0)
    doc.add_text(475, y, "Status", 'F2', 8, 0)
    y -= 20
    for i in range(25):
        doc.add_rect(72, y, 468, 18)
        doc.add_line(172, y, 172, y+18, 0.3, 0.7)
        doc.add_line(217, y, 217, y+18, 0.3, 0.7)
        doc.add_line(337, y, 337, y+18, 0.3, 0.7)
        doc.add_line(402, y, 402, y+18, 0.3, 0.7)
        doc.add_line(472, y, 472, y+18, 0.3, 0.7)
        y -= 20

    # Pages 4-13: Individual Session Notes (10 pages)
    for page_num in range(10):
        doc.new_page()
        doc.add_centered_text(740, f"INDIVIDUAL SESSION NOTES - Page {page_num+1}", 'F2', 13, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        for session in range(2):
            doc.add_filled_rect(72, y+2, 468, 14, 0.9)
            doc.add_text(75, y+3, f"Session {page_num*2+session+1}", 'F2', 8, 0)
            y -= 18
            doc.add_text(72, y, "Student: ___________________  Grade: ___  Date: _________  Time: _____", 'F1', 9, 0.2)
            y -= 16
            doc.add_text(72, y, "Presenting Concern: _______________________________________________", 'F1', 9, 0.2)
            y -= 16
            doc.add_text(72, y, "ASCA Domain: [ ] Academic [ ] Career [ ] Social/Emotional", 'F1', 9, 0.2)
            y -= 16
            doc.add_text(72, y, "Intervention Used: ________________________________________________", 'F1', 9, 0.2)
            y -= 16
            doc.add_text(72, y, "Student Response/Progress: ________________________________________", 'F1', 9, 0.2)
            y -= 14
            doc.add_text(72, y, "___________________________________________________________________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(72, y, "Follow-Up Plan: ___________________________________________________", 'F1', 9, 0.2)
            y -= 16
            doc.add_text(72, y, "Parent Contact: [ ] Yes [ ] No  Teacher Consult: [ ] Yes [ ] No", 'F1', 9, 0.2)
            y -= 16
            doc.add_text(72, y, "Next Session: _____________  Referral Needed: [ ] Yes [ ] No", 'F1', 9, 0.2)
            y -= 30

    # Pages 14-18: Group Counseling Log (5 pages)
    for page_num in range(5):
        doc.new_page()
        doc.add_centered_text(740, f"GROUP COUNSELING SESSION LOG ({page_num+1}/5)", 'F2', 13, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        doc.add_text(72, y, "Group Name: _________________________  Session #: ___  Date: _________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Topic: ____________________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Members Present:", 'F2', 10, 0)
        y -= 18
        for i in range(6):
            doc.add_text(72 + (i%3)*160, y, f"[ ] _______________", 'F1', 9, 0.2)
            if i % 3 == 2:
                y -= 16
        y -= 20
        doc.add_text(72, y, "Activity/Lesson: ___________________________________________________", 'F1', 10, 0.2)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Observations:", 'F2', 10, 0)
        y -= 18
        for i in range(4):
            doc.add_text(72, y, "___________________________________________________________________", 'F1', 9, 0.3)
            y -= 16
        y -= 10
        doc.add_text(72, y, "Changes for next session: __________________________________________", 'F1', 10, 0.2)
        y -= 20
        doc.add_text(72, y, "Individual follow-up needed: _______________________________________", 'F1', 10, 0.2)

    # Pages 19-21: Classroom Lesson Planner (3 pages)
    for page_num in range(3):
        doc.new_page()
        doc.add_centered_text(740, f"CLASSROOM LESSON PLANNER ({page_num+1}/3)", 'F2', 13, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        doc.add_text(72, y, "Grade Level: ___  Date: _________  # Students: ___", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "ASCA Standard: ____________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Lesson Title: _____________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Objective (students will be able to): _____________________________", 'F1', 10, 0.2)
        y -= 18
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Materials Needed: __________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Introduction (5 min): ______________________________________________", 'F1', 10, 0.2)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Activity (20 min): ________________________________________________", 'F1', 10, 0.2)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Closing/Assessment (5 min): ________________________________________", 'F1', 10, 0.2)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Assessment method: [ ] Exit ticket [ ] Show of hands [ ] Written [ ] Other", 'F1', 9, 0.2)
        y -= 22
        doc.add_text(72, y, "Results: ____ % met objective  Adjustments for next time: __________", 'F1', 10, 0.2)

    # Pages 22-24: Crisis Intervention Log (3 pages)
    for page_num in range(3):
        doc.new_page()
        doc.add_centered_text(740, f"CRISIS INTERVENTION LOG ({page_num+1}/3)", 'F2', 13, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        doc.add_filled_rect(72, y-5, 468, 20, 0.88)
        doc.add_text(75, y-2, "CONFIDENTIAL - CRISIS DOCUMENTATION", 'F2', 10, 0)
        y -= 30
        doc.add_text(72, y, "Student: ___________________  Grade: ___  Date: _________  Time: _____", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Type: [ ] SI/SH [ ] Abuse report [ ] Violence [ ] Substance [ ] Other", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Source of referral: ________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Risk Assessment:", 'F2', 10, 0)
        y -= 18
        doc.add_text(72, y, "  Ideation: [ ] Passive [ ] Active   Plan: [ ] Yes [ ] No", 'F1', 9, 0.2)
        y -= 16
        doc.add_text(72, y, "  Means: [ ] Yes [ ] No   Prior attempts: [ ] Yes [ ] No", 'F1', 9, 0.2)
        y -= 16
        doc.add_text(72, y, "  Risk level: [ ] Low [ ] Moderate [ ] High [ ] Imminent", 'F1', 9, 0.2)
        y -= 22
        doc.add_text(72, y, "Actions taken: _____________________________________________________", 'F1', 10, 0.2)
        y -= 18
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 22
        doc.add_text(72, y, "Parent/Guardian contacted: [ ] Yes Time: _____ [ ] Unable (document why)", 'F1', 9, 0.2)
        y -= 22
        doc.add_text(72, y, "Admin notified: [ ] Yes  CPS report filed: [ ] Yes #: ______________", 'F1', 9, 0.2)
        y -= 22
        doc.add_text(72, y, "Safety plan created: [ ] Yes  Referral made to: ____________________", 'F1', 9, 0.2)
        y -= 22
        doc.add_text(72, y, "Follow-up date: ___________  Outcome: _____________________________", 'F1', 10, 0.2)

    # Page 25: 504/IEP Meeting Notes
    doc.new_page()
    doc.add_centered_text(740, "504/IEP MEETING NOTES", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 705
    for meeting in range(3):
        doc.add_filled_rect(72, y+2, 468, 14, 0.9)
        doc.add_text(75, y+3, f"Meeting {meeting+1}", 'F2', 8, 0)
        y -= 18
        doc.add_text(72, y, "Student: ______________  Type: [ ] 504 [ ] IEP  Date: _________", 'F1', 9, 0.2)
        y -= 16
        doc.add_text(72, y, "Attendees: _______________________________________________________", 'F1', 9, 0.2)
        y -= 16
        doc.add_text(72, y, "Key decisions: ___________________________________________________", 'F1', 9, 0.2)
        y -= 14
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 9, 0.3)
        y -= 16
        doc.add_text(72, y, "Counselor action items: ___________________________________________", 'F1', 9, 0.2)
        y -= 16
        doc.add_text(72, y, "Follow-up: ________________________________________________________", 'F1', 9, 0.2)
        y -= 30

    # Pages 26-28: Parent Contact Log (3 pages)
    for page_num in range(3):
        doc.new_page()
        doc.add_centered_text(740, f"PARENT CONTACT LOG ({page_num+1}/3)", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        doc.add_filled_rect(72, y-2, 468, 18, 0.85)
        doc.add_text(75, y, "Date", 'F2', 8, 0)
        doc.add_text(125, y, "Student", 'F2', 8, 0)
        doc.add_text(225, y, "Parent Name", 'F2', 8, 0)
        doc.add_text(335, y, "Method", 'F2', 8, 0)
        doc.add_text(395, y, "Topic/Outcome", 'F2', 8, 0)
        y -= 22
        for i in range(20):
            doc.add_rect(72, y, 468, 25)
            doc.add_line(122, y, 122, y+25, 0.3, 0.7)
            doc.add_line(222, y, 222, y+25, 0.3, 0.7)
            doc.add_line(332, y, 332, y+25, 0.3, 0.7)
            doc.add_line(392, y, 392, y+25, 0.3, 0.7)
            y -= 27

    # Page 29: Needs Assessment & Program Goals
    doc.new_page()
    doc.add_centered_text(740, "NEEDS ASSESSMENT & PROGRAM GOALS", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 705
    doc.add_text(72, y, "Top 5 Student Needs (from data):", 'F2', 11, 0)
    y -= 22
    for i in range(5):
        doc.add_text(72, y, f"{i+1}. ___________________________________  Data source: ____________", 'F1', 10, 0.2)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Annual Program Goals:", 'F2', 11, 0)
    y -= 22
    for i in range(3):
        doc.add_text(72, y, f"Goal {i+1}: __________________________________________________________", 'F1', 10, 0.2)
        y -= 18
        doc.add_text(72, y, "Measurable outcome: _______________________________________________", 'F1', 10, 0.2)
        y -= 18
        doc.add_text(72, y, "Timeline: ___________________  Status: [ ] Met [ ] In Progress [ ] Not Met", 'F1', 9, 0.2)
        y -= 28

    # Page 30: Self-Care for Counselors
    doc.new_page()
    doc.add_centered_text(740, "SELF-CARE FOR COUNSELORS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    doc.add_text(72, y, "You cannot pour from an empty cup. Check in with yourself:", 'F2', 11, 0)
    y -= 25
    doc.add_text(72, y, "Compassion fatigue signs I'm noticing:", 'F1', 10, 0.2)
    y -= 18
    for i in range(3):
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.3)
        y -= 18
    y -= 10
    doc.add_text(72, y, "My boundaries at work:", 'F2', 10, 0)
    y -= 18
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.3)
    y -= 22
    doc.add_text(72, y, "My self-care plan:", 'F2', 10, 0)
    y -= 18
    care = ["Daily:", "Weekly:", "Monthly:", "My own therapist/supervisor:"]
    for c in care:
        doc.add_text(72, y, f"{c} ___________________________________________________", 'F1', 10, 0.2)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Reminder: You carry heavy stories. You deserve support too.", 'F2', 11, 0)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book151_School_Counselor_Planner.pdf')
    print("Book151_School_Counselor_Planner.pdf created successfully!")

if __name__ == "__main__":
    create_book()
