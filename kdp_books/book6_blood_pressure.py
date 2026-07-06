"""
Book 6: Large Print Blood Pressure Log Book for Seniors
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_bp_log():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(540, "LARGE PRINT", font='F2', size=16)
    pdf.add_centered_text(495, "BLOOD PRESSURE", font='F2', size=30)
    pdf.add_centered_text(455, "LOG BOOK", font='F2', size=30)
    pdf.add_line(100, 435, 332, 435, 2)
    pdf.add_centered_text(405, "Daily Tracking & Health Monitoring", font='F1', size=13)
    pdf.add_centered_text(380, "For Seniors | Large Print | Easy to Read", font='F1', size=11)
    pdf.add_centered_text(340, "Record Systolic, Diastolic, Pulse & Notes", font='F1', size=10)
    pdf.add_centered_text(310, "52 Weeks of Daily Tracking", font='F1', size=10)
    pdf.add_centered_text(230, "By", font='F1', size=11)
    pdf.add_centered_text(208, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(140, "Name: _______________________", font='F1', size=12)
    pdf.add_centered_text(115, "Doctor: ______________________", font='F1', size=12)
    pdf.add_centered_text(90, "Phone: ______________________", font='F1', size=12)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(520, "Large Print Blood Pressure Log Book", font='F2', size=13)
    pdf.add_centered_text(495, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(460, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(430, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(405, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(360, "DISCLAIMER: This book is for personal health tracking only.", font='F1', size=8)
    pdf.add_centered_text(340, "It is not a substitute for professional medical advice.", font='F1', size=8)

    # --- UNDERSTANDING BP PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "Understanding Blood Pressure", font='F2', size=16)
    pdf.add_line(60, 585, 372, 585, 1)
    info = [
        "Blood pressure is measured in mmHg with two numbers:",
        "",
        "SYSTOLIC (top number): Pressure during heartbeat",
        "DIASTOLIC (bottom number): Pressure between beats",
        "",
        "BLOOD PRESSURE CATEGORIES:",
        "  Normal:      Less than 120/80",
        "  Elevated:    120-129 / less than 80",
        "  High (Stage 1):  130-139 / 80-89",
        "  High (Stage 2):  140+ / 90+",
        "  Crisis:      180+ / 120+",
        "",
        "TIPS FOR ACCURATE READINGS:",
        "- Sit quietly for 5 minutes before measuring",
        "- Keep feet flat on the floor",
        "- Rest arm at heart level",
        "- Don't talk during measurement",
        "- Take readings at the same time daily",
    ]
    y = 555
    for line in info:
        bold = line.endswith(':') or line.startswith('SYS') or line.startswith('DIA')
        f = 'F2' if bold else 'F1'
        pdf.add_text(60, y, line, font=f, size=11)
        y -= 24

    # --- WEEKLY LOG PAGES (26 weeks = 52 pages, 2 per spread) ---
    for week in range(1, 27):
        pdf.new_page()
        pdf.add_centered_text(615, f"Week {week}", font='F2', size=14)
        pdf.add_line(60, 602, 372, 602, 0.8)

        # Table header
        pdf.add_text(60, 578, "Day", font='F2', size=10)
        pdf.add_text(100, 578, "Date", font='F2', size=10)
        pdf.add_text(160, 578, "Time", font='F2', size=10)
        pdf.add_text(210, 578, "SYS", font='F2', size=10)
        pdf.add_text(252, 578, "DIA", font='F2', size=10)
        pdf.add_text(294, 578, "Pulse", font='F2', size=10)
        pdf.add_text(340, 578, "Notes", font='F2', size=10)
        pdf.add_line(60, 572, 372, 572, 0.8)

        # 7 days x 2 readings each = 14 rows
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        y = 555
        for day in days:
            # Morning reading
            pdf.add_text(60, y, day, font='F1', size=9)
            pdf.add_text(100, y, "___/___", font='F1', size=9)
            pdf.add_text(160, y, "AM", font='F1', size=9)
            pdf.add_text(210, y, "____", font='F1', size=9)
            pdf.add_text(252, y, "____", font='F1', size=9)
            pdf.add_text(294, y, "____", font='F1', size=9)
            pdf.add_text(340, y, "________", font='F1', size=9)
            y -= 22
            # Evening reading
            pdf.add_text(100, y, "___/___", font='F1', size=9)
            pdf.add_text(160, y, "PM", font='F1', size=9)
            pdf.add_text(210, y, "____", font='F1', size=9)
            pdf.add_text(252, y, "____", font='F1', size=9)
            pdf.add_text(294, y, "____", font='F1', size=9)
            pdf.add_text(340, y, "________", font='F1', size=9)
            y -= 20
            # Separator line
            pdf.add_line(60, y + 8, 372, y + 8, 0.3, gray=0.6)
            y -= 8

        # Weekly summary
        pdf.add_text(60, y - 10, "Weekly Average:  SYS: _____ / DIA: _____ / Pulse: _____", font='F2', size=9)
        pdf.add_text(60, y - 30, "Notes: _______________________________________________", font='F1', size=9)
        pdf.add_centered_text(35, f"- {week + 2} -", font='F1', size=8)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(480, "Stay Healthy!", font='F2', size=22)
    pdf.add_centered_text(440, "Consistent tracking helps you and your doctor", font='F1', size=12)
    pdf.add_centered_text(418, "manage your blood pressure effectively.", font='F1', size=12)
    pdf.add_centered_text(370, "If you found this log book helpful,", font='F1', size=11)
    pdf.add_centered_text(348, "please leave a review on Amazon.", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book6_Blood_Pressure_Log.pdf')
    print("Book 6 created: Book6_Blood_Pressure_Log.pdf")

if __name__ == '__main__':
    create_bp_log()
