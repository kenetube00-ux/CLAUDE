"""
Book 38: Our Love Story - A Couples Journal
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(540, "OUR", font='F5', size=20)
    pdf.add_centered_text(500, "LOVE STORY", font='F5', size=30)
    pdf.add_line(100, 480, 332, 480, 2)
    pdf.add_centered_text(450, "A Couples Journal", font='F4', size=16)
    pdf.add_centered_text(415, "Questions, Prompts & Memories", font='F1', size=11)
    pdf.add_centered_text(390, "to Celebrate Your Relationship", font='F1', size=11)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(235, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "Our Love Story - A Couples Journal", font='F2', size=13)
    pdf.add_centered_text(475, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(395, "Published via Amazon KDP", font='F1', size=9)


    # --- ABOUT US PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "ABOUT US", font='F2', size=18)
    pdf.add_line(120, 600, 312, 600, 1)
    y = 565
    about_fields = [
        "Partner 1 Name: _______________________",
        "Partner 2 Name: _______________________",
        "Our Anniversary: ___/___/______",
        "Where We Met: _________________________",
        "Our First Date: _______________________",
        "First Date Location: __________________",
        "Our Song: _____________________________",
        "Our Favorite Restaurant: ______________",
        "What We Love Most About Each Other:",
        "  Partner 1: __________________________",
        "  Partner 2: __________________________",
    ]
    for field in about_fields:
        pdf.add_text(60, y, field, font='F1', size=10)
        y -= 30

    # --- 50 QUESTION PROMPT PAGES ---
    prompts = [
        "What was your first impression of me?",
        "What is your favorite memory of us together?",
        "What do you love most about our relationship?",
        "Where do you see us in 10 years?",
        "What is your favorite thing I cook?",
        "What is the funniest moment we have shared?",
        "What song reminds you of us?",
        "What is your favorite date we have been on?",
        "What do I do that makes you feel most loved?",
        "What is one thing you want us to try together?",
        "If we could travel anywhere, where would we go?",
        "What was our biggest challenge and how did we overcome it?",
        "What is your love language?",
        "What small gesture of mine means the most to you?",
        "What is something new you learned about me recently?",
        "What does a perfect Sunday look like for us?",
        "What tradition do you want us to start?",
        "What is one goal we should work toward together?",
        "What do you appreciate about how I handle stress?",
        "What was the moment you knew you loved me?",
        "What is your favorite holiday memory with me?",
        "How has our relationship changed you for the better?",
        "What is one thing I can do to support you more?",
        "What is your favorite inside joke of ours?",
        "What dream do you want us to chase together?",
        "What makes our relationship unique?",
        "What is the best advice about love you have received?",
        "What do you think is our greatest strength as a couple?",
        "What is one surprise I gave you that you loved?",
        "What would our relationship movie be titled?",
        "What is something you have never told me?",
        "What do you think we do best as a team?",
        "What is one fear you have overcome with my support?",
        "What is your favorite photo of us and why?",
        "What is the kindest thing I have done for you?",
        "How do you feel most connected to me?",
        "What is one adventure you still want us to have?",
        "What is something about me that always makes you laugh?",
        "What was our most romantic moment?",
        "What is one habit of mine that you find endearing?",
        "If we wrote a book about us, what would Chapter 1 be?",
        "What do you wish we had more time for?",
        "What is one thing you are grateful for about me today?",
        "What is our biggest accomplishment together?",
        "What does home mean to you?",
        "What is one way our love has grown?",
        "What is a challenge you want to face together?",
        "What does forever mean to you?",
        "What is the greatest gift our relationship has given you?",
        "Write a love letter to your partner below.",
    ]


    for i, prompt in enumerate(prompts):
        pdf.new_page()
        pdf.add_centered_text(600, f"Question #{i+1}", font='F2', size=12)
        pdf.add_centered_text(570, prompt, font='F4', size=12)
        pdf.add_line(60, 550, 372, 550, 0.5)

        # Partner 1 section
        y = 520
        pdf.add_text(60, y, "Partner 1:", font='F2', size=10)
        y -= 18
        for _ in range(5):
            pdf.add_line(60, y, 372, y, 0.3)
            y -= 18

        y -= 15
        # Partner 2 section
        pdf.add_text(60, y, "Partner 2:", font='F2', size=10)
        y -= 18
        for _ in range(5):
            pdf.add_line(60, y, 372, y, 0.3)
            y -= 18

        pdf.add_centered_text(35, f"- {i + 4} -", font='F1', size=8)

    # --- 5 DATE NIGHT PLANNER PAGES ---
    for dn in range(1, 6):
        pdf.new_page()
        pdf.add_centered_text(615, f"DATE NIGHT PLANNER #{dn}", font='F2', size=14)
        pdf.add_line(100, 600, 332, 600, 0.8)
        y = 570
        dn_fields = [
            "Date: ___/___/______",
            "Activity/Restaurant: ________________________",
            "Time: _____________",
            "What to Wear: _______________________________",
            "Budget: $__________",
            "Reservations Needed?  [ ] Yes  [ ] No",
            "Babysitter Needed?   [ ] Yes  [ ] No",
            "",
            "How was it? (Rate 1-10): _____",
            "Best moment: ________________________________",
            "_______________________________________________",
            "Would we do this again?  [ ] Yes  [ ] No",
            "Next date idea: _____________________________",
        ]
        for field in dn_fields:
            if field == "":
                y -= 15
            else:
                pdf.add_text(60, y, field, font='F1', size=10)
                y -= 28

    # --- ANNIVERSARY MEMORIES PAGE ---
    pdf.new_page()
    pdf.add_centered_text(615, "ANNIVERSARY MEMORIES", font='F2', size=14)
    pdf.add_line(100, 600, 332, 600, 1)
    y = 570
    for ann in range(1, 6):
        pdf.add_text(60, y, f"Anniversary #{ann}:", font='F2', size=10)
        y -= 18
        pdf.add_text(70, y, "Date: ___/___/______  Years Together: _____", font='F1', size=9)
        y -= 16
        pdf.add_text(70, y, "How We Celebrated: ___________________________", font='F1', size=9)
        y -= 16
        pdf.add_text(70, y, "______________________________________________", font='F1', size=9)
        y -= 16
        pdf.add_text(70, y, "Gift Given/Received: _________________________", font='F1', size=9)
        y -= 25

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book38_Couples_Journal.pdf')
    print("Book 38 created: Book38_Couples_Journal.pdf")

if __name__ == '__main__':
    create_book()
