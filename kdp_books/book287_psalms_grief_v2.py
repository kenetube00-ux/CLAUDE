"""Book 287: STILL HELD - Psalms for Every Stage of Grief"""
import random
from pdf_utils import PDFDoc

random.seed(287)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    stages = {
        "STAGE 1: SHOCK & DENIAL": [
            ("Psalm 77:1-2", "I cried unto God with my voice; my soul refused to be comforted."),
            ("Psalm 13:1", "How long wilt thou forget me, O Lord? for ever?"),
            ("Psalm 88:1-2", "O Lord God of my salvation, I have cried day and night before thee."),
            ("Psalm 102:1-2", "Hear my prayer, O Lord, and let my cry come unto thee."),
            ("Psalm 6:6", "I am weary with my groaning; all the night make I my bed to swim."),
            ("Psalm 77:7-9", "Will the Lord cast off for ever? and will he be favourable no more?"),
            ("Psalm 143:4", "Therefore is my spirit overwhelmed within me; my heart is desolate."),
        ],
        "STAGE 2: ANGER": [
            ("Psalm 10:1", "Why standest thou afar off, O Lord? why hidest thou thyself in times of trouble?"),
            ("Psalm 22:1-2", "My God, my God, why hast thou forsaken me? why art thou so far from helping me?"),
            ("Psalm 74:1", "O God, why hast thou cast us off for ever?"),
            ("Psalm 44:23-24", "Awake, why sleepest thou, O Lord? Wherefore hidest thou thy face?"),
            ("Psalm 39:10", "Remove thy stroke away from me: I am consumed by the blow of thine hand."),
            ("Psalm 88:14", "Lord, why castest thou off my soul? why hidest thou thy face from me?"),
            ("Psalm 109:21-22", "Do thou for me, for thy name's sake. For I am poor and needy, and my heart is wounded."),
        ],
        "STAGE 3: BARGAINING": [
            ("Psalm 51:10-12", "Create in me a clean heart, O God; and renew a right spirit within me."),
            ("Psalm 25:4-5", "Shew me thy ways, O Lord; teach me thy paths."),
            ("Psalm 90:12", "So teach us to number our days, that we may apply our hearts unto wisdom."),
            ("Psalm 119:71", "It is good for me that I have been afflicted; that I might learn thy statutes."),
            ("Psalm 27:7-8", "Hear, O Lord, when I cry with my voice: have mercy upon me."),
        ],
        "STAGE 4: DEPRESSION": [
            ("Psalm 6:2-3", "Have mercy upon me, O Lord; for I am weak. My soul is also sore vexed."),
            ("Psalm 38:6-8", "I am troubled; I am bowed down greatly; I go mourning all the day long."),
            ("Psalm 42:3", "My tears have been my meat day and night."),
            ("Psalm 69:1-2", "Save me, O God; for the waters are come in unto my soul. I sink in deep mire."),
            ("Psalm 88:6", "Thou hast laid me in the lowest pit, in darkness, in the deeps."),
            ("Psalm 143:7", "Hear me speedily, O Lord: my spirit faileth. Hide not thy face from me."),
        ],
        "STAGE 5: ACCEPTANCE & HOPE": [
            ("Psalm 30:11-12", "Thou hast turned for me my mourning into dancing."),
            ("Psalm 40:1-3", "I waited patiently for the Lord; and he inclined unto me. He put a new song in my mouth."),
            ("Psalm 116:1-2", "I love the Lord, because he hath heard my voice and my supplications."),
            ("Psalm 126:5-6", "They that sow in tears shall reap in joy."),
            ("Psalm 23:6", "Surely goodness and mercy shall follow me all the days of my life."),
        ],
    }
    
    borders = [
        "thorny branch becoming blooming roses",
        "storm clouds parting to reveal sun",
        "withered tree with one green branch",
        "broken vessel with light streaming through cracks",
        "winter landscape with first spring flower",
        "hands releasing a dove into sky",
        "seed in dark soil with roots growing",
        "bridge over troubled waters",
        "candle flame in darkness",
        "rainbow after storm over valley",
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(25, 25, 562, 742, 3, 0.2)
    doc.add_rect(35, 35, 542, 722, 1, 0.5)
    doc.add_filled_rect(80, 480, 452, 220, 0.88)
    doc.add_rect(80, 480, 452, 220, 2, 0.2)
    doc.add_centered_text(665, "STILL HELD", 'F2', 32, 0.1)
    doc.add_centered_text(625, "Psalms for Every Stage of Grief", 'F5', 18, 0.2)
    doc.add_centered_text(590, "(Coloring & Reflection Journal)", 'F4', 14, 0.35)
    doc.add_centered_text(520, "[ILLUSTRATION: hands holding a broken heart", 'F3', 10, 0.4)
    doc.add_centered_text(505, "with golden light filling the cracks]", 'F3', 10, 0.4)
    doc.add_centered_text(200, "Volume 2", 'F4', 14, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0.2)
    doc.add_centered_text(95, "KJV Scripture", 'F1', 10, 0.4)
    
    # Copyright page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "STILL HELD", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "No part of this publication may be reproduced without permission.", 'F1', 9, 0.3)
    doc.add_text(72, 605, "Scripture from the King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 575, "Published by KDP Amazon", 'F1', 10, 0.3)
    doc.add_text(72, 545, "Dedicated to those walking through the valley.", 'F4', 11, 0.2)
    doc.add_text(72, 525, "You are still held.", 'F5', 12, 0.2)
    
    # TOC page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "TABLE OF CONTENTS", 'F2', 16, 0.1)
    doc.add_line(180, 725, 432, 725, 1, 0.3)
    y = 690
    doc.add_text(72, y, "How to Use This Journal ..................... 4", 'F1', 11, 0.2)
    y -= 25
    pg = 5
    for stage_name in stages.keys():
        doc.add_text(72, y, f"{stage_name} ............ {pg}", 'F2', 10, 0.15)
        y -= 18
        for ref, _ in stages[stage_name]:
            doc.add_text(90, y, f"{ref} .............. {pg+1}", 'F1', 9, 0.35)
            y -= 14
            pg += 2
        pg += 1
        y -= 8
    
    # How to use page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "HOW TO USE THIS JOURNAL", 'F2', 16, 0.1)
    doc.add_line(170, 715, 442, 715, 1, 0.4)
    y = 680
    lines = [
        "Grief is not a straight line. It comes in waves, circles, and",
        "spirals. This journal is organized by the stages of grief,",
        "but you do NOT have to go in order.",
        "",
        "Open to the stage that matches where you are TODAY.",
        "",
        "EACH PSALM INCLUDES:",
        "  * A coloring page with the verse in a decorative frame",
        "  * A reflection page with guided prompts",
        "",
        "THE FIVE STAGES:",
        "  1. Shock & Denial - When it doesn't feel real",
        "  2. Anger - When you're mad at God, life, everyone",
        "  3. Bargaining - When you ask 'what if' and 'if only'",
        "  4. Depression - When the weight feels unbearable",
        "  5. Acceptance - When hope begins to return",
        "",
        "REMEMBER:",
        "  * There is no timeline for grief",
        "  * All emotions are valid before God",
        "  * You may revisit stages many times",
        "  * Coloring can calm your nervous system",
        "  * God can handle your honest prayers",
    ]
    for line in lines:
        if line.startswith("EACH") or line.startswith("THE FIVE") or line.startswith("REMEMBER"):
            doc.add_text(72, y, line, 'F2', 11, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 11, 0.25)
        y -= 18
    
    # Main content - stages with psalms
    psalm_idx = 0
    for stage_name, stage_psalms in stages.items():
        # Stage intro page
        doc.new_page()
        fill = 0.88 + random.uniform(0, 0.07)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(30, 30, 552, 732, 3, 0.2)
        doc.add_filled_rect(80, 380, 452, 200, 0.92)
        doc.add_rect(80, 380, 452, 200, 2, 0.3)
        doc.add_centered_text(540, stage_name, 'F2', 18, 0.1)
        desc_map = {
            "STAGE 1": "The world has stopped making sense. Everything feels surreal.",
            "STAGE 2": "The pain turns to fury. Why? How could God allow this?",
            "STAGE 3": "If only... What if... The mind searches for answers.",
            "STAGE 4": "The full weight of loss settles in. Darkness feels permanent.",
            "STAGE 5": "Slowly, breath by breath, hope whispers again.",
        }
        for key, desc in desc_map.items():
            if key in stage_name:
                doc.add_centered_text(490, desc, 'F4', 12, 0.3)
                break
        doc.add_centered_text(420, f"{len(stage_psalms)} Psalms for this season", 'F1', 11, 0.4)
        border = borders[psalm_idx % len(borders)]
        doc.add_centered_text(300, f"[ILLUSTRATION: {border}]", 'F3', 10, 0.4)
        
        for ref, verse in stage_psalms:
            # Coloring page
            doc.new_page()
            fill = 0.89 + random.uniform(0, 0.08)
            doc.add_filled_rect(0, 0, 612, 792, fill)
            doc.add_rect(25, 25, 562, 742, 3, 0.2)
            doc.add_rect(35, 35, 542, 722, 1, 0.5)
            
            border = borders[psalm_idx % len(borders)]
            doc.add_filled_rect(60, 620, 492, 120, 0.94)
            doc.add_rect(60, 620, 492, 120, 1, 0.4)
            doc.add_centered_text(700, f"[ILLUSTRATION: {border}]", 'F3', 9, 0.4)
            doc.add_centered_text(650, "Color this image as a prayer of lament", 'F3', 8, 0.5)
            
            # Verse frame
            doc.add_filled_rect(70, 300, 472, 280, 0.97)
            doc.add_rect(70, 300, 472, 280, 2, 0.25)
            doc.add_rect(80, 310, 452, 260, 1, 0.5)
            
            doc.add_centered_text(545, ref, 'F2', 14, 0.1)
            words = verse.split()
            lines = []
            cur = ""
            for w in words:
                if len(cur + " " + w) > 48:
                    lines.append(cur)
                    cur = w
                else:
                    cur = (cur + " " + w).strip()
            if cur:
                lines.append(cur)
            vy = 500
            for line in lines:
                doc.add_centered_text(vy, line, 'F5', 12, 0.15)
                vy -= 22
            
            # Bottom area
            doc.add_filled_rect(60, 50, 492, 220, 0.93)
            doc.add_rect(60, 50, 492, 220, 1, 0.4)
            brd2 = borders[(psalm_idx + 3) % len(borders)]
            doc.add_centered_text(220, f"[ILLUSTRATION: {brd2}]", 'F3', 9, 0.4)
            doc.add_centered_text(90, "Color this page as a prayer", 'F4', 11, 0.3)
            
            # Journal page
            doc.new_page()
            fill2 = 0.93 + random.uniform(0, 0.04)
            doc.add_filled_rect(0, 0, 612, 792, fill2)
            doc.add_rect(40, 40, 532, 712, 2, 0.3)
            doc.add_centered_text(740, f"Reflecting on {ref}", 'F2', 13, 0.1)
            doc.add_line(170, 735, 442, 735, 1, 0.4)
            
            y = 700
            prompts = [
                ("What grief stage am I in today?", 3),
                ("How does this Psalm match my feelings?", 4),
                ("What would I say to God right now?", 5),
                ("One thing I need Him to know:", 4),
                ("My honest prayer:", 5),
            ]
            for prompt, num_lines in prompts:
                doc.add_text(72, y, prompt, 'F2', 11, 0.15)
                y -= 18
                for _ in range(num_lines):
                    doc.add_line(72, y, 540, y, 0.5, 0.6)
                    y -= 18
                y -= 10
            
            psalm_idx += 1
    
    # Bonus: Grief timeline page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "MY GRIEF TIMELINE", 'F2', 16, 0.1)
    doc.add_text(72, 690, "Date of loss: ___________________", 'F1', 11, 0.2)
    doc.add_text(72, 660, "Person/thing I'm grieving: ___________________", 'F1', 11, 0.2)
    y = 620
    months = ["Month 1", "Month 3", "Month 6", "Month 9", "Month 12", "Month 18", "Year 2+"]
    for m in months:
        doc.add_text(72, y, f"{m}:", 'F2', 11, 0.2)
        doc.add_line(72, y-18, 540, y-18, 0.5, 0.6)
        doc.add_line(72, y-36, 540, y-36, 0.5, 0.6)
        y -= 70
    
    # Resources page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "GRIEF SUPPORT RESOURCES", 'F2', 16, 0.1)
    y = 680
    resources = [
        "GriefShare - griefshare.org",
        "988 Suicide & Crisis Lifeline - Call or text 988",
        "Crisis Text Line - Text HOME to 741741",
        "National Alliance on Mental Illness - nami.org",
        "Your local church pastoral care team",
        "",
        "Remember: Seeking help is an act of faith, not weakness.",
    ]
    for r in resources:
        if r:
            doc.add_text(72, y, r, 'F1', 11, 0.25)
        y -= 22
    
    # Certificate
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.90)
    doc.add_rect(50, 100, 512, 600, 3, 0.2)
    doc.add_rect(60, 110, 492, 580, 1, 0.4)
    doc.add_centered_text(630, "CERTIFICATE OF COURAGE", 'F2', 20, 0.1)
    doc.add_centered_text(590, "This certifies that", 'F4', 14, 0.3)
    doc.add_line(180, 560, 432, 560, 1, 0.3)
    doc.add_centered_text(540, "(your name)", 'F1', 9, 0.5)
    doc.add_centered_text(500, "has walked through the valley of grief", 'F4', 13, 0.3)
    doc.add_centered_text(475, "with courage, faith, and the Psalms.", 'F4', 13, 0.3)
    doc.add_centered_text(430, "You are STILL HELD.", 'F2', 16, 0.1)
    doc.add_centered_text(380, "\"The Lord is nigh unto them that are of a", 'F4', 12, 0.25)
    doc.add_centered_text(360, "broken heart.\" - Psalm 34:18", 'F4', 12, 0.25)
    doc.add_text(150, 220, "Date: _______________", 'F1', 11, 0.3)
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book287_Psalms_Grief_V2.pdf')
    print("Book287_Psalms_Grief_V2.pdf created successfully!")

if __name__ == "__main__":
    create_book()
