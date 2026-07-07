"""Book 45: Women's Fitness & Workout Journal"""
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)

# Title page
pdf.new_page()
pdf.add_centered_text(400, "WOMEN'S FITNESS", 'F2', 22)
pdf.add_centered_text(365, "& WORKOUT JOURNAL", 'F2', 18)
pdf.add_line(116, 345, 316, 345, 1, 0.5)
pdf.add_centered_text(200, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(400, "Women's Fitness & Workout Journal", 'F2', 14)
pdf.add_centered_text(370, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(350, "All rights reserved.", 'F1', 10)

# Goal setting page
pdf.new_page()
pdf.add_centered_text(600, "My Fitness Goals", 'F2', 16)
pdf.add_text(50, 560, "Start Date: _______________", 'F1', 11)
pdf.add_text(50, 530, "Current Weight: _________ lbs/kg", 'F1', 11)
pdf.add_text(50, 500, "Goal Weight: _________ lbs/kg", 'F1', 11)
y = 460
pdf.add_text(50, y, "Current Measurements:", 'F2', 12)
y -= 22
measures = ["Bust", "Waist", "Hips", "Thighs", "Arms"]
for m in measures:
    pdf.add_text(60, y, f"{m}: _________", 'F1', 10)
    y -= 18
y -= 15
pdf.add_text(50, y, "My goals:", 'F2', 12)
y -= 20
for i in range(4):
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 18


# 12 weekly workout log pages
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for week in range(1, 13):
    pdf.new_page()
    pdf.add_text(50, 610, f"Week {week}", 'F2', 14)
    pdf.add_text(280, 610, "Dates: _____________", 'F1', 9)
    pdf.add_line(50, 600, 382, 600, 0.5, 0.5)
    y = 580
    for day in days:
        pdf.add_text(50, y, f"{day}:", 'F2', 9)
        pdf.add_text(110, y, "Exercise: ________________", 'F1', 8)
        y -= 14
        pdf.add_text(110, y, "Sets/Reps or Duration: __________  Calories: ____", 'F1', 8)
        y -= 14
        pdf.add_text(110, y, "How I felt: _______________", 'F1', 8)
        y -= 20

# Monthly progress page
pdf.new_page()
pdf.add_centered_text(600, "Monthly Progress Tracker", 'F2', 16)
y = 565
for month_num in range(1, 13):
    pdf.add_text(50, y, f"Month {month_num}: Weight____", 'F1', 9)
    pdf.add_text(180, y, "Waist____", 'F1', 9)
    pdf.add_text(250, y, "Hips____", 'F1', 9)
    pdf.add_text(320, y, "Photo? Y/N", 'F1', 9)
    y -= 17

# 4 Workout plan template pages
for plan_num in range(1, 5):
    pdf.new_page()
    pdf.add_text(50, 610, f"Workout Plan {plan_num}", 'F2', 14)
    pdf.add_text(50, 585, "Focus: _________________________", 'F1', 11)
    pdf.add_line(50, 575, 382, 575, 0.5, 0.5)
    y = 555
    pdf.add_text(50, y, "Exercise", 'F2', 10)
    pdf.add_text(200, y, "Sets", 'F2', 10)
    pdf.add_text(250, y, "Reps", 'F2', 10)
    pdf.add_text(310, y, "Rest", 'F2', 10)
    y -= 5
    pdf.add_line(50, y, 382, y, 0.5, 0.5)
    y -= 18
    for _ in range(12):
        pdf.add_line(50, y, 382, y, 0.5, 0.7)
        y -= 22

# Water tracker page
pdf.new_page()
pdf.add_centered_text(600, "Daily Water Tracker", 'F2', 16)
pdf.add_text(50, 570, "Goal: _____ glasses per day", 'F1', 11)
y = 540
pdf.add_text(50, y, "Day", 'F2', 10)
for i in range(1, 9):
    pdf.add_text(80 + i * 35, y, f"Glass {i}", 'F1', 7)
y -= 20
for d in range(1, 32):
    pdf.add_text(50, y, f"{d:2d}", 'F1', 9)
    for i in range(1, 9):
        pdf.add_rect(85 + i * 35, y - 3, 12, 12, 0.5, 0)
    y -= 16

pdf.save("Book45_Womens_Fitness_Journal.pdf")
print("Created Book45_Womens_Fitness_Journal.pdf")
