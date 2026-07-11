"""Book 211: BIBLE HEROES - New Testament Activity Book for Kids Ages 6-10 (KIDLYTICAL)"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.94)
    pdf.add_centered_text(620, "BIBLE HEROES", 'F2', 30)
    pdf.add_centered_text(580, "New Testament Activity Book", 'F4', 16, 0.2)
    pdf.add_centered_text(553, "for Kids Ages 6-10", 'F1', 14, 0.3)
    pdf.add_centered_text(500, "Word Searches + Coloring + Mazes + Fun!", 'F1', 12, 0.3)
    pdf.add_centered_text(470, "KIDLYTICAL", 'F2', 14, 0.4)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "BIBLE HEROES - New Testament Activity Book", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "Scripture from World English Bible (WEB)", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)

    characters = [
        ("JESUS (Good Shepherd)", "Jesus is the Son of God who came to save the world. He healed the sick, loved children, and taught about God's kingdom. He is our Good Shepherd who takes care of us!",
         "John 10:11 - I am the good shepherd. The good shepherd lays down his life for the sheep.",
         ["JESUS", "SHEPHERD", "LOVE", "HEAL", "TEACH", "SAVE", "LAMB", "GOOD"],
         "Draw Jesus as the Good Shepherd carrying a little lamb!"),
        ("PETER", "Peter was a fisherman who became Jesus' closest friend. He was bold but sometimes made mistakes. After Jesus rose, Peter became the leader of the early church!",
         "Matthew 16:18 - On this rock I will build my church.",
         ["PETER", "FISH", "ROCK", "BOLD", "WALK", "WATER", "CHURCH", "PREACH"],
         "Draw Peter stepping out of the boat to walk on water!"),
        ("JOHN", "John was called the disciple Jesus loved. He stayed with Jesus at the cross. He wrote about God's love so we could know how much God loves us!",
         "1 John 4:8 - God is love.",
         ["JOHN", "LOVE", "WRITE", "CROSS", "FRIEND", "TRUTH", "BOOK", "LIGHT"],
         "Draw John writing about God's love on a scroll!"),
        ("MARY (Mother of Jesus)", "Mary was a young woman who said YES to God's plan. She was brave and faithful. She became the mother of Jesus and cared for him his whole life.",
         "Luke 1:38 - I am the Lord's servant. May it be to me as you have said.",
         ["MARY", "ANGEL", "BABY", "FAITH", "MOTHER", "SING", "BRAVE", "YES"],
         "Draw Mary holding baby Jesus with a bright star above!"),
        ("MARY MAGDALENE", "Mary Magdalene followed Jesus faithfully. She was the first person to see Jesus alive after He rose from the dead! She ran to tell the others the good news!",
         "John 20:18 - I have seen the Lord!",
         ["MARY", "TOMB", "RISEN", "FIRST", "TELL", "JOY", "GARDEN", "ALIVE"],
         "Draw Mary Magdalene at the empty tomb on Easter morning!"),
        ("MATTHEW", "Matthew was a tax collector nobody liked. Then Jesus said 'Follow me!' and Matthew left everything to follow Jesus. He wrote one of the four Gospels!",
         "Matthew 9:9 - Follow me. And he rose and followed him.",
         ["MATTHEW", "FOLLOW", "TAX", "WRITE", "GOSPEL", "CHANGE", "CALL", "NEW"],
         "Draw Matthew leaving his table to follow Jesus!"),
        ("PAUL", "Paul used to hurt Christians until Jesus appeared to him in a bright light! Then Paul became the greatest missionary ever, traveling everywhere to tell people about Jesus!",
         "Acts 9:15 - He is a chosen instrument of mine to carry my name.",
         ["PAUL", "LIGHT", "TRAVEL", "LETTER", "SHIP", "PREACH", "CHANGE", "BOLD"],
         "Draw Paul traveling on a ship to tell people about Jesus!"),
        ("BARNABAS", "Barnabas means 'Son of Encouragement.' He always helped and encouraged other Christians. He believed in Paul when nobody else did and helped him get started!",
         "Acts 4:36 - Barnabas, which means Son of Encouragement.",
         ["BARNABAS", "KIND", "HELP", "FRIEND", "SHARE", "TRUST", "TRAVEL", "GOOD"],
         "Draw Barnabas putting his arm around someone to encourage them!"),
        ("TIMOTHY", "Timothy was a young man who loved God. Paul became his mentor and teacher. Even though he was young, Timothy led a whole church! You're never too young for God!",
         "1 Timothy 4:12 - Don't let anyone look down on you because you are young.",
         ["TIMOTHY", "YOUNG", "BRAVE", "LEARN", "LEAD", "TEACH", "FAITH", "GROW"],
         "Draw young Timothy reading a scroll and learning God's word!"),
        ("STEPHEN", "Stephen was full of faith and courage. He told everyone about Jesus even when it was dangerous. He was the first person to die for believing in Jesus (a martyr).",
         "Acts 7:59 - Lord Jesus, receive my spirit.",
         ["STEPHEN", "BRAVE", "FAITH", "PRAY", "SPIRIT", "FIRST", "STAND", "BOLD"],
         "Draw Stephen looking up to heaven with a brave face!"),
        ("LYDIA", "Lydia was a businesswoman who sold purple cloth. When she heard about Jesus, she believed right away! She opened her home for the church to meet in.",
         "Acts 16:14 - The Lord opened her heart to respond to Paul's message.",
         ["LYDIA", "PURPLE", "HEART", "HOME", "OPEN", "CLOTH", "RIVER", "GIVE"],
         "Draw Lydia's house with people gathering for church inside!"),
        ("THE GOOD SAMARITAN", "A man was hurt on the road. Important people walked past without helping. But a Samaritan stopped, bandaged his wounds, and took care of him. Be a neighbor!",
         "Luke 10:37 - Go and do likewise.",
         ["HELP", "KIND", "LOVE", "ROAD", "CARE", "HEAL", "GIVE", "NEIGHBOR"],
         "Draw the Good Samaritan helping the hurt man on the road!"),
    ]

    for char_num, (name, story, verse, words, color_prompt) in enumerate(characters):
        # Page 1: Story + Verse + Learning
        pdf.new_page()
        pdf.add_filled_rect(60, 720, 492, 45, 0.85)
        pdf.add_centered_text(738, name.upper(), 'F2', 18)
        pdf.add_line(72, 710, 540, 710, 1, 0.6)

        pdf.add_text(72, 685, "THE STORY:", 'F2', 12)
        words_list = story.split()
        line = ""
        y = 665
        for w in words_list:
            if len(line + " " + w) > 72:
                pdf.add_text(72, y, line, 'F1', 11)
                y -= 16
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(72, y, line, 'F1', 11)
            y -= 16

        y -= 15
        pdf.add_text(72, y, "KEY VERSE:", 'F2', 12)
        y -= 18
        pdf.add_text(82, y, verse, 'F4', 10)

        y -= 30
        pdf.add_text(72, y, "WHAT DID YOU LEARN?", 'F2', 12)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Coloring
        y -= 25
        pdf.add_text(72, y, "COLOR THIS:", 'F2', 13)
        y -= 5
        pdf.add_rect(72, y - 170, 468, 170, 1, 0.6)
        pdf.add_centered_text(y - 80, color_prompt, 'F1', 11, 0.5)

        # Page 2: Word Search + Activity
        pdf.new_page()
        pdf.add_centered_text(750, f"WORD SEARCH: {name.upper()}", 'F2', 14)
        pdf.add_text(72, 725, "Find these words:", 'F1', 10)
        word_str = "  ".join(words)
        pdf.add_text(72, 708, word_str, 'F2', 9)

        grid_size = 10
        random.seed(char_num * 43 + 11)
        grid = [[chr(random.randint(65, 90)) for _ in range(grid_size)] for _ in range(grid_size)]
        for wi, word in enumerate(words[:4]):
            if wi < grid_size and len(word) <= grid_size:
                for ci, ch in enumerate(word):
                    if ci < grid_size:
                        grid[wi][ci] = ch

        y = 680
        for row in grid:
            row_text = "  ".join(row)
            pdf.add_text(130, y, row_text, 'F3', 12)
            y -= 20

        # Activity/Maze
        y -= 20
        pdf.add_text(72, y, f"MAZE: Help find the way!", 'F2', 12)
        y -= 5
        pdf.add_rect(72, y - 150, 468, 150, 1, 0.5)
        random.seed(char_num * 23)
        for _ in range(10):
            mx = random.randint(80, 500)
            my = random.randint(int(y - 145), int(y - 10))
            mw = random.randint(20, 80)
            pdf.add_line(mx, my, mx + mw, my, 2, 0.3)
        pdf.add_text(82, y - 15, "START", 'F2', 9)
        pdf.add_text(490, y - 140, "END", 'F2', 9)

    # Answer Key
    pdf.new_page()
    pdf.add_centered_text(750, "ANSWER KEY", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    y = 710
    for name, _, _, words, _ in characters:
        pdf.add_text(72, y, f"{name}: {', '.join(words)}", 'F1', 8)
        y -= 14

    # Certificate
    pdf.new_page()
    pdf.add_filled_rect(50, 250, 512, 350, 0.92)
    pdf.add_rect(55, 255, 502, 340, 2, 0.3)
    pdf.add_centered_text(560, "CERTIFICATE OF COMPLETION", 'F2', 22)
    pdf.add_centered_text(520, "This certifies that", 'F1', 12)
    pdf.add_line(180, 495, 432, 495, 1, 0.4)
    pdf.add_centered_text(478, "(write your name)", 'F1', 9, 0.5)
    pdf.add_centered_text(445, "has learned about ALL 12 New Testament Heroes!", 'F1', 12)
    pdf.add_centered_text(415, "You are a NEW TESTAMENT EXPLORER!", 'F2', 14)
    pdf.add_centered_text(380, "Date: _______________", 'F1', 10)
    pdf.add_centered_text(310, "Amazing! Keep following Jesus!", 'F5', 12, 0.3)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book211_Bible_Heroes_NT.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
