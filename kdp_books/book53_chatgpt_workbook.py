"""
Book 53: ChatGPT Workbook - Hands-On Exercises for Adults 45+
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "CHATGPT WORKBOOK", font='F2', size=24)
    pdf.add_centered_text(480, "Hands-On Exercises", font='F1', size=16)
    pdf.add_centered_text(455, "for Adults 45+", font='F1', size=16)
    pdf.add_line(100, 430, 332, 430, 2)
    pdf.add_centered_text(395, "30 Practical Exercises to Master AI", font='F4', size=13)
    pdf.add_centered_text(370, "Learn by Doing - No Tech Skills Required", font='F4', size=12)
    pdf.add_centered_text(300, "By", font='F1', size=12)
    pdf.add_centered_text(275, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "ChatGPT Workbook - Hands-On Exercises for Adults 45+", font='F2', size=11)
    pdf.add_centered_text(470, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(445, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(415, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(390, "Published via Amazon KDP", font='F1', size=10)

    # --- EXERCISES ---
    exercises = [
        ("Your First Conversation", "How to start chatting with AI", "Type 'Hello, I am new to ChatGPT. Can you introduce yourself?'"),
        ("Ask for a Recipe", "Getting cooking help from AI", "Type 'Give me a simple recipe for chicken soup using 5 ingredients'"),
        ("Write an Email", "Let AI help draft messages", "Type 'Help me write a polite email declining a dinner invitation'"),
        ("Plan a Trip", "Use AI as a travel planner", "Type 'Plan a 3-day trip to San Francisco for a couple in their 50s'"),
        ("Summarize an Article", "Get the key points quickly", "Type 'Summarize the main health benefits of walking daily'"),
        ("Get Health Information", "Ask about wellness topics", "Type 'What are simple exercises for someone with bad knees?'"),
        ("Write a Letter", "Compose formal letters easily", "Type 'Write a letter to my insurance company disputing a charge'"),
        ("Create a Shopping List", "Organize your groceries", "Type 'Create a weekly shopping list for two people eating healthy'"),
        ("Learn a New Word", "Expand your vocabulary", "Type 'Explain the word algorithm in simple terms a child would understand'"),
        ("Get Book Recommendations", "Find your next great read", "Type 'Recommend 5 mystery novels for someone who loved Agatha Christie'"),
        ("Write a Birthday Message", "Create heartfelt wishes", "Type 'Write a warm 70th birthday message for my sister who loves gardening'"),
        ("Explain Something Simply", "Understand complex topics", "Type 'Explain how the stock market works in simple terms'"),
        ("Compare Products", "Make better buying decisions", "Type 'Compare the iPad and Samsung Galaxy Tab for a senior who wants to read'"),
        ("Plan a Menu", "Organize weekly meals", "Type 'Plan 5 dinners for this week that are low sodium and easy to cook'"),
        ("Get Exercise Ideas", "Stay active at any age", "Type 'Give me a 15-minute morning exercise routine for someone over 55'"),
        ("Draft a Complaint Letter", "Express concerns professionally", "Type 'Write a complaint letter about poor service at a restaurant'"),
        ("Write a Social Media Post", "Share updates online", "Type 'Write a short Facebook post about my new garden flowers blooming'"),
        ("Get Gardening Advice", "Grow your green thumb", "Type 'What vegetables grow best in a small backyard garden in spring?'"),
        ("Translate a Phrase", "Communicate across languages", "Type 'How do you say thank you very much in Spanish, French, and Italian?'"),
        ("Help with a Crossword", "Get puzzle hints", "Type 'What is a 5 letter word meaning happy that starts with J?'"),
        ("Write a Thank You Note", "Show gratitude beautifully", "Type 'Write a thank you note for a neighbor who watched my cat for a week'"),
        ("Plan a Party", "Organize celebrations", "Type 'Help me plan a surprise 50th anniversary party for 20 guests'"),
        ("Get Movie Recommendations", "Find films to enjoy", "Type 'Recommend 5 feel-good movies from the 1990s'"),
        ("Ask for Tech Help", "Troubleshoot devices", "Type 'My iPhone battery dies too fast. What can I do to fix it?'"),
        ("Create a Daily Schedule", "Organize your time", "Type 'Create a relaxing but productive daily schedule for a retired person'"),
        ("Write a Poem", "Express yourself creatively", "Type 'Write a short poem about the beauty of autumn leaves'"),
        ("Get Financial Tips", "Money wisdom from AI", "Type 'What are 5 ways to save money on groceries without coupons?'"),
        ("Plan a Gift", "Find the perfect present", "Type 'Suggest creative gift ideas for a 60-year-old man who likes fishing'"),
        ("Organize Photos", "Get photo management tips", "Type 'How should I organize 10 years of digital photos on my computer?'"),
        ("Review and Reflect", "Look back on your learning", "Type 'What are the 5 most useful things I can do with ChatGPT every day?'"),
    ]

    for i, (title, learn, prompt) in enumerate(exercises, 1):
        pdf.new_page()
        pdf.add_text(50, 610, f"Exercise {i}", font='F2', size=14)
        pdf.add_text(50, 588, title, font='F2', size=16)
        pdf.add_line(50, 578, 382, 578, 1)

        pdf.add_text(50, 555, "What you'll learn:", font='F5', size=11)
        pdf.add_text(170, 555, learn, font='F4', size=11)

        pdf.add_text(50, 525, "Step-by-step instructions:", font='F5', size=11)
        pdf.add_text(50, 505, "1. Open your browser and go to chat.openai.com", font='F4', size=10)
        pdf.add_text(50, 487, "2. Log in to your free account", font='F4', size=10)
        pdf.add_text(50, 469, "3. Click on 'New Chat' to start fresh", font='F4', size=10)
        pdf.add_text(50, 451, f"4. Type this prompt: {prompt[:50]}", font='F4', size=10)
        pdf.add_text(50, 433, "5. Read the response and ask follow-up questions if needed", font='F4', size=10)

        pdf.add_text(50, 400, "Try it yourself:", font='F5', size=11)
        pdf.add_text(50, 382, f"Your prompt: {prompt}", font='F3', size=9)

        # Blank lines for writing
        pdf.add_text(50, 355, "My result:", font='F5', size=11)
        for j in range(4):
            y_line = 335 - j * 25
            pdf.add_line(50, y_line, 382, y_line, 0.5, gray=0.5)

        pdf.add_text(50, 220, "Tips:", font='F5', size=11)
        pdf.add_text(50, 200, "- Be specific in your requests for better answers.", font='F4', size=10)
        pdf.add_text(50, 182, "- If the response is too complex, ask 'explain it simpler'.", font='F4', size=10)
        pdf.add_text(50, 164, "- You can always say 'try again' for a different response.", font='F4', size=10)

        # Rating
        pdf.add_text(50, 130, "How did it go?  Circle:  1   2   3   4   5  (5 = great!)", font='F1', size=10)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book53_ChatGPT_Workbook.pdf')
    print("Book 53 created: Book53_ChatGPT_Workbook.pdf")

if __name__ == '__main__':
    create_book()
