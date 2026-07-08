from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(530, "WHEN SOMEONE I LOVE DIES", 'F2', 20)
pdf.add_centered_text(495, "A Grief Workbook for Children Ages 5-10", 'F4', 14)
pdf.add_centered_text(350, "It's okay to feel sad.", 'F5', 13)
pdf.add_centered_text(330, "It's okay to feel confused.", 'F5', 13)
pdf.add_centered_text(310, "It's okay to feel everything.", 'F5', 13)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: Message to Grown-Ups
pdf.new_page()
pdf.add_centered_text(750, "A MESSAGE TO GROWN-UPS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Dear Parent, Guardian, or Caregiver,", "",
    "This workbook is designed to help your child process grief in",
    "age-appropriate ways. Children grieve differently than adults.",
    "They may seem fine one moment and fall apart the next.", "",
    "HOW TO USE THIS BOOK:",
    "- Go at your child's pace. Don't rush through it.",
    "- Be present. Sit with them and answer questions honestly.",
    "- It's okay to say 'I don't know' or 'I'm sad too.'",
    "- Some pages may be too hard right now. That's okay. Skip them.",
    "- Return to pages as many times as needed.",
    "- Read body language. Stop if they seem overwhelmed.", "",
    "THINGS CHILDREN NEED TO HEAR:",
    "- 'This is not your fault.'",
    "- 'It's okay to cry. It's also okay not to cry.'",
    "- 'I'm here. I'm not going anywhere.'",
    "- 'There is no wrong way to feel.'",
    "- 'We will get through this together.'", "",
    "If your child shows prolonged distress, please consider",
    "a grief counselor who specializes in children."
]:
    pdf.add_text(60, y, line, 'F4', 11)
    y -= 17

