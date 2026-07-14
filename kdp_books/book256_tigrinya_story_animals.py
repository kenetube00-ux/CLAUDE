"""Book 256: ANIMALS OF ERITREA - Bilingual Story Book (Tigrinya-English) Ages 3-7"""
from pdf_utils import PDFDoc
import os

doc = PDFDoc(612, 792)

# Page 1: Title Page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(650, "ANIMALS OF ERITREA", 'F2', 28, 0)
doc.add_centered_text(610, "[TIGRINYA TEXT: Ensasat Ertra]", 'F3', 14, 0.3)
doc.add_centered_text(560, "Bilingual Story Book", 'F1', 18, 0.2)
doc.add_centered_text(530, "(Tigrinya-English)", 'F1', 16, 0.3)
doc.add_centered_text(490, "Ages 3-7", 'F2', 16, 0.2)
doc.add_rect(180, 250, 252, 200, 2, 0.4)
doc.add_centered_text(340, "[ILLUSTRATION: African animals", 'F3', 11, 0.5)
doc.add_centered_text(320, "gathered together in Eritrean landscape]", 'F3', 11, 0.5)
doc.add_centered_text(150, "Daniel Tesfamariam", 'F2', 16, 0)
doc.add_centered_text(120, "10 Stories About Amazing Animals", 'F1', 12, 0.3)

# Page 2: Copyright
doc.new_page()
doc.add_centered_text(600, "ANIMALS OF ERITREA", 'F2', 16, 0)
doc.add_centered_text(570, "Bilingual Story Book (Tigrinya-English)", 'F1', 12, 0.3)
doc.add_text(72, 500, "Copyright (c) 2025 Daniel Tesfamariam. All rights reserved.", 'F1', 10, 0.3)
doc.add_text(72, 480, "No part of this book may be reproduced without permission.", 'F1', 10, 0.3)
doc.add_text(72, 450, "Written by: Daniel Tesfamariam", 'F1', 10, 0.3)
doc.add_text(72, 430, "For Ages: 3-7 years", 'F1', 10, 0.3)
doc.add_text(72, 410, "Language: Tigrinya & English (Bilingual)", 'F1', 10, 0.3)
doc.add_text(72, 370, "NOTE: [TIGRINYA TEXT] placeholders indicate where", 'F3', 9, 0.4)
doc.add_text(72, 355, "Ge'ez script translations will be added.", 'F3', 9, 0.4)
doc.add_text(72, 300, "Printed in the United States of America", 'F1', 10, 0.3)
doc.add_text(72, 280, "First Edition, 2025", 'F1', 10, 0.3)

