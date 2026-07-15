from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    systems = [
        ("The Skeletal System: Your Frame", "Your skeleton is made up of 206 bones that give your body shape, protect your organs, and help you move. When you were born, you had about 270 bones! Many fused together as you grew. Bones are alive - they grow, heal when broken, and make new blood cells inside their marrow. The smallest bone is in your ear (size of a rice grain). The largest is your thigh bone (femur).",
         ["Babies have about 270 bones, adults have 206 (some fuse together)", "Your skeleton replaces itself completely every 10 years", "Bones are stronger than steel pound-for-pound", "The hyoid bone (in your throat) is the only bone not connected to another bone", "You have 27 bones in each hand - that's 54 total!"],
         "Without your skeleton, you'd be like a jellyfish - a blob on the floor! Your skull protects your brain like a helmet, your ribs protect your heart and lungs like a cage, and your spine holds you upright.", "Eat calcium-rich foods (milk, cheese, broccoli), do weight-bearing exercise, and avoid soda (it can weaken bones)."),
        ("The Muscular System: Your Movers", "You have over 600 muscles that help you move, pump blood, and digest food! There are 3 types: skeletal muscles (you control), smooth muscles (automatic, in organs), and cardiac muscle (your heart - never stops!). Muscles work by contracting (getting shorter). They always work in pairs - one pulls while the other relaxes.",
         ["Your heart beats about 100,000 times per day", "The strongest muscle relative to size is the masseter (jaw muscle)", "Muscles make up 40% of your body weight", "It takes 17 muscles to smile and 43 to frown", "Your tongue is actually 8 muscles working together"],
         "Without muscles, you couldn't blink, breathe, speak, or move at all. Even sitting up straight requires hundreds of muscles working together constantly.", "Exercise regularly, eat protein (helps muscles repair), stretch to stay flexible, and get enough sleep (muscles repair while you sleep)."),
        ("The Digestive System: Food Factory", "From mouth to exit, your digestive system is about 30 feet long! It breaks down food into nutrients your body can use for energy, growth, and repair. The process takes 24-72 hours. Your stomach uses acid strong enough to dissolve metal! But a special mucus lining protects the stomach from digesting itself.",
         ["Your mouth produces about 1 liter of saliva per day", "Your stomach acid (pH 1-3) could dissolve a nail", "The small intestine is about 22 feet long!", "Your large intestine absorbs water (about 1.5 liters daily)", "You'll eat about 60,000 pounds of food in your lifetime"],
         "Without your digestive system, your body would have no energy, no building materials for growth, and no fuel for your brain. You'd literally starve.", "Eat fiber (fruits, veggies, whole grains), drink plenty of water, chew food thoroughly, and don't rush meals."),
        ("The Circulatory System: River of Life", "Your heart pumps blood through 60,000 miles of blood vessels - that's enough to wrap around Earth 2.5 times! Blood carries oxygen and nutrients to every cell and picks up waste. Red blood cells carry oxygen, white blood cells fight germs, and platelets help you stop bleeding when you get a cut.",
         ["Your heart pumps about 2,000 gallons of blood per day", "Red blood cells live about 120 days then are replaced", "Your body makes about 2 million red blood cells every SECOND", "All your blood vessels laid end-to-end would stretch 60,000 miles", "Blood takes about 20 seconds to circulate through your entire body"],
         "Without your circulatory system, no oxygen could reach your cells. Your brain would shut down in 4 minutes, and all other organs would quickly follow.", "Exercise (strengthens your heart), eat healthy fats (not trans fats), limit salt, stay hydrated, and don't smoke (ever!)."),
        ("The Respiratory System: Breathing Machine", "You breathe about 20,000 times per day without even thinking about it! Your lungs bring in oxygen (which cells need to make energy) and remove carbon dioxide (a waste product). If you spread out all the tiny air sacs in your lungs, they'd cover a tennis court! Your diaphragm muscle controls breathing.",
         ["You breathe about 20,000 times per day", "Your lungs contain 300 million tiny air sacs (alveoli)", "The surface area of your lungs equals a tennis court", "You can survive minutes without breathing (trained divers: 20+ min)", "Yawning brings extra oxygen to your brain when you're tired"],
         "Without breathing, your cells would run out of oxygen in minutes. Your brain is the first organ to be damaged - after just 4 minutes without oxygen.", "Exercise to increase lung capacity, breathe through your nose (filters air), avoid polluted areas, NEVER smoke, and practice deep breathing."),
        ("The Nervous System: Command Center", "Your brain has 86 BILLION neurons (nerve cells) connected by 100 TRILLION connections! It processes information faster than any computer. Your nervous system has two parts: the central (brain + spinal cord) and peripheral (nerves to your whole body). Nerve signals travel up to 268 mph!",
         ["Your brain uses 20% of your body's energy (despite being 2% of weight)", "Nerve signals travel up to 268 mph", "Your brain generates enough electricity to power a light bulb", "You have more neural connections than stars in the Milky Way", "Your spinal cord stops growing at age 4 (even though you keep growing)"],
         "Without your nervous system, you couldn't think, feel, move, see, hear, taste, smell, or remember anything. You wouldn't even be able to breathe.", "Sleep 8-10 hours (brain repairs itself during sleep), exercise, eat healthy fats, challenge your brain with puzzles, and protect your head."),
        ("The Immune System: Defense Army", "Your immune system is like a military force protecting you from billions of germs trying to invade every day! It has multiple layers of defense: skin (the wall), mucus (the moat), white blood cells (soldiers), and antibodies (targeted missiles). Once it beats a germ, it REMEMBERS it - that's why you usually only get chickenpox once.",
         ["Your skin is the largest organ and first line of defense", "White blood cells can eat germs (like Pac-Man!)", "Fever is your body turning up the heat to kill germs", "You have about 5 liters of blood full of immune cells", "Vaccines train your immune system without making you sick"],
         "Without your immune system, a simple cold could kill you. People with immune disorders must live in sterile bubbles to avoid ANY germs.", "Wash hands frequently, sleep enough, eat fruits and vegetables, exercise, manage stress, and get recommended vaccines."),
        ("The Endocrine System: Chemical Messengers", "Hormones are chemical messengers that control almost everything in your body: growth, mood, energy, hunger, sleep, and puberty! Glands throughout your body release these hormones into your blood. It's like your body's email system - sending messages to organs telling them what to do.",
         ["The pituitary gland (pea-sized) is the 'master gland' controlling others", "Adrenaline (fight-or-flight hormone) makes you faster and stronger temporarily", "Growth hormone is released mostly during deep sleep", "Insulin (from pancreas) controls blood sugar levels", "Puberty hormones trigger the changes from child to adult body"],
         "Without hormones, you wouldn't grow, couldn't regulate energy, would have no sleep/wake cycle, and couldn't respond to danger.", "Sleep at regular times, eat balanced meals, exercise regularly, manage stress (cortisol is a stress hormone), and drink enough water."),
        ("Your Skin: Living Armor", "Skin is your largest organ - spread out, it would cover about 20 square feet! It's waterproof, stretchy, self-healing, and packed with nerve endings. You shed about 40,000 dead skin cells every HOUR. Your skin protects you from germs, UV radiation, and helps regulate body temperature through sweating.",
         ["You shed 40,000 dead skin cells every hour (about 8 pounds/year)", "Your skin is home to 1,000+ species of bacteria (most are helpful!)", "Skin completely renews itself every 2-3 weeks", "The thinnest skin is on your eyelids; thickest on your feet", "Goosebumps are from tiny muscles trying to fluff up hair you don't have much of anymore"],
         "Without skin, you'd dehydrate instantly and have zero protection from germs. Every bacteria and virus in the air could enter your body.", "Wear sunscreen, stay hydrated, don't pick at wounds, wash gently, eat foods with vitamins A, C, and E."),
        ("Your Five Senses: Body Detectors", "Your senses are how you experience the world! SIGHT: Eyes detect light (you can see a candle flame from 30 miles away on a clear night!). HEARING: Ears detect sound vibrations. TASTE: Tongue has 10,000 taste buds. SMELL: Nose can detect 1 trillion scents. TOUCH: Skin has millions of nerve endings.",
         ["Your eyes can distinguish about 10 million different colors", "You can hear sounds from 20 Hz to 20,000 Hz", "Your nose can detect 1 TRILLION different scents", "Taste buds only live 10-14 days before being replaced", "Fingertips have the most touch receptors per square inch"],
         "Without senses, you'd have no information about the world around you - no beauty, no music, no flavor, no warmth, no warning of danger.", "Protect your ears from loud noise, wear sunglasses in bright sun, don't stare at screens too long, and eat a varied diet for full taste experiences."),
        ("Growth & Development", "From conception to adulthood, your body undergoes incredible transformations! In the first year, babies typically triple their birth weight. Growth plates in bones allow you to grow taller until about age 18-25. Puberty triggers major changes controlled by hormones. Your brain doesn't fully mature until about age 25!",
         ["Babies grow fastest - doubling birth weight by 5 months", "You're tallest in the morning (gravity compresses your spine during the day)", "Teenagers need 8-10 hours of sleep because growth hormone peaks during deep sleep", "Your brain's prefrontal cortex (decision-making) isn't fully developed until 25", "Regular exercise during growth years builds stronger bones for life"],
         "Without proper nutrition and care during growth years, the body can't develop normally. What you eat and do NOW affects your body for life.", "Get plenty of sleep (growth happens while sleeping!), eat nutritious food, exercise daily, manage stress, and be patient with your changing body."),
        ("Taking Care of Your Body", "You only get ONE body for your entire life - taking care of it is the most important investment you can make! The earlier you build healthy habits, the better your life will be. Eat a variety of foods, move your body daily, sleep enough, manage stress, and avoid harmful substances. Your future self will thank you!",
         ["Exercise at least 60 minutes daily for optimal health", "Kids ages 6-12 need 9-12 hours of sleep per night", "Drinking water (6-8 cups/day) keeps everything working properly", "Limiting screen time to 2 hours improves sleep and mood", "Regular check-ups help catch problems early"],
         "Without proper self-care, your body breaks down over time. People who build healthy habits young live longer, happier, and more energetic lives.", "Create a daily routine: exercise, healthy meals, enough water, limited screens, good sleep, stress management, and regular hygiene."),
    ]

    title_page(doc, "THE AMAZING HUMAN BODY", "A Kid's Guide to How You Work (Ages 7-12)", "12 Body Systems * Fun Facts * Experiments * Health Tips")
    copyright_page(doc, "THE AMAZING HUMAN BODY: A Kid's Guide")
    toc_page(doc, [s[0] for s in systems])

    for idx, (title, content, facts, scenario, tips) in enumerate(systems):
        chapter_header(doc, idx+1, title)
        y = 580
        y = add_wrapped(doc, 72, y, content, 'F1', 11, 0.2)
        doc.new_page()

        # Facts page
        doc.add_centered_text(720, f"CHAPTER {idx+1}: FUN FACTS", 'F2', 16, 0)
        doc.add_line(200, 710, 412, 710, 1, 0.3)
        y = 680
        for i, fact in enumerate(facts):
            doc.add_filled_rect(60, y-5, 492, 30, 0.95)
            lines = wrap(fact, 70)
            for j, l in enumerate(lines):
                doc.add_text(80, y + (10 if j == 0 else -8), f"{'* ' if j==0 else '  '}{l}", 'F1', 10, 0.2)
            y -= 50

        y -= 20
        doc.add_text(72, y, "IF THIS SYSTEM STOPPED...", 'F2', 13, 0.1)
        y -= 20
        y = add_wrapped(doc, 90, y, scenario, 'F4', 11, 0.3)
        
        y -= 25
        doc.add_text(72, y, "HEALTH TIPS:", 'F2', 13, 0.1)
        y -= 20
        y = add_wrapped(doc, 90, y, tips, 'F1', 11, 0.2)
        doc.new_page()

        # Activity page
        doc.add_centered_text(720, f"CHAPTER {idx+1}: EXPERIMENT", 'F2', 16, 0)
        experiments = [
            "Feel your bones: Press on your arm. Feel hard bone and soft muscle. Find your kneecap (patella) - it moves! Count how many joints you can find.",
            "Muscle test: Hold a heavy book at arm's length. Time how long before your arm shakes. That's muscle fatigue! Rest and try again - is it shorter?",
            "Digestion timer: Note when you eat lunch. Track when you feel hungry again. That's roughly how long digestion takes in your stomach (3-4 hours).",
            "Pulse finder: Find your pulse on your wrist. Count beats for 15 seconds, multiply by 4. Do jumping jacks for 1 minute. Measure again! What changed?",
            "Lung capacity: Take the deepest breath possible. Blow into a balloon. Compare balloon size with a friend. Exercise improves lung capacity!",
            "Reflex test: Have someone drop a ruler. Catch it as fast as you can. Measure where you caught it - lower = faster reflexes. That's your nervous system!",
            "Germ test: Put hand on bread, seal in bag. Leave another bread slice untouched in a bag. After 5 days, compare mold growth. Germs are everywhere!",
            "Energy test: Notice your energy at different times. When are you most awake? Most tired? That's your circadian rhythm (controlled by hormones)!",
            "Sensitivity map: Use a toothpick to gently touch different body parts with eyes closed. Where can you feel it most? Least? Map your touch sensitivity.",
            "Taste test: Hold your nose and eat a jellybean. Can you taste the flavor? Now release your nose. Surprise! Smell does 80% of the tasting work.",
            "Growth chart: Measure your height monthly. When do you grow fastest? Compare to sleep and nutrition patterns. See the connection!",
            "Health tracker: For one week, track: sleep hours, water glasses, exercise minutes, fruit/veg servings. How do you feel on good-habit days vs bad?",
        ]
        y = add_wrapped(doc, 72, 690, f"TRY THIS: {experiments[idx]}", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "What I observed:", 'F2', 11, 0.1)
        y -= 20
        for _ in range(3):
            doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
            y -= 20
        doc.new_page()

    certificate(doc, "BODY EXPERT CERTIFICATE")
    add_supplemental(doc, 'Human Body', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book334_Kids_Human_Body.pdf')
    print("Book334_Kids_Human_Body.pdf created successfully!")

if __name__ == "__main__":
    create_book()
