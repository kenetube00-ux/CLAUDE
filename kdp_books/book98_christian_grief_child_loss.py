"""Book 98: Christian Grief Journal for Child Loss"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.08)
    pdf.add_centered_text(430, "HELD BY HEAVEN", 'F5', 24, 1)
    pdf.add_centered_text(395, "A Christian Journal for Parents", 'F4', 14, 0.9)
    pdf.add_centered_text(373, "Who Lost a Child", 'F4', 14, 0.9)
    pdf.add_centered_text(325, "60 Days of Scripture, Reflection & Hope", 'F1', 11, 0.8)
    pdf.add_centered_text(150, author, 'F2', 12, 0.9)
    pdf.add_centered_text(125, "For every parent whose arms ache", 'F4', 10, 0.7)
    pdf.add_centered_text(108, "and whose heart still loves", 'F4', 10, 0.7)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(430, "Held by Heaven", 'F5', 13)
    pdf.add_centered_text(410, "A Christian Journal for Parents Who Lost a Child", 'F4', 9)
    pdf.add_centered_text(380, f"Copyright 2024 {author}. All rights reserved.", 'F1', 9)
    pdf.add_centered_text(362, "No part of this book may be reproduced without permission.", 'F1', 8)
    pdf.add_centered_text(335, "Scripture quotations from the public domain (KJV).", 'F1', 8)
    pdf.add_centered_text(310, "This journal is not a substitute for grief counseling.", 'F1', 8)
    pdf.add_centered_text(290, "Your grief is sacred. Take all the time you need.", 'F4', 9)


    # 30 Scripture verses about children in heaven / comfort
    verses = [
        "Let the little children come to me, and do not hinder them, for the kingdom of heaven belongs to such as these. - Matthew 19:14",
        "He will wipe every tear from their eyes. There shall be no more death, neither sorrow, nor crying. - Revelation 21:4",
        "Precious in the sight of the Lord is the death of his saints. - Psalm 116:15",
        "The Lord is close to the brokenhearted and saves those who are crushed in spirit. - Psalm 34:18",
        "For I am convinced that neither death nor life shall be able to separate us from the love of God. - Romans 8:38-39",
        "Blessed are those who mourn, for they shall be comforted. - Matthew 5:4",
        "He heals the brokenhearted and binds up their wounds. - Psalm 147:3",
        "I shall go to him, but he shall not return to me. - 2 Samuel 12:23",
        "In my Father's house are many mansions. I go to prepare a place for you. - John 14:2",
        "The eternal God is thy refuge, and underneath are the everlasting arms. - Deuteronomy 33:27",
        "Cast all your anxiety on him because he cares for you. - 1 Peter 5:7",
        "My grace is sufficient for thee: for my strength is made perfect in weakness. - 2 Corinthians 12:9",
        "Weeping may endure for a night, but joy cometh in the morning. - Psalm 30:5",
        "Be still, and know that I am God. - Psalm 46:10",
        "I will not leave you comfortless: I will come to you. - John 14:18",
        "For this child I prayed; and the Lord hath given me my petition. - 1 Samuel 1:27",
        "Before I formed thee in the belly I knew thee. - Jeremiah 1:5",
        "Are not two sparrows sold for a farthing? Yet not one falls without your Father knowing. - Matthew 10:29",
        "The Lord gave, and the Lord hath taken away; blessed be the name of the Lord. - Job 1:21",
        "Thou hast turned for me my mourning into dancing. - Psalm 30:11",
        "Though I walk through the valley of the shadow of death, I will fear no evil. - Psalm 23:4",
        "God is our refuge and strength, a very present help in trouble. - Psalm 46:1",
        "Come unto me, all ye that labour and are heavy laden, and I will give you rest. - Matthew 11:28",
        "For we know that if our earthly house were dissolved, we have a building of God, eternal in the heavens. - 2 Cor 5:1",
        "And God shall wipe away all tears from their eyes. - Revelation 7:17",
        "I have loved thee with an everlasting love. - Jeremiah 31:3",
        "The Lord is my shepherd; I shall not want. He restoreth my soul. - Psalm 23:1,3",
        "To be absent from the body is to be present with the Lord. - 2 Corinthians 5:8",
        "Surely goodness and mercy shall follow me all the days of my life. - Psalm 23:6",
        "Behold, I make all things new. - Revelation 21:5",
    ]

    # 60 daily pages
    for day in range(1, 61):
        pdf.new_page()
        verse_idx = (day - 1) % 30
        pdf.add_centered_text(620, f"Day {day}", 'F2', 14)
        pdf.add_line(36, 612, 396, 612, 0.5, 0.3)
        y = 595
        pdf.add_text(36, y, "Date: _______________", 'F1', 9)
        y -= 22
        pdf.add_text(36, y, "Today my heart feels:", 'F2', 9)
        y -= 14
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 20

        # Scripture
        pdf.add_text(36, y, "Scripture for today:", 'F2', 9)
        y -= 14
        # Wrap verse text
        verse = verses[verse_idx]
        words = verse.split()
        line = ""
        for word in words:
            test = line + " " + word if line else word
            if len(test) * 5.5 > 340:
                pdf.add_text(42, y, line, 'F4', 8)
                y -= 11
                line = word
            else:
                line = test
        if line:
            pdf.add_text(42, y, line, 'F4', 8)
            y -= 14

        y -= 10
        pdf.add_text(36, y, "I want to remember:", 'F2', 9)
        y -= 13
        for i in range(3):
            pdf.add_line(36, y, 396, y, 0.5, 0.5)
            y -= 14

        y -= 6
        pdf.add_text(36, y, "What I miss most today:", 'F2', 9)
        y -= 13
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14
        pdf.add_line(36, y, 396, y, 0.5, 0.5)

        y -= 16
        pdf.add_text(36, y, "A question I have for God:", 'F2', 9)
        y -= 13
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14
        pdf.add_line(36, y, 396, y, 0.5, 0.5)

        y -= 16
        pdf.add_text(36, y, "Where I found grace today:", 'F2', 9)
        y -= 13
        pdf.add_line(36, y, 396, y, 0.5, 0.5)

        y -= 16
        pdf.add_text(36, y, "I am not alone because:", 'F2', 9)
        y -= 13
        pdf.add_line(36, y, 396, y, 0.5, 0.5)

        y -= 16
        pdf.add_text(36, y, "Evening prayer:", 'F2', 9)
        y -= 13
        pdf.add_line(36, y, 396, y, 0.5, 0.5)
        y -= 14
        pdf.add_line(36, y, 396, y, 0.5, 0.5)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book98_Christian_Grief_Child_Loss.pdf')
    print("Book98_Christian_Grief_Child_Loss.pdf created successfully!")

if __name__ == "__main__":
    create_book()
