#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "RELEASING SHAME", 'F2', 26)
pdf.add_centered_text(480, "A Guided Workbook for Healing", 'F4', 15)
pdf.add_centered_text(440, f"By {author}", 'F4', 12)
pdf.add_line(150, 420, 462, 420, 2)
pdf.add_centered_text(380, "You are worthy of belonging.", 'F4', 12, 0.3)

# Page 2 - Copyright
pdf.new_page()
pdf.add_centered_text(500, f"Copyright - {author}", 'F1', 10)
pdf.add_centered_text(480, "All rights reserved.", 'F1', 10)
pdf.add_centered_text(440, "This workbook is for educational purposes only.", 'F1', 10)
pdf.add_centered_text(420, "Not a substitute for professional therapy.", 'F1', 10)

# Page 3 - Shame vs Guilt
pdf.new_page()
pdf.add_centered_text(740, "UNDERSTANDING SHAME VS GUILT", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 700, "GUILT says: 'I did something bad.'", 'F2', 12)
pdf.add_text(50, 680, "SHAME says: 'I AM bad.'", 'F2', 12)
pdf.add_text(50, 650, "Guilt is about behavior. Shame is about identity.", 'F1', 11)
pdf.add_text(50, 630, "Guilt can be productive - it motivates us to change.", 'F1', 11)
pdf.add_text(50, 610, "Shame is NEVER productive - it keeps us stuck.", 'F1', 11)
pdf.add_text(50, 580, "Where shame comes from:", 'F2', 12)
sources = ["Family messages ('You're too much', 'You'll never be enough')",
           "Cultural/religious messages about worthiness",
           "Trauma and abuse (making us feel fundamentally broken)",
           "Perfectionism (anything less than perfect = failure = shame)",
           "Comparison and social media"]
y = 560
for s in sources:
    pdf.add_text(60, y, f"- {s}", 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "MY SHAME MESSAGES:", 'F2', 12)
pdf.add_text(50, y-32, "What shame tells me about myself:", 'F1', 11)
y -= 50
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y-5, "Where I first learned this message:", 'F1', 11)
pdf.add_line(60, y-22, 540, y-22, 0.5, 0.7)

