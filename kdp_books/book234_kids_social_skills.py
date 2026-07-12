"""Book 234: Social Skills Workbook for Kids Ages 6-12"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.2)
    doc.add_centered_text(755, "SOCIAL SKILLS WORKBOOK", 'F2', 22, 1)
    doc.add_centered_text(722, "FOR KIDS AGES 6-12", 'F2', 20, 1)
    doc.add_centered_text(665, "Making Friends, Managing Emotions & Speaking Up", 'F4', 13, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    doc.new_page()
    doc.add_centered_text(700, "SOCIAL SKILLS WORKBOOK FOR KIDS AGES 6-12", 'F2', 12)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # What Are Social Skills
    doc.new_page()
    doc.add_centered_text(750, "WHAT ARE SOCIAL SKILLS?", 'F2', 16)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = ["Social skills are the tools we use to get along with others!", "",
        "They help you:", "  - Make and keep friends",
        "  - Tell people how you feel", "  - Solve problems without fighting",
        "  - Feel confident in groups", "  - Stand up for yourself kindly", "",
        "Everyone can learn social skills - even grown-ups are still learning!", "",
        "In this workbook, you'll practice:", "  - Reading faces and body language",
        "  - Starting conversations", "  - Managing big feelings",
        "  - Being a great friend", "  - Handling tough situations", "",
        "Ready? Let's go!"]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 11)
        y -= 16

    # Reading Facial Expressions
    doc.new_page()
    doc.add_centered_text(750, "READING FACIAL EXPRESSIONS", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Match the description to the emotion!", 'F4', 11)
    y -= 22
    expressions = [
        ("Eyebrows up, mouth open wide", "___________  (Surprised!)"),
        ("Eyebrows down, lips pressed tight", "___________  (Angry)"),
        ("Corners of mouth up, eyes crinkled", "___________  (Happy)"),
        ("Corners of mouth down, eyes droopy", "___________  (Sad)"),
        ("Eyes wide, body pulled back", "___________  (Scared)"),
        ("Nose wrinkled, tongue out", "___________  (Disgusted)"),
        ("One eyebrow up, head tilted", "___________  (Confused)"),
        ("Looking away, fidgeting", "___________  (Nervous)"),
    ]
    for desc, answer in expressions:
        doc.add_text(72, y, desc, 'F1', 10)
        y -= 16
        doc.add_text(72, y, answer, 'F1', 10)
        y -= 22


    # Body Language Decoder
    doc.new_page()
    doc.add_centered_text(750, "BODY LANGUAGE DECODER", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "What does their body say? Circle: FRIENDLY or NOT FRIENDLY", 'F4', 10)
    y -= 22
    signals = [
        ("Arms crossed, looking away", "Friendly / Not Friendly"),
        ("Leaning in, smiling", "Friendly / Not Friendly"),
        ("Turned away, feet pointing to door", "Friendly / Not Friendly"),
        ("Eye contact, nodding", "Friendly / Not Friendly"),
        ("Yawning, checking phone", "Friendly / Not Friendly"),
        ("Waving, moving closer", "Friendly / Not Friendly"),
    ]
    for signal, choice in signals:
        doc.add_text(90, y, signal, 'F1', 10)
        y -= 18
        doc.add_text(90, y, choice, 'F2', 10)
        y -= 25
    doc.add_text(72, y, "MY body language when I'm happy:", 'F1', 10)
    doc.add_line(72, y-14, 540, y-14, 0.5, 0.4)
    y -= 30
    doc.add_text(72, y, "MY body language when I'm upset:", 'F1', 10)
    doc.add_line(72, y-14, 540, y-14, 0.5, 0.4)

    # Personal Space
    doc.new_page()
    doc.add_centered_text(750, "PERSONAL SPACE AWARENESS", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Everyone has a 'bubble' of personal space!", 'F4', 11)
    y -= 22
    zones = [
        ("CLOSE (arm's length)", "Family, best friends, pets"),
        ("MEDIUM (2 arm's lengths)", "Friends, classmates, teachers"),
        ("FAR (3+ arm's lengths)", "Strangers, people you just met"),
    ]
    for zone, who in zones:
        doc.add_text(72, y, zone, 'F2', 10)
        y -= 16
        doc.add_text(90, y, f"Who belongs here: {who}", 'F1', 10)
        y -= 25
    doc.add_text(72, y, "Signs someone needs MORE space:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "- They step back  - They lean away  - They look uncomfortable", 'F1', 10)
    y -= 22
    doc.add_text(72, y, "What to do: Take a step back and ask 'Is this okay?'", 'F1', 10)

    # Starting Conversations
    doc.new_page()
    doc.add_centered_text(750, "STARTING CONVERSATIONS", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "3 Easy Ways to Start Talking:", 'F2', 11)
    y -= 22
    scripts = [
        ("COMPLIMENT + QUESTION", "'I like your [backpack]. Where did you get it?'"),
        ("SHARED EXPERIENCE", "'That math test was hard! How did you feel about it?'"),
        ("OFFER HELP", "'Need a partner for the project? Want to work together?'"),
    ]
    for name, example in scripts:
        doc.add_text(72, y, name, 'F2', 10)
        y -= 16
        doc.add_text(90, y, example, 'F4', 10)
        y -= 22
    doc.add_text(72, y, "PRACTICE: Write your own conversation starters!", 'F2', 10)
    y -= 18
    for i in range(1, 4):
        doc.add_text(72, y, f"{i}. ________________________________", 'F1', 10)
        y -= 20

    # Joining Groups
    doc.new_page()
    doc.add_centered_text(750, "JOINING A GROUP", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    steps = ["Step 1: WATCH - Observe what they're doing (don't just jump in)",
        "Step 2: WAIT - Find the right moment (a pause or break)",
        "Step 3: APPROACH - Move closer with friendly body language",
        "Step 4: ASK - 'Can I play?' or 'Can I join you?'",
        "Step 5: BLEND IN - Follow their rules, don't try to change the game"]
    for s in steps:
        doc.add_text(72, y, s, 'F1', 10)
        y -= 22
    y -= 10
    doc.add_text(72, y, "If they say no:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "- It's okay! It's not about you.", 'F1', 10)
    y -= 16
    doc.add_text(90, y, "- Find another group or start your own game.", 'F1', 10)
    y -= 16
    doc.add_text(90, y, "- Ask a teacher for help if needed.", 'F1', 10)

    # Taking Turns + Managing Feelings + Disagreements
    doc.new_page()
    doc.add_centered_text(750, "TAKING TURNS & SHARING", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Why taking turns matters: Everyone gets a chance to be included!", 'F4', 10)
    y -= 22
    scenarios = [
        "Your friend wants to play a different game than you.",
        "You've been waiting a long time for the swing.",
        "Someone took the last cookie.",
        "Your sibling won't share the tablet.",
    ]
    for s in scenarios:
        doc.add_text(72, y, f"Scenario: {s}", 'F1', 9)
        y -= 14
        doc.add_text(72, y, "Fair solution: ________________________________", 'F1', 9)
        y -= 22

    doc.new_page()
    doc.add_centered_text(750, "MANAGING BIG FEELINGS - CALM-DOWN TOOLKIT", 'F2', 13)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    tools = ["1. BREATHE: Smell the flower (in), blow out the candle (out) x5",
        "2. COUNT: Count backward from 10 slowly",
        "3. SQUEEZE: Make fists tight for 5 seconds, then release",
        "4. MOVE: Do 10 jumping jacks or run in place",
        "5. DRAW: Scribble out your feelings on paper",
        "6. TALK: Tell someone 'I feel ___ because ___'",
        "7. SPACE: Go to your calm-down corner",
        "8. THINK: Will this matter tomorrow? Next week?"]
    for tool in tools:
        doc.add_text(72, y, tool, 'F1', 10)
        y -= 20
    y -= 10
    doc.add_text(72, y, "My top 3 calm-down tools:", 'F2', 10)
    y -= 16
    doc.add_text(72, y, "1.___________ 2.___________ 3.___________", 'F1', 10)


    # Disagreements + Standing Up + Good Friend + Teasing + Listening + Compliments
    doc.new_page()
    doc.add_centered_text(750, "DEALING WITH DISAGREEMENTS", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "PROBLEM-SOLVING STEPS:", 'F2', 11)
    y -= 20
    steps = ["1. STOP - Don't react right away. Take a breath.",
        "2. SAY what happened (facts only, no name-calling)",
        "3. LISTEN to their side (really listen!)",
        "4. BRAINSTORM solutions together (at least 3 ideas)",
        "5. CHOOSE one you both agree on",
        "6. TRY IT - if it doesn't work, try another solution"]
    for s in steps:
        doc.add_text(72, y, s, 'F1', 10)
        y -= 18
    y -= 15
    doc.add_text(72, y, "Practice: A disagreement I had:", 'F2', 10)
    y -= 16
    doc.add_text(72, y, "What happened: ________________________________", 'F1', 10)
    y -= 16
    doc.add_text(72, y, "How I solved it (or could have): ________________________________", 'F1', 10)

    doc.new_page()
    doc.add_centered_text(750, "STANDING UP FOR YOURSELF", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Assertive = Standing up for yourself WITHOUT being mean", 'F4', 10)
    y -= 22
    doc.add_text(72, y, "The Assertiveness Formula:", 'F2', 11)
    y -= 18
    doc.add_text(72, y, "'I feel [emotion] when you [action]. Please [what you need].'", 'F5', 11)
    y -= 25
    doc.add_text(72, y, "Examples:", 'F2', 10)
    y -= 16
    examples = ["'I feel upset when you take my things. Please ask first.'",
        "'I feel left out when you whisper. Please include me.'",
        "'I feel frustrated when you cut in line. Please wait your turn.'"]
    for e in examples:
        doc.add_text(90, y, e, 'F4', 9)
        y -= 18
    y -= 10
    doc.add_text(72, y, "YOUR TURN - Write your own:", 'F2', 10)
    y -= 16
    doc.add_text(72, y, "'I feel _______ when you _______. Please _______.'", 'F1', 10)

    doc.new_page()
    doc.add_centered_text(750, "BEING A GOOD FRIEND CHECKLIST", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    checklist = ["[ ] I listen when my friend talks",
        "[ ] I take turns and share", "[ ] I say nice things",
        "[ ] I include others", "[ ] I keep promises and secrets",
        "[ ] I apologize when I'm wrong", "[ ] I stand up for my friends",
        "[ ] I celebrate their successes", "[ ] I respect their boundaries",
        "[ ] I'm honest but kind", "[ ] I make time for them",
        "[ ] I forgive mistakes"]
    for item in checklist:
        doc.add_text(72, y, item, 'F1', 11)
        y -= 18

    doc.new_page()
    doc.add_centered_text(750, "HANDLING TEASING & BULLYING", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Response Options (choose what works for the situation):", 'F2', 10)
    y -= 20
    options = ["1. IGNORE - Walk away. Don't give a reaction.",
        "2. AGREE - 'Yeah, maybe!' (takes away their power)",
        "3. HUMOR - Make a joke and walk away",
        "4. ASSERTIVE - 'Stop. I don't like that.'",
        "5. TELL AN ADULT - Always okay, especially if unsafe",
        "6. BUDDY SYSTEM - Stay with friends"]
    for o in options:
        doc.add_text(72, y, o, 'F1', 10)
        y -= 20
    y -= 10
    doc.add_text(72, y, "IMPORTANT: Bullying is NOT your fault.", 'F2', 10)
    y -= 16
    doc.add_text(72, y, "Adults I can tell: ________________________________", 'F1', 10)

    doc.new_page()
    doc.add_centered_text(750, "ACTIVE LISTENING & COMPLIMENTS", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "ACTIVE LISTENING (HEAR):", 'F2', 10)
    y -= 18
    hear = ["H - Hold still (no fidgeting)", "E - Eyes on the speaker",
        "A - Ask questions to show interest", "R - Repeat back what you heard"]
    for h in hear:
        doc.add_text(90, y, h, 'F1', 10)
        y -= 16
    y -= 15
    doc.add_text(72, y, "GIVING COMPLIMENTS:", 'F2', 10)
    y -= 16
    doc.add_text(72, y, "Be specific! Not just 'nice job' but 'I loved how you...'", 'F4', 10)
    y -= 18
    doc.add_text(72, y, "Practice - Give a compliment to:", 'F1', 10)
    y -= 16
    doc.add_text(90, y, "A friend: ________________________________", 'F1', 10)
    y -= 16
    doc.add_text(90, y, "A family member: ________________________________", 'F1', 10)
    y -= 16
    doc.add_text(90, y, "Yourself: ________________________________", 'F1', 10)
    y -= 22
    doc.add_text(72, y, "RECEIVING COMPLIMENTS:", 'F2', 10)
    y -= 16
    doc.add_text(72, y, "Just say 'Thank you!' (Don't argue or put yourself down)", 'F1', 10)


    # 10 Social Scenario Pages
    scenarios = [
        ("A new kid joins your class and sits alone at lunch.", "Invite them to sit with you / Ask what they like / Share something"),
        ("Your friend is crying because they got a bad grade.", "Listen / Don't say 'it's not a big deal' / Offer to help study"),
        ("Someone cuts in front of you in line.", "Say calmly 'I was here first' / Tell teacher if they won't move"),
        ("You accidentally hurt someone's feelings.", "Apologize sincerely / Ask how to make it better"),
        ("A group is playing and you want to join.", "Watch, wait, approach, ask, blend in"),
        ("Your friend wants to copy your homework.", "Say no kindly / Offer to help them understand instead"),
        ("Someone is being mean to another kid.", "Stand up for them / Get an adult / Don't join in"),
        ("You disagree with your friend about what game to play.", "Take turns / Compromise / Find something you both like"),
        ("You feel left out because your friends made plans without you.", "Tell them how you feel / It might not be on purpose"),
        ("Someone spread a rumor about you.", "Don't spread it back / Talk to an adult / Confront calmly"),
    ]
    for i, (situation, options) in enumerate(scenarios, 1):
        doc.new_page()
        doc.add_centered_text(755, f"SOCIAL SCENARIO #{i}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        doc.add_text(72, y, "SITUATION:", 'F2', 10)
        y -= 16
        doc.add_text(72, y, situation, 'F1', 10)
        y -= 30
        doc.add_text(72, y, "WHAT COULD YOU DO? (write 3 options):", 'F2', 10)
        y -= 18
        for o in range(1, 4):
            doc.add_text(72, y, f"{o}. ________________________________", 'F1', 10)
            y -= 20
        y -= 10
        doc.add_text(72, y, "BEST CHOICE and WHY:", 'F2', 10)
        y -= 16
        doc.add_line(72, y, 540, y, 0.5, 0.4)
        y -= 16
        doc.add_line(72, y, 540, y, 0.5, 0.4)
        y -= 25
        doc.add_text(72, y, "HELPFUL HINT:", 'F2', 9)
        y -= 16
        doc.add_text(72, y, options, 'F4', 9)

    # My Social Goals
    doc.new_page()
    doc.add_centered_text(750, "MY SOCIAL GOALS", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Social skills I'm already good at:", 'F2', 10)
    y -= 16
    for _ in range(3):
        doc.add_text(90, y, "- ________________________________", 'F1', 10)
        y -= 16
    y -= 10
    doc.add_text(72, y, "Skills I want to work on:", 'F2', 10)
    y -= 16
    for _ in range(3):
        doc.add_text(90, y, "- ________________________________", 'F1', 10)
        y -= 16
    y -= 10
    doc.add_text(72, y, "My #1 goal this month:", 'F2', 10)
    y -= 16
    doc.add_line(72, y, 540, y, 0.5, 0.4)
    y -= 20
    doc.add_text(72, y, "How I'll practice:", 'F1', 10)
    doc.add_line(72, y-14, 540, y-14, 0.5, 0.4)

    # Weekly Friendship Tracker (4 pages)
    for wk in range(1, 5):
        doc.new_page()
        doc.add_centered_text(755, f"WEEKLY FRIENDSHIP TRACKER - WEEK {wk}", 'F2', 12)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in days:
            doc.add_text(72, y, day, 'F2', 9)
            y -= 14
            doc.add_text(90, y, "Kind thing I did: ________________________________", 'F1', 8)
            y -= 12
            doc.add_text(90, y, "Social skill I practiced: ________________________________", 'F1', 8)
            y -= 12
            doc.add_text(90, y, "Challenge I faced: ________________________________", 'F1', 8)
            y -= 20
        doc.add_text(72, y, "This week I'm proud of: ________________________________", 'F2', 9)

    # Certificate
    doc.new_page()
    doc.add_rect(50, 100, 512, 600, 2, 0.3)
    doc.add_rect(60, 110, 492, 580, 1, 0.5)
    doc.add_centered_text(620, "CERTIFICATE OF", 'F2', 18)
    doc.add_centered_text(590, "SOCIAL SKILLS MASTERY", 'F2', 22)
    doc.add_centered_text(540, "This certifies that", 'F4', 14)
    doc.add_centered_text(500, "________________________________", 'F1', 14)
    doc.add_centered_text(470, "(your name)", 'F1', 10, 0.5)
    doc.add_centered_text(430, "has completed this workbook and demonstrated", 'F4', 12)
    doc.add_centered_text(405, "excellent social skills including:", 'F4', 12)
    doc.add_centered_text(370, "Making Friends | Managing Emotions | Speaking Up", 'F1', 11)
    doc.add_centered_text(345, "Listening | Kindness | Problem Solving", 'F1', 11)
    doc.add_centered_text(290, "Date: ___/___/___", 'F1', 12)
    doc.add_centered_text(250, "Congratulations! You are a Social Skills CHAMPION!", 'F2', 12)

    doc.save("Book234_Social_Skills_Kids_Workbook.pdf")
    print("Created: Book234_Social_Skills_Kids_Workbook.pdf")

if __name__ == "__main__":
    create_book()
