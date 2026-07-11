#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(420, "THE UNMASKED JOURNAL", 'F2', 17)
pdf.add_centered_text(393, "For Women Discovering Their ADHD", 'F4', 12)
pdf.add_centered_text(360, f"By {author}", 'F4', 11)
pdf.add_line(80, 340, 352, 340, 2)
pdf.add_centered_text(310, "You're not broken. You're neurodivergent.", 'F4', 10, 0.3)

# Page 2 - Copyright + Validation
pdf.new_page()
pdf.add_centered_text(620, f"Copyright - {author}", 'F1', 9)
pdf.add_centered_text(605, "All rights reserved.", 'F1', 9)
pdf.add_centered_text(570, "YOUR DIAGNOSIS IS VALID", 'F2', 13)
pdf.add_line(80, 558, 352, 558, 1)
pdf.add_text(40, 540, "Even if you were diagnosed late.", 'F4', 10, 0.3)
pdf.add_text(40, 523, "Even if people say 'but you don't look ADHD.'", 'F4', 10, 0.3)
pdf.add_text(40, 506, "Even if you got straight A's (by exhausting yourself).", 'F4', 10, 0.3)
pdf.add_text(40, 489, "Even if you've been masking for decades.", 'F4', 10, 0.3)
pdf.add_text(40, 472, "Even if you still doubt it some days.", 'F4', 10, 0.3)
pdf.add_text(40, 445, "Your struggle was real. Your diagnosis explains it.", 'F2', 10, 0.3)
pdf.add_text(40, 425, "You are not lazy. You are not 'too much.'", 'F2', 10, 0.3)
pdf.add_text(40, 405, "You have a brain that works differently.", 'F2', 10, 0.3)
pdf.add_text(40, 385, "And this journal is for YOU.", 'F1', 10)

# Page 3 - What ADHD Looks Like in Women
pdf.new_page()
pdf.add_centered_text(620, "ADHD IN WOMEN", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Why we get missed, misdiagnosed, or diagnosed late:", 'F2', 9)
symptoms = [
    "Internalized symptoms (anxiety, depression, shame)",
    "Masking (appearing 'fine' while internally drowning)",
    "Perfectionism as compensation",
    "People-pleasing to avoid rejection",
    "Emotional dysregulation labeled as 'hormonal'",
    "Daydreaming instead of hyperactivity",
    "Chronic exhaustion from trying so hard",
    "Messy but hiding it from others",
    "Starting projects, never finishing",
    "Time blindness that looks like 'not caring'",
    "Sensory overwhelm mistaken for being 'too sensitive'",
]
y = 572
for s in symptoms:
    pdf.add_text(50, y, f"- {s}", 'F1', 8)
    y -= 13
pdf.add_text(40, y-10, "Which ones resonate with me (circle or highlight):", 'F4', 9, 0.3)

# Pages 4-33 - 60 daily entries (2 per page = 30 pages)
for page in range(30):
    pdf.new_page()
    for entry in range(2):
        entry_num = page * 2 + entry + 1
        y_offset = 320 if entry == 1 else 620
        pdf.add_text(40, y_offset, f"Day {entry_num}", 'F2', 10)
        pdf.add_text(130, y_offset, "Date: ___________", 'F1', 8)
        pdf.add_text(260, y_offset, "Energy: 1 2 3 4 5", 'F1', 8)
        y = y_offset - 16
        pdf.add_text(40, y, "Today my ADHD showed up as:", 'F1', 8)
        pdf.add_line(40, y-12, 392, y-12, 0.5, 0.7)
        pdf.add_line(40, y-25, 392, y-25, 0.5, 0.7)
        y -= 40
        pdf.add_text(40, y, "What I'm proud of despite ADHD:", 'F1', 8)
        pdf.add_line(40, y-12, 392, y-12, 0.5, 0.7)
        y -= 27
        pdf.add_text(40, y, "One thing I'm letting go of:", 'F1', 8)
        pdf.add_line(40, y-12, 392, y-12, 0.5, 0.7)
        y -= 27
        pdf.add_text(40, y, "Self-compassion:", 'F1', 8)
        pdf.add_line(40, y-12, 392, y-12, 0.5, 0.7)
        y -= 27
        pdf.add_text(40, y, "Tomorrow's ONE priority:", 'F1', 8)
        pdf.add_line(215, y-2, 392, y-2, 0.5, 0.7)
        if entry == 0:
            pdf.add_line(40, y-18, 392, y-18, 0.3, 0.5)


# Pages 34-36 - Unmasking Reflection (3 pages)
for pg in range(3):
    pdf.new_page()
    pdf.add_centered_text(620, f"UNMASKING REFLECTION {pg+1}", 'F2', 13)
    pdf.add_line(40, 610, 392, 610, 1)
    if pg == 0:
        pdf.add_text(40, 590, "Who am I without the mask?", 'F5', 12, 0.3)
        prompts = ["The mask I wore was:", "I masked by:", "It cost me:",
                   "Without the mask, I am actually:", "What I need others to know:"]
    elif pg == 1:
        pdf.add_text(40, 590, "The roles I played to hide my ADHD:", 'F5', 12, 0.3)
        prompts = ["The 'perfect student' who actually:", "The 'reliable friend' who actually:",
                   "The 'organized one' who actually:", "The 'easygoing girl' who actually:",
                   "Who I really am underneath:"]
    else:
        pdf.add_text(40, 590, "Releasing the mask - one layer at a time:", 'F5', 12, 0.3)
        prompts = ["One mask I'm ready to release:", "What scares me about unmasking:",
                   "What excites me about being authentic:", "People I feel safe unmasking with:",
                   "My unmasking goal this month:"]
    y = 568
    for p in prompts:
        pdf.add_text(40, y, p, 'F2', 9)
        y -= 14
        for i in range(4):
            pdf.add_line(45, y, 392, y, 0.5, 0.7)
            y -= 13
        y -= 8

# Page 37 - Grief for Not Knowing
pdf.new_page()
pdf.add_centered_text(620, "GRIEF FOR THE YEARS OF NOT KNOWING", 'F2', 12)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "It's okay to grieve what could have been.", 'F4', 10, 0.3)
pdf.add_text(40, 570, "What might have been different if I'd known sooner:", 'F2', 9)
y = 552
for i in range(5):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14
pdf.add_text(40, y-5, "What I want to say to my younger self:", 'F2', 9)
y -= 22
for i in range(5):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14
pdf.add_text(40, y-5, "What I'm choosing to believe now:", 'F2', 9)
y -= 22
for i in range(4):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14

