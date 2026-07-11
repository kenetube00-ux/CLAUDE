"""Book 212: BRAVE WOMEN OF THE BIBLE - Activity Book for Girls Ages 6-10 (KIDLYTICAL)"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.93)
    pdf.add_centered_text(620, "BRAVE WOMEN", 'F2', 30)
    pdf.add_centered_text(580, "OF THE BIBLE", 'F2', 30)
    pdf.add_centered_text(540, "Activity Book for Girls Ages 6-10", 'F4', 14, 0.2)
    pdf.add_centered_text(500, "10 Amazing Women Who Trusted God", 'F1', 12, 0.3)
    pdf.add_centered_text(470, "KIDLYTICAL", 'F2', 14, 0.4)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "BRAVE WOMEN OF THE BIBLE", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "Scripture from World English Bible (WEB)", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)

    women = [
        ("SARAH", "Sarah waited a very long time for God's promise. She was old when God finally gave her a baby named Isaac! She laughed with joy. God always keeps His promises, even when we have to wait.",
         "She was brave because she trusted God's promise even when it seemed impossible.",
         "Genesis 21:6 - God has brought me laughter.",
         ["SARAH", "PROMISE", "LAUGH", "ISAAC", "WAIT", "TRUST", "BABY", "JOY"],
         "Draw yourself being brave by waiting patiently for something!"),
        ("MIRIAM", "Miriam watched over her baby brother Moses in the river to keep him safe. Later, she led all the women in dancing and singing when God saved them from Egypt! She was a leader and a worshiper.",
         "She was brave because she protected her brother and led worship.",
         "Exodus 15:20 - Miriam took a tambourine and all the women followed her.",
         ["MIRIAM", "DANCE", "SING", "RIVER", "WATCH", "LEAD", "MUSIC", "BRAVE"],
         "Draw yourself being brave by singing and dancing for God!"),
        ("DEBORAH", "Deborah was a judge and leader of all Israel! People came to her for wisdom. She helped lead an army to victory because she trusted God. She was wise and strong.",
         "She was brave because she led when others were afraid.",
         "Judges 4:4 - Deborah, a prophetess, was leading Israel at that time.",
         ["DEBORAH", "JUDGE", "WISE", "LEAD", "STRONG", "ARMY", "PALM", "FAITH"],
         "Draw yourself being brave by helping solve a problem!"),
        ("RUTH", "Ruth chose to stay with Naomi even when life was hard. She left her home country to follow God. She worked hard in the fields and God blessed her with a new family!",
         "She was brave because she chose loyalty and hard work.",
         "Ruth 1:16 - Where you go I will go.",
         ["RUTH", "LOYAL", "WORK", "FIELD", "GRAIN", "KIND", "NAOMI", "LOVE"],
         "Draw yourself being brave by being loyal to a friend!"),
        ("HANNAH", "Hannah prayed and prayed for a baby. She cried out to God and He heard her! When God gave her Samuel, she kept her promise and dedicated him to God. She was faithful.",
         "She was brave because she kept praying and kept her promise.",
         "1 Samuel 1:27 - I prayed for this child and the LORD gave me what I asked.",
         ["HANNAH", "PRAY", "BABY", "SAMUEL", "TEMPLE", "FAITH", "SONG", "GIVE"],
         "Draw yourself being brave by praying about something important!"),
        ("ESTHER", "Esther was a queen who saved her entire people. Even though she could have been killed, she went to the king to ask him to save the Jews. Her courage saved a nation!",
         "She was brave because she risked her life to save others.",
         "Esther 4:14 - Perhaps you were made queen for such a time as this.",
         ["ESTHER", "QUEEN", "BRAVE", "CROWN", "SAVE", "FAST", "SPEAK", "TIME"],
         "Draw yourself being brave by speaking up for someone!"),
        ("MARY (Mother of Jesus)", "When an angel told Mary she would be the mother of Jesus, she said YES to God! She was young and scared, but she trusted God's plan. She raised the Savior of the world!",
         "She was brave because she said yes to God's big plan.",
         "Luke 1:38 - I am the Lord's servant.",
         ["MARY", "ANGEL", "YES", "MOTHER", "BABY", "FAITH", "SING", "TRUST"],
         "Draw yourself being brave by saying YES to something hard!"),
        ("MARTHA & MARY", "Martha worked hard to serve Jesus in her home. Mary sat and listened to Jesus teach. Jesus said both serving AND listening are important. They both loved Jesus in different ways!",
         "They were brave because they welcomed Jesus and loved Him their own way.",
         "Luke 10:42 - Mary has chosen what is better.",
         ["MARTHA", "MARY", "SERVE", "LISTEN", "JESUS", "HOME", "COOK", "LEARN"],
         "Draw yourself being brave by serving or listening to learn!"),
        ("PRISCILLA", "Priscilla and her husband taught others about Jesus. She was a teacher and leader in the early church! She helped Apollos understand the Bible better. She used her gifts for God!",
         "She was brave because she taught others about God.",
         "Acts 18:26 - They explained to him the way of God more accurately.",
         ["PRISCILLA", "TEACH", "CHURCH", "TENT", "SHARE", "WISE", "HELP", "BOLD"],
         "Draw yourself being brave by teaching someone something you know!"),
        ("LYDIA", "Lydia was a successful businesswoman who sold purple cloth. When she heard about Jesus, she believed right away! She opened her home for the whole church to meet in. She was generous!",
         "She was brave because she opened her heart and her home.",
         "Acts 16:14 - The Lord opened her heart to respond to Paul's message.",
         ["LYDIA", "PURPLE", "HEART", "HOME", "OPEN", "GIVE", "RIVER", "CHURCH"],
         "Draw yourself being brave by sharing what you have!"),
    ]

    for char_num, (name, story, brave_because, verse, words, draw_prompt) in enumerate(women):
        # Page 1: Story
        pdf.new_page()
        pdf.add_filled_rect(60, 720, 492, 45, 0.85)
        pdf.add_centered_text(738, name, 'F2', 18)
        pdf.add_line(72, 710, 540, 710, 1, 0.6)

        pdf.add_text(72, 685, "HER STORY:", 'F2', 12)
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
        pdf.add_text(72, y, brave_because, 'F5', 11)

        y -= 25
        pdf.add_text(72, y, "KEY VERSE:", 'F2', 11)
        y -= 16
        pdf.add_text(82, y, verse, 'F4', 10)

        y -= 30
        pdf.add_text(72, y, "HOW CAN I BE BRAVE LIKE HER?", 'F2', 12)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Drawing prompt
        y -= 25
        pdf.add_text(72, y, "DRAW YOURSELF BEING BRAVE:", 'F2', 12)
        y -= 3
        pdf.add_text(72, y - 5, draw_prompt, 'F1', 10, 0.4)
        pdf.add_rect(72, y - 175, 468, 165, 1, 0.6)

        # Page 2: Word Search + Activity
        pdf.new_page()
        pdf.add_centered_text(750, f"WORD SEARCH: {name}", 'F2', 14)
        pdf.add_text(72, 725, "Find these words:", 'F1', 10)
        word_str = "  ".join(words)
        pdf.add_text(72, 708, word_str, 'F2', 9)

        grid_size = 10
        random.seed(char_num * 53 + 13)
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

        # Activity page
        y -= 20
        pdf.add_text(72, y, "ACTIVITY:", 'F2', 12)
        y -= 18
        pdf.add_text(72, y, f"Write a prayer asking God to make you brave like {name.title()}:", 'F1', 10)
        for _ in range(4):
            y -= 18
            pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Answer Key
    pdf.new_page()
    pdf.add_centered_text(750, "ANSWER KEY", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    y = 710
    for name, _, _, _, words, _ in women:
        pdf.add_text(72, y, f"{name}: {', '.join(words)}", 'F1', 8)
        y -= 14

    # "I Am Brave" Certificate
    pdf.new_page()
    pdf.add_filled_rect(50, 250, 512, 350, 0.92)
    pdf.add_rect(55, 255, 502, 340, 2, 0.3)
    pdf.add_centered_text(560, "I AM BRAVE CERTIFICATE", 'F2', 22)
    pdf.add_centered_text(520, "This certifies that", 'F1', 12)
    pdf.add_line(180, 495, 432, 495, 1, 0.4)
    pdf.add_centered_text(478, "(write your name)", 'F1', 9, 0.5)
    pdf.add_centered_text(445, "is a BRAVE girl of God!", 'F1', 14)
    pdf.add_centered_text(415, "She has learned from 10 Brave Women of the Bible!", 'F1', 11)
    pdf.add_centered_text(385, "She is strong, courageous, and loved!", 'F2', 12)
    pdf.add_centered_text(350, "Date: _______________", 'F1', 10)
    pdf.add_centered_text(310, "'Be strong and courageous!' - Joshua 1:9", 'F5', 11, 0.3)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book212_Women_Of_Bible_Kids.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
