"""Book 252: Large Print Word Search - Nature & Wildlife Edition"""
import random
import string
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(252 * 42)

THEMES = {
    "Birds": ["EAGLE", "ROBIN", "SPARROW", "HAWK", "CARDINAL", "FALCON", "PARROT", "PELICAN", "HERON", "DOVE"],
    "Flowers": ["ROSE", "TULIP", "DAISY", "ORCHID", "LILY", "SUNFLOWER", "IRIS", "PEONY", "VIOLET", "JASMINE"],
    "Trees": ["MAPLE", "OAK", "PINE", "BIRCH", "WILLOW", "CEDAR", "ELM", "REDWOOD", "ASH", "SPRUCE"],
    "Ocean Life": ["DOLPHIN", "WHALE", "SHARK", "OCTOPUS", "CORAL", "SEAHORSE", "STARFISH", "TURTLE", "JELLYFISH", "ORCA"],
    "Mountains": ["EVEREST", "ALPS", "ANDES", "ROCKIES", "SUMMIT", "PEAK", "RIDGE", "GLACIER", "VALLEY", "CLIFF"],
    "Rivers": ["AMAZON", "NILE", "DANUBE", "THAMES", "GANGES", "MISSISSIPPI", "RHINE", "VOLGA", "YANGTZE", "CONGO"],
    "Insects": ["BUTTERFLY", "BEETLE", "ANT", "DRAGONFLY", "CRICKET", "LADYBUG", "MOTH", "FIREFLY", "WASP", "MANTIS"],
    "Mammals": ["ELEPHANT", "TIGER", "BEAR", "WOLF", "DEER", "LION", "GIRAFFE", "ZEBRA", "MOOSE", "OTTER"],
    "Reptiles": ["LIZARD", "COBRA", "TURTLE", "GECKO", "PYTHON", "IGUANA", "VIPER", "CHAMELEON", "GATOR", "CROC"],
    "Weather": ["THUNDER", "LIGHTNING", "RAINBOW", "TORNADO", "BREEZE", "MONSOON", "BLIZZARD", "FROST", "HAIL", "CYCLONE"],
    "Seasons": ["SPRING", "SUMMER", "AUTUMN", "WINTER", "HARVEST", "BLOOM", "FROST", "THAW", "EQUINOX", "SOLSTICE"],
    "Gems & Minerals": ["DIAMOND", "RUBY", "EMERALD", "SAPPHIRE", "TOPAZ", "OPAL", "JADE", "GARNET", "AMETHYST", "QUARTZ"],
    "Planets": ["MERCURY", "VENUS", "EARTH", "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE", "PLUTO", "MOON"],
    "Constellations": ["ORION", "URSA", "DRACO", "LYRA", "PHOENIX", "PEGASUS", "SCORPIO", "GEMINI", "AQUILA", "CASSIOPEIA"],
    "National Parks": ["YELLOWSTONE", "YOSEMITE", "GLACIER", "ZION", "DENALI", "ACADIA", "SEQUOIA", "ARCHES", "CANYON", "OLYMPIC"],
    "Fish": ["SALMON", "TROUT", "BASS", "TUNA", "SWORDFISH", "MARLIN", "PERCH", "CATFISH", "PIKE", "COD"],
    "Butterflies": ["MONARCH", "SWALLOWTAIL", "PAINTED", "ADMIRAL", "SKIPPER", "MORPHO", "COPPER", "VICEROY", "BUCKEYE", "SULPHUR"],
    "Dogs": ["LABRADOR", "POODLE", "BEAGLE", "BULLDOG", "COLLIE", "HUSKY", "SPANIEL", "TERRIER", "BOXER", "DALMATIAN"],
    "Cats": ["PERSIAN", "SIAMESE", "BENGAL", "TABBY", "CALICO", "RAGDOLL", "SPHYNX", "BURMESE", "RUSSIAN", "MAINE"],
    "Gardens": ["PETAL", "BLOSSOM", "GARDEN", "SOIL", "MULCH", "COMPOST", "TRELLIS", "PRUNING", "HEDGE", "HERB"],
    "Forests": ["CANOPY", "FERN", "MOSS", "TRAIL", "CREEK", "HOLLOW", "THICKET", "GROVE", "GLADE", "WOODLAND"],
    "Deserts": ["CACTUS", "SAND", "DUNE", "OASIS", "MIRAGE", "SCORPION", "MESA", "CANYON", "ARID", "SAHARA"],
    "Arctic": ["POLAR", "ICEBERG", "AURORA", "TUNDRA", "PERMAFROST", "GLACIER", "ARCTIC", "PENGUIN", "SEAL", "WALRUS"],
    "Tropical": ["PALM", "COCONUT", "MANGO", "LAGOON", "CORAL", "PARROT", "TOUCAN", "BAMBOO", "ORCHID", "FERN"],
    "Farm": ["BARN", "TRACTOR", "HARVEST", "WHEAT", "CORN", "CHICKEN", "HORSE", "COW", "PIG", "SHEEP"],
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

def generate_word_search(words, grid_size=14):
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
            pdf.add_text(cx + cell_size*0.3, cy - cell_size*0.75, grid[row][col], font='F3', size=14)

pdf = PDFDoc(612, 792)

pdf.add_centered_text(560, "LARGE PRINT", font='F2', size=24)
pdf.add_centered_text(510, "WORD SEARCH", font='F2', size=28)
pdf.add_centered_text(460, "Nature & Wildlife Edition", font='F4', size=20)
pdf.add_centered_text(380, "25 Themed Puzzles", font='F1', size=16)
pdf.add_centered_text(100, "Daniel Tesfamariam", font='F2', size=14)

pdf.new_page()
pdf.add_centered_text(600, "LARGE PRINT WORD SEARCH - Nature & Wildlife", font='F2', size=13)
pdf.add_text(72, 540, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", font='F1', size=11)
pdf.add_text(72, 510, "No part of this publication may be reproduced without permission.", font='F1', size=11)

pdf.new_page()
pdf.add_centered_text(700, "HOW TO PLAY", font='F2', size=22)
pdf.add_text(72, 640, "Find all the hidden words in each puzzle grid.", font='F1', size=13)
pdf.add_text(72, 610, "Words can go in any direction: horizontal, vertical, or diagonal.", font='F1', size=13)
pdf.add_text(72, 580, "Words may read forward or backward.", font='F1', size=13)
pdf.add_text(72, 540, "The word list below each puzzle shows what to find.", font='F1', size=13)

theme_keys = list(THEMES.keys())
grid_size = 14
cell_size = 30

for idx in range(25):
    pdf.new_page()
    theme = theme_keys[idx]
    words = THEMES[theme]
    pdf.add_centered_text(750, f"Puzzle #{idx+1}: {theme}", font='F2', size=14)
    grid, placed = generate_word_search(words, grid_size)
    start_x = (612 - grid_size * cell_size) / 2
    start_y = 700
    pdf.add_rect(start_x - 2, start_y - grid_size*cell_size - 2, grid_size*cell_size + 4, grid_size*cell_size + 4, line_width=1.5)
    draw_word_search(pdf, grid, grid_size, start_x, start_y, cell_size)
    word_y = start_y - grid_size * cell_size - 40
    pdf.add_text(72, word_y, "Find these words:", font='F2', size=12)
    word_y -= 25
    for wi, w in enumerate(placed):
        wcol = wi % 3
        wrow = wi // 3
        pdf.add_text(72 + wcol * 170, word_y - wrow * 20, w.upper(), font='F1', size=11)

# Solutions
pdf.new_page()
pdf.add_centered_text(700, "SOLUTIONS", font='F2', size=24)
for sol_page in range(3):
    pdf.new_page()
    pdf.add_centered_text(750, f"Answer Key (Page {sol_page + 1})", font='F2', size=16)
    y_pos = 710
    start_idx = sol_page * 9
    for p in range(min(9, 25 - start_idx)):
        idx = start_idx + p
        theme = theme_keys[idx]
        words = THEMES[theme]
        pdf.add_text(72, y_pos, f"#{idx+1} - {theme}:", font='F2', size=9)
        y_pos -= 15
        pdf.add_text(72, y_pos, ", ".join([w.upper() for w in words[:10]])[:85], font='F1', size=8)
        y_pos -= 20

pdf.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book252_Word_Search_Nature.pdf"))
print("Book252_Word_Search_Nature.pdf created successfully!")
