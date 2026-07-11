#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "EXECUTIVE FUNCTION WORKBOOK"
subtitle = "For Adults with ADHD"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, title, 'F2', 24)
pdf.add_centered_text(480, subtitle, 'F4', 16)
pdf.add_centered_text(440, f"By {author}", 'F4', 12)
pdf.add_line(150, 420, 462, 420, 2)
pdf.add_centered_text(380, "Because your brain works differently, not worse.", 'F4', 12, 0.3)

# Page 2 - Copyright
pdf.new_page()
pdf.add_centered_text(500, f"Copyright - {author}", 'F1', 10)
pdf.add_centered_text(480, "All rights reserved.", 'F1', 10)
pdf.add_centered_text(440, "This workbook is for educational purposes.", 'F1', 10)
pdf.add_centered_text(420, "Not a substitute for professional diagnosis or treatment.", 'F1', 10)

# Page 3 - What Are Executive Functions
pdf.new_page()
pdf.add_centered_text(740, "WHAT ARE EXECUTIVE FUNCTIONS?", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Executive functions are the brain's CEO - they manage, organize, and direct.", 'F1', 11)
pdf.add_text(50, 685, "With ADHD, these functions are impaired - NOT because you're lazy or stupid.", 'F1', 11)
ef_skills = [
    ("1. Working Memory", "Holding info in mind while using it"),
    ("2. Time Management", "Sensing time and planning accordingly"),
    ("3. Organization", "Creating and maintaining systems"),
    ("4. Task Initiation", "Starting tasks without procrastinating"),
    ("5. Emotional Regulation", "Managing emotional responses"),
    ("6. Flexible Thinking", "Adapting to changes and new info"),
    ("7. Self-Monitoring", "Tracking your own performance"),
    ("8. Planning/Prioritizing", "Setting goals and steps to reach them"),
]
y = 650
for skill, desc in ef_skills:
    pdf.add_text(60, y, skill, 'F2', 11)
    pdf.add_text(250, y, desc, 'F1', 11)
    y -= 28
pdf.add_text(50, y-20, "MY EXECUTIVE FUNCTION ASSESSMENT (rate each 1-10):", 'F2', 11)
y -= 45
for skill, _ in ef_skills:
    pdf.add_text(60, y, f"{skill}: ___/10", 'F1', 10)
    y -= 18


# Page 4 - Working Memory Strategies
pdf.new_page()
pdf.add_centered_text(740, "WORKING MEMORY STRATEGIES", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Your RAM is limited. Use external storage instead:", 'F2', 11)
strategies = [
    "Write EVERYTHING down - if it's not written, it doesn't exist",
    "Use a single capture system (one notebook, one app)",
    "Repeat information back immediately (active listening)",
    "Break instructions into single steps",
    "Use visual reminders (sticky notes, whiteboards)",
    "Set alarms for EVERYTHING (not just appointments)",
    "Create checklists for routine tasks",
    "Use body doubling for complex tasks",
]
y = 680
for s in strategies:
    pdf.add_text(60, y, f"- {s}", 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "MY WORKING MEMORY HACKS:", 'F2', 12)
y -= 35
pdf.add_text(50, y, "My capture system is: ________________________________", 'F1', 11)
y -= 25
pdf.add_text(50, y, "I will write things down by: ___________________________", 'F1', 11)
y -= 25
pdf.add_text(50, y, "My visual reminder system: ___________________________", 'F1', 11)
y -= 25
pdf.add_text(50, y, "How I'll remember verbal instructions: __________________", 'F1', 11)

# Page 5 - Time Management (Time Blindness)
pdf.new_page()
pdf.add_centered_text(740, "TIME MANAGEMENT & TIME BLINDNESS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "ADHD brains experience 'time blindness' - time is NOW or NOT NOW.", 'F2', 11)
pdf.add_text(50, 680, "Hacks to externalize time:", 'F2', 12)
hacks = [
    "Use analog clocks (visual representation of time passing)",
    "Set multiple alarms: 30 min, 15 min, 5 min before events",
    "Time yourself doing tasks to learn how long things REALLY take",
    "Use the 'time tax' - add 50% more time than you think you need",
    "Make time visible: Time Timer, hourglass, countdown apps",
    "Schedule transitions (getting ready IS part of the appointment)",
    "Body double with timers for task sprints",
]
y = 655
for h in hacks:
    pdf.add_text(60, y, f"- {h}", 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "TIME AUDIT - How long do these REALLY take me?", 'F2', 11)
y -= 40
tasks = ["Getting ready in morning", "Commute to work", "Cooking dinner",
         "Grocery shopping", "Getting ready for bed", "Email/messages"]
for t in tasks:
    pdf.add_text(60, y, f"{t}:", 'F1', 10)
    pdf.add_text(280, y, "I think: ___ min  Actual: ___ min", 'F1', 10)
    y -= 20

# Page 6 - Organization Systems
pdf.new_page()
pdf.add_centered_text(740, "ORGANIZATION SYSTEMS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "ADHD-friendly organization is VISUAL and EXTERNAL.", 'F2', 11)
pdf.add_text(50, 680, "Key principles:", 'F2', 12)
principles = [
    "Out of sight = out of mind. Use clear containers.",
    "One-step access (no lids, no closed drawers if possible)",
    "Landing zones: keys, wallet, phone go in ONE spot",
    "Labels everywhere (even if it feels excessive)",
    "Reduce decisions: capsule wardrobe, meal rotation",
    "Good enough IS good enough. Perfection kills systems.",
]
y = 660
for p in principles:
    pdf.add_text(60, y, f"- {p}", 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "MY ORGANIZATION PLAN:", 'F2', 12)
y -= 35
areas = ["My landing zone location:", "My daily 'launch pad' items:",
         "My filing system:", "My meal planning approach:",
         "My clothing system:"]
for a in areas:
    pdf.add_text(50, y, a, 'F1', 11)
    pdf.add_line(50, y-15, 540, y-15, 0.5, 0.7)
    y -= 35


# Page 7 - Task Initiation
pdf.new_page()
pdf.add_centered_text(740, "TASK INITIATION TECHNIQUES", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Starting is the hardest part. These strategies lower the activation energy:", 'F1', 11)
techniques = [
    ("2-Minute Rule:", "If it takes <2 minutes, do it NOW."),
    ("Body Doubling:", "Work alongside someone (in person or virtually)."),
    ("5-4-3-2-1 Launch:", "Count down and START on 1. Don't think."),
    ("Shrink the Task:", "Make it absurdly small. 'Open the document.'"),
    ("Temptation Bundling:", "Pair boring task with something enjoyable."),
    ("Environment Design:", "Remove friction. Set up materials in advance."),
    ("Implementation Intention:", "'When X happens, I will do Y.'"),
    ("Accountability:", "Tell someone what you'll do and by when."),
]
y = 680
for name, desc in techniques:
    pdf.add_text(60, y, name, 'F2', 10)
    pdf.add_text(210, y, desc, 'F1', 10)
    y -= 22
pdf.add_text(50, y-15, "MY TASK INITIATION TOOLKIT:", 'F2', 12)
y -= 40
pdf.add_text(50, y, "My go-to initiation strategy: ________________________________", 'F1', 11)
y -= 25
pdf.add_text(50, y, "My body double partner: ____________________________________", 'F1', 11)
y -= 25
pdf.add_text(50, y, "My implementation intention: When ___________, I will ___________", 'F1', 11)
y -= 25
pdf.add_text(50, y, "Tasks I always procrastinate:", 'F1', 11)
y -= 20
for i in range(4):
    pdf.add_line(70, y, 540, y, 0.5, 0.7)
    y -= 20

# Page 8 - Emotional Regulation
pdf.new_page()
pdf.add_centered_text(740, "EMOTIONAL REGULATION TOOLKIT", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "ADHD emotions are INTENSE, QUICK, and HARD TO REGULATE.", 'F2', 11)
pdf.add_text(50, 680, "This is part of ADHD, not a character flaw.", 'F1', 11)
pdf.add_text(50, 655, "WHEN OVERWHELMED:", 'F2', 12)
overwhelmed = [
    "STOP - don't react. Pause. Walk away if needed.",
    "Name the emotion out loud: 'I'm feeling frustrated.'",
    "Rate intensity 1-10. Above 7? Use body-based strategies first.",
    "Cold water on face/wrists (activates dive reflex, calms you)",
    "Box breathing: 4 in, 4 hold, 4 out, 4 hold",
]
y = 630
for o in overwhelmed:
    pdf.add_text(60, y, f"- {o}", 'F1', 10)
    y -= 18
pdf.add_text(50, y-10, "REJECTION SENSITIVE DYSPHORIA (RSD):", 'F2', 12)
y -= 30
pdf.add_text(50, y, "That extreme pain from perceived rejection IS real. Strategies:", 'F1', 10)
y -= 18
rsd = ["Reality check: Was I actually rejected, or am I interpreting?",
       "Self-compassion: 'This hurts, and that's okay.'",
       "Time buffer: Don't respond for 24 hours when triggered.",
       "Tell your person: 'I might be having an RSD moment.'"]
for r in rsd:
    pdf.add_text(60, y, f"- {r}", 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "MY EMOTIONAL PATTERNS:", 'F2', 11)
y -= 35
pdf.add_text(50, y, "My biggest trigger: ________________________________", 'F1', 11)
y -= 22
pdf.add_text(50, y, "My go-to calming strategy: ________________________________", 'F1', 11)
y -= 22
pdf.add_text(50, y, "My RSD trigger: ________________________________", 'F1', 11)

# Page 9 - Flexible Thinking
pdf.new_page()
pdf.add_centered_text(740, "FLEXIBLE THINKING EXERCISES", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "ADHD can make us rigid - stuck on one way or hyperfocused on details.", 'F1', 11)
pdf.add_text(50, 680, "Practice cognitive flexibility:", 'F2', 12)
exercises = [
    "When Plan A fails, write 3 alternatives BEFORE getting upset",
    "Practice 'yes, and...' thinking instead of 'but...'",
    "Ask: 'What would someone else do in this situation?'",
    "Reframe problems as puzzles to solve",
    "Notice when you're black-and-white thinking (all or nothing)",
]
y = 655
for e in exercises:
    pdf.add_text(60, y, f"- {e}", 'F1', 10)
    y -= 18
pdf.add_text(50, y-15, "FLEXIBILITY PRACTICE:", 'F2', 12)
y -= 35
for i in range(1, 4):
    pdf.add_text(50, y, f"Situation {i}: _______________________________________________", 'F1', 10)
    y -= 20
    pdf.add_text(50, y, "My rigid thought: ___________________________________________", 'F1', 10)
    y -= 20
    pdf.add_text(50, y, "Flexible alternative 1: ______________________________________", 'F1', 10)
    y -= 20
    pdf.add_text(50, y, "Flexible alternative 2: ______________________________________", 'F1', 10)
    y -= 20
    pdf.add_text(50, y, "Flexible alternative 3: ______________________________________", 'F1', 10)
    y -= 30


# Page 10 - Self-Monitoring Checklists
pdf.new_page()
pdf.add_centered_text(740, "SELF-MONITORING CHECKLISTS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "ADHD brains struggle to self-monitor. Use external check-ins:", 'F1', 11)
pdf.add_text(50, 675, "MORNING LAUNCH CHECKLIST:", 'F2', 12)
morning = ["Did I take my medication?", "Do I have my keys/wallet/phone?",
           "Am I dressed appropriately?", "Do I know my top 3 priorities today?",
           "Did I eat?", "Do I have what I need for today's tasks?"]
y = 655
for m in morning:
    pdf.add_rect(60, y-10, 12, 12)
    pdf.add_text(80, y-8, m, 'F1', 10)
    y -= 18
pdf.add_text(50, y-10, "WORK CHECK-IN (set alarm every 2 hours):", 'F2', 12)
y -= 30
work = ["Am I on task?", "What am I supposed to be doing right now?",
        "Am I in a rabbit hole?", "Do I need a break?",
        "Am I drinking water?"]
for w in work:
    pdf.add_rect(60, y-10, 12, 12)
    pdf.add_text(80, y-8, w, 'F1', 10)
    y -= 18
pdf.add_text(50, y-10, "END OF DAY REVIEW:", 'F2', 12)
y -= 30
eod = ["What did I accomplish today?", "What do I need to do tomorrow?",
       "Is anything time-sensitive I'm forgetting?", "Did I respond to important messages?",
       "What went well? What needs adjusting?"]
for e in eod:
    pdf.add_rect(60, y-10, 12, 12)
    pdf.add_text(80, y-8, e, 'F1', 10)
    y -= 18

# Pages 11-15 - Planning & Prioritizing Worksheets
for ws in range(5):
    pdf.new_page()
    pdf.add_centered_text(740, f"PLANNING & PRIORITIZING - WORKSHEET {ws+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, "Date: ________________  Week of: ________________", 'F1', 10)
    pdf.add_text(50, 685, "BRAIN DUMP (everything on your mind - no order):", 'F2', 11)
    y = 665
    for i in range(8):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-10, "NOW categorize using Eisenhower Matrix:", 'F2', 11)
    y -= 30
    pdf.add_text(50, y, "URGENT + IMPORTANT (Do first):", 'F2', 10)
    y -= 15
    for i in range(3):
        pdf.add_text(60, y, f"{i+1}. _________________________________________", 'F1', 9)
        y -= 15
    pdf.add_text(50, y-5, "IMPORTANT, NOT URGENT (Schedule):", 'F2', 10)
    y -= 20
    for i in range(3):
        pdf.add_text(60, y, f"{i+1}. _________________________________________", 'F1', 9)
        y -= 15
    pdf.add_text(50, y-5, "URGENT, NOT IMPORTANT (Delegate/Minimize):", 'F2', 10)
    y -= 20
    for i in range(3):
        pdf.add_text(60, y, f"{i+1}. _________________________________________", 'F1', 9)
        y -= 15
    pdf.add_text(50, y-5, "NOT URGENT, NOT IMPORTANT (Eliminate):", 'F2', 10)
    y -= 20
    for i in range(3):
        pdf.add_text(60, y, f"{i+1}. _________________________________________", 'F1', 9)
        y -= 15
    pdf.add_text(50, y-15, "MY TOP 3 FOR TODAY:", 'F2', 11)
    y -= 30
    for i in range(3):
        pdf.add_rect(60, y-10, 12, 12)
        pdf.add_text(80, y-8, f"________________________________________________", 'F1', 10)
        y -= 22

# Pages 16-18 - Goal Breakdown Templates
for g in range(3):
    pdf.new_page()
    pdf.add_centered_text(740, f"GOAL BREAKDOWN TEMPLATE {g+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, "MY GOAL: ________________________________________________", 'F2', 11)
    pdf.add_text(50, 688, "Deadline: ____________  Why this matters to me: ____________", 'F1', 10)
    pdf.add_text(50, 660, "BREAK IT DOWN (smallest possible steps):", 'F2', 11)
    y = 640
    for i in range(12):
        pdf.add_rect(55, y-10, 12, 12)
        pdf.add_text(75, y-8, f"Step {i+1}: _______________________________________ By: _______", 'F1', 9)
        y -= 22
    pdf.add_text(50, y-10, "What might get in the way? _______________________________", 'F1', 10)
    y -= 30
    pdf.add_text(50, y, "My plan for obstacles: _____________________________________", 'F1', 10)
    y -= 25
    pdf.add_text(50, y, "Accountability partner: ____________________________________", 'F1', 10)
    y -= 25
    pdf.add_text(50, y, "Reward when complete: _____________________________________", 'F1', 10)


# Pages 19-23 - Weekly EF Practice Log (5 pages)
for week in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(740, f"WEEKLY EF PRACTICE LOG - WEEK {week}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 712, "Date range: ___________________", 'F1', 10)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    y = 690
    for day in days:
        pdf.add_text(50, y, day, 'F2', 9)
        pdf.add_text(80, y, "EF skill practiced:____________", 'F1', 8)
        pdf.add_text(240, y, "Strategy used:______________", 'F1', 8)
        pdf.add_text(410, y, "Success? Y/N", 'F1', 8)
        pdf.add_line(50, y-10, 562, y-10, 0.3, 0.8)
        y -= 30
    pdf.add_text(50, y-5, "Wins this week:", 'F2', 10)
    pdf.add_line(50, y-20, 540, y-20, 0.5, 0.7)
    pdf.add_line(50, y-40, 540, y-40, 0.5, 0.7)
    pdf.add_text(50, y-55, "Challenges:", 'F2', 10)
    pdf.add_line(50, y-70, 540, y-70, 0.5, 0.7)
    pdf.add_line(50, y-90, 540, y-90, 0.5, 0.7)
    pdf.add_text(50, y-105, "Adjustments for next week:", 'F2', 10)
    pdf.add_line(50, y-120, 540, y-120, 0.5, 0.7)

# Pages 24-30 - remaining pages
# Page 24 - Personalized EF Strategy Plan
pdf.new_page()
pdf.add_centered_text(740, "MY PERSONALIZED EF STRATEGY PLAN", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
ef_areas = ["Working Memory", "Time Management", "Organization", "Task Initiation",
            "Emotional Regulation", "Flexible Thinking", "Self-Monitoring", "Planning"]
y = 705
for area in ef_areas:
    pdf.add_text(50, y, f"{area}:", 'F2', 10)
    pdf.add_text(50, y-15, "My strategy: _______________________________________________", 'F1', 9)
    pdf.add_text(50, y-30, "Tool/app I'll use: ___________________________________________", 'F1', 9)
    y -= 55

# Pages 25-30 additional content
for pg in range(6):
    pdf.new_page()
    titles = ["ADHD-FRIENDLY ROUTINES", "MY SUPPORT SYSTEM", "MEDICATION & SUPPLEMENT TRACKER",
              "ENVIRONMENT DESIGN PLAN", "CELEBRATING SMALL WINS", "MY ADHD STRENGTHS"]
    pdf.add_centered_text(740, titles[pg], 'F2', 16)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 0:
        pdf.add_text(50, 705, "Morning Routine (keep it SHORT - max 5 steps):", 'F2', 11)
        y = 685
        for i in range(5):
            pdf.add_text(60, y, f"{i+1}. _________________ Time: _____ min", 'F1', 10)
            y -= 20
        pdf.add_text(50, y-10, "Evening Routine (set tomorrow up for success):", 'F2', 11)
        y -= 30
        for i in range(5):
            pdf.add_text(60, y, f"{i+1}. _________________ Time: _____ min", 'F1', 10)
            y -= 20
    elif pg == 5:
        pdf.add_text(50, 705, "ADHD gives you SUPERPOWERS. Own them:", 'F2', 11, 0.3)
        strengths = ["Hyperfocus (when engaged, you're unstoppable)",
                     "Creativity (divergent thinking is your default)",
                     "Resilience (you've overcome more than most)",
                     "Energy/enthusiasm (when interested, you light up a room)",
                     "Crisis management (you thrive under pressure)",
                     "Big-picture thinking (connecting dots others miss)"]
        y = 680
        for s in strengths:
            pdf.add_text(60, y, f"* {s}", 'F1', 11)
            y -= 22
        pdf.add_text(50, y-20, "My personal ADHD superpowers:", 'F2', 11)
        y -= 45
        for i in range(5):
            pdf.add_line(60, y, 540, y, 0.5, 0.7)
            y -= 25
    else:
        y = 700
        for i in range(26):
            pdf.add_line(50, y, 562, y, 0.5, 0.7)
            y -= 24

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book177_Executive_Function_Workbook.pdf')
print("Book177_Executive_Function_Workbook.pdf created successfully!")
