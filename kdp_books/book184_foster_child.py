#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "MY STORY", 'F2', 30)
pdf.add_centered_text(480, "A Life Book for Children in Foster Care", 'F4', 14)
pdf.add_centered_text(440, f"By {author}", 'F4', 12)
pdf.add_line(150, 420, 462, 420, 2)
pdf.add_centered_text(380, "This book belongs to:", 'F4', 12)
pdf.add_line(220, 358, 392, 358, 1)

# Page 2 - Copyright + Message to Grown-ups
pdf.new_page()
pdf.add_centered_text(740, "A MESSAGE TO MY GROWN-UPS", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Dear foster parent, caseworker, or caring adult:", 'F4', 11)
pdf.add_text(50, 680, "This life book helps children in foster care:", 'F1', 10)
points = ["Preserve their personal history and memories",
          "Process feelings about transitions and placements",
          "Maintain connection to their identity and story",
          "Express questions and emotions in a safe way",
          "Feel validated that their experiences matter"]
y = 660
for p in points:
    pdf.add_text(60, y, f"- {p}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-10, "HOW TO USE THIS BOOK:", 'F2', 10)
y -= 28
how = ["Let the child lead. Never force them to fill in pages.",
       "Some pages may bring up big feelings - that's okay.",
       "Offer to write for younger children.",
       "Revisit pages as the child grows and understands more.",
       "This is THEIR book. They decide what goes in it."]
for h in how:
    pdf.add_text(60, y, f"- {h}", 'F1', 10)
    y -= 16
pdf.add_centered_text(y-20, f"Copyright - {author}", 'F1', 9)

# Page 3 - All About Me
pdf.new_page()
pdf.add_centered_text(740, "ALL ABOUT ME", 'F2', 18)
pdf.add_line(50, 730, 562, 730, 1)
fields = [
    "My name is:", "My birthday is:", "I am ___ years old",
    "My favorite color:", "My favorite food:", "My favorite animal:",
    "My favorite song:", "My favorite game:", "My favorite subject in school:",
    "Things I'm good at:", "I am happiest when:", "When I grow up I want to be:",
]
y = 705
for f in fields:
    pdf.add_text(50, y, f, 'F2', 11)
    pdf.add_line(250, y-2, 540, y-2, 0.5, 0.7)
    y -= 32

# Page 4 - My Family
pdf.new_page()
pdf.add_centered_text(740, "MY FAMILY", 'F2', 18)
pdf.add_centered_text(720, "All the people who are important to me", 'F4', 11, 0.4)
pdf.add_line(50, 710, 562, 710, 1)
pdf.add_text(50, 685, "People who are important to me (draw or write):", 'F2', 11)
y = 660
for i in range(8):
    pdf.add_text(50, y, "Name: _________________", 'F1', 10)
    pdf.add_text(250, y, "Who they are to me: _________________", 'F1', 10)
    pdf.add_text(50, y-16, "Something I love about them: ________________________________", 'F1', 10)
    pdf.add_line(50, y-30, 562, y-30, 0.3, 0.8)
    y -= 48


# Page 5 - Where I've Lived
pdf.new_page()
pdf.add_centered_text(740, "WHERE I'VE LIVED", 'F2', 18)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "These are the places I have called home:", 'F4', 11, 0.4)
y = 685
for i in range(6):
    pdf.add_text(50, y, f"Place {i+1}: _______________________________________________", 'F1', 10)
    pdf.add_text(50, y-16, "When: ________________  I was ___ years old", 'F1', 10)
    pdf.add_text(50, y-32, "Something I remember: ___________________________________", 'F1', 10)
    pdf.add_text(50, y-48, "How I felt: ____________________________________________", 'F1', 10)
    pdf.add_line(50, y-60, 562, y-60, 0.5, 0.5)
    y -= 78

# Page 6 - My School
pdf.new_page()
pdf.add_centered_text(740, "MY SCHOOL", 'F2', 18)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Current school: ________________________________________", 'F1', 11)
pdf.add_text(50, 688, "Grade: _______  Teacher: _________________________________", 'F1', 11)
pdf.add_text(50, 666, "My best friend at school: _________________________________", 'F1', 11)
pdf.add_text(50, 644, "Subjects I like: _________________________________________", 'F1', 11)
pdf.add_text(50, 622, "Subjects I find hard: ____________________________________", 'F1', 11)
pdf.add_text(50, 600, "What I like about my school: _____________________________", 'F1', 11)
pdf.add_text(50, 570, "OTHER SCHOOLS I'VE BEEN TO:", 'F2', 11)
y = 550
for i in range(4):
    pdf.add_text(50, y, f"School: _______________________ Grade: ___", 'F1', 10)
    y -= 22

# Page 7 - Things I Love to Do
pdf.new_page()
pdf.add_centered_text(740, "THINGS I LOVE TO DO", 'F2', 18)
pdf.add_line(50, 730, 562, 730, 1)
y = 705
for i in range(15):
    pdf.add_text(50, y, f"{i+1}.", 'F2', 11)
    pdf.add_line(70, y-2, 540, y-2, 0.5, 0.7)
    y -= 30
pdf.add_text(50, y-10, "The thing that makes me happiest is:", 'F2', 11)
pdf.add_line(50, y-28, 540, y-28, 0.5, 0.7)

# Page 8 - My Feelings
pdf.new_page()
pdf.add_centered_text(740, "MY FEELINGS", 'F2', 18)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "It's okay to feel ALL of these feelings:", 'F4', 12, 0.3)
feelings = ["HAPPY", "SAD", "ANGRY", "SCARED", "CONFUSED",
            "LONELY", "EXCITED", "WORRIED", "LOVED", "HOPEFUL"]
