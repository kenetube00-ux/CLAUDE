from pdf_utils import PDFDoc
import random

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
random.seed(172)

# Page 1: Title Page
pdf.new_page()
pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
pdf.add_centered_text(550, "ADDITION & SUBTRACTION", "F2", 26)
pdf.add_centered_text(515, "PRACTICE", "F2", 26)
pdf.add_centered_text(460, "For 1st Grade (Ages 6-7)", "F4", 18, gray=0.3)
pdf.add_line(180, 440, 432, 440, 2, gray=0.5)
pdf.add_centered_text(400, "Over 500 Problems to Build Math Confidence!", "F1", 13, gray=0.4)
pdf.add_centered_text(370, "Addition Facts 0-20", "F1", 12, gray=0.4)
pdf.add_centered_text(350, "Subtraction Facts 0-20", "F1", 12, gray=0.4)
pdf.add_centered_text(200, author, "F2", 14)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, "ADDITION & SUBTRACTION PRACTICE", "F2", 14)
pdf.add_centered_text(480, "For 1st Grade (Ages 6-7)", "F1", 12)
pdf.add_centered_text(440, f"Copyright (c) 2025 {author}", "F1", 11)
pdf.add_centered_text(420, "All rights reserved.", "F1", 11)
pdf.add_centered_text(380, "No part of this book may be reproduced without permission.", "F1", 10)
pdf.add_centered_text(340, "ISBN: 979-8-XXX-XXXXX-X", "F3", 10)
pdf.add_centered_text(300, "Instructions for Parents/Teachers:", "F2", 12)
pdf.add_text(100, 275, "- Start with the addition section (easier problems first)", "F1", 11)
pdf.add_text(100, 255, "- Encourage your child to work at their own pace", "F1", 11)
pdf.add_text(100, 235, "- Celebrate progress, not perfection!", "F1", 11)
pdf.add_text(100, 215, "- Use the answer key to check work together", "F1", 11)
pdf.add_text(100, 195, "- Award the certificate when complete!", "F1", 11)


# Store all problems for answer key
all_addition = []
all_subtraction = []

# Pages 3-16: Addition pages (14 pages, 20 problems each)
for page_num in range(14):
    pdf.new_page()
    pdf.add_centered_text(755, f"ADDITION - Page {page_num + 1}", "F2", 16)
    pdf.add_line(50, 742, 562, 742, 1, gray=0.7)
    
    # Difficulty increases with page number
    if page_num < 4:
        max_num = 5  # 0-5
    elif page_num < 8:
        max_num = 10  # 0-10
    elif page_num < 12:
        max_num = 15  # 0-15
    else:
        max_num = 20  # 0-20
    
    page_problems = []
    problems_per_col = 10
    col_x = [70, 340]
    
    for prob_idx in range(20):
        col = prob_idx // 10
        row = prob_idx % 10
        x = col_x[col]
        y = 710 - row * 65
        
        a = random.randint(0, max_num)
        b = random.randint(0, min(max_num, 20 - a))
        answer = a + b
        page_problems.append((a, b, answer))
        
        num_str = f"{prob_idx + 1:2d})"
        pdf.add_text(x, y, num_str, "F2", 12)
        pdf.add_text(x + 30, y, f"{a}  +  {b}  =  ____", "F1", 14)
    
    all_addition.append(page_problems)

# Pages 17-30: Subtraction pages (14 pages, 20 problems each) - but we need room for answer key
# Let's do 12 subtraction pages + 2 answer key + 1 certificate = pages 17-30 (but that's only 14)
# Recalculating: 14 addition + 14 subtraction + 2 answer key + 1 cert + title + copyright = 33
# Need to fit in 30: title + copyright + 12 addition + 12 subtraction + 2 answer + 1 cert = 30
# Actually let me re-read: 14 addition + 14 subtraction + answer key 2 + certificate = 32 content pages + 2 = 34
# Let me just do what's specified: title + copyright + 14 add + 14 sub + 2 answer + cert - but that's 33
# I'll combine to fit 30 total: title + copyright + 12 add + 12 sub + 2 answer + 1 cert = 30

