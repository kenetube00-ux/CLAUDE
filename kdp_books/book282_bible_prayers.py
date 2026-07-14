#!/usr/bin/env python3
"""Book 282 - When Kids Pray: 10 Bible Stories About the Power of Prayer"""
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
    pdf.add_centered_text(700, "WHEN KIDS PRAY", font='F2', size=28, gray=0.1)
    pdf.add_centered_text(665, "10 Bible Stories About", font='F5', size=16, gray=0.2)
    pdf.add_centered_text(640, "the Power of Prayer", font='F5', size=16, gray=0.2)
    illus_box(pdf, 380, "A child kneeling in prayer with eyes closed, hands folded, surrounded by a soft golden glow. Above the child, divine light rays spread outward. Around the scene, small vignettes show answered prayers: chains breaking, rain falling, a whale, a healed person, an angel. Warm, hopeful atmosphere.", 160)
    pdf.add_centered_text(340, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(310, "Learn to Pray Like Bible Heroes!", font='F4', size=12, gray=0.4)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)

    # COPYRIGHT
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "WHEN KIDS PRAY", font='F2', size=16, gray=0.1)
    pdf.add_line(72, 688, 300, 688, width=0.5, gray=0.5)
    pdf.add_text(72, 665, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 645, "Scripture from World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 50, gray=0.92)
    pdf.add_text(72, 130, "For every kid who wants to talk to God - He's always listening!", font='F5', size=11, gray=0.2)

    prayers = [
        {
            "title": "HANNAH'S TEARS",
            "result": "God Gave Her Samuel",
            "type": "Persistent Prayer",
            "illustration": "Hannah kneeling in the tabernacle with tears streaming down her face, hands raised toward heaven. Her lips move in silent, passionate prayer. Soft golden light from oil lamps illuminates her. The tabernacle curtains are deep blue and purple. Her expression shows deep anguish turning to hope. The priest Eli watches from his chair nearby.",
            "story": "Year after year, Hannah prayed for a baby. Her rival Peninnah mocked her cruelly every single day. At the yearly feast, Hannah cried so hard she couldn't eat. She went to the tabernacle and poured her heart out to God so passionately that her lips moved but no sound came out. The priest Eli thought she was drunk! But Hannah was simply praying with everything in her soul. She promised God: 'If you give me a son, I'll dedicate him to You forever!'",
            "how_prayed": "With tears, with all her heart, silently but passionately. She didn't give up after one try - she prayed for YEARS. She made a bold promise to God.",
            "when_i_pray": "When I really, really want something and have to wait a long time. When others mock me for my faith. When I feel desperate.",
            "verse": "For this child I prayed; and the LORD has given me my petition. - 1 Samuel 1:27 (WEB)",
            "activity": "Write a prayer about something you've been waiting for. Don't give up! God hears persistent prayers!"
        },
        {
            "title": "SOLOMON'S WISH",
            "result": "Wisdom Instead of Riches",
            "type": "Right Priorities",
            "illustration": "Young King Solomon kneeling before a glowing altar at night in Gibeon. God's presence appears as brilliant golden light above. Solomon's face shows humility despite his royal robes and crown. Around the edges, faded images show what he could have asked for: gold coins, armies, a long life - but he chose wisdom, shown as an open book glowing with light.",
            "story": "God appeared to young King Solomon in a dream and said something incredible: 'Ask for ANYTHING you want, and I'll give it to you!' Imagine that! Solomon could have asked for riches, power, revenge on his enemies, a long life. But instead he said: 'I'm just a young man who doesn't know how to lead. Give me a wise and understanding heart to judge Your people.' God was SO pleased that He gave Solomon wisdom AND all the things he didn't ask for - wealth, honor, and fame!",
            "how_prayed": "Humbly! Solomon admitted he was young and needed help. He asked for what would help OTHERS (wisdom to lead) instead of what would benefit only himself.",
            "when_i_pray": "When I need to make a decision. When I could be selfish but choose to ask for what helps others. When I need God's wisdom for a problem.",
            "verse": "Give your servant an understanding heart to judge your people. - 1 Kings 3:9 (WEB)",
            "activity": "If God said 'Ask for ANYTHING,' what would you ask? Write it down. Is it selfish or does it help others too?"
        },

        {
            "title": "ELIJAH'S RAIN",
            "result": "After 3 Years of Drought",
            "type": "Faith Prayer",
            "illustration": "Elijah crouched on top of Mount Carmel with his face between his knees in intense prayer. His servant stands nearby looking toward the sea for clouds. In the distance, a tiny cloud the size of a man's hand appears over the blue Mediterranean Sea. The land below is brown and dry. But dark rain clouds begin forming rapidly in the sky.",
            "story": "For three and a half years, no rain fell on Israel. The land was cracked and dead. Animals died. People starved. It was God's judgment on their idol worship. After Elijah's victory over the prophets of Baal, he climbed Carmel and prayed for rain. He put his face between his knees and prayed intensely. He sent his servant to look at the sky. 'Nothing.' He prayed again. 'Nothing.' Seven times he prayed! The seventh time: 'A cloud! Small as a man's hand!' Minutes later, the sky turned black with storm clouds. RAIN POURED DOWN!",
            "how_prayed": "Intensely and repeatedly! Elijah didn't stop after one try or even six tries. He prayed SEVEN times with full faith until the answer came.",
            "when_i_pray": "When I need to keep praying and not give up. When the answer doesn't come immediately. When I need to pray until I see even a small sign of change.",
            "verse": "Elijah prayed earnestly that it might not rain, and it didn't rain for three years and six months. - James 5:17 (WEB)",
            "activity": "Choose one thing to pray about 7 times today (morning, lunch, after school, dinner, bedtime, etc.). Watch for God's 'small cloud'!"
        },
        {
            "title": "HEZEKIAH'S HEALING",
            "result": "15 More Years of Life",
            "type": "Desperate Prayer",
            "illustration": "King Hezekiah lying sick in bed, face turned toward the stone wall, tears streaming as he prays desperately. His room is dimly lit by a single oil lamp. Through the window, a sundial is visible with its shadow moving BACKWARD ten steps - a miracle sign. God's light begins to enter the room as healing comes. The scene transitions from despair to hope.",
            "story": "King Hezekiah was deathly ill. The prophet Isaiah delivered terrible news: 'Set your house in order - you're going to die.' But Hezekiah turned his face to the wall and WEPT before God: 'Remember, LORD, how I've walked before You faithfully with my whole heart!' His tears soaked the pillow. Before Isaiah even left the courtyard, God spoke: 'I've heard your prayer. I've seen your tears. I will heal you and add FIFTEEN YEARS to your life!' God even made the sundial's shadow go backward as a sign!",
            "how_prayed": "Desperately! With tears! Hezekiah reminded God of his faithfulness and poured out his heart honestly. He didn't accept the bad news as final.",
            "when_i_pray": "When I or someone I love is very sick. When bad news comes. When things seem hopeless and I need God to change the situation.",
            "verse": "I have heard your prayer. I have seen your tears. Behold, I will heal you. - 2 Kings 20:5 (WEB)",
            "activity": "Is someone you know sick? Write their name and pray desperately for them. God sees your tears and hears your prayers!"
        },
        {
            "title": "DANIEL'S WINDOWS",
            "result": "Praying Despite the Law",
            "type": "Courageous Prayer",
            "illustration": "Daniel kneeling at his open window facing Jerusalem, hands clasped, eyes closed in peace despite knowing soldiers watch from below. Through the window, the setting sun casts golden light on his praying form. In the street below, jealous officials point up at him and whisper to guards. Daniel is completely focused on God, choosing prayer over safety.",
            "story": "A new law said anyone who prayed to God (instead of the king) would be thrown to the lions. Daniel heard about the law. Did he close his windows? Did he pray in secret? Did he take a 30-day break from prayer? NO! Daniel went home, opened his windows wide, knelt down, and prayed to God three times that day - exactly like he always did! His enemies watched, grinning. They'd trapped him. But Daniel chose prayer over his own life!",
            "how_prayed": "Openly, bravely, consistently! Daniel didn't let fear change his prayer habits. He prayed the same way he always did - faithfully, three times daily.",
            "when_i_pray": "When it's hard or unpopular to pray. When people might laugh at me. When I'm tempted to hide my faith. When prayer feels risky.",
            "verse": "He kneeled on his knees three times a day, and prayed and gave thanks before his God, as he did before. - Daniel 6:10 (WEB)",
            "activity": "Pray openly today where someone can see you - at lunch, before a test, with a friend. Don't be ashamed of talking to God!"
        },
        {
            "title": "JONAH'S WHALE PRAYER",
            "result": "Praying from Inside a Fish!",
            "type": "Praying Anywhere",
            "illustration": "Jonah inside the whale's belly, kneeling in the dark curved space with seaweed wrapped around him. Despite the terrible surroundings, his face is turned upward in desperate prayer. A faint shaft of light filters in. The ribbed interior of the whale surrounds him. His hands reach toward heaven. The scene is dark but hopeful - God hears even here!",
            "story": "Could there be a WORSE place to pray than inside a giant fish? Surrounded by seaweed, in complete darkness, with stomach acid all around? But Jonah proved that you can pray ANYWHERE! From the belly of the whale, Jonah cried out to God. He admitted he was wrong to run. He praised God even in that disgusting situation. And God heard him! God commanded the fish to vomit Jonah onto dry land. Prayer works everywhere - even inside a fish!",
            "how_prayed": "From the worst place imaginable! Jonah prayed a prayer of repentance (admitting he was wrong) and praise (thanking God even before deliverance). He proved no place is too far from God!",
            "when_i_pray": "When I'm in a terrible situation of my own making. When I need to admit I was wrong. When I feel like God couldn't possibly hear me where I am.",
            "verse": "I called because of my affliction to the LORD. He answered me. Out of the belly of Sheol I cried. - Jonah 2:2 (WEB)",
            "activity": "Pray in an unusual place today - in your closet, under a tree, in your car. Remember: God hears you EVERYWHERE!"
        },

        {
            "title": "JESUS IN THE GARDEN",
            "result": "Not My Will But Yours",
            "type": "Surrender Prayer",
            "illustration": "Jesus kneeling alone in the Garden of Gethsemane at night under ancient twisted olive trees. His face shows agony as He prays. Sweat drops fall like blood. Moonlight filters through the leaves creating dappled silver light. In the distant background, the disciples sleep. An angel appears faintly to strengthen Him. The weight of the world is on His shoulders.",
            "story": "The night before the cross, Jesus faced the hardest prayer of His life. He KNEW what was coming - betrayal, torture, death. He was so distressed that He sweated drops of blood! Three times He prayed: 'Father, if it's possible, let this cup pass from Me.' He was honest about His pain! But each time He added the most powerful words in prayer history: 'Nevertheless, not My will, but YOURS be done.' Jesus showed us that the highest prayer isn't getting what WE want - it's wanting what GOD wants.",
            "how_prayed": "Honestly (He told God His feelings), repeatedly (three times!), and with surrender (Thy will be done). Jesus prayed the hardest prayer - letting go of His own desires.",
            "when_i_pray": "When I want something but I'm not sure it's God's will. When I need to let go of my plans and trust God's bigger plan. When prayer is hard and painful.",
            "verse": "Not my will, but yours, be done. - Luke 22:42 (WEB)",
            "activity": "Write a prayer surrendering something to God: 'God, I want _____ but more than that, I want YOUR will. Help me trust You.'"
        },
        {
            "title": "PETER'S CHAINS",
            "result": "Church Prays, Angel Appears",
            "type": "Community Prayer",
            "illustration": "Split scene: Top - Peter chained in a dark prison cell between sleeping guards, looking hopeless. Bottom - a room full of believers (men, women, children) on their knees praying fervently together by lamplight, faces earnest and unified. A golden prayer connection rises from the praying group toward Peter's cell. Supernatural energy connecting prayer to answer.",
            "story": "Peter was locked in maximum-security prison, chained between soldiers, guarded by sixteen men. Execution was scheduled for morning. What could anyone do? The church did the ONLY thing that could help - they prayed ALL NIGHT LONG! Together, desperately, without stopping. And in the middle of the night, an angel broke into the prison, snapped Peter's chains, opened locked doors, and walked him right past every guard! Community prayer moved heaven!",
            "how_prayed": "Together as a community! All night! Without stopping! Desperately! They combined their faith and stormed heaven as one united voice. And God answered BEYOND what they expected!",
            "when_i_pray": "When a problem is too big for one person's prayer. When I need to join with others. When someone I know is in serious trouble and needs a prayer army!",
            "verse": "Peter was kept in the prison, but the church prayed earnestly to God for him. - Acts 12:5 (WEB)",
            "activity": "Gather 3+ friends or family members and pray TOGETHER for something specific. Community prayer is POWERFUL!"
        },
        {
            "title": "PAUL & SILAS SINGING",
            "result": "Earthquake in Prison",
            "type": "Praise-Prayer",
            "illustration": "Paul and Silas in stocks in a dark inner prison cell, feet locked in wooden blocks, backs bloody from beating - yet their mouths are OPEN IN SONG! Their faces show joy despite pain. Musical notes seem to float upward. Other prisoners lean toward them, listening in amazement. The stone walls begin to crack as the earthquake starts. Chains begin to loosen.",
            "story": "Beaten, bleeding, and locked in stocks in the darkest inner cell - what would YOU do? Paul and Silas did something incredible: at MIDNIGHT, they started SINGING praise to God! Not quiet humming - LOUD praise so all the prisoners could hear! They turned their prison into a worship service! And God responded: EARTHQUAKE! The foundations shook! Every door flew open! Every chain fell off! But instead of escaping, they led the jailer to faith in Jesus!",
            "how_prayed": "Through PRAISE! Through SINGING! Even in pain, even in chains, they praised God BEFORE the answer came. Their worship shook the foundations!",
            "when_i_pray": "When things are terrible and I don't feel like praising. When I need to worship BEFORE I see the answer. When praise seems impossible but I do it anyway!",
            "verse": "About midnight Paul and Silas were praying and singing hymns to God, and the prisoners were listening to them. - Acts 16:25 (WEB)",
            "activity": "Next time you're sad or in a tough situation, SING a praise song to God! Write your own short praise song here."
        },
        {
            "title": "THE LORD'S PRAYER",
            "result": "Jesus Teaches How to Pray",
            "type": "Prayer Model",
            "illustration": "Jesus sitting on a hillside with His disciples gathered around Him attentively. He gestures as He teaches them to pray. Behind Him, the words of the Lord's Prayer float in elegant script against a golden sky. The disciples lean forward eagerly, some with eyes closed practicing. Green hillside, blue Sea of Galilee in the distance. Peaceful, instructional atmosphere.",
            "story": "The disciples watched Jesus pray and saw RESULTS - healings, miracles, peace! They asked: 'Lord, TEACH US to pray!' So Jesus gave them the perfect prayer model. It starts with worship ('Our Father in heaven, hallowed be Your name'), then God's plans ('Your kingdom come, Your will be done'), then our needs ('Give us daily bread'), then relationships ('Forgive us as we forgive'), then protection ('Lead us not into temptation, deliver us from evil'). It's the perfect prayer blueprint!",
            "how_prayed": "Jesus taught a PATTERN: Start with worship, then pray for God's will, then your needs, then forgiveness, then protection. It covers everything!",
            "when_i_pray": "Every day! This is a model for ALL prayer. Use it as a guide when you don't know what to say. It covers every area of life!",
            "verse": "Our Father who is in heaven, hallowed be your name. Your Kingdom come. Your will be done on earth as it is in heaven. - Matthew 6:9-10 (WEB)",
            "activity": "Write your own prayer using the Lord's Prayer pattern: Worship + God's will + My needs + Forgiveness + Protection."
        }
    ]


    # RENDER PRAYER STORIES
    gray_vals = [0.88, 0.92, 0.95, 0.90, 0.93, 0.88, 0.97, 0.91, 0.94, 0.89]
    
    for idx, p in enumerate(prayers):
        bg = gray_vals[idx % len(gray_vals)]
        
        # Page 1: Title + Illustration + Story
        pdf.new_page()
        pdf.add_filled_rect(0, 720, 612, 72, gray=bg)
        pdf.add_filled_rect(45, 725, 522, 60, gray=0.97)
        draw_border(pdf, 45, 725, 522, 60, gray=0.3)
        pdf.add_centered_text(762, f"Prayer Story {idx+1}: {p['type']}", font='F4', size=10, gray=0.5)
        pdf.add_centered_text(742, p["title"], font='F2', size=18, gray=0.1)
        pdf.add_centered_text(727, f"Result: {p['result']}", font='F5', size=10, gray=0.3)
        
        illus_box(pdf, 550, p["illustration"], 140)
        
        pdf.add_filled_rect(50, 350, 512, 180, gray=0.97)
        pdf.add_rect(50, 350, 512, 180, line_width=0.5, gray=0.5)
        pdf.add_text(60, 515, "THE STORY:", font='F2', size=11, gray=0.2)
        wrap(pdf, 60, 495, p["story"], font='F4', size=11, mw=72)
        
        # Page 2: How they prayed + When I Can Pray + Verse + Activity + Write Your Prayer
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_text(60, 760, p["title"] + " - Learning to Pray", font='F2', size=13, gray=0.2)
        pdf.add_line(60, 752, 400, 752, width=0.5, gray=0.4)
        
        # How They Prayed
        pdf.add_filled_rect(50, 650, 512, 80, gray=bg)
        draw_border(pdf, 50, 650, 512, 80, gray=0.4)
        pdf.add_text(65, 715, "HOW THEY PRAYED:", font='F2', size=11, gray=0.1)
        wrap(pdf, 65, 695, p["how_prayed"], font='F5', size=11, mw=70)
        
        # I Can Pray Like This When
        pdf.add_filled_rect(50, 560, 512, 70, gray=0.92)
        pdf.add_text(65, 615, "I CAN PRAY LIKE THIS WHEN...", font='F2', size=11, gray=0.1)
        wrap(pdf, 65, 595, p["when_i_pray"], font='F4', size=10, mw=72)
        
        # Verse
        pdf.add_filled_rect(50, 480, 512, 60, gray=0.95)
        pdf.add_text(65, 525, "PRAYER VERSE:", font='F2', size=10, gray=0.2)
        wrap(pdf, 65, 505, p["verse"], font='F3', size=9, mw=75)
        
        # Activity
        pdf.add_filled_rect(50, 390, 512, 70, gray=0.88)
        pdf.add_rect(50, 390, 512, 70, line_width=1, gray=0.4)
        pdf.add_text(65, 445, "PRAYER ACTIVITY:", font='F2', size=11, gray=0.1)
        wrap(pdf, 65, 425, p["activity"], font='F4', size=10, mw=70)
        
        # Write Your Own Prayer
        pdf.add_text(60, 360, "WRITE YOUR OWN PRAYER:", font='F2', size=12, gray=0.1)
        for i in range(5):
            pdf.add_line(60, 335-(i*25), 550, 335-(i*25), width=0.5, gray=0.6)

    # FINAL PAGE - My Prayer Journal
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    pdf.add_filled_rect(40, 710, 532, 60, gray=0.88)
    draw_border(pdf, 40, 710, 532, 60, gray=0.3)
    pdf.add_centered_text(745, "MY PRAYER COMMITMENT", font='F2', size=18, gray=0.1)
    pdf.add_centered_text(718, "I commit to talking to God every day!", font='F4', size=12, gray=0.3)
    
    pdf.add_text(60, 680, "My daily prayer time will be:", font='F5', size=12, gray=0.2)
    pdf.add_line(60, 660, 300, 660, width=0.5, gray=0.6)
    pdf.add_text(60, 640, "My prayer place will be:", font='F5', size=12, gray=0.2)
    pdf.add_line(60, 620, 300, 620, width=0.5, gray=0.6)
    pdf.add_text(60, 590, "3 people I will pray for every day:", font='F5', size=12, gray=0.2)
    for i in range(3):
        pdf.add_text(60, 565-(i*25), f"{i+1}.", font='F4', size=11, gray=0.3)
        pdf.add_line(80, 565-(i*25), 400, 565-(i*25), width=0.5, gray=0.6)
    
    pdf.add_filled_rect(50, 380, 512, 60, gray=0.92)
    pdf.add_centered_text(420, "Remember: God ALWAYS hears you!", font='F2', size=14, gray=0.2)
    pdf.add_centered_text(395, "He loves when you talk to Him!", font='F5', size=12, gray=0.3)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book282_Kids_Prayer_Stories.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
