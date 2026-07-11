from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1: Title Page
pdf.new_page()
pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
pdf.add_centered_text(530, "HEALING HER WAY", "F2", 28)
pdf.add_line(180, 515, 432, 515, 2, gray=0.5)
pdf.add_centered_text(470, "A PTSD Recovery Workbook", "F4", 18, gray=0.3)
pdf.add_centered_text(445, "for Women", "F4", 18, gray=0.3)
pdf.add_centered_text(390, "Trauma-Informed Tools for", "F1", 13, gray=0.4)
pdf.add_centered_text(368, "Safety, Healing & Reclamation", "F1", 13, gray=0.4)
pdf.add_centered_text(200, author, "F2", 14)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, "HEALING HER WAY", "F2", 14)
pdf.add_centered_text(480, "A PTSD Recovery Workbook for Women", "F4", 12)
pdf.add_centered_text(440, f"Copyright (c) 2025 {author}", "F1", 11)
pdf.add_centered_text(420, "All rights reserved.", "F1", 11)
pdf.add_centered_text(380, "IMPORTANT: This workbook is a supplement to professional treatment,", "F1", 10)
pdf.add_centered_text(365, "not a replacement. If you are in crisis, please reach out:", "F1", 10)
pdf.add_centered_text(340, "RAINN: 1-800-656-4673 | National DV Hotline: 1-800-799-7233", "F2", 10)
pdf.add_centered_text(320, "988 Suicide & Crisis Lifeline: Call/Text 988", "F2", 10)
pdf.add_centered_text(285, "ISBN: 979-8-XXX-XXXXX-X", "F3", 10)
pdf.add_centered_text(250, "Trigger Warning: This workbook discusses trauma, abuse,", "F1", 9, gray=0.4)
pdf.add_centered_text(235, "and PTSD symptoms. Please work through at your own pace.", "F1", 9, gray=0.4)

# Page 3: Understanding PTSD in Women
pdf.new_page()
pdf.add_centered_text(740, "UNDERSTANDING PTSD IN WOMEN", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "PTSD (Post-Traumatic Stress Disorder) affects women at twice", "F1", 12)
pdf.add_text(50, 675, "the rate of men. This isn't weakness - it's biology and circumstance.", "F1", 12)
pdf.add_text(50, 645, "PTSD Symptoms Checklist:", "F2", 13)
pdf.add_text(50, 620, "RE-EXPERIENCING:", "F2", 11)
symptoms_re = ["Flashbacks", "Nightmares", "Intrusive memories", "Emotional flooding"]
y = 600
for s in symptoms_re:
    pdf.add_rect(60, y - 2, 12, 12)
    pdf.add_text(80, y, s, "F1", 11)
    y -= 20
pdf.add_text(50, y - 5, "AVOIDANCE:", "F2", 11)
y -= 25
symptoms_av = ["Avoiding places/people/situations", "Emotional numbing", "Difficulty feeling joy", "Isolation"]
for s in symptoms_av:
    pdf.add_rect(60, y - 2, 12, 12)
    pdf.add_text(80, y, s, "F1", 11)
    y -= 20
pdf.add_text(50, y - 5, "HYPERAROUSAL:", "F2", 11)
y -= 25
symptoms_hy = ["Startle easily", "Difficulty sleeping", "Hypervigilance", "Irritability/anger", "Difficulty concentrating"]
for s in symptoms_hy:
    pdf.add_rect(60, y - 2, 12, 12)
    pdf.add_text(80, y, s, "F1", 11)
    y -= 20
pdf.add_text(50, y - 10, "How many apply to you? ___ How long? ___", "F1", 12)
pdf.add_text(50, y - 35, "Your healing journey starts with understanding. You are not broken.", "F4", 11, gray=0.3)