# Stories data
stories = [
    ("The Clever Monkey", "Ensasat: Habi Tselim", "problem-solving",
     "Once there was a clever monkey who lived in a tall tree in Eritrea.",
     "One day, the monkey could not reach the fruit on a nearby branch.",
     "He thought and thought. Then he used a long stick to pull the fruit closer!",
     "The other animals cheered for the clever monkey.",
     "When you think hard, you can solve any problem!",
     "Moral: Use your brain to solve problems. / [TIGRINYA: Hankela tetsemire, tsegem teftti.]"),
    ("The Brave Lion", "Ensasat: Tebay Anbessa", "courage",
     "In the grasslands of Eritrea, there lived a young lion named Ari.",
     "Ari was afraid of the thunder that boomed in the sky.",
     "One night, a big storm came. Ari's little sister was scared too.",
     "Ari took a deep breath and said, 'Don't worry, I will protect you!'",
     "That night, Ari learned that being brave means helping others even when you are scared.",
     "Moral: Courage is being scared but doing the right thing anyway. / [TIGRINYA: Tiblaht malet...]"),
    ("The Kind Elephant", "Ensasat: Lebamat Hareg", "helping others",
     "Big Elephant had the longest trunk and the strongest legs.",
     "When little animals could not reach the water hole, Elephant helped them.",
     "She carried the baby birds back to their nest when they fell.",
     "All the animals loved Big Elephant because she was so kind.",
     "Kindness makes the world a better place for everyone.",
     "Moral: Always help those who need it. / [TIGRINYA: Kulu gize nzidelyu hager.]"),
    ("The Fast Gazelle", "Ensasat: Qeltafi Midri-Beg", "using your gifts",
     "Gazelle could run faster than any animal in the savanna.",
     "Sometimes she wished she could climb trees like the monkeys instead.",
     "But when a fire came, Gazelle ran to warn all the other animals!",
     "She saved everyone because she was so fast.",
     "Everyone has a special gift. Use yours to help others!",
     "Moral: Your gift is special - use it well! / [TIGRINYA: Tsega Haba zelewo...]"),
    ("The Wise Owl", "Ensasat: Gobez Gogo", "thinking before acting",
     "Owl sat in her tree and watched everything below.",
     "When the animals argued, they came to Owl for help.",
     "She always said, 'First think, then speak. First plan, then act.'",
     "The animals learned to slow down and think carefully.",
     "Being wise means taking time to make good choices.",
     "Moral: Think before you act. / [TIGRINYA: Koynu qedmi hiseb.]"),
    ("The Busy Bee", "Ensasat: Tsebarhi Nhibi", "hard work",
     "Little Bee woke up every morning before the sun rose.",
     "She flew from flower to flower, collecting sweet nectar.",
     "Her friends said, 'Bee, why do you work so hard?'",
     "Bee smiled and said, 'Because I am making honey for everyone!'",
     "Hard work brings sweet rewards for you and others.",
     "Moral: Hard work always pays off. / [TIGRINYA: Tsbuq srah kulu gize yferi.]"),
    ("The Colorful Bird", "Ensasat: Tsebbihi Awaf", "being unique",
     "In a tree full of brown birds, one bird had feathers of many colors.",
     "The colorful bird felt different and sometimes sad.",
     "But one day, she sang a beautiful song that made everyone smile.",
     "The other birds said, 'We love how special you are!'",
     "Being different is what makes you beautiful and amazing.",
     "Moral: Being different is beautiful. / [TIGRINYA: Fikuy mzani tsebbihi eyu.]"),
    ("The Patient Camel", "Ensasat: Tehagazti Gemel", "perseverance",
     "Camel had to cross a very long, hot desert to find water.",
     "The journey was hard, and the sun was very strong.",
     "But Camel kept walking, one step at a time, never giving up.",
     "Finally, he reached the cool water and drank happily.",
     "When things are hard, keep going. You will reach your goal!",
     "Moral: Never give up! / [TIGRINYA: Kebi ztsereg aytreftun!]"),
    ("The Playful Dolphin", "Ensasat: Tsewati Dolphin", "joy",
     "In the Red Sea near Eritrea, a dolphin loved to play.",
     "She jumped high above the waves and splashed back down.",
     "She invited the fish to play games and everyone had fun.",
     "Dolphin said, 'Life is better when we play and laugh together!'",
     "Joy and laughter make every day wonderful.",
     "Moral: Find joy in every day! / [TIGRINYA: Ab kulu meAlti haw-haw bel!]"),
    ("The Strong Eagle", "Ensasat: Hayli Nsri", "reaching high",
     "Eagle wanted to fly higher than any bird had ever flown.",
     "She practiced every day, spreading her wings wider and wider.",
     "Some birds said, 'That is too high! You cannot do it!'",
     "But Eagle believed in herself and flew above the clouds!",
     "When you believe in yourself, you can reach amazing heights.",
     "Moral: Aim high and believe in yourself! / [TIGRINYA: Lali Ariy kemzi tsebqo!]"),
]

