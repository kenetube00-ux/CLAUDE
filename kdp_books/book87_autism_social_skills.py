"""Book 87: Social Skills Workbook for Kids with Autism"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.12)
    pdf.add_centered_text(530, "SOCIAL SKILLS", 'F2', 28, 1)
    pdf.add_centered_text(490, "WORKBOOK", 'F2', 28, 1)
    pdf.add_centered_text(448, "For Kids with Autism", 'F2', 20, 1)
    pdf.add_centered_text(410, "Activities for Ages 6-12", 'F4', 14, 0.9)
    pdf.add_centered_text(370, "Fun exercises to build confidence in social situations", 'F1', 11, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "Social Skills Workbook for Kids with Autism", 'F2', 13)
    pdf.add_centered_text(478, "Activities for Ages 6-12", 'F4', 11)

    pdf.add_centered_text(448, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(428, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(398, "A NOTE TO PARENTS AND CAREGIVERS:", 'F2', 11)
    pdf.add_centered_text(378, "This workbook uses clear, concrete language and visual supports.", 'F1', 9)
    pdf.add_centered_text(360, "Work through it together with your child at their pace.", 'F1', 9)
    pdf.add_centered_text(342, "Celebrate effort, not perfection. Every small step counts.", 'F1', 9)

    # Activity 1: Reading Facial Expressions
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 1: READING FACIAL EXPRESSIONS", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "People show their feelings on their faces. Here are clues to look for:", 'F1', 11)
    y = 680
    expressions = [
        ("HAPPY:", "Corners of mouth go UP, eyes crinkle, cheeks lift"),
        ("SAD:", "Corners of mouth go DOWN, eyebrows droop, eyes look watery"),
        ("ANGRY:", "Eyebrows come together, lips press tight, jaw clenches"),
        ("SCARED:", "Eyes go WIDE, mouth opens, eyebrows go UP"),
        ("SURPRISED:", "Eyebrows go way UP, mouth makes an O shape"),
        ("DISGUSTED:", "Nose wrinkles, upper lip goes up, eyes squint"),
        ("CONFUSED:", "One eyebrow up, head tilts, mouth might twist to one side"),
    ]
    for emotion, clues in expressions:
        pdf.add_text(72, y, emotion, 'F2', 10)
        pdf.add_text(145, y, clues, 'F1', 9)
        y -= 22
    y -= 15
    pdf.add_text(72, y, "MATCHING EXERCISE: Draw a line from the description to the feeling:", 'F2', 10)
    y -= 20
    left_items = [
        "Someone smiling with crinkly eyes",
        "Someone with a furrowed brow and tight lips",
        "Someone with wide eyes and open mouth",
        "Someone with droopy eyes looking down",
        "Someone wrinkling their nose",
    ]
    right_items = ["ANGRY", "HAPPY", "DISGUSTED", "SCARED", "SAD"]
    for i, (left, right) in enumerate(zip(left_items, right_items)):
        pdf.add_text(72, y, left, 'F1', 9)
        pdf.add_text(450, y, right, 'F2', 9)
        y -= 20

    # Activity 2: Body Language Basics
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 2: BODY LANGUAGE BASICS", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "People talk with their BODIES too, not just their words!", 'F1', 11)
    y = 680
    pdf.add_text(72, y, "PERSONAL SPACE RULER:", 'F2', 11)
    y -= 18
    spaces = [
        ("Close friends/family: About 1-2 feet (arm's length)", "This is for hugs and whispers"),
        ("Friends and classmates: About 2-4 feet", "This is for talking and playing"),
        ("Acquaintances/teachers: About 4-6 feet", "This is for classroom distance"),
        ("Strangers: 6+ feet", "This is for people you don't know"),
    ]
    for space, note in spaces:
        pdf.add_text(90, y, space, 'F1', 10)
        y -= 14
        pdf.add_text(90, y, note, 'F4', 9)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "HOW TO CHECK: If someone leans AWAY, you might be too close.", 'F2', 10)
    y -= 20
    pdf.add_text(72, y, "Body Language Signals:", 'F2', 11)
    y -= 18
    signals = [
        ("Arms crossed:", "might mean 'I don't want to talk right now'"),
        ("Turning body away:", "might mean 'I want to leave'"),
        ("Eye contact + nodding:", "means 'I'm listening'"),
        ("Looking at phone/clock:", "might mean 'I need to go'"),
        ("Leaning in:", "means 'I'm interested in what you're saying'"),
    ]
    for signal, meaning in signals:
        pdf.add_text(72, y, signal, 'F2', 9)
        pdf.add_text(210, y, meaning, 'F1', 9)
        y -= 18
    y -= 15
    pdf.add_text(72, y, "PRACTICE: What does each body language mean? Write your guess:", 'F2', 10)
    y -= 18
    practice_items = [
        "Someone yawning while you talk:",
        "Someone smiling and facing you:",
        "Someone tapping their foot fast:",
    ]
    for item in practice_items:
        pdf.add_text(72, y, item, 'F1', 9)
        pdf.add_line(72, y - 14, 540, y - 14, 0.5, 0.5)
        y -= 32

    # Activity 3: Conversation Starters
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 3: CONVERSATION STARTERS", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Starting a conversation can feel hard. Here are scripts that work!", 'F1', 11)
    y = 680
    pdf.add_text(72, y, "AT SCHOOL:", 'F2', 11)
    y -= 16
    school_scripts = [
        "'Hi! What did you do this weekend?'",
        "'That looks cool! What are you working on?'",
        "'Do you want to play with me at recess?'",
        "'I like your [backpack/shoes/shirt]. Where did you get it?'",
    ]
    for s in school_scripts:
        pdf.add_text(90, y, s, 'F4', 10)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "FILL IN THE SPEECH BUBBLE - What could you say?", 'F2', 10)
    y -= 20
    scenarios_conv = [
        "You see a kid playing alone at recess. You say:",
        "You sit next to someone new at lunch. You say:",
        "A classmate has a book you like. You say:",
    ]
    for sc in scenarios_conv:
        pdf.add_text(72, y, sc, 'F1', 9)
        y -= 14
        pdf.add_rect(90, y - 30, 420, 30, 0.5, 0.4)
        y -= 45
    y -= 10
    pdf.add_text(72, y, "CONVERSATION RULES:", 'F2', 10)
    y -= 16
    rules = [
        "1. Ask a question (shows you care about them)",
        "2. Listen to their answer (don't plan what to say next)",
        "3. Say something about what THEY said (not changing topic)",
        "4. Take turns (like a tennis game - back and forth)",
    ]
    for r in rules:
        pdf.add_text(90, y, r, 'F1', 9)
        y -= 15


    # Activity 4: Taking Turns
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 4: TAKING TURNS", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Taking turns means everyone gets a chance. It applies to:", 'F1', 11)
    y = 680
    turn_items = ["Talking in conversation", "Playing games", "Using equipment at recess",
                  "Answering questions in class", "Choosing activities"]
    for item in turn_items:
        pdf.add_text(90, y, f"- {item}", 'F1', 10)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "BOARD GAME SCENARIO: Practice taking turns!", 'F2', 11)
    y -= 18
    pdf.add_text(72, y, "Imagine you are playing a board game. Answer these:", 'F1', 10)
    y -= 20
    turn_questions = [
        "While waiting for your turn, you can:",
        "If you lose a turn, you could say:",
        "If someone takes too long, you could say:",
        "If you win, a kind thing to say is:",
        "If you lose, a good response is:",
    ]
    for q in turn_questions:
        pdf.add_text(72, y, q, 'F1', 10)
        y -= 16
        pdf.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 22

    # Activity 5: Making Friends Step-by-Step
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 5: MAKING FRIENDS STEP-BY-STEP", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    steps = [
        ("Step 1: NOTICE", "Look for someone who seems friendly (smiling, open body)"),
        ("Step 2: APPROACH", "Walk over. Stand at comfortable distance (about 3 feet)"),
        ("Step 3: GREET", "Say 'Hi!' or wave. Use their name if you know it"),
        ("Step 4: ASK", "Ask a question or give a compliment"),
        ("Step 5: LISTEN", "Pay attention to what they say. Nod to show you hear them"),
        ("Step 6: SHARE", "Share something about yourself (keep it short)"),
        ("Step 7: SUGGEST", "If it's going well: 'Do you want to [play/sit together]?'"),
        ("Step 8: ACCEPT", "If they say no, that's okay! Try someone else. You did great for trying!"),
    ]
    for step, desc in steps:
        pdf.add_text(72, y, step, 'F2', 10)
        y -= 14
        pdf.add_text(90, y, desc, 'F1', 9)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "MY FRIENDSHIP GOAL THIS WEEK:", 'F2', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    pdf.add_text(72, y, "Someone I would like to get to know better:", 'F1', 10)
    pdf.add_line(310, y - 2, 540, y - 2, 0.5, 0.5)

    # Activity 6: Handling Unexpected Changes
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 6: HANDLING UNEXPECTED CHANGES", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Sometimes plans change. That can feel really hard. Here is a plan:", 'F1', 11)
    y = 680
    pdf.add_text(72, y, "SOCIAL STORY: When Plans Change", 'F2', 11)
    y -= 18
    story = [
        "Sometimes things don't go the way I expected.",
        "This can make me feel upset, angry, or confused.",
        "These feelings are OKAY. Everyone has them.",
        "",
        "When plans change, I can:",
        "1. Take 3 deep breaths",
        "2. Tell myself: 'I can handle this'",
        "3. Ask: 'What is the new plan?'",
        "4. Think: 'What CAN I control right now?'",
        "5. Try the new plan. I might even like it!",
        "",
        "If I'm still upset, I can ask for a break.",
        "Changes are part of life. I am getting better at handling them!",
    ]
    for line in story:
        pdf.add_text(90, y, line, 'F4', 10)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "MY CHANGE PLAN:", 'F2', 10)
    y -= 16
    pdf.add_text(72, y, "When things change unexpectedly, I will:", 'F1', 9)
    y -= 14
    for i in range(3):
        pdf.add_text(72, y, f"{i+1}.", 'F1', 9)
        pdf.add_line(88, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18
    pdf.add_text(72, y, "My calm-down strategy:", 'F1', 9)
    pdf.add_line(200, y - 2, 540, y - 2, 0.5, 0.5)

    # Activity 7: Understanding Sarcasm & Jokes
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 7: UNDERSTANDING SARCASM & JOKES", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Sometimes people say the OPPOSITE of what they mean. This is sarcasm.", 'F1', 11)
    y = 680
    pdf.add_text(72, y, "CLUES THAT SOMEONE IS BEING SARCASTIC:", 'F2', 10)
    y -= 16
    clues = [
        "- Their voice goes flat or extra dramatic",
        "- They roll their eyes",
        "- What they say doesn't match the situation",
        "- They might smirk (half smile)",
    ]
    for c in clues:
        pdf.add_text(90, y, c, 'F1', 9)
        y -= 14
    y -= 10
    pdf.add_text(72, y, "EXAMPLES - What do they REALLY mean?", 'F2', 10)
    y -= 18
    sarcasm_examples = [
        ("It's raining and someone says 'Great weather!'", "They mean: the weather is BAD"),
        ("You spill milk and mom says 'Nice job!'", "She means: please be more careful"),
        ("'Oh sure, I LOVE homework'", "They mean: they don't like homework"),
    ]
    for example, meaning in sarcasm_examples:
        pdf.add_text(72, y, example, 'F4', 9)
        y -= 14
        pdf.add_text(90, y, meaning, 'F1', 9)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "YOUR TURN: What do they really mean?", 'F2', 10)
    y -= 18
    practice_sarc = [
        "'Oh wonderful, another test' means:",
        "Friend says 'Thanks a lot' sarcastically means:",
        "'I just LOVE waking up early' means:",
    ]
    for p in practice_sarc:
        pdf.add_text(72, y, p, 'F1', 9)
        pdf.add_line(72, y - 14, 400, y - 14, 0.5, 0.5)
        y -= 32

    # Activity 8: Asking for Help
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 8: ASKING FOR HELP SCRIPT", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Everyone needs help sometimes. Here's how to ask:", 'F1', 11)
    y = 680
    help_steps = [
        ("1. Get their attention:", "'Excuse me' or raise your hand or say their name"),
        ("2. Be specific:", "Say exactly what you need help with"),
        ("3. Say please:", "'Could you please help me with...'"),
        ("4. Say thank you:", "Always thank them after, even if they can't help"),
    ]
    for step, desc in help_steps:
        pdf.add_text(72, y, step, 'F2', 10)
        y -= 14
        pdf.add_text(100, y, desc, 'F4', 9)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "SCRIPTS TO PRACTICE:", 'F2', 10)
    y -= 18
    help_scripts = [
        "At school: 'Ms./Mr. ____, I don't understand the directions. Could you explain step 2?'",
        "With friends: 'Hey, could you help me with this? I'm stuck on ____.'",
        "At home: 'Mom/Dad, I need help with ____. Can you show me how?'",
        "At a store: 'Excuse me, could you help me find ____?'",
    ]
    for hs in help_scripts:
        pdf.add_text(90, y, hs, 'F1', 9)
        y -= 18
    y -= 10
    pdf.add_text(72, y, "WRITE YOUR OWN HELP SCRIPTS:", 'F2', 10)
    y -= 18
    pdf.add_text(72, y, "When I need help at school, I will say:", 'F1', 9)
    pdf.add_line(72, y - 14, 540, y - 14, 0.5, 0.5)
    y -= 35
    pdf.add_text(72, y, "When I need help with friends, I will say:", 'F1', 9)
    pdf.add_line(72, y - 14, 540, y - 14, 0.5, 0.5)


    # Activity 9: Joining a Group Activity
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 9: JOINING A GROUP", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Joining a group that's already playing can feel scary. Here's how:", 'F1', 11)
    y = 680
    join_steps = [
        "1. WATCH first (stand nearby and observe what they're doing)",
        "2. WAIT for a pause (don't interrupt in the middle)",
        "3. WALK closer (but not too close - about 3 feet away)",
        "4. ASK: 'Can I play too?' or 'Can I join?'",
        "5. If YES: Follow their rules. Don't try to change the game.",
        "6. If NO: Say 'Okay, maybe next time' and find something else.",
        "   (It's not about YOU - they might just have enough players)",
    ]
    for step in join_steps:
        pdf.add_text(72, y, step, 'F1', 10)
        y -= 18
    y -= 15
    pdf.add_text(72, y, "PRACTICE SCENARIOS: What would you do?", 'F2', 10)
    y -= 18
    scenarios_j = [
        ("Kids are playing tag at recess:", ""),
        ("Classmates are building with blocks:", ""),
        ("Friends are drawing together:", ""),
    ]
    for sc, _ in scenarios_j:
        pdf.add_text(72, y, sc, 'F1', 9)
        y -= 14
        pdf.add_text(72, y, "I would:", 'F1', 9)
        pdf.add_line(115, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22

    # Activity 10: Dealing with Bullying
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 10: DEALING WITH BULLYING", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Bullying is when someone is mean to you ON PURPOSE, more than once.", 'F1', 11)
    y = 680
    pdf.add_text(72, y, "WHAT IS BULLYING vs. WHAT IS NOT:", 'F2', 10)
    y -= 18
    pdf.add_text(72, y, "IS bullying:", 'F2', 9)
    bully_is = ["Hitting/pushing on purpose", "Name-calling repeatedly", "Leaving you out to be mean", "Spreading rumors"]
    for b in bully_is:
        pdf.add_text(90, y - 14, f"- {b}", 'F1', 9)
        y -= 14
    y -= 10
    pdf.add_text(72, y, "Is NOT bullying:", 'F2', 9)
    bully_not = ["Accidentally bumping you", "Not wanting to play once", "Disagreeing with you", "Being in a bad mood"]
    for b in bully_not:
        pdf.add_text(90, y - 14, f"- {b}", 'F1', 9)
        y -= 14
    y -= 15
    pdf.add_text(72, y, "WHAT TO DO (Responses that work):", 'F2', 10)
    y -= 16
    responses = [
        "1. Walk away (this takes away their power)",
        "2. Use a calm, firm voice: 'Stop. I don't like that.'",
        "3. Find a safe person (teacher, counselor, parent)",
        "4. Stay near other people (bullies target kids alone)",
        "5. It is NEVER your fault. You deserve to be treated with respect.",
    ]
    for r in responses:
        pdf.add_text(90, y, r, 'F1', 9)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "My safe adults I can tell:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_text(72, y, f"{i+1}.", 'F1', 9)
        pdf.add_line(88, y - 2, 300, y - 2, 0.5, 0.5)
        y -= 18

    # Activity 11: Sensory Overload Coping
    pdf.new_page()
    pdf.add_centered_text(740, "ACTIVITY 11: SENSORY OVERLOAD COPING", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Sometimes the world feels TOO MUCH - too loud, bright, or crowded.", 'F1', 11)
    pdf.add_text(72, 687, "That's called sensory overload. Here's your coping plan:", 'F1', 11)
    y = 660
    pdf.add_text(72, y, "MY SENSORY TRIGGERS (check the ones that bother you):", 'F2', 10)
    y -= 18
    triggers = [
        "Loud noises (cafeteria, assemblies)", "Bright/flashing lights",
        "Certain textures (clothing tags, food)", "Strong smells",
        "Being touched unexpectedly", "Crowded spaces",
        "Too many people talking", "Certain sounds (chewing, tapping)",
    ]
    for t in triggers:
        pdf.add_rect(72, y - 2, 8, 8, 0.5, 0.3)
        pdf.add_text(86, y, t, 'F1', 9)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "MY COPING CARDS (cut these out or copy them):", 'F2', 10)
    y -= 20
    coping_cards = [
        "CARD 1: Take 5 deep breaths. Count them on my fingers.",
        "CARD 2: Go to my quiet space (where?): ________________",
        "CARD 3: Use my noise-canceling headphones or earplugs",
        "CARD 4: Squeeze my stress ball or fidget toy",
        "CARD 5: Ask for a break: 'I need a few minutes please'",
    ]
    for card in coping_cards:
        pdf.add_rect(72, y - 5, 460, 22, 0.5, 0.4)
        pdf.add_text(78, y, card, 'F1', 9)
        y -= 30

    # Activity 12-16: School Day Social Situations (5 scenarios)
    scenarios_school = [
        ("LUNCHTIME", "You sit down and nobody talks to you.",
         ["Look for someone sitting alone and say 'Can I sit here?'",
          "Bring a conversation topic (book, game, weekend plans)",
          "It's okay to eat quietly - not every lunch needs talking"]),
        ("GROUP PROJECT", "You have to work with kids you don't know well.",
         ["Introduce yourself: 'Hi, I'm ____'",
          "Ask: 'What part do you want to do?'",
          "Listen to their ideas before sharing yours"]),
        ("RECESS", "Everyone seems to already be in groups.",
         ["Look for someone on the edges (they might want company too!)",
          "Ask to join: 'Can I play?'",
          "Start your own activity - others might join you"]),
        ("HALLWAY", "Someone you know walks by.",
         ["A simple wave or 'Hey!' is enough",
          "You don't need to have a full conversation every time",
          "Smile and keep walking - that counts as being social!"]),
        ("CLASSROOM", "The teacher asks you to work with a partner.",
         ["Turn to the nearest person and say 'Want to be partners?'",
          "If someone asks you: say 'Sure!'",
          "Take turns reading/writing/speaking"]),
    ]
    for location, situation, solutions in scenarios_school:
        pdf.new_page()
        pdf.add_centered_text(740, f"SOCIAL SITUATION: {location}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        pdf.add_text(72, 705, f"SITUATION: {situation}", 'F2', 11)
        y = 680
        pdf.add_text(72, y, "WHAT COULD YOU DO?", 'F2', 10)
        y -= 18
        for sol in solutions:
            pdf.add_text(90, y, f"- {sol}", 'F1', 10)
            y -= 16
        y -= 15
        pdf.add_text(72, y, "What would YOU do in this situation?", 'F2', 10)
        y -= 16
        for _ in range(3):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        pdf.add_text(72, y, "How would you feel? (circle one)", 'F1', 10)
        y -= 16
        pdf.add_text(90, y, "Calm    Nervous    Excited    Scared    Okay    Unsure", 'F1', 10)
        y -= 25
        pdf.add_text(72, y, "Rate your confidence to try this (1-10): _____", 'F1', 10)


    # Friendship Maintenance Checklist
    pdf.new_page()
    pdf.add_centered_text(740, "FRIENDSHIP MAINTENANCE CHECKLIST", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Friendships need care, like a plant needs water! Check what you do:", 'F1', 11)
    y = 680
    friend_tasks = [
        "I say hi to my friends when I see them",
        "I ask my friends how they're doing",
        "I remember things they told me and ask about them",
        "I invite friends to play or hang out",
        "I share things (toys, snacks, turns)",
        "I listen when they talk (even if I want to talk about my thing)",
        "I say sorry when I mess up",
        "I am happy for them when good things happen",
        "I help them when they need it",
        "I accept when they want to play with other people too",
    ]
    for task in friend_tasks:
        pdf.add_rect(72, y - 2, 8, 8, 0.5, 0.3)
        pdf.add_text(86, y, task, 'F1', 9)
        y -= 18
    y -= 15
    pdf.add_text(72, y, "My friend's name: ___________________", 'F1', 10)
    y -= 20
    pdf.add_text(72, y, "Something they like that I can ask about:", 'F1', 10)
    pdf.add_line(310, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "Something we both enjoy doing:", 'F1', 10)
    pdf.add_line(265, y - 2, 540, y - 2, 0.5, 0.5)

    # My Social Strengths
    pdf.new_page()
    pdf.add_centered_text(740, "MY SOCIAL STRENGTHS", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "You have SO MANY strengths! Check the ones that are true for you:", 'F1', 11)
    y = 680
    strengths = [
        "I am honest and say what I mean",
        "I am loyal to my friends",
        "I know a LOT about topics I love",
        "I follow the rules",
        "I notice details others miss",
        "I am kind to animals",
        "I am fair and believe in justice",
        "I can focus deeply on things I care about",
        "I am creative and think differently",
        "I am reliable - people can count on me",
    ]
    for s in strengths:
        pdf.add_rect(72, y - 2, 8, 8, 0.5, 0.3)
        pdf.add_text(86, y, s, 'F1', 10)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "My TOP strength:", 'F2', 10)
    pdf.add_line(175, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "How my strength helps me make friends:", 'F1', 10)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 18
    pdf.add_line(72, y, 540, y, 0.5, 0.5)

    # Communication Preference Card
    pdf.new_page()
    pdf.add_centered_text(740, "MY COMMUNICATION PREFERENCE CARD", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Fill this out and share with teachers/friends so they understand you:", 'F1', 10)
    y = 680
    pdf.add_rect(60, 420, 490, 270, 1, 0.3)
    pdf.add_text(72, y, "MY NAME: _______________________________", 'F2', 11)
    y -= 25
    pref_fields = [
        "I communicate best when:",
        "I need extra time to:",
        "Please DON'T:",
        "It helps me when you:",
        "When I'm overwhelmed, I need:",
        "My special interests are:",
        "The best way to get my attention:",
        "I might not look at you, but I AM listening when:",
    ]
    for pf in pref_fields:
        pdf.add_text(72, y, pf, 'F2', 9)
        y -= 14
        pdf.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 18

    # Weekly Social Goals Tracker (4 pages)
    for wk in range(1, 5):
        pdf.new_page()
        pdf.add_centered_text(740, f"WEEKLY SOCIAL GOALS - Week {wk}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        pdf.add_text(72, 710, "My social goal this week:", 'F2', 10)
        pdf.add_line(230, 708, 540, 708, 0.5, 0.5)
        y = 685
        pdf.add_text(72, y, "Day", 'F2', 8)
        pdf.add_text(110, y, "What I tried", 'F2', 8)
        pdf.add_text(300, y, "How it went", 'F2', 8)
        pdf.add_text(450, y, "Rating", 'F2', 8)
        y -= 15
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for d in days:
            pdf.add_text(72, y, d, 'F1', 9)
            pdf.add_line(110, y - 2, 290, y - 2, 0.5, 0.5)
            pdf.add_line(300, y - 2, 440, y - 2, 0.5, 0.5)
            pdf.add_line(450, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 30
        y -= 10
        pdf.add_text(72, y, "Best moment this week:", 'F2', 10)
        pdf.add_line(220, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22
        pdf.add_text(72, y, "What I want to try next week:", 'F2', 10)
        pdf.add_line(250, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22
        pdf.add_text(72, y, "I'm proud of myself for:", 'F2', 10)
        pdf.add_line(220, y - 2, 540, y - 2, 0.5, 0.5)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book87_Autism_Social_Skills.pdf')
    print("Book87_Autism_Social_Skills.pdf created successfully!")

if __name__ == "__main__":
    create_book()
