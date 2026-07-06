"""
Book 26: HOMESCHOOL LESSON PLANNER
KDP Interior - 8.5x11 inches (612x792 points)
Title page + copyright + 36 weekly planning pages + 12 monthly overview pages
+ attendance log page + curriculum tracker page
"""
from pdf_utils import PDFDoc

def create_homeschool_planner():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "HOMESCHOOL", font='F2', size=32)
    pdf.add_centered_text(608, "LESSON PLANNER", font='F2', size=28)
    pdf.add_line(150, 588, 462, 588, 2)
    pdf.add_centered_text(555, "Organize Your Teaching Year", font='F4', size=14)
    pdf.add_centered_text(500, "36 Weekly Plans | 12 Monthly Overviews", font='F1', size=11)
    pdf.add_centered_text(478, "Attendance Log | Curriculum Tracker", font='F1', size=11)
    pdf.add_centered_text(370, "By", font='F1', size=11)
    pdf.add_centered_text(345, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "HOMESCHOOL LESSON PLANNER", font='F2', size=13)
    pdf.add_centered_text(625, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(590, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(570, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(550, "Published via Amazon KDP", font='F1', size=9)


    subjects = ["Math", "Science", "Reading", "Writing", "History", "Art"]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    # --- 36 WEEKLY PLANNING PAGES ---
    for week in range(1, 37):
        pdf.new_page()
        pdf.add_text(72, 750, f"WEEK #{week}", font='F2', size=14)
        pdf.add_text(72, 730, "Dates: ___________________", font='F1', size=10)
        pdf.add_line(72, 720, 540, 720, 0.8)

        # Column headers
        col_x = [72, 150, 228, 306, 384, 462]
        pdf.add_text(72, 700, "Subject", font='F2', size=9)
        for di, day in enumerate(days):
            pdf.add_text(col_x[di + 1], 700, day, font='F2', size=9)
        pdf.add_line(72, 693, 540, 693, 0.5)

        y = 675
        for subj in subjects:
            pdf.add_text(72, y, subj, font='F2', size=9)
            # Draw cells for each day
            for di in range(5):
                pdf.add_rect(col_x[di + 1] - 2, y - 45, 76, 55, 0.3, gray=0.5)
            y -= 60

        # Notes section at bottom
        y -= 10
        pdf.add_text(72, y, "Notes/Homework:", font='F2', size=9)
        y -= 15
        for i in range(3):
            pdf.add_line(72, y, 540, y, 0.3, gray=0.5)
            y -= 18

        pdf.add_centered_text(40, f"- {week + 2} -", font='F1', size=8)


    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # --- 12 MONTHLY OVERVIEW PAGES ---
    for mi, month in enumerate(months):
        pdf.new_page()
        pdf.add_text(72, 750, f"{month.upper()} - MONTHLY OVERVIEW", font='F2', size=14)
        pdf.add_line(72, 738, 540, 738, 0.8)

        y = 710
        # Goals
        pdf.add_text(72, y, "Goals for This Month:", font='F2', size=10)
        y -= 18
        for i in range(4):
            pdf.add_text(72, y, f"{i+1}.", font='F1', size=9)
            pdf.add_line(88, y - 2, 540, y - 2, 0.3, gray=0.5)
            y -= 20
        y -= 15

        # Field Trips
        pdf.add_text(72, y, "Field Trips Planned:", font='F2', size=10)
        y -= 18
        for i in range(3):
            pdf.add_text(72, y, f"{i+1}.", font='F1', size=9)
            pdf.add_line(88, y - 2, 400, y - 2, 0.3, gray=0.5)
            pdf.add_text(410, y, "Date:", font='F1', size=9)
            pdf.add_line(440, y - 2, 540, y - 2, 0.3, gray=0.5)
            y -= 20
        y -= 15

        # Milestones
        pdf.add_text(72, y, "Milestones / Achievements:", font='F2', size=10)
        y -= 18
        for i in range(5):
            pdf.add_rect(72, y - 3, 8, 8, 0.4)
            pdf.add_line(88, y - 2, 540, y - 2, 0.3, gray=0.5)
            y -= 20
        y -= 15

        # Reflection
        pdf.add_text(72, y, "Month Reflection:", font='F2', size=10)
        y -= 18
        for i in range(4):
            pdf.add_line(72, y, 540, y, 0.3, gray=0.5)
            y -= 20

        pdf.add_centered_text(40, f"- {mi + 39} -", font='F1', size=8)


    # --- ATTENDANCE LOG PAGE ---
    pdf.new_page()
    pdf.add_text(72, 750, "ATTENDANCE LOG", font='F2', size=14)
    pdf.add_line(72, 738, 540, 738, 0.8)

    pdf.add_text(72, 715, "Week", font='F2', size=8)
    pdf.add_text(115, 715, "Mon", font='F2', size=8)
    pdf.add_text(160, 715, "Tue", font='F2', size=8)
    pdf.add_text(205, 715, "Wed", font='F2', size=8)
    pdf.add_text(250, 715, "Thu", font='F2', size=8)
    pdf.add_text(295, 715, "Fri", font='F2', size=8)
    pdf.add_text(340, 715, "Total Hrs", font='F2', size=8)
    pdf.add_text(420, 715, "Notes", font='F2', size=8)
    pdf.add_line(72, 709, 540, 709, 0.5)

    y = 693
    for w in range(1, 37):
        pdf.add_text(72, y, f"{w}", font='F1', size=8)
        pdf.add_rect(115, y - 3, 8, 8, 0.3)
        pdf.add_rect(160, y - 3, 8, 8, 0.3)
        pdf.add_rect(205, y - 3, 8, 8, 0.3)
        pdf.add_rect(250, y - 3, 8, 8, 0.3)
        pdf.add_rect(295, y - 3, 8, 8, 0.3)
        pdf.add_line(340, y - 2, 400, y - 2, 0.3, gray=0.5)
        pdf.add_line(420, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 18

    # --- CURRICULUM TRACKER PAGE ---
    pdf.new_page()
    pdf.add_text(72, 750, "CURRICULUM TRACKER", font='F2', size=14)
    pdf.add_line(72, 738, 540, 738, 0.8)

    pdf.add_text(72, 715, "Subject", font='F2', size=9)
    pdf.add_text(180, 715, "Curriculum/Textbook", font='F2', size=9)
    pdf.add_text(370, 715, "Progress", font='F2', size=9)
    pdf.add_text(470, 715, "Complete", font='F2', size=9)
    pdf.add_line(72, 709, 540, 709, 0.5)

    y = 690
    for i in range(15):
        pdf.add_line(72, y - 2, 170, y - 2, 0.3, gray=0.5)
        pdf.add_line(180, y - 2, 360, y - 2, 0.3, gray=0.5)
        pdf.add_rect(370, y - 3, 80, 10, 0.3, gray=0.5)
        pdf.add_rect(480, y - 3, 8, 8, 0.3)
        y -= 28

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book26_Homeschool_Planner.pdf')
    print("Book 26 created: Book26_Homeschool_Planner.pdf")

if __name__ == '__main__':
    create_homeschool_planner()
