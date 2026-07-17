import sys, os
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

os.makedirs('/projects/sandbox/CLAUDE/BOOK_COVERS', exist_ok=True)

# Children's book covers - square format (8.5x8.5 = 612x612 pts)
# Design: Navy + gold + pastels, lamb icon, dreamy/gentle style

covers = [
    (426, "Selam_Bible_Bedtime_Toddlers", "Bible Bedtime\nStories for Toddlers",
     "30 Calming Scripture Tales with Gentle Prayers",
     ["30 Bible Stories", "Bedtime Prayers", "Ages 1-3", "Beautiful Illustrations", "Read-Aloud Format"],
     0.14, "Little Blessings Bible Series"),
    
    (427, "Selam_Bible_Bedtime_Prayers", "Bible Bedtime\nPrayers for\nLittle Ones",
     "30 Gentle Prayers & Scripture for Sweet Dreams",
     ["30 Guided Prayers", "Scripture-Based", "Ages 1-4", "Calming & Gentle", "Nightly Routine"],
     0.18, "Little Blessings Bible Series"),
    
    (428, "Selam_Bible_ABCs", "Bible ABCs",
     "A Scripture Alphabet for Toddlers",
     ["26 Letters of Faith", "Bible Characters", "Scripture Verses", "Ages 2-4", "Learn & Pray"],
     0.12, "Little Blessings Bible Series"),
    
    (429, "Selam_Bible_Preschoolers", "Bible Bedtime\nStories for\nPreschoolers",
     "20 Scripture Adventures for Growing Hearts",
     ["20 Bible Adventures", "Longer Stories", "Ages 3-5", "Discussion Prompts", "Bedtime Prayers"],
     0.20, "Little Blessings Bible Series"),
    
    (430, "Selam_First_Bible_Verses", "My First\nBible Verses",
     "20 Scriptures Every Toddler Should Know",
     ["20 Key Verses", "Simple Explanations", "Ages 1-4", "Memory Building", "Goodnight Prayers"],
     0.16, "Little Blessings Bible Series"),
    
    (431, "Selam_Brave_Bible_Kids", "Brave\nBible Kids",
     "15 Stories of Courage for Little Ones",
     ["15 Courage Stories", "Bible Heroes", "Ages 2-5", "Bravery Lessons", "Empowering Prayers"],
     0.22, "Little Blessings Bible Series"),
    
    (432, "Selam_God_Made_Me_Special", "God Made\nMe Special",
     "A Bible Book About Who I Am",
     ["Identity in Christ", "Self-Worth", "Ages 2-5", "Affirming Truth", "Scripture-Based"],
     0.15, "Little Blessings Bible Series"),
    
    (433, "Selam_Bible_Lullabies", "Bible Bedtime\nLullabies",
     "Scripture Songs to Sing Your Baby to Sleep",
     ["10 Lullaby Songs", "Psalm-Based", "Ages 0-3", "Calming Melodies", "Bedtime Worship"],
     0.19, "Little Blessings Bible Series"),
]

