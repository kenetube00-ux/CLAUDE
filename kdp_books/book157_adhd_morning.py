from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "ADHD MORNING ROUTINE PLANNER"
subtitle = "Stop the Chaos, Start Your Day Right"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 18)
pdf.add_centered_text(510, subtitle, 'F4', 14)
pdf.add_centered_text(400, "Practical Systems for Adults with ADHD", 'F4', 12)
pdf.add_centered_text(380, "Who Struggle with Mornings", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 12)
pdf.add_centered_text(560, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(540, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: Why Mornings Are Hard with ADHD
pdf.new_page()
pdf.add_centered_text(750, "WHY MORNINGS ARE HARD WITH ADHD", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
lines = [
    "If mornings feel like your personal nemesis, you're not lazy.",
    "ADHD brains have specific challenges that make mornings harder:",
    "",
    "1. SLEEP INERTIA: ADHD brains take longer to 'boot up'",
    "   Your prefrontal cortex (planning/decision brain) is sluggish",
    "",
    "2. TIME BLINDNESS: You genuinely don't feel time passing",
    "   '5 more minutes' turns into 45 without you noticing",
    "",
    "3. DECISION FATIGUE: Every choice costs more mental energy",
    "   What to wear, what to eat, what to bring = overwhelming",
    "",
    "4. TRANSITION DIFFICULTY: Switching from sleep to action is HARD",
    "   Your brain resists changing states (this is neurological, not moral)",
    "",
    "5. WORKING MEMORY ISSUES: You forget steps mid-routine",
    "   Start brushing teeth, get distracted, forget breakfast",
    "",
    "6. DOPAMINE DEFICIT: Routine tasks produce zero dopamine",
    "   Your brain screams 'BORING' and seeks stimulation instead",
    "",
    "THE GOOD NEWS:",
    "You don't need more willpower. You need better SYSTEMS.",
    "This planner gives you external structure so your brain doesn't",
    "have to work so hard. Let the system do the thinking.",
]
for line in lines:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 17

# Page 4: The 3-Anchor System
pdf.new_page()
pdf.add_centered_text(750, "THE 3-ANCHOR SYSTEM", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
anchor_text = [
    "Instead of a complex morning routine, build around 3 ANCHORS.",
    "Anchors are non-negotiable actions that everything else attaches to.",
    "",
    "ANCHOR 1: THE WAKE-UP ANCHOR",
    "This is what pulls you out of bed. Choose ONE:",
    "  [ ] Alarm across the room (must physically get up)",
    "  [ ] Light therapy lamp on timer",
    "  [ ] Phone alarm in bathroom",
    "  [ ] Coffee maker on auto-timer (smell gets you up)",
    "  [ ] Accountability partner texts/calls",
    "  My wake-up anchor: _________________________________",
    "",
    "ANCHOR 2: THE BODY ANCHOR",
    "This 'turns on' your body and brain. Choose ONE:",
    "  [ ] Splash cold water on face immediately",
    "  [ ] 2-minute stretch routine (same every day)",
    "  [ ] Step outside for 60 seconds of sunlight",
    "  [ ] Quick shower (no decisions - same temp, same products)",
    "  [ ] 10 jumping jacks right out of bed",
    "  My body anchor: ____________________________________",
    "",
    "ANCHOR 3: THE LAUNCH ANCHOR",
    "This is your 'out the door' signal. Choose ONE:",
    "  [ ] Grab launch pad bag (pre-packed night before)",
    "  [ ] Set 'leaving NOW' alarm 5 min before deadline",
    "  [ ] Keys + phone + wallet checkpoint at door",
    "  [ ] Partner/roommate 5-minute warning",
    "  My launch anchor: __________________________________",
    "",
    "RULE: Do your 3 anchors in ORDER, every single day.",
    "Everything else can flex. The anchors don't."
]
for line in anchor_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 5: Visual Routine Builder
pdf.new_page()
pdf.add_centered_text(750, "VISUAL ROUTINE BUILDER", 'F2', 15)
pdf.add_centered_text(732, "Build YOUR custom morning sequence", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 700
pdf.add_text(50, y, "List ONLY essential tasks. Less is more with ADHD. Aim for 5-8 steps max.", 'F4', 10)
y -= 20
pdf.add_text(50, y, "MY MORNING ROUTINE (in order):", 'F2', 11)
y -= 22
for i in range(10):
    pdf.add_filled_rect(50, y-4, 520, 28, 0.95)
    pdf.add_text(55, y, f"Step {i+1}:", 'F2', 10)
    pdf.add_text(100, y, "Task: _____________________________", 'F1', 10)
    pdf.add_text(360, y, "Time needed: ___ min", 'F1', 10)
    y -= 32
y -= 10
pdf.add_text(50, y, "TOTAL TIME NEEDED: _______ minutes", 'F2', 11)
y -= 20
pdf.add_text(50, y, "ADD BUFFER: + 15 minutes (because ADHD time isn't real time)", 'F2', 11)
y -= 20
pdf.add_text(50, y, "I need to wake up at: _______ to leave by: _______", 'F2', 11)
y -= 30
pdf.add_text(50, y, "TIP: Take a photo of this list and set it as your phone lockscreen.", 'F5', 10)

# Page 6: Time Estimation Practice
pdf.new_page()
pdf.add_centered_text(750, "TIME ESTIMATION PRACTICE", 'F2', 15)
pdf.add_centered_text(732, "How long things ACTUALLY take (not how long you think)", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 695
pdf.add_text(50, y, "For 5 days, time your morning tasks. You'll be shocked.", 'F4', 10.5)
y -= 25
tasks = ["Shower (water on to fully dressed)", "Get dressed (picking outfit to done)",
         "Eat breakfast", "Brush teeth + face + hair", "Pack bag / gather things",
         "Find keys/phone/wallet", "Get in car / to bus stop", "Scroll phone (be honest)"]
pdf.add_text(50, y, "TASK", 'F2', 9)
pdf.add_text(240, y, "GUESS", 'F2', 9)
pdf.add_text(310, y, "DAY 1", 'F2', 9)
pdf.add_text(360, y, "DAY 2", 'F2', 9)
pdf.add_text(410, y, "DAY 3", 'F2', 9)
pdf.add_text(460, y, "DAY 4", 'F2', 9)
pdf.add_text(510, y, "DAY 5", 'F2', 9)
y -= 4
pdf.add_line(50, y, 560, y, 0.5)
y -= 16
for task in tasks:
    pdf.add_text(50, y, task, 'F4', 9)
    pdf.add_text(240, y, "___min", 'F3', 8)
    pdf.add_text(310, y, "___min", 'F3', 8)
    pdf.add_text(360, y, "___min", 'F3', 8)
    pdf.add_text(410, y, "___min", 'F3', 8)
    pdf.add_text(460, y, "___min", 'F3', 8)
    pdf.add_text(510, y, "___min", 'F3', 8)
    y -= 20
    pdf.add_line(50, y+8, 560, y+8, 0.3, 0.8)
y -= 15
pdf.add_text(50, y, "TOTAL ACTUAL TIME (average): _______ minutes", 'F2', 10)
y -= 20
pdf.add_text(50, y, "INSIGHT: Most people with ADHD underestimate by 50-100%.", 'F5', 10)
y -= 14
pdf.add_text(50, y, "Use your ACTUAL times, not your optimistic guesses.", 'F5', 10)

# Page 7: Launch Pad Setup Guide
pdf.new_page()
pdf.add_centered_text(750, "LAUNCH PAD SETUP GUIDE", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
lpad = [
    "A 'Launch Pad' is a designated spot by your door where EVERYTHING",
    "you need to leave the house lives. No searching. No decisions.",
    "",
    "WHAT YOU NEED:",
    "- A table, shelf, hook, or basket BY your exit door",
    "- Good enough lighting to see it",
    "- Nothing else stored there (dedicated space only)",
    "",
    "WHAT GOES ON THE LAUNCH PAD (every night):",
    "[ ] Keys",
    "[ ] Wallet/purse",
    "[ ] Phone (charging there overnight is ideal)",
    "[ ] Bag/backpack (packed with tomorrow's needs)",
    "[ ] Sunglasses",
    "[ ] Jacket/coat (weather appropriate)",
    "[ ] Medications",
    "[ ] Lunch (or money for lunch)",
    "[ ] Anything specific to tomorrow: ___________________",
    "",
    "MY LAUNCH PAD LOCATION: _____________________________",
    "",
    "THE RULE: If it leaves the house with you, it lives on the",
    "launch pad. If it comes home with you, it goes back to the",
    "launch pad. Every. Single. Time.",
    "",
    "PRO TIP: Put a small basket/tray for small items.",
    "Hooks for keys and bags. A charging station for devices.",
]
for line in lpad:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 16

# Page 8: Clothing Decision Eliminator
pdf.new_page()
pdf.add_centered_text(750, "CLOTHING DECISION ELIMINATOR", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
clothing = [
    "Getting dressed should not take 20 minutes. Here's how to fix it:",
    "",
    "STRATEGY 1: THE CAPSULE WARDROBE",
    "Pick 5-7 outfits that all work. Rotate through them. Done.",
    "",
    "STRATEGY 2: THE UNIFORM METHOD",
    "Wear basically the same thing every day (like Steve Jobs).",
    "Nobody notices or cares. Trust me.",
    "",
    "STRATEGY 3: OUTFIT PREP NIGHT BEFORE",
    "Set out tomorrow's complete outfit (including underwear, socks,",
    "shoes) the night before. Decision made = morning brain off the hook.",
    "",
    "MY WEEKLY OUTFIT PLAN:",
]
for line in clothing:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 16
y -= 5
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    pdf.add_text(50, y, f"{day}:", 'F2', 10)
    pdf.add_line(130, y-2, 560, y-2, 0.5, 0.5)
    y -= 22
y -= 15
pdf.add_text(50, y, "WEATHER OVERRIDE: If weather changes, I wear: ______________", 'F4', 10)

# Page 9: Breakfast Simplification System
pdf.new_page()
pdf.add_centered_text(750, "BREAKFAST SIMPLIFICATION", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
breakfast = [
    "ADHD breakfast rules: NO decisions, NO cooking time, NO cleanup.",
    "",
    "TIER 1: ZERO EFFORT (grab and eat, even in the car)",
    "- Protein bar + banana",
    "- Overnight oats (made night before)",
    "- Hard boiled eggs (batch prepped Sunday)",
    "- Greek yogurt cup + granola",
    "- Peanut butter on bread (no toasting needed)",
    "",
    "TIER 2: LOW EFFORT (5 min or less)",
    "- Smoothie (pre-measured bags in freezer + blend)",
    "- Toast + avocado/peanut butter",
    "- Cereal (yes, cereal counts as breakfast)",
    "- Microwave oatmeal packet",
    "",
    "TIER 3: SKIP BREAKFAST OPTION",
    "If eating in the morning is impossible, pre-pack a mid-morning snack.",
    "It's better than nothing and removes the morning pressure.",
    "",
    "MY BREAKFAST ROTATION (no thinking required):",
    "Mon/Wed/Fri: _______________________________________",
    "Tue/Thu: ___________________________________________",
    "Weekends: __________________________________________",
    "",
    "GROCERY LIST ADDITION (always have on hand):",
    "__________, __________, __________, __________",
]
for line in breakfast:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 16

# Pages 10-21: 30-day Morning Tracker (12 pages, ~3 days per page area; let's do 2-3 per page)
for page_num in range(12):
    pdf.new_page()
    start_day = page_num * 3 + 1
    end_day = min(start_day + 2, 30)
    pdf.add_centered_text(750, f"30-DAY MORNING TRACKER", 'F2', 14)
    pdf.add_text(450, 750, f"Days {start_day}-{end_day}", 'F1', 10)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    for day in range(start_day, end_day + 1):
        pdf.add_filled_rect(48, y-80, 520, 95, 0.96)
        pdf.add_text(50, y, f"DAY {day}   Date: ___/___/___", 'F2', 10)
        y -= 16
        pdf.add_text(50, y, "Wake time (alarm): ______  Wake time (actual): ______", 'F3', 9)
        y -= 14
        pdf.add_text(50, y, "Routine completed?  [ ] Yes  [ ] Mostly  [ ] No", 'F3', 9)
        y -= 14
        pdf.add_text(50, y, "Out the door on time?  [ ] Yes  [ ] Late by ___ min", 'F3', 9)
        y -= 14
        pdf.add_text(50, y, "Mood leaving house: 1-5 (1=stressed 5=calm): ___", 'F3', 9)
        y -= 14
        pdf.add_text(50, y, "What worked: _________________________________________", 'F3', 9)
        y -= 14
        pdf.add_text(50, y, "What didn't: _________________________________________", 'F3', 9)
        y -= 24

# Page 22: Evening Prep Checklist
pdf.new_page()
pdf.add_centered_text(750, "EVENING PREP CHECKLIST", 'F2', 15)
pdf.add_centered_text(732, "Set Up Tomorrow Tonight (Your Morning Self Will Thank You)", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 695
pdf.add_text(50, y, "Do this checklist every evening. It takes 10-15 minutes and saves", 'F4', 10.5)
y -= 14
pdf.add_text(50, y, "your morning self 30+ minutes of chaos.", 'F4', 10.5)
y -= 25
evening_items = [
    "Set out tomorrow's outfit (full outfit including shoes)",
    "Pack bag/backpack with everything needed tomorrow",
    "Place keys/wallet/phone on launch pad",
    "Check calendar - any special items needed?",
    "Pack lunch or set out lunch money",
    "Charge all devices",
    "Set alarm(s) - at least 2 alarms",
    "Quick kitchen reset (so morning you doesn't face a mess)",
    "Review tomorrow's schedule (reduce morning surprises)",
    "Lay out medications/vitamins by water glass",
    "Note anything special for morning: _________________",
]
for item in evening_items:
    pdf.add_rect(55, y-2, 12, 12, 0.5)
    pdf.add_text(75, y, item, 'F4', 10.5)
    y -= 24
y -= 15
pdf.add_text(50, y, "EVENING PREP TIME: I'll do this at ___:___ pm every night.", 'F2', 10)
y -= 18
pdf.add_text(50, y, "REMINDER: Set a phone alarm for your evening prep time!", 'F5', 10)

# Page 23: Troubleshooting Common Morning Fails
pdf.new_page()
pdf.add_centered_text(750, "TROUBLESHOOTING COMMON MORNING FAILS", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
issues = [
    ("Can't get out of bed (hit snooze 10 times)", [
        "- Put alarm across room / in bathroom",
        "- Use alarmy app (requires photo/math to turn off)",
        "- Set coffee maker auto-start (smell motivates)"
    ]),
    ("Get sucked into phone immediately", [
        "- Phone stays on launch pad, not bedside",
        "- No social media until after anchor 2",
        "- Use app blocker until 9am"
    ]),
    ("Can't find things (keys, shoes, papers)", [
        "- Everything has ONE home. Always.",
        "- Launch pad system (page 7)",
        "- Tile/AirTag on keys and wallet"
    ]),
    ("Take too long in shower", [
        "- Set waterproof timer for 7 minutes",
        "- Shower at night instead (remove from morning)",
        "- Use shower routine: hair, face, body, done"
    ]),
    ("Hyperfocus on random thing", [
        "- Visual timer in every room (Time Timer brand)",
        "- 'This can wait' sticky note on mirror",
        "- Body double: morning phone call with friend"
    ]),
    ("Run out of time for breakfast", [
        "- Grab-and-go options ONLY (see page 9)",
        "- Eat at work/school instead",
        "- Pre-made smoothie in fridge"
    ]),
]
for problem, solutions in issues:
    pdf.add_text(50, y, f"PROBLEM: {problem}", 'F2', 10)
    y -= 15
    for s in solutions:
        pdf.add_text(50, y, s, 'F4', 9.5)
        y -= 13
    y -= 12

# Page 24: Kids Morning Routine Version
pdf.new_page()
pdf.add_centered_text(750, "KIDS MORNING ROUTINE", 'F2', 15)
pdf.add_centered_text(732, "If you have ADHD kids who also struggle with mornings", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 695
kids_text = [
    "ADHD often runs in families. If your child also has morning chaos:",
    "",
    "VISUAL SCHEDULE (use pictures for younger kids):",
    "1. Wake up + get out of bed",
    "2. Use bathroom",
    "3. Get dressed (outfit laid out night before)",
    "4. Eat breakfast (choice of 2 options only)",
    "5. Brush teeth",
    "6. Grab backpack (packed night before)",
    "7. Shoes on + out the door",
    "",
    "TIPS FOR ADHD KIDS' MORNINGS:",
    "- Use a visual timer they can see counting down",
    "- 'Beat the timer' makes it a game (dopamine!)",
    "- Same order every single day (no variety)",
    "- Reduce decisions to 0 (lay everything out)",
    "- Music playlist that times the routine",
    "- Natural consequences > yelling (miss bus = walk)",
    "",
    "MY CHILD'S MORNING ROUTINE:",
    "Step 1: ______________ (__ min)",
    "Step 2: ______________ (__ min)",
    "Step 3: ______________ (__ min)",
    "Step 4: ______________ (__ min)",
    "Step 5: ______________ (__ min)",
    "Step 6: ______________ (__ min)",
    "Total time needed: _____ min",
    "Must wake by: _____",
]
for line in kids_text:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 16

# Page 25: Partner Communication About Mornings
pdf.new_page()
pdf.add_centered_text(750, "PARTNER COMMUNICATION", 'F2', 15)
pdf.add_centered_text(732, "Talking to your partner/household about your needs", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 695
partner_text = [
    "Mornings can create household tension. Here's how to talk about it:",
    "",
    "WHAT TO EXPLAIN TO YOUR PARTNER:",
    "'My brain works differently in the morning. It's not laziness",
    "or disrespect. I need external supports because my internal",
    "clock and executive function are impaired before I'm fully awake.'",
    "",
    "WHAT HELPS (share this list with them):",
    "- Don't ask me complex questions before [time]",
    "- If I seem stuck/zoned out, a gentle physical cue helps",
    "- Don't rearrange my launch pad or morning setup",
    "- Specific, brief reminders are helpful (not nagging)",
    "- Morning is not the time for hard conversations",
    "",
    "WHAT I NEED FROM MY PARTNER/HOUSEHOLD:",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "",
    "WHAT I CAN OFFER IN RETURN:",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "",
    "OUR MORNING AGREEMENT:",
    "We agree that mornings will work like this: _______________",
    "__________________________________________________",
    "__________________________________________________",
    "",
    "Signed: ___________ & ___________  Date: __________"
]
for line in partner_text:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book157_ADHD_Morning_Routine.pdf')
print("Book157_ADHD_Morning_Routine.pdf created successfully!")
