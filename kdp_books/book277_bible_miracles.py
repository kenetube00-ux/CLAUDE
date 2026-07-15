#!/usr/bin/env python3
"""Book 277 - Amazing Miracles: 10 Incredible Things God Did in the Bible"""
import random
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(277)

TITLE = "AMAZING MIRACLES"
SUBTITLE = "10 Incredible Things God Did in the Bible"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book277_Bible_Miracles_Kids.pdf"

stories = [
    {"title": "Creation - God Makes Everything", "character": "God",
     "verse": "In the beginning, God created the heavens and the earth. - Genesis 1:1 (WEB)",
     "moral": "God's power is so great He can create something from nothing!",
     "p1": "Before anything existed, there was only God. No stars, no sun, no animals, no people - just darkness and emptiness everywhere. Then God spoke, and His powerful voice echoed through the void. 'Let there be light!' And instantly, brilliant light burst into existence, pushing away the darkness.",
     "p2": "Day after day, God continued creating amazing things. He separated the sky from the water, gathered oceans together, and made dry land appear. He filled the ground with grass, flowers, and mighty trees. He set the sun blazing in the sky for daytime and hung the moon and billions of twinkling stars for nighttime. He packed the seas with colorful fish, filled the skies with soaring birds, and covered the land with every kind of animal imaginable.",
     "p3": "On the sixth day, God did something extra special - He formed a man from dust and breathed life into him. He created woman from the man's side to be his partner. God looked at everything He had made and said it was VERY good! On the seventh day, God rested. The entire universe - every galaxy, every mountain, every tiny butterfly - was spoken into existence by God's voice alone. That is the greatest miracle of all!",
     "words": ["CREATE", "LIGHT", "STARS", "EARTH", "ANIMALS", "OCEAN", "GARDEN", "LIFE"]},
    {"title": "Noah's Flood - God Saves a Family", "character": "Noah",
     "verse": "Noah did everything that God commanded him. - Genesis 6:22 (WEB)",
     "moral": "Obedience to God protects us even in the worst storms!",
     "p1": "The world had become so wicked that God was deeply saddened. But one man named Noah still loved and obeyed God with all his heart. God told Noah He would send a great flood to wash the earth clean, but He had a plan to save Noah's family. God gave Noah exact instructions to build an enormous boat called an ark.",
     "p2": "Noah built the ark for many years while people laughed at him. It had never even rained before! But Noah kept building, trusting God's word completely. When the ark was finished, God sent two of every kind of animal marching, flying, and crawling toward the boat. Lions walked alongside lambs. Eagles flew in next to sparrows. Noah's family loaded food and supplies for everyone. Then God Himself shut the door of the ark tight.",
     "p3": "Rain poured from the sky for forty days and forty nights without stopping. Water burst up from underground springs. The flood covered the entire earth - even the tallest mountains disappeared underwater! But inside the ark, Noah's family and all the animals were safe and dry. After many months, the water receded, and a dove brought back an olive branch showing land had appeared. God placed a beautiful rainbow in the sky as His promise to never flood the whole earth again.",
     "words": ["NOAH", "ARK", "FLOOD", "ANIMALS", "RAINBOW", "DOVE", "RAIN", "FAITH"]},

    {"title": "Parting the Red Sea", "character": "Moses",
     "verse": "The LORD caused the sea to go back by a strong east wind. - Exodus 14:21 (WEB)",
     "moral": "When you feel trapped, God can make a way where there is no way!",
     "p1": "The Israelites had just escaped slavery in Egypt through God's mighty plagues. They were finally free! But Pharaoh changed his mind and sent six hundred war chariots thundering after them. The people found themselves trapped between the crashing waves of the Red Sea ahead and the dust cloud of the approaching army behind them.",
     "p2": "The people screamed in terror, certain they would die. But Moses stood firm and raised his staff toward heaven. He commanded the people to be still and watch God work. A pillar of cloud moved between them and the Egyptian army, blocking the enemy. Then Moses stretched his hand over the sea. An incredible east wind began to blow with supernatural force, howling through the night.",
     "p3": "The waters of the Red Sea split apart like curtains being pulled open! Two massive walls of water rose up on either side, and a wide path of dry ground appeared in between. The Israelites walked through with water towering above their heads on the left and right. When the Egyptians charged in after them, Moses stretched out his hand again and the walls of water came crashing down, covering the entire army. God had performed the most spectacular rescue in history!",
     "words": ["MOSES", "SEA", "SPLIT", "WIND", "DRY", "WALL", "WATER", "ESCAPE"]},
    {"title": "Manna from Heaven", "character": "the Israelites",
     "verse": "He rained down manna on them to eat. - Psalm 78:24 (WEB)",
     "moral": "God provides exactly what you need, exactly when you need it!",
     "p1": "After crossing the Red Sea, the Israelites traveled deep into the desert wilderness. There were no farms, no stores, no restaurants - nothing but sand and rocks stretching endlessly in every direction. The people began to grumble and complain, wishing they were back in Egypt where at least they had food. They were hungry and scared.",
     "p2": "God heard their cries and promised Moses something incredible would happen the very next morning. He told Moses that He would rain down bread from heaven! The people must have wondered how that was possible. That evening, thousands of quail birds flew into the camp, providing meat for dinner. Then the people went to sleep wondering what the morning would bring.",
     "p3": "When dawn broke and the dew lifted from the ground, the Israelites found something amazing covering the earth like frost. Small, round, white flakes covered the ground everywhere they looked! It tasted like wafers made with honey. They called it 'manna' meaning 'What is it?' God sent fresh manna every single morning for FORTY YEARS - enough for everyone to eat their fill. God proved He could feed millions of people in the middle of a desert with food that fell from the sky!",
     "words": ["MANNA", "HEAVEN", "BREAD", "DESERT", "MORNING", "QUAIL", "FAITH", "FOOD"]},
    {"title": "Walls of Jericho Fall Down", "character": "Joshua",
     "verse": "By faith the walls of Jericho fell down. - Hebrews 11:30 (WEB)",
     "moral": "God's methods may seem strange, but His plans always work!",
     "p1": "The massive city of Jericho stood like an impossible fortress blocking the Israelites from entering the Promised Land. Its walls were so thick that houses were built on top of them. Armed soldiers patrolled the top day and night. The gates were locked tight and no one could get in or out. Everyone inside felt completely safe from any attack.",
     "p2": "God gave Joshua the most unusual battle plan in military history. No battering rams, no siege towers, no ladders - just marching and music! The army would walk around the city once a day in complete silence for six days, with priests carrying trumpets made from ram's horns. On the seventh day, they would march around seven times, blow the trumpets, and shout. It made no logical sense, but Joshua obeyed completely.",
     "p3": "For six days, the silent army marched while Jericho's defenders watched in confusion from the walls above. On the seventh day, after the seventh trip around the city, the trumpets blasted and all the people shouted with all their might! The ground shook, cracks raced up the massive walls, and with a thunderous CRASH the entire wall collapsed flat into the dust! Every section fell outward. God proved that faith and obedience are more powerful than the strongest fortress ever built.",
     "words": ["JERICHO", "WALLS", "MARCH", "TRUMPET", "SHOUT", "SEVEN", "CRASH", "FAITH"]},

    {"title": "Elijah's Fire from Heaven", "character": "Elijah",
     "verse": "The fire of the LORD fell and consumed the offering. - 1 Kings 18:38 (WEB)",
     "moral": "The one true God always proves Himself to those who believe!",
     "p1": "Israel had been worshipping a false god called Baal, and the prophet Elijah was fed up. He challenged 450 prophets of Baal to a contest on Mount Carmel. Each side would prepare a sacrifice but use no fire - they would call on their god to send fire from heaven. Whichever god answered with fire would be proven as the real God. The people gathered to watch.",
     "p2": "The prophets of Baal went first, dancing and shouting from morning until afternoon. They screamed, jumped around, and begged Baal to answer. Nothing happened. Elijah even made fun of them, suggesting their god might be sleeping or on vacation! They yelled louder and louder but still nothing - not a spark, not a flicker. Finally they gave up, exhausted and humiliated before the watching crowd.",
     "p3": "Then Elijah rebuilt God's altar, arranged the wood and sacrifice, and did something shocking - he poured TWELVE huge jars of water all over everything until it was completely soaked and a trench around the altar was filled with water! Then Elijah simply prayed one quiet prayer. WHOOSH! Fire exploded from heaven, consuming not just the sacrifice but the wood, the stones, the dirt, and even all the water in the trench! The people fell on their faces shouting 'The LORD - He is God!'",
     "words": ["ELIJAH", "FIRE", "ALTAR", "WATER", "PRAYER", "HEAVEN", "PROVE", "LORD"]},
    {"title": "Jonah and the Great Fish", "character": "Jonah",
     "verse": "The LORD prepared a great fish to swallow up Jonah. - Jonah 1:17 (WEB)",
     "moral": "You can't run from God - His love will always find you!",
     "p1": "God told the prophet Jonah to go to the wicked city of Nineveh and warn the people to repent. But Jonah didn't want to go! He was afraid and angry, so he ran in the opposite direction. He found a ship sailing far away and paid for a ticket, thinking he could escape from God. He went below deck and fell fast asleep, running from his mission.",
     "p2": "God sent a terrible storm that threatened to tear the ship apart. Massive waves crashed over the deck while fierce winds howled. The terrified sailors discovered Jonah was running from God and reluctantly threw him overboard at his own request. The instant Jonah hit the water, the storm stopped completely. But Jonah was sinking into the dark ocean depths. Then God sent an enormous fish that swallowed Jonah whole!",
     "p3": "Inside the belly of the great fish for three days and three nights, Jonah finally prayed to God with a repentant heart. He thanked God for saving his life and promised to obey. Then the fish swam to shore and vomited Jonah onto dry land! This time when God said 'Go to Nineveh,' Jonah went immediately. The entire city repented and was saved. God used a storm, a fish, and second chances to show that His plans cannot be stopped.",
     "words": ["JONAH", "FISH", "STORM", "OCEAN", "PRAY", "OBEY", "SECOND", "CHANCE"]},
    {"title": "Jesus Walks on Water", "character": "Jesus",
     "verse": "It is I! Don't be afraid. - Matthew 14:27 (WEB)",
     "moral": "Jesus has power over nature itself - nothing is impossible for Him!",
     "p1": "It was late at night and Jesus' disciples were alone in a small boat far from shore. A powerful storm had blown in with strong winds pushing against them. The waves grew larger and more dangerous with each passing hour. The disciples rowed with all their strength but could barely make progress. They were exhausted and frightened as the storm raged around them in complete darkness.",
     "p2": "Then in the darkest hour, around three in the morning, the disciples saw something that made them scream in terror. A figure was walking toward them on TOP of the surging waves! They thought it was a ghost and cried out in fear. But then a familiar voice cut through the howling wind - 'Take courage! It is I! Don't be afraid.' It was Jesus, calmly strolling on the surface of the raging sea as if it were solid ground.",
     "p3": "Peter, always the boldest, called out asking if he could walk on the water too. Jesus said 'Come!' and Peter actually stepped out of the boat and walked on the waves toward Jesus! But when he noticed the wind, he became afraid and started sinking. Jesus immediately grabbed his hand and pulled him up. The moment they climbed into the boat, the storm completely stopped. The disciples worshipped Jesus saying 'Truly you are the Son of God!'",
     "words": ["JESUS", "WATER", "WALK", "STORM", "WAVES", "PETER", "FAITH", "POWER"]},

    {"title": "Feeding the Five Thousand", "character": "Jesus",
     "verse": "They all ate and were filled. - Matthew 14:20 (WEB)",
     "moral": "Give what little you have to God and watch Him multiply it!",
     "p1": "Thousands of people had followed Jesus to a remote hillside to hear Him teach and be healed. As evening approached, the disciples grew worried - there was no food anywhere nearby and over five thousand hungry people needed to eat. They suggested sending everyone away to find their own food in nearby villages. But Jesus said something shocking: 'You give them something to eat.'",
     "p2": "The disciples were stunned. Feed five thousand people? That would cost a fortune! Then a young boy stepped forward carrying his small lunch - just five little barley loaves and two small fish. Andrew brought the boy to Jesus but said doubtfully, 'What good are these for so many people?' Jesus smiled, took the tiny lunch, looked up to heaven, and gave thanks to His Father.",
     "p3": "Jesus broke the bread and fish, handing pieces to His disciples to distribute. They walked through the crowd passing out food - and it kept coming! Piece after piece, basket after basket, the food never ran out. Every single person in that crowd of over five thousand ate until they were completely full and satisfied. When they collected the leftovers, there were TWELVE baskets overflowing with food remaining! From one boy's tiny lunch, Jesus fed a multitude and had more left over than what they started with.",
     "words": ["FIVE", "BREAD", "FISH", "BASKET", "FEED", "CROWD", "MIRACLE", "SHARE"]},
    {"title": "The Resurrection of Jesus", "character": "Jesus",
     "verse": "He is not here, for he has risen! - Matthew 28:6 (WEB)",
     "moral": "Jesus conquered death itself - and He gives eternal life to all who believe!",
     "p1": "On a dark Friday, Jesus was crucified on a cross and died for the sins of the whole world. His friends were devastated and heartbroken. They wrapped His body in linen cloth and placed it in a tomb carved from rock. A massive stone was rolled across the entrance and Roman soldiers stood guard. Everyone thought the story was over. Hope seemed lost forever.",
     "p2": "Early on Sunday morning, some women who loved Jesus went to the tomb carrying burial spices. But as they approached, the ground shook with a powerful earthquake! An angel descended from heaven, bright as lightning, and rolled away the heavy stone like it was a pebble. The guards fainted in terror. The women looked inside the tomb with trembling hearts and saw something that changed the world forever.",
     "p3": "The tomb was EMPTY! The burial cloths were neatly folded, but Jesus' body was gone! The angel declared joyfully, 'He is not here - He has RISEN just as He said!' Then Jesus Himself appeared to them, alive and glorious! He appeared to His disciples, ate with them, taught them for forty days. Death could not hold Him. The greatest miracle in all of history - God's Son conquered the grave and offers eternal life to everyone who believes in Him!",
     "words": ["RISEN", "ALIVE", "TOMB", "EMPTY", "ANGEL", "STONE", "SUNDAY", "HOPE"]}
]


