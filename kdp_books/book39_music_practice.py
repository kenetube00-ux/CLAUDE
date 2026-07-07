"""
Book 39: Music Practice Log - Track Your Progress
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(540, "MUSIC PRACTICE", font='F2', size=26)
    pdf.add_centered_text(500, "LOG", font='F2', size=26)
    pdf.add_line(100, 480, 332, 480, 2)
    pdf.add_centered_text(450, "Track Your Progress", font='F4', size=16)
    pdf.add_centered_text(415, "50 Practice Sessions | Repertoire List", font='F1', size=10)
    pdf.add_centered_text(395, "Performance Log | Goal Tracking", font='F1', size=10)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(235, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "Music Practice Log - Track Your Progress", font='F2', size=12)
    pdf.add_centered_text(475, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(395, "Published via Amazon KDP", font='F1', size=9)


    # --- STUDENT INFO PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "STUDENT INFORMATION", font='F2', size=16)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 565
    info_fields = [
        "Name: _________________________________",
        "Instrument: ___________________________",
        "Teacher: ______________________________",
        "Level: ________________________________",
        "Years Playing: ________________________",
        "",
        "Practice Goals:",
        "  Short-term: _________________________",
        "  _____________________________________",
        "  Long-term: __________________________",
        "  _____________________________________",
        "",
        "Weekly Practice Target: ______ hours",
        "Preferred Practice Time: ______________",
        "Current Pieces Working On:",
        "  1. ________________________________",
        "  2. ________________________________",
        "  3. ________________________________",
    ]
    for field in info_fields:
        if field == "":
            y -= 12
        else:
            pdf.add_text(60, y, field, font='F1', size=10)
            y -= 26

    # --- 50 PRACTICE SESSION LOG PAGES ---
    for session in range(1, 51):
        pdf.new_page()
        pdf.add_text(60, 615, f"Practice Session #{session}", font='F2', size=12)
        pdf.add_text(280, 615, "Date: ___/___/______", font='F1', size=9)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 580
        pdf.add_text(60, y, "Duration:", font='F2', size=9)
        pdf.add_text(120, y, "_______ minutes", font='F1', size=9)
        pdf.add_text(250, y, "Start: ______  End: ______", font='F1', size=9)
        y -= 22

        pdf.add_text(60, y, "Warm-up:", font='F2', size=9)
        pdf.add_text(120, y, "_________________________________________", font='F1', size=9)
        y -= 22

        pdf.add_text(60, y, "Scales/Technique:", font='F2', size=9)
        pdf.add_text(165, y, "________________________________", font='F1', size=9)
        y -= 22

        pdf.add_text(60, y, "Pieces Practiced:", font='F2', size=9)
        y -= 16
        pdf.add_text(70, y, "1. ____________________________________________", font='F1', size=9)
        y -= 16
        pdf.add_text(70, y, "2. ____________________________________________", font='F1', size=9)
        y -= 16
        pdf.add_text(70, y, "3. ____________________________________________", font='F1', size=9)
        y -= 22


        pdf.add_text(60, y, "What I struggled with:", font='F2', size=9)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 16
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 22

        pdf.add_text(60, y, "What improved:", font='F2', size=9)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 16
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 22

        pdf.add_text(60, y, "Teacher's Notes:", font='F2', size=9)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 16
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 22

        pdf.add_text(60, y, "Next Session Focus:", font='F2', size=9)
        y -= 15
        pdf.add_line(60, y, 372, y, 0.3)
        y -= 16
        pdf.add_line(60, y, 372, y, 0.3)

        pdf.add_centered_text(35, f"- {session + 3} -", font='F1', size=8)

    # --- REPERTOIRE LIST PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "REPERTOIRE LIST", font='F2', size=14)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 578
    pdf.add_text(55, y, "#", font='F2', size=8)
    pdf.add_text(70, y, "Piece Title", font='F2', size=8)
    pdf.add_text(200, y, "Composer", font='F2', size=8)
    pdf.add_text(310, y, "Status", font='F2', size=8)
    y -= 4
    pdf.add_line(55, y, 380, y, 0.4)
    for slot in range(1, 21):
        y -= 22
        pdf.add_text(55, y, f"{slot}.", font='F1', size=8)
        pdf.add_text(70, y, "___________________", font='F1', size=8)
        pdf.add_text(200, y, "__________________", font='F1', size=8)
        pdf.add_text(310, y, "____________", font='F1', size=8)


    # --- PERFORMANCE LOG ---
    pdf.new_page()
    pdf.add_centered_text(615, "PERFORMANCE LOG", font='F2', size=14)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 575
    for perf in range(1, 11):
        pdf.add_text(60, y, f"Performance #{perf}", font='F2', size=9)
        y -= 16
        pdf.add_text(70, y, "Date: ___/___/______", font='F1', size=8)
        pdf.add_text(210, y, "Venue: ____________________", font='F1', size=8)
        y -= 15
        pdf.add_text(70, y, "Pieces Performed: _________________________________", font='F1', size=8)
        y -= 15
        pdf.add_text(70, y, "How It Went: ______________________________________", font='F1', size=8)
        y -= 12
        pdf.add_line(60, y, 372, y, 0.2, gray=0.5)
        y -= 12

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book39_Music_Practice_Log.pdf')
    print("Book 39 created: Book39_Music_Practice_Log.pdf")

if __name__ == '__main__':
    create_book()
