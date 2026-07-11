#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(420, "MY GOOD BOY/GIRL", 'F2', 20)
pdf.add_centered_text(390, "A Grief Journal for Dog Loss", 'F4', 13)
pdf.add_centered_text(355, f"By {author}", 'F4', 11)
pdf.add_line(100, 335, 332, 335, 2)
pdf.add_centered_text(300, "Because they were family.", 'F4', 12, 0.3)

# Page 2 - Copyright + Validation
pdf.new_page()
pdf.add_centered_text(440, f"Copyright - {author}", 'F1', 9)
pdf.add_centered_text(425, "All rights reserved.", 'F1', 9)
pdf.add_centered_text(380, "THEY WERE FAMILY", 'F2', 14)
pdf.add_centered_text(355, "Your grief is real.", 'F4', 11, 0.3)
pdf.add_centered_text(335, "Your love was real.", 'F4', 11, 0.3)
pdf.add_centered_text(315, "The bond you shared was real.", 'F4', 11, 0.3)
pdf.add_centered_text(285, "You don't need anyone's permission to grieve.", 'F4', 11, 0.3)
pdf.add_centered_text(265, "They weren't 'just a dog.'", 'F4', 11, 0.3)
pdf.add_centered_text(245, "They were your companion, your comfort,", 'F4', 11, 0.3)
pdf.add_centered_text(225, "your family member, your best friend.", 'F4', 11, 0.3)
pdf.add_centered_text(195, "Take your time with this journal.", 'F1', 10)
pdf.add_centered_text(178, "There is no timeline for grief.", 'F1', 10)

# Page 3 - Dog Profile
pdf.new_page()
pdf.add_centered_text(620, "MY DOG", 'F2', 16)
pdf.add_line(40, 610, 392, 610, 1)
fields = [
    "Name:", "Breed:", "Birthday (or best guess):",
    "Gotcha Day (when they came home):", "Passed on:",
    "Years together:", "Color/markings:", "Weight:",
    "Favorite food:", "Favorite toy:", "Favorite spot:",
    "Nicknames I called them:", "Their signature move:",
    "What made them unique:"
]
y = 585
for f in fields:
    pdf.add_text(40, y, f, 'F2', 10)
    pdf.add_line(200, y-2, 392, y-2, 0.5, 0.7)
    y -= 28


# Pages 4-23 - 20 guided memory pages
prompts = [
    "The day we brought you home...",
    "Your favorite spot in the house was...",
    "You always made me laugh when...",
    "Our walks together were...",
    "How you comforted me when I was sad...",
    "Your quirks that I miss the most...",
    "What I wish I could tell you...",
    "The way you greeted me at the door...",
    "Our morning routine together...",
    "The funniest thing you ever did...",
    "How you changed my life...",
    "The little sounds you made...",
    "What bedtime was like with you...",
    "Your relationship with other people...",
    "The adventures we had together...",
    "How you showed me love...",
    "The last good day we had...",
    "What I miss most about you...",
    "Things that remind me of you...",
    "What you taught me about love...",
]

for prompt in prompts:
    pdf.new_page()
    pdf.add_centered_text(610, prompt, 'F4', 12, 0.3)
    pdf.add_line(40, 595, 392, 595, 0.5)
    y = 570
    for i in range(26):
        pdf.add_line(40, y, 392, y, 0.5, 0.7)
        y -= 18

# Page 24 - Rainbow Bridge
pdf.new_page()
pdf.add_centered_text(580, "THE RAINBOW BRIDGE", 'F2', 14)
pdf.add_line(80, 565, 352, 565, 1)
lines = [
    "Just this side of heaven is a place",
    "called Rainbow Bridge.",
    "",
    "When an animal who has been especially",
    "close to someone here passes,",
    "they go to Rainbow Bridge.",
    "",
    "There are meadows and hills for all",
    "our special friends so they can run",
    "and play together.",
    "",
    "There is plenty of food, water, and sunshine,",
    "and our friends are warm and comfortable.",
    "",
    "All the animals who had been ill and old",
    "are restored to health and vigor.",
    "",
    "Then the day comes when one suddenly stops",
    "and looks into the distance...",
    "They have spotted you, and when you",
    "and your special friend finally meet,",
    "you cling together in joyous reunion,",
    "never to be parted again.",
]
y = 545
for line in lines:
    if line:
        pdf.add_centered_text(y, line, 'F4', 10)
    y -= 16

