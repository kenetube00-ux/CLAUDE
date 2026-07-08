"""Book 82: ADHD Planner for Women"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"
    
    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.12)
    pdf.add_centered_text(420, "ADHD PLANNER", 'F2', 26, 1)
    pdf.add_centered_text(385, "FOR WOMEN", 'F2', 26, 1)
    pdf.add_centered_text(340, "A Neurodivergent-Friendly Daily Organizer", 'F4', 13, 0.9)
    pdf.add_centered_text(300, "Designed for the ADHD brain:", 'F1', 11, 0.8)
    pdf.add_centered_text(282, "Less overwhelm. More dopamine. Zero guilt.", 'F1', 11, 0.8)
    pdf.add_centered_text(180, author, 'F2', 13, 0.9)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(420, "ADHD Planner for Women", 'F2', 13)
    pdf.add_centered_text(398, "A Neurodivergent-Friendly Daily Organizer", 'F4', 10)
    pdf.add_centered_text(365, f"Copyright 2024 {author}. All rights reserved.", 'F1', 9)
    pdf.add_centered_text(345, "No part of this book may be reproduced without permission.", 'F1', 8)
    pdf.add_centered_text(315, "This planner was designed with ADHD brains in mind.", 'F1', 9)
    pdf.add_centered_text(295, "Low executive function days are valid. Use what works, skip what doesn't.", 'F1', 8)
    pdf.add_centered_text(265, "HOW TO USE THIS PLANNER:", 'F2', 10)
    tips = [
        "- There is no wrong way. Messy is fine.",
        "- Each page is ONE day. No weekly spreads to forget.",
        "- The 'ONE must-do' is your anchor. Everything else is bonus.",
        "- The dopamine menu is your reward system. Use it shamelessly.",
        "- Brain dump zone = get it out of your head, deal with it later.",
    ]
    y = 240
    for tip in tips:
        pdf.add_centered_text(y, tip, 'F1', 8)
        y -= 16

    # 60 Daily Planner Pages
    for day in range(1, 61):
        pdf.new_page()
        # Header
        pdf.add_filled_rect(30, 610, 372, 25, 0.9)
        pdf.add_text(36, 618, f"DAY {day}", 'F2', 12)
        pdf.add_text(200, 618, "Date: ___/___/______", 'F1', 9)
        
        # Energy level
        pdf.add_text(36, 592, "Energy Level:", 'F2', 9)
        pdf.add_text(120, 592, "1    2    3    4    5", 'F3', 9)
        pdf.add_text(230, 592, "(circle one)", 'F1', 7)
        
        # ONE must-do
        pdf.add_filled_rect(30, 563, 372, 22, 0.85)
        pdf.add_text(36, 569, "TODAY'S ONE MUST-DO:", 'F2', 10)
        pdf.add_line(195, 567, 395, 567, 0.5, 0.4)
        
        # Top 3 tasks with urgency/importance
        pdf.add_text(36, 545, "TOP 3 TASKS:", 'F2', 9)
        pdf.add_text(260, 545, "Urgent?", 'F2', 7)
        pdf.add_text(310, 545, "Important?", 'F2', 7)
        y = 527
        for i in range(1, 4):
            pdf.add_rect(36, y - 3, 8, 8, 0.5, 0.3)
            pdf.add_text(50, y, f"{i}.", 'F1', 9)
            pdf.add_line(65, y - 2, 250, y - 2, 0.5, 0.5)
            pdf.add_text(268, y, "Y / N", 'F1', 7)
            pdf.add_text(318, y, "Y / N", 'F1', 7)
            y -= 20
        
        # Time blocks (2-hour chunks)
        pdf.add_text(36, y - 5, "TIME BLOCKS:", 'F2', 9)
        y -= 22
        time_blocks = ["8-10am", "10-12pm", "12-2pm", "2-4pm", "4-6pm", "6-8pm"]
        for tb in time_blocks:
            pdf.add_text(36, y, tb, 'F3', 8)
            pdf.add_line(90, y - 2, 250, y - 2, 0.5, 0.5)
            y -= 16
        
        # Dopamine menu
        pdf.add_text(270, 470, "DOPAMINE MENU:", 'F2', 8)
        pdf.add_text(270, 456, "(rewards for task completion)", 'F1', 7)
        yd = 440
        for i in range(4):
            pdf.add_text(270, yd, "-", 'F1', 8)
            pdf.add_line(280, yd - 2, 395, yd - 2, 0.5, 0.5)
            yd -= 15
        
        # Brain dump zone
        pdf.add_rect(30, 260, 372, 100, 0.5, 0.3)
        pdf.add_text(36, 348, "BRAIN DUMP ZONE:", 'F2', 9)
        
        # Did I checklist
        pdf.add_text(36, 240, "DID I...?", 'F2', 9)
        checklist = ["Take meds", "Drink water", "Eat food", "Move body", "Take a break"]
        y_ck = 224
        for item in checklist:
            pdf.add_rect(36, y_ck - 3, 7, 7, 0.5, 0.3)
            pdf.add_text(48, y_ck, item, 'F1', 8)
            y_ck -= 14
        
        # Body doubling
        pdf.add_text(36, y_ck - 5, "Body doubling buddy:", 'F1', 8)
        pdf.add_line(145, y_ck - 7, 250, y_ck - 7, 0.5, 0.5)
        
        # Evening section
        pdf.add_text(270, 240, "EVENING WIND-DOWN:", 'F2', 8)
        pdf.add_line(270, 225, 395, 225, 0.5, 0.5)
        pdf.add_line(270, 210, 395, 210, 0.5, 0.5)
        
        pdf.add_text(270, 190, "Tomorrow's anchor task:", 'F2', 8)
        pdf.add_line(270, 175, 395, 175, 0.5, 0.5)
        
        # Celebration
        pdf.add_filled_rect(30, 80, 372, 30, 0.9)
        pdf.add_text(36, 95, "CELEBRATION - What went RIGHT today:", 'F2', 9)
        pdf.add_line(36, 82, 395, 82, 0.5, 0.5)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book82_ADHD_Planner_Women.pdf')
    print("Book82_ADHD_Planner_Women.pdf created successfully!")

if __name__ == "__main__":
    create_book()
