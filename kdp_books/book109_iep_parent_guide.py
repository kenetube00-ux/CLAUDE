from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(550, "THE IEP MEETING PLANNER", 'F2', 18)
pdf.add_centered_text(520, "A Parent's Guide to Special Education Advocacy", 'F4', 13)
pdf.add_centered_text(400, "Know Your Rights. Ask the Right Questions.", 'F4', 12)
pdf.add_centered_text(383, "Get Your Child What They Need.", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, "THE IEP MEETING PLANNER", 'F2', 12)
pdf.add_centered_text(575, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)
pdf.add_centered_text(550, "Not legal advice. Consult an education attorney for specific situations.", 'F4', 9)

# Page 3: IEP Basics
pdf.new_page()
pdf.add_centered_text(750, "IEP BASICS EXPLAINED SIMPLY", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "WHAT IS AN IEP?",
    "An Individualized Education Program (IEP) is a legal document that",
    "outlines the special education services your child will receive.", "",
    "WHO QUALIFIES?",
    "Children ages 3-21 with a disability that affects their ability",
    "to learn in a general education setting. Must meet criteria under",
    "one of 13 disability categories in IDEA (Individuals with",
    "Disabilities Education Act).", "",
    "WHAT DOES AN IEP INCLUDE?",
    "- Present levels of performance (where your child is NOW)",
    "- Annual goals (what they'll work toward this year)",
    "- Special education services (speech, OT, resource room, etc.)",
    "- Accommodations and modifications",
    "- How progress will be measured and reported",
    "- Transition planning (age 14-16, depending on state)", "",
    "WHO IS ON THE IEP TEAM?",
    "- YOU (the parent - the MOST important member!)",
    "- General education teacher",
    "- Special education teacher",
    "- School administrator (LEA representative)",
    "- Related service providers (as applicable)",
    "- Your child (when appropriate)",
    "- Anyone else YOU invite (advocate, family member, tutor)"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 4: Your Rights (IDEA overview)
pdf.new_page()
pdf.add_centered_text(750, "YOUR RIGHTS AS A PARENT (IDEA)", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Under the Individuals with Disabilities Education Act (IDEA),",
    "you have these LEGAL RIGHTS:", "",
    "1. RIGHT TO PARTICIPATE in ALL decisions about your child",
    "2. RIGHT TO INFORMED CONSENT before evaluations or placement changes",
    "3. RIGHT TO ACCESS all educational records",
    "4. RIGHT TO AN INDEPENDENT EDUCATIONAL EVALUATION (IEE) at",
    "   district expense if you disagree with their evaluation",
    "5. RIGHT TO WRITTEN NOTICE before any changes to services",
    "6. RIGHT TO DISAGREE and use dispute resolution",
    "7. RIGHT TO BRING ANYONE to IEP meetings (advocate, attorney)",
    "8. RIGHT TO REQUEST an IEP meeting at any time",
    "9. RIGHT TO A FREE APPROPRIATE PUBLIC EDUCATION (FAPE)",
    "10. RIGHT TO LEAST RESTRICTIVE ENVIRONMENT (LRE)", "",
    "IMPORTANT: Everything should be IN WRITING.",
    "Verbal promises mean nothing. If it's not in the IEP, it",
    "does not have to be provided.", "",
    "TIPS:",
    "- Always follow up conversations with a confirming email",
    "- Keep a binder of ALL correspondence and documents",
    "- Record meetings if your state allows (check state law)",
    "- You can say 'I need time to think about this' at any meeting",
    "- You do NOT have to sign the IEP the same day"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 5: Before the Meeting Checklist
pdf.new_page()
pdf.add_centered_text(750, "BEFORE THE MEETING CHECKLIST", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "PREPARATION IS YOUR SUPERPOWER. Do this before every IEP meeting:", "",
    "1 WEEK BEFORE:",
    "__ Request a draft IEP to review (you have this right!)",
    "__ Review current IEP goals and progress reports",
    "__ Gather any outside evaluations or reports",
    "__ Write down your concerns and priorities",
    "__ Prepare questions (see next pages)",
    "__ Invite your support person/advocate", "",
    "DAY BEFORE:",
    "__ Organize your binder (bring copies of everything)",
    "__ Write your 'parent statement' (what you want for your child)",
    "__ Review accommodations list - what's working? What's not?",
    "__ Get a good night's sleep (meetings are emotionally draining)", "",
    "BRING TO THE MEETING:",
    "__ This workbook and your notes",
    "__ Copy of current IEP",
    "__ Any outside evaluations/reports",
    "__ Work samples showing concerns",
    "__ Pen and paper for notes (or voice recorder if allowed)",
    "__ Water and snacks (meetings can be long!)",
    "__ A support person/advocate"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 6-7: Questions to Ask (50 questions)
pdf.new_page()
pdf.add_centered_text(750, "QUESTIONS TO ASK AT IEP MEETINGS", 'F2', 15)
pdf.add_centered_text(733, "Part 1: Goals, Services & Placement", 'F1', 10)
pdf.add_line(60, 725, 552, 725)
y = 707
questions1 = [
    "ABOUT PRESENT LEVELS:",
    "1. What data was used to determine present levels?",
    "2. How does my child compare to grade-level standards?",
    "3. What are my child's specific strengths?",
    "4. What are the areas of greatest need right now?",
    "5. How has my child progressed since last IEP?", "",
    "ABOUT GOALS:",
    "6. How was this goal developed? What data supports it?",
    "7. Is this goal measurable? How will progress be tracked?",
    "8. How often will I receive progress reports?",
    "9. What happens if my child meets the goal early?",
    "10. What happens if my child is not making progress?",
    "11. Are these goals ambitious enough?",
    "12. How do these goals connect to grade-level standards?", "",
    "ABOUT SERVICES:",
    "13. What specific services will be provided?",
    "14. How many minutes per week for each service?",
    "15. Will services be push-in or pull-out?",
    "16. What are the qualifications of the service providers?",
    "17. What happens when the provider is absent?",
    "18. Can we add ESY (Extended School Year) services?"
]
for line in questions1:
    pdf.add_text(60, y, line, 'F4', 9)
    y -= 14

pdf.new_page()
pdf.add_centered_text(750, "QUESTIONS TO ASK (continued)", 'F2', 15)
pdf.add_centered_text(733, "Part 2: Accommodations, Behavior & Transition", 'F1', 10)
pdf.add_line(60, 725, 552, 725)
y = 707
questions2 = [
    "ABOUT ACCOMMODATIONS:",
    "19. What accommodations are currently in place?",
    "20. How do we know if accommodations are being implemented?",
    "21. Can we add [specific accommodation] and why/why not?",
    "22. Will these accommodations apply to state testing?",
    "23. How are accommodations communicated to all teachers?", "",
    "ABOUT BEHAVIOR:",
    "24. Is a Functional Behavior Assessment (FBA) needed?",
    "25. Does my child need a Behavior Intervention Plan (BIP)?",
    "26. What positive behavior supports are in place?",
    "27. How are behaviors documented and communicated to me?",
    "28. What de-escalation strategies does staff use?", "",
    "ABOUT PLACEMENT:",
    "29. Why is this the least restrictive environment?",
    "30. What supports would allow more general ed time?",
    "31. Has a continuum of placement options been considered?", "",
    "ABOUT TRANSITION (age 14+):",
    "32. What are my child's post-secondary goals?",
    "33. What transition assessments have been done?",
    "34. What agencies should be involved?",
    "35. What independent living skills are being taught?", "",
    "POWER QUESTIONS:",
    "36. What does the research say about this approach?",
    "37. Where is that written in the IEP?",
    "38. Can you show me the data that supports this decision?"
]
for line in questions2:
    pdf.add_text(60, y, line, 'F4', 9)
    y -= 14


# Page 8: Goal Writing Guide (SMART Goals)
pdf.new_page()
pdf.add_centered_text(750, "GOAL WRITING GUIDE - SMART GOALS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "IEP goals must be SMART:", "",
    "S - SPECIFIC: What exactly will the child do?",
    "M - MEASURABLE: How will we know they achieved it? (%, frequency)",
    "A - ACHIEVABLE: Challenging but realistic for THIS child",
    "R - RELEVANT: Connected to the child's needs and curriculum",
    "T - TIME-BOUND: By when? (usually within one year)", "",
    "BAD GOAL: 'Student will improve reading.'",
    "GOOD GOAL: 'By [date], student will read grade-level passages",
    "at 90 words per minute with 95% accuracy, as measured by",
    "curriculum-based measurement probes, in 4 of 5 trials.'", "",
    "GOAL TEMPLATE:",
    "By [date], [student] will [specific skill/behavior]",
    "[condition/setting] to [measurable criteria]",
    "as measured by [assessment method] in [frequency].", "",
    "GOALS I WANT FOR MY CHILD:",
    "Area: Reading  Goal: __________________________",
    "_______________________________________________",
    "Area: Math  Goal: _____________________________",
    "_______________________________________________",
    "Area: Behavior  Goal: _________________________",
    "_______________________________________________",
    "Area: ________  Goal: _________________________",
    "_______________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 9: Accommodation vs Modification
pdf.new_page()
pdf.add_centered_text(750, "ACCOMMODATION vs MODIFICATION", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "These are NOT the same thing. Know the difference!", "",
    "ACCOMMODATION = Changes HOW a child learns",
    "(same content, same expectations, different access)",
    "Examples:",
    "- Extended time on tests",
    "- Preferential seating",
    "- Text-to-speech technology",
    "- Fidget tools allowed",
    "- Breaks between tasks",
    "- Reduced homework quantity (same difficulty)",
    "- Large print materials", "",
    "MODIFICATION = Changes WHAT a child learns",
    "(different content or lower expectations)",
    "Examples:",
    "- Simplified assignments",
    "- Alternate grading criteria",
    "- Different curriculum entirely",
    "- Fewer answer choices on tests", "",
    "WHY IT MATTERS:",
    "Accommodations do NOT affect grade-level diploma eligibility.",
    "Modifications MAY affect diploma type in some states.",
    "Always push for accommodations FIRST.", "",
    "MY CHILD'S ACCOMMODATIONS I'M REQUESTING:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 15

# Pages 10-14: Meeting Notes Template (5 pages)
for meeting in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(750, f"MEETING NOTES - MEETING {meeting}", 'F2', 14)
    pdf.add_line(60, 738, 552, 738)
    y = 718
    pdf.add_text(60, y, f"Date: ___/___/_____  Type: Annual / Amendment / Other", 'F4', 10)
    y -= 16
    pdf.add_text(60, y, "Attendees: ____________________________________", 'F4', 10)
    y -= 16
    pdf.add_text(60, y, "_______________________________________________", 'F4', 10)
    y -= 20
    pdf.add_text(60, y, "KEY DECISIONS MADE:", 'F2', 10)
    y -= 16
    for _ in range(4):
        pdf.add_line(60, y, 550, y, 0.5, 0.5)
        y -= 16
    y -= 8
    pdf.add_text(60, y, "WHAT WAS AGREED:", 'F2', 10)
    y -= 16
    for _ in range(4):
        pdf.add_line(60, y, 550, y, 0.5, 0.5)
        y -= 16
    y -= 8
    pdf.add_text(60, y, "WHAT I DISAGREED WITH:", 'F2', 10)
    y -= 16
    for _ in range(3):
        pdf.add_line(60, y, 550, y, 0.5, 0.5)
        y -= 16
    y -= 8
    pdf.add_text(60, y, "ACTION ITEMS / FOLLOW UP:", 'F2', 10)
    y -= 16
    for _ in range(4):
        pdf.add_line(60, y, 550, y, 0.5, 0.5)
        y -= 16
    pdf.add_text(60, y, "Did I sign? YES / NO   Reason if no: ___________", 'F4', 10)


# Page 15: Disagreement Resolution
pdf.new_page()
pdf.add_centered_text(750, "DISAGREEMENT RESOLUTION STEPS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "If you disagree with the school's decisions, you have options:", "",
    "STEP 1: Put your concerns IN WRITING",
    "Send a letter/email stating specifically what you disagree with",
    "and what you want instead. Keep it factual and professional.", "",
    "STEP 2: Request another IEP meeting",
    "You can request a meeting at any time to discuss concerns.", "",
    "STEP 3: Facilitated IEP meeting",
    "Request a neutral facilitator to guide the discussion.", "",
    "STEP 4: Mediation",
    "Free, voluntary process with a trained mediator.",
    "Both sides must agree to participate. Faster than due process.", "",
    "STEP 5: State Complaint",
    "File with your state education department. They investigate",
    "whether the school violated IDEA. Decision within 60 days.", "",
    "STEP 6: Due Process Hearing",
    "Formal legal hearing before an impartial hearing officer.",
    "Consider hiring a special education attorney for this step.", "",
    "REMEMBER:",
    "- Document EVERYTHING",
    "- Stay calm and professional (it's hard but essential)",
    "- Focus on your child's NEEDS, not blame",
    "- Get support: parent training centers, advocates"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 16: Child's Strengths & Needs Profile
pdf.new_page()
pdf.add_centered_text(750, "MY CHILD'S STRENGTHS & NEEDS PROFILE", 'F2', 14)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Bring this to every IEP meeting.", "",
    "CHILD'S NAME: _________________ AGE: ___ GRADE: ___",
    "DISABILITY CATEGORY: __________________________",
    "DATE QUALIFIED: _______________________________", "",
    "MY CHILD'S STRENGTHS (what they're GOOD at):",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "4. ____________________________________________", "",
    "MY CHILD'S INTERESTS & MOTIVATORS:",
    "_______________________________________________",
    "_______________________________________________", "",
    "MY CHILD'S CHALLENGES (biggest needs):",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________", "",
    "WHAT WORKS BEST FOR MY CHILD:",
    "Learning style: Visual / Auditory / Hands-on / Reading",
    "Best time of day: _________ Needs breaks every: ___min",
    "Motivated by: _________________________________",
    "Calmed by: ____________________________________", "",
    "MY #1 PRIORITY FOR THIS YEAR:",
    "_______________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book109_IEP_Parent_Guide.pdf')
print("Book109_IEP_Parent_Guide.pdf created successfully!")
