#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(420, "NEWBORN DAILY LOG", 'F2', 17)
pdf.add_centered_text(393, "Feed, Sleep, Diaper & Health Tracker", 'F4', 11)
pdf.add_centered_text(365, f"By {author}", 'F4', 11)
pdf.add_line(80, 345, 352, 345, 2)

# Page 2 - Baby Info
pdf.new_page()
pdf.add_centered_text(620, "BABY INFORMATION", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
fields = [("Baby's name:", ""), ("Date of birth:", ""), ("Time of birth:", ""),
          ("Weight at birth:", ""), ("Length at birth:", ""),
          ("Blood type:", ""), ("Pediatrician:", ""), ("Pediatrician phone:", ""),
          ("Hospital:", ""), ("Insurance:", ""), ("Policy #:", ""),
          ("Allergies:", ""), ("Special notes:", "")]
y = 590
for label, _ in fields:
    pdf.add_text(40, y, label, 'F2', 9)
    pdf.add_line(175, y-2, 392, y-2, 0.5, 0.7)
    y -= 22

# Pages 3-32 - 90 daily entries (3 per page = 30 pages)
for page in range(30):
    pdf.new_page()
    for entry in range(3):
        day_num = page * 3 + entry + 1
        y_base = 620 - entry * 200
        pdf.add_filled_rect(38, y_base - 188, 357, 192, 0.97)
        pdf.add_text(40, y_base, f"DAY {day_num}", 'F2', 9)
        pdf.add_text(100, y_base, "Date: ________", 'F1', 7)
        pdf.add_text(200, y_base, "Weight: ________", 'F1', 7)
        pdf.add_line(40, y_base - 8, 392, y_base - 8, 0.3)
        
        # Feeding section
        y = y_base - 20
        pdf.add_text(42, y, "FEED", 'F2', 7)
        pdf.add_text(75, y, "Time", 'F2', 6)
        pdf.add_text(115, y, "Type(B-L/R/Bot)", 'F2', 6)
        pdf.add_text(210, y, "Amount/Min", 'F2', 6)
        pdf.add_text(290, y, "Notes", 'F2', 6)
        y -= 10
        for i in range(4):
            pdf.add_line(75, y, 110, y, 0.3, 0.7)
            pdf.add_line(115, y, 205, y, 0.3, 0.7)
            pdf.add_line(210, y, 285, y, 0.3, 0.7)
            pdf.add_line(290, y, 392, y, 0.3, 0.7)
            y -= 10
        
        # Diaper section
        y -= 5
        pdf.add_text(42, y, "DIAPER", 'F2', 7)
        pdf.add_text(85, y, "Times: W___  D___  Both___", 'F1', 6)
        pdf.add_text(250, y, "Color/Notes: __________", 'F1', 6)
        
        # Sleep section
        y -= 14
        pdf.add_text(42, y, "SLEEP", 'F2', 7)
        pdf.add_text(80, y, "Naps: ___  Night: ___hrs  Total: ___hrs", 'F1', 6)
        
        # Health section
        y -= 14
        pdf.add_text(42, y, "HEALTH", 'F2', 7)
        pdf.add_text(85, y, "Temp:___  Meds:_________  Tummy time:___min", 'F1', 6)
        
        # Notes
        y -= 14
        pdf.add_text(42, y, "Notes:", 'F1', 6)
        pdf.add_line(75, y-2, 392, y-2, 0.3, 0.7)


# Page 33 - Weight Check Log
pdf.new_page()
pdf.add_centered_text(620, "WEIGHT CHECK LOG", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
y = 590
pdf.add_text(40, y, "Date", 'F2', 9)
pdf.add_text(110, y, "Age", 'F2', 9)
pdf.add_text(160, y, "Weight", 'F2', 9)
pdf.add_text(225, y, "Percentile", 'F2', 9)
pdf.add_text(310, y, "Notes", 'F2', 9)
y -= 5
pdf.add_line(40, y, 392, y, 0.5)
y -= 14
for i in range(24):
    pdf.add_line(40, y, 105, y, 0.3, 0.7)
    pdf.add_line(110, y, 155, y, 0.3, 0.7)
    pdf.add_line(160, y, 220, y, 0.3, 0.7)
    pdf.add_line(225, y, 305, y, 0.3, 0.7)
    pdf.add_line(310, y, 392, y, 0.3, 0.7)
    y -= 16

# Pages 34-35 - Pediatrician Visit Notes (6 entries over 2 pages)
for pg in range(2):
    pdf.new_page()
    pdf.add_centered_text(620, f"PEDIATRICIAN VISITS - PAGE {pg+1}", 'F2', 13)
    pdf.add_line(40, 610, 392, 610, 1)
    y = 590
    for v in range(3):
        pdf.add_text(40, y, f"Visit #{pg*3+v+1}", 'F2', 10)
        pdf.add_text(100, y, "Date: ________  Age: ________", 'F1', 8)
        y -= 15
        pdf.add_text(40, y, "Weight: _______  Length: _______  Head: _______", 'F1', 8)
        y -= 15
        pdf.add_text(40, y, "Concerns discussed:", 'F1', 8)
        pdf.add_line(150, y-2, 392, y-2, 0.3, 0.7)
        y -= 15
        pdf.add_text(40, y, "Doctor's notes/advice:", 'F1', 8)
        pdf.add_line(155, y-2, 392, y-2, 0.3, 0.7)
        y -= 15
        pdf.add_line(40, y-2, 392, y-2, 0.3, 0.7)
        y -= 15
        pdf.add_text(40, y, "Follow-up needed:", 'F1', 8)
        pdf.add_line(140, y-2, 392, y-2, 0.3, 0.7)
        y -= 15
        pdf.add_text(40, y, "Next appointment: _________________", 'F1', 8)
        pdf.add_line(40, y-12, 392, y-12, 0.5, 0.5)
        y -= 30

# Page 36 - Milestone Tracker
pdf.new_page()
pdf.add_centered_text(620, "MILESTONE TRACKER", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
milestones = [
    "First smile", "First laugh", "Holds head up",
    "Rolls over (tummy to back)", "Rolls over (back to tummy)",
    "Grabs a toy", "Brings hands together", "Coos/babbles",
    "Recognizes parents", "Sleeps through the night",
    "First tooth", "Sits with support", "Sits alone",
    "First solid food", "Crawls", "Pulls to stand",
    "First word", "First steps", "Waves bye-bye", "Claps hands"
]
y = 590
for m in milestones:
    pdf.add_text(40, y, m, 'F1', 8)
    pdf.add_text(215, y, "Date: ________", 'F1', 8)
    pdf.add_text(310, y, "Age: ________", 'F1', 8)
    y -= 16

# Page 37 - Growth Chart Recording
pdf.new_page()
pdf.add_centered_text(620, "GROWTH CHART RECORDING", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
y = 590
pdf.add_text(40, y, "Month", 'F2', 8)
pdf.add_text(90, y, "Weight", 'F2', 8)
pdf.add_text(145, y, "W%", 'F2', 8)
pdf.add_text(180, y, "Length", 'F2', 8)
pdf.add_text(235, y, "L%", 'F2', 8)
pdf.add_text(265, y, "Head", 'F2', 8)
pdf.add_text(315, y, "H%", 'F2', 8)
pdf.add_text(345, y, "Notes", 'F2', 8)
y -= 5
pdf.add_line(40, y, 392, y, 0.5)
y -= 14
months = ["Birth", "1 mo", "2 mo", "4 mo", "6 mo", "9 mo", "12 mo",
           "15 mo", "18 mo", "24 mo"]
for m in months:
    pdf.add_text(40, y, m, 'F1', 8)
    pdf.add_line(90, y, 140, y, 0.3, 0.7)
    pdf.add_line(145, y, 175, y, 0.3, 0.7)
    pdf.add_line(180, y, 230, y, 0.3, 0.7)
    pdf.add_line(235, y, 260, y, 0.3, 0.7)
    pdf.add_line(265, y, 310, y, 0.3, 0.7)
    pdf.add_line(315, y, 340, y, 0.3, 0.7)
    pdf.add_line(345, y, 392, y, 0.3, 0.7)
    y -= 18

# Page 38 - Vaccination Record
pdf.new_page()
pdf.add_centered_text(620, "VACCINATION RECORD", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
vaccines = [
    ("Hepatitis B", "Birth, 1mo, 6mo"), ("DTaP", "2mo, 4mo, 6mo, 15mo"),
    ("IPV (Polio)", "2mo, 4mo, 6-18mo"), ("Hib", "2mo, 4mo, 6mo, 12mo"),
    ("PCV13", "2mo, 4mo, 6mo, 12mo"), ("Rotavirus", "2mo, 4mo, 6mo"),
    ("Influenza", "6mo, annually"), ("MMR", "12-15mo"),
    ("Varicella", "12-15mo"), ("Hepatitis A", "12-23mo"),
]
y = 590
pdf.add_text(40, y, "Vaccine", 'F2', 8)
pdf.add_text(140, y, "Schedule", 'F2', 8)
pdf.add_text(270, y, "Dates Given", 'F2', 8)
y -= 5
pdf.add_line(40, y, 392, y, 0.5)
y -= 14
for vax, sched in vaccines:
    pdf.add_text(40, y, vax, 'F1', 8)
    pdf.add_text(140, y, sched, 'F1', 7)
    pdf.add_line(270, y, 392, y, 0.3, 0.7)
    y -= 18

# Pages 39-40 - Questions for Doctor + Notes
pdf.new_page()
pdf.add_centered_text(620, "QUESTIONS FOR DOCTOR", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
y = 590
for i in range(25):
    pdf.add_text(40, y, f"{i+1}.", 'F1', 9)
    pdf.add_line(55, y-2, 392, y-2, 0.5, 0.7)
    y -= 18

pdf.new_page()
pdf.add_centered_text(620, "NOTES & MEMORIES", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
y = 590
for i in range(28):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book191_Newborn_Daily_Log.pdf')
print("Book191_Newborn_Daily_Log.pdf created successfully!")
