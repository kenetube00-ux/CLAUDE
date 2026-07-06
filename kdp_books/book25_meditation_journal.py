"""
Book 25: MINDFULNESS & MEDITATION JOURNAL
KDP Interior - 6x9 inches (432x648 points)
Title page + copyright + 60 session log pages
"""
from pdf_utils import PDFDoc

def create_meditation_journal():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "MINDFULNESS &", font='F2', size=24)
    pdf.add_centered_text(495, "MEDITATION JOURNAL", font='F2', size=24)
    pdf.add_line(100, 475, 332, 475, 2)
    pdf.add_centered_text(445, "Track Your Inner Journey", font='F4', size=14)
    pdf.add_centered_text(390, "60 Session Logs", font='F1', size=11)
    pdf.add_centered_text(368, "Mood Tracking & Insights", font='F1', size=11)
    pdf.add_centered_text(346, "Gratitude & Awareness", font='F1', size=11)
    pdf.add_centered_text(270, "By", font='F1', size=11)
    pdf.add_centered_text(248, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "MINDFULNESS & MEDITATION JOURNAL", font='F2', size=11)
    pdf.add_centered_text(498, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(440, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(420, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(385, "Be present. Be mindful.", font='F4', size=10)

    # --- 60 SESSION LOG PAGES ---
    for entry in range(1, 61):
        pdf.new_page()
        pdf.add_text(60, 615, f"SESSION #{entry}", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 578

        # Date
        pdf.add_text(60, y, "Date:", font='F2', size=10)
        pdf.add_line(95, y - 2, 220, y - 2, 0.3, gray=0.5)
        # Duration
        pdf.add_text(240, y, "Duration:", font='F2', size=10)
        pdf.add_line(295, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Type of meditation
        pdf.add_text(60, y, "Type of Meditation:", font='F2', size=10)
        pdf.add_line(170, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Intention
        pdf.add_text(60, y, "Intention:", font='F2', size=10)
        pdf.add_line(115, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 28

        # Pre-session mood
        pdf.add_text(60, y, "Pre-Session Mood (1-10):", font='F2', size=10)
        pdf.add_line(210, y - 2, 260, y - 2, 0.3, gray=0.5)
        y -= 26

        # Post-session mood
        pdf.add_text(60, y, "Post-Session Mood (1-10):", font='F2', size=10)
        pdf.add_line(215, y - 2, 265, y - 2, 0.3, gray=0.5)
        y -= 30

        # Thoughts that arose
        pdf.add_text(60, y, "Thoughts That Arose:", font='F2', size=10)
        y -= 18
        for i in range(3):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 20
        y -= 8

        # Insights/awareness
        pdf.add_text(60, y, "Insights / Awareness:", font='F2', size=10)
        y -= 18
        for i in range(3):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 20
        y -= 8

        # Body sensations
        pdf.add_text(60, y, "Body Sensations:", font='F2', size=10)
        pdf.add_line(150, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 30

        # Gratitude
        pdf.add_text(60, y, "Gratitude:", font='F2', size=10)
        y -= 18
        for i in range(2):
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 20

        # Page number
        pdf.add_centered_text(30, f"- {entry + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book25_Meditation_Journal.pdf')
    print("Book 25 created: Book25_Meditation_Journal.pdf")

if __name__ == '__main__':
    create_meditation_journal()
