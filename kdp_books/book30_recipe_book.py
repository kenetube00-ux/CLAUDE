"""
Book 30: MY FAMILY RECIPE BOOK - Preserve Your Favorite Recipes
KDP Interior - 8.5x11 inches (612x792 points)
Title page + copyright + TOC page + 50 recipe pages + conversion chart + index page
"""
from pdf_utils import PDFDoc

def create_recipe_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "MY FAMILY", font='F2', size=30)
    pdf.add_centered_text(610, "RECIPE BOOK", font='F2', size=30)
    pdf.add_line(150, 590, 462, 590, 2)
    pdf.add_centered_text(555, "Preserve Your Favorite Recipes", font='F4', size=15)
    pdf.add_centered_text(500, "50 Recipe Pages | Table of Contents", font='F1', size=11)
    pdf.add_centered_text(478, "Conversion Chart | Index", font='F1', size=11)
    pdf.add_centered_text(370, "By", font='F1', size=11)
    pdf.add_centered_text(345, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "MY FAMILY RECIPE BOOK", font='F2', size=13)
    pdf.add_centered_text(625, "Preserve Your Favorite Recipes", font='F1', size=10)
    pdf.add_centered_text(597, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(560, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(540, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(520, "Published via Amazon KDP", font='F1', size=9)
    pdf.add_centered_text(480, "Made with love.", font='F4', size=10)


    # --- TABLE OF CONTENTS PAGE ---
    pdf.new_page()
    pdf.add_text(72, 750, "TABLE OF CONTENTS", font='F2', size=14)
    pdf.add_line(72, 738, 540, 738, 0.8)

    y = 715
    pdf.add_text(72, y, "#", font='F2', size=8)
    pdf.add_text(95, y, "Recipe Name", font='F2', size=8)
    pdf.add_text(400, y, "Page", font='F2', size=8)
    pdf.add_line(72, y - 5, 540, y - 5, 0.4)
    y -= 18

    for i in range(1, 51):
        pdf.add_text(72, y, f"{i}.", font='F1', size=8)
        pdf.add_line(95, y - 2, 390, y - 2, 0.3, gray=0.5)
        pdf.add_line(400, y - 2, 440, y - 2, 0.3, gray=0.5)
        y -= 13
        if i == 25:
            # Start second column
            break

    # Continue on same page, second half
    for i in range(26, 51):
        pdf.add_text(72, y, f"{i}.", font='F1', size=8)
        pdf.add_line(95, y - 2, 390, y - 2, 0.3, gray=0.5)
        pdf.add_line(400, y - 2, 440, y - 2, 0.3, gray=0.5)
        y -= 13

    # --- 50 RECIPE PAGES ---
    for entry in range(1, 51):
        pdf.new_page()
        pdf.add_text(72, 750, f"RECIPE #{entry}", font='F2', size=12)
        pdf.add_line(72, 740, 540, 740, 0.8)

        y = 720
        # Recipe name
        pdf.add_text(72, y, "Recipe Name:", font='F2', size=10)
        pdf.add_line(155, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 22

        # Source/from
        pdf.add_text(72, y, "Source/From:", font='F2', size=10)
        pdf.add_line(148, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 22

        # Servings, Prep time, Cook time
        pdf.add_text(72, y, "Servings:", font='F2', size=10)
        pdf.add_line(125, y - 2, 195, y - 2, 0.3, gray=0.5)
        pdf.add_text(210, y, "Prep Time:", font='F2', size=10)
        pdf.add_line(270, y - 2, 350, y - 2, 0.3, gray=0.5)
        pdf.add_text(365, y, "Cook Time:", font='F2', size=10)
        pdf.add_line(425, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 22

        # Category
        pdf.add_text(72, y, "Category:", font='F2', size=10)
        pdf.add_line(128, y - 2, 300, y - 2, 0.3, gray=0.5)
        y -= 26

        # Ingredients
        pdf.add_text(72, y, "INGREDIENTS:", font='F2', size=10)
        y -= 16
        for i in range(15):
            pdf.add_line(72, y, 300, y, 0.3, gray=0.5)
            y -= 16
        y -= 10

        # Instructions
        pdf.add_text(72, y, "INSTRUCTIONS:", font='F2', size=10)
        y -= 16
        for i in range(12):
            pdf.add_text(72, y + 2, f"{i+1}.", font='F1', size=8)
            pdf.add_line(88, y, 540, y, 0.3, gray=0.5)
            y -= 16
        y -= 10

        # Notes
        pdf.add_text(72, y, "Notes:", font='F2', size=10)
        pdf.add_line(110, y - 2, 540, y - 2, 0.3, gray=0.5)
        y -= 20

        # Rating
        pdf.add_text(72, y, "Rating (1-5):", font='F2', size=10)
        for i in range(5):
            pdf.add_text(155 + i * 20, y, "*", font='F1', size=14)

        # Page number
        pdf.add_centered_text(40, f"- {entry + 3} -", font='F1', size=8)


    # --- CONVERSION CHART PAGE ---
    pdf.new_page()
    pdf.add_text(72, 750, "KITCHEN CONVERSION CHART", font='F2', size=14)
    pdf.add_line(72, 738, 540, 738, 0.8)

    y = 710
    pdf.add_text(72, y, "VOLUME", font='F2', size=11)
    y -= 20
    volume_conversions = [
        "1 tablespoon = 3 teaspoons",
        "1/4 cup = 4 tablespoons",
        "1/3 cup = 5 tablespoons + 1 teaspoon",
        "1/2 cup = 8 tablespoons",
        "1 cup = 16 tablespoons = 8 fluid ounces",
        "1 pint = 2 cups",
        "1 quart = 4 cups = 2 pints",
        "1 gallon = 4 quarts = 16 cups",
    ]
    for conv in volume_conversions:
        pdf.add_text(82, y, conv, font='F3', size=9)
        y -= 16
    y -= 20

    pdf.add_text(72, y, "WEIGHT", font='F2', size=11)
    y -= 20
    weight_conversions = [
        "1 ounce = 28 grams",
        "4 ounces = 1/4 pound = 113 grams",
        "8 ounces = 1/2 pound = 227 grams",
        "16 ounces = 1 pound = 454 grams",
        "2.2 pounds = 1 kilogram",
    ]
    for conv in weight_conversions:
        pdf.add_text(82, y, conv, font='F3', size=9)
        y -= 16
    y -= 20

    pdf.add_text(72, y, "TEMPERATURE", font='F2', size=11)
    y -= 20
    temp_conversions = [
        "250F = 120C (Low)",
        "300F = 150C (Low-Moderate)",
        "350F = 175C (Moderate)",
        "375F = 190C (Moderate-Hot)",
        "400F = 200C (Hot)",
        "425F = 220C (Hot)",
        "450F = 230C (Very Hot)",
    ]
    for conv in temp_conversions:
        pdf.add_text(82, y, conv, font='F3', size=9)
        y -= 16

    # --- INDEX PAGE ---
    pdf.new_page()
    pdf.add_text(72, 750, "INDEX", font='F2', size=14)
    pdf.add_line(72, 738, 540, 738, 0.8)

    y = 715
    for i in range(35):
        pdf.add_line(72, y, 540, y, 0.3, gray=0.5)
        y -= 18

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book30_Blank_Recipe_Book.pdf')
    print("Book 30 created: Book30_Blank_Recipe_Book.pdf")

if __name__ == '__main__':
    create_recipe_book()
