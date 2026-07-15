"""Book 304: GROWING TOGETHER - A Fruits of the Spirit Family Devotional & Activity Book"""
import random
from pdf_utils import PDFDoc

random.seed(304)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    fruits = [
        ("LOVE", "Galatians 5:22", "The fruit of the Spirit is love.", "Love is choosing to put others first, even when it's hard."),
        ("JOY", "Galatians 5:22", "The fruit of the Spirit is joy.", "Joy is happiness that doesn't depend on circumstances."),
        ("PEACE", "Galatians 5:22", "The fruit of the Spirit is peace.", "Peace is calm confidence that God is in control."),
        ("LONGSUFFERING", "Galatians 5:22", "The fruit of the Spirit is longsuffering.", "Patience is waiting without complaining, trusting God's timing."),
        ("GENTLENESS", "Galatians 5:22", "The fruit of the Spirit is gentleness.", "Gentleness is strength under control - being kind when you could be harsh."),
        ("GOODNESS", "Galatians 5:22", "The fruit of the Spirit is goodness.", "Goodness is doing the right thing because it reflects God's character."),
        ("FAITH", "Galatians 5:22", "The fruit of the Spirit is faith.", "Faithfulness is being trustworthy and keeping your promises."),
        ("MEEKNESS", "Galatians 5:23", "The fruit of the Spirit is meekness.", "Meekness is humility - not thinking less of yourself, but thinking of yourself less."),
        ("TEMPERANCE", "Galatians 5:23", "The fruit of the Spirit is temperance.", "Self-control is saying no to wrong and yes to right, even when feelings disagree."),
    ]
    
    daily_themes = ["LEARN", "PRACTICE", "SHARE", "CHALLENGE", "CREATE", "PRAY", "CELEBRATE"]
    
    def make_word_search(words, size=10):
        grid = [['.' for _ in range(size)] for _ in range(size)]
        for word in words:
            wu = word.upper()[:size]
            for attempt in range(30):
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
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(30, 30, 552, 732, 3, 0.2)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_centered_text(700, "GROWING TOGETHER", 'F2', 26, 0.1)
    doc.add_centered_text(665, "A Fruits of the Spirit", 'F4', 16, 0.25)
    doc.add_centered_text(640, "Family Devotional & Activity Book", 'F4', 14, 0.3)
    doc.add_filled_rect(130, 370, 352, 180, 0.90)
    doc.add_rect(130, 370, 352, 180, 2, 0.3)
    doc.add_centered_text(500, "[ILLUSTRATION: family tree with", 'F3', 10, 0.4)
    doc.add_centered_text(485, "9 different fruits hanging from branches,", 'F3', 10, 0.4)
    doc.add_centered_text(470, "each labeled with a fruit of the Spirit]", 'F3', 10, 0.4)
    doc.add_centered_text(250, "9 Fruits + 7 Days Each = 10 Weeks of Family Growth", 'F1', 10, 0.35)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "GROWING TOGETHER", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "For families with children ages 5-12.", 'F1', 10, 0.3)
    doc.add_text(72, 575, "Published by KDP Amazon", 'F1', 10, 0.3)
    
    # Intro page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "WELCOME, FAMILY!", 'F2', 18, 0.1)
    y = 685
    intro = [
        "This book is designed for your WHOLE FAMILY to do together.",
        "",
        "Over 10 weeks (1 intro week + 9 fruit weeks), you'll explore",
        "the Fruits of the Spirit from Galatians 5:22-23.",
        "",
        "EACH WEEK HAS 7 DAILY ACTIVITIES:",
        "  Day 1: LEARN - Read about the fruit together",
        "  Day 2: PRACTICE - Do a hands-on activity",
        "  Day 3: SHARE - Discussion time as a family",
        "  Day 4: CHALLENGE - A real-life family challenge",
        "  Day 5: CREATE - Coloring, drawing, or crafting",
        "  Day 6: PRAY - Family prayer time",
        "  Day 7: CELEBRATE - Review and reward!",
        "",
        "HOW TO USE:",
        "  - Pick a consistent time (dinner, bedtime, morning)",
        "  - Let every family member participate",
        "  - It only takes 10-15 minutes per day!",
        "  - Celebrate progress, not perfection",
    ]
    for line in intro:
        if line.startswith("This book") or line.startswith("EACH") or line.startswith("HOW"):
            doc.add_text(72, y, line, 'F2', 10, 0.15)
        else:
            doc.add_text(72, y, line, 'F1', 10, 0.25)
        y -= 17
    
    # Intro week page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "INTRO WEEK: WHAT ARE THE FRUITS?", 'F2', 14, 0.1)
    y = 700
    doc.add_text(72, y, "Galatians 5:22-23 (KJV):", 'F2', 11, 0.15)
    y -= 20
    doc.add_text(72, y, "\"But the fruit of the Spirit is love, joy, peace,", 'F4', 11, 0.2)
    y -= 16
    doc.add_text(72, y, "longsuffering, gentleness, goodness, faith,", 'F4', 11, 0.2)
    y -= 16
    doc.add_text(72, y, "meekness, temperance: against such there is no law.\"", 'F4', 11, 0.2)
    y -= 30
    doc.add_text(72, y, "FAMILY DISCUSSION:", 'F2', 11, 0.15)
    y -= 18
    questions = [
        "What is a fruit? (Something that grows from a healthy tree!)",
        "Who is the Spirit? (God's Holy Spirit who lives in believers)",
        "Can we grow these fruits on our own? (No! The Spirit grows them)",
        "Which fruit do you think our family needs most right now?",
    ]
    for q in questions:
        doc.add_text(72, y, f"- {q}", 'F1', 9, 0.3)
        y -= 18
    y -= 10
    doc.add_text(72, y, "FAMILY FRUIT TRACKER (check off each fruit as you study it):", 'F2', 10, 0.15)
    y -= 20
    for fruit, _, _, _ in fruits:
        doc.add_text(72, y, f"[ ] {fruit}", 'F1', 10, 0.3)
        y -= 18
    
    # 9 fruits x 7 days each  
    for f_idx, (fruit, ref, verse, definition) in enumerate(fruits):
        for day_idx in range(7):
            doc.new_page()
            fill = 0.90 + random.uniform(0, 0.07)
            doc.add_filled_rect(0, 0, 612, 792, fill)
            doc.add_rect(40, 40, 532, 712, 2, 0.3)
            
            # Header
            doc.add_filled_rect(40, 745, 532, 30, 0.88)
            doc.add_rect(40, 745, 532, 30, 1, 0.3)
            doc.add_text(55, 755, f"Week {f_idx+2}: {fruit} - Day {day_idx+1}: {daily_themes[day_idx]}", 'F2', 11, 0.1)
            
            # Verse box
            doc.add_filled_rect(55, 700, 502, 30, 0.92)
            doc.add_rect(55, 700, 502, 30, 1, 0.4)
            doc.add_text(65, 710, f"{ref} - \"{verse}\"", 'F4', 9, 0.2)
            
            y = 680
            
            if day_idx == 0:  # LEARN
                doc.add_text(72, y, f"WHAT IS {fruit}?", 'F2', 12, 0.15)
                y -= 20
                doc.add_text(72, y, definition, 'F4', 10, 0.25)
                y -= 25
                doc.add_text(72, y, "FAMILY VERSE (read together 3 times):", 'F2', 10, 0.15)
                y -= 18
                doc.add_text(90, y, verse, 'F5', 11, 0.2)
                y -= 25
                doc.add_text(72, y, "DISCUSSION: When have you seen this fruit in our family?", 'F2', 10, 0.15)
                y -= 18
                for _ in range(4):
                    doc.add_line(72, y, 540, y, 0.5, 0.5)
                    y -= 18
                y -= 10
                doc.add_text(72, y, "FRUIT CHECK: Rate our family (1=growing, 5=ripe!):", 'F2', 10, 0.15)
                y -= 18
                doc.add_text(72, y, "[ 1 ]  [ 2 ]  [ 3 ]  [ 4 ]  [ 5 ]", 'F1', 11, 0.3)
                
            elif day_idx == 1:  # PRACTICE
                doc.add_text(72, y, f"PRACTICE {fruit} TODAY:", 'F2', 12, 0.15)
                y -= 22
                activities = {
                    "LOVE": "Each family member writes a love note to someone else.",
                    "JOY": "Have a family dance party! Play worship music and CELEBRATE.",
                    "PEACE": "Practice 5 minutes of family silence together. Just breathe.",
                    "LONGSUFFERING": "Play a waiting game - see who can wait longest for a treat!",
                    "GENTLENESS": "Speak in whispers for one hour. Notice how it changes the mood.",
                    "GOODNESS": "Do a secret good deed for a neighbor together.",
                    "FAITH": "Each person shares one thing they're trusting God for.",
                    "MEEKNESS": "Let someone else go first ALL day. No arguing about turns.",
                    "TEMPERANCE": "Set a timer. No screens for 2 hours. What will you do instead?",
                }
                doc.add_text(72, y, activities[fruit], 'F4', 10, 0.25)
                y -= 30
                doc.add_text(72, y, "How did it go?", 'F2', 10, 0.15)
                y -= 18
                for _ in range(4):
                    doc.add_line(72, y, 540, y, 0.5, 0.5)
                    y -= 18
                y -= 10
                doc.add_text(72, y, "What was hard about it?", 'F2', 10, 0.15)
                y -= 18
                for _ in range(3):
                    doc.add_line(72, y, 540, y, 0.5, 0.5)
                    y -= 18
                    
            elif day_idx == 2:  # SHARE
                doc.add_text(72, y, "FAMILY SHARING TIME:", 'F2', 12, 0.15)
                y -= 22
                doc.add_text(72, y, f"Each person answers about {fruit}:", 'F4', 10, 0.25)
                y -= 22
                share_qs = [
                    f"1. When is it HARDEST to show {fruit.lower()}?",
                    f"2. Who is someone you know who shows great {fruit.lower()}?",
                    f"3. How can our family grow more {fruit.lower()} this week?",
                    "4. What would change if EVERYONE showed this fruit?",
                ]
                for q in share_qs:
                    doc.add_text(72, y, q, 'F1', 10, 0.25)
                    y -= 16
                    for _ in range(2):
                        doc.add_line(90, y, 540, y, 0.5, 0.5)
                        y -= 16
                    y -= 8
                    
            elif day_idx == 3:  # CHALLENGE
                doc.add_text(72, y, f"FAMILY {fruit} CHALLENGE:", 'F2', 12, 0.15)
                y -= 22
                challenges = {
                    "LOVE": "Show love to 5 people outside your family today.",
                    "JOY": "Find 10 things to be joyful about - even silly ones!",
                    "PEACE": "No arguing or raised voices for the entire day.",
                    "LONGSUFFERING": "Wait without complaining every time you have to wait today.",
                    "GENTLENESS": "Use only gentle words and gentle touches all day.",
                    "GOODNESS": "Do 3 good deeds as a family before bedtime.",
                    "FAITH": "Trust God with something specific together as a family.",
                    "MEEKNESS": "Put others first in EVERY decision today.",
                    "TEMPERANCE": "Practice self-control with food, words, and screen time.",
                }
                doc.add_text(72, y, challenges[fruit], 'F4', 10, 0.25)
                y -= 30
                doc.add_text(72, y, "Did we complete the challenge?  [ ] YES!  [ ] Mostly  [ ] Trying!", 'F1', 10, 0.3)
                y -= 25
                doc.add_text(72, y, "What happened:", 'F2', 10, 0.15)
                y -= 18
                for _ in range(5):
                    doc.add_line(72, y, 540, y, 0.5, 0.5)
                    y -= 18
                    
            elif day_idx == 4:  # CREATE
                doc.add_text(72, y, f"CREATE: DRAW YOUR FAMILY SHOWING {fruit}!", 'F2', 12, 0.15)
                y -= 15
                doc.add_filled_rect(60, y-350, 492, 350, 0.97)
                doc.add_rect(60, y-350, 492, 350, 1, 0.4)
                doc.add_centered_text(y-150, "[DRAWING SPACE]", 'F3', 12, 0.5)
                doc.add_centered_text(y-180, f"Draw your family showing {fruit.lower()}", 'F3', 9, 0.4)
                
            elif day_idx == 5:  # PRAY
                doc.add_text(72, y, "FAMILY PRAYER TIME:", 'F2', 12, 0.15)
                y -= 22
                doc.add_text(72, y, f"Pray together for more {fruit.lower()} in your family:", 'F4', 10, 0.25)
                y -= 25
                doc.add_text(72, y, f"\"Dear God, thank You for the fruit of {fruit.lower()}.", 'F4', 10, 0.25)
                y -= 16
                doc.add_text(72, y, f"Help our family to grow in {fruit.lower()} this week.", 'F4', 10, 0.25)
                y -= 16
                doc.add_text(72, y, "Show us where we need to improve. Give us Your Spirit", 'F4', 10, 0.25)
                y -= 16
                doc.add_text(72, y, "to produce this fruit in our lives. In Jesus' name, Amen.\"", 'F4', 10, 0.25)
                y -= 30
                doc.add_text(72, y, "Each person: what do YOU want to pray about?", 'F2', 10, 0.15)
                y -= 18
                for member in ["Parent/Guardian:", "Child 1:", "Child 2:", "Child 3:"]:
                    doc.add_text(72, y, f"{member} ________________________________", 'F1', 10, 0.3)
                    y -= 22
                    
            elif day_idx == 6:  # CELEBRATE
                doc.add_text(72, y, f"CELEBRATE {fruit} WEEK!", 'F2', 12, 0.15)
                y -= 22
                doc.add_text(72, y, "Review: What did our family learn this week?", 'F2', 10, 0.15)
                y -= 18
                for _ in range(3):
                    doc.add_line(72, y, 540, y, 0.5, 0.5)
                    y -= 18
                y -= 8
                doc.add_text(72, y, "Who showed the MOST fruit this week?", 'F2', 10, 0.15)
                y -= 18
                doc.add_line(72, y, 540, y, 0.5, 0.5)
                y -= 25
                doc.add_text(72, y, f"Rate our family's {fruit.lower()} growth:", 'F2', 10, 0.15)
                y -= 18
                doc.add_text(72, y, "Start of week: [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ]", 'F1', 10, 0.3)
                y -= 18
                doc.add_text(72, y, "End of week:   [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ]", 'F1', 10, 0.3)
                y -= 25
                doc.add_text(72, y, "FAMILY PRAYER:", 'F2', 10, 0.15)
                y -= 18
                for _ in range(4):
                    doc.add_line(72, y, 540, y, 0.5, 0.5)
                    y -= 18
    
    # Extra pages to reach 72+
    extras_304 = ["FAMILY FRUIT NOTES", "OUR FAMILY PRAYERS", "FRUIT WE GREW THIS SEASON", "MEMORIES"]
    for et in extras_304:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, et, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22

    # Final celebration page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.90)
    doc.add_rect(30, 30, 552, 732, 3, 0.2)
    doc.add_centered_text(700, "YOU GREW TOGETHER!", 'F2', 20, 0.1)
    doc.add_centered_text(665, "10 weeks of family fruit-growing!", 'F4', 13, 0.25)
    y = 630
    doc.add_text(72, y, "FRUITS COMPLETED:", 'F2', 12, 0.15)
    y -= 22
    for fruit, _, _, _ in fruits:
        doc.add_text(72, y, f"[ ] {fruit}", 'F1', 11, 0.3)
        y -= 18
    y -= 15
    doc.add_centered_text(y, "\"But the fruit of the Spirit is love, joy, peace...\"", 'F5', 11, 0.2)
    doc.add_centered_text(y-18, "- Galatians 5:22", 'F4', 10, 0.3)
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book304_Fruits_Spirit_Family.pdf')
    print("Book304_Fruits_Spirit_Family.pdf created successfully!")

if __name__ == "__main__":
    create_book()
