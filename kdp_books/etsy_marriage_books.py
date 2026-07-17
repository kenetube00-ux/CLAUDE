#!/usr/bin/env python3
"""Generate 20 Etsy-optimized Biblical Marriage PDFs (406-425)
Format: 8.5x11 printable digital downloads with interactive elements
Designed for Etsy instant download market - journals, planners, workbooks, devotionals"""
import sys, os
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

AUTHOR = "Daniel Tesfamariam"
BRAND = "Bible Made Simple"

def generate_etsy_book(book_num, filename, title, subtitle, pages_content):
    """Generate an Etsy-optimized printable PDF"""
    pdf = PDFDoc(width=612, height=792)  # 8.5x11 letter size (Etsy standard)
    
    # ===== COVER PAGE =====
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    pdf.add_filled_rect(0, 550, 612, 242, gray=0.15)
    pdf.add_rect(20, 20, 572, 752, line_width=3, gray=0.3)
    pdf.add_rect(28, 28, 556, 736, line_width=1, gray=0.5)
    
    # Title on dark band
    tlines = title.split('\n')
    ty = 720 if len(tlines) <= 2 else 740
    for i, tl in enumerate(tlines):
        pdf.add_centered_text(ty - i*40, tl, font='F2', size=28, gray=0.95)
    
    # Subtitle
    pdf.add_centered_text(560, subtitle, font='F4', size=14, gray=0.8)
    
    # Decorative elements
    pdf.add_line(100, 530, 512, 530, width=2, gray=0.3)
    pdf.add_centered_text(500, "A Printable Digital Download", font='F1', size=12, gray=0.3)
    pdf.add_centered_text(470, "For Christian Couples", font='F4', size=13, gray=0.3)
    
    # Features box
    pdf.add_filled_rect(100, 200, 412, 240, gray=0.88)
    pdf.add_rect(100, 200, 412, 240, line_width=1, gray=0.4)
    pdf.add_centered_text(420, "INSTANT DOWNLOAD INCLUDES:", font='F2', size=12, gray=0.2)
    features = ["Printable 8.5 x 11 Format", "Scripture-Based Content", 
                "Interactive Worksheets", "Guided Prompts & Exercises",
                "Print as Many Copies as You Need"]
    for i, f in enumerate(features):
        pdf.add_text(130, 390 - i*30, f"* {f}", font='F1', size=11, gray=0.2)
    
    # Author & brand
    pdf.add_centered_text(150, f"By {AUTHOR}", font='F2', size=14, gray=0.2)
    pdf.add_centered_text(120, BRAND, font='F1', size=11, gray=0.4)
    pdf.add_centered_text(60, "Personal Use License - Do Not Redistribute", font='F1', size=9, gray=0.5)
    
    # ===== TERMS OF USE PAGE =====
    pdf.new_page()
    pdf.add_centered_text(740, "Terms of Use", font='F2', size=18, gray=0.1)
    pdf.add_line(150, 730, 462, 730, width=0.5, gray=0.3)
    terms = [
        f"Thank you for purchasing {title}!",
        "",
        "PERSONAL USE LICENSE:",
        "- You may print unlimited copies for your personal/household use",
        "- You may use this in your small group or Bible study (up to 12 people)",
        "- You may NOT resell, redistribute, or share the digital file",
        "- You may NOT claim this content as your own",
        "- You may NOT upload this file to any website or sharing platform",
        "",
        "REFUND POLICY:",
        "Due to the digital nature of this product, all sales are final.",
        "If you experience any issues, please contact us before leaving a review.",
        "",
        "COPYRIGHT NOTICE:",
        f"(c) {AUTHOR} / {BRAND}. All rights reserved.",
        "Scripture quotations from the King James Version (Public Domain).",
        "",
        "We pray this resource blesses your marriage abundantly!",
    ]
    y = 690
    for line in terms:
        pdf.add_text(72, y, line, font='F1', size=10.5, gray=0.2)
        y -= 18
    
    # ===== HOW TO USE PAGE =====
    pdf.new_page()
    pdf.add_centered_text(740, "How to Use This Resource", font='F2', size=18, gray=0.1)
    pdf.add_line(150, 730, 462, 730, width=0.5, gray=0.3)
    howto = [
        "PRINTING TIPS:",
        "- Print on standard 8.5 x 11 inch paper (US Letter)",
        "- Use cardstock for cover pages for durability",
        "- Print single-sided or double-sided based on preference",
        "- Consider using a 3-ring binder for easy organization",
        "- Color printing recommended but works in black & white too",
        "",
        "GETTING STARTED:",
        "1. Print the pages you need (you don't have to print all at once)",
        "2. Set aside dedicated time with your spouse (30-60 min weekly)",
        "3. Read the Scripture passage together before starting exercises",
        "4. Complete prompts individually first, then share with each other",
        "5. Pray together after each session",
        "",
        "SUGGESTED SCHEDULE:",
        "- Complete one section per week for maximum impact",
        "- Choose a consistent day/time (e.g., Sunday evenings)",
        "- Allow extra time for deeper discussions as needed",
        "- Celebrate completion of each section together!",
    ]
    y = 690
    for line in howto:
        pdf.add_text(72, y, line, font='F1', size=10.5, gray=0.2)
        y -= 18
    
    # ===== CONTENT PAGES =====
    for page_data in pages_content:
        page_type = page_data[0]
        
        if page_type == "section_title":
            # Section divider page
            pdf.new_page()
            pdf.add_filled_rect(0, 350, 612, 150, gray=0.12)
            pdf.add_centered_text(440, page_data[1], font='F2', size=22, gray=0.95)
            if len(page_data) > 2:
                pdf.add_centered_text(390, page_data[2], font='F4', size=13, gray=0.8)
            pdf.add_line(150, 370, 462, 370, width=1, gray=0.3)
            
        elif page_type == "scripture_page":
            # Full scripture meditation page
            pdf.new_page()
            pdf.add_filled_rect(50, 550, 512, 200, gray=0.92)
            pdf.add_rect(50, 550, 512, 200, line_width=1, gray=0.4)
            pdf.add_centered_text(720, "Scripture Meditation", font='F2', size=14, gray=0.2)
            verse_lines = page_data[1].split('|')
            vy = 690
            for vl in verse_lines:
                pdf.add_centered_text(vy, vl.strip(), font='F5', size=12, gray=0.15)
                vy -= 20
            pdf.add_centered_text(560, page_data[2], font='F1', size=10, gray=0.4)
            # Reflection lines
            pdf.add_text(72, 510, "What does this verse mean for your marriage?", font='F2', size=11, gray=0.2)
            for i in range(8):
                y = 480 - i*30
                pdf.add_line(72, y, 540, y, width=0.5, gray=0.6)
            pdf.add_text(72, 220, "Prayer Response:", font='F2', size=11, gray=0.2)
            for i in range(5):
                y = 190 - i*30
                pdf.add_line(72, y, 540, y, width=0.5, gray=0.6)
                
        elif page_type == "journal_page":
            # Guided journal page with prompts and lines
            pdf.new_page()
            pdf.add_centered_text(760, page_data[1], font='F2', size=14, gray=0.15)
            pdf.add_line(72, 748, 540, 748, width=0.5, gray=0.3)
            if len(page_data) > 2:
                pdf.add_text(72, 725, page_data[2], font='F4', size=10, gray=0.3)
            # Prompts with writing lines
            prompts = page_data[3] if len(page_data) > 3 else ["Write your thoughts below:"]
            y = 700
            for prompt in prompts:
                if y < 100:
                    pdf.new_page()
                    pdf.add_text(500, 770, page_data[1][:30], font='F1', size=8, gray=0.5)
                    y = 740
                pdf.add_text(72, y, prompt, font='F2', size=10, gray=0.2)
                y -= 18
                # Add writing lines
                for j in range(4):
                    y -= 22
                    if y < 80: break
                    pdf.add_line(72, y, 540, y, width=0.3, gray=0.65)
                y -= 15
                
        elif page_type == "worksheet":
            # Interactive worksheet with boxes, checkmarks, ratings
            pdf.new_page()
            pdf.add_centered_text(760, page_data[1], font='F2', size=14, gray=0.15)
            pdf.add_line(72, 748, 540, 748, width=0.5, gray=0.3)
            items = page_data[2]
            y = 720
            for item in items:
                if y < 80:
                    pdf.new_page()
                    pdf.add_text(500, 770, page_data[1][:30], font='F1', size=8, gray=0.5)
                    y = 740
                if item.startswith("[BOX]"):
                    pdf.add_rect(72, y-12, 14, 14, line_width=0.5, gray=0.4)
                    pdf.add_text(95, y-8, item[5:], font='F1', size=10, gray=0.2)
                    y -= 28
                elif item.startswith("[RATE]"):
                    pdf.add_text(72, y, item[6:], font='F1', size=10, gray=0.2)
                    y -= 18
                    pdf.add_text(72, y, "1    2    3    4    5    6    7    8    9    10", font='F3', size=10, gray=0.3)
                    pdf.add_text(72, y-14, "(low)                                    (high)", font='F1', size=8, gray=0.5)
                    y -= 35
                elif item.startswith("[LINE]"):
                    pdf.add_text(72, y, item[6:], font='F1', size=10, gray=0.2)
                    y -= 18
                    pdf.add_line(72, y, 540, y, width=0.3, gray=0.65)
                    y -= 8
                    pdf.add_line(72, y, 540, y, width=0.3, gray=0.65)
                    y -= 25
                elif item.startswith("[HEADER]"):
                    pdf.add_text(72, y, item[8:], font='F2', size=11, gray=0.15)
                    y -= 22
                else:
                    pdf.add_text(72, y, item, font='F1', size=10, gray=0.2)
                    y -= 18
                    
        elif page_type == "planner_page":
            # Weekly/monthly planner layout
            pdf.new_page()
            pdf.add_centered_text(760, page_data[1], font='F2', size=14, gray=0.15)
            pdf.add_line(72, 748, 540, 748, width=0.5, gray=0.3)
            sections = page_data[2]
            y = 720
            for section in sections:
                if y < 100:
                    pdf.new_page()
                    y = 740
                pdf.add_filled_rect(72, y-5, 468, 22, gray=0.9)
                pdf.add_text(80, y, section, font='F2', size=10, gray=0.15)
                y -= 28
                for j in range(3):
                    pdf.add_line(90, y, 540, y, width=0.3, gray=0.6)
                    y -= 22
                y -= 10
                
        elif page_type == "prayer_page":
            # Structured prayer template
            pdf.new_page()
            pdf.add_centered_text(760, page_data[1], font='F2', size=14, gray=0.15)
            pdf.add_line(72, 748, 540, 748, width=0.5, gray=0.3)
            if len(page_data) > 2:
                pdf.add_text(72, 725, page_data[2], font='F4', size=10, gray=0.3)
            prayer_sections = page_data[3] if len(page_data) > 3 else ["Praise:", "Confession:", "Thanksgiving:", "Supplication:"]
            y = 695
            for ps in prayer_sections:
                if y < 100:
                    pdf.new_page()
                    y = 740
                pdf.add_text(72, y, ps, font='F2', size=11, gray=0.2)
                y -= 20
                for j in range(4):
                    pdf.add_line(90, y, 540, y, width=0.3, gray=0.6)
                    y -= 22
                y -= 15

        elif page_type == "checklist":
            # Checklist page
            pdf.new_page()
            pdf.add_centered_text(760, page_data[1], font='F2', size=14, gray=0.15)
            pdf.add_line(72, 748, 540, 748, width=0.5, gray=0.3)
            items = page_data[2]
            y = 720
            for item in items:
                if y < 60:
                    pdf.new_page()
                    y = 740
                pdf.add_rect(72, y-10, 12, 12, line_width=0.5, gray=0.4)
                pdf.add_text(92, y-7, item, font='F1', size=10, gray=0.2)
                y -= 24

    # ===== THANK YOU / FINAL PAGE =====
    pdf.new_page()
    pdf.add_filled_rect(0, 300, 612, 250, gray=0.12)
    pdf.add_centered_text(500, "Thank You!", font='F2', size=28, gray=0.95)
    pdf.add_centered_text(460, "We pray this resource transforms your marriage.", font='F4', size=13, gray=0.8)
    pdf.add_centered_text(420, "May God bless your union abundantly.", font='F4', size=13, gray=0.8)
    pdf.add_line(150, 390, 462, 390, width=1, gray=0.3)
    pdf.add_centered_text(360, f"By {AUTHOR}", font='F2', size=14, gray=0.8)
    pdf.add_centered_text(330, BRAND, font='F1', size=11, gray=0.7)
    pdf.add_centered_text(250, "If this blessed you, please leave a 5-star review!", font='F1', size=12, gray=0.3)
    pdf.add_centered_text(220, "Check our shop for more biblical marriage resources.", font='F1', size=11, gray=0.4)
    pdf.add_centered_text(150, "Scripture from King James Version (Public Domain)", font='F1', size=9, gray=0.5)
    
    # SAVE
    output = f"/projects/sandbox/CLAUDE/kdp_books/Book{book_num}_{filename}.pdf"
    pdf.save(output)
    fsize = os.path.getsize(output)
    with open(output, 'rb') as f:
        pcount = f.read().count(b'/Type /Page')
    print(f"  Book {book_num}: {title.split(chr(10))[0][:42]:<44} | {pcount:>3} pages | {fsize:,} bytes")
    return output, pcount



