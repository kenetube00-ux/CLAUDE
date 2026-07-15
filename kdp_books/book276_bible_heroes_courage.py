#!/usr/bin/env python3
"""Book 276 - Heroes of Courage: 10 Amazing Bible Stories About Brave Kids & Adults"""
import random
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(276)

TITLE = "HEROES OF COURAGE"
SUBTITLE = "10 Amazing Bible Stories About Brave Kids & Adults"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book276_Bible_Heroes_Courage.pdf"

stories = [
    {"title": "David vs Goliath", "character": "David",
     "verse": "The LORD is my strength and my shield. - Psalm 28:7 (WEB)",
     "moral": "With God on your side, no challenge is too big!",
     "p1": "Young David was just a shepherd boy who loved to sing songs to God while watching his sheep. One day, his father sent him to bring food to his brothers who were soldiers in King Saul's army. When David arrived at the battlefield, he heard a terrifying voice booming across the valley. A giant named Goliath, over nine feet tall, was challenging anyone to fight him.",
     "p2": "All the soldiers were trembling with fear, but David felt something different in his heart. He remembered how God had helped him fight off lions and bears to protect his sheep. David told King Saul he would fight the giant. Everyone laughed at the small boy, but David knew God was with him. He picked up five smooth stones from a nearby stream and put them in his shepherd's bag. With his simple sling in hand, David walked bravely toward the massive warrior.",
     "p3": "Goliath laughed when he saw the young boy approaching without armor or sword. But David shouted with confidence that he came in the name of the Lord! He placed a stone in his sling, whirled it around, and released it with perfect aim. The stone struck Goliath right in the forehead, and the mighty giant fell to the ground with a thunderous crash. The entire army cheered as young David proved that faith in God is more powerful than any weapon or giant.",
     "words": ["DAVID", "GOLIATH", "STONE", "SLING", "BRAVE", "FAITH", "GIANT", "SHIELD"]},

    {"title": "Esther the Brave Queen", "character": "Esther",
     "verse": "Be strong and courageous. Do not be afraid. - Joshua 1:9 (WEB)",
     "moral": "God places you where you are for a reason - be brave!",
     "p1": "Esther was a beautiful young Jewish woman living in the great kingdom of Persia. The king chose her to be his queen, but no one in the palace knew she was Jewish. Esther's wise cousin Mordecai had raised her and always gave her good advice. Life in the palace seemed wonderful, but danger was lurking in the shadows.",
     "p2": "An evil man named Haman convinced the king to make a terrible law that would hurt all the Jewish people. Mordecai sent an urgent message to Esther asking her to speak to the king. But there was a huge problem - anyone who went to the king without being invited could be put to death! Esther was terrified, but Mordecai reminded her that perhaps God had made her queen for this very moment. She asked all her people to pray and fast for three days. Then she put on her royal robes and made her brave decision.",
     "p3": "With her heart pounding, Queen Esther walked into the king's throne room uninvited. The king looked up and smiled, holding out his golden scepter to welcome her. Esther invited the king to a special dinner where she revealed Haman's evil plan and her own Jewish identity. The king was furious at Haman and saved all the Jewish people. Esther's courage saved an entire nation because she trusted God and spoke up when it mattered most.",
     "words": ["ESTHER", "QUEEN", "BRAVE", "PALACE", "CROWN", "FAITH", "PERSIA", "COURAGE"]},

    {"title": "Daniel in the Lions' Den", "character": "Daniel",
     "verse": "My God sent his angel and shut the lions' mouths. - Daniel 6:22 (WEB)",
     "moral": "Keep praying and trusting God no matter what others say!",
     "p1": "Daniel was one of the wisest and most faithful men in all of Babylon. He prayed to God three times every single day, kneeling by his window that faced toward Jerusalem. Some jealous men in the kingdom noticed Daniel's prayer habit and came up with a wicked plan. They convinced King Darius to sign a law saying that no one could pray to anyone except the king for thirty days.",
     "p2": "Daniel heard about the new law but he refused to stop praying to his God. He went to his window just as he always did and knelt down to pray openly. The jealous men watched and immediately ran to tell King Darius. The king was heartbroken because he loved Daniel, but the law could not be changed. Soldiers came to arrest Daniel and brought him to the pit full of hungry, roaring lions. The king told Daniel he hoped his God would rescue him.",
     "p3": "Daniel was thrown into the den of lions and a heavy stone sealed the entrance. King Darius could not sleep all night, worrying about his friend. At the first light of dawn, the king rushed to the den and called out to Daniel. To his great joy, Daniel answered that God had sent an angel to shut the lions' mouths! Daniel was lifted out without a single scratch. The king declared that everyone must respect Daniel's God who saves those who trust in Him.",
     "words": ["DANIEL", "LIONS", "PRAYER", "ANGEL", "FAITH", "DARIUS", "BRAVE", "TRUST"]},
    {"title": "Shadrach, Meshach & Abednego", "character": "the three friends",
     "verse": "When you walk through the fire, you will not be burned. - Isaiah 43:2 (WEB)",
     "moral": "Stand firm in your faith even when everyone else gives in!",
     "p1": "In the great city of Babylon, three young Jewish friends named Shadrach, Meshach, and Abednego served faithfully in King Nebuchadnezzar's court. One day the king built an enormous golden statue that was ninety feet tall and commanded everyone to bow down and worship it. Music would play and at that signal, every person had to fall on their faces before the statue. But the three friends knew they could only worship the one true God.",
     "p2": "When the music played, thousands of people fell to the ground to worship the golden statue. But three figures remained standing tall - Shadrach, Meshach, and Abednego. Furious guards dragged them before the angry king. Nebuchadnezzar gave them one more chance to bow down or be thrown into a blazing furnace. The three friends calmly replied that their God could save them, but even if He chose not to, they would never bow to a false idol. The king ordered the furnace heated seven times hotter than normal.",
     "p3": "Soldiers threw the three friends into the roaring flames. But then the king jumped up in amazement - he saw FOUR people walking in the fire, unhurt! The fourth looked like an angel of God. Nebuchadnezzar called them out and everyone saw that not a single hair was burned. They did not even smell like smoke! The king praised their God and made a new law protecting those who worshiped the Lord. Their faith had turned a death sentence into an incredible miracle.",
     "words": ["FURNACE", "FIRE", "THREE", "FRIENDS", "ANGEL", "FAITH", "STAND", "BRAVE"]},

    {"title": "Joshua at Jericho", "character": "Joshua",
     "verse": "By faith the walls of Jericho fell down. - Hebrews 11:30 (WEB)",
     "moral": "Follow God's instructions even when they seem strange!",
     "p1": "After Moses died, God chose Joshua to lead the Israelites into the Promised Land. But there was a huge problem - the city of Jericho stood in their path with massive walls so thick that houses were built on top of them. The gates were locked tight and no one could get in or out. Joshua looked at those towering walls and wondered how they could ever conquer such a mighty fortress.",
     "p2": "Then God gave Joshua the most unusual battle plan ever. Instead of battering rams or ladders, God told them to march silently around the city once a day for six days. On the seventh day, they would march around seven times and then blow their trumpets and shout. Joshua trusted God completely and told his people the plan. For six days, the Israelites marched in silence while the people of Jericho watched from the walls in confusion. The soldiers carried the Ark of the Covenant as priests blew ram's horn trumpets.",
     "p3": "On the seventh day, the Israelites rose at dawn and marched around Jericho seven times. After the seventh lap, Joshua commanded the people to shout with all their might. The trumpets blasted, the people roared, and then something incredible happened - the massive walls of Jericho came crashing down flat! Every section crumbled to dust. The Israelites charged in and won the victory God had promised. Joshua learned that obedience to God brings victories no army could win alone.",
     "words": ["JOSHUA", "WALLS", "MARCH", "SHOUT", "TRUMPET", "FAITH", "JERICHO", "OBEY"]},
    {"title": "Gideon's 300 Warriors", "character": "Gideon",
     "verse": "The LORD said, By the 300 I will save you. - Judges 7:7 (WEB)",
     "moral": "God can do amazing things with just a few faithful people!",
     "p1": "The Midianites were terrorizing Israel, destroying their crops and stealing everything. An angel appeared to a young man named Gideon who was secretly threshing wheat in a winepress to hide from the enemy. The angel called him a mighty warrior, but Gideon felt like the weakest person in the smallest tribe. God promised to be with him and use him to save Israel from their enemies.",
     "p2": "Gideon gathered an army of 32,000 men to fight the massive Midianite army. But God said there were too many soldiers - the people would think THEY won the battle instead of giving God the glory. First God sent home everyone who was afraid - 22,000 left! Then God tested the remaining men by how they drank water at a stream. Only 300 men lapped water from their hands while staying alert. God said these 300 were enough. Gideon was stunned but he trusted God's plan completely.",
     "p3": "In the dark of night, Gideon gave each of his 300 men a trumpet, an empty clay jar, and a torch hidden inside. They surrounded the enormous enemy camp. At Gideon's signal, they smashed their jars, held up their blazing torches, and blew their trumpets shouting 'A sword for the Lord and for Gideon!' The confused Midianites panicked in the sudden light and noise, fighting each other in chaos before fleeing. God won an impossible victory with just 300 faithful warriors.",
     "words": ["GIDEON", "THREE", "HUNDRED", "TORCH", "TRUMPET", "FAITH", "NIGHT", "BRAVE"]},

    {"title": "Ruth the Loyal", "character": "Ruth",
     "verse": "Where you go, I will go. Your God will be my God. - Ruth 1:16 (WEB)",
     "moral": "Loyalty and kindness are rewarded by God!",
     "p1": "Ruth was a young woman from the land of Moab who married into an Israelite family. Tragically, her husband died, leaving her mother-in-law Naomi heartbroken and alone. Naomi decided to return to her homeland of Bethlehem and told Ruth to go back to her own family where life would be easier. But Ruth loved Naomi too much to leave her alone.",
     "p2": "With beautiful words of devotion, Ruth declared she would never leave Naomi's side. They traveled together to Bethlehem with nothing but the clothes on their backs. Ruth immediately went to work gathering leftover grain in the fields to feed them both. She worked from early morning until late evening without complaining. The owner of the field, a kind man named Boaz, noticed Ruth's hard work and her loyalty to Naomi. He ordered his workers to leave extra grain for her to find.",
     "p3": "Boaz was amazed by Ruth's courage in leaving everything familiar to care for her mother-in-law. He admired her faith in choosing to follow the God of Israel. As time passed, Boaz and Ruth fell in love and married. Ruth became the great-grandmother of King David and an ancestor of Jesus Himself. Her story shows that loyalty, hard work, and kindness are never wasted - God sees every sacrifice and rewards faithful hearts in ways we never imagine.",
     "words": ["RUTH", "LOYAL", "NAOMI", "GRAIN", "BOAZ", "FAITH", "LOVE", "KIND"]},
    {"title": "Joseph the Dreamer", "character": "Joseph",
     "verse": "You meant evil against me, but God meant it for good. - Genesis 50:20 (WEB)",
     "moral": "God can turn your worst days into your greatest purpose!",
     "p1": "Joseph was the favorite son of his father Jacob, who gave him a beautiful coat of many colors. God gave Joseph special dreams showing that one day his family would bow before him. When Joseph told his brothers about the dreams, they became incredibly jealous. One terrible day, they threw Joseph into a deep pit and then sold him as a slave to traders heading to Egypt.",
     "p2": "In Egypt, Joseph worked faithfully as a servant even though his heart ached for home. He was falsely accused and thrown into prison for years. But even in that dark dungeon, Joseph kept trusting God and using his gift to interpret dreams. One day, the powerful Pharaoh of Egypt had a mysterious dream that no one could explain. Someone remembered Joseph's gift, and he was brought from prison to stand before the most powerful ruler in the world.",
     "p3": "God showed Joseph that Pharaoh's dream meant seven years of plenty followed by seven years of famine. Pharaoh was so impressed that he made Joseph the second most powerful person in all of Egypt! When the famine came, Joseph's brothers traveled to Egypt begging for food - and they bowed before Joseph just as the dream had shown. Instead of revenge, Joseph forgave them with tears of joy. What his brothers meant for evil, God had transformed into the salvation of an entire nation.",
     "words": ["JOSEPH", "DREAM", "COAT", "COLORS", "EGYPT", "FAITH", "FORGIVE", "HOPE"]},

    {"title": "Moses Parts the Sea", "character": "Moses",
     "verse": "Do not be afraid. Stand firm. See the salvation of the LORD. - Exodus 14:13 (WEB)",
     "moral": "When you feel trapped, trust that God will make a way!",
     "p1": "Moses had led the Israelites out of slavery in Egypt after God sent ten mighty plagues. They were finally free! But as they journeyed through the wilderness, they came to the edge of the Red Sea with no boats and no bridge. Then they heard the terrifying sound of thundering hooves - Pharaoh had changed his mind and sent his entire army of chariots to capture them.",
     "p2": "The people were trapped - the sea ahead, mountains on either side, and hundreds of enemy chariots racing toward them from behind. The Israelites cried out in fear, some even wishing they had stayed as slaves. But Moses stood tall and raised his staff toward the heavens. He shouted to the people not to be afraid because God Himself would fight for them today. A towering pillar of cloud moved between them and the Egyptian army, blocking the enemy's advance through the entire night.",
     "p3": "Moses stretched out his hand over the sea, and God sent a powerful east wind that blew all night long. The waters split apart, rising up like walls on the left and right, with dry ground appearing in between! The Israelites walked through on dry land with walls of water towering on both sides. When the Egyptians tried to follow, Moses stretched out his hand again and the waters crashed back together. God had saved His people with the most spectacular miracle they had ever seen.",
     "words": ["MOSES", "WATER", "STAFF", "PARTED", "EGYPT", "FAITH", "FREE", "TRUST"]},
    {"title": "Peter Walks on Water", "character": "Peter",
     "verse": "Lord, if it is you, command me to come to you on the water. - Matthew 14:28 (WEB)",
     "moral": "Keep your eyes on Jesus and you can do impossible things!",
     "p1": "Jesus had just fed five thousand people with only five loaves and two fish. Afterward, he sent his disciples ahead in a boat while he went up a mountain alone to pray. Late that night, the disciples were far from shore and their boat was being tossed by strong winds and crashing waves. They were exhausted and frightened as the storm grew worse around them in the darkness.",
     "p2": "In the darkest hour before dawn, the disciples saw a figure walking toward them ON TOP of the churning waves. They screamed in terror, thinking it was a ghost! But Jesus called out through the wind telling them not to be afraid. Bold Peter shouted back asking if it was really Jesus, then dared to ask if he could walk on the water too. Jesus simply said one word - 'Come!' Peter swung his legs over the side of the rocking boat and stepped onto the stormy sea.",
     "p3": "Amazingly, Peter's feet found solid footing on the surface of the water! He was actually walking on the waves toward Jesus! But then Peter noticed the howling wind and massive waves around him. Fear flooded his heart and he immediately began to sink into the cold dark water. He cried out for Jesus to save him. Instantly, Jesus reached out his hand and caught him. Back in the boat, the storm calmed completely. Peter learned that faith means keeping your eyes fixed on Jesus, not on the storms around you.",
     "words": ["PETER", "WATER", "WAVES", "WALK", "STORM", "FAITH", "JESUS", "TRUST"]}
]


