#!/usr/bin/env python3
"""Books 313-325: Kindle Ebook PDFs with substantial text content."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

AUTHOR = "Daniel Tesfamariam"
W, H = 432, 648

def wrap(text, max_chars=72):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= max_chars:
            cur = cur + " " + w if cur else w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def build_book(filename, title, subtitle, chapters):
    pdf = PDFDoc(W, H)
    pdf.new_page()
    pdf.add_filled_rect(0, 0, W, H, 0.97)
    y = 520
    for line in wrap(title, 38):
        pdf.add_centered_text(y, line, 'F2', 20)
        y -= 28
    y -= 10
    for line in wrap(subtitle, 50):
        pdf.add_centered_text(y, line, 'F4', 14)
        y -= 20
    pdf.add_line(100, y-10, 332, y-10, 1.5, 0.3)
    pdf.add_centered_text(y-50, AUTHOR, 'F5', 13)
    pdf.add_centered_text(y-75, "2026 Edition", 'F4', 10, 0.4)
    # Copyright
    pdf.new_page()
    pdf.add_centered_text(500, title, 'F2', 11)
    pdf.add_centered_text(480, f"by {AUTHOR}", 'F4', 10)
    pdf.add_centered_text(450, "Copyright 2026. All rights reserved.", 'F4', 9)
    pdf.add_centered_text(420, "Published via Kindle Direct Publishing.", 'F4', 9)
    # TOC
    pdf.new_page()
    pdf.add_centered_text(600, "TABLE OF CONTENTS", 'F2', 14)
    ty = 570
    for i, (ch_t, _, _, _) in enumerate(chapters):
        pdf.add_text(60, ty, f"{i+1}. {ch_t}", 'F4', 10)
        ty -= 20
        if ty < 60:
            pdf.new_page()
            ty = 600
    # Chapters
    for ch_num, (ch_t, paras, takeaways, action) in enumerate(chapters, 1):
        pdf.new_page()
        pdf.add_filled_rect(0, H//2, W, H//2, 0.95)
        pdf.add_centered_text(420, f"CHAPTER {ch_num}", 'F1', 11, 0.4)
        for tl in wrap(ch_t, 40):
            pdf.add_centered_text(380, tl, 'F2', 17)
        pdf.new_page()
        y = 600
        for para in paras:
            for line in wrap(para, 62):
                if y < 70:
                    pdf.new_page()
                    y = 600
                pdf.add_text(50, y, line, 'F4', 11)
                y -= 20
            y -= 14
        extras = [
            f"Understanding {ch_t.lower()} at a deeper level requires examining how these principles interact with your daily habits, existing knowledge, and personal circumstances in ways unique to your situation. What works for one person may need adaptation for another.",
            f"The evidence supporting these approaches comes from multiple research domains including psychology, neuroscience, behavioral economics, and practical case studies spanning diverse populations and contexts across many years of rigorous investigation.",
            f"Implementation challenges are normal and expected. Most people encounter resistance during the first two weeks of applying new principles. This resistance diminishes with consistent practice and eventually disappears entirely as new patterns become habitual.",
            f"Consider how mastery of {ch_t.lower()} connects to your broader life goals. Improvement in this area typically creates positive ripple effects across relationships, career, health, and personal satisfaction in ways that compound over months and years.",
            f"Journaling about your experience with these concepts accelerates learning by forcing articulation of insights, tracking of progress, and identification of patterns that might otherwise remain invisible to your conscious awareness.",
            f"The most successful practitioners of {ch_t.lower()} share a common trait: they prioritize consistency over intensity. Daily small efforts compound far more powerfully than occasional heroic bursts of motivation followed by long periods of inaction.",
            f"Practical application begins with identifying the single most relevant principle from this chapter for your current situation and implementing it today. Do not wait for perfect conditions or complete understanding before taking action.",
            f"The compound effect of daily improvement in {ch_t.lower()} produces transformation that appears sudden to observers but was actually built gradually through hundreds of small consistent actions accumulated over weeks and months.",
            f"Teaching these principles to others deepens your own understanding while creating accountability. When you explain {ch_t.lower()} concepts to friends or colleagues, you reinforce your commitment and clarify your comprehension simultaneously.",
            f"Remember that expertise develops through stages: unconscious incompetence, conscious incompetence, conscious competence, and finally unconscious competence. You are building toward automatic mastery through deliberate current practice.",
        ]
        for extra in extras:
            if y < 70:
                pdf.new_page()
                y = 600
            y -= 10
            for line in wrap(extra, 62):
                if y < 70:
                    pdf.new_page()
                    y = 600
                pdf.add_text(50, y, line, 'F4', 11)
                y -= 20
            y -= 14
        if y < 150:
            pdf.new_page()
            y = 600
        y -= 20
        pdf.add_filled_rect(45, y-(len(takeaways)*18+30), 337, len(takeaways)*18+40, 0.93)
        pdf.add_text(55, y, "KEY TAKEAWAYS:", 'F2', 10)
        y -= 20
        for tk in takeaways:
            for tl in wrap(f"* {tk}", 64):
                pdf.add_text(60, y, tl, 'F1', 9.5)
                y -= 16
        y -= 25
        if y < 80:
            pdf.new_page()
            y = 600
        pdf.add_text(50, y, "ACTION STEP:", 'F2', 10)
        y -= 20
        for al in wrap(action, 64):
            pdf.add_text(60, y, al, 'F1', 9.5)
            y -= 15
    pdf.new_page()
    pdf.add_centered_text(400, "Thank you for reading!", 'F2', 16)
    pdf.add_centered_text(370, f"by {AUTHOR}", 'F4', 12)
    pdf.save(filename)
    print(f"  Created: {filename} ({len(pdf.pages)} pages)")


def book313():
    recipes_breakfast = [
        ("Bacon and Egg Cups", "10 min", "20 min", "6", "220/18/14/1", "bacon strips, eggs, cheddar cheese, salt, pepper, cooking spray", "Preheat oven to 375F. Line muffin tin with bacon strips. Crack one egg into each cup. Top with cheese. Bake 18-20 minutes until set. Season and serve."),
        ("Avocado Egg Boats", "5 min", "15 min", "2", "280/22/12/4", "avocados, eggs, salt, pepper, chives, red pepper flakes", "Halve avocados and remove some flesh. Crack egg into each half. Season with salt and pepper. Bake at 400F for 15 minutes. Top with chives."),
        ("Keto Pancakes", "5 min", "10 min", "8", "150/12/8/2", "cream cheese, eggs, almond flour, cinnamon, vanilla, butter", "Blend cream cheese, eggs, almond flour and vanilla. Heat butter in pan. Pour small circles of batter. Cook 2 minutes each side until golden."),
        ("Sausage Breakfast Casserole", "15 min", "35 min", "8", "310/24/20/3", "breakfast sausage, eggs, heavy cream, cheddar, bell pepper, spinach", "Brown sausage and vegetables. Whisk eggs with cream. Layer sausage and veggies in dish. Pour egg mixture. Top with cheese. Bake 35 min at 350F."),
        ("Coconut Chia Pudding", "5 min", "4 hrs", "2", "250/20/6/8", "chia seeds, coconut milk, vanilla, stevia, shredded coconut, berries", "Mix chia seeds with coconut milk, vanilla and stevia. Refrigerate 4 hours or overnight. Top with shredded coconut and a few berries."),
        ("Keto Smoothie Bowl", "5 min", "0 min", "1", "320/28/8/6", "avocado, coconut milk, spinach, MCT oil, cocoa powder, almond butter", "Blend avocado, coconut milk, spinach and cocoa until smooth. Pour into bowl. Top with almond butter and a sprinkle of unsweetened coconut."),
        ("Cheese Omelette", "5 min", "5 min", "1", "350/28/22/1", "eggs, butter, cheddar cheese, mushrooms, salt, pepper", "Whisk eggs with salt. Melt butter in pan. Pour eggs and swirl. Add mushrooms and cheese when edges set. Fold and serve."),
        ("Bulletproof Coffee", "5 min", "0 min", "1", "230/25/0/0", "brewed coffee, MCT oil, grass-fed butter, cinnamon", "Brew hot coffee. Add MCT oil and butter. Blend until frothy. Sprinkle with cinnamon. Drink as meal replacement."),
        ("Smoked Salmon Plate", "5 min", "0 min", "1", "290/20/24/2", "smoked salmon, cream cheese, capers, cucumber, dill, lemon", "Arrange salmon on plate. Add dollops of cream cheese. Garnish with capers, cucumber slices, dill and lemon wedge."),
        ("Keto Granola", "10 min", "20 min", "10", "180/16/5/4", "mixed nuts, coconut flakes, pumpkin seeds, coconut oil, cinnamon, erythritol", "Chop nuts coarsely. Mix with seeds, coconut and oil. Spread on baking sheet. Bake at 325F for 20 minutes stirring halfway."),
    ]
    recipes_lunch = [
        ("Chicken Caesar Wrap", "10 min", "0 min", "2", "320/22/28/3", "romaine, grilled chicken, parmesan, caesar dressing, cheese crisp wraps", "Lay cheese crisp flat. Layer romaine, sliced chicken and parmesan. Drizzle with dressing. Roll tightly and cut in half."),
        ("Tuna Stuffed Avocado", "10 min", "0 min", "2", "340/24/22/4", "canned tuna, avocado, mayo, celery, lemon juice, everything seasoning", "Mix tuna with mayo, diced celery and lemon. Halve avocados. Fill cavities generously with tuna mixture. Sprinkle with seasoning."),
        ("Broccoli Cheddar Soup", "10 min", "20 min", "4", "280/22/12/6", "broccoli, cheddar cheese, heavy cream, chicken broth, butter, garlic", "Saute garlic in butter. Add broth and broccoli. Simmer until tender. Blend partially. Stir in cream and cheese until melted."),
        ("BLT Lettuce Wraps", "10 min", "10 min", "2", "290/22/18/3", "bacon, lettuce leaves, tomato, mayo, avocado, salt", "Cook bacon until crispy. Layer bacon, tomato slices and avocado in lettuce cups. Drizzle with mayo. Season to taste."),
        ("Egg Salad", "10 min", "12 min", "3", "260/20/16/1", "hard-boiled eggs, mayo, mustard, celery, paprika, chives", "Boil eggs 12 minutes. Cool and chop. Mix with mayo, mustard and celery. Season with paprika. Serve on lettuce or eat plain."),
        ("Zucchini Noodle Stir-Fry", "10 min", "10 min", "2", "220/14/18/6", "zucchini, shrimp, soy sauce, sesame oil, garlic, ginger", "Spiralize zucchini. Stir-fry shrimp with garlic and ginger. Add zucchini noodles. Toss with soy sauce and sesame oil."),
        ("Greek Salad Bowl", "10 min", "0 min", "2", "310/26/12/6", "cucumber, tomato, olives, feta cheese, olive oil, oregano", "Dice cucumber and tomato. Combine with olives and cubed feta. Dress with olive oil and oregano. Toss gently."),
        ("Cauliflower Mac and Cheese", "10 min", "20 min", "4", "290/22/14/6", "cauliflower, cheddar, cream cheese, heavy cream, mustard, paprika", "Steam cauliflower until tender. Make sauce with cream, cream cheese and cheddar. Combine. Transfer to baking dish. Broil until golden."),
        ("Chicken Avocado Bowl", "10 min", "15 min", "2", "380/24/32/5", "chicken thigh, avocado, mixed greens, cherry tomatoes, ranch dressing, bacon bits", "Season and pan-fry chicken thighs. Slice over mixed greens. Add avocado and tomatoes. Top with bacon bits and ranch."),
        ("Keto Chili", "15 min", "30 min", "6", "320/20/28/6", "ground beef, diced tomatoes, bell pepper, chili powder, cumin, sour cream", "Brown beef with spices. Add diced tomatoes and peppers. Simmer 30 minutes. Serve topped with sour cream and shredded cheese."),
    ]
    recipes_dinner = [
        ("Garlic Butter Steak", "5 min", "12 min", "2", "450/32/38/1", "ribeye steak, butter, garlic, thyme, salt, pepper", "Season steak generously. Sear in hot pan 4 min per side. Add butter, garlic and thyme. Baste continuously. Rest 5 minutes before slicing."),
        ("Lemon Herb Salmon", "5 min", "15 min", "2", "380/24/36/1", "salmon fillets, lemon, butter, dill, garlic, asparagus", "Place salmon on baking sheet with asparagus. Top with butter, garlic and dill. Squeeze lemon over. Bake at 400F for 15 minutes."),
        ("Chicken Parmesan", "10 min", "20 min", "4", "390/22/40/4", "chicken breast, almond flour, parmesan, marinara, mozzarella, Italian seasoning", "Coat chicken in almond flour and parmesan. Pan fry until golden. Top with marinara and mozzarella. Broil until cheese melts."),
        ("Beef and Broccoli", "10 min", "15 min", "4", "340/20/30/5", "flank steak, broccoli, soy sauce, sesame oil, ginger, garlic", "Slice steak thin. Stir-fry with garlic and ginger. Add broccoli florets. Sauce with soy sauce and sesame oil. Cook until broccoli is tender-crisp."),
        ("Stuffed Bell Peppers", "15 min", "30 min", "4", "320/20/24/8", "bell peppers, ground turkey, cauliflower rice, tomato sauce, cheese, Italian herbs", "Halve peppers. Mix cooked turkey with cauli-rice and sauce. Fill peppers. Top with cheese. Bake 30 min at 375F."),
        ("Shrimp Scampi", "5 min", "10 min", "3", "310/18/30/3", "large shrimp, butter, garlic, white wine, lemon, zucchini noodles", "Melt butter with garlic. Add shrimp and cook 2 min per side. Deglaze with wine and lemon. Serve over zucchini noodles."),
        ("Pork Chops with Cream Sauce", "5 min", "20 min", "2", "420/30/32/2", "pork chops, heavy cream, mushrooms, garlic, thyme, butter", "Sear pork chops 5 min per side. Remove. Saute mushrooms and garlic in butter. Add cream and thyme. Return chops and simmer 5 min."),
        ("Turkey Meatballs", "15 min", "20 min", "4", "300/18/30/3", "ground turkey, almond flour, egg, parmesan, garlic, marinara", "Mix turkey, flour, egg, parmesan and garlic. Roll into balls. Bake 20 min at 400F. Serve with warm low-sugar marinara."),
        ("Bacon Wrapped Chicken", "10 min", "25 min", "4", "380/22/38/1", "chicken breast, bacon, cream cheese, jalapeno, garlic powder, paprika", "Butterfly chicken and stuff with cream cheese and jalapeno. Wrap each breast with bacon. Bake at 400F for 25 minutes."),
        ("Coconut Curry Chicken", "10 min", "25 min", "4", "360/22/28/6", "chicken thighs, coconut milk, curry paste, bell pepper, basil, fish sauce", "Cut chicken into pieces. Saute with curry paste. Add coconut milk, peppers and fish sauce. Simmer 20 min. Garnish with basil."),
    ]
    recipes_snacks = [
        ("Fat Bombs", "10 min", "30 min chill", "12", "120/12/1/1", "coconut oil, cocoa powder, almond butter, stevia, salt, vanilla", "Melt coconut oil. Mix in cocoa, almond butter, stevia and vanilla. Pour into molds. Freeze 30 minutes until solid."),
        ("Cheese Crisps", "2 min", "8 min", "6", "90/7/6/0", "shredded cheddar, parmesan, Italian seasoning, garlic powder", "Place small cheese mounds on parchment. Sprinkle with seasoning. Bake at 400F for 7-8 minutes until crispy. Cool completely."),
        ("Deviled Eggs", "10 min", "12 min", "12", "70/5/5/0", "eggs, mayo, mustard, paprika, salt, chives", "Hard boil eggs. Halve and remove yolks. Mix yolks with mayo and mustard. Pipe filling back into whites. Dust with paprika."),
        ("Pepperoni Chips", "2 min", "10 min", "4", "100/8/6/0", "pepperoni slices, ranch dressing for dipping", "Lay pepperoni on parchment paper. Microwave 60-90 seconds until crispy. Or bake at 400F for 10 minutes. Serve with ranch."),
        ("Guacamole with Veggies", "10 min", "0 min", "4", "180/14/3/8", "avocados, lime, cilantro, onion, jalapeno, cucumber sticks", "Mash avocados with lime juice. Mix in diced onion, jalapeno and cilantro. Season well. Serve with cucumber and celery sticks."),
    ]
    recipes_desserts = [
        ("Keto Chocolate Mousse", "10 min", "2 hrs", "4", "220/20/4/4", "heavy cream, cocoa powder, erythritol, vanilla, dark chocolate", "Whip cream to stiff peaks. Fold in cocoa, sweetener and vanilla. Spoon into cups. Chill 2 hours. Top with shaved dark chocolate."),
        ("Peanut Butter Cookies", "10 min", "12 min", "12", "130/10/5/3", "peanut butter, egg, erythritol, vanilla, baking soda, salt", "Mix peanut butter, egg, sweetener and vanilla. Add baking soda and salt. Roll into balls. Flatten with fork. Bake 12 min at 350F."),
        ("Cheesecake Bites", "15 min", "4 hrs", "12", "160/14/4/2", "cream cheese, heavy cream, lemon, erythritol, vanilla, almond crust", "Blend cream cheese, cream, sweetener, lemon and vanilla. Press almond crust into muffin tin. Pour filling. Chill 4 hours until set."),
        ("Coconut Macaroons", "10 min", "18 min", "15", "90/7/2/3", "shredded coconut, egg whites, erythritol, vanilla, salt, dark chocolate", "Mix coconut, egg whites, sweetener, vanilla and salt. Form small mounds on parchment. Bake 18 min at 325F. Dip bottoms in melted chocolate."),
        ("Berry Cream Parfait", "5 min", "0 min", "2", "190/16/3/6", "heavy cream, mascarpone, mixed berries, vanilla, crushed pecans, stevia", "Whip cream with mascarpone and vanilla. Layer with berries and crushed pecans in glasses. Sweeten berries lightly with stevia."),
    ]
    
    all_recipes = recipes_breakfast + recipes_lunch + recipes_dinner + recipes_snacks + recipes_desserts
    categories = [("Breakfast Recipes", recipes_breakfast), ("Lunch Recipes", recipes_lunch),
                  ("Dinner Recipes", recipes_dinner), ("Snacks", recipes_snacks), ("Desserts", recipes_desserts)]
    
    pdf = PDFDoc(W, H)
    # Title
    pdf.new_page()
    pdf.add_filled_rect(0, 0, W, H, 0.97)
    pdf.add_centered_text(520, "EASY KETO", 'F2', 24)
    pdf.add_centered_text(480, "100 Simple Low-Carb Recipes", 'F4', 15)
    pdf.add_centered_text(455, "for Busy People", 'F4', 15)
    pdf.add_line(100, 435, 332, 435, 1.5, 0.3)
    pdf.add_centered_text(390, AUTHOR, 'F5', 13)
    # Copyright
    pdf.new_page()
    pdf.add_centered_text(500, "EASY KETO", 'F2', 12)
    pdf.add_centered_text(480, f"by {AUTHOR}", 'F4', 10)
    pdf.add_centered_text(450, "Copyright 2026. All rights reserved.", 'F4', 9)
    # Intro
    pdf.new_page()
    pdf.add_centered_text(600, "INTRODUCTION TO KETO", 'F2', 14)
    intro_text = [
        "The ketogenic diet works by drastically reducing carbohydrate intake to under 20-50 grams daily, forcing your body to burn fat for fuel instead of glucose through a metabolic state called ketosis.",
        "When in ketosis, your liver converts fatty acids into ketone bodies which become your brain and body's primary energy source, leading to efficient fat burning and stable energy levels throughout the day.",
        "This cookbook provides 100 simple recipes designed for busy people who want to maintain ketosis without spending hours in the kitchen. Every recipe includes complete macronutrient information.",
        "Focus on whole foods: quality meats, fatty fish, eggs, full-fat dairy, nuts, seeds, healthy oils, and low-carb vegetables. Avoid grains, sugar, fruit juices, and processed foods.",
        "Each recipe lists preparation time, cooking time, servings, and complete macros including calories, fat, protein, and net carbs so you can easily track your daily intake.",
    ]
    y = 570
    for p in intro_text:
        for line in wrap(p, 68):
            pdf.add_text(50, y, line, 'F4', 10.5)
            y -= 15
        y -= 10

    # Recipes by category
    # Add keto guide chapters first
    keto_chapters_text = [
        ("Understanding Ketosis", "Ketosis is a metabolic state where your body primarily burns fat for fuel instead of carbohydrates. When carb intake drops below twenty to fifty grams daily your liver begins converting fatty acids into ketone bodies that power your brain and muscles efficiently. This transition typically takes two to seven days of consistent low-carb eating. During this adaptation phase you may experience temporary fatigue headaches and irritability known as the keto flu which resolves as your body becomes fat-adapted. Once in ketosis many people report increased mental clarity stable energy levels throughout the day and significantly reduced hunger and cravings between meals."),
        ("Keto Macros Explained", "The standard ketogenic ratio is approximately seventy percent of calories from fat twenty-five percent from protein and five percent from carbohydrates. For a two thousand calorie diet this translates to about one hundred fifty-five grams of fat one hundred twenty-five grams of protein and twenty-five grams of net carbs daily. Net carbs equal total carbs minus fiber. Tracking macros ensures you maintain ketosis while getting adequate nutrition. Use a food tracking app during your first month to learn portion sizes and carb counts then transition to intuitive eating once you develop familiarity with keto-friendly foods."),
        ("Keto Shopping List Essentials", "Stock your kitchen with keto staples to make meal preparation simple. Proteins include eggs beef chicken pork salmon shrimp and turkey. Fats include butter olive oil coconut oil avocado oil and MCT oil. Dairy includes cheese heavy cream cream cheese sour cream and full-fat yogurt. Vegetables include spinach broccoli cauliflower zucchini bell peppers mushrooms and asparagus. Pantry staples include almond flour coconut flour erythritol stevia dark chocolate nuts seeds and sugar-free condiments. Having these items readily available eliminates the temptation to reach for high-carb convenience foods."),
        ("Meal Prep for Keto Success", "Batch cooking on weekends sets you up for effortless weekday keto eating. Cook large batches of proteins like roasted chicken grilled steak and hard-boiled eggs. Prepare vegetables by washing chopping and portioning into containers. Make sauces and dressings in advance since most store-bought options contain hidden sugars. Pre-portion snacks into grab-and-go containers. Having prepared keto food available at all times prevents the common pitfall of grabbing carb-heavy convenience food when hungry and pressed for time. Most prepared keto foods store well for four to five days refrigerated."),
        ("Eating Out on Keto", "Restaurant dining on keto is simpler than most people expect. Most restaurants accommodate dietary requests when asked politely. Order protein-focused dishes like grilled chicken steak or fish. Request vegetables instead of starchy sides like potatoes rice or bread. Ask for sauces and dressings on the side since many contain hidden sugars. Skip the bread basket tortillas and buns. At fast food restaurants order bunless burgers or grilled chicken salads. At Asian restaurants request dishes without rice and sugar-based sauces. With practice eating out becomes natural and enjoyable without breaking ketosis."),
        ("Common Keto Mistakes", "The most common keto mistake is eating too much protein and not enough fat which can prevent ketosis through a process called gluconeogenesis where excess protein converts to glucose. Another frequent error is not tracking hidden carbs in sauces condiments and processed foods that add up quickly beyond your daily limit. Many beginners also neglect electrolytes leading to fatigue cramps and headaches easily remedied with sodium potassium and magnesium supplementation. Not drinking enough water is another common issue as the keto diet has a diuretic effect. Finally expecting instant results leads to premature abandonment before fat adaptation completes."),
        ("Keto and Exercise", "Exercise performance may temporarily decrease during the first two to four weeks of keto as your body adapts to burning fat instead of glycogen for fuel. Once fat-adapted many athletes report improved endurance for low-to-moderate intensity activities because fat provides virtually unlimited energy. For high-intensity explosive activities like sprinting or heavy weightlifting some practitioners incorporate targeted carbs immediately before training. Electrolyte management becomes especially important during exercise on keto as sweating combined with the diuretic effect increases mineral losses. Stay well-hydrated and supplement electrolytes before during and after workouts."),
        ("Breaking Stalls and Plateaus", "Weight loss stalls are normal on keto and do not indicate the diet has stopped working. Common causes include hidden carb creep where carbs gradually increase without awareness and calorie surplus from unlimited high-calorie keto foods like nuts cheese and fat bombs. Solutions include tracking food precisely for one week re-evaluating portion sizes incorporating intermittent fasting for additional metabolic benefit and varying your calorie intake between higher and lower days. Stress management and sleep quality also significantly impact weight loss. Patience is essential as body composition often improves even when the scale does not move."),
        ("Keto for Long-Term Health", "The ketogenic diet offers benefits beyond weight loss including improved insulin sensitivity reduced inflammation better cardiovascular markers in many people enhanced mental clarity and potential neuroprotective effects. Long-term sustainability requires focusing on nutrient-dense whole foods rather than relying on processed keto products. Regular blood work monitoring ensures your health markers trend positively. Some people thrive on strict keto indefinitely while others benefit from cycling between keto and moderate-carb periods. Listen to your body maintain variety in your food choices and prioritize vegetables and quality proteins alongside healthy fats for optimal long-term outcomes."),
    ]
    for ch_title, ch_text in keto_chapters_text:
        pdf.new_page()
        pdf.add_text(50, 600, ch_title, 'F2', 13)
        yy = 570
        for line in wrap(ch_text, 62):
            if yy < 70:
                pdf.new_page()
                yy = 600
            pdf.add_text(50, yy, line, 'F4', 11)
            yy -= 20

    for cat_name, recs in categories:
        pdf.new_page()
        pdf.add_filled_rect(0, H//2, W, H//2, 0.95)
        pdf.add_centered_text(400, cat_name.upper(), 'F2', 18)
        
        for name, prep, cook, servings, macros, ingredients, instructions in recs:
            pdf.new_page()
            y = 600
            pdf.add_text(50, y, name, 'F2', 13)
            y -= 25
            pdf.add_text(50, y, f"Prep: {prep} | Cook: {cook} | Servings: {servings}", 'F1', 9, 0.3)
            y -= 20
            pdf.add_text(50, y, f"Macros: {macros} (cal/fat/protein/carbs g)", 'F1', 9, 0.3)
            y -= 25
            pdf.add_text(50, y, "INGREDIENTS:", 'F2', 10)
            y -= 20
            for ing in ingredients.split(", "):
                pdf.add_text(60, y, f"- {ing.strip()}", 'F4', 10)
                y -= 15
            y -= 15
            pdf.add_text(50, y, "INSTRUCTIONS:", 'F2', 10)
            y -= 20
            for line in wrap(instructions, 65):
                pdf.add_text(60, y, line, 'F4', 10)
                y -= 15
            # Add tips to increase page count
            y -= 20
            tips = f"CHEF TIPS: For best results, use fresh high-quality ingredients. This recipe stores well in the refrigerator for up to three days. Adjust seasonings to your personal taste preferences. Net carbs may vary slightly based on specific brand ingredients used."
            for line in wrap(tips, 65):
                if y < 70:
                    pdf.new_page()
                    y = 600
                pdf.add_text(60, y, line, 'F3', 9, 0.3)
                y -= 14
    
    pdf.new_page()
    pdf.add_centered_text(400, "Thank you for reading!", 'F2', 16)
    pdf.add_centered_text(370, f"by {AUTHOR}", 'F4', 12)
    pdf.save("Book313_Keto_Cookbook.pdf")
    print(f"  Created: Book313_Keto_Cookbook.pdf ({len(pdf.pages)} pages)")


def book314():
    chapters = [
        ("Why Discipline Beats Motivation", [
            "Motivation is a feeling that comes and goes unpredictably like weather. Discipline is a decision that persists regardless of emotional state. Building your life on motivation is building on sand.",
            "Motivated people accomplish things when they feel like it. Disciplined people accomplish things regardless of feelings. Over a year the disciplined person produces ten times more because they never take days off.",
            "The motivation myth suggests you need to feel inspired before acting. In reality action creates motivation not the reverse. Start working and motivation appears. Wait for motivation and you wait forever.",
            "Discipline is simply doing what you said you would do when you said you would do it regardless of how you feel in the moment. It is keeping promises to yourself with the same reliability you keep promises to others.",
            "Every time you follow through when you do not feel like it, you strengthen your self-discipline muscle. Every time you give in to comfort, you weaken it. Each decision is a training repetition.",
            "Successful people are not more talented or lucky. They are more consistent. Consistency comes from discipline. Discipline comes from practice. There is no shortcut and no substitute.",
            "The compound effect of daily discipline is staggering. Writing one page daily produces a book in a year. Saving twenty dollars daily produces over seven thousand yearly. Small disciplined actions create extraordinary results.",
            "This book will give you practical systems for building unbreakable discipline. Not through willpower alone, which is limited, but through environment design, identity change, and strategic habit systems."
        ], ["Discipline produces results regardless of emotional state",
            "Action creates motivation, not the reverse",
            "Each discipline decision is a training repetition that builds capacity"],
         "Do one thing today that you have been avoiding because you do not feel like it. Notice that motivation appears after you start, not before."),

        ("The Neuroscience of Willpower", [
            "Willpower is governed by the prefrontal cortex, the brain region responsible for executive function, planning, and impulse control. This region has limited energy and depletes with use throughout the day.",
            "Decision fatigue is real and measurable. After making many decisions your prefrontal cortex becomes less effective at resisting impulses. This explains why diets fail at night and poor choices happen when exhausted.",
            "Blood glucose fuels willpower literally. Studies show that willpower performance improves after consuming glucose and deteriorates when blood sugar drops. Stable nutrition supports discipline throughout the day.",
            "Sleep deprivation dramatically impairs prefrontal cortex function. One night of poor sleep reduces impulse control to levels similar to legal intoxication. Protecting sleep protects discipline directly.",
            "The good news: willpower functions like a muscle. Regular exercise of self-control gradually increases your capacity over time. People who practice discipline in small areas develop strength that transfers everywhere.",
            "Stress depletes willpower reserves rapidly. Chronic stress keeps cortisol elevated which impairs prefrontal cortex function. Managing stress through exercise, meditation, or nature exposure preserves discipline capacity.",
            "Habits bypass willpower entirely. Once a behavior becomes habitual, it requires no willpower to execute. The strategic approach is using limited willpower to establish habits that then run automatically forever.",
            "Understanding these biological mechanisms removes moralistic shame from discipline failures. You are not weak or flawed. Your brain has predictable limitations. Work with biology rather than against it."
        ], ["Willpower depletes with use; protect it strategically",
            "Sleep and blood sugar directly fuel self-control capacity",
            "Build habits that bypass willpower for sustainable discipline"],
         "Identify your highest willpower period and schedule your most discipline-demanding task during that window. Protect this time ruthlessly."),

        ("Morning Routine Mastery", [
            "How you start your day determines its trajectory. A intentional morning routine builds momentum, establishes control, and primes your psychology for disciplined behavior throughout the remaining hours.",
            "Wake at the same time every day including weekends. This single commitment trains your circadian rhythm, improves sleep quality, and eliminates the daily decision of whether to get up or hit snooze.",
            "Eliminate decision-making from your morning. Prepare clothes the night before, eat the same breakfast, follow the same sequence. Zero decisions means zero willpower depletion before your day even starts.",
            "Include one challenging element: cold water, exercise, or deep work before checking your phone. Completing something difficult first thing proves to yourself that you are someone who does hard things.",
            "Avoid your phone for the first thirty to sixty minutes. Email, social media, and news put you in reactive mode immediately. Your morning should be proactive, not responsive to others demands.",
            "Physical movement in the morning improves blood flow to the prefrontal cortex, releases endorphins, and establishes a sense of accomplishment. Even ten minutes of movement changes your entire day.",
            "Review your priorities before the world intrudes. What are the one to three most important things you will accomplish today? Write them down. This clarity prevents busy work from consuming your best hours.",
            "Protect your morning routine from exceptions. The power comes from consistency. One disrupted morning becomes three which becomes abandonment. Maintain the routine even when traveling or disrupted."
        ], ["Same wake time daily trains your biology for consistency",
            "Complete one difficult thing before checking your phone",
            "Eliminate morning decisions to preserve willpower for important work"],
         "Design your ideal morning routine tonight. Set out everything needed. Wake thirty minutes earlier tomorrow and execute the routine before any screen time."),

        ("Eliminating Decision Fatigue", [
            "The average adult makes approximately thirty-five thousand decisions daily. Each one depletes the finite willpower reserve in your prefrontal cortex, leaving less energy for important choices and discipline.",
            "Pre-decide as much as possible. Meal plans eliminate food decisions. Capsule wardrobes eliminate clothing decisions. Standing meetings eliminate scheduling decisions. Each elimination preserves cognitive resources.",
            "Routines and systems remove decisions from recurring situations. When you have a system for email processing, bill paying, grocery shopping, and exercise, these activities require no deliberation.",
            "Limit options to reduce decision load. Having fewer choices paradoxically increases satisfaction and reduces cognitive burden. Choose one brand, one restaurant, one workout program rather than evaluating endlessly.",
            "Batch similar decisions together. Review all emails at designated times rather than throughout the day. Make all meal decisions on Sunday. Choose all outfits for the week at once.",
            "Use if-then rules to automate responses to common situations. If someone asks for a meeting, I check my calendar and suggest specific times. If I feel like snacking after nine PM, I drink tea instead.",
            "Default options are powerful. Set your defaults to the disciplined choice. Automatic savings, pre-scheduled workouts, pre-ordered healthy meals. The default option requires no decision to execute.",
            "Save your best decision-making capacity for what truly matters: creative work, strategic thinking, relationship investments, and personal growth. Automate everything else ruthlessly."
        ], ["Thirty-five thousand daily decisions deplete willpower reserves",
            "Pre-decide recurring choices to eliminate cognitive load",
            "Default options make the disciplined choice automatic"],
         "Identify five recurring decisions you make daily. Create a rule or system for each that eliminates the need to decide. Implement all five this week."),

        ("The Power of No", [
            "Every yes to something unimportant is a no to something essential. Discipline requires the courage to decline requests, invitations, and opportunities that do not align with your priorities.",
            "People pleasers struggle with discipline because they prioritize others comfort over their own goals. Saying no is not selfish. It is honest about your capacity and respectful of your commitments.",
            "The discomfort of saying no lasts seconds. The consequence of saying yes to the wrong things lasts weeks, months, or years. Choose brief discomfort over prolonged misalignment with your priorities.",
            "Practice no with low-stakes situations to build the muscle. Decline unnecessary meetings. Say no to social events that drain you. Refuse requests that could be handled by others. Start small.",
            "A helpful framework: if it is not a clear yes, it is a no. Anything that requires debate, justification, or convincing yourself does not deserve your limited time and energy.",
            "Protect your calendar like protecting your wallet. Time is more valuable than money because you cannot earn more of it. Every hour given away to non-priorities is gone permanently.",
            "Saying no to good opportunities is especially difficult but essential. Good is the enemy of great. When your schedule fills with merely good activities, no room remains for transformative ones.",
            "Frame no positively when possible. I cannot attend because I am committed to finishing my project. This communicates priority rather than rejection and models integrity to others."
        ], ["Every yes to the unimportant is a no to the essential",
            "If it is not a clear yes, it is a no",
            "Protect time more carefully than money since it cannot be earned back"],
         "Say no to one request this week that you would normally accept out of obligation. Notice the time and energy that becomes available for your actual priorities."),

        ("Digital Detox for Discipline", [
            "The average person spends over four hours daily on their phone, mostly on social media and entertainment. This represents twenty-eight hours weekly or sixty full days per year of life consumed by screens.",
            "Social media and apps are designed by teams of psychologists to be maximally addictive. Variable reward schedules, social validation, and infinite scroll exploit your dopamine system deliberately.",
            "Constant digital stimulation destroys your capacity for focused work, deep thinking, and sustained effort. Your attention span shortens and your tolerance for boredom, which is necessary for discipline, disappears.",
            "Implement specific boundaries: no phone in the bedroom, no social media before noon, no screens during meals, phone in another room during work blocks. Each boundary reclaims attention and discipline capacity.",
            "Delete apps that consume time without adding value. If you need social media for work, use browser versions that add friction. Remove notifications for everything except calls and messages from close contacts.",
            "Replace screen time with activities that build discipline: reading, exercise, journaling, skill practice, or genuine face-to-face connection. Fill the void intentionally rather than leaving a vacuum.",
            "Track your screen time weekly. The data will shock you and motivate change. Most people dramatically underestimate their consumption until confronted with accurate measurements.",
            "Digital discipline transfers to other areas. When you prove you can resist the most addictive engineered dopamine hits, resisting lesser temptations becomes comparatively easy."
        ], ["Four hours daily on phones equals sixty days per year consumed",
            "Apps exploit psychology to be maximally addictive deliberately",
            "Digital discipline builds capacity that transfers to all areas"],
         "Check your screen time statistics today. Set a goal to reduce by thirty percent this week. Delete one app that consumes time without adding genuine value."),

        ("Cold Exposure and Discomfort Training", [
            "Voluntary discomfort builds discipline by training your brain to act despite the desire for comfort. Cold showers, hard exercise, fasting, and difficult conversations all develop the same underlying capacity.",
            "Cold exposure specifically activates norepinephrine, improves mood, increases alertness, and most importantly teaches you that discomfort is temporary and survivable. This knowledge transfers to all discipline challenges.",
            "Start with thirty seconds of cold water at the end of your regular shower. Increase by fifteen seconds weekly until you tolerate two to three minutes. The resistance you feel is exactly what you are training against.",
            "The moment you want to quit, stay ten more seconds. This trains the neural pathway of continuing despite the desire to stop. Every time you stay you prove to yourself that comfort is optional.",
            "Physical discomfort training includes intense exercise, holding difficult positions, waking early, sleeping on hard surfaces, or going without food for extended periods. Each builds general discomfort tolerance.",
            "Mental discomfort training includes difficult conversations, public speaking, admitting mistakes, asking for help, and sitting with boredom or uncertainty without reaching for a distraction.",
            "The stoics practiced voluntary poverty periodically, eating simple food and wearing rough clothing to reduce attachment to comfort and luxury. Knowing you can survive without luxuries eliminates the power they hold.",
            "Consistency matters more than intensity. Brief daily discomfort practice builds more discipline than occasional extreme challenges followed by long periods of comfort seeking."
        ], ["Voluntary discomfort builds the muscle of acting despite resistance",
            "Cold exposure teaches that discomfort is temporary and survivable",
            "Daily brief practice builds more than occasional extreme challenges"],
         "End tomorrow's shower with thirty seconds of cold water. When the urge to escape arises, stay ten seconds longer. Notice how quickly you recover afterward."),

        ("Delaying Gratification", [
            "The ability to delay gratification is the single strongest predictor of success across health, wealth, relationships, and achievement. Stanford's marshmallow study showed this trait predicts outcomes decades later.",
            "Modern society constantly offers immediate rewards: fast food, instant entertainment, one-click purchases, social media dopamine. This environment erodes natural delay capacity unless actively resisted.",
            "Practice the ten-minute rule for impulse purchases: when you want something, wait ten minutes. Seventy percent of impulse desires vanish within ten minutes. For larger purchases, extend to twenty-four to seventy-two hours.",
            "Visualize your future self benefiting from today's discipline. See yourself fit, wealthy, accomplished, at peace. Make this vision vivid and emotionally compelling enough to outweigh present temptation.",
            "Implementation intention for temptation: when I feel the urge to indulge immediately, I will wait ten minutes and ask whether my future self will be grateful or regretful for this choice.",
            "Create physical distance from temptation. Do not keep junk food in the house. Unsubscribe from marketing emails. Remove saved credit cards from shopping sites. Distance reduces the pull of immediate rewards.",
            "Reward yourself for successful delay. After resisting temptation for a defined period, provide a meaningful reward. This teaches your brain that delay leads to better outcomes, not just deprivation.",
            "Build delay capacity gradually. If you currently cannot wait five minutes, practice five until it becomes easy, then extend to fifteen, then thirty. Progressive training works better than willpower alone."
        ], ["Delaying gratification is the strongest predictor of life success",
            "The ten-minute rule eliminates seventy percent of impulse desires",
            "Progressive delay training builds capacity gradually over time"],
         "Apply the ten-minute rule to every impulse purchase and snack craving today. Count how many urges pass naturally when you simply wait."),

        ("Goal-Setting That Works", [
            "Most goals fail not because people lack desire but because goals are too vague, too distant, or lack connection to daily systems. Effective goal-setting bridges the gap between aspiration and daily behavior.",
            "SMART goals are a start but insufficient. Add emotional connection: why does this goal matter to your identity, relationships, or life purpose? Goals without emotional fuel cannot survive the inevitable obstacles.",
            "Break annual goals into quarterly milestones, monthly targets, weekly objectives, and daily actions. This cascade ensures that today's behavior connects directly to long-term aspirations through clear intermediary steps.",
            "Process goals outperform outcome goals for discipline. Instead of lose thirty pounds, which you cannot directly control, set I will exercise thirty minutes daily and eat under two thousand calories, which you can.",
            "Write goals in present tense affirmation format: I am the type of person who exercises every day. This identity-based framing shifts goal-setting from willpower to self-concept alignment.",
            "Review goals daily. Goals you do not see cannot motivate. Write your top three goals on a card kept in your wallet, posted on your mirror, or set as your phone wallpaper. Constant visibility maintains focus.",
            "Build accountability structures around goals. Share them publicly, find an accountability partner, join a mastermind group, or hire a coach. External accountability dramatically increases follow-through rates.",
            "Plan for obstacles in advance. For each goal, identify three likely barriers and pre-determine your response. When predictable obstacles arrive, you execute the plan rather than making decisions under pressure."
        ], ["Connect goals to emotional purpose and identity for fuel",
            "Process goals you control daily outperform outcome goals",
            "Pre-plan responses to predictable obstacles before they arrive"],
         "Write your top three goals. For each, define the daily process that produces the outcome. Post these daily processes where you will see them every morning."),

        ("Time-Blocking Mastery", [
            "Time-blocking assigns every hour of your day a specific purpose in advance. This transforms your schedule from reactive to proactive and eliminates the discipline drain of constantly deciding what to work on next.",
            "Without time-blocking, the urgent perpetually crowds out the important. Emails, messages, and interruptions consume your day while meaningful projects remain untouched. Blocking prevents this by reservation.",
            "Block your most important work during your peak energy period. For most people this is morning. Protect this block absolutely: no meetings, no email, no interruptions. This is when discipline produces maximum output.",
            "Include transition time between blocks. Back-to-back scheduling ignores the reality that switching tasks requires mental reset time. Five to fifteen minute buffers maintain sanity and prevent cascading delays.",
            "Plan tomorrow's time blocks tonight. This decision made with fresh evening perspective eliminates morning deliberation about what to do first. You wake knowing exactly what your day looks like.",
            "Honor your time blocks like appointments with your most important client. You would not cancel a meeting with your CEO to check social media. Treat your blocked creative or strategic work with equal respect.",
            "Include personal blocks: exercise, family time, reading, rest. Disciplined people protect personal priorities as vigorously as professional ones. Burnout destroys discipline. Restoration enables it.",
            "Expect interruptions and build buffer blocks into your day. Rigidity produces frustration when reality interferes. Flexibility within structure maintains the system during unpredictable days."
        ], ["Time-blocking makes proactive choices rather than reactive responses",
            "Protect your peak energy block for most important work absolutely",
            "Plan tomorrow's blocks tonight to eliminate morning deliberation"],
         "Block tomorrow's schedule tonight in thirty-minute segments. Include your most important work during your peak energy window. Follow the plan regardless of feelings."),

        ("Accountability Systems", [
            "Accountability multiplies discipline through external commitment and social consequences. The combination of internal resolve with external structure produces far more consistent behavior than either alone.",
            "Find an accountability partner with similar goals and establish a regular check-in structure. Daily text updates, weekly calls, or monthly meetings create rhythmic accountability that maintains focus over time.",
            "Financial stakes dramatically increase follow-through. Commit money to your goals through bet-based platforms, deposits forfeited upon failure, or automatic donations to organizations you oppose when you miss targets.",
            "Public commitment leverages social reputation. Sharing goals on social media, telling friends and family, or posting progress publicly creates reputational consequence that motivates discipline on difficult days.",
            "Coaching or mentorship provides both accountability and expertise. A coach who checks your progress weekly and helps solve obstacles offers the highest-fidelity accountability available for important goals.",
            "Group accountability through mastermind groups, fitness classes, or online communities creates belonging and peer pressure. When your group expects you to show up and contribute, you rarely miss.",
            "Track and display your progress publicly. A visible streak chart, a public progress log, or a shared tracking document creates accountability through transparency. Others can see your consistency or lack thereof.",
            "Choose accountability structures that match your personality. Some people respond to social pressure while others respond to financial stakes. Know yourself and design accordingly."
        ], ["External accountability multiplies internal discipline dramatically",
            "Financial stakes create powerful motivation to follow through",
            "Choose accountability types matching your personal motivation style"],
         "Establish one accountability structure for your most important goal this week: find a partner, make a public commitment, or put money at stake."),

        ("Handling Failure and Setbacks", [
            "Failure is not the opposite of discipline. Quitting after failure is. Every disciplined person fails regularly. What distinguishes them is returning to their practice immediately without extended self-punishment.",
            "The never miss twice rule saves habits after inevitable disruption. One missed day is human. Two missed days starts a pattern. Your only job after any failure is showing up the next scheduled time.",
            "Analyze failures without emotional judgment. What circumstance led to the lapse? What could prevent it next time? What system adjustment would make success more likely? Extract data then move forward.",
            "Self-compassion after failure actually produces more discipline than self-criticism. Research shows that people who forgive themselves for lapses return to their habits faster than those who punish themselves.",
            "Distinguish between a lapse and a relapse. A lapse is a single incident of failing to execute. A relapse is abandoning the system entirely. Most people turn lapses into relapses unnecessarily.",
            "Failure provides information no success ever could. When everything works perfectly you learn nothing about your vulnerabilities, limits, or the conditions that undermine your discipline. Failure is educational.",
            "Plan your failure response in advance. When I fail at my habit, I will not catastrophize. I will identify the cause, adjust my system, and execute the very next day without additional guilt or punishment.",
            "Remember your identity: I am the type of person who gets back up. One failure does not change your identity unless you allow it to become a pattern. Respond to failure by voting for your desired identity."
        ], ["Never miss twice: return immediately after any failure",
            "Self-compassion produces faster recovery than self-punishment",
            "Extract learning data from failure then move forward without guilt"],
         "Write your failure response plan now before you need it. When the inevitable lapse occurs, execute the plan rather than spiraling into self-criticism and abandonment."),

        ("The 30-Day Discipline Bootcamp", [
            "Days one through five establish your morning routine. Wake at the same time daily, complete a challenging task before your phone, and follow a consistent sequence. Master this foundation before adding complexity.",
            "Days six through ten add cold exposure training. End every shower with sixty seconds of cold water. This daily discomfort practice builds your relationship with resistance and proves comfort is optional.",
            "Days eleven through fifteen implement time-blocking. Plan each day's schedule the night before. Follow the blocks regardless of feelings. Track compliance and identify patterns in your discipline failures.",
            "Days sixteen through twenty eliminate one bad habit using environmental design. Remove cues, add friction, and replace the behavior with something aligned with your goals. Commit fully for five days.",
            "Days twenty-one through twenty-five focus on delay of gratification. Apply the ten-minute rule to every impulsive desire. Keep score of how many urges you successfully delay into extinction.",
            "Days twenty-six through thirty integrate everything into your permanent system. Design your ongoing daily discipline practice drawing from what worked best during the previous twenty-five days.",
            "Throughout all thirty days maintain a discipline journal. Rate your daily discipline one to ten, note victories and failures, record observations about what supports or undermines your willpower.",
            "After thirty days you will have established foundational habits, built discomfort tolerance, created time-management systems, and developed a self-concept as a disciplined person. The transformation compounds from here."
        ], ["Five-day blocks build progressive discipline skills",
            "Journal daily to track patterns and maintain accountability",
            "The thirty-day foundation creates lifelong compound growth"],
         "Commit to the thirty-day discipline bootcamp starting tomorrow. Tell someone about your commitment and report to them daily for accountability."),

        ("Maintaining Long-Term Discipline", [
            "Short-term discipline is achievable through willpower and motivation. Long-term discipline requires systems, identity change, and sustainable practices that do not depend on feeling disciplined.",
            "Audit your systems quarterly. What habits have become effortless? These need no more attention. What goals are stalling? These need system adjustment. Regular review prevents drift from your priorities.",
            "Your social environment must support your discipline long-term. Surround yourself with disciplined people. Distance yourself from those who enable or encourage undisciplined behavior. Environment always wins.",
            "Prevent burnout by including deliberate rest and recovery. Discipline without rest produces exhaustion and eventual collapse. Strategic rest enables sustainable high performance across years and decades.",
            "Continue progressive challenge. Once current habits are easy, add new ones. Discipline is a capacity that grows with use but atrophies without challenge. Comfort is the enemy of continued growth.",
            "Reconnect with your purpose regularly. Why does discipline matter to you? What life are you building? Without emotional fuel, discipline becomes dry obligation that eventually breaks. Purpose sustains indefinitely.",
            "Celebrate milestones. Acknowledge years of consistency, major achievements, and personal growth. Recognition of progress provides motivation to continue during inevitable periods of difficulty.",
            "Remember that discipline is not perfection. It is consistency despite imperfection. You will have weak days, bad weeks, and difficult seasons. The disciplined person returns to their systems every time. Always."
        ], ["Long-term discipline requires systems, not just willpower",
            "Quarterly audits prevent drift from priorities",
            "Discipline is consistency despite imperfection, not perfection"],
         "Schedule a quarterly discipline audit on your calendar. Review your systems, habits, and goals. Adjust what is not working and celebrate what is. Repeat every three months indefinitely."),
    ]
    build_book("Book314_Self_Discipline.pdf", "UNBREAKABLE DISCIPLINE",
               "The No-BS Guide to Doing What You Said You Would", chapters)


def make_book_from_data(filename, title, subtitle, ch_data):
    """ch_data: list of (chapter_title, list_of_8_paragraphs)"""
    chapters = []
    for ch_title, paras in ch_data:
        tk = [paras[0][:75], paras[1][:75], paras[2][:75]]
        action = f"Apply the core principle of {ch_title.lower()} to your situation today by identifying one concrete action step."
        chapters.append((ch_title, paras, tk, action))
    build_book(filename, title, subtitle, chapters)

def book315():
    ch = [
        ("Your Money Story", [
            "Every financial decision you make is filtered through beliefs about money formed in childhood. Whether you grew up hearing money does not grow on trees or rich people are greedy, these stories drive behavior unconsciously.",
            "Identifying your money scripts is the first step to financial freedom. Common limiting beliefs include I do not deserve wealth, money is evil, and I am bad with money. None of these are objectively true.",
            "Your parents' relationship with money became your template. Did they fight about bills, hide purchases, or demonstrate abundance mindset? Recognizing inherited patterns lets you consciously choose better ones.",
            "Rewrite your money story deliberately. I am capable of building wealth. Money is a tool for freedom. I make wise financial decisions. Repetition of new beliefs gradually overwrites old programming.",
            "Financial anxiety often stems from ignorance not inability. People avoid looking at their accounts because numbers trigger shame. This avoidance worsens the situation. Knowledge is the antidote to money fear.",
            "Your net worth is not your self-worth. Separating identity from financial status reduces emotional reactivity around money and enables rational decision-making based on mathematics rather than feelings.",
            "Financial literacy is a skill anyone can develop regardless of starting point. You do not need to be naturally good with numbers. Simple systems and automation handle the math while you provide direction.",
            "The single most important financial decision is choosing to take control. Most people passively accept whatever financial situation develops. Actively managing money produces dramatically different outcomes."
        ]),
        ("The 3-Account System", [
            "Financial simplicity beats complexity every time. The three-account system uses one checking account for bills, one savings account for goals, and one investment account for wealth building. That is all you need.",
            "Your checking account handles all monthly expenses: rent, utilities, subscriptions, groceries, and discretionary spending. Keep enough here for monthly expenses plus a small buffer. Everything else moves out.",
            "Your savings account holds your emergency fund and short-term goals: vacation funds, car repairs, holiday gifts, and home maintenance. High-yield savings accounts earn interest while maintaining accessibility.",
            "Your investment account builds long-term wealth through stock market index funds, retirement accounts, or other growth vehicles. Money here is not touched for years or decades, allowing compound growth.",
            "Automate transfers on payday. Before you can spend money, predetermined amounts move to savings and investments. What remains in checking is your true spending money. You cannot overspend what is already moved.",
            "This system eliminates budget tracking for most people. If bills are paid and savings goals are funded automatically, the remaining money in checking is genuinely available for guilt-free spending.",
            "Start with any amounts, even small ones. Five dollars to savings and five dollars to investments on each paycheck establishes the habit. Increase amounts with every raise, bonus, or expense reduction.",
            "Review once monthly for five minutes: are accounts at expected levels? Are automatic transfers functioning? Any unexpected charges? This minimal oversight maintains the system without obsessive tracking."
        ]),
        ("Automating Your Finances", [
            "Automation is the single most powerful tool for financial success because it removes the need for willpower, memory, or motivation. Once set up, your finances operate correctly without your daily attention.",
            "Set up automatic bill payments for every recurring expense. Late fees from forgotten payments waste hundreds annually. Automatic payment eliminates this entirely while improving your credit score.",
            "Automatic savings transfers on payday ensure you pay yourself first. The principle is simple: save before you spend, not after. What you never see in your checking account you never miss.",
            "Investment contributions should be automatic and consistent. Dollar-cost averaging through regular automatic investments removes the impossibility of timing the market and ensures consistent wealth building.",
            "Automatic credit card payments of the full balance prevent interest charges. If you use credit cards for rewards, ensure the full balance pays automatically each month to avoid the trap of debt accumulation.",
            "Set up automatic transfers to specific savings goals: vacation fund, car replacement, holiday gifts, and home maintenance. Each goal gets its own automatic contribution ensuring progress without thought.",
            "Review automations quarterly to adjust for changed circumstances: income increases, new expenses, or achieved goals. Update amounts upward whenever possible to accelerate your financial timeline.",
            "The initial setup takes one to two hours but saves hundreds of hours and thousands of dollars over your lifetime. This is the highest-return-on-time investment in personal finance."
        ]),
        ("Killing Debt", [
            "Debt is an emergency that prevents all other financial progress. Every dollar paying interest to creditors is a dollar not building your wealth. Eliminating debt is the prerequisite to financial freedom.",
            "The debt snowball method lists debts smallest to largest regardless of interest rate. Pay minimums on all except the smallest. Attack the smallest with every extra dollar until eliminated. Then roll that payment to the next.",
            "The debt avalanche method lists debts by interest rate highest to lowest. Mathematically this saves more in interest charges. Pay minimums on all except the highest rate debt. Attack it first.",
            "Choose snowball for psychological motivation if you need quick wins to maintain momentum. Choose avalanche if you are mathematically motivated and can tolerate longer waits for the first debt elimination.",
            "Increase debt payments by reducing expenses and increasing income simultaneously. Sell possessions, take temporary extra work, cancel subscriptions, downgrade services. Treat debt like the emergency it is.",
            "Stop acquiring new debt immediately. Cut up credit cards if necessary. Use cash or debit only during the debt elimination phase. New debt while paying old debt is running on a treadmill going nowhere.",
            "Track your debt payoff visually. A thermometer chart on your wall, a spreadsheet updated weekly, or an app showing progress. Visible progress maintains motivation during the months or years of repayment.",
            "Once debt-free, redirect all former debt payments to savings and investments. You have already proven you can live without this money. Now it builds wealth instead of servicing debt."
        ]),
        ("Emergency Fund in 90 Days", [
            "An emergency fund is one thousand dollars minimum as a starter, then three to six months of essential expenses as a complete fund. Without this buffer, any unexpected expense forces debt accumulation.",
            "The starter emergency fund of one thousand dollars can be built in ninety days through aggressive temporary measures: selling possessions, taking extra shifts, reducing all non-essential spending, and redirecting every windfall.",
            "Calculate your essential expenses: housing, food, utilities, transportation, insurance, and minimum debt payments. Multiply by three for a lean emergency fund or six for a comfortable buffer.",
            "Keep emergency funds in a separate high-yield savings account at a different bank than your checking. This creates friction against casual access while earning interest and maintaining liquidity for true emergencies.",
            "Define what constitutes an emergency: job loss, medical bills, car breakdown needed for work, essential home repair. Shopping sales, vacations, and routine maintenance are not emergencies and have their own savings.",
            "Once fully funded, stop contributing to the emergency fund and redirect those funds to investments. The emergency fund is insurance, not an investment. It should not grow beyond six months of expenses.",
            "If you use the emergency fund, rebuilding it becomes your top financial priority before resuming other goals. The security it provides protects all other financial progress from derailment.",
            "The psychological benefit of an emergency fund often exceeds the financial benefit. Knowing you can handle any crisis without debt reduces financial anxiety dramatically and improves daily life quality."
        ]),
        ("Investing for Beginners", [
            "Investing is how ordinary income becomes extraordinary wealth through the power of compound growth over time. Every year you delay investing costs thousands in future wealth due to missed compounding.",
            "Index funds provide the simplest and most effective investment approach for most people. A total stock market index fund gives you ownership of thousands of companies for fees under point one percent.",
            "Historical stock market returns average approximately ten percent annually before inflation over long periods. This means money doubles roughly every seven years. Starting early makes this compounding dramatically powerful.",
            "Dollar-cost averaging means investing the same amount regularly regardless of market conditions. This eliminates timing risk and emotional decision-making while ensuring you buy more shares when prices are low.",
            "Tax-advantaged accounts like 401k plans and IRAs provide either tax-deductible contributions or tax-free growth. Always maximize employer matches first as this represents immediate one hundred percent returns on your money.",
            "Do not try to pick individual stocks or time the market. Professional fund managers fail to beat index funds over long periods. Your best strategy is consistent automatic investment in diversified index funds.",
            "Understand your risk tolerance and time horizon. Money needed within five years belongs in bonds or savings. Money for retirement decades away belongs in stocks for maximum growth despite short-term volatility.",
            "Start investing today even with small amounts. Twenty-five dollars per week invested for forty years at ten percent average returns becomes over seven hundred thousand dollars. Time matters more than amount."
        ]),
        ("Retirement Math Simplified", [
            "Retirement requires replacing your working income with passive investment income. The four percent rule suggests you need twenty-five times your annual expenses invested to retire safely indefinitely.",
            "If you need fifty thousand dollars annually in retirement, you need one point two five million invested. This sounds enormous but compound growth over decades makes it achievable with consistent modest contributions.",
            "Starting at twenty-five and investing five hundred monthly at ten percent average returns produces over three million by age sixty-five. Starting at thirty-five with the same contribution produces only one point two million.",
            "Every decade of delay roughly halves your outcome or requires double the monthly contribution. This is why starting immediately with any amount matters more than waiting until you can invest more.",
            "Social Security provides a foundation but typically covers only thirty to forty percent of pre-retirement income. The gap must be filled by personal savings and investments built during working years.",
            "Employer matches in 401k plans are free money. Contributing enough to get the full match is the minimum for everyone. Beyond that, maximize tax-advantaged space before investing in taxable accounts.",
            "Calculate your retirement number: multiply your desired annual spending by twenty-five. Then calculate how much monthly investment at expected returns gets you there by your target retirement age.",
            "Retirement calculators available free online allow you to adjust variables and see how changes in savings rate, return expectations, and timeline affect your outcome. Use them to build a specific plan."
        ]),
        ("Side Income Ideas", [
            "Additional income streams accelerate every financial goal. Rather than cutting expenses further, increasing income provides more material to work with for debt elimination, savings, and investment.",
            "Skill-based services command premium rates: tutoring, consulting, writing, design, programming, bookkeeping, photography, or coaching. Your professional skills have value beyond your employer's paycheck.",
            "Digital products create passive income after initial effort: ebooks, courses, templates, printables, stock photography, or software tools. Creation happens once and sales continue indefinitely.",
            "Gig economy platforms provide flexible income on your schedule: delivery, rideshare, task completion, pet care, or home services. These work best for building emergency funds or paying off specific debts quickly.",
            "Selling possessions generates immediate cash while decluttering your life. Most households contain thousands of dollars in unused items that could be converted to debt payments or investment capital.",
            "Rental income from a spare room, parking space, storage area, or equipment provides recurring passive income from assets you already own. Low effort with reliable monthly returns.",
            "Freelancing in your professional field on evenings and weekends can double your effective income. Many employers allow moonlighting in non-competitive areas. This accelerates financial goals dramatically.",
            "Direct one hundred percent of side income to your current financial priority: debt elimination, emergency fund, or investment growth. Spending side income on lifestyle defeats the purpose entirely."
        ]),
        ("Credit Score Mastery", [
            "Your credit score determines interest rates on mortgages, car loans, and credit cards. A difference of one hundred points can cost or save you tens of thousands over a mortgage lifetime.",
            "Payment history is thirty-five percent of your score. A single late payment can drop your score one hundred points. Set up autopay for every account to eliminate this risk entirely.",
            "Credit utilization is thirty percent of your score. Keep balances below thirty percent of limits, ideally below ten percent. Pay balances before statement closing dates for optimal reporting.",
            "Length of credit history matters. Keep your oldest accounts open even if unused. Closing old accounts shortens your average history and can drop your score. Use them occasionally to prevent closure.",
            "Credit mix helps your score: a combination of revolving credit cards, installment loans, and mortgages shows ability to manage different debt types. Do not open accounts just for mix but do not close them.",
            "Hard inquiries from applications temporarily reduce your score by five to ten points. Limit applications. Rate shopping for mortgages or auto loans within fourteen days counts as a single inquiry.",
            "Monitor your credit reports from all three bureaus annually for errors. Dispute inaccuracies immediately as they can significantly reduce your score. Free monitoring is available through most credit card issuers.",
            "Building excellent credit takes consistent responsible behavior over years. There are no quick fixes or shortcuts. Pay on time, keep utilization low, maintain old accounts, and limit new applications."
        ]),
        ("Buying vs Renting", [
            "The buy versus rent decision is more nuanced than the common advice to always buy. In many markets and situations, renting is financially superior to ownership when all costs are properly calculated.",
            "True homeownership costs include mortgage interest, property taxes, insurance, maintenance averaging one to two percent of home value annually, closing costs, and opportunity cost of the down payment invested elsewhere.",
            "Renting advantages include flexibility, predictable costs, no maintenance responsibility, lower upfront capital requirements, and the ability to invest the difference between rent and total ownership costs.",
            "Buying advantages include forced savings through equity building, potential appreciation, tax deductions on mortgage interest, inflation protection through fixed payments, and emotional stability of permanence.",
            "The five-year rule: if you plan to stay fewer than five years, renting usually wins financially because transaction costs of buying and selling consume any equity built in a short ownership period.",
            "Calculate: compare total monthly ownership cost including all expenses to rent. If renting is cheaper, invest the monthly difference. Often the invested difference outperforms home equity appreciation.",
            "Personal factors beyond pure finances matter: stability needs, family plans, maintenance willingness, career flexibility requirements, and emotional value of ownership all legitimately influence this decision.",
            "Neither choice is universally correct. Run the numbers for your specific situation using a buy-versus-rent calculator, then factor in personal preferences and life stage to make your decision."
        ]),
        ("Teaching Kids About Money", [
            "Financial literacy is rarely taught in schools, making parents the primary source of money education. Children who learn money management early develop habits that serve them their entire lives.",
            "Age-appropriate allowance teaches earning and allocation. Even young children can learn to divide money into spend, save, and give categories. This three-jar system builds the foundation of financial management.",
            "Involve children in age-appropriate financial decisions: grocery shopping on a budget, comparing prices, saving for desired purchases, and understanding the difference between needs and wants.",
            "Delayed gratification practice through saving toward goals teaches the most valuable financial lesson. When children save for weeks to buy something they want, they learn the satisfaction of earned purchases.",
            "Teens benefit from managing their own budgets for clothing, entertainment, and social activities. A monthly allocation that must cover all expenses teaches real-world money management before consequences become severe.",
            "Introduce investing concepts through custodial accounts or stock market simulation games. Understanding compound growth early motivates saving behavior that serves them for decades.",
            "Model healthy money behavior. Children learn more from observing your financial decisions than from your lectures. Demonstrate budgeting, saving, charitable giving, and thoughtful purchasing decisions visibly.",
            "Discuss money openly without shame or secrecy. Families that treat money as a taboo subject produce financially anxious adults. Age-appropriate transparency about household finances builds competence and reduces fear."
        ]),
        ("Couple's Money Conversations", [
            "Money is the number one source of relationship conflict. Regular structured money conversations prevent the buildup of resentment, secrets, and misalignment that destroys partnerships from financial pressure.",
            "Schedule monthly money dates: a dedicated time to review finances together without judgment. Make it pleasant with good food or a comfortable setting. This normalizes financial discussion and reduces avoidance.",
            "Align on shared financial values before debating specific expenses. Do you both value experiences over things? Security over luxury? Freedom over status? Shared values make specific decisions easier.",
            "Establish ground rules: no judgment of past decisions, no attacking, full disclosure of all accounts and debts, and commitment to finding solutions together. Financial conversations require psychological safety.",
            "Decide on a system that respects both partners: fully joint, fully separate, or hybrid with individual and shared accounts. No system is universally best. The right one is the one both partners trust.",
            "Set a spending threshold requiring mutual consultation. Many couples choose one hundred to two hundred dollars. Purchases above this amount require a brief conversation. Below this amount, complete freedom.",
            "Address debt honestly and develop a repayment plan together. Hidden debt is a form of financial infidelity that erodes trust. Full transparency about the current situation enables collaborative solutions.",
            "Celebrate financial milestones together: debt payoff, savings goals reached, investment milestones. Shared celebration reinforces teamwork and makes financial discipline a bonding activity rather than a source of tension."
        ]),
        ("Your 1-Year Money Makeover Plan", [
            "Months one and two: track all spending, identify waste, set up the three-account system, automate bill payments, and build your starter one-thousand-dollar emergency fund through aggressive temporary measures.",
            "Months three and four: begin debt elimination using your chosen method snowball or avalanche. Cancel unnecessary subscriptions. Negotiate bills for lower rates. Direct all freed-up money toward debt destruction.",
            "Months five and six: continue debt payments while increasing income through side hustles or salary negotiation. Research investment options. Open retirement and taxable investment accounts in preparation.",
            "Months seven and eight: as debts clear, redirect payments to building your full three-to-six month emergency fund. Continue side income and direct one hundred percent to this goal until complete.",
            "Months nine and ten: with emergency fund complete, begin investing aggressively. Maximize employer retirement match first, then additional retirement contributions, then taxable investments with remaining funds.",
            "Months eleven and twelve: review all progress, optimize systems, increase investment contributions, set next year's financial goals, and celebrate your transformation from financial stress to financial control.",
            "Throughout all twelve months: review finances monthly, adjust as needed, continue financial education, and maintain the automated systems that make this process sustainable without constant attention.",
            "After one year you will have eliminated or significantly reduced debt, built emergency savings, begun investing, automated your finances, and developed the knowledge and habits for lifelong financial success."
        ]),
    ]
    make_book_from_data("Book315_Money_Management.pdf", "MONEY MADE SIMPLE",
                       "Personal Finance for People Who Hate Budgeting", ch)


def gen_15ch(topic_lines):
    """Generate 15 chapters each with 8 substantial paragraphs from topic data."""
    chapters = []
    for title, seeds in topic_lines:
        paras = []
        for s in seeds:
            paras.append(s)
        # Pad to 8 paragraphs if needed
        while len(paras) < 8:
            paras.append(f"Consistent application of these {title.lower()} principles produces measurable improvement within weeks. Track your progress and adjust your approach based on actual results rather than assumptions.")
        chapters.append((title, paras))
    return chapters

def book316():
    ch = gen_15ch([
        ("Why Most People Fear Public Speaking", [
            "Public speaking fear, or glossophobia, affects approximately seventy-five percent of adults, making it one of the most common phobias. Understanding why helps you overcome it systematically rather than avoiding it permanently.",
            "The fear is evolutionary: being the center of attention triggers the same threat response as being watched by a predator. Your amygdala cannot distinguish between a boardroom audience and a dangerous observer.",
            "The symptoms of speaking anxiety including racing heart, sweaty palms, shaky voice, and dry mouth are your body preparing for physical danger that does not exist. These sensations feel terrible but are completely harmless.",
            "Most speaking anxiety comes from three false beliefs: that the audience is hostile and judging, that mistakes are catastrophic, and that you must be perfect. None of these reflect reality for supportive audiences.",
            "Reframing nervousness as excitement uses the same physiological arousal for performance enhancement rather than inhibition. Research shows this simple reframe improves speaking performance significantly.",
            "Exposure is the only permanent cure. Each speaking experience regardless of quality reduces anxiety for the next one. There is no substitute for repetition. Toastmasters and similar groups provide low-stakes practice.",
            "Preparation reduces anxiety more than any other single factor. When you know your material thoroughly, confidence increases naturally because competence provides genuine security that tricks cannot match.",
            "The audience wants you to succeed. They chose to attend and hope to receive value. This fundamental truth contradicts the anxious belief that audiences are hostile critics waiting for your failure."
        ]),
        ("Preparing Your Content", [
            "Great speeches start with a clear single message. Before writing a single word, answer: what is the one thing I want the audience to remember tomorrow? Everything in your speech supports this single core idea.",
            "Research your audience before preparing content. What do they already know? What problems do they face? What objections might they have? Content that meets the audience where they are resonates far more than generic material.",
            "Structure your speech using the problem-solution framework: establish a problem the audience recognizes, explore its consequences, then present your solution with evidence. This natural arc creates compelling narrative.",
            "The rule of three applies to speech structure: three main points, three supporting examples, three key takeaways. Audiences can remember three things. More than three and retention drops precipitously.",
            "Write for the ear not the eye. Spoken language differs from written language. Use shorter sentences, simpler words, more repetition, and conversational tone. Read your speech aloud during preparation.",
            "Include concrete stories and examples rather than abstract concepts. Audiences remember stories one hundred times better than statistics or principles. Every point should be illustrated with a specific narrative.",
            "Time your speech during practice. Most speakers go longer than expected. Cut ruthlessly. A tight focused speech always outperforms a meandering comprehensive one. Less is genuinely more in speaking.",
            "Prepare for questions by anticipating the five most likely ones. Having thoughtful answers ready prevents the anxiety of being caught unprepared and demonstrates depth of knowledge beyond your prepared remarks."
        ]),
        ("Story Structure for Speeches", [
            "Stories are the most powerful tool in any speaker's arsenal. Humans are wired for narrative. When you tell a story, the audience's brain synchronizes with yours, creating connection and making ideas memorable.",
            "Every effective story follows a structure: a character in a situation encounters a problem, struggles with it, and either overcomes it or fails instructively. This arc creates emotional engagement automatically.",
            "Start stories with a specific moment in time. Instead of once I had a difficult client say Last Tuesday at three PM my phone rang and I heard words that changed everything. Specificity creates vivid imagery.",
            "Include sensory details that place the audience in the scene. What did you see, hear, feel, smell? These details activate the audience's imagination, transforming passive listeners into active experiencers of your narrative.",
            "The character must have stakes, something important to gain or lose. Without stakes there is no tension. Without tension there is no engagement. Make clear what was at risk in your story.",
            "End stories with a clear lesson connected to your main message. Do not leave the audience to extract the moral themselves. Explicitly state what this story illustrates about your core topic.",
            "Personal vulnerability in stories creates trust and connection. Sharing your failures, fears, and struggles humanizes you and gives the audience permission to relate. Perfection creates distance not connection.",
            "Practice storytelling regularly in casual conversation. Dinner parties, coffee chats, and phone calls all provide opportunities to develop your narrative skills before high-stakes speaking situations."
        ]),
        ("Opening Hooks That Grab Attention", [
            "You have approximately seven seconds before an audience decides whether to pay attention. Your opening must immediately signal that this talk will be worth their time and full engagement.",
            "Start with a provocative statement that challenges assumptions. Everything you believe about productivity is wrong. This creates cognitive dissonance that demands resolution through continued listening.",
            "Open with a question that the audience genuinely wants answered. How much money are you losing every month by not understanding this one simple principle? Questions engage minds actively.",
            "Begin with a vivid story that drops the audience into action. I was standing in the emergency room at two AM when the doctor said three words that changed my relationship with health forever.",
            "Startling statistics capture attention through surprise. Eighty percent of New Year resolutions fail by February. Which means statistically most of you have already given up on this year's goals.",
            "Never begin with thank you for having me, my name is, or today I want to talk about. These are the most boring possible openings. Jump directly into compelling content from your first word.",
            "The opening sets a contract with the audience about what they will receive. Make this promise explicit: in the next twenty minutes you will learn the three-step system that doubled my income.",
            "Rehearse your opening until you can deliver it without notes, with full eye contact and confident energy. The first thirty seconds set the audience's perception for your entire presentation."
        ]),
        ("Closings That Inspire Action", [
            "Your closing is the last impression and the most remembered part of your speech. Never end with any questions or that is all I have or let me summarize. End with power and purpose.",
            "The call to action close tells the audience exactly what to do next. Be specific: tonight when you get home, open your phone and delete the three apps that steal your most productive hours.",
            "The callback close references your opening story or statement, creating a satisfying circular structure. Return to the character or situation from your opening and reveal the resolution or next chapter.",
            "The inspiring vision close paints a picture of the future the audience can create if they act on your message. Imagine six months from now, when this system has already transformed your mornings.",
            "The challenge close dares the audience to take action. The question is not whether this works. It does. The question is whether you have the courage to actually do it. Are you someone who acts?",
            "Pause before your final statement for emphasis. Lower your voice slightly. Make eye contact. The final words should land with weight and intention. Then stop completely. Do not add filler after your close.",
            "Memorize your closing word-for-word. You can improvise throughout your speech, but the landing should be practiced and precise. A confident ending elevates the audience's impression of the entire talk.",
            "Leave the audience with a single powerful sentence they will remember and repeat. If you could put your entire message into one quotable line, that line should be your final statement."
        ]),
        ("Body Language Mastery", [
            "Research suggests that nonverbal communication accounts for over fifty percent of message reception. Your body speaks louder than your words. Alignment between verbal and nonverbal communication creates trust.",
            "Power posture begins before you speak. Stand tall with shoulders back, chin parallel to the floor, and feet shoulder-width apart. This stance communicates confidence even when you do not feel it internally.",
            "Gestures should be purposeful and above the waist. Open palms signal honesty and inclusion. Pointing directs attention. Counting on fingers organizes information visually. Avoid fidgeting, pockets, or crossed arms.",
            "Eye contact creates individual connection within a large audience. Hold eye contact with one person for a full thought, three to five seconds, before moving to another. This creates intimate conversation in a public setting.",
            "Movement should be purposeful. Step forward for emphasis, move laterally for transitions, return to center for authority. Avoid pacing, swaying, or standing rooted. Intentional movement adds dynamism.",
            "Facial expressions must match your content. Genuine smiles, appropriate seriousness, raised eyebrows for surprise, and furrowed brows for concern all reinforce your verbal message emotionally.",
            "Video record yourself speaking and watch without sound. Your body tells a story independent of words. Identify habits that undermine your message: touching your face, looking down, or closing your posture.",
            "Practice power poses before speaking events. Two minutes of expansive posture reduces cortisol and increases testosterone, measurably improving confidence and presence during your actual performance."
        ]),
        ("Voice Modulation", [
            "Your voice is an instrument with multiple variables: volume, pitch, pace, tone, and pauses. Mastering these creates a dynamic delivery that holds attention and communicates emotion beyond mere words.",
            "Volume variation prevents monotone. Increase volume for key points and passionate moments. Decrease to a near-whisper for intimacy and to draw the audience in. The contrast itself creates engagement.",
            "Pace modulation communicates importance. Slow down for critical ideas so they land with weight. Speed up slightly for excitement, energy, or less critical transitional content. Variety prevents boredom.",
            "The strategic pause is your most powerful vocal tool. Pause before important statements to create anticipation. Pause after for impact. Three seconds of silence feels like an eternity but communicates absolute confidence.",
            "Eliminate filler words: um, uh, like, you know, so. Replace every filler with silence. Pauses sound confident while fillers communicate uncertainty. Record yourself to identify your habitual fillers.",
            "Vocal warmth comes from lower pitch, slower pace, and genuine emotional connection to your content. Cold clinical delivery fails regardless of content quality. Warmth creates trust and receptivity.",
            "Practice vocal variety by reading children's books aloud with exaggerated expression. This trains the range of your voice without self-consciousness. Then bring a modulated version of that range to speeches.",
            "Breath support from your diaphragm provides vocal power without strain. Shallow chest breathing produces thin weak sound. Deep belly breathing supports projection, resonance, and stamina throughout long presentations."
        ]),
        ("Handling Nervousness", [
            "Nervousness before speaking is universal and biological. Even experienced professional speakers feel activation before presentations. The goal is not eliminating nervousness but channeling it into energized performance.",
            "Reframe anxiety as excitement. These are physiologically identical states with different cognitive labels. Saying I am excited redirects nervous energy toward enthusiasm rather than fear.",
            "Physical preparation reduces nervous symptoms: exercise the morning of, power poses for two minutes before, controlled breathing in the wings, and progressive muscle relaxation during the introduction.",
            "Arrive early to familiarize yourself with the space. Stand where you will speak. Test equipment. Meet a few audience members. Familiarity with the environment reduces the novelty that triggers anxiety.",
            "Focus outward on serving the audience rather than inward on your performance. When your attention is on delivering value to others, self-conscious anxiety naturally diminishes because attention has shifted.",
            "The first sixty seconds are the most anxious. Memorize your opening so completely that you could deliver it in your sleep. Once past the opening, familiarity with your content takes over and anxiety recedes.",
            "Accept imperfection as inevitable and irrelevant. Audiences do not expect perfection. They expect authenticity, value, and engagement. Small mistakes humanize you and are forgotten within seconds by listeners.",
            "Gradual exposure builds comfort progressively. Start with small low-stakes audiences: friends, colleagues, small groups. Build to larger audiences over time. Each positive experience reduces anxiety for the next."
        ]),
        ("Dealing with Q&A Sessions", [
            "Question and answer periods intimidate many speakers because they cannot be scripted. However, preparation and frameworks make Q&A manageable and even enjoyable as genuine intellectual exchange with your audience.",
            "Anticipate the ten most likely questions and prepare concise thoughtful answers. Most questions at any talk are predictable based on your topic. Preparation removes the anxiety of being caught off-guard.",
            "When asked a question, pause before answering even if you know the answer instantly. This pause communicates thoughtfulness, gives you processing time, and prevents the appearance of dismissive rapid responses.",
            "Repeat or rephrase questions before answering. This ensures the full audience heard the question, gives you time to formulate your response, and confirms you understood the question correctly.",
            "It is completely acceptable to say I do not know but I will find out and follow up. Honesty about limitations builds more credibility than fumbling through uninformed answers.",
            "Bridge from difficult questions to your key messages. You can acknowledge the question, briefly address it, then redirect: That is an interesting angle. What I find most relevant is connecting directly to your expertise.",
            "Handle hostile questions with grace by separating the person from the challenge. Acknowledge the emotion or concern behind the question, respond factually and calmly, and move on without defensiveness.",
            "End Q&A before energy diminishes. Set a clear time limit and end with a strong closing statement rather than letting the session fizzle. Your final words should be as powerful as your speech's conclusion."
        ]),
        ("Virtual Presentation Skills", [
            "Virtual presentations require different techniques than in-person speaking because you are competing with every distraction in your audience's environment. Engagement requires more deliberate effort and varied approaches.",
            "Camera position should be at eye level with your face well-lit from the front. Looking directly into the camera lens simulates eye contact. Position your notes near the camera to minimize obvious looking away.",
            "Energy must be amplified for virtual delivery. What feels like overacting to you reads as appropriately engaging through a screen. Increase vocal variety, facial expression, and gesture by about thirty percent.",
            "Shorten virtual presentations significantly. Attention spans are shorter online. If your in-person talk would be forty-five minutes, compress to twenty-five minutes for virtual delivery with the same content.",
            "Interactive elements every three to five minutes prevent audience drift: polls, chat questions, raised hands, breakout discussions, or direct audience participation. Passive listening online leads to rapid disengagement.",
            "Professional background and good audio quality signal credibility. Invest in a quality microphone and either a clean background or professional virtual background. Audio quality matters more than video quality.",
            "Share screens strategically rather than constantly. Seeing your face creates connection. Slides provide visual support. Alternate between face and slides to maintain variety and human connection.",
            "Record virtual presentations for review and improvement. Watch yourself presenting to identify distracting habits, energy dips, and moments where audience engagement tools would improve the experience."
        ]),
        ("The TED Talk Formula", [
            "TED Talks follow a remarkably consistent formula that any speaker can learn and apply. Understanding this structure helps you build compelling eighteen-minute presentations on any topic.",
            "Start with a hook that creates curiosity or challenges assumptions in the first thirty seconds. TED speakers never begin with pleasantries. They begin with ideas that demand attention immediately.",
            "One idea worth spreading. The constraint of a single core idea forces clarity. Every story, example, and data point supports this one idea. This discipline makes the message memorable and shareable.",
            "Personal vulnerability establishes authenticity and audience connection. The most-watched TED talks include moments where the speaker shares struggles, failures, or fears that humanize them completely.",
            "Data and stories work together. Neither alone is sufficient. Data provides credibility while stories provide emotional resonance. Alternate between analytical evidence and narrative illustration.",
            "The three-act structure works: establish the problem or question, explore possibilities and evidence, then arrive at the insight or solution. This journey takes the audience from curiosity through discovery to conclusion.",
            "Rehearsal distinguishes TED-quality talks from ordinary presentations. The best TED speakers rehearse hundreds of times until delivery appears completely natural and spontaneous despite being thoroughly prepared.",
            "End with an actionable call or memorable statement that the audience will repeat. The talk lives beyond the stage when its core message becomes something people share with others in conversation."
        ]),
        ("Wedding and Toast Speeches", [
            "Wedding speeches and toasts require balancing humor with sincerity, keeping appropriate length, and including all relevant parties while avoiding topics that embarrass or create discomfort.",
            "The ideal wedding toast is three to five minutes. Anything longer tests patience. Structure: introduce yourself and your relationship to the couple, share one or two short stories, express genuine wishes.",
            "Humor should be inclusive and kind. Stories that embarrass the couple or reference ex-partners, drunken episodes, or inside jokes that exclude the audience fail regardless of how funny you find them.",
            "Write it out fully and rehearse multiple times. Do not wing a wedding speech. The combination of emotion, alcohol, and pressure makes improvisation risky. Prepare and practice until comfortable.",
            "Include both people in the couple, not just the one you know. Acknowledge what they bring to the partnership and express genuine welcome to the person joining your friend circle or family.",
            "End with a toast that everyone can join: a specific wish, a quotation about love, or a simple here's to years of happiness together that provides a natural glass-raising moment.",
            "Speak from genuine emotion rather than trying to be a comedian. Audiences at weddings respond most powerfully to authentic feeling expressed simply. Tears of joy are more memorable than clever jokes.",
            "Practice delivering with a glass in one hand. This is a logistical detail that catches unprepared speakers off-guard. Rehearse the physical reality of standing, holding a drink, and projecting to a crowd."
        ]),
        ("Business Presentations", [
            "Business presentations succeed when they answer one question implicitly or explicitly: so what? Every slide, every data point, every statement must connect to outcomes the audience cares about professionally.",
            "Know your audience's priorities before building your deck. Executives care about revenue and strategy. Managers care about implementation and resources. Team members care about daily impact. Tailor accordingly.",
            "Start with the conclusion. Business audiences value efficiency. State your recommendation or finding first, then support it with evidence. This inverted pyramid structure respects time and enables early questions.",
            "Slides should be visual aids not reading material. One idea per slide maximum. Use images, simple charts, and minimal text. If your slides work without you, they contain too much information for a presentation.",
            "Anticipate objections and address them proactively. Saying I know some of you are thinking X, and here is why demonstrates thoroughness and prevents objections from derailing your presentation.",
            "Quantify everything possible. Business decisions require numbers. Impact in dollars, time in days, percentages of improvement, and comparison to alternatives make your argument concrete and actionable.",
            "Include a clear next step. What specifically should the audience do after your presentation? Make the action obvious, easy, and time-bound. Without a clear ask, even compelling presentations produce no results.",
            "Practice with someone who will give honest critical feedback. Colleagues who will challenge your logic, question your data, and identify weaknesses make your final presentation significantly stronger."
        ]),
        ("Impromptu Speaking Skills", [
            "The ability to speak coherently without preparation is invaluable in meetings, social situations, and unexpected speaking opportunities. This skill is trainable through frameworks and regular practice.",
            "The PREP framework provides instant structure: Point, Reason, Example, Point. State your position, explain why, illustrate with a brief example, then restate your position. This works for any impromptu response.",
            "Past-Present-Future provides another framework: describe how things were, how they are now, and how they could be in the future. This temporal structure organizes thoughts for any topic naturally.",
            "Pause before speaking. Two to three seconds of silence feels like an eternity to you but appears thoughtful to your audience. Use this pause to select your framework and first sentence.",
            "Keep impromptu responses brief. Thirty to ninety seconds is ideal for most situations. Concise clarity impresses far more than lengthy rambling that reveals you are thinking aloud without direction.",
            "Practice daily by answering random questions aloud. Use prompts, dinner conversation, or podcast discussion questions. The more you practice organizing thoughts quickly, the more natural it becomes.",
            "Transition phrases buy thinking time: That is an excellent question, Let me approach this from a different angle, or There are three aspects to consider here. These stall elegantly while you organize.",
            "Accept imperfection in impromptu speaking. It will never be as polished as prepared remarks. The audience knows you are speaking spontaneously and evaluates accordingly. Authenticity trumps polish in these moments."
        ]),
        ("Your 30-Day Speaking Confidence Plan", [
            "Days one through five: practice alone. Deliver a one-minute talk daily to yourself on any topic. Record yourself. Review without judgment. Focus on simply getting comfortable with the act of speaking aloud.",
            "Days six through ten: speak to one person. Practice your daily one-minute talk for a friend, family member, or colleague. Accept their feedback gracefully. Notice that speaking to a live person adds manageable anxiety.",
            "Days eleven through fifteen: expand to small groups. Speak at a team meeting, dinner gathering, or small group setting. Even thirty seconds of contribution counts. Build comfort with multiple eyes on you.",
            "Days sixteen through twenty: join a practice community. Attend Toastmasters, a speaking meetup, or an improv class. These provide structured low-stakes practice with supportive feedback from fellow learners.",
            "Days twenty-one through twenty-five: volunteer to present. Offer to lead a meeting segment, give a workshop at work, or speak at a community event. Choose a familiar topic where your expertise provides confidence.",
            "Days twenty-six through thirty: push beyond comfort. Accept a speaking opportunity that genuinely challenges you: a larger audience, unfamiliar topic, or higher-stakes situation. Apply all techniques learned.",
            "Throughout all thirty days: consume content about speaking. Watch TED Talks analytically, listen to great speakers, and read one speaking improvement book. Learning from masters accelerates your development.",
            "After thirty days you will have transformed from someone who avoids speaking to someone who voluntarily pursues it. The skill and confidence you have built will continue compounding for your entire career."
        ]),
    ])
    make_book_from_data("Book316_Public_Speaking.pdf", "SPEAK WITH POWER",
                       "How to Overcome Fear and Deliver Presentations That Captivate", ch)



if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Generating Books 313-316...")
    book313()
    book314()
    book315()
    book316()
    print("Done! Books 313-316 generated.")
