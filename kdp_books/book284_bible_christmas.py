#!/usr/bin/env python3
"""Book 284 - The First Christmas: The True Story of Jesus' Birth Beautifully Told"""
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc
random.seed(284)
TITLE = "THE FIRST CHRISTMAS"
SUBTITLE = "The True Story of Jesus' Birth Beautifully Told"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book284_Christmas_Story_Kids.pdf"
chapters = [
    {"title": "The Angel Visits Mary", "verse": "You will conceive and give birth to a son, and shall call his name Jesus. - Luke 1:31 (WEB)",
     "p1": "In the small town of Nazareth, a young woman named Mary lived a simple, quiet life. She was engaged to marry Joseph, a kind carpenter. One ordinary day, everything changed forever. The angel Gabriel appeared before her in a blinding flash of light! Mary was terrified and confused. Why would an angel visit someone as ordinary as her?",
     "p2": "Gabriel spoke gently: 'Do not be afraid, Mary! God has chosen you for the greatest honor in history. You will have a baby boy, and you must name Him Jesus. He will be called the Son of the Most High God, and His kingdom will never end!' Mary's mind raced. How could this be? She was not yet married! But she trusted God completely.",
     "p3": "With breathtaking faith, Mary responded: 'I am the Lord's servant. Let it happen as you have said.' In that moment, the most important event in human history began. God Himself was coming to Earth as a tiny baby! Mary did not fully understand, but she said YES to God's incredible plan. Her cousin Elizabeth, also miraculously pregnant, confirmed God's blessing. Mary sang a beautiful song of praise that is still remembered today.",
     "words": ["MARY", "ANGEL", "JESUS", "GABRIEL", "NAZARETH", "YES", "SON", "FAITH"]},
    {"title": "The Journey to Bethlehem", "verse": "Joseph also went up from Galilee to Bethlehem. - Luke 2:4 (WEB)",
     "p1": "The Roman Emperor Augustus ordered everyone in his empire to be counted in a census. Every person had to travel to their ancestral hometown to register. For Joseph and Mary, this meant a long, difficult journey from Nazareth all the way to Bethlehem - about 80 miles! Mary was very pregnant, making the trip incredibly challenging.",
     "p2": "For days they traveled dusty roads, climbing hills and crossing valleys. Mary rode on a donkey while Joseph walked alongside, keeping her safe. The roads were crowded with others traveling for the census. They passed through villages and open countryside, sleeping wherever they could find shelter. Mary must have wondered if the baby would come before they reached Bethlehem!",
     "p3": "Finally, after days of exhausting travel, the little town of Bethlehem appeared in the distance. Its lights flickered in the evening darkness. But as they approached, Joseph's heart sank. The town was overflowing with travelers! Every inn, every guest room, every home was packed full. Where would they stay? Mary needed rest desperately. The baby could come at any moment. Joseph knocked on door after door, hearing the same answer: 'No room.'",
     "words": ["JOURNEY", "BETHLEHEM", "DONKEY", "ROAD", "JOSEPH", "TRAVEL", "CENSUS", "MILES"]},
    {"title": "No Room at the Inn", "verse": "There was no room for them in the inn. - Luke 2:7 (WEB)",
     "p1": "Door after door closed in their faces. 'No room! No room!' Joseph was growing desperate. His young wife needed somewhere warm and safe to rest. The baby was coming soon - he could tell from Mary's expression. The town was bursting with visitors and not a single proper room was available anywhere. What would they do?",
     "p2": "Finally, one innkeeper looked at Mary's condition with compassion. He could not offer them a room, but he had a stable behind his inn where animals were kept. It was not much - just a cave-like shelter with hay, a manger for feeding animals, and the warm bodies of cattle and donkeys. Joseph and Mary gratefully accepted. It was humble and unexpected, but God had prepared this exact spot.",
     "p3": "The stable was simple but sheltered from the cold night wind. Hay covered the ground, and the animals' warmth filled the small space. Joseph made Mary as comfortable as possible on the soft hay. Little did the innkeeper know that the most important birth in all of history was about to happen in his humble stable. God chose the lowliest place to bring His Son into the world - proving that true greatness is not found in palaces but in humble hearts.",
     "words": ["INN", "ROOM", "STABLE", "HUMBLE", "HAY", "MANGER", "SHELTER", "HEART"]},
    {"title": "Born in a Manger", "verse": "She wrapped him in cloths, and laid him in a manger. - Luke 2:7 (WEB)",
     "p1": "In the quiet darkness of that simple stable, surrounded by animals and the scent of hay, the most extraordinary moment in history arrived. Mary gave birth to a baby boy - God's own Son, wrapped in human flesh! The Creator of the universe entered His own creation as a helpless, crying infant. The hands that formed the stars now reached out as tiny baby fingers.",
     "p2": "Mary gently wrapped her newborn in strips of cloth called swaddling cloths and laid Him in the only bed available - a manger, a feeding trough for animals! The King of Kings, whose throne is in heaven, spent His first night on earth lying in a box meant for animal food. Joseph watched in wonder, remembering the angel's message that this child would save people from their sins.",
     "p3": "In that humble stable, heaven touched earth. The baby who created galaxies with a word now needed His mother's care. The one who feeds every creature alive was laid in a feeding trough. God could have arranged a palace birth with servants and luxury. Instead He chose poverty and simplicity. Why? Because He came for ALL people - rich and poor, powerful and weak. The manger tells us that God meets us wherever we are, no matter how humble our circumstances.",
     "words": ["BABY", "MANGER", "BORN", "WRAP", "NIGHT", "KING", "HUMBLE", "LOVE"]},

    {"title": "Shepherds and Angels", "verse": "I bring you good news of great joy which will be for all the people! - Luke 2:10 (WEB)",
     "p1": "That same night, on the dark hillsides outside Bethlehem, shepherds were watching their flocks. It was a cold, quiet, ordinary night shift - the kind they had done a thousand times before. They sat around a small fire, keeping alert for wolves and thieves. They were the lowest class in society - dirty, uneducated, working a job no one else wanted.",
     "p2": "Suddenly, without warning, an angel of the Lord appeared in blazing glory! The dark hillside erupted with supernatural light brighter than the noonday sun! The shepherds were absolutely terrified, falling to the ground and hiding their faces. But the angel said, 'Do not be afraid! I bring you WONDERFUL news that is for ALL people! Today, in Bethlehem, a Savior has been born to you - He is Christ the Lord! You will find the baby wrapped in cloths, lying in a manger.'",
     "p3": "Then the sky EXPLODED with light as a VAST army of angels appeared - thousands upon thousands singing and praising God! 'GLORY TO GOD IN THE HIGHEST! And on earth, peace to those He favors!' The entire sky was filled with angelic worship! When the angels returned to heaven, the stunned shepherds looked at each other and said, 'Let's GO!' They ran to Bethlehem, found the manger exactly as the angel described, and worshipped the newborn King. God announced the greatest news in history to the humblest people first!",
     "words": ["SHEPHERDS", "ANGELS", "GLORY", "SING", "NEWS", "STAR", "JOY", "PEACE"]},
    {"title": "Following the Star", "verse": "We saw his star in the east, and have come to worship him. - Matthew 2:2 (WEB)",
     "p1": "Far away in eastern lands, wise men who studied the stars noticed something extraordinary - a new star appeared in the sky that had never been there before! These Magi were scholars who understood that this special star announced the birth of a great king. They gathered expensive gifts and began an incredible journey of hundreds of miles, following the star westward toward the land of Israel.",
     "p2": "The journey took months across deserts and mountains. They arrived first in Jerusalem and asked King Herod, 'Where is the newborn King of the Jews? We saw His star and have come to worship Him!' Herod was deeply troubled - he was the king and wanted no rival! He secretly asked his scholars who said the Messiah would be born in Bethlehem. Herod told the Magi to find the child and report back - but his intentions were evil.",
     "p3": "The star led the Magi to the exact house in Bethlehem where Mary and the child were! When they saw young Jesus, they fell down and worshipped Him. They opened their treasure boxes and presented gold (for a king), frankincense (for God), and myrrh (foreshadowing His death). Warned in a dream not to return to wicked Herod, they went home by a different route. God used a star to guide seekers from faraway lands to worship His Son!",
     "words": ["STAR", "WISE", "MAGI", "GOLD", "GIFTS", "WORSHIP", "EAST", "FOLLOW"]},
    {"title": "Gifts for the King", "verse": "They offered him gifts: gold, frankincense, and myrrh. - Matthew 2:11 (WEB)",
     "p1": "The three gifts the Magi brought were not random - each one had deep prophetic meaning! Gold was the gift given to KINGS. By presenting gold, the wise men acknowledged that this baby was royalty - not just any king, but the King of Kings whose kingdom would never end. From His manger bed, this infant would one day rule over all creation forever.",
     "p2": "Frankincense was burned in worship of GOD. This expensive resin was used in the temple as incense rising to heaven. By giving frankincense, the Magi recognized that this child was not just a human king - He was God Himself in human form! The Creator had entered His creation. Emmanuel - God WITH us! The fragrant smoke of frankincense declared this baby's divine nature.",
     "p3": "Myrrh was used to prepare bodies for BURIAL. This was a strange gift for a baby, but it prophesied that this King would one day give His life as a sacrifice. Jesus was born to die - to save the world through His death and resurrection. Even at His birth, the shadow of the cross was present. Three gifts telling one complete story: He is KING (gold), He is GOD (frankincense), He is SAVIOR who would die for us (myrrh). The Magi understood more than anyone realized!",
     "words": ["GOLD", "FRANKINCENSE", "MYRRH", "KING", "GOD", "SAVIOR", "GIFT", "WORSHIP"]},
    {"title": "The Meaning of Christmas", "verse": "For God so loved the world that he gave his only Son. - John 3:16 (WEB)",
     "p1": "Christmas is not really about trees, presents, or Santa Claus. It is about the most incredible gift ever given - God giving His own Son to save the world! For thousands of years, people were separated from God by sin. No amount of good behavior could bridge the gap. Humanity needed a Savior, and God loved the world so much that He became one of us.",
     "p2": "Think about what Christmas really means: The God who created billions of galaxies made Himself small enough to be a baby. The King of heaven chose a feeding trough instead of a throne. The almighty God became helpless and dependent on human parents. WHY? Because He LOVES us! He wanted to experience human life, walk among us, feel our pain, and ultimately save us from sin and death through His own sacrifice.",
     "p3": "Every time we celebrate Christmas, we celebrate the greatest love story ever told. God did not send a message - He came HIMSELF. He did not demand that we climb up to Him - He came DOWN to us. He did not choose the powerful - He came to the humble. Christmas means that NO ONE is too small, too poor, too ordinary for God's love. The manger proves it. If God can come as a baby in a stable, He can meet you exactly where you are today. THAT is the meaning of Christmas!",
     "words": ["LOVE", "GIFT", "SAVIOR", "HOPE", "JOY", "PEACE", "WORLD", "GAVE"]}
]


