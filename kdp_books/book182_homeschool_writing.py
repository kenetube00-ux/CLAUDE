#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "CREATIVE WRITING WORKBOOK", 'F2', 22)
pdf.add_centered_text(485, "For Kids Ages 8-12", 'F4', 15)
pdf.add_centered_text(445, f"By {author}", 'F4', 12)
pdf.add_line(150, 425, 462, 425, 2)
pdf.add_centered_text(390, "Every great writer started with one story.", 'F4', 12, 0.3)

# Page 2 - Copyright
pdf.new_page()
pdf.add_centered_text(500, f"Copyright - {author}", 'F1', 10)
pdf.add_centered_text(480, "All rights reserved.", 'F1', 10)

# Page 3 - Story Elements
pdf.new_page()
pdf.add_centered_text(740, "THE 5 STORY ELEMENTS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
elements = [
    ("CHARACTER", "The people (or animals/creatures) in your story. Who is it about?"),
    ("SETTING", "When and where your story takes place."),
    ("PLOT", "What happens in your story - the events from start to finish."),
    ("CONFLICT", "The problem or challenge your character faces."),
    ("RESOLUTION", "How the problem gets solved at the end."),
]
y = 700
for name, desc in elements:
    pdf.add_text(60, y, name, 'F2', 13)
    pdf.add_text(60, y-18, desc, 'F1', 11)
    y -= 55
pdf.add_text(50, y, "Every great story needs all 5! Let's practice each one.", 'F2', 11, 0.3)

# Pages 4-6 - Character Creation (3 pages)
pdf.new_page()
pdf.add_centered_text(740, "CHARACTER CREATION - PAGE 1", 'F2', 14)
pdf.add_centered_text(722, "What Does Your Character Look Like?", 'F4', 12)
pdf.add_line(50, 710, 562, 710, 1)
pdf.add_text(50, 688, "Character name: _______________________________", 'F1', 11)
pdf.add_text(50, 665, "Age: ______  Boy/Girl/Other: _______________", 'F1', 11)
pdf.add_text(50, 640, "Hair color & style: ___________________________", 'F1', 11)
pdf.add_text(50, 617, "Eye color: __________________________________", 'F1', 11)
pdf.add_text(50, 594, "Height (tall/short/average): _________________", 'F1', 11)
pdf.add_text(50, 571, "What they usually wear: ______________________", 'F1', 11)
pdf.add_text(50, 548, "Something unique about how they look: _________", 'F1', 11)
pdf.add_line(50, 528, 540, 528, 0.5, 0.7)
pdf.add_text(50, 500, "Draw your character here:", 'F2', 11)
pdf.add_rect(50, 280, 500, 210)

pdf.new_page()
pdf.add_centered_text(740, "CHARACTER CREATION - PAGE 2", 'F2', 14)
pdf.add_centered_text(722, "Who Is Your Character Inside?", 'F4', 12)
pdf.add_line(50, 710, 562, 710, 1)
pdf.add_text(50, 688, "3 words that describe their personality:", 'F1', 11)
pdf.add_text(50, 668, "1.__________ 2.__________ 3.__________", 'F1', 11)
pdf.add_text(50, 640, "Their biggest strength: ________________________", 'F1', 11)
pdf.add_text(50, 617, "Their biggest weakness: ________________________", 'F1', 11)
pdf.add_text(50, 594, "Their favorite thing to do: ___________________", 'F1', 11)
pdf.add_text(50, 571, "Their biggest fear: ____________________________", 'F1', 11)
pdf.add_text(50, 548, "What makes them laugh: _________________________", 'F1', 11)
pdf.add_text(50, 525, "What makes them mad: ___________________________", 'F1', 11)
pdf.add_text(50, 502, "Their secret: __________________________________", 'F1', 11)
pdf.add_text(50, 470, "Their best friend is: __________________________", 'F1', 11)
pdf.add_text(50, 447, "Their family: __________________________________", 'F1', 11)

pdf.new_page()
pdf.add_centered_text(740, "CHARACTER CREATION - PAGE 3", 'F2', 14)
pdf.add_centered_text(722, "What Does Your Character Want?", 'F4', 12)
pdf.add_line(50, 710, 562, 710, 1)
pdf.add_text(50, 688, "What do they want MORE than anything?", 'F2', 11)
pdf.add_line(50, 668, 540, 668, 0.5, 0.7)
pdf.add_line(50, 648, 540, 648, 0.5, 0.7)
pdf.add_text(50, 620, "What is stopping them from getting it?", 'F2', 11)
pdf.add_line(50, 600, 540, 600, 0.5, 0.7)
pdf.add_line(50, 580, 540, 580, 0.5, 0.7)
pdf.add_text(50, 552, "What would they do to get what they want?", 'F2', 11)
pdf.add_line(50, 532, 540, 532, 0.5, 0.7)
pdf.add_line(50, 512, 540, 512, 0.5, 0.7)
pdf.add_text(50, 484, "How do they change by the end of the story?", 'F2', 11)
pdf.add_line(50, 464, 540, 464, 0.5, 0.7)
pdf.add_line(50, 444, 540, 444, 0.5, 0.7)


# Page 7 - Setting Builder
pdf.new_page()
pdf.add_centered_text(740, "SETTING BUILDER", 'F2', 16)
pdf.add_centered_text(722, "Describe With 5 Senses!", 'F4', 12)
pdf.add_line(50, 710, 562, 710, 1)
pdf.add_text(50, 688, "My story takes place in: ______________________________", 'F1', 11)
pdf.add_text(50, 665, "Time period (past/present/future): _____________________", 'F1', 11)
senses = [("SEE:", "What does your character see? Colors, shapes, objects:"),
           ("HEAR:", "What sounds are there? Loud? Quiet? Music? Animals?"),
           ("SMELL:", "What does it smell like? Fresh? Smoky? Sweet?"),
           ("TOUCH:", "What do things feel like? Rough? Smooth? Hot? Cold?"),
           ("TASTE:", "Any tastes? Food? Salty air? Dust?")]
y = 635
for sense, prompt in senses:
    pdf.add_text(50, y, sense, 'F2', 11)
    pdf.add_text(100, y, prompt, 'F1', 10)
    y -= 18
    for i in range(2):
        pdf.add_line(60, y, 540, y, 0.5, 0.7)
        y -= 18
    y -= 10

# Page 8 - Plot Mountain
pdf.new_page()
pdf.add_centered_text(740, "PLOT MOUNTAIN", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Every story follows a shape - like a mountain!", 'F1', 11)
# Draw a simple mountain shape with labels
pdf.add_line(80, 400, 306, 600, 1.5)
pdf.add_line(306, 600, 532, 400, 1.5)
pdf.add_text(60, 380, "Beginning", 'F2', 10)
pdf.add_text(270, 610, "CLIMAX", 'F2', 10)
pdf.add_text(500, 380, "End", 'F2', 10)
pdf.add_text(140, 480, "Rising", 'F2', 9)
pdf.add_text(140, 465, "Action", 'F2', 9)
pdf.add_text(400, 480, "Falling", 'F2', 9)
pdf.add_text(400, 465, "Action", 'F2', 9)
pdf.add_text(50, 350, "BEGINNING (introduce character + setting):", 'F2', 10)
pdf.add_line(50, 332, 540, 332, 0.5, 0.7)
pdf.add_line(50, 314, 540, 314, 0.5, 0.7)
pdf.add_text(50, 290, "RISING ACTION (problems get bigger):", 'F2', 10)
pdf.add_line(50, 272, 540, 272, 0.5, 0.7)
pdf.add_line(50, 254, 540, 254, 0.5, 0.7)
pdf.add_text(50, 230, "CLIMAX (biggest moment! Most exciting part!):", 'F2', 10)
pdf.add_line(50, 212, 540, 212, 0.5, 0.7)
pdf.add_line(50, 194, 540, 194, 0.5, 0.7)
pdf.add_text(50, 170, "FALLING ACTION (things start to get better):", 'F2', 10)
pdf.add_line(50, 152, 540, 152, 0.5, 0.7)
pdf.add_text(50, 130, "RESOLUTION (how it all ends):", 'F2', 10)
pdf.add_line(50, 112, 540, 112, 0.5, 0.7)

# Pages 9-23 - 15 Story Starter Prompts
starters = [
    "The box had been buried in the backyard for 100 years...",
    "When I woke up, I could suddenly talk to animals...",
    "The map showed a place that shouldn't exist...",
    "My best friend has a secret that changed everything...",
    "The last day of school started with a loud BOOM...",
    "I found a door in my closet that wasn't there yesterday...",
    "The new kid at school was definitely not human...",
    "Three wishes. That's what the old woman offered me...",
    "The spaceship landed in our backyard on a Tuesday...",
    "I woke up and everyone in town had disappeared...",
    "The library book whispered my name when I walked past...",
    "My robot was supposed to do homework, but it had other plans...",
    "The storm brought something strange to our town...",
    "I discovered I could pause time, but only for 60 seconds...",
    "The forgotten kingdom under the school cafeteria...",
]
for starter in starters:
    pdf.new_page()
    pdf.add_centered_text(740, "STORY STARTER", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 705, starter, 'F5', 12)
    pdf.add_text(50, 680, "Keep writing! What happens next?", 'F1', 10, 0.4)
    y = 655
    for i in range(28):
        pdf.add_line(50, y, 562, y, 0.5, 0.7)
        y -= 20


# Pages 24-26 - Dialogue Writing Practice (3 pages)
for pg in range(3):
    pdf.new_page()
    pdf.add_centered_text(740, f"DIALOGUE PRACTICE - {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 0:
        pdf.add_text(50, 710, "RULES FOR WRITING DIALOGUE:", 'F2', 11)
        rules = ['Use quotation marks: "Hello!" she said.',
                 'New speaker = new paragraph',
                 'Use said, asked, whispered, shouted (not too fancy!)',
                 'Show how they feel through actions too']
        y = 690
        for r in rules:
            pdf.add_text(60, y, f"- {r}", 'F1', 10)
            y -= 16
        pdf.add_text(50, y-10, "PRACTICE: Two friends are arguing about what to do after school:", 'F2', 10)
    elif pg == 1:
        pdf.add_text(50, 710, "PRACTICE: A kid is trying to convince a parent to get a pet:", 'F2', 10)
    else:
        pdf.add_text(50, 710, "PRACTICE: Two characters meet for the first time:", 'F2', 10)
    y = 680 if pg == 0 else 690
    for i in range(28):
        pdf.add_line(50, y, 562, y, 0.5, 0.7)
        y -= 20

# Page 27 - Show Don't Tell
pdf.new_page()
pdf.add_centered_text(740, "SHOW, DON'T TELL!", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Instead of TELLING the reader how someone feels,", 'F1', 11)
pdf.add_text(50, 688, "SHOW it through actions, body language, and details!", 'F2', 11)
examples = [
    ("TELLING: She was scared.", "SHOWING: Her hands shook. She pressed her back against the wall."),
    ("TELLING: He was angry.", "SHOWING: He slammed his fist on the table and his face turned red."),
    ("TELLING: It was cold.", "SHOWING: She pulled her jacket tighter, watching her breath form clouds."),
]
y = 660
for tell, show in examples:
    pdf.add_text(60, y, tell, 'F1', 9)
    pdf.add_text(60, y-14, show, 'F4', 9)
    y -= 38
pdf.add_text(50, y, "YOUR TURN! Rewrite these by SHOWING:", 'F2', 11)
tells = ["The dog was happy.", "She was sad.", "The room was messy.", "He was excited."]
y -= 25
for t in tells:
    pdf.add_text(50, y, f"Telling: {t}", 'F1', 10)
    pdf.add_text(50, y-16, "Showing: ", 'F1', 10)
    pdf.add_line(105, y-18, 540, y-18, 0.5, 0.7)
    pdf.add_line(60, y-34, 540, y-34, 0.5, 0.7)
    y -= 52

# Page 28 - Poetry Templates
pdf.new_page()
pdf.add_centered_text(740, "POETRY FUN!", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "HAIKU (3 lines: 5 syllables / 7 syllables / 5 syllables):", 'F2', 11)
pdf.add_text(50, 685, "Example: An old silent pond (5) / A frog jumps into the pond (7) / Splash! Silence again (5)", 'F4', 9)
pdf.add_text(50, 660, "Your haiku:", 'F1', 10)
pdf.add_line(50, 642, 400, 642, 0.5, 0.7)
pdf.add_line(50, 624, 400, 624, 0.5, 0.7)
pdf.add_line(50, 606, 400, 606, 0.5, 0.7)
pdf.add_text(50, 580, "ACROSTIC (first letter of each line spells a word):", 'F2', 11)
pdf.add_text(50, 560, "Write an acrostic for your name or favorite word:", 'F1', 10)
y = 540
for i in range(8):
    pdf.add_text(50, y, "___", 'F2', 11)
    pdf.add_line(80, y-2, 400, y-2, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y-10, "LIMERICK (AABBA rhyme, funny & bouncy):", 'F2', 11)
pdf.add_text(50, y-28, "There once was a _________ from _________  (A)", 'F1', 10)
pdf.add_text(50, y-44, "Who ________________________________  (A)", 'F1', 10)
pdf.add_text(50, y-60, "________________________________  (B)", 'F1', 10)
pdf.add_text(50, y-76, "________________________________  (B)", 'F1', 10)
pdf.add_text(50, y-92, "________________________________  (A)", 'F1', 10)

# Pages 29-30 - Editing checklist + Author bio
pdf.new_page()
pdf.add_centered_text(740, "EDITING CHECKLIST", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Before you say 'I'm done!' check these:", 'F1', 11)
checks = ["Does my story have a clear beginning, middle, and end?",
           "Did I describe my characters so readers can picture them?",
           "Did I use dialogue to make characters come alive?",
           "Did I SHOW feelings instead of just telling?",
           "Does my story have a problem that gets solved?",
           "Did I use interesting words (not just 'nice' and 'good')?",
           "Did I check for spelling mistakes?",
           "Did I use periods and capital letters correctly?",
           "Does each paragraph have one main idea?",
           "Would I want to read this story? Is it exciting?",
           "Did I read it out loud to catch awkward sentences?",
           "Did I give my story a great title?"]
y = 680
for c in checks:
    pdf.add_rect(55, y-9, 12, 12)
    pdf.add_text(75, y-7, c, 'F1', 10)
    y -= 22

pdf.new_page()
pdf.add_centered_text(740, "ABOUT THE AUTHOR (THAT'S YOU!)", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "My pen name (or real name): _________________________", 'F1', 11)
pdf.add_text(50, 680, "My age: ______", 'F1', 11)
pdf.add_text(50, 655, "I love to write about: ________________________________", 'F1', 11)
pdf.add_text(50, 630, "My favorite book is: __________________________________", 'F1', 11)
pdf.add_text(50, 605, "My favorite author is: ________________________________", 'F1', 11)
pdf.add_text(50, 580, "When I grow up I want to: _____________________________", 'F1', 11)
pdf.add_text(50, 555, "Fun fact about me: ____________________________________", 'F1', 11)
pdf.add_text(50, 520, "Write your author bio (the kind you see on book covers):", 'F2', 11)
y = 495
for i in range(10):
    pdf.add_line(50, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y-10, "Draw yourself as an author:", 'F2', 11)
pdf.add_rect(200, y-170, 200, 150)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book182_Creative_Writing_Workbook.pdf')
print("Book182_Creative_Writing_Workbook.pdf created successfully!")
