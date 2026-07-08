from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(550, "VISION BOARD WORKBOOK", 'F2', 20)
pdf.add_centered_text(520, "Design Your Dream Life & Make It Happen", 'F4', 14)
pdf.add_centered_text(400, "Visualize. Plan. Achieve.", 'F5', 13)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: What is a Vision Board
pdf.new_page()
pdf.add_centered_text(750, "WHAT IS A VISION BOARD & WHY IT WORKS", 'F2', 14)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "A vision board is a visual representation of your goals, dreams,",
    "and the life you want to create. It works because:", "",
    "THE SCIENCE:",
    "- Reticular Activating System (RAS): Your brain filters millions",
    "  of data points daily. When you focus on something visually,",
    "  your RAS starts noticing opportunities aligned with those goals.",
    "- Visualization activates the same brain regions as actual",
    "  experience, building neural pathways toward your goals.",
    "- Written goals are 42% more likely to be achieved.", "",
    "HOW TO USE THIS WORKBOOK:",
    "1. Assess where you are NOW in each life area (honestly)",
    "2. Dream about where you WANT to be (no limits!)",
    "3. Set specific goals with action steps",
    "4. Create your physical vision board (images + words)",
    "5. Review daily, take action monthly, adjust quarterly", "",
    "SUPPLIES FOR YOUR VISION BOARD:",
    "- Poster board or cork board",
    "- Magazines, printed images, quotes",
    "- Scissors, glue, tape, markers",
    "- Stickers, washi tape (optional)",
    "- A photo of yourself (put it in the center!)", "",
    "Place it where you'll see it DAILY."
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 4: Life Areas Assessment
pdf.new_page()
pdf.add_centered_text(750, "LIFE AREAS ASSESSMENT", 'F2', 15)
pdf.add_centered_text(733, "Rate each area 1-10 (where you are NOW)", 'F1', 10)
pdf.add_line(60, 725, 552, 725)
y = 700
areas = [
    ("CAREER/BUSINESS", "Job satisfaction, income, growth, purpose"),
    ("HEALTH/FITNESS", "Physical health, energy, nutrition, exercise"),
    ("RELATIONSHIPS", "Partner, family, friendships, community"),
    ("FINANCES", "Income, savings, debt, investments, freedom"),
    ("SPIRITUAL/FAITH", "Connection, peace, purpose, growth"),
    ("FUN/RECREATION", "Hobbies, travel, adventure, play"),
    ("PERSONAL GROWTH", "Learning, skills, mindset, confidence")
]
for area, desc in areas:
    pdf.add_text(60, y, f"{area}:", 'F2', 11)
    y -= 14
    pdf.add_text(70, y, desc, 'F4', 9)
    y -= 14
    pdf.add_text(70, y, "Current rating: ___/10  Desired rating: ___/10", 'F3', 9)
    y -= 14
    pdf.add_text(70, y, "What would make it a 10? ______________________", 'F3', 9)
    y -= 22

