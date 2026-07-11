"""
Book 169: ADHD MEAL PLANNER
Simple Systems for Feeding Yourself Without Overwhelm
Author: Daniel Tesfamariam
"""
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)

# ============ PAGE 1: Title Page ============
pdf.new_page()
pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
pdf.add_centered_text(520, "ADHD MEAL PLANNER", "F2", 28)
pdf.add_centered_text(480, "Simple Systems for Feeding Yourself", "F4", 18, gray=0.2)
pdf.add_centered_text(455, "Without Overwhelm", "F4", 18, gray=0.2)
pdf.add_line(180, 440, 432, 440, 2, gray=0.4)
pdf.add_centered_text(390, "Less Decisions. Less Stress. More Eating.", "F1", 14, gray=0.3)
pdf.add_centered_text(350, "A practical planner for brains that struggle", "F1", 12, gray=0.4)
pdf.add_centered_text(330, "with executive function around food", "F1", 12, gray=0.4)
pdf.add_centered_text(100, "Daniel Tesfamariam", "F2", 16, gray=0.2)
pdf.add_centered_text(75, "KDP Publishing", "F1", 11, gray=0.4)

# ============ PAGE 2: Copyright ============
pdf.new_page()
pdf.add_centered_text(700, "ADHD MEAL PLANNER", "F2", 14)
pdf.add_centered_text(675, "Simple Systems for Feeding Yourself Without Overwhelm", "F1", 11)
pdf.add_centered_text(620, "Copyright 2025 Daniel Tesfamariam", "F1", 11)
pdf.add_centered_text(600, "All rights reserved.", "F1", 11)
pdf.add_centered_text(570, "No part of this publication may be reproduced, distributed,", "F1", 10)
pdf.add_centered_text(555, "or transmitted without the prior written permission of the author.", "F1", 10)
pdf.add_centered_text(510, "This book is designed as a personal planning tool.", "F1", 10)
pdf.add_centered_text(495, "It is not a substitute for medical or nutritional advice.", "F1", 10)
pdf.add_centered_text(475, "Consult a healthcare professional for dietary guidance.", "F1", 10)
pdf.add_centered_text(430, "Published by Daniel Tesfamariam", "F1", 11)
pdf.add_centered_text(410, "First Edition, 2025", "F1", 11)

# ============ PAGE 3: Why Meal Planning is Hard with ADHD ============
pdf.new_page()
pdf.add_centered_text(750, "WHY MEAL PLANNING IS HARD WITH ADHD", "F2", 16)
pdf.add_line(100, 740, 512, 740, 1, gray=0.5)


y = 710
pdf.add_text(72, y, "If you struggle with food planning, you are not broken. Your brain works differently.", "F4", 12, gray=0.2)
y -= 30

pdf.add_text(72, y, "1. DECISION FATIGUE", "F2", 13)
y -= 20
pdf.add_text(90, y, "Every meal requires dozens of micro-decisions: what to eat, what to buy,", "F1", 11)
y -= 16
pdf.add_text(90, y, "how to prep, when to start. ADHD brains burn out on decisions fast.", "F1", 11)
y -= 30

pdf.add_text(72, y, "2. EXECUTIVE DYSFUNCTION", "F2", 13)
y -= 20
pdf.add_text(90, y, "Knowing you need to eat and actually getting up to make food are", "F1", 11)
y -= 16
pdf.add_text(90, y, "two completely different things. The gap between intent and action is real.", "F1", 11)
y -= 30

pdf.add_text(72, y, "3. BOREDOM WITH ROUTINE", "F2", 13)
y -= 20
pdf.add_text(90, y, "Traditional meal plans assume you can eat the same thing happily.", "F1", 11)
y -= 16
pdf.add_text(90, y, "ADHD brains crave novelty - but also need structure. It's a paradox.", "F1", 11)
y -= 30

pdf.add_text(72, y, "4. FORGETTING TO EAT", "F2", 13)
y -= 20
pdf.add_text(90, y, "Poor interoception means hunger signals get missed. You look up", "F1", 11)
y -= 16
pdf.add_text(90, y, "and it's 3pm and you haven't eaten. This isn't laziness - it's neurology.", "F1", 11)
y -= 30

