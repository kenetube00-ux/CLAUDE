"""Book 96: Charlotte Mason Homeschool Planner"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.07)
    pdf.add_centered_text(520, "CHARLOTTE MASON", 'F5', 28, 1)
    pdf.add_centered_text(480, "HOMESCHOOL PLANNER", 'F5', 28, 1)
    pdf.add_centered_text(430, "Nature Study, Living Books & Habits", 'F4', 16, 0.85)
    pdf.add_centered_text(380, "Short Lessons | Narration | Nature Journals", 'F1', 12, 0.75)
    pdf.add_centered_text(358, "Composer Study | Art | Handicrafts", 'F1', 12, 0.75)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "Charlotte Mason Homeschool Planner", 'F5', 14)
    pdf.add_centered_text(478, "Nature Study, Living Books & Habits", 'F4', 11)
    pdf.add_centered_text(445, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(425, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(395, "Inspired by the educational philosophy of Charlotte Mason.", 'F4', 9)


    # Page 1: Charlotte Mason Philosophy Overview
    pdf.new_page()
    pdf.add_centered_text(740, "CHARLOTTE MASON PHILOSOPHY OVERVIEW", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    text = [
        "Charlotte Mason (1842-1923) believed children are born persons, not",
        "blank slates. Education is the science of relations - connecting",
        "children to as many living ideas and experiences as possible.",
        "",
        "KEY PRINCIPLES:",
        "",
        "1. SHORT LESSONS: 10-20 minutes per subject (young children).",
        "   Full attention for a short time beats distracted half-hours.",
        "",
        "2. LIVING BOOKS: Real literature, not dry textbooks.",
        "   Books written by authors passionate about their subject.",
        "",
        "3. NARRATION: The child tells back what they learned in their own words.",
        "   This replaces worksheets and tests for retention.",
        "",
        "4. NATURE STUDY: Weekly outdoor time observing God's creation.",
        "   Keep a nature journal with sketches and observations.",
        "",
        "5. HABIT TRAINING: One habit at a time, practiced for 4-6 weeks.",
        "   Character formation is as important as academics.",
        "",
        "6. THE FEAST: Spread a wide table of subjects - don't narrow too early.",
        "   Include: math, reading, nature, art, music, poetry, handicrafts,",
        "   history, geography, languages, and Scripture.",
        "",
        "7. ATMOSPHERE: The home environment IS the curriculum.",
        "   Children absorb what surrounds them.",
    ]
    for line in text:
        pdf.add_text(72, y, line, 'F4', 10)
        y -= 17

    # Pages 2-4: Term Planning Pages (3 terms)
    for term in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(740, f"TERM {term} PLANNING", 'F2', 16)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        y = 710
        pdf.add_text(72, y, f"Term {term} Dates: _____________ to _____________", 'F1', 10)
        y -= 20
        pdf.add_text(72, y, "Weeks in term: _______", 'F1', 10)
        y -= 25
        subjects = [
            "Bible/Scripture", "Mathematics", "Language Arts (Reading/Writing)",
            "History (Living Books)", "Science/Nature Study",
            "Geography", "Foreign Language", "Composer Study",
            "Artist/Picture Study", "Poetry", "Handicraft",
            "Physical Education",
        ]
        pdf.add_text(72, y, "Subject", 'F2', 9)
        pdf.add_text(220, y, "Book/Resource", 'F2', 9)
        pdf.add_text(420, y, "Pages/Goals", 'F2', 9)
        y -= 15
        for s in subjects:
            pdf.add_text(72, y, s, 'F1', 9)
            pdf.add_line(220, y - 2, 405, y - 2, 0.5, 0.5)
            pdf.add_line(420, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 22
        y -= 10
        pdf.add_text(72, y, "Habit to focus on this term: ________________________________", 'F2', 10)
        y -= 20
        pdf.add_text(72, y, "Nature study focus: ________________________________________", 'F2', 10)
        y -= 20
        pdf.add_text(72, y, "Composer this term: ________________ Artist: ________________", 'F2', 10)


    # Page 5: Daily Schedule Template
    pdf.new_page()
    pdf.add_centered_text(740, "DAILY SCHEDULE TEMPLATE (SHORT LESSONS)", 'F2', 14)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 710
    pdf.add_text(72, y, "Charlotte Mason recommended SHORT, focused lessons. Adjust times to your family.", 'F4', 9)
    y -= 20
    schedule = [
        ("8:00 - 8:15", "Morning Time (Bible, hymn, prayer)", "15 min"),
        ("8:15 - 8:30", "Mathematics", "15 min"),
        ("8:30 - 8:45", "Handwriting / Copywork", "15 min"),
        ("8:45 - 9:00", "BREAK (free play, snack)", "15 min"),
        ("9:00 - 9:20", "Reading Lesson / Literature", "20 min"),
        ("9:20 - 9:40", "History (living book + narration)", "20 min"),
        ("9:40 - 9:55", "BREAK (outdoor play)", "15 min"),
        ("9:55 - 10:10", "Science / Nature Study reading", "15 min"),
        ("10:10 - 10:25", "Geography / Map Work", "15 min"),
        ("10:25 - 10:40", "Foreign Language", "15 min"),
        ("10:40 - 11:00", "BREAK", "20 min"),
        ("11:00 - 11:15", "Art / Picture Study OR Composer Study", "15 min"),
        ("11:15 - 11:30", "Poetry / Shakespeare", "15 min"),
        ("11:30 - 12:00", "Handicraft OR Nature Walk", "30 min"),
        ("12:00", "DONE! Free afternoon for play and exploration.", ""),
    ]
    pdf.add_text(72, y, "Time", 'F2', 9)
    pdf.add_text(160, y, "Subject", 'F2', 9)
    pdf.add_text(450, y, "Duration", 'F2', 9)
    y -= 14
    for time, subject, dur in schedule:
        pdf.add_text(72, y, time, 'F3', 8)
        pdf.add_text(160, y, subject, 'F1', 9)
        pdf.add_text(450, y, dur, 'F1', 9)
        y -= 18
    y -= 15
    pdf.add_text(72, y, "Notes: Total formal instruction ~3 hours. Afternoons are FREE.", 'F2', 9)
    y -= 15
    pdf.add_text(72, y, "Adjust lesson lengths by age: 6-9yrs=10-15min, 10-12=15-20min, 13+=20-30min", 'F4', 9)

    # Pages 6-13: Nature Study Journal Pages (8 pages)
    for pg in range(1, 9):
        pdf.new_page()
        pdf.add_centered_text(750, f"NATURE STUDY JOURNAL - Entry {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 720
        pdf.add_text(72, y, "Date: ________________  Location: _________________________________", 'F1', 10)
        y -= 20
        pdf.add_text(72, y, "Weather: ______________  Temperature: _________  Season: ___________", 'F1', 10)
        y -= 20
        pdf.add_text(72, y, "Time spent outdoors: ___________ Companions: _____________________", 'F1', 10)
        y -= 25
        pdf.add_text(72, y, "WHAT I OBSERVED TODAY:", 'F2', 11)
        y -= 18
        for i in range(6):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18
        y -= 10
        pdf.add_text(72, y, "SKETCH AREA (draw what you observed):", 'F2', 11)
        y -= 10
        pdf.add_rect(72, y - 220, 468, 220, 0.5, 0.4)
        y -= 235
        pdf.add_text(72, y, "Species/Object identified: ______________________________________", 'F1', 9)
        y -= 16
        pdf.add_text(72, y, "Questions I want to research: ____________________________________", 'F1', 9)
        y -= 16
        pdf.add_text(72, y, "Connection to previous observations: _____________________________", 'F1', 9)


    # Page 14: Living Books Reading List Tracker
    pdf.new_page()
    pdf.add_centered_text(740, "LIVING BOOKS READING LIST TRACKER", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 710
    pdf.add_text(72, y, "Title", 'F2', 9)
    pdf.add_text(250, y, "Author", 'F2', 9)
    pdf.add_text(380, y, "Subject", 'F2', 9)
    pdf.add_text(480, y, "Completed", 'F2', 9)
    y -= 14
    for i in range(28):
        pdf.add_line(72, y, 240, y, 0.5, 0.5)
        pdf.add_line(250, y, 370, y, 0.5, 0.5)
        pdf.add_line(380, y, 470, y, 0.5, 0.5)
        pdf.add_rect(480, y - 4, 8, 8, 0.5, 0.3)
        y -= 20

    # Pages 15-19: Narration Record Pages (5 pages)
    for pg in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(740, f"NARRATION RECORD - Page {pg}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        y = 710
        for entry in range(2):
            pdf.add_text(72, y, "Date: __________  Book Title: ________________________________", 'F1', 10)
            y -= 18
            pdf.add_text(72, y, "Pages/Chapter: __________  Child: _____________________________", 'F1', 10)
            y -= 20
            pdf.add_text(72, y, "CHILD'S NARRATION (in their own words):", 'F2', 10)
            y -= 16
            for i in range(10):
                pdf.add_line(72, y, 540, y, 0.5, 0.5)
                y -= 16
            y -= 10
            pdf.add_text(72, y, "Vocabulary/ideas child used well:", 'F1', 9)
            pdf.add_line(270, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 18
            pdf.add_text(72, y, "Areas to develop:", 'F1', 9)
            pdf.add_line(180, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 28

    # Pages 20-21: Habit Training Tracker (12 months = 2 pages)
    for pg in range(1, 3):
        pdf.new_page()
        pdf.add_centered_text(740, f"HABIT TRAINING TRACKER - Page {pg}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        y = 710
        start_month = (pg - 1) * 6 + 1
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        for m in range(6):
            mo = months[start_month - 1 + m]
            pdf.add_text(72, y, f"{mo}:", 'F2', 10)
            y -= 16
            pdf.add_text(72, y, "Habit focus: _____________________________________", 'F1', 9)
            y -= 16
            pdf.add_text(72, y, "Week 1: [ ] [ ] [ ] [ ] [ ]  Week 2: [ ] [ ] [ ] [ ] [ ]", 'F3', 8)
            y -= 14
            pdf.add_text(72, y, "Week 3: [ ] [ ] [ ] [ ] [ ]  Week 4: [ ] [ ] [ ] [ ] [ ]", 'F3', 8)
            y -= 14
            pdf.add_text(72, y, "Established? [ ] Yes [ ] No   Notes: _________________", 'F1', 8)
            y -= 25


    # Page 22: Composer/Artist Study Log
    pdf.new_page()
    pdf.add_centered_text(740, "COMPOSER & ARTIST STUDY LOG", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 710
    pdf.add_text(72, y, "COMPOSER STUDY (listen to one composer per term):", 'F2', 10)
    y -= 18
    for term in range(1, 4):
        pdf.add_text(72, y, f"Term {term} Composer: _________________ Era: _______________", 'F1', 9)
        y -= 16
        pdf.add_text(72, y, "Pieces listened to: ________________________________________", 'F1', 9)
        y -= 16
        pdf.add_text(72, y, "Child's response: __________________________________________", 'F1', 9)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "ARTIST/PICTURE STUDY (study one artist per term):", 'F2', 10)
    y -= 18
    for term in range(1, 4):
        pdf.add_text(72, y, f"Term {term} Artist: ____________________ Style: ______________", 'F1', 9)
        y -= 16
        pdf.add_text(72, y, "Works studied: _____________________________________________", 'F1', 9)
        y -= 16
        pdf.add_text(72, y, "Child's observations: ______________________________________", 'F1', 9)
        y -= 22

    # Page 23: Handicraft Progress
    pdf.new_page()
    pdf.add_centered_text(740, "HANDICRAFT PROGRESS LOG", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 710
    pdf.add_text(72, y, "Charlotte Mason valued working with hands. Track handicraft skills:", 'F4', 9)
    y -= 20
    pdf.add_text(72, y, "Craft/Skill", 'F2', 9)
    pdf.add_text(220, y, "Started", 'F2', 9)
    pdf.add_text(300, y, "Current Level", 'F2', 9)
    pdf.add_text(430, y, "Next Goal", 'F2', 9)
    y -= 14
    crafts = [
        "Knitting", "Sewing/Embroidery", "Woodworking", "Weaving",
        "Pottery/Clay", "Cooking/Baking", "Gardening", "Calligraphy",
        "Origami/Paper", "Drawing/Painting", "Crochet",
        "Other: _____________",
    ]
    for c in crafts:
        pdf.add_text(72, y, c, 'F1', 9)
        pdf.add_line(220, y - 2, 285, y - 2, 0.5, 0.5)
        pdf.add_line(300, y - 2, 415, y - 2, 0.5, 0.5)
        pdf.add_line(430, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "Current project: _______________________________________________", 'F1', 10)
    y -= 18
    pdf.add_text(72, y, "Materials needed: ______________________________________________", 'F1', 10)

    # Page 24: Poetry & Shakespeare Log
    pdf.new_page()
    pdf.add_centered_text(740, "POETRY & SHAKESPEARE LOG", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 710
    pdf.add_text(72, y, "POETRY MEMORIZATION:", 'F2', 11)
    y -= 18
    pdf.add_text(72, y, "Poem Title", 'F2', 9)
    pdf.add_text(250, y, "Poet", 'F2', 9)
    pdf.add_text(380, y, "Memorized?", 'F2', 9)
    pdf.add_text(470, y, "Recited?", 'F2', 9)
    y -= 14
    for i in range(10):
        pdf.add_line(72, y, 240, y, 0.5, 0.5)
        pdf.add_line(250, y, 370, y, 0.5, 0.5)
        pdf.add_rect(380, y - 4, 8, 8, 0.5, 0.3)
        pdf.add_rect(470, y - 4, 8, 8, 0.5, 0.3)
        y -= 20
    y -= 10
    pdf.add_text(72, y, "SHAKESPEARE (one play per term):", 'F2', 11)
    y -= 18
    for term in range(1, 4):
        pdf.add_text(72, y, f"Term {term}: Play: ______________________ Completed: [ ]", 'F1', 9)
        y -= 16
        pdf.add_text(72, y, "Method (read aloud / acted / Lamb's Tales): ___________________", 'F1', 9)
        y -= 16
        pdf.add_text(72, y, "Child's favorite part: ________________________________________", 'F1', 9)
        y -= 22

    # Pages 25-27: Picture Study Pages (3 pages)
    for pg in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(740, f"PICTURE STUDY - Session {pg}", 'F2', 14)
        pdf.add_line(72, 730, 540, 730, 1, 0.3)
        y = 710
        pdf.add_text(72, y, "Artist: _________________________ Title: ______________________", 'F1', 10)
        y -= 20
        pdf.add_text(72, y, "Date: __________  Medium: ________________ Year: ____________", 'F1', 10)
        y -= 25
        pdf.add_text(72, y, "FIRST IMPRESSION (what do you notice first?):", 'F2', 10)
        y -= 16
        for i in range(3):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 8
        pdf.add_text(72, y, "DETAILS (look closely - colors, light, expressions, objects):", 'F2', 10)
        y -= 16
        for i in range(4):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 8
        pdf.add_text(72, y, "TELL THE STORY (what do you think is happening?):", 'F2', 10)
        y -= 16
        for i in range(4):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
        y -= 8
        pdf.add_text(72, y, "SKETCH FROM MEMORY (close the picture, draw what you remember):", 'F2', 10)
        y -= 10
        pdf.add_rect(72, y - 150, 468, 150, 0.5, 0.4)


    # Page 28: Foreign Language Progress
    pdf.new_page()
    pdf.add_centered_text(740, "FOREIGN LANGUAGE PROGRESS", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 710
    pdf.add_text(72, y, "Language: ______________________  Method: ______________________", 'F1', 10)
    y -= 20
    pdf.add_text(72, y, "Resource/Curriculum: ____________________________________________", 'F1', 10)
    y -= 25
    pdf.add_text(72, y, "VOCABULARY LEARNED THIS TERM:", 'F2', 10)
    y -= 16
    for i in range(12):
        pdf.add_text(72, y, "Word/Phrase:", 'F1', 8)
        pdf.add_line(150, y - 2, 300, y - 2, 0.5, 0.5)
        pdf.add_text(310, y, "Meaning:", 'F1', 8)
        pdf.add_line(360, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18
    y -= 10
    pdf.add_text(72, y, "Songs/poems in target language:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16
    pdf.add_text(72, y, "Conversational phrases mastered:", 'F2', 10)
    y -= 16
    for i in range(3):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 16

    # Page 29: Scripture Memory
    pdf.new_page()
    pdf.add_centered_text(740, "SCRIPTURE MEMORY TRACKER", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 710
    pdf.add_text(72, y, "Reference", 'F2', 9)
    pdf.add_text(200, y, "First words", 'F2', 9)
    pdf.add_text(400, y, "Memorized?", 'F2', 9)
    pdf.add_text(490, y, "Review", 'F2', 9)
    y -= 14
    for i in range(24):
        pdf.add_line(72, y, 190, y, 0.5, 0.5)
        pdf.add_line(200, y, 390, y, 0.5, 0.5)
        pdf.add_rect(400, y - 4, 8, 8, 0.5, 0.3)
        pdf.add_rect(490, y - 4, 8, 8, 0.5, 0.3)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "Family memory verse this month: _________________________________", 'F2', 9)

    # Page 30: Year-End Evaluation
    pdf.new_page()
    pdf.add_centered_text(740, "YEAR-END EVALUATION", 'F2', 16)
    pdf.add_line(72, 730, 540, 730, 1, 0.3)
    y = 705
    fields = [
        ("Greatest academic growth this year:", 3),
        ("Character growth observed:", 3),
        ("Favorite books we read:", 3),
        ("Most successful subject/approach:", 2),
        ("What didn't work well (change next year):", 3),
        ("Nature study highlights:", 2),
        ("Habits established:", 3),
        ("Goals for next year:", 3),
        ("My child's reflections on the year:", 3),
    ]
    for label, lines in fields:
        pdf.add_text(72, y, label, 'F2', 10)
        y -= 14
        for _ in range(lines):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 14
        y -= 8

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book96_Charlotte_Mason_Planner.pdf')
    print("Book96_Charlotte_Mason_Planner.pdf created successfully!")

if __name__ == "__main__":
    create_book()
