"""Book 251: Large Print Bible Word Search - 25 Themed Puzzles for Adults"""
import random
import string
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

random.seed(251 * 42)

THEMES = {
    "Books of the Old Testament": ["GENESIS", "EXODUS", "LEVITICUS", "NUMBERS", "PSALMS", "PROVERBS", "ISAIAH", "JEREMIAH", "DANIEL", "JONAH"],
    "Books of the New Testament": ["MATTHEW", "MARK", "LUKE", "JOHN", "ACTS", "ROMANS", "HEBREWS", "JAMES", "PETER", "REVELATION"],
    "Psalms Words": ["PRAISE", "WORSHIP", "GLORY", "MERCY", "GRACE", "FAITHFUL", "REFUGE", "STRENGTH", "SHEPHERD", "DELIVER"],
    "Proverbs Wisdom": ["WISDOM", "PRUDENT", "KNOWLEDGE", "COUNSEL", "TRUTH", "JUSTICE", "VIRTUE", "DILIGENT", "HONEST", "HUMBLE"],
    "Fruits of the Spirit": ["LOVE", "JOY", "PEACE", "PATIENCE", "KINDNESS", "GOODNESS", "FAITHFUL", "GENTLE", "CONTROL", "SPIRIT"],
    "Armor of God": ["HELMET", "SWORD", "SHIELD", "BELT", "BREASTPLATE", "SHOES", "TRUTH", "FAITH", "PRAYER", "SALVATION"],
    "Parables of Jesus": ["SOWER", "MUSTARD", "PEARL", "VINEYARD", "TALENTS", "PRODIGAL", "SAMARITAN", "SHEPHERD", "WEDDING", "LEAVEN"],
    "Miracles of Jesus": ["HEALING", "WATER", "WINE", "LOAVES", "FISHES", "WALKING", "BLIND", "LEPER", "LAZARUS", "STORM"],
    "The Disciples": ["PETER", "ANDREW", "JAMES", "JOHN", "PHILIP", "MATTHEW", "THOMAS", "SIMON", "JUDAS", "BARTHOLOMEW"],
    "Angels in the Bible": ["GABRIEL", "MICHAEL", "CHERUBIM", "SERAPHIM", "ANGELS", "HEAVENLY", "MESSENGER", "WINGS", "GLORY", "GUARDIAN"],
    "Prophets": ["ELIJAH", "ELISHA", "ISAIAH", "JEREMIAH", "EZEKIEL", "DANIEL", "HOSEA", "AMOS", "MICAH", "MALACHI"],
    "Kings of Israel": ["DAVID", "SOLOMON", "SAUL", "JOSIAH", "HEZEKIAH", "REHOBOAM", "JEROBOAM", "AHAB", "UZZIAH", "ASA"],
    "Women of the Bible": ["RUTH", "ESTHER", "SARAH", "MARY", "MARTHA", "DEBORAH", "HANNAH", "NAOMI", "RACHEL", "MIRIAM"],
    "Men of Faith": ["ABRAHAM", "MOSES", "NOAH", "JOSEPH", "DAVID", "SAMUEL", "JOSHUA", "GIDEON", "CALEB", "ENOCH"],
    "Biblical Cities": ["JERUSALEM", "BETHLEHEM", "NAZARETH", "JERICHO", "NINEVEH", "BABYLON", "CORINTH", "EPHESUS", "ROME", "ANTIOCH"],
    "Mountains in the Bible": ["SINAI", "ARARAT", "CARMEL", "ZION", "OLIVE", "HERMON", "TABOR", "MORIAH", "NEBO", "HOREB"],
    "Rivers and Waters": ["JORDAN", "NILE", "EUPHRATES", "TIGRIS", "GALILEE", "OCEAN", "FLOOD", "BROOK", "SPRING", "RIVER"],
    "Animals in the Bible": ["LAMB", "LION", "DOVE", "SERPENT", "EAGLE", "FISH", "DONKEY", "CAMEL", "RAVEN", "WHALE"],
    "Foods in the Bible": ["BREAD", "WINE", "FIGS", "GRAPES", "OLIVES", "HONEY", "FISH", "MANNA", "WHEAT", "BARLEY"],
    "Trees in the Bible": ["OLIVE", "FIG", "CEDAR", "OAK", "PALM", "CYPRESS", "SYCAMORE", "ACACIA", "WILLOW", "ALMOND"],
    "Prayers": ["AMEN", "BLESSING", "PETITION", "THANKS", "PRAISE", "WORSHIP", "INTERCEDE", "MEDITATE", "SUPPLICATION", "FAITH"],
    "Commandments": ["HONOR", "WORSHIP", "TRUTH", "COVET", "STEAL", "MURDER", "ADULTERY", "SABBATH", "IDOLS", "NAME"],
    "Beatitudes": ["BLESSED", "MEEK", "MERCIFUL", "PURE", "PEACEFUL", "HUNGRY", "MOURN", "SPIRIT", "RIGHTEOUS", "PERSECUTED"],
    "Churches in Revelation": ["EPHESUS", "SMYRNA", "PERGAMOS", "THYATIRA", "SARDIS", "LAODICEA", "PHILADELPHIA"],
    "Heaven": ["ETERNAL", "GLORY", "THRONE", "ANGELS", "CROWN", "MANSIONS", "GATES", "STREETS", "PARADISE", "WORSHIP"],
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
            letter = grid[row][col]
            pdf.add_text(cx + cell_size*0.3, cy - cell_size*0.75, letter, font='F3', size=14)

pdf = PDFDoc(612, 792)

# Title
pdf.add_centered_text(560, "LARGE PRINT", font='F2', size=24)
pdf.add_centered_text(510, "BIBLE WORD SEARCH", font='F2', size=28)
pdf.add_centered_text(450, "25 Themed Puzzles for Adults", font='F1', size=18)
pdf.add_centered_text(380, "Books, People, Places & Themes", font='F1', size=14)
pdf.add_centered_text(100, "Daniel Tesfamariam", font='F2', size=14)

# Copyright
pdf.new_page()
pdf.add_centered_text(600, "LARGE PRINT BIBLE WORD SEARCH", font='F2', size=14)
pdf.add_text(72, 540, "Copyright 2025 Daniel Tesfamariam. All rights reserved.", font='F1', size=11)
pdf.add_text(72, 510, "No part of this publication may be reproduced without permission.", font='F1', size=11)

# Instructions
pdf.new_page()
pdf.add_centered_text(700, "HOW TO PLAY", font='F2', size=22)
pdf.add_text(72, 640, "Find all the hidden words in each grid.", font='F1', size=13)
pdf.add_text(72, 610, "Words can be hidden:", font='F1', size=13)
pdf.add_text(100, 585, "- Horizontally (left to right or right to left)", font='F1', size=12)
pdf.add_text(100, 560, "- Vertically (top to bottom or bottom to top)", font='F1', size=12)
pdf.add_text(100, 535, "- Diagonally (any direction)", font='F1', size=12)
pdf.add_text(72, 490, "Circle or highlight each word as you find it.", font='F1', size=13)
pdf.add_text(72, 460, "The word list appears below each puzzle.", font='F1', size=13)

# Puzzles
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
    
    # Draw grid border
    pdf.add_rect(start_x - 2, start_y - grid_size*cell_size - 2, grid_size*cell_size + 4, grid_size*cell_size + 4, line_width=1.5)
    draw_word_search(pdf, grid, grid_size, start_x, start_y, cell_size)
    
    # Word list
    word_y = start_y - grid_size * cell_size - 40
    pdf.add_text(72, word_y, "Find these words:", font='F2', size=12)
    word_y -= 25
    col_width = 170
    for wi, w in enumerate(placed):
        wcol = wi % 3
        wrow = wi // 3
        pdf.add_text(72 + wcol * col_width, word_y - wrow * 20, w.upper(), font='F1', size=11)

# Solutions
pdf.new_page()
pdf.add_centered_text(700, "SOLUTIONS", font='F2', size=24)
pdf.add_text(72, 640, "All words can be found in the grids above.", font='F1', size=12)
pdf.add_text(72, 610, "Words appear horizontally, vertically, or diagonally.", font='F1', size=12)

for sol_page in range(3):
    pdf.new_page()
    pdf.add_centered_text(750, f"Answer Key (Page {sol_page + 1})", font='F2', size=16)
    start_idx = sol_page * 9
    y_pos = 710
    for p in range(min(9, 25 - start_idx)):
        idx = start_idx + p
        theme = theme_keys[idx]
        words = THEMES[theme]
        pdf.add_text(72, y_pos, f"Puzzle #{idx+1} - {theme}:", font='F2', size=9)
        y_pos -= 15
        word_line = ", ".join([w.upper() for w in words[:10]])
        pdf.add_text(72, y_pos, word_line[:80], font='F1', size=8)
        y_pos -= 20

pdf.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book251_Word_Search_Bible.pdf"))
print("Book251_Word_Search_Bible.pdf created successfully!")
