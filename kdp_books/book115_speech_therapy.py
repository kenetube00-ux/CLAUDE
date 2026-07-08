from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(550, "SPEECH THERAPY ACTIVITIES", 'F2', 18)
pdf.add_centered_text(520, "FOR KIDS AGES 3-6", 'F2', 16)
pdf.add_centered_text(490, "Articulation & Language", 'F4', 13)
pdf.add_centered_text(400, "Fun Practice for Home and School", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)
pdf.add_centered_text(575, "Work with your child's SLP for personalized guidance.", 'F4', 9)

# Page 3: How to Use
pdf.new_page()
pdf.add_centered_text(750, "HOW TO USE THIS BOOK", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "This workbook provides practice activities for common speech and",
    "language goals. Use it alongside your child's speech therapy.", "",
    "TIPS FOR HOME PRACTICE:",
    "- Keep sessions short (5-10 minutes for ages 3-4, 10-15 for 5-6)",
    "- Make it FUN (games, silly voices, rewards)",
    "- Practice in natural situations (during meals, play, reading)",
    "- Praise effort, not just accuracy ('Great try!')",
    "- Don't correct every mistake - focus on target sounds",
    "- Practice 3-5 times per week for best results", "",
    "ARTICULATION (SOUND) PRACTICE:",
    "Pages 4-13 focus on sounds children commonly struggle with:",
    "/s/, /r/, /l/, /th/, /sh/, /ch/", "",
    "Each sound includes word lists for:",
    "- Initial position (beginning of word): 'sun'",
    "- Medial position (middle of word): 'messy'",
    "- Final position (end of word): 'bus'",
    "- Sentences for practice at sentence level", "",
    "LANGUAGE BUILDING:",
    "Pages 14-18 focus on vocabulary, categories, and conversation."
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Articulation pages - target sounds
sounds = [
    ("/s/ SOUND", "sun, soap, sock, sand, seven, see, sit, sad, soup, sing",
     "messy, racing, bossing, icing, passing, castle, whistle, fossil",
     "bus, house, mouse, rice, goose, peace, juice, face, dress, ice"),
    ("/r/ SOUND", "red, run, rain, rabbit, ring, rock, rose, rug, read, rope",
     "carrot, parrot, cherry, berry, sorry, worry, mirror, fairy, story",
     "car, star, door, bear, chair, fire, flower, tiger, hammer, spider"),
    ("/l/ SOUND", "lamp, leaf, lemon, lion, love, lake, leg, light, lunch, lip",
     "balloon, pillow, jelly, belly, melon, color, dollar, yellow, hello",
     "ball, bell, shell, tall, mail, pool, school, wheel, girl, owl"),
    ("/th/ SOUND", "think, thumb, three, throw, thick, thin, thank, thirsty",
     "birthday, toothbrush, bathtub, nothing, something, bathroom",
     "bath, teeth, mouth, with, math, earth, tooth, path, cloth, smooth"),
    ("/sh/ SOUND", "shoe, ship, sheep, shop, shell, shark, share, shirt, shut",
     "fishing, washing, pushing, mushroom, ocean, cushion, station",
     "fish, dish, wish, brush, push, cash, trash, leash, fresh, rush"),
    ("/ch/ SOUND", "chair, cheese, chicken, child, chin, chips, chop, chalk",
     "teacher, kitchen, matches, watching, catching, ketchup, nature",
     "beach, peach, coach, each, lunch, much, such, touch, watch, rich")
]

for sound_name, initial, medial, final in sounds:
    pdf.new_page()
    pdf.add_centered_text(750, f"ARTICULATION: {sound_name}", 'F2', 15)
    pdf.add_line(60, 738, 552, 738)
    y = 715
    pdf.add_text(60, y, "INITIAL POSITION (beginning of word):", 'F2', 10)
    y -= 15
    pdf.add_text(60, y, initial, 'F4', 10)
    y -= 25
    pdf.add_text(60, y, "MEDIAL POSITION (middle of word):", 'F2', 10)
    y -= 15
    pdf.add_text(60, y, medial, 'F4', 10)
    y -= 25
    pdf.add_text(60, y, "FINAL POSITION (end of word):", 'F2', 10)
    y -= 15
    pdf.add_text(60, y, final, 'F4', 10)
    y -= 30
    pdf.add_text(60, y, "SENTENCE PRACTICE:", 'F2', 10)
    y -= 15
    sents = [
        f"1. Say each word 5 times clearly.",
        f"2. Put each word in a sentence.",
        f"3. Find objects with the {sound_name.split()[0]} sound around your house.",
        f"4. Read a book and listen for the {sound_name.split()[0]} sound.",
        f"5. Play 'I Spy' with {sound_name.split()[0]} words."
    ]
    for s in sents:
        pdf.add_text(60, y, s, 'F4', 10)
        y -= 15
    y -= 10
    pdf.add_text(60, y, "PROGRESS: Circle words mastered. Star words to keep practicing.", 'F2', 9)
    # Add practice tracking
    y -= 20
    pdf.add_text(60, y, "Date: ___/___ Accuracy: ___%  Date: ___/___ Accuracy: ___%", 'F3', 9)
    y -= 15
    pdf.add_text(60, y, "Date: ___/___ Accuracy: ___%  Date: ___/___ Accuracy: ___%", 'F3', 9)


# Pages for additional articulation practice
for sound_name, _, _, _ in sounds[3:]:
    # Already created above in the loop
    pass

# Pages 10-14: Language Building Activities (5 pages)
# Page: Categories
pdf.new_page()
pdf.add_centered_text(750, "LANGUAGE: CATEGORIES", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "SORTING INTO CATEGORIES helps children organize language.", "",
    "Name 5 things in each category:", "",
    "ANIMALS: ______, ______, ______, ______, ______",
    "FOOD: ______, ______, ______, ______, ______",
    "CLOTHING: ______, ______, ______, ______, ______",
    "VEHICLES: ______, ______, ______, ______, ______",
    "BODY PARTS: ______, ______, ______, ______, ______",
    "COLORS: ______, ______, ______, ______, ______", "",
    "WHICH ONE DOESN'T BELONG? (circle the odd one out)",
    "1. dog, cat, car, fish",
    "2. apple, banana, shoe, grape",
    "3. shirt, pants, book, hat",
    "4. red, blue, table, green",
    "5. spoon, fork, ball, cup", "",
    "WHAT CATEGORY DOES IT BELONG TO?",
    "banana = _______ (fruit!)",
    "fire truck = _______ (vehicle!)",
    "sock = _______ (clothing!)"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Opposites
pdf.new_page()
pdf.add_centered_text(750, "LANGUAGE: OPPOSITES", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "WHAT IS THE OPPOSITE?", "",
    "hot - _______     big - _______     up - _______",
    "fast - _______    happy - _______   on - _______",
    "open - _______    clean - _______   full - _______",
    "loud - _______    old - _______     wet - _______",
    "hard - _______    tall - _______    light - _______", "",
    "USE OPPOSITES IN SENTENCES:",
    "The elephant is big, but the mouse is _______.",
    "The sun is hot, but ice cream is _______.",
    "The rabbit is fast, but the turtle is _______.",
    "The music is loud, but the library is _______.", "",
    "PLAY: Say a word, child says the opposite!",
    "Take turns. Make it a game!", "",
    "HARDER OPPOSITES FOR ADVANCED LEARNERS:",
    "empty - _______   smooth - _______  brave - _______",
    "push - _______    same - _______    first - _______"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Describing Words
pdf.new_page()
pdf.add_centered_text(750, "LANGUAGE: DESCRIBING WORDS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Help your child describe objects using multiple attributes:", "",
    "DESCRIBE BY:",
    "Color: What color is it?",
    "Size: Is it big or small?",
    "Shape: What shape is it?",
    "Texture: Is it soft, hard, rough, smooth?",
    "Function: What do you do with it?",
    "Category: What group does it belong to?", "",
    "PRACTICE: Describe these items (use at least 3 attributes):",
    "",
    "An apple: _____________________________________",
    "(Example: red, round, small, smooth, you eat it, it's a fruit)", "",
    "A puppy: ______________________________________", "",
    "A blanket: ____________________________________", "",
    "A ball: _______________________________________", "",
    "A cookie: _____________________________________", "",
    "GAME: 'Guess What I'm Describing!'",
    "Parent describes, child guesses. Then switch!"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Following Directions
pdf.new_page()
pdf.add_centered_text(750, "LANGUAGE: FOLLOWING DIRECTIONS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Practice following directions of increasing complexity:", "",
    "1-STEP DIRECTIONS (ages 2-3):",
    "- Clap your hands.",
    "- Touch your nose.",
    "- Stand up.",
    "- Get the ball.", "",
    "2-STEP DIRECTIONS (ages 3-4):",
    "- Touch your head AND stomp your feet.",
    "- Pick up the crayon AND draw a circle.",
    "- Close the book AND put it on the shelf.", "",
    "3-STEP DIRECTIONS (ages 4-5):",
    "- Stand up, turn around, AND sit back down.",
    "- Get your shoes, put them on, AND come to the door.",
    "- Draw a circle, color it red, AND write your name.", "",
    "COMPLEX DIRECTIONS (ages 5-6):",
    "- BEFORE you sit down, touch the table.",
    "- Put the big block ON the small block.",
    "- Give me the blue crayon AFTER you draw a star.", "",
    "TIP: Start where the child succeeds, then add complexity.",
    "Use objects and actions from daily routines!"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Conversation Practice
pdf.new_page()
pdf.add_centered_text(750, "CONVERSATION SKILLS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "TURN-TAKING IN CONVERSATION:", "",
    "Rules of conversation (practice with your child):",
    "1. Look at the person talking",
    "2. Wait for your turn (don't interrupt)",
    "3. Stay on topic (don't change the subject suddenly)",
    "4. Ask questions about what the other person said",
    "5. Use a voice that matches the situation", "",
    "TOPIC MAINTENANCE:",
    "Practice talking about ONE topic for 3+ exchanges:", "",
    "Topic: PETS",
    "Adult: 'Do you like dogs or cats?'",
    "Child: (answers)",
    "Adult: 'What would you name a pet?'",
    "Child: (answers)",
    "Adult: 'What would you feed it?'", "",
    "Topics to practice: toys, food, school, animals, friends", "",
    "ASKING AND ANSWERING QUESTIONS:",
    "WHO questions: Who is your teacher?",
    "WHAT questions: What did you eat for lunch?",
    "WHERE questions: Where do you play outside?",
    "WHEN questions: When do you go to bed?",
    "WHY questions: Why do we wear a coat?",
    "HOW questions: How do you brush your teeth?"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Progress Tracking + Home Practice
pdf.new_page()
pdf.add_centered_text(750, "PROGRESS TRACKING & HOME SCHEDULE", 'F2', 14)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "ARTICULATION PROGRESS:", "",
    "Sound: /___/  Start accuracy: ___%",
    "Week 2: ___%  Week 4: ___%  Week 6: ___%  Week 8: ___%", "",
    "Sound: /___/  Start accuracy: ___%",
    "Week 2: ___%  Week 4: ___%  Week 6: ___%  Week 8: ___%", "",
    "LANGUAGE PROGRESS:",
    "Goal: _________________________________________",
    "Start: ________ Current: ________ Target: ________", "",
    "HOME PRACTICE SCHEDULE:", "",
    "Monday: _____ minutes  Focus: _________________",
    "Tuesday: _____ minutes  Focus: ________________",
    "Wednesday: _____ minutes  Focus: ______________",
    "Thursday: _____ minutes  Focus: _______________",
    "Friday: _____ minutes  Focus: _________________", "",
    "TIPS FOR PARENTS:",
    "- Model correct sounds without saying 'say it again'",
    "- Expand what your child says (child: 'big dog' you: 'Yes,",
    "  that's a BIG brown dog running fast!')",
    "- Read books together daily",
    "- Narrate daily activities ('I'm washing the dishes now')"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book115_Speech_Therapy_Activities.pdf')
print("Book115_Speech_Therapy_Activities.pdf created successfully!")
