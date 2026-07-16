"""Book355: My Amazing Life - Guided Journal for Girls"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc()
    author = "Daniel Tesfamariam"


    themes = [
        ("About Me", ["What are your top 5 favorite things in the world?", "Describe yourself in 10 words.", "What makes you laugh the hardest?", "What is your dream job and why?", "If you could have any superpower, what and why?", "Describe your perfect day from morning to night.", "What are you most proud of about yourself?", "What is your favorite memory from this year?", "Three words your best friend would use to describe you.", "If you wrote a book, what would it be about?", "What makes you unique compared to everyone else?", "What is something you are really good at?", "What do you want to be remembered for?", "Describe your personality using only colors.", "What is your love language? How do you show love?", "What is on your bucket list before age 18?", "What song is the soundtrack of your life right now?", "If you could meet anyone alive, who and what would you ask?", "What scares you but also excites you?", "Describe the perfect version of your future life."]),
        ("Feelings & Emotions", ["What emotion do you feel most often? Why?", "When was the last time you cried? What happened?", "What makes you feel safe and calm?", "Describe a time you felt really angry. How did you handle it?", "What worries you most right now?", "When do you feel happiest?", "How do you act when you are nervous?", "What helps you feel better when you are sad?", "Describe a time you felt brave.", "What emotion is hardest for you to express?", "How do you want people to treat you when you are upset?", "What would you tell your past self about handling feelings?", "Draw or describe what anxiety looks like to you.", "What are 3 things that always make you smile?", "How do you know when you need alone time?", "What does confidence feel like in your body?", "When have you felt most peaceful?", "How do you calm yourself down?", "What feeling do you wish you could feel more often?", "Write about a time you surprised yourself with your strength."]),
        ("Friends & Relationships", ["What qualities do you look for in a friend?", "Describe your best friendship. What makes it special?", "How do you handle disagreements with friends?", "Have you ever lost a friendship? What happened?", "What is the kindest thing a friend has done for you?", "How do you make new friends?", "What does loyalty mean to you?", "Describe a time a friend really understood you.", "How do you handle it when friends leave you out?", "What boundary do you need to set with someone?", "Who is someone you want to get to know better?", "How has a friend changed your life for the better?", "What do you bring to your friendships?", "Have you ever been a bad friend? What did you learn?", "What is the difference between a friend and a best friend?", "How do you support a friend who is going through something hard?", "What friendship red flags have you learned to watch for?", "Describe your perfect friend group hangout.", "Who do you feel most yourself around? Why?", "Write a thank-you letter to your best friend."]),
        ("School & Learning", ["What subject interests you most? Why?", "Describe your favorite teacher and what makes them great.", "What is the hardest thing about school right now?", "How do you learn best (visual, audio, hands-on)?", "What goal are you working toward in school?", "Describe a time you overcame a learning challenge.", "If you could change one thing about school, what would it be?", "What extracurricular activities do you love?", "How do you handle test anxiety?", "What have you learned outside of school that matters more?", "Describe a project you were really proud of.", "What do you want to study in college?", "Who inspires you academically?", "How do you stay motivated when school is boring?", "What skill would you love to develop?", "Describe your ideal learning environment.", "What class do you wish your school offered?", "How do you balance school with the rest of your life?", "What is something you learned this week?", "Write about a mistake that taught you something valuable."]),
        ("Dreams & Goals", ["What is your biggest dream for your life?", "Where do you see yourself in 5 years?", "What would you do if you knew you could not fail?", "What goal scares you the most?", "What steps can you take THIS WEEK toward your dream?", "Who has achieved something similar to your dream?", "What obstacles stand between you and your goal?", "How will you feel when you achieve your biggest dream?", "What small goal can you accomplish this month?", "What would your ideal career look like day-to-day?", "What legacy do you want to leave?", "If money was not an issue, how would you spend your life?", "What is a dream you have given up on? Should you try again?", "What skills do you need to develop for your dreams?", "Who can help you get closer to your goals?", "What is one thing you can do today toward your future?", "Describe your dream home in detail.", "What does success mean to YOU (not to others)?", "What would you tell your future self?", "Write your dream life as if it has already happened."]),
        ("Creativity", ["Draw something that represents your current mood.", "Write a short poem about today.", "Create a new word and define it.", "Design your dream bedroom in detail.", "Write a story in exactly 50 words.", "If you could create any invention, what would it be?", "Draw a map of your ideal fantasy world.", "Write a song about something that matters to you.", "Create a new holiday. What would it celebrate?", "Design a logo that represents who you are.", "Write a letter to your future self at age 25.", "Create a recipe for happiness (list the ingredients).", "Draw your family as animals. Which animal is each person?", "Write about a dream you had recently.", "Create a playlist of songs that tell your life story.", "Design your dream app. What would it do?", "Write a fairy tale with yourself as the hero.", "Create your personal coat of arms with symbols.", "Draw what your emotions look like as weather.", "Write a letter to someone who needs encouragement."]),
        ("Gratitude & Positivity", ["List 10 things you are grateful for today.", "Who made you smile this week? Write them a thank-you.", "What is something beautiful you noticed today?", "What is something about your life that others might envy?", "Name 3 things your body did for you today.", "What is a challenge that made you stronger?", "Who is someone you appreciate but rarely thank?", "What is a simple pleasure that makes your day better?", "What is going RIGHT in your life right now?", "Describe a kindness you witnessed recently.", "What is something about today that was better than yesterday?", "List 5 things about yourself you are grateful for.", "What is a lesson you are grateful you learned?", "Who has helped you become who you are?", "What place makes you feel most grateful?", "What ability or talent are you thankful for?", "Describe a hard time that you are now grateful for.", "What small thing brought you joy today?", "Write about someone who changed your life for the better.", "If you lost everything, what would you miss most?"])
    ]


    affirmations = ["I am enough exactly as I am.", "My feelings are valid.", "I deserve good friendships.", "I am capable of amazing things.", "My voice matters.", "I choose joy today.", "I am growing every day."]

    # Title page
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(640, "MY AMAZING LIFE", 'F2', 30, 0.1)
    doc.add_line(150, 620, 462, 620, 2, 0.3)
    doc.add_centered_text(585, "A Guided Journal for Girls Ages 9-14", 'F4', 16, 0.3)
    doc.add_centered_text(555, "365 Prompts for Self-Discovery", 'F4', 14, 0.4)
    doc.add_centered_text(100, author, 'F2', 14, 0.2)
    doc.new_page()
    # Copyright
    doc.add_centered_text(700, "MY AMAZING LIFE", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Author: {author}", 'F1', 11, 0.3)
    doc.add_text(72, 630, "Format: 8.5 x 11 inches | Kindle & Paperback", 'F1', 10, 0.4)
    doc.add_text(72, 600, "All rights reserved.", 'F1', 10, 0.4)
    doc.new_page()
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0.1)
    doc.add_line(72, 705, 540, 705, 1, 0.3)
    y = 680
    for i, (theme, _) in enumerate(themes):
        doc.add_text(72, y, f"Weeks {i*4+1}-{i*4+4}: {theme}", 'F2', 12, 0.2)
        y -= 25
    doc.new_page()

    # Journal pages - 5 prompts per page with writing space
    page_count = 0
    for t_idx, (theme, prompts) in enumerate(themes):
        # Theme header
        doc.add_filled_rect(50, 710, 512, 50, 0.92)
        doc.add_centered_text(740, f"Weeks {t_idx*4+1}-{t_idx*4+4}", 'F1', 10, 0.5)
        doc.add_centered_text(720, theme.upper(), 'F2', 18, 0.1)
        doc.new_page()
        page_count += 1

        # Each page has 4-5 prompts with lines
        for p_idx in range(0, len(prompts), 4):
            batch = prompts[p_idx:p_idx+4]
            y = 730
            for prompt in batch:
                doc.add_text(72, y, prompt, 'F2', 10, 0.2)
                y -= 15
                for j in range(3):
                    doc.add_line(72, y, 540, y, 0.5, 0.75)
                    y -= 18
                y -= 12
            # Affirmation at bottom
            aff = affirmations[t_idx % len(affirmations)]
            doc.add_filled_rect(72, 60, 468, 25, 0.93)
            doc.add_centered_text(70, aff, 'F5', 10, 0.3)
            doc.new_page()
            page_count += 1

    # Extra pages to reach 78+
    while page_count < 76:
        doc.add_centered_text(740, "FREE WRITING SPACE", 'F2', 14, 0.2)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        y = 700
        for j in range(25):
            doc.add_line(72, y, 540, y, 0.5, 0.75)
            y -= 25
        doc.new_page()
        page_count += 1

    # Final page
    doc.add_centered_text(600, "YOUR STORY IS BEAUTIFUL", 'F2', 20, 0.1)
    doc.add_centered_text(560, "Keep writing. Keep growing. Keep being amazing.", 'F4', 13, 0.3)
    doc.new_page()
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book355_Girls_Daily_Journal.pdf')
    print("Book355_Girls_Daily_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
