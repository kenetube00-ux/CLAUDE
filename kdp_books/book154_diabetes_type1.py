"""Book 154: Type 1 Diabetes Daily Log - Blood Sugar, Insulin & Carb Tracker"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "TYPE 1 DIABETES", 'F2', 20, 0)
    doc.add_centered_text(400, "DAILY LOG", 'F2', 20, 0)
    doc.add_centered_text(360, "Blood Sugar, Insulin & Carb Tracker", 'F4', 13, 0.2)
    doc.add_centered_text(300, "90 Daily Entries | Patterns & Insights", 'F1', 11, 0.3)
    doc.add_centered_text(280, "Emergency Plans | Provider Communication", 'F1', 11, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    doc.new_page()
    doc.add_centered_text(500, "TYPE 1 DIABETES DAILY LOG", 'F2', 12, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)
    doc.add_text(50, 410, "Not a substitute for medical advice. Work with your endocrinologist.", 'F1', 9, 0.3)

    # Page 3: My Diabetes Info
    doc.new_page()
    doc.add_centered_text(590, "MY DIABETES INFO", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    fields = [
        "Diagnosis Date: ___________________",
        "Endocrinologist: _______________________  Phone: _______________",
        "Diabetes Educator: ____________________  Phone: _______________",
        "Pharmacy: _____________________________  Phone: _______________",
        "",
        "Insulin Type (Basal): _________________  Dose: ________________",
        "Insulin Type (Bolus): _________________",
        "Carb Ratio: 1 unit per ___ g carbs",
        "Correction Factor: 1 unit drops BG by ___ mg/dL",
        "Target Range: ___ to ___ mg/dL",
        "ISF (Insulin Sensitivity Factor): ___",
        "",
        "A1C History:",
        "  Date: ________  A1C: ___    Date: ________  A1C: ___",
        "  Date: ________  A1C: ___    Date: ________  A1C: ___",
        "",
        "Pump: [ ] Yes Model: _______________  [ ] No (MDI)",
        "CGM: [ ] Yes Model: _______________  [ ] No",
        "",
        "Emergency Contact: _________________  Phone: _________________",
        "Insurance: ___________________________  Member #: _____________"
    ]
    for f in fields:
        if f == "":
            y -= 8
        else:
            doc.add_text(50, y, f, 'F1', 9, 0.2)
            y -= 16

    # Pages 4-33: Daily Entries (30 pages, 3 per page = 90 entries)
    for page_num in range(30):
        doc.new_page()
        doc.add_text(50, 610, f"DAILY LOG - Page {page_num+1}", 'F2', 9, 0.3)
        doc.add_line(50, 604, 382, 604, 0.5, 0.7)
        y = 590
        for entry in range(3):
            day_num = page_num * 3 + entry + 1
            doc.add_filled_rect(50, y+2, 332, 11, 0.9)
            doc.add_text(52, y+3, f"Day {day_num}  Date: ________", 'F2', 7, 0)
            y -= 12
            # Table header
            doc.add_filled_rect(50, y, 332, 10, 0.85)
            doc.add_text(52, y+1, "Time", 'F2', 6, 0)
            doc.add_text(85, y+1, "BG", 'F2', 6, 0)
            doc.add_text(115, y+1, "Carbs(g)", 'F2', 6, 0)
            doc.add_text(165, y+1, "Insulin", 'F2', 6, 0)
            doc.add_text(210, y+1, "Activity", 'F2', 6, 0)
            doc.add_text(275, y+1, "Notes", 'F2', 6, 0)
            y -= 11
            time_slots = ["Fasting", "Brkfst", "Lunch", "Dinner", "Bed"]
            for slot in time_slots:
                doc.add_text(52, y+1, slot, 'F3', 6, 0.3)
                doc.add_rect(83, y-1, 28, 9)
                doc.add_rect(115, y-1, 40, 9)
                doc.add_rect(165, y-1, 38, 9)
                doc.add_rect(210, y-1, 58, 9)
                doc.add_rect(275, y-1, 107, 9)
                y -= 10
            y -= 12

    # Page 34: Hypo & Hyper Action Plans
    doc.new_page()
    doc.add_centered_text(590, "HYPO & HYPER ACTION PLANS", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "HYPOGLYCEMIA (Low - below ___ mg/dL):", 'F2', 10, 0)
    y -= 16
    hypo_steps = ["Check BG to confirm low", "15g fast-acting carbs (juice box, glucose tabs, candy)",
                  "Wait 15 minutes", "Recheck BG", "If still low: repeat 15g carbs",
                  "Once above ___: eat a snack with protein", "If unconscious: Glucagon injection/nasal"]
    for s in hypo_steps:
        doc.add_text(55, y, f"- {s}", 'F1', 8, 0.2)
        y -= 12
    y -= 10
    doc.add_text(50, y, "My 15g carb sources: ______________________________________________", 'F1', 9, 0.2)
    y -= 18
    doc.add_text(50, y, "Glucagon location: ________________________________________________", 'F1', 9, 0.2)
    y -= 22
    doc.add_text(50, y, "HYPERGLYCEMIA (High - above ___ mg/dL):", 'F2', 10, 0)
    y -= 16
    hyper_steps = ["Correction dose per sliding scale: ___",
                   "Check ketones if above 250 mg/dL", "Drink water",
                   "Light activity if ketones negative",
                   "If ketones positive: NO exercise, call endo",
                   "Change pump site if applicable",
                   "Go to ER if: vomiting, ketones high, BG won't come down"]
    for s in hyper_steps:
        doc.add_text(55, y, f"- {s}", 'F1', 8, 0.2)
        y -= 12

    # Page 35: Sick Day Protocol
    doc.new_page()
    doc.add_centered_text(590, "SICK DAY PROTOCOL", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "When sick, blood sugar often runs HIGH even if not eating.", 'F2', 9, 0)
    y -= 18
    rules = ["NEVER stop taking basal insulin (even if not eating)",
             "Check BG every 2-4 hours", "Check ketones every 4 hours if BG > 250",
             "Stay hydrated (water, broth, sugar-free drinks)",
             "Take correction doses as needed",
             "Keep food down: crackers, toast, soup, popsicles",
             "Call endo if: can't keep fluids down, ketones moderate/large, BG > 300 for 4+ hrs"]
    for r in rules:
        doc.add_text(55, y, f"- {r}", 'F1', 8, 0.2)
        y -= 14
    y -= 10
    doc.add_text(50, y, "My endo's after-hours number: _____________________________________", 'F1', 9, 0.2)

    # Page 36: Travel Preparation
    doc.new_page()
    doc.add_centered_text(590, "TRAVEL PREPARATION CHECKLIST", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    travel_items = ["Extra insulin (2x what you need)", "Extra pump supplies (if applicable)",
                    "Syringes as backup (even with pump)", "Glucose tabs/juice boxes",
                    "Glucagon kit", "Meter + extra test strips + extra lancets",
                    "CGM sensors + transmitter backup", "Prescriptions/letter from doctor",
                    "Snacks for lows", "Cooler for insulin (if hot climate)",
                    "Medical ID bracelet/card", "Insurance card + endo number",
                    "Time zone plan (adjust basal/bolus timing)",
                    "Airport: insulin/supplies in carry-on ALWAYS",
                    "TSA notification card"]
    for item in travel_items:
        doc.add_rect(50, y-3, 8, 8)
        doc.add_text(62, y, item, 'F1', 8, 0.2)
        y -= 14

    # Page 37: Monthly A1C Estimation
    doc.new_page()
    doc.add_centered_text(590, "MONTHLY A1C ESTIMATION", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Estimated A1C = (Average BG + 46.7) / 28.7", 'F1', 10, 0.2)
    y = 530
    doc.add_filled_rect(50, y-2, 332, 16, 0.85)
    doc.add_text(52, y, "Month", 'F2', 8, 0)
    doc.add_text(110, y, "Avg BG", 'F2', 8, 0)
    doc.add_text(165, y, "Est A1C", 'F2', 8, 0)
    doc.add_text(220, y, "Time in Range", 'F2', 8, 0)
    doc.add_text(305, y, "Notes", 'F2', 8, 0)
    y -= 18
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for m in months:
        doc.add_text(52, y, m, 'F1', 8, 0.2)
        doc.add_rect(110, y-2, 40, 14)
        doc.add_rect(165, y-2, 40, 14)
        doc.add_rect(220, y-2, 70, 14)
        doc.add_rect(305, y-2, 77, 14)
        y -= 16

    # Page 38: Patterns I'm Noticing
    doc.new_page()
    doc.add_centered_text(590, "PATTERNS I'M NOTICING", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    pattern_qs = [
        "Times of day I tend to go HIGH:",
        "Times of day I tend to go LOW:",
        "Foods that spike me unexpectedly:",
        "Foods that are safe/predictable:",
        "Exercise effect on my BG:",
        "Stress effect on my BG:",
        "Menstrual cycle effect (if applicable):",
        "Sleep effect on morning BG:",
        "Adjustments I want to discuss with my endo:"
    ]
    for q in pattern_qs:
        doc.add_text(50, y, q, 'F2', 9, 0.1)
        y -= 14
        doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
        y -= 20

    # Page 39: Questions for My Endo
    doc.new_page()
    doc.add_centered_text(590, "QUESTIONS FOR MY ENDO", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Write questions as they come up so you don't forget:", 'F1', 10, 0.2)
    y = 530
    for i in range(18):
        doc.add_rect(50, y-3, 8, 8)
        doc.add_text(62, y, "_" * 49, 'F1', 9, 0.4)
        y -= 20

    # Page 40: Emergency Contacts + CGM/Pump Settings
    doc.new_page()
    doc.add_centered_text(590, "EMERGENCY CONTACTS & DEVICE SETTINGS", 'F2', 11, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "EMERGENCY CONTACTS:", 'F2', 10, 0)
    y -= 16
    contacts = ["Endocrinologist:", "Diabetes educator:", "Pharmacy:", "Emergency contact 1:", "Emergency contact 2:"]
    for c in contacts:
        doc.add_text(50, y, f"  {c} ____________________  Phone: ______________", 'F1', 8, 0.3)
        y -= 14
    y -= 12
    doc.add_text(50, y, "CGM/PUMP SETTINGS LOG:", 'F2', 10, 0)
    y -= 16
    settings = ["Basal rates:", "  12am-6am: ___  6am-12pm: ___  12pm-6pm: ___  6pm-12am: ___",
                "Carb ratios:", "  Breakfast: 1:___  Lunch: 1:___  Dinner: 1:___",
                "Correction factor:", "  Day: 1 unit per ___  Night: 1 unit per ___",
                "Active insulin time: ___ hours",
                "CGM alerts: Low ___ mg/dL  High ___ mg/dL",
                "Site rotation: [ ] Abdomen [ ] Arm [ ] Thigh [ ] Buttocks"]
    for s in settings:
        doc.add_text(50, y, s, 'F1', 8, 0.3)
        y -= 13
    y -= 10
    doc.add_text(50, y, "Last site change: ________  Next: ________", 'F1', 8, 0.3)
    y -= 12
    doc.add_text(50, y, "Last sensor change: ________  Next: ________", 'F1', 8, 0.3)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book154_Type1_Diabetes_Log.pdf')
    print("Book154_Type1_Diabetes_Log.pdf created successfully!")

if __name__ == "__main__":
    create_book()
