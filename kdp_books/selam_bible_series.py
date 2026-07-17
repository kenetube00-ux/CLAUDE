#!/usr/bin/env python3
"""Generate Selam Fesehaye's Little Blessings Bible Series (8 books)
Format: 8.5x8.5 square picture books for toddlers/preschoolers
Author: Selam Fesehaye"""
import sys, os
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

AUTHOR = "Selam Fesehaye"
SERIES = "Little Blessings Bible Series"

def create_childrens_book(book_num, filename, title, subtitle, age_range, stories):
    """Create a children's Bible picture book PDF (square format)"""
    pdf = PDFDoc(width=612, height=612)  # 8.5x8.5 square
    
    # ===== TITLE PAGE =====
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 612, gray=0.95)
    pdf.add_filled_rect(0, 400, 612, 212, gray=0.14)
    pdf.add_rect(20, 20, 572, 572, line_width=2.5, gray=0.3)
    
    # Title
    tlines = title.split('\n')
    ty = 560 if len(tlines) == 1 else 575
    for i, tl in enumerate(tlines):
        pdf.add_centered_text(ty - i*40, tl, font='F2', size=26, gray=0.95)
    
    # Subtitle
    pdf.add_centered_text(420, subtitle, font='F4', size=13, gray=0.8)
    
    # Decorative
    pdf.add_line(150, 390, 462, 390, width=1.5, gray=0.4)
    pdf.add_centered_text(360, SERIES, font='F1', size=11, gray=0.4)
    pdf.add_centered_text(320, f"Ages {age_range}", font='F2', size=13, gray=0.3)
    
    # Author
    pdf.add_centered_text(200, f"Written by {AUTHOR}", font='F2', size=15, gray=0.2)
    
    # Bottom
    pdf.add_centered_text(80, "Scripture from King James Version (Public Domain)", font='F1', size=8, gray=0.5)
    pdf.add_centered_text(60, "For Amazon Kindle & Paperback", font='F1', size=8, gray=0.5)
    
    # Small decorative elements (stars)
    pdf.add_text(50, 300, "*", font='F2', size=20, gray=0.3)
    pdf.add_text(540, 320, "*", font='F2', size=16, gray=0.3)
    pdf.add_text(100, 250, "*", font='F2', size=12, gray=0.35)
    pdf.add_text(500, 260, "*", font='F2', size=14, gray=0.35)
    
    # ===== COPYRIGHT PAGE =====
    pdf.new_page()
    pdf.add_centered_text(520, "Copyright", font='F2', size=14, gray=0.2)
    copy_lines = [
        title.replace('\n', ' '),
        f"Written by {AUTHOR}",
        "",
        f"Part of the {SERIES}",
        "",
        "All rights reserved. No portion of this book may be",
        "reproduced without written permission from the author.",
        "",
        "Scripture quotations from the King James Version (KJV),",
        "which is in the public domain.",
        "",
        "First Edition, 2025",
        "",
        "For ordering information, contact:",
        "selamfesehaye@biblemakesimple.com",
    ]
    y = 470
    for line in copy_lines:
        pdf.add_centered_text(y, line, font='F1', size=10, gray=0.3)
        y -= 18
    
    # ===== DEDICATION PAGE =====
    pdf.new_page()
    pdf.add_filled_rect(100, 250, 412, 150, gray=0.92)
    pdf.add_rect(100, 250, 412, 150, line_width=0.5, gray=0.5)
    pdf.add_centered_text(370, "Dedication", font='F5', size=16, gray=0.2)
    pdf.add_centered_text(330, "For every little one who needs to know", font='F4', size=12, gray=0.25)
    pdf.add_centered_text(305, "they are loved by God.", font='F4', size=12, gray=0.25)
    pdf.add_centered_text(270, "And for the parents who read these words aloud —", font='F4', size=11, gray=0.35)
    pdf.add_centered_text(248, "you are planting seeds of faith.", font='F4', size=11, gray=0.35)
    
    # ===== A NOTE TO PARENTS =====
    pdf.new_page()
    pdf.add_centered_text(560, "A Note to Parents", font='F2', size=16, gray=0.15)
    pdf.add_line(180, 548, 432, 548, width=0.5, gray=0.3)
    note_lines = [
        "Dear Parent or Caregiver,",
        "",
        "Thank you for choosing this book as part of your",
        "little one's bedtime routine. These stories are",
        "written in simple, calming language perfect for",
        "toddler ears and sleepy hearts.",
        "",
        "Each story ends with a short prayer you can say",
        "together. Feel free to add your child's name to",
        "make it personal and special.",
        "",
        "There is no wrong way to read this book. Read one",
        "story per night, or let your child pick their",
        "favorite. The goal is simple: help your little one",
        "fall asleep knowing God loves them.",
        "",
        "Sweet dreams and God's blessings,",
        f"{AUTHOR}",
    ]
    y = 510
    for line in note_lines:
        pdf.add_centered_text(y, line, font='F1', size=11, gray=0.2)
        y -= 22
    
    # ===== TABLE OF CONTENTS =====
    pdf.new_page()
    pdf.add_centered_text(570, "Stories Inside", font='F2', size=16, gray=0.15)
    pdf.add_line(180, 558, 432, 558, width=0.5, gray=0.3)
    y = 530
    for i, (story_title, _, _, _) in enumerate(stories):
        if y < 60:
            pdf.new_page()
            y = 560
        pdf.add_text(80, y, f"{i+1}.", font='F2', size=10, gray=0.3)
        pdf.add_text(105, y, story_title, font='F1', size=10, gray=0.2)
        y -= 22
    
    # ===== STORY PAGES =====
    for story_idx, (story_title, scripture_ref, story_text, prayer) in enumerate(stories):
        # Story title page (illustration placeholder)
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 612, gray=0.93)
        pdf.add_filled_rect(40, 40, 532, 532, gray=0.97)
        pdf.add_rect(40, 40, 532, 532, line_width=1, gray=0.4)
        
        # Story number and title
        pdf.add_centered_text(520, f"Story {story_idx + 1}", font='F1', size=10, gray=0.4)
        pdf.add_centered_text(480, story_title, font='F2', size=20, gray=0.12)
        pdf.add_centered_text(445, scripture_ref, font='F4', size=10, gray=0.4)
        
        # Illustration area indicator
        pdf.add_filled_rect(100, 180, 412, 240, gray=0.88)
        pdf.add_rect(100, 180, 412, 240, line_width=0.5, gray=0.5)
        pdf.add_centered_text(310, "[Beautiful Illustration Here]", font='F1', size=12, gray=0.4)
        pdf.add_centered_text(285, "Full-color watercolor artwork", font='F1', size=9, gray=0.5)
        
        # Small decorative stars
        pdf.add_text(60, 100, "*", font='F2', size=14, gray=0.3)
        pdf.add_text(530, 120, "*", font='F2', size=10, gray=0.35)
        
        # Story text page
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 612, gray=0.97)
        pdf.add_rect(50, 50, 512, 512, line_width=0.5, gray=0.6)
        
        # Story text (large font for read-aloud)
        paragraphs = story_text.split('|')
        y = 530
        for para in paragraphs:
            words = para.strip().split()
            line = ""
            for word in words:
                test = line + " " + word if line else word
                if len(test) * 7.5 > 440:
                    pdf.add_centered_text(y, line, font='F4', size=14, gray=0.12)
                    y -= 24
                    line = word
                else:
                    line = test
            if line:
                pdf.add_centered_text(y, line, font='F4', size=14, gray=0.12)
                y -= 24
            y -= 12
        
        # Prayer section
        y -= 20
        if y > 120:
            pdf.add_line(180, y, 432, y, width=0.5, gray=0.4)
            y -= 25
            pdf.add_centered_text(y, "Goodnight Prayer:", font='F2', size=12, gray=0.2)
            y -= 25
            # Prayer text
            prayer_words = prayer.split()
            line = ""
            for word in prayer_words:
                test = line + " " + word if line else word
                if len(test) * 6.5 > 400:
                    pdf.add_centered_text(y, line, font='F4', size=12, gray=0.2)
                    y -= 20
                    line = word
                else:
                    line = test
            if line:
                pdf.add_centered_text(y, line, font='F4', size=12, gray=0.2)
                y -= 20
            pdf.add_centered_text(y - 10, "Amen.", font='F5', size=12, gray=0.2)
    
    # ===== BONUS PAGE =====
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 612, gray=0.93)
    pdf.add_centered_text(520, "My Favorite Stories", font='F2', size=18, gray=0.15)
    pdf.add_centered_text(485, "Circle or color the stars next to the stories you love most!", font='F1', size=10, gray=0.3)
    y = 450
    for i, (story_title, _, _, _) in enumerate(stories[:15]):
        pdf.add_text(80, y, "*", font='F2', size=14, gray=0.4)
        pdf.add_text(105, y, story_title, font='F1', size=10, gray=0.2)
        y -= 24
    
    # ===== PARENT PRAYER PAGE =====
    pdf.new_page()
    pdf.add_filled_rect(0, 300, 612, 312, gray=0.12)
    pdf.add_centered_text(560, "A Prayer for My Little One", font='F2', size=18, gray=0.95)
    pdf.add_centered_text(515, "For the parent reading this book tonight:", font='F4', size=11, gray=0.8)
    parent_prayer = [
        "Lord, bless this precious child You have given me.",
        "Guard their sleep tonight and fill their dreams with peace.",
        "Plant seeds of faith deep in their little heart.",
        "Help me be the parent You have called me to be.",
        "May they grow to know You, love You, and serve You",
        "all the days of their life.",
        "Thank You for the gift of this moment together.",
        "In Jesus' name, Amen.",
    ]
    y = 460
    for line in parent_prayer:
        pdf.add_centered_text(y, line, font='F4', size=12, gray=0.85)
        y -= 24
    
    # ===== ABOUT AUTHOR =====
    pdf.new_page()
    pdf.add_centered_text(520, "About the Author", font='F2', size=16, gray=0.15)
    pdf.add_line(200, 508, 412, 508, width=0.5, gray=0.3)
    about = [
        f"{AUTHOR} is a Christian children's author passionate",
        "about planting seeds of faith in tiny hearts.",
        "",
        f"Through her {SERIES}, Selam creates",
        "gentle, beautifully illustrated Scripture stories",
        "that make bedtime the most meaningful moment of",
        "the day for Christian families.",
        "",
        "Her books are trusted by thousands of parents,",
        "grandparents, and churches as the perfect first",
        "introduction to God's love.",
        "",
        "Find more books in this series on Amazon!",
        "Search: Selam Fesehaye Little Blessings",
    ]
    y = 470
    for line in about:
        pdf.add_centered_text(y, line, font='F1', size=11, gray=0.2)
        y -= 20
    
    # ===== ALSO BY AUTHOR =====
    pdf.new_page()
    pdf.add_centered_text(550, "Also in This Series:", font='F2', size=14, gray=0.15)
    pdf.add_line(180, 538, 432, 538, width=0.5, gray=0.3)
    other_books = [
        "Bible Bedtime Stories for Toddlers (Vol 1 & 2)",
        "Bible Bedtime Prayers for Little Ones",
        "Bible ABCs: A Scripture Alphabet",
        "Bible Bedtime Stories for Preschoolers",
        "My First Bible Verses: 30 Scriptures",
        "Brave Bible Kids: Stories of Courage",
        "Bible Bedtime Lullabies",
        "God Made Me Special: Who I Am",
    ]
    y = 500
    for book in other_books:
        pdf.add_text(120, y, f"* {book}", font='F1', size=10, gray=0.25)
        y -= 28
    pdf.add_centered_text(y - 20, "Available on Amazon - Search 'Selam Fesehaye'", font='F2', size=10, gray=0.3)
    
    # SAVE
    output = f"/projects/sandbox/CLAUDE/kdp_books/Book{book_num}_{filename}.pdf"
    pdf.save(output)
    fsize = os.path.getsize(output)
    with open(output, 'rb') as f:
        pcount = f.read().count(b'/Type /Page')
    print(f"  Book {book_num}: {title.replace(chr(10),' ')[:45]:<47} | {pcount:>3} pg | {fsize:,} bytes")
    return output, pcount