y = 680
for f in feelings:
    pdf.add_text(60, y, f, 'F2', 11)
    pdf.add_text(160, y, "I feel this when: ___________________________________", 'F1', 10)
    y -= 25
pdf.add_text(50, y-10, "Right now I mostly feel: _________________________________", 'F1', 11)
pdf.add_text(50, y-30, "And that's okay.", 'F5', 12, 0.3)

# Page 9 - Questions I Have
pdf.new_page()
pdf.add_centered_text(740, "QUESTIONS I HAVE", 'F2', 18)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "It's okay to have questions. You can write them here.", 'F4', 11, 0.3)
pdf.add_text(50, 690, "You can ask a safe adult to help you find answers.", 'F1', 10)
y = 665
for i in range(18):
    pdf.add_text(50, y, "?", 'F2', 14)
    pdf.add_line(70, y-2, 540, y-2, 0.5, 0.7)
    y -= 30

# Page 10 - My Wishes & Dreams
pdf.new_page()
pdf.add_centered_text(740, "MY WISHES & DREAMS", 'F2', 18)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "If I could wish for anything:", 'F2', 11)
y = 688
for i in range(3):
    pdf.add_text(50, y, f"Wish {i+1}: ", 'F1', 11)
    pdf.add_line(110, y-2, 540, y-2, 0.5, 0.7)
    y -= 28
pdf.add_text(50, y-10, "When I grow up, I dream of:", 'F2', 11)
y -= 30
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y-10, "Something I want to do this year:", 'F2', 11)
y -= 30
for i in range(2):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y-10, "Something I want to learn:", 'F2', 11)
y -= 30
pdf.add_line(60, y, 540, y, 0.5, 0.7)


# Page 11 - People Who Help Me
pdf.new_page()
pdf.add_centered_text(740, "PEOPLE WHO HELP ME", 'F2', 18)
pdf.add_line(50, 730, 562, 730, 1)
helpers = [("My caseworker:", "Phone:"), ("My therapist/counselor:", "Phone:"),
           ("My CASA/advocate:", "Phone:"), ("My foster parent(s):", "Phone:"),
           ("My teacher:", "School:"), ("My doctor:", "Phone:"),
           ("Other important person:", "Phone:")]
y = 705
for role, contact in helpers:
    pdf.add_text(50, y, role, 'F2', 10)
    pdf.add_line(220, y-2, 400, y-2, 0.5, 0.7)
    pdf.add_text(410, y, contact, 'F1', 9)
    pdf.add_line(450, y-2, 562, y-2, 0.5, 0.7)
    y -= 30
