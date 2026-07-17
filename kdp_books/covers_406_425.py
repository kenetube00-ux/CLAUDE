import sys, os
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

os.makedirs('/projects/sandbox/CLAUDE/BOOK_COVERS', exist_ok=True)

# Etsy-style covers - brighter design with "INSTANT DOWNLOAD" badge
covers = [
    (406, "Etsy_Marriage_Prayer_Journal", "52-Week Marriage\nPrayer Journal", "A Year of United Prayer for Couples",
     ["52 Weekly Prayer Templates", "ACTS Prayer Model", "Scripture Prompts", "Couples Prayer Guide", "Printable Format"], 0.18),
    (407, "Etsy_Date_Night_Planner", "52 Date Nights for\nChristian Couples", "A Year of Intentional Romance",
     ["52 Creative Date Ideas", "Budget-Friendly Options", "Planning Templates", "Memory Keepsake Pages", "Rating & Review"], 0.25),
    (408, "Etsy_Communication_Workbook", "Communication\nWorkbook for Couples", "Biblical Tools for Better Conversations",
     ["Style Assessment", "Active Listening Tools", "Conflict Templates", "Daily Check-Ins", "12-Week Program"], 0.15),
    (409, "Etsy_Gratitude_Journal", "Marriage Gratitude\nJournal", "100 Days of Thankfulness for Your Spouse",
     ["100 Guided Pages", "Daily Prompts", "Gratitude Exercises", "Memory Keeper", "Prayer Responses"], 0.30),
    (410, "Etsy_Weekly_Marriage_Planner", "Weekly Marriage\nPlanner", "52 Weeks of Intentional Marriage Building",
     ["52 Weekly Spreads", "Goal Setting Pages", "Date Night Planning", "Prayer Focus", "Intimacy Tracker"], 0.20),
    (411, "Etsy_Bible_Study_Workbook", "Couples Bible Study\nWorkbook", "12 Scripture Sessions for Married Couples",
     ["12 In-Depth Studies", "Discussion Questions", "Application Exercises", "Prayer Prompts", "Memory Verses"], 0.35),
    (412, "Etsy_Love_Language_Workbook", "Love Language\nDiscovery Workbook", "Understanding How Your Spouse Feels Loved",
     ["Assessment Quiz", "5 Language Deep-Dives", "Weekly Practice Pages", "Action Idea Lists", "Progress Tracking"], 0.22),
    (413, "Etsy_Conflict_Resolution_Kit", "Conflict Resolution\nPrintable Kit", "Biblical Tools for Fighting Fair",
     ["Style Assessment", "Resolution Templates", "Cool-Down Protocol", "Rules of Engagement", "Repair Guides"], 0.28),
    (414, "Etsy_Intimacy_Workbook", "Intimacy Building\nWorkbook", "Growing Closer in Every Dimension",
     ["5 Intimacy Areas", "Weekly Exercises", "Action Plans", "Assessment Tools", "Couples Activities"], 0.16),
    (415, "Etsy_Budget_Planner", "Biblical Marriage\nBudget Planner", "Managing God's Resources as One",
     ["12 Monthly Budgets", "Debt Freedom Tracker", "Savings Goals", "Giving Tracker", "Financial Date Night"], 0.33),
    (416, "Etsy_Morning_Devotional", "90-Day Marriage\nMorning Devotional", "Start Each Day United in God's Word",
     ["90 Daily Readings", "Scripture Focus", "Application Prompts", "Couples Prayer", "Reflection Space"], 0.14),
    (417, "Etsy_Conversation_Starters", "200 Conversation\nStarters for Couples", "Deep Questions for Christian Marriages",
     ["200+ Questions", "5 Categories", "Monthly Check-Ins", "Discussion Notes", "Fun & Deep Topics"], 0.26),
    (418, "Etsy_Marriage_Goals_Planner", "Annual Marriage\nGoals Planner", "Setting & Achieving Goals Together",
     ["10 Goal Areas", "Quarterly Reviews", "Monthly Trackers", "Vision Statement", "Celebration Pages"], 0.19),
    (419, "Etsy_Forgiveness_Workbook", "Forgiveness Workbook\nfor Couples", "A Biblical Path to Freedom & Healing",
     ["Self-Assessment", "12 Forgiveness Exercises", "Trust Rebuilding", "Scripture Meditations", "Healing Journey"], 0.37),
    (420, "Etsy_Scripture_Memory_Cards", "52 Scripture Memory\nCards for Marriage", "One Verse Per Week to Transform Your Union",
     ["52 Printable Cards", "KJV Scripture", "Reflection Space", "Memory Aids", "Weekly Practice"], 0.21),
    (421, "Etsy_Marriage_Retreat_Kit", "Marriage Retreat\nat Home", "A Weekend Getaway Without Leaving",
     ["5 Sessions Included", "Activity Guides", "Discussion Prompts", "Prayer Templates", "Quarterly Mini-Retreats"], 0.32),
    (422, "Etsy_Newlywed_Journal", "Our First Year\nJournal", "Documenting 12 Months of Newlywed Life",
     ["12 Monthly Sections", "Check-In Worksheets", "Memory Pages", "Prayer Prompts", "Growth Tracking"], 0.17),
    (423, "Etsy_Counseling_Workbook", "Self-Guided Marriage\nCounseling Workbook", "8 Sessions You Can Do at Home",
     ["8 Full Sessions", "Individual Assessments", "Together Discussions", "Action Steps", "Prayer Closings"], 0.40),
    (424, "Etsy_Anniversary_Planner", "Anniversary\nCelebration Planner", "Making Every Year Memorable Together",
     ["25 Year Planning", "Vow Renewal Guide", "Love Letter Templates", "Gift Ideas", "Memory Keepsake"], 0.24),
    (425, "Etsy_Marriage_Emergency_Kit", "Marriage Emergency\nKit", "When Everything Falls Apart - Start Here",
     ["Crisis Triage Guide", "Emergency Protocols", "30-Day Rescue Plan", "Boundary Templates", "Hope Resources"], 0.13),
]

