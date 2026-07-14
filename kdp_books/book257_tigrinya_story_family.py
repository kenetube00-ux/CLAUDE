"""Book 257: MY FAMILY - Bilingual Story Book (Tigrinya-English) Ages 3-7"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(650, "MY FAMILY", 'F2', 32, 0)
doc.add_centered_text(610, "[TIGRINYA TEXT: Sdrabet-ey]", 'F3', 16, 0.3)
doc.add_centered_text(570, "Bilingual Story Book", 'F1', 18, 0.2)
doc.add_centered_text(540, "(Tigrinya-English)", 'F1', 16, 0.3)
doc.add_centered_text(500, "Ages 3-7", 'F2', 16, 0.2)
doc.add_rect(180, 250, 252, 200, 2, 0.4)
doc.add_centered_text(340, "[ILLUSTRATION: Happy Eritrean family", 'F3', 11, 0.5)
doc.add_centered_text(320, "gathered together - parents, children, grandparents]", 'F3', 11, 0.5)
doc.add_centered_text(150, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(120, "8 Stories About Family Love", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "MY FAMILY / [TIGRINYA: Sdrabet-ey]", 'F2', 14, 0)
doc.add_text(72, 520, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 500, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 470, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 450, "For Ages: 3-7 years", 'F1', 10, 0.3)
doc.add_text(72, 430, "Language: Tigrinya & English (Bilingual)", 'F1', 10, 0.3)
doc.add_text(72, 390, "NOTE: [TIGRINYA TEXT] placeholders indicate where", 'F3', 9, 0.4)
doc.add_text(72, 375, "Ge'ez script translations will be added.", 'F3', 9, 0.4)
doc.add_text(72, 320, "Printed in the United States of America", 'F1', 10, 0.3)
doc.add_text(72, 300, "First Edition, 2025", 'F1', 10, 0.3)

# Stories data
stories = [
    ("I Love My Mom", "Nadeye Yfetwah", "about mothers",
     ["My mom wakes up early every morning to take care of our family.",
      "She makes the best injera and always gives me a big hug.",
      "When I am sad, my mom sings to me and I feel better.",
      "She teaches me to be kind, brave, and always tell the truth.",
      "I love my mom more than all the stars in the sky!"]),
    ("My Father is Strong", "Aboy Hayli Eyu", "about fathers",
     ["My father is the strongest person I know.",
      "He lifts me high up on his shoulders so I can see everything.",
      "He works hard every day so our family has everything we need.",
      "At night, he tells me stories about Eritrea and our ancestors.",
      "My father makes me feel safe and loved every single day."]),
    ("Playing with My Sister", "Msmsar ms Habtey", "siblings",
     ["My sister and I love to play together after school.",
      "Sometimes we run in the yard and sometimes we play inside.",
      "When she falls down, I help her up and give her a hug.",
      "We share our toys and take turns choosing the games we play.",
      "Having a sister is like having a best friend forever!"]),
    ("Grandma's Stories", "Tsirhi Akhoy-aboy", "grandparents",
     ["My grandma knows the best stories in the whole world.",
      "She tells me about life in Eritrea when she was young.",
      "Her voice is soft and warm like a cozy blanket.",
      "She teaches me Tigrinya words and I try to say them right.",
      "Grandma says I am her sunshine and I say she is my star!"]),
    ("Family Dinner Together", "Dirar Sdra-bet Buhada", "togetherness",
     ["Every evening, our whole family sits together for dinner.",
      "We eat injera with our hands and share from one big plate.",
      "Mom and Dad ask us about our day at school.",
      "We laugh and tell stories while we eat delicious food.",
      "Eating together makes our family strong and happy!"]),
    ("Helping at Home", "Abi-Gebi Mhgaz", "responsibility",
     ["I like to help my family with jobs around the house.",
      "I make my bed every morning all by myself.",
      "I help set the table and put my toys away after playing.",
      "Mom smiles and says I am such a good helper.",
      "When we all help, our home is clean and everyone is happy!"]),
    ("A New Baby Brother", "Hadish Haw", "new sibling",
     ["Today our family got bigger - we have a new baby brother!",
      "He is so tiny and soft. I hold him very carefully.",
      "He cries sometimes but Dad says that is how babies talk.",
      "I will be the best big brother and protect him always.",
      "Our family is now even more full of love than before!"]),
    ("Our Family is Special", "Sdrabet-na Fltiy Eya", "celebration",
     ["Every family is different and that is wonderful.",
      "Our family speaks Tigrinya and English - we know two languages!",
      "We have special traditions that make us who we are.",
      "We love each other, help each other, and laugh together.",
      "Our family is the most special family in the world!"]),
]

# Generate story pages (3 pages per story: story + Tigrinya + activity)
for i, (title, tig_title, theme, sentences) in enumerate(stories):
    # Story page 1
    doc.new_page()
    doc.add_filled_rect(0, 720, 612, 72, 0.88)
    doc.add_centered_text(745, f"Story {i+1}: {title}", 'F2', 18, 0)
    doc.add_centered_text(720, f"[TIGRINYA TEXT: {tig_title}]", 'F3', 12, 0.4)
    
    doc.add_rect(170, 520, 272, 170, 1, 0.6)
    doc.add_centered_text(610, f"[ILLUSTRATION: {theme}]", 'F3', 10, 0.5)
    
    y = 490
    for sent in sentences:
        doc.add_text(72, y, sent, 'F4', 13, 0)
        y -= 28
    
    y -= 15
    doc.add_line(72, y+10, 540, y+10, 0.5, 0.7)
    doc.add_text(72, y, "[TIGRINYA TRANSLATION:", 'F3', 11, 0.3); y -= 18
    doc.add_text(72, y, f"Complete Tigrinya translation of '{title}' story.", 'F3', 10, 0.4); y -= 18
    doc.add_text(72, y, "Ge'ez script version to be added by Daniel.]", 'F3', 10, 0.4); y -= 35
    
    doc.add_text(72, y, "What do you love about your family?", 'F2', 13, 0.2); y -= 20
    doc.add_text(72, y, "[TIGRINYA: Nsdra-betkha/betki ehnta zfetwo?]", 'F3', 10, 0.4); y -= 30
    doc.add_line(72, y, 540, y, 0.5, 0.6); y -= 25
    doc.add_line(72, y, 540, y, 0.5, 0.6)
    
    # Activity/drawing page
    doc.new_page()
    doc.add_centered_text(730, f"Draw: {title}", 'F2', 16, 0.2)
    doc.add_centered_text(705, "Draw a picture of your family doing this activity!", 'F1', 13, 0)
    doc.add_centered_text(680, "[TIGRINYA: Sdrabet-kha/ki sirAa nsali!]", 'F3', 10, 0.4)
    doc.add_rect(72, 300, 468, 350, 2, 0.5)
    doc.add_centered_text(475, "Your Drawing Here", 'F1', 14, 0.6)
    doc.add_text(72, 270, "My family makes me happy because:", 'F2', 12, 0)
    doc.add_text(72, 250, "[TIGRINYA: Sdrabet-ey thaw-haw zbleqani sabab:]", 'F3', 10, 0.4)
    doc.add_line(72, 220, 540, 220, 0.5, 0.6)
    doc.add_line(72, 195, 540, 195, 0.5, 0.6)

# Final page: Family tree activity
doc.new_page()
doc.add_centered_text(730, "MY FAMILY TREE", 'F2', 20, 0)
doc.add_centered_text(700, "[TIGRINYA: Zegol Sdrabet-ey]", 'F3', 14, 0.4)
doc.add_centered_text(670, "Draw or write the names of your family members!", 'F1', 13, 0)
doc.add_rect(220, 580, 172, 60, 1.5, 0.3)
doc.add_centered_text(610, "Grandparents", 'F1', 11, 0.3)
doc.add_rect(120, 460, 172, 60, 1.5, 0.3)
doc.add_centered_text(490, "Mom", 'F1', 11, 0.3)
doc.add_rect(320, 460, 172, 60, 1.5, 0.3)
doc.add_centered_text(490, "Dad", 'F1', 11, 0.3)
doc.add_line(306, 580, 206, 520, 1, 0.5)
doc.add_line(306, 580, 406, 520, 1, 0.5)
doc.add_rect(72, 320, 130, 60, 1.5, 0.3)
doc.add_rect(240, 320, 130, 60, 1.5, 0.3)
doc.add_rect(410, 320, 130, 60, 1.5, 0.3)
doc.add_centered_text(350, "Me & My Siblings", 'F1', 11, 0.3)
doc.add_centered_text(200, "I love my family! / [TIGRINYA: Nsdrabet-ey yefetwom!]", 'F2', 13, 0.2)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book257_Tigrinya_Family_Stories.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
