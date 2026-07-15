#!/usr/bin/env python3
"""Book 281 - Bible Adventures: 10 Action-Packed Stories for Brave Kids"""
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc
random.seed(281)
TITLE = "BIBLE ADVENTURES"
SUBTITLE = "10 Action-Packed Stories for Brave Kids"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book281_Bible_Adventures_Kids.pdf"
stories = [
    {"title": "Red Sea Escape", "character": "Moses",
     "verse": "The LORD will fight for you. You only need to be still. - Exodus 14:14 (WEB)",
     "moral": "When danger surrounds you, God fights your battles!",
     "choice": "If you were trapped between an army and a sea, would you: A) Try to swim, B) Trust God's miracle, or C) Surrender?",
     "p1": "The night was dark and the sound of thundering hooves echoed across the desert. Six hundred Egyptian war chariots were racing toward the Israelites at full speed! Dust clouds billowed behind the massive army. Ahead, the Red Sea stretched endlessly with no bridge, no boats, and no escape. Two million people were trapped between the most powerful army in the world and miles of deep, churning water.",
     "p2": "Panic erupted everywhere. Women screamed, children cried, and men argued. Some wanted to surrender and go back to slavery. But Moses stood like a rock against the wind of fear. He raised his staff toward the sky and shouted above the chaos: 'STAND FIRM! Watch what the Lord will do today!' A massive pillar of fire moved between the Israelites and the Egyptian army, blocking the enemy while lighting the night for God's people.",
     "p3": "Moses stretched his hand over the sea and a supernatural wind roared to life! The waters split apart with a CRACK like thunder, rising into towering walls on both sides! A wide highway of dry ground appeared through the middle of the sea! The people rushed through with walls of water higher than buildings on each side, fish swimming behind the transparent walls! When the last person crossed safely, Moses let the walls collapse on the pursuing army. The greatest escape in history!",
     "words": ["ESCAPE", "SEA", "SPLIT", "CHASE", "ARMY", "MIRACLE", "DRY", "FREE"]},
    {"title": "Spy Mission at Jericho", "character": "the spies and Rahab",
     "verse": "Be strong and very courageous. - Joshua 1:7 (WEB)",
     "moral": "Courage means going into dangerous places when God sends you!",
     "choice": "Would you: A) Sneak into an enemy city alone, B) Send a drone (if you had one!), or C) Wait for more info?",
     "p1": "Joshua sent two of his bravest men on the most dangerous mission imaginable - sneak into the heavily fortified city of Jericho and spy out its defenses. The massive walls towered above them as they crept through the city gate disguised as travelers. Enemy soldiers patrolled everywhere. One wrong word, one suspicious look, and they would be captured and killed immediately.",
     "p2": "Word reached the king that Israelite spies had entered the city! Soldiers began searching house by house. The spies had taken shelter with a woman named Rahab whose house was built into the city wall itself. Rahab had heard about God's mighty power and believed He would give Jericho to Israel. She hid the spies under stalks of flax on her rooftop while soldiers searched below. When guards knocked on her door, she bravely lied to protect them, sending the search party in the wrong direction.",
     "p3": "In the dead of night, Rahab lowered the two spies down from her window on a scarlet rope - her house was on the outer wall! She asked them to spare her family when the attack came. They promised to protect anyone in her house marked by that red rope. The spies escaped into the hills, hiding for three days before returning to Joshua with their report: 'The people are terrified of us! God has given us this land!' The spy mission was a complete success thanks to one brave woman's faith.",
     "words": ["SPY", "JERICHO", "RAHAB", "ROPE", "HIDE", "WALL", "BRAVE", "SECRET"]},

    {"title": "Gideon's Night Raid", "character": "Gideon",
     "verse": "The sword of the LORD and of Gideon! - Judges 7:20 (WEB)",
     "moral": "With God, you don't need a big army - just big faith!",
     "choice": "Would you attack with: A) 300 men and torches, B) Wait for a bigger army, or C) Try to negotiate peace?",
     "p1": "The Midianite army stretched across the valley like a swarm of locusts - over 135,000 warriors with their camels. Against them stood Gideon with only 300 men! No swords, no shields - just clay jars, torches hidden inside, and ram horn trumpets. It was the most ridiculous battle plan in military history. But God had designed it that way so everyone would know HE won the victory.",
     "p2": "Under the cover of midnight darkness, Gideon divided his tiny force into three companies of 100 men each. They crept silently around the massive enemy camp, taking positions on three sides. Hearts pounding, hands trembling, they waited for Gideon's signal. The Midianite camp sprawled below them with thousands of tents and sleeping warriors. The night was perfectly still. Then Gideon raised his trumpet to his lips.",
     "p3": "SMASH! Three hundred clay jars shattered simultaneously! Blazing torches burst into light from every direction! 'THE SWORD OF THE LORD AND OF GIDEON!' three hundred voices roared into the night! Trumpets blasted from all sides! The sleeping Midianites woke in total chaos, thinking a massive army surrounded them. In the confusion, they turned their swords on each other and fled in every direction! Without swinging a single weapon, Gideon's 300 won the most incredible victory in Israel's history!",
     "words": ["GIDEON", "NIGHT", "TORCH", "JAR", "SHOUT", "THREE", "HUNDRED", "WIN"]},
    {"title": "David vs the Giant", "character": "David",
     "verse": "The battle is the LORD's! - 1 Samuel 17:47 (WEB)",
     "moral": "Giants fall when you fight with God on your side!",
     "choice": "Facing a giant, would you: A) Run away, B) Grab a sling like David, or C) Put on heavy armor?",
     "p1": "BOOM. BOOM. BOOM. Each thunderous footstep shook the ground as Goliath, the champion of the Philistines, marched into the valley between the two armies. He stood over NINE FEET TALL - a walking mountain of muscle covered in bronze armor that weighed 125 pounds. His spear was as thick as a weaving beam with an iron point weighing fifteen pounds. For forty days he had challenged Israel and no one dared face him.",
     "p2": "Then a teenage shepherd boy named David arrived with lunch for his brothers. When he heard Goliath's booming insults against God, fury blazed in his young heart. 'Who is this uncircumcised Philistine who defies the army of the LIVING GOD?' he demanded. King Saul tried to give David armor but it was too heavy. David stripped it off and walked toward the giant with nothing but his shepherd's staff, a sling, and five smooth stones from the stream.",
     "p3": "Goliath LAUGHED when he saw the boy. 'Am I a dog that you come at me with sticks?' But David sprinted toward the giant at full speed, reaching into his bag. His sling whirled overhead faster and faster - WHIP WHIP WHIP - then RELEASE! The stone flew like a bullet and struck Goliath square in the forehead with a sickening CRACK! The giant's eyes went blank. He crashed face-first into the dirt like a falling tower. The ground shook. The army of Israel ROARED and charged! One boy, one stone, one God - VICTORY!",
     "words": ["DAVID", "GIANT", "SLING", "STONE", "BATTLE", "BRAVE", "FAITH", "WIN"]},
    {"title": "Noah's Flood - Surviving the Storm", "character": "Noah",
     "verse": "Noah did everything just as God commanded. - Genesis 6:22 (WEB)",
     "moral": "Obedience to God keeps you safe even in the worst storms!",
     "choice": "If God told you to build a boat in your backyard, would you: A) Do it immediately, B) Ask questions first, or C) Ignore it?",
     "p1": "For over 100 years, Noah hammered, sawed, and built while everyone laughed. The ark was ENORMOUS - 450 feet long, 75 feet wide, and 45 feet tall! It looked ridiculous sitting on dry ground with no ocean anywhere nearby. People mocked Noah mercilessly. But Noah kept building because God had warned him that the greatest catastrophe in history was coming.",
     "p2": "When the ark was finally finished, something incredible happened. Animals began arriving from everywhere! Lions walked past Noah peacefully. Elephants thundered up the ramp. Eagles swooped in through the upper deck. Snakes slithered aboard. Mice scurried between the feet of hippos. Two by two, every kind of creature God created marched into the ark. Then God Himself shut the massive door with a thundering BOOM that echoed across the silent landscape.",
     "p3": "For seven days, nothing happened. Then the sky turned black. Lightning split the heavens. Rain exploded from the clouds with unimaginable force. Underground springs burst open like geysers. Water rose with terrifying speed - inches became feet, feet became fathoms. The ark lifted off the ground and began to float! Inside, Noah's family clung to each other as the boat rocked in the churning flood. For 40 days it rained without stopping. But inside the ark, every person and animal was perfectly safe. God's obedient servant survived the greatest storm in history!",
     "words": ["NOAH", "ARK", "FLOOD", "STORM", "ANIMALS", "RAIN", "SAFE", "OBEY"]},

    {"title": "Daniel in the Lions' Den", "character": "Daniel",
     "verse": "My God sent his angel and shut the lions' mouths. - Daniel 6:22 (WEB)",
     "moral": "Faith turns the scariest situations into incredible testimonies!",
     "choice": "Would you: A) Keep praying openly like Daniel, B) Pray in secret, or C) Stop praying for 30 days?",
     "p1": "The trap was set perfectly. Jealous officials had tricked King Darius into signing an unbreakable law - anyone who prayed to any god except the king for thirty days would be thrown to the lions. They knew Daniel prayed to God three times every day without fail. Soldiers hid outside Daniel's window, waiting. Sure enough, Daniel knelt before his open window and prayed boldly, just as he always had.",
     "p2": "The officials rushed to the king with their evidence. Darius was devastated - he loved Daniel! He spent the entire day trying to find a legal loophole, but Persian law was unchangeable. At sunset, soldiers dragged Daniel to the lions' den. The king whispered with a breaking voice, 'May your God rescue you.' Daniel was thrown into the darkness below. Hungry lions ROARED, their eyes glowing in the torchlight. A massive stone was rolled over the opening and sealed.",
     "p3": "King Darius could not sleep all night. At the first crack of dawn, he sprinted to the den. 'DANIEL! Has your God been able to save you?' Silence... then a calm voice echoed from below: 'O King, live forever! My God sent His angel and shut the lions' mouths. I am unhurt!' Guards hauled Daniel up - not a single scratch! The lions who had been starving for days had become gentle as kittens all night long. An angel had camped with Daniel in the den of death and turned it into a den of peace!",
     "words": ["DANIEL", "LIONS", "DEN", "ANGEL", "PRAYER", "KING", "SHUT", "SAFE"]},
    {"title": "Elijah's Fire from Heaven", "character": "Elijah",
     "verse": "The God who answers by fire, He is God! - 1 Kings 18:24 (WEB)",
     "moral": "The one true God always shows up when challenged!",
     "choice": "Would you: A) Challenge 450 false prophets alone, B) Wait for backup, or C) Run and hide?",
     "p1": "It was the ultimate showdown - one prophet of God against 450 prophets of the false god Baal on top of Mount Carmel! All of Israel gathered to watch. Elijah laid down the challenge: 'Build an altar, prepare a sacrifice, but light no fire. The god who answers by sending fire from heaven - HE is the true God!' The crowd held their breath. The prophets of Baal went first.",
     "p2": "From morning until afternoon, the 450 prophets danced, screamed, and begged Baal to send fire. They shouted until they were hoarse. They leaped around the altar wildly. Elijah taunted them: 'Shout louder! Maybe your god is sleeping! Maybe he's on vacation!' They screamed louder but nothing happened. Not a spark. Not a flicker. Complete silence from their false god. By afternoon, they collapsed in exhaustion and humiliation.",
     "p3": "Then Elijah rebuilt God's broken altar and laid the sacrifice on it. But then he did something CRAZY - he poured TWELVE huge jars of water over everything! The sacrifice was soaked. The wood was drenched. Water filled the trench around the altar! Then Elijah prayed one simple, quiet prayer. WHOOOOSH! Fire EXPLODED from the sky! Not ordinary fire - supernatural flames that consumed the sacrifice, the wood, the STONES, the dirt, and evaporated every drop of water! The people fell on their faces screaming: 'THE LORD - HE IS GOD!'",
     "words": ["ELIJAH", "FIRE", "HEAVEN", "ALTAR", "WATER", "PROVE", "PRAYER", "GOD"]},
    {"title": "Peter's Prison Break", "character": "Peter",
     "verse": "An angel of the Lord stood by him and a light shone. - Acts 12:7 (WEB)",
     "moral": "No prison can hold you when God decides to set you free!",
     "choice": "Chained between guards in prison, would you: A) Sleep peacefully like Peter, B) Stay awake worrying, or C) Try to escape yourself?",
     "p1": "King Herod had arrested the apostle Peter and planned to execute him the next morning. Peter was locked in the deepest cell of the maximum security prison, chained between TWO soldiers with guards at every door. It was impossible to escape. The entire church was praying desperately through the night for their beloved leader. But inside his cell, Peter was doing something remarkable - he was SLEEPING. Sound asleep between his guards, at total peace.",
     "p2": "Suddenly at midnight, a blazing light filled the dark cell! An angel appeared and struck Peter on the side: 'Quick, get up!' The chains fell off Peter's wrists with a CLANG! Peter thought he was dreaming. 'Put on your sandals. Wrap your cloak around you. Follow me,' the angel commanded. Peter obeyed in a daze, stepping over the sleeping guards. They walked past the first guard post - no one noticed. Past the second - still invisible!",
     "p3": "They reached the massive iron gate leading to the city. Without anyone touching it, the heavy gate swung open BY ITSELF! Peter and the angel walked through into the cool night air and down one street. Then the angel vanished! Peter finally realized he was actually awake - 'The Lord really sent His angel to rescue me!' He rushed to a house where Christians were praying for him. When the servant girl heard his voice, she was so shocked she forgot to open the door! God had broken Peter out of an unbreakable prison!",
     "words": ["PETER", "PRISON", "ANGEL", "CHAINS", "GATE", "FREE", "PRAYER", "LIGHT"]},

    {"title": "Paul's Shipwreck", "character": "Paul",
     "verse": "Not a hair will perish from the head of any of you. - Acts 27:34 (WEB)",
     "moral": "God's promises hold even in the worst catastrophes!",
     "choice": "In a sinking ship, would you: A) Trust God like Paul, B) Panic, or C) Abandon the mission?",
     "p1": "Paul was a prisoner on a ship heading to Rome when the most terrifying storm in memory struck. For FOURTEEN DAYS the ship was battered by hurricane-force winds! The sun and stars disappeared behind black clouds. Waves crashed over the deck. The crew threw cargo overboard to lighten the ship. They wrapped ropes around the hull to keep it from breaking apart. All hope of survival was lost.",
     "p2": "While 276 people on board despaired for their lives, Paul stood up with confidence. 'Take heart, men! Last night an angel told me that God will save everyone on this ship! Not one person will die - but we will run aground on an island.' The sailors did not quite believe it, but Paul's calm faith steadied their nerves. He even made everyone EAT a meal, giving thanks to God in the middle of the storm! Fourteen days without food, and Paul was hosting dinner.",
     "p3": "On the fourteenth night, the sailors sensed land was near. At dawn, they spotted a bay with a beach! They cut the anchors, raised a sail, and aimed for shore. CRUNCH! The ship hit a sandbar and the stern began breaking apart under the pounding waves! Soldiers wanted to kill the prisoners to prevent escape, but the centurion stopped them to save Paul. Everyone jumped into the raging sea - some swimming, some clinging to broken planks. And just as God promised through Paul, all 276 people made it safely to shore on the island of Malta! Not one life was lost!",
     "words": ["PAUL", "SHIP", "STORM", "WRECK", "WAVES", "ANGEL", "SAFE", "ISLAND"]},
    {"title": "The Empty Tomb - Greatest Adventure Ever", "character": "the women and disciples",
     "verse": "He is not here! He is risen! - Luke 24:6 (WEB)",
     "moral": "The greatest adventure is discovering that death has been DEFEATED!",
     "choice": "Finding an empty tomb, would you: A) Run to tell everyone, B) Look inside, or C) Both!",
     "p1": "It was early Sunday morning, still dark, when several women crept toward the tomb where Jesus had been buried. They carried burial spices, their hearts heavy with grief. Their beloved teacher was dead. A massive stone blocked the entrance and Roman soldiers guarded it. How would they even get inside? Every step felt heavier than the last as they walked through the pre-dawn darkness.",
     "p2": "Suddenly the ground SHOOK! An earthquake rocked the area as an angel descended from heaven like lightning! The angel rolled the enormous stone away as easily as a pebble. The Roman guards - trained elite soldiers - fainted in terror! When the women arrived, they found the stone moved, the guards unconscious, and the tomb OPEN. Heart pounding, they peered inside. The burial cloths were there, neatly folded... but Jesus' body was GONE!",
     "p3": "The angel spoke: 'Do not be afraid! You are looking for Jesus who was crucified. HE IS NOT HERE - HE IS RISEN!' Then Jesus Himself appeared to them, alive and glorious! Mary Magdalene grabbed His feet. 'Go tell my brothers!' Jesus said. The women SPRINTED back to the disciples with the most incredible news in human history - DEATH HAD BEEN DEFEATED! Jesus was alive! The tomb was empty! The greatest adventure of all time reached its triumphant climax - love won, death lost, and hope was reborn forever!",
     "words": ["RISEN", "TOMB", "EMPTY", "ALIVE", "ANGEL", "STONE", "HOPE", "SUNDAY"]}
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
    pdf.add_centered_text(720,TITLE,'F2',28,0)
    pdf.add_centered_text(690,SUBTITLE,'F4',14,0.2)
    pdf.add_centered_text(660,"Written and Illustrated by",'F4',12,0.3)
    pdf.add_centered_text(640,AUTHOR,'F2',16,0)
    pdf.add_rect(100,200,412,380,2,0.3)
    pdf.add_centered_text(420,"[ILLUSTRATION: Epic adventure collage - parting sea,",'F3',10,0.4)
    pdf.add_centered_text(405,"boy vs giant, shipwreck, prison break]",'F3',10,0.4)
    pdf.add_centered_text(100,"Are you ready for the adventure of a lifetime?",'F4',12,0.3)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(700,TITLE,'F2',16,0)
    pdf.add_text(72,600,f"Written by {AUTHOR}",'F4',11,0.2)
    pdf.add_text(72,580,"Copyright 2025. All Rights Reserved.",'F4',10,0.3)
    pdf.add_text(72,550,"Scripture: World English Bible (WEB) - Public Domain.",'F4',10,0.3)
    pdf.add_text(72,520,"For children ages 6-12. Published by Kingdom Kids Publishing",'F4',10,0.3)
    pdf.add_text(72,440,"Dedication: For every kid who loves action and adventure - God's stories are the BEST!",'F4',10,0.2)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"TABLE OF CONTENTS",'F2',18,0)
    pdf.add_line(150,720,462,720,1,0.3); y=680
    for i,s in enumerate(stories):
        pdf.add_text(72,y,f"Adventure {i+1}: {s['title']}",'F4',12,0.1); y-=28
    pdf.add_text(72,y-10,"Quiz / Vocabulary / Journal / Certificate / Bonus",'F4',10,0.3)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"HOW TO USE THIS BOOK",'F2',18,0)
    pdf.add_line(150,720,462,720,1,0.3)
    intro=["GET READY FOR THE MOST EXCITING STORIES EVER TOLD!","",
        "These are REAL adventures from the Bible - not made up!","Every story actually happened to real people!","",
        "Each adventure has SIX pages:","  1. The adventure begins! (with illustration)",
        "  2. The action intensifies! (with scene)","  3. The epic conclusion + verse + 'What Would YOU Do?'",
        "  4. Reflection + prayer","  5. Word search puzzle","  6. Draw the adventure!","",
        "SPECIAL FEATURE: Each story has a 'What Would YOU Do?'","choice where you decide how you would handle the situation!","",
        "Buckle up, adventurer. Here we go!"]
    y=680
    for l in intro: pdf.add_text(72,y,l,'F4',11,0.15); y-=22


    for idx, story in enumerate(stories):
        pdf.new_page(); pc+=1
        pdf.add_filled_rect(50,700,512,60,0.88)
        pdf.add_centered_text(735,f"Adventure {idx+1}",'F1',10,0.4)
        pdf.add_centered_text(715,story['title'].upper(),'F2',18,0)
        pdf.add_rect(100,400,412,270,1.5,0.3)
        pdf.add_centered_text(560,f"[ILLUSTRATION: Epic action scene - {story['title']}",'F3',9,0.4)
        pdf.add_centered_text(545,"with dramatic lighting and movement]",'F3',9,0.4)
        for i,line in enumerate(wrap_text(story['p1'],80)):
            pdf.add_text(72,370-i*18,line,'F4',11,0.1)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (the action builds!)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(story['p2'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        pdf.add_rect(100,y-260,412,240,1.5,0.3)
        pdf.add_centered_text(y-120,"[ILLUSTRATION: Intense action moment!",'F3',9,0.4)
        pdf.add_centered_text(y-135,f"{story['character']} facing incredible odds]",'F3',9,0.4)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{story['title']} (EPIC CONCLUSION!)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(story['p3'],80): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=12
        pdf.add_filled_rect(72,y-30,468,40,0.9)
        pdf.add_centered_text(y-5,"KEY BIBLE VERSE:",'F2',10,0.2)
        pdf.add_centered_text(y-22,story['verse'],'F4',11,0)
        y-=50
        pdf.add_rect(72,y-50,468,55,2,0.2)
        pdf.add_centered_text(y-5,"WHAT WOULD YOU DO?",'F2',11,0.1)
        for i,cl in enumerate(wrap_text(story['choice'],70)):
            pdf.add_text(80,y-22-i*14,cl,'F4',10,0.2)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"ADVENTURE REFLECTION",'F2',16,0)
        pdf.add_line(150,740,462,740,1,0.3)
        qs=["1. What was the most exciting moment in this adventure?",
            f"2. How did {story['character']} show faith under pressure?",
            "3. What would you have done differently?"]
        y=700
        for q in qs:
            pdf.add_text(72,y,q,'F2',11,0.1); y-=20
            for _ in range(3): pdf.add_line(90,y,530,y,0.5,0.6); y-=20
            y-=10
        pdf.add_filled_rect(72,y-120,468,130,0.92)
        pdf.add_centered_text(y-5,"MY ADVENTURE PRAYER",'F2',14,0.1)
        pdf.add_text(80,y-25,"God, give me the courage to face my own adventures...",'F4',10,0.2)
        for i in range(5): pdf.add_line(80,y-50-i*20,520,y-50-i*20,0.5,0.6)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"WORD SEARCH PUZZLE",'F2',16,0)
        pdf.add_text(72,720,f"Find words from: {story['title']}",'F4',11,0.2)
        grid=generate_word_search(story['words']); y=680
        for row in grid: pdf.add_centered_text(y,"   ".join(row),'F3',14,0.1); y-=24
        y-=20; pdf.add_text(72,y,"Words:",'F2',11,0.1); y-=20
        pdf.add_text(72,y,"  ".join(story['words']),'F3',10,0.2)
        y-=40; pdf.add_text(72,y,"Rate this adventure! Circle: 1 2 3 4 5 (5 = AMAZING!)",'F4',10,0.3)
        for _ in range(2): y-=22; pdf.add_line(72,y,540,y,0.5,0.6)
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"DRAW THIS ADVENTURE!",'F2',16,0)
        pdf.add_text(72,720,f"Draw the most exciting scene from: {story['title']}",'F4',11,0.2)
        pdf.add_rect(72,280,468,420,1.5,0.3)
        pdf.add_centered_text(260,"My biggest adventure this week will be:",'F2',11,0.1)
        y=230
        for _ in range(4): pdf.add_line(72,y,540,y,0.5,0.6); y-=22


    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 1",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs=[("1. How many chariots chased the Israelites?","a) 100  b) 600  c) 1000"),
        ("2. Who hid the spies in Jericho?","a) Rahab  b) Ruth  c) Esther"),
        ("3. How many warriors did Gideon have?","a) 3000  b) 300  c) 30"),
        ("4. What did David use to defeat Goliath?","a) Sword  b) Sling  c) Spear"),
        ("5. How long did it rain in Noah's flood?","a) 7 days  b) 40 days  c) 100 days")]
    y=700
    for q,o in qs: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"QUIZ TIME! - Part 2",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs2=[("6. What shut the lions' mouths?","a) Chain  b) Angel  c) Stone"),
         ("7. How many jars of water did Elijah use?","a) 3  b) 7  c) 12"),
         ("8. How was Peter chained in prison?","a) By feet  b) Between 2 guards  c) To wall"),
         ("9. How many people survived Paul's shipwreck?","a) 76  b) 176  c) 276"),
         ("10. What day did Jesus rise from the dead?","a) Friday  b) Saturday  c) Sunday")]
    y=700
    for q,o in qs2: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.add_text(72,y-20,"Answers: 1b, 2a, 3b, 4b, 5b, 6b, 7c, 8b, 9c, 10c",'F3',9,0.4)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"VOCABULARY & WORD LIST",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    vocab=[("Adventure","An exciting or daring experience"),("Courageous","Brave in the face of danger"),
           ("Supernatural","Beyond natural explanation - God's power"),("Catastrophe","A sudden great disaster"),
           ("Deliverance","Being rescued from danger or captivity"),("Impossible","Something beyond human ability"),
           ("Providence","God's protective care and guidance"),("Testimony","A story of what God has done"),
           ("Triumph","A great victory or achievement"),("Unstoppable","Cannot be prevented or stopped")]
    y=710
    for w,d in vocab: pdf.add_text(72,y,f"{w}:",'F2',11,0.1); pdf.add_text(200,y,d,'F4',10,0.2); y-=28

    prompts=["The most adventurous thing I have ever done...","An adventure I want God to take me on...",
             "A time God helped me when I was scared...","My adventure prayer for this week..."]
    for j in range(4):
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"MY ADVENTURE JOURNAL - Page {j+1}",'F2',16,0)
        pdf.add_text(72,710,prompts[j],'F5',12,0.2); y=680
        for _ in range(24): pdf.add_line(72,y,540,y,0.5,0.7); y-=25

    pdf.new_page(); pc+=1
    pdf.add_rect(50,50,512,692,3,0.2); pdf.add_rect(60,60,492,672,1.5,0.4)
    pdf.add_centered_text(680,"CERTIFICATE OF COMPLETION",'F2',22,0)
    pdf.add_centered_text(640,"This certifies that",'F4',14,0.2)
    pdf.add_line(180,600,432,600,1,0.3)
    pdf.add_centered_text(540,"has completed all 10 adventures in",'F4',12,0.2)
    pdf.add_centered_text(510,"BIBLE ADVENTURES",'F2',16,0)
    pdf.add_centered_text(400,"Date: _______________",'F4',12,0.3)
    pdf.add_centered_text(280,"\"Be strong and courageous!\" - Joshua 1:9",'F5',14,0.1)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS",'F2',18,0); y=690
    for i,s in enumerate(stories[:5]):
        pdf.add_rect(72,y-55,468,55,1,0.3)
        pdf.add_text(80,y-15,f"Card {i+1}: {s['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,s['verse'],'F4',9,0.2); y-=65
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS (cont.)",'F2',18,0); y=700
    for i,s in enumerate(stories[5:]):
        pdf.add_rect(72,y-55,468,55,1,0.3)
        pdf.add_text(80,y-15,f"Card {i+6}: {s['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,s['verse'],'F4',9,0.2); y-=65

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MY ADVENTURE RANKING",'F2',18,0)
    pdf.add_text(72,710,"Rank all 10 adventures from most exciting to least:",'F4',11,0.2); y=680
    for i in range(10):
        pdf.add_text(72,y,f"#{i+1}:",'F2',11,0.1); pdf.add_line(110,y-2,540,y-2,0.5,0.6); y-=28
    pdf.add_text(72,y-20,"The adventure that made me feel MOST brave:",'F4',10,0.2)
    pdf.add_line(72,y-40,540,y-40,0.5,0.6)

    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),FILENAME)
    pdf.save(out); print(f"Generated {FILENAME} with {pc} pages"); return pc

if __name__=="__main__": build_pdf()