def make_journal_pages(topic, prompts_list):
    """Generate multiple journal pages for a topic"""
    pages = []
    for i, prompts in enumerate(prompts_list):
        pages.append(("journal_page", f"{topic} - Page {i+1}", 
                      f"Take time to reflect honestly with your spouse.",
                      prompts))
    return pages

def make_scripture_set(verses):
    """Generate scripture meditation pages"""
    pages = []
    for ref, text in verses:
        pages.append(("scripture_page", text, f"- {ref}"))
    return pages

def make_worksheet_set(title_prefix, worksheets):
    """Generate worksheet pages"""
    pages = []
    for ws_title, items in worksheets:
        pages.append(("worksheet", f"{title_prefix}: {ws_title}", items))
    return pages



def book_406():
    """Marriage Prayer Journal - 52 Weeks"""
    pages = []
    pages.append(("section_title", "52-Week Marriage\nPrayer Journal", "One Year of Praying Together"))
    for week in range(1, 53):
        themes = ["Unity","Trust","Communication","Forgiveness","Intimacy","Patience",
                  "Gratitude","Protection","Children","Finances","Purpose","Healing",
                  "Joy","Peace","Faithfulness","Kindness","Gentleness","Self-Control",
                  "Wisdom","Courage","Hope","Love","Grace","Mercy","Strength",
                  "Renewal","Restoration","Vision","Commitment","Sacrifice","Service",
                  "Worship","Humility","Obedience","Generosity","Contentment","Endurance",
                  "Breakthrough","Freedom","Blessing","Growth","Surrender","Abundance",
                  "Transformation","Revival","Honor","Respect","Romance","Adventure",
                  "Legacy","Celebration","Thanksgiving"]
        theme = themes[(week-1) % len(themes)]
        pages.append(("prayer_page", f"Week {week}: Praying for {theme}",
                      f"Theme: {theme} in Your Marriage",
                      [f"Praise God for {theme} in your life:",
                       f"Confess where you have lacked {theme}:",
                       f"Thank God for specific examples of {theme}:",
                       f"Ask God to increase {theme} in your marriage:",
                       "Pray for your spouse specifically:"]))
    return generate_etsy_book(406, "Etsy_Marriage_Prayer_Journal",
        "52-Week Marriage\nPrayer Journal", "A Year of United Prayer for Couples", pages)



def book_407():
    """Date Night Planner - 52 Dates"""
    pages = []
    pages.append(("section_title", "52 Date Nights\nfor Christian Couples", "One Year of Intentional Connection"))
    date_ideas = [
        ("Worship Night at Home", "Light candles, play worship music, pray together"),
        ("Scripture Memory Walk", "Walk together while memorizing a verse about love"),
        ("Cook a Biblical Meal", "Prepare a meal from Bible times - bread, fish, wine/juice"),
        ("Love Letter Exchange", "Write and read love letters to each other"),
        ("Stargazing & Prayer", "Go outdoors, look at stars, pray about God's vastness"),
        ("Service Date", "Volunteer together at church or community"),
        ("Marriage Book Club", "Read a chapter together and discuss"),
        ("Dream Session", "Share your 5-year vision for your marriage"),
        ("Photo Memory Night", "Look through old photos and share favorite memories"),
        ("Gratitude Dinner", "Take turns sharing 10 things you appreciate"),
        ("Adventure Challenge", "Try something new together - hiking, cooking class"),
        ("Sunset Picnic", "Pack a simple meal and watch the sunset together"),
        ("Game Night for Two", "Board games, card games, or create your own"),
        ("Budget Planning Date", "Make finances fun - plan a dream vacation"),
        ("Prayer Walk", "Walk your neighborhood praying for each house"),
        ("Creative Night", "Paint, draw, or craft together"),
        ("Breakfast in Bed", "One spouse surprises the other"),
        ("Dance Night", "Learn a new dance in your living room"),
        ("Testimony Night", "Share how God brought you together"),
        ("Future Letters", "Write letters to open on your next anniversary"),
        ("Spa Night at Home", "Pamper each other with massage and relaxation"),
        ("Dessert Crawl", "Visit 3 places for different desserts"),
        ("Nature Hike", "Explore a new trail and discuss God's creation"),
        ("Movie & Discussion", "Watch a faith-based film and discuss"),
        ("Puzzle Night", "Complete a puzzle together while talking"),
        ("Fondue Night", "Make fondue and feed each other"),
        ("Bookstore Date", "Browse together and buy each other a book"),
        ("Coffee Shop Writing", "Write prayers for each other at a cafe"),
        ("Farmers Market", "Shop together and cook what you find"),
        ("Music Night", "Share your favorite songs and why they matter"),
        ("Ice Cream & Questions", "Get ice cream and ask deep questions"),
        ("Bike Ride", "Ride bikes and stop for a picnic"),
        ("Bowling & Fun", "Be silly together - no competition"),
        ("Museum Visit", "Explore art or history together"),
        ("Thrift Store Challenge", "Buy each other a gift under $5"),
        ("Breakfast Date", "Early morning coffee shop before the day starts"),
        ("Garden Together", "Plant something and watch it grow like your love"),
        ("Karaoke Night", "Sing to each other at home"),
        ("Drive & Talk", "Scenic drive with no phones, just conversation"),
        ("Volunteer Together", "Serve at a soup kitchen or shelter"),
        ("Campfire Night", "Build a fire and share stories"),
        ("Yoga/Stretch Together", "Do a couples stretching routine"),
        ("Budget Cooking Challenge", "Cook a gourmet meal for under $10"),
        ("Sunrise Watch", "Wake early and watch the sunrise together"),
        ("DIY Project", "Build or create something for your home"),
        ("Library Date", "Read quietly together at the library"),
        ("Compliment Marathon", "Take turns complimenting for 10 minutes"),
        ("Vision Board Night", "Create a marriage vision board together"),
        ("Candlelit Dinner", "Dress up for dinner at home"),
        ("Couples Quiz", "How well do you know each other?"),
        ("Anniversary Prep", "Plan next anniversary celebration together"),
        ("Year in Review", "Celebrate growth and set new goals"),
    ]
    for i, (date_title, description) in enumerate(date_ideas):
        pages.append(("planner_page", f"Date #{i+1}: {date_title}",
            [f"Description: {description}",
             "Date planned for: ___/___/___",
             "Budget: $________",
             "What we need to prepare:",
             "What I loved about this date:",
             "What my spouse said they enjoyed:",
             "Rate this date: 1 2 3 4 5 6 7 8 9 10",
             "Would we do this again? YES / NO",
             "Notes & Memories:"]))
    return generate_etsy_book(407, "Etsy_Date_Night_Planner",
        "52 Date Nights for\nChristian Couples", "A Year of Intentional Romance & Connection", pages)



