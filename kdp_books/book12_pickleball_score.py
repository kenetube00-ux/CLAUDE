"""
Book 12: Pickleball Score Book & Match Tracker
KDP Interior - 6x9 inches (432x648)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    pdf.new_page()
    pdf.add_centered_text(530, "PICKLEBALL", font='F2', size=34)
    pdf.add_centered_text(485, "SCORE BOOK", font='F2', size=28)
    pdf.add_centered_text(445, "& MATCH TRACKER", font='F2', size=18)
    pdf.add_line(100, 425, 332, 425, 2)
    pdf.add_centered_text(395, "100 Match Score Sheets | Stats Tracker", font='F1', size=11)
    pdf.add_centered_text(370, "Improvement Log | Tournament Records", font='F1', size=11)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(238, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(150, "Player: ________________________", font='F1', size=13)
    pdf.add_centered_text(120, "Rating: ________  Season: _______", font='F1', size=12)

    pdf.new_page()
    pdf.add_centered_text(500, "Pickleball Score Book", font='F2', size=13)
    pdf.add_centered_text(475, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(445, "Copyright 2026. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "ISBN: _______________", font='F1', size=9)


    # Match score sheets (50 pages, 2 matches per page)
    for page in range(1, 51):
        pdf.new_page()
        pdf.add_text(60, 615, f"Match #{page*2-1} & #{page*2}", font='F2', size=11)
        pdf.add_line(60, 605, 372, 605, 0.8)

        for match in range(2):
            y_offset = 305 * match
            base_y = 590 - y_offset
            pdf.add_text(60, base_y, f"Match #{page*2-1+match}", font='F2', size=10)
            pdf.add_text(60, base_y-20, "Date:______  Location:________________", font='F1', size=9)
            pdf.add_text(60, base_y-40, "Type: Singles / Doubles    Tournament: Y / N", font='F1', size=9)
            pdf.add_text(60, base_y-62, "My Team:", font='F2', size=9)
            pdf.add_line(120, base_y-65, 250, base_y-65, 0.3, gray=0.5)
            pdf.add_text(260, base_y-62, "Opponent:", font='F2', size=9)
            pdf.add_line(315, base_y-65, 372, base_y-65, 0.3, gray=0.5)
            # Score grid
            pdf.add_text(60, base_y-85, "Game 1:", font='F1', size=9)
            pdf.add_text(110, base_y-85, "____  vs  ____", font='F1', size=9)
            pdf.add_text(200, base_y-85, "Game 2:", font='F1', size=9)
            pdf.add_text(250, base_y-85, "____  vs  ____", font='F1', size=9)
            pdf.add_text(60, base_y-105, "Game 3:", font='F1', size=9)
            pdf.add_text(110, base_y-105, "____  vs  ____", font='F1', size=9)
            pdf.add_text(200, base_y-105, "Result: W / L", font='F2', size=9)
            pdf.add_text(60, base_y-130, "Notes:_______________________________________", font='F1', size=8)
            pdf.add_line(60, base_y-148, 372, base_y-148, 0.5)

        pdf.add_centered_text(35, f"- {page + 2} -", font='F1', size=8)

    pdf.new_page()
    pdf.add_centered_text(400, "Keep Dinking!", font='F2', size=20)
    pdf.add_centered_text(365, "Track your games, improve your play.", font='F1', size=11)
    pdf.add_centered_text(330, "Leave a review if this helped!", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book12_Pickleball_Score.pdf')
    print("Book 12 created: Book12_Pickleball_Score.pdf")

if __name__ == '__main__':
    create_book()
