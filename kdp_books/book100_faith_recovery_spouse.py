"""Book 100: Faith-Based Recovery Journal for Families of Addicts"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.1)
    pdf.add_centered_text(430, "HEALING TOGETHER", 'F5', 24, 1)
    pdf.add_centered_text(395, "A Faith-Based Journal for Families", 'F4', 13, 0.9)
    pdf.add_centered_text(375, "Affected by Addiction", 'F4', 13, 0.9)
    pdf.add_centered_text(330, "Boundaries | Surrender | Self-Care | Hope", 'F1', 10, 0.8)
    pdf.add_centered_text(150, author, 'F2', 12, 0.9)
    pdf.add_centered_text(125, "For those who love someone struggling with addiction", 'F4', 9, 0.7)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(430, "Healing Together", 'F5', 13)
    pdf.add_centered_text(410, "A Faith-Based Journal for Families Affected by Addiction", 'F4', 9)
    pdf.add_centered_text(380, f"Copyright 2024 {author}. All rights reserved.", 'F1', 9)
    pdf.add_centered_text(362, "No part of this book may be reproduced without permission.", 'F1', 8)
    pdf.add_centered_text(335, "This journal supports but does not replace professional help.", 'F1', 8)
    pdf.add_centered_text(315, "If you are in danger, call 911. SAMHSA helpline: 1-800-662-4357", 'F2', 8)
    pdf.add_centered_text(290, "You did not cause it. You cannot cure it. You cannot control it.", 'F4', 9)


    # 30 Scripture verses about surrender, trust, letting go
    verses = [
        "Trust in the Lord with all thine heart; and lean not unto thine own understanding. - Proverbs 3:5",
        "Cast thy burden upon the Lord, and he shall sustain thee. - Psalm 55:22",
        "Be still, and know that I am God. - Psalm 46:10",
        "Peace I leave with you, my peace I give unto you. Let not your heart be troubled. - John 14:27",
        "Come unto me, all ye that labour and are heavy laden, and I will give you rest. - Matthew 11:28",
        "The Lord is my strength and my shield; my heart trusted in him, and I am helped. - Psalm 28:7",
        "For God hath not given us the spirit of fear; but of power, and of love, and of a sound mind. - 2 Timothy 1:7",
        "And we know that all things work together for good to them that love God. - Romans 8:28",
        "I can do all things through Christ which strengtheneth me. - Philippians 4:13",
        "The Lord is nigh unto them that are of a broken heart. - Psalm 34:18",
        "He giveth power to the faint; and to them that have no might he increaseth strength. - Isaiah 40:29",
        "When thou passest through the waters, I will be with thee. - Isaiah 43:2",
        "Let go, and let God. Commit thy way unto the Lord; trust also in him. - Psalm 37:5",
        "My grace is sufficient for thee: for my strength is made perfect in weakness. - 2 Corinthians 12:9",
        "Fear thou not; for I am with thee: be not dismayed; for I am thy God. - Isaiah 41:10",
        "The Lord shall fight for you, and ye shall hold your peace. - Exodus 14:14",
        "Wait on the Lord: be of good courage, and he shall strengthen thine heart. - Psalm 27:14",
        "Casting all your care upon him; for he careth for you. - 1 Peter 5:7",
        "For I know the plans I have for you, declares the Lord, plans for good and not evil. - Jeremiah 29:11",
        "He restoreth my soul: he leadeth me in the paths of righteousness. - Psalm 23:3",
        "Create in me a clean heart, O God; and renew a right spirit within me. - Psalm 51:10",
        "Blessed is the man that trusteth in the Lord, and whose hope the Lord is. - Jeremiah 17:7",
        "Be anxious for nothing, but in everything by prayer let your requests be made known. - Philippians 4:6",
        "The Lord is good, a strong hold in the day of trouble. - Nahum 1:7",
        "Weeping may endure for a night, but joy cometh in the morning. - Psalm 30:5",
        "I will never leave thee, nor forsake thee. - Hebrews 13:5",
        "Be strong and of a good courage; be not afraid, for the Lord thy God is with thee. - Joshua 1:9",
        "He healeth the broken in heart, and bindeth up their wounds. - Psalm 147:3",
        "The righteous cry, and the Lord heareth, and delivereth them out of all their troubles. - Psalm 34:17",
        "Thou wilt keep him in perfect peace, whose mind is stayed on thee. - Isaiah 26:3",
    ]

    # 30 daily journal pages
    for day in range(1, 31):
        pdf.new_page()
        verse_idx = (day - 1) % 30
        pdf.add_centered_text(620, f"Day {day}", 'F2', 13)
        pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
        y = 595
        pdf.add_text(36, y, "Date: _______________", 'F1', 9)
        y -= 18
        pdf.add_text(36, y, "Today I choose:  [ ] Peace  [ ] Boundaries  [ ] Self-care", 'F2', 8)
        y -= 16

        # Scripture
        pdf.add_text(36, y, "Scripture:", 'F2', 8)
        y -= 12
        verse = verses[verse_idx]
        words = verse.split()
        line = ""
        for word in words:
            test = line + " " + word if line else word
            if len(test) * 5 > 340:
                pdf.add_text(42, y, line, 'F4', 7)
                y -= 10
                line = word
            else:
                line = test
        if line:
            pdf.add_text(42, y, line, 'F4', 7)
            y -= 13

        y -= 6
        pdf.add_text(36, y, "I release control over:", 'F2', 8)
        y -= 12
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14

        pdf.add_text(36, y, "Boundaries I maintained today:", 'F2', 8)
        y -= 12
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14

        pdf.add_text(36, y, "My feelings are valid:", 'F2', 8)
        y -= 12
        pdf.add_text(36, y, "1.__________ 2.__________ 3.__________", 'F1', 8)
        y -= 14

        pdf.add_text(36, y, "I took care of MYSELF by:", 'F2', 8)
        y -= 12
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14

        pdf.add_text(36, y, "I prayed for my loved one:", 'F2', 8)
        y -= 12
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14

        pdf.add_text(36, y, "Al-Anon/Nar-Anon principle I practiced:", 'F2', 8)
        y -= 12
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14

        pdf.add_text(36, y, "Gratitude:", 'F2', 8)
        y -= 12
        pdf.add_text(36, y, "1. ___________________________________", 'F1', 8)
        y -= 12
        pdf.add_text(36, y, "2. ___________________________________", 'F1', 8)


    # 5 Detachment with Love Exercises
    for ex in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(620, f"DETACHMENT WITH LOVE - Exercise {ex}", 'F2', 12)
        pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
        y = 590
        exercises = {
            1: [
                "WHAT IS DETACHMENT WITH LOVE?",
                "",
                "Detachment does NOT mean you stop loving them.",
                "It means you stop letting their addiction control YOUR life.",
                "",
                "Detachment IS:",
                "- Allowing them to face consequences of their choices",
                "- Not lying, covering up, or making excuses for them",
                "- Taking care of your own physical and mental health",
                "- Accepting you cannot fix, cure, or control their addiction",
                "- Trusting God with what you cannot control",
                "",
                "Detachment is NOT:",
                "- Stopping love or prayer",
                "- Cruelty or punishment",
                "- Giving up hope",
                "",
                "Where am I still trying to control their addiction?",
                "________________________________________________",
                "________________________________________________",
                "What would I do differently if I accepted I am powerless over this?",
                "________________________________________________",
            ],
            2: [
                "THE THREE C's MEDITATION:",
                "",
                "I did not CAUSE their addiction.",
                "(Repeat this until you believe it.)",
                "",
                "I cannot CURE their addiction.",
                "(No amount of love, nagging, or sacrifice will fix this.)",
                "",
                "I cannot CONTROL their addiction.",
                "(Only they can choose recovery.)",
                "",
                "What guilt am I carrying that isn't mine?",
                "________________________________________________",
                "________________________________________________",
                "",
                "What have I sacrificed trying to cure them?",
                "________________________________________________",
                "________________________________________________",
                "",
                "What am I trying to control right now?",
                "________________________________________________",
                "",
                "Lord, I surrender _____________________________ to You.",
            ],
            3: [
                "LETTING GO OF THE OUTCOME:",
                "",
                "You have prayed. You have tried. You have loved.",
                "Now: can you release the outcome to God?",
                "",
                "The outcome I am desperate for:",
                "________________________________________________",
                "",
                "What I'm afraid will happen if I let go:",
                "________________________________________________",
                "",
                "What is the COST of holding on so tightly?",
                "To my health: _________________________________",
                "To my peace: __________________________________",
                "To my other relationships: _______________________",
                "To my faith: __________________________________",
                "",
                "A prayer of surrender:",
                "'God, I place _____________ in Your hands today.",
                "I trust that You love them even more than I do.",
                "Give me the serenity to accept what I cannot change. Amen.'",
            ],
            4: [
                "BOUNDARIES ARE LOVE:",
                "",
                "A boundary is not a wall. It is a statement of what you will",
                "and will not accept. Boundaries protect you AND respect them",
                "by treating them as capable adults.",
                "",
                "Complete these sentences:",
                "",
                "I will no longer ____________________________________",
                "(enabling behavior I'm stopping)",
                "",
                "If ______________ happens, I will ____________________",
                "(consequence I will follow through on)",
                "",
                "I need ______________ in order to feel safe.",
                "",
                "I am allowed to ____________________________________",
                "(permission you need to give yourself)",
                "",
                "Keeping this boundary is an act of love because:",
                "________________________________________________",
                "________________________________________________",
            ],
            5: [
                "FINDING MYSELF AGAIN:",
                "",
                "Living with addiction often means losing yourself.",
                "Your entire world revolves around their crisis.",
                "Today, remember: YOU are a person too.",
                "",
                "Before addiction took over, I enjoyed:",
                "________________________________________________",
                "",
                "I used to dream about:",
                "________________________________________________",
                "",
                "People I've lost touch with:",
                "________________________________________________",
                "",
                "One thing I will do for MYSELF this week:",
                "________________________________________________",
                "",
                "I am more than their addiction. I am:",
                "________________________________________________",
                "________________________________________________",
                "",
                "'For I know the plans I have for you,' declares the Lord.",
                "Those plans include YOUR healing, not just theirs.",
            ],
        }
        for line in exercises[ex]:
            pdf.add_text(36, y, line, 'F4', 9)
            y -= 13


    # My Boundaries List page
    pdf.new_page()
    pdf.add_centered_text(620, "MY BOUNDARIES LIST", 'F2', 14)
    pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
    y = 590
    pdf.add_text(36, y, "These are my non-negotiable boundaries. I will enforce them with love.", 'F4', 9)
    y -= 18
    pdf.add_text(36, y, "I will NOT:", 'F2', 10)
    y -= 14
    for i in range(8):
        pdf.add_text(36, y, f"{i+1}.", 'F2', 9)
        pdf.add_line(55, y - 2, 396, y - 2, 0.5, 0.5)
        y -= 18
    y -= 10
    pdf.add_text(36, y, "I WILL:", 'F2', 10)
    y -= 14
    for i in range(8):
        pdf.add_text(36, y, f"{i+1}.", 'F2', 9)
        pdf.add_line(55, y - 2, 396, y - 2, 0.5, 0.5)
        y -= 18
    y -= 10
    pdf.add_text(36, y, "If my boundaries are violated, I will:", 'F2', 9)
    y -= 14
    for i in range(3):
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14

    # My Support Network page
    pdf.new_page()
    pdf.add_centered_text(620, "MY SUPPORT NETWORK", 'F2', 14)
    pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
    y = 590
    pdf.add_text(36, y, "You cannot do this alone. Fill in your support team:", 'F4', 9)
    y -= 22
    supports = [
        ("Al-Anon/Nar-Anon meeting:", "Day/Time: ____________ Location: ____________"),
        ("Sponsor/Mentor:", "Phone: _______________________________"),
        ("Therapist/Counselor:", "Phone: _______________________________"),
        ("Pastor/Faith leader:", "Phone: _______________________________"),
        ("Trusted friend #1:", "Phone: _______________________________"),
        ("Trusted friend #2:", "Phone: _______________________________"),
        ("Family member I can talk to:", "Phone: _______________________________"),
        ("Crisis line:", "SAMHSA: 1-800-662-4357"),
    ]
    for label, info in supports:
        pdf.add_text(36, y, label, 'F2', 9)
        y -= 14
        pdf.add_text(50, y, info, 'F1', 8)
        y -= 20
    y -= 10
    pdf.add_text(36, y, "I will reach out to someone when:", 'F2', 9)
    y -= 14
    for i in range(3):
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14

    # Letter to my addicted loved one
    pdf.new_page()
    pdf.add_centered_text(620, "LETTER TO MY ADDICTED LOVED ONE", 'F2', 12)
    pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
    y = 590
    pdf.add_text(36, y, "(You don't have to send this. This is for YOUR healing.)", 'F4', 9)
    y -= 20
    pdf.add_text(36, y, "Dear _______________,", 'F1', 10)
    y -= 18
    for i in range(28):
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 16

    # Letter to myself
    pdf.new_page()
    pdf.add_centered_text(620, "LETTER TO MYSELF", 'F2', 14)
    pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
    y = 590
    pdf.add_text(36, y, "(Write to yourself with the compassion you give everyone else.)", 'F4', 9)
    y -= 20
    pdf.add_text(36, y, "Dear Me,", 'F1', 10)
    y -= 18
    for i in range(28):
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 16

    # Self-Care Plan page
    pdf.new_page()
    pdf.add_centered_text(620, "MY SELF-CARE PLAN", 'F2', 14)
    pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
    y = 590
    pdf.add_text(36, y, "You MUST take care of yourself. This is not optional.", 'F2', 9)
    y -= 20
    categories = [
        ("Physical (body):", ["Sleep: ___hrs  Exercise: __________  Eating: __________"]),
        ("Emotional (heart):", ["Therapy: __________  Journaling: __________  Crying: OK"]),
        ("Social (connection):", ["Meeting: __________  Friend date: __________"]),
        ("Spiritual (soul):", ["Prayer: __________  Scripture: __________  Church: __________"]),
        ("Mental (mind):", ["Reading: __________  Hobby: __________  Limit news/social media"]),
    ]
    for cat, items in categories:
        pdf.add_text(36, y, cat, 'F2', 9)
        y -= 14
        for item in items:
            pdf.add_text(50, y, item, 'F1', 8)
            y -= 14
        y -= 8
    y -= 5
    pdf.add_text(36, y, "My daily non-negotiable self-care:", 'F2', 9)
    y -= 14
    for i in range(3):
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14
    y -= 5
    pdf.add_text(36, y, "Things that are NOT self-care (enabling disguised as caring):", 'F2', 9)
    y -= 14
    for i in range(3):
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14


    # When to Seek Help / Crisis Resources
    pdf.new_page()
    pdf.add_centered_text(620, "WHEN TO SEEK HELP / CRISIS RESOURCES", 'F2', 12)
    pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
    y = 590
    text = [
        "SEEK IMMEDIATE HELP IF:",
        "- You are in physical danger",
        "- Your loved one is threatening self-harm or harming others",
        "- Children are being neglected or abused",
        "- You are having thoughts of self-harm",
        "- Substances are in the home with children present",
        "",
        "CRISIS RESOURCES:",
        "- 911 (immediate danger)",
        "- SAMHSA Helpline: 1-800-662-4357 (free, 24/7)",
        "- 988 Suicide & Crisis Lifeline",
        "- National Domestic Violence: 1-800-799-7233",
        "- Al-Anon: al-anon.org / 1-888-425-2666",
        "- Nar-Anon: nar-anon.org",
        "",
        "YOU DESERVE HELP WHEN:",
        "- You feel hopeless or trapped",
        "- Your physical health is suffering",
        "- You are unable to function at work/school",
        "- Your other relationships are damaged",
        "- You have lost your sense of self",
        "- You are financially in crisis due to their addiction",
        "",
        "Remember: Getting help for YOURSELF is not giving up on them.",
        "It is the bravest, most loving thing you can do.",
    ]
    for line in text:
        pdf.add_text(36, y, line, 'F4', 9)
        y -= 14

    # Milestone Celebrations page
    pdf.new_page()
    pdf.add_centered_text(620, "MILESTONE CELEBRATIONS", 'F2', 14)
    pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
    y = 590
    pdf.add_text(36, y, "YOUR healing matters. Celebrate YOUR milestones:", 'F2', 9)
    y -= 22
    milestones = [
        ("30 DAYS of MY healing journey:", "Date achieved: __________"),
        ("", "How I'm different: ______________________________"),
        ("", "How I celebrated: _______________________________"),
        ("", ""),
        ("90 DAYS of MY healing journey:", "Date achieved: __________"),
        ("", "Boundaries I've held: ____________________________"),
        ("", "Self-care habits established: ______________________"),
        ("", ""),
        ("6 MONTHS of MY healing:", "Date achieved: __________"),
        ("", "Biggest change in me: ____________________________"),
        ("", "What I'm most proud of: __________________________"),
        ("", ""),
        ("1 YEAR of MY healing:", "Date achieved: __________"),
        ("", "Who I was then vs now: ___________________________"),
        ("", "_________________________________________________"),
        ("", "Message to someone just starting this journey:"),
        ("", "_________________________________________________"),
        ("", "_________________________________________________"),
    ]
    for label, content in milestones:
        if label:
            pdf.add_text(36, y, label, 'F2', 9)
            y -= 14
        pdf.add_text(36, y, content, 'F1', 8)
        y -= 14
    y -= 10
    pdf.add_text(36, y, "No matter what they choose, YOU are choosing life.", 'F5', 10)
    y -= 14
    pdf.add_text(36, y, "And that is enough.", 'F5', 10)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book100_Faith_Recovery_Family.pdf')
    print("Book100_Faith_Recovery_Family.pdf created successfully!")

if __name__ == "__main__":
    create_book()
