"""Book 296: KNOWING GOD - A Names of God Coloring & Meditation Journal"""
import random
from pdf_utils import PDFDoc

random.seed(296)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    names = [
        ("Jehovah Jireh", "The Lord Will Provide", "Genesis 22:14", "God sees your need before you do and provides in His perfect timing."),
        ("El Shaddai", "God Almighty", "Genesis 17:1", "He is all-sufficient. His power has no limit or end."),
        ("Jehovah Rapha", "The Lord Who Heals", "Exodus 15:26", "He heals bodies, hearts, minds, and relationships."),
        ("Prince of Peace", "Sar Shalom", "Isaiah 9:6", "He brings peace that surpasses understanding to every chaos."),
        ("Wonderful Counselor", "Pele Yo'etz", "Isaiah 9:6", "His wisdom is perfect. He guides when you cannot see the way."),
        ("El Roi", "The God Who Sees", "Genesis 16:13", "You are never invisible to Him. He sees every tear and triumph."),
        ("Jehovah Nissi", "The Lord My Banner", "Exodus 17:15", "He goes before you in battle. Victory belongs to Him."),
        ("Emmanuel", "God With Us", "Matthew 1:23", "He is not distant. He dwells among us, with us, in us."),
        ("Jehovah Shalom", "The Lord Is Peace", "Judges 6:24", "In the midst of war, He is wholeness and completeness."),
        ("El Elyon", "The Most High God", "Genesis 14:18", "Above all powers, rulers, and circumstances. Nothing is above Him."),
        ("Adonai", "Lord, Master", "Psalm 8:1", "He is the rightful ruler of your life, worthy of surrender."),
        ("Jehovah Rohi", "The Lord My Shepherd", "Psalm 23:1", "He leads, feeds, protects, and carries you through every valley."),
        ("Alpha and Omega", "Beginning and End", "Revelation 1:8", "He was there before time and will be there after it ends."),
        ("Lion of Judah", "Conquering King", "Revelation 5:5", "He is fierce in battle, undefeated, fighting for His people."),
        ("Lamb of God", "Sacrificial Savior", "John 1:29", "He chose to become the sacrifice. Love made Him willing."),
        ("Abba Father", "Daddy God", "Romans 8:15", "He is not a distant deity. He is your loving, present Father."),
        ("Jehovah Tsidkenu", "The Lord Our Righteousness", "Jeremiah 23:6", "He makes us right with God through His own perfection."),
        ("Ancient of Days", "Eternal One", "Daniel 7:9", "Before anything existed, He was. Time bows to Him."),
        ("Bread of Life", "Sustainer", "John 6:35", "He satisfies the deepest hunger of the soul."),
        ("Light of the World", "Illuminator", "John 8:12", "In Him there is no darkness. He reveals truth in every shadow."),
        ("Good Shepherd", "Caring Protector", "John 10:11", "He lays down His life for the sheep. That is you."),
        ("Resurrection and Life", "Death-Defeater", "John 11:25", "Death has no power over Him. He makes all things new."),
        ("Way, Truth, Life", "The Only Path", "John 14:6", "He is not one of many options. He is THE way to the Father."),
        ("True Vine", "Source of Life", "John 15:1", "Apart from Him we can do nothing. Connected to Him, we bear fruit."),
        ("Deliverer", "Rescuer", "Romans 11:26", "He breaks chains, opens prisons, and sets captives free."),
        ("Cornerstone", "Foundation", "Ephesians 2:20", "Everything is built on Him. Without Him, it all crumbles."),
        ("King of Kings", "Supreme Ruler", "Revelation 19:16", "Every knee will bow. Every king will submit to His throne."),
        ("Faithful and True", "Trustworthy One", "Revelation 19:11", "He has never broken a promise. He never will."),
        ("I AM", "Self-Existent One", "Exodus 3:14", "He needs nothing. He is complete in Himself. He simply IS."),
        ("Everlasting Father", "Eternal Parent", "Isaiah 9:6", "His love has no expiration date. It endures forever."),
    ]
    
    art_styles = [
        "flowing calligraphy with vine embellishments",
        "geometric mandala surrounding the name",
        "nature scene with the name woven into branches",
        "stained glass window frame with bold letters",
        "mountain landscape with name in clouds",
        "ocean waves forming the letters",
        "garden of flowers spelling the name",
        "sunrise/sunset with rays forming letters",
        "Celtic knot border with central name",
        "dove and olive branch framing the name",
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(25, 25, 562, 742, 3, 0.2)
    doc.add_rect(35, 35, 542, 722, 1, 0.5)
    doc.add_centered_text(680, "KNOWING GOD", 'F2', 30, 0.1)
    doc.add_centered_text(640, "A Names of God", 'F4', 18, 0.25)
    doc.add_centered_text(615, "Coloring & Meditation Journal", 'F4', 16, 0.3)
    doc.add_filled_rect(130, 350, 352, 180, 0.88)
    doc.add_rect(130, 350, 352, 180, 2, 0.3)
    doc.add_centered_text(480, "[ILLUSTRATION: artistic arrangement of", 'F3', 9, 0.4)
    doc.add_centered_text(465, "God's names in various lettering styles]", 'F3', 9, 0.4)
    doc.add_centered_text(250, "30 Names. 30 Meditations.", 'F4', 14, 0.3)
    doc.add_centered_text(225, "One Infinite God.", 'F2', 14, 0.2)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "KNOWING GOD", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    
    # Intro
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "INTRODUCTION", 'F2', 16, 0.1)
    y = 685
    intro = [
        "In ancient times, a person's name revealed their CHARACTER.",
        "",
        "God has MANY names in Scripture - and each one reveals a",
        "different facet of who He is. Like a diamond with many sides,",
        "each name shows us a new dimension of His nature.",
        "",
        "This journal explores 30 names of God. Each includes:",
        "  * A coloring page with the name artistically lettered",
        "  * A meditation page with the meaning and reflection prompts",
        "",
        "As you color each name, meditate on what it reveals:",
        "  - What does this name tell me about God's character?",
        "  - When have I experienced this aspect of God?",
        "  - How does knowing this name change my prayers?",
        "",
        "Take your time. Let each name sink deep into your soul.",
        "By the end, you will KNOW God more deeply than before.",
    ]
    for line in intro:
        if line.startswith("In ancient") or line.startswith("Take your"):
            doc.add_text(72, y, line, 'F5', 11, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 10, 0.25)
        y -= 18
    
    # 30 names - coloring + meditation pages
    for i, (name, meaning, ref, description) in enumerate(names):
        # Coloring page
        doc.new_page()
        fill = 0.89 + random.uniform(0, 0.08)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(25, 25, 562, 742, 2, 0.3)
        doc.add_rect(35, 35, 542, 722, 1, 0.5)
        
        art = art_styles[i % len(art_styles)]
        # Top decorative area
        doc.add_filled_rect(55, 580, 502, 160, 0.94)
        doc.add_rect(55, 580, 502, 160, 1, 0.4)
        doc.add_centered_text(710, f"[ILLUSTRATION: {art}]", 'F3', 9, 0.4)
        doc.add_centered_text(620, "Color this design as you meditate", 'F3', 8, 0.5)
        
        # Central name in decorative frame
        doc.add_filled_rect(80, 330, 452, 220, 0.97)
        doc.add_rect(80, 330, 452, 220, 3, 0.25)
        doc.add_rect(90, 340, 432, 200, 1, 0.5)
        doc.add_centered_text(500, name.upper(), 'F2', 22, 0.1)
        doc.add_centered_text(465, f"({meaning})", 'F4', 14, 0.3)
        doc.add_centered_text(430, ref, 'F1', 11, 0.4)
        doc.add_centered_text(380, "Meditate on this name as you color", 'F4', 10, 0.4)
        
        # Bottom artwork area
        doc.add_filled_rect(55, 50, 502, 250, 0.93)
        doc.add_rect(55, 50, 502, 250, 1, 0.4)
        art2 = art_styles[(i+5) % len(art_styles)]
        doc.add_centered_text(220, f"[ILLUSTRATION: {art2}]", 'F3', 9, 0.4)
        
        # Corners
        for cx, cy in [(40, 750), (560, 750), (40, 40), (560, 40)]:
            doc.add_rect(cx-5, cy-5, 10, 10, 1, 0.3)
        
        # Meditation page
        doc.new_page()
        fill2 = 0.93 + random.uniform(0, 0.04)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        
        doc.add_centered_text(740, name.upper(), 'F2', 16, 0.1)
        doc.add_centered_text(718, f"{meaning} | {ref}", 'F4', 10, 0.3)
        doc.add_line(120, 712, 492, 712, 1, 0.4)
        
        y = 690
        doc.add_text(72, y, "MEANING:", 'F2', 11, 0.15)
        y -= 18
        doc.add_text(72, y, description, 'F4', 10, 0.25)
        y -= 30
        
        doc.add_text(72, y, "WHEN HAVE I EXPERIENCED GOD AS THIS NAME?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "HOW DOES THIS NAME CHANGE MY PRAYERS?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "WHERE DO I NEED GOD TO BE THIS NAME RIGHT NOW?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 18
        
        y -= 10
        doc.add_text(72, y, "MY PRAYER USING THIS NAME:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 18
    
    # Bonus pages
    bonus = ["ALL 30 NAMES - REVIEW", "MY FAVORITE NAMES OF GOD", "NAMES I NEED MOST RIGHT NOW",
             "PRAYERS USING GOD'S NAMES", "NAMES FOR EACH SEASON", "HOW I'VE EXPERIENCED THESE NAMES",
             "TEACHING OTHERS GOD'S NAMES", "NAMES JOURNAL", "NOTES"]
    for title in bonus:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.91)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, title, 'F2', 14, 0.1)
        doc.add_line(120, 725, 492, 725, 1, 0.4)
        y = 695
        if "REVIEW" in title:
            for nm, meaning, _, _ in names:
                doc.add_text(72, y, f"[ ] {nm} - {meaning}", 'F1', 9, 0.3)
                y -= 15
        else:
            for _ in range(28):
                doc.add_line(72, y, 540, y, 0.5, 0.6)
                y -= 22
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book296_Names_God_Coloring.pdf')
    print("Book296_Names_God_Coloring.pdf created successfully!")

if __name__ == "__main__":
    create_book()