pdf.add_text(72, y, "5. HYPERFOCUS SKIPPING MEALS", "F2", 13)
y -= 20
pdf.add_text(90, y, "When you're locked into a task, eating feels like an impossible interruption.", "F1", 11)
y -= 16
pdf.add_text(90, y, "Breaking hyperfocus to cook? That requires enormous energy.", "F1", 11)
y -= 40

pdf.add_filled_rect(72, y - 10, 468, 55, gray=0.92)
pdf.add_text(90, y + 28, "THIS PLANNER'S APPROACH:", "F2", 12)
pdf.add_text(90, y + 10, "Remove decisions. Make the easy path the default path.", "F1", 11)
pdf.add_text(90, y - 8, "Systems over willpower. Always.", "F1", 11)


# ============ PAGE 4: The 5-Recipe Rotation System ============
pdf.new_page()
pdf.add_centered_text(750, "THE 5-RECIPE ROTATION SYSTEM", "F2", 16)
pdf.add_line(100, 740, 512, 740, 1, gray=0.5)

y = 710
pdf.add_text(72, y, "The simplest meal planning system that actually works for ADHD brains:", "F4", 12, gray=0.2)
y -= 35

pdf.add_text(72, y, "THE CONCEPT:", "F2", 13)
y -= 22
pdf.add_text(90, y, "Pick 5 dinners you can make on autopilot. Rotate them weekly.", "F1", 11)
y -= 16
pdf.add_text(90, y, "Only add a new recipe when one of the 5 gets boring.", "F1", 11)
y -= 30

pdf.add_text(72, y, "WHY IT WORKS:", "F2", 13)
y -= 20
pdf.add_text(90, y, "- Zero decision-making on weeknights", "F1", 11)
y -= 16
pdf.add_text(90, y, "- Grocery lists become automatic", "F1", 11)
y -= 16
pdf.add_text(90, y, "- You already know you like these meals", "F1", 11)
y -= 16
pdf.add_text(90, y, "- Cooking becomes muscle memory, not a project", "F1", 11)
y -= 30

pdf.add_text(72, y, "MY 5 ROTATION DINNERS:", "F2", 13)
y -= 5

for i in range(1, 6):
    y -= 25
    pdf.add_text(90, y, f"Dinner {i}: ", "F2", 11)
    pdf.add_line(155, y - 2, 500, y - 2, 0.5, gray=0.5)
    y -= 18
    pdf.add_text(90, y, "Key ingredients: ", "F1", 10, gray=0.4)
    pdf.add_line(185, y - 2, 500, y - 2, 0.5, gray=0.7)

y -= 35
pdf.add_text(72, y, "RULES:", "F2", 13)
y -= 20
pdf.add_text(90, y, "1. All 5 must be things you can make in under 30 minutes", "F1", 11)
y -= 16
pdf.add_text(90, y, "2. All 5 must use ingredients you can buy at ONE store", "F1", 11)
y -= 16
pdf.add_text(90, y, "3. If you haven't made one in 3 weeks, swap it out", "F1", 11)
y -= 16
pdf.add_text(90, y, "4. Weekend meals can be different (that's your novelty time)", "F1", 11)
y -= 16
pdf.add_text(90, y, "5. Takeout counts as a rotation slot if you need it to", "F1", 11)

y -= 35
pdf.add_filled_rect(72, y - 10, 468, 40, gray=0.92)
pdf.add_text(90, y + 14, "ADHD TIP: Start with 3 meals if 5 feels like too many.", "F2", 11)
pdf.add_text(90, y - 4, "You can always add more later. Progress over perfection.", "F1", 11)


# ============ PAGE 5: Decision Fatigue Elimination ============
pdf.new_page()
pdf.add_centered_text(750, "DECISION FATIGUE ELIMINATION", "F2", 16)
pdf.add_line(100, 740, 512, 740, 1, gray=0.5)

y = 710
pdf.add_text(72, y, "The fewer food decisions you make each day, the more energy you have for life.", "F4", 12, gray=0.2)
y -= 35

