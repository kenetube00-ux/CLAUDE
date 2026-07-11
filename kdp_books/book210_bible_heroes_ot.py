"""Book 210: BIBLE HEROES - Old Testament Activity Book for Kids Ages 6-10 (KIDLYTICAL)"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.94)
    pdf.add_centered_text(620, "BIBLE HEROES", 'F2', 30)
    pdf.add_centered_text(580, "Old Testament Activity Book", 'F4', 16, 0.2)
    pdf.add_centered_text(553, "for Kids Ages 6-10", 'F1', 14, 0.3)
    pdf.add_centered_text(500, "Word Searches + Coloring + Mazes + Fun!", 'F1', 12, 0.3)
    pdf.add_centered_text(470, "KIDLYTICAL", 'F2', 14, 0.4)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "BIBLE HEROES - Old Testament Activity Book", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "Scripture from World English Bible (WEB)", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)
    pdf.add_text(72, 590, "For ages 6-10", 'F1', 9)

    characters = [
        ("NOAH", "God told Noah to build an ark because a flood was coming. Noah obeyed God even though people laughed. He saved his family and the animals. God made a rainbow promise.",
         "Genesis 6:22 - Noah did everything just as God commanded him.",
         ["NOAH", "ARK", "FLOOD", "RAINBOW", "OBEY", "ANIMALS", "RAIN", "DOVE"],
         "Draw Noah's big ark with animals going in two by two!"),
        ("ABRAHAM", "God called Abraham to leave his home and go to a new land. Abraham trusted God even when it was scary. God promised to make him the father of many nations.",
         "Genesis 15:6 - Abraham believed the LORD and it was credited as righteousness.",
         ["ABRAHAM", "FAITH", "STARS", "PROMISE", "JOURNEY", "TRUST", "ISAAC", "TENT"],
         "Draw Abraham looking up at a sky full of stars!"),
        ("JOSEPH", "Joseph's brothers sold him as a slave because they were jealous. But God was with Joseph in Egypt. He went from prison to the palace! He forgave his brothers.",
         "Genesis 50:20 - You meant evil against me, but God meant it for good.",
         ["JOSEPH", "COAT", "DREAM", "EGYPT", "PRISON", "FORGIVE", "PALACE", "GRAIN"],
         "Draw Joseph's colorful coat with many colors!"),
        ("MOSES", "Baby Moses was saved from the river by a princess. He grew up to lead God's people out of Egypt. God split the Red Sea so they could cross safely!",
         "Exodus 14:21 - The LORD drove the sea back with a strong east wind.",
         ["MOSES", "BASKET", "PHARAOH", "PLAGUES", "SEA", "FREE", "STAFF", "BUSH"],
         "Draw the Red Sea parting with Moses holding up his staff!"),
        ("JOSHUA", "After Moses died, Joshua led the people into the Promised Land. He marched around Jericho and the walls fell down! God gave them the victory.",
         "Joshua 1:9 - Be strong and courageous for the LORD your God is with you.",
         ["JOSHUA", "WALLS", "JERICHO", "MARCH", "BRAVE", "TRUMPET", "LAND", "STRONG"],
         "Draw the walls of Jericho falling down!"),
        ("GIDEON", "Gideon was afraid, but God chose him to save Israel. With only 300 men, torches, and trumpets, God gave him victory over a huge army!",
         "Judges 7:7 - With the 300 men I will save you.",
         ["GIDEON", "TORCH", "TRUMPET", "BRAVE", "THREE", "ARMY", "NIGHT", "JARS"],
         "Draw Gideon's soldiers holding torches and trumpets at night!"),
        ("RUTH", "Ruth was loyal to her mother-in-law Naomi. She left her own country to follow God. Ruth worked hard and God blessed her with a new family and a husband named Boaz.",
         "Ruth 1:16 - Where you go I will go, and where you stay I will stay.",
         ["RUTH", "NAOMI", "LOYAL", "BOAZ", "GRAIN", "FIELD", "KIND", "LOVE"],
         "Draw Ruth gathering grain in the fields!"),
        ("DAVID", "David was just a shepherd boy, but God chose him to be king. He defeated the giant Goliath with just a stone and a sling because he trusted God!",
         "1 Samuel 17:47 - The battle is the LORD's.",
         ["DAVID", "GIANT", "STONE", "SLING", "HARP", "SHEEP", "KING", "BRAVE"],
         "Draw young David facing the giant Goliath!"),
        ("ELIJAH", "Elijah was a brave prophet who stood up for God. He challenged 450 false prophets and God sent fire from heaven! God took care of Elijah with ravens bringing food.",
         "1 Kings 18:39 - The LORD, he is God!",
         ["ELIJAH", "FIRE", "PROPHET", "RAVENS", "ALTAR", "RAIN", "HEAVEN", "BOLD"],
         "Draw fire coming down from heaven onto Elijah's altar!"),
        ("DANIEL", "Daniel prayed to God three times every day. When bad men threw him to the lions, God sent an angel to keep him safe! Daniel was never afraid because God was with him.",
         "Daniel 6:22 - My God sent his angel and shut the lions' mouths.",
         ["DANIEL", "LIONS", "PRAYER", "ANGEL", "FAITH", "DEN", "KING", "SAFE"],
         "Draw Daniel praying peacefully with the lions around him!"),
        ("ESTHER", "Esther was a brave queen who saved her people. Even though she was scared, she went to the king and asked him to protect the Jewish people. God used her courage!",
         "Esther 4:14 - Perhaps you were made queen for such a time as this.",
         ["ESTHER", "QUEEN", "BRAVE", "CROWN", "KING", "SAVE", "FAST", "PRAY"],
         "Draw Queen Esther wearing her crown and being brave!"),
        ("JONAH", "God told Jonah to go to Nineveh but Jonah ran away! A big fish swallowed him for three days. Inside the fish, Jonah prayed and God saved him. Then Jonah obeyed.",
         "Jonah 2:1 - Jonah prayed to the LORD from inside the fish.",
         ["JONAH", "FISH", "STORM", "BOAT", "PRAY", "OBEY", "CITY", "WHALE"],
         "Draw Jonah inside the belly of the big fish!"),
    ]

    for char_num, (name, story, verse, words, color_prompt) in enumerate(characters):
        # Page 1: Story + Verse
        pdf.new_page()
        pdf.add_filled_rect(60, 720, 492, 45, 0.85)
        pdf.add_centered_text(738, f"{name}", 'F2', 20)
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
        pdf.add_text(72, y, f"What did {name.title()} teach you about trusting God?", 'F1', 10)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Coloring prompt
        y -= 30
        pdf.add_text(72, y, "COLOR THIS:", 'F2', 13)
        y -= 5
        pdf.add_rect(72, y - 180, 468, 180, 1, 0.6)
        pdf.add_centered_text(y - 85, color_prompt, 'F1', 11, 0.5)

        # Page 2: Word Search + Maze
        pdf.new_page()
        pdf.add_centered_text(750, f"WORD SEARCH: {name}", 'F2', 16)
        pdf.add_text(72, 725, "Find these words:", 'F1', 10)
        word_str = "  ".join(words)
        pdf.add_text(72, 708, word_str, 'F2', 9)

        # Create word search grid
        grid_size = 10
        random.seed(char_num * 37 + 7)
        grid = [[chr(random.randint(65, 90)) for _ in range(grid_size)] for _ in range(grid_size)]
        # Place some words
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

        # Maze placeholder
        y -= 20
        pdf.add_text(72, y, f"MAZE: Help {name.title()} complete the journey!", 'F2', 12)
        y -= 5
        pdf.add_rect(72, y - 160, 468, 160, 1, 0.5)
        # Simple maze visualization
        random.seed(char_num * 19)
        for _ in range(12):
            mx = random.randint(80, 500)
            my = random.randint(int(y - 155), int(y - 10))
            mw = random.randint(20, 80)
            pdf.add_line(mx, my, mx + mw, my, 2, 0.3)
        pdf.add_text(82, y - 15, "START", 'F2', 9)
        pdf.add_text(490, y - 150, "END", 'F2', 9)

    # Answer Key (2 pages)
    pdf.new_page()
    pdf.add_centered_text(750, "ANSWER KEY - PAGE 1", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    y = 710
    for i, (name, _, _, words, _) in enumerate(characters[:6]):
        pdf.add_text(72, y, f"{name}: {', '.join(words)}", 'F1', 9)
        y -= 18

    pdf.new_page()
    pdf.add_centered_text(750, "ANSWER KEY - PAGE 2", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    y = 710
    for i, (name, _, _, words, _) in enumerate(characters[6:]):
        pdf.add_text(72, y, f"{name}: {', '.join(words)}", 'F1', 9)
        y -= 18

    # Bible Timeline
    pdf.new_page()
    pdf.add_centered_text(750, "OLD TESTAMENT TIMELINE", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    timeline = [
        "1. NOAH - The Flood",
        "2. ABRAHAM - Father of Faith",
        "3. JOSEPH - Sold into Egypt",
        "4. MOSES - Exodus from Egypt",
        "5. JOSHUA - Entering Promised Land",
        "6. GIDEON - Judges Period",
        "7. RUTH - Time of Judges",
        "8. DAVID - King of Israel",
        "9. ELIJAH - Prophet in Israel",
        "10. DANIEL - Exile in Babylon",
        "11. ESTHER - Exile in Persia",
        "12. JONAH - Prophet to Nineveh",
    ]
    y = 710
    for item in timeline:
        pdf.add_text(72, y, item, 'F1', 11)
        pdf.add_line(72, y - 10, 540, y - 10, 0.3, 0.8)
        y -= 30

    # Certificate
    pdf.new_page()
    pdf.add_filled_rect(50, 250, 512, 350, 0.92)
    pdf.add_rect(55, 255, 502, 340, 2, 0.3)
    pdf.add_centered_text(560, "CERTIFICATE OF COMPLETION", 'F2', 22)
    pdf.add_centered_text(520, "This certifies that", 'F1', 12)
    pdf.add_line(180, 495, 432, 495, 1, 0.4)
    pdf.add_centered_text(478, "(write your name)", 'F1', 9, 0.5)
    pdf.add_centered_text(445, "has learned about ALL 12 Old Testament Heroes!", 'F1', 12)
    pdf.add_centered_text(415, "You are a BIBLE HERO EXPLORER!", 'F2', 14)
    pdf.add_centered_text(380, "Date: _______________", 'F1', 10)
    pdf.add_centered_text(310, "Great job! Keep reading God's Word!", 'F5', 12, 0.3)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book210_Bible_Heroes_OT.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
