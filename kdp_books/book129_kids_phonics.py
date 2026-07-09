from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "PHONICS FUN"
subtitle = "Letter Sounds Workbook for Pre-K & Kindergarten"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 24)
pdf.add_centered_text(510, subtitle, 'F4', 14)
pdf.add_centered_text(440, "Learn Letters, Sounds, and First Words", 'F4', 12)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, f"{title} - {subtitle}", 'F2', 11)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)
pdf.add_centered_text(480, "Designed for children ages 3-6 with adult guidance.", 'F4', 9)

# Pages 3-28: 26 Letter Pages (A-Z)
letters_data = [
    ("A", "a", "/a/ as in apple", ["Apple", "Ant", "Airplane"]),
    ("B", "b", "/b/ as in ball", ["Ball", "Bear", "Banana"]),
    ("C", "c", "/k/ as in cat", ["Cat", "Car", "Cup"]),
    ("D", "d", "/d/ as in dog", ["Dog", "Duck", "Door"]),
    ("E", "e", "/e/ as in egg", ["Egg", "Elephant", "Elf"]),
    ("F", "f", "/f/ as in fish", ["Fish", "Fox", "Flower"]),
    ("G", "g", "/g/ as in goat", ["Goat", "Grapes", "Gum"]),
    ("H", "h", "/h/ as in hat", ["Hat", "Horse", "House"]),
    ("I", "i", "/i/ as in igloo", ["Igloo", "Insect", "Ink"]),
    ("J", "j", "/j/ as in jar", ["Jar", "Jelly", "Juice"]),
    ("K", "k", "/k/ as in kite", ["Kite", "King", "Key"]),
    ("L", "l", "/l/ as in lamp", ["Lamp", "Lion", "Leaf"]),
    ("M", "m", "/m/ as in moon", ["Moon", "Monkey", "Map"]),
    ("N", "n", "/n/ as in nest", ["Nest", "Nut", "Nose"]),
    ("O", "o", "/o/ as in octopus", ["Octopus", "Orange", "Otter"]),
    ("P", "p", "/p/ as in pig", ["Pig", "Pen", "Pizza"]),
    ("Q", "q", "/kw/ as in queen", ["Queen", "Quilt", "Quarter"]),
    ("R", "r", "/r/ as in rain", ["Rain", "Rabbit", "Ring"]),
    ("S", "s", "/s/ as in sun", ["Sun", "Star", "Snake"]),
    ("T", "t", "/t/ as in top", ["Top", "Tiger", "Tree"]),
    ("U", "u", "/u/ as in umbrella", ["Umbrella", "Up", "Unicorn"]),
    ("V", "v", "/v/ as in van", ["Van", "Violin", "Vest"]),
    ("W", "w", "/w/ as in water", ["Water", "Whale", "Window"]),
    ("X", "x", "/ks/ as in fox", ["Fox", "Box", "Six"]),
    ("Y", "y", "/y/ as in yellow", ["Yellow", "Yo-yo", "Yarn"]),
    ("Z", "z", "/z/ as in zebra", ["Zebra", "Zoo", "Zipper"])
]

for upper, lower, sound, words in letters_data:
    pdf.new_page()
    # Large letters at top
    pdf.add_text(80, 700, upper, 'F2', 72)
    pdf.add_text(180, 700, lower, 'F4', 72)

    # Dotted trace line for uppercase
    pdf.add_text(50, 620, "Trace the letter:", 'F2', 12)
    pdf.add_text(50, 585, f"  {upper}   {upper}   {upper}   {upper}   {upper}   {upper}   {upper}", 'F1', 24)
    pdf.add_line(50, 578, 562, 578, 0.3, 0.7)

    # Dotted trace line for lowercase
    pdf.add_text(50, 550, f"  {lower}    {lower}    {lower}    {lower}    {lower}    {lower}    {lower}", 'F1', 24)
    pdf.add_line(50, 543, 562, 543, 0.3, 0.7)

    # Sound
    pdf.add_text(50, 505, f"This letter makes the sound: {sound}", 'F2', 13)

    # Words starting with this letter
    pdf.add_text(50, 470, "Words that start with this letter:", 'F2', 12)
    y = 445
    for word in words:
        pdf.add_text(70, y, f"* {word}", 'F4', 14)
        y -= 25

    # Practice writing lines
    pdf.add_text(50, y - 10, "Practice writing:", 'F2', 12)
    y -= 35
    for line_num in range(3):
        pdf.add_line(50, y, 562, y, 0.5, 0.5)
        # Guide lines (middle dotted)
        pdf.add_line(50, y + 15, 562, y + 15, 0.2, 0.8)
        y -= 40

