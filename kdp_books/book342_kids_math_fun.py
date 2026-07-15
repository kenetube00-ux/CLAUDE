from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    chapters = [
        ("Math in Cooking", "Fractions are everywhere in the kitchen! When you follow a recipe, you use fractions: 1/2 cup of sugar, 3/4 teaspoon of salt, 1/3 of the dough. When you double or halve a recipe, you multiply or divide fractions. Understanding fractions through cooking makes them real and delicious!",
         "If a recipe serves 4 and you need to feed 6, what do you multiply by? If you need 3/4 cup of flour but you're doubling the recipe, how much do you need? These are real-world fractions you'll use for life!",
         ["You have 3/4 cup flour and need to double it. How much? (3/4 x 2 = ?)","A recipe serves 8. You want to serve 4. Cut all ingredients by what fraction?","If you eat 2/8 of a pizza, what fraction is that in simplest form?","A cake needs 2 1/2 cups sugar. You're making 3 cakes. Total sugar needed?","You have 1/3 of a bag of chocolate chips. You need to split it 4 ways. Each person gets?"]),
        ("Math in Sports", "Sports are FULL of math! Batting averages in baseball are decimals. Basketball stats use percentages. Football uses geometry (angles of throws). Soccer uses probability. Even fantasy sports require statistical thinking! Athletes and coaches use math constantly to improve performance.",
         "If a basketball player makes 7 out of 10 free throws, their shooting percentage is 70%. If they shoot 100 free throws in a season, you'd predict they'd make about 70!",
         ["A baseball player gets 3 hits in 10 at-bats. What's their batting average?","A team won 15 of 20 games. What's their win percentage?","A runner's times for 5 races: 12.1, 11.8, 12.3, 11.9, 12.0. What's the average?","A quarterback throws 25 passes, completes 15. Completion rate?","A soccer goalie blocks 8 of 12 shots. Save percentage?"]),
        ("Math in Shopping", "Every time you shop, you use math! Percentages help with sales (30% off!), unit prices help you compare deals, tax adds to your total, and budgeting requires addition and subtraction. Being good at shopping math saves you REAL money throughout your entire life.",
         "A $50 video game is 20% off. That's $50 x 0.20 = $10 savings. New price: $40. But with 8% tax: $40 x 1.08 = $43.20. Mental math like this makes you a smart consumer!",
         ["A shirt costs $25 and is 40% off. What's the sale price?","Which is cheaper per ounce: 12 oz for $3.60 or 16 oz for $4.48?","You have $100. After buying items for $23, $17, and $45, what's left?","A $80 item with 25% off, then 10% tax. Final price?","If you save $5/week, how many weeks to buy a $75 game?"]),
        ("Math in Building", "Every building, bridge, and structure uses geometry! Right angles keep walls straight. Triangles provide strength. Circles create domes and arches. Area tells you how much material you need. Volume tells you how much space something holds. Architects and engineers are geometry experts!",
         "To build a treehouse with a floor that's 8 feet by 6 feet, you need to know the area: 8 x 6 = 48 square feet of wood. Want to add diagonal bracing? Use the Pythagorean theorem!",
         ["Find the area of a rectangular room that's 12 ft by 10 ft.","A circular garden has radius 5 ft. What's its area? (pi x r squared)","A triangle has base 6 cm and height 8 cm. Area? (1/2 x base x height)","A box is 3ft x 2ft x 4ft. What's the volume?","A right triangle has legs 3 and 4. What's the hypotenuse? (a2 + b2 = c2)"]),
        ("Math in Nature", "Nature is secretly mathematical! Sunflower seeds grow in Fibonacci spirals. Snowflakes have 6-fold symmetry. Honeybees build hexagonal cells (most efficient shape). Tree branches follow mathematical patterns. The golden ratio appears in shells, hurricanes, and galaxies!",
         "The Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34... Each number is the sum of the two before it. This pattern appears in flower petals, pine cones, and pineapple scales!",
         ["Continue the Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, ?, ?, ?","Count petals on 5 flowers. Are any Fibonacci numbers? (3, 5, 8, 13, 21)","How many sides does a snowflake have? What about a honeycomb cell?","Find the pattern: 2, 4, 8, 16, ___, ___, ___","Find a spiral in nature. How does it relate to math?"]),
        ("Math in Music", "Music IS math! Rhythm is fractions (whole notes, half notes, quarter notes). Frequency determines pitch (doubling frequency = one octave higher). Time signatures are fractions. Even harmonious chords are mathematical ratios! Musicians use math whether they know it or not.",
         "In 4/4 time, each measure has 4 beats. A whole note = 4 beats. A half note = 2. A quarter note = 1. A measure could be: 1 half note + 2 quarter notes = 2 + 1 + 1 = 4 beats!",
         ["How many quarter notes fit in one measure of 4/4 time?","If a song is 3 minutes at 120 beats per minute, total beats?","A half note + a quarter note + ___ = one full measure (4/4 time)?","If you practice 30 min/day for 365 days, how many hours total?","Concert A is 440 Hz. One octave up is double. What frequency?"]),
        ("Math in Art", "Artists use math for symmetry, proportion, perspective, and patterns! The golden ratio (1.618) creates aesthetically pleasing compositions. Tessellations (repeating patterns with no gaps) are pure geometry. Even color mixing uses mathematical proportions. Art and math are creative partners!",
         "Symmetry means both sides match. A butterfly has bilateral symmetry (one line of symmetry). A snowflake has 6 lines of symmetry. A circle has infinite lines of symmetry!",
         ["Draw a shape with exactly 1 line of symmetry, 2 lines, and 4 lines.","Create a tessellation using only triangles (no gaps, no overlaps).","What fraction of a color wheel is red? Blue? Yellow?","Scale up a drawing: if original is 2x3 inches, what's 3x bigger?","Draw a simple picture using only geometric shapes."]),
        ("Math in Games", "Games use probability everywhere! Rolling dice, drawing cards, spinning spinners - all probability. Understanding odds helps you make better decisions in games (and life!). Expected value tells you which choices give the best average outcome over time.",
         "When you roll one die, the probability of getting a 6 is 1/6 (about 17%). With two dice, the probability of getting a total of 7 is 6/36 = 1/6. Seven is the most common roll!",
         ["What's the probability of flipping heads on a coin? (express as fraction)","Rolling a die: what's the chance of getting an even number?","Drawing from a deck: chance of getting a heart? A face card?","If you flip 3 coins, how many possible outcomes? List them.","Rolling 2 dice: which total (2-12) is most likely? Why?"]),
        ("Math in Travel", "Road trips use math constantly! Distance = speed x time. If you're going 60 mph, you'll cover 180 miles in 3 hours. Time zones require addition/subtraction. Currency exchange uses multiplication. Map scales convert inches to miles. Travel is one big math adventure!",
         "If your car goes 60 mph and your destination is 300 miles away, travel time = 300/60 = 5 hours. If you leave at 9 AM, you arrive at 2 PM!",
         ["If driving 55 mph for 4 hours, how far do you travel?","A flight leaves at 3PM Eastern, takes 5 hours. Pacific time arrival? (3 hours behind)","A map scale is 1 inch = 50 miles. Two cities are 3.5 inches apart. Real distance?","$1 USD = 0.85 Euros. How many euros for $100?","A car uses 1 gallon per 30 miles. For 450 miles, how many gallons needed?"]),
        ("Math in Money", "Compound interest is the most important math concept for building wealth! If you invest $100 at 10% annual interest: Year 1 = $110, Year 2 = $121, Year 3 = $133.10. The interest earns interest! This is why starting to save young is SO powerful - time is your greatest ally.",
         "The Rule of 72: divide 72 by your interest rate to find how many years it takes to DOUBLE your money. At 8% interest, 72/8 = 9 years to double!",
         ["If you invest $100 at 10% interest, how much after 1 year? After 2 years?","Using Rule of 72: at 6% interest, how many years to double your money?","You save $10/week for 1 year. Total saved? If it earns 5% interest, year-end total?","A bank offers 3% vs 5% interest on $1000. Difference after 1 year?","If $500 doubles every 9 years, how much in 27 years?"]),
        ("Math in Space", "Space involves ENORMOUS numbers! The Sun is 93 million miles away. Light travels 186,000 miles per SECOND. The Milky Way has 200 billion stars. These astronomical numbers require scientific notation and help us grasp the incredible scale of the universe.",
         "Light travels at 186,000 miles/second. In one year, light travels about 5.88 TRILLION miles. That distance is called a light-year. The nearest star is 4.2 light-years away!",
         ["Light takes 8 min to reach Earth from the Sun. Distance = 186,000 x 480 sec = ?","Jupiter is 5 times farther from the Sun than Earth (93M mi). Jupiter's distance?","If a rocket goes 25,000 mph, how many hours to reach the Moon (238,900 mi)?","Write one million in scientific notation (10 to the what power?)","The Milky Way has 200 billion stars. Write in scientific notation."]),
        ("Math Puzzles & Riddles", "Math puzzles make your brain stronger! They teach creative problem-solving, logical thinking, and persistence. Some puzzles that stumped adults for years were solved by kids who thought differently. Try these 20 puzzles - some are tricky!",
         "A classic: A bat and ball cost $1.10 total. The bat costs $1 more than the ball. How much does the ball cost? (Hint: it's NOT $0.10!)",
         ["I am thinking of a number. I double it, add 6, and get 20. What's my number?","If 3 cats catch 3 mice in 3 minutes, how many cats catch 100 mice in 100 min?","A farmer has 17 sheep. All but 9 escape. How many are left?","Fill in: 1, 4, 9, 16, 25, ___, ___, ___ (what's the pattern?)","You have 8 balls. One is heavier. Using a balance scale twice, find it. How?"]),
        ("Math Tricks to Impress Friends", "These 10 tricks will make you look like a math genius! They all use mathematical properties in clever ways that seem like magic but are actually just smart math.",
         "The 9 Times Table Trick: Hold up 10 fingers. To multiply 9 x 4, put down finger #4. You have 3 fingers on the left and 6 on the right. Answer: 36!",
         ["Multiply any 2-digit number by 11: e.g., 36 x 11 = put 3+6=9 in middle = 396!","To square any number ending in 5: 35 squared = 3x4=12, then add 25 = 1225","Divisibility by 3: if digits add up to a multiple of 3, the number is divisible by 3","Mental math: to add 99, add 100 then subtract 1. E.g., 456+99 = 556-1 = 555","Percent trick: x% of y = y% of x. So 8% of 50 = 50% of 8 = 4!"]),
        ("Famous Mathematicians", "Math was built by brilliant people from all over the world! From ancient civilizations to modern geniuses, mathematicians discovered the rules that govern our universe. Their stories show that math talent comes in all shapes, sizes, genders, and backgrounds.",
         "Katherine Johnson (1918-2020) calculated trajectories for NASA space missions by HAND. Her math sent astronauts to the Moon! The movie 'Hidden Figures' tells her incredible story.",
         ["Research one mathematician and write 5 facts about them","Pythagoras, Euclid, Fibonacci, Newton, Euler, Gauss, Ramanujan, Katherine Johnson","Ada Lovelace wrote the first computer program in 1843!","Maryam Mirzakhani was the first woman to win math's top prize (Fields Medal)","Who is your favorite? What did they discover?"]),
        ("Your Math Adventure Journal", "This final chapter is YOUR space to practice math in the real world! Look for math everywhere you go this month. Record what you find, solve problems you encounter, and create your own math challenges. The more you see math in daily life, the more natural and fun it becomes!",
         "Challenge yourself to find math in at least 3 situations every day for 30 days!",
         ["Day 1-7: Track math you encounter daily (shopping, cooking, games, etc.)","Day 8-14: Create 5 word problems based on your real life","Day 15-21: Teach someone a math trick. Did they learn it?","Day 22-28: Find math in nature, art, and music around you","Day 29-30: Write about how math is connected to your future dreams"]),
    ]

    title_page(doc, "MATH IS EVERYWHERE", "A Fun Guide to Numbers in Real Life (Ages 8-13)", "15 Chapters * Real-World Math * Puzzles * Tricks * Activities")
    copyright_page(doc, "MATH IS EVERYWHERE: A Fun Guide to Numbers in Real Life")
    toc_page(doc, [c[0] for c in chapters])

    for idx, (ch_title, content, wow_fact, problems) in enumerate(chapters):
        chapter_header(doc, idx+1, ch_title)
        y = 580
        y = add_wrapped(doc, 72, y, content, 'F1', 11, 0.2)
        y -= 20
        doc.add_text(72, y, "WOW FACT:", 'F2', 12, 0.1)
        y -= 18
        y = add_wrapped(doc, 90, y, wow_fact, 'F4', 11, 0.3)
        doc.new_page()

        # Practice problems
        doc.add_centered_text(720, f"CHAPTER {idx+1}: PRACTICE", 'F2', 16, 0)
        doc.add_line(200, 710, 412, 710, 1, 0.3)
        y = 685
        for i, prob in enumerate(problems):
            doc.add_text(72, y, f"Problem {i+1}:", 'F2', 10, 0.1)
            y -= 16
            y = add_wrapped(doc, 90, y, prob, 'F1', 10, 0.2, 68)
            y -= 8
            doc.add_text(90, y, "Answer: ___________________", 'F1', 10, 0.4)
            y -= 25
        
        y -= 15
        doc.add_text(72, y, "CHALLENGE PROBLEM:", 'F2', 12, 0.1)
        y -= 18
        doc.add_text(90, y, "Create your own real-world math problem based on this chapter:", 'F4', 10, 0.3)
        y -= 16
        doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
        y -= 16
        doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
        doc.new_page()

    certificate(doc, "MATH CHAMPION CERTIFICATE")
    add_supplemental(doc, 'Math', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book342_Kids_Math_Fun.pdf')
    print("Book342_Kids_Math_Fun.pdf created successfully!")

if __name__ == "__main__":
    create_book()
