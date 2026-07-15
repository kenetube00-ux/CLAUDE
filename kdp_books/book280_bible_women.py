#!/usr/bin/env python3
"""Book 280 - Amazing Women of the Bible: 10 Stories of Faith, Strength & Wisdom"""
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc
random.seed(280)
TITLE = "AMAZING WOMEN OF THE BIBLE"
SUBTITLE = "10 Stories of Faith, Strength & Wisdom"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book280_Amazing_Women_Bible.pdf"
stories = [
    {"title": "Eve - The Mother of All Living", "character": "Eve",
     "verse": "The man called his wife Eve because she was the mother of all living. - Genesis 3:20 (WEB)",
     "moral": "Even after mistakes, God still has a beautiful plan for your life!",
     "application": "I can start fresh after making mistakes because God always offers new beginnings.",
     "p1": "Eve was the very first woman ever created, formed by God from Adam's rib to be his perfect partner. She lived in the stunning Garden of Eden surrounded by beauty beyond imagination. Every fruit tree, every flower, every animal was hers to enjoy. She walked with God in the cool of the evening, talking with Him directly. Life was absolutely perfect.",
     "p2": "But one day the cunning serpent tempted Eve with the one fruit God had forbidden. She listened to the lie that God was holding something good back from her. She ate the fruit and shared it with Adam. Immediately everything changed - shame, fear, and pain entered the world. They were sent out of the beautiful garden. It was the saddest day in human history and Eve must have carried terrible guilt.",
     "p3": "Yet God did not abandon Eve! He made clothes for her and Adam, showing His continued care. He promised that one day her descendant would crush the serpent and defeat evil forever. Eve became the mother of all people. Despite her mistake, God chose to bring salvation through her offspring. Eve teaches us that even our biggest failures cannot cancel God's purposes for our lives. He always offers redemption and a new beginning!",
     "words": ["EVE", "GARDEN", "MOTHER", "WOMAN", "LIFE", "HOPE", "CREATE", "NEW"]},
    {"title": "Sarah - Mother of a Nation", "character": "Sarah",
     "verse": "Is anything too hard for the LORD? - Genesis 18:14 (WEB)",
     "moral": "Nothing is impossible for God - even when it seems way too late!",
     "application": "I can trust God's timing even when His promises seem to take forever.",
     "p1": "Sarah was Abraham's wife, and God had promised them a son who would be the beginning of a great nation. But years passed - ten years, twenty years, thirty years - and no baby came. Sarah grew old, far past the age of having children. She was now ninety years old! Everyone would have given up on such a promise by now. How could God possibly keep this promise?",
     "p2": "One day three visitors appeared at their tent. One of them, the Lord Himself, told Abraham that Sarah would have a son within a year. Sarah was listening from inside the tent and she actually LAUGHED! She could not believe it - she was too old! The visitor asked, 'Is anything too hard for the Lord?' Sarah was embarrassed and tried to deny laughing, but God had heard her doubt.",
     "p3": "Yet exactly as God promised, the impossible happened. Sarah became pregnant and gave birth to a healthy baby boy when she was ninety years old! They named him Isaac, which means 'laughter' - because Sarah said, 'God has brought me laughter! Everyone who hears about this will laugh with joy!' From Sarah and Abraham came the entire nation of Israel and eventually Jesus Himself. Sarah proves that God's promises never expire, no matter how impossible they seem!",
     "words": ["SARAH", "PROMISE", "LAUGH", "BABY", "ISAAC", "FAITH", "NATION", "TRUST"]},

    {"title": "Miriam - The Brave Big Sister", "character": "Miriam",
     "verse": "Miriam the prophetess took a tambourine in her hand. - Exodus 15:20 (WEB)",
     "moral": "Big sisters (and brothers) can be brave heroes in God's story!",
     "application": "I can be brave and protective of my family just like Miriam was.",
     "p1": "When baby Moses was born, Pharaoh had ordered all Hebrew baby boys thrown into the river. Moses' mother hid him for three months, then placed him in a waterproof basket in the reeds of the Nile River. His big sister Miriam, probably about twelve years old, hid nearby watching to see what would happen to her precious baby brother. Her heart pounded with worry and hope.",
     "p2": "Pharaoh's own daughter came to the river to bathe and found the crying baby! Miriam had to think fast. With incredible courage for a young girl, she stepped out from her hiding place and approached the princess of Egypt. 'Shall I find a Hebrew woman to nurse the baby for you?' she asked boldly. The princess agreed! Miriam ran to get her own mother, who was then PAID to raise her own son in safety.",
     "p3": "Miriam's quick thinking and brave action saved Moses who would later lead all of Israel to freedom! Years later, after crossing the Red Sea, Miriam led all the women in a triumphant song and dance of celebration. She became a prophetess and leader alongside Moses and Aaron. From a brave girl watching a basket to a leader of a nation - Miriam shows that God uses young people who are willing to step up with courage in scary moments!",
     "words": ["MIRIAM", "BRAVE", "SISTER", "BASKET", "RIVER", "DANCE", "SONG", "LEADER"]},
    {"title": "Deborah - The Warrior Judge", "character": "Deborah",
     "verse": "Deborah, a prophetess, judged Israel at that time. - Judges 4:4 (WEB)",
     "moral": "God raises up strong women to lead and bring justice!",
     "application": "I can be a leader and stand up for what is right, no matter my age or gender.",
     "p1": "In a time when Israel had no king, God raised up judges to lead the people. Deborah was one of the most remarkable leaders in all the Bible - she was a prophetess, judge, and military strategist! People came from all over Israel to sit under her palm tree and receive her wise decisions. She settled disputes, gave counsel, and spoke God's words with authority and grace.",
     "p2": "When a cruel king named Jabin was oppressing Israel with 900 iron chariots, God gave Deborah a message. She summoned the general Barak and told him to gather ten thousand warriors to fight. But Barak was afraid and said he would only go if Deborah went with him! Without hesitation, Deborah agreed to go to the battlefield. She was not afraid because she knew God would give them the victory He had promised.",
     "p3": "On the day of battle, Deborah gave the command to charge. She declared, 'Go! This is the day the Lord has given the enemy into your hands!' The Israelites swept down from Mount Tabor and God confused the enemy army. A great storm flooded the river and their chariots got stuck in the mud! Israel won a complete victory with Deborah's faith-filled leadership. She led Israel in peace for forty years, proving that God empowers women to be mighty leaders!",
     "words": ["DEBORAH", "JUDGE", "LEADER", "WISE", "BRAVE", "PALM", "BATTLE", "PEACE"]},
    {"title": "Ruth - Loyalty and Love", "character": "Ruth",
     "verse": "Where you go, I will go. Your people will be my people. - Ruth 1:16 (WEB)",
     "moral": "Loyalty and hard work lead to blessings beyond imagination!",
     "application": "I can show loyalty by sticking with people I love even when life gets hard.",
     "p1": "Ruth was a young woman from Moab who married into an Israelite family. When her husband died, she faced a terrible choice - return to her own family in Moab where life would be comfortable, or stay with her grieving mother-in-law Naomi who had nothing to offer. Ruth's sister-in-law chose to leave, but Ruth's heart was bonded to Naomi with unbreakable love.",
     "p2": "With one of the most beautiful speeches in all of Scripture, Ruth declared her loyalty: 'Where you go, I will go. Where you stay, I will stay. Your people will be my people, and your God will be my God.' They traveled together to Bethlehem, arriving poor and hungry. Ruth immediately went to work gleaning leftover grain in the fields - back-breaking labor from dawn to dusk. She never complained, working tirelessly to provide for Naomi.",
     "p3": "The field owner, a wealthy man named Boaz, noticed Ruth's extraordinary character. He admired her loyalty to Naomi, her hard work, and her faith in choosing to follow God. Boaz and Ruth fell in love and married. God blessed them with a son named Obed, who became the grandfather of King David! Ruth, a foreign woman who chose loyalty and love, became part of the family line of Jesus Christ Himself. Her story proves that faithful love is always rewarded.",
     "words": ["RUTH", "LOYAL", "LOVE", "NAOMI", "GLEAM", "BOAZ", "FAITH", "FAMILY"]},

    {"title": "Hannah - The Praying Mother", "character": "Hannah",
     "verse": "For this child I prayed, and the LORD granted my petition. - 1 Samuel 1:27 (WEB)",
     "moral": "Pour your heart out to God in prayer - He hears every word!",
     "application": "I can bring my biggest wishes and deepest hurts to God in prayer.",
     "p1": "Hannah desperately wanted a baby, but year after year she could not have children. In her culture, this brought great shame and sadness. To make things worse, another woman in her household constantly mocked and bullied her about it. Each year when they traveled to the temple, Hannah would cry so much she could barely eat. Her heart was breaking under the weight of unfulfilled longing.",
     "p2": "One day at the temple, Hannah could hold back no more. She fell to her knees and poured out her soul to God in the most intense, heartfelt prayer of her life. She wept and prayed so passionately that her lips moved but no sound came out. The priest Eli thought she was drunk! But Hannah explained she was pouring out her anguish to God. She made a sacred promise that if God gave her a son, she would dedicate him to serve God his entire life.",
     "p3": "God heard Hannah's prayer and remembered her! She became pregnant and gave birth to a son named Samuel. True to her promise, when Samuel was old enough, she brought him to the temple to serve God. It must have been incredibly hard to let her precious answered prayer go, but Hannah trusted God completely. Samuel grew up to become one of the greatest prophets in Israel's history! Hannah's passionate prayer and faithful promise changed a nation.",
     "words": ["HANNAH", "PRAYER", "SAMUEL", "TEMPLE", "PROMISE", "FAITH", "MOTHER", "HEAR"]},
    {"title": "Esther - For Such a Time as This", "character": "Esther",
     "verse": "Who knows if you haven't come to the kingdom for such a time as this? - Esther 4:14 (WEB)",
     "moral": "God places you exactly where you need to be to make a difference!",
     "application": "I can be brave at school, at home, anywhere God has placed me to help others.",
     "p1": "Esther was a young Jewish orphan raised by her cousin Mordecai in the mighty Persian Empire. When the king searched for a new queen, Esther's beauty and grace won his heart. She became Queen of the most powerful empire on earth! But Mordecai warned her to keep her Jewish identity secret. Everything seemed like a fairy tale until a dark shadow fell over the kingdom.",
     "p2": "The king's advisor Haman hated the Jewish people and convinced the king to sign a decree ordering their complete destruction. Mordecai sent an urgent message to Esther: 'Perhaps you have become queen for such a time as this!' But approaching the king uninvited meant risking death. Esther was terrified. She asked all the Jewish people to fast and pray for three days. Then she spoke those brave words: 'If I perish, I perish.'",
     "p3": "Queen Esther put on her royal robes, took a deep breath, and walked uninvited into the king's throne room. The king extended his golden scepter - she was safe! Over two dinners, Esther revealed Haman's evil plot and her own Jewish identity. The king was furious at Haman and saved the Jewish people. Esther's courage saved an entire nation from destruction. She proved that God positions His people in the right place at the right time to change history!",
     "words": ["ESTHER", "QUEEN", "BRAVE", "SAVE", "FAST", "PRAY", "NATION", "TIME"]},
    {"title": "Mary - Mother of Jesus", "character": "Mary",
     "verse": "Behold, the handmaid of the Lord; be it to me according to your word. - Luke 1:38 (WEB)",
     "moral": "Say YES to God even when His plans seem impossible or scary!",
     "application": "I can say yes to God even when I don't fully understand His plan for me.",
     "p1": "Mary was a young Jewish teenager in the small town of Nazareth, engaged to be married to a carpenter named Joseph. She was ordinary in every way except one - her extraordinary faith and humble heart. One day an angel named Gabriel suddenly appeared before her with the most astonishing announcement any person has ever received. Her simple life was about to change forever.",
     "p2": "Gabriel told Mary she would become pregnant by the Holy Spirit and give birth to the Son of God - the Savior the world had been waiting for! Mary was confused and afraid - how could this be? She was not yet married. People would not understand. She could be shamed, rejected, even punished. Everything about this plan seemed impossible and dangerous for a young girl in her world.",
     "p3": "But Mary's response was breathtaking in its humble faith: 'I am the Lord's servant. Let it be done according to your word.' She said YES to God without knowing how everything would work out. Mary carried Jesus, raised Him, stood by Him through His ministry, and was there at the cross. She is remembered forever as the most blessed woman in history - not because she was powerful or wealthy, but because she said yes to God with a humble, trusting heart.",
     "words": ["MARY", "ANGEL", "MOTHER", "JESUS", "HUMBLE", "YES", "FAITH", "BLESSED"]},

    {"title": "Martha and Mary - Two Ways to Love Jesus", "character": "Martha and Mary",
     "verse": "Mary has chosen the good part, which will not be taken from her. - Luke 10:42 (WEB)",
     "moral": "Both serving AND spending time with Jesus are important - but know which comes first!",
     "application": "I will balance busy work with quiet time listening to God each day.",
     "p1": "Jesus had two dear friends who were sisters - Martha and Mary - who lived in the village of Bethany with their brother Lazarus. One day Jesus came to visit their home with His disciples. It was a great honor and Martha wanted everything to be absolutely perfect. She rushed around the kitchen preparing food, setting the table, and making sure every detail was just right.",
     "p2": "Meanwhile, Mary sat at Jesus' feet listening to every word He spoke. She was completely focused on learning from the Master, soaking in His wisdom like a sponge. Martha grew more and more frustrated as she worked alone. Finally she burst out to Jesus, 'Lord, don't you care that my sister has left me to serve alone? Tell her to help me!' She expected Jesus to send Mary to the kitchen immediately.",
     "p3": "But Jesus gently said, 'Martha, Martha, you are worried about many things. But only one thing is truly needed. Mary has chosen the better part, and it will not be taken from her.' Jesus was not saying serving is wrong - Martha's hospitality was beautiful. But He was teaching that spending time with God must come FIRST, before all our busy activity. Both sisters loved Jesus deeply - Martha through serving, Mary through listening. Both are needed, but relationship with God always comes first.",
     "words": ["MARTHA", "MARY", "LISTEN", "SERVE", "JESUS", "HEART", "STILL", "LOVE"]},
    {"title": "Priscilla - Teacher and Leader", "character": "Priscilla",
     "verse": "Greet Priscilla and Aquila, my fellow workers in Christ. - Romans 16:3 (WEB)",
     "moral": "Use your knowledge to help others grow - share what God teaches you!",
     "application": "I can help teach others what I know about God and be a spiritual leader.",
     "p1": "Priscilla and her husband Aquila were an amazing team in the early church. They were tentmakers by trade who opened their home as a church meeting place. When the apostle Paul came to Corinth, he stayed and worked with them. Together they traveled spreading the gospel, teaching new believers, and risking their lives for the faith. Priscilla was known as a brilliant teacher and theologian.",
     "p2": "One day a powerful speaker named Apollos came to their city preaching about Jesus. He was eloquent and passionate, but his understanding of the gospel was incomplete. Instead of publicly embarrassing him, Priscilla and Aquila invited Apollos to their home. There, Priscilla helped explain the way of God more accurately and completely. She taught a great preacher because she knew the Scriptures deeply.",
     "p3": "The Bible mentions Priscilla's name BEFORE her husband's in most references - unusual in that culture - suggesting she was the more prominent teacher. She risked her life for Paul's ministry. Churches met in her home. She discipled new believers and corrected incomplete teaching with grace and wisdom. Priscilla proves that God calls women to be teachers, leaders, and theologians who shape the church and advance His kingdom through their knowledge and boldness.",
     "words": ["PRISCILLA", "TEACH", "LEADER", "CHURCH", "WISE", "BOLD", "SHARE", "GROW"]}
]


