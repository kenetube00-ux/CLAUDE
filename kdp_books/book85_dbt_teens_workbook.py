"""Book 85: DBT Skills Workbook for Teens"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.13)
    pdf.add_centered_text(520, "DBT SKILLS WORKBOOK", 'F2', 28, 1)
    pdf.add_centered_text(480, "FOR TEENS", 'F2', 28, 1)
    pdf.add_centered_text(430, "Manage Big Emotions with Confidence", 'F4', 16, 0.9)
    pdf.add_centered_text(380, "Mindfulness + Distress Tolerance +", 'F1', 11, 0.8)
    pdf.add_centered_text(362, "Emotion Regulation + Interpersonal Effectiveness", 'F1', 11, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "DBT Skills Workbook for Teens", 'F2', 13)
    pdf.add_centered_text(478, "Manage Big Emotions with Confidence", 'F4', 11)

    pdf.add_centered_text(448, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(428, "This workbook is for educational purposes only.", 'F1', 9)
    pdf.add_centered_text(408, "It is not a substitute for professional therapy.", 'F1', 9)
    pdf.add_centered_text(388, "If you are in crisis, text HOME to 741741 (Crisis Text Line).", 'F2', 9)
    pdf.add_centered_text(358, "WHAT IS DBT?", 'F2', 11)
    pdf.add_centered_text(338, "Dialectical Behavior Therapy teaches you skills to handle", 'F1', 9)
    pdf.add_centered_text(322, "intense emotions without making things worse.", 'F1', 9)

    # Chapter 1: What is DBT
    pdf.new_page()
    pdf.add_centered_text(740, "WHAT IS DBT?", 'F2', 18)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    dbt_intro = [
        "DBT stands for Dialectical Behavior Therapy. It was created by Dr. Marsha",
        "Linehan to help people who experience very intense emotions.",
        "",
        "'Dialectical' means holding two things that seem opposite at the same time:",
        "  - I am doing my best AND I can do better.",
        "  - I accept myself AND I want to change.",
        "  - This moment is painful AND it will pass.",
        "",
        "DBT has FOUR main skill areas:",
        "",
        "1. MINDFULNESS - Being present in the moment without judgment",
        "2. DISTRESS TOLERANCE - Surviving crisis without making it worse",
        "3. EMOTION REGULATION - Understanding and managing your feelings",
        "4. INTERPERSONAL EFFECTIVENESS - Getting what you need from relationships",
        "",
        "HOW TO USE THIS WORKBOOK:",
        "- Work through one section at a time",
        "- Practice each skill before moving on",
        "- There are no grades - this is for YOU",
        "- It's okay to come back to skills you've already learned",
        "- The more you practice, the more automatic these skills become",
    ]
    y = 705
    for line in dbt_intro:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17

    # Mindfulness Skills (3 pages)
    # Page 1: Observe
    pdf.new_page()
    pdf.add_centered_text(740, "MINDFULNESS: OBSERVE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Observe means noticing without labeling or judging.", 'F2', 11)
    pdf.add_text(72, 685, "Like a camera - just record what's there.", 'F1', 10)
    y = 655
    pdf.add_text(72, y, "EXERCISE: 5-4-3-2-1 Grounding", 'F2', 11)
    y -= 20
    senses = [
        ("5 things you can SEE:", 5),
        ("4 things you can TOUCH:", 4),
        ("3 things you can HEAR:", 3),
        ("2 things you can SMELL:", 2),
        ("1 thing you can TASTE:", 1),
    ]
    for prompt, count in senses:
        pdf.add_text(72, y, prompt, 'F2', 10)
        y -= 18
        for i in range(count):
            pdf.add_text(90, y, f"{i+1}.", 'F1', 9)
            pdf.add_line(105, y - 2, 400, y - 2, 0.5, 0.5)
            y -= 16
        y -= 8
    pdf.add_text(72, y, "How do you feel after this exercise? (1-10 calm): _____", 'F1', 10)


    # Page 2: Describe
    pdf.new_page()
    pdf.add_centered_text(740, "MINDFULNESS: DESCRIBE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Describe means putting words to your experience - just the facts.", 'F2', 11)
    pdf.add_text(72, 685, "Instead of 'I'm angry' try 'I notice a hot feeling in my chest.'", 'F1', 10)
    y = 655
    pdf.add_text(72, y, "EXERCISE: Describe Without Judging", 'F2', 11)
    y -= 20
    scenarios = [
        "Someone doesn't text you back. Describe the FACTS (not your story):",
        "You get a bad grade. Describe what actually happened:",
        "A friend cancels plans. Describe only what you observe:",
    ]
    for sc in scenarios:
        pdf.add_text(72, y, sc, 'F1', 10)
        y -= 18
        for _ in range(2):
            pdf.add_line(90, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
    pdf.add_text(72, y, "JUDGMENT vs. DESCRIPTION:", 'F2', 11)
    y -= 18
    pdf.add_text(72, y, "Judgment", 'F2', 9)
    pdf.add_text(300, y, "Description (rewrite)", 'F2', 9)
    y -= 15
    judgments = ["She's so rude", "This is the worst day ever", "I'm stupid", "Nobody likes me", "Everything is unfair"]
    for j in judgments:
        pdf.add_text(72, y, j, 'F4', 9)
        pdf.add_line(300, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22

    # Page 3: Participate
    pdf.new_page()
    pdf.add_centered_text(740, "MINDFULNESS: PARTICIPATE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Participate means fully throwing yourself into the moment.", 'F2', 11)
    pdf.add_text(72, 685, "Not watching from the sidelines - BEING in the experience.", 'F1', 10)
    y = 655
    pdf.add_text(72, y, "EXERCISE: Mindful Activities Log", 'F2', 11)
    pdf.add_text(72, y - 18, "This week, try doing these activities with FULL attention:", 'F1', 10)
    y -= 40
    activities = [
        "Eating a meal (no phone)", "Listening to one full song with eyes closed",
        "Walking and noticing each step", "Having a conversation without multitasking",
        "Drawing or doodling for 5 minutes", "Doing one chore with full focus",
    ]
    for act in activities:
        pdf.add_rect(72, y - 2, 8, 8, 0.5, 0.3)
        pdf.add_text(86, y, act, 'F1', 10)
        pdf.add_text(380, y, "How did it feel?", 'F1', 8)
        pdf.add_line(450, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 25
    y -= 15
    pdf.add_text(72, y, "My favorite mindful activity: ________________________________", 'F1', 10)
    y -= 25
    pdf.add_text(72, y, "What I noticed when I was fully present:", 'F1', 10)
    y -= 18
    for _ in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18


    # Distress Tolerance (4 pages)
    # Page 1: TIPP Skills
    pdf.new_page()
    pdf.add_centered_text(740, "DISTRESS TOLERANCE: TIPP SKILLS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "When emotions hit 8-10 intensity, use TIPP to calm your body FAST:", 'F2', 11)
    y = 680
    tipp = [
        ("T - Temperature", "Hold ice cubes, splash cold water on face, or take a cold shower.", "This activates the dive reflex and slows your heart rate."),
        ("I - Intense Exercise", "Run, do jumping jacks, or sprint up stairs for 5-10 minutes.", "Burns off the adrenaline your body is producing."),
        ("P - Paced Breathing", "Breathe out LONGER than you breathe in (in 4, out 6-8).", "Activates your parasympathetic nervous system."),
        ("P - Paired Muscle Relaxation", "Tense each muscle group while breathing in, release while breathing out.", "Tells your body: the danger has passed."),
    ]
    for title, desc, why in tipp:
        pdf.add_text(72, y, title, 'F2', 11)
        y -= 16
        pdf.add_text(90, y, desc, 'F4', 9)
        y -= 14
        pdf.add_text(90, y, why, 'F1', 9)
        y -= 25
    y -= 10
    pdf.add_text(72, y, "MY TIPP PLAN (fill in for YOUR crisis moments):", 'F2', 11)
    y -= 20
    pdf.add_text(72, y, "My T strategy:", 'F1', 10)
    pdf.add_line(170, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "My I strategy:", 'F1', 10)
    pdf.add_line(170, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "My P (breathing) strategy:", 'F1', 10)
    pdf.add_line(220, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "My P (muscle) strategy:", 'F1', 10)
    pdf.add_line(210, y - 2, 540, y - 2, 0.5, 0.5)

    # Page 2: Self-Soothe with 5 Senses
    pdf.new_page()
    pdf.add_centered_text(740, "DISTRESS TOLERANCE: SELF-SOOTHE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Self-soothing means being KIND to yourself when you're hurting.", 'F2', 11)
    pdf.add_text(72, 685, "Build your personal self-soothe kit using all 5 senses:", 'F1', 10)
    y = 655
    senses_list = [
        ("SIGHT", "What calms you to look at? (nature, art, photos, candles)"),
        ("SOUND", "What soothes you to hear? (music, rain, podcasts, silence)"),
        ("SMELL", "What scents comfort you? (candles, perfume, food, nature)"),
        ("TASTE", "What tastes bring comfort? (tea, chocolate, mints, fruit)"),
        ("TOUCH", "What feels good? (soft blanket, hot bath, fidget toy, pet)"),
    ]
    for sense, prompt in senses_list:
        pdf.add_text(72, y, f"{sense}:", 'F2', 11)
        pdf.add_text(130, y, prompt, 'F1', 9)
        y -= 18
        pdf.add_text(90, y, "My choices:", 'F1', 9)
        y -= 14
        pdf.add_text(90, y, "1.", 'F1', 9)
        pdf.add_line(105, y - 2, 280, y - 2, 0.5, 0.5)
        pdf.add_text(290, y, "2.", 'F1', 9)
        pdf.add_line(305, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 25
    y -= 10
    pdf.add_text(72, y, "MY SELF-SOOTHE KIT (items I will keep ready):", 'F2', 10)
    y -= 18
    for i in range(5):
        pdf.add_text(72, y, f"{i+1}.", 'F1', 9)
        pdf.add_line(88, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18


    # Page 3: Pros and Cons
    pdf.new_page()
    pdf.add_centered_text(740, "DISTRESS TOLERANCE: PROS AND CONS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "When you want to act on urges, weigh the pros and cons FIRST.", 'F2', 11)
    pdf.add_text(72, 685, "My urge/crisis behavior: _______________________________________", 'F1', 10)
    y = 655
    pdf.add_rect(72, y - 5, 220, 150, 0.5, 0.3)
    pdf.add_rect(320, y - 5, 220, 150, 0.5, 0.3)
    pdf.add_text(82, y + 140, "PROS of acting on urge", 'F2', 9)
    pdf.add_text(330, y + 140, "CONS of acting on urge", 'F2', 9)
    y -= 170
    pdf.add_rect(72, y - 5, 220, 150, 0.5, 0.3)
    pdf.add_rect(320, y - 5, 220, 150, 0.5, 0.3)
    pdf.add_text(82, y + 140, "PROS of resisting urge", 'F2', 9)
    pdf.add_text(330, y + 140, "CONS of resisting urge", 'F2', 9)
    y -= 180
    pdf.add_text(72, y, "After looking at this, my wisest choice is:", 'F2', 10)
    pdf.add_line(72, y - 18, 540, y - 18, 0.5, 0.5)
    pdf.add_line(72, y - 36, 540, y - 36, 0.5, 0.5)

    # Page 4: Radical Acceptance
    pdf.new_page()
    pdf.add_centered_text(740, "DISTRESS TOLERANCE: RADICAL ACCEPTANCE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Radical acceptance means accepting reality AS IT IS - not approving of it.", 'F2', 10)
    pdf.add_text(72, 685, "Pain + Non-acceptance = SUFFERING. Pain + Acceptance = just pain.", 'F1', 10)
    y = 655
    pdf.add_text(72, y, "Things I cannot change (and need to accept):", 'F2', 11)
    y -= 18
    for i in range(4):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "Turning the Mind: When I catch myself fighting reality, I will:", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "ACCEPTANCE STATEMENTS (check ones that help you):", 'F2', 10)
    y -= 18
    statements = [
        "This is what happened. I cannot change the past.",
        "Fighting reality doesn't change it - it only adds suffering.",
        "I can accept AND still work toward change.",
        "This moment is painful but it is not permanent.",
        "I didn't cause this, but I can choose how to respond.",
        "Acceptance is not approval.",
    ]
    for st in statements:
        pdf.add_rect(72, y - 2, 8, 8, 0.5, 0.3)
        pdf.add_text(86, y, st, 'F4', 9)
        y -= 18

    # Emotion Regulation (4 pages)
    # Page 1: Naming Emotions
    pdf.new_page()
    pdf.add_centered_text(740, "EMOTION REGULATION: NAMING EMOTIONS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "You can't manage what you can't name. Expand your emotion vocabulary!", 'F2', 10)
    y = 680
    emotion_groups = [
        ("ANGER family:", "irritated, frustrated, annoyed, furious, bitter, resentful"),
        ("SADNESS family:", "disappointed, lonely, hopeless, grief, empty, heartbroken"),
        ("FEAR family:", "worried, anxious, panicked, terrified, insecure, nervous"),
        ("JOY family:", "content, excited, proud, grateful, peaceful, amused"),
        ("SHAME family:", "embarrassed, guilty, humiliated, inadequate, exposed"),
        ("DISGUST family:", "repulsed, contempt, judgmental, revolted"),
    ]
    for group, words in emotion_groups:
        pdf.add_text(72, y, group, 'F2', 10)
        pdf.add_text(180, y, words, 'F1', 9)
        y -= 22
    y -= 15
    pdf.add_text(72, y, "EMOTION LOG - Practice naming your emotions this week:", 'F2', 10)
    y -= 18
    pdf.add_text(72, y, "Day", 'F2', 8)
    pdf.add_text(110, y, "Emotion Name", 'F2', 8)
    pdf.add_text(230, y, "Intensity (1-10)", 'F2', 8)
    pdf.add_text(350, y, "What triggered it?", 'F2', 8)
    y -= 15
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        pdf.add_text(72, y, d, 'F1', 9)
        pdf.add_line(110, y - 2, 220, y - 2, 0.5, 0.5)
        pdf.add_line(230, y - 2, 340, y - 2, 0.5, 0.5)
        pdf.add_line(350, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20


    # Emotion Regulation Page 2: Opposite Action
    pdf.new_page()
    pdf.add_centered_text(740, "EMOTION REGULATION: OPPOSITE ACTION", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "When your emotion doesn't fit the facts, do the OPPOSITE of what it urges.", 'F2', 10)
    y = 680
    opposites = [
        ("EMOTION", "URGE", "OPPOSITE ACTION"),
        ("Sadness", "Isolate, stay in bed", "Get active, reach out to someone"),
        ("Anger", "Attack, yell", "Gently avoid, take space, be kind"),
        ("Fear", "Run away, avoid", "Approach what you fear (gradually)"),
        ("Shame", "Hide, don't tell anyone", "Share with a trusted person"),
        ("Guilt", "Punish yourself", "Repair, apologize, let it go"),
    ]
    for i, (em, urge, opp) in enumerate(opposites):
        font = 'F2' if i == 0 else 'F1'
        sz = 9 if i == 0 else 9
        pdf.add_text(72, y, em, font, sz)
        pdf.add_text(180, y, urge, font, sz)
        pdf.add_text(370, y, opp, font, sz)
        y -= 20
    y -= 15
    pdf.add_text(72, y, "MY OPPOSITE ACTION PRACTICE:", 'F2', 11)
    y -= 20
    pdf.add_text(72, y, "Emotion I'm feeling:", 'F1', 10)
    pdf.add_line(200, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "Does this emotion fit the facts? (Y/N):", 'F1', 10)
    pdf.add_line(290, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "What is the urge?", 'F1', 10)
    pdf.add_line(180, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "What is the opposite action?", 'F1', 10)
    pdf.add_line(230, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "Did I do it? What happened?", 'F1', 10)
    y -= 18
    for _ in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18

    # Emotion Regulation Page 3: ABC PLEASE
    pdf.new_page()
    pdf.add_centered_text(740, "EMOTION REGULATION: ABC PLEASE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Reduce vulnerability to negative emotions by taking care of basics:", 'F2', 10)
    y = 680
    abc = [
        ("A - Accumulate Positives", "Do one pleasant thing each day (small counts!)"),
        ("B - Build Mastery", "Do something that gives you a sense of accomplishment"),
        ("C - Cope Ahead", "Plan how you'll handle difficult situations before they happen"),
    ]
    for title, desc in abc:
        pdf.add_text(72, y, title, 'F2', 10)
        y -= 15
        pdf.add_text(90, y, desc, 'F4', 9)
        y -= 22
    y -= 5
    pdf.add_text(72, y, "PLEASE skills (body basics that affect emotions):", 'F2', 10)
    y -= 18
    please = [
        ("PL - PhysicaL illness", "Treat it. Take medication. See a doctor."),
        ("E - Eating", "Eat regularly. Don't skip meals. Balanced food."),
        ("A - Avoid mood-altering substances", "No drugs/alcohol to cope."),
        ("S - Sleep", "7-9 hours. Consistent schedule. Good sleep hygiene."),
        ("E - Exercise", "20+ minutes most days. Anything that moves your body."),
    ]
    for title, desc in please:
        pdf.add_text(72, y, title, 'F2', 9)
        y -= 14
        pdf.add_text(90, y, desc, 'F1', 9)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "MY PLEASE CHECK-IN THIS WEEK:", 'F2', 10)
    y -= 18
    pdf.add_text(72, y, "Day", 'F2', 8)
    pdf.add_text(110, y, "Slept?", 'F2', 8)
    pdf.add_text(160, y, "Ate?", 'F2', 8)
    pdf.add_text(210, y, "Moved?", 'F2', 8)
    pdf.add_text(270, y, "Pleasant?", 'F2', 8)
    pdf.add_text(340, y, "Mastery?", 'F2', 8)
    y -= 15
    for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        pdf.add_text(72, y, d, 'F1', 8)
        pdf.add_text(110, y, "Y/N", 'F1', 8)
        pdf.add_text(160, y, "Y/N", 'F1', 8)
        pdf.add_text(210, y, "Y/N", 'F1', 8)
        pdf.add_line(270, y - 2, 330, y - 2, 0.5, 0.5)
        pdf.add_line(340, y - 2, 400, y - 2, 0.5, 0.5)
        y -= 18

    # Emotion Regulation Page 4: Emotion Tracking
    pdf.new_page()
    pdf.add_centered_text(740, "EMOTION REGULATION: WEEKLY TRACKER", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 710, "Track your emotions daily. Notice patterns over time.", 'F1', 10)
    y = 685
    pdf.add_text(72, y, "Week of: ___/___/____", 'F1', 10)
    y -= 25
    pdf.add_text(72, y, "Day", 'F2', 8)
    pdf.add_text(110, y, "Strongest Emotion", 'F2', 8)
    pdf.add_text(240, y, "Intensity", 'F2', 8)
    pdf.add_text(310, y, "Trigger", 'F2', 8)
    pdf.add_text(430, y, "Skill Used", 'F2', 8)
    y -= 15
    for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        pdf.add_text(72, y, d, 'F1', 9)
        pdf.add_line(110, y - 2, 230, y - 2, 0.5, 0.5)
        pdf.add_line(240, y - 2, 300, y - 2, 0.5, 0.5)
        pdf.add_line(310, y - 2, 420, y - 2, 0.5, 0.5)
        pdf.add_line(430, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 25
    y -= 15
    pdf.add_text(72, y, "Patterns I notice:", 'F2', 10)
    y -= 18
    for _ in range(4):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18


    # Interpersonal Effectiveness (4 pages)
    # Page 1: DEAR MAN
    pdf.new_page()
    pdf.add_centered_text(740, "INTERPERSONAL: DEAR MAN", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Use DEAR MAN when you need to ASK for something or SAY NO:", 'F2', 10)
    y = 680
    dear_man = [
        ("D - Describe", "State the facts of the situation (no judgments)"),
        ("E - Express", "Share how you feel using 'I' statements"),
        ("A - Assert", "Ask clearly for what you want or say no clearly"),
        ("R - Reinforce", "Explain why it benefits them to help/agree"),
        ("M - Mindful", "Stay focused. Don't get sidetracked"),
        ("A - Appear confident", "Eye contact, steady voice, stand tall"),
        ("N - Negotiate", "Be willing to give to get. Offer alternatives"),
    ]
    for letter, desc in dear_man:
        pdf.add_text(72, y, letter, 'F2', 10)
        pdf.add_text(200, y, desc, 'F1', 9)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "MY DEAR MAN SCRIPT (write it out before the conversation):", 'F2', 10)
    y -= 18
    for letter in ["Describe:", "Express:", "Assert:", "Reinforce:"]:
        pdf.add_text(72, y, letter, 'F2', 9)
        pdf.add_line(140, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22
    pdf.add_text(72, y, "How will I stay Mindful?", 'F1', 9)
    pdf.add_line(220, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "What am I willing to negotiate?", 'F1', 9)
    pdf.add_line(240, y - 2, 540, y - 2, 0.5, 0.5)

    # Page 2: GIVE Skills
    pdf.new_page()
    pdf.add_centered_text(740, "INTERPERSONAL: GIVE SKILLS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Use GIVE when you want to maintain the RELATIONSHIP:", 'F2', 10)
    y = 680
    give = [
        ("G - Gentle", "No attacks, threats, or judging. Be respectful."),
        ("I - Interested", "Listen. Ask questions. Don't interrupt."),
        ("V - Validate", "Acknowledge their feelings even if you disagree."),
        ("E - Easy Manner", "Smile. Use humor. Be light when possible."),
    ]
    for letter, desc in give:
        pdf.add_text(72, y, letter, 'F2', 10)
        pdf.add_text(180, y, desc, 'F1', 9)
        y -= 25
    y -= 10
    pdf.add_text(72, y, "PRACTICE: Think of a recent conflict. Rewrite your approach using GIVE:", 'F2', 10)
    y -= 20
    pdf.add_text(72, y, "The situation:", 'F1', 10)
    pdf.add_line(160, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    for letter in ["Gentle:", "Interested:", "Validate:", "Easy manner:"]:
        pdf.add_text(72, y, letter, 'F2', 9)
        pdf.add_line(160, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22

    # Page 3: FAST Skills
    pdf.new_page()
    pdf.add_centered_text(740, "INTERPERSONAL: FAST SKILLS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Use FAST when you want to maintain your SELF-RESPECT:", 'F2', 10)
    y = 680
    fast = [
        ("F - Fair", "Be fair to yourself AND the other person."),
        ("A - Apologies (no excessive)", "Don't over-apologize. Don't apologize for existing."),
        ("S - Stick to values", "Don't sell out your values to be liked."),
        ("T - Truthful", "Don't lie or exaggerate. Be honest."),
    ]
    for letter, desc in fast:
        pdf.add_text(72, y, letter, 'F2', 10)
        pdf.add_text(250, y, desc, 'F1', 9)
        y -= 25
    y -= 10
    pdf.add_text(72, y, "MY VALUES (things I won't compromise on):", 'F2', 10)
    y -= 18
    for i in range(5):
        pdf.add_text(72, y, f"{i+1}.", 'F1', 10)
        pdf.add_line(88, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "Times I over-apologize:", 'F2', 10)
    y -= 18
    for _ in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 10
    pdf.add_text(72, y, "What I will say INSTEAD of sorry:", 'F2', 10)
    y -= 18
    for _ in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18

    # Page 4: Saying No
    pdf.new_page()
    pdf.add_centered_text(740, "INTERPERSONAL: SAYING NO", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Saying no is a complete sentence. But here are scripts if you need them:", 'F2', 10)
    y = 680
    scripts = [
        "'Thanks for thinking of me, but I can't this time.'",
        "'I need to check my schedule. I'll get back to you.' (buys time)",
        "'That doesn't work for me, but here's what I can do...'",
        "'I'm not comfortable with that.'",
        "'I have a rule about that.' (you don't need to explain the rule)",
    ]
    for s in scripts:
        pdf.add_text(90, y, s, 'F4', 10)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "PRACTICE: Write your own 'no' scripts for common situations:", 'F2', 10)
    y -= 20
    situations = [
        "When friends pressure you to do something risky:",
        "When someone asks too much of your time:",
        "When you need to set a boundary with family:",
    ]
    for sit in situations:
        pdf.add_text(72, y, sit, 'F1', 9)
        y -= 16
        pdf.add_text(72, y, "My script:", 'F1', 9)
        pdf.add_line(130, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 22


    # Crisis Survival Kit
    pdf.new_page()
    pdf.add_centered_text(740, "MY CRISIS SURVIVAL KIT", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Fill this out NOW while you're calm. Use it when emotions hit 8+.", 'F2', 10)
    y = 680
    kit_items = [
        ("People I can call/text:", 3),
        ("Places I feel safe:", 2),
        ("Things that distract me:", 3),
        ("Songs that calm me down:", 3),
        ("Reminders that this will pass:", 3),
        ("My TIPP plan:", 2),
        ("Professional help numbers:", 2),
    ]
    for label, lines in kit_items:
        pdf.add_text(72, y, label, 'F2', 10)
        y -= 16
        for _ in range(lines):
            pdf.add_line(90, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 8
    pdf.add_text(72, y, "Crisis Text Line: Text HOME to 741741", 'F2', 9)
    y -= 14
    pdf.add_text(72, y, "988 Suicide & Crisis Lifeline: Call or text 988", 'F2', 9)

    # DBT Skills Toolbox Summary
    pdf.new_page()
    pdf.add_centered_text(740, "MY DBT SKILLS TOOLBOX", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Circle or highlight the skills that work BEST for you:", 'F2', 10)
    y = 680
    toolbox = [
        ("MINDFULNESS:", "5-4-3-2-1 grounding, describe without judgment, participate fully"),
        ("DISTRESS TOLERANCE:", "TIPP, self-soothe, pros/cons, radical acceptance"),
        ("EMOTION REGULATION:", "Name it, opposite action, ABC PLEASE, check the facts"),
        ("INTERPERSONAL:", "DEAR MAN, GIVE, FAST, saying no scripts"),
    ]
    for cat, skills in toolbox:
        pdf.add_text(72, y, cat, 'F2', 10)
        y -= 16
        pdf.add_text(90, y, skills, 'F1', 9)
        y -= 25
    y -= 10
    pdf.add_text(72, y, "My TOP 3 go-to skills:", 'F2', 11)
    y -= 20
    for i in range(3):
        pdf.add_text(72, y, f"{i+1}.", 'F1', 10)
        pdf.add_line(88, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "Skill I want to practice more:", 'F1', 10)
    pdf.add_line(240, y - 2, 540, y - 2, 0.5, 0.5)
    y -= 22
    pdf.add_text(72, y, "When I will practice:", 'F1', 10)
    pdf.add_line(200, y - 2, 540, y - 2, 0.5, 0.5)

    # Weekly Practice Log (3 pages)
    for wk in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(740, f"WEEKLY PRACTICE LOG - Week {wk}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        pdf.add_text(72, 710, f"Week of: ___/___/____", 'F1', 10)
        y = 685
        pdf.add_text(72, y, "Day", 'F2', 8)
        pdf.add_text(110, y, "Skill Practiced", 'F2', 8)
        pdf.add_text(250, y, "Situation", 'F2', 8)
        pdf.add_text(400, y, "Helpful? (1-10)", 'F2', 8)
        y -= 15
        for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            pdf.add_text(72, y, d, 'F1', 9)
            pdf.add_line(110, y - 2, 240, y - 2, 0.5, 0.5)
            pdf.add_line(250, y - 2, 390, y - 2, 0.5, 0.5)
            pdf.add_line(400, y - 2, 480, y - 2, 0.5, 0.5)
            y -= 30
        y -= 10
        pdf.add_text(72, y, "This week I'm proud of:", 'F2', 10)
        pdf.add_line(72, y - 18, 540, y - 18, 0.5, 0.5)
        y -= 40
        pdf.add_text(72, y, "Next week I want to focus on:", 'F2', 10)
        pdf.add_line(72, y - 18, 540, y - 18, 0.5, 0.5)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book85_DBT_Teens_Workbook.pdf')
    print("Book85_DBT_Teens_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
