#!/usr/bin/env python3
"""Book 283 - In the Beginning God Created: The 7 Days of Creation Beautifully Told"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    def draw_border(pdf, x, y, w, h, gray=0.3):
        pdf.add_rect(x, y, w, h, line_width=2, gray=gray)
        pdf.add_rect(x+3, y+3, w-6, h-6, line_width=0.5, gray=gray)

    def illus_box(pdf, y, desc, height=130):
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
    pdf.add_filled_rect(50, 590, 512, 140, gray=0.88)
    pdf.add_centered_text(700, "IN THE BEGINNING", font='F2', size=26, gray=0.1)
    pdf.add_centered_text(668, "GOD CREATED", font='F2', size=26, gray=0.1)
    pdf.add_centered_text(635, "The 7 Days of Creation Beautifully Told", font='F5', size=15, gray=0.2)
    illus_box(pdf, 360, "A stunning panorama showing all seven days of creation in sequence: golden light bursting from darkness, blue sky and ocean separating, green mountains with flowers, brilliant sun and silver moon with stars, colorful fish and birds in flight, animals of every kind, and a peaceful garden with man and woman. Rainbow of colors across the scene.", 170)
    pdf.add_centered_text(320, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(290, "With Science Connections & Gratitude Prompts", font='F4', size=12, gray=0.4)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)

    # COPYRIGHT
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "IN THE BEGINNING GOD CREATED", font='F2', size=14, gray=0.1)
    pdf.add_line(72, 688, 400, 688, width=0.5, gray=0.5)
    pdf.add_text(72, 665, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 645, "Scripture from World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 50, gray=0.92)
    pdf.add_text(72, 130, "For every kid amazed by God's creation - it's all for YOU!", font='F5', size=11, gray=0.2)

    days = [
        {
            "day": "DAY 1", "title": "LIGHT & DARKNESS",
            "illustration": "An explosion of pure golden-white light bursting dramatically from absolute darkness. Rays spread outward in every direction like a cosmic sunrise. The light pushes back the deep void of darkness. Sparkles and energy radiate from the center. The contrast between brilliant light and deep darkness is stunning. Pure, raw creative power visualized.",
            "story_p1": "In the beginning, there was nothing but God. No stars, no planets, no light - just vast, empty darkness stretching in every direction forever. It was darker than the deepest cave, darker than closing your eyes at midnight. Nothing existed except God Himself.",
            "story_p2": "Then God spoke the first words ever spoken: 'LET THERE BE LIGHT!' And instantly - BOOM! - light exploded across the void! Beautiful, brilliant, golden light flooded the darkness! God looked at the light and smiled: 'This is GOOD.' He separated the light from the darkness, calling one 'Day' and the other 'Night.' The very first morning dawned. The very first evening settled. Day One was complete!",
            "science": "Light travels at 186,000 miles per SECOND! That's fast enough to circle the Earth 7.5 times in one second! And God created all that speed and energy just by speaking!",
            "verse": "God said, 'Let there be light,' and there was light. God saw the light, and saw that it was good. - Genesis 1:3-4 (WEB)",
            "gratitude": "Thank God for: Sunshine, flashlights, stars, fireflies, rainbows - all the beautiful light He created!",
            "coloring": "Draw the moment light first appeared - use your brightest yellows and golds against dark black!"
        },
        {
            "day": "DAY 2", "title": "SKY & WATER",
            "illustration": "A breathtaking scene of deep blue sky above and vast blue ocean below, with the separation happening dramatically. Beautiful wispy white clouds form in the new sky. The ocean stretches endlessly with gentle waves. Where sky meets water at the horizon, golden light glows. The atmosphere is being created - air between the waters above and below.",
            "story_p1": "On the second day, God looked at the waters covering everything and created something amazing: SPACE! He stretched out the sky like an enormous tent between waters above and waters below. The air we breathe, the atmosphere that protects us, the beautiful blue canopy above - all created in one word!",
            "story_p2": "Imagine the most beautiful blue sky you've ever seen - God painted that! The fluffy white clouds, the way the sky turns orange at sunset and purple at twilight - all designed by the Master Artist. Below, the deep waters waited, and above, the sky arched in perfect beauty. God was building a home for everything that would come next!",
            "science": "Our atmosphere is about 300 miles thick and contains exactly the right mix of gases for life: 78% nitrogen, 21% oxygen, and 1% other gases. Change any amount slightly and life couldn't exist!",
            "verse": "God said, 'Let there be an expanse in the middle of the waters, and let it divide the waters from the waters.' - Genesis 1:6 (WEB)",
            "gratitude": "Thank God for: Rain, clouds, blue sky, the air you breathe, storms that water the earth!",
            "coloring": "Draw the most beautiful sky you can imagine - sunrise colors, sunset colors, or starry night!"
        },

        {
            "day": "DAY 3", "title": "LAND, MOUNTAINS & PLANTS",
            "illustration": "Majestic snow-capped mountains rising from the newly formed earth, with lush green forests covering the foothills. In the foreground, an incredible garden bursts with color: red roses, purple lavender, yellow sunflowers, orange tulips, pink cherry blossoms. Tall trees bear fruit - apples, oranges, grapes. Emerald green grass carpets everything. Waterfalls cascade from rocky cliffs.",
            "story_p1": "On the third day, God gathered all the waters together, and dry ground appeared for the first time! Mountains shot up toward the sky. Valleys formed between rolling hills. Beaches lined the new coastlands. Deserts, plains, and islands - all rising from the waters at God's command!",
            "story_p2": "But God wasn't done! He spoke again, and the bare ground EXPLODED with life! Grass sprouted in waves of green. Trees rocketed upward - oaks, cedars, palms. Flowers burst open in every color imaginable - reds, blues, yellows, purples! Fruit grew instantly on trees: juicy apples, sweet oranges, perfect grapes. Seeds and nuts filled the branches. In one day, God turned bare rock into a garden paradise!",
            "science": "There are over 400,000 species of plants on Earth! Plants produce the oxygen we breathe through photosynthesis - they literally turn sunlight into food and air. Without plants, we couldn't survive!",
            "verse": "God said, 'Let the earth produce grass, herbs yielding seeds, and fruit trees bearing fruit after their kind.' And it was so. - Genesis 1:11 (WEB)",
            "gratitude": "Thank God for: Your favorite fruit, flowers, trees for climbing, grass for playing, vegetables for health!",
            "coloring": "Draw the most colorful garden ever created - include as many different flowers and trees as you can!"
        },
        {
            "day": "DAY 4", "title": "SUN, MOON & STARS",
            "illustration": "A stunning cosmic scene: the brilliant golden sun blazing with corona and solar flares on one side, the silvery-white moon with its craters and gentle glow on the other side, and between and behind them THOUSANDS of twinkling stars in every size. The Milky Way streaks across the deep blue-black sky. Planets visible in the distance. Pure celestial majesty.",
            "story_p1": "On the fourth day, God hung lights in the sky! First, the SUN - a blazing ball of fire so enormous that a million Earths could fit inside it! It provides light, warmth, energy for all plants, and marks our days. Then the gentle MOON - a faithful companion reflecting sunlight through our nights, controlling our tides.",
            "story_p2": "But God wasn't finished! He scattered STARS across the heavens like diamonds thrown across black velvet! Billions upon billions of stars - some bigger than our sun, some so far away their light takes millions of years to reach us! He named every single one! He set planets spinning in orbit, arranged galaxies in spirals, and painted nebulas in impossible colors. All in ONE DAY!",
            "science": "Our sun is 93 million miles away - exactly the right distance! Any closer, we'd burn. Any farther, we'd freeze. The sun's core is 27 million degrees! And there are more stars in the universe than grains of sand on all Earth's beaches!",
            "verse": "God made the two great lights: the greater light to rule the day, and the lesser light to rule the night. He also made the stars. - Genesis 1:16 (WEB)",
            "gratitude": "Thank God for: Sunny days, moonlit nights, stars to wish on, seasons, sunrise and sunset!",
            "coloring": "Draw a night sky full of stars, the moon, and maybe a shooting star! Add your favorite constellation!"
        },
        {
            "day": "DAY 5", "title": "SEA CREATURES & BIRDS",
            "illustration": "A vibrant split scene - below the waterline: colorful coral reefs with rainbow fish in orange, blue, yellow, and purple, a majestic blue whale, playful dolphins jumping, an octopus, jellyfish glowing, sea turtles swimming. Above the waterline: eagles soaring, colorful parrots flying, a hummingbird hovering at a flower, flamingos in pink, a peacock displaying its feathers, tiny sparrows.",
            "story_p1": "On the fifth day, God filled the waters with LIFE! Tiny colorful fish darted through coral reefs. Massive blue whales glided through the deep. Dolphins leaped for joy! Octopuses changed colors. Jellyfish pulsed with light. Sharks patrolled the depths. Seahorses swayed in currents. From the tiniest krill to the mightiest whale - the oceans TEEMED with millions of species!",
            "story_p2": "Then God filled the skies! Eagles with six-foot wingspans caught the wind. Tiny hummingbirds hovered like helicopters. Parrots exploded in reds, blues, and greens. Penguins waddled and swam. Owls prepared for night patrol. Flamingos stood in pink formations. Every bird sang a different song - God composed a symphony with wings! 'Be fruitful and multiply!' God blessed them.",
            "science": "There are over 35,000 species of fish and 10,000 species of birds! The blue whale is the largest animal to ever live - up to 100 feet long, bigger than any dinosaur! A hummingbird's wings beat 80 times per SECOND!",
            "verse": "God created the large sea creatures and every living creature that moves, with which the waters swarmed, and every winged bird. God saw that it was good. - Genesis 1:21 (WEB)",
            "gratitude": "Thank God for: Dolphins, eagles, your favorite fish, birdsong in the morning, penguins making you laugh!",
            "coloring": "Draw your favorite ocean animal AND your favorite bird together! Make them colorful!"
        },

        {
            "day": "DAY 6", "title": "ANIMALS & PEOPLE",
            "illustration": "An incredible scene of animals covering a green landscape: majestic lion with full mane, tall giraffe reaching tree tops, gray elephant with baby, black and orange tiger, fluffy panda, zebra with stripes, colorful butterflies floating, playful puppies, kittens, horses galloping. In the center, a happy man and woman stand together in a beautiful garden, smiling with arms outstretched in wonder.",
            "story_p1": "The sixth day was God's masterpiece day! First, He created land animals: mighty lions with golden manes, gentle elephants with their babies, tall giraffes reaching the treetops, playful monkeys swinging through trees, horses galloping across plains, tiny ladybugs and huge hippos! Every creature in its perfect design!",
            "story_p2": "Then came the GREATEST creation of all! God said: 'Let Us make humans in OUR IMAGE!' God personally formed the first man from the dust - then breathed His own breath of life into him! Adam opened his eyes and saw paradise. God then created Eve from Adam's side - a perfect companion. Together they were given dominion over all creation. They walked with God in the cool of the day. They were the crown of creation - made in GOD'S image!",
            "science": "There are over 6,000 species of mammals, 10,000 reptile species, and over 1 million insect species! The human body alone has 37 TRILLION cells, 206 bones, and a brain with 86 billion neurons. We are fearfully and wonderfully made!",
            "verse": "God created man in his own image. In God's image he created him; male and female he created them. - Genesis 1:27 (WEB)",
            "gratitude": "Thank God for: Your amazing body, your family, animals, pets, and being made in God's own image!",
            "coloring": "Draw yourself surrounded by your favorite animals in a beautiful garden - you are God's masterpiece!"
        },
        {
            "day": "DAY 7", "title": "REST",
            "illustration": "A serene, peaceful garden scene at sunset. Everything is in perfect harmony: animals resting together peacefully (lion beside lamb, deer beside bear), flowers in full bloom, a crystal-clear river flowing gently, fruit hanging perfectly from trees. Adam and Eve rest together in the shade. The sky is painted in the most beautiful sunset colors - golds, pinks, purples, oranges. Complete peace and perfection.",
            "story_p1": "On the seventh day, God looked at EVERYTHING He had made - light and darkness, sky and seas, mountains and flowers, sun and stars, fish and birds, animals and humans - and He declared it was VERY good! Every piece fit together perfectly. Every creature was in its place. Paradise was complete.",
            "story_p2": "So God RESTED. Not because He was tired (God never gets tired!) but because His work was FINISHED. Everything was perfect. He blessed the seventh day and made it holy - a gift of rest for all creation. This day reminds us that we don't always have to DO something. Sometimes the most important thing is to stop, rest, and enjoy what God has made! He created rest as a gift for us!",
            "science": "Scientists have proven that humans need rest! Our bodies repair cells, strengthen immune systems, and consolidate memories during sleep. Even our brains need 'down time' to process information. God designed us to need rest!",
            "verse": "God blessed the seventh day and made it holy, because in it he rested from all his work of creation. - Genesis 2:3 (WEB)",
            "gratitude": "Thank God for: Rest, sleep, weekends, vacation, peaceful quiet moments, and the gift of Sabbath!",
            "coloring": "Draw the most peaceful scene you can imagine - a place where everything is perfect and at rest."
        }
    ]


    # RENDER CREATION DAYS
    day_grays = [0.88, 0.90, 0.92, 0.94, 0.88, 0.91, 0.95]
    
    for idx, day in enumerate(days):
        bg = day_grays[idx]
        pages_for_day = 4 if idx < 6 else 3
        
        # Page 1: Day title + Illustration
        pdf.new_page()
        pdf.add_filled_rect(0, 700, 612, 92, gray=bg)
        pdf.add_filled_rect(40, 705, 532, 80, gray=0.97)
        draw_border(pdf, 40, 705, 532, 80, gray=0.3)
        pdf.add_centered_text(765, day["day"], font='F2', size=14, gray=0.5)
        pdf.add_centered_text(740, day["title"], font='F2', size=24, gray=0.1)
        pdf.add_centered_text(715, "God Speaks and It Happens!", font='F4', size=11, gray=0.4)
        
        illus_box(pdf, 450, day["illustration"], 200)
        
        # Decorative accent
        pdf.add_filled_rect(50, 430, 512, 8, gray=0.3)
        
        # Story part 1
        pdf.add_filled_rect(50, 250, 512, 165, gray=0.97)
        pdf.add_rect(50, 250, 512, 165, line_width=0.5, gray=0.5)
        wrap(pdf, 65, 400, day["story_p1"], font='F5', size=12, mw=68)
        
        # Page 2: Story part 2
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.98)
        pdf.add_filled_rect(40, 750, 532, 5, gray=bg)
        pdf.add_text(60, 740, f"{day['day']}: {day['title']} (continued)", font='F2', size=14, gray=0.2)
        pdf.add_line(60, 732, 350, 732, width=1, gray=0.4)
        
        pdf.add_filled_rect(50, 550, 512, 170, gray=0.97)
        pdf.add_rect(50, 550, 512, 170, line_width=0.5, gray=0.5)
        wrap(pdf, 65, 705, day["story_p2"], font='F5', size=12, mw=68)
        
        # Science connection
        pdf.add_filled_rect(50, 400, 512, 130, gray=0.92)
        draw_border(pdf, 50, 400, 512, 130, gray=0.4)
        pdf.add_text(65, 515, "DID YOU KNOW? (Science Connection)", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 495, day["science"], font='F4', size=11, mw=70)
        
        # Verse
        pdf.add_filled_rect(50, 300, 512, 80, gray=0.95)
        pdf.add_text(65, 365, "MEMORY VERSE:", font='F2', size=11, gray=0.2)
        wrap(pdf, 65, 345, day["verse"], font='F3', size=10, mw=72)
        
        # Page 3: Gratitude + Coloring reference
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_filled_rect(40, 720, 532, 50, gray=bg)
        pdf.add_centered_text(748, f"{day['day']}: THANK GOD FOR...", font='F2', size=16, gray=0.1)
        
        # Gratitude prompt
        pdf.add_filled_rect(50, 600, 512, 100, gray=0.88)
        draw_border(pdf, 50, 600, 512, 100, gray=0.3)
        pdf.add_text(65, 685, "THANK GOD FOR:", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 665, day["gratitude"], font='F5', size=11, mw=70)
        
        # Personal gratitude writing
        pdf.add_text(60, 570, "What else from " + day["day"] + " are you grateful for?", font='F4', size=11, gray=0.3)
        for i in range(4):
            pdf.add_line(60, 545-(i*25), 550, 545-(i*25), width=0.5, gray=0.6)
        
        # Coloring activity
        pdf.add_filled_rect(50, 250, 512, 170, gray=0.95)
        pdf.add_rect(50, 250, 512, 170, line_width=1.5, gray=0.4)
        pdf.add_text(65, 405, "COLOR / DRAW:", font='F2', size=12, gray=0.2)
        wrap(pdf, 65, 385, day["coloring"], font='F4', size=11, mw=70)
        pdf.add_centered_text(280, "[Your artwork here]", font='F3', size=11, gray=0.5)

        # Page 4 (extra page for days 1-6)
        if pages_for_day == 4:
            pdf.new_page()
            pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
            pdf.add_filled_rect(40, 720, 532, 50, gray=bg)
            pdf.add_centered_text(748, f"{day['day']} REFLECTION", font='F2', size=16, gray=0.1)
            pdf.add_text(60, 680, f"What amazes you most about {day['title']}?", font='F5', size=12, gray=0.2)
            for i in range(5):
                pdf.add_line(60, 650-(i*30), 550, 650-(i*30), width=0.5, gray=0.6)
            pdf.add_text(60, 470, "Draw or write a praise to God for this day of creation:", font='F5', size=12, gray=0.2)
            pdf.add_filled_rect(50, 200, 512, 250, gray=0.95)
            pdf.add_rect(50, 200, 512, 250, line_width=1, gray=0.4)

    # FINAL PAGE
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    draw_border(pdf, 40, 40, 532, 712, gray=0.2)
    pdf.add_centered_text(700, "GOD SAW EVERYTHING HE MADE", font='F2', size=18, gray=0.1)
    pdf.add_centered_text(670, "AND IT WAS VERY GOOD!", font='F2', size=18, gray=0.1)
    pdf.add_centered_text(630, "- Genesis 1:31 -", font='F5', size=14, gray=0.3)
    pdf.add_centered_text(570, "You are part of God's VERY GOOD creation!", font='F5', size=13, gray=0.2)
    pdf.add_centered_text(540, "He made you on purpose, for a purpose.", font='F5', size=13, gray=0.2)
    pdf.add_centered_text(510, "You are fearfully and wonderfully made!", font='F5', size=13, gray=0.2)
    pdf.add_centered_text(450, "Thank God every day for His amazing creation!", font='F4', size=12, gray=0.3)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book283_Creation_Story_Detailed.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
