"""Book 301: PEACE FOR HER - A Women's Psalm Prayer Journal for Anxious Seasons"""
import random
from pdf_utils import PDFDoc

random.seed(301)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    days = [
        ("Day 1", "Motherhood Anxiety", "Psalm 127:3", "Lo, children are an heritage of the Lord: and the fruit of the womb is his reward."),
        ("Day 2", "Fear of Failure", "Psalm 37:23-24", "The steps of a good man are ordered by the Lord. Though he fall, he shall not be utterly cast down."),
        ("Day 3", "Health Worries", "Psalm 103:2-3", "Bless the Lord who forgiveth all thine iniquities; who healeth all thy diseases."),
        ("Day 4", "Relationship Anxiety", "Psalm 37:4-5", "Delight thyself in the Lord; and he shall give thee the desires of thine heart."),
        ("Day 5", "Financial Fear", "Psalm 34:9-10", "There is no want to them that fear him. They that seek the Lord shall not want any good thing."),
        ("Day 6", "Body Image", "Psalm 139:14", "I will praise thee; for I am fearfully and wonderfully made."),
        ("Day 7", "Work Stress", "Psalm 90:17", "Let the beauty of the Lord our God be upon us: and establish the work of our hands."),
        ("Day 8", "Comparison Trap", "Psalm 139:16", "Thine eyes did see my substance; in thy book all my members were written."),
        ("Day 9", "Sleepless Nights", "Psalm 4:8", "I will both lay me down in peace, and sleep: for thou, Lord, only makest me dwell in safety."),
        ("Day 10", "Overwhelm", "Psalm 61:2", "When my heart is overwhelmed: lead me to the rock that is higher than I."),
        ("Day 11", "People-Pleasing", "Psalm 118:6", "The Lord is on my side; I will not fear: what can man do unto me?"),
        ("Day 12", "Loneliness", "Psalm 68:6", "God setteth the solitary in families."),
        ("Day 13", "Grief & Loss", "Psalm 34:18", "The Lord is nigh unto them that are of a broken heart."),
        ("Day 14", "Control Issues", "Psalm 46:10", "Be still, and know that I am God."),
        ("Day 15", "Past Trauma", "Psalm 147:3", "He healeth the broken in heart, and bindeth up their wounds."),
        ("Day 16", "Marriage Worry", "Psalm 133:1", "Behold, how good and how pleasant it is for brethren to dwell together in unity!"),
        ("Day 17", "Parenting Guilt", "Psalm 103:13-14", "Like as a father pitieth his children, so the Lord pitieth them that fear him."),
        ("Day 18", "Aging Fears", "Psalm 92:14", "They shall still bring forth fruit in old age; they shall be fat and flourishing."),
        ("Day 19", "Decision Anxiety", "Psalm 32:8", "I will instruct thee and teach thee in the way which thou shalt go."),
        ("Day 20", "Caregiver Burden", "Psalm 55:22", "Cast thy burden upon the Lord, and he shall sustain thee."),
        ("Day 21", "Social Anxiety", "Psalm 27:1", "The Lord is my light and my salvation; whom shall I fear?"),
        ("Day 22", "Perfectionism", "Psalm 18:30", "As for God, his way is perfect."),
        ("Day 23", "Children's Safety", "Psalm 91:11", "He shall give his angels charge over thee, to keep thee in all thy ways."),
        ("Day 24", "Identity Crisis", "Psalm 139:1-3", "O Lord, thou hast searched me, and known me. Thou knowest my downsitting and uprising."),
        ("Day 25", "Burnout", "Psalm 23:2-3", "He maketh me to lie down in green pastures: he restoreth my soul."),
        ("Day 26", "World Events", "Psalm 46:1-2", "God is our refuge and strength. Therefore will not we fear."),
        ("Day 27", "Unworthiness", "Psalm 8:4-5", "What is man that thou art mindful of him? Thou hast crowned him with glory."),
        ("Day 28", "Future Dread", "Psalm 31:15", "My times are in thy hand."),
        ("Day 29", "Letting Go", "Psalm 37:7", "Rest in the Lord, and wait patiently for him."),
        ("Day 30", "Finding Peace", "Psalm 23:1-3", "The Lord is my shepherd; I shall not want. He leadeth me beside the still waters."),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(30, 30, 552, 732, 2, 0.3)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_centered_text(680, "PEACE FOR HER", 'F2', 28, 0.1)
    doc.add_centered_text(645, "A Women's Psalm Prayer Journal", 'F4', 16, 0.25)
    doc.add_centered_text(620, "for Anxious Seasons", 'F4', 16, 0.25)
    doc.add_filled_rect(140, 380, 332, 150, 0.88)
    doc.add_rect(140, 380, 332, 150, 2, 0.3)
    doc.add_centered_text(480, "[ILLUSTRATION: woman in peaceful garden", 'F3', 10, 0.4)
    doc.add_centered_text(465, "with flowing water and lavender fields]", 'F3', 10, 0.4)
    doc.add_centered_text(250, "30 Days of Praying Your Anxiety", 'F4', 13, 0.3)
    doc.add_centered_text(225, "Back to God", 'F4', 13, 0.3)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "PEACE FOR HER", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    doc.add_text(72, 560, "Disclaimer: This journal is not a substitute for professional", 'F1', 9, 0.3)
    doc.add_text(72, 545, "mental health treatment. Please seek help if needed.", 'F1', 9, 0.3)
    
    # Intro page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "DEAR SISTER", 'F2', 18, 0.1)
    y = 685
    intro = [
        "You carry so much.",
        "",
        "The mental load of motherhood. The pressure to hold it together.",
        "The worry about your children, your marriage, your health.",
        "The comparison game. The guilt. The endless to-do list.",
        "",
        "This journal was written specifically for YOU - a woman who",
        "loves God but still struggles with anxiety.",
        "",
        "Each day addresses a specific anxiety that women face:",
        "  motherhood, body image, relationships, caregiving,",
        "  perfectionism, people-pleasing, and more.",
        "",
        "For each day:",
        "  1. Read the Psalm that addresses YOUR specific anxiety",
        "  2. Identify the LIE anxiety is telling you",
        "  3. Rewrite the Psalm as YOUR personal prayer",
        "  4. Track your anxiety level",
        "  5. Practice the evening surrender",
        "",
        "You are not alone. You are not broken.",
        "You are a woman learning to give her anxiety to God.",
    ]
    for line in intro:
        if line.startswith("You carry") or line.startswith("You are not"):
            doc.add_text(72, y, line, 'F5', 11, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 10, 0.25)
        y -= 17
    
    # Anxiety types overview
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "WHAT ANXIETY LOOKS LIKE FOR WOMEN", 'F2', 14, 0.1)
    y = 700
    symptoms = [
        "CHECK THE ONES YOU EXPERIENCE:",
        "",
        "[ ] Racing thoughts that won't stop (especially at night)",
        "[ ] Constantly worrying about your children's safety",
        "[ ] Feeling like you're never doing enough",
        "[ ] Comparing yourself to other women/moms",
        "[ ] Physical symptoms: chest tight, stomach churning",
        "[ ] Difficulty sleeping or eating",
        "[ ] Snapping at loved ones then feeling guilty",
        "[ ] Avoiding social situations",
        "[ ] Needing to control everything",
        "[ ] Scrolling social media and feeling worse",
        "[ ] Difficulty making decisions",
        "[ ] Guilt about not being thankful enough",
        "[ ] Fear of something terrible happening",
        "[ ] Feeling like a fraud/imposter",
        "[ ] Exhaustion from carrying everyone's emotions",
        "",
        "If you checked several: you are in the right place.",
        "Let's bring these to God together.",
    ]
    for line in symptoms:
        if line.startswith("CHECK") or line.startswith("If you"):
            doc.add_text(72, y, line, 'F2', 10, 0.15)
        else:
            doc.add_text(72, y, line, 'F1', 10, 0.25)
        y -= 17
    
    # 30 daily entries
    for i, (day, topic, ref, verse) in enumerate(days):
        # Page 1
        doc.new_page()
        fill = 0.92 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        
        doc.add_filled_rect(40, 745, 532, 30, 0.88)
        doc.add_rect(40, 745, 532, 30, 1, 0.3)
        doc.add_text(55, 755, f"{day}: {topic}", 'F2', 12, 0.1)
        doc.add_text(430, 755, "Date: ___/___", 'F1', 9, 0.4)
        
        # Verse box
        doc.add_filled_rect(55, 680, 502, 50, 0.95)
        doc.add_rect(55, 680, 502, 50, 1, 0.4)
        doc.add_text(65, 710, ref, 'F2', 10, 0.15)
        words = verse.split()
        v_lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) > 62:
                v_lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            v_lines.append(cur)
        vy = 698
        for ln in v_lines:
            doc.add_text(65, vy, ln, 'F4', 9, 0.2)
            vy -= 12
        
        y = 660
        doc.add_text(72, y, f"THE LIE ANXIETY TELLS ME ABOUT {topic.upper()}:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 8
        doc.add_text(72, y, "THE TRUTH FROM THIS PSALM:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 8
        doc.add_text(72, y, "MY PRAYER (rewrite this Psalm in your own words):", 'F2', 10, 0.15)
        y -= 18
        for _ in range(7):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 8
        # Evening surrender box
        doc.add_filled_rect(55, y-55, 502, 65, 0.88)
        doc.add_rect(55, y-55, 502, 65, 1, 0.3)
        doc.add_text(70, y, "EVENING SURRENDER:", 'F2', 10, 0.15)
        doc.add_text(70, y-16, "Anxiety level: Morning ___ Evening ___", 'F1', 9, 0.3)
        doc.add_text(70, y-32, "What I'm releasing to God tonight: ______________________", 'F1', 9, 0.3)
        doc.add_text(70, y-48, "One thing I'm grateful for: _____________________________", 'F1', 9, 0.3)
        
        # Page 2: Deeper for women
        doc.new_page()
        fill2 = 0.94 + random.uniform(0, 0.03)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"{day}: {topic} - Going Deeper", 'F2', 12, 0.15)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        
        y = 720
        doc.add_text(72, y, "What specifically triggered this anxiety today?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 8
        doc.add_text(72, y, "Is there an action I need to take, or do I need to let go?", 'F2', 10, 0.15)
        y -= 18
        doc.add_text(72, y, "[ ] Take action: _________________  [ ] Let go and trust God", 'F1', 9, 0.3)
        y -= 25
        doc.add_text(72, y, "What would I tell a friend feeling this way?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 8
        doc.add_text(72, y, "A truth I'm choosing to believe over this fear:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 8
        doc.add_text(72, y, "Self-care I practiced/will practice today:", 'F2', 10, 0.15)
        y -= 18
        doc.add_text(72, y, "[ ] Movement  [ ] Nature  [ ] Rest  [ ] Connection  [ ] Creative", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(72, y, "[ ] Prayer  [ ] Music  [ ] Journaling  [ ] Other: _______", 'F1', 9, 0.3)
    
    # Bonus: Verses for specific anxieties
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "QUICK REFERENCE: VERSES FOR HER ANXIETIES", 'F2', 13, 0.1)
    y = 700
    quick_ref = [
        ("Kids' safety:", "Psalm 91:11-12"),
        ("Marriage:", "Ecclesiastes 4:12"),
        ("Health:", "Psalm 103:3"),
        ("Finances:", "Philippians 4:19"),
        ("Loneliness:", "Psalm 68:6"),
        ("Comparison:", "Psalm 139:14"),
        ("Body image:", "1 Samuel 16:7"),
        ("Work stress:", "Colossians 3:23"),
        ("Sleeplessness:", "Psalm 4:8"),
        ("Overwhelm:", "Psalm 61:2"),
        ("Control:", "Proverbs 3:5-6"),
        ("Guilt:", "Romans 8:1"),
        ("Future:", "Jeremiah 29:11"),
        ("Past:", "Isaiah 43:18-19"),
    ]
    for topic, verse in quick_ref:
        doc.add_text(72, y, f"{topic}", 'F2', 10, 0.15)
        doc.add_text(200, y, verse, 'F4', 10, 0.3)
        y -= 20
    
    # Final page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.91)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(650, "YOU MADE IT, SISTER.", 'F2', 20, 0.1)
    doc.add_centered_text(610, "30 days of giving your anxiety to God.", 'F4', 13, 0.25)
    y = 570
    closing = [
        "You showed up. Even on the hard days. Even when prayer",
        "felt pointless. Even when anxiety screamed louder than faith.",
        "",
        "You chose to bring it to God anyway. That IS faith.",
        "",
        "Keep going. Keep praying. Keep being honest.",
        "Peace isn't the absence of problems -",
        "it's the presence of God in the middle of them.",
        "",
        "\"Thou wilt keep him in perfect peace, whose mind",
        "is stayed on thee.\" - Isaiah 26:3",
    ]
    for line in closing:
        if line.startswith("You chose") or line.startswith("Keep"):
            doc.add_text(72, y, line, 'F5', 11, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 11, 0.25)
        y -= 20
    
    # Extra pages to reach 72+
    extras_301 = ["MY ANXIETY TRIGGERS & TRUTHS", "SELF-CARE PLAN", "VERSES FOR EVERY WORRY",
                  "LETTERS TO MY ANXIOUS SELF", "PROGRESS JOURNAL", "PEACE MILESTONES"]
    for et in extras_301:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, et, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book301_Psalms_Anxiety_Women.pdf')
    print("Book301_Psalms_Anxiety_Women.pdf created successfully!")

if __name__ == "__main__":
    create_book()
