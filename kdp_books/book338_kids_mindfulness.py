from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    chapters = [
        ("What Is Mindfulness?", "Mindfulness means paying attention to the present moment on purpose, without judgment. It means noticing what is happening RIGHT NOW - what you see, hear, feel, and think - without trying to change it. Your mind naturally wanders to the past (worrying about what happened) or future (worrying about what might happen). Mindfulness brings you back to NOW, where life actually happens. It is a skill anyone can learn with practice!",
         "Sit still for 1 minute. Just breathe and notice. What do you hear? What do you feel? Where does your mind wander? Gently bring attention back to your breath each time. That's mindfulness!",
         "Draw or list 5 things you notice right now using your senses."),
        ("Mindful Breathing (5 Techniques)", "Your breath is always with you - it is the easiest mindfulness anchor. When you focus on breathing, your nervous system calms down, your heart rate slows, and your brain gets more oxygen. Here are 5 breathing techniques: 1) Belly Breathing (hand on belly, breathe so it rises), 2) 4-7-8 Breathing (in 4, hold 7, out 8), 3) Box Breathing (in 4, hold 4, out 4, hold 4), 4) Bunny Breathing (3 quick sniffs in, 1 long out), 5) Flower & Candle (smell flower in, blow candle out).",
         "Choose one technique. Practice it 3 times right now. In through nose for 4 counts, hold for 4 counts, out through mouth for 6 counts. Notice how you feel before and after.",
         "Which breathing technique is your favorite? Practice it 3 times today."),
        ("Body Scan for Kids", "A body scan means slowly paying attention to each part of your body, from toes to head. You notice how each part feels without trying to change anything. Does your forehead feel tight? Are your shoulders up by your ears? Is your tummy relaxed? A body scan helps you find where you hold stress and tension, and gently release it.",
         "Lie down comfortably. Close your eyes. Start at your toes - wiggle them, then relax. Move to feet, ankles, shins, knees... all the way up to the top of your head. Spend 5 seconds on each area.",
         "Color in a body outline showing where you feel tense (red) vs relaxed (blue)."),
        ("Mindful Eating", "How often do you eat while watching TV, playing games, or rushing? Mindful eating means paying full attention to your food. Notice its colors, smell it, feel its texture, chew slowly, and taste every flavor. When you eat mindfully, you enjoy food MORE, eat the right amount (your body tells you when it is full), and feel more satisfied afterward.",
         "Take ONE raisin (or any small food). Look at it closely for 30 seconds. Smell it. Put it on your tongue without chewing. Notice the flavor. Chew slowly - 20 chews! Notice how the taste changes.",
         "At your next meal, eat the first 5 bites mindfully - no talking, no screens, full attention."),
        ("Mindful Walking", "You walk every day but rarely NOTICE it. Mindful walking means paying attention to each step: how your feet feel hitting the ground, the sensation of movement, the air on your skin, and the world around you. Walking mindfully can be done anywhere - on the way to school, in a hallway, or in nature. It's a great way to calm down and feel grounded.",
         "Walk very slowly for 1 minute. Feel your heel touch down, then your toes. Notice weight shifting. Feel your legs move. Look around as if seeing everything for the first time.",
         "Take a 5-minute mindful walk today. Count your steps. What did you notice?"),
        ("5 Senses Grounding", "When you feel overwhelmed, anxious, or scattered, use your 5 senses to come back to the present moment. This technique is called 5-4-3-2-1 Grounding: Notice 5 things you can SEE, 4 things you can TOUCH, 3 things you can HEAR, 2 things you can SMELL, 1 thing you can TASTE. By the time you finish, your mind has returned to the present.",
         "Right now, try it: Name 5 things you see. Touch 4 different textures near you. Listen for 3 sounds. Find 2 smells. Notice 1 taste in your mouth. How do you feel now?",
         "Practice 5-4-3-2-1 grounding when you feel worried or overwhelmed today."),
        ("Dealing with Worry Mindfully", "Everyone worries sometimes. But worry is about the FUTURE - things that haven't happened (and usually won't!). Mindfulness helps with worry by bringing you back to the present, where you are safe. Instead of fighting worry or pushing it away, mindfulness teaches you to NOTICE it, name it ('Oh, that's worry'), and let it pass like a cloud in the sky.",
         "Imagine your thoughts are clouds floating across the sky. You are the sky - vast and calm. Worries are just clouds passing through. Watch them come... and go... without grabbing onto them.",
         "Next time you worry, try 'thought clouds' - watch the worry float by without grabbing it."),
        ("Anger Management Through Mindfulness", "Anger is energy! It is not bad - but it needs to be expressed safely. Mindfulness helps with anger by creating a PAUSE between the trigger and your reaction. In that pause, you can choose a response instead of reacting impulsively. Notice anger in your body first: hot face, tight jaw, clenched fists. Name it: 'I feel angry.' Then choose your response.",
         "STOP technique: S-Stop what you're doing. T-Take 3 deep breaths. O-Observe what you're feeling. P-Proceed with a wise choice. Practice this before anger peaks.",
         "Think of your last angry moment. Where did you feel it in your body? What triggered it?"),
        ("Bedtime Relaxation", "Many kids struggle to fall asleep because their minds race with thoughts. Bedtime mindfulness helps your body and mind wind down. Progressive muscle relaxation (tense then release each muscle group), body scans, counting breaths, and peaceful visualization all help signal to your brain: it's time to sleep. A calm mind leads to better sleep.",
         "Lie in bed. Squeeze your toes tight for 5 seconds, then release. Move up: calves, thighs, belly, chest, arms, hands, face. Squeeze tight, then let go. Feel yourself melting into the bed.",
         "Tonight, try progressive muscle relaxation before sleep. Rate your sleep quality tomorrow."),
        ("Gratitude Practice", "Gratitude means noticing and appreciating what is GOOD in your life. Research shows grateful people are happier, healthier, and sleep better! Mindful gratitude means really FEELING thankful, not just listing things. When you appreciate something, pause and let the warm feeling fill you up. It rewires your brain to notice more positive things.",
         "Close your eyes. Think of someone you love. Picture their face. Feel the warmth of love and gratitude for them. Let that feeling expand in your chest. Stay with it for 1 minute.",
         "Write 3 things you're grateful for. But for each one, also write WHY and how it FEELS."),
        ("Loving-Kindness Meditation", "Loving-kindness meditation involves silently sending good wishes to yourself and others. You repeat phrases like 'May I be happy. May I be safe. May I be healthy. May I live with ease.' Then you extend these wishes to loved ones, friends, difficult people, and eventually all beings. This practice increases empathy, reduces anger, and builds compassion.",
         "Sit quietly. Say to yourself: 'May I be happy. May I be peaceful. May I be safe.' Feel it. Now think of someone you love: 'May they be happy. May they be peaceful. May they be safe.'",
         "Send loving-kindness wishes to 3 people today: yourself, a friend, and someone you find difficult."),
        ("Mindful Movement (Yoga Poses)", "Yoga combines movement, breathing, and mindfulness into one practice. Simple poses help you connect body and mind, build strength and flexibility, and find calm. Key poses for kids: Mountain Pose (standing tall), Tree Pose (balance on one foot), Child's Pose (rest), Cat-Cow (spine stretch), Warrior (strength), and Corpse Pose (total relaxation).",
         "Try Mountain Pose: Stand tall, feet together, arms at sides. Feel your feet on the ground. Imagine a string pulling the top of your head toward the sky. Breathe 5 times. Feel strong and centered.",
         "Try 3 yoga poses and hold each for 5 breaths. Notice how your body and mind feel after."),
        ("Nature Mindfulness", "Nature is the perfect place to practice mindfulness because it engages all your senses. The sounds of birds, the feel of wind, the smell of grass, the sight of colors - nature pulls you into the present moment naturally. Research shows that spending time mindfully in nature reduces stress hormones, boosts immunity, and improves mood significantly.",
         "Sit outside quietly for 5 minutes. Don't use any device. Just BE in nature. What sounds do you hear? What do you smell? What do you feel on your skin? What colors do you see?",
         "Take a mindful nature walk this week. Collect 5 natural items and describe each with 3 words."),
        ("Mindfulness at School", "School can be stressful: tests, social situations, busy schedules. But mindfulness can help everywhere - even at your desk! Try: 3 deep breaths before a test. Mindful listening in class. Feeling your feet on the floor when anxious. One-minute breathing breaks between classes. Noticing without judgment when your mind wanders.",
         "Before your next test, try this: Close eyes, take 3 deep breaths, say 'I am prepared and calm,' open eyes. This reduces test anxiety and improves focus.",
         "Practice 3 mindful breaths before each class tomorrow. Notice any difference in focus."),
        ("30-Day Mindfulness Challenge", "You now have all the tools for a mindful life! This 30-day challenge gives you one simple practice per day. Remember: mindfulness is a SKILL - it gets easier with practice. Some days will be hard and your mind will wander a LOT. That is normal and okay! The practice is NOTICING the wandering and gently coming back. Every time you notice, you get stronger.",
         "Commit to just 5 minutes per day for 30 days. That's all it takes to build a life-changing habit. Mark each day you practice. Be kind to yourself on days you forget.",
         "Start Day 1 today! Set a daily reminder. Tell someone about your challenge for accountability."),
    ]

    title_page(doc, "CALM KIDS", "A Mindfulness & Meditation Guide for Children (Ages 6-12)", "15 Chapters * Guided Scripts * Activities * 30-Day Challenge")
    copyright_page(doc, "CALM KIDS: A Mindfulness & Meditation Guide")
    toc_page(doc, [c[0] for c in chapters])

    for idx, (ch_title, content, guided, activity) in enumerate(chapters):
        chapter_header(doc, idx+1, ch_title)
        y = 580
        y = add_wrapped(doc, 72, y, content, 'F1', 11, 0.2)
        doc.new_page()

        doc.add_centered_text(720, f"CHAPTER {idx+1}: PRACTICE", 'F2', 16, 0)
        doc.add_line(200, 710, 412, 710, 1, 0.3)
        
        doc.add_text(72, 680, "GUIDED PRACTICE (Read Slowly):", 'F2', 13, 0.1)
        y = add_wrapped(doc, 90, 658, guided, 'F4', 11, 0.2)
        
        y -= 30
        doc.add_text(72, y, "YOUR ACTIVITY:", 'F2', 13, 0.1)
        y -= 20
        y = add_wrapped(doc, 90, y, activity, 'F1', 11, 0.2)
        
        y -= 30
        doc.add_text(72, y, "JOURNAL REFLECTION:", 'F2', 12, 0.1)
        y -= 20
        doc.add_text(90, y, "How do I feel before practicing? ________________________________", 'F1', 10, 0.4)
        y -= 20
        doc.add_text(90, y, "How do I feel after practicing? _________________________________", 'F1', 10, 0.4)
        y -= 20
        doc.add_text(90, y, "What did I notice? _____________________________________________", 'F1', 10, 0.4)
        y -= 20
        doc.add_text(90, y, "_______________________________________________________________", 'F1', 10, 0.4)
        
        y -= 30
        doc.add_text(72, y, "DRAWING/COLORING SPACE:", 'F2', 12, 0.1)
        doc.add_rect(72, y-180, 468, 170, 1, 0.5)
        doc.add_centered_text(y-90, "Draw how you feel after mindfulness practice", 'F1', 10, 0.5)
        doc.new_page()

    # 30-day challenge pages
    doc.add_centered_text(720, "30-DAY MINDFULNESS CHALLENGE", 'F2', 18, 0)
    challenges_30 = [
        "1 min belly breathing","Body scan (head to toe)","Mindful eating (1 bite)","5-4-3-2-1 grounding","3 gratitude items",
        "Mindful walking (2 min)","Cloud watching (thoughts)","Loving-kindness (self)","Nature sit (5 min)","Mindful listening (1 min)",
        "Box breathing (5 rounds)","Progressive relaxation","Mindful coloring","Count 10 breaths","Gratitude letter",
        "Yoga poses (5 min)","Mindful shower","Loving-kindness (friend)","Worry cloud exercise","Silent minute",
        "4-7-8 breathing","Body scan before sleep","Mindful eating (full meal)","Nature walk","Compliment mindfully",
        "Breathing before test","Loving-kindness (all)","Mindful stretching","Gratitude jar entry","Full 10-min meditation",
    ]
    y = 690
    for i, ch in enumerate(challenges_30):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "30-DAY CHALLENGE (continued)", 'F2', 14, 0)
            y = 700
        doc.add_text(72, y, f"Day {i+1:2d}: [ ] {ch}   Feeling after: _______________", 'F1', 10, 0.3)
        y -= 20
    doc.new_page()

    certificate(doc, "MINDFULNESS MASTER CERTIFICATE")
    add_supplemental(doc, 'Mindfulness', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book338_Kids_Mindfulness.pdf')
    print("Book338_Kids_Mindfulness.pdf created successfully!")

if __name__ == "__main__":
    create_book()