def generate_word_search(words):
    grid=[[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)] for _ in range(10)]
    for word in words[:8]:
        word=word.upper()
        for _ in range(50):
            d=random.choice([(0,1),(1,0),(1,1)])
            r=random.randint(0,max(0,9-len(word)*d[0])); c=random.randint(0,max(0,9-len(word)*d[1]))
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
    pdf.add_centered_text(720,TITLE,'F2',24,0)
    pdf.add_centered_text(690,SUBTITLE,'F4',14,0.2)
    pdf.add_centered_text(660,"Written and Illustrated by",'F4',12,0.3)
    pdf.add_centered_text(640,AUTHOR,'F2',16,0)
    pdf.add_rect(100,200,412,380,2,0.3)
    pdf.add_centered_text(420,"[ILLUSTRATION: Beautiful collage of Bible women -",'F3',10,0.4)
    pdf.add_centered_text(405,"Esther, Ruth, Mary, Deborah standing strong]",'F3',10,0.4)
    pdf.add_centered_text(100,"For every girl who wants to be strong and wise!",'F4',12,0.3)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(700,TITLE,'F2',16,0)
    pdf.add_text(72,600,f"Written by {AUTHOR}",'F4',11,0.2)
    pdf.add_text(72,580,"Copyright 2025. All Rights Reserved.",'F4',10,0.3)
    pdf.add_text(72,550,"Scripture: World English Bible (WEB) - Public Domain.",'F4',10,0.3)
    pdf.add_text(72,520,"For children ages 6-12. Published by Kingdom Kids Publishing",'F4',10,0.3)
    pdf.add_text(72,490,"First Edition - 2025",'F4',10,0.3)
    pdf.add_text(72,440,"Dedication: For every girl who dreams big - God has amazing plans for you!",'F4',11,0.2)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"TABLE OF CONTENTS",'F2',18,0)
    pdf.add_line(150,720,462,720,1,0.3); y=680
    for i,s in enumerate(stories):
        pdf.add_text(72,y,f"Woman {i+1}: {s['title']}",'F4',12,0.1); y-=28
    pdf.add_text(72,y-10,"Quiz / Vocabulary / Journal / Certificate / Bonus",'F4',10,0.3)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"HOW TO USE THIS BOOK",'F2',18,0)
    pdf.add_line(150,720,462,720,1,0.3)
    intro=["Welcome! The Bible is filled with incredible women who","changed history through their faith, courage, and wisdom!","",
        "Each woman's story has SIX pages:","  1. Her story begins + illustration",
        "  2. The story continues + action scene","  3. Story conclusion + verse + moral + application",
        "  4. Reflection questions + prayer","  5. Word search puzzle",
        "  6. Draw her + 'I Can Be Like Her By...'","",
        "These women were real people who faced real challenges.","They can inspire YOU to be brave and faithful too!","",
        "Ready to meet these amazing women? Turn the page!"]
    y=680
    for l in intro: pdf.add_text(72,y,l,'F4',11,0.15); y-=22


    for idx, story in enumerate(stories):
        pdf.new_page(); pc+=1
        pdf.add_filled_rect(50,700,512,60,0.88)
        pdf.add_centered_text(735,f"Woman of Faith {idx+1}",'F1',10,0.4)
        pdf.add_centered_text(715,story['title'].upper(),'F2',18,0)
        pdf.add_rect(100,400,412,270,1.5,0.3)
        pdf.add_centered_text(560,f"[ILLUSTRATION: {story['character']} in a beautiful scene",'F3',9,0.4)
        pdf.add_centered_text(545,"showing strength and grace]",'F3',9,0.4)
        for i,line in enumerate(wrap_text(story['p1'],80)):
            pdf.add_text(72,370-i*18,line,'F4',11,0.1)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (continued)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(story['p2'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        pdf.add_rect(100,y-260,412,240,1.5,0.3)
        pdf.add_centered_text(y-120,f"[ILLUSTRATION: {story['character']} in action]",'F3',9,0.4)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (conclusion)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(story['p3'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=15
        pdf.add_filled_rect(72,y-30,468,40,0.9)
        pdf.add_centered_text(y-5,"KEY BIBLE VERSE:",'F2',10,0.2)
        pdf.add_centered_text(y-22,story['verse'],'F4',10,0)
        y-=55
        pdf.add_rect(72,y-40,468,50,2,0.2)
        pdf.add_centered_text(y-5,"MORAL:",'F2',11,0.1)
        pdf.add_centered_text(y-25,story['moral'],'F5',11,0)
        y-=60
        pdf.add_filled_rect(72,y-35,468,40,0.93)
        pdf.add_text(80,y-8,"I CAN BE LIKE HER BY:",'F2',10,0.1)
        pdf.add_text(80,y-25,story['application'],'F4',10,0.2)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"WHAT I LEARNED",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_text(72,710,f"Reflecting on: {story['title']}",'F4',11,0.2)
        qs=[f"1. What challenge did {story['character']} face?",
            f"2. How did {story['character']} show faith and courage?",
            "3. How can I apply her example in my own life?"]
        y=670
        for q in qs:
            pdf.add_text(72,y,q,'F2',11,0.1); y-=20
            for _ in range(3): pdf.add_line(90,y,530,y,0.5,0.6); y-=20
            y-=10
        pdf.add_filled_rect(72,y-120,468,130,0.92)
        pdf.add_centered_text(y-5,"MY PRAYER",'F2',14,0.1)
        pdf.add_text(80,y-25,f"God, help me be strong and faithful like {story['character']}...",'F4',10,0.2)
        for i in range(5): pdf.add_line(80,y-50-i*20,520,y-50-i*20,0.5,0.6)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"WORD SEARCH PUZZLE",'F2',16,0)
        pdf.add_text(72,720,f"Find words from: {story['title']}",'F4',11,0.2)
        grid=generate_word_search(story['words']); y=680
        for row in grid: pdf.add_centered_text(y,"   ".join(row),'F3',14,0.1); y-=24
        y-=20; pdf.add_text(72,y,"Words:",'F2',11,0.1); y-=20
        pdf.add_text(72,y,"  ".join(story['words']),'F3',10,0.2)
        y-=40; pdf.add_text(72,y,"What quality of this woman inspires you most?",'F4',10,0.3)
        for _ in range(3): y-=22; pdf.add_line(72,y,540,y,0.5,0.6)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"DRAW {story['character'].upper()}!",'F2',16,0)
        pdf.add_text(72,720,f"Draw {story['character']} showing courage:",'F4',11,0.2)
        pdf.add_rect(72,300,468,400,1.5,0.3)
        pdf.add_centered_text(280,f"I CAN BE LIKE {story['character'].upper()} BY...",'F2',11,0.1)
        y=250
        for _ in range(4): pdf.add_line(72,y,540,y,0.5,0.6); y-=22


    # Quiz (2 pages)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 1",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    qs=[("1. Who was the first woman God created?","a) Sarah  b) Eve  c) Mary"),
        ("2. How old was Sarah when Isaac was born?","a) 30  b) 60  c) 90"),
        ("3. Who watched baby Moses in the basket?","a) Miriam  b) Hannah  c) Ruth"),
        ("4. Deborah judged Israel under a ___","a) Oak tree  b) Palm tree  c) Fig tree"),
        ("5. Who said 'Where you go, I will go'?","a) Esther  b) Mary  c) Ruth")]
    y=700
    for q,o in qs: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 2",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    qs2=[("6. Hannah prayed for a ___","a) Daughter  b) Son  c) House"),
         ("7. Esther was queen of which empire?","a) Rome  b) Persia  c) Egypt"),
         ("8. Who said 'Be it unto me according to your word'?","a) Ruth  b) Esther  c) Mary"),
         ("9. Who sat at Jesus' feet to learn?","a) Martha  b) Mary  c) Priscilla"),
         ("10. Priscilla taught which preacher?","a) Paul  b) Peter  c) Apollos")]
    y=700
    for q,o in qs2: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.add_text(72,y-20,"Answers: 1b, 2c, 3a, 4b, 5c, 6b, 7b, 8c, 9b, 10c",'F3',9,0.4)

    # Vocabulary
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"VOCABULARY & WORD LIST",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    vocab=[("Prophetess","A woman who speaks God's messages"),("Matriarch","A respected female leader of a family"),
           ("Courage","Doing the right thing even when afraid"),("Devotion","Deep love and commitment"),
           ("Wisdom","Using knowledge in the best way"),("Grace","Undeserved kindness and favor"),
           ("Intercession","Praying on behalf of others"),("Redemption","Being rescued from trouble"),
           ("Legacy","What you leave behind for future generations"),("Virtue","Moral excellence and goodness")]
    y=710
    for w,d in vocab: pdf.add_text(72,y,f"{w}:",'F2',11,0.1); pdf.add_text(200,y,d,'F4',10,0.2); y-=28

    prompts=["A woman I admire and want to be like...","How I can show courage this week...",
             "A time I stood up for what was right...","My prayer for strength and wisdom..."]
    for j in range(4):
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"MY FAITH JOURNAL - Page {j+1}",'F2',16,0)
        pdf.add_text(72,710,prompts[j],'F5',12,0.2); y=680
        for _ in range(24): pdf.add_line(72,y,540,y,0.5,0.7); y-=25

    pdf.new_page(); pc+=1
    pdf.add_rect(50,50,512,692,3,0.2); pdf.add_rect(60,60,492,672,1.5,0.4)
    pdf.add_centered_text(680,"CERTIFICATE OF COMPLETION",'F2',22,0)
    pdf.add_centered_text(640,"This certifies that",'F4',14,0.2)
    pdf.add_line(180,600,432,600,1,0.3)
    pdf.add_centered_text(540,"has studied all 10 amazing women in",'F4',12,0.2)
    pdf.add_centered_text(510,TITLE,'F2',14,0)
    pdf.add_centered_text(400,"Date: _______________",'F4',12,0.3)
    pdf.add_centered_text(280,"\"She is clothed with strength and dignity\" - Proverbs 31:25",'F5',13,0.1)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS",'F2',18,0); y=690
    for i,s in enumerate(stories[:5]):
        pdf.add_rect(72,y-55,468,55,1,0.3)
        pdf.add_text(80,y-15,f"Card {i+1}: {s['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,s['verse'],'F4',9,0.2); y-=65
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS (continued)",'F2',18,0); y=700
    for i,s in enumerate(stories[5:]):
        pdf.add_rect(72,y-55,468,55,1,0.3)
        pdf.add_text(80,y-15,f"Card {i+6}: {s['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,s['verse'],'F4',9,0.2); y-=65

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MY ROLE MODEL PROFILE",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    pdf.add_text(72,710,"Choose your favorite woman from this book and create her profile:",'F4',11,0.2)
    y=680
    fields=["Name:","Her greatest quality:","The challenge she faced:","How she showed faith:",
            "What I admire most:","How I will be like her:","My prayer to be more like her:"]
    for f in fields:
        pdf.add_text(72,y,f,'F2',10,0.1); pdf.add_line(220,y-2,540,y-2,0.5,0.6); y-=35

    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),FILENAME)
    pdf.save(out)
    print(f"Generated {FILENAME} with {pc} pages")
    return pc

if __name__=="__main__":
    build_pdf()
