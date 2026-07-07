"""
Book 33: Car Maintenance Log & Service Record
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(540, "CAR MAINTENANCE", font='F2', size=26)
    pdf.add_centered_text(500, "LOG &", font='F2', size=20)
    pdf.add_centered_text(465, "SERVICE RECORD", font='F2', size=26)
    pdf.add_line(100, 445, 332, 445, 2)
    pdf.add_centered_text(415, "Complete Vehicle Service History Tracker", font='F1', size=11)
    pdf.add_centered_text(390, "Oil Changes | Tire Rotation | Repairs | Fuel Log", font='F1', size=10)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(235, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(150, "Vehicle Owner: ______________________", font='F1', size=12)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "Car Maintenance Log & Service Record", font='F2', size=13)
    pdf.add_centered_text(475, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(395, "Published via Amazon KDP", font='F1', size=9)

    # --- VEHICLE INFORMATION PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "VEHICLE INFORMATION", font='F2', size=16)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 570
    fields = [
        "Make: _________________________________",
        "Model: ________________________________",
        "Year: _________________________________",
        "VIN: __________________________________",
        "Color: ________________________________",
        "License Plate: ________________________",
        "Insurance Company: ____________________",
        "Insurance Policy #: ___________________",
        "Dealer Name: __________________________",
        "Dealer Phone: _________________________",
        "Purchase Date: ________________________",
        "Purchase Mileage: _____________________",
    ]
    for field in fields:
        pdf.add_text(70, y, field, font='F1', size=11)
        y -= 35

    # --- 50 SERVICE RECORD ENTRIES ---
    for entry in range(1, 51):
        if entry % 3 == 1:
            pdf.new_page()
            pdf.add_centered_text(620, "SERVICE RECORD", font='F2', size=14)
            pdf.add_line(100, 608, 332, 608, 0.8)
            y_start = 585

        slot = (entry - 1) % 3
        y = y_start - slot * 190

        pdf.add_text(60, y, f"Service #{entry}", font='F2', size=10)
        pdf.add_line(60, y - 5, 372, y - 5, 0.5)
        y -= 22
        pdf.add_text(60, y, "Date: ___/___/______", font='F1', size=9)
        pdf.add_text(220, y, "Mileage: ______________", font='F1', size=9)
        y -= 18
        pdf.add_text(60, y, "Service Type: ___________________________________", font='F1', size=9)
        y -= 18
        pdf.add_text(60, y, "Performed By: ___________________________________", font='F1', size=9)
        y -= 18
        pdf.add_text(60, y, "Cost: $__________", font='F1', size=9)
        pdf.add_text(200, y, "Next Service Due: ___/___/______", font='F1', size=9)
        y -= 18
        pdf.add_text(60, y, "Notes: __________________________________________", font='F1', size=9)
        y -= 15
        pdf.add_text(60, y, "________________________________________________", font='F1', size=9)

    # --- TIRE ROTATION LOG PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "TIRE ROTATION LOG", font='F2', size=16)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 575
    pdf.add_text(60, y, "Date", font='F2', size=9)
    pdf.add_text(130, y, "Mileage", font='F2', size=9)
    pdf.add_text(210, y, "Tire Brand/Type", font='F2', size=9)
    pdf.add_text(330, y, "Next Due", font='F2', size=9)
    y -= 5
    pdf.add_line(60, y, 372, y, 0.5)
    for i in range(20):
        y -= 22
        pdf.add_text(60, y, "___/___/___", font='F1', size=8)
        pdf.add_text(130, y, "___________", font='F1', size=8)
        pdf.add_text(210, y, "__________________", font='F1', size=8)
        pdf.add_text(330, y, "___/___/___", font='F1', size=8)
        y -= 3
        pdf.add_line(60, y, 372, y, 0.2, gray=0.6)

    # --- FUEL LOG PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "FUEL LOG", font='F2', size=16)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 575
    pdf.add_text(55, y, "Date", font='F2', size=8)
    pdf.add_text(110, y, "Mileage", font='F2', size=8)
    pdf.add_text(175, y, "Gallons", font='F2', size=8)
    pdf.add_text(235, y, "Cost", font='F2', size=8)
    pdf.add_text(290, y, "$/Gal", font='F2', size=8)
    pdf.add_text(345, y, "MPG", font='F2', size=8)
    y -= 5
    pdf.add_line(55, y, 380, y, 0.5)
    for i in range(20):
        y -= 24
        pdf.add_text(55, y, "___/___", font='F1', size=8)
        pdf.add_text(110, y, "_________", font='F1', size=8)
        pdf.add_text(175, y, "_______", font='F1', size=8)
        pdf.add_text(235, y, "$______", font='F1', size=8)
        pdf.add_text(290, y, "$_____", font='F1', size=8)
        pdf.add_text(345, y, "______", font='F1', size=8)
        y -= 3
        pdf.add_line(55, y, 380, y, 0.2, gray=0.6)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book33_Car_Maintenance_Log.pdf')
    print("Book 33 created: Book33_Car_Maintenance_Log.pdf")

if __name__ == '__main__':
    create_book()
