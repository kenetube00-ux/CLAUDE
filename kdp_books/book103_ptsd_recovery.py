from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, "PTSD RECOVERY WORKBOOK", 'F2', 20)
pdf.add_centered_text(515, "Reclaim Your Life After Trauma", 'F4', 14)
pdf.add_centered_text(400, "Evidence-Based Exercises for Healing,", 'F4', 12)
pdf.add_centered_text(382, "Understanding, and Moving Forward", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, "PTSD RECOVERY WORKBOOK", 'F2', 12)
pdf.add_centered_text(575, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)
pdf.add_centered_text(550, "This workbook is not a substitute for professional treatment.", 'F4', 9)
pdf.add_centered_text(535, "If you are in crisis, call 988 or go to your nearest ER.", 'F4', 9)

# Page 3: Understanding PTSD
pdf.new_page()
pdf.add_centered_text(750, "UNDERSTANDING PTSD", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
lines = [
    "Post-Traumatic Stress Disorder (PTSD) is a normal response to abnormal events.",
    "It is NOT a sign of weakness. It means your brain is trying to protect you.",
    "",
    "WHAT CAUSES PTSD:",
    "- Combat/military service        - Physical or sexual assault",
    "- Childhood abuse or neglect     - Natural disasters",
    "- Serious accidents              - Witnessing violence",
    "- Medical trauma                 - Sudden loss of loved one",
    "",
    "PTSD SYMPTOMS (you don't need all of them):",
    "",
    "RE-EXPERIENCING: Flashbacks, nightmares, intrusive memories, emotional",
    "reactions to triggers that remind you of the trauma.",
    "",
    "AVOIDANCE: Avoiding places, people, activities, thoughts, or feelings",
    "associated with the trauma. Emotional numbness.",
    "",
    "HYPERAROUSAL: Being on edge, easily startled, difficulty sleeping,",
    "irritability, difficulty concentrating, hypervigilance.",
    "",
    "NEGATIVE CHANGES IN THOUGHTS/MOOD: Negative beliefs about self/world,",
    "blame, diminished interest, feeling detached, inability to feel positive.",
    "",
    "IMPORTANT: PTSD is TREATABLE. Recovery is possible at any stage.",
    "Effective treatments include CPT, PE, EMDR, and medication."
]
for line in lines:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 4: Trauma Response Types
pdf.new_page()
pdf.add_centered_text(750, "TRAUMA RESPONSE TYPES", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
responses = [
    "Your body has 4 survival responses. Understanding yours helps healing.",
    "",
    "FIGHT RESPONSE:",
    "- Anger, rage, desire to control",
    "- Difficulty letting things go, argumentative",
    "- Tight jaw, clenched fists, confrontational",
    "- May look like: aggression, bullying, perfectionism",
    "",
    "FLIGHT RESPONSE:",
    "- Anxiety, restlessness, panic",
    "- Overworking, over-exercising, staying busy",
    "- Can't sit still, always planning escape routes",
    "- May look like: workaholism, perfectionism, rushing",
    "",
    "FREEZE RESPONSE:",
    "- Numbness, dissociation, 'spacing out'",
    "- Difficulty making decisions, feeling stuck",
    "- Brain fog, feeling disconnected from body",
    "- May look like: depression, isolation, zoning out",
    "",
    "FAWN RESPONSE:",
    "- People-pleasing, inability to say no",
    "- Putting others' needs above your own always",
    "- Losing sense of self, over-apologizing",
    "- May look like: codependency, no boundaries",
    "",
    "MY PRIMARY RESPONSE(S): _________________________",
    "How this shows up in my daily life: ______________"
]
for line in responses:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 5: Safety Plan
pdf.new_page()
pdf.add_centered_text(750, "MY SAFETY PLAN", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
safety = [
    "Complete this plan NOW, while you are feeling stable.",
    "Keep it accessible for crisis moments.",
    "",
    "WARNING SIGNS that a crisis is developing:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "",
    "COPING STRATEGIES I can do alone:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "",
    "PEOPLE I can call for support:",
    "Name: _________________ Phone: ________________",
    "Name: _________________ Phone: ________________",
    "",
    "SAFE PLACES I can go:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "",
    "PROFESSIONAL CONTACTS:",
    "Therapist: _________________ Phone: ____________",
    "Psychiatrist: _______________ Phone: ____________",
    "Crisis line: 988 (Suicide & Crisis Lifeline)",
    "Crisis text: Text HOME to 741741",
    "Emergency: 911",
    "",
    "THINGS WORTH LIVING FOR (list at least 5):",
    "1. _____________ 2. _____________ 3. _____________",
    "4. _____________ 5. _____________"
]
for line in safety:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 6: Grounding Techniques
pdf.new_page()
pdf.add_centered_text(750, "GROUNDING TECHNIQUES", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
grounding = [
    "Grounding brings you back to the PRESENT when triggered.",
    "",
    "TECHNIQUE 1: 5-4-3-2-1 (Sensory Grounding)",
    "Name 5 things you can SEE: ____________________",
    "Name 4 things you can TOUCH: __________________",
    "Name 3 things you can HEAR: ___________________",
    "Name 2 things you can SMELL: __________________",
    "Name 1 thing you can TASTE: ___________________",
    "",
    "TECHNIQUE 2: Body Scan",
    "Starting at your feet, slowly notice each body part.",
    "Feet on the floor. Legs supported by the chair.",
    "Hands in your lap. Shoulders dropping. Jaw unclenching.",
    "Say: 'I am here. I am safe. This is now, not then.'",
    "",
    "TECHNIQUE 3: Safe Place Visualization",
    "Close your eyes. Imagine a place where you feel completely safe.",
    "My safe place is: _____________________________",
    "What I see there: _____________________________",
    "What I hear there: _____________________________",
    "What I feel there: _____________________________",
    "What makes it safe: ____________________________",
    "",
    "TECHNIQUE 4: Temperature Change",
    "Hold ice cubes, splash cold water on face, or drink cold water.",
    "This activates the dive reflex and calms your nervous system.",
    "",
    "TECHNIQUE 5: Mental Games",
    "Count backward from 100 by 7s. Name all 50 states.",
    "List every color you can think of. Spell your name backward."
]
for line in grounding:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 7: Trigger Identification
pdf.new_page()
pdf.add_centered_text(750, "TRIGGER IDENTIFICATION WORKSHEET", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
triggers = [
    "Triggers are reminders of trauma. They can be obvious or subtle.",
    "Identifying them gives you power to prepare and respond.",
    "",
    "SENSORY TRIGGERS:",
    "Sounds: _______________________________________",
    "Smells: _______________________________________",
    "Sights: _______________________________________",
    "Touch/physical sensations: _____________________",
    "Tastes: _______________________________________",
    "",
    "SITUATIONAL TRIGGERS:",
    "Places: _______________________________________",
    "Times of day/year: _____________________________",
    "People/relationship types: _____________________",
    "Activities: ____________________________________",
    "",
    "EMOTIONAL TRIGGERS:",
    "Feeling helpless: _____________________________",
    "Feeling trapped: ______________________________",
    "Feeling out of control: ________________________",
    "",
    "INTERNAL TRIGGERS:",
    "Physical pain: ________________________________",
    "Fatigue: ______________________________________",
    "Hunger: _______________________________________",
    "",
    "MY TOP 5 TRIGGERS & MY PLAN FOR EACH:",
    "1. Trigger: _____________ Plan: _______________",
    "2. Trigger: _____________ Plan: _______________",
    "3. Trigger: _____________ Plan: _______________",
    "4. Trigger: _____________ Plan: _______________",
    "5. Trigger: _____________ Plan: _______________"
]
for line in triggers:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 8: Window of Tolerance
pdf.new_page()
pdf.add_centered_text(750, "WINDOW OF TOLERANCE", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
window = [
    "The 'Window of Tolerance' is the zone where you can function well.",
    "",
    "HYPERAROUSAL (above the window):",
    "- Anxiety, panic, rage, hypervigilance",
    "- Racing thoughts, inability to rest",
    "- Fight or flight mode activated",
    "",
    "---- WINDOW OF TOLERANCE (ideal zone) ----",
    "- Calm but alert, able to think clearly",
    "- Can manage emotions, connect with others",
    "- Feel present and grounded",
    "",
    "HYPOAROUSAL (below the window):",
    "- Numbness, disconnection, depression",
    "- Foggy thinking, flat emotions",
    "- Freeze or collapse mode activated",
    "",
    "EXPANDING YOUR WINDOW:",
    "The goal is to WIDEN your window of tolerance over time.",
    "Practices that expand the window:",
    "- Regular grounding exercises",
    "- Mindfulness meditation (start with 2 minutes)",
    "- Safe physical movement (yoga, walking)",
    "- Therapy (especially EMDR, Somatic Experiencing)",
    "- Social connection with safe people",
    "- Consistent sleep schedule",
    "",
    "Right now, my window feels: Narrow / Medium / Wide",
    "I tend to go: Above / Below / Both directions"
]
for line in window:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 9: Coping Strategies Menu
pdf.new_page()
pdf.add_centered_text(750, "COPING STRATEGIES MENU", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
coping = [
    "Choose strategies from each category. Star your favorites.",
    "",
    "PHYSICAL (body-based):",
    "__ Deep breathing (box breathing: 4-4-4-4)",
    "__ Progressive muscle relaxation",
    "__ Walk or exercise",
    "__ Cold water on face/wrists",
    "__ Yoga or stretching",
    "__ Dance or movement",
    "",
    "COGNITIVE (thought-based):",
    "__ Challenge catastrophic thoughts",
    "__ Remind yourself: 'That was THEN, this is NOW'",
    "__ Use a coping statement card",
    "__ Journaling",
    "__ List facts about the present moment",
    "",
    "SENSORY (using your senses):",
    "__ Essential oils or scented candle",
    "__ Weighted blanket",
    "__ Music playlist (calming or energizing)",
    "__ Tactile objects (smooth stone, fidget)",
    "__ Nature sounds or being in nature",
    "",
    "SOCIAL (connection-based):",
    "__ Call a safe person",
    "__ Go somewhere with people (coffee shop, park)",
    "__ Support group (in-person or online)",
    "__ Pet an animal",
    "__ Help someone else"
]
for line in coping:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 10: Cognitive Processing (Stuck Points)
pdf.new_page()
pdf.add_centered_text(750, "STUCK POINTS WORKSHEET", 'F2', 16)
pdf.add_centered_text(733, "From Cognitive Processing Therapy", 'F1', 10)
pdf.add_line(60, 725, 552, 725)
y = 705
stuck = [
    "Stuck points are unhelpful beliefs that developed after trauma.",
    "They keep you stuck in pain. Identifying them is step one.",
    "",
    "COMMON STUCK POINTS ABOUT SAFETY:",
    "'I can never be safe.'  'The world is completely dangerous.'",
    "",
    "ABOUT TRUST:",
    "'I can never trust anyone.'  'Everyone will betray me.'",
    "",
    "ABOUT POWER/CONTROL:",
    "'I am helpless.'  'I should have been able to stop it.'",
    "",
    "ABOUT ESTEEM:",
    "'I am damaged.'  'I am worthless because of what happened.'",
    "",
    "ABOUT INTIMACY:",
    "'I can never be close to anyone.'  'No one could love me.'",
    "",
    "MY STUCK POINTS:",
    "1. ____________________________________________",
    "   Evidence FOR this belief: ___________________",
    "   Evidence AGAINST this belief: _______________",
    "   More balanced thought: ______________________",
    "",
    "2. ____________________________________________",
    "   Evidence FOR: ______________________________",
    "   Evidence AGAINST: ___________________________",
    "   More balanced thought: ______________________"
]
for line in stuck:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 11: Self-Compassion Exercises
pdf.new_page()
pdf.add_centered_text(750, "SELF-COMPASSION EXERCISES", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
compassion = [
    "Trauma survivors often blame themselves. Self-compassion heals.",
    "",
    "EXERCISE 1: What Would You Tell a Friend?",
    "If your best friend went through what you did, would you tell",
    "them it was their fault? Would you call them weak? No.",
    "Write what you WOULD say to them: ______________",
    "_______________________________________________",
    "Now say those same words to YOURSELF.",
    "",
    "EXERCISE 2: Self-Compassion Break",
    "When pain arises, say these 3 phrases:",
    "1. 'This is a moment of suffering.' (mindfulness)",
    "2. 'Suffering is part of being human.' (common humanity)",
    "3. 'May I be kind to myself.' (self-kindness)",
    "",
    "EXERCISE 3: Compassionate Letter to Yourself",
    "Write to yourself from the perspective of a loving friend",
    "who knows everything about your trauma and sees you with",
    "unconditional compassion. What would they say?",
    "_______________________________________________",
    "_______________________________________________",
    "_______________________________________________",
    "",
    "EXERCISE 4: Daily Self-Compassion Practice",
    "Each night, place your hand on your heart and say:",
    "'I did the best I could today. That is enough.'"
]
for line in compassion:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 12: Sleep Hygiene for PTSD
pdf.new_page()
pdf.add_centered_text(750, "SLEEP HYGIENE FOR PTSD", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
sleep = [
    "Sleep disruption is one of the most common PTSD symptoms.",
    "Better sleep does not fix PTSD, but it makes everything easier.",
    "",
    "NIGHTTIME ROUTINE (do the same thing every night):",
    "__ Set consistent bedtime: ___:___ PM",
    "__ Set consistent wake time: ___:___ AM",
    "__ Stop screens 1 hour before bed",
    "__ Dim lights in the evening",
    "__ Do calming activity: reading, gentle stretching, bath",
    "__ Keep bedroom cool (65-68 degrees)",
    "__ Use white noise or fan if needed",
    "",
    "FOR NIGHTMARES:",
    "- Practice Image Rehearsal Therapy: while awake, choose a",
    "  recurring nightmare and rewrite the ending to something safe.",
    "  Rehearse the new version 10-20 min daily for 2 weeks.",
    "- Keep a dim nightlight if total darkness is triggering",
    "- Have grounding objects by your bed (smooth stone, familiar scent)",
    "- Upon waking from nightmare: orient to the room, name 5 objects,",
    "  remind yourself 'I am safe. That was then, this is now.'",
    "",
    "FOR HYPERVIGILANCE AT NIGHT:",
    "- Check locks ONCE (not repeatedly)",
    "- Consider a security camera if it helps (check once only)",
    "- Place bed where you can see the door",
    "- Reassure yourself: 'I have done what I can. I am safe.'"
]
for line in sleep:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 13: Flashback Protocol
pdf.new_page()
pdf.add_centered_text(750, "FLASHBACK PROTOCOL", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
flash = [
    "A flashback makes the past feel like it's happening NOW.",
    "Use this protocol to come back to the present:",
    "",
    "STEP 1: RECOGNIZE what is happening",
    "Say out loud: 'I am having a flashback. This is a memory.",
    "It is not happening right now. I am safe.'",
    "",
    "STEP 2: GROUND yourself in the present",
    "- Stamp your feet. Feel the floor.",
    "- Look around. Name the room you are in.",
    "- What year is it? What day? What time?",
    "- Touch something real: table, wall, your own arms.",
    "",
    "STEP 3: BREATHE slowly",
    "- Breathe in for 4 counts",
    "- Hold for 4 counts",
    "- Breathe out for 6 counts",
    "- Repeat until heart rate slows",
    "",
    "STEP 4: COMFORT yourself",
    "- Wrap yourself in a blanket",
    "- Hold a warm drink",
    "- Put on familiar, safe music",
    "- Call a safe person if needed",
    "",
    "STEP 5: RETURN to activity slowly",
    "- Don't rush. Take your time.",
    "- Drink water. Eat something small.",
    "- You survived. You came back. You are strong."
]
for line in flash:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 14: Support Network Map
pdf.new_page()
pdf.add_centered_text(750, "MY SUPPORT NETWORK MAP", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
network = [
    "Recovery happens in relationship. Build your support network.",
    "",
    "INNER CIRCLE (closest, most trusted):",
    "1. Name: _____________ Relationship: ___________",
    "   How they help me: ___________________________",
    "2. Name: _____________ Relationship: ___________",
    "   How they help me: ___________________________",
    "",
    "MIDDLE CIRCLE (supportive, reliable):",
    "1. Name: _____________ Relationship: ___________",
    "2. Name: _____________ Relationship: ___________",
    "3. Name: _____________ Relationship: ___________",
    "",
    "PROFESSIONAL SUPPORT:",
    "Therapist: ____________________________________",
    "Psychiatrist: __________________________________",
    "Support group: _________________________________",
    "Doctor: ________________________________________",
    "",
    "COMMUNITY RESOURCES:",
    "Crisis line: 988",
    "Veterans crisis: 1-800-273-8255 (Press 1)",
    "RAINN hotline: 1-800-656-4673",
    "Local support group: ___________________________",
    "",
    "PEOPLE TO AVOID DURING RECOVERY:",
    "(Those who minimize, blame, or trigger you)",
    "_______________________________________________"
]
for line in network:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Pages 15-18: Weekly Symptom Tracker (4 pages)
for week in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEKLY SYMPTOM TRACKER - WEEK {week}", 'F2', 14)
    pdf.add_line(60, 738, 552, 738)
    y = 720
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    pdf.add_text(60, y, "Rate 0-10:  0=none  5=moderate  10=severe", 'F3', 8)
    y -= 15
    headers = "Day   Flashbacks  Nightmares  Anxiety  Avoidance  Mood"
    pdf.add_text(60, y, headers, 'F2', 9)
    y -= 5
    pdf.add_line(60, y, 550, y, 0.5)
    y -= 15
    for day in days:
        pdf.add_text(60, y, f"{day}   ___/10      ___/10     ___/10   ___/10    ___/10", 'F3', 9)
        y -= 18
    y -= 10
    pdf.add_text(60, y, "Triggers this week:", 'F2', 9)
    y -= 15
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 18
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 18
    pdf.add_text(60, y, "Coping strategies used:", 'F2', 9)
    y -= 15
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 18
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 18
    pdf.add_text(60, y, "Wins this week (no matter how small):", 'F2', 9)
    y -= 15
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 18
    pdf.add_line(60, y, 550, y, 0.5, 0.5)


# Page 19: Recovery Milestones
pdf.new_page()
pdf.add_centered_text(750, "RECOVERY MILESTONES", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
milestones = [
    "Recovery is not linear. Celebrate every step forward.",
    "Check off milestones as you reach them:",
    "",
    "__ I acknowledged that what happened was not my fault",
    "__ I told someone safe about my trauma",
    "__ I identified my triggers",
    "__ I used a grounding technique successfully",
    "__ I slept through the night",
    "__ I went somewhere I was avoiding",
    "__ I felt a positive emotion (joy, peace, love)",
    "__ I set a boundary with someone",
    "__ I asked for help",
    "__ I went a full day without intrusive memories",
    "__ I felt safe in my body",
    "__ I trusted someone new",
    "__ I forgave myself for something",
    "__ I found meaning or purpose in my experience",
    "__ I helped another trauma survivor",
    "",
    "MY PERSONAL MILESTONES:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "",
    "Date I started this workbook: __________________",
    "Where I was then: _____________________________",
    "Where I am now: _______________________________"
]
for line in milestones:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 20: Professional Resources
pdf.new_page()
pdf.add_centered_text(750, "PROFESSIONAL RESOURCES", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
resources = [
    "This workbook is a supplement, not a replacement for therapy.",
    "Here are evidence-based treatments for PTSD:",
    "",
    "RECOMMENDED THERAPIES:",
    "- Cognitive Processing Therapy (CPT): Challenges stuck points",
    "- Prolonged Exposure (PE): Gradually facing avoided memories",
    "- EMDR: Eye Movement Desensitization and Reprocessing",
    "- Somatic Experiencing: Body-based trauma processing",
    "- DBT: Dialectical Behavior Therapy (skills for regulation)",
    "",
    "HOW TO FIND A THERAPIST:",
    "- Psychology Today therapist directory (filter by 'trauma')",
    "- EMDR International Association directory",
    "- VA mental health services (veterans)",
    "- Ask your primary care doctor for a referral",
    "",
    "CRISIS RESOURCES:",
    "- 988 Suicide & Crisis Lifeline (call or text 988)",
    "- Crisis Text Line: Text HOME to 741741",
    "- Veterans Crisis Line: 1-800-273-8255 (Press 1)",
    "- RAINN (sexual assault): 1-800-656-4673",
    "- National DV Hotline: 1-800-799-7233",
    "",
    "BOOKS RECOMMENDED:",
    "- 'The Body Keeps the Score' by Bessel van der Kolk",
    "- 'Complex PTSD: From Surviving to Thriving' by Pete Walker",
    "- 'Waking the Tiger' by Peter Levine",
    "",
    "You deserve healing. You deserve peace. Keep going."
]
for line in resources:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book103_PTSD_Recovery_Workbook.pdf')
print("Book103_PTSD_Recovery_Workbook.pdf created successfully!")
