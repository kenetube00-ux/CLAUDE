#!/usr/bin/env python3
"""Book 280 - Amazing Women of the Bible: 10 Stories of Faith, Strength & Wisdom"""
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
    pdf.add_centered_text(700, "AMAZING WOMEN", font='F2', size=28, gray=0.1)
    pdf.add_centered_text(668, "OF THE BIBLE", font='F2', size=22, gray=0.15)
    pdf.add_centered_text(638, "10 Stories of Faith, Strength & Wisdom", font='F5', size=15, gray=0.2)
    illus_box(pdf, 370, "A beautiful montage of Bible women: Queen Esther in royal purple, Ruth gathering wheat in golden fields, Miriam dancing with a tambourine, Deborah in warrior armor, Mary holding baby Jesus, all radiating strength and grace. Warm golden background with decorative floral border.", 170)
    pdf.add_centered_text(330, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(300, "Inspiring Stories of Women Who Changed the World", font='F4', size=12, gray=0.4)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)

    # COPYRIGHT
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "AMAZING WOMEN OF THE BIBLE", font='F2', size=16, gray=0.1)
    pdf.add_line(72, 688, 400, 688, width=0.5, gray=0.5)
    pdf.add_text(72, 665, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 645, "Scripture from World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 50, gray=0.92)
    pdf.add_text(72, 130, "For every girl AND boy - these women inspire us all!", font='F5', size=11, gray=0.2)

    women = [
        {
            "title": "EVE", "subtitle": "The First Woman",
            "theme": "Courage to Start New",
            "illustration": "Eve in the Garden of Eden, a beautiful woman with long dark hair adorned with flowers, wearing a simple flowing dress made of leaves. She stands in awe among incredible plants - giant ferns, blooming roses, orchids. Animals surround her peacefully - a deer nuzzles her hand, birds perch on her shoulder. Garden of Eden in full glory with waterfall behind.",
            "story": "Eve was the first woman ever created - made by God Himself from Adam's rib. She was perfect, beautiful, and lived in Paradise! She walked with God in the cool of the day. Though Eve made a terrible mistake listening to the serpent, she also showed incredible courage afterward - facing a completely new world outside Eden, becoming the mother of all humanity, and learning to trust God even after failure.",
            "amazing": "Eve is amazing because she was the first to experience EVERYTHING - the first sunset, first laugh, first friendship. And even after her worst mistake, she didn't give up. She kept going and trusted God's promise of a future Savior.",
            "verse": "Adam named his wife Eve because she would be the mother of all the living. - Genesis 3:20 (WEB)",
            "be_like_her": "When you make a mistake, don't give up! Get back up, trust God's grace, and keep moving forward. Every new day is a fresh start!"
        },
        {
            "title": "SARAH", "subtitle": "Laughing at Impossible Promises",
            "theme": "Faith in Waiting",
            "illustration": "Elderly Sarah with silver hair and warm smile, holding baby Isaac in her arms inside a decorated tent. Her face shows pure joy and disbelief. Abraham stands beside her beaming with pride. The tent is luxurious with colorful woven tapestries. A cradle and baby items visible. Stars visible through the tent opening.",
            "story": "God promised Abraham and Sarah a baby. Simple, right? Except Sarah was 90 years old! When angels told Abraham the promise would finally come true, Sarah laughed behind the tent door - it seemed absolutely impossible! But God asked: 'Is anything too hard for the LORD?' And sure enough, baby Isaac was born. His name means 'laughter' because Sarah said: 'God has made me laugh; everyone who hears will laugh with me!'",
            "amazing": "Sarah is amazing because she waited 25 years for God's promise without giving up entirely. She reminds us that God's timing is perfect even when it feels impossibly slow. Her laughter of disbelief turned into laughter of pure joy!",
            "verse": "Is anything too hard for the LORD? - Genesis 18:14 (WEB)",
            "be_like_her": "When you're waiting for something and it feels like it will NEVER happen, remember Sarah. God keeps His promises - His timing is always perfect!"
        },

        {
            "title": "MIRIAM", "subtitle": "Dancing with Joy After Deliverance",
            "theme": "Worship & Celebration",
            "illustration": "Miriam, a joyful woman with flowing dark hair and colorful robes of blue and gold, dancing on the shore of the Red Sea with a tambourine raised high. Behind her, hundreds of women dance and celebrate. The parted Red Sea is visible in the background with water walls. Freedom and pure joy radiate from her expression.",
            "story": "Miriam watched over baby Moses in his basket on the Nile River when she was just a young girl - brave even as a child! Years later, when God parted the Red Sea and Israel walked to freedom, Miriam grabbed her tambourine and LED all the women in the greatest victory dance ever! She sang: 'Sing to the LORD for He has triumphed gloriously!' She was a prophet, a leader, and a worshiper.",
            "amazing": "Miriam is amazing because she was brave from childhood (protecting baby Moses) through adulthood (leading worship). She shows us that praising God with all our energy is the right response to His goodness!",
            "verse": "Miriam the prophetess took a tambourine in her hand, and all the women went out after her with tambourines and with dances. - Exodus 15:20 (WEB)",
            "be_like_her": "When God does something good in your life - CELEBRATE! Don't hold back your joy! Sing, dance, shout praise - worship God with all your heart!"
        },
        {
            "title": "DEBORAH", "subtitle": "The Warrior Judge",
            "theme": "Leadership",
            "illustration": "Deborah sitting under a large palm tree on a hill, dressed in strong yet elegant robes of deep red and gold. People line up for her wise judgment. Behind her, she rises to point toward battle - a female warrior leading troops. Her expression shows confidence and divine authority. Military tents and the army of Israel visible in the valley below.",
            "story": "In a time when Israel had no king, God raised up Deborah as judge over all the land! She sat under her palm tree and people came from everywhere for her wise decisions. When a cruel general named Sisera terrorized Israel, Deborah called the commander Barak and said: 'God commands you to fight!' Barak said: 'Only if you come with me!' So Deborah marched to war alongside 10,000 soldiers. Israel won a total victory!",
            "amazing": "Deborah is amazing because she was a prophet, judge, military leader, and poet - all in one! She didn't wait for someone else to lead. She stepped up with courage and wisdom when her nation needed her.",
            "verse": "The villagers ceased in Israel until I, Deborah, arose as a mother in Israel. - Judges 5:7 (WEB)",
            "be_like_her": "Don't wait for others to step up! If you see a need, be a leader. God gives both boys AND girls wisdom and courage to lead!"
        },
        {
            "title": "RUTH", "subtitle": "Loyalty That Changed History",
            "theme": "Devotion",
            "illustration": "Ruth kneeling to embrace her mother-in-law Naomi on a country road, both women wearing simple traveling clothes. Ruth's face shows fierce determination and love. In the background, the land of Moab fades behind and green Bethlehem beckons ahead. Wind blows their hair. A single shaft of golden sunlight illuminates the two women.",
            "story": "Ruth was from Moab - a foreigner to Israel. When her husband died, her mother-in-law Naomi said: 'Go home to your family.' But Ruth refused! She clung to Naomi and said the most beautiful loyalty pledge ever: 'Where you go, I will go. Your people will be my people. Your God will be my God.' In Bethlehem, Ruth worked humbly in the fields. Her loyalty was rewarded when she married Boaz - and became the great-grandmother of King David!",
            "amazing": "Ruth is amazing because she chose love over comfort, loyalty over convenience, and God over familiar gods. She's one of only five women named in Jesus' family tree!",
            "verse": "Where you go, I will go; your people will be my people, and your God, my God. - Ruth 1:16 (WEB)",
            "be_like_her": "Be loyal! Stick with people who need you. Don't choose the easy path - choose the loving path. God honors faithfulness!"
        },
        {
            "title": "HANNAH", "subtitle": "Prayer That Moved Heaven",
            "theme": "Persistence in Prayer",
            "illustration": "Hannah kneeling in the tabernacle, tears streaming down her face, hands raised in desperate prayer. Light streams through the tent fabric onto her. Her lips move silently. The altar and lampstand glow nearby. Her expression shows both agony and faith. After: Hannah joyfully presenting young Samuel to the priest Eli at the temple.",
            "story": "Hannah desperately wanted a child but couldn't have one. Year after year she wept and prayed. Her rival mocked her cruelly. But Hannah didn't stop praying! She poured her heart out to God so passionately that the priest thought she was drunk! She promised: 'If You give me a son, I'll give him back to serve You.' God heard her cry and gave her Samuel - who became one of Israel's greatest prophets! Hannah kept her promise and dedicated Samuel to God.",
            "amazing": "Hannah is amazing because she never stopped praying, never stopped believing, and when God answered, she kept her promise! Her prayer in 1 Samuel 2 is one of the most beautiful worship songs in the Bible.",
            "verse": "For this child I prayed, and the LORD has given me my petition. - 1 Samuel 1:27 (WEB)",
            "be_like_her": "Never give up praying! Even when it takes years, keep pouring your heart out to God. He hears every prayer!"
        },

        {
            "title": "ESTHER", "subtitle": "Beauty with Purpose",
            "theme": "Courage for Others",
            "illustration": "Queen Esther in her finest royal robes of deep purple and gold, crown sparkling on her head, walking bravely into the king's throne room. Her face shows calm determination despite fear. Persian palace with tall golden pillars, intricate mosaic floors, hanging gardens visible through windows. Guards stand at attention.",
            "story": "Esther was an orphan raised by her cousin Mordecai. Her beauty won the king's heart and she became queen - but she hid her Jewish identity. When wicked Haman plotted to destroy all Jews, Mordecai told Esther: 'Perhaps you became queen for such a time as this!' Going to the king uninvited meant risking death. Esther fasted three days, then bravely entered the throne room. The king extended mercy, and Esther exposed Haman's evil plot. She saved her entire nation!",
            "amazing": "Esther is amazing because she used her position not for personal luxury but to save others! She risked everything - even her life - for her people. True beauty is beauty with purpose!",
            "verse": "Who knows whether you haven't come to the kingdom for such a time as this? - Esther 4:14 (WEB)",
            "be_like_her": "Use whatever position God gives you to help others! Whether you're popular, talented, or in leadership - use it for good!"
        },
        {
            "title": "MARY", "subtitle": "Saying Yes to God",
            "theme": "Trust & Obedience",
            "illustration": "Young Mary, about 14-15 years old, kneeling in a simple room in Nazareth. Angel Gabriel stands before her in brilliant white light with golden wings spread. Mary's expression shows surprise turning to humble acceptance. Her hands are open in surrender. Simple pottery and woven items in her modest home. Divine light fills the room.",
            "story": "Mary was just a young teenager when the angel Gabriel appeared with the most incredible news: she would be the mother of God's Son! This was terrifying - she wasn't married, people wouldn't understand, her life would never be normal. But Mary's response was pure faith: 'I am the Lord's servant. Let it be as you have said.' She said YES to God's impossible plan without knowing how it would work out. And she became the mother of Jesus - the Savior of the world!",
            "amazing": "Mary is amazing because she trusted God completely at such a young age! She didn't understand everything but she said yes anyway. Her willingness changed the course of human history forever.",
            "verse": "Behold, the servant of the Lord; let it be done to me according to your word. - Luke 1:38 (WEB)",
            "be_like_her": "When God asks you to do something that seems impossible or scary, say YES! You don't need to understand everything - just trust Him!"
        },
        {
            "title": "MARTHA & MARY", "subtitle": "Two Ways to Love Jesus",
            "theme": "Balance",
            "illustration": "Inside a cozy home: Mary sitting at Jesus' feet on the floor, looking up with rapt attention, completely focused on His words. Meanwhile Martha rushes past with dishes, food, and a slightly frustrated expression. Jesus sits on a cushion teaching gently. The home is warm with oil lamps, bread baking, flowers on the table.",
            "story": "When Jesus visited their home, the two sisters showed love in totally different ways. Martha rushed around cooking and cleaning - showing love through SERVICE. Mary sat at Jesus' feet and listened - showing love through PRESENCE. Martha got frustrated: 'Jesus, tell Mary to help me!' But Jesus gently said: 'Martha, you're worried about many things. Mary has chosen what is better.' Both ways of loving are good, but spending time WITH Jesus comes first!",
            "amazing": "Martha and Mary together show us that serving God and spending time with God are BOTH important! Martha later showed incredible faith when Lazarus died. Both sisters were deeply loved by Jesus.",
            "verse": "Mary has chosen the good portion, which will not be taken away from her. - Luke 10:42 (WEB)",
            "be_like_her": "Don't get so busy DOING things for God that you forget to SIT with God! Both service and quiet time matter. Find your balance!"
        },
        {
            "title": "PRISCILLA", "subtitle": "Teaching God's Word",
            "theme": "Using Your Gifts",
            "illustration": "Priscilla and her husband Aquila sitting with the eloquent speaker Apollos in their tent-making workshop, scrolls spread on a wooden table. Priscilla points to a passage and explains it warmly. Leather and tentmaking tools visible in background. Oil lamp illuminates the scripture. All three show mutual respect and eagerness to learn.",
            "story": "Priscilla and her husband Aquila were tent-makers who also taught God's word! When they heard the brilliant preacher Apollos speak, they noticed he didn't know the full story about Jesus. Instead of embarrassing him publicly, they invited him to their home and taught him privately. Priscilla is always mentioned alongside her husband - an equal partner in ministry! Paul called them his 'fellow workers in Christ Jesus' who risked their lives for him.",
            "amazing": "Priscilla is amazing because she used her intelligence and knowledge to teach others - including famous preachers! She hosted churches in her home and risked her life for the gospel. She proves that women are meant to teach and lead!",
            "verse": "Greet Prisca and Aquila, my fellow workers in Christ Jesus, who risked their own necks for my life. - Romans 16:3-4 (WEB)",
            "be_like_her": "Use your gifts to teach and help others grow! You're never too young or too anything to share what God has taught you!"
        }
    ]


    # RENDER WOMEN STORIES
    gray_vals = [0.88, 0.92, 0.95, 0.90, 0.93, 0.88, 0.97, 0.91, 0.94, 0.89]
    
    for idx, w in enumerate(women):
        bg = gray_vals[idx % len(gray_vals)]
        
        # Page 1: Title + Illustration + Story
        pdf.new_page()
        pdf.add_filled_rect(0, 720, 612, 72, gray=bg)
        pdf.add_filled_rect(45, 725, 522, 60, gray=0.97)
        draw_border(pdf, 45, 725, 522, 60, gray=0.3)
        pdf.add_centered_text(762, f"Story {idx+1}: {w['subtitle']}", font='F4', size=10, gray=0.5)
        pdf.add_centered_text(742, w["title"], font='F2', size=22, gray=0.1)
        pdf.add_centered_text(727, w["theme"], font='F5', size=11, gray=0.3)
        
        illus_box(pdf, 545, w["illustration"], 145)
        
        pdf.add_filled_rect(50, 340, 512, 185, gray=0.97)
        pdf.add_rect(50, 340, 512, 185, line_width=0.5, gray=0.5)
        pdf.add_text(60, 510, "HER STORY:", font='F2', size=11, gray=0.2)
        wrap(pdf, 60, 490, w["story"], font='F4', size=11, mw=72)

        # Page 2: Amazing + Verse + Be Like Her + Prayer
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_text(60, 760, w["title"] + " - Why She Inspires Us", font='F2', size=13, gray=0.2)
        pdf.add_line(60, 752, 400, 752, width=0.5, gray=0.4)
        
        # She Was Amazing Because box
        pdf.add_filled_rect(50, 630, 512, 100, gray=bg)
        draw_border(pdf, 50, 630, 512, 100, gray=0.4)
        pdf.add_text(65, 715, "SHE WAS AMAZING BECAUSE...", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 695, w["amazing"], font='F5', size=11, mw=70)
        
        # Verse box
        pdf.add_filled_rect(50, 550, 512, 60, gray=0.92)
        pdf.add_text(65, 595, "KEY VERSE:", font='F2', size=11, gray=0.2)
        wrap(pdf, 65, 575, w["verse"], font='F3', size=9, mw=75)
        
        # I Can Be Like Her By
        pdf.add_filled_rect(50, 430, 512, 100, gray=0.95)
        pdf.add_rect(50, 430, 512, 100, line_width=1, gray=0.4)
        pdf.add_text(65, 515, "I CAN BE LIKE HER BY...", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 495, w["be_like_her"], font='F4', size=11, mw=70)
        
        # Prayer & writing space
        pdf.add_filled_rect(50, 310, 512, 100, gray=0.88)
        pdf.add_text(65, 395, "MY PRAYER:", font='F2', size=11, gray=0.1)
        pdf.add_text(65, 375, f"Dear God, help me be like {w['title'].title()} by...", font='F5', size=11, gray=0.3)
        for i in range(3):
            pdf.add_line(65, 345-(i*25), 545, 345-(i*25), width=0.5, gray=0.6)

    # FINAL PAGE - Role Model Reflection
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    pdf.add_filled_rect(40, 710, 532, 60, gray=0.88)
    draw_border(pdf, 40, 710, 532, 60, gray=0.3)
    pdf.add_centered_text(745, "MY ROLE MODEL REFLECTION", font='F2', size=18, gray=0.1)
    pdf.add_centered_text(718, "Which woman inspired you most?", font='F4', size=12, gray=0.3)
    
    pdf.add_text(60, 680, "The woman who inspired me most is:", font='F5', size=12, gray=0.2)
    pdf.add_line(60, 660, 550, 660, width=0.5, gray=0.6)
    pdf.add_text(60, 630, "She inspires me because:", font='F5', size=12, gray=0.2)
    for i in range(3):
        pdf.add_line(60, 605-(i*25), 550, 605-(i*25), width=0.5, gray=0.6)
    pdf.add_text(60, 510, "Three qualities I want to develop:", font='F5', size=12, gray=0.2)
    pdf.add_text(60, 485, "1.", font='F4', size=11, gray=0.3)
    pdf.add_line(80, 485, 550, 485, width=0.5, gray=0.6)
    pdf.add_text(60, 455, "2.", font='F4', size=11, gray=0.3)
    pdf.add_line(80, 455, 550, 455, width=0.5, gray=0.6)
    pdf.add_text(60, 425, "3.", font='F4', size=11, gray=0.3)
    pdf.add_line(80, 425, 550, 425, width=0.5, gray=0.6)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book280_Amazing_Women_Bible.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
