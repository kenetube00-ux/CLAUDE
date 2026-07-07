"""
Book 40: Large Print Word Search for Seniors - Volume 1
KDP Interior - 8.5x11 inches (612x792 points)
"""
import random
from pdf_utils import PDFDoc

def place_word(grid, word, size, rng):
    """Try to place a word in the grid. Returns True if successful."""
    directions = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]
    rng.shuffle(directions)
    for _ in range(100):
        dr, dc = rng.choice(directions)
        r = rng.randint(0, size-1)
        c = rng.randint(0, size-1)
        # Check if word fits
        end_r = r + dr * (len(word)-1)
        end_c = c + dc * (len(word)-1)
        if end_r < 0 or end_r >= size or end_c < 0 or end_c >= size:
            continue
        ok = True
        for i, ch in enumerate(word):
            gr = r + dr*i
            gc = c + dc*i
            if grid[gr][gc] != '' and grid[gr][gc] != ch:
                ok = False
                break
        if ok:
            for i, ch in enumerate(word):
                grid[r+dr*i][c+dc*i] = ch
            return True
    return False


def create_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "LARGE PRINT", font='F2', size=28)
    pdf.add_centered_text(600, "WORD SEARCH", font='F2', size=36)
    pdf.add_centered_text(555, "FOR SENIORS", font='F2', size=28)
    pdf.add_line(150, 535, 462, 535, 2)
    pdf.add_centered_text(505, "Volume 1", font='F4', size=18)
    pdf.add_centered_text(470, "25 Themed Puzzles with Solutions", font='F1', size=13)
    pdf.add_centered_text(445, "Easy-to-Read Large Print Format", font='F1', size=12)
    pdf.add_centered_text(320, "By", font='F1', size=12)
    pdf.add_centered_text(290, "Daniel Tesfamariam", font='F2', size=18)
    pdf.add_centered_text(200, "Fun & Relaxing Brain Exercise!", font='F2', size=14)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(550, "Large Print Word Search for Seniors - Volume 1", font='F2', size=12)
    pdf.add_centered_text(525, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(495, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(470, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(445, "Published via Amazon KDP", font='F1', size=9)

    # --- INSTRUCTIONS PAGE ---
    pdf.new_page()
    pdf.add_centered_text(700, "HOW TO PLAY", font='F2', size=22)
    pdf.add_line(180, 685, 432, 685, 1)
    y = 650
    instructions = [
        "1. Look at the word list below each puzzle.",
        "2. Find each word hidden in the grid of letters.",
        "3. Words can go in any direction:",
        "   - Horizontal (left to right or right to left)",
        "   - Vertical (top to bottom or bottom to top)",
        "   - Diagonal (any direction)",
        "4. Circle or highlight each word when you find it.",
        "5. Cross off words from the list as you find them.",
        "6. Solutions are provided at the back of the book.",
        "",
        "Tips:",
        "- Start with longer words - they are easier to spot.",
        "- Look for uncommon letters like Q, X, Z first.",
        "- Take your time and enjoy the puzzle!",
    ]
    for line in instructions:
        if line == "":
            y -= 15
        else:
            pdf.add_text(80, y, line, font='F1', size=13)
            y -= 28


    # --- 25 WORD SEARCH PUZZLE PAGES ---
    puzzles = [
        ("Fruits", ["APPLE", "BANANA", "CHERRY", "GRAPE", "ORANGE", "MANGO", "PEACH", "PLUM"]),
        ("Animals", ["ELEPHANT", "GIRAFFE", "DOLPHIN", "PENGUIN", "RABBIT", "TIGER", "EAGLE", "HORSE"]),
        ("Countries", ["FRANCE", "BRAZIL", "CANADA", "JAPAN", "EGYPT", "MEXICO", "INDIA", "ITALY"]),
        ("Colors", ["PURPLE", "YELLOW", "ORANGE", "GREEN", "SILVER", "GOLDEN", "VIOLET", "CORAL"]),
        ("Kitchen Items", ["SPATULA", "BLENDER", "TOASTER", "KETTLE", "GRATER", "SKILLET", "LADLE", "WHISK"]),
        ("Garden", ["TOMATO", "SHOVEL", "FLOWER", "COMPOST", "TRELLIS", "MULCH", "SEEDS", "FENCE"]),
        ("Music", ["GUITAR", "VIOLIN", "TRUMPET", "FLUTE", "RHYTHM", "MELODY", "CHORUS", "TEMPO"]),
        ("Sports", ["TENNIS", "SOCCER", "HOCKEY", "BOXING", "ROWING", "DIVING", "RUGBY", "GOLF"]),
        ("Weather", ["THUNDER", "RAINBOW", "BREEZE", "CLOUDY", "FROSTY", "STORMY", "SUNNY", "WINDY"]),
        ("Family", ["MOTHER", "FATHER", "SISTER", "BROTHER", "COUSIN", "NEPHEW", "NIECE", "UNCLE"]),
        ("Food", ["BURGER", "SUSHI", "PASTA", "TACOS", "PIZZA", "SALAD", "STEAK", "BREAD"]),
        ("Birds", ["ROBIN", "EAGLE", "SPARROW", "FALCON", "PARROT", "HERON", "CRANE", "FINCH"]),
        ("Flowers", ["DAISY", "TULIP", "ORCHID", "LILY", "VIOLET", "PEONY", "IRIS", "POPPY"]),
        ("Tools", ["HAMMER", "WRENCH", "PLIERS", "SCREWDRIVER", "DRILL", "LEVEL", "CLAMP", "CHISEL"]),
        ("Ocean", ["WHALE", "CORAL", "SHARK", "TURTLE", "SHELL", "WAVES", "ANCHOR", "TIDE"]),
        ("Holidays", ["CHRISTMAS", "EASTER", "THANKSGIVING", "VALENTINE", "HALLOWEEN", "NEWYEAR", "JULY", "LABOR"]),
        ("Clothing", ["JACKET", "SWEATER", "SCARF", "BOOTS", "GLOVES", "PANTS", "SHIRT", "DRESS"]),
        ("Vehicles", ["TRUCK", "TRAIN", "PLANE", "BICYCLE", "BOAT", "SUBWAY", "TAXI", "ROCKET"]),
        ("Desserts", ["COOKIE", "BROWNIE", "SUNDAE", "WAFFLE", "ECLAIR", "MOUSSE", "CREPE", "FUDGE"]),
        ("Nature", ["FOREST", "RIVER", "CANYON", "MEADOW", "VALLEY", "ISLAND", "DESERT", "LAKE"]),
        ("Seasons", ["SPRING", "SUMMER", "AUTUMN", "WINTER", "HARVEST", "BLOSSOM", "FROST", "BLOOM"]),
        ("Movies", ["COMEDY", "DRAMA", "ACTION", "HORROR", "THRILLER", "ROMANCE", "FANTASY", "WESTERN"]),
        ("Body Parts", ["SHOULDER", "ELBOW", "ANKLE", "WRIST", "FINGER", "SPINE", "KNEE", "HEART"]),
        ("Jobs", ["DOCTOR", "TEACHER", "PILOT", "NURSE", "ARTIST", "LAWYER", "CHEF", "FARMER"]),
        ("Famous Cities", ["PARIS", "LONDON", "TOKYO", "ROME", "CAIRO", "BERLIN", "SYDNEY", "MADRID"]),
    ]

    grid_size = 12
    cell_size = 38
    solutions = []

    for puz_idx, (theme, words) in enumerate(puzzles):
        pdf.new_page()
        pdf.add_centered_text(760, f"Puzzle #{puz_idx+1}: {theme}", font='F2', size=18)

        # Generate grid
        rng = random.Random(puz_idx * 42 + 7)
        grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]

        placed_words = []
        for word in words:
            if place_word(grid, word.upper(), grid_size, rng):
                placed_words.append(word)

        # Fill empty cells with random letters
        for r in range(grid_size):
            for c in range(grid_size):
                if grid[r][c] == '':
                    grid[r][c] = chr(rng.randint(65, 90))

        solutions.append((theme, placed_words))

        # Draw grid
        start_x = (612 - grid_size * cell_size) / 2
        start_y = 720 - grid_size * cell_size
        for r in range(grid_size):
            for c in range(grid_size):
                x = start_x + c * cell_size
                y = start_y + (grid_size - 1 - r) * cell_size
                pdf.add_rect(x, y, cell_size, cell_size, line_width=0.5)
                pdf.add_text(x + 12, y + 10, grid[r][c], font='F2', size=16)

        # Word list below grid
        wy = start_y - 30
        pdf.add_text(80, wy, "Find these words:", font='F2', size=12)
        wy -= 22
        for w_idx, word in enumerate(placed_words):
            wx = 80 if w_idx < 4 else 330
            wy2 = wy - (w_idx % 4) * 22
            pdf.add_text(wx, wy2, word, font='F3', size=12)

        pdf.add_centered_text(40, f"- {puz_idx + 4} -", font='F1', size=9)


    # --- SOLUTIONS PAGES (3 pages) ---
    for sol_page in range(3):
        pdf.new_page()
        pdf.add_centered_text(750, f"SOLUTIONS (Page {sol_page+1})", font='F2', size=18)
        pdf.add_line(150, 735, 462, 735, 1)
        y = 710
        start_idx = sol_page * 9
        end_idx = min(start_idx + 9, len(solutions))
        for s_idx in range(start_idx, end_idx):
            theme, words = solutions[s_idx]
            pdf.add_text(80, y, f"Puzzle #{s_idx+1} - {theme}:", font='F2', size=11)
            y -= 18
            words_str = ", ".join(words)
            pdf.add_text(90, y, words_str, font='F1', size=9)
            y -= 14
            if len(words_str) > 55:
                y -= 10
            y -= 18

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book40_Elderly_Word_Search.pdf')
    print("Book 40 created: Book40_Elderly_Word_Search.pdf")

if __name__ == '__main__':
    create_book()
