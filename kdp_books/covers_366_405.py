import sys, os
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

os.makedirs('/projects/sandbox/CLAUDE/BOOK_COVERS', exist_ok=True)

# Cover data: (book_num, filename, title, subtitle, features, accent_gray)
covers = [
    # Books 366-385 (first batch)
    (366, "Biblical_Marriage_Foundation", "The Biblical\nFoundation of Marriage", "God's Blueprint for an Unbreakable Union",
     ["15 Scripture-Rich Chapters", "Discussion Questions", "Prayer Prompts", "Weekly Action Steps", "Couples Devotional"], 0.12),
    (367, "Marriage_Communication", "Holy Words,\nHappy Marriage", "Biblical Communication for Couples",
     ["12 Communication Chapters", "Conflict Resolution Tools", "Daily Dialogue Rituals", "Healing Verbal Wounds", "Scripture Foundations"], 0.22),
    (368, "Marriage_Intimacy", "Sacred Intimacy", "God's Design for Physical & Emotional Oneness",
     ["Song of Solomon Study", "Overcoming Shame", "Rekindling the Flame", "Intimacy After Children", "30-Day Challenge"], 0.18),
    (369, "Marriage_Forgiveness", "The Forgiving\nMarriage", "Freedom Through Biblical Reconciliation",
     ["70x7 Principle", "Forgiving Betrayal", "Breaking Bitterness", "Boundary Setting", "Generational Healing"], 0.28),
    (370, "Marriage_Prayer", "The Praying Couple", "Transforming Your Marriage Through United Prayer",
     ["Daily Prayer Models", "Warfare Prayer Guide", "Fasting Together", "40-Day Prayer Journey", "Prayer Altar Guide"], 0.15),
    (371, "Marriage_Roles", "His and Hers:\nBiblical Roles", "Understanding Headship, Submission & Partnership",
     ["Biblical Headship Defined", "Submission as Strength", "Mutual Submission", "Decision-Making", "Proverbs 31 Study"], 0.32),
    (372, "Marriage_Money", "Kingdom Finances\nfor Couples", "Biblical Money Management in Marriage",
     ["Tithing Together", "Debt Elimination Plan", "Budget Templates", "Generosity Lifestyle", "Legacy Planning"], 0.25),
    (373, "Marriage_Parenting", "Parenting as\nPartners", "Raising Godly Children in a United Marriage",
     ["United Front Strategy", "Discipline Agreement", "Faith at Home Guide", "Empty Nest Prep", "Priority Order"], 0.20),
    (374, "Marriage_Healing", "Healing Broken\nMarriages", "Restoration Through God's Redemptive Power",
     ["Hope for the Hopeless", "Addiction Recovery", "Abuse Healing", "Trust Rebuilding", "Professional Help Guide"], 0.35),
    (375, "Marriage_Seasons", "For Every Season", "Navigating Life's Changes as One",
     ["Honeymoon to Golden Years", "Illness & Suffering", "Financial Storms", "Career Transitions", "Gratitude Practices"], 0.30),
    (376, "Marriage_Spiritual_Warfare", "Battle Ready\nMarriage", "Spiritual Warfare for Couples",
     ["Full Armor of God", "Satan's Schemes Exposed", "Breaking Strongholds", "Worship as Weapon", "Standing Firm Guide"], 0.14),
    (377, "Marriage_Legacy", "A Marriage\nThat Lasts", "Building a Generational Legacy of Faith & Love",
     ["Legacy Blueprint", "Breaking Curses", "Family Traditions", "Mentoring Couples", "50-Year Vision"], 0.38),
    (378, "Marriage_Love_Languages", "Speaking Love\nFluently", "Discovering Your Spouse's Heart Language",
     ["5 Love Languages + Scripture", "Language Assessment", "When Languages Clash", "Seasonal Changes", "Children's Languages"], 0.23),
    (379, "Marriage_Boundaries", "Holy Boundaries", "Protecting Your Marriage with Biblical Wisdom",
     ["In-Law Boundaries", "Opposite Sex Boundaries", "Technology Limits", "Work-Life Balance", "Saying No Guide"], 0.27),
    (380, "Marriage_Date_Nights", "52 Dates\nwith Purpose", "A Year of Intentional Connection",
     ["52 Creative Dates", "Budget-Friendly Ideas", "Spiritual Dates", "Adventure Dates", "At-Home Dates"], 0.19),
    (381, "Marriage_Newlywed", "The First Year", "A Biblical Guide for Newlywed Couples",
     ["Expectation Management", "Money Conversations", "In-Law Navigation", "Intimacy Year One", "Foundation Setting"], 0.33),
    (382, "Marriage_Devotional", "Together With God", "90-Day Devotional for Christian Couples",
     ["90 Daily Readings", "Scripture & Prayer", "Discussion Prompts", "Couples Exercises", "Covenant Renewal"], 0.16),
    (383, "Marriage_Mens_Guide", "Man of the House", "A Biblical Guide for Husbands Who Lead Well",
     ["Biblical Manhood Defined", "Leading Without Dominating", "Emotional Availability", "Romance Guide", "Accountability"], 0.40),
    (384, "Marriage_Womens_Guide", "The Godly Wife", "A Biblical Guide for Women Who Thrive in Marriage",
     ["God-Given Influence", "Respect Language", "Strength + Submission", "Praying for Husband", "Titus 2 Mentoring"], 0.26),
    (385, "Marriage_Restoration", "Miracles in\nMarriage", "True Stories of God's Restoration Power",
     ["Real Couple Testimonies", "Addiction to Freedom", "Infidelity Survival", "Divorce to Renewal", "Hope for You"], 0.36),
    
    # Books 386-405 (second batch)
    (386, "Marriage_Workbook_Couples", "The Biblical\nMarriage Workbook", "12-Week Interactive Study for Couples",
     ["12-Week Structure", "Guided Exercises", "Assessment Tools", "Couples Activities", "Progress Tracking"], 0.13),
    (387, "Marriage_After_Betrayal", "After the\nBetrayal", "Biblical Healing for Shattered Marriages",
     ["Crisis First 30 Days", "Full Disclosure Guide", "Trust Rebuilding Steps", "Trigger Management", "Redemption Story"], 0.34),
    (388, "Marriage_Empty_Nest", "Love After the\nKids Leave", "Rediscovering Marriage in the Empty Nest",
     ["Identity Rediscovery", "Dating Again Tips", "New Dreams Together", "Grandparenting Balance", "Renewed Intimacy"], 0.24),
    (389, "Marriage_Blended_Family", "Blending\nwith Grace", "Biblical Wisdom for Stepfamily Marriages",
     ["Stepfamily Challenges", "Co-Parenting Biblically", "Loyalty Conflicts", "New Traditions", "Redeemed Family"], 0.29),
    (390, "Marriage_Long_Distance", "Faithful\nfrom Afar", "Keeping Marriage Strong Through Distance",
     ["Military Marriage Guide", "Technology Connection", "Guarding Temptation", "Reunion Preparation", "Children & Distance"], 0.21),
    (391, "Marriage_Intercultural", "Different\nBackgrounds\nOne Faith", "Biblical Marriage Across Cultures",
     ["Scripture on Race", "Cultural Celebrations", "Biracial Children", "Family Disapproval", "Kingdom Statement"], 0.17),
    (392, "Marriage_Mental_Health", "When Your Spouse\nStruggles", "Supporting a Partner Through Mental Health",
     ["Depression & Marriage", "Anxiety Impact", "PTSD Support", "Medication + Faith", "Caregiver Self-Care"], 0.37),
    (393, "Marriage_Ministry_Life", "Ministry\nMarriage", "Surviving & Thriving as a Couple in Ministry",
     ["Ministry Pressures", "Burnout Prevention", "Fishbowl Living", "PK Parenting", "Sabbath Rest"], 0.31),
    (394, "Marriage_Finances_Crisis", "Financial Storm\nTogether", "Navigating Job Loss & Debt in Marriage",
     ["Income Loss Survival", "Emergency Budget", "Blame-Free Zone", "Creative Income", "Faith & Finances"], 0.42),
    (395, "Marriage_Chronic_Illness", "In Sickness\nand In Health", "Marriage When One Partner Has Chronic Illness",
     ["Diagnosis Day", "Caregiver + Spouse", "Intimacy Changes", "Financial Impact", "Joy in Suffering"], 0.39),
    (396, "Marriage_Devotional_Morning", "Morning by\nMorning Together", "A 90-Day Sunrise Devotional for Couples",
     ["90 Morning Readings", "Scripture Focus", "Daily Prayer", "Couples Discussion", "Gratitude Practice"], 0.15),
    (397, "Marriage_Bible_Study_Genesis", "In the Beginning:\nMarriage", "A Book-of-Genesis Study for Couples",
     ["12 Genesis Passages", "Marriage Origins", "Couple Case Studies", "Application Questions", "Memory Verses"], 0.20),
    (398, "Marriage_Conflict_Workbook", "Fight Fair,\nLove Deep", "A Biblical Conflict Resolution Workbook",
     ["Conflict Style Assessment", "Cool-Down Protocol", "Repair Attempts", "Money Fights Guide", "Closeness After Conflict"], 0.25),
    (399, "Marriage_Sexual_Intimacy", "Holy Fire", "God's Design for Passionate Intimacy in Marriage",
     ["God Created Passion", "Overcoming Shame", "Desire Differences", "Pornography Freedom", "Lifelong Flame"], 0.18),
    (400, "Marriage_Anger_Management", "Taming the\nFire Within", "Biblical Anger Management for Couples",
     ["Anger Triggers Map", "Righteous vs Sinful", "Self-Control Fruit", "Repair After Rage", "Gentle Answer Guide"], 0.33),
    (401, "Marriage_Second_Marriage", "Love Again", "God's Grace for Second Marriages",
     ["Scripture on Remarriage", "Healing First Marriage", "Baggage Inventory", "New Patterns", "Chapter Two Story"], 0.28),
    (402, "Marriage_Addiction_Recovery", "Free Together", "Biblical Marriage Recovery from Addiction",
     ["Addiction Understanding", "Codependency Help", "Intervention Guide", "Relapse Response", "Restored Marriage"], 0.36),
    (403, "Marriage_Premarital_Guide", "Before I Do", "Biblical Premarital Preparation for Engaged Couples",
     ["Readiness Assessment", "Non-Negotiables Talk", "Money Before Marriage", "Intimacy Expectations", "First Year Plan"], 0.14),
    (404, "Marriage_Anniversary_Renewal", "Renewing\nYour Vows", "A Biblical Covenant Renewal Guide",
     ["Why Renewal Matters", "Decade Reflections", "New Vow Writing", "Ceremony Planning", "Letters to Each Other"], 0.22),
    (405, "Marriage_Daily_Prayers", "365 Prayers for\nYour Marriage", "A Daily Prayer Guide for Couples",
     ["365 Daily Prayers", "Monthly Themes", "Scripture-Based", "Seasonal Prayers", "Warfare Prayers"], 0.16),
]

