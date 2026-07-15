"""Book 288: TALK TO GOD LIKE A MAN - A Prayer Journal for Teen Boys"""
import random
from pdf_utils import PDFDoc

random.seed(288)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    verses = [
        "Be strong and of a good courage. - Joshua 1:9",
        "I can do all things through Christ. - Philippians 4:13",
        "The Lord is my shepherd. - Psalm 23:1",
        "Trust in the Lord with all thine heart. - Proverbs 3:5",
        "Be not afraid, only believe. - Mark 5:36",
        "God is our refuge and strength. - Psalm 46:1",
        "The Lord is my light and my salvation. - Psalm 27:1",
        "For God hath not given us the spirit of fear. - 2 Timothy 1:7",
        "Wait on the Lord: be of good courage. - Psalm 27:14",
        "The Lord shall fight for you. - Exodus 14:14",
        "Greater is he that is in you. - 1 John 4:4",
        "Commit thy way unto the Lord. - Psalm 37:5",
        "He giveth power to the faint. - Isaiah 40:29",
        "The joy of the Lord is your strength. - Nehemiah 8:10",
        "Watch ye, stand fast in the faith. - 1 Corinthians 16:13",
        "Be ye doers of the word, not hearers only. - James 1:22",
        "Resist the devil, and he will flee. - James 4:7",
        "Love thy neighbour as thyself. - Mark 12:31",
        "Honour thy father and thy mother. - Exodus 20:12",
        "Set your affection on things above. - Colossians 3:2",
        "Let no man despise thy youth. - 1 Timothy 4:12",
        "Iron sharpeneth iron. - Proverbs 27:17",
        "He that walketh with wise men shall be wise. - Proverbs 13:20",
        "Create in me a clean heart, O God. - Psalm 51:10",
        "If any man be in Christ, he is a new creature. - 2 Corinthians 5:17",
        "Study to shew thyself approved. - 2 Timothy 2:15",
        "Flee also youthful lusts. - 2 Timothy 2:22",
        "Be not overcome of evil, but overcome evil with good. - Romans 12:21",
        "The Lord is good; his mercy is everlasting. - Psalm 100:5",
        "In all thy ways acknowledge him. - Proverbs 3:6",
        "For I know the plans I have for you. - Jeremiah 29:11",
        "Whatsoever ye do, do it heartily unto the Lord. - Colossians 3:23",
        "A soft answer turneth away wrath. - Proverbs 15:1",
        "He that is slow to anger is better than the mighty. - Proverbs 16:32",
        "Be still, and know that I am God. - Psalm 46:10",
        "Delight thyself also in the Lord. - Psalm 37:4",
        "As for me and my house, we will serve the Lord. - Joshua 24:15",
        "Seek ye first the kingdom of God. - Matthew 6:33",
        "The Lord is near to all who call on him. - Psalm 145:18",
        "No weapon formed against thee shall prosper. - Isaiah 54:17",
        "My grace is sufficient for thee. - 2 Corinthians 12:9",
        "Cast all your care upon him. - 1 Peter 5:7",
        "Blessed is the man that endureth temptation. - James 1:12",
        "Be ye kind one to another. - Ephesians 4:32",
        "Put on the whole armour of God. - Ephesians 6:11",
        "Let your light so shine before men. - Matthew 5:16",
        "The Lord is faithful; he will strengthen you. - 2 Thessalonians 3:3",
        "In quietness and confidence shall be your strength. - Isaiah 30:15",
        "Thou wilt keep him in perfect peace. - Isaiah 26:3",
        "Run with patience the race set before us. - Hebrews 12:1",
        "The battle is the Lord's. - 1 Samuel 17:47",
        "Blessed are the peacemakers. - Matthew 5:9",
        "Be strong in the Lord and the power of his might. - Ephesians 6:10",
        "Call unto me, and I will answer thee. - Jeremiah 33:3",
        "Fear not, for I am with thee. - Isaiah 41:10",
        "All things work together for good. - Romans 8:28",
        "I will never leave thee nor forsake thee. - Hebrews 13:5",
        "The Lord is gracious and full of compassion. - Psalm 145:8",
        "Be ye transformed by the renewing of your mind. - Romans 12:2",
        "Draw nigh to God, and he will draw nigh to you. - James 4:8",
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.15)
    doc.add_rect(30, 30, 552, 732, 3, 0.7)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_filled_rect(80, 500, 452, 180, 0.2)
    doc.add_rect(80, 500, 452, 180, 2, 0.7)
    doc.add_centered_text(645, "TALK TO GOD", 'F2', 30, 0.9)
    doc.add_centered_text(605, "LIKE A MAN", 'F2', 30, 0.9)
    doc.add_centered_text(560, "A Prayer Journal for Teen Boys", 'F4', 16, 0.7)
    doc.add_centered_text(530, "[ILLUSTRATION: shield and cross geometric design]", 'F3', 9, 0.5)
    doc.add_centered_text(200, "Real Talk. Real Faith. Real God.", 'F2', 14, 0.7)
    doc.add_centered_text(120, author, 'F2', 16, 0.8)
    
    # Copyright page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "TALK TO GOD LIKE A MAN", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    doc.add_text(72, 570, "For every young man finding his way to God.", 'F4', 11, 0.2)
    
    # Intro page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.18)
    doc.add_rect(40, 40, 532, 712, 2, 0.6)
    doc.add_centered_text(720, "BEFORE YOU START", 'F2', 18, 0.85)
    y = 680
    intro = [
        "Bro, let me be real with you.",
        "",
        "Prayer isn't about fancy words or religious language.",
        "It's about talking to God like He's right there - because He is.",
        "",
        "You don't have to clean up your language first.",
        "You don't have to have your life together.",
        "You don't have to sound like a pastor.",
        "",
        "Just show up. Be honest. That's it.",
        "",
        "This journal gives you 60 days of guided prayer.",
        "Each day has:",
        "  - A space to dump what's on your mind",
        "  - A place to tell God what you need",
        "  - A verse to carry through the day",
        "  - A spot to write your prayer (just talk)",
        "  - An evening check-in",
        "",
        "You can write one sentence or fill the whole page.",
        "God doesn't grade your prayers.",
        "",
        "Let's go.",
    ]
    for line in intro:
        if line.startswith("Bro") or line.startswith("Just show") or line.startswith("Let's"):
            doc.add_text(72, y, line, 'F2', 11, 0.85)
        else:
            doc.add_text(72, y, line, 'F1', 11, 0.7)
        y -= 18
    
    # How to use page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "HOW TO USE THIS JOURNAL", 'F2', 16, 0.1)
    doc.add_line(170, 715, 442, 715, 1, 0.3)
    y = 680
    how_to = [
        "1. Find 5-10 minutes. Morning, night, lunch - whenever.",
        "",
        "2. Read the verse at the top of the page.",
        "",
        "3. Write what's actually on your mind. No filter.",
        "",
        "4. Tell God where you need Him today. Be specific.",
        "",
        "5. Write your prayer. Talk to Him like a friend.",
        "",
        "6. At night, do the quick check-in.",
        "",
        "TIPS:",
        "- Don't overthink it",
        "- Messy handwriting is fine",
        "- Skip days if needed, just come back",
        "- Be brutally honest - God already knows anyway",
        "- This is between you and God. Nobody else reads this.",
    ]
    for line in how_to:
        if line.startswith("TIPS") or line[0:2].isdigit() if line else False:
            doc.add_text(72, y, line, 'F2', 11, 0.15)
        else:
            doc.add_text(72, y, line, 'F1', 11, 0.25)
        y -= 20
    
    # 60 daily journal pages
    for day in range(1, 61):
        doc.new_page()
        gray_bg = 0.92 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, gray_bg)
        # Bold geometric border
        doc.add_rect(25, 25, 562, 742, 2, 0.2)
        doc.add_line(25, 750, 587, 750, 3, 0.2)
        doc.add_line(25, 42, 587, 42, 3, 0.2)
        
        # Day header with dark fill
        doc.add_filled_rect(25, 750, 562, 30, 0.2)
        doc.add_text(35, 758, f"DAY {day}", 'F2', 14, 0.9)
        
        # Verse
        verse = verses[(day-1) % len(verses)]
        doc.add_filled_rect(50, 700, 512, 35, 0.88)
        doc.add_rect(50, 700, 512, 35, 1, 0.4)
        doc.add_text(60, 712, f"Today's verse: {verse}", 'F4', 9, 0.2)
        
        # Date line
        doc.add_text(72, 680, "Date: _____ / _____ / _____", 'F1', 10, 0.3)
        
        y = 650
        # What's on my mind
        doc.add_text(72, y, "WHAT'S ON MY MIND:", 'F2', 11, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 8
        # Where I need God
        doc.add_text(72, y, "WHERE I NEED GOD TODAY:", 'F2', 11, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 8
        # My prayer
        doc.add_text(72, y, "MY PRAYER (just talk to Him):", 'F2', 11, 0.15)
        y -= 18
        for _ in range(7):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 8
        # Evening check-in
        doc.add_filled_rect(50, y-60, 512, 70, 0.88)
        doc.add_rect(50, y-60, 512, 70, 1, 0.3)
        doc.add_text(65, y, "TONIGHT'S CHECK-IN:", 'F2', 10, 0.15)
        doc.add_text(65, y-18, "Did I see God today?  [ ] Yes  [ ] Not sure  [ ] Didn't look", 'F1', 9, 0.3)
        doc.add_text(65, y-36, "One word for today: _______________", 'F1', 9, 0.3)
    
    # Bonus: Prayers for tough situations (5 pages)
    tough_situations = [
        ("WHEN YOU'RE ANGRY", [
            "God, I'm so angry right now. I feel like punching something.",
            "Help me not destroy relationships or make things worse.",
            "Give me the strength to pause before I react.",
            "Show me what's really underneath this anger.",
            "I trust that You can handle my rage. Here it is.",
        ]),
        ("WHEN YOU'RE TEMPTED", [
            "God, I don't want to give in but I feel weak.",
            "Remind me who I am and whose I am.",
            "Give me an escape route right now.",
            "Replace this desire with something better.",
            "I choose You over this. Help my choice stick.",
        ]),
        ("WHEN YOU FEEL ALONE", [
            "God, I feel invisible. Like nobody sees me.",
            "Remind me that You're here even when I can't feel You.",
            "Bring one good friend into my life.",
            "Help me reach out instead of isolating.",
            "You said You'd never leave. I'm holding You to that.",
        ]),
        ("WHEN YOU'VE MESSED UP", [
            "God, I blew it. Again. I'm embarrassed and ashamed.",
            "But You already knew I'd fall. Help me get back up.",
            "Don't let guilt keep me from coming back to You.",
            "Help me make it right with the people I hurt.",
            "Thank You that Your mercy is new every morning.",
        ]),
        ("WHEN THE FUTURE SCARES YOU", [
            "God, I don't know what I'm doing with my life.",
            "Everyone seems to have a plan except me.",
            "Help me trust that You have a path even when I can't see it.",
            "Give me courage to take the next step.",
            "I don't need the whole map. Just the next turn.",
        ]),
    ]
    for title, prayers in tough_situations:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.2)
        doc.add_rect(40, 40, 532, 712, 2, 0.6)
        doc.add_centered_text(720, title, 'F2', 16, 0.85)
        doc.add_line(150, 715, 462, 715, 1, 0.6)
        y = 680
        doc.add_text(72, y, "A prayer you can pray:", 'F4', 12, 0.7)
        y -= 30
        for line in prayers:
            doc.add_text(72, y, line, 'F1', 11, 0.75)
            y -= 22
        y -= 30
        doc.add_text(72, y, "Write your own version:", 'F2', 12, 0.8)
        y -= 25
        for _ in range(10):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 20
    
    # Verses for real life (2 pages)
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "VERSES FOR REAL LIFE", 'F2', 16, 0.1)
    y = 695
    categories = [
        ("WHEN YOU'RE SCARED:", "Isaiah 41:10 - Fear not, for I am with thee"),
        ("WHEN YOU'RE SAD:", "Psalm 34:18 - The Lord is nigh unto them of a broken heart"),
        ("WHEN YOU'RE MAD:", "James 1:19 - Be slow to wrath"),
        ("WHEN TEMPTED:", "1 Corinthians 10:13 - God will make a way to escape"),
        ("WHEN LONELY:", "Deuteronomy 31:6 - He will not forsake thee"),
        ("WHEN CONFUSED:", "Proverbs 3:5-6 - Trust in the Lord with all thine heart"),
        ("WHEN FAILING:", "Proverbs 24:16 - A just man falleth and riseth up again"),
        ("ABOUT GIRLS:", "Proverbs 4:23 - Keep thy heart with all diligence"),
        ("ABOUT FRIENDS:", "Proverbs 27:17 - Iron sharpeneth iron"),
        ("ABOUT PURPOSE:", "Jeremiah 29:11 - I know the plans I have for you"),
    ]
    for cat, verse in categories:
        doc.add_text(72, y, cat, 'F2', 10, 0.15)
        doc.add_text(72, y-15, verse, 'F4', 10, 0.3)
        y -= 40
    
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "VERSES FOR REAL LIFE (continued)", 'F2', 16, 0.1)
    y = 695
    categories2 = [
        ("ABOUT PARENTS:", "Ephesians 6:1-2 - Honour thy father and mother"),
        ("ABOUT SCHOOL:", "Colossians 3:23 - Whatsoever ye do, do it heartily"),
        ("ABOUT SPORTS:", "1 Corinthians 9:24 - Run that ye may obtain"),
        ("ABOUT FUTURE:", "Matthew 6:34 - Take no thought for the morrow"),
        ("ABOUT IDENTITY:", "Psalm 139:14 - I am fearfully and wonderfully made"),
        ("ABOUT STRESS:", "Philippians 4:6 - Be anxious for nothing"),
        ("ABOUT MONEY:", "Matthew 6:33 - Seek ye first the kingdom of God"),
        ("ABOUT BULLYING:", "Romans 12:21 - Overcome evil with good"),
        ("ABOUT DEATH:", "John 11:25 - I am the resurrection and the life"),
        ("ABOUT DOUBT:", "Mark 9:24 - Lord, I believe; help thou mine unbelief"),
    ]
    for cat, verse in categories2:
        doc.add_text(72, y, cat, 'F2', 10, 0.15)
        doc.add_text(72, y-15, verse, 'F4', 10, 0.3)
        y -= 40
    
    # Faith milestones page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.18)
    doc.add_rect(40, 40, 532, 712, 2, 0.6)
    doc.add_centered_text(720, "MY FAITH MILESTONES", 'F2', 18, 0.85)
    y = 680
    milestones = [
        "Date I gave my life to Christ: _______________",
        "Date I was baptized: _______________",
        "First time I shared my faith: _______________",
        "First answered prayer I noticed: _______________",
        "A time God showed up big: _______________",
        "A verse that changed everything: _______________",
        "A person who shaped my faith: _______________",
        "My biggest faith lesson this year: _______________",
    ]
    for m in milestones:
        doc.add_text(72, y, m, 'F1', 11, 0.75)
        y -= 30
        doc.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 30
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book288_Teen_Boys_Prayer_Journal.pdf')
    print("Book288_Teen_Boys_Prayer_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
