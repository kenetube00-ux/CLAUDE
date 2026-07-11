#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "READING INTERVENTION TRACKER", 'F2', 20)
pdf.add_centered_text(485, "For Teachers & Reading Specialists", 'F4', 14)
pdf.add_centered_text(445, f"By {author}", 'F4', 12)
pdf.add_line(150, 425, 462, 425, 2)

# Page 2 - Copyright + Student Assessment Summary
pdf.new_page()
pdf.add_centered_text(740, "STUDENT READING LEVEL ASSESSMENT", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 715, "Teacher: _________________  School Year: ____________", 'F1', 10)
y = 693
pdf.add_text(50, y, "#", 'F2', 8)
pdf.add_text(65, y, "Student Name", 'F2', 8)
pdf.add_text(180, y, "Gr", 'F2', 8)
pdf.add_text(205, y, "Current Level", 'F2', 8)
pdf.add_text(300, y, "Goal Level", 'F2', 8)
pdf.add_text(380, y, "Intervention Type", 'F2', 8)
y -= 5
pdf.add_line(50, y, 562, y, 0.5)
y -= 15
for i in range(1, 11):
    pdf.add_text(50, y, f"{i}", 'F1', 8)
    pdf.add_line(65, y-2, 175, y-2, 0.3, 0.7)
    pdf.add_line(180, y-2, 200, y-2, 0.3, 0.7)
    pdf.add_line(205, y-2, 295, y-2, 0.3, 0.7)
    pdf.add_line(300, y-2, 375, y-2, 0.3, 0.7)
    pdf.add_line(380, y-2, 562, y-2, 0.3, 0.7)
    y -= 20
pdf.add_text(50, y-10, "Assessment tools used: _________________________________", 'F1', 9)
pdf.add_text(50, y-28, "Assessment dates: ______________________________________", 'F1', 9)
pdf.add_text(50, y-46, "Notes: ________________________________________________", 'F1', 9)

# Pages 3-17 - Weekly Intervention Log (15 pages)
for week in range(1, 16):
    pdf.new_page()
    pdf.add_centered_text(740, f"WEEKLY INTERVENTION LOG - WEEK {week}", 'F2', 12)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 715, f"Dates: _____________ to _____________", 'F1', 9)
    y = 698
    pdf.add_text(50, y, "Student", 'F2', 7)
    pdf.add_text(130, y, "Date", 'F2', 7)
    pdf.add_text(175, y, "Strategy", 'F2', 7)
    pdf.add_text(260, y, "Text Lvl", 'F2', 7)
    pdf.add_text(315, y, "Acc%", 'F2', 7)
    pdf.add_text(355, y, "WPM", 'F2', 7)
    pdf.add_text(395, y, "Comp", 'F2', 7)
    pdf.add_text(440, y, "Next Steps", 'F2', 7)
    y -= 5
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 13
    for i in range(30):
        pdf.add_line(50, y, 125, y, 0.3, 0.7)
        pdf.add_line(130, y, 170, y, 0.3, 0.7)
        pdf.add_line(175, y, 255, y, 0.3, 0.7)
        pdf.add_line(260, y, 310, y, 0.3, 0.7)
        pdf.add_line(315, y, 350, y, 0.3, 0.7)
        pdf.add_line(355, y, 390, y, 0.3, 0.7)
        pdf.add_line(395, y, 435, y, 0.3, 0.7)
        pdf.add_line(440, y, 562, y, 0.3, 0.7)
        y -= 15