pdf.add_text(72, y, "PRE-DECIDE EVERYTHING", "F2", 13)
y -= 22
pdf.add_text(90, y, "Your future self should never have to think. Today-you decides for tomorrow-you.", "F1", 11)
y -= 30

pdf.add_text(72, y, "SAME BREAKFAST DAILY IS FINE", "F2", 13)
y -= 20
pdf.add_text(90, y, "Eating the same breakfast every day is not boring - it's efficient.", "F1", 11)
y -= 16
pdf.add_text(90, y, "My default breakfast: ", "F1", 11)
pdf.add_line(220, y - 2, 500, y - 2, 0.5, gray=0.5)
y -= 16
pdf.add_text(90, y, "My backup breakfast: ", "F1", 11)
pdf.add_line(220, y - 2, 500, y - 2, 0.5, gray=0.5)
y -= 30

pdf.add_text(72, y, "REDUCE CHOICES", "F2", 13)
y -= 20
pdf.add_text(90, y, "Instead of 'what do I want for lunch?' choose from 3 preset options:", "F1", 11)
y -= 20
for i in range(1, 4):
    pdf.add_text(90, y, f"Lunch option {i}: ", "F1", 11)
    pdf.add_line(195, y - 2, 500, y - 2, 0.5, gray=0.5)
    y -= 20
y -= 15

pdf.add_text(72, y, "SNACK DEFAULTS (no thinking required):", "F2", 13)
y -= 20
for i in range(1, 5):
    pdf.add_text(90, y, f"Go-to snack {i}: ", "F1", 11)
    pdf.add_line(185, y - 2, 400, y - 2, 0.5, gray=0.5)
    y -= 20
y -= 15

pdf.add_text(72, y, "THE 'DON'T THINK' FRAMEWORK:", "F2", 13)
y -= 22
pdf.add_text(90, y, "- Hungry + no plan = grab preset snack (always stocked)", "F1", 11)
y -= 16
pdf.add_text(90, y, "- Hungry + some energy = make rotation meal", "F1", 11)
y -= 16
pdf.add_text(90, y, "- Hungry + zero energy = permission to order food", "F1", 11)
y -= 16
pdf.add_text(90, y, "- Not hungry but it's mealtime = eat 5 bites minimum", "F1", 11)
y -= 30

pdf.add_filled_rect(72, y - 10, 468, 40, gray=0.92)
pdf.add_text(90, y + 14, "REMEMBER: Eating 'imperfectly' is always better than not eating.", "F2", 11)
pdf.add_text(90, y - 4, "Cereal for dinner counts. A protein bar counts. You ate. That's the win.", "F1", 11)


# ============ PAGES 6-13: Grocery List Templates (8 pages) ============
grocery_sections = [
    ("PRODUCE", ["Bananas", "Apples", "Baby carrots", "Bagged salad mix", "Avocados",
                 "Frozen berries", "Potatoes", "Onions", "Garlic", "Tomatoes",
                 "Bell peppers", "Lemons/limes", "Fresh herbs", "Broccoli", "Spinach"]),
    ("DAIRY & EGGS", ["Milk/alt milk", "Eggs", "Shredded cheese", "Butter", "Yogurt (plain or Greek)",
                      "Cream cheese", "Sour cream", "Cottage cheese", "Parmesan", "String cheese",
                      "Heavy cream", "Coffee creamer", "", "", ""]),
    ("PROTEIN", ["Chicken breast/thighs", "Ground beef/turkey", "Deli meat", "Bacon/sausage",
                 "Canned tuna/salmon", "Tofu/tempeh", "Frozen shrimp", "Rotisserie chicken",
                 "Hot dogs/brats", "Frozen fish fillets", "Beef stew meat", "Pork chops",
                 "", "", ""]),
    ("PANTRY STAPLES", ["Rice (white/brown)", "Pasta (2 shapes)", "Bread", "Tortillas",
                        "Canned beans (2 types)", "Canned tomatoes", "Chicken/veggie broth",
                        "Peanut butter", "Olive oil", "Soy sauce", "Marinara sauce",
                        "Oatmeal", "Cereal", "Crackers", "Granola bars"]),
    ("FROZEN FOODS", ["Frozen veggies (3 types)", "Frozen fruit", "Frozen pizza",
                      "Frozen burritos", "Ice cream/treats", "Frozen meals (backup)",
                      "Frozen chicken nuggets", "Frozen waffles", "Frozen dumplings",
                      "Frozen hash browns", "Edamame", "Frozen bread/rolls", "", "", ""]),
    ("SNACKS & DRINKS", ["Coffee/tea", "Sparkling water", "Juice", "Trail mix",
                         "Chips", "Popcorn", "Dried fruit", "Nuts", "Hummus",
                         "Pretzels", "Protein bars", "Chocolate", "Cheese crackers",
                         "Fruit snacks", "Applesauce cups"]),
    ("CONDIMENTS & SPICES", ["Salt & pepper", "Garlic powder", "Italian seasoning",
                             "Cumin", "Paprika", "Red pepper flakes", "Ketchup",
                             "Mustard", "Mayo", "Hot sauce", "Ranch dressing",
                             "Honey", "Vinegar", "Salad dressing", "BBQ sauce"]),
    ("HOUSEHOLD & OTHER", ["Paper towels", "Dish soap", "Trash bags", "Aluminum foil",
                           "Plastic wrap", "Zip bags", "Sponges", "Napkins",
                           "", "", "", "", "", "", ""])
]

