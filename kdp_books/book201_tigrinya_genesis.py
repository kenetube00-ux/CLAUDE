"""Book 201: IN THE BEGINNING - Genesis Bible Study (Tigrinya-English)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.94)
    pdf.add_centered_text(600, "IN THE BEGINNING", 'F2', 28)
    pdf.add_centered_text(560, "Genesis Bible Study", 'F4', 16, 0.2)
    pdf.add_centered_text(535, "(Tigrinya-English)", 'F1', 13, 0.3)
    pdf.add_centered_text(480, "10 Weekly Studies Through Genesis", 'F1', 12, 0.3)
    pdf.add_centered_text(200, f"By {author}", 'F2', 14, 0.2)

    # Copyright page
    pdf.new_page()
    pdf.add_text(72, 700, "IN THE BEGINNING - Genesis Bible Study", 'F2', 12)
    pdf.add_text(72, 680, f"By {author}", 'F1', 10)
    pdf.add_text(72, 655, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(72, 635, "Scripture from World English Bible (WEB) - Public Domain", 'F1', 9)
    pdf.add_text(72, 610, "Published by KIDLYTICAL Books", 'F1', 9)

    studies = [
        ("Genesis 1:1-2:3", "Creation", "In the beginning, God created the heavens and the earth.", "God spoke and everything came into being. He made light, sky, land, sea, plants, sun, moon, stars, fish, birds, animals, and humans."),
        ("Genesis 2:4-25", "The Garden of Eden", "The LORD God formed man from the dust of the ground and breathed life into him.", "God placed Adam in a beautiful garden and gave him a partner, Eve. They walked with God in perfect fellowship."),
        ("Genesis 3:1-24", "The Fall", "For God knows that in the day you eat of it, your eyes will be opened.", "The serpent deceived Eve, and both Adam and Eve disobeyed God. Sin entered the world, but God promised a Savior."),
        ("Genesis 6:9-9:17", "Noah and the Flood", "Noah was a righteous man, blameless among his generation. Noah walked with God.", "God judged wickedness with a flood but saved Noah and his family. After the flood, God made a covenant with the rainbow."),
        ("Genesis 12:1-9", "The Call of Abraham", "I will make of you a great nation. I will bless you and make your name great.", "God called Abram to leave his homeland and go to a new place. Abram obeyed by faith and God promised to bless all nations through him."),
        ("Genesis 22:1-19", "Abraham's Test", "God will provide himself the lamb for a burnt offering, my son.", "God tested Abraham by asking him to sacrifice Isaac. Abraham obeyed, and God provided a ram instead. This foreshadows Jesus."),
        ("Genesis 27-28", "Jacob's Story", "Your brother came with deceit, and has taken away your blessing.", "Jacob deceived his father and brother, yet God still chose him. At Bethel, God appeared to Jacob and renewed the covenant promise."),
        ("Genesis 37:1-36", "Joseph Sold", "Come, let us sell him to the Ishmaelites, and let our hand not be upon him.", "Joseph's brothers sold him into slavery out of jealousy. But God was with Joseph and had a plan for good."),
        ("Genesis 39-41", "Joseph in Egypt", "The LORD was with Joseph, and he was a prosperous man.", "Though imprisoned falsely, Joseph trusted God. God gave him the ability to interpret dreams and raised him to power."),
        ("Genesis 45:1-15; 50:15-21", "Reconciliation", "You meant evil against me, but God meant it for good.", "Joseph forgave his brothers and saved his family from famine. What was meant for evil, God turned for good.")
    ]

    for week_num, (passage, title, key_verse, summary) in enumerate(studies, 1):
        # Study page
        pdf.new_page()
        pdf.add_filled_rect(50, 725, 512, 42, 0.85)
        pdf.add_centered_text(742, f"WEEK {week_num}: {title.upper()}", 'F2', 16)
        pdf.add_centered_text(718, passage, 'F5', 12)
        pdf.add_line(72, 710, 540, 710, 1, 0.6)

        # Key Verse
        pdf.add_text(72, 688, "Key Verse (WEB):", 'F2', 11)
        words = key_verse.split()
        line = ""
        y = 670
        for w in words:
            if len(line + " " + w) > 75:
                pdf.add_text(82, y, line, 'F4', 10)
                y -= 14
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(82, y, line, 'F4', 10)
            y -= 14

        # Tigrinya placeholder
        y -= 8
        pdf.add_text(72, y, "Tigrinya:", 'F2', 10)
        y -= 14
        pdf.add_text(82, y, "[Tigrinya key verse text here]", 'F3', 9, 0.4)

        # Summary
        y -= 25
        pdf.add_text(72, y, "Passage Summary:", 'F2', 11)
        y -= 16
        words = summary.split()
        line = ""
        for w in words:
            if len(line + " " + w) > 78:
                pdf.add_text(82, y, line, 'F1', 10)
                y -= 14
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(82, y, line, 'F1', 10)
            y -= 14

        # What happened?
        y -= 25
        pdf.add_text(72, y, "WHAT HAPPENED IN THIS PASSAGE?", 'F2', 11)
        for _ in range(3):
            y -= 18
            pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # What does this teach about God?
        y -= 25
        pdf.add_text(72, y, "WHAT DOES THIS TEACH ABOUT GOD?", 'F2', 11)
        for _ in range(3):
            y -= 18
            pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # How does this apply?
        y -= 25
        pdf.add_text(72, y, "HOW DOES THIS APPLY TO MY LIFE?", 'F2', 11)
        for _ in range(3):
            y -= 18
            pdf.add_line(72, y, 540, y, 0.5, 0.7)

        # Discussion Questions
        y -= 25
        pdf.add_text(72, y, "DISCUSSION QUESTIONS:", 'F2', 11)
        disc_qs = [
            "What surprises you about this passage?",
            "How does this connect to the rest of the Bible story?",
            "What would you have done in this situation?"
        ]
        for q in disc_qs:
            y -= 18
            pdf.add_text(82, y, f"- {q}", 'F1', 10)

        # Prayer
        y -= 30
        pdf.add_text(72, y, "PRAYER:", 'F2', 11)
        y -= 18
        pdf.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 16
        pdf.add_line(72, y, 540, y, 0.5, 0.7)

    # Genesis Timeline
    pdf.new_page()
    pdf.add_centered_text(750, "GENESIS TIMELINE", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    events = [
        ("Ch 1-2", "Creation"),
        ("Ch 3", "The Fall - Sin Enters"),
        ("Ch 4", "Cain and Abel"),
        ("Ch 5", "Genealogy: Adam to Noah"),
        ("Ch 6-9", "The Flood & Noah's Covenant"),
        ("Ch 10-11", "Tower of Babel"),
        ("Ch 12-14", "Call of Abraham"),
        ("Ch 15-17", "God's Covenant with Abraham"),
        ("Ch 18-19", "Sodom & Gomorrah"),
        ("Ch 21-22", "Isaac Born & Abraham's Test"),
        ("Ch 25-27", "Jacob and Esau"),
        ("Ch 28-35", "Jacob's Journey"),
        ("Ch 37-41", "Joseph in Egypt"),
        ("Ch 42-50", "Reconciliation & Israel in Egypt")
    ]
    y = 710
    for ch, event in events:
        pdf.add_text(72, y, ch, 'F2', 10)
        pdf.add_text(160, y, event, 'F1', 10)
        pdf.add_line(72, y - 8, 540, y - 8, 0.3, 0.8)
        y -= 28

    # Character Map
    pdf.new_page()
    pdf.add_centered_text(750, "GENESIS CHARACTER MAP", 'F2', 18)
    pdf.add_line(72, 735, 540, 735, 1, 0.5)
    characters = [
        ("Adam & Eve", "First humans, created by God"),
        ("Cain & Abel", "Sons of Adam - first murder"),
        ("Noah", "Righteous man saved from flood"),
        ("Abraham", "Father of faith, called by God"),
        ("Sarah", "Abraham's wife, mother of Isaac"),
        ("Isaac", "Son of promise"),
        ("Rebekah", "Isaac's wife"),
        ("Jacob (Israel)", "Deceiver who was transformed"),
        ("Esau", "Jacob's twin brother"),
        ("Joseph", "Dreamer sold into slavery, rose to power"),
    ]
    y = 710
    for name, desc in characters:
        pdf.add_text(72, y, name, 'F2', 11)
        pdf.add_text(220, y, desc, 'F1', 10, 0.3)
        y -= 28

    # Fill to 30 pages
    current_pages = len(pdf.pages) + 1
    for extra in range(30 - current_pages):
        pdf.new_page()
        pdf.add_centered_text(750, "NOTES & REFLECTIONS", 'F2', 14)
        y = 720
        while y > 80:
            pdf.add_line(72, y, 540, y, 0.5, 0.8)
            y -= 22

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book201_Tigrinya_Genesis_Study.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
