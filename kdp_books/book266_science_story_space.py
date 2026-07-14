"""Book 266: ADVENTURE TO THE STARS - A Science Story About Space (Ages 7-12)"""
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

    def title_page(doc):
        doc.add_filled_rect(0, 0, W, H, 0.1)
        doc.add_centered_text(650, "ADVENTURE TO THE STARS", 'F2', 26, 1)
        doc.add_centered_text(620, "A Science Story About Space", 'F5', 18, 0.9)
        doc.add_centered_text(590, "Ages 7-12", 'F4', 14, 0.8)
        doc.add_centered_text(520, "* * * * * * * * * *", 'F1', 20, 0.8)
        doc.add_centered_text(460, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
        doc.add_centered_text(430, "Science Story Series - Book 1", 'F4', 12, 0.7)
        doc.add_centered_text(200, "Explore the wonders of our universe", 'F4', 13, 0.8)
        doc.add_centered_text(175, "through an incredible adventure!", 'F4', 13, 0.8)
        doc.add_centered_text(100, "Educational Content | Real Science | Amazing Stories", 'F1', 10, 0.7)

    def copyright_page(doc):
        doc.new_page()
        doc.add_centered_text(650, "ADVENTURE TO THE STARS", 'F2', 16)
        doc.add_centered_text(620, "A Science Story About Space", 'F4', 12)
        doc.add_text(margin, 550, "Author: Daniel Tesfamariam", 'F4', 11)
        doc.add_text(margin, 530, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", 'F4', 10)
        doc.add_text(margin, 510, "No part of this publication may be reproduced without permission.", 'F4', 10)
        doc.add_text(margin, 480, "This book is designed to inspire young scientists through storytelling.", 'F4', 10)
        doc.add_text(margin, 460, "Scientific facts have been simplified for young readers.", 'F4', 10)
        doc.add_text(margin, 430, "For ages 7-12", 'F2', 11)
        doc.add_text(margin, 400, "First Edition, 2025", 'F4', 10)

    def toc_page(doc):
        doc.new_page()
        doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18)
        doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
        chapters = [
            "Chapter 1: The Night Sky",
            "Chapter 2: Our Solar System",
            "Chapter 3: The Moon Mission",
            "Chapter 4: Riding a Comet",
            "Chapter 5: The Red Planet",
            "Chapter 6: The Giant Storm",
            "Chapter 7: Saturn's Rings",
            "Chapter 8: Coming Home"
        ]
        y = 670
        for ch in chapters:
            doc.add_text(margin, y, ch, 'F4', 13)
            y -= 30
        doc.add_text(margin, y - 20, "Solar System Quiz", 'F4', 13)
        doc.add_text(margin, y - 50, "Space Vocabulary", 'F4', 13)
        doc.add_text(margin, y - 80, "I Want to Be a Scientist!", 'F4', 13)

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

    # === BUILD BOOK ===
    title_page(doc)
    copyright_page(doc)
    toc_page(doc)

    # Chapter 1: The Night Sky
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: The Night Sky", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story1 = [
        "Maya loved spending summer evenings with her grandfather on the porch.",
        "One clear night, the sky was filled with thousands of twinkling lights.",
        "'Grandpa, what are those lights?' Maya asked, her eyes wide with wonder.",
        "'Those are stars, Maya,' Grandpa smiled. 'Each one is a giant ball of burning gas.'",
        "Maya could hardly believe it. Some of those tiny dots were bigger than our Sun!",
        "'They look small because they are so incredibly far away,' Grandpa explained.",
    ]
    y = text_block(doc, story1, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE OF STARS", 'F2', 13)
    y -= 20
    science1 = [
        "Stars are enormous balls of hot gas, mostly hydrogen and helium.",
        "Deep inside a star, nuclear fusion smashes atoms together, releasing energy.",
        "This energy is what makes stars shine so brightly across the universe.",
        "Light travels at 186,000 miles per second, the fastest speed possible.",
        "A light-year is the distance light travels in one whole year - about 6 trillion miles!",
        "Our nearest star (besides the Sun) is Proxima Centauri, 4.24 light-years away.",
    ]
    y = text_block(doc, science1, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 20, [
        "The Sun is a medium-sized star - some stars are 1,000 times bigger!",
        "You can see about 2,500 stars with your naked eye on a clear night.",
        "Stars appear to twinkle because Earth's atmosphere bends their light."
    ])
    y = try_this(doc, y, "Go outside on a clear night and count the stars you can see. Try finding the Big Dipper!")
    y = think_about_it(doc, y, "If light takes 4 years to reach us from the nearest star, are we seeing it as it is NOW?")

    # Chapter 2: Our Solar System
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: Our Solar System", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story2 = [
        "That night, Maya dreamed she was floating in space. She could see all the planets!",
        "'Welcome to our Solar System!' said a friendly voice. It was the Sun itself!",
        "'I have eight planets orbiting around me,' the Sun beamed proudly.",
        "'Let me introduce you to each one - they are all so different and special!'",
        "Maya zoomed past each planet, amazed by their colors and sizes.",
        "Some were rocky and small; others were giant balls of swirling gas.",
    ]
    y = text_block(doc, story2, 680)
    y -= 20
    doc.add_text(margin, y, "MEET THE PLANETS", 'F2', 13)
    y -= 20
    planets = [
        "Mercury - Closest to Sun, smallest planet, scorching hot days, freezing nights.",
        "Venus - Hottest planet (462C), thick toxic clouds, spins backward!",
        "Earth - Our home! Perfect temperature for liquid water and life.",
        "Mars - The Red Planet, has the tallest volcano (Olympus Mons, 72,000 ft).",
        "Jupiter - Biggest planet, could fit 1,300 Earths inside, has 95 moons!",
        "Saturn - Famous for beautiful rings made of ice and rock particles.",
        "Uranus - Tilted on its side, rolls around the Sun like a ball.",
        "Neptune - Farthest planet, windiest place in solar system (1,200 mph winds).",
    ]
    y = text_block(doc, planets, y, 'F4', 10, 16)
    y = science_fact_box(doc, y - 10, [
        "A trick to remember planet order: My Very Excited Mother Just Served Us Nachos.",
        "Jupiter is so massive its gravity protects Earth from many asteroids.",
        "One day on Venus is longer than one year on Venus (it spins very slowly)."
    ])
    y = try_this(doc, y, "Make a scale model: if Sun is a basketball, Earth would be a tiny bead 78 feet away!")
    y = think_about_it(doc, y, "Why do you think Earth is the only planet with liquid water on its surface?")

    # Chapter 3: The Moon Mission
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: The Moon Mission", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story3 = [
        "In her dream, Maya put on a spacesuit and climbed into a rocket ship.",
        "'Destination: The Moon!' announced the computer. Maya held on tight!",
        "The engines roared and Maya felt herself pressed back into her seat.",
        "After three days of travel, the Moon appeared in her window - huge and gray.",
        "She bounced across the surface in the low gravity, jumping incredibly high!",
        "'I weigh only 15 pounds here!' Maya laughed, doing somersaults in the dust.",
    ]
    y = text_block(doc, story3, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE OF OUR MOON", 'F2', 13)
    y -= 20
    moon_sci = [
        "The Moon's gravity is only 1/6 of Earth's - you could jump 6 times higher!",
        "There is no air on the Moon, so astronauts must wear spacesuits with oxygen.",
        "The Moon has phases because we see different amounts of its sunlit side.",
        "New Moon, Crescent, Quarter, Gibbous, Full Moon - the cycle takes 29.5 days.",
        "The Moon is slowly moving away from Earth - about 1.5 inches per year!",
        "Footprints on the Moon will last millions of years because there is no wind or rain.",
    ]
    y = text_block(doc, moon_sci, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 10, [
        "12 people have walked on the Moon, all between 1969 and 1972.",
        "The Moon causes ocean tides on Earth through its gravitational pull.",
        "A Moon 'day' lasts about 14 Earth days, followed by 14 days of night."
    ])
    y = try_this(doc, y, "Use a flashlight and a ball in a dark room to recreate Moon phases!")
    y = think_about_it(doc, y, "If you weigh 60 lbs on Earth, how much would you weigh on the Moon?")

    # Chapter 4: Riding a Comet
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: Riding a Comet", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story4 = [
        "Suddenly, a brilliant streak of light zoomed past Maya's window!",
        "'A comet!' she gasped. Without thinking, she jumped aboard for a ride.",
        "The comet was like a giant dirty snowball, flying through space at incredible speed.",
        "A glowing tail stretched behind them for millions of miles, shimmering in the sunlight.",
        "'This is amazing!' Maya shouted. 'We are riding a piece of ancient history!'",
        "The comet had been orbiting the Sun for billions of years, older than Earth itself.",
    ]
    y = text_block(doc, story4, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE OF COMETS", 'F2', 13)
    y -= 20
    comet_sci = [
        "Comets are made of ice, dust, and rock - often called 'dirty snowballs.'",
        "They orbit the Sun in long, elliptical (oval-shaped) paths.",
        "When a comet gets close to the Sun, the ice vaporizes creating a glowing tail.",
        "Comet tails always point AWAY from the Sun, pushed by solar wind.",
        "Halley's Comet visits Earth every 75-76 years (next in 2061!).",
        "Some comets take thousands of years to complete one orbit around the Sun.",
    ]
    y = text_block(doc, comet_sci, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 10, [
        "The word 'comet' comes from Greek meaning 'long-haired star.'",
        "A comet's tail can stretch over 100 million miles long!",
        "Scientists think comets may have brought water to early Earth."
    ])
    y = try_this(doc, y, "Make a comet: mix dirt, water, and dry ice (with adult help) to see it 'outgas'!")
    y = think_about_it(doc, y, "Why does a comet's tail always point away from the Sun, not behind it?")

    # Chapter 5: The Red Planet
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: The Red Planet", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story5 = [
        "Maya's comet ride brought her close to a rusty-red world: Mars!",
        "She landed gently on the dusty red surface and looked around in awe.",
        "The sky was a pinkish color, and the landscape was covered in red rocks.",
        "'It looks like a desert!' Maya said. 'But much colder and with barely any air.'",
        "In the distance, she could see an enormous volcano rising above the horizon.",
        "'That must be Olympus Mons - the biggest volcano in the entire solar system!'",
    ]
    y = text_block(doc, story5, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE OF MARS", 'F2', 13)
    y -= 20
    mars_sci = [
        "Mars has a very thin atmosphere - mostly carbon dioxide, not breathable.",
        "The red color comes from iron oxide (rust) in the soil and dust.",
        "Olympus Mons is 72,000 feet tall - nearly 3 times taller than Mt. Everest!",
        "Mars has seasons, polar ice caps, and the longest canyon (Valles Marineris).",
        "A day on Mars is 24 hours 37 minutes - almost the same as Earth!",
        "Scientists have found evidence that liquid water once flowed on Mars's surface.",
    ]
    y = text_block(doc, mars_sci, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 10, [
        "Mars has two tiny moons: Phobos and Deimos (Fear and Panic in Greek).",
        "NASA's rovers (Curiosity, Perseverance) are exploring Mars right now!",
        "A trip to Mars would take about 7-9 months with current technology."
    ])
    y = try_this(doc, y, "Mix red paint with sand to make 'Mars soil.' Compare it to real Earth soil!")
    y = think_about_it(doc, y, "What would humans need to survive living on Mars? Make a list!")

    # Chapter 6: The Giant Storm
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: The Giant Storm", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story6 = [
        "Maya blasted off from Mars and headed toward the biggest planet of all.",
        "Jupiter grew larger and larger in her window until it filled the entire view.",
        "'It is ENORMOUS!' Maya exclaimed. This planet could swallow Earth 1,300 times!",
        "Colorful bands of clouds swirled across its surface in beautiful patterns.",
        "Then she spotted it: a massive red oval bigger than Earth itself.",
        "'The Great Red Spot!' Maya whispered. 'A storm that has raged for over 400 years!'",
    ]
    y = text_block(doc, story6, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE OF JUPITER", 'F2', 13)
    y -= 20
    jupiter_sci = [
        "Jupiter is a gas giant - it has no solid surface to stand on!",
        "The Great Red Spot is a hurricane-like storm raging for at least 400 years.",
        "This storm is so big that TWO Earths could fit inside it!",
        "Jupiter spins incredibly fast - one day is only about 10 hours long.",
        "It has at least 95 known moons, including four giant ones discovered by Galileo.",
        "Jupiter's gravity is so strong it acts like a cosmic vacuum cleaner for asteroids.",
    ]
    y = text_block(doc, jupiter_sci, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 10, [
        "Jupiter's moon Europa may have an ocean under its icy surface - possible life!",
        "Jupiter is made mostly of hydrogen and helium, like a star that never ignited.",
        "The planet has faint rings too, but they are very thin and hard to see."
    ])
    y = try_this(doc, y, "Swirl food coloring in water to see how Jupiter's bands and storms look!")
    y = think_about_it(doc, y, "Why can't you land on Jupiter? What would happen if you tried?")

    # Chapter 7: Saturn's Rings
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: Saturn's Rings", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story7 = [
        "Beyond Jupiter, Maya saw the most beautiful sight of her entire journey.",
        "Saturn floated like a golden jewel, surrounded by spectacular glowing rings!",
        "'They look solid from far away,' Maya noticed as she flew closer.",
        "But up close, she could see billions of individual pieces of ice and rock.",
        "Some chunks were tiny as grains of sand; others were as big as houses!",
        "Maya carefully weaved between the ring particles, feeling like she was in a snowstorm.",
    ]
    y = text_block(doc, story7, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE OF SATURN'S RINGS", 'F2', 13)
    y -= 20
    saturn_sci = [
        "Saturn's rings are made of billions of pieces of ice and rock.",
        "The pieces range from tiny grains to chunks as big as a house.",
        "The rings are incredibly wide (282,000 km) but very thin (only 10-30 meters!).",
        "Saturn is the least dense planet - it would float in a bathtub of water!",
        "Like Jupiter, Saturn is a gas giant with no solid ground.",
        "Saturn has 146 known moons - more than any other planet!",
    ]
    y = text_block(doc, saturn_sci, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 10, [
        "Saturn's moon Titan has lakes and rivers - but they are liquid methane, not water!",
        "You could fit 764 Earths inside Saturn.",
        "Saturn's rings may disappear in about 100 million years as they slowly fall inward."
    ])
    y = try_this(doc, y, "Spin a coin on a table - see how it looks like a ring? That is how Saturn's rings appear!")
    y = think_about_it(doc, y, "If Saturn could float in water, what does that tell you about its density?")

    # Chapter 8: Coming Home
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: Coming Home", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story8 = [
        "As Maya flew past Neptune and the edge of our solar system, she turned back.",
        "From out here, Earth was just a tiny pale blue dot in the vast darkness.",
        "'Our whole world... everything and everyone I love... is on that tiny dot.'",
        "Maya felt a warm hand on her shoulder. 'Time to wake up,' said Grandpa.",
        "She opened her eyes. She was back on the porch, stars still twinkling above.",
        "'Grandpa, I had the most amazing dream! I visited every planet!'",
    ]
    y = text_block(doc, story8, 680)
    y -= 20
    moral = [
        "Grandpa smiled. 'The universe is full of wonders waiting to be discovered.'",
        "'Anyone can explore space - all you need is curiosity and determination.'",
        "'Scientists, astronauts, engineers - they all started as kids who looked up and wondered.'",
        "",
        "MORAL: Dream big - the universe is waiting for curious minds like yours!",
        "",
        "Maya knew that one day she would become a real space scientist.",
        "She would study the stars, visit other planets, and unlock the secrets of the cosmos.",
        "And it all started with one simple question on a summer evening:",
        "'Grandpa, what are those lights?'",
    ]
    y = text_block(doc, moral, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 20, [
        "The Voyager 1 spacecraft is the farthest human-made object - over 15 billion miles away!",
        "There are more stars in the universe than grains of sand on all Earth's beaches.",
        "You are made of stardust - elements in your body were created inside ancient stars!"
    ])

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "SOLAR SYSTEM QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. How many planets are in our solar system?",
        "2. What are stars made of? (Hint: two types of gas)",
        "3. Which planet is closest to the Sun?",
        "4. What is the Great Red Spot on Jupiter?",
        "5. What are Saturn's rings made of?",
        "6. Why does the Moon appear to change shape?",
        "7. What are comets often called? (Hint: dirty ___)",
        "8. Why is Mars red?",
        "9. How long does it take light from the Sun to reach Earth?",
        "10. Which planet could float in water?",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 28

    # Vocabulary Page
    doc.new_page()
    doc.add_centered_text(720, "SPACE VOCABULARY", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    vocab = [
        ("Nuclear Fusion", "When atoms combine, releasing enormous energy (how stars shine)"),
        ("Light-Year", "Distance light travels in one year (about 6 trillion miles)"),
        ("Orbit", "The curved path an object takes around another object in space"),
        ("Gravity", "The force that pulls objects toward each other"),
        ("Atmosphere", "The layer of gases surrounding a planet"),
        ("Comet", "A ball of ice and dust that orbits the Sun"),
        ("Gas Giant", "A large planet made mostly of gas (Jupiter, Saturn, Uranus, Neptune)"),
        ("Solar System", "Our Sun and everything that orbits around it"),
        ("Astronaut", "A person trained to travel and work in space"),
        ("Galaxy", "A huge collection of stars, gas, and dust (we live in the Milky Way)"),
    ]
    y = 680
    for word, defn in vocab:
        doc.add_text(margin, y, word, 'F2', 12)
        y -= 16
        doc.add_text(margin + 20, y, defn, 'F4', 10)
        y -= 24

    # Certificate Page
    doc.new_page()
    doc.add_filled_rect(50, 100, W - 100, H - 200, 0.95)
    doc.add_rect(60, 110, W - 120, H - 220, 2, 0.3)
    doc.add_centered_text(650, "CERTIFICATE OF COMPLETION", 'F2', 22)
    doc.add_centered_text(600, "I Want to Be a Scientist Because:", 'F5', 16)
    doc.add_line(150, 540, W - 150, 540, 0.5, 0.5)
    doc.add_line(150, 490, W - 150, 490, 0.5, 0.5)
    doc.add_line(150, 440, W - 150, 440, 0.5, 0.5)
    doc.add_centered_text(380, "My favorite planet is: _________________________", 'F4', 12)
    doc.add_centered_text(340, "One day I will discover: _________________________", 'F4', 12)
    doc.add_centered_text(270, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(230, "Date: _________________", 'F4', 14)
    doc.add_centered_text(170, "Congratulations, Young Scientist!", 'F2', 16)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book266_Space_Adventure_Story.pdf')
    print("Book266_Space_Adventure_Story.pdf created successfully!")

if __name__ == '__main__':
    create_book()
