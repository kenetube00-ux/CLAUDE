"""Book 143: Nourish - An Eating Disorder Recovery Journal"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "NOURISH", 'F2', 28, 0)
    doc.add_centered_text(395, "An Eating Disorder", 'F4', 16, 0.2)
    doc.add_centered_text(370, "Recovery Journal", 'F4', 16, 0.2)
    doc.add_centered_text(310, "You deserve to eat.", 'F4', 12, 0.3)
    doc.add_centered_text(290, "You deserve to heal.", 'F4', 12, 0.3)
    doc.add_centered_text(270, "You deserve to live fully.", 'F4', 12, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(500, "NOURISH", 'F2', 14, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)
    doc.add_text(50, 410, "This journal is not a substitute for professional ED treatment.", 'F1', 9, 0.3)
    doc.add_text(50, 380, "NEDA Helpline: 1-800-931-2237 | Crisis Text: Text NEDA to 741741", 'F2', 9, 0.3)
    doc.add_text(50, 360, "If you are in medical danger, go to the emergency room.", 'F1', 9, 0.3)

    # Page 3: Recovery is Possible
    doc.new_page()
    doc.add_centered_text(590, "RECOVERY IS POSSIBLE", 'F2', 16, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "If you're holding this journal, part of you wants to recover.", 'F4', 11, 0.2)
    doc.add_text(50, 535, "That part - however small - is enough to begin.", 'F4', 11, 0.2)
    y = 505
    doc.add_text(50, y, "Recovery means:", 'F2', 11, 0)
    y -= 20
    meanings = ["Eating is not a moral issue", "Your body deserves nourishment",
                "You are more than a number on a scale", "Food is not the enemy - the ED is",
                "Slip-ups are part of recovery, not failure"]
    for m in meanings:
        doc.add_text(65, y, f"- {m}", 'F1', 11, 0.2)
        y -= 18
    y -= 20
    doc.add_text(50, y, "This journal is a safe space. No calorie counts. No body measurements.", 'F2', 10, 0)
    y -= 18
    doc.add_text(50, y, "Just healing.", 'F2', 10, 0)

    # Page 4: ED Thoughts vs Healthy Thoughts
    doc.new_page()
    doc.add_centered_text(590, "ED THOUGHTS vs HEALTHY THOUGHTS", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Learning to tell the difference is key to recovery:", 'F1', 10, 0.2)
    y = 530
    doc.add_filled_rect(50, y+2, 165, 16, 0.85)
    doc.add_filled_rect(220, y+2, 165, 16, 0.85)
    doc.add_text(70, y+4, "ED VOICE SAYS:", 'F2', 9, 0)
    doc.add_text(240, y+4, "RECOVERY VOICE SAYS:", 'F2', 9, 0)
    y -= 20
    pairs = [
        ("You don't deserve to eat", "Everyone deserves food"),
        ("You'll get fat", "Your body needs fuel to live"),
        ("Skip this meal", "Skipping makes it harder"),
        ("You're disgusting", "You are worthy of love"),
        ("No one will love you at that weight", "Love isn't conditional on size"),
        ("Just one more day of restriction", "One more day hurts my recovery"),
        ("You ate too much", "I ate what my body needed")
    ]
    for ed, healthy in pairs:
        doc.add_text(52, y, ed, 'F3', 8, 0.3)
        doc.add_text(222, y, healthy, 'F4', 9, 0.2)
        y -= 22

    # Pages 5-7: Body Image Healing (3 pages)
    for page_num in range(3):
        doc.new_page()
        doc.add_centered_text(590, f"BODY IMAGE HEALING ({page_num+1}/3)", 'F2', 14, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 555
        if page_num == 0:
            doc.add_text(50, y, "Things my body DOES for me (not how it looks):", 'F2', 10, 0)
            y -= 20
            for i in range(8):
                doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 10, 0.2)
                y -= 20
        elif page_num == 1:
            doc.add_text(50, y, "A letter to my body:", 'F2', 10, 0)
            y -= 20
            doc.add_text(50, y, "Dear Body,", 'F4', 10, 0.2)
            y -= 18
            for i in range(16):
                doc.add_text(50, y, "_" * 52, 'F1', 10, 0.4)
                y -= 16
        else:
            doc.add_text(50, y, "Body neutrality statements (not positive - just NEUTRAL):", 'F2', 10, 0)
            y -= 20
            statements = ["My body carries me through the day", "My body is doing its best",
                         "I don't have to love my body to treat it well",
                         "My worth is not determined by my appearance",
                         "Bodies change. That's normal, not failure."]
            for s in statements:
                doc.add_text(60, y, f"- {s}", 'F4', 10, 0.2)
                y -= 18
            y -= 15
            doc.add_text(50, y, "My own body neutral statements:", 'F2', 10, 0)
            y -= 18
            for i in range(5):
                doc.add_text(50, y, "_" * 52, 'F1', 10, 0.4)
                y -= 16

    # Pages 8-12: Meal Planning (5 pages)
    for page_num in range(5):
        doc.new_page()
        doc.add_centered_text(590, f"MEAL PLANNING WITHOUT FEAR ({page_num+1}/5)", 'F2', 12, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 558
        doc.add_text(50, y, f"Day: _______________  Date: ___________", 'F1', 10, 0.2)
        y -= 25
        meals = ["Breakfast", "Morning Snack", "Lunch", "Afternoon Snack", "Dinner", "Evening Snack"]
        for meal in meals:
            doc.add_text(50, y, f"{meal}:", 'F2', 9, 0)
            y -= 16
            doc.add_text(50, y, "What I ate: _______________________________________________", 'F1', 9, 0.3)
            y -= 14
            doc.add_text(50, y, "How I felt before: _______ During: _______ After: _______", 'F1', 9, 0.3)
            y -= 14
            doc.add_text(50, y, "ED voice said: ____________________________________________", 'F1', 9, 0.3)
            y -= 14
            doc.add_text(50, y, "Recovery voice said: ______________________________________", 'F1', 9, 0.3)
            y -= 20

    # Page 13: Trigger Identification
    doc.new_page()
    doc.add_centered_text(590, "TRIGGER IDENTIFICATION", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "What triggers ED behaviors for me?", 'F2', 10, 0)
    y = 530
    trigger_cats = ["People:", "Places:", "Times of day:", "Emotions:", "Situations:", "Social media/images:"]
    for cat in trigger_cats:
        doc.add_text(50, y, cat, 'F2', 9, 0)
        doc.add_text(150, y, "________________________________________________", 'F1', 9, 0.3)
        y -= 25
    y -= 10
    doc.add_text(50, y, "My plan for when I'm triggered:", 'F2', 10, 0)
    y -= 20
    for i in range(4):
        doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 10, 0.2)
        y -= 20

    # Page 14: Coping with Urges
    doc.new_page()
    doc.add_centered_text(590, "COPING WITH URGES", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "When the urge hits, try these INSTEAD:", 'F2', 10, 0)
    y = 530
    alternatives = ["Call someone from my support list", "Write in this journal",
                   "Take a walk (not for burning calories - for fresh air)",
                   "Put on a comfort show", "Hold ice cubes", "Do a body scan meditation",
                   "Look at my 'reasons for recovery' page", "Text a friend",
                   "Draw/paint/create something", "Read recovery affirmations",
                   "Remind myself: the urge will pass in 15-20 minutes"]
    for a in alternatives:
        doc.add_text(60, y, f"- {a}", 'F1', 9, 0.2)
        y -= 16

    # Pages 15-17: Self-Compassion Letters (3 pages)
    for page_num in range(3):
        doc.new_page()
        doc.add_centered_text(590, f"SELF-COMPASSION LETTER ({page_num+1}/3)", 'F2', 13, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        prompts = [
            "Write to yourself after a hard day (with kindness, not judgment):",
            "Write to yourself about a slip-up (with grace, not punishment):",
            "Write to yourself about why you deserve recovery:"
        ]
        doc.add_text(50, 555, prompts[page_num], 'F4', 10, 0.2)
        y = 530
        for i in range(22):
            doc.add_text(50, y, "_" * 52, 'F1', 10, 0.4)
            y -= 18

    # Page 18: Body Gratitude
    doc.new_page()
    doc.add_centered_text(590, "BODY GRATITUDE PRACTICE", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Thank your body for what it DOES, not how it looks:", 'F1', 10, 0.2)
    y = 530
    body_parts = ["My hands:", "My legs:", "My heart:", "My brain:", "My stomach:",
                  "My lungs:", "My voice:", "My arms:", "My eyes:", "My whole body:"]
    for bp in body_parts:
        doc.add_text(50, y, f"{bp} I'm grateful because ___________________________", 'F1', 9, 0.2)
        y -= 22

    # Pages 19-21: Challenging Food Rules (3 pages)
    for page_num in range(3):
        doc.new_page()
        doc.add_centered_text(590, f"CHALLENGING FOOD RULES ({page_num+1}/3)", 'F2', 13, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 555
        for entry in range(2):
            doc.add_text(50, y, f"Food Rule #{page_num*2+entry+1}:", 'F2', 10, 0)
            y -= 18
            doc.add_text(50, y, "The rule: ____________________________________________________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Where did it come from? _______________________________________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Evidence this rule is HELPING me: ______________________________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Evidence this rule is HURTING me: ______________________________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Challenge: What would happen if I broke this rule? ______________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "____________________________________________________________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Did I break it? What happened? ________________________________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "____________________________________________________________", 'F1', 9, 0.3)
            y -= 30

    # Page 22: Social Eating Prep
    doc.new_page()
    doc.add_centered_text(590, "SOCIAL EATING PREPARATION", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Eating with others can be hard. Let's plan ahead:", 'F1', 10, 0.2)
    y = 530
    doc.add_text(50, y, "The event: _______________________________________________________", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(50, y, "My fears about it: _______________________________________________", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(50, y, "My plan: I will eat _____________ and that is ENOUGH.", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(50, y, "If ED voice gets loud, I will: ___________________________________", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(50, y, "Person who knows and can support me: _____________________________", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(50, y, "Reminder: Eating with others is NORMAL and I deserve to enjoy it.", 'F2', 10, 0)

    # Pages 23-30: Weekly Recovery Check-In (8 pages)
    for week in range(8):
        doc.new_page()
        doc.add_centered_text(590, f"WEEKLY RECOVERY CHECK-IN - Week {week+1}", 'F2', 12, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 558
        doc.add_text(50, y, "Week of: _______________", 'F1', 9, 0.3)
        y -= 20
        doc.add_text(50, y, "Meals completed (aim for 3 meals + 2-3 snacks/day): ___ /day avg", 'F1', 9, 0.2)
        y -= 20
        doc.add_text(50, y, "ED urges this week (how many times): ___", 'F1', 9, 0.2)
        y -= 20
        doc.add_text(50, y, "Times I acted on the urge: ___   Times I resisted: ___", 'F1', 9, 0.2)
        y -= 20
        doc.add_text(50, y, "Coping skills I used: _____________________________________________", 'F1', 9, 0.2)
        y -= 20
        doc.add_text(50, y, "Recovery wins this week:", 'F2', 9, 0)
        y -= 16
        for i in range(3):
            doc.add_text(50, y, f"  {i+1}. ________________________________________________________", 'F1', 9, 0.3)
            y -= 16
        y -= 10
        doc.add_text(50, y, "Struggles this week: ______________________________________________", 'F1', 9, 0.2)
        y -= 20
        doc.add_text(50, y, "Body image rating (1=terrible, 10=neutral/good): ___", 'F1', 9, 0.2)
        y -= 20
        doc.add_text(50, y, "One food rule I challenged: _______________________________________", 'F1', 9, 0.2)
        y -= 20
        doc.add_text(50, y, "Self-compassion moment: ___________________________________________", 'F1', 9, 0.2)

    # Page 31: My Reasons for Recovery
    doc.new_page()
    doc.add_centered_text(590, "MY REASONS FOR RECOVERY", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "When the ED voice is loud, read this page:", 'F2', 10, 0)
    y = 530
    for i in range(12):
        doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 10, 0.2)
        y -= 22
    y -= 10
    doc.add_text(50, y, "I am recovering for ME. Not to be thin. Not for others.", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "I am recovering to LIVE.", 'F2', 10, 0)

    # Page 32: Professional Support Log
    doc.new_page()
    doc.add_centered_text(590, "PROFESSIONAL SUPPORT LOG", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "My treatment team:", 'F2', 10, 0)
    y -= 20
    team = ["Therapist:", "Dietitian:", "Psychiatrist:", "Doctor:", "Support group:"]
    for member in team:
        doc.add_text(50, y, f"{member} _____________________________  Phone: ____________", 'F1', 9, 0.2)
        y -= 20
    y -= 10
    doc.add_text(50, y, "Appointment notes:", 'F2', 10, 0)
    y -= 18
    for i in range(8):
        doc.add_text(50, y, "Date: ________  With: ________  Notes: ____________________", 'F1', 8, 0.3)
        y -= 18

    # Page 33: Recovery Milestones
    doc.new_page()
    doc.add_centered_text(590, "RECOVERY MILESTONES CELEBRATION", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    milestones = ["Ate a fear food", "Ate without counting", "Ate in public",
                  "Went a full day without ED behaviors", "Looked in mirror without criticizing",
                  "Wore something I was scared to wear", "Ate when hungry (honored my body)",
                  "Told someone about my ED", "Went a full week without behaviors",
                  "Chose recovery over the ED voice"]
    for m in milestones:
        doc.add_rect(50, y-3, 10, 10)
        doc.add_text(65, y, m, 'F1', 9, 0.2)
        doc.add_text(310, y, "Date: ________", 'F1', 8, 0.3)
        y -= 22
    y -= 10
    doc.add_text(50, y, "You are doing the hardest, bravest thing. Keep going.", 'F2', 10, 0)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book143_ED_Recovery_Journal.pdf')
    print("Book143_ED_Recovery_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
