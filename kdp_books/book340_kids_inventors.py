from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    inventors = [
        ("Louis Braille", "15", "France, 1824", "Reading System for the Blind",
         "Louis lost his sight in an accident at age 3. At school for the blind, he found the existing raised-letter system impossible to use. Inspired by a military night-writing code, Louis spent 2 years (ages 13-15) developing a system of 6 raised dots that could represent every letter, number, and punctuation mark. Today, Braille is used worldwide!",
         "Over 39 million blind people worldwide", "Tactile communication, pattern design, combinatorics"),
        ("Frank Epperson", "11", "USA, 1905", "The Popsicle (Ice Pop)",
         "On a cold San Francisco night, 11-year-old Frank accidentally left a cup of soda mix with a stirring stick outside. By morning, it had frozen solid around the stick! He called it an 'Epsicle.' Years later, he patented it as the Popsicle. Today, over 2 billion popsicles are sold yearly!",
         "Happy accident turned into billion-dollar industry", "Chemistry of freezing, accidental discovery, observation"),
        ("Philo Farnsworth", "14", "USA, 1920", "Electronic Television",
         "At 14, while plowing a potato field in rows, Philo had a brilliant idea: what if you could transmit images in rows of light, line by line? He sketched his concept for his high school teacher. By 21, he demonstrated the first fully electronic television. His Idaho potato field inspiration changed entertainment forever!",
         "Television exists in 1.7 billion households worldwide", "Electron beams, cathode rays, image scanning"),
        ("Gitanjali Rao", "11", "USA, 2017", "Lead Water Contamination Detector",
         "After watching news about the Flint, Michigan water crisis, 11-year-old Gitanjali was determined to help. She invented a device called Tethys that detects lead in water faster and cheaper than existing methods. Using carbon nanotube sensors connected to a smartphone app, her invention can test water in seconds!",
         "37 million Americans are served by water systems with lead violations", "Nanotechnology, sensor design, app development"),
        ("Jack Andraka", "15", "USA, 2012", "Pancreatic Cancer Test",
         "After losing a family friend to pancreatic cancer, 15-year-old Jack researched why the disease is so deadly (usually detected too late). He invented a paper sensor that detects pancreatic cancer 168 times faster, 26,000 times cheaper, and 400 times more sensitive than existing tests. He was rejected by 197 labs before one said yes!",
         "Could save thousands of lives through early detection", "Bioengineering, carbon nanotubes, protein markers"),
        ("Kelvin Doe", "13", "Sierra Leone, 2012", "Generator & Radio Station from Trash",
         "In a country with severe electricity problems, 13-year-old Kelvin built a generator from discarded electronics found in trash bins. He then built his own radio station to broadcast music and news in his community! He became the youngest person invited to visit MIT's engineering program.",
         "Provided electricity and media to his entire community", "Electrical engineering, resourcefulness, circuit design"),
        ("Param Jaggi", "14", "USA, 2011", "Device to Convert CO2 to Oxygen",
         "Concerned about car emissions, 14-year-old Param invented a device that attaches to car tailpipes and uses algae to convert carbon dioxide into oxygen through photosynthesis. His Algae Mobile device showed that young people can tackle even the biggest environmental challenges.",
         "Cars produce 4.6 metric tons of CO2 per year each", "Photosynthesis, algae biology, emission reduction"),
        ("Elif Bilgin", "16", "Turkey, 2013", "Bioplastic from Banana Peels",
         "Elif spent 2 years experimenting to create a bioplastic from banana peels as an alternative to petroleum-based plastics. After many failed attempts, she succeeded in creating a material that could replace some traditional plastics. Her persistence through failure is as inspiring as her invention!",
         "World uses 380 million tons of plastic per year", "Polymer chemistry, sustainable materials, perseverance"),
        ("Kenneth Shinozuka", "15", "USA, 2014", "Wearable Sensor for Alzheimer's Patients",
         "After his grandfather with Alzheimer's wandered from home, Kenneth invented a wearable sensor that alerts caregivers when patients get out of bed. The pressure sensor in a sock sends Bluetooth alerts to a smartphone. Simple, affordable, and life-saving for millions of families dealing with Alzheimer's.",
         "Over 6 million Americans have Alzheimer's disease", "Sensors, Bluetooth, app development, user-centered design"),
        ("Hannah Herbst", "15", "USA, 2015", "Ocean Energy Harvesting Device",
         "Hannah's pen pal in Ethiopia lived without electricity. Inspired to help, Hannah invented BEACON: a device that harvests energy from ocean currents to power small devices and provide light. Using a 3D-printed propeller and generator, her prototype proved the concept of accessible ocean energy.",
         "940 million people worldwide lack access to electricity", "Renewable energy, fluid dynamics, 3D printing"),
        ("Mikaila Ulmer", "9", "USA, 2009", "Me & the Bees Lemonade",
         "After being stung by a bee twice in one week, 9-year-old Mikaila didn't get angry - she got curious! She learned about the importance of bees and their decline. She started a lemonade company using her grandmother's recipe with honey, donating a percentage to save bees. She got a $60K deal on Shark Tank at age 11!",
         "Bees pollinate 75% of flowering plants and 35% of food crops", "Entrepreneurship, environmental conservation, business"),
        ("Cassidy Goldstein", "12", "USA, 2003", "Unbreakable Crayon Holder",
         "Frustrated that her crayons kept breaking (especially the small pieces too tiny to hold), 12-year-old Cassidy invented a plastic tube holder that grips broken crayon pieces, allowing them to be used until completely finished. She patented her invention and it sold in stores!",
         "Reduces waste - no more thrown-away broken crayons", "Product design, patents, problem observation"),
        ("Ann Makosinski", "15", "Canada, 2013", "Body-Heat Powered Flashlight",
         "When Ann learned her friend in the Philippines couldn't study at night due to no electricity, she invented a flashlight powered only by body heat! Using Peltier tiles that convert temperature difference into electricity, her 'Hollow Flashlight' needs no batteries or charging. Just hold it!",
         "Design for people without access to electricity or batteries", "Thermoelectric effect, energy conversion, humanitarian design"),
        ("Ryan Patterson", "17", "USA, 2001", "Sign Language Translator Glove",
         "Ryan invented a glove embedded with sensors that translates American Sign Language finger-spelling into text displayed on a screen. Each finger movement is detected and matched to a letter, enabling deaf individuals to communicate more easily with hearing people who don't know sign language.",
         "Over 500,000 people use ASL in North America", "Sensors, pattern recognition, assistive technology"),
        ("Moziah Bridges", "9", "USA, 2011", "Mo's Bows - Handmade Bow Ties",
         "When 9-year-old Mo couldn't find bow ties he liked, he taught himself to sew using YouTube and his grandmother's guidance. He started selling handmade bow ties and built a million-dollar business by age 15! He appeared on Shark Tank and was mentored by Daymond John.",
         "Youth entrepreneurship proves age is not a barrier", "Fashion design, entrepreneurship, self-teaching"),
        ("Keiana Cave", "16", "USA, 2014", "Chemical Test for Environmental Pollution",
         "Keiana developed a method to detect cancer-causing compounds in water from industrial contamination. Her research helped identify pollution in her New Orleans community that was making people sick. She proved that young scientists can contribute to environmental justice.",
         "Environmental pollution causes 12.6 million deaths per year globally", "Analytical chemistry, environmental science, activism"),
        ("Taylor Wilson", "14", "USA, 2008", "Nuclear Fusion Reactor",
         "Taylor became the youngest person ever to build a working nuclear fusion reactor at age 14! His device smashes atoms together, demonstrating the same process that powers the Sun. He went on to develop nuclear detection technology for national security.",
         "Youngest nuclear scientist in history", "Nuclear physics, fusion, plasma physics, radiation"),
        ("Tripp Phillips", "8", "USA, 2014", "Le-Glue (Temporary Lego Adhesive)",
         "Tired of his LEGO creations falling apart, 8-year-old Tripp invented Le-Glue: a non-toxic, water-soluble adhesive that holds LEGO bricks together but dissolves with water when you want to take them apart. His product has sold over a million units!",
         "Solves a problem every LEGO builder has experienced", "Chemistry, product development, market identification"),
        ("Kiara Nirghin", "16", "South Africa, 2016", "Super Absorbent Material for Drought",
         "During South Africa's worst drought in decades, Kiara invented a low-cost super absorbent polymer made from orange peels and avocado skins. Placed in soil, it retains hundreds of times its weight in water, reducing irrigation needs by up to 73% and helping farmers survive drought.",
         "Agriculture uses 70% of global freshwater; droughts are increasing", "Polymer science, agriculture, waste utilization"),
        ("Bishop Curry V", "10", "USA, 2016", "Oasis - Device to Prevent Hot Car Deaths",
         "After hearing about a baby who died in a hot car, 10-year-old Bishop invented Oasis: a device that monitors temperature inside cars and sends alerts to parents' phones. It can also activate cooling fans when temperatures rise dangerously. His empathy-driven innovation could save lives.",
         "Average of 38 children die from hot cars per year in the US", "Temperature sensors, IoT, alerts, safety engineering"),
    ]

    title_page(doc, "YOUNG INVENTORS WHO CHANGED THE WORLD", "20 True Stories of Kids Like You (Ages 8-14)", "20 Inventor Stories * Science * Your Turn Challenges * Worksheets")
    copyright_page(doc, "YOUNG INVENTORS WHO CHANGED THE WORLD")
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0)
    doc.add_line(180, 710, 432, 710, 1, 0.3)
    y = 685
    for i, (name, age, _, invention, _, _, _) in enumerate(inventors):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "TABLE OF CONTENTS (cont.)", 'F2', 16, 0)
            y = 690
        doc.add_text(72, y, f"{i+1}. {name} (age {age}) - {invention}", 'F4', 10, 0.2)
        y -= 20
    doc.new_page()

    for idx, (name, age, place, invention, story, impact, science) in enumerate(inventors):
        # Story page
        doc.add_text(72, 730, f"INVENTOR #{idx+1}", 'F1', 10, 0.4)
        doc.add_text(72, 710, f"{name}", 'F2', 20, 0)
        doc.add_text(72, 685, f"Age: {age} | {place}", 'F1', 11, 0.3)
        doc.add_text(72, 668, f"Invention: {invention}", 'F2', 12, 0.1)
        doc.add_line(72, 660, 450, 660, 1, 0.3)
        
        y = 640
        doc.add_text(72, y, "THE STORY:", 'F2', 12, 0.1)
        y -= 18
        y = add_wrapped(doc, 72, y, story, 'F4', 11, 0.2)
        
        y -= 20
        doc.add_text(72, y, "IMPACT:", 'F2', 11, 0.1)
        y -= 18
        y = add_wrapped(doc, 90, y, impact, 'F1', 10, 0.3)
        
        y -= 15
        doc.add_text(72, y, "THE SCIENCE:", 'F2', 11, 0.1)
        y -= 18
        doc.add_text(90, y, science, 'F3', 9, 0.3)
        doc.new_page()

        # Your Turn page
        doc.add_centered_text(720, f"YOUR TURN: INVENTOR #{idx+1}", 'F2', 16, 0)
        doc.add_text(72, 690, "INVENTION CHALLENGE:", 'F2', 12, 0.1)
        challenges = [
            "Design a new way to help people with a disability.",
            "What everyday item could you improve with a simple change?",
            "Invent something using only items from your recycling bin.",
            "Design a device that detects something harmful in the environment.",
            "Create a faster or cheaper way to test for a health problem.",
            "Build something useful from items others have thrown away.",
            "Design an invention that helps the environment using nature.",
            "Create a useful material from food waste.",
            "Invent a device that helps elderly or sick people stay safe.",
            "Design something that harvests energy from an unusual source.",
            "Start a kid business that solves a problem AND helps the world.",
            "Improve an everyday item that frustrates you.",
            "Invent something powered by a surprising energy source.",
            "Design a device that helps people communicate better.",
            "Create a product from a skill you taught yourself.",
            "Invent something that detects pollution or harmful substances.",
            "Design an experiment that demonstrates a physics concept.",
            "Solve a problem that every kid you know experiences.",
            "Invent something that uses food/plant waste productively.",
            "Design a safety device that protects children.",
        ]
        y = add_wrapped(doc, 90, 670, challenges[idx], 'F4', 11, 0.2)
        
        y -= 20
        doc.add_text(72, y, "MY INVENTION IDEA:", 'F2', 12, 0.1)
        y -= 18
        doc.add_text(90, y, "Problem I want to solve: ________________________________________", 'F1', 10, 0.4)
        y -= 18
        doc.add_text(90, y, "My solution: ____________________________________________________", 'F1', 10, 0.4)
        y -= 18
        doc.add_text(90, y, "Materials needed: _______________________________________________", 'F1', 10, 0.4)
        y -= 18
        doc.add_text(90, y, "How it works: ___________________________________________________", 'F1', 10, 0.4)
        y -= 18
        doc.add_text(90, y, "Who would use it: _______________________________________________", 'F1', 10, 0.4)
        
        y -= 25
        doc.add_text(72, y, "SKETCH YOUR INVENTION:", 'F2', 11, 0.1)
        doc.add_rect(72, y - 200, 468, 190, 1, 0.5)
        doc.new_page()

    # Scientific Method guide
    doc.add_centered_text(720, "THE SCIENTIFIC METHOD", 'F2', 18, 0)
    steps = ["1. OBSERVE - Notice a problem or ask a question","2. RESEARCH - Learn what's already been tried","3. HYPOTHESIZE - Predict a possible solution","4. EXPERIMENT - Test your idea","5. ANALYZE - Study your results","6. CONCLUDE - Did it work? What did you learn?","7. SHARE - Tell others about your discovery!"]
    y = 680
    for s in steps:
        doc.add_text(72, y, s, 'F1', 13, 0.2)
        y -= 35
    doc.new_page()

    # Invention Worksheet
    doc.add_centered_text(720, "MY INVENTION WORKSHEET", 'F2', 18, 0)
    fields = ["Inventor name: ","Problem to solve: ","Who has this problem: ","My solution idea: ","Materials needed: ","How it works (explain): ","How to test it: ","Expected result: "]
    y = 680
    for f in fields:
        doc.add_text(72, y, f"{f}______________________________________________", 'F1', 11, 0.3)
        y -= 35
    doc.new_page()

    certificate(doc, "YOUNG INVENTOR CERTIFICATE")
    add_supplemental(doc, 'Inventors', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book340_Kids_Inventors_Stories.pdf')
    print("Book340_Kids_Inventors_Stories.pdf created successfully!")

if __name__ == "__main__":
    create_book()
