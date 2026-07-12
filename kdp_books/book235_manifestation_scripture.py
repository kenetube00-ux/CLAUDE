"""Book 235: Declare & Believe - Scripture-Based Manifestation Journal"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)  # 6x9
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 560, 432, 88, 0.15)
    doc.add_centered_text(608, "DECLARE & BELIEVE", 'F2', 20, 1)
    doc.add_centered_text(578, "A 90-Day Scripture-Based", 'F5', 14, 1)
    doc.add_centered_text(555, "Manifestation & Declaration Journal", 'F5', 14, 1)
    doc.add_centered_text(500, "Speak God's Word Over Your Life Daily", 'F4', 11, 0.3)
    doc.add_centered_text(150, author, 'F2', 12, 0.3)

    doc.new_page()
    doc.add_centered_text(560, "DECLARE & BELIEVE", 'F2', 12)
    doc.add_centered_text(540, "A 90-Day Scripture-Based Manifestation & Declaration Journal", 'F1', 9)
    doc.add_centered_text(505, f"Copyright {author}. All rights reserved.", 'F1', 9)

    # What the Bible Says About Declarations
    doc.new_page()
    doc.add_centered_text(610, "WHAT THE BIBLE SAYS ABOUT DECLARATIONS", 'F2', 11)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    verses = [
        "'Death and life are in the power of the tongue.'",
        "  - Proverbs 18:21", "",
        "'Truly I tell you, if anyone says to this mountain,",
        "Be lifted up and thrown into the sea, and does not doubt",
        "in their heart, but believes that what they say will happen,",
        "it will be done for them.' - Mark 11:23-24", "",
        "'As it is written: I have made you a father of many nations.",
        "He is our father in the sight of God, in whom he believed -",
        "the God who gives life to the dead and calls into being",
        "things that were not.' - Romans 4:17", "",
        "God SPOKE the world into existence.",
        "You are made in His image.",
        "Your words carry creative power.",
        "Declare His promises over your life!", "",
    ]
    for line in verses:
        doc.add_text(50, y, line, 'F4', 9)
        y -= 13

    # The Power of Speaking God's Word
    doc.new_page()
    doc.add_centered_text(610, "THE POWER OF SPEAKING GOD'S WORD", 'F2', 11)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    lines = ["When you declare Scripture out loud, you:", "",
        "  1. Align your words with God's truth",
        "  2. Replace lies with promises",
        "  3. Build your faith (faith comes by hearing!)",
        "  4. Release spiritual authority",
        "  5. Shift your atmosphere", "",
        "How to use this journal:", "",
        "  - Speak your declarations OUT LOUD each morning",
        "  - Write the scripture you're standing on",
        "  - Record what you're believing God for",
        "  - Take one action step in faith daily",
        "  - Note what you're grateful for",
        "  - Watch for signs, confirmations, and answers", "",
        "Commitment: I will declare God's Word daily for 90 days.",
        "", "Signed: ________________  Date: ___/___/___"]
    for line in lines:
        doc.add_text(50, y, line, 'F1', 9)
        y -= 13


    # My Faith Declarations (10 areas)
    doc.new_page()
    doc.add_centered_text(610, "MY FAITH DECLARATIONS - 10 AREAS", 'F2', 11)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    areas = ["HEALTH", "FINANCES", "FAMILY", "PURPOSE", "PEACE",
             "RELATIONSHIPS", "WISDOM", "PROVISION", "PROTECTION", "DESTINY"]
    for area in areas:
        doc.add_text(50, y, f"{area}:", 'F2', 8)
        y -= 12
        doc.add_text(60, y, "I declare: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(60, y, "Scripture: ________________________________", 'F4', 8)
        y -= 16

    # 90 Daily Entries (3 per page = 30 pages)
    for page in range(30):
        doc.new_page()
        for entry in range(3):
            day_num = page * 3 + entry + 1
            if day_num > 90:
                break
            y_start = 615 - entry * 200
            doc.add_text(50, y_start, f"DAY {day_num}", 'F2', 9)
            doc.add_text(130, y_start, "Date: ___/___", 'F1', 8)
            y = y_start - 14
            doc.add_text(50, y, "Today I declare:", 'F2', 8)
            y -= 12
            doc.add_line(50, y, 382, y, 0.5, 0.5)
            y -= 12
            doc.add_line(50, y, 382, y, 0.5, 0.5)
            y -= 14
            doc.add_text(50, y, "Scripture I stand on:", 'F4', 8)
            doc.add_line(160, y-2, 382, y-2, 0.5, 0.5)
            y -= 14
            doc.add_text(50, y, "What I'm believing God for:", 'F1', 8)
            doc.add_line(195, y-2, 382, y-2, 0.5, 0.5)
            y -= 14
            doc.add_text(50, y, "Action I'm taking in faith:", 'F1', 8)
            doc.add_line(190, y-2, 382, y-2, 0.5, 0.5)
            y -= 14
            doc.add_text(50, y, "Grateful for:", 'F1', 8)
            doc.add_line(115, y-2, 382, y-2, 0.5, 0.5)
            y -= 14
            doc.add_text(50, y, "Signs/confirmations:", 'F1', 8)
            doc.add_line(155, y-2, 382, y-2, 0.5, 0.5)
            y -= 8
            doc.add_line(50, y, 382, y, 0.3, 0.4)

    # Monthly Declaration Review (3 pages)
    for month in range(1, 4):
        doc.new_page()
        doc.add_centered_text(610, f"MONTHLY DECLARATION REVIEW - MONTH {month}", 'F2', 11)
        doc.add_line(50, 598, 382, 598, 0.5, 0.3)
        y = 575
        prompts = ["What has manifested this month:", "________________________________",
            "________________________________", "",
            "What I'm still believing for:", "________________________________",
            "________________________________", "",
            "How my faith has been strengthened:", "________________________________",
            "________________________________", "",
            "Scriptures that came alive this month:", "________________________________", "",
            "Prayers answered:", "________________________________", "",
            "My declaration for next month:", "________________________________",
            "________________________________"]
        for p in prompts:
            doc.add_text(50, y, p, 'F1', 9)
            y -= 13


    # 30 "I Am" Declarations with Scripture
    doc.new_page()
    doc.add_centered_text(610, "30 'I AM' DECLARATIONS WITH SCRIPTURE", 'F2', 11)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    declarations = [
        ("I am loved.", "Romans 8:38-39"),
        ("I am forgiven.", "1 John 1:9"),
        ("I am chosen.", "1 Peter 2:9"),
        ("I am healed.", "Isaiah 53:5"),
        ("I am provided for.", "Philippians 4:19"),
        ("I am more than a conqueror.", "Romans 8:37"),
        ("I am the head and not the tail.", "Deuteronomy 28:13"),
        ("I am blessed coming in and going out.", "Deuteronomy 28:6"),
        ("I am a new creation.", "2 Corinthians 5:17"),
        ("I am victorious.", "1 John 5:4"),
        ("I am fearfully and wonderfully made.", "Psalm 139:14"),
        ("I am strong in the Lord.", "Ephesians 6:10"),
        ("I am at peace.", "John 14:27"),
        ("I am prosperous.", "Jeremiah 29:11"),
        ("I am protected.", "Psalm 91:11"),
    ]
    for decl, verse in declarations:
        doc.add_text(50, y, f"{decl}", 'F2', 8)
        doc.add_text(250, y, f"({verse})", 'F4', 7)
        y -= 12

    doc.new_page()
    doc.add_centered_text(610, "'I AM' DECLARATIONS CONTINUED", 'F2', 11)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    declarations2 = [
        ("I am wise.", "James 1:5"),
        ("I am free.", "John 8:36"),
        ("I am an overcomer.", "Revelation 12:11"),
        ("I am God's workmanship.", "Ephesians 2:10"),
        ("I am the righteousness of God.", "2 Corinthians 5:21"),
        ("I am complete in Christ.", "Colossians 2:10"),
        ("I am anointed.", "1 John 2:27"),
        ("I am a child of the King.", "Galatians 3:26"),
        ("I am able to do all things.", "Philippians 4:13"),
        ("I am surrounded by favor.", "Psalm 5:12"),
        ("I am redeemed.", "Galatians 3:13"),
        ("I am walking in purpose.", "Ephesians 2:10"),
        ("I am an heir of God.", "Romans 8:17"),
        ("I am filled with the Holy Spirit.", "Acts 1:8"),
        ("I am destined for greatness.", "Jeremiah 1:5"),
    ]
    for decl, verse in declarations2:
        doc.add_text(50, y, f"{decl}", 'F2', 8)
        doc.add_text(250, y, f"({verse})", 'F4', 7)
        y -= 12

    # Prayer of Activation
    doc.new_page()
    doc.add_centered_text(610, "PRAYER OF ACTIVATION", 'F2', 13)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    prayer = [
        "Heavenly Father,",
        "I thank You that Your Word is alive and powerful.",
        "I activate these declarations over my life today.",
        "I speak in faith, knowing that You are faithful",
        "to perform Your Word.",
        "",
        "I declare that every promise You've made is YES",
        "and AMEN in my life. I align my words with Your truth.",
        "I release doubt, fear, and unbelief.",
        "I receive Your promises by faith.",
        "",
        "As I speak Your Word daily for these 90 days,",
        "I expect transformation, breakthrough, and testimony.",
        "Let my mouth be filled with Your praise",
        "and my declarations bring forth fruit.",
        "",
        "In Jesus' name, Amen.",
        "",
        "Today I begin. Today I declare. Today I believe.",
    ]
    for line in prayer:
        doc.add_text(50, y, line, 'F4', 9)
        y -= 14

    # My Testimony Journal
    doc.new_page()
    doc.add_centered_text(610, "MY TESTIMONY JOURNAL", 'F2', 13)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    doc.add_text(50, y, "Record when your declarations manifest!", 'F4', 9)
    y -= 18
    for t in range(1, 8):
        doc.add_text(50, y, f"TESTIMONY {t}:", 'F2', 8)
        y -= 12
        doc.add_text(50, y, "Date: ___/___  What I declared: ________________", 'F1', 8)
        y -= 12
        doc.add_text(50, y, "What happened: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(50, y, "________________________________", 'F1', 8)
        y -= 16

    doc.save("Book235_Faith_Manifestation_Journal.pdf")
    print("Created: Book235_Faith_Manifestation_Journal.pdf")

if __name__ == "__main__":
    create_book()
