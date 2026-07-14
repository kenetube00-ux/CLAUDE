"""Book 274: KIDS WHO CHANGED THE WORLD - True Stories of Young Inventors (Ages 8-14)"""
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
    doc.add_filled_rect(0, 0, W, H, 0.08)
    doc.add_centered_text(660, "KIDS WHO CHANGED", 'F2', 26, 1)
    doc.add_centered_text(628, "THE WORLD", 'F2', 28, 1)
    doc.add_centered_text(590, "True Stories of Young Inventors", 'F5', 16, 0.9)
    doc.add_centered_text(560, "Ages 8-14", 'F4', 14, 0.8)
    doc.add_centered_text(490, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
    doc.add_centered_text(460, "Science Story Series - Book 9", 'F4', 12, 0.7)
    doc.add_centered_text(350, "You are NEVER too young to change the world!", 'F4', 13, 0.8)
    doc.add_centered_text(325, "These kids proved it.", 'F4', 13, 0.8)
    doc.add_centered_text(100, "Educational Content | Real Science | Inspiring True Stories", 'F1', 10, 0.7)

    # Copyright
    doc.new_page()
    doc.add_centered_text(650, "KIDS WHO CHANGED THE WORLD", 'F2', 16)
    doc.add_text(margin, 600, "Author: Daniel Tesfamariam", 'F4', 11)
    doc.add_text(margin, 580, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", 'F4', 10)
    doc.add_text(margin, 560, "No part of this publication may be reproduced without permission.", 'F4', 10)
    doc.add_text(margin, 530, "For ages 8-14. Inspiring true stories of young inventors and scientists.", 'F4', 10)
    doc.add_text(margin, 500, "First Edition, 2025", 'F4', 10)

    # TOC
    doc.new_page()
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    chapters = [
        "Chapter 1: Louis Braille (age 15) - Reading by Touch",
        "Chapter 2: Philo Farnsworth (age 14) - The Television Idea",
        "Chapter 3: Frank Epperson (age 11) - The Popsicle",
        "Chapter 4: Param Jaggi (age 14) - Cleaning the Air",
        "Chapter 5: Gitanjali Rao (age 11) - Detecting Lead in Water",
        "Chapter 6: Jack Andraka (age 15) - Cancer Detection",
        "Chapter 7: Kelvin Doe (age 13) - Battery from Trash",
        "Chapter 8: YOUR Turn!",
    ]
    y = 670
    for ch in chapters:
        doc.add_text(margin, y, ch, 'F4', 12)
        y -= 30

    # Chapter 1: Louis Braille
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: Louis Braille", 'F2', 20)
    doc.add_centered_text(698, "Age 15 - Invented Braille Reading System", 'F4', 12, 0.4)
    doc.add_line(margin, 688, W - margin, 688, 1, 0.5)
    story = [
        "Louis Braille lost his sight in an accident when he was only 3 years old.",
        "In 1800s France, blind people had almost no way to read or write.",
        "At school for the blind, Louis was frustrated. The raised-letter books were clumsy.",
        "At age 15, he invented a system of raised dots that could represent any letter!",
        "Using just 6 dots in different patterns, he created an entire alphabet for the blind.",
        "Today, millions of blind people worldwide read using Braille's brilliant system.",
    ]
    y = text_block(doc, story, 660)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: HOW TOUCH AND NERVES WORK", 'F2', 13)
    y -= 20
    science = [
        "Your fingertips have about 3,000 touch receptors per square centimeter!",
        "These receptors detect pressure, vibration, and texture with incredible sensitivity.",
        "Nerve signals from your fingertips travel to your brain at up to 250 mph!",
        "Your brain can distinguish bumps as small as 0.04mm - smaller than a grain of sand!",
        "Blind people often develop even more sensitive touch as their brain adapts.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Braille uses patterns of 1-6 raised dots that represent letters, numbers, and punctuation.",
        "Experienced Braille readers can read up to 200 words per minute by touch!",
        "Braille is used in over 130 languages worldwide today."
    ])
    y = try_this(doc, y, "Close your eyes and try to identify 5 objects by touch alone. How sensitive are your fingers?")
    y = think_about_it(doc, y, "How does losing one sense (like sight) make other senses (like touch) stronger?")

    # Chapter 2: Philo Farnsworth
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: Philo Farnsworth", 'F2', 20)
    doc.add_centered_text(698, "Age 14 - Conceived the Idea for Television", 'F4', 12, 0.4)
    doc.add_line(margin, 688, W - margin, 688, 1, 0.5)
    story = [
        "In 1920, 14-year-old Philo was plowing a potato field in Idaho.",
        "Looking at the parallel rows of soil, he had a brilliant idea!",
        "'What if you could capture an image line by line, like rows in a field?'",
        "He sketched his idea for his high school teacher: electronic television!",
        "By age 21, he built the first fully electronic TV and transmitted an image.",
        "His idea from a potato field changed how the entire world receives information!",
    ]
    y = text_block(doc, story, 660)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: HOW SCREENS CREATE IMAGES", 'F2', 13)
    y -= 20
    science = [
        "TV screens create images using thousands of tiny pixels (picture elements).",
        "Each pixel produces light in combinations of red, green, and blue (RGB).",
        "By mixing different amounts of these three colors, ANY color can be created!",
        "Your screen refreshes 30-60 times per second - too fast for your eyes to notice!",
        "Farnsworth's original idea used an electron beam scanning line by line (CRT technology).",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "A 4K TV has over 8 million pixels, each with 3 sub-pixels (24+ million tiny lights!).",
        "Farnsworth first demonstrated TV at age 21 with a simple straight line image.",
        "He said he hoped TV would be used for education - 'There is nothing worthwhile on it.'"
    ])
    y = try_this(doc, y, "Look at a screen with a magnifying glass. Can you see the tiny red, green, and blue sub-pixels?")
    y = think_about_it(doc, y, "How did looking at rows in a potato field inspire the biggest invention of the century?")

    # Chapter 3: Frank Epperson
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: Frank Epperson", 'F2', 20)
    doc.add_centered_text(698, "Age 11 - Accidentally Invented the Popsicle", 'F4', 12, 0.4)
    doc.add_line(margin, 688, W - margin, 688, 1, 0.5)
    story = [
        "In 1905, 11-year-old Frank was mixing powdered soda and water on his porch.",
        "He accidentally left the cup outside overnight with the mixing stick still in it.",
        "That night, the temperature dropped below freezing in San Francisco.",
        "The next morning, Frank found his drink frozen solid around the stick!",
        "He pulled it out and had the world's first popsicle! He called it the 'Epsicle.'",
        "Years later, he patented it and sold millions. All from a happy accident!",
    ]
    y = text_block(doc, story, 660)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: FREEZING AND SOLUTIONS", 'F2', 13)
    y -= 20
    science = [
        "Pure water freezes at 32F (0C), but dissolved substances lower the freezing point!",
        "That is why Frank's sugary soda water froze at a lower temperature than plain water.",
        "This is called 'freezing point depression' - salt on icy roads uses the same principle!",
        "When water freezes, molecules slow down and form a crystal structure (ice).",
        "Adding sugar or salt disrupts crystal formation, requiring colder temperatures to freeze.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Americans eat over 2 billion popsicles every year!",
        "Ocean water freezes at about 28.4F (-2C) because of dissolved salt.",
        "Ice cream trucks exist because Frank's 'accident' created a whole new industry!"
    ])
    y = try_this(doc, y, "Make popsicles! Freeze juice in cups with sticks. Try salt water vs sugar water - which freezes first?")
    y = think_about_it(doc, y, "Many great inventions were accidents. Why is being observant so important for scientists?")

    # Chapter 4: Param Jaggi
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: Param Jaggi", 'F2', 20)
    doc.add_centered_text(698, "Age 14 - Invented a CO2 Filter for Cars", 'F4', 12, 0.4)
    doc.add_line(margin, 688, W - margin, 688, 1, 0.5)
    story = [
        "At 14, Param Jaggi was concerned about car exhaust polluting the air.",
        "He knew that plants convert CO2 into oxygen through photosynthesis.",
        "'What if I could make a device that does what plants do?' he wondered.",
        "He created a device that attaches to car exhaust pipes and uses algae to absorb CO2!",
        "The algae use the CO2 for photosynthesis, converting it to oxygen before it leaves.",
        "His invention won numerous science awards and inspired other young inventors.",
    ]
    y = text_block(doc, story, 660)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: AIR PURIFICATION", 'F2', 13)
    y -= 20
    science = [
        "Cars produce CO2 when they burn gasoline - a greenhouse gas that warms our planet.",
        "Photosynthesis: plants/algae use CO2 + sunlight + water to make sugar + oxygen.",
        "Algae are incredibly efficient at photosynthesis - even better than trees per volume!",
        "Carbon capture means removing CO2 from the air or exhaust before it enters atmosphere.",
        "Engineers are developing many ways to capture carbon: algae, minerals, and technology.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "A single car produces about 4.6 metric tons of CO2 per year!",
        "Algae can double their population in just hours - incredibly fast growers.",
        "Trees absorb CO2 but algae can be 10-50 times more efficient per unit area!"
    ])
    y = try_this(doc, y, "Grow algae! Put pond water in a clear jar in sunlight. In days, green algae will multiply!")
    y = think_about_it(doc, y, "What everyday problems around you could be solved with a creative invention?")

    # Chapter 5: Gitanjali Rao
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: Gitanjali Rao", 'F2', 20)
    doc.add_centered_text(698, "Age 11 - Created a Lead Detection Device", 'F4', 12, 0.4)
    doc.add_line(margin, 688, W - margin, 688, 1, 0.5)
    story = [
        "When 11-year-old Gitanjali saw news about the Flint, Michigan water crisis,",
        "she was shocked that families were drinking lead-contaminated water without knowing.",
        "'Testing for lead is expensive and slow,' she learned. 'I want to change that!'",
        "She invented 'Tethys' - a device that detects lead in water quickly and cheaply.",
        "It uses carbon nanotube sensors that change when lead atoms attach to them.",
        "In 2017, she won the Discovery Education 3M Young Scientist Challenge!",
    ]
    y = text_block(doc, story, 660)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: WATER CONTAMINATION", 'F2', 13)
    y -= 20
    science = [
        "Lead is a toxic metal that can damage the brain, especially in children.",
        "Old lead pipes can leach lead into drinking water - invisible and tasteless!",
        "Standard lead tests take days and cost hundreds of dollars. Gitanjali's device: seconds!",
        "Carbon nanotubes are tiny tubes of carbon atoms - incredibly sensitive chemical sensors.",
        "The sensor changes electrical resistance when lead atoms bond to it - detectable by a phone!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Even tiny amounts of lead (parts per billion) can harm developing brains.",
        "Gitanjali was named TIME Magazine's first-ever 'Kid of the Year' in 2020!",
        "She has since created apps to fight cyberbullying and detect other contaminants."
    ])
    y = try_this(doc, y, "Research your local water quality report. What gets tested? Are there any concerns?")
    y = think_about_it(doc, y, "What problems in your community could technology help solve?")

    # Chapter 6: Jack Andraka
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: Jack Andraka", 'F2', 20)
    doc.add_centered_text(698, "Age 15 - Developed a Low-Cost Cancer Test", 'F4', 12, 0.4)
    doc.add_line(margin, 688, W - margin, 688, 1, 0.5)
    story = [
        "When a close family friend died of pancreatic cancer, 15-year-old Jack was devastated.",
        "He learned that the existing test was 60 years old, expensive, and missed 70% of cases!",
        "'I can do better,' he decided. He spent months researching at the library and online.",
        "He developed a paper sensor that detects a cancer protein 168 times faster!",
        "His test costs just 3 cents (vs $800!) and takes 5 minutes (vs hours!).",
        "After being rejected by 197 labs, one professor said yes - and Jack proved it worked!",
    ]
    y = text_block(doc, story, 660)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: BIOSENSORS", 'F2', 13)
    y -= 20
    science = [
        "Biosensors detect biological substances (proteins, DNA) using chemical reactions.",
        "Jack's sensor uses antibodies that bind specifically to a cancer protein (mesothelin).",
        "When the protein attaches to antibodies on the paper, electrical properties change.",
        "Carbon nanotubes on filter paper create a network that responds to the protein binding.",
        "This is similar to how COVID rapid tests work - antibodies detecting specific targets!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Jack was rejected by 197 researchers before finding one who believed in his idea!",
        "His test is 26,000 times less expensive and 400 times more sensitive than existing tests.",
        "Persistence paid off - he never gave up despite nearly 200 rejections!"
    ])
    y = try_this(doc, y, "Research 'antibodies' - how do they recognize specific things? Draw how a lock-and-key system works.")
    y = think_about_it(doc, y, "Jack was rejected 197 times before succeeding. What does this teach about persistence?")

    # Chapter 7: Kelvin Doe
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: Kelvin Doe", 'F2', 20)
    doc.add_centered_text(698, "Age 13 - Built Batteries and a Radio from Trash", 'F4', 12, 0.4)
    doc.add_line(margin, 688, W - margin, 688, 1, 0.5)
    story = [
        "In Sierra Leone, Africa, 13-year-old Kelvin had no access to electronics or electricity.",
        "But he was endlessly curious and loved taking things apart to see how they worked.",
        "He collected discarded electronics and scrap metal from trash dumps.",
        "From this 'junk,' he built batteries, a generator, and eventually a radio station!",
        "His community radio station broadcast music and news to his whole neighborhood.",
        "He became the youngest person ever invited to MIT's 'Visiting Practitioner' program!",
    ]
    y = text_block(doc, story, 660)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: BATTERIES FROM RECYCLED MATERIALS", 'F2', 13)
    y -= 20
    science = [
        "Kelvin made batteries by combining acid, soda, and metal from recycled electronics.",
        "A battery needs two different metals and an electrolyte (acid/base solution).",
        "Chemical reactions between the metals and electrolyte produce an electrical current.",
        "His generator used a motor in reverse: spinning it by hand produced electricity!",
        "Radio transmitters convert electrical signals into electromagnetic waves.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Kelvin had no formal engineering training - he taught himself from discarded textbooks!",
        "He created his own radio station: 'DJ Focus' broadcasting to his community.",
        "He later started a company to bring power to communities without electricity."
    ])
    y = try_this(doc, y, "Build a simple battery: put copper and zinc strips in lemon juice. Measure voltage with a multimeter!")
    y = think_about_it(doc, y, "How does Kelvin's story show that creativity is more important than resources?")

    # Chapter 8: YOUR Turn!
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: YOUR Turn!", 'F2', 20)
    doc.add_centered_text(698, "The Next Great Inventor Could Be YOU!", 'F4', 12, 0.4)
    doc.add_line(margin, 688, W - margin, 688, 1, 0.5)
    story = [
        "Every inventor in this book was once just a kid with a question or a problem.",
        "They did not have special powers or expensive labs. They had CURIOSITY and PERSISTENCE.",
        "Louis was blind. Kelvin had no electricity. Jack was rejected 197 times.",
        "But they all shared one thing: they saw a problem and decided to solve it.",
        "The world has millions of problems still waiting for creative solutions.",
        "And the next great inventor might be reading this book right now. That means YOU!",
    ]
    y = text_block(doc, story, 660)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: THE SCIENTIFIC METHOD", 'F2', 13)
    y -= 20
    science = [
        "Step 1: OBSERVE - Notice a problem that needs solving.",
        "Step 2: QUESTION - Ask 'Why does this happen?' or 'How can I fix this?'",
        "Step 3: RESEARCH - Learn everything you can about the problem.",
        "Step 4: HYPOTHESIZE - Make an educated guess about a solution.",
        "Step 5: EXPERIMENT - Build a prototype and test your idea.",
        "Step 6: ANALYZE - Did it work? What can you improve?",
        "Step 7: SHARE - Tell others about your findings!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y -= 15
    doc.add_text(margin, y, "MORAL:", 'F2', 14)
    y -= 18
    doc.add_text(margin, y, "You are never too young to change the world with science!", 'F5', 13)
    y = science_fact_box(doc, y - 30, [
        "The average age of a first patent in the US is getting younger every decade!",
        "Many of the world's biggest companies were started by teenagers in garages.",
        "Every problem you notice is an opportunity for an invention!"
    ])

    # Invention Worksheet
    doc.new_page()
    doc.add_centered_text(720, "MY INVENTION WORKSHEET", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    doc.add_text(margin, 680, "1. THE PROBLEM I want to solve:", 'F2', 12)
    doc.add_line(margin, 660, W - margin, 660, 0.5, 0.5)
    doc.add_line(margin, 640, W - margin, 640, 0.5, 0.5)
    doc.add_text(margin, 610, "2. WHO has this problem?", 'F2', 12)
    doc.add_line(margin, 590, W - margin, 590, 0.5, 0.5)
    doc.add_text(margin, 560, "3. MY SOLUTION idea:", 'F2', 12)
    doc.add_line(margin, 540, W - margin, 540, 0.5, 0.5)
    doc.add_line(margin, 520, W - margin, 520, 0.5, 0.5)
    doc.add_text(margin, 490, "4. MATERIALS I would need:", 'F2', 12)
    doc.add_line(margin, 470, W - margin, 470, 0.5, 0.5)
    doc.add_text(margin, 440, "5. How would I TEST it?", 'F2', 12)
    doc.add_line(margin, 420, W - margin, 420, 0.5, 0.5)
    doc.add_text(margin, 390, "6. DRAW your invention here:", 'F2', 12)
    doc.add_rect(margin, 150, W - 2*margin, 230, 1, 0.5)

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "INVENTOR'S QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. What did Louis Braille invent and why?",
        "2. What inspired Philo Farnsworth's TV idea?",
        "3. How was the popsicle invented accidentally?",
        "4. How does Param Jaggi's CO2 filter work?",
        "5. What problem did Gitanjali Rao solve?",
        "6. How many times was Jack Andraka rejected before success?",
        "7. What did Kelvin Doe build from trash?",
        "8. List the steps of the scientific method.",
        "9. What do all these young inventors have in common?",
        "10. What problem would YOU like to solve?",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 26

    # Certificate
    doc.new_page()
    doc.add_filled_rect(50, 100, W - 100, H - 200, 0.95)
    doc.add_rect(60, 110, W - 120, H - 220, 2, 0.3)
    doc.add_centered_text(650, "FUTURE INVENTOR CERTIFICATE", 'F2', 20)
    doc.add_centered_text(600, "I am inspired to change the world!", 'F5', 14)
    doc.add_centered_text(555, "The inventor who inspired me most: _______________", 'F4', 12)
    doc.add_centered_text(515, "My invention idea: ______________________________", 'F4', 12)
    doc.add_centered_text(475, "The problem it solves: ___________________________", 'F4', 12)
    doc.add_centered_text(400, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(360, "Date: _________________", 'F4', 14)
    doc.add_centered_text(290, "Future World-Changer!", 'F2', 18)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book274_Kid_Inventors_Story.pdf')
    print("Book274_Kid_Inventors_Story.pdf created successfully!")

if __name__ == '__main__':
    create_book()