for page_idx, (section_name, items) in enumerate(grocery_sections):
    pdf.new_page()
    pdf.add_centered_text(750, f"GROCERY LIST - {section_name}", "F2", 15)
    pdf.add_text(72, 730, f"Week of: _______________    Store: _______________", "F1", 10, gray=0.4)
    pdf.add_line(72, 722, 540, 722, 1, gray=0.5)

    y = 700
    pdf.add_text(72, y, "Item", "F2", 10)
    pdf.add_text(350, y, "Qty", "F2", 10)
    pdf.add_text(420, y, "Got it", "F2", 10)
    pdf.add_text(490, y, "Notes", "F2", 10)
    y -= 5
    pdf.add_line(72, y, 540, y, 0.5, gray=0.4)
    y -= 18

    for item in items:
        if item == "":
            # blank row for custom items
            pdf.add_rect(72, y - 3, 10, 10, 0.5, gray=0.5)
            pdf.add_line(100, y - 2, 330, y - 2, 0.5, gray=0.7)
            pdf.add_line(350, y - 2, 400, y - 2, 0.5, gray=0.7)
            pdf.add_rect(435, y - 3, 10, 10, 0.5, gray=0.5)
            pdf.add_line(490, y - 2, 540, y - 2, 0.5, gray=0.7)
        else:
            pdf.add_rect(72, y - 3, 10, 10, 0.5, gray=0.5)
            pdf.add_text(100, y, item, "F1", 10)
            pdf.add_line(350, y - 2, 400, y - 2, 0.5, gray=0.7)
            pdf.add_rect(435, y - 3, 10, 10, 0.5, gray=0.5)
            pdf.add_line(490, y - 2, 540, y - 2, 0.5, gray=0.7)
        y -= 22

    # Add extra blank rows
    for _ in range(10):
        pdf.add_rect(72, y - 3, 10, 10, 0.5, gray=0.5)
        pdf.add_line(100, y - 2, 330, y - 2, 0.5, gray=0.7)
        pdf.add_line(350, y - 2, 400, y - 2, 0.5, gray=0.7)
        pdf.add_rect(435, y - 3, 10, 10, 0.5, gray=0.5)
        pdf.add_line(490, y - 2, 540, y - 2, 0.5, gray=0.7)
        y -= 22

    pdf.add_filled_rect(72, 60, 468, 35, gray=0.93)
    pdf.add_text(90, 80, "ADHD TIP: Take a photo of this list before you go. Phone > paper in the store.", "F1", 9, gray=0.3)
    pdf.add_text(90, 66, f"Page {page_idx + 6} of 30", "F1", 8, gray=0.5)


