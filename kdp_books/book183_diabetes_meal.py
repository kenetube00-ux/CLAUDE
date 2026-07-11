#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "DIABETIC MEAL PLANNER", 'F2', 22)
pdf.add_centered_text(480, "Weekly Menus & Carb Counting Made Simple", 'F4', 13)
pdf.add_centered_text(440, f"By {author}", 'F4', 12)
pdf.add_line(150, 420, 462, 420, 2)

# Page 2 - Copyright + Carb Counting Basics
pdf.new_page()
pdf.add_centered_text(500, f"Copyright - {author}", 'F1', 10)
pdf.add_centered_text(480, "All rights reserved. Not medical advice.", 'F1', 10)
pdf.add_centered_text(460, "Consult your healthcare team for personalized guidance.", 'F1', 10)

# Page 3 - Carb Counting Basics
pdf.new_page()
pdf.add_centered_text(740, "UNDERSTANDING CARB COUNTING", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "WHY COUNT CARBS?", 'F2', 12)
pdf.add_text(50, 685, "Carbohydrates have the biggest impact on blood sugar.", 'F1', 11)
pdf.add_text(50, 665, "Counting helps you match insulin/medication to food intake.", 'F1', 11)
pdf.add_text(50, 635, "1 CARB SERVING = 15 grams of carbohydrates", 'F2', 12)
pdf.add_text(50, 610, "COMMON PORTIONS (each = ~15g carbs):", 'F2', 11)
portions = ["1 slice bread", "1/3 cup rice or pasta", "1 small fruit",
            "1/2 cup oatmeal", "3/4 cup dry cereal", "1/2 cup beans",
            "1 small potato", "1 cup milk", "1/2 cup juice"]
