"""Book 215: BIBLE PUZZLE FUN - Word Searches, Mazes & Brain Teasers for Kids Ages 7-12 (KIDLYTICAL)"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    random.seed(215)

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.93)
    pdf.add_centered_text(620, "BIBLE PUZZLE FUN!", 'F2', 30)
    pdf.add_centered_text(575, "Word Searches, Mazes &", 'F4', 16, 0.2)
    pdf.add_centered_text(550, "Brain Teasers for Kids Ages 7-12", 'F4', 16, 0.2)
    pdf.add_centered_text(500, "30 Puzzle Pages + Complete Answer Key!", 'F1', 12, 0.3)
    pdf.add_centered_text(470, "KIDLYTICAL", 'F2', 14, 0.4)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "BIBLE PUZZLE FUN", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "Published by KIDLYTICAL Books", 'F1', 9)
    pdf.add_text(72, 610, "For ages 7-12", 'F1', 9)

    # ===== 10 WORD SEARCHES =====
    word_search_themes = [
        ("FRUITS OF THE SPIRIT", ["LOVE", "JOY", "PEACE", "PATIENCE", "KINDNESS", "GOODNESS", "FAITHFUL", "GENTLE", "CONTROL", "SPIRIT"]),
        ("ARMOR OF GOD", ["TRUTH", "RIGHTEOUS", "PEACE", "FAITH", "SALVATION", "SWORD", "SPIRIT", "PRAYER", "HELMET", "SHIELD"]),
        ("12 DISCIPLES", ["PETER", "ANDREW", "JAMES", "JOHN", "PHILIP", "THOMAS", "MATTHEW", "SIMON", "JUDAS", "THADDEUS"]),
        ("BOOKS OF BIBLE - OT", ["GENESIS", "EXODUS", "PSALMS", "PROVERBS", "ISAIAH", "DANIEL", "JONAH", "RUTH", "ESTHER", "JOB"]),
        ("BOOKS OF BIBLE - NT", ["MATTHEW", "MARK", "LUKE", "JOHN", "ACTS", "ROMANS", "HEBREWS", "JAMES", "JUDE", "TITUS"]),
        ("CREATION", ["LIGHT", "SKY", "LAND", "PLANTS", "SUN", "MOON", "STARS", "FISH", "BIRDS", "PEOPLE"]),
        ("MIRACLES OF JESUS", ["WATER", "WINE", "HEAL", "BLIND", "WALK", "FEED", "STORM", "RAISE", "LOAVES", "FISH"]),
        ("PARABLES", ["SOWER", "SEED", "SHEEP", "LOST", "TALENT", "PEARL", "FIELD", "VINE", "MASTER", "LAMP"]),
        ("WOMEN OF BIBLE", ["MARY", "RUTH", "ESTHER", "SARAH", "EVE", "DEBORAH", "HANNAH", "MIRIAM", "LYDIA", "MARTHA"]),
        ("ANIMALS IN BIBLE", ["LION", "LAMB", "DOVE", "FISH", "DONKEY", "CAMEL", "RAVEN", "WHALE", "SERPENT", "EAGLE"]),
    ]

    for ws_num, (theme, words) in enumerate(word_search_themes):
        pdf.new_page()
        pdf.add_centered_text(750, f"WORD SEARCH #{ws_num+1}: {theme}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)

        # Show word list
        pdf.add_text(72, 718, "Find these words:", 'F1', 10)
        # Display in 2 columns
        for i, word in enumerate(words[:5]):
            pdf.add_text(72, 700 - i*14, word, 'F2', 9)
        for i, word in enumerate(words[5:]):
            pdf.add_text(250, 700 - i*14, word, 'F2', 9)

        # Generate grid
        grid_size = 12
        random.seed(ws_num * 47 + 215)
        grid = [[chr(random.randint(65, 90)) for _ in range(grid_size)] for _ in range(grid_size)]

        # Place words in grid (horizontally, rows 0-9)
        for wi, word in enumerate(words):
            if wi < grid_size and len(word) <= grid_size:
                row = wi
                for ci, ch in enumerate(word):
                    grid[row][ci] = ch

        # Draw grid
        y = 615
        for row in grid:
            row_text = "  ".join(row)
            pdf.add_text(110, y, row_text, 'F3', 12)
            y -= 22

    # ===== 10 MAZE PAGES =====
    maze_themes = [
        ("Help Moses reach the Promised Land!", "MOSES", "PROMISED LAND"),
        ("Help David reach Goliath!", "DAVID", "GOLIATH"),
        ("Help Jonah reach Nineveh!", "JONAH", "NINEVEH"),
        ("Help Noah reach the Ark!", "NOAH", "THE ARK"),
        ("Help the Wise Men reach Baby Jesus!", "WISE MEN", "BABY JESUS"),
        ("Help Daniel escape the Lions!", "DANIEL", "FREEDOM"),
        ("Help Ruth reach the Fields!", "RUTH", "HARVEST"),
        ("Help Peter reach Jesus on the water!", "PETER", "JESUS"),
        ("Help Paul reach Rome!", "PAUL", "ROME"),
        ("Help Abraham reach the Promised Land!", "ABRAHAM", "CANAAN"),
    ]

    for maze_num, (title, start_label, end_label) in enumerate(maze_themes):
        pdf.new_page()
        pdf.add_centered_text(750, f"MAZE #{maze_num+1}", 'F2', 16)
        pdf.add_centered_text(730, title, 'F1', 12)
        pdf.add_line(72, 718, 540, 718, 1, 0.5)

        # Maze border
        pdf.add_rect(72, 200, 468, 500, 1.5, 0.3)
        pdf.add_text(82, 685, f"START: {start_label}", 'F2', 10)
        pdf.add_text(440, 215, f"END: {end_label}", 'F2', 10)

        # Generate random walls
        random.seed(maze_num * 73 + 100)
        for _ in range(25):
            wall_type = random.randint(0, 1)
            if wall_type == 0:  # Horizontal wall
                wx = random.randint(90, 480)
                wy = random.randint(230, 670)
                wlen = random.randint(30, 100)
                pdf.add_line(wx, wy, min(wx + wlen, 520), wy, 2, 0.3)
            else:  # Vertical wall
                wx = random.randint(90, 520)
                wy = random.randint(230, 640)
                wlen = random.randint(30, 80)
                pdf.add_line(wx, wy, wx, min(wy + wlen, 680), 2, 0.3)

        # Entry and exit markers
        pdf.add_filled_rect(78, 660, 20, 20, 0.7)
        pdf.add_filled_rect(510, 210, 20, 20, 0.7)

        # Fun fact at bottom
        facts = [
            "Moses led Israel for 40 years in the wilderness!",
            "David was just a shepherd boy when he fought Goliath!",
            "Jonah was inside the fish for 3 days and 3 nights!",
            "Noah's ark was about 450 feet long - bigger than a football field!",
            "The Wise Men traveled hundreds of miles to see Jesus!",
            "Daniel prayed 3 times every day, no matter what!",
            "Ruth worked hard from morning until evening!",
            "Peter walked on water when he looked at Jesus!",
            "Paul wrote 13 books of the New Testament!",
            "Abraham left his home when he was 75 years old!",
        ]
        pdf.add_text(72, 180, f"Fun Fact: {facts[maze_num]}", 'F4', 9, 0.4)

    # ===== 10 BIBLE TRIVIA PAGES =====
    trivia_pages = [
        [("Who built the ark?", "A) Moses", "B) Noah", "C) David", "D) Paul", "B"),
         ("How many days did God take to create the world?", "A) 3", "B) 5", "C) 6", "D) 10", "C"),
         ("What did God create on Day 1?", "A) Animals", "B) Stars", "C) Fish", "D) Light", "D"),
         ("Who was the first man?", "A) Noah", "B) Abraham", "C) Adam", "D) Moses", "C"),
         ("What was the sign of God's promise to Noah?", "A) Star", "B) Rainbow", "C) Cloud", "D) Dove", "B")],
        [("How many disciples did Jesus have?", "A) 7", "B) 10", "C) 12", "D) 15", "C"),
         ("What sea did Moses part?", "A) Dead Sea", "B) Red Sea", "C) Blue Sea", "D) Lake", "B"),
         ("Who killed Goliath?", "A) Saul", "B) Samuel", "C) David", "D) Jonathan", "C"),
         ("What did Jesus turn water into?", "A) Juice", "B) Milk", "C) Wine", "D) Oil", "C"),
         ("How many books are in the Bible?", "A) 55", "B) 66", "C) 72", "D) 80", "B")],
        [("Who was thrown in the lions' den?", "A) David", "B) Jonah", "C) Daniel", "D) Moses", "C"),
         ("What fish swallowed Jonah?", "A) Shark", "B) Dolphin", "C) Whale", "D) Great fish", "D"),
         ("Who was Jesus' mother?", "A) Martha", "B) Mary", "C) Ruth", "D) Sarah", "B"),
         ("Where was Jesus born?", "A) Nazareth", "B) Jerusalem", "C) Bethlehem", "D) Egypt", "C"),
         ("What did Jesus ride into Jerusalem?", "A) Horse", "B) Camel", "C) Chariot", "D) Donkey", "D")],
        [("Who betrayed Jesus?", "A) Peter", "B) John", "C) Judas", "D) Thomas", "C"),
         ("How many plagues were in Egypt?", "A) 5", "B) 7", "C) 10", "D) 12", "C"),
         ("What is the first book of the Bible?", "A) Exodus", "B) Matthew", "C) Psalms", "D) Genesis", "D"),
         ("Who wrote most of the Psalms?", "A) Moses", "B) Solomon", "C) David", "D) Paul", "C"),
         ("What is the last book of the Bible?", "A) Jude", "B) Revelation", "C) Malachi", "D) Acts", "B")],
        [("What did Samson lose when his hair was cut?", "A) Memory", "B) Strength", "C) Sight", "D) Voice", "B"),
         ("Who was the wisest king?", "A) David", "B) Solomon", "C) Saul", "D) Hezekiah", "B"),
         ("How long did Jesus fast in the desert?", "A) 7 days", "B) 20 days", "C) 40 days", "D) 100 days", "C"),
         ("What apostle was a tent-maker?", "A) Peter", "B) John", "C) Paul", "D) James", "C"),
         ("Who climbed a tree to see Jesus?", "A) Peter", "B) Zacchaeus", "C) Nicodemus", "D) Matthew", "B")],
        [("What garden did Jesus pray in?", "A) Eden", "B) Gethsemane", "C) Babylon", "D) Bethany", "B"),
         ("How many fruits of the Spirit are there?", "A) 7", "B) 9", "C) 10", "D) 12", "B"),
         ("Who was Abraham's wife?", "A) Rachel", "B) Rebecca", "C) Sarah", "D) Leah", "C"),
         ("What did Jesus feed 5000 people with?", "A) Bread only", "B) Fish only", "C) Bread & fish", "D) Manna", "C"),
         ("Who was the first king of Israel?", "A) David", "B) Solomon", "C) Saul", "D) Samuel", "C")],
        [("What did Moses receive on Mt. Sinai?", "A) Food", "B) 10 Commandments", "C) A crown", "D) Gold", "B"),
         ("What weapon did David use against Goliath?", "A) Sword", "B) Spear", "C) Sling", "D) Bow", "C"),
         ("Where did Jesus grow up?", "A) Bethlehem", "B) Jerusalem", "C) Nazareth", "D) Egypt", "C"),
         ("How old was Jesus when he started ministry?", "A) 20", "B) 25", "C) 30", "D) 33", "C"),
         ("What type of wood was Noah's ark made of?", "A) Oak", "B) Cedar", "C) Gopher/Cypress", "D) Pine", "C")],
        [("Who denied Jesus 3 times?", "A) Judas", "B) Thomas", "C) Peter", "D) John", "C"),
         ("What river was Jesus baptized in?", "A) Nile", "B) Jordan", "C) Euphrates", "D) Red Sea", "B"),
         ("How many days was Lazarus dead before Jesus raised him?", "A) 1", "B) 2", "C) 3", "D) 4", "D"),
         ("Who was the first woman?", "A) Sarah", "B) Eve", "C) Mary", "D) Ruth", "B"),
         ("What did God make Eve from?", "A) Dust", "B) Water", "C) Adam's rib", "D) Clay", "C")],
        [("What did the burning bush tell Moses?", "A) Run away", "B) Build an ark", "C) Free my people", "D) Go to sleep", "C"),
         ("Who was Joseph's father?", "A) Abraham", "B) Isaac", "C) Jacob", "D) David", "C"),
         ("How many brothers did Joseph have?", "A) 7", "B) 9", "C) 11", "D) 13", "C"),
         ("What color was Joseph's coat?", "A) Red", "B) Blue", "C) Many colors", "D) White", "C"),
         ("Who was the strongest man in the Bible?", "A) David", "B) Goliath", "C) Samson", "D) Joshua", "C")],
        [("What's the shortest verse in the Bible?", "A) God is love", "B) Jesus wept", "C) Pray always", "D) Be still", "B"),
         ("How many commandments did God give Moses?", "A) 5", "B) 7", "C) 10", "D) 12", "C"),
         ("What miracle did Jesus do first?", "A) Walking on water", "B) Water to wine", "C) Feeding 5000", "D) Healing blind", "B"),
         ("Where did Adam and Eve live?", "A) Babylon", "B) Egypt", "C) Garden of Eden", "D) Canaan", "C"),
         ("What animal talked to Balaam?", "A) Snake", "B) Donkey", "C) Parrot", "D) Dog", "B")],
    ]

    for trivia_num, questions in enumerate(trivia_pages):
        pdf.new_page()
        pdf.add_centered_text(750, f"BIBLE TRIVIA #{trivia_num+1}", 'F2', 16)
        pdf.add_centered_text(730, "Circle the correct answer!", 'F1', 10, 0.4)
        pdf.add_line(72, 720, 540, 720, 1, 0.5)

        y = 695
        for q_num, (question, a, b, c, d, answer) in enumerate(questions):
            pdf.add_text(72, y, f"{q_num+1}. {question}", 'F2', 11)
            y -= 18
            pdf.add_text(100, y, a, 'F1', 10)
            pdf.add_text(250, y, b, 'F1', 10)
            y -= 16
            pdf.add_text(100, y, c, 'F1', 10)
            pdf.add_text(250, y, d, 'F1', 10)
            y -= 25

    # ===== ANSWER KEY (5 pages) =====
    # Word Search Answers
    pdf.new_page()
    pdf.add_centered_text(750, "ANSWER KEY - WORD SEARCHES", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    y = 710
    for ws_num, (theme, words) in enumerate(word_search_themes):
        pdf.add_text(72, y, f"#{ws_num+1} {theme}: {', '.join(words)}", 'F1', 8)
        y -= 14

    # Maze Answers
    pdf.new_page()
    pdf.add_centered_text(750, "ANSWER KEY - MAZES", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    y = 710
    for maze_num, (title, start, end) in enumerate(maze_themes):
        pdf.add_text(72, y, f"Maze #{maze_num+1}: {title}", 'F1', 10)
        y -= 14
        pdf.add_text(92, y, f"Follow the path from {start} to {end}!", 'F1', 9, 0.4)
        y -= 18

    # Trivia Answers (3 pages)
    pdf.new_page()
    pdf.add_centered_text(750, "ANSWER KEY - TRIVIA (Pages 1-5)", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    y = 710
    for trivia_num, questions in enumerate(trivia_pages[:5]):
        pdf.add_text(72, y, f"Trivia #{trivia_num+1}:", 'F2', 10)
        answers_str = ", ".join([f"{i+1}){ans}" for i, (_, _, _, _, _, ans) in enumerate(questions)])
        pdf.add_text(160, y, answers_str, 'F1', 9)
        y -= 18

    pdf.new_page()
    pdf.add_centered_text(750, "ANSWER KEY - TRIVIA (Pages 6-10)", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    y = 710
    for trivia_num, questions in enumerate(trivia_pages[5:]):
        pdf.add_text(72, y, f"Trivia #{trivia_num+6}:", 'F2', 10)
        answers_str = ", ".join([f"{i+1}){ans}" for i, (_, _, _, _, _, ans) in enumerate(questions)])
        pdf.add_text(160, y, answers_str, 'F1', 9)
        y -= 18

    # Final answer page with fun message
    pdf.new_page()
    pdf.add_centered_text(750, "GREAT JOB!", 'F2', 24)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_centered_text(700, "You completed ALL 30 puzzles!", 'F1', 14)
    pdf.add_centered_text(670, "You are a BIBLE PUZZLE CHAMPION!", 'F2', 16)
    pdf.add_centered_text(620, "Keep reading God's Word and having fun!", 'F1', 12)
    pdf.add_centered_text(580, "Here are some more ways to learn the Bible:", 'F1', 11)
    tips = [
        "1. Read one chapter a day",
        "2. Memorize one verse a week",
        "3. Join a Bible study group at church",
        "4. Make your own Bible puzzles for friends!",
        "5. Draw pictures of your favorite Bible stories",
    ]
    y = 550
    for tip in tips:
        pdf.add_text(150, y, tip, 'F1', 11)
        y -= 22

    pdf.add_centered_text(400, "God loves you!", 'F5', 18)
    pdf.add_centered_text(365, "'Your word is a lamp to my feet", 'F4', 12)
    pdf.add_centered_text(345, "and a light for my path.' - Psalm 119:105", 'F4', 12)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book215_Bible_Puzzle_Book_Kids.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
