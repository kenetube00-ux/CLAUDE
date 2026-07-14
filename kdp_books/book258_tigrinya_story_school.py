"""Book 258: MY FIRST DAY AT SCHOOL - Bilingual Story Book (Tigrinya-English) Ages 4-8"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(650, "MY FIRST DAY AT SCHOOL", 'F2', 26, 0)
doc.add_centered_text(610, "[TIGRINYA TEXT: Qadamay Mealtey ab Timhirti]", 'F3', 13, 0.3)
doc.add_centered_text(570, "Bilingual Story Book (Tigrinya-English)", 'F1', 16, 0.2)
doc.add_centered_text(540, "Ages 4-8", 'F2', 16, 0.2)
doc.add_rect(180, 280, 252, 200, 2, 0.4)
doc.add_centered_text(380, "[ILLUSTRATION: Child with backpack", 'F3', 11, 0.5)
doc.add_centered_text(360, "walking to school, excited and happy]", 'F3', 11, 0.5)
doc.add_centered_text(180, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(150, "8 Stories About School Adventures", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "MY FIRST DAY AT SCHOOL", 'F2', 14, 0)
doc.add_text(72, 520, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 500, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 470, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 450, "For Ages: 4-8 years", 'F1', 10, 0.3)
doc.add_text(72, 430, "Language: Tigrinya & English (Bilingual)", 'F1', 10, 0.3)
doc.add_text(72, 390, "NOTE: [TIGRINYA TEXT] placeholders indicate where", 'F3', 9, 0.4)
doc.add_text(72, 375, "Ge'ez script translations will be added.", 'F3', 9, 0.4)
doc.add_text(72, 320, "First Edition, 2025", 'F1', 10, 0.3)

stories = [
    ("Getting Ready for School", "Mdslab nTimhirti", "preparation",
     ["Today is my first day of school and I am so excited!",
      "I put on my new clothes and pack my bag carefully.",
      "Mom makes me a good breakfast to give me energy.",
      "I brush my teeth and comb my hair neatly.",
      "I am ready! Let's go to school!"]),
    ("Meeting My Teacher", "Misrah Ms Memhir-ey", "respect",
     ["My teacher has a big smile and a kind voice.",
      "She says, 'Welcome to school! I am happy you are here.'",
      "She shows us where to sit and where to put our things.",
      "My teacher is patient and helps us learn new things every day.",
      "I respect my teacher because she helps me grow."]),
    ("Making New Friends", "Mftsam Hadishti Azmat", "friendship",
     ["At school, I see many other children my age.",
      "A boy named Abel smiles at me and says hello.",
      "We play together at break time and share our snacks.",
      "By the end of the day, I have three new friends!",
      "School is wonderful because I get to make friends."]),
    ("Learning the Alphabet", "Mmlad Fidel", "education",
     ["Today we are learning the alphabet letters.",
      "My teacher writes big letters on the board for us to see.",
      "A, B, C, D... I try to write them in my notebook.",
      "It is hard at first, but I keep practicing every day.",
      "Soon I will be able to read and write all by myself!"]),
    ("Playtime Fun", "Gize Tsewta", "play",
     ["The bell rings and it is time for break!",
      "We run outside to the playground with big smiles.",
      "Some children play on the swings, others kick a ball.",
      "I like to run and play catch with my new friends.",
      "Playtime makes school even more fun!"]),
    ("Sharing with Others", "Mkataf Ms Kalot", "generosity",
     ["Today I brought two pencils to school.",
      "My friend Miriam forgot her pencil at home and looked sad.",
      "I gave her one of my pencils and she smiled so big!",
      "Sharing makes other people happy and it makes me happy too.",
      "When we share, everyone has what they need."]),
    ("My Favorite Subject", "Zfetwo Timhirt-ey", "interests",
     ["At school, we learn many different things.",
      "We learn numbers, letters, science, and art.",
      "My favorite is art because I love to draw and color!",
      "My friend likes math because he loves counting.",
      "Everyone has something they are good at and enjoy!"]),
    ("I Can Do It!", "Ikhlyo Eyen!", "confidence",
     ["Sometimes school feels hard and I want to give up.",
      "The math problem looks too difficult for me to solve.",
      "But my teacher says, 'Try again. I believe in you!'",
      "I take a deep breath, try one more time, and I get it right!",
      "I can do hard things when I believe in myself!"]),
]

for i, (title, tig_title, theme, sentences) in enumerate(stories):
    # Story page
    doc.new_page()
    doc.add_filled_rect(0, 720, 612, 72, 0.88)
    doc.add_centered_text(745, f"Story {i+1}: {title}", 'F2', 18, 0)
    doc.add_centered_text(720, f"[TIGRINYA TEXT: {tig_title}]", 'F3', 12, 0.4)
    
    doc.add_rect(170, 520, 272, 160, 1, 0.6)
    doc.add_centered_text(600, f"[ILLUSTRATION: {theme} scene]", 'F3', 10, 0.5)
    
    y = 490
    for sent in sentences:
        doc.add_text(72, y, sent, 'F4', 13, 0)
        y -= 28

    y -= 10
    doc.add_line(72, y+10, 540, y+10, 0.5, 0.7)
    doc.add_text(72, y, "[TIGRINYA TRANSLATION:", 'F3', 11, 0.3); y -= 18
    doc.add_text(72, y, f"Full translation of '{title}' in Ge'ez script.]", 'F3', 10, 0.4); y -= 40
    
    # Activity page
    doc.new_page()
    doc.add_centered_text(730, f"Activity: {title}", 'F2', 16, 0.2)
    if i == 0:
        doc.add_text(72, 690, "Circle the things you need for school:", 'F1', 13, 0)
        items = ["Backpack", "Pencil", "Notebook", "Lunchbox", "Eraser"]
        y = 650
        for item in items:
            doc.add_rect(72, y-5, 20, 20, 1, 0.5)
            doc.add_text(100, y, f"{item} / [TIGRINYA PLACEHOLDER]", 'F1', 12, 0)
            y -= 35
    elif i == 3:
        doc.add_text(72, 690, "Trace the letters:", 'F1', 13, 0)
        letters = "A B C D E F G H I J"
        doc.add_text(72, 640, letters, 'F2', 24, 0.7)
        doc.add_text(72, 590, "[TIGRINYA: Trace Fidel characters here]", 'F3', 12, 0.4)
    else:
        doc.add_text(72, 690, "Draw your favorite part of this story!", 'F1', 13, 0)
        doc.add_text(72, 665, "[TIGRINYA TEXT: Zfetukha kfli sirAa!]", 'F3', 10, 0.4)
    
    doc.add_rect(72, 300, 468, 320, 2, 0.5)
    doc.add_centered_text(460, "Your Drawing/Activity Here", 'F1', 14, 0.6)
    doc.add_text(72, 270, "I love school because:", 'F2', 12, 0)
    doc.add_line(72, 240, 540, 240, 0.5, 0.6)
    doc.add_line(72, 215, 540, 215, 0.5, 0.6)

# Final page: School words vocabulary
doc.new_page()
doc.add_centered_text(730, "SCHOOL WORDS / [TIGRINYA: Qalat Timhirti]", 'F2', 16, 0)
vocab = [("School", "Timhirti"), ("Teacher", "Memhir"), ("Book", "Metshaf"),
         ("Pencil", "Irsas"), ("Friend", "Azmi"), ("Learn", "Memlad"),
         ("Read", "Manbab"), ("Write", "Mitsihaf")]
y = 670
for eng, tig in vocab:
    doc.add_text(72, y, eng, 'F2', 14, 0)
    doc.add_text(200, y, f"[TIGRINYA: {tig}]", 'F3', 13, 0.3)
    doc.add_line(72, y-12, 540, y-12, 0.5, 0.8)
    y -= 45

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book258_Tigrinya_School_Stories.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
