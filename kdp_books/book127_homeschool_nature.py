from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "NATURE STUDY JOURNAL"
subtitle = "A Charlotte Mason Inspired Outdoor Learning Guide"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 20)
pdf.add_centered_text(515, subtitle, 'F4', 13)
pdf.add_centered_text(440, "Observe. Sketch. Wonder. Learn.", 'F4', 12)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 12)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: How to Do Nature Study
pdf.new_page()
pdf.add_centered_text(750, "HOW TO DO NATURE STUDY", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
intro = [
    "Charlotte Mason believed that children learn best through direct",
    "contact with the natural world. Nature study is not about textbooks -",
    "it is about stepping outside and truly SEEING what is around you.",
    "",
    "THE PRACTICE IS SIMPLE:",
    "1. Go outside regularly (aim for weekly, same location if possible)",
    "2. SIT QUIETLY for the first 5 minutes - just observe",
    "3. Choose ONE thing to study closely (a leaf, insect, cloud, rock)",
    "4. SKETCH what you see (skill does not matter - observation does)",
    "5. RECORD details: color, size, texture, behavior, habitat",
    "6. RESEARCH what you found when you return home",
    "7. Keep this journal as your growing record of discovery",
    "",
    "TIPS FOR SUCCESS:",
    "- Bring a magnifying glass to notice small details",
    "- Go at different times of day (dawn, midday, dusk)",
    "- Visit the same spot across seasons to notice changes",
    "- Let your child lead - follow THEIR curiosity",
    "- There are no wrong observations",
    "- Silence is part of the practice (resist filling every moment with talk)",
    "- Bring field guides if you want to identify species",
    "- A camera can supplement sketching but should not replace it",
    "",
    "WHAT YOU NEED:",
    "- This journal and a pencil (colored pencils optional)",
    "- Magnifying glass",
    "- Comfortable outdoor clothing",
    "- A willing heart to slow down and notice"
]
for line in intro:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Pages 4-7: Seasonal Observation Pages
seasons = [
    ("SPRING", [
        "Birds returning from migration (listen for new songs)",
        "First flowers blooming (crocuses, daffodils, dandelions)",
        "Tree buds opening - notice the stages",
        "Insects emerging (bees, butterflies, ants becoming active)",
        "Rain patterns and puddle ecosystems",
        "Nesting behavior - birds gathering materials",
        "Longer days - track sunrise/sunset times",
        "Seed sprouting - plant something and observe daily",
        "Frog/toad activity near water",
        "Weeds - identify 5 common spring weeds in your area"
    ]),
    ("SUMMER", [
        "Full canopy - compare leaf shapes from different trees",
        "Garden visitors - identify insects on plants",
        "Cloud formations (cumulus, stratus, cirrus)",
        "Night sky - visible constellations, moon phases",
        "Water life - pond study, stream inhabitants",
        "Heat effects - observe how plants and animals adapt",
        "Fruit and berry development on plants",
        "Spider webs - early morning with dew is best",
        "Lightning bugs / fireflies at dusk",
        "Rock and mineral study - visit a creek bed"
    ]),
    ("FALL", [
        "Leaf color changes - collect and press specimens",
        "Migration patterns - flocks of birds heading south",
        "Seed dispersal methods (wind, animal, water)",
        "Mushrooms and fungi appearing",
        "Squirrel behavior (gathering, burying)",
        "Shorter days - track the changing light",
        "First frost - observe what happens to plants",
        "Harvest observations - visit farm or garden",
        "Deciduous vs evergreen - compare preparations",
        "Animal tracks in mud after rain"
    ]),
    ("WINTER", [
        "Bare tree silhouettes - compare branch patterns",
        "Bird identification (easier without leaves blocking view!)",
        "Animal tracks in snow",
        "Evergreen study - types of needles and cones",
        "Ice formations - icicles, frozen puddles, frost patterns",
        "Winter sky - stars are brighter in cold air",
        "Dormant plants - what is happening underground?",
        "Bird feeder observations (species, behavior, hierarchy)",
        "Weather patterns - wind direction, cloud types",
        "Signs of life persisting through cold"
    ])
]

for season_name, observations in seasons:
    pdf.new_page()
    pdf.add_centered_text(750, f"{season_name} OBSERVATIONS", 'F2', 16)
    pdf.add_line(50, 740, 562, 740)
    y = 715
    pdf.add_text(50, y, f"What to look for during {season_name.lower()}:", 'F2', 11)
    y -= 20
    for obs in observations:
        pdf.add_text(55, y, f"- {obs}", 'F4', 10)
        y -= 15
    y -= 20
    pdf.add_text(50, y, f"MY {season_name} GOALS:", 'F2', 11)
    y -= 18
    for i in range(5):
        pdf.add_rect(55, y - 2, 10, 10, 0.5)
        pdf.add_text(70, y, "_______________________________________________", 'F1', 9)
        y -= 18
    y -= 15
    pdf.add_text(50, y, f"Favorite {season_name.lower()} discovery this year:", 'F2', 10)
    y -= 16
    pdf.add_line(50, y, 562, y, 0.3, 0.5)
    y -= 14
    pdf.add_line(50, y, 562, y, 0.3, 0.5)

# Pages 8-31: 24 Nature Study Entry Pages
for entry in range(1, 25):
    pdf.new_page()
    pdf.add_centered_text(755, f"NATURE STUDY ENTRY #{entry}", 'F2', 13)
    pdf.add_line(50, 745, 562, 745)
    y = 725
    pdf.add_text(50, y, "Date: ___/___/___   Time: _______   Season: ___________", 'F1', 9)
    y -= 16
    pdf.add_text(50, y, "Location: _______________________________________________________", 'F1', 9)
    y -= 16
    pdf.add_text(50, y, "Weather: Temp ___ F/C  Sky: Clear/Cloudy/Overcast/Rain/Snow  Wind: None/Light/Moderate/Strong", 'F1', 8)
    y -= 20
    pdf.add_text(50, y, "WHAT I OBSERVED:", 'F2', 10)
    y -= 14
    for _ in range(5):
        pdf.add_line(50, y, 562, y, 0.3, 0.5)
        y -= 14
    y -= 10
    # Sketch box
    pdf.add_text(50, y, "DETAILED SKETCH:", 'F2', 10)
    y -= 5
    sketch_height = 220
    pdf.add_rect(50, y - sketch_height, 512, sketch_height, 0.5, 0.5)
    y -= sketch_height + 10
    pdf.add_text(50, y, "Common Name: ________________________  Scientific Name: ________________________", 'F1', 9)
    y -= 16
    pdf.add_text(50, y, "Habitat/Where Found: ___________________________________________________", 'F1', 9)
    y -= 16
    pdf.add_text(50, y, "Colors: ____________________  Size: ____________________  Texture: ____________________", 'F1', 9)
    y -= 16
    pdf.add_text(50, y, "Questions to Research:", 'F2', 9)
    y -= 14
    pdf.add_line(50, y, 562, y, 0.3, 0.5)
    y -= 14
    pdf.add_line(50, y, 562, y, 0.3, 0.5)

# Page 32: Bird Identification Log (page 1)
pdf.new_page()
pdf.add_centered_text(750, "BIRD IDENTIFICATION LOG - PAGE 1", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 720
pdf.add_filled_rect(50, y - 3, 512, 14, 0.85)
pdf.add_text(55, y, "Date", 'F2', 8)
pdf.add_text(100, y, "Bird Name", 'F2', 8)
pdf.add_text(220, y, "Colors/Markings", 'F2', 8)
pdf.add_text(350, y, "Behavior", 'F2', 8)
pdf.add_text(450, y, "Location", 'F2', 8)
y -= 16
for _ in range(30):
    pdf.add_text(55, y, "___/___", 'F3', 7)
    pdf.add_line(100, y - 1, 215, y - 1, 0.2, 0.6)
    pdf.add_line(220, y - 1, 345, y - 1, 0.2, 0.6)
    pdf.add_line(350, y - 1, 445, y - 1, 0.2, 0.6)
    pdf.add_line(450, y - 1, 560, y - 1, 0.2, 0.6)
    y -= 14

# Page 33: Bird Identification Log (page 2)
pdf.new_page()
pdf.add_centered_text(750, "BIRD IDENTIFICATION LOG - PAGE 2", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 720
pdf.add_filled_rect(50, y - 3, 512, 14, 0.85)
pdf.add_text(55, y, "Date", 'F2', 8)
pdf.add_text(100, y, "Bird Name", 'F2', 8)
pdf.add_text(220, y, "Colors/Markings", 'F2', 8)
pdf.add_text(350, y, "Behavior", 'F2', 8)
pdf.add_text(450, y, "Location", 'F2', 8)
y -= 16
for _ in range(30):
    pdf.add_text(55, y, "___/___", 'F3', 7)
    pdf.add_line(100, y - 1, 215, y - 1, 0.2, 0.6)
    pdf.add_line(220, y - 1, 345, y - 1, 0.2, 0.6)
    pdf.add_line(350, y - 1, 445, y - 1, 0.2, 0.6)
    pdf.add_line(450, y - 1, 560, y - 1, 0.2, 0.6)
    y -= 14

# Page 34: Plant Press Record
pdf.new_page()
pdf.add_centered_text(750, "PLANT PRESS RECORD", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Record details of plants you press and preserve:", 'F4', 10)
y -= 20
for p in range(10):
    pdf.add_filled_rect(50, y - 3, 512, 50, 0.95)
    pdf.add_rect(50, y - 3, 512, 50, 0.5, 0.5)
    pdf.add_text(55, y + 33, f"Specimen {p+1}:", 'F2', 9)
    pdf.add_text(130, y + 33, "Name: ____________________", 'F1', 8)
    pdf.add_text(310, y + 33, "Date collected: ___/___/___", 'F1', 8)
    pdf.add_text(55, y + 18, "Location: ___________________________", 'F1', 8)
    pdf.add_text(300, y + 18, "Habitat: _____________________", 'F1', 8)
    pdf.add_text(55, y + 3, "Description: ____________________________________________________________", 'F1', 8)
    y -= 60

# Page 35: Seasonal Tree Observation
pdf.new_page()
pdf.add_centered_text(750, "SEASONAL TREE OBSERVATION", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Choose ONE tree near your home. Observe and sketch it each season.", 'F4', 10)
y -= 16
pdf.add_text(50, y, "My tree: Species ___________________  Location: ___________________", 'F1', 9)
y -= 25
tree_seasons = ["SPRING", "SUMMER", "FALL", "WINTER"]
for ts in tree_seasons:
    pdf.add_text(50, y, f"{ts}   Date: ___/___/___", 'F2', 10)
    y -= 5
    pdf.add_rect(50, y - 110, 250, 110, 0.5, 0.5)
    pdf.add_text(310, y - 15, "Leaves: ___________________", 'F1', 8)
    pdf.add_text(310, y - 30, "Color: ____________________", 'F1', 8)
    pdf.add_text(310, y - 45, "Bark: _____________________", 'F1', 8)
    pdf.add_text(310, y - 60, "Visitors: _________________", 'F1', 8)
    pdf.add_text(310, y - 75, "Changes from last season:", 'F1', 8)
    pdf.add_line(310, y - 87, 560, y - 87, 0.3, 0.5)
    y -= 125

# Page 36: Nature Collection Inventory
pdf.new_page()
pdf.add_centered_text(750, "NATURE COLLECTION INVENTORY", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 720
pdf.add_text(50, y, "Record items in your nature collection:", 'F4', 10)
y -= 18
pdf.add_filled_rect(50, y - 3, 512, 14, 0.85)
pdf.add_text(55, y, "#", 'F2', 8)
pdf.add_text(70, y, "Item", 'F2', 8)
pdf.add_text(200, y, "Type", 'F2', 8)
pdf.add_text(290, y, "Found Where", 'F2', 8)
pdf.add_text(420, y, "Date", 'F2', 8)
pdf.add_text(475, y, "Notes", 'F2', 8)
y -= 14
for i in range(35):
    pdf.add_text(55, y, f"{i+1}", 'F3', 7)
    pdf.add_line(70, y - 1, 195, y - 1, 0.2, 0.6)
    pdf.add_line(200, y - 1, 285, y - 1, 0.2, 0.6)
    pdf.add_line(290, y - 1, 415, y - 1, 0.2, 0.6)
    pdf.add_text(420, y, "___/___", 'F3', 7)
    pdf.add_line(475, y - 1, 560, y - 1, 0.2, 0.6)
    y -= 14

# Page 37: Monthly Nature Challenge Cards
pdf.new_page()
pdf.add_centered_text(750, "MONTHLY NATURE CHALLENGE CARDS", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Complete one challenge each month. Check off when done!", 'F4', 10)
y -= 20
challenges = [
    ("January", "Find 5 different types of animal tracks"),
    ("February", "Observe the same bird for 10 minutes straight"),
    ("March", "Find signs of spring awakening (3 examples)"),
    ("April", "Press and identify 5 different wildflowers"),
    ("May", "Find a bird nest (observe from distance, never touch)"),
    ("June", "Catch and release 3 insects - sketch each one"),
    ("July", "Map all the trees in your yard or block"),
    ("August", "Stargaze - identify 3 constellations"),
    ("September", "Collect 10 different leaf types, identify each"),
    ("October", "Find 3 different types of fungus/mushrooms"),
    ("November", "Sit silently outdoors for 15 minutes, record all sounds"),
    ("December", "Identify 5 birds at a feeder or in your neighborhood")
]
for month, challenge in challenges:
    pdf.add_rect(55, y - 2, 10, 10, 0.5)
    pdf.add_text(70, y, f"{month}:", 'F2', 9)
    pdf.add_text(130, y, challenge, 'F4', 9)
    y -= 14
    pdf.add_text(130, y, "Date completed: ___/___/___   Notes: ____________________________", 'F1', 8)
    y -= 20

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book127_Nature_Study_Journal.pdf')
print("Book127_Nature_Study_Journal.pdf created successfully!")