# Page 25 - Grief is Love
pdf.new_page()
pdf.add_centered_text(450, "Grief is love", 'F5', 18)
pdf.add_centered_text(420, "with nowhere to go.", 'F5', 18)
pdf.add_centered_text(370, "Your grief is proof", 'F4', 12, 0.3)
pdf.add_centered_text(350, "of how deeply you loved.", 'F4', 12, 0.3)
pdf.add_centered_text(320, "And that love still exists.", 'F4', 12, 0.3)
pdf.add_centered_text(290, "It always will.", 'F4', 12, 0.3)


# Page 26 - Creating a Memorial
pdf.new_page()
pdf.add_centered_text(620, "CREATING A MEMORIAL", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 585, "Ways to honor your dog's memory:", 'F2', 10)
ideas = [
    "Plant a tree or garden in their name",
    "Create a photo album or shadow box",
    "Donate to a shelter in their honor",
    "Commission a portrait or custom artwork",
    "Keep their collar in a special place",
    "Write their story and share it",
    "Create a stepping stone for the garden",
    "Light a candle on their birthday",
    "Volunteer at an animal rescue",
    "Frame their paw print",
]
y = 565
for idea in ideas:
    pdf.add_text(50, y, f"- {idea}", 'F1', 9)
    y -= 16
pdf.add_text(40, y-15, "How I want to honor my dog:", 'F2', 10)
y -= 35
for i in range(6):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 18

# Page 27 - When to Open Your Heart Again
pdf.new_page()
pdf.add_centered_text(620, "WHEN TO OPEN YOUR HEART AGAIN", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 585, "There is no right timeline for getting another dog.", 'F4', 10, 0.3)
pdf.add_text(40, 560, "Some things to consider:", 'F2', 10)
consider = [
    "A new dog will never replace your dog - they don't have to",
    "Getting another dog is not a betrayal",
    "Your dog would want you to love again",
    "Only you know when you're ready",
    "It's okay if that's soon. It's okay if that's years.",
    "It's also okay if the answer is never.",
]
y = 540
for c in consider:
    pdf.add_text(50, y, f"- {c}", 'F1', 9)
    y -= 16
pdf.add_text(40, y-15, "My feelings about another dog someday:", 'F2', 10)
y -= 35
for i in range(8):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 18

# Pages 28-29 - Love Letter
pdf.new_page()
pdf.add_centered_text(620, "MY LOVE LETTER TO YOU", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Dear ___________________,", 'F4', 11)
y = 565
for i in range(28):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 17

pdf.new_page()
pdf.add_centered_text(620, "MY LOVE LETTER (continued)", 'F2', 12)
pdf.add_line(40, 610, 392, 610, 1)
y = 585
for i in range(28):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 17
pdf.add_text(40, y-10, "Forever yours, _____________________", 'F4', 11)

# Page 30 - Closing
pdf.new_page()
pdf.add_centered_text(420, "Until we meet again", 'F5', 16)
pdf.add_centered_text(385, "at the Rainbow Bridge,", 'F5', 16)
pdf.add_centered_text(345, "know that you were the", 'F4', 12, 0.3)
pdf.add_centered_text(325, "very best dog.", 'F4', 12, 0.3)
pdf.add_centered_text(285, "You were loved beyond measure.", 'F4', 12, 0.3)
pdf.add_centered_text(255, "And you always will be.", 'F4', 12, 0.3)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book180_Dog_Loss_Grief_Journal.pdf')
print("Book180_Dog_Loss_Grief_Journal.pdf created successfully!")