def create_cover(book_num, filename, title, subtitle, features, accent_gray):
    """Create an Etsy-optimized cover with INSTANT DOWNLOAD badge"""
    pdf = PDFDoc(width=432, height=648)  # 6x9 cover
    pdf.new_page()
    
    # BACKGROUND ACCENT BAND (top)
    pdf.add_filled_rect(0, 480, 432, 168, gray=accent_gray)
    
    # DECORATIVE BORDER
    pdf.add_rect(12, 12, 408, 624, line_width=2, gray=0.3)
    pdf.add_rect(18, 18, 396, 612, line_width=0.5, gray=0.5)
    
    # "INSTANT DOWNLOAD" badge at top
    pdf.add_filled_rect(130, 630, 172, 18, gray=0.3)
    pdf.add_text(140, 634, "INSTANT DOWNLOAD", font='F2', size=9, gray=0.95)
    
    # SECTION SEPARATOR
    pdf.add_line(30, 475, 402, 475, width=1.5, gray=0.4)
    
    # TITLE
    title_lines = title.split('\n')
    title_y_start = 590 if len(title_lines) <= 2 else 605
    for i, line in enumerate(title_lines):
        y_pos = title_y_start - (i * 35)
        if accent_gray < 0.25:
            pdf.add_centered_text(y_pos, line, font='F2', size=25, gray=0.95)
        else:
            pdf.add_centered_text(y_pos, line, font='F2', size=25, gray=0.0)
    
    # SUBTITLE
    sub_y = 488
    if accent_gray < 0.25:
        pdf.add_centered_text(sub_y, subtitle, font='F4', size=11, gray=0.85)
    else:
        pdf.add_centered_text(sub_y, subtitle, font='F4', size=11, gray=0.1)
    
    # DECORATIVE DIVIDER
    pdf.add_line(140, 458, 292, 458, width=1, gray=0.4)
    pdf.add_filled_rect(206, 454, 20, 8, gray=0.4)
    
    # FEATURES
    pdf.add_centered_text(433, "What's Inside:", font='F2', size=10, gray=0.2)
    for i, feature in enumerate(features):
        y = 410 - (i * 25)
        pdf.add_text(60, y, ">>", font='F2', size=9, gray=accent_gray)
        pdf.add_text(80, y, feature, font='F1', size=10, gray=0.15)
    
    # "PRINTABLE PDF" badge
    pdf.add_filled_rect(150, 260, 132, 20, gray=0.88)
    pdf.add_rect(150, 260, 132, 20, line_width=0.5, gray=0.4)
    pdf.add_text(162, 264, "PRINTABLE 8.5 x 11", font='F2', size=9, gray=0.2)
    
    # BOTTOM ACCENT BAND
    pdf.add_filled_rect(0, 40, 432, 55, gray=accent_gray)
    
    # AUTHOR NAME
    if accent_gray < 0.25:
        pdf.add_centered_text(60, "DANIEL TESFAMARIAM", font='F2', size=13, gray=0.95)
    else:
        pdf.add_centered_text(60, "DANIEL TESFAMARIAM", font='F2', size=13, gray=0.0)
    
    # BOOK NUMBER
    pdf.add_text(365, 20, f"#{book_num}", font='F3', size=8, gray=0.5)
    
    # CORNER ELEMENTS
    pdf.add_line(24, 620, 54, 620, width=1.5, gray=0.4)
    pdf.add_line(24, 620, 24, 590, width=1.5, gray=0.4)
    pdf.add_line(378, 620, 408, 620, width=1.5, gray=0.4)
    pdf.add_line(408, 620, 408, 590, width=1.5, gray=0.4)
    pdf.add_line(24, 105, 54, 105, width=1.5, gray=0.4)
    pdf.add_line(24, 105, 24, 135, width=1.5, gray=0.4)
    pdf.add_line(378, 105, 408, 105, width=1.5, gray=0.4)
    pdf.add_line(408, 105, 408, 135, width=1.5, gray=0.4)
    
    # BRAND
    pdf.add_centered_text(112, "BIBLE MADE SIMPLE", font='F1', size=9, gray=0.45)
    
    # "FOR ETSY" small tag
    pdf.add_text(30, 20, "Digital Download", font='F1', size=7, gray=0.5)
    
    output_path = f"/projects/sandbox/CLAUDE/BOOK_COVERS/Cover{book_num}_{filename}.pdf"
    pdf.save(output_path)
    return output_path

# Generate all 20 covers
print("=" * 70)
print("GENERATING ETSY COVERS FOR BOOKS 406-425")
print("=" * 70)

for cover_data in covers:
    path = create_cover(*cover_data)
    size = os.path.getsize(path)
    print(f"  Cover {cover_data[0]}: {cover_data[2].split(chr(10))[0][:35]:<37} ({size:,} bytes)")

print(f"\n{'=' * 70}")
print(f"ALL {len(covers)} ETSY COVERS CREATED SUCCESSFULLY!")
print("=" * 70)