# Page 5: Dream Life Visualization
pdf.new_page()
pdf.add_centered_text(750, "DREAM LIFE VISUALIZATION", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Close your eyes. Imagine your IDEAL life 5 years from now.", 
    "Everything went right. Answer these questions:", "",
    "Where do I live? _____________________________",
    "What does my home look like? __________________",
    "_______________________________________________",
    "What do I do for work? ________________________",
    "_______________________________________________",
    "How much do I earn? $__________________________",
    "Who am I with? ________________________________",
    "What does a typical Monday look like? __________",
    "_______________________________________________",
    "_______________________________________________",
    "What does a typical Saturday look like? ________",
    "_______________________________________________",
    "_______________________________________________",
    "How do I FEEL in this life? ___________________",
    "What am I most proud of? _____________________",
    "_______________________________________________",
    "What did I have to do/become to get here?",
    "_______________________________________________",
    "_______________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Pages 6-12: Goal Setting for Each Life Area (7 pages)
goal_areas = [
    "CAREER / BUSINESS",
    "HEALTH / FITNESS",
    "RELATIONSHIPS",
    "FINANCES",
    "SPIRITUAL / FAITH",
    "FUN / RECREATION",
    "PERSONAL GROWTH"
]
for area in goal_areas:
    pdf.new_page()
    pdf.add_centered_text(750, f"GOALS: {area}", 'F2', 14)
    pdf.add_line(60, 738, 552, 738)
    y = 715
    for line in [
        f"1-YEAR GOAL for {area}:",
        "_______________________________________________",
        "_______________________________________________", "",
        "5-YEAR GOAL:",
        "_______________________________________________",
        "_______________________________________________", "",
        "10-YEAR DREAM:",
        "_______________________________________________",
        "_______________________________________________", "",
        "ACTION STEPS (what I need to do):",
        "1. ____________________________________________",
        "2. ____________________________________________",
        "3. ____________________________________________", "",
        "OBSTACLES I might face:",
        "_______________________________________________",
        "How I'll overcome them: _______________________", "",
        "RESOURCES I need (people, money, skills, tools):",
        "_______________________________________________",
        "_______________________________________________", "",
        "Images/words for my vision board for this area:",
        "_______________________________________________"
    ]:
        pdf.add_text(60, y, line, 'F4', 10)
        y -= 15

# Pages 13-15: Monthly Action Planner (3 pages)
for month in range(1, 4):
    pdf.new_page()
    pdf.add_centered_text(750, f"MONTHLY ACTION PLANNER - MONTH {month}", 'F2', 14)
    pdf.add_line(60, 738, 552, 738)
    y = 715
    for line in [
        f"Month: _____________ Focus area: _____________", "",
        "TOP 3 GOALS THIS MONTH:",
        "1. ____________________________________________",
        "   Weekly action: _____________________________",
        "2. ____________________________________________",
        "   Weekly action: _____________________________",
        "3. ____________________________________________",
        "   Weekly action: _____________________________", "",
        "HABITS TO BUILD THIS MONTH:",
        "Morning: ______________________________________",
        "Daily: ________________________________________",
        "Evening: ______________________________________", "",
        "WEEKLY CHECK-IN:",
        "Week 1: On track? Y/N  Adjust: ________________",
        "Week 2: On track? Y/N  Adjust: ________________",
        "Week 3: On track? Y/N  Adjust: ________________",
        "Week 4: On track? Y/N  Adjust: ________________", "",
        "END OF MONTH REFLECTION:",
        "What I accomplished: __________________________",
        "What I'll carry to next month: _________________"
    ]:
        pdf.add_text(60, y, line, 'F4', 10)
        y -= 15

# Page 16: Affirmations Creation
pdf.new_page()
pdf.add_centered_text(750, "AFFIRMATIONS CREATION WORKSHEET", 'F2', 14)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Write affirmations as if your goals are ALREADY achieved:", "",
    "CAREER: 'I am ________________________________'",
    "HEALTH: 'I am ________________________________'",
    "RELATIONSHIPS: 'I am _________________________'",
    "FINANCES: 'I have ____________________________'",
    "SPIRITUAL: 'I am _____________________________'",
    "FUN: 'I regularly ____________________________'",
    "GROWTH: 'I am becoming _______________________'", "",
    "MY POWER AFFIRMATION (put this on your vision board):",
    "_______________________________________________", "",
    "SAY THESE DAILY: Morning (upon waking) and evening (before bed)",
    "Read them out loud. Feel them. Believe them.", "",
    "GRATITUDE PRACTICE:",
    "Today I am grateful for:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "4. ____________________________________________",
    "5. ____________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 17: Accountability + Vision Board Checklist
pdf.new_page()
pdf.add_centered_text(750, "ACCOUNTABILITY & VISION BOARD CHECKLIST", 'F2', 13)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "ACCOUNTABILITY PARTNER AGREEMENT:", "",
    "Partner name: _________________________________",
    "Check-in frequency: Weekly / Biweekly / Monthly",
    "Check-in method: Call / Text / In-person / Video", "",
    "I commit to:",
    "- Sharing my goals honestly",
    "- Reporting progress and setbacks",
    "- Being open to feedback",
    "- Supporting my partner's goals equally", "",
    "Signed: ___________________ Date: _____________", "",
    "VISION BOARD CREATION CHECKLIST:", "",
    "__ Completed life areas assessment",
    "__ Written goals for all 7 areas",
    "__ Created affirmations",
    "__ Collected images for each area",
    "__ Found inspirational quotes/words",
    "__ Included photo of myself",
    "__ Assembled the board",
    "__ Placed it where I'll see it daily",
    "__ Set monthly review dates",
    "__ Told someone about my goals"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Pages 18-21: Quarterly Review (4 pages)
for q in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(750, f"QUARTERLY REVIEW - Q{q}", 'F2', 14)
    pdf.add_line(60, 738, 552, 738)
    y = 715
    for line in [
        f"Quarter {q} dates: ___/___/___ to ___/___/___", "",
        "WINS THIS QUARTER (celebrate them!):",
        "1. ____________________________________________",
        "2. ____________________________________________",
        "3. ____________________________________________", "",
        "PROGRESS BY AREA (rate 1-10 again):",
        "Career: ___  Health: ___  Relationships: ___",
        "Finances: ___  Spiritual: ___  Fun: ___  Growth: ___", "",
        "WHAT WORKED:",
        "_______________________________________________", "",
        "WHAT DIDN'T WORK:",
        "_______________________________________________", "",
        "ADJUSTMENTS FOR NEXT QUARTER:",
        "_______________________________________________",
        "_______________________________________________", "",
        "GOALS FOR NEXT QUARTER:",
        "1. ____________________________________________",
        "2. ____________________________________________",
        "3. ____________________________________________"
    ]:
        pdf.add_text(60, y, line, 'F4', 10)
        y -= 16

# Page 22: Year-End Reflection
pdf.new_page()
pdf.add_centered_text(750, "YEAR-END REFLECTION", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Look back at the year. Honor your journey.", "",
    "BIGGEST ACCOMPLISHMENT:",
    "_______________________________________________", "",
    "BIGGEST LESSON LEARNED:",
    "_______________________________________________", "",
    "MOST UNEXPECTED BLESSING:",
    "_______________________________________________", "",
    "WHAT I'M MOST PROUD OF:",
    "_______________________________________________", "",
    "HOW I GREW AS A PERSON:",
    "_______________________________________________", "",
    "GOALS I ACHIEVED FROM MY VISION BOARD:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________", "",
    "GOALS TO CARRY INTO NEXT YEAR:",
    "1. ____________________________________________",
    "2. ____________________________________________", "",
    "NOTE TO FUTURE SELF:",
    "_______________________________________________",
    "_______________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 23: My Word of the Year
pdf.new_page()
pdf.add_centered_text(600, "MY WORD OF THE YEAR", 'F2', 18)
pdf.add_line(100, 580, 512, 580)
pdf.add_centered_text(520, "Choose ONE word that captures your intention for the year:", 'F4', 11)
pdf.add_centered_text(450, "____________________________", 'F2', 22)
y = 400
for line in [
    "Why I chose this word:", "",
    "_______________________________________________",
    "_______________________________________________", "",
    "What it means to me:", "",
    "_______________________________________________",
    "_______________________________________________", "",
    "How I will live this word daily:", "",
    "_______________________________________________",
    "_______________________________________________", "",
    "Put this word on your vision board in BIG letters.", "",
    "WORD IDEAS: Growth, Brave, Joy, Peace, Create, Focus,",
    "Abundance, Freedom, Believe, Become, Bold, Heal, Shine"
]:
    pdf.add_text(60, y, line, 'F4', 11)
    y -= 18

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book120_Vision_Board_Workbook.pdf')
print("Book120_Vision_Board_Workbook.pdf created successfully!")
