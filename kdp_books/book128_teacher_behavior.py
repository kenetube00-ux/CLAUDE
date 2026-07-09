from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "CLASSROOM BEHAVIOR TRACKING SYSTEM"
subtitle = "Daily Data Collection for Teachers"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 17)
pdf.add_centered_text(515, subtitle, 'F4', 13)
pdf.add_centered_text(440, "ABC Data | Interval Recording | Daily Charts", 'F4', 11)
pdf.add_centered_text(420, "BIP Templates | Progress Monitoring", 'F4', 11)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 11)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: Behavior Definitions Page
pdf.new_page()
pdf.add_centered_text(750, "BEHAVIOR DEFINITIONS", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Operational definitions must be OBSERVABLE and MEASURABLE.", 'F4', 10)
y -= 14
pdf.add_text(50, y, "Define behaviors so ANY observer would record them the same way.", 'F4', 10)
y -= 20
behaviors = [
    ("1. Off-Task Behavior", "Eyes not directed at instructional materials, teacher, or relevant task for 3+ consecutive seconds."),
    ("2. Verbal Disruption", "Any vocalization (talking, humming, calling out) without teacher permission that interrupts instruction."),
    ("3. Physical Aggression", "Any instance of hitting, kicking, pushing, biting, or throwing objects at another person."),
    ("4. Non-Compliance", "Failure to initiate a teacher-directed task within 10 seconds of the instruction being given."),
    ("5. Elopement", "Leaving designated area (seat, classroom, or assigned space) without permission."),
    ("6. Property Destruction", "Any action that damages or attempts to damage materials, furniture, or others' belongings."),
    ("7. Self-Stimulatory Behavior", "Repetitive motor movements (hand flapping, rocking, spinning) lasting 5+ seconds."),
    ("8. Verbal Aggression", "Threats, insults, profanity, or intimidating statements directed at peers or adults."),
    ("9. Task Refusal", "Verbally stating 'no' or putting head down when presented with academic work."),
    ("10. Positive Peer Interaction", "Appropriate verbal or physical exchanges (sharing, complimenting, cooperating) with peers.")
]
for bname, bdef in behaviors:
    pdf.add_text(50, y, bname, 'F2', 10)
    y -= 14
    # wrap definition
    while len(bdef) > 80:
        split = bdef[:80].rfind(' ')
        pdf.add_text(60, y, bdef[:split], 'F4', 9)
        bdef = bdef[split+1:]
        y -= 12
    pdf.add_text(60, y, bdef, 'F4', 9)
    y -= 18

# Pages 4-13: ABC Data Collection Sheets (10 pages)
for abc_page in range(1, 11):
    pdf.new_page()
    pdf.add_centered_text(750, f"ABC DATA COLLECTION - PAGE {abc_page}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 722
    pdf.add_text(50, y, "Student: _______________________  Observer: _______________________  Date: ___/___/___", 'F1', 9)
    y -= 20
    for entry in range(5):
        pdf.add_filled_rect(50, y - 3, 512, 110, 0.95)
        pdf.add_rect(50, y - 3, 512, 110, 0.5, 0.5)
        pdf.add_text(55, y + 92, f"Incident {(abc_page-1)*5 + entry + 1}", 'F2', 9)
        pdf.add_text(160, y + 92, "Time: _______", 'F1', 8)
        pdf.add_text(260, y + 92, "Duration: _______", 'F1', 8)
        pdf.add_text(380, y + 92, "Frequency today: _____", 'F1', 8)
        pdf.add_text(55, y + 74, "ANTECEDENT (what happened BEFORE):", 'F2', 8)
        pdf.add_line(260, y + 72, 555, y + 72, 0.3, 0.5)
        pdf.add_line(55, y + 58, 555, y + 58, 0.3, 0.5)
        pdf.add_text(55, y + 44, "BEHAVIOR (what the student DID - be specific):", 'F2', 8)
        pdf.add_line(310, y + 42, 555, y + 42, 0.3, 0.5)
        pdf.add_line(55, y + 28, 555, y + 28, 0.3, 0.5)
        pdf.add_text(55, y + 14, "CONSEQUENCE (what happened AFTER):", 'F2', 8)
        pdf.add_line(260, y + 12, 555, y + 12, 0.3, 0.5)
        pdf.add_line(55, y - 2, 555, y - 2, 0.3, 0.5)
        y -= 125

# Pages 14-18: Interval Recording Sheets (5 pages)
for int_page in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(750, f"INTERVAL RECORDING SHEET - PAGE {int_page}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 722
    pdf.add_text(50, y, "Student: ____________________  Date: ___/___/___  Observer: ____________________", 'F1', 9)
    y -= 14
    pdf.add_text(50, y, "Target Behavior: _________________________  Interval Length: 15 minutes", 'F1', 9)
    y -= 14
    pdf.add_text(50, y, "Setting: ___________________________  Activity: ___________________________", 'F1', 9)
    y -= 20
    pdf.add_text(50, y, "Recording Method:  [ ] Whole Interval  [ ] Partial Interval  [ ] Momentary Time Sampling", 'F1', 8)
    y -= 20
    # Table header
    pdf.add_filled_rect(50, y - 3, 512, 16, 0.85)
    pdf.add_text(55, y, "Interval", 'F2', 8)
    pdf.add_text(110, y, "Time", 'F2', 8)
    pdf.add_text(170, y, "Behavior? (Y/N)", 'F2', 8)
    pdf.add_text(290, y, "Intensity (1-5)", 'F2', 8)
    pdf.add_text(400, y, "Notes", 'F2', 8)
    y -= 16
    for interval in range(1, 25):
        start_min = (interval - 1) * 15
        end_min = interval * 15
        start_hr = start_min // 60
        start_m = start_min % 60
        pdf.add_text(55, y, f"{interval}", 'F3', 7)
        pdf.add_text(110, y, f":__-:__", 'F3', 7)
        pdf.add_text(195, y, "Y / N", 'F3', 7)
        pdf.add_text(315, y, "1 2 3 4 5", 'F3', 7)
        pdf.add_line(400, y - 1, 560, y - 1, 0.2, 0.6)
        y -= 14
    y -= 8
    pdf.add_text(50, y, f"Total intervals with behavior: ___/24 = ___%   Summary: _______________________", 'F1', 8)

# Pages 19-23: Daily Behavior Charts (5 pages)
for chart_page in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(750, f"DAILY BEHAVIOR CHART - PAGE {chart_page}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 722
    pdf.add_text(50, y, "Student: _______________________  Week of: ___/___/___", 'F1', 9)
    y -= 16
    pdf.add_text(50, y, "Target Behaviors:  1. ___________________  2. ___________________  3. ___________________", 'F1', 9)
    y -= 16
    pdf.add_text(50, y, "Rating Scale: 1=Poor  2=Below Expected  3=Expected  4=Above Expected  5=Excellent", 'F1', 8)
    y -= 20
    # Table
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods = ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5", "Period 6", "Lunch", "Specials"]
    pdf.add_filled_rect(50, y - 3, 512, 14, 0.85)
    pdf.add_text(55, y, "Day/Period", 'F2', 7)
    x_pos = 130
    for period in periods:
        pdf.add_text(x_pos, y, period[:6], 'F2', 6)
        x_pos += 55
    pdf.add_text(x_pos, y, "Total", 'F2', 7)
    y -= 16
    for day in days:
        pdf.add_text(55, y, day, 'F2', 8)
        x_pos = 130
        for _ in periods:
            pdf.add_text(x_pos + 10, y, "___", 'F3', 7)
            x_pos += 55
        pdf.add_text(x_pos + 5, y, "___/40", 'F3', 7)
        y -= 14
    y -= 15
    pdf.add_text(50, y, "DAILY NOTES:", 'F2', 9)
    y -= 14
    for day in days:
        pdf.add_text(55, y, f"{day}:", 'F1', 8)
        pdf.add_line(105, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 14
    y -= 10
    pdf.add_text(50, y, "WEEKLY SUMMARY:", 'F2', 9)
    y -= 14
    pdf.add_text(55, y, "Best day: ___________  Most challenging day: ___________", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Strategies that worked: _____________________________________________", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Adjustments for next week: __________________________________________", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Parent contact: [ ] Phone [ ] Email [ ] Note home  Date: ___/___/___", 'F1', 8)

# Page 24: Weekly Summary Graph Template
pdf.new_page()
pdf.add_centered_text(750, "WEEKLY SUMMARY GRAPH TEMPLATE", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 720
pdf.add_text(50, y, "Student: _______________________  Behavior: _______________________", 'F1', 9)
y -= 16
pdf.add_text(50, y, "Measurement: [ ] Frequency  [ ] Duration  [ ] Percentage of intervals  [ ] Rating", 'F1', 9)
y -= 25
# Draw graph axes
graph_bottom = 350
graph_top = y - 10
graph_left = 80
graph_right = 540
pdf.add_line(graph_left, graph_bottom, graph_left, graph_top, 1)  # y-axis
pdf.add_line(graph_left, graph_bottom, graph_right, graph_bottom, 1)  # x-axis
# Y-axis labels
for i in range(11):
    tick_y = graph_bottom + (graph_top - graph_bottom) * i // 10
    pdf.add_line(graph_left - 5, tick_y, graph_left, tick_y, 0.5)
    pdf.add_text(55, tick_y - 3, f"{i*10}", 'F3', 7)
# X-axis labels (weeks)
for w in range(12):
    tick_x = graph_left + (graph_right - graph_left) * w // 11
    pdf.add_line(tick_x, graph_bottom, tick_x, graph_bottom - 5, 0.5)
    pdf.add_text(tick_x - 5, graph_bottom - 15, f"Wk{w+1}", 'F3', 6)
y = graph_bottom - 40
pdf.add_text(50, y, "Goal line at: _______  Baseline: _______  Current: _______", 'F1', 9)
y -= 20
pdf.add_text(50, y, "Trend:  [ ] Improving  [ ] Stable  [ ] Worsening  [ ] Variable", 'F1', 9)
y -= 16
pdf.add_text(50, y, "Notes: _______________________________________________________________", 'F1', 9)

# Pages 25-26: Behavior Intervention Plan Template (2 pages)
pdf.new_page()
pdf.add_centered_text(750, "BEHAVIOR INTERVENTION PLAN (BIP) - PAGE 1", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 720
bip_fields = [
    "Student: _______________________  DOB: ___/___/___  Grade: _____",
    "School: _______________________  Teacher: _______________________",
    "Date of Plan: ___/___/___  Review Date: ___/___/___",
    "",
    "TARGET BEHAVIOR (operationally defined):",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "",
    "BASELINE DATA:",
    "Frequency: _____/day  Duration: _____ min  Intensity: 1 2 3 4 5",
    "Data collection method: _________________________________________",
    "Data collection period: ___/___/___ to ___/___/___",
    "",
    "FUNCTION OF BEHAVIOR (based on FBA):",
    "[ ] Escape/Avoidance (from task, person, setting)",
    "[ ] Attention (from peers, adults)",
    "[ ] Access to tangible (object, activity, privilege)",
    "[ ] Sensory/Automatic (internal reinforcement)",
    "Evidence for function: __________________________________________",
    "_______________________________________________________________",
    "",
    "SETTING EVENTS / ANTECEDENT TRIGGERS:",
    "Setting events (distant): ________________________________________",
    "Immediate triggers: ____________________________________________",
    "Time of day most likely: ________________________________________",
    "Context/activity most likely: ____________________________________"
]
for line in bip_fields:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 14

pdf.new_page()
pdf.add_centered_text(750, "BEHAVIOR INTERVENTION PLAN (BIP) - PAGE 2", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 720
bip_fields2 = [
    "PREVENTION STRATEGIES (antecedent modifications):",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "3. ____________________________________________________________",
    "",
    "REPLACEMENT BEHAVIOR (same function, appropriate form):",
    "_______________________________________________________________",
    "How it will be taught: _________________________________________",
    "",
    "REINFORCEMENT PLAN:",
    "Reinforcer(s): _________________________________________________",
    "Schedule: [ ] Continuous  [ ] Fixed ratio ___  [ ] Variable ratio ___",
    "Delivered by: _________________________________________________",
    "",
    "RESPONSE TO BEHAVIOR (reactive strategies):",
    "Mild behavior: _________________________________________________",
    "Moderate behavior: _____________________________________________",
    "Severe/crisis behavior: _________________________________________",
    "",
    "GOAL:",
    "Reduce target behavior from ___/day to ___/day within ___ weeks.",
    "Increase replacement behavior from ___% to ___% within ___ weeks.",
    "",
    "TEAM MEMBERS:",
    "Name: ___________________  Role: ___________________",
    "Name: ___________________  Role: ___________________",
    "Name: ___________________  Role: ___________________",
    "",
    "SIGNATURES:",
    "Teacher: ___________________  Date: ___/___/___",
    "Parent: ____________________  Date: ___/___/___",
    "Administrator: _____________  Date: ___/___/___"
]
for line in bip_fields2:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 14

# Pages 27-29: Parent Communication Forms (3 pages)
for comm_page in range(1, 4):
    pdf.new_page()
    pdf.add_centered_text(750, f"PARENT COMMUNICATION FORM - PAGE {comm_page}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    for form in range(2):
        pdf.add_rect(50, y - 5, 512, 290, 0.5, 0.5)
        pdf.add_text(55, y + 270, "PARENT/GUARDIAN COMMUNICATION LOG", 'F2', 10)
        pdf.add_text(55, y + 252, "Student: _______________________  Date: ___/___/___", 'F1', 9)
        pdf.add_text(55, y + 236, "Contact Method: [ ] Phone  [ ] Email  [ ] Note  [ ] Conference  [ ] Other", 'F1', 8)
        pdf.add_text(55, y + 218, "Parent/Guardian contacted: _______________________________________", 'F1', 9)
        pdf.add_text(55, y + 198, "PURPOSE:", 'F2', 9)
        pdf.add_text(55, y + 183, "[ ] Positive report  [ ] Behavior concern  [ ] Academic concern", 'F1', 8)
        pdf.add_text(55, y + 168, "[ ] IEP/BIP update  [ ] Request meeting  [ ] Follow-up", 'F1', 8)
        pdf.add_text(55, y + 148, "DISCUSSION SUMMARY:", 'F2', 9)
        for line_num in range(4):
            pdf.add_line(55, y + 132 - line_num * 14, 555, y + 132 - line_num * 14, 0.3, 0.5)
        pdf.add_text(55, y + 68, "PARENT RESPONSE/FEEDBACK:", 'F2', 9)
        for line_num in range(2):
            pdf.add_line(55, y + 52 - line_num * 14, 555, y + 52 - line_num * 14, 0.3, 0.5)
        pdf.add_text(55, y + 20, "ACTION ITEMS:", 'F2', 9)
        pdf.add_text(55, y + 5, "School will: ______________________________________________________", 'F1', 8)
        pdf.add_text(55, y - 10, "Parent will: ______________________________________________________", 'F1', 8)
        pdf.add_text(55, y - 25, "Follow-up date: ___/___/___  Teacher signature: ___________________", 'F1', 8)
        y -= 310

# Page 30: Function-Based Analysis Worksheet
pdf.new_page()
pdf.add_centered_text(750, "FUNCTION-BASED ANALYSIS WORKSHEET", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
fba = [
    "Student: _______________________  Date: ___/___/___",
    "Behavior being analyzed: ________________________________________",
    "",
    "PATTERNS FROM DATA (review your ABC sheets):",
    "",
    "Most common ANTECEDENTS (what happens before):",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "3. ____________________________________________________________",
    "",
    "Most common CONSEQUENCES (what happens after):",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "3. ____________________________________________________________",
    "",
    "FUNCTION ANALYSIS:",
    "When does behavior INCREASE? ____________________________________",
    "When does behavior DECREASE or not occur? ________________________",
    "What does the student GAIN from the behavior? ____________________",
    "What does the student AVOID from the behavior? ___________________",
    "",
    "HYPOTHESIS STATEMENT:",
    "'When [antecedent/trigger], [student] engages in [behavior]",
    "in order to [get/avoid] [function]. This is evidenced by",
    "[data/observations].'",
    "",
    "My hypothesis:",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "_______________________________________________________________"
]
for line in fba:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 15

# Page 31: Reinforcement Menu
pdf.new_page()
pdf.add_centered_text(750, "REINFORCEMENT MENU", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Student: _______________________  Updated: ___/___/___", 'F1', 9)
y -= 16
pdf.add_text(50, y, "Interview the student: What do you enjoy? What motivates you?", 'F4', 10)
y -= 20
categories = [
    ("SOCIAL REINFORCERS (free!)", ["Verbal praise (specific)", "High-five or fist bump", "Lunch with teacher/friend", "Positive phone call home", "Class helper role", "Extra social time"]),
    ("ACTIVITY REINFORCERS", ["Extra recess (5 min)", "Computer/tablet time", "Drawing/art time", "Reading free-choice book", "Game with a friend", "Leading a class activity"]),
    ("TANGIBLE REINFORCERS", ["Stickers/stamps", "Pencil/eraser", "Snack from prize box", "Homework pass", "Treasure box item", "Special certificate"]),
    ("ESCAPE REINFORCERS (use carefully)", ["Shortened assignment", "Choice of where to sit", "Break from task (timed)", "Reduced homework", "Skip one problem", "Work in preferred location"])
]
for cat_name, items in categories:
    pdf.add_text(50, y, cat_name, 'F2', 9)
    y -= 14
    for item in items:
        pdf.add_rect(60, y - 2, 8, 8, 0.4)
        pdf.add_text(73, y, item, 'F4', 8)
        y -= 12
    y -= 8
y -= 5
pdf.add_text(50, y, "STUDENT'S TOP 5 PREFERRED REINFORCERS:", 'F2', 9)
y -= 14
for i in range(5):
    pdf.add_text(55, y, f"{i+1}. _________________________________  Earned by: ________________________", 'F1', 8)
    y -= 13

# Page 32: Progress Monitoring
pdf.new_page()
pdf.add_centered_text(750, "PROGRESS MONITORING SUMMARY", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Student: _______________________  Target Behavior: _______________________", 'F1', 9)
y -= 16
pdf.add_text(50, y, "Goal: _______________________________________________________________", 'F1', 9)
y -= 20
pdf.add_filled_rect(50, y - 3, 512, 14, 0.85)
pdf.add_text(55, y, "Week", 'F2', 8)
pdf.add_text(95, y, "Dates", 'F2', 8)
pdf.add_text(175, y, "Frequency", 'F2', 8)
pdf.add_text(250, y, "Duration", 'F2', 8)
pdf.add_text(320, y, "% Intervals", 'F2', 8)
pdf.add_text(400, y, "Rating Avg", 'F2', 8)
pdf.add_text(480, y, "On Track?", 'F2', 8)
y -= 16
for w in range(16):
    pdf.add_text(55, y, f"{w+1}", 'F3', 7)
    pdf.add_line(95, y - 1, 170, y - 1, 0.2, 0.6)
    pdf.add_line(175, y - 1, 245, y - 1, 0.2, 0.6)
    pdf.add_line(250, y - 1, 315, y - 1, 0.2, 0.6)
    pdf.add_line(320, y - 1, 395, y - 1, 0.2, 0.6)
    pdf.add_line(400, y - 1, 475, y - 1, 0.2, 0.6)
    pdf.add_text(490, y, "Y / N", 'F3', 7)
    y -= 14
y -= 10
pdf.add_text(50, y, "DECISION RULES:", 'F2', 9)
y -= 14
pdf.add_text(55, y, "If on track for 3+ weeks: Continue current plan", 'F4', 8)
y -= 12
pdf.add_text(55, y, "If NOT on track for 3+ weeks: Modify intervention (change strategies, reinforcers, or goals)", 'F4', 8)
y -= 12
pdf.add_text(55, y, "If goal MET for 3+ weeks: Fade supports, set new goal, or discharge", 'F4', 8)
y -= 16
pdf.add_text(50, y, "NOTES/MODIFICATIONS MADE:", 'F1', 9)
y -= 14
for _ in range(3):
    pdf.add_line(50, y, 562, y, 0.3, 0.5)
    y -= 14

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book128_Classroom_Behavior_Tracker.pdf')
print("Book128_Classroom_Behavior_Tracker.pdf created successfully!")
