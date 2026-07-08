from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(480, "FOSTER PARENT", 'F2', 17)
pdf.add_centered_text(458, "DOCUMENTATION JOURNAL", 'F2', 15)
pdf.add_centered_text(430, "Track Everything That Matters", 'F4', 12)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(500, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: Child Placement Information
pdf.new_page()
pdf.add_centered_text(610, "CHILD PLACEMENT INFORMATION", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "CHILD INFORMATION:",
    "Name: ________________________________________",
    "DOB: ___/___/_____ Age at placement: ___________",
    "Placement date: ___/___/_____",
    "Placement type: Emergency / Temporary / Long-term / Pre-adopt", "",
    "CASE INFORMATION:",
    "Caseworker: ___________________________________",
    "Phone: _________________ Email: _______________",
    "Supervisor: ___________________________________",
    "Agency: _______________________________________",
    "Judge: ________________________________________",
    "CASA volunteer: _______________________________",
    "Case number: __________________________________", "",
    "BIOLOGICAL FAMILY:",
    "Birth mother: _________________________________",
    "Birth father: _________________________________",
    "Siblings (names/placement): ____________________",
    "_______________________________________________", "",
    "IMPORTANT NOTES:",
    "Allergies: ____________________________________",
    "Medications: __________________________________",
    "Diagnoses: ____________________________________",
    "Special needs: ________________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14

# Page 4: Medical Info
pdf.new_page()
pdf.add_centered_text(610, "MEDICAL INFORMATION LOG", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "DOCTORS:",
    "Pediatrician: _________________ Phone: ________",
    "Dentist: _____________________ Phone: ________",
    "Specialist: __________________ Phone: ________",
    "Therapist: ___________________ Phone: ________",
    "Insurance: ___________________ ID#: ___________", "",
    "IMMUNIZATION STATUS: Up to date? Y / N",
    "Missing: ______________________________________", "",
    "MEDICAL APPOINTMENTS:",
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14
for i in range(8):
    pdf.add_text(50, y, "Date: ___/___ Doctor: ________ Reason: ________ Outcome: ________", 'F3', 7)
    y -= 14

# Page 5: Educational Records
pdf.new_page()
pdf.add_centered_text(610, "EDUCATIONAL RECORDS", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "School: _______________________________________",
    "Grade: _____ Teacher: _________________________",
    "Principal: ____________________________________",
    "School counselor: _____________________________",
    "IEP/504? Y / N  Services: _____________________", "",
    "ACADEMIC PERFORMANCE:",
    "Reading level: _____ Math level: _______________",
    "Areas of strength: ____________________________",
    "Areas of concern: _____________________________", "",
    "ATTENDANCE:",
    "Days missed since placement: ___________________",
    "Reasons: ______________________________________", "",
    "BEHAVIORAL NOTES FROM SCHOOL:",
    "_______________________________________________",
    "_______________________________________________",
    "_______________________________________________", "",
    "SCHOOL COMMUNICATION LOG:",
    "Date: ___/___ With whom: ________ Topic: ________",
    "Date: ___/___ With whom: ________ Topic: ________",
    "Date: ___/___ With whom: ________ Topic: ________"
]:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 14


# Pages 6-15: Behavior Observation Log (10 pages)
for pg in range(1, 11):
    pdf.new_page()
    pdf.add_centered_text(610, f"BEHAVIOR OBSERVATION LOG - PAGE {pg}", 'F2', 12)
    pdf.add_line(50, 598, 382, 598)
    y = 582
    for entry in range(5):
        pdf.add_text(50, y, "Date: ___/___/___ Time: ___:___", 'F2', 8)
        y -= 12
        pdf.add_text(50, y, "Behavior: ____________________________________", 'F3', 8)
        y -= 11
        pdf.add_text(50, y, "Antecedent (what happened before): _____________", 'F3', 8)
        y -= 11
        pdf.add_text(50, y, "Consequence (what happened after): _____________", 'F3', 8)
        y -= 11
        pdf.add_text(50, y, "Duration: ______ Intensity (1-10): ___ Location: ___", 'F3', 8)
        y -= 14
        pdf.add_line(50, y+4, 382, y+4, 0.3, 0.7)
        y -= 8

# Pages 16-20: Visitation Log (5 pages)
for pg in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(610, f"VISITATION LOG - PAGE {pg}", 'F2', 12)
    pdf.add_line(50, 598, 382, 598)
    y = 582
    for entry in range(5):
        pdf.add_text(50, y, "Date: ___/___/___ Time: ___:___ to ___:___", 'F2', 8)
        y -= 12
        pdf.add_text(50, y, "Who visited: __________________________________", 'F3', 8)
        y -= 11
        pdf.add_text(50, y, "Location: _____________________________________", 'F3', 8)
        y -= 11
        pdf.add_text(50, y, "Child's reaction BEFORE: ______________________", 'F3', 8)
        y -= 11
        pdf.add_text(50, y, "Child's reaction AFTER: _______________________", 'F3', 8)
        y -= 11
        pdf.add_text(50, y, "Notes: ________________________________________", 'F3', 8)
        y -= 14
        pdf.add_line(50, y+4, 382, y+4, 0.3, 0.7)
        y -= 8

# Page 21: Communication with Agency Log
pdf.new_page()
pdf.add_centered_text(610, "COMMUNICATION WITH AGENCY LOG", 'F2', 12)
pdf.add_line(50, 598, 382, 598)
y = 580
for i in range(12):
    pdf.add_text(50, y, "Date: ___/___ Contact: __________ Method: Call/Email/Text", 'F3', 8)
    y -= 12
    pdf.add_text(50, y, "Topic: ________________________________________", 'F3', 8)
    y -= 12
    pdf.add_text(50, y, "Outcome/Action: _______________________________", 'F3', 8)
    y -= 16
    pdf.add_line(50, y+5, 382, y+5, 0.2, 0.7)
    y -= 6

# Page 22: Court + Milestones + Medication
pdf.new_page()
pdf.add_centered_text(610, "COURT DATES & MILESTONES", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
pdf.add_text(50, y, "COURT DATE TRACKER:", 'F2', 10)
y -= 15
for i in range(5):
    pdf.add_text(50, y, f"Date: ___/___/___ Type: ________ Outcome: ________", 'F3', 8)
    y -= 14
y -= 10
pdf.add_text(50, y, "MILESTONES & PROGRESS:", 'F2', 10)
y -= 15
for i in range(6):
    pdf.add_text(50, y, f"Date: ___/___ Milestone: _______________________", 'F3', 8)
    y -= 14
y -= 10
pdf.add_text(50, y, "MEDICATION LOG:", 'F2', 10)
y -= 15
for i in range(4):
    pdf.add_text(50, y, "Med: ____________ Dose: ____ Time: ____ Prescriber: ____", 'F3', 8)
    y -= 14

# Page 23: Important Contacts + Mileage
pdf.new_page()
pdf.add_centered_text(610, "CONTACTS & MILEAGE/EXPENSES", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
pdf.add_text(50, y, "IMPORTANT CONTACTS:", 'F2', 10)
y -= 15
contacts = ["Caseworker", "CASA", "Attorney/GAL", "Therapist", "School", "Agency after-hours"]
for c in contacts:
    pdf.add_text(50, y, f"{c}: __________________ Ph: __________________", 'F3', 8)
    y -= 13
y -= 10
pdf.add_text(50, y, "MILEAGE/EXPENSE TRACKER:", 'F2', 10)
y -= 15
for i in range(10):
    pdf.add_text(50, y, "Date: ___/___ Purpose: __________ Miles: ___ Cost: $___", 'F3', 8)
    y -= 13

# Page 24: Self-Care for Foster Parents
pdf.new_page()
pdf.add_centered_text(610, "SELF-CARE FOR FOSTER PARENTS", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "You cannot pour from an empty cup. Your well-being matters.", "",
    "SIGNS YOU NEED A BREAK:",
    "- Feeling resentful or emotionally numb",
    "- Snapping at small things",
    "- Difficulty sleeping (not related to child's needs)",
    "- Feeling isolated or unsupported",
    "- Questioning if you can keep doing this", "",
    "SELF-CARE IDEAS:",
    "__ Respite care (ASK FOR IT - you deserve it)",
    "__ Support group for foster parents",
    "__ Time alone (even 30 minutes)",
    "__ Talk to someone who understands",
    "__ Physical activity",
    "__ Therapy for YOU (not just the child)", "",
    "MY SELF-CARE COMMITMENT:",
    "Weekly: _______________________________________",
    "Monthly: ______________________________________",
    "My respite contact: ___________________________", "",
    "You are doing sacred, hard, important work.",
    "Thank you for showing up for this child."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book114_Foster_Parent_Journal.pdf')
print("Book114_Foster_Parent_Journal.pdf created successfully!")