# ============================================================
# BOOK 1: Bible Bedtime Stories for Toddlers (30 stories)
# ============================================================
def book_426():
    stories = [
        # (title, scripture_ref, story_text, prayer)
        ("God Made the World", "Genesis 1",
         "In the very beginning, God made everything.|He made the bright sun and the silver moon.|He made the tall trees and tiny flowers.|He made the birds that sing and the fish that swim.|He made fluffy clouds and sparkly stars.|God looked at everything He made and smiled.|It was all so good!|And then God rested.",
         "Thank You, God, for making such a beautiful world for me. Help me see Your love in the sunshine, the stars, and all the pretty things You made. Goodnight, God."),
        
        ("God Made You Special", "Psalm 139:14",
         "Before you were born, God already knew you.|He knew your little nose and your tiny toes.|He knew the color of your eyes.|He counted every hair on your head.|God made you just the way you are.|You are not too big or too small.|You are not too loud or too quiet.|You are wonderfully made by God.|And He loves you so very much.",
         "Dear God, thank You for making me just the way I am. Help me remember that I am special because You made me. I love You, God. Goodnight."),
        
        ("Adam and Eve's Garden", "Genesis 2:8",
         "God made a beautiful garden called Eden.|It had green grass and pretty flowers.|Animals played together happily.|There were yummy fruits on the trees.|God gave this garden to Adam and Eve.|It was their home, and it was perfect.|God walked with them in the cool of the day.|He loved spending time with them.",
         "God, thank You for making beautiful places. Thank You for spending time with me too. Help me enjoy Your world. Sweet dreams tonight."),
        
        ("Noah and the Rainbow", "Genesis 9:13",
         "Noah loved God very much.|God told Noah to build a big boat.|Noah obeyed, even when it was hard.|The animals came two by two.|Then the rain fell down, down, down.|But Noah and the animals were safe inside.|When the rain stopped, God painted a rainbow.|It was His promise: I will always love you.",
         "Thank You, God, for Your promises. Thank You for keeping me safe, just like You kept Noah safe. I trust You. Goodnight, God."),
        
        ("God Counts the Stars", "Psalm 147:4",
         "Look up at the sky tonight.|Can you see the stars twinkling?|There are so many, you cannot count them all.|But God can! He knows every single star.|He even gave each one a name.|If God cares about every little star,|imagine how much He cares about you!|You are more special to God than all the stars.",
         "Dear God, You know every star by name, and You know my name too. Thank You for loving me more than all the stars. Goodnight, twinkly stars. Goodnight, God."),
        
        ("The Animals Go Two by Two", "Genesis 7:9",
         "God told Noah the animals were coming.|Two big elephants stomped up the ramp.|Two tall giraffes bent their long necks.|Two fluffy sheep said baa-baa.|Two little mice scurried quickly.|Two colorful birds flew right in.|Two bouncy rabbits hopped aboard.|Everyone had a partner. Everyone was safe.|God took care of every single one.",
         "God, You take care of all the animals, and You take care of me too. Thank You for keeping me safe tonight. I love You."),
        
        ("Baby Moses in the Basket", "Exodus 2:3",
         "A mama put her baby in a little basket.|She placed it gently in the river.|The basket floated softly on the water.|Baby Moses slept peacefully inside.|God was watching over that tiny baby.|A kind princess found him and smiled.|She picked him up and loved him.|God kept baby Moses safe, just like He keeps you safe.",
         "Dear God, You watched over baby Moses, and You watch over me too. Keep me safe while I sleep tonight. Thank You for loving me."),
        
        ("God Feeds Elijah", "1 Kings 17:6",
         "Elijah was hungry and tired.|He did not know where his food would come from.|But God had a plan!|Every morning, birds brought him bread.|Every evening, birds brought him meat.|God sent the birds to feed His friend.|Elijah never went hungry.|God always provides what we need.",
         "Thank You, God, for giving me food to eat and a warm bed to sleep in. You always take care of me. I am never alone. Goodnight."),
        
        ("Daniel and the Friendly Lions", "Daniel 6:22",
         "Daniel loved to pray to God every day.|Some mean people put Daniel in a den of lions.|The lions had big teeth and sharp claws.|But Daniel was not afraid.|He knew God was with him.|God sent an angel to close the lions' mouths.|The lions became gentle and quiet.|Daniel was safe all night long!",
         "God, You kept Daniel safe with the lions. Please keep me safe tonight too. I know You are always with me. Thank You. Goodnight."),
        
        ("David the Brave Shepherd Boy", "1 Samuel 17:37",
         "David was just a young boy.|He took care of his father's sheep.|He played his harp and sang songs to God.|One day, a big giant came to scare everyone.|But David was not afraid.|He knew God was bigger than any giant.|With just a small stone and big faith,|David showed everyone that God is strong.",
         "Dear God, help me be brave like David. When things feel scary, remind me that You are bigger and stronger. I trust You tonight."),
        
        ("The Lord Is My Shepherd", "Psalm 23:1",
         "The Lord is my shepherd.|He gives me everything I need.|He lets me rest in soft green grass.|He leads me beside quiet, still waters.|He makes me feel calm and peaceful.|Even when it is dark, I am not afraid.|Because God is right there with me.|His love and goodness follow me every day.",
         "Lord, You are my shepherd. Thank You for quiet places, still waters, and peaceful sleep. Be with me through the night. I love You."),
        
        ("Jonah's Big Fish Adventure", "Jonah 2:10",
         "God asked Jonah to do something important.|But Jonah said no and ran away!|He jumped on a boat going far away.|A big storm came, and splash — Jonah fell in the sea!|A huge fish swallowed him up.|Inside the fish, Jonah prayed: I am sorry, God!|God heard him. The fish spit Jonah onto the beach.|God never gave up on Jonah, and He never gives up on you.",
         "God, thank You for never giving up on me. Even when I make mistakes, You still love me. Help me always listen to You. Goodnight."),
        
        ("Kind Ruth", "Ruth 1:16",
         "Ruth loved her mother-in-law Naomi very much.|When Naomi was sad, Ruth stayed with her.|Where you go, I will go, Ruth said.|Ruth was kind and helpful every day.|She worked hard to find food for them both.|God saw Ruth's kindness and blessed her.|He gave her a new family and a happy home.|Being kind makes God smile.",
         "Dear God, help me be kind like Ruth. Help me love my family and take care of the people around me. Thank You for kindness. Goodnight."),
        
        ("Samuel Hears God's Voice", "1 Samuel 3:10",
         "Little Samuel lived in God's house.|One night, he heard someone call his name.|Samuel! Samuel!|He thought it was his teacher Eli.|But it was God speaking!|Samuel said: Speak, Lord. I am listening.|God had an important message for Samuel.|God speaks to little children too — even you!",
         "God, help me listen for Your voice. Speak to my heart even while I sleep. I want to hear You like Samuel did. Goodnight, God."),
        
        ("Miriam's Song", "Exodus 15:20",
         "God did something amazing for His people.|He rescued them from the mean king.|He opened the sea so they could walk through!|When they were safe on the other side,|Miriam was so happy she picked up a tambourine.|She danced and sang a song of thanks.|Thank You, God! You saved us!|We can sing to God when we are happy too.",
         "God, You do amazing things! I want to sing and be happy like Miriam. Thank You for all the good things You do. Goodnight with a song in my heart."),
        
        ("Joseph's Colorful Coat", "Genesis 37:3",
         "Joseph's daddy gave him a beautiful coat.|It had every color of the rainbow!|Red and orange, yellow and green,|blue, purple, and more!|Joseph's brothers were not very nice to him.|They were jealous and mean.|But God had a special plan for Joseph.|Even when things are hard, God is working on something good.",
         "Dear God, even when things feel hard or unfair, help me trust that You have a good plan. Thank You for loving me always. Sweet dreams."),
        
        ("Abraham Counts the Stars", "Genesis 15:5",
         "God took Abraham outside on a clear night.|Look up at the sky, God said.|Count the stars if you can!|Abraham looked up — so many stars!|God said: I will bless you with a big family,|as many as the stars!|Abraham believed God's promise.|And God kept every single promise He made.",
         "God, Your promises are true — every single one. Thank You for the stars that remind me of Your faithfulness. Goodnight under Your starry sky."),
        
        ("Esther the Brave Queen", "Esther 4:14",
         "Esther was a young woman who became a queen!|Her people were in trouble and needed help.|Esther was scared, but she knew God was with her.|She prayed and asked for courage.|Then she went to the king to ask for help.|God gave her bravery, and she saved her people!|God can make you brave too,|even when you feel small and scared.",
         "God, thank You for making Esther brave. Please give me courage too. Help me know that You are always with me. I can be brave because of You. Goodnight."),
        
        ("Baby Jesus Is Born", "Luke 2:7",
         "On a quiet, starry night,|baby Jesus was born in a stable.|His mama Mary wrapped Him in soft cloth.|She laid Him in a manger filled with hay.|The animals watched quietly.|A bright star shone above.|Angels sang in the sky: Glory to God!|Baby Jesus came because God loves the whole world — including you.",
         "Thank You, God, for sending baby Jesus. Thank You for loving me so much. As I close my eyes tonight, I remember that You sent the best gift ever. Goodnight."),
        
        ("The Shepherds Visit", "Luke 2:15",
         "Shepherds were watching their sheep in the dark.|Suddenly, an angel appeared — so bright!|Do not be afraid! the angel said.|A special baby has been born tonight!|The shepherds ran to find baby Jesus.|They found Him in the manger, just like the angel said.|They were so happy, they told everyone!|Good news makes hearts glad.",
         "Dear God, thank You for the good news that Jesus came for me. Fill my heart with joy like the shepherds had. Goodnight with good news in my heart."),
        
        ("Jesus Blesses the Children", "Mark 10:14",
         "One day, mamas and daddies brought their children to Jesus.|Some grown-ups said: Go away! He is too busy!|But Jesus said: No! Let the children come to me!|He picked them up and held them close.|He smiled at them and blessed each one.|Jesus loves little children so much.|He loves YOU so much.|You are never too small for Jesus.",
         "Jesus, thank You for loving children — for loving ME. I am never too small for You. Hold me close tonight as I fall asleep. I love You."),
        
        ("Jesus Calms the Storm", "Mark 4:39",
         "Jesus was sleeping in a boat.|A big storm came — wind, waves, splash!|His friends were so scared!|Jesus! Help us! they cried.|Jesus stood up and said: Peace. Be still.|The wind stopped. The waves became calm.|Everything was quiet and peaceful.|When you feel scared, Jesus can bring peace to your heart too.",
         "Jesus, when I feel scared, please calm my heart like You calmed the storm. Bring me peace tonight. Be still, worries. Be still, fears. Goodnight."),
        
        ("The Good Shepherd", "John 10:14",
         "Jesus said: I am the Good Shepherd.|A good shepherd knows every sheep by name.|He leads them to green grass and cool water.|If one sheep gets lost, he searches until he finds it.|He carries it home on his shoulders, so happy!|Jesus is your Good Shepherd.|He knows YOUR name.|He will never, ever lose you.",
         "Jesus, You are my Good Shepherd. You know my name and You will never lose me. Thank You for always finding me. Goodnight, my Shepherd."),
        
        ("Jesus Feeds 5,000", "John 6:11",
         "A huge crowd of people was hungry.|A little boy had five small loaves and two fish.|That is not very much food!|But the boy gave it to Jesus.|Jesus thanked God and broke the bread.|And suddenly — there was food for everyone!|5,000 people ate until they were full!|When you share what you have, God makes it enough.",
         "God, help me share like that little boy. Even small things become big when I give them to You. Thank You for always being enough. Goodnight."),
        
        ("The Good Samaritan", "Luke 10:33",
         "A man was hurt and lying on the road.|Some people walked past and did not help.|But one kind man stopped.|He bandaged the man's boo-boos.|He gave him water and took him somewhere safe.|Jesus told this story to teach us:|Be kind to everyone — even people who are different from you.|Kindness is always the right thing to do.",
         "Jesus, help me be kind like the good Samaritan. Help me see people who need help and be brave enough to help them. Goodnight with a kind heart."),
        
        ("The Lost Sheep", "Luke 15:6",
         "A shepherd had 100 sheep.|But one little sheep wandered away!|The shepherd left the 99 safe sheep|and went searching for the one who was lost.|He looked and looked until he found it!|He carried it home and was SO happy!|That is how God feels about you.|He will always come looking for you.",
         "God, thank You for always coming to find me. I am never lost to You. You love me that much. I feel so safe tonight. Goodnight."),
        
        ("Love One Another", "John 13:34",
         "Jesus gave His friends one important rule:|Love one another, He said.|Love each other the way I love you.|What does love look like?|Love is being kind. Love is sharing.|Love is saying sorry. Love is forgiving.|Love is hugging. Love is helping.|When we love others, we make Jesus smile.",
         "Jesus, fill my heart with love. Help me love my family, my friends, and everyone I meet. Thank You for loving me first. Goodnight with love."),
        
        ("Be Still and Know", "Psalm 46:10",
         "Sometimes the world is very noisy.|Cars honk. Dogs bark. People talk.|But God says: Be still.|That means: stop, breathe, and be quiet.|In the stillness, you can feel God near.|He whispers: I am here. I love you.|You do not need to be busy or loud.|Just be still — and know that God is God.",
         "God, help me be still right now. I breathe in Your peace. I breathe out my worries. You are here with me. I am still. I am safe. Goodnight."),
        
        ("God Watches Over You", "Psalm 121:3-4",
         "Did you know God never sleeps?|When you close your eyes at night,|God's eyes stay wide open.|He watches over you all night long.|He will not let your foot slip.|He guards you like a loving father.|The moon and stars are His nightlights.|You can sleep peacefully because God is awake.",
         "God, thank You for watching over me tonight. You never sleep, so I can sleep safely. Guard my dreams and keep me until morning. Goodnight."),
        
        ("Goodnight, God Loves You", "Zephaniah 3:17",
         "It is time to close your sleepy eyes.|But first, remember this:|God is with you right now.|He is happy because of you.|He loves you with a quiet, gentle love.|He even sings over you!|Can you hear it? A soft, sweet lullaby.|God is singing you to sleep tonight.|Goodnight, little one. God loves you so.",
         "Dear God, sing over me tonight. Wrap me in Your love like a warm blanket. I am safe. I am loved. I am Yours. Goodnight, God. I love You too."),
    ]
    return create_childrens_book(426, "Selam_Bible_Bedtime_Toddlers",
        "Bible Bedtime Stories\nfor Toddlers", "30 Calming Scripture Tales with Gentle Prayers for Little Ones Ages 1-3",
        "1-3", stories)




