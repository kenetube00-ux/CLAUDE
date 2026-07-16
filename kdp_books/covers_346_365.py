import sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc
import os

# Ensure BOOK_COVERS directory exists
os.makedirs('/projects/sandbox/CLAUDE/BOOK_COVERS', exist_ok=True)

# Cover data: (book_num, filename_suffix, title, subtitle, features, accent_gray)
covers = [
    (346, "Girls_Changed_World", "Girls Who Changed\nthe World", "25 True Stories of Courage & Inspiration", 
     ["25 Real Women's Stories", "Ages 8-14", "Discussion Questions", "Timeline Activities", "Growth Mindset Lessons"], 0.25),
    
    (347, "Mother_Daughter_Journal", "Between Us:\nMother-Daughter\nJournal", "60 Guided Prompts for Connection", 
     ["60 Shared Prompts", "Bonding Activities", "Memory Pages", "Letter Templates", "Keepsake Format"], 0.35),
    
    (348, "Girls_Confidence", "She Believed\nShe Could", "A Girl's Confidence Workbook", 
     ["15 Self-Esteem Chapters", "Daily Affirmations", "Goal-Setting Tools", "Journaling Prompts", "Ages 9-14"], 0.20),
    
    (349, "Women_Science", "Women in Science", "20 Female Scientists Who Changed Everything", 
     ["20 Scientist Profiles", "STEM Activities", "Lab Experiments", "Career Exploration", "Ages 9-14"], 0.30),
    
    (350, "Girls_Puberty", "Growing Up Girl", "Your Complete Puberty & Body Guide", 
     ["Body Changes Explained", "Emotional Health Tips", "Hygiene Guides", "Q&A Format", "Ages 9-14"], 0.22),
    
    (351, "Mom_Self_Care", "The Overwhelmed\nMom's Self-Care\nGuide", "15 Chapters to Reclaim Your Wellness", 
     ["Stress Management", "Sleep Strategies", "Boundary Setting", "Mindfulness Exercises", "Weekly Planners"], 0.38),
    
    (352, "Girls_Money", "Girls & Money", "A Financial Literacy Workbook for Smart Girls", 
     ["Budgeting Basics", "Saving Strategies", "Entrepreneurship 101", "Money Worksheets", "Ages 10-15"], 0.28),
    
    (353, "Girls_STEM", "Girls in STEM", "50 Hands-On Science & Engineering Projects", 
     ["50 DIY Projects", "Step-by-Step Guides", "Science Explanations", "Engineering Challenges", "Ages 8-13"], 0.18),
    
    (354, "Women_History", "Women Who\nMade History", "30 Trailblazers Every Girl Should Know", 
     ["30 Biographies", "Historical Context", "Legacy Lessons", "Activity Pages", "Ages 9-15"], 0.32),
    
    (355, "Girls_Journal", "My Amazing Life", "365 Guided Journal Prompts for Girls", 
     ["365 Daily Prompts", "Gratitude Sections", "Creative Writing", "Self-Discovery", "Ages 9-14"], 0.24),
    
    (356, "Pregnancy_Guide", "First-Time Mom", "Your Week-by-Week Pregnancy Guide", 
     ["40 Weekly Updates", "Baby Development", "Health Checklists", "Birth Planning", "Postpartum Prep"], 0.40),
    
    (357, "Girls_Leadership", "Lead Like a Girl", "A Leadership Workbook for Future Change-Makers", 
     ["12 Leadership Chapters", "Team-Building Skills", "Public Speaking Tips", "Project Planning", "Ages 10-15"], 0.15),
    
    (358, "Women_Sports", "Game Changers", "25 Women Athletes Who Broke Barriers", 
     ["25 Athlete Stories", "Sports History", "Training Mindset", "Goal Setting", "Ages 8-14"], 0.27),
    
    (359, "Girls_Emotions", "Big Feelings\nAre Okay", "An Emotional Intelligence Guide for Girls", 
     ["Emotion Identification", "Coping Strategies", "Mindfulness Tools", "Communication Skills", "Ages 8-13"], 0.33),
    
    (360, "Working_Mom", "The Working Mom's\nSurvival Guide", "Balance, Boundaries & Thriving at Work + Home", 
     ["Time Management", "Career Growth Tips", "Family Routines", "Self-Care Practices", "Guilt-Free Framework"], 0.42),
    
    (361, "Girls_Body_Positive", "Love Your Body", "A Body Positivity Workbook for Girls", 
     ["Self-Love Exercises", "Media Literacy", "Health vs. Appearance", "Affirmation Cards", "Ages 10-15"], 0.19),
    
    (362, "Mother_Daughter_Activities", "50 Mother-Daughter\nActivities", "Creative Ways to Bond & Make Memories", 
     ["50 Fun Activities", "Indoor & Outdoor", "Craft Projects", "Cooking Together", "All Ages"], 0.36),
    
    (363, "Girls_Code", "Girls Who Code", "A Beginner's Guide to Programming & Tech", 
     ["15 Coding Chapters", "Scratch & Python", "Logic Puzzles", "Real-World Projects", "Ages 9-14"], 0.23),
    
    (364, "New_Mom_First_Year", "The First Year", "A New Mom's Month-by-Month Guide", 
     ["12 Monthly Chapters", "Baby Milestones", "Mom Recovery", "Sleep Training", "Feeding Guides"], 0.37),
    
    (365, "Girls_Dream_Big", "Dream Big, Girl!", "A Goal-Setting Journal for Future Leaders", 
     ["Vision Board Pages", "Goal Frameworks", "Monthly Check-Ins", "Inspiration Quotes", "Ages 10-15"], 0.21),
]