# Pages 18-20 - Running Record Template (3 pages)
for pg in range(3):
    pdf.new_page()
    pdf.add_centered_text(740, f"RUNNING RECORD - PAGE {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 715, "Student: _________________  Date: ________  Text: __________________", 'F1', 9)
    pdf.add_text(50, 698, "Level: ______  Words: ______  Errors: ______  SC: ______", 'F1', 9)
    pdf.add_text(50, 681, "Accuracy: ______%  SC Rate: 1:______  Fluency WPM: ______", 'F1', 9)
    y = 660
    pdf.add_text(50, y, "TEXT", 'F2', 8)
    pdf.add_text(300, y, "E", 'F2', 8)
    pdf.add_text(330, y, "SC", 'F2', 8)
    pdf.add_text(360, y, "MSV (E)", 'F2', 8)
    pdf.add_text(430, y, "MSV (SC)", 'F2', 8)
    pdf.add_line(50, y-5, 562, y-5, 0.5)
    y -= 20
    for i in range(24):
        pdf.add_line(50, y, 290, y, 0.3, 0.7)
        pdf.add_line(300, y, 320, y, 0.3, 0.7)
        pdf.add_line(330, y, 350, y, 0.3, 0.7)
        pdf.add_line(360, y, 420, y, 0.3, 0.7)
        pdf.add_line(430, y, 490, y, 0.3, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "Comprehension questions:", 'F2', 9)
    pdf.add_line(50, y-18, 562, y-18, 0.5, 0.7)
    pdf.add_line(50, y-33, 562, y-33, 0.5, 0.7)

# Page 21 - Progress Monitoring Graph
pdf.new_page()
pdf.add_centered_text(740, "PROGRESS MONITORING GRAPH", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 715, "Student: _________________  Goal: _________________", 'F1', 10)
# Draw graph axes
pdf.add_line(80, 200, 80, 680, 1)
pdf.add_line(80, 200, 550, 200, 1)
pdf.add_text(30, 440, "Level", 'F2', 9)
pdf.add_text(290, 180, "Week", 'F2', 9)
# Y-axis labels
for i in range(10):
    y_pos = 200 + i * 48
    pdf.add_text(55, y_pos-3, f"{i+1}", 'F1', 8)
    pdf.add_line(78, y_pos, 550, y_pos, 0.3, 0.9)
# X-axis labels
for i in range(1, 16):
    x_pos = 80 + i * 30
    pdf.add_text(x_pos-3, 185, f"{i}", 'F1', 7)
pdf.add_text(50, 160, "Goal line: ________  Trend line: ________", 'F1', 9)

# Page 22 - Phonics Skills Checklist
pdf.new_page()
pdf.add_centered_text(740, "PHONICS SKILLS CHECKLIST", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 715, "Student: _________________", 'F1', 10)
skills_groups = [
    ("CVC Words", ["short a (cat)", "short e (bed)", "short i (pig)", "short o (dog)", "short u (cup)"]),
    ("Blends", ["initial (bl, cl, fl)", "initial (br, cr, dr)", "final (nd, nt, nk)", "3-letter (str, spr)"]),
    ("Digraphs", ["sh", "ch", "th", "wh", "ph"]),
    ("Vowel Teams", ["ai/ay", "ee/ea", "oa/ow", "oo", "ou/ow"]),
    ("R-Controlled", ["ar", "or", "er/ir/ur"]),
]
y = 693
for group, skills in skills_groups:
    pdf.add_text(50, y, group, 'F2', 9)
    y -= 14
    for s in skills:
        pdf.add_rect(65, y-7, 9, 9)
        pdf.add_text(80, y-5, s, 'F1', 8)
        pdf.add_text(220, y-5, "Date mastered: ______", 'F1', 8)
        y -= 14
    y -= 8

# Page 23 - Sight Word Tracker
pdf.new_page()
pdf.add_centered_text(740, "SIGHT WORD MASTERY TRACKER", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 715, "Student: _________________  Start date: _________", 'F1', 10)
y = 695
pdf.add_text(50, y, "WORD", 'F2', 8)
pdf.add_text(150, y, "Intro", 'F2', 8)
pdf.add_text(200, y, "Practice", 'F2', 8)
pdf.add_text(260, y, "Reading", 'F2', 8)
pdf.add_text(320, y, "Writing", 'F2', 8)
pdf.add_text(380, y, "Mastered", 'F2', 8)
pdf.add_text(445, y, "Date", 'F2', 8)
y -= 5
pdf.add_line(50, y, 562, y, 0.5)
y -= 13
for i in range(35):
    pdf.add_line(50, y, 145, y, 0.3, 0.7)
    pdf.add_rect(165, y-5, 9, 9)
    pdf.add_rect(220, y-5, 9, 9)
    pdf.add_rect(280, y-5, 9, 9)
    pdf.add_rect(340, y-5, 9, 9)
    pdf.add_rect(400, y-5, 9, 9)
    pdf.add_line(445, y, 520, y, 0.3, 0.7)
    y -= 14

# Pages 24-26 - Parent Communication (3 pages)
for pg in range(3):
    pdf.new_page()
    pdf.add_centered_text(740, f"PARENT COMMUNICATION LOG - {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    y = 710
    for i in range(5):
        pdf.add_text(50, y, "Student: _________________  Parent: _________________", 'F1', 9)
        pdf.add_text(50, y-15, "Date: ______  Method: Phone / Email / In-person / Note", 'F1', 9)
        pdf.add_text(50, y-30, "Discussion:", 'F2', 9)
        pdf.add_line(50, y-43, 562, y-43, 0.5, 0.7)
        pdf.add_line(50, y-58, 562, y-58, 0.5, 0.7)
        pdf.add_text(50, y-72, "Home practice recommendation:", 'F1', 8)
        pdf.add_line(215, y-74, 562, y-74, 0.3, 0.7)
        pdf.add_line(50, y-90, 562, y-90, 0.5, 0.5)
        y -= 108


# Page 27 - Intervention Group Planning
pdf.new_page()
pdf.add_centered_text(740, "INTERVENTION GROUP PLANNING", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
y = 710
for grp in range(3):
    pdf.add_text(50, y, f"GROUP {grp+1}:", 'F2', 10)
    pdf.add_text(50, y-15, "Students: _________________________________________________", 'F1', 9)
    pdf.add_text(50, y-30, "Focus area: ___________________  Level: ___________________", 'F1', 9)
    pdf.add_text(50, y-45, "Schedule: ________________  Materials: ____________________", 'F1', 9)
    pdf.add_text(50, y-60, "Strategy: _________________________________________________", 'F1', 9)
    pdf.add_text(50, y-75, "Goal: _____________________________________________________", 'F1', 9)
    pdf.add_line(50, y-90, 562, y-90, 0.5, 0.5)
    y -= 110

# Pages 28-30 - End-of-Quarter Summary + extra
for pg in range(3):
    pdf.new_page()
    titles = ["END-OF-QUARTER DATA SUMMARY", "STRATEGY EFFECTIVENESS NOTES",
              "PROFESSIONAL DEVELOPMENT NOTES"]
    pdf.add_centered_text(740, titles[pg], 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 0:
        pdf.add_text(50, 715, "Quarter: ______  Date range: ___________________", 'F1', 10)
        y = 693
        pdf.add_text(50, y, "Student", 'F2', 8)
        pdf.add_text(160, y, "Start Lvl", 'F2', 8)
        pdf.add_text(230, y, "End Lvl", 'F2', 8)
        pdf.add_text(300, y, "Growth", 'F2', 8)
        pdf.add_text(355, y, "Met Goal?", 'F2', 8)
        pdf.add_text(430, y, "Next Steps", 'F2', 8)
        y -= 5
        pdf.add_line(50, y, 562, y, 0.5)
        y -= 15
        for i in range(10):
            pdf.add_line(50, y, 155, y, 0.3, 0.7)
            pdf.add_line(160, y, 225, y, 0.3, 0.7)
            pdf.add_line(230, y, 295, y, 0.3, 0.7)
            pdf.add_line(300, y, 350, y, 0.3, 0.7)
            pdf.add_line(355, y, 425, y, 0.3, 0.7)
            pdf.add_line(430, y, 562, y, 0.3, 0.7)
            y -= 20
        pdf.add_text(50, y-10, "Overall notes:", 'F2', 9)
        for i in range(4):
            pdf.add_line(50, y-25-(i*16), 562, y-25-(i*16), 0.5, 0.7)
    else:
        y = 710
        for i in range(28):
            pdf.add_line(50, y, 562, y, 0.5, 0.7)
            y -= 22

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book186_Reading_Intervention_Log.pdf')
print("Book186_Reading_Intervention_Log.pdf created successfully!")
