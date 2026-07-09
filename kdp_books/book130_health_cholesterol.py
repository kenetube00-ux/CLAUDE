from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "CHOLESTEROL & HEART HEALTH TRACKER"
subtitle = "Monitor Your Numbers, Protect Your Heart"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, title, 'F2', 14)
pdf.add_centered_text(455, subtitle, 'F4', 11)
pdf.add_centered_text(380, "Track Cholesterol, Blood Pressure, and", 'F4', 10)
pdf.add_centered_text(365, "Heart-Healthy Habits in One Place", 'F4', 10)
pdf.add_centered_text(230, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, title, 'F2', 10)
pdf.add_centered_text(470, f"Copyright 2025 {author}", 'F4', 9)
pdf.add_centered_text(455, "All rights reserved.", 'F4', 9)
pdf.add_centered_text(425, "This book is for tracking purposes only and does not", 'F4', 8)
pdf.add_centered_text(412, "replace medical advice from your healthcare provider.", 'F4', 8)

# Page 3: Understanding Cholesterol
pdf.new_page()
pdf.add_centered_text(610, "UNDERSTANDING CHOLESTEROL", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
lines = [
    "Cholesterol is a waxy substance your body needs, but too much",
    "of the wrong kind can build up in arteries and cause heart disease.",
    "",
    "HDL (High-Density Lipoprotein) - 'GOOD' cholesterol",
    "  - Removes cholesterol from arteries",
    "  - Higher is BETTER (aim for 60+ mg/dL)",
    "  - Raised by: exercise, healthy fats, not smoking",
    "",
    "LDL (Low-Density Lipoprotein) - 'BAD' cholesterol",
    "  - Deposits cholesterol IN arteries (forms plaque)",
    "  - Lower is BETTER (aim for under 100 mg/dL)",
    "  - Lowered by: diet, exercise, medications (statins)",
    "",
    "TRIGLYCERIDES - Blood fats from food",
    "  - High levels increase heart disease risk",
    "  - Aim for under 150 mg/dL",
    "  - Lowered by: reducing sugar, alcohol, refined carbs",
    "",
    "TOTAL CHOLESTEROL = HDL + LDL + (Triglycerides / 5)",
    "  - Desirable: under 200 mg/dL",
    "  - Borderline high: 200-239 mg/dL",
    "  - High: 240+ mg/dL",
    "",
    "WHY IT MATTERS:",
    "High cholesterol has NO SYMPTOMS until a heart attack or stroke.",
    "The ONLY way to know your numbers is through a blood test.",
    "Regular monitoring helps you catch changes early."
]
for line in lines:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 4: Healthy Ranges Reference Chart
pdf.new_page()
pdf.add_centered_text(610, "HEALTHY RANGES REFERENCE CHART", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "CHOLESTEROL LEVELS (mg/dL):", 'F2', 10)
y -= 16
chol_ranges = [
    ("Total Cholesterol", "< 200", "200-239", "240+"),
    ("LDL ('Bad')", "< 100", "100-159", "160+"),
    ("HDL ('Good')", "60+", "40-59", "< 40"),
    ("Triglycerides", "< 150", "150-199", "200+"),
]
pdf.add_filled_rect(40, y - 3, 352, 14, 0.85)
pdf.add_text(45, y, "Measure", 'F2', 8)
pdf.add_text(150, y, "Optimal", 'F2', 8)
pdf.add_text(230, y, "Borderline", 'F2', 8)
pdf.add_text(315, y, "High Risk", 'F2', 8)
y -= 16
for measure, optimal, border, high in chol_ranges:
    pdf.add_text(45, y, measure, 'F4', 8)
    pdf.add_text(155, y, optimal, 'F3', 8)
    pdf.add_text(235, y, border, 'F3', 8)
    pdf.add_text(320, y, high, 'F3', 8)
    y -= 14
y -= 15
pdf.add_text(40, y, "BLOOD PRESSURE (mmHg):", 'F2', 10)
y -= 16
bp_ranges = [
    ("Normal", "< 120/80"),
    ("Elevated", "120-129 / < 80"),
    ("Stage 1 Hypertension", "130-139 / 80-89"),
    ("Stage 2 Hypertension", "140+ / 90+"),
    ("Crisis (call 911)", "180+ / 120+"),
]
for label, value in bp_ranges:
    pdf.add_text(50, y, f"{label}: {value}", 'F4', 9)
    y -= 13
y -= 15
pdf.add_text(40, y, "HEART RATE (resting):", 'F2', 10)
y -= 14
pdf.add_text(50, y, "Normal adult: 60-100 bpm", 'F4', 9)
y -= 12
pdf.add_text(50, y, "Athletic: 40-60 bpm", 'F4', 9)
y -= 12
pdf.add_text(50, y, "Concerning: consistently above 100 bpm at rest", 'F4', 9)
y -= 20
pdf.add_text(40, y, "RISK FACTORS I HAVE (check all that apply):", 'F2', 9)
y -= 14
risks = ["Family history of heart disease", "High blood pressure", "Diabetes",
    "Smoker/former smoker", "Overweight/obese", "Sedentary lifestyle",
    "High stress", "Age (men 45+, women 55+)", "Poor diet"]
for risk in risks:
    pdf.add_rect(50, y - 2, 8, 8, 0.4)
    pdf.add_text(62, y, risk, 'F4', 8)
    y -= 12

# Page 5: My Health Profile
pdf.new_page()
pdf.add_centered_text(610, "MY HEALTH PROFILE", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
profile = [
    "Name: ___________________________________  DOB: ___/___/___",
    "Height: ________  Weight: ________  BMI: ________",
    "",
    "CURRENT NUMBERS (most recent lab work):",
    "Date tested: ___/___/___",
    "Total Cholesterol: ________ mg/dL",
    "HDL: ________ mg/dL",
    "LDL: ________ mg/dL",
    "Triglycerides: ________ mg/dL",
    "TC/HDL Ratio: ________",
    "Blood Pressure: ________/________ mmHg",
    "Resting Heart Rate: ________ bpm",
    "Blood Sugar (fasting): ________ mg/dL",
    "A1C: ________%",
    "",
    "CURRENT MEDICATIONS:",
    "1. _________________ Dose: _______ Time: _______",
    "2. _________________ Dose: _______ Time: _______",
    "3. _________________ Dose: _______ Time: _______",
    "4. _________________ Dose: _______ Time: _______",
    "",
    "MY DOCTOR:",
    "Name: ___________________________________",
    "Phone: ___________________________________",
    "Next appointment: ___/___/___",
    "",
    "MY GOALS:",
    "Target LDL: ________  Target HDL: ________",
    "Target BP: ________/________  Target weight: ________"
]
for line in profile:
    pdf.add_text(40, y, line, 'F4', 9)
    y -= 14

# Pages 6-17: 12 Monthly Tracking Pages
for month in range(1, 13):
    pdf.new_page()
    pdf.add_centered_text(610, f"MONTHLY TRACKING - MONTH {month}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    pdf.add_text(40, y, f"Month: _____________  Year: ________", 'F1', 9)
    y -= 18
    pdf.add_text(40, y, "LAB RESULTS (if tested this month):", 'F2', 9)
    y -= 14
    pdf.add_text(45, y, "Date tested: ___/___/___", 'F1', 8)
    y -= 12
    lab_items = [
        "Total Cholesterol: ________ mg/dL  (Goal: < 200)",
        "HDL: ________ mg/dL  (Goal: > 60)",
        "LDL: ________ mg/dL  (Goal: < 100)",
        "Triglycerides: ________ mg/dL  (Goal: < 150)",
        "TC/HDL Ratio: ________  (Goal: < 4.5)",
    ]
    for item in lab_items:
        pdf.add_text(50, y, item, 'F1', 8)
        y -= 12
    y -= 8
    pdf.add_text(40, y, "BLOOD PRESSURE LOG:", 'F2', 9)
    y -= 14
    pdf.add_filled_rect(40, y - 3, 352, 12, 0.9)
    pdf.add_text(45, y, "Date", 'F2', 7)
    pdf.add_text(90, y, "AM Reading", 'F2', 7)
    pdf.add_text(175, y, "PM Reading", 'F2', 7)
    pdf.add_text(260, y, "Heart Rate", 'F2', 7)
    pdf.add_text(330, y, "Notes", 'F2', 7)
    y -= 13
    for _ in range(8):
        pdf.add_text(45, y, "___/___", 'F3', 7)
        pdf.add_text(95, y, "___/___", 'F3', 7)
        pdf.add_text(180, y, "___/___", 'F3', 7)
        pdf.add_text(268, y, "___bpm", 'F3', 7)
        pdf.add_line(325, y - 1, 390, y - 1, 0.2, 0.6)
        y -= 11
    y -= 8
    pdf.add_text(40, y, "WEIGHT: Start ______ End ______ Change ______", 'F1', 8)
    y -= 14
    pdf.add_text(40, y, "NOTES (symptoms, changes, concerns):", 'F2', 8)
    y -= 12
    pdf.add_line(40, y, 392, y, 0.3, 0.5)
    y -= 12
    pdf.add_line(40, y, 392, y, 0.3, 0.5)

# Page 18: Medication Log
pdf.new_page()
pdf.add_centered_text(610, "MEDICATION LOG", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Track medication changes, side effects, and effectiveness:", 'F4', 9)
y -= 18
for med in range(5):
    pdf.add_filled_rect(40, y - 3, 352, 90, 0.95)
    pdf.add_rect(40, y - 3, 352, 90, 0.5, 0.5)
    pdf.add_text(45, y + 72, f"Medication {med+1}: _______________________", 'F2', 8)
    pdf.add_text(45, y + 58, "Dose: ________  Frequency: ________  Started: ___/___/___", 'F1', 8)
    pdf.add_text(45, y + 44, "Purpose: _______________________________________________", 'F1', 8)
    pdf.add_text(45, y + 30, "Side effects: __________________________________________", 'F1', 8)
    pdf.add_text(45, y + 16, "Effectiveness (1-10): ___  Doctor notes: ________________", 'F1', 8)
    pdf.add_text(45, y + 2, "Discontinued? [ ] Yes  Date: ___/___  Reason: ____________", 'F1', 8)
    y -= 105

# Pages 19-21: Exercise Tracker (12 weeks over 3 pages)
for ex_page in range(3):
    pdf.new_page()
    start_week = ex_page * 4 + 1
    end_week = start_week + 3
    pdf.add_centered_text(610, f"EXERCISE TRACKER - WEEKS {start_week}-{end_week}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    pdf.add_text(40, y, "Goal: 150+ min moderate exercise per week for heart health", 'F4', 8)
    y -= 16
    for w in range(4):
        week_num = start_week + w
        pdf.add_filled_rect(40, y - 3, 352, 14, 0.9)
        pdf.add_text(45, y, f"WEEK {week_num}", 'F2', 8)
        y -= 16
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in days:
            pdf.add_text(45, y, f"{day}:", 'F2', 7)
            pdf.add_text(70, y, "Activity: ___________", 'F1', 7)
            pdf.add_text(185, y, "Duration: ___ min", 'F1', 7)
            pdf.add_text(290, y, "HR: ___bpm", 'F1', 7)
            y -= 10
        pdf.add_text(45, y, f"TOTAL MINUTES: _______  Goal met? Y/N", 'F2', 7)
        y -= 16

# Pages 22-25: Heart-Healthy Food Diary (4 pages)
for food_page in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(610, f"HEART-HEALTHY FOOD DIARY - PAGE {food_page}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    for day in range(3):
        day_num = (food_page - 1) * 3 + day + 1
        pdf.add_filled_rect(40, y - 3, 352, 14, 0.9)
        pdf.add_text(45, y, f"DAY {day_num}  Date: ___/___/___", 'F2', 8)
        y -= 16
        meals = ["Breakfast:", "Lunch:", "Dinner:", "Snacks:"]
        for meal in meals:
            pdf.add_text(45, y, meal, 'F2', 7)
            pdf.add_line(95, y - 1, 392, y - 1, 0.2, 0.6)
            y -= 11
        pdf.add_text(45, y, "Water (8oz glasses): O O O O O O O O", 'F1', 7)
        y -= 11
        pdf.add_text(45, y, "Fruits/Veggies servings: ___  Fiber: ___g  Sodium: ___mg", 'F1', 7)
        y -= 11
        pdf.add_text(45, y, "Heart-healthy?  [ ] Yes  [ ] Mostly  [ ] Need improvement", 'F1', 7)
        y -= 16

# Page 26: Doctor Appointment Prep
pdf.new_page()
pdf.add_centered_text(610, "DOCTOR APPOINTMENT PREP", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
prep = [
    "Appointment Date: ___/___/___  Time: _______",
    "Doctor: ___________________________________",
    "Purpose: ___________________________________",
    "",
    "BRING TO APPOINTMENT:",
    "[ ] This tracking book",
    "[ ] Current medication list",
    "[ ] Insurance card",
    "[ ] List of symptoms or concerns",
    "[ ] Recent lab results (if from another provider)",
    "",
    "MY CURRENT NUMBERS TO DISCUSS:",
    "Last cholesterol: TC____ HDL____ LDL____ Trig____",
    "Last BP average: ________/________",
    "Current weight: ________",
    "",
    "SYMPTOMS OR CONCERNS TO MENTION:",
    "1. ________________________________________________________",
    "2. ________________________________________________________",
    "3. ________________________________________________________",
    "",
    "QUESTIONS FOR MY DOCTOR:",
    "1. ________________________________________________________",
    "2. ________________________________________________________",
    "3. ________________________________________________________",
    "4. ________________________________________________________",
    "5. ________________________________________________________",
    "",
    "DOCTOR'S RECOMMENDATIONS:",
    "________________________________________________________",
    "________________________________________________________",
    "Next labs needed: ___/___/___",
    "Next appointment: ___/___/___"
]
for line in prep:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 27: Questions for My Cardiologist
pdf.new_page()
pdf.add_centered_text(610, "QUESTIONS FOR MY CARDIOLOGIST", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
questions = [
    "Use this page to keep track of questions between appointments.",
    "Write them down as you think of them so you do not forget!",
    "",
    "ABOUT MY CHOLESTEROL:",
    "Q: ________________________________________________________",
    "A: ________________________________________________________",
    "Q: ________________________________________________________",
    "A: ________________________________________________________",
    "",
    "ABOUT MY MEDICATIONS:",
    "Q: ________________________________________________________",
    "A: ________________________________________________________",
    "Q: ________________________________________________________",
    "A: ________________________________________________________",
    "",
    "ABOUT MY LIFESTYLE:",
    "Q: ________________________________________________________",
    "A: ________________________________________________________",
    "Q: ________________________________________________________",
    "A: ________________________________________________________",
    "",
    "ABOUT MY RISK LEVEL:",
    "Q: ________________________________________________________",
    "A: ________________________________________________________",
    "",
    "ABOUT PROCEDURES/TESTS:",
    "Q: ________________________________________________________",
    "A: ________________________________________________________",
    "",
    "OTHER QUESTIONS:",
    "Q: ________________________________________________________",
    "A: ________________________________________________________"
]
for line in questions:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 28: Emergency Information
pdf.new_page()
pdf.add_centered_text(610, "EMERGENCY INFORMATION", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
emergency = [
    "CALL 911 IMMEDIATELY IF YOU EXPERIENCE:",
    "- Chest pain or pressure lasting more than a few minutes",
    "- Pain spreading to shoulder, arm, back, neck, or jaw",
    "- Shortness of breath with or without chest pain",
    "- Cold sweat, nausea, or lightheadedness",
    "- Sudden numbness/weakness (especially on one side)",
    "- Sudden confusion or trouble speaking",
    "- Sudden severe headache with no known cause",
    "",
    "MY EMERGENCY CONTACTS:",
    "1. Name: _________________ Phone: _________________",
    "   Relationship: _________________",
    "2. Name: _________________ Phone: _________________",
    "   Relationship: _________________",
    "",
    "MY DOCTORS:",
    "Primary Care: _________________ Phone: _________________",
    "Cardiologist: _________________ Phone: _________________",
    "Nearest ER: _________________ Address: _________________",
    "",
    "MY MEDICATIONS (for paramedics):",
    "1. _________________ Dose: _________________",
    "2. _________________ Dose: _________________",
    "3. _________________ Dose: _________________",
    "4. _________________ Dose: _________________",
    "",
    "ALLERGIES: _____________________________________________",
    "BLOOD TYPE: _______  PACEMAKER/DEVICE: [ ] Yes [ ] No",
    "",
    "INSURANCE: _________________ Member #: _________________"
]
for line in emergency:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 29: My Heart Health Goals
pdf.new_page()
pdf.add_centered_text(610, "MY HEART HEALTH GOALS", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
goals = [
    "Setting clear goals helps you stay motivated. Be specific!",
    "",
    "3-MONTH GOALS:",
    "Cholesterol goal: ___________________________________________",
    "Blood pressure goal: ________________________________________",
    "Exercise goal: ______________________________________________",
    "Diet goal: _________________________________________________",
    "Weight goal: _______________________________________________",
    "",
    "6-MONTH GOALS:",
    "Cholesterol goal: ___________________________________________",
    "Blood pressure goal: ________________________________________",
    "Exercise goal: ______________________________________________",
    "Diet goal: _________________________________________________",
    "Weight goal: _______________________________________________",
    "",
    "1-YEAR GOALS:",
    "Cholesterol goal: ___________________________________________",
    "Blood pressure goal: ________________________________________",
    "Exercise goal: ______________________________________________",
    "Diet goal: _________________________________________________",
    "Weight goal: _______________________________________________",
    "",
    "MY MOTIVATION (why I want to be heart-healthy):",
    "___________________________________________________________",
    "___________________________________________________________",
    "",
    "MY REWARD FOR REACHING 3-MONTH GOAL: ________________________",
    "MY REWARD FOR REACHING 6-MONTH GOAL: ________________________",
    "MY REWARD FOR REACHING 1-YEAR GOAL: _________________________"
]
for line in goals:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book130_Cholesterol_Health_Tracker.pdf')
print("Book130_Cholesterol_Health_Tracker.pdf created successfully!")
