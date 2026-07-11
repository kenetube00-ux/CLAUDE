from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1: Title Page
pdf.new_page()
pdf.add_filled_rect(0, 0, 432, 648, gray=0.95)
pdf.add_centered_text(430, "THE CAREGIVER'S", "F2", 22)
pdf.add_centered_text(400, "JOURNAL", "F2", 22)
pdf.add_line(120, 385, 312, 385, 2, gray=0.5)
pdf.add_centered_text(350, "You Can't Pour from", "F4", 16, gray=0.3)
pdf.add_centered_text(328, "an Empty Cup", "F4", 16, gray=0.3)
pdf.add_centered_text(270, "Daily Reflections for Those", "F1", 12, gray=0.4)
pdf.add_centered_text(252, "Who Care for Others", "F1", 12, gray=0.4)
pdf.add_centered_text(180, author, "F2", 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(420, "THE CAREGIVER'S JOURNAL", "F2", 13)
pdf.add_centered_text(400, "You Can't Pour from an Empty Cup", "F4", 11)
pdf.add_centered_text(365, f"Copyright (c) 2025 {author}", "F1", 10)
pdf.add_centered_text(347, "All rights reserved.", "F1", 10)
pdf.add_centered_text(315, "This journal is for personal reflection and does not", "F1", 9)
pdf.add_centered_text(302, "replace professional medical or psychological advice.", "F1", 9)
pdf.add_centered_text(270, "ISBN: 979-8-XXX-XXXXX-X", "F3", 9)


# Page 3: Recognizing Caregiver Burnout
pdf.new_page()
pdf.add_centered_text(610, "RECOGNIZING CAREGIVER BURNOUT", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Burnout doesn't happen overnight. It creeps in slowly.", "F1", 11)
pdf.add_text(40, 552, "Check any signs you've been experiencing:", "F2", 11)
signs = [
    "Feeling exhausted even after sleeping",
    "Resentment toward the person you care for",
    "Withdrawing from friends and activities",
    "Getting sick more often",
    "Feeling hopeless or trapped",
    "Neglecting your own health needs",
    "Difficulty sleeping or sleeping too much",
    "Increased irritability or anger",
    "Feeling unappreciated",
    "Loss of interest in things you used to enjoy",
    "Feeling like you have nothing left to give"
]
y = 525
for sign in signs:
    pdf.add_rect(45, y - 2, 12, 12)
    pdf.add_text(65, y, sign, "F1", 10)
    y -= 22
pdf.add_text(40, y - 15, "How many did you check? ___", "F2", 11)
pdf.add_text(40, y - 35, "If 5+, you may be in burnout. This journal is for YOU.", "F1", 10)

# Page 4: Compassion Fatigue Assessment
pdf.new_page()
pdf.add_centered_text(610, "COMPASSION FATIGUE ASSESSMENT", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Rate each statement (1=Never, 5=Always):", "F1", 11)
statements = [
    "I feel emotionally drained by caregiving",
    "I have difficulty separating my problems from theirs",
    "I feel guilty when I take time for myself",
    "I have lost my sense of humor",
    "I feel trapped in my caregiving role",
    "I avoid talking about how I really feel",
    "I feel angry that no one helps me",
    "I have physical symptoms (headaches, pain)",
    "I feel like I'm losing myself",
    "I can't remember the last time I felt joy"
]
y = 545
for i, stmt in enumerate(statements):
    pdf.add_text(40, y, f"{i+1}. {stmt}", "F1", 10)
    pdf.add_text(350, y, "1 2 3 4 5", "F3", 9)
    y -= 24
pdf.add_line(40, y - 5, 392, y - 5, 0.5)
pdf.add_text(40, y - 25, "Total Score: ___/50", "F2", 11)
pdf.add_text(40, y - 45, "10-20: Mild fatigue  |  21-35: Moderate  |  36-50: Severe", "F1", 10)
pdf.add_text(40, y - 70, "Today's date: ___________", "F1", 10)
pdf.add_text(40, y - 90, "Retake this monthly to track changes.", "F4", 10, gray=0.4)


# Pages 5-19: Daily Entries (2 per page, 30 entries total = 15 pages)
for page_num in range(15):
    pdf.new_page()
    entry_start = page_num * 2 + 1
    pdf.add_centered_text(615, f"DAILY JOURNAL - ENTRIES {entry_start} & {entry_start+1}", "F2", 13)
    pdf.add_line(40, 603, 392, 603, 1, gray=0.7)
    
    for entry in range(2):
        base_y = 580 - entry * 285
        pdf.add_filled_rect(40, base_y - 5, 352, 20, gray=0.88)
        pdf.add_text(45, base_y, f"ENTRY {entry_start + entry}", "F2", 10)
        pdf.add_text(200, base_y, "Date: ___/___/___", "F1", 9)
        
        pdf.add_text(40, base_y - 25, "Stress Level (1-10): ___", "F1", 10)
        pdf.add_text(220, base_y - 25, "Hours of sleep: ___", "F1", 10)
        
        pdf.add_text(40, base_y - 48, "What I did for my loved one today:", "F2", 10)
        pdf.add_line(40, base_y - 63, 392, base_y - 63, 0.5)
        pdf.add_line(40, base_y - 80, 392, base_y - 80, 0.5)
        
        pdf.add_text(40, base_y - 98, "What I did for MYSELF today:", "F2", 10)
        pdf.add_line(40, base_y - 113, 392, base_y - 113, 0.5)
        pdf.add_line(40, base_y - 130, 392, base_y - 130, 0.5)
        
        pdf.add_text(40, base_y - 148, "One boundary I held:", "F1", 10)
        pdf.add_line(200, base_y - 148, 392, base_y - 148, 0.5)
        
        pdf.add_text(40, base_y - 168, "One feeling I acknowledge:", "F1", 10)
        pdf.add_line(220, base_y - 168, 392, base_y - 168, 0.5)
        
        pdf.add_text(40, base_y - 188, "Tomorrow I need help with:", "F1", 10)
        pdf.add_line(220, base_y - 188, 392, base_y - 188, 0.5)


# Page 20: Respite Care Planning
pdf.new_page()
pdf.add_centered_text(610, "RESPITE CARE PLANNING", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Respite care = planned breaks from caregiving.", "F1", 11)
pdf.add_text(40, 552, "You NEED this. It's not optional - it's survival.", "F2", 11)
pdf.add_text(40, 522, "People who could help me take a break:", "F2", 11)
for i in range(4):
    pdf.add_text(50, 497 - i*22, f"{i+1}. Name: _____________ Can help with: _____________", "F1", 10)
pdf.add_text(40, 400, "Professional respite options I can look into:", "F2", 11)
pdf.add_text(50, 378, "- Adult day care centers", "F1", 10)
pdf.add_text(50, 358, "- Home health aides (even a few hours/week)", "F1", 10)
pdf.add_text(50, 338, "- Respite care facilities (short stays)", "F1", 10)
pdf.add_text(50, 318, "- Volunteer visitor programs", "F1", 10)
pdf.add_text(40, 285, "My ideal respite schedule:", "F2", 11)
pdf.add_text(50, 263, "Daily break: ___ minutes doing _______________", "F1", 10)
pdf.add_text(50, 243, "Weekly break: ___ hours doing _______________", "F1", 10)
pdf.add_text(50, 223, "Monthly break: ___ day(s) doing _______________", "F1", 10)
pdf.add_text(40, 190, "What's stopping me from taking breaks?", "F1", 11)
pdf.add_line(40, 170, 392, 170, 0.5)
pdf.add_line(40, 148, 392, 148, 0.5)

# Page 21: Asking for Help Scripts
pdf.new_page()
pdf.add_centered_text(610, "ASKING FOR HELP - SCRIPTS", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Asking for help is HARD. Here are scripts you can use:", "F1", 11)
pdf.add_filled_rect(40, 535, 352, 30, gray=0.92)
pdf.add_text(45, 550, "To a family member:", "F2", 10)
pdf.add_text(45, 537, "'I need help with [task]. Could you do this on [day]?'", "F4", 10)
pdf.add_filled_rect(40, 495, 352, 30, gray=0.92)
pdf.add_text(45, 510, "To a friend:", "F2", 10)
pdf.add_text(45, 497, "'I'm struggling. I don't need you to fix it, just listen.'", "F4", 10)
pdf.add_filled_rect(40, 455, 352, 30, gray=0.92)
pdf.add_text(45, 470, "To a sibling who isn't helping:", "F2", 10)
pdf.add_text(45, 457, "'I can't do this alone. Here's what I need from you: [specific task].'", "F4", 10)
pdf.add_filled_rect(40, 415, 352, 30, gray=0.92)
pdf.add_text(45, 430, "To a doctor:", "F2", 10)
pdf.add_text(45, 417, "'I'm the caregiver and I'm burning out. What resources exist?'", "F4", 10)
pdf.add_text(40, 385, "My own script for asking for help:", "F2", 11)
pdf.add_line(40, 363, 392, 363, 0.5)
pdf.add_line(40, 341, 392, 341, 0.5)
pdf.add_line(40, 319, 392, 319, 0.5)
pdf.add_text(40, 290, "Who I will ask: _______________", "F1", 11)
pdf.add_text(40, 268, "What I will ask for: _______________", "F1", 11)
pdf.add_text(40, 246, "When I will ask: _______________", "F1", 11)


# Page 22: Setting Boundaries with Family
pdf.new_page()
pdf.add_centered_text(610, "SETTING BOUNDARIES WITH FAMILY", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Boundaries aren't selfish. They're how you survive this.", "F1", 11)
pdf.add_text(40, 545, "Boundaries I need to set:", "F2", 11)
boundary_areas = [
    "With the person I care for:",
    "With other family members:",
    "With my own expectations:",
    "With work/outside obligations:"
]
y = 520
for area in boundary_areas:
    pdf.add_text(40, y, area, "F2", 10)
    pdf.add_line(40, y - 18, 392, y - 18, 0.5)
    pdf.add_line(40, y - 36, 392, y - 36, 0.5)
    y -= 65
pdf.add_text(40, y, "Boundary phrases I can use:", "F2", 11)
phrases = [
    "'I love you AND I need rest right now.'",
    "'I can do X but I cannot do Y today.'",
    "'That's not something I'm able to take on.'",
    "'I need 30 minutes of uninterrupted time.'"
]
y -= 20
for phrase in phrases:
    pdf.add_text(50, y, phrase, "F4", 10)
    y -= 20

# Page 23: My Support Network
pdf.new_page()
pdf.add_centered_text(610, "MY SUPPORT NETWORK", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Map out the people and resources in your life:", "F1", 11)
pdf.add_text(40, 545, "EMOTIONAL SUPPORT (people who listen):", "F2", 11)
for i in range(3):
    pdf.add_text(50, 520 - i*20, f"{i+1}. ___________________________", "F1", 10)
pdf.add_text(40, 450, "PRACTICAL SUPPORT (people who can DO things):", "F2", 11)
for i in range(3):
    pdf.add_text(50, 425 - i*20, f"{i+1}. ___________________________ Can help with: ___________", "F1", 10)
pdf.add_text(40, 355, "PROFESSIONAL SUPPORT:", "F2", 11)
pdf.add_text(50, 333, "Doctor: ___________________________", "F1", 10)
pdf.add_text(50, 313, "Therapist/Counselor: ___________________________", "F1", 10)
pdf.add_text(50, 293, "Support Group: ___________________________", "F1", 10)
pdf.add_text(50, 273, "Social Worker: ___________________________", "F1", 10)
pdf.add_text(40, 243, "ONLINE/COMMUNITY RESOURCES:", "F2", 11)
pdf.add_text(50, 221, "- Caregiver Action Network: caregiveraction.org", "F1", 10)
pdf.add_text(50, 201, "- AARP Caregiver Support: aarp.org/caregiving", "F1", 10)
pdf.add_text(50, 181, "- Local Area Agency on Aging: _______________", "F1", 10)

# Page 24: Self-Compassion Exercises
pdf.new_page()
pdf.add_centered_text(610, "SELF-COMPASSION EXERCISES", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "You deserve the same kindness you give others.", "F4", 12, gray=0.3)
pdf.add_text(40, 542, "Exercise 1: The Friend Test", "F2", 12)
pdf.add_text(40, 522, "What would you say to a friend in your situation?", "F1", 10)
pdf.add_line(40, 502, 392, 502, 0.5)
pdf.add_line(40, 482, 392, 482, 0.5)
pdf.add_text(40, 455, "Now say that same thing to yourself.", "F2", 10)
pdf.add_text(40, 428, "Exercise 2: Permission Slips", "F2", 12)
pdf.add_text(40, 408, "I give myself permission to:", "F1", 10)
permissions = ["feel tired", "say no", "ask for help", "feel angry", "rest without guilt"]
y = 386
for p in permissions:
    pdf.add_rect(45, y - 2, 12, 12)
    pdf.add_text(65, y, p, "F1", 10)
    y -= 20
pdf.add_text(40, y - 10, "Exercise 3: Loving-Kindness for Yourself", "F2", 12)
pdf.add_text(40, y - 30, "Repeat: 'May I be safe. May I be healthy.", "F4", 10)
pdf.add_text(40, y - 48, "May I be at peace. May I know I am enough.'", "F4", 10)
pdf.add_text(40, y - 75, "How did that feel? (circle)", "F1", 10)
pdf.add_text(50, y - 93, "Awkward / Emotional / Comforting / Nothing / Other:___", "F1", 10)


# Page 25: Emergency Burnout Plan
pdf.new_page()
pdf.add_centered_text(610, "EMERGENCY BURNOUT PLAN", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_filled_rect(40, 560, 352, 25, gray=0.85)
pdf.add_text(45, 567, "Fill this out NOW. Use it when you hit your breaking point.", "F2", 10)
pdf.add_text(40, 530, "Signs I'm at my breaking point:", "F2", 11)
pdf.add_line(40, 510, 392, 510, 0.5)
pdf.add_line(40, 490, 392, 490, 0.5)
pdf.add_text(40, 465, "Person who can take over immediately:", "F2", 11)
pdf.add_text(50, 445, "Name: _______________ Phone: _______________", "F1", 10)
pdf.add_text(40, 420, "My emergency self-care plan:", "F2", 11)
pdf.add_text(50, 400, "Step 1 (right now): ___________________________", "F1", 10)
pdf.add_text(50, 380, "Step 2 (today): ___________________________", "F1", 10)
pdf.add_text(50, 360, "Step 3 (this week): ___________________________", "F1", 10)
pdf.add_text(40, 330, "Place I can go to decompress:", "F1", 11)
pdf.add_line(40, 310, 300, 310, 0.5)
pdf.add_text(40, 285, "Professional I can call:", "F1", 11)
pdf.add_line(40, 265, 300, 265, 0.5)
pdf.add_filled_rect(40, 200, 352, 45, gray=0.92)
pdf.add_text(45, 230, "Remember: You cannot care for someone else", "F2", 10)
pdf.add_text(45, 215, "if you have completely depleted yourself.", "F2", 10)
pdf.add_text(45, 200, "Getting help is NOT abandoning them.", "F2", 10)

# Pages 26-30: Additional reflections and resources
# Page 26: Weekly Reflection
pdf.new_page()
pdf.add_centered_text(610, "WEEKLY REFLECTION", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Take a few minutes each week to check in with yourself.", "F1", 11)
pdf.add_text(40, 545, "Week of: _______________", "F1", 11)
pdf.add_text(40, 518, "Overall stress this week (1-10): ___", "F1", 11)
pdf.add_text(40, 491, "Moments I felt overwhelmed:", "F2", 11)
pdf.add_line(40, 471, 392, 471, 0.5)
pdf.add_line(40, 451, 392, 451, 0.5)
pdf.add_text(40, 424, "Moments I felt okay or even good:", "F2", 11)
pdf.add_line(40, 404, 392, 404, 0.5)
pdf.add_line(40, 384, 392, 384, 0.5)
pdf.add_text(40, 357, "Did I ask for help this week? Y / N", "F1", 11)
pdf.add_text(40, 335, "If yes, how did it go?", "F1", 10)
pdf.add_line(40, 315, 392, 315, 0.5)
pdf.add_text(40, 288, "One thing I'll do differently next week:", "F2", 11)
pdf.add_line(40, 268, 392, 268, 0.5)
pdf.add_line(40, 248, 392, 248, 0.5)
pdf.add_text(40, 221, "Something kind I did for myself:", "F1", 11)
pdf.add_line(40, 201, 392, 201, 0.5)

# Page 27: Gratitude & Grief
pdf.new_page()
pdf.add_centered_text(610, "GRATITUDE & GRIEF", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Caregiving often means grieving while caregiving.", "F1", 11)
pdf.add_text(40, 552, "Both gratitude and grief can exist at the same time.", "F4", 11, gray=0.3)
pdf.add_text(40, 522, "What I'm grieving:", "F2", 11)
pdf.add_text(50, 500, "(lost time, changed relationship, my old life, their health...)", "F1", 9, gray=0.5)
pdf.add_line(40, 478, 392, 478, 0.5)
pdf.add_line(40, 456, 392, 456, 0.5)
pdf.add_line(40, 434, 392, 434, 0.5)
pdf.add_text(40, 407, "What I'm grateful for:", "F2", 11)
pdf.add_line(40, 385, 392, 385, 0.5)
pdf.add_line(40, 363, 392, 363, 0.5)
pdf.add_line(40, 341, 392, 341, 0.5)
pdf.add_text(40, 310, "A memory that makes me smile:", "F2", 11)
pdf.add_line(40, 288, 392, 288, 0.5)
pdf.add_line(40, 266, 392, 266, 0.5)
pdf.add_text(40, 235, "Something I want them to know:", "F2", 11)
pdf.add_line(40, 213, 392, 213, 0.5)
pdf.add_line(40, 191, 392, 191, 0.5)


# Page 28: Caregiver Rights
pdf.new_page()
pdf.add_centered_text(610, "YOUR CAREGIVER BILL OF RIGHTS", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "As a caregiver, you have the RIGHT to:", "F1", 11)
rights = [
    "Take care of myself without feeling guilty",
    "Seek help from others even if my loved one objects",
    "Maintain parts of my own life that don't include caregiving",
    "Get angry, be sad, and express difficult feelings",
    "Reject any attempt to manipulate me through guilt",
    "Receive consideration, affection, and acceptance",
    "Take pride in what I accomplish",
    "Be treated with respect by those I care for",
    "Make mistakes without feeling like a failure",
    "Protect my individuality and my right to a life of my own",
    "Expect and demand improvements in our support system",
    "Say 'I'm done for today' without explanation"
]
y = 545
for right in rights:
    pdf.add_text(50, y, f"* {right}", "F1", 10)
    y -= 22
pdf.add_text(40, y - 15, "Which right do you most need to claim today?", "F2", 11)
pdf.add_line(40, y - 35, 392, y - 35, 0.5)
pdf.add_line(40, y - 55, 392, y - 55, 0.5)

# Page 29: Monthly Check-In
pdf.new_page()
pdf.add_centered_text(610, "MONTHLY CHECK-IN", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Month: _______________", "F1", 11)
pdf.add_text(40, 545, "My physical health this month (1-10): ___", "F1", 11)
pdf.add_text(40, 523, "My emotional health this month (1-10): ___", "F1", 11)
pdf.add_text(40, 501, "My relationships this month (1-10): ___", "F1", 11)
pdf.add_text(40, 471, "Biggest challenge this month:", "F2", 11)
pdf.add_line(40, 451, 392, 451, 0.5)
pdf.add_line(40, 431, 392, 431, 0.5)
pdf.add_text(40, 404, "How I handled it:", "F2", 11)
pdf.add_line(40, 384, 392, 384, 0.5)
pdf.add_line(40, 364, 392, 364, 0.5)
pdf.add_text(40, 337, "Something that brought me joy:", "F2", 11)
pdf.add_line(40, 317, 392, 317, 0.5)
pdf.add_text(40, 290, "My goals for next month:", "F2", 11)
pdf.add_text(50, 268, "For my loved one: ___________________________", "F1", 10)
pdf.add_text(50, 248, "For myself: ___________________________", "F1", 10)
pdf.add_text(50, 228, "For my health: ___________________________", "F1", 10)
pdf.add_text(40, 195, "Am I getting the support I need? Y / N", "F1", 11)
pdf.add_text(40, 173, "If no, what needs to change?", "F1", 10)
pdf.add_line(40, 153, 392, 153, 0.5)

# Page 30: Closing Page
pdf.new_page()
pdf.add_filled_rect(0, 0, 432, 648, gray=0.95)
pdf.add_centered_text(440, "YOU ARE DOING", "F2", 22)
pdf.add_centered_text(410, "SOMETHING INCREDIBLE.", "F2", 22)
pdf.add_line(120, 390, 312, 390, 2, gray=0.5)
pdf.add_centered_text(355, "And you deserve care too.", "F4", 14, gray=0.3)
pdf.add_centered_text(320, "You are not alone in this journey.", "F1", 12, gray=0.4)
pdf.add_centered_text(298, "You are not failing.", "F1", 12, gray=0.4)
pdf.add_centered_text(276, "You are human.", "F1", 12, gray=0.4)
pdf.add_centered_text(220, "Caregiver Support:", "F2", 11)
pdf.add_centered_text(200, "Caregiver Action Network: 1-855-227-3640", "F1", 10)
pdf.add_centered_text(182, "AARP Caregiving Helpline: 1-877-333-5885", "F1", 10)
pdf.add_centered_text(140, f"With gratitude, {author}", "F4", 11, gray=0.4)

pdf.save("Book171_Caregiver_Burnout_Journal.pdf")
print("SUCCESS: Book171_Caregiver_Burnout_Journal.pdf created (30 pages)")
