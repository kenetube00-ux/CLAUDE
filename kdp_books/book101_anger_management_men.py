from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "ANGER MANAGEMENT WORKBOOK FOR MEN"
subtitle = "Take Control Before It Controls You"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(500, title, 'F2', 16)
pdf.add_centered_text(470, subtitle, 'F4', 13)
pdf.add_centered_text(350, "A Practical Guide to Understanding,", 'F4', 11)
pdf.add_centered_text(335, "Managing, and Overcoming Anger", 'F4', 11)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, title, 'F2', 11)
pdf.add_centered_text(460, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(440, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(400, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: What is Anger
pdf.new_page()
pdf.add_centered_text(610, "WHAT IS ANGER?", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
lines = [
    "Anger is a natural human emotion that signals something feels wrong.",
    "It becomes a problem when it is too intense, too frequent, or leads",
    "to harmful actions. Anger is not just 'losing your temper' - it is a",
    "complex emotional response involving thoughts, physical sensations,",
    "and behaviors.",
    "",
    "PRIMARY vs SECONDARY EMOTION:",
    "Anger often masks deeper feelings like hurt, fear, or shame.",
    "Learning to identify what is underneath your anger is the first step.",
    "",
    "THE COST OF UNMANAGED ANGER:",
    "- Damaged relationships with partner, children, friends",
    "- Health problems: high blood pressure, heart disease, headaches",
    "- Career consequences: lost jobs, missed promotions",
    "- Legal issues: assault charges, restraining orders",
    "- Emotional toll: guilt, shame, isolation",
    "",
    "THE GOOD NEWS:",
    "Anger CAN be managed. This workbook will teach you practical tools",
    "to understand your triggers, interrupt the anger cycle, and respond",
    "rather than react. Change is possible at any age."
]
for line in lines:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16


# Page 4: Triggers Worksheet
pdf.new_page()
pdf.add_centered_text(610, "MY ANGER TRIGGERS WORKSHEET", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
triggers_text = [
    "Instructions: Identify your personal anger triggers. Be specific.",
    "Rate each trigger 1-10 for intensity. Understanding your triggers",
    "is essential for developing an early warning system.",
    "",
    "COMMON TRIGGER CATEGORIES:"
]
for line in triggers_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15
categories = ["Disrespect / Being dismissed", "Feeling controlled or powerless",
    "Injustice or unfairness", "Criticism or blame", "Unmet expectations",
    "Feeling overwhelmed or stressed", "Physical discomfort (tired, hungry, pain)",
    "Memories of past trauma"]
for i, cat in enumerate(categories):
    pdf.add_text(60, y, f"{i+1}. {cat}", 'F1', 10)
    y -= 14
y -= 10
pdf.add_text(50, y, "MY PERSONAL TRIGGERS (list at least 5):", 'F2', 10)
y -= 20
for i in range(8):
    pdf.add_text(50, y, f"Trigger {i+1}: ", 'F1', 9)
    pdf.add_line(130, y-2, 380, y-2, 0.5, 0.5)
    y -= 14
    pdf.add_text(50, y, "Intensity (1-10): ___  Frequency: Daily / Weekly / Monthly", 'F1', 9)
    y -= 20

# Page 5: Physical Warning Signs
pdf.new_page()
pdf.add_centered_text(610, "PHYSICAL WARNING SIGNS CHECKLIST", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
pdf.add_text(50, y, "Your body sends signals BEFORE anger takes over. Check all that apply:", 'F4', 10)
y -= 25
signs = ["Jaw clenching or teeth grinding", "Fists tightening", "Heart racing or pounding",
    "Face feeling hot or flushed", "Chest tightness", "Shallow rapid breathing",
    "Stomach churning or nausea", "Muscle tension in shoulders/neck", "Sweating",
    "Voice getting louder", "Pacing or restlessness", "Tunnel vision",
    "Feeling shaky or trembling", "Headache developing", "Feeling 'hot all over'"]
for sign in signs:
    pdf.add_rect(55, y-2, 10, 10, 0.5)
    pdf.add_text(72, y, sign, 'F4', 10)
    y -= 20
y -= 10
pdf.add_text(50, y, "MY TOP 3 EARLY WARNING SIGNS:", 'F2', 10)
y -= 18
for i in range(3):
    pdf.add_text(50, y, f"{i+1}.", 'F1', 10)
    pdf.add_line(65, y-2, 380, y-2, 0.5, 0.5)
    y -= 22


# Page 6: The Anger Cycle
pdf.new_page()
pdf.add_centered_text(610, "THE ANGER CYCLE EXPLAINED", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
cycle_text = [
    "Anger follows a predictable cycle. Understanding this cycle gives",
    "you power to interrupt it at multiple points.",
    "",
    "PHASE 1: TRIGGER (The Spark)",
    "Something happens externally or internally that starts the process.",
    "This can be an event, memory, thought, or physical sensation.",
    "",
    "PHASE 2: ESCALATION (The Build-Up)",
    "Physical arousal increases. Thoughts become more negative and rigid.",
    "This is where early warning signs appear. You still have choices here.",
    "",
    "PHASE 3: CRISIS (The Explosion)",
    "Anger reaches peak intensity. Rational thinking shuts down.",
    "Fight-or-flight takes over. Harmful actions are most likely here.",
    "",
    "PHASE 4: RECOVERY (The Cool-Down)",
    "Physiological arousal gradually decreases. This takes 20-60 minutes.",
    "Do NOT try to resolve issues during this phase.",
    "",
    "PHASE 5: AFTERMATH (The Consequences)",
    "Guilt, shame, damage assessment. Opportunity for repair and learning.",
    "",
    "KEY INSIGHT: The best intervention point is Phase 2 (Escalation).",
    "Once you hit Phase 3, your rational brain is offline.",
    "Learn to recognize Phase 2 and use your Time-Out technique."
]
for line in cycle_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 7: Time-Out Technique
pdf.new_page()
pdf.add_centered_text(610, "THE TIME-OUT TECHNIQUE", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
timeout_text = [
    "The Time-Out is your EMERGENCY BRAKE. Use it when you feel yourself",
    "entering Phase 2 of the anger cycle.",
    "",
    "STEP 1: RECOGNIZE",
    "Notice your early warning signs (refer to your checklist on page 3).",
    "Say to yourself: 'I am getting angry. I need a time-out.'",
    "",
    "STEP 2: ANNOUNCE",
    "Tell the other person calmly: 'I need to take a break. I will be",
    "back in [specific time].' Do NOT just storm out.",
    "",
    "STEP 3: LEAVE",
    "Go to a pre-planned location. Do NOT drive. Do NOT drink alcohol.",
    "Go for a walk, sit in another room, or step outside.",
    "",
    "STEP 4: COOL DOWN (minimum 20 minutes)",
    "Use deep breathing: inhale 4 counts, hold 4, exhale 6.",
    "Do NOT rehearse the argument in your head.",
    "Use physical activity: push-ups, walk, squeeze stress ball.",
    "",
    "STEP 5: RETURN",
    "Come back at the time you said. If still escalated, ask for more",
    "time. Address the issue when BOTH people are calm.",
    "",
    "MY TIME-OUT PLAN:",
    "I will go to: _________________________________",
    "I will do: ___________________________________",
    "My cool-down time: ___________ minutes"
]
for line in timeout_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Pages 8-9: Cognitive Restructuring Exercises (10 exercises over 2 pages)
pdf.new_page()
pdf.add_centered_text(610, "COGNITIVE RESTRUCTURING EXERCISES", 'F2', 14)
pdf.add_centered_text(593, "Changing the Thoughts That Fuel Your Anger", 'F1', 10)
pdf.add_line(50, 585, 382, 585)
y = 565
exercises_p1 = [
    "Your thoughts CREATE your emotions. Angry thoughts = angry feelings.",
    "Challenge distorted thinking patterns with these exercises:",
    "",
    "EXERCISE 1: Identify the Hot Thought",
    "Situation: ______________________________________",
    "Hot thought (what I told myself): ________________",
    "Emotion & intensity (1-10): _____________________",
    "",
    "EXERCISE 2: Evidence For and Against",
    "Hot thought: ___________________________________",
    "Evidence FOR this thought: ______________________",
    "Evidence AGAINST this thought: __________________",
    "Balanced thought: ______________________________",
    "",
    "EXERCISE 3: Decatastrophizing",
    "Worst case scenario: ____________________________",
    "Best case scenario: _____________________________",
    "Most LIKELY scenario: ___________________________",
    "",
    "EXERCISE 4: Perspective Shift",
    "What would I tell a friend in this situation?",
    "_______________________________________________",
    "",
    "EXERCISE 5: The 10-10-10 Rule",
    "Will this matter in 10 minutes? 10 months? 10 years?",
    "_______________________________________________"
]
for line in exercises_p1:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

pdf.new_page()
pdf.add_centered_text(610, "COGNITIVE RESTRUCTURING (continued)", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
exercises_p2 = [
    "EXERCISE 6: Should vs Preference",
    "Change 'He SHOULD respect me' to 'I PREFER to be respected.'",
    "My 'should' statement: __________________________",
    "Rewritten as preference: ________________________",
    "",
    "EXERCISE 7: Mind-Reading Check",
    "What I assume they meant: ______________________",
    "What they MIGHT have meant: ____________________",
    "How can I find out for sure? ____________________",
    "",
    "EXERCISE 8: Responsibility Pie",
    "Situation: _____________________________________",
    "My contribution ___% Their contribution ___% Circumstances ___%",
    "",
    "EXERCISE 9: Cost-Benefit Analysis",
    "If I act on my anger, what do I GAIN? ___________",
    "If I act on my anger, what do I LOSE? ___________",
    "Is it worth it? YES / NO",
    "",
    "EXERCISE 10: Compassion Challenge",
    "What pain might the other person be carrying?",
    "_______________________________________________",
    "Does understanding their pain change my response?",
    "_______________________________________________"
]
for line in exercises_p2:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Pages 10-11: Assertive Communication Scripts
pdf.new_page()
pdf.add_centered_text(610, "ASSERTIVE COMMUNICATION SCRIPTS", 'F2', 14)
pdf.add_centered_text(593, "5 Common Scenarios with Scripts", 'F1', 10)
pdf.add_line(50, 585, 382, 585)
y = 565
scripts1 = [
    "SCENARIO 1: Someone disrespects you at work",
    "AGGRESSIVE: 'Who do you think you are talking to me like that?!'",
    "PASSIVE: (Say nothing, seethe internally)",
    "ASSERTIVE: 'When you speak to me that way, I feel disrespected.",
    "  I need you to communicate with me professionally.'",
    "",
    "SCENARIO 2: Partner criticizes you",
    "AGGRESSIVE: 'You never appreciate anything I do!'",
    "PASSIVE: (Shut down, withdraw)",
    "ASSERTIVE: 'I feel hurt when my efforts are criticized. Can we",
    "  talk about what you need without blaming?'",
    "",
    "SCENARIO 3: Someone cuts you off in traffic",
    "AGGRESSIVE: Tailgate, honk, road rage",
    "PASSIVE: Panic, anxiety spiral",
    "ASSERTIVE: (Self-talk) 'That was dangerous but I am safe. Their",
    "  driving is not about me. Let it go.'",
]
for line in scripts1:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

pdf.new_page()
pdf.add_centered_text(610, "ASSERTIVE COMMUNICATION (continued)", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
scripts2 = [
    "SCENARIO 4: Child won't listen",
    "AGGRESSIVE: Yelling, threatening, intimidating",
    "PASSIVE: Give up, let child do whatever",
    "ASSERTIVE: 'I need you to [specific behavior] by [specific time].",
    "  If you choose not to, the consequence will be [specific].'",
    "",
    "SCENARIO 5: Friend borrows money and doesn't pay back",
    "AGGRESSIVE: 'You're a deadbeat! Pay me back NOW!'",
    "PASSIVE: Never mention it, resent them forever",
    "ASSERTIVE: 'I lent you $X on [date]. I need that back by [date].",
    "  Can we agree on a plan?'",
    "",
    "THE ASSERTIVE FORMULA:",
    "1. When you [specific behavior]...",
    "2. I feel [emotion]...",
    "3. Because [impact on me]...",
    "4. I need [specific request]...",
    "",
    "PRACTICE: Write your own assertive script for a current situation:",
    "When you: ______________________________________",
    "I feel: ________________________________________",
    "Because: _______________________________________",
    "I need: ________________________________________"
]
for line in scripts2:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 12: Conflict Resolution Steps
pdf.new_page()
pdf.add_centered_text(610, "CONFLICT RESOLUTION STEPS", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
conflict_text = [
    "Follow these steps AFTER both parties are calm (not during anger):",
    "",
    "STEP 1: Choose the right time and place",
    "  - Both people must be calm (at least 20 min after conflict)",
    "  - Private location, no audience, no distractions",
    "  - Ask: 'Is now a good time to talk about what happened?'",
    "",
    "STEP 2: Define the problem WITHOUT blame",
    "  - Use I-statements, not You-statements",
    "  - Stick to ONE issue at a time (no 'kitchen sinking')",
    "  - State facts, not interpretations",
    "",
    "STEP 3: Listen actively",
    "  - Let them finish without interrupting",
    "  - Reflect back what you heard: 'So you felt...'",
    "  - Ask: 'Did I understand you correctly?'",
    "",
    "STEP 4: Acknowledge their perspective",
    "  - Validation is NOT agreement. Say: 'I can see why you felt...'",
    "  - Find the grain of truth in their complaint",
    "",
    "STEP 5: Brainstorm solutions together",
    "  - What would work for BOTH of us?",
    "  - Be willing to compromise (not capitulate)",
    "  - Agree on specific actions going forward",
    "",
    "STEP 6: Follow through and check back",
    "  - Do what you agreed to do",
    "  - Check in: 'How is this working for you?'"
]
for line in conflict_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14

# Page 13: Stress Management Plan
pdf.new_page()
pdf.add_centered_text(610, "MY STRESS MANAGEMENT PLAN", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
stress_text = [
    "Chronic stress is the fuel that makes anger fires burn hotter.",
    "Build a daily stress management routine:",
    "",
    "PHYSICAL: (Choose at least 2)",
]
for line in stress_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15
physical = ["Exercise 30+ minutes daily", "Progressive muscle relaxation", "Deep breathing 3x daily",
    "Adequate sleep (7-9 hours)", "Reduce caffeine/sugar"]
for p in physical:
    pdf.add_rect(55, y-2, 10, 10, 0.5)
    pdf.add_text(72, y, p, 'F4', 10)
    y -= 17
y -= 8
pdf.add_text(50, y, "MENTAL: (Choose at least 2)", 'F2', 10)
y -= 17
mental = ["Mindfulness meditation", "Journaling", "Cognitive restructuring practice",
    "Gratitude practice", "Limit news/social media"]
for m in mental:
    pdf.add_rect(55, y-2, 10, 10, 0.5)
    pdf.add_text(72, y, m, 'F4', 10)
    y -= 17
y -= 8
pdf.add_text(50, y, "SOCIAL: (Choose at least 1)", 'F2', 10)
y -= 17
social = ["Talk to a trusted friend weekly", "Attend a support group",
    "Spend quality time with family", "Volunteer/help others"]
for s in social:
    pdf.add_rect(55, y-2, 10, 10, 0.5)
    pdf.add_text(72, y, s, 'F4', 10)
    y -= 17


# Page 14: Forgiveness Exercises
pdf.new_page()
pdf.add_centered_text(610, "FORGIVENESS EXERCISES", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
forgive_text = [
    "Forgiveness is NOT condoning, excusing, or forgetting.",
    "Forgiveness is RELEASING the hold resentment has on YOU.",
    "",
    "EXERCISE 1: The Resentment Inventory",
    "Person I resent: _______________________________",
    "What they did: _________________________________",
    "How it affected me: ____________________________",
    "My part (if any): ______________________________",
    "What holding this costs me: ____________________",
    "",
    "EXERCISE 2: Empathy Building",
    "What might have been happening in their life?",
    "_______________________________________________",
    "Were they doing the best they could at the time?",
    "_______________________________________________",
    "",
    "EXERCISE 3: Letting Go Letter (do not send)",
    "Write a letter expressing everything you feel. Then choose to",
    "release it. You can destroy the letter as a symbolic act.",
    "",
    "EXERCISE 4: Self-Forgiveness",
    "What I did that I regret: ______________________",
    "What I have learned: ___________________________",
    "How I will do differently: _____________________",
    "I choose to forgive myself because: _____________",
    "",
    "Remember: Forgiveness is a PROCESS, not an event.",
    "You may need to choose forgiveness daily for a while."
]
for line in forgive_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Pages 15-18: Weekly Anger Log (4 pages)
for week in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(610, f"WEEKLY ANGER LOG - WEEK {week}", 'F2', 14)
    pdf.add_line(50, 600, 382, 600)
    y = 580
    for day in range(7):
        pdf.add_text(50, y, f"Day {day+1}  Date: ___/___/___", 'F2', 9)
        y -= 13
        pdf.add_text(50, y, "Trigger: _________________ Intensity (1-10): ___", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Thought: _________________ Strategy used: _______", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Outcome: _________________ What I learned: ______", 'F3', 8)
        y -= 16
        pdf.add_line(50, y+4, 382, y+4, 0.3, 0.7)
        y -= 8


# Page 19: Relapse Prevention
pdf.new_page()
pdf.add_centered_text(610, "RELAPSE PREVENTION PLAN", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
relapse_text = [
    "Setbacks are NORMAL. They do not erase your progress.",
    "Plan ahead for high-risk situations:",
    "",
    "MY HIGH-RISK SITUATIONS:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "",
    "MY WARNING SIGNS THAT I'M SLIPPING:",
    "- Skipping my stress management routine",
    "- Isolating from supportive people",
    "- Increased irritability over small things",
    "- Returning to aggressive language",
    "- Stopping journaling or self-reflection",
    "",
    "MY EMERGENCY PLAN:",
    "If I lose my temper, I will:",
    "1. Remove myself immediately (time-out)",
    "2. Call: _________________ (my support person)",
    "3. Use grounding: 5 things I can see, 4 I can hear...",
    "4. Review this workbook - especially pages 4-7",
    "5. Be compassionate with myself - one slip is not failure",
    "",
    "IF I NEED PROFESSIONAL HELP:",
    "Therapist/Counselor: ___________________________",
    "Crisis line: 988 Suicide & Crisis Lifeline",
    "Domestic violence hotline: 1-800-799-7233"
]
for line in relapse_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 20: My Commitment Contract
pdf.new_page()
pdf.add_centered_text(610, "MY COMMITMENT CONTRACT", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 565
pdf.add_text(50, y, "I, __________________________________, commit to the following:", 'F4', 11)
y -= 30
commitments = [
    "1. I will recognize that I am responsible for my own anger.",
    "2. I will use the time-out technique when I feel escalating.",
    "3. I will practice my stress management plan daily.",
    "4. I will communicate assertively, not aggressively.",
    "5. I will be patient with myself during this process.",
    "6. I will ask for help when I need it.",
    "7. I will not use anger to control or intimidate others.",
    "8. I will track my progress honestly in this workbook.",
    "9. I will make amends when I fall short.",
    "10. I choose to be the man my family deserves."
]
for c in commitments:
    pdf.add_text(50, y, c, 'F4', 10)
    y -= 22
y -= 20
pdf.add_text(50, y, "Signed: ______________________________", 'F4', 11)
y -= 25
pdf.add_text(50, y, "Date: ________________________________", 'F4', 11)
y -= 25
pdf.add_text(50, y, "Witness (optional): ___________________", 'F4', 11)
y -= 40
pdf.add_centered_text(y, "You are not your anger. You are the man choosing to change.", 'F5', 11)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book101_Anger_Management_Men.pdf')
print("Book101_Anger_Management_Men.pdf created successfully!")
