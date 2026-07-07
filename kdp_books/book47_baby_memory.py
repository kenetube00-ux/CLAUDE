"""Book 47: Baby's First Year Memory Book"""
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)

# Title page
pdf.new_page()
pdf.add_centered_text(420, "BABY'S FIRST YEAR", 'F2', 22)
pdf.add_centered_text(380, "A Memory Book", 'F4', 16, 0.3)
pdf.add_line(130, 360, 302, 360, 1, 0.5)
pdf.add_centered_text(200, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(400, "Baby's First Year - A Memory Book", 'F2', 14)
pdf.add_centered_text(370, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(350, "All rights reserved.", 'F1', 10)

# About Our Baby page
pdf.new_page()
pdf.add_centered_text(600, "About Our Baby", 'F2', 16)
y = 560
fields = [
    "Baby's Name: ___________________________________",
    "Date of Birth: ___________________________________",
    "Time of Birth: ___________________________________",
    "Weight: ___________________________________",
    "Length: ___________________________________",
    "Hospital: ___________________________________",
    "Doctor: ___________________________________",
    "Hair Color: ___________________________________",
    "Eye Color: ___________________________________",
]
for field in fields:
    pdf.add_text(50, y, field, 'F1', 11)
    y -= 28


# 12 monthly milestone pages
month_milestones = [
    "lifting head, focusing on faces, grasping reflex",
    "smiling, cooing, following objects with eyes",
    "holding head steady, reaching for objects, laughing",
    "rolling over, grabbing toys, recognizing parents",
    "sitting with support, babbling, teething may begin",
    "sitting alone briefly, responding to name, solid foods",
    "crawling, pulling up, waving bye-bye",
    "standing with support, pincer grasp, stranger anxiety",
    "cruising furniture, pointing, understanding 'no'",
    "standing alone, first words, clapping hands",
    "walking with help, imitating actions, feeding self",
    "first steps, several words, shows affection"
]

for month in range(1, 13):
    pdf.new_page()
    pdf.add_centered_text(610, f"Month {month}", 'F2', 16)
    pdf.add_line(50, 598, 382, 598, 0.5, 0.5)

    y = 575
    pdf.add_text(50, y, f"Date: _______________", 'F1', 10)
    y -= 25
    pdf.add_text(50, y, f"Weight: ________  Length: ________", 'F1', 11)
    y -= 28
    pdf.add_text(50, y, "New Skills:", 'F2', 11)
    y -= 18
    pdf.add_text(55, y, f"(common: {month_milestones[month-1]})", 'F1', 8, 0.5)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 16
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 25
    pdf.add_text(50, y, "Favorite Things:", 'F2', 11)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 25
    pdf.add_text(50, y, "Sleeping Pattern:", 'F2', 11)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 25
    pdf.add_text(50, y, "Feeding:", 'F2', 11)
    y -= 18
    pdf.add_line(50, y, 382, y, 0.5, 0.6)

    if month >= 6:
        y -= 25
        pdf.add_text(50, y, "First words/teeth/steps:", 'F2', 11)
        y -= 18
        pdf.add_line(50, y, 382, y, 0.5, 0.6)

    y -= 28
    pdf.add_text(50, y, "This month you...", 'F2', 11)
    y -= 18
    for _ in range(4):
        pdf.add_line(50, y, 382, y, 0.5, 0.6)
        y -= 16

    y -= 20
    pdf.add_text(50, y, "Photo Space:", 'F2', 10)
    y -= 5
    pdf.add_rect(116, y - 100, 200, 100, 1, 0.4)


# First Christmas/Birthday page
pdf.new_page()
pdf.add_centered_text(600, "First Christmas & First Birthday", 'F2', 16)
y = 560
pdf.add_text(50, y, "First Christmas:", 'F2', 12)
y -= 22
pdf.add_text(55, y, "Date: _______________", 'F1', 10)
y -= 20
pdf.add_text(55, y, "What we did: _________________________________", 'F1', 10)
y -= 18
pdf.add_line(55, y, 382, y, 0.5, 0.6)
y -= 20
pdf.add_text(55, y, "Gifts received: _______________________________", 'F1', 10)
y -= 18
pdf.add_line(55, y, 382, y, 0.5, 0.6)
y -= 35
pdf.add_text(50, y, "First Birthday:", 'F2', 12)
y -= 22
pdf.add_text(55, y, "Date: _______________", 'F1', 10)
y -= 20
pdf.add_text(55, y, "Theme: ______________________________________", 'F1', 10)
y -= 20
pdf.add_text(55, y, "Guests: ______________________________________", 'F1', 10)
y -= 18
pdf.add_line(55, y, 382, y, 0.5, 0.6)
y -= 20
pdf.add_text(55, y, "Cake: ________________________________________", 'F1', 10)
y -= 20
pdf.add_text(55, y, "Best moment: _________________________________", 'F1', 10)
y -= 18
pdf.add_line(55, y, 382, y, 0.5, 0.6)

# Family tree page
pdf.new_page()
pdf.add_centered_text(600, "Our Family Tree", 'F2', 16)
y = 550
pdf.add_text(50, y, "Baby:", 'F2', 11)
pdf.add_text(120, y, "________________________________", 'F1', 11)
y -= 35
pdf.add_text(50, y, "Mother:", 'F2', 11)
pdf.add_text(120, y, "________________________________", 'F1', 11)
y -= 25
pdf.add_text(50, y, "Father:", 'F2', 11)
pdf.add_text(120, y, "________________________________", 'F1', 11)
y -= 35
pdf.add_text(50, y, "Maternal Grandmother:", 'F2', 11)
pdf.add_text(210, y, "____________________", 'F1', 11)
y -= 25
pdf.add_text(50, y, "Maternal Grandfather:", 'F2', 11)
pdf.add_text(210, y, "____________________", 'F1', 11)
y -= 35
pdf.add_text(50, y, "Paternal Grandmother:", 'F2', 11)
pdf.add_text(210, y, "____________________", 'F1', 11)
y -= 25
pdf.add_text(50, y, "Paternal Grandfather:", 'F2', 11)
pdf.add_text(210, y, "____________________", 'F1', 11)
y -= 35
pdf.add_text(50, y, "Siblings:", 'F2', 11)
pdf.add_line(120, y, 382, y, 0.5, 0.6)

# Letter to baby page
pdf.new_page()
pdf.add_centered_text(600, "A Letter to Our Baby", 'F2', 16)
pdf.add_text(50, 565, "Dear _________________________,", 'F4', 12)
y = 535
for _ in range(20):
    pdf.add_line(50, y, 382, y, 0.5, 0.6)
    y -= 22
y -= 10
pdf.add_text(250, y, "With all our love,", 'F4', 11)
y -= 22
pdf.add_line(250, y, 382, y, 0.5, 0.6)

pdf.save("Book47_Baby_First_Year_Memory.pdf")
print("Created Book47_Baby_First_Year_Memory.pdf")