# ============ PAGES 14-25: Weekly Meal Plan Pages (12 weeks) ============
grab_and_go_breakfasts = [
    "Yogurt + granola", "Toast + PB", "Protein bar", "Overnight oats", "Banana + nuts"
]
grab_and_go_lunches = [
    "Deli sandwich", "Leftovers", "Quesadilla", "Soup (canned/frozen)", "Wrap + veggies"
]

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

for week_num in range(1, 13):
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEKLY MEAL PLAN - WEEK {week_num}", "F2", 15)
    pdf.add_text(72, 730, f"Dates: ____/____  to  ____/____", "F1", 10, gray=0.4)
    pdf.add_line(72, 722, 540, 722, 1, gray=0.5)

    # Grab and go presets at top
    y = 705
    pdf.add_filled_rect(72, y - 12, 468, 48, gray=0.93)
    pdf.add_text(80, y + 20, "GRAB-AND-GO PRESETS (no planning needed):", "F2", 9)
    b_text = "Breakfast: " + " | ".join(grab_and_go_breakfasts)
    l_text = "Lunch: " + " | ".join(grab_and_go_lunches)
    pdf.add_text(80, y + 5, b_text, "F1", 8, gray=0.3)
    pdf.add_text(80, y - 8, l_text, "F1", 8, gray=0.3)

    y = 680
    pdf.add_text(72, y, "Plan dinners only - keep it simple:", "F1", 10, gray=0.3)
    y -= 20

    for day in days:
        pdf.add_filled_rect(72, y - 5, 100, 18, gray=0.88)
        pdf.add_text(80, y, day, "F2", 9)
        pdf.add_text(180, y, "Dinner:", "F1", 9, gray=0.4)
        pdf.add_line(215, y - 2, 430, y - 2, 0.5, gray=0.6)
        pdf.add_text(440, y, "Prep:", "F1", 8, gray=0.4)
        pdf.add_line(465, y - 2, 540, y - 2, 0.5, gray=0.6)
        y -= 28

    # Notes section
    y -= 15
    pdf.add_text(72, y, "NOTES / GROCERY REMINDERS:", "F2", 10)
    y -= 5
    pdf.add_rect(72, y - 80, 468, 80, 0.5, gray=0.5)

    # Bottom tips
    y -= 100
    pdf.add_text(72, y, "This week's energy level (circle): LOW  /  MEDIUM  /  HIGH", "F1", 9, gray=0.4)
    y -= 16
    pdf.add_text(72, y, "Backup plan if I can't cook: ________________________________", "F1", 9, gray=0.4)
    y -= 16
    pdf.add_text(72, y, "Grocery shopping day: __________  Prep day: __________", "F1", 9, gray=0.4)

    pdf.add_text(490, 50, f"Page {week_num + 13}", "F1", 8, gray=0.5)


# ============ PAGE 26: Pantry Staples Master List ============
pdf.new_page()
pdf.add_centered_text(750, "PANTRY STAPLES MASTER LIST", "F2", 16)
pdf.add_text(72, 730, "Always have these on hand - never run out of easy meal options", "F4", 11, gray=0.3)
pdf.add_line(72, 722, 540, 722, 1, gray=0.5)

y = 700
categories = [
    ("GRAINS & CARBS", ["Rice", "Pasta (2 shapes)", "Bread/tortillas", "Oatmeal", "Crackers"]),
    ("CANNED GOODS", ["Beans (black, chickpea)", "Diced tomatoes", "Broth (chicken/veggie)", "Tuna/salmon", "Coconut milk"]),
    ("OILS & SAUCES", ["Olive oil", "Soy sauce", "Marinara", "Hot sauce", "Peanut butter"]),
    ("SPICES (basics only)", ["Salt", "Pepper", "Garlic powder", "Italian seasoning", "Cumin"]),
    ("FRIDGE ALWAYS", ["Eggs", "Butter", "Cheese (shredded)", "Milk/alt milk", "Tortillas"]),
    ("FREEZER ALWAYS", ["Frozen veggies (3 bags)", "Frozen fruit", "Frozen protein", "Frozen meals (backup)", "Ice cream (joy matters)"]),
]

