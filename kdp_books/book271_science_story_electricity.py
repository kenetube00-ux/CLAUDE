"""Book 271: THE SPARK THAT CHANGED EVERYTHING - A Science Story About Electricity (Ages 8-13)"""
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
    doc.add_centered_text(660, "THE SPARK THAT", 'F2', 26, 1)
    doc.add_centered_text(628, "CHANGED EVERYTHING", 'F2', 26, 1)
    doc.add_centered_text(590, "A Science Story About Electricity", 'F5', 16, 0.9)
    doc.add_centered_text(560, "Ages 8-13", 'F4', 14, 0.8)
    doc.add_centered_text(490, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
    doc.add_centered_text(460, "Science Story Series - Book 6", 'F4', 12, 0.7)
    doc.add_centered_text(350, "Discover the invisible force that", 'F4', 13, 0.8)
    doc.add_centered_text(325, "powers our entire modern world!", 'F4', 13, 0.8)
    doc.add_centered_text(100, "Educational Content | Real Science | Amazing Stories", 'F1', 10, 0.7)

    # Copyright
    doc.new_page()
    doc.add_centered_text(650, "THE SPARK THAT CHANGED EVERYTHING", 'F2', 14)
    doc.add_text(margin, 600, "Author: Daniel Tesfamariam", 'F4', 11)
    doc.add_text(margin, 580, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", 'F4', 10)
    doc.add_text(margin, 560, "No part of this publication may be reproduced without permission.", 'F4', 10)
    doc.add_text(margin, 530, "For ages 8-13. Scientific concepts simplified for young readers.", 'F4', 10)
    doc.add_text(margin, 500, "First Edition, 2025", 'F4', 10)
    doc.add_text(margin, 460, "SAFETY NOTE: Never experiment with electricity from wall outlets!", 'F2', 10)
    doc.add_text(margin, 440, "Only use batteries for the experiments in this book.", 'F4', 10)

    # TOC
    doc.new_page()
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    chapters = [
        "Chapter 1: Lights Out!",
        "Chapter 2: Benjamin's Kite",
        "Chapter 3: The Circuit Path",
        "Chapter 4: Battery Power",
        "Chapter 5: Magnets and Motors",
        "Chapter 6: The Power Plant",
        "Chapter 7: Saving Energy",
        "Chapter 8: Lights On!",
    ]
    y = 670
    for ch in chapters:
        doc.add_text(margin, y, ch, 'F4', 13)
        y -= 30

    # Chapter 1: Lights Out!
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: Lights Out!", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "It was a normal Tuesday evening when suddenly - everything went dark.",
        "The lights, the TV, the computer, the refrigerator - all silent. A blackout!",
        "Zara sat in the darkness, amazed at how quiet everything was without electricity.",
        "'We depend on electricity for EVERYTHING!' she realized, lighting a candle.",
        "No phone charging, no microwave, no hot water, no internet!",
        "'I never thought about where electricity comes from,' Zara whispered. 'Until now.'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: WHAT IS ELECTRICITY?", 'F2', 13)
    y -= 20
    science = [
        "Electricity is the flow of tiny particles called electrons through a material.",
        "Electrons are incredibly tiny - part of every atom in the universe.",
        "When electrons flow in the same direction, we call it electric current.",
        "Electric current is measured in amperes (amps) - like measuring water flow.",
        "Voltage is the 'push' that makes electrons flow (like water pressure in a pipe).",
        "Electricity moves at nearly the speed of light - 186,000 miles per second!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The average home uses about 30 kilowatt-hours of electricity per day.",
        "Electricity was not 'invented' - it is a natural force. We learned to harness it!",
        "Electric eels can produce up to 860 volts - enough to stun a horse!"
    ])
    y = try_this(doc, y, "List everything in your home that uses electricity. How many items can you count?")
    y = think_about_it(doc, y, "What would life be like if electricity had never been harnessed?")

    # Chapter 2: Benjamin's Kite
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: Benjamin's Kite", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "By candlelight, Zara opened a book about the history of electricity.",
        "'In 1752, Benjamin Franklin flew a kite in a thunderstorm!' she read.",
        "He attached a metal key to the kite string and waited for lightning.",
        "When lightning hit nearby, electricity traveled down the wet string to the key!",
        "A spark jumped from the key - proving that lightning IS electricity!",
        "'That was incredibly dangerous,' Zara noted, 'but it changed science forever!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: STATIC vs CURRENT ELECTRICITY", 'F2', 13)
    y -= 20
    science = [
        "Static electricity: charges build up on a surface (like rubbing a balloon on hair).",
        "Current electricity: charges flow continuously through a conductor (like in wires).",
        "Lightning is static electricity on a massive scale - billions of volts!",
        "Static builds up from friction - electrons transfer from one material to another.",
        "Current electricity is what powers our homes - a steady flow of electrons in wires.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "A lightning bolt carries about 300 million volts and 30,000 amps!",
        "Static electricity is why you get shocked touching a doorknob in winter.",
        "Ben Franklin also invented the lightning rod to protect buildings."
    ])
    y = try_this(doc, y, "Rub a balloon on your hair, then hold it near small paper bits. Watch them jump! That is static!")
    y = think_about_it(doc, y, "Why do you get more static shocks in winter than in summer?")

    # Chapter 3: The Circuit Path
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: The Circuit Path", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The next day (power still out), Zara found a flashlight with batteries.",
        "She took it apart carefully. 'Battery, wires, switch, bulb,' she listed.",
        "'It is a circuit! Electricity flows in a complete loop from the battery.'",
        "She noticed when she broke the loop (turned off the switch), the light went out.",
        "'The electricity needs a complete path to flow! No gaps allowed!'",
        "She experimented - a paper clip completed the circuit; paper did not. Fascinating!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: CIRCUITS", 'F2', 13)
    y -= 20
    science = [
        "A circuit is a complete path for electricity to flow through.",
        "Every circuit needs: a power source, a conductor (wire), and a load (like a bulb).",
        "Conductors let electricity flow easily: metals like copper, gold, aluminum.",
        "Insulators block electricity: rubber, plastic, glass, wood.",
        "A switch opens or closes the circuit - when open, electricity cannot flow.",
        "If there is ANY break in the circuit, electricity stops flowing completely!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Copper is used in most wiring because it conducts electricity very well and is affordable.",
        "Your body is a conductor! That is why you can get an electric shock (be careful!).",
        "Series circuits have one path; parallel circuits have multiple paths for electricity."
    ])
    y = try_this(doc, y, "Connect a battery to a small LED bulb with two wires. You built a circuit! Add a switch (paper clip).")
    y = think_about_it(doc, y, "Why are electrical wires covered in plastic or rubber?")

    # Chapter 4: Battery Power
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: Battery Power", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Zara was curious about the batteries in her flashlight. How do they work?",
        "'A battery stores chemical energy and converts it to electrical energy!'",
        "She read that inside are chemicals that react, pushing electrons through the wire.",
        "'The positive end (+) pulls electrons in, and the negative end (-) pushes them out.'",
        "'When the chemicals are used up, the battery dies - no more electron push!'",
        "'Rechargeable batteries can reverse the chemical reaction!' Zara was impressed.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: HOW BATTERIES WORK", 'F2', 13)
    y -= 20
    science = [
        "Batteries convert stored chemical energy into electrical energy.",
        "Inside are two different materials (electrodes) and a chemical paste (electrolyte).",
        "A chemical reaction at the anode (-) releases electrons that travel through the circuit.",
        "Electrons arrive at the cathode (+) where another reaction absorbs them.",
        "When the chemicals are completely reacted, the battery is 'dead.'",
        "Rechargeable batteries use a reverse current to undo the chemical reaction!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The first battery was invented in 1800 by Alessandro Volta (that is where 'volt' comes from!).",
        "A potato can make a tiny battery! The acid reacts with zinc and copper electrodes.",
        "Electric car batteries can weigh 1,000 pounds and contain thousands of small cells."
    ])
    y = try_this(doc, y, "Make a 'lemon battery': push a copper penny and a zinc nail into a lemon. Measure voltage with a multimeter!")
    y = think_about_it(doc, y, "Why do batteries eventually run out of power? What is being used up inside?")

    # Chapter 5: Magnets and Motors
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: Magnets and Motors", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Zara discovered something amazing: electricity and magnetism are connected!",
        "'When electricity flows through a wire, it creates a magnetic field around it!'",
        "She wrapped wire around a nail and connected it to a battery. The nail became a magnet!",
        "'An electromagnet! I can turn it on and off!' Zara was thrilled.",
        "'This is how electric motors work - electromagnets spinning inside them!'",
        "'Motors are in everything: fans, washing machines, electric cars, even phones!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: ELECTROMAGNETISM", 'F2', 13)
    y -= 20
    science = [
        "Moving electricity creates magnetism; moving magnets create electricity!",
        "An electromagnet is made by wrapping wire around iron and running current through it.",
        "Electric motors use electromagnets to convert electrical energy into spinning motion.",
        "Generators do the opposite: spinning magnets near wire creates electricity!",
        "This connection was discovered by Michael Faraday in 1831 - it powers our world!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "MRI machines in hospitals use super-powerful electromagnets to see inside your body.",
        "Junkyard cranes use electromagnets to pick up cars - turn off the magnet, car drops!",
        "Earth itself is a giant magnet (that is how compasses work!)."
    ])
    y = try_this(doc, y, "Wrap insulated wire around a nail 50 times, connect to a battery. Pick up paper clips - electromagnet!")
    y = think_about_it(doc, y, "Why is an electromagnet more useful than a regular magnet?")

    # Chapter 6: The Power Plant
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: The Power Plant", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "'So where does all the electricity in our homes actually COME from?' Zara wondered.",
        "She researched power plants - huge facilities that generate electricity for cities.",
        "'Most power plants spin giant generators using steam, water, or wind!'",
        "'The spinning magnets inside generators push electrons through miles of wires.'",
        "'Then electricity travels through power lines all the way to our homes!'",
        "Zara was amazed that the same basic principle (spinning magnets) powers everything.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: GENERATING ELECTRICITY", 'F2', 13)
    y -= 20
    science = [
        "Coal/Gas plants: Burn fuel to boil water, steam spins turbines, turbines spin generators.",
        "Hydroelectric: Falling water spins turbines (like at dams and waterfalls).",
        "Wind power: Wind spins turbine blades connected to generators.",
        "Solar power: Sunlight hits special cells that directly convert light to electricity!",
        "Nuclear: Splitting atoms creates heat, boils water, steam spins turbines.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Power travels through lines at nearly light speed - coast to coast in milliseconds!",
        "Solar panels have no moving parts - photons knock electrons loose in silicon cells.",
        "One wind turbine can power about 1,500 homes!"
    ])
    y = try_this(doc, y, "Spin a magnet near a coil of wire connected to an LED. Can you make it flicker? That is a generator!")
    y = think_about_it(doc, y, "What are the advantages and disadvantages of solar vs coal power?")

    # Chapter 7: Saving Energy
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: Saving Energy", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "After learning where electricity comes from, Zara realized something important.",
        "'Burning coal and gas to make electricity creates pollution and CO2!'",
        "'If we use less electricity, power plants burn less fuel and pollute less!'",
        "She made a plan: turn off lights when leaving rooms, unplug chargers, use less AC.",
        "'Renewable sources like solar and wind do not pollute at all!'",
        "'The future of energy is clean, renewable, and exciting!' Zara declared.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: ENERGY CONSERVATION", 'F2', 13)
    y -= 20
    science = [
        "Renewable energy: sun, wind, water, geothermal - they never run out!",
        "Non-renewable energy: coal, oil, natural gas - limited supply, creates pollution.",
        "LED bulbs use 75% less energy than old incandescent bulbs for the same light!",
        "Energy efficiency means getting the same result while using less electricity.",
        "Even turning off a game console (not standby) saves electricity over a year!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "If everyone in the US turned off one light for one hour, it would save enough energy for 1M homes!",
        "The Sun provides more energy to Earth in one hour than humans use in an entire year.",
        "Electric cars are 3-4 times more efficient than gasoline cars."
    ])
    y = try_this(doc, y, "Do an energy audit: walk through your home and list everything using electricity. What could you turn off?")
    y = think_about_it(doc, y, "How could your school use less electricity without losing comfort?")

    # Chapter 8: Lights On!
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: Lights On!", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "After 24 hours, the power finally came back on. CLICK! The lights returned!",
        "But Zara looked at everything differently now. She understood the magic behind it all.",
        "'Every light switch, every phone charge, every song from a speaker...'",
        "'...it is all electrons flowing through circuits, powered by spinning generators!'",
        "She turned off the lights she did not need and smiled.",
        "'Knowledge really IS power - literally!' Zara laughed at her own joke.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "MORAL:", 'F2', 14)
    y -= 18
    doc.add_text(margin, y, "Knowledge is power - literally! Understanding electricity helps us", 'F5', 12)
    y -= 16
    doc.add_text(margin, y, "use it wisely and build a cleaner, brighter future for everyone.", 'F5', 12)
    y -= 30
    science = [
        "What Zara learned on her journey:",
        "  - Electricity is the flow of electrons through conductors",
        "  - Circuits need a complete path for electricity to flow",
        "  - Batteries convert chemical energy to electrical energy",
        "  - Electromagnetism connects electricity and magnetism",
        "  - Generators spin magnets to create electricity",
        "  - Renewable energy is the future - solar, wind, and water power!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Nikola Tesla and Thomas Edison competed to bring electricity to homes in the 1880s.",
        "Today, about 1 billion people worldwide still lack access to electricity.",
        "YOU could be the scientist who invents the next big energy breakthrough!"
    ])

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "ELECTRICITY QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. What is electricity? (What flows?)",
        "2. What is the difference between static and current electricity?",
        "3. What three things does every circuit need?",
        "4. Name two conductors and two insulators.",
        "5. How does a battery make electricity?",
        "6. What is an electromagnet?",
        "7. Name three ways power plants generate electricity.",
        "8. What is the difference between renewable and non-renewable energy?",
        "9. Who flew a kite in a thunderstorm and why?",
        "10. Name three ways you can save electricity at home.",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 26

    # Vocabulary Page
    doc.new_page()
    doc.add_centered_text(720, "ELECTRICITY VOCABULARY", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    vocab = [
        ("Electron", "A tiny particle that carries negative charge; flows to make electricity"),
        ("Circuit", "A complete loop path that electricity can flow through"),
        ("Conductor", "A material that lets electricity flow easily (copper, aluminum, gold)"),
        ("Insulator", "A material that blocks electricity (rubber, plastic, glass)"),
        ("Voltage", "The 'push' or pressure that makes electrons flow (measured in volts)"),
        ("Current", "The flow of electrons; measured in amperes (amps)"),
        ("Generator", "A machine that converts motion into electricity using magnets"),
        ("Renewable", "Energy sources that never run out (solar, wind, water)"),
    ]
    y = 680
    for word, defn in vocab:
        doc.add_text(margin, y, word, 'F2', 12)
        y -= 16
        doc.add_text(margin + 20, y, defn, 'F4', 10)
        y -= 26

    # Certificate Page
    doc.new_page()
    doc.add_filled_rect(50, 100, W - 100, H - 200, 0.95)
    doc.add_rect(60, 110, W - 120, H - 220, 2, 0.3)
    doc.add_centered_text(650, "ELECTRICITY SCIENTIST CERTIFICATE", 'F2', 18)
    doc.add_centered_text(600, "I understand the power of electricity!", 'F5', 14)
    doc.add_centered_text(550, "Experiments I completed:", 'F4', 12)
    experiments = ["[ ] Static electricity (balloon)", "[ ] Simple circuit (battery + LED)",
                   "[ ] Electromagnet (nail + wire)", "[ ] Energy audit of my home"]
    y = 520
    for e in experiments:
        doc.add_text(150, y, e, 'F4', 11)
        y -= 25
    doc.add_centered_text(370, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(330, "Date: _________________", 'F4', 14)
    doc.add_centered_text(260, "Future Electrical Engineer!", 'F2', 16)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book271_Electricity_Story.pdf')
    print("Book271_Electricity_Story.pdf created successfully!")

if __name__ == '__main__':
    create_book()
