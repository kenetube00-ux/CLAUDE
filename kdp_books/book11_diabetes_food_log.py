"""
Book 11: Large Print Diabetes Food & Blood Sugar Log
KDP Interior - 6x9 inches (432x648)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    pdf.new_page()
    pdf.add_centered_text(540, "LARGE PRINT", font='F2', size=16)
    pdf.add_centered_text(500, "DIABETES", font='F2', size=32)
    pdf.add_centered_text(460, "FOOD & BLOOD SUGAR", font='F2', size=20)
    pdf.add_centered_text(430, "LOG BOOK", font='F2', size=20)
    pdf.add_line(100, 410, 332, 410, 2)
    pdf.add_centered_text(380, "Daily Glucose Tracking | Meal Log | A1C Record", font='F1', size=10)
    pdf.add_centered_text(355, "Medication Tracker | 52 Weeks", font='F1', size=10)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(238, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(150, "Name: ______________________", font='F1', size=12)
    pdf.add_centered_text(125, "Doctor: _____________________", font='F1', size=12)

    # Copyright
    pdf.new_page()
    pdf.add_centered_text(500, "Diabetes Food & Blood Sugar Log Book", font='F2', size=12)
    pdf.add_centered_text(475, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(445, "Copyright 2026. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(380, "DISCLAIMER: Not a substitute for medical advice.", font='F1', size=8)


    # Weekly log pages (26 weeks)
    for week in range(1, 27):
        pdf.new_page()
        pdf.add_text(60, 615, f"Week {week}", font='F2', size=14)
        pdf.add_text(250, 615, "Date Range: ___/___  to  ___/___", font='F1', size=9)
        pdf.add_line(60, 602, 372, 602, 0.8)
        days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        y = 580
        for day in days:
            pdf.add_text(60, y, day, font='F2', size=9)
            pdf.add_text(90, y, "Fasting:____", font='F1', size=8)
            pdf.add_text(165, y, "After Meal:____", font='F1', size=8)
            pdf.add_text(265, y, "Bedtime:____", font='F1', size=8)
            y -= 18
            pdf.add_text(90, y, "Breakfast:________________", font='F1', size=8)
            pdf.add_text(250, y, "Carbs:___g", font='F1', size=8)
            y -= 16
            pdf.add_text(90, y, "Lunch:____________________", font='F1', size=8)
            pdf.add_text(250, y, "Carbs:___g", font='F1', size=8)
            y -= 16
            pdf.add_text(90, y, "Dinner:___________________", font='F1', size=8)
            pdf.add_text(250, y, "Carbs:___g", font='F1', size=8)
            y -= 16
            pdf.add_text(90, y, "Meds Taken: Y / N   Exercise: ___min", font='F1', size=8)
            y -= 10
            pdf.add_line(60, y, 372, y, 0.3, gray=0.5)
            y -= 12
        pdf.add_centered_text(35, f"- {week + 2} -", font='F1', size=8)

    # Back matter
    pdf.new_page()
    pdf.add_centered_text(400, "Stay Healthy!", font='F2', size=20)
    pdf.add_centered_text(365, "Track consistently for better health outcomes.", font='F1', size=11)
    pdf.add_centered_text(330, "Please leave a review if this helped you!", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book11_Diabetes_Food_Log.pdf')
    print("Book 11 created: Book11_Diabetes_Food_Log.pdf")

if __name__ == '__main__':
    create_book()
