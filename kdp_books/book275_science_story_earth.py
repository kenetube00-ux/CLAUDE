"""Book 275: OUR AMAZING PLANET - A Science Story About Earth (Ages 6-11)"""
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
    doc.add_filled_rect(0, 0, W, H, 0.12)
    doc.add_centered_text(660, "OUR AMAZING PLANET", 'F2', 28, 1)
    doc.add_centered_text(620, "A Science Story About Earth", 'F5', 16, 0.9)
    doc.add_centered_text(590, "Ages 6-11", 'F4', 14, 0.8)
    doc.add_centered_text(490, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
    doc.add_centered_text(460, "Science Story Series - Book 10", 'F4', 12, 0.7)
    doc.add_centered_text(350, "Earth tells its own amazing story", 'F4', 13, 0.8)
    doc.add_centered_text(325, "- 4.5 billion years in the making!", 'F4', 13, 0.8)
    doc.add_centered_text(100, "Educational Content | Real Science | Amazing Stories", 'F1', 10, 0.7)

    # Copyright
    doc.new_page()
    doc.add_centered_text(650, "OUR AMAZING PLANET", 'F2', 16)
    doc.add_text(margin, 600, "Author: Daniel Tesfamariam", 'F4', 11)
    doc.add_text(margin, 580, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", 'F4', 10)
    doc.add_text(margin, 560, "No part of this publication may be reproduced without permission.", 'F4', 10)
    doc.add_text(margin, 530, "For ages 6-11. Earth science concepts simplified for young readers.", 'F4', 10)
    doc.add_text(margin, 500, "First Edition, 2025", 'F4', 10)

    # TOC
    doc.new_page()
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    chapters = [
        "Chapter 1: I Was Born (Earth's Formation)",
        "Chapter 2: My Layers (Earth's Interior)",
        "Chapter 3: My Moving Skin (Plate Tectonics)",
        "Chapter 4: My Fiery Breath (Volcanoes)",
        "Chapter 5: My Blue Blanket (The Atmosphere)",
        "Chapter 6: My Rock Collection (Rock Cycle)",
        "Chapter 7: My Living Coat (Biomes)",
        "Chapter 8: Please Take Care of Me",
    ]
    y = 670
    for ch in chapters:
        doc.add_text(margin, y, ch, 'F4', 13)
        y -= 30

    # Chapter 1: I Was Born
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: I Was Born", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Hello! I am Earth, your planet. Let me tell you my life story!",
        "I was born about 4.5 billion years ago from a swirling cloud of gas and dust.",
        "The Sun formed first, and leftover material clumped together to make the planets.",
        "At first, I was a ball of melting rock, constantly bombarded by asteroids!",
        "Slowly, I cooled down. Heavy metals sank to my center. Lighter rock floated up.",
        "Over millions of years, I formed my layers - like a giant rocky onion!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: HOW EARTH FORMED", 'F2', 13)
    y -= 20
    science = [
        "Our solar system formed from a giant cloud of gas and dust (solar nebula) 4.6 billion years ago.",
        "Gravity pulled material together. The center became the Sun; leftovers became planets.",
        "Earth formed from billions of rocky and metallic pieces smashing and sticking together.",
        "Early Earth was so hot that the entire surface was molten (liquid) rock!",
        "As it cooled, heavier elements (iron, nickel) sank to the center forming the core.",
        "Lighter rocks floated up to form the crust. Water appeared from volcanic gases and comets.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Earth is 4.54 billion years old - if Earth's history were a 24-hour clock, humans appear at 11:59 PM!",
        "The Moon formed when a Mars-sized object crashed into young Earth, ejecting debris.",
        "Early Earth had no oxygen in its atmosphere - you could not have breathed the air!"
    ])
    y = try_this(doc, y, "Mix oil and water in a jar, shake, then watch them separate. Heavy stuff sinks - like Earth forming layers!")
    y = think_about_it(doc, y, "If Earth is 4.5 billion years old, how old is that compared to a human lifetime?")

    # Chapter 2: My Layers
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: My Layers", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "I am not the same all the way through! I have layers, like an egg or an onion.",
        "My outside layer (the crust) is thin and rocky - you live on it!",
        "Beneath that is my mantle - thick, hot, and slowly flowing like thick honey.",
        "Deep inside is my outer core - liquid metal, so hot it glows!",
        "At my very center is my inner core - solid iron and nickel, hotter than the Sun's surface!",
        "Each of my layers is important and makes me the special planet I am.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: EARTH'S LAYERS", 'F2', 13)
    y -= 20
    science = [
        "Crust: 5-70 km thick. Thin and solid. Ocean crust is thinner than continental crust.",
        "Mantle: 2,900 km thick. Hot rock that flows very slowly (like toothpaste).",
        "Outer Core: 2,200 km thick. Liquid iron and nickel. Creates Earth's magnetic field!",
        "Inner Core: 1,200 km radius. Solid iron ball. Temperature: 9,800F (hotter than Sun's surface!).",
        "The deeper you go, the hotter it gets - about 25C per km in the crust!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "If Earth were an apple, the crust would be thinner than the apple's skin!",
        "The deepest hole ever drilled (Kola Superdeep) went only 7.6 miles - barely scratching the crust!",
        "Earth's liquid outer core generates the magnetic field that protects us from solar radiation."
    ])
    y = try_this(doc, y, "Cut a hard-boiled egg in half: shell=crust, white=mantle, yolk=core. Earth is like a giant egg!")
    y = think_about_it(doc, y, "How do scientists know what is inside Earth if we cannot dig that deep?")

    # Chapter 3: My Moving Skin
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: My Moving Skin", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Here is a secret: my skin (crust) is not one solid piece. It is broken into plates!",
        "These huge plates float on my mantle and move very slowly - about as fast as your fingernails grow.",
        "Where plates bump together, mountains push up! Where they pull apart, valleys form!",
        "Sometimes plates slide past each other and get stuck. When they slip - EARTHQUAKE!",
        "My plates have been moving for billions of years, rearranging continents like puzzle pieces.",
        "Africa and South America used to be joined together - you can see how they fit!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: PLATE TECTONICS", 'F2', 13)
    y -= 20
    science = [
        "Earth's crust is broken into about 15 major tectonic plates that slowly move.",
        "Convection currents in the hot mantle push and pull the plates (like a pot of boiling soup).",
        "Convergent boundaries: plates collide - mountains form (Himalayas!).",
        "Divergent boundaries: plates pull apart - new crust forms (Mid-Atlantic Ridge).",
        "Transform boundaries: plates slide past each other - earthquakes (San Andreas Fault).",
        "Plates move 1-10 cm per year - about as fast as your fingernails grow!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The Himalayas grow about 1 cm taller every year as India pushes into Asia!",
        "250 million years from now, scientists predict the continents will rejoin into 'Pangaea Ultima.'",
        "About 500,000 earthquakes are detected each year, but only 100,000 can be felt."
    ])
    y = try_this(doc, y, "Put crackers on pudding. Push them together (mountains form!) and pull apart (rift!). That is plate tectonics!")
    y = think_about_it(doc, y, "If continents are still moving, what will the world map look like in 100 million years?")

    # Chapter 4: My Fiery Breath
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: My Fiery Breath", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Sometimes my insides get so hot that melted rock pushes up through my skin!",
        "BOOM! A volcano erupts, shooting lava, ash, and gas high into the sky!",
        "I have about 1,500 active volcanoes around the world right now.",
        "Most of them are along the edges of my plates - a ring around the Pacific Ocean!",
        "Scientists call it the Ring of Fire because so many volcanoes circle the Pacific.",
        "My volcanoes helped create my atmosphere and even brought water to my surface!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: VOLCANOES", 'F2', 13)
    y -= 20
    science = [
        "Magma is melted rock below the surface; lava is melted rock ABOVE the surface.",
        "Volcanoes form where magma finds a path up through cracks in the crust.",
        "Shield volcanoes: wide and flat (Hawaii) - gentle lava flows.",
        "Stratovolcanoes: tall and steep (Mt. Fuji) - explosive and dangerous.",
        "The Ring of Fire: 75% of the world's volcanoes circle the Pacific Ocean.",
        "Volcanic eruptions helped form Earth's atmosphere by releasing gases from deep inside.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "There are more volcanoes under the ocean than on land!",
        "The biggest volcano on Earth is Mauna Loa in Hawaii (measured from the ocean floor).",
        "Volcanic soil is extremely fertile - that is why people live near volcanoes despite the danger."
    ])
    y = try_this(doc, y, "Build a volcano: pile sand around a cup, add baking soda inside, pour vinegar + red food coloring. ERUPTION!")
    y = think_about_it(doc, y, "Why do people choose to live near active volcanoes despite the danger?")

    # Chapter 5: My Blue Blanket
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: My Blue Blanket", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "I am wrapped in a beautiful invisible blanket called the atmosphere!",
        "It is made of gases: mostly nitrogen (78%) and oxygen (21%) that you breathe.",
        "My atmosphere protects you from the Sun's harmful rays and from space rocks!",
        "Without it, daytime would be boiling hot and nighttime would be freezing cold.",
        "It also keeps my temperature just right for life - like a greenhouse for the whole planet!",
        "But lately, humans are adding too many greenhouse gases and my blanket is getting too thick.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: THE ATMOSPHERE", 'F2', 13)
    y -= 20
    science = [
        "The atmosphere has layers: troposphere (weather), stratosphere (ozone), mesosphere, thermosphere.",
        "The ozone layer (in stratosphere) blocks 97% of the Sun's harmful UV radiation.",
        "Greenhouse effect: gases trap heat and keep Earth warm enough for life (naturally good!).",
        "BUT: extra CO2 from burning fossil fuels makes the greenhouse effect too strong.",
        "This 'enhanced' greenhouse effect is causing Earth's temperature to rise (climate change).",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "99% of the atmosphere is within 20 miles of the surface. Space is closer than you think!",
        "Without the greenhouse effect, Earth would average -18C (0F) instead of 15C (59F).",
        "The atmosphere weighs 5.5 quadrillion tons - pressing on you with 14.7 lbs per square inch!"
    ])
    y = try_this(doc, y, "Put a thermometer in a sealed clear jar in the sun vs one outside. The jar heats up more = greenhouse effect!")
    y = think_about_it(doc, y, "What would Earth be like without an atmosphere? (Hint: look at the Moon!)")

    # Chapter 6: My Rock Collection
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: My Rock Collection", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "I have the most amazing rock collection! Three types of rocks, endlessly recycling.",
        "When my volcanoes cool their lava, I make igneous rocks - born from fire!",
        "When wind and water wear rocks into tiny pieces that settle in layers, I make sedimentary rocks.",
        "And when heat and pressure squeeze and bake existing rocks, I make metamorphic rocks!",
        "These three types keep changing into each other - it is called the rock cycle!",
        "A rock on the ground today might have been lava, then sand, then squeezed into marble!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: THE ROCK CYCLE", 'F2', 13)
    y -= 20
    science = [
        "Igneous rocks: formed from cooled magma/lava (granite, basalt, obsidian).",
        "Sedimentary rocks: formed from layers of compressed sediment (sandstone, limestone, shale).",
        "Metamorphic rocks: changed by extreme heat and pressure (marble, slate, quartzite).",
        "The rock cycle: any rock type can become any other type given enough time!",
        "Igneous melts -> sediment erodes -> metamorphic gets squeezed -> melts again = cycle!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The oldest known rock on Earth is 4.03 billion years old (found in Canada).",
        "Diamonds are metamorphic - carbon squeezed under extreme pressure deep underground!",
        "Fossils are found in sedimentary rocks because layers bury dead organisms over time."
    ])
    y = try_this(doc, y, "Collect 3 rocks. Try to identify: Is each one igneous, sedimentary, or metamorphic? Use a guide!")
    y = think_about_it(doc, y, "If all rocks are constantly recycling, could the sand on a beach today have once been a volcano?")

    # Chapter 7: My Living Coat
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: My Living Coat", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The best thing about me? I am covered in LIFE! From deserts to jungles to frozen poles!",
        "I have rainforests so thick with life that millions of species live in them.",
        "I have deserts where clever animals survive with almost no water at all!",
        "I have frozen tundra where polar bears and penguins thrive in extreme cold.",
        "And my oceans are bursting with life from surface to deepest trench!",
        "All these different regions are called biomes - each one is a unique world of life!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: EARTH'S BIOMES", 'F2', 13)
    y -= 20
    science = [
        "Tropical Rainforest: warm, wet, most biodiversity. Contains 50% of all species!",
        "Desert: dry (less than 10 inches rain/year), hot days, cold nights.",
        "Tundra: freezing, permafrost, short summers, hardy plants and animals.",
        "Temperate Forest: four seasons, deciduous trees that lose leaves in fall.",
        "Ocean: largest biome, covering 71% of Earth, from warm coral reefs to icy depths.",
        "An ecosystem is all the living and non-living things interacting in one area.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Scientists estimate 8.7 million species exist on Earth - but only 1.2 million have been identified!",
        "Rainforests produce 28% of the world's oxygen despite covering only 6% of land.",
        "Biodiversity = more types of life. It makes ecosystems stronger and more resilient."
    ])
    y = try_this(doc, y, "Create an 'ecosystem in a jar': put soil, small plants, and a little water in a sealed jar. Watch it self-sustain!")
    y = think_about_it(doc, y, "Why is biodiversity important? What happens when too many species disappear?")

    # Chapter 8: Please Take Care of Me
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: Please Take Care of Me", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "I have taken care of life for 4.5 billion years. Now I need YOUR help!",
        "My climate is changing faster than at any time in millions of years.",
        "My forests are shrinking. My oceans are warming. My ice caps are melting.",
        "But here is the good news: humans are the smartest species I have ever hosted!",
        "You have the knowledge to fix these problems if you work together.",
        "Every small action matters - from recycling to planting trees to using less energy!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: TAKING CARE OF EARTH", 'F2', 13)
    y -= 20
    science = [
        "Climate change: Earth's average temperature rising due to extra greenhouse gases.",
        "Effects: melting ice, rising seas, more extreme weather, habitat loss.",
        "Solutions: renewable energy, planting trees, reducing waste, sustainable living.",
        "Conservation: protecting ecosystems, endangered species, and natural resources.",
        "Every person can help: reduce, reuse, recycle, walk more, learn more, share more!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y -= 15
    doc.add_text(margin, y, "MORAL:", 'F2', 14)
    y -= 18
    doc.add_text(margin, y, "Earth is our only home - every action we take matters for our planet's future!", 'F5', 12)
    y = science_fact_box(doc, y - 30, [
        "If everyone planted just one tree, that would be 8 billion new trees absorbing CO2!",
        "Reducing food waste could cut 8% of global greenhouse gas emissions.",
        "Young people around the world are leading the fight for climate action. You can too!"
    ])

    # Activities Page
    doc.new_page()
    doc.add_centered_text(720, "EARTH SCIENCE ACTIVITIES", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    doc.add_text(margin, 680, "1. ROCK COLLECTION SORTING:", 'F2', 12)
    doc.add_text(margin + 10, 660, "Collect 6-10 rocks. Sort them into igneous, sedimentary, and metamorphic.", 'F4', 10)
    doc.add_text(margin + 10, 644, "Hints: Igneous (crystals/glassy), Sedimentary (layers/gritty), Metamorphic (banded/shiny)", 'F4', 10)
    doc.add_text(margin, 610, "2. BUILD A VOLCANO:", 'F2', 12)
    doc.add_text(margin + 10, 590, "Materials: sand/clay, small bottle, baking soda, vinegar, red food coloring, dish soap", 'F4', 10)
    doc.add_text(margin + 10, 574, "Build a cone around the bottle, add baking soda inside, then pour in vinegar mix!", 'F4', 10)
    doc.add_text(margin, 540, "3. ECOSYSTEM IN A JAR:", 'F2', 12)
    doc.add_text(margin + 10, 520, "Get a large jar with lid. Add: gravel, activated charcoal, soil, small plants, water.", 'F4', 10)
    doc.add_text(margin + 10, 504, "Seal it and place in indirect light. The water cycle happens inside the jar!", 'F4', 10)
    doc.add_text(margin, 470, "4. MY EARTH PLEDGE - Things I will do:", 'F2', 12)
    pledges = [
        "[ ] Turn off lights when I leave a room",
        "[ ] Use a reusable water bottle",
        "[ ] Walk or bike instead of driving when possible",
        "[ ] Plant a tree or garden",
        "[ ] Reduce, reuse, and recycle",
        "[ ] Learn more about our planet",
    ]
    y = 448
    for p in pledges:
        doc.add_text(margin + 10, y, p, 'F4', 11)
        y -= 20

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "PLANET EARTH QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. How old is Earth?",
        "2. Name Earth's four layers from outside to center.",
        "3. What are tectonic plates?",
        "4. What is the difference between magma and lava?",
        "5. What gases make up most of our atmosphere?",
        "6. Name the three types of rocks.",
        "7. What is a biome? Name three.",
        "8. What is the greenhouse effect?",
        "9. What causes earthquakes?",
        "10. Name three things you can do to help Earth.",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 26

    # Vocabulary Page
    doc.new_page()
    doc.add_centered_text(720, "EARTH SCIENCE VOCABULARY", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    vocab = [
        ("Tectonic Plate", "A large piece of Earth's crust that slowly moves over the mantle"),
        ("Magma", "Melted rock below Earth's surface (called lava when it reaches the surface)"),
        ("Atmosphere", "The layer of gases surrounding Earth that protects us and provides air"),
        ("Biome", "A large region with similar climate, plants, and animals (desert, forest, etc.)"),
        ("Fossil", "Preserved remains or traces of ancient life found in rock"),
        ("Erosion", "The wearing away of rock and soil by water, wind, or ice over time"),
        ("Ecosystem", "All living and non-living things interacting in one area"),
        ("Renewable", "A resource that can be replaced naturally (sunlight, wind, trees)"),
    ]
    y = 680
    for word, defn in vocab:
        doc.add_text(margin, y, word, 'F2', 12)
        y -= 16
        doc.add_text(margin + 20, y, defn, 'F4', 10)
        y -= 26

    # Certificate
    doc.new_page()
    doc.add_filled_rect(50, 100, W - 100, H - 200, 0.95)
    doc.add_rect(60, 110, W - 120, H - 220, 2, 0.3)
    doc.add_centered_text(650, "EARTH SCIENTIST CERTIFICATE", 'F2', 20)
    doc.add_centered_text(600, "I understand our amazing planet!", 'F5', 14)
    doc.add_centered_text(550, "My favorite Earth science fact:", 'F4', 12)
    doc.add_line(150, 525, W - 150, 525, 0.5, 0.5)
    doc.add_centered_text(490, "My promise to help Earth:", 'F4', 12)
    doc.add_line(150, 465, W - 150, 465, 0.5, 0.5)
    doc.add_centered_text(400, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(360, "Date: _________________", 'F4', 14)
    doc.add_centered_text(280, "Certified Earth Scientist!", 'F2', 18)
    doc.add_centered_text(240, "Remember: This is our only planet. Take care of it!", 'F4', 11)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book275_Planet_Earth_Story.pdf')
    print("Book275_Planet_Earth_Story.pdf created successfully!")

if __name__ == '__main__':
    create_book()
