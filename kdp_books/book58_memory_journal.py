"""
Book 58: My Life Story - A Guided Memory Journal for Ages 45+
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "MY LIFE STORY", font='F2', size=26)
    pdf.add_centered_text(480, "A Guided Memory Journal", font='F1', size=16)
    pdf.add_centered_text(455, "for Ages 45+", font='F1', size=16)
    pdf.add_line(100, 430, 332, 430, 2)
    pdf.add_centered_text(395, "50 Prompts to Capture Your Memories", font='F4', size=13)
    pdf.add_centered_text(370, "Leave a Legacy for Future Generations", font='F4', size=12)
    pdf.add_centered_text(300, "By", font='F1', size=12)
    pdf.add_centered_text(275, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "My Life Story - A Guided Memory Journal for Ages 45+", font='F2', size=11)
    pdf.add_centered_text(470, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(445, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(415, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(390, "Published via Amazon KDP", font='F1', size=10)

    # --- 50 GUIDED PROMPT PAGES ---
    prompts = [
        "Where I grew up...",
        "My childhood home looked like...",
        "My parents were...",
        "My favorite childhood memory is...",
        "My favorite teacher was...",
        "My best friend growing up was...",
        "My first job was...",
        "How I met my spouse/partner...",
        "My wedding day...",
        "When my first child was born...",
        "My proudest moment as a parent...",
        "The hardest thing I ever overcame...",
        "My favorite decade was the...",
        "Technology that changed my life...",
        "Music that defined my youth...",
        "Lessons I learned the hard way...",
        "My career journey started with...",
        "The best vacation I ever took...",
        "Friendships that have lasted a lifetime...",
        "What I would tell my younger self...",
        "My grandchildren mean to me...",
        "Traditions I want to pass on...",
        "The funniest thing that ever happened to me...",
        "A meal I will never forget...",
        "My happiest Christmas/holiday was...",
        "The bravest thing I ever did...",
        "My favorite family recipe is...",
        "A person who changed my life...",
        "What home means to me...",
        "My spiritual or faith journey...",
        "The biggest surprise of my life...",
        "What I am most grateful for...",
        "My hobbies and passions are...",
        "A book or movie that changed my perspective...",
        "The world was different when I was young because...",
        "My neighborhood growing up was...",
        "A pet that was special to me...",
        "My favorite season and why...",
        "Something I wish more people knew...",
        "The kindest thing anyone ever did for me...",
        "A risk I took that paid off...",
        "What makes me laugh the most...",
        "My definition of success has changed because...",
        "A place I would love to visit again...",
        "Something I created that I am proud of...",
        "The best advice I ever received...",
        "What I hope my family remembers about me...",
        "My daily routine and simple pleasures...",
        "How the world has changed in my lifetime...",
        "A letter to my future great-grandchildren...",
    ]

    for i, prompt in enumerate(prompts, 1):
        pdf.new_page()
        pdf.add_text(50, 610, f"Prompt {i}", font='F1', size=10, gray=0.4)
        pdf.add_text(50, 585, prompt, font='F2', size=14)
        pdf.add_line(50, 572, 382, 572, 1)

        # 8 lined writing spaces
        y = 545
        for j in range(16):
            pdf.add_line(50, y, 382, y, 0.4, gray=0.5)
            y -= 28

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book58_Memory_Journal_Seniors.pdf')
    print("Book 58 created: Book58_Memory_Journal_Seniors.pdf")

if __name__ == '__main__':
    create_book()
