from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "STILL LOVED"
subtitle = "A Guided Journal for Pregnancy Loss & Miscarriage"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, title, 'F2', 20)
pdf.add_centered_text(450, subtitle, 'F4', 11)
pdf.add_centered_text(380, "For the baby who was wanted,", 'F4', 10)
pdf.add_centered_text(365, "loved, and will never be forgotten.", 'F4', 10)
pdf.add_centered_text(230, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, title, 'F2', 11)
pdf.add_centered_text(470, f"Copyright 2025 {author}", 'F4', 9)
pdf.add_centered_text(455, "All rights reserved.", 'F4', 9)
pdf.add_centered_text(425, "No part of this publication may be reproduced without permission.", 'F4', 8)
pdf.add_centered_text(395, "If you are in crisis, please call 988 (Suicide & Crisis Lifeline)", 'F4', 8)
pdf.add_centered_text(380, "or the Postpartum Support Helpline: 1-800-944-4773", 'F4', 8)

# Page 3: You Are Not Alone (Opening Letter)
pdf.new_page()
pdf.add_centered_text(610, "YOU ARE NOT ALONE", 'F2', 14)
pdf.add_line(40, 600, 392, 600)
y = 575
letter = [
    "Dear Mama (or Papa),",
    "",
    "I am so deeply sorry for your loss. The baby you carried, no matter",
    "how briefly, was real. Your love was real. Your grief is real.",
    "",
    "You may have heard:",
    "'At least you know you can get pregnant.'",
    "'It was not meant to be.'",
    "'You can always try again.'",
    "'At least it was early.'",
    "",
    "None of those words help. None of them honor what you lost.",
    "What you lost was a PERSON. A future. A hope. A part of yourself.",
    "",
    "This journal is your safe space. There are no right or wrong",
    "answers. There is no timeline for grief. There is no 'getting over",
    "it' - there is only learning to carry it.",
    "",
    "You may use this journal every day, or you may pick it up only",
    "when the waves of grief feel too heavy to carry alone.",
    "",
    "Your baby existed. Your baby mattered. Your baby is still loved.",
    "",
    "With compassion and understanding,",
    f"{author}"
]
for line in letter:
    pdf.add_text(40, y, line, 'F4', 9)
    y -= 14

# Page 4: My Baby's Details
pdf.new_page()
pdf.add_centered_text(610, "MY BABY'S DETAILS", 'F2', 14)
pdf.add_line(40, 600, 392, 600)
y = 575
pdf.add_text(40, y, "You do not have to fill in everything. Write only what feels right.", 'F4', 9)
y -= 20
details = [
    "Due date: ___/___/___",
    "",
    "How far along I was: _____ weeks",
    "",
    "Date of loss: ___/___/___",
    "",
    "Names I considered or chose:",
    "_______________________________________________________________",
    "",
    "How I found out I was pregnant:",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "",
    "How I felt when I found out:",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "",
    "Who I told:",
    "_______________________________________________________________",
    "",
    "What I want to remember about this pregnancy:",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "",
    "My baby, you were: _____________________________________________",
    "_______________________________________________________________"
]
for line in details:
    pdf.add_text(40, y, line, 'F4', 9)
    y -= 14

# Pages 5-34: 30 Daily Guided Pages
prompts = [
    "What I want people to understand about my loss...",
    "A letter to my baby...",
    "My body is healing by...",
    "I honor my baby by...",
    "What brings me comfort today...",
    "Permission I give myself today...",
    "My hope for tomorrow...",
    "What I am angry about...",
    "A letter to my body...",
    "The hardest part of today was...",
    "What I want people to understand about my loss...",
    "A letter to my baby...",
    "My body is healing by...",
    "I honor my baby by...",
    "What brings me comfort today...",
    "Permission I give myself today...",
    "My hope for tomorrow...",
    "What I wish I could say to someone...",
    "A memory I want to keep...",
    "Today I am grateful for...",
    "What I want people to understand about my loss...",
    "A letter to my baby...",
    "My body is healing by...",
    "I honor my baby by...",
    "What brings me comfort today...",
    "Permission I give myself today...",
    "My hope for tomorrow...",
    "How I am different now...",
    "What I want my future to hold...",
    "A letter to myself one year from now..."
]

for day in range(1, 31):
    pdf.new_page()
    pdf.add_text(40, 615, f"Day {day}", 'F2', 11)
    pdf.add_text(300, 615, "Date: ___/___/___", 'F1', 9)
    pdf.add_line(40, 607, 392, 607)
    y = 590
    pdf.add_text(40, y, "Today I feel:", 'F2', 9)
    y -= 14
    pdf.add_line(40, y, 392, y, 0.3, 0.5)
    y -= 18
    # Prompt
    prompt = prompts[day - 1]
    pdf.add_text(40, y, prompt, 'F5', 10)
    y -= 22
    # Writing lines
    num_lines = 22
    for _ in range(num_lines):
        pdf.add_line(40, y, 392, y, 0.3, 0.6)
        y -= 16

