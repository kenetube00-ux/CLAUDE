"""Book 255: Extra Large Print Word Search for Seniors - Volume 2"""
import random
import string
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(255 * 42)

THEMES = {
    "Classic Movies": ["CASABLANCA", "CITIZEN", "WIZARD", "GONE", "SINGING", "PSYCHO", "VERTIGO", "REBECCA"],
    "Old TV Shows": ["BONANZA", "GUNSMOKE", "LASSIE", "DRAGNET", "TWILIGHT", "BEWITCHED", "GILLIGAN", "BATMAN"],
    "1950s-60s Music": ["ELVIS", "BEATLES", "MOTOWN", "SINATRA", "BUDDY", "CHUCK", "DRIFTERS", "PLATTERS"],
    "Vintage Cars": ["MUSTANG", "CORVETTE", "CADILLAC", "BUICK", "IMPALA", "THUNDERBIRD", "PONTIAC", "CHEVY"],
    "Retro Brands": ["ZENITH", "ADMIRAL", "PHILCO", "MOTOROLA", "FRIGIDAIRE", "POLAROID", "KODAK", "SEARS"],
    "Childhood Games": ["HOPSCOTCH", "JACKS", "MARBLES", "TAG", "KICKBALL", "JUMP", "FREEZE", "CAPTURE"],
    "Famous Couples": ["LUCY", "BOGART", "TRACY", "ASTAIRE", "BURNS", "ALLEN", "OZZIE", "HARRIET"],
    "Historical Events": ["APOLLO", "WOODSTOCK", "KENNEDY", "ELVIS", "BEATLES", "BERLIN", "MOON", "MARCH"],
    "Golden Age Hollywood": ["GARBO", "MONROE", "BOGART", "BACALL", "HEPBURN", "STEWART", "GRANT", "KELLY"],
    "Classic Books": ["GATSBY", "MOCKINGBIRD", "CATCHER", "GRAPES", "BRAVE", "FAREWELL", "PRIDE", "MOBY"],
    "Big Band Era": ["SWING", "MILLER", "DORSEY", "ELLINGTON", "GOODMAN", "BASIE", "SHAW", "CALLOWAY"],
    "Swing Dance": ["LINDY", "JIVE", "BOOGIE", "SWING", "CHARLESTON", "FOXTROT", "TWIRL", "STOMP"],
    "Radio Shows": ["SHADOW", "FIBBER", "AMOS", "ANDY", "LONE", "RANGER", "JACK", "BENNY"],
    "Newspaper Comics": ["PEANUTS", "BLONDIE", "BEETLE", "GARFIELD", "ARCHIE", "NANCY", "POPEYE", "DICK"],
    "Penny Candy": ["LICORICE", "JAWBREAKER", "TAFFY", "LOLLIPOP", "CANDY", "GUMBALL", "CARAMEL", "FUDGE"],
    "Soda Fountain": ["MALT", "FLOAT", "SUNDAE", "SHAKE", "SODA", "CHERRY", "VANILLA", "BANANA"],
    "Diner Food": ["BURGER", "FRIES", "MEATLOAF", "GRAVY", "MILKSHAKE", "PIE", "COFFEE", "TOAST"],
    "Drive-In Movies": ["POPCORN", "SPEAKER", "SCREEN", "DUSK", "DOUBLE", "FEATURE", "SNACK", "STARS"],
    "Sock Hop": ["POODLE", "SADDLE", "PONYTAIL", "BOBBY", "JUKEBOX", "MALT", "DANCE", "TWIST"],
    "Rotary Phone Era": ["DIAL", "OPERATOR", "PARTY", "LINE", "BUSY", "RING", "CORD", "BOOTH"],
    "Typewriter Words": ["RIBBON", "CARRIAGE", "KEYS", "PLATEN", "BELL", "TAB", "SHIFT", "RETURN"],
    "Vinyl Records": ["ALBUM", "SINGLE", "GROOVE", "NEEDLE", "STEREO", "TURNTABLE", "SLEEVE", "VINYL"],
    "Transistor Radio": ["TRANSISTOR", "ANTENNA", "DIAL", "SPEAKER", "BATTERY", "STATION", "TUNE", "VOLUME"],
    "Black and White TV": ["RABBIT", "ANTENNA", "CHANNEL", "TUBE", "KNOB", "STATIC", "CONSOLE", "SCREEN"],
    "Corner Store": ["PENNY", "NICKEL", "CANDY", "SODA", "COUNTER", "REGISTER", "BELL", "SHELF"],
}

