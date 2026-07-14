#!/usr/bin/env python3
"""Book 276 - Heroes of Courage: 10 Amazing Bible Stories About Brave Kids & Adults"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Helper functions
    def draw_decorative_border(pdf, x, y, w, h, gray=0.3):
        pdf.add_rect(x, y, w, h, line_width=2, gray=gray)
        pdf.add_rect(x+3, y+3, w-6, h-6, line_width=0.5, gray=gray)

    def draw_section_header(pdf, y, title, gray_bg=0.92):
        pdf.add_filled_rect(50, y-5, 512, 30, gray=gray_bg)
        pdf.add_text(60, y+5, title, font='F2', size=14, gray=0.1)
        pdf.add_line(50, y-5, 562, y-5, width=1.5, gray=0.3)

    def draw_illustration_box(pdf, y, description, height=100):
        pdf.add_filled_rect(60, y, 492, height, gray=0.95)
        pdf.add_rect(60, y, 492, height, line_width=1.5, gray=0.4)
        pdf.add_text(70, y+height-20, "[ILLUSTRATION:", font='F2', size=10, gray=0.3)
        words = description.split()
        line = ""
        line_y = y + height - 35
        for word in words:
            if len(line + " " + word) > 75:
                pdf.add_text(70, line_y, line.strip(), font='F3', size=9, gray=0.4)
                line_y -= 13
                line = word
            else:
                line = line + " " + word if line else word
        if line:
            pdf.add_text(70, line_y, line.strip(), font='F3', size=9, gray=0.4)
        pdf.add_text(70, line_y-15, "]", font='F2', size=10, gray=0.3)

    def wrap_text(pdf, x, y, text, font='F4', size=11, max_width=70, gray=0):
        words = text.split()
        line = ""
        curr_y = y
        for word in words:
            if len(line + " " + word) > max_width:
                pdf.add_text(x, curr_y, line.strip(), font=font, size=size, gray=gray)
                curr_y -= 15
                line = word
            else:
                line = line + " " + word if line else word
        if line:
            pdf.add_text(x, curr_y, line.strip(), font=font, size=size, gray=gray)
            curr_y -= 15
        return curr_y


    # ============ TITLE PAGE ============
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    draw_decorative_border(pdf, 30, 30, 552, 732, gray=0.2)
    pdf.add_filled_rect(50, 600, 512, 120, gray=0.88)
    pdf.add_centered_text(690, "HEROES OF COURAGE", font='F2', size=28, gray=0.1)
    pdf.add_centered_text(655, "10 Amazing Bible Stories About", font='F5', size=18, gray=0.2)
    pdf.add_centered_text(630, "Brave Kids & Adults", font='F5', size=18, gray=0.2)
    pdf.add_centered_text(560, "Stories of Faith, Bravery & Standing Strong", font='F4', size=14, gray=0.3)
    draw_illustration_box(pdf, 350, "A montage of Bible heroes: young David with sling, Queen Esther in royal robes, Daniel praying calmly surrounded by lions, all against a golden sunrise background with dramatic clouds", 150)
    pdf.add_centered_text(300, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(270, "With Vivid Illustrations, Moral Lessons & Activities", font='F4', size=12, gray=0.4)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)
    pdf.add_line(200, 90, 412, 90, width=1, gray=0.5)

    # ============ COPYRIGHT PAGE ============
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "HEROES OF COURAGE", font='F2', size=16, gray=0.1)
    pdf.add_text(72, 675, "10 Amazing Bible Stories About Brave Kids & Adults", font='F4', size=12, gray=0.3)
    pdf.add_line(72, 665, 400, 665, width=0.5, gray=0.5)
    pdf.add_text(72, 640, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 620, "No part of this book may be reproduced without permission.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 590, "Scripture quotations from the World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 560, "Written and designed for children ages 5-15", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 530, "Illustrations described for future artist collaboration", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 60, gray=0.92)
    pdf.add_text(72, 135, "Dedicated to every child who needs courage today -", font='F5', size=11, gray=0.2)
    pdf.add_text(72, 115, "God is always with you!", font='F5', size=11, gray=0.2)


    # ============ STORY DATA ============
    stories = [
        {
            "title": "DAVID vs GOLIATH",
            "subtitle": "A Boy Defeats a Giant with Faith",
            "illustration_a": "Young David, about 12 years old with curly brown hair, standing confidently in a green valley. He wears a simple shepherd's tunic and holds a leather sling. Before him towers Goliath, a 9-foot warrior in bronze armor. The Israelite army watches from hills behind David. Blue sky with dramatic clouds.",
            "opening": "Everyone was afraid of the giant. For forty days, Goliath had shouted terrible challenges at Israel's army. But one young shepherd boy named David heard those words and felt something burn in his heart - not fear, but faith.",
            "illustration_b": "David in mid-swing, his sling whirling above his head in a circular motion. His eyes are focused and determined. The smooth stone is about to fly. Goliath's massive shield and spear are visible. Dust rises from the valley floor. Other soldiers watch in amazement from both hillsides.",
            "middle": "David refused the king's heavy armor. Instead, he picked five smooth stones from the brook. The army gasped - was this boy crazy? Goliath laughed and mocked him. But David shouted back with boldness that shook the valley.",
            "brave_moment": "David swung his sling with all his might. The stone flew straight and true, striking the giant's forehead. Goliath crashed to the ground like a falling tower!",
            "resolution": "The Philistine army fled in terror. Israel celebrated their impossible victory. David proved that with God's help, even the smallest person can overcome the biggest problem.",
            "moral": "Size doesn't matter to God. When you face 'giants' in life - big problems, scary situations, bullies - remember that God is bigger than any giant!",
            "verse": "The LORD who delivered me out of the paw of the lion and the bear will deliver me out of the hand of this Philistine. - 1 Samuel 17:37 (WEB)",
            "prayer": "Dear God, help me be brave like David when I face my own giants. Remind me that You are always bigger than my problems. Amen.",
            "activity": "Draw YOUR giant - what is something big and scary you need to face? Now draw yourself standing brave with God beside you!"
        },
        {
            "title": "ESTHER THE BRAVE QUEEN",
            "subtitle": "A Girl Saves Her People",
            "illustration_a": "Beautiful young Queen Esther in a deep purple royal gown with golden crown, standing at the entrance to the king's throne room. Her face shows determination mixed with nervousness. Golden pillars line the hall. Persian tapestries hang on walls. Light streams through arched windows.",
            "opening": "Esther had a secret - she was Jewish. The wicked Haman had tricked the king into signing a terrible law. Now all her people would be destroyed unless someone was brave enough to speak up.",
            "illustration_b": "Esther kneeling before King Xerxes on his golden throne, her arms outstretched in pleading. The king extends his golden scepter toward her, showing mercy. Haman lurks in the shadows looking guilty. Rich Persian decorations fill the palace room with deep reds and golds.",
            "middle": "Going to the king without being called meant death. Esther fasted for three days, asking all her people to pray. Her cousin Mordecai reminded her: maybe she became queen for this very moment! Esther took a deep breath and made her choice. She said the famous words: 'If I perish, I perish.'",
            "brave_moment": "Esther walked into the throne room uninvited. The king could have ordered her death. But when he saw her, he extended his golden scepter - she would live! And she would save her people!",
            "resolution": "Esther exposed Haman's evil plot at a banquet. The king reversed the terrible law. The Jewish people were saved because one young woman chose courage over comfort.",
            "moral": "Sometimes God puts you in a special position for a reason. Don't be afraid to speak up for what's right, even when it's scary!",
            "verse": "Who knows if you haven't come to the kingdom for such a time as this? - Esther 4:14 (WEB)",
            "prayer": "Dear God, give me Esther's courage to speak up for others who need help, even when it feels risky. Use me where You've placed me. Amen.",
            "activity": "Think of someone who needs you to speak up for them. Write down one brave thing you can do this week to help them."
        },

        {
            "title": "DANIEL IN THE LIONS' DEN",
            "subtitle": "A Man Who Wouldn't Stop Praying",
            "illustration_a": "Daniel, a dignified man with gray-streaked beard wearing a blue and white robe, kneeling at his open window in prayer. The city of Babylon is visible through the window with its hanging gardens and ziggurats. Golden sunset light bathes the scene. His face is peaceful and trusting.",
            "opening": "Daniel prayed three times every day, no matter what. When jealous officials convinced the king to make prayer illegal, Daniel had a choice: hide his faith or keep praying openly.",
            "illustration_b": "Daniel standing calmly in a dark stone pit, surrounded by seven massive golden-maned lions. An angel in brilliant white stands behind Daniel with outstretched wings. The lions are lying down peacefully like kittens. Moonlight streams in from above through the pit opening.",
            "middle": "Daniel didn't even hesitate. He went home, opened his window toward Jerusalem, and prayed just as he always did. His enemies watched and reported him immediately. The king was heartbroken but couldn't break his own law. Daniel was thrown into the lion's den that very night.",
            "brave_moment": "The lions surrounded Daniel in the darkness. But instead of attacking, they lay down at his feet like gentle lambs. God had sent an angel to shut their mouths! Daniel slept peacefully among the beasts.",
            "resolution": "At dawn, the king rushed to the den and found Daniel alive and unharmed. The king declared that Daniel's God was the living God. Daniel's faithfulness in prayer saved his life and glorified God before the whole kingdom.",
            "moral": "Never stop talking to God, no matter what others say or do. Prayer is your most powerful weapon, and God always hears you!",
            "verse": "My God sent his angel and shut the lions' mouths. - Daniel 6:22 (WEB)",
            "prayer": "Dear God, help me pray every day no matter what. Thank You for protecting me like You protected Daniel. Amen.",
            "activity": "Set a prayer time today! Pick 3 times you'll talk to God - morning, lunch, and bedtime. Write them here and keep the habit!"
        },
        {
            "title": "SHADRACH, MESHACH & ABEDNEGO",
            "subtitle": "Three Friends in the Fire",
            "illustration_a": "Three young men in colorful Babylonian robes (red, blue, green) standing together with arms crossed, looking defiantly at a massive golden statue towering 90 feet high. Everyone else is bowing down around them. King Nebuchadnezzar points angrily from his throne. Desert sun blazes overhead.",
            "opening": "The king built a giant golden statue and commanded everyone to bow down to it. Music would play, and everyone must worship. But three young friends made a pact: they would bow to no one but God.",
            "illustration_b": "The three friends walking calmly inside a roaring furnace with orange and yellow flames all around them. Their robes are untouched by fire. A mysterious fourth figure glows brilliant white beside them - like a divine being. Guards at the furnace door shield their faces from the heat.",
            "middle": "When the music played, everyone fell to their knees - except three brave friends standing tall. The king was furious! He ordered the furnace heated seven times hotter. Soldiers tied them up and threw them in. The heat was so intense it killed the soldiers who threw them!",
            "brave_moment": "The king leaped to his feet in shock. 'Didn't we throw three men in?' he cried. 'I see FOUR men walking in the fire - and the fourth looks like a son of the gods!' The fire couldn't touch them!",
            "resolution": "When they walked out, not a single hair was singed. Their clothes didn't even smell like smoke! The king promoted them and declared their God the most powerful of all.",
            "moral": "When friends stand together for what's right, God stands with them. You're never alone when you choose to do the right thing!",
            "verse": "Our God whom we serve is able to deliver us from the burning fiery furnace. - Daniel 3:17 (WEB)",
            "prayer": "Dear God, thank You for friends who stand with me. Help me be a faithful friend who never gives up doing right. Amen.",
            "activity": "Write the names of 3 friends you can count on to do the right thing with you. Plan to encourage them this week!"
        },

        {
            "title": "JOSHUA AT JERICHO",
            "subtitle": "Walls Come Tumbling Down",
            "illustration_a": "Joshua, a strong warrior with a red cloak and sword at his side, looking up at the massive stone walls of Jericho. The walls are 25 feet thick and tower high. Behind Joshua, the Israelite army stretches across the desert plains. Seven priests hold golden rams' horn trumpets. Morning light glints off the walls.",
            "opening": "Jericho's walls were the strongest in the land - thick enough to drive chariots on top! No army could break through. But God gave Joshua the strangest battle plan anyone had ever heard.",
            "illustration_b": "The Israelite army marching in a perfect circle around Jericho's walls. Priests in white carry the golden Ark of the Covenant. Seven priests blow rams' horn trumpets. People on Jericho's walls look down in confusion. Dust rises from thousands of marching feet. The sky is deep blue.",
            "middle": "God's plan: March around the city once a day for six days. Don't talk. Don't shout. Just march in silence. On the seventh day, march seven times. Then blow trumpets and SHOUT! The people obeyed even though it seemed crazy. The people of Jericho watched in confusion from their walls.",
            "brave_moment": "On the seventh day, after the seventh lap, Joshua raised his hand. Trumpets blasted! The people gave a mighty SHOUT! And the impossible happened - those massive walls crumbled and crashed to the ground like sand castles!",
            "resolution": "Israel walked straight into the city over the rubble. God had fought the battle for them! They learned that obedience to God's unusual plans brings incredible victories.",
            "moral": "God's plans might seem strange to us, but they always work! Trust Him even when His instructions don't make sense to you.",
            "verse": "By faith the walls of Jericho fell down after they had been marched around for seven days. - Hebrews 11:30 (WEB)",
            "prayer": "Dear God, help me trust Your plans even when they seem unusual. I know You see what I cannot see. Amen.",
            "activity": "Think of something God might be asking you to do that seems strange or hard. Write it down and commit to trusting Him with it!"
        },
        {
            "title": "GIDEON'S 300",
            "subtitle": "God Uses the Few to Defeat the Many",
            "illustration_a": "Gideon, a young farmer with uncertain eyes but growing confidence, standing by a spring where soldiers drink water. Some lap water from their hands (alert and watchful) while others kneel face-down to drink. A massive Midianite army camp fills the valley below with countless tents like locusts. Torches and clay jars sit nearby.",
            "opening": "The Midianite army was huge - 135,000 warriors! Gideon gathered 32,000 Israelites, but God said: 'Too many. I want Israel to know I won the victory.' God kept reducing the army until only 300 remained.",
            "illustration_b": "300 warriors on a dark hillside, each holding a blazing torch inside a clay jar in one hand and a trumpet in the other. Below them, the massive Midianite camp sleeps. Stars fill the night sky. Gideon leads at the front, raising his torch. The scene is dramatic with orange torch light against deep blue darkness.",
            "middle": "Only 300 men against 135,000! God's plan was wild: no swords, just torches hidden in clay jars and trumpets. At midnight, they surrounded the enemy camp. Gideon gave the signal. Every man smashed his jar, held up his blazing torch, blew his trumpet, and shouted: 'A sword for the LORD and for Gideon!'",
            "brave_moment": "The sleeping Midianites woke to blazing lights and trumpet blasts from every direction! In their panic, they turned on each other with their swords and fled in total chaos! God won the battle with just 300 obedient warriors!",
            "resolution": "The massive army was completely routed by 300 men with torches and trumpets. God proved that His power doesn't depend on numbers. He can do amazing things with anyone willing to obey.",
            "moral": "God doesn't need big numbers or strong armies. He can use YOU - just one person willing to be brave and obey!",
            "verse": "Not by might, nor by power, but by my Spirit, says the LORD. - Zechariah 4:6 (WEB)",
            "prayer": "Dear God, even when I feel small or outnumbered, remind me that Your power is more than enough. Use me! Amen.",
            "activity": "Write about a time you felt outnumbered or outmatched. How might God want to use that situation for His glory?"
        },

        {
            "title": "RUTH THE LOYAL",
            "subtitle": "Following God to a New Land",
            "illustration_a": "Ruth, a beautiful young Moabite woman with olive skin and dark braided hair, walking alongside her elderly mother-in-law Naomi on a dusty road. Ruth wears a simple brown traveling dress and carries a small bundle. Behind them, the land of Moab fades into distance. Ahead, green hills of Bethlehem appear. Golden wheat fields shimmer in sunlight.",
            "opening": "Ruth had every reason to stay home in Moab. Her husband had died. She could go back to her family, find a new husband, live comfortably. But she looked at her heartbroken mother-in-law Naomi and made the bravest choice of all: loyalty.",
            "illustration_b": "Ruth bent over in a golden wheat field at sunrise, carefully gathering leftover grain stalks. Her face shows determination despite tiredness. In the background, the wealthy landowner Boaz watches her with admiration from the edge of the field. Other workers harvest nearby. Rolling hills of Bethlehem surround the scene.",
            "middle": "Ruth spoke words so beautiful they're still quoted today: 'Where you go, I will go. Your people will be my people. Your God will be my God.' She left everything familiar. In Bethlehem, she worked in the fields picking up leftover grain just to feed herself and Naomi. She never complained.",
            "brave_moment": "Ruth's loyal love caught the attention of Boaz, a kind and wealthy relative. Her faithfulness was rewarded! But even greater - Ruth became the great-grandmother of King David and an ancestor of Jesus himself!",
            "resolution": "From a poor foreign widow to a woman in Jesus' family line! God honored Ruth's loyalty beyond anything she could imagine. Her story proves that faithful love is the bravest choice of all.",
            "moral": "Loyalty and kindness are their own kind of courage. When you stick by people who need you, God sees and rewards your faithfulness!",
            "verse": "Where you go, I will go; and where you stay, I will stay. Your people will be my people, and your God my God. - Ruth 1:16 (WEB)",
            "prayer": "Dear God, help me be loyal like Ruth. Give me courage to stick with people who need me, even when it's hard. Amen.",
            "activity": "Write a loyalty pledge to someone important in your life. What can you promise to do for them no matter what?"
        },
        {
            "title": "JOSEPH THE DREAMER",
            "subtitle": "From Prison to Palace",
            "illustration_a": "Young Joseph, about 17, wearing a magnificent coat of many colors (red, blue, purple, gold, green stripes) standing in a field. His eleven brothers glare at him with jealousy from behind. Sheaves of wheat bow toward his sheaf in the background, representing his dream. Bright sunlight and blue sky above.",
            "opening": "Joseph had dreams that made his brothers furious - dreams of them bowing down to him! Their jealousy grew so terrible that they threw him into a pit and sold him as a slave. At just seventeen, Joseph lost everything.",
            "illustration_b": "Joseph standing before Pharaoh in an Egyptian palace with golden pillars and hieroglyphics on walls. Joseph wears fine white linen robes and a gold chain. Pharaoh sits on an elaborate throne looking amazed. Joseph gestures as he interprets a dream - seven fat cows and seven thin cows visible in a thought bubble above.",
            "middle": "Slavery. False accusations. Prison. Years of waiting in the dark. Joseph could have been bitter and angry. Instead, he kept trusting God, using his gift of interpreting dreams to help others. In prison, he interpreted dreams for Pharaoh's servants. Then one day, Pharaoh himself had a dream no one could explain.",
            "brave_moment": "Joseph stood before the most powerful man on earth and boldly said: 'It is not in me; God will give Pharaoh an answer.' He interpreted the dream - seven years of plenty followed by seven years of famine - and Pharaoh made him second-in-command of all Egypt!",
            "resolution": "Years later, Joseph's brothers came begging for food - and bowed before him, just as the dreams foretold! Joseph forgave them with tears of joy, saying: 'You meant it for evil, but God meant it for good!'",
            "moral": "Hard times are not the end of your story! God can use every difficulty to prepare you for something greater. Keep trusting through the waiting!",
            "verse": "You meant evil against me, but God meant it for good. - Genesis 50:20 (WEB)",
            "prayer": "Dear God, when life feels unfair, help me trust like Joseph that You're preparing something good. Help me forgive those who hurt me. Amen.",
            "activity": "Write about a hard time in your life. Now write how God might use that experience to help others someday."
        },

        {
            "title": "MOSES PARTS THE SEA",
            "subtitle": "Freedom from Slavery",
            "illustration_a": "Moses, an 80-year-old man with long white beard and flowing brown robes, standing on the shore of the Red Sea with his staff raised high. Behind him, two million Israelite men, women, and children look terrified. In the far distance behind them, dust clouds rise from Pharaoh's approaching army with golden chariots. The sea before them is deep blue and impassable.",
            "opening": "Trapped! The Red Sea ahead, Pharaoh's army behind. Two million people with nowhere to run. Children cried, parents panicked. It seemed like the end. But Moses raised his staff and said the words that changed everything: 'Stand still and see the salvation of the LORD!'",
            "illustration_b": "The Red Sea split in two with massive walls of blue-green water towering on both sides like glass cliffs. Fish and sea creatures visible in the transparent walls. A wide dry path stretches between the water walls. Millions of Israelites walk through with amazed faces, carrying children and belongings. Pillar of fire glows behind them blocking Egypt's army.",
            "middle": "Moses stretched his staff over the sea. A mighty east wind blew all night long. Slowly, incredibly, the waters pulled apart! Two enormous walls of water stood up on each side with dry ground between them. The people walked through on dry land with fish swimming in the walls of water beside them!",
            "brave_moment": "As Pharaoh's army charged between the water walls, God told Moses to stretch out his staff again. The walls of water crashed together! The entire Egyptian army was swept away. Israel was finally, completely FREE!",
            "resolution": "On the other shore, Moses and all Israel sang a song of praise. Miriam danced with a tambourine. They had witnessed the greatest rescue in history. God had set His people free!",
            "moral": "When you feel trapped with no way out, God can make a way where there seems to be no way! Trust Him to open doors you can't even see yet.",
            "verse": "The LORD will fight for you, and you shall be still. - Exodus 14:14 (WEB)",
            "prayer": "Dear God, when I feel trapped or stuck, remind me that You can split seas for me. Help me trust and be still while You work. Amen.",
            "activity": "Draw your own 'Red Sea moment' - a situation where you need God to make a way. Write a prayer asking Him to part the waters for you!"
        },
        {
            "title": "PETER WALKS ON WATER",
            "subtitle": "Keeping Eyes on Jesus",
            "illustration_a": "A small wooden fishing boat tossed on dark, stormy waves at night. Twelve terrified disciples grip the sides. Lightning flashes in the sky. Rain pours down. In the distance, a glowing figure walks calmly on top of the churning waves - Jesus in white robes, his feet resting gently on the water surface. Moonlight breaks through clouds around Him.",
            "opening": "The storm was terrifying. Waves crashed over the boat. The disciples rowed desperately through the night. Then they saw something that made them scream - a figure walking toward them ON the water! 'It's a ghost!' they cried. But Jesus called out: 'Don't be afraid. It is I!'",
            "illustration_b": "Peter stepping out of the rocking boat onto dark turbulent water, one foot on the boat's edge, one foot on the wave's surface. His face shows a mix of excitement and fear. Jesus stands a few yards away on the water, hand extended toward Peter, smiling encouragingly. Waves splash around them. Other disciples watch in disbelief from the boat.",
            "middle": "Peter, always the boldest, shouted: 'Lord, if it's really You, tell me to come to You on the water!' Jesus said one word: 'Come.' Peter swung his leg over the side of the boat and stepped onto the waves. He was WALKING ON WATER! Step after impossible step!",
            "brave_moment": "For several glorious seconds, Peter defied every law of nature - walking on water toward Jesus! But then he noticed the wind and waves. Fear gripped him and he began to sink. 'Lord, save me!' he cried. Instantly, Jesus grabbed his hand and pulled him up.",
            "resolution": "Jesus gently asked: 'Why did you doubt?' Back in the boat, the storm immediately stopped. Every disciple fell to their knees and worshiped. Peter learned the greatest lesson: keep your eyes on Jesus, not the storm!",
            "moral": "You can do impossible things when you keep your eyes on Jesus! Don't look at the storms around you - look at the One who controls the storms!",
            "verse": "He said, 'Come!' Peter stepped down from the boat and walked on the waters to come to Jesus. - Matthew 14:29 (WEB)",
            "prayer": "Dear Jesus, help me step out in faith even when things are scary. When I start to sink, grab my hand and pull me up. Amen.",
            "activity": "What 'impossible' thing is Jesus asking you to step out and try? Write it down and take one brave step toward it this week!"
        }
    ]


    # ============ RENDER STORIES ============
    gray_values = [0.88, 0.92, 0.95, 0.97, 0.90, 0.93, 0.88, 0.95, 0.92, 0.97]
    
    for idx, story in enumerate(stories):
        bg_gray = gray_values[idx % len(gray_values)]
        
        # PAGE A: Title + Illustration + Opening
        pdf.new_page()
        pdf.add_filled_rect(0, 700, 612, 92, gray=bg_gray)
        pdf.add_filled_rect(40, 705, 532, 75, gray=0.97)
        draw_decorative_border(pdf, 40, 705, 532, 75, gray=0.3)
        pdf.add_centered_text(755, f"Story {idx+1}", font='F4', size=10, gray=0.5)
        pdf.add_centered_text(735, story["title"], font='F2', size=20, gray=0.1)
        pdf.add_centered_text(712, story["subtitle"], font='F5', size=13, gray=0.3)
        
        draw_illustration_box(pdf, 500, story["illustration_a"], 170)
        
        pdf.add_filled_rect(50, 380, 512, 100, gray=0.95)
        pdf.add_rect(50, 380, 512, 100, line_width=0.5, gray=0.6)
        wrap_text(pdf, 65, 465, story["opening"], font='F4', size=12, max_width=68)
        
        # Decorative accent bar
        pdf.add_filled_rect(50, 360, 512, 8, gray=0.4)
        
        # PAGE B: Middle + Illustration + Brave Moment
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.98)
        pdf.add_filled_rect(40, 650, 532, 5, gray=bg_gray)
        
        pdf.add_text(60, 750, story["title"], font='F2', size=14, gray=0.2)
        pdf.add_line(60, 742, 300, 742, width=1, gray=0.4)
        
        y = wrap_text(pdf, 60, 720, story["middle"], font='F4', size=11, max_width=72)
        
        draw_illustration_box(pdf, y - 170, story["illustration_b"], 150)
        
        # The Brave Moment box
        brave_y = y - 200
        pdf.add_filled_rect(50, brave_y, 512, 55, gray=0.88)
        pdf.add_rect(50, brave_y, 512, 55, line_width=1.5, gray=0.3)
        pdf.add_text(60, brave_y+38, "THE BRAVE MOMENT:", font='F2', size=11, gray=0.1)
        wrap_text(pdf, 60, brave_y+22, story["brave_moment"], font='F5', size=10, max_width=72)
        
        # PAGE C: Resolution + Moral + Verse + Writing lines
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        
        pdf.add_text(60, 750, story["title"] + " (continued)", font='F2', size=12, gray=0.2)
        pdf.add_line(60, 742, 350, 742, width=0.5, gray=0.4)
        
        y = wrap_text(pdf, 60, 720, story["resolution"], font='F4', size=11, max_width=72)
        
        # Moral box
        y -= 20
        pdf.add_filled_rect(50, y-60, 512, 75, gray=bg_gray)
        draw_decorative_border(pdf, 50, y-60, 512, 75, gray=0.3)
        pdf.add_text(65, y, "LIFE LESSON:", font='F2', size=12, gray=0.1)
        wrap_text(pdf, 65, y-18, story["moral"], font='F5', size=11, max_width=68)
        
        # Verse box
        y -= 100
        pdf.add_filled_rect(50, y-45, 512, 55, gray=0.92)
        pdf.add_text(65, y, "KEY VERSE:", font='F2', size=10, gray=0.2)
        wrap_text(pdf, 65, y-15, story["verse"], font='F3', size=9, max_width=75)
        
        # What I Learned section
        y -= 80
        pdf.add_text(60, y, "WHAT I LEARNED:", font='F2', size=12, gray=0.1)
        for i in range(4):
            line_y = y - 25 - (i * 25)
            pdf.add_line(60, line_y, 550, line_y, width=0.5, gray=0.6)


        # HALF PAGE D: Prayer + Activity + Draw prompt
        pdf.new_page()
        pdf.add_filled_rect(0, 400, 612, 392, gray=0.95)
        
        # Prayer section
        pdf.add_filled_rect(50, 680, 512, 30, gray=0.88)
        pdf.add_text(60, 688, "MY PRAYER:", font='F2', size=13, gray=0.1)
        wrap_text(pdf, 60, 660, story["prayer"], font='F5', size=11, max_width=70)
        
        # Activity section
        pdf.add_line(50, 600, 562, 600, width=1, gray=0.4)
        pdf.add_filled_rect(50, 540, 512, 50, gray=0.92)
        pdf.add_text(60, 575, "HOW CAN I BE BRAVE TODAY?", font='F2', size=12, gray=0.1)
        wrap_text(pdf, 60, 555, story["activity"], font='F4', size=11, max_width=70)
        
        # Writing lines for activity response
        for i in range(3):
            line_y = 500 - (i * 25)
            pdf.add_line(60, line_y, 550, line_y, width=0.5, gray=0.6)
        
        # Color/Draw prompt in bottom half
        pdf.add_filled_rect(50, 200, 512, 180, gray=0.97)
        pdf.add_rect(50, 200, 512, 180, line_width=1.5, gray=0.4)
        pdf.add_text(60, 365, "DRAW OR COLOR:", font='F2', size=12, gray=0.2)
        pdf.add_text(60, 345, f"Draw your favorite scene from the story of {story['title']}!", font='F4', size=11, gray=0.3)
        pdf.add_text(250, 220, "[Your artwork here]", font='F3', size=10, gray=0.5)

    # ============ MY COURAGE JOURNAL (5 pages) ============
    journal_prompts = [
        "Write about a time you were brave. What happened? How did you feel?",
        "Who is someone brave you admire? What makes them courageous?",
        "What is something that scares you? How can God help you face it?",
        "Describe a time you stood up for someone else. What gave you strength?",
        "What brave thing do you want to do this year? What's your first step?"
    ]
    
    for i, prompt in enumerate(journal_prompts):
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_filled_rect(40, 720, 532, 50, gray=0.88)
        draw_decorative_border(pdf, 40, 720, 532, 50, gray=0.3)
        pdf.add_centered_text(748, "MY COURAGE JOURNAL", font='F2', size=16, gray=0.1)
        pdf.add_centered_text(728, f"Entry {i+1}", font='F4', size=11, gray=0.4)
        
        pdf.add_filled_rect(50, 665, 512, 40, gray=0.92)
        wrap_text(pdf, 60, 692, prompt, font='F5', size=12, max_width=70)
        
        # Writing lines
        for j in range(18):
            line_y = 640 - (j * 30)
            pdf.add_line(60, line_y, 550, line_y, width=0.5, gray=0.7)

    # ============ HEROES QUIZ ============
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    pdf.add_filled_rect(40, 710, 532, 60, gray=0.88)
    draw_decorative_border(pdf, 40, 710, 532, 60, gray=0.3)
    pdf.add_centered_text(745, "HEROES OF COURAGE QUIZ!", font='F2', size=18, gray=0.1)
    pdf.add_centered_text(720, "Test Your Knowledge - 10 Questions", font='F4', size=12, gray=0.3)
    
    questions = [
        "1. What weapon did David use against Goliath?",
        "2. What did Esther risk by going to the king?",
        "3. How many times a day did Daniel pray?",
        "4. How many friends were thrown in the furnace?",
        "5. How many days did Israel march around Jericho?",
        "6. How many soldiers did Gideon have?",
        "7. Where did Ruth follow Naomi to?",
        "8. Where was Joseph before becoming ruler?",
        "9. What did Moses part with his staff?",
        "10. What happened when Peter looked at the waves?"
    ]
    y = 680
    for q in questions:
        pdf.add_text(60, y, q, font='F4', size=11, gray=0.2)
        pdf.add_line(60, y-15, 400, y-15, width=0.5, gray=0.6)
        y -= 45


    # ============ CERTIFICATE OF COURAGE ============
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    draw_decorative_border(pdf, 40, 40, 532, 712, gray=0.2)
    draw_decorative_border(pdf, 50, 50, 512, 692, gray=0.4)
    pdf.add_filled_rect(80, 600, 452, 100, gray=0.88)
    pdf.add_centered_text(680, "CERTIFICATE OF COURAGE", font='F2', size=24, gray=0.1)
    pdf.add_centered_text(640, "This certifies that", font='F4', size=14, gray=0.3)
    pdf.add_line(180, 600, 432, 600, width=1, gray=0.3)
    pdf.add_centered_text(580, "(write your name)", font='F4', size=10, gray=0.5)
    pdf.add_centered_text(540, "has completed all 10 stories in", font='F4', size=13, gray=0.3)
    pdf.add_centered_text(510, "HEROES OF COURAGE", font='F2', size=18, gray=0.1)
    pdf.add_centered_text(470, "and is now equipped with the knowledge that", font='F4', size=12, gray=0.3)
    pdf.add_centered_text(440, "GOD GIVES COURAGE TO THOSE WHO TRUST HIM!", font='F2', size=13, gray=0.2)
    pdf.add_centered_text(380, "Be strong and courageous! Do not be afraid or", font='F5', size=12, gray=0.3)
    pdf.add_centered_text(360, "discouraged, for the LORD your God is with you", font='F5', size=12, gray=0.3)
    pdf.add_centered_text(340, "wherever you go. - Joshua 1:9", font='F5', size=12, gray=0.3)
    pdf.add_line(150, 250, 300, 250, width=0.5, gray=0.4)
    pdf.add_text(180, 235, "Date", font='F4', size=10, gray=0.5)
    pdf.add_line(350, 250, 500, 250, width=0.5, gray=0.4)
    pdf.add_text(380, 235, "Signature", font='F4', size=10, gray=0.5)

    # Save
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book276_Bible_Heroes_Courage.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
