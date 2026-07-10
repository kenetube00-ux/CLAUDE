"""Book 149: Man Up (To Healing) - A Mental Health Journal for Men"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "MAN UP (TO HEALING)", 'F2', 20, 0)
    doc.add_centered_text(395, "A Mental Health Journal", 'F4', 16, 0.2)
    doc.add_centered_text(370, "for Men", 'F4', 16, 0.2)
    doc.add_centered_text(300, "Strength is not silence.", 'F4', 12, 0.3)
    doc.add_centered_text(280, "Real men feel. Real men heal.", 'F4', 12, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(500, "MAN UP (TO HEALING)", 'F2', 14, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)
    doc.add_text(50, 410, "If you are in crisis: Call 988 | Crisis Text: Text HELLO to 741741", 'F1', 9, 0.3)

    # Page 3: Breaking the Stigma
    doc.new_page()
    doc.add_centered_text(590, "BREAKING THE STIGMA", 'F2', 16, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Men die by suicide at 4x the rate of women. Not because men are weaker -", 'F1', 10, 0.2)
    doc.add_text(50, 538, "but because men are taught to never ask for help.", 'F1', 10, 0.2)
    y = 510
    doc.add_text(50, y, "Messages men receive:", 'F2', 10, 0)
    y -= 18
    messages = ["'Man up' / 'Boys don't cry'", "'Don't be so sensitive'",
                "'Provide, protect, be strong - always'", "'Handle it yourself'",
                "'Therapy is for weak people'", "'Just push through it'"]
    for m in messages:
        doc.add_text(65, y, f"- {m}", 'F1', 9, 0.2)
        y -= 15
    y -= 15
    doc.add_text(50, y, "THE TRUTH:", 'F2', 11, 0)
    y -= 18
    truths = ["Feeling emotions IS strength", "Asking for help IS brave",
              "Vulnerability IS masculine", "You cannot pour from an empty cup"]
    for t in truths:
        doc.add_text(65, y, f"- {t}", 'F2', 9, 0)
        y -= 15

    # Page 4: Emotions Are Not Weakness
    doc.new_page()
    doc.add_centered_text(590, "EMOTIONS ARE NOT WEAKNESS", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Most men grow up with only 2 'acceptable' emotions: happy and angry.", 'F1', 10, 0.2)
    doc.add_text(50, 537, "But under anger, there's almost always something else:", 'F1', 10, 0.2)
    y = 510
    under_anger = ["Fear", "Hurt", "Shame", "Loneliness", "Grief", "Feeling disrespected",
                   "Feeling powerless", "Sadness", "Overwhelm", "Exhaustion"]
    for u in under_anger:
        doc.add_text(65, y, f"- {u}", 'F1', 9, 0.2)
        y -= 14
    y -= 10
    doc.add_text(50, y, "Today, under my anger/frustration, I might actually feel:", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)

    # Page 5: Identifying What You're Feeling
    doc.new_page()
    doc.add_centered_text(590, "EXPANDED EMOTION VOCABULARY", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Beyond 'fine' and 'angry' - circle what fits today:", 'F2', 10, 0)
    y = 530
    emotion_groups = [
        ("SAD:", "lonely, hopeless, disappointed, grieving, empty, depressed, lost"),
        ("ANGRY:", "frustrated, disrespected, betrayed, bitter, resentful, annoyed"),
        ("SCARED:", "anxious, worried, insecure, vulnerable, panicked, uncertain"),
        ("ASHAMED:", "embarrassed, worthless, guilty, inadequate, exposed, failing"),
        ("HAPPY:", "content, proud, grateful, relieved, connected, hopeful, peaceful"),
        ("TIRED:", "burned out, depleted, numb, overwhelmed, defeated, checked out")
    ]
    for group, words in emotion_groups:
        doc.add_text(50, y, group, 'F2', 9, 0)
        y -= 14
        doc.add_text(55, y, words, 'F1', 9, 0.3)
        y -= 22

    # Page 6: Anger Iceberg
    doc.new_page()
    doc.add_centered_text(590, "THE ANGER ICEBERG", 'F2', 16, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "What people SEE: Anger, irritability, shutting down, aggression", 'F2', 10, 0)
    doc.add_line(50, 540, 382, 540, 1, 0.3)
    doc.add_text(50, 525, "What's UNDERNEATH (the real feelings):", 'F2', 10, 0)
    y = 505
    doc.add_text(50, y, "Think about the last time you were really angry. Underneath was:", 'F1', 9, 0.3)
    y -= 20
    doc.add_text(50, y, "I felt: __________________________________________________________", 'F1', 9, 0.3)
    y -= 18
    doc.add_text(50, y, "I needed: ________________________________________________________", 'F1', 9, 0.3)
    y -= 18
    doc.add_text(50, y, "I was afraid of: _________________________________________________", 'F1', 9, 0.3)
    y -= 18
    doc.add_text(50, y, "What would have actually helped: ___________________________________", 'F1', 9, 0.3)
    y -= 25
    doc.add_text(50, y, "My anger pattern:", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "Trigger: _____________ -> Underlying feeling: ______________", 'F1', 9, 0.3)
    y -= 16
    doc.add_text(50, y, " -> What I actually need: __________________________________________", 'F1', 9, 0.3)

    # Page 7: Stress Management
    doc.new_page()
    doc.add_centered_text(590, "STRESS MANAGEMENT FOR MEN", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Healthy outlets (that actually work):", 'F2', 10, 0)
    y -= 18
    outlets = ["Exercise (lifting, running, martial arts, sports)",
               "Time in nature (fishing, hiking, camping)",
               "Creative work (woodworking, music, cooking, writing)",
               "Connection (calling a friend, being honest with someone)",
               "Rest (actual rest, not just numbing with screens/alcohol)",
               "Routine (sleep, nutrition, movement - the basics matter)"]
    for o in outlets:
        doc.add_text(60, y, f"- {o}", 'F1', 9, 0.2)
        y -= 15
    y -= 15
    doc.add_text(50, y, "What I'm currently doing to cope (be honest):", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
    y -= 18
    doc.add_text(50, y, "Is it helping or hurting long-term?", 'F1', 9, 0.3)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)

    # Page 8: Communication with Partner
    doc.new_page()
    doc.add_centered_text(590, "COMMUNICATION WITH PARTNER", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Common patterns men fall into:", 'F2', 10, 0)
    y -= 16
    patterns = ["Stonewalling (shutting down during conflict)",
                "Fixing instead of listening", "Minimizing partner's feelings",
                "Withdrawing when overwhelmed", "Expressing frustration as anger"]
    for p in patterns:
        doc.add_text(60, y, f"- {p}", 'F1', 9, 0.2)
        y -= 14
    y -= 15
    doc.add_text(50, y, "Scripts to try:", 'F2', 10, 0)
    y -= 16
    scripts = [
        "'I need a minute to think before I respond.'",
        "'I'm feeling [emotion] but I don't know how to express it yet.'",
        "'I hear you. Tell me more about how that felt for you.'",
        "'I'm struggling right now. Can you just be with me?'",
        "'I'm sorry. I was wrong about that.'"
    ]
    for s in scripts:
        doc.add_text(55, y, s, 'F4', 9, 0.2)
        y -= 16

    # Page 9: Fatherhood Struggles
    doc.new_page()
    doc.add_centered_text(590, "FATHERHOOD STRUGGLES VALIDATION", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Things no one tells dads:", 'F2', 10, 0)
    y -= 18
    dad_truths = ["You might not bond immediately - that's normal",
                  "You can love your kids AND miss your old life",
                  "Postpartum depression affects dads too (10%)",
                  "Feeling like a provider isn't enough is common",
                  "Your own father wounds show up when you become a dad",
                  "It's okay to not know what you're doing",
                  "Needing time alone doesn't make you selfish"]
    for t in dad_truths:
        doc.add_text(60, y, f"- {t}", 'F1', 9, 0.2)
        y -= 15
    y -= 15
    doc.add_text(50, y, "What I wish I could tell someone about being a dad:", 'F2', 9, 0)
    y -= 16
    for i in range(4):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14

    # Page 10: Work-Life Boundaries
    doc.new_page()
    doc.add_centered_text(590, "WORK-LIFE BOUNDARIES", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Your worth is not your productivity.", 'F2', 10, 0)
    y -= 22
    doc.add_text(50, y, "Current work hours per week (honestly): ___", 'F1', 9, 0.2)
    y -= 18
    doc.add_text(50, y, "Ideal work hours: ___", 'F1', 9, 0.2)
    y -= 18
    doc.add_text(50, y, "What I sacrifice for work: _________________________________________", 'F1', 9, 0.2)
    y -= 18
    doc.add_text(50, y, "One boundary I could set this week: _________________________________", 'F1', 9, 0.2)
    y -= 25
    doc.add_text(50, y, "Signs of burnout:", 'F2', 9, 0)
    y -= 16
    burnout = ["Dreading every morning", "Physical exhaustion that rest doesn't fix",
               "Cynicism about everything", "Feeling like nothing matters",
               "Using substances to cope with work stress"]
    for b in burnout:
        doc.add_rect(50, y-3, 10, 10)
        doc.add_text(65, y, b, 'F1', 9, 0.2)
        y -= 15

    # Page 11: Substance Use Self-Check
    doc.new_page()
    doc.add_centered_text(590, "SUBSTANCE USE SELF-CHECK", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Honest assessment (no judgment, just awareness):", 'F2', 10, 0)
    y = 530
    qs = ["Do I drink/use more than I intend to?",
          "Do I need it to relax or sleep?",
          "Would I feel anxious without it?",
          "Has someone expressed concern?",
          "Do I hide how much I use?",
          "Is it causing problems at work/home?",
          "Am I using it to avoid feelings?"]
    for q in qs:
        doc.add_rect(50, y-3, 10, 10)
        doc.add_text(65, y, q, 'F1', 9, 0.2)
        y -= 16
    y -= 15
    doc.add_text(50, y, "If you checked 2+, consider talking to someone.", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "SAMHSA Helpline: 1-800-662-4357 (free, confidential)", 'F1', 9, 0.2)

    # Page 12: Friendship and Isolation
    doc.new_page()
    doc.add_centered_text(590, "FRIENDSHIP AND ISOLATION", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Men lose friends as they age. This is an epidemic.", 'F1', 10, 0.2)
    y -= 20
    doc.add_text(50, y, "My close friends (who I can really talk to): ___", 'F1', 9, 0.2)
    y -= 18
    doc.add_text(50, y, "Last time I hung out with a friend: _________________________________", 'F1', 9, 0.2)
    y -= 18
    doc.add_text(50, y, "Last time I told a friend how I'm really doing: ____________________", 'F1', 9, 0.2)
    y -= 22
    doc.add_text(50, y, "Ways to build connection:", 'F2', 9, 0)
    y -= 16
    ways = ["Join a league/club/group (sports, hobby, church)",
            "Be the one to reach out first", "Say yes to one invitation this week",
            "Start a regular thing (weekly basketball, monthly dinner)",
            "Be vulnerable with ONE person about how you're really doing"]
    for w in ways:
        doc.add_text(60, y, f"- {w}", 'F1', 9, 0.2)
        y -= 14

    # Page 13: Physical-Mental Connection
    doc.new_page()
    doc.add_centered_text(590, "PHYSICAL + MENTAL HEALTH CONNECTION", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Your body and mind are the same system:", 'F1', 10, 0.2)
    y -= 20
    doc.add_text(50, y, "Current sleep (hours/quality): _____________________________________", 'F1', 9, 0.2)
    y -= 16
    doc.add_text(50, y, "Exercise this week: ________________________________________________", 'F1', 9, 0.2)
    y -= 16
    doc.add_text(50, y, "Nutrition (honest): ________________________________________________", 'F1', 9, 0.2)
    y -= 16
    doc.add_text(50, y, "Water intake: _____________________________________________________", 'F1', 9, 0.2)
    y -= 16
    doc.add_text(50, y, "Substances used: ___________________________________________________", 'F1', 9, 0.2)
    y -= 16
    doc.add_text(50, y, "Screen time: _______________________________________________________", 'F1', 9, 0.2)
    y -= 22
    doc.add_text(50, y, "ONE physical change I'll make this week:", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)

    # Pages 14-28: Daily Check-In (15 pages)
    for day in range(15):
        doc.new_page()
        doc.add_centered_text(590, f"DAILY CHECK-IN - Day {day+1}", 'F2', 12, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 558
        doc.add_text(50, y, "Date: _______________", 'F1', 9, 0.3)
        y -= 20
        doc.add_text(50, y, "Mood (1-10): ___  Energy (1-10): ___  Sleep (hours): ___", 'F1', 9, 0.2)
        y -= 22
        doc.add_text(50, y, "One honest thought (what's really on my mind):", 'F2', 9, 0)
        y -= 16
        for i in range(4):
            doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
            y -= 14
        y -= 10
        doc.add_text(50, y, "One thing I need right now:", 'F2', 9, 0)
        y -= 16
        for i in range(2):
            doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
            y -= 14
        y -= 10
        doc.add_text(50, y, "One win today (any size):", 'F2', 9, 0)
        y -= 16
        for i in range(2):
            doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
            y -= 14
        y -= 10
        doc.add_text(50, y, "Did I connect with someone? [ ] Yes [ ] No", 'F1', 9, 0.2)
        y -= 16
        doc.add_text(50, y, "Did I move my body? [ ] Yes [ ] No", 'F1', 9, 0.2)

    # Page 29: When to Get Professional Help
    doc.new_page()
    doc.add_centered_text(590, "WHEN TO GET PROFESSIONAL HELP", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Consider therapy or counseling if:", 'F2', 10, 0)
    y -= 18
    signs = ["You're thinking about not being alive",
             "Anger is damaging relationships",
             "Substances are the only way you cope",
             "You feel nothing (numbness for weeks)",
             "Sleep is consistently terrible",
             "You're isolating from everyone",
             "Work performance is declining",
             "Physical symptoms with no medical cause"]
    for s in signs:
        doc.add_text(60, y, f"- {s}", 'F1', 9, 0.2)
        y -= 14
    y -= 15
    doc.add_text(50, y, "Resources:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "988 Suicide & Crisis Lifeline: Call or text 988", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Veterans Crisis Line: 988, then press 1", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "SAMHSA: 1-800-662-4357", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Therapy for Black Men: therapyforblackmen.org", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Man Therapy: mantherapy.org", 'F1', 9, 0.2)

    # Page 30: Personal Commitment
    doc.new_page()
    doc.add_centered_text(590, "MY PERSONAL COMMITMENT TO HEALING", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "I commit to:", 'F2', 11, 0)
    y -= 20
    commitments = [
        "Being honest with myself about how I'm doing",
        "Asking for help when I need it",
        "Not numbing my pain with ___________________",
        "Connecting with at least one person per week",
        "Moving my body regularly",
        "Being patient with my own healing",
        "Remembering that vulnerability is strength"
    ]
    for c in commitments:
        doc.add_rect(50, y-3, 10, 10)
        doc.add_text(65, y, c, 'F1', 9, 0.2)
        y -= 18
    y -= 20
    doc.add_text(50, y, "Signed: ____________________________  Date: __________", 'F1', 10, 0.2)
    y -= 30
    doc.add_text(50, y, "You are not broken. You are a man who feels deeply.", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "That is not weakness. That is being fully human.", 'F4', 10, 0.2)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book149_Mens_Mental_Health_Journal.pdf')
    print("Book149_Mens_Mental_Health_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
