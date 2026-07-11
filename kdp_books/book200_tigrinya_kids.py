"""Book 200: BIBLE STORIES FOR KIDS - Bilingual Activity Book (Tigrinya-English)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.94)
    pdf.add_centered_text(600, "BIBLE STORIES FOR KIDS", 'F2', 26)
    pdf.add_centered_text(565, "Bilingual Activity Book", 'F4', 16, 0.2)
    pdf.add_centered_text(540, "(Tigrinya-English)", 'F1', 13, 0.3)
    pdf.add_centered_text(480, "10 Favorite Stories with Activities!", 'F1', 12, 0.3)
    pdf.add_centered_text(450, "Coloring + Word Search + Memory Verses", 'F1', 11, 0.4)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright page
    pdf.new_page()
    pdf.add_text(72, 700, "BIBLE STORIES FOR KIDS - Bilingual Activity Book", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "Scripture from World English Bible (WEB)", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)
    pdf.add_text(72, 590, "For ages 5-10", 'F1', 9)

    stories = [
        ("Noah's Ark", "Noh Merhav",
         "God told Noah to build a big ark because a flood was coming. Noah obeyed God and brought two of every animal. It rained for 40 days, but Noah's family was safe. God put a rainbow in the sky as a promise.",
         "Genesis 6:22 - Noah did everything just as God commanded him.",
         ["NOAH", "ARK", "FLOOD", "ANIMAL", "RAINBOW", "OBEY"]),
        ("David and Goliath", "Dawit Hagolyat",
         "A giant named Goliath scared everyone, but young David trusted God. David took five smooth stones and a sling. With one stone, David defeated the giant. God gave David the victory because he trusted.",
         "1 Samuel 17:47 - The battle is the LORD's.",
         ["DAVID", "GOLIATH", "STONE", "SLING", "BRAVE", "GIANT"]),
        ("Daniel in the Lions' Den", "Daniel Abgude Anbesa",
         "Daniel prayed to God three times a day. Bad men tricked the king into throwing Daniel to the lions. God sent an angel to shut the lions' mouths. Daniel was safe because he trusted God.",
         "Daniel 6:22 - My God sent his angel and shut the lions' mouths.",
         ["DANIEL", "LIONS", "PRAYER", "ANGEL", "FAITH", "KING"]),
        ("Jonah and the Fish", "Yonas Asa",
         "God told Jonah to go to Nineveh, but Jonah ran away. A big storm came and Jonah was thrown into the sea. A huge fish swallowed Jonah for three days. Jonah prayed and God saved him.",
         "Jonah 2:1 - Jonah prayed to the LORD his God from inside the fish.",
         ["JONAH", "FISH", "STORM", "PRAY", "NINEVEH", "SEA"]),
        ("Baby Moses", "Hisan Muse",
         "Baby Moses was in danger, so his mother hid him in a basket on the river. Pharaoh's daughter found him and took care of him. God protected baby Moses. Moses grew up to lead God's people.",
         "Exodus 2:10 - She named him Moses, saying I drew him out of the water.",
         ["MOSES", "BASKET", "RIVER", "BABY", "PRINCESS", "SAFE"]),
        ("The Good Samaritan", "Tsbuq Samrawi",
         "A man was hurt on the road. Two people walked past without helping. But a kind Samaritan stopped and helped the hurt man. Jesus told us to love our neighbors like this.",
         "Luke 10:27 - Love your neighbor as yourself.",
         ["HELP", "KIND", "LOVE", "NEIGHBOR", "ROAD", "CARE"]),
        ("Jesus Feeds 5000", "Yesus 5000 Meblie",
         "A huge crowd was hungry but there was only a boy's lunch of five loaves and two fish. Jesus took the food, thanked God, and fed everyone. There were even leftovers! Jesus can do miracles.",
         "John 6:11 - Jesus took the loaves and gave thanks.",
         ["JESUS", "BREAD", "FISH", "MIRACLE", "SHARE", "CROWD"]),
        ("The Lost Sheep", "Ziteghedn Beg",
         "A shepherd had 100 sheep but one got lost. He left the 99 safe sheep to find the one lost sheep. When he found it, he was so happy! Jesus says God looks for us like that shepherd.",
         "Luke 15:6 - Rejoice with me, for I have found my sheep which was lost.",
         ["SHEEP", "LOST", "FOUND", "SHEPHERD", "HAPPY", "LOVE"]),
        ("Creation", "Ftret",
         "In the beginning, God made everything. He made light, sky, land, sun, moon, stars, fish, birds, animals, and people. Everything God made was good. God rested on the seventh day.",
         "Genesis 1:1 - In the beginning God created the heavens and the earth.",
         ["GOD", "LIGHT", "STARS", "ANIMALS", "PEOPLE", "GOOD"]),
        ("Jesus Walks on Water", "Yesus Ab May Kezamere",
         "The disciples were in a boat during a big storm. Jesus came walking on the water! Peter tried to walk on water too. When Peter looked at Jesus instead of the waves, he could walk!",
         "Matthew 14:27 - Take courage! It is I. Do not be afraid.",
         ["JESUS", "WATER", "BOAT", "STORM", "PETER", "FAITH"])
    ]

    import random
    for story_num, (title_en, title_ti, summary, verse, words) in enumerate(stories, 1):
        # Page 1: Story
        pdf.new_page()
        pdf.add_filled_rect(60, 720, 492, 45, 0.85)
        pdf.add_centered_text(738, f"STORY {story_num}: {title_en.upper()}", 'F2', 16)
        pdf.add_centered_text(718, title_ti, 'F5', 12)

        pdf.add_text(72, 690, "The Story:", 'F2', 12)
        # Wrap summary
        words_list = summary.split()
        line = ""
        y = 670
        for w in words_list:
            if len(line + " " + w) > 75:
                pdf.add_text(72, y, line, 'F4', 11)
                y -= 16
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(72, y, line, 'F4', 11)
            y -= 16

        y -= 10
        pdf.add_text(72, y, "Tigrinya:", 'F2', 11)
        y -= 16
        pdf.add_text(72, y, "[Tigrinya story text here]", 'F3', 10, 0.4)

        # Memory verse
        y -= 35
        pdf.add_text(72, y, "Memory Verse:", 'F2', 12)
        y -= 18
        pdf.add_text(82, y, verse, 'F4', 10)
        y -= 16
        pdf.add_text(82, y, "[Tigrinya verse here]", 'F3', 9, 0.4)

        # Coloring prompt
        y -= 35
        pdf.add_text(72, y, "COLOR THIS SCENE:", 'F2', 13)
        y -= 5
        pdf.add_rect(72, y - 200, 468, 200, 1, 0.6)
        pdf.add_centered_text(y - 95, f"Draw and color: {title_en}", 'F1', 11, 0.5)

        # Page 2: Word Search + Questions
        pdf.new_page()
        pdf.add_centered_text(750, f"WORD SEARCH: {title_en.upper()}", 'F2', 14)
        pdf.add_text(72, 725, "Find these words:", 'F1', 10)
        # Show word list
        word_str = "  ".join(words)
        pdf.add_text(72, 708, word_str, 'F2', 10)

        # Create simple word search grid
        grid_size = 8
        random.seed(story_num * 42)
        grid = [[chr(random.randint(65, 90)) for _ in range(grid_size)] for _ in range(grid_size)]
        # Place first word horizontally in row 0
        if len(words[0]) <= grid_size:
            for ci, ch in enumerate(words[0]):
                grid[0][ci] = ch
        if len(words) > 1 and len(words[1]) <= grid_size:
            for ci, ch in enumerate(words[1]):
                grid[2][ci] = ch

        y = 680
        for row in grid:
            row_text = "  ".join(row)
            pdf.add_text(150, y, row_text, 'F3', 12)
            y -= 22

        # What did you learn?
        y -= 20
        pdf.add_text(72, y, "WHAT DID YOU LEARN?", 'F2', 12)
        y -= 20
        pdf.add_text(72, y, "What did this story teach you about God?", 'F1', 10)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

        y -= 30
        pdf.add_text(72, y, "Memory Verse (both languages):", 'F2', 10)
        y -= 18
        pdf.add_text(72, y, "English:", 'F1', 9)
        pdf.add_line(120, y - 2, 540, y - 2, 0.5, 0.7)
        y -= 20
        pdf.add_text(72, y, "Tigrinya:", 'F1', 9)
        pdf.add_line(120, y - 2, 540, y - 2, 0.5, 0.7)

    # Certificate of Completion
    pdf.new_page()
    pdf.add_filled_rect(50, 250, 512, 350, 0.92)
    pdf.add_rect(55, 255, 502, 340, 2, 0.3)
    pdf.add_centered_text(560, "CERTIFICATE OF COMPLETION", 'F2', 22)
    pdf.add_centered_text(520, "This certifies that", 'F1', 12)
    pdf.add_line(180, 490, 432, 490, 1, 0.4)
    pdf.add_centered_text(475, "(write your name)", 'F1', 9, 0.5)
    pdf.add_centered_text(440, "has completed all 10 Bible Stories!", 'F1', 12)
    pdf.add_centered_text(410, "You are a BIBLE CHAMPION!", 'F2', 14)
    pdf.add_centered_text(370, "Date: _______________", 'F1', 10)
    pdf.add_centered_text(310, "Great job! God is proud of you!", 'F5', 12, 0.3)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book200_Tigrinya_Kids_Bible_Activity.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
