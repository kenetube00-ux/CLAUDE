"""
Book 37: Baseball & Softball Scorebook
KDP Interior - 8.5x11 inches (612x792 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "BASEBALL", font='F2', size=36)
    pdf.add_centered_text(605, "&", font='F2', size=20)
    pdf.add_centered_text(565, "SOFTBALL", font='F2', size=36)
    pdf.add_centered_text(520, "SCOREBOOK", font='F2', size=30)
    pdf.add_line(170, 500, 442, 500, 2)
    pdf.add_centered_text(470, "30 Game Scoring Sheets", font='F1', size=14)
    pdf.add_centered_text(445, "Batting Order | Pitching Stats | Inning Scores", font='F1', size=11)
    pdf.add_centered_text(320, "By", font='F1', size=12)
    pdf.add_centered_text(290, "Daniel Tesfamariam", font='F2', size=18)

    pdf.add_centered_text(200, "Team: ________________________", font='F1', size=14)
    pdf.add_centered_text(170, "Season: ______________________", font='F1', size=14)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(550, "Baseball & Softball Scorebook", font='F2', size=14)
    pdf.add_centered_text(525, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(495, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(470, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(445, "Published via Amazon KDP", font='F1', size=9)

    # --- 30 GAME SCORING SHEETS ---
    for game in range(1, 31):
        pdf.new_page()
        pdf.add_text(50, 760, f"Game #{game}", font='F2', size=12)
        pdf.add_text(150, 760, "Date: ___/___/___", font='F1', size=9)
        pdf.add_text(300, 760, "Location: _____________________", font='F1', size=9)

        # Teams
        pdf.add_text(50, 738, "Home: ____________________", font='F1', size=9)
        pdf.add_text(310, 738, "Away: ____________________", font='F1', size=9)

        # Inning-by-inning score grid
        y = 710
        pdf.add_text(50, y, "INNING SCORE", font='F2', size=9)
        y -= 14
        # Header row
        pdf.add_text(50, y, "Team", font='F2', size=7)
        innings_x = [120, 150, 180, 210, 240, 270, 300, 330, 360]
        for i, ix in enumerate(innings_x):
            pdf.add_text(ix, y, str(i+1), font='F2', size=7)
        pdf.add_text(400, y, "R", font='F2', size=7)
        pdf.add_text(425, y, "H", font='F2', size=7)
        pdf.add_text(450, y, "E", font='F2', size=7)
        y -= 4
        pdf.add_line(50, y, 470, y, 0.5)

        # Away row
        y -= 14
        pdf.add_text(50, y, "Away", font='F1', size=7)
        for ix in innings_x:
            pdf.add_rect(ix-3, y-4, 22, 14, 0.3)
        pdf.add_rect(397, y-4, 22, 14, 0.3)
        pdf.add_rect(422, y-4, 22, 14, 0.3)
        pdf.add_rect(447, y-4, 22, 14, 0.3)
        # Home row
        y -= 18
        pdf.add_text(50, y, "Home", font='F1', size=7)
        for ix in innings_x:
            pdf.add_rect(ix-3, y-4, 22, 14, 0.3)
        pdf.add_rect(397, y-4, 22, 14, 0.3)
        pdf.add_rect(422, y-4, 22, 14, 0.3)
        pdf.add_rect(447, y-4, 22, 14, 0.3)

        # Batting order
        y -= 30
        pdf.add_text(50, y, "BATTING ORDER", font='F2', size=9)
        y -= 14
        pdf.add_text(50, y, "#", font='F2', size=7)
        pdf.add_text(65, y, "Player Name", font='F2', size=7)
        pdf.add_text(210, y, "Pos", font='F2', size=7)
        pdf.add_text(245, y, "AB", font='F2', size=7)
        pdf.add_text(275, y, "R", font='F2', size=7)
        pdf.add_text(300, y, "H", font='F2', size=7)
        pdf.add_text(325, y, "RBI", font='F2', size=7)
        pdf.add_text(355, y, "BB", font='F2', size=7)
        y -= 4
        pdf.add_line(50, y, 385, y, 0.4)
        for batter in range(1, 10):
            y -= 16
            pdf.add_text(50, y, str(batter), font='F1', size=7)
            pdf.add_text(65, y, "_____________________", font='F1', size=7)
            pdf.add_text(210, y, "____", font='F1', size=7)
            pdf.add_text(245, y, "____", font='F1', size=7)
            pdf.add_text(275, y, "____", font='F1', size=7)
            pdf.add_text(300, y, "____", font='F1', size=7)
            pdf.add_text(325, y, "____", font='F1', size=7)
            pdf.add_text(355, y, "____", font='F1', size=7)


        # Pitching stats
        y -= 25
        pdf.add_text(50, y, "PITCHING STATS", font='F2', size=9)
        y -= 14
        pdf.add_text(50, y, "Pitcher", font='F2', size=7)
        pdf.add_text(180, y, "IP", font='F2', size=7)
        pdf.add_text(210, y, "H", font='F2', size=7)
        pdf.add_text(235, y, "R", font='F2', size=7)
        pdf.add_text(260, y, "ER", font='F2', size=7)
        pdf.add_text(290, y, "BB", font='F2', size=7)
        pdf.add_text(320, y, "K", font='F2', size=7)
        y -= 4
        pdf.add_line(50, y, 345, y, 0.4)
        for p in range(3):
            y -= 16
            pdf.add_text(50, y, "_____________________", font='F1', size=7)
            pdf.add_text(180, y, "____", font='F1', size=7)
            pdf.add_text(210, y, "____", font='F1', size=7)
            pdf.add_text(235, y, "____", font='F1', size=7)
            pdf.add_text(260, y, "____", font='F1', size=7)
            pdf.add_text(290, y, "____", font='F1', size=7)
            pdf.add_text(320, y, "____", font='F1', size=7)

        # Game notes and final info
        y -= 25
        pdf.add_text(50, y, "Game Notes:", font='F2', size=9)
        y -= 14
        pdf.add_line(50, y, 560, y, 0.3)
        y -= 16
        pdf.add_line(50, y, 560, y, 0.3)
        y -= 16
        pdf.add_line(50, y, 560, y, 0.3)

        y -= 22
        pdf.add_text(50, y, "Final Score: _____ - _____", font='F2', size=9)
        pdf.add_text(250, y, "Winning Pitcher: ________________", font='F1', size=9)
        y -= 16
        pdf.add_text(50, y, "MVP: ____________________", font='F1', size=9)

        pdf.add_centered_text(30, f"- {game + 2} -", font='F1', size=8)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book37_Baseball_Scorebook.pdf')
    print("Book 37 created: Book37_Baseball_Scorebook.pdf")

if __name__ == '__main__':
    create_book()
