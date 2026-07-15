from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    chapters = [
        ("Fixed vs Growth Mindset", "There are two ways to think about your abilities. A FIXED mindset says: 'I'm either smart or I'm not. I can either do it or I can't.' A GROWTH mindset says: 'I can get smarter with effort. I can't do it YET, but I will if I keep trying.' People with growth mindsets learn faster, handle challenges better, and achieve more - because they believe effort leads to improvement!",
         "Thomas Edison failed 1,000 times before inventing the light bulb. He said: 'I didn't fail. I found 1,000 ways that don't work.' That's growth mindset!",
         ["I'm bad at math -> I'm still learning math", "I can't do this -> I can't do this YET", "This is too hard -> This will take more effort"]),
        ("The Power of YET", "One tiny word can change everything: YET. 'I can't ride a bike' becomes 'I can't ride a bike YET.' 'I don't understand fractions' becomes 'I don't understand fractions YET.' The word YET means you're on a journey. You haven't arrived, but you're moving forward. Every expert started as a beginner who kept going. Add YET to every negative thought and watch how it transforms your perspective.",
         "A baby doesn't give up after falling 100 times while learning to walk. They don't say 'I guess I'm just not a walker.' They get up and try again. That's the power of YET.",
         ["I don't understand science", "I'm not good at sports", "I can't make friends easily"]),
        ("Learning from Mistakes", "Mistakes are not proof that you're failing - they're proof that you're TRYING. Every mistake teaches you something valuable. Scientists call mistakes 'data.' Athletes call missed shots 'practice.' Musicians call wrong notes 'learning.' The only real mistake is being too afraid to try at all. Embrace your mistakes, study them, and use them as stepping stones to success.",
         "Michael Jordan was cut from his high school basketball team. J.K. Rowling's Harry Potter was rejected by 12 publishers. Oprah was fired from her first TV job. They all learned from their mistakes.",
         ["Write about a time a mistake taught you something valuable", "Interview an adult about their biggest mistake and what they learned", "Start a 'Mistake Journal' - record mistakes and lessons weekly"]),
        ("Effort Beats Talent", "Natural talent is great, but effort always wins in the long run. Research shows that people who believe in effort outperform those who rely on talent alone. Why? Because talented people often avoid challenges (they might fail and look bad). But effort-focused people embrace challenges (that's how they grow). The tortoise really does beat the hare!",
         "Studies show that praising kids for effort ('You worked so hard!') leads to better outcomes than praising talent ('You're so smart!'). Effort praise motivates trying harder.",
         ["Think of something you improved at through practice", "Set a goal that requires effort, not just talent", "Track your practice hours this week on something challenging"]),
        ("Embracing Challenges", "Challenges are like weights at the gym - they make you stronger! When something feels difficult, your brain is literally growing new connections. Easy things don't teach you much. Hard things build new neural pathways. Next time you face something challenging, try saying: 'My brain is growing right now!' instead of 'This is too hard.' Challenges are where all the growth happens.",
         "Your brain is like a muscle. Just like lifting weights makes muscles bigger, solving hard problems makes your brain form new connections. No challenge = no growth.",
         ["List 3 challenges you're currently facing", "Pick one and break it into smaller, manageable steps", "Celebrate after completing each step!"]),
        ("Dealing with Failure", "Failure is not the opposite of success - it's PART of success. Every successful person has a long list of failures. The difference is they didn't let failure stop them. They failed FORWARD - using each failure as a lesson and stepping stone. How you respond to failure defines your future. Will you give up or get up?",
         "FAIL = First Attempt In Learning. Reframe failure as a teacher, not a judge. Ask: 'What can I learn?' not 'What's wrong with me?'",
         ["Write about your biggest failure - what did it teach you?", "Create a 'failure resume' of famous people's failures", "Next time you fail, write 3 things you learned from it"]),
        ("The Brain Is a Muscle", "Neuroscience proves that your brain physically changes when you learn! Every time you practice something hard, neurons in your brain make new connections. The more you practice, the stronger these connections get. This is called neuroplasticity. You are literally BUILDING your brain every time you study, practice, or learn something new. Your intelligence is not fixed!",
         "When you struggle with something, your brain releases a chemical that helps neurons connect. That means struggling is actually your brain's BEST learning state!",
         ["Draw your brain growing new connections", "Research: what does 'neurons that fire together wire together' mean?", "Choose one skill and practice it 15 minutes daily for a week"]),
        ("Famous People Who Failed First", "Walt Disney was fired for 'lacking imagination.' Einstein couldn't speak until age 4. Beethoven's music teacher said he was 'hopeless.' Steven Spielberg was rejected from film school 3 times. Each of these people could have given up. But they had growth mindsets. They believed they could improve. And they did - changing the world in the process.",
         "The pattern: Try -> Fail -> Learn -> Try differently -> Fail better -> Learn more -> Eventually SUCCEED. There are no shortcuts.",
         ["Research 3 more famous people who overcame failure", "Write a 'failure to success' story about yourself", "Create a motivational poster with a growth mindset quote"]),
        ("Positive Self-Talk", "The voice in your head matters more than any voice outside. If you constantly tell yourself 'I'm stupid' or 'I can't do this,' your brain believes it. But if you tell yourself 'I'm learning' and 'I can figure this out,' your brain rises to meet that belief. You talk to yourself all day long - make sure it's helpful, encouraging talk!",
         "Replace: 'I'm not smart enough' with 'I haven't learned this yet.' Replace: 'Everyone is better than me' with 'Everyone is on their own journey.'",
         ["Write 5 negative thoughts you often have, then rewrite each positively", "Put positive sticky notes on your mirror", "Practice saying 'I can do hard things' before challenges"]),
        ("Setting Stretch Goals", "A stretch goal pushes you just beyond your comfort zone. Not so easy it's boring, not so hard you give up - just challenging enough to make you grow. Break big goals into smaller milestones. Celebrate progress, not just completion. And remember: the person who aims for the moon might land among the stars. Dream big, then plan small steps.",
         "SMART goals: Specific, Measurable, Achievable, Relevant, Time-bound. 'I'll read more' is vague. 'I'll read 20 pages daily for 30 days' is SMART.",
         ["Set 3 stretch goals: easy, medium, and hard", "Break your hard goal into 5 smaller steps", "Create a visual tracker for your goals"]),
        ("Celebrating Growth (Not Just Success)", "Growth mindset means celebrating the PROCESS, not just the result. Did you try something scary? Celebrate! Did you practice even when it was boring? Celebrate! Did you ask for help? Celebrate! Did you keep going after failure? Celebrate! Growth happens in the trying, not just the achieving. Notice and appreciate your effort, persistence, and courage.",
         "Instead of 'I got an A!' try 'I studied really hard and it paid off!' The first celebrates luck. The second celebrates effort you can repeat.",
         ["List 5 growth moments from this month (even small ones!)", "Write a letter to yourself celebrating your effort", "Create a 'Growth Wins' jar - add a note whenever you grow"]),
        ("My Growth Mindset Journal", "This final chapter is YOUR space. Use these 30 daily prompts to build your growth mindset muscle every single day. Journaling helps your brain process experiences, find patterns, and strengthen positive thinking pathways. Just 5 minutes a day can transform how you think about challenges, effort, and your own potential. You've got this!",
         "Consistency is key. Even on days when you don't feel like writing, just jot one sentence. Small daily actions create massive long-term change.",
         ["Complete at least 10 prompts this month", "Share one insight with a friend or family member", "Re-read your entries after 30 days to see your growth"]),
    ]

    title_page(doc, "I CAN DO HARD THINGS", "A Growth Mindset Workbook for Kids (Ages 7-12)", "12 Chapters * True Stories * Science * Activities * 30 Journal Prompts")
    copyright_page(doc, "I CAN DO HARD THINGS: A Growth Mindset Workbook")
    toc_page(doc, [c[0] for c in chapters])

    # Intro
    doc.add_centered_text(720, "YOUR BRAIN CAN GROW!", 'F2', 18, 0)
    y = add_wrapped(doc, 72, 680, "What if I told you that your brain is like a muscle? That every time you try something hard, practice a new skill, or even make a mistake, your brain is literally getting STRONGER? That's not just motivation talk - it's science! This book will show you how to develop a GROWTH MINDSET: the belief that you can improve at anything through effort, strategies, and help from others. Ready to discover your unlimited potential?", 'F4', 12, 0.2)
    doc.new_page()

    for idx, (ch_title, content, story, rewrites) in enumerate(chapters):
        chapter_header(doc, idx+1, ch_title)
        y = 580
        y = add_wrapped(doc, 72, y, content, 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "INSPIRING TRUE STORY:", 'F2', 12, 0.1)
        y -= 20
        y = add_wrapped(doc, 90, y, story, 'F4', 11, 0.3)
        doc.new_page()

        # Activity page
        doc.add_centered_text(720, f"CHAPTER {idx+1}: GROWTH ACTIVITIES", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        
        if idx < 11:  # Reframe exercises for first 11 chapters
            doc.add_text(72, 680, "REFRAME IT! (Fixed -> Growth)", 'F2', 13, 0.1)
            y = 655
            for r in rewrites:
                doc.add_text(90, y, f"Fixed: \"{r}\"", 'F1', 11, 0.2)
                y -= 20
                doc.add_text(90, y, "Growth: _______________________________________________", 'F1', 11, 0.4)
                y -= 30
        
            # Affirmation
            y -= 20
            affirmations = [
                "I can learn anything I put my mind to.",
                "I haven't mastered this YET, and that's okay.",
                "Mistakes help me grow and learn.",
                "My effort determines my success.",
                "Challenges make me stronger.",
                "Failure is just feedback for improvement.",
                "My brain grows stronger every day.",
                "If they can do it, I can learn to do it too.",
                "I choose encouraging thoughts.",
                "I set goals and work toward them daily.",
                "I celebrate my effort, not just results.",
                "Every day I am growing and improving.",
            ]
            doc.add_text(72, y, "TODAY'S AFFIRMATION:", 'F2', 13, 0.1)
            y -= 25
            doc.add_centered_text(y, f'"{affirmations[idx]}"', 'F5', 14, 0.2)
            y -= 30
            doc.add_text(72, y, "Say it 3 times. Write it on a sticky note. Believe it!", 'F4', 11, 0.3)
        
        # Challenge
        y -= 40
        challenges = [
            "This week: Catch yourself saying 'I can't' and add 'YET' every time.",
            "Add YET to every negative statement for an entire day. Notice the shift.",
            "Make ONE mistake on purpose today. Notice: the world didn't end!",
            "Practice one skill for 30 minutes. Notice improvement vs day 1.",
            "Do something outside your comfort zone today. Report what you learned.",
            "Intentionally try something hard. When you fail, journal what you learned.",
            "Learn one new fact about the brain today. Share it with someone.",
            "Research one famous failure story and present it to your family.",
            "Write 10 positive self-talk phrases and read them every morning.",
            "Set a stretch goal for this week and track daily progress.",
            "Notice 3 times you grew today (even tiny growth counts!).",
            "Complete your first journal entry! Then do one every day this week.",
        ]
        doc.add_text(72, y, "THIS WEEK'S CHALLENGE:", 'F2', 13, 0.1)
        y -= 20
        y = add_wrapped(doc, 90, y, challenges[idx], 'F4', 11, 0.3)
        doc.new_page()

    # 30 daily journal prompts
    prompts = [
        "What is one thing I'm proud of learning recently?",
        "Describe a time I didn't give up when something was hard.",
        "What mistake did I make today? What did it teach me?",
        "Name 3 things I'm better at now than I was a year ago.",
        "What challenge am I facing? How can I break it into steps?",
        "Who inspires me? What growth mindset traits do they have?",
        "What would I attempt if I knew I couldn't fail?",
        "How did I show effort today? Rate my effort 1-10.",
        "Write about something I used to find hard that is now easy.",
        "What's one thing I want to improve at? What's my plan?",
        "Describe a failure that led to something good.",
        "What positive self-talk did I use today?",
        "What's outside my comfort zone? Am I willing to try?",
        "List 5 of my strengths. How can I use them today?",
        "What did I learn from feedback I received?",
        "How did I help someone else grow today?",
        "What's a new strategy I tried when stuck?",
        "Rate my growth mindset today: 1-10. Why that rating?",
        "What would 'future me' tell 'today me' about this challenge?",
        "Describe a moment I chose courage over comfort.",
        "What am I grateful I can learn?",
        "How did struggle lead to growth for me this week?",
        "What's one limiting belief I'm ready to let go of?",
        "Write a letter of encouragement to yourself.",
        "What growth do I want to celebrate?",
        "How will I practice growth mindset tomorrow?",
        "What did trying hard feel like today?",
        "Name someone who believes in me. How does that feel?",
        "What's my biggest growth mindset win this month?",
        "Write your growth mindset declaration for the future!",
    ]
    
    doc.add_centered_text(720, "30-DAY GROWTH MINDSET JOURNAL", 'F2', 18, 0)
    doc.add_line(150, 710, 462, 710, 1, 0.3)
    y = 680
    for i, prompt in enumerate(prompts):
        if y < 100:
            doc.new_page()
            doc.add_centered_text(720, "30-DAY JOURNAL (continued)", 'F2', 16, 0)
            y = 690
        doc.add_text(72, y, f"Day {i+1}: {prompt}", 'F2', 10, 0.1)
        y -= 18
        doc.add_text(90, y, "____________________________________________________________", 'F1', 10, 0.4)
        y -= 18
        doc.add_text(90, y, "____________________________________________________________", 'F1', 10, 0.4)
        y -= 25

    doc.new_page()
    certificate(doc, "GROWTH MINDSET CHAMPION CERTIFICATE")
    add_supplemental(doc, 'Growth Mindset', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book330_Kids_Growth_Mindset.pdf')
    print("Book330_Kids_Growth_Mindset.pdf created successfully!")

if __name__ == "__main__":
    create_book()
