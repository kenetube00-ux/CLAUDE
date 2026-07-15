"""Book 286: PSALMS OF COMFORT - A Coloring Journal for Seasons of Grief"""
import random
from pdf_utils import PDFDoc

random.seed(286)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    psalms = [
        ("Psalm 23:4", "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me."),
        ("Psalm 34:18", "The Lord is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit."),
        ("Psalm 46:1", "God is our refuge and strength, a very present help in trouble."),
        ("Psalm 55:22", "Cast thy burden upon the Lord, and he shall sustain thee."),
        ("Psalm 56:8", "Thou tellest my wanderings: put thou my tears into thy bottle."),
        ("Psalm 61:2", "From the end of the earth will I cry unto thee, when my heart is overwhelmed: lead me to the rock that is higher than I."),
        ("Psalm 62:1-2", "Truly my soul waiteth upon God: from him cometh my salvation. He only is my rock and my salvation."),
        ("Psalm 73:26", "My flesh and my heart faileth: but God is the strength of my heart, and my portion for ever."),
        ("Psalm 91:1-2", "He that dwelleth in the secret place of the most High shall abide under the shadow of the Almighty."),
        ("Psalm 103:13", "Like as a father pitieth his children, so the Lord pitieth them that fear him."),
        ("Psalm 116:15", "Precious in the sight of the Lord is the death of his saints."),
        ("Psalm 119:50", "This is my comfort in my affliction: for thy word hath quickened me."),
        ("Psalm 121:1-2", "I will lift up mine eyes unto the hills, from whence cometh my help. My help cometh from the Lord."),
        ("Psalm 126:5", "They that sow in tears shall reap in joy."),
        ("Psalm 138:7", "Though I walk in the midst of trouble, thou wilt revive me."),
        ("Psalm 139:16", "Thine eyes did see my substance, yet being unperfect; in thy book all my members were written."),
        ("Psalm 147:3", "He healeth the broken in heart, and bindeth up their wounds."),
        ("Psalm 30:5", "Weeping may endure for a night, but joy cometh in the morning."),
        ("Psalm 31:24", "Be of good courage, and he shall strengthen your heart, all ye that hope in the Lord."),
        ("Psalm 34:4", "I sought the Lord, and he heard me, and delivered me from all my fears."),
        ("Psalm 37:4", "Delight thyself also in the Lord; and he shall give thee the desires of thine heart."),
        ("Psalm 40:1-2", "I waited patiently for the Lord; and he inclined unto me, and heard my cry."),
        ("Psalm 42:11", "Why art thou cast down, O my soul? Hope thou in God: for I shall yet praise him."),
        ("Psalm 46:10", "Be still, and know that I am God."),
        ("Psalm 56:3", "What time I am afraid, I will trust in thee."),
        ("Psalm 71:20-21", "Thou, which hast shewed me great and sore troubles, shalt quicken me again."),
        ("Psalm 86:15", "But thou, O Lord, art a God full of compassion, and gracious, longsuffering."),
        ("Psalm 94:19", "In the multitude of my thoughts within me thy comforts delight my soul."),
        ("Psalm 116:7", "Return unto thy rest, O my soul; for the Lord hath dealt bountifully with thee."),
        ("Psalm 145:18", "The Lord is nigh unto all them that call upon him, to all that call upon him in truth."),
    ]
    
    borders_desc = [
        "floral vine border with roses and leaves",
        "nature scene frame with birds and branches",
        "geometric mandala corner decorations",
        "flowing water and lily pad border",
        "climbing ivy and butterfly frame",
        "mountain landscape border",
        "sunflower and garden border",
        "ocean waves and shells frame",
        "forest trees and deer border",
        "heart-shaped vine frame with doves",
    ]
    
    # Page 1: Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(30, 30, 552, 732, 3, 0.3)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_filled_rect(56, 500, 500, 200, 0.90)
    doc.add_rect(56, 500, 500, 200, 2, 0.3)
    doc.add_centered_text(660, "PSALMS OF COMFORT", 'F2', 28, 0.1)
    doc.add_centered_text(620, "A Coloring Journal for", 'F4', 18, 0.3)
    doc.add_centered_text(590, "Seasons of Grief", 'F5', 22, 0.1)
    doc.add_centered_text(530, "[ILLUSTRATION: peaceful garden scene with", 'F3', 10, 0.4)
    doc.add_centered_text(515, "a winding path through flowers toward light]", 'F3', 10, 0.4)
    doc.add_centered_text(200, "A Coloring & Journaling Experience", 'F4', 14, 0.3)
    doc.add_centered_text(160, "for Healing Through Scripture", 'F4', 14, 0.3)
    doc.add_centered_text(100, author, 'F2', 16, 0.2)
    
    # Page 2: Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.6)
    doc.add_centered_text(700, "PSALMS OF COMFORT", 'F2', 16, 0.2)
    doc.add_centered_text(675, "A Coloring Journal for Seasons of Grief", 'F4', 12, 0.3)
    doc.add_text(72, 620, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 600, "No portion of this book may be reproduced without written permission.", 'F1', 9, 0.3)
    doc.add_text(72, 575, "Scripture quotations are from the King James Version (KJV)", 'F1', 9, 0.3)
    doc.add_text(72, 555, "of the Holy Bible, which is in the public domain.", 'F1', 9, 0.3)
    doc.add_text(72, 520, "Published by KDP Amazon", 'F1', 10, 0.3)
    doc.add_text(72, 500, "ISBN: Pending", 'F1', 10, 0.3)
    doc.add_text(72, 470, "Printed in the United States of America", 'F1', 10, 0.3)
    doc.add_text(72, 430, "Dedicated to all who walk through seasons of grief.", 'F1', 11, 0.2)
    doc.add_text(72, 410, "May the Psalms bring comfort to your soul.", 'F4', 11, 0.3)
    
    # Page 3: Table of Contents
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.96)
    doc.add_rect(40, 40, 532, 712, 2, 0.4)
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0.1)
    doc.add_line(180, 715, 432, 715, 1, 0.3)
    y = 685
    doc.add_text(72, y, "How to Use This Journal ............... 4", 'F1', 11, 0.2)
    y -= 20
    for i, (ref, _) in enumerate(psalms[:15]):
        doc.add_text(72, y, f"{ref} ............... {5 + i*2}", 'F1', 10, 0.3)
        y -= 16
    
    # Page 4: How to Use
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.4)
    doc.add_centered_text(720, "HOW TO USE THIS JOURNAL", 'F2', 18, 0.1)
    doc.add_line(150, 715, 462, 715, 1, 0.3)
    y = 680
    instructions = [
        "This journal is designed to help you process grief through the beauty",
        "of Scripture and the meditative practice of coloring.",
        "",
        "FOR EACH PSALM, YOU WILL FIND:",
        "",
        "1. A COLORING PAGE - featuring the verse in a decorative frame",
        "   surrounded by nature-inspired artwork. Color slowly and",
        "   prayerfully. There is no right or wrong way to color.",
        "",
        "2. A JOURNAL PAGE - with guided prompts to help you process",
        "   your feelings, memories, and prayers.",
        "",
        "SUGGESTIONS FOR USE:",
        "",
        "- Find a quiet, comfortable space",
        "- Use colored pencils, crayons, or fine-tip markers",
        "- Read the verse aloud before coloring",
        "- Take your time - this is not a race",
        "- Write honestly in the journal sections",
        "- Return to favorite passages as often as needed",
        "- Share with a grief support group if helpful",
        "",
        "Remember: Grief is not linear. Some days will be harder than",
        "others. This journal meets you wherever you are today.",
    ]
    for line in instructions:
        if line.startswith("FOR EACH") or line.startswith("SUGGESTIONS"):
            doc.add_text(72, y, line, 'F2', 11, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 11, 0.25)
        y -= 18
    
    # 30 Psalms - each with coloring page + journal page
    for i, (ref, verse) in enumerate(psalms):
        border_desc = borders_desc[i % len(borders_desc)]
        
        # Coloring page
        doc.new_page()
        fill = 0.88 + random.uniform(0, 0.09)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        # Outer decorative border
        doc.add_rect(25, 25, 562, 742, 3, 0.2)
        doc.add_rect(35, 35, 542, 722, 1, 0.4)
        # Inner decorative frame
        doc.add_filled_rect(60, 300, 492, 350, 0.97)
        doc.add_rect(60, 300, 492, 350, 2, 0.3)
        doc.add_rect(70, 310, 472, 330, 1, 0.5)
        
        # Illustration box at top
        doc.add_filled_rect(60, 660, 492, 90, 0.93)
        doc.add_rect(60, 660, 492, 90, 1, 0.4)
        doc.add_centered_text(710, f"[ILLUSTRATION: {border_desc}]", 'F3', 9, 0.4)
        doc.add_centered_text(690, "Color this scene as a meditation on God's comfort", 'F3', 8, 0.5)
        
        # Verse in center
        words = verse.split()
        lines = []
        current = ""
        for w in words:
            if len(current + " " + w) > 50:
                lines.append(current)
                current = w
            else:
                current = (current + " " + w).strip()
        if current:
            lines.append(current)
        
        vy = 500 + (len(lines) * 10)
        doc.add_centered_text(vy + 30, ref, 'F2', 14, 0.1)
        for line in lines:
            doc.add_centered_text(vy, line, 'F5', 13, 0.15)
            vy -= 22
        
        # Bottom illustration area
        doc.add_filled_rect(60, 50, 492, 220, 0.95)
        doc.add_rect(60, 50, 492, 220, 1, 0.4)
        doc.add_centered_text(230, f"[ILLUSTRATION: {borders_desc[(i+5) % len(borders_desc)]}]", 'F3', 9, 0.4)
        doc.add_centered_text(100, "Color this page as a prayer", 'F4', 12, 0.3)
        
        # Corner decorations
        for cx, cy in [(40, 740), (555, 740), (40, 40), (555, 40)]:
            doc.add_rect(cx, cy, 15, 15, 1, 0.3)
            doc.add_rect(cx+3, cy+3, 9, 9, 0.5, 0.5)
        
        # Journal page
        doc.new_page()
        fill2 = 0.92 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.4)
        doc.add_centered_text(740, f"Reflecting on {ref}", 'F2', 14, 0.1)
        doc.add_line(150, 735, 462, 735, 1, 0.4)
        
        y = 700
        # Today I feel
        doc.add_text(72, y, "Today I feel:", 'F2', 12, 0.15)
        y -= 20
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        y -= 10
        doc.add_text(72, y, "This verse comforts me because:", 'F2', 12, 0.15)
        y -= 20
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        y -= 10
        doc.add_text(72, y, "A memory I want to hold:", 'F2', 12, 0.15)
        y -= 20
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        y -= 10
        doc.add_text(72, y, "My prayer:", 'F2', 12, 0.15)
        y -= 20
        for _ in range(6):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 20
        
        # Small decorative element at bottom
        doc.add_filled_rect(250, 55, 112, 25, 0.88)
        doc.add_centered_text(63, "~ Be Still ~", 'F4', 10, 0.4)
    
    # Faith journal pages (5 pages)
    journal_titles = [
        "MY FAITH JOURNEY THROUGH GRIEF",
        "LETTERS TO MY LOVED ONE",
        "PROMISES I'M HOLDING ONTO",
        "MOMENTS OF UNEXPECTED PEACE",
        "MY PRAYER FOR THE FUTURE"
    ]
    for title in journal_titles:
        doc.new_page()
        fill = 0.90 + random.uniform(0, 0.07)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, title, 'F2', 14, 0.1)
        doc.add_line(100, 725, 512, 725, 1, 0.4)
        y = 690
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22
    
    # Memory page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(40, 40, 532, 712, 3, 0.3)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(720, "IN LOVING MEMORY", 'F2', 20, 0.1)
    doc.add_line(180, 715, 432, 715, 2, 0.3)
    doc.add_text(72, 670, "Name: _______________________________________________", 'F1', 12, 0.2)
    doc.add_text(72, 640, "Born: ___________________  Passed: ___________________", 'F1', 12, 0.2)
    doc.add_text(72, 600, "What I miss most:", 'F2', 12, 0.15)
    y = 575
    for _ in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.6)
        y -= 20
    doc.add_text(72, y-10, "Their favorite verse:", 'F2', 12, 0.15)
    y -= 35
    for _ in range(3):
        doc.add_line(72, y, 540, y, 0.5, 0.6)
        y -= 20
    doc.add_text(72, y-10, "How they showed God's love:", 'F2', 12, 0.15)
    y -= 35
    for _ in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.6)
        y -= 20
    doc.add_filled_rect(150, 80, 312, 150, 0.95)
    doc.add_rect(150, 80, 312, 150, 1, 0.4)
    doc.add_centered_text(160, "[Place a photo or draw a memory here]", 'F3', 10, 0.4)
    
    # Resources page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "GRIEF SUPPORT RESOURCES", 'F2', 16, 0.1)
    doc.add_line(170, 715, 442, 715, 1, 0.3)
    y = 680
    resources = [
        ("GriefShare", "griefshare.org - Find a local support group"),
        ("National Suicide Prevention Lifeline", "988 - Available 24/7"),
        ("Crisis Text Line", "Text HOME to 741741"),
        ("The Dougy Center", "dougy.org - Grief support for children"),
        ("What's Your Grief", "whatsyourgrief.com - Online resources"),
        ("", ""),
        ("HELPFUL BOOKS:", ""),
        ("", "A Grief Observed - C.S. Lewis"),
        ("", "Tear Soup - Pat Schwiebert"),
        ("", "The Year of Magical Thinking - Joan Didion"),
        ("", "When God Doesn't Fix It - Laura Story"),
    ]
    for title, desc in resources:
        if title:
            doc.add_text(72, y, title, 'F2', 11, 0.15)
            if desc:
                doc.add_text(72, y-16, desc, 'F1', 10, 0.3)
                y -= 40
            else:
                y -= 22
        elif desc:
            doc.add_text(90, y, desc, 'F4', 10, 0.3)
            y -= 20
        else:
            y -= 15
    
    # Certificate page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(50, 100, 512, 600, 3, 0.2)
    doc.add_rect(60, 110, 492, 580, 1, 0.4)
    doc.add_rect(70, 120, 472, 560, 0.5, 0.6)
    doc.add_centered_text(620, "CERTIFICATE OF COMPLETION", 'F2', 20, 0.1)
    doc.add_centered_text(570, "This certifies that", 'F4', 14, 0.3)
    doc.add_line(180, 530, 432, 530, 1, 0.3)
    doc.add_centered_text(510, "(your name)", 'F1', 9, 0.5)
    doc.add_centered_text(470, "has completed the", 'F4', 14, 0.3)
    doc.add_centered_text(440, "Psalms of Comfort Coloring Journal", 'F5', 16, 0.1)
    doc.add_centered_text(400, "through 30 meditations on God's Word", 'F4', 12, 0.3)
    doc.add_centered_text(360, "in a season of grief.", 'F4', 12, 0.3)
    doc.add_centered_text(300, "\"He healeth the broken in heart,", 'F4', 13, 0.2)
    doc.add_centered_text(280, "and bindeth up their wounds.\" - Psalm 147:3", 'F4', 13, 0.2)
    doc.add_text(150, 200, "Date: _______________", 'F1', 11, 0.3)
    doc.add_text(350, 200, "Signed: _______________", 'F1', 11, 0.3)
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book286_Psalms_Grief_Coloring.pdf')
    print("Book286_Psalms_Grief_Coloring.pdf created successfully!")

if __name__ == "__main__":
    create_book()
