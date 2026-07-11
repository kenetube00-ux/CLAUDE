from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "COUNTING BLESSINGS"
subtitle = "A Christian Gratitude Journal with Daily Scripture"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, title, 'F2', 18)
pdf.add_centered_text(450, subtitle, 'F4', 12)
pdf.add_centered_text(350, "90 Days of Thanksgiving", 'F4', 11)
pdf.add_centered_text(335, "Guided by God's Word", 'F4', 11)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(520, title, 'F2', 12)
pdf.add_centered_text(490, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(470, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(440, "No part of this publication may be reproduced without permission.", 'F4', 8)

# Page 3: Why Gratitude Matters Biblically
pdf.new_page()
pdf.add_centered_text(610, "WHY GRATITUDE MATTERS BIBLICALLY", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
lines = [
    "Scripture is clear: gratitude is not optional for believers.",
    "It is a command, a practice, and a pathway to deeper faith.",
    "",
    "'Give thanks in all circumstances; for this is God's will",
    "for you in Christ Jesus.' - 1 Thessalonians 5:18",
    "",
    "'Enter his gates with thanksgiving and his courts with praise;",
    "give thanks to him and praise his name.' - Psalm 100:4",
    "",
    "WHY DAILY GRATITUDE TRANSFORMS YOUR FAITH:",
    "- It shifts focus from what's wrong to what God is doing",
    "- It builds trust that God is faithful and good",
    "- It combats anxiety and worry (Philippians 4:6-7)",
    "- It opens your eyes to blessings you've been missing",
    "- It creates a record of God's faithfulness to revisit",
    "",
    "HOW TO USE THIS JOURNAL:",
    "- Each day has a scripture verse to meditate on",
    "- Write 3 things you're grateful for (big or small)",
    "- Note how God showed up today (even in small ways)",
    "- Write a short prayer of thanksgiving",
    "- Don't skip days even when life is hard - especially then",
    "",
    "'Rejoice always, pray continually, give thanks in all",
    "circumstances.' - 1 Thessalonians 5:16-18",
]
for line in lines:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15


# 90 daily scripture verses (30 pages, 3 entries per page)
scriptures = [
    "Psalm 118:24 - This is the day the LORD has made; let us rejoice and be glad in it.",
    "James 1:17 - Every good and perfect gift is from above, coming down from the Father.",
    "Psalm 107:1 - Give thanks to the LORD, for he is good; his love endures forever.",
    "Colossians 3:17 - Whatever you do, in word or deed, do it all in the name of the Lord Jesus, giving thanks.",
    "Psalm 9:1 - I will give thanks to you, LORD, with all my heart; I will tell of your wonderful deeds.",
    "Philippians 4:6 - Do not be anxious, but in every situation, by prayer and petition, with thanksgiving, present your requests to God.",
    "Psalm 136:1 - Give thanks to the LORD, for he is good. His love endures forever.",
    "1 Chronicles 16:34 - Give thanks to the LORD, for he is good; his love endures forever.",
    "Psalm 103:2 - Praise the LORD, my soul, and forget not all his benefits.",
    "Ephesians 5:20 - Always giving thanks to God the Father for everything.",
    "Psalm 95:2 - Let us come before him with thanksgiving and extol him with music and song.",
    "Romans 8:28 - We know that in all things God works for the good of those who love him.",
    "Psalm 28:7 - The LORD is my strength and my shield; my heart trusts in him, and he helps me.",
    "2 Corinthians 9:15 - Thanks be to God for his indescribable gift!",
    "Psalm 34:8 - Taste and see that the LORD is good; blessed is the one who takes refuge in him.",
    "1 Thessalonians 5:18 - Give thanks in all circumstances; for this is God's will for you.",
    "Psalm 23:1 - The LORD is my shepherd, I lack nothing.",
    "Lamentations 3:22-23 - His mercies are new every morning; great is your faithfulness.",
    "Psalm 46:1 - God is our refuge and strength, an ever-present help in trouble.",
    "Matthew 6:33 - Seek first his kingdom and his righteousness, and all these things will be given.",
    "Psalm 16:11 - You make known to me the path of life; you will fill me with joy in your presence.",
    "Jeremiah 29:11 - I know the plans I have for you, declares the LORD, plans to prosper you.",
    "Psalm 37:4 - Take delight in the LORD, and he will give you the desires of your heart.",
    "Isaiah 41:10 - Do not fear, for I am with you; do not be dismayed, for I am your God.",
    "Psalm 139:14 - I praise you because I am fearfully and wonderfully made.",
    "Proverbs 3:5-6 - Trust in the LORD with all your heart and lean not on your own understanding.",
    "Psalm 27:1 - The LORD is my light and my salvation; whom shall I fear?",
    "John 3:16 - For God so loved the world that he gave his one and only Son.",
    "Psalm 145:9 - The LORD is good to all; he has compassion on all he has made.",
    "Romans 15:13 - May the God of hope fill you with all joy and peace as you trust in him.",
    "Psalm 63:3 - Because your love is better than life, my lips will glorify you.",
    "Matthew 11:28 - Come to me, all you who are weary, and I will give you rest.",
    "Psalm 91:1 - Whoever dwells in the shelter of the Most High will rest in his shadow.",
    "Philippians 4:13 - I can do all things through Christ who strengthens me.",
    "Psalm 121:1-2 - My help comes from the LORD, the Maker of heaven and earth.",
    "Isaiah 40:31 - Those who hope in the LORD will renew their strength.",
    "Psalm 30:5 - Weeping may stay for the night, but rejoicing comes in the morning.",
    "2 Timothy 1:7 - God has not given us a spirit of fear, but of power, love, and a sound mind.",
    "Psalm 119:105 - Your word is a lamp for my feet, a light on my path.",
    "Romans 8:38-39 - Nothing can separate us from the love of God in Christ Jesus.",
    "Psalm 147:3 - He heals the brokenhearted and binds up their wounds.",
    "Joshua 1:9 - Be strong and courageous. The LORD your God is with you wherever you go.",
    "Psalm 73:26 - My flesh and heart may fail, but God is the strength of my heart forever.",
    "Hebrews 13:8 - Jesus Christ is the same yesterday and today and forever.",
    "Psalm 46:10 - Be still, and know that I am God.",
    "Matthew 7:7 - Ask and it will be given to you; seek and you will find.",
    "Psalm 55:22 - Cast your cares on the LORD and he will sustain you.",
    "1 Peter 5:7 - Cast all your anxiety on him because he cares for you.",
    "Psalm 100:4 - Enter his gates with thanksgiving and his courts with praise.",
    "Deuteronomy 31:6 - Be strong and courageous. The LORD goes with you; he will never leave you.",
    "Psalm 40:5 - Many, LORD my God, are the wonders you have done.",
    "John 14:27 - Peace I leave with you; my peace I give you.",
    "Psalm 86:15 - You, Lord, are compassionate and gracious, slow to anger, abounding in love.",
    "Galatians 5:22-23 - The fruit of the Spirit is love, joy, peace, patience, kindness.",
    "Psalm 62:1 - Truly my soul finds rest in God; my salvation comes from him.",
    "Isaiah 26:3 - You will keep in perfect peace those whose minds are steadfast.",
    "Psalm 19:1 - The heavens declare the glory of God; the skies proclaim his handiwork.",
    "Nahum 1:7 - The LORD is good, a refuge in times of trouble.",
    "Psalm 33:5 - The earth is full of his unfailing love.",
    "Hebrews 12:2 - Let us fix our eyes on Jesus, the author and perfecter of our faith.",
    "Psalm 150:6 - Let everything that has breath praise the LORD.",
    "Zephaniah 3:17 - The LORD your God is with you, the Mighty Warrior who saves.",
    "Psalm 113:3 - From the rising of the sun to the place where it sets, praise the LORD.",
    "Colossians 3:15 - Let the peace of Christ rule in your hearts, and be thankful.",
    "Psalm 84:11 - The LORD bestows favor and honor; no good thing does he withhold.",
    "John 10:10 - I have come that they may have life, and have it to the full.",
    "Psalm 18:2 - The LORD is my rock, my fortress and my deliverer.",
    "2 Corinthians 12:9 - My grace is sufficient for you, my power is made perfect in weakness.",
    "Psalm 31:24 - Be strong and take heart, all you who hope in the LORD.",
    "Proverbs 16:9 - In their hearts humans plan their course, but the LORD establishes their steps.",
    "Psalm 126:3 - The LORD has done great things for us, and we are filled with joy.",
    "Matthew 5:16 - Let your light shine before others, that they may see your good deeds.",
    "Psalm 65:11 - You crown the year with your bounty, and your carts overflow with abundance.",
    "1 John 4:19 - We love because he first loved us.",
    "Psalm 138:8 - The LORD will vindicate me; your love endures forever.",
    "Romans 12:12 - Be joyful in hope, patient in affliction, faithful in prayer.",
    "Psalm 8:1 - LORD, our Lord, how majestic is your name in all the earth!",
    "Habakkuk 3:18 - Yet I will rejoice in the LORD, I will be joyful in God my Savior.",
    "Psalm 92:1 - It is good to praise the LORD and make music to your name.",
    "Ephesians 3:20 - God is able to do immeasurably more than all we ask or imagine.",
    "Psalm 96:1 - Sing to the LORD a new song; sing to the LORD, all the earth.",
    "1 Corinthians 15:57 - Thanks be to God who gives us the victory through our Lord Jesus.",
    "Psalm 104:24 - How many are your works, LORD! In wisdom you made them all.",
    "Isaiah 12:4 - Give praise to the LORD, proclaim his name; make known his deeds.",
    "Psalm 111:1 - Praise the LORD. I will extol the LORD with all my heart.",
    "Revelation 7:12 - Blessing and glory and wisdom and thanksgiving be to our God forever.",
    "Psalm 145:3 - Great is the LORD and most worthy of praise; his greatness no one can fathom.",
    "Philippians 1:6 - He who began a good work in you will carry it on to completion.",
    "Psalm 98:1 - Sing to the LORD a new song, for he has done marvelous things.",
    "1 Thessalonians 5:16-18 - Rejoice always, pray continually, give thanks in all circumstances.",
]

# 30 pages with 3 entries each
for page in range(30):
    pdf.new_page()
    y = 615
    for entry in range(3):
        day_num = page * 3 + entry + 1
        if day_num > 90:
            break
        scripture = scriptures[day_num - 1] if day_num <= len(scriptures) else "Psalm 136:1 - Give thanks to the LORD, for he is good."
        pdf.add_text(40, y, f"Day {day_num}  Date: ___/___/___", 'F2', 9)
        y -= 13
        # Truncate scripture to fit
        if len(scripture) > 70:
            pdf.add_text(40, y, scripture[:70], 'F5', 8)
            y -= 11
            pdf.add_text(40, y, scripture[70:], 'F5', 8)
        else:
            pdf.add_text(40, y, scripture, 'F5', 8)
        y -= 13
        pdf.add_text(40, y, "3 things I'm grateful for:", 'F4', 8)
        y -= 11
        pdf.add_text(40, y, "1. _____________________________________________", 'F1', 8)
        y -= 11
        pdf.add_text(40, y, "2. _____________________________________________", 'F1', 8)
        y -= 11
        pdf.add_text(40, y, "3. _____________________________________________", 'F1', 8)
        y -= 13
        pdf.add_text(40, y, "How God showed up today: _________________________", 'F1', 8)
        y -= 11
        pdf.add_text(40, y, "___________________________________________________", 'F1', 8)
        y -= 13
        pdf.add_text(40, y, "Prayer of thanksgiving: ____________________________", 'F1', 8)
        y -= 11
        pdf.add_text(40, y, "___________________________________________________", 'F1', 8)
        y -= 16
        pdf.add_line(40, y+8, 392, y+8, 0.3, 0.7)
        y -= 8


# Monthly Reflection Pages (3 pages)
for month in range(1, 4):
    pdf.new_page()
    pdf.add_centered_text(610, f"MONTHLY REFLECTION - MONTH {month}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 578
    reflection = [
        "What themes am I seeing in my gratitude?",
        "___________________________________________________",
        "___________________________________________________",
        "___________________________________________________",
        "",
        "How has daily gratitude changed my perspective?",
        "___________________________________________________",
        "___________________________________________________",
        "",
        "Where have I seen God most clearly this month?",
        "___________________________________________________",
        "___________________________________________________",
        "",
        "What prayers has God answered (even unexpectedly)?",
        "___________________________________________________",
        "___________________________________________________",
        "",
        "What am I still waiting on God for?",
        "___________________________________________________",
        "",
        "How has my faith grown through this practice?",
        "___________________________________________________",
        "___________________________________________________",
        "",
        "A verse that meant the most to me this month:",
        "___________________________________________________",
        "",
        "My prayer for next month:",
        "___________________________________________________",
        "___________________________________________________",
    ]
    for line in reflection:
        pdf.add_text(40, y, line, 'F4', 9.5)
        y -= 14

# 30-Day Gratitude Challenge List
pdf.new_page()
pdf.add_centered_text(610, "30-DAY GRATITUDE CHALLENGE", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Complete one challenge each day for a deeper gratitude practice:", 'F4', 9.5)
y -= 18
challenges = [
    "1. Thank God for 5 people in your life by name",
    "2. Write a thank-you note to someone who helped you",
    "3. Thank God for something you normally take for granted",
    "4. Give a genuine compliment to 3 people today",
    "5. Thank God for a trial that grew your faith",
    "6. Take a gratitude walk - notice beauty around you",
    "7. Text someone to tell them why you appreciate them",
    "8. Thank God for your body and what it can do",
    "9. Give something away to someone who needs it",
    "10. Thank God for answered prayers (list 3)",
    "11. Thank a service worker today (genuinely)",
    "12. Thank God for the Bible and a specific passage",
    "13. Pay for someone's coffee or meal anonymously",
    "14. Thank God for your church community by name",
    "15. Write down 10 simple pleasures you enjoy",
    "16. Thank someone who has prayed for you",
    "17. Thank God for a lesson learned from failure",
    "18. Leave an encouraging note for someone to find",
    "19. Thank God for nature - spend time outside",
    "20. Donate to a cause you're grateful exists",
    "21. Thank God for your home and name specific things",
    "22. Call a family member just to say you love them",
    "23. Thank God for music - worship with intention",
    "24. Share a testimony of God's faithfulness",
    "25. Thank God for seasons of waiting (they built faith)",
    "26. Write a psalm of thanksgiving in your own words",
    "27. Thank God for eternal life and salvation",
    "28. Do an act of service without being asked",
    "29. Thank God for second chances and grace",
    "30. Share this gratitude practice with someone else",
]
for c in challenges:
    pdf.add_text(40, y, c, 'F4', 8.5)
    y -= 14

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book163_Christian_Gratitude_Journal.pdf')
print("Book163_Christian_Gratitude_Journal.pdf created successfully!")
