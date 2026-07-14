"""Book 263: MY BODY - Learn Body Parts (Tigrinya-English) Ages 2-5"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(660, "MY BODY", 'F2', 36, 0)
doc.add_centered_text(620, "[TIGRINYA TEXT: Sga-ey]", 'F3', 16, 0.3)
doc.add_centered_text(570, "Learn Body Parts", 'F1', 18, 0.2)
doc.add_centered_text(540, "(Tigrinya-English)", 'F1', 16, 0.3)
doc.add_centered_text(500, "Ages 2-5", 'F2', 16, 0.2)
doc.add_rect(200, 270, 212, 180, 2, 0.4)
doc.add_centered_text(370, "[ILLUSTRATION: Smiling child", 'F3', 11, 0.5)
doc.add_centered_text(350, "with body parts labeled]", 'F3', 11, 0.5)
doc.add_centered_text(170, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(140, "Learn Body Parts in Two Languages!", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "MY BODY / [TIGRINYA: Sga-ey]", 'F2', 14, 0)
doc.add_text(72, 520, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 500, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 470, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 450, "For Ages: 2-5 years", 'F1', 10, 0.3)
doc.add_text(72, 430, "Language: Tigrinya & English (Bilingual)", 'F1', 10, 0.3)
doc.add_text(72, 390, "NOTE: [TIGRINYA TEXT] placeholders indicate where", 'F3', 9, 0.4)
doc.add_text(72, 375, "Ge'ez script translations will be added.", 'F3', 9, 0.4)
doc.add_text(72, 320, "First Edition, 2025", 'F1', 10, 0.3)

# Body parts data
body_parts = [
    ("Head", "Risi", "Your head helps you think big thoughts!",
     "Your brain is inside your head. It helps you learn, dream, and remember.",
     "Touch your head and say 'Risi'!"),
    ("Eyes", "Ayni", "Your eyes help you see the beautiful world!",
     "You have two eyes. They help you see colors, shapes, and your family.",
     "Blink your eyes and say 'Ayni'!"),
    ("Ears", "Ezni", "Your ears help you hear sounds all around!",
     "You have two ears. They help you hear music, birds, and your mom's voice.",
     "Touch your ears and say 'Ezni'!"),
    ("Nose", "Anfi", "Your nose helps you smell yummy food!",
     "Your nose helps you breathe and smell flowers, food, and rain.",
     "Touch your nose and say 'Anfi'!"),
    ("Mouth", "Af", "Your mouth helps you talk, eat, and smile!",
     "Your mouth has teeth for chewing and a tongue for tasting.",
     "Open your mouth wide and say 'Af'!"),
    ("Hands", "Idi", "Your hands help you hold things and wave hello!",
     "You have two hands. They help you draw, clap, and hug people you love.",
     "Clap your hands and say 'Idi'!"),
    ("Fingers", "Atsabi'i", "Your fingers help you pick up small things!",
     "You have ten fingers - five on each hand! They help you write and point.",
     "Wiggle your fingers and say 'Atsabi-i'!"),
    ("Legs", "Egri", "Your legs help you run and jump high!",
     "You have two strong legs. They help you walk, run, dance, and kick a ball.",
     "Stomp your legs and say 'Egri'!"),
    ("Feet", "Egri (feet)", "Your feet carry you everywhere you go!",
     "You have two feet with ten toes. They help you stand, walk, and balance.",
     "Stamp your feet and say 'Egri'!"),
    ("Tummy", "Kebd", "Your tummy tells you when it is hungry!",
     "Your tummy digests the food you eat and gives you energy to play.",
     "Pat your tummy and say 'Kebd'!"),
    ("Hair", "Tseguri", "Your hair grows on top of your head!",
     "Everyone's hair is different and beautiful - curly, straight, short, or long.",
     "Touch your hair and say 'Tseguri'!"),
    ("Heart", "Libi", "Your heart beats inside your chest!",
     "Your heart pumps blood through your whole body. It beats all day and night!",
     "Put your hand on your chest and feel your 'Libi' beat!"),
]

for part_eng, part_tig, intro, fun_fact, action in body_parts:
    # Body part page
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.85)
    doc.add_centered_text(755, part_eng.upper(), 'F2', 32, 0)
    doc.add_centered_text(720, f"[TIGRINYA: {part_tig}]", 'F3', 18, 0.3)
    doc.add_centered_text(700, "[FIDEL CHARACTER PLACEHOLDER]", 'F3', 11, 0.5)
    
    # Illustration area
    doc.add_rect(200, 500, 212, 170, 2, 0.4)
    doc.add_centered_text(590, f"[ILLUSTRATION: {part_eng}", 'F3', 10, 0.5)
    doc.add_centered_text(570, "clearly shown on a child's body]", 'F3', 10, 0.5)
    
    # Introduction sentence
    doc.add_centered_text(470, intro, 'F4', 15, 0)
    doc.add_centered_text(445, "[TIGRINYA TRANSLATION PLACEHOLDER]", 'F3', 11, 0.4)
    
    # Fun fact
    doc.add_text(72, 400, "Fun Fact:", 'F2', 13, 0.2)
    doc.add_text(72, 378, fun_fact, 'F4', 12, 0)
    doc.add_text(72, 355, "[TIGRINYA: Fun fact translation placeholder]", 'F3', 10, 0.4)
    
    # Action
    doc.add_filled_rect(60, 280, 492, 50, 0.92)
    doc.add_centered_text(310, action, 'F2', 14, 0)
    doc.add_centered_text(285, f"[TIGRINYA: Action instruction for {part_tig}]", 'F3', 10, 0.4)
    
    # Activity: trace or circle
    doc.add_text(72, 245, f"Trace the word: {part_eng}", 'F2', 13, 0)
    doc.add_text(72, 210, part_eng, 'F2', 28, 0.75)
    doc.add_line(72, 170, 540, 170, 1, 0.6)
    doc.add_line(72, 130, 540, 130, 1, 0.6)
    doc.add_text(72, 100, f"[TIGRINYA: Trace {part_tig} in Fidel here]", 'F3', 10, 0.4)

# Body labeling activity page
doc.new_page()
doc.add_centered_text(740, "LABEL MY BODY!", 'F2', 20, 0)
doc.add_centered_text(710, "[TIGRINYA: Sga-ey Semiy!]", 'F3', 12, 0.4)
doc.add_centered_text(680, "Can you point to each body part and say its name?", 'F1', 13, 0)

doc.add_rect(220, 250, 172, 400, 2, 0.4)
doc.add_centered_text(460, "[ILLUSTRATION: Outline of a child", 'F3', 10, 0.5)
doc.add_centered_text(440, "for labeling body parts]", 'F3', 10, 0.5)

# Labels around the figure
doc.add_text(72, 620, "Head [Risi]", 'F1', 10, 0.3)
doc.add_text(72, 580, "Eyes [Ayni]", 'F1', 10, 0.3)
doc.add_text(72, 540, "Ears [Ezni]", 'F1', 10, 0.3)
doc.add_text(72, 500, "Nose [Anfi]", 'F1', 10, 0.3)
doc.add_text(72, 460, "Mouth [Af]", 'F1', 10, 0.3)
doc.add_text(420, 580, "Hair [Tseguri]", 'F1', 10, 0.3)
doc.add_text(420, 500, "Hands [Idi]", 'F1', 10, 0.3)
doc.add_text(420, 420, "Tummy [Kebd]", 'F1', 10, 0.3)
doc.add_text(420, 340, "Legs [Egri]", 'F1', 10, 0.3)
doc.add_text(420, 280, "Feet [Egri]", 'F1', 10, 0.3)

doc.add_centered_text(210, "I know my body parts!", 'F2', 16, 0.2)
doc.add_centered_text(180, "[TIGRINYA: Kflit sga-ey feliteyo!]", 'F3', 12, 0.4)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book263_Tigrinya_Body_Parts.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
