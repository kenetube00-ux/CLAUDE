from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1: Title Page
pdf.new_page()
pdf.add_filled_rect(0, 0, 432, 648, gray=0.95)
pdf.add_centered_text(440, "GESTATIONAL", "F2", 22)
pdf.add_centered_text(410, "DIABETES TRACKER", "F2", 22)
pdf.add_line(120, 395, 312, 395, 2, gray=0.5)
pdf.add_centered_text(360, "Blood Sugar, Meals &", "F4", 14, gray=0.3)
pdf.add_centered_text(340, "Baby Health Log", "F4", 14, gray=0.3)
pdf.add_centered_text(290, "Daily Monitoring for a Healthy Pregnancy", "F1", 11, gray=0.4)
pdf.add_centered_text(180, author, "F2", 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(420, "GESTATIONAL DIABETES TRACKER", "F2", 12)
pdf.add_centered_text(402, "Blood Sugar, Meals & Baby Health Log", "F4", 10)
pdf.add_centered_text(370, f"Copyright (c) 2025 {author}", "F1", 10)
pdf.add_centered_text(352, "All rights reserved.", "F1", 10)
pdf.add_centered_text(320, "MEDICAL DISCLAIMER: This tracker is for personal record-keeping.", "F1", 9)
pdf.add_centered_text(305, "It does not replace medical advice. Always follow your", "F1", 9)
pdf.add_centered_text(290, "healthcare provider's recommendations.", "F1", 9)
pdf.add_centered_text(260, "ISBN: 979-8-XXX-XXXXX-X", "F3", 9)

# Page 3: Understanding Gestational Diabetes
pdf.new_page()
pdf.add_centered_text(610, "UNDERSTANDING GESTATIONAL DIABETES", "F2", 14)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Gestational diabetes (GDM) is high blood sugar that", "F1", 11)
pdf.add_text(40, 555, "develops during pregnancy. It affects 2-10% of pregnancies.", "F1", 11)
pdf.add_text(40, 525, "Key Facts:", "F2", 11)
pdf.add_text(50, 503, "- Usually develops around weeks 24-28", "F1", 10)
pdf.add_text(50, 485, "- Usually goes away after delivery", "F1", 10)
pdf.add_text(50, 467, "- Can be managed with diet, exercise, and sometimes insulin", "F1", 10)
pdf.add_text(50, 449, "- Monitoring blood sugar is essential", "F1", 10)
pdf.add_text(50, 431, "- You did NOT cause this - hormones from the placenta block insulin", "F1", 10)
pdf.add_text(40, 400, "Why Tracking Matters:", "F2", 11)
pdf.add_text(50, 378, "- Helps you see patterns in your blood sugar", "F1", 10)
pdf.add_text(50, 360, "- Identifies foods that spike your levels", "F1", 10)
pdf.add_text(50, 342, "- Provides data for your care team", "F1", 10)
pdf.add_text(50, 324, "- Gives you a sense of control", "F1", 10)
pdf.add_text(50, 306, "- Helps ensure healthy outcomes for you and baby", "F1", 10)
pdf.add_text(40, 270, "My diagnosis date: ___/___/___", "F1", 11)
pdf.add_text(40, 248, "Weeks pregnant at diagnosis: ___", "F1", 11)
pdf.add_text(40, 226, "Due date: ___/___/___", "F1", 11)


# Page 4: Target Blood Sugar Ranges
pdf.new_page()
pdf.add_centered_text(610, "TARGET BLOOD SUGAR RANGES", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "These are GENERAL targets. Your doctor may adjust yours.", "F1", 11)
pdf.add_filled_rect(40, 535, 352, 25, gray=0.88)
pdf.add_text(45, 545, "TIMING", "F2", 10)
pdf.add_text(200, 545, "TARGET (mg/dL)", "F2", 10)
pdf.add_text(45, 515, "Fasting (before breakfast)", "F1", 10)
pdf.add_text(200, 515, "95 or below", "F1", 10)
pdf.add_text(45, 495, "1 hour after meals", "F1", 10)
pdf.add_text(200, 495, "140 or below", "F1", 10)
pdf.add_text(45, 475, "2 hours after meals", "F1", 10)
pdf.add_text(200, 475, "120 or below", "F1", 10)
pdf.add_text(45, 455, "Bedtime", "F1", 10)
pdf.add_text(200, 455, "Ask your doctor", "F1", 10)
pdf.add_line(40, 440, 392, 440, 0.5)
pdf.add_text(40, 415, "MY Personal Targets (from my doctor):", "F2", 11)
pdf.add_text(50, 393, "Fasting: ___ mg/dL", "F1", 10)
pdf.add_text(50, 373, "1hr after meals: ___ mg/dL", "F1", 10)
pdf.add_text(50, 353, "2hr after meals: ___ mg/dL", "F1", 10)
pdf.add_text(50, 333, "Bedtime: ___ mg/dL", "F1", 10)
pdf.add_text(40, 300, "When to call your doctor:", "F2", 11)
pdf.add_text(50, 278, "- Fasting BG consistently above ___", "F1", 10)
pdf.add_text(50, 258, "- Any reading above ___", "F1", 10)
pdf.add_text(50, 238, "- Feeling very thirsty/urinating a lot", "F1", 10)
pdf.add_text(50, 218, "- Decreased baby movement", "F1", 10)
pdf.add_text(50, 198, "- Blurred vision or headaches", "F1", 10)

# Page 5: My Care Team
pdf.new_page()
pdf.add_centered_text(610, "MY CARE TEAM", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Keep all your contacts in one place:", "F1", 11)
team_members = [
    ("OB/GYN:", "Phone:"),
    ("Endocrinologist:", "Phone:"),
    ("Diabetes Educator:", "Phone:"),
    ("Dietitian/Nutritionist:", "Phone:"),
    ("Midwife:", "Phone:"),
    ("Pharmacy:", "Phone:"),
    ("Hospital L&D:", "Phone:"),
    ("Emergency Contact:", "Phone:")
]
y = 545
for name, phone in team_members:
    pdf.add_text(40, y, name, "F2", 10)
    pdf.add_line(40, y - 15, 250, y - 15, 0.5)
    pdf.add_text(260, y, phone, "F1", 9)
    pdf.add_line(295, y - 15, 392, y - 15, 0.5)
    y -= 40
pdf.add_text(40, y, "Next appointment: ___/___/___ with _______________", "F1", 10)
pdf.add_text(40, y - 20, "Questions for next visit:", "F2", 10)
pdf.add_line(40, y - 38, 392, y - 38, 0.5)
pdf.add_line(40, y - 56, 392, y - 56, 0.5)


# Pages 6-20: Daily Entries (2 per page, 30 entries = 15 pages)
for page_num in range(15):
    pdf.new_page()
    entry_start = page_num * 2 + 1
    pdf.add_centered_text(618, f"DAILY BLOOD SUGAR & MEAL LOG", "F2", 12)
    pdf.add_text(320, 618, f"Entries {entry_start}-{entry_start+1}", "F1", 8)
    pdf.add_line(40, 607, 392, 607, 1, gray=0.7)
    
    for entry in range(2):
        base_y = 590 - entry * 290
        pdf.add_filled_rect(40, base_y - 3, 352, 15, gray=0.85)
        pdf.add_text(42, base_y, f"DAY {entry_start + entry}", "F2", 8)
        pdf.add_text(100, base_y, "Date: ___/___/___", "F1", 8)
        pdf.add_text(210, base_y, "Week: ___", "F1", 8)
        pdf.add_text(280, base_y, "Weight: ___", "F1", 8)
        
        y = base_y - 20
        pdf.add_text(42, y, "BLOOD SUGAR:", "F2", 8)
        y -= 14
        pdf.add_text(42, y, "Fasting: ___ mg/dL", "F1", 8)
        pdf.add_text(160, y, "After B: ___ mg/dL", "F1", 8)
        pdf.add_text(290, y, "After L: ___ mg/dL", "F1", 8)
        y -= 14
        pdf.add_text(42, y, "After D: ___ mg/dL", "F1", 8)
        pdf.add_text(160, y, "Bedtime: ___ mg/dL", "F1", 8)
        
        y -= 18
        pdf.add_text(42, y, "MEALS:", "F2", 8)
        y -= 13
        pdf.add_text(42, y, "B:", "F2", 7)
        pdf.add_line(55, y, 250, y, 0.3)
        pdf.add_text(255, y, "Carbs: ___g", "F1", 7)
        y -= 13
        pdf.add_text(42, y, "L:", "F2", 7)
        pdf.add_line(55, y, 250, y, 0.3)
        pdf.add_text(255, y, "Carbs: ___g", "F1", 7)
        y -= 13
        pdf.add_text(42, y, "D:", "F2", 7)
        pdf.add_line(55, y, 250, y, 0.3)
        pdf.add_text(255, y, "Carbs: ___g", "F1", 7)
        y -= 13
        pdf.add_text(42, y, "Snacks:", "F1", 7)
        pdf.add_line(80, y, 250, y, 0.3)
        pdf.add_text(255, y, "Carbs: ___g", "F1", 7)
        
        y -= 17
        pdf.add_text(42, y, "Insulin: Y/N  Dose: ___", "F1", 8)
        pdf.add_text(200, y, "Exercise: _______________", "F1", 8)
        y -= 14
        pdf.add_text(42, y, "Baby movement (kicks): ___", "F1", 8)
        pdf.add_text(200, y, "Notes:", "F1", 8)
        pdf.add_line(240, y, 392, y, 0.3)


# Page 21: Weekly Average Calculator
pdf.new_page()
pdf.add_centered_text(610, "WEEKLY AVERAGE CALCULATOR", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Calculate your weekly averages to share with your doctor:", "F1", 11)
y = 545
for week in range(6):
    pdf.add_filled_rect(40, y - 3, 352, 15, gray=0.92)
    pdf.add_text(42, y, f"WEEK ___", "F2", 9)
    pdf.add_text(120, y, "Dates: ___/___ to ___/___", "F1", 8)
    y -= 18
    pdf.add_text(42, y, "Avg Fasting: ___", "F1", 8)
    pdf.add_text(150, y, "Avg After Meals: ___", "F1", 8)
    pdf.add_text(290, y, "In range: ___/7 days", "F1", 8)
    y -= 15
    pdf.add_text(42, y, "Trend: Better / Same / Worse", "F1", 8)
    pdf.add_text(220, y, "Notes: _______________", "F1", 8)
    y -= 25

pdf.add_text(40, y - 10, "Overall pattern I notice:", "F2", 10)
pdf.add_line(40, y - 28, 392, y - 28, 0.5)
pdf.add_line(40, y - 46, 392, y - 46, 0.5)

# Pages 22-24: Doctor Appointment Prep (3 pages)
for appt in range(3):
    pdf.new_page()
    pdf.add_centered_text(610, f"DOCTOR APPOINTMENT PREP ({appt+1})", "F2", 16)
    pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
    pdf.add_text(40, 572, f"Appointment Date: ___/___/___", "F1", 11)
    pdf.add_text(40, 552, "Doctor: _______________", "F1", 11)
    pdf.add_text(40, 532, "Current week of pregnancy: ___", "F1", 11)
    pdf.add_text(40, 505, "Blood sugar summary this period:", "F2", 11)
    pdf.add_text(50, 483, "Fasting average: ___ mg/dL", "F1", 10)
    pdf.add_text(50, 463, "Post-meal average: ___ mg/dL", "F1", 10)
    pdf.add_text(50, 443, "Number of highs: ___", "F1", 10)
    pdf.add_text(50, 423, "Number of lows: ___", "F1", 10)
    pdf.add_text(40, 395, "Questions I want to ask:", "F2", 11)
    for i in range(4):
        pdf.add_text(50, 373 - i*22, f"{i+1}.", "F1", 10)
        pdf.add_line(60, 373 - i*22, 392, 373 - i*22, 0.5)
    pdf.add_text(40, 280, "Concerns/Symptoms to discuss:", "F2", 11)
    pdf.add_line(40, 260, 392, 260, 0.5)
    pdf.add_line(40, 240, 392, 240, 0.5)
    pdf.add_text(40, 215, "Doctor's recommendations:", "F2", 11)
    pdf.add_line(40, 195, 392, 195, 0.5)
    pdf.add_line(40, 175, 392, 175, 0.5)
    pdf.add_line(40, 155, 392, 155, 0.5)
    pdf.add_text(40, 130, "Next appointment: ___/___/___", "F1", 10)


# Page 25: Meal Ideas
pdf.new_page()
pdf.add_centered_text(610, "GDM-FRIENDLY MEAL IDEAS", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Focus on: protein + healthy fat + fiber + controlled carbs", "F1", 11)
pdf.add_filled_rect(40, 545, 352, 18, gray=0.88)
pdf.add_text(45, 549, "BREAKFAST IDEAS", "F2", 10)
breakfasts = [
    "Eggs + avocado + whole grain toast (1 slice)",
    "Greek yogurt + berries + nuts",
    "Oatmeal (1/2 cup) + peanut butter + seeds",
    "Veggie omelet + small fruit"
]
y = 525
for b in breakfasts:
    pdf.add_text(50, y, f"- {b}", "F1", 9)
    y -= 16
pdf.add_filled_rect(40, y - 5, 352, 18, gray=0.88)
pdf.add_text(45, y, "LUNCH IDEAS", "F2", 10)
y -= 20
lunches = [
    "Grilled chicken salad + quinoa + olive oil dressing",
    "Turkey + cheese wrap (whole wheat) + veggies",
    "Lentil soup + side salad",
    "Tuna + avocado + crackers (whole grain)"
]
for l in lunches:
    pdf.add_text(50, y, f"- {l}", "F1", 9)
    y -= 16
pdf.add_filled_rect(40, y - 5, 352, 18, gray=0.88)
pdf.add_text(45, y, "DINNER IDEAS", "F2", 10)
y -= 20
dinners = [
    "Salmon + roasted vegetables + brown rice (1/2 cup)",
    "Stir-fry with chicken + vegetables + cauliflower rice",
    "Lean beef + sweet potato + steamed broccoli",
    "Baked chicken + green beans + small roll"
]
for d in dinners:
    pdf.add_text(50, y, f"- {d}", "F1", 9)
    y -= 16
pdf.add_filled_rect(40, y - 5, 352, 18, gray=0.88)
pdf.add_text(45, y, "SNACK IDEAS (15-20g carbs)", "F2", 10)
y -= 20
snacks = [
    "Apple slices + almond butter",
    "Cheese + whole grain crackers",
    "Hard-boiled egg + veggies",
    "Small handful of nuts + berries"
]
for s in snacks:
    pdf.add_text(50, y, f"- {s}", "F1", 9)
    y -= 16
pdf.add_text(40, y - 10, "Foods that spike MY blood sugar:", "F2", 10)
pdf.add_line(40, y - 28, 392, y - 28, 0.5)

# Page 26: Post-Delivery Monitoring
pdf.new_page()
pdf.add_centered_text(610, "POST-DELIVERY MONITORING", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "What to expect after your baby arrives:", "F1", 11)
pdf.add_text(40, 545, "Immediately after delivery:", "F2", 11)
pdf.add_text(50, 525, "- Blood sugar usually returns to normal", "F1", 10)
pdf.add_text(50, 507, "- You'll be tested 24-72 hours after delivery", "F1", 10)
pdf.add_text(50, 489, "- Breastfeeding can help stabilize blood sugar", "F1", 10)
pdf.add_text(40, 460, "Follow-up testing:", "F2", 11)
pdf.add_text(50, 440, "- 6-12 week postpartum glucose test", "F1", 10)
pdf.add_text(50, 422, "- Annual diabetes screening recommended", "F1", 10)
pdf.add_text(50, 404, "- Higher risk for Type 2 diabetes later in life", "F1", 10)
pdf.add_text(40, 375, "My post-delivery plan:", "F2", 11)
pdf.add_text(50, 355, "6-week test date: ___/___/___", "F1", 10)
pdf.add_text(50, 335, "Result: _______________", "F1", 10)
pdf.add_text(50, 315, "Follow-up with: _______________", "F1", 10)
pdf.add_text(40, 285, "Lifestyle changes I want to maintain:", "F2", 11)
pdf.add_line(40, 265, 392, 265, 0.5)
pdf.add_line(40, 245, 392, 245, 0.5)
pdf.add_line(40, 225, 392, 225, 0.5)
pdf.add_text(40, 195, "Baby's birth date: ___/___/___", "F1", 11)
pdf.add_text(40, 175, "Baby's weight: ___ lbs ___ oz", "F1", 11)
pdf.add_text(40, 155, "Any complications: _______________", "F1", 11)


# Page 27: Emotional Support
pdf.new_page()
pdf.add_centered_text(610, "EMOTIONAL SUPPORT", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "A GDM diagnosis can bring up many emotions.", "F1", 11)
pdf.add_text(40, 552, "All your feelings are valid.", "F4", 11, gray=0.3)
pdf.add_text(40, 522, "How I felt when diagnosed:", "F2", 11)
pdf.add_line(40, 502, 392, 502, 0.5)
pdf.add_line(40, 482, 392, 482, 0.5)
pdf.add_text(40, 455, "Things I want to let go of:", "F2", 11)
pdf.add_rect(45, 433, 12, 12)
pdf.add_text(65, 435, "Guilt (this is NOT your fault)", "F1", 10)
pdf.add_rect(45, 413, 12, 12)
pdf.add_text(65, 415, "Fear about baby's health", "F1", 10)
pdf.add_rect(45, 393, 12, 12)
pdf.add_text(65, 395, "Frustration with food restrictions", "F1", 10)
pdf.add_rect(45, 373, 12, 12)
pdf.add_text(65, 375, "Overwhelm from monitoring", "F1", 10)
pdf.add_rect(45, 353, 12, 12)
pdf.add_text(65, 355, "Shame or embarrassment", "F1", 10)
pdf.add_text(40, 325, "Positive reminders:", "F2", 11)
pdf.add_text(50, 303, "- GDM is temporary and manageable", "F1", 10)
pdf.add_text(50, 283, "- You are doing an amazing job monitoring", "F1", 10)
pdf.add_text(50, 263, "- Every good choice helps your baby", "F1", 10)
pdf.add_text(50, 243, "- Many women with GDM have healthy babies", "F1", 10)
pdf.add_text(50, 223, "- You are stronger than you think", "F1", 10)
pdf.add_text(40, 193, "A letter to my baby:", "F2", 11)
pdf.add_line(40, 173, 392, 173, 0.5)
pdf.add_line(40, 153, 392, 153, 0.5)
pdf.add_line(40, 133, 392, 133, 0.5)
pdf.add_line(40, 113, 392, 113, 0.5)

# Pages 28-30: Additional tracking pages
# Page 28: Exercise & Movement Log
pdf.new_page()
pdf.add_centered_text(610, "EXERCISE & MOVEMENT LOG", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Exercise helps control blood sugar. Aim for 30 min/day.", "F1", 11)
pdf.add_text(40, 550, "Safe exercises during pregnancy:", "F2", 10)
pdf.add_text(50, 530, "Walking, swimming, prenatal yoga, stationary bike", "F1", 10)
pdf.add_text(40, 505, "My exercise log:", "F2", 11)
y = 480
for i in range(10):
    pdf.add_filled_rect(40, y - 2, 352, 14, gray=0.95 if i % 2 == 0 else 1.0)
    pdf.add_text(42, y, f"Day ___:", "F1", 8)
    pdf.add_text(85, y, "Activity: ___________", "F1", 8)
    pdf.add_text(210, y, "Duration: ___ min", "F1", 8)
    pdf.add_text(310, y, "BG effect: ___", "F1", 8)
    y -= 18
pdf.add_text(40, y - 15, "Best time of day for me to exercise:", "F1", 10)
pdf.add_line(40, y - 33, 300, y - 33, 0.5)
pdf.add_text(40, y - 53, "Activities that lower my blood sugar most:", "F1", 10)
pdf.add_line(40, y - 71, 392, y - 71, 0.5)

# Page 29: Kick Count Tracker
pdf.new_page()
pdf.add_centered_text(610, "BABY KICK COUNT TRACKER", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Track 10 movements in 2 hours, once daily (after 28 weeks).", "F1", 11)
pdf.add_text(40, 552, "If less than 10 in 2 hours, contact your doctor.", "F2", 10)
y = 525
for i in range(14):
    pdf.add_filled_rect(40, y - 2, 352, 14, gray=0.95 if i % 2 == 0 else 1.0)
    pdf.add_text(42, y, "Date: ___/___", "F1", 8)
    pdf.add_text(110, y, "Start time: ___:___", "F1", 8)
    pdf.add_text(215, y, "10 kicks by: ___:___", "F1", 8)
    pdf.add_text(330, y, "Total: ___", "F1", 8)
    y -= 18
pdf.add_text(40, y - 15, "Pattern I notice: ___________________________", "F1", 10)
pdf.add_text(40, y - 35, "Baby is most active:", "F1", 10)
pdf.add_text(50, y - 53, "Morning / Afternoon / Evening / Night", "F1", 10)

# Page 30: Final Page
pdf.new_page()
pdf.add_filled_rect(0, 0, 432, 648, gray=0.95)
pdf.add_centered_text(440, "YOU'VE GOT THIS,", "F2", 20)
pdf.add_centered_text(412, "MAMA.", "F2", 20)
pdf.add_line(140, 395, 292, 395, 2, gray=0.5)
pdf.add_centered_text(360, "Every number you track,", "F4", 12, gray=0.3)
pdf.add_centered_text(340, "every healthy choice you make,", "F4", 12, gray=0.3)
pdf.add_centered_text(320, "is an act of love for your baby.", "F4", 12, gray=0.3)
pdf.add_centered_text(270, "You are not defined by a diagnosis.", "F1", 11, gray=0.4)
pdf.add_centered_text(250, "You are a warrior growing life.", "F1", 11, gray=0.4)
pdf.add_centered_text(190, "Wishing you a healthy, happy delivery!", "F2", 11)
pdf.add_centered_text(150, f"With care, {author}", "F4", 11, gray=0.4)

pdf.save("Book174_Gestational_Diabetes_Log.pdf")
print("SUCCESS: Book174_Gestational_Diabetes_Log.pdf created (30 pages)")
