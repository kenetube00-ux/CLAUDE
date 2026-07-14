#!/usr/bin/env python3
"""Book 277 - Amazing Miracles: 10 Incredible Things God Did in the Bible"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    def draw_decorative_border(pdf, x, y, w, h, gray=0.3):
        pdf.add_rect(x, y, w, h, line_width=2, gray=gray)
        pdf.add_rect(x+3, y+3, w-6, h-6, line_width=0.5, gray=gray)

    def draw_illustration_box(pdf, y, description, height=110):
        pdf.add_filled_rect(60, y, 492, height, gray=0.95)
        pdf.add_rect(60, y, 492, height, line_width=1.5, gray=0.4)
        pdf.add_text(70, y+height-18, "[ILLUSTRATION:", font='F2', size=10, gray=0.3)
        words = description.split()
        line = ""
        line_y = y + height - 33
        for word in words:
            if len(line + " " + word) > 75:
                pdf.add_text(70, line_y, line.strip(), font='F3', size=9, gray=0.4)
                line_y -= 13
                line = word
            else:
                line = line + " " + word if line else word
        if line:
            pdf.add_text(70, line_y, line.strip(), font='F3', size=9, gray=0.4)
        pdf.add_text(70, line_y-13, "]", font='F2', size=10, gray=0.3)

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


    # TITLE PAGE
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    draw_decorative_border(pdf, 30, 30, 552, 732, gray=0.2)
    pdf.add_filled_rect(50, 600, 512, 130, gray=0.88)
    pdf.add_centered_text(700, "AMAZING MIRACLES", font='F2', size=28, gray=0.1)
    pdf.add_centered_text(665, "10 Incredible Things God Did in the Bible", font='F5', size=16, gray=0.2)
    draw_illustration_box(pdf, 380, "A stunning collage: Red Sea parting with walls of water, fire falling from heaven, Jesus walking on glowing water, a giant fish in the ocean, manna falling like snow from golden clouds - all connected by rays of divine light", 160)
    pdf.add_centered_text(340, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(310, "With Science Connections, Activities & Prayers", font='F4', size=12, gray=0.4)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)

    # COPYRIGHT PAGE
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "AMAZING MIRACLES", font='F2', size=16, gray=0.1)
    pdf.add_text(72, 675, "10 Incredible Things God Did in the Bible", font='F4', size=12, gray=0.3)
    pdf.add_line(72, 665, 400, 665, width=0.5, gray=0.5)
    pdf.add_text(72, 640, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 620, "Scripture quotations from the World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 590, "Written for children ages 5-15", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 60, gray=0.92)
    pdf.add_text(72, 135, "Dedicated to every child who wonders about God's power -", font='F5', size=11, gray=0.2)
    pdf.add_text(72, 115, "His miracles are real and He still works today!", font='F5', size=11, gray=0.2)

    # MIRACLE DATA
    miracles = [
        {
            "title": "CREATION",
            "subtitle": "God Makes Everything from Nothing (Genesis 1)",
            "illustration": "An explosion of colorful light bursting from darkness - stars spiraling outward, planets forming in brilliant colors, Earth emerging blue and green with swirling white clouds. Golden divine light radiates from center. Galaxies spin in purples and blues.",
            "story": "In the very beginning, there was nothing. No light, no sound, no stars, no animals - absolutely nothing but God. Then God spoke, and His words had more power than anything we can imagine. 'Let there be light!' He said, and BOOM - light exploded across the emptiness! Over six incredible days, God created everything: the sky, oceans, mountains, flowers, fish, birds, animals, and finally - people! He made it all from nothing, just by speaking. Every star you see at night, every puppy that licks your face, every sunset that paints the sky - God made them all!",
            "wow_factor": "Scientists estimate there are 200 billion trillion stars in the universe. That's 200,000,000,000,000,000,000,000 stars! And God made every single one just by speaking!",
            "verse": "In the beginning, God created the heavens and the earth. - Genesis 1:1 (WEB)",
            "prayer": "Dear God, thank You for making this amazing world! Help me see Your miracles in nature every day. Amen.",
            "activity": "Go outside and list 10 things God created that amaze you. Which one is your favorite miracle of creation?"
        },
        {
            "title": "NOAH'S FLOOD",
            "subtitle": "God Saves a Family and All Animals (Genesis 6-9)",
            "illustration": "A massive wooden ark floating on endless dark floodwaters under stormy skies. Through open windows, pairs of colorful animals peek out - giraffes stretching necks, parrots on the edge, elephants' trunks visible. A rainbow begins to break through dark clouds. Rain still falls but sunlight pierces through.",
            "story": "The world had become so wicked that God decided to start over. But one man - Noah - still loved God. So God gave Noah an incredible task: build a boat big enough for his family AND two of every animal on Earth! People laughed at Noah for years as he built. But when the rain came, it didn't stop for 40 days and nights. Water covered everything - even the tallest mountains! But inside the ark, Noah's family and all those animals were safe and dry. After months floating, a dove brought back an olive leaf - land was appearing! God painted the first rainbow as a promise: never again.",
            "wow_factor": "The ark was about 450 feet long - that's longer than a football field! Scientists estimate it could hold over 125,000 sheep-sized animals!",
            "verse": "I will set my rainbow in the cloud, and it will be a sign of a covenant between me and the earth. - Genesis 9:13 (WEB)",
            "prayer": "Dear God, thank You for always keeping Your promises. When I see a rainbow, remind me of Your faithfulness. Amen.",
            "activity": "How many animals can you name in 2 minutes? Imagine fitting them ALL on one boat! Draw your favorite ark animal."
        },

        {
            "title": "PARTING THE RED SEA",
            "subtitle": "A Path Through the Water (Exodus 14)",
            "illustration": "Two towering walls of blue-green water rising 50 feet high on each side. A wide dry sandy path runs between them. Millions of Israelites walk through carrying children and bundles. Fish and sea creatures are frozen in the transparent water walls. A pillar of fire glows behind them. Moses stands at the front with staff raised.",
            "story": "Two million Israelites were trapped! The Red Sea in front, Pharaoh's army behind with thundering chariots. Children cried. Adults panicked. There was no escape! But Moses raised his staff and God sent a powerful east wind that blew ALL NIGHT. Slowly, impossibly, the sea split in two! Walls of water rose up like glass skyscrapers on each side. The ground between was completely dry - not even muddy! The people walked through on dry ground. When Pharaoh's army followed, God released the water walls, and the entire army was swept away!",
            "wow_factor": "The Red Sea is about 7,000 feet deep in some places! Scientists estimate that splitting it would require holding back billions of gallons of water - only God's power could do that!",
            "verse": "The children of Israel went into the middle of the sea on dry ground; and the waters were a wall to them on their right hand and on their left. - Exodus 14:22 (WEB)",
            "prayer": "Dear God, when I feel trapped, remind me that You can make a way through anything! Nothing is impossible for You. Amen.",
            "activity": "Fill a bowl with water. Try to push the water to one side. Impossible, right? That's why only God could part a whole sea!"
        },
        {
            "title": "MANNA FROM HEAVEN",
            "subtitle": "God Feeds His People Daily (Exodus 16)",
            "illustration": "Early morning in a desert camp with tents. Small white flaky substance covers the ground like frost or snow, glistening in golden sunrise light. Children kneel picking it up with wonder on their faces. Parents hold baskets collecting it. The sky above is pale gold and pink with tiny white flakes still floating down.",
            "story": "Two million people in a desert with no grocery stores, no farms, no food! The Israelites were hungry and worried. But God had an incredible plan. Every morning, when they woke up, the ground was covered with something amazing - small white flakes that tasted like honey wafers! They called it 'manna' which means 'What is it?' God sent this miracle food every single morning for FORTY YEARS! On the sixth day, He sent double so they could rest on the seventh. If anyone tried to hoard extra, it spoiled overnight. God wanted them to trust Him fresh each day.",
            "wow_factor": "God fed about 2 million people every day for 40 years. That's over 29 BILLION meals! Scientists have never been able to explain what manna actually was.",
            "verse": "I will rain bread from heaven for you. - Exodus 16:4 (WEB)",
            "prayer": "Dear God, help me trust You for what I need today without worrying about tomorrow. You always provide! Amen.",
            "activity": "For one week, write down one thing God provided for you each day. You'll be amazed at how much He gives!"
        },
        {
            "title": "WALLS OF JERICHO",
            "subtitle": "Shout and They Fall! (Joshua 6)",
            "illustration": "Massive stone walls crumbling and falling outward in an explosion of dust and debris. Huge blocks of stone tumble through the air. Israelite soldiers with trumpets raised stand below, mouths open in mighty shouts. Seven priests blow rams horn trumpets. Golden dust clouds rise. The city behind the walls is exposed.",
            "story": "Jericho's walls were legendary - 25 feet thick and incredibly tall! No army could break through them. But God's battle plan was unlike anything ever heard. March around the city once a day for six days. Don't talk, don't shout, just march in silence. On day seven, march seven times, then blow trumpets and SHOUT! It sounded crazy! But Joshua and the people obeyed God perfectly. On the seventh day, after the seventh lap, trumpets blasted and the people released the mightiest shout in history. Those massive, impossible, impenetrable walls CRUMBLED to the ground!",
            "wow_factor": "Archaeologists have actually found the ruins of Jericho's walls - and they fell OUTWARD (not inward like a typical siege)! This matches the Bible's account perfectly!",
            "verse": "By faith the walls of Jericho fell down after they had been marched around for seven days. - Hebrews 11:30 (WEB)",
            "prayer": "Dear God, help me obey You even when Your plans seem strange. I trust that You know what You're doing! Amen.",
            "activity": "Build a wall with blocks or books. Now try to knock it down by just shouting! Only God's power could do that with REAL walls!"
        },

        {
            "title": "ELIJAH AND FIRE",
            "subtitle": "God Answers with Fire from Heaven (1 Kings 18)",
            "illustration": "A stone altar drenched in water on top of Mount Carmel. Brilliant orange-white fire falls from heaven like a lightning bolt striking the altar. The fire is so intense it vaporizes the water and stones. Prophet Elijah stands with arms raised, face toward sky. 450 prophets of Baal cower in fear. The crowd falls on their faces in awe.",
            "story": "It was the ultimate showdown - God vs. the fake god Baal! 450 prophets of Baal built an altar and danced and shouted all day trying to get their god to send fire. Nothing happened! Elijah even teased them: 'Maybe your god is sleeping!' Then Elijah built his altar and made it HARDER - he soaked everything with water three times! Twelve jars of water drenched the altar until water filled the trench around it. Then Elijah prayed one simple prayer. WHOOOOSH! Fire fell from heaven so powerful it burned up the sacrifice, the stones, the soil, and ALL the water!",
            "wow_factor": "Water doesn't burn - it puts fires out! The fact that God's fire consumed soaking wet stones shows supernatural power beyond anything in nature!",
            "verse": "Then the fire of the LORD fell and consumed the burnt offering, the wood, the stones, and the dust, and licked up the water that was in the trench. - 1 Kings 18:38 (WEB)",
            "prayer": "Dear God, You are the one true God! Your power is real and amazing. Help me trust only in You. Amen.",
            "activity": "Pour water on a piece of paper. Could you light it on fire? Nope! That's what makes God's miracle so incredible!"
        },
        {
            "title": "JONAH AND THE WHALE",
            "subtitle": "3 Days Inside a Fish! (Jonah 1-2)",
            "illustration": "A massive whale or great fish swimming in deep dark blue ocean. Through its translucent belly, the silhouette of Jonah is visible praying on his knees. Seaweed wraps around the fish. Shafts of light penetrate from the ocean surface far above. Smaller fish swim nearby. Bubbles rise from the great fish.",
            "story": "God told Jonah to go to Nineveh, but Jonah ran the other way! He jumped on a ship sailing to Tarshish. But you can't run from God! A terrible storm arose. Jonah confessed it was his fault and told the sailors to throw him overboard. SPLASH! But instead of drowning, God sent an enormous fish that SWALLOWED Jonah whole! For three days and three nights, Jonah sat inside that fish - praying and repenting. Then God commanded the fish, and it vomited Jonah onto dry land! This time, Jonah obeyed and went to Nineveh.",
            "wow_factor": "Some whale species have throats large enough to swallow a person! In 1891, a sailor named James Bartley reportedly survived being inside a whale for hours - though Jonah's 3 days was definitely supernatural!",
            "verse": "The LORD prepared a great fish to swallow up Jonah; and Jonah was in the belly of the fish three days and three nights. - Jonah 1:17 (WEB)",
            "prayer": "Dear God, help me obey You the FIRST time. I don't want to run away from Your plans for me. Amen.",
            "activity": "Have you ever tried to avoid something God wanted you to do? Write about it. What happened? Did you eventually obey?"
        },
        {
            "title": "JESUS WALKS ON WATER",
            "subtitle": "Defying Gravity (Matthew 14)",
            "illustration": "Jesus in flowing white robes walking calmly on dark stormy sea waves at night. His feet rest lightly on the water surface creating gentle ripples. Wind blows his robes and hair. A small boat with terrified disciples tosses in the background. Moonlight breaks through storm clouds illuminating Jesus in an ethereal glow.",
            "story": "The disciples were alone on the Sea of Galilee in the middle of the night. A violent storm battered their little boat. Waves crashed over the sides. Then, through the rain and darkness, they saw a figure walking toward them - ON THE WATER! They screamed, thinking it was a ghost! But Jesus called out: 'Don't be afraid! It's me!' Peter shouted back: 'If it's really You, let me come to You!' Jesus said 'Come!' and Peter actually stepped out and WALKED ON WATER toward Jesus! He only sank when he looked at the waves instead of Jesus.",
            "wow_factor": "Water cannot support human weight - we are too dense! A person would need to run at 67 mph to 'skip' across water like some lizards do. Jesus simply walked calmly - defying the laws of physics!",
            "verse": "But when he saw that the wind was strong, he was afraid, and beginning to sink, he cried out, 'Lord, save me!' - Matthew 14:30 (WEB)",
            "prayer": "Dear Jesus, help me keep my eyes on You instead of my problems. When I start to sink, catch me! Amen.",
            "activity": "Fill a bowl with water and try to make a coin float. It sinks! That's why walking on water is impossible without God's power!"
        },

        {
            "title": "FEEDING 5,000",
            "subtitle": "5 Loaves and 2 Fish Feed Thousands (John 6)",
            "illustration": "Jesus standing on a green hillside holding up a small wicker basket with 5 round loaves of bread and 2 small fish. His hands glow with divine light. Around Him, 5000+ men plus women and children sit on green grass in groups, all eating happily. Twelve baskets overflow with leftover bread in the foreground. Blue lake and mountains in background.",
            "story": "Five thousand men (plus women and children - maybe 15,000 total!) were hungry after listening to Jesus teach all day. The disciples panicked: 'Send them away!' But a small boy offered his lunch - just 5 little bread rolls and 2 dried fish. Jesus took that tiny lunch, looked up to heaven, said thank you to God, and started breaking the bread. And breaking. And breaking! The bread and fish just kept multiplying in His hands! Everyone ate until they were STUFFED. And there were TWELVE baskets of leftovers!",
            "wow_factor": "To feed 15,000 people, you'd need about 4,500 pounds of bread - that's more than 2 tons! Jesus created all that from a boy's small lunch!",
            "verse": "He took the five loaves and the two fish, and looking up to heaven, he blessed and broke the loaves. - Mark 6:41 (WEB)",
            "prayer": "Dear God, thank You that even when I only have a little to offer, You can multiply it into something amazing! Amen.",
            "activity": "Take 5 crackers and 2 goldfish crackers. Now imagine them feeding your whole school! That's how powerful Jesus is!"
        },
        {
            "title": "JESUS RISES FROM THE DEAD",
            "subtitle": "The Greatest Miracle Ever (Matthew 28)",
            "illustration": "An empty stone tomb with the massive round stone rolled away to the side. Brilliant golden-white light pours from inside the tomb. Burial cloths lie neatly folded inside. An angel in blazing white sits on the stone. Roman guards lie on the ground in shock. Mary and other women approach with spices, faces showing shock turning to joy. Easter morning sunrise in pink and gold.",
            "story": "Jesus had been crucified and buried in a sealed tomb guarded by Roman soldiers. For three dark days, His followers wept, thinking all hope was lost. But on Sunday morning, the earth shook! An angel descended like lightning and rolled away the massive stone! The tough Roman guards fainted in terror! When the women came with burial spices, the angel said the most amazing words in history: 'He is not here! He is RISEN!' Jesus was ALIVE! Death itself could not hold Him! He appeared to over 500 people over 40 days - eating, talking, showing His wounds. The greatest miracle ever: Jesus conquered death!",
            "wow_factor": "No one in recorded history has ever come back to life on their own after being dead for 3 days. Over 500 eyewitnesses saw the risen Jesus. Many died rather than deny what they saw - proving they truly believed!",
            "verse": "He is not here, for he has risen, just like he said. - Matthew 28:6 (WEB)",
            "prayer": "Dear Jesus, thank You for conquering death so I can live forever with You! You are truly alive! Amen.",
            "activity": "The resurrection changes EVERYTHING! Write 3 reasons why it matters that Jesus is alive today."
        }
    ]


    # RENDER MIRACLES
    gray_bgs = [0.88, 0.92, 0.95, 0.90, 0.93, 0.88, 0.97, 0.91, 0.94, 0.89]
    
    for idx, miracle in enumerate(miracles):
        bg = gray_bgs[idx % len(gray_bgs)]
        
        # Page 1: Title + Illustration + Story beginning
        pdf.new_page()
        pdf.add_filled_rect(0, 720, 612, 72, gray=bg)
        pdf.add_filled_rect(45, 725, 522, 60, gray=0.97)
        draw_decorative_border(pdf, 45, 725, 522, 60, gray=0.3)
        pdf.add_centered_text(762, f"Miracle {idx+1}", font='F4', size=10, gray=0.5)
        pdf.add_centered_text(742, miracle["title"], font='F2', size=20, gray=0.1)
        pdf.add_centered_text(727, miracle["subtitle"], font='F4', size=11, gray=0.3)
        
        draw_illustration_box(pdf, 540, miracle["illustration"], 150)
        
        # Story text
        pdf.add_filled_rect(50, 330, 512, 190, gray=0.97)
        pdf.add_rect(50, 330, 512, 190, line_width=0.5, gray=0.6)
        wrap_text(pdf, 60, 505, miracle["story"], font='F4', size=11, max_width=72)
        
        # Accent divider
        pdf.add_filled_rect(50, 315, 512, 8, gray=0.4)
        
        # Page 2: WOW Factor + Verse + Prayer + Activity
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_text(60, 760, miracle["title"] + " (continued)", font='F2', size=13, gray=0.2)
        pdf.add_line(60, 752, 350, 752, width=0.5, gray=0.4)
        
        # WOW Factor box
        pdf.add_filled_rect(50, 640, 512, 90, gray=0.88)
        draw_decorative_border(pdf, 50, 640, 512, 90, gray=0.3)
        pdf.add_text(65, 715, "WOW FACTOR - Science Connection:", font='F2', size=12, gray=0.1)
        wrap_text(pdf, 65, 695, miracle["wow_factor"], font='F4', size=10, max_width=72)
        
        # Verse box
        pdf.add_filled_rect(50, 560, 512, 60, gray=0.92)
        pdf.add_text(65, 605, "KEY VERSE:", font='F2', size=11, gray=0.2)
        wrap_text(pdf, 65, 585, miracle["verse"], font='F3', size=9, max_width=75)
        
        # Prayer section
        pdf.add_filled_rect(50, 460, 512, 80, gray=0.95)
        pdf.add_text(65, 525, "MY PRAYER:", font='F2', size=12, gray=0.1)
        wrap_text(pdf, 65, 505, miracle["prayer"], font='F5', size=11, max_width=70)
        
        # Activity section
        pdf.add_filled_rect(50, 340, 512, 100, gray=bg)
        pdf.add_rect(50, 340, 512, 100, line_width=1, gray=0.4)
        pdf.add_text(65, 425, "MIRACLE ACTIVITY:", font='F2', size=12, gray=0.1)
        wrap_text(pdf, 65, 405, miracle["activity"], font='F4', size=11, max_width=70)
        
        # Writing lines
        for i in range(4):
            pdf.add_line(60, 300 - (i*25), 550, 300 - (i*25), width=0.5, gray=0.6)

    # FINAL PAGE - Miracle Tracker
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    pdf.add_filled_rect(40, 710, 532, 60, gray=0.88)
    draw_decorative_border(pdf, 40, 710, 532, 60, gray=0.3)
    pdf.add_centered_text(745, "MY MIRACLE TRACKER", font='F2', size=18, gray=0.1)
    pdf.add_centered_text(720, "Check off each miracle as you read and discuss it!", font='F4', size=11, gray=0.3)
    
    y = 680
    for idx, m in enumerate(miracles):
        pdf.add_filled_rect(50, y-5, 512, 25, gray=0.97 if idx%2==0 else 0.92)
        pdf.add_rect(60, y, 15, 15, line_width=1, gray=0.3)
        pdf.add_text(85, y+3, f"{idx+1}. {m['title']} - {m['subtitle']}", font='F4', size=10, gray=0.2)
        y -= 30

    pdf.add_centered_text(350, "You've discovered 10 AMAZING MIRACLES!", font='F2', size=14, gray=0.2)
    pdf.add_centered_text(320, "Remember: The same God who did these miracles", font='F5', size=12, gray=0.3)
    pdf.add_centered_text(300, "is still working miracles today!", font='F5', size=12, gray=0.3)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book277_Bible_Miracles_Kids.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
