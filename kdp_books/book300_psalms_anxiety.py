"""Book 300: PRAYING THROUGH ANXIETY - A 30-Day Psalm Prayer Challenge"""
import random
from pdf_utils import PDFDoc

random.seed(300)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    days = [
        ("Day 1", "Psalm 46:1-3", "God is our refuge and strength, a very present help in trouble. Therefore will not we fear, though the earth be removed."),
        ("Day 2", "Psalm 55:22", "Cast thy burden upon the Lord, and he shall sustain thee: he shall never suffer the righteous to be moved."),
        ("Day 3", "Psalm 94:19", "In the multitude of my thoughts within me thy comforts delight my soul."),
        ("Day 4", "Psalm 56:3-4", "What time I am afraid, I will trust in thee. In God I will praise his word, in God I have put my trust."),
        ("Day 5", "Psalm 34:4", "I sought the Lord, and he heard me, and delivered me from all my fears."),
        ("Day 6", "Psalm 27:1", "The Lord is my light and my salvation; whom shall I fear? the Lord is the strength of my life."),
        ("Day 7", "Psalm 46:10", "Be still, and know that I am God."),
        ("Day 8", "Psalm 23:4", "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me."),
        ("Day 9", "Psalm 62:1-2", "Truly my soul waiteth upon God: from him cometh my salvation. He only is my rock."),
        ("Day 10", "Psalm 139:23-24", "Search me, O God, and know my heart: try me, and know my thoughts: see if there be any wicked way in me."),
        ("Day 11", "Psalm 37:7-8", "Rest in the Lord, and wait patiently for him: fret not thyself."),
        ("Day 12", "Psalm 91:1-2", "He that dwelleth in the secret place of the most High shall abide under the shadow of the Almighty."),
        ("Day 13", "Psalm 121:1-2", "I will lift up mine eyes unto the hills, from whence cometh my help. My help cometh from the Lord."),
        ("Day 14", "Psalm 4:8", "I will both lay me down in peace, and sleep: for thou, Lord, only makest me dwell in safety."),
        ("Day 15", "Psalm 103:1-5", "Bless the Lord, O my soul, and forget not all his benefits: Who forgiveth, who healeth, who redeemeth."),
        ("Day 16", "Psalm 30:5", "Weeping may endure for a night, but joy cometh in the morning."),
        ("Day 17", "Psalm 116:7", "Return unto thy rest, O my soul; for the Lord hath dealt bountifully with thee."),
        ("Day 18", "Psalm 18:2", "The Lord is my rock, and my fortress, and my deliverer; my God, my strength."),
        ("Day 19", "Psalm 42:11", "Why art thou cast down, O my soul? hope thou in God: for I shall yet praise him."),
        ("Day 20", "Psalm 61:2", "From the end of the earth will I cry unto thee, when my heart is overwhelmed."),
        ("Day 21", "Psalm 34:17-18", "The righteous cry, and the Lord heareth. The Lord is nigh unto them of a broken heart."),
        ("Day 22", "Psalm 143:8", "Cause me to hear thy lovingkindness in the morning; for in thee do I trust."),
        ("Day 23", "Psalm 73:26", "My flesh and my heart faileth: but God is the strength of my heart, and my portion for ever."),
        ("Day 24", "Psalm 107:28-29", "Then they cry unto the Lord in their trouble, and he bringeth them out. He maketh the storm a calm."),
        ("Day 25", "Psalm 40:1-2", "I waited patiently for the Lord; and he inclined unto me. He set my feet upon a rock."),
        ("Day 26", "Psalm 145:18-19", "The Lord is nigh unto all them that call upon him. He will fulfil the desire of them that fear him."),
        ("Day 27", "Psalm 86:15", "But thou, O Lord, art a God full of compassion, and gracious, longsuffering."),
        ("Day 28", "Psalm 147:3", "He healeth the broken in heart, and bindeth up their wounds."),
        ("Day 29", "Psalm 31:24", "Be of good courage, and he shall strengthen your heart, all ye that hope in the Lord."),
        ("Day 30", "Psalm 23:1-3", "The Lord is my shepherd; I shall not want. He maketh me to lie down in green pastures."),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(30, 30, 552, 732, 3, 0.2)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_centered_text(680, "PRAYING THROUGH", 'F2', 26, 0.1)
    doc.add_centered_text(645, "ANXIETY", 'F2', 26, 0.1)
    doc.add_centered_text(605, "A 30-Day Psalm Prayer Challenge", 'F4', 16, 0.25)
    doc.add_filled_rect(140, 360, 332, 160, 0.88)
    doc.add_rect(140, 360, 332, 160, 2, 0.3)
    doc.add_centered_text(470, "[ILLUSTRATION: storm clouds parting to", 'F3', 10, 0.4)
    doc.add_centered_text(455, "reveal peaceful blue sky with dove]", 'F3', 10, 0.4)
    doc.add_centered_text(250, "Turn Your Worry Into Worship", 'F4', 14, 0.3)
    doc.add_centered_text(225, "One Psalm at a Time", 'F4', 14, 0.3)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "PRAYING THROUGH ANXIETY", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    doc.add_text(72, 560, "Note: This journal is not a substitute for professional mental", 'F1', 9, 0.3)
    doc.add_text(72, 545, "health care. If you are in crisis, call 988 or text HOME to 741741.", 'F1', 9, 0.3)
    
    # Introduction
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "THE CHALLENGE", 'F2', 16, 0.1)
    y = 685
    intro = [
        "Anxiety is real. God knows that. The Psalms prove it.",
        "",
        "David - a warrior king - wrote about fear, panic, sleepless",
        "nights, racing thoughts, and overwhelming dread. He wasn't",
        "weak for feeling those things. And neither are you.",
        "",
        "But here's what David did with his anxiety: he PRAYED it.",
        "He turned his worry into worship. He took his spinning",
        "thoughts and aimed them at God instead of at himself.",
        "",
        "THIS 30-DAY CHALLENGE:",
        "  Each day gives you a Psalm passage about anxiety/fear.",
        "  You'll rewrite it as YOUR personal prayer.",
        "  You'll track your anxiety level (1-10).",
        "  You'll notice patterns and breakthroughs.",
        "",
        "THIS IS NOT:",
        "  - A replacement for therapy or medication",
        "  - A promise that anxiety will vanish instantly",
        "  - A guilt trip for struggling",
        "",
        "THIS IS:",
        "  - A spiritual tool alongside your other tools",
        "  - A way to retrain your brain toward peace",
        "  - A 30-day experiment in trusting God with your fears",
    ]
    for line in intro:
        if line.startswith("Anxiety") or line.startswith("But here"):
            doc.add_text(72, y, line, 'F5', 10, 0.1)
        elif line.startswith("THIS"):
            doc.add_text(72, y, line, 'F2', 10, 0.15)
        else:
            doc.add_text(72, y, line, 'F4', 10, 0.25)
        y -= 17
    
    # Anxiety tracker page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "30-DAY ANXIETY TRACKER", 'F2', 16, 0.1)
    doc.add_text(72, 700, "Rate your anxiety 1-10 each day (1=calm, 10=severe):", 'F1', 10, 0.3)
    y = 670
    for row in range(6):
        x = 72
        for col in range(5):
            day_num = row * 5 + col + 1
            if day_num <= 30:
                doc.add_rect(x, y, 90, 30, 1, 0.4)
                doc.add_text(x+3, y+17, f"Day {day_num}:", 'F1', 8, 0.3)
                doc.add_text(x+50, y+17, "___", 'F1', 8, 0.3)
            x += 96
        y -= 38
    doc.add_text(72, y-10, "Pattern I notice: ___________________________________________", 'F1', 10, 0.3)
    doc.add_text(72, y-35, "My biggest trigger: __________________________________________", 'F1', 10, 0.3)
    doc.add_text(72, y-60, "What helps most: ____________________________________________", 'F1', 10, 0.3)
    
    # 30 daily pages (2+ pages each)
    for i, (day, ref, verse) in enumerate(days):
        # Page 1: Psalm + personal prayer version
        doc.new_page()
        fill = 0.92 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        
        # Header
        doc.add_filled_rect(40, 745, 532, 30, 0.88)
        doc.add_rect(40, 745, 532, 30, 1, 0.3)
        doc.add_text(55, 755, f"{day}", 'F2', 13, 0.1)
        doc.add_text(200, 755, ref, 'F4', 11, 0.3)
        doc.add_text(420, 755, "Date: ___/___/___", 'F1', 9, 0.4)
        
        # Verse in box
        doc.add_filled_rect(55, 670, 502, 60, 0.95)
        doc.add_rect(55, 670, 502, 60, 1, 0.4)
        words = verse.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) > 60:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        vy = 710
        for ln in lines:
            doc.add_text(65, vy, ln, 'F4', 10, 0.2)
            vy -= 14
        
        y = 650
        # Anxiety truth in this Psalm
        doc.add_text(72, y, "THE ANXIETY TRUTH IN THIS PSALM:", 'F2', 11, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 10
        # My prayer version
        doc.add_text(72, y, "MY PRAYER VERSION (rewrite this Psalm as YOUR prayer):", 'F2', 11, 0.15)
        y -= 18
        for _ in range(8):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 10
        # Evening check-in
        doc.add_filled_rect(55, y-65, 502, 75, 0.88)
        doc.add_rect(55, y-65, 502, 75, 1, 0.3)
        doc.add_text(70, y, "EVENING CHECK-IN:", 'F2', 10, 0.15)
        doc.add_text(70, y-18, "Anxiety level this morning (1-10): ___  This evening: ___", 'F1', 9, 0.3)
        doc.add_text(70, y-36, "Did praying this Psalm shift anything?  [ ] Yes  [ ] Somewhat  [ ] Not yet", 'F1', 9, 0.3)
        doc.add_text(70, y-54, "One word for how I feel now: _______________", 'F1', 9, 0.3)
        
        # Page 2: Notes and deeper reflection
        doc.new_page()
        fill2 = 0.94 + random.uniform(0, 0.03)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"{day} - Deeper Reflection", 'F2', 12, 0.15)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        
        y = 720
        doc.add_text(72, y, "What triggered my anxiety today?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What physical sensations did I notice?", 'F2', 10, 0.15)
        y -= 18
        doc.add_text(72, y, "[ ] Racing heart  [ ] Tight chest  [ ] Stomach knots", 'F1', 9, 0.3)
        y -= 16
        doc.add_text(72, y, "[ ] Shallow breathing  [ ] Tension  [ ] Other: _______", 'F1', 9, 0.3)
        y -= 25
        doc.add_text(72, y, "The lie anxiety told me today:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(2):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "The TRUTH from today's Psalm:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(2):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What I'm choosing to believe:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "Tomorrow, I will:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(2):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
    
    # Bonus: Breathing prayer exercise
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.91)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "BREATHING PRAYER EXERCISE", 'F2', 16, 0.1)
    y = 695
    breathing = [
        "When anxiety hits, try this Scripture breathing pattern:",
        "",
        "BREATHE IN (4 counts): 'The Lord is my shepherd'",
        "HOLD (4 counts): 'I shall not want'",
        "BREATHE OUT (6 counts): 'He makes me lie down in peace'",
        "",
        "Repeat 5-10 times until your body calms.",
        "",
        "OTHER PSALM BREATHING PRAYERS:",
        "",
        "IN: 'Be still'  OUT: 'and know that I am God'",
        "IN: 'Cast your burden'  OUT: 'upon the Lord'",
        "IN: 'God is our refuge'  OUT: 'and strength'",
        "IN: 'I sought the Lord'  OUT: 'and He heard me'",
        "IN: 'When I am afraid'  OUT: 'I will trust in You'",
        "",
        "Practice daily - even when NOT anxious - to build the habit.",
    ]
    for line in breathing:
        if line.startswith("BREATHE") or line.startswith("HOLD") or line.startswith("IN:") or line.startswith("OTHER") or line.startswith("When") or line.startswith("Practice"):
            doc.add_text(72, y, line, 'F2', 10, 0.15)
        else:
            doc.add_text(72, y, line, 'F4', 10, 0.25)
        y -= 20
    
    # Resources
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "ANXIETY SUPPORT RESOURCES", 'F2', 16, 0.1)
    y = 695
    resources = [
        "If anxiety is severely impacting your daily life,",
        "please seek professional help. Faith and therapy work together.",
        "",
        "988 Suicide & Crisis Lifeline - Call or text 988",
        "Crisis Text Line - Text HOME to 741741",
        "NAMI (National Alliance on Mental Illness) - nami.org",
        "Anxiety & Depression Association - adaa.org",
        "",
        "REMEMBER:",
        "- Anxiety is not a sin or lack of faith",
        "- God created therapy, medication, and community to help",
        "- Using professional help is wise, not weak",
        "- You can pray AND get professional support",
    ]
    for line in resources:
        if line.startswith("REMEMBER"):
            doc.add_text(72, y, line, 'F2', 11, 0.15)
        else:
            doc.add_text(72, y, line, 'F1', 11, 0.25)
        y -= 20
    
    # Extra journal pages to reach 72+
    extras_300 = ["MY ANXIETY PATTERNS", "TRUTHS VS LIES", "PROGRESS NOTES", "PRAYERS THAT HELPED", "GRATITUDE LIST", "COPING STRATEGIES"]
    for et in extras_300:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, et, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book300_Psalms_Anxiety_30Day.pdf')
    print("Book300_Psalms_Anxiety_30Day.pdf created successfully!")

if __name__ == "__main__":
    create_book()