def generate_word_search(words):
    grid = [[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)] for _ in range(10)]
    for word in words[:8]:
        word = word.upper()
        for attempt in range(50):
            direction = random.choice([(0,1),(1,0),(1,1)])
            r = random.randint(0, max(0, 9 - len(word)*direction[0]))
            c = random.randint(0, max(0, 9 - len(word)*direction[1]))
            if r + len(word)*direction[0] > 10 or c + len(word)*direction[1] > 10:
                continue
            for i, ch in enumerate(word):
                grid[r+i*direction[0]][c+i*direction[1]] = ch
            break
    return grid

def wrap_text(text, max_chars=75):
    words_list = text.split()
    lines = []
    current = ""
    for w in words_list:
        if len(current) + len(w) + 1 <= max_chars:
            current += (" " if current else "") + w
        else:
            if current: lines.append(current)
            current = w
    if current: lines.append(current)
    return lines

def build_pdf():
    pdf = PDFDoc()
    page_count = 0

    # Title Page
    pdf.new_page(); page_count += 1
    pdf.add_filled_rect(50, 650, 512, 100, 0.85)
    pdf.add_centered_text(720, TITLE, 'F2', 28, 0)
    pdf.add_centered_text(690, SUBTITLE, 'F4', 14, 0.2)
    pdf.add_centered_text(660, "Written and Illustrated by", 'F4', 12, 0.3)
    pdf.add_centered_text(640, AUTHOR, 'F2', 16, 0)
    pdf.add_rect(100, 200, 412, 380, 2, 0.3)
    pdf.add_centered_text(420, "[ILLUSTRATION: A stunning collage of miracles -", 'F3', 10, 0.4)
    pdf.add_centered_text(405, "parting sea, fire from heaven, empty tomb]", 'F3', 10, 0.4)
    pdf.add_centered_text(100, "Discover the incredible power of God!", 'F4', 12, 0.3)

    # Copyright Page
    pdf.new_page(); page_count += 1
    pdf.add_centered_text(700, TITLE, 'F2', 16, 0)
    pdf.add_centered_text(670, SUBTITLE, 'F4', 11, 0.2)
    pdf.add_text(72, 600, f"Written by {AUTHOR}", 'F4', 11, 0.2)
    pdf.add_text(72, 580, "Copyright 2025. All Rights Reserved.", 'F4', 10, 0.3)
    pdf.add_text(72, 550, "Scripture quotations from the World English Bible (WEB) - Public Domain.", 'F4', 10, 0.3)
    pdf.add_text(72, 520, "Designed for children ages 6-12.", 'F4', 10, 0.3)
    pdf.add_text(72, 490, "Published by Kingdom Kids Publishing", 'F4', 10, 0.3)
    pdf.add_text(72, 460, "First Edition - 2025", 'F4', 10, 0.3)
    pdf.add_text(72, 410, "Dedication:", 'F2', 12, 0.1)
    pdf.add_text(72, 390, "To every child who wonders about God's power - these miracles are real!", 'F4', 11, 0.2)

    # Table of Contents
    pdf.new_page(); page_count += 1
    pdf.add_centered_text(730, "TABLE OF CONTENTS", 'F2', 18, 0)
    pdf.add_line(150, 720, 462, 720, 1, 0.3)
    y = 680
    for i, s in enumerate(stories):
        pdf.add_text(72, y, f"Miracle {i+1}: {s['title']}", 'F4', 12, 0.1)
        y -= 28
    pdf.add_text(72, y-10, "Quiz Section / Vocabulary / Faith Journal / Certificate / Bonus", 'F4', 10, 0.3)

    # How to Use This Book
    pdf.new_page(); page_count += 1
    pdf.add_centered_text(730, "HOW TO USE THIS BOOK", 'F2', 18, 0)
    pdf.add_line(150, 720, 462, 720, 1, 0.3)
    lines = [
        "Welcome to the most AMAZING book about God's miracles!",
        "", "Inside you will find 10 incredible true stories about",
        "times when God did the impossible.", "",
        "Each miracle has SIX pages:", "  1. The miracle story begins (with illustration)",
        "  2. The miracle unfolds (with action scene)", "  3. The miracle's conclusion + Bible verse",
        "  4. Reflection questions + prayer space", "  5. Word search puzzle",
        "  6. Draw the miracle yourself!", "",
        "Remember: The same God who did these miracles", "is alive today and loves YOU!", "",
        "Ready to be amazed? Turn the page!"
    ]
    y = 680
    for line in lines:
        pdf.add_text(72, y, line, 'F4', 11, 0.15)
        y -= 22


    # 10 stories x 6 pages = 60 pages
    for idx, story in enumerate(stories):
        # Page 1: Story opening
        pdf.new_page(); page_count += 1
        pdf.add_filled_rect(50, 700, 512, 60, 0.88)
        pdf.add_centered_text(735, f"Miracle {idx+1}", 'F1', 10, 0.4)
        pdf.add_centered_text(715, story['title'].upper(), 'F2', 18, 0)
        pdf.add_rect(100, 400, 412, 270, 1.5, 0.3)
        pdf.add_centered_text(560, f"[ILLUSTRATION: {story['title']}", 'F3', 9, 0.4)
        pdf.add_centered_text(545, "dramatic miracle scene with bright colors]", 'F3', 9, 0.4)
        for i, line in enumerate(wrap_text(story['p1'], 80)):
            pdf.add_text(72, 370-i*18, line, 'F4', 11, 0.1)

        # Page 2: Story middle
        pdf.new_page(); page_count += 1
        pdf.add_centered_text(750, f"{story['title']} (continued)", 'F2', 14, 0.1)
        pdf.add_line(72, 740, 540, 740, 0.5, 0.4)
        y = 710
        for line in wrap_text(story['p2'], 80):
            pdf.add_text(72, y, line, 'F4', 11, 0.1); y -= 20
        pdf.add_rect(100, y-260, 412, 240, 1.5, 0.3)
        pdf.add_centered_text(y-120, "[ILLUSTRATION: The miracle in progress!", 'F3', 9, 0.4)
        pdf.add_centered_text(y-135, "showing God's awesome power at work]", 'F3', 9, 0.4)

        # Page 3: Climax + verse + moral
        pdf.new_page(); page_count += 1
        pdf.add_centered_text(750, f"{story['title']} (the miracle!)", 'F2', 14, 0.1)
        pdf.add_line(72, 740, 540, 740, 0.5, 0.4)
        y = 710
        for line in wrap_text(story['p3'], 80):
            pdf.add_text(72, y, line, 'F4', 11, 0.1); y -= 20
        y -= 20
        pdf.add_filled_rect(72, y-30, 468, 40, 0.9)
        pdf.add_centered_text(y-5, "KEY BIBLE VERSE:", 'F2', 10, 0.2)
        pdf.add_centered_text(y-22, story['verse'], 'F4', 11, 0)
        y -= 70
        pdf.add_rect(72, y-40, 468, 50, 2, 0.2)
        pdf.add_centered_text(y-5, "WHAT THIS MIRACLE TEACHES US:", 'F2', 11, 0.1)
        pdf.add_centered_text(y-25, story['moral'], 'F5', 12, 0)

        # Page 4: Reflection + Prayer
        pdf.new_page(); page_count += 1
        pdf.add_centered_text(750, "WHAT I LEARNED", 'F2', 16, 0)
        pdf.add_line(150, 740, 462, 740, 1, 0.3)
        pdf.add_text(72, 710, f"Reflecting on: {story['title']}", 'F4', 11, 0.2)
        questions = [
            "1. What was the impossible problem in this story?",
            "2. How did God solve it in a miraculous way?",
            f"3. What does this miracle teach us about God's power?"
        ]
        y = 670
        for q in questions:
            pdf.add_text(72, y, q, 'F2', 11, 0.1); y -= 20
            for _ in range(3):
                pdf.add_line(90, y, 530, y, 0.5, 0.6); y -= 20
            y -= 10
        pdf.add_filled_rect(72, y-120, 468, 130, 0.92)
        pdf.add_centered_text(y-5, "MY PRAYER OF WONDER", 'F2', 14, 0.1)
        pdf.add_text(80, y-25, "Dear God, this miracle amazes me because...", 'F4', 10, 0.2)
        for i in range(5):
            pdf.add_line(80, y-50-i*20, 520, y-50-i*20, 0.5, 0.6)

        # Page 5: Word Search
        pdf.new_page(); page_count += 1
        pdf.add_centered_text(750, "WORD SEARCH PUZZLE", 'F2', 16, 0)
        pdf.add_text(72, 720, f"Find words from: {story['title']}", 'F4', 11, 0.2)
        grid = generate_word_search(story['words'])
        y = 680
        for row in grid:
            pdf.add_centered_text(y, "   ".join(row), 'F3', 14, 0.1); y -= 24
        y -= 20
        pdf.add_text(72, y, "Words to find:", 'F2', 11, 0.1); y -= 20
        pdf.add_text(72, y, "  ".join(story['words']), 'F3', 10, 0.2)
        y -= 40
        pdf.add_text(72, y, "BONUS: Write a sentence using three of these words:", 'F4', 10, 0.3)
        for _ in range(3):
            y -= 22; pdf.add_line(72, y, 540, y, 0.5, 0.6)

        # Page 6: Drawing
        pdf.new_page(); page_count += 1
        pdf.add_centered_text(750, "DRAW THIS MIRACLE!", 'F2', 16, 0)
        pdf.add_text(72, 720, f"Draw your version of: {story['title']}", 'F4', 11, 0.2)
        pdf.add_rect(72, 280, 468, 420, 1.5, 0.3)
        pdf.add_centered_text(260, "If you could ask God for a miracle, what would it be?", 'F2', 11, 0.1)
        y = 230
        for _ in range(4):
            pdf.add_line(72, y, 540, y, 0.5, 0.6); y -= 22


    # Quiz Section (2 pages)
    pdf.new_page(); page_count += 1
    pdf.add_centered_text(750, "QUIZ TIME! - Part 1", 'F2', 18, 0)
    pdf.add_line(150, 740, 462, 740, 1, 0.3)
    quizzes = [
        ("1. How many days did God take to create the world?", "a) 5  b) 6  c) 7"),
        ("2. What sign did God put in the sky after the flood?", "a) Star  b) Rainbow  c) Cloud"),
        ("3. What did the Israelites eat in the desert?", "a) Manna  b) Pizza  c) Rice"),
        ("4. How many jars of water did Elijah pour?", "a) 3  b) 7  c) 12"),
        ("5. How long was Jonah inside the fish?", "a) 1 day  b) 3 days  c) 7 days"),
    ]
    y = 700
    for q, opts in quizzes:
        pdf.add_text(72, y, q, 'F2', 11, 0.1); y -= 22
        pdf.add_text(100, y, opts, 'F4', 10, 0.2); y -= 35

    pdf.new_page(); page_count += 1
    pdf.add_centered_text(750, "QUIZ TIME! - Part 2", 'F2', 18, 0)
    pdf.add_line(150, 740, 462, 740, 1, 0.3)
    quizzes2 = [
        ("6. How many loaves did the boy have?", "a) 2  b) 5  c) 7"),
        ("7. Who walked on water with Jesus?", "a) John  b) Peter  c) James"),
        ("8. What day did Jesus rise from the dead?", "a) Friday  b) Saturday  c) Sunday"),
        ("9. How many times did Israel march around Jericho on day 7?", "a) 1  b) 3  c) 7"),
        ("10. What blew all night to part the Red Sea?", "a) East wind  b) North wind  c) Tornado"),
    ]
    y = 700
    for q, opts in quizzes2:
        pdf.add_text(72, y, q, 'F2', 11, 0.1); y -= 22
        pdf.add_text(100, y, opts, 'F4', 10, 0.2); y -= 35
    pdf.add_text(72, y-20, "Answers: 1b, 2b, 3a, 4c, 5b, 6b, 7b, 8c, 9c, 10a", 'F3', 9, 0.4)

    # Vocabulary Page
    pdf.new_page(); page_count += 1
    pdf.add_centered_text(750, "VOCABULARY & WORD LIST", 'F2', 18, 0)
    pdf.add_line(150, 740, 462, 740, 1, 0.3)
    vocab = [
        ("Miracle", "An event that defies natural law, done by God's power"),
        ("Creation", "The act of bringing something into existence from nothing"),
        ("Resurrection", "Coming back to life after dying"),
        ("Supernatural", "Beyond what is natural or explainable by science"),
        ("Providence", "God's care and guidance in all circumstances"),
        ("Omnipotent", "All-powerful - able to do anything"),
        ("Deliverance", "Being rescued or set free from danger"),
        ("Sovereign", "Having supreme power and authority over everything"),
        ("Redemption", "Being saved or bought back from trouble"),
        ("Testimony", "A declaration of what you have witnessed"),
    ]
    y = 710
    for word, defn in vocab:
        pdf.add_text(72, y, f"{word}:", 'F2', 11, 0.1)
        pdf.add_text(200, y, defn, 'F4', 10, 0.2); y -= 28

    # Faith Journal (4 pages)
    prompts = ["A miracle I see in nature every day...", "If I could witness one Bible miracle...",
               "How God has done amazing things in my life...", "What I want to thank God for today..."]
    for j in range(4):
        pdf.new_page(); page_count += 1
        pdf.add_centered_text(750, f"MY FAITH JOURNAL - Page {j+1}", 'F2', 16, 0)
        pdf.add_text(72, 710, prompts[j], 'F5', 12, 0.2)
        y = 680
        for _ in range(24):
            pdf.add_line(72, y, 540, y, 0.5, 0.7); y -= 25

    # Certificate
    pdf.new_page(); page_count += 1
    pdf.add_rect(50, 50, 512, 692, 3, 0.2)
    pdf.add_rect(60, 60, 492, 672, 1.5, 0.4)
    pdf.add_centered_text(680, "CERTIFICATE OF COMPLETION", 'F2', 22, 0)
    pdf.add_centered_text(640, "This certifies that", 'F4', 14, 0.2)
    pdf.add_line(180, 600, 432, 600, 1, 0.3)
    pdf.add_centered_text(580, "(write your name)", 'F4', 9, 0.4)
    pdf.add_centered_text(540, "has explored all 10 miracles in", 'F4', 12, 0.2)
    pdf.add_centered_text(510, "AMAZING MIRACLES", 'F2', 16, 0)
    pdf.add_centered_text(470, "and believes in the power of God!", 'F4', 12, 0.2)
    pdf.add_centered_text(400, "Date: _______________", 'F4', 12, 0.3)
    pdf.add_centered_text(280, "\"Nothing is impossible with God\" - Luke 1:37", 'F5', 14, 0.1)

    # Memory Verse Cards (2 pages)
    pdf.new_page(); page_count += 1
    pdf.add_centered_text(750, "MEMORY VERSE CARDS", 'F2', 18, 0)
    pdf.add_text(72, 725, "Cut out and memorize one verse each week!", 'F4', 10, 0.3)
    y = 690
    for i, s in enumerate(stories[:5]):
        pdf.add_rect(72, y-55, 468, 55, 1, 0.3)
        pdf.add_text(80, y-15, f"Card {i+1}: {s['title']}", 'F2', 9, 0.1)
        pdf.add_text(80, y-35, s['verse'], 'F4', 9, 0.2); y -= 65

    pdf.new_page(); page_count += 1
    pdf.add_centered_text(750, "MEMORY VERSE CARDS (continued)", 'F2', 18, 0)
    y = 700
    for i, s in enumerate(stories[5:]):
        pdf.add_rect(72, y-55, 468, 55, 1, 0.3)
        pdf.add_text(80, y-15, f"Card {i+6}: {s['title']}", 'F2', 9, 0.1)
        pdf.add_text(80, y-35, s['verse'], 'F4', 9, 0.2); y -= 65

    # Bonus: Miracle Rankings page
    pdf.new_page(); page_count += 1
    pdf.add_centered_text(750, "MY MIRACLE RANKINGS", 'F2', 18, 0)
    pdf.add_line(150, 740, 462, 740, 1, 0.3)
    pdf.add_text(72, 710, "Rank the 10 miracles from your MOST favorite (#1) to least:", 'F4', 11, 0.2)
    y = 680
    for i in range(10):
        pdf.add_text(72, y, f"#{i+1}: ", 'F2', 12, 0.1)
        pdf.add_line(110, y-2, 540, y-2, 0.5, 0.6); y -= 30
    pdf.add_text(72, y-20, "The miracle that amazes me most is:", 'F2', 11, 0.1)
    pdf.add_line(72, y-45, 540, y-45, 0.5, 0.6)
    pdf.add_text(72, y-70, "Because:", 'F4', 11, 0.2)
    pdf.add_line(72, y-95, 540, y-95, 0.5, 0.6)
    pdf.add_line(72, y-120, 540, y-120, 0.5, 0.6)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAME)
    pdf.save(output_path)
    print(f"Generated {FILENAME} with {page_count} pages")
    return page_count

if __name__ == "__main__":
    build_pdf()
