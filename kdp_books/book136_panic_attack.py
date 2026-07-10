"""Book 136: Panic Attack Workbook - CBT Tools to Stop Panic in Its Tracks"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(520, "PANIC ATTACK WORKBOOK", 'F2', 28, 0)
    doc.add_centered_text(480, "CBT Tools to Stop Panic in Its Tracks", 'F4', 18, 0.2)
    doc.add_centered_text(420, "Evidence-Based Strategies for", 'F1', 14, 0.3)
    doc.add_centered_text(400, "Managing and Overcoming Panic Disorder", 'F1', 14, 0.3)
    doc.add_centered_text(300, "Includes:", 'F2', 14, 0.2)
    doc.add_centered_text(275, "Interoceptive Exposure Exercises", 'F1', 12, 0.3)
    doc.add_centered_text(255, "Catastrophic Misinterpretation Challenging", 'F1', 12, 0.3)
    doc.add_centered_text(235, "Breathing Retraining Techniques", 'F1', 12, 0.3)
    doc.add_centered_text(215, "Panic Diary & Tracking Tools", 'F1', 12, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(600, "PANIC ATTACK WORKBOOK", 'F2', 14, 0)
    doc.add_centered_text(570, "CBT Tools to Stop Panic in Its Tracks", 'F4', 12, 0.3)
    doc.add_text(72, 500, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.3)
    doc.add_text(72, 480, "No part of this workbook may be reproduced without written permission.", 'F1', 10, 0.3)
    doc.add_text(72, 450, "DISCLAIMER: This workbook is for educational purposes only and is not a", 'F1', 10, 0.3)
    doc.add_text(72, 435, "substitute for professional mental health treatment. If you are experiencing", 'F1', 10, 0.3)
    doc.add_text(72, 420, "severe panic attacks, please seek help from a licensed therapist.", 'F1', 10, 0.3)
    doc.add_text(72, 390, "If you are in crisis, call 988 (Suicide & Crisis Lifeline).", 'F2', 10, 0.3)

    # Page 3: What is Panic Disorder
    doc.new_page()
    doc.add_centered_text(740, "WHAT IS PANIC DISORDER?", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Panic disorder is characterized by recurrent, unexpected panic attacks -", 'F1', 11, 0.2)
    doc.add_text(72, 683, "sudden surges of intense fear that reach a peak within minutes.", 'F1', 11, 0.2)
    doc.add_text(72, 650, "Common symptoms include:", 'F2', 12, 0.1)
    symptoms = ["Racing or pounding heart", "Sweating, trembling, or shaking",
                "Shortness of breath or feeling smothered", "Chest pain or discomfort",
                "Nausea or stomach distress", "Dizziness or lightheadedness",
                "Chills or hot flashes", "Numbness or tingling",
                "Feeling detached from yourself (derealization)", "Fear of losing control or dying"]
    y = 625
    for s in symptoms:
        doc.add_text(90, y, f"- {s}", 'F1', 11, 0.2)
        y -= 18
    doc.add_text(72, y-20, "Key Point: Panic attacks are NOT dangerous. They are your body's", 'F2', 11, 0)
    doc.add_text(72, y-38, "fight-or-flight system misfiring. You will NOT die, go crazy, or faint.", 'F2', 11, 0)

    # Page 4: The Panic Cycle
    doc.new_page()
    doc.add_centered_text(740, "THE PANIC CYCLE EXPLAINED", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Understanding the cycle keeps you trapped:", 'F2', 12, 0.1)
    doc.add_text(100, 670, "1. TRIGGER: A body sensation or situation", 'F1', 11, 0.2)
    doc.add_text(100, 645, "2. CATASTROPHIC THOUGHT: 'I'm having a heart attack!'", 'F1', 11, 0.2)
    doc.add_text(100, 620, "3. ANXIETY INCREASES: More adrenaline released", 'F1', 11, 0.2)
    doc.add_text(100, 595, "4. MORE BODY SENSATIONS: Heart races faster, breathing changes", 'F1', 11, 0.2)
    doc.add_text(100, 570, "5. MORE CATASTROPHIC THOUGHTS: 'Something is really wrong!'", 'F1', 11, 0.2)
    doc.add_text(100, 545, "6. FULL PANIC ATTACK: Peak fear, intense symptoms", 'F1', 11, 0.2)
    doc.add_text(100, 520, "7. AVOIDANCE: You avoid similar situations next time", 'F1', 11, 0.2)
    doc.add_text(100, 495, "8. CYCLE STRENGTHENS: Avoidance confirms danger belief", 'F1', 11, 0.2)
    doc.add_rect(80, 480, 450, 250, 1, 0.5)
    doc.add_text(72, 450, "BREAKING THE CYCLE:", 'F2', 12, 0)
    doc.add_text(72, 425, "This workbook targets steps 2 & 7. By changing your interpretation", 'F1', 11, 0.2)
    doc.add_text(72, 408, "of symptoms and facing feared situations, the cycle breaks.", 'F1', 11, 0.2)

    # Page 5: Body Sensations Log
    doc.new_page()
    doc.add_centered_text(740, "BODY SENSATIONS LOG", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Track your body sensations and the thoughts they trigger:", 'F1', 11, 0.2)
    headers = ["Sensation", "Catastrophic Thought", "Rational Alternative", "Anxiety (0-10)"]
    x_positions = [72, 185, 330, 490]
    widths = [110, 140, 155, 60]
    doc.add_filled_rect(72, 670, 468, 20, 0.85)
    for i, h in enumerate(headers):
        doc.add_text(x_positions[i]+3, 675, h, 'F2', 9, 0)
    y = 650
    for row in range(12):
        for i in range(4):
            doc.add_rect(x_positions[i], y, widths[i], 35)
        y -= 37
    doc.add_text(72, y-10, "Example: Heart racing -> 'Heart attack!' -> 'Exercise does this too, it's adrenaline' -> 6", 'F3', 8, 0.4)

    # Pages 6-10: Interoceptive Exposure Exercises (5 pages)
    exercises = [
        ("SPINNING IN A CHAIR", "Spin in an office chair for 60 seconds",
         ["Creates dizziness and disorientation", "Mimics lightheadedness during panic",
          "Shows you that dizziness is temporary and safe"]),
        ("BREATHING THROUGH A STRAW", "Breathe only through a thin straw for 60 seconds",
         ["Creates sensation of restricted breathing", "Mimics 'can't get enough air' feeling",
          "Proves you won't suffocate"]),
        ("HYPERVENTILATION", "Breathe rapidly and deeply for 30 seconds",
         ["Creates tingling, lightheadedness, chest tightness", "Mimics many panic symptoms directly",
          "Shows symptoms pass quickly when you stop"]),
        ("RUNNING IN PLACE", "Run in place vigorously for 60 seconds",
         ["Creates racing heart, sweating, breathlessness", "Mimics cardiac symptoms of panic",
          "Proves racing heart is normal and safe"]),
        ("BREATH HOLDING", "Hold your breath for 30 seconds",
         ["Creates chest pressure and urge to breathe", "Mimics suffocation fear",
          "Shows your body will breathe automatically"])
    ]
    for ex_name, instruction, points in exercises:
        doc.new_page()
        doc.add_centered_text(740, f"INTEROCEPTIVE EXPOSURE: {ex_name}", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        doc.add_text(72, 700, f"Exercise: {instruction}", 'F2', 11, 0.1)
        y = 670
        for p in points:
            doc.add_text(90, y, f"- {p}", 'F1', 11, 0.2)
            y -= 18
        doc.add_text(72, y-15, "SUDS RATINGS (Subjective Units of Distress Scale, 0-10):", 'F2', 11, 0)
        y -= 45
        doc.add_text(72, y, "Trial 1:", 'F1', 11, 0.2)
        doc.add_text(130, y, "Before: ___   During (peak): ___   After 1 min: ___   After 3 min: ___", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "Trial 2:", 'F1', 11, 0.2)
        doc.add_text(130, y, "Before: ___   During (peak): ___   After 1 min: ___   After 3 min: ___", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "Trial 3:", 'F1', 11, 0.2)
        doc.add_text(130, y, "Before: ___   During (peak): ___   After 1 min: ___   After 3 min: ___", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "Trial 4:", 'F1', 11, 0.2)
        doc.add_text(130, y, "Before: ___   During (peak): ___   After 1 min: ___   After 3 min: ___", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "Trial 5:", 'F1', 11, 0.2)
        doc.add_text(130, y, "Before: ___   During (peak): ___   After 1 min: ___   After 3 min: ___", 'F1', 11, 0.2)
        y -= 50
        doc.add_text(72, y, "Sensations experienced: ________________________________________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "Similarity to panic (0-10): ___", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "What I learned: _______________________________________________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)

    # Pages 11-15: Catastrophic Misinterpretation Challenging (5 pages)
    for page_num in range(5):
        doc.new_page()
        doc.add_centered_text(740, f"CATASTROPHIC MISINTERPRETATION CHALLENGING ({page_num+1}/5)", 'F2', 13, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 700
        doc.add_text(72, y, "Body Sensation: ______________________________________________________", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "My Catastrophic Interpretation: _______________________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "Evidence FOR this interpretation:", 'F2', 11, 0.1)
        for i in range(3):
            y -= 22
            doc.add_text(90, y, f"{i+1}. ___________________________________________________________", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "Evidence AGAINST this interpretation:", 'F2', 11, 0.1)
        for i in range(3):
            y -= 22
            doc.add_text(90, y, f"{i+1}. ___________________________________________________________", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "Alternative explanation (rational): ____________________________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "How many times have I had this sensation without dying/going crazy? ___", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "What would I tell a friend who had this thought? _____________________", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
        y -= 35
        doc.add_text(72, y, "Belief in catastrophic thought BEFORE (0-100%): ___", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "Belief in catastrophic thought AFTER (0-100%): ___", 'F1', 11, 0.2)

    # Page 16: Safety Behavior Reduction
    doc.new_page()
    doc.add_centered_text(740, "SAFETY BEHAVIOR REDUCTION PLAN", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Safety behaviors maintain panic by preventing you from learning it's safe.", 'F1', 11, 0.2)
    doc.add_text(72, 680, "Common safety behaviors:", 'F2', 11, 0.1)
    behaviors = ["Carrying medication 'just in case'", "Always sitting near exits",
                 "Avoiding being alone", "Checking pulse constantly",
                 "Deep breathing at first sign of anxiety", "Avoiding exercise or caffeine"]
    y = 660
    for b in behaviors:
        doc.add_text(90, y, f"- {b}", 'F1', 10, 0.3)
        y -= 16
    y -= 15
    doc.add_text(72, y, "MY SAFETY BEHAVIORS TO REDUCE:", 'F2', 12, 0)
    y -= 25
    headers2 = ["Safety Behavior", "Why I Do It", "Drop Date", "What Happened"]
    x_pos2 = [72, 210, 350, 430]
    w2 = [135, 137, 77, 110]
    doc.add_filled_rect(72, y-5, 468, 20, 0.85)
    for i, h in enumerate(headers2):
        doc.add_text(x_pos2[i]+3, y, h, 'F2', 9, 0)
    y -= 30
    for row in range(8):
        for i in range(4):
            doc.add_rect(x_pos2[i], y, w2[i], 35)
        y -= 37

    # Page 17: Breathing Retraining
    doc.new_page()
    doc.add_centered_text(740, "BREATHING RETRAINING", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "4-7-8 BREATHING TECHNIQUE:", 'F2', 14, 0)
    doc.add_text(90, 675, "1. Exhale completely through your mouth", 'F1', 11, 0.2)
    doc.add_text(90, 655, "2. Inhale quietly through your nose for 4 counts", 'F1', 11, 0.2)
    doc.add_text(90, 635, "3. Hold your breath for 7 counts", 'F1', 11, 0.2)
    doc.add_text(90, 615, "4. Exhale completely through your mouth for 8 counts", 'F1', 11, 0.2)
    doc.add_text(90, 595, "5. Repeat 4 times", 'F1', 11, 0.2)
    doc.add_text(72, 555, "DIAPHRAGMATIC BREATHING:", 'F2', 14, 0)
    doc.add_text(90, 530, "1. Place one hand on chest, one on belly", 'F1', 11, 0.2)
    doc.add_text(90, 510, "2. Breathe in slowly - belly hand should rise, chest hand stays still", 'F1', 11, 0.2)
    doc.add_text(90, 490, "3. Exhale slowly - belly falls back", 'F1', 11, 0.2)
    doc.add_text(90, 470, "4. Practice 5 minutes, 3 times daily (NOT just during panic)", 'F1', 11, 0.2)
    doc.add_text(72, 430, "PRACTICE LOG:", 'F2', 12, 0)
    doc.add_filled_rect(72, 405, 468, 18, 0.85)
    doc.add_text(75, 408, "Date", 'F2', 9, 0)
    doc.add_text(140, 408, "Technique", 'F2', 9, 0)
    doc.add_text(240, 408, "Duration", 'F2', 9, 0)
    doc.add_text(320, 408, "Before (0-10)", 'F2', 9, 0)
    doc.add_text(420, 408, "After (0-10)", 'F2', 9, 0)
    y = 385
    for i in range(10):
        doc.add_rect(72, y, 468, 25)
        y -= 27

    # Page 18: Progressive Muscle Relaxation
    doc.new_page()
    doc.add_centered_text(740, "PROGRESSIVE MUSCLE RELAXATION SCRIPT", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Tense each muscle group for 5 seconds, then release for 10 seconds.", 'F1', 11, 0.2)
    doc.add_text(72, 685, "Notice the contrast between tension and relaxation.", 'F1', 11, 0.2)
    muscle_groups = [
        ("1. Hands & Forearms:", "Make fists, squeeze tight"),
        ("2. Upper Arms:", "Bend elbows, flex biceps"),
        ("3. Shoulders:", "Shrug shoulders up to ears"),
        ("4. Forehead:", "Raise eyebrows high"),
        ("5. Eyes & Cheeks:", "Squeeze eyes shut tight"),
        ("6. Mouth & Jaw:", "Clench jaw, press lips together"),
        ("7. Neck:", "Press head back gently"),
        ("8. Chest:", "Take deep breath, hold"),
        ("9. Stomach:", "Tighten abdominal muscles"),
        ("10. Back:", "Arch back slightly"),
        ("11. Thighs:", "Press legs together, tighten"),
        ("12. Calves:", "Point toes up toward shins"),
        ("13. Feet:", "Curl toes under")
    ]
    y = 655
    for group, instr in muscle_groups:
        doc.add_text(72, y, group, 'F2', 11, 0.1)
        doc.add_text(220, y, instr, 'F1', 11, 0.2)
        y -= 22
    y -= 20
    doc.add_text(72, y, "Total time: approximately 15-20 minutes. Practice daily for best results.", 'F2', 11, 0)

    # Pages 19-28: Panic Diary (10 pages)
    for page_num in range(10):
        doc.new_page()
        doc.add_centered_text(740, f"PANIC DIARY - Page {page_num+1}", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 700
        for entry in range(2):
            doc.add_filled_rect(72, y+2, 468, 16, 0.88)
            doc.add_text(75, y+4, f"Entry {page_num*2 + entry + 1}", 'F2', 10, 0.2)
            y -= 20
            doc.add_text(72, y, "Date: ____________  Time: ________  Duration: ________ min", 'F1', 10, 0.2)
            y -= 20
            doc.add_text(72, y, "Situation/Where I was: _____________________________________________", 'F1', 10, 0.2)
            y -= 20
            doc.add_text(72, y, "Symptoms (circle): Heart racing / Dizzy / Sweating / Chest pain / Numb /", 'F1', 10, 0.2)
            y -= 16
            doc.add_text(72, y, "   Shaking / Breathless / Nausea / Hot/Cold / Detached / Other: _______", 'F1', 10, 0.2)
            y -= 20
            doc.add_text(72, y, "Peak anxiety (0-10): ___    Catastrophic thought: ___________________", 'F1', 10, 0.2)
            y -= 20
            doc.add_text(72, y, "What I did (coping): ______________________________________________", 'F1', 10, 0.2)
            y -= 20
            doc.add_text(72, y, "Outcome: __________________________________________________________", 'F1', 10, 0.2)
            y -= 20
            doc.add_text(72, y, "What I learned: ___________________________________________________", 'F1', 10, 0.2)
            y -= 35
            doc.add_line(72, y+10, 540, y+10, 0.5, 0.7)
            y -= 10

    # Page 29: Agoraphobia Hierarchy
    doc.new_page()
    doc.add_centered_text(740, "AGORAPHOBIA EXPOSURE HIERARCHY", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "List situations you avoid due to panic fear, from least to most scary:", 'F1', 11, 0.2)
    y = 670
    for i in range(10):
        anxiety_level = (i + 1) * 10
        doc.add_filled_rect(72, y-2, 30, 18, 0.7 + (0.02 * (10-i)))
        doc.add_text(78, y, f"{anxiety_level}", 'F2', 10, 0)
        doc.add_text(110, y, f"{'_'*60}", 'F1', 11, 0.2)
        y -= 30
    y -= 20
    doc.add_text(72, y, "Start with lowest item. Practice until anxiety drops by 50%, then move up.", 'F2', 11, 0)
    y -= 30
    doc.add_text(72, y, "PROGRESS NOTES:", 'F2', 12, 0)
    y -= 25
    for i in range(6):
        doc.add_text(72, y, "Date: _______  Situation: _______________________  SUDS: before ___ after ___", 'F1', 10, 0.2)
        y -= 22

    # Page 30: Panic Toolkit + Relapse Prevention
    doc.new_page()
    doc.add_centered_text(740, "MY PANIC TOOLKIT & RELAPSE PREVENTION", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "MY PANIC TOOLKIT (what works for me):", 'F2', 12, 0)
    y = 680
    for i in range(5):
        doc.add_text(72, y, f"{i+1}. _________________________________________________________________", 'F1', 11, 0.2)
        y -= 25
    y -= 15
    doc.add_text(72, y, "RELAPSE PREVENTION PLAN:", 'F2', 12, 0)
    y -= 25
    doc.add_text(72, y, "Early warning signs that panic is returning:", 'F1', 11, 0.2)
    y -= 20
    for i in range(3):
        doc.add_text(90, y, f"- ________________________________________________________________", 'F1', 11, 0.2)
        y -= 20
    y -= 10
    doc.add_text(72, y, "If panic returns, I will:", 'F1', 11, 0.2)
    y -= 20
    for i in range(3):
        doc.add_text(90, y, f"- ________________________________________________________________", 'F1', 11, 0.2)
        y -= 20
    y -= 10
    doc.add_text(72, y, "My therapist/support person to contact: _________________________________", 'F1', 11, 0.2)
    y -= 30
    doc.add_text(72, y, "REMEMBER:", 'F2', 14, 0)
    y -= 25
    doc.add_text(72, y, "- A panic attack has NEVER killed anyone", 'F2', 11, 0)
    y -= 20
    doc.add_text(72, y, "- Symptoms ALWAYS pass (usually within 10-20 minutes)", 'F2', 11, 0)
    y -= 20
    doc.add_text(72, y, "- You have survived 100% of your worst days", 'F2', 11, 0)
    y -= 20
    doc.add_text(72, y, "- Recovery is not linear - setbacks are normal, not failures", 'F2', 11, 0)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book136_Panic_Attack_Workbook.pdf')
    print("Book136_Panic_Attack_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
