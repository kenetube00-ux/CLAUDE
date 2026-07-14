#!/usr/bin/env python3
"""Book 278 - Stories Jesus Told: 10 Parables Every Kid Should Know"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    def draw_border(pdf, x, y, w, h, gray=0.3):
        pdf.add_rect(x, y, w, h, line_width=2, gray=gray)
        pdf.add_rect(x+3, y+3, w-6, h-6, line_width=0.5, gray=gray)

    def illus_box(pdf, y, desc, height=100):
        pdf.add_filled_rect(60, y, 492, height, gray=0.95)
        pdf.add_rect(60, y, 492, height, line_width=1.5, gray=0.4)
        pdf.add_text(70, y+height-18, "[COLORFUL ILLUSTRATION:", font='F2', size=10, gray=0.3)
        words = desc.split()
        line, line_y = "", y+height-33
        for word in words:
            if len(line+" "+word)>75:
                pdf.add_text(70, line_y, line.strip(), font='F3', size=9, gray=0.4)
                line_y -= 13; line = word
            else: line = line+" "+word if line else word
        if line: pdf.add_text(70, line_y, line.strip(), font='F3', size=9, gray=0.4)
        pdf.add_text(70, line_y-13, "]", font='F2', size=10, gray=0.3)

    def wrap(pdf, x, y, text, font='F4', size=11, mw=70, gray=0):
        words = text.split()
        line, cy = "", y
        for word in words:
            if len(line+" "+word)>mw:
                pdf.add_text(x, cy, line.strip(), font=font, size=size, gray=gray)
                cy -= 15; line = word
            else: line = line+" "+word if line else word
        if line: pdf.add_text(x, cy, line.strip(), font=font, size=size, gray=gray); cy -= 15
        return cy


    # TITLE PAGE
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    draw_border(pdf, 30, 30, 552, 732, gray=0.2)
    pdf.add_filled_rect(50, 600, 512, 130, gray=0.88)
    pdf.add_centered_text(700, "STORIES JESUS TOLD", font='F2', size=26, gray=0.1)
    pdf.add_centered_text(668, "10 Parables Every Kid Should Know", font='F5', size=16, gray=0.2)
    illus_box(pdf, 380, "Jesus sitting under a large olive tree on a green hillside, surrounded by children and adults listening intently. He gestures with his hands as He teaches. Sheep graze nearby. A sower scatters seeds in a field in the background. Warm golden sunlight bathes the scene.", 160)
    pdf.add_centered_text(340, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)

    # COPYRIGHT
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "STORIES JESUS TOLD", font='F2', size=16, gray=0.1)
    pdf.add_text(72, 675, "10 Parables Every Kid Should Know", font='F4', size=12, gray=0.3)
    pdf.add_line(72, 665, 400, 665, width=0.5, gray=0.5)
    pdf.add_text(72, 640, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 620, "Scripture from World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 50, gray=0.92)
    pdf.add_text(72, 130, "Dedicated to kids who love stories - Jesus was the greatest storyteller!", font='F5', size=11, gray=0.2)

    parables = [
        {
            "title": "THE GOOD SAMARITAN",
            "theme": "Helping Everyone - Even Strangers",
            "illustration": "A kind Samaritan man in colorful robes kneeling beside an injured traveler on a rocky road. He pours oil on wounds and wraps bandages. His donkey waits patiently. In the distance, a priest and Levite walk away looking the other way. Desert road between Jerusalem and Jericho with rocky hills.",
            "modern": "Imagine a kid at school trips and spills everything from their backpack. Two popular kids walk right past. Then the new kid nobody talks to stops, kneels down, and helps pick up every single pencil, book, and paper. That's what the Good Samaritan did - he helped when nobody else would!",
            "bible_version": "A man was robbed and beaten on the road to Jericho. A priest saw him and crossed to the other side. A Levite did the same. But a Samaritan - someone the Jews didn't like - stopped, bandaged his wounds, put him on his donkey, and paid for his care at an inn.",
            "meaning": "Your neighbor isn't just the person next door - it's ANYONE who needs help. Jesus wants us to help everyone, even people who are different from us.",
            "application": "This week, look for someone who needs help - especially someone you wouldn't normally talk to. Be their Good Samaritan!",
            "question": "Who in your life might need a Good Samaritan right now? What can you do for them?"
        },
        {
            "title": "THE PRODIGAL SON",
            "theme": "Forgiveness & Coming Home",
            "illustration": "A joyful father running with open arms toward his ragged, dirty son on a country road. The son is thin and wearing torn clothes. The father's face beams with love and tears. A grand house with warm light glows in the background. Green hills and a sunset sky in orange and purple.",
            "modern": "Imagine telling your parents 'I wish you weren't my family!' then taking your birthday money and running away. You spend everything on junk food and video games until you're broke and sleeping in the park. Finally you go home, expecting anger - but your parents RUN to hug you and throw a party!",
            "bible_version": "A young son demanded his inheritance early and left home. He wasted everything on wild living. When a famine hit, he ended up feeding pigs and was so hungry he wanted to eat their food. He went home planning to be a servant. But his father saw him from far away, ran to him, hugged him, and threw a feast!",
            "meaning": "No matter how far you wander from God, He's always watching for you, ready to welcome you home with a party! God never stops loving you.",
            "application": "If you've been ignoring God or doing wrong things, come back! He's not angry - He's waiting with arms wide open!",
            "question": "Have you ever done something wrong and been afraid to say sorry? What happened when you finally did?"
        },
        {
            "title": "THE LOST SHEEP",
            "theme": "You Are Valuable to God",
            "illustration": "A shepherd carrying a small white fluffy lamb on his shoulders, walking through rocky wilderness at sunset. His face shows relief and joy. Behind him, 99 sheep graze safely in a green meadow. Stars begin to appear in a twilight purple sky. The shepherd's crook hangs at his side.",
            "modern": "Imagine having 100 stuffed animals but your absolute FAVORITE one goes missing. Would you say 'Oh well, I still have 99'? NO! You'd tear your room apart looking for it! That's how God feels about YOU - you're His favorite!",
            "bible_version": "A shepherd had 100 sheep. One wandered away. He left the 99 safe sheep and searched through dangerous hills and valleys until he found the lost one. He carried it home on his shoulders, rejoicing. He called his friends to celebrate: 'I found my lost sheep!'",
            "meaning": "YOU are that sheep to God! He doesn't say 'I have billions of people, one doesn't matter.' Every single person matters to Him! He will search for you!",
            "application": "Remember that you are NEVER too lost for God to find. And help others know they matter to God too!",
            "question": "Have you ever felt lost or alone? How does it feel to know God is actively searching for you?"
        },

        {
            "title": "THE SOWER & SEEDS",
            "theme": "How We Receive God's Word",
            "illustration": "A farmer in brown tunic scattering golden seeds from a bag across four types of ground: a hard rocky path with birds eating seeds, shallow rocky soil with tiny sprouts wilting, thorny ground with weeds choking plants, and rich dark soil with tall golden wheat growing abundantly. Bright blue sky.",
            "modern": "Imagine your teacher gives the whole class the same amazing book. One kid never opens it. Another reads a page then forgets. A third starts reading but gets distracted by their phone. But the fourth kid reads it, loves it, and shares it with everyone! Same book - different responses!",
            "bible_version": "A farmer scattered seeds. Some fell on the path - birds ate them. Some fell on rocks - they grew quickly but died in the sun. Some fell among thorns - they were choked. But seeds on good soil grew 30, 60, even 100 times what was planted!",
            "meaning": "The seed is God's word. The soils are our hearts. Some people ignore it, some accept it briefly, some let worries choke it out. But those who truly receive it and live it produce amazing fruit!",
            "application": "Be good soil! When you hear God's word, don't just say 'cool' - let it grow deep roots in your life!",
            "question": "Which soil are you right now? What can you do to be 'good soil' for God's word?"
        },
        {
            "title": "THE WISE & FOOLISH BUILDERS",
            "theme": "Build on Solid Ground",
            "illustration": "Split scene: Left side shows a beautiful stone house on solid rock standing firm in a terrible storm with rain and floods. Right side shows a fancy house on sand collapsing as floods wash the sand away. Lightning flashes. Waves crash. One house stands strong, the other crumbles dramatically.",
            "modern": "Imagine two kids building sandcastles. One builds on wet sand near the water - it looks amazing but one wave destroys it! The other builds higher up on solid ground - it's not as flashy but it LASTS! Building your life on Jesus is like building on solid rock.",
            "bible_version": "Two men built houses. The wise man dug deep and built on rock. When storms came with rain, floods, and wind, his house stood firm. The foolish man built quickly on sand. The same storm came and his house collapsed completely - what a crash!",
            "meaning": "If you build your life on Jesus' teachings, nothing can knock you down! But if you build on popularity, money, or anything else, eventually storms will reveal the weak foundation.",
            "application": "What's your life built on? Make sure you're building on rock by reading God's word and obeying it daily!",
            "question": "What 'storms' have tested your foundation? What helps you stand strong?"
        },
        {
            "title": "THE MUSTARD SEED",
            "theme": "Small Faith Grows Big",
            "illustration": "A progression scene: tiny black mustard seed in a child's palm on the left, growing progressively larger through stages, until it becomes a massive tree with birds nesting in its spreading branches on the right. The tree is full and green with colorful birds. Child looks up in amazement.",
            "modern": "You plant a tiny apple seed - so small you could lose it! But years later it's a huge tree giving apples to the whole neighborhood. That's what faith is like! Your small trust in God can grow into something that helps thousands!",
            "bible_version": "Jesus said the kingdom of heaven is like a mustard seed - the smallest of all seeds. But when it grows, it becomes the largest garden plant, like a tree! Birds come and nest in its branches.",
            "meaning": "Don't despise small beginnings! Even tiny faith in a big God can grow into something that provides shelter and blessing to many people around you.",
            "application": "Start small! Pray one prayer. Help one person. Share one kind word. Watch God grow it into something amazing!",
            "question": "What small step of faith can you take today that God might grow into something huge?"
        },
        {
            "title": "THE HIDDEN TREASURE",
            "theme": "The Kingdom Is Worth Everything",
            "illustration": "A man in a wheat field discovering a wooden chest overflowing with gold coins, jewels, and precious gems. His face shows absolute shock and joy. Wheat stalks surround him. Sunlight glints off the treasure. He clutches his heart in disbelief. The field stretches to green hills beyond.",
            "modern": "Imagine finding out that the vacant lot on your street has a million dollars buried in it. Would you sell your bike, your games, everything you own to buy that lot? OF COURSE! Because what you'd get is worth way more than what you'd give up!",
            "bible_version": "The kingdom of heaven is like treasure hidden in a field. A man found it, hid it again, and in his JOY went and sold everything he had to buy that field!",
            "meaning": "Knowing God is like finding the greatest treasure ever! It's worth giving up anything and everything because what you get - eternal life with God - is infinitely more valuable!",
            "application": "What would you give up for God? Is there anything you value more than Him? Put Him first!",
            "question": "If following Jesus cost you something (popularity, time, comfort), would it be worth it? Why?"
        },

        {
            "title": "THE TALENTS",
            "theme": "Use What God Gave You",
            "illustration": "Three servants standing before a wealthy master at his estate. The first proudly shows doubled gold bags (10 total). The second shows doubled silver (4 total). The third nervously holds a dirty cloth with one buried coin. Master smiles at first two, looks disappointed at third. Rich estate with columns behind.",
            "modern": "Your teacher gives three students a project. One works super hard and makes something amazing. Another does a great job too. The third is so scared of failing that they don't even TRY! Who do you think the teacher is proud of? The ones who USED what they were given!",
            "bible_version": "A master gave three servants talents (money). One got 5 and earned 5 more. One got 2 and earned 2 more. The last got 1 and buried it in fear. The master praised the first two: 'Well done, good and faithful servant!' But the fearful one was rebuked for wasting his opportunity.",
            "meaning": "God gives everyone different gifts and abilities. He doesn't expect the same from everyone - just that you USE what He gave you! Don't bury your talent in fear!",
            "application": "What gifts has God given you? Singing? Drawing? Kindness? Math? Sports? USE them for Him! Don't hide them!",
            "question": "What talent or gift has God given you? How can you use it to serve others this week?"
        },
        {
            "title": "THE WEDDING FEAST",
            "theme": "God Invites Everyone",
            "illustration": "A magnificent banquet hall with a long table covered in delicious food - roasted meats, fruits, bread, desserts. Golden chandeliers hang above. Well-dressed guests mingle. But also at the table are surprised poor people, homeless people, children - everyone welcomed in! A king gestures 'come in!' at the door.",
            "modern": "Imagine throwing the biggest, most amazing birthday party ever - but all your 'cool' friends say they're too busy. So you go to the park and invite EVERYONE - the kid sitting alone, the elderly neighbor, people nobody usually notices. And THEY come and have the best time!",
            "bible_version": "A king prepared a wedding feast. He invited important guests, but they all made excuses - too busy with land, oxen, or new marriages. The angry king sent servants to invite EVERYONE from the streets - poor, disabled, strangers. The hall was filled with thankful guests!",
            "meaning": "God invites everyone into His kingdom! Some 'religious' people reject Him while unexpected people accept! Don't make excuses when God invites you - His feast is the best thing ever!",
            "application": "Don't be too busy for God! Accept His invitation. And invite others who might think they're not welcome - God wants EVERYONE!",
            "question": "Do you know someone who thinks they're not good enough for God? How can you invite them to know His love?"
        },
        {
            "title": "THE UNFORGIVING SERVANT",
            "theme": "Forgive As God Forgives",
            "illustration": "Two contrasting scenes: Top - a king forgiving a servant who owes millions, tearing up a huge scroll of debt, servant weeping gratefully. Bottom - that same servant angrily grabbing a poor man by the collar who owes him just pennies, refusing mercy. Other servants watch in shock and disgust.",
            "modern": "Imagine your friend accidentally breaks your $500 phone and you forgive them completely. Then you see your little brother borrow your $1 pencil without asking and you EXPLODE at him! That's how crazy it is to receive God's forgiveness but refuse to forgive others!",
            "bible_version": "A servant owed the king millions - an impossible debt! The king forgave it ALL! But that same servant found a man who owed him just a few dollars and threw him in prison. When the king heard, he was furious: 'I forgave YOUR huge debt! Shouldn't you forgive a small one?'",
            "meaning": "God has forgiven us an ENORMOUS debt of sin. How can we refuse to forgive others their small offenses against us? Forgive others because God forgave you!",
            "application": "Is there someone you need to forgive? Remember how much God has forgiven you, and let it go!",
            "question": "Who do you need to forgive? Write their name and pray for the strength to let go of anger."
        }
    ]


    # RENDER PARABLES
    gray_vals = [0.88, 0.92, 0.95, 0.90, 0.93, 0.88, 0.97, 0.91, 0.94, 0.89]
    
    for idx, p in enumerate(parables):
        bg = gray_vals[idx % len(gray_vals)]
        
        # Page 1: Title + Illustration + Modern retelling
        pdf.new_page()
        pdf.add_filled_rect(0, 720, 612, 72, gray=bg)
        pdf.add_filled_rect(45, 725, 522, 60, gray=0.97)
        draw_border(pdf, 45, 725, 522, 60, gray=0.3)
        pdf.add_centered_text(762, f"Parable {idx+1}", font='F4', size=10, gray=0.5)
        pdf.add_centered_text(742, p["title"], font='F2', size=18, gray=0.1)
        pdf.add_centered_text(727, p["theme"], font='F5', size=11, gray=0.3)
        
        illus_box(pdf, 560, p["illustration"], 130)
        
        pdf.add_filled_rect(50, 380, 512, 160, gray=0.97)
        pdf.add_rect(50, 380, 512, 160, line_width=0.5, gray=0.5)
        pdf.add_text(60, 525, "TODAY'S VERSION:", font='F2', size=11, gray=0.2)
        wrap(pdf, 60, 505, p["modern"], font='F4', size=11, mw=72)
        
        # Page 2: Bible version + Meaning + Application + Discussion
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_text(60, 760, p["title"] + " - What Jesus Actually Said", font='F2', size=13, gray=0.2)
        pdf.add_line(60, 752, 450, 752, width=0.5, gray=0.4)
        
        # Bible version
        pdf.add_filled_rect(50, 620, 512, 120, gray=0.92)
        pdf.add_rect(50, 620, 512, 120, line_width=1, gray=0.4)
        pdf.add_text(65, 725, "THE BIBLE STORY:", font='F2', size=11, gray=0.1)
        wrap(pdf, 65, 705, p["bible_version"], font='F5', size=11, mw=70)
        
        # What Jesus Meant
        pdf.add_filled_rect(50, 500, 512, 100, gray=bg)
        draw_border(pdf, 50, 500, 512, 100, gray=0.4)
        pdf.add_text(65, 585, "WHAT JESUS MEANT:", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 565, p["meaning"], font='F4', size=11, mw=70)
        
        # Life Application
        pdf.add_filled_rect(50, 390, 512, 90, gray=0.95)
        pdf.add_text(65, 465, "LIFE APPLICATION:", font='F2', size=11, gray=0.1)
        wrap(pdf, 65, 445, p["application"], font='F4', size=11, mw=70)
        
        # Discussion Question
        pdf.add_filled_rect(50, 280, 512, 90, gray=0.88)
        pdf.add_rect(50, 280, 512, 90, line_width=1, gray=0.3)
        pdf.add_text(65, 355, "DISCUSSION QUESTION:", font='F2', size=11, gray=0.1)
        wrap(pdf, 65, 335, p["question"], font='F5', size=11, mw=70)
        
        # Writing lines
        for i in range(4):
            pdf.add_line(60, 240-(i*25), 550, 240-(i*25), width=0.5, gray=0.6)

    # FINAL REFLECTION PAGE
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    pdf.add_filled_rect(40, 700, 532, 60, gray=0.88)
    draw_border(pdf, 40, 700, 532, 60, gray=0.3)
    pdf.add_centered_text(735, "MY FAVORITE PARABLES", font='F2', size=18, gray=0.1)
    pdf.add_centered_text(710, "Which stories spoke to your heart?", font='F4', size=12, gray=0.3)
    pdf.add_text(60, 670, "My #1 favorite parable is:", font='F5', size=12, gray=0.2)
    pdf.add_line(60, 650, 550, 650, width=0.5, gray=0.6)
    pdf.add_text(60, 620, "Because:", font='F5', size=12, gray=0.2)
    for i in range(3):
        pdf.add_line(60, 595-(i*25), 550, 595-(i*25), width=0.5, gray=0.6)
    pdf.add_text(60, 500, "One thing I will DO differently because of these stories:", font='F5', size=12, gray=0.2)
    for i in range(4):
        pdf.add_line(60, 475-(i*25), 550, 475-(i*25), width=0.5, gray=0.6)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book278_Jesus_Parables_Kids.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
