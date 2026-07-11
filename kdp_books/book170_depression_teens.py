from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1: Title Page
pdf.new_page()
pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
pdf.add_centered_text(520, "WHEN EVERYTHING", "F2", 28)
pdf.add_centered_text(485, "FEELS HEAVY", "F2", 28)
pdf.add_centered_text(430, "A Depression Workbook for Teens", "F4", 18, gray=0.3)
pdf.add_line(180, 415, 432, 415, 2, gray=0.5)
pdf.add_centered_text(350, "Understanding Your Feelings", "F1", 14, gray=0.4)
pdf.add_centered_text(330, "Building Coping Skills", "F1", 14, gray=0.4)
pdf.add_centered_text(310, "Finding Your Way Back", "F1", 14, gray=0.4)
pdf.add_centered_text(200, author, "F2", 14)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, "WHEN EVERYTHING FEELS HEAVY", "F2", 14)
pdf.add_centered_text(480, "A Depression Workbook for Teens", "F1", 12)
pdf.add_centered_text(440, f"Copyright (c) 2025 {author}", "F1", 11)
pdf.add_centered_text(420, "All rights reserved.", "F1", 11)
pdf.add_centered_text(380, "This workbook is not a substitute for professional mental health treatment.", "F1", 10)
pdf.add_centered_text(365, "If you are in crisis, contact 988 Suicide & Crisis Lifeline", "F1", 10)
pdf.add_centered_text(345, "or text HOME to 741741 (Crisis Text Line).", "F1", 10)
pdf.add_centered_text(300, "ISBN: 979-8-XXX-XXXXX-X", "F3", 10)

# Page 3: What is Depression (teen-friendly)
pdf.new_page()
pdf.add_centered_text(740, "WHAT IS DEPRESSION?", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 690, "Depression is more than just feeling sad. It's a real medical condition that", "F1", 12)
pdf.add_text(50, 672, "affects how you think, feel, and handle daily activities.", "F1", 12)
pdf.add_text(50, 640, "It's like your brain's 'mood thermostat' gets stuck on low.", "F2", 12)
pdf.add_text(50, 610, "Signs that you might be dealing with depression:", "F1", 12)
pdf.add_filled_rect(60, 572, 490, 22, gray=0.92)
pdf.add_text(70, 578, "* Feeling sad, empty, or hopeless most of the day, nearly every day", "F1", 11)
pdf.add_filled_rect(60, 548, 490, 22, gray=0.92)
pdf.add_text(70, 554, "* Lost interest in things you used to enjoy (hobbies, friends, sports)", "F1", 11)
pdf.add_filled_rect(60, 524, 490, 22, gray=0.92)
pdf.add_text(70, 530, "* Sleeping way too much OR not being able to sleep at all", "F1", 11)
pdf.add_filled_rect(60, 500, 490, 22, gray=0.92)
pdf.add_text(70, 506, "* Feeling exhausted even when you haven't done anything", "F1", 11)
pdf.add_filled_rect(60, 476, 490, 22, gray=0.92)
pdf.add_text(70, 482, "* Trouble concentrating on schoolwork or conversations", "F1", 11)
pdf.add_filled_rect(60, 452, 490, 22, gray=0.92)
pdf.add_text(70, 458, "* Feeling worthless or guilty about everything", "F1", 11)
pdf.add_filled_rect(60, 428, 490, 22, gray=0.92)
pdf.add_text(70, 434, "* Thoughts of death or suicide (please tell someone if this is you)", "F1", 11)
pdf.add_text(50, 390, "How many of these apply to you right now? Circle them above.", "F1", 12)
pdf.add_text(50, 360, "How long have you been feeling this way?", "F1", 12)
pdf.add_line(50, 340, 400, 340, 0.5)
pdf.add_text(50, 310, "On a scale of 1-10, how much is this affecting your daily life?", "F1", 12)
pdf.add_rect(50, 275, 30, 25)
pdf.add_text(55, 282, "/10", "F1", 12)


