"""
Generate Book Covers 6-70 (65 covers total)
KDP Covers using pdf_utils.py - White background with accent elements
"""
import sys
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

AUTHOR = "Daniel Tesfamariam"

# Book data: (book_num, title, subtitle, filename, features_list)
# Sizes: 6x9 = 432x648, 8.5x11 = 612x792
BOOKS_6x9 = {6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 27, 28, 29,
              31, 32, 33, 34, 36, 38, 39, 41, 42, 43, 45, 47, 48, 49, 51, 53, 55,
              58, 59, 61, 62, 63, 64, 65, 68, 69, 70}

BOOKS_85x11 = {9, 10, 16, 20, 24, 26, 30, 35, 37, 40, 44, 46, 50, 52, 54, 56, 57, 60, 66, 67}

BOOK_DATA = [
    (6, "LARGE PRINT BLOOD PRESSURE LOG BOOK", "Daily Tracking for Seniors",
     "Cover6_Blood_Pressure_Log.pdf",
     ["Daily AM/PM Recording Pages", "120/80 Goal Reference Charts", "Large Easy-to-Read Format", "52 Weeks of Tracking"]),
    (7, "GOLDEN RETRIEVER OWNER'S JOURNAL", "Health Records & Memories",
     "Cover7_Golden_Retriever.pdf",
     ["Vet Visit Records", "Vaccination Tracker", "Growth Milestones", "Photo Memory Pages"]),
    (8, "SOBRIETY TRACKER & RECOVERY JOURNAL", "One Day at a Time",
     "Cover8_Sobriety_Tracker.pdf",
     ["Daily Sobriety Counter", "Mood & Trigger Tracking", "Gratitude Reflections", "Milestone Celebrations"]),
    (9, "BACKYARD GARDEN PLANNER & LOG", "Plan, Plant, Grow",
     "Cover9_Garden_Planner.pdf",
     ["Seasonal Planting Guides", "Garden Layout Pages", "Plant Care Logs", "Harvest Tracker"]),
    (10, "DARK ACADEMIA COLORING BOOK", "Gothic Illustrations for Adults",
     "Cover10_Dark_Academia_Coloring.pdf",
     ["35+ Detailed Illustrations", "Gothic Architecture", "Vintage Library Scenes", "Single-Sided Pages"]),
    (11, "DIABETES FOOD & BLOOD SUGAR LOG", "Daily Glucose Tracker",
     "Cover11_Diabetes_Food_Log.pdf",
     ["Before/After Meal Logging", "Carb & Medication Notes", "A1C Goal Tracking", "90-Day Format"]),
    (12, "PICKLEBALL SCORE BOOK", "100 Match Score Sheets",
     "Cover12_Pickleball_Score.pdf",
     ["100 Match Score Sheets", "Singles & Doubles Format", "Tournament Brackets", "Player Stats Pages"]),
    (13, "FOREVER IN MY HEART", "Pet Loss Grief Journal",
     "Cover13_Pet_Loss_Journal.pdf",
     ["Guided Grief Prompts", "Memory Pages", "Photo Keepsake Sections", "Healing Affirmations"]),
    (14, "ADHD-FRIENDLY DAILY PLANNER", "Designed for the ADHD Brain",
     "Cover14_ADHD_Planner.pdf",
     ["Time-Block Scheduling", "Priority Task Lists", "Brain Dump Pages", "Habit Tracking"]),
    (15, "KETO MEAL PLANNER", "& Macro Tracker",
     "Cover15_Keto_Meal_Planner.pdf",
     ["Weekly Meal Plans", "Net Carb Calculator", "Grocery Lists", "90-Day Tracking"]),
    (16, "HOME MAINTENANCE LOG & PLANNER", "Monthly Checklists & Repair Logs",
     "Cover16_Home_Maintenance.pdf",
     ["Monthly Checklists", "Repair & Service Logs", "Contractor Contacts", "Seasonal Tasks"]),
    (17, "FISHING LOG BOOK", "Record Every Catch",
     "Cover17_Fishing_Log.pdf",
     ["Catch Records", "Weather & Location Notes", "Bait & Tackle Used", "Personal Best Tracker"]),
    (18, "MY PREGNANCY JOURNAL", "Week by Week",
     "Cover18_Pregnancy_Journal.pdf",
     ["40-Week Guided Prompts", "Appointment Tracker", "Baby Kick Counter", "Birth Plan Pages"]),
    (19, "THE 5-MINUTE JOURNAL FOR MEN", "Daily Gratitude & Reflection",
     "Cover19_Gratitude_Journal_Men.pdf",
     ["Morning & Evening Prompts", "Weekly Goals", "Gratitude Practice", "90-Day Format"]),
    (20, "WITCHY COLORING BOOK", "Magical Illustrations for Adults",
     "Cover20_Witchy_Coloring.pdf",
     ["35+ Mystical Designs", "Potions & Crystals", "Moon Phase Art", "Single-Sided Pages"]),
    (21, "DREAM JOURNAL", "Capture & Interpret Your Dreams",
     "Cover21_Dream_Journal.pdf",
     ["Nightly Dream Records", "Symbol Dictionary", "Lucid Dream Techniques", "Pattern Tracking"]),
    (22, "MONTHLY BUDGET PLANNER", "Take Control of Your Money",
     "Cover22_Budget_Planner.pdf",
     ["Monthly Income/Expense Pages", "Savings Goal Tracker", "Debt Payoff Planner", "12-Month Format"]),
    (23, "MY READING LOG", "A Book Lover's Journal",
     "Cover23_Reading_Log.pdf",
     ["100 Book Entry Pages", "Rating & Review Sections", "Reading Challenge Lists", "TBR Tracker"]),
    (24, "BIRD WATCHING LOG", "& Field Journal",
     "Cover24_Bird_Watching.pdf",
     ["Species Identification Pages", "Location & Habitat Notes", "Seasonal Checklists", "Sketch Pages"]),
    (25, "MINDFULNESS & MEDITATION JOURNAL", "Track Your Inner Journey",
     "Cover25_Meditation_Journal.pdf",
     ["Daily Meditation Log", "Guided Mindfulness Prompts", "Gratitude Sections", "90-Day Journey"]),
    (26, "HOMESCHOOL LESSON PLANNER", "Organize Your Teaching Year",
     "Cover26_Homeschool_Planner.pdf",
     ["Weekly Lesson Plans", "Subject Tracking", "Field Trip Log", "36-Week Format"]),
    (27, "WINE TASTING JOURNAL", "A Connoisseur's Log Book",
     "Cover27_Wine_Journal.pdf",
     ["100 Tasting Entries", "Aroma & Flavor Wheels", "Rating System", "Vineyard Notes"]),
    (28, "THE 90-DAY HABIT TRACKER", "Build Better Habits",
     "Cover28_Habit_Tracker.pdf",
     ["Daily Habit Grid", "Goal Setting Pages", "Progress Charts", "Reflection Prompts"]),
    (29, "CAMPING LOG BOOK", "Record Your Adventures",
     "Cover29_Camping_Log.pdf",
     ["Campsite Reviews", "Gear Checklists", "Trail & Hike Notes", "Weather Records"]),
    (30, "MY FAMILY RECIPE BOOK", "Preserve Your Favorite Recipes",
     "Cover30_Recipe_Book.pdf",
     ["100+ Recipe Entry Pages", "Category Sections", "Conversion Charts", "Family Favorites Index"]),
    (31, "BLOOD SUGAR & FOOD DIARY", "Type 2 Diabetes Daily Tracker",
     "Cover31_Blood_Sugar_Diary.pdf",
     ["4x Daily Glucose Logs", "Meal & Carb Notes", "Medication Tracker", "A1C Records"]),
    (32, "MY DAILY PRAYER JOURNAL", "90 Days of Faith & Gratitude",
     "Cover32_Prayer_Journal.pdf",
     ["Daily Prayer Prompts", "Scripture Reflections", "Gratitude Lists", "Prayer Request Pages"]),
    (33, "CAR MAINTENANCE LOG", "& Service Record",
     "Cover33_Car_Maintenance.pdf",
     ["Oil Change & Service Logs", "Mileage Tracker", "Repair History", "Tire & Brake Records"]),
    (34, "MY ANXIETY WORKBOOK", "Daily Tools for Calmer Days",
     "Cover34_Anxiety_Workbook.pdf",
     ["CBT-Based Exercises", "Thought Records", "Breathing Techniques", "Worry Tracking Pages"]),
    (35, "MY FIRST ACTIVITY BOOK", "For Toddlers Ages 2-4",
     "Cover35_Toddler_Activity.pdf",
     ["Tracing & Coloring", "Shape Recognition", "Simple Mazes", "Fun Learning Activities"]),
    (36, "WEIGHT LOSS TRACKER", "& Fitness Journal",
     "Cover36_Weight_Loss_Tracker.pdf",
     ["Daily Weigh-In Log", "Meal Planning Pages", "Workout Tracker", "Body Measurement Charts"]),
    (37, "BASEBALL & SOFTBALL SCOREBOOK", "30 Game Scoring Sheets",
     "Cover37_Baseball_Scorebook.pdf",
     ["30 Full Game Sheets", "9-Inning Format", "Player Lineup Pages", "Season Statistics"]),
    (38, "OUR LOVE STORY", "A Couples Journal",
     "Cover38_Love_Story.pdf",
     ["How We Met Pages", "Memory Prompts", "Date Night Ideas", "Anniversary Milestones"]),
    (39, "MUSIC PRACTICE LOG", "Track Your Progress",
     "Cover39_Music_Practice.pdf",
     ["Daily Practice Sessions", "Piece/Song Tracker", "Goal Setting Pages", "Performance Notes"]),
    (40, "LARGE PRINT WORD SEARCH", "For Seniors - Volume 1",
     "Cover40_Word_Search.pdf",
     ["75+ Puzzles", "Large Easy-to-Read Print", "Themed Categories", "Full Solutions Included"]),
    (41, "MOM'S SELF-CARE JOURNAL", "Because You Matter Too",
     "Cover41_Mom_Self_Care.pdf",
     ["Daily Self-Care Prompts", "Gratitude & Affirmations", "Me-Time Planning", "Mood Tracker"]),
    (42, "KIDS GRATITUDE JOURNAL", "Ages 5-10",
     "Cover42_Kids_Gratitude.pdf",
     ["Daily Gratitude Prompts", "Drawing Spaces", "Kindness Challenges", "Happy Moments Log"]),
    (43, "MY PERIOD TRACKER", "& Cycle Journal",
     "Cover43_Period_Tracker.pdf",
     ["Monthly Cycle Tracking", "Symptom Log", "Mood & Energy Notes", "12-Month Calendar"]),
    (44, "PRINCESS COLORING BOOK", "For Girls Ages 4-8",
     "Cover44_Princess_Coloring.pdf",
     ["30+ Princess Illustrations", "Castles & Unicorns", "Single-Sided Pages", "Bold Outlines for Kids"]),
    (45, "WOMEN'S FITNESS JOURNAL", "& Workout Tracker",
     "Cover45_Women_Fitness.pdf",
     ["Workout Log Pages", "Body Measurement Charts", "Goal Setting", "Progress Photos"]),
    (46, "HANDWRITING PRACTICE", "For Kids Ages 4-7",
     "Cover46_Handwriting_Practice.pdf",
     ["Letter Tracing A-Z", "Number Practice 1-20", "Word Building", "Sentence Writing"]),
    (47, "BABY'S FIRST YEAR", "A Memory Book",
     "Cover47_Baby_First_Year.pdf",
     ["Monthly Milestones", "First Moments Pages", "Growth Charts", "Photo Memory Sections"]),
    (48, "MY SECRET JOURNAL", "For Girls Ages 9-12",
     "Cover48_Secret_Journal.pdf",
     ["Creative Writing Prompts", "Doodle Pages", "Fun Lists & Quizzes", "Lock-Style Privacy"]),
    (49, "A WOMAN'S PRAYER JOURNAL", "90 Days of Grace",
     "Cover49_Women_Prayer.pdf",
     ["Daily Prayer Prompts", "Scripture Meditation", "Gratitude Pages", "Faith Reflections"]),
    (50, "FUN MATH WORKBOOK", "For Kids Ages 5-7",
     "Cover50_Math_Workbook.pdf",
     ["Addition & Subtraction", "Number Patterns", "Word Problems", "Fun Puzzles & Games"]),
    (51, "AI FOR BEGINNERS", "A Simple Guide for Adults Over 45",
     "Cover51_AI_Beginners.pdf",
     ["Plain Language Explanations", "Real-World Examples", "Step-by-Step Guides", "No Tech Jargon"]),
    (52, "SMARTPHONE MADE EASY", "Large Print Guide for Ages 45+",
     "Cover52_Smartphone_Easy.pdf",
     ["Large Print Instructions", "Screenshot Examples", "Troubleshooting Tips", "App Guides"]),
    (53, "CHATGPT WORKBOOK", "Hands-On Exercises for Adults 45+",
     "Cover53_ChatGPT_Workbook.pdf",
     ["Step-by-Step Exercises", "Real Prompt Examples", "Practice Pages", "Tips & Tricks"]),
    (54, "BRAIN GAMES & MEMORY EXERCISES", "For Adults 45+",
     "Cover54_Brain_Games.pdf",
     ["Memory Challenges", "Logic Puzzles", "Word Games", "Daily Brain Training"]),
    (55, "MY RETIREMENT PLANNER", "Plan Your Best Chapter",
     "Cover55_Retirement_Planner.pdf",
     ["Financial Worksheets", "Bucket List Pages", "Health Planning", "Legacy Notes"]),
    (56, "INTERNET SAFETY FOR SENIORS", "Protect Yourself Online",
     "Cover56_Internet_Safety.pdf",
     ["Scam Recognition Guide", "Password Management", "Privacy Settings", "Safe Browsing Tips"]),
    (57, "AI CREATIVITY WORKBOOK", "Learn to Create with AI Tools",
     "Cover57_AI_Creativity.pdf",
     ["Image Generation Guides", "Writing with AI", "Music & Art Projects", "Hands-On Exercises"]),
    (58, "MY LIFE STORY", "A Guided Memory Journal for Ages 45+",
     "Cover58_Life_Story.pdf",
     ["Childhood Memories", "Career Reflections", "Family History", "Legacy Pages"]),
    (59, "THE AI-POWERED DAILY PLANNER", "Use Technology to Organize Life (45+)",
     "Cover59_AI_Planner.pdf",
     ["AI Productivity Tips", "Daily Schedule Pages", "Goal Setting", "Tech Integration Guides"]),
    (60, "LARGE PRINT TECH DICTIONARY", "200+ Terms Explained Simply",
     "Cover60_Tech_Dictionary.pdf",
     ["200+ Tech Terms", "Plain English Definitions", "Large Print Format", "A-Z Organization"]),
    (61, "HOW TO START AN ETSY SHOP", "Step-by-Step Guide for Beginners",
     "Cover61_Etsy_Shop.pdf",
     ["Shop Setup Guide", "Product Listing Tips", "SEO & Marketing", "Pricing Strategies"]),
    (62, "HOW TO BUDGET YOUR MONEY", "A Simple Guide to Financial Freedom",
     "Cover62_Budget_Money.pdf",
     ["Budget Templates", "Savings Strategies", "Debt Elimination Plan", "Financial Goals"]),
    (63, "HOW TO MEAL PREP", "Save Time, Eat Healthy, Spend Less",
     "Cover63_Meal_Prep.pdf",
     ["Weekly Prep Plans", "Shopping Lists", "Storage Tips", "Quick Recipes"]),
    (64, "HOW TO SELL ON AMAZON", "From Zero to Your First Sale",
     "Cover64_Sell_Amazon.pdf",
     ["Account Setup Guide", "Product Research", "Listing Optimization", "FBA vs FBM Explained"]),
    (65, "HOW TO START A PODCAST", "The Complete Beginner's Guide",
     "Cover65_Start_Podcast.pdf",
     ["Equipment Guide", "Recording Tips", "Editing Basics", "Launch Strategy"]),
    (66, "HOW TO CROCHET", "Learn the Basics Step by Step",
     "Cover66_Crochet.pdf",
     ["Basic Stitch Guide", "10 Beginner Projects", "Pattern Reading", "Illustrated Instructions"]),
    (67, "HOW TO GROW VEGETABLES", "A Beginner's Garden Guide",
     "Cover67_Grow_Vegetables.pdf",
     ["Seed Starting Guide", "Planting Calendar", "Pest Control Tips", "Harvest Instructions"]),
    (68, "HOW TO DECLUTTER YOUR HOME", "Room by Room Minimalist Guide",
     "Cover68_Declutter_Home.pdf",
     ["Room-by-Room Checklists", "30-Day Challenge", "Organization Systems", "Donation Guide"]),
    (69, "HOW TO TRAIN YOUR PUPPY", "Positive Methods That Work",
     "Cover69_Train_Puppy.pdf",
     ["Basic Commands", "House Training Guide", "Socialization Tips", "Problem Solving"]),
    (70, "HOW TO START A YOUTUBE CHANNEL", "Grow from 0 to 1000 Subscribers",
     "Cover70_YouTube_Channel.pdf",
     ["Channel Setup Guide", "Content Strategy", "SEO & Thumbnails", "Monetization Path"]),
]


