"""Book 213: JESUS' STORIES - Parables Activity Book for Kids Ages 5-9 (KIDLYTICAL)"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.93)
    pdf.add_centered_text(620, "JESUS' STORIES", 'F2', 30)
    pdf.add_centered_text(580, "Parables Activity Book", 'F4', 16, 0.2)
    pdf.add_centered_text(553, "for Kids Ages 5-9", 'F1', 14, 0.3)
    pdf.add_centered_text(500, "10 Stories Jesus Told", 'F1', 12, 0.3)
    pdf.add_centered_text(475, "Activities + Word Search + Coloring", 'F1', 11, 0.4)
    pdf.add_centered_text(440, "KIDLYTICAL", 'F2', 14, 0.4)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "JESUS' STORIES - Parables Activity Book", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "Scripture from World English Bible (WEB)", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)

    # What is a Parable?
    pdf.new_page()
    pdf.add_centered_text(700, "WHAT IS A PARABLE?", 'F2', 22)
    pdf.add_line(72, 680, 540, 680, 1, 0.5)
    pdf.add_centered_text(650, "A parable is a simple story that teaches", 'F1', 13)
    pdf.add_centered_text(630, "an important lesson about God!", 'F1', 13)
    pdf.add_centered_text(590, "Jesus loved to teach using stories.", 'F1', 12)
    pdf.add_centered_text(565, "He used things people knew about -", 'F1', 12)
    pdf.add_centered_text(545, "sheep, seeds, coins, and families -", 'F1', 12)
    pdf.add_centered_text(525, "to teach BIG truths about God's love!", 'F1', 12)
    pdf.add_centered_text(480, "Are you ready to hear Jesus' stories?", 'F2', 14)
    pdf.add_centered_text(450, "Let's go!", 'F2', 16)

    parables = [
        ("THE LOST SHEEP", "A shepherd had 100 sheep. One got lost! He left the 99 safe sheep to find the one lost sheep. When he found it, he was SO happy! He put it on his shoulders and celebrated.",
         "Jesus was teaching us that God loves each one of us so much that He will search for us when we are lost.",
         "Luke 15:6 - Rejoice with me, for I have found my sheep!",
         ["SHEEP", "LOST", "FOUND", "HAPPY", "SEARCH", "LOVE", "SHEPHERD", "SAFE"],
         "Draw the happy shepherd carrying his lost sheep home!"),
        ("THE PRODIGAL SON", "A son asked for his money early and ran away. He spent it all and had nothing. He went home scared, but his father RAN to hug him! The father threw a big party!",
         "Jesus was teaching us that God always welcomes us back when we say sorry.",
         "Luke 15:24 - This son of mine was lost and is found!",
         ["SON", "FATHER", "HOME", "PARTY", "HUG", "SORRY", "LOVE", "RUN"],
         "Draw the father running to hug his son!"),
        ("THE GOOD SAMARITAN", "A man was hurt on the road. Important people walked past. But a Samaritan stopped, bandaged him, and took care of him. He showed real love to a stranger.",
         "Jesus was teaching us that our neighbor is anyone who needs help, and we should be kind to everyone.",
         "Luke 10:37 - Go and do likewise.",
         ["HELP", "KIND", "ROAD", "HURT", "CARE", "LOVE", "HEAL", "GIVE"],
         "Draw yourself helping someone who needs it!"),
        ("THE SOWER", "A farmer scattered seeds. Some fell on the path (eaten by birds). Some on rocks (died quickly). Some in thorns (choked). Some on good soil (grew big and strong)!",
         "Jesus was teaching us that God's word grows best in hearts that are ready to listen and obey.",
         "Matthew 13:23 - The one who hears the word and understands it bears fruit.",
         ["SEED", "SOIL", "GROW", "BIRD", "ROCK", "FRUIT", "FARMER", "HEAR"],
         "Draw a big plant growing from good soil!"),
        ("THE MUSTARD SEED", "Jesus said the kingdom of God is like a tiny mustard seed. It's the smallest seed! But when planted, it grows into the biggest plant - so big that birds nest in it!",
         "Jesus was teaching us that even small faith can grow into something amazing!",
         "Matthew 13:32 - It becomes a tree and the birds nest in its branches.",
         ["SEED", "TINY", "GROW", "BIG", "TREE", "BIRD", "NEST", "FAITH"],
         "Draw a tiny seed growing into a huge tree with birds!"),
        ("THE HIDDEN TREASURE", "A man found an amazing treasure hidden in a field! He was SO happy that he sold everything he owned to buy that field and get the treasure!",
         "Jesus was teaching us that knowing God is the most valuable treasure we can ever have!",
         "Matthew 13:44 - In his joy he sells all that he has and buys that field.",
         ["TREASURE", "FIELD", "JOY", "FIND", "GOLD", "BUY", "HAPPY", "BEST"],
         "Draw a treasure chest full of golden treasure!"),
        ("WISE & FOOLISH BUILDERS", "One man built his house on rock. Another built on sand. When storms came, the house on rock stood strong! But the house on sand fell down with a big crash!",
         "Jesus was teaching us that when we obey God's word, we build our lives on a strong foundation.",
         "Matthew 7:24 - Everyone who hears these words and does them is like a wise man.",
         ["ROCK", "SAND", "HOUSE", "STORM", "WISE", "BUILD", "STRONG", "STAND"],
         "Draw two houses - one standing strong, one falling down!"),
        ("THE TALENTS", "A master gave money to three servants. Two invested and doubled their money! One buried his in the ground. The master praised the ones who used what they were given!",
         "Jesus was teaching us to use the gifts and abilities God gives us, not hide them!",
         "Matthew 25:21 - Well done, good and faithful servant!",
         ["TALENT", "GIVE", "USE", "DOUBLE", "SERVE", "FAITHFUL", "WORK", "GOOD"],
         "Draw yourself using a talent God gave you!"),
        ("THE UNMERCIFUL SERVANT", "A king forgave a servant a HUGE debt. But that servant refused to forgive a tiny debt someone owed HIM! The king was angry because the servant was not kind like him.",
         "Jesus was teaching us that since God forgives us so much, we should forgive others too.",
         "Matthew 18:33 - Should you not have had mercy as I had mercy on you?",
         ["FORGIVE", "MERCY", "KING", "DEBT", "KIND", "FREE", "LOVE", "GIVE"],
         "Draw yourself forgiving a friend!"),
        ("THE TEN VIRGINS", "Ten girls waited for a wedding party. Five were smart and brought extra oil for their lamps. Five were not ready. When the party started, only the ready ones got in!",
         "Jesus was teaching us to be ready for when He comes back! Stay close to God always.",
         "Matthew 25:13 - Watch therefore, for you know neither the day nor the hour.",
         ["LAMP", "OIL", "READY", "WAIT", "WISE", "LIGHT", "WATCH", "PARTY"],
         "Draw five lamps shining bright in the dark!"),
    ]

    for par_num, (title, story, lesson, verse, words, color_prompt) in enumerate(parables):
        # Page 1: Story + Lesson
        pdf.new_page()
        pdf.add_filled_rect(60, 720, 492, 45, 0.85)
        pdf.add_centered_text(738, title, 'F2', 18)
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
        pdf.add_text(72, y, "JESUS WAS TEACHING US THAT:", 'F2', 11)
        y -= 16
        words_l = lesson.split()
        line = ""
        for w in words_l:
            if len(line + " " + w) > 72:
                pdf.add_text(82, y, line, 'F5', 10)
                y -= 14
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(82, y, line, 'F5', 10)
            y -= 14

        y -= 15
        pdf.add_text(72, y, "VERSE:", 'F2', 10)
        y -= 14
        pdf.add_text(82, y, verse, 'F4', 10)

        y -= 25
        pdf.add_text(72, y, "HOW CAN I LIVE THIS TODAY?", 'F2', 12)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Coloring prompt
        y -= 25
        pdf.add_text(72, y, "COLOR THIS:", 'F2', 12)
        y -= 5
        pdf.add_rect(72, y - 150, 468, 150, 1, 0.6)
        pdf.add_centered_text(y - 70, color_prompt, 'F1', 11, 0.5)

        # Page 2: Word Search + Matching
        pdf.new_page()
        pdf.add_centered_text(750, f"WORD SEARCH: {title}", 'F2', 14)
        pdf.add_text(72, 725, "Find these words:", 'F1', 10)
        word_str = "  ".join(words)
        pdf.add_text(72, 708, word_str, 'F2', 9)

        grid_size = 10
        random.seed(par_num * 61 + 17)
        grid = [[chr(random.randint(65, 90)) for _ in range(grid_size)] for _ in range(grid_size)]
        for wi, word in enumerate(words[:5]):
            if wi < grid_size and len(word) <= grid_size:
                for ci, ch in enumerate(word):
                    if ci < grid_size:
                        grid[wi][ci] = ch

        y = 680
        for row in grid:
            row_text = "  ".join(row)
            pdf.add_text(130, y, row_text, 'F3', 12)
            y -= 20

        # Matching activity
        y -= 25
        pdf.add_text(72, y, "MATCHING: Draw a line to connect!", 'F2', 12)
        y -= 20
        # Simple matching pairs related to the parable
        pdf.add_text(82, y, "The shepherd...", 'F1', 10)
        pdf.add_text(350, y, "...teaches us to forgive", 'F1', 10)
        y -= 16
        pdf.add_text(82, y, "The good soil...", 'F1', 10)
        pdf.add_text(350, y, "...finds the lost sheep", 'F1', 10)
        y -= 16
        pdf.add_text(82, y, "The father...", 'F1', 10)
        pdf.add_text(350, y, "...hears and obeys God", 'F1', 10)

    # Answer Key
    pdf.new_page()
    pdf.add_centered_text(750, "ANSWER KEY", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    y = 710
    for title, _, _, _, words, _ in parables:
        pdf.add_text(72, y, f"{title}: {', '.join(words)}", 'F1', 8)
        y -= 14

    # Certificate
    pdf.new_page()
    pdf.add_filled_rect(50, 250, 512, 350, 0.92)
    pdf.add_rect(55, 255, 502, 340, 2, 0.3)
    pdf.add_centered_text(560, "CERTIFICATE OF COMPLETION", 'F2', 22)
    pdf.add_centered_text(520, "This certifies that", 'F1', 12)
    pdf.add_line(180, 495, 432, 495, 1, 0.4)
    pdf.add_centered_text(478, "(write your name)", 'F1', 9, 0.5)
    pdf.add_centered_text(445, "has learned ALL 10 Parables of Jesus!", 'F1', 12)
    pdf.add_centered_text(415, "You are a PARABLE EXPERT!", 'F2', 14)
    pdf.add_centered_text(380, "Date: _______________", 'F1', 10)
    pdf.add_centered_text(310, "Now go and live like Jesus taught!", 'F5', 12, 0.3)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book213_Parables_Activity_Book.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