# Generate story pages (2 pages per story)
for i, (title, tig_title, theme, s1, s2, s3, s4, s5, moral) in enumerate(stories):
    # Story page 1: Title and story
    doc.new_page()
    doc.add_filled_rect(0, 720, 612, 72, 0.85)
    doc.add_centered_text(740, f"Story {i+1}: {title}", 'F2', 18, 0)
    doc.add_centered_text(720, f"[TIGRINYA TEXT: {tig_title}]", 'F3', 12, 0.4)
    
    doc.add_rect(150, 500, 312, 180, 1, 0.6)
    doc.add_centered_text(600, f"[ILLUSTRATION: Scene from '{title}']", 'F3', 10, 0.5)
    
    y = 470
    doc.add_text(72, y, s1, 'F4', 13, 0); y -= 25
    doc.add_text(72, y, s2, 'F4', 13, 0); y -= 25
    doc.add_text(72, y, s3, 'F4', 13, 0); y -= 25
    doc.add_text(72, y, s4, 'F4', 13, 0); y -= 25
    doc.add_text(72, y, s5, 'F4', 13, 0); y -= 40
    
    doc.add_text(72, y, "[TIGRINYA TRANSLATION:", 'F3', 11, 0.3); y -= 18
    doc.add_text(72, y, f"Full Tigrinya translation of story '{title}' goes here.", 'F3', 10, 0.4); y -= 18
    doc.add_text(72, y, "Daniel will add Ge'ez script version.]", 'F3', 10, 0.4); y -= 35
    
    doc.add_line(72, y+10, 540, y+10, 0.5, 0.7)
    doc.add_text(72, y, moral, 'F2', 11, 0.2)
    
    # Story page 2: Activity
    doc.new_page()
    doc.add_centered_text(730, f"Activity: {title}", 'F2', 16, 0.2)
    doc.add_centered_text(700, "Draw your favorite part of this story!", 'F1', 14, 0)
    doc.add_centered_text(680, "[TIGRINYA TEXT: Zfetukha kfli nahazi tsirhi sirAka!]", 'F3', 10, 0.4)
    
    doc.add_rect(72, 350, 468, 300, 2, 0.5)
    doc.add_centered_text(500, "Your Drawing Here", 'F1', 14, 0.6)
    
    doc.add_text(72, 320, f"What I learned from this story:", 'F2', 12, 0.2)
    doc.add_text(72, 300, "[TIGRINYA TEXT: Kabti tsirhi ezy ezi eyu ztemelkutwo:]", 'F3', 10, 0.4)
    doc.add_line(72, 270, 540, 270, 0.5, 0.6)
    doc.add_line(72, 245, 540, 245, 0.5, 0.6)
    doc.add_line(72, 220, 540, 220, 0.5, 0.6)

# Vocabulary page
doc.new_page()
doc.add_filled_rect(0, 720, 612, 72, 0.85)
doc.add_centered_text(750, "VOCABULARY - Animal Names", 'F2', 20, 0)
doc.add_centered_text(725, "[TIGRINYA TEXT: Qalat - Asmat Ensasat]", 'F3', 12, 0.4)

animals_vocab = [
    ("Monkey", "Tselim/Habi"), ("Lion", "Anbessa"), ("Elephant", "Hareg"),
    ("Gazelle", "Midri-Beg"), ("Owl", "Gogo"), ("Bee", "Nhibi"),
    ("Bird", "Awaf"), ("Camel", "Gemel"), ("Dolphin", "Dolphin"),
    ("Eagle", "Nsri")
]

y = 660
for eng, tig in animals_vocab:
    doc.add_text(72, y, f"{eng}", 'F2', 14, 0)
    doc.add_text(200, y, f"[TIGRINYA: {tig}]", 'F3', 13, 0.3)
    doc.add_text(400, y, "[FIDEL PLACEHOLDER]", 'F3', 12, 0.5)
    doc.add_line(72, y-10, 540, y-10, 0.5, 0.8)
    y -= 45

doc.add_centered_text(150, "Great job learning animal names!", 'F2', 14, 0.2)
doc.add_centered_text(125, "[TIGRINYA TEXT: Tsbuq srah ab mflaT asmat ensasat!]", 'F3', 11, 0.4)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book256_Tigrinya_Animals_Story.pdf")
doc.save(output_path)
print(f"Generated: {output_path}")
