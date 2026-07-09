from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "ADHD HOMEWORK PLANNER FOR KIDS"
subtitle = "Ages 8-14"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 18)
pdf.add_centered_text(515, subtitle, 'F4', 14)
pdf.add_centered_text(450, "A Weekly Planning System Designed for", 'F4', 12)
pdf.add_centered_text(430, "How YOUR Brain Works Best", 'F4', 12)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 12)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: How to Use This Planner
pdf.new_page()
pdf.add_centered_text(750, "HOW TO USE THIS PLANNER", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
lines = [
    "FOR PARENTS:",
    "- Sit with your child for 5-10 minutes each Sunday to plan the week",
    "- Help them break big projects into small steps",
    "- Review the planner together each evening (keep it brief!)",
    "- Celebrate effort, not just grades",
    "- Use the reward system - kids with ADHD need more frequent rewards",
    "- Sign off each week to show you noticed their work",
    "",
    "FOR KIDS:",
    "- This is YOUR planner - decorate it however you want!",
    "- Write down ALL assignments as soon as you get them",
    "- Check off each box when you finish something (so satisfying!)",
    "- Use 'Break It Down' for any project that takes more than 1 day",
    "- Be honest about what is hard - that is how we figure out help",
    "- Remember: ADHD is not about being smart or not smart.",
    "  Your brain just works DIFFERENTLY. This planner works WITH your brain.",
    "",
    "TIPS FOR ADHD HOMEWORK SUCCESS:",
    "1. SAME TIME every day (build a routine, not willpower)",
    "2. SAME PLACE every day (remove distractions from that spot)",
    "3. START with the hardest or least favorite subject FIRST",
    "4. Take BREAKS every 15-25 minutes (set a timer!)",
    "5. BODY DOUBLES help - do homework near someone else working",
    "6. MUSIC without words can help focus (try lo-fi beats)",
    "7. FIDGET tools are allowed if they help you think",
    "8. CELEBRATE finishing - you earned that reward!"
]
for line in lines:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Pages 4-39: 36 Weekly Homework Pages
for week in range(1, 37):
    pdf.new_page()
    pdf.add_centered_text(755, f"WEEK {week}", 'F2', 16)
    pdf.add_line(50, 745, 562, 745)
    y = 725

    # Assignments Due This Week table
    pdf.add_text(50, y, "ASSIGNMENTS DUE THIS WEEK:", 'F2', 11)
    y -= 18
    # Header
    pdf.add_filled_rect(50, y - 3, 512, 16, 0.85)
    pdf.add_text(55, y, "Subject", 'F2', 9)
    pdf.add_text(150, y, "Assignment", 'F2', 9)
    pdf.add_text(380, y, "Due Date", 'F2', 9)
    pdf.add_text(460, y, "Done?", 'F2', 9)
    y -= 18
    for row in range(7):
        pdf.add_text(55, y, "____________", 'F1', 8)
        pdf.add_text(150, y, "________________________________", 'F1', 8)
        pdf.add_text(380, y, "___/___", 'F1', 8)
        pdf.add_rect(465, y - 2, 12, 12, 0.5)
        y -= 17
        pdf.add_line(50, y + 5, 562, y + 5, 0.2, 0.8)

    y -= 15
    # Break It Down section
    pdf.add_filled_rect(50, y - 3, 512, 18, 0.9)
    pdf.add_text(55, y, "BREAK IT DOWN (for big projects):", 'F2', 11)
    y -= 22
    pdf.add_text(50, y, "Project Name: ________________________________________________", 'F1', 9)
    y -= 16
    pdf.add_text(50, y, "Final Due Date: ___/___/___", 'F1', 9)
    y -= 18
    for step in range(5):
        pdf.add_rect(55, y - 2, 10, 10, 0.5)
        pdf.add_text(70, y, f"Step {step+1}: ______________________________ Do by: ___/___", 'F1', 9)
        y -= 16

    y -= 15
    # How did this week go?
    pdf.add_text(50, y, "HOW DID THIS WEEK GO?", 'F2', 10)
    y -= 16
    pdf.add_text(50, y, "Hardest subject: _________________  Easiest: _________________", 'F1', 9)
    y -= 14
    pdf.add_text(50, y, "What helped me focus: ___________________________________________", 'F1', 9)
    y -= 14
    pdf.add_text(50, y, "What distracted me: _____________________________________________", 'F1', 9)
    y -= 20

    # Reward & Signatures
    pdf.add_filled_rect(50, y - 3, 250, 45, 0.92)
    pdf.add_rect(50, y - 3, 250, 45, 0.5, 0.5)
    pdf.add_text(55, y + 28, "REWARD EARNED THIS WEEK:", 'F2', 9)
    pdf.add_text(55, y + 12, "________________________", 'F1', 9)

    pdf.add_rect(320, y - 3, 242, 45, 0.5, 0.5)
    pdf.add_text(325, y + 28, "Parent Signature:", 'F1', 9)
    pdf.add_line(415, y + 26, 555, y + 26, 0.3, 0.5)
    pdf.add_text(325, y + 12, "Teacher Notes:", 'F1', 9)
    pdf.add_line(405, y + 10, 555, y + 10, 0.3, 0.5)

# Page 40: Study Tips for ADHD Kids
pdf.new_page()
pdf.add_centered_text(750, "STUDY TIPS FOR ADHD KIDS", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
tips = [
    "YOUR BRAIN IS AWESOME! It just needs the right strategies:",
    "",
    "FOR READING:",
    "- Read out loud or whisper-read (hearing helps memory)",
    "- Use a ruler or finger to track the line you are on",
    "- Summarize each paragraph in 1 sentence in the margin",
    "- Set a timer for 10 minutes, then take a 2-minute break",
    "",
    "FOR MATH:",
    "- Do problems on graph paper to keep numbers lined up",
    "- Circle the operation sign before you start each problem",
    "- Check your work by doing the opposite operation",
    "- Use colored pencils for different steps",
    "",
    "FOR WRITING:",
    "- Talk out your ideas first (record yourself on a phone)",
    "- Use bullet points before writing full sentences",
    "- Focus on IDEAS first, fix spelling/grammar LAST",
    "- Write for 5 minutes, break for 2, repeat",
    "",
    "FOR STUDYING/TESTS:",
    "- Make flashcards (the ACT of making them helps you learn)",
    "- Teach the material to a stuffed animal or pet",
    "- Use silly songs or rhymes for things you need to memorize",
    "- Study in short bursts (15 min) spread over multiple days",
    "",
    "FOR STAYING ORGANIZED:",
    "- Use ONE folder or binder (fewer things to lose)",
    "- Take a photo of the homework board before leaving class",
    "- Pack your backpack the NIGHT before",
    "- Put things you need by the door so you cannot forget them"
]
for line in tips:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 41: Test Prep Planning
pdf.new_page()
pdf.add_centered_text(750, "TEST PREP PLANNING PAGE", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Use this page when you have an upcoming test or quiz.", 'F4', 11)
y -= 25
for test in range(3):
    pdf.add_filled_rect(50, y - 5, 512, 185, 0.95)
    pdf.add_rect(50, y - 5, 512, 185, 0.5, 0.5)
    pdf.add_text(55, y + 165, f"TEST #{test+1}", 'F2', 11)
    pdf.add_text(55, y + 148, "Subject: __________________  Test Date: ___/___/___", 'F1', 9)
    pdf.add_text(55, y + 132, "Topics covered: _________________________________________________", 'F1', 9)
    pdf.add_text(55, y + 116, "Study materials I need: _________________________________________", 'F1', 9)
    pdf.add_text(55, y + 96, "MY STUDY PLAN:", 'F2', 9)
    pdf.add_text(55, y + 80, "Day 1 (___/___): ________________________________________________", 'F1', 9)
    pdf.add_text(55, y + 64, "Day 2 (___/___): ________________________________________________", 'F1', 9)
    pdf.add_text(55, y + 48, "Day 3 (___/___): ________________________________________________", 'F1', 9)
    pdf.add_text(55, y + 32, "Study method I will use: Flash cards / Teach someone / Practice problems / Other", 'F1', 9)
    pdf.add_text(55, y + 16, "How I did: ____  What I will do differently next time: ____________", 'F1', 9)
    y -= 205

# Page 42: End-of-Semester Celebration
pdf.new_page()
pdf.add_centered_text(750, "END-OF-SEMESTER CELEBRATION!", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 710
pdf.add_centered_text(y, "YOU DID IT!", 'F2', 20)
y -= 35
celebrate = [
    "Look back at all the weeks you completed. That took REAL effort",
    "and you should be incredibly proud of yourself!",
    "",
    "MY ACCOMPLISHMENTS THIS SEMESTER:",
    "",
    "Total weeks I used my planner: _____ / 36",
    "Assignments I completed on time: _____",
    "Big projects I broke into steps: _____",
    "Tests I studied for using my plan: _____",
    "",
    "WHAT I LEARNED ABOUT MYSELF:",
    "My best study time is: _________________________________________",
    "My best study place is: ________________________________________",
    "The strategy that helps me most: ________________________________",
    "I work best when: ______________________________________________",
    "",
    "WHAT I AM MOST PROUD OF: _______________________________________",
    "________________________________________________________________",
    "",
    "GOAL FOR NEXT SEMESTER: _________________________________________",
    "________________________________________________________________",
    "",
    "REWARD I EARNED FOR FINISHING THIS PLANNER:",
    "________________________________________________________________",
    "",
    "Parent message to student:",
    "________________________________________________________________",
    "________________________________________________________________",
    "",
]
for line in celebrate:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

pdf.add_centered_text(y - 10, "Remember: Having ADHD means your brain is wired for creativity,", 'F5', 11)
pdf.add_centered_text(y - 26, "energy, and big ideas. Keep using tools that work WITH your brain!", 'F5', 11)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book122_ADHD_Kids_Homework_Planner.pdf')
print("Book122_ADHD_Kids_Homework_Planner.pdf created successfully!")
