from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(550, "SIGHT WORDS PRACTICE WORKBOOK", 'F2', 18)
pdf.add_centered_text(520, "100 Essential Words for Kindergarten", 'F4', 14)
pdf.add_centered_text(420, "Trace, Write, Read, and Find!", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, "SIGHT WORDS PRACTICE WORKBOOK", 'F2', 12)
pdf.add_centered_text(575, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: How to Use
pdf.new_page()
pdf.add_centered_text(750, "HOW TO USE THIS BOOK", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 715
for line in [
    "Dear Parents and Teachers,",
    "",
    "This workbook contains 100 of the most common sight words that",
    "kindergartners need to learn. Sight words are words that appear so",
    "frequently in reading that children should recognize them instantly.",
    "",
    "EACH WORD INCLUDES:",
    "- The word printed in large, clear font",
    "- Dotted letters to trace (builds muscle memory)",
    "- Lines to write the word 3 times independently",
    "- A fill-in-the-blank sentence using the word",
    "- A small word search to find the word (builds recognition)",
    "",
    "TIPS FOR SUCCESS:",
    "- Work on 2-4 words per day (don't rush!)",
    "- Read each word aloud before tracing",
    "- Use a finger to trace first, then pencil",
    "- Celebrate each word mastered!",
    "- Review previous words regularly",
    "- Make it fun: play games, use flashcards too",
    "",
    "The 100 words in this book cover approximately 50% of all",
    "words your child will encounter in early reading materials.",
    "Mastering these words builds reading confidence and fluency!",
    "",
    "Happy learning!"
]:
    pdf.add_text(60, y, line, 'F4', 11)
    y -= 18

# 100 sight words
words = [
    "the", "and", "is", "it", "to", "in", "he", "she", "was", "for",
    "on", "are", "but", "not", "you", "all", "can", "her", "had", "one",
    "said", "they", "we", "do", "if", "up", "my", "go", "no", "so",
    "us", "an", "am", "has", "him", "how", "its", "let", "may", "new",
    "now", "old", "our", "out", "own", "say", "too", "use", "way", "who",
    "big", "came", "come", "day", "did", "get", "just", "like", "long", "look",
    "made", "many", "more", "much", "must", "name", "only", "over", "such", "take",
    "than", "them", "then", "very", "when", "what", "will", "with", "your", "each",
    "find", "from", "give", "good", "have", "help", "here", "know", "live", "make",
    "most", "some", "time", "want", "well", "were", "work", "been", "does", "hand"
]

sentences = [
    "I saw ___ cat.", "Tom ___ Sue are friends.", "This ___ my book.", "Give ___ to me.",
    "I want ___ go.", "The ball is ___ the box.", "___ is tall.", "___ likes to read.",
    "It ___ a good day.", "This is ___ you.", "Sit ___ the chair.", "We ___ happy.",
    "I like it, ___ he does not.", "Do ___ run here.", "Can ___ see it?",
    "We ___ went home.", "I ___ do it!", "Give ___ the toy.", "I ___ a cat.",
    "I have ___ dog.", "She ___ hello.", "___ are my friends.", "___ like pizza.",
    "I ___ my homework.", "___ I can, I will.", "Look ___ at the sky.",
    "This is ___ hat.", "Let's ___ outside.", "___, I cannot.", "I am ___ happy.",
    "Come with ___.", "I want ___ apple.", "I ___ glad.", "He ___ a bike.",
    "Tell ___ the story.", "___ do you do it?", "The cat licked ___ paw.",
    "___ me try.", "You ___ sit here.", "I got a ___ toy.",
    "I want it ___.", "The ___ man sat.", "This is ___ house.",
    "Go ___ and play.", "I have my ___ room.", "I ___ thank you.",
    "I like it ___.", "I ___ a pencil.", "Which ___ do I go?", "___ is at the door?",
    "The dog is ___.", "He ___ to see me.", "Please ___ here.",
    "What a nice ___.", "I ___ it myself.", "I ___ a new toy.",
    "He is ___ nice.", "I ___ to play.", "It is so ___.",
    "___ at the bird.", "Mom ___ a cake.", "I have ___ books.",
    "I want ___ of it.", "Thank you so ___.", "We ___ go now.",
    "Write your ___.", "If ___ I could fly.", "Jump ___ the fence.",
    "___ a big one.", "I will ___ a bath.", "I am taller ___ you.",
    "I gave ___ the ball.", "___ we ate lunch.", "She is ___ kind.",
    "___ is it raining?", "___ is your name?", "I ___ try my best.",
    "Come ___ me.", "Write ___ name here.", "___ child got one.",
    "I will ___ my toy.", "I come ___ home.", "I ___ you a gift.",
    "That was ___!", "I ___ two pets.", "Come ___ me.",
    "I am ___ now.", "I ___ the answer.", "I ___ by the lake.",
    "I will ___ a card.", "___ of us are ready.", "I need ___ water.",
    "What ___ is it?", "I ___ to go.", "I feel ___.",
    "We ___ at the park.", "I did good ___.", "He has ___ here.",
    "She ___ her best.", "Raise your ___."
]


# Generate 25 practice pages (4 words per page)
for page_num in range(25):
    pdf.new_page()
    page_words = words[page_num*4:(page_num+1)*4]
    y = 745
    for wi, word in enumerate(page_words):
        word_idx = page_num * 4 + wi
        # Word in large bold
        pdf.add_text(60, y, word.upper(), 'F2', 22)
        y -= 22
        # Dotted trace line (using small dots to simulate)
        pdf.add_text(60, y, f"Trace:  {word}  {word}  {word}", 'F3', 14)
        y -= 18
        # Write lines
        pdf.add_text(60, y, "Write it 3 times:", 'F1', 9)
        pdf.add_line(170, y-2, 280, y-2, 0.5, 0.5)
        pdf.add_line(290, y-2, 400, y-2, 0.5, 0.5)
        pdf.add_line(410, y-2, 520, y-2, 0.5, 0.5)
        y -= 18
        # Sentence
        if word_idx < len(sentences):
            pdf.add_text(60, y, f"Sentence: {sentences[word_idx]}", 'F4', 10)
        y -= 18
        # Mini word search description
        pdf.add_text(60, y, f"Find '{word}' in this row:", 'F1', 9)
        # Create a simple row of letters with the word hidden
        import random
        letters = list("abcdefghijklmnopqrstuvwxyz")
        row_letters = [random.choice(letters) for _ in range(4)]
        pos = random.randint(0, 3)
        row_letters.insert(pos, word)
        search_row = "  ".join(row_letters)
        pdf.add_text(60, y-14, search_row, 'F3', 11)
        y -= 32
        if wi < 3:
            pdf.add_line(60, y+5, 552, y+5, 0.3, 0.7)
            y -= 10

# Page 29-30: Review pages
pdf.new_page()
pdf.add_centered_text(750, "WORD MASTERY CHECKLIST", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 720
pdf.add_text(60, y, "Check off each word as your child masters it:", 'F4', 10)
y -= 18
for i in range(50):
    col = i % 5
    row = i // 5
    pdf.add_text(60 + col*100, y - row*16, f"__ {words[i]}", 'F3', 9)

pdf.new_page()
pdf.add_centered_text(750, "WORD MASTERY CHECKLIST (continued)", 'F2', 16)
pdf.add_line(60, 740, 552, 740)
y = 720
pdf.add_text(60, y, "Check off each word as your child masters it:", 'F4', 10)
y -= 18
for i in range(50, 100):
    col = (i-50) % 5
    row = (i-50) // 5
    pdf.add_text(60 + col*100, y - row*16, f"__ {words[i]}", 'F3', 9)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book106_Sight_Words_Workbook.pdf')
print("Book106_Sight_Words_Workbook.pdf created successfully!")
