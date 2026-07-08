from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(550, "SOCIAL MEDIA CONTENT PLANNER", 'F2', 18)
pdf.add_centered_text(520, "90 Days of Strategy for Small Business", 'F4', 14)
pdf.add_centered_text(400, "Plan, Create, Post, and Grow", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: Brand Voice Worksheet
pdf.new_page()
pdf.add_centered_text(750, "BRAND VOICE WORKSHEET", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Your brand voice is HOW you communicate. It should be consistent.", "",
    "MY BRAND PERSONALITY (choose 3-5 words):",
    "__ Professional  __ Playful  __ Bold  __ Warm  __ Witty",
    "__ Educational  __ Inspirational  __ Casual  __ Luxurious",
    "__ Authentic  __ Empowering  __ Fun  __ Minimal", "",
    "My brand voice is: _________, _________, _________", "",
    "WE ARE:                          WE ARE NOT:",
    "______________________________  ______________________________",
    "______________________________  ______________________________",
    "______________________________  ______________________________", "",
    "VOCABULARY WE USE:              VOCABULARY WE AVOID:",
    "______________________________  ______________________________",
    "______________________________  ______________________________", "",
    "TONE GUIDELINES:",
    "When educating: _______________________________",
    "When selling: _________________________________",
    "When responding to comments: ___________________",
    "When addressing problems: _____________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 4: Content Pillars
pdf.new_page()
pdf.add_centered_text(750, "CONTENT PILLARS DEFINITION", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Content pillars are 3-5 core topics you consistently post about.", "",
    "PILLAR 1: ____________________________________",
    "What it covers: _______________________________",
    "Content ideas: ________________________________",
    "% of content: ___%", "",
    "PILLAR 2: ____________________________________",
    "What it covers: _______________________________",
    "Content ideas: ________________________________",
    "% of content: ___%", "",
    "PILLAR 3: ____________________________________",
    "What it covers: _______________________________",
    "Content ideas: ________________________________",
    "% of content: ___%", "",
    "PILLAR 4: ____________________________________",
    "What it covers: _______________________________",
    "Content ideas: ________________________________",
    "% of content: ___%", "",
    "CONTENT MIX RULE OF THUMB:",
    "80% value (educate/entertain/inspire)",
    "20% promotion (sell/CTA)"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 5: Target Audience
pdf.new_page()
pdf.add_centered_text(750, "TARGET AUDIENCE PROFILE", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "WHO IS YOUR IDEAL FOLLOWER/CUSTOMER?", "",
    "Demographics:",
    "Age range: _______ Gender: _______ Location: ______",
    "Income: _________ Education: ___________________",
    "Job/role: _____________________________________", "",
    "Pain points (problems they have):",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________", "",
    "Goals/desires:",
    "1. ____________________________________________",
    "2. ____________________________________________", "",
    "Online behavior:",
    "Most active time: _______ Platform preference: _____",
    "Content they engage with: _____________________",
    "Accounts they follow: _________________________",
    "Hashtags they use: ____________________________", "",
    "HOW MY CONTENT HELPS THEM:",
    "My content solves: ____________________________",
    "After following me, they will feel: ______________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 6: Platform Strategy
pdf.new_page()
pdf.add_centered_text(750, "PLATFORM STRATEGY", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "You don't need to be everywhere. Choose 1-2 platforms to master.", "",
    "PLATFORM     BEST FOR              MY PLAN",
    "Instagram    Visual brands, lifestyle  _____________",
    "TikTok       Short video, young audience _____________",
    "Facebook     Local biz, communities, 35+ _____________",
    "LinkedIn     B2B, professional services _____________",
    "Pinterest    DIY, recipes, visual search _____________",
    "YouTube      Long-form education, SEO    _____________",
    "Twitter/X    News, tech, real-time       _____________", "",
    "MY PRIMARY PLATFORM: __________________________",
    "Why: __________________________________________",
    "Post frequency: _______/week", "",
    "MY SECONDARY PLATFORM: ________________________",
    "Why: __________________________________________",
    "Post frequency: _______/week", "",
    "CONTENT FORMAT FOCUS:",
    "__ Reels/Short video  __ Carousels  __ Stories",
    "__ Long video  __ Static images  __ Text posts",
    "__ Live streams  __ Threads/Articles"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Pages 7-9: Monthly Content Calendar (3 months)
for month in range(1, 4):
    pdf.new_page()
    pdf.add_centered_text(755, f"CONTENT CALENDAR - MONTH {month}", 'F2', 14)
    pdf.add_line(60, 743, 552, 743)
    y = 728
    pdf.add_text(60, y, "Month: _____________ Theme: ___________________", 'F4', 10)
    y -= 18
    days_header = "Mon      Tue      Wed      Thu      Fri      Sat      Sun"
    pdf.add_text(60, y, days_header, 'F2', 9)
    y -= 5
    pdf.add_line(60, y, 552, y, 0.5)
    y -= 5
    for week in range(5):
        for col in range(7):
            x = 60 + col * 71
            pdf.add_rect(x, y - 40, 68, 40, 0.3)
        y -= 45

# Pages 10-21: Weekly Content Batching Planner (12 weeks)
for week in range(1, 13):
    pdf.new_page()
    pdf.add_centered_text(755, f"WEEKLY CONTENT PLAN - WEEK {week}", 'F2', 13)
    pdf.add_line(60, 743, 552, 743)
    y = 728
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    for day in days:
        pdf.add_text(60, y, f"{day}:", 'F2', 9)
        y -= 13
        pdf.add_text(75, y, "Type: _____ Caption idea: _____________________", 'F3', 8)
        y -= 12
        pdf.add_text(75, y, "Hashtags: _____________ CTA: _________________", 'F3', 8)
        y -= 15
        pdf.add_line(60, y+4, 552, y+4, 0.3, 0.7)
        y -= 6

# Page 22: Analytics Tracking
pdf.new_page()
pdf.add_centered_text(750, "MONTHLY ANALYTICS TRACKING", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
pdf.add_text(60, y, "Track these numbers monthly to measure growth:", 'F4', 10)
y -= 20
headers = "Metric              Month 1    Month 2    Month 3"
pdf.add_text(60, y, headers, 'F2', 9)
y -= 5
pdf.add_line(60, y, 552, y, 0.5)
y -= 15
metrics = ["Followers", "Engagement rate", "Reach/Impressions", "Profile visits",
    "Website clicks", "Saves/Shares", "DMs received", "Sales from social"]
for m in metrics:
    pdf.add_text(60, y, f"{m:<22} ________   ________   ________", 'F3', 9)
    y -= 18

# Page 23: Content Ideas (100 prompts) + Hashtag + Engagement
pdf.new_page()
pdf.add_centered_text(750, "100 POST IDEA PROMPTS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
prompts = [
    "1. Share your origin story", "2. Behind the scenes of your day",
    "3. Client testimonial", "4. Day in the life", "5. FAQ answer",
    "6. Myth vs fact in your industry", "7. Tool/resource recommendation",
    "8. Before and after", "9. How-to tutorial", "10. Your biggest mistake",
    "11. Unpopular opinion", "12. Fill in the blank prompt",
    "13. This or that poll", "14. Product/service showcase",
    "15. Customer spotlight", "16. Workspace tour",
    "17. 5 tips for beginners", "18. What I wish I knew when starting",
    "19. Share a win", "20. Ask a question to followers",
    "21. Trending audio + your niche", "22. Comparison post",
    "23. Listicle/carousel", "24. Motivational quote + your take",
    "25. Free resource/download", "26. Repost user-generated content",
    "27. Show your process", "28. Celebrate a milestone",
    "29. Seasonal/holiday content", "30. Collab/duet with another creator"
]
for p in prompts:
    pdf.add_text(60, y, p, 'F4', 9)
    y -= 14

# Page 24: 90-Day Goals
pdf.new_page()
pdf.add_centered_text(750, "90-DAY SOCIAL MEDIA GOALS & KPIs", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "FOLLOWER GOAL:", "",
    "Current followers: _________  Goal: ___________",
    "Growth needed: _________ (___/week)", "",
    "ENGAGEMENT GOAL:",
    "Current rate: _________%  Goal: _________%", "",
    "REVENUE GOAL FROM SOCIAL:",
    "Current: $________  Goal: $________", "",
    "CONTENT CREATION GOAL:",
    "Posts per week: _____ Stories per day: _____",
    "Reels per week: _____ Lives per month: _____", "",
    "MY 3 BIGGEST PRIORITIES:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________", "",
    "WHAT SUCCESS LOOKS LIKE IN 90 DAYS:",
    "_______________________________________________",
    "_______________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book113_Social_Media_Planner.pdf')
print("Book113_Social_Media_Planner.pdf created successfully!")
