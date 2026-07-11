"""Book 166: PTSD Recovery Workbook for Veterans"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    margin = 50
    rmargin = 562

    # === PAGE 1: Title Page ===
    pdf.add_filled_rect(0, 0, 612, 792, 0.1)
    pdf.add_centered_text(620, "WARRIOR'S PATH", 'F5', 30, 1)
    pdf.add_centered_text(575, "A PTSD Recovery Workbook", 'F4', 18, 0.9)
    pdf.add_centered_text(550, "for Veterans", 'F4', 18, 0.9)
    pdf.add_line(150, 530, 462, 530, 1.5, 0.7)
    pdf.add_centered_text(490, "Evidence-Based Tools for Healing", 'F1', 12, 0.8)
    pdf.add_centered_text(468, "After Military Service", 'F1', 12, 0.8)
    pdf.add_centered_text(400, "Cognitive Processing Therapy Worksheets", 'F1', 10, 0.7)
    pdf.add_centered_text(383, "Grounding Techniques for Hypervigilance", 'F1', 10, 0.7)
    pdf.add_centered_text(366, "Weekly Symptom Tracking", 'F1', 10, 0.7)
    pdf.add_centered_text(349, "Reintegration & Moral Injury Work", 'F1', 10, 0.7)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    pdf.add_centered_text(170, "You served with honor. You deserve to heal.", 'F4', 11, 0.7)


    # === PAGE 2: Copyright ===
    pdf.new_page()
    pdf.add_centered_text(700, "Warrior's Path", 'F5', 14)
    pdf.add_centered_text(680, "A PTSD Recovery Workbook for Veterans", 'F4', 10)
    pdf.add_centered_text(650, f"Copyright 2024 {author}. All rights reserved.", 'F1', 9)
    pdf.add_centered_text(632, "No part of this book may be reproduced without written permission.", 'F1', 8)
    pdf.add_centered_text(600, "IMPORTANT DISCLAIMER", 'F2', 10)
    pdf.add_text(margin, 580, "This workbook is designed as a supplemental tool for PTSD recovery.", 'F1', 9)
    pdf.add_text(margin, 565, "It is NOT a replacement for professional mental health treatment.", 'F1', 9)
    pdf.add_text(margin, 550, "If you are in crisis, contact the Veterans Crisis Line: 988 (Press 1)", 'F2', 9)
    pdf.add_text(margin, 535, "or text 838255.", 'F2', 9)
    pdf.add_text(margin, 505, "This workbook incorporates evidence-based techniques from:", 'F1', 9)
    pdf.add_text(margin, 488, "- Cognitive Processing Therapy (CPT)", 'F1', 9)
    pdf.add_text(margin, 473, "- Prolonged Exposure (PE) principles", 'F1', 9)
    pdf.add_text(margin, 458, "- Mindfulness-Based Stress Reduction (MBSR)", 'F1', 9)
    pdf.add_text(margin, 443, "- Imagery Rehearsal Therapy (IRT)", 'F1', 9)
    pdf.add_centered_text(400, "Dedicated to all who served and carry invisible wounds.", 'F4', 10)
    pdf.add_centered_text(380, "Your courage didn't end when your service did.", 'F4', 10)


    # === PAGE 3: Understanding Combat PTSD ===
    pdf.new_page()
    pdf.add_centered_text(750, "UNDERSTANDING COMBAT PTSD", 'F2', 16)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 720
    pdf.add_text(margin, y, "WHAT IS PTSD?", 'F2', 12)
    y -= 18
    pdf.add_text(margin, y, "Post-Traumatic Stress Disorder is a normal response to abnormal events.", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "Your brain is doing exactly what it was trained to do: stay alert, anticipate", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "threats, and protect you. The problem is that these responses are now", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "activating in situations where there is no actual danger.", 'F1', 10)
    y -= 30
    pdf.add_text(margin, y, "PREVALENCE IN VETERANS:", 'F2', 11)
    y -= 18
    pdf.add_text(margin, y, "- 11-20% of veterans from Iraq/Afghanistan develop PTSD", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "- 12% of Gulf War veterans have PTSD in a given year", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "- 15% of Vietnam veterans were diagnosed with PTSD at time of study", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "- You are NOT alone. Millions of veterans share this experience.", 'F1', 10)
    y -= 30
    pdf.add_text(margin, y, "PTSD IS NOT WEAKNESS", 'F2', 11)
    y -= 18
    pdf.add_text(margin, y, "Just as a physical injury from combat requires medical treatment, a", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "psychological injury requires care. PTSD is not a character flaw.", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "It is not cowardice. It is a wound that needs healing.", 'F1', 10)
    y -= 30
    pdf.add_filled_rect(margin, y - 80, rmargin - margin, 80, 0.93)
    pdf.add_text(margin + 10, y - 15, "Reflect: What has PTSD cost you? What would healing give back?", 'F2', 10)
    y -= 35
    for i in range(4):
        pdf.add_line(margin + 10, y, rmargin - 10, y, 0.5, 0.5)
        y -= 18


    # === PAGE 4: Trauma Response Types ===
    pdf.new_page()
    pdf.add_centered_text(750, "TRAUMA RESPONSE TYPES IN MILITARY CONTEXT", 'F2', 14)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 720
    pdf.add_text(margin, y, "Your nervous system developed survival responses during service. Understanding", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "them helps you recognize when they activate inappropriately in civilian life.", 'F1', 10)
    y -= 30

    responses = [
        ("FIGHT", "Aggression, confrontation, rage outbursts, road rage, verbal attacks",
         "In combat: necessary for survival and mission completion",
         "In civilian life: damaged relationships, legal trouble, isolation"),
        ("FLIGHT", "Avoidance, substance use, workaholism, constant busyness",
         "In combat: tactical withdrawal, strategic repositioning",
         "In civilian life: avoiding crowds, isolating, numbing with alcohol"),
        ("FREEZE", "Shutdown, dissociation, numbness, inability to act or feel",
         "In combat: playing dead, waiting for the right moment to act",
         "In civilian life: emotional flatness, feeling disconnected from family"),
        ("FAWN", "People-pleasing, inability to say no, loss of identity",
         "In combat: following orders without question for unit cohesion",
         "In civilian life: losing yourself to keep the peace, no boundaries"),
    ]

    for name, desc, combat, civilian in responses:
        pdf.add_text(margin, y, f"{name} Response:", 'F2', 11)
        y -= 15
        pdf.add_text(margin + 15, y, desc, 'F1', 9)
        y -= 13
        pdf.add_text(margin + 15, y, combat, 'F4', 9)
        y -= 13
        pdf.add_text(margin + 15, y, civilian, 'F4', 9)
        y -= 22

    pdf.add_text(margin, y, "HYPERVIGILANCE:", 'F2', 11)
    y -= 16
    pdf.add_text(margin, y, "Always scanning for threats. Sitting with back to the wall. Checking exits.", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "Startling at loud noises. Difficulty relaxing even in safe environments.", 'F1', 10)
    y -= 25
    pdf.add_text(margin, y, "My primary trauma response is: _________________________________", 'F2', 10)
    y -= 20
    pdf.add_text(margin, y, "It shows up most in these situations:", 'F1', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(margin, y, rmargin, y, 0.5, 0.5)
        y -= 16


    # === PAGE 5: Safety Plan ===
    pdf.new_page()
    pdf.add_centered_text(750, "MY VETERAN SAFETY PLAN", 'F2', 16)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 720
    pdf.add_text(margin, y, "Complete this plan NOW, while you are calm. When crisis hits, you", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "won't be able to think clearly - this plan does the thinking for you.", 'F1', 10)
    y -= 25

    pdf.add_filled_rect(margin, y - 25, rmargin - margin, 25, 0.9)
    pdf.add_text(margin + 5, y - 17, "VETERANS CRISIS LINE: 988 (Press 1) | Text: 838255 | Chat: VeteransCrisisLine.net", 'F2', 9)
    y -= 40

    pdf.add_text(margin, y, "1. WARNING SIGNS (What tells me a crisis is building?):", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_text(margin + 10, y, f"{chr(9744)}", 'F1', 10)
        pdf.add_line(margin + 25, y, rmargin, y, 0.5, 0.5)
        y -= 16
    y -= 10

    pdf.add_text(margin, y, "2. MY BATTLE BUDDY (who I can call anytime):", 'F2', 10)
    y -= 16
    pdf.add_text(margin + 10, y, "Name: _________________________ Phone: _________________________", 'F1', 10)
    y -= 16
    pdf.add_text(margin + 10, y, "Name: _________________________ Phone: _________________________", 'F1', 10)
    y -= 22

    pdf.add_text(margin, y, "3. INTERNAL COPING (things I can do alone):", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_text(margin + 10, y, f"{chr(9744)}", 'F1', 10)
        pdf.add_line(margin + 25, y, rmargin, y, 0.5, 0.5)
        y -= 16
    y -= 10

    pdf.add_text(margin, y, "4. SAFE PLACES I CAN GO:", 'F2', 10)
    y -= 16
    pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
    y -= 16
    pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
    y -= 22

    pdf.add_text(margin, y, "5. PROFESSIONAL SUPPORT:", 'F2', 10)
    y -= 16
    pdf.add_text(margin + 10, y, "VA Therapist: _________________________ Phone: ______________", 'F1', 10)
    y -= 16
    pdf.add_text(margin + 10, y, "Vet Center: __________________________ Phone: ______________", 'F1', 10)
    y -= 16
    pdf.add_text(margin + 10, y, "Chaplain: ___________________________ Phone: ______________", 'F1', 10)
    y -= 22

    pdf.add_text(margin, y, "6. MAKING MY ENVIRONMENT SAFE:", 'F2', 10)
    y -= 16
    pdf.add_text(margin + 10, y, "Firearms secured: Yes / No   Location of safe storage: _______________", 'F1', 10)
    y -= 16
    pdf.add_text(margin + 10, y, "Medications secured: Yes / No   Alcohol removed: Yes / No", 'F1', 10)
    y -= 22

    pdf.add_text(margin, y, "7. MY REASON TO STAY:", 'F2', 10)
    y -= 16
    pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)


    # === PAGE 6: Grounding Techniques ===
    pdf.new_page()
    pdf.add_centered_text(750, "GROUNDING TECHNIQUES FOR HYPERVIGILANCE", 'F2', 14)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 720
    pdf.add_text(margin, y, "When your threat detection system is in overdrive, these techniques bring", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "you back to the present moment and signal SAFETY to your nervous system.", 'F1', 10)
    y -= 28

    pdf.add_text(margin, y, "5-4-3-2-1 SENSORY GROUNDING:", 'F2', 11)
    y -= 18
    pdf.add_text(margin + 10, y, "5 things I can SEE: ________________________________________________", 'F1', 9)
    y -= 15
    pdf.add_text(margin + 10, y, "4 things I can TOUCH: ______________________________________________", 'F1', 9)
    y -= 15
    pdf.add_text(margin + 10, y, "3 things I can HEAR: _______________________________________________", 'F1', 9)
    y -= 15
    pdf.add_text(margin + 10, y, "2 things I can SMELL: ______________________________________________", 'F1', 9)
    y -= 15
    pdf.add_text(margin + 10, y, "1 thing I can TASTE: _______________________________________________", 'F1', 9)
    y -= 28

    pdf.add_text(margin, y, "TACTICAL BREATHING (Box Breathing - adapted from combat breathing):", 'F2', 11)
    y -= 18
    pdf.add_text(margin + 10, y, "1. Inhale through nose: 4 counts (like taking cover)", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "2. Hold: 4 counts (steady your position)", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "3. Exhale through mouth: 4 counts (controlled release)", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "4. Hold empty: 4 counts (reset)", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "Repeat 4-6 cycles. This activates your parasympathetic nervous system.", 'F1', 10)
    y -= 28

    pdf.add_text(margin, y, "ORIENTING TO SAFETY:", 'F2', 11)
    y -= 18
    pdf.add_text(margin + 10, y, "1. Slowly look around the room. Name what you see out loud.", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "2. Identify evidence of safety: locked doors, familiar objects, time/date.", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "3. Say: 'I am [name]. I am in [place]. It is [year]. I am safe.'", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "4. Feel your feet on the ground. Press your back into the chair.", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "5. Hold something cold (ice cube) or textured (keys, coin).", 'F1', 10)
    y -= 28

    pdf.add_text(margin, y, "MY GO-TO GROUNDING TECHNIQUES (write what works best for you):", 'F2', 10)
    y -= 18
    for i in range(4):
        pdf.add_text(margin + 5, y, f"{i+1}.", 'F1', 10)
        pdf.add_line(margin + 20, y, rmargin, y, 0.5, 0.5)
        y -= 18


    # === PAGE 7: Trigger Mapping ===
    pdf.new_page()
    pdf.add_centered_text(750, "TRIGGER MAPPING", 'F2', 16)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 720
    pdf.add_text(margin, y, "Identifying triggers is the first step to managing them. Rate intensity 1-10.", 'F1', 10)
    y -= 25

    categories = [
        ("SOUND TRIGGERS", ["Fireworks/explosions:", "Helicopters/aircraft:", "Loud bangs/backfires:", "Yelling/arguing:"]),
        ("SMELL TRIGGERS", ["Diesel fuel/exhaust:", "Burning/smoke:", "Specific foods:", "Other:"]),
        ("SITUATION TRIGGERS", ["Crowded places:", "Driving (especially overpasses/debris):", "Being startled from behind:", "Confined spaces:"]),
    ]

    for cat_name, items in categories:
        pdf.add_text(margin, y, cat_name, 'F2', 11)
        y -= 5
        # Table header
        pdf.add_line(margin, y, rmargin, y, 0.5, 0.3)
        y -= 13
        pdf.add_text(margin + 5, y, "Trigger", 'F2', 8)
        pdf.add_text(320, y, "Intensity", 'F2', 8)
        pdf.add_text(400, y, "My Coping Plan", 'F2', 8)
        y -= 5
        pdf.add_line(margin, y, rmargin, y, 0.5, 0.3)
        y -= 14
        for item in items:
            pdf.add_text(margin + 5, y, item, 'F1', 9)
            pdf.add_text(320, y, "__ /10", 'F1', 9)
            pdf.add_line(400, y, rmargin - 5, y, 0.5, 0.5)
            y -= 16
        y -= 12

    pdf.add_text(margin, y, "OTHER TRIGGERS I'VE IDENTIFIED:", 'F2', 10)
    y -= 16
    for i in range(4):
        pdf.add_text(margin + 5, y, "Trigger: ___________________________ Intensity: __/10", 'F1', 9)
        y -= 14
        pdf.add_text(margin + 5, y, "Coping plan: ___________________________________________________", 'F1', 9)
        y -= 20


    # === PAGES 8-12: Cognitive Processing Therapy Worksheets ===
    stuck_points = [
        ("It was my fault.",
         "Many veterans blame themselves for events outside their control.",
         "What was actually within your control in that situation?",
         "What would you say to a fellow service member who said this?",
         "What training/orders/chaos factors were at play?",
         "Rewrite this belief with the evidence:"),
        ("I should have done more.",
         "Survivor's guilt is common. You did what you could with what you had.",
         "What DID you do? List your actions in that moment:",
         "Given the information you had at the time (not now), what was possible?",
         "Would you judge a squad mate this harshly for the same actions?",
         "A more balanced thought:"),
        ("The world is dangerous.",
         "Your brain learned this in a war zone. It was true THERE. Is it true HERE?",
         "List 5 safe moments from the past week:",
         "What percentage of your day involves actual threat? (be honest)",
         "What evidence do you have that you are safe right now?",
         "A more balanced thought:"),
        ("I can't trust anyone.",
         "Betrayal and loss in combat make trust feel impossible.",
         "Who has shown up for you, even in small ways?",
         "What is the difference between healthy caution and total isolation?",
         "What is one small trust you could extend this week?",
         "A more balanced thought:"),
        ("I don't deserve good things.",
         "Moral injury and guilt can convince you that you deserve punishment.",
         "If you don't deserve good things, why do you want them for others?",
         "What would your service mean if you never allowed yourself peace?",
         "What have you done since service that shows your character?",
         "A more balanced thought:"),
    ]

    for idx, (belief, context, q1, q2, q3, rewrite) in enumerate(stuck_points):
        pdf.new_page()
        pdf.add_centered_text(750, f"STUCK POINT #{idx+1}", 'F2', 14)
        pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
        y = 720

        pdf.add_filled_rect(margin, y - 28, rmargin - margin, 28, 0.92)
        pdf.add_centered_text(y - 18, f'"{belief}"', 'F5', 14)
        y -= 45

        pdf.add_text(margin, y, context, 'F4', 10)
        y -= 30

        pdf.add_text(margin, y, "CHALLENGING THIS STUCK POINT:", 'F2', 11)
        y -= 22

        prompts = [q1, q2, q3]
        for prompt in prompts:
            pdf.add_text(margin, y, prompt, 'F2', 9)
            y -= 16
            for i in range(3):
                pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
                y -= 15
            y -= 10

        pdf.add_text(margin, y, rewrite, 'F2', 10)
        y -= 16
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.4)
        y -= 16
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.4)
        y -= 16
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.4)
        y -= 25

        pdf.add_text(margin, y, "Belief strength BEFORE this exercise: ___/100", 'F1', 9)
        y -= 16
        pdf.add_text(margin, y, "Belief strength AFTER this exercise:  ___/100", 'F1', 9)


    # === PAGE 13: Anger Management for Veterans ===
    pdf.new_page()
    pdf.add_centered_text(750, "ANGER MANAGEMENT FOR VETERANS", 'F2', 14)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 720
    pdf.add_text(margin, y, "In the military, controlled aggression was a tool. In civilian life, that same", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "intensity can destroy relationships, careers, and freedom.", 'F1', 10)
    y -= 28

    pdf.add_text(margin, y, "THE ANGER ESCALATION LADDER:", 'F2', 11)
    y -= 18
    levels = [
        "10 - Violence / Destruction (point of no return)",
        " 8 - Yelling, threatening, slamming things",
        " 6 - Raised voice, clenched fists, pacing",
        " 4 - Irritation, short responses, muscle tension",
        " 2 - Mild annoyance, restlessness",
        " 0 - Calm baseline",
    ]
    for level in levels:
        pdf.add_text(margin + 15, y, level, 'F3', 9)
        y -= 14
    y -= 12

    pdf.add_text(margin, y, "MY EARLY WARNING SIGNS (catch it at 2-4, not 8-10):", 'F2', 10)
    y -= 16
    pdf.add_text(margin + 10, y, "Physical: ___________________________________________", 'F1', 9)
    y -= 15
    pdf.add_text(margin + 10, y, "Thoughts: ___________________________________________", 'F1', 9)
    y -= 15
    pdf.add_text(margin + 10, y, "Behaviors: __________________________________________", 'F1', 9)
    y -= 25

    pdf.add_text(margin, y, "TACTICAL PAUSE PROTOCOL:", 'F2', 11)
    y -= 18
    pdf.add_text(margin + 10, y, "1. STOP - Recognize the activation. Say 'I need a tactical pause.'", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "2. STEP BACK - Physically remove yourself for 20 minutes minimum.", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "3. BREATHE - Use tactical breathing (4-4-4-4 box breathing).", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "4. THINK - What am I actually angry about? Is this threat real?", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "5. RETURN - Come back when at 2-3, not 0 (that takes longer).", 'F1', 10)
    y -= 25

    pdf.add_text(margin, y, "ANGER LOG - Track your episodes this week:", 'F2', 10)
    y -= 16
    pdf.add_text(margin, y, "Date | Trigger | Level (0-10) | What I Did | What I Wish I Did", 'F2', 8)
    y -= 5
    pdf.add_line(margin, y, rmargin, y, 0.5, 0.3)
    y -= 15
    for i in range(5):
        pdf.add_line(margin, y, rmargin, y, 0.5, 0.5)
        y -= 18


    # === PAGE 14: Sleep & Nightmares Protocol ===
    pdf.new_page()
    pdf.add_centered_text(750, "SLEEP & NIGHTMARES PROTOCOL", 'F2', 14)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 720
    pdf.add_text(margin, y, "Sleep disturbance is one of the most common and debilitating PTSD symptoms.", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "Your brain keeps you on guard duty even when you need rest.", 'F1', 10)
    y -= 28

    pdf.add_text(margin, y, "SLEEP HYGIENE FOR PTSD:", 'F2', 11)
    y -= 18
    hygiene = [
        "Set a consistent wake time (more important than bedtime)",
        "Create a 'stand down' routine: dim lights 1 hour before bed",
        "No screens 30 min before sleep (blue light = alertness signal)",
        "Make bedroom feel SAFE: nightlight OK, door locks checked, clear sightlines",
        "No caffeine after 1400 hours",
        "Exercise daily but not within 3 hours of bedtime",
        "If not asleep in 20 min, get up - bed is for sleep only",
    ]
    for item in hygiene:
        pdf.add_text(margin + 10, y, f"{chr(9744)} {item}", 'F1', 9)
        y -= 14
    y -= 12

    pdf.add_text(margin, y, "IMAGERY REHEARSAL THERAPY (IRT) for Nightmares:", 'F2', 11)
    y -= 18
    pdf.add_text(margin, y, "Step 1: Write down your recurring nightmare (brief):", 'F1', 10)
    y -= 14
    for i in range(2):
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
        y -= 14
    y -= 8

    pdf.add_text(margin, y, "Step 2: Now REWRITE the ending. You are in control. Change it:", 'F1', 10)
    y -= 14
    for i in range(3):
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
        y -= 14
    y -= 8

    pdf.add_text(margin, y, "Step 3: Practice visualizing the NEW ending for 10 min before sleep.", 'F1', 10)
    y -= 20

    pdf.add_text(margin, y, "NIGHTMARE LOG:", 'F2', 10)
    y -= 14
    pdf.add_text(margin, y, "Date | Content (brief) | Intensity 1-10 | IRT Practiced?", 'F2', 8)
    y -= 5
    pdf.add_line(margin, y, rmargin, y, 0.5, 0.3)
    y -= 14
    for i in range(5):
        pdf.add_line(margin, y, rmargin, y, 0.5, 0.5)
        y -= 16


    # === PAGE 15: Reintegration Challenges ===
    pdf.new_page()
    pdf.add_centered_text(750, "REINTEGRATION CHALLENGES", 'F2', 14)
    pdf.add_centered_text(733, "Adjusting to Civilian Life", 'F4', 11)
    pdf.add_line(margin, 725, rmargin, 725, 1, 0.3)
    y = 705
    pdf.add_text(margin, y, "The transition from military to civilian life is one of the biggest adjustments", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "you'll ever make. It's OK to struggle with it.", 'F1', 10)
    y -= 25

    pdf.add_text(margin, y, "RATE YOUR CHALLENGE AREAS (1=managing well, 10=major struggle):", 'F2', 10)
    y -= 18
    challenges = [
        "Loss of structure/routine", "Loss of mission/purpose",
        "Relating to civilians who 'don't get it'", "Family relationships",
        "Finding meaningful employment", "Financial management",
        "Making decisions without chain of command", "Social isolation",
        "Feeling like I don't belong anywhere", "Missing my unit/brothers/sisters",
    ]
    for ch in challenges:
        pdf.add_text(margin + 10, y, f"___/10  {ch}", 'F1', 9)
        y -= 14
    y -= 12

    pdf.add_text(margin, y, "TOP 3 CHALLENGES I WANT TO WORK ON:", 'F2', 10)
    y -= 18
    for i in range(3):
        pdf.add_text(margin + 5, y, f"{i+1}. Challenge: _________________________________________________", 'F1', 9)
        y -= 14
        pdf.add_text(margin + 15, y, "One small step I can take this week: ________________________________", 'F1', 9)
        y -= 14
        pdf.add_text(margin + 15, y, "Who can help me with this: ________________________________________", 'F1', 9)
        y -= 20

    pdf.add_text(margin, y, "THINGS I MISS ABOUT SERVICE:", 'F2', 10)
    y -= 16
    pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
    y -= 16
    pdf.add_text(margin, y, "CIVILIAN EQUIVALENT I CAN BUILD:", 'F2', 10)
    y -= 16
    pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)


    # === PAGE 16: Moral Injury Exploration ===
    pdf.new_page()
    pdf.add_centered_text(750, "MORAL INJURY EXPLORATION", 'F2', 14)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 720
    pdf.add_text(margin, y, "Moral injury occurs when you participated in, witnessed, or failed to prevent", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "events that conflict with your deeply held moral beliefs and values.", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "This is different from PTSD - it's a wound to the soul, not just the mind.", 'F4', 10)
    y -= 28

    pdf.add_text(margin, y, "UNDERSTANDING MORAL INJURY:", 'F2', 11)
    y -= 18
    pdf.add_text(margin + 10, y, "- Things I did that conflict with my values", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "- Things I failed to do (acts of omission)", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "- Things I witnessed that shattered my worldview", 'F1', 10)
    y -= 15
    pdf.add_text(margin + 10, y, "- Betrayal by leadership or the system", 'F1', 10)
    y -= 28

    pdf.add_text(margin, y, "WITHOUT NAMING SPECIFIC EVENTS (unless you choose to):", 'F2', 10)
    y -= 20
    pdf.add_text(margin, y, "What value of mine was violated? ____________________________________", 'F1', 9)
    y -= 18
    pdf.add_text(margin, y, "What emotion comes up most? (shame/guilt/anger/betrayal/grief)", 'F1', 9)
    y -= 16
    pdf.add_line(margin, y, rmargin, y, 0.5, 0.5)
    y -= 22

    pdf.add_text(margin, y, "CONTEXT THAT MATTERS:", 'F2', 10)
    y -= 16
    pdf.add_text(margin, y, "What were the circumstances? (war, orders, split-second decisions, fog of war)", 'F1', 9)
    y -= 14
    for i in range(3):
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
        y -= 15
    y -= 10

    pdf.add_text(margin, y, "SELF-COMPASSION:", 'F2', 10)
    y -= 16
    pdf.add_text(margin, y, "Would you condemn a fellow veteran who did the same thing?  Yes / No", 'F1', 9)
    y -= 15
    pdf.add_text(margin, y, "What would you say to them? ________________________________________", 'F1', 9)
    y -= 15
    pdf.add_line(margin, y, rmargin, y, 0.5, 0.5)
    y -= 22

    pdf.add_text(margin, y, "MOVING FORWARD:", 'F2', 10)
    y -= 16
    pdf.add_text(margin, y, "What act of repair, service, or meaning-making could help? (not penance)", 'F1', 9)
    y -= 14
    for i in range(3):
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
        y -= 15


    # === PAGE 17: Building Purpose Post-Service ===
    pdf.new_page()
    pdf.add_centered_text(750, "BUILDING PURPOSE POST-SERVICE", 'F2', 14)
    pdf.add_centered_text(733, "Identity Beyond the Uniform", 'F4', 11)
    pdf.add_line(margin, 725, rmargin, 725, 1, 0.3)
    y = 705
    pdf.add_text(margin, y, "When your identity was built around service, who are you without it?", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "The answer: you are the VALUES behind the uniform, not the uniform itself.", 'F1', 10)
    y -= 28

    pdf.add_text(margin, y, "MILITARY VALUES I STILL CARRY:", 'F2', 11)
    y -= 18
    values = ["Loyalty", "Duty", "Integrity", "Service to others", "Discipline", "Courage"]
    for val in values:
        pdf.add_text(margin + 10, y, f"{chr(9744)} {val}: How I can express this now: ____________________________", 'F1', 9)
        y -= 16
    y -= 12

    pdf.add_text(margin, y, "STRENGTHS FROM MY SERVICE:", 'F2', 10)
    y -= 16
    pdf.add_text(margin, y, "Skills I developed: _________________________________________________", 'F1', 9)
    y -= 16
    pdf.add_text(margin, y, "Character traits forged: _____________________________________________", 'F1', 9)
    y -= 16
    pdf.add_text(margin, y, "What I'm proud of: _________________________________________________", 'F1', 9)
    y -= 25

    pdf.add_text(margin, y, "NEW MISSION STATEMENT:", 'F2', 11)
    y -= 18
    pdf.add_text(margin, y, "In service, your mission was given to you. Now you choose your own.", 'F4', 9)
    y -= 18
    pdf.add_text(margin, y, "I want to be remembered for: _________________________________________", 'F1', 9)
    y -= 16
    pdf.add_text(margin, y, "The people I want to serve now: ______________________________________", 'F1', 9)
    y -= 16
    pdf.add_text(margin, y, "My new mission: ___________________________________________________", 'F1', 9)
    y -= 16
    pdf.add_line(margin, y, rmargin, y, 0.5, 0.5)
    y -= 25

    pdf.add_text(margin, y, "AREAS TO EXPLORE:", 'F2', 10)
    y -= 16
    areas = [
        "Mentoring younger veterans or at-risk youth",
        "Volunteering with veteran organizations",
        "Education / new career aligned with my values",
        "Creative expression (writing, art, music)",
        "Physical challenges (sports, hiking, fitness goals)",
        "Community building / starting something new",
    ]
    for area in areas:
        pdf.add_text(margin + 10, y, f"{chr(9744)} {area}", 'F1', 9)
        y -= 14


    # === PAGES 18-22: Weekly Symptom Tracker (5 pages) ===
    for week in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"WEEKLY SYMPTOM TRACKER - WEEK {week}", 'F2', 14)
        pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
        y = 720
        pdf.add_text(margin, y, f"Dates: ______________ to ______________", 'F1', 10)
        y -= 25

        pdf.add_text(margin, y, "Rate each symptom daily (0=none, 1=mild, 2=moderate, 3=severe):", 'F1', 9)
        y -= 18

        # Header row
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        pdf.add_text(margin, y, "Symptom", 'F2', 8)
        x_start = 200
        for d_idx, day in enumerate(days):
            pdf.add_text(x_start + d_idx * 50, y, day, 'F2', 8)
        y -= 5
        pdf.add_line(margin, y, rmargin, y, 0.5, 0.3)
        y -= 15

        symptoms = [
            "Nightmares",
            "Flashbacks",
            "Avoidance",
            "Hyperarousal",
            "Anger/Irritability",
            "Mood (low)",
            "Concentration",
            "Sleep quality",
        ]

        for symptom in symptoms:
            pdf.add_text(margin, y, symptom, 'F1', 8)
            for d_idx in range(7):
                pdf.add_text(x_start + d_idx * 50 + 5, y, "___", 'F1', 8)
            y -= 16

        y -= 10
        pdf.add_line(margin, y, rmargin, y, 0.5, 0.3)
        y -= 18

        pdf.add_text(margin, y, "WEEKLY TOTAL SCORE: _____ / 168", 'F2', 10)
        y -= 15
        pdf.add_text(margin, y, "(Lower is better. Track your progress over time.)", 'F4', 9)
        y -= 25

        pdf.add_text(margin, y, "BIGGEST TRIGGER THIS WEEK:", 'F2', 10)
        y -= 14
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
        y -= 20

        pdf.add_text(margin, y, "COPING STRATEGY THAT WORKED:", 'F2', 10)
        y -= 14
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
        y -= 20

        pdf.add_text(margin, y, "WHAT I'M PROUD OF THIS WEEK:", 'F2', 10)
        y -= 14
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
        y -= 20

        pdf.add_text(margin, y, "GOAL FOR NEXT WEEK:", 'F2', 10)
        y -= 14
        pdf.add_line(margin + 10, y, rmargin, y, 0.5, 0.5)
        y -= 20

        pdf.add_text(margin, y, "APPOINTMENTS/SUPPORT USED:", 'F2', 10)
        y -= 14
        pdf.add_text(margin + 10, y, f"{chr(9744)} Therapy  {chr(9744)} VA visit  {chr(9744)} Group  {chr(9744)} Battle buddy call  {chr(9744)} Exercise", 'F1', 9)


    # === PAGE 23: VA Resources & Crisis Lines ===
    pdf.new_page()
    pdf.add_centered_text(750, "VA RESOURCES & CRISIS LINES", 'F2', 16)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 715

    pdf.add_filled_rect(margin, y - 40, rmargin - margin, 40, 0.9)
    pdf.add_centered_text(y - 15, "VETERANS CRISIS LINE", 'F2', 14)
    pdf.add_centered_text(y - 33, "Call: 988 (Press 1)  |  Text: 838255  |  Chat: VeteransCrisisLine.net", 'F2', 10)
    y -= 58

    pdf.add_text(margin, y, "IMMEDIATE CRISIS RESOURCES:", 'F2', 12)
    y -= 20
    crisis = [
        ("Veterans Crisis Line", "988 (Press 1)"),
        ("Crisis Text Line", "Text 838255"),
        ("Military OneSource", "1-800-342-9647"),
        ("National Suicide Prevention", "988"),
        ("SAMHSA Helpline", "1-800-662-4357"),
    ]
    for name, number in crisis:
        pdf.add_text(margin + 10, y, f"{name}:", 'F2', 10)
        pdf.add_text(300, y, number, 'F1', 10)
        y -= 16
    y -= 15

    pdf.add_text(margin, y, "VA MENTAL HEALTH SERVICES:", 'F2', 12)
    y -= 20
    va_services = [
        "VA PTSD Treatment Programs (CPT, PE, EMDR)",
        "Vet Centers (community-based counseling)",
        "VA Telehealth / Video Connect appointments",
        "VA Whole Health Program",
        "Residential PTSD treatment programs",
        "VA Caregiver Support Line: 1-855-260-3274",
    ]
    for svc in va_services:
        pdf.add_text(margin + 10, y, f"- {svc}", 'F1', 10)
        y -= 15
    y -= 15

    pdf.add_text(margin, y, "PEER SUPPORT & COMMUNITY:", 'F2', 12)
    y -= 20
    peer = [
        "Team Red White & Blue (physical/social activities)",
        "The Mission Continues (community service)",
        "Wounded Warrior Project",
        "Give an Hour (free mental health services)",
        "Cohen Veterans Network (free/low-cost therapy)",
        "IAVA (Iraq and Afghanistan Veterans of America)",
    ]
    for p in peer:
        pdf.add_text(margin + 10, y, f"- {p}", 'F1', 10)
        y -= 15
    y -= 15

    pdf.add_text(margin, y, "MY LOCAL VA FACILITY:", 'F2', 10)
    y -= 16
    pdf.add_text(margin + 10, y, "Name: _________________________________ Phone: _________________", 'F1', 9)
    y -= 16
    pdf.add_text(margin + 10, y, "My provider: ___________________________ Next appt: ______________", 'F1', 9)


    # === PAGE 24: My Recovery Commitment ===
    pdf.new_page()
    pdf.add_centered_text(750, "MY RECOVERY COMMITMENT", 'F2', 16)
    pdf.add_line(margin, 742, rmargin, 742, 1, 0.3)
    y = 715

    pdf.add_text(margin, y, "Recovery is not a sign of weakness. It is the bravest mission you will ever", 'F4', 11)
    y -= 16
    pdf.add_text(margin, y, "undertake. You survived the battlefield. Now choose to thrive beyond it.", 'F4', 11)
    y -= 35

    pdf.add_filled_rect(margin, y - 280, rmargin - margin, 280, 0.95)
    box_y = y - 20

    pdf.add_centered_text(box_y, "I, _________________________________, commit to my recovery.", 'F2', 11)
    box_y -= 30
    pdf.add_text(margin + 20, box_y, "I acknowledge that:", 'F2', 10)
    box_y -= 20
    commitments = [
        "PTSD is a wound, not a weakness, and I deserve to heal.",
        "Recovery is not linear - setbacks are part of the process.",
        "Asking for help is a sign of strength, not failure.",
        "I am more than my worst moment in service.",
        "My family and loved ones deserve the best version of me.",
        "I have survived 100% of my worst days so far.",
    ]
    for c in commitments:
        pdf.add_text(margin + 30, box_y, f"{chr(9744)} {c}", 'F1', 9)
        box_y -= 16
    box_y -= 15

    pdf.add_text(margin + 20, box_y, "My commitment to myself:", 'F2', 10)
    box_y -= 16
    pdf.add_line(margin + 30, box_y, rmargin - 30, box_y, 0.5, 0.5)
    box_y -= 16
    pdf.add_line(margin + 30, box_y, rmargin - 30, box_y, 0.5, 0.5)
    box_y -= 25

    pdf.add_text(margin + 20, box_y, "Signed: _________________________  Date: _______________", 'F1', 10)

    y -= 310
    pdf.add_centered_text(y, "REMEMBER:", 'F2', 12)
    y -= 22
    pdf.add_centered_text(y, "You didn't fight alone overseas.", 'F4', 11)
    y -= 18
    pdf.add_centered_text(y, "You don't have to fight alone at home.", 'F4', 11)
    y -= 35
    pdf.add_centered_text(y, "If you are in crisis right now:", 'F2', 10)
    y -= 18
    pdf.add_centered_text(y, "Veterans Crisis Line: 988 (Press 1)", 'F2', 12)
    y -= 18
    pdf.add_centered_text(y, "You are not broken. You are not beyond help. You matter.", 'F4', 10)

    # === PAGES 25-30: Additional journal/notes pages ===
    for pg in range(25, 31):
        pdf.new_page()
        pdf.add_centered_text(750, "RECOVERY JOURNAL", 'F2', 14)
        pdf.add_text(margin, 730, f"Page {pg - 24} of 6", 'F1', 9)
        pdf.add_line(margin, 725, rmargin, 725, 0.5, 0.3)
        pdf.add_text(margin, 710, "Date: ______________", 'F1', 9)
        pdf.add_text(margin, 692, "How am I feeling today (0-10)? ___  What happened:", 'F1', 9)
        y = 675
        for i in range(30):
            pdf.add_line(margin, y, rmargin, y, 0.5, 0.6)
            y -= 20

    # Save the PDF
    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book166_PTSD_Workbook_Veterans.pdf')
    print("Book166_PTSD_Workbook_Veterans.pdf created successfully!")

if __name__ == "__main__":
    create_book()
