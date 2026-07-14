"""Book 265: GOOD MANNERS - Bilingual Story Book (Tigrinya-English) Ages 3-7"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(660, "GOOD MANNERS", 'F2', 32, 0)
doc.add_centered_text(620, "[TIGRINYA TEXT: Tsbuq Bahli]", 'F3', 16, 0.3)
doc.add_centered_text(570, "Bilingual Story Book", 'F1', 18, 0.2)
doc.add_centered_text(540, "(Tigrinya-English)", 'F1', 16, 0.3)
doc.add_centered_text(500, "Ages 3-7", 'F2', 16, 0.2)
doc.add_rect(180, 270, 252, 180, 2, 0.4)
doc.add_centered_text(370, "[ILLUSTRATION: Polite child", 'F3', 11, 0.5)
doc.add_centered_text(350, "showing good manners]", 'F3', 11, 0.5)
doc.add_centered_text(170, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(140, "10 Stories About Being Kind and Polite", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "GOOD MANNERS / [TIGRINYA: Tsbuq Bahli]", 'F2', 14, 0)
doc.add_text(72, 520, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 500, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 470, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 450, "For Ages: 3-7 years", 'F1', 10, 0.3)
doc.add_text(72, 430, "Language: Tigrinya & English (Bilingual)", 'F1', 10, 0.3)
doc.add_text(72, 390, "NOTE: [TIGRINYA TEXT] placeholders indicate where", 'F3', 9, 0.4)
doc.add_text(72, 375, "Ge'ez script translations will be added.", 'F3', 9, 0.4)
doc.add_text(72, 320, "First Edition, 2025", 'F1', 10, 0.3)

# Manners stories data
manners = [
    ("Saying Please", "Bejakha/Bejakhi",
     ["Abe wants a glass of water from his mom.",
      "He remembers to say, 'Please may I have water?'",
      "Mom smiles and gives him a big glass of cold water.",
      "Saying 'please' shows respect and makes people happy to help."],
     "Always say 'please' when you ask for something!",
     "asking politely"),
    ("Saying Thank You", "Yekeneyeley",
     ["Grandma gives Sara a beautiful new book.",
      "Sara says, 'Thank you, Grandma! I love it!'",
      "Grandma hugs Sara and feels happy that Sara is grateful.",
      "Saying 'thank you' shows we appreciate what others do for us."],
     "Say 'thank you' whenever someone does something nice!",
     "receiving a gift gratefully"),
    ("Sharing is Caring", "Mkataf Mihur Eyu",
     ["Daniel has a big box of crayons at school.",
      "His friend Yonas does not have any crayons today.",
      "Daniel says, 'Here, you can use my crayons!'",
      "Sharing makes both friends happy and shows we care."],
     "When you share, everyone is happier!",
     "children sharing toys"),
    ("Waiting Your Turn", "Terai-kha Tsennah",
     ["The children line up for the slide at the playground.",
      "Miriam wants to go first, but others were there before her.",
      "She waits patiently for her turn, and soon it is time!",
      "Waiting our turn is fair and shows respect for others."],
     "Be patient and wait your turn!",
     "children in a queue"),
    ("Being Kind to Others", "Nkalot Lebamat Mzaw",
     ["Abe sees a new boy at school who looks lonely.",
      "Abe walks over and says, 'Hi! Do you want to play with us?'",
      "The new boy smiles big and says, 'Yes, thank you!'",
      "Being kind to others makes the world a better place."],
     "Look for someone who needs a friend today!",
     "child welcoming a new friend"),
    ("Listening When Others Speak", "Ab Gize Kalot Zzerarbu Msmma'",
     ["When Dad is talking, Sara puts down her toy and looks at him.",
      "She listens carefully to what Dad is saying.",
      "Dad says, 'Thank you for listening so well, Sara!'",
      "Good listening shows we care about what others say."],
     "Listen with your eyes and ears!",
     "child listening attentively"),
    ("Saying Sorry", "Yiqirta",
     ["Dawit accidentally bumps into his sister and she falls down.",
      "He quickly helps her up and says, 'I am sorry! Are you okay?'",
      "His sister smiles and says, 'It is okay, I know it was an accident.'",
      "Saying sorry when we make mistakes helps fix things."],
     "When you make a mistake, say sorry right away!",
     "child apologizing"),
    ("Respecting Elders", "Kibri ni Zeygbat",
     ["When Grandpa enters the room, Abe stands up to greet him.",
      "He says, 'Good morning, Grandpa! How are you today?'",
      "He offers Grandpa his seat and brings him tea.",
      "In Eritrean culture, we always show great respect to our elders."],
     "Always greet elders first and show them respect!",
     "child greeting an elder"),
    ("Helping Others", "Nkalot Mhgaz",
     ["Mom is carrying heavy bags from the market.",
      "Sara runs to help and says, 'Let me carry one, Mom!'",
      "Mom is so happy and says, 'What a good helper you are!'",
      "Helping others without being asked shows a kind heart."],
     "Look for ways to help your family every day!",
     "child helping carry things"),
    ("Being Honest", "Haqenet",
     ["Daniel accidentally breaks a cup while playing inside.",
      "He could hide it, but he goes to tell Dad what happened.",
      "'Dad, I am sorry. I broke the cup by accident.'",
      "Dad says, 'Thank you for being honest. That took courage.'"],
     "Always tell the truth, even when it is hard!",
     "child telling the truth"),
]

for i, (title, tig_title, sentences, reinforcement, illustration) in enumerate(manners):
    # Story page
    doc.new_page()
    doc.add_filled_rect(0, 720, 612, 72, 0.88)
    doc.add_centered_text(745, f"Story {i+1}: {title}", 'F2', 18, 0)
    doc.add_centered_text(720, f"[TIGRINYA TEXT: {tig_title}]", 'F3', 12, 0.4)
    
    doc.add_rect(180, 530, 252, 150, 1, 0.6)
    doc.add_centered_text(610, f"[ILLUSTRATION: {illustration}]", 'F3', 10, 0.5)
    
    y = 500
    for sent in sentences:
        doc.add_text(72, y, sent, 'F4', 13, 0)
        y -= 28
    
    y -= 10
    doc.add_line(72, y+8, 540, y+8, 0.5, 0.7)
    doc.add_text(72, y, "[TIGRINYA TRANSLATION:", 'F3', 11, 0.3); y -= 16
    doc.add_text(72, y, f"Full translation of '{title}' story in Ge'ez script.]", 'F3', 10, 0.4); y -= 30
    
    # What should you do?
    doc.add_text(72, y, "What should you do?", 'F2', 14, 0.2); y -= 20
    doc.add_text(72, y, "[TIGRINYA: Ehnta Eyu kttgebrwo zoleka?]", 'F3', 10, 0.4); y -= 25
    
    # Good behavior reinforcement
    doc.add_filled_rect(60, y-25, 492, 40, 0.92)
    doc.add_centered_text(y, reinforcement, 'F2', 12, 0)
    doc.add_centered_text(y-18, f"[TIGRINYA: Translation of reinforcement]", 'F3', 9, 0.4)
    y -= 50
    
    # Happy face activity
    doc.add_text(72, y, "Color the happy face when you practice this!", 'F1', 12, 0)
    doc.add_text(72, y-18, "[TIGRINYA: Haw-haw zbl geits hbri gbero ente tetegbirutwo!]", 'F3', 9, 0.4)
    # Draw a simple circle for face
    doc.add_rect(72, y-80, 50, 50, 2, 0.4)
    doc.add_text(130, y-50, "= I practiced this today!", 'F1', 11, 0)

# Manners checklist page
doc.new_page()
doc.add_centered_text(740, "MY GOOD MANNERS CHECKLIST", 'F2', 18, 0)
doc.add_centered_text(710, "[TIGRINYA: Zrzr Tsbuq Bahli-ey]", 'F3', 12, 0.4)
doc.add_centered_text(680, "Check off each manner you practiced this week!", 'F1', 13, 0)

y = 630
for title, tig_title, _, _, _ in manners:
    doc.add_rect(72, y-5, 18, 18, 1.5, 0.4)
    doc.add_text(100, y, f"{title} / [{tig_title}]", 'F1', 11, 0)
    y -= 35

doc.add_centered_text(220, "You have GREAT manners!", 'F2', 16, 0.2)
doc.add_centered_text(190, "[TIGRINYA: Tsbuq bahli aleka/aleki!]", 'F3', 12, 0.4)

# Certificate page
doc.new_page()
doc.add_rect(50, 200, 512, 500, 3, 0.3)
doc.add_rect(60, 210, 492, 480, 1, 0.5)
doc.add_centered_text(620, "CERTIFICATE OF GOOD MANNERS", 'F2', 20, 0)
doc.add_centered_text(580, "[TIGRINYA: Wereqet Mskker Tsbuq Bahli]", 'F3', 12, 0.4)
doc.add_centered_text(530, "This certifies that", 'F4', 14, 0.3)
doc.add_line(180, 485, 432, 485, 1.5, 0.3)
doc.add_centered_text(490, "(write your name here)", 'F1', 10, 0.5)
doc.add_centered_text(440, "has shown EXCELLENT good manners!", 'F4', 14, 0)
doc.add_centered_text(400, "Keep being kind, polite, and respectful!", 'F1', 12, 0.3)
doc.add_centered_text(360, "[TIGRINYA: Lebamat, adabot, kiburut qitsil!]", 'F3', 11, 0.4)
doc.add_centered_text(300, "Date: _______________", 'F1', 12, 0.3)
doc.add_centered_text(260, "Signed: Daniel Tesfamariam", 'F5', 14, 0)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book265_Tigrinya_Manners_Book.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
