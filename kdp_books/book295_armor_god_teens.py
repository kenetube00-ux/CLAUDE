"""Book 295: SUIT UP - Armor of God Study Journal for Teens"""
import random
from pdf_utils import PDFDoc

random.seed(295)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    armor = [
        ("BELT OF TRUTH", "Ephesians 6:14a", "Stand therefore, having your loins girt about with truth.",
         ["In a world of fake filters and half-truths, truth is radical.",
          "Social media shows highlight reels. Truth shows the real you.",
          "God's truth isn't just facts - it's the foundation of identity."]),
        ("BREASTPLATE OF RIGHTEOUSNESS", "Ephesians 6:14b", "Having on the breastplate of righteousness.",
         ["Your heart is the most attacked part of your spiritual life.",
          "Every compromise chips away at your confidence before God.",
          "Righteousness isn't perfection - it's right standing with God."]),
        ("SHOES OF PEACE", "Ephesians 6:15", "Your feet shod with the preparation of the gospel of peace.",
         ["Peace isn't the absence of conflict. It's God's presence in the chaos.",
          "Anxiety is the enemy's favorite weapon against your generation.",
          "Standing firm in peace means not being shaken by circumstances."]),
        ("SHIELD OF FAITH", "Ephesians 6:16", "Taking the shield of faith to quench all the fiery darts.",
         ["The enemy's arrows come as thoughts: 'You're not enough. God's not real.'",
          "Faith doesn't mean no doubts. It means choosing trust over fear.",
          "Your shield gets stronger every time you use it."]),
        ("HELMET OF SALVATION", "Ephesians 6:17a", "And take the helmet of salvation.",
         ["Your mind is a battlefield. The helmet protects your thinking.",
          "Salvation isn't just about heaven - it's about NOW.",
          "When lies attack your identity, your salvation reminds you who you are."]),
        ("SWORD OF THE SPIRIT", "Ephesians 6:17b", "The sword of the Spirit, which is the word of God.",
         ["This is the only OFFENSIVE weapon. Everything else is defense.",
          "Jesus used Scripture to fight temptation in the wilderness.",
          "You need verses in your memory bank - not just your phone."]),
        ("PRAYER", "Ephesians 6:18", "Praying always with all prayer and supplication in the Spirit.",
         ["Prayer isn't a ritual - it's a relationship.",
          "You can pray while walking to class, before a test, in bed at night.",
          "The enemy hates prayer because it connects you to unlimited power."]),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.12)
    doc.add_rect(25, 25, 562, 742, 3, 0.6)
    for cx, cy in [(30, 735), (575, 735), (30, 30), (575, 30)]:
        doc.add_line(cx, cy, cx + (20 if cx < 300 else -20), cy, 2, 0.6)
        doc.add_line(cx, cy, cx, cy + (-20 if cy > 400 else 20), 2, 0.6)
    doc.add_centered_text(660, "SUIT UP", 'F2', 36, 0.9)
    doc.add_centered_text(610, "Armor of God Study Journal", 'F4', 18, 0.7)
    doc.add_centered_text(580, "for Teens", 'F4', 16, 0.6)
    doc.add_filled_rect(150, 320, 312, 180, 0.2)
    doc.add_rect(150, 320, 312, 180, 2, 0.6)
    doc.add_centered_text(450, "[ILLUSTRATION: modern shield and sword", 'F3', 9, 0.5)
    doc.add_centered_text(435, "with urban graffiti-style lettering]", 'F3', 9, 0.5)
    doc.add_centered_text(180, "7 Pieces. 7 Weeks. Total Transformation.", 'F2', 12, 0.7)
    doc.add_centered_text(100, author, 'F2', 16, 0.8)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "SUIT UP: Armor of God Study Journal for Teens", 'F2', 12, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    
    # Intro
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.15)
    doc.add_rect(40, 40, 532, 712, 2, 0.6)
    doc.add_centered_text(720, "WHY THIS MATTERS", 'F2', 18, 0.85)
    y = 685
    intro = [
        "You're in a war. Not one you can see, but one that's very real.",
        "",
        "The battlefield? Your mind. Your identity. Your faith.",
        "The weapons? Doubt, temptation, comparison, fear, lies.",
        "The enemy? He's subtle, strategic, and relentless.",
        "",
        "But here's the thing: God didn't leave you defenseless.",
        "",
        "In Ephesians 6, He lays out a full set of armor - not ancient",
        "relics, but living, active, supernatural protection for the",
        "spiritual attacks you face EVERY. SINGLE. DAY.",
        "",
        "This 7-week study goes DEEP into each piece:",
        "  - What it really means (not Sunday school answers)",
        "  - How it applies to YOUR life right now",
        "  - Modern scenarios you'll actually face",
        "  - Personal reflection and journaling",
        "  - Group discussion questions",
        "",
        "You can do this solo or with your youth group.",
        "Either way: it's time to suit up.",
    ]
    for line in intro:
        if line.startswith("You're") or line.startswith("But here") or line.startswith("Either"):
            doc.add_text(72, y, line, 'F2', 11, 0.85)
        else:
            doc.add_text(72, y, line, 'F1', 11, 0.7)
        y -= 18
    
    # 7 sections - each ~9 pages
    for idx, (title, ref, verse, deep_points) in enumerate(armor):
        # Section opener
        doc.new_page()
        fill = 0.13 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(30, 30, 552, 732, 3, 0.6)
        doc.add_centered_text(650, f"WEEK {idx+1}", 'F1', 16, 0.6)
        doc.add_centered_text(600, title, 'F2', 22, 0.9)
        doc.add_centered_text(560, ref, 'F4', 12, 0.6)
        doc.add_filled_rect(100, 320, 412, 140, 0.2)
        doc.add_rect(100, 320, 412, 140, 1, 0.5)
        doc.add_centered_text(420, f'"{verse}"', 'F4', 10, 0.7)
        doc.add_centered_text(200, "What the enemy DOESN'T want you to know:", 'F2', 11, 0.7)
        doc.add_centered_text(175, deep_points[0], 'F4', 10, 0.6)
        
        # Deep Dive page 1
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"WEEK {idx+1}: {title} - DEEP DIVE", 'F2', 13, 0.1)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        doc.add_text(72, y, "THE BIG IDEA:", 'F2', 12, 0.15)
        y -= 20
        for point in deep_points:
            doc.add_text(72, y, point, 'F4', 10, 0.25)
            y -= 18
        y -= 15
        doc.add_text(72, y, "SCRIPTURE STUDY:", 'F2', 12, 0.15)
        y -= 20
        doc.add_text(72, y, f"Read Ephesians 6:10-18 in full. Then focus on verse(s) about {title.lower()}.", 'F1', 10, 0.3)
        y -= 25
        doc.add_text(72, y, "What words stand out to you?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What does this armor piece PROTECT you from?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "When have you needed this armor piece and didn't use it?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Modern Scenario page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.92)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"WEEK {idx+1}: MODERN SCENARIO", 'F2', 13, 0.1)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        scenarios = {
            0: "Your ex posted a story with someone new. Your friends are screenshot-sharing. The urge to stalk, compare, and spiral is REAL.",
            1: "You gave in to temptation again last night. The guilt is crushing. You feel like a hypocrite going to youth group.",
            2: "Your anxiety is through the roof. College apps, friend drama, family stuff. You can't sleep and can't focus.",
            3: "You're sitting in biology class and the teacher just said something that made you doubt everything you believe.",
            4: "A voice in your head keeps saying: 'You're not really saved. If you were, you wouldn't struggle with this.'",
            5: "You know the Bible says one thing, but your entire friend group - even Christian ones - says something different.",
            6: "You used to pray all the time. Now it's been weeks. You feel disconnected from God. Prayer feels pointless.",
        }
        scenario = scenarios[idx]
        doc.add_text(72, y, "THE SITUATION:", 'F2', 11, 0.15)
        y -= 18
        words = scenario.split()
        cur = ""
        for w in words:
            if len(cur + " " + w) > 62:
                doc.add_text(72, y, cur, 'F4', 10, 0.25)
                y -= 15
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            doc.add_text(72, y, cur, 'F4', 10, 0.25)
            y -= 15
        
        y -= 20
        doc.add_text(72, y, f"How does the {title.lower()} apply here?", 'F2', 11, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What would you tell a friend in this situation?", 'F2', 11, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What verse could you use as a weapon here?", 'F2', 11, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Personal Journal page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.94)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"WEEK {idx+1}: MY JOURNAL", 'F2', 13, 0.1)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        doc.add_text(72, y, "Where am I MOST vulnerable without this armor piece?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What lies do I believe that this armor piece counters?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "My prayer to God about this:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(8):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Social Media page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.91)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"WEEK {idx+1}: DIGITAL BATTLEFIELD", 'F2', 13, 0.1)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        doc.add_text(72, y, "How does the enemy use TECHNOLOGY to attack this area?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What app/platform is the BIGGEST threat to this armor piece?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(2):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "One digital boundary I'll set this week:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "How I'll use technology FOR this armor piece:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Group discussion page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"WEEK {idx+1}: GROUP DISCUSSION", 'F2', 13, 0.1)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        questions = [
            f"1. In your own words, what does the {title.lower()} protect?",
            "2. Share a time you needed this armor and didn't use it.",
            "3. What's the hardest part about 'putting on' this piece daily?",
            "4. How can we help each other stay armored up?",
            "5. What's one thing you'll do differently this week?",
        ]
        for q in questions:
            doc.add_text(72, y, q, 'F1', 10, 0.25)
            y -= 18
            for _ in range(3):
                doc.add_line(90, y, 540, y, 0.5, 0.5)
                y -= 18
            y -= 10
        
        # Weekly challenge page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.15)
        doc.add_rect(40, 40, 532, 712, 2, 0.6)
        doc.add_text(55, 750, f"WEEK {idx+1}: CHALLENGE", 'F2', 14, 0.85)
        y = 710
        doc.add_text(72, y, "This week's challenge:", 'F2', 12, 0.8)
        y -= 25
        week_challenges = [
            "Speak ONLY truth for 7 days - no exaggeration, no lies, no half-truths.",
            "Confess one thing you've been hiding. Experience the freedom of clean armor.",
            "When anxiety hits, stop and pray for 60 seconds before reacting. Track it.",
            "Write down every doubt that hits you this week. Counter each with a verse.",
            "Memorize 3 verses about your identity in Christ. Recite them when lies come.",
            "Read one chapter of the Bible each day. Use a verse in real conversation.",
            "Pray for 5 minutes every morning before looking at your phone. All 7 days.",
        ]
        doc.add_text(72, y, week_challenges[idx], 'F4', 11, 0.7)
        y -= 40
        doc.add_text(72, y, "DAILY TRACKER:", 'F2', 12, 0.8)
        y -= 25
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            doc.add_text(72, y, f"[ ] {day}: ______________________________________", 'F1', 10, 0.6)
            y -= 22
        
        # Deeper theology page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"WEEK {idx+1}: GOING DEEPER", 'F2', 13, 0.1)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        doc.add_text(72, y, "WORD STUDY:", 'F2', 11, 0.15)
        y -= 18
        doc.add_text(72, y, f"Look up the original Greek/Hebrew word for '{title.split()[-1].lower()}'.", 'F1', 10, 0.25)
        y -= 18
        doc.add_text(72, y, "What extra meaning does it carry?", 'F1', 10, 0.25)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "CROSS REFERENCES (find 3 other verses about this topic):", 'F2', 10, 0.15)
        y -= 18
        for num in ["1.", "2.", "3."]:
            doc.add_text(72, y, f"{num} _________________________________________________", 'F1', 10, 0.3)
            y -= 22
        y -= 10
        doc.add_text(72, y, "HOW DID JESUS MODEL THIS ARMOR PIECE?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "MY PERSONAL BATTLE PLAN for using this armor:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Weekly reflection page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.94)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"WEEK {idx+1}: END-OF-WEEK REFLECTION", 'F2', 13, 0.1)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        doc.add_text(72, y, "What did God show me this week about this armor piece?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "Where did I succeed in using it?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "Where did I fail? (No shame - just awareness)", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "My prayer as I move to the next piece:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "Armor confidence level:  1  2  3  4  5  6  7  8  9  10", 'F1', 10, 0.3)
    
    # Final page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.12)
    doc.add_rect(40, 40, 532, 712, 2, 0.6)
    doc.add_centered_text(650, "FULLY ARMED.", 'F2', 28, 0.9)
    doc.add_centered_text(600, "7 weeks. 7 pieces. One unstoppable warrior.", 'F4', 13, 0.7)
    doc.add_centered_text(500, "\"Be strong in the Lord, and in the", 'F4', 14, 0.8)
    doc.add_centered_text(475, "power of his might.\"", 'F4', 14, 0.8)
    doc.add_centered_text(445, "- Ephesians 6:10", 'F1', 12, 0.6)
    doc.add_centered_text(350, "Now go live like the warrior God made you to be.", 'F2', 12, 0.8)
    
    # Extra journal pages
    extras_295 = ["MY BATTLE PLAN", "ARMOR CHECK-IN LOG", "VERSES FOR BATTLE",
                  "PRAYERS FOR SPIRITUAL WARFARE", "MY WARRIOR TESTIMONY"]
    for et in extras_295:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, et, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book295_Armor_God_Teens.pdf')
    print("Book295_Armor_God_Teens.pdf created successfully!")

if __name__ == "__main__":
    create_book()
