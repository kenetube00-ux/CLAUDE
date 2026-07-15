"""Book 297: WHO IS GOD? - A 30-Day Names of God Study Workbook"""
import random
from pdf_utils import PDFDoc

random.seed(297)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    names = [
        ("Jehovah Jireh", "The Lord Will Provide", "Genesis 22:14", "Abraham named the place after God provided the ram."),
        ("El Shaddai", "God Almighty", "Genesis 17:1", "God revealed this name when making covenant with Abraham."),
        ("Jehovah Rapha", "The Lord Who Heals", "Exodus 15:26", "Revealed when God healed the bitter waters of Marah."),
        ("Prince of Peace", "Sar Shalom", "Isaiah 9:6", "A messianic prophecy about Christ's nature."),
        ("Wonderful Counselor", "Pele Yo'etz", "Isaiah 9:6", "His wisdom surpasses all human understanding."),
        ("El Roi", "The God Who Sees", "Genesis 16:13", "Hagar named God this when He found her in the wilderness."),
        ("Jehovah Nissi", "The Lord My Banner", "Exodus 17:15", "Moses built an altar after victory over Amalek."),
        ("Emmanuel", "God With Us", "Matthew 1:23", "The angel declared this name for Jesus before His birth."),
        ("Jehovah Shalom", "The Lord Is Peace", "Judges 6:24", "Gideon named an altar this after meeting the Angel of the Lord."),
        ("El Elyon", "The Most High God", "Genesis 14:18", "Melchizedek served as priest of El Elyon."),
        ("Adonai", "Lord, Master", "Psalm 8:1", "Used over 400 times in the Old Testament."),
        ("Jehovah Rohi", "The Lord My Shepherd", "Psalm 23:1", "David's most intimate description of God's care."),
        ("Alpha and Omega", "Beginning and End", "Revelation 1:8", "Christ declares His eternal nature."),
        ("Lion of Judah", "Conquering King", "Revelation 5:5", "Only He was worthy to open the sealed scroll."),
        ("Lamb of God", "Sacrificial Savior", "John 1:29", "John the Baptist proclaimed Jesus as the sacrifice."),
        ("Abba Father", "Daddy God", "Romans 8:15", "The Spirit of adoption gives us intimacy with God."),
        ("Jehovah Tsidkenu", "The Lord Our Righteousness", "Jeremiah 23:6", "A messianic prophecy about the righteous Branch."),
        ("Ancient of Days", "Eternal One", "Daniel 7:9", "Daniel's vision of God on His throne."),
        ("Bread of Life", "Sustainer", "John 6:35", "Jesus declared this after feeding the 5,000."),
        ("Light of the World", "Illuminator", "John 8:12", "Jesus spoke this during the Feast of Tabernacles."),
        ("Good Shepherd", "Caring Protector", "John 10:11", "The shepherd lays down his life for the sheep."),
        ("Resurrection and Life", "Death-Defeater", "John 11:25", "Spoken to Martha before raising Lazarus."),
        ("Way, Truth, Life", "The Only Path", "John 14:6", "Jesus' response to Thomas' question about the way."),
        ("True Vine", "Source of Life", "John 15:1", "Jesus taught about abiding and fruitfulness."),
        ("Deliverer", "Rescuer", "Romans 11:26", "Paul quotes Isaiah about the coming Deliverer."),
        ("Cornerstone", "Foundation", "Ephesians 2:20", "Christ is the foundation of the church."),
        ("King of Kings", "Supreme Ruler", "Revelation 19:16", "His title at His second coming."),
        ("Faithful and True", "Trustworthy One", "Revelation 19:11", "The name of the rider on the white horse."),
        ("I AM", "Self-Existent One", "Exodus 3:14", "God's self-revelation to Moses at the burning bush."),
        ("Everlasting Father", "Eternal Parent", "Isaiah 9:6", "His love and care have no beginning or end."),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(30, 30, 552, 732, 3, 0.2)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_centered_text(680, "WHO IS GOD?", 'F2', 30, 0.1)
    doc.add_centered_text(640, "A 30-Day Names of God", 'F4', 18, 0.25)
    doc.add_centered_text(615, "Study Workbook", 'F4', 18, 0.25)
    doc.add_filled_rect(130, 380, 352, 150, 0.88)
    doc.add_rect(130, 380, 352, 150, 2, 0.3)
    doc.add_centered_text(480, "[ILLUSTRATION: ancient scroll unrolling", 'F3', 10, 0.4)
    doc.add_centered_text(465, "with names of God written in gold]", 'F3', 10, 0.4)
    doc.add_centered_text(220, "Name + Meaning + Scripture + Application", 'F1', 11, 0.35)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "WHO IS GOD?", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    
    # How to use
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "HOW TO USE THIS WORKBOOK", 'F2', 16, 0.1)
    y = 685
    how = [
        "Each day you'll study one name of God through these lenses:",
        "",
        "1. THE NAME - the original language and pronunciation",
        "2. THE MEANING - what this name reveals about God",
        "3. THE SCRIPTURE - where this name appears in the Bible",
        "4. THE CONTEXT - the story behind the name",
        "5. WORD STUDY - key terms to understand",
        "6. LIFE APPLICATION - how this name applies TODAY",
        "7. PRAYER - a prayer using this name",
        "8. GROUP QUESTIONS - for small group discussion",
        "",
        "This workbook works for:",
        "  - Personal daily devotions (30 days)",
        "  - Small group Bible study (6-week series)",
        "  - Sunday school curriculum",
        "  - Deeper individual theology study",
    ]
    for line in how:
        if line and line[0].isdigit():
            doc.add_text(72, y, line, 'F2', 11, 0.15)
        else:
            doc.add_text(72, y, line, 'F4', 11, 0.25)
        y -= 20
    
    # 30 daily entries - 2 pages each
    for i, (name, meaning, ref, context) in enumerate(names):
        # Page 1: Study
        doc.new_page()
        fill = 0.92 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        
        # Header
        doc.add_filled_rect(40, 740, 532, 35, 0.88)
        doc.add_rect(40, 740, 532, 35, 1, 0.3)
        doc.add_text(55, 752, f"Day {i+1}: {name}", 'F2', 13, 0.1)
        doc.add_text(420, 752, meaning, 'F4', 10, 0.3)
        
        y = 715
        # Name and meaning
        doc.add_text(72, y, f"THE NAME: {name} ({meaning})", 'F2', 11, 0.15)
        y -= 22
        doc.add_text(72, y, f"SCRIPTURE: {ref}", 'F2', 11, 0.15)
        y -= 22
        doc.add_text(72, y, f"CONTEXT: {context}", 'F4', 10, 0.25)
        y -= 28
        
        # Word study
        doc.add_text(72, y, "WORD STUDY:", 'F2', 11, 0.15)
        y -= 18
        doc.add_text(72, y, f"Look up {ref} in your Bible. What words stand out?", 'F1', 10, 0.3)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "WHAT DOES THIS NAME REVEAL ABOUT GOD'S CHARACTER?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "LIFE APPLICATION - Where do I need God as this name today?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "MY PRAYER USING THIS NAME:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Page 2: Group questions + deeper study
        doc.new_page()
        fill2 = 0.94 + random.uniform(0, 0.03)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"Day {i+1}: {name} - DEEPER STUDY", 'F2', 12, 0.15)
        doc.add_line(55, 745, 557, 745, 1, 0.4)
        
        y = 720
        doc.add_text(72, y, "GROUP DISCUSSION QUESTIONS:", 'F2', 11, 0.15)
        y -= 20
        questions = [
            f"1. What does the name '{name}' mean to you personally?",
            f"2. Share a time God was '{meaning}' in your life.",
            "3. How would knowing this name change how you pray?",
            "4. What situation in our world needs God to be this name?",
            "5. How can we reflect this attribute of God to others?",
        ]
        for q in questions:
            doc.add_text(72, y, q, 'F1', 10, 0.25)
            y -= 18
        
        y -= 15
        doc.add_text(72, y, "CROSS-REFERENCES (look these up):", 'F2', 11, 0.15)
        y -= 18
        doc.add_text(72, y, "1. ________________________  2. ________________________", 'F1', 10, 0.3)
        y -= 18
        doc.add_text(72, y, "3. ________________________  4. ________________________", 'F1', 10, 0.3)
        y -= 28
        
        doc.add_text(72, y, "WHAT I LEARNED TODAY:", 'F2', 11, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "HOW I'LL LIVE DIFFERENTLY BECAUSE OF THIS NAME:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Rating box
        y -= 10
        doc.add_filled_rect(55, y-40, 502, 50, 0.88)
        doc.add_rect(55, y-40, 502, 50, 1, 0.3)
        doc.add_text(70, y, "How well do I know God as this name?  1  2  3  4  5", 'F1', 9, 0.3)
        doc.add_text(70, y-18, "Am I trusting Him as this name today?  [ ] Yes  [ ] Working on it", 'F1', 9, 0.3)
    
    # Summary page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.91)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "30 NAMES - SUMMARY", 'F2', 16, 0.1)
    y = 705
    for nm, meaning, ref, _ in names:
        doc.add_text(72, y, f"{nm} ({meaning}) - {ref}", 'F1', 8, 0.3)
        y -= 14
    
    # Additional bonus pages
    bonus_titles = ["NAMES I EXPERIENCED THIS MONTH", "MY TOP 5 NAMES AND WHY", "NAMES FOR HARD SEASONS",
                   "TEACHING THESE NAMES TO OTHERS", "PRAYERS USING GOD'S NAMES", "NOTES", "REFLECTIONS"]
    for bt in bonus_titles:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, bt, 'F2', 14, 0.1)
        doc.add_line(100, 725, 512, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22
    
    # Final reflection
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "FINAL REFLECTION", 'F2', 16, 0.1)
    y = 695
    doc.add_text(72, y, "After 30 days of studying God's names:", 'F4', 11, 0.25)
    y -= 30
    doc.add_text(72, y, "The name that impacted me most:", 'F2', 10, 0.15)
    y -= 18
    for _ in range(3):
        doc.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 10
    doc.add_text(72, y, "How my view of God has changed:", 'F2', 10, 0.15)
    y -= 18
    for _ in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 10
    doc.add_text(72, y, "The name I need to cling to in this season:", 'F2', 10, 0.15)
    y -= 18
    for _ in range(3):
        doc.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    y -= 10
    doc.add_text(72, y, "My commitment going forward:", 'F2', 10, 0.15)
    y -= 18
    for _ in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book297_Names_God_Study.pdf')
    print("Book297_Names_God_Study.pdf created successfully!")

if __name__ == "__main__":
    create_book()
