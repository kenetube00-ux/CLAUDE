from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "IEP GOAL TRACKING WORKBOOK"
subtitle = "Monitor Your Child's Progress at Home"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 18)
pdf.add_centered_text(510, subtitle, 'F4', 14)
pdf.add_centered_text(400, "A Parent's Guide to Understanding", 'F4', 12)
pdf.add_centered_text(380, "and Tracking IEP Goals", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 12)
pdf.add_centered_text(560, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(540, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: Understanding IEP Goals (SMART format)
pdf.new_page()
pdf.add_centered_text(750, "UNDERSTANDING IEP GOALS", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
lines = [
    "An IEP (Individualized Education Program) is a legal document that",
    "outlines your child's educational goals and the support they'll receive.",
    "Understanding how goals work empowers you as a parent advocate.",
    "",
    "SMART GOALS FORMAT:",
    "S - Specific: What exactly will the child do?",
    "M - Measurable: How will progress be tracked? (numbers, percentages)",
    "A - Achievable: Is this realistic for your child?",
    "R - Relevant: Does this address a real need?",
    "T - Time-bound: By when? (usually within the IEP year)",
    "",
    "EXAMPLE OF A GOOD IEP GOAL:",
    "'By [date], [child] will read grade-level passages and answer",
    "comprehension questions with 80% accuracy in 4 out of 5 trials,",
    "as measured by teacher-created assessments.'",
    "",
    "WHAT TO LOOK FOR IN YOUR CHILD'S GOALS:",
    "- Is the baseline stated? (where they are NOW)",
    "- Is the target clear? (where they should be)",
    "- How will it be measured? (data collection method)",
    "- How often will data be collected?",
    "- Is progress reported to you regularly?",
    "",
    "YOUR ROLE AS A PARENT:",
    "- Request progress reports (at least quarterly)",
    "- Track progress at home (this workbook helps!)",
    "- Attend all IEP meetings prepared",
    "- Ask questions when goals are unclear",
    "- Request changes if goals aren't appropriate",
]
for line in lines:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 17

# Pages 4-5: My Child's Current IEP Goals (10 slots over 2 pages)
for page in range(2):
    pdf.new_page()
    start = page * 5 + 1
    end = start + 4
    pdf.add_centered_text(750, f"MY CHILD'S IEP GOALS (Goals {start}-{end})", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    for g in range(start, end + 1):
        pdf.add_filled_rect(48, y-82, 520, 95, 0.96)
        pdf.add_text(50, y, f"GOAL #{g}", 'F2', 11)
        y -= 16
        pdf.add_text(50, y, "Goal: ___________________________________________________", 'F4', 9.5)
        y -= 14
        pdf.add_text(50, y, "____________________________________________________", 'F4', 9.5)
        y -= 14
        pdf.add_text(50, y, "Baseline (current level): ___________________________________", 'F4', 9.5)
        y -= 14
        pdf.add_text(50, y, "Target (end goal): ________________________________________", 'F4', 9.5)
        y -= 14
        pdf.add_text(50, y, "Measurement method: _____________________________________", 'F4', 9.5)
        y -= 14
        pdf.add_text(50, y, "Area: [ ] Academic [ ] Speech [ ] OT [ ] Behavior [ ] Social [ ] Other", 'F4', 9.5)
        y -= 22

# Pages 6-20: Weekly Progress Tracking Sheets (15 pages)
for week in range(1, 16):
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEKLY PROGRESS TRACKING - WEEK {week}", 'F2', 14)
    pdf.add_text(50, 735, f"Week of: ___/___/___ to ___/___/___", 'F1', 10)
    pdf.add_line(50, 727, 562, 727)
    y = 710
    for g in range(5):
        pdf.add_text(50, y, f"Goal #{g+1}: ________________________", 'F2', 9)
        y -= 14
        pdf.add_text(50, y, "Data collected this week: _________________________________", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Observations: ___________________________________________", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Parent notes: ___________________________________________", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Progress: [ ] On track [ ] Behind [ ] Ahead [ ] Mastered", 'F3', 8)
        y -= 18
        pdf.add_line(50, y+6, 562, y+6, 0.3, 0.7)
        y -= 8
    y -= 5
    pdf.add_text(50, y, "OVERALL NOTES FOR THIS WEEK:", 'F2', 9)
    y -= 14
    for _ in range(4):
        pdf.add_line(50, y, 562, y, 0.3, 0.7)
        y -= 14
    y -= 8
    pdf.add_text(50, y, "Follow-up needed?  [ ] Yes: ________________________  [ ] No", 'F4', 9)

# Pages 21-25: Communication Log with School (5 pages)
for page in range(5):
    pdf.new_page()
    pdf.add_centered_text(750, "COMMUNICATION LOG WITH SCHOOL", 'F2', 14)
    pdf.add_text(50, 735, f"Page {page+1} of 5", 'F1', 9)
    pdf.add_line(50, 727, 562, 727)
    y = 710
    for entry in range(5):
        pdf.add_filled_rect(48, y-68, 520, 82, 0.96)
        pdf.add_text(50, y, "Date: ___/___/___", 'F2', 9)
        pdf.add_text(200, y, "Who I spoke with: ___________________", 'F4', 9)
        y -= 14
        pdf.add_text(50, y, "Role: [ ] Teacher [ ] SpEd [ ] SLP [ ] OT [ ] Admin [ ] Other", 'F4', 9)
        y -= 14
        pdf.add_text(50, y, "Topic: __________________________________________________", 'F4', 9)
        y -= 14
        pdf.add_text(50, y, "Outcome: ________________________________________________", 'F4', 9)
        y -= 14
        pdf.add_text(50, y, "Follow-up needed: [ ] Yes: ___________________ By: ___/___  [ ] No", 'F4', 9)
        y -= 24

# Page 26: Quarterly Review Preparation
pdf.new_page()
pdf.add_centered_text(750, "QUARTERLY REVIEW PREPARATION", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
quarterly = [
    "Before each quarterly progress report or IEP meeting, review this:",
    "",
    "QUARTER: [ ] Q1 (Oct-Dec) [ ] Q2 (Jan-Mar) [ ] Q3 (Apr-Jun) [ ] Q4",
    "",
    "FOR EACH GOAL, NOTE:",
    "Goal 1 - Progress: [ ] On track [ ] Behind [ ] Mastered",
    "  My observations: _____________________________________",
    "Goal 2 - Progress: [ ] On track [ ] Behind [ ] Mastered",
    "  My observations: _____________________________________",
    "Goal 3 - Progress: [ ] On track [ ] Behind [ ] Mastered",
    "  My observations: _____________________________________",
    "Goal 4 - Progress: [ ] On track [ ] Behind [ ] Mastered",
    "  My observations: _____________________________________",
    "Goal 5 - Progress: [ ] On track [ ] Behind [ ] Mastered",
    "  My observations: _____________________________________",
    "",
    "CONCERNS TO RAISE:",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "",
    "CHANGES I WANT TO REQUEST:",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "",
    "DOCUMENTS TO BRING:",
    "[ ] This tracking workbook  [ ] Outside evaluations  [ ] Report cards",
    "[ ] Work samples  [ ] Communication log  [ ] Notes from therapists",
]
for line in quarterly:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 27: Questions for the IEP Team
pdf.new_page()
pdf.add_centered_text(750, "QUESTIONS FOR THE IEP TEAM", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
questions = [
    "Keep this page handy during IEP meetings. Circle questions to ask:",
    "",
    "ABOUT PROGRESS:",
    "- How is progress being measured?",
    "- How often is data being collected?",
    "- Can I see the raw data?",
    "- Is my child making adequate progress?",
    "- What happens if a goal isn't being met?",
    "",
    "ABOUT SERVICES:",
    "- How many minutes of service per week?",
    "- Is it individual or group?",
    "- Who provides the service?",
    "- What happens when the provider is absent?",
    "- Are services being delivered as written?",
    "",
    "ABOUT ACCOMMODATIONS:",
    "- Are all accommodations being used consistently?",
    "- Are they working? How do you know?",
    "- Does my child need additional accommodations?",
    "- Are teachers aware of all accommodations?",
    "",
    "ABOUT NEXT STEPS:",
    "- What goals do you recommend for next year?",
    "- Is my child on track for grade promotion?",
    "- What can I do at home to support these goals?",
    "- When is the next meeting/progress report?",
    "",
    "MY QUESTIONS: ________________________________________",
    "__________________________________________________",
]
for line in questions:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 28: Accommodation Effectiveness Tracker
pdf.new_page()
pdf.add_centered_text(750, "ACCOMMODATION EFFECTIVENESS TRACKER", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "List your child's accommodations and track if they're working:", 'F4', 10)
y -= 22
for i in range(8):
    pdf.add_filled_rect(48, y-40, 520, 54, 0.96)
    pdf.add_text(50, y, f"Accommodation {i+1}: _______________________________________", 'F2', 9)
    y -= 14
    pdf.add_text(50, y, "Being used? [ ] Always [ ] Sometimes [ ] Rarely [ ] Never", 'F4', 9)
    y -= 14
    pdf.add_text(50, y, "Effective? [ ] Very [ ] Somewhat [ ] Not effective [ ] Need to discuss", 'F4', 9)
    y -= 14
    pdf.add_text(50, y, "Notes: _________________________________________________", 'F4', 9)
    y -= 22

# Page 29: My Child's Strengths & Growth Areas
pdf.new_page()
pdf.add_centered_text(750, "MY CHILD'S STRENGTHS & GROWTH AREAS", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
strengths = [
    "IEP meetings often focus on deficits. Remember your child's WHOLE self:",
    "",
    "MY CHILD'S STRENGTHS (what they're great at):",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "4. _________________________________________________",
    "5. _________________________________________________",
    "",
    "MY CHILD'S INTERESTS & PASSIONS:",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "",
    "GROWTH I'VE SEEN THIS YEAR:",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "",
    "AREAS THAT STILL NEED SUPPORT:",
    "1. _________________________________________________",
    "2. _________________________________________________",
    "3. _________________________________________________",
    "",
    "WHAT MOTIVATES MY CHILD:",
    "__________________________________________________",
    "",
    "WHAT ADULTS SHOULD KNOW ABOUT MY CHILD:",
    "__________________________________________________",
    "__________________________________________________",
]
for line in strengths:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 30: Annual Meeting Checklist & Parent Rights
pdf.new_page()
pdf.add_centered_text(750, "ANNUAL IEP MEETING CHECKLIST", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
annual = [
    "BEFORE THE MEETING:",
    "[ ] Review current IEP goals and progress data",
    "[ ] Complete this workbook's tracking pages",
    "[ ] Write down concerns and questions",
    "[ ] Get input from outside therapists (if any)",
    "[ ] Bring an advocate or support person (your right!)",
    "[ ] Request draft IEP in advance (at least 3 days before)",
    "",
    "DURING THE MEETING:",
    "[ ] Take notes or record (inform them - usually your right)",
    "[ ] Ask for clarification on anything unclear",
    "[ ] Share your home observations",
    "[ ] Review proposed goals for SMART criteria",
    "[ ] Don't sign same day if you need time to review",
    "",
    "AFTER THE MEETING:",
    "[ ] Get a copy of the final IEP",
    "[ ] Set up tracking in this workbook for new goals",
    "[ ] Share new goals/accommodations with tutors/therapists",
    "[ ] Calendar the next meeting date",
    "",
    "PARENT RIGHTS REMINDER:",
    "- You are an EQUAL member of the IEP team",
    "- You can disagree with the team's decisions",
    "- You can request an IEP meeting at any time (in writing)",
    "- You can bring anyone to the meeting for support",
    "- You can request Independent Educational Evaluations",
    "- You do NOT have to sign the IEP at the meeting",
    "- You can file for mediation or due process if needed",
]
for line in annual:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book160_IEP_Goal_Tracker.pdf')
print("Book160_IEP_Goal_Tracker.pdf created successfully!")