# Page 4: What Happened
pdf.new_page()
pdf.add_centered_text(750, "WHAT HAPPENED", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
for line in [
    "Someone I love has died.", "",
    "Their name is: ________________________________", "",
    "They were my: _________________________________",
    "(grandma, grandpa, mom, dad, sister, brother, friend, pet)", "",
    "They died on: _________________________________", "",
    "When I found out, I felt:", "",
    "  sad    scared    angry    confused    numb", "",
    "It's okay to feel ALL of those things.", "",
    "Dead means their body stopped working.", 
    "It is not sleeping. They cannot wake up.",
    "It is not anyone's fault.", "",
    "Even though they died, my love for them",
    "will NEVER die. Love lasts forever."
]:
    pdf.add_text(60, y, line, 'F4', 12)
    y -= 20

# Page 5: Feelings Are Okay
pdf.new_page()
pdf.add_centered_text(750, "FEELINGS ARE OKAY", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
pdf.add_text(60, y, "Circle how you feel today (you can circle more than one!):", 'F4', 12)
y -= 35
feelings = ["SAD", "ANGRY", "SCARED", "CONFUSED", "LONELY",
    "HAPPY", "GUILTY", "WORRIED", "NUMB", "OKAY"]
for i, feel in enumerate(feelings):
    col = i % 2
    row = i // 2
    x = 100 + col * 250
    ypos = y - row * 60
    # Draw a circle-like shape with a rect
    pdf.add_rect(x, ypos - 10, 120, 40, 1.5)
    pdf.add_centered_text(ypos + 8, feel if col == 0 else "            " + feel, 'F2', 14)

# Page 6: Draw Your Person
pdf.new_page()
pdf.add_centered_text(750, "MY PERSON", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 710
pdf.add_text(60, y, "Draw a picture of the person who died.", 'F4', 12)
pdf.add_text(60, y-18, "What did they look like? What do you remember about them?", 'F4', 12)
pdf.add_rect(80, 150, 450, 500, 1)
pdf.add_text(60, 130, "Their name: ___________________________________", 'F4', 12)


# Page 7: Things I Remember
pdf.new_page()
pdf.add_centered_text(750, "THINGS I REMEMBER", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
for line in [
    "Write or draw things you remember about your person:", "",
    "Their favorite food was: _______________________", "",
    "They always used to say: ______________________", "",
    "They smelled like: ____________________________", "",
    "Their laugh sounded like: _____________________", "",
    "Something funny they did: _____________________", "",
    "They made me feel: ____________________________", "",
    "The best thing about them was: ________________", "",
    "I will never forget: __________________________"
]:
    pdf.add_text(60, y, line, 'F4', 12)
    y -= 25

# Page 8: Special Times
pdf.new_page()
pdf.add_centered_text(750, "OUR SPECIAL TIMES", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
pdf.add_text(60, y, "Draw or write about a happy time you had together:", 'F4', 12)
pdf.add_rect(80, 250, 450, 400, 1)
pdf.add_text(60, 220, "What we were doing: ___________________________", 'F4', 12)
pdf.add_text(60, 190, "How I felt: ___________________________________", 'F4', 12)

# Page 9: Questions I Have
pdf.new_page()
pdf.add_centered_text(750, "QUESTIONS I HAVE", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
pdf.add_text(60, y, "It's okay to have questions. Write them here:", 'F4', 12)
y -= 30
for _ in range(15):
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 25
pdf.add_text(60, y, "It's okay if no one has all the answers.", 'F5', 12)

# Page 10: Who Helps Me
pdf.new_page()
pdf.add_centered_text(750, "WHO HELPS ME FEEL BETTER", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
pdf.add_text(60, y, "When I feel sad, these people help me:", 'F4', 12)
y -= 40
for i in range(5):
    pdf.add_text(60, y, f"Person {i+1}: ___________________________________", 'F4', 12)
    pdf.add_text(60, y-22, f"How they help: ________________________________", 'F4', 12)
    y -= 60
pdf.add_text(60, y, "I am NOT alone. People love me.", 'F5', 13)

# Page 11: Things That Make Me Feel Safe
pdf.new_page()
pdf.add_centered_text(750, "THINGS THAT MAKE ME FEEL SAFE", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
for line in [
    "When I feel scared or sad, these things help:", "",
    "My favorite stuffed animal: ___________________", "",
    "A blanket or comfy thing: _____________________", "",
    "A song that makes me feel better: ______________", "",
    "A place that feels safe: ______________________", "",
    "Something I can hold in my hand: _______________", "",
    "A happy memory I can think about: ______________", "",
    "Taking deep breaths helps. Let's try:", "",
    "Breathe in like you're smelling a flower... 1, 2, 3, 4",
    "Breathe out like you're blowing out candles... 1, 2, 3, 4"
]:
    pdf.add_text(60, y, line, 'F4', 12)
    y -= 25


# Page 12: It's Okay to Cry AND Laugh
pdf.new_page()
pdf.add_centered_text(750, "IT'S OKAY TO CRY AND LAUGH", 'F2', 16)
pdf.add_line(60, 735, 552, 735)
y = 700
for line in [
    "Sometimes you might feel happy and then feel guilty about it.",
    "That's normal! Here's what you need to know:", "",
    "It's OKAY to cry.",
    "Crying means you loved them.", "",
    "It's OKAY to laugh.",
    "Laughing doesn't mean you forgot them.", "",
    "It's OKAY to play and have fun.",
    "Your person would WANT you to be happy.", "",
    "It's OKAY to feel angry.",
    "You can be mad that they're gone.", "",
    "It's OKAY to be confused.",
    "Death is hard for EVERYONE to understand.", "",
    "It's OKAY to feel nothing sometimes.",
    "Your heart might need a break.", "",
    "Whatever you feel is the RIGHT thing to feel.",
    "There is no wrong way to be sad."
]:
    pdf.add_text(60, y, line, 'F4', 12)
    y -= 22

# Page 13: Letter to My Person
pdf.new_page()
pdf.add_centered_text(750, "A LETTER TO MY PERSON", 'F2', 16)
pdf.add_line(60, 735, 552, 735)
y = 700
pdf.add_text(60, y, "Write a letter to the person who died. Tell them anything:", 'F4', 12)
y -= 25
pdf.add_text(60, y, "Dear ________________________,", 'F5', 13)
y -= 30
for _ in range(18):
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 25
pdf.add_text(60, y, "Love, _________________", 'F5', 13)

# Page 14: Things I Want to Say
pdf.new_page()
pdf.add_centered_text(750, "THINGS I WANT TO SAY", 'F2', 16)
pdf.add_line(60, 735, 552, 735)
y = 700
for line in [
    "If I could talk to them one more time, I would say:", "",
    "I love you because: ___________________________", "",
    "I miss you because: ___________________________", "",
    "I wish I had told you: ________________________", "",
    "Thank you for: ________________________________", "",
    "My favorite thing you taught me: _______________", "",
    "I promise I will: _____________________________", "",
    "I want you to know: ___________________________"
]:
    pdf.add_text(60, y, line, 'F4', 12)
    y -= 28

# Page 15: My Worry Box
pdf.new_page()
pdf.add_centered_text(750, "MY WORRY BOX", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
for line in [
    "Write your worries here to let them go:", "",
    "Sometimes when someone dies, we worry about other things.", "",
    "I worry that: _________________________________", "",
    "I worry that: _________________________________", "",
    "I worry that: _________________________________", "",
    "I worry that: _________________________________", "",
    "Now take a deep breath.",
    "You put your worries in this box.",
    "A grown-up can help carry them for you.", "",
    "Things I can CONTROL:", "",
    "_______________________________________________", "",
    "Things I CANNOT control (let them go):", "",
    "_______________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 12)
    y -= 22

# Page 16: Good Memories
pdf.new_page()
pdf.add_centered_text(750, "GOOD MEMORIES I NEVER WANT TO FORGET", 'F2', 14)
pdf.add_line(60, 735, 552, 735)
y = 710
for i in range(5):
    pdf.add_text(60, y, f"Memory {i+1}:", 'F2', 12)
    y -= 22
    for _ in range(3):
        pdf.add_line(60, y, 550, y, 0.5, 0.5)
        y -= 20
    y -= 20

# Page 17: People Who Love Me
pdf.new_page()
pdf.add_centered_text(750, "PEOPLE WHO LOVE ME", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
pdf.add_text(60, y, "Write the names of people who love and care for you:", 'F4', 12)
y -= 40
for _ in range(8):
    pdf.add_line(60, y, 350, y, 0.5, 0.5)
    y -= 30
pdf.add_text(60, y, "You are loved. You are never alone.", 'F5', 14)

# Page 18: Feelings Calendar
pdf.new_page()
pdf.add_centered_text(750, "MY FEELINGS CALENDAR", 'F2', 16)
pdf.add_line(60, 735, 552, 735)
y = 710
pdf.add_text(60, y, "Color each day: Blue=sad Green=okay Yellow=happy Red=angry", 'F4', 10)
y -= 25
for row in range(5):
    for col in range(6):
        day = row * 6 + col + 1
        if day <= 30:
            x = 70 + col * 80
            pdf.add_rect(x, y - 40, 65, 40, 0.5)
            pdf.add_text(x + 5, y - 10, f"Day {day}", 'F1', 8)
    y -= 55

# Page 19: I Am Brave Because
pdf.new_page()
pdf.add_centered_text(750, "I AM BRAVE BECAUSE...", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 700
for line in [
    "Going through something this hard takes courage.", "",
    "I am brave because I keep going even when it hurts.", "",
    "I am brave because I let myself feel sad.", "",
    "I am brave because I ask for help.", "",
    "I am brave because: ___________________________", "",
    "I am strong because: __________________________", "",
    "I am growing because: _________________________", "",
    "Something I'm proud of myself for:", "",
    "_______________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 12)
    y -= 25

# Page 20: Goodbye For Now
pdf.new_page()
pdf.add_centered_text(750, "GOODBYE FOR NOW", 'F2', 18)
pdf.add_line(60, 735, 552, 735)
y = 680
for line in [
    "Saying goodbye doesn't mean forgetting.", "",
    "Your person will always be part of you.", "",
    "They live on in your memories,", "in the things they taught you,",
    "in the love they gave you,", "and in the love you still feel.", "",
    "Grief gets softer over time.", "Not smaller, but softer.",
    "Like a heavy backpack that slowly gets lighter.", "",
    "You will smile again. You will laugh again.",
    "And that's exactly what your person wants for you.", "", "",
    "You are loved.",
    "You are brave.",
    "You are going to be okay.", "", "",
    "With love and hope always."
]:
    pdf.add_text(100, y, line, 'F5', 13)
    y -= 22

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book112_Grief_Workbook_Children.pdf')
print("Book112_Grief_Workbook_Children.pdf created successfully!")