# Page 29: Beginning Sounds Matching
pdf.new_page()
pdf.add_centered_text(750, "BEGINNING SOUNDS MATCHING", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 710
pdf.add_text(50, y, "Draw a line from each word to the letter it starts with!", 'F4', 12)
y -= 30
# Left column: words
left_words = ["Ball", "Cat", "Dog", "Fish", "Hat", "Kite", "Moon", "Sun", "Tree", "Zebra"]
# Right column: letters (shuffled order)
right_letters = ["S", "Z", "B", "M", "F", "T", "H", "D", "K", "C"]
for i in range(10):
    left_y = y - i * 40
    pdf.add_text(80, left_y, left_words[i], 'F2', 14)
    pdf.add_text(450, left_y, right_letters[i], 'F2', 18)
    # dots for drawing lines
    pdf.add_text(160, left_y, ". . . . . . . . . . . . . . . . . . . . .", 'F1', 8)

# Page 30: Rhyming Words
pdf.new_page()
pdf.add_centered_text(750, "RHYMING WORDS", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 710
pdf.add_text(50, y, "Words that RHYME sound the same at the end!", 'F4', 12)
y -= 25
pdf.add_text(50, y, "Circle the word that rhymes with the first word:", 'F2', 11)
y -= 30
rhyme_sets = [
    ("CAT", "dog", "hat", "cup"),
    ("PIG", "big", "pen", "pot"),
    ("SUN", "map", "fun", "sit"),
    ("BALL", "tall", "bed", "cup"),
    ("PAN", "man", "pig", "top"),
    ("HOP", "hat", "hit", "mop"),
    ("BED", "red", "big", "bat"),
    ("RING", "ran", "king", "rug"),
    ("FOX", "fun", "fit", "box"),
    ("CAKE", "lake", "cup", "cat"),
]
for base, opt1, opt2, opt3 in rhyme_sets:
    pdf.add_text(80, y, base, 'F2', 14)
    pdf.add_text(200, y, opt1, 'F4', 14)
    pdf.add_text(310, y, opt2, 'F4', 14)
    pdf.add_text(420, y, opt3, 'F4', 14)
    y -= 35

# Page 31: CVC Word Building
pdf.new_page()
pdf.add_centered_text(750, "CVC WORD BUILDING", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 710
pdf.add_text(50, y, "CVC = Consonant + Vowel + Consonant (your first words to read!)", 'F4', 11)
y -= 25
pdf.add_text(50, y, "Fill in the missing letter to make the word:", 'F2', 12)
y -= 30
cvc_words = [
    ("_at", "c", "cat (a furry pet)"),
    ("_og", "d", "dog (a pet that barks)"),
    ("_un", "s", "sun (bright in the sky)"),
    ("_ig", "p", "pig (pink farm animal)"),
    ("h_t", "a", "hat (you wear on your head)"),
    ("b_d", "e", "bed (where you sleep)"),
    ("c_p", "u", "cup (you drink from it)"),
    ("_op", "m", "mop (cleans the floor)"),
    ("r_n", "u", "run (move your legs fast)"),
    ("_en", "h", "hen (a girl chicken)"),
    ("b_g", "a", "bag (carry things in it)"),
    ("_ot", "h", "hot (very warm)")
]
for word_blank, answer, hint in cvc_words:
    pdf.add_text(80, y, word_blank, 'F2', 18)
    pdf.add_rect(200, y - 4, 30, 22, 0.5)
    pdf.add_text(250, y, f"= {hint}", 'F4', 11)
    y -= 35

# Page 32: "I Can Read!" Simple Sentences
pdf.new_page()
pdf.add_centered_text(750, "I CAN READ!", 'F2', 20)
pdf.add_line(50, 740, 562, 740)
y = 710
pdf.add_centered_text(y, "Try reading these simple sentences!", 'F4', 12)
y -= 30
sentences = [
    "The cat sat on the mat.",
    "I can see the big dog.",
    "The red hen is in the pen.",
    "Sam has a hat and a bat.",
    "The sun is hot and fun.",
    "A pig can dig in the mud.",
    "I like my pet fish.",
    "The fox ran to the box.",
    "Mom and Dad are the best.",
    "I can read! I am so good!",
]
for sentence in sentences:
    pdf.add_text(80, y, sentence, 'F2', 14)
    y -= 20
    # reading practice line
    pdf.add_text(80, y, "(Read it again! Point to each word.)", 'F4', 9)
    y -= 30

y -= 10
pdf.add_centered_text(y, "GREAT JOB! You are a READER!", 'F2', 16)
y -= 25
pdf.add_centered_text(y, "Color a star each time you read this page:", 'F4', 11)
y -= 20
# Draw 10 stars (as asterisks)
pdf.add_centered_text(y, "*    *    *    *    *    *    *    *    *    *", 'F2', 18)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book129_Phonics_Workbook_PreK.pdf')
print("Book129_Phonics_Workbook_PreK.pdf created successfully!")