# Page 4: You're Not Broken (normalization)
pdf.new_page()
pdf.add_centered_text(740, "YOU'RE NOT BROKEN", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 690, "Let's get something straight:", "F1", 12)
pdf.add_text(50, 660, "Depression is NOT:", "F2", 13)
pdf.add_text(70, 638, "- A sign of weakness", "F1", 12)
pdf.add_text(70, 618, "- Something you can just 'snap out of'", "F1", 12)
pdf.add_text(70, 598, "- Your fault", "F1", 12)
pdf.add_text(70, 578, "- A character flaw", "F1", 12)
pdf.add_text(70, 558, "- Something to be ashamed of", "F1", 12)
pdf.add_text(50, 520, "Depression IS:", "F2", 13)
pdf.add_text(70, 498, "- A medical condition involving brain chemistry", "F1", 12)
pdf.add_text(70, 478, "- Incredibly common (1 in 5 teens experience it)", "F1", 12)
pdf.add_text(70, 458, "- Treatable with the right support", "F1", 12)
pdf.add_text(70, 438, "- Something many successful people have dealt with", "F1", 12)
pdf.add_text(70, 418, "- A chapter, not your whole story", "F1", 12)
pdf.add_filled_rect(50, 350, 512, 50, gray=0.92)
pdf.add_text(60, 380, "Write one thing you want people to know about your experience:", "F2", 11)
pdf.add_line(60, 360, 540, 360, 0.5)
pdf.add_text(50, 310, "What messages have you received about depression that aren't helpful?", "F1", 12)
pdf.add_line(50, 290, 562, 290, 0.5)
pdf.add_line(50, 268, 562, 268, 0.5)
pdf.add_line(50, 246, 562, 246, 0.5)
pdf.add_text(50, 210, "What would you tell a friend who was going through the same thing?", "F1", 12)
pdf.add_line(50, 190, 562, 190, 0.5)
pdf.add_line(50, 168, 562, 168, 0.5)
pdf.add_line(50, 146, 562, 146, 0.5)

# Page 5: Mood-Activity Connection
pdf.new_page()
pdf.add_centered_text(740, "THE MOOD-ACTIVITY CONNECTION", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 690, "Here's something scientists have discovered about depression:", "F1", 12)
pdf.add_filled_rect(50, 645, 512, 35, gray=0.9)
pdf.add_text(60, 665, "When you're depressed, you stop doing things.", "F2", 12)
pdf.add_text(60, 650, "When you stop doing things, you get more depressed. It's a cycle.", "F2", 12)
pdf.add_text(50, 615, "The good news? You can break this cycle by GENTLY adding activities", "F1", 12)
pdf.add_text(50, 597, "back into your life - even tiny ones.", "F1", 12)
pdf.add_text(50, 565, "This is called BEHAVIORAL ACTIVATION. It works like this:", "F2", 12)
pdf.add_text(70, 540, "1. You do a small activity (even if you don't feel like it)", "F1", 12)
pdf.add_text(70, 520, "2. Your brain gets a tiny boost of feel-good chemicals", "F1", 12)
pdf.add_text(70, 500, "3. You feel slightly better (even 1% counts!)", "F1", 12)
pdf.add_text(70, 480, "4. That makes the next activity a little easier", "F1", 12)
pdf.add_text(50, 440, "Track your mood before and after an activity this week:", "F1", 12)
pdf.add_text(50, 415, "Activity:", "F2", 11)
pdf.add_line(120, 415, 400, 415, 0.5)
pdf.add_text(50, 393, "Mood BEFORE (1-10):", "F1", 11)
pdf.add_rect(200, 385, 30, 20)
pdf.add_text(50, 370, "Mood AFTER (1-10):", "F1", 11)
pdf.add_rect(200, 362, 30, 20)
pdf.add_text(50, 340, "What did you notice?", "F1", 11)
pdf.add_line(50, 320, 562, 320, 0.5)
pdf.add_line(50, 298, 562, 298, 0.5)