# ============================================================
# BOOKS 2-8: Quick generation using template
# ============================================================

def book_427():
    """Bible Bedtime Prayers for Little Ones"""
    stories = [
        ("A Prayer for Morning", "Psalm 118:24", "God, thank You for this brand new day!|The sun is shining and the birds are singing.|Help me be kind and happy today.|Help me share and play nicely.|Thank You for my family who loves me.|Thank You for food and a warm home.|I know You will be with me all day long.|Today is a gift from You!", "Dear God, thank You for today. Walk with me, hold my hand, and help me shine Your light. I love You. Goodnight."),
        ("A Prayer for Nighttime", "Psalm 4:8", "The day is done, the stars are out.|It is time to rest my sleepy head.|God, thank You for everything today.|Thank You for playtime and snack time.|Thank You for hugs and bedtime stories.|Now I close my eyes and rest.|I know You are watching over me.|Goodnight, world. Goodnight, God.", "Lord, as I close my eyes, fill my dreams with peace. Keep me safe until the morning light. I trust You. Goodnight."),
        ("A Prayer for My Family", "Psalm 128:1", "God, thank You for my family.|Thank You for Mama and Daddy.|Thank You for brothers and sisters.|Thank You for grandmas and grandpas.|Bless each one of them tonight.|Keep them safe and full of love.|Help us be kind to each other.|We are a family, and You love us all.", "Dear God, wrap my whole family in Your love tonight. Keep us close to each other and close to You. Bless our home. Goodnight."),
        ("A Prayer When I'm Scared", "Isaiah 41:10", "God, sometimes I feel scared.|The dark feels big and I feel small.|But You said: Do not be afraid.|You are with me in the dark.|You are bigger than any shadow.|You are stronger than any noise.|With You beside me, I can be brave.|I am not alone — You are here.", "God, take away my fears tonight. You are my protector. You are my light in the darkness. I am safe because You are near. Goodnight."),
        ("A Prayer for My Friends", "Proverbs 17:17", "God, thank You for my friends!|Thank You for playing together.|Thank You for sharing and laughing.|Help me be a good friend tomorrow.|Help me share my toys and take turns.|Help me say kind words.|If my friend is sad, help me help them.|Friends are a gift from You.", "Dear God, bless all my friends tonight. Keep them safe and happy. Help me be the best friend I can be. Thank You for friendship. Goodnight."),
        ("A Prayer for Courage", "Joshua 1:9", "God, sometimes things feel scary.|New places, new people, new things.|But You tell me to be strong and brave.|You promise to be with me everywhere I go.|At school, at the store, at the park —|You are always right beside me.|I can do hard things with Your help.|You make me brave!", "Lord, fill me with courage for tomorrow. Whatever comes, I know You are with me. I am strong because You are strong. Goodnight, brave heart."),
        ("A Prayer of Thanks", "1 Thessalonians 5:18", "Thank You, God, for everything!|For sunshine and for rain.|For ice cream and for vegetables.|For puppies and for butterflies.|For books and for songs.|For warm blankets and soft pillows.|For people who love me.|My heart is full of thank-You's!", "God, my heart overflows with gratitude. Thank You for a million blessings — big ones and tiny ones. I go to sleep thankful tonight. Goodnight."),
        ("A Prayer for Forgiveness", "1 John 1:9", "God, today I made some mistakes.|I was not always kind or patient.|Sometimes I said things I should not say.|Sometimes I did not listen or obey.|But You still love me — mistakes and all!|When I say sorry, You always forgive me.|You never hold it against me.|Tomorrow is a fresh new start.", "Dear God, I am sorry for the wrong things I did today. Thank You for forgiving me completely. Help me do better tomorrow. Your love never runs out. Goodnight."),
        ("A Prayer for Sweet Dreams", "Proverbs 3:24", "It is time to close my eyes.|God, please give me happy dreams.|Dreams of playing in green meadows.|Dreams of flying with the birds.|Dreams of laughing with my friends.|Dreams of being held by You.|Let my sleep be deep and peaceful.|Guard my mind through the night.", "Lord, be the guardian of my dreams tonight. Fill my sleep with joy and peace. Let me wake up refreshed and full of Your love. Sweet dreams. Goodnight."),
        ("A Prayer for Tomorrow", "Jeremiah 29:11", "God, I do not know what tomorrow holds.|But You do! You know every day of my life.|You have good plans for me.|Plans to help me and not hurt me.|Plans full of hope and a future.|So I do not need to worry.|I can rest tonight knowing|tomorrow is already in Your hands.", "God, I give You tomorrow. Whatever it holds, I trust You. Your plans for me are good. I will sleep in peace. Goodnight."),
        ("A Prayer for Helpers", "Psalm 121:2", "God, thank You for all my helpers!|Thank You for doctors who make me feel better.|Thank You for teachers who help me learn.|Thank You for firefighters and police.|Thank You for grandparents and neighbors.|You put helpers all around me.|I am never alone.|You send people to love me.", "Dear God, bless all the people who take care of me. Keep them safe tonight too. Thank You for sending helpers into my life. Goodnight."),
        ("A Prayer for Animals", "Genesis 1:25", "God, You made so many animals!|Big elephants and tiny ladybugs.|Fast cheetahs and slow turtles.|Loud lions and quiet rabbits.|Thank You for making them all!|Help me be gentle with animals.|Help me take care of Your creation.|Every creature is special to You.", "God, bless all the animals tonight — the ones in my house and the ones far away. Thank You for making so many wonderful creatures. Goodnight."),
        ("A Prayer for Sharing", "Acts 20:35", "God, help me share with others.|Sharing toys, sharing food, sharing smiles.|It is not always easy to share.|Sometimes I want to keep things for myself.|But You said it is better to give.|When I share, I make others happy.|And that makes my heart happy too!|Help me be generous like You.", "Lord, give me a generous heart. Help me share my blessings with everyone around me. When I give, I become more like You. Goodnight."),
        ("A Prayer for Patience", "James 1:4", "God, waiting is SO hard!|Waiting for my turn. Waiting for dinner.|Waiting for tomorrow. Waiting to grow up.|But You say patience is good.|It makes me strong inside.|Help me wait without whining.|Help me be calm when things are slow.|Good things are worth waiting for.", "Dear God, teach me patience. When I want to rush, help me slow down. When I want to fuss, help me breathe. Patience makes me more like You. Goodnight."),
        ("A Prayer for Kindness", "Ephesians 4:32", "God, help me be kind today.|Kind words, kind hands, kind heart.|Help me say please and thank you.|Help me smile at people.|Help me help someone who is struggling.|Kindness is like a warm hug for the world.|When I am kind, I spread Your love.|Make me a kindness superhero!", "Lord, fill me up with so much kindness that it spills over onto everyone I meet. Let my words be sweet and my actions be gentle. Goodnight, kind heart."),
        ("A Prayer for When I'm Sad", "Psalm 34:18", "God, today my heart feels heavy.|Sometimes things make me sad.|But You said You are close to the brokenhearted.|You collect every tear.|You hold me when I cry.|It is okay to feel sad sometimes.|You understand. You care.|And You promise joy will come in the morning.", "God, hold my sad heart tonight. You are close to me, even when I cry. Thank You for caring about my feelings. Tomorrow will be better. Goodnight."),
        ("A Prayer for Obedience", "Colossians 3:20", "God, help me obey my parents.|When they say stop, help me stop.|When they say come, help me come.|When they say share, help me share.|Obeying is not always fun.|But it keeps me safe and makes You happy.|My parents love me — that is why they have rules.|Help me listen and obey.", "Dear God, give me a heart that wants to obey. Help me listen to my parents and trust that their rules are for my good. I want to make You proud. Goodnight."),
        ("A Prayer for Peace", "John 14:27", "Jesus said: Peace I leave with you.|Peace means feeling calm inside.|No worries. No fears. No racing thoughts.|Just quiet, gentle peace.|Like a still lake on a calm day.|Like a baby sleeping in mama's arms.|Jesus gives me peace tonight.|Everything is going to be okay.", "Jesus, pour Your peace over me like warm water. Calm every worry, every fear, every anxious thought. I rest in Your peace tonight. Goodnight."),
        ("A Prayer for God's Love", "Romans 8:39", "Nothing can take God's love away from me!|Not monsters under my bed. Not bad days.|Not mistakes I make. Not anything!|God's love is bigger than the ocean.|Higher than the mountains.|Deeper than the deepest sea.|It wraps around me like a warm blanket.|I am loved. I am loved. I am loved.", "God, Your love is unstoppable and unbreakable. Nothing in the whole world can separate me from it. I fall asleep wrapped in Your love. Goodnight."),
        ("A Prayer for the World", "John 3:16", "God, You love the whole world!|Every person in every country.|Kids who look like me and kids who look different.|People who are happy and people who are sad.|God, please help everyone tonight.|Give food to those who are hungry.|Give homes to those who have none.|Your love is big enough for everyone.", "Dear God, bless the whole world tonight. Help people who are hurting. Send Your love to every corner of the earth. You love us all. Goodnight."),
        ("A Prayer for Healing", "Psalm 103:3", "God, please heal the boo-boos.|The ones we can see — scrapes and bumps.|And the ones we cannot see — sad hearts and worries.|You are the Great Doctor.|You can fix anything.|Thank You for medicine and bandaids.|Thank You for hugs that help us feel better.|You heal us with Your love.", "Lord, if anyone in my family is hurting tonight, please bring healing. You are the healer. Touch us with Your gentle hands. Goodnight."),
        ("A Prayer Before Church", "Psalm 122:1", "Tomorrow we go to God's house!|I am glad! I love church!|Singing songs and learning about God.|Being with friends who love Jesus.|Hearing stories from the Bible.|Giving offerings and saying prayers.|Church is where we worship together.|It makes God's heart so happy.", "God, thank You for church and for people who love You. Help me pay attention and learn more about You. I am excited! Goodnight."),
        ("A Prayer for Rainy Days", "Isaiah 55:10", "God, sometimes it rains and rains.|The sky is gray and we stay inside.|But rain is not bad — it helps things grow!|Flowers need rain. Trees need rain.|Gardens need rain to give us food.|God sends rain as a gift.|Even gray days have blessings.|Sunshine always comes back.", "God, thank You for rainy days and sunny days. Both are gifts from You. Help me find joy in every kind of day. Goodnight."),
        ("A Prayer for My Pets", "Proverbs 12:10", "God, thank You for my pet!|Thank You for furry cuddles and wagging tails.|Thank You for soft purrs and happy chirps.|Help me take good care of my animal friend.|Give them food and water and love.|Animals are a gift from You.|They make my heart so happy!|Bless my pet tonight.", "Dear God, watch over my pet tonight. Keep them warm and safe. Thank You for the joy they bring to my life. We are both loved by You. Goodnight."),
        ("A Prayer for New Things", "Isaiah 43:19", "God, new things can feel scary.|A new house. A new school. A new baby.|New things mean everything is different.|But You said: Behold, I do new things!|You are the God of new beginnings.|You go before me into every new place.|I do not have to be afraid.|New can be wonderful!", "God, if something new is coming, help me be excited instead of afraid. You are already there, making it good. I trust You with new things. Goodnight."),
        ("A Prayer for Being Quiet", "Psalm 46:10", "Sometimes being quiet is the best thing.|Shh. Listen. What do you hear?|Maybe the wind. Maybe crickets.|Maybe your own heartbeat.|In the quiet, God speaks.|Not with a loud voice — with a gentle whisper.|Be still, little one.|God is here in the quiet.", "God, I am quiet now. I am still. I am listening for Your gentle voice. Whisper Your love to my heart. I am here. Goodnight."),
        ("A Prayer of Praise", "Psalm 150:6", "Everything that has breath — praise God!|Clap your hands! Stomp your feet!|Sing a loud song! Whisper a prayer!|God deserves all our praise.|For the sun and the moon and the stars.|For food and family and fun.|For love and laughter and life.|Praise You, God! You are amazing!", "God, I praise You tonight! You are wonderful, powerful, and so full of love. I clap for You in my heart. I sing for You in my soul. Goodnight with praise."),
        ("A Prayer for Sleepy Eyes", "Psalm 3:5", "My eyes are getting heavy.|My body is getting still.|It is time to rest, to stop, to sleep.|God, thank You for this cozy bed.|Thank You for my soft pillow.|Thank You for blankets that keep me warm.|I will lie down and sleep in peace.|Because You, Lord, keep me safe.", "Lord, my sleepy eyes are closing now. Thank You for rest. Thank You for peace. Thank You for this day. I will sleep and wake because of You. Goodnight."),
        ("A Prayer for Mama and Daddy", "Exodus 20:12", "God, please bless my mama and daddy.|They work so hard to take care of me.|They feed me, clothe me, and love me.|They read me stories and tuck me in.|They kiss my boo-boos and wipe my tears.|Help me honor them and make them happy.|They are such a gift from You.|I love them so much.", "God, bless Mama and Daddy tonight. Give them rest, give them strength, give them joy. Thank You for parents who love me like You do. Goodnight."),
        ("A Prayer for God's Protection", "Psalm 91:11", "God, You send angels to watch over me!|They are around me right now.|I cannot see them, but they are there.|Guarding me. Protecting me.|Nothing can get past God's angels.|No bad dreams. No scary sounds.|Only peace and safety tonight.|God's angels are on duty.", "Lord, thank You for sending Your angels to protect me. I am surrounded by Your heavenly guard. I sleep without fear tonight. Goodnight, safe and sound."),
        ("A Goodnight Blessing", "Numbers 6:24-26", "The Lord bless you and keep you.|The Lord make His face shine on you.|The Lord be gracious to you.|The Lord turn His face toward you.|And give you peace.|This is God's blessing over your life.|Every single night.|You are blessed, little one. So very blessed.", "God, I receive Your blessing tonight. Shine Your face on me. Be gracious to me. Give me peace. I am blessed. I am loved. I am Yours. Goodnight forever and always."),
    ]
    return create_childrens_book(427, "Selam_Bible_Bedtime_Prayers",
        "Bible Bedtime Prayers\nfor Little Ones", "30 Gentle Prayers & Scripture for Sweet Dreams",
        "1-4", stories)