def book_408():
    """Marriage Communication Workbook"""
    pages = []
    pages.append(("section_title", "Communication\nWorkbook for Couples", "Biblical Tools for Better Conversations"))
    worksheets = [
        ("Communication Style Assessment", [
            "[HEADER]Identify Your Communication Style",
            "[BOX] I tend to avoid conflict at all costs",
            "[BOX] I express my feelings immediately (sometimes too quickly)",
            "[BOX] I shut down and go silent when upset",
            "[BOX] I use humor to deflect serious conversations",
            "[BOX] I listen fully before responding",
            "[BOX] I interrupt when I disagree",
            "[BOX] I bring up past issues during current conflicts",
            "[BOX] I express needs clearly and calmly",
            "[BOX] I use 'you always' or 'you never' statements",
            "[BOX] I apologize easily when wrong",
            "[LINE]My biggest communication strength:",
            "[LINE]My biggest communication weakness:",
            "[LINE]One thing I want to improve this month:",
        ]),
        ("Active Listening Practice", [
            "[HEADER]The HEAR Method",
            "[LINE]H - Halt: Stop what you are doing and give full attention",
            "[LINE]E - Empathize: Try to feel what your spouse feels",
            "[LINE]A - Attend: Use body language that shows you care",
            "[LINE]R - Respond: Summarize before giving your perspective",
            "",
            "[HEADER]Practice Exercise:",
            "[LINE]Topic my spouse shared:",
            "[LINE]What I heard them say (summarize):",
            "[LINE]The emotion behind their words:",
            "[LINE]My response after listening fully:",
            "[RATE]How well did I listen? (be honest)",
        ]),
        ("Conflict Resolution Template", [
            "[HEADER]When We Disagree - Fill This Out Together",
            "[LINE]The issue (state facts, not feelings):",
            "[LINE]How I FEEL about this issue:",
            "[LINE]What I NEED from my spouse:",
            "[LINE]What I am willing to COMPROMISE on:",
            "[LINE]What is NON-NEGOTIABLE for me:",
            "[LINE]A solution we BOTH can live with:",
            "[LINE]How we will CHECK IN on this issue:",
            "[BOX] We have prayed about this together",
            "[BOX] We both feel heard and understood",
            "[BOX] We agree on next steps",
        ]),
        ("Daily Check-In Template", [
            "[HEADER]10-Minute Daily Connection (use daily!)",
            "[LINE]Best part of my day:",
            "[LINE]Hardest part of my day:",
            "[LINE]Something I appreciated about you today:",
            "[LINE]Something on my mind for tomorrow:",
            "[LINE]One thing I need from you right now:",
            "[BOX] We prayed together today",
            "[RATE]My emotional connection level today:",
        ]),
    ]
    for ws_title, items in worksheets:
        pages.append(("worksheet", ws_title, items))
    # Repeat worksheets multiple times for ongoing use (Etsy customers love lots of pages)
    for week in range(1, 13):
        pages.append(("worksheet", f"Week {week} Daily Check-In (Mon-Sun)", [
            f"[HEADER]Week {week} - Daily Connection Log",
            "[LINE]Monday - Best moment:",
            "[LINE]Monday - Appreciation:",
            "[LINE]Tuesday - Best moment:",
            "[LINE]Tuesday - Appreciation:",
            "[LINE]Wednesday - Best moment:",
            "[LINE]Wednesday - Appreciation:",
            "[LINE]Thursday - Best moment:",
            "[LINE]Thursday - Appreciation:",
            "[LINE]Friday - Best moment:",
            "[LINE]Friday - Appreciation:",
            "[LINE]Saturday - Best moment:",
            "[LINE]Saturday - Appreciation:",
            "[LINE]Sunday - Best moment:",
            "[LINE]Sunday - Appreciation:",
            "[RATE]Overall connection this week:",
        ]))
    return generate_etsy_book(408, "Etsy_Communication_Workbook",
        "Communication Workbook\nfor Couples", "Biblical Tools for Better Conversations", pages)



def book_409():
    """Marriage Gratitude Journal"""
    pages = []
    pages.append(("section_title", "Marriage Gratitude\nJournal", "100 Days of Thankfulness for Your Spouse"))
    for day in range(1, 101):
        prompts = [
            f"Day {day} - Date: ___/___/___",
            f"Today I am grateful for my spouse because:",
            f"One thing they did today that blessed me:",
            f"A character trait I admire in them:",
            f"A memory with them that makes me smile:",
            f"My prayer of thanks for them today:",
        ]
        pages.append(("journal_page", f"Day {day} of 100", 
                      "Write what you are thankful for in your spouse today.", prompts))
    return generate_etsy_book(409, "Etsy_Gratitude_Journal",
        "Marriage Gratitude\nJournal", "100 Days of Thankfulness for Your Spouse", pages)

def book_410():
    """Weekly Marriage Planner"""
    pages = []
    pages.append(("section_title", "Weekly Marriage\nPlanner", "52 Weeks of Intentional Marriage Building"))
    for week in range(1, 53):
        pages.append(("planner_page", f"Week {week} Marriage Planner",
            ["This Week's Marriage Goal:",
             "Date Night Plans:",
             "Prayer Focus for Our Marriage:",
             "Scripture to Meditate On Together:",
             "Acts of Love I Will Do This Week:",
             "Conversation Topic to Discuss:",
             "Conflict to Resolve:",
             "Intimacy Goal:",
             "Gratitude - 3 Things I Love About My Spouse:",
             "Weekend Plans Together:",
             "Week Reflection - What Went Well:",
             "Next Week's Priority:"]))
    return generate_etsy_book(410, "Etsy_Weekly_Marriage_Planner",
        "Weekly Marriage\nPlanner", "52 Weeks of Intentional Marriage Building", pages)



