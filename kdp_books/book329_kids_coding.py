from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    chapters = [
        ("What Is Coding?", "Coding is giving instructions to a computer in a language it understands. Computers are super fast but not smart on their own - they need YOU to tell them exactly what to do! Every app on your phone, every video game, every website was built by someone writing code. Coding is like learning a superpower: once you know it, you can create almost anything you imagine. The best part? Anyone can learn, no matter how old you are.", 
         "Think of coding like writing a recipe. If you leave out a step or put steps in the wrong order, the recipe fails. Computers follow instructions perfectly - but only if those instructions are perfect too!",
         ["Write step-by-step instructions for making a sandwich - be VERY specific", "Have a friend follow your instructions EXACTLY - what went wrong?", "List 5 things in your life that use computer code"]),
        ("Algorithms in Daily Life", "An algorithm is just a step-by-step set of instructions to solve a problem or complete a task. You already use algorithms every day without knowing it! Getting dressed is an algorithm: underwear first, then pants, then shirt, then shoes. Brushing your teeth is an algorithm. Even your morning routine is a series of steps in a specific order. Programmers write algorithms to tell computers how to solve problems - from simple math to driving cars.",
         "A good algorithm is: 1) Clear (no confusion), 2) Complete (nothing missing), 3) In the right order, 4) Has an ending point.",
         ["Write an algorithm for your morning routine (at least 10 steps)", "Create an algorithm for finding the largest number in a list", "Draw a flowchart for deciding what to wear based on weather"]),
        ("Sequences & Order", "A sequence in coding means the ORDER in which instructions happen. Order matters a LOT! Think about it: 'Put on socks, then put on shoes' works great. But 'Put on shoes, then put on socks' is impossible! In coding, if you put instructions in the wrong order, the program breaks or does something unexpected. Every program you use runs line by line in sequence.",
         "The computer reads code from top to bottom, one line at a time. If step 3 needs information from step 2, step 2 MUST come first.",
         ["Arrange these scrambled steps to make them work correctly", "Write a 5-step sequence for making hot chocolate", "Find the error: what happens if step 3 and 4 are swapped?"]),
        ("Loops: Repeat!", "A loop is a set of instructions that repeats over and over. Without loops, you would have to write the same code hundreds of times! Imagine telling someone to 'clap 100 times.' Would you write 'clap' 100 times? No! You would say 'repeat clapping 100 times.' That is a loop. Loops can repeat a set number of times, or keep going until something happens.",
         "Types: FOR loops repeat a specific number of times. WHILE loops repeat until a condition changes. INFINITE loops never stop (usually a bug!).",
         ["Do 10 jumping jacks - you just used a FOR loop!", "Walk until you reach the wall - you just used a WHILE loop!", "Write pseudocode using REPEAT to draw 4 sides of a square"]),
        ("Conditionals: If/Then", "Conditionals let programs make decisions! IF something is true, THEN do this. ELSE do that. Your brain uses conditionals all day: IF it is raining, THEN take an umbrella. IF the light is red, THEN stop, ELSE go. Without conditionals, programs would do the same thing every time, no matter what. Conditionals make programs smart and responsive.",
         "IF (condition is true) THEN (do action A) ELSE (do action B). You can also chain: IF...ELSE IF...ELSE for multiple options.",
         ["Write IF/THEN rules for: What to wear based on temperature", "Create a yes/no decision tree for choosing a snack", "Write pseudocode: IF score > 90, print A, ELSE IF > 80, print B..."]),
        ("Variables: Containers for Info", "A variable is like a labeled box that holds information. You give it a name and put data inside. The data can change (that is why it is called a VARIABLE!). Example: playerScore = 0. Later: playerScore = 10. The box called playerScore now holds 10 instead of 0. Variables can hold numbers, text, true/false values, and more.",
         "Rules for variables: 1) Give clear names (playerName, not x). 2) They can change value. 3) Each holds one thing at a time.",
         ["Make 3 labeled boxes - put different things in each (name, age, fav color)", "Change a variable: myScore starts at 0, add 5, add 10. What is it now?", "Write pseudocode using variables to calculate area of a rectangle"]),
        ("Debugging: Finding Mistakes", "Debugging means finding and fixing errors in code. The word comes from a real moth found inside a computer in 1947! Every programmer makes mistakes - even experts. The key is learning to find them systematically. Common bugs: typos, wrong order, missing steps, wrong variable names. Good debuggers are patient, logical, and check one thing at a time.",
         "Debugging strategy: 1) Read the error message. 2) Find where it broke. 3) Check what changed. 4) Fix ONE thing and test again.",
         ["Find the 3 bugs in this sandwich algorithm (given scrambled steps)", "Play 'spot the difference' between working and broken code", "Write about a time you solved a problem by trying different solutions"]),
        ("Functions: Mini-Programs", "A function is a reusable chunk of code with a name. Instead of writing the same 10 lines over and over, you write them once as a function and call it by name whenever needed. Example: a 'makeBreakfast' function might contain steps for toast, eggs, and juice. Every time you want breakfast, just call makeBreakfast() instead of rewriting all steps!",
         "Functions: 1) Have a name, 2) May take inputs (ingredients), 3) Do something specific, 4) May give back a result (output).",
         ["Create a function called 'greetPerson' that takes a name as input", "List 3 everyday 'functions' (routine tasks you repeat daily)", "Write a function that calculates the tip at a restaurant"]),
        ("Input & Output", "Programs take INPUT (information going IN), process it, and produce OUTPUT (results coming OUT). When you type your name in a game, that is input. When the game says 'Welcome, [name]!' that is output. A calculator takes number inputs and outputs answers. Understanding input/output helps you design programs that interact with users.",
         "INPUT: keyboard typing, mouse clicks, voice, camera, touch screen. OUTPUT: screen display, sound, printing, vibration.",
         ["List 5 inputs and 5 outputs of your favorite app", "Design a simple app: what inputs does it need? What does it output?", "Write pseudocode that asks for name, then prints a greeting"]),
        ("Simple Game Design Concepts", "Every video game uses the coding concepts you have learned! Games have: LOOPS (the game keeps running), CONDITIONALS (if player hits enemy, lose life), VARIABLES (score, lives, level), FUNCTIONS (jump, attack, move). Game design starts with an idea, then you plan the rules, characters, and win/lose conditions before writing any code.",
         "Game elements: Player, Goal, Obstacles, Rules, Score, Levels, Win/Lose conditions, Game Loop (repeat until game over).",
         ["Design a simple board game using IF/THEN rules", "Plan a video game: character, goal, 3 obstacles, scoring system", "Write pseudocode for a number guessing game"]),
        ("Web Basics: HTML Intro", "Every website you visit is built with HTML (HyperText Markup Language). HTML uses 'tags' to tell the browser what to show. Tags look like this: <h1>Big Title</h1>. The <h1> tag means 'make this a big heading.' HTML is not really programming - it is more like formatting - but it is the foundation of the web. Combined with CSS (styling) and JavaScript (behavior), you can build any website!",
         "Basic tags: <h1> headings, <p> paragraphs, <img> images, <a> links, <ul><li> lists. Every tag that opens must close.",
         ["Write simple HTML for a page about yourself (name, hobbies, picture idea)", "Look at a website and guess what HTML tags were used", "Design a webpage layout on paper before coding it"]),
        ("App Thinking", "Apps solve problems for people. Every app started as an IDEA about how to help someone. App thinking means: 1) Find a problem, 2) Think about who has this problem, 3) Design a solution, 4) Plan the features, 5) Build a simple version first, 6) Get feedback and improve. You do not need to know how to code perfectly to THINK like an app developer!",
         "Start small: the first version of every app is simple. Facebook started as just profiles. Instagram started as just photo filters.",
         ["Identify 3 problems at school or home that an app could solve", "Pick one and design screens on paper (what buttons, what happens)", "Write the user story: As a [user], I want to [action], so that [benefit]"]),
        ("AI Basics for Kids", "Artificial Intelligence (AI) is when computers learn from data instead of just following instructions. Regular programs do exactly what you tell them. AI programs learn patterns and make predictions! When Netflix suggests shows or your phone autocorrects words, that is AI. AI learns from LOTS of examples - like how you learned to recognize cats by seeing thousands of cats.",
         "AI needs: 1) Lots of data (examples), 2) A learning algorithm, 3) Computing power. AI is not magic - it is math and patterns!",
         ["Train a friend: show them 20 drawings and have them guess the pattern", "List 5 places you encounter AI in daily life", "Discuss: what can AI do well? What can humans do better?"]),
        ("Coding Careers", "People who code build the future! Careers include: Software Engineer (builds apps), Game Developer (makes games), Data Scientist (finds patterns in data), Web Developer (builds websites), Cybersecurity Expert (protects systems), Robotics Engineer (programs robots), AI Researcher (teaches computers to learn). All of these are in HIGH demand and pay well!",
         "You do not need to decide now! Try different areas and see what excites you. The best coders love solving puzzles and never stop learning.",
         ["Research 3 coding careers that interest you", "Interview someone who codes for their job (or watch a video)", "Set a goal: what coding skill will you learn this month?"]),
        ("Your Coding Journey Plan", "You have learned the fundamentals of computational thinking! Now what? Start with visual coding tools like Scratch, then try Python or JavaScript. Build small projects. Join coding clubs. Watch tutorials. The key is PRACTICE - code a little bit every day. Every expert programmer started exactly where you are right now. Your coding journey is just beginning!",
         "Resources: Scratch (scratch.mit.edu), Code.org, Khan Academy, Python for Kids books, YouTube coding tutorials.",
         ["Create your 30-day coding challenge plan", "Pick your first language and find a free tutorial", "Start your first project: something small that excites YOU"]),
    ]

    title_page(doc, "CODING FOR KIDS", "Learn to Think Like a Programmer (Ages 8-14)", "15 Chapters * No Computer Needed * Puzzles * Activities")
    copyright_page(doc, "CODING FOR KIDS: Learn to Think Like a Programmer")
    toc_page(doc, [c[0] for c in chapters])

    # Intro
    doc.add_centered_text(720, "WELCOME, FUTURE CODER!", 'F2', 18, 0)
    doc.add_line(180, 710, 432, 710, 1, 0.3)
    y = add_wrapped(doc, 72, 680, "Did you know that coding is the most in-demand skill in the world right now? And the best part is: you do NOT need a computer to start learning how to THINK like a programmer! This book teaches you computational thinking - the logical, creative problem-solving approach that all coders use. Each chapter builds on the last, with real-world examples, hands-on activities (no screen required!), and fun challenges. By the end, you will understand how programs work and be ready to start writing your own code!", 'F4', 12, 0.2)
    doc.new_page()

    for idx, (title, content, key_point, activities) in enumerate(chapters):
        chapter_header(doc, idx+1, title)
        y = 580
        y = add_wrapped(doc, 72, y, content, 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "KEY CONCEPT:", 'F2', 12, 0.1)
        y -= 20
        y = add_wrapped(doc, 90, y, key_point, 'F4', 11, 0.3)
        doc.new_page()

        # Activities page
        doc.add_centered_text(720, f"CHAPTER {idx+1} ACTIVITIES", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        y = 680
        for i, act in enumerate(activities):
            doc.add_filled_rect(60, y-10, 492, 50, 0.95)
            doc.add_text(72, y+20, f"Challenge {i+1}:", 'F2', 11, 0.1)
            y2 = add_wrapped(doc, 72, y, act, 'F1', 11, 0.2, 70)
            y = y2 - 30

        # Pseudocode exercise
        y -= 20
        doc.add_text(72, y, "CODE THIS! (Pseudocode Exercise)", 'F2', 13, 0.1)
        y -= 20
        pseudocode_prompts = [
            "Write step-by-step instructions to sort 5 numbers from smallest to largest.",
            "Write an algorithm that finds a specific word in a list of 20 words.",
            "Arrange these steps to bake a cake in the correct SEQUENCE.",
            "Write a loop that counts from 1 to 20 and prints each number.",
            "Write IF/THEN logic for a vending machine (insert coin, select item, dispense).",
            "Create variables to store: your name, age, grade, and favorite subject.",
            "Here is broken code - find and fix the 3 bugs to make it work.",
            "Write a function called calculateArea that takes width and height.",
            "Design input/output for a calculator that converts Celsius to Fahrenheit.",
            "Write pseudocode for Rock-Paper-Scissors game against the computer.",
            "Write HTML-style tags to structure a simple webpage about your pet.",
            "Plan an app: write the features list and draw 3 screen layouts.",
            "Describe how you would train an AI to recognize dogs vs cats.",
            "Write your ideal coding job description - what would you build?",
            "Create a 4-week learning plan: what will you study each week?",
        ]
        y = add_wrapped(doc, 90, y, pseudocode_prompts[idx], 'F4', 11, 0.3)
        y -= 15
        for _ in range(4):
            doc.add_text(90, y, "_______________________________________________________________", 'F1', 10, 0.4)
            y -= 18
        doc.new_page()

        # Puzzle page
        doc.add_centered_text(720, f"CHAPTER {idx+1} PUZZLE", 'F2', 16, 0)
        doc.add_line(200, 710, 412, 710, 1, 0.3)
        puzzles = [
            "WORD SEARCH: Find these coding words: ALGORITHM, CODE, BUG, LOOP, VARIABLE, FUNCTION, INPUT, OUTPUT, DEBUG, PROGRAM",
            "SEQUENCE PUZZLE: Put these 8 steps for making a phone call in the correct order.",
            "ORDER CHALLENGE: Number these from 1-6 to make a working morning routine.",
            "LOOP PUZZLE: What does this loop print? REPEAT 5 TIMES: print(counter * 2)",
            "DECISION TREE: Follow the IF/THEN paths to find what activity to do today.",
            "VARIABLE TRACKER: Follow the code and write what each variable equals after each line.",
            "BUG HUNT: Find 5 errors in this recipe-algorithm. Circle and fix each one.",
            "FUNCTION MATCH: Match each function name to what it does (draw lines).",
            "I/O MATCHING: Match each input device to its corresponding output.",
            "GAME LOGIC: Fill in the missing IF/THEN rules for this simple game.",
            "TAG MATCHING: Match each HTML tag to the correct description.",
            "APP DESIGN: Sketch 4 screens for a homework reminder app.",
            "PATTERN FINDER: What comes next in each sequence? (AI thinking!)",
            "CAREER QUIZ: Answer 10 questions to discover your ideal coding career path.",
            "CODING BINGO: Complete 5 in a row of coding activities this month!",
        ]
        y = add_wrapped(doc, 72, 680, puzzles[idx], 'F2', 12, 0.1)
        y -= 30
        doc.add_rect(72, y-300, 468, 300, 1, 0.5)
        doc.add_centered_text(y-150, "[Work Space]", 'F1', 14, 0.5)
        doc.new_page()

    # Coding vocabulary
    doc.add_centered_text(720, "CODING VOCABULARY", 'F2', 18, 0)
    vocab = [("Algorithm","Step-by-step instructions"),("Bug","An error in code"),("Debug","Finding and fixing bugs"),("Loop","Code that repeats"),("Variable","A named container for data"),("Function","A reusable block of code"),("Conditional","IF/THEN decision making"),("Input","Data going into a program"),("Output","Results from a program"),("Syntax","The grammar rules of a language")]
    y = 680
    for term, defn in vocab:
        doc.add_text(72, y, f"{term}:", 'F2', 12, 0.1)
        doc.add_text(200, y, defn, 'F1', 11, 0.3)
        y -= 30
    doc.new_page()

    certificate(doc, "FUTURE PROGRAMMER CERTIFICATE")
    add_supplemental(doc, 'Coding', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book329_Kids_Coding_Beginners.pdf')
    print("Book329_Kids_Coding_Beginners.pdf created successfully!")

if __name__ == "__main__":
    create_book()
