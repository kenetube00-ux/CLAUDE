from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(490, "BABY-LED WEANING", 'F2', 17)
pdf.add_centered_text(465, "MEAL PLANNER &", 'F2', 15)
pdf.add_centered_text(443, "FOOD INTRODUCTION TRACKER", 'F2', 14)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(500, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)
pdf.add_centered_text(475, "Always consult your pediatrician before starting solids.", 'F4', 9)

# Page 3: BLW Basics
pdf.new_page()
pdf.add_centered_text(610, "BLW BASICS EXPLAINED", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "WHAT IS BABY-LED WEANING (BLW)?",
    "Letting your baby self-feed from the start of solids (around 6",
    "months). No purees, no spoon-feeding - baby picks up food!", "",
    "BENEFITS:",
    "- Develops fine motor skills and hand-eye coordination",
    "- Baby learns to self-regulate appetite",
    "- Reduces picky eating (exposed to textures early)",
    "- Family eats together (same foods, modified)", "",
    "SAFETY ESSENTIALS:",
    "- Baby must sit upright independently",
    "- Always supervise meals (never leave baby alone with food)",
    "- Know the difference between gagging and choking",
    "- Cut round foods (grapes, cherry tomatoes) lengthwise",
    "- No honey until age 1, no whole nuts until age 4",
    "- Soft enough to squish between your fingers = safe", "",
    "FIRST FOOD SHAPES (for 6-month-olds):",
    "- Finger-length strips (baby grabs with whole fist)",
    "- Soft, mashable with gums",
    "- Examples: avocado strips, banana, steamed sweet potato"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 4: Readiness Signs
pdf.new_page()
pdf.add_centered_text(610, "READINESS SIGNS CHECKLIST", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "ALL of these must be present (usually around 6 months):", "",
    "__ Can sit upright with minimal support",
    "__ Has lost the tongue-thrust reflex",
    "__ Shows interest in food (reaching, watching you eat)",
    "__ Can bring objects to mouth",
    "__ Can hold head steady", "",
    "NOT readiness signs (common myths):",
    "- Waking at night (normal at any age)",
    "- Watching you eat (curiosity, not hunger)",
    "- Being a certain weight", "",
    "MY BABY'S READINESS:",
    "Date baby showed all signs: ___/___/___",
    "Date we started BLW: ___/___/___",
    "Pediatrician approved: Y / N  Date: ___/___/___", "",
    "FOODS BY AGE:", "",
    "6 MONTHS: Soft strips, single ingredients",
    "7-8 MONTHS: Smaller pieces, soft combinations",
    "9-12 MONTHS: Most family foods, modified for safety",
    "12+ MONTHS: Almost everything (watch choking hazards)"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 5: Allergen Introduction
pdf.new_page()
pdf.add_centered_text(610, "ALLERGEN INTRODUCTION TRACKER", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
pdf.add_text(50, y, "Introduce top allergens early (6-12 months) & often.", 'F4', 10)
y -= 12
pdf.add_text(50, y, "Give each new allergen for 3 days. Note any reactions.", 'F4', 9)
y -= 18
allergens = ["Cow's milk (dairy)", "Egg", "Peanut", "Tree nuts", "Wheat",
    "Soy", "Fish", "Shellfish", "Sesame"]
for a in allergens:
    pdf.add_text(50, y, f"{a}:", 'F2', 9)
    y -= 12
    pdf.add_text(55, y, "Date introduced: ___/___ Form given: ____________", 'F3', 8)
    y -= 11
    pdf.add_text(55, y, "Reaction? Y/N  If yes: ________________________", 'F3', 8)
    y -= 11
    pdf.add_text(55, y, "Date re-introduced: ___/___ Ongoing? Y/N", 'F3', 8)
    y -= 16


# Pages 6-20: Daily Food Log (15 pages)
for pg in range(1, 16):
    pdf.new_page()
    start = (pg-1)*3 + 1
    pdf.add_centered_text(618, f"DAILY FOOD LOG - DAYS {start}-{start+2}", 'F2', 12)
    pdf.add_line(50, 608, 382, 608)
    y = 592
    for day in range(3):
        pdf.add_text(50, y, f"DAY {start+day}  Date: ___/___", 'F2', 9)
        y -= 13
        pdf.add_text(55, y, "Breakfast: ____________________________________", 'F3', 8)
        y -= 11
        pdf.add_text(55, y, "Lunch: ________________________________________", 'F3', 8)
        y -= 11
        pdf.add_text(55, y, "Dinner: _______________________________________", 'F3', 8)
        y -= 11
        pdf.add_text(55, y, "New foods tried: ______________________________", 'F3', 8)
        y -= 11
        pdf.add_text(55, y, "Reactions: _________ Stool changes: ____________", 'F3', 8)
        y -= 16
        pdf.add_line(50, y+5, 382, y+5, 0.3, 0.7)
        y -= 8

# Page 21: Gagging vs Choking
pdf.new_page()
pdf.add_centered_text(610, "GAGGING vs CHOKING GUIDE", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "GAGGING (NORMAL - do NOT intervene):",
    "- Baby is noisy (coughing, sputtering)",
    "- Face may turn red briefly",
    "- Baby can still breathe",
    "- Baby resolves it on their own",
    "- This is baby LEARNING to eat safely", "",
    "CHOKING (EMERGENCY - act immediately):",
    "- Baby is SILENT (no sound)",
    "- Cannot cry or cough",
    "- Lips/face turning blue",
    "- Panicked look", "",
    "IF CHOKING: Infant CPR (take a class BEFORE starting BLW!)",
    "1. 5 back blows (between shoulder blades)",
    "2. 5 chest thrusts (center of chest)",
    "3. Alternate until object dislodges or baby goes limp",
    "4. Call 911 if not resolved", "",
    "PREVENT CHOKING:",
    "- No round foods (cut grapes, hot dogs lengthwise)",
    "- No hard foods (raw carrot, whole nuts)",
    "- Always supervise",
    "- Baby sitting upright in high chair",
    "- No eating in car seats or while walking"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14

# Pages 22-25: Weekly Meal Plans + Iron-Rich + Milestones
pdf.new_page()
pdf.add_centered_text(610, "IRON-RICH FOODS & MEAL PREP TIPS", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "IRON-RICH FOODS (essential for babies 6+ months):", "",
    "- Red meat (ground beef, lamb - easiest for baby)",
    "- Dark poultry (chicken thigh)",
    "- Lentils and beans (mashed or whole for 9+mo)",
    "- Tofu (cubed or strips)",
    "- Egg yolks",
    "- Iron-fortified cereal",
    "- Spinach (cooked, mixed into foods)",
    "- Chia seeds (mixed into yogurt or oatmeal)", "",
    "PAIR WITH VITAMIN C for better absorption:",
    "Strawberries, oranges, bell peppers, tomatoes, broccoli", "",
    "MEAL PREP TIPS FOR BLW:",
    "- Batch cook and freeze in portions",
    "- Roast veggies in strips at start of week",
    "- Keep avocados and bananas for quick meals",
    "- Modify your dinner for baby (less salt, softer)",
    "- Silicone ice trays = perfect portion freezing", "",
    "FOODS MASTERED LIST:",
    "_______________________________________________",
    "_______________________________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14

for week in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(610, f"WEEKLY MEAL PLAN - WEEK {week}", 'F2', 13)
    pdf.add_line(50, 598, 382, 598)
    y = 580
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        pdf.add_text(50, y, f"{day}:", 'F2', 9)
        pdf.add_text(80, y, "B: _________ L: _________ D: _________", 'F3', 8)
        y -= 18

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book116_Baby_Led_Weaning_Planner.pdf')
print("Book116_Baby_Led_Weaning_Planner.pdf created successfully!")
