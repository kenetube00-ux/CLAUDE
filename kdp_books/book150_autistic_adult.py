"""Book 150: Late Diagnosed - A Self-Discovery Workbook for Autistic Adults"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "LATE DIAGNOSED", 'F2', 24, 0)
    doc.add_centered_text(395, "A Self-Discovery Workbook", 'F4', 15, 0.2)
    doc.add_centered_text(370, "for Autistic Adults", 'F4', 15, 0.2)
    doc.add_centered_text(300, "You're not broken. You're autistic.", 'F4', 12, 0.3)
    doc.add_centered_text(280, "And that's a beautiful thing to discover.", 'F4', 12, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    doc.new_page()
    doc.add_centered_text(500, "LATE DIAGNOSED", 'F2', 14, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)

    # Page 3: Welcome
    doc.new_page()
    doc.add_centered_text(590, "WELCOME TO YOUR NEUROTYPE", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "If you were diagnosed as an adult (or suspect you're autistic),", 'F1', 10, 0.2)
    doc.add_text(50, 538, "you may be feeling a mix of:", 'F1', 10, 0.2)
    y = 512
    feelings = ["Relief ('So THAT'S why!')", "Grief (for years of struggling without support)",
                "Anger (at being missed/dismissed)", "Confusion (what does this mean for me?)",
                "Imposter syndrome ('Am I autistic enough?')", "Excitement (finally understanding yourself)"]
    for f in feelings:
        doc.add_text(60, y, f"- {f}", 'F1', 9, 0.2)
        y -= 15
    y -= 15
    doc.add_text(50, y, "ALL of these are valid. This workbook is YOUR space to explore.", 'F2', 9, 0)

    # Page 4: Autistic Identity
    doc.new_page()
    doc.add_centered_text(590, "UNDERSTANDING YOUR AUTISTIC IDENTITY", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "What autism means to ME (not textbook definitions):", 'F2', 10, 0)
    y -= 18
    for i in range(4):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14
    y -= 10
    doc.add_text(50, y, "Moments in my past that NOW make sense:", 'F2', 10, 0)
    y -= 18
    for i in range(4):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14
    y -= 10
    doc.add_text(50, y, "My autistic strengths:", 'F2', 10, 0)
    y -= 18
    for i in range(4):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14

    # Pages 5-7: Unmasking Exercises (3 pages)
    unmasking_prompts = [
        ("WHO AM I WITHOUT THE MASK?", ["What I do to appear 'normal':", "What I'd do if no one was watching:",
         "Social rules I follow that exhaust me:", "My natural way of communicating:"]),
        ("MASKS I WEAR", ["At work I pretend to:", "With family I hide:", "With friends I force myself to:",
         "The cost of masking (what it takes from me):"]),
        ("UNMASKING SAFELY", ["Safe people I can be unmasked with:", "Environments where I don't mask:",
         "One mask I want to slowly drop:", "What I need to feel safe being myself:"])
    ]
    for title, prompts in unmasking_prompts:
        doc.new_page()
        doc.add_centered_text(590, title, 'F2', 12, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 555
        for p in prompts:
            doc.add_text(50, y, p, 'F2', 9, 0.1)
            y -= 16
            for i in range(4):
                doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
                y -= 14
            y -= 10

    # Page 8: Sensory Profile Builder
    doc.new_page()
    doc.add_centered_text(590, "SENSORY PROFILE BUILDER", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    senses = [("SOUND:", "Overwhelms:", "Soothes:"), ("SIGHT:", "Overwhelms:", "Soothes:"),
              ("TOUCH:", "Overwhelms:", "Soothes:"), ("SMELL:", "Overwhelms:", "Soothes:"),
              ("TASTE:", "Overwhelms:", "Soothes:"), ("MOVEMENT:", "Overwhelms:", "Soothes:")]
    for sense, overwhelms, soothes in senses:
        doc.add_text(50, y, sense, 'F2', 9, 0)
        y -= 14
        doc.add_text(55, y, f"{overwhelms} ________________________________________", 'F1', 8, 0.3)
        y -= 13
        doc.add_text(55, y, f"{soothes} __________________________________________", 'F1', 8, 0.3)
        y -= 18

    # Page 9: Communication Preferences
    doc.new_page()
    doc.add_centered_text(590, "COMMUNICATION PREFERENCES", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "I communicate best when:", 'F2', 10, 0)
    y -= 18
    prefs = ["[ ] Writing vs [ ] Speaking", "[ ] One-on-one vs [ ] Groups",
             "[ ] Direct/blunt vs [ ] Softened language",
             "[ ] Time to process vs [ ] On the spot",
             "[ ] Structured topics vs [ ] Open-ended chat"]
    for p in prefs:
        doc.add_text(55, y, p, 'F1', 9, 0.2)
        y -= 15
    y -= 10
    doc.add_text(50, y, "Things I wish people knew about how I communicate:", 'F2', 9, 0)
    y -= 16
    for i in range(4):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14

    # Page 10: Social Battery
    doc.new_page()
    doc.add_centered_text(590, "SOCIAL BATTERY MANAGEMENT", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "My social battery:", 'F2', 10, 0)
    y -= 18
    doc.add_text(50, y, "Full charge lasts approximately: ___ hours of socializing", 'F1', 9, 0.2)
    y -= 16
    doc.add_text(50, y, "Recharge time needed: ___ hours alone", 'F1', 9, 0.2)
    y -= 20
    doc.add_text(50, y, "What DRAINS my battery fastest:", 'F2', 9, 0)
    y -= 14
    for i in range(3):
        doc.add_text(50, y, f"_______________________________________________________________", 'F1', 9, 0.4)
        y -= 14
    y -= 8
    doc.add_text(50, y, "What RECHARGES me:", 'F2', 9, 0)
    y -= 14
    for i in range(3):
        doc.add_text(50, y, f"_______________________________________________________________", 'F1', 9, 0.4)
        y -= 14
    y -= 8
    doc.add_text(50, y, "Signs my battery is low:", 'F2', 9, 0)
    y -= 14
    for i in range(3):
        doc.add_text(50, y, f"_______________________________________________________________", 'F1', 9, 0.4)
        y -= 14

    # Page 11: Special Interests
    doc.new_page()
    doc.add_centered_text(590, "SPECIAL INTERESTS AS SELF-CARE", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Your special interests are not 'obsessions.' They are JOY.", 'F2', 10, 0)
    y -= 22
    doc.add_text(50, y, "My current special interests:", 'F1', 9, 0.2)
    y -= 16
    for i in range(3):
        doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 9, 0.3)
        y -= 16
    y -= 8
    doc.add_text(50, y, "Past special interests I look back on fondly:", 'F1', 9, 0.2)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
    y -= 18
    doc.add_text(50, y, "How I can protect time for my interests:", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
    y -= 18
    doc.add_text(50, y, "Ways my interests HELP me (regulation, joy, purpose):", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)

    # Page 12: Executive Function
    doc.new_page()
    doc.add_centered_text(590, "EXECUTIVE FUNCTION STRATEGIES", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    strategies = [
        ("Task initiation:", "Body doubling, timers, 'just do 2 min', pair with special interest"),
        ("Transitions:", "Warnings (timer 10 min before), routines, transition objects"),
        ("Planning:", "Visual schedules, one task at a time, external reminders"),
        ("Time awareness:", "Analog clocks, time-timer app, alarms for everything"),
        ("Organization:", "Everything has a visible home, labels, clear containers"),
        ("Emotional regulation:", "Stim freely, sensory tools, alone time, scripting")
    ]
    for area, tips in strategies:
        doc.add_text(50, y, area, 'F2', 9, 0)
        y -= 14
        doc.add_text(55, y, tips, 'F1', 8, 0.3)
        y -= 20

    # Page 13: Burnout
    doc.new_page()
    doc.add_centered_text(590, "AUTISTIC BURNOUT RECOGNITION", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Autistic burnout is different from regular burnout:", 'F1', 10, 0.2)
    y -= 18
    signs = ["Loss of skills you used to have (speech, driving, self-care)",
             "Extreme exhaustion that sleep doesn't fix", "Increased sensory sensitivity",
             "Loss of ability to mask", "Increased meltdowns/shutdowns",
             "Memory problems", "Physical illness", "Can't do 'simple' things"]
    for s in signs:
        doc.add_text(60, y, f"- {s}", 'F1', 9, 0.2)
        y -= 14
    y -= 10
    doc.add_text(50, y, "Prevention plan:", 'F2', 9, 0)
    y -= 14
    doc.add_text(50, y, "Daily rest needed: ___  Weekly alone time: ___", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Masking I can reduce: _____________________________________________", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Demands I can delegate/drop: ______________________________________", 'F1', 9, 0.2)

    # Page 14: Accommodations
    doc.new_page()
    doc.add_centered_text(590, "ACCOMMODATIONS I DESERVE", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    areas = [("AT WORK:", ["Noise-canceling headphones", "Written instructions", "Flexible schedule",
                           "Reduced meetings", "Clear expectations"]),
             ("AT HOME:", ["Sensory-friendly spaces", "Predictable routines", "Time alone",
                          "Reduced household demands", "Safe foods always available"]),
             ("SOCIALLY:", ["Permission to leave early", "Advance notice of plans",
                           "One-on-one instead of groups", "Text instead of call",
                           "No surprise visitors"])]
    for area, items in areas:
        doc.add_text(50, y, area, 'F2', 9, 0)
        y -= 14
        for item in items:
            doc.add_rect(50, y-3, 8, 8)
            doc.add_text(62, y, item, 'F1', 8, 0.3)
            y -= 12
        y -= 10

    # Page 15: Relationships
    doc.new_page()
    doc.add_centered_text(590, "RELATIONSHIP NAVIGATION", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "What I need in relationships (any kind):", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
    y -= 16
    doc.add_text(50, y, "What I struggle with in relationships:", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
    y -= 16
    doc.add_text(50, y, "How to tell people about my autism:", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "_______________________________________________________________", 'F1', 9, 0.4)
    y -= 16
    doc.add_text(50, y, "Scripts:", 'F2', 9, 0)
    y -= 14
    doc.add_text(50, y, "'I'm autistic, which means I ___________________________________'", 'F4', 9, 0.3)
    y -= 14
    doc.add_text(50, y, "'It helps me when you ___________________________________________'", 'F4', 9, 0.3)
    y -= 14
    doc.add_text(50, y, "'I need __________________________ to be at my best'", 'F4', 9, 0.3)

    # Page 16: Grief + Self-Compassion
    doc.new_page()
    doc.add_centered_text(590, "GRIEF FOR THE YEARS OF MASKING", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "It's okay to grieve:", 'F2', 10, 0)
    y -= 18
    griefs = ["The childhood support you didn't get", "The friendships lost to masking exhaustion",
              "The energy spent pretending to be neurotypical", "The burnouts that could have been prevented",
              "The self you never got to be"]
    for g in griefs:
        doc.add_text(60, y, f"- {g}", 'F1', 9, 0.2)
        y -= 14
    y -= 15
    doc.add_text(50, y, "Letter to past me (with compassion):", 'F2', 9, 0)
    y -= 16
    for i in range(8):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14

    # Page 17: Autistic Joy
    doc.new_page()
    doc.add_centered_text(590, "MY AUTISTIC JOY LIST", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Being autistic isn't all struggle. Celebrate what's GOOD:", 'F2', 10, 0)
    y = 530
    for i in range(15):
        doc.add_text(50, y, f"{i+1}. __________________________________________________________", 'F1', 9, 0.3)
        y -= 20
    y -= 10
    doc.add_text(50, y, "Suggestions: info-dumping about interests, deep focus, pattern", 'F3', 7, 0.4)
    y -= 12
    doc.add_text(50, y, "recognition, honesty, loyalty, sensory joys, stimming, expertise", 'F3', 7, 0.4)

    # Pages 18-22: Weekly Energy/Masking Tracker (5 pages)
    for week in range(5):
        doc.new_page()
        doc.add_centered_text(590, f"WEEKLY ENERGY & MASKING TRACKER - Week {week+1}", 'F2', 10, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 558
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        doc.add_filled_rect(50, y-2, 332, 14, 0.85)
        doc.add_text(52, y, "Day", 'F2', 7, 0)
        doc.add_text(80, y, "Energy", 'F2', 7, 0)
        doc.add_text(120, y, "Masking", 'F2', 7, 0)
        doc.add_text(165, y, "Sensory Load", 'F2', 7, 0)
        doc.add_text(235, y, "Meltdowns", 'F2', 7, 0)
        doc.add_text(295, y, "Special Int.", 'F2', 7, 0)
        y -= 16
        for d in days:
            doc.add_text(52, y, d, 'F1', 8, 0.2)
            doc.add_rect(80, y-3, 30, 13)
            doc.add_rect(120, y-3, 35, 13)
            doc.add_rect(165, y-3, 55, 13)
            doc.add_rect(235, y-3, 45, 13)
            doc.add_rect(295, y-3, 50, 13)
            y -= 16
        y -= 8
        doc.add_text(50, y, "Rate 0-10. Notes: _________________________________________________", 'F1', 8, 0.3)
        y -= 14
        doc.add_text(50, y, "Patterns I notice: _________________________________________________", 'F1', 8, 0.3)
        y -= 14
        doc.add_text(50, y, "Adjustment for next week: __________________________________________", 'F1', 8, 0.3)

    # Page 23: Resources
    doc.new_page()
    doc.add_centered_text(590, "RESOURCES & COMMUNITY", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Online communities:", 'F2', 10, 0)
    y -= 16
    resources = ["r/AutismInWomen (Reddit)", "r/AutisticAdults (Reddit)",
                 "ASAN (Autistic Self Advocacy Network)", "Embrace Autism (assessment + resources)",
                 "#ActuallyAutistic community (social media)", "Neuroclastic.com (by autistic writers)"]
    for r in resources:
        doc.add_text(60, y, f"- {r}", 'F1', 9, 0.2)
        y -= 14
    y -= 10
    doc.add_text(50, y, "Books by autistic authors:", 'F2', 10, 0)
    y -= 16
    books = ["Unmasking Autism - Devon Price", "Divergent Mind - Jenara Nerenberg",
             "Is This Autism? - Donna Henderson"]
    for b in books:
        doc.add_text(60, y, f"- {b}", 'F1', 9, 0.2)
        y -= 14
    y -= 15
    doc.add_text(50, y, "You belong. You always have.", 'F2', 10, 0)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book150_Autistic_Adults_Workbook.pdf')
    print("Book150_Autistic_Adults_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