# Page 35: Milestone Dates to Honor
pdf.new_page()
pdf.add_centered_text(610, "MILESTONE DATES TO HONOR", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 575
pdf.add_text(40, y, "Grief does not follow a calendar, but certain dates may bring", 'F4', 9)
y -= 12
pdf.add_text(40, y, "waves of emotion. Planning ahead can help you feel prepared.", 'F4', 9)
y -= 20
milestones = [
    ("My baby's due date:", "___/___/___"),
    ("Anniversary of the loss:", "___/___/___"),
    ("Mother's Day:", "___/___/___"),
    ("Father's Day:", "___/___/___"),
    ("Baby shower dates (if planned):", "___/___/___"),
    ("Holidays that feel hardest:", "_______________"),
    ("Other significant dates:", "_______________"),
]
for label, blank in milestones:
    pdf.add_text(40, y, label, 'F2', 9)
    pdf.add_text(250, y, blank, 'F1', 9)
    y -= 16
    pdf.add_text(45, y, "How I want to honor this date:", 'F1', 8)
    pdf.add_line(195, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 12
    pdf.add_line(45, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 16
y -= 10
pdf.add_text(40, y, "IDEAS FOR HONORING MY BABY:", 'F2', 9)
y -= 14
ideas = [
    "Light a candle on significant dates",
    "Plant a tree or flower in their memory",
    "Donate to a pregnancy loss charity",
    "Write a letter each year on the due date",
    "Wear a special piece of jewelry",
    "Create a memory box with any keepsakes",
    "Say their name - they deserve to be spoken of"
]
for idea in ideas:
    pdf.add_text(50, y, f"- {idea}", 'F4', 8)
    y -= 12

# Page 36: Resources & Support
pdf.new_page()
pdf.add_centered_text(610, "RESOURCES & SUPPORT", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 575
resources = [
    "CRISIS SUPPORT:",
    "  988 Suicide & Crisis Lifeline: Call or text 988",
    "  Postpartum Support International: 1-800-944-4773",
    "  Crisis Text Line: Text HOME to 741741",
    "",
    "PREGNANCY LOSS ORGANIZATIONS:",
    "  March of Dimes: marchofdimes.org",
    "  Share Pregnancy & Infant Loss: nationalshare.org",
    "  The Compassionate Friends: compassionatefriends.org",
    "  Still Birthday: stillbirthday.com",
    "",
    "SUPPORT GROUPS:",
    "  Local group: _________________________________________",
    "  Online group: ________________________________________",
    "  Meeting day/time: ____________________________________",
    "",
    "MY SUPPORT PEOPLE:",
    "  Who I can call anytime: _______________________________",
    "  Who understands (has been through loss): _______________",
    "  My therapist/counselor: _______________________________",
    "  My doctor/midwife: ___________________________________",
    "",
    "BOOKS THAT MAY HELP:",
    "  (Ask your librarian or therapist for recommendations",
    "  on pregnancy loss grief books)",
    "",
    "WHEN TO SEEK PROFESSIONAL HELP:",
    "  - Thoughts of harming yourself",
    "  - Unable to function in daily life after several weeks",
    "  - Turning to alcohol or substances to cope",
    "  - Relationship is severely strained",
    "  - Previous mental health conditions are worsening",
    "  There is NO shame in needing help. You deserve support."
]
for line in resources:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 37: My Healing Affirmations
pdf.new_page()
pdf.add_centered_text(610, "MY HEALING AFFIRMATIONS", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 575
pdf.add_text(40, y, "Read these when you need them. Add your own at the bottom.", 'F4', 9)
y -= 20
affirmations = [
    "My grief is proof of my love.",
    "I am allowed to feel whatever I feel.",
    "My baby was real and my baby mattered.",
    "I am not broken. I am healing.",
    "There is no timeline for grief.",
    "I can miss my baby and still live my life.",
    "I am stronger than I know.",
    "It is okay to laugh again. Joy does not erase love.",
    "My body did its best. This was not my fault.",
    "I will carry my baby in my heart forever.",
    "I am allowed to say my baby's name.",
    "I can be sad and hopeful at the same time.",
    "Asking for help is brave, not weak.",
    "I will get through this moment. And the next one.",
    "My baby's life, however brief, changed me forever."
]
for aff in affirmations:
    pdf.add_text(50, y, f"~ {aff}", 'F5', 9)
    y -= 16
y -= 10
pdf.add_text(40, y, "MY OWN AFFIRMATIONS:", 'F2', 9)
y -= 16
for _ in range(5):
    pdf.add_line(40, y, 392, y, 0.3, 0.5)
    y -= 16

# Page 38: Letter to Future Self
pdf.new_page()
pdf.add_centered_text(610, "A LETTER TO MY FUTURE SELF", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 575
pdf.add_text(40, y, "Write a letter to yourself one year from now.", 'F4', 9)
y -= 12
pdf.add_text(40, y, "What do you hope you will know, feel, or have accomplished?", 'F4', 9)
y -= 20
pdf.add_text(40, y, "Dear Future Me,", 'F5', 10)
y -= 18
for _ in range(28):
    pdf.add_line(40, y, 392, y, 0.3, 0.5)
    y -= 15
y -= 5
pdf.add_text(40, y, "With love,", 'F5', 9)
y -= 14
pdf.add_text(40, y, "Me (today's date: ___/___/___)", 'F4', 9)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book131_Miscarriage_Grief_Journal.pdf')
print("Book131_Miscarriage_Grief_Journal.pdf created successfully!")
