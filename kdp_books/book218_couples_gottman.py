"""Book 218: The 7 Principles Workbook for Couples"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.2)
    doc.add_centered_text(750, "THE 7 PRINCIPLES WORKBOOK", 'F2', 22, 1)
    doc.add_centered_text(720, "FOR COUPLES", 'F2', 22, 1)
    doc.add_centered_text(660, "Build Your Love Maps & Strengthen Your Marriage", 'F4', 14, 0.3)
    doc.add_centered_text(620, "Research-Based Exercises for Lasting Love", 'F1', 12, 0.4)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    # Copyright
    doc.new_page()
    doc.add_centered_text(700, "THE 7 PRINCIPLES WORKBOOK FOR COUPLES", 'F2', 13)
    doc.add_centered_text(670, f"Copyright {author}", 'F1', 10)
    doc.add_centered_text(650, "All rights reserved.", 'F1', 10)

    # Page 3: The Research Behind Happy Marriages
    doc.new_page()
    doc.add_centered_text(750, "THE RESEARCH BEHIND HAPPY MARRIAGES", 'F2', 15)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = [
        "After decades of research on thousands of couples, key principles emerged:",
        "", "Happy couples are not perfect - they handle conflict differently.",
        "They build deep friendship, maintain positive interactions,",
        "and repair quickly after disagreements.", "",
        "The Magic Ratio: 5 positive interactions for every 1 negative.", "",
        "The Four Horsemen that predict divorce:",
        "  1. Criticism (attacking character, not behavior)",
        "  2. Contempt (disgust, superiority, disrespect)",
        "  3. Defensiveness (counter-attacking, playing victim)",
        "  4. Stonewalling (shutting down, withdrawing)", "",
        "The Antidotes:",
        "  1. Gentle startup (I feel... about... I need...)",
        "  2. Build culture of appreciation",
        "  3. Take responsibility",
        "  4. Self-soothe, then re-engage", "",
        "This workbook guides you through building each principle.",
    ]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 18


    # Love Maps Exercise (pages 4-5)
    for part in range(1, 3):
        doc.new_page()
        doc.add_centered_text(755, f"LOVE MAPS - PARTNER {part}", 'F2', 14)
        doc.add_text(72, 730, "How well do you know your partner's inner world?", 'F4', 11)
        doc.add_line(72, 720, 540, 720, 0.5, 0.3)
        y = 695
        questions = [
            "1. Name your partner's two closest friends:",
            "2. What is your partner's current biggest worry?",
            "3. What is your partner's dream vacation?",
            "4. What is your partner's favorite way to unwind?",
            "5. Name a recent accomplishment they're proud of:",
            "6. What is their biggest life dream right now?",
            "7. What stresses them most at work?",
            "8. Who was their childhood best friend?",
            "9. What would they do with an unexpected $10,000?",
            "10. What is their favorite meal you could make?",
            "11. What is their deepest fear?",
            "12. What makes them feel most loved?",
            "13. What is their favorite way to spend a Saturday?",
            "14. Name something on their bucket list:",
            "15. What is their love language?",
            "16. What family member are they closest to?",
            "17. What would their ideal retirement look like?",
            "18. What song reminds them of your relationship?",
            "19. What do they wish you did more of?",
            "20. What are they most grateful for right now?",
        ]
        for q in questions:
            doc.add_text(72, y, q, 'F1', 9)
            y -= 15
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18

    # Fondness & Admiration (14 days - pages 6-7)
    for part in range(1, 3):
        doc.new_page()
        doc.add_centered_text(755, f"FONDNESS & ADMIRATION - DAYS {(part-1)*7+1}-{part*7}", 'F2', 14)
        doc.add_text(72, 730, "Each day, tell your partner one thing you appreciate about them.", 'F4', 10)
        doc.add_line(72, 720, 540, 720, 0.5, 0.3)
        y = 695
        for day in range((part-1)*7+1, part*7+1):
            doc.add_text(72, y, f"Day {day}  Date: ___/___/___", 'F2', 10)
            y -= 18
            doc.add_text(72, y, "What I appreciate:", 'F1', 9)
            doc.add_line(170, y-2, 540, y-2, 0.5, 0.4)
            y -= 16
            doc.add_text(72, y, "Their response:", 'F1', 9)
            doc.add_line(150, y-2, 540, y-2, 0.5, 0.4)
            y -= 16
            doc.add_text(72, y, "How it made me feel:", 'F1', 9)
            doc.add_line(170, y-2, 540, y-2, 0.5, 0.4)
            y -= 25


    # Turning Toward - Bid Tracking (7 days - pages 8-9)
    for part in range(1, 3):
        doc.new_page()
        ttl = "TURNING TOWARD - BID TRACKING"
        doc.add_centered_text(755, ttl, 'F2', 14)
        doc.add_text(72, 730, "A 'bid' is any attempt to connect. Track how you respond.", 'F4', 10)
        doc.add_line(72, 718, 540, 718, 0.5, 0.3)
        y = 695
        start_day = (part-1)*4 + 1
        end_day = min(part*4, 7)
        for day in range(start_day, end_day+1):
            doc.add_text(72, y, f"Day {day}", 'F2', 10)
            y -= 16
            doc.add_text(72, y, "Bid received:", 'F1', 9)
            doc.add_line(145, y-2, 540, y-2, 0.5, 0.4)
            y -= 16
            doc.add_text(72, y, "My response: [ ] Turned Toward  [ ] Turned Away  [ ] Turned Against", 'F1', 9)
            y -= 16
            doc.add_text(72, y, "Bid I made:", 'F1', 9)
            doc.add_line(130, y-2, 540, y-2, 0.5, 0.4)
            y -= 16
            doc.add_text(72, y, "Partner's response: [ ] Toward  [ ] Away  [ ] Against", 'F1', 9)
            y -= 25

    # Four Horsemen Assessment (pages 10-11)
    doc.new_page()
    doc.add_centered_text(755, "THE FOUR HORSEMEN - ASSESSMENT", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 715
    horsemen = [
        ("CRITICISM", "Attacking character vs. complaining about behavior",
         "Antidote: Gentle startup - 'I feel ___ about ___ and I need ___'"),
        ("CONTEMPT", "Disgust, eye-rolling, name-calling, mockery",
         "Antidote: Build culture of appreciation and respect"),
        ("DEFENSIVENESS", "Counter-attacking, whining, playing victim",
         "Antidote: Accept responsibility for even a small part"),
        ("STONEWALLING", "Shutting down, withdrawing, silent treatment",
         "Antidote: Self-soothe (20 min break), then re-engage"),
    ]
    for name, desc, antidote in horsemen:
        doc.add_text(72, y, name, 'F2', 11)
        y -= 16
        doc.add_text(90, y, desc, 'F1', 9)
        y -= 14
        doc.add_text(90, y, antidote, 'F4', 9)
        y -= 14
        doc.add_text(90, y, "When I do this:", 'F1', 9)
        doc.add_line(170, y-2, 540, y-2, 0.5, 0.4)
        y -= 14
        doc.add_text(90, y, "Instead I will:", 'F1', 9)
        doc.add_line(160, y-2, 540, y-2, 0.5, 0.4)
        y -= 25

    doc.new_page()
    doc.add_centered_text(755, "FOUR HORSEMEN - WEEKLY CHECK-IN", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Track instances this week. Tally marks.", 'F1', 10)
    y -= 25
    for h in ["Criticism", "Contempt", "Defensiveness", "Stonewalling"]:
        doc.add_text(72, y, f"{h}: Me _______ | Partner _______", 'F1', 10)
        y -= 15
        doc.add_text(72, y, f"Antidote used: ________________________________", 'F1', 9)
        y -= 30

    # Repair Attempts Menu (page 12)
    doc.new_page()
    doc.add_centered_text(755, "REPAIR ATTEMPTS MENU", 'F2', 14)
    doc.add_text(72, 730, "20 phrases to use when things get heated:", 'F4', 10)
    doc.add_line(72, 720, 540, 720, 0.5, 0.3)
    y = 700
    repairs = [
        "1. I'm sorry. Please forgive me.",
        "2. Can we take a break and come back to this?",
        "3. I can see my part in this.",
        "4. Let me start again in a softer way.",
        "5. I love you. This is hard but we'll get through it.",
        "6. Tell me what you need right now.",
        "7. I'm getting flooded. I need 20 minutes.",
        "8. Can I have a do-over?",
        "9. You're right. I hadn't thought of it that way.",
        "10. I appreciate you telling me how you feel.",
        "11. One thing I admire about you is...",
        "12. I feel defensive. Can you say that more gently?",
        "13. We're on the same team here.",
        "14. What can I do to make this better right now?",
        "15. I hear you. That makes sense.",
        "16. I'm grateful you're willing to work on this with me.",
        "17. Help me understand your perspective better.",
        "18. This isn't about winning. I want us both to feel heard.",
        "19. Let's find a compromise we can both live with.",
        "20. I believe in us.",
    ]
    for r in repairs:
        doc.add_text(72, y, r, 'F1', 9)
        y -= 16
    y -= 10
    doc.add_text(72, y, "My favorite repairs (circle 5 above). My partner's favorites:", 'F2', 9)
    doc.add_line(72, y-15, 540, y-15, 0.5, 0.4)


    # Creating Shared Meaning (pages 13-16)
    shared_meaning = [
        ("RITUALS OF CONNECTION", ["Morning ritual:", "________________________________",
         "Reunion ritual:", "________________________________",
         "Bedtime ritual:", "________________________________",
         "Weekly date:", "________________________________",
         "Annual traditions:", "________________________________", "________________________________"]),
        ("ROLES IN OUR RELATIONSHIP", ["How we divide household tasks:", "________________________________",
         "How we make financial decisions:", "________________________________",
         "How we parent (or plan to):", "________________________________",
         "How we handle extended family:", "________________________________",
         "How we support each other's careers:", "________________________________"]),
        ("SHARED GOALS", ["1-year goals together:", "________________________________",
         "5-year goals together:", "________________________________",
         "Lifetime dreams together:", "________________________________",
         "How we'll support each other:", "________________________________",
         "What we'll sacrifice for these:", "________________________________"]),
        ("SYMBOLS & STORIES", ["Songs that define us:", "________________________________",
         "Our origin story:", "________________________________",
         "Inside jokes:", "________________________________",
         "Places that matter to us:", "________________________________",
         "Objects that symbolize our love:", "________________________________"]),
    ]
    for title, content in shared_meaning:
        doc.new_page()
        doc.add_centered_text(755, f"CREATING SHARED MEANING: {title}", 'F2', 12)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 20

    # Dreams Within Conflict (page 17)
    doc.new_page()
    doc.add_centered_text(755, "DREAMS WITHIN CONFLICT", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "Behind every gridlocked conflict is an unfulfilled dream.", 'F4', 10)
    y -= 30
    prompts = [
        "The issue we keep fighting about:", "________________________________", "________________________________", "",
        "My position:", "________________________________",
        "My partner's position:", "________________________________", "",
        "The dream behind MY position:", "________________________________",
        "Where this dream comes from (history):", "________________________________", "",
        "The dream behind MY PARTNER'S position:", "________________________________",
        "(Ask them - don't assume)", "",
        "Areas of flexibility (where I can give):", "________________________________",
        "Core areas (non-negotiable for me):", "________________________________", "",
        "A temporary compromise we can try:", "________________________________",
        "________________________________",
    ]
    for line in prompts:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 18

    # Weekly State of the Union (8 pages, 18-25)
    for week in range(1, 9):
        doc.new_page()
        doc.add_centered_text(755, f"STATE OF THE UNION MEETING - WEEK {week}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        doc.add_text(72, y, f"Date: ___/___/___   Duration: ___ minutes", 'F1', 10)
        y -= 25
        sections = [
            "APPRECIATIONS (5 things I appreciated this week):",
            "1. ________________________________",
            "2. ________________________________",
            "3. ________________________________",
            "4. ________________________________",
            "5. ________________________________", "",
            "ISSUES TO PROCESS (use gentle startup):",
            "Issue: ________________________________",
            "My feeling: ________________________________",
            "My need: ________________________________",
            "Partner's perspective: ________________________________",
            "Compromise reached: ________________________________", "",
            "UPCOMING EVENTS & LOGISTICS:",
            "________________________________",
            "________________________________", "",
            "FUN PLANNED THIS WEEK:",
            "________________________________", "",
            "HOW WE'RE DOING (rate 1-10):",
            "Friendship: ___  Intimacy: ___  Fun: ___  Teamwork: ___",
        ]
        for line in sections:
            doc.add_text(72, y, line, 'F1', 9)
            y -= 16

    # Relationship Vision Board (page 26 = last page = 40)
    doc.new_page()
    doc.add_centered_text(755, "OUR RELATIONSHIP VISION", 'F2', 16)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 710
    prompts = [
        "In 1 year, our relationship will be:", "________________________________", "________________________________", "",
        "In 5 years:", "________________________________", "________________________________", "",
        "In 20 years:", "________________________________", "________________________________", "",
        "The kind of couple we want to be:", "________________________________", "",
        "How we want others to describe us:", "________________________________", "",
        "Our shared life mission:", "________________________________", "________________________________", "",
        "What we commit to doing differently:", "________________________________", "________________________________", "",
        "Signed:", "",
        "Partner 1: ___________________ Date: ___/___/___",
        "Partner 2: ___________________ Date: ___/___/___",
    ]
    for line in prompts:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 20

    doc.save("Book218_Gottman_Couples_Workbook.pdf")
    print("Created: Book218_Gottman_Couples_Workbook.pdf")

if __name__ == "__main__":
    create_book()
