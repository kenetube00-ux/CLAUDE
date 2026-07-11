"""Book 197: PSALMS OF COMFORT - Bilingual Devotional (Tigrinya-English)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.93)
    pdf.add_centered_text(500, "PSALMS OF COMFORT", 'F2', 22)
    pdf.add_centered_text(470, "Bilingual Devotional", 'F4', 14, 0.2)
    pdf.add_centered_text(445, "(Tigrinya-English)", 'F1', 12, 0.3)
    pdf.add_centered_text(390, "30 Daily Devotions from the Psalms", 'F1', 11, 0.3)
    pdf.add_centered_text(180, f"By {author}", 'F2', 12, 0.2)

    # Copyright page
    pdf.new_page()
    pdf.add_text(50, 580, "PSALMS OF COMFORT - Bilingual Devotional", 'F2', 11)
    pdf.add_text(50, 560, f"By {author}", 'F1', 10)
    pdf.add_text(50, 535, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(50, 515, "Scripture from World English Bible (WEB) - Public Domain", 'F1', 9)
    pdf.add_text(50, 490, "Published by KIDLYTICAL Books", 'F1', 9)

    # 30 Daily Devotions
    psalms = [
        ("Psalm 23:1", "The LORD is my shepherd; I shall not want."),
        ("Psalm 46:1", "God is our refuge and strength, a very present help in trouble."),
        ("Psalm 91:1-2", "He who dwells in the secret place of the Most High will rest in the shadow of the Almighty."),
        ("Psalm 27:1", "The LORD is my light and my salvation. Whom shall I fear?"),
        ("Psalm 34:18", "The LORD is near to those who have a broken heart and saves those who have a crushed spirit."),
        ("Psalm 37:4", "Delight yourself also in the LORD, and he will give you the desires of your heart."),
        ("Psalm 40:1-2", "I waited patiently for the LORD. He turned to me and heard my cry."),
        ("Psalm 42:11", "Why are you in despair, my soul? Hope in God! For I shall still praise him."),
        ("Psalm 46:10", "Be still and know that I am God."),
        ("Psalm 55:22", "Cast your burden on the LORD and he will sustain you."),
        ("Psalm 56:3", "What time I am afraid, I will put my trust in you."),
        ("Psalm 61:2", "From the end of the earth I will call to you when my heart is overwhelmed."),
        ("Psalm 62:1", "My soul rests in God alone. My salvation is from him."),
        ("Psalm 63:1", "God, you are my God. I will earnestly seek you. My soul thirsts for you."),
        ("Psalm 73:26", "My flesh and my heart fail, but God is the strength of my heart and my portion forever."),
        ("Psalm 86:5", "For you, Lord, are good and ready to forgive, abundant in loving kindness to all who call on you."),
        ("Psalm 90:12", "So teach us to number our days, that we may gain a heart of wisdom."),
        ("Psalm 91:11", "For he will put his angels in charge of you, to guard you in all your ways."),
        ("Psalm 103:1", "Praise the LORD, my soul! All that is within me, praise his holy name!"),
        ("Psalm 107:1", "Give thanks to the LORD, for he is good, for his loving kindness endures forever."),
        ("Psalm 118:24", "This is the day that the LORD has made. We will rejoice and be glad in it."),
        ("Psalm 119:105", "Your word is a lamp to my feet and a light for my path."),
        ("Psalm 121:1-2", "I lift up my eyes to the hills. Where does my help come from? My help comes from the LORD."),
        ("Psalm 139:14", "I will give thanks to you, for I am fearfully and wonderfully made."),
        ("Psalm 143:8", "Cause me to hear your loving kindness in the morning, for I trust in you."),
        ("Psalm 145:18", "The LORD is near to all those who call on him in truth."),
        ("Psalm 147:3", "He heals the broken in heart and binds up their wounds."),
        ("Psalm 150:6", "Let everything that has breath praise the LORD! Praise the LORD!"),
        ("Psalm 16:11", "You will show me the path of life. In your presence is fullness of joy."),
        ("Psalm 30:5", "Weeping may stay for the night, but joy comes in the morning.")
    ]

    for day, (ref, verse) in enumerate(psalms, 1):
        pdf.new_page()
        pdf.add_filled_rect(40, 590, 352, 35, 0.88)
        pdf.add_centered_text(602, f"DAY {day}", 'F2', 16)
        pdf.add_centered_text(575, ref, 'F5', 12)
        pdf.add_line(50, 565, 382, 565, 0.5, 0.6)

        # English verse
        pdf.add_text(50, 545, "English:", 'F2', 10)
        words = verse.split()
        line = ""
        y = 528
        for w in words:
            if len(line + " " + w) > 55:
                pdf.add_text(50, y, line, 'F4', 10)
                y -= 14
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(50, y, line, 'F4', 10)
            y -= 14

        # Tigrinya
        y -= 10
        pdf.add_text(50, y, "Tigrinya:", 'F2', 10)
        y -= 16
        pdf.add_text(50, y, "[Tigrinya scripture text here]", 'F3', 9, 0.4)

        # What is David saying?
        y -= 35
        pdf.add_text(50, y, "What is David saying?", 'F2', 11)
        y -= 18
        pdf.add_line(50, y, 382, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(50, y, 382, y, 0.5, 0.7)

        # How does this comfort me?
        y -= 30
        pdf.add_text(50, y, "How does this comfort me?", 'F2', 11)
        y -= 18
        pdf.add_line(50, y, 382, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(50, y, 382, y, 0.5, 0.7)

        # My prayer today
        y -= 30
        pdf.add_text(50, y, "My prayer today:", 'F2', 11)
        y -= 18
        pdf.add_line(50, y, 382, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(50, y, 382, y, 0.5, 0.7)

    # Monthly Reflection
    pdf.new_page()
    pdf.add_centered_text(600, "MONTHLY REFLECTION", 'F2', 16)
    pdf.add_line(50, 588, 382, 588, 1, 0.5)
    questions = [
        "Which Psalm comforted me the most this month?",
        "How has my prayer life changed?",
        "What did I learn about God's character?",
        "How did God answer my prayers?",
        "What will I carry forward into next month?"
    ]
    y = 560
    for q in questions:
        pdf.add_text(50, y, q, 'F1', 10)
        for _ in range(3):
            y -= 18
            pdf.add_line(50, y, 382, y, 0.5, 0.7)
        y -= 25

    # Favorite Psalms List
    pdf.new_page()
    pdf.add_centered_text(600, "MY FAVORITE PSALMS", 'F2', 16)
    pdf.add_line(50, 588, 382, 588, 1, 0.5)
    pdf.add_text(50, 565, "Record the Psalms that spoke to your heart:", 'F1', 10)
    y = 540
    for i in range(15):
        pdf.add_text(50, y, f"{i+1}.", 'F1', 10)
        pdf.add_line(70, y - 2, 382, y - 2, 0.5, 0.7)
        y -= 28

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book197_Tigrinya_Psalms_Study.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