def generate_word_search(words):
    """Generate a 10x10 word search grid with hidden words."""
    grid = [[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)] for _ in range(10)]
    for word in words[:8]:
        word = word.upper()
        placed = False
        for attempt in range(50):
            direction = random.choice([(0,1),(1,0),(1,1)])
            r = random.randint(0, 9 - len(word)*direction[0]) if direction[0] else random.randint(0,9)
            c = random.randint(0, 9 - len(word)*direction[1]) if direction[1] else random.randint(0,9)
            if r + len(word)*direction[0] > 10 or c + len(word)*direction[1] > 10:
                continue
            can_place = True
            for i, ch in enumerate(word):
                nr, nc = r+i*direction[0], c+i*direction[1]
                if nr >= 10 or nc >= 10:
                    can_place = False
                    break
                if grid[nr][nc] != ch and grid[nr][nc].isupper():
                    pass  # overwrite random letters
            if can_place:
                for i, ch in enumerate(word):
                    grid[r+i*direction[0]][c+i*direction[1]] = ch
                placed = True
                break
    return grid

def wrap_text(text, max_chars=75):
    """Wrap text into lines of max_chars width."""
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= max_chars:
            current += (" " if current else "") + w
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines

def build_pdf():
    pdf = PDFDoc()
    page_count = 0

    # --- PAGE 1: Title Page ---
    pdf.new_page()
    page_count += 1
    pdf.add_filled_rect(50, 650, 512, 100, 0.85)
    pdf.add_centered_text(720, TITLE, 'F2', 28, 0)
    pdf.add_centered_text(690, SUBTITLE, 'F4', 14, 0.2)
    pdf.add_centered_text(650, "Written and Illustrated by", 'F4', 12, 0.3)
    pdf.add_centered_text(630, AUTHOR, 'F2', 16, 0)
    pdf.add_rect(100, 200, 412, 380, 2, 0.3)
    pdf.add_centered_text(420, "[ILLUSTRATION: A collage of brave Bible heroes", 'F3', 10, 0.4)
    pdf.add_centered_text(405, "standing together with shields and swords of faith]", 'F3', 10, 0.4)
    pdf.add_centered_text(100, "For brave kids who want to learn about God's heroes!", 'F4', 12, 0.3)

    # --- PAGE 2: Copyright Page ---
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(700, "HEROES OF COURAGE", 'F2', 16, 0)
    pdf.add_centered_text(670, "10 Amazing Bible Stories About Brave Kids & Adults", 'F4', 11, 0.2)
    pdf.add_text(72, 600, f"Written by {AUTHOR}", 'F4', 11, 0.2)
    pdf.add_text(72, 580, "Copyright 2025. All Rights Reserved.", 'F4', 10, 0.3)
    pdf.add_text(72, 550, "No part of this publication may be reproduced without permission.", 'F4', 10, 0.3)
    pdf.add_text(72, 520, "Scripture quotations from the World English Bible (WEB) - Public Domain.", 'F4', 10, 0.3)
    pdf.add_text(72, 490, "This book is designed for children ages 6-12.", 'F4', 10, 0.3)
    pdf.add_text(72, 460, "Published by Kingdom Kids Publishing", 'F4', 10, 0.3)
    pdf.add_text(72, 430, "First Edition - 2025", 'F4', 10, 0.3)
    pdf.add_text(72, 380, "Dedication:", 'F2', 12, 0.1)
    pdf.add_text(72, 360, "For every child who needs courage - God is always with you!", 'F4', 11, 0.2)

    # --- PAGE 3: Table of Contents ---
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(730, "TABLE OF CONTENTS", 'F2', 18, 0)
    pdf.add_line(150, 720, 462, 720, 1, 0.3)
    y = 680
    for i, story in enumerate(stories):
        pdf.add_text(72, y, f"Story {i+1}: {story['title']}", 'F4', 12, 0.1)
        pdf.add_text(450, y, f"Page {5 + i*6}", 'F1', 10, 0.3)
        y -= 30
    pdf.add_text(72, y-20, "Quiz Section", 'F2', 12, 0.1)
    pdf.add_text(72, y-45, "Vocabulary & Word List", 'F2', 12, 0.1)
    pdf.add_text(72, y-70, "My Faith Journal", 'F2', 12, 0.1)
    pdf.add_text(72, y-95, "Certificate of Completion", 'F2', 12, 0.1)
    pdf.add_text(72, y-120, "Bonus: Memory Verse Cards", 'F2', 12, 0.1)

    # --- PAGE 4: How to Use This Book ---
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(730, "HOW TO USE THIS BOOK", 'F2', 18, 0)
    pdf.add_line(150, 720, 462, 720, 1, 0.3)
    intro_lines = [
        "Welcome, brave reader! This book contains 10 amazing stories about",
        "real heroes from the Bible who showed incredible courage.",
        "",
        "Each story has SIX exciting pages:",
        "  1. The story beginning with a colorful illustration",
        "  2. The middle of the story with an action scene",
        "  3. The exciting ending with a Bible verse and moral",
        "  4. A reflection page with questions and prayer space",
        "  5. A fun word search puzzle with words from the story",
        "  6. A drawing page where YOU become the artist!",
        "",
        "Tips for Parents and Teachers:",
        "  - Read one story per day or week for best results",
        "  - Discuss the questions together as a family",
        "  - Encourage children to write their own prayers",
        "  - Use the word searches as vocabulary builders",
        "  - Let children color and draw freely on activity pages",
        "",
        "Are you ready to meet some incredible heroes?",
        "Turn the page and let the adventure begin!"
    ]
    y = 680
    for line in intro_lines:
        pdf.add_text(72, y, line, 'F4', 11, 0.15)
        y -= 22


    # --- STORIES (10 stories x 6 pages = 60 pages) ---
    for idx, story in enumerate(stories):
        # PAGE 1: Story Title + Opening
        pdf.new_page()
        page_count += 1
        pdf.add_filled_rect(50, 700, 512, 60, 0.88)
        pdf.add_centered_text(735, f"Story {idx+1}", 'F1', 10, 0.4)
        pdf.add_centered_text(715, story['title'].upper(), 'F2', 20, 0)
        pdf.add_rect(100, 400, 412, 270, 1.5, 0.3)
        pdf.add_centered_text(560, f"[ILLUSTRATION: {story['character']} in a dramatic scene", 'F3', 9, 0.4)
        pdf.add_centered_text(545, "showing courage and faith in God]", 'F3', 9, 0.4)
        lines = wrap_text(story['p1'], 80)
        y = 370
        for line in lines:
            pdf.add_text(72, y, line, 'F4', 11, 0.1)
            y -= 18

        # PAGE 2: Story Middle
        pdf.new_page()
        page_count += 1
        pdf.add_centered_text(750, f"{story['title']} (continued)", 'F2', 14, 0.1)
        pdf.add_line(72, 740, 540, 740, 0.5, 0.4)
        lines = wrap_text(story['p2'], 80)
        y = 710
        for line in lines:
            pdf.add_text(72, y, line, 'F4', 11, 0.1)
            y -= 20
        pdf.add_rect(100, y-280, 412, 250, 1.5, 0.3)
        pdf.add_centered_text(y-130, f"[ILLUSTRATION: Action scene - {story['character']}", 'F3', 9, 0.4)
        pdf.add_centered_text(y-145, "facing the challenge with determination]", 'F3', 9, 0.4)

        # PAGE 3: Climax + Verse + Moral
        pdf.new_page()
        page_count += 1
        pdf.add_centered_text(750, f"{story['title']} (conclusion)", 'F2', 14, 0.1)
        pdf.add_line(72, 740, 540, 740, 0.5, 0.4)
        lines = wrap_text(story['p3'], 80)
        y = 710
        for line in lines:
            pdf.add_text(72, y, line, 'F4', 11, 0.1)
            y -= 20
        # Bible Verse
        y -= 20
        pdf.add_filled_rect(72, y-30, 468, 40, 0.9)
        pdf.add_centered_text(y-5, "KEY BIBLE VERSE:", 'F2', 10, 0.2)
        pdf.add_centered_text(y-22, story['verse'], 'F4', 11, 0)
        # Moral Box
        y -= 70
        pdf.add_rect(72, y-40, 468, 50, 2, 0.2)
        pdf.add_centered_text(y-5, "MORAL OF THE STORY:", 'F2', 11, 0.1)
        pdf.add_centered_text(y-25, story['moral'], 'F5', 12, 0)

        # PAGE 4: Reflection + Prayer
        pdf.new_page()
        page_count += 1
        pdf.add_centered_text(750, "WHAT I LEARNED", 'F2', 16, 0)
        pdf.add_line(150, 740, 462, 740, 1, 0.3)
        pdf.add_text(72, 710, f"Reflecting on: {story['title']}", 'F4', 11, 0.2)
        questions = [
            f"1. What made {story['character']} brave in this story?",
            "2. How did God help in this situation?",
            "3. How can you show the same kind of courage in your life?"
        ]
        y = 670
        for q in questions:
            pdf.add_text(72, y, q, 'F2', 11, 0.1)
            y -= 20
            for _ in range(3):
                pdf.add_line(90, y, 530, y, 0.5, 0.6)
                y -= 20
            y -= 10
        # Prayer section
        y -= 10
        pdf.add_filled_rect(72, y-120, 468, 130, 0.92)
        pdf.add_centered_text(y-5, "MY PRAYER", 'F2', 14, 0.1)
        pdf.add_text(80, y-25, "Dear God, after reading this story I want to tell you...", 'F4', 10, 0.2)
        for i in range(5):
            pdf.add_line(80, y-50-i*20, 520, y-50-i*20, 0.5, 0.6)
        pdf.add_text(400, y-155, "Amen.", 'F5', 12, 0.1)


        # PAGE 5: Word Search
        pdf.new_page()
        page_count += 1
        pdf.add_centered_text(750, "WORD SEARCH PUZZLE", 'F2', 16, 0)
        pdf.add_text(72, 720, f"Find these words from the story of {story['title']}:", 'F4', 11, 0.2)
        grid = generate_word_search(story['words'])
        y = 680
        for row in grid:
            row_text = "   ".join(row)
            pdf.add_centered_text(y, row_text, 'F3', 14, 0.1)
            y -= 24
        y -= 20
        pdf.add_text(72, y, "Words to find:", 'F2', 11, 0.1)
        y -= 20
        word_line = "  ".join(story['words'])
        pdf.add_text(72, y, word_line, 'F3', 10, 0.2)
        y -= 40
        pdf.add_text(72, y, "BONUS CHALLENGE: Can you use three of these words in a sentence?", 'F4', 10, 0.3)
        y -= 20
        for _ in range(3):
            pdf.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22

        # PAGE 6: Drawing Page
        pdf.new_page()
        page_count += 1
        pdf.add_centered_text(750, "DRAW YOUR FAVORITE PART!", 'F2', 16, 0)
        pdf.add_text(72, 720, f"Draw your favorite scene from the story of {story['title']}:", 'F4', 11, 0.2)
        pdf.add_rect(72, 280, 468, 420, 1.5, 0.3)
        pdf.add_centered_text(260, f"How can I be brave like {story['character']}?", 'F2', 12, 0.1)
        y = 230
        for _ in range(4):
            pdf.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22
        pdf.add_text(72, y-10, "My courage goal this week:", 'F2', 10, 0.2)
        pdf.add_line(72, y-30, 540, y-30, 0.5, 0.6)

    # --- QUIZ SECTION (2 pages) ---
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(750, "QUIZ TIME! - Part 1", 'F2', 18, 0)
    pdf.add_line(150, 740, 462, 740, 1, 0.3)
    quiz_questions = [
        ("1. What did David use to defeat Goliath?", "a) Sword  b) Sling & stone  c) Spear"),
        ("2. Who said 'Where you go, I will go'?", "a) Esther  b) Ruth  c) Mary"),
        ("3. How many times did Israel march around Jericho on day 7?", "a) 3 times  b) 7 times  c) 12 times"),
        ("4. How many warriors did God choose for Gideon?", "a) 32,000  b) 3,000  c) 300"),
        ("5. What shut the lions' mouths in Daniel's story?", "a) A rock  b) God's angel  c) Daniel's prayer"),
    ]
    y = 700
    for q, opts in quiz_questions:
        pdf.add_text(72, y, q, 'F2', 11, 0.1)
        y -= 22
        pdf.add_text(100, y, opts, 'F4', 10, 0.2)
        y -= 35

    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(750, "QUIZ TIME! - Part 2", 'F2', 18, 0)
    pdf.add_line(150, 740, 462, 740, 1, 0.3)
    quiz_questions2 = [
        ("6. What did Esther risk by visiting the king?", "a) Her crown  b) Her life  c) Her money"),
        ("7. How many men were in the fiery furnace?", "a) 2  b) 3  c) 4 (including the angel)"),
        ("8. What happened when Peter took his eyes off Jesus?", "a) He flew  b) He sank  c) He swam"),
        ("9. Joseph was sold as a slave by his...", "a) Friends  b) Brothers  c) Enemies"),
        ("10. What did Moses hold when parting the Red Sea?", "a) His staff  b) A sword  c) A shield"),
    ]
    y = 700
    for q, opts in quiz_questions2:
        pdf.add_text(72, y, q, 'F2', 11, 0.1)
        y -= 22
        pdf.add_text(100, y, opts, 'F4', 10, 0.2)
        y -= 35
    pdf.add_text(72, y-20, "Answers: 1b, 2b, 3b, 4c, 5b, 6b, 7c, 8b, 9b, 10a", 'F3', 9, 0.4)


    # --- VOCABULARY PAGE ---
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(750, "VOCABULARY & WORD LIST", 'F2', 18, 0)
    pdf.add_line(150, 740, 462, 740, 1, 0.3)
    vocab = [
        ("Courage", "Being brave even when you feel scared"),
        ("Faith", "Trusting God even when you cannot see the answer"),
        ("Miracle", "Something amazing that only God can do"),
        ("Obedience", "Following God's instructions willingly"),
        ("Devotion", "Loving someone with all your heart"),
        ("Sacrifice", "Giving up something for someone else"),
        ("Victory", "Winning a battle or challenge"),
        ("Salvation", "Being saved or rescued by God"),
        ("Prophet", "Someone who speaks God's messages"),
        ("Worship", "Showing love and respect to God"),
        ("Perseverance", "Never giving up no matter how hard it gets"),
        ("Redemption", "Being bought back or set free from trouble"),
    ]
    y = 710
    for word, defn in vocab:
        pdf.add_text(72, y, f"{word}:", 'F2', 11, 0.1)
        pdf.add_text(200, y, defn, 'F4', 10, 0.2)
        y -= 25

    # --- FAITH JOURNAL (4 pages) ---
    for j in range(4):
        pdf.new_page()
        page_count += 1
        pdf.add_centered_text(750, f"MY FAITH JOURNAL - Page {j+1}", 'F2', 16, 0)
        pdf.add_line(150, 740, 462, 740, 1, 0.3)
        prompts = [
            "Today I saw God's courage in...",
            "A time I was brave like a Bible hero...",
            "What I want to tell God today...",
            "My favorite Bible hero and why..."
        ]
        pdf.add_text(72, 710, prompts[j], 'F5', 12, 0.2)
        y = 680
        for _ in range(24):
            pdf.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 25

    # --- CERTIFICATE OF COMPLETION ---
    pdf.new_page()
    page_count += 1
    pdf.add_rect(50, 50, 512, 692, 3, 0.2)
    pdf.add_rect(60, 60, 492, 672, 1.5, 0.4)
    pdf.add_centered_text(680, "CERTIFICATE OF COMPLETION", 'F2', 22, 0)
    pdf.add_centered_text(640, "This certifies that", 'F4', 14, 0.2)
    pdf.add_line(180, 600, 432, 600, 1, 0.3)
    pdf.add_centered_text(580, "(write your name)", 'F4', 9, 0.4)
    pdf.add_centered_text(540, "has successfully read all 10 stories in", 'F4', 12, 0.2)
    pdf.add_centered_text(510, "HEROES OF COURAGE", 'F2', 16, 0)
    pdf.add_centered_text(470, "and has shown the bravery of a true Bible hero!", 'F4', 12, 0.2)
    pdf.add_centered_text(400, "Date: _______________", 'F4', 12, 0.3)
    pdf.add_centered_text(350, "Signed: _______________", 'F4', 12, 0.3)
    pdf.add_centered_text(280, "\"Be strong and courageous!\" - Joshua 1:9", 'F5', 14, 0.1)

    # --- MEMORY VERSE CARDS ---
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(750, "MEMORY VERSE CARDS", 'F2', 18, 0)
    pdf.add_text(72, 725, "Cut out these cards and memorize one verse each week!", 'F4', 10, 0.3)
    y = 690
    for i, story in enumerate(stories[:5]):
        pdf.add_rect(72, y-55, 468, 55, 1, 0.3)
        pdf.add_text(80, y-15, f"Card {i+1}: {story['title']}", 'F2', 9, 0.1)
        pdf.add_text(80, y-35, story['verse'], 'F4', 9, 0.2)
        y -= 65

    # --- BONUS ACTIVITY PAGES ---
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(750, "MEMORY VERSE CARDS (continued)", 'F2', 18, 0)
    y = 700
    for i, story in enumerate(stories[5:]):
        pdf.add_rect(72, y-55, 468, 55, 1, 0.3)
        pdf.add_text(80, y-15, f"Card {i+6}: {story['title']}", 'F2', 9, 0.1)
        pdf.add_text(80, y-35, story['verse'], 'F4', 9, 0.2)
        y -= 65

    # Bonus: Courage Pledge page
    pdf.new_page()
    page_count += 1
    pdf.add_centered_text(750, "MY COURAGE PLEDGE", 'F2', 18, 0)
    pdf.add_line(150, 740, 462, 740, 1, 0.3)
    pledge_lines = [
        "I pledge to be brave like the heroes in this book!",
        "",
        "With God's help, I promise to:",
        "  - Stand up for what is right",
        "  - Trust God when things are scary",
        "  - Be kind and loyal to others",
        "  - Pray every day for courage",
        "  - Help others who are afraid",
        "",
        "My name: _________________________________",
        "",
        "Date: ____________________________________",
        "",
        "My favorite hero from this book: __________",
        "",
        "The bravest thing I want to do: ___________",
        "________________________________________",
        "",
        "My prayer for courage:"
    ]
    y = 710
    for line in pledge_lines:
        pdf.add_text(72, y, line, 'F4', 11, 0.15)
        y -= 22
    for _ in range(4):
        pdf.add_line(72, y, 540, y, 0.5, 0.6)
        y -= 22

    # Save PDF
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAME)
    pdf.save(output_path)
    print(f"Generated {FILENAME} with {page_count} pages")
    return page_count

if __name__ == "__main__":
    build_pdf()
