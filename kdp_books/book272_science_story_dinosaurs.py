"""Book 272: DINOSAUR TIME MACHINE - A Science Story About Prehistoric Life (Ages 6-12)"""
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
    doc.add_centered_text(660, "DINOSAUR TIME MACHINE", 'F2', 26, 1)
    doc.add_centered_text(625, "A Science Story About Prehistoric Life", 'F5', 16, 0.9)
    doc.add_centered_text(595, "Ages 6-12", 'F4', 14, 0.8)
    doc.add_centered_text(490, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
    doc.add_centered_text(460, "Science Story Series - Book 7", 'F4', 12, 0.7)
    doc.add_centered_text(350, "Travel back 230 million years and meet", 'F4', 13, 0.8)
    doc.add_centered_text(325, "the incredible creatures that ruled Earth!", 'F4', 13, 0.8)
    doc.add_centered_text(100, "Educational Content | Real Science | Amazing Stories", 'F1', 10, 0.7)

    # Copyright
    doc.new_page()
    doc.add_centered_text(650, "DINOSAUR TIME MACHINE", 'F2', 16)
    doc.add_text(margin, 600, "Author: Daniel Tesfamariam", 'F4', 11)
    doc.add_text(margin, 580, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", 'F4', 10)
    doc.add_text(margin, 560, "No part of this publication may be reproduced without permission.", 'F4', 10)
    doc.add_text(margin, 530, "For ages 6-12. Scientific facts based on current paleontological research.", 'F4', 10)
    doc.add_text(margin, 500, "First Edition, 2025", 'F4', 10)

    # TOC
    doc.new_page()
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    chapters = [
        "Chapter 1: The Time Machine",
        "Chapter 2: The Triassic Period",
        "Chapter 3: Giants of the Jurassic",
        "Chapter 4: The Fierce Hunters",
        "Chapter 5: Flying Reptiles",
        "Chapter 6: Ocean Giants",
        "Chapter 7: The Day Everything Changed",
        "Chapter 8: Back to Today",
    ]
    y = 670
    for ch in chapters:
        doc.add_text(margin, y, ch, 'F4', 13)
        y -= 30

    # Chapter 1: The Time Machine
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: The Time Machine", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Twins Leo and Luna were exploring their grandpa's dusty attic one rainy afternoon.",
        "Behind old boxes and cobwebs, they found something incredible - a strange machine!",
        "It had dials, buttons, and a screen that said 'DESTINATION: 230,000,000 YEARS AGO.'",
        "'It is a time machine!' Luna gasped. 'Should we try it?'",
        "Leo grinned. 'Absolutely! Let us visit the age of the dinosaurs!'",
        "They climbed in, pressed the big green button, and WHOOOOSH - they were gone!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: HOW WE KNOW ABOUT DINOSAURS", 'F2', 13)
    y -= 20
    science = [
        "Fossils are preserved remains or traces of ancient life (bones, teeth, footprints).",
        "Scientists called paleontologists dig up and study fossils to learn about the past.",
        "Fossils form when an animal is buried quickly in sediment after death.",
        "Over millions of years, minerals replace the bone, turning it to stone.",
        "We can determine fossil ages using radioactive dating of the surrounding rock.",
        "Dinosaurs lived during the Mesozoic Era: Triassic, Jurassic, and Cretaceous periods.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The word 'dinosaur' means 'terrible lizard' in Greek (coined in 1842).",
        "Over 1,000 different dinosaur species have been named so far!",
        "New dinosaur species are discovered about every 2 weeks somewhere in the world."
    ])
    y = try_this(doc, y, "Make a fossil: press a shell or leaf into clay, remove it, fill the impression with plaster!")
    y = think_about_it(doc, y, "Why do we only find fossils of some animals and not all of them?")

    # Chapter 2: The Triassic Period
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: The Triassic Period", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The time machine landed with a THUD. Leo and Luna stepped out into a hot, dry world.",
        "'Welcome to the Triassic Period - 230 million years ago!' the machine announced.",
        "The landscape looked different: all the continents were joined in one supercontinent!",
        "Small dinosaurs, only about the size of dogs, scurried through the ferns.",
        "'These are the FIRST dinosaurs!' Luna pointed. 'They are so small!'",
        "'But give them 165 million years,' Leo smiled, 'and they will rule the whole planet!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: THE TRIASSIC WORLD", 'F2', 13)
    y -= 20
    science = [
        "The Triassic Period lasted from 252 to 201 million years ago.",
        "All continents were joined in one supercontinent called Pangaea.",
        "The first dinosaurs appeared about 230 million years ago - they were small!",
        "Early dinosaurs like Eoraptor were only about 3 feet long and walked on two legs.",
        "Other animals lived alongside them: early mammals (tiny!), crocodile ancestors, and more.",
        "The climate was mostly hot and dry with no polar ice caps.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Pangaea means 'all lands' in Greek - it was one giant landmass!",
        "The first dinosaurs were not the biggest - they had to compete with other reptiles.",
        "Dinosaurs became dominant after a mass extinction wiped out their competitors."
    ])
    y = try_this(doc, y, "Cut out the continents from a map and try to fit them together like a puzzle - that is Pangaea!")
    y = think_about_it(doc, y, "If all continents were once joined, how did they move apart? What force moved them?")

    # Chapter 3: Giants of the Jurassic
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: Giants of the Jurassic", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The twins jumped forward in time to the Jurassic Period. The world had changed!",
        "Suddenly, an ENORMOUS shadow fell over them. They looked up... and up... and UP!",
        "A Brachiosaurus towered above the trees - taller than a five-story building!",
        "'It is as long as three school buses!' Leo whispered, amazed.",
        "The gentle giant munched on treetop leaves, unbothered by the tiny humans below.",
        "A herd of them moved slowly across the lush green landscape like living mountains.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: GIANT HERBIVORES", 'F2', 13)
    y -= 20
    science = [
        "Sauropods were the largest land animals EVER - some over 100 feet long!",
        "They were herbivores (plant-eaters) with long necks to reach high treetops.",
        "Brachiosaurus: 85 ft long, 40 ft tall, weighed 80 tons (like 11 elephants!).",
        "Diplodocus: 90 ft long with a whip-like tail for defense against predators.",
        "They swallowed stones (gastroliths) to help grind food in their stomachs!",
        "Their long necks let them eat from trees that other dinosaurs could not reach.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Sauropod footprints have been found that are over 5 feet across!",
        "The biggest sauropod (Argentinosaurus) may have weighed 100 tons!",
        "Some sauropods may have lived 100+ years based on bone growth ring analysis."
    ])
    y = try_this(doc, y, "Measure 85 feet outside (about 28 big steps). That is how long a Brachiosaurus was!")
    y = think_about_it(doc, y, "How much food would a 100-foot-long animal need to eat every day?")

    # Chapter 4: The Fierce Hunters
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: The Fierce Hunters", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The twins traveled to the Cretaceous Period - 68 million years ago.",
        "THUMP. THUMP. THUMP. The ground shook with heavy footsteps.",
        "Through the trees appeared the most famous dinosaur of all: Tyrannosaurus Rex!",
        "It was 40 feet long with teeth the size of bananas and jaws that could crush bone!",
        "'RUN!' Leo yelled. But the T. Rex was not interested in them - it was chasing prey!",
        "They watched from behind a fallen log as the mighty hunter sprinted past at 20 mph.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: CARNIVOROUS DINOSAURS", 'F2', 13)
    y -= 20
    science = [
        "T. Rex: 40 ft long, 12 ft tall at the hip, 9 tons - the apex predator!",
        "Its bite force was 12,800 pounds - strong enough to crush a car!",
        "T. Rex had excellent eyesight and could see better than a hawk.",
        "Velociraptor: smaller (6 ft) but hunted in packs and was incredibly smart.",
        "Spinosaurus: possibly the largest carnivorous dinosaur (50+ ft), ate fish!",
        "Carnivores had sharp, curved teeth for tearing meat (unlike flat herbivore teeth).",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "T. Rex arms were only about 3 feet long - but could still lift 400 pounds each!",
        "T. Rex could eat up to 500 pounds of meat in a single bite.",
        "Real Velociraptors were only about 6 feet long and had feathers (not like in movies!)."
    ])
    y = try_this(doc, y, "Compare your teeth in a mirror: flat ones for grinding (herbivore) and pointed ones for tearing (carnivore)!")
    y = think_about_it(doc, y, "Was T. Rex a hunter, a scavenger, or both? What evidence would tell us?")

    # Chapter 5: Flying Reptiles
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: Flying Reptiles", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Luna looked up and saw something incredible soaring through the Cretaceous sky.",
        "A Pteranodon glided overhead with wings wider than a small airplane!",
        "'Wait - are those flying dinosaurs?' Leo asked.",
        "'Actually no!' Luna corrected. 'Pterosaurs were flying reptiles, NOT dinosaurs!'",
        "'They lived alongside dinosaurs but belonged to a completely different group.'",
        "The enormous creature swooped down toward the ocean, snatching fish from the waves.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: PTEROSAURS", 'F2', 13)
    y -= 20
    science = [
        "Pterosaurs were flying reptiles that lived alongside dinosaurs - but were NOT dinosaurs!",
        "Their wings were made of skin membrane stretched from an elongated finger to their body.",
        "Quetzalcoatlus had a 36-foot wingspan - as wide as a fighter jet!",
        "Despite their size, many pterosaurs were surprisingly lightweight (hollow bones).",
        "Some pterosaurs were as small as sparrows; others were the largest flying animals ever.",
        "They went extinct along with the dinosaurs 66 million years ago.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Quetzalcoatlus stood as tall as a giraffe when on the ground!",
        "Pterosaurs had excellent eyesight for hunting fish from high in the air.",
        "The first pterosaur fossil was discovered in 1784 in Germany."
    ])
    y = try_this(doc, y, "Make a paper airplane. How is its 'wing' different from a bird's wing or a pterosaur's wing?")
    y = think_about_it(doc, y, "What is the difference between pterosaurs, birds, and bats? They all fly differently!")

    # Chapter 6: Ocean Giants
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: Ocean Giants", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The time machine could also work underwater! The twins dove into the ancient sea.",
        "Massive creatures swam through the dark water all around them.",
        "A Mosasaurus glided past - 50 feet of powerful jaws and streamlined body!",
        "'These are marine reptiles,' Luna explained. 'Also NOT technically dinosaurs.'",
        "Long-necked Plesiosaurs paddled gracefully with their four flippers.",
        "'The oceans were just as dangerous as the land!' Leo gulped.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: MARINE REPTILES", 'F2', 13)
    y -= 20
    science = [
        "Marine reptiles ruled the oceans while dinosaurs ruled the land.",
        "Mosasaurus: 50 ft long, top predator of Cretaceous seas, ate sharks and fish.",
        "Plesiosaur: long neck, four flippers, some were 40+ feet long.",
        "Ichthyosaur: shaped like dolphins, could swim up to 22 mph, gave live birth!",
        "These ocean giants were air-breathing reptiles - they had to surface to breathe.",
        "None of these marine reptiles were actually dinosaurs (dinosaurs lived only on land).",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Some Plesiosaurs had necks 23 feet long - half their total body length!",
        "Loch Ness Monster legends may have been inspired by Plesiosaur fossils.",
        "Mosasaurus is related to modern Komodo dragons and monitor lizards."
    ])
    y = try_this(doc, y, "Compare a dolphin shape to an ichthyosaur picture. Notice they look similar even though not related!")
    y = think_about_it(doc, y, "Why do ichthyosaurs and dolphins look so similar despite not being related?")

    # Chapter 7: The Day Everything Changed
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: The Day Everything Changed", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The twins set the time machine to 66 million years ago - the day it all ended.",
        "A bright light streaked across the sky, growing larger and larger.",
        "'The asteroid!' Luna whispered. 'It is about 7 miles wide, moving at 44,000 mph!'",
        "They watched from the safety of the machine as it struck the Earth near Mexico.",
        "The impact was unimaginable - 10 billion times more powerful than a nuclear bomb.",
        "Dust filled the sky, blocking the Sun. Within months, most life on Earth would die.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: THE KT EXTINCTION", 'F2', 13)
    y -= 20
    science = [
        "66 million years ago, an asteroid about 7 miles wide hit what is now Mexico.",
        "The impact created the Chicxulub crater - 110 miles wide and 12 miles deep!",
        "Dust and debris blocked sunlight for months, causing a global 'winter.'",
        "Without sunlight, plants died. Without plants, herbivores starved. Then carnivores.",
        "About 75% of all species went extinct, including all non-bird dinosaurs.",
        "Evidence: a thin layer of rare element iridium found worldwide in 66-million-year-old rock.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "The asteroid hit with the force of 10 billion Hiroshima bombs!",
        "Tsunamis over 300 feet high swept across the globe after impact.",
        "Small mammals survived by burrowing underground and eating insects/seeds."
    ])
    y = try_this(doc, y, "Drop a ball into a tray of flour/cocoa powder. See the 'crater' and 'debris' pattern it makes!")
    y = think_about_it(doc, y, "If the asteroid had missed Earth, would dinosaurs still be alive today?")

    # Chapter 8: Back to Today
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: Back to Today", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The twins returned to the present day, their minds full of incredible memories.",
        "'It is amazing that birds are actually living dinosaurs!' Leo said.",
        "'That is right! Birds evolved from small feathered dinosaurs that survived.'",
        "They looked out the window at sparrows hopping on the lawn.",
        "'Those little guys are real-life dinosaurs!' Luna laughed.",
        "'The past teaches us so much about our world,' they agreed. 'Stay curious!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: DINOSAURS LIVE ON!", 'F2', 13)
    y -= 20
    science = [
        "Birds ARE dinosaurs! They evolved from small, feathered theropod dinosaurs.",
        "The link: archaeopteryx had feathers AND teeth, claws, and a bony tail!",
        "All 10,000+ bird species today are technically avian dinosaurs.",
        "Paleontology is the study of prehistoric life through fossils.",
        "New fossils are found every year, rewriting what we know about the past!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y -= 15
    doc.add_text(margin, y, "MORAL:", 'F2', 14)
    y -= 18
    doc.add_text(margin, y, "The past teaches us about the future - stay curious and keep exploring!", 'F5', 13)
    y = science_fact_box(doc, y - 30, [
        "A chicken is more closely related to T. Rex than a lizard is!",
        "Some dinosaur fossils still contain preserved proteins from 80 million years ago.",
        "YOU could discover a new dinosaur species - many are still waiting to be found!"
    ])

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "DINOSAUR QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. What are fossils?",
        "2. What was Pangaea?",
        "3. Name the three periods of the Mesozoic Era.",
        "4. Were pterosaurs dinosaurs? Why or why not?",
        "5. What was the largest land carnivore?",
        "6. What killed the dinosaurs 66 million years ago?",
        "7. What living animals are actually dinosaurs?",
        "8. How big was Brachiosaurus?",
        "9. What is a paleontologist?",
        "10. Name one marine reptile from the dinosaur age.",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 26

    # Dino Size Chart Activity
    doc.new_page()
    doc.add_centered_text(720, "DINOSAUR SIZE COMPARISON", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    doc.add_text(margin, 680, "Draw a line for each dinosaur's length. Use the scale: 1 inch = 10 feet", 'F4', 11)
    dinos = [
        ("Compsognathus", "3 ft (tiny!)", 0.3),
        ("Velociraptor", "6 ft", 0.6),
        ("Human (for comparison)", "6 ft", 0.6),
        ("T. Rex", "40 ft", 4.0),
        ("Triceratops", "30 ft", 3.0),
        ("Brachiosaurus", "85 ft", 8.5),
        ("Argentinosaurus", "100 ft", 10.0),
    ]
    y = 640
    for name, length, _ in dinos:
        doc.add_text(margin, y, f"{name}: {length}", 'F4', 11)
        y -= 14
        doc.add_text(margin, y, "Draw line here: ____________________________________________", 'F3', 9, 0.4)
        y -= 30

    # Certificate
    doc.new_page()
    doc.add_filled_rect(50, 100, W - 100, H - 200, 0.95)
    doc.add_rect(60, 110, W - 120, H - 220, 2, 0.3)
    doc.add_centered_text(650, "JUNIOR PALEONTOLOGIST CERTIFICATE", 'F2', 18)
    doc.add_centered_text(600, "I traveled through time and learned about dinosaurs!", 'F5', 13)
    doc.add_centered_text(550, "My favorite dinosaur: _______________________", 'F4', 12)
    doc.add_centered_text(510, "because: ___________________________________", 'F4', 12)
    doc.add_centered_text(450, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(410, "Date: _________________", 'F4', 14)
    doc.add_centered_text(340, "Certified Dinosaur Expert!", 'F2', 18)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book272_Dinosaur_Time_Travel.pdf')
    print("Book272_Dinosaur_Time_Travel.pdf created successfully!")

if __name__ == '__main__':
    create_book()
