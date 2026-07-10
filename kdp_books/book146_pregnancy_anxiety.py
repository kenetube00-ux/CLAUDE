"""Book 146: Expecting & Anxious - A CBT Workbook for Pregnancy Anxiety"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "EXPECTING & ANXIOUS", 'F2', 22, 0)
    doc.add_centered_text(395, "A CBT Workbook for", 'F4', 15, 0.2)
    doc.add_centered_text(370, "Pregnancy Anxiety", 'F4', 15, 0.2)
    doc.add_centered_text(300, "Evidence-Based Tools for Managing", 'F1', 11, 0.3)
    doc.add_centered_text(280, "Worry During Pregnancy", 'F1', 11, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(500, "EXPECTING & ANXIOUS", 'F2', 14, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)
    doc.add_text(50, 410, "Not a substitute for prenatal care or mental health treatment.", 'F1', 9, 0.3)
    doc.add_text(50, 390, "If you are experiencing severe anxiety, tell your OB or midwife.", 'F2', 9, 0.3)

    # Page 3: Anxiety During Pregnancy is Common
    doc.new_page()
    doc.add_centered_text(590, "ANXIETY DURING PREGNANCY IS COMMON", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Up to 25% of pregnant women experience significant anxiety.", 'F1', 10, 0.2)
    doc.add_text(50, 537, "You are NOT alone. You are NOT a bad mom for feeling this way.", 'F2', 10, 0)
    y = 510
    doc.add_text(50, y, "Common pregnancy worries:", 'F1', 10, 0.2)
    y -= 18
    worries = ["Is the baby healthy?", "Will something go wrong during delivery?",
               "Am I eating/doing everything right?", "What if I'm a bad mother?",
               "Financial fears about supporting a baby", "Relationship changes",
               "Loss of identity/freedom", "History of miscarriage or loss"]
    for w in worries:
        doc.add_text(65, y, f"- {w}", 'F1', 9, 0.2)
        y -= 15
    y -= 10
    doc.add_text(50, y, "When worry becomes TOO MUCH:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "Constant dread, can't sleep, avoiding appointments, checking", 'F1', 9, 0.3)
    y -= 14
    doc.add_text(50, y, "obsessively, physical symptoms (racing heart, nausea beyond morning", 'F1', 9, 0.3)
    y -= 14
    doc.add_text(50, y, "sickness), intrusive thoughts about harm to baby.", 'F1', 9, 0.3)

    # Page 4: Cognitive Distortions in Pregnancy
    doc.new_page()
    doc.add_centered_text(590, "COGNITIVE DISTORTIONS IN PREGNANCY", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    distortions = [
        ("CATASTROPHIZING:", "'One glass of wine before I knew = my baby will have problems'"),
        ("WHAT-IFS:", "'What if the ultrasound shows something terrible?'"),
        ("PROBABILITY OVERESTIMATION:", "'I just KNOW something will go wrong with delivery'"),
        ("INTOLERANCE OF UNCERTAINTY:", "'I need to KNOW the baby is okay RIGHT NOW'"),
        ("SHOULD STATEMENTS:", "'I SHOULD be enjoying every moment of pregnancy'"),
        ("EMOTIONAL REASONING:", "'I feel anxious, so something must be wrong'")
    ]
    for name, example in distortions:
        doc.add_text(50, y, name, 'F2', 9, 0)
        y -= 14
        doc.add_text(55, y, example, 'F3', 8, 0.4)
        y -= 22

    # Pages 5-9: Thought Records (5 pages)
    for page_num in range(5):
        doc.new_page()
        doc.add_centered_text(590, f"PREGNANCY THOUGHT RECORD ({page_num+1}/5)", 'F2', 12, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 558
        doc.add_text(50, y, "Date: ________  Week of pregnancy: ___", 'F1', 9, 0.3)
        y -= 20
        doc.add_text(50, y, "Situation/Trigger: ________________________________________________", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(50, y, "Anxious thought: __________________________________________________", 'F1', 9, 0.3)
        y -= 16
        doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.3)
        y -= 20
        doc.add_text(50, y, "Distortion type: __________________________________________________", 'F1', 9, 0.3)
        y -= 20
        doc.add_text(50, y, "Anxiety level (0-10): ___", 'F1', 9, 0.3)
        y -= 20
        doc.add_text(50, y, "Evidence FOR this worry:", 'F2', 9, 0)
        y -= 16
        doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(50, y, "Evidence AGAINST this worry:", 'F2', 9, 0)
        y -= 16
        doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.3)
        y -= 16
        doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.3)
        y -= 20
        doc.add_text(50, y, "Balanced thought: _________________________________________________", 'F1', 9, 0.3)
        y -= 16
        doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.3)
        y -= 20
        doc.add_text(50, y, "Anxiety level AFTER (0-10): ___", 'F1', 9, 0.3)
        y -= 20
        doc.add_text(50, y, "What I can CONTROL: _______________________________________________", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(50, y, "What I need to LET GO: ____________________________________________", 'F1', 9, 0.3)

    # Page 10: Relaxation for Pregnant Women
    doc.new_page()
    doc.add_centered_text(590, "RELAXATION FOR PREGNANT WOMEN", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "BODY SCAN (Safe in all trimesters):", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "Lie on left side with pillow between knees. Breathe slowly.", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Scan from toes to head, releasing tension in each area.", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "When you reach your belly, send love and calm to baby.", 'F1', 9, 0.2)
    y -= 22
    doc.add_text(50, y, "SAFE PLACE VISUALIZATION:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "Close eyes. Imagine a place where you feel completely safe.", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "What do you see? Hear? Smell? Feel? Breathe here for 5 min.", 'F1', 9, 0.2)
    y -= 22
    doc.add_text(50, y, "CONNECTING WITH BABY:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "Place hands on belly. Breathe deeply. Tell baby:", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "'We are safe. We are together. I love you already.'", 'F4', 9, 0.3)
    y -= 22
    doc.add_text(50, y, "PRACTICE LOG:", 'F2', 10, 0)
    y -= 18
    for i in range(6):
        doc.add_text(50, y, "Date: _______  Technique: ____________  Anxiety before/after: __/__", 'F1', 8, 0.3)
        y -= 16

    # Page 11: Birth Anxiety Prep
    doc.new_page()
    doc.add_centered_text(590, "BIRTH ANXIETY PREPARATION", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "My specific fears about birth:", 'F2', 10, 0)
    y -= 18
    for i in range(3):
        doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 9, 0.3)
        y -= 16
    y -= 10
    doc.add_text(50, y, "Things I CAN control about my birth:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "(birth plan preferences, support person, environment)", 'F3', 8, 0.4)
    y -= 16
    for i in range(3):
        doc.add_text(50, y, f"_______________________________________________________________", 'F1', 9, 0.3)
        y -= 16
    y -= 10
    doc.add_text(50, y, "Things I CANNOT control (practice releasing):", 'F2', 10, 0)
    y -= 16
    for i in range(3):
        doc.add_text(50, y, f"_______________________________________________________________", 'F1', 9, 0.3)
        y -= 16
    y -= 10
    doc.add_text(50, y, "My coping plan for labor:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "Breathing technique: _____________________________________________", 'F1', 9, 0.3)
    y -= 16
    doc.add_text(50, y, "Mantras: _________________________________________________________", 'F1', 9, 0.3)
    y -= 16
    doc.add_text(50, y, "Support person & their role: _____________________________________", 'F1', 9, 0.3)

    # Page 12: Postpartum Anxiety Prevention
    doc.new_page()
    doc.add_centered_text(590, "POSTPARTUM ANXIETY PREVENTION PLAN", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Planning NOW reduces risk later:", 'F2', 10, 0)
    y -= 20
    doc.add_text(50, y, "My support team after birth:", 'F1', 10, 0.2)
    y -= 16
    for i in range(3):
        doc.add_text(50, y, f"  Name: _________________  How they'll help: __________________", 'F1', 8, 0.3)
        y -= 16
    y -= 10
    doc.add_text(50, y, "Warning signs to watch for:", 'F2', 10, 0)
    y -= 16
    signs = ["Excessive worry about baby's safety", "Inability to sleep (even when baby sleeps)",
             "Intrusive scary thoughts", "Needing to check baby constantly",
             "Irritability/rage", "Physical symptoms (racing heart, nausea)"]
    for s in signs:
        doc.add_text(60, y, f"- {s}", 'F1', 8, 0.3)
        y -= 14
    y -= 10
    doc.add_text(50, y, "If I notice these, I will: _________________________________________", 'F1', 9, 0.2)
    y -= 18
    doc.add_text(50, y, "Provider to call: _________________________________________________", 'F1', 9, 0.2)

    # Page 13: Baby Health Worry
    doc.new_page()
    doc.add_centered_text(590, "BABY HEALTH WORRY MANAGEMENT", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Rules for Dr. Google:", 'F2', 10, 0)
    y -= 16
    rules = ["Set a time limit (10 min max)", "Only use trusted sources (OB's recommendations)",
             "If searching makes anxiety WORSE, close the browser",
             "Write down questions for your next appointment instead",
             "One search, then STOP. Don't go down the rabbit hole."]
    for r in rules:
        doc.add_text(60, y, f"- {r}", 'F1', 9, 0.2)
        y -= 15
    y -= 15
    doc.add_text(50, y, "Questions for my next appointment:", 'F2', 10, 0)
    y -= 18
    for i in range(6):
        doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 9, 0.3)
        y -= 16
    y -= 10
    doc.add_text(50, y, "Reassurances from my provider: _____________________________________", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.3)

    # Page 14: Mindful Pregnancy
    doc.new_page()
    doc.add_centered_text(590, "MINDFUL PREGNANCY PRACTICES", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    practices = [
        ("Morning intention:", "Before getting up, place hands on belly and set one calm intention."),
        ("Mindful eating:", "One meal/day, eat slowly. Notice textures, flavors. Thank your body."),
        ("Movement:", "Gentle yoga, walking, swimming. Focus on how movement FEELS, not looks."),
        ("Kick counts as meditation:", "During kick counts, breathe and connect. Not just counting - bonding."),
        ("Evening gratitude:", "3 things you're grateful for today. One about your body, one about baby.")
    ]
    for title, desc in practices:
        doc.add_text(50, y, title, 'F2', 9, 0)
        y -= 14
        doc.add_text(55, y, desc, 'F1', 9, 0.3)
        y -= 22

    # Pages 15-22: Weekly Anxiety Tracker (8 pages)
    for week in range(8):
        doc.new_page()
        doc.add_centered_text(590, f"WEEKLY ANXIETY TRACKER - Week {week+1}", 'F2', 11, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 558
        doc.add_text(50, y, f"Week of: __________  Pregnancy week: ___", 'F1', 9, 0.3)
        y -= 18
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        doc.add_filled_rect(50, y-2, 332, 14, 0.85)
        doc.add_text(52, y, "Day", 'F2', 7, 0)
        doc.add_text(80, y, "Anxiety (0-10)", 'F2', 7, 0)
        doc.add_text(165, y, "Main Trigger", 'F2', 7, 0)
        doc.add_text(280, y, "Coping Used", 'F2', 7, 0)
        y -= 16
        for d in days:
            doc.add_text(52, y, d, 'F1', 8, 0.2)
            doc.add_rect(80, y-3, 60, 13)
            doc.add_rect(165, y-3, 110, 13)
            doc.add_rect(280, y-3, 102, 13)
            y -= 16
        y -= 10
        doc.add_text(50, y, "Baby connection moment this week:", 'F2', 9, 0)
        y -= 16
        doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(50, y, "Something I'm looking forward to: __________________________________", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(50, y, "Self-care I did: ___________________________________________________", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(50, y, "Avg anxiety this week: ___  Compared to last week: better/same/worse", 'F1', 9, 0.3)

    # Page 23: Birth Preferences
    doc.new_page()
    doc.add_centered_text(590, "MY BIRTH PREFERENCES", 'F2', 14, 0)
    doc.add_centered_text(572, "(Not a rigid plan - preferences reduce anxiety)", 'F1', 9, 0.3)
    doc.add_line(50, 562, 382, 562, 1, 0.5)
    y = 540
    prefs = [
        ("Support people:", "________________________________________"),
        ("Environment:", "________________________________________"),
        ("Pain management preference:", "________________________________________"),
        ("Music/comfort items:", "________________________________________"),
        ("If plans change, I want:", "________________________________________"),
        ("After birth, I'd like:", "________________________________________"),
        ("Feeding plan:", "________________________________________")
    ]
    for label, blank in prefs:
        doc.add_text(50, y, f"{label} {blank}", 'F1', 9, 0.2)
        y -= 22
    y -= 10
    doc.add_text(50, y, "My mantra for birth: ______________________________________________", 'F2', 9, 0)
    y -= 20
    doc.add_text(50, y, "Reminder: Healthy mom + healthy baby = successful birth, no matter how.", 'F4', 9, 0.2)

    # Page 24: Support Network
    doc.new_page()
    doc.add_centered_text(590, "SUPPORT NETWORK FOR NEW MOTHERHOOD", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Line up support NOW (before baby comes):", 'F2', 10, 0)
    y -= 20
    support = [
        "Person who will bring meals:", "Person who will help with older kids:",
        "Person I can call crying at 3am:", "Lactation consultant:",
        "Postpartum therapist (have number ready):", "Mom group/community:",
        "Partner's specific postpartum responsibilities:"
    ]
    for s in support:
        doc.add_text(50, y, f"{s}", 'F1', 9, 0.2)
        y -= 14
        doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
        y -= 18

    # Page 25: When to Seek Help
    doc.new_page()
    doc.add_centered_text(590, "WHEN TO SEEK HELP", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Talk to your provider if:", 'F2', 10, 0)
    y -= 18
    help_signs = ["Anxiety interferes with daily functioning",
                  "You can't sleep even when you have the chance",
                  "You're avoiding prenatal appointments out of fear",
                  "You have intrusive thoughts of harm (to self or baby)",
                  "You feel disconnected from the pregnancy",
                  "Physical symptoms that won't ease (racing heart, panic attacks)",
                  "You're using substances to cope"]
    for s in help_signs:
        doc.add_text(60, y, f"- {s}", 'F1', 9, 0.2)
        y -= 15
    y -= 15
    doc.add_text(50, y, "Resources:", 'F2', 10, 0)
    y -= 16
    resources = ["Postpartum Support International: 1-800-944-4773",
                 "Crisis Text Line: Text HOME to 741741",
                 "Your OB/midwife's after-hours number: ________________"]
    for r in resources:
        doc.add_text(50, y, f"  {r}", 'F1', 9, 0.2)
        y -= 16
    y -= 15
    doc.add_text(50, y, "Asking for help makes you a GOOD mom, not a weak one.", 'F2', 10, 0)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book146_Pregnancy_Anxiety_Workbook.pdf')
    print("Book146_Pregnancy_Anxiety_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
