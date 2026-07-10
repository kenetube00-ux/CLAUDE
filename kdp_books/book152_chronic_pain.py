"""Book 152: Living with Chronic Pain - A Daily Management Journal"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "LIVING WITH CHRONIC PAIN", 'F2', 18, 0)
    doc.add_centered_text(400, "A Daily Management Journal", 'F4', 14, 0.2)
    doc.add_centered_text(320, "Track | Manage | Advocate | Live", 'F1', 12, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    doc.new_page()
    doc.add_centered_text(500, "LIVING WITH CHRONIC PAIN", 'F2', 14, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)
    doc.add_text(50, 410, "Not a substitute for medical care.", 'F1', 9, 0.3)

    # Page 3: Understanding Chronic Pain
    doc.new_page()
    doc.add_centered_text(590, "UNDERSTANDING CHRONIC PAIN", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Chronic pain is REAL. It is not 'in your head.'", 'F2', 10, 0)
    doc.add_text(50, 537, "Gate Control Theory (simplified):", 'F1', 10, 0.2)
    y = 515
    doc.add_text(50, y, "Your brain has a 'gate' that controls how much pain signal gets through.", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Things that OPEN the gate (more pain): stress, poor sleep, fear, focus", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Things that CLOSE the gate (less pain): relaxation, distraction, movement", 'F1', 9, 0.2)
    y -= 22
    doc.add_text(50, y, "PAIN vs SUFFERING:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "Pain = the physical sensation (you may not control this fully)", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Suffering = the mental/emotional response (you CAN influence this)", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "This journal helps you manage BOTH.", 'F2', 9, 0)

    # Pages 4-33: Daily Tracking (30 pages, 3 entries per page = 90 entries)
    for page_num in range(30):
        doc.new_page()
        doc.add_centered_text(600, f"DAILY PAIN TRACKER - Page {page_num+1}", 'F2', 11, 0)
        doc.add_line(50, 592, 382, 592, 0.5, 0.7)
        y = 578
        for entry in range(3):
            entry_num = page_num * 3 + entry + 1
            doc.add_filled_rect(50, y+2, 332, 12, 0.9)
            doc.add_text(52, y+3, f"Day {entry_num}", 'F2', 7, 0)
            doc.add_text(100, y+3, "Date: ________", 'F1', 7, 0.3)
            y -= 14
            doc.add_text(50, y, "Pain (1-10): ___  Location: ______________  Type: ache/sharp/burn/throb", 'F1', 8, 0.2)
            y -= 12
            doc.add_text(50, y, "Worse: ________________________  Better: _________________________", 'F1', 8, 0.2)
            y -= 12
            doc.add_text(50, y, "Meds: ________________  Mood (1-10): ___  Sleep (hrs): ___  Quality: ___", 'F1', 8, 0.2)
            y -= 12
            doc.add_text(50, y, "Activity level: [ ] Rest [ ] Light [ ] Moderate  Wins despite pain:", 'F1', 8, 0.2)
            y -= 12
            doc.add_text(50, y, "_______________________________________________________________", 'F1', 8, 0.4)
            y -= 20

    # Page 34: Flare-Up Action Plan
    doc.new_page()
    doc.add_centered_text(590, "FLARE-UP ACTION PLAN", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "When pain spikes, follow this plan:", 'F2', 10, 0)
    y -= 20
    steps = [
        "1. STOP what you're doing. Rest is not failure.",
        "2. Medication: Take _______________ (as prescribed)",
        "3. Position: _______________ (best position for my pain)",
        "4. Heat/Ice: _______________ for ___ minutes",
        "5. Breathing: 4-7-8 breathing x 5 rounds",
        "6. Distraction: _______________ (audio book, TV, music)",
        "7. Tell someone: _______________ (so you're not alone)",
        "8. Remind yourself: This will pass. Flares are temporary."
    ]
    for s in steps:
        doc.add_text(50, y, s, 'F1', 9, 0.2)
        y -= 18
    y -= 15
    doc.add_text(50, y, "My emergency comfort kit contains:", 'F2', 9, 0)
    y -= 16
    for i in range(4):
        doc.add_text(50, y, f"_______________________________________________________________", 'F1', 9, 0.4)
        y -= 14

    # Page 35: Pacing Activities
    doc.new_page()
    doc.add_centered_text(590, "PACING ACTIVITIES WORKSHEET", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Pacing = doing activities in manageable chunks with planned rest.", 'F1', 10, 0.2)
    doc.add_text(50, 537, "NOT pushing through pain. NOT resting until you feel 100%.", 'F2', 9, 0)
    y = 510
    doc.add_filled_rect(50, y-2, 332, 16, 0.85)
    doc.add_text(52, y, "Activity", 'F2', 8, 0)
    doc.add_text(160, y, "Current limit", 'F2', 8, 0)
    doc.add_text(250, y, "Paced version", 'F2', 8, 0)
    doc.add_text(340, y, "Rest after", 'F2', 8, 0)
    y -= 18
    for i in range(10):
        doc.add_rect(50, y-2, 332, 18)
        doc.add_line(157, y-2, 157, y+16, 0.3, 0.7)
        doc.add_line(247, y-2, 247, y+16, 0.3, 0.7)
        doc.add_line(337, y-2, 337, y+16, 0.3, 0.7)
        y -= 20
    y -= 10
    doc.add_text(50, y, "Example: Cleaning -> 15 min max -> Break 10 min -> Repeat if able", 'F3', 7, 0.4)

    # Pages 36-38: Doctor Appointment Prep (3 pages)
    for page_num in range(3):
        doc.new_page()
        doc.add_centered_text(590, f"DOCTOR APPOINTMENT PREP ({page_num+1}/3)", 'F2', 12, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 558
        doc.add_text(50, y, "Appointment date: _________  Provider: ___________________________", 'F1', 9, 0.2)
        y -= 20
        doc.add_text(50, y, "Pain since last visit (summary): __________________________________", 'F1', 9, 0.2)
        y -= 14
        doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.3)
        y -= 18
        doc.add_text(50, y, "Average pain level: ___  Worst: ___  Best: ___", 'F1', 9, 0.2)
        y -= 18
        doc.add_text(50, y, "Current medications & are they helping?", 'F2', 9, 0)
        y -= 16
        for i in range(3):
            doc.add_text(50, y, f"  Med: _______________ Dose: ______ Helping? [ ]Yes [ ]No [ ]Somewhat", 'F1', 8, 0.3)
            y -= 14
        y -= 10
        doc.add_text(50, y, "Questions I want to ask:", 'F2', 9, 0)
        y -= 16
        for i in range(4):
            doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 9, 0.3)
            y -= 14
        y -= 10
        doc.add_text(50, y, "What I want them to know: __________________________________________", 'F1', 9, 0.2)
        y -= 14
        doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.3)

    # Page 39: Medication Log
    doc.new_page()
    doc.add_centered_text(590, "MEDICATION LOG", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_filled_rect(50, y-2, 332, 16, 0.85)
    doc.add_text(52, y, "Medication", 'F2', 7, 0)
    doc.add_text(140, y, "Dose", 'F2', 7, 0)
    doc.add_text(185, y, "Frequency", 'F2', 7, 0)
    doc.add_text(250, y, "For", 'F2', 7, 0)
    doc.add_text(300, y, "Side Effects", 'F2', 7, 0)
    y -= 18
    for i in range(15):
        doc.add_rect(50, y-2, 332, 16)
        doc.add_line(137, y-2, 137, y+14, 0.3, 0.7)
        doc.add_line(182, y-2, 182, y+14, 0.3, 0.7)
        doc.add_line(247, y-2, 247, y+14, 0.3, 0.7)
        doc.add_line(297, y-2, 297, y+14, 0.3, 0.7)
        y -= 18

    # Pages 40-42: Pain Acceptance (ACT-based) (3 pages)
    act_pages = [
        ("PAIN ACCEPTANCE: WILLINGNESS", ["Willingness means making room for pain WITHOUT fighting it.",
         "Fighting pain (tensing, bracing, fearing) often makes it WORSE.",
         "", "What would change if I stopped fighting the pain?",
         "_______________________________________________________________",
         "What am I missing by focusing all energy on fighting?",
         "_______________________________________________________________",
         "Can I hold pain AND still do something meaningful today?",
         "_______________________________________________________________"]),
        ("PAIN ACCEPTANCE: VALUES", ["Pain has narrowed my life. What do I still VALUE?",
         "Relationships: ________________________________________________",
         "Activities: ___________________________________________________",
         "Purpose: ______________________________________________________",
         "One small step toward a value TODAY (despite pain):",
         "_______________________________________________________________"]),
        ("PAIN ACCEPTANCE: DEFUSION", ["Thoughts about pain are not COMMANDS.",
         "Instead of 'I can't do anything,' try: 'I'm having the thought that I can't do anything.'",
         "", "A thought about pain I'm fused with:",
         "_______________________________________________________________",
         "Defused version ('I notice I'm having the thought that...'):",
         "_______________________________________________________________",
         "Does this thought serve me? [ ] Yes [ ] No",
         "What would I do if I didn't believe this thought?",
         "_______________________________________________________________"])
    ]
    for title, lines in act_pages:
        doc.new_page()
        doc.add_centered_text(590, title, 'F2', 11, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 555
        for line in lines:
            if line == "":
                y -= 8
            elif line.startswith("___"):
                doc.add_text(50, y, line, 'F1', 9, 0.4)
                y -= 16
            else:
                doc.add_text(50, y, line, 'F1', 9, 0.2)
                y -= 16

    # Page 43: Gratitude Despite Pain
    doc.new_page()
    doc.add_centered_text(590, "GRATITUDE DESPITE PAIN", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "This is not toxic positivity. This is choosing to notice what's ALSO true.", 'F1', 9, 0.2)
    y = 530
    for i in range(15):
        doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 9, 0.3)
        y -= 20
    y -= 10
    doc.add_text(50, y, "Pain is part of my life. It is not ALL of my life.", 'F2', 9, 0)

    # Page 44: Support Network + Movement Menu
    doc.new_page()
    doc.add_centered_text(590, "MY SUPPORT NETWORK & MOVEMENT MENU", 'F2', 11, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "People who understand:", 'F2', 10, 0)
    y -= 16
    for i in range(3):
        doc.add_text(50, y, f"_______________________________________________________________", 'F1', 9, 0.4)
        y -= 14
    y -= 10
    doc.add_text(50, y, "GENTLE MOVEMENT OPTIONS (for low-pain days):", 'F2', 10, 0)
    y -= 16
    movements = ["Gentle stretching (5 min)", "Slow walk (flat surface)", "Chair yoga",
                 "Swimming/water therapy", "Tai chi/qi gong", "Gentle cycling",
                 "Seated exercises", "Deep breathing with movement"]
    for m in movements:
        doc.add_rect(50, y-3, 8, 8)
        doc.add_text(62, y, m, 'F1', 9, 0.2)
        y -= 14
    y -= 10
    doc.add_text(50, y, "Movement I can do even on bad days: ________________________________", 'F1', 9, 0.2)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book152_Chronic_Pain_Journal.pdf')
    print("Book152_Chronic_Pain_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