for cat_name, cat_items in categories:
    pdf.add_text(72, y, cat_name, "F2", 11)
    y -= 18
    for item in cat_items:
        pdf.add_rect(90, y - 2, 8, 8, 0.5, gray=0.5)
        pdf.add_text(105, y, item, "F1", 10)
        y -= 16
    y -= 12

pdf.add_filled_rect(72, y - 10, 468, 45, gray=0.92)
pdf.add_text(90, y + 20, "RESTOCK RULE: When you use the last of something, write it on the", "F1", 10)
pdf.add_text(90, y + 5, "fridge list IMMEDIATELY. Don't trust your memory. ADHD + grocery", "F1", 10)
pdf.add_text(90, y - 8, "recall = empty pantry. Keep a running list visible at all times.", "F2", 10)


# ============ PAGE 27: 10-Minute Meal Ideas ============
pdf.new_page()
pdf.add_centered_text(750, "10-MINUTE MEAL IDEAS", "F2", 16)
pdf.add_text(72, 730, "20 meals you can make when you have zero executive function left", "F4", 11, gray=0.3)
pdf.add_line(72, 722, 540, 722, 1, gray=0.5)

meals_10min = [
    ("Quesadilla", "Tortilla, cheese, salsa, microwave/pan"),
    ("Egg scramble", "Eggs, cheese, whatever veggies you have"),
    ("PB&J + banana", "Bread, peanut butter, jam, banana"),
    ("Ramen upgrade", "Instant ramen, egg, frozen veggies, soy sauce"),
    ("Yogurt bowl", "Greek yogurt, granola, frozen berries, honey"),
    ("Bean & cheese burrito", "Tortilla, canned beans, cheese, hot sauce"),
    ("Toast trio", "3 pieces toast with different toppings"),
    ("Frozen pizza", "Frozen pizza, bag salad on the side"),
    ("Tuna melt", "Bread, canned tuna, mayo, cheese, broil"),
    ("Cereal dinner", "Cereal + milk (no shame, it's food)"),
    ("Hummus plate", "Hummus, crackers, baby carrots, cheese cubes"),
    ("Grilled cheese + soup", "Bread, butter, cheese, canned soup"),
    ("Rice + fried egg", "Leftover/instant rice, fried egg, soy sauce"),
    ("Avocado toast", "Toast, avocado, salt, pepper, everything bagel spice"),
    ("Mac & cheese +", "Box mac & cheese, add frozen peas or broccoli"),
    ("BLT sandwich", "Bacon (microwave), lettuce, tomato, bread, mayo"),
    ("Snack dinner", "Cheese, crackers, fruit, nuts, deli meat"),
    ("Smoothie", "Frozen fruit, yogurt, milk, honey, blend"),
    ("Pasta + jarred sauce", "Boil pasta, heat sauce, add parmesan"),
    ("Loaded nachos", "Chips, cheese, beans, microwave, add salsa"),
]

y = 700
for i, (name, ingredients) in enumerate(meals_10min):
    pdf.add_text(72, y, f"{i+1}.", "F2", 10)
    pdf.add_text(90, y, name, "F2", 10)
    pdf.add_text(210, y, ingredients, "F1", 9, gray=0.3)
    y -= 16
    if i == 9:
        y -= 8  # extra space at halfway

pdf.add_filled_rect(72, 60, 468, 35, gray=0.92)
pdf.add_text(90, 80, "RULE: If it takes under 10 min and you eat it, it counts as cooking.", "F2", 9)
pdf.add_text(90, 66, "Perfection is the enemy of fed.", "F1", 9, gray=0.3)


# ============ PAGE 28: Batch Cooking Day Guide ============
pdf.new_page()
pdf.add_centered_text(750, "BATCH COOKING DAY GUIDE", "F2", 16)
pdf.add_text(72, 730, "Pick ONE day. Cook 3-4 things. Fill the fridge for the week.", "F4", 11, gray=0.3)
pdf.add_line(72, 722, 540, 722, 1, gray=0.5)

y = 700
pdf.add_text(72, y, "THE ADHD-FRIENDLY BATCH COOK (2-3 hours max):", "F2", 12)
y -= 25