y = 590
for p in portions:
    pdf.add_text(70, y, f"- {p}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-10, "MY DAILY CARB TARGET (from my doctor):", 'F2', 11)
pdf.add_text(50, y-28, "Breakfast: _____g   Lunch: _____g   Dinner: _____g   Snacks: _____g", 'F1', 11)
pdf.add_text(50, y-48, "Total daily carbs: _____g", 'F2', 11)

# Page 4 - The Plate Method
pdf.new_page()
pdf.add_centered_text(740, "THE PLATE METHOD", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "A simple way to build balanced meals:", 'F1', 11)
pdf.add_text(50, 680, "Use a 9-inch plate and divide it:", 'F2', 11)
pdf.add_text(70, 655, "1/2 plate = Non-starchy vegetables", 'F1', 11)
pdf.add_text(90, 638, "(broccoli, salad, green beans, peppers)", 'F1', 10, 0.4)
pdf.add_text(70, 615, "1/4 plate = Lean protein", 'F1', 11)
pdf.add_text(90, 598, "(chicken, fish, tofu, eggs)", 'F1', 10, 0.4)
pdf.add_text(70, 575, "1/4 plate = Carbohydrates/starch", 'F1', 11)
pdf.add_text(90, 558, "(rice, potato, bread, pasta)", 'F1', 10, 0.4)
pdf.add_text(70, 535, "+ Water or zero-calorie drink", 'F1', 11)
pdf.add_text(50, 500, "TIPS:", 'F2', 12)
tips = ["Eat at regular times each day", "Don't skip meals",
        "Include protein with every meal/snack to slow carb absorption",
        "Choose whole grains over refined grains",
        "Pair carbs with fiber, protein, or healthy fat"]
y = 480
for t in tips:
    pdf.add_text(60, y, f"- {t}", 'F1', 10)
    y -= 16


# Pages 5-16 - 12 Weekly Meal Plan Pages
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for week in range(1, 13):
    pdf.new_page()
    pdf.add_centered_text(740, f"WEEKLY MEAL PLAN - WEEK {week}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    y = 715
    for day in days:
        pdf.add_text(50, y, day, 'F2', 8)
        pdf.add_text(115, y, "B:", 'F2', 7)
        pdf.add_line(128, y-2, 280, y-2, 0.3, 0.7)
        pdf.add_text(285, y, "Carbs:___g", 'F1', 7)
        pdf.add_text(115, y-12, "L:", 'F2', 7)
        pdf.add_line(128, y-14, 280, y-14, 0.3, 0.7)
        pdf.add_text(285, y-12, "Carbs:___g", 'F1', 7)
        pdf.add_text(115, y-24, "D:", 'F2', 7)
        pdf.add_line(128, y-26, 280, y-26, 0.3, 0.7)
        pdf.add_text(285, y-24, "Carbs:___g", 'F1', 7)
        pdf.add_text(355, y, "Snk:", 'F1', 7)
        pdf.add_line(380, y-2, 500, y-2, 0.3, 0.7)
        pdf.add_text(505, y, "___g", 'F1', 7)
        pdf.add_text(355, y-12, "Total:", 'F2', 7)
        pdf.add_text(390, y-12, "___g", 'F1', 7)
        pdf.add_line(50, y-34, 562, y-34, 0.5, 0.5)
        y -= 44
    pdf.add_text(50, y, "Weekly avg carbs/day: ___g  Blood sugar notes:", 'F1', 9)
    pdf.add_line(350, y-2, 562, y-2, 0.5, 0.7)
    pdf.add_text(50, y-18, "Meals that spiked me: ___________________________________", 'F1', 9)

# Pages 17-20 - Grocery List Templates (4 pages)
for pg in range(4):
    pdf.new_page()
    pdf.add_centered_text(740, f"GROCERY LIST - WEEK ___", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    categories = [("VEGETABLES", 50), ("FRUITS", 50), ("PROTEINS", 310),
                  ("GRAINS/STARCHES", 310), ("DAIRY", 50), ("OTHER", 310)]
    y_start = 710
    col_items = 6
    for idx, (cat, x) in enumerate(categories):
        y_pos = y_start - (idx // 2) * 180
        if idx % 2 == 0 and idx > 0:
            pass
        pdf.add_text(x, y_pos, cat, 'F2', 9)
        y = y_pos - 15
        for i in range(col_items):
            pdf.add_rect(x + 5, y-7, 8, 8)
            pdf.add_line(x + 18, y-4, x + 200, y-4, 0.3, 0.7)
            y -= 15

# Page 21 - Low-Glycemic Food Reference
pdf.new_page()
pdf.add_centered_text(740, "LOW-GLYCEMIC FOOD REFERENCE", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "LOW GI (55 or less) - Best choices:", 'F2', 11)
low_gi = ["Most fruits (berries, apples, pears)", "Non-starchy vegetables",
           "Steel-cut oats", "Sweet potatoes", "Legumes/beans",
           "Whole grain bread", "Quinoa", "Nuts and seeds"]
y = 690
for f in low_gi:
    pdf.add_text(60, y, f"- {f}", 'F1', 10)
    y -= 15
pdf.add_text(50, y-10, "MEDIUM GI (56-69) - In moderation:", 'F2', 11)
y -= 28
med_gi = ["Brown rice", "Whole wheat pasta", "Banana", "Raisins", "Corn"]
for f in med_gi:
    pdf.add_text(60, y, f"- {f}", 'F1', 10)
    y -= 15
pdf.add_text(50, y-10, "HIGH GI (70+) - Limit or pair with protein:", 'F2', 11)
y -= 28
high_gi = ["White bread", "White rice", "Potatoes", "Watermelon",
           "Sugary cereals", "Soda/juice"]
for f in high_gi:
    pdf.add_text(60, y, f"- {f}", 'F1', 10)
    y -= 15


# Page 22 - Eating Out Guide
pdf.new_page()
pdf.add_centered_text(740, "EATING OUT GUIDE", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Restaurant strategies for blood sugar control:", 'F2', 11)
strategies = [
    "Look at the menu online beforehand and plan your order",
    "Ask for sauces/dressings on the side",
    "Choose grilled over fried",
    "Sub extra vegetables for starchy sides",
    "Share a dessert instead of having a whole one",
    "Drink water instead of sweetened beverages",
    "Don't arrive starving - have a small protein snack before",
    "Ask how food is prepared (hidden sugars in sauces!)",
    "Take half home - restaurant portions are usually 2x a serving",
]
y = 688
for s in strategies:
    pdf.add_text(60, y, f"- {s}", 'F1', 10)
    y -= 17
pdf.add_text(50, y-10, "FAST FOOD SWAPS:", 'F2', 11)
y -= 30
swaps = [("Burger with bun", "Lettuce wrap or half the bun"),
         ("French fries", "Side salad or apple slices"),
         ("Regular soda", "Water, diet soda, or unsweetened tea"),
         ("Large combo", "Smallest size, no combo")]
for orig, swap in swaps:
    pdf.add_text(60, y, f"{orig}  ->  {swap}", 'F1', 10)
    y -= 16

# Page 23 - Snack Ideas Under 15g Carbs
pdf.new_page()
pdf.add_centered_text(740, "SNACK IDEAS UNDER 15g CARBS", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
snacks = [
    ("Cheese stick + 5 crackers", "~12g"), ("1/4 cup almonds", "~6g"),
    ("Celery + 2 tbsp peanut butter", "~7g"), ("Hard boiled egg", "~1g"),
    ("1/2 cup cottage cheese + berries", "~10g"), ("10 baby carrots + hummus", "~12g"),
    ("Turkey roll-ups (deli meat + cheese)", "~2g"), ("1 small apple + 1 tbsp almond butter", "~14g"),
    ("Sugar-free jello + whipped cream", "~3g"), ("1/4 cup sunflower seeds", "~5g"),
    ("Cucumber + cream cheese", "~4g"), ("1/2 cup edamame", "~7g"),
    ("Greek yogurt (plain, 1/2 cup)", "~5g"), ("Handful of olives", "~2g"),
    ("Beef or turkey jerky (1 oz)", "~3g"), ("Dill pickles (unlimited!)", "~1g"),
]
y = 710
for snack, carbs in snacks:
    pdf.add_text(60, y, snack, 'F1', 10)
    pdf.add_text(420, y, carbs, 'F3', 9)
    y -= 18
pdf.add_text(50, y-15, "My favorite diabetic-friendly snacks:", 'F2', 10)
y -= 35
for i in range(5):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 18

# Pages 24-29 - Recipe Cards (6 blank recipe cards)
for rc in range(6):
    pdf.new_page()
    pdf.add_centered_text(740, f"MY DIABETIC-FRIENDLY RECIPE #{rc+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, "Recipe name: _________________________________________", 'F1', 11)
    pdf.add_text(50, 690, "Servings: _____  Carbs per serving: _____g  Prep time: _____", 'F1', 10)
    pdf.add_text(50, 665, "INGREDIENTS:", 'F2', 11)
    y = 645
    for i in range(10):
        pdf.add_line(60, y, 350, y, 0.5, 0.7)
        y -= 16
    pdf.add_text(50, y-5, "DIRECTIONS:", 'F2', 11)
    y -= 22
    for i in range(8):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 16
    pdf.add_text(50, y-5, "Blood sugar response: _______ (before) _______ (2hr after)", 'F1', 10)
    pdf.add_text(50, y-22, "Would I make this again?  Y / N   Rating: ___/5", 'F1', 10)

# Page 30 - Blood Sugar Response Notes
pdf.new_page()
pdf.add_centered_text(740, "BLOOD SUGAR RESPONSE NOTES", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Track which meals spike you and which keep you steady:", 'F1', 10)
y = 690
pdf.add_text(50, y, "MEAL", 'F2', 8)
pdf.add_text(200, y, "BEFORE", 'F2', 8)
pdf.add_text(260, y, "2HR AFTER", 'F2', 8)
pdf.add_text(340, y, "SPIKE?", 'F2', 8)
pdf.add_text(400, y, "NOTES", 'F2', 8)
y -= 5
pdf.add_line(50, y, 562, y, 0.5)
y -= 15
for i in range(28):
    pdf.add_line(50, y, 190, y, 0.3, 0.7)
    pdf.add_line(200, y, 252, y, 0.3, 0.7)
    pdf.add_line(260, y, 332, y, 0.3, 0.7)
    pdf.add_line(340, y, 390, y, 0.3, 0.7)
    pdf.add_line(400, y, 562, y, 0.3, 0.7)
    y -= 18

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book183_Diabetic_Meal_Planner.pdf')
print("Book183_Diabetic_Meal_Planner.pdf created successfully!")
