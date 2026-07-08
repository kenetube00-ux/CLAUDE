"""Book 81: CBT Workbook for Anxiety"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.15)
    pdf.add_centered_text(520, "CBT WORKBOOK", 'F2', 32, 1)
    pdf.add_centered_text(480, "FOR ANXIETY", 'F2', 32, 1)
    pdf.add_centered_text(430, "Evidence-Based Exercises to Calm Your Mind", 'F4', 16, 0.9)
    pdf.add_centered_text(350, "A Practical Guide with Worksheets,", 'F1', 13, 0.8)
    pdf.add_centered_text(330, "Thought Records & Behavioral Experiments", 'F1', 13, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    pdf.add_centered_text(170, "Licensed CBT Techniques for Self-Help", 'F1', 11, 0.7)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "CBT Workbook for Anxiety", 'F2', 14)
    pdf.add_centered_text(475, "Evidence-Based Exercises to Calm Your Mind", 'F4', 11)
    pdf.add_centered_text(440, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(390, "This workbook is for educational purposes only.", 'F1', 9)
    pdf.add_centered_text(370, "It is not a substitute for professional mental health treatment.", 'F1', 9)
    pdf.add_centered_text(340, "If you are in crisis, call 988 Suicide & Crisis Lifeline.", 'F2', 9)
    
    # Chapter 1: What is CBT
    pdf.new_page()
    pdf.add_centered_text(740, "CHAPTER 1: WHAT IS CBT?", 'F2', 18)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 700
    cbt_text = [
        "Cognitive Behavioral Therapy (CBT) is an evidence-based psychological",
        "treatment that has been proven effective for anxiety disorders.",
        "",
        "The core principle of CBT is that our THOUGHTS affect our FEELINGS,",
        "which in turn affect our BEHAVIORS. By changing unhelpful thought",
        "patterns, we can reduce anxiety and improve our quality of life.",
        "",
        "THE CBT TRIANGLE:",
        "",
        "  THOUGHTS (what we think)",
        "       |",
        "  FEELINGS (what we feel emotionally and physically)",
        "       |",
        "  BEHAVIORS (what we do or avoid)",
        "",
        "HOW THIS WORKBOOK WORKS:",
        "",
        "1. You will learn to IDENTIFY your anxious thoughts",
        "2. You will EXAMINE the evidence for and against these thoughts",
        "3. You will CHALLENGE cognitive distortions",
        "4. You will CREATE balanced, realistic alternatives",
        "5. You will EXPERIMENT with new behaviors",
        "",
        "CBT is not about positive thinking - it is about REALISTIC thinking.",
        "You will learn to evaluate your thoughts like a scientist,",
        "testing hypotheses rather than accepting anxious predictions as facts.",
    ]
    for line in cbt_text:
        pdf.add_text(72, y, line, 'F4', 11)
        y -= 18
    
    # Chapter 2: Identifying Anxiety Triggers
    pdf.new_page()
    pdf.add_centered_text(740, "CHAPTER 2: IDENTIFYING ANXIETY TRIGGERS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 700, "Understanding what triggers your anxiety is the first step to managing it.", 'F4', 11)
    pdf.add_text(72, 680, "List your top anxiety triggers below:", 'F1', 11)
    y = 650
    for i in range(1, 11):
        pdf.add_text(72, y, f"{i}.", 'F2', 11)
        pdf.add_line(95, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 30
    pdf.add_text(72, y - 10, "For each trigger, rate intensity (1-10):", 'F2', 11)
    y -= 40
    pdf.add_text(72, y, "Trigger:", 'F1', 10)
    pdf.add_text(300, y, "Intensity:", 'F1', 10)
    pdf.add_text(420, y, "Frequency:", 'F1', 10)
    y -= 20
    for i in range(8):
        pdf.add_line(72, y, 280, y, 0.5, 0.5)
        pdf.add_line(300, y, 400, y, 0.5, 0.5)
        pdf.add_line(420, y, 540, y, 0.5, 0.5)
        y -= 25

    # Thought Record pages (5 pages)
    for page_num in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(750, f"THOUGHT RECORD - Page {page_num}", 'F2', 14)
        pdf.add_line(72, 742, 540, 742, 1, 0.3)
        pdf.add_text(72, 720, "Date: _______________    Time: ___________    Situation: _________________________", 'F1', 9)
        headers = ["SITUATION", "AUTOMATIC", "EMOTION", "EVIDENCE", "BALANCED"]
        sub_headers = ["(What happened?)", "THOUGHT", "(0-100%)", "FOR/AGAINST", "THOUGHT"]
        col_w = 95
        start_x = 72
        for i, (h, s) in enumerate(zip(headers, sub_headers)):
            x = start_x + i * col_w
            pdf.add_text(x + 2, 690, h, 'F2', 8)
            pdf.add_text(x + 2, 678, s, 'F1', 7)
            pdf.add_rect(x, 580, col_w, 110, 0.5, 0.4)
        # Second row
        for i in range(5):
            x = start_x + i * col_w
            pdf.add_rect(x, 460, col_w, 110, 0.5, 0.4)
        # Third row
        for i in range(5):
            x = start_x + i * col_w
            pdf.add_rect(x, 340, col_w, 110, 0.5, 0.4)
        pdf.add_text(72, 310, "What I learned from this thought record:", 'F2', 10)
        for i in range(4):
            pdf.add_line(72, 290 - i*22, 540, 290 - i*22, 0.5, 0.5)
        pdf.add_text(72, 190, "New behavior I will try based on my balanced thought:", 'F2', 10)
        for i in range(3):
            pdf.add_line(72, 170 - i*22, 540, 170 - i*22, 0.5, 0.5)

    # Cognitive Distortions page
    pdf.new_page()
    pdf.add_centered_text(740, "10 COMMON COGNITIVE DISTORTIONS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    distortions = [
        ("1. All-or-Nothing Thinking", "Seeing things in black-and-white. Example: 'If I'm not perfect, I'm a failure.'"),
        ("2. Catastrophizing", "Expecting the worst outcome. Example: 'This headache must be a brain tumor.'"),
        ("3. Mind Reading", "Assuming you know what others think. Example: 'They think I'm stupid.'"),
        ("4. Fortune Telling", "Predicting negative outcomes. Example: 'I'll definitely fail the interview.'"),
        ("5. Emotional Reasoning", "Feelings = facts. Example: 'I feel anxious, so something bad will happen.'"),
        ("6. Should Statements", "Rigid rules. Example: 'I should never make mistakes.'"),
        ("7. Labeling", "Defining self by one event. Example: 'I'm a loser' after one setback."),
        ("8. Magnification/Minimization", "Blowing up negatives, shrinking positives."),
        ("9. Overgeneralization", "One event = always. Example: 'I always mess things up.'"),
        ("10. Personalization", "Blaming yourself for everything. Example: 'It's all my fault.'"),
    ]
    y = 705
    for title, desc in distortions:
        pdf.add_text(72, y, title, 'F2', 10)
        y -= 15
        pdf.add_text(90, y, desc, 'F4', 9)
        y -= 28

    # Challenging Negative Thoughts (3 pages)
    for pg in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(740, f"CHALLENGING NEGATIVE THOUGHTS - Exercise {pg}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        pdf.add_text(72, 705, "My anxious thought:", 'F2', 11)
        pdf.add_line(72, 685, 540, 685, 0.5, 0.5)
        pdf.add_line(72, 665, 540, 665, 0.5, 0.5)
        pdf.add_text(72, 640, "Evidence SUPPORTING this thought:", 'F2', 11)
        for i in range(3):
            pdf.add_line(72, 620 - i*20, 540, 620 - i*20, 0.5, 0.5)
        pdf.add_text(72, 550, "Evidence AGAINST this thought:", 'F2', 11)
        for i in range(3):
            pdf.add_line(72, 530 - i*20, 540, 530 - i*20, 0.5, 0.5)
        pdf.add_text(72, 460, "Which cognitive distortion is at play?", 'F2', 11)
        pdf.add_line(72, 440, 540, 440, 0.5, 0.5)
        pdf.add_text(72, 415, "What would I tell a friend with this thought?", 'F2', 11)
        pdf.add_line(72, 395, 540, 395, 0.5, 0.5)
        pdf.add_line(72, 375, 540, 375, 0.5, 0.5)
        pdf.add_text(72, 350, "My balanced, realistic alternative thought:", 'F2', 11)
        pdf.add_line(72, 330, 540, 330, 0.5, 0.5)
        pdf.add_line(72, 310, 540, 310, 0.5, 0.5)
        pdf.add_text(72, 280, "How much do I believe the original thought now? (0-100%): _______", 'F1', 10)
        pdf.add_text(72, 260, "Emotion intensity now (0-100%): _______", 'F1', 10)

    # Behavioral Experiments Planner (3 pages)
    for pg in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(740, f"BEHAVIORAL EXPERIMENT PLANNER - #{pg}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        fields = [
            ("Anxious prediction (what I think will happen):", 3),
            ("How strongly I believe this (0-100%):", 1),
            ("The experiment (what I will do to test this):", 3),
            ("When and where:", 1),
            ("What actually happened:", 4),
            ("What I learned:", 3),
            ("Belief in prediction now (0-100%):", 1),
        ]
        y = 700
        for label, lines in fields:
            pdf.add_text(72, y, label, 'F2', 10)
            y -= 18
            for _ in range(lines):
                pdf.add_line(72, y, 540, y, 0.5, 0.5)
                y -= 20
            y -= 10

    # Exposure Hierarchy (2 pages)
    for pg in range(1, 3):
        pdf.new_page()
        pdf.add_centered_text(740, f"EXPOSURE HIERARCHY WORKSHEET - Page {pg}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        pdf.add_text(72, 705, "List feared situations from LEAST to MOST anxiety-provoking (SUDS 0-100):", 'F1', 10)
        pdf.add_text(72, 680, "SUDS", 'F2', 9)
        pdf.add_text(120, 680, "Feared Situation", 'F2', 9)
        pdf.add_text(420, 680, "Date Attempted", 'F2', 9)
        y = 660
        for i in range(10):
            suds = (i + 1) * 10 if pg == 1 else (i + 1) * 10
            pdf.add_text(72, y, f"{suds}", 'F1', 9)
            pdf.add_line(120, y - 2, 400, y - 2, 0.5, 0.5)
            pdf.add_line(420, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 30

    # Relaxation: Progressive Muscle Relaxation
    pdf.new_page()
    pdf.add_centered_text(740, "PROGRESSIVE MUSCLE RELAXATION SCRIPT", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pmr_text = [
        "Find a comfortable position. Close your eyes. Take three deep breaths.",
        "",
        "FEET: Curl your toes tightly. Hold 5 seconds. Release. Notice the difference.",
        "CALVES: Point your toes up toward your shins. Hold 5 sec. Release.",
        "THIGHS: Squeeze your thigh muscles. Hold 5 seconds. Release.",
        "STOMACH: Tighten your abdominal muscles. Hold 5 seconds. Release.",
        "CHEST: Take a deep breath and hold it. Hold 5 seconds. Exhale slowly.",
        "HANDS: Make tight fists. Hold 5 seconds. Release. Spread fingers wide.",
        "ARMS: Flex your biceps. Hold 5 seconds. Release.",
        "SHOULDERS: Shrug shoulders to your ears. Hold 5 seconds. Drop them.",
        "NECK: Gently press head back. Hold 5 seconds. Release.",
        "FACE: Scrunch your entire face. Hold 5 seconds. Release.",
        "",
        "Now scan your body from feet to head. Notice any remaining tension.",
        "Breathe into those areas. Allow your whole body to feel heavy and warm.",
        "",
        "Practice daily for best results. Duration: 15-20 minutes.",
        "",
        "MY PMR PRACTICE LOG:",
        "Date          Before (1-10)    After (1-10)    Notes",
    ]
    y = 705
    for line in pmr_text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    for i in range(8):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 20

    # Breathing Exercises
    pdf.new_page()
    pdf.add_centered_text(740, "BREATHING EXERCISES", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 700, "THE 4-7-8 TECHNIQUE (Dr. Andrew Weil)", 'F2', 12)
    breathing = [
        "",
        "1. Exhale completely through your mouth, making a whoosh sound.",
        "2. Close your mouth and inhale quietly through your nose for 4 counts.",
        "3. Hold your breath for 7 counts.",
        "4. Exhale completely through your mouth for 8 counts.",
        "5. This is one breath cycle. Repeat 3 more times (4 cycles total).",
        "",
        "Practice twice daily. It becomes more effective with repetition.",
        "",
    ]
    y = 680
    for line in breathing:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17
    pdf.add_text(72, y, "BOX BREATHING (Navy SEAL Technique)", 'F2', 12)
    y -= 20
    box = [
        "1. Breathe IN for 4 counts",
        "2. HOLD for 4 counts",
        "3. Breathe OUT for 4 counts", 
        "4. HOLD for 4 counts",
        "Repeat 4-6 cycles.",
    ]
    for line in box:
        pdf.add_text(90, y, line, 'F4', 10)
        y -= 17
    y -= 20
    pdf.add_text(72, y, "DIAPHRAGMATIC BREATHING", 'F2', 12)
    y -= 20
    dia = [
        "1. Place one hand on chest, one on belly.",
        "2. Breathe in slowly - only belly hand should rise.",
        "3. Exhale slowly - belly falls. Chest stays still.",
        "4. Practice 5-10 minutes daily.",
    ]
    for line in dia:
        pdf.add_text(90, y, line, 'F4', 10)
        y -= 17

    # Worry Time Scheduling
    pdf.new_page()
    pdf.add_centered_text(740, "WORRY TIME SCHEDULING", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Designate 15-20 minutes daily as your 'worry time.'", 'F2', 11)
    pdf.add_text(72, 685, "Outside this time, write worries down and postpone them.", 'F1', 10)
    pdf.add_text(72, 660, "My designated worry time: ________ to ________", 'F1', 11)
    pdf.add_text(72, 640, "Location: _________________________________", 'F1', 11)
    pdf.add_text(72, 610, "TODAY'S WORRY LIST:", 'F2', 12)
    pdf.add_text(72, 592, "Worry", 'F2', 9)
    pdf.add_text(350, 592, "Can I control it?", 'F2', 9)
    pdf.add_text(470, 592, "Action step", 'F2', 9)
    y = 575
    for i in range(12):
        pdf.add_line(72, y, 340, y, 0.5, 0.5)
        pdf.add_line(350, y, 460, y, 0.5, 0.5)
        pdf.add_line(470, y, 540, y, 0.5, 0.5)
        y -= 25
    pdf.add_text(72, y - 10, "After worry time, rate your anxiety (1-10): _____", 'F1', 10)
    pdf.add_text(72, y - 30, "Did any worries feel less important by worry time? (circle) YES / NO", 'F1', 10)

    # Safety Behaviors Identification
    pdf.new_page()
    pdf.add_centered_text(740, "SAFETY BEHAVIORS IDENTIFICATION", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "Safety behaviors are things we do to prevent feared outcomes.", 'F1', 10)
    pdf.add_text(72, 688, "They maintain anxiety by preventing us from learning the truth.", 'F1', 10)
    pdf.add_text(72, 660, "MY SAFETY BEHAVIORS:", 'F2', 12)
    y = 635
    headers_sb = ["Situation", "Safety Behavior", "What I fear without it", "Drop it? (Y/N)"]
    xs = [72, 200, 340, 480]
    for i, h in enumerate(headers_sb):
        pdf.add_text(xs[i], y, h, 'F2', 8)
    y -= 18
    for row in range(10):
        for x_pos in xs:
            pdf.add_line(x_pos, y, x_pos + 110 if x_pos < 480 else x_pos + 50, y, 0.5, 0.5)
        y -= 28

    # Graded Exposure Ladder
    pdf.new_page()
    pdf.add_centered_text(740, "GRADED EXPOSURE LADDER", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 705, "My feared situation: ___________________________________________", 'F1', 11)
    pdf.add_text(72, 680, "Build steps from EASIEST (bottom) to HARDEST (top):", 'F1', 10)
    y = 640
    for step in range(10, 0, -1):
        pdf.add_filled_rect(100, y - 5, 400, 25, 0.92)
        pdf.add_text(80, y, f"{step}.", 'F2', 11)
        pdf.add_line(110, y - 2, 490, y - 2, 0.5, 0.5)
        pdf.add_text(500, y, "SUDS:___", 'F1', 8)
        y -= 35
    pdf.add_text(72, y - 10, "Start at step 1. Move up only when SUDS drops to 3 or below.", 'F2', 9)

    # Weekly Mood Tracker (4 pages)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for wk in range(1, 5):
        pdf.new_page()
        pdf.add_centered_text(740, f"WEEKLY MOOD TRACKER - Week {wk}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        pdf.add_text(72, 710, "Rate each item 1-10 daily:", 'F1', 10)
        headers_m = ["Day", "Anxiety", "Mood", "Sleep", "Exercise", "Social", "CBT Done?"]
        xs_m = [72, 120, 180, 240, 310, 380, 450]
        for i, h in enumerate(headers_m):
            pdf.add_text(xs_m[i], 685, h, 'F2', 9)
        y = 665
        for day in days:
            pdf.add_text(72, y, day, 'F1', 10)
            for x_pos in xs_m[1:]:
                pdf.add_line(x_pos, y - 2, x_pos + 45, y - 2, 0.5, 0.5)
            y -= 28
        pdf.add_text(72, y - 10, "Week's biggest challenge:", 'F2', 10)
        pdf.add_line(72, y - 30, 540, y - 30, 0.5, 0.5)
        pdf.add_text(72, y - 50, "Week's biggest win:", 'F2', 10)
        pdf.add_line(72, y - 70, 540, y - 70, 0.5, 0.5)
        pdf.add_text(72, y - 90, "What I will do differently next week:", 'F2', 10)
        pdf.add_line(72, y - 110, 540, y - 110, 0.5, 0.5)
        pdf.add_line(72, y - 130, 540, y - 130, 0.5, 0.5)

    # Relapse Prevention Plan
    pdf.new_page()
    pdf.add_centered_text(740, "RELAPSE PREVENTION PLAN", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    fields_rp = [
        ("My early warning signs that anxiety is returning:", 3),
        ("My known triggers:", 3),
        ("CBT skills that work best for me:", 3),
        ("My coping statements:", 3),
        ("People I can reach out to:", 3),
        ("Professional support contacts:", 2),
        ("My self-care non-negotiables:", 3),
        ("If I notice a setback, I will:", 3),
    ]
    y = 705
    for label, lines in fields_rp:
        pdf.add_text(72, y, label, 'F2', 10)
        y -= 16
        for _ in range(lines):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 8

    # 30-Day CBT Challenge Checklist
    pdf.new_page()
    pdf.add_centered_text(740, "30-DAY CBT CHALLENGE", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    pdf.add_text(72, 710, "Complete one challenge each day. Check off when done.", 'F1', 10)
    challenges = [
        "Day 1: Write down 3 anxious thoughts you had today",
        "Day 2: Identify the cognitive distortion in each thought",
        "Day 3: Practice 4-7-8 breathing 3 times today",
        "Day 4: Complete one full thought record",
        "Day 5: List 5 things you are avoiding due to anxiety",
        "Day 6: Do one thing from your avoidance list (easiest)",
        "Day 7: Practice progressive muscle relaxation",
        "Day 8: Challenge one 'should' statement",
        "Day 9: Write evidence for AND against your biggest worry",
        "Day 10: Set up your daily worry time",
        "Day 11: Notice and record 3 safety behaviors",
        "Day 12: Drop one safety behavior today",
        "Day 13: Practice box breathing before a stressful event",
        "Day 14: Complete a behavioral experiment",
        "Day 15: MID-POINT CHECK-IN - Rate anxiety now vs Day 1",
        "Day 16: Practice 'observe without judgment' for 5 min",
        "Day 17: Write a compassionate letter to your anxious self",
        "Day 18: Identify your #1 core belief driving anxiety",
        "Day 19: Create a coping card for your worst situation",
        "Day 20: Practice accepting uncertainty for one decision",
        "Day 21: Do something fun you've been avoiding",
        "Day 22: Challenge a fortune-telling thought",
        "Day 23: Practice saying 'I notice I'm having the thought...'",
        "Day 24: Move up one step on your exposure ladder",
        "Day 25: Teach someone else one CBT technique",
        "Day 26: Review all your thought records - find patterns",
        "Day 27: Update your relapse prevention plan",
        "Day 28: Practice gratitude - write 5 things",
        "Day 29: Celebrate your progress - write what changed",
        "Day 30: Set 3 CBT goals for the next month",
    ]
    y = 690
    for ch in challenges:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, ch, 'F1', 9)
        y -= 21

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book81_CBT_Anxiety_Workbook.pdf')
    print("Book81_CBT_Anxiety_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