pdf.add_text(72, y, "STEP 1: Pick your batch day:  _______________", "F2", 11)
y -= 25

pdf.add_text(72, y, "STEP 2: Choose 3-4 items from this list:", "F2", 11)
y -= 20

batch_items = [
    "A big pot of rice or grain",
    "A sheet pan of roasted veggies",
    "A protein (baked chicken, ground meat, hard-boiled eggs)",
    "A sauce or dressing",
    "A batch of soup or chili",
    "Overnight oats (5 jars for the week)",
    "Cut up raw veggies + portion snacks into grab bags",
    "A casserole or baked pasta dish"
]

for item in batch_items:
    pdf.add_rect(90, y - 2, 8, 8, 0.5, gray=0.5)
    pdf.add_text(108, y, item, "F1", 10)
    y -= 18

y -= 20
pdf.add_text(72, y, "STEP 3: Write your batch plan for this week:", "F2", 11)
y -= 20
for i in range(1, 5):
    pdf.add_text(90, y, f"Item {i}: ", "F1", 10)
    pdf.add_line(135, y - 2, 400, y - 2, 0.5, gray=0.5)
    y -= 20

y -= 20
pdf.add_text(72, y, "STEP 4: Set a timer. Put on music/podcast. START.", "F2", 11)
y -= 25

pdf.add_text(72, y, "BATCH COOKING TIPS FOR ADHD:", "F2", 11)
y -= 18
tips = [
    "Set a phone timer for each item - don't trust yourself to 'just check'",
    "Clean as you go (or don't - it's fine to clean later)",
    "Body double: call a friend, watch a show, listen to a podcast",
    "If you only get 2 things done instead of 4, that's still a WIN",
    "Label containers with contents + date (you WILL forget what's in there)",
    "Store in single-serving containers for zero-thought grab-and-eat"
]
for tip in tips:
    pdf.add_text(90, y, f"- {tip}", "F1", 9)
    y -= 15

pdf.add_filled_rect(72, y - 15, 468, 35, gray=0.92)
pdf.add_text(90, y + 5, "PERMISSION SLIP: You don't have to batch cook every week.", "F2", 9)
pdf.add_text(90, y - 8, "Do it when you have energy. Skip it when you don't. Both are fine.", "F1", 9, gray=0.3)


# ============ PAGE 29: Snack Station + Emergency Options ============
pdf.new_page()
pdf.add_centered_text(750, "SNACK STATION SETUP", "F2", 16)
pdf.add_text(72, 730, "Plus: 'I Forgot to Plan' Emergency Options", "F4", 12, gray=0.3)
pdf.add_line(72, 722, 540, 722, 1, gray=0.5)

y = 700
pdf.add_text(72, y, "BUILD A SNACK STATION (one visible spot in your kitchen):", "F2", 12)
y -= 25

pdf.add_text(72, y, "Counter/shelf snacks (visible = eaten):", "F2", 11)
y -= 18
counter_snacks = ["Bananas/apples", "Granola bars", "Trail mix", "Crackers", "Nuts"]
for s in counter_snacks:
    pdf.add_rect(90, y - 2, 8, 8, 0.5, gray=0.5)
    pdf.add_text(108, y, s, "F1", 10)
    y -= 16

y -= 10
pdf.add_text(72, y, "Fridge snacks (clear containers, front of fridge):", "F2", 11)
y -= 18
fridge_snacks = ["Cut veggies + hummus", "Cheese sticks/cubes", "Yogurt cups", "Hard-boiled eggs", "Fruit (pre-washed)"]
for s in fridge_snacks:
    pdf.add_rect(90, y - 2, 8, 8, 0.5, gray=0.5)
    pdf.add_text(108, y, s, "F1", 10)
    y -= 16

y -= 10
pdf.add_text(72, y, "Freezer snacks (for texture cravings):", "F2", 11)
y -= 18
freezer_snacks = ["Frozen grapes", "Ice cream bars", "Frozen burritos", "Edamame", "Smoothie packs"]
for s in freezer_snacks:
    pdf.add_rect(90, y - 2, 8, 8, 0.5, gray=0.5)
    pdf.add_text(108, y, s, "F1", 10)
    y -= 16

