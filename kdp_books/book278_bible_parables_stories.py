#!/usr/bin/env python3
"""Book 278 - Stories Jesus Told: 10 Parables Every Kid Should Know"""
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc
random.seed(278)
TITLE = "STORIES JESUS TOLD"
SUBTITLE = "10 Parables Every Kid Should Know"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book278_Jesus_Parables_Kids.pdf"
stories = [
    {"title": "The Good Samaritan", "character": "the Samaritan",
     "verse": "Love your neighbor as yourself. - Luke 10:27 (WEB)",
     "moral": "A true neighbor helps anyone in need, regardless of differences!",
     "modern": "Helping a new kid at school who looks different from you or has no friends.",
     "p1": "One day a man asked Jesus, 'Who is my neighbor?' Jesus answered with a story. A man was traveling from Jerusalem to Jericho along a dangerous, winding road through rocky hills. Suddenly, robbers jumped out and attacked him! They took everything he had, beat him badly, and left him lying half-dead on the dusty road.",
     "p2": "A priest came walking down the same road and saw the injured man bleeding on the ground. Instead of helping, he crossed to the other side and hurried past. Then a Levite, a religious teacher, came along. He also looked at the hurt man, but walked away without helping. Both of these men were supposed to be holy and good, yet they ignored someone who desperately needed their compassion and care.",
     "p3": "Then a Samaritan man came along - someone from a group that was hated and despised by the injured man's people. But the Samaritan felt deep compassion. He bandaged the man's wounds, put him on his own donkey, and took him to an inn. He paid for the man's care and promised to cover any extra costs. Jesus asked, 'Which one was the true neighbor?' The answer was clear - the one who showed mercy. Jesus said, 'Go and do the same.'",
     "words": ["NEIGHBOR", "HELP", "MERCY", "KINDNESS", "LOVE", "ROAD", "CARE", "GOOD"]},
    {"title": "The Prodigal Son", "character": "the father",
     "verse": "This my son was dead and is alive again; was lost and is found. - Luke 15:24 (WEB)",
     "moral": "God welcomes us back with open arms when we return to Him!",
     "modern": "When you mess up badly and your parents still love you and forgive you.",
     "p1": "Jesus told of a man with two sons. The younger son demanded his share of the family's money right away - which was terribly disrespectful. The heartbroken father gave him what he asked for. The young man packed everything and traveled to a far country where no one knew him. He wasted all his money on foolish living and wild parties.",
     "p2": "Soon his money was completely gone. Then a terrible famine struck the land and he had nothing to eat. He was so desperate he took a job feeding pigs - the lowest, most shameful work for a Jewish person. He was so hungry he wanted to eat the pig food, but no one gave him anything. Sitting in the mud surrounded by pigs, he finally came to his senses and remembered his father's kindness.",
     "p3": "The young man decided to go home and beg his father to hire him as a servant. But while he was still far away, his father saw him and ran toward him with arms wide open! The father hugged him, kissed him, and threw a huge celebration party. He put the finest robe on him, a ring on his finger, and sandals on his feet. His father said, 'My son was lost and now is found!' God celebrates the same way when anyone returns to Him.",
     "words": ["FATHER", "SON", "LOST", "FOUND", "FORGIVE", "HOME", "LOVE", "RETURN"]},

    {"title": "The Lost Sheep", "character": "the shepherd",
     "verse": "There will be more joy in heaven over one sinner who repents. - Luke 15:7 (WEB)",
     "moral": "Every single person matters so much to God that He will search until He finds them!",
     "modern": "A teacher who notices when one student is missing or sad and goes to check on them.",
     "p1": "Jesus asked the crowd a simple question: If a shepherd has one hundred sheep and loses just one, what does he do? Does he say, 'Oh well, I still have ninety-nine'? No! A good shepherd notices that one sheep is missing. He knows each one by name. His heart breaks when even one is lost and alone in the dangerous wilderness.",
     "p2": "The shepherd leaves the ninety-nine sheep in a safe place and goes searching for the one lost sheep. He climbs over rocky hills, pushes through thorny bushes, and calls out through dark valleys. The search might take hours. He does not give up, even when his feet hurt and his clothes are torn. He keeps calling, keeps looking, keeps searching because that one sheep matters to him deeply.",
     "p3": "Finally, the shepherd hears a faint bleating cry! He finds the frightened sheep caught in thorns, cold and scared. With great joy, he gently lifts it onto his shoulders and carries it all the way home. Then he calls all his friends and neighbors saying, 'Celebrate with me! I found my lost sheep!' Jesus said that heaven celebrates even MORE when one lost person returns to God. YOU are that precious to Him.",
     "words": ["SHEEP", "LOST", "FOUND", "SEARCH", "SHEPHERD", "JOY", "CARRY", "LOVE"]},
    {"title": "The Sower and the Seeds", "character": "the farmer",
     "verse": "The seed is the word of God. - Luke 8:11 (WEB)",
     "moral": "Prepare your heart to receive God's word like good, rich soil!",
     "modern": "Paying attention in class vs. daydreaming - only attentive hearts grow wisdom.",
     "p1": "Jesus told about a farmer who went out to scatter seeds across his land. As he walked along, throwing handfuls of seeds, they landed on four different types of ground. Some seeds fell on the hard path where people walked. Birds swooped down immediately and gobbled them up before they could even begin to grow. Those seeds never had a chance.",
     "p2": "Some seeds fell on rocky ground with only a thin layer of soil. They sprouted quickly but had no deep roots. When the hot sun blazed down, the little plants withered and died. Other seeds fell among thorny weeds. They started growing but the thorns grew faster, choking the good plants until they produced nothing. Three types of ground - three types of failure.",
     "p3": "But some seeds fell on good, rich, deep soil. These seeds put down strong roots, grew tall and healthy, and produced an amazing harvest - thirty, sixty, even a hundred times what was planted! Jesus explained that the seed is God's Word and the soil represents our hearts. Some people ignore God's message, some believe briefly but quit when life gets hard. But those with good hearts who really listen and obey will produce incredible fruit in their lives!",
     "words": ["SEED", "SOIL", "GROW", "HEART", "WORD", "FRUIT", "ROOTS", "HARVEST"]},
    {"title": "The Wise and Foolish Builders", "character": "the wise builder",
     "verse": "Everyone who hears these words and does them is like a wise man. - Matthew 7:24 (WEB)",
     "moral": "Build your life on God's truth and nothing can knock you down!",
     "modern": "Studying hard and building good habits vs. taking shortcuts that fall apart under pressure.",
     "p1": "Jesus finished a long sermon and told one final story everyone would remember. Two men each decided to build a house. The first man was wise - he searched carefully for the perfect spot and found solid rock to build upon. It took longer to dig down to the rock foundation. It was harder work. But the wise man knew a strong foundation was worth the extra effort.",
     "p2": "The second man was foolish and impatient. He wanted his house built quickly with no hard work. He found a nice flat stretch of sand and started building right away. His house went up fast! It looked great on the outside. The foolish man probably laughed at the wise man still working on his foundation. For a while, both houses looked equally fine standing side by side under clear blue skies.",
     "p3": "Then the storms came. Rain pounded down, floods rose up, and fierce winds howled against both houses. The house built on sand shifted, cracked, and CRASHED down into a pile of rubble! Nothing was left. But the house on the rock stood firm - not a single crack! Jesus said anyone who hears His words AND obeys them is like the wise builder. Build your life on God's truth and no storm in life can ever destroy you.",
     "words": ["ROCK", "SAND", "BUILD", "STORM", "WISE", "STRONG", "OBEY", "STAND"]},

    {"title": "The Mustard Seed", "character": "the gardener",
     "verse": "The kingdom of heaven is like a grain of mustard seed. - Matthew 13:31 (WEB)",
     "moral": "Small beginnings can lead to enormous, world-changing results!",
     "modern": "Being kind to one person can start a chain reaction that changes an entire school.",
     "p1": "Jesus held up something incredibly tiny between His fingers - a mustard seed! It was one of the smallest seeds in all the land, barely visible to the eye. The crowd leaned in close trying to see it. Jesus said the kingdom of heaven is like this tiny, insignificant-looking seed. Everyone must have wondered how something so small could represent anything important at all.",
     "p2": "But when that tiny seed is planted in good soil and given water and sunlight, something amazing happens. Day by day it grows bigger and bigger. It pushes through the dirt, reaches toward the sky, and keeps growing. Other seeds around it might be bigger at first, but the mustard plant outgrows them all. It spreads its branches wider and wider, stretching taller and taller until it becomes one of the largest plants in the garden.",
     "p3": "Eventually, the full-grown mustard plant becomes so large that birds come and build their nests in its branches! From the tiniest seed comes one of the biggest plants - a home and shelter for many. Jesus was teaching that faith starts small but grows incredibly powerful. Even faith as small as a mustard seed can move mountains! Never despise small beginnings - God can take your small act of faith and grow it into something that blesses the whole world.",
     "words": ["MUSTARD", "SEED", "SMALL", "GROW", "TREE", "FAITH", "BIRDS", "BIG"]},
    {"title": "The Hidden Treasure", "character": "the finder",
     "verse": "The kingdom of heaven is like treasure hidden in a field. - Matthew 13:44 (WEB)",
     "moral": "God's kingdom is worth giving up everything to have!",
     "modern": "Choosing to do the right thing even when it costs you popularity or convenience.",
     "p1": "Jesus told a short but powerful story. A man was working in a field one day - perhaps digging or plowing - when suddenly his tool struck something hard. He brushed away the dirt and discovered a chest full of the most magnificent treasure he had ever seen! Gold coins, precious jewels, and priceless objects gleamed in the sunlight. His heart raced with excitement.",
     "p2": "The man quickly covered the treasure back up and stood there thinking. This treasure was worth more than everything he owned combined. It was worth more than his house, his animals, his savings - everything! He knew he had to buy this field to own the treasure legally. But how? He had to sell everything he owned to afford the field. That would mean giving up his comfortable life completely.",
     "p3": "But the man was SO overjoyed at finding this treasure that he GLADLY sold everything he had without a moment of sadness! He ran to buy the field with a huge smile on his face. He was not sad about what he gave up because what he gained was infinitely more valuable. Jesus was saying that knowing God and being part of His kingdom is the greatest treasure in the universe - worth any sacrifice, worth giving up everything to have!",
     "words": ["TREASURE", "FIELD", "HIDDEN", "JOY", "VALUE", "FIND", "GOLD", "WORTH"]},
    {"title": "The Talents", "character": "the faithful servants",
     "verse": "Well done, good and faithful servant! - Matthew 25:21 (WEB)",
     "moral": "Use the gifts God gives you wisely - He trusts you with great responsibility!",
     "modern": "Using your skills and talents to help others instead of being lazy or hiding them.",
     "p1": "A wealthy master was going on a long journey and entrusted his fortune to three servants. To the first servant, he gave five talents of gold (an enormous amount of money). To the second, he gave two talents. To the third, he gave one talent. Each received according to their ability. Then the master departed on his trip, trusting them to be wise stewards.",
     "p2": "The servant with five talents immediately went to work - trading, investing, and building until he doubled his money to ten talents! The servant with two talents worked just as hard and also doubled his to four. But the third servant was afraid of failing. Instead of trying anything, he dug a hole in the ground and buried his one talent where it was safe but completely useless.",
     "p3": "When the master returned, he was thrilled with the first two servants. 'Well done, good and faithful servant!' he said to each, giving them even greater responsibilities. But to the servant who buried his talent, the master was deeply disappointed. 'You lazy servant! You could have at least put the money in the bank to earn interest!' He took the talent away and gave it to the one with ten. God gives us all different gifts and talents - He wants us to USE them boldly, not hide them in fear!",
     "words": ["TALENT", "INVEST", "DOUBLE", "FAITHFUL", "BOLD", "WORK", "GIFT", "USE"]},

    {"title": "The Wedding Feast", "character": "the king",
     "verse": "Many are called, but few are chosen. - Matthew 22:14 (WEB)",
     "moral": "God invites everyone to His celebration - don't miss out by making excuses!",
     "modern": "Being invited to an amazing party but saying no because you want to watch TV instead.",
     "p1": "A king prepared a magnificent wedding feast for his son - the most incredible celebration anyone could imagine! The finest food, beautiful decorations, and wonderful music were all prepared. He sent servants to invite the guests who had been chosen to attend. Everything was ready for the most joyous day of the kingdom.",
     "p2": "But the invited guests began making excuses! One said he had to check on his new field. Another had to test his new oxen. Another had just gotten married and was too busy. They all refused to come, treating the king's generous invitation as worthless. Some even mistreated the servants who brought the invitations! The king was furious and deeply hurt that his incredible celebration was being rejected.",
     "p3": "The king told his servants to go out into the streets, the highways, and the back alleys. They were to invite EVERYONE they found - poor and rich, good and bad, anyone who would come! The wedding hall was filled with grateful guests who could hardly believe they were invited to such a wonderful feast. Jesus was teaching that God invites everyone to His kingdom celebration. The question is not whether you are invited - it is whether you will accept the invitation or make excuses.",
     "words": ["FEAST", "INVITE", "PARTY", "KING", "COME", "JOY", "WELCOME", "READY"]},
    {"title": "The Unforgiving Servant", "character": "the king",
     "verse": "Forgive, and you will be forgiven. - Luke 6:37 (WEB)",
     "moral": "Since God forgives us so much, we must forgive others too!",
     "modern": "Being forgiven by your parents for something big, then refusing to forgive your friend for something tiny.",
     "p1": "A servant owed his king an enormous debt - ten thousand talents! That is MILLIONS of dollars in today's money - an amount he could never possibly repay in a hundred lifetimes. The king summoned him and ordered that he, his wife, and children be sold to pay the debt. The terrified servant fell on his knees and begged for patience, promising to repay everything.",
     "p2": "The king felt deep compassion for the servant and did something incredible - he completely forgave the ENTIRE enormous debt! Just like that, millions were wiped clean. The servant was free! He walked out of the palace a new man. But then he met a fellow servant who owed him a tiny amount - just a few dollars. The forgiven servant grabbed him by the throat and demanded immediate payment.",
     "p3": "The fellow servant begged for patience using almost the same words! But the first servant refused to show any mercy. He had the poor man thrown into prison over a tiny debt. When the king heard about this, he was furious. 'I forgave you millions and you cannot forgive a few dollars?' He called the wicked servant back and reversed his forgiveness. Jesus taught that God has forgiven us an enormous debt of sin - so we must freely forgive others their small offenses against us.",
     "words": ["FORGIVE", "MERCY", "DEBT", "FREE", "KING", "GRACE", "PARDON", "LOVE"]}
]