def get_dimensions(book_num):
    """Return (width, height) for a given book number."""
    if book_num in BOOKS_6x9:
        return (432, 648)
    else:
        return (612, 792)


def create_cover(book_num, title, subtitle, filename, features):
    """Create a single book cover PDF."""
    w, h = get_dimensions(book_num)
    pdf = PDFDoc(w, h)
    pdf.new_page()

    # Margins and layout proportions based on page size
    margin = 20 if w == 432 else 25
    inner_margin = margin + 5

    # Border
    pdf.add_rect(margin, margin, w - 2*margin, h - 2*margin, line_width=2)

    # Top accent band
    band_height = 35 if w == 432 else 45
    band_y = h - margin - band_height - 10
    pdf.add_filled_rect(margin + 10, band_y, w - 2*margin - 20, band_height, gray=0.88)

    # Book number label in accent band
    book_label = f"BOOK {book_num}"
    label_size = 14 if w == 432 else 16
    pdf.add_centered_text(band_y + (band_height - label_size) // 2 + 2, book_label, font='F2', size=label_size, gray=0.3)

    # Main title
    title_y = band_y - 50
    # Determine title font size based on title length and page width
    if w == 432:
        if len(title) > 35:
            title_size = 18
        elif len(title) > 25:
            title_size = 22
        else:
            title_size = 26
    else:
        if len(title) > 35:
            title_size = 22
        elif len(title) > 25:
            title_size = 28
        else:
            title_size = 32

    # Split long titles into two lines
    if len(title) > 30 and w == 432:
        words = title.split()
        mid = len(words) // 2
        line1 = " ".join(words[:mid])
        line2 = " ".join(words[mid:])
        pdf.add_centered_text(title_y, line1, font='F2', size=title_size)
        pdf.add_centered_text(title_y - title_size - 8, line2, font='F2', size=title_size)
        subtitle_y = title_y - 2 * (title_size + 8) - 15
    elif len(title) > 35 and w == 612:
        words = title.split()
        mid = len(words) // 2
        line1 = " ".join(words[:mid])
        line2 = " ".join(words[mid:])
        pdf.add_centered_text(title_y, line1, font='F2', size=title_size)
        pdf.add_centered_text(title_y - title_size - 8, line2, font='F2', size=title_size)
        subtitle_y = title_y - 2 * (title_size + 8) - 15
    else:
        pdf.add_centered_text(title_y, title, font='F2', size=title_size)
        subtitle_y = title_y - title_size - 20

    # Subtitle
    sub_size = 14 if w == 432 else 17
    pdf.add_centered_text(subtitle_y, subtitle, font='F4', size=sub_size, gray=0.2)

    # Decorative line separator
    line_y = subtitle_y - 25
    line_margin = 80 if w == 432 else 120
    pdf.add_line(line_margin, line_y, w - line_margin, line_y, 2, gray=0.4)

    # Features section
    features_start_y = line_y - 40
    feat_size = 11 if w == 432 else 13
    feat_spacing = 22 if w == 432 else 26

    for i, feat in enumerate(features):
        feat_y = features_start_y - i * feat_spacing
        feat_text = f"* {feat}"
        pdf.add_centered_text(feat_y, feat_text, font='F1', size=feat_size, gray=0.15)

    # Author section at bottom
    author_line_y = margin + 70 if w == 432 else margin + 90
    author_line_margin = 120 if w == 432 else 160
    pdf.add_line(author_line_margin, author_line_y, w - author_line_margin, author_line_y, 1, gray=0.5)

    author_y = margin + 40 if w == 432 else margin + 55
    author_size = 16 if w == 432 else 20
    pdf.add_centered_text(author_y, AUTHOR, font='F2', size=author_size)

    output_path = f'/projects/sandbox/CLAUDE/BOOK_COVERS/{filename}'
    pdf.save(output_path)
    return output_path


def main():
    print("Generating 65 book covers (Books 6-70)...")
    print("=" * 50)

    generated = []
    for book_num, title, subtitle, filename, features in BOOK_DATA:
        path = create_cover(book_num, title, subtitle, filename, features)
        dims = get_dimensions(book_num)
        size_label = "6x9" if dims == (432, 648) else "8.5x11"
        print(f"  Book {book_num:2d} ({size_label}): {filename}")
        generated.append(path)

    print("=" * 50)
    print(f"\nTotal covers generated: {len(generated)}")

    # Verify all files exist
    import os
    missing = []
    for path in generated:
        if not os.path.exists(path):
            missing.append(path)

    if missing:
        print(f"\nWARNING: {len(missing)} files missing!")
        for m in missing:
            print(f"  MISSING: {m}")
    else:
        print("All 65 cover PDFs verified successfully!")


if __name__ == '__main__':
    main()
