"""Book 93: Psalms Bible Study for Women"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.1)
    pdf.add_centered_text(520, "PEACE IN THE STORM", 'F5', 30, 1)
    pdf.add_centered_text(475, "A Psalms Bible Study for Women", 'F4', 18, 0.9)
    pdf.add_centered_text(420, "10 Psalms of Comfort, Trust & Peace", 'F1', 13, 0.8)
    pdf.add_centered_text(395, "With Reflection Questions & Application", 'F1', 13, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    pdf.add_centered_text(170, "A Study of God's Faithfulness", 'F4', 11, 0.7)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "Peace in the Storm", 'F5', 14)
    pdf.add_centered_text(478, "A Psalms Bible Study for Women", 'F4', 11)
    pdf.add_centered_text(445, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(425, "Scripture quotations are from the public domain (KJV).", 'F1', 9)
    pdf.add_centered_text(395, "This study is designed for personal and group use.", 'F1', 9)
    pdf.add_centered_text(375, "May God's Word bring comfort to your heart.", 'F4', 10)


    # 10 Study Pages - Each Psalm
    psalms_data = [
        ("Psalm 23", "The Lord is My Shepherd",
         ["The Lord is my shepherd; I shall not want.",
          "He maketh me to lie down in green pastures:",
          "he leadeth me beside the still waters.",
          "He restoreth my soul: he leadeth me in the",
          "paths of righteousness for his name's sake.",
          "Yea, though I walk through the valley of the",
          "shadow of death, I will fear no evil: for thou",
          "art with me; thy rod and thy staff they comfort me."],
         "David is experiencing vulnerability, yet trusting God as provider and protector.",
         "God promises provision, rest, restoration, guidance, comfort, and eternal presence.",
         "When have you felt lost like a sheep without a shepherd?"),

        ("Psalm 46", "God is Our Refuge and Strength",
         ["God is our refuge and strength, a very present",
          "help in trouble. Therefore will not we fear,",
          "though the earth be removed, and though the",
          "mountains be carried into the midst of the sea.",
          "Be still, and know that I am God: I will be",
          "exalted among the heathen, I will be exalted",
          "in the earth. The Lord of hosts is with us;",
          "the God of Jacob is our refuge."],
         "David faces chaos and upheaval but finds stability in God alone.",
         "God promises to be a refuge, a present help, and commands us to be still and trust.",
         "When has your world felt like it was falling apart?"),

        ("Psalm 91", "Under His Wings",
         ["He that dwelleth in the secret place of the most",
          "High shall abide under the shadow of the Almighty.",
          "I will say of the Lord, He is my refuge and my",
          "fortress: my God; in him will I trust.",
          "He shall cover thee with his feathers, and under",
          "his wings shalt thou trust: his truth shall be",
          "thy shield and buckler. Thou shalt not be afraid",
          "for the terror by night; nor for the arrow by day."],
         "The psalmist seeks protection and finds complete safety in God's presence.",
         "God promises protection, deliverance, angelic guardianship, and answered prayer.",
         "Where do you run for safety when you feel afraid?"),

        ("Psalm 121", "My Help Comes from the Lord",
         ["I will lift up mine eyes unto the hills, from",
          "whence cometh my help. My help cometh from the",
          "Lord, which made heaven and earth. He will not",
          "suffer thy foot to be moved: he that keepeth",
          "thee will not slumber. The Lord is thy keeper:",
          "the Lord is thy shade upon thy right hand.",
          "The Lord shall preserve thee from all evil:",
          "he shall preserve thy soul."],
         "The psalmist looks beyond earthly help to the Creator who never sleeps.",
         "God promises constant watchfulness, preservation, and protection day and night.",
         "When have you felt like no one was watching over you?"),

        ("Psalm 139", "Fearfully and Wonderfully Made",
         ["O Lord, thou hast searched me, and known me.",
          "Thou knowest my downsitting and mine uprising,",
          "thou understandest my thought afar off.",
          "I will praise thee; for I am fearfully and",
          "wonderfully made: marvellous are thy works;",
          "and that my soul knoweth right well.",
          "How precious also are thy thoughts unto me,",
          "O God! how great is the sum of them!"],
         "David marvels that God knows him completely and still loves him deeply.",
         "God promises intimate knowledge of us, constant presence, and declares our worth.",
         "When have you struggled to believe you are wonderfully made?"),


        ("Psalm 27", "The Lord is My Light",
         ["The Lord is my light and my salvation; whom",
          "shall I fear? the Lord is the strength of my",
          "life; of whom shall I be afraid?",
          "Though an host should encamp against me, my",
          "heart shall not fear. One thing have I desired",
          "of the Lord, that will I seek after; that I",
          "may dwell in the house of the Lord all the",
          "days of my life, to behold the beauty of the Lord."],
         "David faces enemies and opposition but chooses confidence over fear.",
         "God promises to be light in darkness, salvation from fear, and beauty in worship.",
         "What is the one thing you desire most from God right now?"),

        ("Psalm 34", "The Lord Delivers",
         ["I sought the Lord, and he heard me, and",
          "delivered me from all my fears. They looked",
          "unto him, and were lightened: and their faces",
          "were not ashamed. This poor man cried, and the",
          "Lord heard him, and saved him out of all his",
          "troubles. The angel of the Lord encampeth round",
          "about them that fear him, and delivereth them.",
          "O taste and see that the Lord is good."],
         "David recalls being delivered from fear and invites others to experience God.",
         "God promises to hear our cries, deliver from fear, and be near the brokenhearted.",
         "When has God delivered you from something you feared?"),

        ("Psalm 37", "Trust and Do Not Fret",
         ["Fret not thyself because of evildoers, neither",
          "be thou envious against the workers of iniquity.",
          "Trust in the Lord, and do good; so shalt thou",
          "dwell in the land, and verily thou shalt be fed.",
          "Delight thyself also in the Lord: and he shall",
          "give thee the desires of thine heart. Commit",
          "thy way unto the Lord; trust also in him; and",
          "he shall bring it to pass."],
         "David addresses the frustration of watching evil prosper while the righteous struggle.",
         "God promises that trusting Him leads to provision, fulfilled desires, and justice.",
         "What situation makes you want to fret or compare yourself to others?"),

        ("Psalm 40", "He Lifted Me Out",
         ["I waited patiently for the Lord; and he",
          "inclined unto me, and heard my cry. He brought",
          "me up also out of an horrible pit, out of the",
          "miry clay, and set my feet upon a rock, and",
          "established my goings. And he hath put a new",
          "song in my mouth, even praise unto our God:",
          "many shall see it, and fear, and shall trust",
          "in the Lord. Blessed is that man that maketh the Lord his trust."],
         "David testifies of waiting, being rescued from despair, and receiving joy.",
         "God promises to hear patient waiting, rescue from despair, and give a new song.",
         "When have you been in a pit and felt God lifting you out?"),

        ("Psalm 103", "Bless the Lord, O My Soul",
         ["Bless the Lord, O my soul: and all that is",
          "within me, bless his holy name. Bless the Lord,",
          "O my soul, and forget not all his benefits:",
          "Who forgiveth all thine iniquities; who healeth",
          "all thy diseases; Who redeemeth thy life from",
          "destruction; who crowneth thee with",
          "lovingkindness and tender mercies; Who satisfieth",
          "thy mouth with good things."],
         "David commands his soul to remember God's benefits and not forget His goodness.",
         "God promises forgiveness, healing, redemption, love, mercy, and renewed strength.",
         "What benefits of God have you forgotten that you need to remember today?"),
    ]


    for idx, (ref, title, verses, experiencing, promises, personal_q) in enumerate(psalms_data):
        pdf.new_page()
        pdf.add_centered_text(750, f"STUDY {idx+1}: {ref.upper()}", 'F2', 16)
        pdf.add_centered_text(730, title, 'F4', 13)
        pdf.add_line(72, 720, 540, 720, 1, 0.3)

        # Scripture text
        y = 700
        pdf.add_text(72, y, "SCRIPTURE:", 'F2', 10)
        y -= 16
        for v in verses:
            pdf.add_text(90, y, v, 'F4', 10)
            y -= 14
        y -= 12

        # What is David experiencing?
        pdf.add_text(72, y, "What is David experiencing?", 'F2', 10)
        y -= 14
        pdf.add_text(90, y, experiencing, 'F4', 9)
        y -= 20

        # What does God promise?
        pdf.add_text(72, y, "What does God promise here?", 'F2', 10)
        y -= 14
        pdf.add_text(90, y, promises, 'F4', 9)
        y -= 20

        # Personal reflection
        pdf.add_text(72, y, "When have I felt this way?", 'F2', 10)
        y -= 14
        pdf.add_text(90, y, personal_q, 'F4', 9)
        y -= 14
        for i in range(3):
            pdf.add_line(90, y, 540, y, 0.5, 0.5)
            y -= 16

        # Application
        pdf.add_text(72, y, "Application to my life right now:", 'F2', 10)
        y -= 14
        for i in range(3):
            pdf.add_line(90, y, 540, y, 0.5, 0.5)
            y -= 16

        # Prayer response
        pdf.add_text(72, y, "My prayer response:", 'F2', 10)
        y -= 14
        for i in range(3):
            pdf.add_line(90, y, 540, y, 0.5, 0.5)
            y -= 16

        # Memory verse
        pdf.add_text(72, y, "Memory verse from this Psalm:", 'F2', 10)
        y -= 14
        pdf.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 20

        # Group discussion
        pdf.add_text(72, y, "Group Discussion Questions:", 'F2', 10)
        y -= 14
        pdf.add_text(90, y, "1. What stood out to you most in this Psalm?", 'F1', 9)
        y -= 13
        pdf.add_text(90, y, "2. How does this Psalm apply to a current struggle?", 'F1', 9)
        y -= 13
        pdf.add_text(90, y, "3. What character of God is revealed here?", 'F1', 9)
        y -= 18

        # Creative response
        pdf.add_text(72, y, "Creative Response (draw, write a poem, or journal freely):", 'F2', 10)
        y -= 14
        pdf.add_rect(72, y - 80, 468, 80, 0.5, 0.4)
        y -= 95

        # Week challenge
        pdf.add_text(72, y, "This Week's Challenge:", 'F2', 10)
        y -= 14
        pdf.add_line(90, y, 540, y, 0.5, 0.5)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book93_Psalms_Bible_Study_Women.pdf')
    print("Book93_Psalms_Bible_Study_Women.pdf created successfully!")

if __name__ == "__main__":
    create_book()
