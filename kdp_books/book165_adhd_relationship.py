from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "ADHD & LOVE"
subtitle = "A Relationship Workbook for Couples Where One Partner Has ADHD"

pdf.new_page()
pdf.add_centered_text(480, title, 'F2', 20)
pdf.add_centered_text(448, subtitle, 'F4', 10)
pdf.add_centered_text(350, "Understanding, Communicating,", 'F4', 11)
pdf.add_centered_text(335, "and Thriving Together", 'F4', 11)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(520, title, 'F2', 12)
pdf.add_centered_text(490, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(470, "All rights reserved.", 'F4', 10)

# Page 3: How ADHD Affects Relationships
pdf.new_page()
pdf.add_centered_text(610, "HOW ADHD AFFECTS RELATIONSHIPS", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 578
lines = [
    "ADHD doesn't just affect the person who has it - it affects the",
    "relationship dynamic. Understanding this is the first step to healing.",
    "",
    "COMMON PATTERNS IN ADHD RELATIONSHIPS:",
    "- Parent-child dynamic (non-ADHD partner becomes 'nagging parent')",
    "- Hyperfocus courtship -> neglect (intense beginning, then distracted)",
    "- Broken promises (not from lack of caring, but lack of follow-through)",
    "- Emotional volatility (dysregulation affects both partners)",
    "- Unequal mental load (one partner carries all the planning)",
    "- Communication breakdowns (distraction during conversations)",
    "",
    "WHAT'S HAPPENING (not excuses, but explanations):",
    "- Working memory issues: forget requests, lose track of conversations",
    "- Time blindness: chronically late, poor time estimation",
    "- Executive dysfunction: sees the mess but can't initiate cleaning",
    "- Emotional dysregulation: overreacts, can't let things go",
    "- Dopamine-seeking: novelty preference affects attention to partner",
    "",
    "THE GOOD NEWS:",
    "- Understanding WHY eliminates blame and builds compassion",
    "- Systems (not willpower) solve most ADHD relationship issues",
    "- Many ADHD traits are ASSETS: creativity, humor, passion, energy",
    "- Both partners have legitimate needs that CAN be met",
]
for line in lines:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 4: The ADHD Partner's Perspective
pdf.new_page()
pdf.add_centered_text(610, "THE ADHD PARTNER'S PERSPECTIVE", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 578
adhd_persp = [
    "If you have ADHD, your experience in the relationship may include:",
    "",
    "- Feeling like you can never do enough or do it right",
    "- Shame about forgetting things your partner told you",
    "- Frustration that you can't just 'be normal'",
    "- Feeling micromanaged or controlled",
    "- Defensive because you're constantly being corrected",
    "- Wondering if your partner even likes you anymore",
    "",
    "WHAT I WANT MY PARTNER TO KNOW:",
    "- I'm not forgetting because I don't care",
    "- When I zone out during conversations, I'm not ignoring you",
    "- I WANT to follow through - my brain makes it harder",
    "- I need systems and reminders, not lectures",
    "- When you nag, I shut down (even though I know you're frustrated)",
    "",
    "WHAT I TAKE RESPONSIBILITY FOR:",
    "1. ________________________________________________",
    "2. ________________________________________________",
    "3. ________________________________________________",
    "",
    "WHAT I NEED FROM MY PARTNER:",
    "1. ________________________________________________",
    "2. ________________________________________________",
    "3. ________________________________________________",
    "",
    "MY COMMITMENT TO THIS RELATIONSHIP:",
    "________________________________________________",
]
for line in adhd_persp:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 5: The Non-ADHD Partner's Perspective
pdf.new_page()
pdf.add_centered_text(610, "THE NON-ADHD PARTNER'S PERSPECTIVE", 'F2', 12)
pdf.add_line(40, 600, 392, 600)
y = 578
non_persp = [
    "If your partner has ADHD, your experience may include:",
    "",
    "- Feeling like the only responsible adult in the house",
    "- Exhaustion from carrying the mental load alone",
    "- Loneliness (your partner is physically present but mentally absent)",
    "- Resentment that builds over years of unmet expectations",
    "- Guilt for feeling angry (because you know it's not their 'fault')",
    "- Grief for the equal partnership you imagined",
    "",
    "WHAT I WANT MY PARTNER TO KNOW:",
    "- I didn't sign up to be your parent",
    "- When I remind you, it's because I don't trust it'll happen",
    "- I'm exhausted from thinking for two people",
    "- I need to see EFFORT, not just apologies",
    "- I love you AND I'm struggling with how things are",
    "",
    "WHAT I TAKE RESPONSIBILITY FOR:",
    "1. ________________________________________________",
    "2. ________________________________________________",
    "3. ________________________________________________",
    "",
    "WHAT I NEED FROM MY PARTNER:",
    "1. ________________________________________________",
    "2. ________________________________________________",
    "3. ________________________________________________",
    "",
    "MY COMMITMENT TO THIS RELATIONSHIP:",
    "________________________________________________",
]
for line in non_persp:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 6: Communication Breakdown Patterns
pdf.new_page()
pdf.add_centered_text(610, "COMMUNICATION BREAKDOWN PATTERNS", 'F2', 12)
pdf.add_line(40, 600, 392, 600)
y = 578
comm = [
    "PATTERN 1: The Nag Cycle",
    "Partner A asks -> Partner B forgets -> A asks again -> B feels",
    "nagged -> A feels unheard -> both resentful",
    "BREAK IT: Use shared reminders/apps, not verbal requests",
    "",
    "PATTERN 2: The Shutdown",
    "A criticizes -> B gets overwhelmed -> B shuts down/walks away ->",
    "A feels abandoned -> A escalates -> B shuts down more",
    "BREAK IT: Scheduled check-ins, time-outs with return time",
    "",
    "PATTERN 3: The Blame Game",
    "Something goes wrong -> A blames ADHD -> B says 'it's not an",
    "excuse' -> A feels shame -> A gets defensive -> fight",
    "BREAK IT: 'The ADHD made this harder AND I'm responsible'",
    "",
    "OUR PATTERN (identify your most common cycle):",
    "It starts when: ____________________________________",
    "Then I/we: _________________________________________",
    "It ends with: ______________________________________",
    "We could break it by: ______________________________",
    "",
    "COMMUNICATION RULES WE AGREE ON:",
    "1. No conversations about problems when: ___________",
    "2. Time-out signal: ________________________________",
    "3. We come back to discuss within: ___ hours",
]
for line in comm:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 7: Chore Wars Resolution System
pdf.new_page()
pdf.add_centered_text(610, "CHORE WARS RESOLUTION SYSTEM", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 578
chores = [
    "Chores are the #1 fight in ADHD relationships. Fix the SYSTEM:",
    "",
    "STEP 1: List ALL household tasks",
    "STEP 2: Each person marks: Love / Don't mind / Hate",
    "STEP 3: Assign based on preference, not 'fairness'",
    "STEP 4: ADHD partner gets external reminders for their tasks",
    "",
    "MY TASKS (with reminder system):",
    "Task: _________________ Reminder: _______________",
    "Task: _________________ Reminder: _______________",
    "Task: _________________ Reminder: _______________",
    "Task: _________________ Reminder: _______________",
    "Task: _________________ Reminder: _______________",
    "",
    "PARTNER'S TASKS:",
    "Task: _________________ ",
    "Task: _________________ ",
    "Task: _________________ ",
    "Task: _________________ ",
    "Task: _________________ ",
    "",
    "ADHD-FRIENDLY CHORE STRATEGIES:",
    "- Body doubling (do chores at the same time, side by side)",
    "- Timer challenges (race against the clock, not each other)",
    "- Music/podcast while doing chores (dopamine helper)",
    "- Lower standards for ADHD partner's tasks (done > perfect)",
    "- Outsource what you can afford (cleaning service, meal kit)",
]
for line in chores:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 8: Time Management as a Team
pdf.new_page()
pdf.add_centered_text(610, "TIME MANAGEMENT AS A TEAM", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 578
time_mgmt = [
    "Time blindness affects BOTH partners. Build systems together:",
    "",
    "SHARED CALENDAR (non-negotiable):",
    "App we'll use: ___________________",
    "[ ] Both have access and ADD events",
    "[ ] Review together every Sunday evening",
    "[ ] Include travel time for appointments",
    "",
    "PUNCTUALITY SYSTEM:",
    "For the ADHD partner leaving the house:",
    "- Set 'start getting ready' alarm, not 'leave' alarm",
    "- Ready = keys, wallet, phone, shoes ON",
    "- The non-ADHD partner does NOT manage departure time",
    "  (this creates parent-child dynamic)",
    "",
    "AVOIDING 'ADHD TAX' ON THE RELATIONSHIP:",
    "- Auto-pay all bills (ADHD partner should not be responsible",
    "  for time-sensitive tasks without automation)",
    "- Shared grocery/to-do list app",
    "- Weekly planning meeting (15 min max, same day/time)",
    "",
    "OUR WEEKLY PLANNING MEETING:",
    "Day: _____________ Time: ___________",
    "We will cover: calendar, finances, household needs",
    "Maximum time: 15 minutes (set timer!)",
]
for line in time_mgmt:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 9: Emotional Dysregulation & Your Partner
pdf.new_page()
pdf.add_centered_text(610, "EMOTIONAL DYSREGULATION & YOUR PARTNER", 'F2', 12)
pdf.add_line(40, 600, 392, 600)
y = 578
emo = [
    "ADHD emotions are BIGGER and FASTER than neurotypical emotions.",
    "This affects the relationship profoundly.",
    "",
    "FOR THE ADHD PARTNER:",
    "- Your emotions are real AND they're amplified by ADHD",
    "- You feel things at 100% when the situation is at 30%",
    "- You may say things you don't mean when flooded",
    "- Cool down takes longer (don't make decisions while activated)",
    "",
    "FOR THE NON-ADHD PARTNER:",
    "- Their reaction is not proportional - that's the ADHD, not you",
    "- Don't match their intensity (stay calm, don't escalate)",
    "- Give space without abandoning (I'm here when you're ready)",
    "- It's not your job to regulate their emotions",
    "",
    "OUR EMOTIONAL AGREEMENT:",
    "When I'm flooded, I will: ___________________________",
    "My partner will: ___________________________________",
    "We'll reconnect after: ___ minutes/hours",
    "Words I should NEVER say when activated:",
    "________________________________________________",
    "",
    "RSD (Rejection Sensitive Dysphoria):",
    "ADHD brains feel criticism/rejection as physical pain.",
    "This is not manipulation. It's neurological.",
    "How it shows up in us: _____________________________",
]
for line in emo:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 10: RSD Explained
pdf.new_page()
pdf.add_centered_text(610, "REJECTION SENSITIVE DYSPHORIA", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 578
rsd = [
    "RSD is intense emotional pain triggered by perceived rejection",
    "or criticism. It affects 99% of people with ADHD.",
    "",
    "WHAT RSD LOOKS LIKE IN RELATIONSHIPS:",
    "- Overreacting to mild criticism or suggestions",
    "- Assuming partner is disappointed/angry without evidence",
    "- People-pleasing to avoid any possibility of rejection",
    "- Withdrawing or rage in response to feeling criticized",
    "- Interpreting neutral facial expressions as negative",
    "",
    "FOR THE ADHD PARTNER - WHEN RSD HITS:",
    "1. Name it: 'This might be RSD talking, not reality'",
    "2. Ask: 'Are you actually upset with me or am I reading into this?'",
    "3. Wait before reacting (give it 20 minutes)",
    "4. Check the facts, not the feelings",
    "",
    "FOR THE NON-ADHD PARTNER - HOW TO HELP:",
    "1. Lead with reassurance: 'I love you AND I need to discuss...'",
    "2. Be specific, not general ('this dish' not 'you never clean')",
    "3. Separate the person from the behavior",
    "4. When they spiral: 'I'm not rejecting you. I'm addressing this thing.'",
    "",
    "OUR RSD PLAN:",
    "Code word for 'I think RSD is hitting': _______________",
    "What I need when it happens: ________________________",
    "What helps me come back: ___________________________",
]
for line in rsd:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 11: Rebuilding Trust After ADHD Chaos
pdf.new_page()
pdf.add_centered_text(610, "REBUILDING TRUST", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 578
trust = [
    "Trust erodes when promises are repeatedly broken - even",
    "unintentionally. Here's how to rebuild it:",
    "",
    "FOR THE ADHD PARTNER:",
    "- Stop making promises you can't keep (undercommit, overdeliver)",
    "- Use systems, not memory (if it's not written, it doesn't exist)",
    "- Acknowledge the impact of your ADHD on your partner",
    "- ADHD explains behavior but doesn't excuse harm",
    "- Show change through consistent SMALL actions over time",
    "",
    "FOR THE NON-ADHD PARTNER:",
    "- Notice and acknowledge improvements (even small ones)",
    "- Separate current behavior from past resentments",
    "- Allow your partner to rebuild trust gradually",
    "- Forgiveness is a process, not a one-time event",
    "",
    "TRUST-BUILDING AGREEMENT:",
    "One thing I commit to doing consistently for 30 days:",
    "ADHD partner: _____________________________________",
    "Non-ADHD partner will: _____________________________",
    "",
    "30-DAY CHECK-IN:",
    "Did it happen? [ ] Yes [ ] Mostly [ ] No",
    "How does it feel? __________________________________",
    "Next commitment: __________________________________",
]
for line in trust:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Pages 12-19: Weekly Couples Check-In (8 pages)
for week in range(1, 9):
    pdf.new_page()
    pdf.add_centered_text(610, f"WEEKLY COUPLES CHECK-IN - WEEK {week}", 'F2', 12)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    pdf.add_text(40, y, f"Date: ___/___/___  Time spent: ___ minutes", 'F1', 9)
    y -= 18
    checkin = [
        "WHAT WENT WELL THIS WEEK (be specific):",
        "Partner 1: ________________________________________",
        "Partner 2: ________________________________________",
        "",
        "WHAT WAS HARD THIS WEEK (no blame, just facts):",
        "Partner 1: ________________________________________",
        "Partner 2: ________________________________________",
        "",
        "WHAT I NEED FROM YOU NEXT WEEK:",
        "Partner 1: ________________________________________",
        "Partner 2: ________________________________________",
        "",
        "WHAT I APPRECIATE ABOUT YOU:",
        "Partner 1: ________________________________________",
        "Partner 2: ________________________________________",
        "",
        "SYSTEM CHECK: Are our systems working?",
        "Calendar: [ ] Working [ ] Needs adjustment",
        "Chores: [ ] Working [ ] Needs adjustment",
        "Communication: [ ] Working [ ] Needs adjustment",
        "",
        "ONE THING WE'LL DO DIFFERENTLY NEXT WEEK:",
        "__________________________________________________",
    ]
    for line in checkin:
        pdf.add_text(40, y, line, 'F4', 9.5)
        y -= 14

# Page 20: Date Night Planning
pdf.new_page()
pdf.add_centered_text(610, "DATE NIGHT PLANNING (ADHD-FRIENDLY)", 'F2', 12)
pdf.add_line(40, 600, 392, 600)
y = 578
dates = [
    "ADHD-friendly dates: Novel, active, engaging (not 'sit and talk'):",
    "",
    "IDEAS THAT WORK FOR ADHD COUPLES:",
    "- Cooking a new recipe together (novelty + activity)",
    "- Mini golf, bowling, arcade (movement + fun)",
    "- Taking a class together (pottery, dance, cooking)",
    "- Hiking or biking (movement helps ADHD focus)",
    "- Game night (board games, card games, video games)",
    "- Food tour / trying a new restaurant",
    "- Escape room (ADHD brains shine here!)",
    "- Drive with no destination (ADHD loves spontaneity)",
    "",
    "DATE PLANNING SYSTEM:",
    "Who plans this month: _______________",
    "(Alternate months so one person doesn't always plan)",
    "",
    "OUR DATE NIGHTS THIS MONTH:",
    "Date 1: _______________ Day/Time: __________",
    "Date 2: _______________ Day/Time: __________",
    "",
    "RULE: No discussing problems/household stuff on dates.",
    "This is CONNECTION time only.",
    "",
    "DATES WE WANT TO TRY:",
    "1. _______________________________________________",
    "2. _______________________________________________",
    "3. _______________________________________________",
]
for line in dates:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 21: ADHD Accommodation Requests & Partner Needs
pdf.new_page()
pdf.add_centered_text(610, "ACCOMMODATION REQUESTS", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 578
accom = [
    "ADHD PARTNER'S ACCOMMODATION REQUESTS:",
    "(What I need to function, not excuses to avoid responsibility)",
    "",
    "1. ________________________________________________",
    "2. ________________________________________________",
    "3. ________________________________________________",
    "4. ________________________________________________",
    "5. ________________________________________________",
    "",
    "NON-ADHD PARTNER'S NEEDS LIST:",
    "(What I need to feel respected and partnered)",
    "",
    "1. ________________________________________________",
    "2. ________________________________________________",
    "3. ________________________________________________",
    "4. ________________________________________________",
    "5. ________________________________________________",
    "",
    "OUR RELATIONSHIP AGREEMENTS:",
    "We agree to: _______________________________________",
    "________________________________________________",
    "________________________________________________",
    "________________________________________________",
    "________________________________________________",
    "",
    "Signed: _______________ & _______________",
    "Date: ___/___/___",
    "Review date: ___/___/___ (every 3 months)",
]
for line in accom:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book165_ADHD_Relationship_Workbook.pdf')
print("Book165_ADHD_Relationship_Workbook.pdf created successfully!")
