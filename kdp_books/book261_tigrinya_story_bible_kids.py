"""Book 261: BIBLE STORIES FOR CHILDREN - Bilingual (Tigrinya-English) Ages 4-8"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(660, "BIBLE STORIES FOR CHILDREN", 'F2', 26, 0)
doc.add_centered_text(620, "[TIGRINYA TEXT: Tsirhi Metshaf Qiddus ni Qolaat]", 'F3', 13, 0.3)
doc.add_centered_text(570, "Bilingual (Tigrinya-English)", 'F1', 16, 0.2)
doc.add_centered_text(540, "Ages 4-8", 'F2', 16, 0.2)
doc.add_rect(180, 280, 252, 200, 2, 0.4)
doc.add_centered_text(380, "[ILLUSTRATION: Children reading", 'F3', 11, 0.5)
doc.add_centered_text(360, "the Bible together with joy]", 'F3', 11, 0.5)
doc.add_centered_text(180, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(150, "10 Beloved Bible Stories Simply Told", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "BIBLE STORIES FOR CHILDREN", 'F2', 14, 0)
doc.add_text(72, 520, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 500, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 470, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 450, "For Ages: 4-8 years", 'F1', 10, 0.3)
doc.add_text(72, 430, "Language: Tigrinya & English (Bilingual)", 'F1', 10, 0.3)
doc.add_text(72, 400, "Scripture quotations from the World English Bible (WEB).", 'F1', 10, 0.3)
doc.add_text(72, 370, "NOTE: [TIGRINYA TEXT] placeholders indicate where", 'F3', 9, 0.4)
doc.add_text(72, 355, "Ge'ez script translations will be added.", 'F3', 9, 0.4)
doc.add_text(72, 300, "First Edition, 2025", 'F1', 10, 0.3)

stories = [
    ("God Made the World", "Amlak Alem Fetiruwa", "Creation",
     ["In the beginning, God made the sky and the earth.",
      "He made the sun, moon, stars, and all the animals.",
      "He made the flowers, trees, and the beautiful ocean.",
      "Then God made people - He made you and me!",
      "God looked at everything He made and said, 'It is very good!'"],
     "Genesis 1:31 - God saw everything that He had made, and it was very good.",
     "What is your favorite thing God made?"),
    ("Noah and the Big Boat", "Noh-n Abi Merkeb-n", "Noah's Ark",
     ["God told Noah to build a very big boat called an ark.",
      "Noah brought two of every animal onto the boat.",
      "Then it rained for forty days and forty nights!",
      "But Noah, his family, and all the animals were safe inside.",
      "God put a rainbow in the sky as a promise of His love."],
     "Genesis 9:13 - I set my rainbow in the cloud, and it will be a sign.",
     "Can you name the animals on the boat?"),
    ("Abraham's Big Journey", "Abrahamen Abi Gufho-n", "Faith",
     ["God told Abraham to go to a new land far away.",
      "Abraham trusted God even though he did not know the way.",
      "God promised Abraham a family as many as the stars!",
      "Abraham believed God and started his big journey.",
      "God always keeps His promises to those who trust Him."],
     "Genesis 15:6 - He believed in the Lord, and He credited it to him.",
     "Have you ever trusted someone to lead you?"),
    ("Baby Moses in the River", "Hitsanat Muse ab Ruba", "Protection",
     ["Baby Moses' mom put him in a basket on the river to keep him safe.",
      "His big sister Miriam watched over him from the tall grass.",
      "A princess found the baby and decided to take care of him.",
      "God protected baby Moses because He had big plans for him!",
      "God always watches over us and keeps us safe."],
     "Exodus 2:10 - She named him Moses, 'Because I drew him out of the water.'",
     "Who watches over you and keeps you safe?"),
    ("David and the Giant", "Dawit-n Goliath-n", "Courage",
     ["A giant named Goliath was scaring everyone in the land.",
      "Young David was small but he was very brave.",
      "David said, 'God will help me!' and picked up five stones.",
      "With just one small stone and God's help, David won!",
      "With God's help, we can face any problem, no matter how big."],
     "1 Samuel 17:45 - David said, 'I come to you in the name of the Lord.'",
     "What makes you feel brave?"),
    ("Daniel and the Lions", "Dani-El-n Anbessa-tat-n", "Trust",
     ["Daniel loved God and prayed every single day.",
      "Bad men threw Daniel into a den full of hungry lions!",
      "But Daniel was not afraid because he trusted God.",
      "God sent an angel to close the lions' mouths!",
      "Daniel was safe because he trusted God completely."],
     "Daniel 6:22 - My God sent His angel and shut the lions' mouths.",
     "What do you pray about?"),
    ("Jonah and the Big Fish", "Yonas-n Abi Asa-n", "Obedience",
     ["God asked Jonah to go help the people of Nineveh.",
      "But Jonah said 'No!' and ran away on a boat.",
      "A big storm came and a huge fish swallowed Jonah!",
      "Inside the fish, Jonah prayed and said 'Sorry, God!'",
      "God saved Jonah and he went to help the people, just as God asked."],
     "Jonah 2:1 - Then Jonah prayed to the Lord his God from the fish's belly.",
     "Why is it important to listen and obey?"),
    ("Baby Jesus is Born", "Hitsanat Yesus Tewelidyu", "Christmas",
     ["Mary and Joseph traveled to a little town called Bethlehem.",
      "There was no room at the inn, so they stayed in a stable.",
      "That night, baby Jesus was born and laid in a manger!",
      "Angels sang in the sky and shepherds came to see Him.",
      "Baby Jesus came to bring love and joy to the whole world!"],
     "Luke 2:11 - For there is born to you today a Savior, who is Christ the Lord.",
     "How does your family celebrate Jesus' birthday?"),
    ("Jesus Loves the Children", "Yesus ni Qolaat Yfetuwom", "Love",
     ["One day, families brought their children to see Jesus.",
      "Some people said, 'Go away! Jesus is too busy for children!'",
      "But Jesus said, 'No! Let the children come to me!'",
      "He held the children, blessed them, and loved them.",
      "Jesus loves every child - He loves YOU very much!"],
     "Mark 10:14 - Let the little children come to me, and do not hinder them.",
     "How do you know Jesus loves you?"),
    ("Jesus is Alive!", "Yesus Tensieu!", "Easter",
     ["Jesus died on the cross because He loves us so much.",
      "His friends were very sad and put Him in a tomb.",
      "But on the third day, something amazing happened!",
      "The tomb was empty - Jesus was alive again!",
      "Jesus is alive forever and He is with us always!"],
     "Matthew 28:6 - He is not here, for He has risen!",
     "What makes Easter special to you?"),
]

for i, (title, tig_title, theme, sentences, verse, question) in enumerate(stories):
    # Story page
    doc.new_page()
    doc.add_filled_rect(0, 720, 612, 72, 0.85)
    doc.add_centered_text(745, f"Story {i+1}: {title}", 'F2', 18, 0)
    doc.add_centered_text(720, f"[TIGRINYA TEXT: {tig_title}]", 'F3', 12, 0.4)
    
    doc.add_rect(170, 520, 272, 160, 1, 0.6)
    doc.add_centered_text(600, f"[ILLUSTRATION: {theme} scene]", 'F3', 10, 0.5)
    
    y = 490
    for sent in sentences:
        doc.add_text(72, y, sent, 'F4', 13, 0)
        y -= 26
    
    y -= 10
    doc.add_line(72, y+8, 540, y+8, 0.5, 0.7)
    doc.add_text(72, y, "[TIGRINYA TRANSLATION:", 'F3', 11, 0.3); y -= 16
    doc.add_text(72, y, f"Full Ge'ez script translation of '{title}' story.]", 'F3', 10, 0.4); y -= 30
    
    # Key verse
    doc.add_filled_rect(60, y-35, 492, 45, 0.92)
    doc.add_text(72, y, "Key Verse:", 'F2', 11, 0)
    doc.add_text(72, y-18, verse[:75], 'F4', 10, 0.2)
    if len(verse) > 75:
        doc.add_text(72, y-33, verse[75:], 'F4', 10, 0.2)
    
    # Activity page
    doc.new_page()
    doc.add_centered_text(730, f"What Did You Learn?", 'F2', 18, 0.2)
    doc.add_centered_text(700, f"[TIGRINYA: Ehnta Eyu Ztemelkutwo?]", 'F3', 12, 0.4)
    doc.add_text(72, 660, question, 'F2', 14, 0)
    doc.add_text(72, 635, "[TIGRINYA TRANSLATION PLACEHOLDER]", 'F3', 10, 0.4)
    doc.add_line(72, 600, 540, 600, 0.5, 0.6)
    doc.add_line(72, 575, 540, 575, 0.5, 0.6)
    
    doc.add_text(72, 540, "Draw your favorite part of this story:", 'F2', 13, 0)
    doc.add_rect(72, 250, 468, 270, 2, 0.5)
    doc.add_centered_text(380, "Your Drawing Here", 'F1', 14, 0.6)
    
    doc.add_text(72, 220, "My prayer today:", 'F2', 12, 0)
    doc.add_text(72, 200, "[TIGRINYA: Tsalot-ey nayharda:]", 'F3', 10, 0.4)
    doc.add_line(72, 175, 540, 175, 0.5, 0.6)
    doc.add_line(72, 150, 540, 150, 0.5, 0.6)

# Final page: Memory verses
doc.new_page()
doc.add_centered_text(740, "BIBLE VERSES TO REMEMBER", 'F2', 18, 0)
doc.add_centered_text(710, "[TIGRINYA: Tsehuf Qiddus Zzkker]", 'F3', 12, 0.4)
y = 660
short_verses = [
    "God is love. - 1 John 4:8",
    "Be kind to one another. - Eph. 4:32",
    "The Lord is my shepherd. - Psalm 23:1",
    "I can do all things through Christ. - Phil. 4:13",
    "Trust in the Lord. - Proverbs 3:5",
]
for v in short_verses:
    doc.add_filled_rect(60, y-8, 492, 35, 0.92)
    doc.add_text(72, y, v, 'F4', 12, 0)
    doc.add_text(72, y-18, "[TIGRINYA TRANSLATION PLACEHOLDER]", 'F3', 9, 0.4)
    y -= 55

doc.add_centered_text(350, "God loves you! / [TIGRINYA: Amlak yfetukha!]", 'F2', 16, 0.2)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book261_Tigrinya_Bible_Kids_Stories.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
