"""
Book 8: Sobriety Tracker & Recovery Journal
KDP Interior - 6x9 inches (432x648 points)
Daily check-ins, milestone celebrations, gratitude, trigger tracking
"""
from pdf_utils import PDFDoc

def create_sobriety_journal():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "ONE DAY AT A TIME", font='F2', size=22)
    pdf.add_centered_text(485, "SOBRIETY TRACKER", font='F2', size=28)
    pdf.add_centered_text(445, "& RECOVERY JOURNAL", font='F2', size=20)
    pdf.add_line(100, 425, 332, 425, 2)
    pdf.add_centered_text(395, "Daily Check-Ins | Milestone Celebrations", font='F1', size=11)
    pdf.add_centered_text(372, "Trigger Tracking | Gratitude & Reflection", font='F1', size=11)
    pdf.add_centered_text(340, "365 Days of Guided Support", font='F1', size=11)
    pdf.add_centered_text(250, "By", font='F1', size=11)
    pdf.add_centered_text(228, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(150, "My Sobriety Start Date:", font='F1', size=13)
    pdf.add_line(140, 130, 292, 130, 0.8)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(520, "One Day at a Time: Sobriety Tracker", font='F2', size=12)
    pdf.add_centered_text(495, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(430, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(405, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(360, "You are not alone. You are stronger than you know.", font='F1', size=10)

    # --- DEDICATION ---
    pdf.new_page()
    pdf.add_centered_text(400, "For everyone fighting the fight.", font='F2', size=14)
    pdf.add_centered_text(370, "Every single day sober is a victory.", font='F1', size=13)
    pdf.add_centered_text(340, "Be proud of how far you've come.", font='F1', size=13)

    # --- DAILY CHECK-IN PAGES (30 pages) ---
    for day in range(1, 31):
        pdf.new_page()
        pdf.add_text(60, 610, f"Day {day}", font='F2', size=16)
        pdf.add_text(280, 610, "Date: ___/___/______", font='F1', size=10)
        pdf.add_line(60, 598, 372, 598, 0.8)

        # Mood check
        pdf.add_text(60, 572, "Today's Mood (1-10): _____", font='F1', size=11)
        pdf.add_text(60, 548, "Hours of Sleep: _____", font='F1', size=11)
        pdf.add_text(60, 524, "Cravings Today (1-10): _____", font='F1', size=11)

        # Gratitude
        pdf.add_text(60, 490, "3 Things I'm Grateful For:", font='F2', size=11)
        pdf.add_text(70, 467, "1.", font='F1', size=10)
        pdf.add_line(85, 464, 372, 464, 0.3, gray=0.5)
        pdf.add_text(70, 444, "2.", font='F1', size=10)
        pdf.add_line(85, 441, 372, 441, 0.3, gray=0.5)
        pdf.add_text(70, 421, "3.", font='F1', size=10)
        pdf.add_line(85, 418, 372, 418, 0.3, gray=0.5)

        # Triggers
        pdf.add_text(60, 388, "Triggers I Faced:", font='F2', size=11)
        pdf.add_line(60, 365, 372, 365, 0.3, gray=0.5)
        pdf.add_line(60, 342, 372, 342, 0.3, gray=0.5)

        # Coping strategies
        pdf.add_text(60, 312, "How I Coped:", font='F2', size=11)
        pdf.add_line(60, 289, 372, 289, 0.3, gray=0.5)
        pdf.add_line(60, 266, 372, 266, 0.3, gray=0.5)

        # Free reflection
        pdf.add_text(60, 236, "Today's Reflection:", font='F2', size=11)
        for ln in range(5):
            pdf.add_line(60, 213 - ln * 25, 372, 213 - ln * 25, 0.3, gray=0.5)

        # Affirmation
        pdf.add_text(60, 75, "Tomorrow I will: ________________________________", font='F1', size=10)
        pdf.add_centered_text(35, f"- {day + 3} -", font='F1', size=8)

    # --- MILESTONE PAGES ---
    milestones = [
        ("24 Hours", "The hardest step is the first one. You did it."),
        ("1 Week", "Seven days of choosing yourself. Keep going."),
        ("30 Days", "A full month! Your body and mind are healing."),
        ("90 Days", "You've built new habits. You're unstoppable."),
        ("6 Months", "Half a year of freedom. Celebrate this!"),
        ("1 Year", "365 days. You are proof that change is possible."),
    ]
    for title, quote in milestones:
        pdf.new_page()
        pdf.add_centered_text(500, "MILESTONE", font='F2', size=14)
        pdf.add_centered_text(460, title, font='F2', size=28)
        pdf.add_line(130, 440, 302, 440, 1)
        pdf.add_centered_text(410, quote, font='F1', size=12)
        pdf.add_text(60, 360, "Date Achieved: ________________", font='F1', size=11)
        pdf.add_text(60, 330, "How I Feel:", font='F2', size=11)
        for ln in range(6):
            pdf.add_line(60, 305 - ln * 28, 372, 305 - ln * 28, 0.3, gray=0.5)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(450, "You Are Enough.", font='F2', size=22)
    pdf.add_centered_text(410, "Recovery is not a straight line.", font='F1', size=13)
    pdf.add_centered_text(385, "Be gentle with yourself on hard days.", font='F1', size=13)
    pdf.add_centered_text(340, "If this journal helped you,", font='F1', size=11)
    pdf.add_centered_text(318, "please consider leaving a review.", font='F1', size=11)
    pdf.add_centered_text(270, "Crisis Resources:", font='F2', size=12)
    pdf.add_centered_text(247, "SAMHSA Helpline: 1-800-662-4357", font='F1', size=11)
    pdf.add_centered_text(225, "Crisis Text Line: Text HOME to 741741", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book8_Sobriety_Tracker.pdf')
    print("Book 8 created: Book8_Sobriety_Tracker.pdf")

if __name__ == '__main__':
    create_sobriety_journal()
