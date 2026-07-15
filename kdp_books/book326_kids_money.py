from pdf_utils import PDFDoc
from book_helpers import add_supplemental, wrap

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    title = "MONEY SMART KIDS: How to Save, Earn & Grow Your Money (Ages 8-14)"

    chapters = [
        ("What Is Money?", "Money is something people use to trade for goods and services.", 
         "Long ago, people used to trade things directly. A farmer might trade eggs for bread. But what if the baker didn't want eggs? That was a big problem! So people invented money as a way to make trading easier. First, they used shells and beads. Then they used metal coins. Today, we use paper bills, coins, and even digital money on computers.",
         ["Find 5 different coins and list what year they were made", "Draw what you think money looked like 1000 years ago", "Ask a parent how they pay for things (cash, card, phone)"],
         "What is the main purpose of money? A) To collect B) To trade for things we need C) To look pretty"),
        ("Needs vs Wants", "Understanding the difference between needs and wants is the first step to being money smart.",
         "A need is something you must have to survive and be healthy: food, water, shelter, clothing, and medicine. A want is something nice to have but you can live without: video games, candy, toys, and fancy clothes. Sometimes it's tricky to tell the difference! Is a phone a need or a want? It depends on the situation.",
         ["Make two columns: NEEDS and WANTS. List 10 items in each", "Look at your last 5 purchases - were they needs or wants?", "Play the Needs vs Wants sorting game with a friend"],
         "Which is a NEED? A) New sneakers B) Warm winter coat C) Video game"),
        ("Saving Strategies", "Saving money means keeping some of your money for later instead of spending it all now.",
         "The best savers follow a simple rule: Pay yourself first! That means before you spend any money, put some into savings. Even saving a small amount adds up over time. If you save just one dollar a day, you'll have 365 dollars in a year! Try the 50-30-20 rule: 50% for needs, 30% for wants, and 20% for savings.",
         ["Set up 3 jars labeled SAVE, SPEND, GIVE", "Calculate how much you'd have if you saved $2/week for a year", "Create a savings thermometer chart for something you want"],
         "If you save $5 every week, how much will you have in 10 weeks? A) $5 B) $50 C) $100"),
        ("Earning Money: 10 Kid-Friendly Ideas", "You don't have to wait until you're grown up to earn money!",
         "There are many ways kids can earn money responsibly. The key is finding something you enjoy that also helps others. When you earn your own money, it feels amazing because you worked hard for it. You also learn to value money more when you know how much effort goes into earning it.",
         ["Pick one idea and make a plan to try it this week", "Create a flyer or poster advertising your service", "Set an earning goal for this month"],
         "What's the best reason to earn your own money? A) To buy everything you want B) To learn responsibility C) To show off"),
        ("Budgeting Basics", "A budget is a plan for how you will use your money.",
         "Making a budget is like making a map for your money. It tells every dollar where to go. Without a budget, money seems to disappear! Start by writing down all the money you get (allowance, gifts, earnings). Then write down what you need to spend. Finally, decide how to split the rest between saving and fun spending.",
         ["Create your first monthly budget on paper", "Track every penny you spend for one week", "Make a pie chart showing where your money goes"],
         "What is a budget? A) A way to get more money B) A plan for your money C) A type of bank account"),
        ("Banking Explained", "A bank is a safe place to keep your money that also helps it grow.",
         "Banks are like super-safe piggy banks. When you put money in a bank (called a deposit), they keep it safe and even pay you a little extra money called interest. Banks use some of the money people deposit to lend to others who need it. There are different types of accounts: savings accounts (for growing money) and checking accounts (for spending money).",
         ["Visit a bank with a parent and ask questions", "Compare interest rates of 3 different banks online", "Open a savings account if you don't have one"],
         "What is interest? A) Being bored B) Extra money the bank pays you C) A fee you pay"),
        ("The Magic of Compound Interest", "Compound interest is when you earn interest on your interest - it's like a money snowball!",
         "Imagine you put $100 in the bank at 5% interest. After one year, you have $105. But the next year, you earn interest on $105, not just $100! So you get $110.25. Each year, the amount grows faster and faster. This is why starting to save when you're young is so powerful - your money has more time to grow.",
         ["Calculate compound interest for $50 over 5 years at 5%", "Draw a graph showing how $100 grows over 20 years", "Ask a parent about retirement accounts and compound interest"],
         "Compound interest means earning interest on: A) Just your original money B) Your interest too C) Someone else's money"),
        ("Setting Financial Goals", "A goal without a plan is just a wish. Financial goals give your saving purpose.",
         "Financial goals are things you want to buy or achieve with money. Short-term goals might take a few weeks (like buying a book). Medium-term goals take months (like buying a bike). Long-term goals take years (like saving for college). Writing down your goals and tracking progress makes you much more likely to achieve them.",
         ["Write 3 financial goals: short, medium, and long-term", "Calculate how long each goal will take to reach", "Make a visual tracker for your biggest goal"],
         "A medium-term financial goal might take: A) 1 week B) A few months C) 10 years"),
        ("Giving & Generosity", "Being generous with money is one of the most rewarding things you can do.",
         "Giving money to help others isn't just nice - it actually makes you happier! Scientists have proven that generous people are healthier and more satisfied with life. You can give to charities, help people in need, or support causes you care about. Even small amounts make a difference when many people give together.",
         ["Research 3 charities that help kids", "Plan a fundraiser for a cause you care about", "Put money in your GIVE jar and choose where to donate it"],
         "Why is giving good for YOU? A) It makes you famous B) It makes you happier C) People owe you"),
        ("Smart Spending Decisions", "Being smart with money isn't about never spending - it's about spending wisely.",
         "Before buying something, ask yourself these questions: Do I really need this? Will I still want it next week? Can I find it cheaper somewhere else? Am I buying it because my friends have it? The 24-hour rule is powerful: wait a full day before buying something you want. If you still want it tomorrow, it might be worth it.",
         ["Use the 24-hour rule on your next purchase", "Compare prices of something you want at 3 stores", "Make a pros and cons list before a big purchase"],
         "The 24-hour rule means: A) Buy it within 24 hours B) Wait 24 hours before buying C) Return it in 24 hours"),
        ("Entrepreneurship for Kids", "An entrepreneur is someone who starts a business to solve a problem and earn money.",
         "You're never too young to be an entrepreneur! Kids all over the world have started successful businesses. The key is finding a problem and creating a solution people will pay for. It could be as simple as a lemonade stand or as creative as making and selling crafts online. Every big business started with just one idea.",
         ["Brainstorm 5 business ideas you could start", "Create a simple business plan for your best idea", "Interview a business owner about how they started"],
         "An entrepreneur: A) Works for someone else B) Starts their own business C) Only adults can be one"),
        ("Building Wealth Habits", "The habits you build now with money will shape your entire financial future.",
         "Wealthy people aren't just lucky - they have specific habits. They save before they spend. They invest their money so it grows. They avoid debt whenever possible. They keep learning about money. And they start young! By building these habits now, you're giving yourself a huge advantage. Even small, consistent actions lead to big results over time.",
         ["Write your top 5 money rules", "Create a daily money habit you'll follow", "Design your Money Smart Kids certificate"],
         "The best time to build good money habits is: A) When you're old B) When you're rich C) Right now, when you're young"),
    ]

    earning_ideas = [
        "1. Dog walking or pet sitting for neighbors",
        "2. Yard work (raking leaves, pulling weeds, watering plants)",
        "3. Tutoring younger kids in a subject you're good at",
        "4. Making and selling crafts or artwork",
        "5. Lemonade or baked goods stand",
        "6. Car washing service",
        "7. Helping elderly neighbors with chores",
        "8. Organizing or decluttering for people",
        "9. Tech help (teaching adults to use phones/computers)",
        "10. Recycling collection service",
    ]

    # Title page
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(620, "MONEY SMART KIDS", 'F2', 32, 0)
    doc.add_centered_text(580, "How to Save, Earn & Grow Your Money", 'F4', 20, 0.2)
    doc.add_centered_text(550, "(Ages 8-14)", 'F4', 16, 0.3)
    doc.add_line(150, 530, 462, 530, 2, 0.3)
    doc.add_centered_text(480, "A Complete Financial Literacy Guide for Kids", 'F4', 14, 0.3)
    doc.add_centered_text(440, "12 Chapters of Money Wisdom", 'F1', 12, 0.4)
    doc.add_centered_text(400, "Stories + Lessons + Activities + Quizzes", 'F1', 12, 0.4)
    doc.add_centered_text(350, "[$]  SAVE  *  EARN  *  GROW  *  GIVE  [$]", 'F3', 14, 0.3)
    doc.add_centered_text(100, f"By {author}", 'F2', 16, 0.2)
    doc.new_page()

    # Copyright page
    doc.add_centered_text(600, "MONEY SMART KIDS", 'F2', 16, 0)
    doc.add_centered_text(570, "How to Save, Earn & Grow Your Money (Ages 8-14)", 'F4', 12, 0.2)
    doc.add_centered_text(530, f"Written by {author}", 'F1', 11, 0.3)
    doc.add_centered_text(510, "Copyright 2025. All rights reserved.", 'F1', 10, 0.4)
    doc.add_centered_text(490, "No part of this book may be reproduced without permission.", 'F1', 10, 0.4)
    doc.add_centered_text(450, "Published for Amazon KDP", 'F1', 10, 0.4)
    doc.add_centered_text(430, "Paperback Edition - 8.5 x 11 inches", 'F1', 10, 0.4)
    doc.add_centered_text(390, "For kids ages 8-14 and their families", 'F1', 11, 0.3)
    doc.new_page()

    # Table of Contents
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 20, 0)
    doc.add_line(150, 710, 462, 710, 1, 0.3)
    y = 670
    for i, (ch_title, _, _, _, _) in enumerate(chapters):
        doc.add_text(72, y, f"Chapter {i+1}: {ch_title}", 'F4', 13, 0.2)
        y -= 28
    doc.add_text(72, y-20, "My Money Plan Worksheets", 'F4', 13, 0.2)
    doc.add_text(72, y-48, "Certificate of Completion", 'F4', 13, 0.2)
    doc.new_page()

    # Introduction
    doc.add_centered_text(720, "INTRODUCTION", 'F2', 20, 0)
    doc.add_line(200, 710, 412, 710, 1, 0.3)
    intro_text = [
        "Welcome to Money Smart Kids!",
        "",
        "Did you know that most adults wish they had learned about money",
        "when they were your age? By reading this book, you're already",
        "ahead of the game! Money is a tool - and like any tool, you need",
        "to learn how to use it properly.",
        "",
        "In this book, you'll discover:",
        "  * What money is and how it works",
        "  * How to save money (even small amounts add up!)",
        "  * Ways to earn your own money",
        "  * The magic of compound interest",
        "  * How to be a smart spender AND generous giver",
        "  * Real stories of kids who are money-smart",
        "",
        "Each chapter includes:",
        "  - A real-life story about a kid like you",
        "  - Clear explanations of money concepts",
        "  - Fun activities to try",
        "  - Quiz questions to test your knowledge",
        "  - A My Money Plan worksheet section",
        "",
        "Are you ready to become a Money Smart Kid?",
        "Let's get started!",
    ]
    y = 670
    for line in intro_text:
        doc.add_text(72, y, line, 'F4', 12, 0.2)
        y -= 22
    doc.new_page()

    # Chapters
    for ch_idx, (ch_title, subtitle, content, activities, quiz) in enumerate(chapters):
        # Chapter title page
        doc.add_filled_rect(50, 600, 512, 130, 0.9)
        doc.add_centered_text(700, f"CHAPTER {ch_idx + 1}", 'F1', 14, 0.4)
        doc.add_centered_text(660, ch_title, 'F2', 22, 0)
        doc.add_centered_text(625, subtitle, 'F4', 12, 0.3)
        
        # Story section
        doc.add_text(72, 560, "A STORY ABOUT MONEY", 'F2', 14, 0.1)
        doc.add_line(72, 555, 300, 555, 1, 0.3)
        
        story_names = ["Maya", "Jordan", "Kai", "Sofia", "Ethan", "Lily", "Marcus", "Aisha", "Tyler", "Priya", "Noah", "Zoe"]
        story_name = story_names[ch_idx % len(story_names)]
        
        stories = [
            f"{story_name} looked at the shiny toy in the store window. It cost $25. 'I wish I had money,' {story_name} said. Then grandma explained that money is something we earn and use carefully. {story_name} decided to learn everything about money - and that's when the adventure began!",
            f"{story_name} really wanted a new video game ($40) AND new shoes for school ($35). But {story_name} only had $50 saved up. 'I can't get both,' {story_name} realized. That's when Dad said, 'Which one do you NEED and which do you WANT?' This question changed everything.",
            f"Every time {story_name} got money, it seemed to disappear! Birthday money - gone. Allowance - spent by Tuesday. Then {story_name}'s aunt taught the 3-jar system. 'Put money in SAVE, SPEND, and GIVE jars before you do anything else.' Three months later, {story_name} had saved $60!",
            f"{story_name} wanted to buy a drone that cost $150. 'That's so much money!' {story_name} thought. But then {story_name} made a list of ways to earn money. Starting with walking the neighbor's dog for $5 per walk, {story_name} earned the full amount in just 6 weeks!",
            f"{story_name} used to spend every dollar the moment it arrived. But after learning about budgets, {story_name} made a plan: $10/week allowance = $5 savings + $3 spending + $2 giving. After 3 months, {story_name} had enough for the bike without asking parents for extra!",
            f"When {story_name} turned 10, Mom took them to open a real bank account. 'Your money will be safe here AND it will grow!' Mom explained. {story_name} deposited birthday money and watched the balance grow each month. It was like planting a money seed!",
            f"'{story_name}, if you invest $100 and it grows 10% each year, how much will you have in 30 years?' asked the math teacher. {story_name} guessed $400. The real answer? Over $1,700! The class was amazed. 'That is compound interest,' the teacher smiled.",
            f"{story_name} wanted three things: a skateboard ($80), summer camp ($200), and college savings. 'You can have all of them,' said Dad, 'but not all at once. That is why we set goals with timelines.' {story_name} learned to be patient and plan ahead.",
            f"When {story_name} saw kids at school who couldn't afford lunch, something changed inside. {story_name} started putting 20% of all money into a GIVE jar. After a few months, {story_name} donated $30 to the school lunch fund. It felt better than buying any toy!",
            f"{story_name} almost bought a $30 t-shirt just because friends had it. Then {story_name} remembered the 24-hour rule: wait one day. The next day, {story_name} didn't even want it anymore! That $30 went straight into savings instead.",
            f"At age 11, {story_name} started a dog-walking business. It began with one neighbor's dog. Within a month, {story_name} had 4 regular clients earning $40/week! 'I'm an entrepreneur!' {story_name} said proudly. And it all started with solving one simple problem.",
            f"{story_name} made a promise: 'Every single week, I will save something - even if it's just one dollar.' One year later, {story_name} had $200 saved. 'Small actions, done consistently, lead to big results,' {story_name} wrote in a journal. The wealth-building habit was set for life.",
        ]
        
        story = stories[ch_idx]
        words = story.split()
        lines = []
        line = ""
        for word in words:
            if len(line + " " + word) > 70:
                lines.append(line)
                line = word
            else:
                line = line + " " + word if line else word
        if line:
            lines.append(line)
        
        y = 530
        for sline in lines:
            doc.add_text(72, y, sline, 'F4', 11, 0.2)
            y -= 20
        
        # Lesson explanation
        y -= 20
        doc.add_text(72, y, "THE LESSON", 'F2', 14, 0.1)
        y -= 5
        doc.add_line(72, y, 200, y, 1, 0.3)
        y -= 25
        
        content_words = content.split()
        content_lines = []
        line = ""
        for word in content_words:
            if len(line + " " + word) > 75:
                content_lines.append(line)
                line = word
            else:
                line = line + " " + word if line else word
        if line:
            content_lines.append(line)
        
        for cline in content_lines:
            if y < 80:
                doc.new_page()
                y = 720
            doc.add_text(72, y, cline, 'F1', 11, 0.2)
            y -= 20
        
        doc.new_page()
        
        # Extra content for earning ideas chapter
        if ch_idx == 3:
            doc.add_centered_text(720, "10 KID-FRIENDLY WAYS TO EARN MONEY", 'F2', 16, 0)
            doc.add_line(150, 710, 462, 710, 1, 0.3)
            y = 680
            for idea in earning_ideas:
                doc.add_text(72, y, idea, 'F1', 12, 0.2)
                y -= 35
                tip = ["Walk dogs before/after school", "Spring and fall are busiest", "Start with subjects you get A's in",
                       "Try Etsy or local craft fairs", "Weekends in warm weather work best", "Offer interior and exterior",
                       "Be reliable and friendly", "Start with family members", "Many adults need basic tech help",
                       "Check local recycling rates first"]
                doc.add_text(90, y, f"Tip: {tip[earning_ideas.index(idea)]}", 'F4', 10, 0.4)
                y -= 28
            doc.new_page()
        
        # Activities page
        doc.add_centered_text(720, f"CHAPTER {ch_idx + 1} ACTIVITIES", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        y = 670
        for i, activity in enumerate(activities):
            doc.add_filled_rect(60, y - 5, 492, 45, 0.95)
            doc.add_text(72, y + 20, f"Activity {i+1}:", 'F2', 12, 0.1)
            doc.add_text(72, y, activity, 'F1', 11, 0.2)
            y -= 70
        
        # Quiz
        y -= 30
        doc.add_text(72, y, "QUIZ TIME!", 'F2', 14, 0.1)
        y -= 25
        doc.add_text(72, y, quiz, 'F1', 11, 0.2)
        
        # My Money Plan section
        y -= 60
        doc.add_text(72, y, "MY MONEY PLAN", 'F2', 14, 0.1)
        y -= 5
        doc.add_line(72, y, 250, y, 1, 0.3)
        y -= 30
        doc.add_text(72, y, "What I learned from this chapter: ________________________________", 'F1', 11, 0.3)
        y -= 30
        doc.add_text(72, y, "_________________________________________________________________", 'F1', 11, 0.3)
        y -= 30
        doc.add_text(72, y, "One thing I will do this week: ___________________________________", 'F1', 11, 0.3)
        y -= 30
        doc.add_text(72, y, "_________________________________________________________________", 'F1', 11, 0.3)
        y -= 30
        doc.add_text(72, y, "My money goal for this month: ____________________________________", 'F1', 11, 0.3)
        
        doc.new_page()

    # Bonus: Money Vocabulary page
    doc.add_centered_text(720, "MONEY VOCABULARY", 'F2', 18, 0)
    doc.add_line(180, 710, 432, 710, 1, 0.3)
    vocab = [
        ("Budget", "A plan for how you will spend and save your money"),
        ("Interest", "Money the bank pays you for keeping your money there"),
        ("Deposit", "Putting money INTO your bank account"),
        ("Withdrawal", "Taking money OUT of your bank account"),
        ("Entrepreneur", "Someone who starts their own business"),
        ("Investment", "Using money to make more money over time"),
        ("Debt", "Money you owe to someone else"),
        ("Income", "Money you earn or receive"),
        ("Expense", "Money you spend"),
        ("Profit", "Money earned after subtracting costs"),
    ]
    y = 670
    for term, definition in vocab:
        doc.add_text(72, y, f"{term}:", 'F2', 12, 0.1)
        doc.add_text(72, y - 20, definition, 'F1', 11, 0.3)
        y -= 50
    doc.new_page()

    # 30-day savings challenge
    doc.add_centered_text(720, "30-DAY SAVINGS CHALLENGE", 'F2', 18, 0)
    doc.add_centered_text(695, "Save a little each day and watch it grow!", 'F4', 12, 0.3)
    y = 660
    for week in range(1, 5):
        doc.add_text(72, y, f"Week {week}:", 'F2', 12, 0.1)
        y -= 25
        for day in range(1, 8):
            day_num = (week - 1) * 7 + day
            if day_num <= 30:
                doc.add_text(90, y, f"Day {day_num}: Amount saved $_____ | Running total: $_____", 'F1', 10, 0.3)
                y -= 20
        y -= 15
    doc.add_text(72, y - 10, "TOTAL SAVED IN 30 DAYS: $________________", 'F2', 13, 0.1)
    doc.new_page()

    # Certificate
    doc.add_filled_rect(50, 200, 512, 450, 0.95)
    doc.add_rect(60, 210, 492, 430, 2, 0.3)
    doc.add_centered_text(600, "CERTIFICATE OF COMPLETION", 'F2', 22, 0)
    doc.add_centered_text(560, "This certifies that", 'F4', 14, 0.3)
    doc.add_centered_text(520, "________________________________", 'F1', 14, 0.3)
    doc.add_centered_text(495, "(Your Name)", 'F1', 10, 0.5)
    doc.add_centered_text(460, "has successfully completed", 'F4', 14, 0.3)
    doc.add_centered_text(430, "MONEY SMART KIDS", 'F2', 18, 0)
    doc.add_centered_text(400, "and is now officially a Money Smart Kid!", 'F4', 14, 0.3)
    doc.add_centered_text(350, "Date: _______________", 'F1', 12, 0.3)
    doc.add_centered_text(300, f"Author: {author}", 'F4', 12, 0.3)
    doc.new_page()

    add_supplemental(doc, 'Money', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book326_Kids_Money_Smart.pdf')
    print("Book326_Kids_Money_Smart.pdf created successfully!")

if __name__ == "__main__":
    create_book()