# Page 4 - Shame Triggers Inventory
pdf.new_page()
pdf.add_centered_text(740, "SHAME TRIGGERS INVENTORY", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Shame is triggered in specific areas. Rate each 1-10:", 'F1', 11)
triggers = [
    "Appearance/body", "Intelligence/competence", "Parenting",
    "Work/career performance", "Sexuality/intimacy", "Money/financial status",
    "Being a good friend/partner", "Mental health", "Addiction/habits",
    "Aging", "Relationships/belonging", "Motherhood/fatherhood",
    "Religion/spirituality", "Being seen/vulnerability"
]
y = 680
for t in triggers:
    pdf.add_text(60, y, t, 'F1', 10)
    pdf.add_text(350, y, "___/10", 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "My top 3 shame triggers:", 'F2', 11)
y -= 35
for i in range(3):
    pdf.add_text(50, y, f"{i+1}.", 'F1', 11)
    pdf.add_line(70, y-2, 540, y-2, 0.5, 0.7)
    y -= 25


# Page 5 - The Shame Spiral
pdf.new_page()
pdf.add_centered_text(740, "THE SHAME SPIRAL", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Shame creates a downward spiral. Recognizing it is the first step out.", 'F1', 11)
pdf.add_text(50, 675, "THE CYCLE:", 'F2', 12)
cycle = ["1. TRIGGER: Something happens (criticism, failure, rejection)",
         "2. PHYSICAL: Body responds (face flush, chest tight, stomach drop)",
         "3. THOUGHT: 'I'm not enough' / 'Something is wrong with me'",
         "4. EMOTION: Shame floods in (feels like drowning)",
         "5. BEHAVIOR: Hide, withdraw, lash out, numb, or overachieve",
         "6. ISOLATION: Shame thrives in secrecy and silence",
         "7. REINFORCEMENT: Isolation confirms 'I don't belong'"]
y = 650
for c in cycle:
    pdf.add_text(60, y, c, 'F1', 10)
    y -= 20
pdf.add_text(50, y-15, "INTERRUPTING THE SPIRAL:", 'F2', 12)
y -= 35
interrupts = ["Name it: 'I'm feeling shame right now.'",
              "Share it: Tell one safe person.",
              "Normalize it: 'Everyone feels this sometimes.'",
              "Self-compassion: 'I'm human. This is part of being human.'"]
for intr in interrupts:
    pdf.add_text(60, y, f"- {intr}", 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "MY SHAME SPIRAL:", 'F2', 11)
pdf.add_text(50, y-32, "My trigger: _______________________________________", 'F1', 10)
pdf.add_text(50, y-50, "My body signal: ___________________________________", 'F1', 10)
pdf.add_text(50, y-68, "My shame thought: _________________________________", 'F1', 10)
pdf.add_text(50, y-86, "My typical behavior: _______________________________", 'F1', 10)
pdf.add_text(50, y-104, "How I can interrupt: _______________________________", 'F1', 10)

# Page 6 - Shame Resilience Theory
pdf.new_page()
pdf.add_centered_text(740, "SHAME RESILIENCE", 'F2', 16)
pdf.add_centered_text(720, "(Based on Brene Brown's Research)", 'F4', 11, 0.4)
pdf.add_line(50, 710, 562, 710, 1)
pdf.add_text(50, 685, "Shame resilience is the ability to move through shame without losing yourself.", 'F1', 11)
pdf.add_text(50, 660, "THE FOUR ELEMENTS:", 'F2', 12)
elements = [
    ("1. Recognizing Shame", "Know your physical symptoms, triggers, and messages"),
    ("2. Critical Awareness", "Reality-check the expectations causing your shame"),
    ("3. Reaching Out", "Share your story with someone who has earned the right to hear it"),
    ("4. Speaking Shame", "Name it. Shame cannot survive being spoken aloud"),
]
y = 635
for title, desc in elements:
    pdf.add_text(60, y, title, 'F2', 11)
    pdf.add_text(60, y-16, desc, 'F1', 10)
    y -= 42
pdf.add_text(50, y, "MY SHAME RESILIENCE PLAN:", 'F2', 12)
y -= 20
pdf.add_text(50, y, "I recognize shame in my body by: ____________________________", 'F1', 10)
y -= 22
pdf.add_text(50, y, "The expectation I need to reality-check: _____________________", 'F1', 10)
y -= 22
pdf.add_text(50, y, "Safe person I can reach out to: _____________________________", 'F1', 10)
y -= 22
pdf.add_text(50, y, "How I will speak my shame: _________________________________", 'F1', 10)

# Page 7 - Critical Inner Voice
pdf.new_page()
pdf.add_centered_text(740, "CRITICAL INNER VOICE IDENTIFICATION", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "The shame voice often sounds like someone from our past.", 'F1', 11)
pdf.add_text(50, 685, "Whose voice is your inner critic? _________________________", 'F1', 11)
pdf.add_text(50, 655, "COMMON SHAME VOICE MESSAGES:", 'F2', 11)
messages = ["'You're not good enough'", "'Who do you think you are?'",
            "'You don't deserve good things'", "'Everyone can see you're a fraud'",
            "'You're too much/not enough'", "'You'll never change'"]
y = 635
for m in messages:
    pdf.add_rect(55, y-9, 12, 12)
    pdf.add_text(75, y-7, m, 'F4', 10)
    y -= 22
pdf.add_text(50, y-10, "MY inner critic says:", 'F2', 11)
y -= 30
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y-5, "REWRITING THE VOICE (what is actually TRUE?):", 'F2', 11)
y -= 25
for i in range(4):
    pdf.add_text(50, y, f"Critic says: _________________ Truth: _________________", 'F1', 10)
    y -= 30


# Pages 8-12 - Rewriting Shame Narratives (5 pages)
for pg in range(5):
    pdf.new_page()
    pdf.add_centered_text(740, f"REWRITING SHAME NARRATIVES - {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, "THE SHAME STORY:", 'F2', 11)
    pdf.add_text(50, 692, "What happened (just the facts): ", 'F1', 10)
    y = 672
    for i in range(3):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "What shame told me it meant about me:", 'F1', 10)
    y -= 22
    for i in range(2):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "THE REWRITE:", 'F2', 11)
    y -= 22
    pdf.add_text(50, y, "What actually happened (with compassion):", 'F1', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "What is TRUE about me:", 'F1', 10)
    y -= 18
    for i in range(2):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "What would I say to a friend in this situation?", 'F1', 10)
    y -= 18
    for i in range(3):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "My new narrative (one sentence):", 'F2', 10)
    pdf.add_line(60, y-22, 540, y-22, 0.5, 0.7)