def book_428():
    """Bible ABCs: A Scripture Alphabet for Toddlers"""
    stories = [
        ("A is for Adam", "Genesis 2:7", "A is for Adam, the very first man.|God made him from dust with His own hands.|He lived in a garden full of delight.|God gave him a helper — everything was right!", "Dear God, thank You for making people. You made Adam and You made me. Thank You! Goodnight."),
        ("B is for Bethlehem", "Luke 2:4", "B is for Bethlehem, a little town.|Where baby Jesus wore no crown.|Born in a stable, small and sweet.|With tiny hands and tiny feet!", "Jesus, You came to a tiny town for me. Thank You for being born so I could know You. Goodnight, little Bethlehem."),
        ("C is for Creation", "Genesis 1:1", "C is for Creation — God made it all!|Mountains so big and ants so small.|Oceans and forests and skies so blue.|He made the whole world, and He made you!", "Creator God, everything You made is wonderful — including me! Thank You for this beautiful world. Goodnight."),
        ("D is for David", "1 Samuel 16:7", "D is for David, a shepherd so small.|God chose him — the youngest of all!|He fought a giant with faith so strong.|With God beside him, nothing went wrong!", "God, if You can use David, You can use me too. I may be small, but You make me strong. Goodnight."),
        ("E is for Esther", "Esther 4:14", "E is for Esther, a queen so brave.|She trusted God and people she saved!|Though she was scared, she did what was right.|God gave her courage and shining light!", "God, make me brave like Esther. Even when I am afraid, help me do what is right. Goodnight."),
        ("F is for Faith", "Hebrews 11:1", "F is for Faith — believing what is true.|Even when you cannot see, God is there for you!|Faith is like a seed planted in your heart.|Trust God completely — that is where it starts!", "Lord, help my faith grow big and strong like a tall tree. I believe in You even though I cannot see You. Goodnight."),
        ("G is for God", "Psalm 46:1", "G is for God — the greatest of all!|He is always there when you call.|Bigger than mountains, gentler than rain.|God loves you over and over again!", "God, You are the greatest! Bigger than anything and gentler than everything. I love You most of all. Goodnight."),
        ("H is for Heaven", "John 14:2", "H is for Heaven, a beautiful place.|Where we will see God face to face!|Streets of gold and gates so bright.|No more tears and no more night!", "Dear God, thank You that heaven is real. One day I will see You there. But for now, be close to me tonight. Goodnight."),
        ("I is for Isaac", "Genesis 21:3", "I is for Isaac, a promised child.|His mama Sarah laughed and smiled!|God kept His promise — He always does.|Isaac was proof of how great God's love was!", "God, You always keep Your promises. Thank You for being trustworthy. I can count on You. Goodnight."),
        ("J is for Jesus", "John 3:16", "J is for Jesus, God's only Son.|He came to earth for everyone!|He loves the big and loves the small.|Jesus is the best gift of all!", "Jesus, You are the greatest gift ever given. Thank You for coming for me. I love You. Goodnight."),
        ("K is for Kindness", "Ephesians 4:32", "K is for Kindness — be gentle and sweet.|Kind to your friends and people you meet!|Sharing and caring and lending a hand.|Kindness makes the world more grand!", "God, fill me with kindness from my head to my toes. Help me spread it everywhere I go. Goodnight."),
        ("L is for Love", "1 John 4:8", "L is for Love — God IS love, you see!|He loves you and He loves me!|Love is patient, love is kind.|The greatest treasure you will find!", "God, You ARE love. Fill me with Your love so I can share it with everyone. Goodnight with love."),
        ("M is for Moses", "Exodus 3:4", "M is for Moses, whom God called by name.|From a burning bush — what a flame!|God said: Go set My people free!|Moses obeyed — and so can we!", "God, when You call me, help me answer like Moses did. I want to obey You. Goodnight."),
        ("N is for Noah", "Genesis 6:9", "N is for Noah who built a big boat.|In the flood it would float and float!|Two by two the animals came.|Noah trusted God just the same!", "God, help me trust You like Noah did, even when things seem impossible. Goodnight."),
        ("O is for Obey", "John 14:15", "O is for Obey — to follow God's way.|To listen and do what He has to say!|Obeying is love shown through what we do.|When we obey God, we grow closer too!", "Lord, help me obey with a happy heart. I want to follow Your way. Goodnight."),
        ("P is for Prayer", "Philippians 4:6", "P is for Prayer — talking to God!|You can pray anywhere — is that not odd?|In bed, in the car, at school, at play.|God hears every word that you say!", "God, thank You for always listening to me. I can talk to You anytime, anywhere. Hear my prayers tonight. Goodnight."),
        ("Q is for Quiet", "Psalm 46:10", "Q is for Quiet — be still and know.|God is near wherever you go.|In the quiet moments, listen well.|God has wonderful things to tell!", "God, in the quiet of this night, I listen for You. Speak peace to my heart. Goodnight."),
        ("R is for Ruth", "Ruth 1:16", "R is for Ruth, so faithful and true.|Where you go, I will go too!|She was kind and worked real hard.|God blessed her life — every single part!", "God, make me faithful like Ruth. Help me stick close to the people I love. Goodnight."),
        ("S is for Shepherd", "Psalm 23:1", "S is for Shepherd — that is Jesus' name!|He leads His sheep — they are never the same!|Beside still waters, through green grass.|With the Good Shepherd, peace will last!", "Jesus, my Shepherd, lead me to peaceful rest tonight. Goodnight."),
        ("T is for Trust", "Proverbs 3:5", "T is for Trust — with all of your heart!|Let God guide you right from the start!|You do not need to understand it all.|Just trust in God — He will not let you fall!", "God, I trust You with my whole heart tonight. Even what I do not understand, I give to You. Goodnight."),
        ("U is for Unity", "Psalm 133:1", "U is for Unity — together as one!|Brothers and sisters having fun!|Living in peace, side by side.|With God's love as our guide!", "God, help my family live in unity and love. Bring us close together and close to You. Goodnight."),
        ("V is for Vine", "John 15:5", "V is for Vine — Jesus said stay close!|Like a branch that grows the most.|Connected to Him, we bear good fruit.|Love, joy, and peace from the root!", "Jesus, help me stay connected to You like a branch to a vine. I need You. Goodnight."),
        ("W is for Wisdom", "Proverbs 2:6", "W is for Wisdom — it comes from God!|Ask Him for it — that is not odd!|Wisdom helps you know right from wrong.|With God's wisdom, you are strong!", "God, give me wisdom even while I sleep. Help me make good choices tomorrow. Goodnight."),
        ("X is for eXtra Love", "1 Corinthians 13:13", "X is for eXtra — God's love overflows!|More than the sand, more than the stars that glow!|You can never use up God's love supply.|It stretches from earth up to the sky!", "God, Your love is extra, overflowing, never-ending. Drown me in it tonight. Goodnight."),
        ("Y is for Yes", "2 Corinthians 1:20", "Y is for Yes — God's promises are true!|Every single one — for me and you!|When God says yes, it always will be.|His word is sure for all to see!", "God, Your yes is always yes. I believe Your promises tonight. Every one. Goodnight."),
        ("Z is for Zion", "Psalm 48:1", "Z is for Zion, God's holy hill!|A place of beauty, a place of thrill!|One day we will worship there.|In God's presence — beyond compare!", "God, I look forward to being with You one day in Your beautiful presence. Until then, be near me tonight. Goodnight."),
    ]
    return create_childrens_book(428, "Selam_Bible_ABCs",
        "Bible ABCs", "A Scripture Alphabet for Toddlers to Learn God's Word",
        "2-4", stories)




