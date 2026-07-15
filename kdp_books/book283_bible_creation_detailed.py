#!/usr/bin/env python3
"""Book 283 - In the Beginning God Created: The 7 Days of Creation Beautifully Told"""
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc
random.seed(283)
TITLE = "IN THE BEGINNING GOD CREATED"
SUBTITLE = "The 7 Days of Creation Beautifully Told"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book283_Creation_Story_Detailed.pdf"
days = [
    {"day": 1, "title": "Light!", "verse": "God said, 'Let there be light,' and there was light. - Genesis 1:3 (WEB)",
     "story1": "Before anything existed, there was only darkness - deep, total, complete darkness everywhere. No sun, no stars, no glow of any kind. The earth was empty and formless, covered in endless dark waters. But God was there, and His Spirit hovered over the surface of the deep. Then God spoke the most powerful words ever uttered in all of eternity.",
     "story2": "GOD SAID, 'LET THERE BE LIGHT!' And instantly - BANG! - brilliant, glorious, radiant light burst into existence! For the very first time, light pushed back the darkness. It was the first sunrise that ever was! God looked at the light and saw that it was good. He separated the light from the darkness, calling the light 'Day' and the darkness 'Night.' Evening came, then morning. The first day was complete.",
     "science": "Light travels at 186,000 miles per SECOND! That means it could circle the Earth 7.5 times in just one second. Scientists say light is both a wave and a particle at the same time!",
     "gratitude": "Thank you God for: Sunshine, Flashlights, Stars, Rainbows, Colors!",
     "words": ["LIGHT", "DARK", "FIRST", "SPEAK", "GOOD", "DAY", "NIGHT", "CREATE"]},
    {"day": 2, "title": "Sky and Water!", "verse": "God made the expanse, and separated the waters. - Genesis 1:7 (WEB)",
     "story1": "On the second day, God looked at all the water that covered everything and had a magnificent plan. He needed to create space - room for air, clouds, and the beautiful blue sky. God spoke again with creative power: 'Let there be an expanse in the middle of the waters, and let it separate the waters from the waters!'",
     "story2": "The waters obeyed their Creator's voice! Some water stayed below, forming the vast oceans, seas, and rivers. Other water rose up above, forming clouds full of rain and moisture. Between them God stretched out the magnificent sky - the expanse we call the atmosphere. Miles and miles of breathable air, perfect for the creatures He would soon create. God called this expanse 'Heaven.' The second day was complete!",
     "science": "Earth's atmosphere is about 60 miles thick and contains the perfect mix of gases for life: 78% nitrogen, 21% oxygen! Without our atmosphere, Earth would be -270 degrees at night and 250 degrees in the day!",
     "gratitude": "Thank you God for: Blue sky, Clouds, Rain, Fresh air, Sunsets!",
     "words": ["SKY", "WATER", "CLOUDS", "AIR", "BLUE", "ABOVE", "BELOW", "BREATH"]},
    {"day": 3, "title": "Land and Plants!", "verse": "God said, 'Let the dry land appear,' and it was so. - Genesis 1:9 (WEB)",
     "story1": "On day three, God commanded the waters below the sky to gather together in one place and for dry land to appear. With a rumble and surge, the waters rushed together forming mighty oceans and seas! Mountains rose up from beneath the waves. Valleys formed. Continents appeared. Sandy beaches, rocky cliffs, rolling hills, and flat plains emerged from the retreating waters.",
     "story2": "Then God spoke again: 'Let the earth produce vegetation - seed-bearing plants and trees!' Instantly the bare ground erupted with life! Green grass carpeted the hills. Wildflowers of every color burst into bloom. Mighty oak trees stretched toward the sky. Apple trees appeared laden with fruit. Roses, tulips, sunflowers, and a million other varieties painted the earth in breathtaking color. Each plant contained seeds to reproduce its own kind forever.",
     "science": "There are over 400,000 species of plants on Earth! Trees can live thousands of years - the oldest known tree is over 5,000 years old. Plants produce the oxygen we breathe through photosynthesis!",
     "gratitude": "Thank you God for: Mountains, Flowers, Fruit trees, Green grass, Forests!",
     "words": ["LAND", "PLANTS", "TREES", "FLOWERS", "GREEN", "GROW", "SEEDS", "EARTH"]},
    {"day": 4, "title": "Sun, Moon, and Stars!", "verse": "God made the two great lights and the stars. - Genesis 1:16 (WEB)",
     "story1": "On the fourth day, God filled the sky with the most spectacular lights. He created the great blazing sun to rule the day - a massive ball of fire so hot its surface burns at 10,000 degrees! He set it at the perfect distance from Earth: close enough to warm us but far enough not to burn us. Then He made the gentle moon to rule the night, reflecting soft silver light.",
     "story2": "But God was not finished! He scattered BILLIONS of stars across the darkness of space like diamonds thrown on black velvet. Each star is a burning sun, many far bigger than our own. He grouped them into galaxies - swirling pinwheels of light. He created the Milky Way with over 200 billion stars! God placed them all in precise positions to mark seasons, days, and years. The night sky became God's spectacular art gallery.",
     "science": "Our sun is 93 million miles from Earth and over 1 million Earths could fit inside it! There are more stars in the universe than grains of sand on all Earth's beaches - estimated at 200 billion trillion!",
     "gratitude": "Thank you God for: Sunshine, Moonlight, Stars, Seasons, Beautiful sunsets!",
     "words": ["SUN", "MOON", "STARS", "LIGHT", "SHINE", "SPACE", "NIGHT", "BRIGHT"]},

    {"day": 5, "title": "Fish and Birds!", "verse": "God created the large sea creatures and every living creature that moves in the waters, and every winged bird. - Genesis 1:21 (WEB)",
     "story1": "On day five, God turned His attention to filling the waters and skies with LIFE! He spoke and the empty oceans suddenly teemed with creatures. Tiny colorful tropical fish darted through coral reefs. Enormous whales breached the surface. Dolphins leaped joyfully. Octopuses changed colors. Jellyfish glowed. Sea turtles glided gracefully. From microscopic plankton to the massive blue whale, every water creature appeared at God's command!",
     "story2": "Then God filled the sky with birds of every kind! Eagles soared on mighty wings. Hummingbirds hovered before flowers, their wings beating 80 times per second. Colorful parrots chattered in tropical trees. Penguins waddled on icy shores. Owls prepared for nighttime hunting. Flamingos stood on one leg. God created over 10,000 species of birds and countless ocean creatures, each one unique and perfectly designed. He blessed them saying, 'Be fruitful and multiply!'",
     "science": "The ocean covers 71% of Earth's surface and contains 97% of all water! Blue whales are the largest animals ever - up to 100 feet long. Hummingbirds can fly backwards and their hearts beat over 1,200 times per minute!",
     "gratitude": "Thank you God for: Fish, Dolphins, Eagles, Songbirds, Ocean life!",
     "words": ["FISH", "BIRDS", "OCEAN", "WINGS", "SWIM", "FLY", "WHALE", "EAGLE"]},
    {"day": 6, "title": "Animals and People!", "verse": "God created man in his own image. - Genesis 1:27 (WEB)",
     "story1": "The sixth day was the most incredible of all! God filled the land with animals - lions roared, elephants trumpeted, horses galloped, rabbits hopped, and monkeys swung through trees. He created every kind: massive dinosaurs, tiny insects, slithering snakes, and jumping frogs. Cats purred, dogs wagged their tails, and butterflies floated on the breeze. Each animal was perfectly designed for its environment.",
     "story2": "But God saved the BEST for last. He said, 'Let Us make man in Our image!' From the dust of the ground, God carefully formed a man and breathed life into his nostrils. Adam opened his eyes and saw his Creator! God made Eve from Adam's rib to be his partner. They were made in God's IMAGE - able to think, love, create, and have relationship with God. God gave them authority over all creation and called everything 'VERY good!'",
     "science": "The human body has 206 bones, 600 muscles, 60,000 miles of blood vessels, and a brain with 86 billion neurons! DNA in one human cell would stretch 6 feet if uncoiled. You are incredibly designed!",
     "gratitude": "Thank you God for: My body, Animals, My family, Being made in God's image!",
     "words": ["ANIMALS", "PEOPLE", "IMAGE", "ADAM", "EVE", "LIFE", "BREATH", "GOOD"]},
    {"day": 7, "title": "God Rested!", "verse": "God blessed the seventh day and made it holy, because He rested. - Genesis 2:3 (WEB)",
     "story1": "On the seventh day, something different happened. God did not create anything new. Instead, He RESTED. Not because He was tired - God never gets tired! He rested because His work was FINISHED. Everything was perfect. Every star was in place. Every creature was alive. Every plant was blooming. Adam and Eve walked in perfect relationship with their Creator. It was paradise beyond imagination.",
     "story2": "God blessed the seventh day and made it HOLY - set apart and special. He created the pattern of rest for all humanity to follow. Six days of work, one day of rest and worship. This rhythm of work and rest is built into the fabric of creation itself. God wanted humans to take time to stop, appreciate His creation, worship Him, and enjoy relationship. The Sabbath was God's gift to humanity - proof that we are more than machines.",
     "science": "Scientists confirm that humans need regular rest to function. Sleep deprivation affects memory, immune system, and emotions. Our bodies actually heal and grow during rest! God designed us to need regular renewal.",
     "gratitude": "Thank you God for: Rest, Weekends, Family time, Worship, Peace!",
     "words": ["REST", "HOLY", "BLESSED", "FINISH", "PEACE", "WORSHIP", "SABBATH", "PERFECT"]}
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
    # Title
    pdf.new_page(); pc+=1
    pdf.add_filled_rect(50,650,512,100,0.85)
    pdf.add_centered_text(720,TITLE,'F2',22,0); pdf.add_centered_text(690,SUBTITLE,'F4',13,0.2)
    pdf.add_centered_text(660,"Written and Illustrated by",'F4',12,0.3)
    pdf.add_centered_text(640,AUTHOR,'F2',16,0)
    pdf.add_rect(100,200,412,380,2,0.3)
    pdf.add_centered_text(420,"[ILLUSTRATION: Spectacular creation scene with",'F3',10,0.4)
    pdf.add_centered_text(405,"light bursting through darkness, animals, stars]",'F3',10,0.4)
    pdf.add_centered_text(100,"Explore each day of creation in beautiful detail!",'F4',12,0.3)
    # Copyright
    pdf.new_page(); pc+=1
    pdf.add_centered_text(700,TITLE,'F2',14,0)
    pdf.add_text(72,600,f"Written by {AUTHOR}",'F4',11,0.2)
    pdf.add_text(72,580,"Copyright 2025. All Rights Reserved.",'F4',10,0.3)
    pdf.add_text(72,550,"Scripture: World English Bible (WEB) - Public Domain.",'F4',10,0.3)
    pdf.add_text(72,520,"For children ages 6-12. Published by Kingdom Kids Publishing",'F4',10,0.3)
    pdf.add_text(72,440,"Dedication: For every child who looks at creation with wonder!",'F4',11,0.2)
    # TOC
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"TABLE OF CONTENTS",'F2',18,0); pdf.add_line(150,720,462,720,1,0.3); y=680
    for d in days: pdf.add_text(72,y,f"Day {d['day']}: {d['title']}",'F4',12,0.1); y-=35
    pdf.add_text(72,y-10,"Quiz / Vocabulary / Journal / Certificate / Bonus",'F4',10,0.3)
    # Intro
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"HOW TO USE THIS BOOK",'F2',18,0); pdf.add_line(150,720,462,720,1,0.3)
    intro=["Have you ever wondered HOW God created everything?","This book explores each of the 7 days of creation!","",
        "Each day has NINE exciting pages:","  1-2. The creation story told poetically",
        "  3. Full-page illustration","  4. REAL science connections!","  5. Activity page",
        "  6. Coloring/drawing page","  7. Gratitude list","  8. Memory verse page",
        "  9. Discussion questions","","Plus quizzes, vocabulary, journal, and bonus pages!","",
        "Ready to explore how God made EVERYTHING? Let's go!"]
    y=680
    for l in intro: pdf.add_text(72,y,l,'F4',11,0.15); y-=22


    # 7 days x 9 pages = 63 pages
    for day in days:
        # P1: Story part 1
        pdf.new_page(); pc+=1
        pdf.add_filled_rect(50,700,512,60,0.88)
        pdf.add_centered_text(735,f"Day {day['day']} of Creation",'F1',10,0.4)
        pdf.add_centered_text(715,day['title'].upper(),'F2',22,0)
        pdf.add_line(72,690,540,690,1,0.3); y=670
        for line in wrap_text(day['story1'],78): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=20
        pdf.add_filled_rect(72,y-25,468,30,0.92)
        pdf.add_centered_text(y-8,day['verse'],'F5',10,0)
        # P2: Story part 2
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"Day {day['day']}: {day['title']} (continued)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(day['story2'],78): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=30
        pdf.add_rect(72,y-200,468,200,1.5,0.3)
        pdf.add_centered_text(y-80,f"[ILLUSTRATION: Day {day['day']} - {day['title']}",'F3',10,0.4)
        pdf.add_centered_text(y-100,"Beautiful detailed scene of what God created]",'F3',10,0.4)
        # P3: Full illustration page
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"DAY {day['day']}: {day['title'].upper()}",'F2',18,0)
        pdf.add_rect(50,80,512,640,2,0.3)
        pdf.add_centered_text(420,f"[FULL-PAGE ILLUSTRATION: Day {day['day']}",'F3',11,0.4)
        pdf.add_centered_text(400,f"God creates {day['title'].lower().replace('!','')}",'F3',11,0.4)
        pdf.add_centered_text(380,"in magnificent, colorful detail]",'F3',11,0.4)
        # P4: Science connection
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"SCIENCE CONNECTION - Day {day['day']}",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_text(72,710,"Did you know? God's creation is even MORE amazing",'F4',11,0.1)
        pdf.add_text(72,690,"when we learn the science behind it!",'F4',11,0.1)
        y=650
        pdf.add_filled_rect(72,y-80,468,90,0.92)
        pdf.add_text(80,y-10,"AMAZING SCIENCE FACTS:",'F2',12,0.1)
        for i,line in enumerate(wrap_text(day['science'],70)):
            pdf.add_text(80,y-30-i*16,line,'F4',10,0.2)
        y-=120
        pdf.add_text(72,y,"Questions to think about:",'F2',12,0.1); y-=25
        pdf.add_text(72,y,"1. How does this science fact make you appreciate God more?",'F4',10,0.2); y-=20
        pdf.add_line(90,y,540,y,0.5,0.6); y-=20; pdf.add_line(90,y,540,y,0.5,0.6); y-=30
        pdf.add_text(72,y,"2. What other science facts do you know about Day "+str(day['day'])+"?",'F4',10,0.2); y-=20
        pdf.add_line(90,y,540,y,0.5,0.6); y-=20; pdf.add_line(90,y,540,y,0.5,0.6)
        # P5: Activity page
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"ACTIVITY PAGE - Day {day['day']}",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_text(72,710,"WORD SEARCH - Find words about what God created on this day:",'F4',11,0.2)
        grid=generate_word_search(day['words']); y=680
        for row in grid: pdf.add_centered_text(y,"   ".join(row),'F3',13,0.1); y-=22
        y-=15; pdf.add_text(72,y,"Words: "+"  ".join(day['words']),'F3',9,0.2)
        y-=30; pdf.add_text(72,y,"UNSCRAMBLE: Rearrange these letters:",'F2',10,0.1)
        scrambled = day['words'][:4]
        y-=20
        for w in scrambled:
            letters = list(w); random.shuffle(letters)
            pdf.add_text(100,y,"".join(letters)+" = ________",'F3',11,0.2); y-=22
        # P6: Coloring/Drawing
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"DRAW DAY {day['day']}!",'F2',16,0)
        pdf.add_text(72,720,f"Draw what God created on Day {day['day']}: {day['title']}",'F4',11,0.2)
        pdf.add_rect(72,250,468,450,1.5,0.3)
        pdf.add_centered_text(230,"Color this page with your favorite colors!",'F4',10,0.3)
        pdf.add_text(72,200,"My favorite thing God created on this day:",'F2',10,0.1)
        pdf.add_line(72,180,540,180,0.5,0.6)
        # P7: Gratitude list
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"GRATITUDE LIST - Day {day['day']}",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_text(72,710,f"Things from Day {day['day']} I am thankful for:",'F4',11,0.2)
        y=680
        pdf.add_filled_rect(72,y-60,468,65,0.93)
        pdf.add_text(80,y-15,day['gratitude'],'F4',11,0.2)
        y-=90
        pdf.add_text(72,y,"Add your own! What else are you thankful for from Day "+str(day['day'])+"?",'F2',10,0.1)
        y-=25
        for i in range(8):
            pdf.add_text(72,y,f"{i+1}.",'F2',11,0.1); pdf.add_line(100,y-2,540,y-2,0.5,0.6); y-=28
        # P8: Memory verse
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"MEMORY VERSE - Day {day['day']}",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_filled_rect(72,620,468,80,0.88)
        pdf.add_centered_text(670,"Today's Verse:",'F2',12,0.1)
        pdf.add_centered_text(645,day['verse'],'F5',11,0)
        pdf.add_text(72,580,"Write the verse 3 times to help memorize it:",'F4',11,0.2)
        y=550
        for i in range(3):
            pdf.add_text(72,y,f"#{i+1}:",'F2',10,0.1)
            for j in range(2): pdf.add_line(100,y-j*20,540,y-j*20,0.5,0.6)
            y-=55
        pdf.add_text(72,y,"Now try writing it from MEMORY:",'F2',10,0.1); y-=20
        for _ in range(2): pdf.add_line(72,y,540,y,0.5,0.6); y-=20
        # P9: Discussion
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"DISCUSSION - Day {day['day']}",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_text(72,710,"Talk about these questions with your family:",'F4',11,0.2)
        disc_qs=[f"1. Why do you think God created {day['title'].lower().replace('!','')} on Day {day['day']}?",
                 "2. What is the most amazing thing about what God made this day?",
                 "3. How does this part of creation help us in our daily lives?",
                 "4. What would the world be like without what God made on this day?"]
        y=670
        for q in disc_qs:
            pdf.add_text(72,y,q,'F2',10,0.1); y-=20
            for _ in range(3): pdf.add_line(90,y,530,y,0.5,0.6); y-=18
            y-=15


    # Quiz (2 pages)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"CREATION QUIZ - Part 1",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs=[("1. What did God create on Day 1?","a) Sun  b) Light  c) Animals"),
        ("2. What separates waters above from below?","a) Mountains  b) Sky/expanse  c) Trees"),
        ("3. What appeared when waters gathered?","a) Islands  b) Dry land  c) Fish"),
        ("4. What rules the night sky?","a) Stars  b) Moon  c) Clouds"),
        ("5. What creatures were made on Day 5?","a) Dogs  b) Fish and birds  c) Insects")]
    y=700
    for q,o in qs: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"CREATION QUIZ - Part 2",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs2=[("6. Humans were made in God's ___","a) Likeness  b) Image  c) Both"),
         ("7. What did God do on Day 7?","a) Created angels  b) Rested  c) Made more animals"),
         ("8. God called His creation ___","a) Okay  b) Good  c) Very good"),
         ("9. Where did God place the first humans?","a) Mountain  b) Garden of Eden  c) City"),
         ("10. How many days did creation take?","a) 5  b) 6  c) 7 (including rest)")]
    y=700
    for q,o in qs2: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.add_text(72,y-20,"Answers: 1b, 2b, 3b, 4b, 5b, 6c, 7b, 8c, 9b, 10c",'F3',9,0.4)

    # Vocabulary
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"VOCABULARY & WORD LIST",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    vocab=[("Creation","The act of bringing everything into existence"),("Expanse","The great stretch of sky above us"),
           ("Vegetation","All plant life - trees, grass, flowers"),("Luminaries","Lights in the sky - sun, moon, stars"),
           ("Abundance","Having much more than enough"),("Dominion","Authority and rule over something"),
           ("Sabbath","The day of rest God made holy"),("Image","A likeness or representation"),
           ("Formless","Without shape or structure"),("Sovereign","Having complete power and authority")]
    y=710
    for w,d in vocab: pdf.add_text(72,y,f"{w}:",'F2',11,0.1); pdf.add_text(200,y,d,'F4',10,0.2); y-=28

    # Journal (4 pages)
    prompts=["The part of creation that amazes me most...","What I want to ask God about creation...",
             "How I can take care of God's creation...","My creation praise poem to God..."]
    for j in range(4):
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"MY CREATION JOURNAL - Page {j+1}",'F2',16,0)
        pdf.add_text(72,710,prompts[j],'F5',12,0.2); y=680
        for _ in range(24): pdf.add_line(72,y,540,y,0.5,0.7); y-=25

    # Certificate
    pdf.new_page(); pc+=1
    pdf.add_rect(50,50,512,692,3,0.2); pdf.add_rect(60,60,492,672,1.5,0.4)
    pdf.add_centered_text(680,"CERTIFICATE OF COMPLETION",'F2',22,0)
    pdf.add_centered_text(640,"This certifies that",'F4',14,0.2)
    pdf.add_line(180,600,432,600,1,0.3)
    pdf.add_centered_text(540,"has explored all 7 days of creation in",'F4',12,0.2)
    pdf.add_centered_text(510,TITLE,'F2',14,0)
    pdf.add_centered_text(400,"Date: _______________",'F4',12,0.3)
    pdf.add_centered_text(280,"\"The heavens declare the glory of God\" - Psalm 19:1",'F5',13,0.1)

    # Bonus: Creation Week Chart
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MY CREATION WEEK CHART",'F2',18,0)
    pdf.add_text(72,720,"Fill in what God created each day from memory:",'F4',11,0.2); y=680
    for i in range(7):
        pdf.add_filled_rect(72,y-40,468,42,0.95 if i%2==0 else 1.0)
        pdf.add_text(80,y-12,f"Day {i+1}: ",'F2',12,0.1)
        pdf.add_line(150,y-15,520,y-15,0.5,0.6)
        pdf.add_text(80,y-32,"Draw a small picture:",'F4',8,0.4)
        pdf.add_rect(350,y-38,170,36,0.5,0.5); y-=50

    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),FILENAME)
    pdf.save(out); print(f"Generated {FILENAME} with {pc} pages"); return pc
if __name__=="__main__": build_pdf()
