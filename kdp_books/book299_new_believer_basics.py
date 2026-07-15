"""Book 299: STARTING STRONG - Essential Truths for New Christians (A 12-Week Workbook)"""
import random
from pdf_utils import PDFDoc

random.seed(299)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    weeks = [
        ("SALVATION", "What happened when I said yes to Jesus?", "Ephesians 2:8-9"),
        ("THE BIBLE", "How do I read and understand God's Word?", "2 Timothy 3:16"),
        ("PRAYER", "How do I talk to God?", "Philippians 4:6"),
        ("CHURCH", "Why do I need other believers?", "Hebrews 10:25"),
        ("BAPTISM", "What is baptism and should I do it?", "Romans 6:4"),
        ("COMMUNION", "What is the Lord's Supper?", "1 Corinthians 11:24-25"),
        ("FORGIVENESS", "How do I deal with guilt and forgive others?", "Colossians 3:13"),
        ("HOLY SPIRIT", "Who is the Holy Spirit and what does He do?", "John 14:26"),
        ("SPIRITUAL GIFTS", "What has God gifted me to do?", "1 Corinthians 12:7"),
        ("TEMPTATION", "How do I resist sin?", "1 Corinthians 10:13"),
        ("SHARING FAITH", "How do I tell others about Jesus?", "Matthew 28:19-20"),
        ("GROWING DAILY", "How do I keep growing for the rest of my life?", "2 Peter 3:18"),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(30, 30, 552, 732, 3, 0.2)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_centered_text(680, "STARTING STRONG", 'F2', 28, 0.1)
    doc.add_centered_text(645, "Essential Truths for", 'F4', 16, 0.25)
    doc.add_centered_text(620, "New Christians", 'F4', 16, 0.25)
    doc.add_centered_text(580, "A 12-Week Workbook", 'F2', 14, 0.3)
    doc.add_filled_rect(150, 350, 312, 150, 0.90)
    doc.add_rect(150, 350, 312, 150, 2, 0.3)
    doc.add_centered_text(460, "[ILLUSTRATION: seedling growing", 'F3', 10, 0.4)
    doc.add_centered_text(445, "into strong tree with deep roots]", 'F3', 10, 0.4)
    doc.add_centered_text(220, "12 Foundations for Lifelong Faith", 'F4', 13, 0.3)
    doc.add_centered_text(110, author, 'F2', 16, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "STARTING STRONG", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.2)
    doc.add_text(72, 630, "Scripture from King James Version (Public Domain).", 'F1', 9, 0.3)
    doc.add_text(72, 600, "Published by KDP Amazon", 'F1', 10, 0.3)
    
    # TOC
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "TABLE OF CONTENTS", 'F2', 16, 0.1)
    y = 695
    for i, (title, question, _) in enumerate(weeks):
        doc.add_text(72, y, f"Week {i+1}: {title}", 'F2', 11, 0.15)
        doc.add_text(90, y-16, question, 'F4', 10, 0.35)
        y -= 40
    
    # 12 weeks - 5 pages each
    for w_idx, (title, question, key_verse) in enumerate(weeks):
        # Page 1: Teaching
        doc.new_page()
        fill = 0.90 + random.uniform(0, 0.05)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_filled_rect(40, 740, 532, 35, 0.88)
        doc.add_rect(40, 740, 532, 35, 1, 0.3)
        doc.add_text(55, 752, f"WEEK {w_idx+1}: {title}", 'F2', 14, 0.1)
        
        doc.add_centered_text(710, question, 'F4', 12, 0.25)
        doc.add_line(120, 705, 492, 705, 1, 0.4)
        
        y = 680
        doc.add_text(72, y, f"KEY VERSE: {key_verse}", 'F2', 11, 0.15)
        y -= 25
        
        # Teaching content per topic
        teachings = {
            "SALVATION": [
                "THE BASICS:",
                "When you accepted Jesus as your Lord and Savior, several things happened:",
                "  1. Your sins were completely forgiven (past, present, future)",
                "  2. You received eternal life - a relationship with God that never ends",
                "  3. The Holy Spirit came to live inside you",
                "  4. You became part of God's family",
                "  5. Your name was written in the Book of Life",
                "",
                "IMPORTANT TO KNOW:",
                "  - Salvation is a GIFT, not something you earn (Ephesians 2:8-9)",
                "  - You can't lose your salvation by messing up (Romans 8:38-39)",
                "  - Salvation changes your eternity AND your today",
                "  - It's the beginning of a journey, not the end",
            ],
            "THE BIBLE": [
                "THE BASICS:",
                "The Bible is God's written Word to humanity. It contains:",
                "  - 66 books written over 1,500 years by 40+ authors",
                "  - Old Testament (before Jesus) - 39 books",
                "  - New Testament (Jesus and after) - 27 books",
                "",
                "WHY READ IT:",
                "  - It reveals who God is",
                "  - It shows you how to live",
                "  - It gives wisdom for decisions",
                "  - It strengthens your faith",
                "  - It's how God speaks to you",
                "",
                "START HERE: Gospel of John, Psalms, Proverbs",
            ],
            "PRAYER": [
                "THE BASICS:",
                "Prayer = talking to God. It's a conversation, not a performance.",
                "",
                "TYPES OF PRAYER:",
                "  - Praise: telling God how great He is",
                "  - Thanks: gratitude for what He's done",
                "  - Confession: admitting wrongs honestly",
                "  - Requests: asking for needs (yours and others')",
                "  - Listening: being quiet to hear His voice",
                "",
                "TIPS:",
                "  - Pray at set times AND throughout the day",
                "  - Use your own words (no special language needed)",
                "  - Be honest about feelings, doubts, anger - God can handle it",
                "  - Keep a prayer journal to track answers",
            ],
        }
        teaching = teachings.get(title, [
            "THE BASICS:",
            f"This week we explore: {question}",
            "",
            f"Key Scripture: {key_verse}",
            "",
            "As a new believer, understanding this topic will help you:",
            "  - Grow stronger in your faith",
            "  - Live more confidently as a Christian",
            "  - Connect more deeply with God and others",
            "",
            "Read the key verse several times this week.",
            "Let it sink into your heart and mind.",
        ])
        for line in teaching:
            if line and (line.startswith("THE ") or line.startswith("WHY") or line.startswith("TYPES") or line.startswith("TIPS") or line.startswith("IMPORTANT") or line.startswith("START")):
                doc.add_text(72, y, line, 'F2', 10, 0.15)
            else:
                doc.add_text(72, y, line, 'F1', 10, 0.25)
            y -= 16
        
        # Page 2: Scripture study
        doc.new_page()
        fill2 = 0.93 + random.uniform(0, 0.04)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"Week {w_idx+1}: {title} - SCRIPTURE STUDY", 'F2', 12, 0.15)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        doc.add_text(72, y, f"Read: {key_verse} (look it up in your Bible)", 'F2', 10, 0.15)
        y -= 25
        doc.add_text(72, y, "Write the verse in your own words:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What does this verse tell me about GOD?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What does this verse tell me about ME?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "What should I DO because of this verse?", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "Questions I still have:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Page 3: Exercises
        doc.new_page()
        fill3 = 0.94 + random.uniform(0, 0.03)
        doc.add_filled_rect(0, 0, 612, 792, fill3)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"Week {w_idx+1}: {title} - EXERCISES", 'F2', 12, 0.15)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        
        # Fill in blanks exercise
        doc.add_text(72, y, "FILL IN THE BLANKS:", 'F2', 11, 0.15)
        y -= 20
        blanks_exercises = [
            f"Salvation is a _______ from God, not something I _______.",
            f"The topic of {title.lower()} matters because _______________________.",
            f"One thing I learned this week: _________________________________.",
            f"God wants me to _______________________________________________.",
        ]
        for ex in blanks_exercises:
            doc.add_text(72, y, ex, 'F1', 10, 0.3)
            y -= 22
        
        y -= 15
        doc.add_text(72, y, "TRUE OR FALSE:", 'F2', 11, 0.15)
        y -= 20
        tf = [
            ("God's love depends on my behavior.", "[ ] T  [ ] F"),
            ("I need to understand everything before I can grow.", "[ ] T  [ ] F"),
            ("The Bible is relevant to my life today.", "[ ] T  [ ] F"),
            ("I can talk to God about anything.", "[ ] T  [ ] F"),
        ]
        for question_tf, options in tf:
            doc.add_text(72, y, f"{options}  {question_tf}", 'F1', 10, 0.3)
            y -= 22
        
        y -= 15
        doc.add_text(72, y, "THIS WEEK'S CHALLENGE:", 'F2', 11, 0.15)
        y -= 20
        challenges = [
            "Write out your salvation story in 3-5 sentences.",
            "Read one chapter of the Gospel of John each day.",
            "Pray for 5 minutes each morning this week.",
            "Visit one church or small group this week.",
            "Watch a video or read an article about baptism.",
            "Take communion at church this Sunday.",
            "Write a letter of forgiveness (you don't have to send it).",
            "Ask God to show you the Holy Spirit's work in your day.",
            "Take a spiritual gifts assessment online.",
            "Identify one temptation and write a plan to resist it.",
            "Share your faith story with one person this week.",
            "Create a daily routine that includes God.",
        ]
        doc.add_text(72, y, challenges[w_idx], 'F4', 10, 0.25)
        
        # Page 4: Journal
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.92)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"Week {w_idx+1}: {title} - MY JOURNAL", 'F2', 12, 0.15)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        doc.add_text(72, y, "What I'm feeling about my faith this week:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "Something new I learned about God:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "My prayer this week:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(6):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        doc.add_text(72, y, "One thing I want to do differently:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        
        # Page 5: Discussion
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.94)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_text(55, 750, f"Week {w_idx+1}: {title} - GROUP DISCUSSION", 'F2', 12, 0.15)
        doc.add_line(55, 745, 557, 745, 1, 0.3)
        y = 720
        disc_questions = [
            f"1. Before becoming a Christian, what did you think about {title.lower()}?",
            f"2. What surprised you most in this week's lesson?",
            f"3. What questions do you still have about {title.lower()}?",
            f"4. How can this group help you grow in this area?",
            f"5. What's one thing you'll do differently this week?",
        ]
        for q in disc_questions:
            doc.add_text(72, y, q, 'F1', 10, 0.25)
            y -= 18
            for _ in range(3):
                doc.add_line(90, y, 540, y, 0.5, 0.5)
                y -= 18
            y -= 10
        
        y -= 10
        doc.add_text(72, y, "GROUP PRAYER REQUESTS:", 'F2', 10, 0.15)
        y -= 18
        for _ in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
    
    # Final page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.91)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(700, "YOU STARTED STRONG!", 'F2', 20, 0.1)
    doc.add_centered_text(665, "12 weeks of foundational faith-building. Well done!", 'F4', 12, 0.25)
    y = 620
    doc.add_text(72, y, "Your journey with God is just beginning.", 'F5', 12, 0.2)
    y -= 30
    doc.add_text(72, y, "Remember:", 'F2', 12, 0.15)
    y -= 22
    reminders = [
        "- Progress, not perfection",
        "- God is patient with you",
        "- Every day is a fresh start",
        "- You are never alone",
        "- The best is yet to come",
    ]
    for r in reminders:
        doc.add_text(90, y, r, 'F4', 11, 0.25)
        y -= 20
    
    # Extra journal and notes pages for 72+ total
    extras = ["MY TESTIMONY", "PRAYER REQUESTS", "ANSWERED PRAYERS", "VERSES TO MEMORIZE",
              "QUESTIONS FOR MY PASTOR", "MY SPIRITUAL GROWTH TIMELINE", "NOTES", "NOTES (continued)"]
    for et in extras:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, et, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book299_New_Believer_Basics.pdf')
    print("Book299_New_Believer_Basics.pdf created successfully!")

if __name__ == "__main__":
    create_book()
