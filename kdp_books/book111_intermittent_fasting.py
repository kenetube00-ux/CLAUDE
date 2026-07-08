from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(480, "INTERMITTENT FASTING", 'F2', 16)
pdf.add_centered_text(458, "TRACKER & JOURNAL", 'F2', 16)
pdf.add_centered_text(425, "90 Days to a Healthier You", 'F4', 13)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(500, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)
pdf.add_centered_text(475, "Consult your doctor before starting any fasting program.", 'F4', 9)

# Page 3: IF Methods Explained
pdf.new_page()
pdf.add_centered_text(610, "IF METHODS EXPLAINED", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "WHAT IS INTERMITTENT FASTING?",
    "An eating pattern that cycles between fasting and eating windows.",
    "It's about WHEN you eat, not necessarily WHAT you eat.", "",
    "POPULAR METHODS:", "",
    "16:8 METHOD (most popular for beginners)",
    "Fast 16 hours, eat within 8-hour window",
    "Example: Eat 12pm-8pm, fast 8pm-12pm", "",
    "18:6 METHOD (intermediate)",
    "Fast 18 hours, eat within 6-hour window",
    "Example: Eat 1pm-7pm, fast 7pm-1pm", "",
    "20:4 METHOD (advanced)",
    "Fast 20 hours, eat within 4-hour window",
    "Example: Eat 3pm-7pm, fast 7pm-3pm", "",
    "OMAD - One Meal A Day (advanced)",
    "Eat one large meal, fast the remaining 23 hours", "",
    "START WITH 16:8 and work up as your body adapts.",
    "Most people see results with 16:8 alone."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 4: Getting Started Guide
pdf.new_page()
pdf.add_centered_text(610, "GETTING STARTED GUIDE", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "WEEK 1: Ease into it",
    "- Start by pushing breakfast 1-2 hours later each day",
    "- Stop eating 2-3 hours before bed",
    "- Drink water, black coffee, or plain tea during fasting", "",
    "WEEK 2: Find your window",
    "- Settle into your chosen eating window",
    "- Notice energy patterns and adjust timing",
    "- Eat nutritious meals (don't binge during eating window)", "",
    "DURING FASTING, YOU CAN HAVE:",
    "- Water (add lemon/electrolytes if needed)",
    "- Black coffee (no cream, sugar, or sweetener)",
    "- Plain tea (green, herbal, black)",
    "- Sparkling water", "",
    "DURING EATING WINDOW, FOCUS ON:",
    "- Protein at every meal",
    "- Vegetables and fiber",
    "- Healthy fats",
    "- Adequate calories (don't under-eat!)", "",
    "STOP FASTING IF: you feel dizzy, faint, nauseous beyond the",
    "first week of adjustment, or have a medical condition."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 5: My Chosen Method
pdf.new_page()
pdf.add_centered_text(610, "MY IF PLAN", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "My chosen method: ____________________________",
    "Fasting window: From ___:___ to ___:___",
    "Eating window: From ___:___ to ___:___",
    "Start date: ___/___/___", "",
    "My goals for these 90 days:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________", "",
    "Starting measurements:",
    "Weight: _______ Waist: _______ Hips: _______",
    "Energy level (1-10): _____",
    "Sleep quality (1-10): _____", "",
    "30-day check-in measurements:",
    "Weight: _______ Waist: _______ Hips: _______", "",
    "60-day check-in measurements:",
    "Weight: _______ Waist: _______ Hips: _______", "",
    "90-day FINAL measurements:",
    "Weight: _______ Waist: _______ Hips: _______"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16


# Pages 6-30: Daily Tracking (25 pages with 3-4 days per page)
for page in range(25):
    pdf.new_page()
    start_day = page * 4 + 1
    end_day = min(start_day + 3, 91)
    pdf.add_centered_text(618, f"DAYS {start_day}-{end_day}", 'F2', 12)
    pdf.add_line(50, 608, 382, 608)
    y = 592
    for day_offset in range(min(4, 91 - start_day + 1)):
        day_num = start_day + day_offset
        if day_num > 90:
            break
        pdf.add_text(50, y, f"DAY {day_num}  Date: ___/___", 'F2', 9)
        y -= 13
        pdf.add_text(50, y, "Fast start: ___:___ Fast end: ___:___  Total: ___hrs", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Meals: ________________________________________", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Water (oz): ___ Energy(1-5): ___ Hunger(1-5): ___", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Weight: _______ Notes: ________________________", 'F3', 8)
        y -= 16
        pdf.add_line(50, y+5, 382, y+5, 0.3, 0.7)
        y -= 8

# Final pages: FAQ + Meal Ideas
pdf.new_page()
pdf.add_centered_text(610, "MEAL IDEAS & FAQ", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "BREAKING YOUR FAST - GOOD FIRST MEALS:",
    "- Eggs + avocado + veggies",
    "- Greek yogurt + nuts + berries",
    "- Bone broth + chicken + rice",
    "- Smoothie with protein powder + greens", "",
    "COMMON QUESTIONS:", "",
    "Q: Won't I lose muscle?",
    "A: No, if you eat adequate protein (0.7-1g per lb bodyweight)", "",
    "Q: Can I exercise while fasting?",
    "A: Yes! Many people train fasted. Listen to your body.", "",
    "Q: What if I'm hungry?",
    "A: Hunger comes in waves. Drink water. It passes in 15-20 min.", "",
    "Q: Can I do IF every day?",
    "A: Most people do. Some prefer 5 days on, 2 off.", "",
    "Q: Will it slow my metabolism?",
    "A: No. Short-term fasting can actually increase metabolic rate."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book111_Intermittent_Fasting_Tracker.pdf')
print("Book111_Intermittent_Fasting_Tracker.pdf created successfully!")