def create_cover(book_num, filename, title, subtitle, features, accent_gray):
    """Create a professional KDP cover page"""
    pdf = PDFDoc(width=432, height=648)  # 6x9 cover
    pdf.new_page()
    
    # BACKGROUND ACCENT BAND (top)
    pdf.add_filled_rect(0, 480, 432, 168, gray=accent_gray)
    
    # DECORATIVE BORDER
    pdf.add_rect(12, 12, 408, 624, line_width=2, gray=0.3)
    pdf.add_rect(18, 18, 396, 612, line_width=0.5, gray=0.5)
    
    # INNER LINE (section separator)
    pdf.add_line(30, 475, 402, 475, width=1.5, gray=0.4)
    
    # TITLE
    title_lines = title.split('\n')
    title_y_start = 590 if len(title_lines) <= 2 else 610
    for i, line in enumerate(title_lines):
        y_pos = title_y_start - (i * 36)
        if accent_gray < 0.30:
            pdf.add_centered_text(y_pos, line, font='F2', size=26, gray=0.95)
        else:
            pdf.add_centered_text(y_pos, line, font='F2', size=26, gray=0.0)
    
    # SUBTITLE
    sub_y = 490
    if accent_gray < 0.30:
        pdf.add_centered_text(sub_y, subtitle, font='F4', size=12, gray=0.85)
    else:
        pdf.add_centered_text(sub_y, subtitle, font='F4', size=12, gray=0.1)
    
    # DECORATIVE DIVIDER
    pdf.add_line(140, 458, 292, 458, width=1, gray=0.4)
    pdf.add_filled_rect(206, 454, 20, 8, gray=0.4)
    
    # FEATURES
    pdf.add_centered_text(433, "What's Inside:", font='F2', size=11, gray=0.2)
    for i, feature in enumerate(features):
        y = 410 - (i * 26)
        pdf.add_text(60, y, ">>", font='F2', size=10, gray=accent_gray)
        pdf.add_text(82, y, feature, font='F1', size=11, gray=0.15)
    
    # BOTTOM ACCENT BAND
    pdf.add_filled_rect(0, 40, 432, 55, gray=accent_gray)
    
    # AUTHOR NAME
    if accent_gray < 0.30:
        pdf.add_centered_text(60, "DANIEL TESFAMARIAM", font='F2', size=14, gray=0.95)
    else:
        pdf.add_centered_text(60, "DANIEL TESFAMARIAM", font='F2', size=14, gray=0.0)
    
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
    
    output_path = f"/projects/sandbox/CLAUDE/BOOK_COVERS/Cover{book_num}_{filename}.pdf"
    pdf.save(output_path)
    return output_path

# Generate all 40 covers
print("=" * 70)
print("GENERATING COVERS FOR BOOKS 366-405 (Biblical Marriage Series)")
print("=" * 70)

for cover_data in covers:
    path = create_cover(*cover_data)
    size = os.path.getsize(path)
    print(f"  Cover {cover_data[0]}: {cover_data[2].split(chr(10))[0][:35]:<37} ({size:,} bytes)")

print(f"\n{'=' * 70}")
print(f"ALL {len(covers)} COVERS CREATED SUCCESSFULLY!")
print("=" * 70)
