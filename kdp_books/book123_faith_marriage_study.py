from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "BUILT TO LAST"
subtitle = "A Biblical Marriage Study for Couples"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 22)
pdf.add_centered_text(510, subtitle, 'F4', 14)
pdf.add_centered_text(440, "12 Weeks of Scripture, Discussion, and Growth", 'F4', 12)
pdf.add_centered_text(420, "for Husbands and Wives Together", 'F4', 12)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, f"{title} - {subtitle}", 'F2', 11)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "Scripture quotations are from the public domain (KJV).", 'F4', 9)
pdf.add_centered_text(490, "No part of this publication may be reproduced without permission.", 'F4', 9)

# 12 Weekly Studies (2 pages each = 24 pages)
weeks = [
    {
        "title": "THE FOUNDATION - What God Intended for Marriage",
        "scripture": "Genesis 2:18-25",
        "passage": [
            "'And the Lord God said, It is not good that the man should be alone;",
            "I will make him an help meet for him... Therefore shall a man leave his",
            "father and his mother, and shall cleave unto his wife: and they shall",
            "be one flesh.' - Genesis 2:18, 24 (KJV)"
        ],
        "discuss": [
            "What does 'leave and cleave' mean practically for us today?",
            "How do we maintain 'one flesh' unity when life gets busy?",
            "What outside influences threaten our unity as a couple?",
            "How can we better prioritize our marriage above other relationships?"
        ],
        "apply": "This week, identify one area where an outside influence is competing with your marriage. Discuss a boundary you can set together.",
        "pray": "Lord, help us return to Your original design for marriage. Show us where we have let other things come between us. Make us truly one.",
        "husband": "What is one way I can show my wife she is my first priority this week?",
        "wife": "What is one way I can show my husband he is my first priority this week?",
        "challenge": "Go on a 'no phone' date this week. Give each other undivided attention."
    },
    {
        "title": "LOVE THAT SERVES - Christ's Example for Husbands",
        "scripture": "Ephesians 5:25-33",
        "passage": [
            "'Husbands, love your wives, even as Christ also loved the church,",
            "and gave himself for it.' - Ephesians 5:25 (KJV)"
        ],
        "discuss": [
            "What does sacrificial love look like in daily marriage life?",
            "Husband: In what ways do you find it hardest to serve your wife?",
            "Wife: When do you feel most loved and served by your husband?",
            "How is Christ's love for the church a model we can actually follow?"
        ],
        "apply": "Husband: Ask your wife, 'What is one thing I can do this week that would make you feel deeply loved?' Then do it without complaint.",
        "pray": "Father, give husbands the strength to love sacrificially. Help us see service as strength, not weakness. Shape us into Your image.",
        "husband": "Where am I being selfish in my marriage? What would sacrificial love look like in that area?",
        "wife": "Am I making it easy or hard for my husband to love me well? How can I receive his love more openly?",
        "challenge": "Husband: Do one task your wife normally does without being asked. Wife: Express specific gratitude for his service."
    },
    {
        "title": "RESPECT AND HONOR - Building Each Other Up",
        "scripture": "Ephesians 5:33, 1 Peter 3:7",
        "passage": [
            "'Nevertheless let every one of you in particular so love his wife",
            "even as himself; and the wife see that she reverence her husband.'",
            "- Ephesians 5:33 (KJV)"
        ],
        "discuss": [
            "What does respect look like vs. what does disrespect look like?",
            "How do we show honor to each other in front of others?",
            "When have you felt most respected/disrespected by your spouse?",
            "How can we disagree while still maintaining honor?"
        ],
        "apply": "Each day this week, find one specific thing to praise about your spouse - say it out loud, in front of others if possible.",
        "pray": "God, guard our tongues from criticism and contempt. Fill our mouths with words that build up. Help us see the best in each other.",
        "husband": "Do I speak about my wife with respect when she is not in the room? What needs to change?",
        "wife": "Do I communicate respect to my husband in the ways HE receives it? What does respect look like to him?",
        "challenge": "Write 5 things you respect about your spouse and read the list to them tonight."
    },
    {
        "title": "COMMUNICATION - Speaking the Truth in Love",
        "scripture": "Ephesians 4:15, 25-32",
        "passage": [
            "'But speaking the truth in love, may grow up into him in all things...",
            "Let no corrupt communication proceed out of your mouth, but that which",
            "is good to the use of edifying.' - Ephesians 4:15, 29 (KJV)"
        ],
        "discuss": [
            "What is the difference between honesty and harshness?",
            "What communication patterns damage our connection?",
            "When is it hardest for us to communicate well?",
            "How can we create a safe space for vulnerable conversation?"
        ],
        "apply": "Practice the Speaker-Listener technique: One person speaks for 2 minutes without interruption, then the listener reflects back what they heard.",
        "pray": "Holy Spirit, guard our words. Help us listen to understand, not to respond. Give us courage to be honest and grace to be gentle.",
        "husband": "What topic have I been avoiding that we need to discuss? What am I afraid will happen if I bring it up?",
        "wife": "What topic have I been avoiding that we need to discuss? What am I afraid will happen if I bring it up?",
        "challenge": "Have a 15-minute 'State of Our Marriage' conversation. No phones, no distractions, no defensiveness."
    },
    {
        "title": "FORGIVENESS - Releasing the Debt",
        "scripture": "Colossians 3:12-14, Matthew 18:21-22",
        "passage": [
            "'And be ye kind one to another, tenderhearted, forgiving one another,",
            "even as God for Christ's sake hath forgiven you.' - Ephesians 4:32 (KJV)",
            "'Then came Peter to him, and said, Lord, how oft shall my brother sin",
            "against me, and I forgive him? till seven times? Jesus saith unto him,",
            "I say not unto thee, Until seven times: but, Until seventy times seven.'",
            "- Matthew 18:21-22 (KJV)"
        ],
        "discuss": [
            "What does biblical forgiveness actually require of us?",
            "Is there any unresolved hurt between us that needs attention?",
            "How do we forgive without enabling repeated harmful behavior?",
            "What is the difference between forgiveness and trust?"
        ],
        "apply": "If there is a lingering hurt, bring it to each other this week with 'I felt hurt when... I choose to forgive... I need... going forward.'",
        "pray": "Father, we have been forgiven so much. Help us extend that same grace to each other. Heal old wounds and give us fresh starts.",
        "husband": "Is there anything I am holding onto that I need to release? Am I punishing my wife for past mistakes?",
        "wife": "Is there anything I am holding onto that I need to release? Am I punishing my husband for past mistakes?",
        "challenge": "Write each other a letter of forgiveness for a past hurt. Exchange them and burn them together as a symbol of release."
    },
    {
        "title": "INTIMACY - More Than Physical",
        "scripture": "Song of Solomon 2:10-13, 1 Corinthians 7:3-5",
        "passage": [
            "'My beloved spake, and said unto me, Rise up, my love, my fair one,",
            "and come away. For, lo, the winter is past, the rain is over and gone.'",
            "- Song of Solomon 2:10-11 (KJV)"
        ],
        "discuss": [
            "What are the different types of intimacy (emotional, spiritual, physical)?",
            "Which type of intimacy do we need to strengthen most right now?",
            "What barriers exist to deeper intimacy between us?",
            "How can we create more space for connection in our busy lives?"
        ],
        "apply": "Schedule 3 intentional moments of connection this week: one emotional (deep conversation), one spiritual (pray together), one physical (non-sexual touch).",
        "pray": "Lord, deepen our intimacy in every dimension. Remove the barriers we have built. Help us be fully known and fully loved.",
        "husband": "What makes me feel closest to my wife? Have I told her? What is one thing I can do to make her feel emotionally safe?",
        "wife": "What makes me feel closest to my husband? Have I told him? What is one thing I can do to make him feel desired and appreciated?",
        "challenge": "Hold hands and pray together every night this week before sleep - even if it is just one sentence each."
    },
    {
        "title": "FINANCES - Stewardship Together",
        "scripture": "Proverbs 3:9-10, Luke 16:10-11",
        "passage": [
            "'Honour the Lord with thy substance, and with the firstfruits of all",
            "thine increase: So shall thy barns be filled with plenty.' - Proverbs 3:9-10 (KJV)"
        ],
        "discuss": [
            "What money habits did we each bring from our families of origin?",
            "Are we unified in our financial decisions or do we operate separately?",
            "What financial stress is affecting our marriage right now?",
            "How can we better honor God with our finances as a team?"
        ],
        "apply": "Sit down together and review your budget (or create one). Pray over your finances and decide on one financial goal to pursue together.",
        "pray": "God, You own it all. Help us be faithful stewards together. Remove financial stress and help us trust You with our provision.",
        "husband": "Am I being transparent about all spending? Is there any financial secret I need to confess?",
        "wife": "Am I being transparent about all spending? Is there any financial secret I need to confess?",
        "challenge": "Create a shared financial goal and put a visual tracker somewhere you both see daily."
    },
    {
        "title": "PARENTING AS A TEAM",
        "scripture": "Proverbs 22:6, Deuteronomy 6:6-7",
        "passage": [
            "'Train up a child in the way he should go: and when he is old, he will",
            "not depart from it.' - Proverbs 22:6 (KJV)"
        ],
        "discuss": [
            "Are we on the same page with discipline and expectations?",
            "Do our children see us as a united team or do they divide us?",
            "How do we protect our marriage while raising children?",
            "What values are we intentionally passing to our children?"
        ],
        "apply": "Identify one area where you are not on the same page with parenting. Discuss privately (never in front of children) and agree on a unified approach.",
        "pray": "Father, help us raise our children with wisdom and unity. Protect our marriage from being consumed by parenting. Give us Your wisdom.",
        "husband": "Am I an engaged father? Where can I step up in leading our family spiritually?",
        "wife": "Am I supporting my husband's role as father? Where can I encourage him more?",
        "challenge": "If applicable, have a family meeting to discuss one family value and how you will all live it out this week."
    },
    {
        "title": "CONFLICT - Fighting Fair",
        "scripture": "Proverbs 15:1, James 1:19-20",
        "passage": [
            "'A soft answer turneth away wrath: but grievous words stir up anger.'",
            "- Proverbs 15:1 (KJV)",
            "'Wherefore, my beloved brethren, let every man be swift to hear, slow",
            "to speak, slow to wrath.' - James 1:19 (KJV)"
        ],
        "discuss": [
            "What are our unhealthy conflict patterns (stonewalling, yelling, etc.)?",
            "What triggers escalation in our disagreements?",
            "How can we fight FOR our marriage instead of against each other?",
            "What 'rules of engagement' should we agree on?"
        ],
        "apply": "Create your own 'Fair Fighting Rules' together. Write them down, sign them, and post them where you can both see them.",
        "pray": "Lord, help us fight fair. When we disagree, remind us we are on the same team. Give us self-control and grace under pressure.",
        "husband": "What is my default in conflict (fight, flight, freeze)? How does that affect my wife?",
        "wife": "What is my default in conflict (fight, flight, freeze)? How does that affect my husband?",
        "challenge": "Agree on a 'time-out' signal. When either of you uses it, take 20 minutes apart, then come back calmly."
    },
    {
        "title": "SPIRITUAL LEADERSHIP - Growing Together in Faith",
        "scripture": "Joshua 24:15, Acts 2:42",
        "passage": [
            "'But as for me and my house, we will serve the Lord.' - Joshua 24:15 (KJV)"
        ],
        "discuss": [
            "What does spiritual leadership in the home look like to each of you?",
            "Are we growing in faith together or separately?",
            "What spiritual disciplines can we practice as a couple?",
            "How can we serve together outside our home?"
        ],
        "apply": "Choose one spiritual discipline to practice together this week: praying together, reading Scripture together, serving together, or fasting together.",
        "pray": "God, draw us closer to You and to each other. Help us lead our home with faith and humility. Use our marriage for Your glory.",
        "husband": "Am I leading spiritually with humility? What one step can I take to grow in spiritual leadership?",
        "wife": "Am I supporting and encouraging spiritual growth? How can I make space for us to grow together?",
        "challenge": "Start a couples devotional routine - even 5 minutes a day reading one verse and praying together."
    },
    {
        "title": "SEASONS OF MARRIAGE - Enduring Through Change",
        "scripture": "Ecclesiastes 3:1-8, Romans 8:28",
        "passage": [
            "'To every thing there is a season, and a time to every purpose under",
            "the heaven.' - Ecclesiastes 3:1 (KJV)"
        ],
        "discuss": [
            "What season is our marriage in right now (newlywed, young kids, empty nest, crisis)?",
            "What has been the hardest season we have faced together?",
            "How has our marriage grown through difficulty?",
            "What season do we want to prepare for next?"
        ],
        "apply": "Name the current season of your marriage honestly. Discuss what this season needs from each of you and from God.",
        "pray": "Father, thank You for sustaining us through every season. Give us eyes to see Your faithfulness and hope for what is ahead.",
        "husband": "What does my wife need from me in THIS season that may be different from past seasons?",
        "wife": "What does my husband need from me in THIS season that may be different from past seasons?",
        "challenge": "Look at your wedding photos together. Share what you remember feeling that day and recommit to that love."
    },
    {
        "title": "LEGACY - The Marriage You Are Building",
        "scripture": "Psalm 127:1, Proverbs 13:22",
        "passage": [
            "'Except the Lord build the house, they labour in vain that build it.'",
            "- Psalm 127:1 (KJV)",
            "'A good man leaveth an inheritance to his children's children.'",
            "- Proverbs 13:22 (KJV)"
        ],
        "discuss": [
            "What kind of marriage legacy do we want to leave for our children/grandchildren?",
            "What did our parents' marriages teach us (good and bad)?",
            "What would we want people to say about our marriage in 50 years?",
            "How can we be an example to other couples around us?"
        ],
        "apply": "Write a Marriage Mission Statement together: 'Our marriage exists to...' Keep it to 1-2 sentences. Display it in your home.",
        "pray": "Lord, build our house. Let our marriage bring You glory and point others to Your love. Help us leave a legacy of faithfulness.",
        "husband": "What kind of husband do I want to be remembered as? What needs to change now to become that man?",
        "wife": "What kind of wife do I want to be remembered as? What needs to change now to become that woman?",
        "challenge": "Write your Marriage Mission Statement and post it where you will see it daily."
    }
]

