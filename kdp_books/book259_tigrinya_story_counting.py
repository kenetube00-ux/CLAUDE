"""Book 259: LET'S COUNT! 1-10 - Bilingual Number Book (Tigrinya-English) Ages 2-5"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(660, "LET'S COUNT! 1-10", 'F2', 30, 0)
doc.add_centered_text(620, "[TIGRINYA TEXT: Nqotsir! 1-10]", 'F3', 14, 0.3)
doc.add_centered_text(570, "Bilingual Number Book", 'F1', 18, 0.2)
doc.add_centered_text(540, "(Tigrinya-English)", 'F1', 16, 0.3)
doc.add_centered_text(500, "Ages 2-5", 'F2', 16, 0.2)
doc.add_rect(180, 260, 252, 180, 2, 0.4)
doc.add_centered_text(350, "[ILLUSTRATION: Numbers 1-10", 'F3', 11, 0.5)
doc.add_centered_text(330, "with colorful objects to count]", 'F3', 11, 0.5)
doc.add_centered_text(160, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(130, "Learn to Count in Tigrinya and English!", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "LET'S COUNT! 1-10", 'F2', 14, 0)
doc.add_text(72, 520, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 500, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 470, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 450, "For Ages: 2-5 years", 'F1', 10, 0.3)
doc.add_text(72, 430, "Language: Tigrinya & English (Bilingual)", 'F1', 10, 0.3)
doc.add_text(72, 390, "NOTE: [TIGRINYA TEXT] placeholders indicate where", 'F3', 9, 0.4)
doc.add_text(72, 375, "Ge'ez script translations will be added.", 'F3', 9, 0.4)
doc.add_text(72, 320, "First Edition, 2025", 'F1', 10, 0.3)

# Number data
numbers = [
    (1, "One", "Hade", "Sun", "Tsehay", "There is ONE bright sun in the sky!"),
    (2, "Two", "Klte", "Eyes", "Ayni", "I have TWO eyes to see the world!"),
    (3, "Three", "Seleste", "Birds", "Awaf", "THREE birds are singing in the tree!"),
    (4, "Four", "Arbaate", "Legs", "Egri", "A cat has FOUR legs to walk!"),
    (5, "Five", "Hamushte", "Fingers", "Atsabi'i", "I have FIVE fingers on each hand!"),
    (6, "Six", "Shidushte", "Stars", "Kokob", "SIX stars are shining tonight!"),
    (7, "Seven", "Shewate", "Colors", "Hbri", "SEVEN colors in the rainbow!"),
    (8, "Eight", "Shemonte", "Flowers", "Zembaba", "EIGHT flowers in the garden!"),
    (9, "Nine", "Tishate", "Fish", "Asa", "NINE fish swimming in the sea!"),
    (10, "Ten", "Aserte", "Bananas", "Banan", "TEN bananas in the basket!"),
]

for num, eng, tig, obj_eng, obj_tig, sentence in numbers:
    # Number page
    doc.new_page()
    doc.add_filled_rect(0, 650, 612, 142, 0.88)
    doc.add_centered_text(730, str(num), 'F2', 72, 0)
    doc.add_centered_text(680, f"{eng} / [TIGRINYA: {tig}]", 'F2', 22, 0.2)
    
    doc.add_centered_text(620, sentence, 'F4', 16, 0)
    doc.add_centered_text(590, f"[TIGRINYA TRANSLATION PLACEHOLDER]", 'F3', 12, 0.4)
    
    doc.add_centered_text(550, f"{obj_eng} / [TIGRINYA: {obj_tig}]", 'F2', 16, 0.2)
    
    # Draw counting objects (circles)
    start_x = 306 - (num * 25)
    for c in range(num):
        cx = start_x + c * 50
        doc.add_rect(cx, 440, 35, 35, 2, 0.3)
        doc.add_centered_text(455, "", 'F1', 10, 0.5)  # placeholder for object
    
    doc.add_centered_text(400, f"Count the {obj_eng.lower()}! / [TIGRINYA: Qotsir neh {obj_tig}!]", 'F1', 13, 0.3)
    
    # Trace section
    doc.add_text(72, 350, "Trace the number:", 'F2', 14, 0)
    doc.add_text(72, 325, "[TIGRINYA: Qotsir tsihaf:]", 'F3', 10, 0.4)
    doc.add_text(150, 270, str(num), 'F2', 60, 0.8)
    doc.add_text(250, 270, str(num), 'F2', 60, 0.8)
    doc.add_text(350, 270, str(num), 'F2', 60, 0.8)
    
    # Writing practice lines
    doc.add_line(72, 200, 540, 200, 1, 0.6)
    doc.add_line(72, 160, 540, 160, 1, 0.6)
    doc.add_line(72, 120, 540, 120, 1, 0.6)

# Count and match activity page
doc.new_page()
doc.add_centered_text(740, "COUNT AND MATCH!", 'F2', 20, 0)
doc.add_centered_text(710, "[TIGRINYA: Qotsirn Atsamamiy!]", 'F3', 12, 0.4)
doc.add_centered_text(680, "Draw a line from the number to the right group!", 'F1', 13, 0)

y = 620
for i in range(5):
    doc.add_text(100, y, str(i+1), 'F2', 24, 0)
    # Draw circles representing the count on the right side
    for c in range(i+1):
        doc.add_rect(350 + c*30, y-5, 20, 20, 1.5, 0.4)
    y -= 70

# Review page
doc.new_page()
doc.add_centered_text(740, "LET'S REVIEW! / [TIGRINYA: Ndeggim!]", 'F2', 18, 0)
doc.add_centered_text(700, "Can you count from 1 to 10?", 'F1', 14, 0)
y = 650
for num, eng, tig, obj_eng, obj_tig, sentence in numbers:
    doc.add_text(72, y, f"{num}. {eng}", 'F2', 13, 0)
    doc.add_text(200, y, f"[TIGRINYA: {tig}]", 'F3', 12, 0.4)
    doc.add_text(350, y, f"{obj_eng}", 'F1', 12, 0.3)
    y -= 40

doc.add_centered_text(200, "Great job counting! / [TIGRINYA: Tsbuq srah ab mqotsir!]", 'F2', 14, 0.2)
doc.add_centered_text(170, "You can count to 10 in TWO languages!", 'F1', 13, 0)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book259_Tigrinya_Counting_Book.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
