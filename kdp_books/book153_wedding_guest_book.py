"""Book 153: Our Wedding Guest Book - Wishes, Advice & Memories"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(520, "OUR WEDDING", 'F5', 32, 0)
    doc.add_centered_text(475, "GUEST BOOK", 'F5', 32, 0)
    doc.add_centered_text(400, "Wishes, Advice & Memories", 'F4', 18, 0.2)
    doc.add_centered_text(300, "________________________", 'F1', 14, 0.5)
    doc.add_centered_text(270, "&", 'F4', 18, 0.3)
    doc.add_centered_text(240, "________________________", 'F1', 14, 0.5)
    doc.add_centered_text(190, "Date: ________________________", 'F4', 14, 0.3)
    doc.add_centered_text(120, author, 'F2', 12, 0)

    doc.new_page()
    doc.add_centered_text(600, "OUR WEDDING GUEST BOOK", 'F2', 14, 0)
    doc.add_text(72, 500, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.3)

    # Page 3: Our Love Story
    doc.new_page()
    doc.add_centered_text(740, "OUR LOVE STORY", 'F5', 22, 0)
    doc.add_line(150, 725, 462, 725, 1, 0.5)
    y = 690
    doc.add_text(72, y, "How We Met:", 'F2', 12, 0)
    y -= 22
    for i in range(4):
        doc.add_text(72, y, "_" * 70, 'F1', 11, 0.4)
        y -= 20
    y -= 15
    doc.add_text(72, y, "Our First Date:", 'F2', 12, 0)
    y -= 22
    for i in range(3):
        doc.add_text(72, y, "_" * 70, 'F1', 11, 0.4)
        y -= 20
    y -= 15
    doc.add_text(72, y, "The Proposal:", 'F2', 12, 0)
    y -= 22
    for i in range(4):
        doc.add_text(72, y, "_" * 70, 'F1', 11, 0.4)
        y -= 20
    y -= 15
    doc.add_text(72, y, "Our Wedding Date: ____________________", 'F2', 12, 0)
    y -= 25
    doc.add_text(72, y, "Venue: ________________________________", 'F2', 12, 0)

    # Pages 4-33: Guest Entry Pages (30 pages)
    for page_num in range(30):
        doc.new_page()
        guest_num = page_num + 1
        doc.add_centered_text(750, f"Guest #{guest_num}", 'F4', 11, 0.4)
        doc.add_line(72, 740, 540, 740, 0.5, 0.7)
        y = 715
        doc.add_text(72, y, "Name: _____________________________________________________________", 'F4', 12, 0.2)
        y -= 30
        doc.add_text(72, y, "Relationship to Couple: ____________________________________________", 'F4', 12, 0.2)
        y -= 40
        doc.add_text(72, y, "Words of Wisdom for the Couple:", 'F2', 13, 0)
        y -= 22
        for i in range(4):
            doc.add_text(72, y, "_" * 70, 'F1', 11, 0.4)
            y -= 22
        y -= 20
        doc.add_text(72, y, "Favorite Memory with Us:", 'F2', 13, 0)
        y -= 22
        for i in range(4):
            doc.add_text(72, y, "_" * 70, 'F1', 11, 0.4)
            y -= 22
        y -= 20
        doc.add_text(72, y, "Prediction for Our Future:", 'F2', 13, 0)
        y -= 22
        for i in range(3):
            doc.add_text(72, y, "_" * 70, 'F1', 11, 0.4)
            y -= 22
        y -= 25
        doc.add_text(72, y, "Signature: _______________________", 'F4', 12, 0.2)

    # Pages 34-36: Photo Pages (3 pages)
    for page_num in range(3):
        doc.new_page()
        doc.add_centered_text(740, f"PHOTO MEMORIES - Page {page_num+1}", 'F2', 14, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        doc.add_text(72, 710, "Attach polaroid or photo booth strips here:", 'F4', 11, 0.3)
        # Photo boxes
        y = 660
        for row in range(2):
            x = 92
            for col in range(2):
                doc.add_rect(x, y-180, 190, 180, 1, 0.5)
                doc.add_text(x+50, y-185, "Caption: ______________", 'F1', 9, 0.4)
                x += 210
            y -= 220

    # Page 37: Advice from Longest-Married
    doc.new_page()
    doc.add_centered_text(740, "MARRIAGE ADVICE FROM OUR", 'F2', 14, 0)
    doc.add_centered_text(720, "LONGEST-MARRIED GUESTS", 'F2', 14, 0)
    doc.add_line(72, 710, 540, 710, 1, 0.5)
    y = 685
    for i in range(5):
        doc.add_text(72, y, f"Names: _________________________  Years Married: _____", 'F4', 11, 0.2)
        y -= 22
        doc.add_text(72, y, "Their secret to a lasting marriage:", 'F1', 10, 0.3)
        y -= 18
        for line in range(3):
            doc.add_text(72, y, "_" * 70, 'F1', 10, 0.4)
            y -= 18
        y -= 22

    # Page 38: Date Night Suggestions
    doc.new_page()
    doc.add_centered_text(740, "DATE NIGHT SUGGESTIONS FROM GUESTS", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 710, "Our guests suggest we try:", 'F4', 12, 0.3)
    y = 685
    for i in range(20):
        doc.add_text(72, y, f"{i+1}. ____________________________________________________________", 'F1', 11, 0.3)
        y -= 25
    y -= 10
    doc.add_text(72, y, "Guest favorite: ___________________________________________________", 'F2', 11, 0.2)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book153_Wedding_Guest_Book.pdf')
    print("Book153_Wedding_Guest_Book.pdf created successfully!")

if __name__ == "__main__":
    create_book()