# Page 13 - Self-Compassion Exercises
pdf.new_page()
pdf.add_centered_text(740, "SELF-COMPASSION EXERCISES", 'F2', 16)
pdf.add_centered_text(720, "(Based on Kristin Neff's Research)", 'F4', 11, 0.4)
pdf.add_line(50, 710, 562, 710, 1)
pdf.add_text(50, 685, "THREE COMPONENTS OF SELF-COMPASSION:", 'F2', 12)
comps = [
    ("1. Self-Kindness", "Treating yourself as you'd treat a good friend"),
    ("2. Common Humanity", "Remembering suffering is part of being human"),
    ("3. Mindfulness", "Acknowledging pain without over-identifying with it"),
]
y = 665
for title, desc in comps:
    pdf.add_text(60, y, title, 'F2', 11)
    pdf.add_text(60, y-16, desc, 'F1', 10)
    y -= 40
pdf.add_text(50, y, "SELF-COMPASSION BREAK (use in moments of shame):", 'F2', 11)
y -= 20
steps_sc = [
    "1. 'This is a moment of suffering.' (mindfulness)",
    "2. 'Suffering is part of life.' (common humanity)",
    "3. Place hand on heart. 'May I be kind to myself.' (self-kindness)",
]
for s in steps_sc:
    pdf.add_text(60, y, s, 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "PRACTICE: Write yourself a compassionate letter:", 'F2', 11)
y -= 35
for i in range(10):
    pdf.add_line(50, y, 540, y, 0.5, 0.7)
    y -= 18

# Page 14 - Vulnerability Practice
pdf.new_page()
pdf.add_centered_text(740, "VULNERABILITY PRACTICE", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Vulnerability is the antidote to shame. It requires courage.", 'F4', 11, 0.3)
pdf.add_text(50, 680, "Vulnerability is NOT oversharing. It IS showing up authentically.", 'F1', 11)
pdf.add_text(50, 650, "VULNERABILITY LADDER (start small, build up):", 'F2', 11)
ladder = [
    "Level 1: Share a preference or opinion",
    "Level 2: Ask for help with something small",
    "Level 3: Admit you don't know something",
    "Level 4: Share a feeling in the moment",
    "Level 5: Set a boundary",
    "Level 6: Share something you're struggling with",
    "Level 7: Apologize without excuses",
    "Level 8: Let someone see you imperfect",
]
y = 625
for l in ladder:
    pdf.add_text(60, y, l, 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "MY VULNERABILITY PRACTICE THIS WEEK:", 'F2', 11)
y -= 35
pdf.add_text(50, y, "What I'll do: _________________________________________", 'F1', 10)
y -= 22
pdf.add_text(50, y, "With whom: ____________________________________________", 'F1', 10)
y -= 22
pdf.add_text(50, y, "What I'm afraid will happen: ___________________________", 'F1', 10)
y -= 22
pdf.add_text(50, y, "What actually happened: ________________________________", 'F1', 10)
y -= 22
pdf.add_line(50, y, 540, y, 0.5, 0.7)


# Page 15 - Worthiness Affirmations
pdf.new_page()
pdf.add_centered_text(740, "WORTHINESS AFFIRMATIONS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Read these daily. Say them out loud. Write the ones that resonate:", 'F1', 11)
affirmations = [
    "I am worthy of love and belonging.",
    "I am enough, exactly as I am.",
    "My worth is not based on my productivity.",
    "I deserve to take up space.",
    "My past does not define my worthiness.",
    "I am allowed to make mistakes.",
    "I belong here.",
    "I am worthy of connection.",
    "My imperfections make me human, not broken.",
    "I choose to believe I am enough today.",
]
y = 680
for a in affirmations:
    pdf.add_text(80, y, a, 'F4', 12)
    y -= 30
pdf.add_text(50, y-10, "My personal worthiness statement:", 'F2', 11)
y -= 30
for i in range(4):
    pdf.add_line(50, y, 540, y, 0.5, 0.7)
    y -= 20

# Page 16 - Shame in Relationships
pdf.new_page()
pdf.add_centered_text(740, "SHAME IN RELATIONSHIPS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Shame shows up in how we connect (or disconnect) with others.", 'F1', 11)
pdf.add_text(50, 680, "SHAME-DRIVEN RELATIONSHIP PATTERNS:", 'F2', 11)
patterns = [
    ("People-pleasing:", "Abandoning yourself to be accepted"),
    ("Perfectionism:", "Never letting others see the real you"),
    ("Withdrawal:", "Pulling away before others can reject you"),
    ("Aggression:", "Pushing others away before they get too close"),
    ("Over-giving:", "Earning your right to exist through service"),
]
y = 658
for name, desc in patterns:
    pdf.add_text(60, y, name, 'F2', 10)
    pdf.add_text(180, y, desc, 'F1', 10)
    y -= 20
pdf.add_text(50, y-10, "My pattern: _______________________________________________", 'F1', 10)
y -= 30
pdf.add_text(50, y, "How shame shows up in my closest relationship:", 'F1', 10)
y -= 18
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 18
pdf.add_text(50, y-5, "What I really need from others:", 'F1', 10)
y -= 22
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 18

# Page 17 - Body Shame Healing
pdf.new_page()
pdf.add_centered_text(740, "BODY SHAME HEALING", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Body shame is one of the most common and devastating forms of shame.", 'F1', 11)
pdf.add_text(50, 680, "Messages I received about my body growing up:", 'F2', 11)
y = 660
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "What I want to tell my body now:", 'F2', 11)
y -= 20
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "Things my body does for me (gratitude):", 'F2', 11)
y -= 20
for i in range(5):
    pdf.add_text(60, y, f"{i+1}.", 'F1', 10)
    pdf.add_line(75, y-2, 540, y-2, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y-5, "My body neutrality/appreciation statement:", 'F2', 10)
