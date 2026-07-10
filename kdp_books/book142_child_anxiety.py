"""Book 142: Brave & Strong - An Anxiety Workbook for Kids Ages 6-12"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(520, "BRAVE & STRONG", 'F2', 30, 0)
    doc.add_centered_text(480, "An Anxiety Workbook for Kids Ages 6-12", 'F4', 16, 0.2)
    doc.add_centered_text(400, "You are braver than you think!", 'F4', 14, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0)

    # Page 2: Copyright + Message for Parents
    doc.new_page()
    doc.add_centered_text(700, "A MESSAGE FOR PARENTS & CAREGIVERS", 'F2', 14, 0)
    doc.add_line(72, 690, 540, 690, 1, 0.5)
    doc.add_text(72, 660, "This workbook uses CBT (Cognitive Behavioral Therapy) principles adapted", 'F1', 11, 0.2)
    doc.add_text(72, 643, "for children. It teaches kids to:", 'F1', 11, 0.2)
    y = 615
    points = ["Understand what anxiety is (normalizing it)", "Identify their worries and triggers",
              "Challenge anxious thoughts with evidence", "Face fears gradually (exposure therapy)",
              "Build a toolkit of calming strategies"]
    for p in points:
        doc.add_text(90, y, f"- {p}", 'F1', 11, 0.2)
        y -= 18
    y -= 15
    doc.add_text(72, y, "HOW TO USE: Work through pages together or let your child work", 'F2', 11, 0)
    y -= 18
    doc.add_text(72, y, "independently. Go at their pace. Celebrate all brave steps!", 'F1', 11, 0.2)
    y -= 30
    doc.add_text(72, y, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.4)

    # Page 3: What is Anxiety? (Kid-friendly)
    doc.new_page()
    doc.add_centered_text(740, "WHAT IS ANXIETY?", 'F2', 20, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Anxiety is your brain's ALARM SYSTEM. It's supposed to keep you safe.", 'F1', 12, 0.2)
    doc.add_text(72, 675, "But sometimes the alarm goes off when there's NO real danger.", 'F1', 12, 0.2)
    doc.add_text(72, 650, "It's like a smoke alarm going off because of toast - not a fire!", 'F1', 12, 0.2)
    y = 615
    doc.add_text(72, y, "When I feel anxious, my body might:", 'F2', 12, 0)
    y -= 22
    body_signs = ["Tummy hurts or feels funny", "Heart beats really fast",
                  "Hands get sweaty", "Hard to breathe", "Feel dizzy",
                  "Want to run away or hide", "Can't stop thinking scary thoughts"]
    for b in body_signs:
        doc.add_rect(72, y-3, 12, 12)
        doc.add_text(90, y, b, 'F1', 12, 0.2)
        y -= 22
    y -= 15
    doc.add_text(72, y, "Circle the ones YOU feel! It's totally normal.", 'F2', 12, 0)

    # Page 4: My Worry Monsters
    doc.new_page()
    doc.add_centered_text(740, "MY WORRY MONSTERS", 'F2', 20, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Let's give your worries a name! When we name them, they lose power.", 'F1', 12, 0.2)
    y = 665
    for i in range(3):
        doc.add_text(72, y, f"Worry Monster #{i+1}:", 'F2', 12, 0)
        y -= 22
        doc.add_text(72, y, "Name: _________________________ What it says to me:", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.3)
        y -= 22
        doc.add_text(72, y, "Draw it here:", 'F1', 11, 0.2)
        doc.add_rect(72, y-80, 180, 75)
        doc.add_text(280, y, "How big is this worry? (circle)", 'F1', 11, 0.2)
        doc.add_text(280, y-20, "TINY   SMALL   MEDIUM   BIG   HUGE", 'F1', 11, 0.2)
        y -= 100

    # Page 5: The Anxiety Trick
    doc.new_page()
    doc.add_centered_text(740, "THE ANXIETY TRICK", 'F2', 20, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Here's a SECRET about anxiety:", 'F2', 12, 0)
    doc.add_text(72, 673, "The more you AVOID something scary, the SCARIER it gets!", 'F2', 13, 0)
    y = 643
    doc.add_text(72, y, "It's like a bully. If you run away, it chases you harder.", 'F1', 12, 0.2)
    y -= 22
    doc.add_text(72, y, "But if you face it (a little bit at a time), it gets SMALLER.", 'F1', 12, 0.2)
    y -= 35
    doc.add_text(72, y, "EXAMPLE:", 'F2', 12, 0)
    y -= 22
    doc.add_text(90, y, "Sarah was scared of dogs. She avoided ALL dogs.", 'F1', 11, 0.2)
    y -= 18
    doc.add_text(90, y, "Her fear got BIGGER and BIGGER.", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(90, y, "Then she tried her BRAVE LADDER:", 'F1', 11, 0.2)
    y -= 18
    doc.add_text(90, y, "Step 1: Look at pictures of dogs", 'F1', 11, 0.2)
    y -= 16
    doc.add_text(90, y, "Step 2: Watch dogs from far away", 'F1', 11, 0.2)
    y -= 16
    doc.add_text(90, y, "Step 3: Be near a small, calm dog", 'F1', 11, 0.2)
    y -= 16
    doc.add_text(90, y, "Step 4: Pet a friendly dog", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(90, y, "Each step felt scary at first, but her brain LEARNED it was safe!", 'F2', 11, 0)

    # Page 6: Brave Ladder
    doc.new_page()
    doc.add_centered_text(740, "MY BRAVE LADDER", 'F2', 20, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Write your fear at the top. Break it into small steps from easy to hard:", 'F1', 11, 0.2)
    doc.add_text(72, 680, "My fear: __________________________________________________________", 'F2', 12, 0)
    y = 640
    for step in range(7, 0, -1):
        doc.add_filled_rect(72 + (7-step)*15, y-5, 400 - (7-step)*15, 30, 0.9 - step*0.02)
        doc.add_text(80 + (7-step)*15, y+5, f"Step {step}: ___________________________________________", 'F1', 11, 0.2)
        doc.add_text(80 + (7-step)*15, y-10, f"Scariness (1-10): ___   Done? [ ]", 'F1', 9, 0.3)
        y -= 42
    y -= 10
    doc.add_text(72, y, "Remember: Start at the bottom! You don't have to rush to the top.", 'F2', 11, 0)

    # Page 7: Calm-Down Breathing
    doc.new_page()
    doc.add_centered_text(740, "CALM-DOWN BREATHING EXERCISES", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    doc.add_text(72, y, "BALLOON BREATH:", 'F2', 14, 0)
    y -= 22
    doc.add_text(90, y, "1. Put your hands on your tummy", 'F1', 12, 0.2)
    y -= 18
    doc.add_text(90, y, "2. Breathe IN slowly - blow up the balloon in your tummy!", 'F1', 12, 0.2)
    y -= 18
    doc.add_text(90, y, "3. Breathe OUT slowly - let the air out of the balloon", 'F1', 12, 0.2)
    y -= 18
    doc.add_text(90, y, "4. Do this 5 times. Your body will calm down!", 'F1', 12, 0.2)
    y -= 35
    doc.add_text(72, y, "STAR BREATH:", 'F2', 14, 0)
    y -= 22
    doc.add_text(90, y, "1. Hold up your hand like a star", 'F1', 12, 0.2)
    y -= 18
    doc.add_text(90, y, "2. With your other finger, trace UP each finger = breathe IN", 'F1', 12, 0.2)
    y -= 18
    doc.add_text(90, y, "3. Trace DOWN each finger = breathe OUT", 'F1', 12, 0.2)
    y -= 18
    doc.add_text(90, y, "4. By the time you finish all 5 fingers, you'll feel calmer!", 'F1', 12, 0.2)
    y -= 35
    doc.add_text(72, y, "HOT CHOCOLATE BREATH:", 'F2', 14, 0)
    y -= 22
    doc.add_text(90, y, "Pretend you're holding a cup of hot chocolate.", 'F1', 12, 0.2)
    y -= 18
    doc.add_text(90, y, "Smell the yummy chocolate (breathe IN through nose)", 'F1', 12, 0.2)
    y -= 18
    doc.add_text(90, y, "Cool it down (breathe OUT through mouth slowly)", 'F1', 12, 0.2)

    # Page 8: Thinking Traps for Kids
    doc.new_page()
    doc.add_centered_text(740, "THINKING TRAPS", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Sometimes our brains trick us into thinking the WORST will happen.", 'F1', 12, 0.2)
    doc.add_text(72, 683, "These are called THINKING TRAPS:", 'F1', 12, 0.2)
    y = 650
    traps = [
        ("THE DISASTER TRAP:", "Thinking the WORST thing will definitely happen.",
         "'If I raise my hand, everyone will laugh at me and I'll die of embarrassment!'"),
        ("THE ALL-OR-NOTHING TRAP:", "Everything is either PERFECT or TERRIBLE.",
         "'If I'm not the best at soccer, I'm the worst player ever!'"),
        ("THE MIND-READING TRAP:", "Thinking you know what others think.",
         "'That kid didn't wave back - they must HATE me!'"),
        ("THE FORTUNE-TELLING TRAP:", "Predicting bad things will happen.",
         "'I KNOW the test will be impossible and I'll fail!'")
    ]
    for name, desc, example in traps:
        doc.add_text(72, y, name, 'F2', 11, 0)
        y -= 18
        doc.add_text(90, y, desc, 'F1', 11, 0.2)
        y -= 18
        doc.add_text(90, y, example, 'F3', 9, 0.4)
        y -= 30

    # Pages 9-13: Brave Thoughts Practice (5 pages)
    scenarios = [
        ("Going to a birthday party", "What if nobody talks to me?", "I've been to parties before and had fun. If I feel nervous, I can find one person to talk to."),
        ("Taking a test at school", "I'm going to fail and everyone will think I'm dumb!", "I studied. Even if I don't get 100%, I'll do my best. One test doesn't make me dumb."),
        ("Sleeping alone at night", "Something scary might happen in the dark!", "My room is safe. My parents are right here. Nothing bad has happened before."),
        ("Trying something new", "I'll mess up and everyone will laugh!", "Everyone messes up when they're learning. That's how we get better!"),
        ("Being away from parents", "What if something bad happens to them?", "My parents are safe. They always come back. Worrying doesn't keep them safer.")
    ]
    for scenario, worry, brave in scenarios:
        doc.new_page()
        doc.add_centered_text(740, "BRAVE THOUGHTS PRACTICE", 'F2', 16, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 700
        doc.add_text(72, y, f"Situation: {scenario}", 'F2', 11, 0)
        y -= 28
        doc.add_text(72, y, f"Worry thought: {worry}", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, f"Brave thought: {brave}", 'F4', 11, 0.2)
        y -= 40
        doc.add_text(72, y, "NOW YOUR TURN! Think of a time you felt this way:", 'F2', 12, 0)
        y -= 25
        doc.add_text(72, y, "My situation: ______________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "My worry thought: __________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Evidence it's NOT true: _____________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "My BRAVE thought: __________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Scariness BEFORE brave thought (1-10): ___", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "Scariness AFTER brave thought (1-10): ___", 'F1', 11, 0.2)

    # Page 14: My Calm-Down Toolkit
    doc.new_page()
    doc.add_centered_text(740, "MY CALM-DOWN TOOLKIT", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "When I feel anxious, these things help me calm down:", 'F1', 12, 0.2)
    y = 670
    for i in range(8):
        doc.add_text(72, y, f"{i+1}. _____________________________________________________________", 'F1', 12, 0.2)
        y -= 30
    y -= 10
    doc.add_text(72, y, "Draw your happy/calm place here:", 'F2', 12, 0)
    doc.add_rect(72, y-130, 468, 125)

    # Page 15: Worry Time Box
    doc.new_page()
    doc.add_centered_text(740, "WORRY TIME BOX", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "You get 10 minutes of 'Worry Time' each day. That's it!", 'F1', 12, 0.2)
    doc.add_text(72, 680, "If a worry comes at other times, write it down and save it for Worry Time.", 'F1', 12, 0.2)
    y = 645
    doc.add_text(72, y, "My Worry Time is at: _____________ (same time every day)", 'F2', 11, 0)
    y -= 30
    doc.add_text(72, y, "WORRIES I'M SAVING FOR WORRY TIME:", 'F2', 12, 0)
    y -= 22
    for i in range(8):
        doc.add_rect(72, y-3, 468, 25)
        y -= 28
    y -= 10
    doc.add_text(72, y, "When Worry Time is over, I close the box and go do something fun!", 'F2', 11, 0)

    # Pages 16-25: Brave Challenges Log (10 pages)
    for page_num in range(10):
        doc.new_page()
        doc.add_centered_text(740, f"BRAVE CHALLENGES LOG - Page {page_num+1}", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        for entry in range(2):
            doc.add_filled_rect(72, y+2, 468, 16, 0.9)
            doc.add_text(75, y+4, f"Brave Challenge #{page_num*2+entry+1}", 'F2', 10, 0)
            y -= 20
            doc.add_text(72, y, "Date: __________  What I faced: ___________________________________", 'F1', 10, 0.2)
            y -= 22
            doc.add_text(72, y, "How scared I was before (1-10): ___", 'F1', 10, 0.2)
            y -= 22
            doc.add_text(72, y, "How scared I was during (1-10): ___", 'F1', 10, 0.2)
            y -= 22
            doc.add_text(72, y, "How scared I was after (1-10): ___", 'F1', 10, 0.2)
            y -= 22
            doc.add_text(72, y, "What actually happened: ____________________________________________", 'F1', 10, 0.2)
            y -= 22
            doc.add_text(72, y, "Was it as bad as I thought? YES / NO", 'F1', 10, 0.2)
            y -= 22
            doc.add_text(72, y, "I am BRAVE because: _______________________________________________", 'F1', 10, 0.2)
            y -= 35

    # Page 26: Certificate of Bravery
    doc.new_page()
    doc.add_rect(52, 52, 508, 688, 3, 0)
    doc.add_rect(62, 62, 488, 668, 1, 0.5)
    doc.add_centered_text(620, "CERTIFICATE OF BRAVERY", 'F2', 26, 0)
    doc.add_centered_text(560, "This certifies that", 'F4', 14, 0.3)
    doc.add_centered_text(520, "________________________________", 'F1', 16, 0.3)
    doc.add_centered_text(470, "has shown incredible courage by", 'F4', 14, 0.3)
    doc.add_centered_text(440, "facing their fears and doing hard things!", 'F4', 14, 0.3)
    doc.add_centered_text(380, "You are BRAVE. You are STRONG.", 'F2', 16, 0)
    doc.add_centered_text(350, "You are more powerful than your worries!", 'F2', 16, 0)
    doc.add_centered_text(280, "Date: _________________", 'F1', 12, 0.3)
    doc.add_centered_text(240, "Signed: _________________", 'F1', 12, 0.3)

    # Page 27: Parent Guide
    doc.new_page()
    doc.add_centered_text(740, "PARENT GUIDE", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 700
    doc.add_text(72, y, "HOW TO SUPPORT YOUR ANXIOUS CHILD:", 'F2', 12, 0)
    y -= 22
    tips = [
        "Validate their feelings: 'I can see you're scared. That's okay.'",
        "Don't accommodate avoidance - gently encourage facing fears",
        "Model brave behavior and coping out loud",
        "Praise EFFORT, not just outcomes ('You tried! That's so brave!')",
        "Don't promise 'nothing bad will happen' - teach them they can COPE",
        "Keep your own anxiety in check (they mirror you)",
        "Celebrate small victories - every brave step matters",
        "Seek professional help if anxiety interferes with daily life"
    ]
    for t in tips:
        doc.add_text(90, y, f"- {t}", 'F1', 10, 0.2)
        y -= 20
    y -= 15
    doc.add_text(72, y, "WHEN TO SEEK PROFESSIONAL HELP:", 'F2', 12, 0)
    y -= 20
    signs = ["Refuses to go to school", "Can't sleep alone for weeks",
             "Physical symptoms interfere with activities", "Extreme tantrums around feared situations",
             "Anxiety is getting worse, not better"]
    for s in signs:
        doc.add_text(90, y, f"- {s}", 'F1', 10, 0.2)
        y -= 18

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book142_Child_Anxiety_Workbook.pdf')
    print("Book142_Child_Anxiety_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
