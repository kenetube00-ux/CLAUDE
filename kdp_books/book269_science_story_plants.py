"""Book 269: THE SECRET LIFE OF PLANTS - A Science Story About How Plants Grow (Ages 5-9)"""
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
    doc.add_filled_rect(0, 0, W, H, 0.1)
    doc.add_centered_text(660, "THE SECRET LIFE OF PLANTS", 'F2', 24, 1)
    doc.add_centered_text(625, "A Science Story About How Plants Grow", 'F5', 16, 0.9)
    doc.add_centered_text(595, "Ages 5-9", 'F4', 14, 0.8)
    doc.add_centered_text(500, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
    doc.add_centered_text(470, "Science Story Series - Book 4", 'F4', 12, 0.7)
    doc.add_centered_text(350, "Watch a tiny seed grow into", 'F4', 13, 0.8)
    doc.add_centered_text(325, "a mighty tree in this amazing story!", 'F4', 13, 0.8)
    doc.add_centered_text(100, "Educational Content | Real Science | Amazing Stories", 'F1', 10, 0.7)

    # Copyright
    doc.new_page()
    doc.add_centered_text(650, "THE SECRET LIFE OF PLANTS", 'F2', 16)
    doc.add_text(margin, 600, "Author: Daniel Tesfamariam", 'F4', 11)
    doc.add_text(margin, 580, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", 'F4', 10)
    doc.add_text(margin, 560, "No part of this publication may be reproduced without permission.", 'F4', 10)
    doc.add_text(margin, 530, "For ages 5-9. Scientific concepts simplified for young readers.", 'F4', 10)
    doc.add_text(margin, 500, "First Edition, 2025", 'F4', 10)

    # TOC
    doc.new_page()
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    chapters = [
        "Chapter 1: A Tiny Seed",
        "Chapter 2: Waking Up",
        "Chapter 3: Reaching for the Sun",
        "Chapter 4: Making Food from Sunlight",
        "Chapter 5: Drinking Through Roots",
        "Chapter 6: Flowers and Friends",
        "Chapter 7: Fruits and Seeds",
        "Chapter 8: A Mighty Tree",
    ]
    y = 670
    for ch in chapters:
        doc.add_text(margin, y, ch, 'F4', 13)
        y -= 30

    # Chapter 1: A Tiny Seed
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: A Tiny Seed", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Once upon a time, there was a tiny seed named Seedling.",
        "She was no bigger than a pea, buried in the dark, cool earth.",
        "'It is so dark down here,' Seedling whispered. 'When will I grow?'",
        "A wise old worm crawled by. 'Be patient, little one. Your time will come.'",
        "'Inside you is everything you need to become something amazing!'",
        "Seedling did not know it yet, but she was going to become a mighty oak tree!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: INSIDE A SEED", 'F2', 13)
    y -= 20
    science = [
        "A seed is like a tiny suitcase packed with everything a plant needs to start life.",
        "The seed coat is a tough outer shell that protects the baby plant inside.",
        "Inside is an embryo - a tiny baby plant with a root, stem, and leaves already formed!",
        "Seeds also carry stored food (endosperm) to feed the baby plant until it can make its own.",
        "Seeds can wait dormant for years, even centuries, until conditions are just right!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The world's oldest germinated seed was 2,000 years old (a date palm from Israel)!",
        "The biggest seed in the world is the coco de mer - it can weigh 40 pounds!",
        "A single sunflower head can contain up to 2,000 seeds."
    ])
    y = try_this(doc, y, "Soak a bean seed overnight, then carefully open it. Can you see the tiny baby plant inside?")
    y = think_about_it(doc, y, "How do seeds 'know' when it is the right time to start growing?")

    # Chapter 2: Waking Up
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: Waking Up", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "One spring morning, rain soaked into the soil around Seedling.",
        "'Oh! Water!' Seedling felt herself swelling up as she soaked it in.",
        "The water softened her tough seed coat. She could feel herself waking up!",
        "A tiny white root poked out from the bottom of her shell.",
        "'I am growing!' Seedling cheered. 'I am finally growing!'",
        "The root pushed deeper into the soil, anchoring her in place. Life had begun!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: GERMINATION", 'F2', 13)
    y -= 20
    science = [
        "Germination is when a seed starts to grow into a new plant.",
        "Seeds need three things to germinate: water, warmth, and oxygen.",
        "Water soaks into the seed, making it swell and crack open the seed coat.",
        "The first thing to grow is always the root (radicle) - it grows downward.",
        "Then the shoot (plumule) pushes upward toward the light and air.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Some seeds germinate in just 1-2 days; others take weeks or months!",
        "Bean seeds are great for watching germination - they sprout in about 5 days.",
        "Some seeds need fire, cold, or even animal digestion to trigger germination!"
    ])
    y = try_this(doc, y, "Put a bean seed between wet paper towels in a bag. Watch it sprout over 5 days!")
    y = think_about_it(doc, y, "Why does the root always grow DOWN and the shoot always grow UP?")

    # Chapter 3: Reaching for the Sun
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: Reaching for the Sun", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Seedling's green shoot pushed up through the dark soil with all her might.",
        "POP! She broke through the surface into the bright, beautiful sunlight!",
        "'The world is so big and bright!' Seedling gasped, seeing the sky for the first time.",
        "Her tiny stem leaned toward the warm sunshine like a dancer reaching for a spotlight.",
        "Two little leaves unfurled like tiny green hands reaching toward the light.",
        "'I need that sunlight!' Seedling could feel it. The light was her energy source.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: PHOTOTROPISM", 'F2', 13)
    y -= 20
    science = [
        "Phototropism means growing toward light (photo=light, tropism=turning).",
        "Plants can actually sense where light is coming from and bend toward it!",
        "A hormone called auxin collects on the shady side, making that side grow faster.",
        "The shady side growing faster causes the plant to bend toward the light.",
        "This is why houseplants lean toward windows - they are chasing the sunshine!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Sunflowers are famous for following the sun across the sky (when young)!",
        "Roots show negative phototropism - they grow AWAY from light, deeper into soil.",
        "Some plants can completely turn their leaves to face the sun during the day."
    ])
    y = try_this(doc, y, "Put a plant near a window. After a week, see how it leans toward the light. Rotate it and watch!")
    y = think_about_it(doc, y, "What would happen to a plant if it could not sense light at all?")

    # Chapter 4: Making Food from Sunlight
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: Making Food from Sunlight", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Seedling's leaves grew bigger and greener every day.",
        "'I am making my own food!' she announced proudly to the worm.",
        "'How?' asked the worm. 'You do not have a mouth or a kitchen!'",
        "'I use sunlight, water from my roots, and air from the sky!' Seedling explained.",
        "'My green leaves mix them all together to make sugar - my favorite food!'",
        "'And the best part? I breathe out oxygen that animals need to live!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: PHOTOSYNTHESIS", 'F2', 13)
    y -= 20
    science = [
        "Photosynthesis is how plants make food from sunlight (photo=light, synthesis=making).",
        "The recipe: Sunlight + Water + Carbon Dioxide = Sugar + Oxygen.",
        "Chlorophyll is the green chemical in leaves that captures sunlight energy.",
        "Plants take in CO2 (carbon dioxide) from the air through tiny holes in their leaves.",
        "They release oxygen (O2) as a waste product - which is what all animals breathe!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "One large tree produces enough oxygen for two people to breathe all year!",
        "Leaves are green because chlorophyll reflects green light but absorbs red and blue.",
        "Photosynthesis produces all the oxygen in Earth's atmosphere!"
    ])
    y = try_this(doc, y, "Put a water plant (like Elodea) in water in sunlight. Watch oxygen bubbles form on the leaves!")
    y = think_about_it(doc, y, "If plants make oxygen and we make carbon dioxide, how do we help each other?")

    # Chapter 5: Drinking Through Roots
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: Drinking Through Roots", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "While Seedling's leaves worked above ground, her roots were busy underground.",
        "They spread out like fingers reaching through the soil in every direction.",
        "'I am so thirsty!' Seedling said. 'My roots need to find water!'",
        "Tiny root hairs, thinner than human hair, absorbed water like tiny sponges.",
        "The water traveled up through the stem like drinking through a straw.",
        "'All the way from my roots to my highest leaf!' Seedling marveled at herself.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: ROOT SYSTEMS", 'F2', 13)
    y -= 20
    science = [
        "Roots have two main jobs: anchoring the plant in soil and absorbing water and minerals.",
        "Root hairs are tiny extensions that greatly increase the surface area for absorption.",
        "Water moves from soil into roots through osmosis (water moves toward higher concentration).",
        "Some trees have roots that spread wider underground than the tree's branches above!",
        "Water travels up through tiny tubes (xylem) against gravity using capillary action.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "A single rye grass plant can have 14 billion root hairs!",
        "The deepest known root belongs to a fig tree - over 400 feet deep!",
        "Roots can sense water and grow toward it - this is called hydrotropism."
    ])
    y = try_this(doc, y, "Put a white flower (carnation) in colored water. Watch the color travel up the stem!")
    y = think_about_it(doc, y, "How does water get from the roots to the top of a 300-foot tall tree?")

    # Chapter 6: Flowers and Friends
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: Flowers and Friends", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "After many seasons of growing, something wonderful happened to Seedling.",
        "Beautiful flowers bloomed on her branches for the very first time!",
        "'Why am I making flowers?' Seedling wondered. 'They are so pretty!'",
        "BUZZ! A fuzzy bumblebee landed on one of her flowers, covered in yellow dust.",
        "'Thank you for the sweet nectar!' the bee said, flying to another flower.",
        "'That bee is helping me make seeds!' Seedling realized. 'We are a team!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: POLLINATION", 'F2', 13)
    y -= 20
    science = [
        "Flowers are not just pretty - they are a plant's way of making new plants!",
        "Pollen is a yellow powder made by the male part of the flower (stamen).",
        "Pollination happens when pollen reaches the female part (pistil) of another flower.",
        "Bees, butterflies, birds, bats, and even wind carry pollen between flowers.",
        "Flowers attract pollinators with bright colors, sweet scent, and tasty nectar.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Bees pollinate about 75% of the fruits and vegetables we eat!",
        "Some flowers only bloom at night to attract moth and bat pollinators.",
        "Without pollinators, we would lose most of our food crops!"
    ])
    y = try_this(doc, y, "Look closely at a flower. Can you find the stamen (pollen) and pistil (center)? Use a magnifier!")
    y = think_about_it(doc, y, "Why are so many flowers brightly colored? Who are they trying to attract?")

    # Chapter 7: Fruits and Seeds
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: Fruits and Seeds", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "After the bees did their work, Seedling's flowers changed into something new.",
        "Where each flower had been, a fruit began to grow - with seeds inside!",
        "'My babies!' Seedling said proudly, looking at her acorns (oak tree fruits).",
        "A squirrel came and took some acorns, burying them in the ground far away.",
        "The wind blew some seeds to new places. A bird ate a berry and flew off.",
        "'My children will grow in new places all over the forest!' Seedling was so happy.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: SEED DISPERSAL", 'F2', 13)
    y -= 20
    science = [
        "After pollination, flowers develop into fruits that contain seeds.",
        "Seeds need to travel away from the parent plant to find space and sunlight.",
        "Wind dispersal: Dandelion seeds have 'parachutes,' maple seeds have 'helicopters.'",
        "Animal dispersal: Birds eat berries and drop seeds far away in their droppings.",
        "Water dispersal: Coconuts float across oceans to reach new islands!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Dandelion seeds can travel up to 5 miles on the wind!",
        "Every fruit you eat started as a flower - apples, oranges, even tomatoes!",
        "Some seeds (like burrs) have tiny hooks that stick to animal fur for a free ride."
    ])
    y = try_this(doc, y, "Collect different seeds. Sort them by how they travel: wind, animal, water, or explosion!")
    y = think_about_it(doc, y, "Why is it important that seeds travel far from the parent plant?")

    # Chapter 8: A Mighty Tree
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: A Mighty Tree", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Years passed. Seasons came and went. Seedling grew taller every year.",
        "She was no longer a tiny seedling - she was now a magnificent oak tree!",
        "Birds built nests in her branches. Squirrels stored acorns in her trunk.",
        "Children played in her shade on hot summer days.",
        "'I started as a tiny seed no bigger than a marble,' she remembered.",
        "'And now look at me! Patience and persistence helped me grow into something great!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: TREE RINGS AND GROWTH", 'F2', 13)
    y -= 20
    science = [
        "Trees grow a new layer of wood each year, creating visible rings in the trunk.",
        "You can count a tree's rings to discover its age - one ring per year!",
        "Wide rings mean a good year with plenty of rain; thin rings mean drought.",
        "The oldest living tree is over 5,000 years old (a bristlecone pine in California)!",
        "Trees produce oxygen, clean the air, provide habitat, and prevent soil erosion.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y -= 20
    doc.add_text(margin, y, "MORAL:", 'F2', 14)
    y -= 20
    doc.add_text(margin, y, "Great things start small - patience and persistence make you grow!", 'F5', 13)
    y = science_fact_box(doc, y - 30, [
        "A single oak tree can produce 70,000 acorns in one year!",
        "Trees communicate underground through a 'wood wide web' of fungal networks.",
        "The tallest tree in the world is a redwood named Hyperion - 380 feet tall!"
    ])

    # Activity: Label Plant Parts
    doc.new_page()
    doc.add_centered_text(720, "ACTIVITY: LABEL THE PLANT PARTS", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    doc.add_text(margin, 680, "Draw a plant and label these parts:", 'F4', 12)
    parts = [
        "1. Roots - absorb water and minerals, anchor the plant",
        "2. Stem - supports the plant, carries water up and food down",
        "3. Leaves - make food through photosynthesis",
        "4. Flower - makes seeds for new plants",
        "5. Fruit - protects and disperses seeds",
        "6. Seed - contains a baby plant and food supply",
    ]
    y = 650
    for p in parts:
        doc.add_text(margin, y, p, 'F4', 11)
        y -= 22
    doc.add_rect(margin, 150, W - 2*margin, 340, 1, 0.5)
    doc.add_centered_text(130, "Draw your plant here!", 'F4', 12, 0.4)

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "PLANT SCIENCE QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. What three things does a seed need to germinate?",
        "2. What is photosynthesis? (Describe the recipe!)",
        "3. What makes leaves green?",
        "4. What is pollination?",
        "5. Name three ways seeds can travel to new places.",
        "6. How can you tell how old a tree is?",
        "7. What is phototropism?",
        "8. What do roots absorb from the soil?",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 30

    # Certificate Page
    doc.new_page()
    doc.add_filled_rect(50, 100, W - 100, H - 200, 0.95)
    doc.add_rect(60, 110, W - 120, H - 220, 2, 0.3)
    doc.add_centered_text(650, "I AM A PLANT SCIENTIST!", 'F2', 22)
    doc.add_centered_text(600, "I understand the secret life of plants!", 'F5', 14)
    doc.add_centered_text(550, "My favorite plant fact:", 'F4', 12)
    doc.add_line(150, 520, W - 150, 520, 0.5, 0.5)
    doc.add_line(150, 480, W - 150, 480, 0.5, 0.5)
    doc.add_centered_text(420, "I planted a seed and it grew: YES / NOT YET", 'F4', 12)
    doc.add_centered_text(360, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(320, "Date: _________________", 'F4', 14)
    doc.add_centered_text(250, "Certified Plant Expert!", 'F2', 18)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book269_Secret_Life_Plants.pdf')
    print("Book269_Secret_Life_Plants.pdf created successfully!")

if __name__ == '__main__':
    create_book()
