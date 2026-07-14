"""Book 267: THE INCREDIBLE JOURNEY INSIDE ME - A Science Story About the Human Body (Ages 6-10)"""
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
    doc.add_centered_text(660, "THE INCREDIBLE JOURNEY", 'F2', 26, 1)
    doc.add_centered_text(630, "INSIDE ME", 'F2', 28, 1)
    doc.add_centered_text(590, "A Science Story About the Human Body", 'F5', 16, 0.9)
    doc.add_centered_text(560, "Ages 6-10", 'F4', 14, 0.8)
    doc.add_centered_text(490, "Written by Daniel Tesfamariam", 'F4', 14, 0.9)
    doc.add_centered_text(460, "Science Story Series - Book 2", 'F4', 12, 0.7)
    doc.add_centered_text(300, "Join Nano the Explorer on an amazing", 'F4', 13, 0.8)
    doc.add_centered_text(275, "adventure inside the human body!", 'F4', 13, 0.8)
    doc.add_centered_text(100, "Educational Content | Real Science | Amazing Stories", 'F1', 10, 0.7)

    # Copyright Page
    doc.new_page()
    doc.add_centered_text(650, "THE INCREDIBLE JOURNEY INSIDE ME", 'F2', 16)
    doc.add_text(margin, 600, "Author: Daniel Tesfamariam", 'F4', 11)
    doc.add_text(margin, 580, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", 'F4', 10)
    doc.add_text(margin, 560, "No part of this publication may be reproduced without permission.", 'F4', 10)
    doc.add_text(margin, 530, "For ages 6-10. Scientific concepts simplified for young readers.", 'F4', 10)
    doc.add_text(margin, 500, "First Edition, 2025", 'F4', 10)

    # TOC
    doc.new_page()
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    chapters = [
        "Chapter 1: Shrinking Down",
        "Chapter 2: The Food Factory",
        "Chapter 3: The River of Life",
        "Chapter 4: The Pump That Never Stops",
        "Chapter 5: The Breathing Machine",
        "Chapter 6: The Command Center",
        "Chapter 7: The Defense Army",
        "Chapter 8: Growing Strong",
    ]
    y = 670
    for ch in chapters:
        doc.add_text(margin, y, ch, 'F4', 13)
        y -= 30

    # Chapter 1: Shrinking Down
    doc.new_page()
    doc.add_centered_text(720, "Chapter 1: Shrinking Down", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Meet Nano! He is the smallest explorer in the world - so small he can",
        "travel inside a human body! Today, Nano has a very special mission.",
        "'I am going to explore what happens inside you!' Nano announced excitedly.",
        "He put on his tiny explorer hat, grabbed his magnifying glass, and jumped",
        "straight into a glass of water that a boy named Alex was about to drink.",
        "'Here I go!' Nano shouted as Alex took a big gulp. The adventure begins!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: YOUR DIGESTIVE SYSTEM", 'F2', 13)
    y -= 20
    science = [
        "When you eat or drink, food enters your mouth and begins an incredible journey.",
        "Your body has a long tube called the digestive system - about 30 feet long!",
        "Its job is to break food into tiny pieces your body can use for energy.",
        "The journey from mouth to exit takes about 24-72 hours. That is 1-3 days!",
        "Every part of this system has a special job in breaking down your food.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Your digestive system is about 30 feet long - as long as a school bus!",
        "You produce about 1 liter of saliva (spit) every single day.",
        "Your body digests food even when you are standing on your head (gravity not needed)!"
    ])
    y = try_this(doc, y, "Chew a plain cracker for 30 seconds without swallowing. Does it start to taste sweet? That is enzymes!")
    y = think_about_it(doc, y, "Why do you think we need to chew food before swallowing it?")

    # Chapter 2: The Food Factory
    doc.new_page()
    doc.add_centered_text(720, "Chapter 2: The Food Factory", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Nano slid down a long, dark, squishy tube. 'This must be the esophagus!'",
        "SPLASH! He landed in a pool of bubbling liquid. 'Welcome to the stomach!'",
        "The walls around him were squeezing and churning like a washing machine.",
        "'This is where food gets broken into tiny pieces!' Nano observed.",
        "Strong acid and special chemicals called enzymes dissolved everything around him.",
        "'Time to move on before I get dissolved too!' Nano laughed nervously.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: YOUR STOMACH", 'F2', 13)
    y -= 20
    science = [
        "Your stomach is like a muscular bag that churns and mixes food with acid.",
        "Stomach acid is so strong it could dissolve metal! But a special lining protects you.",
        "Enzymes are like tiny scissors that cut food into smaller and smaller pieces.",
        "Food stays in your stomach for 2-5 hours, being broken down into a soupy mixture.",
        "After the stomach, food moves to the small intestine where nutrients are absorbed.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Your stomach can hold about 1 liter of food (like a large water bottle).",
        "The stomach lining replaces itself every 3-4 days to avoid being dissolved!",
        "Rumbling sounds happen when your stomach squeezes air and liquid together."
    ])
    y = try_this(doc, y, "Put a piece of bread in a zip bag with a little vinegar. Squeeze it - that is like digestion!")
    y = think_about_it(doc, y, "Why does your stomach make growling noises when you are hungry?")

    # Chapter 3: The River of Life
    doc.new_page()
    doc.add_centered_text(720, "Chapter 3: The River of Life", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Nano squeezed through the stomach wall and found himself in a rushing river!",
        "'This is your blood!' Nano exclaimed, amazed by the red flowing river.",
        "Tiny red discs zoomed past him like millions of delivery trucks.",
        "'Those are red blood cells! They carry oxygen to every part of your body!'",
        "White blob-like cells patrolled the area like police officers on duty.",
        "'And those are white blood cells - your body's defense soldiers!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: YOUR BLOOD", 'F2', 13)
    y -= 20
    science = [
        "Blood is made of plasma (liquid), red blood cells, white blood cells, and platelets.",
        "Red blood cells carry oxygen from your lungs to every cell in your body.",
        "White blood cells fight germs, bacteria, and viruses that try to make you sick.",
        "Platelets are tiny cell fragments that help stop bleeding when you get a cut.",
        "You have about 25 trillion red blood cells in your body right now!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "If you lined up all your blood vessels, they would stretch 60,000 miles!",
        "A single drop of blood contains about 5 million red blood cells.",
        "Your body makes about 2 million new red blood cells every single second!"
    ])
    y = try_this(doc, y, "Look at the veins on the inside of your wrist. That blue color is blood returning to your heart!")
    y = think_about_it(doc, y, "Why do you think blood looks red when it carries oxygen?")

    # Chapter 4: The Pump That Never Stops
    doc.new_page()
    doc.add_centered_text(720, "Chapter 4: The Pump That Never Stops", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "The blood river carried Nano to the most powerful muscle in the body.",
        "THUMP-THUMP! THUMP-THUMP! The sound was deafening!",
        "'The heart!' Nano shouted over the rhythmic pounding.",
        "He watched as blood flowed in and out of four amazing chambers.",
        "The right side pumped blood to the lungs, the left side to the whole body.",
        "'This incredible pump beats 100,000 times every single day!' Nano marveled.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: YOUR HEART", 'F2', 13)
    y -= 20
    science = [
        "Your heart is about the size of your fist and weighs less than a pound.",
        "It has four chambers: two atria (top) receive blood, two ventricles (bottom) pump it out.",
        "The right side sends blood to your lungs to pick up oxygen.",
        "The left side pumps oxygen-rich blood to every cell in your body.",
        "Your heart beats about 100,000 times per day - that is 35 million times a year!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "A child's heart beats about 80-100 times per minute.",
        "Your heart pumps about 2,000 gallons of blood every day!",
        "The heart starts beating about 4 weeks after a baby starts growing."
    ])
    y = try_this(doc, y, "Put your hand on your chest and count heartbeats for 15 seconds. Multiply by 4 for your heart rate!")
    y = think_about_it(doc, y, "Why does your heart beat faster when you exercise?")

    # Chapter 5: The Breathing Machine
    doc.new_page()
    doc.add_centered_text(720, "Chapter 5: The Breathing Machine", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Nano rode the bloodstream up into two enormous, spongy pink organs.",
        "'The lungs!' he exclaimed. 'This is where blood picks up fresh oxygen!'",
        "Millions of tiny air sacs called alveoli surrounded him like clusters of grapes.",
        "He watched oxygen molecules jump from the air into the blood cells.",
        "At the same time, carbon dioxide waste jumped out of the blood into the air sacs.",
        "'It is like a perfect trade!' Nano said. 'Oxygen in, carbon dioxide out!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: YOUR LUNGS", 'F2', 13)
    y -= 20
    science = [
        "You breathe about 20,000 times every day without even thinking about it!",
        "Your lungs have 300 million alveoli (tiny air sacs) for gas exchange.",
        "The diaphragm is a dome-shaped muscle under your lungs that helps you breathe.",
        "When you breathe in, oxygen goes into blood. When you breathe out, CO2 leaves.",
        "If you spread out all your alveoli flat, they would cover a tennis court!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "You breathe in about 11,000 liters of air every single day.",
        "Your right lung is slightly bigger than your left (to make room for your heart).",
        "Yawning helps get extra oxygen when your body needs it."
    ])
    y = try_this(doc, y, "Breathe onto a cold mirror - the fog is water vapor leaving your lungs!")
    y = think_about_it(doc, y, "Why do you breathe faster when you run? What does your body need more of?")

    # Chapter 6: The Command Center
    doc.new_page()
    doc.add_centered_text(720, "Chapter 6: The Command Center", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Nano traveled up through blood vessels into the most amazing organ of all.",
        "'The brain!' he whispered in awe. 'The command center of the entire body!'",
        "Billions of tiny cells called neurons were firing signals like lightning bolts.",
        "Messages zoomed along at 270 miles per hour in every direction!",
        "'This is where you think, dream, remember, feel emotions, and control everything!'",
        "Nano watched as different areas handled seeing, hearing, moving, and thinking.",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: YOUR BRAIN", 'F2', 13)
    y -= 20
    science = [
        "Your brain has about 86 billion neurons (nerve cells) that communicate with each other.",
        "Neurons send electrical signals to each other at speeds up to 270 miles per hour!",
        "Different parts of the brain control different things: movement, vision, language, emotions.",
        "Your brain uses 20% of your body's energy, even though it is only 2% of your weight.",
        "The brain is always active, even when you sleep - that is when it organizes memories!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Your brain generates enough electricity to power a small light bulb!",
        "The brain cannot feel pain - it has no pain receptors!",
        "Your brain is about 73% water. Staying hydrated helps you think better!"
    ])
    y = try_this(doc, y, "Try rubbing your belly in circles while patting your head. Your brain controls both at once!")
    y = think_about_it(doc, y, "How does your brain know to keep your heart beating while you sleep?")

    # Chapter 7: The Defense Army
    doc.new_page()
    doc.add_centered_text(720, "Chapter 7: The Defense Army", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Suddenly, alarms went off everywhere! 'Intruder alert!' signals flashed.",
        "A germ had invaded the body! Nano watched the defense army spring into action.",
        "White blood cells rushed to the scene like an army of brave soldiers.",
        "Some cells surrounded the germ and swallowed it whole! Others sent out antibodies.",
        "'Antibodies are like guided missiles!' Nano observed. 'They lock onto the germ!'",
        "Within hours, the invader was defeated. The body was safe again!",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: YOUR IMMUNE SYSTEM", 'F2', 13)
    y -= 20
    science = [
        "White blood cells are your body's soldiers - they fight off germs and diseases.",
        "Your skin is the first defense - it acts like armor keeping germs out.",
        "Antibodies are special proteins that remember germs so they can fight them faster next time.",
        "Vaccines work by teaching your immune system to recognize dangers before they attack.",
        "A fever is your body turning up the heat to kill germs that cannot survive high temperatures.",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y = science_fact_box(doc, y - 15, [
        "Your body makes different white blood cells, each with a special job.",
        "Once you beat a disease, your body remembers it and can fight it faster next time!",
        "Washing hands for 20 seconds removes 99% of germs. Sing 'Happy Birthday' twice!"
    ])
    y = try_this(doc, y, "Put glitter on your hands and try to wash it off. See how hard it is to remove all germs!")
    y = think_about_it(doc, y, "Why do you only get chickenpox once? How does your body remember?")

    # Chapter 8: Growing Strong
    doc.new_page()
    doc.add_centered_text(720, "Chapter 8: Growing Strong", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    story = [
        "Nano's last stop was the bones and muscles that give your body its shape.",
        "'Your skeleton is like a building's frame!' Nano explained to Alex.",
        "He watched muscles pulling on bones like puppet strings, making Alex move.",
        "'Muscles always work in pairs - one pulls while the other relaxes!'",
        "Nano looked at all the amazing things he had seen and smiled.",
        "'Alex, your body is truly the most incredible machine ever made!'",
    ]
    y = text_block(doc, story, 680)
    y -= 20
    doc.add_text(margin, y, "THE SCIENCE: BONES AND MUSCLES", 'F2', 13)
    y -= 20
    science = [
        "You have 206 bones in your body (babies have about 270 - some fuse together!).",
        "Bones are alive! They have blood vessels inside and grow as you grow.",
        "You have over 600 muscles that help you move, from tiny eye muscles to big leg muscles.",
        "Muscles work in pairs: biceps bends your arm, triceps straightens it.",
        "Your strongest muscle is your jaw muscle (masseter) - it can bite with 200 lbs of force!",
    ]
    y = text_block(doc, science, y, 'F4', 11, 16)
    y -= 20
    doc.add_text(margin, y, "MORAL:", 'F2', 14)
    y -= 20
    doc.add_text(margin, y, "Your body is the most incredible machine ever made - take care of it!", 'F5', 13)
    y -= 16
    doc.add_text(margin, y, "Eat healthy food, exercise, sleep well, and drink plenty of water.", 'F4', 11)
    y = science_fact_box(doc, y - 25, [
        "The smallest bone is in your ear (stirrup) - smaller than a grain of rice!",
        "Your body replaces all its bone cells every 7-10 years.",
        "Smiling uses 17 muscles; frowning uses 43. Smiling is easier!"
    ])

    # Quiz Page
    doc.new_page()
    doc.add_centered_text(720, "HUMAN BODY QUIZ", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    questions = [
        "1. How many bones does an adult human have?",
        "2. What do red blood cells carry to your body?",
        "3. How many times does your heart beat per day?",
        "4. What organ is the 'command center' of your body?",
        "5. What are the tiny air sacs in your lungs called?",
        "6. What fights germs in your body?",
        "7. How long is your digestive system?",
        "8. How many neurons are in your brain?",
        "9. What do muscles work in? (Hint: they come in ___)",
        "10. What percentage of your brain is water?",
    ]
    y = 680
    for q in questions:
        doc.add_text(margin, y, q, 'F4', 11)
        y -= 18
        doc.add_text(margin, y, "Answer: ___________________________________", 'F3', 9, 0.5)
        y -= 28

    # Vocabulary Page
    doc.new_page()
    doc.add_centered_text(720, "BODY VOCABULARY", 'F2', 20)
    doc.add_line(margin, 710, W - margin, 710, 1, 0.5)
    vocab = [
        ("Neuron", "A nerve cell that sends electrical signals in your brain and body"),
        ("Enzyme", "A chemical that speeds up breaking down food in digestion"),
        ("Alveoli", "Tiny air sacs in lungs where oxygen enters the blood"),
        ("Antibody", "A protein that helps your body fight specific germs"),
        ("Plasma", "The liquid part of blood that carries cells and nutrients"),
        ("Diaphragm", "The muscle under your lungs that helps you breathe"),
        ("Platelet", "A tiny cell fragment that helps your blood clot and stop bleeding"),
        ("Organ", "A body part with a specific important job (heart, lungs, brain)"),
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
    doc.add_centered_text(650, "I AM A BODY SCIENTIST!", 'F2', 22)
    doc.add_centered_text(600, "I learned about these body systems:", 'F5', 14)
    y = 560
    systems = ["Digestive System", "Circulatory System (Blood)", "Heart", "Lungs",
               "Brain & Nervous System", "Immune System", "Bones & Muscles"]
    for s in systems:
        doc.add_text(150, y, "[ ] " + s, 'F4', 12)
        y -= 25
    doc.add_centered_text(340, "The most amazing thing I learned: ___________________", 'F4', 12)
    doc.add_centered_text(280, "Name: _______________________________", 'F4', 14)
    doc.add_centered_text(240, "Date: _________________", 'F4', 14)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book267_Human_Body_Adventure.pdf')
    print("Book267_Human_Body_Adventure.pdf created successfully!")

if __name__ == '__main__':
    create_book()