def generate_word_search(words):
    grid=[[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)] for _ in range(10)]
    for word in words[:8]:
        word=word.upper()
        for _ in range(50):
            d=random.choice([(0,1),(1,0),(1,1)]); r=random.randint(0,max(0,9-len(word)*d[0])); c=random.randint(0,max(0,9-len(word)*d[1]))
            if r+len(word)*d[0]>10 or c+len(word)*d[1]>10: continue
            for i,ch in enumerate(word): grid[r+i*d[0]][c+i*d[1]]=ch
            break
    return grid
def wrap_text(text,mx=75):
    wds=text.split(); lines=[]; cur=""
    for w in wds:
        if len(cur)+len(w)+1<=mx: cur+=(" " if cur else "")+w
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def build_pdf():
    pdf=PDFDoc(); pc=0
    pdf.new_page(); pc+=1
    pdf.add_filled_rect(50,650,512,100,0.85)
    pdf.add_centered_text(720,TITLE,'F2',26,0); pdf.add_centered_text(690,SUBTITLE,'F4',13,0.2)
    pdf.add_centered_text(660,"Written and Illustrated by",'F4',12,0.3); pdf.add_centered_text(640,AUTHOR,'F2',16,0)
    pdf.add_rect(100,200,412,380,2,0.3)
    pdf.add_centered_text(420,"[ILLUSTRATION: Nativity scene with star, manger,",'F3',10,0.4)
    pdf.add_centered_text(405,"angels, shepherds, and the holy family]",'F3',10,0.4)
    pdf.add_centered_text(100,"The most beautiful story ever told!",'F4',12,0.3)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(700,TITLE,'F2',16,0)
    pdf.add_text(72,600,f"Written by {AUTHOR}",'F4',11,0.2)
    pdf.add_text(72,580,"Copyright 2025. All Rights Reserved.",'F4',10,0.3)
    pdf.add_text(72,550,"Scripture: World English Bible (WEB) - Public Domain.",'F4',10,0.3)
    pdf.add_text(72,520,"For children ages 6-12. Published by Kingdom Kids Publishing",'F4',10,0.3)
    pdf.add_text(72,440,"Dedication: For every child waiting for Christmas morning!",'F4',11,0.2)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"TABLE OF CONTENTS",'F2',18,0); pdf.add_line(150,720,462,720,1,0.3); y=680
    for i,ch in enumerate(chapters): pdf.add_text(72,y,f"Chapter {i+1}: {ch['title']}",'F4',12,0.1); y-=30
    pdf.add_text(72,y-10,"Quiz / Vocabulary / Journal / Certificate / Bonus",'F4',10,0.3)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"HOW TO USE THIS BOOK",'F2',18,0); pdf.add_line(150,720,462,720,1,0.3)
    intro=["Welcome to the most BEAUTIFUL story ever told!","This is the TRUE story of the first Christmas.","",
        "Each chapter has EIGHT pages:","  1-3. The story told in beautiful detail",
        "  4. Full-page illustration","  5. Bible verse + reflection",
        "  6. Activity page","  7. Advent activity (count down to Christmas!)","  8. Drawing + prayer page","",
        "Read one chapter each day during Advent,","or enjoy the whole book in one sitting!","",
        "Merry Christmas! Let the story begin!"]
    y=680
    for l in intro: pdf.add_text(72,y,l,'F4',11,0.15); y-=22
    # 8 chapters x 8 pages = 64 pages
    for idx, ch in enumerate(chapters):
        # P1: Story opening
        pdf.new_page(); pc+=1
        pdf.add_filled_rect(50,700,512,60,0.88)
        pdf.add_centered_text(735,f"Chapter {idx+1}",'F1',10,0.4)
        pdf.add_centered_text(715,ch['title'].upper(),'F2',18,0)
        pdf.add_line(72,690,540,690,0.5,0.4); y=665
        for line in wrap_text(ch['p1'],78): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        # P2: Story middle
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{ch['title']} (continued)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(ch['p2'],78): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=20
        pdf.add_rect(100,y-220,412,210,1.5,0.3)
        pdf.add_centered_text(y-90,f"[ILLUSTRATION: {ch['title']}",'F3',10,0.4)
        pdf.add_centered_text(y-110,"beautiful Christmas scene with warm colors]",'F3',10,0.4)
        # P3: Story conclusion
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{ch['title']} (conclusion)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(ch['p3'],78): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=20
        pdf.add_filled_rect(72,y-35,468,40,0.9)
        pdf.add_centered_text(y-8,"KEY VERSE:",'F2',10,0.2)
        pdf.add_centered_text(y-25,ch['verse'],'F4',10,0)
        # P4: Illustration page
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"CHAPTER {idx+1}: {ch['title'].upper()}",'F2',16,0)
        pdf.add_rect(50,80,512,640,2,0.3)
        pdf.add_centered_text(420,f"[FULL-PAGE ILLUSTRATION: {ch['title']}",'F3',11,0.4)
        pdf.add_centered_text(400,"in rich, detailed Christmas artwork]",'F3',11,0.4)


        # P5: Verse + Reflection
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"REFLECTION",'F2',16,0); pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_filled_rect(72,680,468,40,0.9)
        pdf.add_centered_text(705,ch['verse'],'F5',10,0)
        qs=["1. What is the most important moment in this chapter?",
            "2. How does this chapter show God's love?",
            "3. What does this chapter mean for YOUR life?"]
        y=650
        for q in qs:
            pdf.add_text(72,y,q,'F2',10,0.1); y-=18
            for _ in range(3): pdf.add_line(90,y,530,y,0.5,0.6); y-=18
            y-=10
        pdf.add_text(72,y,"My prayer:",'F2',11,0.1); y-=20
        for _ in range(4): pdf.add_line(72,y,540,y,0.5,0.6); y-=18
        # P6: Activity (word search)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"CHRISTMAS ACTIVITY",'F2',16,0)
        pdf.add_text(72,720,f"Word Search - {ch['title']}",'F4',11,0.2)
        grid=generate_word_search(ch['words']); y=680
        for row in grid: pdf.add_centered_text(y,"   ".join(row),'F3',14,0.1); y-=24
        y-=15; pdf.add_text(72,y,"Words: "+"  ".join(ch['words']),'F3',9,0.2)
        y-=35; pdf.add_text(72,y,"Write what Christmas means to you:",'F2',10,0.1)
        for _ in range(3): y-=22; pdf.add_line(72,y,540,y,0.5,0.6)
        # P7: Advent activity
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"ADVENT ACTIVITY - Day {idx+1}",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        activities=["Make a card for someone you love and write why they matter to you.",
                    "Help someone today without being asked - surprise act of kindness!",
                    "Tell 3 people what Christmas really means to you.",
                    "Pray for someone who is alone this Christmas season.",
                    "Sing a Christmas carol with your family tonight!",
                    "Read Luke 2:1-20 out loud together as a family.",
                    "Give away something you own to someone who needs it more.",
                    "Write a thank-you letter to God for sending Jesus."]
        pdf.add_text(72,710,"Today's Advent Challenge:",'F2',12,0.1)
        pdf.add_filled_rect(72,650,468,50,0.92)
        for i,line in enumerate(wrap_text(activities[idx],65)):
            pdf.add_text(80,680-i*16,line,'F4',11,0.15)
        pdf.add_text(72,620,"How I did it:",'F4',11,0.2); y=595
        for _ in range(5): pdf.add_line(72,y,540,y,0.5,0.6); y-=22
        pdf.add_text(72,y-10,"How it made me feel:",'F4',11,0.2)
        for _ in range(3): y-=22; pdf.add_line(72,y,540,y,0.5,0.6)
        # P8: Drawing + prayer
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"DRAW CHAPTER {idx+1}",'F2',16,0)
        pdf.add_text(72,720,f"Draw your favorite scene from: {ch['title']}",'F4',11,0.2)
        pdf.add_rect(72,320,468,380,1.5,0.3)
        pdf.add_text(72,300,"My Christmas prayer:",'F2',11,0.1); y=275
        for _ in range(4): pdf.add_line(72,y,540,y,0.5,0.6); y-=20


    # Quiz (2 pages)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"CHRISTMAS QUIZ - Part 1",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs=[("1. What angel visited Mary?","a) Michael  b) Gabriel  c) Raphael"),
        ("2. Where was Jesus born?","a) Nazareth  b) Jerusalem  c) Bethlehem"),
        ("3. Why were Mary and Joseph traveling?","a) Vacation  b) Census  c) Wedding"),
        ("4. Where was baby Jesus laid?","a) Bed  b) Cradle  c) Manger")]
    y=700
    for q,o in qs: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=40
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"CHRISTMAS QUIZ - Part 2",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs2=[("5. Who heard the angel's announcement first?","a) Kings  b) Shepherds  c) Priests"),
         ("6. What guided the wise men?","a) Map  b) Angel  c) Star"),
         ("7. What 3 gifts were given?","a) Gold, silver, bronze  b) Gold, frankincense, myrrh  c) Food, clothes, toys"),
         ("8. John 3:16 says God gave His Son because He ___ the world","a) Judged  b) Loved  c) Made")]
    y=700
    for q,o in qs2: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=40
    pdf.add_text(72,y-10,"Answers: 1b, 2c, 3b, 4c, 5b, 6c, 7b, 8b",'F3',9,0.4)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"VOCABULARY",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    vocab=[("Advent","The season of waiting and preparing for Christmas"),("Manger","A feeding trough for animals"),
           ("Messiah","The promised Savior sent by God"),("Incarnation","God becoming human in Jesus"),
           ("Emmanuel","Means 'God with us'"),("Frankincense","Fragrant resin burned in worship"),
           ("Myrrh","Expensive burial spice"),("Census","An official count of all people"),
           ("Nativity","The birth of Jesus Christ"),("Prophecy","A prediction of future events by God")]
    y=710
    for w,d in vocab: pdf.add_text(72,y,f"{w}:",'F2',11,0.1); pdf.add_text(210,y,d,'F4',10,0.2); y-=28

    prompts=["What Christmas means to me...","A gift I want to give to Jesus this year...",
             "My favorite part of the Christmas story...","My prayer for this Christmas season..."]
    for j in range(4):
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"MY CHRISTMAS JOURNAL - Page {j+1}",'F2',16,0)
        pdf.add_text(72,710,prompts[j],'F5',12,0.2); y=680
        for _ in range(24): pdf.add_line(72,y,540,y,0.5,0.7); y-=25

    pdf.new_page(); pc+=1
    pdf.add_rect(50,50,512,692,3,0.2); pdf.add_rect(60,60,492,672,1.5,0.4)
    pdf.add_centered_text(680,"CERTIFICATE OF COMPLETION",'F2',22,0)
    pdf.add_centered_text(640,"This certifies that",'F4',14,0.2)
    pdf.add_line(180,600,432,600,1,0.3)
    pdf.add_centered_text(540,"has read the complete Christmas story in",'F4',12,0.2)
    pdf.add_centered_text(510,TITLE,'F2',14,0)
    pdf.add_centered_text(400,"Date: _______________",'F4',12,0.3)
    pdf.add_centered_text(280,"\"For unto us a child is born!\" - Isaiah 9:6",'F5',14,0.1)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS",'F2',18,0); y=690
    for i,ch in enumerate(chapters[:4]):
        pdf.add_rect(72,y-55,468,55,1,0.3); pdf.add_text(80,y-15,f"Card {i+1}: {ch['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,ch['verse'],'F4',9,0.2); y-=65
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS (cont.)",'F2',18,0); y=700
    for i,ch in enumerate(chapters[4:]):
        pdf.add_rect(72,y-55,468,55,1,0.3); pdf.add_text(80,y-15,f"Card {i+5}: {ch['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,ch['verse'],'F4',9,0.2); y-=65

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MY CHRISTMAS GIFT LIST FOR JESUS",'F2',16,0)
    pdf.add_line(150,740,462,740,1,0.3)
    pdf.add_text(72,710,"The wise men gave Jesus gifts. What gifts can YOU give Him?",'F4',11,0.2)
    pdf.add_text(72,680,"(Not things you buy - gifts from your HEART!)",'F4',10,0.3); y=650
    gifts=["My time (to pray, read Bible, serve):","My talent (something I'm good at):","My love (acts of kindness):","My obedience (following God's word):","My worship (praise and thankfulness):"]
    for g in gifts:
        pdf.add_text(72,y,g,'F2',10,0.1); y-=20; pdf.add_line(72,y,540,y,0.5,0.6); y-=15
        pdf.add_line(72,y,540,y,0.5,0.6); y-=30

    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),FILENAME)
    pdf.save(out); print(f"Generated {FILENAME} with {pc} pages"); return pc
if __name__=="__main__": build_pdf()