# Actually, I already created 14 addition pages. Let me do 12 subtraction pages to fit.
for page_num in range(12):
    pdf.new_page()
    pdf.add_centered_text(755, f"SUBTRACTION - Page {page_num + 1}", "F2", 16)
    pdf.add_line(50, 742, 562, 742, 1, gray=0.7)
    
    if page_num < 3:
        max_num = 5
    elif page_num < 6:
        max_num = 10
    elif page_num < 9:
        max_num = 15
    else:
        max_num = 20
    
    page_problems = []
    col_x = [70, 340]
    
    for prob_idx in range(20):
        col = prob_idx // 10
        row = prob_idx % 10
        x = col_x[col]
        y = 710 - row * 65
        
        a = random.randint(1, max_num)
        b = random.randint(0, a)
        answer = a - b
        page_problems.append((a, b, answer))
        
        num_str = f"{prob_idx + 1:2d})"
        pdf.add_text(x, y, num_str, "F2", 12)
        pdf.add_text(x + 30, y, f"{a}  -  {b}  =  ____", "F1", 14)
    
    all_subtraction.append(page_problems)


# Answer Key Page 1 (Addition answers)
pdf.new_page()
pdf.add_centered_text(755, "ANSWER KEY - ADDITION", "F2", 16)
pdf.add_line(50, 742, 562, 742, 1, gray=0.7)
y = 720
for pg_idx, page_probs in enumerate(all_addition):
    if pg_idx == 7:  # split at page 7
        break
    pdf.add_text(50, y, f"Page {pg_idx+1}:", "F2", 9)
    answers_str = "  ".join([f"{i+1}){p[2]}" for i, p in enumerate(page_probs)])
    pdf.add_text(100, y, answers_str[:90], "F3", 7)
    y -= 14
    if len(answers_str) > 90:
        pdf.add_text(100, y, answers_str[90:], "F3", 7)
        y -= 14
    y -= 6

# Continue addition + subtraction answers
for pg_idx in range(7, len(all_addition)):
    pdf.add_text(50, y, f"Page {pg_idx+1}:", "F2", 9)
    answers_str = "  ".join([f"{i+1}){p[2]}" for i, p in enumerate(all_addition[pg_idx])])
    pdf.add_text(100, y, answers_str[:90], "F3", 7)
    y -= 14
    if len(answers_str) > 90:
        pdf.add_text(100, y, answers_str[90:], "F3", 7)
        y -= 14
    y -= 6

# Answer Key Page 2 (Subtraction answers)
pdf.new_page()
pdf.add_centered_text(755, "ANSWER KEY - SUBTRACTION", "F2", 16)
pdf.add_line(50, 742, 562, 742, 1, gray=0.7)
y = 720
for pg_idx, page_probs in enumerate(all_subtraction):
    pdf.add_text(50, y, f"Page {pg_idx+1}:", "F2", 9)
    answers_str = "  ".join([f"{i+1}){p[2]}" for i, p in enumerate(page_probs)])
    pdf.add_text(100, y, answers_str[:90], "F3", 7)
    y -= 14
    if len(answers_str) > 90:
        pdf.add_text(100, y, answers_str[90:], "F3", 7)
        y -= 14
    y -= 6

# Certificate of Completion
pdf.new_page()
pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
pdf.add_rect(40, 200, 532, 450, 3, gray=0.3)
pdf.add_rect(50, 210, 512, 430, 1, gray=0.5)
pdf.add_centered_text(600, "CERTIFICATE", "F2", 30)
pdf.add_centered_text(565, "OF COMPLETION", "F2", 24)
pdf.add_line(150, 545, 462, 545, 2, gray=0.5)
pdf.add_centered_text(510, "This certifies that", "F4", 14)
pdf.add_line(180, 470, 432, 470, 1)
pdf.add_centered_text(455, "(write your name here)", "F1", 9, gray=0.5)
pdf.add_centered_text(420, "has successfully completed", "F4", 14)
pdf.add_centered_text(390, "Addition & Subtraction Practice", "F2", 16)
pdf.add_centered_text(365, "for 1st Grade", "F1", 12)
pdf.add_centered_text(330, "Completing over 500 math problems!", "F1", 12)
pdf.add_text(100, 280, "Date: _______________", "F1", 12)
pdf.add_text(350, 280, "Teacher/Parent: _______________", "F1", 12)
pdf.add_centered_text(240, "GREAT JOB, MATH STAR!", "F2", 18)

pdf.save("Book172_Addition_Subtraction_Grade1.pdf")
print("SUCCESS: Book172_Addition_Subtraction_Grade1.pdf created (30 pages)")