def book_429():
    """Bible Bedtime Stories for Preschoolers"""
    s = [
        ("The Creation Story", "Genesis 1:31", "Day one God made light — bright and warm!|Day two He made the sky so high.|Day three He made the land and seas.|Day four He hung the sun, moon, and stars.|Day five He filled the sea with fish and the sky with birds.|Day six He made animals AND people!|Day seven? God rested. It was ALL very good.", "Creator God, everything You made is amazing. Thank You for making ME on purpose. Goodnight."),
        ("Noah Builds the Ark", "Genesis 6:22", "God told Noah: Build a boat! A really BIG one!|People laughed at Noah. Why build a boat on dry land?|But Noah obeyed God anyway.|He hammered and sawed for years and years.|When the boat was done, God sent the animals.|Then the rain came — forty days and nights!|Noah's family was safe because Noah trusted God.", "God, help me obey You even when others laugh. You always know best. Goodnight."),
        ("Abraham's Big Move", "Genesis 12:1", "God told Abraham: Leave your home. Go where I tell you.|Abraham did not even know where he was going!|But he trusted God and packed his bags.|He took his wife Sarah and his nephew Lot.|They walked and walked to a brand new land.|God promised to bless Abraham with a big family.|Abraham believed — and God kept His word!", "God, help me trust You when I do not know what comes next. You always lead me to good places. Goodnight."),
        ("Joseph the Dreamer", "Genesis 37:19", "Joseph had special dreams from God!|His brothers were jealous and sold him away.|Joseph was far from home and lonely.|But God was with Joseph every single day.|Years later, Joseph became a ruler!|He helped feed hungry people — even his brothers!|God turned something bad into something beautiful.", "God, even when bad things happen, You can make something beautiful. I trust Your plan. Goodnight."),
        ("Moses and the Burning Bush", "Exodus 3:4", "Moses saw something strange — a bush on fire!|But the bush was not burning up!|God spoke from the bush: Moses! Moses!|I am sending you to set My people free.|Moses was scared. Who am I? he asked.|God said: I will be with you. That is enough.|And it was.", "God, You are always enough. When You call me to do something, You will help me do it. Goodnight."),
        ("Crossing the Red Sea", "Exodus 14:21", "The people were trapped! Water in front, army behind!|But God had a plan.|He told Moses to stretch his hand over the sea.|The water split in two — walls of water on each side!|The people walked across on DRY ground!|When the army followed, the water came back.|God saved His people in the most amazing way!", "God, You make a way where there seems to be no way. Nothing is impossible for You. Goodnight."),
        ("Joshua and the Walls", "Joshua 6:20", "God told Joshua to march around the city walls.|No fighting. No pushing. Just marching.|March once a day for six days.|On day seven — march seven times, then SHOUT!|The people obeyed. They marched and marched.|Then they shouted — and the walls fell DOWN!|God won the battle His way.", "God, Your ways are not my ways — but Your ways always work. Help me trust Your timing. Goodnight."),
        ("Gideon's Brave 300", "Judges 7:7", "God chose Gideon to save His people.|But instead of a big army, God gave him only 300 men!|That is not very many!|But God said: I want everyone to know that I am strong.|The 300 men blew trumpets and held torches.|The enemy ran away in confusion!|God does not need a big army — He just needs willing hearts.", "God, I may be small, but You are big. Use me for Your glory. I am willing. Goodnight."),
        ("Ruth's Faithfulness", "Ruth 2:12", "Ruth lost her husband and was very sad.|She could have gone back to her old home.|But she chose to stay with Naomi and follow God.|Ruth worked hard picking grain in the fields.|God noticed her faithfulness.|He gave her a new husband named Boaz!|And Ruth became part of Jesus' family tree!", "God, help me be faithful even in hard times. You see me and You reward faithfulness. Goodnight."),
        ("David and Goliath", "1 Samuel 17:45", "A giant named Goliath scared everyone!|He was over nine feet tall with huge armor!|But young David was not afraid.|He said: I come in the name of the Lord!|With one small stone and one big God,|David defeated the giant!|The bigger the problem, the bigger God can show off.", "God, no giant is too big for You. Help me face my giants with faith, not fear. Goodnight."),
        ("Solomon Asks for Wisdom", "1 Kings 3:9", "Solomon became king when he was young.|God said: Ask Me for anything you want!|Solomon could have asked for money or power.|But instead he said: Give me wisdom.|God was SO pleased!|He gave Solomon wisdom AND riches AND honor.|When we ask for the right things, God gives extra blessings.", "God, I do not ask for toys or treats — I ask for wisdom. Help me make good choices. Goodnight."),
        ("Elijah and the Ravens", "1 Kings 17:4", "Elijah was hungry and there was no food.|But God said: Go to the brook. I will feed you.|Every morning and evening, ravens brought bread and meat!|Birds delivering food! Only God could do that.|When everyone else forgot about Elijah,|God did not. He always provides.|Sometimes in the most surprising ways.", "God, You feed the birds and You feed me. Thank You for providing everything I need. Goodnight."),
        ("Daniel in the Lions' Den", "Daniel 6:22", "Daniel prayed three times every day.|Bad people made a law against praying.|But Daniel kept praying anyway!|They threw him into a den of hungry lions.|Daniel was not afraid — God was with him!|An angel shut the lions' mouths!|In the morning, Daniel was perfectly safe.", "God, I will keep talking to You no matter what. Thank You for protecting those who love You. Goodnight."),
        ("Jonah and the Big Fish", "Jonah 2:1", "God said: Go to Nineveh, Jonah!|But Jonah ran the OTHER way!|A storm came. Jonah fell into the sea.|A huge fish swallowed him whole!|Inside the fish, Jonah prayed: I am sorry, God!|Three days later, the fish spit him out.|Jonah finally obeyed. God gives second chances!", "God, thank You for second chances. When I run from You, bring me back. I want to obey. Goodnight."),
        ("Jesus Walks on Water", "Matthew 14:25", "The disciples were in a boat on a stormy sea.|They saw someone walking on the water!|It was Jesus!|Peter said: Lord, let me come to You!|He stepped out of the boat and walked on water too!|But when he looked at the waves, he sank.|Jesus caught him: Why did you doubt?|Keep your eyes on Jesus!", "Jesus, help me keep my eyes on You — not on the storms. When I start to sink, catch me. Goodnight."),
        ("The Prodigal Son", "Luke 15:20", "A son took his money and left home.|He spent everything on foolish things.|When the money was gone, he was alone and hungry.|He decided to go home and say sorry.|His father saw him coming from FAR away|and RAN to hug him!|That is how God feels when we come back to Him.", "God, no matter how far I wander, You are always waiting with open arms. Thank You for never giving up on me. Goodnight."),
        ("Jesus Feeds 5,000", "John 6:11", "A huge crowd was hungry.|A little boy had five loaves and two fish.|Not much for 5,000 people!|But he gave it to Jesus.|Jesus prayed, broke the bread, and shared.|Everyone ate until they were FULL!|There were even leftovers!|Small things become big in Jesus' hands.", "Jesus, I give You what I have — even if it seems small. Make it into something amazing. Goodnight."),
        ("Jesus Heals the Blind Man", "John 9:25", "A man had been blind since birth.|He had never seen colors or faces or sunsets.|Jesus made mud and put it on his eyes.|Go wash, Jesus said.|The man washed — and he could SEE!|For the first time ever, he saw the world!|Jesus opens blind eyes.|He helps us see what matters most.", "Jesus, open my eyes to see the beautiful things You are doing all around me. Goodnight."),
        ("Jesus Rises Again", "Matthew 28:6", "Jesus died on the cross for our sins.|His friends were so sad. They thought it was over.|They put Him in a tomb and sealed it shut.|But on the third day — the tomb was EMPTY!|Jesus was alive! He conquered death!|He is alive today — right now!|Because Jesus lives, we can live too!", "Jesus, You are alive! Death could not hold You. Thank You for giving me life that lasts forever. Goodnight, risen King."),
        ("Jesus Is Coming Back", "Revelation 21:4", "One day, Jesus is coming back!|He will make everything new and perfect.|No more tears. No more pain. No more sadness.|Only joy and love and peace forever.|We will see Him face to face!|We will live with Him always.|Until then, we wait with hope.|The best is yet to come!", "Jesus, I cannot wait to see You one day. Until then, I will live for You right here. The best IS yet to come. Goodnight."),
    ]
    return create_childrens_book(429, "Selam_Bible_Preschoolers",
        "Bible Bedtime Stories\nfor Preschoolers", "20 Scripture Adventures for Growing Hearts Ages 3-5",
        "3-5", s)




