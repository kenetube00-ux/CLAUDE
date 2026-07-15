"""Shared helpers for KDP children's book generation."""
from pdf_utils import PDFDoc

AUTHOR = "Daniel Tesfamariam"

def wrap(text, mx=75):
    words = text.split()
    lines, line = [], ""
    for w in words:
        if len(line + " " + w) > mx:
            lines.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        lines.append(line)
    return lines

def title_page(doc, title, subtitle, tagline, author=AUTHOR):
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    tlines = wrap(title, 40)
    y = 660
    for tl in tlines:
        doc.add_centered_text(y, tl, 'F2', 28, 0)
        y -= 35
    doc.add_centered_text(y, subtitle, 'F4', 16, 0.2)
    doc.add_line(150, y-15, 462, y-15, 2, 0.3)
    doc.add_centered_text(y-50, tagline, 'F1', 12, 0.3)
    doc.add_centered_text(100, f"By {author}", 'F2', 16, 0.2)
    doc.new_page()

def copyright_page(doc, title, author=AUTHOR):
    doc.add_centered_text(600, title[:60], 'F2', 14, 0)
    doc.add_centered_text(560, f"Written by {author}", 'F1', 11, 0.3)
    doc.add_centered_text(540, "Copyright 2025. All rights reserved.", 'F1', 10, 0.4)
    doc.add_centered_text(510, "Published for Amazon KDP", 'F1', 10, 0.4)
    doc.add_centered_text(490, "Paperback Edition - 8.5 x 11 inches", 'F1', 10, 0.4)
    doc.new_page()

def toc_page(doc, chapters):
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 20, 0)
    doc.add_line(180, 710, 432, 710, 1, 0.3)
    y = 670
    for i, ch in enumerate(chapters):
        t = ch if isinstance(ch, str) else ch[0]
        doc.add_text(72, y, f"Chapter {i+1}: {t}", 'F4', 12, 0.2)
        y -= 25
        if y < 80:
            doc.new_page()
            y = 720
    doc.new_page()

def chapter_header(doc, num, title, subtitle=""):
    doc.add_filled_rect(50, 620, 512, 120, 0.9)
    doc.add_centered_text(720, f"CHAPTER {num}", 'F1', 14, 0.4)
    doc.add_centered_text(670, title, 'F2', 20, 0)
    if subtitle:
        lines = wrap(subtitle, 65)
        y = 640
        for l in lines:
            doc.add_centered_text(y, l, 'F4', 11, 0.3)
            y -= 18

def add_wrapped(doc, x, y, text, font='F1', size=11, gray=0.2, mx=75):
    for line in wrap(text, mx):
        if y < 72:
            doc.new_page()
            y = 720
        doc.add_text(x, y, line, font, size, gray)
        y -= 18
    return y

def certificate(doc, cert_title, author=AUTHOR):
    doc.add_filled_rect(50, 250, 512, 400, 0.95)
    doc.add_rect(60, 260, 492, 380, 2, 0.3)
    doc.add_centered_text(600, cert_title, 'F2', 18, 0)
    doc.add_centered_text(550, "Awarded to:", 'F4', 14, 0.3)
    doc.add_centered_text(515, "________________________________", 'F1', 14, 0.3)
    doc.add_centered_text(470, "For completing this entire book!", 'F4', 13, 0.3)
    doc.add_centered_text(420, "Date: _______________", 'F1', 12, 0.3)
    doc.add_centered_text(380, f"Author: {author}", 'F4', 12, 0.3)
    doc.new_page()



