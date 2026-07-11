"""Book 204: GOD IS BIGGER THAN MY ANXIETY - A Faith-Based CBT Workbook for Christian Teens"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.95)
    pdf.add_centered_text(620, "GOD IS BIGGER THAN", 'F2', 26)
    pdf.add_centered_text(585, "MY ANXIETY", 'F2', 26)
    pdf.add_centered_text(545, "A Faith-Based CBT Workbook for Christian Teens", 'F4', 13, 0.2)
    pdf.add_centered_text(500, "You are not alone. God gets it.", 'F1', 12, 0.3)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "GOD IS BIGGER THAN MY ANXIETY", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "If you are in crisis: 988 Suicide & Crisis Lifeline", 'F2', 9)
    pdf.add_text(72, 615, "This workbook does not replace professional help.", 'F1', 9)
    pdf.add_text(72, 590, "Published by KIDLYTICAL Books", 'F1', 9)

    # What is Anxiety (teen-friendly)
    pdf.new_page()
    pdf.add_centered_text(750, "WHAT IS ANXIETY?", 'F2', 20)
    pdf.add_centered_text(725, "(And why does it feel so awful?)", 'F1', 11, 0.4)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    content = [
        "Anxiety is your brain's alarm system going off - even when there's no fire.",
        "",
        "It can feel like:",
        "  - Your heart racing",
        "  - Can't catch your breath",
        "  - Stomach in knots",
        "  - Mind won't stop racing",
        "  - Wanting to hide or run away",
        "",
        "HERE'S THE TRUTH:",
        "  - You are NOT crazy",
        "  - You are NOT weak",
        "  - You are NOT a bad Christian",
        "  - Anxiety is super common in teens (you're not alone!)",
        "",
        "WHAT GOD SAYS:",
        "'For I am the LORD your God who takes hold of your right hand",
        " and says to you, Do not fear; I will help you.' - Isaiah 41:13",
    ]
    y = 690
    for line in content:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    # God Gets It page
    pdf.new_page()
    pdf.add_centered_text(750, "GOD GETS IT", 'F2', 20)
    pdf.add_centered_text(725, "Jesus Felt Anxious Too", 'F5', 13)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    content2 = [
        "In the Garden of Gethsemane (Matthew 26:36-39), Jesus felt:",
        "",
        "  - 'Sorrowful and deeply distressed' (v.37)",
        "  - So stressed his sweat was like drops of blood (Luke 22:44)",
        "  - He asked God to take the cup away (v.39)",
        "",
        "Jesus - God in human form - experienced extreme distress.",
        "He didn't sin. He prayed. He was honest with God.",
        "",
        "This means:",
        "  - Feeling anxious is NOT a sin",
        "  - God understands exactly how you feel",
        "  - You can be honest with God about your fears",
        "  - Jesus is not disappointed in you",
        "",
        "'For we do not have a high priest who is unable to empathize",
        " with our weaknesses.' - Hebrews 4:15",
        "",
        "Write: When have you felt like God didn't understand?",
    ]
    y = 690
    for line in content2:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16
    y -= 5
    pdf.add_line(72, y, 540, y, 0.5, 0.7)
    y -= 16
    pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # My Anxiety Profile
    pdf.new_page()
    pdf.add_centered_text(750, "MY ANXIETY PROFILE", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "Let's figure out YOUR anxiety. Check what applies:", 'F1', 11)
    y = 685
    checks = [
        "I worry about school/grades",
        "I worry about what people think of me",
        "I have trouble sleeping because of worry",
        "I avoid social situations",
        "I get nervous before tests/presentations",
        "I worry about my family",
        "I feel like something bad will happen",
        "I check my phone constantly for messages",
        "I have panic attacks",
        "I worry about the future",
    ]
    for c in checks:
        pdf.add_rect(72, y - 10, 10, 10, 0.5, 0.5)
        pdf.add_text(90, y - 8, c, 'F1', 10)
        y -= 22

    y -= 15
    pdf.add_text(72, y, "My anxiety is worst when:", 'F2', 10)
    y -= 18
    pdf.add_line(72, y, 540, y, 0.5, 0.7)
    y -= 20
    pdf.add_text(72, y, "My body feels it here:", 'F2', 10)
    y -= 18
    pdf.add_line(72, y, 540, y, 0.5, 0.7)
    y -= 20
    pdf.add_text(72, y, "On a scale of 1-10, my average anxiety level is: ____", 'F1', 10)

    # Thinking Traps + Biblical Truth (6 pages)
    traps = [
        ("CATASTROPHIZING", "Thinking the worst will happen",
         "Example: 'If I fail this test, my life is over!'",
         "Truth: Matthew 6:34 - Don't worry about tomorrow. Each day has enough trouble.",
         "Reframe: 'One test doesn't define my future. God has plans for me.'"),
        ("MIND READING", "Assuming you know what others think",
         "Example: 'Everyone thinks I'm weird.'",
         "Truth: 1 Samuel 16:7 - People look at the outside; God looks at the heart.",
         "Reframe: 'I can't actually read minds. Some people might like me!'"),
        ("ALL-OR-NOTHING", "Everything is either perfect or terrible",
         "Example: 'I got a B. I'm a total failure.'",
         "Truth: Romans 3:23 - All fall short. Grace is for imperfect people.",
         "Reframe: 'A B is good! I don't have to be perfect to have value.'"),
        ("FORTUNE TELLING", "Predicting the future negatively",
         "Example: 'I know the party will be awkward.'",
         "Truth: James 4:14 - You don't know what tomorrow brings.",
         "Reframe: 'I've been surprised before. It might actually be fun.'"),
        ("FILTERING", "Only seeing the negative",
         "Example: '20 people liked my post but 1 didn't - I'm unlikable.'",
         "Truth: Philippians 4:8 - Think on what is good, lovely, praiseworthy.",
         "Reframe: 'Let me focus on the 20 who liked it!'"),
        ("SHOULD STATEMENTS", "Rigid rules for yourself",
         "Example: 'I should always have it together. Christians don't struggle.'",
         "Truth: 2 Corinthians 12:9 - God's power is made perfect in weakness.",
         "Reframe: 'It's okay to struggle. That's when God shows up most.'"),
    ]
    for trap_name, definition, example, truth, reframe in traps:
        pdf.new_page()
        pdf.add_centered_text(750, f"THINKING TRAP: {trap_name}", 'F2', 15)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        pdf.add_text(72, 710, f"What it is: {definition}", 'F1', 11)
        pdf.add_text(72, 685, example, 'F3', 10, 0.3)
        pdf.add_text(72, 655, "BIBLICAL TRUTH:", 'F2', 11)
        pdf.add_text(82, 635, truth, 'F4', 10)
        pdf.add_text(72, 610, "REFRAME:", 'F2', 11)
        pdf.add_text(82, 590, reframe, 'F1', 10)

        pdf.add_text(72, 555, "YOUR TURN:", 'F2', 12)
        pdf.add_text(72, 535, "A time I fell into this trap:", 'F1', 10)
        pdf.add_line(72, 515, 540, 515, 0.5, 0.7)
        pdf.add_line(72, 497, 540, 497, 0.5, 0.7)
        pdf.add_text(72, 470, "The truth I can tell myself instead:", 'F1', 10)
        pdf.add_line(72, 450, 540, 450, 0.5, 0.7)
        pdf.add_line(72, 432, 540, 432, 0.5, 0.7)
        pdf.add_text(72, 405, "A verse that helps me:", 'F1', 10)
        pdf.add_line(72, 385, 540, 385, 0.5, 0.7)

    # Brave Ladder with God
    pdf.new_page()
    pdf.add_centered_text(750, "MY BRAVE LADDER WITH GOD", 'F2', 16)
    pdf.add_centered_text(728, "Face your fears one step at a time - with prayer at each step!", 'F1', 10, 0.4)
    pdf.add_line(72, 718, 540, 718, 1, 0.5)
    y = 690
    for step in range(10, 0, -1):
        pdf.add_text(72, y, f"Step {step} (Fear: {step*10}%)", 'F2', 10)
        pdf.add_line(180, y - 2, 400, y - 2, 0.5, 0.7)
        pdf.add_text(410, y, "Prayer:", 'F1', 9, 0.4)
        pdf.add_line(450, y - 2, 540, y - 2, 0.5, 0.7)
        y -= 30

    pdf.add_text(72, y - 10, "Start at step 1. You've got this. God's got you.", 'F5', 10, 0.3)

    # Calm-Down Toolkit
    pdf.new_page()
    pdf.add_centered_text(750, "MY CALM-DOWN TOOLKIT", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "BREATHING (4-7-8):", 'F2', 11)
    pdf.add_text(82, 692, "Breathe in for 4... Hold for 7... Out for 8...", 'F1', 10)
    pdf.add_text(72, 660, "5-4-3-2-1 GROUNDING + GOD IS HERE:", 'F2', 11)
    grounding = [
        "5 things I can SEE (God made each one)",
        "4 things I can TOUCH (God is near)",
        "3 things I can HEAR (God speaks peace)",
        "2 things I can SMELL (God provides)",
        "1 thing I can TASTE (taste and see God is good!)"
    ]
    y = 642
    for g in grounding:
        pdf.add_text(82, y, g, 'F1', 10)
        y -= 16

    y -= 15
    pdf.add_text(72, y, "MY SCRIPTURE EMERGENCY KIT:", 'F2', 11)
    verses = [
        "Psalm 56:3 - When I am afraid, I will trust in you.",
        "Isaiah 41:10 - Fear not, for I am with you.",
        "Philippians 4:6-7 - The peace of God will guard your heart.",
    ]
    for v in verses:
        y -= 16
        pdf.add_text(82, y, v, 'F4', 10)

    # Social Media & Anxiety
    pdf.new_page()
    pdf.add_centered_text(750, "SOCIAL MEDIA & ANXIETY", 'F2', 16)
    pdf.add_centered_text(728, "A Faith Perspective", 'F5', 11)
    pdf.add_line(72, 718, 540, 718, 1, 0.5)
    content3 = [
        "Social media can increase anxiety because:",
        "  - Comparison (but see Galatians 6:4 - test your own work)",
        "  - FOMO (but see Psalm 16:5 - God is your portion)",
        "  - Cyberbullying (but see Psalm 27:1 - God is your light)",
        "  - Always 'on' (but see Mark 6:31 - come away and rest)",
        "",
        "HEALTHY BOUNDARIES:",
        "  - No phone 1 hour before bed",
        "  - Unfollow accounts that make you feel bad",
        "  - Set time limits on apps",
        "  - Remember: people post highlights, not reality",
        "",
        "MY SOCIAL MEDIA PLAN:",
        "  Time limit per day: ______ minutes",
        "  Accounts to unfollow: ___________",
        "  My phone-free times: ___________",
        "  What I'll do instead: ___________",
    ]
    y = 695
    for line in content3:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Weekly Trackers (5 pages)
    for week in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"WEEKLY CHECK-IN - WEEK {week}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        pdf.add_text(72, 710, "Day   Anxiety(1-10)  Brave thing I did     God moment", 'F2', 9)
        y = 690
        for day in days:
            pdf.add_text(72, y, day, 'F1', 9)
            pdf.add_line(110, y - 2, 540, y - 2, 0.5, 0.7)
            y -= 22
        y -= 10
        pdf.add_text(72, y, "This week I'm proud of:", 'F2', 10)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 20
        pdf.add_text(72, y, "Next week I want to try:", 'F2', 10)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Safety Plan
    pdf.new_page()
    pdf.add_centered_text(750, "MY SAFETY PLAN", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    fields = [
        ("Warning signs that I'm not okay:", 2),
        ("Things I can do to calm down:", 2),
        ("People I can talk to:", 2),
        ("Adults who can help (parent/teacher/pastor):", 2),
        ("My therapist/counselor:", 1),
        ("Crisis number: 988 (Suicide & Crisis Lifeline)", 0),
        ("My reason to keep going:", 2),
        ("God's promise to me:", 2),
    ]
    y = 710
    for label, lines in fields:
        pdf.add_text(72, y, label, 'F2', 10)
        y -= 5
        for _ in range(lines):
            y -= 16
            pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 18

    # Resources
    pdf.new_page()
    pdf.add_centered_text(750, "RESOURCES", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    resources = [
        "988 Suicide & Crisis Lifeline: Call or text 988",
        "Crisis Text Line: Text HOME to 741741",
        "NAMI (National Alliance on Mental Illness): nami.org",
        "Your church youth pastor or counselor",
        "School counselor",
        "Christian counseling: faithfulcounseling.com",
    ]
    y = 710
    for r in resources:
        pdf.add_text(72, y, r, 'F1', 11)
        y -= 22

    y -= 20
    pdf.add_text(72, y, "A LETTER FROM GOD TO YOU:", 'F2', 14)
    y -= 25
    letter = [
        "Dear one, I see you. I know you're scared.",
        "I am not angry at you for feeling anxious.",
        "I made you, I know you, and I am with you.",
        "You are brave for picking up this book.",
        "I will never leave you or forsake you.",
        "One day at a time. I've got you.",
        "   - Your Heavenly Father",
        "",
        "(Isaiah 43:1, Psalm 139, Deuteronomy 31:6, Hebrews 13:5)"
    ]
    for line in letter:
        pdf.add_text(100, y, line, 'F4', 11)
        y -= 18

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book204_CBT_Anxiety_Christian_Teens.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
