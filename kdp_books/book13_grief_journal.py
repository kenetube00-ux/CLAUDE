"""
Book 13: Pet Loss Grief Journal & Memory Book
KDP Interior - 6x9 inches (432x648)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    pdf.new_page()
    pdf.add_centered_text(530, "FOREVER IN", font='F2', size=22)
    pdf.add_centered_text(495, "MY HEART", font='F2', size=32)
    pdf.add_line(130, 475, 302, 475, 2)
    pdf.add_centered_text(450, "A Pet Loss Grief Journal", font='F1', size=16)
    pdf.add_centered_text(420, "& Memory Book", font='F1', size=16)
    pdf.add_centered_text(375, "Guided Prompts | Cherished Memories", font='F1', size=11)
    pdf.add_centered_text(350, "Letters to My Pet | Healing Reflections", font='F1', size=11)
    pdf.add_centered_text(260, "By", font='F1', size=11)
    pdf.add_centered_text(238, "Daniel Tesfamariam", font='F2', size=16)
    pdf.add_centered_text(150, "In Loving Memory of:", font='F1', size=13)
    pdf.add_line(140, 130, 292, 130, 0.8)

    pdf.new_page()
    pdf.add_centered_text(500, "Forever In My Heart", font='F2', size=13)
    pdf.add_centered_text(475, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(445, "Copyright 2026. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "ISBN: _______________", font='F1', size=9)


    # Pet profile
    pdf.new_page()
    pdf.add_centered_text(600, "About My Beloved Pet", font='F2', size=16)
    pdf.add_line(60, 585, 372, 585, 1)
    fields = ["Name:","Species/Breed:","Color/Markings:","Birthday:",
              "Gotcha Day:","Passed On:","Years Together:",
              "Favorite Toy:","Favorite Treat:","Favorite Spot:","Nickname:"]
    y = 555
    for f in fields:
        pdf.add_text(60, y, f, font='F2', size=11)
        pdf.add_line(180, y-3, 372, y-3, 0.4, gray=0.5)
        y -= 35

    # Memory prompts (15 pages)
    prompts = [
        "The day we first met...", "The funniest thing you ever did...",
        "Our daily routine together...", "The way you greeted me...",
        "Your favorite place to sleep...", "Adventures we shared...",
        "How you comforted me when I was sad...", "Your quirks I miss the most...",
        "The last good day we had...", "What I wish I could tell you...",
        "The lessons you taught me about love...", "How my life changed because of you...",
        "A letter to you in heaven...", "What I want to remember forever...",
        "How I will honor your memory...",
    ]
    for i, prompt in enumerate(prompts):
        pdf.new_page()
        pdf.add_centered_text(600, prompt, font='F2', size=14)
        pdf.add_line(60, 580, 372, 580, 0.8)
        for ln in range(16):
            pdf.add_line(60, 550 - ln*30, 372, 550 - ln*30, 0.25, gray=0.5)
        pdf.add_centered_text(35, f"- {i+4} -", font='F1', size=8)

    # Healing affirmations
    pdf.new_page()
    pdf.add_centered_text(550, "Healing Affirmations", font='F2', size=18)
    pdf.add_line(130, 535, 302, 535, 1)
    affs = [
        "It is okay to grieve. My pain reflects my love.",
        "The bond we shared can never be broken.",
        "I gave my pet a wonderful life.",
        "Healing is not forgetting. It is remembering with peace.",
        "I will love again when my heart is ready.",
        "My pet would want me to be happy.",
    ]
    y = 495
    for a in affs:
        pdf.add_centered_text(y, a, font='F1', size=11)
        y -= 40

    pdf.new_page()
    pdf.add_centered_text(400, "Until We Meet Again", font='F2', size=20)
    pdf.add_centered_text(365, "Your love lives on in every memory.", font='F1', size=12)
    pdf.add_centered_text(325, "If this journal helped you heal,", font='F1', size=11)
    pdf.add_centered_text(303, "please leave a review on Amazon.", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book13_Pet_Loss_Journal.pdf')
    print("Book 13 created: Book13_Pet_Loss_Journal.pdf")

if __name__ == '__main__':
    create_book()
