from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    recipes = {
        "Breakfast": [
            ("Fluffy Scrambled Eggs","**","10 min","2",["3 eggs","1 tbsp butter","2 tbsp milk","Salt and pepper","Optional: cheese"],["Crack eggs into bowl, add milk, whisk well","Heat butter in pan on medium-low","Pour in eggs, let sit 30 seconds","Gently push eggs with spatula, folding softly","Remove from heat while still slightly wet","Season and serve immediately"],"Eggs are packed with protein to fuel your morning brain!"),
            ("Banana Pancakes (3 ingredients!)","*","15 min","2",["2 ripe bananas","2 eggs","1/2 cup oats (optional)","Cinnamon","Cooking spray"],["Mash bananas in a bowl until smooth","Whisk in eggs (and oats if using)","Sprinkle in cinnamon","Heat pan with cooking spray on medium","Pour small circles, cook 2 min each side","Serve with fruit on top"],"Bananas provide natural sweetness without added sugar!"),
            ("Overnight Oats","*","5 min prep","1",["1/2 cup oats","1/2 cup milk","1 tbsp honey","1/4 cup yogurt","Fruit toppings"],["Mix oats, milk, yogurt, and honey in a jar","Stir well until combined","Cover and refrigerate overnight (8+ hours)","In the morning, add fresh fruit on top","Eat cold or microwave 1 minute","Enjoy a ready-made breakfast!"],"Oats are whole grains with fiber that keeps you full until lunch!"),
            ("Fruit Smoothie Bowl","*","5 min","1",["1 frozen banana","1/2 cup berries","1/4 cup yogurt","Splash of milk","Toppings: granola, seeds, fruit"],["Blend frozen banana, berries, yogurt, and milk","Blend until thick and creamy (not too liquid)","Pour into a bowl (should be spoonable)","Arrange toppings in rows on top","Add granola, sliced fruit, seeds","Eat with a spoon - don't drink!"],"Frozen fruit makes it thick like ice cream but much healthier!"),
            ("Avocado Toast","*","5 min","1",["1 ripe avocado","2 slices bread","Lemon juice","Salt, pepper, red pepper flakes","Optional: egg on top"],["Toast bread until golden and crispy","Cut avocado in half, remove pit","Scoop avocado onto toast","Mash with fork, leaving some chunks","Squeeze lemon juice, add salt and spices","Add a fried egg on top for extra protein"],"Avocados have healthy fats that help your brain develop!"),
            ("Yogurt Parfait","*","5 min","1",["1 cup yogurt","1/4 cup granola","Mixed berries","1 tbsp honey","Optional: chia seeds"],["Spoon yogurt layer into glass or bowl","Add a layer of berries","Sprinkle granola on top","Drizzle with honey","Repeat layers if glass is tall","Top with a few chia seeds"],"Layering makes eating healthy feel fancy and fun!"),
            ("French Toast Sticks","**","15 min","2",["4 bread slices","2 eggs","1/4 cup milk","Cinnamon and vanilla","Butter for cooking"],["Cut bread slices into 3 strips each","Whisk eggs, milk, cinnamon, and vanilla","Dip bread strips in egg mixture","Cook in buttered pan 2 min per side","Cook until golden all over","Serve with maple syrup for dipping"],"Using whole wheat bread adds fiber and nutrients!"),
            ("Breakfast Quesadilla","**","10 min","1",["1 tortilla","2 eggs (scrambled)","1/4 cup cheese","Salsa","Optional: beans"],["Scramble eggs in a pan, set aside","Place tortilla in clean pan on medium","Sprinkle cheese on half the tortilla","Add scrambled eggs on cheese","Fold tortilla in half, press gently","Cook 2 min each side until crispy, serve with salsa"],"Combining protein (eggs) and carbs (tortilla) gives lasting energy!"),
            ("Cinnamon Apple Oatmeal","*","10 min","1",["1 cup oats","2 cups water","1 apple (diced)","Cinnamon","Honey and walnuts"],["Bring water to boil, add oats","Stir and reduce heat to medium-low","Add diced apple and cinnamon","Cook 5 minutes, stirring occasionally","Remove from heat, add honey","Top with walnuts for crunch"],"Apples add natural sweetness and fiber to your oatmeal!"),
            ("Egg Muffin Cups","**","25 min","6",["6 eggs","1/4 cup milk","Diced veggies (peppers, spinach)","Cheese","Salt and pepper"],["Preheat oven to 350F (adult help with oven)","Grease a muffin tin with cooking spray","Whisk eggs and milk together","Divide veggies into muffin cups","Pour egg mixture over veggies","Bake 20 minutes until set. Cool 5 min."],"Make on Sunday, reheat all week - meal prep like a pro!"),
        ],
        "Lunch": [
            ("Rainbow Wraps","*","10 min","2",["2 large tortillas","Hummus","Shredded carrots, lettuce","Sliced cucumber, bell pepper","Cheese or turkey"],["Spread hummus across entire tortilla","Layer vegetables in a rainbow of colors","Add cheese or turkey if desired","Roll tightly, tucking in the sides","Cut in half diagonally","Wrap in foil for lunch box"],"Eating colorful veggies means getting different vitamins!"),
            ("Homemade Pizza Bagels","**","15 min","4",["4 bagel halves","Pizza sauce","Mozzarella cheese","Toppings: pepperoni, veggies","Italian seasoning"],["Preheat oven to 375F (adult help)","Place bagel halves on baking sheet","Spread sauce on each bagel","Add cheese and your favorite toppings","Sprinkle Italian seasoning","Bake 10-12 min until cheese melts"],"Making pizza at home lets you control ingredients and portions!"),
            ("Chicken Salad Sandwich","**","10 min","2",["1 can chicken (drained)","2 tbsp mayo or yogurt","Diced celery and grapes","Salt and pepper","Bread or crackers"],["Drain chicken and place in bowl","Add mayo/yogurt, celery, and halved grapes","Mix well with fork, mashing slightly","Season with salt and pepper","Spread on bread or scoop with crackers","Add lettuce for extra crunch"],"Chicken provides lean protein for growing muscles!"),
            ("Ants on a Log (Upgraded)","*","5 min","1",["Celery stalks","Peanut butter","Raisins","Optional: sunflower seeds","Optional: cream cheese version"],["Wash celery and cut into 4-inch pieces","Fill the celery groove with peanut butter","Place raisins in a row on top (the 'ants')","Try variations: cream cheese + dried cranberries","Or sunflower seed butter + chocolate chips","Arrange on plate and enjoy!"],"Celery is 95% water - super hydrating snack!"),
            ("Quesadilla with Beans","**","10 min","1",["1 large tortilla","Canned black beans (rinsed)","Cheese","Salsa and sour cream","Optional: corn, peppers"],["Heat pan on medium","Place tortilla in pan","Spread beans and cheese on half","Fold tortilla over","Cook 2-3 min each side until golden","Cut into triangles, serve with salsa"],"Beans are a superfood: protein, fiber, and iron!"),
            ("Pasta Salad","**","20 min","4",["2 cups cooked pasta (cooled)","Cherry tomatoes (halved)","Cucumber (diced)","Italian dressing","Cheese cubes, olives"],["Cook pasta according to package (adult help with boiling)","Rinse with cold water to cool","Chop vegetables into bite-size pieces","Combine everything in a large bowl","Add dressing and toss well","Chill 30 min for best flavor"],"Cold pasta salad is perfect for meal prep and lunch boxes!"),
            ("Mini Sandwiches (Sliders)","*","10 min","4",["Dinner rolls (4)","Deli meat or cheese","Lettuce, tomato","Mustard or mayo","Pickles"],["Slice rolls in half horizontally","Spread mustard or mayo on bottom halves","Layer meat, cheese, lettuce, tomato","Add pickle slices if desired","Place top halves on","Secure with toothpicks if needed"],"Smaller portions help you not overeat at lunch!"),
            ("Veggie Fried Rice","**","15 min","2",["2 cups leftover rice (cold)","2 eggs","Frozen mixed veggies","Soy sauce","Sesame oil"],["Heat sesame oil in large pan or wok","Add frozen veggies, cook 3 minutes","Push veggies to side, scramble eggs in pan","Add cold rice, stir everything together","Add soy sauce (2 tbsp) and stir well","Cook 3 more minutes until rice is hot"],"Using leftover rice prevents food waste AND tastes better!"),
            ("Tomato Soup & Grilled Cheese","**","20 min","2",["1 can tomato soup","Bread (4 slices)","Butter","Cheese slices","Milk (for soup)"],["Heat soup with milk in pot (follow can directions)","Butter outsides of bread slices","Place cheese between 2 bread slices","Cook in pan on medium 3 min per side","Cut diagonally into triangles","Serve soup in mug, dip sandwich in!"],"This classic combo provides calcium, lycopene, and carbs!"),
            ("Tuna Salad Stuffed Tomato","**","10 min","2",["1 can tuna (drained)","Mayo or yogurt","Diced celery and onion","2 large tomatoes","Salt, pepper, lemon"],["Drain tuna and mix with mayo in bowl","Add diced celery and onion","Season with salt, pepper, lemon juice","Cut tops off tomatoes, scoop out seeds","Fill tomatoes with tuna mixture","Serve on lettuce leaves"],"Tuna is rich in omega-3 fatty acids for brain health!"),
        ],
        "Snacks": [
            ("Trail Mix","*","5 min","4",["Mixed nuts","Raisins or dried fruit","Dark chocolate chips","Pretzels","Coconut flakes"],["Measure equal portions of each ingredient","Pour all into a large bowl","Toss and mix well","Divide into small bags or containers","Store for grab-and-go snacking","Customize with your favorites!"],"Nuts provide healthy fats and protein for sustained energy!"),
            ("Apple Nachos","*","5 min","2",["2 apples (sliced thin)","Peanut butter (melted)","Granola","Mini chocolate chips","Honey drizzle"],["Slice apples and arrange on a plate","Microwave peanut butter 15 sec to thin it","Drizzle peanut butter over apples","Sprinkle granola and chocolate chips","Drizzle honey on top","Share and eat immediately!"],"Apples have fiber, PB has protein - a perfect combination!"),
            ("Frozen Yogurt Bites","*","5 min + freeze","lots",["Yogurt","Berries or fruit pieces","Parchment paper","Baking sheet"],["Line baking sheet with parchment paper","Drop small spoonfuls of yogurt","Press a berry into each yogurt drop","Freeze for 2+ hours until solid","Pop off parchment and store in freezer bag","Eat frozen as a cold treat!"],"Frozen yogurt bites satisfy sweet cravings with probiotics!"),
            ("Hummus & Veggie Sticks","*","5 min","2",["Store-bought or homemade hummus","Carrot sticks","Cucumber slices","Bell pepper strips","Pita chips"],["Wash and cut vegetables into sticks","Arrange veggies around a bowl of hummus","Include pita chips for variety","Dip and enjoy!","Try different hummus flavors","Store extra veggies in water to keep crisp"],"Hummus is made from chickpeas - full of protein and fiber!"),
            ("Energy Balls (No Bake)","**","15 min","12",["1 cup oats","1/2 cup peanut butter","1/3 cup honey","1/2 cup chocolate chips","Optional: flax seeds"],["Mix all ingredients in a large bowl","Stir until completely combined","Refrigerate mixture 15 minutes","Roll into 1-inch balls with your hands","Place on parchment paper","Store in fridge for up to 1 week"],"No-bake means no oven needed - safe and easy!"),
            ("Frozen Banana Pops","*","10 min + freeze","4",["2 bananas","Popsicle sticks","Melted chocolate","Toppings: sprinkles, nuts, coconut","Parchment paper"],["Cut bananas in half crosswise","Insert popsicle stick in each half","Freeze bananas 1 hour until firm","Dip in melted chocolate (microwave)","Roll in toppings immediately","Freeze 30 more min, then enjoy!"],"Frozen bananas have a creamy texture like ice cream!"),
            ("Popcorn 3 Ways","*","5 min","2",["Popcorn (air-popped or microwave)","Option 1: cinnamon + sugar","Option 2: parmesan + garlic powder","Option 3: cocoa powder + sugar"],["Pop popcorn (adult help if using stove)","Divide into 3 bowls","Add different seasonings to each","Toss well to coat evenly","Taste-test all three versions","Vote on your family's favorite!"],"Air-popped popcorn is a whole grain with lots of fiber!"),
            ("Ants on a Raft","*","5 min","2",["Crackers","Cream cheese or PB","Raisins","Pretzel sticks","Celery optional"],["Spread cream cheese on crackers (the raft)","Place raisins on top (the ants)","Stick pretzel sticks as oars","Make different designs on each cracker","Create a whole fleet of rafts!","Eat your edible art"],"Making food fun makes healthy snacking enjoyable!"),
            ("Smoothie Popsicles","*","5 min + freeze","6",["Blended smoothie (any flavor)","Popsicle molds","Fruit chunks","Yogurt","Juice"],["Blend your favorite smoothie","Pour into popsicle molds","Drop in fruit chunks","Insert sticks","Freeze 4+ hours until solid","Run warm water on mold to release"],"Popsicles from real fruit are so much healthier than store-bought!"),
            ("Cheese & Crackers Board","*","10 min","4",["Various cheeses (cubed)","Crackers (2-3 types)","Grapes and berries","Sliced apples","Honey for drizzling"],["Arrange cheeses on a board or plate","Fan out different crackers","Add clusters of grapes and berries","Arrange apple slices (dip in lemon water first)","Drizzle honey in a small bowl","Make it look beautiful!"],"A balanced snack board has protein, carbs, and fruit!"),
        ],
        "Dinner Helpers": [
            ("Simple Salad","*","10 min","4",["Mixed greens","Cherry tomatoes","Cucumber","Shredded carrots","Your favorite dressing"],["Wash all vegetables thoroughly","Tear lettuce into bite-size pieces","Halve cherry tomatoes","Slice cucumber into rounds","Toss everything in a large bowl","Add dressing just before serving"],"Eating salad before dinner fills you with nutrients first!"),
            ("Garlic Bread","**","10 min","4",["French bread or baguette","Butter (softened)","Garlic powder or minced garlic","Parsley","Parmesan (optional)"],["Preheat oven to 375F (adult help)","Slice bread in half lengthwise","Mix softened butter with garlic and parsley","Spread mixture on bread halves","Sprinkle parmesan if desired","Bake 8-10 min until golden and crispy"],"Garlic has natural antibacterial properties!"),
            ("Steamed Vegetables","*","10 min","4",["Broccoli florets","Carrots (sliced)","Snap peas","Salt and butter","Steamer basket or microwave"],["Cut vegetables into similar sizes","Place in steamer basket over boiling water","Or microwave with 2 tbsp water, covered, 3-4 min","Steam until tender but still bright colored","Season with a little butter and salt","Don't overcook - crunchy is healthier!"],"Steaming preserves more vitamins than boiling!"),
            ("Mashed Potatoes","**","25 min","4",["4 potatoes (peeled, cubed)","1/4 cup milk","2 tbsp butter","Salt and pepper","Optional: cheese, chives"],["Peel and cube potatoes (adult help with peeling)","Boil in salted water 15-20 min until fork-tender","Drain water carefully (adult help)","Add butter and milk","Mash with potato masher until smooth","Season and add toppings"],"Potatoes are high in potassium and vitamin C!"),
            ("Stir-Fry Vegetables","**","15 min","4",["Mixed veggies (bell peppers, broccoli, snap peas)","2 tbsp soy sauce","1 tbsp oil","Garlic (minced)","Optional: sesame seeds"],["Cut all veggies into similar small pieces","Heat oil in large pan on medium-high","Add garlic, cook 30 seconds","Add firm veggies first (carrots, broccoli)","After 3 min add softer veggies","Add soy sauce, cook 2 more min"],"Stir-frying is quick, keeping veggies crisp and nutritious!"),
            ("Rice (Perfect Every Time)","*","20 min","4",["1 cup rice","2 cups water","Pinch of salt","1 tsp butter (optional)"],["Rinse rice under cold water until water runs clear","Add rice, water, and salt to pot","Bring to boil, then reduce to lowest heat","Cover with lid - DO NOT OPEN for 18 minutes","Turn off heat, let sit 5 min (still covered)","Fluff with fork and serve"],"Rice feeds more people worldwide than any other food!"),
            ("Simple Taco Filling","**","15 min","4",["1 can black beans (rinsed)","1 cup corn","Taco seasoning","Diced tomatoes","Lime juice"],["Heat beans and corn in pan","Add taco seasoning and a splash of water","Cook 5 minutes until heated through","Squeeze lime juice on top","Serve in taco shells with toppings","Add cheese, lettuce, salsa, sour cream"],"Bean tacos are cheaper AND healthier than meat tacos!"),
            ("Caprese Skewers","*","10 min","8",["Cherry tomatoes","Mozzarella balls (small)","Fresh basil leaves","Toothpicks or small skewers","Balsamic glaze"],["Thread a tomato onto skewer","Add a basil leaf, folded","Add a mozzarella ball","Repeat pattern on each skewer","Arrange on a plate","Drizzle balsamic glaze before serving"],"This Italian appetizer takes minutes but looks impressive!"),
            ("Corn on the Cob","*","10 min","4",["4 ears of corn","Butter","Salt","Optional: chili powder, lime","Large pot of water"],["Shuck corn (remove husks and silk)","Bring large pot of water to boil (adult help)","Add corn to boiling water","Boil 5-7 minutes until tender","Remove carefully with tongs","Add butter, salt, and optional seasonings"],"Corn is a whole grain and good source of fiber!"),
            ("Fruit Salad Dessert","*","10 min","4",["Strawberries","Blueberries","Grapes","Banana","Honey-lime dressing"],["Wash and cut all fruit into bite-size pieces","Combine in a large bowl","Mix 2 tbsp honey with juice of 1 lime","Pour dressing over fruit","Toss gently to coat","Serve immediately or chill 30 min"],"A rainbow of fruits means a variety of vitamins and antioxidants!"),
        ],
    }

    title_page(doc, "KIDS IN THE KITCHEN", "40 Easy & Healthy Recipes You Can Make (Ages 8-14)", "40 Recipes * Safety Tips * Nutrition Facts * Meal Planning")
    copyright_page(doc, "KIDS IN THE KITCHEN: 40 Easy & Healthy Recipes")
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0)
    y = 680
    doc.add_text(72, y, "Kitchen Safety Rules", 'F4', 12, 0.2); y -= 25
    doc.add_text(72, y, "Equipment Guide", 'F4', 12, 0.2); y -= 25
    doc.add_text(72, y, "Measurement Basics", 'F4', 12, 0.2); y -= 25
    for cat in recipes:
        doc.add_text(72, y, f"{cat} Recipes (10)", 'F2', 13, 0.1); y -= 25
    doc.new_page()

    # Safety page
    doc.add_centered_text(720, "KITCHEN SAFETY RULES", 'F2', 18, 0)
    rules = ["Always ask permission before cooking","Wash hands before and after handling food","Use oven mitts for anything hot","Keep handles turned inward on the stove","Never leave cooking food unattended","Clean up spills immediately (slippery!)","Ask an adult to help with sharp knives","Keep water away from hot oil","Know where the fire extinguisher is","When in doubt, ask an adult for help!"]
    y = 680
    for i, r in enumerate(rules):
        doc.add_text(72, y, f"{i+1}. {r}", 'F1', 12, 0.2)
        y -= 30
    doc.new_page()

    # Measurements
    doc.add_centered_text(720, "MEASUREMENT BASICS", 'F2', 18, 0)
    measures = ["1 tablespoon (tbsp) = 3 teaspoons (tsp)","1 cup = 16 tablespoons","1 cup = 8 fluid ounces","1 pint = 2 cups","1 quart = 4 cups","Pinch = what you can grab between 2 fingers","Dash = a quick shake","To measure flour: spoon into cup, level with knife","To measure liquids: use clear measuring cup at eye level","Abbreviations: tsp=teaspoon, tbsp=tablespoon, oz=ounce"]
    y = 680
    for m in measures:
        doc.add_text(72, y, f"* {m}", 'F1', 11, 0.2)
        y -= 28
    doc.new_page()

    recipe_num = 0
    for cat_name, cat_recipes in recipes.items():
        doc.add_filled_rect(50, 380, 512, 100, 0.9)
        doc.add_centered_text(440, cat_name.upper(), 'F2', 22, 0)
        doc.new_page()
        
        for name, diff, time, servings, ingredients, steps, tip in cat_recipes:
            recipe_num += 1
            doc.add_text(72, 730, f"RECIPE #{recipe_num}", 'F1', 10, 0.4)
            doc.add_text(72, 710, name, 'F2', 16, 0)
            doc.add_line(72, 702, 350, 702, 1, 0.3)
            
            doc.add_text(72, 682, f"Difficulty: {diff}", 'F1', 10, 0.3)
            doc.add_text(200, 682, f"Time: {time}", 'F1', 10, 0.3)
            doc.add_text(330, 682, f"Serves: {servings}", 'F1', 10, 0.3)
            
            y = 655
            doc.add_text(72, y, "INGREDIENTS:", 'F2', 11, 0.1)
            y -= 16
            for ing in ingredients:
                doc.add_text(90, y, f"[ ] {ing}", 'F1', 9, 0.2)
                y -= 14
            
            y -= 10
            doc.add_text(72, y, "DIRECTIONS:", 'F2', 11, 0.1)
            y -= 16
            for i, step in enumerate(steps):
                lines = wrap(step, 65)
                for j, l in enumerate(lines):
                    if y < 80:
                        doc.new_page()
                        y = 720
                    prefix = f"{i+1}. " if j == 0 else "   "
                    doc.add_text(90, y, f"{prefix}{l}", 'F1', 9, 0.2)
                    y -= 14
            
            y -= 12
            if y < 100:
                doc.new_page()
                y = 720
            doc.add_filled_rect(60, y-5, 492, 22, 0.95)
            doc.add_text(72, y, f"NUTRITION TIP: {tip}", 'F4', 9, 0.2)
            doc.new_page()

    # Meal planning & grocery list
    doc.add_centered_text(720, "MY WEEKLY MEAL PLAN", 'F2', 16, 0)
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    y = 685
    for day in days:
        doc.add_text(72, y, f"{day}: B________ L________ S________ D________", 'F1', 10, 0.3)
        y -= 25
    doc.new_page()

    doc.add_centered_text(720, "GROCERY LIST", 'F2', 16, 0)
    y = 690
    cols = [("Produce",72),("Dairy/Protein",250),("Pantry",430)]
    for name, x in cols:
        doc.add_text(x, y, name, 'F2', 11, 0.1)
    y -= 20
    for _ in range(15):
        for _, x in cols:
            doc.add_text(x, y, "[ ] _______________", 'F1', 9, 0.4)
        y -= 18
    doc.new_page()

    certificate(doc, "JUNIOR CHEF CERTIFICATE")
    add_supplemental(doc, 'Cooking', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book337_Kids_Cooking_Guide.pdf')
    print("Book337_Kids_Cooking_Guide.pdf created successfully!")

if __name__ == "__main__":
    create_book()
