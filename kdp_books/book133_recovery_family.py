from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "WHEN SOMEONE YOU LOVE IS ADDICTED"
subtitle = "A Workbook for Families"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, title, 'F2', 13)
pdf.add_centered_text(455, subtitle, 'F4', 12)
pdf.add_centered_text(380, "Boundaries, Self-Care, and Healing", 'F4', 10)
pdf.add_centered_text(365, "for Those Who Love an Addict", 'F4', 10)
pdf.add_centered_text(230, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, title, 'F2', 10)
pdf.add_centered_text(470, f"Copyright 2025 {author}", 'F4', 9)
pdf.add_centered_text(455, "All rights reserved.", 'F4', 9)
pdf.add_centered_text(425, "This workbook is not a substitute for professional counseling.", 'F4', 8)
pdf.add_centered_text(410, "If you are in crisis, call 988 or Al-Anon: 1-888-425-2666", 'F4', 8)

# Page 3: Understanding Addiction as a Family Disease
pdf.new_page()
pdf.add_centered_text(610, "ADDICTION IS A FAMILY DISEASE", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
lines = [
    "When one person is addicted, EVERYONE in the family is affected.",
    "You did not cause this. You cannot control it. You cannot cure it.",
    "But you CAN heal from its effects on YOUR life.",
    "",
    "HOW ADDICTION AFFECTS FAMILIES:",
    "- Constant worry, fear, and hypervigilance",
    "- Walking on eggshells to avoid conflict",
    "- Financial strain from enabling or consequences",
    "- Broken trust and repeated disappointments",
    "- Isolation (shame keeps you from telling others)",
    "- Loss of identity (your life revolves around them)",
    "- Physical symptoms: insomnia, headaches, stomach issues",
    "- Children in the home absorb the chaos",
    "",
    "COMMON FAMILY ROLES:",
    "- The Enabler: protects the addict from consequences",
    "- The Hero: tries to make everything look perfect",
    "- The Scapegoat: acts out to divert attention",
    "- The Lost Child: withdraws and becomes invisible",
    "- The Mascot: uses humor to diffuse tension",
    "",
    "Which role(s) do I play? _____________________________________",
    "",
    "THIS WORKBOOK WILL HELP YOU:",
    "1. Understand what you CAN and CANNOT control",
    "2. Set boundaries that protect your well-being",
    "3. Practice detachment with love",
    "4. Build your own support system",
    "5. Begin your own healing journey"
]
for line in lines:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 4: The 3 Cs
pdf.new_page()
pdf.add_centered_text(610, "THE 3 Cs", 'F2', 14)
pdf.add_line(40, 600, 392, 600)
y = 580
three_cs = [
    "The foundation of Al-Anon and family recovery:",
    "",
    "I did not CAUSE it.",
    "  - Addiction is a brain disease, not a moral failing",
    "  - Nothing you did or did not do made them addicted",
    "  - You are not responsible for their choices",
    "  - Let go of guilt for 'what I should have done differently'",
    "",
    "  What I need to stop blaming myself for:",
    "  ____________________________________________________________",
    "  ____________________________________________________________",
    "",
    "I cannot CONTROL it.",
    "  - You cannot love someone into sobriety",
    "  - Begging, threatening, and bargaining do not work long-term",
    "  - Their recovery is THEIR responsibility",
    "  - You are powerless over another person's choices",
    "",
    "  What I have been trying to control that is not mine to control:",
    "  ____________________________________________________________",
    "  ____________________________________________________________",
    "",
    "I cannot CURE it.",
    "  - There is no magic thing you can say or do",
    "  - Recovery is a personal journey they must choose",
    "  - You can support without taking responsibility",
    "  - Your job is to heal YOURSELF",
    "",
    "  What I need to accept I am powerless over:",
    "  ____________________________________________________________",
    "  ____________________________________________________________"
]
for line in three_cs:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 5: Codependency Self-Assessment
pdf.new_page()
pdf.add_centered_text(610, "CODEPENDENCY SELF-ASSESSMENT", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Check all that apply to you. Be honest - this is for YOUR awareness.", 'F4', 8)
y -= 14
questions = [
    "I feel responsible for other people's feelings and actions",
    "I have difficulty saying 'no' even when I want to",
    "I put others' needs before my own consistently",
    "I try to fix, manage, or control other people's problems",
    "I feel guilty when I do something for myself",
    "I stay in relationships that are harmful to me",
    "I need external approval to feel good about myself",
    "I am afraid of being abandoned or alone",
    "I confuse love with pity or rescuing",
    "I tolerate behavior from others that I would not accept from myself",
    "I have difficulty identifying my own feelings",
    "I am more aware of others' feelings than my own",
    "I feel anxious when I am not needed",
    "I make excuses for my loved one's addiction",
    "I lie to cover up the addict's behavior",
    "I check their phone, belongings, or whereabouts obsessively",
    "I have lost friendships because of this situation",
    "I have neglected my own health, hobbies, or goals",
    "I feel crazy, exhausted, or hopeless most days",
    "I believe if I just love them enough, they will change"
]
for q in questions:
    pdf.add_rect(45, y - 2, 8, 8, 0.4)
    pdf.add_text(57, y, q, 'F4', 7)
    y -= 12
y -= 8
pdf.add_text(40, y, "Total checked: ___/20", 'F2', 8)
y -= 12
pdf.add_text(40, y, "0-5: Minimal codependency  6-10: Moderate  11-15: Significant  16+: Severe", 'F4', 7)
y -= 12
pdf.add_text(40, y, "Remember: This is not a diagnosis. It is awareness. Healing starts here.", 'F4', 7)

# Page 6: Enabling vs Helping Worksheet
pdf.new_page()
pdf.add_centered_text(610, "ENABLING vs HELPING", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
enabling = [
    "ENABLING removes consequences. HELPING supports recovery.",
    "",
    "ENABLING looks like:              HELPING looks like:",
    "- Paying their bills/rent         - Letting them face consequences",
    "- Lying to cover for them         - Being honest with others",
    "- Giving money (used for drugs)   - Offering to pay for treatment",
    "- Bailing them out of jail        - Providing information on resources",
    "- Making excuses to employer      - Expressing concern with boundaries",
    "- Cleaning up their messes        - Attending your own recovery meetings",
    "- Ignoring the problem            - Naming the problem honestly",
    "",
    "MY ENABLING BEHAVIORS (be specific and honest):",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "3. ____________________________________________________________",
    "4. ____________________________________________________________",
    "5. ____________________________________________________________",
    "",
    "WHY I ENABLE (what am I afraid will happen if I stop?):",
    "____________________________________________________________",
    "____________________________________________________________",
    "",
    "ONE ENABLING BEHAVIOR I COMMIT TO STOPPING THIS WEEK:",
    "____________________________________________________________",
    "What might happen: ___________________________________________",
    "How I will cope: _____________________________________________"
]
for line in enabling:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Pages 7-11: Boundary Setting Exercises (5 pages)
boundary_situations = [
    "money/finances",
    "their behavior when using/drinking",
    "their presence around children",
    "communication (lies, manipulation, yelling)",
    "my home and personal space"
]
for b_page, situation in enumerate(boundary_situations, 1):
    pdf.new_page()
    pdf.add_centered_text(610, f"BOUNDARY SETTING - EXERCISE {b_page}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    pdf.add_text(40, y, f"Focus area: {situation.upper()}", 'F2', 9)
    y -= 18
    boundary_fields = [
        "THE SITUATION (what keeps happening):",
        "_______________________________________________________________",
        "_______________________________________________________________",
        "",
        "HOW IT AFFECTS ME (emotionally, physically, financially):",
        "_______________________________________________________________",
        "_______________________________________________________________",
        "",
        "MY BOUNDARY (what I will no longer accept):",
        "_______________________________________________________________",
        "_______________________________________________________________",
        "",
        "HOW I WILL COMMUNICATE IT (use calm, clear language):",
        "'I love you AND I need to tell you that ________________________",
        "_______________________________________________________________",
        "Going forward, I will ________________________________________",
        "If [boundary is crossed], I will _______________________________'",
        "",
        "WHAT IF THEY PUSH BACK? (they will - prepare for it):",
        "They might say: ______________________________________________",
        "My response: ________________________________________________",
        "They might do: _______________________________________________",
        "My response: ________________________________________________",
        "",
        "MY SUPPORT FOR HOLDING THIS BOUNDARY:",
        "Who I will call if I waver: ___________________________________",
        "What I will remind myself: ____________________________________",
        "",
        "DATE SET: ___/___/___  DID I HOLD IT?  [ ] Yes  [ ] No",
        "What happened: _______________________________________________",
        "What I learned: ______________________________________________"
    ]
    for line in boundary_fields:
        pdf.add_text(40, y, line, 'F4', 8)
        y -= 13

# Pages 12-21: Detachment with Love Daily Practice (10 pages)
for det_page in range(1, 11):
    pdf.new_page()
    pdf.add_centered_text(610, f"DETACHMENT WITH LOVE - PAGE {det_page}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    if det_page == 1:
        pdf.add_text(40, y, "Detachment is NOT abandonment. It means:", 'F4', 8)
        y -= 11
        pdf.add_text(40, y, "Loving them WITHOUT losing yourself in their disease.", 'F2', 8)
        y -= 16
    for entry in range(3):
        day_num = (det_page - 1) * 3 + entry + 1
        pdf.add_filled_rect(40, y - 3, 352, 145, 0.95)
        pdf.add_rect(40, y - 3, 352, 145, 0.5, 0.5)
        pdf.add_text(45, y + 128, f"DAY {day_num}   Date: ___/___/___", 'F2', 8)
        pdf.add_text(45, y + 112, "Situation that triggered me:", 'F1', 8)
        pdf.add_line(200, y + 110, 385, y + 110, 0.3, 0.5)
        pdf.add_line(45, y + 96, 385, y + 96, 0.3, 0.5)
        pdf.add_text(45, y + 80, "My reaction (what I did/felt):", 'F1', 8)
        pdf.add_line(200, y + 78, 385, y + 78, 0.3, 0.5)
        pdf.add_line(45, y + 64, 385, y + 64, 0.3, 0.5)
        pdf.add_text(45, y + 48, "Healthier response (what I could do instead):", 'F1', 8)
        pdf.add_line(275, y + 46, 385, y + 46, 0.3, 0.5)
        pdf.add_line(45, y + 32, 385, y + 32, 0.3, 0.5)
        pdf.add_text(45, y + 16, "Self-care I did today:", 'F1', 8)
        pdf.add_line(170, y + 14, 385, y + 14, 0.3, 0.5)
        pdf.add_text(45, y, "Mantra: 'I release what I cannot control.'", 'F5', 7)
        y -= 160

# Page 22: Al-Anon Meeting Log
pdf.new_page()
pdf.add_centered_text(610, "AL-ANON / SUPPORT MEETING LOG", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Regular meetings are essential for YOUR recovery. Track attendance:", 'F4', 8)
y -= 16
for meeting in range(12):
    pdf.add_filled_rect(40, y - 3, 352, 36, 0.95)
    pdf.add_rect(40, y - 3, 352, 36, 0.5, 0.5)
    pdf.add_text(45, y + 20, f"Meeting {meeting+1}  Date: ___/___/___  Group: ______________", 'F1', 7)
    pdf.add_text(45, y + 8, "Topic: ___________________________  My takeaway:", 'F1', 7)
    pdf.add_line(250, y + 6, 385, y + 6, 0.2, 0.5)
    pdf.add_line(45, y - 4, 385, y - 4, 0.2, 0.5)
    y -= 42

# Page 23: My Support Network Map
pdf.new_page()
pdf.add_centered_text(610, "MY SUPPORT NETWORK MAP", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
network = [
    "You cannot do this alone. Build your support team:",
    "",
    "INNER CIRCLE (people I can call anytime, who truly get it):",
    "1. Name: _________________ Phone: _________________",
    "2. Name: _________________ Phone: _________________",
    "3. Name: _________________ Phone: _________________",
    "",
    "PROFESSIONAL SUPPORT:",
    "Therapist/Counselor: _________________ Phone: _____________",
    "Al-Anon sponsor: ___________________ Phone: _______________",
    "Family group: ______________________ Meeting day: __________",
    "",
    "TRUSTED FRIENDS (who I can be honest with):",
    "1. ___________________________",
    "2. ___________________________",
    "3. ___________________________",
    "",
    "FAITH COMMUNITY (if applicable):",
    "Pastor/leader: _________________ Phone: ___________________",
    "",
    "CRISIS RESOURCES:",
    "Al-Anon: 1-888-425-2666 (Meeting finder: al-anon.org)",
    "Nar-Anon: nar-anon.org",
    "SAMHSA Helpline: 1-800-662-4357 (free, 24/7)",
    "Crisis line: 988",
    "",
    "WHAT I NEED FROM MY SUPPORT PEOPLE:",
    "- Someone to listen without fixing",
    "- Someone to tell me the truth lovingly",
    "- Someone to remind me of my boundaries",
    "- Someone to do fun things with (life beyond addiction)"
]
for line in network:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 24: Self-Care Plan
pdf.new_page()
pdf.add_centered_text(610, "MY SELF-CARE PLAN", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
selfcare = [
    "You cannot pour from an empty cup. You MATTER.",
    "Self-care is not selfish - it is survival.",
    "",
    "DAILY NON-NEGOTIABLES (do these every single day):",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "3. ____________________________________________________________",
    "",
    "WEEKLY SELF-CARE (schedule these like appointments):",
    "[ ] Exercise/movement: _________________________________________",
    "[ ] Social connection: _________________________________________",
    "[ ] Something just for me: _____________________________________",
    "[ ] Support group/therapy: _____________________________________",
    "",
    "THINGS THAT RECHARGE ME:",
    "1. ________________________  2. ________________________",
    "3. ________________________  4. ________________________",
    "",
    "THINGS I HAVE NEGLECTED (that I am reclaiming):",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "3. ____________________________________________________________",
    "",
    "MY SELF-CARE MANTRA:",
    "'_______________________________________________________________'",
    "",
    "WHEN I FEEL GUILTY ABOUT SELF-CARE, I WILL REMEMBER:",
    "- I deserve rest and joy regardless of what they are doing",
    "- Taking care of myself models health for everyone",
    "- I am a better support when I am not depleted"
]
for line in selfcare:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 25: Family Communication Scripts
pdf.new_page()
pdf.add_centered_text(610, "FAMILY COMMUNICATION SCRIPTS", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
scripts = [
    "WHEN THEY ARE USING/DRINKING:",
    "'I love you, and I am not going to be around you when you are",
    "using. I will be here when you are sober.'",
    "",
    "WHEN THEY ASK FOR MONEY:",
    "'I cannot give you money. I can help you find a treatment program",
    "if you are ready. That is what I am willing to offer.'",
    "",
    "WHEN THEY MAKE PROMISES:",
    "'I hear you saying you will change. I hope that is true. I have",
    "learned to pay attention to actions, not words. Show me.'",
    "",
    "WHEN FAMILY MEMBERS JUDGE YOU FOR SETTING BOUNDARIES:",
    "'I understand you see this differently. I have to do what keeps",
    "me healthy. I hope you can respect that.'",
    "",
    "WHEN TALKING TO CHILDREN ABOUT IT:",
    "'Mommy/Daddy has a sickness that makes them act differently.",
    "It is NOT your fault. You are loved and safe.'",
    "",
    "WHEN THEY HIT ROCK BOTTOM:",
    "'I love you. I have found some treatment options. Here they are.",
    "I cannot make you go, but I want you to know help is available",
    "whenever you are ready.'",
    "",
    "WHEN YOU ARE READY TO STATE YOUR BOUNDARY:",
    "'I love you. Because I love you AND myself, I need to tell you:",
    "[state boundary]. This is not a punishment. It is how I stay well.'",
    "",
    "Remember: Short. Calm. Consistent. You do not owe explanations."
]
for line in scripts:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 12

# Page 26: When to Seek Intervention
pdf.new_page()
pdf.add_centered_text(610, "WHEN TO SEEK INTERVENTION", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
intervention = [
    "An intervention is a structured conversation where loved ones",
    "express concern and present treatment options. Consider it when:",
    "",
    "[ ] Their addiction is life-threatening",
    "[ ] They refuse to acknowledge the problem",
    "[ ] Children are at risk",
    "[ ] Previous conversations have not worked",
    "[ ] You have support from a professional interventionist",
    "",
    "INTERVENTION PLANNING:",
    "Professional interventionist: _________________________________",
    "Phone: _______________________________________________________",
    "Treatment facility researched: ________________________________",
    "Insurance verified? [ ] Yes [ ] No  Coverage: _________________",
    "",
    "WHO WILL PARTICIPATE:",
    "1. ___________________________  Relationship: _________________",
    "2. ___________________________  Relationship: _________________",
    "3. ___________________________  Relationship: _________________",
    "4. ___________________________  Relationship: _________________",
    "",
    "WHAT IF THEY SAY NO:",
    "My consequence if they refuse treatment:",
    "____________________________________________________________",
    "Am I prepared to follow through?  [ ] Yes  [ ] Not yet",
    "",
    "IMPORTANT: Never attempt an intervention:",
    "- When the person is actively under the influence",
    "- Without professional guidance",
    "- If there is a risk of violence",
    "- If you are not prepared to follow through on consequences"
]
for line in intervention:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 27: Crisis Plan
pdf.new_page()
pdf.add_centered_text(610, "CRISIS PLAN", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
crisis = [
    "IF THERE IS IMMEDIATE DANGER: Call 911",
    "",
    "SIGNS OF OVERDOSE (call 911 immediately):",
    "- Blue lips or fingertips",
    "- Slow or stopped breathing",
    "- Cannot be woken up",
    "- Gurgling or choking sounds",
    "- Seizures",
    "",
    "IF I NEED TO LEAVE QUICKLY:",
    "Go-bag location: ___________________________________________",
    "Contents: [ ] ID  [ ] Cash  [ ] Phone charger  [ ] Medications",
    "          [ ] Important documents  [ ] Clothes for ___ days",
    "Safe place to go: __________________________________________",
    "Person who will take me in: _________________________________",
    "",
    "EMERGENCY NUMBERS:",
    "911 (always first if danger)",
    "Local crisis line: _________________________________________",
    "Domestic violence hotline: 1-800-799-7233",
    "SAMHSA: 1-800-662-4357",
    "My therapist emergency line: ________________________________",
    "My sponsor: ________________________________________________",
    "",
    "IF CHILDREN ARE INVOLVED:",
    "Who will take them: _________________________________________",
    "School contact: _____________________________________________",
    "What to tell them: 'We are going to stay with ___ tonight.",
    "You are safe. I love you. This is not your fault.'",
    "",
    "I WILL NOT: Stay in an unsafe situation out of guilt or love."
]
for line in crisis:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 28: Letter to My Loved One (Unsent)
pdf.new_page()
pdf.add_centered_text(610, "LETTER TO MY LOVED ONE (UNSENT)", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Write everything you need to say. You do not have to send this.", 'F4', 8)
y -= 12
pdf.add_text(40, y, "This is for YOUR healing.", 'F4', 8)
y -= 18
pdf.add_text(40, y, "Dear _______________,", 'F5', 9)
y -= 16
for _ in range(30):
    pdf.add_line(40, y, 392, y, 0.3, 0.5)
    y -= 14
y -= 5
pdf.add_text(40, y, "With love and boundaries,", 'F5', 8)
y -= 12
pdf.add_text(40, y, "_______________", 'F4', 8)

# Page 29: Progress Reflection
pdf.new_page()
pdf.add_centered_text(610, "PROGRESS REFLECTION", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
reflection = [
    "Look back at where you started. Acknowledge your growth.",
    "",
    "WHEN I STARTED THIS WORKBOOK, I FELT:",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "",
    "NOW I FEEL:",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "",
    "BOUNDARIES I HAVE SET AND MAINTAINED:",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "3. ____________________________________________________________",
    "",
    "ENABLING BEHAVIORS I HAVE STOPPED:",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "",
    "SELF-CARE PRACTICES I HAVE STARTED:",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "",
    "WHAT I AM MOST PROUD OF:",
    "_______________________________________________________________",
    "",
    "WHAT STILL NEEDS WORK:",
    "_______________________________________________________________",
    "",
    "MY NEXT STEP IN MY OWN RECOVERY:",
    "_______________________________________________________________",
    "",
    "REMINDER: Their recovery is their journey.",
    "YOUR recovery is YOUR journey. Keep going."
]
for line in reflection:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book133_Family_Recovery_Workbook.pdf')
print("Book133_Family_Recovery_Workbook.pdf created successfully!")
