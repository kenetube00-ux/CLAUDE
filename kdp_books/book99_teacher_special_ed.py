"""Book 99: Special Education Teacher Planner"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.12)
    pdf.add_centered_text(530, "SPECIAL EDUCATION", 'F2', 28, 1)
    pdf.add_centered_text(492, "TEACHER PLANNER", 'F2', 28, 1)
    pdf.add_centered_text(440, "IEP Goals, Data & Documentation", 'F4', 15, 0.9)
    pdf.add_centered_text(395, "Caseload Management | Progress Monitoring", 'F1', 12, 0.8)
    pdf.add_centered_text(375, "Behavior Plans | Parent Communication", 'F1', 12, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    pdf.add_centered_text(170, "Designed for Special Education Professionals", 'F1', 11, 0.7)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "Special Education Teacher Planner", 'F2', 14)
    pdf.add_centered_text(478, "IEP Goals, Data & Documentation", 'F4', 11)
    pdf.add_centered_text(445, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(425, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(395, "For the tireless special education teachers who change lives daily.", 'F4', 9)


    # Page 1: Student Caseload Overview
    pdf.new_page()
    pdf.add_centered_text(750, "STUDENT CASELOAD OVERVIEW", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "School Year: ____________  Teacher: ______________________________", 'F1', 10)
    y -= 22
    pdf.add_text(72, y, "#", 'F2', 8)
    pdf.add_text(90, y, "Student Name", 'F2', 8)
    pdf.add_text(210, y, "Disability", 'F2', 8)
    pdf.add_text(310, y, "Grade", 'F2', 8)
    pdf.add_text(360, y, "IEP Date", 'F2', 8)
    pdf.add_text(440, y, "Annual Review", 'F2', 8)
    y -= 14
    for i in range(1, 21):
        pdf.add_text(72, y, f"{i}.", 'F1', 8)
        pdf.add_line(90, y - 2, 200, y - 2, 0.5, 0.5)
        pdf.add_line(210, y - 2, 300, y - 2, 0.5, 0.5)
        pdf.add_line(310, y - 2, 348, y - 2, 0.5, 0.5)
        pdf.add_line(360, y - 2, 430, y - 2, 0.5, 0.5)
        pdf.add_line(440, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18

    # Pages 2-11: IEP Goal Tracking Sheets (10 pages)
    for pg in range(1, 11):
        pdf.new_page()
        pdf.add_centered_text(750, f"IEP GOAL TRACKING - Sheet {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 720
        pdf.add_text(72, y, "Student: ____________________________  Grade: _____  IEP Date: __________", 'F1', 10)
        y -= 20
        pdf.add_text(72, y, "Goal Area: ________________________  Goal #: _____", 'F1', 10)
        y -= 22
        pdf.add_text(72, y, "ANNUAL GOAL:", 'F2', 10)
        y -= 14
        for i in range(2):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 5
        pdf.add_text(72, y, "Baseline: ______________  Target: ______________  Criteria: ______________", 'F1', 9)
        y -= 20
        pdf.add_text(72, y, "Data Collection Method:", 'F2', 9)
        methods = ["Frequency count", "Duration", "% accuracy", "Rubric", "Work samples", "Observation"]
        for m in methods:
            pdf.add_rect(72, y - 16, 8, 8, 0.5, 0.3)
            pdf.add_text(85, y - 14, m, 'F1', 8)
            y -= 14
        y -= 12
        pdf.add_text(72, y, "WEEKLY PROGRESS DATA:", 'F2', 10)
        y -= 16
        pdf.add_text(72, y, "Week", 'F2', 8)
        pdf.add_text(120, y, "Date", 'F2', 8)
        pdf.add_text(200, y, "Data Point", 'F2', 8)
        pdf.add_text(310, y, "Notes/Observations", 'F2', 8)
        pdf.add_text(490, y, "Trend", 'F2', 8)
        y -= 14
        for wk in range(1, 13):
            pdf.add_text(72, y, f"{wk}", 'F1', 8)
            pdf.add_line(120, y - 2, 190, y - 2, 0.5, 0.5)
            pdf.add_line(200, y - 2, 300, y - 2, 0.5, 0.5)
            pdf.add_line(310, y - 2, 480, y - 2, 0.5, 0.5)
            pdf.add_line(490, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 18
        y -= 5
        pdf.add_text(72, y, "Progress toward goal: [ ] Met  [ ] Progressing  [ ] Insufficient  [ ] Regression", 'F1', 9)


    # Page 12: Accommodation Checklist Master
    pdf.new_page()
    pdf.add_centered_text(750, "ACCOMMODATION CHECKLIST - MASTER LIST", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "Student: ____________________ Check all that apply to this student's IEP:", 'F1', 10)
    y -= 20
    pdf.add_text(72, y, "PRESENTATION:", 'F2', 9)
    y -= 14
    pres = ["Read aloud", "Large print", "Highlighted text", "Reduced items per page",
            "Visual schedules", "Graphic organizers", "Preferential seating", "Fidget tools allowed"]
    for p in pres:
        pdf.add_rect(72, y - 3, 8, 8, 0.5, 0.3)
        pdf.add_text(85, y, p, 'F1', 8)
        y -= 14
    y -= 5
    pdf.add_text(72, y, "RESPONSE:", 'F2', 9)
    y -= 14
    resp = ["Verbal responses", "Scribe provided", "Word processor", "Extended time (1.5x / 2x)",
            "Calculator allowed", "Spell check", "Reduced writing", "Alternative assignments"]
    for r in resp:
        pdf.add_rect(72, y - 3, 8, 8, 0.5, 0.3)
        pdf.add_text(85, y, r, 'F1', 8)
        y -= 14
    y -= 5
    pdf.add_text(72, y, "SETTING:", 'F2', 9)
    y -= 14
    sett = ["Small group testing", "Separate room", "Minimal distractions",
            "Flexible seating", "Breaks allowed", "Noise-reducing headphones"]
    for s in sett:
        pdf.add_rect(72, y - 3, 8, 8, 0.5, 0.3)
        pdf.add_text(85, y, s, 'F1', 8)
        y -= 14
    y -= 5
    pdf.add_text(72, y, "TIMING/SCHEDULING:", 'F2', 9)
    y -= 14
    timing = ["Extended time", "Frequent breaks", "Chunked assignments",
              "Flexible deadlines", "Morning testing preferred", "Reduced homework"]
    for t in timing:
        pdf.add_rect(72, y - 3, 8, 8, 0.5, 0.3)
        pdf.add_text(85, y, t, 'F1', 8)
        y -= 14
    y -= 5
    pdf.add_text(72, y, "BEHAVIORAL:", 'F2', 9)
    y -= 14
    behav = ["Behavior chart", "Token economy", "Positive reinforcement plan",
             "Sensory breaks", "Check-in/check-out", "Social skills instruction"]
    for b in behav:
        pdf.add_rect(72, y - 3, 8, 8, 0.5, 0.3)
        pdf.add_text(85, y, b, 'F1', 8)
        y -= 14

    # Pages 13-15: Behavior Intervention Plan Template (3 pages)
    # Page 13: ABC Data
    pdf.new_page()
    pdf.add_centered_text(750, "BEHAVIOR INTERVENTION PLAN - ABC DATA", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "Student: ________________________  Date range: _____________________", 'F1', 10)
    y -= 20
    pdf.add_text(72, y, "Target behavior (observable, measurable): _____________________________", 'F1', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "ABC DATA COLLECTION:", 'F2', 11)
    y -= 16
    pdf.add_text(72, y, "Date/Time", 'F2', 8)
    pdf.add_text(150, y, "Antecedent (what happened before)", 'F2', 8)
    pdf.add_text(350, y, "Behavior (what student did)", 'F2', 8)
    pdf.add_text(490, y, "Consequence", 'F2', 8)
    y -= 14
    for i in range(15):
        pdf.add_line(72, y, 140, y, 0.5, 0.5)
        pdf.add_line(150, y, 340, y, 0.5, 0.5)
        pdf.add_line(350, y, 480, y, 0.5, 0.5)
        pdf.add_line(490, y, 540, y, 0.5, 0.5)
        y -= 22
    y -= 5
    pdf.add_text(72, y, "Patterns noticed: ________________________________________________", 'F1', 9)

    # Page 14: Function & Replacement Behavior
    pdf.new_page()
    pdf.add_centered_text(750, "BIP - FUNCTION & REPLACEMENT BEHAVIOR", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    pdf.add_text(72, y, "Student: ________________________", 'F1', 10)
    y -= 25
    pdf.add_text(72, y, "HYPOTHESIZED FUNCTION OF BEHAVIOR:", 'F2', 11)
    y -= 16
    functions = ["Escape/Avoidance (getting OUT of something)",
                 "Attention (getting attention from adults/peers)",
                 "Tangible (getting access to something)",
                 "Sensory (feels good / meets a sensory need)"]
    for f in functions:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, f, 'F1', 9)
        y -= 18
    y -= 10
    pdf.add_text(72, y, "Evidence for this function:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "REPLACEMENT BEHAVIOR (serves same function, appropriate):", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "HOW TO TEACH THE REPLACEMENT BEHAVIOR:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "REINFORCEMENT PLAN:", 'F2', 10)
    y -= 16
    pdf.add_text(72, y, "Reinforcer: _____________________________  Schedule: _________________", 'F1', 9)
    y -= 18
    pdf.add_text(72, y, "Criteria for earning: _______________________________________________", 'F1', 9)
    y -= 18
    pdf.add_text(72, y, "How/when delivered: _______________________________________________", 'F1', 9)

    # Page 15: BIP Implementation
    pdf.new_page()
    pdf.add_centered_text(750, "BIP - IMPLEMENTATION & MONITORING", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    pdf.add_text(72, y, "PREVENTION STRATEGIES (proactive):", 'F2', 10)
    y -= 16
    for i in range(4):
        pdf.add_text(72, y, f"{i+1}.", 'F1', 9)
        pdf.add_line(90, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18
    y -= 10
    pdf.add_text(72, y, "RESPONSE TO TARGET BEHAVIOR (what adults do):", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "CRISIS PLAN (if behavior escalates):", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "DATA TRACKING (frequency per week):", 'F2', 10)
    y -= 16
    pdf.add_text(72, y, "Week", 'F2', 8)
    pdf.add_text(120, y, "Mon", 'F2', 8)
    pdf.add_text(170, y, "Tue", 'F2', 8)
    pdf.add_text(220, y, "Wed", 'F2', 8)
    pdf.add_text(270, y, "Thu", 'F2', 8)
    pdf.add_text(320, y, "Fri", 'F2', 8)
    pdf.add_text(370, y, "Total", 'F2', 8)
    pdf.add_text(430, y, "Notes", 'F2', 8)
    y -= 14
    for wk in range(1, 9):
        pdf.add_text(72, y, f"{wk}", 'F1', 8)
        pdf.add_line(120, y - 2, 160, y - 2, 0.5, 0.5)
        pdf.add_line(170, y - 2, 210, y - 2, 0.5, 0.5)
        pdf.add_line(220, y - 2, 260, y - 2, 0.5, 0.5)
        pdf.add_line(270, y - 2, 310, y - 2, 0.5, 0.5)
        pdf.add_line(320, y - 2, 360, y - 2, 0.5, 0.5)
        pdf.add_line(370, y - 2, 420, y - 2, 0.5, 0.5)
        pdf.add_line(430, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
    pdf.add_text(72, y, "BIP effective? [ ] Yes, continue  [ ] Modify  [ ] Redesign", 'F1', 9)


    # Page 16: Related Services Log
    pdf.new_page()
    pdf.add_centered_text(750, "RELATED SERVICES LOG", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "Student", 'F2', 8)
    pdf.add_text(170, y, "Service", 'F2', 8)
    pdf.add_text(270, y, "Provider", 'F2', 8)
    pdf.add_text(370, y, "Frequency", 'F2', 8)
    pdf.add_text(460, y, "Minutes", 'F2', 8)
    pdf.add_text(510, y, "Location", 'F2', 8)
    y -= 14
    for i in range(25):
        pdf.add_line(72, y, 160, y, 0.5, 0.5)
        pdf.add_line(170, y, 260, y, 0.5, 0.5)
        pdf.add_line(270, y, 360, y, 0.5, 0.5)
        pdf.add_line(370, y, 450, y, 0.5, 0.5)
        pdf.add_line(460, y, 500, y, 0.5, 0.5)
        pdf.add_line(510, y, 540, y, 0.5, 0.5)
        y -= 20

    # Pages 17-18: Parent Communication Tracker (2 pages)
    for pg in range(1, 3):
        pdf.new_page()
        pdf.add_centered_text(750, f"PARENT COMMUNICATION TRACKER - Page {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 720
        pdf.add_text(72, y, "Date", 'F2', 8)
        pdf.add_text(130, y, "Student", 'F2', 8)
        pdf.add_text(230, y, "Parent/Guardian", 'F2', 8)
        pdf.add_text(350, y, "Method", 'F2', 8)
        pdf.add_text(420, y, "Topic/Notes", 'F2', 8)
        y -= 14
        for i in range(25):
            pdf.add_line(72, y, 120, y, 0.5, 0.5)
            pdf.add_line(130, y, 220, y, 0.5, 0.5)
            pdf.add_line(230, y, 340, y, 0.5, 0.5)
            pdf.add_line(350, y, 410, y, 0.5, 0.5)
            pdf.add_line(420, y, 540, y, 0.5, 0.5)
            y -= 20

    # Page 19: Annual Review Preparation Checklist
    pdf.new_page()
    pdf.add_centered_text(750, "ANNUAL REVIEW PREPARATION CHECKLIST", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "Student: __________________________  Review Date: __________________", 'F1', 10)
    y -= 22
    pdf.add_text(72, y, "BEFORE THE MEETING:", 'F2', 10)
    y -= 16
    before = [
        "Review current IEP goals and progress data",
        "Collect work samples demonstrating progress",
        "Complete progress reports on all goals",
        "Gather input from general education teachers",
        "Gather input from related service providers",
        "Review assessment data / state testing results",
        "Draft new goals based on present levels",
        "Update present levels of performance",
        "Send parent notification / meeting invitation (10 days prior)",
        "Confirm parent attendance / offer alternate times",
        "Prepare parent-friendly progress summary",
        "Reserve meeting room and send calendar invites",
        "Prepare copies of documents for all team members",
        "Update transition plan (if student 14+)",
    ]
    for item in before:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, item, 'F1', 9)
        y -= 17
    y -= 10
    pdf.add_text(72, y, "DURING THE MEETING:", 'F2', 10)
    y -= 16
    during = [
        "Review current goals and data with team",
        "Discuss parent input and concerns",
        "Present updated present levels",
        "Propose and discuss new goals",
        "Review/update accommodations and modifications",
        "Determine placement and services",
        "Obtain signatures",
    ]
    for item in during:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, item, 'F1', 9)
        y -= 17

    # Page 20: Transition Planning Worksheet (ages 14+)
    pdf.new_page()
    pdf.add_centered_text(750, "TRANSITION PLANNING WORKSHEET (Ages 14+)", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    pdf.add_text(72, y, "Student: ________________________  Age: _____  Grad Year: __________", 'F1', 10)
    y -= 22
    fields = [
        ("Post-secondary EDUCATION goal:", 2),
        ("Post-secondary EMPLOYMENT goal:", 2),
        ("Independent LIVING goal:", 2),
        ("Transition assessments completed:", 2),
        ("Student's interests/preferences:", 2),
        ("Community experiences needed:", 2),
        ("Agency connections (Vocational Rehab, etc.):", 2),
        ("Self-advocacy skills to develop:", 2),
        ("Daily living skills to teach:", 2),
        ("Timeline for transition activities:", 3),
    ]
    for label, lines in fields:
        pdf.add_text(72, y, label, 'F2', 9)
        y -= 14
        for _ in range(lines):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 14
        y -= 6


    # Pages 21-24: Progress Report Template (4 pages)
    for pg in range(1, 5):
        pdf.new_page()
        pdf.add_centered_text(750, f"PROGRESS REPORT - Page {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 720
        pdf.add_text(72, y, "Student: ________________________  Reporting Period: ________________", 'F1', 10)
        y -= 20
        pdf.add_text(72, y, "Teacher: ________________________  Date: __________________________", 'F1', 10)
        y -= 25
        for goal in range(1, 4):
            pdf.add_text(72, y, f"GOAL {goal + (pg-1)*3}:", 'F2', 10)
            y -= 14
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 14
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
            pdf.add_text(72, y, "Baseline: _________  Current level: _________  Target: _________", 'F1', 9)
            y -= 16
            pdf.add_text(72, y, "Progress: [ ] Met [ ] Sufficient [ ] Insufficient [ ] Not addressed", 'F1', 9)
            y -= 16
            pdf.add_text(72, y, "Data summary:", 'F1', 9)
            pdf.add_line(160, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 16
            pdf.add_text(72, y, "Strategies used:", 'F1', 9)
            pdf.add_line(160, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 16
            pdf.add_text(72, y, "Recommendations:", 'F1', 9)
            pdf.add_line(170, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 22

    # Pages 25-27: Meeting Notes Pages (3 pages)
    for pg in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(750, f"MEETING NOTES - Page {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 720
        pdf.add_text(72, y, "Date: __________  Student: __________________  Meeting Type: ___________", 'F1', 10)
        y -= 18
        pdf.add_text(72, y, "Attendees: _________________________________________________________", 'F1', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 20
        pdf.add_text(72, y, "DISCUSSION POINTS:", 'F2', 10)
        y -= 14
        for i in range(8):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 5
        pdf.add_text(72, y, "DECISIONS MADE:", 'F2', 10)
        y -= 14
        for i in range(5):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 5
        pdf.add_text(72, y, "ACTION ITEMS:", 'F2', 10)
        y -= 14
        pdf.add_text(72, y, "What", 'F2', 8)
        pdf.add_text(280, y, "Who", 'F2', 8)
        pdf.add_text(380, y, "By When", 'F2', 8)
        pdf.add_text(480, y, "Done?", 'F2', 8)
        y -= 12
        for i in range(6):
            pdf.add_line(72, y, 270, y, 0.5, 0.5)
            pdf.add_line(280, y, 370, y, 0.5, 0.5)
            pdf.add_line(380, y, 470, y, 0.5, 0.5)
            pdf.add_rect(480, y - 4, 8, 8, 0.5, 0.3)
            y -= 18
        pdf.add_text(72, y, "Follow-up date: __________", 'F1', 9)

    # Page 28: Professional Development Log
    pdf.new_page()
    pdf.add_centered_text(750, "PROFESSIONAL DEVELOPMENT LOG", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "Date", 'F2', 8)
    pdf.add_text(140, y, "Training/Workshop", 'F2', 8)
    pdf.add_text(340, y, "Hours", 'F2', 8)
    pdf.add_text(400, y, "Key Takeaway", 'F2', 8)
    y -= 14
    for i in range(22):
        pdf.add_line(72, y, 130, y, 0.5, 0.5)
        pdf.add_line(140, y, 330, y, 0.5, 0.5)
        pdf.add_line(340, y, 390, y, 0.5, 0.5)
        pdf.add_line(400, y, 540, y, 0.5, 0.5)
        y -= 22
    y -= 5
    pdf.add_text(72, y, "Total PD hours this year: _______  Required: _______", 'F1', 9)
    y -= 16
    pdf.add_text(72, y, "Areas I want to grow in next year: ________________________________", 'F1', 9)


    # Page 29: Self-Care for Special Ed Teachers
    pdf.new_page()
    pdf.add_centered_text(750, "SELF-CARE FOR SPECIAL ED TEACHERS", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 710
    text = [
        "Special education is rewarding AND exhausting. You cannot pour from",
        "an empty cup. Your self-care is not selfish - it's essential.",
        "",
        "BURNOUT WARNING SIGNS (check any you're experiencing):",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 16
    signs = [
        "Dreading going to work", "Crying in your car before/after school",
        "Feeling like nothing you do makes a difference",
        "Short-tempered with students or coworkers",
        "Physical symptoms (headaches, stomach issues, insomnia)",
        "Unable to 'turn off' work thoughts at home",
        "Compassion fatigue (emotionally numb)",
        "Considering leaving the profession",
    ]
    for s in signs:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, s, 'F1', 9)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "If you checked 3+, please talk to someone. You deserve support too.", 'F2', 9)
    y -= 20
    pdf.add_text(72, y, "MY SELF-CARE PLAN:", 'F2', 10)
    y -= 16
    pdf.add_text(72, y, "Daily (something small every day):", 'F1', 9)
    pdf.add_line(270, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 18
    pdf.add_text(72, y, "Weekly (protected time for me):", 'F1', 9)
    pdf.add_line(270, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 18
    pdf.add_text(72, y, "Monthly (bigger self-care activity):", 'F1', 9)
    pdf.add_line(270, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 18
    pdf.add_text(72, y, "Boundary I will set:", 'F1', 9)
    pdf.add_line(200, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 18
    pdf.add_text(72, y, "Person I can vent to safely:", 'F1', 9)
    pdf.add_line(240, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "REMINDER: You chose one of the hardest jobs in education.", 'F5', 10)
    y -= 16
    pdf.add_text(72, y, "You make a difference even when you can't see it yet.", 'F5', 10)

    # Page 30: Caseload at a Glance (second semester update)
    pdf.new_page()
    pdf.add_centered_text(750, "MID-YEAR CASELOAD UPDATE", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "#", 'F2', 8)
    pdf.add_text(90, y, "Student", 'F2', 8)
    pdf.add_text(200, y, "Goals On Track?", 'F2', 8)
    pdf.add_text(320, y, "BIP Needed?", 'F2', 8)
    pdf.add_text(420, y, "Next Steps", 'F2', 8)
    y -= 14
    for i in range(1, 21):
        pdf.add_text(72, y, f"{i}.", 'F1', 8)
        pdf.add_line(90, y - 2, 190, y - 2, 0.5, 0.5)
        pdf.add_line(200, y - 2, 310, y - 2, 0.5, 0.5)
        pdf.add_line(320, y - 2, 410, y - 2, 0.5, 0.5)
        pdf.add_line(420, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18
    y -= 10
    pdf.add_text(72, y, "Students meeting all goals: _____  Students needing goal revision: _____", 'F1', 9)
    y -= 16
    pdf.add_text(72, y, "Students at risk of regression: _____  New referrals pending: _____", 'F1', 9)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book99_Special_Ed_Teacher_Planner.pdf')
    print("Book99_Special_Ed_Teacher_Planner.pdf created successfully!")

if __name__ == "__main__":
    create_book()