def add_supplemental(doc, topic, target=78):
    """Add supplemental pages to reach target page count."""
    # Count current pages
    current = len(doc.pages) + (1 if doc.current_stream else 0)
    needed = target - current
    if needed <= 0:
        return
    
    # Mix of content types
    # Journal pages
    journal_count = min(needed // 3, 15)
    for i in range(journal_count):
        doc.add_centered_text(720, f"MY {topic.upper()} JOURNAL - Entry {i+1}", 'F2', 14, 0)
        doc.add_line(150, 710, 462, 710, 1, 0.4)
        doc.add_text(72, 685, "Date: _______________", 'F1', 11, 0.3)
        doc.add_text(72, 660, "Today I learned:", 'F2', 11, 0.2)
        y = 640
        for _ in range(4):
            doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.4)
            y -= 22
        doc.add_text(72, y-5, "How I will use this:", 'F2', 11, 0.2)
        y -= 28
        for _ in range(3):
            doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.4)
            y -= 22
        doc.add_text(72, y-5, "My goal for tomorrow:", 'F2', 11, 0.2)
        y -= 28
        for _ in range(2):
            doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.4)
            y -= 22
        doc.add_text(72, y-5, "Free writing space:", 'F2', 11, 0.2)
        y -= 25
        while y > 80:
            doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.4)
            y -= 22
        doc.new_page()
    needed -= journal_count
    
    # Activity/worksheet pages
    activity_count = min(needed // 3, 12)
    activities_list = [
        "Think of 3 new ideas related to this topic and explain each one.",
        "Create a mind map connecting everything you learned.",
        "Write a letter explaining this topic to a younger child.",
        "Design a poster that teaches the most important concept.",
        "List 10 questions you still have about this topic.",
        "Draw a comic strip showing what you learned in action.",
        "Write 5 ways you can apply this knowledge in real life.",
        "Create a quiz for a friend (with answer key!).",
        "Compare and contrast two concepts from this book.",
        "Write a short story using ideas from this chapter.",
        "Design an invention inspired by what you learned.",
        "Make a timeline of your learning journey through this book.",
    ]
    for i in range(activity_count):
        doc.add_centered_text(720, f"{topic.upper()} ACTIVITY #{i+1}", 'F2', 14, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.4)
        act = activities_list[i % len(activities_list)]
        doc.add_text(72, 685, "CHALLENGE:", 'F2', 12, 0.1)
        y = 665
        for line in wrap(act, 70):
            doc.add_text(90, y, line, 'F4', 11, 0.2)
            y -= 20
        y -= 10
        doc.add_text(72, y, "My Work:", 'F2', 11, 0.2)
        y -= 20
        while y > 100:
            doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.4)
            y -= 22
        doc.add_text(72, y, "Self-rating (circle): AMAZING / GOOD / NEEDS MORE WORK", 'F1', 10, 0.4)
        doc.new_page()
    needed -= activity_count
    
    # Drawing/creative pages
    draw_count = min(needed // 3, 10)
    draw_prompts = [
        "Draw what you learned today", "Illustrate your favorite concept",
        "Create a visual summary of this chapter", "Draw yourself using this knowledge",
        "Design a symbol that represents this topic", "Sketch your goals",
        "Illustrate a story from this book", "Create an infographic",
        "Draw before and after learning this", "Design a book cover for this chapter",
    ]
    for i in range(draw_count):
        prompt = draw_prompts[i % len(draw_prompts)]
        doc.add_centered_text(720, f"CREATIVE SPACE: {topic.upper()}", 'F2', 14, 0)
        doc.add_centered_text(695, prompt, 'F4', 12, 0.3)
        doc.add_rect(72, 120, 468, 550, 1, 0.4)
        doc.add_centered_text(100, "Use this space for drawing, writing, or brainstorming!", 'F1', 9, 0.5)
        doc.new_page()
    needed -= draw_count
    
    # Notes pages for any remaining
    for i in range(max(0, needed)):
        doc.add_centered_text(720, f"NOTES & IDEAS", 'F2', 14, 0)
        doc.add_line(200, 712, 412, 712, 1, 0.4)
        y = 690
        while y > 60:
            doc.add_text(72, y, "___________________________________________________________________", 'F1', 10, 0.5)
            y -= 22
        doc.new_page()
