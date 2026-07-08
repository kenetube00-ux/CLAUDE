from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(490, "STRONGER TOGETHER", 'F2', 18)
pdf.add_centered_text(465, "A Christian Marriage Counseling", 'F4', 12)
pdf.add_centered_text(448, "Workbook for Couples", 'F4', 12)
pdf.add_centered_text(380, "Build a Marriage That Honors God", 'F5', 11)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(500, "STRONGER TOGETHER", 'F2', 12)
pdf.add_centered_text(475, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: Marriage Covenant Reflection
pdf.new_page()
pdf.add_centered_text(610, "OUR MARRIAGE COVENANT REFLECTION", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "'Therefore what God has joined together, let no one separate.'",
    "- Mark 10:9", "",
    "Our wedding date: ____________________________",
    "Years married: _______", "",
    "What drew me to my spouse initially:",
    "His answer: ___________________________________",
    "Her answer: ___________________________________", "",
    "What I promised on our wedding day:",
    "His answer: ___________________________________",
    "Her answer: ___________________________________", "",
    "What 'covenant' means to us as a couple:",
    "_______________________________________________",
    "_______________________________________________", "",
    "Where are we now? (Rate 1-10):",
    "Communication: His ___ Her ___",
    "Intimacy: His ___ Her ___",
    "Trust: His ___ Her ___",
    "Spiritual connection: His ___ Her ___",
    "Fun together: His ___ Her ___"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 4: Communication Styles
pdf.new_page()
pdf.add_centered_text(610, "COMMUNICATION STYLES ASSESSMENT", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "Understanding how you EACH communicate prevents misunderstanding.", "",
    "MY COMMUNICATION STYLE (each person check):",
    "__ Assertive (direct, respectful, clear)",
    "__ Passive (avoid conflict, hold it in, hint)",
    "__ Aggressive (loud, critical, attacking)",
    "__ Passive-aggressive (sarcasm, silent treatment)", "",
    "WHEN I'M UPSET, I TEND TO:",
    "He: __ Withdraw  __ Attack  __ Shut down  __ Cry",
    "She: __ Withdraw  __ Attack  __ Shut down  __ Cry", "",
    "WHAT I NEED WHEN I'M UPSET:",
    "He needs: ____________________________________",
    "She needs: ____________________________________", "",
    "CONVERSATION RULES WE AGREE TO:",
    "1. No name-calling, ever",
    "2. No bringing up the past (stay on topic)",
    "3. Take a break if voices raise (return in ___ min)",
    "4. Listen to understand, not to respond",
    "5. Use 'I feel' instead of 'You always'",
    "6. Pray before difficult conversations",
    "7. _____________________________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 5: Love Languages
pdf.new_page()
pdf.add_centered_text(610, "LOVE LANGUAGES DISCOVERY", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "The 5 Love Languages (Gary Chapman):", "",
    "1. WORDS OF AFFIRMATION: Compliments, encouragement, verbal love",
    "2. ACTS OF SERVICE: Doing helpful things (chores, errands, cooking)",
    "3. RECEIVING GIFTS: Thoughtful presents, symbolic gestures",
    "4. QUALITY TIME: Undivided attention, shared experiences",
    "5. PHYSICAL TOUCH: Hugs, holding hands, intimacy, closeness", "",
    "MY PRIMARY LOVE LANGUAGE: He: ___ She: ___",
    "MY SECONDARY LOVE LANGUAGE: He: ___ She: ___", "",
    "HOW TO FILL MY SPOUSE'S LOVE TANK:",
    "If his language is ________, I will: __________",
    "_______________________________________________",
    "If her language is ________, I will: __________",
    "_______________________________________________", "",
    "THINGS THAT DRAIN MY LOVE TANK:",
    "He: ___________________________________________",
    "She: __________________________________________", "",
    "This week I will love my spouse in THEIR language by:",
    "He will: ______________________________________",
    "She will: _____________________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 6: Conflict Resolution God's Way
pdf.new_page()
pdf.add_centered_text(610, "CONFLICT RESOLUTION GOD'S WAY", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "'Be quick to listen, slow to speak, slow to become angry.'",
    "- James 1:19", "",
    "BIBLICAL PRINCIPLES FOR CONFLICT:", "",
    "1. PRAY FIRST (Matthew 18:19-20)",
    "   Before discussing, pray together for wisdom and humility.", "",
    "2. SPEAK THE TRUTH IN LOVE (Ephesians 4:15)",
    "   Be honest but gentle. Seek to build up, not tear down.", "",
    "3. DO NOT LET THE SUN GO DOWN ON YOUR ANGER (Eph 4:26)",
    "   Resolve issues the same day when possible.", "",
    "4. SEEK TO UNDERSTAND (Proverbs 18:2)",
    "   A fool takes no pleasure in understanding. Listen first.", "",
    "5. FORGIVE AS CHRIST FORGAVE YOU (Colossians 3:13)",
    "   Forgiveness is a choice, not a feeling. Choose it daily.", "",
    "OUR CONFLICT PATTERN:",
    "What we fight about most: _____________________",
    "What triggers us: He: _________ She: __________",
    "What we'll do differently: ____________________",
    "_______________________________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 7: Forgiveness Exercises
pdf.new_page()
pdf.add_centered_text(610, "FORGIVENESS EXERCISES FOR COUPLES", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "'Bear with each other and forgive one another if any of you has",
    "a grievance. Forgive as the Lord forgave you.' - Col 3:13", "",
    "EXERCISE 1: Naming the Hurt",
    "What my spouse did that hurt me:",
    "_______________________________________________",
    "How it made me feel: __________________________",
    "What I need to hear from them: ________________", "",
    "EXERCISE 2: Taking Responsibility",
    "My part in the conflict (be honest):",
    "_______________________________________________",
    "What I'm sorry for: ___________________________", "",
    "EXERCISE 3: Choosing Forgiveness",
    "'I forgive you for _____________________________.",
    "I choose to release this and not hold it over you.",
    "This does not mean it was okay, but I choose freedom.'", "",
    "EXERCISE 4: Rebuilding Trust",
    "Trust is rebuilt through consistent actions over time.",
    "Action I commit to: ___________________________",
    "How my spouse can help: _______________________",
    "We will check in on this: Weekly / Monthly"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 8: Intimacy Building
pdf.new_page()
pdf.add_centered_text(610, "INTIMACY BUILDING ACTIVITIES", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "Intimacy = Into Me You See. It's more than physical.", "",
    "EMOTIONAL INTIMACY BUILDERS:",
    "- Share one thing you're grateful for about each other daily",
    "- Ask 'How was your heart today?' instead of 'How was your day?'",
    "- Share a childhood memory each week",
    "- Dream together about the future",
    "- Pray together before sleep", "",
    "PHYSICAL INTIMACY BUILDERS:",
    "- Hold hands during prayer",
    "- 10-second kiss daily (yes, count!)",
    "- Non-sexual touch: back rubs, foot massages",
    "- Discuss needs and desires openly without shame", "",
    "SPIRITUAL INTIMACY BUILDERS:",
    "- Read Scripture together weekly",
    "- Pray together daily (even if short)",
    "- Attend church together",
    "- Serve together in ministry",
    "- Share what God is teaching you", "",
    "This week we will intentionally connect by:",
    "_______________________________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 9: Prayer Together Guide
pdf.new_page()
pdf.add_centered_text(610, "PRAYER TOGETHER GUIDE", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "'For where two or three gather in my name, there am I with them.'",
    "- Matthew 18:20", "",
    "Many couples struggle to pray together. Start simple:", "",
    "BEGINNER: Sentence Prayers",
    "Take turns saying one sentence each. That's enough.", "",
    "INTERMEDIATE: ACTS Model",
    "A - Adoration (praise God together)",
    "C - Confession (not to each other - to God silently)",
    "T - Thanksgiving (name 3 blessings together)",
    "S - Supplication (pray for each other's needs)", "",
    "ADVANCED: Praying Scripture Together",
    "Choose a verse and pray it over your marriage:", "",
    "PRAYER PROMPTS FOR COUPLES:",
    "- Lord, help us to love each other as You love us.",
    "- Give us patience when we frustrate each other.",
    "- Protect our marriage from temptation and division.",
    "- Help us to put each other before ourselves.",
    "- Draw us closer to You and to each other.", "",
    "We commit to praying together:",
    "__ Daily  __ 3x/week  __ Weekly",
    "Best time for us: ____________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 10: Financial Unity
pdf.new_page()
pdf.add_centered_text(610, "FINANCIAL UNITY WORKSHEET", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "Money conflict is the #1 cause of divorce. Get on the same page.", "",
    "OUR FINANCIAL VALUES:",
    "His top financial priority: ____________________",
    "Her top financial priority: ____________________",
    "Where we agree: _______________________________",
    "Where we disagree: ____________________________", "",
    "OUR FINANCIAL GOALS (together):",
    "6-month goal: $_________ For: _________________",
    "1-year goal: $__________ For: _________________",
    "5-year goal: $__________ For: _________________", "",
    "BUDGET AGREEMENTS:",
    "Monthly income: $______________________________",
    "Giving/tithe (____%): $________________________",
    "Savings (____%): $____________________________",
    "Spending money (each): $______________________",
    "No-discussion spending limit: $________________",
    "Must-discuss spending limit: $_________________", "",
    "DEBT PAYOFF PLAN:",
    "Total debt: $__________________________________",
    "Method: Snowball / Avalanche / Other",
    "Target debt-free date: ________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 11: Parenting Alignment + Date Night Planner
pdf.new_page()
pdf.add_centered_text(610, "PARENTING ALIGNMENT & DATE NIGHTS", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "PARENTING ALIGNMENT CHECK (if applicable):", "",
    "Our parenting style: Authoritative / Permissive / Strict",
    "His tendency: ____ Her tendency: ____", "",
    "We agree on: __________________________________",
    "We disagree on: _______________________________",
    "How we'll handle disagreements about kids:",
    "_______________________________________________", "",
    "Rules: united front in public, discuss privately.", "",
    "WEEKLY DATE NIGHT PLANNER:",
    "Our date night: Every _________ at _____",
    "Babysitter/childcare: _________________________", "",
    "DATE IDEAS (alternate choosing):",
    "1. _____________________ 2. ___________________",
    "3. _____________________ 4. ___________________",
    "5. _____________________ 6. ___________________", "",
    "DATE NIGHT RULES:",
    "- No phones (or limited use)",
    "- No talking about kids/work only",
    "- Take turns planning",
    "- Budget: $_______ per date"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 12: Gratitude 30-Day Challenge
pdf.new_page()
pdf.add_centered_text(610, "30-DAY GRATITUDE CHALLENGE FOR SPOUSE", 'F2', 12)
pdf.add_line(50, 598, 382, 598)
y = 578
pdf.add_text(50, y, "Each day, write one thing you're grateful for about your spouse:", 'F4', 9)
y -= 15
for i in range(30):
    col = i % 2
    row = i // 2
    pdf.add_text(50 + col*190, y - row*17, f"Day {i+1}: ________________________", 'F3', 8)


# Page 13: Fighting Fair Rules
pdf.new_page()
pdf.add_centered_text(610, "FIGHTING FAIR RULES AGREEMENT", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "We agree to the following rules when we disagree:", "",
    "__ We will not raise our voices",
    "__ We will not use words like 'always' or 'never'",
    "__ We will not bring up past forgiven offenses",
    "__ We will not involve children in our arguments",
    "__ We will not threaten divorce",
    "__ We will take a time-out if emotions escalate",
    "__ We will use I-statements",
    "__ We will listen without interrupting",
    "__ We will not go to bed without at least a truce",
    "__ We will pray together after resolution",
    "__ We will not discuss issues via text message",
    "__ We will not criticize in front of others", "",
    "Our safe word for 'I need a break': ____________",
    "Break duration: _______ minutes",
    "Who returns to the conversation first: _________", "",
    "Signed: He: ________________ She: _____________",
    "Date: _________________________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 14: Shared Vision & Goals
pdf.new_page()
pdf.add_centered_text(610, "OUR SHARED VISION & GOALS", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "'Where there is no vision, the people perish.' - Proverbs 29:18", "",
    "OUR FAMILY VISION STATEMENT:",
    "_______________________________________________",
    "_______________________________________________", "",
    "1-YEAR GOALS (together):",
    "Spiritual: ____________________________________",
    "Financial: ____________________________________",
    "Relational: ___________________________________",
    "Fun/Adventure: ________________________________", "",
    "5-YEAR VISION:",
    "Where we live: ________________________________",
    "Career: _______________________________________",
    "Family: _______________________________________",
    "Ministry: _____________________________________", "",
    "10-YEAR DREAM:",
    "_______________________________________________",
    "_______________________________________________", "",
    "OUR MARRIAGE MISSION:",
    "As a couple, we exist to: _____________________",
    "_______________________________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Pages 15-19: Anniversary Reflection (5 years)
for yr in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(610, f"ANNIVERSARY REFLECTION - YEAR {yr}", 'F2', 13)
    pdf.add_line(50, 598, 382, 598)
    y = 575
    for line in [
        f"Date: ___/___/_____ (Anniversary #{yr})", "",
        "HIGHLIGHTS OF THIS YEAR:",
        "Best memory together: _________________________",
        "_______________________________________________",
        "Biggest challenge we overcame: ________________",
        "_______________________________________________",
        "How we grew closer: ___________________________",
        "_______________________________________________", "",
        "GRATITUDE:",
        "He is grateful for: ___________________________",
        "She is grateful for: __________________________", "",
        "AREAS FOR GROWTH NEXT YEAR:",
        "We want to improve: ___________________________",
        "We commit to: _________________________________", "",
        "LOVE NOTE TO EACH OTHER:",
        "His note: _____________________________________",
        "_______________________________________________",
        "Her note: _____________________________________",
        "_______________________________________________"
    ]:
        pdf.add_text(50, y, line, 'F4', 10)
        y -= 15

# Page 20: Scripture Promises
pdf.new_page()
pdf.add_centered_text(610, "SCRIPTURE PROMISES FOR MARRIAGE", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "'Love is patient, love is kind. It does not envy, it does not boast.'",
    "- 1 Corinthians 13:4", "",
    "'Two are better than one, because they have a good return for",
    "their labor.' - Ecclesiastes 4:9", "",
    "'Above all, love each other deeply, because love covers over a",
    "multitude of sins.' - 1 Peter 4:8", "",
    "'Submit to one another out of reverence for Christ.'",
    "- Ephesians 5:21", "",
    "'Be completely humble and gentle; be patient, bearing with one",
    "another in love.' - Ephesians 4:2", "",
    "'Therefore encourage one another and build each other up.'",
    "- 1 Thessalonians 5:11", "",
    "'Let all that you do be done in love.' - 1 Corinthians 16:14", "",
    "OUR MARRIAGE VERSE:",
    "_______________________________________________",
    "_______________________________________________", "",
    "Your marriage is worth fighting for. Keep choosing each other."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book108_Marriage_Counseling_Workbook.pdf')
print("Book108_Marriage_Counseling_Workbook.pdf created successfully!")
