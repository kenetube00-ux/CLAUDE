"""Book 214: GOD MADE EVERYTHING - Creation Week Activity Book for Ages 4-7 (KIDLYTICAL)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.93)
    pdf.add_centered_text(620, "GOD MADE", 'F2', 34)
    pdf.add_centered_text(575, "EVERYTHING!", 'F2', 34)
    pdf.add_centered_text(530, "Creation Week Activity Book", 'F4', 16, 0.2)
    pdf.add_centered_text(503, "for Ages 4-7", 'F1', 14, 0.3)
    pdf.add_centered_text(460, "Coloring + Counting + Tracing + Prayer", 'F1', 11, 0.4)
    pdf.add_centered_text(430, "KIDLYTICAL", 'F2', 14, 0.4)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "GOD MADE EVERYTHING - Creation Week Activity Book", 'F2', 11)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "Scripture from World English Bible (WEB)", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)
    pdf.add_text(72, 590, "For ages 4-7", 'F1', 9)

    days = [
        ("DAY 1: LIGHT!", "Genesis 1:3 - God said, Let there be light! And there was light.",
         "God made LIGHT and separated it from darkness. Day and night!",
         "Color the bright sunshine and the dark nighttime sky!",
         "light", "Count the rays of sunshine: draw 8 rays coming from the sun!",
         "Thank You God for LIGHT so I can see!"),
        ("DAY 2: SKY & WATER!", "Genesis 1:7 - God made the sky and separated the waters.",
         "God made the beautiful blue SKY above and the WATER below!",
         "Color the blue sky with fluffy white clouds and the water below!",
         "sky", "Count the clouds: draw 5 fluffy clouds in the sky!",
         "Thank You God for the SKY and WATER!"),
        ("DAY 3: LAND & PLANTS!", "Genesis 1:11 - Let the earth produce plants and trees!",
         "God made the dry LAND and covered it with beautiful PLANTS and TREES!",
         "Color the green land with trees, flowers, and grass!",
         "plants", "Count the flowers: draw 7 flowers growing in the garden!",
         "Thank You God for PLANTS and TREES!"),
        ("DAY 4: SUN, MOON & STARS!", "Genesis 1:16 - God made the two great lights.",
         "God put the SUN in the daytime sky and the MOON and STARS at night!",
         "Color the big yellow sun AND the moon with twinkly stars!",
         "stars", "Count the stars: draw 10 stars in the night sky!",
         "Thank You God for the SUN, MOON and STARS!"),
        ("DAY 5: FISH & BIRDS!", "Genesis 1:21 - God created the great sea creatures and every bird.",
         "God filled the oceans with FISH and the sky with BIRDS! So many!",
         "Color fish swimming in the water and birds flying in the sky!",
         "fish", "Count the fish: draw 6 fish swimming in the water!",
         "Thank You God for FISH and BIRDS!"),
        ("DAY 6: ANIMALS & PEOPLE!", "Genesis 1:27 - God created mankind in his own image.",
         "God made all the ANIMALS and then He made PEOPLE - that's you!",
         "Color your favorite animals and draw yourself with them!",
         "animals", "Count the animals: draw 4 of your favorite animals!",
         "Thank You God for ANIMALS and for making ME!"),
        ("DAY 7: REST!", "Genesis 2:2 - On the seventh day God rested.",
         "God finished making everything and He RESTED. It was all very good!",
         "Color a peaceful scene of someone resting and enjoying creation!",
         "rest", "Draw what YOU do when you rest. Do you read? Nap? Play?",
         "Thank You God for REST and for making everything GOOD!"),
    ]

    for day_num, (title, verse, summary, color_desc, trace_word, count_activity, prayer) in enumerate(days):
        # Page 1: Story + Verse
        pdf.new_page()
        pdf.add_filled_rect(50, 710, 512, 55, 0.85)
        pdf.add_centered_text(733, title, 'F2', 22)
        pdf.add_line(72, 700, 540, 700, 1, 0.6)

        pdf.add_text(72, 672, verse, 'F4', 11)
        pdf.add_text(72, 645, summary, 'F1', 12)
        pdf.add_centered_text(610, '"God said... and it was GOOD!"', 'F5', 14)

        # Coloring area
        pdf.add_text(72, 575, "COLOR THIS:", 'F2', 14)
        pdf.add_text(72, 555, color_desc, 'F1', 11, 0.4)
        pdf.add_rect(72, 320, 468, 225, 1, 0.5)
        pdf.add_centered_text(430, f"[Draw and color: Day {day_num+1} of Creation]", 'F1', 12, 0.5)

        # Tracing
        pdf.add_text(72, 290, "TRACE & WRITE:", 'F2', 13)
        pdf.add_text(72, 268, f"God made  {trace_word.upper()}", 'F2', 16, 0.6)
        pdf.add_text(72, 245, f"Write it yourself: God made _______________", 'F1', 12)
        pdf.add_line(280, 243, 540, 243, 0.5, 0.7)

        # Page 2: Counting + Prayer
        pdf.new_page()
        pdf.add_centered_text(750, f"DAY {day_num+1} ACTIVITIES", 'F2', 18)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)

        # Counting activity
        pdf.add_text(72, 710, "COUNTING ACTIVITY:", 'F2', 14)
        pdf.add_text(72, 688, count_activity, 'F1', 11)
        pdf.add_rect(72, 480, 468, 195, 1, 0.5)
        pdf.add_centered_text(575, "[Draw here!]", 'F1', 12, 0.5)

        # Prayer line
        pdf.add_text(72, 440, "MY PRAYER:", 'F2', 14)
        pdf.add_text(82, 418, prayer, 'F4', 12)
        pdf.add_text(72, 388, "What else do you want to thank God for today?", 'F1', 11)
        pdf.add_line(72, 365, 540, 365, 0.5, 0.7)
        pdf.add_line(72, 345, 540, 345, 0.5, 0.7)

        # Fun fact
        pdf.add_text(72, 310, "FUN FACT:", 'F2', 12)
        facts = [
            "Light travels at 186,000 miles per second! God made that!",
            "The sky is blue because of how sunlight bounces! God designed that!",
            "There are over 400,000 types of plants! God made them all!",
            "Our sun is so big that 1.3 million Earths could fit inside it!",
            "There are more fish in the ocean than stars we can see!",
            "Elephants are the biggest land animals - God made them gentle!",
            "Even God rested! Rest is important and good!",
        ]
        pdf.add_text(82, 290, facts[day_num], 'F1', 10, 0.3)

        # Page 3: Extra activity
        pdf.new_page()
        pdf.add_centered_text(750, f"DAY {day_num+1}: MORE FUN!", 'F2', 16)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)

        # Connect the dots / simple activity
        pdf.add_text(72, 710, "CIRCLE THE RIGHT ANSWER:", 'F2', 12)
        qs = [
            [f"What did God make on Day {day_num+1}?", "A) Pizza", f"B) {trace_word.capitalize()}", "C) Cars"],
            ["Was God's creation good?", "A) YES!", "B) No", "C) Maybe"],
            ["Who made everything?", "A) A wizard", "B) Nobody", "C) GOD!"],
        ]
        y = 685
        for q_set in qs:
            pdf.add_text(82, y, q_set[0], 'F1', 11)
            y -= 18
            for opt in q_set[1:]:
                pdf.add_text(100, y, opt, 'F1', 10)
                y -= 15
            y -= 10

        y -= 15
        pdf.add_text(72, y, "DRAW YOUR FAVORITE THING GOD MADE ON THIS DAY:", 'F2', 11)
        y -= 5
        pdf.add_rect(72, y - 200, 468, 195, 1, 0.5)

    # Days of Creation Poster Page
    pdf.new_page()
    pdf.add_centered_text(750, "7 DAYS OF CREATION POSTER", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    day_labels = [
        "Day 1: LIGHT", "Day 2: SKY & WATER", "Day 3: LAND & PLANTS",
        "Day 4: SUN, MOON, STARS", "Day 5: FISH & BIRDS",
        "Day 6: ANIMALS & PEOPLE", "Day 7: REST!"
    ]
    y = 700
    for i, label in enumerate(day_labels):
        pdf.add_filled_rect(72, y - 5, 468, 30, 0.9)
        pdf.add_rect(72, y - 5, 468, 30, 0.5, 0.5)
        pdf.add_text(82, y + 5, label, 'F2', 13)
        pdf.add_text(350, y + 5, "[draw here]", 'F1', 9, 0.5)
        y -= 42

    pdf.add_centered_text(y - 10, '"God saw everything He had made, and it was very good!"', 'F5', 11)
    pdf.add_centered_text(y - 28, "Genesis 1:31", 'F1', 9, 0.4)

    # "God Made ME!" Self-Portrait Page
    pdf.new_page()
    pdf.add_centered_text(750, "GOD MADE ME!", 'F2', 24)
    pdf.add_centered_text(720, "Psalm 139:14 - I am fearfully and wonderfully made!", 'F4', 11)
    pdf.add_line(72, 705, 540, 705, 1, 0.5)
    pdf.add_centered_text(680, "Draw a picture of YOURSELF below!", 'F1', 12)
    pdf.add_centered_text(660, "God made YOU special and wonderful!", 'F1', 11, 0.3)
    pdf.add_rect(100, 300, 412, 340, 1.5, 0.4)
    pdf.add_centered_text(280, "My name is: _____________________", 'F1', 12)
    pdf.add_centered_text(255, "I am _____ years old!", 'F1', 12)
    pdf.add_centered_text(230, "God made me special because: __________________", 'F1', 11)
    pdf.add_centered_text(200, "Thank You, God, for making ME!", 'F5', 14)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book214_Creation_Activity_Book.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
