"""Book 268: DROPLET'S BIG ADVENTURE - A Science Story About the Water Cycle (Ages 5-9)"""
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
    doc.add_centered_text(660, "DROPLET'S BIG ADVENTURE", 'F2', 26, 1)
    doc.add_centered_text(625, "A Science Story About the Water Cycle", 'F5', 16, 0.9)
    doc.add_centered_text(595, "Ages 5-9", 'F4', 14, 0.8)
    doc.add_centered_text(500, "~ ~ ~ ~ ~ ~ ~ ~ ~ ~", 'F1', 20, 0.8)
    doc.add_centered_text(450, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
    doc.add_centered_text(420, "Science Story Series - Book 3", 'F4', 12, 0.7)
    doc.add_centered_text(300, "Follow Droplet on her endless journey", 'F4', 13, 0.8)
    doc.add_centered_text(275, "from ocean to sky and back again!", 'F4', 13, 0.8)
    doc.add_centered_text(100, "Educational Content | Real Science | Amazing Stories", 'F1', 10, 0.7)

    # Copyright
    doc.new_page()
    doc.add_centered_text(650, "DROPLET'S BIG ADVENTURE", 'F2', 16)
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
        "Chapter 1: Life in the Ocean",
        "Chapter 2: Rising Up!",
        "Chapter 3: Becoming a Cloud",
        "Chapter 4: The Big Fall",
        "Chapter 5: Down the Mountain",
        "Chapter 6: Underground Secret",
        "Chapter 7: Helping Plants Grow",
        "Chapter 8: Back to the Ocean",
    ]
    y = 670
    for ch in chapters:
        doc.add_text(margin, y, ch, 'F4', 13)
        y -= 30

    # Chapter 1: Life in the Ocean
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: Life in the Ocean", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Deep in the sparkling blue ocean lived a tiny water droplet named Droplet.",
        "She was one of billions and billions of water droplets in the enormous sea.",
        "Droplet loved swimming with the fish and riding the ocean waves.",
        "'I wonder what is beyond the surface?' Droplet thought one sunny day.",
        "She had heard stories from older droplets about amazing adventures above the water.",
        "'Someday, I will go on my own big adventure!' Droplet promised herself.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: OUR OCEANS", 'F2', 13)
    y -= 20
    science = [
        "Oceans cover about 71% of Earth's surface - that is almost three-quarters!",
        "There are five main oceans: Pacific, Atlantic, Indian, Southern, and Arctic.",
        "The Pacific Ocean is the biggest - it is larger than all the land on Earth combined!",
        "Ocean water is salty because rivers wash minerals from rocks into the sea.",
        "About 97% of all water on Earth is in the oceans. Only 3% is freshwater!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The ocean is home to over 230,000 known species of animals and plants.",
        "The deepest point in the ocean is the Mariana Trench - 36,000 feet deep!",
        "If you could drive a car to the bottom of the ocean, it would take about 7 hours."
    ])
    y = try_this(doc, y, "Fill a glass with water and add 2 tablespoons of salt. Taste it - that is like ocean water!")
    y = think_about_it(doc, y, "If most of Earth is covered by water, why is fresh water so precious?")

    # Chapter 2: Rising Up!
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: Rising Up!", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "One hot summer day, the Sun beat down on the ocean surface with powerful rays.",
        "Droplet felt herself getting warmer and warmer and warmer!",
        "'What is happening to me?' she exclaimed as she began to feel lighter.",
        "Suddenly, Droplet was floating UP! She was turning into invisible water vapor!",
        "'I am evaporating!' she shouted with excitement. 'I am becoming a gas!'",
        "Higher and higher she rose, leaving the ocean far below. The adventure had begun!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: EVAPORATION", 'F2', 13)
    y -= 20
    science = [
        "Evaporation is when liquid water turns into water vapor (an invisible gas).",
        "The Sun's energy heats water molecules, making them move faster and faster.",
        "When molecules move fast enough, they escape from the liquid into the air!",
        "Evaporation happens from oceans, lakes, rivers, puddles - even your wet laundry!",
        "Warm air can hold more water vapor than cold air. That is why hot days feel humid.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "About 90% of water in the atmosphere came from ocean evaporation.",
        "Evaporation is happening right now from every body of water on Earth!",
        "Hot water evaporates faster than cold water because molecules move faster."
    ])
    y = try_this(doc, y, "Put a shallow dish of water in the sun. Mark the water level. Check it the next day!")
    y = think_about_it(doc, y, "Why do puddles disappear on sunny days? Where does the water go?")

    # Chapter 3: Becoming a Cloud
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: Becoming a Cloud", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "High up in the sky, the air was much colder. Droplet started to shiver.",
        "'Brrr! It is freezing up here!' She felt herself changing again.",
        "The cold air turned her back from invisible vapor into a tiny visible droplet!",
        "She looked around and saw millions of other droplets gathering together.",
        "'We are forming a cloud!' her new friends cheered.",
        "Together, they made a big, fluffy, white cloud floating across the blue sky.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: CONDENSATION & CLOUDS", 'F2', 13)
    y -= 20
    science = [
        "Condensation is the opposite of evaporation - gas turns back into liquid.",
        "When warm, moist air rises and cools, water vapor condenses into tiny droplets.",
        "Clouds are made of billions of tiny water droplets or ice crystals.",
        "Each droplet forms around a tiny speck of dust or pollen in the air.",
        "Different cloud shapes tell us about the weather that is coming!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "An average cloud weighs about 1.1 million pounds! It floats because it is spread out.",
        "You can see condensation on a cold glass of water on a hot day.",
        "Fog is actually a cloud that forms close to the ground!"
    ])
    y = try_this(doc, y, "Breathe onto a cold window - the fog you see is condensation from your warm breath!")
    y = think_about_it(doc, y, "If clouds are so heavy, why do they float in the sky?")

    # Chapter 4: The Big Fall
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: The Big Fall", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The cloud grew bigger and bigger as more water droplets joined.",
        "It turned from white to gray and then to dark, heavy gray.",
        "'I am getting too heavy to stay up here!' Droplet cried.",
        "WHOOSH! She fell from the cloud, tumbling down through the air!",
        "'WHEEEEE! I am rain!' Droplet laughed as she fell faster and faster.",
        "All around her, millions of other droplets were falling too. It was raining!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: PRECIPITATION", 'F2', 13)
    y -= 20
    science = [
        "Precipitation is any water that falls from clouds: rain, snow, sleet, or hail.",
        "Raindrops form when tiny cloud droplets bump together and grow bigger.",
        "When droplets get too heavy for the air to hold up, they fall as rain!",
        "If it is cold enough, water freezes into snowflakes or ice pellets (sleet).",
        "Hailstones form when raindrops get pushed up in a storm and freeze over and over.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "A raindrop falls at about 14 miles per hour (faster if the drop is bigger).",
        "The wettest place on Earth gets about 467 inches of rain per year!",
        "Raindrops are not actually teardrop-shaped - they look more like hamburger buns!"
    ])
    y = try_this(doc, y, "Put a cup outside when it rains. Measure how much water collects in one hour!")
    y = think_about_it(doc, y, "What makes it snow instead of rain? What is the difference?")

    # Chapter 5: Down the Mountain
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: Down the Mountain", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "SPLASH! Droplet landed on the top of a tall mountain.",
        "She joined a tiny trickle of water running down the rocky slope.",
        "More and more droplets joined until the trickle became a stream!",
        "'We are getting stronger together!' Droplet cheered as they flowed faster.",
        "The stream became a river, winding through valleys and past towns.",
        "Droplet could feel herself slowly wearing away the rocks beneath her.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: RIVERS & EROSION", 'F2', 13)
    y -= 20
    science = [
        "Rivers start as small streams high in the mountains from rain or melting snow.",
        "Gravity pulls water downhill, making it flow from mountains toward the ocean.",
        "Erosion is when flowing water wears away rock and soil over time.",
        "The Grand Canyon was carved by the Colorado River over millions of years!",
        "A watershed is all the land area that drains water into a particular river.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The Nile River in Africa is the longest river in the world (4,130 miles).",
        "Rivers carry tiny bits of rock and soil all the way to the ocean.",
        "Water always flows downhill - it follows the path of least resistance."
    ])
    y = try_this(doc, y, "Pour water on a pile of sand or dirt. Watch how it carves channels - that is erosion!")
    y = think_about_it(doc, y, "How did the Grand Canyon form? How long do you think it took?")

    # Chapter 6: Underground Secret
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: Underground Secret", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Some of Droplet's friends did not stay in the river. They soaked into the ground!",
        "Droplet decided to follow them on this underground adventure.",
        "She seeped through soil, squeezed between grains of sand, and went deeper.",
        "'It is dark down here!' Droplet said. 'But I can feel other water all around me.'",
        "She had found a hidden underground lake called an aquifer!",
        "'So this is where some drinking water comes from!' Droplet realized.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: GROUNDWATER", 'F2', 13)
    y -= 20
    science = [
        "When rain soaks into the ground, it becomes groundwater.",
        "Groundwater fills the spaces between soil particles and cracks in rocks.",
        "An aquifer is a layer of rock or sand that holds lots of groundwater.",
        "Wells are holes drilled down to reach aquifers so people can pump up clean water.",
        "Groundwater can stay underground for thousands of years before resurfacing!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "About 30% of the world's freshwater is groundwater (most freshwater is in ice!).",
        "Springs happen when groundwater naturally flows out of the earth.",
        "It can take a single drop of water 10,000 years to travel through a large aquifer."
    ])
    y = try_this(doc, y, "Fill a clear cup with small rocks. Slowly pour water in - watch it fill the spaces between rocks!")
    y = think_about_it(doc, y, "Where does the water in your home come from? A well, a river, or a lake?")

    # Chapter 7: Helping Plants Grow
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: Helping Plants Grow", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Underground, Droplet was pulled toward something - a tree root!",
        "'The tree is drinking me up!' Droplet exclaimed as she was absorbed.",
        "She traveled UP through the roots, into the trunk, and out to the leaves!",
        "'I am helping this tree make food from sunlight!' Droplet said proudly.",
        "When the Sun heated the leaf, Droplet evaporated back into the air again!",
        "'This is called transpiration!' she shouted. 'I am going back to the sky!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: TRANSPIRATION", 'F2', 13)
    y -= 20
    science = [
        "Plants absorb water from the soil through their roots.",
        "Water travels up through the plant like drinking through a straw.",
        "Plants use water plus sunlight plus carbon dioxide to make sugar (food) - photosynthesis!",
        "Transpiration is when water evaporates from tiny holes in leaves (stomata).",
        "A large tree can release 100 gallons of water into the air per day through its leaves!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "A large oak tree drinks about 40,000 gallons of water from the soil each year.",
        "Plants release oxygen as a waste product - which is what we breathe!",
        "If you put a plastic bag over a leaf on a sunny day, you will see water collect inside."
    ])
    y = try_this(doc, y, "Put a clear plastic bag over a leafy branch. In a few hours, see water droplets form inside!")
    y = think_about_it(doc, y, "If trees release water into the air, do forests help make rain?")

    # Chapter 8: Back to the Ocean
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: Back to the Ocean", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "After her time as cloud, rain, river, groundwater, and tree visitor,",
        "Droplet finally flowed back into the great blue ocean where she started!",
        "'I am home!' Droplet cheered, reuniting with her ocean friends.",
        "'Tell us about your adventure!' they cried. 'Where did you go?'",
        "Droplet told them everything. 'And the best part?' she smiled.",
        "'I will do it all over again! The water cycle never, ever stops!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: THE WATER CYCLE NEVER ENDS", 'F2', 13)
    y -= 20
    science = [
        "The water cycle has been running for billions of years without stopping!",
        "The water you drink today might have been dinosaur bathwater millions of years ago!",
        "No new water is created - the same water just keeps cycling over and over.",
        "Evaporation, condensation, precipitation, collection - round and round it goes.",
        "Every living thing on Earth depends on the water cycle to survive.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y -= 20
    doc.add_text(margin, y, "MORAL:", 'F2', 14)
    y -= 20
    doc.add_text(margin, y, "Everything in nature is connected - even a tiny droplet matters!", 'F5', 13)
    y = science_fact_box(doc, y - 30, [
        "Earth has the same amount of water now as when dinosaurs roamed the planet!",
        "Only about 0.3% of all water on Earth is usable freshwater for humans.",
        "It takes about 9 days for a water molecule to complete the cycle from evaporation to rain."
    ])

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "WATER CYCLE QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. What percentage of Earth is covered by oceans?",
        "2. What is it called when liquid water turns into gas?",
        "3. What are clouds made of?",
        "4. Name three types of precipitation.",
        "5. What is an aquifer?",
        "6. What is transpiration?",
        "7. What provides the energy that drives the water cycle?",
        "8. Can new water be created? Why or why not?",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 30

    # Activity: Draw the Water Cycle
    doc.new_page()
    doc.add_centered_text(720, "DRAW THE WATER CYCLE!", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    doc.add_text(margin, 680, "Draw and label each step of the water cycle in the space below:", 'F4', 12)
    doc.add_text(margin, 655, "Include: Ocean, Evaporation, Cloud, Precipitation, River, Groundwater", 'F4', 11)
    doc.add_rect(margin, 150, W - 2*margin, 480, 1, 0.5)
    doc.add_text(margin, 120, "Label these words in your drawing:", 'F2', 11)
    doc.add_text(margin, 100, "Evaporation | Condensation | Precipitation | Collection | Transpiration", 'F3', 10)

    # Certificate Page
    doc.new_page()
    doc.add_filled_rect(50, 100, W - 100, H - 200, 0.95)
    doc.add_rect(60, 110, W - 120, H - 220, 2, 0.3)
    doc.add_centered_text(650, "I AM A WATER SCIENTIST!", 'F2', 22)
    doc.add_centered_text(600, "I completed Droplet's Big Adventure!", 'F5', 14)
    doc.add_centered_text(550, "I can explain the water cycle:", 'F4', 12)
    y = 510
    steps = ["Evaporation (liquid to gas)", "Condensation (gas to liquid)",
             "Precipitation (rain/snow)", "Collection (rivers/groundwater)"]
    for s in steps:
        doc.add_text(150, y, "[ ] " + s, 'F4', 12)
        y -= 28
    doc.add_centered_text(350, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(310, "Date: _________________", 'F4', 14)
    doc.add_centered_text(250, "Water Cycle Expert!", 'F2', 18)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book268_Water_Cycle_Story.pdf')
    print("Book268_Water_Cycle_Story.pdf created successfully!")

if __name__ == '__main__':
    create_book()
