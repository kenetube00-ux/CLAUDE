"""Book 270: WEATHER WONDERS - A Science Story About Storms, Sunshine & Seasons (Ages 6-11)"""
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
    doc.add_centered_text(660, "WEATHER WONDERS", 'F2', 28, 1)
    doc.add_centered_text(620, "A Science Story About Storms,", 'F5', 16, 0.9)
    doc.add_centered_text(598, "Sunshine & Seasons", 'F5', 16, 0.9)
    doc.add_centered_text(565, "Ages 6-11", 'F4', 14, 0.8)
    doc.add_centered_text(490, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
    doc.add_centered_text(460, "Science Story Series - Book 5", 'F4', 12, 0.7)
    doc.add_centered_text(350, "Join Sunny the Weather Reporter on an", 'F4', 13, 0.8)
    doc.add_centered_text(325, "exciting investigation of weather!", 'F4', 13, 0.8)
    doc.add_centered_text(100, "Educational Content | Real Science | Amazing Stories", 'F1', 10, 0.7)

    # Copyright
    doc.new_page()
    doc.add_centered_text(650, "WEATHER WONDERS", 'F2', 16)
    doc.add_text(margin, 600, "Author: Daniel Tesfamariam", 'F4', 11)
    doc.add_text(margin, 580, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", 'F4', 10)
    doc.add_text(margin, 560, "No part of this publication may be reproduced without permission.", 'F4', 10)
    doc.add_text(margin, 530, "For ages 6-11. Scientific concepts simplified for young readers.", 'F4', 10)
    doc.add_text(margin, 500, "First Edition, 2025", 'F4', 10)

    # TOC
    doc.new_page()
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    chapters = [
        "Chapter 1: Why Is the Sky Blue?",
        "Chapter 2: Cloud Detectives",
        "Chapter 3: Thunder and Lightning!",
        "Chapter 4: The Spinning Storm",
        "Chapter 5: Snowflake Magic",
        "Chapter 6: The Rainbow Surprise",
        "Chapter 7: Why Do Seasons Change?",
        "Chapter 8: Weather vs Climate",
    ]
    y = 670
    for ch in chapters:
        doc.add_text(margin, y, ch, 'F4', 13)
        y -= 30

    # Chapter 1: Why Is the Sky Blue?
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: Why Is the Sky Blue?", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Sunny loved asking questions about weather. Today she had a big one.",
        "'Mom, why is the sky blue? Why not green or purple or red?'",
        "Her mom smiled. 'That is a great science question! Let me show you.'",
        "She held a glass prism in the sunlight and a rainbow appeared on the wall!",
        "'Sunlight looks white, but it is actually made of ALL the colors mixed together!'",
        "'The sky is blue because of how those colors bounce around in the atmosphere.'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: LIGHT SCATTERING", 'F2', 13)
    y -= 20
    science = [
        "Sunlight is made of all colors of the rainbow mixed together (white light).",
        "When sunlight hits tiny gas molecules in the atmosphere, it bounces around (scatters).",
        "Blue light has a short wavelength, so it scatters much more than other colors.",
        "This scattered blue light reaches our eyes from every direction - making the sky look blue!",
        "At sunset, light travels through more atmosphere, scattering away all the blue,",
        "leaving longer-wavelength red and orange light - that is why sunsets are red!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The sky on Mars looks pinkish-red because of dust particles in its thin atmosphere.",
        "If Earth had no atmosphere, the sky would be black (like on the Moon)!",
        "Violet light scatters even more than blue, but our eyes are more sensitive to blue."
    ])
    y = try_this(doc, y, "Fill a glass with water, add a drop of milk, and shine a flashlight through it. See blue scattering!")
    y = think_about_it(doc, y, "Why do you think the sky turns orange and red during sunset?")

    # Chapter 2: Cloud Detectives
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: Cloud Detectives", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Sunny lay on the grass and looked up at the clouds floating by.",
        "'Every cloud tells a story about what weather is coming!' she said to her friend.",
        "Some clouds were big and puffy like cotton balls. Others were thin and wispy.",
        "'That flat, dark one means rain is probably coming,' Sunny predicted.",
        "Sure enough, twenty minutes later, the rain began to fall!",
        "'How did you know that?' her friend asked, amazed. 'Science!' Sunny grinned.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: TYPES OF CLOUDS", 'F2', 13)
    y -= 20
    science = [
        "Cumulus: Big, puffy, flat-bottomed clouds that look like cotton balls. Usually fair weather.",
        "Stratus: Low, flat, gray blanket clouds that cover the whole sky. Light rain or drizzle.",
        "Cirrus: Thin, wispy, feathery clouds very high up. Made of ice crystals.",
        "Cumulonimbus: Giant tower clouds that bring thunderstorms, heavy rain, and hail!",
        "Clouds form when warm air rises, cools, and water vapor condenses into droplets.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Clouds float because the tiny water droplets are spread over a huge area.",
        "The highest clouds (noctilucent) form 50 miles up - you can see them at night!",
        "Cloud names come from Latin: cumulus=heap, stratus=layer, cirrus=curl."
    ])
    y = try_this(doc, y, "Keep a cloud journal for a week. Draw the clouds you see and note what weather follows!")
    y = think_about_it(doc, y, "Can you predict tomorrow's weather by looking at today's clouds?")

    # Chapter 3: Thunder and Lightning!
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: Thunder and Lightning!", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "CRACK! BOOM! A thunderstorm rolled in one afternoon.",
        "Sunny was not afraid - she was fascinated! She started counting.",
        "'One-Mississippi, two-Mississippi, three...' BOOM! 'Three miles away!'",
        "'The lightning and thunder happen at the same time,' Sunny explained,",
        "'but light travels much faster than sound, so we see the flash first!'",
        "She watched the incredible light show from the safety of her window.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: LIGHTNING & THUNDER", 'F2', 13)
    y -= 20
    science = [
        "Lightning is a giant spark of electricity between clouds or between a cloud and ground.",
        "Inside storm clouds, ice particles collide and build up electrical charges.",
        "Positive charges collect at the top, negative at the bottom, until ZAP - lightning!",
        "Lightning is 5 times hotter than the surface of the Sun (54,000 degrees F)!",
        "Thunder is the sound of air rapidly expanding from the extreme heat of lightning.",
        "Light travels at 186,000 miles/sec; sound at only 1,100 ft/sec. That is the delay!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Earth gets struck by lightning about 100 times every second!",
        "Count seconds between flash and boom, divide by 5 = miles away.",
        "Lightning can be up to 5 miles long and happen in under a millisecond."
    ])
    y = try_this(doc, y, "Rub a balloon on your hair in the dark - see tiny sparks? That is static electricity like lightning!")
    y = think_about_it(doc, y, "Why should you NEVER stand under a tree during a lightning storm?")

    # Chapter 4: The Spinning Storm
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: The Spinning Storm", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Sunny watched a documentary about the most powerful storms on Earth.",
        "'Hurricanes are like giant spinning engines powered by warm ocean water!'",
        "She learned that these massive storms can be 600 miles wide!",
        "'And tornadoes are like nature's vacuum cleaners,' the narrator explained.",
        "'They form when warm and cold air collide, creating a spinning vortex.'",
        "Sunny was amazed by nature's power, but also glad she knew how to stay safe.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: EXTREME STORMS", 'F2', 13)
    y -= 20
    science = [
        "Hurricanes form over warm ocean water (above 80F) when moist air rises and spins.",
        "They can be 200-600 miles wide with winds over 157 mph (Category 5)!",
        "The calm center is called the 'eye' - it can be 20-40 miles across.",
        "Tornadoes form when warm, moist air meets cold, dry air, creating rotation.",
        "Tornado winds can reach 300 mph - the fastest winds on Earth!",
        "SAFETY: Go to a basement or interior room. Stay away from windows!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The US averages about 1,200 tornadoes per year (most of any country).",
        "A hurricane releases energy equal to 10,000 nuclear bombs per day!",
        "Hurricanes in the Pacific are called 'typhoons'; in the Indian Ocean, 'cyclones.'"
    ])
    y = try_this(doc, y, "Fill a bottle with water, flip it upside down, and swirl it - you made a vortex (mini tornado)!")
    y = think_about_it(doc, y, "Why do hurricanes weaken quickly after reaching land?")

    # Chapter 5: Snowflake Magic
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: Snowflake Magic", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Winter arrived and with it came Sunny's favorite weather event: SNOW!",
        "She caught a snowflake on her dark mitten and looked at it closely.",
        "'It is a perfect six-pointed crystal!' she gasped. 'Like a tiny ice star!'",
        "'Every single snowflake has six sides, but no two are exactly the same!'",
        "She spent an hour catching and examining snowflakes, each one unique.",
        "'Nature is the greatest artist,' Sunny decided, watching the world turn white.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: HOW SNOW FORMS", 'F2', 13)
    y -= 20
    science = [
        "Snowflakes form when water vapor freezes directly into ice crystals in clouds.",
        "They always have six sides because of how water molecules bond together.",
        "As a crystal falls through the cloud, it grows arms and branches in unique patterns.",
        "The shape depends on temperature and humidity - that is why each one is different!",
        "Fresh snow is actually about 90-95% air trapped between the crystals.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The largest snowflake ever recorded was 15 inches wide (Montana, 1887)!",
        "It is NOT true that Eskimos have 50 words for snow (but they do have several).",
        "Snow appears white because light bounces off all the crystal surfaces."
    ])
    y = try_this(doc, y, "Catch snowflakes on black paper or fabric and use a magnifying glass to see the crystals!")
    y = think_about_it(doc, y, "If every snowflake is unique, how many different designs are possible?")

    # Chapter 6: The Rainbow Surprise
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: The Rainbow Surprise", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "After a spring rain shower, the sun came out and Sunny rushed outside.",
        "'LOOK!' she shouted, pointing at the sky. A beautiful rainbow arched overhead!",
        "Red, orange, yellow, green, blue, indigo, violet - all the colors in perfect order.",
        "'A rainbow is like nature's prism!' Sunny explained to her little brother.",
        "'Each raindrop acts like a tiny glass prism, splitting white light into colors!'",
        "'But you can only see it when the sun is behind you and rain is in front of you.'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: LIGHT REFRACTION", 'F2', 13)
    y -= 20
    science = [
        "White sunlight is made up of all colors (red, orange, yellow, green, blue, indigo, violet).",
        "When light enters a raindrop, it slows down and bends - this is called refraction.",
        "Inside the drop, light reflects off the back surface like a mirror.",
        "As light exits the drop, it bends again, separating into all its colors!",
        "ROYGBIV helps you remember the rainbow color order.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "You can never reach the end of a rainbow - it moves as you move!",
        "From an airplane, you can see a full-circle rainbow (not just an arch)!",
        "Double rainbows happen when light reflects twice inside each raindrop."
    ])
    y = try_this(doc, y, "On a sunny day, spray a garden hose with the sun behind you. Make your own rainbow!")
    y = think_about_it(doc, y, "Why do the colors in a rainbow always appear in the same order?")

    # Chapter 7: Why Do Seasons Change?
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: Why Do Seasons Change?", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "'Why is it hot in summer and cold in winter?' Sunny wondered.",
        "'Is it because Earth is closer to the Sun in summer?' her friend guessed.",
        "'Actually, no!' Sunny had looked it up. 'It is because Earth is TILTED!'",
        "'Our planet leans to one side at 23.5 degrees as it orbits the Sun.'",
        "'When our half tilts toward the Sun, we get more direct sunlight - that is summer!'",
        "'When it tilts away, sunlight hits at an angle - that is winter!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: EARTH'S TILT & SEASONS", 'F2', 13)
    y -= 20
    science = [
        "Earth is tilted at 23.5 degrees on its axis (like a leaning spinning top).",
        "As Earth orbits the Sun, different hemispheres tilt toward or away from the Sun.",
        "When the Northern Hemisphere tilts toward the Sun = summer in the north, winter in the south.",
        "When the Southern Hemisphere tilts toward the Sun = summer in the south, winter in the north.",
        "The equator gets direct sunlight year-round, which is why tropical areas are always warm.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "When it is summer in the US, it is winter in Australia (and vice versa)!",
        "The longest day (summer solstice) has about 15 hours of daylight.",
        "If Earth were NOT tilted, we would have no seasons - every day would be the same!"
    ])
    y = try_this(doc, y, "Shine a flashlight straight down on paper (summer), then at an angle (winter). Which is brighter?")
    y = think_about_it(doc, y, "If Earth were not tilted at all, what would life on our planet be like?")

    # Chapter 8: Weather vs Climate
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: Weather vs Climate", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "'Sunny, are weather and climate the same thing?' asked her classmate.",
        "'Great question! They are related but different!' Sunny pulled out her notebook.",
        "'Weather is what is happening RIGHT NOW outside - today's temperature and rain.'",
        "'Climate is the pattern of weather over a LONG TIME - like 30 years or more.'",
        "'Think of it this way: weather is your mood today; climate is your personality!'",
        "'And just like personality can change slowly, our climate is changing too.'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: WEATHER & CLIMATE", 'F2', 13)
    y -= 20
    science = [
        "Weather: short-term conditions (today's temperature, humidity, wind, precipitation).",
        "Climate: long-term average weather patterns in a region over 30+ years.",
        "Climate change means Earth's average temperature is slowly rising over decades.",
        "Greenhouse gases (CO2, methane) trap heat in the atmosphere like a blanket.",
        "Everyone can help: use less energy, plant trees, reduce waste, bike more!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y -= 15
    doc.add_text(margin, y, "MORAL:", 'F2', 14)
    y -= 18
    doc.add_text(margin, y, "Understanding nature helps us protect our beautiful planet!", 'F5', 13)
    y = science_fact_box(doc, y - 30, [
        "Earth's average temperature has risen about 1.1C (2F) since 1880.",
        "Ice at the North and South Poles is melting faster each decade.",
        "One tree can absorb about 48 pounds of CO2 per year. Plant more trees!"
    ])

    # Activities Page
    doc.new_page()
    doc.add_centered_text(720, "WEATHER ACTIVITIES", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    doc.add_text(margin, 680, "1. MAKE A RAIN GAUGE:", 'F2', 12)
    doc.add_text(margin + 10, 660, "Cut the top off a plastic bottle, invert it as a funnel, tape a ruler to the side.", 'F4', 10)
    doc.add_text(margin + 10, 644, "Put it outside and measure rainfall each day for a week!", 'F4', 10)
    doc.add_text(margin, 610, "2. CLOUD IDENTIFICATION CHART:", 'F2', 12)
    doc.add_text(margin + 10, 590, "Draw these cloud types: Cumulus (puffy), Stratus (flat), Cirrus (wispy)", 'F4', 10)
    doc.add_text(margin + 10, 574, "Label each one and write what weather it brings.", 'F4', 10)
    doc.add_text(margin, 540, "3. ONE-WEEK WEATHER JOURNAL:", 'F2', 12)
    y = 518
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for d in days:
        doc.add_text(margin + 10, y, d + ": Temp: ___ Cloud Type: _______ Rain: Y/N Wind: ___", 'F3', 9)
        y -= 20

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "WEATHER QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. Why is the sky blue?",
        "2. Name three types of clouds and their shapes.",
        "3. What causes thunder?",
        "4. What do hurricanes need to form?",
        "5. How many sides does every snowflake have?",
        "6. What is ROYGBIV?",
        "7. What causes the seasons to change?",
        "8. What is the difference between weather and climate?",
        "9. How can you tell how far away lightning struck?",
        "10. What are greenhouse gases?",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 26

    # Certificate Page
    doc.new_page()
    doc.add_filled_rect(50, 100, W - 100, H - 200, 0.95)
    doc.add_rect(60, 110, W - 120, H - 220, 2, 0.3)
    doc.add_centered_text(650, "WEATHER WONDERS CERTIFICATE", 'F2', 20)
    doc.add_centered_text(600, "I am a certified Weather Scientist!", 'F5', 14)
    doc.add_centered_text(550, "My favorite weather phenomenon: _________________", 'F4', 12)
    doc.add_centered_text(500, "One thing I will do to help the planet:", 'F4', 12)
    doc.add_line(150, 470, W - 150, 470, 0.5, 0.5)
    doc.add_centered_text(400, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(360, "Date: _________________", 'F4', 14)
    doc.add_centered_text(280, "Certified Weather Expert!", 'F2', 18)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book270_Weather_Wonders_Story.pdf')
    print("Book270_Weather_Wonders_Story.pdf created successfully!")

if __name__ == '__main__':
    create_book()
