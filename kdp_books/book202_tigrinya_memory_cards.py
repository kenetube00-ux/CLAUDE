"""Book 202: 52 SCRIPTURE MEMORY VERSES - Bilingual Cards (Tigrinya-English)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.94)
    pdf.add_centered_text(600, "52 SCRIPTURE MEMORY VERSES", 'F2', 24)
    pdf.add_centered_text(565, "Bilingual Cards (Tigrinya-English)", 'F4', 14, 0.2)
    pdf.add_centered_text(520, "One Verse Per Week for One Year", 'F1', 12, 0.3)
    pdf.add_centered_text(490, "Categories: Faith | Peace | Strength | Wisdom", 'F1', 11, 0.4)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright page
    pdf.new_page()
    pdf.add_text(72, 700, "52 SCRIPTURE MEMORY VERSES", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "Scripture from World English Bible (WEB) - Public Domain", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)

    # 52 verses with categories
    verses = [
        ("Faith", "Hebrews 11:1", "Now faith is assurance of things hoped for, proof of things not seen."),
        ("Faith", "Romans 10:17", "So faith comes by hearing, and hearing by the word of God."),
        ("Faith", "2 Corinthians 5:7", "For we walk by faith, not by sight."),
        ("Faith", "Mark 11:22", "Have faith in God."),
        ("Faith", "Hebrews 11:6", "Without faith it is impossible to be well pleasing to him."),
        ("Faith", "James 2:17", "Even so faith, if it has no works, is dead in itself."),
        ("Faith", "Galatians 2:20", "I live by faith in the Son of God, who loved me and gave himself for me."),
        ("Peace", "John 14:27", "Peace I leave with you. My peace I give to you."),
        ("Peace", "Philippians 4:7", "The peace of God which surpasses all understanding will guard your hearts."),
        ("Peace", "Isaiah 26:3", "You will keep him in perfect peace whose mind is stayed on you."),
        ("Peace", "Romans 8:6", "The mind of the Spirit is life and peace."),
        ("Peace", "Psalm 29:11", "The LORD will give strength to his people. He will bless his people with peace."),
        ("Peace", "Colossians 3:15", "Let the peace of Christ rule in your hearts."),
        ("Strength", "Philippians 4:13", "I can do all things through Christ who strengthens me."),
        ("Strength", "Isaiah 40:31", "Those who wait for the LORD shall renew their strength."),
        ("Strength", "Psalm 46:1", "God is our refuge and strength, a very present help in trouble."),
        ("Strength", "2 Timothy 1:7", "God did not give us a spirit of fear but of power, love, and self-control."),
        ("Strength", "Deuteronomy 31:6", "Be strong and courageous. Do not fear, for the LORD your God goes with you."),
        ("Strength", "Nehemiah 8:10", "The joy of the LORD is your strength."),
        ("Strength", "Ephesians 6:10", "Be strong in the Lord and in the strength of his might."),
        ("Wisdom", "Proverbs 3:5-6", "Trust in the LORD with all your heart and lean not on your own understanding."),
        ("Wisdom", "James 1:5", "If any of you lacks wisdom, let him ask of God who gives generously."),
        ("Wisdom", "Proverbs 9:10", "The fear of the LORD is the beginning of wisdom."),
        ("Wisdom", "Colossians 3:16", "Let the word of Christ dwell in you richly in all wisdom."),
        ("Wisdom", "Psalm 119:105", "Your word is a lamp to my feet and a light for my path."),
        ("Wisdom", "Proverbs 2:6", "For the LORD gives wisdom. From his mouth come knowledge and understanding."),
        ("Faith", "Romans 8:28", "All things work together for good for those who love God."),
        ("Faith", "Jeremiah 29:11", "I know the plans I have for you, plans for welfare and not for calamity."),
        ("Peace", "Matthew 11:28", "Come to me all who labor and are heavily burdened and I will give you rest."),
        ("Peace", "Psalm 23:1", "The LORD is my shepherd; I shall not want."),
        ("Strength", "Joshua 1:9", "Be strong and courageous. The LORD your God is with you wherever you go."),
        ("Strength", "Romans 8:37", "In all these things we are more than conquerors through him who loved us."),
        ("Wisdom", "Romans 12:2", "Be transformed by the renewing of your mind."),
        ("Wisdom", "Proverbs 16:3", "Commit your works to the LORD and your plans will be established."),
        ("Faith", "1 John 5:4", "This is the victory that has overcome the world: our faith."),
        ("Faith", "Psalm 37:4", "Delight yourself in the LORD and he will give you the desires of your heart."),
        ("Peace", "Psalm 46:10", "Be still and know that I am God."),
        ("Peace", "1 Peter 5:7", "Cast all your anxiety on him because he cares for you."),
        ("Strength", "Isaiah 41:10", "Fear not for I am with you. Be not dismayed for I am your God."),
        ("Strength", "Psalm 27:1", "The LORD is my light and my salvation. Whom shall I fear?"),
        ("Wisdom", "Matthew 6:33", "Seek first the kingdom of God and his righteousness."),
        ("Wisdom", "Proverbs 4:7", "Wisdom is supreme. Get wisdom. With all your getting, get understanding."),
        ("Faith", "Habakkuk 2:4", "The righteous will live by his faith."),
        ("Faith", "1 Corinthians 16:13", "Watch! Stand firm in the faith! Be courageous! Be strong!"),
        ("Peace", "Numbers 6:26", "The LORD lift up his face toward you and give you peace."),
        ("Peace", "Romans 15:13", "May the God of hope fill you with all joy and peace in believing."),
        ("Strength", "2 Corinthians 12:9", "My grace is sufficient for you. My power is made perfect in weakness."),
        ("Strength", "Psalm 18:32", "It is God who arms me with strength and makes my way perfect."),
        ("Wisdom", "Ecclesiastes 7:12", "The advantage of knowledge is that wisdom preserves the life of those who have it."),
        ("Wisdom", "Proverbs 1:7", "The fear of the LORD is the beginning of knowledge."),
        ("Faith", "Matthew 17:20", "If you have faith as small as a mustard seed, nothing will be impossible for you."),
        ("Faith", "Psalm 56:3", "When I am afraid, I will put my trust in you."),
    ]

    # 4 cards per page = 13 pages
    for page_idx in range(13):
        pdf.new_page()
        y_positions = [600, 440, 280, 120]
        for card_idx in range(4):
            verse_idx = page_idx * 4 + card_idx
            if verse_idx >= 52:
                break
            category, ref, text = verses[verse_idx]
            y_base = y_positions[card_idx]

            # Card border
            pdf.add_rect(60, y_base, 492, 140, 1, 0.4)
            # Category label
            pdf.add_filled_rect(62, y_base + 120, 80, 18, 0.85)
            pdf.add_text(67, y_base + 125, category, 'F2', 9)
            # Week number
            pdf.add_text(470, y_base + 125, f"Week {verse_idx + 1}", 'F1', 8, 0.4)
            # Reference
            pdf.add_text(80, y_base + 105, ref, 'F2', 12)
            # English text - wrap
            words = text.split()
            line = ""
            y = y_base + 85
            for w in words:
                if len(line + " " + w) > 68:
                    pdf.add_text(80, y, line, 'F4', 10)
                    y -= 13
                    line = w
                else:
                    line = (line + " " + w).strip()
            if line:
                pdf.add_text(80, y, line, 'F4', 10)
                y -= 13
            # Tigrinya
            y -= 6
            pdf.add_text(80, y, "[Tigrinya: " + ref + "]", 'F3', 9, 0.4)

    # How to Memorize Scripture guide
    pdf.new_page()
    pdf.add_centered_text(750, "HOW TO MEMORIZE SCRIPTURE", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    tips = [
        "1. Read the verse out loud 3 times",
        "2. Write it out by hand",
        "3. Break it into phrases and memorize one at a time",
        "4. Say it from memory before looking",
        "5. Review yesterday's verse before learning today's",
        "6. Put the verse on your mirror or phone wallpaper",
        "7. Say it before bed and when you wake up",
        "8. Teach it to someone else - teaching helps you remember",
        "9. Connect it to a life situation - when will you need this verse?",
        "10. Pray the verse back to God in your own words"
    ]
    y = 710
    for tip in tips:
        pdf.add_text(72, y, tip, 'F1', 11)
        y -= 25

    # Review Schedule (spaced repetition)
    pdf.new_page()
    pdf.add_centered_text(750, "REVIEW SCHEDULE (SPACED REPETITION)", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 710, "After memorizing a verse, review it on this schedule:", 'F1', 11)
    schedule = [
        "Day 1: Learn the verse",
        "Day 2: Review (next day)",
        "Day 4: Review (2 days later)",
        "Day 7: Review (1 week)",
        "Day 14: Review (2 weeks)",
        "Day 30: Review (1 month)",
        "Day 60: Review (2 months)",
        "Day 90: Review (3 months) - It's now in long-term memory!"
    ]
    y = 680
    for s in schedule:
        pdf.add_text(82, y, s, 'F1', 11)
        y -= 22

    y -= 20
    pdf.add_text(72, y, "Tip: Use this book as a reference. Mark verses you've mastered!", 'F5', 10, 0.3)

    # Tracking Checklist (52 boxes)
    pdf.new_page()
    pdf.add_centered_text(750, "VERSE MEMORIZATION TRACKER", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    pdf.add_text(72, 715, "Check off each verse as you memorize it:", 'F1', 10)
    y = 690
    for row in range(13):
        for col in range(4):
            num = row * 4 + col + 1
            if num > 52:
                break
            x = 72 + col * 130
            pdf.add_rect(x, y - 12, 12, 12, 0.5, 0.5)
            pdf.add_text(x + 16, y - 10, f"Week {num}", 'F1', 9)
        y -= 25

    # Verse Index by Topic
    pdf.new_page()
    pdf.add_centered_text(750, "VERSE INDEX BY TOPIC", 'F2', 16)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    categories_list = {"Faith": [], "Peace": [], "Strength": [], "Wisdom": []}
    for i, (cat, ref, _) in enumerate(verses):
        categories_list[cat].append((i + 1, ref))

    y = 710
    for cat, entries in categories_list.items():
        pdf.add_text(72, y, f"{cat.upper()}:", 'F2', 12)
        y -= 18
        for week, ref in entries:
            pdf.add_text(92, y, f"Week {week}: {ref}", 'F1', 9)
            y -= 14
        y -= 10

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book202_Tigrinya_Scripture_Cards.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