def place_word_in_grid(grid, word, grid_size):
    directions = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]
    for attempt in range(100):
        direction = random.choice(directions)
        dr, dc = direction
        max_r = grid_size - 1 if dr == 0 else (grid_size - len(word) if dr > 0 else grid_size - 1)
        min_r = 0 if dr >= 0 else len(word) - 1
        max_c = grid_size - 1 if dc == 0 else (grid_size - len(word) if dc > 0 else grid_size - 1)
        min_c = 0 if dc >= 0 else len(word) - 1
        if min_r > max_r or min_c > max_c:
            continue
        row = random.randint(min_r, max_r)
        col = random.randint(min_c, max_c)
        can_place = True
        for i in range(len(word)):
            r = row + i * dr
            c = col + i * dc
            if r < 0 or r >= grid_size or c < 0 or c >= grid_size:
                can_place = False
                break
            if grid[r][c] != '' and grid[r][c] != word[i]:
                can_place = False
                break
        if can_place:
            for i in range(len(word)):
                r = row + i * dr
                c = col + i * dc
                grid[r][c] = word[i]
            return True
    return False

def generate_word_search(words, grid_size=12):
    grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]
    placed_words = []
    for word in words:
        w = word.upper().replace(' ', '')
        if len(w) <= grid_size and place_word_in_grid(grid, w, grid_size):
            placed_words.append(word)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == '':
                grid[i][j] = random.choice(string.ascii_uppercase)
    return grid, placed_words

def draw_word_search(pdf, grid, grid_size, start_x, start_y, cell_size):
    for row in range(grid_size):
        for col in range(grid_size):
            cx = start_x + col * cell_size
            cy = start_y - row * cell_size
            pdf.add_text(cx + cell_size*0.25, cy - cell_size*0.72, grid[row][col], font='F3', size=18)

pdf = PDFDoc(612, 792)

pdf.add_centered_text(560, "EXTRA LARGE PRINT", font='F2', size=26)
pdf.add_centered_text(510, "WORD SEARCH", font='F2', size=30)
pdf.add_centered_text(460, "FOR SENIORS", font='F2', size=22)
pdf.add_centered_text(410, "Volume 2", font='F1', size=18)
pdf.add_centered_text(350, "25 Nostalgic Themed Puzzles", font='F1', size=16)
pdf.add_centered_text(310, "12x12 Grids - 8 Words Per Puzzle", font='F1', size=13)
pdf.add_centered_text(100, "Daniel Tesfamariam", font='F2', size=14)

pdf.new_page()
pdf.add_centered_text(600, "EXTRA LARGE PRINT WORD SEARCH FOR SENIORS", font='F2', size=12)
pdf.add_text(72, 540, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", font='F1', size=11)
pdf.add_text(72, 510, "No part of this publication may be reproduced without permission.", font='F1', size=11)
pdf.add_text(72, 460, "Designed with extra-large letters for easy reading.", font='F1', size=12)
pdf.add_text(72, 435, "Nostalgic themes from the golden days.", font='F4', size=12)

pdf.new_page()
pdf.add_centered_text(700, "HOW TO PLAY", font='F2', size=24)
pdf.add_text(72, 630, "Find all the hidden words in each puzzle.", font='F1', size=15)
pdf.add_text(72, 590, "Words go horizontal, vertical, or diagonal.", font='F1', size=15)
pdf.add_text(72, 550, "Words may go forward or backward.", font='F1', size=15)
pdf.add_text(72, 500, "8 words per puzzle. Take your time!", font='F2', size=15)

theme_keys = list(THEMES.keys())
grid_size = 12
cell_size = 38  # Extra large cells

for idx in range(25):
    pdf.new_page()
    theme = theme_keys[idx]
    words = THEMES[theme][:8]
    pdf.add_centered_text(755, f"Puzzle #{idx+1}", font='F2', size=18)
    pdf.add_centered_text(732, theme, font='F4', size=14)
    grid, placed = generate_word_search(words, grid_size)
    start_x = (612 - grid_size * cell_size) / 2
    start_y = 690
    pdf.add_rect(start_x - 3, start_y - grid_size*cell_size - 3, grid_size*cell_size + 6, grid_size*cell_size + 6, line_width=2)
    draw_word_search(pdf, grid, grid_size, start_x, start_y, cell_size)
    word_y = start_y - grid_size * cell_size - 45
    pdf.add_text(72, word_y, "Find these words:", font='F2', size=14)
    word_y -= 30
    for wi, w in enumerate(placed):
        wcol = wi % 2
        wrow = wi // 2
        pdf.add_text(90 + wcol * 230, word_y - wrow * 25, w.upper(), font='F1', size=14)

# Solutions
pdf.new_page()
pdf.add_centered_text(700, "SOLUTIONS", font='F2', size=26)
for sol_page in range(3):
    pdf.new_page()
    pdf.add_centered_text(750, f"Answer Key (Page {sol_page + 1})", font='F2', size=16)
    y_pos = 700
    start_idx = sol_page * 9
    for p in range(min(9, 25 - start_idx)):
        idx = start_idx + p
        theme = theme_keys[idx]
        words = THEMES[theme][:8]
        pdf.add_text(72, y_pos, f"#{idx+1} - {theme}:", font='F2', size=10)
        y_pos -= 18
        pdf.add_text(72, y_pos, ", ".join([w.upper() for w in words]), font='F1', size=9)
        y_pos -= 25

pdf.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book255_Word_Search_Seniors.pdf"))
print("Book255_Word_Search_Seniors.pdf created successfully!")
