#!/usr/bin/env python3
"""Book 279 - Amazing Animals in the Bible: 10 Incredible Creature Stories"""
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc
random.seed(279)
TITLE = "AMAZING ANIMALS IN THE BIBLE"
SUBTITLE = "10 Incredible Creature Stories"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book279_Bible_Animals_Stories.pdf"
stories = [
    {"title": "The Serpent in the Garden", "animal": "Serpent",
     "verse": "The serpent was more subtle than any animal. - Genesis 3:1 (WEB)",
     "moral": "Be careful of tricky lies - always check what God really said!",
     "fact": "Snakes have over 200 vertebrae, can sense vibrations, and some species can go a year without eating!",
     "p1": "In the beautiful Garden of Eden, God placed every kind of wonderful animal. Among them was the serpent - the cleverest creature of all. Adam and Eve lived in paradise with everything they could ever want. God gave them only one rule: do not eat from the tree of knowledge of good and evil in the middle of the garden.",
     "p2": "One day the crafty serpent approached Eve near the forbidden tree. It twisted God's words, asking 'Did God REALLY say you cannot eat from any tree?' Eve corrected the serpent but then listened as it told her the biggest lie ever - that she would not die and would become like God. The fruit looked delicious and the promise of wisdom was tempting. Eve reached out, took the fruit, and ate it. She gave some to Adam too.",
     "p3": "Immediately, everything changed. Adam and Eve felt shame and fear for the first time. They tried to hide from God among the trees. When God found them, He pronounced consequences for everyone. The serpent was cursed to crawl on its belly in the dust forever. But God also made a beautiful promise - one day a descendant of Eve would crush the serpent's head, defeating evil forever. That promise was fulfilled through Jesus!",
     "words": ["SERPENT", "GARDEN", "EDEN", "FRUIT", "TREE", "SNAKE", "CRAFTY", "TRUTH"]},
    {"title": "Noah's Animals - Two by Two", "animal": "all animals",
     "verse": "Of every living thing, you shall bring two into the ark. - Genesis 6:19 (WEB)",
     "moral": "God cares about every creature He made - big and small!",
     "fact": "Scientists estimate there are about 8.7 million animal species on Earth, from tiny insects to massive blue whales!",
     "p1": "When God told Noah to build an enormous ark to survive the coming flood, He gave very specific instructions about the animals. Two of every kind of creature - one male and one female - would come to Noah and enter the boat. Can you imagine the incredible parade that must have been? Lions, elephants, giraffes, birds, insects, reptiles - all walking, flying, and crawling toward one man and his giant wooden boat.",
     "p2": "Noah must have been amazed as animals began arriving from every direction! Tall giraffes ducking through the door, tiny mice scurrying between elephant feet. Colorful parrots flying in beside silent owls. Fierce tigers walking peacefully alongside gentle deer. God brought them all - from the tiniest ant to the largest elephant. For clean animals, Noah brought seven pairs instead of just one. He stored enough food for every creature's special diet.",
     "p3": "For over a year on the ark, Noah and his family cared for all these animals through the terrible flood. When the waters finally receded and the ark landed on dry ground, God opened the door and every creature burst out into the fresh new world! They spread across the earth, filling forests, oceans, deserts, and mountains. God had preserved every species through Noah's faithful obedience. Today when we see the amazing variety of animals, we see God's love for all His creatures.",
     "words": ["NOAH", "ARK", "PAIRS", "ANIMALS", "FLOOD", "CARE", "TWO", "EVERY"]},

    {"title": "Balaam's Talking Donkey", "animal": "Donkey",
     "verse": "The LORD opened the mouth of the donkey. - Numbers 22:28 (WEB)",
     "moral": "God can use anyone - even a stubborn donkey - to deliver His message!",
     "fact": "Donkeys have incredible memories, can live 25-30 years, and can carry up to 30% of their body weight!",
     "p1": "A prophet named Balaam was hired by an evil king to curse Israel. He saddled his donkey and set off on the road. But God was angry and sent an angel with a drawn sword to block the path. The donkey could see the terrifying angel, but Balaam could not! The faithful donkey turned off the road into a field to avoid the angel, and Balaam beat her angrily.",
     "p2": "The angel moved to a narrow path between vineyard walls. Again the donkey saw the angel and pressed against the wall, crushing Balaam's foot. He beat her again! Then the angel stood in a spot so narrow there was no room to pass at all. The poor donkey did the only thing she could - she lay down on the ground. Furious, Balaam beat her with his staff for the third time.",
     "p3": "Then God did something extraordinary - He opened the donkey's mouth and she SPOKE! 'What have I done to you that you have beaten me three times?' she asked! Balaam was so angry he argued back without even being surprised a donkey was talking! Then God opened Balaam's eyes and he finally saw the angel with the sword. He fell on his face in terror. The angel told him the donkey had saved his life THREE times! God used a humble donkey to protect a stubborn man.",
     "words": ["DONKEY", "ANGEL", "SPEAK", "BALAAM", "SWORD", "THREE", "ROAD", "EYES"]},
    {"title": "David's Faithful Sheep", "animal": "Sheep",
     "verse": "The LORD is my shepherd; I shall not want. - Psalm 23:1 (WEB)",
     "moral": "God watches over us like a good shepherd protects his sheep!",
     "fact": "Sheep can recognize up to 50 other sheep faces and remember them for years! They also have excellent peripheral vision.",
     "p1": "Before David became king, he was a young shepherd boy caring for his father's flock in the hills near Bethlehem. Day after day, he led his sheep to green pastures and still waters, just as he later wrote in his famous Psalm 23. He knew each sheep by name and they knew his voice. Whenever he called, they would come running to him.",
     "p2": "But being a shepherd was dangerous! One day a fierce lion crept toward the flock. David did not run away - he chased the lion, grabbed it, and struck it down to save his sheep! Another time a massive bear attacked. Again David fought it off bare-handed, rescuing the lamb from its jaws. His love for his sheep gave him incredible courage that would later help him face the giant Goliath.",
     "p3": "David's experience as a shepherd taught him everything about how God cares for His people. Just as David led his sheep to food and water, God provides for us. Just as David protected his sheep from predators, God protects us from evil. And just as David's sheep trusted his voice completely, we can trust God's voice in our lives. When David wrote 'The Lord is my shepherd,' he understood exactly what that meant from years of faithful shepherding.",
     "words": ["SHEEP", "SHEPHERD", "DAVID", "PROTECT", "GREEN", "FLOCK", "TRUST", "CARE"]},
    {"title": "Elijah's Ravens - Special Delivery", "animal": "Ravens",
     "verse": "I have commanded the ravens to feed you there. - 1 Kings 17:4 (WEB)",
     "moral": "God can use unexpected things to provide for your needs!",
     "fact": "Ravens are among the most intelligent birds - they can solve puzzles, use tools, and even plan for the future!",
     "p1": "The prophet Elijah boldly told wicked King Ahab that no rain would fall until God said so. This made the king furious and Elijah's life was in danger! God told Elijah to hide by a brook called Cherith, far from the king's reach. Elijah obeyed and made camp beside the small stream where he could drink fresh water. But what would he eat all alone in the wilderness?",
     "p2": "God had an amazing plan for feeding His prophet. He commanded ravens - large, black, intelligent birds - to bring food to Elijah every single day! Morning and evening, these wild birds would fly to Elijah carrying bread and meat in their beaks. They were like God's personal delivery service! Normally ravens are scavengers who keep food for themselves, but God changed their nature to serve His faithful prophet.",
     "p3": "Day after day, the ravens came faithfully with their deliveries. Elijah had fresh bread and meat every morning and evening, and cool water from the brook. God showed that He can use anything in creation to provide for His people. He used birds as waiters! When the brook eventually dried up, God had another plan ready - sending Elijah to a widow who would provide for him. God always has a provision plan, sometimes from the most unexpected sources!",
     "words": ["RAVENS", "BREAD", "MEAT", "BROOK", "ELIJAH", "FEED", "BIRDS", "PROVIDE"]},

    {"title": "Daniel's Lions - Mouths Shut Tight", "animal": "Lions",
     "verse": "My God sent his angel and shut the lions' mouths. - Daniel 6:22 (WEB)",
     "moral": "When you are faithful to God, He will protect you from every danger!",
     "fact": "A lion's roar can be heard from 5 miles away! Male lions can weigh up to 500 pounds with jaws that exert 650 PSI of force.",
     "p1": "Daniel was thrown into a den of hungry, roaring lions because he refused to stop praying to God. King Darius was heartbroken but the law could not be changed. As Daniel was lowered into the pit, he could hear the deep rumbling growls of the powerful beasts. Their eyes glowed in the darkness. Their massive paws had claws like knives. Any normal person would have been devoured in seconds.",
     "p2": "But Daniel was not any normal person - he was a man of deep faith! As his feet touched the floor of the den, something miraculous happened. God sent an angel who stood between Daniel and the lions. The angel shut their powerful jaws tight! Those lions that could crush bones with a single bite suddenly became as gentle as kittens. Daniel spent the entire night in complete peace, surrounded by lions who could not harm him.",
     "p3": "At dawn, King Darius rushed to the den calling out desperately for Daniel. To his overwhelming joy, Daniel answered! Not a single scratch was on him. The lions had not touched him because God's angel kept their mouths shut all night long. The king pulled Daniel out and declared that everyone must respect Daniel's God who has the power to shut the mouths of lions. God proved that faith is stronger than the fiercest predator on earth!",
     "words": ["LIONS", "DANIEL", "DEN", "ANGEL", "SHUT", "MOUTHS", "FAITH", "NIGHT"]},
    {"title": "Jonah's Great Fish", "animal": "Great Fish",
     "verse": "The LORD prepared a great fish to swallow up Jonah. - Jonah 1:17 (WEB)",
     "moral": "God's creatures obey Him perfectly - even when people refuse to!",
     "fact": "Blue whales are the largest animals ever, with mouths big enough to hold 100 people! Whale sharks can also swallow very large prey.",
     "p1": "When Jonah ran from God by boarding a ship going the wrong direction, God sent a terrible storm. The sailors threw Jonah into the raging sea. As Jonah plunged into the dark, cold waters and began sinking, all seemed lost. But God had prepared something extraordinary beneath the waves - an enormous fish, specially chosen for this exact moment.",
     "p2": "The great fish opened its massive mouth and swallowed Jonah whole! Instead of drowning in the ocean, Jonah found himself alive inside the belly of this incredible creature. For three days and three nights, the fish served as Jonah's living submarine. In that dark, strange place, surrounded by seaweed and the sounds of the deep ocean, Jonah finally stopped running from God and started praying with a truly repentant heart.",
     "p3": "After three days, at God's command, the great fish swam toward the shore and vomited Jonah out onto dry land! The fish had obeyed God perfectly - swallowing Jonah at exactly the right moment, keeping him alive for three days, and delivering him safely to land. While Jonah had disobeyed, the fish followed God's instructions flawlessly. This incredible creature was both Jonah's punishment and his rescue - proving that all of creation obeys its Creator.",
     "words": ["FISH", "JONAH", "SWALLOW", "OCEAN", "THREE", "DAYS", "OBEY", "WHALE"]},
    {"title": "Jesus Rides a Donkey", "animal": "Donkey",
     "verse": "Your King comes to you, gentle, and riding on a donkey. - Matthew 21:5 (WEB)",
     "moral": "Jesus chose humility over power - true kings serve their people!",
     "fact": "In Bible times, kings rode horses in war but donkeys in peace. A donkey showed the king came as a friend, not a conqueror!",
     "p1": "It was almost time for Jesus to complete His mission on earth. He sent two disciples ahead to a village where they would find a young donkey tied up that no one had ever ridden. They brought it to Jesus and placed their cloaks on its back as a saddle. Jesus, the King of Kings, chose to ride this humble donkey into Jerusalem rather than a powerful warhorse.",
     "p2": "As Jesus rode the donkey down the Mount of Olives toward Jerusalem, an incredible thing happened. Huge crowds gathered along the road! People threw their cloaks on the ground before Him like a carpet. Others cut palm branches and waved them, shouting 'Hosanna! Blessed is He who comes in the name of the Lord!' The whole city was stirred with excitement. Children were singing His praises in the streets.",
     "p3": "This fulfilled a prophecy written 500 years earlier - that Israel's king would come riding on a humble donkey. While earthly kings rode powerful horses with armies behind them, Jesus chose a simple donkey and came in peace and gentleness. The donkey carried the most important person in history, yet this humble animal perfectly represented Jesus' message - true greatness is found in service and humility, not in power and force.",
     "words": ["DONKEY", "JESUS", "PALM", "HUMBLE", "KING", "PEACE", "RIDE", "CLOAKS"]},

    {"title": "Peter's Rooster - The Warning Cry", "animal": "Rooster",
     "verse": "Before the rooster crows, you will deny me three times. - Matthew 26:34 (WEB)",
     "moral": "Even when we fail, Jesus still loves us and gives us another chance!",
     "fact": "Roosters crow at dawn as a natural alarm clock. They can crow up to 15 times each morning and can be heard over a mile away!",
     "p1": "At the Last Supper, Jesus told Peter something shocking - that before the rooster crowed at dawn, Peter would deny knowing Jesus three times! Peter was outraged. 'Never! I would die for you!' he declared boldly. He truly believed he would never betray his beloved teacher. But Jesus knew what was coming and looked at Peter with eyes full of love and sadness.",
     "p2": "That night, Jesus was arrested. Peter followed at a distance to the courtyard of the high priest. A servant girl recognized him and said, 'You were with Jesus!' Terrified, Peter lied: 'I don't know Him!' Another person pointed at him: 'You were with that Galilean!' Again Peter denied it. Then a third person insisted Peter was a follower of Jesus. Peter began cursing and swearing, 'I DO NOT KNOW THE MAN!'",
     "p3": "At that exact moment, a rooster crowed, piercing the cold dawn air. Peter remembered Jesus' words and their eyes met across the courtyard. Jesus looked at him not with anger but with heartbreaking love. Peter broke down and wept bitterly, devastated by his failure. But this was not the end! After the resurrection, Jesus sought Peter out and restored him three times, asking 'Do you love me?' For every denial, Jesus offered forgiveness. The rooster reminded Peter of his weakness, but Jesus reminded him of grace.",
     "words": ["ROOSTER", "PETER", "DENY", "CROW", "DAWN", "TEARS", "FORGIVE", "GRACE"]},
    {"title": "The Lamb of God", "animal": "Lamb",
     "verse": "Behold, the Lamb of God, who takes away the sin of the world! - John 1:29 (WEB)",
     "moral": "Jesus is the perfect Lamb who gave His life to save everyone who believes!",
     "fact": "Lambs are born helpless and completely dependent on their shepherd. They are symbols of innocence and purity in many cultures.",
     "p1": "Throughout the Bible, lambs held a very special and sacred meaning. In the very first sacrifice, God provided a covering for Adam and Eve. When Abraham was about to sacrifice his son Isaac, God provided a ram caught in thorns instead. Each year at Passover, Jewish families sacrificed a perfect lamb without any blemish, and its blood protected them from death - just as it did in Egypt when they were slaves.",
     "p2": "When John the Baptist saw Jesus approaching the Jordan River, he proclaimed something powerful: 'Behold! The Lamb of God who takes away the sin of the world!' John recognized that Jesus was THE lamb that all other sacrifices pointed toward. Jesus was perfect, without sin, innocent and pure - the ultimate sacrifice that would end all other sacrifices forever. He came not to be served but to give His life for others.",
     "p3": "On the cross, Jesus became the final, perfect Lamb. Just as Passover lambs were sacrificed so families could be saved from death, Jesus was sacrificed so all humanity could be saved from eternal death. He was gentle and did not fight back. He was innocent yet took our punishment. In heaven, Jesus is worshiped as the Lamb who was slain - proving that the greatest power in the universe is not force but sacrificial love. The Lamb of God conquered death itself!",
     "words": ["LAMB", "JESUS", "PURE", "SACRIFICE", "LOVE", "SAVE", "BLOOD", "ETERNAL"]}
]


