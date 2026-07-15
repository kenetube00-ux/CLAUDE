"""Book 294: THE ARMOR OF GOD - Interactive Activity Book for Kids Ages 8-12"""
import random
from pdf_utils import PDFDoc

random.seed(294)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    armor_pieces = [
        ("THE BELT OF TRUTH", "Ephesians 6:14a", "Stand therefore, having your loins girt about with truth.",
         "truth", "A belt holds everything together. Truth holds YOUR life together!"),
        ("THE BREASTPLATE OF RIGHTEOUSNESS", "Ephesians 6:14b", "Having on the breastplate of righteousness.",
         "righteousness", "A breastplate protects your heart. Doing right protects YOUR heart!"),
        ("THE SHOES OF PEACE", "Ephesians 6:15", "And your feet shod with the preparation of the gospel of peace.",
         "peace", "Good shoes help you stand firm. Peace helps YOU stand strong!"),
        ("THE SHIELD OF FAITH", "Ephesians 6:16", "Taking the shield of faith, wherewith ye shall be able to quench all the fiery darts.",
         "faith", "A shield blocks attacks. Faith blocks the enemy's lies!"),
        ("THE HELMET OF SALVATION", "Ephesians 6:17a", "And take the helmet of salvation.",
         "salvation", "A helmet protects your head. Salvation protects your MIND!"),
        ("THE SWORD OF THE SPIRIT", "Ephesians 6:17b", "And the sword of the Spirit, which is the word of God.",
         "spirit", "A sword is for battle. God's Word is YOUR weapon!"),
        ("PRAYER", "Ephesians 6:18", "Praying always with all prayer and supplication in the Spirit.",
         "prayer", "Prayer connects you to headquarters. It's your communication line to God!"),
    ]
    
    def make_word_search(words, size=12):
        grid = [['.' for _ in range(size)] for _ in range(size)]
        placed = []
        for word in words:
            word_upper = word.upper()
            attempts = 0
            while attempts < 50:
                direction = random.choice([(0,1),(1,0),(1,1)])
                r = random.randint(0, size - 1)
                c = random.randint(0, size - 1)
                dr, dc = direction
                if r + dr * len(word_upper) > size or c + dc * len(word_upper) > size:
                    attempts += 1
                    continue
                fits = True
                for k, ch in enumerate(word_upper):
                    gr = r + dr * k
                    gc = c + dc * k
                    if grid[gr][gc] != '.' and grid[gr][gc] != ch:
                        fits = False
                        break
                if fits:
                    for k, ch in enumerate(word_upper):
                        grid[r + dr*k][c + dc*k] = ch
                    placed.append(word_upper)
                    break
                attempts += 1
        # Fill remaining
        for r in range(size):
            for c in range(size):
                if grid[r][c] == '.':
                    grid[r][c] = chr(random.randint(65, 90))
        return grid, placed
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(25, 25, 562, 742, 3, 0.2)
    doc.add_rect(35, 35, 542, 722, 1, 0.5)
    doc.add_centered_text(700, "THE ARMOR OF GOD", 'F2', 28, 0.1)
    doc.add_centered_text(665, "Interactive Activity Book", 'F4', 18, 0.25)
    doc.add_centered_text(640, "for Kids Ages 8-12", 'F4', 16, 0.3)
    doc.add_filled_rect(120, 350, 372, 220, 0.90)
    doc.add_rect(120, 350, 372, 220, 2, 0.3)
    doc.add_centered_text(530, "[ILLUSTRATION: kid warrior with full", 'F3', 10, 0.4)
    doc.add_centered_text(515, "armor of God, cartoon style, bold colors]", 'F3', 10, 0.4)
    doc.add_centered_text(400, "Coloring + Word Searches + Activities", 'F1', 11, 0.35)
    doc.add_centered_text(200, "Put on the WHOLE armor of God!", 'F2', 14, 0.2)
    doc.add_centered_text(175, "- Ephesians 6:11", 'F4', 12, 0.3)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "THE ARMOR OF GOD", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "For ages 8-12. Published by KDP Amazon.", 'F1', 10, 0.3)
    
    # Intro page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "SUIT UP, SOLDIER!", 'F2', 20, 0.1)
    y = 680
    intro = [
        "Did you know that God gives you REAL armor?",
        "",
        "Not metal armor you can touch - but SPIRITUAL armor",
        "that protects you from the enemy's tricks!",
        "",
        "In Ephesians 6:10-18, God tells us about 7 pieces of armor:",
        "",
        "  1. Belt of Truth",
        "  2. Breastplate of Righteousness",
        "  3. Shoes of Peace",
        "  4. Shield of Faith",
        "  5. Helmet of Salvation",
        "  6. Sword of the Spirit (God's Word)",
        "  7. Prayer",
        "",
        "In this book, you'll learn about EACH piece through:",
        "  * A story that shows why it matters",
        "  * Coloring pages  * Word searches",
        "  * Fun activities  * Quizzes",
        "  * Drawing challenges  * Real-life missions!",
        "",
        "Are you ready to SUIT UP? Let's go!",
    ]
    for line in intro:
        if "Did you know" in line or "Are you ready" in line:
            doc.add_text(72, y, line, 'F2', 12, 0.1)
        else:
            doc.add_text(72, y, line, 'F1', 11, 0.25)
        y -= 18
    
    # 7 armor sections - each 9+ pages
    for idx, (title, ref, verse, keyword, explanation) in enumerate(armor_pieces):
        # Section title page
        doc.new_page()
        fill = 0.88 + random.uniform(0, 0.07)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(30, 30, 552, 732, 3, 0.2)
        doc.add_filled_rect(80, 400, 452, 250, 0.92)
        doc.add_rect(80, 400, 452, 250, 2, 0.3)
        doc.add_centered_text(700, f"PIECE #{idx+1}", 'F1', 14, 0.3)
        doc.add_centered_text(620, title, 'F2', 20, 0.1)
        doc.add_centered_text(580, ref, 'F4', 12, 0.3)
        doc.add_centered_text(520, f"[ILLUSTRATION: cartoon {keyword} armor piece", 'F3', 9, 0.4)
        doc.add_centered_text(505, f"with action lines and sparkles]", 'F3', 9, 0.4)
        doc.add_centered_text(440, f'"{verse}"', 'F4', 10, 0.25)
        doc.add_centered_text(200, explanation, 'F2', 11, 0.2)
        
        # Story page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.95)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, f"THE STORY: {title}", 'F2', 14, 0.1)
        doc.add_line(120, 725, 492, 725, 1, 0.3)
        y = 700
        stories = {
            "truth": [
                "Marcus was at school when his friend Jayden started a rumor about",
                "another kid. 'Just go along with it,' Jayden said. 'It's funny.'",
                "",
                "Marcus felt his stomach twist. He knew it wasn't true.",
                "",
                "'I'm not going to say that,' Marcus said. 'It's not true and",
                "it could really hurt him.'",
                "",
                "Some kids laughed at Marcus. But by the end of the day, the kid",
                "who was being talked about came up to Marcus and said, 'Thanks",
                "for standing up for me.'",
                "",
                "That night, Marcus felt PEACE. The belt of truth kept him",
                "standing when it would have been easier to go along with the lie.",
                "",
                "TRUTH holds your life together - just like a belt holds",
                "a soldier's armor in place!",
            ],
            "righteousness": [
                "Sophia found a wallet on the playground with $20 inside.",
                "Nobody was looking. She could keep it and nobody would know.",
                "",
                "'Finders keepers!' her friend whispered.",
                "",
                "But Sophia remembered what her Sunday school teacher said:",
                "'Doing the right thing protects your heart.' She took the wallet",
                "to the office. The boy who lost it was SO happy.",
                "",
                "Sophia's friend was confused. 'Why didn't you keep it?'",
                "",
                "'Because doing wrong stuff makes my heart feel heavy,'",
                "Sophia said. 'I'd rather feel clean inside.'",
                "",
                "The breastplate of RIGHTEOUSNESS protects your heart from",
                "the heavy feeling that comes from doing wrong!",
            ],
            "peace": [
                "Tyler's parents were fighting again. He could hear them",
                "downstairs. His stomach was in knots. He felt scared.",
                "",
                "Then he remembered his verse: the gospel of PEACE.",
                "",
                "He closed his eyes and whispered, 'God, I need Your peace",
                "right now. I can't control what's happening downstairs,",
                "but You can control what's happening in my heart.'",
                "",
                "Slowly, the knot in his stomach loosened. He still heard the",
                "noise, but something shifted inside him. He wasn't shaking anymore.",
                "",
                "The shoes of peace help you STAND FIRM even when the ground",
                "around you is shaking!",
            ],
            "faith": [
                "Emma was terrified of the dark. Every night she imagined",
                "monsters in her closet and under her bed.",
                "",
                "Her dad told her about the SHIELD OF FAITH.",
                "'When scary thoughts come,' he said, 'they're like flaming",
                "arrows. Your faith is a shield that blocks them.'",
                "",
                "That night when the fear came, Emma whispered:",
                "'God is with me. God is bigger than anything in the dark.",
                "I trust Him.' She imagined holding up a giant shield.",
                "",
                "The fear didn't disappear instantly - but it got smaller.",
                "Each night she used her shield, it got easier.",
                "",
                "FAITH blocks the enemy's attacks on your mind!",
            ],
            "salvation": [
                "Jake used to think God could never love someone like him.",
                "He'd messed up too many times. The voice in his head said:",
                "'You're too bad for God. Give up.'",
                "",
                "But then his youth leader explained SALVATION:",
                "'God already knows everything you've done. And He STILL",
                "chose to save you. You can't lose His love.'",
                "",
                "It was like putting on a helmet that blocked all the lies.",
                "",
                "'But what about when I mess up again?' Jake asked.",
                "",
                "'That's what grace is for. The helmet stays on.'",
                "",
                "The helmet of SALVATION protects your thoughts from the",
                "lie that you're not good enough for God!",
            ],
            "spirit": [
                "When the bully cornered Ana and said horrible things about her,",
                "she didn't fight back with fists or mean words.",
                "",
                "Instead she said: 'The Bible says I am fearfully and",
                "wonderfully made. God loves me and nothing you say can change that.'",
                "",
                "The bully was speechless. He expected her to cry or fight.",
                "He didn't expect THE WORD OF GOD.",
                "",
                "Later, Ana told her mom: 'It was like the verse was a sword",
                "that cut through his words!'",
                "",
                "That's EXACTLY what it is. The Sword of the Spirit - God's",
                "Word - is the only offensive weapon in your armor!",
            ],
            "prayer": [
                "David's grandma was really sick. He felt helpless.",
                "'I'm just a kid,' he thought. 'What can I do?'",
                "",
                "Then his mom said: 'You can PRAY. Prayer is the most",
                "powerful thing any of us can do - kid or adult.'",
                "",
                "So David prayed. Not fancy prayers. Just honest ones:",
                "'God, please help Grandma. I'm scared. Please be with her.'",
                "",
                "His grandma didn't get better overnight. But something",
                "changed in DAVID. He felt less helpless. He felt like",
                "he was actually DOING something.",
                "",
                "PRAYER is your direct line to God - the Commander of",
                "the army. Use it ALWAYS!",
            ],
        }
        story = stories.get(keyword, stories["truth"])
        for line in story:
            if line:
                doc.add_text(72, y, line, 'F4', 10, 0.25)
            y -= 15
        
        # Coloring page
        doc.new_page()
        fill = 0.92 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(30, 30, 552, 732, 2, 0.3)
        doc.add_centered_text(740, f"COLOR THIS: {title}", 'F2', 14, 0.1)
        doc.add_filled_rect(60, 200, 492, 500, 0.97)
        doc.add_rect(60, 200, 492, 500, 2, 0.3)
        doc.add_centered_text(550, f"[ILLUSTRATION: detailed coloring page", 'F3', 10, 0.4)
        doc.add_centered_text(530, f"of child warrior wearing {keyword} armor piece", 'F3', 10, 0.4)
        doc.add_centered_text(510, f"with decorative patterns to color]", 'F3', 10, 0.4)
        doc.add_centered_text(100, f'"{verse}"', 'F4', 10, 0.3)
        
        # Word Search page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.94)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(740, f"WORD SEARCH: {title}", 'F2', 14, 0.1)
        
        search_words = {
            "truth": ["TRUTH", "HONEST", "BELT", "STAND", "REAL", "TRUST", "GOD", "LIGHT"],
            "righteousness": ["RIGHT", "HEART", "GOOD", "ARMOR", "CHEST", "GUARD", "HOLY", "PURE"],
            "peace": ["PEACE", "SHOES", "STAND", "FIRM", "CALM", "REST", "STILL", "QUIET"],
            "faith": ["FAITH", "SHIELD", "BLOCK", "TRUST", "BRAVE", "FIRE", "DARTS", "SAFE"],
            "salvation": ["SAVED", "HELMET", "MIND", "HEAD", "GRACE", "FREE", "LOVE", "LIFE"],
            "spirit": ["SWORD", "WORD", "BIBLE", "FIGHT", "POWER", "SPEAK", "VERSE", "SHARP"],
            "prayer": ["PRAY", "TALK", "ASK", "LISTEN", "KNEEL", "ALWAYS", "GOD", "FAITH"],
        }
        words_to_find = search_words.get(keyword, search_words["truth"])
        grid, placed = make_word_search(words_to_find, 12)
        
        # Draw grid
        start_x = 120
        start_y = 650
        cell = 30
        for r in range(12):
            for c in range(12):
                doc.add_rect(start_x + c*cell, start_y - r*cell, cell, cell, 0.5, 0.4)
                doc.add_text(start_x + c*cell + 10, start_y - r*cell + 8, grid[r][c], 'F2', 14, 0.2)
        
        # Word list
        y = 270
        doc.add_text(72, y, "FIND THESE WORDS:", 'F2', 11, 0.15)
        y -= 20
        for w in words_to_find:
            doc.add_text(72, y, f"[ ] {w}", 'F1', 11, 0.3)
            y -= 18
        
        # Activity page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, f"ACTIVITY: {title}", 'F2', 14, 0.1)
        y = 700
        doc.add_text(72, y, f"FILL IN THE BLANKS:", 'F2', 12, 0.15)
        y -= 25
        words_v = verse.split()
        blanks = random.sample(range(len(words_v)), min(3, len(words_v)))
        display = []
        for k, w in enumerate(words_v):
            if k in blanks:
                display.append("_" * len(w))
            else:
                display.append(w)
        blank_verse = " ".join(display)
        blines = []
        cur = ""
        for w in blank_verse.split():
            if len(cur + " " + w) > 55:
                blines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            blines.append(cur)
        for ln in blines:
            doc.add_text(90, y, ln, 'F4', 11, 0.25)
            y -= 18
        
        y -= 25
        doc.add_text(72, y, "DECODE THE MESSAGE:", 'F2', 12, 0.15)
        y -= 22
        # Simple number code
        coded_word = keyword.upper()
        code_str = " ".join([str(ord(c) - 64) for c in coded_word])
        doc.add_text(90, y, f"Use A=1, B=2, C=3... Z=26 to decode: {code_str}", 'F1', 10, 0.3)
        y -= 18
        doc.add_text(90, y, f"Answer: __ __ __ __ __ {'__ ' * (len(coded_word)-5) if len(coded_word)>5 else ''}", 'F1', 10, 0.3)
        
        y -= 35
        doc.add_text(72, y, "TRUE OR FALSE:", 'F2', 12, 0.15)
        y -= 22
        tf_questions = {
            "truth": [("The belt of truth helps us tell lies.", "FALSE"), ("Truth holds our life together.", "TRUE"), ("God wants us to be honest.", "TRUE")],
            "righteousness": [("We can protect our hearts by doing wrong.", "FALSE"), ("Righteousness means doing what is right.", "TRUE"), ("A breastplate covers your back.", "FALSE")],
            "peace": [("The shoes of peace help us run away.", "FALSE"), ("God's peace helps us stand firm.", "TRUE"), ("We can have peace even in hard times.", "TRUE")],
            "faith": [("The shield of faith blocks the enemy's lies.", "TRUE"), ("Faith means we never feel scared.", "FALSE"), ("Trust in God grows stronger with practice.", "TRUE")],
            "salvation": [("The helmet protects our feet.", "FALSE"), ("Salvation means God saved us.", "TRUE"), ("We have to be perfect for God to love us.", "FALSE")],
            "spirit": [("The sword of the Spirit is a real metal sword.", "FALSE"), ("God's Word is a weapon against evil.", "TRUE"), ("We should memorize Bible verses.", "TRUE")],
            "prayer": [("Prayer is only for adults.", "FALSE"), ("God hears every prayer.", "TRUE"), ("We should pray only on Sundays.", "FALSE")],
        }
        for q, a in tf_questions.get(keyword, tf_questions["truth"]):
            doc.add_text(90, y, f"[ ] T  [ ] F  -  {q}", 'F1', 10, 0.3)
            y -= 20
        
        # Application page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.95)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, f"REAL LIFE: {title}", 'F2', 14, 0.1)
        y = 700
        doc.add_text(72, y, "When might you need this armor piece? Write or draw:", 'F2', 11, 0.15)
        y -= 25
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 20
        y -= 10
        doc.add_text(72, y, "DRAW YOURSELF wearing this armor piece:", 'F2', 11, 0.15)
        y -= 15
        doc.add_filled_rect(100, y-250, 412, 250, 0.97)
        doc.add_rect(100, y-250, 412, 250, 1, 0.4)
        doc.add_centered_text(y-100, "[YOUR DRAWING HERE]", 'F3', 12, 0.5)
        
        # Challenge page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.92)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, f"THIS WEEK'S CHALLENGE", 'F2', 14, 0.1)
        doc.add_line(170, 725, 442, 725, 1, 0.3)
        y = 695
        challenges = {
            "truth": ["Tell the truth even when it's hard - every day this week.", "Keep a truth journal - write one truth about God each day.", "Memorize the verse by Friday!"],
            "righteousness": ["Do one right thing nobody will see each day.", "Help someone without being asked.", "Memorize the verse by Friday!"],
            "peace": ["When something upsets you, pause and pray for peace first.", "Be a peacemaker - help two people resolve an argument.", "Memorize the verse by Friday!"],
            "faith": ["Write down 3 things you're trusting God for.", "Tell someone about one time God came through for you.", "Memorize the verse by Friday!"],
            "salvation": ["Write a letter thanking God for saving you.", "Tell a friend what salvation means to you.", "Memorize the verse by Friday!"],
            "spirit": ["Read your Bible every day this week (even just one verse).", "Use a verse when you feel attacked by negative thoughts.", "Memorize the verse by Friday!"],
            "prayer": ["Pray every morning before school this week.", "Pray for 3 different people each day.", "Memorize the verse by Friday!"],
        }
        for c in challenges.get(keyword, challenges["truth"]):
            doc.add_text(72, y, f"* {c}", 'F1', 11, 0.25)
            y -= 25
        
        y -= 15
        doc.add_text(72, y, "MY PROGRESS:", 'F2', 12, 0.15)
        y -= 20
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            doc.add_text(90, y, f"[ ] {day}: ________________________________", 'F1', 10, 0.3)
            y -= 20
        
        # Quiz page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.94)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, f"QUIZ: {title}", 'F2', 14, 0.1)
        y = 700
        doc.add_text(72, y, "1. What does this armor piece protect?", 'F2', 11, 0.15)
        y -= 18
        for _ in range(2):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "2. Write the verse from memory:", 'F2', 11, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "3. Give a real-life example of using this armor:", 'F2', 11, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "4. How did you use it this week?", 'F2', 11, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "5. Rate yourself: How well did you 'wear' this piece?", 'F2', 11, 0.15)
        y -= 18
        doc.add_text(72, y, "[ 1 ]  [ 2 ]  [ 3 ]  [ 4 ]  [ 5 ]  [ 6 ]  [ 7 ]  [ 8 ]  [ 9 ]  [ 10 ]", 'F1', 10, 0.3)
        
        # Drawing/journal page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, f"MY {title} JOURNAL", 'F2', 14, 0.1)
        y = 700
        doc.add_text(72, y, "Draw or write about a time you needed this armor:", 'F2', 10, 0.15)
        y -= 15
        doc.add_filled_rect(72, y-200, 468, 200, 0.97)
        doc.add_rect(72, y-200, 468, 200, 1, 0.4)
        doc.add_centered_text(y-90, "[Draw or write here]", 'F3', 10, 0.5)
        y -= 220
        doc.add_text(72, y, "What I learned about this armor piece:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "My prayer for strength in this area:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
    
    # Final page - Full Armor
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.90)
    doc.add_rect(30, 30, 552, 732, 3, 0.2)
    doc.add_centered_text(730, "YOU'RE SUITED UP!", 'F2', 20, 0.1)
    doc.add_centered_text(695, "You've learned about ALL 7 pieces of God's armor!", 'F4', 12, 0.25)
    y = 650
    for idx, (title, _, _, _, _) in enumerate(armor_pieces):
        doc.add_text(72, y, f"[ ] {idx+1}. {title} - MASTERED!", 'F1', 11, 0.25)
        y -= 22
    y -= 20
    doc.add_centered_text(y, "\"Be strong in the Lord, and in the power of his might.\"", 'F5', 12, 0.2)
    doc.add_centered_text(y-20, "- Ephesians 6:10", 'F4', 10, 0.3)
    
    # Extra activity and review pages
    extras_294 = ["MY ARMOR PRAYER", "DRAW THE FULL ARMOR", "VERSES I MEMORIZED",
                  "MY ARMOR JOURNAL", "TELLING FRIENDS ABOUT THE ARMOR"]
    for et in extras_294:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, et, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        if "DRAW" in et:
            doc.add_filled_rect(72, 150, 468, 530, 0.97)
            doc.add_rect(72, 150, 468, 530, 1, 0.4)
            doc.add_centered_text(420, "[Draw yourself in full armor!]", 'F3', 12, 0.5)
        else:
            y = 695
            for _ in range(28):
                doc.add_line(72, y, 540, y, 0.5, 0.6)
                y -= 22
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book294_Armor_God_Kids.pdf')
    print("Book294_Armor_God_Kids.pdf created successfully!")

if __name__ == "__main__":
    create_book()
