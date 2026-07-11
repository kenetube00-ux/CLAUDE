"""Book 209: HE HEALS THE BROKENHEARTED - A Faith-Integrated PTSD Recovery Workbook"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.95)
    pdf.add_centered_text(620, "HE HEALS THE", 'F2', 26)
    pdf.add_centered_text(585, "BROKENHEARTED", 'F2', 26)
    pdf.add_centered_text(545, "A Faith-Integrated PTSD Recovery Workbook", 'F4', 13, 0.2)
    pdf.add_centered_text(510, "Psalm 147:3 - He heals the broken in heart", 'F4', 11, 0.3)
    pdf.add_centered_text(487, "and binds up their wounds.", 'F4', 11, 0.3)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright
    pdf.new_page()
    pdf.add_text(72, 700, "HE HEALS THE BROKENHEARTED", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "IMPORTANT: This workbook does NOT replace trauma therapy.", 'F2', 9)
    pdf.add_text(72, 615, "Please work with a licensed therapist trained in trauma.", 'F1', 9)
    pdf.add_text(72, 595, "Crisis: 988 Lifeline | PTSD Helpline: 1-800-662-4357", 'F2', 9)
    pdf.add_text(72, 570, "Published by KIDLYTICAL Books", 'F1', 9)

    # Understanding PTSD through faith
    pdf.new_page()
    pdf.add_centered_text(750, "UNDERSTANDING PTSD THROUGH FAITH", 'F2', 16)
    pdf.add_centered_text(728, "Psalm 34:18 - The LORD is close to the brokenhearted", 'F5', 10)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    content = [
        "PTSD (Post-Traumatic Stress Disorder) happens when your brain",
        "gets stuck in 'danger mode' after a traumatic event.",
        "",
        "Symptoms include:",
        "  - Flashbacks and nightmares",
        "  - Hypervigilance (always on alert)",
        "  - Avoidance of reminders",
        "  - Emotional numbness",
        "  - Difficulty sleeping",
        "  - Feeling disconnected from others (including God)",
        "",
        "PTSD is NOT:",
        "  - A sign of weakness",
        "  - Punishment from God",
        "  - Something you should 'just get over'",
        "  - A lack of faith",
        "",
        "PTSD IS a normal response to abnormal events.",
        "Even warriors in the Bible showed trauma responses.",
        "God is NOT distant. He is close (Psalm 34:18).",
    ]
    y = 690
    for line in content:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Safety Plan
    pdf.new_page()
    pdf.add_centered_text(750, "MY SAFETY PLAN", 'F2', 18)
    pdf.add_centered_text(728, "With Spiritual Supports", 'F1', 11, 0.4)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    sections = [
        ("Warning signs I'm being triggered:", 2),
        ("Things I can do to self-soothe:", 2),
        ("People I can call:", 2),
        ("Places I feel safe:", 1),
        ("Scripture that grounds me:", 1),
        ("Prayer I can pray:", 2),
        ("My therapist (name/number):", 1),
        ("Crisis number: 988", 0),
        ("Church support (pastor/group):", 1),
        ("Reason to keep going:", 2),
    ]
    y = 690
    for label, lines in sections:
        pdf.add_text(72, y, label, 'F2', 10)
        if lines == 0:
            y -= 18
        else:
            for _ in range(lines):
                y -= 16
                pdf.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 15

    # Grounding in God's Presence
    pdf.new_page()
    pdf.add_centered_text(750, "GROUNDING IN GOD'S PRESENCE", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "When triggered or dissociating, use 5-4-3-2-1 + GOD IS HERE:", 'F1', 10)
    grounding = [
        "5 things I can SEE (God created each one - thank Him)",
        "4 things I can TOUCH (press feet to floor - God is my foundation)",
        "3 things I can HEAR (God speaks peace into chaos)",
        "2 things I can SMELL (breathe deep - God's breath gives life)",
        "1 thing I can TASTE (taste and see that the LORD is good)",
    ]
    y = 685
    for g in grounding:
        pdf.add_text(82, y, g, 'F1', 10)
        y -= 20

    y -= 15
    pdf.add_text(72, y, "PRESENCE MEDITATION:", 'F2', 11)
    y -= 18
    meditation = [
        "'God is here. I am safe. This moment is not that moment.'",
        "'The LORD is my shepherd. I am not in danger right now.'",
        "'I am in [location]. It is [year]. I am safe.'",
        "'God holds me. I can feel my body. I am present.'",
    ]
    for m in meditation:
        pdf.add_text(82, y, m, 'F4', 10)
        y -= 16

    # Trigger Identification
    pdf.new_page()
    pdf.add_centered_text(750, "TRIGGER IDENTIFICATION + SCRIPTURE ANCHORS", 'F2', 14)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 715, "Identify triggers and pair each with a scripture anchor:", 'F1', 10)
    y = 690
    for i in range(6):
        pdf.add_text(72, y, f"Trigger {i+1}:", 'F2', 10)
        pdf.add_line(145, y - 2, 380, y - 2, 0.5, 0.7)
        y -= 18
        pdf.add_text(82, y, "Scripture anchor:", 'F1', 9)
        pdf.add_line(175, y - 2, 540, y - 2, 0.5, 0.7)
        y -= 18
        pdf.add_text(82, y, "What I'll do when triggered:", 'F1', 9)
        pdf.add_line(230, y - 2, 540, y - 2, 0.5, 0.7)
        y -= 25

    # Window of Tolerance
    pdf.new_page()
    pdf.add_centered_text(750, "WINDOW OF TOLERANCE", 'F2', 16)
    pdf.add_centered_text(728, "Psalm 46:10 - Be still and know that I am God", 'F5', 10)
    pdf.add_line(72, 715, 540, 715, 1, 0.5)
    pdf.add_text(72, 690, "HYPERAROUSAL (too activated):", 'F2', 11)
    pdf.add_text(82, 672, "Racing heart, panic, rage, can't sit still", 'F1', 10)
    pdf.add_text(82, 655, "-> Calm down: Breathe, ground, 'Be still...'", 'F1', 10, 0.3)
    pdf.add_line(72, 640, 540, 640, 1, 0.4)
    pdf.add_filled_rect(72, 560, 468, 70, 0.9)
    pdf.add_centered_text(600, "WINDOW OF TOLERANCE", 'F2', 12)
    pdf.add_centered_text(580, "(Safe zone - where healing happens)", 'F1', 10, 0.4)
    pdf.add_line(72, 555, 540, 555, 1, 0.4)
    pdf.add_text(72, 535, "HYPOAROUSAL (too shut down):", 'F2', 11)
    pdf.add_text(82, 517, "Numb, frozen, disconnected, can't feel", 'F1', 10)
    pdf.add_text(82, 500, "-> Activate: Move body, cold water, 'Awake, O my soul!'", 'F1', 10, 0.3)

    y = 460
    pdf.add_text(72, y, "Right now I am:", 'F2', 10)
    pdf.add_rect(72, y - 22, 8, 8, 0.5, 0.5)
    pdf.add_text(86, y - 20, "Hyperaroused", 'F1', 9)
    pdf.add_rect(200, y - 22, 8, 8, 0.5, 0.5)
    pdf.add_text(214, y - 20, "In my window", 'F1', 9)
    pdf.add_rect(330, y - 22, 8, 8, 0.5, 0.5)
    pdf.add_text(344, y - 20, "Hypoaroused", 'F1', 9)

    # Cognitive Processing - stuck points about God
    pdf.new_page()
    pdf.add_centered_text(750, "STUCK POINTS ABOUT GOD", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 712, "After trauma, many struggle with questions about God:", 'F1', 10)
    stuck_points = [
        ("'Why did God allow this?'", "God did not cause this. We live in a broken world. He weeps with you (John 11:35)."),
        ("'God didn't protect me'", "Evil people have free will. God promises to redeem, not to prevent all pain (Rom 8:28)."),
        ("'I must have deserved it'", "NO. God does not punish through trauma. You did not deserve this (John 9:2-3)."),
        ("'God can't be good if this happened'", "God's goodness includes being WITH you in suffering (Psalm 23:4 - through the valley)."),
    ]
    y = 688
    for stuck, truth in stuck_points:
        pdf.add_text(72, y, stuck, 'F2', 10)
        y -= 14
        words = truth.split()
        line = ""
        for w in words:
            if len(line + " " + w) > 72:
                pdf.add_text(82, y, line, 'F1', 9)
                y -= 13
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(82, y, line, 'F1', 9)
            y -= 13
        y -= 15

    # Trauma Narrative (optional)
    pdf.new_page()
    pdf.add_centered_text(750, "TRAUMA NARRATIVE (OPTIONAL)", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "IMPORTANT: Only do this with your therapist's guidance.", 'F2', 10)
    pdf.add_text(72, 690, "If you feel ready, writing your story can be part of healing.", 'F1', 10)
    pdf.add_text(72, 665, "Before writing, pray:", 'F2', 10)
    pdf.add_text(82, 645, "'Lord, be with me as I remember. You were there then.", 'F4', 10)
    pdf.add_text(82, 628, " You are here now. Keep me safe. Amen.'", 'F4', 10)

    y = 600
    pdf.add_text(72, y, "My story (what happened, what I felt, what it means now):", 'F2', 10)
    y -= 5
    while y > 120:
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    pdf.add_text(72, 100, "After writing, pray: 'Lord, I give this to You. Heal me. Amen.'", 'F4', 9, 0.3)

    # Self-Compassion
    pdf.new_page()
    pdf.add_centered_text(750, "SELF-COMPASSION AS GOD SEES YOU", 'F2', 15)
    pdf.add_centered_text(728, "Psalm 139 - You are fearfully and wonderfully made", 'F5', 10)
    pdf.add_line(72, 718, 540, 718, 1, 0.5)
    truths = [
        "God says: 'I knew you before you were born' (Jeremiah 1:5)",
        "God says: 'You are precious in my eyes' (Isaiah 43:4)",
        "God says: 'I will never leave you' (Hebrews 13:5)",
        "God says: 'Nothing can separate you from my love' (Romans 8:38-39)",
        "God says: 'I make all things new' (Revelation 21:5)",
    ]
    y = 695
    for t in truths:
        pdf.add_text(72, y, t, 'F4', 10)
        y -= 20

    y -= 15
    pdf.add_text(72, y, "Write a letter of compassion to yourself:", 'F2', 10)
    y -= 5
    for _ in range(8):
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Reclaiming Your Body
    pdf.new_page()
    pdf.add_centered_text(750, "RECLAIMING YOUR BODY AS GOD'S TEMPLE", 'F2', 14)
    pdf.add_centered_text(728, "1 Corinthians 6:19", 'F5', 10)
    pdf.add_line(72, 718, 540, 718, 1, 0.5)
    content2 = [
        "Trauma often disconnects us from our bodies.",
        "Your body is not the enemy - it is God's temple.",
        "",
        "Gentle ways to reconnect:",
        "  - Stretching while praying (yoga-style + scripture)",
        "  - Walking in nature (God's creation)",
        "  - Deep breathing (receiving God's breath of life)",
        "  - Warm bath/shower (water as cleansing/baptism)",
        "  - Noticing your body without judgment",
        "",
        "Affirmation: 'My body carried me through the worst day.",
        "It deserves kindness, not punishment. God dwells here.'",
        "",
        "What's one way I can be kind to my body today?",
    ]
    y = 695
    for line in content2:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16
    y -= 5
    pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Weekly Symptom + Faith Tracker (5 pages)
    for week in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"WEEKLY TRACKER - WEEK {week}", 'F2', 14)
        pdf.add_line(72, 735, 540, 735, 1, 0.5)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        pdf.add_text(72, 712, "Day", 'F2', 9)
        pdf.add_text(110, 712, "Distress", 'F2', 9)
        pdf.add_text(165, 712, "Sleep", 'F2', 9)
        pdf.add_text(210, 712, "Flashbacks?", 'F2', 9)
        pdf.add_text(295, 712, "Grounded?", 'F2', 9)
        pdf.add_text(375, 712, "Prayer?", 'F2', 9)
        pdf.add_text(435, 712, "Safe?", 'F2', 9)
        y = 695
        for day in days:
            pdf.add_text(72, y, day, 'F1', 9)
            pdf.add_line(110, y-2, 150, y-2, 0.5, 0.7)
            pdf.add_line(165, y-2, 200, y-2, 0.5, 0.7)
            pdf.add_line(210, y-2, 280, y-2, 0.5, 0.7)
            pdf.add_line(295, y-2, 360, y-2, 0.5, 0.7)
            pdf.add_line(375, y-2, 420, y-2, 0.5, 0.7)
            pdf.add_line(435, y-2, 480, y-2, 0.5, 0.7)
            y -= 22
        y -= 10
        pdf.add_text(72, y, "Where I saw God this week:", 'F2', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 20
        pdf.add_text(72, y, "One thing I'm grateful for:", 'F2', 10)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Post-Traumatic Growth
    pdf.new_page()
    pdf.add_centered_text(750, "POST-TRAUMATIC GROWTH THROUGH FAITH", 'F2', 14)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    content3 = [
        "Many trauma survivors report unexpected growth:",
        "  - Deeper faith and relationship with God",
        "  - Greater compassion for others who suffer",
        "  - Clearer sense of what truly matters",
        "  - Stronger relationships (authentic vulnerability)",
        "  - New purpose (helping others heal)",
        "",
        "Romans 8:28 doesn't mean trauma was 'good.'",
        "It means God can bring good FROM it.",
        "",
        "Growth I've noticed in myself:",
    ]
    y = 710
    for line in content3:
        pdf.add_text(72, y, line, 'F1', 10)
        y -= 16
    for _ in range(4):
        y -= 5
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 14

    # Resources
    pdf.new_page()
    pdf.add_centered_text(750, "RESOURCES", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    resources = [
        "988 Suicide & Crisis Lifeline: Call or text 988",
        "SAMHSA Helpline: 1-800-662-4357",
        "PTSD Foundation of America",
        "Celebrate Recovery (church-based)",
        "EMDR therapists (emdr.com)",
        "Faith-based trauma counselors",
        "Trauma-informed church resources",
        "Books: 'The Body Keeps the Score' by Bessel van der Kolk",
    ]
    y = 710
    for r in resources:
        pdf.add_text(72, y, f"- {r}", 'F1', 10)
        y -= 20

    y -= 20
    pdf.add_text(72, y, "You are not broken beyond repair.", 'F5', 12, 0.2)
    y -= 20
    pdf.add_text(72, y, "He heals the brokenhearted and binds up their wounds.", 'F5', 12, 0.2)
    y -= 16
    pdf.add_text(72, y, "- Psalm 147:3", 'F1', 10, 0.4)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book209_CBT_PTSD_Christian.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