def create_childrens_cover(book_num, filename, title, subtitle, features, accent_gray, series):
    """Create a children's book cover - square format with gentle, dreamy design"""
    pdf = PDFDoc(width=612, height=612)  # 8.5x8.5 square
    pdf.new_page()
    
    # === FULL BACKGROUND (gentle warm tone) ===
    pdf.add_filled_rect(0, 0, 612, 612, gray=0.94)
    
    # === TOP ACCENT BAND (navy-style dark) ===
    pdf.add_filled_rect(0, 420, 612, 192, gray=accent_gray)
    
    # === DECORATIVE BORDER (double frame) ===
    pdf.add_rect(15, 15, 582, 582, line_width=2.5, gray=0.25)
    pdf.add_rect(22, 22, 568, 568, line_width=0.8, gray=0.45)
    
    # === SERIES NAME (top banner) ===
    pdf.add_filled_rect(150, 585, 312, 18, gray=0.25)
    pdf.add_text(175, 589, series, font='F1', size=9, gray=0.9)
    
    # === DECORATIVE STARS ===
    pdf.add_text(45, 560, "*", font='F2', size=18, gray=0.35)
    pdf.add_text(545, 565, "*", font='F2', size=14, gray=0.35)
    pdf.add_text(70, 440, "*", font='F2', size=12, gray=0.4)
    pdf.add_text(525, 445, "*", font='F2', size=10, gray=0.4)
    pdf.add_text(50, 100, "*", font='F2', size=10, gray=0.35)
    pdf.add_text(540, 90, "*", font='F2', size=14, gray=0.35)
    
    # === TITLE ===
    title_lines = title.split('\n')
    title_y = 550 if len(title_lines) <= 2 else 560
    for i, line in enumerate(title_lines):
        y_pos = title_y - (i * 38)
        if accent_gray < 0.20:
            pdf.add_centered_text(y_pos, line, font='F2', size=30, gray=0.95)
        else:
            pdf.add_centered_text(y_pos, line, font='F2', size=30, gray=0.0)
    
    # === SUBTITLE ===
    if accent_gray < 0.20:
        pdf.add_centered_text(430, subtitle, font='F4', size=12, gray=0.8)
    else:
        pdf.add_centered_text(430, subtitle, font='F4', size=12, gray=0.1)
    
    # === DECORATIVE DIVIDER (gentle curve-style) ===
    pdf.add_line(150, 405, 462, 405, width=1.5, gray=0.35)
    # Small lamb icon (represented as text symbol)
    pdf.add_filled_rect(285, 398, 42, 14, gray=0.94)
    pdf.add_text(291, 400, "lamb", font='F1', size=8, gray=0.35)
    
    # === FEATURES SECTION ===
    pdf.add_centered_text(375, "Inside This Book:", font='F2', size=10, gray=0.25)
    for i, feature in enumerate(features):
        y = 348 - (i * 24)
        pdf.add_text(170, y, "*", font='F2', size=10, gray=0.3)
        pdf.add_text(188, y, feature, font='F1', size=10, gray=0.18)
    
    # === ILLUSTRATION AREA (gentle placeholder) ===
    pdf.add_filled_rect(180, 150, 252, 70, gray=0.88)
    pdf.add_rect(180, 150, 252, 70, line_width=0.5, gray=0.5)
    pdf.add_centered_text(190, "[Cover Illustration]", font='F1', size=9, gray=0.4)
    pdf.add_centered_text(170, "Soft Watercolor Artwork", font='F1', size=8, gray=0.5)
    
    # === BOTTOM ACCENT BAND ===
    pdf.add_filled_rect(0, 30, 612, 55, gray=accent_gray)
    
    # === AUTHOR NAME ===
    if accent_gray < 0.20:
        pdf.add_centered_text(52, "SELAM FESEHAYE", font='F2', size=15, gray=0.95)
    else:
        pdf.add_centered_text(52, "SELAM FESEHAYE", font='F2', size=15, gray=0.0)
    
    # === AGE BADGE ===
    age = [f for f in features if "Ages" in f][0] if any("Ages" in f for f in features) else ""
    if age:
        pdf.add_filled_rect(480, 95, 90, 22, gray=0.25)
        pdf.add_text(490, 99, age, font='F2', size=9, gray=0.9)
    
    # === CORNER DECORATIONS (gentle arcs) ===
    pdf.add_line(30, 580, 60, 580, width=1.5, gray=0.35)
    pdf.add_line(30, 580, 30, 550, width=1.5, gray=0.35)
    pdf.add_line(552, 580, 582, 580, width=1.5, gray=0.35)
    pdf.add_line(582, 580, 582, 550, width=1.5, gray=0.35)
    pdf.add_line(30, 95, 60, 95, width=1.5, gray=0.35)
    pdf.add_line(30, 95, 30, 125, width=1.5, gray=0.35)
    pdf.add_line(552, 95, 582, 95, width=1.5, gray=0.35)
    pdf.add_line(582, 95, 582, 125, width=1.5, gray=0.35)
    
    # === BOOK NUMBER (subtle) ===
    pdf.add_text(540, 35, f"#{book_num}", font='F3', size=7, gray=0.5)
    
    # === TAGLINE ===
    pdf.add_centered_text(110, "Planting Seeds of Faith in Tiny Hearts", font='F4', size=9, gray=0.4)
    
    # Save
    output = f"/projects/sandbox/CLAUDE/BOOK_COVERS/Cover{book_num}_{filename}.pdf"
    pdf.save(output)
    return output

# Generate all 8 covers
print("=" * 70)
print("GENERATING COVERS: SELAM FESEHAYE'S LITTLE BLESSINGS BIBLE SERIES")
print("=" * 70)

for data in covers:
    path = create_childrens_cover(*data)
    size = os.path.getsize(path)
    print(f"  Cover {data[0]}: {data[2].split(chr(10))[0]:<35} ({size:,} bytes)")

print(f"\n{'=' * 70}")
print(f"ALL 8 COVERS CREATED SUCCESSFULLY!")
print("=" * 70)
