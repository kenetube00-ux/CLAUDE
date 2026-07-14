"""Book 260: WHAT COLOR IS IT? - Bilingual Color Book (Tigrinya-English) Ages 2-5"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(660, "WHAT COLOR IS IT?", 'F2', 30, 0)
doc.add_centered_text(620, "[TIGRINYA TEXT: Ehnta Hbri Eyu?]", 'F3', 14, 0.3)
doc.add_centered_text(570, "Bilingual Color Book", 'F1', 18, 0.2)
doc.add_centered_text(540, "(Tigrinya-English)", 'F1', 16, 0.3)
doc.add_centered_text(500, "Ages 2-5", 'F2', 16, 0.2)
doc.add_rect(180, 260, 252, 180, 2, 0.4)
doc.add_centered_text(350, "[ILLUSTRATION: Rainbow with", 'F3', 11, 0.5)
doc.add_centered_text(330, "all colors labeled]", 'F3', 11, 0.5)
doc.add_centered_text(160, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(130, "Learn Colors in Tigrinya and English!", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "WHAT COLOR IS IT?", 'F2', 14, 0)
doc.add_text(72, 520, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 500, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 470, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 450, "For Ages: 2-5 years", 'F1', 10, 0.3)
doc.add_text(72, 430, "Language: Tigrinya & English (Bilingual)", 'F1', 10, 0.3)
doc.add_text(72, 390, "NOTE: [TIGRINYA TEXT] placeholders indicate where", 'F3', 9, 0.4)
doc.add_text(72, 375, "Ge'ez script translations will be added.", 'F3', 9, 0.4)
doc.add_text(72, 320, "First Edition, 2025", 'F1', 10, 0.3)

# Colors data
colors = [
    ("Red", "Keyih", "The apple is red.", "apple"),
    ("Blue", "Semayawi", "The sky is blue.", "sky"),
    ("Green", "Hamlay", "The grass is green.", "grass and leaves"),
    ("Yellow", "Bitsuy", "The sun is yellow.", "sun"),
    ("Orange", "Aranconi", "The orange is orange.", "orange fruit"),
    ("Black", "Tsellim", "The night is black.", "night sky"),
    ("White", "Tsaeda", "The snow is white.", "snow/clouds"),
    ("Brown", "Bunni", "The tree is brown.", "tree trunk"),
    ("Pink", "Roza", "The flower is pink.", "flowers"),
    ("Purple", "Hamrawi", "The grape is purple.", "grapes"),
]

for color_eng, color_tig, sentence, obj_desc in colors:
    # Color page 1: Introduction
    doc.new_page()
    doc.add_filled_rect(0, 650, 612, 142, 0.85)
    doc.add_centered_text(730, color_eng.upper(), 'F2', 40, 0)
    doc.add_centered_text(690, f"[TIGRINYA: {color_tig}]", 'F3', 20, 0.3)
    doc.add_centered_text(650, "[FIDEL CHARACTER PLACEHOLDER]", 'F3', 14, 0.5)
    
    doc.add_centered_text(600, sentence, 'F4', 18, 0)
    doc.add_centered_text(570, f"[TIGRINYA TRANSLATION: {sentence}]", 'F3', 12, 0.4)
    
    # Object illustration area
    doc.add_rect(170, 330, 272, 200, 2, 0.4)
    doc.add_centered_text(440, f"[ILLUSTRATION: {obj_desc}", 'F3', 11, 0.5)
    doc.add_centered_text(420, f"clearly showing {color_eng.lower()} color]", 'F3', 11, 0.5)
    
    # Activity
    doc.add_text(72, 290, f"Color this {color_eng.lower()}!", 'F2', 16, 0)
    doc.add_text(72, 265, f"[TIGRINYA: Nezi {color_tig} gberwo!]", 'F3', 11, 0.4)
    
    # Coloring area
    doc.add_rect(72, 100, 200, 140, 2, 0.5)
    doc.add_centered_text(170, f"Color me {color_eng.lower()}!", 'F1', 11, 0.6)
    
    # Find and circle
    doc.add_text(310, 240, "Find something", 'F2', 13, 0)
    doc.add_text(310, 220, f"{color_eng.lower()} in your room!", 'F2', 13, 0)
    doc.add_text(310, 195, f"[TIGRINYA: {color_tig} ab kiflkha deli!]", 'F3', 10, 0.4)
    doc.add_text(310, 165, "Draw it here:", 'F1', 12, 0)
    doc.add_rect(310, 100, 220, 55, 1.5, 0.5)

# Color review page
doc.new_page()
doc.add_centered_text(740, "ALL THE COLORS! / [TIGRINYA: Kulu Hbri!]", 'F2', 18, 0)
doc.add_centered_text(710, "Point to each color and say its name!", 'F1', 13, 0)

y = 650
for color_eng, color_tig, sentence, obj_desc in colors:
    doc.add_rect(72, y-5, 30, 25, 2, 0.3)
    doc.add_text(115, y, f"{color_eng}", 'F2', 13, 0)
    doc.add_text(220, y, f"[TIGRINYA: {color_tig}]", 'F3', 12, 0.4)
    doc.add_text(380, y, f"[FIDEL]", 'F3', 10, 0.5)
    y -= 40

doc.add_centered_text(200, "I know my colors! / [TIGRINYA: Hbri-ey feliteyo!]", 'F2', 14, 0.2)

# Color matching activity
doc.new_page()
doc.add_centered_text(740, "COLOR MATCHING GAME", 'F2', 18, 0)
doc.add_centered_text(710, "[TIGRINYA: Tsewta Matsmats Hbri]", 'F3', 12, 0.4)
doc.add_centered_text(680, "Draw a line from the word to the colored box!", 'F1', 13, 0)

y = 620
for i, (color_eng, color_tig, _, _) in enumerate(colors[:5]):
    doc.add_text(72, y, f"{color_eng} / [{color_tig}]", 'F2', 13, 0)
    doc.add_rect(430, y-5, 50, 30, 2, 0.3)
    y -= 60

doc.add_centered_text(250, "Great job learning colors!", 'F2', 14, 0.2)
doc.add_centered_text(220, "[TIGRINYA: Tsbuq srah ab mflaT hbri!]", 'F3', 12, 0.4)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book260_Tigrinya_Colors_Book.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
