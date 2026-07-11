from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "ANGER MANAGEMENT WORKBOOK FOR TEENS"
subtitle = "Cool Down Before You Blow Up"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 18)
pdf.add_centered_text(510, subtitle, 'F4', 14)
pdf.add_centered_text(400, "A Practical Guide for Teenagers", 'F4', 12)
pdf.add_centered_text(380, "to Understand and Manage Anger", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 12)
pdf.add_centered_text(560, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(540, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: What is Anger (Teen-Friendly)
pdf.new_page()
pdf.add_centered_text(750, "WHAT IS ANGER? (Real Talk)", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
lines = [
    "Let's be honest: everyone gets angry. Your parents, your teachers,",
    "your friends - literally everyone. Anger is a NORMAL emotion. It's not",
    "bad or wrong to feel angry. The problem only starts when anger makes",
    "you do things you regret.",
    "",
    "WHY DO TEENS GET SO ANGRY?",
    "- Your brain is literally under construction (prefrontal cortex developing)",
    "- Hormones are all over the place",
    "- You're dealing with more social pressure than ever",
    "- You want independence but still have rules to follow",
    "- School stress, friend drama, family issues - it's a LOT",
    "",
    "ANGER IS A SECONDARY EMOTION",
    "Under anger, there's usually something else:",
    "  - Feeling disrespected or embarrassed",
    "  - Feeling hurt or rejected",
    "  - Feeling scared or anxious",
    "  - Feeling powerless or unheard",
    "  - Feeling overwhelmed",
    "",
    "THIS WORKBOOK WILL HELP YOU:",
    "- Understand YOUR anger (everyone's is different)",
    "- Catch it before it explodes",
    "- Handle it without making things worse",
    "- Communicate what you actually need",
    "- Stop the guilt/shame cycle after blowups",
    "",
    "You're not broken. You just need better tools."
]
for line in lines:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 17

# Page 4: Anger Triggers Worksheet
pdf.new_page()
pdf.add_centered_text(750, "MY ANGER TRIGGERS", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "What sets YOU off? Be specific. Circle the ones that hit hardest:", 'F4', 10.5)
y -= 25
triggers = [
    "Being told what to do / micromanaged", "Getting embarrassed in front of others",
    "Someone touching my stuff", "Being accused of something I didn't do",
    "People talking behind my back", "Feeling left out or excluded",
    "Parents comparing me to siblings", "Teachers being unfair",
    "Someone breaking a promise", "Losing at something important to me",
    "Being interrupted or ignored", "Someone disrespecting my friends/family",
    "Not getting enough sleep", "Being hungry (hangry is real)",
    "Social media drama", "Feeling misunderstood"
]
for t in triggers:
    pdf.add_text(60, y, f"o  {t}", 'F1', 10)
    y -= 18
y -= 10
pdf.add_text(50, y, "MY TOP 5 PERSONAL TRIGGERS:", 'F2', 11)
y -= 22
for i in range(5):
    pdf.add_text(50, y, f"{i+1}.", 'F1', 10)
    pdf.add_line(70, y-2, 560, y-2, 0.5, 0.5)
    y -= 14
    pdf.add_text(70, y, "How often (daily/weekly/rarely): _________  Intensity 1-10: ___", 'F1', 9)
    y -= 22

# Page 5: Physical Warning Signs Body Map
pdf.new_page()
pdf.add_centered_text(750, "PHYSICAL WARNING SIGNS", 'F2', 15)
pdf.add_centered_text(732, "Your body talks before you explode", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 700
pdf.add_text(50, y, "Check the warning signs YOUR body gives you:", 'F2', 10)
y -= 22
body_signs = [
    ("HEAD:", ["Headache", "Seeing red/tunnel vision", "Can't think straight", "Racing thoughts"]),
    ("FACE/NECK:", ["Jaw clenching", "Face gets hot/red", "Neck tension", "Teeth grinding"]),
    ("CHEST:", ["Heart pounding", "Chest tight", "Breathing fast", "Feel like screaming"]),
    ("STOMACH:", ["Stomach in knots", "Nausea", "Appetite disappears", "Butterflies"]),
    ("HANDS/ARMS:", ["Fists clenching", "Shaking", "Want to hit something", "Gripping things hard"]),
    ("LEGS/FEET:", ["Pacing", "Leg bouncing", "Want to run", "Stomping"]),
]
for area, signs in body_signs:
    pdf.add_text(50, y, area, 'F2', 10)
    y -= 16
    for s in signs:
        pdf.add_rect(65, y-1, 8, 8, 0.5)
        pdf.add_text(80, y, s, 'F4', 9.5)
        y -= 15
    y -= 8
y -= 10
pdf.add_text(50, y, "My FIRST warning sign (the earliest one I notice):", 'F2', 10)
y -= 16
pdf.add_line(50, y, 560, y, 0.5, 0.5)

# Page 6: The Volcano Model
pdf.new_page()
pdf.add_centered_text(750, "THE VOLCANO MODEL", 'F2', 15)
pdf.add_centered_text(732, "Anger has levels - know where you are", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 695
levels = [
    ("LEVEL 5 - ERUPTION (10/10)", [
        "Full explosion. Yelling, breaking things, saying horrible things.",
        "You can't think. Adrenaline has taken over completely.",
        "RECOVERY TIME: 30-60 minutes minimum"
    ]),
    ("LEVEL 4 - ABOUT TO BLOW (7-9/10)", [
        "Shouting, aggressive body language, threatening.",
        "Still a tiny bit of control. THIS IS YOUR LAST CHANCE to use tools.",
        "BEST MOVE: Walk away NOW. No discussion. Just leave safely."
    ]),
    ("LEVEL 3 - HEATING UP (5-6/10)", [
        "Arguing, raised voice, sarcasm, door slamming.",
        "You can still think but it's getting harder.",
        "BEST MOVE: Use a cool-down strategy. Tell them you need a minute."
    ]),
    ("LEVEL 2 - WARMING (3-4/10)", [
        "Irritated, annoyed, eye-rolling, short responses.",
        "You can still make good choices easily here.",
        "BEST MOVE: Name it. 'I'm getting frustrated.' Use a strategy."
    ]),
    ("LEVEL 1 - CALM (1-2/10)", [
        "Chill, relaxed, can handle things that come up.",
        "This is where you build skills and make plans.",
        "BEST MOVE: Practice your strategies so they're automatic."
    ]),
]
for level_name, descriptions in levels:
    pdf.add_text(50, y, level_name, 'F2', 11)
    y -= 16
    for d in descriptions:
        pdf.add_text(60, y, d, 'F4', 9.5)
        y -= 14
    y -= 12
y -= 5
pdf.add_text(50, y, "Right now I'm usually at Level ___ when I start my strategies.", 'F2', 10)
y -= 16
pdf.add_text(50, y, "I want to start catching myself at Level ___.", 'F2', 10)

# Page 7: Cool-Down Strategies Menu
pdf.new_page()
pdf.add_centered_text(750, "COOL-DOWN STRATEGIES MENU", 'F2', 15)
pdf.add_centered_text(732, "Pick 5 favorites and practice them when calm", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 700
strategies = [
    "1. Box breathing (4 in, 4 hold, 4 out, 4 hold)",
    "2. Squeeze an ice cube in your hand (pain redirect)",
    "3. Sprint or do jumping jacks for 60 seconds",
    "4. Listen to ONE song (loud, with headphones)",
    "5. Count backwards from 100 by 7s",
    "6. Cold water on wrists and face",
    "7. Text a friend about something totally different",
    "8. Draw your anger (abstract scribbles count)",
    "9. Write down everything you want to say (don't send)",
    "10. Do 20 push-ups or wall sits",
    "11. Name 5 things you can see, 4 hear, 3 touch, 2 smell, 1 taste",
    "12. Rip up paper into tiny pieces",
    "13. Put in earbuds and listen to a guided meditation (even 2 min)",
    "14. Go outside - just stand outside for 2 minutes",
    "15. Squeeze a stress ball until your hand is tired",
    "16. Watch a funny video (have one saved for emergencies)",
    "17. Chew gum aggressively",
    "18. Take a shower (water resets your nervous system)",
    "19. Journal stream-of-consciousness for 5 minutes",
    "20. Play a simple phone game (Tetris, puzzle) for 5 min",
]
for s in strategies:
    pdf.add_text(50, y, s, 'F4', 10)
    y -= 17
y -= 10
pdf.add_text(50, y, "MY TOP 5 GO-TO STRATEGIES:", 'F2', 10)
y -= 18
for i in range(5):
    pdf.add_text(50, y, f"{i+1}. ___________________________________________", 'F1', 10)
    y -= 16

# Pages 8-12: Thought Challenging for Angry Thoughts (5 pages)
thought_scenarios = [
    ("Someone posts something mean about you online", "Everyone is laughing at me. I'll destroy them."),
    ("Your parent says you can't go out with friends", "They don't trust me! They ruin EVERYTHING."),
    ("A teacher calls you out in front of the class", "They're trying to humiliate me. I hate them."),
    ("Your friend cancels plans last minute", "Nobody actually cares about me. They're fake."),
    ("Your sibling takes your stuff without asking", "They have ZERO respect for me. They deserve payback."),
]
for i, (situation, hot_thought) in enumerate(thought_scenarios):
    pdf.new_page()
    pdf.add_centered_text(750, f"THOUGHT CHALLENGE #{i+1}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 715
    pdf.add_text(50, y, f"SITUATION: {situation}", 'F2', 10.5)
    y -= 20
    pdf.add_text(50, y, f"HOT THOUGHT: \"{hot_thought}\"", 'F4', 10.5)
    y -= 25
    prompts = [
        "What emotion am I actually feeling under the anger?",
        "_________________________________________________",
        "",
        "Is my hot thought 100% true? What's the evidence?",
        "_________________________________________________",
        "_________________________________________________",
        "",
        "What's another way to see this situation?",
        "_________________________________________________",
        "_________________________________________________",
        "",
        "What would my best friend say to me right now?",
        "_________________________________________________",
        "",
        "Will this matter in 1 week? 1 month? 1 year?",
        "1 week: _________ 1 month: _________ 1 year: _________",
        "",
        "What's a more balanced thought I can replace the hot thought with?",
        "_________________________________________________",
        "_________________________________________________",
        "",
        "What's the SMART move here (not the anger move)?",
        "_________________________________________________",
        "",
        "Anger level BEFORE this exercise: ___/10",
        "Anger level AFTER this exercise: ___/10",
    ]
    for p in prompts:
        pdf.add_text(50, y, p, 'F4', 10)
        y -= 16

# Page 13: Assertive vs Aggressive Communication
pdf.new_page()
pdf.add_centered_text(750, "ASSERTIVE vs AGGRESSIVE", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
comm_text = [
    "AGGRESSIVE = Getting your way by intimidation, yelling, threatening",
    "  Result: People fear you, avoid you, don't trust you",
    "",
    "PASSIVE = Saying nothing, bottling it up, people-pleasing",
    "  Result: Resentment builds, eventually explodes 10x worse",
    "",
    "ASSERTIVE = Saying what you need clearly, calmly, respectfully",
    "  Result: People respect you, problems get solved, you feel empowered",
    "",
    "THE ASSERTIVE FORMULA FOR TEENS:",
    "  'I feel [emotion] when [specific thing happens]",
    "   because [why it matters to me].",
    "   What I need is [specific request].'",
    "",
    "EXAMPLES:",
    "Instead of: 'GET OUT OF MY ROOM OR I'LL BREAK YOUR STUFF!'",
    "Try: 'I feel frustrated when you come in without knocking because",
    "I need privacy. Can you please knock first?'",
    "",
    "Instead of: 'You're the WORST teacher. This class is stupid.'",
    "Try: 'I'm confused about this assignment. Can I get help",
    "understanding what you expect?'",
    "",
    "Instead of: (saying nothing and ghosting a friend who hurt you)",
    "Try: 'I felt hurt when you said that in front of everyone.",
    "Our friendship matters to me. Can we talk about it?'",
    "",
    "YOUR TURN - Rewrite an aggressive thing you've said recently:",
    "What I said: ___________________________________________",
    "Assertive version: _____________________________________",
    "____________________________________________________",
]
for line in comm_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Pages 14-18: Conflict Resolution Scripts (5 scenarios)
scenarios = [
    ("CONFLICT WITH A PARENT", [
        "The Setup: Your parent says something that feels unfair or controlling.",
        "",
        "STEP 1: DON'T RESPOND IN THE MOMENT",
        "Say: 'I need to think about this. Can we talk in 20 minutes?'",
        "(This is NOT disrespectful - it's mature.)",
        "",
        "STEP 2: COOL DOWN & FIGURE OUT WHAT YOU ACTUALLY NEED",
        "Under the anger, what do I want? More freedom? To feel trusted?",
        "My real need: ________________________________________",
        "",
        "STEP 3: START THE CONVO WITH UNDERSTANDING",
        "'I get that you [their concern]. I feel [your feeling] because",
        "[why]. Can we find a middle ground where [compromise]?'",
        "",
        "STEP 4: PROPOSE A SOLUTION",
        "My proposal: _________________________________________",
        "What I'm willing to give: ______________________________",
        "",
        "STEP 5: IF THEY SAY NO",
        "Stay calm. Ask: 'What would I need to do to earn this?'",
        "This shows maturity and they WILL notice.",
    ]),
    ("CONFLICT WITH A FRIEND", [
        "The Setup: A friend did something that pissed you off.",
        "",
        "STEP 1: CHECK YOUR ASSUMPTIONS",
        "Did they do it on purpose? Do I have the full story?",
        "What I assume: ________________________________________",
        "What might be true: ___________________________________",
        "",
        "STEP 2: CHOOSE THE RIGHT TIME",
        "Not over text. Not in front of others. In person, privately.",
        "",
        "STEP 3: USE THE FORMULA",
        "'Hey, I need to talk about something. When [thing happened],",
        "I felt [emotion]. I didn't want to just let it build up.'",
        "",
        "STEP 4: LISTEN TO THEIR SIDE",
        "They might apologize. They might explain. Let them talk.",
        "",
        "STEP 5: DECIDE WHAT YOU NEED",
        "Apology? Changed behavior? Or do you need to set a boundary?",
        "What I need from this convo: __________________________",
    ]),
    ("CONFLICT WITH A TEACHER", [
        "The Setup: A teacher is unfair, embarrasses you, or you disagree.",
        "",
        "RULE #1: Never escalate with a teacher publicly. You will lose.",
        "",
        "STEP 1: STAY QUIET IN THE MOMENT",
        "Breathe. You can address it later. Reacting now = consequences.",
        "",
        "STEP 2: TALK PRIVATELY AFTER CLASS",
        "'Can I talk to you for a minute? I felt [emotion] when [thing].",
        "I want to understand / I want to explain my perspective.'",
        "",
        "STEP 3: STAY RESPECTFUL EVEN IF THEY'RE WRONG",
        "Teachers are human. They make mistakes. Giving them grace =",
        "they'll give you grace back.",
        "",
        "STEP 4: IF IT DOESN'T RESOLVE",
        "Talk to a counselor, parent, or another trusted adult.",
        "Document what happened (date, time, what was said).",
        "",
        "STEP 5: WHAT I'LL DO NEXT TIME",
        "My plan: ____________________________________________",
    ]),
    ("CONFLICT WITH A SIBLING", [
        "The Setup: Your sibling is annoying, takes your stuff, starts drama.",
        "",
        "REALITY CHECK: You live together. You have to coexist.",
        "",
        "STEP 1: IS THIS WORTH MY ENERGY?",
        "Scale of 1-10, how much does this actually matter? ___",
        "If under 5: Let it go. Save your energy for real battles.",
        "",
        "STEP 2: SET A CLEAR BOUNDARY",
        "'Don't touch my [thing]. If you need to borrow something, ask.'",
        "Keep it simple. Don't lecture.",
        "",
        "STEP 3: DON'T TAKE THE BAIT",
        "Siblings know your buttons because they installed them.",
        "When they poke: grey rock (boring, short answers, walk away).",
        "",
        "STEP 4: INVOLVE PARENTS STRATEGICALLY",
        "Only for real issues. Tattling about everything = lose credibility.",
        "",
        "STEP 5: WHAT BOUNDARY WILL I SET?",
        "My boundary: ________________________________________",
        "Consequence if crossed: _______________________________",
    ]),
    ("CONFLICT ON SOCIAL MEDIA", [
        "The Setup: Someone posts about you, starts drama online, cyberbullying.",
        "",
        "RULE #1: NEVER respond in anger online. Screenshots last forever.",
        "",
        "STEP 1: PUT THE PHONE DOWN",
        "Literally set a timer: 1 hour. Do NOT respond for 1 hour.",
        "",
        "STEP 2: ASK YOURSELF",
        "Is this person worth my peace? ___",
        "Will responding make it better or worse? ___",
        "What do I actually gain by clapping back? ___",
        "",
        "STEP 3: YOUR OPTIONS",
        "a) Ignore completely (this drives them CRAZY)",
        "b) Block/mute (not weakness - it's power)",
        "c) Screenshot and report (if it's harassment)",
        "d) Talk to a trusted adult (if it's serious)",
        "",
        "STEP 4: NEVER DO THIS",
        "- Don't screenshot and share to 'expose' them",
        "- Don't get your friends to gang up on them",
        "- Don't make vague posts about them",
        "These ALL escalate and make YOU look bad.",
        "",
        "STEP 5: My plan for next online conflict:",
        "I will: ____________________________________________",
    ]),
]
for title_text, content in scenarios:
    pdf.new_page()
    pdf.add_centered_text(750, title_text, 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 715
    for line in content:
        pdf.add_text(50, y, line, 'F4', 10)
        y -= 16

# Page 19: Consequence Thinking Worksheet
pdf.new_page()
pdf.add_centered_text(750, "CONSEQUENCE THINKING", 'F2', 15)
pdf.add_centered_text(732, "Think it through BEFORE you act", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 700
pdf.add_text(50, y, "When anger takes over, we stop thinking about consequences.", 'F4', 10.5)
y -= 14
pdf.add_text(50, y, "Practice this BEFORE you're angry so it becomes automatic:", 'F4', 10.5)
y -= 25
for i in range(4):
    pdf.add_text(50, y, f"SITUATION {i+1}: ________________________________________", 'F2', 10)
    y -= 18
    pdf.add_text(50, y, "What I WANT to do (anger response): ________________________", 'F4', 10)
    y -= 16
    pdf.add_text(50, y, "Consequences in 5 MINUTES: ________________________________", 'F4', 10)
    y -= 16
    pdf.add_text(50, y, "Consequences in 5 DAYS: ___________________________________", 'F4', 10)
    y -= 16
    pdf.add_text(50, y, "Consequences in 5 MONTHS: _________________________________", 'F4', 10)
    y -= 16
    pdf.add_text(50, y, "Is it worth it?  YES / NO", 'F4', 10)
    y -= 16
    pdf.add_text(50, y, "SMART alternative action: __________________________________", 'F4', 10)
    y -= 28
    pdf.add_line(50, y+10, 562, y+10, 0.3, 0.7)
    y -= 8

# Pages 20-27: Weekly Anger Log (8 pages)
for week in range(1, 9):
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEKLY ANGER LOG - WEEK {week}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    for day in range(7):
        pdf.add_text(50, y, f"Day {day+1}  Date: ___/___/___", 'F2', 9)
        y -= 13
        pdf.add_text(50, y, "Trigger: _________________________ Level (1-5): ___", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Strategy used: __________________ Did it work? Y/N", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "What I'd do differently: _______________________________", 'F3', 8)
        y -= 16
        pdf.add_line(50, y+5, 562, y+5, 0.3, 0.7)
        y -= 8

# Page 28: My Anger Action Plan
pdf.new_page()
pdf.add_centered_text(750, "MY ANGER ACTION PLAN", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 710
plan_items = [
    "MY TOP 3 TRIGGERS:",
    "1. ___________________________________________________",
    "2. ___________________________________________________",
    "3. ___________________________________________________",
    "",
    "MY EARLY WARNING SIGN (the first one I notice):",
    "___________________________________________________",
    "",
    "MY GO-TO COOL-DOWN STRATEGIES:",
    "At school: _________________________________________",
    "At home: ___________________________________________",
    "Online: ____________________________________________",
    "",
    "MY ASSERTIVE PHRASE (memorize this):",
    "'I feel _________ when _________ because _________.",
    "What I need is _________.'",
    "",
    "MY SUPPORT PEOPLE:",
    "Person I can talk to: _______________________________",
    "Person I can text when I'm heated: ___________________",
    "",
    "WHEN I MESS UP (because I will sometimes):",
    "1. Don't beat myself up - I'm learning",
    "2. Apologize if I hurt someone (no excuses, just sorry)",
    "3. Figure out what went wrong",
    "4. Try again tomorrow",
    "",
    "MY GOAL: I want to get to the point where I can:",
    "___________________________________________________",
]
for line in plan_items:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 17

# Page 29: Letter of Apology Template
pdf.new_page()
pdf.add_centered_text(750, "LETTER OF APOLOGY TEMPLATE", 'F2', 15)
pdf.add_centered_text(732, "For when you mess up (we all do)", 'F1', 10)
pdf.add_line(50, 722, 562, 722)
y = 695
pdf.add_text(50, y, "A REAL apology has 5 parts:", 'F2', 11)
y -= 22
parts = [
    "1. NAME what you did (no minimizing)",
    "   'I [specific thing I did]...'",
    "",
    "2. ACKNOWLEDGE how it affected them",
    "   'I know that made you feel [emotion]...'",
    "",
    "3. TAKE RESPONSIBILITY (no 'but')",
    "   'That was wrong of me. There's no excuse.'",
    "",
    "4. SAY WHAT YOU'LL DO DIFFERENTLY",
    "   'Next time, I will [specific different action]...'",
    "",
    "5. ASK if there's anything else they need",
    "   'Is there anything else I can do to make this right?'",
]
for p in parts:
    pdf.add_text(50, y, p, 'F4', 10.5)
    y -= 16
y -= 15
pdf.add_text(50, y, "MY APOLOGY (draft it here first):", 'F2', 11)
y -= 20
for i in range(10):
    pdf.add_line(50, y, 560, y, 0.5, 0.5)
    y -= 18
y -= 10
pdf.add_text(50, y, "Remember: An apology without changed behavior is just manipulation.", 'F5', 10)

# Page 30: Final Page
pdf.new_page()
pdf.add_centered_text(750, "YOU'VE GOT THIS", 'F2', 16)
pdf.add_line(50, 738, 562, 738)
y = 700
final_lines = [
    "The fact that you're reading this workbook means you WANT to change.",
    "That takes guts. Most people just keep exploding and blaming everyone else.",
    "",
    "Remember:",
    "- Anger is normal. How you handle it is what matters.",
    "- Every time you choose a strategy over a blowup, you're rewiring your brain.",
    "- Progress isn't perfect. It's doing better more often than not.",
    "- You deserve relationships where people feel safe around you.",
    "- You deserve to feel in control of yourself.",
    "",
    "If you need more help:",
    "- Talk to a school counselor (it's free and confidential)",
    "- 988 Suicide & Crisis Lifeline (call or text 988)",
    "- Crisis Text Line (text HOME to 741741)",
    "- Ask a parent/guardian about therapy (it's not just for 'crazy' people)",
    "",
    "",
    "You are not your worst moment.",
    "You are the person choosing to do better.",
]
for line in final_lines:
    pdf.add_text(50, y, line, 'F4', 11)
    y -= 18

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book156_Anger_Management_Teens.pdf')
print("Book156_Anger_Management_Teens.pdf created successfully!")
