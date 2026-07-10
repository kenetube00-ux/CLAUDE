"""Book 141: Healing from Trauma - A Workbook for Teens Ages 13-18"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(520, "HEALING FROM TRAUMA", 'F2', 28, 0)
    doc.add_centered_text(480, "A Workbook for Teens Ages 13-18", 'F4', 18, 0.2)
    doc.add_centered_text(400, "You survived something hard.", 'F4', 14, 0.3)
    doc.add_centered_text(375, "This workbook helps you heal.", 'F4', 14, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(600, "HEALING FROM TRAUMA", 'F2', 14, 0)
    doc.add_text(72, 500, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.3)
    doc.add_text(72, 470, "IMPORTANT: This workbook is not therapy. If you are in crisis:", 'F2', 10, 0.3)
    doc.add_text(72, 450, "Call 988 | Text HOME to 741741 | Tell a trusted adult", 'F1', 10, 0.3)

    # Page 3: What is Trauma
    doc.new_page()
    doc.add_centered_text(740, "WHAT IS TRAUMA?", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Trauma is what happens INSIDE you after something bad happens.", 'F2', 11, 0.2)
    doc.add_text(72, 678, "It's not about what happened being 'bad enough.' If it affected you, it counts.", 'F1', 11, 0.2)
    y = 648
    doc.add_text(72, y, "Trauma can come from:", 'F1', 11, 0.2)
    y -= 20
    sources = ["Abuse (physical, emotional, sexual)", "Neglect or abandonment",
               "Bullying or cyberbullying", "Witnessing violence", "Loss of someone you love",
               "Accidents or medical trauma", "Natural disasters", "Community violence",
               "Divorce or family chaos", "Anything that made you feel unsafe or helpless"]
    for s in sources:
        doc.add_text(90, y, f"- {s}", 'F1', 11, 0.2)
        y -= 18
    y -= 15
    doc.add_text(72, y, "YOUR EXPERIENCE IS VALID. You don't need to compare your pain to others.", 'F2', 11, 0)

    # Page 4: How Trauma Affects Brain & Body
    doc.new_page()
    doc.add_centered_text(740, "HOW TRAUMA AFFECTS YOUR BRAIN & BODY", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "After trauma, your brain gets stuck in 'survival mode.' This causes:", 'F1', 11, 0.2)
    y = 672
    effects = [
        ("BRAIN:", "Trouble concentrating, memory gaps, nightmares, flashbacks"),
        ("BODY:", "Stomachaches, headaches, muscle tension, fatigue, startle response"),
        ("EMOTIONS:", "Anger outbursts, numbness, anxiety, sadness, shame, mood swings"),
        ("BEHAVIOR:", "Isolation, risk-taking, sleep changes, avoiding reminders"),
        ("RELATIONSHIPS:", "Trust issues, pushing people away, people-pleasing")
    ]
    for area, desc in effects:
        doc.add_text(72, y, area, 'F2', 11, 0)
        doc.add_text(160, y, desc, 'F1', 10, 0.2)
        y -= 28
    y -= 15
    doc.add_text(72, y, "IMPORTANT: These are NORMAL responses to ABNORMAL events.", 'F2', 12, 0)
    y -= 22
    doc.add_text(72, y, "Your brain is trying to protect you. It just needs help knowing you're safe now.", 'F1', 11, 0.2)

    # Page 5: Am I Safe Now?
    doc.new_page()
    doc.add_centered_text(740, "AM I SAFE NOW? (Safety Assessment)", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Before healing can start, you need to feel safe. Let's check:", 'F1', 11, 0.2)
    y = 670
    questions = [
        "Am I physically safe right now? (not being hurt)", 
        "Do I have a safe place to sleep?",
        "Is there at least ONE adult I can trust?",
        "Am I still in contact with the person who hurt me?",
        "Do I have basic needs met (food, shelter, safety)?",
        "Am I currently hurting myself?"
    ]
    for q in questions:
        doc.add_rect(72, y-3, 12, 12)
        doc.add_text(90, y, q, 'F1', 11, 0.2)
        y -= 25
    y -= 15
    doc.add_filled_rect(72, y-5, 468, 50, 0.9)
    doc.add_text(80, y+25, "If you answered NO to safety questions or YES to being hurt:", 'F2', 10, 0)
    doc.add_text(80, y+8, "TELL SOMEONE. A teacher, counselor, coach, or call: Childhelp 1-800-422-4453", 'F2', 10, 0)
    y -= 70
    doc.add_text(72, y, "My safe people right now:", 'F2', 12, 0)
    y -= 22
    for i in range(3):
        doc.add_text(72, y, f"{i+1}. Name: _______________________ How to reach them: _____________", 'F1', 11, 0.2)
        y -= 22

    # Page 6: Window of Tolerance
    doc.new_page()
    doc.add_centered_text(740, "MY WINDOW OF TOLERANCE", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Your 'window of tolerance' is where you feel okay - not too hyped, not too numb.", 'F1', 11, 0.2)
    y = 665
    doc.add_text(72, y, "HYPERAROUSAL (above the window):", 'F2', 11, 0)
    y -= 18
    doc.add_text(90, y, "Anxiety, panic, rage, racing thoughts, can't sit still, reactive", 'F1', 10, 0.3)
    y -= 25
    doc.add_filled_rect(72, y-5, 468, 40, 0.88)
    doc.add_text(200, y+12, "WINDOW OF TOLERANCE", 'F2', 12, 0)
    doc.add_text(150, y-5, "(calm enough to think, feel, and cope)", 'F1', 10, 0.3)
    y -= 55
    doc.add_text(72, y, "HYPOAROUSAL (below the window):", 'F2', 11, 0)
    y -= 18
    doc.add_text(90, y, "Numbness, spacing out, exhaustion, disconnected, can't feel anything", 'F1', 10, 0.3)
    y -= 35
    doc.add_text(72, y, "Right now, I usually spend time:", 'F2', 11, 0)
    y -= 20
    doc.add_rect(72, y-3, 12, 12)
    doc.add_text(90, y, "Above (hyper - too activated)", 'F1', 11, 0.2)
    y -= 20
    doc.add_rect(72, y-3, 12, 12)
    doc.add_text(90, y, "In the window (mostly okay)", 'F1', 11, 0.2)
    y -= 20
    doc.add_rect(72, y-3, 12, 12)
    doc.add_text(90, y, "Below (hypo - shut down)", 'F1', 11, 0.2)
    y -= 30
    doc.add_text(72, y, "Things that push me OUT of my window:", 'F1', 11, 0.2)
    y -= 20
    for i in range(3):
        doc.add_text(72, y, f"_____________________________________________________________________", 'F1', 10, 0.3)
        y -= 18

    # Page 7: Grounding Techniques
    doc.new_page()
    doc.add_centered_text(740, "GROUNDING TECHNIQUES FOR TEENS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "When you're triggered or dissociating, these bring you back to NOW:", 'F1', 11, 0.2)
    y = 670
    doc.add_text(72, y, "5-4-3-2-1 TECHNIQUE:", 'F2', 12, 0)
    y -= 20
    senses = ["5 things you can SEE", "4 things you can TOUCH", "3 things you can HEAR",
              "2 things you can SMELL", "1 thing you can TASTE"]
    for s in senses:
        doc.add_text(90, y, f"- {s}", 'F1', 11, 0.2)
        y -= 18
    y -= 15
    doc.add_text(72, y, "ICE CUBE TECHNIQUE:", 'F2', 12, 0)
    y -= 18
    doc.add_text(90, y, "Hold ice in your hands. Focus on the cold. It brings you to present.", 'F1', 11, 0.2)
    y -= 25
    doc.add_text(72, y, "MUSIC GROUNDING:", 'F2', 12, 0)
    y -= 18
    doc.add_text(90, y, "Put on a song you love. Focus on every instrument, every word.", 'F1', 11, 0.2)
    y -= 25
    doc.add_text(72, y, "MOVEMENT:", 'F2', 12, 0)
    y -= 18
    doc.add_text(90, y, "Jump, dance, do pushups, stomp your feet. Get back in your body.", 'F1', 11, 0.2)
    y -= 30
    doc.add_text(72, y, "The grounding technique that works best for ME:", 'F2', 11, 0)
    y -= 22
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)

    # Page 8: Triggers & Warning Signs
    doc.new_page()
    doc.add_centered_text(740, "MY TRIGGERS & EARLY WARNING SIGNS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Triggers are things that remind your brain of the trauma:", 'F1', 11, 0.2)
    y = 672
    doc.add_text(72, y, "My triggers (people, places, sounds, smells, dates, situations):", 'F2', 11, 0)
    y -= 22
    for i in range(5):
        doc.add_text(72, y, f"{i+1}. _____________________________________________________________", 'F1', 11, 0.2)
        y -= 22
    y -= 15
    doc.add_text(72, y, "Early warning signs I'm getting triggered:", 'F2', 11, 0)
    y -= 22
    doc.add_text(72, y, "In my body: ________________________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "In my thoughts: ____________________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "In my behavior: ____________________________________________________", 'F1', 11, 0.2)
    y -= 30
    doc.add_text(72, y, "My plan when triggered:", 'F2', 11, 0)
    y -= 22
    doc.add_text(72, y, "1. ________________________________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "2. ________________________________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "3. ________________________________________________________________", 'F1', 11, 0.2)

    # Page 9: Healthy vs Unhealthy Coping
    doc.new_page()
    doc.add_centered_text(740, "HEALTHY COPING vs UNHEALTHY COPING", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "No judgment. You survived however you could. Now let's find safer ways.", 'F1', 11, 0.2)
    y = 675
    doc.add_filled_rect(72, y-2, 230, 20, 0.85)
    doc.add_filled_rect(310, y-2, 230, 20, 0.85)
    doc.add_text(120, y+2, "UNHEALTHY (makes sense but hurts)", 'F2', 8, 0)
    doc.add_text(360, y+2, "HEALTHY (try these instead)", 'F2', 8, 0)
    y -= 25
    pairs = [
        ("Self-harm", "Ice cube, red marker, snapping rubber band"),
        ("Isolating completely", "Text one person, sit near others"),
        ("Substances", "Exercise, cold water, intense music"),
        ("Risky behavior", "Safe thrills: roller coasters, spicy food"),
        ("Exploding at people", "Journaling, punching pillow, running"),
        ("Starving/bingeing", "Eating one small thing, telling someone"),
        ("Numbing out (screens 24/7)", "10 min outside, grounding exercise")
    ]
    for unhealthy, healthy in pairs:
        doc.add_text(75, y, unhealthy, 'F1', 10, 0.2)
        doc.add_text(315, y, healthy, 'F1', 10, 0.2)
        doc.add_line(72, y-8, 540, y-8, 0.3, 0.8)
        y -= 25

    # Page 10: Processing Feelings
    doc.new_page()
    doc.add_centered_text(740, "PROCESSING FEELINGS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Trauma can make it hard to know what you're feeling. Let's practice:", 'F1', 11, 0.2)
    y = 670
    doc.add_text(72, y, "EMOTION WHEEL - Today I feel (circle all that apply):", 'F2', 11, 0)
    y -= 22
    emotions = ["Angry - frustrated - annoyed - rage - irritated",
                "Sad - lonely - hopeless - grieving - empty",
                "Scared - anxious - panicked - worried - on edge",
                "Ashamed - guilty - embarrassed - worthless - dirty",
                "Numb - disconnected - foggy - frozen - nothing",
                "Happy - calm - grateful - hopeful - proud"]
    for e in emotions:
        doc.add_text(90, y, e, 'F1', 10, 0.2)
        y -= 18
    y -= 15
    doc.add_text(72, y, "Where do I feel this in my body? (check):", 'F2', 11, 0)
    y -= 20
    body_parts = ["Head/face", "Throat/chest", "Stomach", "Hands/arms", "Legs", "All over"]
    for b in body_parts:
        doc.add_rect(72, y-3, 10, 10)
        doc.add_text(88, y, b, 'F1', 10, 0.2)
        y -= 18

    # Page 11: Safe People List
    doc.new_page()
    doc.add_centered_text(740, "BUILDING MY SAFE PEOPLE LIST", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    doc.add_text(72, y, "Not everyone needs to know everything. Different people for different needs:", 'F1', 11, 0.2)
    y -= 30
    categories = [
        ("Person I can talk to about ANYTHING:", 3),
        ("Person who makes me laugh:", 2),
        ("Adult I trust at school:", 2),
        ("Person I can call at 2am:", 2),
        ("Online community that gets it:", 2)
    ]
    for cat, lines in categories:
        doc.add_text(72, y, cat, 'F2', 11, 0)
        y -= 22
        for i in range(lines):
            doc.add_text(72, y, "_______________________________________________________________", 'F1', 10, 0.3)
            y -= 18
        y -= 15

    # Page 12: Self-Care Menu
    doc.new_page()
    doc.add_centered_text(740, "MY SELF-CARE MENU", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    menus = [
        ("PHYSICAL:", ["Walk/run/dance", "Take a shower", "Eat something nourishing", "Sleep", "Stretch"]),
        ("EMOTIONAL:", ["Journal", "Cry (it's okay!)", "Talk to someone", "Create art/music", "Watch comfort show"]),
        ("SOCIAL:", ["Text a friend", "Sit with someone", "Join an activity", "Help someone else", "Hug someone safe"]),
        ("SPIRITUAL:", ["Spend time in nature", "Pray/meditate", "Listen to meaningful music", "Practice gratitude", "Journal about purpose"])
    ]
    for cat, items in menus:
        doc.add_text(72, y, cat, 'F2', 12, 0)
        y -= 18
        for item in items:
            doc.add_text(90, y, f"- {item}", 'F1', 10, 0.2)
            y -= 16
        y -= 12

    # Pages 13-20: Weekly Check-In (8 pages)
    for week in range(8):
        doc.new_page()
        doc.add_centered_text(740, f"WEEKLY CHECK-IN - Week {week+1}", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        doc.add_text(72, y, "Date range: _______________________", 'F1', 10, 0.3)
        y -= 25
        doc.add_text(72, y, "Overall mood this week (1-10): ___", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "Times I was triggered: ___", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "Coping skills I used: _____________________________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "Something hard this week: __________________________________________", 'F1', 11, 0.2)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "Something good this week: __________________________________________", 'F1', 11, 0.2)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "Person I connected with: ___________________________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "Self-care I did: ___________________________________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "Am I sleeping okay? ___  Eating okay? ___", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "One thing I'm proud of myself for: _________________________________", 'F1', 11, 0.2)

    # Page 21: Healing Journey Milestones
    doc.new_page()
    doc.add_centered_text(740, "MY HEALING JOURNEY MILESTONES", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    milestones = ["Acknowledged what happened to me", "Told someone I trust",
                  "Used a coping skill instead of hurting myself", "Slept through the night",
                  "Felt safe for a moment", "Went a day without being triggered",
                  "Asked for help", "Set a boundary", "Felt a positive emotion",
                  "Realized it wasn't my fault"]
    for m in milestones:
        doc.add_rect(72, y-3, 12, 12)
        doc.add_text(90, y, m, 'F1', 11, 0.2)
        doc.add_text(430, y, "Date: _______", 'F1', 9, 0.3)
        y -= 25

    # Page 22: Resources for Teens
    doc.new_page()
    doc.add_centered_text(740, "RESOURCES FOR TEENS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    resources = [
        ("Crisis:", "Call/Text 988 | Crisis Text Line: Text HOME to 741741"),
        ("Child Abuse:", "Childhelp National Hotline: 1-800-422-4453"),
        ("Sexual Assault:", "RAINN: 1-800-656-4673 | rainn.org"),
        ("Trevor Project:", "LGBTQ+ youth: 1-866-488-7386"),
        ("Teen Line:", "1-800-852-8336 (peer support)"),
        ("Your Life Your Voice:", "1-800-448-3000 (Boys Town)")
    ]
    for title, info in resources:
        doc.add_text(72, y, title, 'F2', 11, 0)
        doc.add_text(200, y, info, 'F1', 10, 0.2)
        y -= 25

    # Page 23: Letter to Myself
    doc.new_page()
    doc.add_centered_text(740, "LETTER TO MYSELF:", 'F2', 14, 0)
    doc.add_centered_text(715, "I AM MORE THAN WHAT HAPPENED TO ME", 'F2', 14, 0)
    doc.add_line(72, 705, 540, 705, 1, 0.5)
    doc.add_text(72, 680, "Dear Me,", 'F4', 12, 0.2)
    y = 650
    for i in range(22):
        doc.add_text(72, y, "_" * 70, 'F1', 11, 0.4)
        y -= 24
    y -= 10
    doc.add_text(72, y, "With love and strength, ___________", 'F4', 12, 0.2)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book141_Trauma_Workbook_Teens.pdf')
    print("Book141_Trauma_Workbook_Teens.pdf created successfully!")

if __name__ == "__main__":
    create_book()