def book_430():
    """My First Bible Verses"""
    verses = [
        ("God Is Love", "1 John 4:8", "God IS love. Not just that He has love —|He IS love! Everything He does comes from love.|When you feel lonely, remember: Love is here.|When you feel scared, remember: Love is near.|God's love never runs out. Never gets tired.|Never goes away. Always always always.", "God, You ARE love. Let me feel Your love all around me tonight like a warm hug. Goodnight."),
        ("Be Strong and Brave", "Joshua 1:9", "Be strong and courageous!|Do not be afraid!|God is with you wherever you go.|At school, at the park, in the dark.|God does not leave. God does not hide.|He is right beside you.|You CAN be brave because God is with you.", "God, I am strong and brave because You are with me. No fear tonight. Only courage. Goodnight."),
        ("Trust God", "Proverbs 3:5", "Trust in the Lord with ALL your heart.|Not just a little bit — with ALL of it!|Do not try to figure everything out alone.|Let God lead the way.|He sees further than you can see.|He knows more than you can know.|Trust Him. He has never let anyone down.", "God, I trust You with my whole heart tonight. Lead me. Guide me. I will follow. Goodnight."),
        ("God's Plans", "Jeremiah 29:11", "God has plans for you!|Good plans — not bad ones!|Plans to give you a future full of hope.|He is not making it up as He goes.|He thought about YOUR life before you were born.|Every day is part of His beautiful plan.|You are not an accident. You are on purpose.", "God, thank You for planning my life with love. I am excited about my future with You. Goodnight."),
        ("Nothing Is Impossible", "Luke 1:37", "With God, nothing is impossible!|NOTHING! Not one single thing!|That mountain? God can move it.|That problem? God can solve it.|That dream? God can make it happen.|Nothing is too hard for the Creator of the universe.|Believe it. Trust it. Rest in it.", "God, nothing is impossible for You. I bring You everything I am worried about and let it go. Goodnight."),
        ("I Can Do All Things", "Philippians 4:13", "I can do ALL things —|through Christ who gives me strength!|Not some things. Not easy things. ALL things.|Hard homework? I can do it.|Being kind when others are mean? I can do it.|Trying again after failing? I can do it.|Christ gives me His strength. That is enough.", "Jesus, thank You for being my strength. I cannot do it alone, but I can do anything WITH You. Goodnight."),
        ("The Lord Is My Light", "Psalm 27:1", "The Lord is my light — no more darkness!|The Lord is my salvation — no more fear!|When scary things come, I do not tremble.|Why? Because GOD is on my side.|His light shines in every dark corner.|His love drives away every fear.|I am safe. I am seen. I am His.", "God, be my light tonight. Chase away every shadow. I am not afraid because You are here. Goodnight."),
        ("Fearfully Made", "Psalm 139:14", "I am fearfully and wonderfully made!|That means God made me with care and thought.|Every freckle. Every dimple. Every curl.|My laugh, my voice, my personality.|None of it was random or accidental.|God designed ME on purpose.|I am His masterpiece. His art. His treasure.", "God, I am Your masterpiece. Help me see myself the way You see me — beautiful and loved. Goodnight."),
        ("Love One Another", "John 13:34", "Love one another.|The way Jesus loved us — love each other.|With patience. With kindness. With forgiveness.|Love when it is easy. Love when it is hard.|Love the lovable. Love the unlovable.|This is how people will know we follow Jesus.|By our love.", "Jesus, give me Your love for others. Help me love the way You love — with no limits. Goodnight."),
        ("Do Not Worry", "Matthew 6:34", "Do not worry about tomorrow!|Tomorrow will take care of itself.|Today has enough to think about.|God holds tomorrow in His hands.|He already knows what is coming.|And He already has a plan.|So breathe. Rest. Let go.|God has got this.", "God, I give You every worry. I will not think about tomorrow tonight. You have it all under control. Goodnight."),
        ("Be Kind", "Colossians 3:12", "Put on kindness like putting on clothes!|Every morning, dress yourself in gentleness.|Wrap yourself in compassion.|Button up with patience.|Zip up with forgiveness.|Walk out the door wearing LOVE.|The world needs more people dressed in kindness.", "God, tomorrow I will put on kindness first thing. Dress me in Your love from the inside out. Goodnight."),
        ("Joy of the Lord", "Nehemiah 8:10", "The joy of the Lord is my strength!|Not happiness that depends on what happens —|but JOY that comes from knowing God.|Joy when things go well. Joy when they do not.|Joy in the morning. Joy at night.|Joy is deeper than a smile.|It lives in my heart because God lives there.", "God, fill me with Your joy — the deep kind that nothing can steal. Joy is my strength. Goodnight."),
        ("God Hears Me", "Psalm 34:17", "When I cry out, God hears me!|He does not ignore me or turn away.|My voice matters to Him.|My whispers reach His ears.|My tears touch His heart.|I am never talking to an empty room.|God is always listening. Always.", "God, thank You for hearing every word I say — even the ones I do not say out loud. You know my heart. Goodnight."),
        ("Peace I Give You", "John 14:27", "Jesus said: My peace I give to you.|Not the world's kind of peace — something better.|A deep calm that nothing can shake.|Peace in the storm. Peace in the waiting.|Peace in the unknown. Peace in the dark.|Jesus-peace is supernatural.|Receive it right now.", "Jesus, I receive Your peace. Let it fill every part of me like warm water. Calm my mind. Still my heart. Goodnight."),
        ("God Is My Helper", "Psalm 121:2", "My help comes from the Lord!|The one who made heaven and earth!|If He can make EVERYTHING —|He can certainly help ME.|No problem is too big.|No question is too hard.|No situation is hopeless.|My helper is the Creator of the universe.", "God, You are my helper. I do not face anything alone. Whatever tomorrow brings, You will be there helping me. Goodnight."),
        ("Shine Your Light", "Matthew 5:16", "Let your light shine!|Do not hide it under a basket.|Be kind — that is shining!|Be helpful — that is shining!|Be honest — that is shining!|Be brave — that is shining!|The world needs YOUR light.|Shine bright, little one!", "God, help me shine my light for You tomorrow. Let everyone see Your love through me. Goodnight, little light."),
        ("God Never Changes", "Malachi 3:6", "Everything around us changes.|Seasons change. People move. Kids grow up.|But God? He NEVER changes.|His love is the same yesterday, today, and forever.|You can count on Him when everything else shifts.|He is the one steady thing in a spinning world.|God is your anchor.", "God, in a world that always changes, You stay the same. Thank You for being my steady anchor. Goodnight."),
        ("God Goes Before Me", "Deuteronomy 31:8", "The Lord goes before you!|He is already in tomorrow.|He is already in next week and next year.|Wherever you are going, God is already there.|Preparing the way. Making it ready.|You are never walking into the unknown alone.|God went first.", "God, You are already in my tomorrow. I do not need to be afraid of what is ahead. You went before me. Goodnight."),
        ("New Every Morning", "Lamentations 3:23", "God's mercies are new every morning!|Every single day is a fresh start.|Yesterday's mistakes are gone.|Today is brand new.|No matter what happened before,|God gives you a clean page every sunrise.|Great is His faithfulness!", "God, tomorrow is a fresh new day with fresh new mercy. Thank You for never running out of grace. Goodnight."),
        ("Forever Loved", "Romans 8:38-39", "NOTHING can separate you from God's love!|Not height or depth.|Not angels or demons.|Not today or tomorrow.|Not anything in all creation.|You are loved FOREVER.|Stuck to God's love like glue.|Nothing can peel you away.", "God, NOTHING can take Your love from me. Nothing. I am locked in Your love forever. That is the best goodnight of all. Goodnight."),
    ]
    return create_childrens_book(430, "Selam_First_Bible_Verses",
        "My First Bible Verses", "20 Scriptures Every Toddler Should Know",
        "1-4", verses)




