"""
Book 4: Dinosaur Activity Book (Ages 7-10)
KDP Interior - 8.5x11 inches (612x792 points)
Mixed activities: word search, mazes, connect dots, coloring, trivia
"""
import random
import math
from pdf_utils import PDFDoc

def create_dinosaur_activity_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "AWESOME", font='HelveticaBold', size=32)
    pdf.add_centered_text(600, "DINOSAUR", font='HelveticaBold', size=44)
    pdf.add_centered_text(550, "ACTIVITY BOOK", font='HelveticaBold', size=32)
    pdf.add_line(150, 530, 462, 530, 2)
    pdf.add_centered_text(490, "For Kids Ages 7-10", font='Helvetica', size=18)
    pdf.add_centered_text(450, "Word Search | Mazes | Puzzles | Coloring | Trivia", font='Helvetica', size=12)
    pdf.add_centered_text(410, "50+ Activities to Keep Young Dino Fans Busy!", font='Helvetica', size=12)
    # Simple dino silhouette
    draw_simple_dino(pdf, 260, 220, 1.5)
    pdf.add_centered_text(120, "Hours of Screen-Free Fun!", font='HelveticaBold', size=14)


    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(550, "Awesome Dinosaur Activity Book", font='HelveticaBold', size=14)
    pdf.add_centered_text(525, "For Kids Ages 7-10", font='Helvetica', size=11)
    pdf.add_centered_text(490, "Copyright 2026. All Rights Reserved.", font='Helvetica', size=9)
    pdf.add_centered_text(465, "No part of this book may be reproduced without permission.", font='Helvetica', size=8)
    pdf.add_centered_text(430, "ISBN: _______________", font='Helvetica', size=9)
    pdf.add_centered_text(405, "Published via Amazon KDP", font='Helvetica', size=9)

    # --- WORD SEARCH PAGES (4 pages) ---
    dino_word_lists = [
        ("Herbivore Dinosaurs", ["TRICERATOPS", "STEGOSAURUS", "BRACHIOSAURUS", "DIPLODOCUS",
         "ANKYLOSAURUS", "PARASAUROLOPHUS", "IGUANODON", "APATOSAURUS"]),
        ("Carnivore Dinosaurs", ["TYRANNOSAURUS", "VELOCIRAPTOR", "SPINOSAURUS", "ALLOSAURUS",
         "CARNOTAURUS", "DILOPHOSAURUS", "GIGANOTOSAURUS", "MEGALOSAURUS"]),
        ("Dinosaur World", ["JURASSIC", "CRETACEOUS", "TRIASSIC", "FOSSIL", "EXTINCT",
         "PALEONTOLOGY", "SKELETON", "VOLCANO"]),
        ("Dinosaur Body Parts", ["TEETH", "CLAWS", "TAIL", "HORNS", "SCALES",
         "WINGS", "BONES", "SKULL", "SPINE", "PLATES"]),
    ]

    for ws_idx, (title, words) in enumerate(dino_word_lists):
        pdf.new_page()
        pdf.add_centered_text(750, f"Word Search: {title}", font='HelveticaBold', size=18)
        pdf.add_centered_text(725, "Find all the hidden words!", font='Helvetica', size=11)

        # Generate word search grid
        grid_size = 14
        cell_size = 30
        start_x = (612 - grid_size * cell_size) / 2
        start_y = 680 - grid_size * cell_size

        # Fill grid with random letters
        random.seed(ws_idx * 100 + 42)
        grid = [[chr(random.randint(65, 90)) for _ in range(grid_size)] for _ in range(grid_size)]

        # Draw grid
        for row in range(grid_size):
            for col in range(grid_size):
                x = start_x + col * cell_size
                y = start_y + (grid_size - 1 - row) * cell_size
                pdf.add_rect(x, y, cell_size, cell_size, line_width=0.5)
                letter = grid[row][col]
                pdf.add_text(x + 10, y + 8, letter, font='Courier', size=14)

        # Word list below grid
        pdf.add_text(80, start_y - 30, "Find these words:", font='HelveticaBold', size=11)
        col1_x, col2_x = 80, 320
        for w_idx, word in enumerate(words):
            wx = col1_x if w_idx < 4 else col2_x
            wy = start_y - 55 - (w_idx % 4) * 20
            pdf.add_text(wx, wy, f"__ {word}", font='Courier', size=10)

        pdf.add_centered_text(40, f"- {ws_idx + 3} -", font='Helvetica', size=9)


    # --- MAZE PAGES (3 pages) ---
    maze_themes = [
        "Help the T-Rex find its dinner!",
        "Guide the baby dinosaur to its mother!",
        "Help the Pterodactyl reach its nest!",
    ]

    for maze_idx, maze_title in enumerate(maze_themes):
        pdf.new_page()
        pdf.add_centered_text(750, f"Dino Maze #{maze_idx + 1}", font='HelveticaBold', size=20)
        pdf.add_centered_text(725, maze_title, font='Helvetica', size=13)

        # Draw a maze using grid-based walls
        random.seed(maze_idx * 50 + 7)
        maze_w, maze_h = 12, 12
        cell = 40
        mx_start = (612 - maze_w * cell) / 2
        my_start = 250

        # Outer border
        pdf.add_rect(mx_start, my_start, maze_w * cell, maze_h * cell, line_width=2)

        # START and END labels
        pdf.add_text(mx_start - 5, my_start + maze_h * cell + 10, "START ->", font='HelveticaBold', size=12)
        pdf.add_text(mx_start + maze_w * cell - 50, my_start - 20, "-> END", font='HelveticaBold', size=12)

        # Generate random internal walls
        for r in range(maze_h):
            for c in range(maze_w):
                x = mx_start + c * cell
                y = my_start + r * cell
                # Random horizontal walls
                if random.random() < 0.4 and r > 0:
                    pdf.add_line(x, y, x + cell, y, 1.5)
                # Random vertical walls
                if random.random() < 0.4 and c > 0:
                    pdf.add_line(x, y, x, y + cell, 1.5)

        # Entry and exit gaps
        pdf.set_gray(1)
        pdf.add_line(mx_start, my_start + maze_h * cell - cell, mx_start, my_start + maze_h * cell, 3)
        pdf.add_line(mx_start + maze_w * cell, my_start, mx_start + maze_w * cell, my_start + cell, 3)
        pdf.reset_color()

        pdf.add_centered_text(40, f"- {maze_idx + 7} -", font='Helvetica', size=9)


    # --- CONNECT THE DOTS (2 pages) ---
    dot_themes = ["T-Rex", "Triceratops"]

    for dot_idx, dino_name in enumerate(dot_themes):
        pdf.new_page()
        pdf.add_centered_text(750, f"Connect the Dots: {dino_name}", font='HelveticaBold', size=18)
        pdf.add_centered_text(725, "Connect the numbers in order to reveal the dinosaur!", font='Helvetica', size=11)

        # Generate dots in a rough dinosaur shape
        random.seed(dot_idx * 33 + 99)
        num_dots = 30
        if dot_idx == 0:  # T-Rex shape
            base_points = [
                (200, 600), (220, 620), (250, 640), (280, 650), (310, 640),
                (330, 620), (340, 590), (350, 560), (360, 530), (370, 500),
                (380, 470), (390, 440), (400, 410), (390, 380), (370, 360),
                (350, 350), (330, 360), (320, 380), (310, 400), (300, 380),
                (290, 350), (280, 320), (270, 300), (260, 320), (250, 350),
                (240, 400), (220, 420), (200, 400), (190, 450), (195, 500),
            ]
        else:  # Triceratops shape
            base_points = [
                (180, 400), (200, 430), (220, 460), (250, 480), (280, 500),
                (310, 510), (340, 500), (370, 490), (400, 470), (420, 450),
                (430, 420), (420, 400), (400, 390), (380, 400), (360, 410),
                (340, 400), (320, 380), (300, 370), (280, 380), (260, 390),
                (240, 380), (220, 370), (210, 380), (200, 390), (190, 395),
                (230, 500), (250, 520), (200, 350), (180, 360), (175, 380),
            ]

        for i, (dx, dy) in enumerate(base_points):
            # Draw dot
            pdf.add_filled_rect(dx - 3, dy - 3, 6, 6, gray=0.0)
            # Number label
            pdf.add_text(dx + 5, dy + 5, str(i + 1), font='Helvetica', size=9)

        pdf.add_centered_text(40, f"- {dot_idx + 10} -", font='Helvetica', size=9)


    # --- DINOSAUR TRIVIA PAGES (3 pages) ---
    trivia_sets = [
        [
            ("How long ago did dinosaurs live?", "A) 1 million years", "B) 65 million years", "C) 500 years", "D) 1 billion years", "B"),
            ("What does 'dinosaur' mean?", "A) Big lizard", "B) Terrible lizard", "C) Ancient bird", "D) Giant monster", "B"),
            ("Which dinosaur had three horns?", "A) T-Rex", "B) Stegosaurus", "C) Triceratops", "D) Velociraptor", "C"),
            ("What do we call a scientist who studies dinosaurs?", "A) Biologist", "B) Geologist", "C) Paleontologist", "D) Zoologist", "C"),
        ],
        [
            ("Which was the biggest dinosaur?", "A) Velociraptor", "B) Argentinosaurus", "C) Compsognathus", "D) Troodon", "B"),
            ("What did T-Rex eat?", "A) Plants", "B) Fish only", "C) Other dinosaurs", "D) Insects", "C"),
            ("How many legs did most dinosaurs walk on?", "A) 2", "B) 4", "C) 6", "D) 2 or 4", "D"),
            ("What era did T-Rex live in?", "A) Triassic", "B) Jurassic", "C) Cretaceous", "D) Modern", "C"),
        ],
        [
            ("Which dinosaur could fly?", "A) Pterodactyl", "B) T-Rex", "C) Triceratops", "D) Stegosaurus", "A"),
            ("What killed the dinosaurs?", "A) Flood", "B) Ice Age", "C) Asteroid", "D) Humans", "C"),
            ("Which dinosaur had plates on its back?", "A) Diplodocus", "B) Stegosaurus", "C) Ankylosaurus", "D) Brachiosaurus", "B"),
            ("How fast could T-Rex run?", "A) 5 mph", "B) 100 mph", "C) 20 mph", "D) 50 mph", "C"),
        ],
    ]

    for t_idx, trivia in enumerate(trivia_sets):
        pdf.new_page()
        pdf.add_centered_text(750, f"Dino Trivia Quiz #{t_idx + 1}", font='HelveticaBold', size=20)
        pdf.add_centered_text(725, "Circle the correct answer!", font='Helvetica', size=12)

        y = 680
        for q_idx, (question, a, b, c, d, answer) in enumerate(trivia):
            pdf.add_text(72, y, f"{q_idx + 1}. {question}", font='HelveticaBold', size=12)
            y -= 25
            pdf.add_text(100, y, a, font='Helvetica', size=11)
            y -= 20
            pdf.add_text(100, y, b, font='Helvetica', size=11)
            y -= 20
            pdf.add_text(100, y, c, font='Helvetica', size=11)
            y -= 20
            pdf.add_text(100, y, d, font='Helvetica', size=11)
            y -= 35

        pdf.add_centered_text(40, f"- {t_idx + 12} -", font='Helvetica', size=9)


    # --- COLORING PAGES (3 pages with dino outlines) ---
    dino_color_pages = ["Tyrannosaurus Rex", "Stegosaurus", "Brachiosaurus"]

    for c_idx, dino in enumerate(dino_color_pages):
        pdf.new_page()
        pdf.add_centered_text(750, f"Color Me: {dino}", font='HelveticaBold', size=18)

        # Draw simple dinosaur outline
        if c_idx == 0:  # T-Rex
            draw_trex(pdf, 150, 200, 1.2)
        elif c_idx == 1:  # Stegosaurus
            draw_stegosaurus(pdf, 120, 250, 1.2)
        else:  # Brachiosaurus
            draw_brachiosaurus(pdf, 150, 200, 1.2)

        # Ground line
        pdf.add_line(72, 200, 540, 200, 1)
        # Simple plants
        for px in range(100, 520, 60):
            pdf.add_line(px, 200, px, 220, 0.5)
            pdf.add_line(px, 220, px - 8, 235, 0.5)
            pdf.add_line(px, 220, px + 8, 235, 0.5)

        pdf.add_centered_text(40, f"- {c_idx + 15} -", font='Helvetica', size=9)

    # --- DINO FACTS PAGE ---
    pdf.new_page()
    pdf.add_centered_text(740, "Amazing Dinosaur Facts!", font='HelveticaBold', size=22)
    pdf.add_line(150, 720, 462, 720, 1)
    facts = [
        "The word 'dinosaur' comes from Greek and means 'terrible lizard'.",
        "Some dinosaurs were as small as chickens!",
        "The T-Rex had teeth as big as bananas.",
        "Dinosaurs lived on every continent, including Antarctica.",
        "The longest dinosaur was Argentinosaurus at 130 feet long.",
        "Velociraptors were actually only about 2 feet tall.",
        "Some dinosaurs had over 1,000 teeth!",
        "Birds are the living descendants of dinosaurs.",
        "The Stegosaurus had a brain the size of a walnut.",
        "Dinosaurs ruled the Earth for over 160 million years.",
    ]
    y = 680
    for i, fact in enumerate(facts):
        pdf.add_text(72, y, f"  {i+1}.", font='HelveticaBold', size=12)
        # Simple word wrap
        if len(fact) > 60:
            pdf.add_text(105, y, fact[:60], font='Helvetica', size=11)
            pdf.add_text(105, y - 16, fact[60:], font='Helvetica', size=11)
            y -= 50
        else:
            pdf.add_text(105, y, fact, font='Helvetica', size=11)
            y -= 35


    # --- ANSWER KEY ---
    pdf.new_page()
    pdf.add_centered_text(740, "ANSWER KEY", font='HelveticaBold', size=22)
    pdf.add_line(200, 720, 412, 720, 1)
    pdf.add_text(72, 680, "Trivia Quiz #1:", font='HelveticaBold', size=12)
    pdf.add_text(72, 660, "1. B  2. B  3. C  4. C", font='Courier', size=11)
    pdf.add_text(72, 625, "Trivia Quiz #2:", font='HelveticaBold', size=12)
    pdf.add_text(72, 605, "1. B  2. C  3. D  4. C", font='Courier', size=11)
    pdf.add_text(72, 570, "Trivia Quiz #3:", font='HelveticaBold', size=12)
    pdf.add_text(72, 550, "1. A  2. C  3. B  4. C", font='Courier', size=11)

    # --- BACK PAGE ---
    pdf.new_page()
    pdf.add_centered_text(480, "Great Job, Dino Explorer!", font='HelveticaBold', size=22)
    pdf.add_centered_text(440, "You completed the activity book!", font='Helvetica', size=14)
    pdf.add_centered_text(400, "If you loved this book, ask a parent to leave", font='Helvetica', size=11)
    pdf.add_centered_text(380, "a review on Amazon. It helps a lot!", font='Helvetica', size=11)
    pdf.add_centered_text(330, "Check out more activity books:", font='HelveticaBold', size=12)
    pdf.add_centered_text(305, "- Ocean Animals Activity Book (Ages 7-10)", font='Helvetica', size=11)
    pdf.add_centered_text(283, "- Space & Planets Activity Book (Ages 7-10)", font='Helvetica', size=11)
    pdf.add_centered_text(261, "- Jungle Animals Activity Book (Ages 7-10)", font='Helvetica', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book4_Dinosaur_Activity_Book.pdf')
    print("Book 4 created: Book4_Dinosaur_Activity_Book.pdf")


def draw_simple_dino(pdf, x, y, scale=1):
    """Draw a simple T-Rex silhouette outline."""
    s = scale
    # Body
    pdf.add_rect(x, y, int(100*s), int(60*s), line_width=1.5)
    # Head
    pdf.add_rect(x + int(80*s), y + int(50*s), int(50*s), int(35*s), line_width=1.5)
    # Tail
    pdf.add_line(x, y + int(30*s), x - int(60*s), y + int(50*s), 1.5)
    pdf.add_line(x - int(60*s), y + int(50*s), x - int(70*s), y + int(40*s), 1.5)
    # Legs
    pdf.add_line(x + int(20*s), y, x + int(15*s), y - int(40*s), 1.5)
    pdf.add_line(x + int(60*s), y, x + int(55*s), y - int(40*s), 1.5)
    # Teeth
    for t in range(4):
        tx = x + int(85*s) + t * int(10*s)
        pdf.add_line(tx, y + int(50*s), tx + int(5*s), y + int(43*s), 1)

def draw_trex(pdf, x, y, scale=1):
    """Draw T-Rex outline for coloring."""
    s = scale
    # Body oval (simplified as rectangle)
    pdf.add_rect(x + int(50*s), y + int(80*s), int(180*s), int(120*s), line_width=2)
    # Head
    pdf.add_rect(x + int(200*s), y + int(170*s), int(100*s), int(60*s), line_width=2)
    # Jaw
    pdf.add_rect(x + int(210*s), y + int(155*s), int(90*s), int(20*s), line_width=1.5)
    # Eye
    pdf.add_rect(x + int(260*s), y + int(200*s), int(15*s), int(15*s))
    # Tail
    pdf.add_line(x + int(50*s), y + int(140*s), x, y + int(180*s), 2)
    pdf.add_line(x, y + int(180*s), x - int(20*s), y + int(160*s), 2)
    # Legs
    pdf.add_rect(x + int(100*s), y, int(25*s), int(80*s), line_width=1.5)
    pdf.add_rect(x + int(170*s), y, int(25*s), int(80*s), line_width=1.5)
    # Arms (small)
    pdf.add_line(x + int(180*s), y + int(160*s), x + int(195*s), y + int(130*s), 1.5)
    pdf.add_line(x + int(195*s), y + int(130*s), x + int(200*s), y + int(135*s), 1)


def draw_stegosaurus(pdf, x, y, scale=1):
    """Draw Stegosaurus outline for coloring."""
    s = scale
    # Body
    pdf.add_rect(x + int(60*s), y + int(50*s), int(200*s), int(100*s), line_width=2)
    # Head (smaller, forward)
    pdf.add_rect(x + int(250*s), y + int(80*s), int(60*s), int(40*s), line_width=2)
    # Tail (pointed)
    pdf.add_line(x + int(60*s), y + int(100*s), x, y + int(130*s), 2)
    pdf.add_line(x, y + int(130*s), x - int(30*s), y + int(120*s), 2)
    # Tail spikes
    for sp in range(4):
        sx = x + int(10*s) + sp * int(15*s)
        pdf.add_line(sx, y + int(125*s), sx - int(8*s), y + int(150*s), 1.5)
    # Plates on back
    for p in range(6):
        px = x + int(80*s) + p * int(30*s)
        pdf.add_line(px, y + int(150*s), px + int(10*s), y + int(185*s), 1.5)
        pdf.add_line(px + int(10*s), y + int(185*s), px + int(20*s), y + int(150*s), 1.5)
    # Legs
    pdf.add_rect(x + int(90*s), y, int(25*s), int(50*s), line_width=1.5)
    pdf.add_rect(x + int(140*s), y, int(25*s), int(50*s), line_width=1.5)
    pdf.add_rect(x + int(200*s), y, int(25*s), int(50*s), line_width=1.5)
    pdf.add_rect(x + int(240*s), y, int(25*s), int(50*s), line_width=1.5)

def draw_brachiosaurus(pdf, x, y, scale=1):
    """Draw Brachiosaurus outline for coloring."""
    s = scale
    # Body (large oval)
    pdf.add_rect(x + int(50*s), y + int(50*s), int(180*s), int(100*s), line_width=2)
    # Long neck
    pdf.add_line(x + int(180*s), y + int(150*s), x + int(220*s), y + int(300*s), 2)
    pdf.add_line(x + int(200*s), y + int(150*s), x + int(240*s), y + int(300*s), 2)
    # Head
    pdf.add_rect(x + int(215*s), y + int(300*s), int(40*s), int(25*s), line_width=2)
    # Eye
    pdf.add_rect(x + int(235*s), y + int(310*s), int(8*s), int(8*s))
    # Tail
    pdf.add_line(x + int(50*s), y + int(100*s), x, y + int(120*s), 2)
    pdf.add_line(x, y + int(120*s), x - int(30*s), y + int(100*s), 2)
    # Legs (tall front, shorter back)
    pdf.add_rect(x + int(70*s), y, int(25*s), int(50*s), line_width=1.5)
    pdf.add_rect(x + int(120*s), y, int(25*s), int(50*s), line_width=1.5)
    pdf.add_rect(x + int(170*s), y, int(25*s), int(70*s), line_width=1.5)
    pdf.add_rect(x + int(200*s), y, int(25*s), int(70*s), line_width=1.5)


if __name__ == '__main__':
    create_dinosaur_activity_book()