for i, week in enumerate(weeks):
    # Page 1 of each week
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEK {i+1}: {week['title']}", 'F2', 13)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    pdf.add_text(50, y, f"Scripture: {week['scripture']}", 'F2', 10)
    y -= 20
    pdf.add_text(50, y, "READ TOGETHER:", 'F2', 10)
    y -= 14
    for pline in week['passage']:
        pdf.add_text(60, y, pline, 'F4', 9)
        y -= 13
    y -= 12
    pdf.add_text(50, y, "DISCUSS:", 'F2', 10)
    y -= 14
    for q_idx, q in enumerate(week['discuss']):
        pdf.add_text(60, y, f"{q_idx+1}. {q}", 'F4', 9)
        y -= 13
    y -= 12
    pdf.add_text(50, y, "APPLY:", 'F2', 10)
    y -= 14
    # Wrap apply text
    apply_text = week['apply']
    while len(apply_text) > 75:
        split = apply_text[:75].rfind(' ')
        pdf.add_text(60, y, apply_text[:split], 'F4', 9)
        apply_text = apply_text[split+1:]
        y -= 13
    pdf.add_text(60, y, apply_text, 'F4', 9)
    y -= 18
    pdf.add_text(50, y, "PRAY TOGETHER:", 'F2', 10)
    y -= 14
    pray_text = week['pray']
    while len(pray_text) > 75:
        split = pray_text[:75].rfind(' ')
        pdf.add_text(60, y, pray_text[:split], 'F4', 9)
        pray_text = pray_text[split+1:]
        y -= 13
    pdf.add_text(60, y, pray_text, 'F4', 9)
    y -= 20

    # Page 2 of each week: Individual reflection
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEK {i+1} - INDIVIDUAL REFLECTION", 'F2', 13)
    pdf.add_line(50, 740, 562, 740)
    y = 715
    pdf.add_text(50, y, "FOR HIM:", 'F2', 12)
    y -= 16
    pdf.add_text(60, y, week['husband'], 'F4', 10)
    y -= 18
    for _ in range(5):
        pdf.add_line(60, y, 562, y, 0.3, 0.5)
        y -= 18
    y -= 20
    pdf.add_text(50, y, "FOR HER:", 'F2', 12)
    y -= 16
    pdf.add_text(60, y, week['wife'], 'F4', 10)
    y -= 18
    for _ in range(5):
        pdf.add_line(60, y, 562, y, 0.3, 0.5)
        y -= 18
    y -= 25
    pdf.add_filled_rect(50, y - 5, 512, 50, 0.92)
    pdf.add_rect(50, y - 5, 512, 50, 0.5, 0.5)
    pdf.add_text(60, y + 30, "WEEKLY CHALLENGE:", 'F2', 11)
    pdf.add_text(60, y + 12, week['challenge'], 'F4', 10)
    y -= 70
    pdf.add_text(50, y, "How did the challenge go?", 'F2', 10)
    y -= 16
    for _ in range(4):
        pdf.add_line(60, y, 562, y, 0.3, 0.5)
        y -= 18

