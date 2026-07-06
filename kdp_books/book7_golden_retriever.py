"""
Book 7: Golden Retriever Owner's Journal
KDP Interior - 6x9 inches (432x648 points)
Dog breed-specific journal - vet visits, memories, training log
"""
from pdf_utils import PDFDoc

def create_dog_journal():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(540, "GOLDEN RETRIEVER", font='F2', size=26)
    pdf.add_centered_text(500, "OWNER'S JOURNAL", font='F2', size=24)
    pdf.add_line(100, 480, 332, 480, 2)
    pdf.add_centered_text(450, "Health Records | Training Log | Memories", font='F1', size=12)
    pdf.add_centered_text(425, "Vet Visits | Milestones | Photo Notes", font='F1', size=12)
    pdf.add_centered_text(380, "A Complete Life Record for Your Golden", font='F1', size=11)
    pdf.add_centered_text(250, "By", font='F1', size=11)
    pdf.add_centered_text(228, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(160, "Dog's Name: ______________________", font='F1', size=13)
    pdf.add_centered_text(130, "Owner: ___________________________", font='F1', size=13)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(520, "Golden Retriever Owner's Journal", font='F2', size=13)
    pdf.add_centered_text(495, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(430, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(405, "Published via Amazon KDP", font='F1', size=9)

    # --- DOG PROFILE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(610, "My Golden Retriever", font='F2', size=18)
    pdf.add_line(60, 595, 372, 595, 1)
    fields = [
        "Name:", "Breed Color:", "Date of Birth:", "Adoption Date:",
        "Breeder/Rescue:", "Microchip #:", "Registration #:",
        "Weight:", "Favorite Toy:", "Favorite Treat:",
        "Personality:", "Special Markings:",
    ]
    y = 565
    for field in fields:
        pdf.add_text(60, y, field, font='F2', size=11)
        pdf.add_line(180, y - 3, 372, y - 3, 0.4, gray=0.5)
        y -= 35

    # --- VET VISIT PAGES (10 pages) ---
    for i in range(10):
        pdf.new_page()
        pdf.add_centered_text(610, f"Vet Visit #{i+1}", font='F2', size=14)
        pdf.add_line(60, 595, 372, 595, 0.8)
        vet_fields = [
            ("Date:", 560), ("Vet/Clinic:", 530), ("Reason:", 500),
            ("Weight:", 470), ("Temperature:", 440),
            ("Vaccinations Given:", 410), ("Medications:", 370),
            ("Diagnosis:", 330), ("Next Appointment:", 290),
            ("Cost:", 260),
        ]
        for label, fy in vet_fields:
            pdf.add_text(60, fy, label, font='F2', size=10)
            pdf.add_line(170, fy - 3, 372, fy - 3, 0.4, gray=0.5)
        pdf.add_text(60, 220, "Notes:", font='F2', size=10)
        for ln in range(4):
            pdf.add_line(60, 195 - ln * 25, 372, 195 - ln * 25, 0.3, gray=0.5)
        pdf.add_centered_text(35, f"- {i + 4} -", font='F1', size=8)

    # --- TRAINING LOG (8 pages) ---
    training_areas = [
        "Sit & Stay", "Come/Recall", "Leash Walking",
        "Fetch & Drop", "Crate Training", "House Training",
        "Socialization", "Tricks & Commands",
    ]
    for i, area in enumerate(training_areas):
        pdf.new_page()
        pdf.add_centered_text(610, f"Training Log: {area}", font='F2', size=14)
        pdf.add_line(60, 595, 372, 595, 0.8)
        # Training table
        pdf.add_text(60, 570, "Date", font='F2', size=10)
        pdf.add_text(130, 570, "Duration", font='F2', size=10)
        pdf.add_text(210, 570, "Progress (1-5)", font='F2', size=10)
        pdf.add_text(320, 570, "Notes", font='F2', size=10)
        pdf.add_line(60, 562, 372, 562, 0.5)
        y = 545
        for row in range(16):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 30
        pdf.add_centered_text(35, f"- {i + 14} -", font='F1', size=8)

    # --- MILESTONE PAGES (5 pages) ---
    milestones = [
        "First Day Home", "First Walk Outside", "First Trick Learned",
        "First Birthday", "Favorite Memory Together",
    ]
    for i, milestone in enumerate(milestones):
        pdf.new_page()
        pdf.add_centered_text(610, milestone, font='F2', size=16)
        pdf.add_line(100, 590, 332, 590, 1)
        pdf.add_text(60, 560, "Date: _______________", font='F1', size=11)
        pdf.add_text(60, 530, "Age: ________________", font='F1', size=11)
        pdf.add_text(60, 490, "What happened:", font='F2', size=11)
        for ln in range(12):
            pdf.add_line(60, 460 - ln * 28, 372, 460 - ln * 28, 0.3, gray=0.5)
        pdf.add_centered_text(35, f"- {i + 22} -", font='F1', size=8)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(450, "Cherish Every Moment", font='F2', size=20)
    pdf.add_centered_text(415, "with your Golden Retriever.", font='F1', size=14)
    pdf.add_centered_text(370, "If you loved this journal, please leave a review!", font='F1', size=11)
    pdf.add_centered_text(330, "Also available:", font='F2', size=12)
    pdf.add_centered_text(305, "- Labrador Retriever Owner's Journal", font='F1', size=11)
    pdf.add_centered_text(283, "- German Shepherd Owner's Journal", font='F1', size=11)
    pdf.add_centered_text(261, "- French Bulldog Owner's Journal", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book7_Golden_Retriever_Journal.pdf')
    print("Book 7 created: Book7_Golden_Retriever_Journal.pdf")

if __name__ == '__main__':
    create_dog_journal()