y -= 20
pdf.add_line(72, y + 5, 540, y + 5, 1.5, gray=0.4)
y -= 10
pdf.add_text(72, y, "'I FORGOT TO PLAN' EMERGENCY OPTIONS:", "F2", 13)
y -= 22

emergencies = [
    "1. Order delivery (have your go-to saved in the app)",
    "2. Drive-through (keep a short list of your orders by restaurant)",
    "3. Cereal, toast, or snack plate = a real meal",
    "4. Frozen meal from the freezer stash",
    "5. Call someone to eat with (body doubling helps)",
    "6. Smoothie (throw anything in the blender)",
    "7. 'Adult lunchable' - cheese, crackers, meat, fruit on a plate",
]

for e in emergencies:
    pdf.add_text(90, y, e, "F1", 10)
    y -= 17

y -= 15
pdf.add_filled_rect(72, y - 10, 468, 35, gray=0.92)
pdf.add_text(90, y + 10, "THERE IS NO WRONG WAY TO FEED YOURSELF.", "F2", 10)
pdf.add_text(90, y - 5, "Eating something > eating nothing. Every single time.", "F1", 10, gray=0.3)


# ============ PAGE 30: Kitchen Organization + Meal Prep Checklist ============
pdf.new_page()
pdf.add_centered_text(750, "EXECUTIVE FUNCTION FRIENDLY KITCHEN", "F2", 15)
pdf.add_text(72, 730, "Organization + Meal Prep Day Checklist", "F4", 12, gray=0.3)
pdf.add_line(72, 722, 540, 722, 1, gray=0.5)

y = 700
pdf.add_text(72, y, "KITCHEN ORGANIZATION PRINCIPLES:", "F2", 12)
y -= 22

org_tips = [
    "Everything you use daily should be within arm's reach (not in cabinets)",
    "Clear containers > opaque (if you can't see it, it doesn't exist)",
    "Labels on EVERYTHING (your future self won't remember)",
    "Keep counters clear except your snack station",
    "One designated 'landing zone' for groceries when you get home",
    "Trash/recycling should be the easiest thing to access",
    "Keep your most-used pan on the stove (removing barriers = cooking)",
    "Paper plates are valid (if dishes stop you from eating, skip dishes)",
]

for tip in org_tips:
    pdf.add_text(80, y, f"- {tip}", "F1", 9.5)
    y -= 16

y -= 20
pdf.add_line(72, y + 5, 540, y + 5, 1.5, gray=0.4)
y -= 10
pdf.add_text(72, y, "MEAL PREP DAY CHECKLIST:", "F2", 12)
y -= 22

checklist = [
    "Pick your prep day and TIME (put it in your calendar with an alarm)",
    "Review what's in the fridge that needs to be used up",
    "Pick 3-4 batch items from page 28",
    "Check pantry staples list - do you need anything?",
    "Write grocery list (or use the templates on pages 6-13)",
    "Go shopping (or order delivery/pickup)",
    "Set up your space: clear counter, get out tools, set timer",
    "Put on music/podcast/show (dopamine helps!)",
    "Cook item 1 - set timer",
    "While waiting: prep item 2",
    "Cook item 3 - set timer",
    "While waiting: portion into containers + label",
    "Clean up (or leave it - future you can handle it)",
    "Take a photo of your full fridge (dopamine hit!)",
    "Celebrate - you just made the whole week easier",
]

for item in checklist:
    pdf.add_rect(80, y - 2, 8, 8, 0.5, gray=0.5)
    pdf.add_text(98, y, item, "F1", 9.5)
    y -= 16

y -= 15
pdf.add_filled_rect(72, y - 10, 468, 35, gray=0.92)
pdf.add_text(90, y + 10, "YOU DID IT. This planner is here whenever you need it.", "F2", 10)
pdf.add_text(90, y - 5, "Progress, not perfection. Systems, not willpower. You've got this.", "F1", 10, gray=0.3)

# ============ SAVE ============
pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book169_ADHD_Meal_Planner.pdf')
print("SUCCESS: Book169_ADHD_Meal_Planner.pdf generated (30 pages)")