def generate_word_search(words):
    grid = [[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)] for _ in range(10)]
    for word in words[:8]:
        word = word.upper()
        for attempt in range(50):
            d = random.choice([(0,1),(1,0),(1,1)])
            r = random.randint(0, max(0, 9-len(word)*d[0]))
            c = random.randint(0, max(0, 9-len(word)*d[1]))
            if r+len(word)*d[0]>10 or c+len(word)*d[1]>10: continue
            for i,ch in enumerate(word): grid[r+i*d[0]][c+i*d[1]]=ch
            break
    return grid

def wrap_text(text, mx=75):
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
    # Title
    pdf.new_page(); pc+=1
    pdf.add_filled_rect(50,650,512,100,0.85)
    pdf.add_centered_text(720, TITLE, 'F2', 28, 0)
    pdf.add_centered_text(690, SUBTITLE, 'F4', 14, 0.2)
    pdf.add_centered_text(660, "Written and Illustrated by", 'F4', 12, 0.3)
    pdf.add_centered_text(640, AUTHOR, 'F2', 16, 0)
    pdf.add_rect(100,200,412,380,2,0.3)
    pdf.add_centered_text(420,"[ILLUSTRATION: Jesus sitting with children, telling stories", 'F3',10,0.4)
    pdf.add_centered_text(405,"while they listen with wonder and excitement]", 'F3',10,0.4)
    pdf.add_centered_text(100,"Discover the amazing stories Jesus told!", 'F4',12,0.3)
    # Copyright
    pdf.new_page(); pc+=1
    pdf.add_centered_text(700,TITLE,'F2',16,0)
    pdf.add_centered_text(670,SUBTITLE,'F4',11,0.2)
    pdf.add_text(72,600,f"Written by {AUTHOR}",'F4',11,0.2)
    pdf.add_text(72,580,"Copyright 2025. All Rights Reserved.",'F4',10,0.3)
    pdf.add_text(72,550,"Scripture quotations from the World English Bible (WEB) - Public Domain.",'F4',10,0.3)
    pdf.add_text(72,520,"Designed for children ages 6-12.",'F4',10,0.3)
    pdf.add_text(72,490,"Published by Kingdom Kids Publishing",'F4',10,0.3)
    pdf.add_text(72,460,"First Edition - 2025",'F4',10,0.3)
    pdf.add_text(72,410,"Dedication: To every child learning to listen to Jesus' stories.",'F4',11,0.2)
    # TOC
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"TABLE OF CONTENTS",'F2',18,0)
    pdf.add_line(150,720,462,720,1,0.3)
    y=680
    for i,s in enumerate(stories):
        pdf.add_text(72,y,f"Parable {i+1}: {s['title']}",'F4',12,0.1); y-=28
    pdf.add_text(72,y-10,"Quiz / Vocabulary / Faith Journal / Certificate / Bonus",'F4',10,0.3)
    # How to Use
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"HOW TO USE THIS BOOK",'F2',18,0)
    pdf.add_line(150,720,462,720,1,0.3)
    intro=["Welcome! Jesus was the greatest storyteller who ever lived!","",
        "He used simple stories called PARABLES to teach deep truths.","Each parable has a hidden meaning for your life today!","",
        "Each parable has SIX pages:","  1. The story begins (with illustration)",
        "  2. The story continues (with scene)","  3. The ending + verse + moral + modern example",
        "  4. Reflection questions + prayer","  5. Word search puzzle","  6. Draw the parable!","",
        "After all 10 parables you will find quizzes, vocabulary,","journal pages, and bonus activities!","",
        "Ready to hear what Jesus has to teach you? Let's go!"]
    y=680
    for l in intro: pdf.add_text(72,y,l,'F4',11,0.15); y-=22


    # Stories: 10 x 6 pages = 60
    for idx, story in enumerate(stories):
        # P1
        pdf.new_page(); pc+=1
        pdf.add_filled_rect(50,700,512,60,0.88)
        pdf.add_centered_text(735,f"Parable {idx+1}",'F1',10,0.4)
        pdf.add_centered_text(715,story['title'].upper(),'F2',18,0)
        pdf.add_rect(100,400,412,270,1.5,0.3)
        pdf.add_centered_text(560,f"[ILLUSTRATION: Scene from {story['title']}",'F3',9,0.4)
        pdf.add_centered_text(545,"with Jesus teaching the crowd]",'F3',9,0.4)
        for i,line in enumerate(wrap_text(story['p1'],80)):
            pdf.add_text(72,370-i*18,line,'F4',11,0.1)
        # P2
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (continued)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4)
        y=710
        for line in wrap_text(story['p2'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        pdf.add_rect(100,y-260,412,240,1.5,0.3)
        pdf.add_centered_text(y-120,"[ILLUSTRATION: The parable scene unfolding",'F3',9,0.4)
        pdf.add_centered_text(y-135,"with vivid colors and emotion]",'F3',9,0.4)
        # P3
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (the lesson!)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4)
        y=710
        for line in wrap_text(story['p3'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=15
        pdf.add_filled_rect(72,y-30,468,40,0.9)
        pdf.add_centered_text(y-5,"KEY BIBLE VERSE:",'F2',10,0.2)
        pdf.add_centered_text(y-22,story['verse'],'F4',11,0)
        y-=60
        pdf.add_rect(72,y-40,468,50,2,0.2)
        pdf.add_centered_text(y-5,"MORAL:",'F2',11,0.1)
        pdf.add_centered_text(y-25,story['moral'],'F5',11,0)
        y-=60
        pdf.add_filled_rect(72,y-35,468,40,0.93)
        pdf.add_text(80,y-10,"MODERN DAY EXAMPLE:",'F2',10,0.1)
        pdf.add_text(80,y-28,story['modern'],'F4',10,0.2)
        # P4
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"WHAT I LEARNED",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_text(72,710,f"Reflecting on: {story['title']}",'F4',11,0.2)
        qs=["1. What is the main lesson Jesus is teaching in this parable?",
            "2. Who do you relate to most in this story and why?",
            "3. How can you apply this parable to your life this week?"]
        y=670
        for q in qs:
            pdf.add_text(72,y,q,'F2',11,0.1); y-=20
            for _ in range(3): pdf.add_line(90,y,530,y,0.5,0.6); y-=20
            y-=10
        pdf.add_filled_rect(72,y-120,468,130,0.92)
        pdf.add_centered_text(y-5,"MY PRAYER",'F2',14,0.1)
        pdf.add_text(80,y-25,"Jesus, help me to understand this parable and...",'F4',10,0.2)
        for i in range(5): pdf.add_line(80,y-50-i*20,520,y-50-i*20,0.5,0.6)
        # P5
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"WORD SEARCH PUZZLE",'F2',16,0)
        pdf.add_text(72,720,f"Find words from: {story['title']}",'F4',11,0.2)
        grid=generate_word_search(story['words'])
        y=680
        for row in grid: pdf.add_centered_text(y,"   ".join(row),'F3',14,0.1); y-=24
        y-=20
        pdf.add_text(72,y,"Words to find:",'F2',11,0.1); y-=20
        pdf.add_text(72,y,"  ".join(story['words']),'F3',10,0.2)
        y-=40
        pdf.add_text(72,y,"CHALLENGE: Retell this parable in your own words below:",'F4',10,0.3)
        for _ in range(3): y-=22; pdf.add_line(72,y,540,y,0.5,0.6)
        # P6
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"DRAW THIS PARABLE!",'F2',16,0)
        pdf.add_text(72,720,f"Illustrate: {story['title']}",'F4',11,0.2)
        pdf.add_rect(72,280,468,420,1.5,0.3)
        pdf.add_centered_text(260,"What would YOU do differently in this story?",'F2',11,0.1)
        y=230
        for _ in range(4): pdf.add_line(72,y,540,y,0.5,0.6); y-=22


    # Quiz (2 pages)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 1",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    qs=[("1. Who helped the injured man in the Good Samaritan?","a) Priest  b) Levite  c) Samaritan"),
        ("2. What did the Prodigal Son do with his money?","a) Saved it  b) Wasted it  c) Gave it away"),
        ("3. How many sheep were lost in Jesus' parable?","a) 10  b) 5  c) 1"),
        ("4. What type of ground produces good fruit?","a) Rocky  b) Thorny  c) Good soil"),
        ("5. What did the wise man build his house on?","a) Sand  b) Rock  c) Wood")]
    y=700
    for q,o in qs: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 2",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    qs2=[("6. What grows from a mustard seed?","a) Small bush  b) Large tree  c) Flower"),
         ("7. The hidden treasure was found in a...","a) Cave  b) House  c) Field"),
         ("8. How many servants received talents?","a) 2  b) 3  c) 5"),
         ("9. Who refused to come to the wedding feast?","a) The poor  b) The invited guests  c) Children"),
         ("10. The unforgiving servant owed how much?","a) A little  b) Millions  c) Nothing")]
    y=700
    for q,o in qs2: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.add_text(72,y-20,"Answers: 1c, 2b, 3c, 4c, 5b, 6b, 7c, 8b, 9b, 10b",'F3',9,0.4)

    # Vocabulary
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"VOCABULARY & WORD LIST",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    vocab=[("Parable","A simple story with a deeper spiritual meaning"),
           ("Compassion","Deep caring for someone who is suffering"),
           ("Repentance","Turning away from wrong and back to God"),
           ("Stewardship","Taking good care of what God gives you"),
           ("Forgiveness","Choosing not to hold wrong against someone"),
           ("Grace","Receiving good things you do not deserve"),
           ("Obedience","Doing what God asks willingly and joyfully"),
           ("Kingdom","God's rule and reign in people's hearts"),
           ("Harvest","The good results of faithful living"),
           ("Mercy","Not giving punishment that is deserved")]
    y=710
    for w,d in vocab: pdf.add_text(72,y,f"{w}:",'F2',11,0.1); pdf.add_text(200,y,d,'F4',10,0.2); y-=28

    # Journal (4 pages)
    prompts=["A parable that changed how I think about...","How I can be a better neighbor this week...",
             "Something I need to forgive someone for...","How I will use my talents for God..."]
    for j in range(4):
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"MY FAITH JOURNAL - Page {j+1}",'F2',16,0)
        pdf.add_text(72,710,prompts[j],'F5',12,0.2)
        y=680
        for _ in range(24): pdf.add_line(72,y,540,y,0.5,0.7); y-=25

    # Certificate
    pdf.new_page(); pc+=1
    pdf.add_rect(50,50,512,692,3,0.2); pdf.add_rect(60,60,492,672,1.5,0.4)
    pdf.add_centered_text(680,"CERTIFICATE OF COMPLETION",'F2',22,0)
    pdf.add_centered_text(640,"This certifies that",'F4',14,0.2)
    pdf.add_line(180,600,432,600,1,0.3)
    pdf.add_centered_text(580,"(write your name)",'F4',9,0.4)
    pdf.add_centered_text(540,"has studied all 10 parables in",'F4',12,0.2)
    pdf.add_centered_text(510,TITLE,'F2',16,0)
    pdf.add_centered_text(400,"Date: _______________",'F4',12,0.3)
    pdf.add_centered_text(280,"\"He who has ears to hear, let him hear!\" - Mark 4:9",'F5',14,0.1)

    # Memory Verse Cards (2 pages)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS",'F2',18,0)
    y=690
    for i,s in enumerate(stories[:5]):
        pdf.add_rect(72,y-55,468,55,1,0.3)
        pdf.add_text(80,y-15,f"Card {i+1}: {s['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,s['verse'],'F4',9,0.2); y-=65
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS (continued)",'F2',18,0)
    y=700
    for i,s in enumerate(stories[5:]):
        pdf.add_rect(72,y-55,468,55,1,0.3)
        pdf.add_text(80,y-15,f"Card {i+6}: {s['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,s['verse'],'F4',9,0.2); y-=65

    # Bonus
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MY PARABLE APPLICATION PLAN",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    pdf.add_text(72,710,"Choose 3 parables and write how you will live them out this month:",'F4',11,0.2)
    y=680
    for i in range(3):
        pdf.add_text(72,y,f"Parable #{i+1}: ",'F2',11,0.1); pdf.add_line(180,y-2,540,y-2,0.5,0.6); y-=30
        pdf.add_text(72,y,"My action plan: ",'F4',10,0.2); pdf.add_line(180,y-2,540,y-2,0.5,0.6); y-=25
        pdf.add_line(72,y,540,y,0.5,0.6); y-=25
        pdf.add_text(72,y,"Result: ",'F4',10,0.2); pdf.add_line(130,y-2,540,y-2,0.5,0.6); y-=35

    output_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),FILENAME)
    pdf.save(output_path)
    print(f"Generated {FILENAME} with {pc} pages")
    return pc

if __name__=="__main__":
    build_pdf()
