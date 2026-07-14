"""Book 262: MY FIRST TIGRINYA ALPHABET - Learn Fidel for Kids Ages 3-6"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(660, "MY FIRST TIGRINYA ALPHABET", 'F2', 26, 0)
doc.add_centered_text(620, "[TIGRINYA TEXT: Qadamay Fidel-ey]", 'F3', 14, 0.3)
doc.add_centered_text(580, "Learn Fidel for Kids", 'F1', 18, 0.2)
doc.add_centered_text(550, "Ages 3-6", 'F2', 16, 0.2)
doc.add_rect(180, 280, 252, 200, 2, 0.4)
doc.add_centered_text(380, "[ILLUSTRATION: Colorful Fidel/Ge'ez", 'F3', 11, 0.5)
doc.add_centered_text(360, "alphabet characters for children]", 'F3', 11, 0.5)
doc.add_centered_text(180, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(150, "Introduction to the Ge'ez Script (Fidel)", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "MY FIRST TIGRINYA ALPHABET", 'F2', 14, 0)
doc.add_text(72, 520, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 500, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 470, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 450, "For Ages: 3-6 years", 'F1', 10, 0.3)
doc.add_text(72, 430, "Language: Tigrinya (Ge'ez Script) & English", 'F1', 10, 0.3)
doc.add_text(72, 390, "NOTE: [FIDEL CHARACTER PLACEHOLDER] indicates where", 'F3', 9, 0.4)
doc.add_text(72, 375, "actual Ge'ez script characters will be added.", 'F3', 9, 0.4)
doc.add_text(72, 340, "The Tigrinya alphabet (Fidel) has over 200 characters.", 'F1', 10, 0.3)
doc.add_text(72, 320, "This book introduces the first-order characters.", 'F1', 10, 0.3)
doc.add_text(72, 280, "First Edition, 2025", 'F1', 10, 0.3)

# Page 3: Introduction
doc.new_page()
doc.add_centered_text(730, "WHAT IS FIDEL?", 'F2', 20, 0)
doc.add_centered_text(700, "[TIGRINYA: Ehnta Eyu Fidel?]", 'F3', 12, 0.4)
doc.add_text(72, 650, "The Tigrinya alphabet is called FIDEL.", 'F4', 14, 0)
doc.add_text(72, 620, "It is one of the oldest writing systems in the world!", 'F4', 14, 0)
doc.add_text(72, 590, "Fidel is also called the Ge'ez script.", 'F4', 14, 0)
doc.add_text(72, 560, "Each character represents a consonant + vowel sound.", 'F4', 14, 0)
doc.add_text(72, 530, "There are 7 forms for each base consonant.", 'F4', 14, 0)
doc.add_text(72, 490, "In this book, we will learn the FIRST form of each letter.", 'F2', 13, 0)
doc.add_text(72, 460, "This is called the 'Ge'ez' or first order.", 'F1', 13, 0)
doc.add_text(72, 420, "[TIGRINYA TRANSLATION OF INTRODUCTION]", 'F3', 11, 0.4)
doc.add_text(72, 400, "[Full Ge'ez script version to be added]", 'F3', 11, 0.4)
doc.add_rect(170, 200, 272, 160, 1.5, 0.5)
doc.add_centered_text(290, "[CHART: Overview of first-order", 'F3', 10, 0.5)
doc.add_centered_text(270, "Fidel characters will go here]", 'F3', 10, 0.5)

# Fidel characters data (first order - Ge'ez form)
fidel_chars = [
    ("Ha", "ha", "Hawi", "Air", "Hawi means air/wind"),
    ("Le", "le", "Libi", "Heart", "Libi means heart"),
    ("He", "he (h)", "Hareg", "Elephant", "Hareg means elephant"),
    ("Me", "me", "May", "Water", "May means water"),
    ("Se", "se (s)", "Selam", "Peace", "Selam means peace"),
    ("Re", "re", "Risi", "Head", "Risi means head"),
    ("She", "she", "Shemesh", "Candle", "Shemesh means candle"),
    ("Qe", "qe (q)", "Qal", "Word", "Qal means word"),
    ("Be", "be", "Bet", "House", "Bet means house"),
    ("Te", "te", "Tsehay", "Sun", "Tsehay means sun"),
    ("Ne", "ne", "Nibi", "Bee", "Nibi means bee"),
    ("Ke", "ke", "Kelbi", "Dog", "Kelbi means dog"),
    ("We", "we", "Wedi", "Son/Boy", "Wedi means son or boy"),
    ("Ae", "ae (')", "Ayni", "Eye", "Ayni means eye"),
    ("Ze", "ze", "Zena", "News", "Zena means news"),
    ("Ye", "ye", "Yebab", "Heart", "Yebab means crazy/funny"),
    ("De", "de", "Dimu", "Cat", "Dimu means cat"),
    ("Ge", "ge", "Gemel", "Camel", "Gemel means camel"),
    ("Fe", "fe", "Fithi", "Justice", "Fithi means justice"),
    ("Pe", "pe", "Papos", "Grandpa", "Papos means grandpa"),
    ("Tse", "tse (ts)", "Tsebbihi", "Beautiful", "Tsebbihi means beautiful"),
    ("Tze", "tze", "Tzehay", "Sun", "Another sun variant"),
    ("Che", "che", "Chira", "Problem", "Chira means problem"),
    ("Nye", "nye", "Nay", "Of/Mine", "Nay means of or belonging to"),
    ("Gne", "gne", "Gnay", "Self", "Gnay means self"),
    ("Je", "je", "Jebena", "Coffee pot", "Jebena is the coffee pot"),
]

for i, (char_name, pronunciation, word, eng_meaning, description) in enumerate(fidel_chars):
    doc.new_page()
    # Header
    doc.add_filled_rect(0, 700, 612, 92, 0.85)
    doc.add_centered_text(760, f"Letter: {char_name}", 'F2', 20, 0)
    doc.add_centered_text(730, f"Sound: \"{pronunciation}\"", 'F1', 14, 0.2)
    doc.add_centered_text(705, f"Letter {i+1} of 26", 'F1', 11, 0.4)
    
    # Large character placeholder
    doc.add_rect(200, 520, 212, 160, 3, 0.3)
    doc.add_centered_text(610, "[FIDEL CHARACTER PLACEHOLDER]", 'F3', 14, 0.4)
    doc.add_centered_text(580, f"{char_name}", 'F2', 36, 0.6)
    doc.add_centered_text(540, "Ge'ez script character goes here", 'F3', 10, 0.5)
    
    # Word example
    doc.add_text(72, 480, f"Word: {word} = {eng_meaning}", 'F2', 14, 0)
    doc.add_text(72, 455, f"[TIGRINYA: {word}] - {description}", 'F3', 12, 0.4)
    
    # Say it
    doc.add_text(72, 420, f"Say it: \"{pronunciation}\" as in \"{word}\"", 'F2', 13, 0.2)
    doc.add_text(72, 395, "[TIGRINYA: Pronunciation guide in Ge'ez]", 'F3', 10, 0.4)
    
    # Trace area
    doc.add_text(72, 360, "Trace the letter:", 'F2', 14, 0)
    doc.add_text(72, 340, "[TIGRINYA: Fidel Tsihaf:]", 'F3', 10, 0.4)
    
    # Dotted trace boxes
    doc.add_rect(72, 240, 80, 80, 1, 0.7)
    doc.add_rect(170, 240, 80, 80, 1, 0.7)
    doc.add_rect(268, 240, 80, 80, 1, 0.7)
    doc.add_rect(366, 240, 80, 80, 1, 0.7)
    doc.add_rect(464, 240, 80, 80, 1, 0.7)
    
    # Practice lines
    doc.add_text(72, 210, "Write it on your own:", 'F1', 12, 0)
    doc.add_line(72, 180, 540, 180, 1, 0.6)
    doc.add_line(72, 140, 540, 140, 1, 0.6)
    doc.add_line(72, 100, 540, 100, 1, 0.6)

# Final review page
doc.new_page()
doc.add_centered_text(740, "GREAT JOB! YOU LEARNED THE FIDEL!", 'F2', 16, 0)
doc.add_centered_text(710, "[TIGRINYA: Tsbuq Srah! Fidel Temhirka!]", 'F3', 12, 0.4)
doc.add_centered_text(670, "Review all the letters you learned:", 'F1', 13, 0)

y = 630
col = 0
for i, (char_name, pronunciation, word, eng_meaning, desc) in enumerate(fidel_chars):
    x = 72 + col * 190
    doc.add_text(x, y, f"{char_name} ({pronunciation})", 'F1', 10, 0)
    col += 1
    if col >= 3:
        col = 0
        y -= 22

doc.add_centered_text(200, "You are learning Tigrinya! Keep practicing!", 'F2', 14, 0.2)
doc.add_centered_text(170, "[TIGRINYA: Tigrinya tmehar aleka! Qitsil!]", 'F3', 12, 0.4)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book262_Tigrinya_Alphabet_Book.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
