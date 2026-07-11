#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(420, "TINY FOOTPRINTS", 'F2', 18)
pdf.add_centered_text(393, "A Memorial Book for Infant Loss", 'F4', 11)
pdf.add_centered_text(375, "& Stillbirth", 'F4', 11)
pdf.add_centered_text(345, f"By {author}", 'F4', 10)
pdf.add_line(100, 325, 332, 325, 2)

# Page 2 - Validation
pdf.new_page()
pdf.add_centered_text(520, "YOUR BABY WAS REAL", 'F2', 14)
pdf.add_line(80, 508, 352, 508, 1)
pdf.add_centered_text(480, "Your love was real.", 'F4', 11, 0.3)
pdf.add_centered_text(460, "Your pregnancy was real.", 'F4', 11, 0.3)
pdf.add_centered_text(440, "Your hopes were real.", 'F4', 11, 0.3)
pdf.add_centered_text(420, "Your baby existed.", 'F4', 11, 0.3)
pdf.add_centered_text(390, "No matter how brief,", 'F4', 11, 0.3)
pdf.add_centered_text(370, "their life mattered.", 'F4', 11, 0.3)
pdf.add_centered_text(340, "YOUR grief is valid.", 'F5', 12, 0.3)
pdf.add_centered_text(310, "Take all the time you need.", 'F1', 10)
pdf.add_centered_text(280, f"Copyright - {author}", 'F1', 8)
pdf.add_centered_text(265, "All rights reserved.", 'F1', 8)

# Page 3 - Baby's Details
pdf.new_page()
pdf.add_centered_text(620, "MY BABY", 'F2', 16)
pdf.add_line(40, 610, 392, 610, 1)
details = [
    "Name:", "Due date:", "Birthday:",
    "Weight:", "Length:",
    "Hair:", "Who was there:",
    "Hospital:", "Doctor/midwife:",
    "Time of birth:", "Time with baby:",
]
y = 585
for d in details:
    pdf.add_text(40, y, d, 'F2', 10)
    pdf.add_line(160, y-2, 392, y-2, 0.5, 0.7)
    y -= 25
pdf.add_text(40, y-5, "What I want the world to know about my baby:", 'F2', 9)
y -= 22
for i in range(4):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 16

# Pages 4-23 - 20 Memory & Healing Pages
prompts = [
    "When I found out I was pregnant...",
    "I imagined our life together...",
    "The name we chose and why...",
    "The day everything changed...",
    "What happened (as much or little as you want to write)...",
    "What people don't understand about this grief...",
    "Things that bring me comfort...",
    "How I want to honor you...",
    "My body is healing by...",
    "The hardest part is...",
    "What I need from others right now...",
    "My love for you will always...",
    "Things I bought for you...",
    "The nursery/plans we made...",
    "What I wish I could say to you...",
    "How your father/other parent is grieving...",
    "The moments I feel closest to you...",
    "What brings me peace on the hardest days...",
    "How I am changed by knowing you...",
    "My promise to you...",
]
for prompt in prompts:
    pdf.new_page()
    pdf.add_centered_text(610, prompt, 'F4', 11, 0.3)
    pdf.add_line(40, 595, 392, 595, 0.5)
    y = 575
    for i in range(28):
        pdf.add_line(40, y, 392, y, 0.5, 0.7)
        y -= 17


# Page 24 - Handprint/Footprint Memorial
pdf.new_page()
pdf.add_centered_text(620, "HANDPRINTS & FOOTPRINTS", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Place prints, photos, or drawings here:", 'F4', 10, 0.4)
pdf.add_rect(66, 200, 300, 370)
pdf.add_text(40, 180, "Date: _______________", 'F1', 9)
pdf.add_text(40, 162, "Notes: _______________________________________________", 'F1', 9)

# Page 25 - Letter to My Baby
pdf.new_page()
pdf.add_centered_text(620, "A LETTER TO MY BABY", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Dear ___________________,", 'F4', 11)
y = 568
for i in range(28):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 16
pdf.add_text(40, y, "All my love forever, ___________________", 'F4', 11)

# Page 26 - Dates That Matter
pdf.new_page()
pdf.add_centered_text(620, "DATES THAT MATTER TO ME", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "These days may be hard. Planning ahead can help:", 'F1', 9)
dates = ["Due date:", "Birthday:", "Day of loss:",
         "Mother's Day/Father's Day:", "Anniversary of finding out:",
         "Holidays that feel hardest:", "Other meaningful dates:"]
y = 568
for d in dates:
    pdf.add_text(40, y, d, 'F2', 9)
    pdf.add_line(210, y-2, 392, y-2, 0.5, 0.7)
    pdf.add_text(40, y-16, "My plan for this day:", 'F1', 8)
    pdf.add_line(145, y-18, 392, y-18, 0.3, 0.7)
    y -= 38

# Page 27 - Support Resources
pdf.new_page()
pdf.add_centered_text(620, "SUPPORT RESOURCES", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "You don't have to walk this alone:", 'F4', 10, 0.3)
resources = [
    ("Share Pregnancy & Infant Loss Support:", "nationalshare.org"),
    ("Now I Lay Me Down to Sleep:", "nilmdts.org (remembrance photography)"),
    ("March of Dimes:", "marchofdimes.org"),
    ("Still Standing Magazine:", "stillstandingmag.com"),
    ("The Compassionate Friends:", "compassionatefriends.org"),
    ("Postpartum Support International:", "postpartum.net"),
]
y = 568
for org, url in resources:
    pdf.add_text(40, y, org, 'F2', 9)
    pdf.add_text(40, y-13, url, 'F1', 8)
    y -= 30
pdf.add_text(40, y-5, "My therapist/counselor: ___________________", 'F1', 9)
pdf.add_text(40, y-20, "My support group: ___________________", 'F1', 9)
pdf.add_text(40, y-35, "People who understand: ___________________", 'F1', 9)

# Pages 28-29 - Additional healing pages
pdf.new_page()
pdf.add_centered_text(620, "HOW I WILL HONOR MY BABY", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
ideas = ["Light a candle on special days", "Plant a tree or garden",
         "Donate to infant loss charity", "Create a memory box",
         "Wear jewelry in remembrance", "Write their name in the sand",
         "Release balloons or butterflies", "Support other bereaved parents",
         "Create art or music in their honor", "Say their name - always"]
y = 588
for idea in ideas:
    pdf.add_text(50, y, f"- {idea}", 'F1', 9)
    y -= 15
pdf.add_text(40, y-10, "My personal way to honor them:", 'F2', 9)
y -= 28
for i in range(6):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 16

# Page 30 - Closing
pdf.new_page()
pdf.add_centered_text(480, "You were wanted.", 'F5', 14)
pdf.add_centered_text(450, "You were loved.", 'F5', 14)
pdf.add_centered_text(420, "You are remembered.", 'F5', 14)
pdf.add_centered_text(380, "Always.", 'F5', 16)
pdf.add_centered_text(330, "There is no foot so small", 'F4', 11, 0.3)
pdf.add_centered_text(310, "that it cannot leave", 'F4', 11, 0.3)
pdf.add_centered_text(290, "an imprint on this world.", 'F4', 11, 0.3)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book193_Infant_Loss_Memorial_Book.pdf')
print("Book193_Infant_Loss_Memorial_Book.pdf created successfully!")
