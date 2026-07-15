from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    chapters = [
        ("You Are Unique & That's Great", "There are nearly 8 billion people on Earth, and not a SINGLE one is exactly like you. Your combination of thoughts, talents, experiences, humor, and heart is completely one-of-a-kind. That's not just a nice thing to say - it's a scientific fact! Your fingerprints, voice print, and DNA are unique. Even identical twins are different people! Being unique isn't weird - it's your SUPERPOWER.",
         "Look at your thumbprint. No one who has ever lived or ever WILL live has that same print. You are literally irreplaceable.",
         "Think about this: if everyone were the same, the world would be incredibly boring. Differences make life interesting!",
         ["List 10 things that make you uniquely YOU", "What can you do that nobody else does quite the same way?", "Draw yourself as a superhero. What's your unique superpower?"]),
        ("Knowing Your Strengths", "Everyone has strengths - things they're naturally good at or have worked hard to develop. Maybe you're creative, kind, funny, athletic, smart, musical, brave, or patient. Knowing your strengths gives you confidence because you focus on what you CAN do instead of what you can't. Strengths aren't just academics - being a good friend is a strength!",
         "Make a list of 20 strengths. Can't think of 20? Ask 3 people who know you well. You'll be surprised what others see in you that you don't notice yourself!",
         "Your strengths are like tools in a toolbox. Different situations require different tools. The key is knowing which ones you have.",
         ["List your top 10 strengths (ask family/friends for help!)", "How did you develop each strength? Practice? Natural talent? Both?", "How can you use your strengths to help others this week?"]),
        ("Dealing with Comparison", "Comparing yourself to others is a happiness thief! Social media makes it worse because people only show their best moments. When you compare your behind-the-scenes to someone else's highlight reel, you'll always feel bad. The ONLY fair comparison is you vs. yesterday's you. Are you growing? That's all that matters.",
         "Comparison is like measuring a fish by its ability to climb a tree. Everyone has different starting points, challenges, and paths. Your journey is YOURS.",
         "Instead of 'They're better than me,' try 'They're good at that, AND I'm good at other things.'",
         ["Identify 3 comparisons you make often. Are they fair?", "Go 24 hours without comparing yourself to anyone", "For every person you admire, find something YOU have that they might admire"]),
        ("Social Media and Self-Image", "Social media shows a fake version of reality. Filters, angles, editing, and selective posting mean what you see is NOT real life. Studies show the more time kids spend on social media, the lower their self-esteem. This doesn't mean social media is evil - but you need to use it WISELY. Unfollow accounts that make you feel bad. Follow ones that inspire you.",
         "For every 'perfect' photo you see, remember: they took 47 versions, chose the best one, filtered it, and probably still don't think it's good enough.",
         "Limit social media time and notice how you FEEL while scrolling. If it makes you feel worse, put it down!",
         ["Track: how do you feel BEFORE and AFTER 30 min of social media?", "Unfollow 5 accounts that make you feel bad about yourself", "Post something REAL (no filter) and notice: the world doesn't end!"]),
        ("Handling Criticism", "Criticism stings, but it doesn't define you. There are two types: CONSTRUCTIVE (meant to help you improve) and DESTRUCTIVE (meant to hurt). Learn to tell the difference. Constructive criticism is a GIFT - it helps you grow. Destructive criticism says more about the critic than about you. Don't let anyone's words become your inner voice.",
         "Before reacting to criticism, ask: 1) Is this person trying to help me? 2) Is there any truth I can learn from? 3) Would I say this to a friend?",
         "You are not what others say about you. You are what you repeatedly do and believe about yourself.",
         ["Think of criticism that hurt. Was it constructive or destructive?", "Write a 'criticism filter': questions to ask before taking it personally", "Practice responding to criticism calmly: 'Thanks for the feedback. I'll think about it.'"]),
        ("Positive Self-Talk: Your Inner Voice", "You talk to yourself more than anyone else talks to you - about 60,000 thoughts per day! If that inner voice is constantly negative ('I'm stupid,' 'I can't do anything right,' 'Nobody likes me'), it becomes your reality. But you can CHANGE your inner voice! Replace negative thoughts with realistic, positive ones. It feels fake at first but rewires your brain over time.",
         "Notice negative self-talk and literally say 'STOP.' Then replace it: 'I'm stupid' becomes 'I'm still learning.' 'Nobody likes me' becomes 'The right people appreciate me.'",
         "Your brain believes what you tell it repeatedly. Choose your words to yourself as carefully as you'd choose words for your best friend.",
         ["Write 10 negative thoughts you have, then rewrite each one positively", "Put positive affirmations on sticky notes around your mirror", "For one day, treat yourself as kindly as you'd treat your best friend"]),
        ("Body Confidence", "Your body is AMAZING regardless of its shape or size. It carries you through life, heals when injured, lets you hug people you love, and does billions of things automatically. Body confidence isn't about looking a certain way - it's about appreciating what your body CAN DO rather than only how it looks. Every body is a good body.",
         "Focus on FUNCTION not APPEARANCE: My legs carry me. My arms hug. My brain thinks. My heart beats 100,000 times daily without me thinking about it. That's miraculous!",
         "The 'ideal body' has changed every decade in history. It's a social construct, not a health standard.",
         ["List 10 amazing things your body does for you every day", "Stop negative body talk for one full week - notice the difference", "Move your body for FUN, not punishment. What movement brings you JOY?"]),
        ("Academic Confidence", "You don't have to be perfect in school to be smart! Intelligence has many forms: logical, creative, musical, physical, social, emotional, and more. If you struggle with math, you might excel at writing. If science is hard, maybe you're gifted in art. Academic confidence comes from effort, not just grades. Celebrate PROGRESS, not just perfection.",
         "Einstein failed an entrance exam. Darwin was called 'lazy' by teachers. Thomas Edison's teacher said he was 'too stupid to learn.' Grades don't measure your worth OR your future success.",
         "Focus on learning, not just performing. Ask: Am I understanding more today than yesterday? That's success.",
         ["Identify your strongest type of intelligence (there are 8 types!)", "Set a growth goal: 'I will improve at ___ by ___'", "Ask for help in your weak areas - it's smart, not weak"]),
        ("Social Confidence", "Social confidence means feeling comfortable around others - not being the loudest or most popular. It means: being yourself, starting conversations, handling awkward moments, and knowing your worth regardless of others' opinions. Social skills IMPROVE with practice! Every confident person was once nervous too.",
         "Social confidence isn't about impressing everyone. It's about being genuine and knowing that the right people will appreciate the REAL you.",
         "Tip: Focus on making OTHERS comfortable. When you stop worrying about yourself and help others relax, YOUR nervousness disappears!",
         ["Practice making eye contact and smiling at 5 people today", "Start one conversation with someone you don't know well", "Remember: most people are too worried about themselves to judge you"]),
        ("Trying New Things", "Fear of failure stops people from trying new things - and that's the BIGGEST failure of all! Everything you're good at now was once something you'd never tried. The first time you rode a bike, you probably fell. The first time you swam, you sank. Growth requires trying things badly at first. Give yourself permission to be a beginner!",
         "The 'comfort zone' is a real thing - but nothing grows there! Think of your comfort zone as a tiny circle. Every new thing you try makes that circle BIGGER.",
         "No one starts as an expert. Every master was once a disaster. The only way to get good at something is to be willing to be bad at it first.",
         ["List 5 things you want to try but are afraid to", "This week, do ONE thing that scares you a little", "After trying, rate your fear 1-10 before vs after. It always drops!"]),
        ("Standing Up for Yourself", "Self-esteem means knowing you DESERVE respect - from others AND from yourself. Standing up for yourself isn't being mean or aggressive. It's calmly and clearly saying 'That's not okay' when someone crosses a line. You can be kind AND have boundaries. People with healthy self-esteem don't let others treat them badly.",
         "Assertiveness formula: 'I feel [emotion] when you [behavior]. I need [what you want instead].' Practice it until it feels natural.",
         "You teach people how to treat you. If you accept disrespect, you'll get more of it. If you calmly assert your boundaries, people learn to respect you.",
         ["Write 3 boundaries that are important to you", "Practice saying 'No' without apologizing (in front of a mirror)", "The next time someone crosses a line, use the assertiveness formula"]),
        ("Daily Confidence Builders", "Self-esteem isn't built in one day - it's built daily through small, consistent actions. This chapter gives you 30 days of confidence-building activities. Each one takes just 5-10 minutes but compounds over time. Think of it like exercise for your self-worth. Do one every day and watch yourself transform over a month!",
         "Consistency beats intensity. Five minutes daily beats one hour monthly. Small daily deposits of self-love add up to massive self-esteem over time.",
         "Self-esteem is not something you find once and keep forever. It's something you practice and maintain, like brushing your teeth. Make it a habit!",
         ["Commit to the 30-day challenge starting TODAY", "Get an accountability partner to do it with you", "Track how you feel on day 1 vs day 30 - expect amazing changes!"]),
    ]

    title_page(doc, "I AM AWESOME", "Building Self-Esteem & Confidence for Kids (Ages 7-12)", "12 Chapters * Stories * Activities * Affirmations * 30-Day Challenge")
    copyright_page(doc, "I AM AWESOME: Building Self-Esteem & Confidence")
    toc_page(doc, [c[0] for c in chapters])

    # Intro
    doc.add_centered_text(720, "A MESSAGE FOR YOU", 'F2', 18, 0)
    y = add_wrapped(doc, 72, 680, "Before you turn another page, I want you to know something important: You are enough. Right now. As you are. Not when you get better grades, not when you're more popular, not when you lose or gain weight. RIGHT NOW. This book will help you believe that truth deep in your bones. Self-esteem isn't about thinking you're better than others - it's about knowing you're worthy of love, respect, and happiness. You already are. Let's build on that foundation together.", 'F4', 12, 0.2)
    doc.new_page()

    for idx, (ch_title, content, mirror_ex, science, activities) in enumerate(chapters):
        chapter_header(doc, idx+1, ch_title)
        y = 580
        y = add_wrapped(doc, 72, y, content, 'F1', 11, 0.2)
        doc.new_page()

        # Mirror exercise + activities
        doc.add_centered_text(720, f"CHAPTER {idx+1}: BUILD YOUR CONFIDENCE", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        
        doc.add_text(72, 685, "MIRROR EXERCISE:", 'F2', 12, 0.1)
        y = add_wrapped(doc, 90, 665, mirror_ex, 'F4', 11, 0.2)
        
        y -= 20
        doc.add_text(72, y, "THE SCIENCE:", 'F2', 12, 0.1)
        y -= 18
        y = add_wrapped(doc, 90, y, science, 'F1', 10, 0.3)
        
        y -= 20
        doc.add_text(72, y, "ACTIVITIES:", 'F2', 12, 0.1)
        y -= 18
        for i, act in enumerate(activities):
            y = add_wrapped(doc, 90, y, f"{i+1}. {act}", 'F1', 10, 0.2, 68)
            y -= 10
        
        # Affirmation card
        y -= 20
        affirmations = [
            "I am unique, valuable, and irreplaceable.",
            "My strengths make me capable of amazing things.",
            "I don't need to be like anyone else to be worthy.",
            "What I see online is not real life. I am enough offline.",
            "Criticism helps me grow. It does not define me.",
            "I choose kind, encouraging thoughts about myself.",
            "My body is amazing for all it does, not how it looks.",
            "My intelligence shows in many different ways.",
            "I am worthy of friendship and connection just as I am.",
            "Being a beginner at something is brave, not embarrassing.",
            "I deserve respect, and I set healthy boundaries.",
            "Every day, I grow stronger and more confident.",
        ]
        doc.add_filled_rect(60, y-40, 492, 45, 0.95)
        doc.add_rect(62, y-38, 488, 41, 1, 0.3)
        doc.add_centered_text(y-20, f'AFFIRMATION: "{affirmations[idx]}"', 'F5', 12, 0.1)
        doc.new_page()

    # 30-day confidence challenge
    doc.add_centered_text(720, "30-DAY CONFIDENCE CHALLENGE", 'F2', 18, 0)
    doc.add_centered_text(695, "Do one each day. Watch your confidence grow!", 'F4', 11, 0.3)
    daily = [
        "Look in the mirror and say 3 nice things about yourself",
        "Write down 5 things you're proud of accomplishing",
        "Give someone a genuine compliment",
        "Try something new (even if small)",
        "Say 'no' to something you don't want to do",
        "Write a letter of appreciation to yourself",
        "Stand in a 'power pose' for 2 minutes",
        "List 10 things your body can do that you're grateful for",
        "Start a conversation with someone new",
        "Celebrate a mistake - what did it teach you?",
        "Wear something that makes you feel confident",
        "Help someone without expecting anything back",
        "Write your strengths on sticky notes around your room",
        "Do something you're good at and enjoy it fully",
        "Forgive yourself for something you've been holding onto",
        "Ask for help with something (it takes strength!)",
        "Spend 10 minutes doing something just for YOU",
        "Write down a fear, then do it anyway (if safe)",
        "Read your affirmations out loud with conviction",
        "Unfollow one social media account that makes you feel bad",
        "Make eye contact and smile at 10 people today",
        "Write 'I am enough' 10 times. Mean it.",
        "Do 5 minutes of positive visualization (picture success)",
        "Thank your body for something it did today",
        "Set one boundary today. Hold it.",
        "Record yourself saying something kind about you. Play it back.",
        "Notice one negative thought. Replace it immediately.",
        "Do something kind for yourself (rest, treat, nature)",
        "Tell someone you trust something you're insecure about",
        "Write: 'I am awesome because...' Fill a whole page!",
    ]
    y = 665
    for i, d in enumerate(daily):
        if y < 75:
            doc.new_page()
            doc.add_centered_text(720, "30-DAY CHALLENGE (continued)", 'F2', 14, 0)
            y = 700
        doc.add_text(72, y, f"Day {i+1:2d}: [ ] {d}", 'F1', 9, 0.3)
        y -= 19
    doc.new_page()

    # Strengths list page
    doc.add_centered_text(720, "MY AWESOME STRENGTHS LIST", 'F2', 18, 0)
    doc.add_centered_text(695, "Fill this page with things you're good at - ask friends & family!", 'F4', 11, 0.3)
    y = 665
    for i in range(20):
        doc.add_text(72, y, f"{i+1:2d}. ________________________________________________________", 'F1', 10, 0.4)
        y -= 22
        if y < 75:
            doc.new_page()
            y = 720
    doc.new_page()

    # Compliment jar page
    doc.add_centered_text(720, "MY COMPLIMENT COLLECTION", 'F2', 18, 0)
    doc.add_centered_text(695, "Write down every compliment you receive. Read on hard days!", 'F4', 11, 0.3)
    y = 660
    for i in range(12):
        doc.add_rect(72, y-55, 225, 55, 1, 0.4)
        doc.add_rect(315, y-55, 225, 55, 1, 0.4)
        y -= 70
        if y < 60:
            doc.new_page()
            y = 720
    doc.new_page()

    certificate(doc, "I AM AWESOME CERTIFICATE")
    add_supplemental(doc, 'Self-Esteem', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book345_Kids_Self_Esteem.pdf')
    print("Book345_Kids_Self_Esteem.pdf created successfully!")

if __name__ == "__main__":
    create_book()
