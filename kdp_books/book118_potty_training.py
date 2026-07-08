from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(550, "POTTY TRAINING", 'F2', 20)
pdf.add_centered_text(520, "PROGRESS CHART & REWARD BOOK", 'F2', 16)
pdf.add_centered_text(490, "For Toddlers Ages 18mo-4yr", 'F4', 13)
pdf.add_centered_text(400, "You Can Do It!", 'F5', 14)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: Readiness Signs for Parents
pdf.new_page()
pdf.add_centered_text(750, "READINESS SIGNS CHECKLIST", 'F2', 15)
pdf.add_centered_text(733, "For Parents", 'F1', 10)
pdf.add_line(60, 725, 552, 725)
y = 705
for line in [
    "Most children are ready between 18 months and 3 years.",
    "Do NOT start until MOST of these signs are present:", "",
    "PHYSICAL READINESS:",
    "__ Can walk to and sit on toilet/potty",
    "__ Stays dry for 2+ hours at a time",
    "__ Has predictable bowel movements",
    "__ Can pull pants up and down", "",
    "COGNITIVE READINESS:",
    "__ Can follow 2-step directions",
    "__ Understands 'pee' and 'poop' words",
    "__ Knows the difference between wet and dry",
    "__ Can communicate need to go (words or signals)", "",
    "EMOTIONAL READINESS:",
    "__ Shows interest in the toilet/potty",
    "__ Wants to wear 'big kid' underwear",
    "__ Dislikes being in a wet/dirty diaper",
    "__ Is in a cooperative phase (not oppositional)", "",
    "NOT READY SIGNS (wait if):",
    "- New sibling arriving within 2 months",
    "- Recent move or major life change",
    "- Child is in a 'no' phase about everything",
    "- Child shows fear of toilet", "",
    "My child shows ___ out of 12 readiness signs.",
    "Start date: ___/___/___"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 15

# Page 4: Big Kid Intro Page
pdf.new_page()
pdf.add_centered_text(600, "I'M A BIG KID!", 'F2', 22)
pdf.add_centered_text(550, "This book belongs to:", 'F4', 14)
pdf.add_centered_text(520, "________________________", 'F1', 16)
pdf.add_centered_text(450, "I am learning to use the potty!", 'F5', 14)
pdf.add_centered_text(420, "Every time I try, I get a sticker!", 'F4', 12)
pdf.add_centered_text(390, "I am brave and I can do this!", 'F5', 14)
pdf.add_centered_text(300, "My potty training started on: ___/___/___", 'F4', 12)

# Pages 5-19: Daily Potty Chart (15 pages)
for day_page in range(15):
    pdf.new_page()
    day_num = day_page + 1
    pdf.add_centered_text(755, f"POTTY CHART - DAY {day_num}", 'F2', 14)
    pdf.add_text(60, 735, f"Date: ___/___/___  Name: _____________", 'F4', 10)
    pdf.add_line(60, 728, 552, 728)
    y = 710
    # AM Section
    pdf.add_text(60, y, "MORNING (AM)", 'F2', 11)
    y -= 16
    times_am = ["7:00", "8:00", "9:00", "10:00", "11:00", "12:00"]
    pdf.add_text(60, y, "Time    Tried?  Success?  Accident?  Sticker!", 'F2', 9)
    y -= 5
    pdf.add_line(60, y, 400, y, 0.5)
    y -= 14
    for t in times_am:
        pdf.add_text(60, y, f"{t}    [  ]     [  ]      [  ]      [  ]", 'F3', 9)
        y -= 15
    y -= 10
    # PM Section
    pdf.add_text(60, y, "AFTERNOON & EVENING (PM)", 'F2', 11)
    y -= 16
    times_pm = ["1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00"]
    pdf.add_text(60, y, "Time    Tried?  Success?  Accident?  Sticker!", 'F2', 9)
    y -= 5
    pdf.add_line(60, y, 400, y, 0.5)
    y -= 14
    for t in times_pm:
        pdf.add_text(60, y, f"{t}    [  ]     [  ]      [  ]      [  ]", 'F3', 9)
        y -= 15
    y -= 15
    pdf.add_text(60, y, f"Day {day_num} Summary: Tries: ___ Successes: ___ Accidents: ___", 'F2', 9)
    y -= 15
    pdf.add_text(60, y, "Notes: ________________________________________", 'F4', 9)


# Pages 20-23: Weekly Progress Overview (4 pages)
for week in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEKLY PROGRESS - WEEK {week}", 'F2', 14)
    pdf.add_line(60, 738, 552, 738)
    y = 715
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        pdf.add_text(60, y, f"{day}:", 'F2', 10)
        pdf.add_text(140, y, "Successes: ___  Accidents: ___  Dry nap? Y/N", 'F3', 9)
        y -= 20
    y -= 15
    pdf.add_text(60, y, "WEEK SUMMARY:", 'F2', 10)
    y -= 16
    pdf.add_text(60, y, "Total successes: ____  Total accidents: ____", 'F4', 10)
    y -= 16
    pdf.add_text(60, y, "Improvement from last week? Y / N / Same", 'F4', 10)
    y -= 16
    pdf.add_text(60, y, "What's working: _______________________________", 'F4', 10)
    y -= 16
    pdf.add_text(60, y, "What to try differently: ______________________", 'F4', 10)

# Page 24: Reward Ideas + Nighttime Training + Troubleshooting
pdf.new_page()
pdf.add_centered_text(750, "REWARDS & TROUBLESHOOTING", 'F2', 14)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "REWARD IDEAS (choose what motivates YOUR child):", "",
    "- Sticker chart (5 stickers = small prize)",
    "- Special dance or high five",
    "- Extra story at bedtime",
    "- Choose a snack",
    "- Small toy from 'prize box'",
    "- Special activity (park, bubbles)", "",
    "NIGHTTIME TRAINING (separate from daytime!):",
    "Start nighttime training AFTER daytime is consistent.",
    "__ Limit fluids 1 hour before bed",
    "__ Potty right before bed",
    "__ Use waterproof mattress pad",
    "__ Night light near bathroom",
    "Date started: ___/___", "",
    "COMMON PROBLEMS & SOLUTIONS:",
    "Refuses to sit: Make it fun (books, songs on potty)",
    "Holds it in: Increase fiber, more water, don't pressure",
    "Only goes in diaper: Let them sit on potty WITH diaper",
    "Regression: Normal! Stay calm, no punishment, restart gently"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 25: Certificate + Celebration
pdf.new_page()
pdf.add_rect(60, 150, 492, 550, 2)
pdf.add_rect(70, 160, 472, 530, 1)
pdf.add_centered_text(620, "CERTIFICATE OF COMPLETION", 'F2', 20)
pdf.add_centered_text(570, "This certifies that", 'F5', 14)
pdf.add_centered_text(530, "________________________", 'F2', 16)
pdf.add_centered_text(490, "has successfully learned to", 'F5', 14)
pdf.add_centered_text(460, "USE THE POTTY!", 'F2', 18)
pdf.add_centered_text(410, "We are SO PROUD of you!", 'F5', 14)
pdf.add_centered_text(370, "You are a BIG KID now!", 'F5', 14)
pdf.add_centered_text(310, "Date completed: ___/___/___", 'F4', 12)
pdf.add_centered_text(270, "Signed: ______________________", 'F4', 12)
pdf.add_centered_text(220, "I DID IT!", 'F2', 24)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book118_Potty_Training_Chart.pdf')
print("Book118_Potty_Training_Chart.pdf created successfully!")
