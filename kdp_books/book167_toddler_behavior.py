"""
Book 167: The Toddler Behavior Workbook
Gentle Parenting Solutions for Ages 1-4
Author: Daniel Tesfamariam
Trim: 6x9 inches (432x648 points), 25 pages
"""

from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    margin = 50
    pw = 432 - 2 * margin  # page width usable

    # ===== PAGE 1: Title Page =====
    pdf.new_page()
    pdf.add_centered_text(560, "THE TODDLER BEHAVIOR", 'F2', 22)
    pdf.add_centered_text(530, "WORKBOOK", 'F2', 22)
    pdf.add_line(100, 515, 332, 515, 2)
    pdf.add_centered_text(480, "Gentle Parenting Solutions", 'F4', 16)
    pdf.add_centered_text(458, "for Ages 1-4", 'F4', 16)
    pdf.add_centered_text(400, "Understanding Tantrums, Building Connection,", 'F1', 11)
    pdf.add_centered_text(384, "and Raising Emotionally Intelligent Children", 'F1', 11)
    pdf.add_centered_text(340, "Behavior Tracking | Emotion Coaching Scripts", 'F1', 10)
    pdf.add_centered_text(322, "Routine Charts | Gentle Boundary Setting", 'F1', 10)
    pdf.add_centered_text(304, "Self-Regulation Milestones | Parent Self-Care", 'F1', 10)
    pdf.add_filled_rect(130, 220, 172, 30, 0.85)
    pdf.add_centered_text(232, "Daniel Tesfamariam", 'F2', 14)
    pdf.add_centered_text(180, "A Practical Workbook for Parents & Caregivers", 'F1', 10)
    pdf.add_centered_text(100, "Ages 1-4 | Gentle Parenting Approach", 'F1', 9, 0.4)

    # ===== PAGE 2: Copyright =====
    pdf.new_page()
    pdf.add_centered_text(580, "Copyright Notice", 'F2', 14)
    pdf.add_line(50, 570, 382, 570, 0.5)
    y = 540
    copyright_lines = [
        "The Toddler Behavior Workbook:",
        "Gentle Parenting Solutions for Ages 1-4",
        "",
        "Copyright (c) 2025 Daniel Tesfamariam",
        "All rights reserved.",
        "",

        "No part of this publication may be reproduced, distributed,",
        "or transmitted in any form without prior written permission.",
        "",
        "This workbook is intended for personal use only.",
        "It is not a substitute for professional therapy or",
        "medical advice. If your child is experiencing severe",
        "behavioral challenges, please consult a pediatrician",
        "or child psychologist.",
        "",
        "First Edition, 2025",
        "Published independently via KDP",
        "",
        "For bulk orders or licensing inquiries:",
        "Contact the author through Amazon."
    ]
    for line in copyright_lines:
        pdf.add_text(margin, y, line, 'F1', 10)
        y -= 18

    # ===== PAGE 3: Understanding Toddler Brain Development =====
    pdf.new_page()
    pdf.add_centered_text(610, "Understanding Toddler Brain Development", 'F2', 14)
    pdf.add_line(50, 600, 382, 600, 1)
    y = 575
    brain_content = [
        ("Why Their Brain Is Different From Ours:", 'F2', 11),
        ("", 'F1', 10),
        ("The prefrontal cortex - the part of the brain responsible for", 'F1', 10),
        ("impulse control, emotional regulation, planning, and reasoning -", 'F1', 10),
        ("is NOT fully developed until approximately age 25.", 'F1', 10),
        ("", 'F1', 10),
        ("In toddlers (ages 1-4), this area is barely beginning to form.", 'F1', 10),
        ("This means your toddler literally CANNOT:", 'F1', 10),
        ("", 'F1', 10),
        ("  * Control impulses consistently", 'F1', 10),
        ("  * Manage big emotions without help", 'F1', 10),
        ("  * Think logically when upset", 'F1', 10),
        ("  * Understand consequences in the moment", 'F1', 10),
        ("  * See things from another person's perspective", 'F1', 10),
        ("", 'F1', 10),
        ("Why Tantrums Are Normal and Developmentally Appropriate:", 'F2', 11),
        ("", 'F1', 10),
        ("Tantrums are NOT a sign of bad parenting or a 'bad child.'", 'F1', 10),
        ("They are a sign that your child's emotional brain (the amygdala)", 'F1', 10),
        ("is working perfectly - it's sending big feelings that the", 'F1', 10),
        ("underdeveloped prefrontal cortex cannot yet regulate.", 'F1', 10),
        ("", 'F1', 10),
        ("Think of it this way: Your toddler has an adult-sized gas pedal", 'F1', 10),
        ("(emotions) but baby-sized brakes (self-regulation). They need", 'F1', 10),
        ("YOU to be their external brakes until their own develop.", 'F1', 10),
        ("", 'F1', 10),
        ("Key Takeaway:", 'F2', 11),
        ("Your job is not to stop tantrums. Your job is to help your", 'F1', 10),
        ("child feel safe while experiencing big emotions, and to model", 'F1', 10),
        ("the regulation skills they will eventually internalize.", 'F1', 10),
    ]
    for text, font, size in brain_content:
        if text:
            pdf.add_text(margin, y, text, font, size)
        y -= 16


    # ===== PAGE 4: Why Toddlers Have Tantrums =====
    pdf.new_page()
    pdf.add_centered_text(610, "Why Toddlers Have Tantrums", 'F2', 14)
    pdf.add_line(50, 600, 382, 600, 1)
    y = 575
    tantrum_reasons = [
        ("1. Big Emotions, Small Toolbox", 'F2', 11),
        ("Toddlers feel emotions just as intensely as adults - anger, joy,", 'F1', 10),
        ("frustration, fear - but they have almost NO tools to manage them.", 'F1', 10),
        ("They haven't learned words for feelings, deep breathing, or", 'F1', 10),
        ("walking away. A tantrum IS their only tool right now.", 'F1', 10),
        ("", 'F1', 10),
        ("2. Communication Frustration", 'F2', 11),
        ("Your toddler knows what they want but often cannot express it.", 'F1', 10),
        ("Imagine being in a foreign country where nobody understands you -", 'F1', 10),
        ("that frustration is what your toddler feels daily. Limited", 'F1', 10),
        ("vocabulary + big needs = explosive behavior.", 'F1', 10),
        ("", 'F1', 10),
        ("3. Independence vs. Capability Gap", 'F2', 11),
        ("Toddlers desperately want to do things themselves (pour milk,", 'F1', 10),
        ("put on shoes, climb high) but their motor skills and cognitive", 'F1', 10),
        ("abilities haven't caught up to their desires. This gap between", 'F1', 10),
        ("'I want to' and 'I can't yet' creates intense frustration.", 'F1', 10),
        ("", 'F1', 10),
        ("4. Sensory Overload", 'F2', 11),
        ("Toddler nervous systems are still developing. Loud noises,", 'F1', 10),
        ("bright lights, crowds, new textures, or too many transitions", 'F1', 10),
        ("can overwhelm their system. When overwhelmed, they shut down", 'F1', 10),
        ("or explode - this is a protective nervous system response,", 'F1', 10),
        ("not misbehavior.", 'F1', 10),
        ("", 'F1', 10),
        ("Remember:", 'F2', 11),
        ("Behind every challenging behavior is an unmet need or an", 'F1', 10),
        ("underdeveloped skill. Our job is to figure out which one", 'F1', 10),
        ("and help - not punish.", 'F1', 10),
    ]
    for text, font, size in tantrum_reasons:
        if text:
            pdf.add_text(margin, y, text, font, size)
        y -= 16

    # ===== PAGE 5: Tantrum Response Flowchart =====
    pdf.new_page()
    pdf.add_centered_text(610, "Tantrum Response Flowchart", 'F2', 14)
    pdf.add_line(50, 600, 382, 600, 1)
    y = 575
    pdf.add_text(margin, y, "Follow these steps when your toddler is having a tantrum:", 'F1', 10)
    y -= 25

    steps = [
        ("STEP 1: Is My Child Safe?", "Check for physical danger. Move objects, move child if needed."),
        ("STEP 2: Am I Calm?", "Take 3 deep breaths. You cannot regulate a child if dysregulated."),
        ("STEP 3: Get Close & Low", "Kneel to their level. Open body language. Soft eyes."),
        ("STEP 4: Validate the Emotion", "Name what they feel: 'You're really frustrated right now.'"),
        ("STEP 5: Set the Boundary (if needed)", "'I won't let you hit. Hitting hurts. I'm keeping everyone safe.'"),
        ("STEP 6: Wait", "Do not rush. Do not lecture. Be present. Let the storm pass."),
        ("STEP 7: Co-Regulate", "Offer comfort: hug, rocking, humming. Match their breathing."),
        ("STEP 8: Reconnect After", "Once calm: 'That was hard. I'm here. Let's figure this out.'"),
    ]
    for title, desc in steps:
        pdf.add_filled_rect(margin, y - 5, pw, 32, 0.92)
        pdf.add_text(margin + 5, y + 14, title, 'F2', 10)
        pdf.add_text(margin + 5, y, desc, 'F1', 9)
        y -= 45

    y -= 10
    pdf.add_text(margin, y, "Key Principles:", 'F2', 10)
    y -= 16
    pdf.add_text(margin, y, "* Connection before correction", 'F1', 9)
    y -= 14
    pdf.add_text(margin, y, "* All feelings are allowed; not all behaviors are allowed", 'F1', 9)
    y -= 14
    pdf.add_text(margin, y, "* You are the calm in their storm", 'F1', 9)


    # ===== PAGES 6-10: Emotion Coaching Scripts (2 scenarios per page) =====
    scenarios = [
        ("Hitting", "Angry, frustrated, overwhelmed",
         "I won't let you hit. You're mad! You can stomp your feet or hit this pillow.",
         "Stop hitting! What's wrong with you? Bad boy/girl!",
         "Block the hit gently. Stay calm. Offer an alternative physical outlet."),
        ("Biting", "Frustrated, overstimulated, teething pain, exploring",
         "Ouch, biting hurts! You're frustrated. Let's find something safe to bite.",
         "Bite them back so they know how it feels!",
         "Offer a teething toy. Remove from situation briefly. Stay neutral."),
        ("Not Sharing", "Possessive (developmentally normal), anxious about losing things",
         "You're not ready to share that yet. That's okay. When you're done, it will be Maya's turn.",
         "Share right now or I'm taking it away!",
         "Teach turn-taking, not forced sharing. Use a timer for turns."),
        ("Bedtime Resistance", "Fear of separation, not tired, need for control",
         "I know you don't want bedtime. It's hard to stop playing. Would you like one more story or one more song?",
         "Get in bed NOW or no dessert tomorrow!",
         "Offer limited choices. Keep routine consistent. Stay boring but present."),
        ("Food Refusal", "Asserting autonomy, sensory sensitivity, not hungry",
         "You don't have to eat it. Your tummy will tell you when it's hungry.",
         "You're not leaving this table until you finish!",
         "Offer food without pressure. Let them explore. No short-order cooking."),
        ("Separation Anxiety", "Fear, insecurity, developmental phase",
         "You're scared I'm leaving. I always come back. Let's do our special goodbye.",
         "Just stop crying, I'll be right back! (while sneaking out)",
         "Create a goodbye ritual. Never sneak away. Keep goodbyes short and confident."),
        ("Sibling Conflict", "Jealousy, need for attention, boundary testing",
         "You both want the truck. That's hard! Let's figure this out together.",
         "Why can't you just get along? Be nice to your sister!",
         "Sportscaster the conflict. Don't take sides. Coach problem-solving."),
        ("Public Meltdowns", "Overstimulated, hungry, tired, embarrassed",
         "This is too much right now. Let's find a quiet spot together.",
         "Everyone is looking at us. Stop it right now!",
         "Leave if possible. Ignore stares. Your child's needs > strangers' opinions."),
        ("Whining", "Unmet need, wants connection, tired, doesn't know how to ask",
         "I want to help you. Can you use your regular voice to tell me?",
         "I can't hear you when you whine! Stop that voice!",
         "Model the tone you want. Don't shame. Meet the underlying need."),
        ("Defiance", "Asserting independence, testing boundaries, power struggle",
         "You don't want to put your shoes on. I hear you. We need shoes outside. Red ones or blue ones?",
         "Because I said so! Do it now or else!",
         "Offer choices within boundaries. Make it playful. Avoid power struggles."),
    ]

    for i in range(0, 10, 2):
        pdf.new_page()
        page_num = (i // 2) + 1
        pdf.add_centered_text(610, f"Emotion Coaching Scripts (Page {page_num} of 5)", 'F2', 13)
        pdf.add_line(50, 600, 382, 600, 1)

        y = 580
        for j in range(2):
            idx = i + j
            if idx >= len(scenarios):
                break
            name, feeling, say, not_say, do_action = scenarios[idx]

            pdf.add_filled_rect(margin, y - 5, pw, 18, 0.85)
            pdf.add_text(margin + 5, y, f"Scenario: {name}", 'F2', 11)
            y -= 22

            pdf.add_text(margin, y, f"What they're feeling: {feeling}", 'F4', 9)
            y -= 16

            pdf.add_text(margin, y, "What to SAY:", 'F2', 9)
            y -= 13
            pdf.add_text(margin + 10, y, f'"{say}"', 'F1', 9)
            y -= 16

            pdf.add_text(margin, y, "What NOT to say:", 'F2', 9)
            y -= 13
            pdf.add_text(margin + 10, y, f'"{not_say}"', 'F1', 9)
            y -= 16

            pdf.add_text(margin, y, "What to DO:", 'F2', 9)
            y -= 13
            pdf.add_text(margin + 10, y, do_action, 'F1', 9)
            y -= 30


    # ===== PAGE 11: Positive Reinforcement Tracker =====
    pdf.new_page()
    pdf.add_centered_text(610, "Positive Reinforcement Tracker", 'F2', 14)
    pdf.add_line(50, 600, 382, 600, 1)
    y = 580
    pdf.add_text(margin, y, "Notice and name the good! Catch them being kind, patient, brave.", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "Specific praise > generic praise. 'You waited so patiently!' > 'Good job!'", 'F1', 9)
    y -= 25

    # Table header
    col1 = margin
    col2 = margin + 130
    col3 = margin + 260
    row_h = 28

    pdf.add_filled_rect(col1, y - 5, pw, 20, 0.8)
    pdf.add_text(col1 + 5, y, "Behavior Noticed", 'F2', 9)
    pdf.add_text(col2 + 5, y, "Praise Given", 'F2', 9)
    pdf.add_text(col3 + 5, y, "Child's Response", 'F2', 9)
    y -= 25

    for row in range(15):
        pdf.add_rect(col1, y - 5, 130, row_h, 0.5, 0.3)
        pdf.add_rect(col2, y - 5, 130, row_h, 0.5, 0.3)
        pdf.add_rect(col3, y - 5, pw - 260, row_h, 0.5, 0.3)
        y -= row_h

    y -= 15
    pdf.add_text(margin, y, "Tips: Be specific, immediate, and genuine. Describe the behavior, not the child.", 'F1', 8)

    # ===== PAGE 12: Daily Routine Chart Builder =====
    pdf.new_page()
    pdf.add_centered_text(610, "Daily Routine Chart Builder", 'F2', 14)
    pdf.add_line(50, 600, 382, 600, 1)
    y = 580
    pdf.add_text(margin, y, "Toddlers thrive on predictability. Build your visual schedule below:", 'F1', 10)
    y -= 25

    routines = [
        ("MORNING", ["Wake up time: ___:___", "Diaper/potty", "Get dressed", "Breakfast", "Brush teeth"]),
        ("MIDDAY", ["Morning activity/outing", "Snack time: ___:___", "Free play", "Lunch time: ___:___", "Quiet time/nap: ___:___"]),
        ("AFTERNOON", ["Wake from nap: ___:___", "Snack time: ___:___", "Outdoor play", "Screen time (if any): ___ min", "Help with dinner"]),
        ("EVENING", ["Dinner time: ___:___", "Bath time", "Pajamas", "Story/song", "Lights out: ___:___"]),
    ]

    for section_name, items in routines:
        pdf.add_filled_rect(margin, y - 3, pw, 16, 0.85)
        pdf.add_text(margin + 5, y, section_name, 'F2', 10)
        y -= 20
        for item in items:
            pdf.add_text(margin + 15, y, f"[ ] {item}", 'F1', 9)
            y -= 14
        y -= 10

    y -= 5
    pdf.add_text(margin, y, "Notes: Adjust times to fit your family. Consistency matters more than perfection.", 'F1', 8)


    # ===== PAGES 13-22: Behavior Pattern Tracking (10 pages) =====
    for page_num in range(1, 11):
        pdf.new_page()
        pdf.add_centered_text(610, f"Behavior Pattern Tracking (Page {page_num} of 10)", 'F2', 13)
        pdf.add_line(50, 600, 382, 600, 1)
        y = 580

        fields = [
            ("Date:", 120),
            ("Time:", 120),
            ("Trigger (what happened right before):", 200),
            ("Behavior (what child did):", 200),
            ("My Response (what I said/did):", 200),
            ("What Worked:", 200),
            ("What Didn't Work:", 200),
            ("Pattern I Notice:", 200),
        ]

        for entry in range(2):
            if entry > 0:
                y -= 10
                pdf.add_line(margin, y, 382, y, 0.5, 0.5)
                y -= 15

            pdf.add_text(margin, y, f"Entry {entry + 1}", 'F2', 10)
            y -= 18

            for label, width in fields:
                pdf.add_text(margin, y, label, 'F2', 9)
                y -= 14
                pdf.add_line(margin + 5, y + 3, margin + width, y + 3, 0.5, 0.4)
                y -= 16

        y -= 10
        pdf.add_text(margin, y, "Reflection: What am I learning about my child's needs?", 'F4', 9, 0.3)
        pdf.add_line(margin, y - 10, 382, y - 10, 0.5, 0.4)


    # ===== PAGE 23: Gentle Boundary Setting Language =====
    pdf.new_page()
    pdf.add_centered_text(610, "Gentle Boundary Setting Language", 'F2', 14)
    pdf.add_line(50, 600, 382, 600, 1)
    y = 580
    pdf.add_text(margin, y, "How to Say No With Empathy:", 'F2', 11)
    y -= 20
    pdf.add_text(margin, y, "Boundaries are not mean. They are how children learn safety,", 'F1', 10)
    y -= 15
    pdf.add_text(margin, y, "structure, and what to expect. Deliver them with warmth and firmness.", 'F1', 10)
    y -= 25

    phrases = [
        ("Instead of: 'No!'", "Try: 'I won't let you do that. Here's what you CAN do...'"),
        ("Instead of: 'Stop it!'", "Try: 'I'm going to help you stop. Your body is telling me you need help.'"),
        ("Instead of: 'Because I said so'", "Try: 'The rule is ___ because it keeps you safe.'"),
        ("Instead of: 'You're being bad'", "Try: 'You're having a hard time. I'm here to help.'"),
        ("Instead of: 'If you don't stop...'", "Try: 'When you're ready, we can ___.'"),
        ("Instead of: 'Go to your room!'", "Try: 'Let's go to our calm-down spot together.'"),
        ("Instead of: 'I'm going to count to 3'", "Try: 'I can see you need more time. I'll wait with you.'"),
        ("Instead of: 'Big kids don't cry'", "Try: 'It's okay to cry. I'll be right here.'"),
        ("Instead of: 'You're fine'", "Try: 'That was scary/hard. Tell me about it.'"),
        ("Instead of: 'Share NOW'", "Try: 'When you're all done, it will be their turn.'"),
    ]

    for old, new in phrases:
        pdf.add_text(margin, y, old, 'F1', 9, 0.3)
        y -= 14
        pdf.add_text(margin + 10, y, new, 'F2', 9)
        y -= 20

    y -= 10
    pdf.add_text(margin, y, "Remember: Firm does not mean harsh. Kind does not mean permissive.", 'F4', 10)
    y -= 16
    pdf.add_text(margin, y, "You can hold a boundary AND hold your child's emotions at the same time.", 'F4', 10)

    # ===== PAGE 24: Self-Regulation Development Milestones =====
    pdf.new_page()
    pdf.add_centered_text(610, "Self-Regulation Development Milestones", 'F2', 14)
    pdf.add_line(50, 600, 382, 600, 1)
    y = 580
    pdf.add_text(margin, y, "What to Expect at Each Age (Every child is different!)", 'F2', 11)
    y -= 25

    milestones = [
        ("Age 1 (12-18 months):", [
            "* Beginning to understand 'no' (but cannot consistently follow it)",
            "* Tantrums begin as communication develops",
            "* Easily distracted/redirected",
            "* Separation anxiety peaks",
            "* Cannot share or take turns yet",
            "* Needs immediate comfort when distressed",
        ]),
        ("Age 2 (18-30 months):", [
            "* 'NO!' becomes a favorite word (healthy autonomy!)",
            "* Tantrums peak in frequency and intensity",
            "* Beginning to name some emotions with help",
            "* Parallel play (playing beside, not with, peers)",
            "* Can follow simple 1-step directions",
            "* Needs co-regulation for all big emotions",
        ]),
        ("Age 3 (30-42 months):", [
            "* Can start to use words for some feelings",
            "* Beginning to wait short periods",
            "* Starting cooperative play",
            "* Can follow 2-step directions",
            "* May use simple calming strategies with prompting",
            "* Tantrums decrease slightly but may get more intense",
        ]),
        ("Age 4 (42-54 months):", [
            "* Can identify basic emotions in self and others",
            "* Beginning to problem-solve simple conflicts",
            "* Can wait longer (with support)",
            "* Starting to internalize some regulation strategies",
            "* Can follow rules in structured settings",
            "* Still needs help with big emotions regularly",
        ]),
    ]

    for age_label, items in milestones:
        pdf.add_filled_rect(margin, y - 3, pw, 16, 0.88)
        pdf.add_text(margin + 5, y, age_label, 'F2', 10)
        y -= 20
        for item in items:
            pdf.add_text(margin + 10, y, item, 'F1', 9)
            y -= 13
        y -= 10


    # ===== PAGE 25: Parent Self-Care Check =====
    pdf.new_page()
    pdf.add_centered_text(610, "Parent Self-Care Check", 'F2', 14)
    pdf.add_line(50, 600, 382, 600, 1)
    y = 580
    pdf.add_text(margin, y, "Burnout Checklist - Check any that apply:", 'F2', 11)
    y -= 22

    burnout_items = [
        "I feel exhausted even after sleeping",
        "I dread waking up to another day of tantrums",
        "I yell more than I want to",
        "I feel guilty about my parenting daily",
        "I've lost interest in things I used to enjoy",
        "I feel touched out / overstimulated by my child",
        "I feel like I'm failing as a parent",
        "I have no time for myself at all",
        "I feel resentful toward my partner or child",
        "I cry more often than usual",
    ]

    for item in burnout_items:
        pdf.add_text(margin, y, f"[ ] {item}", 'F1', 10)
        y -= 18

    y -= 10
    pdf.add_text(margin, y, "If you checked 3+: You need support. This is not weakness.", 'F2', 10)
    y -= 20

    pdf.add_text(margin, y, "Self-Compassion Reminders:", 'F2', 11)
    y -= 20

    reminders = [
        "* You are not a bad parent for having hard days.",
        "* Your child's behavior is not a reflection of your worth.",
        "* Repair is always possible. You can always try again.",
        "* Asking for help is brave, not weak.",
        "* You cannot pour from an empty cup.",
        "* Progress is not linear - for you OR your toddler.",
        "* Good enough parenting IS good parenting.",
        "* Your child needs a regulated parent, not a perfect one.",
    ]

    for reminder in reminders:
        pdf.add_text(margin, y, reminder, 'F4', 10)
        y -= 16

    y -= 15
    pdf.add_filled_rect(margin, y - 5, pw, 40, 0.92)
    pdf.add_centered_text(y + 18, "You are doing harder work than anyone gives you credit for.", 'F5', 10)
    pdf.add_centered_text(y + 2, "Your child is lucky to have a parent who is trying this hard.", 'F5', 10)

    # ===== SAVE =====
    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book167_Toddler_Behavior_Guide.pdf')
    print("SUCCESS: Book167_Toddler_Behavior_Guide.pdf created successfully!")
    print("Title: THE TODDLER BEHAVIOR WORKBOOK - Gentle Parenting Solutions for Ages 1-4")
    print("Author: Daniel Tesfamariam")
    print("Pages: 25 | Size: 6x9 inches (432x648 points)")

if __name__ == "__main__":
    create_book()
