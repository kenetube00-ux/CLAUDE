#!/usr/bin/env python3
"""Book 282 - When Kids Pray: 10 Bible Stories About the Power of Prayer"""
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc
random.seed(282)
TITLE = "WHEN KIDS PRAY"
SUBTITLE = "10 Bible Stories About the Power of Prayer"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book282_Kids_Prayer_Stories.pdf"
stories = [
    {"title": "Hannah's Tearful Prayer", "character": "Hannah",
     "verse": "I prayed for this child, and the LORD granted my petition. - 1 Samuel 1:27 (WEB)",
     "moral": "Pray with all your heart - God hears every tear and every whisper!",
     "prayer_type": "Prayer of Desperation - Pouring out your deepest needs to God",
     "p1": "Year after year, Hannah went to the temple with a heavy heart. She longed for a baby more than anything in the world, but God had not given her one. Another woman constantly mocked her about it, making her feel worthless. Hannah was so heartbroken she could barely eat. Each year at the temple festival, while everyone else celebrated, Hannah sat weeping with an empty ache in her soul.",
     "p2": "One year, Hannah could not contain her pain any longer. She fell to her knees in the temple and poured out her entire soul to God in the most intense, passionate prayer of her life. Tears streamed down her face. Her lips moved but no sound came out - she was praying from a place deeper than words. She made a bold promise: if God gave her a son, she would dedicate him to God's service for his entire life.",
     "p3": "The priest Eli saw her and initially thought she was drunk, but Hannah explained she was pouring out her anguish to God. Eli blessed her and said, 'May God grant your request.' Peace flooded Hannah's heart for the first time in years. God remembered Hannah and gave her a son - Samuel - who became one of the greatest prophets in Israel's history! Hannah's desperate, tearful prayer moved the heart of God and changed a nation forever.",
     "words": ["HANNAH", "PRAYER", "TEARS", "SAMUEL", "TEMPLE", "HEART", "ANSWER", "FAITH"]},
    {"title": "Solomon Asks for Wisdom", "character": "Solomon",
     "verse": "Give your servant an understanding heart to judge your people. - 1 Kings 3:9 (WEB)",
     "moral": "Ask God for wisdom instead of stuff - it's the best gift ever!",
     "prayer_type": "Prayer for Wisdom - Asking God for what you truly need, not just what you want",
     "p1": "Young King Solomon had just become ruler of all Israel after his father David died. He was overwhelmed by the enormous responsibility. One night, God appeared to Solomon in a dream and made an incredible offer: 'Ask for whatever you want, and I will give it to you.' Imagine - ANYTHING in the universe! Solomon could have asked for riches, long life, victory over enemies, or ultimate power.",
     "p2": "But Solomon did not ask for money, fame, or power. Instead, he humbly admitted that he felt like a small child who did not know how to lead such a great nation. He asked God for one thing: 'Give me an understanding heart to judge your people, that I may discern between good and evil.' He wanted WISDOM - the ability to make right decisions and lead justly. Of all the things in the universe, Solomon chose the one thing that would help everyone, not just himself.",
     "p3": "God was so pleased with Solomon's unselfish request that He gave him not only incredible wisdom beyond any person who ever lived, but ALSO the riches and honor he did not ask for! Solomon became the wisest man in history - people traveled from distant lands just to hear him speak. God said, 'Because you asked for wisdom instead of selfish things, I will give you everything.' When we pray unselfishly for what truly matters, God often gives us far more than we asked for!",
     "words": ["SOLOMON", "WISDOM", "DREAM", "KING", "HEART", "JUDGE", "ASK", "GIFT"]},

    {"title": "Elijah's Mountain Prayer", "character": "Elijah",
     "verse": "The effective prayer of a righteous man has great power. - James 5:16 (WEB)",
     "moral": "One sincere prayer is more powerful than hours of empty words!",
     "prayer_type": "Prayer of Faith - Praying with bold confidence that God will act",
     "p1": "After 450 prophets of Baal had exhausted themselves trying to call down fire, it was Elijah's turn. The entire nation watched from Mount Carmel. Elijah calmly rebuilt God's broken altar with twelve stones representing the twelve tribes of Israel. He arranged the wood and sacrifice carefully. Then he did something that made everyone gasp - he drenched everything with twelve huge jars of water!",
     "p2": "Water ran down the altar, soaked the wood and sacrifice, and filled the trench around it completely. By human standards, there was ZERO chance of fire now. The 450 prophets had screamed and danced all day. But Elijah? He simply stepped forward, lifted his face to heaven, and prayed one short, simple prayer. No screaming. No dancing. No drama. Just faith-filled words from a righteous heart directly to the living God.",
     "p3": "The moment Elijah said 'Amen,' fire EXPLODED from heaven! Not ordinary fire - supernatural flames that consumed the soaking wet sacrifice, the drenched wood, the stones of the altar, the dirt, and even evaporated every drop of water in the trench! The people fell on their faces crying 'The LORD is God!' One quiet prayer from one faithful man accomplished what 450 screamers could not. God does not measure prayers by volume or length, but by the faith behind them.",
     "words": ["ELIJAH", "FIRE", "PRAYER", "ALTAR", "HEAVEN", "FAITH", "POWER", "SHORT"]},
    {"title": "Hezekiah Prays for Healing", "character": "Hezekiah",
     "verse": "I have heard your prayer. I have seen your tears. I will heal you. - 2 Kings 20:5 (WEB)",
     "moral": "God sees your tears and hears your desperate prayers for help!",
     "prayer_type": "Prayer for Healing - Bringing your pain and sickness to God",
     "p1": "King Hezekiah was deathly ill. The prophet Isaiah delivered a devastating message from God: 'Set your affairs in order, because you are going to die. You will not recover from this illness.' Imagine hearing that! Hezekiah was a good king who loved God. He was heartbroken. He turned his face to the wall and wept bitterly, pouring out his heart to God in his darkest hour.",
     "p2": "Lying in bed, too sick to even stand, Hezekiah prayed through his tears: 'Remember, LORD, how I have walked before you faithfully and with complete devotion. I have done what is good in your eyes.' His prayer was not demanding or entitled - it was the honest cry of a faithful servant who was not ready to leave the world yet. Tears soaked his pillow as he pleaded with God for more time.",
     "p3": "God heard every word and saw every tear! Before Isaiah even left the palace courtyard, God told him to go back with an incredible new message: 'I have heard your prayer. I have SEEN your tears. I WILL heal you! I am adding fifteen years to your life!' Hezekiah's illness was completely reversed. God literally changed His stated plan because of one man's heartfelt prayer! Our tears are not wasted - God collects every one and responds to our desperate cries with compassion.",
     "words": ["HEZEKIAH", "HEAL", "TEARS", "FIFTEEN", "PRAYER", "SICK", "HOPE", "LIVE"]},
    {"title": "Daniel's Disciplined Prayer", "character": "Daniel",
     "verse": "He knelt on his knees three times a day, and prayed. - Daniel 6:10 (WEB)",
     "moral": "Make prayer a daily habit that NOTHING can stop!",
     "prayer_type": "Prayer of Discipline - Making prayer a non-negotiable daily habit",
     "p1": "Daniel had a prayer habit that never changed for decades. Three times every single day - morning, noon, and evening - he knelt before his open window facing Jerusalem and prayed. Rain or shine. Busy or free. Young or old. Whether he felt like it or not, Daniel kept his appointment with God. This discipline built such a deep relationship with God that Daniel received visions of the future itself.",
     "p2": "When jealous officials convinced the king to ban all prayer for thirty days, Daniel faced a terrible choice: stop praying and stay safe, or keep praying and face the lions' den. For Daniel, there was no choice at all. He went to his window at the regular time and knelt down, just as he always did. He did not pray quietly in a closet or skip a day. He prayed openly because his relationship with God was worth more than his life.",
     "p3": "Daniel was arrested and thrown to the lions, but God protected him all night. His faithful prayer habit did not just save him - it saved the nation! The king saw God's power and declared that everyone must respect Daniel's God. Daniel's disciplined prayer life produced: wisdom beyond compare, supernatural protection, divine revelations, influence over kings, and a legacy remembered forever. Daily prayer is not a burden - it is the source of supernatural power for your entire life!",
     "words": ["DANIEL", "THREE", "DAILY", "KNEEL", "WINDOW", "HABIT", "LIONS", "POWER"]},

    {"title": "Jonah's Underwater Prayer", "character": "Jonah",
     "verse": "Out of the belly of Sheol I cried, and you heard my voice. - Jonah 2:2 (WEB)",
     "moral": "It is never too late to pray - God hears you from ANY place!",
     "prayer_type": "Prayer of Repentance - Saying sorry and turning back to God",
     "p1": "Jonah had run from God, been thrown into the sea, and was now inside the belly of an enormous fish! Seaweed wrapped around his head. Darkness surrounded him completely. He was in the most impossible place any person had ever prayed from. The digestive sounds of the great fish echoed around him. He had hit absolute rock bottom - literally at the bottom of the ocean inside a fish.",
     "p2": "In that dark, terrifying place, Jonah finally stopped running and started praying. His prayer from inside the fish is one of the most beautiful in the Bible. He admitted he had been running from God. He acknowledged that God had saved his life even when he didn't deserve it. He declared that he would keep his promises to God. From the depths of the sea, from inside a fish, Jonah's voice reached the throne of heaven.",
     "p3": "God heard Jonah's prayer from that impossible place! He commanded the fish to swim toward shore and vomit Jonah out onto dry land. The man who had run from God was given a complete second chance. Jonah's story teaches us that no matter how far you have run from God, no matter how deep a mess you are in, it is NEVER too late to pray. There is no place so dark that your prayer cannot reach God's ears. He is always ready to hear a repentant heart.",
     "words": ["JONAH", "FISH", "DEEP", "SORRY", "SECOND", "CHANCE", "HEAR", "PRAYER"]},
    {"title": "Jesus in Gethsemane", "character": "Jesus",
     "verse": "Not my will, but yours, be done. - Luke 22:42 (WEB)",
     "moral": "The hardest but most powerful prayer is 'Your will be done, God'!",
     "prayer_type": "Prayer of Surrender - Giving your will to God even when it's painful",
     "p1": "The night before His crucifixion, Jesus went to a garden called Gethsemane to pray. He knew exactly what was coming - arrest, torture, and death on a cross. He brought His closest friends Peter, James, and John, asking them to pray with Him. Then Jesus walked a little further, fell to the ground, and began to pray with an intensity no human has ever matched.",
     "p2": "Jesus' anguish was so great that His sweat fell like drops of blood. He cried out to His Father: 'If it is possible, let this cup pass from me!' He was asking if there was ANY other way to save the world without the cross. He prayed this three times, each time more intensely. His three friends kept falling asleep while Jesus wrestled in prayer alone. An angel from heaven came to strengthen Him.",
     "p3": "Finally, Jesus prayed the most powerful words ever spoken: 'Nevertheless, not MY will, but YOUR will be done.' He surrendered completely to God's plan even though it meant suffering and death. This prayer of surrender is the model for all prayer - telling God what we want, but ultimately trusting His plan above our own wishes. Jesus' surrender in Gethsemane led to the salvation of the entire world. Sometimes saying 'Your will be done' takes more courage than any other prayer.",
     "words": ["JESUS", "GARDEN", "NIGHT", "SWEAT", "WILL", "FATHER", "SURRENDER", "TRUST"]},
    {"title": "Peter's Prison Prayer Chain", "character": "the church",
     "verse": "Constant prayer was made by the church to God for him. - Acts 12:5 (WEB)",
     "moral": "When we pray together, amazing things happen!",
     "prayer_type": "Prayer of Unity - Praying together with others for a common need",
     "p1": "Peter was locked in maximum security prison, chained between two soldiers with guards at every door. King Herod planned to execute him the next morning. The situation seemed completely hopeless - no human rescue was possible. But the church had a secret weapon more powerful than any army: PRAYER. Believers gathered in homes across the city and prayed non-stop through the night for Peter's life.",
     "p2": "All night long, groups of Christians prayed together with desperate faith. Men, women, and children lifted their voices to God, crying out for Peter's deliverance. They did not know HOW God could save him from such an impossible situation, but they prayed anyway. The Bible says their prayer was 'constant' and 'earnest' - not casual or half-hearted. They meant every word and they prayed together as one body.",
     "p3": "While they prayed, God answered in spectacular fashion! An angel appeared in Peter's cell, woke him up, broke his chains, and led him past every guard and through locked gates that opened by themselves! When Peter showed up at the prayer meeting, they were so shocked they could barely believe it. Sometimes our prayers are answered so powerfully that we can hardly believe it ourselves! United prayer moves the hand of God in ways that individual prayer cannot.",
     "words": ["CHURCH", "TOGETHER", "PRAYER", "NIGHT", "UNITED", "ANGEL", "CHAINS", "FREE"]},

    {"title": "Paul and Silas Sing in Prison", "character": "Paul and Silas",
     "verse": "About midnight Paul and Silas were praying and singing. - Acts 16:25 (WEB)",
     "moral": "Praise God even in your darkest moments - miracles follow worship!",
     "prayer_type": "Prayer of Praise - Worshiping God even when life is terrible",
     "p1": "Paul and Silas had been arrested for preaching the gospel, stripped, severely beaten with rods, and thrown into the deepest, darkest inner cell of the prison. Their backs were bloody and raw. Their feet were locked in painful wooden stocks. It was midnight, pitch black, and they were in agony. By any human standard, this was the worst possible situation to worship.",
     "p2": "But at midnight - the DARKEST hour - Paul and Silas did something shocking. Instead of crying, complaining, or giving up, they began PRAYING and SINGING hymns to God! Their praise echoed through the dark prison halls. Other prisoners stopped and listened in amazement. Who could possibly sing in such pain and darkness? Their worship was not because life was good - it was because GOD is good, regardless of circumstances.",
     "p3": "Suddenly a massive earthquake shook the foundations of the prison! Every door flew open! Every chain fell off every prisoner! The jailer was about to kill himself in despair when Paul called out that everyone was still there. The amazed jailer asked, 'What must I do to be saved?' That night the jailer and his entire family believed in Jesus and were baptized! Paul and Silas' midnight worship in chains led to an earthquake of salvation. When you praise God in your darkest hour, the ground shakes!",
     "words": ["SING", "PRISON", "MIDNIGHT", "PRAISE", "QUAKE", "CHAINS", "WORSHIP", "JOY"]},
    {"title": "The Lord's Prayer - Jesus Teaches Us", "character": "Jesus",
     "verse": "When you pray, say: Our Father, who is in heaven. - Luke 11:2 (WEB)",
     "moral": "Jesus gave us the perfect pattern for how to pray every day!",
     "prayer_type": "The Model Prayer - Jesus' template showing us how to pray about everything",
     "p1": "One day Jesus' disciples watched Him pray and were amazed at His intimate connection with God. When He finished, they asked, 'Lord, teach US to pray!' Jesus did not give them a complicated formula or long ritual. Instead He taught them a simple, beautiful prayer that covers everything a person could ever need. It became the most famous prayer in all of history - The Lord's Prayer.",
     "p2": "Jesus taught them to begin with 'Our Father in heaven, hallowed be Your name.' Start by recognizing WHO you are talking to - your loving Father whose name is holy. Then 'Your kingdom come, Your will be done on earth as it is in heaven' - put God's plans first! Then 'Give us today our daily bread' - ask for your needs. 'Forgive us as we forgive others' - keep relationships clean. 'Lead us not into temptation, deliver us from evil' - ask for protection.",
     "p3": "This simple prayer contains EVERYTHING: worship (hallowed be Your name), submission (Your will be done), provision (daily bread), forgiveness (forgive us), and protection (deliver us from evil). Jesus showed that prayer does not need fancy words or long speeches. It needs a genuine heart talking to a loving Father. Whether you pray for five minutes or five hours, following Jesus' pattern ensures you cover every area of your spiritual life. This is how the Master Himself taught us to pray!",
     "words": ["FATHER", "HEAVEN", "DAILY", "BREAD", "FORGIVE", "KINGDOM", "LORD", "TEACH"]}
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
    pdf.add_centered_text(720,TITLE,'F2',28,0); pdf.add_centered_text(690,SUBTITLE,'F4',14,0.2)
    pdf.add_centered_text(660,"Written and Illustrated by",'F4',12,0.3)
    pdf.add_centered_text(640,AUTHOR,'F2',16,0)
    pdf.add_rect(100,200,412,380,2,0.3)
    pdf.add_centered_text(420,"[ILLUSTRATION: Children and Bible heroes praying",'F3',10,0.4)
    pdf.add_centered_text(405,"with golden light representing answered prayers]",'F3',10,0.4)
    pdf.add_centered_text(100,"Discover the incredible power of talking to God!",'F4',12,0.3)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(700,TITLE,'F2',16,0)
    pdf.add_text(72,600,f"Written by {AUTHOR}",'F4',11,0.2)
    pdf.add_text(72,580,"Copyright 2025. All Rights Reserved.",'F4',10,0.3)
    pdf.add_text(72,550,"Scripture: World English Bible (WEB) - Public Domain.",'F4',10,0.3)
    pdf.add_text(72,520,"For children ages 6-12. Published by Kingdom Kids Publishing",'F4',10,0.3)
    pdf.add_text(72,440,"Dedication: For every child learning to talk to God - He ALWAYS listens!",'F4',10,0.2)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"TABLE OF CONTENTS",'F2',18,0); pdf.add_line(150,720,462,720,1,0.3); y=680
    for i,s in enumerate(stories): pdf.add_text(72,y,f"Prayer {i+1}: {s['title']}",'F4',12,0.1); y-=28
    pdf.add_text(72,y-10,"Quiz / Vocabulary / Prayer Journal / Certificate / Bonus",'F4',10,0.3)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"HOW TO USE THIS BOOK",'F2',18,0); pdf.add_line(150,720,462,720,1,0.3)
    intro=["Welcome, prayer warrior! Did you know that prayer is","the most POWERFUL thing a person can do?","",
        "Each story teaches a DIFFERENT TYPE of prayer:","Desperate prayer, Wisdom prayer, Faith prayer,",
        "Healing prayer, Disciplined prayer, Repentance prayer,","Surrender prayer, United prayer, Praise prayer, and Model prayer!","",
        "Each story has SIX pages including:","  - The story + Write Your Own Prayer section","  - Word search + Drawing page","",
        "By the end you will know 10 different ways to pray!","",
        "Ready to become a prayer warrior? Let's begin!"]
    y=680
    for l in intro: pdf.add_text(72,y,l,'F4',11,0.15); y-=22
    for idx, story in enumerate(stories):
        pdf.new_page(); pc+=1
        pdf.add_filled_rect(50,700,512,60,0.88)
        pdf.add_centered_text(735,f"Prayer Story {idx+1}",'F1',10,0.4)
        pdf.add_centered_text(715,story['title'].upper(),'F2',18,0)
        pdf.add_rect(100,400,412,270,1.5,0.3)
        pdf.add_centered_text(560,f"[ILLUSTRATION: {story['character']} praying",'F3',9,0.4)
        pdf.add_centered_text(545,"with divine light surrounding them]",'F3',9,0.4)
        for i,line in enumerate(wrap_text(story['p1'],80)): pdf.add_text(72,370-i*18,line,'F4',11,0.1)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (continued)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(story['p2'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        pdf.add_rect(100,y-260,412,240,1.5,0.3)
        pdf.add_centered_text(y-120,f"[ILLUSTRATION: {story['character']} deep in prayer]",'F3',9,0.4)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (God answers!)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(story['p3'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=12
        pdf.add_filled_rect(72,y-30,468,40,0.9)
        pdf.add_centered_text(y-5,"KEY BIBLE VERSE:",'F2',10,0.2)
        pdf.add_centered_text(y-22,story['verse'],'F4',10,0)
        y-=50
        pdf.add_rect(72,y-45,468,50,2,0.2)
        pdf.add_text(80,y-10,"PRAYER TYPE:",'F2',10,0.1)
        pdf.add_text(80,y-30,story['prayer_type'],'F4',10,0.2)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"REFLECTION & MY PRAYER",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        qs=["1. What did this person pray for?","2. How did God answer their prayer?",
            "3. What do I want to pray for today?"]
        y=700
        for q in qs:
            pdf.add_text(72,y,q,'F2',11,0.1); y-=20
            for _ in range(3): pdf.add_line(90,y,530,y,0.5,0.6); y-=20
            y-=8
        pdf.add_filled_rect(72,y-130,468,140,0.92)
        pdf.add_centered_text(y-5,"WRITE YOUR OWN PRAYER",'F2',14,0.1)
        pdf.add_text(80,y-22,f"Using the style of {story['prayer_type'].split(' - ')[0]}:",'F4',10,0.2)
        for i in range(6): pdf.add_line(80,y-45-i*18,520,y-45-i*18,0.5,0.6)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"WORD SEARCH PUZZLE",'F2',16,0)
        pdf.add_text(72,720,f"Find words from: {story['title']}",'F4',11,0.2)
        grid=generate_word_search(story['words']); y=680
        for row in grid: pdf.add_centered_text(y,"   ".join(row),'F3',14,0.1); y-=24
        y-=20; pdf.add_text(72,y,"Words:",'F2',11,0.1); y-=20
        pdf.add_text(72,y,"  ".join(story['words']),'F3',10,0.2)
        y-=40; pdf.add_text(72,y,"Write a one-sentence prayer using these words:",'F4',10,0.3)
        for _ in range(2): y-=22; pdf.add_line(72,y,540,y,0.5,0.6)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"DRAW & PRAY",'F2',16,0)
        pdf.add_text(72,720,f"Draw {story['character']} praying:",'F4',11,0.2)
        pdf.add_rect(72,300,468,400,1.5,0.3)
        pdf.add_centered_text(280,"Something I want to pray about today:",'F2',11,0.1)
        y=250
        for _ in range(4): pdf.add_line(72,y,540,y,0.5,0.6); y-=22


    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 1",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs=[("1. What did Hannah pray for?","a) Money  b) A son  c) Health"),
        ("2. What did Solomon ask God for?","a) Gold  b) Power  c) Wisdom"),
        ("3. How many jars of water did Elijah pour?","a) 4  b) 8  c) 12"),
        ("4. How many years did God add to Hezekiah?","a) 5  b) 15  c) 25"),
        ("5. How many times a day did Daniel pray?","a) 1  b) 3  c) 7")]
    y=700
    for q,o in qs: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 2",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs2=[("6. Where did Jonah pray from?","a) Temple  b) Inside fish  c) Mountain"),
         ("7. Where did Jesus pray before the cross?","a) Temple  b) Gethsemane  c) Mount Sinai"),
         ("8. What happened when the church prayed for Peter?","a) Nothing  b) Angel freed him  c) Earthquake"),
         ("9. What did Paul and Silas do at midnight?","a) Slept  b) Cried  c) Sang"),
         ("10. The Lord's Prayer starts with...","a) Dear God  b) Our Father  c) Help me")]
    y=700
    for q,o in qs2: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.add_text(72,y-20,"Answers: 1b, 2c, 3c, 4b, 5b, 6b, 7b, 8b, 9c, 10b",'F3',9,0.4)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"VOCABULARY & WORD LIST",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    vocab=[("Petition","A formal request made to God in prayer"),("Intercession","Praying on behalf of someone else"),
           ("Supplication","Humbly asking God for what you need"),("Repentance","Turning from sin back to God"),
           ("Surrender","Giving control to God completely"),("Worship","Expressing love and honor to God"),
           ("Discipline","Regular practice of spiritual habits"),("Thanksgiving","Expressing gratitude to God"),
           ("Confession","Admitting wrongs to God honestly"),("Amen","So be it - agreement with prayer")]
    y=710
    for w,d in vocab: pdf.add_text(72,y,f"{w}:",'F2',11,0.1); pdf.add_text(200,y,d,'F4',10,0.2); y-=28
    prompts=["My prayer for my family today...","Something I need to say sorry to God about...",
             "What I am thankful for right now...","My biggest prayer request this week..."]
    for j in range(4):
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"MY PRAYER JOURNAL - Page {j+1}",'F2',16,0)
        pdf.add_text(72,710,prompts[j],'F5',12,0.2); y=680
        for _ in range(24): pdf.add_line(72,y,540,y,0.5,0.7); y-=25
    pdf.new_page(); pc+=1
    pdf.add_rect(50,50,512,692,3,0.2); pdf.add_rect(60,60,492,672,1.5,0.4)
    pdf.add_centered_text(680,"CERTIFICATE OF COMPLETION",'F2',22,0)
    pdf.add_centered_text(640,"This certifies that",'F4',14,0.2)
    pdf.add_line(180,600,432,600,1,0.3)
    pdf.add_centered_text(540,"has completed all 10 prayer stories in",'F4',12,0.2)
    pdf.add_centered_text(510,TITLE,'F2',16,0)
    pdf.add_centered_text(400,"Date: _______________",'F4',12,0.3)
    pdf.add_centered_text(280,"\"Pray without ceasing\" - 1 Thessalonians 5:17",'F5',14,0.1)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS",'F2',18,0); y=690
    for i,s in enumerate(stories[:5]):
        pdf.add_rect(72,y-55,468,55,1,0.3); pdf.add_text(80,y-15,f"Card {i+1}: {s['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,s['verse'],'F4',9,0.2); y-=65
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS (cont.)",'F2',18,0); y=700
    for i,s in enumerate(stories[5:]):
        pdf.add_rect(72,y-55,468,55,1,0.3); pdf.add_text(80,y-15,f"Card {i+6}: {s['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,s['verse'],'F4',9,0.2); y-=65
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MY 10-DAY PRAYER CHALLENGE",'F2',18,0)
    pdf.add_text(72,710,"Try a different prayer type each day for 10 days!",'F4',11,0.2); y=680
    for i,s in enumerate(stories):
        pdf.add_text(72,y,f"Day {i+1}: {s['prayer_type'].split(' - ')[0]}",'F2',9,0.1)
        pdf.add_rect(520,y-3,15,15,0.5,0.3); y-=28
    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),FILENAME)
    pdf.save(out); print(f"Generated {FILENAME} with {pc} pages"); return pc
if __name__=="__main__": build_pdf()