def book_411():
    """Couples Bible Study Workbook"""
    pages = []
    pages.append(("section_title", "Couples Bible Study\nWorkbook", "12 Sessions on Marriage in Scripture"))
    studies = [
        ("Genesis 2:18-25", "God's Original Design", "The First Marriage"),
        ("Proverbs 31:10-31", "The Virtuous Spouse", "Character That Lasts"),
        ("Song of Solomon 2:1-17", "Celebrating Romantic Love", "Passion God's Way"),
        ("Ephesians 5:21-33", "Christ and the Church Model", "Sacrificial Love"),
        ("1 Corinthians 13:1-13", "The Love Chapter", "What Real Love Looks Like"),
        ("Colossians 3:12-19", "Clothing Yourself in Love", "Daily Love Choices"),
        ("1 Peter 3:1-12", "Instructions for Spouses", "Honor and Respect"),
        ("Matthew 19:1-12", "Jesus on Marriage", "What God Has Joined"),
        ("Ruth 1-4 (Summary)", "A Love Story of Faithfulness", "Covenant Loyalty"),
        ("Hosea 1-3 (Summary)", "Unconditional Love", "Love That Never Quits"),
        ("Malachi 2:13-16", "The Marriage Covenant", "God Hates Divorce"),
        ("Revelation 19:6-9", "The Marriage Supper", "Eternal Love Story"),
    ]
    for i, (passage, title, subtitle) in enumerate(studies):
        pages.append(("section_title", f"Session {i+1}: {title}", subtitle))
        pages.append(("scripture_page", passage, f"Read: {passage}"))
        pages.append(("worksheet", f"Study {i+1}: {title}", [
            f"[HEADER]Read {passage} together before starting",
            f"[LINE]What is the main theme of this passage?",
            f"[LINE]What does this passage teach about marriage?",
            f"[LINE]What surprised you in this passage?",
            f"[LINE]How does this apply to OUR marriage specifically?",
            f"[LINE]What is one change we can make based on this?",
            f"[RATE]How well are we living this out currently?",
            f"[BOX] We read the passage together",
            f"[BOX] We discussed honestly",
            f"[BOX] We prayed together about it",
            f"[BOX] We committed to one action step",
        ]))
        pages.append(("journal_page", f"Session {i+1} Reflections",
            "Write your personal response to this study.",
            ["What God spoke to me through this passage:",
             "What I want to tell my spouse about how I feel:",
             "One commitment I make based on this study:",
             "My prayer for our marriage after this session:"]))
    return generate_etsy_book(411, "Etsy_Bible_Study_Workbook",
        "Couples Bible Study\nWorkbook", "12 Scripture Sessions for Married Couples", pages)

def book_412():
    """Love Language Discovery Workbook"""
    pages = []
    pages.append(("section_title", "Love Language\nDiscovery Workbook", "Understanding How Your Spouse Feels Loved"))
    # Assessment pages
    pages.append(("worksheet", "Love Language Assessment - Spouse 1", [
        "[HEADER]For each pair, choose A or B (which you prefer RECEIVING):",
        "[BOX] A: A heartfelt compliment  OR  B: A long hug",
        "[BOX] A: A thoughtful gift  OR  B: Help with chores",
        "[BOX] A: Undivided attention  OR  B: Words of encouragement",
        "[BOX] A: A back rub  OR  B: A surprise present",
        "[BOX] A: Quality conversation  OR  B: An act of service",
        "[BOX] A: Being told 'I love you'  OR  B: Holding hands",
        "[BOX] A: A meaningful gift  OR  B: Full attention during conversation",
        "[BOX] A: Help without being asked  OR  B: Physical closeness",
        "[BOX] A: A love note  OR  B: Time alone together",
        "[BOX] A: An embrace  OR  B: A word of appreciation",
        "",
        "[LINE]My primary love language:",
        "[LINE]My secondary love language:",
        "[LINE]How I feel most loved (in my own words):",
    ]))
    pages.append(("worksheet", "Love Language Assessment - Spouse 2", [
        "[HEADER]For each pair, choose A or B (which you prefer RECEIVING):",
        "[BOX] A: A heartfelt compliment  OR  B: A long hug",
        "[BOX] A: A thoughtful gift  OR  B: Help with chores",
        "[BOX] A: Undivided attention  OR  B: Words of encouragement",
        "[BOX] A: A back rub  OR  B: A surprise present",
        "[BOX] A: Quality conversation  OR  B: An act of service",
        "[BOX] A: Being told 'I love you'  OR  B: Holding hands",
        "[BOX] A: A meaningful gift  OR  B: Full attention during conversation",
        "[BOX] A: Help without being asked  OR  B: Physical closeness",
        "[BOX] A: A love note  OR  B: Time alone together",
        "[BOX] A: An embrace  OR  B: A word of appreciation",
        "",
        "[LINE]My primary love language:",
        "[LINE]My secondary love language:",
        "[LINE]How I feel most loved (in my own words):",
    ]))
    # Weekly practice pages for each language
    languages = ["Words of Affirmation", "Quality Time", "Acts of Service", "Physical Touch", "Gift Giving"]
    for lang in languages:
        pages.append(("section_title", f"Practicing:\n{lang}", "Ideas and Tracking"))
        for week in range(1, 5):
            pages.append(("worksheet", f"{lang} - Week {week} Practice", [
                f"[HEADER]This week I will speak {lang} by:",
                f"[LINE]Monday action:",
                f"[LINE]Tuesday action:",
                f"[LINE]Wednesday action:",
                f"[LINE]Thursday action:",
                f"[LINE]Friday action:",
                f"[LINE]Saturday action:",
                f"[LINE]Sunday action:",
                f"[RATE]My spouse's response this week:",
                f"[LINE]What worked best:",
                f"[LINE]What I will continue:",
            ]))
    return generate_etsy_book(412, "Etsy_Love_Language_Workbook",
        "Love Language\nDiscovery Workbook", "Understanding How Your Spouse Feels Loved", pages)



def book_413():
    """Marriage Conflict Resolution Printable"""
    pages = []
    pages.append(("section_title", "Conflict Resolution\nPrintable Kit", "Biblical Tools for Fighting Fair"))
    # Conflict style assessment
    pages.append(("worksheet", "Your Conflict Style Assessment", [
        "[HEADER]Check all that apply to you during disagreements:",
        "[BOX] I raise my voice when frustrated",
        "[BOX] I withdraw and go silent",
        "[BOX] I cry easily during conflict",
        "[BOX] I bring up past offenses",
        "[BOX] I use sarcasm or mockery",
        "[BOX] I try to win the argument at all costs",
        "[BOX] I avoid confrontation entirely",
        "[BOX] I seek to understand before responding",
        "[BOX] I apologize quickly when wrong",
        "[BOX] I take breaks when emotions are high",
        "[BOX] I involve third parties (family/friends)",
        "[BOX] I use the silent treatment",
        "[LINE]My conflict style in one word:",
        "[LINE]My spouse's conflict style in one word:",
        "[LINE]Our biggest recurring conflict topic:",
    ]))
    # Conflict resolution worksheets (20 copies for repeated use)
    for i in range(1, 21):
        pages.append(("worksheet", f"Conflict Resolution Worksheet #{i}", [
            "[HEADER]Use this sheet during or after a disagreement",
            f"[LINE]Date: ___/___/___",
            "[LINE]The issue (facts only, no blame):",
            "[LINE]How I feel (use emotion words):",
            "[LINE]What I need from my spouse:",
            "[LINE]What triggered my reaction:",
            "[LINE]My part in this conflict (own it):",
            "[LINE]What I heard my spouse say they need:",
            "[LINE]A compromise we both accept:",
            "[BOX] We took a cool-down break if needed",
            "[BOX] We both feel heard",
            "[BOX] We prayed together about this",
            "[BOX] We forgave each other",
            "[LINE]Follow-up date to check on this: ___/___/___",
        ]))
    return generate_etsy_book(413, "Etsy_Conflict_Resolution_Kit",
        "Conflict Resolution\nPrintable Kit", "Biblical Tools for Fighting Fair in Marriage", pages)

def book_414():
    """Intimacy Building Workbook"""
    pages = []
    pages.append(("section_title", "Intimacy Building\nWorkbook", "Growing Closer in Every Way"))
    areas = [
        ("Spiritual Intimacy", [
            "How often do we pray together currently?",
            "What prevents us from consistent spiritual connection?",
            "Our shared spiritual goals for this season:",
            "A Scripture we will memorize together:",
            "How we will worship together this week:"]),
        ("Emotional Intimacy", [
            "On a scale of 1-10, how emotionally safe do I feel?",
            "What makes me feel emotionally connected to my spouse?",
            "A fear I have not shared with my spouse yet:",
            "A dream I want to share with my spouse:",
            "What 'emotional safety' looks like to me:"]),
        ("Intellectual Intimacy", [
            "Topics we enjoy discussing together:",
            "A book we could read together:",
            "Something new I want to learn with my spouse:",
            "How we stimulate each other's minds:",
            "A debate topic we can enjoy exploring:"]),
        ("Recreational Intimacy", [
            "Activities we both enjoy:",
            "Something my spouse loves that I could try:",
            "A new hobby we could start together:",
            "Our ideal weekend together looks like:",
            "An adventure we want to take this year:"]),
        ("Physical Intimacy", [
            "Non-sexual touch I most appreciate:",
            "How I feel about our current physical connection:",
            "What makes me feel desired by my spouse:",
            "Barriers to physical closeness right now:",
            "How we can prioritize physical connection:"]),
    ]
    for area_name, prompts in areas:
        pages.append(("section_title", area_name, "Growing deeper together"))
        for week in range(1, 5):
            pages.append(("journal_page", f"{area_name} - Week {week}",
                f"Reflect on your {area_name.lower()} this week.", prompts))
        pages.append(("worksheet", f"{area_name} - Action Plan", [
            f"[HEADER]{area_name} Growth Plan",
            f"[RATE]Current satisfaction level:",
            f"[LINE]One thing we do well in this area:",
            f"[LINE]One thing we need to improve:",
            f"[LINE]Specific action for this week:",
            f"[LINE]How we will hold each other accountable:",
            f"[BOX] We discussed this openly and honestly",
            f"[BOX] We both committed to growth",
        ]))
    return generate_etsy_book(414, "Etsy_Intimacy_Workbook",
        "Intimacy Building\nWorkbook", "Growing Closer in Every Dimension", pages)



