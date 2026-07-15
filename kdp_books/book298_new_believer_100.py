"""Book 298: FIRST 100 DAYS WITH JESUS - A Guided Journal for New Believers"""
import random
from pdf_utils import PDFDoc

random.seed(298)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    daily_verses = [
        "John 3:16 - For God so loved the world.",
        "Romans 10:9 - Confess with thy mouth the Lord Jesus.",
        "2 Corinthians 5:17 - If any man be in Christ, he is a new creature.",
        "Ephesians 2:8 - By grace are ye saved through faith.",
        "John 1:12 - As many as received him, to them gave he power.",
        "Romans 8:1 - No condemnation to them which are in Christ.",
        "1 John 1:9 - If we confess our sins, he is faithful to forgive.",
        "Philippians 1:6 - He which hath begun a good work will perform it.",
        "Psalm 119:105 - Thy word is a lamp unto my feet.",
        "Matthew 6:33 - Seek ye first the kingdom of God.",
        "Proverbs 3:5-6 - Trust in the Lord with all thine heart.",
        "Joshua 1:9 - Be strong and of a good courage.",
        "Isaiah 41:10 - Fear thou not; for I am with thee.",
        "Jeremiah 29:11 - I know the thoughts I think toward you.",
        "Psalm 23:1 - The Lord is my shepherd.",
        "Romans 8:28 - All things work together for good.",
        "Philippians 4:13 - I can do all things through Christ.",
        "Hebrews 13:5 - I will never leave thee nor forsake thee.",
        "1 Peter 5:7 - Casting all your care upon him.",
        "Matthew 11:28 - Come unto me all ye that labour.",
        "John 14:6 - I am the way, the truth, and the life.",
        "Galatians 5:22 - The fruit of the Spirit is love, joy, peace.",
        "Colossians 3:23 - Do it heartily, as to the Lord.",
        "James 1:5 - If any lack wisdom, let him ask of God.",
        "1 Thessalonians 5:17 - Pray without ceasing.",
        "Hebrews 11:1 - Faith is the substance of things hoped for.",
        "Romans 12:2 - Be not conformed to this world.",
        "Ephesians 6:11 - Put on the whole armour of God.",
        "Matthew 5:16 - Let your light so shine before men.",
        "John 15:5 - I am the vine, ye are the branches.",
        "Psalm 46:10 - Be still, and know that I am God.",
        "Isaiah 40:31 - They that wait upon the Lord renew their strength.",
        "Deuteronomy 31:6 - He will not fail thee nor forsake thee.",
        "Psalm 139:14 - I am fearfully and wonderfully made.",
        "Romans 5:8 - While we were yet sinners, Christ died for us.",
        "John 10:10 - I am come that they might have life.",
        "Matthew 28:20 - Lo, I am with you always.",
        "Psalm 34:8 - O taste and see that the Lord is good.",
        "1 John 4:4 - Greater is he that is in you.",
        "2 Timothy 1:7 - God hath not given us the spirit of fear.",
        "Psalm 37:4 - Delight thyself also in the Lord.",
        "Proverbs 16:3 - Commit thy works unto the Lord.",
        "Matthew 6:34 - Take no thought for the morrow.",
        "Psalm 100:5 - The Lord is good; his mercy is everlasting.",
        "John 8:32 - Ye shall know the truth, and it shall make you free.",
        "Ephesians 4:32 - Be ye kind one to another.",
        "Colossians 3:2 - Set your affection on things above.",
        "1 Corinthians 10:13 - God will make a way to escape temptation.",
        "Psalm 118:24 - This is the day the Lord hath made.",
        "Romans 15:13 - The God of hope fill you with joy and peace.",
        "Mark 12:30 - Love the Lord thy God with all thy heart.",
        "James 4:8 - Draw nigh to God, he will draw nigh to you.",
        "1 John 3:1 - Behold what manner of love the Father bestowed.",
        "Psalm 27:1 - The Lord is my light and my salvation.",
        "Matthew 7:7 - Ask, and it shall be given you.",
        "Romans 12:21 - Overcome evil with good.",
        "Hebrews 12:1 - Run with patience the race set before us.",
        "Psalm 55:22 - Cast thy burden upon the Lord.",
        "John 16:33 - In the world ye shall have tribulation.",
        "Philippians 4:6 - Be careful for nothing; in everything by prayer.",
        "Psalm 91:1 - He that dwelleth in the secret place.",
        "Isaiah 26:3 - Thou wilt keep him in perfect peace.",
        "Matthew 5:9 - Blessed are the peacemakers.",
        "1 Peter 2:9 - Ye are a chosen generation.",
        "Psalm 19:14 - Let the words of my mouth be acceptable.",
        "Galatians 2:20 - I live by the faith of the Son of God.",
        "Romans 6:23 - The gift of God is eternal life.",
        "Psalm 30:5 - Joy cometh in the morning.",
        "John 14:27 - Peace I leave with you.",
        "2 Corinthians 12:9 - My grace is sufficient for thee.",
        "Psalm 145:18 - The Lord is nigh unto all that call on him.",
        "Matthew 18:20 - Where two or three are gathered.",
        "James 1:12 - Blessed is the man that endureth temptation.",
        "Psalm 150:6 - Let every thing that hath breath praise the Lord.",
        "1 John 5:14 - If we ask according to his will, he heareth us.",
        "Proverbs 27:17 - Iron sharpeneth iron.",
        "Romans 1:16 - I am not ashamed of the gospel of Christ.",
        "Psalm 103:1 - Bless the Lord, O my soul.",
        "Matthew 22:37 - Thou shalt love the Lord with all thy heart.",
        "Ephesians 3:20 - Exceeding abundantly above all we ask or think.",
        "Psalm 121:1-2 - My help cometh from the Lord.",
        "1 Corinthians 16:13 - Watch ye, stand fast in the faith.",
        "John 13:34 - Love one another as I have loved you.",
        "Psalm 147:3 - He healeth the broken in heart.",
        "2 Timothy 2:15 - Study to shew thyself approved.",
        "Romans 8:38-39 - Nothing shall separate us from God's love.",
        "Psalm 46:1 - God is our refuge and strength.",
        "Mark 11:24 - Believe that ye receive, and ye shall have.",
        "1 Thessalonians 5:18 - In every thing give thanks.",
        "Psalm 62:1 - My soul waiteth upon God.",
        "Matthew 6:6 - Pray to thy Father which is in secret.",
        "Hebrews 4:16 - Come boldly unto the throne of grace.",
        "John 15:13 - Greater love hath no man than this.",
        "Psalm 73:26 - God is the strength of my heart.",
        "Philippians 2:3 - Let each esteem other better than themselves.",
        "Revelation 3:20 - Behold, I stand at the door, and knock.",
        "Psalm 51:10 - Create in me a clean heart, O God.",
        "Matthew 5:14 - Ye are the light of the world.",
        "James 4:7 - Resist the devil, and he will flee.",
        "Psalm 23:6 - Goodness and mercy shall follow me.",
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(30, 30, 552, 732, 3, 0.2)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_centered_text(680, "FIRST 100 DAYS", 'F2', 28, 0.1)
    doc.add_centered_text(645, "WITH JESUS", 'F2', 28, 0.1)
    doc.add_centered_text(600, "A Guided Journal for New Believers", 'F4', 16, 0.25)
    doc.add_filled_rect(150, 360, 312, 160, 0.90)
    doc.add_rect(150, 360, 312, 160, 2, 0.3)
    doc.add_centered_text(480, "[ILLUSTRATION: sunrise over open path", 'F3', 10, 0.4)
    doc.add_centered_text(465, "with cross silhouette and new dawn]", 'F3', 10, 0.4)
    doc.add_centered_text(220, "Your new life starts NOW.", 'F4', 14, 0.3)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "FIRST 100 DAYS WITH JESUS", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    
    # Intro pages (5 pages of basics)
    basics = [
        ("WHAT JUST HAPPENED?", [
            "You gave your life to Jesus. Here's what that means:",
            "",
            "1. Your sins are FORGIVEN - past, present, and future.",
            "   (1 John 1:9, Psalm 103:12)",
            "",
            "2. You are a NEW CREATION - the old you is gone.",
            "   (2 Corinthians 5:17)",
            "",
            "3. You are GOD'S CHILD - adopted into His family forever.",
            "   (John 1:12, Romans 8:15)",
            "",
            "4. The Holy Spirit LIVES IN YOU - God's presence is with you.",
            "   (1 Corinthians 6:19)",
            "",
            "5. Nothing can SEPARATE you from God's love now.",
            "   (Romans 8:38-39)",
            "",
            "This isn't about being perfect. It's about being HIS.",
            "And that happened the moment you said yes.",
        ]),
        ("HOW TO PRAY", [
            "Prayer is simply TALKING TO GOD. Here's how to start:",
            "",
            "1. Find a quiet spot (but anywhere works)",
            "2. Talk to God like He's right there (He is!)",
            "3. You can pray out loud or silently",
            "4. Be honest - God already knows everything",
            "",
            "A SIMPLE PRAYER PATTERN:",
            "  THANK - Thank God for something specific",
            "  SORRY - Confess anything weighing on you",
            "  PLEASE - Ask for what you need",
            "  OTHERS - Pray for people you love",
            "",
            "REMEMBER:",
            "  - There are no magic words",
            "  - You don't need to sound 'religious'",
            "  - Short prayers count",
            "  - Pray anytime, anywhere",
            "  - God LOVES hearing from you",
        ]),
        ("HOW TO READ THE BIBLE", [
            "The Bible is God's message to you. Start here:",
            "",
            "FOR BRAND NEW BELIEVERS, START WITH:",
            "  1. The Gospel of John (who Jesus is)",
            "  2. Psalms (prayers and praise)",
            "  3. Proverbs (daily wisdom)",
            "",
            "HOW TO READ:",
            "  1. Find a quiet time (morning is great)",
            "  2. Read a small section (even one chapter)",
            "  3. Ask: 'God, what are you saying to me?'",
            "  4. Write down what stands out",
            "  5. Try to apply ONE thing each day",
            "",
            "DON'T WORRY ABOUT:",
            "  - Reading the whole Bible immediately",
            "  - Understanding everything right away",
            "  - Difficult passages (skip and come back later)",
            "  - Reading fast (slow is better)",
        ]),
        ("WHAT IS CHURCH?", [
            "Church isn't a building - it's GOD'S FAMILY gathering.",
            "",
            "WHY GO TO CHURCH?",
            "  1. To worship God with other believers",
            "  2. To learn the Bible from a teacher",
            "  3. To find community and friendships",
            "  4. To serve others with your gifts",
            "  5. To be encouraged and encouraged others",
            "",
            "HOW TO FIND A GOOD CHURCH:",
            "  - They teach from the Bible",
            "  - They welcome newcomers warmly",
            "  - They encourage questions",
            "  - The people are real (not fake-perfect)",
            "  - You feel fed, not judged",
            "",
            "TIPS FOR YOUR FIRST VISIT:",
            "  - Come as you are (no dress code!)",
            "  - Arrive early to find your way around",
            "  - Don't worry about not knowing songs or rituals",
            "  - Introduce yourself to one person",
        ]),
        ("WHAT NOW?", [
            "Your first 100 days are about building FOUNDATIONS:",
            "",
            "THIS JOURNAL GIVES YOU:",
            "  - A daily verse to read and think about",
            "  - Space to process your new faith",
            "  - Prompts to help you talk to God",
            "  - A record of how God is working",
            "",
            "DAILY PRACTICE (just 10 minutes!):",
            "  1. Read today's verse",
            "  2. Write what it means for your new life",
            "  3. Write one question you have",
            "  4. Pray (even one sentence)",
            "",
            "MILESTONES TO LOOK FORWARD TO:",
            "  [ ] First time I pray out loud",
            "  [ ] First Bible book I finish",
            "  [ ] First time I share my faith",
            "  [ ] First answered prayer I notice",
            "  [ ] Finding a church home",
        ]),
    ]
    
    for title, content in basics:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.94)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, title, 'F2', 16, 0.1)
        doc.add_line(150, 725, 462, 725, 1, 0.3)
        y = 695
        for line in content:
            if line and (line[0].isdigit() or line.startswith("FOR") or line.startswith("HOW") or line.startswith("WHY") or line.startswith("REMEMBER") or line.startswith("DON'T") or line.startswith("TIPS") or line.startswith("THIS") or line.startswith("DAILY") or line.startswith("MILESTONES") or line.startswith("A SIMPLE")):
                doc.add_text(72, y, line, 'F2', 10, 0.15)
            else:
                doc.add_text(72, y, line, 'F1', 10, 0.25)
            y -= 17
    
    # 100 daily entries (each ~2/3 page - fitting about 1.5 entries per page for efficiency)
    # To reach 72+ pages we need about 67 pages for entries + 5 intro + bonus
    for day in range(1, 101):
        doc.new_page()
        fill = 0.93 + random.uniform(0, 0.04)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        
        # Header
        doc.add_filled_rect(40, 748, 532, 30, 0.88)
        doc.add_rect(40, 748, 532, 30, 1, 0.3)
        doc.add_text(55, 758, f"DAY {day}", 'F2', 12, 0.1)
        doc.add_text(200, 758, f"Date: ___/___/___", 'F1', 9, 0.3)
        
        # Verse
        verse = daily_verses[(day-1) % len(daily_verses)]
        doc.add_filled_rect(55, 705, 502, 30, 0.90)
        doc.add_rect(55, 705, 502, 30, 1, 0.4)
        doc.add_text(65, 715, f"Today's Verse: {verse}", 'F4', 9, 0.2)
        
        y = 685
        doc.add_text(72, y, "What this means for my new life:", 'F2', 10, 0.15)
        y -= 16
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        
        y -= 8
        doc.add_text(72, y, "One question I have:", 'F2', 10, 0.15)
        y -= 16
        for _ in range(2):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        
        y -= 8
        doc.add_text(72, y, "My prayer:", 'F2', 10, 0.15)
        y -= 16
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        
        y -= 8
        doc.add_text(72, y, "Something I noticed God doing today:", 'F2', 10, 0.15)
        y -= 16
        for _ in range(2):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        
        # Milestone markers at certain days
        if day in [7, 14, 30, 50, 75, 100]:
            y -= 10
            doc.add_filled_rect(55, y-40, 502, 50, 0.85)
            doc.add_rect(55, y-40, 502, 50, 2, 0.3)
            milestone_msg = {7: "1 WEEK! You showed up for 7 days!", 14: "2 WEEKS! Habits are forming!",
                          30: "1 MONTH! You're building a foundation!", 50: "HALFWAY! Look how far you've come!",
                          75: "75 DAYS! You're a prayer warrior!", 100: "100 DAYS! You did it!!!"}
            doc.add_centered_text(y-10, f"MILESTONE: {milestone_msg[day]}", 'F2', 11, 0.1)
    
    # Resources page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "NEXT STEPS", 'F2', 16, 0.1)
    y = 695
    next_steps = [
        "Congratulations on 100 days with Jesus!",
        "",
        "KEEP GROWING:",
        "  [ ] Find a Bible reading plan",
        "  [ ] Join a small group",
        "  [ ] Find a mentor or accountability partner",
        "  [ ] Get baptized (if you haven't yet)",
        "  [ ] Start serving at your church",
        "  [ ] Share your story with someone",
        "",
        "BOOKS TO READ NEXT:",
        "  - Mere Christianity by C.S. Lewis",
        "  - Knowing God by J.I. Packer",
        "  - The Purpose Driven Life by Rick Warren",
        "",
        "REMEMBER:",
        "  You don't have to figure it all out.",
        "  Just keep showing up. God does the rest.",
    ]
    for line in next_steps:
        if line.startswith("KEEP") or line.startswith("BOOKS") or line.startswith("REMEMBER") or line.startswith("Cong"):
            doc.add_text(72, y, line, 'F2', 11, 0.15)
        else:
            doc.add_text(72, y, line, 'F1', 11, 0.25)
        y -= 20
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book298_New_Believer_100_Days.pdf')
    print("Book298_New_Believer_100_Days.pdf created successfully!")

if __name__ == "__main__":
    create_book()
