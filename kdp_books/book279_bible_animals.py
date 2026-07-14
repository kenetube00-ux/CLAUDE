#!/usr/bin/env python3
"""Book 279 - Amazing Animals in the Bible: 10 Incredible Creature Stories"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    def draw_border(pdf, x, y, w, h, gray=0.3):
        pdf.add_rect(x, y, w, h, line_width=2, gray=gray)
        pdf.add_rect(x+3, y+3, w-6, h-6, line_width=0.5, gray=gray)

    def illus_box(pdf, y, desc, height=110):
        pdf.add_filled_rect(60, y, 492, height, gray=0.95)
        pdf.add_rect(60, y, 492, height, line_width=1.5, gray=0.4)
        pdf.add_text(70, y+height-18, "[ILLUSTRATION:", font='F2', size=10, gray=0.3)
        words = desc.split()
        line, ly = "", y+height-33
        for w in words:
            if len(line+" "+w)>75:
                pdf.add_text(70, ly, line.strip(), font='F3', size=9, gray=0.4)
                ly -= 13; line = w
            else: line = line+" "+w if line else w
        if line: pdf.add_text(70, ly, line.strip(), font='F3', size=9, gray=0.4)
        pdf.add_text(70, ly-13, "]", font='F2', size=10, gray=0.3)

    def wrap(pdf, x, y, text, font='F4', size=11, mw=70, gray=0):
        words = text.split()
        line, cy = "", y
        for w in words:
            if len(line+" "+w)>mw:
                pdf.add_text(x, cy, line.strip(), font=font, size=size, gray=gray)
                cy -= 15; line = w
            else: line = line+" "+w if line else w
        if line: pdf.add_text(x, cy, line.strip(), font=font, size=size, gray=gray); cy -= 15
        return cy


    # TITLE PAGE
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    draw_border(pdf, 30, 30, 552, 732, gray=0.2)
    pdf.add_filled_rect(50, 600, 512, 130, gray=0.88)
    pdf.add_centered_text(700, "AMAZING ANIMALS", font='F2', size=28, gray=0.1)
    pdf.add_centered_text(668, "IN THE BIBLE", font='F2', size=22, gray=0.15)
    pdf.add_centered_text(638, "10 Incredible Creature Stories", font='F5', size=16, gray=0.2)
    illus_box(pdf, 370, "A colorful collection of Bible animals: a majestic lion lying peacefully, a white dove with olive branch, a large whale breaching the ocean surface, a raven carrying bread, a loyal donkey, and sheep in green pastures. All arranged in a circular composition with golden light.", 170)
    pdf.add_centered_text(330, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(300, "Real Animal Facts + Bible Stories + Activities", font='F4', size=12, gray=0.4)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)

    # COPYRIGHT
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "AMAZING ANIMALS IN THE BIBLE", font='F2', size=16, gray=0.1)
    pdf.add_line(72, 688, 400, 688, width=0.5, gray=0.5)
    pdf.add_text(72, 665, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 645, "Scripture from World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 50, gray=0.92)
    pdf.add_text(72, 130, "For every kid who loves animals - God made them all amazing!", font='F5', size=11, gray=0.2)

    animals = [
        {
            "title": "THE SERPENT IN THE GARDEN",
            "ref": "Genesis 3",
            "theme": "About Choices",
            "illustration": "A beautiful green serpent coiled around the branch of a tree heavy with red fruit in the Garden of Eden. Lush tropical plants surround the tree - ferns, flowers in every color, butterflies. Eve stands nearby looking at the fruit curiously. The garden is incredibly beautiful with waterfalls and golden light.",
            "story": "In the perfect Garden of Eden, a crafty serpent whispered lies to Eve. 'Did God really say you can't eat from any tree?' it twisted God's words. Eve knew the rule but listened anyway. The serpent promised she'd become like God. Eve took the fruit, ate it, and gave some to Adam. In that moment, sin entered the world and everything changed forever.",
            "moral": "Be careful who you listen to! Not every voice that sounds friendly has good intentions. Always check what people say against what God says.",
            "fact": "Snakes don't actually have vocal cords! They communicate through hissing, body language, and vibrations. The serpent in Eden was likely possessed by Satan himself.",
            "verse": "The serpent said to the woman, 'You won't really die.' - Genesis 3:4 (WEB)",
            "activity": "Draw the most beautiful garden you can imagine. Now think: what 'serpents' (bad influences) try to get you to break rules?"
        },
        {
            "title": "NOAH'S ANIMALS",
            "ref": "Genesis 7",
            "theme": "God Cares for All Creatures",
            "illustration": "Pairs of animals walking in an orderly line up a wooden ramp into the massive ark. Two giraffes stretch their necks, two elephants lumber along, two colorful parrots fly overhead, two striped tigers walk proudly, two penguins waddle. Noah gestures welcomingly at the door. Raindrops begin to fall from darkening sky.",
            "story": "God didn't just save Noah's family - He saved EVERY kind of animal! Two of each (seven of some) marched onto the ark in perfect order. Lions walked beside lambs. Eagles didn't chase mice. God made them all peaceful together on that boat for over a year! He fed them, kept them calm, and protected every single one. After the flood, they all burst out onto fresh new land to fill the earth again.",
            "moral": "God cares about ALL His creatures, not just people! Every animal matters to Him. And when He asks us to do something hard, He also provides everything we need.",
            "fact": "Scientists estimate there are about 6.5 million land animal species on Earth today! The ark would have needed about 7,000 'kinds' of animals (not every variety, but original types).",
            "verse": "Of every living thing, you shall bring two of every sort into the ship to keep them alive. - Genesis 6:19 (WEB)",
            "activity": "List your 10 favorite animals. Thank God for making each one! Which would be hardest to have on a boat?"
        },

        {
            "title": "BALAAM'S TALKING DONKEY",
            "ref": "Numbers 22",
            "theme": "God Uses Unexpected Things",
            "illustration": "A gray donkey stopped on a narrow path between two stone walls, turning its head to look at its rider Balaam with an almost human expression of frustration. Balaam holds a stick raised in anger. An invisible angel with a flaming sword stands blocking the path - only visible in ethereal outline showing the donkey can see what the man cannot.",
            "story": "Balaam was riding his donkey to do something God didn't want. Three times the donkey stopped or turned because it could see an angel blocking the path! Balaam hit the donkey each time. Then God opened the donkey's mouth and it SPOKE: 'What have I done to you that you've hit me three times?' Balaam argued with his donkey! Finally God opened Balaam's eyes to see the angel, and he realized his donkey had saved his life!",
            "moral": "Sometimes God uses the most unexpected things to get our attention. Pay attention to the 'donkeys' in your life - the things that seem to be blocking you might actually be protecting you!",
            "fact": "Donkeys are incredibly intelligent! They have a memory span of 25+ years, can recognize other donkeys they've met, and refuse to do anything they consider unsafe - that's why they're called 'stubborn'!",
            "verse": "The LORD opened the mouth of the donkey, and she said to Balaam, 'What have I done to you?' - Numbers 22:28 (WEB)",
            "activity": "Think of a time when something 'went wrong' but actually protected you. Write about how God might have been redirecting you!"
        },
        {
            "title": "DAVID'S SHEEP",
            "ref": "Psalm 23",
            "theme": "God Is Our Shepherd",
            "illustration": "Young David as a teenager sitting on a green hillside playing a small harp, surrounded by fluffy white sheep grazing peacefully. Some sheep drink from a crystal-clear stream. Green pastures stretch toward gentle hills. A sunset paints the sky in pinks and golds. David's shepherd's staff leans against a rock beside him.",
            "story": "Before David was a king, he was a shepherd boy. He spent years caring for sheep - leading them to green grass, finding them clean water, protecting them from lions and bears! This experience inspired the most famous poem ever written: Psalm 23. 'The LORD is MY shepherd,' David wrote, realizing that God cared for him just like he cared for his sheep. God led him, fed him, protected him, and comforted him.",
            "moral": "You are God's precious sheep! Just like a good shepherd provides everything his sheep need, God provides everything YOU need. You don't need to worry!",
            "fact": "Sheep can recognize up to 50 other sheep faces AND 10 human faces for years! They also can't get up on their own if they fall on their backs - they need their shepherd to help them. Just like we need God!",
            "verse": "The LORD is my shepherd; I shall not want. He makes me lie down in green pastures. He leads me beside still waters. - Psalm 23:1-2 (WEB)",
            "activity": "Read all of Psalm 23. Draw a picture for each verse. How is God YOUR shepherd today?"
        },
        {
            "title": "ELIJAH'S RAVENS",
            "ref": "1 Kings 17",
            "theme": "God Provides Through Nature",
            "illustration": "Prophet Elijah sitting beside a rocky brook in a wilderness ravine. Two large black ravens fly toward him - one carrying bread in its beak, the other carrying meat. The brook has clear flowing water. Rocky desert canyon walls rise on both sides. Morning golden light filters through. Elijah looks up gratefully.",
            "story": "A terrible drought hit the land because of evil King Ahab. God told Elijah to hide by a brook, and promised: 'I have commanded the ravens to feed you there.' Every morning AND every evening, ravens flew in carrying bread and meat in their beaks! Ravens - birds known for stealing food - were now DELIVERING meals! God used unlikely delivery birds to keep His prophet alive during the drought.",
            "moral": "God has creative ways to provide for you! He's not limited to normal methods. Sometimes help comes from the most unexpected places - trust Him to provide!",
            "fact": "Ravens are among the smartest birds on Earth! They can solve complex puzzles, use tools, and even plan for the future. They normally HIDE food for themselves - bringing food to someone else is totally against their nature. Only God could make them do that!",
            "verse": "The ravens brought him bread and meat in the morning, and bread and meat in the evening; and he drank from the brook. - 1 Kings 17:6 (WEB)",
            "activity": "List 5 unexpected ways God has provided for your family. Sometimes His delivery methods surprise us!"
        },

        {
            "title": "DANIEL'S LIONS",
            "ref": "Daniel 6",
            "theme": "God Protects the Faithful",
            "illustration": "Daniel sitting calmly in a stone pit with seven large lions lying around him peacefully. One lion rests its head near Daniel's lap like a giant house cat. Another lion yawns showing huge teeth but making no threat. A glowing angel stands protectively behind Daniel. Moonlight streams from the pit opening above. Daniel's hands are folded in prayer.",
            "story": "Daniel was thrown into a den of hungry lions because he refused to stop praying to God. The king sealed the pit with a stone and spent a sleepless night worrying. But God sent an angel who shut the lions' mouths! The fierce predators became like gentle kittens around Daniel. In the morning, the king found Daniel perfectly safe - not a scratch on him! The lions hadn't even tried to hurt him.",
            "moral": "When you stay faithful to God, He protects you in ways that seem impossible. The 'lions' in your life - bullies, fears, problems - cannot hurt you when God is your defender!",
            "fact": "A lion's bite force is about 650 PSI - strong enough to crush bones! A male lion can eat 75 pounds of meat in one sitting. For these hungry lions to ignore Daniel, something truly supernatural had to happen!",
            "verse": "My God sent his angel, and shut the lions' mouths, and they have not hurt me. - Daniel 6:22 (WEB)",
            "activity": "Draw a lion looking fierce - then draw it looking gentle. What 'lions' (fears) in your life need God to shut their mouths?"
        },
        {
            "title": "JONAH'S GREAT FISH",
            "ref": "Jonah 1",
            "theme": "You Can't Run from God",
            "illustration": "A massive whale-like fish swimming in deep dark blue ocean waters. Inside its enormous belly (shown in cross-section), Jonah kneels in prayer surrounded by seaweed. The fish's eye is visible and wise-looking. Schools of smaller fish swim around the great fish. Light rays filter down from the distant surface. Bubbles rise from Jonah.",
            "story": "When Jonah ran from God's mission, God sent a storm. The sailors threw Jonah overboard and GULP - a massive fish swallowed him whole! For three terrifying days inside that fish, Jonah finally prayed and repented. The fish then vomited Jonah onto dry land - alive, seaweed-covered, and ready to obey! This time Jonah went straight to Nineveh as God commanded.",
            "moral": "You can't run from God! But here's the good news - even when you've messed up badly, God gives second chances. Running from God only makes things harder. Turn around and obey!",
            "fact": "Sperm whales have been found with giant squid in their stomachs, proving they can swallow very large things! Their stomach acid is strong but there are reports of people surviving briefly inside large marine animals. Jonah's 3-day survival was definitely a miracle!",
            "verse": "Jonah prayed to the LORD his God out of the fish's belly. - Jonah 2:1 (WEB)",
            "activity": "Have you ever tried to run from something God wanted you to do? Write about what happened. Did you eventually obey?"
        },
        {
            "title": "JESUS' DONKEY",
            "ref": "Matthew 21",
            "theme": "Humble Service Matters",
            "illustration": "Jesus riding a small humble donkey through the streets of Jerusalem. People throw colorful cloaks and green palm branches on the road before Him. Children wave palm branches and shout joyfully. The donkey walks proudly carrying the King of Kings. Stone buildings of Jerusalem line the street. Crowds fill every space cheering.",
            "story": "When Jesus entered Jerusalem as King, He didn't choose a mighty warhorse or a golden chariot. He chose a small, humble donkey! The animal had never been ridden before, yet it walked calmly carrying Jesus while thousands cheered. This humble donkey carried the King of the Universe! No one remembers the donkey's name, but it played the most important role that day.",
            "moral": "God uses humble servants! You don't have to be the biggest, strongest, or most famous. Just be willing to carry Jesus - to let Him use you - and you'll play an important role in His story!",
            "fact": "Donkeys have been working alongside humans for over 5,000 years! They can carry 20-30% of their body weight and walk 20+ miles per day. In Bible times, riding a donkey signified coming in peace (horses meant war).",
            "verse": "Behold, your King comes to you, humble, and riding on a donkey. - Matthew 21:5 (WEB)",
            "activity": "What 'small' job can you do for God this week? Remember - no job is too small if Jesus is the one you're serving!"
        },
        {
            "title": "PETER'S ROOSTER",
            "ref": "Matthew 26",
            "theme": "Honesty and Repentance",
            "illustration": "Peter standing in a courtyard at night by a fire, face showing shock and guilt as a rooster crows on a stone wall nearby. Tears stream down Peter's face. Firelight flickers on his features. In the background through an archway, Jesus is being led away by guards and turns to look at Peter with sad, loving eyes. Pre-dawn sky barely lightens the horizon.",
            "story": "Peter swore he'd NEVER deny Jesus - even if everyone else did! But that very night, when people asked if he knew Jesus, Peter denied it. Once. Twice. Three times: 'I DON'T KNOW HIM!' Immediately, a rooster crowed - just as Jesus predicted. Peter looked up and saw Jesus looking at him. Peter ran outside and cried the bitterest tears of his life.",
            "moral": "We all fail sometimes, even when we mean well. But failure isn't the end! Peter's story proves that tears of repentance lead to restoration. God uses broken people who are honest about their mistakes.",
            "fact": "Roosters crow at dawn as a territorial call, but they can crow at any time! In the first century, the 'rooster crow' was also a term for the Roman trumpet call at the third watch of the night (around 3 AM).",
            "verse": "Before the rooster crows, you will deny me three times. - Matthew 26:34 (WEB)",
            "activity": "Have you ever let fear cause you to deny or hide your faith? Write about it. Remember - God forgives and restores!"
        },
        {
            "title": "THE LAMB OF GOD",
            "ref": "John 1:29",
            "theme": "Jesus' Love for Us",
            "illustration": "A pure white lamb standing in a beam of golden heavenly light on a green hill. A gentle cross shadow falls behind it. The lamb looks directly at the viewer with kind, innocent eyes. Flowers bloom around its feet - lilies and roses. In the sky, clouds part to reveal brilliant golden rays. Everything is peaceful and sacred.",
            "story": "When John the Baptist saw Jesus coming toward him, he said something strange: 'Look! The Lamb of God who takes away the sin of the world!' In the Old Testament, people sacrificed lambs to cover their sins. But these lambs were temporary. Jesus came as the FINAL Lamb - perfect, pure, and willing to give His life so that we could be forgiven forever. He is the ultimate sacrifice of love.",
            "moral": "Jesus gave everything for YOU because He loves you that much! The Lamb of God took your punishment so you could be free. That's the greatest love story ever told!",
            "fact": "Lambs are symbols of innocence and gentleness. In Jesus' time, over 250,000 lambs were sacrificed at Passover in Jerusalem each year. Jesus fulfilled what all those lambs pointed to - one perfect sacrifice for all time!",
            "verse": "Behold, the Lamb of God, who takes away the sin of the world! - John 1:29 (WEB)",
            "activity": "Write a thank-you letter to Jesus for being your Lamb - for loving you enough to take your place. What does His love mean to you?"
        }
    ]


    # RENDER ANIMAL STORIES
    gray_vals = [0.88, 0.92, 0.95, 0.90, 0.93, 0.88, 0.97, 0.91, 0.94, 0.89]
    
    for idx, a in enumerate(animals):
        bg = gray_vals[idx % len(gray_vals)]
        
        # Page 1: Title + Illustration + Story
        pdf.new_page()
        pdf.add_filled_rect(0, 720, 612, 72, gray=bg)
        pdf.add_filled_rect(45, 725, 522, 60, gray=0.97)
        draw_border(pdf, 45, 725, 522, 60, gray=0.3)
        pdf.add_centered_text(762, f"Animal Story {idx+1} - {a['ref']}", font='F4', size=10, gray=0.5)
        pdf.add_centered_text(742, a["title"], font='F2', size=18, gray=0.1)
        pdf.add_centered_text(727, a["theme"], font='F5', size=11, gray=0.3)
        
        illus_box(pdf, 550, a["illustration"], 140)
        
        pdf.add_filled_rect(50, 350, 512, 180, gray=0.97)
        pdf.add_rect(50, 350, 512, 180, line_width=0.5, gray=0.5)
        pdf.add_text(60, 515, "THE BIBLE STORY:", font='F2', size=11, gray=0.2)
        wrap(pdf, 60, 495, a["story"], font='F4', size=11, mw=72)

        # Page 2: Moral + Facts + Verse + Activity
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_text(60, 760, a["title"] + " (continued)", font='F2', size=13, gray=0.2)
        pdf.add_line(60, 752, 400, 752, width=0.5, gray=0.4)
        
        # Moral box
        pdf.add_filled_rect(50, 650, 512, 80, gray=bg)
        draw_border(pdf, 50, 650, 512, 80, gray=0.4)
        pdf.add_text(65, 715, "MORAL / LIFE LESSON:", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 695, a["moral"], font='F5', size=11, mw=70)
        
        # Did You Know? box
        pdf.add_filled_rect(50, 530, 512, 100, gray=0.92)
        pdf.add_rect(50, 530, 512, 100, line_width=1, gray=0.3)
        pdf.add_text(65, 615, "DID YOU KNOW? (Animal Facts!):", font='F2', size=11, gray=0.1)
        wrap(pdf, 65, 595, a["fact"], font='F4', size=10, mw=72)
        
        # Verse
        pdf.add_filled_rect(50, 440, 512, 70, gray=0.95)
        pdf.add_text(65, 495, "KEY VERSE:", font='F2', size=11, gray=0.2)
        wrap(pdf, 65, 475, a["verse"], font='F3', size=9, mw=75)
        
        # Activity
        pdf.add_filled_rect(50, 320, 512, 100, gray=0.88)
        pdf.add_rect(50, 320, 512, 100, line_width=1, gray=0.4)
        pdf.add_text(65, 405, "ACTIVITY:", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 385, a["activity"], font='F4', size=11, mw=70)
        
        # Writing lines
        for i in range(3):
            pdf.add_line(60, 280-(i*25), 550, 280-(i*25), width=0.5, gray=0.6)

    # FINAL PAGE - Animal Match Game
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    pdf.add_filled_rect(40, 710, 532, 60, gray=0.88)
    draw_border(pdf, 40, 710, 532, 60, gray=0.3)
    pdf.add_centered_text(745, "BIBLE ANIMAL MATCHING GAME!", font='F2', size=16, gray=0.1)
    pdf.add_centered_text(718, "Draw a line from each animal to its Bible story!", font='F4', size=11, gray=0.3)
    
    left_items = ["Serpent", "Dove (Noah's)", "Donkey (Balaam's)", "Sheep (David's)", "Ravens (Elijah's)", "Lions (Daniel's)", "Great Fish (Jonah's)", "Donkey (Jesus')", "Rooster (Peter's)", "Lamb of God"]
    right_items = ["Carried the King", "Took away sin", "Warned of lies", "Provided food", "Showed peace", "Said 'What have I done?'", "Swallowed a prophet", "Announced a denial", "Lay down peacefully", "Showed God's care"]
    
    y = 670
    for i in range(10):
        pdf.add_text(70, y, f"{i+1}. {left_items[i]}", font='F4', size=10, gray=0.2)
        pdf.add_text(370, y, f"{chr(65+i)}. {right_items[i]}", font='F4', size=10, gray=0.2)
        y -= 30

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book279_Bible_Animals_Stories.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
