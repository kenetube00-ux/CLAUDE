"""
Book 35: My First Activity Book - For Toddlers Ages 2-4
KDP Interior - 8.5x11 inches (612x792 points)
"""
import random
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    random.seed(35)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "MY FIRST", font='F2', size=32)
    pdf.add_centered_text(600, "ACTIVITY BOOK", font='F2', size=36)
    pdf.add_line(150, 580, 462, 580, 2)
    pdf.add_centered_text(545, "For Toddlers Ages 2-4", font='F1', size=18)

    pdf.add_centered_text(505, "Trace Shapes | Trace Letters | Trace Numbers", font='F1', size=12)
    pdf.add_centered_text(480, "Connect the Dots | Matching | Counting", font='F1', size=12)
    pdf.add_centered_text(320, "By", font='F1', size=12)
    pdf.add_centered_text(290, "Daniel Tesfamariam", font='F2', size=18)
    pdf.add_centered_text(200, "This book belongs to:", font='F4', size=14)
    pdf.add_centered_text(170, "________________________", font='F1', size=14)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(550, "My First Activity Book", font='F2', size=14)
    pdf.add_centered_text(525, "For Toddlers Ages 2-4", font='F1', size=11)
    pdf.add_centered_text(500, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(470, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(445, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(420, "Published via Amazon KDP", font='F1', size=9)


    # --- ACTIVITY PAGES (30 pages) ---
    # Activity 1-4: Trace the Shapes
    shapes_data = [
        ("Circle", 306, 400, 80),
        ("Square", 306, 400, 80),
        ("Triangle", 306, 400, 80),
        ("Rectangle", 306, 400, 80),
    ]
    for i, (shape_name, cx, cy, size) in enumerate(shapes_data):
        pdf.new_page()
        pdf.add_centered_text(740, f"Trace the {shape_name}", font='F2', size=24)
        pdf.add_centered_text(710, "Follow the dotted lines with your pencil!", font='F1', size=12)
        # Draw dotted outline of shape
        if shape_name == "Circle":
            import math
            for angle in range(0, 360, 8):
                rad = math.radians(angle)
                x1 = cx + size * math.cos(rad)
                y1 = cy + size * math.sin(rad)
                rad2 = math.radians(angle + 4)
                x2 = cx + size * math.cos(rad2)
                y2 = cy + size * math.sin(rad2)
                pdf.add_line(x1, y1, x2, y2, 1.5, gray=0.5)
        elif shape_name == "Square":
            x0, y0 = cx - size, cy - size
            for seg in range(0, size*2, 10):
                pdf.add_line(x0+seg, y0, x0+seg+5, y0, 1.5, gray=0.5)
                pdf.add_line(x0+seg, y0+size*2, x0+seg+5, y0+size*2, 1.5, gray=0.5)
                pdf.add_line(x0, y0+seg, x0, y0+seg+5, 1.5, gray=0.5)
                pdf.add_line(x0+size*2, y0+seg, x0+size*2, y0+seg+5, 1.5, gray=0.5)
        elif shape_name == "Triangle":
            pts = [(cx, cy+size), (cx-size, cy-size), (cx+size, cy-size)]
            for j in range(3):
                x1, y1 = pts[j]
                x2, y2 = pts[(j+1)%3]
                for seg in range(0, 20, 2):
                    t1 = seg / 20.0
                    t2 = (seg+1) / 20.0
                    sx = x1 + (x2-x1)*t1
                    sy = y1 + (y2-y1)*t1
                    ex = x1 + (x2-x1)*t2
                    ey = y1 + (y2-y1)*t2
                    pdf.add_line(sx, sy, ex, ey, 1.5, gray=0.5)
        elif shape_name == "Rectangle":
            x0, y0 = cx - size - 20, cy - size + 20
            w, h = (size+20)*2, (size-20)*2
            for seg in range(0, int(w), 10):
                pdf.add_line(x0+seg, y0, x0+seg+5, y0, 1.5, gray=0.5)
                pdf.add_line(x0+seg, y0+h, x0+seg+5, y0+h, 1.5, gray=0.5)
            for seg in range(0, int(h), 10):
                pdf.add_line(x0, y0+seg, x0, y0+seg+5, 1.5, gray=0.5)
                pdf.add_line(x0+w, y0+seg, x0+w, y0+seg+5, 1.5, gray=0.5)
        pdf.add_centered_text(50, f"- {i+3} -", font='F1', size=9)


    # Activity 5-10: Trace Letters A-F (large dotted outlines)
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    for i, letter in enumerate(letters):
        pdf.new_page()
        pdf.add_centered_text(740, f"Trace the Letter {letter}", font='F2', size=24)
        pdf.add_centered_text(710, "Trace over the dotted letter below!", font='F1', size=12)
        # Large dotted letter in center
        pdf.add_centered_text(400, letter, font='F2', size=200, gray=0.75)
        # Practice lines at bottom
        pdf.add_text(80, 200, "Now try writing it yourself:", font='F1', size=12)
        pdf.add_line(80, 170, 530, 170, 0.5, gray=0.4)
        pdf.add_line(80, 130, 530, 130, 0.5, gray=0.4)
        pdf.add_line(80, 90, 530, 90, 0.5, gray=0.4)
        pdf.add_centered_text(50, f"- {i+7} -", font='F1', size=9)

    # Activity 11-15: Trace Numbers 1-5 (large)
    for num in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(740, f"Trace the Number {num}", font='F2', size=24)
        pdf.add_centered_text(710, "Trace over the dotted number below!", font='F1', size=12)
        pdf.add_centered_text(400, str(num), font='F2', size=200, gray=0.75)
        # Draw that many shapes for counting
        pdf.add_text(80, 220, f"Count: {num} star(s)!", font='F1', size=14)
        for s in range(num):
            x = 120 + s * 80
            pdf.add_text(x, 185, "*", font='F2', size=40)
        pdf.add_line(80, 130, 530, 130, 0.5, gray=0.4)
        pdf.add_line(80, 90, 530, 90, 0.5, gray=0.4)
        pdf.add_centered_text(50, f"- {num+12} -", font='F1', size=9)


    # Activity 16-19: Color by shape (shapes in grid)
    shape_names = ["Circles", "Squares", "Triangles", "Stars"]
    for i, sname in enumerate(shape_names):
        pdf.new_page()
        pdf.add_centered_text(740, f"Color All the {sname}!", font='F2', size=22)
        pdf.add_centered_text(710, "Find and color only the shapes listed above.", font='F1', size=12)
        # Draw a grid of mixed shapes
        for row in range(4):
            for col in range(5):
                x = 106 + col * 100
                y = 350 + row * 80
                shape_type = random.choice(["circle", "square", "triangle", "star"])
                if shape_type == "circle":
                    import math
                    for angle in range(0, 360, 15):
                        rad = math.radians(angle)
                        rad2 = math.radians(angle+12)
                        pdf.add_line(x+25*math.cos(rad), y+25*math.sin(rad),
                                   x+25*math.cos(rad2), y+25*math.sin(rad2), 1)
                elif shape_type == "square":
                    pdf.add_rect(x-20, y-20, 40, 40)
                elif shape_type == "triangle":
                    pdf.add_line(x, y+25, x-22, y-18, 1)
                    pdf.add_line(x-22, y-18, x+22, y-18, 1)
                    pdf.add_line(x+22, y-18, x, y+25, 1)
                else:
                    pdf.add_text(x-12, y-12, "*", font='F2', size=30)
        pdf.add_centered_text(50, f"- {i+18} -", font='F1', size=9)

    # Activity 20-23: Connect the dots (simple 1-10)
    for pg in range(4):
        pdf.new_page()
        pdf.add_centered_text(740, f"Connect the Dots #{pg+1}", font='F2', size=22)
        pdf.add_centered_text(710, "Connect the numbers 1 to 10 in order!", font='F1', size=12)
        random.seed(pg * 100 + 20)
        points = []
        for n in range(1, 11):
            px = random.randint(120, 490)
            py = random.randint(200, 600)
            points.append((px, py))
            pdf.add_text(px, py, f" {n}", font='F2', size=14)
            # dot
            pdf.add_filled_rect(px-2, py-2, 5, 5, gray=0)
        pdf.add_centered_text(50, f"- {pg+22} -", font='F1', size=9)


    # Activity 24-26: Find the match (pairs of shapes)
    for pg in range(3):
        pdf.new_page()
        pdf.add_centered_text(740, f"Find the Match #{pg+1}", font='F2', size=22)
        pdf.add_centered_text(710, "Draw a line between matching shapes!", font='F1', size=12)
        shapes_left = ["O", "[]", "/\\", "*", "+"]
        random.seed(pg+240)
        shapes_right = shapes_left[:]
        random.shuffle(shapes_right)
        for idx in range(5):
            ly = 580 - idx * 90
            pdf.add_text(100, ly, shapes_left[idx], font='F2', size=28)
            pdf.add_text(450, ly, shapes_right[idx], font='F2', size=28)
        pdf.add_centered_text(50, f"- {pg+26} -", font='F1', size=9)

    # Activity 27-28: Big/Small comparison
    for pg in range(2):
        pdf.new_page()
        pdf.add_centered_text(740, "Circle the BIG one!", font='F2', size=22)
        pdf.add_centered_text(710, "In each row, circle the bigger shape.", font='F1', size=12)
        for row in range(4):
            y = 550 - row * 120
            # Small shape
            pdf.add_rect(150, y, 30, 30, 1.5)
            # Big shape
            pdf.add_rect(380, y-15, 60, 60, 1.5)
        pdf.add_centered_text(50, f"- {pg+29} -", font='F1', size=9)

    # Activity 29-30: Counting objects (1-5)
    for pg in range(2):
        pdf.new_page()
        pdf.add_centered_text(740, f"Count and Write #{pg+1}", font='F2', size=22)
        pdf.add_centered_text(710, "Count the shapes in each row and write the number.", font='F1', size=12)
        for row in range(5):
            count = row + 1
            y = 580 - row * 100
            pdf.add_text(80, y, f"Row {row+1}:", font='F2', size=12)
            for s in range(count):
                pdf.add_rect(160 + s*40, y-8, 20, 20, 1.2)
            pdf.add_text(400, y, "= ____", font='F1', size=14)
        pdf.add_centered_text(50, f"- {pg+31} -", font='F1', size=9)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book35_Toddler_Activity_Book.pdf')
    print("Book 35 created: Book35_Toddler_Activity_Book.pdf")

if __name__ == '__main__':
    create_book()
