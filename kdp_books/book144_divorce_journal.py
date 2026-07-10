"""Book 144: Starting Over - A Guided Journal for Healing After Divorce"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "STARTING OVER", 'F2', 24, 0)
    doc.add_centered_text(395, "A Guided Journal for", 'F4', 16, 0.2)
    doc.add_centered_text(370, "Healing After Divorce", 'F4', 16, 0.2)
    doc.add_centered_text(300, "The end of a marriage is not", 'F4', 12, 0.3)
    doc.add_centered_text(280, "the end of your story.", 'F4', 12, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(500, "STARTING OVER", 'F2', 14, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)

    # Page 3: Where You Are Is Okay
    doc.new_page()
    doc.add_centered_text(590, "WHERE YOU ARE IS OKAY", 'F2', 16, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Whether you initiated the divorce or it happened to you,", 'F4', 11, 0.2)
    doc.add_text(50, 535, "whether it's been days or years, whether you feel relief or", 'F4', 11, 0.2)
    doc.add_text(50, 515, "devastation or both - where you are right now is okay.", 'F4', 11, 0.2)
    y = 480
    doc.add_text(50, y, "You might feel:", 'F1', 11, 0.2)
    y -= 20
    feelings = ["Grief for what you lost", "Relief that it's over", "Anger at them (or yourself)",
                "Fear of the unknown", "Guilt about the kids", "Freedom you didn't expect",
                "Loneliness that takes your breath away", "All of these at once"]
    for f in feelings:
        doc.add_text(65, y, f"- {f}", 'F1', 10, 0.2)
        y -= 16
    y -= 15
    doc.add_text(50, y, "ALL of these feelings are valid. There is no 'right' way to divorce.", 'F2', 10, 0)

    # Page 4: Processing the End
    doc.new_page()
    doc.add_centered_text(590, "PROCESSING THE END", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    prompts = [
        ("Our story (how it began):", 4),
        ("The breaking point:", 4),
        ("What I lost:", 4),
        ("What I gained (even if small):", 4)
    ]
    for prompt, lines in prompts:
        doc.add_text(50, y, prompt, 'F2', 10, 0.1)
        y -= 18
        for i in range(lines):
            doc.add_text(50, y, "_" * 52, 'F1', 10, 0.4)
            y -= 14
        y -= 12

    # Page 5: Grief Stages in Divorce
    doc.new_page()
    doc.add_centered_text(590, "GRIEF STAGES IN DIVORCE", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Divorce IS grief - even if no one died. You're mourning:", 'F1', 10, 0.2)
    y = 530
    mourning = ["The future you planned", "The family unit", "The person they used to be",
                "Your identity as a spouse", "Financial security", "Daily routines and 'home'"]
    for m in mourning:
        doc.add_text(65, y, f"- {m}", 'F1', 10, 0.2)
        y -= 16
    y -= 15
    doc.add_text(50, y, "The stages (non-linear - you'll bounce around):", 'F2', 10, 0)
    y -= 18
    stages = [("DENIAL:", "This can't be happening."), ("ANGER:", "How could they do this?"),
              ("BARGAINING:", "If only I had..."), ("DEPRESSION:", "I'll never be happy again."),
              ("ACCEPTANCE:", "This is my reality. I can build something new.")]
    for stage, desc in stages:
        doc.add_text(50, y, stage, 'F2', 9, 0)
        doc.add_text(130, y, desc, 'F4', 9, 0.3)
        y -= 18
    y -= 10
    doc.add_text(50, y, "Where I am today: ______________________________________________", 'F1', 10, 0.2)

    # Pages 6-8: Releasing Anger (3 pages)
    anger_prompts = [
        "I am angry because...",
        "What I wish I could say to them (uncensored):",
        "What I need to forgive myself for:"
    ]
    for i, prompt in enumerate(anger_prompts):
        doc.new_page()
        doc.add_centered_text(590, f"RELEASING ANGER ({i+1}/3)", 'F2', 14, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        doc.add_text(50, 555, prompt, 'F2', 10, 0.1)
        y = 530
        for line in range(24):
            doc.add_text(50, y, "_" * 52, 'F1', 10, 0.4)
            y -= 18

    # Page 9: Forgiveness Work
    doc.new_page()
    doc.add_centered_text(590, "FORGIVENESS WORK", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Forgiveness is NOT saying what happened was okay.", 'F2', 10, 0)
    doc.add_text(50, 535, "It's releasing the poison so YOU can heal.", 'F1', 10, 0.2)
    y = 505
    doc.add_text(50, y, "Forgiving THEM:", 'F2', 10, 0)
    y -= 18
    doc.add_text(50, y, "What I need to release: ___________________________________________", 'F1', 9, 0.3)
    y -= 16
    doc.add_text(50, y, "Why holding this hurts ME: ________________________________________", 'F1', 9, 0.3)
    y -= 16
    doc.add_text(50, y, "I choose to release: ______________________________________________", 'F1', 9, 0.3)
    y -= 25
    doc.add_text(50, y, "Forgiving MYSELF:", 'F2', 10, 0)
    y -= 18
    doc.add_text(50, y, "What I blame myself for: __________________________________________", 'F1', 9, 0.3)
    y -= 16
    doc.add_text(50, y, "The truth is: ____________________________________________________", 'F1', 9, 0.3)
    y -= 16
    doc.add_text(50, y, "I deserve grace because: __________________________________________", 'F1', 9, 0.3)

    # Page 10: Coparenting Communication Scripts
    doc.new_page()
    doc.add_centered_text(590, "COPARENTING COMMUNICATION SCRIPTS", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    scripts = [
        ("Schedule changes:", "'I need to adjust pickup on [date]. Can we do [alternative]?'"),
        ("Concerns about child:", "'I noticed [behavior]. Can we discuss how to handle it together?'"),
        ("Boundaries:", "'I'm not comfortable discussing our relationship. Let's focus on the kids.'"),
        ("Disagreements:", "'I see it differently. Can we find a middle ground for [child]?'"),
        ("When they push buttons:", "'I'm going to take some time before responding to this.'")
    ]
    for scenario, script in scripts:
        doc.add_text(50, y, scenario, 'F2', 9, 0.1)
        y -= 16
        doc.add_text(50, y, script, 'F4', 9, 0.3)
        y -= 25
    y -= 10
    doc.add_text(50, y, "GOLDEN RULES: Business-like. Brief. Child-focused. Written when calm.", 'F2', 9, 0)

    # Page 11: Rebuilding Identity
    doc.new_page()
    doc.add_centered_text(590, "REBUILDING IDENTITY: WHO AM I NOW?", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    identity_qs = [
        "Things I like that had nothing to do with my ex:",
        "Things I stopped doing during the marriage:",
        "Things I want to try now that I'm free:",
        "Values that are MINE (not ours):",
        "Who I want to become in this next chapter:"
    ]
    for q in identity_qs:
        doc.add_text(50, y, q, 'F2', 9, 0.1)
        y -= 16
        for line in range(3):
            doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
            y -= 14
        y -= 10

    # Page 12: Financial Reset
    doc.new_page()
    doc.add_centered_text(590, "FINANCIAL RESET WORKSHEET", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "My new monthly income: $__________", 'F1', 10, 0.2)
    y -= 20
    doc.add_text(50, y, "Essential expenses:", 'F2', 10, 0)
    y -= 18
    expenses = ["Housing:", "Utilities:", "Food:", "Transportation:", "Insurance:", "Childcare:", "Debt payments:"]
    for e in expenses:
        doc.add_text(50, y, f"  {e} $__________", 'F1', 9, 0.3)
        y -= 16
    y -= 10
    doc.add_text(50, y, "Total essentials: $__________  What's left: $__________", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(50, y, "First financial priority: ________________________________________", 'F1', 10, 0.2)
    y -= 20
    doc.add_text(50, y, "Help I need: _____________________________________________________", 'F1', 10, 0.2)

    # Page 13: Boundaries with Ex
    doc.new_page()
    doc.add_centered_text(590, "NEW BOUNDARIES WITH MY EX", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Communication boundaries:", 'F2', 10, 0)
    y -= 18
    doc.add_text(50, y, "(e.g., text only, no calls after 9pm, only about kids)", 'F3', 8, 0.4)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.3)
    y -= 22
    doc.add_text(50, y, "Physical boundaries:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.3)
    y -= 22
    doc.add_text(50, y, "Emotional boundaries:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.3)
    y -= 22
    doc.add_text(50, y, "What I will NO LONGER tolerate:", 'F2', 10, 0)
    y -= 16
    for i in range(3):
        doc.add_text(50, y, f"_______________________________________________________________", 'F1', 9, 0.3)
        y -= 16

    # Page 14: Social Life Rebuild + Dating Readiness
    doc.new_page()
    doc.add_centered_text(590, "SOCIAL LIFE REBUILD & DATING READINESS", 'F2', 11, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Friends I want to reconnect with:", 'F2', 10, 0)
    y -= 18
    for i in range(3):
        doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 9, 0.3)
        y -= 16
    y -= 10
    doc.add_text(50, y, "New activities/groups to try:", 'F2', 10, 0)
    y -= 18
    for i in range(3):
        doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 9, 0.3)
        y -= 16
    y -= 10
    doc.add_text(50, y, "DATING READINESS CHECK (be honest):", 'F2', 10, 0)
    y -= 18
    checks = ["I'm dating to connect, not to avoid loneliness", "I know what I want and won't want",
              "I've processed the divorce (mostly)", "I'm not trying to make my ex jealous",
              "I can be alone and be okay"]
    for c in checks:
        doc.add_rect(50, y-3, 10, 10)
        doc.add_text(65, y, c, 'F1', 9, 0.2)
        y -= 16

    # Pages 15-29: Daily Healing Prompts (15 pages)
    prompts_list = [
        "What am I grieving today?",
        "One thing I'm grateful for in my new life:",
        "A memory I need to release:",
        "What growth have I noticed in myself?",
        "Who showed up for me during this? How can I thank them?",
        "What does 'home' mean to me now?",
        "A boundary I'm proud of setting:",
        "What scares me about being single?",
        "What excites me about being single?",
        "A letter to my future self (1 year from now):",
        "What I want my kids to know about love:",
        "Something I did today just for ME:",
        "The hardest part of this week was:",
        "Three things that went RIGHT this week:",
        "What I know now that I didn't know then:"
    ]
    for i, prompt in enumerate(prompts_list):
        doc.new_page()
        doc.add_centered_text(590, f"HEALING PROMPT {i+1}", 'F2', 12, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        doc.add_text(50, 555, prompt, 'F2', 11, 0.1)
        y = 525
        for line in range(24):
            doc.add_text(50, y, "_" * 52, 'F1', 10, 0.4)
            y -= 18

    # Page 30: My New Chapter Vision
    doc.new_page()
    doc.add_centered_text(590, "MY NEW CHAPTER VISION", 'F2', 16, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "In this new chapter of my life, I want:", 'F4', 11, 0.2)
    y -= 25
    areas = ["My home:", "My career:", "My health:", "My relationships:", "My daily life:", "My growth:"]
    for area in areas:
        doc.add_text(50, y, f"{area} ___________________________________________________", 'F1', 10, 0.2)
        y -= 22
    y -= 15
    doc.add_text(50, y, "I am not starting over. I am starting FROM EXPERIENCE.", 'F2', 10, 0)
    y -= 18
    doc.add_text(50, y, "I am wiser. I am stronger. I will build something beautiful.", 'F4', 10, 0.2)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book144_Divorce_Recovery_Journal.pdf')
    print("Book144_Divorce_Recovery_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
