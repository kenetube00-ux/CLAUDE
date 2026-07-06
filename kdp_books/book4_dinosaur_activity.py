"""
Book 4: Dinosaur Activity Book (Ages 7-10)
KDP Interior - 8.5x11 inches (612x792 points)
WHITE background, BLACK text
"""
import random
from pdf_utils import PDFDoc

def draw_simple_dino(pdf, x, y, scale=1):
    """Draw a simple T-Rex silhouette outline."""
    s = scale
    pdf.add_rect(x, y, int(100*s), int(60*s), line_width=1.5)
    pdf.add_rect(x + int(80*s), y + int(50*s), int(50*s), int(35*s), line_width=1.5)
    pdf.add_line(x, y + int(30*s), x - int(60*s), y + int(50*s), 1.5)
    pdf.add_line(x - int(60*s), y + int(50*s), x - int(70*s), y + int(40*s), 1.5)
    pdf.add_line(x + int(20*s), y, x + int(15*s), y - int(40*s), 1.5)
    pdf.add_line(x + int(60*s), y, x + int(55*s), y - int(40*s), 1.5)

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
    draw_simple_dino(pdf, 260, 250, 1.5)
    pdf.add_centered_text(170, "By", font='Helvetica', size=12)
    pdf.add_centered_text(145, "Daniel Tesfamariam", font='HelveticaBold', size=18)
    pdf.add_centered_text(100, "Hours of Screen-Free Fun!", font='HelveticaBold', size=14)

    # --- COPYRIGHT ---
    pdf.new_page()
    pdf.add_centered_text(550, "Awesome Dinosaur Activity Book", font='HelveticaBold', size=14)
    pdf.add_centered_text(525, "For Kids Ages 7-10", font='Helvetica', size=11)
    pdf.add_centered_text(500, "By Daniel Tesfamariam", font='HelveticaBold', size=11)
    pdf.add_centered_text(470, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='Helvetica', size=9)
    pdf.add_centered_text(445, "ISBN: _______________", font='Helvetica', size=9)
    pdf.add_centered_text(420, "Published via Amazon KDP", font='Helvetica', size=9)

    # --- WORD SEARCH PAGES (4 pages) ---
    dino_word_lists = [
        ("Herbivore Dinosaurs", ["TRICERATOPS", "STEGOSAURUS", "DIPLODOCUS", "ANKYLOSAURUS",
         "IGUANODON", "APATOSAURUS", "BRONTOSAURUS", "HADROSAURUS"]),
        ("Carnivore Dinosaurs", ["TYRANNOSAURUS", "VELOCIRAPTOR", "SPINOSAURUS", "ALLOSAURUS",
         "CARNOTAURUS", "MEGALOSAURUS", "GIGANOTOSAURUS", "UTAHRAPTOR"]),
        ("Dinosaur World", ["JURASSIC", "CRETACEOUS", "TRIASSIC", "FOSSIL", "EXTINCT",
         "SKELETON", "VOLCANO", "ASTEROID"]),
        ("Dinosaur Body Parts", ["TEETH", "CLAWS", "TAIL", "HORNS", "SCALES",
         "WINGS", "BONES", "SKULL", "SPINE", "PLATES"]),
    ]

    for ws_idx, (title, words) in enumerate(dino_word_lists):
        pdf.new_page()
        pdf.add_centered_text(750, f"Word Search: {title}", font='HelveticaBold', size=18)
        pdf.add_centered_text(725, "Find all the hidden words!", font='Helvetica', size=11)

        grid_size = 14
        cell_size = 30
        start_x = (612 - grid_size * cell_size) / 2
        start_y = 680 - grid_size * cell_size

        random.seed(ws_idx * 100 + 42)
        for row in range(grid_size):
            for col in range(grid_size):
                x = start_x + col * cell_size
                y = start_y + (grid_size - 1 - row) * cell_size
                pdf.add_rect(x, y, cell_size, cell_size, line_width=0.5)
                letter = chr(random.randint(65, 90))
                pdf.add_text(x + 10, y + 8, letter, font='Courier', size=14)

        pdf.add_text(80, start_y - 30, "Find these words:", font='HelveticaBold', size=11)
        for w_idx, word in enumerate(words):
            wx = 80 if w_idx < 4 else 320
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

        random.seed(maze_idx * 50 + 7)
        maze_w, maze_h = 12, 12
        cell = 40
        mx_start = (612 - maze_w * cell) / 2
        my_start = 250

        pdf.add_rect(mx_start, my_start, maze_w * cell, maze_h * cell, line_width=2)
        pdf.add_text(mx_start - 5, my_start + maze_h * cell + 10, "START ->", font='HelveticaBold', size=12)
        pdf.add_text(mx_start + maze_w * cell - 50, my_start - 20, "-> END", font='HelveticaBold', size=12)

        for r in range(maze_h):
            for c in range(maze_w):
                x = mx_start + c * cell
                y = my_start + r * cell
                if random.random() < 0.4 and r > 0:
                    pdf.add_line(x, y, x + cell, y, 1.5)
                if random.random() < 0.4 and c > 0:
                    pdf.add_line(x, y, x, y + cell, 1.5)

        pdf.add_centered_text(40, f"- {maze_idx + 7} -", font='Helvetica', size=9)

    # --- TRIVIA (3 pages) ---
    trivia_sets = [
        [("How long ago did dinosaurs live?", "A) 1 million years", "B) 65 million years", "C) 500 years", "D) 1 billion years"),
         ("What does 'dinosaur' mean?", "A) Big lizard", "B) Terrible lizard", "C) Ancient bird", "D) Giant monster"),
         ("Which dinosaur had three horns?", "A) T-Rex", "B) Stegosaurus", "C) Triceratops", "D) Velociraptor")],
        [("Which was the biggest dinosaur?", "A) Velociraptor", "B) Argentinosaurus", "C) Compsognathus", "D) Troodon"),
         ("What did T-Rex eat?", "A) Plants", "B) Fish only", "C) Other dinosaurs", "D) Insects"),
         ("What era did T-Rex live in?", "A) Triassic", "B) Jurassic", "C) Cretaceous", "D) Modern")],
        [("Which dinosaur could fly?", "A) Pterodactyl", "B) T-Rex", "C) Triceratops", "D) Stegosaurus"),
         ("What killed the dinosaurs?", "A) Flood", "B) Ice Age", "C) Asteroid", "D) Humans"),
         ("Which dino had plates on its back?", "A) Diplodocus", "B) Stegosaurus", "C) Ankylosaurus", "D) Brachiosaurus")],
    ]

    for t_idx, trivia in enumerate(trivia_sets):
        pdf.new_page()
        pdf.add_centered_text(750, f"Dino Trivia Quiz #{t_idx + 1}", font='HelveticaBold', size=20)
        pdf.add_centered_text(725, "Circle the correct answer!", font='Helvetica', size=12)
        y = 680
        for q_idx, (question, a, b, c, d) in enumerate(trivia):
            pdf.add_text(72, y, f"{q_idx + 1}. {question}", font='HelveticaBold', size=12)
            y -= 25
            for opt in [a, b, c, d]:
                pdf.add_text(100, y, opt, font='Helvetica', size=11)
                y -= 20
            y -= 25
        pdf.add_centered_text(40, f"- {t_idx + 10} -", font='Helvetica', size=9)

    # --- DINO FACTS ---
    pdf.new_page()
    pdf.add_centered_text(740, "Amazing Dinosaur Facts!", font='HelveticaBold', size=22)
    pdf.add_line(150, 720, 462, 720, 1)
    facts = [
        "1. The word 'dinosaur' means 'terrible lizard' in Greek.",
        "2. Some dinosaurs were as small as chickens!",
        "3. The T-Rex had teeth as big as bananas.",
        "4. Dinosaurs lived on every continent.",
        "5. The longest dinosaur was 130 feet long.",
        "6. Velociraptors were only about 2 feet tall.",
        "7. Some dinosaurs had over 1,000 teeth!",
        "8. Birds are descendants of dinosaurs.",
        "9. Stegosaurus had a brain the size of a walnut.",
        "10. Dinosaurs ruled Earth for 160 million years.",
    ]
    y = 680
    for fact in facts:
        pdf.add_text(72, y, fact, font='Helvetica', size=12)
        y -= 40

    # --- ANSWER KEY ---
    pdf.new_page()
    pdf.add_centered_text(740, "ANSWER KEY", font='HelveticaBold', size=22)
    pdf.add_line(200, 720, 412, 720, 1)
    pdf.add_text(72, 680, "Trivia Quiz #1:  1.B  2.B  3.C", font='Courier', size=12)
    pdf.add_text(72, 645, "Trivia Quiz #2:  1.B  2.C  3.C", font='Courier', size=12)
    pdf.add_text(72, 610, "Trivia Quiz #3:  1.A  2.C  3.B", font='Courier', size=12)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book4_Dinosaur_Activity_Book.pdf')
    print("Book 4 created: Book4_Dinosaur_Activity_Book.pdf")

if __name__ == '__main__':
    create_dinosaur_activity_book()
