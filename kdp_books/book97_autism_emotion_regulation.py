"""Book 97: Autism Emotion Workbook for Kids"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.1)
    pdf.add_centered_text(530, "UNDERSTANDING", 'F2', 28, 1)
    pdf.add_centered_text(492, "MY EMOTIONS", 'F2', 28, 1)
    pdf.add_centered_text(440, "A Workbook for Kids with Autism Ages 8-14", 'F4', 15, 0.9)
    pdf.add_centered_text(395, "Emotion Identification | Body Awareness", 'F1', 12, 0.8)
    pdf.add_centered_text(375, "Calm-Down Strategies | Regulation Tools", 'F1', 12, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    pdf.add_centered_text(170, "Tools for Understanding & Managing Big Feelings", 'F1', 11, 0.7)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "Understanding My Emotions", 'F2', 14)
    pdf.add_centered_text(478, "A Workbook for Kids with Autism Ages 8-14", 'F4', 11)
    pdf.add_centered_text(445, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(425, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(395, "Designed for neurodiverse children and their caregivers.", 'F1', 9)
    pdf.add_centered_text(375, "Consult a professional for individualized support.", 'F1', 9)


    # Page 1: Emotion Thermometer
    pdf.new_page()
    pdf.add_centered_text(740, "MY EMOTION THERMOMETER", 'F2', 18)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "Color in how BIG your emotion feels right now (1 = tiny, 10 = HUGE):", 'F2', 11)
    y -= 30
    # Draw thermometer levels
    for level in range(10, 0, -1):
        gray = 0.9 - (level * 0.07)
        pdf.add_rect(200, y - 5, 200, 30, 0.5, 0.3)
        pdf.add_text(180, y + 5, f"{level}", 'F2', 14)
        labels = {10: "EXPLOSION! I can't control myself",
                  9: "About to explode - need help NOW",
                  8: "Very upset - hard to think",
                  7: "Really frustrated or sad",
                  6: "Getting uncomfortable",
                  5: "Medium - I notice something",
                  4: "A little bit bothered",
                  3: "Slightly annoyed",
                  2: "Mostly calm",
                  1: "Totally calm and relaxed"}
        pdf.add_text(410, y + 5, labels[level], 'F1', 8)
        y -= 35
    y -= 10
    pdf.add_text(72, y, "Today my emotion thermometer is at: _____", 'F2', 11)
    pdf.add_text(72, y - 18, "The emotion I feel is: ______________________", 'F1', 10)
    pdf.add_text(72, y - 36, "What made it go up: ________________________", 'F1', 10)

    # Page 2: Body Map
    pdf.new_page()
    pdf.add_centered_text(740, "WHERE DO I FEEL EMOTIONS IN MY BODY?", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "Different emotions feel different in our bodies. Draw or write where", 'F4', 10)
    pdf.add_text(72, y - 15, "YOU feel each emotion:", 'F4', 10)
    y -= 40
    emotions_body = [
        ("ANGRY:", "Hot face? Tight fists? Fast heartbeat? Tense shoulders?"),
        ("SAD:", "Heavy chest? Tired body? Lumpy throat? Stinging eyes?"),
        ("ANXIOUS:", "Butterflies in stomach? Sweaty hands? Racing heart?"),
        ("HAPPY:", "Light feeling? Warm chest? Bouncy legs? Smiling face?"),
        ("OVERWHELMED:", "Buzzing head? Tingling skin? Ringing ears? Tight all over?"),
    ]
    for emotion, hints in emotions_body:
        pdf.add_text(72, y, emotion, 'F2', 11)
        y -= 16
        pdf.add_text(90, y, hints, 'F4', 9)
        y -= 16
        pdf.add_text(90, y, "Where I feel it: _____________________________________________", 'F1', 9)
        y -= 16
        pdf.add_text(90, y, "How strong (1-10): _____", 'F1', 9)
        y -= 25
    y -= 10
    pdf.add_text(72, y, "IMPORTANT: There are no WRONG answers! Everyone's body is different.", 'F2', 10)
    pdf.add_text(72, y - 18, "Knowing where you feel emotions helps you catch them EARLY.", 'F4', 10)


    # Page 3: Identifying Emotions Vocabulary
    pdf.new_page()
    pdf.add_centered_text(740, "EMOTIONS VOCABULARY - 20 FEELINGS WORDS", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 710
    emotions_vocab = [
        ("Happy", "Feeling good, smiling, things are going well"),
        ("Sad", "Feeling down, wanting to cry, things feel heavy"),
        ("Angry", "Feeling hot, wanting to yell or hit, unfair things happened"),
        ("Scared", "Feeling afraid, wanting to run away or hide"),
        ("Anxious", "Worried about something that MIGHT happen"),
        ("Frustrated", "Trying hard but things won't work, stuck"),
        ("Excited", "Can't wait! Lots of energy, happy about something coming"),
        ("Embarrassed", "Wanting to disappear, face feels hot, others are looking"),
        ("Jealous", "Wanting what someone else has, feels unfair"),
        ("Lonely", "Feeling alone even around people, wanting connection"),
        ("Bored", "Nothing seems interesting, time goes slowly"),
        ("Overwhelmed", "Too much happening, brain overloaded, can't process"),
        ("Disappointed", "Expected something good but it didn't happen"),
        ("Proud", "Did something difficult, feeling good about myself"),
        ("Confused", "Don't understand, brain feels foggy, need help"),
        ("Calm", "Body relaxed, brain quiet, feeling peaceful"),
        ("Disgusted", "Something gross, want to get away from it"),
        ("Surprised", "Didn't expect that! Can be good or bad surprise"),
        ("Grateful", "Feeling thankful for something or someone"),
        ("Guilty", "Did something wrong, stomach feels bad, want to fix it"),
    ]
    for emotion, desc in emotions_vocab:
        pdf.add_text(72, y, f"{emotion}:", 'F2', 9)
        pdf.add_text(160, y, desc, 'F1', 8)
        y -= 17
    y -= 10
    pdf.add_text(72, y, "Circle the 5 emotions you feel MOST OFTEN.", 'F2', 10)

    # Page 4: Trigger Tracking Worksheet
    pdf.new_page()
    pdf.add_centered_text(740, "TRIGGER TRACKING WORKSHEET", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "A TRIGGER is something that makes a big emotion start.", 'F2', 11)
    pdf.add_text(72, y - 16, "When you know your triggers, you can prepare for them!", 'F4', 10)
    y -= 40
    pdf.add_text(72, y, "What happened?", 'F2', 9)
    pdf.add_text(250, y, "How I felt", 'F2', 9)
    pdf.add_text(360, y, "How big? (1-10)", 'F2', 9)
    pdf.add_text(480, y, "What I did", 'F2', 9)
    y -= 15
    for i in range(10):
        pdf.add_line(72, y, 240, y, 0.5, 0.5)
        pdf.add_line(250, y, 350, y, 0.5, 0.5)
        pdf.add_line(360, y, 470, y, 0.5, 0.5)
        pdf.add_line(480, y, 540, y, 0.5, 0.5)
        y -= 28
    y -= 10
    pdf.add_text(72, y, "MY TOP 3 TRIGGERS:", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_text(72, y, f"{i+1}.", 'F2', 10)
        pdf.add_line(90, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20

    # Page 5: Meltdown vs Tantrum Explanation
    pdf.new_page()
    pdf.add_centered_text(740, "MELTDOWN vs TANTRUM - WHAT'S THE DIFFERENCE?", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Sometimes people think a meltdown is 'bad behavior.' It is NOT.",
        "A meltdown is your brain's OVERLOAD response. Here's the difference:",
        "",
        "MELTDOWN:",
        "  - Happens when your brain gets TOO MUCH input",
        "  - You CANNOT control it (it's like a computer crashing)",
        "  - You feel WORSE during and after",
        "  - It can happen even when you're alone",
        "  - You need LESS input and a safe space to recover",
        "  - It is NOT your fault",
        "",
        "TANTRUM:",
        "  - Happens to get something you want",
        "  - Stops when you get what you want",
        "  - You're somewhat in control of it",
        "  - Needs an audience",
        "",
        "IMPORTANT MESSAGE: If you have meltdowns, you are NOT bad.",
        "Your brain processes the world differently. That's okay.",
        "The goal is to recognize the WARNING SIGNS early so you can",
        "get to a safe place BEFORE full overload.",
        "",
        "My early warning signs that a meltdown is coming:",
        "  1. ____________________________________________________",
        "  2. ____________________________________________________",
        "  3. ____________________________________________________",
        "",
        "What helps me during a meltdown:",
        "  ________________________________________________________",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17


    # Page 6: My Early Warning Signs
    pdf.new_page()
    pdf.add_centered_text(740, "MY EARLY WARNING SIGNS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "Before a BIG emotion takes over, your body gives you CLUES.", 'F2', 11)
    pdf.add_text(72, y - 16, "Check the signs that happen to YOU:", 'F4', 10)
    y -= 40
    signs = [
        "My face gets hot or red",
        "My hands make fists",
        "My stomach hurts or feels tight",
        "I feel like crying",
        "I want to run away or hide",
        "I start talking louder or faster",
        "I can't sit still / need to move",
        "I cover my ears",
        "Everything seems TOO LOUD",
        "Lights seem TOO BRIGHT",
        "I can't think of words",
        "I start picking at my skin or nails",
        "I feel dizzy or lightheaded",
        "I want to be completely alone",
        "I feel like hitting or throwing things",
    ]
    for s in signs:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, s, 'F1', 10)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "My personal warning signs not listed above:", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18

    # Page 7: Calm-Down Toolkit Builder
    pdf.new_page()
    pdf.add_centered_text(740, "MY CALM-DOWN TOOLKIT", 'F2', 18)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "When emotions get big, THESE are my tools. Choose what works for YOU:", 'F2', 10)
    y -= 22
    pdf.add_text(72, y, "BODY TOOLS (things I can DO):", 'F2', 11)
    y -= 16
    body_tools = [
        "Jump on trampoline", "Squeeze a stress ball", "Do wall push-ups",
        "Swing on swing", "Run or walk fast", "Wrap up in weighted blanket",
        "Take deep breaths (smell flowers, blow candles)", "Do animal walks (bear, crab)",
    ]
    for t in body_tools:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, t, 'F1', 9)
        y -= 16
    y -= 8
    pdf.add_text(72, y, "SENSORY TOOLS (things I can FEEL/HEAR/SEE):", 'F2', 11)
    y -= 16
    sensory_tools = [
        "Listen to calm music", "Squeeze putty or slime", "Smell a calming scent",
        "Look at a lava lamp or glitter jar", "Hold something cold (ice pack)",
        "Put on noise-canceling headphones", "Chew gum or crunchy snack",
    ]
    for t in sensory_tools:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, t, 'F1', 9)
        y -= 16
    y -= 8
    pdf.add_text(72, y, "THINKING TOOLS (things I can THINK):", 'F2', 11)
    y -= 16
    think_tools = [
        "Count backward from 20", "Name 5 blue things I can see",
        "Think about my favorite place", "Say my calm-down phrase",
        "Remember: this feeling will pass",
    ]
    for t in think_tools:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, t, 'F1', 9)
        y -= 16
    y -= 10
    pdf.add_text(72, y, "MY TOP 3 GO-TO TOOLS: 1._________ 2._________ 3._________", 'F2', 10)

    # Page 8: 5-Point Scale
    pdf.new_page()
    pdf.add_centered_text(740, "5-POINT SCALE FOR MY EMOTIONS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    pdf.add_text(72, y, "For each emotion, fill in what each level looks/feels like FOR YOU:", 'F2', 10)
    y -= 25
    # Angry scale
    pdf.add_text(72, y, "ANGRY:", 'F2', 12)
    y -= 18
    angry_levels = [
        "5 = Rage (hitting, screaming, breaking things)",
        "4 = Very angry (yelling, stomping, can't think)",
        "3 = Mad (arguing, complaining loudly)",
        "2 = Annoyed (huffing, eye-rolling, short answers)",
        "1 = Calm (no anger, relaxed, peaceful)",
    ]
    for lev in angry_levels:
        pdf.add_text(90, y, lev, 'F1', 9)
        y -= 16
    y -= 5
    pdf.add_text(90, y, "What helps me come DOWN: ________________________________", 'F1', 9)
    y -= 25
    # Anxious scale
    pdf.add_text(72, y, "ANXIOUS:", 'F2', 12)
    y -= 18
    anx_levels = [
        "5 = Panic (can't breathe, can't move, frozen)",
        "4 = Very worried (stomach hurts, want to escape)",
        "3 = Nervous (thinking about bad things happening)",
        "2 = A little uneasy (something feels off)",
        "1 = Calm (not worried at all)",
    ]
    for lev in anx_levels:
        pdf.add_text(90, y, lev, 'F1', 9)
        y -= 16
    y -= 5
    pdf.add_text(90, y, "What helps me come DOWN: ________________________________", 'F1', 9)
    y -= 25
    # Sad scale
    pdf.add_text(72, y, "SAD:", 'F2', 12)
    y -= 18
    sad_levels = [
        "5 = Crying hard, can't stop, hopeless",
        "4 = Very sad, teary, don't want to do anything",
        "3 = Down, heavy feeling, low energy",
        "2 = A little sad but managing",
        "1 = Not sad, feeling okay or happy",
    ]
    for lev in sad_levels:
        pdf.add_text(90, y, lev, 'F1', 9)
        y -= 16
    y -= 5
    pdf.add_text(90, y, "What helps me come DOWN: ________________________________", 'F1', 9)


    # Page 9: Zone of Regulation Activities
    pdf.new_page()
    pdf.add_centered_text(740, "ZONES OF REGULATION", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "All zones are OKAY. The goal is to KNOW which zone you are in", 'F4', 10)
    pdf.add_text(72, y - 14, "and have tools to get to the zone you NEED to be in.", 'F4', 10)
    y -= 35
    zones = [
        ("BLUE ZONE (low energy):", "Sad, tired, bored, sick, shut down",
         ["Move your body (jumping jacks, dancing)", "Eat a healthy snack", "Splash cold water on face",
          "Talk to someone", "Get fresh air/sunlight"]),
        ("GREEN ZONE (just right!):", "Calm, focused, happy, ready to learn",
         ["This is where we want to be for learning!", "Keep doing what's working!",
          "Notice what got you here - do more of that"]),
        ("YELLOW ZONE (heightened):", "Frustrated, anxious, excited, silly, wiggly",
         ["Deep breathing", "Take a movement break", "Use fidget tool",
          "Count to 10", "Get a drink of water"]),
        ("RED ZONE (extremely high):", "Rage, terror, meltdown, out of control",
         ["STOP - go to safe space immediately", "Use TIPP (cold water, exercise)",
          "Squeeze ice", "Do NOT try to talk or solve problems yet",
          "Wait until back in Yellow or Green to discuss"]),
    ]
    for zone_name, feelings, tools in zones:
        pdf.add_text(72, y, zone_name, 'F2', 10)
        y -= 14
        pdf.add_text(90, y, f"Feelings: {feelings}", 'F4', 9)
        y -= 14
        pdf.add_text(90, y, "Tools to use:", 'F1', 9)
        y -= 12
        for t in tools:
            pdf.add_text(105, y, f"- {t}", 'F1', 8)
            y -= 12
        y -= 12

    # Page 10: Sensory Supports for Each Emotion
    pdf.new_page()
    pdf.add_centered_text(740, "SENSORY SUPPORTS FOR EACH EMOTION", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "Different emotions need different sensory input to calm down:", 'F2', 10)
    y -= 22
    sensory_data = [
        ("When ANGRY (need to release energy):",
         ["Heavy work: push-ups, carry heavy books", "Chew crunchy food (carrots, pretzels)",
          "Rip paper or squeeze clay", "Stomp feet or march", "Scream into a pillow"]),
        ("When ANXIOUS (need to feel safe):",
         ["Deep pressure: weighted blanket, tight hug", "Slow rocking or swinging",
          "Calming scents (lavender)", "Soft music or white noise", "Small enclosed space (tent, closet)"]),
        ("When SAD (need comfort):",
         ["Warm bath or shower", "Soft textures (fuzzy blanket, stuffed animal)",
          "Gentle music", "Warm drink", "Being near a safe person (no talking needed)"]),
        ("When OVERWHELMED (need LESS input):",
         ["Noise-canceling headphones", "Dark room or sunglasses",
          "Remove yourself from the situation", "One sense at a time (focus on breathing only)",
          "Do NOT add more sensory input"]),
    ]
    for emotion, supports in sensory_data:
        pdf.add_text(72, y, emotion, 'F2', 10)
        y -= 14
        for s in supports:
            pdf.add_text(90, y, f"- {s}", 'F1', 9)
            y -= 13
        y -= 12

    # Pages 11-15: Social Stories about Big Emotions (5 scenarios)
    scenarios = [
        ("Someone Changed the Plan",
         ["Marcus was told they would go to the park after school.",
          "But when school ended, Mom said they had to go to the store first.",
          "Marcus felt his stomach get tight and his face get hot.",
          "He wanted to yell 'NO! You SAID the park!'",
          "",
          "What Marcus can do:",
          "- Take 3 deep breaths before speaking",
          "- Say: 'I'm upset because the plan changed. Can we still go to the park after?'",
          "- Remember: changed plans are not CANCELLED plans",
          "- It's OKAY to feel upset. It's NOT okay to hit or scream.",
          "",
          "What would YOU do if this happened to you?",]),
        ("Someone is Being Too Loud",
         ["Aisha is in the cafeteria. It's very loud.",
          "The noise feels like needles in her ears.",
          "Her body is getting tense and she wants to cover her ears and run.",
          "She's at a level 7 on her emotion thermometer.",
          "",
          "What Aisha can do:",
          "- Put on noise-reducing earplugs (it's okay to use them!)",
          "- Ask a teacher to eat in a quieter spot",
          "- Take 5 deep breaths to bring her level down",
          "- Leave for 2 minutes to a quiet hallway, then come back",
          "",
          "What would YOU do if this happened to you?",]),
        ("I Made a Mistake in Front of Everyone",
         ["Jordan answered a question wrong in class.",
          "Some kids laughed. Jordan's face turned red.",
          "Jordan wanted to disappear. The embarrassment was at level 8.",
          "Jordan thought: 'I'm so stupid. Everyone thinks I'm dumb.'",
          "",
          "The truth is:",
          "- EVERYONE makes mistakes. Even teachers.",
          "- Most kids forgot about it in 5 minutes",
          "- Making mistakes is how brains LEARN",
          "- One wrong answer does NOT mean you are stupid",
          "",
          "What would YOU think if you saw someone else make a mistake?",]),
        ("I Can't Stop Thinking About Something",
         ["Sam keeps thinking about something scary that MIGHT happen.",
          "The thought goes around and around like a hamster wheel.",
          "Sam can't focus on anything else. Anxiety is at level 6.",
          "Sam's stomach hurts and hands are sweaty.",
          "",
          "What Sam can do:",
          "- Name it: 'I'm having a worry thought'",
          "- Ask: 'Is this happening RIGHT NOW?' (Usually no!)",
          "- Do the 5-4-3-2-1 grounding (5 things I see, 4 hear, etc.)",
          "- Tell a trusted adult: 'I can't stop worrying about...'",
          "",
          "What helps YOU when your brain gets stuck on a thought?",]),
        ("Someone Won't Play With Me",
         ["Alex asked three kids to play at recess. They all said no.",
          "Alex feels sad and lonely. The feeling is at level 6.",
          "Alex thinks: 'Nobody likes me. I'll never have friends.'",
          "",
          "The truth is:",
          "- Sometimes people say no for reasons that aren't about you",
          "- They might already be in the middle of a game",
          "- One day of 'no' doesn't mean 'never'",
          "- You can: ask different people, play alone (that's okay too!),",
          "  or ask a teacher to help you join a group",
          "",
          "What would YOU do if this happened to you?",]),
    ]
    for title, lines in scenarios:
        pdf.new_page()
        pdf.add_centered_text(740, f"SOCIAL STORY: {title.upper()}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        y = 710
        for line in lines:
            pdf.add_text(72, y, line, 'F4', 10)
            y -= 16
        y -= 10
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.5)


    # Page 16: Cool-Down Sequence Cards
    pdf.new_page()
    pdf.add_centered_text(740, "COOL-DOWN SEQUENCE (Do These Steps in Order!)", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    steps = [
        ("STEP 1: STOP", "Freeze your body. Don't do anything yet."),
        ("STEP 2: NAME IT", "What emotion am I feeling? How big is it (1-10)?"),
        ("STEP 3: BREATHE", "Smell the flowers (in through nose 4 counts).\nBlow out the candles (out through mouth 6 counts). Do this 3 times."),
        ("STEP 4: CHOOSE A TOOL", "Pick ONE tool from your toolkit.\nDo it for at least 2 minutes."),
        ("STEP 5: CHECK", "Am I calmer? If yes, great! If no, try a different tool."),
        ("STEP 6: THINK", "Now that I'm calmer, what do I need? Do I need:\n- To talk to someone?  - To be alone?  - To solve a problem?"),
        ("STEP 7: ACT", "Now you can respond. Use calm words.\nRemember: you can feel angry AND still be kind."),
    ]
    for step_title, desc in steps:
        pdf.add_filled_rect(72, y - 10, 468, 40, 0.93)
        pdf.add_text(80, y + 10, step_title, 'F2', 11)
        lines = desc.split('\n')
        for i, line in enumerate(lines):
            pdf.add_text(80, y - 5 - i * 12, line, 'F1', 9)
        y -= 55
    y -= 10
    pdf.add_text(72, y, "Practice this sequence EVERY DAY when calm so it becomes automatic!", 'F2', 9)

    # Page 17: After the Storm Reflection
    pdf.new_page()
    pdf.add_centered_text(740, "AFTER THE STORM - REFLECTION PAGE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "Fill this out AFTER you've calmed down from a big emotion:", 'F2', 10)
    y -= 22
    fields = [
        ("Date:", "____________"),
        ("What happened (just the facts):", ""),
        ("", "_______________________________________________"),
        ("", "_______________________________________________"),
        ("What emotion did I feel?", "_________________________________"),
        ("How big was it (1-10)?", "_____"),
        ("What did my body feel like?", "______________________________"),
        ("What did I DO?", "_________________________________________"),
        ("Did my reaction help or make things worse?", "______________"),
        ("What tool from my toolkit could I try next time?", ""),
        ("", "_______________________________________________"),
        ("Am I okay now? (circle)", "YES  /  MOSTLY  /  NOT YET"),
        ("Do I need to talk to someone?", "YES  /  NO"),
        ("Do I need to apologize to anyone?", "YES  /  NO  (Who? __________)"),
        ("", ""),
        ("IMPORTANT: Having big emotions does NOT make you bad.", ""),
        ("You are learning. Every time you practice, it gets easier.", ""),
    ]
    for label, fill in fields:
        if label and fill:
            pdf.add_text(72, y, f"{label} {fill}", 'F1', 10)
        elif label:
            pdf.add_text(72, y, label, 'F2', 10)
        else:
            pdf.add_text(72, y, fill, 'F1', 10)
        y -= 18

    # Page 18: My Safe Person/Place
    pdf.new_page()
    pdf.add_centered_text(740, "MY SAFE PERSON & SAFE PLACE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "MY SAFE PEOPLE (adults I trust when emotions are big):", 'F2', 11)
    y -= 22
    for i in range(4):
        pdf.add_text(72, y, f"Person {i+1}: ___________________  Where to find them: ______________", 'F1', 10)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "What I need from my safe person:", 'F2', 11)
    y -= 16
    needs = [
        "Just sit with me quietly (don't talk)",
        "Give me a hug or deep pressure",
        "Help me use my breathing",
        "Take me to my safe place",
        "Help me problem-solve AFTER I'm calm",
    ]
    for n in needs:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, n, 'F1', 9)
        y -= 18
    y -= 15
    pdf.add_text(72, y, "MY SAFE PLACE (where I can go to calm down):", 'F2', 11)
    y -= 18
    pdf.add_text(72, y, "At home: _____________________________________________________", 'F1', 10)
    y -= 20
    pdf.add_text(72, y, "At school: ___________________________________________________", 'F1', 10)
    y -= 20
    pdf.add_text(72, y, "Other: _______________________________________________________", 'F1', 10)
    y -= 25
    pdf.add_text(72, y, "What I need in my safe place:", 'F2', 10)
    y -= 16
    safe_items = ["Quiet (no loud noises)", "Dim lighting", "Soft things to touch",
                  "Space to move", "Weighted blanket or cushions", "Headphones"]
    for item in safe_items:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, item, 'F1', 9)
        y -= 16


    # Pages 19-23: Emotion Journal Pages (5 pages)
    for pg in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(740, f"MY EMOTION JOURNAL - Page {pg}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        y = 710
        for entry in range(3):
            pdf.add_text(72, y, f"Date: __________  Time: __________", 'F1', 9)
            y -= 16
            pdf.add_text(72, y, "Emotion: __________________  Level (1-10): _____", 'F1', 9)
            y -= 16
            pdf.add_text(72, y, "What happened: ___________________________________________", 'F1', 9)
            y -= 16
            pdf.add_text(72, y, "Tool I used: ______________________________________________", 'F1', 9)
            y -= 16
            pdf.add_text(72, y, "Did it help? (circle)  YES  /  A LITTLE  /  NO", 'F1', 9)
            y -= 16
            pdf.add_text(72, y, "Level after using tool (1-10): _____", 'F1', 9)
            y -= 25
            pdf.add_line(72, y, 540, y, 0.5, 0.3)
            y -= 18

    # Page 24: My Regulation Plan
    pdf.new_page()
    pdf.add_centered_text(740, "MY EMOTION REGULATION PLAN", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    pdf.add_text(72, y, "This is MY plan. I made it. I can use it anytime.", 'F2', 11)
    y -= 25
    pdf.add_text(72, y, "My name: ____________________________", 'F1', 11)
    y -= 22
    pdf.add_text(72, y, "My biggest emotion challenge: _________________________________", 'F1', 10)
    y -= 22
    pdf.add_text(72, y, "My #1 trigger: ________________________________________________", 'F1', 10)
    y -= 22
    pdf.add_text(72, y, "My early warning signs: ________________________________________", 'F1', 10)
    y -= 22
    pdf.add_text(72, y, "My 3 best calm-down tools:", 'F2', 11)
    y -= 18
    for i in range(3):
        pdf.add_text(72, y, f"{i+1}. ________________________________________________________", 'F1', 10)
        y -= 20
    y -= 5
    pdf.add_text(72, y, "My safe place: ________________________________________________", 'F1', 10)
    y -= 22
    pdf.add_text(72, y, "My safe person: _______________________________________________", 'F1', 10)
    y -= 22
    pdf.add_text(72, y, "My calm-down phrase: __________________________________________", 'F1', 10)
    y -= 22
    pdf.add_text(72, y, "(Examples: 'This will pass' / 'I can handle this' / 'I am safe')", 'F4', 9)
    y -= 22
    pdf.add_text(72, y, "I WILL ask for help when my level reaches: _____", 'F2', 10)
    y -= 22
    pdf.add_text(72, y, "I deserve to feel calm and happy. I am learning every day.", 'F5', 11)

    # Page 25: Message to the Child
    pdf.new_page()
    pdf.add_centered_text(740, "A MESSAGE FOR YOU", 'F5', 18)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    message = [
        "Dear Reader,",
        "",
        "Having big emotions is not a bad thing.",
        "It means you feel things deeply. That is a STRENGTH.",
        "",
        "Your brain works differently from some other kids.",
        "That does not mean it works WRONG.",
        "It means the world wasn't designed for your brain,",
        "so you have to work a little harder sometimes.",
        "That's not fair. But you are stronger than you know.",
        "",
        "Some days will be hard. Some days you will feel",
        "overwhelmed or frustrated or sad.",
        "That's okay. Those feelings will pass.",
        "",
        "You are not 'too much.'",
        "You are not 'broken.'",
        "You are not 'bad.'",
        "",
        "You are a person who is LEARNING.",
        "And every single day you practice,",
        "it gets a tiny bit easier.",
        "",
        "Be patient with yourself.",
        "You are doing great.",
        "",
        "- This workbook believes in you.",
    ]
    for line in message:
        pdf.add_text(100, y, line, 'F4', 12)
        y -= 20

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book97_Autism_Emotion_Workbook.pdf')
    print("Book97_Autism_Emotion_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
