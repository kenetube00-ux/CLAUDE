#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "FAITH THAT WORKS", 'F2', 28)
pdf.add_centered_text(480, "A Study of the Book of James", 'F5', 16)
pdf.add_centered_text(440, f"By {author}", 'F4', 12)
pdf.add_line(150, 420, 462, 420, 2)
pdf.add_centered_text(380, "10 Week In-Depth Bible Study", 'F4', 13, 0.3)

# Page 2 - Copyright
pdf.new_page()
pdf.add_centered_text(500, f"Copyright - {author}", 'F1', 10)
pdf.add_centered_text(480, "All rights reserved.", 'F1', 10)
pdf.add_centered_text(440, "Scripture references from various translations.", 'F1', 10)
pdf.add_centered_text(420, "For personal and small group study use.", 'F1', 10)

# Page 3 - Introduction
pdf.new_page()
pdf.add_centered_text(740, "INTRODUCTION TO JAMES", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Author: James, brother of Jesus (likely written 45-50 AD)", 'F1', 11)
pdf.add_text(50, 685, "Audience: Jewish Christians scattered among the nations", 'F1', 11)
pdf.add_text(50, 665, "Theme: Genuine faith produces genuine works", 'F1', 11)
pdf.add_text(50, 640, "Key Verse: 'Faith without works is dead.' - James 2:26", 'F5', 12)
pdf.add_text(50, 610, "OVERVIEW OF JAMES:", 'F2', 12)
topics = [
    "Chapter 1: Trials, Temptation, and True Religion",
    "Chapter 2: Favoritism and Faith & Works",
    "Chapter 3: Taming the Tongue, Two Kinds of Wisdom",
    "Chapter 4: Worldliness, Humility, and Planning",
    "Chapter 5: Patience, Prayer, and Restoration",
]
y = 590
for t in topics:
    pdf.add_text(60, y, t, 'F1', 11)
    y -= 20
pdf.add_text(50, y-20, "HOW TO USE THIS STUDY:", 'F2', 12)
y -= 45
instructions = [
    "1. Read the passage at least twice before answering questions",
    "2. Observation: What does the text SAY?",
    "3. Interpretation: What does it MEAN?",
    "4. Application: How do I APPLY this to my life?",
    "5. Pray before and after each session",
]
for inst in instructions:
    pdf.add_text(60, y, inst, 'F1', 10)
    y -= 18


# 10 weekly studies (2 pages each = 20 pages)
studies = [
    ("Week 1: Trials & Wisdom", "James 1:1-8",
     "James opens with a shocking command: 'Consider it pure joy when you face trials.'",
     ["What does James say trials produce? (v. 3-4)", "Why does James connect trials to wisdom?",
      "What conditions does James give for receiving wisdom? (v. 5-6)",
      "What does 'double-minded' mean in this context?"]),
    ("Week 2: Temptation", "James 1:9-18",
     "James distinguishes between trials (external) and temptation (internal desire).",
     ["How does James describe the progression of temptation? (v. 14-15)",
      "Why does James emphasize God does NOT tempt us?",
      "What is the 'crown of life' promised to? (v. 12)",
      "What do verses 17-18 reveal about God's character?"]),
    ("Week 3: Hearing & Doing", "James 1:19-27",
     "Faith that is real shows up in daily life - quick to listen, slow to speak.",
     ["What three commands does James give in verse 19?",
      "What is the 'mirror' illustration about? (v. 23-25)",
      "What does James define as 'pure religion'? (v. 27)",
      "How does 'getting rid of moral filth' (v. 21) relate to hearing the Word?"]),
    ("Week 4: Favoritism", "James 2:1-13",
     "James confronts the sin of showing partiality based on wealth or status.",
     ["What example does James use to illustrate favoritism? (v. 2-4)",
      "Why is favoritism inconsistent with faith in Christ? (v. 1)",
      "What does James say about God's view of the poor? (v. 5)",
      "How does the 'royal law' relate to favoritism? (v. 8)"]),
    ("Week 5: Faith & Works", "James 2:14-26",
     "The most debated passage in James - what is the relationship between faith and works?",
     ["What kind of faith does James say CANNOT save? (v. 14)",
      "What illustration does James use in v. 15-16?",
      "How do Abraham and Rahab demonstrate faith WITH works?",
      "How do you reconcile James with Paul's teaching on grace?"]),
    ("Week 6: Taming the Tongue", "James 3:1-12",
     "Small but powerful - the tongue can bless or destroy.",
     ["What three metaphors does James use for the tongue? (v. 3-6)",
      "Why does James say the tongue is impossible to tame? (v. 8)",
      "What inconsistency does James point out? (v. 9-12)",
      "What responsibility do teachers have? (v. 1)"]),
    ("Week 7: Godly vs Worldly Wisdom", "James 3:13-4:10",
     "Two kinds of wisdom produce two kinds of living.",
     ["What are the marks of worldly wisdom? (v. 3:14-16)",
      "What are the marks of heavenly wisdom? (v. 3:17-18)",
      "What causes fights among believers? (4:1-3)",
      "What does 'friendship with the world' mean? (4:4)"]),
    ("Week 8: Planning & Pride", "James 4:11-5:6",
     "James warns against arrogant planning and exploitation.",
     ["What does James say about judging others? (4:11-12)",
      "What is wrong with the merchants' plans? (4:13-16)",
      "What principle does 4:17 establish?",
      "What warnings does James give the rich? (5:1-6)"]),
    ("Week 9: Patience in Suffering", "James 5:7-12",
     "In light of Jesus' return, James calls for patient endurance.",
     ["What illustration does James use for patience? (v. 7)",
      "Why does James mention the prophets and Job? (v. 10-11)",
      "What does 'the Lord is compassionate and merciful' mean here?",
      "Why does James mention swearing/oaths in this context? (v. 12)"]),
    ("Week 10: Prayer & Healing", "James 5:13-20",
     "James closes with the power of prayer and community restoration.",
     ["What does James prescribe for different situations? (v. 13-14)",
      "What role do elders play in healing? (v. 14-15)",
      "Why confess sins to one another? (v. 16)",
      "What does it mean to 'turn a sinner back'? (v. 19-20)"]),
]

for title, passage, intro, questions in studies:
    # Study page 1
    pdf.new_page()
    pdf.add_centered_text(740, title.upper(), 'F2', 14)
    pdf.add_centered_text(720, passage, 'F5', 12)
    pdf.add_line(50, 710, 562, 710, 1)
    pdf.add_text(50, 688, intro, 'F4', 10, 0.3)
    pdf.add_text(50, 660, "READ the passage at least twice. Then answer:", 'F2', 11)
    pdf.add_text(50, 640, "OBSERVATION - What does the text SAY?", 'F2', 11)
    y = 618
    for q in questions:
        pdf.add_text(60, y, f"Q: {q}", 'F1', 9)
        y -= 14
        for ln in range(2):
            pdf.add_line(70, y, 540, y, 0.5, 0.7)
            y -= 14
        y -= 5
    pdf.add_text(50, y-5, "INTERPRETATION - What does it MEAN?", 'F2', 11)
    y -= 20
    pdf.add_text(50, y, "What is the main point James is making in this passage?", 'F1', 10)
    y -= 15
    for ln in range(3):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 15

    # Study page 2 - Application, Prayer, Discussion
    pdf.new_page()
    pdf.add_centered_text(740, f"{title.upper()} (continued)", 'F2', 12)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, "APPLICATION - How do I APPLY this?", 'F2', 12)
    pdf.add_text(50, 690, "What is one specific way I can live this out this week?", 'F1', 10)
    y = 670
    for ln in range(4):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "What do I need to change, start, or stop?", 'F1', 10)
    y -= 22
    for ln in range(3):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-10, "PRAYER:", 'F2', 12)
    y -= 28
    pdf.add_text(50, y, "Write a prayer responding to what God has shown you:", 'F1', 10)
    y -= 15
    for ln in range(5):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-10, "DISCUSSION QUESTIONS (for small groups):", 'F2', 12)
    y -= 28
    pdf.add_text(50, y, "1. What stood out to you most in this passage and why?", 'F1', 10)
    y -= 18
    pdf.add_text(50, y, "2. How does this challenge or comfort you?", 'F1', 10)
    y -= 18
    pdf.add_text(50, y, "3. Where do you see this principle in your own life?", 'F1', 10)
    y -= 18
    pdf.add_text(50, y, "4. How can our group support each other in applying this?", 'F1', 10)
    y -= 30
    pdf.add_text(50, y, "NOTES:", 'F2', 11)
    y -= 15
    for ln in range(6):
        pdf.add_line(50, y, 540, y, 0.5, 0.7)
        y -= 18

# Pages 24-25 - Summary and final pages
pdf.new_page()
pdf.add_centered_text(740, "MY JAMES JOURNEY SUMMARY", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Looking back over 10 weeks with James:", 'F2', 11)
pdf.add_text(50, 680, "The biggest lesson I learned:", 'F1', 11)
y = 660
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "How my faith has grown:", 'F1', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "Changes I've made:", 'F1', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "What I want to continue studying:", 'F1', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_centered_text(y-30, "But be doers of the word, and not hearers only. - James 1:22", 'F5', 12, 0.3)

pdf.new_page()
pdf.add_centered_text(500, "May your faith produce works of love.", 'F5', 14, 0.3)
pdf.add_centered_text(460, "Keep studying. Keep growing. Keep doing.", 'F4', 12, 0.3)
pdf.add_centered_text(400, f"- {author}", 'F1', 10)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book178_James_Bible_Study.pdf')
print("Book178_James_Bible_Study.pdf created successfully!")