def book_431():
    """Brave Bible Kids"""
    s = [("David vs Goliath", "1 Samuel 17:45", "Everyone was scared of the giant.|But David said: God is bigger!|He picked up five smooth stones.|He did not need a sword or shield.|He had something better — faith in God!|David ran toward the giant. WHOOSH!|One stone. One God. One victory.|You can face giants too!", "God, I am not afraid of giants because You are on my side. Make me brave like David. Goodnight."),
         ("Esther Saves Her People", "Esther 4:14", "Queen Esther had to make a choice.|Stay quiet and be safe? Or speak up and risk everything?|She chose to be brave.|I was born for such a time as this, she said.|She went to the king even though she was scared.|God gave her favor. Her people were saved!|Sometimes being brave means speaking up.", "God, give me Esther's courage. When I need to speak up, help me be bold. Goodnight."),
         ("Daniel Keeps Praying", "Daniel 6:10", "The rule said: No praying to God!|But Daniel loved God too much to stop.|He opened his window and prayed anyway.|Three times a day. Every single day.|Even when they threw him to the lions.|Daniel chose God over comfort.|That is real bravery.", "God, help me choose You over everything — even when it costs me something. That is true courage. Goodnight."),
         ("Moses at the Red Sea", "Exodus 14:13", "The army was coming. The sea was ahead.|There was nowhere to go!|But Moses said: Do not be afraid! Stand still!|Watch God fight for you!|Moses raised his staff. The sea split open!|When God says GO — go!|The impossible became possible.", "God, when I feel trapped, remind me that You are about to do something amazing. I will stand still and watch. Goodnight."),
         ("Joshua at Jericho", "Joshua 6:2", "The walls were thick. The gates were locked.|No way in. No way through.|But God said: March around the city.|Joshua obeyed — even though it seemed silly.|March. March. March. Shout!|CRASH! The walls fell flat!|God's methods might seem strange, but they always work.", "God, help me follow Your instructions even when they do not make sense to me. Your way always wins. Goodnight."),
         ("Shadrach, Meshach, Abednego", "Daniel 3:17", "The king said: Bow to my statue!|Three young men said: NO. We bow to God alone.|The king threw them into a fiery furnace!|But when he looked inside — FOUR people were walking!|God was in the fire with them!|They came out without even smelling like smoke.|When you stand for God, He stands with you.", "God, if I ever face a fire, I know You will be in it with me. I will not bow to anything but You. Goodnight."),
         ("Gideon's Brave 300", "Judges 7:7", "God told Gideon: Your army is too big.|Send most of them home.|Only 300 men remained. Against thousands!|God wanted everyone to know: I AM the strength.|Trumpets and torches. No swords needed.|The enemy fled in terror!|With God, you do not need to be the biggest or strongest.", "God, You do not need me to be big. You just need me to be willing. I am willing. Goodnight."),
         ("Nehemiah Builds the Wall", "Nehemiah 2:18", "The city walls were broken and burned.|People said: It is impossible to rebuild!|But Nehemiah prayed. Then he got to work.|People tried to scare him. He kept building.|People mocked him. He kept building.|In 52 days — the wall was finished!|Brave people keep going when others quit.", "God, help me keep going even when people say I cannot. With You, all things are possible. Goodnight."),
         ("Peter Walks on Water", "Matthew 14:29", "Jesus said: Come.|Peter looked at the water. Stepped out of the boat.|He was WALKING ON WATER!|But then he looked at the waves and sank.|Jesus grabbed him immediately.|Bravery is stepping out.|When you start to sink, Jesus catches you.", "Jesus, help me step out in faith. And when I start to sink, grab me. You always catch me. Goodnight."),
         ("Stephen's Last Prayer", "Acts 7:60", "Stephen loved Jesus and told everyone about Him.|People got angry. Very angry.|They threw stones at him.|But even as he was dying, Stephen prayed:|Lord, forgive them.|He was brave enough to forgive his enemies.|That is the bravest thing of all.", "Jesus, give me a heart brave enough to forgive. Even when people hurt me, help me pray for them. Goodnight."),
         ("Paul in Prison", "Acts 16:25", "Paul and Silas were in prison.|Chained up. Beaten. In the dark.|But at midnight — they started SINGING!|Worshipping God in the worst place!|An earthquake shook the prison. Chains fell off!|The doors flew open!|Worship is the bravest weapon of all.", "God, even in my hardest moments, I will worship You. Praise breaks chains. Goodnight with a song."),
         ("Mary Says Yes", "Luke 1:38", "An angel appeared to young Mary.|You will have a baby — God's Son!|Mary was just a teenager. She was scared.|But she said: Let it be as God says.|She did not fully understand.|But she trusted God completely.|Saying yes to God is always brave.", "God, I say yes to You tonight. Whatever You are asking of me, my answer is yes. I trust You. Goodnight."),
         ("Rahab's Red Rope", "Joshua 2:21", "Rahab lived in a city about to fall.|Spies from God's people came to her door.|She hid them because she believed in God.|Tie a red rope in your window, they said.|She did — and when the walls fell, she was saved!|One act of faith. One red rope. One saved family.|Bravery is choosing God when everyone else does not.", "God, I choose You. Even if no one else does, I will believe in You. Goodnight."),
         ("Joseph Forgives", "Genesis 50:20", "Joseph's brothers sold him as a slave.|Years of suffering. Prison. Loneliness.|But God raised Joseph to power!|When his brothers came begging, Joseph could have gotten revenge.|Instead, he said: What you meant for evil, God meant for good.|Forgiving those who hurt you? THAT is brave.", "God, help me forgive like Joseph. Bravery is not revenge — it is grace. Goodnight."),
         ("Jesus in the Garden", "Luke 22:42", "Jesus knew what was coming.|Pain. Suffering. The cross.|He was so stressed, He sweated drops of blood.|Father, take this cup from me, He prayed.|But He added: Not my will — Yours.|Jesus was brave enough to obey when it cost Him everything.|The ultimate act of courage.", "Jesus, You were brave for ME. Thank You. Help me be brave for others. Goodnight."),
    ]
    return create_childrens_book(431, "Selam_Brave_Bible_Kids",
        "Brave Bible Kids", "15 Stories of Courage for Little Ones",
        "2-5", s)




