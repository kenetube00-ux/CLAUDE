"""Book 216: The Therapy Companion Workbook - Between-Session Exercises for Clients"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.2)
    doc.add_centered_text(750, "THE THERAPY COMPANION", 'F2', 26, 1)
    doc.add_centered_text(720, "WORKBOOK", 'F2', 26, 1)
    doc.add_centered_text(660, "Between-Session Exercises for Clients", 'F4', 16, 0.3)
    doc.add_centered_text(600, "Structured Homework Worksheets for Every Session", 'F1', 12, 0.4)
    doc.add_centered_text(550, "Thought Records | Behavioral Experiments | Mood Tracking", 'F1', 11, 0.4)
    doc.add_centered_text(500, "Skills Practice | Crisis Planning | Progress Monitoring", 'F1', 11, 0.4)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)
    doc.add_centered_text(170, "Professional Therapeutic Resource", 'F1', 10, 0.5)
    
    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(700, "THE THERAPY COMPANION WORKBOOK", 'F2', 14)
    doc.add_centered_text(675, "Between-Session Exercises for Clients", 'F1', 11)
    doc.add_centered_text(620, f"Copyright {author}", 'F1', 10)
    doc.add_centered_text(600, "All rights reserved.", 'F1', 10)
    doc.add_centered_text(560, "This workbook is designed to be used in conjunction with", 'F1', 10)
    doc.add_centered_text(545, "professional therapy. It is not a substitute for treatment.", 'F1', 10)
    doc.add_centered_text(500, "For personal therapeutic use only.", 'F1', 10)
    
    # Page 3: For Therapists to Assign note
    doc.new_page()
    doc.add_centered_text(720, "FOR THERAPISTS TO ASSIGN", 'F2', 18)
    doc.add_line(150, 705, 462, 705, 1, 0.3)
    doc.add_text(72, 660, "Dear Therapist,", 'F4', 12)
    doc.add_text(72, 630, "This workbook provides structured between-session exercises for your clients.", 'F1', 11)
    doc.add_text(72, 610, "Each worksheet is designed to reinforce in-session work and build skills.", 'F1', 11)
    doc.add_text(72, 580, "How to use this workbook:", 'F2', 11)
    doc.add_text(90, 555, "- Assign specific worksheets based on session content", 'F1', 10)
    doc.add_text(90, 535, "- Review completed sheets at the start of next session", 'F1', 10)
    doc.add_text(90, 515, "- Use mood tracker to monitor patterns between sessions", 'F1', 10)
    doc.add_text(90, 495, "- Encourage daily use of coping skills reference card", 'F1', 10)
    doc.add_text(90, 475, "- Update crisis plan as needed with client", 'F1', 10)
    doc.add_text(72, 430, "Contents:", 'F2', 11)
    doc.add_text(90, 410, "- 30 Therapy Homework Worksheets (comprehensive session tracking)", 'F1', 10)
    doc.add_text(90, 390, "- 4-Week Mood Tracker", 'F1', 10)
    doc.add_text(90, 370, "- Coping Skills Reference Card", 'F1', 10)
    doc.add_text(90, 350, "- My Therapy Goals Page", 'F1', 10)
    doc.add_text(90, 330, "- Progress Milestone Tracker", 'F1', 10)
    doc.add_text(90, 310, "- Emergency Contacts", 'F1', 10)
    
    # Pages 4-33: 30 Therapy Homework Worksheets
    for i in range(1, 31):
        doc.new_page()
        doc.add_centered_text(760, f"THERAPY HOMEWORK WORKSHEET #{i}", 'F2', 14)
        doc.add_line(72, 748, 540, 748, 0.5, 0.3)
        
        y = 720
        doc.add_text(72, y, "Session Date: _______________", 'F1', 10)
        doc.add_text(320, y, "Session #: _______", 'F1', 10)
        y -= 25
        doc.add_text(72, y, "Topic Covered in Session:", 'F2', 10)
        y -= 15
        doc.add_line(72, y, 540, y, 0.5, 0.4)
        y -= 5
        doc.add_line(72, y-15, 540, y-15, 0.5, 0.4)
        
        y -= 40
        doc.add_text(72, y, "THOUGHT RECORD", 'F2', 10)
        y -= 18
        doc.add_text(72, y, "Situation:", 'F1', 9)
        doc.add_line(130, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "Automatic Thought:", 'F1', 9)
        doc.add_line(175, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "Emotion (0-10):", 'F1', 9)
        doc.add_line(160, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "Evidence For:", 'F1', 9)
        doc.add_line(145, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "Evidence Against:", 'F1', 9)
        doc.add_line(165, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "Balanced Thought:", 'F1', 9)
        doc.add_line(165, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "New Emotion (0-10):", 'F1', 9)
        doc.add_line(180, y-2, 540, y-2, 0.5, 0.4)
        
        y -= 35
        doc.add_text(72, y, "BEHAVIORAL EXPERIMENT", 'F2', 10)
        y -= 18
        doc.add_text(72, y, "Prediction:", 'F1', 9)
        doc.add_line(135, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "Experiment:", 'F1', 9)
        doc.add_line(135, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "Outcome:", 'F1', 9)
        doc.add_line(125, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "What I Learned:", 'F1', 9)
        doc.add_line(155, y-2, 540, y-2, 0.5, 0.4)
        
        y -= 35
        doc.add_text(72, y, "MOOD CHECK", 'F2', 10)
        y -= 18
        doc.add_text(72, y, "Overall Mood (1-10): ___   Anxiety (1-10): ___   Energy (1-10): ___", 'F1', 9)
        y -= 18
        doc.add_text(72, y, "Sleep Quality (1-10): ___   Hours Slept: ___   Appetite: Good / Fair / Poor", 'F1', 9)
        
        y -= 35
        doc.add_text(72, y, "SKILLS PRACTICED THIS WEEK", 'F2', 10)
        y -= 18
        for s in range(3):
            doc.add_text(72, y, f"{s+1}.", 'F1', 9)
            doc.add_line(90, y-2, 540, y-2, 0.5, 0.4)
            y -= 18
        
        y -= 25
        doc.add_text(72, y, "HOMEWORK ASSIGNMENT FOR NEXT WEEK", 'F2', 10)
        y -= 18
        for s in range(3):
            doc.add_line(72, y-2, 540, y-2, 0.5, 0.4)
            y -= 18
        
        y -= 25
        doc.add_filled_rect(72, y-25, 468, 30, 0.92)
        doc.add_text(80, y, "CRISIS PLAN REMINDER: If in crisis, call: _______________", 'F2', 9)
        doc.add_text(80, y-15, "Safety plan location: _______________ Support person: _______________", 'F1', 9)
    
    # Pages 34-37: Mood Tracker (4 weeks)
    for week in range(1, 5):
        doc.new_page()
        doc.add_centered_text(760, f"MOOD TRACKER - WEEK {week}", 'F2', 14)
        doc.add_line(72, 748, 540, 748, 0.5, 0.3)
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        y = 720
        # Header
        doc.add_text(72, y, "Day", 'F2', 9)
        doc.add_text(150, y, "Mood", 'F2', 9)
        doc.add_text(200, y, "Anxiety", 'F2', 9)
        doc.add_text(260, y, "Sleep", 'F2', 9)
        doc.add_text(310, y, "Triggers/Notes", 'F2', 9)
        y -= 5
        doc.add_line(72, y, 540, y, 0.5, 0.3)
        
        for day in days:
            y -= 25
            doc.add_text(72, y, day, 'F1', 9)
            doc.add_text(150, y, "___/10", 'F1', 9)
            doc.add_text(200, y, "___/10", 'F1', 9)
            doc.add_text(260, y, "___/10", 'F1', 9)
            doc.add_line(310, y-2, 540, y-2, 0.5, 0.4)
            y -= 20
            doc.add_text(100, y, "AM mood: ___  PM mood: ___  Coping used:", 'F1', 8)
            doc.add_line(330, y-2, 540, y-2, 0.5, 0.4)
            y -= 5
            doc.add_line(72, y, 540, y, 0.5, 0.7)
        
        y -= 30
        doc.add_text(72, y, "WEEKLY PATTERNS:", 'F2', 10)
        y -= 18
        doc.add_text(72, y, "Best day: _______________  Worst day: _______________", 'F1', 9)
        y -= 18
        doc.add_text(72, y, "Average mood: ___/10    Triggers noticed:", 'F1', 9)
        doc.add_line(310, y-2, 540, y-2, 0.5, 0.4)
        y -= 18
        doc.add_text(72, y, "Most helpful coping skill:", 'F1', 9)
        doc.add_line(210, y-2, 540, y-2, 0.5, 0.4)
    
    # Page 38: Coping Skills Reference Card
    doc.new_page()
    doc.add_centered_text(760, "COPING SKILLS REFERENCE CARD", 'F2', 14)
    doc.add_line(72, 748, 540, 748, 0.5, 0.3)
    
    y = 720
    categories = [
        ("GROUNDING (5-4-3-2-1)", ["5 things you see", "4 things you touch", "3 things you hear", "2 things you smell", "1 thing you taste"]),
        ("BREATHING", ["Box breathing: 4 in, 4 hold, 4 out, 4 hold", "4-7-8: breathe in 4, hold 7, out 8", "Belly breathing: hand on belly, expand"]),
        ("PHYSICAL", ["Cold water on wrists", "Progressive muscle relaxation", "Walk or stretch for 5 minutes", "Hold ice cubes"]),
        ("COGNITIVE", ["Name the emotion without judgment", "Challenge the thought: evidence?", "Rate distress 0-10, wait, re-rate", "Wise mind: what would wise me say?"]),
        ("SOCIAL", ["Call support person", "Text crisis line (741741)", "Go to safe place with people", "Ask for a hug"]),
        ("SELF-SOOTHING", ["Listen to calming music", "Wrap in weighted/warm blanket", "Use favorite scent", "Drink warm tea slowly"]),
    ]
    
    for cat_name, skills in categories:
        doc.add_text(72, y, cat_name, 'F2', 10)
        y -= 16
        for skill in skills:
            doc.add_text(90, y, f"- {skill}", 'F1', 9)
            y -= 14
        y -= 10
    
    # Page 39: My Therapy Goals
    doc.new_page()
    doc.add_centered_text(760, "MY THERAPY GOALS", 'F2', 14)
    doc.add_line(72, 748, 540, 748, 0.5, 0.3)
    
    y = 710
    doc.add_text(72, y, "Date Started Therapy: _______________", 'F1', 10)
    doc.add_text(320, y, "Therapist: _______________", 'F1', 10)
    y -= 30
    
    for g in range(1, 6):
        doc.add_text(72, y, f"GOAL {g}:", 'F2', 10)
        y -= 18
        doc.add_line(72, y, 540, y, 0.5, 0.4)
        y -= 20
        doc.add_text(72, y, "Why this matters to me:", 'F1', 9)
        doc.add_line(190, y-2, 540, y-2, 0.5, 0.4)
        y -= 20
        doc.add_text(72, y, "How I'll know I've achieved it:", 'F1', 9)
        doc.add_line(225, y-2, 540, y-2, 0.5, 0.4)
        y -= 20
        doc.add_text(72, y, "Progress (circle): 1  2  3  4  5  6  7  8  9  10", 'F1', 9)
        y -= 20
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 15
    
    # Page 40: Progress Milestone Tracker + Emergency Contacts
    doc.new_page()
    doc.add_centered_text(760, "PROGRESS MILESTONES & EMERGENCY CONTACTS", 'F2', 13)
    doc.add_line(72, 748, 540, 748, 0.5, 0.3)
    
    y = 720
    doc.add_text(72, y, "PROGRESS MILESTONES", 'F2', 11)
    y -= 20
    milestones = ["First session completed", "Identified core issue", "Learned first coping skill",
                  "Used skill outside session", "Noticed mood improvement", "Handled trigger differently",
                  "Reached first goal", "Maintained gains 1 month", "Reduced session frequency",
                  "Therapy graduation"]
    for m in milestones:
        doc.add_text(90, y, f"[ ] {m}", 'F1', 9)
        doc.add_text(340, y, "Date achieved: ___________", 'F1', 9)
        y -= 18
    
    y -= 30
    doc.add_text(72, y, "EMERGENCY CONTACTS", 'F2', 11)
    y -= 20
    contacts = ["Therapist", "Psychiatrist", "Crisis Line (988)", "Emergency Contact 1",
                "Emergency Contact 2", "Local ER", "Support Group"]
    for c in contacts:
        doc.add_text(90, y, f"{c}: ", 'F2', 9)
        doc.add_line(200, y-2, 540, y-2, 0.5, 0.4)
        y -= 20
    
    y -= 15
    doc.add_filled_rect(72, y-30, 468, 35, 0.9)
    doc.add_text(80, y, "If you are in immediate danger, call 911.", 'F2', 9)
    doc.add_text(80, y-15, "National Suicide Prevention Lifeline: 988 | Crisis Text Line: Text HOME to 741741", 'F1', 9)
    
    doc.save("Book216_Therapist_Client_Workbook.pdf")
    print("Created: Book216_Therapist_Client_Workbook.pdf")

if __name__ == "__main__":
    create_book()
