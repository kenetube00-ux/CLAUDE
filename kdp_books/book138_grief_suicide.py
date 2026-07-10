"""Book 138: Suicide Loss Grief Journal - After the Unthinkable"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "AFTER THE UNTHINKABLE", 'F2', 22, 0)
    doc.add_centered_text(395, "A Grief Journal for", 'F4', 16, 0.2)
    doc.add_centered_text(370, "Suicide Loss Survivors", 'F4', 16, 0.2)
    doc.add_centered_text(300, "You did not cause this.", 'F4', 12, 0.3)
    doc.add_centered_text(280, "You could not have prevented this.", 'F4', 12, 0.3)
    doc.add_centered_text(260, "You are not alone.", 'F4', 12, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(500, "AFTER THE UNTHINKABLE", 'F2', 12, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)
    doc.add_text(50, 410, "This journal is not a substitute for grief counseling.", 'F1', 9, 0.3)
    doc.add_text(50, 380, "If you are in crisis: Call 988 (Suicide & Crisis Lifeline)", 'F2', 9, 0.3)
    doc.add_text(50, 360, "AFSP: afsp.org | Alliance of Hope: allianceofhope.org", 'F1', 9, 0.3)

    # Page 3: You Are Not Alone
    doc.new_page()
    doc.add_centered_text(590, "YOU ARE NOT ALONE", 'F2', 16, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "If you are holding this journal, you have experienced one of the", 'F4', 11, 0.2)
    doc.add_text(50, 538, "most devastating losses a human can face. The death of someone", 'F4', 11, 0.2)
    doc.add_text(50, 521, "you love by suicide.", 'F4', 11, 0.2)
    doc.add_text(50, 490, "This grief is different. It comes with:", 'F1', 11, 0.2)
    items = ["Questions that may never be answered", "Guilt that does not belong to you",
             "Anger at the person you love and miss", "Stigma that silences your pain",
             "A loneliness that feels impossible to explain"]
    y = 465
    for item in items:
        doc.add_text(65, y, f"- {item}", 'F1', 11, 0.2)
        y -= 20
    y -= 15
    doc.add_text(50, y, "This journal is a safe space. There are no wrong feelings here.", 'F2', 11, 0)
    y -= 20
    doc.add_text(50, y, "Write as much or as little as you need. Skip pages. Come back.", 'F1', 11, 0.2)
    y -= 20
    doc.add_text(50, y, "Your grief is valid. Your love is real. You will survive this.", 'F4', 11, 0.2)

    # Page 4: The Unique Grief of Suicide Loss
    doc.new_page()
    doc.add_centered_text(590, "THE UNIQUE GRIEF OF SUICIDE LOSS", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Suicide grief is complicated by factors other losses don't carry:", 'F1', 11, 0.2)
    y = 530
    factors = [
        ("The 'Why':", "The endless search for reasons that may never fully satisfy."),
        ("The 'If Only':", "Replaying moments, wondering if you missed signs."),
        ("The Stigma:", "Others may not know what to say, or say hurtful things."),
        ("The Anger:", "It's okay to be angry at someone you love and mourn."),
        ("The Guilt:", "Survivor's guilt is universal in suicide loss - and undeserved."),
        ("The Trauma:", "You may have found them. You may replay the notification.")
    ]
    for title, desc in factors:
        doc.add_text(50, y, title, 'F2', 10, 0.1)
        doc.add_text(50, y-16, desc, 'F1', 10, 0.3)
        y -= 42

    # Pages 5-34: 30 Daily Journal Pages
    prompts_rotation = [
        "How I feel today (1-10):",
        "The guilt I'm carrying today:",
        "What I wish I could say to them:",
        "Where I found light today (even a flicker):",
        "One truth I need to hear right now:",
        "Evening prayer or reflection:"
    ]
    for day in range(1, 31):
        doc.new_page()
        doc.add_centered_text(600, f"DAY {day}", 'F2', 14, 0)
        doc.add_line(50, 590, 382, 590, 0.5, 0.7)
        doc.add_text(50, 570, "Date: _________________", 'F1', 10, 0.3)
        y = 545
        for prompt in prompts_rotation:
            doc.add_text(50, y, prompt, 'F2', 10, 0.1)
            y -= 18
            for line in range(3):
                doc.add_text(50, y, "_" * 55, 'F1', 10, 0.4)
                y -= 16
            y -= 12

    # Page 35: Common Myths Debunked
    doc.new_page()
    doc.add_centered_text(590, "COMMON MYTHS ABOUT SUICIDE - DEBUNKED", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    myths = [
        ("MYTH: It was selfish.", "TRUTH: They were in unbearable pain and saw no other way out."),
        ("MYTH: You should have seen the signs.", "TRUTH: Many people hide their pain. This is not your fault."),
        ("MYTH: Talking about it is dangerous.", "TRUTH: Open conversation reduces stigma and saves lives."),
        ("MYTH: They didn't love you enough to stay.", "TRUTH: Mental illness distorts thinking. Their love was real."),
        ("MYTH: You'll 'get over it' with time.", "TRUTH: You learn to carry it differently. Grief has no timeline."),
        ("MYTH: They are in a 'better place' (if unhelpful).", "TRUTH: You're allowed to be angry about platitudes.")
    ]
    y = 555
    for myth, truth in myths:
        doc.add_text(50, y, myth, 'F2', 9, 0.1)
        y -= 16
        doc.add_text(50, y, truth, 'F4', 9, 0.3)
        y -= 28

    # Page 36: Complicated Grief vs Normal Grief
    doc.new_page()
    doc.add_centered_text(590, "COMPLICATED GRIEF vs NORMAL GRIEF", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "All grief after suicide is painful. But seek help if you notice:", 'F1', 10, 0.2)
    y = 530
    signs = ["Intense longing that doesn't lessen after 6+ months",
             "Inability to accept the death", "Feeling life has no meaning or purpose",
             "Difficulty trusting others", "Emotional numbness or detachment",
             "Feeling that part of you died too", "Avoiding reminders of the loss entirely",
             "Suicidal thoughts of your own"]
    for s in signs:
        doc.add_text(65, y, f"- {s}", 'F1', 10, 0.2)
        y -= 18
    y -= 15
    doc.add_text(50, y, "These are signs of Prolonged Grief Disorder. Help is available.", 'F2', 10, 0)
    y -= 20
    doc.add_text(50, y, "A grief therapist specializing in suicide loss can help.", 'F1', 10, 0.2)

    # Page 37: My Support Network
    doc.new_page()
    doc.add_centered_text(590, "MY SUPPORT NETWORK", 'F2', 16, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "People I can call when the grief is heavy:", 'F2', 11, 0)
    y -= 25
    for i in range(4):
        doc.add_text(50, y, f"Name: _____________________  Phone: _________________  Relation: ________", 'F1', 9, 0.2)
        y -= 25
    y -= 10
    doc.add_text(50, y, "My therapist/counselor: ____________________________________________", 'F1', 10, 0.2)
    y -= 25
    doc.add_text(50, y, "My support group: _________________________________________________", 'F1', 10, 0.2)
    y -= 30
    doc.add_text(50, y, "What helps when I'm spiraling:", 'F2', 11, 0)
    y -= 22
    for i in range(4):
        doc.add_text(50, y, f"{i+1}. _____________________________________________________________", 'F1', 10, 0.2)
        y -= 22

    # Page 38: Survivor Support Group Log
    doc.new_page()
    doc.add_centered_text(590, "SURVIVOR SUPPORT GROUP LOG", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    for i in range(5):
        doc.add_text(50, y, f"Meeting {i+1}  Date: __________  Group: ________________________", 'F2', 10, 0.1)
        y -= 20
        doc.add_text(50, y, "What resonated: __________________________________________________", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(50, y, "How I felt after: ________________________________________________", 'F1', 9, 0.3)
        y -= 30

    # Page 39: Letter to My Person
    doc.new_page()
    doc.add_centered_text(590, "LETTER TO MY PERSON", 'F2', 16, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Write what you need to say. There are no rules here.", 'F4', 10, 0.3)
    y = 530
    for i in range(25):
        doc.add_text(50, y, "_" * 55, 'F1', 10, 0.4)
        y -= 18

    # Page 40: Anniversary Coping Plan + Resources
    doc.new_page()
    doc.add_centered_text(590, "ANNIVERSARY & BIRTHDAY COPING PLAN", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 558, "Important dates to prepare for:", 'F2', 10, 0.1)
    y = 538
    dates = ["Their birthday:", "Anniversary of their death:", "Holidays:", "Our special dates:"]
    for d in dates:
        doc.add_text(50, y, f"{d} _______________________________________________", 'F1', 10, 0.2)
        y -= 22
    y -= 10
    doc.add_text(50, y, "My plan for hard days:", 'F2', 10, 0.1)
    y -= 20
    for i in range(3):
        doc.add_text(50, y, f"{i+1}. ___________________________________________________________", 'F1', 10, 0.2)
        y -= 20
    y -= 15
    doc.add_text(50, y, "RESOURCES:", 'F2', 12, 0)
    y -= 22
    resources = ["988 Suicide & Crisis Lifeline: Call or text 988",
                 "AFSP (American Foundation for Suicide Prevention): afsp.org",
                 "Alliance of Hope for Suicide Loss Survivors: allianceofhope.org",
                 "Survivors of Suicide Loss: soslsd.org",
                 "Crisis Text Line: Text HOME to 741741"]
    for r in resources:
        doc.add_text(50, y, f"- {r}", 'F1', 9, 0.2)
        y -= 16

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book138_Suicide_Loss_Grief_Journal.pdf')
    print("Book138_Suicide_Loss_Grief_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
