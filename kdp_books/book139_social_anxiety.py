"""Book 139: Social Anxiety Workbook - Face Your Fears & Build Confidence"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(520, "SOCIAL ANXIETY WORKBOOK", 'F2', 26, 0)
    doc.add_centered_text(480, "Face Your Fears & Build Confidence", 'F4', 18, 0.2)
    doc.add_centered_text(400, "CBT-Based Exercises Including:", 'F1', 13, 0.3)
    doc.add_centered_text(375, "Thought Challenging | Behavioral Experiments", 'F1', 12, 0.3)
    doc.add_centered_text(355, "Exposure Hierarchy | Assertiveness Training", 'F1', 12, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(600, "SOCIAL ANXIETY WORKBOOK", 'F2', 14, 0)
    doc.add_text(72, 500, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.3)
    doc.add_text(72, 480, "This workbook is for educational purposes only.", 'F1', 10, 0.3)
    doc.add_text(72, 460, "Not a substitute for professional treatment.", 'F1', 10, 0.3)

    # Page 3: What is Social Anxiety
    doc.new_page()
    doc.add_centered_text(740, "WHAT IS SOCIAL ANXIETY?", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Social Anxiety Disorder (SAD) is more than shyness. It's an intense fear of:", 'F1', 11, 0.2)
    fears = ["Being judged or evaluated negatively by others",
             "Embarrassing or humiliating yourself", "Being the center of attention",
             "Saying something 'stupid'", "Others noticing you're anxious",
             "Everyday situations like ordering food or making phone calls"]
    y = 675
    for f in fears:
        doc.add_text(90, y, f"- {f}", 'F1', 11, 0.2)
        y -= 20
    y -= 20
    doc.add_text(72, y, "The Social Anxiety Cycle:", 'F2', 12, 0)
    y -= 25
    cycle = ["1. Anticipatory anxiety (worrying before the event)",
             "2. Safety behaviors (avoiding eye contact, rehearsing, staying quiet)",
             "3. Self-focused attention (monitoring how you look/sound)",
             "4. Post-event processing (replaying and criticizing yourself after)",
             "5. Avoidance (canceling plans, saying no, isolating)"]
    for c in cycle:
        doc.add_text(90, y, c, 'F1', 11, 0.2)
        y -= 20

    # Page 4: Safety Behaviors Identification
    doc.new_page()
    doc.add_centered_text(740, "SAFETY BEHAVIORS IDENTIFICATION", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Safety behaviors MAINTAIN social anxiety by preventing you from learning", 'F1', 11, 0.2)
    doc.add_text(72, 688, "that your fears won't come true. Check all that apply to you:", 'F1', 11, 0.2)
    y = 660
    behaviors = ["Avoiding eye contact", "Speaking very quietly", "Rehearsing what to say",
                 "Holding a drink to hide trembling hands", "Wearing certain clothes to avoid sweating",
                 "Arriving early/late to avoid mingling", "Staying near exits",
                 "Only speaking when spoken to", "Over-preparing for conversations",
                 "Using alcohol to cope socially", "Checking phone to look busy",
                 "Deflecting attention/compliments", "Standing at edges of groups"]
    for b in behaviors:
        doc.add_rect(72, y-3, 12, 12)
        doc.add_text(90, y, b, 'F1', 11, 0.2)
        y -= 22
    y -= 15
    doc.add_text(72, y, "My other safety behaviors: __________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)

    # Page 5: Cognitive Distortions
    doc.new_page()
    doc.add_centered_text(740, "COGNITIVE DISTORTIONS IN SOCIAL SITUATIONS", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    distortions = [
        ("MIND READING:", "Assuming you know what others think about you.",
         "Example: 'They think I'm boring' (without evidence)"),
        ("FORTUNE TELLING:", "Predicting negative outcomes before they happen.",
         "Example: 'I'll definitely embarrass myself at the party'"),
        ("SPOTLIGHT EFFECT:", "Believing everyone notices your anxiety.",
         "Example: 'Everyone can see I'm blushing/sweating'"),
        ("CATASTROPHIZING:", "Blowing consequences out of proportion.",
         "Example: 'If I say something wrong, everyone will hate me'"),
        ("DISQUALIFYING THE POSITIVE:", "Dismissing positive social experiences.",
         "Example: 'They were just being polite, they don't really like me'"),
        ("EMOTIONAL REASONING:", "Feeling anxious = something IS wrong.",
         "Example: 'I feel awkward so I must BE awkward'")
    ]
    y = 700
    for name, desc, example in distortions:
        doc.add_text(72, y, name, 'F2', 11, 0)
        y -= 18
        doc.add_text(90, y, desc, 'F1', 10, 0.2)
        y -= 16
        doc.add_text(90, y, example, 'F3', 9, 0.4)
        y -= 28

    # Pages 6-11: Thought Challenging Worksheets (6 pages)
    for page_num in range(6):
        doc.new_page()
        doc.add_centered_text(740, f"THOUGHT CHALLENGING WORKSHEET ({page_num+1}/6)", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        doc.add_text(72, y, "Social Situation: ____________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Anxious Thought: ____________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Distortion Type (circle): Mind Reading / Fortune Telling / Spotlight /", 'F1', 10, 0.2)
        y -= 18
        doc.add_text(72, y, "  Catastrophizing / Disqualifying Positive / Emotional Reasoning", 'F1', 10, 0.2)
        y -= 28
        doc.add_text(72, y, "Evidence this thought is TRUE:", 'F2', 11, 0.1)
        y -= 20
        for i in range(2):
            doc.add_text(72, y, "_____________________________________________________________________", 'F1', 10, 0.3)
            y -= 18
        y -= 15
        doc.add_text(72, y, "Evidence this thought is NOT true:", 'F2', 11, 0.1)
        y -= 20
        for i in range(2):
            doc.add_text(72, y, "_____________________________________________________________________", 'F1', 10, 0.3)
            y -= 18
        y -= 15
        doc.add_text(72, y, "What would I tell a friend with this thought? ________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Balanced/realistic thought: __________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Belief in anxious thought: Before ___% After ___%", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "Anxiety level: Before ___ (0-10) After ___ (0-10)", 'F1', 11, 0.2)

    # Pages 12-16: Behavioral Experiments (5 pages)
    for page_num in range(5):
        doc.new_page()
        doc.add_centered_text(740, f"BEHAVIORAL EXPERIMENT ({page_num+1}/5)", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 705
        doc.add_text(72, y, "My prediction (what I think will happen): ____________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "Belief in prediction (0-100%): ___", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "The experiment (what I will do to test it): __________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "Safety behaviors I will DROP during the experiment:", 'F2', 11, 0.1)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "ACTUAL OUTCOME (what really happened): _______________________________", 'F2', 11, 0.1)
        y -= 22
        for i in range(3):
            doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
            y -= 20
        y -= 15
        doc.add_text(72, y, "Was my prediction accurate? _________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "What I learned: _____________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "_____________________________________________________________________", 'F1', 11, 0.2)
        y -= 28
        doc.add_text(72, y, "Updated belief in prediction (0-100%): ___", 'F1', 11, 0.2)

    # Page 17: Exposure Hierarchy
    doc.new_page()
    doc.add_centered_text(740, "EXPOSURE HIERARCHY FOR SOCIAL SITUATIONS", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "List social situations from least to most anxiety-provoking:", 'F1', 11, 0.2)
    y = 675
    for i in range(10):
        level = (i+1)*10
        doc.add_text(72, y, f"[{level}]", 'F2', 10, 0.2)
        doc.add_text(105, y, "_" * 58, 'F1', 11, 0.3)
        y -= 30
    y -= 10
    doc.add_text(72, y, "Start at the bottom. Practice each until anxiety drops 50%.", 'F2', 11, 0)

    # Page 18: Post-Event Processing Reduction
    doc.new_page()
    doc.add_centered_text(740, "POST-EVENT PROCESSING REDUCTION", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Post-event processing (PEP) = replaying social situations in your mind,", 'F1', 11, 0.2)
    doc.add_text(72, 683, "focusing on everything you did 'wrong.' This MAINTAINS social anxiety.", 'F1', 11, 0.2)
    y = 650
    doc.add_text(72, y, "When you catch yourself ruminating:", 'F2', 12, 0)
    y -= 25
    steps = ["1. NOTICE: 'I'm doing post-event processing right now.'",
             "2. REDIRECT: Shift attention to present moment (5 senses).",
             "3. REMIND: 'My anxious brain exaggerates. The reality was probably fine.'",
             "4. STOP: Set a rule - no analyzing social events after they're over."]
    for s in steps:
        doc.add_text(90, y, s, 'F1', 11, 0.2)
        y -= 22
    y -= 20
    doc.add_text(72, y, "PEP TRACKING:", 'F2', 12, 0)
    y -= 20
    doc.add_filled_rect(72, y-2, 468, 18, 0.85)
    doc.add_text(75, y, "Date", 'F2', 9, 0)
    doc.add_text(135, y, "Situation I'm replaying", 'F2', 9, 0)
    doc.add_text(310, y, "How long", 'F2', 9, 0)
    doc.add_text(380, y, "How I stopped", 'F2', 9, 0)
    y -= 25
    for i in range(10):
        doc.add_rect(72, y, 468, 28)
        y -= 30

    # Page 19: Attention Training
    doc.new_page()
    doc.add_centered_text(740, "ATTENTION TRAINING EXERCISES", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Social anxiety makes you SELF-FOCUSED. The cure: shift to EXTERNAL focus.", 'F1', 11, 0.2)
    y = 670
    exercises = [
        ("Exercise 1: The Observer", "In a social situation, focus entirely on the OTHER person. Notice their eye color, what they're wearing, their tone. You can't be self-conscious if all your attention is on them."),
        ("Exercise 2: The Reporter", "Pretend you're a journalist. Your job is to find out 3 interesting things about each person you talk to. Ask questions. Listen to answers."),
        ("Exercise 3: The Noticer", "In a group, notice 5 things about the environment. What's on the walls? What music is playing? What are people eating? Get OUT of your head."),
        ("Exercise 4: The Helper", "Focus on making the OTHER person comfortable. This shifts your brain from 'Am I okay?' to 'Are THEY okay?' - and reduces self-focus.")
    ]
    for title, desc in exercises:
        doc.add_text(72, y, title, 'F2', 11, 0)
        y -= 20
        # Word wrap the description
        words = desc.split()
        line = ""
        for word in words:
            if len(line + word) > 75:
                doc.add_text(90, y, line.strip(), 'F1', 10, 0.2)
                y -= 15
                line = word + " "
            else:
                line += word + " "
        if line.strip():
            doc.add_text(90, y, line.strip(), 'F1', 10, 0.2)
            y -= 25

    # Pages 20-24: Assertiveness Scripts (5 scenarios)
    scenarios = [
        ("RETURNING AN ITEM TO A STORE", ["Walk in with confidence", "Say: 'I'd like to return this please.'", "If questioned: 'It didn't work for me.'", "You don't need to over-explain or apologize."]),
        ("MAKING A PHONE CALL", ["Write down key points before calling", "Say: 'Hi, my name is ___. I'm calling about ___.'", "If confused: 'Could you repeat that please?'", "It's okay to pause and think."]),
        ("DISAGREEING WITH SOMEONE", ["Start with: 'I see it differently...'", "Or: 'I respect your view, and I think...'", "Stay calm. You don't need to 'win.'", "Disagreeing is not rude. Silence is self-betrayal."]),
        ("SAYING NO TO AN INVITATION", ["Say: 'Thanks for thinking of me. I can't make it.'", "You do NOT need to give a reason.", "If pushed: 'I appreciate it but my answer is no.'", "No is a complete sentence."]),
        ("STARTING A CONVERSATION", ["Comment on shared environment: 'This place is great.'", "Ask open-ended questions: 'What brings you here?'", "Share something small about yourself.", "Remember: most people love talking about themselves."])
    ]
    for title, scripts in scenarios:
        doc.new_page()
        doc.add_centered_text(740, f"ASSERTIVENESS: {title}", 'F2', 12, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 700
        for s in scripts:
            doc.add_text(90, y, f"- {s}", 'F1', 11, 0.2)
            y -= 22
        y -= 20
        doc.add_text(72, y, "Practice notes:", 'F2', 11, 0)
        y -= 22
        doc.add_text(72, y, "When I tried this: ___________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "What happened: ______________________________________________________", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "How I felt before (0-10): ___  After (0-10): ___", 'F1', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "What I learned: _____________________________________________________", 'F1', 11, 0.2)

    # Page 25: Social Skills Practice Log
    doc.new_page()
    doc.add_centered_text(740, "SOCIAL SKILLS PRACTICE LOG", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_filled_rect(72, 695, 468, 20, 0.85)
    doc.add_text(75, 698, "Date", 'F2', 8, 0)
    doc.add_text(125, 698, "Situation", 'F2', 8, 0)
    doc.add_text(275, 698, "Skill Practiced", 'F2', 8, 0)
    doc.add_text(395, 698, "Outcome", 'F2', 8, 0)
    y = 675
    for i in range(18):
        doc.add_rect(72, y, 468, 30)
        y -= 32

    # Page 26: Self-Compassion
    doc.new_page()
    doc.add_centered_text(740, "SELF-COMPASSION EXERCISES", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Replace self-criticism with self-compassion:", 'F2', 12, 0)
    y = 670
    doc.add_text(72, y, "What I'm criticizing myself for: _____________________________________", 'F1', 11, 0.2)
    y -= 30
    doc.add_text(72, y, "1. MINDFULNESS (acknowledge without over-identifying):", 'F2', 11, 0)
    y -= 20
    doc.add_text(72, y, "'This is a moment of suffering. This is hard right now.'", 'F4', 11, 0.3)
    y -= 30
    doc.add_text(72, y, "2. COMMON HUMANITY (I'm not alone in this):", 'F2', 11, 0)
    y -= 20
    doc.add_text(72, y, "'Many people struggle with social anxiety. I'm not the only one.'", 'F4', 11, 0.3)
    y -= 30
    doc.add_text(72, y, "3. SELF-KINDNESS (what would I say to a friend?):", 'F2', 11, 0)
    y -= 20
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)
    y -= 22
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)

    # Pages 27-30: Weekly Progress Tracker (4 pages)
    for week in range(4):
        doc.new_page()
        doc.add_centered_text(740, f"WEEKLY PROGRESS TRACKER - Week {week+1}", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 700
        doc.add_text(72, y, f"Week of: ______________", 'F1', 11, 0.2)
        y -= 30
        doc.add_text(72, y, "Social situations I faced this week:", 'F2', 11, 0)
        y -= 22
        for i in range(3):
            doc.add_text(72, y, f"{i+1}. _____________________________________________________________", 'F1', 10, 0.2)
            y -= 20
        y -= 15
        doc.add_text(72, y, "Safety behaviors I dropped:", 'F2', 11, 0)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Experiments I tried:", 'F2', 11, 0)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Wins/progress (even small):", 'F2', 11, 0)
        y -= 20
        doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.2)
        y -= 25
        doc.add_text(72, y, "Overall anxiety this week (0-10): ___", 'F1', 11, 0.2)
        y -= 25
        doc.add_text(72, y, "Next week's goal: __________________________________________________", 'F1', 11, 0.2)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book139_Social_Anxiety_Workbook.pdf')
    print("Book139_Social_Anxiety_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
