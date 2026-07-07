"""Book 48: Tween Journal for Girls Ages 9-12"""
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)

# Title page
pdf.new_page()
pdf.add_centered_text(420, "MY SECRET JOURNAL", 'F2', 22)
pdf.add_centered_text(380, "For Girls Ages 9-12", 'F4', 16, 0.3)
pdf.add_line(130, 360, 302, 360, 1, 0.5)
pdf.add_centered_text(200, "Daniel Tesfamariam", 'F4', 14, 0.3)

# Copyright page
pdf.new_page()
pdf.add_centered_text(400, "My Secret Journal - For Girls Ages 9-12", 'F2', 14)
pdf.add_centered_text(370, "Copyright - Daniel Tesfamariam", 'F1', 10)
pdf.add_centered_text(350, "All rights reserved.", 'F1', 10)

# All About Me page
pdf.new_page()
pdf.add_centered_text(600, "All About Me", 'F2', 16)
y = 560
about_fields = [
    "My name: ___________________________________",
    "My age: ________  Birthday: _______________",
    "My favorite color: __________________________",
    "My favorite food: ___________________________",
    "My favorite song: ___________________________",
    "My favorite movie/show: _____________________",
    "My best friends: ____________________________",
    "My hobbies: ________________________________",
    "When I grow up I want to be: ________________",
    "My secret talent: ___________________________",
    "I am happiest when: _________________________",
    "My biggest dream: ___________________________",
]
for field in about_fields:
    pdf.add_text(50, y, field, 'F1', 11)
    y -= 25


# 50 guided prompt pages
prompts = [
    "My best quality is...",
    "If I could have any superpower...",
    "My dream job is...",
    "3 goals for this year...",
    "My best friend makes me happy because...",
    "Something I'm worried about...",
    "What makes me unique...",
    "A letter to my future self...",
    "If I could travel anywhere...",
    "My favorite memory...",
    "Something I want to learn...",
    "The best compliment I ever received...",
    "If I could change one thing about the world...",
    "My favorite place in the whole world...",
    "What I love most about my family...",
    "A challenge I overcame...",
    "If I had a million dollars I would...",
    "The kindest thing someone did for me...",
    "My favorite holiday and why...",
    "Something that always makes me laugh...",
    "A person I look up to and why...",
    "If I could invent anything...",
    "My perfect day would look like...",
    "Three things I am grateful for today...",
    "What being a good friend means to me...",
    "A book or movie that changed my thinking...",
    "My biggest accomplishment so far...",
    "Something I wish adults understood about kids...",
    "If I could meet anyone in history...",
    "What makes me feel brave...",
    "My favorite season and why...",
    "Something new I tried recently...",
    "How I handle feeling sad or angry...",
    "The best advice I ever got...",
    "If I could have dinner with anyone...",
    "What I want to be remembered for...",
    "A time I helped someone...",
    "My favorite thing about school...",
    "Something that scares me but I want to try...",
    "If I could live in any time period...",
    "What makes my generation special...",
    "A skill I want to master...",
    "The funniest thing that happened to me...",
    "What I do when I need to feel better...",
    "My favorite family tradition...",
    "If I could talk to animals...",
    "What confidence means to me...",
    "A place I feel most peaceful...",
    "What I love about being a girl...",
    "My hopes and dreams for next year...",
]

for i, prompt in enumerate(prompts, 1):
    pdf.new_page()
    pdf.add_text(50, 610, f"Prompt {i}", 'F1', 9, 0.5)
    pdf.add_text(50, 580, prompt, 'F2', 13)
    pdf.add_line(50, 568, 382, 568, 0.5, 0.5)
    y = 540
    for _ in range(6):
        pdf.add_line(50, y, 382, y, 0.5, 0.6)
        y -= 28

pdf.save("Book48_Tween_Journal.pdf")
print("Created Book48_Tween_Journal.pdf")