# Page 27: Renewal of Vows Writing Page
pdf.new_page()
pdf.add_centered_text(750, "RENEWAL OF VOWS", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "After 12 weeks of study, write new vows to each other reflecting", 'F4', 11)
y -= 14
pdf.add_text(50, y, "what you have learned and how you want to love going forward.", 'F4', 11)
y -= 30
pdf.add_text(50, y, "HIS VOWS TO HER:", 'F2', 12)
y -= 18
for _ in range(10):
    pdf.add_line(60, y, 562, y, 0.3, 0.5)
    y -= 18
y -= 25
pdf.add_text(50, y, "HER VOWS TO HIM:", 'F2', 12)
y -= 18
for _ in range(10):
    pdf.add_line(60, y, 562, y, 0.3, 0.5)
    y -= 18
y -= 15
pdf.add_text(50, y, "Date of renewal: ___/___/___    Witnessed by: _______________________", 'F4', 10)

# Page 28: Our Marriage Vision Page
pdf.new_page()
pdf.add_centered_text(750, "OUR MARRIAGE VISION", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
vision = [
    "Use this page to capture your shared vision for your marriage.",
    "",
    "OUR MARRIAGE MISSION STATEMENT:",
]
for line in vision:
    pdf.add_text(50, y, line, 'F4', 11)
    y -= 16
for _ in range(3):
    pdf.add_line(60, y, 562, y, 0.3, 0.5)
    y -= 18
y -= 10
pdf.add_text(50, y, "IN 1 YEAR, WE WANT OUR MARRIAGE TO:", 'F2', 11)
y -= 16
for _ in range(3):
    pdf.add_line(60, y, 562, y, 0.3, 0.5)
    y -= 18
y -= 10
pdf.add_text(50, y, "IN 5 YEARS, WE WANT OUR MARRIAGE TO:", 'F2', 11)
y -= 16
for _ in range(3):
    pdf.add_line(60, y, 562, y, 0.3, 0.5)
    y -= 18
y -= 10
pdf.add_text(50, y, "IN 25 YEARS, WE WANT OUR MARRIAGE TO:", 'F2', 11)
y -= 16
for _ in range(3):
    pdf.add_line(60, y, 562, y, 0.3, 0.5)
    y -= 18
y -= 10
pdf.add_text(50, y, "THE LEGACY WE WANT TO LEAVE:", 'F2', 11)
y -= 16
for _ in range(3):
    pdf.add_line(60, y, 562, y, 0.3, 0.5)
    y -= 18
y -= 15
pdf.add_centered_text(y, "'Two are better than one; because they have a good reward", 'F5', 10)
pdf.add_centered_text(y - 14, "for their labour.' - Ecclesiastes 4:9", 'F5', 10)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book123_Biblical_Marriage_Study.pdf')
print("Book123_Biblical_Marriage_Study.pdf created successfully!")
