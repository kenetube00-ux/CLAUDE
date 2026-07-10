"""Book 147: Reclaiming Me - A Recovery Workbook for Narcissistic Abuse Survivors"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "RECLAIMING ME", 'F2', 24, 0)
    doc.add_centered_text(395, "A Recovery Workbook for", 'F4', 15, 0.2)
    doc.add_centered_text(370, "Narcissistic Abuse Survivors", 'F4', 15, 0.2)
    doc.add_centered_text(300, "You are not crazy.", 'F4', 12, 0.3)
    doc.add_centered_text(280, "It was real. It was abuse.", 'F4', 12, 0.3)
    doc.add_centered_text(260, "And you can heal.", 'F4', 12, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(500, "RECLAIMING ME", 'F2', 14, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)
    doc.add_text(50, 410, "National DV Hotline: 1-800-799-7233 | thehotline.org", 'F1', 9, 0.3)

    # Page 3: Understanding Narcissistic Abuse
    doc.new_page()
    doc.add_centered_text(590, "UNDERSTANDING NARCISSISTIC ABUSE", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "The Cycle of Narcissistic Abuse:", 'F2', 10, 0)
    y = 533
    cycle = [
        ("1. LOVE BOMBING:", "Intense attention, gifts, 'soulmate' talk, moving fast"),
        ("2. DEVALUATION:", "Criticism, gaslighting, withdrawal, triangulation"),
        ("3. DISCARD:", "Silent treatment, replacement, cruel exit"),
        ("4. HOOVERING:", "Comes back with apologies, promises, 'I've changed'"),
        ("5. REPEAT:", "The cycle starts again, each time more intense")
    ]
    for step, desc in cycle:
        doc.add_text(50, y, step, 'F2', 9, 0)
        y -= 14
        doc.add_text(55, y, desc, 'F1', 9, 0.3)
        y -= 20
    y -= 10
    doc.add_text(50, y, "Where I was in the cycle: _________________________________________", 'F1', 9, 0.2)
    y -= 18
    doc.add_text(50, y, "How many times the cycle repeated: _________________________________", 'F1', 9, 0.2)

    # Page 4: Am I Being Gaslit?
    doc.new_page()
    doc.add_centered_text(590, "AM I BEING GASLIT? CHECKLIST", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Gaslighting makes you doubt YOUR reality. Check what applies:", 'F1', 10, 0.2)
    y = 530
    signs = ["They deny things you KNOW happened",
             "They say 'You're too sensitive' or 'You're crazy'",
             "You constantly second-guess yourself",
             "You feel confused about what's real",
             "You apologize for everything (even their behavior)",
             "They rewrite history and you start to believe them",
             "You feel like you're walking on eggshells",
             "You've stopped trusting your own memory",
             "You make excuses for their behavior to others",
             "You feel like you've lost yourself",
             "Other people say you've changed",
             "You're afraid to bring up concerns"]
    for s in signs:
        doc.add_rect(50, y-3, 10, 10)
        doc.add_text(65, y, s, 'F1', 9, 0.2)
        y -= 16
    y -= 10
    doc.add_text(50, y, "If you checked 3+: Trust yourself. Your experience is REAL.", 'F2', 9, 0)

    # Page 5: FOG Assessment
    doc.new_page()
    doc.add_centered_text(590, "THE FOG: Fear, Obligation, Guilt", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Narcissists keep you trapped using FOG:", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(50, y, "FEAR - What am I afraid will happen if I leave/set boundaries?", 'F2', 9, 0)
    y -= 16
    for i in range(3):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14
    y -= 10
    doc.add_text(50, y, "OBLIGATION - What do I feel I 'owe' them?", 'F2', 9, 0)
    y -= 16
    for i in range(3):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14
    y -= 10
    doc.add_text(50, y, "GUILT - What do I feel guilty about?", 'F2', 9, 0)
    y -= 16
    for i in range(3):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14
    y -= 15
    doc.add_text(50, y, "TRUTH: You don't owe your abuser anything. Fear and guilt are", 'F2', 9, 0)
    y -= 14
    doc.add_text(50, y, "tools THEY installed in you. You can uninstall them.", 'F2', 9, 0)

    # Page 6: Trauma Bonding
    doc.new_page()
    doc.add_centered_text(590, "UNDERSTANDING TRAUMA BONDING", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Trauma bonds form through intermittent reinforcement:", 'F1', 10, 0.2)
    doc.add_text(50, 535, "Cruelty + occasional kindness = addiction to the relationship.", 'F1', 10, 0.2)
    y = 508
    doc.add_text(50, y, "Signs of trauma bonding:", 'F2', 10, 0)
    y -= 16
    signs = ["You miss them even though they hurt you",
             "You justify their abuse", "You believe you can 'fix' them",
             "Leaving feels physically painful", "You keep going back",
             "You defend them to others", "You feel addicted to the highs"]
    for s in signs:
        doc.add_text(60, y, f"- {s}", 'F1', 9, 0.2)
        y -= 14
    y -= 15
    doc.add_text(50, y, "This is NOT love. This is a trauma response. And it CAN be broken.", 'F2', 9, 0)

    # Page 7: No-Contact / Gray Rock Planning
    doc.new_page()
    doc.add_centered_text(590, "NO-CONTACT / GRAY ROCK PLANNING", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "NO CONTACT (if possible):", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "Block on: [ ] Phone [ ] Text [ ] Email [ ] All social media", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Flying monkeys to block/limit: _____________________________________", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "My plan if they show up: ___________________________________________", 'F1', 9, 0.2)
    y -= 20
    doc.add_text(50, y, "GRAY ROCK (when no-contact isn't possible - coparenting, work):", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "Be boring. Be brief. Be uninteresting. Give them NOTHING.", 'F1', 9, 0.2)
    y -= 14
    gray_rock = ["Only discuss necessary topics (kids, work logistics)",
                 "Don't share emotions, opinions, or personal info",
                 "Use short answers: 'okay' 'noted' 'I'll think about it'",
                 "Don't defend yourself (they'll use it against you)",
                 "Communicate in writing when possible (evidence)"]
    for g in gray_rock:
        doc.add_text(60, y, f"- {g}", 'F1', 8, 0.3)
        y -= 14
    y -= 10
    doc.add_text(50, y, "My gray rock phrases: _____________________________________________", 'F1', 9, 0.2)

    # Pages 8-12: Rebuilding Self-Trust (5 pages)
    trust_prompts = [
        "Things I KNOW are true about what happened (trust your memory):",
        "Times my gut was RIGHT and I ignored it:",
        "Decisions I made on my own that turned out well:",
        "What I need to hear: 'I trust myself because...'",
        "Evidence that I am capable, smart, and worthy:"
    ]
    for i, prompt in enumerate(trust_prompts):
        doc.new_page()
        doc.add_centered_text(590, f"REBUILDING SELF-TRUST ({i+1}/5)", 'F2', 13, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        doc.add_text(50, 555, prompt, 'F2', 10, 0.1)
        y = 530
        for line in range(22):
            doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
            y -= 18

    # Pages 13-17: Cognitive Distortions from Abuse (5 pages)
    beliefs = [
        ("'I am not enough'", "Where this came from:", "Evidence this is THEIR voice, not truth:"),
        ("'No one will believe me'", "Where this came from:", "People who DO believe me:"),
        ("'I provoked the abuse'", "Where this came from:", "Truth: Abuse is ALWAYS the abuser's choice:"),
        ("'I'll never be normal'", "Where this came from:", "Evidence of my healing/strength:"),
        ("'I deserved it'", "Where this came from:", "NO ONE deserves abuse. What I actually deserve:")
    ]
    for belief, prompt1, prompt2 in beliefs:
        doc.new_page()
        doc.add_centered_text(590, "CHALLENGING INTERNALIZED BELIEFS", 'F2', 12, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 555
        doc.add_text(50, y, f"The belief: {belief}", 'F2', 10, 0)
        y -= 22
        doc.add_text(50, y, prompt1, 'F1', 9, 0.2)
        y -= 16
        for line in range(4):
            doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
            y -= 14
        y -= 10
        doc.add_text(50, y, prompt2, 'F1', 9, 0.2)
        y -= 16
        for line in range(4):
            doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
            y -= 14
        y -= 10
        doc.add_text(50, y, "Rewritten belief (in MY voice):", 'F2', 9, 0)
        y -= 16
        for line in range(3):
            doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
            y -= 14

    # Page 18: Re-establishing Boundaries
    doc.new_page()
    doc.add_centered_text(590, "RE-ESTABLISHING BOUNDARIES", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Narcissists taught you that your boundaries don't matter.", 'F1', 10, 0.2)
    doc.add_text(50, y-16, "They DO. Let's rebuild them:", 'F2', 10, 0)
    y -= 38
    boundary_types = ["Physical boundaries:", "Emotional boundaries:", "Time/energy boundaries:",
                      "Digital/communication:", "What I will no longer tolerate from ANYONE:"]
    for b in boundary_types:
        doc.add_text(50, y, b, 'F2', 9, 0.1)
        y -= 16
        doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
        y -= 20

    # Page 19: Red Flags for Future Relationships
    doc.new_page()
    doc.add_centered_text(590, "RED FLAGS FOR FUTURE RELATIONSHIPS", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Now that you know the pattern, you can spot it early:", 'F2', 10, 0)
    y -= 18
    red_flags = ["Love bombing (too much too fast)", "Isolating you from friends/family",
                 "Needing to know where you are always", "Criticizing then saying 'just joking'",
                 "Making everything about them", "Never apologizing sincerely",
                 "Your gut says something is off", "You start to feel 'crazy' again",
                 "They have zero accountability", "They triangulate (comparing you to exes)",
                 "Excessive jealousy framed as 'love'", "You feel smaller around them"]
    for rf in red_flags:
        doc.add_text(60, y, f"- {rf}", 'F1', 9, 0.2)
        y -= 14
    y -= 10
    doc.add_text(50, y, "Green flags I want instead:", 'F2', 9, 0)
    y -= 14
    for i in range(3):
        doc.add_text(50, y, f"_______________________________________________________________", 'F1', 9, 0.4)
        y -= 14

    # Pages 20-27: Healing Progress Tracker (8 pages)
    for week in range(8):
        doc.new_page()
        doc.add_centered_text(590, f"HEALING PROGRESS TRACKER - Week {week+1}", 'F2', 11, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 558
        doc.add_text(50, y, "Week of: _______________", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(50, y, "Times I thought about them: ___  (no judgment - just tracking)", 'F1', 9, 0.2)
        y -= 16
        doc.add_text(50, y, "Times I almost broke no-contact: ___", 'F1', 9, 0.2)
        y -= 16
        doc.add_text(50, y, "Did I break it? [ ] No (proud!) [ ] Yes (no shame, try again)", 'F1', 9, 0.2)
        y -= 18
        doc.add_text(50, y, "A boundary I held:", 'F2', 9, 0)
        y -= 14
        doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
        y -= 18
        doc.add_text(50, y, "A moment I trusted myself:", 'F2', 9, 0)
        y -= 14
        doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
        y -= 18
        doc.add_text(50, y, "Self-care I did:", 'F2', 9, 0)
        y -= 14
        doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
        y -= 18
        doc.add_text(50, y, "Something that triggered me & how I coped:", 'F2', 9, 0)
        y -= 14
        doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
        y -= 18
        doc.add_text(50, y, "Evidence I'm healing (even small):", 'F2', 9, 0)
        y -= 14
        doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)

    # Page 28: Letter to My Younger Self
    doc.new_page()
    doc.add_centered_text(590, "LETTER TO MY YOUNGER SELF", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Write to yourself before the abuse began:", 'F4', 10, 0.3)
    y = 530
    for i in range(24):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 18

    # Page 29: I Am Not Crazy
    doc.new_page()
    doc.add_centered_text(590, "I AM NOT CRAZY", 'F2', 18, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 550
    validations = [
        "What happened to me was real.",
        "My feelings are valid.",
        "I am not 'too sensitive.'",
        "I did not cause the abuse.",
        "I did not deserve the abuse.",
        "My memory is trustworthy.",
        "I am not crazy for being affected.",
        "The confusion I feel was CREATED by them.",
        "I am stronger than I know.",
        "I am allowed to be angry.",
        "I am allowed to grieve.",
        "I am allowed to heal at my own pace.",
        "I am allowed to never forgive them.",
        "I am worthy of healthy love.",
        "I am reclaiming my life."
    ]
    for v in validations:
        doc.add_text(50, y, v, 'F2', 10, 0)
        y -= 22
    y -= 10
    doc.add_text(50, y, "Read this page whenever the self-doubt creeps back in.", 'F4', 10, 0.3)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book147_Narcissistic_Abuse_Recovery.pdf')
    print("Book147_Narcissistic_Abuse_Recovery.pdf created successfully!")

if __name__ == "__main__":
    create_book()
