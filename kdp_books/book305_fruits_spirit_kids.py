"""Book 305: FRUIT SALAD! - Fruits of the Spirit Activity Book for Kids Ages 5-10"""
import random
from pdf_utils import PDFDoc

random.seed(305)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    fruits = [
        ("LOVE", "A red apple", "Love is being kind to others even when they're not kind to you!"),
        ("JOY", "A bright yellow banana", "Joy is being happy inside because God is with you!"),
        ("PEACE", "A green pear", "Peace is feeling calm because you trust God is in charge!"),
        ("PATIENCE", "An orange", "Patience is waiting without whining or getting upset!"),
        ("KINDNESS", "Purple grapes", "Kindness is treating others the way you want to be treated!"),
        ("GOODNESS", "A pink strawberry", "Goodness is doing the right thing even when no one is watching!"),
        ("FAITHFULNESS", "A blue blueberry", "Faithfulness is keeping your promises and being trustworthy!"),
        ("GENTLENESS", "A peach", "Gentleness is using soft words and being careful with others!"),
        ("SELF-CONTROL", "A watermelon", "Self-control is stopping yourself from doing something wrong!"),
    ]
    
    def make_word_search(words, size=10):
        grid = [['.' for _ in range(size)] for _ in range(size)]
        for word in words:
            wu = word.upper()[:size]
            for attempt in range(40):
                d = random.choice([(0,1),(1,0),(1,1)])
                r = random.randint(0, size-1)
                c = random.randint(0, size-1)
                if r + d[0]*len(wu) > size or c + d[1]*len(wu) > size:
                    continue
                ok = True
                for k, ch in enumerate(wu):
                    if grid[r+d[0]*k][c+d[1]*k] not in ('.', ch):
                        ok = False
                        break
                if ok:
                    for k, ch in enumerate(wu):
                        grid[r+d[0]*k][c+d[1]*k] = ch
                    break
        for r in range(size):
            for c in range(size):
                if grid[r][c] == '.':
                    grid[r][c] = chr(random.randint(65, 90))
        return grid
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(25, 25, 562, 742, 3, 0.2)
    doc.add_rect(35, 35, 542, 722, 1, 0.5)
    doc.add_centered_text(710, "FRUIT SALAD!", 'F2', 32, 0.1)
    doc.add_centered_text(670, "Fruits of the Spirit Activity Book", 'F4', 16, 0.25)
    doc.add_centered_text(645, "for Kids Ages 5-10", 'F4', 14, 0.3)
    doc.add_filled_rect(120, 340, 372, 220, 0.92)
    doc.add_rect(120, 340, 372, 220, 2, 0.3)
    doc.add_centered_text(510, "[ILLUSTRATION: colorful bowl of fruit", 'F3', 10, 0.4)
    doc.add_centered_text(495, "overflowing with 9 different fruits,", 'F3', 10, 0.4)
    doc.add_centered_text(480, "each with a smiling face, cartoon style]", 'F3', 10, 0.4)
    doc.add_centered_text(250, "Coloring + Word Searches + Mazes + Drawing!", 'F1', 11, 0.35)
    doc.add_centered_text(220, "9 Fruits = 72 Pages of FUN!", 'F2', 12, 0.2)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "FRUIT SALAD!", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "For kids ages 5-10. Published by KDP Amazon", 'F1', 10, 0.3)
    
    # Intro for kids
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "HEY THERE, KIDDO!", 'F2', 20, 0.1)
    y = 685
    intro = [
        "Did you know that God grows FRUIT inside you?",
        "",
        "Not real fruit (that would be silly!) but SPECIAL fruit",
        "called the Fruits of the Spirit!",
        "",
        "When you follow Jesus, His Spirit helps you grow:",
        "",
        "  LOVE - JOY - PEACE - PATIENCE - KINDNESS",
        "  GOODNESS - FAITHFULNESS - GENTLENESS - SELF-CONTROL",
        "",
        "That's 9 amazing fruits! And this book has activities",
        "for EACH one:",
        "",
        "  * Stories  * Coloring Pages  * Word Searches",
        "  * Mazes  * Fill-in-the-Blanks  * Drawing",
        "  * Real-Life Application  * Memory Verses",
        "",
        "Ready to make the BEST fruit salad ever?",
        "Let's go! (You might need crayons and a pencil!)",
    ]
    for line in intro:
        if line.startswith("Did") or line.startswith("Ready"):
            doc.add_text(72, y, line, 'F2', 12, 0.1)
        else:
            doc.add_text(72, y, line, 'F1', 11, 0.25)
        y -= 18
    
    # Verse page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "OUR MEMORY VERSE", 'F2', 18, 0.1)
    doc.add_filled_rect(70, 500, 472, 180, 0.95)
    doc.add_rect(70, 500, 472, 180, 2, 0.3)
    doc.add_centered_text(650, "\"But the fruit of the Spirit is", 'F5', 14, 0.15)
    doc.add_centered_text(625, "love, joy, peace, longsuffering,", 'F5', 14, 0.15)
    doc.add_centered_text(600, "gentleness, goodness, faith,", 'F5', 14, 0.15)
    doc.add_centered_text(575, "meekness, temperance.\"", 'F5', 14, 0.15)
    doc.add_centered_text(540, "- Galatians 5:22-23", 'F4', 12, 0.3)
    doc.add_centered_text(400, "Can you memorize this verse by the end of the book?", 'F2', 12, 0.2)
    doc.add_centered_text(370, "Try saying it every day!", 'F1', 11, 0.3)
    
    # 9 fruits x 8 pages each
    for f_idx, (fruit, fruit_name, definition) in enumerate(fruits):
        # Page 1: Story
        doc.new_page()
        fill = 0.89 + random.uniform(0, 0.08)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(30, 30, 552, 732, 3, 0.2)
        doc.add_filled_rect(80, 550, 452, 180, 0.92)
        doc.add_rect(80, 550, 452, 180, 2, 0.3)
        doc.add_centered_text(700, f"FRUIT #{f_idx+1}: {fruit}", 'F2', 20, 0.1)
        doc.add_centered_text(670, f"({fruit_name})", 'F4', 12, 0.3)
        doc.add_centered_text(620, f"[ILLUSTRATION: big cartoon {fruit_name}", 'F3', 9, 0.4)
        doc.add_centered_text(605, f"with a happy face and sparkles]", 'F3', 9, 0.4)
        doc.add_centered_text(570, definition, 'F2', 10, 0.15)
        
        y = 500
        stories = {
            "LOVE": ["Sam saw a new kid sitting alone at lunch. Nobody was talking to him.",
                     "Sam could have stayed with his friends, but he remembered:",
                     "LOVE means being kind to others even when it's not easy.",
                     "So Sam sat with the new kid and said, 'Want to be friends?'",
                     "The new kid smiled SO big. That's the fruit of LOVE!"],
            "JOY": ["Emma's family couldn't go on vacation this year.",
                    "She could have been sad and grumpy all summer.",
                    "But she remembered: JOY comes from knowing God loves her.",
                    "She decided to find fun where she was - backyard camping!",
                    "Joy doesn't need perfect circumstances. That's JOY!"],
            "PEACE": ["Leo's parents were arguing again. His stomach felt sick.",
                     "He went to his room and whispered a prayer:",
                     "'God, please give me PEACE right now.'",
                     "Slowly, his stomach unknotted. He felt calmer.",
                     "PEACE is God's gift when things around us are stormy."],
            "PATIENCE": ["Mia wanted her birthday to come SO badly!",
                        "Every day she asked: 'Is it my birthday yet?'",
                        "Her mom said: 'Patience means trusting that good things come.'",
                        "Mia learned to enjoy each day instead of just waiting.",
                        "PATIENCE makes the waiting easier!"],
            "KINDNESS": ["Jake saw a kid drop all his papers in the hallway.",
                        "Other kids just walked past. Some laughed.",
                        "Jake stopped and helped pick everything up.",
                        "'Thanks!' the kid said. Jake just smiled.",
                        "KINDNESS is helping without being asked!"],
            "GOODNESS": ["Lily found a dollar on the playground.",
                        "Nobody was looking. She could keep it!",
                        "But she knew the right thing was to turn it in.",
                        "She gave it to the teacher. It felt good inside.",
                        "GOODNESS means doing right because God sees!"],
            "FAITHFULNESS": ["Noah promised to feed his dog every morning.",
                           "Some mornings he was tired and didn't want to.",
                           "But a promise is a promise! He got up anyway.",
                           "His dog wagged his tail every single morning.",
                           "FAITHFULNESS means keeping promises even when it's hard!"],
            "GENTLENESS": ["When baby sister knocked over Ava's tower, Ava was MAD.",
                          "She wanted to yell! But she took a deep breath.",
                          "'It's okay, sissy. Let's build a new one together.'",
                          "Her mom said: 'That was SO gentle of you!'",
                          "GENTLENESS is being soft when you could be harsh!"],
            "SELF-CONTROL": ["Ben really wanted to eat ALL the cookies before dinner.",
                           "His body said YES but his brain said WAIT.",
                           "He took one cookie and saved the rest for after dinner.",
                           "At dinner he wasn't too full to eat his veggies!",
                           "SELF-CONTROL is saying 'not now' when you want to say 'NOW!'"],
        }
        story = stories[fruit]
        for line in story:
            doc.add_text(72, y, line, 'F4', 10, 0.25)
            y -= 16
        
        # Page 2: Coloring page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.97)
        doc.add_rect(30, 30, 552, 732, 2, 0.3)
        doc.add_centered_text(740, f"COLOR THE {fruit} FRUIT!", 'F2', 16, 0.1)
        doc.add_filled_rect(60, 150, 492, 550, 0.98)
        doc.add_rect(60, 150, 492, 550, 2, 0.3)
        doc.add_centered_text(500, f"[ILLUSTRATION: Large {fruit_name} to color", 'F3', 11, 0.3)
        doc.add_centered_text(480, f"with kid showing {fruit.lower()} in a scene.", 'F3', 10, 0.3)
        doc.add_centered_text(460, "Bold simple outlines for young kids to color]", 'F3', 10, 0.3)
        doc.add_centered_text(100, f"I will show {fruit.lower()} today!", 'F2', 12, 0.2)
        
        # Page 3: Word search
        doc.new_page()
        fill2 = 0.93 + random.uniform(0, 0.04)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(740, f"{fruit} WORD SEARCH!", 'F2', 16, 0.1)
        
        search_words_map = {
            "LOVE": ["LOVE", "KIND", "CARE", "HELP", "HUG", "GIVE"],
            "JOY": ["JOY", "HAPPY", "SMILE", "SING", "DANCE", "GLAD"],
            "PEACE": ["PEACE", "CALM", "REST", "QUIET", "STILL", "SAFE"],
            "PATIENCE": ["WAIT", "CALM", "TRUST", "SLOW", "HOPE", "STILL"],
            "KINDNESS": ["KIND", "NICE", "HELP", "SHARE", "CARE", "GOOD"],
            "GOODNESS": ["GOOD", "RIGHT", "TRUE", "JUST", "FAIR", "PURE"],
            "FAITHFULNESS": ["FAITH", "TRUST", "KEEP", "TRUE", "LOYAL", "SURE"],
            "GENTLENESS": ["SOFT", "KIND", "MILD", "CALM", "TENDER", "SWEET"],
            "SELF-CONTROL": ["STOP", "WAIT", "THINK", "CALM", "WISE", "HOLD"],
        }
        search_words = search_words_map[fruit]
        grid = make_word_search(search_words, 10)
        
        start_x = 140
        start_y = 650
        cell = 32
        for r in range(10):
            for c in range(10):
                doc.add_rect(start_x + c*cell, start_y - r*cell, cell, cell, 0.5, 0.4)
                doc.add_text(start_x + c*cell + 10, start_y - r*cell + 8, grid[r][c], 'F2', 14, 0.2)
        
        y = 300
        doc.add_text(72, y, "FIND THESE WORDS:", 'F2', 12, 0.15)
        y -= 22
        for w in search_words:
            doc.add_text(72, y, f"[ ] {w}", 'F1', 11, 0.3)
            y -= 18
        
        # Page 4: Maze
        doc.new_page()
        fill3 = 0.94 + random.uniform(0, 0.03)
        doc.add_filled_rect(0, 0, 612, 792, fill3)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(740, f"HELP THE KID FIND THE {fruit} FRUIT!", 'F2', 14, 0.1)
        doc.add_filled_rect(80, 150, 452, 540, 0.97)
        doc.add_rect(80, 150, 452, 540, 2, 0.3)
        doc.add_centered_text(500, "[ILLUSTRATION: Simple maze", 'F3', 11, 0.3)
        doc.add_centered_text(480, f"from a kid at START to a {fruit_name} at FINISH.", 'F3', 10, 0.3)
        doc.add_centered_text(460, "Large paths suitable for young children]", 'F3', 10, 0.3)
        doc.add_text(90, 170, "START -->", 'F2', 12, 0.3)
        doc.add_text(420, 650, f"--> {fruit}!", 'F2', 12, 0.3)
        
        # Page 5: Fill in blanks
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(740, f"FILL IN THE BLANKS: {fruit}", 'F2', 14, 0.1)
        y = 700
        blanks = {
            "LOVE": ["L _ _ E means being k _ _ d to others.", "When I show love, I make God h _ _ _ y.", f"The fruit of the Spirit is L _ _ _. (Galatians 5:22)"],
            "JOY": ["J _ _ is being happy because God l _ _ _ s me.", "I can have joy even on b _ _ days.", "The fruit of the Spirit is J _ _. (Galatians 5:22)"],
            "PEACE": ["P _ _ _ E is feeling c _ _ m inside.", "God gives me peace when I'm s _ _ _ _ d.", "The fruit of the Spirit is P _ _ _ _. (Galatians 5:22)"],
            "PATIENCE": ["P _ _ _ _ _ _ E means w _ _ _ _ _ g without fussing.", "God is patient with m _ too!", "The fruit of the Spirit is P _ _ _ _ _ _ _. (Galatians 5:22)"],
            "KINDNESS": ["K _ _ _ _ _ _ S is helping without being a _ _ _ d.", "I can show kindness to e _ _ _ _ _ _ e.", "The fruit of the Spirit is K _ _ _ _ _ _ _. (Galatians 5:22)"],
            "GOODNESS": ["G _ _ _ _ _ _ S is doing r _ _ _ t things.", "When no one is w _ _ _ _ _ _ g, I still choose good.", "The fruit of the Spirit is G _ _ _ _ _ _ _. (Galatians 5:22)"],
            "FAITHFULNESS": ["F _ _ _ _ _ _ _ _ _ S means keeping p _ _ _ _ _ _ s.", "God is always f _ _ _ _ _ _ l to me!", "The fruit of the Spirit is F _ _ _ _ . (Galatians 5:22)"],
            "GENTLENESS": ["G _ _ _ _ _ _ _ _ S means using s _ _ t words.", "I can be gentle with my h _ _ _ s and words.", "The fruit of the Spirit is G _ _ _ _ _ _ _ _ _. (Galatians 5:23)"],
            "SELF-CONTROL": ["Self-C _ _ _ _ _ _ is saying n _ to wrong things.", "I can s _ _ p and t _ _ _ k before I act.", "The fruit of the Spirit is S _ _ _ - C _ _ _ _ _ _. (Gal 5:23)"],
        }
        for blank in blanks[fruit]:
            doc.add_text(72, y, blank, 'F1', 12, 0.25)
            y -= 30
        y -= 20
        doc.add_text(72, y, "WRITE THE VERSE:", 'F2', 12, 0.15)
        y -= 22
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 25
        
        # Page 6: Drawing page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.95)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(740, f"DRAW YOURSELF SHOWING {fruit}!", 'F2', 14, 0.1)
        doc.add_text(72, 710, f"Draw a picture of YOU showing {fruit.lower()} to someone:", 'F1', 10, 0.3)
        doc.add_filled_rect(60, 150, 492, 540, 0.98)
        doc.add_rect(60, 150, 492, 540, 1, 0.4)
        doc.add_centered_text(420, "[YOUR DRAWING HERE]", 'F3', 14, 0.5)
        doc.add_text(72, 120, f"I showed {fruit.lower()} when I: ________________________________", 'F1', 10, 0.3)
        
        # Page 7: Life application
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.92)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(740, f"REAL LIFE {fruit}!", 'F2', 14, 0.1)
        y = 710
        doc.add_text(72, y, f"How can YOU show {fruit.lower()} this week?", 'F2', 11, 0.15)
        y -= 25
        applications = {
            "LOVE": ["At home: ___________", "At school: ___________", "With friends: ___________", "With family: ___________"],
            "JOY": ["When I'm sad: ___________", "When things don't go my way: ___________", "When I'm bored: ___________", "When it's a hard day: ___________"],
            "PEACE": ["When I'm scared: ___________", "When I'm worried: ___________", "When people are fighting: ___________", "At bedtime: ___________"],
            "PATIENCE": ["When I have to wait: ___________", "When my sibling is annoying: ___________", "In line at school: ___________", "When something takes long: ___________"],
            "KINDNESS": ["To a new kid: ___________", "To my teacher: ___________", "To my parents: ___________", "To someone sad: ___________"],
            "GOODNESS": ["When no one sees: ___________", "When tempted to cheat: ___________", "When I could be lazy: ___________", "When I could lie: ___________"],
            "FAITHFULNESS": ["A promise I'll keep: ___________", "A chore I'll do daily: ___________", "A friend I'll be loyal to: ___________", "A habit I'll build: ___________"],
            "GENTLENESS": ["With my words: ___________", "With my hands: ___________", "With little kids: ___________", "With animals: ___________"],
            "SELF-CONTROL": ["With my mouth: ___________", "With sweets: ___________", "With screen time: ___________", "With my temper: ___________"],
        }
        for app in applications[fruit]:
            doc.add_text(72, y, app, 'F1', 11, 0.3)
            y -= 28
        y -= 15
        doc.add_text(72, y, f"I will try to show {fruit.lower()} by: _______________", 'F2', 10, 0.15)
        y -= 25
        doc.add_text(72, y, "Did I do it?  [ ] YES!  [ ] I tried!  [ ] I'll try again!", 'F1', 10, 0.3)
        
        # Page 8: Memory verse
        doc.new_page()
        fill4 = 0.91 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill4)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(740, f"MEMORY VERSE: {fruit}", 'F2', 14, 0.1)
        doc.add_filled_rect(70, 580, 472, 120, 0.95)
        doc.add_rect(70, 580, 472, 120, 2, 0.3)
        doc.add_centered_text(670, f"\"The fruit of the Spirit is {fruit.lower()}.\"", 'F5', 14, 0.15)
        doc.add_centered_text(640, "- Galatians 5:22-23", 'F4', 11, 0.3)
        doc.add_centered_text(610, "Say it 5 times! Color a star each time:", 'F1', 10, 0.3)
        doc.add_centered_text(590, "* * * * *", 'F2', 20, 0.4)
        
        y = 550
        doc.add_text(72, y, "Write the verse yourself:", 'F2', 11, 0.15)
        y -= 22
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 25
        
        y -= 15
        doc.add_text(72, y, f"Draw the {fruit_name} from memory:", 'F2', 11, 0.15)
        y -= 10
        doc.add_filled_rect(150, y-180, 312, 180, 0.97)
        doc.add_rect(150, y-180, 312, 180, 1, 0.4)
    
    # Final page - fruit salad complete
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.90)
    doc.add_rect(30, 30, 552, 732, 3, 0.2)
    doc.add_centered_text(700, "YOUR FRUIT SALAD IS COMPLETE!", 'F2', 18, 0.1)
    doc.add_centered_text(665, "You learned ALL 9 fruits!", 'F4', 13, 0.25)
    y = 630
    for fruit, fruit_name, _ in fruits:
        doc.add_text(72, y, f"[ ] {fruit} ({fruit_name})", 'F1', 11, 0.3)
        y -= 20
    y -= 15
    doc.add_centered_text(y, "\"The fruit of the Spirit is love, joy, peace...\"", 'F5', 11, 0.2)
    doc.add_centered_text(y-18, "- Galatians 5:22-23", 'F4', 10, 0.3)
    y -= 45
    doc.add_centered_text(y, "Great job! Keep growing God's fruit every day!", 'F2', 12, 0.15)
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book305_Fruits_Spirit_Kids.pdf')
    print("Book305_Fruits_Spirit_Kids.pdf created successfully!")

if __name__ == "__main__":
    create_book()