# Page 38 - ADHD Superpowers
pdf.new_page()
pdf.add_centered_text(620, "MY ADHD SUPERPOWERS", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "ADHD isn't all struggle. Claim your strengths:", 'F4', 10, 0.3)
powers = ["Creativity/out-of-box thinking", "Hyperfocus on passions",
           "Empathy and emotional depth", "Resilience (we've survived so much!)",
           "Energy and enthusiasm", "Pattern recognition",
           "Crisis management skills", "Humor and quick wit",
           "Passion and intensity", "Big-picture thinking"]
y = 572
for p in powers:
    pdf.add_rect(45, y-7, 9, 9)
    pdf.add_text(58, y-5, p, 'F1', 9)
    y -= 15
pdf.add_text(40, y-10, "My personal superpowers:", 'F2', 9)
y -= 28
for i in range(4):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14

# Page 39 - Accommodations I Deserve
pdf.new_page()
pdf.add_centered_text(620, "ACCOMMODATIONS I DESERVE", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "You are allowed to need support. That's not weakness.", 'F4', 10, 0.3)
accom = ["Written instructions instead of verbal", "Flexible deadlines when possible",
          "Body doubling for task initiation", "Visual reminders and alarms",
          "Noise-canceling headphones", "Movement breaks",
          "Shorter meetings with agendas", "Permission to fidget",
          "Reduced clutter environment", "Understanding during hormonal shifts"]
y = 572
for a in accom:
    pdf.add_rect(45, y-7, 9, 9)
    pdf.add_text(58, y-5, a, 'F1', 8)
    y -= 14
pdf.add_text(40, y-10, "Accommodations I will ask for:", 'F2', 9)
y -= 28
for i in range(4):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14

# Page 40 - Community
pdf.new_page()
pdf.add_centered_text(620, "MY NEURODIVERGENT COMMUNITY", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "You are not alone. Find your people.", 'F4', 10, 0.3)
pdf.add_text(40, 568, "People who understand:", 'F2', 10)
y = 550
for i in range(5):
    pdf.add_text(40, y, "Name: _________________  How they support me: ___________", 'F1', 8)
    y -= 18
pdf.add_text(40, y-10, "Online communities I follow:", 'F2', 9)
y -= 28
for i in range(4):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14
pdf.add_text(40, y-10, "Books/podcasts that help:", 'F2', 9)
y -= 28
for i in range(4):
    pdf.add_line(45, y, 392, y, 0.5, 0.7)
    y -= 14
pdf.add_centered_text(y-20, "You are not too much. You are exactly enough.", 'F5', 10, 0.3)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book189_ADHD_Women_Journal.pdf')
print("Book189_ADHD_Women_Journal.pdf created successfully!")
