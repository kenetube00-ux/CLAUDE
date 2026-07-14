#!/usr/bin/env python3
"""Book 284 - The First Christmas: The True Story of Jesus' Birth Beautifully Told"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    def draw_border(pdf, x, y, w, h, gray=0.3):
        pdf.add_rect(x, y, w, h, line_width=2, gray=gray)
        pdf.add_rect(x+3, y+3, w-6, h-6, line_width=0.5, gray=gray)

    def illus_box(pdf, y, desc, height=140):
        pdf.add_filled_rect(60, y, 492, height, gray=0.95)
        pdf.add_rect(60, y, 492, height, line_width=1.5, gray=0.4)
        pdf.add_text(70, y+height-18, "[FULL-PAGE ILLUSTRATION:", font='F2', size=10, gray=0.3)
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
    pdf.add_filled_rect(50, 580, 512, 150, gray=0.88)
    pdf.add_centered_text(700, "THE FIRST CHRISTMAS", font='F2', size=28, gray=0.1)
    pdf.add_centered_text(665, "The True Story of Jesus' Birth", font='F5', size=16, gray=0.2)
    pdf.add_centered_text(638, "Beautifully Told", font='F5', size=16, gray=0.2)
    illus_box(pdf, 340, "A beautiful nativity scene at night: Baby Jesus in a manger glowing with soft golden light. Mary and Joseph lean close. A bright star shines directly above the stable. Shepherds approach from one side, wise men from the other. Angels fill the sky. Animals watch peacefully. The scene radiates warmth, love, and holy mystery.", 180)
    pdf.add_centered_text(300, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(270, "With Illustrations, Facts & Advent Activities", font='F4', size=12, gray=0.4)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)

    # COPYRIGHT
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "THE FIRST CHRISTMAS", font='F2', size=16, gray=0.1)
    pdf.add_line(72, 688, 350, 688, width=0.5, gray=0.5)
    pdf.add_text(72, 665, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 645, "Scripture from World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 50, gray=0.92)
    pdf.add_text(72, 130, "For every child who loves Christmas - this is what it's really about!", font='F5', size=11, gray=0.2)

    chapters = [
        {
            "title": "ANGEL VISITS MARY",
            "chapter": "Chapter 1",
            "illustration": "Angel Gabriel appearing in brilliant white with massive golden wings spread wide, standing in a small room in Nazareth. Young Mary, about 14, kneels in awe and surprise, her simple blue dress spreading around her. Divine golden light fills the humble room. Pottery and simple woven items in the background. Gabriel's expression is warm and reassuring. Mary's face shows wonder turning to acceptance.",
            "narrative": "In a tiny village called Nazareth lived a young girl named Mary. She was kind, faithful, and loved God with all her heart. One ordinary day, as she went about her chores, the room suddenly filled with blinding light! An angel - Gabriel himself - appeared before her! 'Greetings, favored one!' he said. 'The Lord is with you!' Mary was terrified! But Gabriel said: 'Don't be afraid, Mary. God has chosen YOU for the greatest honor in history. You will have a baby - God's own Son! He will be called Jesus, and His kingdom will never end!' Mary trembled, but her faith was strong. She whispered: 'I am the Lord's servant. Let it be as you say.'",
            "verse": "The angel said to her, 'Don't be afraid, Mary, for you have found favor with God.' - Luke 1:30 (WEB)",
            "fact": "Mary was likely between 13-15 years old - a teenager! God chose a young person to play the most important role in history!",
            "activity": "Mary said 'yes' to God's amazing plan. What is God asking YOU to say 'yes' to? Write it here."
        },
        {
            "title": "THE JOURNEY TO BETHLEHEM",
            "chapter": "Chapter 2",
            "illustration": "Mary riding a small gray donkey along a dusty road, very pregnant and tired but peaceful. Joseph walks beside her holding the donkey's rope, looking concerned and protective. The road winds through brown hills toward the distant town of Bethlehem. Stars are beginning to appear in the darkening purple sky. Other travelers visible on the road. The journey looks long and exhausting.",
            "narrative": "The Roman emperor ordered everyone to return to their ancestral city to be counted. For Joseph, that meant Bethlehem - 90 miles from Nazareth! Mary was nearly nine months pregnant. The journey took about a week on foot and donkey, over rocky hills and through dusty valleys. Mary's baby could come any day! Joseph walked beside her, worried but trusting God. Every bump on the road, every hill they climbed, brought them closer to the place where God had planned, hundreds of years earlier, for His Son to be born. The ancient prophet Micah had written: 'But you, Bethlehem, though small, out of you will come a ruler over Israel.'",
            "verse": "Joseph also went up from Galilee, out of the city of Nazareth, into the city of David, which is called Bethlehem. - Luke 2:4 (WEB)",
            "fact": "The journey from Nazareth to Bethlehem is about 90 miles. On foot with a donkey, it would take 4-7 days! That's like walking from one city to another!",
            "activity": "Plan a 'journey' of kindness this week - each day, do one kind thing for someone as you move toward Christmas!"
        },
        {
            "title": "NO ROOM AT THE INN",
            "chapter": "Chapter 3",
            "illustration": "A tired, dusty Joseph knocking on a wooden door at night while Mary sits exhausted on the donkey behind him. The innkeeper stands in the doorway shaking his head sadly, pointing toward a small stone stable behind the inn. The town of Bethlehem is crowded and bustling. Lanterns glow in windows. The one open door leads to a humble stable with hay visible inside.",
            "narrative": "Bethlehem was PACKED with travelers! Every room was full. Every home had guests. Joseph knocked on door after door, growing more desperate with each rejection. Mary gripped the donkey's mane as another wave of pain washed over her - the baby was coming SOON! 'Please,' Joseph begged at yet another door, 'my wife is about to have a baby!' The innkeeper looked sorry: 'I have no room... but there's a stable out back. It's warm and dry.' A stable? For the Son of God? But God had a plan. The King of the Universe would enter the world in the humblest place - showing that He came for everyone, not just the rich and powerful.",
            "verse": "She wrapped him in bands of cloth and laid him in a manger, because there was no room for them in the inn. - Luke 2:7 (WEB)",
            "fact": "Stables in Bible times were often caves carved into hillsides! Animals lived there and mangers (feeding troughs) were carved from stone or wood. Not fancy - but God chose it on purpose!",
            "activity": "Make room for Jesus! Clear a space in your heart this week. What distractions can you remove to focus on Him?"
        },

        {
            "title": "BORN IN A MANGER",
            "chapter": "Chapter 4",
            "illustration": "The holy moment: Baby Jesus wrapped tightly in strips of white cloth, lying in a stone manger filled with soft hay. Mary kneels beside Him, face glowing with love and exhaustion. Joseph stands behind, one hand on Mary's shoulder, tears in his eyes. A warm oil lamp casts golden light. A cow and donkey watch quietly from their stalls. Straw covers the stone floor. Everything is humble but glowing with divine presence.",
            "narrative": "In that humble stable, surrounded by the warm breath of animals, Mary gave birth to her baby boy. She wrapped Him carefully in strips of cloth and laid Him gently in the feeding trough filled with soft hay. This was Jesus - Immanuel - GOD WITH US! The Creator of the universe, the One who spoke stars into existence, now lay as a tiny, helpless baby. He didn't come in a palace. He didn't arrive with trumpets and armies. He came quietly, humbly, to a teenage mother in a borrowed stable. His first bed was an animal's food dish. His first visitors would be common shepherds. God chose to enter our world at the very bottom - so He could lift EVERYONE up!",
            "verse": "She gave birth to her firstborn son. She wrapped him in bands of cloth and laid him in a manger. - Luke 2:7 (WEB)",
            "fact": "The name 'Jesus' means 'God saves.' The title 'Immanuel' means 'God with us.' Both names together tell the whole Christmas story: God came to be with us and save us!",
            "activity": "Jesus was born in the humblest place possible. How can you serve others humbly this Christmas season?"
        },
        {
            "title": "SHEPHERDS & ANGELS",
            "chapter": "Chapter 5",
            "illustration": "A dark hillside suddenly BLAZING with supernatural light! The entire night sky is filled with thousands of angels in brilliant white, wings spread, singing in glory. Below, terrified shepherds stumble backward, shielding their eyes from the brightness. Their sheep scatter. One angel in the foreground announces the news with arms outstretched. The glory of God radiates in golden rays. The contrast between dark earth and blazing heaven is dramatic.",
            "narrative": "On the hills outside Bethlehem, shepherds huddled around a fire watching their sheep. It was an ordinary, quiet night. Until it WASN'T! Suddenly, an angel appeared in blazing glory! The shepherds were TERRIFIED! 'Don't be afraid!' the angel said. 'I bring you GOOD NEWS of GREAT JOY for ALL people! Today in Bethlehem, a Savior has been born - He is Christ the Lord! You'll find Him wrapped in cloths, lying in a manger.' Then - as if one angel wasn't enough - the entire sky EXPLODED with angels! Thousands upon thousands, singing: 'GLORY TO GOD IN THE HIGHEST! Peace on earth! Goodwill to all!' The shepherds ran to Bethlehem and found everything exactly as the angel said!",
            "verse": "The angel said to them, 'Don't be afraid, for behold, I bring you good news of great joy which will be for all the people.' - Luke 2:10 (WEB)",
            "fact": "God announced Jesus' birth to SHEPHERDS first - not kings, not priests, not rich people. Shepherds were considered lowly workers. God showed that Jesus came for EVERYONE, especially the ordinary!",
            "activity": "Be an 'angel' this week - share the GOOD NEWS with someone! Tell a friend why Christmas matters!"
        },
        {
            "title": "FOLLOWING THE STAR",
            "chapter": "Chapter 6",
            "illustration": "Three richly dressed wise men on decorated camels traveling across a moonlit desert landscape. They follow an extraordinarily bright star that shines directly ahead, casting a beam of light toward distant Bethlehem on the horizon. The wise men wear colorful robes - purple, deep red, and royal blue - with golden turbans. Their camels carry ornate saddlebags with gifts. The star dominates the night sky, far brighter than all other stars.",
            "narrative": "Far to the East, wise men who studied the stars saw something extraordinary: a new star appeared in the sky! Not just any star - a star so bright and unusual that they knew it meant something incredible. These scholars, perhaps from Persia or Babylon, understood from ancient writings that a great King had been born in Israel. So they packed precious gifts and began an incredible journey of perhaps 1,000 miles! Week after week they traveled, following that miraculous star across deserts and mountains. Nothing would stop them from worshiping this new King! The star moved ahead of them, guiding them, until it stopped directly over one specific place in little Bethlehem.",
            "verse": "The star which they saw in the east went before them until it came and stood over where the young child was. - Matthew 2:9 (WEB)",
            "fact": "The wise men (Magi) were likely scholars from Babylon or Persia - they traveled about 900-1,000 miles! Their journey may have taken 3-12 months. That's some serious dedication!",
            "activity": "What 'star' is God using to guide you right now? A Bible verse? A person? A feeling? Follow it!"
        },
        {
            "title": "GIFTS FOR A KING",
            "chapter": "Chapter 7",
            "illustration": "The three wise men kneeling in reverence before the young child Jesus, who sits on Mary's lap. They offer their gifts: one presents a chest of gleaming gold coins, another holds an ornate jar of frankincense with wispy smoke rising, the third offers a beautiful bottle of myrrh. Their expensive robes pool on the simple floor. The contrast between their wealth and the humble home is striking. Jesus reaches toward them with small hands.",
            "narrative": "When the wise men entered the house and saw the child Jesus with Mary, they fell to their knees and WORSHIPED Him! These were powerful, wealthy, educated men - yet they bowed before a small child because they recognized who He truly was! Then they opened their treasures: GOLD - because He is the King of Kings! FRANKINCENSE - a priestly incense, because He would be our High Priest before God! MYRRH - a burial spice, because He would one day give His life for us. Every gift pointed to who Jesus is and what He came to do. These weren't random presents - they were prophetic!",
            "verse": "They came into the house and saw the young child with Mary, his mother, and they fell down and worshiped him. Opening their treasures, they offered him gifts. - Matthew 2:11 (WEB)",
            "fact": "Gold = King. Frankincense = Priest (used in temple worship). Myrrh = Sacrifice (used for burial). Each gift was a prophecy about who Jesus would be! Pretty amazing 'baby shower' gifts!",
            "activity": "What gift can YOU give Jesus this Christmas? Your time? Your obedience? Your love? Write your gift to Him."
        },
        {
            "title": "THE MEANING OF CHRISTMAS",
            "chapter": "Chapter 8",
            "illustration": "A beautiful composite nativity scene with ALL the characters together: Baby Jesus glowing in the manger at center, Mary and Joseph close by, shepherds kneeling with a lamb, wise men offering gifts, angels singing above, animals watching peacefully. The star shines brilliant directly above. Everything radiates with warm golden divine light. The scene captures the full wonder, love, and meaning of the first Christmas.",
            "narrative": "Christmas isn't about presents under a tree. It's not about Santa or cookies or vacation. The REAL meaning of Christmas is the most amazing love story ever told: GOD LOVED YOU SO MUCH that He sent His only Son to become a baby - to grow up, live perfectly, and die for YOUR sins so you could be forgiven and live forever! Jesus left the glory of heaven to sleep in hay. The King chose a stable. The Creator became a creature. The Mighty God became a helpless infant. WHY? Because He LOVES you. Because nothing else could save you. Because He wanted to be CLOSE to you forever. THAT'S Christmas! Emmanuel - God WITH us!",
            "verse": "For God so loved the world, that he gave his one and only Son, that whoever believes in him should not perish, but have eternal life. - John 3:16 (WEB)",
            "fact": "Christmas celebrations began in the early church around the 4th century. But the EVENT happened about 2,000 years ago in a real place, to real people, fulfilling real prophecies written hundreds of years earlier!",
            "activity": "Write a letter to Jesus thanking Him for Christmas. Tell Him what His birth means to YOU personally."
        }
    ]


    # RENDER CHAPTERS
    gray_vals = [0.88, 0.92, 0.95, 0.90, 0.93, 0.88, 0.97, 0.91]
    
    for idx, ch in enumerate(chapters):
        bg = gray_vals[idx % len(gray_vals)]
        
        # Page 1: Chapter title + Illustration
        pdf.new_page()
        pdf.add_filled_rect(0, 700, 612, 92, gray=bg)
        pdf.add_filled_rect(40, 705, 532, 80, gray=0.97)
        draw_border(pdf, 40, 705, 532, 80, gray=0.3)
        pdf.add_centered_text(762, ch["chapter"], font='F4', size=11, gray=0.5)
        pdf.add_centered_text(738, ch["title"], font='F2', size=20, gray=0.1)
        
        illus_box(pdf, 460, ch["illustration"], 200)
        
        pdf.add_filled_rect(50, 440, 512, 8, gray=0.3)
        
        # Narrative start
        pdf.add_filled_rect(50, 200, 512, 220, gray=0.97)
        pdf.add_rect(50, 200, 512, 220, line_width=0.5, gray=0.5)
        wrap(pdf, 65, 405, ch["narrative"], font='F5', size=11, mw=70)
        
        # Page 2: Verse + Fact + Activity
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_text(60, 760, ch["title"] + " (continued)", font='F2', size=13, gray=0.2)
        pdf.add_line(60, 752, 400, 752, width=0.5, gray=0.4)
        
        # Verse box
        pdf.add_filled_rect(50, 650, 512, 80, gray=0.92)
        draw_border(pdf, 50, 650, 512, 80, gray=0.4)
        pdf.add_text(65, 715, "KEY VERSE:", font='F2', size=11, gray=0.1)
        wrap(pdf, 65, 695, ch["verse"], font='F3', size=10, mw=72)
        
        # Did You Know?
        pdf.add_filled_rect(50, 540, 512, 90, gray=bg)
        pdf.add_text(65, 615, "DID YOU KNOW?", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 595, ch["fact"], font='F4', size=10, mw=72)
        
        # Advent Activity
        pdf.add_filled_rect(50, 420, 512, 100, gray=0.95)
        pdf.add_rect(50, 420, 512, 100, line_width=1, gray=0.4)
        pdf.add_text(65, 505, "ADVENT ACTIVITY:", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 485, ch["activity"], font='F4', size=11, mw=70)
        
        # Writing lines
        for i in range(4):
            pdf.add_line(60, 380-(i*25), 550, 380-(i*25), width=0.5, gray=0.6)

    # FINAL PAGE
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    draw_border(pdf, 40, 40, 532, 712, gray=0.2)
    pdf.add_centered_text(700, "MERRY CHRISTMAS!", font='F2', size=24, gray=0.1)
    pdf.add_centered_text(660, "For to us a child is born, to us a son is given,", font='F5', size=13, gray=0.2)
    pdf.add_centered_text(640, "and the government will be on his shoulders.", font='F5', size=13, gray=0.2)
    pdf.add_centered_text(620, "And he will be called Wonderful Counselor,", font='F5', size=13, gray=0.2)
    pdf.add_centered_text(600, "Mighty God, Everlasting Father, Prince of Peace.", font='F5', size=13, gray=0.2)
    pdf.add_centered_text(570, "- Isaiah 9:6 -", font='F4', size=11, gray=0.4)
    pdf.add_centered_text(500, "Jesus is the REASON for the season!", font='F2', size=16, gray=0.2)
    pdf.add_centered_text(460, "Thank You, God, for the greatest gift ever given.", font='F5', size=13, gray=0.3)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book284_Christmas_Story_Kids.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
