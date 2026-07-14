"""Book 264: ERITREAN FOOD - Bilingual Food Book (Tigrinya-English) Ages 3-7"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(660, "ERITREAN FOOD", 'F2', 32, 0)
doc.add_centered_text(620, "[TIGRINYA TEXT: Megibi Ertra]", 'F3', 16, 0.3)
doc.add_centered_text(570, "Bilingual Food Book", 'F1', 18, 0.2)
doc.add_centered_text(540, "(Tigrinya-English)", 'F1', 16, 0.3)
doc.add_centered_text(500, "Ages 3-7", 'F2', 16, 0.2)
doc.add_rect(180, 270, 252, 180, 2, 0.4)
doc.add_centered_text(370, "[ILLUSTRATION: Traditional Eritrean", 'F3', 11, 0.5)
doc.add_centered_text(350, "food spread on mesob/basket]", 'F3', 11, 0.5)
doc.add_centered_text(170, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(140, "Discover Delicious Eritrean Foods!", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "ERITREAN FOOD / [TIGRINYA: Megibi Ertra]", 'F2', 14, 0)
doc.add_text(72, 520, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 500, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 470, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 450, "For Ages: 3-7 years", 'F1', 10, 0.3)
doc.add_text(72, 430, "Language: Tigrinya & English (Bilingual)", 'F1', 10, 0.3)
doc.add_text(72, 390, "NOTE: [TIGRINYA TEXT] placeholders indicate where", 'F3', 9, 0.4)
doc.add_text(72, 375, "Ge'ez script translations will be added.", 'F3', 9, 0.4)
doc.add_text(72, 320, "First Edition, 2025", 'F1', 10, 0.3)

# Introduction page
doc.new_page()
doc.add_centered_text(730, "ERITREAN FOOD IS SPECIAL!", 'F2', 18, 0)
doc.add_centered_text(700, "[TIGRINYA: Megibi Ertra Fliuy Eyu!]", 'F3', 12, 0.4)
doc.add_text(72, 650, "Eritrean food is one of the most delicious in the world!", 'F4', 14, 0)
doc.add_text(72, 620, "We eat together from one big plate as a family.", 'F4', 14, 0)
doc.add_text(72, 590, "We use our hands to eat - no forks or spoons needed!", 'F4', 14, 0)
doc.add_text(72, 560, "Our food brings people together with love and joy.", 'F4', 14, 0)
doc.add_text(72, 520, "[TIGRINYA: Full translation of introduction]", 'F3', 11, 0.4)
doc.add_text(72, 500, "[Ge'ez script version to be added by Daniel]", 'F3', 11, 0.4)
doc.add_rect(170, 280, 272, 180, 1.5, 0.5)
doc.add_centered_text(380, "[ILLUSTRATION: Family eating together", 'F3', 10, 0.5)
doc.add_centered_text(360, "from a shared plate on a mesob]", 'F3', 10, 0.5)

# Food data
foods = [
    ("Injera", "Injera", "Injera is our special bread.",
     ["Injera is a big, soft, spongy flatbread.",
      "It is made from a special grain called teff.",
      "We put all our food on top of the injera and eat together!"],
     "Injera is eaten every day in Eritrea. It takes 3 days to make!",
     "spongy round flatbread"),
    ("Tsebhi", "Tsebhi", "Tsebhi is a yummy stew.",
     ["Tsebhi is a delicious stew made with meat and spices.",
      "It is cooked slowly until it is tender and full of flavor.",
      "We scoop it up with pieces of injera - so tasty!"],
     "There are many types of tsebhi - chicken (dorho), beef, and lamb!",
     "bowl of rich stew"),
    ("Shiro", "Shiro", "Shiro is made from chickpeas.",
     ["Shiro is a smooth, creamy stew made from ground chickpeas.",
      "It is spiced with berbere and has a warm, comforting taste.",
      "Many children love shiro because it is smooth and mild."],
     "Shiro is one of the most popular foods during fasting days.",
     "smooth chickpea stew"),
    ("Zigni", "Zigni", "Zigni is spicy and delicious!",
     ["Zigni is a spicy beef stew that is very popular.",
      "It is made with lots of berbere spice and tomatoes.",
      "The meat is cooked until it is soft and the sauce is thick."],
     "Zigni uses berbere spice, which is a special Eritrean spice mix!",
     "spicy red stew with meat"),
    ("Hilbet", "Hilbet", "Hilbet is smooth and tasty.",
     ["Hilbet is made from lentils and is very smooth.",
      "It has a mild, nice taste that children enjoy.",
      "It is often served as a side dish with injera."],
     "Hilbet is very healthy because lentils have lots of protein!",
     "smooth lentil dip"),
    ("Fool", "Ful", "Fool is great for breakfast!",
     ["Fool is made from fava beans cooked until soft.",
      "We eat it for breakfast with bread and sometimes eggs.",
      "It gives us energy to start our day strong!"],
     "Fool is a popular breakfast across East Africa and the Middle East!",
     "bowl of mashed fava beans"),
    ("Suwa", "Suwa", "Suwa is a traditional drink.",
     ["Suwa is a traditional homemade drink from Eritrea.",
      "It is made from grains and has been made for hundreds of years.",
      "Adults drink suwa at celebrations and special gatherings."],
     "For kids: Parents can make a non-alcoholic version as a special treat!",
     "traditional clay pot with drink"),
    ("Himbasha", "Himbasha", "Himbasha is celebration bread!",
     ["Himbasha is a special sweet bread we bake for celebrations.",
      "It has beautiful patterns on top and a slightly sweet taste.",
      "We share himbasha at holidays, weddings, and happy gatherings."],
     "Himbasha has a beautiful design scored on top before baking!",
     "round decorated sweet bread"),
    ("Firfir", "Firfir", "Firfir is made with injera pieces.",
     ["Firfir is made by tearing injera into small pieces.",
      "The pieces are mixed with spicy sauce and sometimes butter.",
      "It is a great way to use leftover injera - nothing goes to waste!"],
     "Firfir means 'to crumble' in Tigrinya - because we crumble the injera!",
     "torn injera pieces in sauce"),
    ("Tea with Milk", "Shahi bi Halib", "We love our sweet tea!",
     ["Eritrean tea is made with milk, sugar, and spices.",
      "It smells wonderful and tastes warm and sweet.",
      "We drink it in the morning and when friends come to visit."],
     "Tea time is important in Eritrea - it brings people together!",
     "cup of milky spiced tea"),
]

for food_eng, food_tig, tagline, sentences, cultural_note, illustration in foods:
    # Food page
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.85)
    doc.add_centered_text(755, food_eng.upper(), 'F2', 28, 0)
    doc.add_centered_text(720, f"[TIGRINYA: {food_tig}]", 'F3', 16, 0.3)
    doc.add_centered_text(700, "[FIDEL CHARACTER PLACEHOLDER]", 'F3', 10, 0.5)
    
    doc.add_centered_text(665, tagline, 'F4', 16, 0)
    doc.add_centered_text(640, "[TIGRINYA TRANSLATION PLACEHOLDER]", 'F3', 11, 0.4)
    
    # Illustration
    doc.add_rect(180, 460, 252, 150, 2, 0.4)
    doc.add_centered_text(540, f"[ILLUSTRATION: {illustration}]", 'F3', 10, 0.5)
    
    # Description sentences
    y = 430
    for sent in sentences:
        doc.add_text(72, y, sent, 'F4', 13, 0)
        y -= 25
    
    y -= 10
    doc.add_text(72, y, "[TIGRINYA: Full translation in Ge'ez script]", 'F3', 11, 0.4)
    y -= 30
    
    # Cultural note
    doc.add_filled_rect(60, y-25, 492, 40, 0.92)
    doc.add_text(72, y, "For Parents:", 'F2', 10, 0.2)
    doc.add_text(72, y-15, cultural_note, 'F1', 10, 0.3)
    y -= 50
    
    # Activity
    doc.add_text(72, y, "Have you tried this? Draw it!", 'F2', 13, 0)
    doc.add_text(72, y-20, "[TIGRINYA: Ftinim-do? Sirahu!]", 'F3', 10, 0.4)
    doc.add_rect(72, y-120, 250, 80, 2, 0.5)

# Food vocabulary page
doc.new_page()
doc.add_centered_text(740, "FOOD WORDS / [TIGRINYA: Qalat Megibi]", 'F2', 18, 0)
y = 680
food_vocab = [("Delicious", "Tmuy"), ("Hungry", "Tsemey"), ("Eat", "Mblai"),
              ("Cook", "Mstay"), ("Share", "Mkataf"), ("Family", "Sdra-bet"),
              ("Bread", "Bani"), ("Spicy", "Mririr"), ("Sweet", "Miquy"), ("Drink", "Mstay")]
for eng, tig in food_vocab:
    doc.add_text(72, y, eng, 'F2', 13, 0)
    doc.add_text(200, y, f"[TIGRINYA: {tig}]", 'F3', 12, 0.4)
    doc.add_line(72, y-12, 540, y-12, 0.5, 0.8)
    y -= 40

doc.add_centered_text(230, "Enjoy your Eritrean food! / [TIGRINYA: Megibi Ertra thmem!]", 'F2', 13, 0.2)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book264_Tigrinya_Food_Book.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
