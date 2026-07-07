"""
Book 54: Brain Games & Memory Exercises - For Adults 45+
KDP Interior - 8.5x11 inches (612x792 points)
"""
import random
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    random.seed(54)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "BRAIN GAMES &", font='F2', size=30)
    pdf.add_centered_text(575, "MEMORY EXERCISES", font='F2', size=30)
    pdf.add_centered_text(530, "For Adults 45+", font='F1', size=20)
    pdf.add_line(150, 500, 462, 500, 2)
    pdf.add_centered_text(460, "Word Scrambles | Trivia | Memory Challenges", font='F4', size=14)
    pdf.add_centered_text(435, "Pattern Recognition | Math Brain Teasers", font='F4', size=13)
    pdf.add_centered_text(380, "Keep Your Mind Sharp!", font='F1', size=16)
    pdf.add_centered_text(310, "By", font='F1', size=12)
    pdf.add_centered_text(280, "Daniel Tesfamariam", font='F2', size=18)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "Brain Games & Memory Exercises - For Adults 45+", font='F2', size=13)
    pdf.add_centered_text(570, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(545, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(515, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(490, "Published via Amazon KDP", font='F1', size=10)

    # --- WORD SCRAMBLES (10 pages) ---
    word_sets = [
        ["COMPUTER", "INTERNET", "KEYBOARD", "MONITOR", "SOFTWARE", "NETWORK", "DIGITAL", "PROGRAM"],
        ["TELEPHONE", "CELLULAR", "WIRELESS", "BATTERY", "CHARGER", "SIGNAL", "DISPLAY", "TOUCHPAD"],
        ["MOUNTAIN", "TROPICAL", "PEACEFUL", "WATERFALL", "SUNSHINE", "ADVENTURE", "BEAUTIFUL", "LANDSCAPE"],
        ["MEDICINE", "PHARMACY", "HOSPITAL", "EXERCISE", "VITAMINS", "WELLNESS", "HEALTHY", "STRENGTH"],
        ["BREAKFAST", "MUSHROOM", "SANDWICH", "BROCCOLI", "CHOCOLATE", "CINNAMON", "BLUEBERRY", "PINEAPPLE"],
        ["FOOTBALL", "BASEBALL", "SWIMMING", "MARATHON", "CHAMPION", "ATHLETIC", "PRACTICE", "TRAINING"],
        ["PAINTING", "SCULPTURE", "CREATIVE", "MUSICIAN", "ARTISTIC", "DRAWING", "GALLERY", "CONCERT"],
        ["ELEPHANT", "DOLPHIN", "PENGUIN", "GIRAFFE", "BUTTERFLY", "FLAMINGO", "TORTOISE", "KANGAROO"],
        ["CALENDAR", "SCHEDULE", "ORGANIZE", "REMEMBER", "PLANNING", "DEADLINE", "ROUTINE", "MONTHLY"],
        ["GRATEFUL", "KINDNESS", "PATIENCE", "GENEROUS", "FRIENDLY", "CHEERFUL", "PEACEFUL", "THANKFUL"],
    ]

    answers_scrambles = []
    for page_num, words in enumerate(word_sets, 1):
        pdf.new_page()
        pdf.add_centered_text(740, f"Word Scramble #{page_num}", font='F2', size=20)
        pdf.add_centered_text(710, "Unscramble each word. Write your answer on the line.", font='F1', size=12)
        pdf.add_line(100, 695, 512, 695, 1)

        y = 660
        scrambled_list = []
        for word in words:
            letters = list(word)
            random.shuffle(letters)
            scrambled = ''.join(letters)
            scrambled_list.append((scrambled, word))
            pdf.add_text(80, y, f"{scrambled}", font='F3', size=14)
            pdf.add_text(280, y, "___________________", font='F1', size=12)
            y -= 55

        answers_scrambles.append((page_num, scrambled_list))
        pdf.add_centered_text(40, f"- Page {page_num} -", font='F1', size=9)

    # --- MEMORY CHALLENGES (5 pages) ---
    memory_lists = [
        ("Grocery List", ["Milk", "Bread", "Eggs", "Butter", "Apples", "Cheese", "Carrots", "Chicken", "Rice", "Tomatoes"]),
        ("Famous People", ["Einstein", "Mozart", "Lincoln", "Curie", "Edison", "Shakespeare", "Churchill", "Earhart", "Franklin", "Twain"]),
        ("Countries", ["France", "Japan", "Brazil", "Egypt", "Canada", "India", "Italy", "Mexico", "Greece", "Norway"]),
        ("Colors & Objects", ["Red apple", "Blue sky", "Green frog", "Yellow sun", "Purple grape", "Orange cat", "Pink rose", "White cloud", "Brown bear", "Black hat"]),
        ("Actions", ["Running", "Cooking", "Reading", "Swimming", "Painting", "Dancing", "Writing", "Singing", "Gardening", "Laughing"]),
    ]

    for page_num, (category, items) in enumerate(memory_lists, 1):
        pdf.new_page()
        pdf.add_centered_text(740, f"Memory Challenge #{page_num}", font='F2', size=20)
        pdf.add_centered_text(710, f"Category: {category}", font='F1', size=14)
        pdf.add_line(100, 695, 512, 695, 1)
        pdf.add_centered_text(670, "Study these 10 items for 2 minutes, then turn the page.", font='F4', size=12)

        y = 630
        for i, item in enumerate(items, 1):
            pdf.add_text(200, y, f"{i}. {item}", font='F2', size=14)
            y -= 40

        # Questions page
        pdf.new_page()
        pdf.add_centered_text(740, f"Memory Challenge #{page_num} - Questions", font='F2', size=18)
        pdf.add_centered_text(710, "Without looking back, answer these questions:", font='F1', size=12)
        pdf.add_line(100, 695, 512, 695, 1)

        questions = [
            f"1. What was the 3rd item on the list? ___________________",
            f"2. What was the 7th item on the list? ___________________",
            f"3. What was the last item on the list? ___________________",
            f"4. What was the 1st item on the list? ___________________",
            f"5. Can you write all 10 items from memory?",
        ]
        y = 660
        for q in questions:
            pdf.add_text(80, y, q, font='F4', size=12)
            y -= 45

        pdf.add_text(80, y, "Write all 10 here:", font='F5', size=12)
        y -= 30
        for j in range(10):
            pdf.add_text(100, y, f"{j+1}. ___________________", font='F1', size=11)
            y -= 25

    # --- TRIVIA QUESTIONS (10 pages) ---
    trivia_sets = [
        ("1970s Trivia", [
            ("What year did the first Star Wars movie come out?", "1977"),
            ("Who was the US President during the Watergate scandal?", "Nixon"),
            ("What band released 'Stairway to Heaven'?", "Led Zeppelin"),
            ("What 1970s dance movie starred John Travolta?", "Saturday Night Fever"),
            ("What year did the Vietnam War end?", "1975"),
        ]),
        ("1980s Trivia", [
            ("What year did the Berlin Wall fall?", "1989"),
            ("Who sang 'Thriller' in 1982?", "Michael Jackson"),
            ("What was the first Space Shuttle called?", "Columbia"),
            ("What 1980s video game features a plumber?", "Super Mario Bros"),
            ("Who was the 'Iron Lady' Prime Minister?", "Margaret Thatcher"),
        ]),
        ("1990s Trivia", [
            ("What year did the World Wide Web become public?", "1991"),
            ("What TV show featured six friends in New York?", "Friends"),
            ("Who won the 1999 Women's World Cup soccer?", "USA"),
            ("What boy band sang 'I Want It That Way'?", "Backstreet Boys"),
            ("What animated movie featured a lion cub named Simba?", "The Lion King"),
        ]),
        ("Music Trivia", [
            ("Who is known as the King of Rock and Roll?", "Elvis Presley"),
            ("What instrument does a pianist play?", "Piano"),
            ("Who sang 'Imagine'?", "John Lennon"),
            ("What genre of music originated in New Orleans?", "Jazz"),
            ("Who is the Queen of Soul?", "Aretha Franklin"),
        ]),
        ("Geography Trivia", [
            ("What is the largest ocean on Earth?", "Pacific"),
            ("What country has the most people?", "China/India"),
            ("What is the longest river in the world?", "Nile"),
            ("What is the smallest continent?", "Australia"),
            ("What city is known as the Big Apple?", "New York"),
        ]),
        ("Science Trivia", [
            ("What planet is closest to the Sun?", "Mercury"),
            ("What gas do plants breathe in?", "Carbon dioxide"),
            ("How many bones are in the adult human body?", "206"),
            ("What is the hardest natural substance?", "Diamond"),
            ("What force keeps us on the ground?", "Gravity"),
        ]),
        ("Food & Drink Trivia", [
            ("What country is sushi originally from?", "Japan"),
            ("What fruit is used to make wine?", "Grapes"),
            ("What is the main ingredient in guacamole?", "Avocado"),
            ("What Italian dish is made with flat dough and toppings?", "Pizza"),
            ("What bean is chocolate made from?", "Cacao"),
        ]),
        ("History Trivia", [
            ("Who was the first man to walk on the moon?", "Neil Armstrong"),
            ("What ship sank in 1912 on its maiden voyage?", "Titanic"),
            ("What year did World War II end?", "1945"),
            ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
            ("What ancient wonder was in Egypt?", "Great Pyramid"),
        ]),
        ("Nature Trivia", [
            ("What is the largest land animal?", "Elephant"),
            ("How many legs does a spider have?", "Eight"),
            ("What is the fastest land animal?", "Cheetah"),
            ("What type of animal is a dolphin?", "Mammal"),
            ("What season do leaves change color?", "Autumn/Fall"),
        ]),
        ("Movies & TV Trivia", [
            ("Who played Dorothy in The Wizard of Oz?", "Judy Garland"),
            ("What movie features the line 'Here's looking at you, kid'?", "Casablanca"),
            ("Who directed Jaws and E.T.?", "Steven Spielberg"),
            ("What TV show had the catchphrase 'Live long and prosper'?", "Star Trek"),
            ("What animated movie has a character named Woody?", "Toy Story"),
        ]),
    ]

    answers_trivia = []
    for page_num, (category, questions) in enumerate(trivia_sets, 1):
        pdf.new_page()
        pdf.add_centered_text(740, f"Trivia #{page_num}: {category}", font='F2', size=18)
        pdf.add_line(100, 720, 512, 720, 1)

        y = 680
        for i, (question, answer) in enumerate(questions, 1):
            pdf.add_text(80, y, f"{i}. {question}", font='F4', size=12)
            y -= 25
            pdf.add_text(100, y, "Your answer: ___________________", font='F1', size=11)
            y -= 50

        answers_trivia.append((category, questions))

    # --- PATTERN RECOGNITION (5 pages) ---
    patterns = [
        [("2, 4, 6, 8, ___", "10"), ("A, C, E, G, ___", "I"), ("1, 4, 9, 16, ___", "25"),
         ("10, 20, 30, 40, ___", "50"), ("Z, Y, X, W, ___", "V")],
        [("3, 6, 12, 24, ___", "48"), ("AA, BB, CC, DD, ___", "EE"), ("1, 1, 2, 3, 5, ___", "8"),
         ("100, 90, 80, 70, ___", "60"), ("M, T, W, T, ___", "F")],
        [("5, 10, 15, 20, ___", "25"), ("J, F, M, A, ___", "M"), ("1, 3, 5, 7, ___", "9"),
         ("2, 6, 18, 54, ___", "162"), ("AB, CD, EF, GH, ___", "IJ")],
        [("50, 45, 40, 35, ___", "30"), ("1, 4, 7, 10, ___", "13"), ("B, D, F, H, ___", "J"),
         ("11, 22, 33, 44, ___", "55"), ("SUN, MON, TUE, WED, ___", "THU")],
        [("7, 14, 21, 28, ___", "35"), ("A, E, I, O, ___", "U"), ("1, 8, 27, 64, ___", "125"),
         ("99, 88, 77, 66, ___", "55"), ("DO, RE, MI, FA, ___", "SOL")],
    ]

    answers_patterns = []
    for page_num, pattern_set in enumerate(patterns, 1):
        pdf.new_page()
        pdf.add_centered_text(740, f"Pattern Recognition #{page_num}", font='F2', size=18)
        pdf.add_centered_text(710, "What comes next in each sequence?", font='F1', size=13)
        pdf.add_line(100, 695, 512, 695, 1)

        y = 650
        for i, (seq, answer) in enumerate(pattern_set, 1):
            pdf.add_text(80, y, f"{i}. {seq}", font='F3', size=14)
            y -= 55
        answers_patterns.append(pattern_set)

    # --- WORD ASSOCIATION (5 pages) ---
    associations = [
        [("Salt", "Pepper"), ("Hot", "Cold"), ("Day", "Night"), ("Up", "Down"),
         ("Black", "White"), ("Stop", "Go"), ("Left", "Right"), ("Old", "New")],
        [("Bread", "Butter"), ("Lock", "Key"), ("Cup", "Saucer"), ("Needle", "Thread"),
         ("Thunder", "Lightning"), ("Shoes", "Socks"), ("Pen", "Paper"), ("Stars", "Moon")],
        [("King", "Queen"), ("Doctor", "Nurse"), ("Husband", "Wife"), ("Teacher", "Student"),
         ("Mother", "Father"), ("Brother", "Sister"), ("Uncle", "Aunt"), ("Boy", "Girl")],
        [("Apple", "Tree"), ("Fish", "Water"), ("Bird", "Sky"), ("Flower", "Garden"),
         ("Bee", "Honey"), ("Cow", "Milk"), ("Sheep", "Wool"), ("Hen", "Egg")],
        [("Hammer", "Nail"), ("Brush", "Paint"), ("Saw", "Wood"), ("Oven", "Bake"),
         ("Scissors", "Cut"), ("Broom", "Sweep"), ("Hose", "Water"), ("Shovel", "Dig")],
    ]

    for page_num, pairs in enumerate(associations, 1):
        pdf.new_page()
        pdf.add_centered_text(740, f"Word Association #{page_num}", font='F2', size=18)
        pdf.add_centered_text(710, "Match each word on the left with its partner on the right.", font='F1', size=12)
        pdf.add_line(100, 695, 512, 695, 1)

        # Shuffle right column for the puzzle
        left_words = [p[0] for p in pairs]
        right_words = [p[1] for p in pairs]
        shuffled_right = right_words[:]
        random.shuffle(shuffled_right)

        y = 650
        for i in range(len(pairs)):
            pdf.add_text(100, y, f"{i+1}. {left_words[i]}", font='F2', size=13)
            pdf.add_text(250, y, "___", font='F1', size=13)
            pdf.add_text(350, y, f"{chr(65+i)}. {shuffled_right[i]}", font='F1', size=13)
            y -= 50

    # --- MATH BRAIN TEASERS (5 pages) ---
    math_problems = [
        [("15 + 27 = ___", "42"), ("100 - 37 = ___", "63"), ("8 x 7 = ___", "56"),
         ("144 / 12 = ___", "12"), ("25 + 38 + 12 = ___", "75"),
         ("Half of 86 = ___", "43"), ("Double 35 = ___", "70")],
        [("19 + 44 = ___", "63"), ("200 - 85 = ___", "115"), ("9 x 6 = ___", "54"),
         ("96 / 8 = ___", "12"), ("33 + 17 + 50 = ___", "100"),
         ("Half of 124 = ___", "62"), ("Double 48 = ___", "96")],
        [("67 + 45 = ___", "112"), ("500 - 175 = ___", "325"), ("12 x 11 = ___", "132"),
         ("156 / 12 = ___", "13"), ("45 + 55 + 25 = ___", "125"),
         ("Half of 250 = ___", "125"), ("Double 67 = ___", "134")],
        [("88 + 77 = ___", "165"), ("1000 - 450 = ___", "550"), ("15 x 8 = ___", "120"),
         ("108 / 9 = ___", "12"), ("125 + 75 + 50 = ___", "250"),
         ("Half of 500 = ___", "250"), ("Double 125 = ___", "250")],
        [("99 + 101 = ___", "200"), ("750 - 325 = ___", "425"), ("25 x 4 = ___", "100"),
         ("225 / 15 = ___", "15"), ("200 + 150 + 75 = ___", "425"),
         ("Half of 1000 = ___", "500"), ("Double 250 = ___", "500")],
    ]

    answers_math = []
    for page_num, problems in enumerate(math_problems, 1):
        pdf.new_page()
        pdf.add_centered_text(740, f"Math Brain Teaser #{page_num}", font='F2', size=18)
        pdf.add_centered_text(710, "Solve these without a calculator!", font='F1', size=13)
        pdf.add_line(100, 695, 512, 695, 1)

        y = 650
        for problem, answer in problems:
            pdf.add_text(150, y, problem, font='F3', size=15)
            y -= 55
        answers_math.append(problems)

    # --- ANSWER KEY (3 pages) ---
    pdf.new_page()
    pdf.add_centered_text(740, "ANSWER KEY - Page 1", font='F2', size=20)
    pdf.add_line(150, 720, 462, 720, 2)
    y = 690
    pdf.add_text(80, y, "Word Scrambles:", font='F2', size=12)
    y -= 25
    for page_num, scrambled_list in answers_scrambles[:5]:
        pdf.add_text(80, y, f"  Set {page_num}: {', '.join([w for _, w in scrambled_list])}", font='F3', size=9)
        y -= 20

    y -= 15
    pdf.add_text(80, y, "Word Scrambles (continued):", font='F2', size=12)
    y -= 25
    for page_num, scrambled_list in answers_scrambles[5:]:
        pdf.add_text(80, y, f"  Set {page_num}: {', '.join([w for _, w in scrambled_list])}", font='F3', size=9)
        y -= 20

    y -= 15
    pdf.add_text(80, y, "Pattern Recognition:", font='F2', size=12)
    y -= 25
    for page_num, pattern_set in enumerate(answers_patterns, 1):
        answers_str = ', '.join([ans for _, ans in pattern_set])
        pdf.add_text(80, y, f"  Set {page_num}: {answers_str}", font='F3', size=9)
        y -= 20

    pdf.new_page()
    pdf.add_centered_text(740, "ANSWER KEY - Page 2", font='F2', size=20)
    pdf.add_line(150, 720, 462, 720, 2)
    y = 690
    pdf.add_text(80, y, "Trivia Answers:", font='F2', size=12)
    y -= 25
    for category, questions in answers_trivia:
        pdf.add_text(80, y, f"  {category}:", font='F2', size=10)
        y -= 18
        for i, (q, a) in enumerate(questions, 1):
            pdf.add_text(100, y, f"    {i}. {a}", font='F3', size=9)
            y -= 15
        y -= 10
        if y < 80:
            pdf.new_page()
            pdf.add_centered_text(740, "ANSWER KEY - Page 3", font='F2', size=20)
            pdf.add_line(150, 720, 462, 720, 2)
            y = 690

    y -= 15
    pdf.add_text(80, y, "Math Brain Teasers:", font='F2', size=12)
    y -= 25
    for page_num, problems in enumerate(answers_math, 1):
        answers_str = ', '.join([ans for _, ans in problems])
        pdf.add_text(80, y, f"  Set {page_num}: {answers_str}", font='F3', size=9)
        y -= 20

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book54_Brain_Games_Seniors.pdf')
    print("Book 54 created: Book54_Brain_Games_Seniors.pdf")

if __name__ == '__main__':
    create_book()
