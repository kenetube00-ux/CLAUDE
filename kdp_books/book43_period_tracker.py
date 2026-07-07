"""Book 43: Period Tracker & Cycle Journal"""
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)

# Title page
pdf.new_page()
pdf.add_centered_text(400, "MY PERIOD TRACKER", 'F2', 22)
pdf.add_centered_text(365, "& CYCLE JOURNAL", 'F2', 18)
pdf.add_line(130, 345, 302, 345, 1, 0.5)
pdf.add_centered_text(200, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(400, "My Period Tracker & Cycle Journal", 'F2', 14)
pdf.add_centered_text(370, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(350, "All rights reserved.", 'F1', 10)

# Cycle info page
pdf.new_page()
pdf.add_centered_text(590, "My Cycle Information", 'F2', 16)
pdf.add_text(50, 540, "Average Cycle Length: _________ days", 'F1', 12)
pdf.add_text(50, 510, "Average Period Length: _________ days", 'F1', 12)
pdf.add_text(50, 480, "Last Period Start Date: ___ / ___ / ______", 'F1', 12)
pdf.add_text(50, 440, "Notes:", 'F2', 12)
pdf.add_line(50, 420, 382, 420, 0.5, 0.6)
pdf.add_line(50, 400, 382, 400, 0.5, 0.6)
pdf.add_line(50, 380, 382, 380, 0.5, 0.6)

# 12 monthly cycle tracking pages
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

for month in months:
    pdf.new_page()
    pdf.add_text(50, 610, f"Month: {month}", 'F2', 14)
    pdf.add_text(50, 585, "Year: ________", 'F1', 10)
    pdf.add_line(50, 575, 382, 575, 0.5, 0.5)

    y = 555
    pdf.add_text(50, y, "Day 1 Start Date: ___ / ___", 'F1', 11)
    y -= 20
    pdf.add_text(50, y, "Day Period Ended: ___ / ___", 'F1', 11)
    y -= 20
    pdf.add_text(50, y, "Total Days: _______", 'F1', 11)

    y -= 30
    pdf.add_text(50, y, "Flow Level Each Day (1=light, 5=heavy):", 'F2', 10)
    y -= 18
    pdf.add_text(55, y, "Day 1:__  2:__  3:__  4:__  5:__  6:__  7:__", 'F3', 9)

    y -= 30
    pdf.add_text(50, y, "Symptoms (check all that apply):", 'F2', 10)
    y -= 18
    symptoms = ["Cramps", "Headache", "Bloating", "Fatigue", "Mood swings", "Acne", "Back pain"]
    for s in symptoms:
        pdf.add_text(60, y, f"[ ] {s}", 'F1', 10)
        y -= 16

    y -= 15
    pdf.add_text(50, y, "Mood:", 'F2', 10)
    y -= 18
    pdf.add_text(55, y, "Day 1:____  2:____  3:____  4:____  5:____", 'F1', 9)

    y -= 25
    pdf.add_text(50, y, "Medication: _________________________________", 'F1', 10)

    y -= 25
    pdf.add_text(50, y, "Notes:", 'F2', 10)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

# PMS Pattern Tracker page
pdf.new_page()
pdf.add_centered_text(600, "PMS Pattern Tracker", 'F2', 16)
pdf.add_text(50, 565, "Track your PMS symptoms to identify patterns.", 'F1', 11)
y = 535
pdf.add_text(50, y, "Common PMS symptoms and when they occur:", 'F2', 11)
y -= 25
pms_symptoms = ["Irritability", "Cravings", "Breast tenderness", "Insomnia",
                "Anxiety", "Headaches", "Bloating", "Fatigue"]
for s in pms_symptoms:
    pdf.add_text(55, y, f"{s}: Days before period: ___  Severity (1-5): ___", 'F1', 10)
    y -= 22

y -= 20
pdf.add_text(50, y, "What helps me manage PMS:", 'F2', 11)
y -= 18
for _ in range(4):
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 18

# Doctor visit log (4 entries)
pdf.new_page()
pdf.add_centered_text(600, "Doctor Visit Log", 'F2', 16)
y = 560
for visit in range(1, 5):
    pdf.add_text(50, y, f"Visit {visit}", 'F2', 12)
    y -= 20
    pdf.add_text(55, y, "Date: ___ / ___ / ______", 'F1', 10)
    y -= 18
    pdf.add_text(55, y, "Doctor: ________________________________", 'F1', 10)
    y -= 18
    pdf.add_text(55, y, "Reason: ________________________________", 'F1', 10)
    y -= 18
    pdf.add_text(55, y, "Notes: _________________________________", 'F1', 10)
    y -= 18
    pdf.add_text(55, y, "Follow-up: _____________________________", 'F1', 10)
    y -= 30

pdf.save("Book43_Period_Tracker.pdf")
print("Created Book43_Period_Tracker.pdf")
