"""
Book 34: My Anxiety Workbook - Daily Tools for Calmer Days
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(540, "MY ANXIETY", font='F2', size=28)
    pdf.add_centered_text(500, "WORKBOOK", font='F2', size=28)
    pdf.add_line(100, 480, 332, 480, 2)
    pdf.add_centered_text(450, "Daily Tools for Calmer Days", font='F4', size=16)
    pdf.add_centered_text(415, "30-Day Guided Journal for Managing Worry,", font='F1', size=11)
    pdf.add_centered_text(395, "Panic & Anxious Thoughts", font='F1', size=11)
    pdf.add_centered_text(350, "CBT & Grounding Exercises Included", font='F1', size=10)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(235, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "My Anxiety Workbook", font='F2', size=14)
    pdf.add_centered_text(475, "Daily Tools for Calmer Days", font='F1', size=11)
    pdf.add_centered_text(450, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(420, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(395, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(370, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(340, "DISCLAIMER: This book is not a substitute for professional", font='F1', size=8)
    pdf.add_centered_text(325, "mental health treatment. If you are in crisis, please", font='F1', size=8)
    pdf.add_centered_text(310, "contact a mental health professional or call 988.", font='F1', size=8)

    # --- 30 DAILY PAGES ---
    for day in range(1, 31):
        pdf.new_page()
        pdf.add_text(60, 615, f"Day {day}", font='F2', size=14)
        pdf.add_text(280, 615, "Date: ___/___/______", font='F1', size=10)
        pdf.add_line(60, 605, 372, 605, 1)

        y = 582
        # Anxiety level
        pdf.add_text(60, y, "Anxiety Level (1-10):", font='F2', size=10)
        pdf.add_text(205, y, "1  2  3  4  5  6  7  8  9  10", font='F3', size=9)
        y -= 22

        # Trigger
        pdf.add_text(60, y, "Trigger:", font='F2', size=10)
        pdf.add_text(115, y, "_________________________________________", font='F1', size=9)
        y -= 22

        # Physical symptoms checklist
        pdf.add_text(60, y, "Physical Symptoms:", font='F2', size=10)
        y -= 16
        pdf.add_text(70, y, "[ ] Racing heart   [ ] Tight chest   [ ] Sweating", font='F3', size=8)
        y -= 14
        pdf.add_text(70, y, "[ ] Nausea         [ ] Dizziness     [ ] Other: _______", font='F3', size=8)
        y -= 22

        # Negative thought
        pdf.add_text(60, y, "Negative Thought:", font='F2', size=10)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 20

        # Reframed thought
        pdf.add_text(60, y, "Reframed Thought:", font='F2', size=10)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 20

        # Coping strategy
        pdf.add_text(60, y, "Coping Strategy Used:", font='F2', size=10)
        pdf.add_text(200, y, "___________________________", font='F1', size=9)
        y -= 22

        # Grounding exercise 5-4-3-2-1
        pdf.add_text(60, y, "Grounding Exercise (5-4-3-2-1):", font='F2', size=10)
        y -= 16
        pdf.add_text(70, y, "5 things I SEE:", font='F5', size=8)
        pdf.add_text(155, y, "________________________________", font='F1', size=8)
        y -= 14
        pdf.add_text(70, y, "4 things I HEAR:", font='F5', size=8)
        pdf.add_text(160, y, "_______________________________", font='F1', size=8)
        y -= 14
        pdf.add_text(70, y, "3 things I TOUCH:", font='F5', size=8)
        pdf.add_text(165, y, "______________________________", font='F1', size=8)
        y -= 14
        pdf.add_text(70, y, "2 things I SMELL:", font='F5', size=8)
        pdf.add_text(163, y, "______________________________", font='F1', size=8)
        y -= 14
        pdf.add_text(70, y, "1 thing I TASTE:", font='F5', size=8)
        pdf.add_text(158, y, "_______________________________", font='F1', size=8)
        y -= 22

        # Evening rating
        pdf.add_text(60, y, "Evening Rating (1-10):", font='F2', size=10)
        pdf.add_text(210, y, "1  2  3  4  5  6  7  8  9  10", font='F3', size=9)
        y -= 22

        # Wins of the day
        pdf.add_text(60, y, "Wins of the Day:", font='F2', size=10)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)

        pdf.add_centered_text(35, f"- {day + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book34_Anxiety_Workbook.pdf')
    print("Book 34 created: Book34_Anxiety_Workbook.pdf")

if __name__ == '__main__':
    create_book()
