"""Book347: Between Us - A Mother-Daughter Journal"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc()
    author = "Daniel Tesfamariam"
    
    prompts = [
        "My happiest memory of us together is...",
        "Something I admire about you is...",
        "What I wish you knew about me...",
        "Our funniest moment together was...",
        "What scares me right now is...",
        "My dream for your future is...",
        "When I feel sad I wish you would...",
        "The best advice you ever gave me was...",
        "Something that made me proud of you recently...",
        "A tradition I want us to always keep...",
        "If we could travel anywhere together...",
        "The song that reminds me of you is...",
        "Something I have never told you...",
        "My favorite thing we do together is...",
        "When I grow up I want to be like you because...",
        "The hardest part of my day is...",
        "Something that always makes us laugh...",
        "If I could give you one gift it would be...",
        "The way you show love is...",
        "A challenge I am facing right now...",
        "What home means to me...",
        "My favorite meal you make is...",
        "Something I want to learn together...",
        "The best surprise you ever gave me...",
        "When I need comfort I...",
        "Something about our family I love...",
        "A goal I am working toward...",
        "What makes me feel brave...",
        "My favorite bedtime memory...",
        "The quality I most want to develop...",
        "Something I am grateful for today...",
        "A book or movie that changed how I think...",
        "What friendship means to me...",
        "The kindest thing someone did for me...",
        "What I think about before falling asleep...",
        "My favorite season and why...",
        "Something I wish I could change about the world...",
        "A moment I felt truly happy...",
        "What I love about our home...",
        "Something that made me cry happy tears...",
        "The person outside our family I admire most...",
        "What I want you to know about my friends...",
        "A skill I want to learn this year...",
        "My biggest accomplishment so far...",
        "Something I find really hard to talk about...",
        "What makes our bond special...",
        "A promise I want to make to you...",
        "The funniest thing that happened this week...",
        "What I need more of in my life...",
        "Something beautiful I noticed today...",
        "My definition of success is...",
        "A fear I am trying to overcome...",
        "What forgiveness means to me...",
        "The best part of being a mother/daughter...",
        "Something I want to do before next year...",
        "What I love about myself...",
        "A moment I felt close to you...",
        "What I hope we never stop doing...",
        "My wish for our relationship...",
        "A letter to you ten years from now..."
    ]
    
    discussion_nudges = [
        "Find a quiet moment today to share your answers face to face.",
        "Read each other's response and give a hug before discussing.",
        "Take turns reading aloud what you wrote. Listen without interrupting.",
        "After sharing, tell each other one new thing you learned.",
        "Discuss this over your favorite shared snack.",
        "Go for a walk together and talk about what you wrote.",
        "Set a timer for 10 minutes of uninterrupted sharing time.",
        "Light a candle and create a cozy moment to discuss this.",
        "Share your answers, then write a one-sentence summary together.",
        "Take turns asking follow-up questions about each other's answers."
    ]
    
    # Title page
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(650, "BETWEEN US", 'F2', 34, 0.1)
    doc.add_line(150, 630, 462, 630, 2, 0.3)
    doc.add_centered_text(590, "A Mother-Daughter Journal for Sharing", 'F4', 16, 0.3)
    doc.add_centered_text(565, "Thoughts & Building Connection", 'F4', 16, 0.3)
    doc.add_centered_text(530, "(Ages 8-14)", 'F1', 13, 0.4)
    doc.add_centered_text(480, "60 Guided Prompts to Bring You Closer", 'F4', 13, 0.4)
    doc.add_centered_text(100, author, 'F2', 14, 0.2)
    doc.new_page()
    
    # Copyright
    doc.add_centered_text(700, "BETWEEN US", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Author: {author}", 'F1', 11, 0.3)
    doc.add_text(72, 630, "Format: 8.5 x 11 inches | Kindle & Paperback", 'F1', 10, 0.4)
    doc.add_text(72, 600, "All rights reserved.", 'F1', 10, 0.4)
    doc.new_page()
    
    # How to use this journal
    doc.add_centered_text(720, "HOW TO USE THIS JOURNAL", 'F2', 18, 0.1)
    doc.add_line(150, 705, 462, 705, 1, 0.3)
    instructions = [
        "Welcome to your shared space! This journal is designed for a mother",
        "and daughter to write in together, taking turns and sharing your hearts.",
        "",
        "HOW IT WORKS:",
        "",
        "1. Choose a prompt that speaks to you both today.",
        "2. Mom writes her response in the 'Mom's Turn' section.",
        "3. Daughter writes her response in 'Daughter's Turn' section.",
        "4. Read each other's answers when you are both ready.",
        "5. Use the 'Talk About This' discussion nudge to go deeper.",
        "",
        "GROUND RULES:",
        "",
        "- There are no wrong answers. Be honest and open.",
        "- No judging each other's responses. This is a safe space.",
        "- You don't have to share everything. Skip what feels too hard.",
        "- Take your time. There is no rush to finish this journal.",
        "- Come back to prompts you skipped when you feel ready.",
        "",
        "THE MOST IMPORTANT RULE:",
        "",
        "Have fun! This journal is about building your bond,",
        "creating memories, and showing each other love through words.",
        "",
        "Let the conversations begin..."
    ]
    y = 680
    for line in instructions:
        if line == "":
            y -= 10
        elif line.startswith("HOW IT") or line.startswith("GROUND") or line.startswith("THE MOST"):
            doc.add_text(72, y, line, 'F2', 12, 0.2)
            y -= 18
        else:
            doc.add_text(72, y, line, 'F4', 11, 0.3)
            y -= 16
    doc.new_page()
    
    # 60 prompts - each gets about 1.25 pages (mom section + daughter section)
    for idx, prompt in enumerate(prompts):
        nudge = discussion_nudges[idx % len(discussion_nudges)]
        
        # Prompt header with decorative frame
        doc.add_rect(50, 690, 512, 70, 1.5, 0.3)
        doc.add_filled_rect(55, 695, 502, 60, 0.95)
        doc.add_centered_text(735, f"Prompt #{idx+1}", 'F1', 10, 0.5)
        doc.add_centered_text(715, prompt, 'F5', 13, 0.1)
        
        # Mom's section
        doc.add_text(72, 665, "MOM'S TURN", 'F2', 13, 0.2)
        doc.add_line(72, 655, 180, 655, 1, 0.4)
        y = 635
        for j in range(6):
            doc.add_line(72, y, 540, y, 0.5, 0.75)
            y -= 22
        
        # Daughter's section
        y -= 10
        doc.add_text(72, y, "DAUGHTER'S TURN", 'F2', 13, 0.2)
        y -= 10
        doc.add_line(72, y, 220, y, 1, 0.4)
        y -= 20
        for j in range(6):
            doc.add_line(72, y, 540, y, 0.5, 0.75)
            y -= 22
        
        # Discussion nudge
        y -= 10
        doc.add_filled_rect(72, y - 10, 468, 30, 0.93)
        doc.add_text(82, y, "Talk About This:", 'F2', 10, 0.3)
        doc.add_text(180, y, nudge, 'F4', 10, 0.4)
        
        doc.new_page()
    
    # Memory Pages
    doc.add_centered_text(720, "OUR FAVORITE MEMORIES TOGETHER", 'F2', 16, 0.1)
    doc.add_line(100, 705, 512, 705, 1, 0.3)
    doc.add_text(72, 680, "Use these pages to write about your favorite shared memories:", 'F4', 11, 0.3)
    y = 650
    for i in range(1, 11):
        doc.add_text(72, y, f"Memory #{i}:", 'F2', 10, 0.3)
        y -= 5
        for j in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 18
        y -= 10
        if y < 100:
            doc.new_page()
            y = 740
    doc.new_page()
    
    # Closing page
    doc.add_centered_text(600, "This journal belongs to:", 'F4', 14, 0.3)
    doc.add_line(200, 570, 412, 570, 0.5, 0.5)
    doc.add_centered_text(555, "(Mom's name)", 'F1', 9, 0.5)
    doc.add_centered_text(520, "&", 'F4', 16, 0.3)
    doc.add_line(200, 500, 412, 500, 0.5, 0.5)
    doc.add_centered_text(485, "(Daughter's name)", 'F1', 9, 0.5)
    doc.add_centered_text(430, "Started on: _______________", 'F4', 12, 0.3)
    doc.add_centered_text(390, "Our bond is forever.", 'F5', 14, 0.2)
    doc.new_page()
    

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()


    # Extra content pages for 78+ minimum
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "MY ACTION PLAN", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "CREATIVE RESPONSE", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "ADDITIONAL THOUGHTS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "MY ACTION PLAN", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "CREATIVE RESPONSE", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "ADDITIONAL THOUGHTS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book347_Mother_Daughter_Journal.pdf')
    print("Book347_Mother_Daughter_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