def book_415():
    """Marriage Budget Planner - Biblical Finances"""
    pages = []
    pages.append(("section_title", "Biblical Marriage\nBudget Planner", "Managing God's Resources Together"))
    # Monthly budget sheets x12
    for month in ["January","February","March","April","May","June",
                  "July","August","September","October","November","December"]:
        pages.append(("planner_page", f"{month} Budget",
            [f"Month: {month}  Year: _______",
             "INCOME:",
             "  Spouse 1 Income: $________",
             "  Spouse 2 Income: $________",
             "  Other Income: $________",
             "  TOTAL INCOME: $________",
             "GIVING:",
             "  Tithe (10%): $________",
             "  Offerings: $________",
             "  Charity: $________",
             "EXPENSES:",
             "  Housing/Rent: $________",
             "  Utilities: $________",
             "  Food/Groceries: $________",
             "  Transportation: $________",
             "  Insurance: $________",
             "  Debt Payments: $________",
             "  Savings: $________",
             "  Fun Money (Spouse 1): $________",
             "  Fun Money (Spouse 2): $________",
             "  Date Nights: $________",
             "  Miscellaneous: $________",
             "  TOTAL EXPENSES: $________",
             "SURPLUS/DEFICIT: $________",
             "Prayer over our finances this month:"]))
    # Debt tracker
    pages.append(("worksheet", "Debt Freedom Tracker", [
        "[HEADER]Proverbs 22:7 - The borrower is servant to the lender",
        "[LINE]Debt 1: _______ Balance: $_____ Min Payment: $_____",
        "[LINE]Debt 2: _______ Balance: $_____ Min Payment: $_____",
        "[LINE]Debt 3: _______ Balance: $_____ Min Payment: $_____",
        "[LINE]Debt 4: _______ Balance: $_____ Min Payment: $_____",
        "[LINE]Debt 5: _______ Balance: $_____ Min Payment: $_____",
        "[LINE]Total Debt: $_________",
        "[LINE]Target debt-free date: ___/___/___",
        "[LINE]Our debt-free celebration plan:",
        "[BOX] We agree to add no new debt",
        "[BOX] We will attack smallest debt first",
    ]))
    # Savings goals
    pages.append(("worksheet", "Savings Goals Together", [
        "[HEADER]Building Financial Security God's Way",
        "[LINE]Emergency Fund Goal: $________ Current: $________",
        "[LINE]Vacation Fund: $________ Current: $________",
        "[LINE]Children's Education: $________ Current: $________",
        "[LINE]Retirement: $________ Current: $________",
        "[LINE]Home Purchase/Improvement: $________ Current: $________",
        "[LINE]Generosity Fund: $________ Current: $________",
        "[RATE]Our financial unity level:",
        "[LINE]Our #1 financial goal this year:",
    ]))
    # Giving tracker
    for q in range(1, 5):
        pages.append(("worksheet", f"Quarter {q} Giving Tracker", [
            f"[HEADER]Quarter {q} - Faithful Stewardship Log",
            "[LINE]Month 1 Tithe: $_______ Date: ___",
            "[LINE]Month 1 Offering: $_______ Date: ___",
            "[LINE]Month 2 Tithe: $_______ Date: ___",
            "[LINE]Month 2 Offering: $_______ Date: ___",
            "[LINE]Month 3 Tithe: $_______ Date: ___",
            "[LINE]Month 3 Offering: $_______ Date: ___",
            "[LINE]Total Given This Quarter: $________",
            "[LINE]How we saw God provide this quarter:",
            "[BOX] We were faithful in tithing",
        ]))
    return generate_etsy_book(415, "Etsy_Budget_Planner",
        "Biblical Marriage\nBudget Planner", "Managing God's Resources as One", pages)

def book_416():
    """Morning Devotional Printable - 90 Days"""
    pages = []
    pages.append(("section_title", "90-Day Marriage\nMorning Devotional", "Start Each Day United in God's Word"))
    verses_90 = [
        "Genesis 2:24","Proverbs 3:5-6","1 Corinthians 13:4","Ephesians 5:25","Colossians 3:14",
        "1 Peter 4:8","Proverbs 18:22","Ecclesiastes 4:9-10","Song of Solomon 8:7","Mark 10:9",
        "Philippians 2:3-4","Romans 12:10","1 John 4:19","Proverbs 31:10","Hebrews 13:4",
        "Galatians 5:22-23","James 1:19","Ephesians 4:32","1 Corinthians 7:3","Proverbs 15:1",
        "Romans 15:5-7","Colossians 3:12-13","1 Thessalonians 5:11","Proverbs 12:4","Matthew 19:6",
        "2 Corinthians 6:14","Ruth 1:16-17","Proverbs 21:9","Psalm 127:1","Ephesians 4:2-3",
        "1 Peter 3:7","Proverbs 31:28","Song of Solomon 2:16","Matthew 18:21-22","Romans 12:12",
        "Galatians 6:2","Proverbs 27:17","1 Corinthians 16:14","Philippians 4:6-7","Psalm 34:3",
        "Proverbs 19:14","Ecclesiastes 4:12","1 John 4:7-8","Colossians 3:19","1 Peter 3:1-2",
        "Proverbs 5:18-19","Romans 8:28","Ephesians 5:21","Matthew 7:12","Psalm 128:1-4",
        "Proverbs 14:1","1 Corinthians 13:7","Song of Solomon 4:7","Hebrews 10:24","James 5:16",
        "Proverbs 17:17","Romans 13:8","Ephesians 4:15","1 Peter 4:10","Psalm 133:1",
        "Proverbs 22:6","1 Corinthians 11:11","Colossians 3:23","Matthew 6:33","Psalm 37:4",
        "Proverbs 3:3-4","Romans 12:18","Ephesians 5:33","1 John 3:18","Psalm 100:2",
        "Proverbs 16:3","1 Corinthians 13:13","Song of Solomon 2:10","Hebrews 12:1","James 1:5",
        "Proverbs 4:23","Romans 5:3-5","Ephesians 3:20","1 Peter 5:7","Psalm 46:1",
        "Proverbs 11:25","1 Corinthians 10:13","Colossians 2:2","Matthew 5:9","Psalm 91:1-2",
        "Proverbs 31:30","Romans 8:31","Ephesians 6:10-11","1 John 4:18","Psalm 23:1-3",
    ]
    for day in range(1, 91):
        verse = verses_90[(day-1) % len(verses_90)]
        pages.append(("prayer_page", f"Day {day} - {verse}",
            f"Read {verse} together this morning.",
            [f"What this verse means for our marriage today:",
             "How I will apply this today:",
             "My prayer for my spouse today:",
             "My prayer for our marriage today:",
             "One word to carry with me all day:"]))
    return generate_etsy_book(416, "Etsy_Morning_Devotional",
        "90-Day Marriage\nMorning Devotional", "Start Each Day United in God's Word", pages)



def book_417():
    """Marriage Conversation Starters - 200 Questions"""
    pages = []
    pages.append(("section_title", "200 Conversation\nStarters for Couples", "Deep Questions to Know Each Other Better"))
    categories = [
        ("Spiritual Life", [
            "What is God teaching you right now?",
            "When did you feel closest to God recently?",
            "What Scripture has been on your heart lately?",
            "How can I pray for you this week?",
            "What does your ideal spiritual life look like?",
            "Is there a sin you are struggling with that I can support you in?",
            "What spiritual discipline do you want to grow in?",
            "How do you experience God's love most clearly?",
        ]),
        ("Dreams & Goals", [
            "Where do you see us in 5 years?",
            "What is a dream you have never told me?",
            "If money were no object what would we do?",
            "What legacy do you want to leave?",
            "What skill do you want to develop?",
            "What adventure is on your bucket list?",
            "How can I better support your dreams?",
            "What goal scares you but excites you?",
        ]),
        ("Emotional Connection", [
            "When do you feel most loved by me?",
            "What is your happiest memory of us?",
            "What do you need from me right now?",
            "When do you feel safest with me?",
            "What is something I do that hurts you unintentionally?",
            "How can I be a better listener for you?",
            "What emotion is hardest for you to express?",
            "When did you last feel truly seen by me?",
        ]),
        ("Fun & Light", [
            "What is your favorite thing about our home?",
            "If we could travel anywhere tomorrow where?",
            "What is the funniest memory from our marriage?",
            "What song reminds you of us?",
            "What is your love language this season?",
            "What is the best meal I ever made for you?",
            "What Netflix show should we watch next?",
            "What is something silly that makes you happy?",
        ]),
        ("Hard Questions", [
            "Is there anything unresolved between us?",
            "What do you wish I would change?",
            "Are there boundaries we need to set?",
            "How is our intimacy - honestly?",
            "Do you feel respected by me?",
            "Is there anything you are afraid to tell me?",
            "How are we doing with money - truly?",
            "What keeps you up at night about us?",
        ]),
    ]
    for cat_name, questions in categories:
        pages.append(("section_title", cat_name, "Conversation Starters"))
        for i in range(0, len(questions), 2):
            batch = questions[i:i+2]
            items = []
            for q in batch:
                items.extend([f"[LINE]{q}", ""])
            items.append("[LINE]Notes from our conversation:")
            items.append("[LINE]Follow-up needed?")
            pages.append(("worksheet", f"{cat_name} Questions", items))
    # Bonus: monthly check-in pages
    for m in range(1, 13):
        pages.append(("worksheet", f"Monthly Check-In #{m}", [
            f"[HEADER]Month {m} Marriage Check-In",
            "[RATE]Overall happiness this month:",
            "[RATE]Communication quality:",
            "[RATE]Spiritual connection:",
            "[RATE]Physical intimacy:",
            "[RATE]Fun and friendship:",
            "[LINE]Best moment this month:",
            "[LINE]Hardest moment this month:",
            "[LINE]One thing to improve next month:",
            "[BOX] We had at least 2 date nights",
            "[BOX] We prayed together regularly",
            "[BOX] We resolved conflicts quickly",
        ]))
    return generate_etsy_book(417, "Etsy_Conversation_Starters",
        "200 Conversation\nStarters for Couples", "Deep Questions for Christian Marriages", pages)

