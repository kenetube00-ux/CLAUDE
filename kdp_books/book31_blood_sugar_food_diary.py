"""
Book 31: Blood Sugar & Food Diary - Type 2 Diabetes Daily Tracker
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(540, "BLOOD SUGAR", font='F2', size=28)
    pdf.add_centered_text(500, "&", font='F2', size=18)
    pdf.add_centered_text(465, "FOOD DIARY", font='F2', size=28)
    pdf.add_line(100, 445, 332, 445, 2)
    pdf.add_centered_text(415, "Type 2 Diabetes Daily Tracker", font='F1', size=14)
    pdf.add_centered_text(385, "90 Days of Glucose, Meals & Wellness Tracking", font='F1', size=10)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(235, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(150, "Name: ______________________", font='F1', size=12)
    pdf.add_centered_text(125, "Doctor: _____________________", font='F1', size=12)
    pdf.add_centered_text(100, "Phone: _____________________", font='F1', size=12)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "Blood Sugar & Food Diary", font='F2', size=14)
    pdf.add_centered_text(475, "Type 2 Diabetes Daily Tracker", font='F1', size=11)
    pdf.add_centered_text(450, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(420, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(395, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(370, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(340, "DISCLAIMER: This book is not a substitute for professional", font='F1', size=8)
    pdf.add_centered_text(325, "medical advice. Consult your healthcare provider.", font='F1', size=8)

    # --- 90 DAILY PAGES ---
    for day in range(1, 91):
        pdf.new_page()
        pdf.add_text(60, 615, f"Day {day}", font='F2', size=14)
        pdf.add_text(280, 615, "Date: ___/___/______", font='F1', size=10)
        pdf.add_line(60, 605, 372, 605, 1)

        y = 580
        # Fasting glucose
        pdf.add_text(60, y, "Fasting Glucose:", font='F2', size=10)
        pdf.add_text(180, y, "_______ mg/dL", font='F1', size=10)
        y -= 30

        # Breakfast
        pdf.add_text(60, y, "BREAKFAST", font='F2', size=10)
        y -= 18
        pdf.add_text(70, y, "Before:", font='F1', size=9)
        pdf.add_text(115, y, "_____ mg/dL", font='F1', size=9)
        pdf.add_text(220, y, "After:", font='F1', size=9)
        pdf.add_text(258, y, "_____ mg/dL", font='F1', size=9)
        y -= 16
        pdf.add_text(70, y, "Carbs: _____ g", font='F1', size=9)
        pdf.add_text(180, y, "Meal: _________________________________", font='F1', size=9)
        y -= 25

        # Lunch
        pdf.add_text(60, y, "LUNCH", font='F2', size=10)
        y -= 18
        pdf.add_text(70, y, "Before:", font='F1', size=9)
        pdf.add_text(115, y, "_____ mg/dL", font='F1', size=9)
        pdf.add_text(220, y, "After:", font='F1', size=9)
        pdf.add_text(258, y, "_____ mg/dL", font='F1', size=9)
        y -= 16
        pdf.add_text(70, y, "Carbs: _____ g", font='F1', size=9)
        pdf.add_text(180, y, "Meal: _________________________________", font='F1', size=9)
        y -= 25

        # Dinner
        pdf.add_text(60, y, "DINNER", font='F2', size=10)
        y -= 18
        pdf.add_text(70, y, "Before:", font='F1', size=9)
        pdf.add_text(115, y, "_____ mg/dL", font='F1', size=9)
        pdf.add_text(220, y, "After:", font='F1', size=9)
        pdf.add_text(258, y, "_____ mg/dL", font='F1', size=9)
        y -= 16
        pdf.add_text(70, y, "Carbs: _____ g", font='F1', size=9)
        pdf.add_text(180, y, "Meal: _________________________________", font='F1', size=9)
        y -= 30

        # Snacks
        pdf.add_text(60, y, "Snacks:", font='F2', size=9)
        pdf.add_text(115, y, "________________________________________", font='F1', size=9)
        y -= 25

        # Insulin / Medication
        pdf.add_text(60, y, "Insulin Dose:", font='F2', size=9)
        pdf.add_text(145, y, "____________ units", font='F1', size=9)
        y -= 20
        pdf.add_text(60, y, "Medication:", font='F1', size=9)
        pdf.add_text(130, y, "________________________", font='F1', size=9)
        y -= 25

        # Exercise
        pdf.add_text(60, y, "Exercise:", font='F2', size=9)
        pdf.add_text(120, y, "_______ minutes", font='F1', size=9)
        pdf.add_text(230, y, "Type: ________________", font='F1', size=9)
        y -= 22

        # Water intake
        pdf.add_text(60, y, "Water Intake:", font='F2', size=9)
        pdf.add_text(145, y, "_______ glasses", font='F1', size=9)
        y -= 25

        # Bedtime glucose
        pdf.add_text(60, y, "Bedtime Glucose:", font='F2', size=10)
        pdf.add_text(180, y, "_______ mg/dL", font='F1', size=10)
        y -= 30

        # Notes
        pdf.add_text(60, y, "Notes:", font='F2', size=9)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 18
        pdf.add_line(60, y, 372, y, 0.3)

        pdf.add_centered_text(35, f"- {day + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book31_Blood_Sugar_Food_Diary.pdf')
    print("Book 31 created: Book31_Blood_Sugar_Food_Diary.pdf")

if __name__ == '__main__':
    create_book()
