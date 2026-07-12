"""Book 231: The Complete Grief Recovery Workbook"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)  # 6x9
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 560, 432, 88, 0.15)
    doc.add_centered_text(605, "THE COMPLETE GRIEF", 'F2', 18, 1)
    doc.add_centered_text(580, "RECOVERY WORKBOOK", 'F2', 18, 1)
    doc.add_centered_text(525, "Process, Heal & Find Meaning After Loss", 'F4', 11, 0.3)
    doc.add_centered_text(150, author, 'F2', 12, 0.3)

    doc.new_page()
    doc.add_centered_text(560, "THE COMPLETE GRIEF RECOVERY WORKBOOK", 'F2', 11)
    doc.add_centered_text(535, f"Copyright {author}. All rights reserved.", 'F1', 9)

    # Understanding Grief
    doc.new_page()
    doc.add_centered_text(610, "UNDERSTANDING GRIEF", 'F2', 13)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    lines = ["Grief is not stages. It is waves.", "",
        "Some days the waves are gentle. Some days they knock",
        "you down. Both are normal. Both are grief.", "",
        "There is no timeline. There is no 'getting over it.'",
        "There is only learning to carry it differently.", "",
        "Types of loss acknowledged in this workbook:",
        "  - Death of a loved one",
        "  - End of a relationship",
        "  - Loss of health or ability",
        "  - Loss of a dream or future",
        "  - Loss of identity or role",
        "  - Loss of safety or trust", "",
        "All grief is valid. Your loss matters."]
    for line in lines:
        doc.add_text(50, y, line, 'F1', 9)
        y -= 14

    # My Grief Profile
    doc.new_page()
    doc.add_centered_text(610, "MY GRIEF PROFILE", 'F2', 13)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    prompts = ["What/who I lost: ________________________________",
        "When: ________________________________",
        "How it happened: ________________________________",
        "________________________________", "",
        "How it changed me:", "________________________________",
        "________________________________", "",
        "What I miss most:", "________________________________", "",
        "What feels unfinished:", "________________________________", "",
        "My grief style: [ ] Intuitive (emotional) [ ] Instrumental (action)",
        "[ ] Mix of both"]
    for p in prompts:
        doc.add_text(50, y, p, 'F1', 9)
        y -= 14

    # Grief Timeline + Unfinished Business
    doc.new_page()
    doc.add_centered_text(610, "THE GRIEF TIMELINE", 'F2', 13)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    doc.add_text(50, y, "Map your relationship story:", 'F4', 9)
    y -= 18
    events = ["How we met/began:", "Happiest memory:", "Hardest moment together:",
              "Last good memory:", "The loss itself:", "First days after:",
              "First month:", "Where I am now:"]
    for e in events:
        doc.add_text(50, y, e, 'F1', 9)
        y -= 12
        doc.add_line(50, y, 382, y, 0.5, 0.5)
        y -= 16

    doc.new_page()
    doc.add_centered_text(610, "UNFINISHED BUSINESS", 'F2', 13)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    prompts = ["Things I wish I had said:", "________________________________",
        "________________________________", "",
        "Things I wish I had done:", "________________________________",
        "________________________________", "",
        "Things I wish they knew:", "________________________________",
        "________________________________", "",
        "Apologies I need to make or receive:", "________________________________", "",
        "What I need to forgive (them or myself):", "________________________________"]
    for p in prompts:
        doc.add_text(50, y, p, 'F1', 9)
        y -= 14

    # Completion Letter
    doc.new_page()
    doc.add_centered_text(610, "RELATIONSHIP REVIEW - COMPLETION LETTER", 'F2', 11)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    doc.add_text(50, y, "Write a letter to express what needs to be said:", 'F4', 9)
    y -= 18
    doc.add_text(50, y, "Dear _______________,", 'F1', 9)
    y -= 16
    doc.add_text(50, y, "I want you to know...", 'F1', 9)
    y -= 14
    for _ in range(20):
        doc.add_line(50, y, 382, y, 0.5, 0.5)
        y -= 14


    # Processing Anger/Guilt/Regret (3 pages each)
    emotions = [
        ("PROCESSING ANGER", ["My anger is directed at:", "What feels unfair:",
            "What my anger is protecting me from:", "Healthy ways to express it:",
            "Letter to my anger:", "________________________________",
            "________________________________", "________________________________"]),
        ("PROCESSING GUILT", ["I feel guilty about:", "Was this actually in my control?",
            "What I would tell a friend feeling this guilt:",
            "Evidence I did my best with what I knew:",
            "Self-forgiveness statement:", "________________________________",
            "________________________________", "________________________________"]),
        ("PROCESSING REGRET", ["My biggest regret:", "Can I change this now?",
            "If no, can I accept it?", "What I learned from this:",
            "How I'll honor this lesson going forward:",
            "________________________________", "________________________________", "________________________________"]),
    ]
    for title, prompts in emotions:
        doc.new_page()
        doc.add_centered_text(610, title, 'F2', 12)
        doc.add_line(50, 598, 382, 598, 0.5, 0.3)
        y = 575
        for p in prompts:
            doc.add_text(50, y, p, 'F1', 9)
            y -= 14
            if not p.startswith("_"):
                doc.add_line(50, y, 382, y, 0.5, 0.5)
                y -= 16

    # Finding Meaning + Continuing Bonds + New Rituals + Identity
    pages = [
        ("FINDING MEANING", ["(Viktor Frankl: meaning doesn't explain loss, it helps us survive it)", "",
            "What meaning am I making from this loss?", "________________________________",
            "How has this changed my values?", "________________________________",
            "What do I want my life to stand for now?", "________________________________",
            "How can I honor what I lost?", "________________________________"]),
        ("CONTINUING BONDS", ["Ways I maintain connection:", "________________________________",
            "Rituals I keep:", "________________________________",
            "How I talk about them:", "________________________________",
            "Items I treasure:", "________________________________",
            "How I feel their presence:", "________________________________"]),
        ("CREATING NEW RITUALS", ["Birthday ritual:", "________________________________",
            "Anniversary/death date:", "________________________________",
            "Holiday traditions:", "________________________________",
            "Daily small ritual:", "________________________________",
            "Memorial/legacy project:", "________________________________"]),
        ("IDENTITY RECONSTRUCTION", ["Who I was before:", "________________________________",
            "Who I am now:", "________________________________",
            "Who I am becoming:", "________________________________",
            "Roles that have changed:", "________________________________",
            "New strengths I've discovered:", "________________________________"]),
    ]
    for title, content in pages:
        doc.new_page()
        doc.add_centered_text(610, title, 'F2', 12)
        doc.add_line(50, 598, 382, 598, 0.5, 0.3)
        y = 575
        for line in content:
            doc.add_text(50, y, line, 'F1', 9)
            y -= 14

    # 30 Daily Grief Journal Pages
    for page in range(10):
        doc.new_page()
        for entry in range(3):
            day_num = page * 3 + entry + 1
            if day_num > 30:
                break
            y_start = 610 - entry * 195
            doc.add_text(50, y_start, f"DAY {day_num}", 'F2', 9)
            doc.add_text(130, y_start, "Date: ___/___", 'F1', 8)
            y = y_start - 14
            doc.add_text(50, y, "Grief wave intensity (1-10): ___", 'F1', 8)
            y -= 12
            doc.add_text(50, y, "What triggered it: ________________________________", 'F1', 8)
            y -= 12
            doc.add_text(50, y, "What helped: ________________________________", 'F1', 8)
            y -= 12
            doc.add_text(50, y, "One thing I'm grateful for: ________________________________", 'F1', 8)
            y -= 12
            doc.add_text(50, y, "One way I honored them: ________________________________", 'F1', 8)
            y -= 8
            doc.add_line(50, y, 382, y, 0.3, 0.5)

    # Support Network + Complicated Grief + Healing Declaration
    doc.new_page()
    doc.add_centered_text(610, "SUPPORT & HEALING", 'F2', 13)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    doc.add_text(50, y, "MY SUPPORT NETWORK:", 'F2', 9)
    y -= 14
    for _ in range(4):
        doc.add_text(60, y, "Name: _____________ How they help: _____________", 'F1', 8)
        y -= 14
    y -= 10
    doc.add_text(50, y, "WHEN GRIEF IS COMPLICATED (seek help if):", 'F2', 9)
    y -= 14
    signs = ["- Unable to function after 6+ months", "- Suicidal thoughts",
        "- Substance use to cope", "- Complete inability to feel joy",
        "- Persistent disbelief the loss occurred"]
    for s in signs:
        doc.add_text(60, y, s, 'F1', 8)
        y -= 12
    y -= 10
    doc.add_text(50, y, "MY HEALING DECLARATION:", 'F2', 9)
    y -= 14
    doc.add_text(50, y, "I am healing. This is what that looks like for me:", 'F4', 9)
    y -= 14
    for _ in range(5):
        doc.add_line(50, y, 382, y, 0.5, 0.5)
        y -= 14

    doc.save("Book231_Grief_Recovery_Complete.pdf")
    print("Created: Book231_Grief_Recovery_Complete.pdf")

if __name__ == "__main__":
    create_book()
