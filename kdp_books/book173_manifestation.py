from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1: Title Page
pdf.new_page()
pdf.add_filled_rect(0, 0, 432, 648, gray=0.95)
pdf.add_centered_text(440, "MANIFEST YOUR", "F2", 22)
pdf.add_centered_text(410, "DREAM LIFE", "F2", 22)
pdf.add_line(120, 395, 312, 395, 2, gray=0.5)
pdf.add_centered_text(360, "A 90-Day Law of Attraction", "F4", 14, gray=0.3)
pdf.add_centered_text(340, "Workbook", "F4", 14, gray=0.3)
pdf.add_centered_text(290, "Align Your Thoughts, Beliefs & Actions", "F1", 11, gray=0.4)
pdf.add_centered_text(270, "with Your Highest Vision", "F1", 11, gray=0.4)
pdf.add_centered_text(180, author, "F2", 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(420, "MANIFEST YOUR DREAM LIFE", "F2", 13)
pdf.add_centered_text(400, "A 90-Day Law of Attraction Workbook", "F4", 11)
pdf.add_centered_text(365, f"Copyright (c) 2025 {author}", "F1", 10)
pdf.add_centered_text(347, "All rights reserved.", "F1", 10)
pdf.add_centered_text(315, "This workbook is for personal development purposes only.", "F1", 9)
pdf.add_centered_text(300, "Results may vary based on individual commitment and action.", "F1", 9)
pdf.add_centered_text(270, "ISBN: 979-8-XXX-XXXXX-X", "F3", 9)

# Page 3: How Manifestation Works
pdf.new_page()
pdf.add_centered_text(610, "HOW MANIFESTATION WORKS", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Manifestation is the practice of turning your thoughts,", "F1", 11)
pdf.add_text(40, 555, "beliefs, and energy into reality through focused intention", "F1", 11)
pdf.add_text(40, 538, "and aligned action.", "F1", 11)
pdf.add_text(40, 508, "The Core Principles:", "F2", 12)
pdf.add_filled_rect(40, 475, 352, 25, gray=0.92)
pdf.add_text(45, 485, "1. THOUGHTS BECOME THINGS", "F2", 10)
pdf.add_text(55, 460, "What you focus on expands. Your dominant thoughts", "F1", 10)
pdf.add_text(55, 445, "shape your reality over time.", "F1", 10)
pdf.add_filled_rect(40, 420, 352, 25, gray=0.92)
pdf.add_text(45, 430, "2. ENERGY ATTRACTS LIKE ENERGY", "F2", 10)
pdf.add_text(55, 405, "Your emotional frequency draws matching experiences.", "F1", 10)
pdf.add_filled_rect(40, 380, 352, 25, gray=0.92)
pdf.add_text(45, 390, "3. CLARITY IS POWER", "F2", 10)
pdf.add_text(55, 365, "The more specific your vision, the easier it manifests.", "F1", 10)
pdf.add_filled_rect(40, 340, 352, 25, gray=0.92)
pdf.add_text(45, 350, "4. BELIEF CREATES POSSIBILITY", "F2", 10)
pdf.add_text(55, 325, "You must believe you deserve what you desire.", "F1", 10)
pdf.add_filled_rect(40, 300, 352, 25, gray=0.92)
pdf.add_text(45, 310, "5. ALIGNED ACTION IS ESSENTIAL", "F2", 10)
pdf.add_text(55, 285, "Manifestation requires action, not just wishing.", "F1", 10)
pdf.add_text(40, 255, "What do you most want to manifest in the next 90 days?", "F2", 11)
pdf.add_line(40, 235, 392, 235, 0.5)
pdf.add_line(40, 215, 392, 215, 0.5)


# Page 4: Getting Clear on What You Want
pdf.new_page()
pdf.add_centered_text(610, "GETTING CLEAR ON WHAT YOU WANT", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "You can't manifest what you haven't clearly defined.", "F1", 11)
pdf.add_text(40, 545, "My dream life in these areas:", "F2", 11)
areas = ["Career/Business:", "Relationships:", "Health/Body:", "Finances:", "Personal Growth:", "Home/Living:"]
y = 520
for area in areas:
    pdf.add_text(40, y, area, "F2", 10)
    pdf.add_line(40, y - 16, 392, y - 16, 0.5)
    pdf.add_line(40, y - 34, 392, y - 34, 0.5)
    y -= 60
pdf.add_text(40, y, "My #1 focus for these 90 days:", "F2", 11)
pdf.add_rect(40, y - 50, 352, 40)

# Pages 5-7: Limiting Beliefs (3 pages)
beliefs_titles = ["IDENTIFYING LIMITING BELIEFS", "REWRITING LIMITING BELIEFS", "BELIEF TRANSFORMATION"]
for pg in range(3):
    pdf.new_page()
    pdf.add_centered_text(610, beliefs_titles[pg], "F2", 16)
    pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
    if pg == 0:
        pdf.add_text(40, 572, "Limiting beliefs are lies you've told yourself for so long", "F1", 11)
        pdf.add_text(40, 555, "they feel like truth. Let's uncover them:", "F1", 11)
        prompts = [
            "I'm not good enough to...",
            "I don't deserve...",
            "Money is...",
            "People like me can't...",
            "I'll never be able to...",
            "Success requires...",
            "Love means..."
        ]
        y = 525
        for p in prompts:
            pdf.add_text(40, y, p, "F4", 10)
            pdf.add_line(40, y - 16, 392, y - 16, 0.5)
            y -= 38
    elif pg == 1:
        pdf.add_text(40, 572, "For each limiting belief, write a new empowering belief:", "F1", 11)
        y = 545
        for i in range(6):
            pdf.add_text(40, y, f"Old Belief {i+1}:", "F2", 10)
            pdf.add_line(140, y, 392, y, 0.5)
            pdf.add_text(40, y - 22, "New Belief:", "F2", 10)
            pdf.add_line(140, y - 22, 392, y - 22, 0.5)
            pdf.add_text(40, y - 42, "Evidence it's possible:", "F1", 9, gray=0.4)
            pdf.add_line(180, y - 42, 392, y - 42, 0.5)
            y -= 70
    else:
        pdf.add_text(40, 572, "Daily belief work: Read your new beliefs every morning.", "F1", 11)
        pdf.add_text(40, 545, "Rate how much you believe each new belief (1-10):", "F2", 11)
        pdf.add_text(40, 520, "Week 1 ratings:", "F1", 10)
        for i in range(5):
            pdf.add_text(50, 498 - i*18, f"Belief {i+1}: ___/10", "F1", 10)
        pdf.add_text(40, 390, "Week 4 ratings:", "F1", 10)
        for i in range(5):
            pdf.add_text(50, 368 - i*18, f"Belief {i+1}: ___/10", "F1", 10)
        pdf.add_text(40, 260, "Week 8 ratings:", "F1", 10)
        for i in range(5):
            pdf.add_text(50, 238 - i*18, f"Belief {i+1}: ___/10", "F1", 10)


# Pages 8-12: Scripting Exercises (5 pages)
for pg in range(5):
    pdf.new_page()
    pdf.add_centered_text(610, f"SCRIPTING EXERCISE ({pg+1}/5)", "F2", 16)
    pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
    topics = [
        "Write about your ideal day 1 year from now (present tense, as if it's real):",
        "Describe your dream career/business as if you already have it:",
        "Write about your ideal relationship/social life as if it's happening now:",
        "Describe your financial freedom as if it's your current reality:",
        "Write a letter from your future self thanking you for taking action:"
    ]
    pdf.add_text(40, 572, topics[pg], "F2", 10)
    pdf.add_text(40, 552, "Write in present tense. Feel the emotions. Be specific.", "F1", 9, gray=0.4)
    y = 530
    for i in range(22):
        pdf.add_line(40, y, 392, y, 0.5)
        y -= 22

# Page 13: Daily Affirmation Creation
pdf.new_page()
pdf.add_centered_text(610, "CREATING YOUR DAILY AFFIRMATIONS", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Affirmations work best when they are:", "F1", 11)
pdf.add_text(50, 550, "- Present tense ('I am' not 'I will be')", "F1", 10)
pdf.add_text(50, 532, "- Positive ('I am healthy' not 'I'm not sick')", "F1", 10)
pdf.add_text(50, 514, "- Specific and personal to YOU", "F1", 10)
pdf.add_text(50, 496, "- Emotionally charged (feel them!)", "F1", 10)
pdf.add_text(40, 466, "My Power Affirmations:", "F2", 12)
y = 442
for i in range(10):
    pdf.add_text(40, y, f"{i+1}.", "F2", 10)
    pdf.add_line(55, y, 392, y, 0.5)
    y -= 28
pdf.add_text(40, y - 10, "Say these out loud every morning with FEELING.", "F4", 10, gray=0.3)
pdf.add_text(40, y - 30, "Best time to say affirmations: right after waking", "F1", 10)
pdf.add_text(40, y - 48, "and right before sleep.", "F1", 10)

# Page 14: Visualization Practice
pdf.new_page()
pdf.add_centered_text(610, "VISUALIZATION PRACTICE", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Visualization = mental rehearsal of your desired outcome.", "F1", 11)
pdf.add_text(40, 545, "Daily Visualization Steps:", "F2", 11)
steps = [
    "1. Close your eyes. Take 3 deep breaths.",
    "2. See your desired outcome clearly (like a movie).",
    "3. Add details: colors, sounds, people, smells.",
    "4. FEEL the emotions of having it NOW.",
    "5. Hold this feeling for 5-10 minutes.",
    "6. Release and trust the process.",
    "7. Take one aligned action today."
]
y = 518
for step in steps:
    pdf.add_text(50, y, step, "F1", 10)
    y -= 22
pdf.add_text(40, y - 15, "After visualizing, write what you saw and felt:", "F2", 11)
y -= 35
for i in range(8):
    pdf.add_line(40, y, 392, y, 0.5)
    y -= 20


# Page 15: Gratitude as Fuel
pdf.new_page()
pdf.add_centered_text(610, "GRATITUDE AS FUEL", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Gratitude raises your vibration instantly. It tells the universe:", "F1", 11)
pdf.add_text(40, 555, "'I'm ready for MORE good things.'", "F4", 11, gray=0.3)
pdf.add_text(40, 525, "Morning Gratitude (things you HAVE):", "F2", 11)
for i in range(5):
    pdf.add_text(50, 500 - i*20, f"{i+1}. I'm grateful for:", "F1", 10)
    pdf.add_line(170, 500 - i*20, 392, 500 - i*20, 0.5)
pdf.add_text(40, 385, "Future Gratitude (things you're manifesting as if here):", "F2", 11)
for i in range(5):
    pdf.add_text(50, 360 - i*20, f"{i+1}. Thank you for:", "F1", 10)
    pdf.add_line(170, 360 - i*20, 392, 360 - i*20, 0.5)
pdf.add_text(40, 245, "How does gratitude make me feel?", "F1", 11)
pdf.add_line(40, 225, 392, 225, 0.5)
pdf.add_line(40, 205, 392, 205, 0.5)

# Page 16: Aligned Action Planning
pdf.new_page()
pdf.add_centered_text(610, "ALIGNED ACTION PLANNING", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Manifestation without action is just daydreaming.", "F1", 11)
pdf.add_text(40, 552, "What ACTIONS align with your desires?", "F2", 11)
pdf.add_text(40, 525, "My Big Goal:", "F2", 11)
pdf.add_line(40, 505, 392, 505, 0.5)
pdf.add_text(40, 480, "3 actions I can take THIS WEEK:", "F2", 11)
for i in range(3):
    pdf.add_text(50, 455 - i*25, f"{i+1}.", "F1", 10)
    pdf.add_line(65, 455 - i*25, 392, 455 - i*25, 0.5)
pdf.add_text(40, 370, "3 actions I can take THIS MONTH:", "F2", 11)
for i in range(3):
    pdf.add_text(50, 345 - i*25, f"{i+1}.", "F1", 10)
    pdf.add_line(65, 345 - i*25, 392, 345 - i*25, 0.5)
pdf.add_text(40, 260, "What feels scary but exciting? (That's your aligned action!)", "F2", 10)
pdf.add_line(40, 240, 392, 240, 0.5)
pdf.add_line(40, 220, 392, 220, 0.5)
pdf.add_text(40, 190, "One 'inspired action' I took today:", "F1", 11)
pdf.add_line(40, 170, 392, 170, 0.5)

# Pages 17-26: 90-Day Tracker (10 pages, 9 days per page)
for tracker_page in range(10):
    pdf.new_page()
    day_start = tracker_page * 9 + 1
    day_end = min(day_start + 8, 90)
    pdf.add_centered_text(615, f"90-DAY MANIFESTATION TRACKER", "F2", 13)
    pdf.add_text(300, 615, f"Days {day_start}-{day_end}", "F1", 10)
    pdf.add_line(40, 603, 392, 603, 1, gray=0.7)
    
    y = 585
    for day_offset in range(9):
        day_num = day_start + day_offset
        if day_num > 90:
            break
        pdf.add_filled_rect(40, y - 3, 352, 14, gray=0.92)
        pdf.add_text(42, y, f"DAY {day_num}", "F2", 8)
        pdf.add_text(90, y, "Date:___", "F1", 7)
        y -= 16
        pdf.add_text(42, y, "Intention:", "F1", 7)
        pdf.add_line(85, y, 250, y, 0.3)
        pdf.add_text(255, y, "Affirmation: Y/N", "F1", 7)
        y -= 14
        pdf.add_text(42, y, "Action:", "F1", 7)
        pdf.add_line(75, y, 250, y, 0.3)
        pdf.add_text(255, y, "Signs:", "F1", 7)
        pdf.add_line(285, y, 392, y, 0.3)
        y -= 14
        pdf.add_text(42, y, "Gratitude:", "F1", 7)
        pdf.add_line(90, y, 392, y, 0.3)
        y -= 20


# Page 27: Moon Phase Rituals
pdf.new_page()
pdf.add_centered_text(610, "MOON PHASE RITUALS", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Work with the moon's energy to amplify your manifesting:", "F1", 11)
pdf.add_filled_rect(40, 538, 352, 28, gray=0.92)
pdf.add_text(45, 550, "NEW MOON - Set intentions, plant seeds", "F2", 10)
pdf.add_text(50, 515, "My new moon intention:", "F1", 10)
pdf.add_line(50, 498, 392, 498, 0.5)
pdf.add_filled_rect(40, 472, 352, 28, gray=0.92)
pdf.add_text(45, 484, "WAXING MOON - Take action, build momentum", "F2", 10)
pdf.add_text(50, 449, "Actions I'm taking:", "F1", 10)
pdf.add_line(50, 432, 392, 432, 0.5)
pdf.add_filled_rect(40, 406, 352, 28, gray=0.92)
pdf.add_text(45, 418, "FULL MOON - Celebrate, express gratitude", "F2", 10)
pdf.add_text(50, 383, "What I'm celebrating:", "F1", 10)
pdf.add_line(50, 366, 392, 366, 0.5)
pdf.add_filled_rect(40, 340, 352, 28, gray=0.92)
pdf.add_text(45, 352, "WANING MOON - Release, let go, clear space", "F2", 10)
pdf.add_text(50, 317, "What I'm releasing:", "F1", 10)
pdf.add_line(50, 300, 392, 300, 0.5)
pdf.add_text(40, 265, "Full Moon Ritual: Write what no longer serves you on paper.", "F4", 10, gray=0.3)
pdf.add_text(40, 248, "Safely burn it or tear it up. Release with love.", "F4", 10, gray=0.3)

# Page 28: Letting Go Exercises
pdf.new_page()
pdf.add_centered_text(610, "THE ART OF LETTING GO", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Manifestation requires releasing attachment to HOW and WHEN.", "F1", 11)
pdf.add_text(40, 545, "What I'm trying to control:", "F2", 11)
pdf.add_line(40, 525, 392, 525, 0.5)
pdf.add_line(40, 505, 392, 505, 0.5)
pdf.add_text(40, 478, "What I can ACTUALLY control:", "F2", 11)
pdf.add_text(50, 458, "- My thoughts and beliefs", "F1", 10)
pdf.add_text(50, 440, "- My daily actions", "F1", 10)
pdf.add_text(50, 422, "- My energy and attitude", "F1", 10)
pdf.add_text(50, 404, "- Who I surround myself with", "F1", 10)
pdf.add_text(40, 375, "Letting Go Affirmation:", "F2", 11)
pdf.add_text(40, 355, "'I trust that what is meant for me will find me.", "F4", 10)
pdf.add_text(40, 338, "I release the need to control the timing.'", "F4", 10)
pdf.add_text(40, 308, "What would feel lighter if I released it?", "F1", 11)
pdf.add_line(40, 288, 392, 288, 0.5)
pdf.add_line(40, 268, 392, 268, 0.5)
pdf.add_text(40, 240, "Surrender practice: Write 'I trust' 10 times:", "F2", 10)
y = 218
for i in range(5):
    pdf.add_line(40, y, 200, y, 0.5)
    pdf.add_line(210, y, 392, y, 0.5)
    y -= 18

# Page 29: 30/60/90 Day Check-In
pdf.new_page()
pdf.add_centered_text(610, "30 / 60 / 90 DAY CHECK-IN", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_filled_rect(40, 565, 352, 22, gray=0.88)
pdf.add_text(45, 572, "30-DAY CHECK-IN", "F2", 11)
pdf.add_text(40, 545, "What's shifted in my life?", "F1", 10)
pdf.add_line(40, 528, 392, 528, 0.5)
pdf.add_text(40, 508, "Signs the universe has sent:", "F1", 10)
pdf.add_line(40, 491, 392, 491, 0.5)
pdf.add_text(40, 471, "Belief level now (1-10): ___", "F1", 10)
pdf.add_filled_rect(40, 440, 352, 22, gray=0.88)
pdf.add_text(45, 447, "60-DAY CHECK-IN", "F2", 11)
pdf.add_text(40, 420, "What's shifted in my life?", "F1", 10)
pdf.add_line(40, 403, 392, 403, 0.5)
pdf.add_text(40, 383, "Manifestations received (big or small):", "F1", 10)
pdf.add_line(40, 366, 392, 366, 0.5)
pdf.add_text(40, 346, "Belief level now (1-10): ___", "F1", 10)
pdf.add_filled_rect(40, 315, 352, 22, gray=0.88)
pdf.add_text(45, 322, "90-DAY CHECK-IN", "F2", 11)
pdf.add_text(40, 295, "What's shifted in my life?", "F1", 10)
pdf.add_line(40, 278, 392, 278, 0.5)
pdf.add_text(40, 258, "Did I manifest my big goal? Y/N/In Progress", "F1", 10)
pdf.add_text(40, 238, "Biggest lesson learned:", "F1", 10)
pdf.add_line(40, 218, 392, 218, 0.5)
pdf.add_text(40, 198, "Next 90-day intention:", "F1", 10)
pdf.add_line(40, 178, 392, 178, 0.5)

# Page 30: Success Stories
pdf.new_page()
pdf.add_centered_text(610, "MY MANIFESTATION SUCCESS STORIES", "F2", 16)
pdf.add_line(40, 597, 392, 597, 1, gray=0.7)
pdf.add_text(40, 572, "Document every win - big or small. Proof builds belief!", "F1", 11)
y = 545
for i in range(6):
    pdf.add_filled_rect(40, y - 3, 352, 16, gray=0.92)
    pdf.add_text(42, y, f"SUCCESS #{i+1}", "F2", 9)
    pdf.add_text(120, y, "Date: ___/___/___", "F1", 8)
    y -= 18
    pdf.add_text(42, y, "What manifested:", "F1", 9)
    pdf.add_line(130, y, 392, y, 0.5)
    y -= 16
    pdf.add_text(42, y, "How I felt:", "F1", 9)
    pdf.add_line(100, y, 392, y, 0.5)
    y -= 16
    pdf.add_text(42, y, "What I did to align:", "F1", 9)
    pdf.add_line(140, y, 392, y, 0.5)
    y -= 25
pdf.add_filled_rect(40, 90, 352, 30, gray=0.92)
pdf.add_text(50, 108, "You are a powerful creator. Keep manifesting!", "F2", 10)
pdf.add_text(50, 93, f"- {author}", "F4", 10, gray=0.4)

pdf.save("Book173_Manifestation_Workbook.pdf")
print("SUCCESS: Book173_Manifestation_Workbook.pdf created (30 pages)")
