from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, "HEALING YOUR INNER CHILD", 'F2', 17)
pdf.add_centered_text(455, "A Guided Workbook for Adults", 'F4', 13)
pdf.add_centered_text(370, "Reconnect, Nurture, and Heal", 'F4', 11)
pdf.add_centered_text(355, "the Child Within You", 'F4', 11)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, "HEALING YOUR INNER CHILD", 'F2', 12)
pdf.add_centered_text(475, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)
pdf.add_centered_text(450, "This workbook is for educational purposes.", 'F4', 9)

# Page 3: What is Inner Child Work
pdf.new_page()
pdf.add_centered_text(610, "WHAT IS INNER CHILD WORK?", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
text = [
    "Your 'inner child' is the part of you that still carries the",
    "emotions, memories, and needs from childhood. When childhood needs",
    "went unmet, wounds formed that still affect you as an adult.",
    "",
    "SIGNS YOUR INNER CHILD NEEDS HEALING:",
    "- You have a harsh inner critic",
    "- You struggle with self-worth",
    "- You people-please or over-give",
    "- You feel guilty for having needs",
    "- You have difficulty playing or having fun",
    "- You fear abandonment or rejection",
    "- You struggle to trust others",
    "- You have difficulty setting boundaries",
    "",
    "WHAT INNER CHILD WORK IS NOT:",
    "- It is not about blaming your parents",
    "- It is not about staying stuck in the past",
    "- It is not about being immature",
    "",
    "WHAT IT IS:",
    "- Acknowledging what you missed",
    "- Giving yourself what you needed then",
    "- Reparenting yourself with compassion",
    "- Integrating all parts of who you are"
]
for line in text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 4: Letter from Adult Self to Child Self
pdf.new_page()
pdf.add_centered_text(610, "LETTER FROM YOUR ADULT SELF", 'F2', 14)
pdf.add_centered_text(593, "to Your Inner Child", 'F1', 11)
pdf.add_line(50, 583, 382, 583)
y = 560
pdf.add_text(50, y, "Dear Little Me,", 'F5', 11)
y -= 20
pdf.add_text(50, y, "Write what your child self needed to hear:", 'F4', 9)
y -= 18
for _ in range(25):
    pdf.add_line(50, y, 380, y, 0.5, 0.6)
    y -= 16
y -= 5
pdf.add_text(50, y, "With all my love, Your Grown-Up Self", 'F5', 10)

# Page 5: Childhood Timeline
pdf.new_page()
pdf.add_centered_text(610, "CHILDHOOD TIMELINE", 'F2', 14)
pdf.add_centered_text(593, "Key Events Ages 0-18", 'F1', 10)
pdf.add_line(50, 583, 382, 583)
y = 565
ages = ["Ages 0-3:", "Ages 4-6:", "Ages 7-9:", "Ages 10-12:", "Ages 13-15:", "Ages 16-18:"]
for age in ages:
    pdf.add_text(50, y, age, 'F2', 10)
    y -= 15
    pdf.add_text(50, y, "Key event: ", 'F4', 9)
    pdf.add_line(110, y-2, 380, y-2, 0.5, 0.5)
    y -= 14
    pdf.add_text(50, y, "How I felt: ", 'F4', 9)
    pdf.add_line(110, y-2, 380, y-2, 0.5, 0.5)
    y -= 14
    pdf.add_text(50, y, "What I needed: ", 'F4', 9)
    pdf.add_line(125, y-2, 380, y-2, 0.5, 0.5)
    y -= 14
    pdf.add_text(50, y, "Did I get it? ", 'F4', 9)
    pdf.add_line(120, y-2, 380, y-2, 0.5, 0.5)
    y -= 20

# Page 6: Unmet Needs Identification
pdf.new_page()
pdf.add_centered_text(610, "UNMET NEEDS IDENTIFICATION", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
needs = [
    "Every child has core needs. Check the ones that went UNMET for you:",
    "",
    "SAFETY NEEDS:",
    "__ Physical safety (freedom from abuse/violence)",
    "__ Emotional safety (freedom from criticism/shaming)",
    "__ Predictability (consistent routines, stable home)",
    "",
    "VALIDATION NEEDS:",
    "__ Being seen and acknowledged",
    "__ Having feelings accepted (not dismissed or mocked)",
    "__ Being told 'I'm proud of you'",
    "",
    "COMFORT NEEDS:",
    "__ Physical affection (hugs, being held)",
    "__ Comfort when scared or hurt",
    "__ Someone to turn to in distress",
    "",
    "PLAY NEEDS:",
    "__ Freedom to be creative and messy",
    "__ Unstructured play time",
    "__ Joy and laughter in the home",
    "",
    "BOUNDARY NEEDS:",
    "__ Having my 'no' respected",
    "__ Age-appropriate responsibilities (not parentified)",
    "__ Privacy and personal space",
    "",
    "My deepest unmet need was: _____________________",
    "How this shows up in my adult life: _____________"
]
for line in needs:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14


# Pages 7-11: Reparenting Exercises (5 pages)
reparenting = [
    ("REPARENTING: SAFETY", [
        "Your inner child needs to know they are SAFE with you now.",
        "",
        "PRACTICE: Close your eyes. Visualize your child self in a scary",
        "moment. Now imagine your adult self walking in.",
        "What do you say to reassure them?",
        "_______________________________________________",
        "What do you DO to make them feel safe?",
        "_______________________________________________",
        "",
        "DAILY SAFETY AFFIRMATIONS:",
        "- I am safe now. The danger has passed.",
        "- I protect myself. I am my own guardian.",
        "- I create safe spaces for myself.",
        "- I choose safe people to be around.",
        "",
        "THIS WEEK I WILL CREATE SAFETY BY:",
        "_______________________________________________",
        "_______________________________________________"
    ]),
    ("REPARENTING: VALIDATION", [
        "Your inner child needs to know their feelings MATTER.",
        "",
        "PRACTICE: Think of a childhood memory where your feelings",
        "were dismissed. What did you feel?",
        "_______________________________________________",
        "Now validate that feeling as your adult self:",
        "'Of course you felt ________. That makes sense because",
        "________. Your feelings are real and important.'",
        "",
        "VALIDATION SCRIPTS TO USE DAILY:",
        "- It makes sense that I feel this way.",
        "- My emotions are valid information.",
        "- I don't need anyone's permission to feel.",
        "- Feeling this doesn't make me weak.",
        "",
        "TODAY I VALIDATE MYSELF FOR:",
        "_______________________________________________",
        "_______________________________________________"
    ]),
    ("REPARENTING: COMFORT", [
        "Your inner child needs to be COMFORTED when hurting.",
        "",
        "PRACTICE: Place your hand on your heart or wrap your arms",
        "around yourself. Say: 'I'm here. You're not alone anymore.'",
        "",
        "COMFORT MENU (choose what soothes you):",
        "__ Warm bath or shower",
        "__ Soft blanket and cozy space",
        "__ Gentle music or nature sounds",
        "__ Warm drink (tea, cocoa)",
        "__ Journaling your feelings",
        "__ Talking to a safe person",
        "__ Being in nature",
        "__ Creative expression (art, music)",
        "",
        "When I'm hurting, I will comfort myself by:",
        "_______________________________________________",
        "",
        "I no longer need to suffer in silence."
    ]),
    ("REPARENTING: PLAY", [
        "Your inner child needs PLAY and JOY.",
        "",
        "Many adults with wounded inner children forgot how to play.",
        "Play is not frivolous - it is ESSENTIAL for healing.",
        "",
        "WHAT DID YOU LOVE TO DO AS A CHILD?",
        "_______________________________________________",
        "_______________________________________________",
        "",
        "PLAY IDEAS FOR ADULTS:",
        "- Color, paint, or draw (no skill required!)",
        "- Dance like nobody's watching",
        "- Build something with your hands",
        "- Play a sport or game just for fun",
        "- Explore somewhere new with curiosity",
        "- Sing loudly, even badly",
        "- Watch cartoons or read children's books",
        "- Play with animals",
        "",
        "THIS WEEK I WILL PLAY BY:",
        "_______________________________________________",
        "I give myself permission to have fun without guilt."
    ]),
    ("REPARENTING: BOUNDARIES", [
        "Your inner child needs to learn that 'NO' is a complete sentence.",
        "",
        "If your boundaries were violated as a child, you may struggle",
        "with boundaries as an adult. This is not your fault.",
        "",
        "BOUNDARIES I NEEDED AS A CHILD BUT DIDN'T HAVE:",
        "_______________________________________________",
        "_______________________________________________",
        "",
        "BOUNDARIES I NEED NOW AS AN ADULT:",
        "With family: __________________________________",
        "At work: _____________________________________",
        "In relationships: _____________________________",
        "With myself: __________________________________",
        "",
        "BOUNDARY AFFIRMATIONS:",
        "- I am allowed to say no without guilt.",
        "- My needs are not too much.",
        "- I don't have to earn love by being useful.",
        "- I can love someone AND have boundaries.",
        "",
        "One boundary I will set this week:",
        "_______________________________________________"
    ])
]
for title, lines in reparenting:
    pdf.new_page()
    pdf.add_centered_text(610, title, 'F2', 13)
    pdf.add_line(50, 600, 382, 600)
    y = 575
    for line in lines:
        pdf.add_text(50, y, line, 'F4', 10)
        y -= 15


# Page 12: Core Wound Identification
pdf.new_page()
pdf.add_centered_text(610, "CORE WOUND IDENTIFICATION", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
wounds = [
    "Core wounds are deep beliefs formed in childhood that drive",
    "adult behavior patterns. Which resonate with you?",
    "",
    "__ ABANDONMENT: 'People always leave me.'",
    "   Pattern: clinging, jealousy, fear of being alone",
    "",
    "__ REJECTION: 'I'm not good enough to be loved.'",
    "   Pattern: people-pleasing, over-achieving, hiding true self",
    "",
    "__ BETRAYAL: 'I can't trust anyone.'",
    "   Pattern: controlling, hypervigilant, walls up",
    "",
    "__ UNWORTHINESS: 'I don't deserve good things.'",
    "   Pattern: self-sabotage, settling, not asking for needs",
    "",
    "__ INVISIBILITY: 'I don't matter.'",
    "   Pattern: staying quiet, over-giving, losing self in others",
    "",
    "My primary core wound: _________________________",
    "When I first learned this belief: _______________",
    "How it affects me today: _______________________",
    "The truth to replace it: _______________________"
]
for line in wounds:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 13: Family Dynamics Mapping
pdf.new_page()
pdf.add_centered_text(610, "FAMILY DYNAMICS MAPPING", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
family = [
    "Understanding family roles helps you see patterns clearly.",
    "",
    "MY ROLE IN THE FAMILY WAS:",
    "__ The Hero (responsible, achieving, 'perfect' child)",
    "__ The Scapegoat (blamed, acted out, black sheep)",
    "__ The Lost Child (invisible, quiet, withdrawn)",
    "__ The Mascot (funny, distracted from family pain)",
    "__ The Caretaker (parentified, took care of adults)",
    "",
    "FAMILY COMMUNICATION STYLE:",
    "__ Open and honest  __ Avoidant/silent",
    "__ Volatile/explosive  __ Passive-aggressive",
    "",
    "UNSPOKEN FAMILY RULES I GREW UP WITH:",
    "(Examples: Don't cry. Don't ask for help. Be perfect.)",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "",
    "WHICH OF THESE RULES DO I STILL FOLLOW?",
    "_______________________________________________",
    "",
    "NEW RULES I CHOOSE FOR MYSELF:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________"
]
for line in family:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 14: Forgiveness Work
pdf.new_page()
pdf.add_centered_text(610, "FORGIVENESS WORK", 'F2', 14)
pdf.add_centered_text(593, "(Not Condoning)", 'F1', 10)
pdf.add_line(50, 583, 382, 583)
y = 560
forgive = [
    "Forgiveness is not saying what happened was okay.",
    "Forgiveness is releasing its power over your present.",
    "",
    "WHAT I NEED TO FORGIVE:",
    "Person: _______________________________________",
    "What they did/didn't do: _______________________",
    "How it affected me: ____________________________",
    "",
    "STAGES OF FORGIVENESS (it's a process):",
    "1. Acknowledge the harm fully (don't minimize)",
    "2. Feel the feelings (anger, grief, betrayal)",
    "3. Understand (not excuse) their limitations",
    "4. Choose to release (for YOUR freedom, not theirs)",
    "5. Repeat as needed (it's not a one-time event)",
    "",
    "I AM READY TO RELEASE:",
    "_______________________________________________",
    "",
    "SELF-FORGIVENESS:",
    "I forgive myself for: __________________________",
    "I was doing the best I could with what I had.",
    "",
    "What I know now that I didn't know then:",
    "_______________________________________________"
]
for line in forgive:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 15: Nurturing Daily Practice
pdf.new_page()
pdf.add_centered_text(610, "NURTURING YOUR INNER CHILD DAILY", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
nurture = [
    "Healing happens in small daily moments, not big breakthroughs.",
    "",
    "MORNING RITUAL (choose 1-2):",
    "- Place hand on heart: 'Good morning, little one. I'm here.'",
    "- Look in mirror with compassion, not criticism",
    "- Do something joyful before responsibilities",
    "",
    "THROUGHOUT THE DAY:",
    "- When stressed: 'What do you need right now?'",
    "- When triggered: 'I've got you. We're safe.'",
    "- When criticized: 'Their opinion doesn't define us.'",
    "- When lonely: 'You're never alone. I'm always here.'",
    "",
    "EVENING RITUAL (choose 1-2):",
    "- Review the day with self-compassion",
    "- Thank your inner child for being brave today",
    "- Cozy bedtime routine (what you wished for as a child)",
    "",
    "MY PERSONAL DAILY PRACTICE:",
    "Morning: _____________________________________",
    "Midday check-in: ______________________________",
    "Evening: ______________________________________",
    "",
    "Commitment: I will practice for ___ days in a row."
]
for line in nurture:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 16: Integration Exercises
pdf.new_page()
pdf.add_centered_text(610, "INTEGRATION EXERCISES", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
integ = [
    "Integration means bringing your inner child and adult self",
    "together as one whole person.",
    "",
    "EXERCISE 1: Dialogue with Your Inner Child",
    "Adult: 'How are you feeling today?'",
    "Child: ________________________________________",
    "Adult: 'What do you need from me?'",
    "Child: ________________________________________",
    "Adult: 'I promise you...'",
    "Child: ________________________________________",
    "",
    "EXERCISE 2: Photo Exercise",
    "Find a photo of yourself as a child. Look at that child.",
    "What do you feel when you see them? ______________",
    "What do you want to say to them? ________________",
    "_______________________________________________",
    "",
    "EXERCISE 3: Non-Dominant Hand Writing",
    "Write a question with your dominant hand.",
    "Answer with your non-dominant hand (accesses child brain).",
    "Question: _____________________________________",
    "Answer: _______________________________________",
    "",
    "EXERCISE 4: Inner Child Meditation",
    "Visualize meeting your younger self. Give them what they need.",
    "What happened: _________________________________"
]
for line in integ:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Pages 17-19: Inner Child Meditation Scripts (3 pages)
meditations = [
    ("MEDITATION 1: MEETING YOUR INNER CHILD", [
        "Find a comfortable position. Close your eyes. Take 3 deep breaths.",
        "",
        "Imagine walking down a path into a beautiful, safe garden.",
        "The sun is warm. The air is gentle. You feel completely safe here.",
        "",
        "In the center of the garden, you see a child sitting alone.",
        "As you get closer, you recognize them - it's you, at age ___.",
        "",
        "Notice how they look. What are they wearing? How do they seem?",
        "Are they happy? Sad? Scared? Lonely?",
        "",
        "Approach them gently. Kneel down to their level.",
        "Look into their eyes with love.",
        "",
        "Say: 'Hi. I'm you, all grown up. I came to see you.'",
        "Notice their reaction. Let them respond however they need to.",
        "",
        "Say: 'I want you to know that everything is going to be okay.",
        "You survive. You grow. And I'm here to take care of you now.'",
        "",
        "Offer them a hug if they want one. Sit with them as long as",
        "you need. When ready, promise to return, and slowly come back."
    ]),
    ("MEDITATION 2: THE SAFE ROOM", [
        "Close your eyes. Breathe deeply three times.",
        "",
        "Imagine you are building a room just for your inner child.",
        "This room is the safest place in the universe.",
        "",
        "What color are the walls? _____________________",
        "What's on the floor? (soft carpet? pillows?) ___",
        "What comforting items are there? _______________",
        "What sounds fill the room? ____________________",
        "What does it smell like? ______________________",
        "",
        "Your inner child enters the room and looks around.",
        "They smile. They feel safe here. This is THEIRS.",
        "",
        "Tell them: 'This room is always here for you. Whenever you",
        "feel scared or overwhelmed, you can come here. No one can",
        "hurt you here. I built this just for you.'",
        "",
        "Watch them settle in. Notice how their body relaxes.",
        "Stay as long as you need. This room exists inside you forever."
    ]),
    ("MEDITATION 3: GIVING THEM WHAT THEY NEEDED", [
        "Close your eyes. Breathe deeply. Ground yourself in the present.",
        "",
        "Think of a specific childhood memory where you needed something",
        "and didn't get it. Let the scene form clearly.",
        "",
        "Now imagine your adult self stepping INTO that memory.",
        "You are strong, capable, and full of love.",
        "",
        "What does your child self need in this moment?",
        "Safety? Comfort? Someone to stand up for them? Permission to cry?",
        "",
        "Give it to them. In your imagination, give them EXACTLY",
        "what they needed. Hold them. Protect them. Speak for them.",
        "",
        "Say: 'I am sorry this happened to you. You didn't deserve it.",
        "I am here now. I will always be here now.'",
        "",
        "Feel the healing happening. Your child self relaxes.",
        "They know they are not alone anymore. They never will be again.",
        "",
        "Slowly bring your awareness back. Place hand on heart. Breathe."
    ])
]
for title, lines in meditations:
    pdf.new_page()
    pdf.add_centered_text(610, title, 'F2', 12)
    pdf.add_line(50, 597, 382, 597)
    y = 575
    for line in lines:
        pdf.add_text(50, y, line, 'F4', 10)
        y -= 15


# Page 20: Healing Affirmations
pdf.new_page()
pdf.add_centered_text(610, "MY HEALING AFFIRMATIONS", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
affs = [
    "Read these daily. Say them to your inner child:",
    "",
    "- I am safe now. The past cannot hurt me anymore.",
    "- I deserve love without earning it.",
    "- My feelings are valid and important.",
    "- I am allowed to take up space.",
    "- I can be imperfect and still be loved.",
    "- I don't have to be useful to be worthy.",
    "- My needs matter.",
    "- I am allowed to rest without guilt.",
    "- Joy is my birthright.",
    "- I am healing, and that is enough for today.",
    "",
    "MY OWN AFFIRMATIONS (write what YOUR inner child needs):",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "4. ____________________________________________",
    "5. ____________________________________________"
]
for line in affs:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 21: Progress Reflection
pdf.new_page()
pdf.add_centered_text(610, "PROGRESS REFLECTION", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
progress = [
    "Look back at how far you've come.",
    "",
    "When I started this workbook, I felt:",
    "_______________________________________________",
    "_______________________________________________",
    "",
    "Now I feel:",
    "_______________________________________________",
    "_______________________________________________",
    "",
    "The most important thing I learned:",
    "_______________________________________________",
    "_______________________________________________",
    "",
    "The hardest exercise for me was:",
    "_______________________________________________",
    "Because: ______________________________________",
    "",
    "My relationship with my inner child is now:",
    "_______________________________________________",
    "",
    "One thing I want to continue practicing:",
    "_______________________________________________",
    "",
    "A message from my inner child to my adult self:",
    "_______________________________________________",
    "_______________________________________________",
    "",
    "You showed up for the child within you.",
    "That child is so proud of who you've become."
]
for line in progress:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book104_Inner_Child_Workbook.pdf')
print("Book104_Inner_Child_Workbook.pdf created successfully!")