# Page 6: My Activity Menu
pdf.new_page()
pdf.add_centered_text(740, "MY ACTIVITY MENU", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Not every day has the same energy. Create your personal menu:", "F1", 12)
pdf.add_filled_rect(50, 645, 512, 30, gray=0.85)
pdf.add_text(60, 655, "LOW ENERGY ACTIVITIES (when getting out of bed is hard)", "F2", 12)
pdf.add_text(60, 625, "Examples: listen to a song, pet an animal, open a window, drink water", "F1", 10, gray=0.4)
for i in range(5):
    pdf.add_text(60, 600 - i*22, f"{i+1}.", "F1", 11)
    pdf.add_line(80, 600 - i*22, 540, 600 - i*22, 0.5)
pdf.add_filled_rect(50, 470, 512, 30, gray=0.85)
pdf.add_text(60, 480, "MEDIUM ENERGY ACTIVITIES (when you can manage a little more)", "F2", 12)
pdf.add_text(60, 450, "Examples: take a shower, text a friend, go for a short walk, draw", "F1", 10, gray=0.4)
for i in range(5):
    pdf.add_text(60, 425 - i*22, f"{i+1}.", "F1", 11)
    pdf.add_line(80, 425 - i*22, 540, 425 - i*22, 0.5)
pdf.add_filled_rect(50, 295, 512, 30, gray=0.85)
pdf.add_text(60, 305, "HIGH ENERGY ACTIVITIES (for your better days)", "F2", 12)
pdf.add_text(60, 275, "Examples: exercise, hang out with friends, cook something, create art", "F1", 10, gray=0.4)
for i in range(5):
    pdf.add_text(60, 250 - i*22, f"{i+1}.", "F1", 11)
    pdf.add_line(80, 250 - i*22, 540, 250 - i*22, 0.5)

# Page 7: Thought Patterns in Depression
pdf.new_page()
pdf.add_centered_text(740, "THOUGHT PATTERNS IN DEPRESSION", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Depression doesn't just affect your mood - it changes how you THINK.", "F1", 12)
pdf.add_text(50, 675, "These are called 'cognitive distortions' - thinking traps that feel real", "F1", 12)
pdf.add_text(50, 655, "but are actually your depression talking.", "F1", 12)
pdf.add_filled_rect(50, 610, 512, 35, gray=0.92)
pdf.add_text(60, 630, "ALL-OR-NOTHING THINKING", "F2", 12)
pdf.add_text(60, 615, "Seeing things in black and white: 'I failed one test = I'm a total failure'", "F1", 11)
pdf.add_filled_rect(50, 565, 512, 35, gray=0.92)
pdf.add_text(60, 585, "CATASTROPHIZING", "F2", 12)
pdf.add_text(60, 570, "Assuming the worst: 'My friend didn't text back = they hate me'", "F1", 11)
pdf.add_filled_rect(50, 520, 512, 35, gray=0.92)
pdf.add_text(60, 540, "MENTAL FILTER", "F2", 12)
pdf.add_text(60, 525, "Only seeing the negative: 'I got 9 compliments but focus on 1 criticism'", "F1", 11)
pdf.add_filled_rect(50, 475, 512, 35, gray=0.92)
pdf.add_text(60, 495, "MIND READING", "F2", 12)
pdf.add_text(60, 480, "Assuming you know what others think: 'Everyone thinks I'm weird'", "F1", 11)
pdf.add_filled_rect(50, 430, 512, 35, gray=0.92)
pdf.add_text(60, 450, "SHOULD STATEMENTS", "F2", 12)
pdf.add_text(60, 435, "'I should be happy' 'I should be over this by now' - adding guilt to pain", "F1", 11)
pdf.add_text(50, 395, "Which of these thinking traps do you fall into most often?", "F1", 12)
pdf.add_line(50, 375, 562, 375, 0.5)
pdf.add_text(50, 350, "Write a recent example of one of these traps:", "F1", 12)
pdf.add_line(50, 330, 562, 330, 0.5)
pdf.add_line(50, 308, 562, 308, 0.5)
pdf.add_line(50, 286, 562, 286, 0.5)


# Pages 8-12: Challenging Negative Thoughts (5 pages)
for pg in range(5):
    pdf.new_page()
    pdf.add_centered_text(740, f"CHALLENGING NEGATIVE THOUGHTS ({pg+1}/5)", "F2", 18)
    pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
    pdf.add_text(50, 695, "Use this worksheet to challenge a negative thought:", "F1", 12)
    pdf.add_text(50, 665, "The negative thought:", "F2", 12)
    pdf.add_line(50, 645, 562, 645, 0.5)
    pdf.add_line(50, 623, 562, 623, 0.5)
    pdf.add_text(50, 595, "Which thinking trap is this? (circle one)", "F2", 12)
    pdf.add_text(70, 573, "All-or-Nothing / Catastrophizing / Mental Filter / Mind Reading / Should", "F1", 11)
    pdf.add_text(50, 545, "What evidence SUPPORTS this thought?", "F2", 12)
    pdf.add_line(50, 525, 562, 525, 0.5)
    pdf.add_line(50, 503, 562, 503, 0.5)
    pdf.add_text(50, 475, "What evidence is AGAINST this thought?", "F2", 12)
    pdf.add_line(50, 455, 562, 455, 0.5)
    pdf.add_line(50, 433, 562, 433, 0.5)
    pdf.add_text(50, 405, "What would I tell a friend who had this thought?", "F2", 12)
    pdf.add_line(50, 385, 562, 385, 0.5)
    pdf.add_line(50, 363, 562, 363, 0.5)
    pdf.add_text(50, 335, "A more balanced thought:", "F2", 12)
    pdf.add_rect(50, 285, 512, 45)
    pdf.add_text(50, 260, "How do I feel after reframing? (1-10):", "F1", 12)
    pdf.add_rect(310, 252, 30, 20)

# Page 13: Building Your Support Team
pdf.new_page()
pdf.add_centered_text(740, "BUILDING YOUR SUPPORT TEAM", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "You don't have to do this alone. Who are your people?", "F1", 12)
roles = [
    "Person I can call when I'm having a bad day:",
    "Person I can be totally honest with:",
    "Adult I trust (teacher, counselor, coach, etc.):",
    "Friend who makes me laugh:",
    "Person who checks in on me:",
    "Professional support (therapist, doctor):",
    "Online community or group that helps:"
]
y = 660
for role in roles:
    pdf.add_text(50, y, role, "F2", 11)
    pdf.add_line(50, y - 18, 562, y - 18, 0.5)
    pdf.add_text(50, y - 35, "Their number/contact:", "F1", 10, gray=0.4)
    pdf.add_line(200, y - 35, 400, y - 35, 0.5)
    y -= 70
pdf.add_filled_rect(50, 80, 512, 40, gray=0.92)
pdf.add_text(60, 105, "Remember: Asking for help is a sign of STRENGTH, not weakness.", "F2", 11)

# Page 14: Self-Care When You Have Zero Energy
pdf.new_page()
pdf.add_centered_text(740, "SELF-CARE WITH ZERO ENERGY", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "When depression steals your energy, even basic self-care feels impossible.", "F1", 12)
pdf.add_text(50, 675, "Here's a 'bare minimum' self-care checklist for your hardest days:", "F1", 12)
basics = [
    "Drink one glass of water",
    "Eat something (anything counts)",
    "Change your shirt (if nothing else)",
    "Open a window or step outside for 60 seconds",
    "Brush your teeth (or at least rinse)",
    "Send one text to someone (even just an emoji)",
    "Take your medication (if prescribed)",
    "Set one alarm for tomorrow"
]
y = 640
for item in basics:
    pdf.add_rect(55, y - 3, 15, 15)
    pdf.add_text(80, y, item, "F1", 12)
    y -= 30
pdf.add_text(50, y - 20, "On my hardest days, the ONE thing I can always do is:", "F2", 12)
pdf.add_line(50, y - 42, 562, y - 42, 0.5)
pdf.add_text(50, y - 70, "It's okay if this is all you can manage. Every small thing counts.", "F4", 12, gray=0.3)


# Page 15: Social Media & Mood Audit
pdf.new_page()
pdf.add_centered_text(740, "SOCIAL MEDIA & MOOD AUDIT", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Social media can make depression worse. Let's audit your feeds:", "F1", 12)
pdf.add_text(50, 665, "How much time do you spend on social media daily?", "F1", 12)
pdf.add_line(50, 645, 250, 645, 0.5)
pdf.add_text(50, 620, "How do you USUALLY feel after scrolling? (circle)", "F2", 12)
pdf.add_text(70, 598, "Worse  /  The Same  /  Better  /  Numb  /  Anxious  /  Lonely", "F1", 12)
pdf.add_text(50, 565, "Accounts that make me feel BAD about myself:", "F2", 12)
for i in range(3):
    pdf.add_line(50, 540 - i*22, 400, 540 - i*22, 0.5)
pdf.add_text(50, 470, "Accounts that make me feel GOOD or inspired:", "F2", 12)
for i in range(3):
    pdf.add_line(50, 445 - i*22, 400, 445 - i*22, 0.5)
pdf.add_text(50, 375, "My social media boundaries:", "F2", 12)
pdf.add_rect(55, 345, 15, 15)
pdf.add_text(80, 348, "No phone 30 min before bed", "F1", 11)
pdf.add_rect(55, 323, 15, 15)
pdf.add_text(80, 326, "Unfollow/mute accounts that trigger me", "F1", 11)
pdf.add_rect(55, 301, 15, 15)
pdf.add_text(80, 304, "Time limit of ___ minutes per day", "F1", 11)
pdf.add_rect(55, 279, 15, 15)
pdf.add_text(80, 282, "No comparing myself to others' highlight reels", "F1", 11)
pdf.add_rect(55, 257, 15, 15)
pdf.add_text(80, 260, "Other: ___________________", "F1", 11)

# Page 16: Sleep for Depression
pdf.new_page()
pdf.add_centered_text(740, "SLEEP & DEPRESSION", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Depression and sleep have a two-way relationship:", "F1", 12)
pdf.add_text(50, 675, "Poor sleep makes depression worse, and depression disrupts sleep.", "F1", 12)
pdf.add_text(50, 645, "My current sleep pattern:", "F2", 12)
pdf.add_text(70, 623, "I usually go to bed at: ________", "F1", 12)
pdf.add_text(70, 601, "I usually wake up at: ________", "F1", 12)
pdf.add_text(70, 579, "Hours of sleep I get: ________", "F1", 12)
pdf.add_text(70, 557, "Quality (1-10): ________", "F1", 12)
pdf.add_text(50, 520, "Sleep Hygiene Tips for Depression:", "F2", 13)
tips = [
    "Same bedtime and wake time (even weekends)",
    "No screens 1 hour before bed (blue light blocks melatonin)",
    "Keep your room cool and dark",
    "Use bed ONLY for sleep (not homework, scrolling, worrying)",
    "If you can't sleep after 20 min, get up and do something calm",
    "Avoid caffeine after 2 PM",
    "Try a relaxation routine: breathing, stretching, or meditation"
]
y = 490
for tip in tips:
    pdf.add_text(70, y, f"- {tip}", "F1", 11)
    y -= 22
pdf.add_text(50, y - 20, "One sleep change I'll try this week:", "F2", 12)
pdf.add_line(50, y - 40, 562, y - 40, 0.5)


# Pages 17-24: Weekly Mood & Activity Tracker (8 pages)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for week in range(8):
    pdf.new_page()
    pdf.add_centered_text(740, f"WEEKLY MOOD & ACTIVITY TRACKER - WEEK {week+1}", "F2", 16)
    pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
    y = 700
    for day in days:
        pdf.add_filled_rect(50, y - 5, 512, 18, gray=0.92)
        pdf.add_text(55, y, day, "F2", 10)
        pdf.add_text(140, y, "Mood (1-10): ___", "F1", 9)
        pdf.add_text(260, y, "Activity: _______________", "F1", 9)
        pdf.add_text(440, y, "Sleep: ___ hrs", "F1", 9)
        y -= 22
        pdf.add_text(55, y, "Energy: ___/10", "F1", 9)
        pdf.add_text(170, y, "Thought trap noticed: _______________", "F1", 9)
        pdf.add_text(440, y, "Self-care: Y/N", "F1", 9)
        y -= 28
    pdf.add_text(50, y - 10, "This week's overall mood average: ___/10", "F2", 11)
    pdf.add_text(50, y - 30, "One thing that helped this week:", "F1", 11)
    pdf.add_line(50, y - 48, 562, y - 48, 0.5)
    pdf.add_text(50, y - 68, "One challenge I faced:", "F1", 11)
    pdf.add_line(50, y - 86, 562, y - 86, 0.5)
    pdf.add_text(50, y - 106, "Something I'm proud of (no matter how small):", "F1", 11)
    pdf.add_line(50, y - 124, 562, y - 124, 0.5)

# Page 25: Crisis Safety Plan
pdf.new_page()
pdf.add_centered_text(740, "MY CRISIS SAFETY PLAN", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_filled_rect(50, 690, 512, 25, gray=0.85)
pdf.add_text(60, 697, "Fill this out NOW so you have it when you need it most.", "F2", 12)
pdf.add_text(50, 660, "Warning signs that I'm in crisis:", "F2", 12)
pdf.add_line(50, 640, 562, 640, 0.5)
pdf.add_line(50, 618, 562, 618, 0.5)
pdf.add_text(50, 590, "Things I can do to distract myself:", "F2", 12)
pdf.add_line(50, 570, 562, 570, 0.5)
pdf.add_line(50, 548, 562, 548, 0.5)
pdf.add_text(50, 520, "People I can reach out to:", "F2", 12)
pdf.add_text(70, 498, "1. Name: _____________ Phone: _____________", "F1", 11)
pdf.add_text(70, 476, "2. Name: _____________ Phone: _____________", "F1", 11)
pdf.add_text(70, 454, "3. Name: _____________ Phone: _____________", "F1", 11)
pdf.add_text(50, 424, "Professional help:", "F2", 12)
pdf.add_text(70, 402, "My therapist/counselor: _____________ Phone: _____________", "F1", 11)
pdf.add_text(70, 380, "Local crisis center: _____________", "F1", 11)
pdf.add_text(50, 350, "Places I feel safe:", "F2", 12)
pdf.add_line(50, 330, 562, 330, 0.5)
pdf.add_text(50, 300, "Reasons I want to keep going:", "F2", 12)
pdf.add_line(50, 280, 562, 280, 0.5)
pdf.add_line(50, 258, 562, 258, 0.5)
pdf.add_line(50, 236, 562, 236, 0.5)
pdf.add_filled_rect(50, 170, 512, 50, gray=0.9)
pdf.add_text(60, 203, "EMERGENCY: Call 988 (Suicide & Crisis Lifeline)", "F2", 12)
pdf.add_text(60, 183, "Text HOME to 741741 (Crisis Text Line) | Go to nearest ER", "F2", 11)


# Page 26: Resources for Teens
pdf.new_page()
pdf.add_centered_text(740, "RESOURCES FOR TEENS", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "You deserve support. Here are real resources that can help:", "F1", 12)
pdf.add_filled_rect(50, 655, 512, 35, gray=0.92)
pdf.add_text(60, 675, "988 Suicide & Crisis Lifeline", "F2", 12)
pdf.add_text(60, 660, "Call or text 988 - Free, 24/7, confidential", "F1", 11)
pdf.add_filled_rect(50, 610, 512, 35, gray=0.92)
pdf.add_text(60, 630, "Crisis Text Line", "F2", 12)
pdf.add_text(60, 615, "Text HOME to 741741 - Free, 24/7, trained counselors", "F1", 11)
pdf.add_filled_rect(50, 565, 512, 35, gray=0.92)
pdf.add_text(60, 585, "Teen Line", "F2", 12)
pdf.add_text(60, 570, "Call 1-800-852-8336 (6-10 PM PST) - Teens helping teens", "F1", 11)
pdf.add_filled_rect(50, 520, 512, 35, gray=0.92)
pdf.add_text(60, 540, "NAMI (National Alliance on Mental Illness)", "F2", 12)
pdf.add_text(60, 525, "nami.org - Info, support groups, helpline: 1-800-950-6264", "F1", 11)
pdf.add_filled_rect(50, 475, 512, 35, gray=0.92)
pdf.add_text(60, 495, "The Trevor Project (LGBTQ+ youth)", "F2", 12)
pdf.add_text(60, 480, "Call 1-866-488-7386 or text START to 678-678", "F1", 11)
pdf.add_filled_rect(50, 430, 512, 35, gray=0.92)
pdf.add_text(60, 450, "Your School Counselor", "F2", 12)
pdf.add_text(60, 435, "Free, confidential, and they WANT to help you", "F1", 11)
pdf.add_text(50, 390, "My personal resource list:", "F2", 12)
pdf.add_text(70, 368, "Therapist name: _______________________________", "F1", 11)
pdf.add_text(70, 346, "Doctor name: _______________________________", "F1", 11)
pdf.add_text(70, 324, "Trusted adult: _______________________________", "F1", 11)
pdf.add_text(70, 302, "App I use: _______________________________", "F1", 11)

# Page 27: Letter to Myself on Good Days (page 1)
pdf.new_page()
pdf.add_centered_text(740, "A LETTER TO MYSELF ON GOOD DAYS", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Write this letter when you're having a GOOD day.", "F1", 12)
pdf.add_text(50, 675, "Read it when the darkness comes back. Trust your good-day self.", "F1", 12)
pdf.add_text(50, 640, "Dear future me,", "F4", 13)
pdf.add_text(50, 615, "Right now I'm feeling:", "F1", 12)
pdf.add_line(50, 595, 562, 595, 0.5)
y = 570
for i in range(15):
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 22
pdf.add_text(50, y - 10, "Things that helped me get here:", "F2", 12)
pdf.add_line(50, y - 30, 562, y - 30, 0.5)
pdf.add_line(50, y - 52, 562, y - 52, 0.5)
pdf.add_line(50, y - 74, 562, y - 74, 0.5)

# Page 28: Letter continued
pdf.new_page()
pdf.add_centered_text(740, "LETTER TO MYSELF (CONTINUED)", "F2", 18)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Reminders for when it gets hard again:", "F2", 12)
y = 670
for i in range(8):
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 22
pdf.add_text(50, y - 10, "What I want you to remember about yourself:", "F2", 12)
y -= 30
for i in range(8):
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 22
pdf.add_text(50, y - 10, "With love from your good-day self,", "F4", 13)
pdf.add_line(50, y - 40, 250, y - 40, 0.5)
pdf.add_text(50, y - 55, "(your name)", "F1", 10, gray=0.5)
pdf.add_text(50, y - 80, "Date written: _______________", "F1", 11)


# Page 29: Healing is Not Linear
pdf.new_page()
pdf.add_centered_text(740, "HEALING IS NOT LINEAR", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 690, "Some days will be harder than others. That doesn't mean you're failing.", "F1", 12)
pdf.add_text(50, 660, "Recovery looks like:", "F2", 13)
pdf.add_text(70, 635, "- Two good days, one bad day, three okay days", "F1", 12)
pdf.add_text(70, 613, "- Feeling better, then feeling worse, then better again", "F1", 12)
pdf.add_text(70, 591, "- Needing help even after you thought you were 'fine'", "F1", 12)
pdf.add_text(70, 569, "- Celebrating tiny victories", "F1", 12)
pdf.add_text(70, 547, "- Being patient with yourself", "F1", 12)
pdf.add_text(50, 510, "Progress I've made (even if it feels small):", "F2", 12)
for i in range(5):
    pdf.add_text(60, 485 - i*25, f"{i+1}.", "F1", 11)
    pdf.add_line(80, 485 - i*25, 562, 485 - i*25, 0.5)
pdf.add_text(50, 350, "Things I can do now that I couldn't before:", "F2", 12)
for i in range(5):
    pdf.add_text(60, 325 - i*25, f"{i+1}.", "F1", 11)
    pdf.add_line(80, 325 - i*25, 562, 325 - i*25, 0.5)
pdf.add_filled_rect(50, 150, 512, 40, gray=0.92)
pdf.add_centered_text(175, "You are still here. That takes incredible strength.", "F5", 14)

# Page 30: Final Page - You Matter
pdf.new_page()
pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
pdf.add_centered_text(550, "YOU MATTER.", "F2", 36)
pdf.add_centered_text(490, "Your feelings are valid.", "F4", 16, gray=0.3)
pdf.add_centered_text(460, "Your struggles are real.", "F4", 16, gray=0.3)
pdf.add_centered_text(430, "Your future is worth fighting for.", "F4", 16, gray=0.3)
pdf.add_line(180, 400, 432, 400, 2, gray=0.5)
pdf.add_centered_text(360, "If you need help right now:", "F2", 14)
pdf.add_centered_text(335, "Call or text 988", "F1", 14)
pdf.add_centered_text(310, "Text HOME to 741741", "F1", 14)
pdf.add_centered_text(250, "Keep going. Keep fighting.", "F5", 18)
pdf.add_centered_text(220, "You are not alone.", "F5", 18)
pdf.add_centered_text(150, f"Written with care by {author}", "F1", 11, gray=0.5)

pdf.save("Book170_Depression_Workbook_Teens.pdf")
print("SUCCESS: Book170_Depression_Workbook_Teens.pdf created (30 pages)")
