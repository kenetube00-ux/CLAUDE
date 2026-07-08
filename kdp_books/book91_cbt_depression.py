"""Book 91: CBT Workbook for Depression"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.12)
    pdf.add_centered_text(520, "CBT WORKBOOK", 'F2', 32, 1)
    pdf.add_centered_text(480, "FOR DEPRESSION", 'F2', 28, 1)
    pdf.add_centered_text(430, "Break the Cycle of Negative Thinking", 'F4', 16, 0.9)
    pdf.add_centered_text(380, "Behavioral Activation, Mood Tracking &", 'F1', 13, 0.8)
    pdf.add_centered_text(360, "Evidence-Based Exercises for Recovery", 'F1', 13, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    pdf.add_centered_text(170, "Practical Tools for Managing Depression", 'F1', 11, 0.7)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "CBT Workbook for Depression", 'F2', 14)
    pdf.add_centered_text(475, "Break the Cycle of Negative Thinking", 'F4', 11)
    pdf.add_centered_text(440, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)

    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(390, "This workbook is for educational purposes only.", 'F1', 9)
    pdf.add_centered_text(370, "It is not a substitute for professional mental health treatment.", 'F1', 9)
    pdf.add_centered_text(340, "If you are in crisis, call 988 Suicide & Crisis Lifeline.", 'F2', 9)

    # Page 1: Understanding Depression Cycles
    pdf.new_page()
    pdf.add_centered_text(740, "UNDERSTANDING THE DEPRESSION CYCLE", 'F2', 18)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    text = [
        "Depression creates a vicious cycle that keeps you stuck:",
        "",
        "  LOW MOOD --> WITHDRAWAL --> LESS ACTIVITY --> FEWER REWARDS",
        "       ^                                            |",
        "       |____________________________________________|",
        "",
        "When you feel depressed, you naturally do less. But doing less means",
        "fewer opportunities for pleasure, accomplishment, and connection.",
        "This CONFIRMS depressive thoughts ('Nothing matters', 'I can't do anything').",
        "",
        "CBT for depression breaks this cycle through BEHAVIORAL ACTIVATION:",
        "Instead of waiting to feel motivated, you ACT FIRST and let mood follow.",
        "",
        "KEY PRINCIPLE: Action comes BEFORE motivation, not after.",
        "",
        "The Depression Triangle:",
        "  THOUGHTS: 'I'm worthless, nothing will help, what's the point'",
        "  FEELINGS: Sad, empty, hopeless, guilty, irritable",
        "  BEHAVIORS: Isolating, sleeping too much, avoiding tasks",
        "",
        "This workbook will help you:",
        "  1. Identify YOUR depression cycle",
        "  2. Schedule activities that bring pleasure and mastery",
        "  3. Challenge hopelessness and self-critical thoughts",
        "  4. Build energy gradually through structured activation",
        "  5. Prevent relapse by recognizing warning signs early",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 11)
        y -= 18


    # Page 2: Behavioral Activation - Activity Scheduling
    pdf.new_page()
    pdf.add_centered_text(740, "BEHAVIORAL ACTIVATION: ACTIVITY SCHEDULING", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Schedule activities BEFORE you feel like doing them.", 'F2', 11)
    pdf.add_text(72, 685, "Rate each: P = Pleasure (0-10)  M = Mastery (0-10)", 'F1', 10)
    y = 655
    times = ["7 AM", "9 AM", "11 AM", "1 PM", "3 PM", "5 PM", "7 PM", "9 PM"]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # Header row
    pdf.add_text(72, y, "Time", 'F2', 8)
    for i, d in enumerate(days):
        pdf.add_text(120 + i * 62, y, d, 'F2', 8)
    y -= 15
    for t in times:
        pdf.add_text(72, y, t, 'F1', 8)
        for i in range(7):
            pdf.add_rect(120 + i * 62, y - 8, 58, 30, 0.5, 0.4)
        y -= 35
    pdf.add_text(72, y - 5, "End-of-week reflection: Which activities improved my mood most?", 'F2', 9)
    pdf.add_line(72, y - 25, 540, y - 25, 0.5, 0.5)
    pdf.add_line(72, y - 45, 540, y - 45, 0.5, 0.5)

    # Page 3: Pleasure and Mastery Ratings
    pdf.new_page()
    pdf.add_centered_text(740, "PLEASURE & MASTERY ACTIVITY LIST", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Rate activities you USED to enjoy or that give a sense of accomplishment.", 'F1', 10)
    pdf.add_text(72, 685, "P = Pleasure (how enjoyable)  M = Mastery (sense of achievement)  Both 0-10", 'F1', 9)
    y = 660
    pdf.add_text(72, y, "Activity", 'F2', 9)
    pdf.add_text(320, y, "P Rating", 'F2', 9)
    pdf.add_text(400, y, "M Rating", 'F2', 9)
    pdf.add_text(480, y, "Schedule?", 'F2', 9)
    y -= 20
    activities = [
        "Walking outside", "Calling a friend", "Cooking a meal",
        "Reading a book", "Listening to music", "Taking a shower/bath",
        "Light exercise", "Gardening", "Watching a favorite show",
        "Completing a small task", "Helping someone", "Creative activity",
        "Going to a cafe", "Playing with a pet", "Organizing one drawer",
    ]
    for act in activities:
        pdf.add_text(72, y, act, 'F1', 9)
        pdf.add_line(320, y - 2, 380, y - 2, 0.5, 0.5)
        pdf.add_line(400, y - 2, 460, y - 2, 0.5, 0.5)
        pdf.add_line(480, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22
    pdf.add_text(72, y - 5, "My own activities:", 'F2', 9)
    for i in range(5):
        pdf.add_line(72, y - 25 - i * 20, 540, y - 25 - i * 20, 0.5, 0.5)


    # Page 4: Challenging Hopelessness Thoughts
    pdf.new_page()
    pdf.add_centered_text(740, "CHALLENGING HOPELESSNESS THOUGHTS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    text = [
        "Depression tells you lies disguised as facts. Common hopeless thoughts:",
        "",
        "  'Nothing will ever get better'",
        "  'I'm a burden to everyone'",
        "  'What's the point of trying'",
        "  'I'll always feel this way'",
        "  'I don't deserve to be happy'",
        "",
        "CHALLENGING THESE THOUGHTS:",
        "",
        "1. What is the thought? ________________________________________",
        "",
        "2. What evidence SUPPORTS this thought?",
        "   _____________________________________________________________",
        "",
        "3. What evidence CONTRADICTS this thought?",
        "   _____________________________________________________________",
        "",
        "4. Am I confusing a FEELING with a FACT?  Yes / No",
        "",
        "5. What would I say to a friend thinking this?",
        "   _____________________________________________________________",
        "",
        "6. A more balanced thought:",
        "   _____________________________________________________________",
        "",
        "7. Belief in hopeless thought now (0-100%): _____",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 18

    # Page 5: Gratitude Reframing
    pdf.new_page()
    pdf.add_centered_text(740, "GRATITUDE REFRAMING EXERCISE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Depression narrows your focus to the negative. Gratitude retrains attention.", 'F4', 10)
    pdf.add_text(72, 685, "This is NOT toxic positivity - it's noticing what depression makes invisible.", 'F4', 10)
    y = 655
    for day in range(1, 8):
        pdf.add_text(72, y, f"Day {day}:", 'F2', 10)
        y -= 18
        pdf.add_text(72, y, "Three small things I noticed today (not big - tiny is fine):", 'F1', 9)
        y -= 16
        for i in range(3):
            pdf.add_text(85, y, f"{i+1}.", 'F1', 9)
            pdf.add_line(100, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 18
        y -= 8

    # Page 6: Energy Management
    pdf.new_page()
    pdf.add_centered_text(740, "ENERGY MANAGEMENT FOR DEPRESSION", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    text = [
        "Depression drains energy. You cannot do everything. Prioritize wisely.",
        "",
        "THE SPOON THEORY FOR DEPRESSION:",
        "Imagine you start each day with 10 spoons of energy.",
        "Each task costs spoons. When they're gone, you're done.",
        "",
        "Rate your energy today (1-10): _____",
        "",
        "MUST DO (costs 1-2 spoons each):",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    for i in range(3):
        pdf.add_line(72, y, 400, y, 0.5, 0.5)
        y -= 20
    pdf.add_text(72, y, "SHOULD DO (costs 2-3 spoons each):", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(72, y, 400, y, 0.5, 0.5)
        y -= 20
    pdf.add_text(72, y, "WOULD LIKE TO DO (costs 1 spoon - only if energy remains):", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(72, y, 400, y, 0.5, 0.5)
        y -= 20
    pdf.add_text(72, y, "ENERGY BOOSTERS (give spoons back):", 'F2', 10)
    y -= 18
    for i in range(4):
        pdf.add_line(72, y, 400, y, 0.5, 0.5)
        y -= 20


    # Page 7: Social Withdrawal Prevention
    pdf.new_page()
    pdf.add_centered_text(740, "SOCIAL WITHDRAWAL PREVENTION PLAN", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    text = [
        "Depression makes you want to isolate. Isolation makes depression worse.",
        "You don't need to be social - just CONNECTED.",
        "",
        "MY MINIMUM SOCIAL CONTACTS (aim for at least 1 per day):",
        "",
        "LOW ENERGY OPTIONS (when everything feels too hard):",
        "  - Send one text message to someone",
        "  - Reply to one message I've been avoiding",
        "  - Sit in a public place (cafe, park) for 10 min",
        "  - Say hi to one neighbor or coworker",
        "",
        "MEDIUM ENERGY OPTIONS:",
        "  - Call someone for 5-10 minutes",
        "  - Accept one invitation this week",
        "  - Eat one meal with another person",
        "  - Attend one regular activity (class, meeting)",
        "",
        "HIGH ENERGY OPTIONS (for better days):",
        "  - Plan a small outing with a friend",
        "  - Host someone for coffee at home",
        "  - Join a group activity or class",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    y -= 10
    pdf.add_text(72, y, "My safe people (who I can be honest with about how I feel):", 'F2', 10)
    y -= 18
    for i in range(4):
        pdf.add_text(72, y, f"{i+1}. Name: _________________ How to reach: _________________", 'F1', 9)
        y -= 20

    # Page 8: Sleep Hygiene Worksheet
    pdf.new_page()
    pdf.add_centered_text(740, "SLEEP HYGIENE WORKSHEET", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    text = [
        "Depression disrupts sleep (too much OR too little). Good sleep = better mood.",
        "",
        "MY SLEEP GOALS:",
        "  Bedtime: _________  Wake time: _________  Total hours target: _____",
        "",
        "SLEEP HYGIENE CHECKLIST (check what you'll commit to):",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    checklist = [
        "Same wake time every day (even weekends)",
        "No screens 30 min before bed",
        "Bedroom is dark, cool, and quiet",
        "No caffeine after 2 PM",
        "No naps longer than 20 minutes",
        "Get sunlight within 30 min of waking",
        "Wind-down routine (bath, reading, stretching)",
        "Bed is for sleep only (not phone/TV/work)",
        "If awake 20 min, get up and do something boring",
        "Limit alcohol (disrupts sleep quality)",
    ]
    for item in checklist:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, item, 'F1', 9)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "SLEEP LOG:", 'F2', 10)
    y -= 18
    pdf.add_text(72, y, "Day", 'F2', 8)
    pdf.add_text(120, y, "Bed Time", 'F2', 8)
    pdf.add_text(200, y, "Wake Time", 'F2', 8)
    pdf.add_text(290, y, "Hours", 'F2', 8)
    pdf.add_text(350, y, "Quality(1-10)", 'F2', 8)
    pdf.add_text(450, y, "Mood AM", 'F2', 8)
    y -= 15
    for d in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]:
        pdf.add_text(72, y, d, 'F1', 8)
        pdf.add_line(120, y-2, 185, y-2, 0.5, 0.5)
        pdf.add_line(200, y-2, 275, y-2, 0.5, 0.5)
        pdf.add_line(290, y-2, 335, y-2, 0.5, 0.5)
        pdf.add_line(350, y-2, 430, y-2, 0.5, 0.5)
        pdf.add_line(450, y-2, 530, y-2, 0.5, 0.5)
        y -= 20


    # Page 9: Rumination Interruption Techniques
    pdf.new_page()
    pdf.add_centered_text(740, "RUMINATION INTERRUPTION TECHNIQUES", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    text = [
        "Rumination = replaying negative thoughts over and over without solving anything.",
        "It feels productive but actually deepens depression.",
        "",
        "RECOGNIZE: Am I problem-solving or ruminating?",
        "  Problem-solving: Leads to a plan of action",
        "  Rumination: Goes in circles, focuses on 'why me', no solution",
        "",
        "INTERRUPTION TECHNIQUES:",
        "",
        "1. THE 5-4-3-2-1 GROUNDING:",
        "   5 things I see: ____________________________________________",
        "   4 things I can touch: _______________________________________",
        "   3 things I hear: ___________________________________________",
        "   2 things I smell: __________________________________________",
        "   1 thing I taste: ___________________________________________",
        "",
        "2. SCHEDULE RUMINATION TIME: Give yourself 15 min at a set time.",
        "   Outside that time, write the thought down and POSTPONE it.",
        "",
        "3. CHANGE PHYSICAL STATE: Stand up, splash cold water, hold ice.",
        "",
        "4. MENTAL SHIFT: Count backward from 100 by 7s, name countries A-Z.",
        "",
        "5. ASK: 'Will this matter in 5 years?' If no, redirect attention.",
        "",
        "My go-to interruption technique: ________________________________",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17

    # Page 10: Values Identification
    pdf.new_page()
    pdf.add_centered_text(740, "VALUES IDENTIFICATION WORKSHEET", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Depression disconnects you from what matters. Reconnect with your values.", 'F4', 10)
    pdf.add_text(72, 685, "Rate importance (1-10) and how well you're living this value (1-10):", 'F1', 9)
    y = 660
    values = [
        "Family/Relationships", "Health/Physical well-being", "Career/Work",
        "Friendship/Social", "Spirituality/Faith", "Learning/Growth",
        "Creativity/Self-expression", "Fun/Recreation", "Service/Helping others",
        "Independence/Freedom", "Honesty/Integrity", "Nature/Environment",
    ]
    pdf.add_text(72, y, "Value Area", 'F2', 9)
    pdf.add_text(280, y, "Importance", 'F2', 9)
    pdf.add_text(370, y, "Living it?", 'F2', 9)
    pdf.add_text(460, y, "Gap", 'F2', 9)
    y -= 18
    for v in values:
        pdf.add_text(72, y, v, 'F1', 9)
        pdf.add_line(280, y - 2, 340, y - 2, 0.5, 0.5)
        pdf.add_line(370, y - 2, 430, y - 2, 0.5, 0.5)
        pdf.add_line(460, y - 2, 520, y - 2, 0.5, 0.5)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "My TOP 3 values I want to reconnect with:", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_text(72, y, f"{i+1}.", 'F1', 10)
        pdf.add_line(90, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22
    pdf.add_text(72, y, "One small action I can take THIS WEEK toward my #1 value:", 'F2', 9)
    pdf.add_line(72, y - 18, 540, y - 18, 0.5, 0.5)


    # Page 11: Goal-Setting When Depressed
    pdf.new_page()
    pdf.add_centered_text(740, "GOAL-SETTING WHEN DEPRESSED", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    text = [
        "Depression makes everything feel impossible. The key: TINY goals.",
        "",
        "RULES FOR DEPRESSION-FRIENDLY GOALS:",
        "  1. Make it so small it feels almost too easy",
        "  2. Focus on DOING, not FEELING (you can't control feelings)",
        "  3. Be specific: what, when, where",
        "  4. No 'should' or 'must' - use 'I choose to'",
        "  5. Celebrate completion regardless of how it felt",
        "",
        "EXAMPLE: Instead of 'Exercise more' --> 'Walk to mailbox Monday at 9am'",
        "",
        "MY GOALS FOR THIS WEEK:",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    y -= 5
    for i in range(5):
        pdf.add_text(72, y, f"Goal {i+1}:", 'F2', 10)
        pdf.add_line(120, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18
        pdf.add_text(72, y, "When/Where:", 'F1', 9)
        pdf.add_line(150, y - 2, 350, y - 2, 0.5, 0.5)
        pdf.add_text(360, y, "Done?", 'F1', 9)
        pdf.add_rect(400, y - 3, 10, 10, 0.5, 0.3)
        y -= 25

    # Pages 12-15: Weekly Mood/Activity Log (4 pages)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for wk in range(1, 5):
        pdf.new_page()
        pdf.add_centered_text(740, f"WEEKLY MOOD & ACTIVITY LOG - Week {wk}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        y = 710
        pdf.add_text(72, y, "Day", 'F2', 8)
        pdf.add_text(130, y, "Mood(1-10)", 'F2', 8)
        pdf.add_text(210, y, "Energy(1-10)", 'F2', 8)
        pdf.add_text(300, y, "Activities Completed", 'F2', 8)
        pdf.add_text(470, y, "P/M Rating", 'F2', 8)
        y -= 15
        for day in days:
            pdf.add_text(72, y, day[:3], 'F1', 8)
            pdf.add_line(130, y - 2, 195, y - 2, 0.5, 0.5)
            pdf.add_line(210, y - 2, 285, y - 2, 0.5, 0.5)
            pdf.add_line(300, y - 2, 460, y - 2, 0.5, 0.5)
            pdf.add_line(470, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 22
            pdf.add_line(300, y - 2, 460, y - 2, 0.5, 0.5)
            pdf.add_line(470, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 22
        y -= 10
        pdf.add_text(72, y, "Patterns I notice:", 'F2', 9)
        pdf.add_line(72, y - 16, 540, y - 16, 0.5, 0.5)
        pdf.add_line(72, y - 34, 540, y - 34, 0.5, 0.5)
        pdf.add_text(72, y - 52, "Highest mood day & what I did:", 'F2', 9)
        pdf.add_line(72, y - 68, 540, y - 68, 0.5, 0.5)
        pdf.add_text(72, y - 86, "Lowest mood day & what was different:", 'F2', 9)
        pdf.add_line(72, y - 102, 540, y - 102, 0.5, 0.5)


    # Page 16: Identifying Depression Cycles (Personal)
    pdf.new_page()
    pdf.add_centered_text(740, "IDENTIFYING MY DEPRESSION CYCLE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    pdf.add_text(72, y, "Map YOUR specific depression cycle below:", 'F2', 11)
    y -= 25
    pdf.add_text(72, y, "1. My typical depressive THOUGHTS:", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 20
    pdf.add_text(72, y, "2. How these thoughts make me FEEL (emotions + body):", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 20
    pdf.add_text(72, y, "3. What I DO (or stop doing) when I feel this way:", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 20
    pdf.add_text(72, y, "4. How my behaviors make the thoughts/feelings WORSE:", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 20
    pdf.add_text(72, y, "5. WHERE CAN I BREAK THE CYCLE? (circle one):", 'F2', 10)
    y -= 18
    pdf.add_text(90, y, "Change a THOUGHT    |    Change a BEHAVIOR    |    Both", 'F1', 10)
    y -= 25
    pdf.add_text(72, y, "6. My specific plan to interrupt the cycle:", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 20

    # Page 17: Relapse Warning Signs
    pdf.new_page()
    pdf.add_centered_text(740, "RELAPSE WARNING SIGNS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    text = [
        "Depression often returns gradually. Knowing YOUR early signs helps you",
        "act quickly before a full episode develops.",
        "",
        "MY EARLY WARNING SIGNS (check those that apply to you):",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    signs = [
        "Sleeping more than usual / difficulty getting out of bed",
        "Canceling plans with friends/family",
        "Letting dishes/laundry/mail pile up",
        "Negative self-talk increasing",
        "Loss of interest in things I usually enjoy",
        "Increased irritability or tearfulness",
        "Difficulty concentrating / brain fog",
        "Changes in appetite (eating more or less)",
        "Physical symptoms (headaches, body aches)",
        "Withdrawing from social media / not responding to messages",
        "Skipping self-care routines (showering, brushing teeth)",
        "Thoughts of hopelessness returning",
    ]
    for sign in signs:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, sign, 'F1', 9)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "My personal early signs not listed above:", 'F2', 9)
    y -= 18
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    pdf.add_text(72, y, "When I notice 3+ signs, I will:", 'F2', 9)
    pdf.add_line(72, y - 16, 540, y - 16, 0.5, 0.5)


    # Page 18: My Support Plan
    pdf.new_page()
    pdf.add_centered_text(740, "MY SUPPORT PLAN", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    fields = [
        ("My therapist/counselor:", 1),
        ("Phone:", 1),
        ("My doctor:", 1),
        ("Phone:", 1),
        ("Crisis line: 988 Suicide & Crisis Lifeline", 0),
        ("", 0),
        ("People I can call when I'm struggling:", 0),
        ("1. Name: ______________ Phone: ______________", 0),
        ("2. Name: ______________ Phone: ______________", 0),
        ("3. Name: ______________ Phone: ______________", 0),
        ("", 0),
        ("Things that have helped me in past episodes:", 0),
    ]
    for label, lines in fields:
        pdf.add_text(72, y, label, 'F2' if lines == 0 else 'F1', 10)
        y -= 18
    for i in range(4):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 20
    y -= 5
    pdf.add_text(72, y, "My non-negotiable self-care (things I do even on worst days):", 'F2', 10)
    y -= 18
    for i in range(4):
        pdf.add_text(72, y, f"{i+1}.", 'F1', 10)
        pdf.add_line(90, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "Medications (name/dose/time):", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 20
    pdf.add_text(72, y, "I will seek emergency help if:", 'F2', 10)
    y -= 18
    pdf.add_line(72, y, 540, y, 0.5, 0.5)

    # Pages 19-25: Additional Content Pages
    # Page 19: 30-Day Behavioral Activation Challenge
    pdf.new_page()
    pdf.add_centered_text(740, "30-DAY BEHAVIORAL ACTIVATION CHALLENGE", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 710, "Do ONE thing each day. Check off when done. Tiny counts!", 'F1', 10)
    challenges = [
        "Day 1: Get out of bed within 10 min of alarm",
        "Day 2: Take a 5-minute walk (around block or house)",
        "Day 3: Text or call one person",
        "Day 4: Cook or prepare one meal (not just snacks)",
        "Day 5: Take a full shower and get dressed",
        "Day 6: Do one load of laundry (start to finish)",
        "Day 7: Go to a store or public place for 10 min",
        "Day 8: Write down 3 things you accomplished this week",
        "Day 9: Listen to music that used to make you feel good",
        "Day 10: Spend 10 min in sunlight/outdoors",
        "Day 11: Clean one small area (one counter, one shelf)",
        "Day 12: Reach out to someone you've been avoiding",
        "Day 13: Do 5 minutes of gentle stretching",
        "Day 14: HALFWAY! Rate mood vs Day 1. Celebrate progress.",
        "Day 15: Try one new or forgotten activity for 15 min",
        "Day 16: Write a brief gratitude list (3 items)",
        "Day 17: Go to bed at a planned time tonight",
        "Day 18: Help someone with something small",
        "Day 19: Eat at a table (not in bed/couch) for one meal",
        "Day 20: Spend 15 min on a hobby or creative activity",
        "Day 21: Attend a social event (even online counts)",
        "Day 22: Do one task you've been putting off",
        "Day 23: Practice the 5-4-3-2-1 grounding exercise",
        "Day 24: Move your body for 15 minutes (any movement)",
        "Day 25: Declutter one small space",
        "Day 26: Do something kind for yourself",
        "Day 27: Plan one enjoyable activity for next week",
        "Day 28: Review your values - do one value-based action",
        "Day 29: Write what has changed since Day 1",
        "Day 30: Create your ongoing self-care plan",
    ]
    y = 690
    for ch in challenges:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, ch, 'F1', 9)
        y -= 21


    # Pages 20-25: Additional worksheets
    # Page 20: Challenging Hopelessness - Worksheet 2
    pdf.new_page()
    pdf.add_centered_text(740, "THOUGHT CHALLENGE WORKSHEET", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    for section in range(2):
        pdf.add_text(72, y, f"Situation #{section+1}:", 'F2', 10)
        pdf.add_line(160, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22
        pdf.add_text(72, y, "Automatic thought:", 'F1', 9)
        pdf.add_line(180, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
        pdf.add_text(72, y, "Emotion + intensity (0-100%):", 'F1', 9)
        pdf.add_line(240, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
        pdf.add_text(72, y, "Evidence for:", 'F1', 9)
        pdf.add_line(150, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
        pdf.add_text(72, y, "Evidence against:", 'F1', 9)
        pdf.add_line(170, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
        pdf.add_text(72, y, "Balanced thought:", 'F1', 9)
        pdf.add_line(170, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 20
        pdf.add_text(72, y, "Emotion now (0-100%):", 'F1', 9)
        pdf.add_line(200, y - 2, 350, y - 2, 0.5, 0.5)
        y -= 30

    # Page 21: Behavioral Activation Schedule 2
    pdf.new_page()
    pdf.add_centered_text(740, "BEHAVIORAL ACTIVATION SCHEDULE - Week 2", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Plan activities that mix Pleasure (P) and Mastery (M).", 'F2', 10)
    y = 680
    times = ["Morning", "Midday", "Afternoon", "Evening"]
    dys = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    pdf.add_text(72, y, "", 'F2', 8)
    for i, d in enumerate(dys):
        pdf.add_text(130 + i * 58, y, d, 'F2', 8)
    y -= 15
    for t in times:
        pdf.add_text(72, y, t, 'F1', 8)
        for i in range(7):
            pdf.add_rect(130 + i * 58, y - 10, 54, 35, 0.5, 0.4)
        y -= 42
    pdf.add_text(72, y - 5, "Activities that gave me the most pleasure this week:", 'F2', 9)
    pdf.add_line(72, y - 22, 540, y - 22, 0.5, 0.5)
    pdf.add_text(72, y - 40, "Activities that gave me the most mastery this week:", 'F2', 9)
    pdf.add_line(72, y - 57, 540, y - 57, 0.5, 0.5)

    # Page 22: Thought Challenge 2
    pdf.new_page()
    pdf.add_centered_text(740, "CHALLENGING SELF-CRITICAL THOUGHTS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    text = [
        "Depression amplifies your inner critic. Common self-critical thoughts:",
        "  'I'm not good enough'  'I always mess things up'  'I'm lazy'",
        "",
        "THE COMPASSIONATE RESPONSE TECHNIQUE:",
        "",
        "My self-critical thought:",
        "_______________________________________________________________",
        "",
        "What a harsh critic would say (write it out):",
        "_______________________________________________________________",
        "",
        "What a compassionate friend would say instead:",
        "_______________________________________________________________",
        "",
        "Evidence that I am NOT what my critic says:",
        "1. ____________________________________________________________",
        "2. ____________________________________________________________",
        "3. ____________________________________________________________",
        "",
        "What I would tell my best friend if they said this about themselves:",
        "_______________________________________________________________",
        "",
        "My compassionate response to myself:",
        "_______________________________________________________________",
        "_______________________________________________________________",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 18

    # Page 23: Behavioral Activation Schedule 3
    pdf.new_page()
    pdf.add_centered_text(740, "BEHAVIORAL ACTIVATION SCHEDULE - Week 3", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Increase difficulty slightly. Add one new activity per day.", 'F2', 10)
    y = 680
    pdf.add_text(72, y, "", 'F2', 8)
    for i, d in enumerate(dys):
        pdf.add_text(130 + i * 58, y, d, 'F2', 8)
    y -= 15
    for t in times:
        pdf.add_text(72, y, t, 'F1', 8)
        for i in range(7):
            pdf.add_rect(130 + i * 58, y - 10, 54, 35, 0.5, 0.4)
        y -= 42
    pdf.add_text(72, y - 5, "New activities I tried this week:", 'F2', 9)
    pdf.add_line(72, y - 22, 540, y - 22, 0.5, 0.5)
    pdf.add_text(72, y - 40, "Mood improvement noticed (1-10):", 'F2', 9)
    pdf.add_line(280, y - 42, 350, y - 42, 0.5, 0.5)


    # Page 24: Behavioral Activation Schedule 4
    pdf.new_page()
    pdf.add_centered_text(740, "BEHAVIORAL ACTIVATION SCHEDULE - Week 4", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Maintain momentum. Focus on sustainability.", 'F2', 10)
    y = 680
    pdf.add_text(72, y, "", 'F2', 8)
    for i, d in enumerate(dys):
        pdf.add_text(130 + i * 58, y, d, 'F2', 8)
    y -= 15
    for t in times:
        pdf.add_text(72, y, t, 'F1', 8)
        for i in range(7):
            pdf.add_rect(130 + i * 58, y - 10, 54, 35, 0.5, 0.4)
        y -= 42
    pdf.add_text(72, y - 5, "Activities I want to keep doing permanently:", 'F2', 9)
    pdf.add_line(72, y - 22, 540, y - 22, 0.5, 0.5)
    pdf.add_line(72, y - 40, 540, y - 40, 0.5, 0.5)

    # Page 25: Final Reflection & Moving Forward
    pdf.new_page()
    pdf.add_centered_text(740, "MOVING FORWARD: MY ONGOING PLAN", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    fields = [
        ("CBT skills that work best for me:", 3),
        ("My daily non-negotiables (things I do every day):", 3),
        ("My weekly non-negotiables:", 3),
        ("My warning signs to watch for:", 3),
        ("When I notice warning signs, I will:", 3),
        ("My reason for continuing to fight depression:", 2),
        ("What I want my life to look like in 6 months:", 3),
    ]
    for label, lines in fields:
        pdf.add_text(72, y, label, 'F2', 10)
        y -= 16
        for _ in range(lines):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 8

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book91_CBT_Depression_Workbook.pdf')
    print("Book91_CBT_Depression_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
