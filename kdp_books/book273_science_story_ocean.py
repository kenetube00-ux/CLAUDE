"""Book 273: DEEP BLUE SECRETS - A Science Story About Ocean Life (Ages 7-12)"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc()
    W, H = 612, 792
    margin = 72

    def text_block(doc, lines, start_y, font='F4', size=11, spacing=16, gray=0):
        y = start_y
        for line in lines:
            if y < 60:
                doc.new_page()
                y = H - margin
            doc.add_text(margin, y, line, font, size, gray)
            y -= spacing
        return y

    def science_fact_box(doc, y, facts):
        doc.add_filled_rect(margin - 5, y - 5 - len(facts)*18, W - 2*margin + 10, len(facts)*18 + 35, 0.92)
        doc.add_text(margin + 5, y, "SCIENCE FACT BOX", 'F2', 11)
        y -= 20
        for fact in facts:
            doc.add_text(margin + 10, y, "* " + fact, 'F4', 10)
            y -= 18
        return y

    def try_this(doc, y, activity):
        y -= 15
        doc.add_text(margin, y, "TRY THIS!", 'F2', 11)
        y -= 16
        doc.add_text(margin + 10, y, activity, 'F4', 10)
        return y

    def think_about_it(doc, y, question):
        y -= 20
        doc.add_text(margin, y, "THINK ABOUT IT:", 'F2', 11)
        y -= 16
        doc.add_text(margin + 10, y, question, 'F4', 10, 0.2)
        return y

    # Title Page
    doc.add_filled_rect(0, 0, W, H, 0.15)
    doc.add_centered_text(660, "DEEP BLUE SECRETS", 'F2', 28, 1)
    doc.add_centered_text(620, "A Science Story About Ocean Life", 'F5', 16, 0.9)
    doc.add_centered_text(590, "Ages 7-12", 'F4', 14, 0.8)
    doc.add_centered_text(490, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
    doc.add_centered_text(460, "Science Story Series - Book 8", 'F4', 12, 0.7)
    doc.add_centered_text(350, "Dive deep into the ocean and discover", 'F4', 13, 0.8)
    doc.add_centered_text(325, "incredible creatures in every zone!", 'F4', 13, 0.8)
    doc.add_centered_text(100, "Educational Content | Real Science | Amazing Stories", 'F1', 10, 0.7)

    # Copyright
    doc.new_page()
    doc.add_centered_text(650, "DEEP BLUE SECRETS", 'F2', 16)
    doc.add_text(margin, 600, "Author: Daniel Tesfamariam", 'F4', 11)
    doc.add_text(margin, 580, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", 'F4', 10)
    doc.add_text(margin, 560, "No part of this publication may be reproduced without permission.", 'F4', 10)
    doc.add_text(margin, 530, "For ages 7-12. Marine science facts simplified for young readers.", 'F4', 10)
    doc.add_text(margin, 500, "First Edition, 2025", 'F4', 10)

    # TOC
    doc.new_page()
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    chapters = [
        "Chapter 1: Setting Sail",
        "Chapter 2: The Coral City",
        "Chapter 3: School of Fish",
        "Chapter 4: The Twilight Zone",
        "Chapter 5: Giant Squid!",
        "Chapter 6: The Midnight Zone",
        "Chapter 7: The Ocean Floor",
        "Chapter 8: Protecting Our Oceans",
    ]
    y = 670
    for ch in chapters:
        doc.add_text(margin, y, ch, 'F4', 13)
        y -= 30

    # Chapter 1: Setting Sail
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: Setting Sail", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Captain Marina and her crew of young scientists boarded the research submarine.",
        "'Today we dive to the deepest parts of the ocean!' she announced excitedly.",
        "The submarine slipped beneath the waves into the warm, sunlit surface waters.",
        "Sunlight sparkled through the blue water as schools of colorful fish swam past.",
        "'This is the Sunlight Zone,' Marina explained. 'The top 200 meters of ocean.'",
        "'Most ocean life lives here because sunlight means plants can grow!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: OCEAN ZONES", 'F2', 13)
    y -= 20
    science = [
        "The ocean is divided into zones based on how deep sunlight can reach:",
        "  Sunlight Zone (0-200m): Bright, warm, most life lives here.",
        "  Twilight Zone (200-1000m): Dim light, cooler, strange creatures.",
        "  Midnight Zone (1000-4000m): Total darkness, near-freezing, high pressure.",
        "  Abyssal Zone (4000-6000m): Pitch black, extreme pressure, very few animals.",
        "  Hadal Zone (6000m+): The deepest trenches, barely explored by humans.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "We have explored less than 20% of the ocean floor - more of the Moon is mapped!",
        "The ocean holds 97% of all water on Earth and covers 71% of the surface.",
        "Average ocean depth is about 12,100 feet (3,688 meters) - over 2 miles deep!"
    ])
    y = try_this(doc, y, "Fill a tall clear glass with water. Shine a flashlight from above - notice how light fades with depth!")
    y = think_about_it(doc, y, "Why do you think most ocean life lives in the top 200 meters?")

    # Chapter 2: The Coral City
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: The Coral City", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The submarine glided over a breathtaking sight: a massive coral reef!",
        "It looked like an underwater city, bursting with color and life.",
        "'A coral reef is the most biodiverse ecosystem in the ocean!' Marina said.",
        "Fish of every color darted between the coral structures. Crabs scuttled along the bottom.",
        "Sea turtles glided gracefully overhead. Eels peeked out from hiding spots.",
        "'It is like a rainforest under the sea!' one of the young scientists exclaimed.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: CORAL REEFS", 'F2', 13)
    y -= 20
    science = [
        "Coral looks like rock or a plant, but it is actually made of tiny ANIMALS!",
        "Each coral is made of thousands of tiny polyps that build limestone skeletons.",
        "Coral has a symbiotic relationship with algae (zooxanthellae) that live inside it.",
        "The algae give coral food through photosynthesis; coral gives algae shelter!",
        "Coral reefs support 25% of all marine species despite covering less than 1% of the ocean floor.",
        "The Great Barrier Reef (Australia) is so big you can see it from space!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Coral reefs take thousands of years to grow - they are incredibly fragile.",
        "When water gets too warm, coral 'bleaches' (turns white) and can die.",
        "Some coral species can live for over 4,000 years!"
    ])
    y = try_this(doc, y, "Look up pictures of coral bleaching. Compare healthy (colorful) vs bleached (white) coral.")
    y = think_about_it(doc, y, "Why is it important to protect coral reefs even if you live far from the ocean?")

    # Chapter 3: School of Fish
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: School of Fish", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "A massive school of silver fish surrounded the submarine - thousands of them!",
        "They moved together as one giant shape, turning and twisting in perfect unison.",
        "'How do they all move together without bumping into each other?' a student asked.",
        "'Each fish watches its neighbors and matches their speed and direction,' Marina explained.",
        "'Being in a school protects them - predators get confused by so many moving targets!'",
        "A barracuda charged in, but the school split apart and reformed perfectly!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: FISH BIOLOGY", 'F2', 13)
    y -= 20
    science = [
        "Fish breathe underwater using gills that extract dissolved oxygen from water.",
        "Water flows in through the mouth and over the gills, where oxygen is absorbed.",
        "Fish have a lateral line - a sensory organ that detects vibrations and movement nearby.",
        "This lateral line helps fish swim in schools without crashing into each other!",
        "Fish are cold-blooded - their body temperature matches the surrounding water.",
        "There are over 35,000 known species of fish - more than all other vertebrates combined!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The fastest fish (sailfish) can swim at 68 mph - faster than a car on the highway!",
        "Some fish (like clownfish) change sex during their lifetime!",
        "The ocean sunfish (Mola mola) can weigh up to 5,000 pounds!"
    ])
    y = try_this(doc, y, "Watch a video of a fish school moving. Notice how they turn together like one organism!")
    y = think_about_it(doc, y, "Why do fish swim in schools? What advantages does it give them?")

    # Chapter 4: The Twilight Zone
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: The Twilight Zone", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The submarine descended past 200 meters. The water grew darker and colder.",
        "'Welcome to the Twilight Zone,' Marina announced. 'Very little light reaches here.'",
        "Strange creatures appeared in the dim blue darkness around them.",
        "A jellyfish drifted by, its body pulsing with an eerie blue-green glow!",
        "'Bioluminescence!' Marina exclaimed. 'It is making its own light!'",
        "More glowing creatures appeared: fish with built-in flashlights under their eyes!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: BIOLUMINESCENCE", 'F2', 13)
    y -= 20
    science = [
        "Bioluminescence is the ability of living things to produce their own light!",
        "A chemical reaction between luciferin and oxygen creates light without heat.",
        "About 76% of ocean creatures in the deep sea can produce bioluminescence!",
        "Uses: attracting prey, confusing predators, finding mates, communication.",
        "Anglerfish have a glowing lure on their head to attract prey in total darkness.",
        "On land, fireflies use bioluminescence too - same basic chemistry!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Some squid squirt glowing 'ink' to confuse predators while they escape!",
        "Bioluminescent bacteria can make dead fish glow in the dark.",
        "The cookiecutter shark glows to camouflage against dim light from above."
    ])
    y = try_this(doc, y, "Break a glow stick in the dark. The chemical reaction inside is similar to bioluminescence!")
    y = think_about_it(doc, y, "Why would making your own light be useful in total darkness?")

    # Chapter 5: Giant Squid!
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: Giant Squid!", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "At 600 meters deep, something enormous appeared at the edge of the submarine lights.",
        "Two huge eyes - the size of dinner plates - stared back at them from the darkness!",
        "'A GIANT SQUID!' Marina gasped. 'We are so lucky - they are rarely seen alive!'",
        "Its tentacles stretched over 40 feet long, lined with powerful suction cups.",
        "The massive creature glided past gracefully, then vanished into the black depths.",
        "'For centuries, sailors thought these were mythical sea monsters!' Marina said.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: DEEP SEA ADAPTATIONS", 'F2', 13)
    y -= 20
    science = [
        "Giant squid can grow up to 43 feet long and have the largest eyes in the animal kingdom!",
        "Their eyes (10 inches across!) help them see in near-total darkness.",
        "Deep-sea animals face extreme pressure: at 1000m, pressure is 100 times surface pressure!",
        "Many deep creatures have flexible bodies (no gas-filled spaces) to withstand pressure.",
        "Some fish have no swim bladder and have super-soft bones to survive the crushing depths.",
        "Food is scarce in the deep, so many animals have very slow metabolisms.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Sperm whales dive 3,000+ feet to hunt giant squid - epic battles leave scars on both!",
        "The colossal squid (even bigger!) has rotating hooks on its tentacles.",
        "Giant squid were not photographed alive until 2004 - truly mysterious creatures."
    ])
    y = try_this(doc, y, "Fill a plastic bottle and squeeze it - feel the pressure? Imagine that x100 at the deep ocean!")
    y = think_about_it(doc, y, "Why do giant squid have such enormous eyes? What advantage does that give them?")

    # Chapter 6: The Midnight Zone
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: The Midnight Zone", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Below 1,000 meters, there was absolutely zero sunlight. Total, complete darkness.",
        "The temperature dropped to near freezing. The pressure was immense.",
        "'Nothing can survive here... can it?' a student asked nervously.",
        "Then the submarine's lights revealed an incredible sight: a hydrothermal vent!",
        "Superheated water (750F!) shot up from cracks in the ocean floor like underwater geysers.",
        "And around it - life! Tube worms, crabs, shrimp - a whole community in total darkness!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: DEEP SEA VENTS", 'F2', 13)
    y -= 20
    science = [
        "Hydrothermal vents are cracks where superheated water erupts from beneath the ocean floor.",
        "Water heated by magma dissolves minerals, creating 'black smokers' (mineral chimneys).",
        "Extremophiles are organisms that thrive in these extreme conditions!",
        "These creatures get energy from chemicals (chemosynthesis) instead of sunlight!",
        "This discovery changed biology - life does not always need sunlight!",
        "Scientists think life on Earth may have started at hydrothermal vents billions of years ago.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Giant tube worms near vents can grow 6 feet long - they have no mouth or stomach!",
        "Vent water can reach 750F but extreme pressure keeps it from boiling.",
        "These vents support entire ecosystems with no sunlight at all - amazing!"
    ])
    y = try_this(doc, y, "Research 'extremophiles' - organisms that live in extreme conditions (hot springs, ice, acid)!")
    y = think_about_it(doc, y, "If life can exist without sunlight on Earth, could it exist in the dark oceans of other moons?")

    # Chapter 7: The Ocean Floor
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: The Ocean Floor", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The submarine continued down to the abyssal plain - the vast, flat ocean floor.",
        "'We are over 4,000 meters deep now,' Marina reported. 'The pressure is enormous!'",
        "Then the seafloor dropped away into an impossibly deep trench!",
        "'The Mariana Trench!' Marina announced. 'The deepest point on Earth!'",
        "'Nearly 11,000 meters (36,000 feet) deep - Mount Everest could fit inside with room to spare!'",
        "Even here, at the very bottom, they found signs of life. Life finds a way!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: THE OCEAN FLOOR", 'F2', 13)
    y -= 20
    science = [
        "The abyssal plain covers over 50% of Earth's surface - mostly flat, muddy, and dark.",
        "The Mariana Trench is the deepest point: 36,089 feet (10,994m) at Challenger Deep.",
        "Pressure at the bottom is 1,086 times surface pressure - 8 tons per square inch!",
        "Only 3 people have ever visited the bottom: Piccard & Walsh (1960), Cameron (2012).",
        "Mid-ocean ridges are underwater mountain chains where new ocean floor is made.",
        "The ocean floor is always moving due to plate tectonics - spreading and subducting.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "If you put Mt. Everest (29,032 ft) in the Mariana Trench, it would still be under a mile of water!",
        "Plastic bags have been found at the bottom of the Mariana Trench. Pollution reaches everywhere.",
        "The deepest fish ever found lives at 27,000 feet - a snailfish."
    ])
    y = try_this(doc, y, "Stack books to 29 inches (Everest scale). Now measure 36 inches (Mariana Trench). See the difference!")
    y = think_about_it(doc, y, "How could finding plastic at the deepest point on Earth change how we think about pollution?")

    # Chapter 8: Protecting Our Oceans
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: Protecting Our Oceans", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "As the submarine rose back to the surface, the crew was quiet and thoughtful.",
        "'The ocean is so incredible,' Marina said, 'and it is in danger from human activity.'",
        "They passed floating plastic bags, tangled fishing nets, and murky polluted water.",
        "'8 million tons of plastic enter the ocean every year,' Marina said sadly.",
        "'But we can change this! Every person who cares can make a difference!'",
        "'The ocean gives us oxygen, food, and beauty. We must protect it!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: OCEAN CONSERVATION", 'F2', 13)
    y -= 20
    science = [
        "Plastic pollution: 8 million tons of plastic enter the ocean yearly. Takes 500+ years to decompose.",
        "Ocean acidification: CO2 dissolves in seawater, making it more acidic (harms shells/coral).",
        "Overfishing: taking too many fish faster than they can reproduce.",
        "What YOU can do: reduce single-use plastic, recycle, do beach cleanups!",
        "Eat sustainable seafood, support marine protected areas, and spread awareness!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y -= 15
    doc.add_text(margin, y, "MORAL:", 'F2', 14)
    y -= 18
    doc.add_text(margin, y, "We must protect what we don't fully understand yet!", 'F5', 13)
    y = science_fact_box(doc, y - 30, [
        "The ocean produces over 50% of the world's oxygen (thank you, phytoplankton!).",
        "By 2050, there could be more plastic in the ocean than fish (by weight) if we do not act.",
        "Marine protected areas can help fish populations recover by 400% in just a few years!"
    ])

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "OCEAN QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. Name the five ocean zones from shallowest to deepest.",
        "2. What are coral reefs made of? (Animal, plant, or rock?)",
        "3. What is bioluminescence?",
        "4. What is the deepest point in the ocean?",
        "5. How do fish breathe underwater?",
        "6. What is a hydrothermal vent?",
        "7. How big can a giant squid grow?",
        "8. What is the biggest threat to ocean health?",
        "9. How much of the ocean floor has been explored?",
        "10. Name two things you can do to help protect the ocean.",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 26

    # Activity: Ocean Zone Diagram
    doc.new_page()
    doc.add_centered_text(720, "DRAW THE OCEAN ZONES", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    doc.add_text(margin, 680, "Draw and label each ocean zone with depth and animals that live there:", 'F4', 11)
    zones = [
        "Sunlight Zone (0-200m): coral, fish, dolphins, sea turtles",
        "Twilight Zone (200-1000m): jellyfish, swordfish, bioluminescent creatures",
        "Midnight Zone (1000-4000m): giant squid, anglerfish, no sunlight",
        "Abyssal Zone (4000-6000m): sea cucumbers, tube worms near vents",
        "Hadal Zone (6000m+): snailfish, amphipods, extreme pressure",
    ]
    y = 650
    for z in zones:
        doc.add_text(margin, y, z, 'F4', 10)
        y -= 20
    doc.add_rect(margin, 130, W - 2*margin, 380, 1, 0.5)
    doc.add_centered_text(115, "Draw your ocean zone diagram here!", 'F4', 11, 0.4)

    # Certificate
    doc.new_page()
    doc.add_filled_rect(50, 100, W - 100, H - 200, 0.95)
    doc.add_rect(60, 110, W - 120, H - 220, 2, 0.3)
    doc.add_centered_text(650, "OCEAN EXPLORER CERTIFICATE", 'F2', 20)
    doc.add_centered_text(600, "I dove deep and discovered ocean secrets!", 'F5', 14)
    doc.add_centered_text(550, "The coolest ocean creature I learned about:", 'F4', 12)
    doc.add_line(150, 520, W - 150, 520, 0.5, 0.5)
    doc.add_centered_text(480, "One thing I will do to protect the ocean:", 'F4', 12)
    doc.add_line(150, 450, W - 150, 450, 0.5, 0.5)
    doc.add_centered_text(390, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(350, "Date: _________________", 'F4', 14)
    doc.add_centered_text(280, "Certified Ocean Scientist!", 'F2', 18)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book273_Ocean_Deep_Story.pdf')
    print("Book273_Ocean_Deep_Story.pdf created successfully!")

if __name__ == '__main__':
    create_book()
