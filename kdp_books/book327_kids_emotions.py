from pdf_utils import PDFDoc
from book_helpers import add_supplemental, wrap

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    title = "MY BIG FEELINGS: Understanding & Managing Emotions (Ages 6-12)"

    chapters = [
        ("What Are Emotions?", "Emotions are feelings that happen inside you. They affect how you think, act, and feel in your body.",
         "Everyone has emotions - happy, sad, angry, scared, excited, and more! Emotions are not good or bad. They are just signals that tell you something important. Like a traffic light tells drivers what to do, emotions tell you what is happening inside. Learning to understand your emotions is one of the most important skills you will ever develop.",
         ["Happy", "Surprised", "Content", "Proud"], "Take 5 deep breaths: in through your nose (4 counts), out through your mouth (6 counts)."),
        ("Anger: The Volcano Inside", "Anger is a normal emotion that everyone feels. It often happens when something seems unfair or when our boundaries are crossed.",
         "Anger can feel like a volcano building up inside you. Your face might get hot, your fists might clench, and your heart beats faster. Anger isn't bad - it tells you something needs to change. But HOW you express anger matters a lot. Yelling, hitting, or breaking things hurts others and yourself. There are much better ways to let anger out safely.",
         ["Hot face", "Tight muscles", "Fast heartbeat", "Clenched fists"], "STOP: Stop what you're doing. Take 3 deep breaths. Open your hands wide. Pick a calm response."),
        ("Sadness: It's Okay to Cry", "Sadness is a natural response to loss, disappointment, or when something doesn't go the way we hoped.",
         "Sadness might feel like a heavy weight on your chest or a gray cloud over your head. You might want to be alone, cry, or not do your usual activities. Crying is actually GOOD for you - it releases stress chemicals from your body! Everyone feels sad sometimes. The key is knowing that sadness always passes eventually, like clouds moving across the sky.",
         ["Heavy feeling", "Wanting to cry", "Low energy", "Quiet mood"], "Hug yourself tight for 30 seconds. This releases oxytocin, the comfort chemical in your brain."),
        ("Fear & Worry: The What-If Monster", "Fear is your brain's alarm system. It tries to protect you from danger - but sometimes it goes off when there's no real threat.",
         "Fear makes your body ready to fight, run away, or freeze. This was very helpful when humans had to escape from wild animals! But today, our brains sometimes treat non-dangerous things as threats - like taking a test, meeting new people, or sleeping in the dark. The What-If Monster fills your head with scary thoughts that probably won't come true.",
         ["Racing heart", "Sweaty palms", "Butterflies in stomach", "Wanting to hide"], "Ground yourself with 5-4-3-2-1: Name 5 things you SEE, 4 you TOUCH, 3 you HEAR, 2 you SMELL, 1 you TASTE."),
        ("Happiness: Sharing Joy", "Happiness is a wonderful feeling of contentment, joy, or pleasure. The best part? It's contagious!",
         "Happiness can come from big things (a birthday party!) or tiny things (a sunny day, a good joke, a hug). Scientists have found that happiness isn't about having everything you want. It's about appreciating what you have, connecting with people you love, and doing things that give you purpose. And here's a secret: sharing happiness makes it BIGGER.",
         ["Smiling", "Light feeling", "Energy", "Wanting to share"], "Write down 3 things you're grateful for right now. Gratitude is like happiness fertilizer!"),
        ("Jealousy: The Green-Eyed Monster", "Jealousy happens when we want something someone else has. It's uncomfortable but very normal.",
         "Jealousy might show up when your friend gets a new toy, when a sibling gets more attention, or when someone is better at something than you. It can feel like a burning in your chest or an angry-sad mix. The important thing to know is: someone else's success doesn't take away from YOUR worth. There's enough good stuff in the world for everyone.",
         ["Burning feeling", "Comparison thoughts", "Anger-sadness mix", "Wanting what others have"], "Turn jealousy into inspiration: Instead of 'I wish I had that,' think 'How can I work toward that?'"),
        ("Frustration: When Things Are Hard", "Frustration happens when things don't go as planned or when a task is harder than expected.",
         "Frustration is that 'UGGHH!' feeling when your homework is confusing, your game level is impossible, or your drawing doesn't look right. It makes you want to give up or throw things. But here's the truth: frustration means you're trying something challenging, and that's actually GOOD! Every expert was once frustrated. The key is taking breaks and trying different approaches.",
         ["Tension", "Wanting to quit", "Irritability", "Impatience"], "Take a 5-minute break, then return with fresh eyes. Break the hard thing into smaller, easier steps."),
        ("Loneliness: Finding Connection", "Loneliness is feeling disconnected from others, like no one understands or cares about you.",
         "You can feel lonely even in a room full of people. Loneliness is not about being alone - it's about feeling like you don't belong. Almost every kid feels lonely sometimes, especially during transitions (new school, moving, etc.). The cure for loneliness is connection: reaching out to someone, joining a group, or even being a friend to someone else who seems lonely.",
         ["Empty feeling", "Disconnection", "Sadness", "Wanting to belong"], "Reach out to one person today - call, text, or say hi. Connection is the antidote to loneliness."),
        ("Excitement: The Energy Burst", "Excitement is joyful anticipation - the bubbly, can't-sit-still feeling before something great happens!",
         "Excitement fills you with energy! Your body might feel jumpy, your thoughts race, and you might talk fast or giggle. Excitement is wonderful, but sometimes it can be overwhelming or make it hard to focus or sleep. Learning to enjoy excitement without letting it take over helps you stay balanced and present for the good things coming your way.",
         ["Bubbly energy", "Can't sit still", "Racing thoughts", "Big smile"], "Channel excitement into movement: jump, dance, or do 20 star jumps to let the energy flow!"),
        ("Embarrassment: Everyone Feels It", "Embarrassment is the hot, uncomfortable feeling when you think others are judging you negatively.",
         "Your face turns red, you want to disappear, and you might replay the moment over and over. Tripping in front of the class, getting an answer wrong, or having food on your face - everyone has embarrassing moments! The truth is: people think about your embarrassing moments WAY less than you do. Most people are too busy worrying about themselves!",
         ["Red face", "Wanting to hide", "Hot feeling", "Replay thoughts"], "Remember: in 5 years, will this moment matter? Almost always the answer is NO."),
        ("Mixed Emotions", "Sometimes you can feel two or more emotions at the same time - and that's completely normal!",
         "Have you ever felt happy AND sad at the same time? Like at the end of summer camp - you're glad to go home but sad to leave friends? These are mixed emotions. You might feel excited AND nervous about a performance. Happy for a friend AND jealous. Life is complex, and so are our emotions. All of them are valid and real.",
         ["Confusion", "Conflicting feelings", "Complexity", "Depth"], "Draw a pie chart of your emotions right now. How much of each feeling do you have? They can all exist together."),
        ("Building Emotional Strength", "Emotional strength (resilience) means being able to handle difficult emotions without falling apart.",
         "Building emotional strength is like building physical strength - it takes practice! Every time you face a hard emotion and get through it, you become stronger. Tools that help: talking to trusted people, journaling, exercise, sleep, healthy food, breathing techniques, and positive self-talk. You have already survived 100% of your bad days - that's pretty amazing!",
         ["Resilience", "Recovery", "Strength", "Growth"], "Create a Feelings First Aid Kit: list 5 things that help you feel better when emotions are big."),
    ]

    # Title page
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(650, "MY BIG FEELINGS", 'F2', 34, 0)
    doc.add_centered_text(610, "Understanding & Managing Emotions", 'F4', 18, 0.2)
    doc.add_centered_text(580, "(Ages 6-12)", 'F4', 14, 0.3)
    doc.add_line(150, 560, 462, 560, 2, 0.3)
    doc.add_centered_text(520, "A Complete Emotional Intelligence Guide for Kids", 'F1', 13, 0.3)
    doc.add_centered_text(490, "12 Chapters * Stories * Activities * Coping Strategies", 'F1', 12, 0.4)
    doc.add_centered_text(440, "Learn to understand your feelings", 'F4', 14, 0.3)
    doc.add_centered_text(410, "and handle them like a champion!", 'F4', 14, 0.3)
    doc.add_centered_text(100, f"By {author}", 'F2', 16, 0.2)
    doc.new_page()

    # Copyright
    doc.add_centered_text(600, "MY BIG FEELINGS", 'F2', 16, 0)
    doc.add_centered_text(570, "Understanding & Managing Emotions (Ages 6-12)", 'F4', 12, 0.2)
    doc.add_centered_text(530, f"Written by {author}", 'F1', 11, 0.3)
    doc.add_centered_text(510, "Copyright 2025. All rights reserved.", 'F1', 10, 0.4)
    doc.add_centered_text(470, "Published for Amazon KDP", 'F1', 10, 0.4)
    doc.add_centered_text(450, "Paperback Edition - 8.5 x 11 inches", 'F1', 10, 0.4)
    doc.new_page()

    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 20, 0)
    doc.add_line(180, 710, 432, 710, 1, 0.3)
    y = 670
    for i, (ch_title, _, _, _, _) in enumerate(chapters):
        doc.add_text(72, y, f"Chapter {i+1}: {ch_title}", 'F4', 13, 0.2)
        y -= 28
    doc.new_page()

    # Introduction
    doc.add_centered_text(720, "A NOTE TO KIDS (AND PARENTS!)", 'F2', 18, 0)
    doc.add_line(150, 710, 462, 710, 1, 0.3)
    intro_lines = [
        "Dear Reader,", "",
        "Did you know you experience about 400 different emotions EVERY DAY?",
        "That's a lot of feelings! And sometimes those feelings can be confusing,",
        "scary, or overwhelming.", "",
        "This book is your guide to understanding all those big feelings.",
        "You'll learn:", "",
        "  * What each emotion feels like in your body",
        "  * Why you have these feelings (they all have a purpose!)",
        "  * Healthy ways to manage big emotions",
        "  * Breathing exercises and calming techniques",
        "  * That you are NOT alone - everyone has these feelings!", "",
        "Remember: There are no 'bad' emotions. Every feeling is trying to",
        "tell you something important. The goal isn't to stop having feelings.",
        "The goal is to understand them and choose how to respond.", "",
        "You are braver than you believe, stronger than you seem,",
        "and smarter than you think!", "",
        "Let's explore your feelings together!",
    ]
    y = 670
    for line in intro_lines:
        doc.add_text(72, y, line, 'F4', 12, 0.2)
        y -= 22
    doc.new_page()

    # Chapters
    for ch_idx, (ch_title, subtitle, content, body_signs, coping) in enumerate(chapters):
        # Chapter title page
        doc.add_filled_rect(50, 620, 512, 110, 0.9)
        doc.add_centered_text(710, f"CHAPTER {ch_idx + 1}", 'F1', 14, 0.4)
        doc.add_centered_text(670, ch_title, 'F2', 22, 0)
        doc.add_centered_text(635, subtitle[:70], 'F4', 11, 0.3)
        if len(subtitle) > 70:
            doc.add_centered_text(618, subtitle[70:], 'F4', 11, 0.3)

        # Story
        kid_names = ["Emma", "Lucas", "Mia", "Jackson", "Aria", "Oliver", "Zara", "Liam", "Chloe", "Aiden", "Nora", "Caleb"]
        kid = kid_names[ch_idx]
        stories = [
            f"{kid} didn't understand why some days felt sunny inside and other days felt like rain. 'Why do I feel different every day?' {kid} asked Mom. 'Those are your emotions, sweetheart. Everyone has them. Let me teach you about the amazing world of feelings!' And so {kid}'s journey of emotional discovery began.",
            f"{kid} slammed the door SO hard the whole house shook. 'IT'S NOT FAIR!' The volcano inside was erupting. Dad came in quietly. 'I see you're really angry. That's okay. But the door didn't do anything wrong. Let's find a better way to let that anger out.' {kid} took a deep breath and listened.",
            f"{kid}'s best friend moved away last week. Everything felt gray. Food didn't taste good. Games weren't fun. 'I just feel so heavy,' {kid} told the school counselor. 'That heaviness is sadness, and it's completely okay to feel it. Let me show you something that might help.'",
            f"Every night, {kid} checked under the bed three times, inside the closet twice, and behind the curtains once. 'What if there's something there?' The What-If Monster was working overtime. {kid} needed to learn that most 'what-ifs' never come true - and that brave means scared but doing it anyway.",
            f"{kid} just got the best news ever - the family was going to Disney World! {kid} couldn't stop bouncing, laughing, and telling EVERYONE. This happiness was so big it needed to be shared! {kid} learned that joy grows bigger when you spread it around.",
            f"When {kid}'s little sister won the art contest, {kid} felt a weird, uncomfortable burning inside. 'I should be happy for her... but I'm NOT.' {kid} felt guilty about feeling jealous. Then {kid} learned that jealousy is normal - what matters is what you DO with it.",
            f"{kid} had been working on the puzzle for an hour. Pieces everywhere, nothing fitting. 'I'M SO STUPID!' {kid} yelled, sweeping pieces off the table. Then {kid} took a breath. 'Wait. I'm not stupid. This is just hard. And hard isn't impossible.'",
            f"At the lunch table, everyone was talking and laughing in groups. {kid} sat at the end, quiet, invisible. 'Nobody even notices me,' {kid} thought. The lonely feeling was heavy. But that day, {kid} noticed another kid sitting alone too - and decided to be brave and say hello.",
            f"{kid}'s birthday was TOMORROW! Sleep was impossible. Ideas were racing. Tomorrow! Tomorrow! TOMORROW! The excitement was so big that {kid}'s body couldn't contain it. Jumping on the bed at midnight, {kid} needed to learn how to enjoy excitement without exploding!",
            f"During show-and-tell, {kid}'s voice cracked and everyone laughed. {kid}'s face turned tomato-red. 'I wish I could disappear!' For the rest of the day, {kid} replayed that moment 100 times. But then {kid} realized something important about embarrassment...",
            f"At the end-of-year party, {kid} felt happy (school's out!), sad (won't see friends daily), nervous (what about next year?), and excited (summer plans!) ALL AT ONCE. 'Is something wrong with me?' No! Mixed emotions are completely normal and human.",
            f"When {kid} didn't make the soccer team, it felt like the end of the world. But then {kid} remembered all the other hard things survived: moving schools, losing a pet, failing a test. 'I got through all of those. I can get through this too.' That's emotional strength.",
        ]

        y = 570
        doc.add_text(72, y, f"{kid}'s STORY:", 'F2', 13, 0.1)
        y -= 25
        story = stories[ch_idx]
        words = story.split()
        lines = []
        line = ""
        for word in words:
            if len(line + " " + word) > 72:
                lines.append(line)
                line = word
            else:
                line = line + " " + word if line else word
        if line:
            lines.append(line)
        for sline in lines:
            doc.add_text(72, y, sline, 'F4', 11, 0.2)
            y -= 20

        # Main content
        y -= 20
        doc.add_text(72, y, "UNDERSTANDING THIS FEELING:", 'F2', 13, 0.1)
        y -= 25
        words = content.split()
        lines = []
        line = ""
        for word in words:
            if len(line + " " + word) > 75:
                lines.append(line)
                line = word
            else:
                line = line + " " + word if line else word
        if line:
            lines.append(line)
        for cline in lines:
            if y < 80:
                doc.new_page()
                y = 720
            doc.add_text(72, y, cline, 'F1', 11, 0.2)
            y -= 20

        doc.new_page()

        # Body signs & coping page
        doc.add_centered_text(720, f"CHAPTER {ch_idx+1}: BODY & COPING", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)

        doc.add_text(72, 670, "WHAT'S HAPPENING IN MY BODY?", 'F2', 13, 0.1)
        y = 645
        for sign in body_signs:
            doc.add_text(90, y, f"* {sign}", 'F1', 11, 0.2)
            y -= 22

        y -= 20
        doc.add_text(72, y, "COPING STRATEGY:", 'F2', 13, 0.1)
        y -= 25
        words = coping.split()
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
        for cline in lines:
            doc.add_text(90, y, cline, 'F4', 11, 0.2)
            y -= 20

        # Breathing exercise
        y -= 30
        doc.add_text(72, y, "BREATHING EXERCISE:", 'F2', 13, 0.1)
        y -= 25
        breathing = [
            "1. Sit comfortably and close your eyes",
            "2. Breathe IN through your nose for 4 counts: 1... 2... 3... 4...",
            "3. HOLD your breath for 4 counts: 1... 2... 3... 4...",
            "4. Breathe OUT through your mouth for 6 counts: 1... 2... 3... 4... 5... 6...",
            "5. Repeat 3-5 times until you feel calmer",
        ]
        for step in breathing:
            doc.add_text(90, y, step, 'F1', 11, 0.3)
            y -= 22

        # Journal prompt
        y -= 30
        doc.add_text(72, y, "JOURNAL PROMPT:", 'F2', 13, 0.1)
        y -= 25
        prompts = [
            "When was the last time I felt a big emotion? What happened?",
            "What makes me angry? How do I usually react? How could I react differently?",
            "What helps me most when I feel sad? Write about a time sadness passed.",
            "What am I most afraid of? Is it a real danger or a What-If Monster thought?",
            "What are 5 things that make me genuinely happy? Why?",
            "Have I ever felt jealous? What did I do? What could I do next time?",
            "What's something hard I didn't give up on? How did it feel to keep trying?",
            "Do I ever feel lonely? What could I do to feel more connected?",
            "What am I most excited about right now? How does my body feel?",
            "What's my most embarrassing moment? Can I laugh about it now?",
            "Write about a time you felt two emotions at once. What were they?",
            "What are 3 hard things I've survived? What did they teach me?",
        ]
        doc.add_text(90, y, prompts[ch_idx], 'F4', 11, 0.2)
        y -= 25
        doc.add_text(90, y, "_______________________________________________________________", 'F1', 11, 0.4)
        y -= 22
        doc.add_text(90, y, "_______________________________________________________________", 'F1', 11, 0.4)
        y -= 22
        doc.add_text(90, y, "_______________________________________________________________", 'F1', 11, 0.4)

        doc.new_page()

        # Activity page
        doc.add_centered_text(720, f"CHAPTER {ch_idx+1}: ACTIVITY PAGE", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        
        doc.add_text(72, 670, "DRAW YOUR EMOTION:", 'F2', 13, 0.1)
        doc.add_text(72, 650, "Draw a face showing this emotion. Then draw what this emotion", 'F1', 11, 0.3)
        doc.add_text(72, 633, "looks like as a creature or character:", 'F1', 11, 0.3)
        doc.add_rect(72, 420, 220, 200, 1, 0.5)
        doc.add_rect(320, 420, 220, 200, 1, 0.5)
        doc.add_text(140, 405, "Face", 'F1', 10, 0.5)
        doc.add_text(380, 405, "Creature", 'F1', 10, 0.5)

        doc.add_text(72, 370, "EMOTION SCALE (circle your level right now):", 'F2', 12, 0.1)
        doc.add_text(90, 345, "1 -------- 2 -------- 3 -------- 4 -------- 5 -------- 6 -------- 7 -------- 8 -------- 9 -------- 10", 'F3', 10, 0.3)
        doc.add_text(72, 325, "(calm)                                                                                              (intense)", 'F1', 9, 0.5)

        doc.add_text(72, 290, "MY CALMING TOOLKIT (list things that help you calm down):", 'F2', 12, 0.1)
        y = 265
        for i in range(5):
            doc.add_text(90, y, f"{i+1}. _______________________________________________________", 'F1', 11, 0.4)
            y -= 25

        doc.new_page()

    # Feelings Wheel page
    doc.add_centered_text(720, "MY FEELINGS WHEEL", 'F2', 18, 0)
    doc.add_centered_text(695, "Use this wheel to identify exactly what you're feeling", 'F4', 12, 0.3)
    feelings_categories = [
        ("HAPPY:", "Joyful, Grateful, Proud, Excited, Content, Hopeful, Peaceful"),
        ("SAD:", "Lonely, Disappointed, Heartbroken, Grief, Hopeless, Gloomy"),
        ("ANGRY:", "Frustrated, Irritated, Furious, Resentful, Jealous, Bitter"),
        ("SCARED:", "Anxious, Worried, Terrified, Nervous, Insecure, Panicked"),
        ("SURPRISED:", "Amazed, Confused, Shocked, Astonished, Overwhelmed"),
        ("DISGUSTED:", "Disapproving, Revolted, Uncomfortable, Judgmental"),
    ]
    y = 650
    for cat, feelings in feelings_categories:
        doc.add_text(72, y, cat, 'F2', 12, 0.1)
        doc.add_text(160, y, feelings, 'F1', 11, 0.3)
        y -= 40
    doc.new_page()

    # 30-day emotional journal
    doc.add_centered_text(720, "30-DAY FEELINGS JOURNAL", 'F2', 18, 0)
    doc.add_centered_text(695, "Check in with yourself every day!", 'F4', 12, 0.3)
    y = 660
    for day in range(1, 31):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "30-DAY FEELINGS JOURNAL (continued)", 'F2', 16, 0)
            y = 690
        doc.add_text(72, y, f"Day {day:2d}: I felt _____________ because _________________________________", 'F1', 10, 0.3)
        y -= 20
    doc.new_page()

    # Certificate
    doc.add_filled_rect(50, 250, 512, 400, 0.95)
    doc.add_rect(60, 260, 492, 380, 2, 0.3)
    doc.add_centered_text(600, "FEELINGS CHAMPION CERTIFICATE", 'F2', 20, 0)
    doc.add_centered_text(560, "This certifies that", 'F4', 14, 0.3)
    doc.add_centered_text(530, "________________________________", 'F1', 14, 0.3)
    doc.add_centered_text(500, "understands their emotions and has the tools", 'F4', 13, 0.3)
    doc.add_centered_text(475, "to handle any feeling that comes their way!", 'F4', 13, 0.3)
    doc.add_centered_text(430, "Date: _______________", 'F1', 12, 0.3)
    doc.add_centered_text(380, f"Author: {author}", 'F4', 12, 0.3)
    doc.new_page()

    add_supplemental(doc, 'Emotions', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book327_Kids_Emotions_Guide.pdf')
    print("Book327_Kids_Emotions_Guide.pdf created successfully!")

if __name__ == "__main__":
    create_book()
