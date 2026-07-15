"""Book 289: 30-DAY PRAYER CHALLENGE FOR TEEN GUYS - Level Up Your Faith"""
import random
from pdf_utils import PDFDoc

random.seed(289)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    days = [
        ("COURAGE", "When fear holds you back", "Joshua 1:9", "Have not I commanded thee? Be strong and of a good courage."),
        ("IDENTITY", "Who are you really?", "Psalm 139:14", "I am fearfully and wonderfully made."),
        ("TEMPTATION", "The pull you feel", "1 Corinthians 10:13", "God is faithful, who will not suffer you to be tempted above that ye are able."),
        ("ANGER", "When you want to explode", "Proverbs 16:32", "He that is slow to anger is better than the mighty."),
        ("GIRLS", "Keeping your heart right", "Proverbs 4:23", "Keep thy heart with all diligence; for out of it are the issues of life."),
        ("FRIENDS", "Choosing your crew", "Proverbs 13:20", "He that walketh with wise men shall be wise."),
        ("PARENTS", "Even when they don't get it", "Ephesians 6:2", "Honour thy father and mother; which is the first commandment with promise."),
        ("FUTURE", "When you have no clue", "Jeremiah 29:11", "For I know the thoughts that I think toward you, saith the Lord."),
        ("PURPOSE", "Why am I here?", "Ephesians 2:10", "For we are his workmanship, created unto good works."),
        ("SOCIAL MEDIA", "The comparison trap", "Galatians 1:10", "Do I now persuade men, or God? or do I seek to please men?"),
        ("SPORTS", "Competing God's way", "1 Corinthians 9:24", "Know ye not that they which run in a race run all?"),
        ("FAILURE", "When you blow it", "Proverbs 24:16", "For a just man falleth seven times, and riseth up again."),
        ("LONELINESS", "Feeling invisible", "Deuteronomy 31:6", "He will not fail thee, nor forsake thee."),
        ("PEER PRESSURE", "Standing alone", "Romans 12:2", "Be not conformed to this world: but be ye transformed."),
        ("PORNOGRAPHY", "Breaking free", "Psalm 101:3", "I will set no wicked thing before mine eyes."),
        ("GRADES", "When school is hard", "Colossians 3:23", "Whatsoever ye do, do it heartily, as to the Lord."),
        ("BULLYING", "Dealing with haters", "Romans 12:21", "Be not overcome of evil, but overcome evil with good."),
        ("ANXIETY", "When worry takes over", "Philippians 4:6", "Be careful for nothing; but in every thing by prayer."),
        ("FAITH DOUBTS", "Is this even real?", "Mark 9:24", "Lord, I believe; help thou mine unbelief."),
        ("MONEY", "What matters most", "Matthew 6:33", "Seek ye first the kingdom of God, and his righteousness."),
        ("LEADERSHIP", "Stepping up", "1 Timothy 4:12", "Let no man despise thy youth."),
        ("FORGIVENESS", "Letting go of grudges", "Ephesians 4:32", "Be ye kind one to another, forgiving one another."),
        ("INTEGRITY", "When no one's watching", "Proverbs 10:9", "He that walketh uprightly walketh surely."),
        ("GRIEF", "When someone dies", "Psalm 34:18", "The Lord is nigh unto them that are of a broken heart."),
        ("ADDICTION", "Anything controlling you", "John 8:36", "If the Son therefore shall make you free, ye shall be free indeed."),
        ("SERVING", "It's not about you", "Mark 10:45", "The Son of man came not to be ministered unto, but to minister."),
        ("WORSHIP", "More than music", "Romans 12:1", "Present your bodies a living sacrifice."),
        ("SHARING FAITH", "Telling others", "Matthew 5:16", "Let your light so shine before men."),
        ("GRATITUDE", "Counting what matters", "1 Thessalonians 5:18", "In every thing give thanks."),
        ("LEGACY", "What will you leave?", "Psalm 78:4", "We will not hide them from their children."),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.12)
    doc.add_rect(25, 25, 562, 742, 3, 0.6)
    # Geometric pattern - corner brackets
    for cx, cy in [(30, 735), (575, 735), (30, 30), (575, 30)]:
        doc.add_line(cx, cy, cx+20, cy, 2, 0.6)
        doc.add_line(cx, cy, cx, cy-20 if cy > 400 else cy+20, 2, 0.6)
    doc.add_centered_text(660, "30-DAY PRAYER", 'F2', 28, 0.9)
    doc.add_centered_text(620, "CHALLENGE", 'F2', 28, 0.9)
    doc.add_centered_text(575, "FOR TEEN GUYS", 'F2', 20, 0.7)
    doc.add_centered_text(530, "Level Up Your Faith", 'F4', 16, 0.6)
    doc.add_filled_rect(150, 300, 312, 150, 0.2)
    doc.add_rect(150, 300, 312, 150, 2, 0.6)
    doc.add_centered_text(400, "[ILLUSTRATION: modern cross with", 'F3', 9, 0.5)
    doc.add_centered_text(385, "geometric mountain and lightning bolt]", 'F3', 9, 0.5)
    doc.add_centered_text(150, "30 Days. 30 Themes. 1 God.", 'F2', 14, 0.7)
    doc.add_centered_text(100, author, 'F2', 16, 0.8)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "30-DAY PRAYER CHALLENGE FOR TEEN GUYS", 'F2', 13, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    
    # Intro page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.15)
    doc.add_rect(40, 40, 532, 712, 2, 0.6)
    doc.add_centered_text(720, "THE CHALLENGE", 'F2', 18, 0.85)
    y = 680
    intro_lines = [
        "Here's the deal: 30 days. 30 real-life topics.",
        "Each day tackles something you're actually dealing with.",
        "",
        "Every day gives you:",
        "  A STORY/SCENARIO - something you'll recognize",
        "  A VERSE - God's take on it",
        "  A GUIDED PRAYER - to get you started",
        "  A CHALLENGE - something to actually DO",
        "  JOURNAL SPACE - for your own words",
        "",
        "THE RULES:",
        "  1. Show up every day (even for 5 minutes)",
        "  2. Be completely honest",
        "  3. Actually do the challenge",
        "  4. No judgment - this is growth, not perfection",
        "",
        "Ready to level up? Let's go.",
    ]
    for line in intro_lines:
        if line.startswith("THE RULES") or line.startswith("Here's") or line.startswith("Ready"):
            doc.add_text(72, y, line, 'F2', 11, 0.85)
        else:
            doc.add_text(72, y, line, 'F1', 11, 0.7)
        y -= 20
    
    # Tracking chart page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "30-DAY TRACKING CHART", 'F2', 16, 0.1)
    doc.add_text(72, 700, "Check off each day as you complete it:", 'F1', 11, 0.3)
    y = 670
    for row in range(6):
        x = 72
        for col in range(5):
            day_num = row * 5 + col + 1
            if day_num <= 30:
                doc.add_rect(x, y, 90, 35, 1, 0.3)
                doc.add_text(x+5, y+20, f"Day {day_num}", 'F2', 9, 0.2)
                doc.add_text(x+5, y+5, f"[ ] Done", 'F1', 8, 0.4)
            x += 95
        y -= 45
    doc.add_text(72, y-20, "Start Date: ___________  End Date: ___________", 'F1', 11, 0.3)
    doc.add_text(72, y-50, "Accountability Partner: _______________", 'F1', 11, 0.3)
    
    # 30 days - each 2 pages
    for i, (theme, subtitle, ref, verse) in enumerate(days):
        # Page 1: Story + Verse + Guided Prayer
        doc.new_page()
        bg = 0.90 + random.uniform(0, 0.07)
        doc.add_filled_rect(0, 0, 612, 792, bg)
        doc.add_rect(25, 25, 562, 742, 2, 0.2)
        
        # Day header
        doc.add_filled_rect(25, 745, 562, 35, 0.2)
        doc.add_text(35, 755, f"DAY {i+1}: {theme}", 'F2', 14, 0.9)
        doc.add_text(400, 755, subtitle, 'F4', 10, 0.7)
        
        # Verse box
        doc.add_filled_rect(50, 690, 512, 40, 0.88)
        doc.add_rect(50, 690, 512, 40, 1, 0.3)
        doc.add_text(60, 710, ref, 'F2', 10, 0.1)
        doc.add_text(60, 695, f'"{verse}"', 'F4', 9, 0.2)
        
        # Scenario
        y = 665
        doc.add_text(72, y, "THE SCENARIO:", 'F2', 11, 0.15)
        y -= 18
        scenarios = {
            "COURAGE": "Your friend group is doing something you know is wrong. Everyone's looking at you.",
            "IDENTITY": "You scroll social media and everyone seems cooler, stronger, more popular than you.",
            "TEMPTATION": "It's late at night. You're alone. Your phone is right there. Nobody would know.",
            "ANGER": "Someone disrespected you in front of everyone. Your fists are clenched.",
            "GIRLS": "She's beautiful and she's interested. But you know where this is heading.",
            "FRIENDS": "Your best friend is changing. Making choices that pull you away from God.",
            "PARENTS": "They said no. Again. They don't understand your life AT ALL.",
            "FUTURE": "Everyone's asking what you want to be. You have absolutely no idea.",
            "PURPOSE": "What's the point? School, work, repeat. There has to be more than this.",
            "SOCIAL MEDIA": "His life looks perfect online. Yours feels like a mess in comparison.",
        }
        scenario = scenarios.get(theme, f"You're facing {theme.lower()} and don't know what to do.")
        words = scenario.split()
        line = ""
        for w in words:
            if len(line + " " + w) > 65:
                doc.add_text(72, y, line, 'F1', 10, 0.3)
                y -= 15
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            doc.add_text(72, y, line, 'F1', 10, 0.3)
            y -= 15
        
        y -= 15
        doc.add_text(72, y, "GUIDED PRAYER:", 'F2', 11, 0.15)
        y -= 18
        guided = f"God, today I'm dealing with {theme.lower()}. You see me right now."
        doc.add_text(72, y, guided, 'F4', 10, 0.25)
        y -= 15
        doc.add_text(72, y, f"Your Word says: {verse[:50]}...", 'F4', 10, 0.25)
        y -= 15
        doc.add_text(72, y, "Help me to trust You in this. I choose faith over fear.", 'F4', 10, 0.25)
        y -= 15
        doc.add_text(72, y, "Show me what to do. Give me strength. Amen.", 'F4', 10, 0.25)
        
        y -= 30
        doc.add_text(72, y, "TODAY'S CHALLENGE:", 'F2', 11, 0.15)
        y -= 18
        challenges = {
            "COURAGE": "Do one thing today that scares you (in a good way).",
            "IDENTITY": "Write 3 things God says about you. Read them out loud.",
            "TEMPTATION": "Delete one app or block one site that pulls you down.",
            "ANGER": "Next time you're angry, count to 10 and pray before responding.",
            "GIRLS": "Set one boundary for yourself today regarding girls.",
            "FRIENDS": "Text an encouraging message to one godly friend.",
            "PARENTS": "Thank your parent(s) for one specific thing today.",
            "FUTURE": "Write down 3 things you're good at. Ask God how to use them.",
            "PURPOSE": "Do one kind thing for someone today. Notice how it feels.",
            "SOCIAL MEDIA": "Go 4 hours without checking social media.",
        }
        challenge = challenges.get(theme, f"Apply today's theme ({theme.lower()}) in one specific action.")
        doc.add_text(72, y, challenge, 'F1', 10, 0.3)
        
        y -= 30
        doc.add_text(72, y, "MY RESPONSE:", 'F2', 11, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Page 2: Journal space
        doc.new_page()
        bg2 = 0.93 + random.uniform(0, 0.04)
        doc.add_filled_rect(0, 0, 612, 792, bg2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(50, 750, f"DAY {i+1} - CONTINUED", 'F2', 12, 0.15)
        doc.add_line(50, 745, 562, 745, 1, 0.3)
        
        y = 720
        doc.add_text(72, y, "MY PRAYER IN MY OWN WORDS:", 'F2', 11, 0.15)
        y -= 20
        for _ in range(10):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 20
        
        y -= 15
        doc.add_text(72, y, "DID I COMPLETE THE CHALLENGE?  [ ] Yes  [ ] No  [ ] Partial", 'F1', 10, 0.25)
        y -= 25
        doc.add_text(72, y, "What happened:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 15
        doc.add_filled_rect(50, y-70, 512, 80, 0.88)
        doc.add_rect(50, y-70, 512, 80, 1, 0.3)
        doc.add_text(65, y, "LEVEL CHECK:", 'F2', 10, 0.15)
        doc.add_text(65, y-18, "Faith level today:  1  2  3  4  5  6  7  8  9  10", 'F1', 9, 0.3)
        doc.add_text(65, y-36, "Prayer felt:  [ ] easy  [ ] hard  [ ] real  [ ] forced", 'F1', 9, 0.3)
        doc.add_text(65, y-54, "Tomorrow I want to: _______________________________", 'F1', 9, 0.3)
    
    # Extra journal pages
    extra_titles = [
        "THINGS I WANT TO TELL GOD",
        "PRAYERS I'M WAITING ON",
        "WHAT GOD IS TEACHING ME",
        "PEOPLE I'M PRAYING FOR",
        "MY FAITH GOALS",
        "VERSES I'M MEMORIZING",
        "QUESTIONS FOR GOD",
    ]
    for et in extra_titles:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, et, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22

    # Bonus page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.15)
    doc.add_rect(40, 40, 532, 712, 2, 0.6)
    doc.add_centered_text(720, "YOU DID IT.", 'F2', 24, 0.9)
    doc.add_centered_text(680, "30 days of showing up before God.", 'F4', 14, 0.7)
    y = 630
    closing = [
        "That takes guts. Most guys won't do this.",
        "",
        "Here's what you've built in 30 days:",
        "  - A habit of talking to God",
        "  - Honest self-awareness",
        "  - Scripture in your mind",
        "  - Courage to face real issues",
        "  - A foundation for lifelong faith",
        "",
        "Don't stop now. Keep the momentum.",
        "Start over from Day 1 or find a new challenge.",
        "",
        "God's not done with you. Not even close.",
        "",
        "\"Being confident of this very thing, that he which",
        "hath begun a good work in you will perform it.\"",
        "  - Philippians 1:6",
    ]
    for line in closing:
        if line.startswith("That takes") or line.startswith("Don't") or line.startswith("God's"):
            doc.add_text(72, y, line, 'F2', 11, 0.85)
        else:
            doc.add_text(72, y, line, 'F1', 11, 0.7)
        y -= 20
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book289_Teen_Boys_30Day.pdf')
    print("Book289_Teen_Boys_30Day.pdf created successfully!")

if __name__ == "__main__":
    create_book()