y -= 22
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 18

# Pages 18-22 - Weekly Shame Awareness Log (5 pages)
for week in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(740, f"SHAME AWARENESS LOG - WEEK {week}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    y = 710
    for day in days:
        pdf.add_text(50, y, day, 'F2', 9)
        pdf.add_text(80, y, "Trigger:______________", 'F1', 8)
        pdf.add_text(210, y, "Intensity:__/10", 'F1', 8)
        pdf.add_text(300, y, "Response:________________", 'F1', 8)
        pdf.add_text(470, y, "Spoke it? Y/N", 'F1', 8)
        pdf.add_line(50, y-10, 562, y-10, 0.3, 0.8)
        y -= 30
    pdf.add_text(50, y-5, "Pattern I notice: _________________________________________", 'F1', 10)
    pdf.add_text(50, y-25, "Self-compassion practice: __________________________________", 'F1', 10)
    pdf.add_text(50, y-45, "Connection I made: _________________________________________", 'F1', 10)

# Pages 23-30 remaining content
titles_remain = ["MY SHAME RESILIENCE TOOLKIT", "I AM ENOUGH DECLARATION",
                 "FORGIVENESS PRACTICE", "BOUNDARIES & SHAME",
                 "CELEBRATING MY IMPERFECT SELF", "MY WHOLEHEARTED LIVING GOALS",
                 "LETTER OF RELEASE", "MOVING FORWARD"]
for pg, t in enumerate(titles_remain):
    pdf.new_page()
    pdf.add_centered_text(740, t, 'F2', 16)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 1:  # I AM ENOUGH
        pdf.add_centered_text(500, "I AM ENOUGH.", 'F2', 24)
        pdf.add_centered_text(450, "Not when I achieve more.", 'F4', 13, 0.3)
        pdf.add_centered_text(425, "Not when I lose weight.", 'F4', 13, 0.3)
        pdf.add_centered_text(400, "Not when I earn more.", 'F4', 13, 0.3)
        pdf.add_centered_text(375, "Not when I'm perfect.", 'F4', 13, 0.3)
        pdf.add_centered_text(340, "Right now. As I am.", 'F2', 14, 0.3)
        pdf.add_centered_text(300, "I AM ENOUGH.", 'F2', 18)
    else:
        y = 700
        for i in range(26):
            pdf.add_line(50, y, 562, y, 0.5, 0.7)
            y -= 24

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book181_Shame_Resilience_Workbook.pdf')
print("Book181_Shame_Resilience_Workbook.pdf created successfully!")