pdf.add_text(50, y-10, "If I need help, I can call: ________________________________", 'F2', 10)
pdf.add_text(50, y-30, "If it's an emergency, I call: 911", 'F2', 10)

# Page 12 - Letters I Want to Write
pdf.new_page()
pdf.add_centered_text(740, "LETTERS I WANT TO WRITE", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Dear ___________________,", 'F1', 11)
y = 685
for i in range(25):
    pdf.add_line(50, y, 562, y, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y, "From, ___________________", 'F1', 11)

# Page 13 - Things I Want to Remember
pdf.new_page()
pdf.add_centered_text(740, "THINGS I WANT TO REMEMBER", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Happy memories, things people said, or things I don't want to forget:", 'F4', 10, 0.4)
y = 685
for i in range(26):
    pdf.add_line(50, y, 562, y, 0.5, 0.7)
    y -= 22

# Page 14 - My Strengths & Superpowers
pdf.new_page()
pdf.add_centered_text(740, "MY STRENGTHS & SUPERPOWERS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "I am STRONG because I have been through hard things.", 'F5', 12, 0.3)
pdf.add_text(50, 685, "My superpowers:", 'F2', 12)
y = 665
for i in range(8):
    pdf.add_text(60, y, f"Power {i+1}:", 'F1', 11)
    pdf.add_line(120, y-2, 540, y-2, 0.5, 0.7)
    y -= 28
pdf.add_text(50, y-10, "Things other people say I'm good at:", 'F2', 11)
y -= 30
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y-10, "I am proud of myself for:", 'F2', 11)
y -= 30
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 22

# Page 15 - What I Need Others to Know
pdf.new_page()
pdf.add_centered_text(740, "WHAT I NEED OTHERS TO KNOW ABOUT ME", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "If there's one thing I want grown-ups to understand:", 'F4', 11, 0.4)
y = 685
for i in range(6):
    pdf.add_line(50, y, 562, y, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y, "What helps me when I'm upset:", 'F2', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y, "What does NOT help when I'm upset:", 'F2', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y, "Things I need to feel safe:", 'F2', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y, "My biggest hope right now:", 'F2', 11)
y -= 20
pdf.add_line(60, y, 540, y, 0.5, 0.7)

# Pages 16-20 - Photo/Drawing pages
for pg in range(5):
    pdf.new_page()
    titles = ["PICTURES OF ME", "PICTURES OF MY FAMILY",
              "PICTURES OF MY FRIENDS", "PICTURES OF MY PETS",
              "MY FAVORITE DRAWING"]
    pdf.add_centered_text(740, titles[pg], 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, "Paste a photo or draw a picture here:", 'F1', 10, 0.4)
    pdf.add_rect(56, 150, 500, 540)
    pdf.add_text(50, 130, "Caption: _________________________________________________", 'F1', 10)
    pdf.add_text(50, 110, "Date: ________________", 'F1', 10)

# Pages 21-30 - Additional guided pages
extra_pages = [
    "MY DAILY ROUTINE", "THINGS THAT MAKE ME FEEL SAFE",
    "MY FAVORITE MEMORIES", "PEOPLE I MISS",
    "WHAT I'M LOOKING FORWARD TO", "MY GOALS",
    "THINGS I'M GRATEFUL FOR", "A LETTER TO MY FUTURE SELF",
    "MY ACHIEVEMENTS", "YOU ARE BRAVE AND LOVED"
]
for pg, title in enumerate(extra_pages):
    pdf.new_page()
    pdf.add_centered_text(740, title, 'F2', 16)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 9:  # Last page - affirmation
        pdf.add_centered_text(500, "You are BRAVE.", 'F2', 18)
        pdf.add_centered_text(460, "You are STRONG.", 'F2', 18)
        pdf.add_centered_text(420, "You are LOVED.", 'F2', 18)
        pdf.add_centered_text(370, "Your story matters.", 'F4', 14, 0.3)
        pdf.add_centered_text(340, "YOU matter.", 'F4', 14, 0.3)
    else:
        y = 705
        for i in range(26):
            pdf.add_line(50, y, 562, y, 0.5, 0.7)
            y -= 22

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book184_Foster_Child_Life_Book.pdf')
print("Book184_Foster_Child_Life_Book.pdf created successfully!")
