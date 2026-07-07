"""
Book 59: The AI-Powered Daily Planner - Use Technology to Organize Your Life (45+)
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "THE AI-POWERED", font='F2', size=22)
    pdf.add_centered_text(500, "DAILY PLANNER", font='F2', size=24)
    pdf.add_line(100, 478, 332, 478, 2)
    pdf.add_centered_text(450, "Use Technology to", font='F1', size=14)
    pdf.add_centered_text(428, "Organize Your Life", font='F1', size=14)
    pdf.add_centered_text(395, "For Adults 45+", font='F4', size=13)
    pdf.add_centered_text(300, "By", font='F1', size=12)
    pdf.add_centered_text(275, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "The AI-Powered Daily Planner", font='F2', size=12)
    pdf.add_centered_text(475, "Use Technology to Organize Your Life (45+)", font='F1', size=11)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(390, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(365, "Published via Amazon KDP", font='F1', size=10)

    # --- INTRO PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "How AI Can Help You Plan", font='F2', size=16)
    pdf.add_line(80, 585, 352, 585, 1)

    intro_lines = [
        "Welcome to a new way of planning your day! AI tools like ChatGPT,",
        "Siri, and Google Assistant can help you organize your life effortlessly.",
        "",
        "Each daily page in this planner includes an 'Ask AI' suggestion -",
        "a prompt you can try with ChatGPT or your voice assistant.",
        "",
        "How to use this planner:",
        "1. Start each morning by reading the AI suggestion for the day.",
        "2. Try the prompt with ChatGPT or your preferred AI tool.",
        "3. Write down your priorities and schedule for the day.",
        "4. In the evening, note what AI tool you tried and what you learned.",
        "5. Track your wellness: sleep, water intake, and steps.",
        "",
        "You do not need to use AI every day - go at your own pace.",
        "Even trying one new AI prompt per week will build your confidence.",
        "",
        "Remember: AI is your assistant, not your boss. You are in control!",
    ]

    y = 555
    for line in intro_lines:
        if line == "":
            y -= 10
        else:
            pdf.add_text(50, y, line, font='F4', size=11)
            y -= 18

    # --- 30 DAILY PLANNER PAGES ---
    ai_prompts = [
        "Ask ChatGPT to plan healthy meals for today",
        "Ask AI for 3 gentle stretching exercises for morning",
        "Ask ChatGPT to create a gratitude prompt for reflection",
        "Ask AI for exercise ideas suitable for your fitness level",
        "Ask ChatGPT to suggest a calming evening routine",
        "Ask AI to recommend a podcast on a topic you are curious about",
        "Ask ChatGPT to write a kind message to send to a friend",
        "Ask AI for tips on improving your sleep quality tonight",
        "Ask ChatGPT to suggest a new hobby to try this week",
        "Ask AI to plan a 30-minute nature walk route in your area",
        "Ask ChatGPT to explain one new technology term simply",
        "Ask AI for a simple recipe using what is in your fridge",
        "Ask ChatGPT to create a short mindfulness meditation script",
        "Ask AI for book recommendations based on your favorite genre",
        "Ask ChatGPT to help you draft a letter to a loved one",
        "Ask AI for brain exercises to keep your mind sharp today",
        "Ask ChatGPT to suggest ways to declutter one room this week",
        "Ask AI for tips on staying motivated with your goals",
        "Ask ChatGPT to plan a fun activity for this weekend",
        "Ask AI to create a simple budget for this month's extras",
        "Ask ChatGPT for conversation starters for a family dinner",
        "Ask AI to suggest a new music artist based on your taste",
        "Ask ChatGPT to help you set a realistic weekly fitness goal",
        "Ask AI for tips on reducing screen time before bed",
        "Ask ChatGPT to write a positive affirmation for your day",
        "Ask AI to suggest volunteer opportunities in your community",
        "Ask ChatGPT to create a simple daily routine for productivity",
        "Ask AI for tips on staying socially connected as you age",
        "Ask ChatGPT to help you plan a small garden project",
        "Ask AI to summarize the most important news of this week",
    ]

    tomorrow_prompts = [
        "Ask AI how to start a morning meditation practice",
        "Ask ChatGPT for a healthy breakfast idea",
        "Ask AI for a quick home workout",
        "Ask ChatGPT to plan your week ahead",
        "Ask AI for a new recipe to try",
        "Ask ChatGPT for a fun trivia question",
        "Ask AI for ways to reduce stress today",
        "Ask ChatGPT to recommend a movie tonight",
        "Ask AI for tips on better posture",
        "Ask ChatGPT to create a mini bucket list",
        "Ask AI for a new word to learn",
        "Ask ChatGPT for a weekend adventure idea",
        "Ask AI for a simple craft project",
        "Ask ChatGPT for deep breathing exercises",
        "Ask AI for a historical fact for today",
        "Ask ChatGPT for a healthy snack idea",
        "Ask AI for a compliment to share",
        "Ask ChatGPT for a puzzle to solve",
        "Ask AI for a new walking route idea",
        "Ask ChatGPT for journaling prompts",
        "Ask AI for a fun science fact",
        "Ask ChatGPT for a random act of kindness idea",
        "Ask AI for a memory game to play",
        "Ask ChatGPT for a life reflection question",
        "Ask AI for easy stretches at your desk",
        "Ask ChatGPT for a quote to inspire you",
        "Ask AI for a phone organization tip",
        "Ask ChatGPT for an evening wind-down routine",
        "Ask AI for a fun family activity idea",
        "Ask ChatGPT for something new to learn today",
    ]

    for day in range(1, 31):
        pdf.new_page()
        pdf.add_text(50, 615, f"Day {day}", font='F2', size=14)
        pdf.add_text(300, 615, "Date: ___/___/______", font='F1', size=10)
        pdf.add_line(50, 605, 382, 605, 1)

        # Ask AI section
        pdf.add_filled_rect(50, 573, 332, 25, gray=0.92)
        pdf.add_text(55, 580, "Ask AI:", font='F2', size=10)
        pdf.add_text(105, 580, ai_prompts[day - 1], font='F4', size=9)

        # Priority tasks
        pdf.add_text(50, 555, "Priority Tasks:", font='F5', size=11)
        y = 537
        for t in range(3):
            pdf.add_rect(55, y - 3, 8, 8, line_width=0.5)
            pdf.add_line(70, y - 2, 382, y - 2, 0.4, gray=0.5)
            y -= 20

        # Schedule
        y -= 5
        pdf.add_text(50, y, "Schedule:", font='F5', size=11)
        y -= 18
        blocks = ["Morning (8-12):", "Afternoon (12-5):", "Evening (5-9):"]
        for block in blocks:
            pdf.add_text(55, y, block, font='F2', size=9)
            pdf.add_line(160, y - 2, 382, y - 2, 0.4, gray=0.5)
            y -= 16
            pdf.add_line(160, y - 2, 382, y - 2, 0.4, gray=0.5)
            y -= 20

        # AI tool tried today
        y -= 5
        pdf.add_text(50, y, "AI tool I tried today:", font='F5', size=10)
        pdf.add_line(190, y - 2, 382, y - 2, 0.4, gray=0.5)
        y -= 22

        pdf.add_text(50, y, "What I learned:", font='F5', size=10)
        y -= 15
        pdf.add_line(50, y, 382, y, 0.4, gray=0.5)
        y -= 15
        pdf.add_line(50, y, 382, y, 0.4, gray=0.5)

        # Wellness check
        y -= 25
        pdf.add_text(50, y, "Wellness Check:", font='F5', size=10)
        y -= 18
        pdf.add_text(55, y, "Sleep: ___hrs   Water: ___glasses   Steps: _______", font='F1', size=9)

        # Tomorrow's prompt
        y -= 25
        pdf.add_text(50, y, "Tomorrow's AI prompt to try:", font='F5', size=9)
        y -= 15
        pdf.add_text(55, y, tomorrow_prompts[day - 1], font='F4', size=9)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book59_AI_Powered_Daily_Planner.pdf')
    print("Book 59 created: Book59_AI_Powered_Daily_Planner.pdf")

if __name__ == '__main__':
    create_book()