def book_432():
    """God Made Me Special"""
    s = [
        ("God Planned You", "Psalm 139:16", "Before you were born, God had a plan.|He knew exactly who you would be.|Your smile. Your laugh. Your favorite color.|All planned by the Creator of everything.|You are not a mistake or an accident.|You are ON PURPOSE.", "God, I am not random — I am planned. Thank You for thinking of me before I was born. Goodnight."),
        ("Your Amazing Body", "Psalm 139:14", "Look at your hands — they can hold and hug!|Look at your feet — they can run and jump!|Your eyes see colors. Your ears hear music.|Your nose smells flowers. Your tongue tastes food.|God designed every single part of you.|And He said: VERY GOOD!", "God, my body is amazing because You made it. Thank You for every part of me. Goodnight."),
        ("Your Feelings Matter", "Psalm 56:8", "Happy, sad, angry, scared —|ALL your feelings are okay!|God gave you feelings for a reason.|It is okay to cry. It is okay to laugh.|God sees every tear you shed.|He keeps them in a bottle.|Your feelings matter to Him.", "God, thank You for caring about my feelings. You never say stop crying. You hold my tears. Goodnight."),
        ("You Are Loved No Matter What", "Romans 8:38", "Did you have a bad day?|God still loves you.|Did you make a mistake?|God still loves you.|Were you grumpy or unkind?|God STILL loves you.|Nothing you do makes God love you less.|And nothing you do makes God love you more.|His love is always at maximum.", "God, Your love for me never changes. Bad days, good days — You love me the same. Thank You. Goodnight."),
        ("Nobody Is Like You", "Psalm 139:13", "In the whole wide world —|seven billion people —|there is NO ONE exactly like you!|Your fingerprints are unique.|Your voice is unique.|Your combination of gifts is unique.|God broke the mold after making you.|You are one of a kind!", "God, I am one of a kind because You made me that way. Help me celebrate being ME. Goodnight."),
        ("God Gave You Gifts", "1 Peter 4:10", "God gave YOU special gifts!|Maybe you are good at singing or drawing.|Maybe you are kind or funny.|Maybe you are brave or gentle.|Maybe you notice when others are sad.|Whatever your gift — it is from God.|Use it to make the world better!", "God, show me my gifts. Help me use them to help others and bring You glory. Goodnight."),
        ("You Are Never Alone", "Matthew 28:20", "When you wake up — God is there.|When you eat breakfast — God is there.|When you play — God is there.|When you sleep — God is there.|In the car, at the store, at the doctor.|God never leaves your side.|You are NEVER alone. Not even for one second.", "God, You are with me right now. You will be with me when I wake up. I am never alone. Goodnight."),
        ("God Has Big Plans", "Ephesians 2:10", "You are God's masterpiece!|Created to do good things that God planned in advance.|You might not know what they are yet.|But God does!|Maybe you will help people.|Maybe you will create beautiful things.|Maybe you will tell others about Jesus.|Whatever it is — it will be amazing!", "God, I am excited to discover the big plans You have for me. I am Your masterpiece in progress. Goodnight."),
        ("Your Words Have Power", "Proverbs 18:21", "Your mouth is powerful!|Kind words can make someone's day.|Mean words can break someone's heart.|Choose your words carefully, little one.|Say: You are special. I love you. Thank you.|Say: I am sorry. I forgive you.|Words can build people up like building blocks.", "God, help me use my words to build people up, not tear them down. Put kind words on my tongue. Goodnight."),
        ("God's Child Forever", "1 John 3:1", "You are a child of GOD!|Not a stranger. Not a servant.|A CHILD. A son or daughter of the King!|That makes you royalty.|You belong to the most powerful family in the universe.|No one can kick you out.|You are His child today, tomorrow, and forever.", "God, I am YOUR child. That is my identity. Nothing can change it. I belong to You forever. Goodnight, my Father."),
    ]
    return create_childrens_book(432, "Selam_God_Made_Me_Special",
        "God Made Me Special", "A Bible Book About Who I Am for Little Ones",
        "2-5", s)




def book_433():
    """Bible Bedtime Lullabies"""
    s = [
        ("The Lord Is My Shepherd Lullaby", "Psalm 23:1-2", "The Lord is my shepherd, I shall not want.|He makes me lie down in green pastures.|He leads me beside still, quiet waters.|He restores my little soul.|Shh, shh, rest now, little lamb.|Your Shepherd is watching tonight.|Close your eyes, breathe deep,|everything is going to be all right.", "Shepherd Jesus, sing me to sleep tonight in Your green pastures beside Your still waters. Goodnight."),
        ("Be Still Lullaby", "Psalm 46:10", "Be still, be still, and know.|Know that He is God.|Be still, be still, and rest.|Rest in His gentle love.|The world may spin and rush around,|but here with God, peace is found.|Be still. Be still. Be still.", "God, I am still now. Perfectly still. Wrapped in Your peace. Goodnight."),
        ("Goodnight Stars Lullaby", "Psalm 147:4", "Goodnight stars, goodnight moon.|Goodnight to my cozy room.|God knows every star by name,|and He knows mine just the same.|Twinkle, twinkle, rest your light,|God is watching through the night.", "God who names the stars, You know my name too. Watch over me tonight. Goodnight."),
        ("Angels Watching Lullaby", "Psalm 91:11", "Angels watching, angels near,|nothing scary, nothing to fear.|God commands them: guard this child.|Keep them safe and undefiled.|Wings of mercy, shields of grace,|angels guarding this small place.|Sleep, sleep, little one. Angels are on watch.", "God, thank You for sending angels to guard me while I sleep. Goodnight under their wings."),
        ("Jesus Loves Me Lullaby", "John 3:16", "Jesus loves me, this I know.|For the Bible tells me so.|Little ones to Him belong.|We are weak but He is strong.|Yes, Jesus loves me.|Yes, Jesus loves me.|Close my eyes and rest tonight.|In His love, everything is right.", "Jesus, You love me. That is the best bedtime truth. I rest in Your love. Goodnight."),
        ("Peace Like a River Lullaby", "Isaiah 26:3", "Peace like a river flows through me.|Peace like the ocean, deep and free.|God gives peace to those who trust.|Peace at bedtime is a must.|Flowing, flowing, calm and slow,|peace from God from head to toe.", "God, let Your peace flow through me like a gentle river. From my head to my toes. Goodnight."),
        ("God Never Sleeps Lullaby", "Psalm 121:4", "I close my eyes, but God does not.|He watches me, He sees my cot.|He never sleeps, He never naps,|He holds me gently in His lap.|So rest, dear child, your Father's near,|all through the night, He's always here.", "God, You never close Your eyes. You watch me all night long. I can sleep because You are awake. Goodnight."),
        ("Zephaniah Song Lullaby", "Zephaniah 3:17", "God sings over you tonight.|A lullaby of pure delight.|He rejoices with great joy.|Over every girl and boy.|Hush now, listen, can you hear?|God is singing — He is near.|La la la, shh shh shh,|God is singing just for you.", "God, I hear Your song tonight. Sing over me. Sing me to sleep. I am listening. Goodnight."),
        ("Counting Sheep Lullaby", "John 10:27", "One little sheep, two little sheep,|three little sheep falling asleep.|The Shepherd counts them every one,|not a single sheep left undone.|He calls them each by name so dear.|Every lamb, the Shepherd's near.|You are His lamb. Close your eyes. Sleep.", "Good Shepherd, You know my name. You count me among Your sheep. I am safe in Your flock. Goodnight."),
        ("Morning Will Come Lullaby", "Psalm 30:5", "Weeping may last for the night,|but joy comes with morning light.|So rest your head, dry your tears,|God is bigger than your fears.|Dawn is coming, soft and bright.|Everything will be all right.|Sleep now, morning joy awaits.", "God, joy comes in the morning. Whatever tonight holds, tomorrow brings new mercy. Goodnight."),
    ]
    return create_childrens_book(433, "Selam_Bible_Lullabies",
        "Bible Bedtime Lullabies", "Scripture Songs to Sing Your Baby to Sleep",
        "0-3", s)




# ============================================================
# MAIN - Generate all 8 books
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("GENERATING SELAM FESEHAYE'S LITTLE BLESSINGS BIBLE SERIES")
    print("8 Books for Amazon KDP (Kindle + Paperback)")
    print("=" * 70)
    print()
    
    results = []
    books = [
        (book_426, "Bible Bedtime Stories for Toddlers"),
        (book_427, "Bible Bedtime Prayers for Little Ones"),
        (book_428, "Bible ABCs: Scripture Alphabet"),
        (book_429, "Bible Bedtime Stories for Preschoolers"),
        (book_430, "My First Bible Verses"),
        (book_431, "Brave Bible Kids"),
        (book_432, "God Made Me Special"),
        (book_433, "Bible Bedtime Lullabies"),
    ]
    
    for fn, name in books:
        path, pages = fn()
        results.append((name, pages, path))
    
    print()
    print("=" * 70)
    print("SERIES SUMMARY")
    print("=" * 70)
    total = 0
    for name, pages, path in results:
        total += pages
        print(f"  {name:<45} | {pages:>3} pages")
    print(f"\n  TOTAL: {len(results)} books | {total} total pages")
    print(f"  Author: {AUTHOR}")
    print(f"  Series: {SERIES}")
    print("=" * 70)