def create_cover(book_num, filename_suffix, title, subtitle, features, accent_gray):
    """Create a professional KDP cover page"""
    pdf = PDFDoc(width=432, height=648)  # 6x9 cover size
    pdf.new_page()
    
    # === BACKGROUND ACCENT BAND (top) ===
    pdf.add_filled_rect(0, 480, 432, 168, gray=accent_gray)
    
    # === DECORATIVE BORDER ===
    pdf.add_rect(12, 12, 408, 624, line_width=2, gray=0.3)
    pdf.add_rect(18, 18, 396, 612, line_width=0.5, gray=0.5)
    
    # === INNER DECORATIVE LINE (top section separator) ===
    pdf.add_line(30, 475, 402, 475, width=1.5, gray=0.4)
    
    # === TITLE ===
    title_lines = title.split('\n')
    title_y_start = 580 if len(title_lines) <= 2 else 600
    for i, line in enumerate(title_lines):
        y_pos = title_y_start - (i * 38)
        # White text on dark band
        if accent_gray < 0.35:
            pdf.add_centered_text(y_pos, line, font='F2', size=28, gray=0.95)
        else:
            pdf.add_centered_text(y_pos, line, font='F2', size=28, gray=0.0)
    
    # === SUBTITLE ===
    sub_y = 490
    if accent_gray < 0.35:
        pdf.add_centered_text(sub_y, subtitle, font='F4', size=13, gray=0.85)
    else:
        pdf.add_centered_text(sub_y, subtitle, font='F4', size=13, gray=0.1)
    
    # === DECORATIVE DIVIDER ===
    pdf.add_line(140, 460, 292, 460, width=1, gray=0.4)
    pdf.add_filled_rect(206, 456, 20, 8, gray=0.4)  # center diamond
    
    # === FEATURES SECTION ===
    feature_y_start = 420
    pdf.add_centered_text(feature_y_start + 15, "What's Inside:", font='F2', size=11, gray=0.2)
    
    for i, feature in enumerate(features):
        y = feature_y_start - (i * 28)
        # Bullet point style
        pdf.add_text(60, y, ">>", font='F2', size=10, gray=accent_gray)
        pdf.add_text(82, y, feature, font='F1', size=11, gray=0.15)
    
    # === BOTTOM ACCENT BAND ===
    pdf.add_filled_rect(0, 40, 432, 55, gray=accent_gray)
    
    # === AUTHOR NAME (in bottom band) ===
    if accent_gray < 0.35:
        pdf.add_centered_text(60, "DANIEL TESFAMARIAM", font='F2', size=14, gray=0.95)
    else:
        pdf.add_centered_text(60, "DANIEL TESFAMARIAM", font='F2', size=14, gray=0.0)
    
    # === BOOK NUMBER (small, bottom corner) ===
    pdf.add_text(365, 20, f"#{book_num}", font='F3', size=8, gray=0.5)
    
    # === DECORATIVE CORNER ELEMENTS ===
    # Top-left
    pdf.add_line(24, 620, 54, 620, width=1.5, gray=0.4)
    pdf.add_line(24, 620, 24, 590, width=1.5, gray=0.4)
    # Top-right
    pdf.add_line(378, 620, 408, 620, width=1.5, gray=0.4)
    pdf.add_line(408, 620, 408, 590, width=1.5, gray=0.4)
    # Bottom-left
    pdf.add_line(24, 105, 54, 105, width=1.5, gray=0.4)
    pdf.add_line(24, 105, 24, 135, width=1.5, gray=0.4)
    # Bottom-right
    pdf.add_line(378, 105, 408, 105, width=1.5, gray=0.4)
    pdf.add_line(408, 105, 408, 135, width=1.5, gray=0.4)
    
    # === BRAND TAG ===
    pdf.add_centered_text(112, "KIDLYTICAL", font='F1', size=9, gray=0.45)
    
    # Save
    output_path = f"/projects/sandbox/CLAUDE/BOOK_COVERS/Cover{book_num}_{filename_suffix}.pdf"
    pdf.save(output_path)
    return output_path

# Generate all 20 covers
print("=" * 60)
print("GENERATING COVERS FOR BOOKS 346-365")
print("=" * 60)

for cover_data in covers:
    path = create_cover(*cover_data)
    size = os.path.getsize(path)
    print(f"  ✓ Cover {cover_data[0]}: {cover_data[2].split(chr(10))[0]} ({size:,} bytes)")

print("\n" + "=" * 60)
print(f"ALL 20 COVERS CREATED SUCCESSFULLY!")
print("=" * 60)