def book_418():
    """Marriage Goals Planner - Annual"""
    pages = []
    pages.append(("section_title", "Annual Marriage\nGoals Planner", "Setting & Achieving Goals as One"))
    # Vision casting
    pages.append(("journal_page", "Our Marriage Vision Statement",
        "Create your shared vision for this year and beyond.",
        ["Our marriage mission statement:",
         "3 words that describe the marriage we want:",
         "What we want people to say about our marriage:",
         "Our 'win' for this year as a couple:",
         "One Bible verse that defines our marriage vision:"]))
    # Goal areas
    areas = ["Spiritual Growth", "Communication", "Intimacy & Romance",
             "Finances", "Parenting", "Health & Wellness",
             "Social Life & Friendships", "Career & Purpose",
             "Home & Environment", "Fun & Adventure"]
    for area in areas:
        pages.append(("worksheet", f"Goal Setting: {area}", [
            f"[HEADER]{area} Goals",
            f"[RATE]Current satisfaction (1-10):",
            f"[LINE]Where we are now:",
            f"[LINE]Where we want to be by year end:",
            f"[LINE]Goal #1 (specific & measurable):",
            f"[LINE]Goal #2 (specific & measurable):",
            f"[LINE]Action steps for Goal #1:",
            f"[LINE]Action steps for Goal #2:",
            f"[LINE]Potential obstacles:",
            f"[LINE]How we will overcome them:",
            f"[LINE]Check-in date: ___/___/___",
            f"[BOX] We both agree on these goals",
        ]))
    # Quarterly reviews
    for q in range(1, 5):
        pages.append(("worksheet", f"Quarter {q} Review", [
            f"[HEADER]Quarter {q} Marriage Review",
            "[RATE]Overall progress on goals:",
            "[LINE]Goals we achieved:",
            "[LINE]Goals we are behind on:",
            "[LINE]What worked well:",
            "[LINE]What needs to change:",
            "[LINE]Biggest win this quarter:",
            "[LINE]Biggest challenge this quarter:",
            "[LINE]Adjusted goals for next quarter:",
            "[BOX] We celebrated our progress together",
        ]))
    # Monthly trackers
    for m in range(1, 13):
        pages.append(("checklist", f"Month {m} Habit Tracker", [
            "Prayed together daily",
            "Had date night (at least 2x)",
            "Read Scripture together",
            "Expressed gratitude daily",
            "Resolved conflicts same day",
            "Physical affection daily",
            "Budget review completed",
            "Served each other intentionally",
            "Encouraged each other verbally",
            "Attended church together",
            "Had fun together (laughed!)",
            "Discussed goals/dreams",
        ]))
    return generate_etsy_book(418, "Etsy_Marriage_Goals_Planner",
        "Annual Marriage\nGoals Planner", "Setting & Achieving Goals Together as One", pages)



def book_419():
    """Forgiveness Workbook for Couples"""
    pages = []
    pages.append(("section_title", "Forgiveness Workbook\nfor Couples", "A Biblical Path to Freedom & Healing"))
    # Assessment
    pages.append(("worksheet", "Forgiveness Self-Assessment", [
        "[HEADER]Answer honestly - no judgment",
        "[BOX] I am holding onto resentment toward my spouse",
        "[BOX] There are past offenses I bring up during arguments",
        "[BOX] I struggle to trust my spouse due to past hurts",
        "[BOX] I feel bitter when I think about certain events",
        "[BOX] I have forgiven with words but not in my heart",
        "[BOX] I use past failures as weapons",
        "[BOX] I compare my spouse to others negatively",
        "[BOX] I struggle to believe my spouse has changed",
        "[BOX] I have not fully confessed my own offenses",
        "[BOX] I avoid certain topics because of unhealed wounds",
        "[RATE]My current level of forgiveness toward my spouse:",
        "[LINE]The offense that is hardest to release:",
    ]))
    # 12 forgiveness exercises
    for i in range(1, 13):
        pages.append(("journal_page", f"Forgiveness Exercise #{i}",
            "Work through this honestly. Take your time.",
            [f"The offense/hurt I am processing today:",
             "How this made me FEEL (name the emotions):",
             "How this affected my trust:",
             "What I wish had happened instead:",
             "Can I choose to release this today? YES / NOT YET",
             "If not yet - what do I need first?",
             "My prayer releasing this to God:",
             "A Scripture to replace this pain:"]))
    # Rebuilding trust worksheets
    for week in range(1, 9):
        pages.append(("worksheet", f"Rebuilding Trust - Week {week}", [
            f"[HEADER]Week {week} Trust Assessment",
            f"[RATE]Trust level this week (1-10):",
            f"[LINE]Evidence of changed behavior I noticed:",
            f"[LINE]A trigger that came up this week:",
            f"[LINE]How I handled the trigger:",
            f"[LINE]What my spouse did to rebuild trust:",
            f"[LINE]What I still need from my spouse:",
            f"[BOX] I chose forgiveness today even when I didn't feel it",
            f"[BOX] We talked openly about the healing process",
        ]))
    return generate_etsy_book(419, "Etsy_Forgiveness_Workbook",
        "Forgiveness Workbook\nfor Couples", "A Biblical Path to Freedom & Healing", pages)

