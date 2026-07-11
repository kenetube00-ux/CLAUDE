from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "FOREVER MY PARENT"
subtitle = "A Grief Journal for Adult Children Who Lost a Parent"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, title, 'F2', 18)
pdf.add_centered_text(450, subtitle, 'F4', 12)
pdf.add_centered_text(350, "A space to remember, grieve,", 'F4', 11)
pdf.add_centered_text(335, "and carry their love forward", 'F4', 11)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(520, title, 'F2', 12)
pdf.add_centered_text(490, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(470, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(440, "No part of this publication may be reproduced without permission.", 'F4', 8)

# Page 3: The Unique Grief of Losing a Parent
pdf.new_page()
pdf.add_centered_text(610, "THE UNIQUE GRIEF OF LOSING A PARENT", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
lines = [
    "Losing a parent changes you at your core. It doesn't matter",
    "if you were 25 or 55 when it happened. Something fundamental",
    "shifts when the person who brought you into this world leaves it.",
    "",
    "This grief is unique because:",
    "- They knew you from your very beginning",
    "- They were your first model of love (imperfect as it may have been)",
    "- Part of your identity was built in relationship to them",
    "- You may now feel like an 'adult orphan' - untethered",
    "- Every milestone from now on will have their absence",
    "",
    "This journal is for you to:",
    "- Process the waves of grief as they come",
    "- Preserve memories before they fade",
    "- Say the things left unsaid",
    "- Find ways to carry their love forward",
    "- Give yourself permission to grieve YOUR way",
    "",
    "There is no timeline for this. There is no 'getting over it.'",
    "There is only learning to carry this love-turned-grief",
    "alongside everything else in your life.",
    "",
    "Write when you're ready. Skip days when you're not.",
    "This journal will wait for you.",
]
for line in lines:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Pages 4-33: 30 Daily Grief Journal Pages
prompts = [
    "What I wish I could ask you today...",
    "A lesson you taught me that I carry every day...",
    "Holiday traditions I want to keep alive...",
    "How I see you in myself (mannerisms, habits, values)...",
    "Things I never got to say to you...",
    "How I'm honoring your memory this week...",
    "A smell, sound, or place that brings you back to me...",
    "What I wish I could ask you today...",
    "Something funny I remember about you...",
    "What I miss most about our everyday life...",
    "A lesson you taught me that I carry every day...",
    "How I wish you could see my life now...",
    "Holiday traditions I want to keep alive...",
    "The hardest part of grief today...",
    "How I see you in myself (mannerisms, habits, values)...",
    "Something I'm grateful you gave me...",
    "Things I never got to say to you...",
    "A time you made me feel completely loved...",
    "How I'm honoring your memory this week...",
    "What I want my children to know about you...",
    "What I wish I could ask you today...",
    "A tradition or recipe of yours I'll never let die...",
    "A lesson you taught me that I carry every day...",
    "How grief surprised me today...",
    "Holiday traditions I want to keep alive...",
    "Your voice - what I remember you saying...",
    "How I see you in myself (mannerisms, habits, values)...",
    "What I'm learning about myself through this grief...",
    "Things I never got to say to you...",
    "How I'm honoring your memory this week...",
]

for day in range(30):
    pdf.new_page()
    pdf.add_text(40, 615, f"Day {day+1}", 'F2', 11)
    pdf.add_text(280, 615, "Date: ___/___/___", 'F1', 10)
    pdf.add_line(40, 607, 392, 607)
    y = 590
    pdf.add_text(40, y, "Missing you level today (1-10): ___", 'F4', 9.5)
    y -= 20
    pdf.add_text(40, y, f"Today's prompt: {prompts[day]}", 'F5', 10)
    y -= 22
    # Writing lines
    while y > 50:
        pdf.add_line(40, y, 392, y, 0.3, 0.7)
        y -= 18

# Page 34: First Holidays Without Them
pdf.new_page()
pdf.add_centered_text(610, "FIRST HOLIDAYS WITHOUT THEM", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
holidays = [
    "The firsts are the hardest. Give yourself permission to do these",
    "YOUR way - not how everyone expects you to.",
    "",
    "THEIR BIRTHDAY:",
    "How I want to honor it: ______________________________",
    "___________________________________________________",
    "",
    "MAJOR HOLIDAYS:",
    "What I want to keep: ________________________________",
    "What I need to change: _______________________________",
    "Who I want to be with: _______________________________",
    "",
    "ANNIVERSARY OF THEIR PASSING:",
    "How I want to spend this day: _________________________",
    "___________________________________________________",
    "",
    "MY BIRTHDAY / MILESTONES:",
    "How I'll include their memory: ________________________",
    "___________________________________________________",
    "",
    "PERMISSION SLIPS:",
    "- I'm allowed to be sad at celebrations",
    "- I'm allowed to be happy on hard days",
    "- I'm allowed to skip traditions that hurt too much",
    "- I'm allowed to create new traditions",
    "- I'm allowed to cry in public without apology",
]
for line in holidays:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15

# Page 35: Carrying Their Legacy Forward
pdf.new_page()
pdf.add_centered_text(610, "CARRYING THEIR LEGACY FORWARD", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
legacy = [
    "Your parent lives on through you. Here's how to carry them:",
    "",
    "VALUES THEY MODELED THAT I WANT TO LIVE:",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "",
    "THINGS THEY LOVED THAT I'LL CONTINUE:",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "",
    "THEIR WISDOM I'LL PASS ON:",
    "___________________________________________________",
    "___________________________________________________",
    "",
    "HOW I'LL KEEP THEIR MEMORY ALIVE FOR OTHERS:",
    "___________________________________________________",
    "___________________________________________________",
    "",
    "A CAUSE OR VALUE I'LL CHAMPION IN THEIR NAME:",
    "___________________________________________________",
    "",
    "LETTER TO MY PARENT:",
    "Dear ___________,",
]
for line in legacy:
    pdf.add_text(40, y, line, 'F4', 9.5)
    y -= 15
# Add writing lines for the letter
while y > 50:
    pdf.add_line(40, y, 392, y, 0.3, 0.7)
    y -= 18

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book158_Grief_Journal_Parent_Loss.pdf')
print("Book158_Grief_Journal_Parent_Loss.pdf created successfully!")
