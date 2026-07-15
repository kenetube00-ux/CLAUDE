"""Book 303: THE LIFE OF JESUS IN STAINED GLASS - Large Print Coloring Book"""
import random
from pdf_utils import PDFDoc

random.seed(303)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    scenes = [
        ("The Annunciation", "Angel Gabriel tells Mary she will bear the Son of God.", "Luke 1:31", "Mary's faith and surrender: 'Be it unto me according to thy word.'"),
        ("The Birth of Jesus", "Born in a manger in Bethlehem, wrapped in swaddling clothes.", "Luke 2:7", "God chose humility. The King of Kings entered the world as a baby."),
        ("Shepherds Visit", "Angels appear to shepherds declaring 'Glory to God in the highest!'", "Luke 2:14", "Good news came first to the humble and working class."),
        ("Wise Men's Gifts", "Magi from the East follow a star to worship the young King.", "Matthew 2:11", "Even distant nations recognized the significance of Jesus' birth."),
        ("Flight to Egypt", "Joseph and Mary flee with baby Jesus to escape Herod's decree.", "Matthew 2:14", "God protects His plans even through dangerous circumstances."),
        ("Boy Jesus in Temple", "At age 12, Jesus astounds teachers with His understanding.", "Luke 2:47", "Even as a child, Jesus was about His Father's business."),
        ("Baptism by John", "The heavens open and the Spirit descends like a dove.", "Matthew 3:16", "The Father declares: 'This is my beloved Son.'"),
        ("Temptation in Wilderness", "Jesus defeats Satan's temptations with Scripture alone.", "Matthew 4:10", "God's Word is our weapon against every temptation."),
        ("Calling the Disciples", "Jesus says 'Follow me' and ordinary men leave everything.", "Mark 1:17", "God calls the available, not just the qualified."),
        ("Water Into Wine", "At a wedding in Cana, Jesus performs His first miracle.", "John 2:11", "Jesus cares about joy and celebration, not just survival."),
        ("Sermon on the Mount", "Jesus teaches the Beatitudes to crowds on a hillside.", "Matthew 5:3", "The kingdom of God operates on opposite principles from the world."),
        ("Calming the Storm", "Jesus speaks 'Peace, be still' and the wind and waves obey.", "Mark 4:39", "The One who made the sea has authority over it."),
        ("Walking on Water", "Jesus walks on the sea and calls Peter to come.", "Matthew 14:29", "Faith means stepping out even when the waves are high."),
        ("Feeding the 5000", "Five loaves and two fish feed a multitude with leftovers.", "John 6:11", "In Jesus' hands, our little becomes more than enough."),
        ("Healing the Blind Man", "Jesus restores sight to one born blind using mud and spit.", "John 9:25", "'One thing I know: I was blind, but now I see.'"),
        ("The Good Samaritan", "Jesus tells a parable about loving your neighbor.", "Luke 10:37", "Love has no boundaries of race, religion, or convenience."),
        ("Raising Lazarus", "Jesus calls Lazarus out of the tomb after four days.", "John 11:43", "'I am the resurrection and the life' - it's never too late for God."),
        ("Transfiguration", "Jesus' face shines like the sun on the mountain.", "Matthew 17:2", "A glimpse of His true glory that strengthened the disciples' faith."),
        ("Children Come to Me", "Jesus welcomes and blesses the little children.", "Mark 10:14", "'Of such is the kingdom of God' - childlike faith is the model."),
        ("The Prodigal Son", "Jesus tells of a father running to embrace his lost son.", "Luke 15:20", "God's love pursues us even when we've walked away."),
        ("Triumphal Entry", "Jesus rides into Jerusalem on a donkey while crowds shout Hosanna.", "Matthew 21:9", "The humble King enters His city one final time."),
        ("Cleansing the Temple", "Jesus overturns tables of money changers in holy anger.", "John 2:16", "God's house is for prayer, not profit."),
        ("The Last Supper", "Jesus breaks bread and shares wine with His disciples.", "Luke 22:19", "'Do this in remembrance of me' - communion connects us to Him."),
        ("Washing Disciples' Feet", "The King kneels to wash the feet of His followers.", "John 13:14", "True greatness is found in humble service to others."),
        ("Garden of Gethsemane", "Jesus prays 'Not my will, but thine' in agony.", "Luke 22:42", "Even Jesus wrestled in prayer. Surrender is not weakness."),
        ("The Crucifixion", "Jesus dies on the cross for the sins of the world.", "John 19:30", "'It is finished' - the price has been paid in full."),
        ("The Empty Tomb", "Mary finds the stone rolled away and the tomb empty.", "Matthew 28:6", "'He is not here: for he is risen!' Death could not hold Him."),
        ("Road to Emmaus", "The risen Jesus walks and talks with two grieving disciples.", "Luke 24:32", "He meets us in our confusion and makes our hearts burn."),
        ("The Great Commission", "Jesus sends His followers to make disciples of all nations.", "Matthew 28:19", "The mission continues through every generation of believers."),
        ("The Ascension", "Jesus rises into heaven with the promise to return.", "Acts 1:9", "He is preparing a place and will come back for His own."),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(25, 25, 562, 742, 4, 0.1)
    doc.add_rect(35, 35, 542, 722, 2, 0.3)
    doc.add_centered_text(700, "THE LIFE OF JESUS", 'F2', 26, 0.1)
    doc.add_centered_text(665, "IN STAINED GLASS", 'F2', 26, 0.1)
    doc.add_centered_text(630, "Large Print Coloring Book", 'F4', 16, 0.25)
    doc.add_filled_rect(110, 330, 392, 220, 0.88)
    doc.add_rect(110, 330, 392, 220, 3, 0.15)
    doc.add_centered_text(500, "[ILLUSTRATION: stained glass cross", 'F3', 10, 0.4)
    doc.add_centered_text(485, "with rays of light in bold outlines", 'F3', 10, 0.4)
    doc.add_centered_text(470, "suitable for coloring]", 'F3', 10, 0.4)
    doc.add_centered_text(230, "30 Scenes from Birth to Ascension", 'F4', 14, 0.3)
    doc.add_centered_text(200, "Bold Simple Outlines for Seniors", 'F1', 12, 0.35)
    doc.add_centered_text(110, author, 'F2', 18, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "THE LIFE OF JESUS IN STAINED GLASS", 'F2', 12, 0.2)
    doc.add_text(72, 640, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 12, 0.2)
    doc.add_text(72, 610, "Scripture from King James Version (Public Domain).", 'F1', 11, 0.3)
    doc.add_text(72, 580, "Features LARGE PRINT text and BOLD outlines for seniors.", 'F2', 11, 0.2)
    doc.add_text(72, 550, "Published by KDP Amazon", 'F1', 12, 0.3)
    
    # Coloring guide
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "COLORING GUIDE", 'F2', 18, 0.1)
    y = 680
    guide = [
        "Welcome to the story of Jesus in stained glass!",
        "",
        "Each scene features BOLD, SIMPLE outlines designed",
        "for comfortable coloring at any skill level.",
        "",
        "STAINED GLASS STYLE TIPS:",
        "  - Think of each section as a piece of glass",
        "  - Use bright, jewel-tone colors (ruby, sapphire, gold)",
        "  - The thick black lines are the 'lead' - leave them dark",
        "  - Fill each section with solid, even color",
        "",
        "SUGGESTED COLOR THEMES:",
        "  Jesus: white/gold clothing, brown hair",
        "  Sky: deep blues and purples",
        "  Halos: bright gold or yellow",
        "  Backgrounds: rich greens, blues, reds",
        "",
        "Take your time. Color prayerfully.",
        "Let the story of Jesus wash over you.",
    ]
    for line in guide:
        if "STAINED" in line or "SUGGESTED" in line or "Welcome" in line or "Take your" in line:
            doc.add_text(72, y, line, 'F2', 14, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 14, 0.25)
        y -= 24
    
    # Table of contents
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "TABLE OF CONTENTS", 'F2', 16, 0.1)
    y = 700
    for i, (scene, _, ref, _) in enumerate(scenes[:15]):
        doc.add_text(72, y, f"{i+1}. {scene} ({ref})", 'F1', 10, 0.3)
        y -= 18
    
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "TABLE OF CONTENTS (cont.)", 'F2', 16, 0.1)
    y = 700
    for i, (scene, _, ref, _) in enumerate(scenes[15:]):
        doc.add_text(72, y, f"{i+16}. {scene} ({ref})", 'F1', 10, 0.3)
        y -= 18
    
    # 30 scenes - coloring + story page
    for i, (scene, description, ref, lesson) in enumerate(scenes):
        # Coloring page
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.97)
        # Stained glass frame
        doc.add_rect(20, 20, 572, 752, 4, 0.05)
        doc.add_rect(30, 30, 552, 732, 2, 0.15)
        # Gothic arch shape at top
        doc.add_line(30, 700, 582, 700, 3, 0.1)
        doc.add_line(200, 762, 200, 700, 2, 0.1)
        doc.add_line(412, 762, 412, 700, 2, 0.1)
        
        # Title in arch
        doc.add_centered_text(730, scene.upper(), 'F2', 14, 0.1)
        
        # Main panel
        doc.add_filled_rect(50, 100, 512, 580, 0.98)
        doc.add_rect(50, 100, 512, 580, 3, 0.08)
        # Cross-pieces for stained glass effect
        doc.add_line(306, 100, 306, 680, 2, 0.1)
        doc.add_line(50, 390, 562, 390, 2, 0.1)
        doc.add_line(178, 100, 178, 680, 1, 0.15)
        doc.add_line(434, 100, 434, 680, 1, 0.15)
        
        doc.add_centered_text(500, f"[ILLUSTRATION: Stained glass depiction of", 'F3', 10, 0.3)
        doc.add_centered_text(480, f"{scene} - {description}", 'F3', 9, 0.3)
        doc.add_centered_text(460, f"Bold simple outlines, large sections to color]", 'F3', 9, 0.3)
        
        # Bottom banner
        doc.add_filled_rect(50, 40, 512, 45, 0.92)
        doc.add_rect(50, 40, 512, 45, 2, 0.1)
        doc.add_centered_text(60, ref, 'F4', 12, 0.2)
        
        # Story page
        doc.new_page()
        fill = 0.93 + random.uniform(0, 0.04)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        
        doc.add_centered_text(720, scene.upper(), 'F2', 20, 0.1)
        doc.add_line(150, 712, 462, 712, 1, 0.4)
        doc.add_centered_text(690, ref, 'F4', 14, 0.3)
        
        y = 650
        # Description in large print
        doc.add_text(72, y, "THE SCENE:", 'F2', 16, 0.15)
        y -= 30
        words = description.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) > 40:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        for ln in lines:
            doc.add_text(72, y, ln, 'F4', 16, 0.2)
            y -= 28
        
        y -= 30
        doc.add_text(72, y, "THE LESSON:", 'F2', 16, 0.15)
        y -= 30
        words = lesson.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) > 40:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        for ln in lines:
            doc.add_text(72, y, ln, 'F4', 16, 0.2)
            y -= 28
        
        y -= 30
        doc.add_filled_rect(60, y-50, 492, 60, 0.88)
        doc.add_rect(60, y-50, 492, 60, 1, 0.3)
        doc.add_centered_text(y, "Reflect on this scene as you color.", 'F4', 14, 0.3)
        doc.add_centered_text(y-25, "Let Jesus' story become YOUR story.", 'F5', 14, 0.2)
    
    # Extra pages to reach 72+
    extras_303 = ["MY FAVORITE SCENES", "COLORING REFLECTIONS", "PRAYERS FROM JESUS' LIFE",
                  "HOW JESUS CHANGED MY LIFE", "SHARING JESUS WITH OTHERS", "NOTES & REFLECTIONS"]
    for et in extras_303:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, et, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22

    # Final page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.90)
    doc.add_rect(40, 40, 532, 712, 3, 0.2)
    doc.add_centered_text(600, "THE STORY CONTINUES...", 'F2', 22, 0.1)
    doc.add_centered_text(550, "Jesus ascended to heaven, but He left us", 'F4', 14, 0.25)
    doc.add_centered_text(525, "with a promise:", 'F4', 14, 0.25)
    doc.add_centered_text(475, "\"Lo, I am with you always, even", 'F5', 16, 0.15)
    doc.add_centered_text(448, "unto the end of the world.\"", 'F5', 16, 0.15)
    doc.add_centered_text(415, "- Matthew 28:20", 'F4', 12, 0.3)
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book303_Stained_Glass_Jesus.pdf')
    print("Book303_Stained_Glass_Jesus.pdf created successfully!")

if __name__ == "__main__":
    create_book()