# Page 4: Types of Trauma Women Face
pdf.new_page()
pdf.add_centered_text(740, "TYPES OF TRAUMA WOMEN FACE", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Women experience unique forms of trauma. Naming what happened", "F1", 12)
pdf.add_text(50, 675, "is a powerful first step (only when YOU are ready).", "F1", 12)
trauma_types = [
    ("Sexual assault or abuse", "1 in 3 women experience this in their lifetime"),
    ("Domestic violence", "Physical, emotional, financial, or sexual abuse by a partner"),
    ("Childhood abuse or neglect", "Including witnessing domestic violence as a child"),
    ("Birth trauma", "Traumatic delivery, NICU, pregnancy loss"),
    ("Medical trauma", "Invasive procedures, medical gaslighting, misdiagnosis"),
    ("Stalking or harassment", "Including online harassment and workplace harassment"),
    ("Community or systemic violence", "Racism, discrimination, intergenerational trauma"),
    ("Loss and grief", "Sudden death, complicated grief, abandonment")
]
y = 640
for trauma, desc in trauma_types:
    pdf.add_filled_rect(50, y - 3, 512, 30, gray=0.92)
    pdf.add_text(60, y + 12, trauma, "F2", 11)
    pdf.add_text(60, y - 2, desc, "F1", 9, gray=0.4)
    y -= 38
pdf.add_text(50, y - 15, "You do NOT need to identify your trauma to start healing.", "F2", 11)
pdf.add_text(50, y - 38, "If reading this list activated you, pause. Use the grounding", "F1", 11)
pdf.add_text(50, y - 56, "exercises on page 7 before continuing.", "F1", 11)

# Page 5: Safety Planning
pdf.new_page()
pdf.add_centered_text(740, "SAFETY PLANNING", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Before we go deeper, let's make sure you have a safety plan.", "F1", 12)
pdf.add_text(50, 665, "Am I currently in a safe living situation? Y / N", "F2", 12)
pdf.add_text(50, 640, "If NO: Here are immediate resources:", "F1", 11)
pdf.add_text(70, 618, "National DV Hotline: 1-800-799-7233 (24/7)", "F1", 11)
pdf.add_text(70, 596, "RAINN (sexual assault): 1-800-656-4673", "F1", 11)
pdf.add_text(70, 574, "Local shelter: ___________________________", "F1", 11)
pdf.add_text(50, 540, "My Personal Safety Plan:", "F2", 13)
pdf.add_text(50, 515, "Safe person I can call anytime:", "F1", 12)
pdf.add_line(50, 495, 400, 495, 0.5)
pdf.add_text(50, 472, "Safe place I can go:", "F1", 12)
pdf.add_line(50, 452, 400, 452, 0.5)
pdf.add_text(50, 429, "My therapist/counselor:", "F1", 12)
pdf.add_line(50, 409, 400, 409, 0.5)
pdf.add_text(50, 386, "Things that help when I'm triggered:", "F1", 12)
pdf.add_line(50, 366, 562, 366, 0.5)
pdf.add_line(50, 344, 562, 344, 0.5)
pdf.add_text(50, 316, "Code word I can use with a friend if I need help:", "F1", 12)
pdf.add_line(50, 296, 300, 296, 0.5)
pdf.add_text(50, 268, "Things I do to keep myself safe:", "F1", 12)
pdf.add_line(50, 248, 562, 248, 0.5)
pdf.add_line(50, 226, 562, 226, 0.5)


# Page 6: Body-Based Healing (Somatic)
pdf.new_page()
pdf.add_centered_text(740, "BODY-BASED HEALING (SOMATIC)", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Trauma lives in the body, not just the mind. Healing must include", "F1", 12)
pdf.add_text(50, 675, "the body. These exercises help release stored trauma.", "F1", 12)
pdf.add_text(50, 645, "Exercise 1: Body Scan", "F2", 13)
pdf.add_text(70, 623, "Close your eyes. Slowly scan from head to toe.", "F1", 11)
pdf.add_text(70, 603, "Where do you hold tension? Where do you feel numb?", "F1", 11)
pdf.add_text(70, 578, "Head/Face: ___________________________", "F1", 11)
pdf.add_text(70, 556, "Throat/Shoulders: ___________________________", "F1", 11)
pdf.add_text(70, 534, "Chest/Heart: ___________________________", "F1", 11)
pdf.add_text(70, 512, "Stomach/Gut: ___________________________", "F1", 11)
pdf.add_text(70, 490, "Hips/Pelvis: ___________________________", "F1", 11)
pdf.add_text(70, 468, "Legs/Feet: ___________________________", "F1", 11)
pdf.add_text(50, 435, "Exercise 2: Shake It Off", "F2", 13)
pdf.add_text(70, 413, "Stand up. Shake your hands for 30 seconds.", "F1", 11)
pdf.add_text(70, 393, "Then shake your whole body for 2 minutes.", "F1", 11)
pdf.add_text(70, 373, "Animals do this after danger - it releases survival energy.", "F1", 11)
pdf.add_text(50, 340, "Exercise 3: Butterfly Hug", "F2", 13)
pdf.add_text(70, 318, "Cross arms over chest, hands on shoulders.", "F1", 11)
pdf.add_text(70, 298, "Alternately tap left, right, left, right.", "F1", 11)
pdf.add_text(70, 278, "Continue for 2 minutes while breathing deeply.", "F1", 11)
pdf.add_text(50, 248, "After these exercises, I notice:", "F2", 11)
pdf.add_line(50, 228, 562, 228, 0.5)
pdf.add_line(50, 206, 562, 206, 0.5)

# Page 7: Grounding for Flashbacks
pdf.new_page()
pdf.add_centered_text(740, "GROUNDING FOR FLASHBACKS", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "When a flashback happens, you need to come back to the present.", "F1", 12)
pdf.add_text(50, 675, "These techniques remind your brain: I am safe NOW.", "F2", 12)
pdf.add_filled_rect(50, 635, 512, 35, gray=0.92)
pdf.add_text(60, 655, "5-4-3-2-1 TECHNIQUE", "F2", 12)
pdf.add_text(60, 640, "Name: 5 things you see, 4 you touch, 3 you hear, 2 you smell, 1 you taste", "F1", 10)
pdf.add_text(50, 608, "My 5-4-3-2-1 right now:", "F1", 11)
pdf.add_text(70, 588, "See: ___________________________", "F1", 11)
pdf.add_text(70, 568, "Touch: ___________________________", "F1", 11)
pdf.add_text(70, 548, "Hear: ___________________________", "F1", 11)
pdf.add_text(70, 528, "Smell: ___________________________", "F1", 11)
pdf.add_text(70, 508, "Taste: ___________________________", "F1", 11)
pdf.add_filled_rect(50, 475, 512, 25, gray=0.92)
pdf.add_text(60, 485, "ORIENTATION SCRIPT (say out loud):", "F2", 11)
pdf.add_text(60, 450, "'My name is ___. I am ___ years old. Today is ___.", "F4", 11)
pdf.add_text(60, 430, "I am in [location]. I am safe. That was then. This is now.'", "F4", 11)
pdf.add_text(50, 400, "Other grounding techniques that work for me:", "F2", 11)
pdf.add_text(70, 378, "- Hold ice cubes", "F1", 11)
pdf.add_text(70, 358, "- Stomp feet on the ground", "F1", 11)
pdf.add_text(70, 338, "- Smell something strong (peppermint, coffee)", "F1", 11)
pdf.add_text(70, 318, "- Splash cold water on face", "F1", 11)
pdf.add_text(70, 298, "- Press palms together hard for 30 seconds", "F1", 11)
pdf.add_text(50, 265, "My personal grounding strategy:", "F2", 11)
pdf.add_line(50, 245, 562, 245, 0.5)
pdf.add_line(50, 223, 562, 223, 0.5)


# Page 8: Trauma & Relationships
pdf.new_page()
pdf.add_centered_text(740, "TRAUMA & RELATIONSHIPS", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Trauma changes how we relate to others. You may notice:", "F1", 12)
patterns = [
    "Difficulty trusting anyone",
    "Attracting or staying in unhealthy relationships",
    "People-pleasing or fawning to stay safe",
    "Pushing people away when they get too close",
    "Feeling unworthy of healthy love",
    "Difficulty with intimacy (physical or emotional)",
    "Hypervigilance - always scanning for threats in others"
]
y = 665
for p in patterns:
    pdf.add_rect(55, y - 2, 12, 12)
    pdf.add_text(75, y, p, "F1", 11)
    y -= 24
pdf.add_text(50, y - 10, "Which patterns do you recognize in yourself?", "F2", 12)
pdf.add_line(50, y - 30, 562, y - 30, 0.5)
pdf.add_line(50, y - 52, 562, y - 52, 0.5)
pdf.add_text(50, y - 80, "A relationship that feels safe to me:", "F1", 12)
pdf.add_line(50, y - 100, 562, y - 100, 0.5)
pdf.add_text(50, y - 125, "What 'safe' looks like in a relationship:", "F2", 12)
pdf.add_text(70, y - 147, "- Consistency (they do what they say)", "F1", 11)
pdf.add_text(70, y - 167, "- Respect for my boundaries", "F1", 11)
pdf.add_text(70, y - 187, "- I can say no without consequences", "F1", 11)
pdf.add_text(70, y - 207, "- They don't punish me for my feelings", "F1", 11)
pdf.add_text(70, y - 227, "- I feel calm (not anxious) around them", "F1", 11)

# Page 9: Rebuilding Trust
pdf.new_page()
pdf.add_centered_text(740, "REBUILDING TRUST", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Trust was broken. Rebuilding it is brave work - and it takes time.", "F1", 12)
pdf.add_text(50, 665, "Trust in myself:", "F2", 13)
pdf.add_text(70, 643, "Do I trust my own judgment? (1-10): ___", "F1", 11)
pdf.add_text(70, 621, "Do I trust my ability to keep myself safe? (1-10): ___", "F1", 11)
pdf.add_text(70, 599, "Do I trust that I deserve good things? (1-10): ___", "F1", 11)
pdf.add_text(50, 565, "Trust in others:", "F2", 13)
pdf.add_text(70, 543, "Who has earned my trust? (and how):", "F1", 11)
pdf.add_line(70, 523, 562, 523, 0.5)
pdf.add_line(70, 501, 562, 501, 0.5)
pdf.add_text(50, 470, "Small trust-building experiments:", "F2", 12)
pdf.add_text(70, 448, "1. Share something small and see how they respond", "F1", 11)
pdf.add_text(70, 426, "2. Ask for something small and see if they follow through", "F1", 11)
pdf.add_text(70, 404, "3. Set a small boundary and see if they respect it", "F1", 11)
pdf.add_text(50, 372, "My trust-building experiment:", "F2", 11)
pdf.add_text(70, 350, "What I'll try:", "F1", 11)
pdf.add_line(160, 350, 562, 350, 0.5)
pdf.add_text(70, 328, "With whom:", "F1", 11)
pdf.add_line(160, 328, 400, 328, 0.5)
pdf.add_text(70, 306, "How it went:", "F1", 11)
pdf.add_line(160, 306, 562, 306, 0.5)
pdf.add_line(70, 284, 562, 284, 0.5)

# Page 10: Cognitive Processing (Stuck Points)
pdf.new_page()
pdf.add_centered_text(740, "STUCK POINTS: SELF-BLAME & SHAME", "F2", 18)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Stuck points are beliefs that keep you trapped in trauma's aftermath.", "F1", 12)
pdf.add_text(50, 675, "Women often carry EXTRA shame and self-blame around trauma.", "F1", 12)
pdf.add_text(50, 645, "Common Stuck Points for Women:", "F2", 13)
stuck_points = [
    "'It was my fault' (IT WAS NOT)",
    "'I should have fought harder / said no louder'",
    "'If I hadn't [worn that / gone there / trusted them]...'",
    "'Something is wrong with me'",
    "'I'm damaged goods'",
    "'No one will love me if they know'",
    "'I should be over this by now'"
]
y = 618
for sp in stuck_points:
    pdf.add_text(70, y, sp, "F4", 11)
    y -= 22
pdf.add_text(50, y - 10, "Which stuck points do you carry?", "F2", 12)
pdf.add_line(50, y - 30, 562, y - 30, 0.5)
pdf.add_line(50, y - 52, 562, y - 52, 0.5)
pdf.add_text(50, y - 80, "Challenge: What would you say to another woman who said this?", "F2", 11)
pdf.add_line(50, y - 100, 562, y - 100, 0.5)
pdf.add_line(50, y - 122, 562, y - 122, 0.5)
pdf.add_filled_rect(50, y - 175, 512, 40, gray=0.92)
pdf.add_text(60, y - 148, "The truth: What happened to you was NOT your fault.", "F2", 12)
pdf.add_text(60, y - 168, "You survived. That took extraordinary strength.", "F2", 12)


# Page 11: Self-Compassion
pdf.new_page()
pdf.add_centered_text(740, "SELF-COMPASSION AFTER TRAUMA", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Trauma survivors are often their own harshest critics.", "F1", 12)
pdf.add_text(50, 675, "Self-compassion is revolutionary healing.", "F4", 12, gray=0.3)
pdf.add_text(50, 645, "Exercise: Write a Letter of Compassion to Yourself", "F2", 13)
pdf.add_text(50, 620, "Write to yourself as you would to a dear friend who experienced", "F1", 11)
pdf.add_text(50, 600, "what you went through:", "F1", 11)
pdf.add_text(50, 575, "Dear _______________,", "F4", 12)
y = 550
for i in range(12):
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 22
pdf.add_text(50, y - 10, "With love,", "F4", 12)
pdf.add_text(50, y - 32, "_______________", "F1", 11)
pdf.add_text(50, y - 60, "Self-Compassion Mantra:", "F2", 11)
pdf.add_text(50, y - 82, "'This is a moment of suffering. Suffering is part of being human.", "F4", 11)
pdf.add_text(50, y - 102, "May I be kind to myself. May I give myself the compassion I need.'", "F4", 11)

# Page 12: Boundaries After Trauma
pdf.new_page()
pdf.add_centered_text(740, "BOUNDARIES AFTER TRAUMA", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Trauma often destroys our sense of boundaries. Rebuilding them", "F1", 12)
pdf.add_text(50, 675, "is reclaiming your right to say YES and NO.", "F1", 12)
pdf.add_text(50, 645, "Types of boundaries I need:", "F2", 13)
boundary_types = [
    ("Physical:", "Who can touch me, how close people stand, personal space"),
    ("Emotional:", "What I share, with whom, how much I take on"),
    ("Time:", "How I spend my time, saying no to obligations"),
    ("Digital:", "Who has access to me online, response expectations"),
    ("Sexual:", "What I'm comfortable with, what I need, what's a no")
]
y = 615
for btype, desc in boundary_types:
    pdf.add_text(60, y, btype, "F2", 11)
    pdf.add_text(150, y, desc, "F1", 10, gray=0.4)
    pdf.add_text(60, y - 20, "My boundary:", "F1", 10)
    pdf.add_line(130, y - 20, 562, y - 20, 0.5)
    y -= 50
pdf.add_text(50, y - 10, "Boundary scripts:", "F2", 12)
pdf.add_text(70, y - 32, "'I'm not comfortable with that.'", "F4", 11)
pdf.add_text(70, y - 52, "'I need some space right now.'", "F4", 11)
pdf.add_text(70, y - 72, "'That doesn't work for me.'", "F4", 11)
pdf.add_text(70, y - 92, "'I'm going to leave now.'", "F4", 11)
pdf.add_text(50, y - 120, "Remember: You don't owe anyone an explanation for your boundaries.", "F2", 11)


# Page 13: Reclaiming Your Body
pdf.new_page()
pdf.add_centered_text(740, "RECLAIMING YOUR BODY", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "After trauma, your body can feel like enemy territory.", "F1", 12)
pdf.add_text(50, 675, "Reclaiming it means learning to live in it safely again.", "F1", 12)
pdf.add_text(50, 645, "My relationship with my body right now:", "F2", 12)
pdf.add_text(70, 623, "I feel disconnected from my body: Y / N / Sometimes", "F1", 11)
pdf.add_text(70, 601, "I feel safe in my body: Y / N / Sometimes", "F1", 11)
pdf.add_text(70, 579, "I punish my body: Y / N / Sometimes", "F1", 11)
pdf.add_text(70, 557, "I can feel pleasure: Y / N / Sometimes", "F1", 11)
pdf.add_text(50, 525, "Body Reclamation Activities:", "F2", 13)
activities = [
    "Gentle yoga or stretching (you control the movement)",
    "Dance alone to music you love",
    "Take a warm bath with intention",
    "Get a massage (when/if you're ready)",
    "Wear something that makes you feel powerful",
    "Look in the mirror and say one kind thing",
    "Practice interoception (notice hunger, thirst, temperature)"
]
y = 498
for act in activities:
    pdf.add_rect(55, y - 2, 12, 12)
    pdf.add_text(75, y, act, "F1", 11)
    y -= 24
pdf.add_text(50, y - 15, "Something I want my body to know:", "F2", 11)
pdf.add_line(50, y - 35, 562, y - 35, 0.5)
pdf.add_line(50, y - 57, 562, y - 57, 0.5)
pdf.add_text(50, y - 85, "My body kept me alive. It deserves my gratitude, not my punishment.", "F4", 11, gray=0.3)

# Pages 14-18: Weekly Healing Tracker (5 pages)
for week in range(5):
    pdf.new_page()
    pdf.add_centered_text(740, f"WEEKLY HEALING TRACKER - WEEK {week+1}", "F2", 18)
    pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
    pdf.add_text(50, 700, f"Week of: ___/___/___ to ___/___/___", "F1", 11)
    
    # Daily check-in grid
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    y = 670
    pdf.add_filled_rect(50, y - 3, 512, 18, gray=0.88)
    pdf.add_text(55, y, "Day", "F2", 9)
    pdf.add_text(90, y, "Triggers?", "F2", 9)
    pdf.add_text(165, y, "Grounding used?", "F2", 9)
    pdf.add_text(280, y, "Sleep (hrs)", "F2", 9)
    pdf.add_text(360, y, "Mood (1-10)", "F2", 9)
    pdf.add_text(445, y, "Self-care?", "F2", 9)
    y -= 22
    for day in days:
        pdf.add_text(55, y, day, "F1", 9)
        pdf.add_text(90, y, "Y / N", "F1", 9)
        pdf.add_text(165, y, "Y / N", "F1", 9)
        pdf.add_text(280, y, "___", "F1", 9)
        pdf.add_text(360, y, "___", "F1", 9)
        pdf.add_text(445, y, "Y / N", "F1", 9)
        y -= 20
    
    y -= 10
    pdf.add_text(50, y, "Biggest trigger this week:", "F2", 11)
    pdf.add_line(50, y - 18, 562, y - 18, 0.5)
    pdf.add_text(50, y - 40, "How I coped:", "F2", 11)
    pdf.add_line(50, y - 58, 562, y - 58, 0.5)
    pdf.add_text(50, y - 80, "A moment of healing I noticed:", "F2", 11)
    pdf.add_line(50, y - 98, 562, y - 98, 0.5)
    pdf.add_text(50, y - 120, "Something I'm proud of:", "F2", 11)
    pdf.add_line(50, y - 138, 562, y - 138, 0.5)
    pdf.add_text(50, y - 160, "What I need more of next week:", "F2", 11)
    pdf.add_line(50, y - 178, 562, y - 178, 0.5)
    pdf.add_text(50, y - 205, "Healing affirmation for the week:", "F4", 11, gray=0.3)
    pdf.add_line(50, y - 225, 562, y - 225, 0.5)


# Page 19: My Healing is Not Linear
pdf.new_page()
pdf.add_centered_text(740, "MY HEALING IS NOT LINEAR", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Some days you'll feel like you're making progress.", "F1", 12)
pdf.add_text(50, 675, "Some days it will feel like you're back at square one.", "F1", 12)
pdf.add_text(50, 655, "Both are part of healing.", "F2", 12)
pdf.add_text(50, 620, "Signs of healing (even if it doesn't feel like it):", "F2", 13)
healing_signs = [
    "Flashbacks are shorter or less intense",
    "You can name your emotions",
    "You set a boundary (even a small one)",
    "You asked for help",
    "You had a moment of peace",
    "You didn't dissociate as often",
    "You chose something just for you",
    "You recognized a trigger before reacting",
    "You felt anger (instead of numbness)",
    "You allowed someone to be kind to you"
]
y = 593
for sign in healing_signs:
    pdf.add_rect(55, y - 2, 12, 12)
    pdf.add_text(75, y, sign, "F1", 11)
    y -= 24
pdf.add_text(50, y - 15, "My personal signs of healing:", "F2", 12)
pdf.add_line(50, y - 35, 562, y - 35, 0.5)
pdf.add_line(50, y - 57, 562, y - 57, 0.5)
pdf.add_line(50, y - 79, 562, y - 79, 0.5)
pdf.add_filled_rect(50, y - 130, 512, 35, gray=0.92)
pdf.add_centered_text(y - 108, "A setback is not a reset. You never go back to zero.", "F5", 13)

# Page 20: Support Resources
pdf.new_page()
pdf.add_centered_text(740, "SUPPORT RESOURCES", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "You deserve support. Here are resources specifically for women:", "F1", 12)
resources = [
    ("RAINN (Rape, Abuse & Incest National Network)", "1-800-656-4673 | rainn.org"),
    ("National Domestic Violence Hotline", "1-800-799-7233 | thehotline.org"),
    ("988 Suicide & Crisis Lifeline", "Call or text 988 (24/7)"),
    ("Crisis Text Line", "Text HOME to 741741"),
    ("National Sexual Assault Hotline", "1-800-656-4673 (24/7)"),
    ("Women's Law (legal help)", "womenslaw.org | 1-800-799-7233"),
    ("SAMHSA Helpline", "1-800-662-4357 (treatment referrals)"),
    ("Veterans Crisis Line (women vets)", "988, Press 1")
]
y = 660
for name, info in resources:
    pdf.add_filled_rect(50, y - 5, 512, 32, gray=0.92)
    pdf.add_text(60, y + 10, name, "F2", 11)
    pdf.add_text(60, y - 5, info, "F1", 10)
    y -= 42
pdf.add_text(50, y - 10, "My personal resources:", "F2", 12)
pdf.add_text(70, y - 32, "Therapist: ___________________________", "F1", 11)
pdf.add_text(70, y - 54, "Support group: ___________________________", "F1", 11)
pdf.add_text(70, y - 76, "Trusted friend: ___________________________", "F1", 11)
pdf.add_text(70, y - 98, "Safe place: ___________________________", "F1", 11)


# Page 21: Window of Tolerance
pdf.new_page()
pdf.add_centered_text(740, "YOUR WINDOW OF TOLERANCE", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Your 'window of tolerance' is the zone where you can function.", "F1", 12)
pdf.add_text(50, 675, "Trauma narrows this window. Healing expands it.", "F1", 12)
pdf.add_filled_rect(50, 630, 512, 30, gray=0.85)
pdf.add_text(60, 647, "HYPERAROUSAL (above the window): anxiety, panic, rage, hypervigilance", "F2", 10)
pdf.add_rect(50, 560, 512, 60, 2)
pdf.add_centered_text(595, "WINDOW OF TOLERANCE", "F2", 12)
pdf.add_centered_text(575, "(Calm, present, able to think clearly)", "F1", 10)
pdf.add_filled_rect(50, 520, 512, 30, gray=0.85)
pdf.add_text(60, 537, "HYPOAROUSAL (below the window): numbing, dissociation, collapse", "F2", 10)
pdf.add_text(50, 490, "When I'm ABOVE my window (hyperaroused), I notice:", "F2", 11)
pdf.add_line(50, 470, 562, 470, 0.5)
pdf.add_line(50, 448, 562, 448, 0.5)
pdf.add_text(50, 420, "What brings me back DOWN into my window:", "F1", 11)
pdf.add_line(50, 400, 562, 400, 0.5)
pdf.add_text(50, 372, "When I'm BELOW my window (hypoaroused), I notice:", "F2", 11)
pdf.add_line(50, 352, 562, 352, 0.5)
pdf.add_line(50, 330, 562, 330, 0.5)
pdf.add_text(50, 302, "What brings me back UP into my window:", "F1", 11)
pdf.add_line(50, 282, 562, 282, 0.5)
pdf.add_text(50, 250, "My window is getting wider: True / Not Yet / I'm Not Sure", "F1", 12)

# Page 22: Trauma Responses (Fight/Flight/Freeze/Fawn)
pdf.new_page()
pdf.add_centered_text(740, "UNDERSTANDING YOUR TRAUMA RESPONSES", "F2", 18)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Your nervous system developed these responses to keep you alive.", "F1", 12)
pdf.add_text(50, 675, "They were survival strategies. Thank them, then learn new ones.", "F1", 12)
responses = [
    ("FIGHT", "Anger, control, perfectionism, criticizing others"),
    ("FLIGHT", "Staying busy, overworking, overthinking, avoiding"),
    ("FREEZE", "Numbing, dissociating, brain fog, inability to act"),
    ("FAWN", "People-pleasing, losing yourself, no boundaries, over-giving")
]
y = 640
for resp, desc in responses:
    pdf.add_filled_rect(50, y - 5, 512, 28, gray=0.92)
    pdf.add_text(60, y + 8, resp, "F2", 12)
    pdf.add_text(120, y + 8, desc, "F1", 10)
    pdf.add_text(60, y - 5, "I notice this when:", "F1", 9)
    pdf.add_line(160, y - 5, 550, y - 5, 0.3)
    y -= 42
pdf.add_text(50, y - 5, "My primary response pattern: _______________", "F2", 12)
pdf.add_text(50, y - 30, "My secondary response: _______________", "F1", 11)
pdf.add_text(50, y - 60, "New response I'm learning:", "F2", 11)
pdf.add_line(50, y - 80, 562, y - 80, 0.5)
pdf.add_line(50, y - 102, 562, y - 102, 0.5)
pdf.add_text(50, y - 130, "Mantra: 'I am safe now. I can choose a different response.'", "F4", 11, gray=0.3)

# Page 23: Shame vs. Guilt
pdf.new_page()
pdf.add_centered_text(740, "RELEASING SHAME", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Shame says 'I AM bad.' Guilt says 'I DID something bad.'", "F1", 12)
pdf.add_text(50, 675, "Trauma survivors carry shame that doesn't belong to them.", "F2", 12)
pdf.add_text(50, 645, "Shame I'm carrying that ISN'T mine:", "F2", 12)
pdf.add_line(50, 625, 562, 625, 0.5)
pdf.add_line(50, 603, 562, 603, 0.5)
pdf.add_line(50, 581, 562, 581, 0.5)
pdf.add_text(50, 553, "Who does this shame actually belong to?", "F2", 12)
pdf.add_line(50, 533, 562, 533, 0.5)
pdf.add_text(50, 503, "Shame Release Exercise:", "F2", 13)
pdf.add_text(50, 480, "Complete these sentences:", "F1", 11)
pdf.add_text(70, 455, "I am NOT what happened to me. I am...", "F4", 11)
pdf.add_line(70, 435, 562, 435, 0.5)
pdf.add_text(70, 410, "I release the shame of...", "F4", 11)
pdf.add_line(70, 390, 562, 390, 0.5)
pdf.add_text(70, 365, "I deserve...", "F4", 11)
pdf.add_line(70, 345, 562, 345, 0.5)
pdf.add_text(70, 320, "My worth is not determined by...", "F4", 11)
pdf.add_line(70, 300, 562, 300, 0.5)
pdf.add_text(70, 275, "I am worthy because...", "F4", 11)
pdf.add_line(70, 255, 562, 255, 0.5)
pdf.add_filled_rect(50, 195, 512, 40, gray=0.92)
pdf.add_centered_text(220, "Shame cannot survive being spoken.", "F5", 13)
pdf.add_centered_text(200, "Share with someone safe when you're ready.", "F1", 11)


# Page 24: Inner Child Work
pdf.new_page()
pdf.add_centered_text(740, "HEALING YOUR INNER CHILD", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "If your trauma happened in childhood, your inner child needs healing.", "F1", 12)
pdf.add_text(50, 675, "You can give her now what she didn't receive then.", "F4", 12, gray=0.3)
pdf.add_text(50, 645, "Write a letter to your younger self:", "F2", 13)
pdf.add_text(50, 620, "Dear little _______________,", "F4", 12)
y = 595
for i in range(14):
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 22
pdf.add_text(50, y - 10, "What I want her to know:", "F2", 11)
pdf.add_text(70, y - 32, "- It wasn't your fault", "F1", 11)
pdf.add_text(70, y - 52, "- You were just a child", "F1", 11)
pdf.add_text(70, y - 72, "- You deserved protection", "F1", 11)
pdf.add_text(70, y - 92, "- You are lovable", "F1", 11)
pdf.add_text(70, y - 112, "- You survive and become strong", "F1", 11)

# Page 25: Triggers Map
pdf.new_page()
pdf.add_centered_text(740, "MY TRIGGERS MAP", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Knowing your triggers gives you power over them.", "F1", 12)
pdf.add_text(50, 665, "Common triggers for me:", "F2", 12)
trigger_cats = [
    ("Sensory:", "sounds, smells, touch, visuals"),
    ("Situational:", "places, times of day/year, events"),
    ("Relational:", "people, behaviors, tone of voice"),
    ("Internal:", "emotions, body sensations, thoughts"),
    ("Anniversary:", "dates, seasons, milestones")
]
y = 638
for cat, examples in trigger_cats:
    pdf.add_text(60, y, cat, "F2", 11)
    pdf.add_text(160, y, examples, "F1", 9, gray=0.4)
    pdf.add_text(60, y - 20, "My triggers:", "F1", 10)
    pdf.add_line(130, y - 20, 562, y - 20, 0.5)
    pdf.add_text(60, y - 40, "My plan:", "F1", 10)
    pdf.add_line(110, y - 40, 562, y - 40, 0.5)
    y -= 68
pdf.add_text(50, y, "Emerging trigger I'm working on:", "F2", 11)
pdf.add_line(50, y - 20, 562, y - 20, 0.5)

# Page 26: Sleep After Trauma
pdf.new_page()
pdf.add_centered_text(740, "SLEEP AFTER TRAUMA", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Trauma disrupts sleep. Nightmares, insomnia, and hypervigilance", "F1", 12)
pdf.add_text(50, 675, "make bedtime feel unsafe. Here's how to reclaim your rest:", "F1", 12)
pdf.add_text(50, 645, "My Sleep Safety Plan:", "F2", 13)
pdf.add_text(70, 620, "My bedroom feels safe when:", "F1", 11)
pdf.add_line(260, 620, 562, 620, 0.5)
pdf.add_text(70, 596, "My bedtime routine:", "F1", 11)
pdf.add_line(200, 596, 562, 596, 0.5)
pdf.add_text(70, 572, "If I have a nightmare, I will:", "F1", 11)
pdf.add_line(260, 572, 562, 572, 0.5)
pdf.add_text(70, 548, "Comfort items near my bed:", "F1", 11)
pdf.add_line(260, 548, 562, 548, 0.5)
pdf.add_text(50, 515, "Techniques for trauma-related insomnia:", "F2", 12)
pdf.add_text(70, 493, "- Body scan meditation (noticing without judging)", "F1", 11)
pdf.add_text(70, 471, "- Weighted blanket for grounding", "F1", 11)
pdf.add_text(70, 449, "- Nightlight or leaving door open (it's okay!)", "F1", 11)
pdf.add_text(70, 427, "- Sleep audio (rain, white noise, guided meditation)", "F1", 11)
pdf.add_text(70, 405, "- Journaling before bed to 'empty' your mind", "F1", 11)
pdf.add_text(70, 383, "- Keep a grounding object on nightstand", "F1", 11)
pdf.add_text(50, 350, "If nightmares persist, ask your therapist about:", "F2", 11)
pdf.add_text(70, 328, "- Imagery Rehearsal Therapy (IRT)", "F1", 11)
pdf.add_text(70, 306, "- EMDR for nightmare processing", "F1", 11)
pdf.add_text(70, 284, "- Prazosin (medication for PTSD nightmares)", "F1", 11)


# Page 27: Anger After Trauma
pdf.new_page()
pdf.add_centered_text(740, "YOUR RIGHT TO ANGER", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Women are taught that anger is 'unladylike.' But after trauma,", "F1", 12)
pdf.add_text(50, 675, "anger is a sign of healing. It means you know you didn't deserve it.", "F1", 12)
pdf.add_text(50, 645, "Anger is information. It tells you:", "F2", 12)
pdf.add_text(70, 623, "- A boundary was violated", "F1", 11)
pdf.add_text(70, 601, "- Something is unjust", "F1", 11)
pdf.add_text(70, 579, "- You deserve better", "F1", 11)
pdf.add_text(70, 557, "- You are ready to fight for yourself", "F1", 11)
pdf.add_text(50, 525, "Safe ways to express anger:", "F2", 12)
pdf.add_text(70, 503, "- Write an unsent letter to the person who hurt you", "F1", 11)
pdf.add_text(70, 481, "- Scream into a pillow or in your car", "F1", 11)
pdf.add_text(70, 459, "- Intense exercise (boxing, running, dancing)", "F1", 11)
pdf.add_text(70, 437, "- Tear up paper or smash ice cubes", "F1", 11)
pdf.add_text(70, 415, "- Talk to your therapist about it", "F1", 11)
pdf.add_text(50, 383, "Write what you're angry about (this is a safe space):", "F2", 11)
y = 360
for i in range(7):
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 22
pdf.add_text(50, y - 10, "Your anger is valid. It means you're waking up.", "F4", 11, gray=0.3)

# Page 28: Post-Traumatic Growth
pdf.new_page()
pdf.add_centered_text(740, "POST-TRAUMATIC GROWTH", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Trauma changes you. But some of those changes can become strengths.", "F1", 12)
pdf.add_text(50, 675, "This is NOT about being grateful for trauma - it's about honoring", "F1", 12)
pdf.add_text(50, 655, "what you've built from the wreckage.", "F1", 12)
pdf.add_text(50, 625, "Areas of Post-Traumatic Growth:", "F2", 13)
growth_areas = [
    "Deeper appreciation for life",
    "Stronger sense of self",
    "Deeper relationships (quality over quantity)",
    "New possibilities or paths",
    "Spiritual or existential growth"
]
y = 598
for area in growth_areas:
    pdf.add_text(70, y, f"- {area}", "F1", 11)
    y -= 22
pdf.add_text(50, y - 10, "Strengths that came from my experience:", "F2", 12)
for i in range(4):
    pdf.add_text(60, y - 35 - i*25, f"{i+1}.", "F1", 11)
    pdf.add_line(80, y - 35 - i*25, 562, y - 35 - i*25, 0.5)
pdf.add_text(50, y - 150, "How has trauma shaped who I am becoming?", "F2", 11)
pdf.add_line(50, y - 172, 562, y - 172, 0.5)
pdf.add_line(50, y - 194, 562, y - 194, 0.5)
pdf.add_line(50, y - 216, 562, y - 216, 0.5)
pdf.add_text(50, y - 250, "You are not what happened to you.", "F5", 13)
pdf.add_text(50, y - 275, "You are what you CHOOSE to become.", "F5", 13)

# Page 29: My Healing Commitments
pdf.new_page()
pdf.add_centered_text(740, "MY HEALING COMMITMENTS", "F2", 20)
pdf.add_line(50, 725, 562, 725, 1, gray=0.7)
pdf.add_text(50, 695, "Healing is active. What are you committing to?", "F1", 12)
pdf.add_text(50, 665, "I commit to:", "F2", 13)
commitments = [
    "Being patient with my healing timeline",
    "Attending therapy regularly",
    "Using my grounding techniques when triggered",
    "Setting boundaries that protect my peace",
    "Not isolating when I'm struggling",
    "Treating my body with kindness",
    "Believing I deserve a life beyond survival",
    "Asking for help when I need it",
    "Celebrating my progress (no matter how small)",
    "Not giving up on myself"
]
y = 638
for c in commitments:
    pdf.add_rect(55, y - 2, 12, 12)
    pdf.add_text(75, y, c, "F1", 11)
    y -= 24
pdf.add_text(50, y - 15, "My personal commitment:", "F2", 12)
pdf.add_line(50, y - 37, 562, y - 37, 0.5)
pdf.add_line(50, y - 59, 562, y - 59, 0.5)
pdf.add_text(50, y - 85, "Signed: _______________ Date: ___/___/___", "F1", 12)


# Page 30: Final Page - You Are More Than What Happened
pdf.new_page()
pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
pdf.add_centered_text(560, "YOU ARE MORE", "F2", 30)
pdf.add_centered_text(520, "THAN WHAT HAPPENED.", "F2", 30)
pdf.add_line(180, 500, 432, 500, 2, gray=0.5)
pdf.add_centered_text(460, "You are the one who survived.", "F4", 15, gray=0.3)
pdf.add_centered_text(435, "You are the one who kept going.", "F4", 15, gray=0.3)
pdf.add_centered_text(410, "You are the one who said: enough.", "F4", 15, gray=0.3)
pdf.add_centered_text(385, "You are the one choosing to heal.", "F4", 15, gray=0.3)
pdf.add_centered_text(330, "That is extraordinary.", "F5", 18)
pdf.add_line(220, 310, 392, 310, 1, gray=0.5)
pdf.add_centered_text(275, "If you need help right now:", "F2", 12)
pdf.add_centered_text(250, "RAINN: 1-800-656-4673", "F1", 12)
pdf.add_centered_text(228, "National DV Hotline: 1-800-799-7233", "F1", 12)
pdf.add_centered_text(206, "988 Suicide & Crisis Lifeline: Call/Text 988", "F1", 12)
pdf.add_centered_text(184, "Crisis Text Line: Text HOME to 741741", "F1", 12)
pdf.add_centered_text(140, f"Written with hope by {author}", "F1", 11, gray=0.5)

pdf.save("Book175_PTSD_Workbook_Women.pdf")
print("SUCCESS: Book175_PTSD_Workbook_Women.pdf created (30 pages)")
