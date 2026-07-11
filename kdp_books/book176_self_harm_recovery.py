#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "CHOOSING LIFE"
subtitle = "A Self-Harm Recovery Workbook for Teens & Young Adults"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, title, 'F2', 28)
pdf.add_centered_text(470, subtitle, 'F4', 14)
pdf.add_centered_text(420, f"By {author}", 'F4', 12)
pdf.add_line(150, 400, 462, 400, 2)
pdf.add_centered_text(360, "You matter. Your pain is real.", 'F4', 13, 0.3)
pdf.add_centered_text(340, "And you deserve to find another way.", 'F4', 13, 0.3)

# Page 2 - Copyright
pdf.new_page()
pdf.add_centered_text(500, f"Copyright - {author}", 'F1', 10)
pdf.add_centered_text(480, "All rights reserved.", 'F1', 10)
pdf.add_centered_text(440, "CRISIS RESOURCES:", 'F2', 12)
pdf.add_centered_text(420, "988 Suicide & Crisis Lifeline: Call or text 988", 'F1', 11)
pdf.add_centered_text(400, "Crisis Text Line: Text HOME to 741741", 'F1', 11)
pdf.add_centered_text(380, "This workbook is not a substitute for professional help.", 'F1', 10)

# Page 3 - Understanding Self-Harm
pdf.new_page()
pdf.add_centered_text(740, "UNDERSTANDING SELF-HARM", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 700, "Self-harm is NOT:", 'F2', 12)
pdf.add_text(70, 680, "- Attention-seeking", 'F1', 11)
pdf.add_text(70, 665, "- A failed suicide attempt (though risk increases)", 'F1', 11)
pdf.add_text(70, 650, "- Something to be ashamed of", 'F1', 11)
pdf.add_text(50, 620, "Self-harm IS:", 'F2', 12)
pdf.add_text(70, 600, "- A coping mechanism for overwhelming emotions", 'F1', 11)
pdf.add_text(70, 585, "- A way to feel something when feeling numb", 'F1', 11)
pdf.add_text(70, 570, "- A signal that you need and deserve support", 'F1', 11)
pdf.add_text(50, 530, "Common reasons people self-harm:", 'F2', 12)
items = ["To manage intense emotions", "To feel in control",
         "To express pain they can't put into words",
         "To punish themselves", "To feel something when numb"]
y = 510
for item in items:
    pdf.add_text(70, y, f"- {item}", 'F1', 11)
    y -= 18
pdf.add_text(50, y-20, "Recovery IS possible. Many people find healthier ways to cope.", 'F2', 11, 0.3)


