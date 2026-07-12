"""Book 228: The 90-Day Meditation Journal"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)  # 6x9
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 560, 432, 88, 0.2)
    doc.add_centered_text(605, "THE 90-DAY", 'F2', 22, 1)
    doc.add_centered_text(578, "MEDITATION JOURNAL", 'F2', 22, 1)
    doc.add_centered_text(520, "Track Your Practice, Deepen Your Awareness", 'F4', 12, 0.3)
    doc.add_centered_text(150, author, 'F2', 12, 0.3)

    doc.new_page()
    doc.add_centered_text(560, "THE 90-DAY MEDITATION JOURNAL", 'F2', 12)
    doc.add_centered_text(535, f"Copyright {author}. All rights reserved.", 'F1', 9)

    # Types of Meditation
    doc.new_page()
    doc.add_centered_text(610, "TYPES OF MEDITATION", 'F2', 14)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    types = [
        ("MINDFULNESS", "Focus on present moment. Observe without judgment."),
        ("LOVING-KINDNESS", "Send compassion to self and others."),
        ("BODY SCAN", "Slowly move attention through each body part."),
        ("BREATH FOCUS", "Anchor attention on inhale/exhale."),
        ("MANTRA", "Repeat a word or phrase to focus the mind."),
        ("VISUALIZATION", "Imagine a peaceful scene or desired outcome."),
    ]
    for name, desc in types:
        doc.add_text(50, y, name, 'F2', 10)
        y -= 14
        doc.add_text(60, y, desc, 'F1', 9)
        y -= 22

    # Setting Up Practice
    doc.new_page()
    doc.add_centered_text(610, "SETTING UP YOUR PRACTICE", 'F2', 14)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    setup = ["My meditation space: ________________________________",
        "Best time of day for me: ________________________________",
        "Starting duration: ___ minutes",
        "Goal duration by day 90: ___ minutes",
        "Preferred type(s): ________________________________",
        "Cushion/chair/position: ________________________________",
        "Timer/app I use: ________________________________", "",
        "My intention for these 90 days:",
        "________________________________",
        "________________________________", "",
        "Obstacles I anticipate:", "________________________________",
        "How I'll overcome them:", "________________________________"]
    for line in setup:
        doc.add_text(50, y, line, 'F1', 9)
        y -= 16

    # 90 Daily Entries (3 per page = 30 pages)
    for page in range(30):
        doc.new_page()
        for entry in range(3):
            day_num = page * 3 + entry + 1
            if day_num > 90:
                break
            y_start = 610 - entry * 195
            doc.add_text(50, y_start, f"DAY {day_num}", 'F2', 9)
            doc.add_text(130, y_start, "Date: ___/___", 'F1', 8)
            doc.add_text(230, y_start, "Type: __________", 'F1', 8)
            doc.add_text(340, y_start, "___ min", 'F1', 8)
            y = y_start - 14
            doc.add_text(50, y, "Intention: ________________________________", 'F1', 8)
            y -= 13
            doc.add_text(50, y, "Pre-mood: ___/10  Post-mood: ___/10", 'F1', 8)
            y -= 13
            doc.add_text(50, y, "Thoughts that arose: ________________________________", 'F1', 8)
            y -= 13
            doc.add_text(50, y, "Insights: ________________________________", 'F1', 8)
            y -= 13
            doc.add_text(50, y, "Body sensations: ________________ Gratitude: ________________", 'F1', 8)
            y -= 8
            doc.add_line(50, y, 382, y, 0.3, 0.5)


    # Weekly Reflections (12 pages)
    for wk in range(1, 13):
        doc.new_page()
        doc.add_centered_text(610, f"WEEKLY REFLECTION - WEEK {wk}", 'F2', 12)
        doc.add_line(50, 598, 382, 598, 0.5, 0.3)
        y = 575
        prompts = [f"Days meditated this week: ___/7",
            "Total minutes: ___", "Average session: ___ min", "",
            "Patterns noticed:", "________________________________",
            "________________________________", "",
            "Challenges this week:", "________________________________", "",
            "Breakthroughs:", "________________________________", "",
            "What I'll try next week:", "________________________________", "",
            "Mood trend (circle): Improving / Same / Declining",
            "Focus trend: Improving / Same / Declining"]
        for p in prompts:
            doc.add_text(50, y, p, 'F1', 9)
            y -= 14

    # Monthly Milestones (3 pages)
    for month in range(1, 4):
        doc.new_page()
        doc.add_centered_text(610, f"MONTH {month} MILESTONE", 'F2', 12)
        doc.add_line(50, 598, 382, 598, 0.5, 0.3)
        y = 575
        prompts = [f"Days completed: ___/30", "Longest session: ___ min",
            "Favorite meditation type: ________________", "",
            "How my practice has changed:", "________________________________",
            "________________________________", "",
            "Changes I notice in daily life:", "________________________________",
            "________________________________", "",
            "Biggest lesson this month:", "________________________________", "",
            "Goal for next month:", "________________________________"]
        for p in prompts:
            doc.add_text(50, y, p, 'F1', 9)
            y -= 14

    # Progress Comparison
    doc.new_page()
    doc.add_centered_text(610, "30/60/90 DAY PROGRESS COMPARISON", 'F2', 12)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    metrics = ["Average daily minutes", "Consistency (days/week)", "Ease of focus (1-10)",
               "Calm during day (1-10)", "Sleep quality (1-10)", "Reactivity (1-10, lower=better)",
               "Self-awareness (1-10)", "Compassion (1-10)"]
    doc.add_text(50, y, "Metric", 'F2', 8)
    doc.add_text(200, y, "Day 30", 'F2', 8)
    doc.add_text(260, y, "Day 60", 'F2', 8)
    doc.add_text(320, y, "Day 90", 'F2', 8)
    y -= 5
    doc.add_line(50, y, 382, y, 0.5, 0.3)
    for m in metrics:
        y -= 20
        doc.add_text(50, y, m, 'F1', 8)
        doc.add_text(210, y, "___", 'F1', 8)
        doc.add_text(270, y, "___", 'F1', 8)
        doc.add_text(330, y, "___", 'F1', 8)

    # My Meditation Evolution
    doc.new_page()
    doc.add_centered_text(610, "MY MEDITATION EVOLUTION", 'F2', 14)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    prompts = ["When I started, meditation felt like:", "________________________________", "",
        "Now it feels like:", "________________________________", "",
        "The biggest change in me:", "________________________________", "",
        "What I've learned about my mind:", "________________________________", "",
        "How I'll continue after 90 days:", "________________________________", "",
        "My meditation in one word:", "________________________________", "",
        "Advice for my future self:", "________________________________", "________________________________"]
    for p in prompts:
        doc.add_text(50, y, p, 'F1', 9)
        y -= 14

    doc.save("Book228_Meditation_90Day_Journal.pdf")
    print("Created: Book228_Meditation_90Day_Journal.pdf")

if __name__ == "__main__":
    create_book()