def book_420():
    """Scripture Memory Cards for Marriage"""
    pages = []
    pages.append(("section_title", "52 Scripture Memory\nCards for Marriage", "One Verse Per Week for Your Marriage"))
    verses = [
        ("Genesis 2:24", "Therefore shall a man leave his father and mother, and cleave unto his wife."),
        ("Proverbs 3:5-6", "Trust in the LORD with all thine heart; lean not unto thine own understanding."),
        ("1 Corinthians 13:4", "Love is patient, love is kind. It does not envy, it does not boast."),
        ("Ephesians 5:25", "Husbands, love your wives, even as Christ loved the church."),
        ("Colossians 3:14", "Above all these things put on love, which is the bond of perfectness."),
        ("1 Peter 4:8", "Above all things have fervent love among yourselves."),
        ("Ecclesiastes 4:9", "Two are better than one; they have a good reward for their labour."),
        ("Proverbs 18:22", "Whoso findeth a wife findeth a good thing."),
        ("Mark 10:9", "What God hath joined together, let not man put asunder."),
        ("Ephesians 4:32", "Be ye kind one to another, tenderhearted, forgiving one another."),
        ("Song of Solomon 8:7", "Many waters cannot quench love, neither can the floods drown it."),
        ("Romans 12:10", "Be kindly affectioned one to another with brotherly love."),
        ("1 John 4:19", "We love him, because he first loved us."),
        ("Philippians 2:3", "In lowliness of mind let each esteem other better than themselves."),
        ("Hebrews 13:4", "Marriage is honourable in all, and the bed undefiled."),
        ("Proverbs 31:10", "Who can find a virtuous woman? Her price is far above rubies."),
        ("James 1:19", "Be swift to hear, slow to speak, slow to wrath."),
        ("Galatians 5:22", "The fruit of the Spirit is love, joy, peace, longsuffering."),
        ("1 Corinthians 7:3", "Let the husband render unto the wife due benevolence."),
        ("Proverbs 15:1", "A soft answer turneth away wrath."),
        ("Romans 15:7", "Receive ye one another, as Christ also received us."),
        ("Colossians 3:13", "Forbearing one another, and forgiving one another."),
        ("1 Thessalonians 5:11", "Comfort yourselves together, and edify one another."),
        ("Matthew 19:6", "They are no more twain, but one flesh."),
        ("Psalm 127:1", "Except the LORD build the house, they labour in vain."),
        ("Ephesians 4:2", "With all lowliness and meekness, with longsuffering."),
        ("1 Peter 3:7", "Giving honour unto the wife, as unto the weaker vessel."),
        ("Song of Solomon 2:16", "My beloved is mine, and I am his."),
        ("Matthew 18:22", "I say not unto thee seven times, but seventy times seven."),
        ("Romans 12:12", "Rejoicing in hope; patient in tribulation."),
        ("Galatians 6:2", "Bear ye one another's burdens."),
        ("Proverbs 27:17", "Iron sharpeneth iron; so a man sharpeneth his friend."),
        ("1 Corinthians 16:14", "Let all your things be done with love."),
        ("Philippians 4:6", "Be careful for nothing; but in prayer let your requests be known."),
        ("Psalm 34:3", "O magnify the LORD with me, and let us exalt his name together."),
        ("Ecclesiastes 4:12", "A threefold cord is not quickly broken."),
        ("1 John 4:7", "Let us love one another: for love is of God."),
        ("Romans 8:28", "All things work together for good to them that love God."),
        ("Ephesians 5:21", "Submitting yourselves one to another in the fear of God."),
        ("Matthew 7:12", "All things whatsoever ye would that men do to you, do ye to them."),
        ("Psalm 128:1", "Blessed is every one that feareth the LORD; that walketh in his ways."),
        ("Proverbs 14:1", "Every wise woman buildeth her house."),
        ("1 Corinthians 13:7", "Love beareth all things, believeth all, hopeth all, endureth all."),
        ("Hebrews 10:24", "Let us consider one another to provoke unto love and good works."),
        ("James 5:16", "Pray one for another, that ye may be healed."),
        ("Romans 13:8", "Owe no man any thing, but to love one another."),
        ("Ephesians 4:15", "Speaking the truth in love, may grow up into him."),
        ("1 Peter 4:10", "Minister the same one to another, as good stewards."),
        ("Psalm 133:1", "How good and how pleasant for brethren to dwell together in unity!"),
        ("Proverbs 16:3", "Commit thy works unto the LORD, and thy thoughts shall be established."),
        ("1 Corinthians 13:13", "Now abideth faith, hope, love, these three; the greatest is love."),
        ("Ephesians 3:20", "Unto him that is able to do exceeding abundantly above all we ask."),
    ]
    for i, (ref, text) in enumerate(verses):
        pages.append(("scripture_page", text, f"- {ref} (Week {i+1})"))
    return generate_etsy_book(420, "Etsy_Scripture_Memory_Cards",
        "52 Scripture Memory\nCards for Marriage", "One Verse Per Week to Transform Your Union", pages)



def book_421():
    """Marriage Retreat at Home Kit"""
    pages = []
    pages.append(("section_title", "Marriage Retreat\nat Home", "A Weekend Getaway Without Leaving"))
    sessions = [
        ("Friday Evening: Reconnecting", [
            "Put away all devices for the weekend",
            "Light candles and play worship music",
            "Share: What has been weighing on your heart?",
            "Share: What are you grateful for about us?",
            "Pray together to open your retreat",
            "Read Song of Solomon 2:10-13 together"]),
        ("Saturday Morning: The State of Our Union", [
            "Rate your marriage in these areas (1-10):",
            "  Communication / Intimacy / Finances",
            "  Parenting / Spiritual Life / Fun",
            "What is our biggest win this year?",
            "What is our biggest challenge right now?",
            "Where do we want to be in 1 year?"]),
        ("Saturday Afternoon: Healing & Forgiveness", [
            "Is there anything unresolved between us?",
            "Are there hurts we have not processed?",
            "Write a 'release letter' (things you are letting go)",
            "Read Colossians 3:12-14 together",
            "Pray and verbally release each offense",
            "Hug for 60 seconds in silence"]),
        ("Saturday Evening: Romance & Intimacy", [
            "Take turns sharing what makes you feel desired",
            "Share your favorite physical memory together",
            "Discuss: How is our intimacy? What do we need?",
            "Plan your next 3 date nights right now",
            "Read Song of Solomon 4:1-7",
            "Enjoy a candlelit dinner together"]),
        ("Sunday Morning: Vision & Covenant", [
            "Write your marriage vision for the next year",
            "Create 3 shared goals with deadlines",
            "Write a renewed covenant statement",
            "Read Ephesians 3:20 - God can do MORE",
            "Pray and declare your vision over your marriage",
            "Celebrate with communion (bread and juice)"]),
    ]
    for session_title, activities in sessions:
        pages.append(("section_title", session_title, "Marriage Retreat at Home"))
        pages.append(("checklist", f"Checklist: {session_title}", activities))
        pages.append(("journal_page", f"Reflections: {session_title}",
            "Journal your thoughts from this session.",
            ["What God revealed to me:",
             "What I want to tell my spouse:",
             "My commitment from this session:",
             "My prayer:"]))
    # Bonus planning pages
    for i in range(1, 5):
        pages.append(("planner_page", f"Quarterly Mini-Retreat #{i}",
            ["Date: ___/___/___",
             "Location (home, hotel, park):",
             "Theme for this retreat:",
             "Scripture focus:",
             "What we will discuss:",
             "What we will do for fun:",
             "One goal to set:",
             "How we will celebrate:"]))
    return generate_etsy_book(421, "Etsy_Marriage_Retreat_Kit",
        "Marriage Retreat\nat Home", "A Weekend Getaway Without Leaving Your House", pages)

def book_422():
    """Newlywed First Year Journal"""
    pages = []
    pages.append(("section_title", "Our First Year\nJournal", "Documenting 12 Months of Marriage"))
    for month in range(1, 13):
        month_names = ["","January","February","March","April","May","June",
                       "July","August","September","October","November","December"]
        pages.append(("section_title", f"Month {month}", month_names[month]))
        pages.append(("journal_page", f"Month {month} Reflections",
            f"Document your marriage in month {month}.",
            [f"How we are adjusting to married life:",
             "Best moment this month:",
             "Hardest moment this month:",
             "What we learned about each other:",
             "How we grew closer to God together:",
             "A funny memory from this month:"]))
        pages.append(("worksheet", f"Month {month} Check-In", [
            f"[HEADER]Month {month} Marriage Assessment",
            "[RATE]Communication quality:",
            "[RATE]Physical intimacy satisfaction:",
            "[RATE]Spiritual connection:",
            "[RATE]Conflict resolution:",
            "[RATE]Fun and laughter together:",
            "[LINE]One thing we do well:",
            "[LINE]One thing to work on:",
            "[LINE]Date night we had this month:",
            "[BOX] We prayed together regularly",
            "[BOX] We attended church together",
            "[BOX] We discussed our budget",
        ]))
        pages.append(("prayer_page", f"Month {month} Prayer",
            "Pray for your marriage this month.",
            ["Thank God for your spouse:",
             "Ask for wisdom in:",
             "Pray for your future together:",
             "Release any frustration about:"]))
    return generate_etsy_book(422, "Etsy_Newlywed_Journal",
        "Our First Year\nJournal", "Documenting 12 Months of Newlywed Life", pages)



def book_423():
    """Marriage Counseling Self-Guided Workbook"""
    pages = []
    pages.append(("section_title", "Self-Guided Marriage\nCounseling Workbook", "8 Sessions You Can Do at Home"))
    sessions = [
        ("Session 1: Where Are We?", "Overall assessment"),
        ("Session 2: Communication Patterns", "How we talk (and don't)"),
        ("Session 3: Unresolved Hurts", "The elephant in the room"),
        ("Session 4: Expectations vs Reality", "What we expected vs what we got"),
        ("Session 5: Intimacy Check", "Physical, emotional, spiritual"),
        ("Session 6: Money & Stress", "Financial health check"),
        ("Session 7: Family & Boundaries", "In-laws, children, friends"),
        ("Session 8: Future Vision", "Where do we go from here?"),
    ]
    for sess_num, (sess_title, sess_desc) in enumerate(sessions, 1):
        pages.append(("section_title", sess_title, sess_desc))
        # Pre-session individual worksheet
        pages.append(("worksheet", f"{sess_title} - Individual Assessment (Spouse 1)", [
            f"[HEADER]Complete ALONE before discussing together",
            f"[RATE]Satisfaction in this area currently:",
            f"[LINE]How I honestly feel about this area:",
            f"[LINE]What I wish my spouse understood:",
            f"[LINE]My part in the problem (be honest):",
            f"[LINE]What I need from my spouse:",
            f"[LINE]What I am willing to do differently:",
            f"[LINE]A Scripture that speaks to me here:",
        ]))
        pages.append(("worksheet", f"{sess_title} - Individual Assessment (Spouse 2)", [
            f"[HEADER]Complete ALONE before discussing together",
            f"[RATE]Satisfaction in this area currently:",
            f"[LINE]How I honestly feel about this area:",
            f"[LINE]What I wish my spouse understood:",
            f"[LINE]My part in the problem (be honest):",
            f"[LINE]What I need from my spouse:",
            f"[LINE]What I am willing to do differently:",
            f"[LINE]A Scripture that speaks to me here:",
        ]))
        # Together discussion
        pages.append(("worksheet", f"{sess_title} - Together Discussion", [
            f"[HEADER]Discuss your individual answers together",
            f"[LINE]What surprised us about each other's answers:",
            f"[LINE]Where we agree:",
            f"[LINE]Where we differ:",
            f"[LINE]A compromise or solution:",
            f"[LINE]Our action step this week:",
            f"[LINE]Check-in date: ___/___/___",
            f"[BOX] We both feel heard",
            f"[BOX] We prayed together about this",
            f"[BOX] We committed to our action step",
        ]))
        pages.append(("prayer_page", f"{sess_title} - Prayer",
            "Close this session in prayer together.",
            ["Praise God for your marriage:",
             "Confess where you have fallen short:",
             "Ask for help in this specific area:",
             "Declare God's promises over your marriage:"]))
    return generate_etsy_book(423, "Etsy_Counseling_Workbook",
        "Self-Guided Marriage\nCounseling Workbook", "8 Sessions You Can Do at Home Together", pages)

