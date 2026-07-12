"""Book 225: The Complete IEP Toolkit for Parents"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.15)
    doc.add_centered_text(755, "THE COMPLETE IEP TOOLKIT", 'F2', 22, 1)
    doc.add_centered_text(722, "FOR PARENTS", 'F2', 22, 1)
    doc.add_centered_text(660, "Know Your Rights, Track Progress, Advocate Effectively", 'F4', 13, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    doc.new_page()
    doc.add_centered_text(700, "THE COMPLETE IEP TOOLKIT FOR PARENTS", 'F2', 13)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # Rights under IDEA
    doc.new_page()
    doc.add_centered_text(750, "YOUR RIGHTS UNDER IDEA - PLAIN LANGUAGE", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    rights = [
        "1. FREE APPROPRIATE PUBLIC EDUCATION (FAPE) - Your child deserves",
        "   a free education designed to meet their unique needs.",
        "2. EVALUATION - You can request an evaluation at any time. The school",
        "   must respond within their state timeline.",
        "3. PARTICIPATION - You are an EQUAL member of the IEP team. Your",
        "   input matters as much as any professional's.",
        "4. INFORMED CONSENT - Nothing happens without your written permission.",
        "5. PRIOR WRITTEN NOTICE - School must tell you IN WRITING before",
        "   changing (or refusing to change) your child's services.",
        "6. LEAST RESTRICTIVE ENVIRONMENT - Your child should be with",
        "   non-disabled peers to the maximum extent appropriate.",
        "7. DISPUTE RESOLUTION - You can disagree! Options: mediation,",
        "   due process hearing, state complaint.",
        "8. STAY PUT - During disputes, child stays in current placement.",
        "9. INDEPENDENT EVALUATION - You can get an outside evaluation",
        "   at district expense if you disagree with theirs.",
        "10. TRANSFER OF RIGHTS - At 18, rights transfer to student.",
    ]
    for line in rights:
        doc.add_text(72, y, line, 'F1', 9)
        y -= 14

    # IEP Meeting Prep
    doc.new_page()
    doc.add_centered_text(750, "IEP MEETING PREPARATION WORKSHEET", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    items = [
        "Meeting date: ___/___/___  Time: ___  Location: _______________",
        "Meeting type: [ ] Initial [ ] Annual [ ] Triennial [ ] Amendment [ ] Other", "",
        "MY PRIORITIES FOR THIS MEETING:",
        "1. ________________________________",
        "2. ________________________________",
        "3. ________________________________", "",
        "DOCUMENTS TO BRING:",
        "[ ] Current IEP copy  [ ] Progress reports  [ ] Report cards",
        "[ ] Private evaluations  [ ] Work samples  [ ] Medical records",
        "[ ] Communication log  [ ] My notes  [ ] Parent rights booklet", "",
        "TEAM MEMBERS EXPECTED:",
        "________________________________", "________________________________", "",
        "QUESTIONS I MUST ASK:", "________________________________",
        "________________________________", "________________________________",
    ]
    for item in items:
        doc.add_text(72, y, item, 'F1', 10)
        y -= 16


    # 100 Questions (2 pages)
    questions_by_cat = {
        "PRESENT LEVELS": [
            "What are my child's current academic levels?",
            "How were these levels determined?",
            "What assessments were used?",
            "How does my child compare to grade-level peers?",
            "What are my child's strengths?",
        ],
        "GOALS": [
            "How is this goal measurable?",
            "What is the baseline for this goal?",
            "How often will progress be reported?",
            "Who is responsible for implementing this goal?",
            "What happens if the goal isn't met?",
        ],
        "SERVICES": [
            "How many minutes per week of each service?",
            "Is it push-in or pull-out?",
            "Who provides the service (credential)?",
            "What happens when the provider is absent?",
            "Can services be increased if needed?",
        ],
        "ACCOMMODATIONS": [
            "How will this accommodation be implemented daily?",
            "Who ensures the accommodation is provided?",
            "How will we know if it's working?",
            "Are these accommodations also for testing?",
            "Can accommodations be added mid-year?",
        ],
        "PLACEMENT": [
            "What percentage of time in general education?",
            "What supports exist in general ed classroom?",
            "Why was this placement chosen over less restrictive?",
            "What would need to happen to move to less restrictive?",
            "How is my child included in non-academic activities?",
        ],
    }
    for pg in range(2):
        doc.new_page()
        doc.add_centered_text(755, f"100 QUESTIONS FOR IEP MEETINGS - PAGE {pg+1}", 'F2', 12)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        cats = list(questions_by_cat.items())
        page_cats = cats[pg*3:(pg+1)*3] if pg == 0 else cats[3:]
        for cat_name, questions in page_cats:
            doc.add_text(72, y, cat_name, 'F2', 9)
            y -= 14
            for q in questions:
                doc.add_text(90, y, f"- {q}", 'F1', 8)
                y -= 12
            y -= 10

    # Goal Writing Guide
    doc.new_page()
    doc.add_centered_text(750, "GOAL WRITING GUIDE - SMART FORMAT", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = [
        "S - Specific: What exactly will the child do?",
        "M - Measurable: How will we measure it? (%, frequency, accuracy)",
        "A - Achievable: Can the child reach this in one year?",
        "R - Relevant: Does this address the child's identified needs?",
        "T - Time-bound: By when? (usually annual review date)", "",
        "FORMULA: By [date], [child] will [specific skill] with [accuracy]",
        "as measured by [method] in [setting] given [supports].", "",
        "EXAMPLE: By 12/15/2025, Johnny will read a grade-level passage",
        "with 95% accuracy as measured by curriculum-based measures", 
        "in the resource room given no additional prompts.", "",
        "MY CHILD'S GOAL DRAFTS:",
        "Goal 1: By ___/___, _______ will _______________________",
        "with ___% accuracy as measured by _______________________", "",
        "Goal 2: By ___/___, _______ will _______________________",
        "with ___% accuracy as measured by _______________________",
    ]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Goal Tracking Pages (10 pages)
    for g in range(1, 11):
        doc.new_page()
        doc.add_centered_text(755, f"IEP GOAL TRACKING - GOAL {g}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        doc.add_text(72, y, "Goal: ________________________________", 'F1', 10)
        y -= 14
        doc.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
        doc.add_text(72, y, f"Baseline: __________  Target: __________  By date: ___/___/___", 'F1', 10)
        y -= 18
        doc.add_text(72, y, "Measurement method: ________________________________", 'F1', 10)
        y -= 25
        doc.add_text(72, y, "MONTHLY DATA:", 'F2', 10)
        y -= 18
        for month in ["Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr","May","Jun"]:
            doc.add_text(72, y, f"{month}: Score/Level: _____  Notes: _______________________", 'F1', 9)
            y -= 16
        y -= 15
        doc.add_text(72, y, "GOAL MET? [ ] Yes [ ] No [ ] Partial  New goal needed? [ ] Yes", 'F1', 10)


    # Accommodation Effectiveness Tracker
    doc.new_page()
    doc.add_centered_text(755, "ACCOMMODATION EFFECTIVENESS TRACKER", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    for a in range(1, 9):
        doc.add_text(72, y, f"Accommodation {a}: ________________________________", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Being provided consistently? [ ] Yes [ ] Sometimes [ ] No", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Effectiveness: [ ] Very [ ] Somewhat [ ] Not helpful", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Notes: ________________________________", 'F1', 8)
        y -= 20

    # Related Services Log
    doc.new_page()
    doc.add_centered_text(755, "RELATED SERVICES LOG", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    services = ["Speech/Language", "Occupational Therapy", "Physical Therapy",
                "Counseling", "Adaptive PE", "Other: ___________"]
    for svc in services:
        doc.add_text(72, y, f"{svc}", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "IEP says: ___min/week  Actually received: ___min/week", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Missed sessions this month: ___  Made up? [ ] Yes [ ] No", 'F1', 8)
        y -= 20

    # Communication Log (5 pages)
    for pg in range(1, 6):
        doc.new_page()
        doc.add_centered_text(755, f"COMMUNICATION LOG WITH SCHOOL - PAGE {pg}", 'F2', 12)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        for _ in range(6):
            doc.add_text(72, y, "Date: ___/___  With: ______________ Role: ______________", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Method: [ ] Email [ ] Phone [ ] In-person [ ] Written note", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Topic: ________________________________", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Their response: ________________________________", 'F1', 9)
            y -= 14
            doc.add_text(72, y, "Next steps: ________________________________", 'F1', 9)
            y -= 22

    # Disagreement Resolution + Due Process
    doc.new_page()
    doc.add_centered_text(750, "DISAGREEMENT RESOLUTION & DUE PROCESS", 'F2', 13)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = [
        "STEPS WHEN YOU DISAGREE:", "",
        "Step 1: Put your concerns in WRITING (Prior Written Notice)",
        "Step 2: Request a meeting to discuss",
        "Step 3: If unresolved, options are:", "",
        "  MEDIATION - Free, voluntary, neutral mediator",
        "  STATE COMPLAINT - File with state dept of education",
        "  DUE PROCESS - Formal hearing before judge", "",
        "IMPORTANT TIMELINES:",
        "  - File complaint within 2 years of violation",
        "  - School must respond within 10 days of formal request",
        "  - Due process hearing within 45 days of request", "",
        "MY DISAGREEMENT TRACKER:",
        "Issue: ________________________________",
        "Date raised: ___/___  With whom: ______________",
        "School's response: ________________________________",
        "Resolution: [ ] Resolved [ ] Escalating to: ___________",
    ]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Annual Review + Transition + Strengths + Team Contacts
    doc.new_page()
    doc.add_centered_text(750, "ANNUAL REVIEW & TRANSITION PLANNING", 'F2', 13)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "ANNUAL REVIEW PREPARATION:", 'F2', 10)
    y -= 16
    checklist = ["[ ] Review all current goals - which are met?",
        "[ ] Gather work samples showing progress/struggles",
        "[ ] List new concerns since last meeting",
        "[ ] Draft new goals I want to propose",
        "[ ] Update accommodations that aren't working",
        "[ ] Request any new evaluations needed"]
    for item in checklist:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 14
    y -= 15
    doc.add_text(72, y, "TRANSITION PLANNING (Ages 14+):", 'F2', 10)
    y -= 16
    trans = ["Post-secondary goal: ________________________________",
        "Employment goal: ________________________________",
        "Independent living: ________________________________",
        "Transition services needed: ________________________________",
        "Agency connections: ________________________________"]
    for item in trans:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 14

    # Strengths Profile + Team Contacts
    doc.new_page()
    doc.add_centered_text(750, "MY CHILD'S PROFILE & TEAM", 'F2', 13)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "MY CHILD'S STRENGTHS:", 'F2', 10)
    y -= 16
    for _ in range(5):
        doc.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 16
    y -= 10
    doc.add_text(72, y, "MY CHILD'S NEEDS:", 'F2', 10)
    y -= 16
    for _ in range(5):
        doc.add_line(90, y, 540, y, 0.5, 0.5)
        y -= 16
    y -= 10
    doc.add_text(72, y, "PROFESSIONAL TEAM CONTACTS:", 'F2', 10)
    y -= 16
    team = ["Special Ed Teacher", "General Ed Teacher", "School Psychologist",
            "Speech Therapist", "OT", "Counselor", "Principal", "Advocate/Attorney"]
    for role in team:
        doc.add_text(90, y, f"{role}: ______________ Ph: ______________", 'F1', 9)
        y -= 14

    doc.save("Book225_IEP_Complete_Parent_Guide.pdf")
    print("Created: Book225_IEP_Complete_Parent_Guide.pdf")

if __name__ == "__main__":
    create_book()
