"""
Book 3: Nurse Guided Journal
KDP Interior - 6x9 inches (432x648 points)
WHITE background, BLACK text
"""
from pdf_utils import PDFDoc

def create_nurse_journal():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "THE", font='Helvetica', size=14)
    pdf.add_centered_text(475, "NURSE'S", font='HelveticaBold', size=36)
    pdf.add_centered_text(430, "GUIDED JOURNAL", font='HelveticaBold', size=28)
    pdf.add_line(130, 410, 302, 410, 2)
    pdf.add_centered_text(380, "Reflections, Gratitude & Self-Care", font='Helvetica', size=13)
    pdf.add_centered_text(350, "for Healthcare Heroes", font='Helvetica', size=13)
    pdf.add_centered_text(290, "Daily Prompts | Affirmations | Wellness Tracking", font='Helvetica', size=10)
    pdf.add_centered_text(260, "120 Pages of Guided Journaling", font='Helvetica', size=10)
    pdf.add_centered_text(200, "By", font='Helvetica', size=11)
    pdf.add_centered_text(178, "Daniel Tesfamariam", font='HelveticaBold', size=16)
    pdf.add_centered_text(130, "This journal belongs to:", font='Helvetica', size=11)
    pdf.add_line(140, 112, 292, 112, 0.8)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "The Nurse's Guided Journal", font='HelveticaBold', size=13)
    pdf.add_centered_text(475, "Reflections, Gratitude & Self-Care for Healthcare Heroes", font='Helvetica', size=9)
    pdf.add_centered_text(450, "By Daniel Tesfamariam", font='HelveticaBold', size=10)
    pdf.add_centered_text(420, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='Helvetica', size=9)
    pdf.add_centered_text(398, "No part of this publication may be reproduced without permission.", font='Helvetica', size=8)
    pdf.add_centered_text(370, "ISBN: _______________", font='Helvetica', size=9)
    pdf.add_centered_text(348, "Published via Amazon KDP", font='Helvetica', size=9)

    # --- DEDICATION PAGE ---
    pdf.new_page()
    pdf.add_centered_text(420, "Dedicated to every nurse", font='Helvetica', size=14)
    pdf.add_centered_text(395, "who gives their heart to healing others.", font='Helvetica', size=14)
    pdf.add_centered_text(355, "Your compassion changes lives.", font='Helvetica', size=13)
    pdf.add_centered_text(325, "Take a moment to care for yourself too.", font='Helvetica', size=13)

    # --- DAILY REFLECTION PAGES (10 pages) ---
    daily_prompts = [
        "What was the most meaningful moment of my shift today?",
        "How did I make a difference in someone's life today?",
        "What challenge did I face, and how did I handle it?",
        "What am I most proud of from today's work?",
        "What did a patient teach me today?",
        "How did I show compassion today - to others and myself?",
        "What moment made me smile during my shift?",
        "What would I do differently if I could replay today?",
        "How did I grow as a nurse today?",
        "What boundaries did I set (or need to set) for myself?",
    ]

    for i, prompt in enumerate(daily_prompts):
        pdf.new_page()
        pdf.add_centered_text(600, "Daily Reflection", font='HelveticaBold', size=16)
        pdf.add_line(60, 585, 372, 585, 0.5)
        pdf.add_text(60, 560, "Date: _______________    Shift:  Day / Night", font='Helvetica', size=10)
        pdf.add_text(60, 525, "Today's Prompt:", font='HelveticaBold', size=11)

        if len(prompt) > 50:
            pdf.add_text(60, 505, prompt[:50], font='Helvetica', size=11)
            pdf.add_text(60, 488, prompt[50:], font='Helvetica', size=11)
            start_y = 460
        else:
            pdf.add_text(60, 505, prompt, font='Helvetica', size=11)
            start_y = 475

        for line_idx in range(14):
            y_line = start_y - line_idx * 28
            if y_line > 70:
                pdf.add_line(60, y_line, 372, y_line, 0.3, gray=0.5)

        pdf.add_centered_text(40, f"- {i + 4} -", font='Helvetica', size=8)

    # --- GRATITUDE SECTION (5 pages) ---
    gratitude_prompts = [
        "3 patients I am grateful to have cared for this week:",
        "3 colleagues who supported me recently:",
        "3 skills I am grateful to have learned:",
        "3 moments that reminded me why I became a nurse:",
        "3 things about myself as a nurse that I appreciate:",
    ]

    for i, prompt in enumerate(gratitude_prompts):
        pdf.new_page()
        pdf.add_centered_text(600, "Gratitude Page", font='HelveticaBold', size=15)
        pdf.add_line(60, 585, 372, 585, 0.5)
        pdf.add_text(60, 555, prompt, font='Helvetica', size=10)

        y = 510
        for num in range(1, 4):
            pdf.add_text(60, y, f"{num}.", font='HelveticaBold', size=12)
            for line_idx in range(4):
                y -= 25
                pdf.add_line(85, y, 372, y, 0.3, gray=0.5)
            y -= 20

        pdf.add_centered_text(40, f"- {i + 15} -", font='Helvetica', size=8)

    # --- AFFIRMATION PAGES ---
    affirmation_pages = [
        ["I am making a real difference", "in the lives of my patients.", "My work has deep meaning and purpose."],
        ["I am allowed to rest.", "Taking care of myself is not selfish -", "it makes me a better caregiver."],
        ["I am strong, capable, and resilient.", "I have handled difficult situations before", "and I will handle them again."],
        ["I do not have to be perfect.", "Good enough IS enough.", "I give myself grace today."],
        ["My compassion is a superpower.", "The world needs nurses like me.", "I am proud of who I am becoming."],
    ]

    for i, affirmations in enumerate(affirmation_pages):
        pdf.new_page()
        pdf.add_line(60, 520, 372, 520, 0.8)
        y = 440
        for line in affirmations:
            pdf.add_centered_text(y, line, font='HelveticaBold', size=16)
            y -= 35
        pdf.add_line(60, y - 20, 372, y - 20, 0.8)
        pdf.add_text(60, y - 60, "My personal affirmation today:", font='Helvetica', size=11)
        for line_idx in range(4):
            pdf.add_line(60, y - 90 - line_idx * 28, 372, y - 90 - line_idx * 28, 0.3, gray=0.5)
        pdf.add_centered_text(40, f"- {i + 20} -", font='Helvetica', size=8)

    # --- FREE WRITING PAGES (5 pages) ---
    for page_num in range(5):
        pdf.new_page()
        pdf.add_text(60, 605, "Date: _______________", font='Helvetica', size=9)
        for line_idx in range(20):
            y_line = 570 - line_idx * 26
            if y_line > 60:
                pdf.add_line(60, y_line, 372, y_line, 0.25, gray=0.5)
        pdf.add_centered_text(40, f"- {page_num + 26} -", font='Helvetica', size=8)

    # --- BACK MATTER ---
    pdf.new_page()
    pdf.add_centered_text(480, "Thank You", font='HelveticaBold', size=24)
    pdf.add_centered_text(440, "for being a nurse.", font='Helvetica', size=16)
    pdf.add_line(150, 420, 282, 420, 1)
    pdf.add_centered_text(380, "The world is better because of you.", font='Helvetica', size=13)
    pdf.add_centered_text(340, "If you found this journal helpful,", font='Helvetica', size=11)
    pdf.add_centered_text(318, "please consider leaving a review on Amazon.", font='Helvetica', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book3_Nurse_Guided_Journal.pdf')
    print("Book 3 created: Book3_Nurse_Guided_Journal.pdf")

if __name__ == '__main__':
    create_nurse_journal()