def generate_word_search(words):
    grid = [[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)] for _ in range(10)]
    for word in words[:8]:
        word = word.upper()
        for _ in range(50):
            d = random.choice([(0,1),(1,0),(1,1)])
            r = random.randint(0, max(0,9-len(word)*d[0]))
            c = random.randint(0, max(0,9-len(word)*d[1]))
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
    pdf.add_centered_text(720,TITLE,'F2',26,0)
    pdf.add_centered_text(690,SUBTITLE,'F4',14,0.2)
    pdf.add_centered_text(660,"Written and Illustrated by",'F4',12,0.3)
    pdf.add_centered_text(640,AUTHOR,'F2',16,0)
    pdf.add_rect(100,200,412,380,2,0.3)
    pdf.add_centered_text(420,"[ILLUSTRATION: A collection of Bible animals -",'F3',10,0.4)
    pdf.add_centered_text(405,"lion, dove, fish, lamb, raven together]",'F3',10,0.4)
    pdf.add_centered_text(100,"Discover God's amazing creatures!",'F4',12,0.3)
    # Copyright
    pdf.new_page(); pc+=1
    pdf.add_centered_text(700,TITLE,'F2',16,0)
    pdf.add_text(72,600,f"Written by {AUTHOR}",'F4',11,0.2)
    pdf.add_text(72,580,"Copyright 2025. All Rights Reserved.",'F4',10,0.3)
    pdf.add_text(72,550,"Scripture: World English Bible (WEB) - Public Domain.",'F4',10,0.3)
    pdf.add_text(72,520,"For children ages 6-12.",'F4',10,0.3)
    pdf.add_text(72,490,"Published by Kingdom Kids Publishing - First Edition 2025",'F4',10,0.3)
    pdf.add_text(72,440,"Dedication: For every child who loves animals and loves God!",'F4',11,0.2)
    # TOC
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"TABLE OF CONTENTS",'F2',18,0)
    pdf.add_line(150,720,462,720,1,0.3); y=680
    for i,s in enumerate(stories):
        pdf.add_text(72,y,f"Animal {i+1}: {s['title']}",'F4',12,0.1); y-=28
    pdf.add_text(72,y-10,"Quiz / Vocabulary / Journal / Certificate / Bonus",'F4',10,0.3)
    # How to Use
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"HOW TO USE THIS BOOK",'F2',18,0)
    pdf.add_line(150,720,462,720,1,0.3)
    intro=["Welcome animal lovers! Did you know the Bible is FULL","of amazing animals? From snakes to whales, lions to lambs!","",
        "Each animal story has SIX pages:","  1. The story begins + illustration",
        "  2. The story continues + action scene","  3. Story ending + verse + moral + REAL animal facts!",
        "  4. Reflection questions + prayer","  5. Word search puzzle","  6. Draw the animal!","",
        "BONUS: Each story includes real science facts","about the animal! Learn Bible AND science!","",
        "Ready to meet God's amazing creatures? Let's go!"]
    y=680
    for l in intro: pdf.add_text(72,y,l,'F4',11,0.15); y-=22


    # 10 stories x 6 pages = 60
    for idx, story in enumerate(stories):
        pdf.new_page(); pc+=1
        pdf.add_filled_rect(50,700,512,60,0.88)
        pdf.add_centered_text(735,f"Animal Story {idx+1}",'F1',10,0.4)
        pdf.add_centered_text(715,story['title'].upper(),'F2',18,0)
        pdf.add_rect(100,400,412,270,1.5,0.3)
        pdf.add_centered_text(560,f"[ILLUSTRATION: {story['animal']} in Bible scene",'F3',9,0.4)
        pdf.add_centered_text(545,"with detailed, colorful artwork]",'F3',9,0.4)
        for i,line in enumerate(wrap_text(story['p1'],80)):
            pdf.add_text(72,370-i*18,line,'F4',11,0.1)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (continued)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(story['p2'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        pdf.add_rect(100,y-260,412,240,1.5,0.3)
        pdf.add_centered_text(y-120,f"[ILLUSTRATION: {story['animal']} action scene]",'F3',9,0.4)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (conclusion)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(story['p3'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=15
        pdf.add_filled_rect(72,y-30,468,40,0.9)
        pdf.add_centered_text(y-5,"KEY BIBLE VERSE:",'F2',10,0.2)
        pdf.add_centered_text(y-22,story['verse'],'F4',11,0)
        y-=55
        pdf.add_rect(72,y-40,468,50,2,0.2)
        pdf.add_centered_text(y-5,"MORAL:",'F2',11,0.1)
        pdf.add_centered_text(y-25,story['moral'],'F5',11,0)
        y-=60
        pdf.add_filled_rect(72,y-40,468,45,0.93)
        pdf.add_text(80,y-8,"ANIMAL SCIENCE FACT:",'F2',10,0.1)
        for i,fl in enumerate(wrap_text(story['fact'],70)):
            pdf.add_text(80,y-25-i*14,fl,'F4',9,0.2)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"WHAT I LEARNED",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_text(72,710,f"Reflecting on: {story['title']}",'F4',11,0.2)
        qs=[f"1. What role did the {story['animal'].lower()} play in this story?",
            "2. What does this story teach us about God?",
            "3. What is the most amazing thing about this animal?"]
        y=670
        for q in qs:
            pdf.add_text(72,y,q,'F2',11,0.1); y-=20
            for _ in range(3): pdf.add_line(90,y,530,y,0.5,0.6); y-=20
            y-=10
        pdf.add_filled_rect(72,y-120,468,130,0.92)
        pdf.add_centered_text(y-5,"MY PRAYER",'F2',14,0.1)
        pdf.add_text(80,y-25,"Thank you God for creating amazing animals like...",'F4',10,0.2)
        for i in range(5): pdf.add_line(80,y-50-i*20,520,y-50-i*20,0.5,0.6)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"WORD SEARCH PUZZLE",'F2',16,0)
        pdf.add_text(72,720,f"Find words about: {story['animal']}",'F4',11,0.2)
        grid=generate_word_search(story['words']); y=680
        for row in grid: pdf.add_centered_text(y,"   ".join(row),'F3',14,0.1); y-=24
        y-=20; pdf.add_text(72,y,"Words to find:",'F2',11,0.1); y-=20
        pdf.add_text(72,y,"  ".join(story['words']),'F3',10,0.2)
        y-=40; pdf.add_text(72,y,"BONUS: What other animals are in the Bible?",'F4',10,0.3)
        for _ in range(3): y-=22; pdf.add_line(72,y,540,y,0.5,0.6)

        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"DRAW THE {story['animal'].upper()}!",'F2',16,0)
        pdf.add_text(72,720,f"Draw a {story['animal'].lower()} from this story:",'F4',11,0.2)
        pdf.add_rect(72,280,468,420,1.5,0.3)
        pdf.add_centered_text(260,"What is your favorite animal and why?",'F2',11,0.1)
        y=230
        for _ in range(4): pdf.add_line(72,y,540,y,0.5,0.6); y-=22


    # Quiz (2 pages)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 1",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    qs=[("1. Which animal tricked Eve in the Garden?","a) Lion  b) Serpent  c) Raven"),
        ("2. How many of each animal went on the ark?","a) 1  b) 2  c) 7"),
        ("3. What did Balaam's donkey see?","a) A lion  b) An angel  c) A fire"),
        ("4. What did ravens bring Elijah?","a) Water  b) Bread and meat  c) Fish"),
        ("5. How long was Jonah inside the fish?","a) 1 day  b) 3 days  c) 7 days")]
    y=700
    for q,o in qs: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 2",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    qs2=[("6. What animal did Jesus ride into Jerusalem?","a) Horse  b) Camel  c) Donkey"),
         ("7. Peter denied Jesus before the ____ crowed.","a) Eagle  b) Rooster  c) Dove"),
         ("8. What did David protect his sheep from?","a) Lions and bears  b) Wolves  c) Foxes"),
         ("9. Jesus is called the Lamb of ____","a) Peace  b) God  c) Israel"),
         ("10. What shut the lions' mouths for Daniel?","a) A stone  b) An angel  c) Chains")]
    y=700
    for q,o in qs2: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.add_text(72,y-20,"Answers: 1b, 2b, 3b, 4b, 5b, 6c, 7b, 8a, 9b, 10b",'F3',9,0.4)

    # Vocabulary
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"VOCABULARY & WORD LIST",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    vocab=[("Creature","Any living thing created by God"),("Flock","A group of sheep or birds"),
           ("Predator","An animal that hunts other animals"),("Sacrifice","An offering given to God"),
           ("Obedience","Following instructions willingly"),("Provision","God supplying what is needed"),
           ("Shepherd","Someone who cares for sheep"),("Habitat","The natural home of an animal"),
           ("Instinct","Natural behavior God built into animals"),("Stewardship","Caring for God's creation")]
    y=710
    for w,d in vocab: pdf.add_text(72,y,f"{w}:",'F2',11,0.1); pdf.add_text(200,y,d,'F4',10,0.2); y-=28

    # Journal (4 pages)
    prompts=["My favorite animal God created and why...","How animals show us God's creativity...",
             "An animal I want to learn more about...","How I can care for God's animal creation..."]
    for j in range(4):
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"MY FAITH JOURNAL - Page {j+1}",'F2',16,0)
        pdf.add_text(72,710,prompts[j],'F5',12,0.2); y=680
        for _ in range(24): pdf.add_line(72,y,540,y,0.5,0.7); y-=25

    # Certificate
    pdf.new_page(); pc+=1
    pdf.add_rect(50,50,512,692,3,0.2); pdf.add_rect(60,60,492,672,1.5,0.4)
    pdf.add_centered_text(680,"CERTIFICATE OF COMPLETION",'F2',22,0)
    pdf.add_centered_text(640,"This certifies that",'F4',14,0.2)
    pdf.add_line(180,600,432,600,1,0.3)
    pdf.add_centered_text(540,"has studied all 10 animal stories in",'F4',12,0.2)
    pdf.add_centered_text(510,TITLE,'F2',14,0)
    pdf.add_centered_text(400,"Date: _______________",'F4',12,0.3)
    pdf.add_centered_text(280,"\"Ask the animals, and they will teach you\" - Job 12:7",'F5',13,0.1)

    # Memory Verse Cards (2 pages)
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

    # Bonus
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MY ANIMAL FACTS COLLECTION",'F2',18,0)
    pdf.add_line(150,740,462,740,1,0.3)
    pdf.add_text(72,710,"Research and write one amazing fact about each animal:",'F4',11,0.2); y=680
    for i,s in enumerate(stories):
        pdf.add_text(72,y,f"{i+1}. {s['animal']}: ",'F2',10,0.1)
        pdf.add_line(180,y-2,540,y-2,0.5,0.6); y-=30

    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),FILENAME)
    pdf.save(out)
    print(f"Generated {FILENAME} with {pc} pages")
    return pc

if __name__=="__main__":
    build_pdf()