# Page 4 - Triggers Identification
pdf.new_page()
pdf.add_centered_text(740, "MY TRIGGERS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 700, "Triggers are situations, feelings, or thoughts that make you want to self-harm.", 'F1', 11)
pdf.add_text(50, 680, "Identifying them is the first step to managing them.", 'F1', 11)
pdf.add_text(50, 650, "EMOTIONAL TRIGGERS (feelings that come before the urge):", 'F2', 11)
y = 630
for i in range(5):
    pdf.add_line(70, y, 540, y, 0.5, 0.7)
    y -= 25
pdf.add_text(50, y-10, "SITUATIONAL TRIGGERS (events, places, people):", 'F2', 11)
y -= 30
for i in range(5):
    pdf.add_line(70, y, 540, y, 0.5, 0.7)
    y -= 25
pdf.add_text(50, y-10, "THOUGHT TRIGGERS (what I tell myself before an urge):", 'F2', 11)
y -= 30
for i in range(5):
    pdf.add_line(70, y, 540, y, 0.5, 0.7)
    y -= 25
pdf.add_text(50, y-20, "BODY SIGNALS (physical signs an urge is building):", 'F2', 11)
y -= 40
for i in range(3):
    pdf.add_line(70, y, 540, y, 0.5, 0.7)
    y -= 25

# Page 5 - Urge Surfing
pdf.new_page()
pdf.add_centered_text(740, "URGE SURFING TECHNIQUE", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 700, "Urges are like waves - they rise, peak, and pass.", 'F2', 11)
pdf.add_text(50, 675, "The average urge lasts 15-30 minutes if you don't act on it.", 'F1', 11)
pdf.add_text(50, 645, "STEPS TO SURF AN URGE:", 'F2', 12)
steps = [
    "1. NOTICE: 'I'm having an urge right now.' Name it without judgment.",
    "2. BREATHE: Take 5 slow breaths. In for 4, hold for 4, out for 6.",
    "3. OBSERVE: Where do you feel the urge in your body? Rate it 1-10.",
    "4. DESCRIBE: What triggered this? What emotion is underneath?",
    "5. RIDE: The urge WILL pass. Set a timer for 15 minutes.",
    "6. DISTRACT: Use a coping skill (next page) until the wave passes.",
    "7. CELEBRATE: You surfed the urge! Record your success."
]
y = 615
for step in steps:
    pdf.add_text(60, y, step, 'F1', 10)
    y -= 22
pdf.add_text(50, y-20, "My urge rating right now (1-10): ______", 'F1', 11)
pdf.add_text(50, y-40, "Timer set for: ______ minutes", 'F1', 11)
pdf.add_text(50, y-60, "What I notice about the urge after waiting:", 'F1', 11)
pdf.add_line(50, y-80, 540, y-80, 0.5, 0.7)
pdf.add_line(50, y-105, 540, y-105, 0.5, 0.7)
pdf.add_line(50, y-130, 540, y-130, 0.5, 0.7)


# Page 6 - Alternative Coping Strategies
pdf.new_page()
pdf.add_centered_text(740, "ALTERNATIVE COPING STRATEGIES", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Instead of harming, try these alternatives that address the SAME need:", 'F1', 11)
pdf.add_text(50, 680, "FOR INTENSE EMOTIONS (need to feel something physical):", 'F2', 10)
alts1 = ["Hold ice cubes tightly", "Snap a rubber band on wrist", "Take a very cold shower",
         "Bite into a lemon or hot pepper", "Squeeze a stress ball as hard as possible"]
y = 665
for a in alts1:
    pdf.add_text(70, y, f"- {a}", 'F1', 10)
    y -= 15
pdf.add_text(50, y-10, "FOR ANGER/FRUSTRATION:", 'F2', 10)
y -= 25
alts2 = ["Rip up paper or an old phone book", "Scream into a pillow",
         "Punch a punching bag or pillow", "Run or do intense exercise",
         "Write angry words and burn the paper safely"]
for a in alts2:
    pdf.add_text(70, y, f"- {a}", 'F1', 10)
    y -= 15
pdf.add_text(50, y-10, "FOR SADNESS/NUMBNESS (need to feel):", 'F2', 10)
y -= 25
alts3 = ["Draw on skin with RED marker where you would harm", "Hold ice on your skin",
         "Take a cold shower", "Eat something with intense flavor",
         "Listen to loud emotional music"]
for a in alts3:
    pdf.add_text(70, y, f"- {a}", 'F1', 10)
    y -= 15
pdf.add_text(50, y-10, "FOR SELF-PUNISHMENT:", 'F2', 10)
y -= 25
alts4 = ["Write a letter of self-compassion", "Do something kind for someone else",
         "Challenge the thought: 'What would I say to a friend?'",
         "List 3 things you did well today"]
for a in alts4:
    pdf.add_text(70, y, f"- {a}", 'F1', 10)
    y -= 15
pdf.add_text(50, y-20, "MY TOP 3 GO-TO ALTERNATIVES:", 'F2', 11)
y -= 40
for i in range(3):
    pdf.add_text(50, y, f"{i+1}. ", 'F1', 11)
    pdf.add_line(70, y-2, 540, y-2, 0.5, 0.7)
    y -= 25

# Page 7 - Distress Tolerance Skills
pdf.new_page()
pdf.add_centered_text(740, "DISTRESS TOLERANCE SKILLS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "The TIPP Skills (change your body chemistry fast):", 'F2', 12)
tips = [
    ("T - Temperature:", "Dunk face in cold water or hold ice to face for 30 sec"),
    ("I - Intense Exercise:", "Sprint, jump, do burpees for 5-10 minutes"),
    ("P - Paced Breathing:", "Breathe out longer than in (4 in, 7 out)"),
    ("P - Paired Muscle Relaxation:", "Tense each muscle group, then release")
]
y = 680
for label, desc in tips:
    pdf.add_text(60, y, label, 'F2', 11)
    pdf.add_text(200, y, desc, 'F1', 10)
    y -= 22
pdf.add_text(50, y-15, "The ACCEPTS Skills (distraction when emotions are HIGH):", 'F2', 12)
y -= 40
accepts = [
    ("A - Activities:", "Do something that requires focus"),
    ("C - Contributing:", "Help someone else, volunteer, do a kind act"),
    ("C - Comparisons:", "Compare to a time you coped well"),
    ("E - Emotions:", "Watch a funny video, listen to upbeat music"),
    ("P - Pushing Away:", "Mentally put the problem on a shelf for now"),
    ("T - Thoughts:", "Count backwards from 100 by 7s"),
    ("S - Sensations:", "Hold ice, smell strong scent, taste something sour")
]
for label, desc in accepts:
    pdf.add_text(60, y, label, 'F2', 10)
    pdf.add_text(200, y, desc, 'F1', 10)
    y -= 20
pdf.add_text(50, y-20, "Which TIPP skill works best for me? ___________________________", 'F1', 11)
pdf.add_text(50, y-40, "Which ACCEPTS skill works best for me? ___________________________", 'F1', 11)


# Page 8 - Emotion Regulation
pdf.new_page()
pdf.add_centered_text(740, "EMOTION REGULATION BASICS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Self-harm often happens when emotions feel unmanageable.", 'F1', 11)
pdf.add_text(50, 685, "These skills help you manage emotions BEFORE they reach crisis level.", 'F1', 11)
pdf.add_text(50, 655, "THE EMOTION WAVE:", 'F2', 12)
pdf.add_text(50, 635, "Trigger -> Thought -> Emotion -> Urge -> Action", 'F3', 10)
pdf.add_text(50, 615, "You can interrupt at ANY point in this chain!", 'F2', 10, 0.3)
pdf.add_text(50, 585, "NAME IT TO TAME IT:", 'F2', 12)
pdf.add_text(50, 565, "Right now I feel: _______________________", 'F1', 11)
pdf.add_text(50, 545, "On a scale of 1-10, the intensity is: ______", 'F1', 11)
pdf.add_text(50, 525, "This emotion is telling me: _______________________", 'F1', 11)
pdf.add_text(50, 495, "OPPOSITE ACTION:", 'F2', 12)
pdf.add_text(50, 475, "When the emotion is NOT justified or when acting on it would be harmful:", 'F1', 10)
opp = [("Sadness urge: withdraw", "Opposite: reach out to someone, get active"),
       ("Anger urge: attack", "Opposite: gently avoid, do something kind"),
       ("Fear urge: avoid", "Opposite: approach what you fear (safely)"),
       ("Shame urge: hide", "Opposite: tell someone, show yourself")]
y = 450
for urge, opp_act in opp:
    pdf.add_text(60, y, urge, 'F1', 10)
    pdf.add_text(300, y, opp_act, 'F2', 10)
    y -= 20
pdf.add_text(50, y-20, "My emotion that most often leads to self-harm: ___________________", 'F1', 11)
pdf.add_text(50, y-40, "My opposite action plan: ___________________________________", 'F1', 11)
pdf.add_line(50, y-62, 540, y-62, 0.5, 0.7)

# Page 9 - Safety Plan
pdf.new_page()
pdf.add_centered_text(740, "MY SAFETY PLAN", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_filled_rect(45, 60, 525, 670, 0.95)
pdf.add_text(50, 710, "Step 1: Warning signs that a crisis may be building:", 'F2', 11)
y = 690
for i in range(3):
    pdf.add_line(70, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y-5, "Step 2: Internal coping strategies (things I can do alone):", 'F2', 11)
y -= 25
for i in range(3):
    pdf.add_line(70, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y-5, "Step 3: People who can distract me:", 'F2', 11)
y -= 25
for i in range(3):
    pdf.add_text(70, y, "Name: _________________ Phone: _________________", 'F1', 10)
    y -= 20
pdf.add_text(50, y-5, "Step 4: People I can ask for help:", 'F2', 11)
y -= 25
for i in range(3):
    pdf.add_text(70, y, "Name: _________________ Phone: _________________", 'F1', 10)
    y -= 20
pdf.add_text(50, y-5, "Step 5: Professionals/agencies I can contact:", 'F2', 11)
y -= 25
pdf.add_text(70, y, "Therapist: _________________ Phone: _________________", 'F1', 10)
y -= 20
pdf.add_text(70, y, "988 Suicide & Crisis Lifeline (call or text 988)", 'F1', 10)
y -= 20
pdf.add_text(70, y, "Crisis Text Line: Text HOME to 741741", 'F1', 10)
y -= 20
pdf.add_text(70, y, "Emergency: 911", 'F1', 10)
y -= 30
pdf.add_text(50, y, "Step 6: Making my environment safe (removing means):", 'F2', 11)
y -= 20
for i in range(2):
    pdf.add_line(70, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "My one reason to stay safe today:", 'F2', 11)
y -= 20
pdf.add_line(70, y, 540, y, 0.5, 0.7)


# Page 10 - Wound Care Info
pdf.new_page()
pdf.add_centered_text(740, "WOUND CARE INFORMATION", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "If you have harmed, caring for wounds is an act of self-compassion.", 'F2', 11, 0.3)
pdf.add_text(50, 680, "BASIC FIRST AID:", 'F2', 12)
steps_wc = [
    "1. Wash hands before touching any wound",
    "2. Clean the wound gently with cool running water",
    "3. Apply gentle pressure with clean cloth if bleeding",
    "4. Apply antibiotic ointment if available",
    "5. Cover with a clean bandage",
    "6. Change bandage daily and watch for infection"
]
y = 660
for s in steps_wc:
    pdf.add_text(60, y, s, 'F1', 11)
    y -= 18
pdf.add_text(50, y-10, "SEEK MEDICAL HELP IF:", 'F2', 12)
y -= 30
seek = ["Bleeding won't stop after 10 minutes of pressure",
        "Wound is deep, wide, or won't close",
        "Signs of infection (redness spreading, warmth, pus, fever)",
        "You feel dizzy or faint", "You are in severe pain"]
for s in seek:
    pdf.add_text(70, y, f"- {s}", 'F1', 11)
    y -= 18
pdf.add_text(50, y-15, "Remember: Getting medical help is NOT shameful.", 'F2', 11, 0.3)
pdf.add_text(50, y-35, "You deserve care and healing.", 'F2', 11, 0.3)

# Page 11 - Trusted Adults
pdf.new_page()
pdf.add_centered_text(740, "MY TRUSTED ADULTS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Having at least ONE adult who knows what you're going through is critical.", 'F1', 11)
pdf.add_text(50, 685, "A trusted adult is someone who:", 'F1', 11)
traits = ["Listens without judgment", "Keeps appropriate confidences",
          "Doesn't minimize your pain", "Helps you get professional support",
          "Checks in on you without being controlling"]
y = 665
for t in traits:
    pdf.add_text(70, y, f"- {t}", 'F1', 10)
    y -= 15
pdf.add_text(50, y-15, "MY TRUSTED PEOPLE:", 'F2', 12)
y -= 40
for i in range(4):
    pdf.add_text(50, y, f"Person {i+1}: ___________________  Relationship: ___________________", 'F1', 11)
    pdf.add_text(50, y-18, "Phone/Contact: ___________________", 'F1', 11)
    pdf.add_text(50, y-36, "What I want them to know: ", 'F1', 11)
    pdf.add_line(50, y-56, 540, y-56, 0.5, 0.7)
    y -= 80


# Pages 12-19 - Weekly Urge Tracker (8 pages)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for week in range(1, 9):
    pdf.new_page()
    pdf.add_centered_text(740, f"WEEKLY URGE TRACKER - WEEK {week}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    y = 710
    for day in days:
        pdf.add_text(50, y, day, 'F2', 9)
        pdf.add_text(120, y, "Urge(1-10):___", 'F1', 8)
        pdf.add_text(210, y, "Trigger:______________", 'F1', 8)
        pdf.add_text(350, y, "Coped?:Y/N", 'F1', 8)
        pdf.add_text(430, y, "Skill used:____________", 'F1', 8)
        pdf.add_line(50, y-8, 562, y-8, 0.3, 0.8)
        y -= 28
    pdf.add_text(50, y-10, "Highest urge this week: ___ Lowest: ___ Average: ___", 'F1', 10)
    pdf.add_text(50, y-28, "Harm-free days this week: ___/7", 'F2', 10)
    pdf.add_text(50, y-48, "What helped most this week:", 'F1', 10)
    pdf.add_line(50, y-66, 540, y-66, 0.5, 0.7)
    pdf.add_text(50, y-86, "What I'm proud of:", 'F1', 10)
    pdf.add_line(50, y-104, 540, y-104, 0.5, 0.7)
    pdf.add_text(50, y-124, "Goal for next week:", 'F1', 10)
    pdf.add_line(50, y-142, 540, y-142, 0.5, 0.7)

# Page 20 - My Reasons to Stay Safe
pdf.new_page()
pdf.add_centered_text(740, "MY REASONS TO STAY SAFE", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "On hard days, come back to this page. These are YOUR reasons.", 'F2', 11, 0.3)
y = 675
for i in range(1, 16):
    pdf.add_text(50, y, f"{i}.", 'F2', 11)
    pdf.add_line(70, y-2, 540, y-2, 0.5, 0.7)
    y -= 35
pdf.add_text(50, y-10, "You are not your worst moment. You are capable of healing.", 'F4', 11, 0.3)

# Page 21 - Communication Scripts
pdf.new_page()
pdf.add_centered_text(740, "COMMUNICATION SCRIPTS", 'F2', 16)
pdf.add_centered_text(720, "How to Ask for Help", 'F4', 12, 0.3)
pdf.add_line(50, 710, 562, 710, 1)
scripts = [
    ("To a friend:", "\"I'm going through something hard. I don't need you to fix it,\nbut I need someone to know. Can I talk to you?\""),
    ("To a parent:", "\"I need to tell you something. Please listen before reacting.\nI've been hurting myself and I want to stop. I need help.\""),
    ("To a therapist:", "\"I've been self-harming. I want to learn better coping skills.\nI'm ready to work on this.\""),
    ("To a teacher:", "\"I'm struggling with something personal that's affecting me.\nI need to talk to the school counselor. Can you help me?\""),
    ("In crisis:", "\"I'm not safe right now. I need help immediately.\nPlease stay with me / Please call 988.\""),
]
y = 685
for label, script in scripts:
    pdf.add_text(50, y, label, 'F2', 11)
    y -= 18
    for line in script.split('\n'):
        pdf.add_text(70, y, line, 'F4', 10)
        y -= 15
    y -= 20
pdf.add_text(50, y, "My own words (what feels right for ME to say):", 'F2', 11)
y -= 20
for i in range(4):
    pdf.add_line(50, y, 540, y, 0.5, 0.7)
    y -= 22


# Page 22 - Professional Resources
pdf.new_page()
pdf.add_centered_text(740, "PROFESSIONAL RESOURCES", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "IMMEDIATE CRISIS:", 'F2', 12)
pdf.add_text(50, 685, "988 Suicide & Crisis Lifeline: Call or text 988 (24/7)", 'F1', 11)
pdf.add_text(50, 665, "Crisis Text Line: Text HOME to 741741 (24/7)", 'F1', 11)
pdf.add_text(50, 645, "Trevor Project (LGBTQ+): 1-866-488-7386", 'F1', 11)
pdf.add_text(50, 625, "Emergency Services: 911", 'F1', 11)
pdf.add_text(50, 595, "ONGOING SUPPORT:", 'F2', 12)
pdf.add_text(50, 575, "To Write Love on Her Arms: twloha.com", 'F1', 11)
pdf.add_text(50, 555, "Self-Injury Outreach & Support: sioutreach.org", 'F1', 11)
pdf.add_text(50, 535, "SAMHSA Helpline: 1-800-662-4357", 'F1', 11)
pdf.add_text(50, 505, "EVIDENCE-BASED TREATMENTS:", 'F2', 12)
pdf.add_text(50, 485, "- Dialectical Behavior Therapy (DBT)", 'F1', 11)
pdf.add_text(50, 465, "- Cognitive Behavioral Therapy (CBT)", 'F1', 11)
pdf.add_text(50, 445, "- Mentalization-Based Therapy (MBT)", 'F1', 11)
pdf.add_text(50, 415, "MY TREATMENT TEAM:", 'F2', 12)
pdf.add_text(50, 395, "Therapist: ___________________ Phone: _______________", 'F1', 11)
pdf.add_text(50, 375, "Doctor: ___________________ Phone: _______________", 'F1', 11)
pdf.add_text(50, 355, "School Counselor: ___________________ ", 'F1', 11)
pdf.add_text(50, 335, "Support Group: ___________________", 'F1', 11)

# Pages 23-30 remaining pages (Milestones, affirmations, etc)
for pg in range(8):
    pdf.new_page()
    if pg == 0:
        pdf.add_centered_text(740, "MILESTONES IN MY RECOVERY", 'F2', 16)
        pdf.add_line(50, 730, 562, 730, 1)
        milestones = ["1 day harm-free", "3 days harm-free", "1 week harm-free",
                      "2 weeks harm-free", "1 month harm-free", "3 months harm-free",
                      "6 months harm-free", "1 year harm-free"]
        y = 700
        for m in milestones:
            pdf.add_rect(50, y-12, 15, 15)
            pdf.add_text(75, y-10, m, 'F1', 12)
            pdf.add_text(280, y-10, "Date achieved: _______________", 'F1', 10)
            pdf.add_text(280, y-28, "How I celebrated: _______________", 'F1', 10)
            y -= 60
    elif pg == 1:
        pdf.add_centered_text(740, "DAILY AFFIRMATIONS FOR RECOVERY", 'F2', 16)
        pdf.add_line(50, 730, 562, 730, 1)
        affs = ["I deserve to be safe.", "My pain is valid and temporary.",
                "I am more than my scars.", "I am learning healthier ways to cope.",
                "I am worthy of love and support.", "One day at a time is enough.",
                "My feelings matter, even the hard ones.",
                "I choose compassion toward myself today.",
                "Recovery is not linear, and that's okay.",
                "I am brave for choosing healing."]
        y = 700
        for a in affs:
            pdf.add_text(80, y, a, 'F4', 13)
            y -= 40
    elif pg == 2:
        pdf.add_centered_text(740, "SELF-COMPASSION LETTER", 'F2', 16)
        pdf.add_line(50, 730, 562, 730, 1)
        pdf.add_text(50, 705, "Write a letter to yourself as if you were writing to a friend you love:", 'F1', 11)
        y = 680
        for i in range(24):
            pdf.add_line(50, y, 562, y, 0.5, 0.7)
            y -= 24
    elif pg == 3:
        pdf.add_centered_text(740, "WHAT I WANT MY FUTURE TO LOOK LIKE", 'F2', 16)
        pdf.add_line(50, 730, 562, 730, 1)
        pdf.add_text(50, 705, "In 1 year, I want:", 'F2', 11)
        y = 685
        for i in range(4):
            pdf.add_line(70, y, 540, y, 0.5, 0.7)
            y -= 22
        pdf.add_text(50, y, "In 5 years, I want:", 'F2', 11)
        y -= 20
        for i in range(4):
            pdf.add_line(70, y, 540, y, 0.5, 0.7)
            y -= 22
        pdf.add_text(50, y, "People I want in my life:", 'F2', 11)
        y -= 20
        for i in range(4):
            pdf.add_line(70, y, 540, y, 0.5, 0.7)
            y -= 22
        pdf.add_text(50, y, "Things I want to experience:", 'F2', 11)
        y -= 20
        for i in range(4):
            pdf.add_line(70, y, 540, y, 0.5, 0.7)
            y -= 22
    else:
        topics = ["GRATITUDE JOURNAL", "MY SUPPORT NETWORK MAP",
                  "PROGRESS REFLECTION", "MY COMMITMENT TO HEALING"]
        pdf.add_centered_text(740, topics[pg-4], 'F2', 16)
        pdf.add_line(50, 730, 562, 730, 1)
        y = 700
        for i in range(26):
            pdf.add_line(50, y, 562, y, 0.5, 0.7)
            y -= 24

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book176_Self_Harm_Recovery_Workbook.pdf')
print("Book176_Self_Harm_Recovery_Workbook.pdf created successfully!")