def book_424():
    """Anniversary Celebration Planner"""
    pages = []
    pages.append(("section_title", "Anniversary\nCelebration Planner", "Making Every Year Memorable"))
    # Annual pages for 25 years
    for year in range(1, 26):
        traditional = {1:"Paper",2:"Cotton",3:"Leather",4:"Fruit/Flowers",5:"Wood",
                      6:"Candy/Iron",7:"Wool/Copper",8:"Pottery",9:"Willow",10:"Tin/Aluminum",
                      11:"Steel",12:"Silk/Linen",13:"Lace",14:"Ivory",15:"Crystal",
                      16:"Wax",17:"Furniture",18:"Porcelain",19:"Bronze",20:"China",
                      21:"Brass",22:"Copper",23:"Silver Plate",24:"Musical",25:"Silver"}
        gift_theme = traditional.get(year, "Love")
        pages.append(("planner_page", f"Year {year} Anniversary ({gift_theme})",
            [f"Anniversary #{year} - Traditional Gift: {gift_theme}",
             "Date: ___/___/___",
             "Gift Ideas for My Spouse:",
             "How We Will Celebrate:",
             "Budget: $________",
             "Special Memory from This Year:",
             "What I Love Most About My Spouse This Year:",
             "Our Biggest Achievement as a Couple:",
             "One Challenge We Overcame Together:",
             "Our Goal for Next Year:",
             "A Love Note to My Spouse:"]))
    # Vow renewal planning
    pages.append(("section_title", "Vow Renewal\nPlanning", "For a Special Anniversary"))
    pages.append(("planner_page", "Vow Renewal Ceremony Plan", [
        "Date: ___/___/___",
        "Location:",
        "Guest List (or just us?):",
        "Officiant:",
        "What We Will Wear:",
        "Flowers/Decorations:",
        "Music Selections:",
        "Scripture Reading:",
        "Who Will Speak/Pray:",
        "Reception/Dinner Plans:",
        "Photography:",
        "Budget: $________",
        "Our Renewed Vows (draft here):"]))
    # Love letter templates
    for i in range(1, 11):
        pages.append(("journal_page", f"Love Letter #{i}",
            "Write a love letter to your spouse for any anniversary.",
            ["Dear ______,",
             "What I remember about the day we met:",
             "What I love about who you have become:",
             "My favorite memory from this year:",
             "What I promise you for our future:",
             "Forever yours,"]))
    return generate_etsy_book(424, "Etsy_Anniversary_Planner",
        "Anniversary\nCelebration Planner", "Making Every Year Memorable Together", pages)

def book_425():
    """Marriage Emergency Kit - Crisis Printable"""
    pages = []
    pages.append(("section_title", "Marriage Emergency\nKit", "When Everything Falls Apart - Start Here"))
    # Crisis triage
    pages.append(("worksheet", "CRISIS TRIAGE - Where Are You?", [
        "[HEADER]Check all that apply right now:",
        "[BOX] We are barely speaking",
        "[BOX] One or both of us has mentioned divorce",
        "[BOX] There has been infidelity (emotional or physical)",
        "[BOX] There is addiction involved",
        "[BOX] There is a financial crisis",
        "[BOX] One of us wants to leave",
        "[BOX] We have lost all intimacy",
        "[BOX] There is verbal/emotional abuse present",
        "[BOX] We are living like roommates",
        "[BOX] We cannot agree on anything",
        "[BOX] Extended family is causing division",
        "[BOX] One of us has checked out emotionally",
        "",
        "[HEADER]IMPORTANT: If there is physical abuse, seek safety FIRST.",
        "[LINE]National Domestic Violence Hotline: 1-800-799-7233",
    ]))
    # Emergency protocols
    emergencies = [
        ("When You Cannot Stop Fighting", [
            "STOP. Take 30 minutes apart (set a timer).",
            "Each person: Write down what you NEED (not what you are angry about).",
            "Come back together. Read your needs to each other WITHOUT interrupting.",
            "Find ONE thing you can both agree on. Start there.",
            "Pray together even if it is one sentence each.",
            "If you cannot resolve it: agree to pause and revisit in 24 hours.",
            "Seek pastoral counseling if this pattern repeats weekly.",
        ]),
        ("When Trust Is Broken", [
            "The offending spouse must take FULL ownership. No excuses.",
            "The hurt spouse has the right to ask questions. Answer honestly.",
            "Commit to TOTAL transparency (passwords, locations, schedules).",
            "Find a Christian counselor immediately. Do not try to heal alone.",
            "Set a rebuilding timeline (trust takes 12-24 months minimum).",
            "The offending spouse must demonstrate CONSISTENT changed behavior.",
            "Both must agree: bringing it up as a weapon is off-limits.",
        ]),
        ("When You Feel Like Giving Up", [
            "Remember: feelings are not facts. Hopelessness is a feeling, not reality.",
            "Read Jeremiah 29:11 - God has plans for your future.",
            "Call a trusted pastor, mentor, or Christian friend TODAY.",
            "Write down 10 reasons you married your spouse (from memory).",
            "Commit to 30 more days before making any permanent decision.",
            "Remove the word 'divorce' from your vocabulary this month.",
            "Ask God to give you supernatural love beyond your own ability.",
        ]),
        ("When Communication Has Broken Down", [
            "Start with WRITING instead of talking. Write a letter.",
            "Keep it to 'I feel...' statements only. No accusations.",
            "Request one 15-minute conversation with ground rules.",
            "Ground rules: No interrupting. No yelling. No name-calling.",
            "Use a timer: 5 min for person A, 5 min for person B, 5 min together.",
            "If it works - schedule this weekly until you rebuild the habit.",
            "Consider a communication-focused couples retreat.",
        ]),
    ]
    for title, steps in emergencies:
        pages.append(("section_title", title, "Emergency Protocol"))
        pages.append(("checklist", f"Action Steps: {title}", steps))
        pages.append(("journal_page", f"Processing: {title}",
            "Use this space to process your emotions honestly.",
            ["What I am feeling right now:",
             "What I am afraid of:",
             "What I actually need from my spouse:",
             "What I am willing to do differently:",
             "My honest prayer to God right now:"]))
    # 30-day rescue plan
    for day in range(1, 31):
        actions = [
            "Pray for your spouse (even 1 minute)",
            "Say one kind thing to them",
            "Do one act of service without being asked",
            "Touch them gently (hand on shoulder, brief hug)",
            "Send a text with something you appreciate",
            "Listen without giving advice or defending",
            "Apologize for one thing (even small)",
        ]
        action = actions[(day-1) % len(actions)]
        pages.append(("checklist", f"Day {day} Rescue Action", [
            f"Today's action: {action}",
            "Did I do it? YES / NO",
            "How did my spouse respond?",
            "How did I feel?",
            "Tomorrow I will also try to:",
        ]))
    return generate_etsy_book(425, "Etsy_Marriage_Emergency_Kit",
        "Marriage Emergency\nKit", "When Everything Falls Apart - Start Here", pages)



# ============================================================
# MAIN EXECUTION
# ============================================================
def generate_all():
    print("=" * 70)
    print("GENERATING 20 ETSY BIBLICAL MARRIAGE PDFs (406-425)")
    print("Format: 8.5x11 Printable Digital Downloads")
    print("=" * 70)
    print()
    
    results = []
    books = [book_406, book_407, book_408, book_409, book_410,
             book_411, book_412, book_413, book_414, book_415,
             book_416, book_417, book_418, book_419, book_420,
             book_421, book_422, book_423, book_424, book_425]
    
    for book_fn in books:
        path, pages = book_fn()
        results.append((path, pages))
    
    print()
    print("=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)
    total = 0
    for path, pages in results:
        fname = os.path.basename(path)
        total += pages
        status = "PASS" if pages >= 30 else "LOW"
        print(f"  {fname:<55} | {pages:>3} pg | {status}")
    
    print(f"\n  TOTAL: {len(results)} Etsy PDFs | {total} total pages")
    print("  All optimized for Etsy digital download market!")
    print("=" * 70)

if __name__ == "__main__":
    generate_all()
