"""
Book 63: How To Meal Prep - Save Time, Eat Healthy, Spend Less
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "HOW TO MEAL PREP", font='F2', size=24)
    pdf.add_centered_text(485, "Save Time, Eat Healthy, Spend Less", font='F1', size=14)
    pdf.add_line(80, 460, 352, 460, 2)
    pdf.add_centered_text(420, "The Complete Guide to Planning,", font='F4', size=13)
    pdf.add_centered_text(398, "Cooking, and Storing Meals Ahead", font='F4', size=13)
    pdf.add_centered_text(330, "By", font='F1', size=12)
    pdf.add_centered_text(305, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "How To Meal Prep", font='F2', size=11)
    pdf.add_centered_text(475, "Save Time, Eat Healthy, Spend Less", font='F1', size=10)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(390, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(365, "Published via Amazon KDP", font='F1', size=10)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: What is Meal Prepping?", [
            "Meal prepping means preparing some or all of your meals in advance.",
            "You set aside a few hours each week to cook food for the days ahead.",
            "This can mean full meals ready to reheat or ingredients prepped for quick cooking.",
            "There are different levels: full meal prep, ingredient prep, and batch cooking.",
            "Full meal prep means complete meals portioned into containers ready to eat.",
            "Ingredient prep means washing, chopping, and measuring items for faster cooking.",
            "Batch cooking means making large quantities of one recipe to eat all week.",
            "Most meal preppers dedicate Sunday afternoon to cooking for the entire week.",
            "You do not have to prep every single meal. Even two to three saves significant time.",
            "Meal prepping has exploded in popularity because it works for busy lives.",
            "It removes the daily stress of deciding what to eat when you are tired.",
            "By the end of this book you will have a complete system that works for you.",
        ]),
        ("Chapter 2: Benefits of Meal Prepping", [
            "Save time: cooking once instead of seven times saves hours every week.",
            "Save money: buying in bulk and reducing food waste cuts grocery bills.",
            "Eat healthier: when healthy food is ready, you skip fast food and junk.",
            "Reduce stress: no more staring at the fridge wondering what to make.",
            "Control portions: pre-portioned meals help with weight management goals.",
            "Less food waste: you buy only what you need and use everything you purchase.",
            "More variety: planning ahead lets you enjoy diverse meals throughout the week.",
            "Better nutrition: you can balance proteins, carbs, and vegetables intentionally.",
            "Fewer dishes: one big cooking session means fewer total pots and pans to wash.",
            "More free time: weeknight dinners take minutes instead of an hour.",
            "Consistent eating: you are less likely to skip meals when food is ready.",
            "The average meal prepper saves four to six hours and fifty dollars per week.",
        ]),
        ("Chapter 3: Essential Kitchen Tools", [
            "Glass meal prep containers with locking lids are your most important investment.",
            "Buy a set of twelve to fifteen containers in different sizes.",
            "A large cutting board gives you space to chop vegetables efficiently.",
            "A sharp chef knife makes prep work faster and actually safer.",
            "Sheet pans are essential for roasting large batches of vegetables and proteins.",
            "A slow cooker or Instant Pot cooks hands-free while you prep other items.",
            "A rice cooker produces perfect grains every time without monitoring.",
            "Measuring cups and a food scale help with accurate portion control.",
            "Gallon and quart sized freezer bags store soups, sauces, and marinades flat.",
            "A good set of mixing bowls in various sizes helps organize ingredients.",
            "Labels and a marker let you date containers so you know freshness.",
            "You do not need expensive equipment. Start with containers and a good knife.",
        ]),
        ("Chapter 4: Planning Your Weekly Menu", [
            "Start by choosing three to four protein sources for the week.",
            "Select two to three grain or starch options to rotate throughout the week.",
            "Pick four to five vegetables that you enjoy and are in season.",
            "Plan breakfasts, lunches, dinners, and snacks based on your schedule.",
            "Consider which meals you eat at home versus which you take to work.",
            "Check what you already have in your pantry and fridge before planning.",
            "Build meals around sales and seasonal produce to save money.",
            "Keep a list of ten reliable recipes you can rotate without getting bored.",
            "Plan one new recipe per week to add variety without overwhelming yourself.",
            "Write out exactly what you will eat each day of the week.",
            "Note which ingredients overlap between recipes to maximize efficiency.",
            "A solid weekly plan is the foundation that makes everything else easy.",
        ]),
        ("Chapter 5: Grocery Shopping on a Budget", [
            "Always shop with a list based on your weekly meal plan.",
            "Check store flyers and apps for sales before making your list.",
            "Buy proteins in bulk when on sale and freeze what you will not use immediately.",
            "Purchase seasonal fruits and vegetables which are cheaper and taste better.",
            "Buy store brand staples like rice, beans, oats, and canned goods.",
            "Frozen vegetables are nutritious, affordable, and last much longer.",
            "Avoid shopping when hungry as this leads to impulse purchases.",
            "Shop the perimeter of the store first for fresh whole foods.",
            "Compare unit prices rather than total prices to find true deals.",
            "Buy whole chickens instead of pre-cut pieces to save significantly.",
            "Stock up on pantry staples when they go on deep discount.",
            "The average meal prepper spends fifty to seventy-five dollars per week for one person.",
        ]),
        ("Chapter 6: Batch Cooking Basics", [
            "Choose one day per week as your dedicated cooking day, usually Sunday.",
            "Start with items that take longest: roast meats and bake grains first.",
            "While proteins cook, wash and chop all vegetables for the week.",
            "Cook multiple items simultaneously using your oven, stovetop, and slow cooker.",
            "Prepare a large batch of grains: rice, quinoa, or pasta for the week.",
            "Roast two to three sheet pans of mixed vegetables at the same time.",
            "Cook two different proteins: perhaps chicken breasts and ground turkey.",
            "Make a big pot of soup or chili that provides four to six servings.",
            "Prepare sauces and dressings in advance to add flavor variety to base meals.",
            "Let everything cool completely before portioning into containers.",
            "Label each container with contents and date before refrigerating.",
            "A typical batch cooking session takes two to three hours for a full week of food.",
        ]),
        ("Chapter 7: Storing Food Safely", [
            "Refrigerated meal prep stays fresh for three to four days maximum.",
            "Freeze anything you plan to eat after day four for food safety.",
            "Cool hot food to room temperature within two hours before refrigerating.",
            "Store raw and cooked foods separately to prevent cross-contamination.",
            "Use airtight containers to maintain freshness and prevent freezer burn.",
            "Leave space in containers for frozen food to expand without cracking lids.",
            "Label everything with the date prepared and contents clearly.",
            "Most cooked meals freeze well for two to three months without quality loss.",
            "Thaw frozen meals overnight in the refrigerator, not on the counter.",
            "Reheat food to 165 degrees Fahrenheit to ensure safety.",
            "Glass containers are microwave safe and do not stain like plastic.",
            "When in doubt, throw it out. Food safety is not worth the risk.",
        ]),
        ("Chapter 8: Breakfast Prep Ideas", [
            "Overnight oats are the easiest make-ahead breakfast, requiring zero cooking.",
            "Mix oats, milk, yogurt, and toppings in jars the night before.",
            "Egg muffins bake in a muffin tin with vegetables and freeze perfectly.",
            "Make a batch of twelve egg muffins for two weeks of quick breakfasts.",
            "Smoothie packs: pre-portion fruit and greens into freezer bags.",
            "In the morning just dump a smoothie pack into the blender with liquid.",
            "Chia pudding preps in five minutes and keeps for five days refrigerated.",
            "Baked oatmeal cuts into squares and reheats in one minute.",
            "Homemade granola bars are cheaper and healthier than store-bought.",
            "Breakfast burritos wrap, freeze, and reheat in two minutes.",
            "Greek yogurt parfaits layer in mason jars for grab-and-go mornings.",
            "Having breakfast ready eliminates the most skipped meal of the day.",
        ]),
        ("Chapter 9: Lunch Prep Ideas", [
            "Mason jar salads layer ingredients so lettuce stays crisp for five days.",
            "Put dressing on the bottom, hard vegetables next, and greens on top.",
            "Grain bowls combine rice, protein, roasted vegetables, and sauce.",
            "Make five identical grain bowls on Sunday for the entire work week.",
            "Wraps and pinwheels prepare quickly and travel well in lunch boxes.",
            "Soup in thermos containers stays hot for hours without a microwave.",
            "Bento-style boxes with cheese, crackers, fruit, and protein need no cooking.",
            "Pasta salad keeps well and actually tastes better after a day in the fridge.",
            "Stuffed sweet potatoes reheat beautifully in the microwave at work.",
            "Chicken salad or tuna salad can be portioned for easy sandwich assembly.",
            "Include a mix of textures and colors to keep lunches interesting.",
            "Having lunch prepped saves the average person eight dollars per workday.",
        ]),
        ("Chapter 10: Dinner Prep Ideas", [
            "Sheet pan dinners combine protein and vegetables on one pan for easy cleanup.",
            "Stir-fry kits: pre-chop vegetables and sauce, cook fresh in five minutes.",
            "Slow cooker meals can be assembled raw in bags and frozen until needed.",
            "Dump the frozen bag into the slow cooker in the morning for dinner by evening.",
            "Casseroles assemble ahead and bake fresh when you are ready to eat.",
            "Pre-made burger patties freeze individually between parchment paper.",
            "Marinated proteins absorb flavor in the fridge and cook in minutes.",
            "Taco fillings prep in large batches and serve differently each night.",
            "One batch of taco meat becomes tacos, burritos, nachos, and salad toppings.",
            "Pasta sauces freeze in portions for instant homemade Italian dinners.",
            "Pre-formed meatballs freeze on sheet pans then transfer to bags.",
            "The goal is getting a home-cooked dinner on the table in under fifteen minutes.",
        ]),
        ("Chapter 11: Snack Prep Ideas", [
            "Wash and cut fruit into grab-and-go portions in clear containers.",
            "Pre-portion nuts and trail mix into small bags for calorie control.",
            "Cut vegetables like carrots, celery, and peppers with hummus for dipping.",
            "Hard-boiled eggs make for a high-protein snack that lasts five days.",
            "Energy balls combine oats, nut butter, and honey with no baking required.",
            "Make a batch of twenty energy balls and freeze for up to three months.",
            "Homemade popcorn seasons in bulk and portions into bags cheaply.",
            "String cheese, yogurt cups, and deli meat roll-ups need no prep at all.",
            "Pre-made protein boxes with crackers, cheese, and fruit satisfy any craving.",
            "Apple slices with individual peanut butter cups are kid and adult friendly.",
            "Having healthy snacks ready prevents reaching for chips and candy.",
            "Snack prep takes only fifteen minutes and lasts the entire week.",
        ]),
        ("Chapter 12: Meal Prep for One Person", [
            "Solo meal prep is actually easier because you only have your preferences.",
            "Cook one protein, one grain, and two vegetables for simple mix-and-match meals.",
            "Freeze half of everything you make so you always have backup meals.",
            "Single-serve freezer meals prevent waste and provide instant variety.",
            "Use smaller containers to avoid the temptation to overeat large portions.",
            "Cook a whole chicken on Sunday for proteins throughout the entire week.",
            "Repurpose leftovers creatively: Monday roast chicken becomes Wednesday stir-fry.",
            "Invest in a smaller slow cooker designed for one to two servings.",
            "Sheet pan meals for one use a quarter pan size perfectly.",
            "Freeze individual soup portions in muffin tins then pop into bags.",
            "Single meal prep typically takes only sixty to ninety minutes per week.",
            "You deserve home-cooked meals even when cooking just for yourself.",
        ]),
        ("Chapter 13: Meal Prep for Families", [
            "Get family input on the weekly menu so everyone looks forward to meals.",
            "Prep base ingredients that can be customized for picky eaters.",
            "Taco bars, bowl bars, and sandwich stations let everyone build their own.",
            "Double recipes since it takes the same time but yields twice the food.",
            "Assign age-appropriate prep tasks to children to teach them cooking skills.",
            "Keep a family favorites list and rotate them to avoid complaints.",
            "Prep school lunches assembly-line style for the entire week on Sunday.",
            "Use a large slow cooker or Instant Pot to handle family-sized portions.",
            "Freeze kid-friendly meals like mac and cheese, meatballs, and chicken tenders.",
            "Label kids containers with their names and the day to grab easily.",
            "Plan at least one family cooking session per week for bonding time.",
            "Family meal prep saves the average household over two hundred dollars monthly.",
        ]),
        ("Chapter 14: Common Mistakes", [
            "Mistake one: prepping too much food that goes bad before you eat it.",
            "Start small with three to four meals and increase as you find your rhythm.",
            "Mistake two: making the same boring meals every single week.",
            "Rotate recipes and try one new dish weekly to keep things interesting.",
            "Mistake three: not seasoning food well because healthy does not mean bland.",
            "Mistake four: skipping the cooling step and putting hot food in the fridge.",
            "Mistake five: not investing in quality containers that seal properly.",
            "Mistake six: overcomplicating recipes instead of keeping meals simple.",
            "Mistake seven: prepping foods that do not reheat or store well.",
            "Avoid prepping fried foods, dressed salads, and crispy items in advance.",
            "Mistake eight: trying to prep every meal instead of just the hardest ones.",
            "Learn from mistakes and adjust your system. Perfection is not the goal.",
        ]),
        ("Chapter 15: Your First Week Meal Prep Plan", [
            "Saturday: Write your menu, make your grocery list, and go shopping.",
            "Sunday morning: Start the slow cooker with a big batch of shredded chicken.",
            "Sunday mid-morning: Put a large pot of rice or quinoa on the stovetop.",
            "While grains cook: wash and chop all vegetables for the week.",
            "Roast two sheet pans of mixed vegetables (broccoli, peppers, sweet potatoes).",
            "Make a batch of overnight oats in five mason jars for weekday breakfasts.",
            "Hard-boil a dozen eggs for quick breakfasts and snacks throughout the week.",
            "Portion shredded chicken into five containers with rice and roasted vegetables.",
            "Assemble three mason jar salads for midweek lunches.",
            "Make a big pot of soup and freeze half in individual portions.",
            "Cut fruit and vegetables for snack containers.",
            "Total time: approximately two and a half hours for twenty-plus meals and snacks.",
        ]),
    ]

    page_num = 1
    for title, lines in chapters:
        pdf.new_page()
        pdf.add_centered_text(600, title, font='F2', size=16)
        pdf.add_line(60, 585, 372, 585, 1)
        y = 560
        for line in lines:
            pdf.add_text(50, y, line, font='F4', size=11)
            y -= 22
        pdf.add_centered_text(30, str(page_num), font='F1', size=10)
        page_num += 1

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book63_How_To_Meal_Prep.pdf')
    print("Book 63 created: Book63_How_To_Meal_Prep.pdf")

if __name__ == '__main__':
    create_book()
