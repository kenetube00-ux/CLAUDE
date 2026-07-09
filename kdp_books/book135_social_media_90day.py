from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "90-DAY SOCIAL MEDIA GROWTH PLAN"
subtitle = "From Zero to Profitable"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 18)
pdf.add_centered_text(515, subtitle, 'F4', 14)
pdf.add_centered_text(440, "A Complete Content Planning & Growth System", 'F4', 11)
pdf.add_centered_text(420, "for Creators, Coaches, and Business Owners", 'F4', 11)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 12)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)


# Page 3: Platform Selection Worksheet
pdf.new_page()
pdf.add_centered_text(750, "PLATFORM SELECTION WORKSHEET", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "You do NOT need to be on every platform. Choose 1-2 to master.", 'F4', 10)
y -= 18
platforms = [
    ("INSTAGRAM", "Visual content, reels, stories", "Best for: lifestyle, fashion, food, coaching, local biz", "Pros: Visual storytelling, reels reach new people easily", "Cons: Algorithm changes frequently, link-in-bio limitation"),
    ("TIKTOK", "Short-form video, trending audio", "Best for: entertainment, education, Gen Z/Millennial audience", "Pros: Massive organic reach, easy to go viral", "Cons: Young demographic, trends change daily, controversial"),
    ("YOUTUBE", "Long-form video, tutorials, vlogs", "Best for: education, how-to, reviews, storytelling", "Pros: Long content shelf life, search engine, ad revenue", "Cons: High production effort, slow growth initially"),
    ("PINTEREST", "Visual search engine, pins, boards", "Best for: DIY, recipes, home, wedding, fashion, templates", "Pros: Evergreen traffic, drives website clicks, passive", "Cons: Not social (no DMs/engagement), slow build"),
    ("LINKEDIN", "Professional networking, articles", "Best for: B2B, coaches, consultants, job seekers", "Pros: High-quality leads, professional audience, organic reach", "Cons: Limited to business content, smaller audience"),
]
for pname, ptype, best_for, pros, cons in platforms:
    pdf.add_text(50, y, pname, 'F2', 10)
    pdf.add_text(140, y, f"({ptype})", 'F4', 8)
    y -= 12
    pdf.add_text(55, y, best_for, 'F4', 8)
    y -= 11
    pdf.add_text(55, y, pros, 'F4', 8)
    y -= 11
    pdf.add_text(55, y, cons, 'F4', 8)
    y -= 16
y -= 5
pdf.add_text(50, y, "MY PRIMARY PLATFORM: _______________________________________", 'F2', 9)
y -= 14
pdf.add_text(50, y, "MY SECONDARY PLATFORM: ____________________________________", 'F2', 9)
y -= 14
pdf.add_text(50, y, "WHY (matches my audience + content style): ___________________", 'F1', 9)


# Page 4: Content Pillar Definition
pdf.new_page()
pdf.add_centered_text(750, "CONTENT PILLAR DEFINITION", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Content pillars = 3-5 core topics you post about consistently.", 'F4', 10)
y -= 14
pdf.add_text(50, y, "Every post should fit ONE pillar. This keeps you focused and recognizable.", 'F4', 10)
y -= 22
for pillar in range(1, 6):
    pdf.add_filled_rect(50, y - 5, 512, 110, 0.95)
    pdf.add_rect(50, y - 5, 512, 110, 0.5, 0.5)
    pdf.add_text(55, y + 90, f"PILLAR {pillar}: _________________________________", 'F2', 10)
    pdf.add_text(55, y + 74, "Why my audience cares about this: _________________________________", 'F1', 8)
    pdf.add_text(55, y + 58, "10 Post Ideas:", 'F2', 8)
    for row in range(2):
        base_y = y + 42 - row * 14
        for col in range(5):
            num = row * 5 + col + 1
            x_pos = 55 + col * 100
            pdf.add_text(x_pos, base_y, f"{num}. ______________", 'F3', 7)
    y -= 125

# Page 5: Ideal Follower Avatar
pdf.new_page()
pdf.add_centered_text(750, "IDEAL FOLLOWER AVATAR", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
avatar = [
    "Who EXACTLY are you creating content for? Be specific.",
    "",
    "DEMOGRAPHICS:",
    "Age range: _________  Gender: _________  Location: _________",
    "Income level: _________  Education: _________",
    "Job/Role: _________________________________________________________",
    "",
    "PSYCHOGRAPHICS:",
    "What do they struggle with? ________________________________________",
    "What do they dream about? __________________________________________",
    "What keeps them up at night? _______________________________________",
    "What would change their life? ______________________________________",
    "Where do they spend time online? ___________________________________",
    "Who do they already follow? ________________________________________",
    "",
    "CONTENT PREFERENCES:",
    "They prefer: [ ] Short videos [ ] Long videos [ ] Images [ ] Text [ ] Stories",
    "They are online at: _____________ (time of day)",
    "They engage with: [ ] Humor [ ] Education [ ] Inspiration [ ] Raw/Real",
    "",
    "THEIR TRANSFORMATION:",
    "BEFORE finding my content, they feel: _______________________________",
    "AFTER following me consistently, they will: _________________________",
    "",
    "I HELP MY FOLLOWERS GO FROM:",
    "____________________________________________ (pain point)",
    "TO:",
    "____________________________________________ (desired result)",
    "",
    "ONE SENTENCE CONTENT MISSION:",
    "'I help [who] achieve [what] through [how] on [platform].'",
    "___________________________________________________________________"
]
for line in avatar:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 15

# Page 6: Bio Optimization Template
pdf.new_page()
pdf.add_centered_text(750, "BIO OPTIMIZATION TEMPLATE", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Your bio has 3 seconds to tell someone: Who you are, who you help, why follow.", 'F4', 10)
y -= 20
bio_platforms = ["INSTAGRAM", "TIKTOK", "LINKEDIN", "YOUTUBE"]
for plat in bio_platforms:
    pdf.add_filled_rect(50, y - 5, 512, 120, 0.95)
    pdf.add_rect(50, y - 5, 512, 120, 0.5, 0.5)
    pdf.add_text(55, y + 100, f"{plat} BIO", 'F2', 10)
    pdf.add_text(55, y + 84, "Name/Handle: @_______________________________________________", 'F1', 9)
    pdf.add_text(55, y + 68, "Line 1 (who you are): ________________________________________", 'F1', 9)
    pdf.add_text(55, y + 52, "Line 2 (who you help + how): __________________________________", 'F1', 9)
    pdf.add_text(55, y + 36, "Line 3 (credibility/social proof): _____________________________", 'F1', 9)
    pdf.add_text(55, y + 20, "CTA (call to action): ________________________________________", 'F1', 9)
    pdf.add_text(55, y + 4, "Link: ________________________________________________________", 'F1', 9)
    y -= 135


# Pages 7-18: 12 Weekly Content Planning Pages
for week in range(1, 13):
    pdf.new_page()
    pdf.add_centered_text(755, f"WEEKLY CONTENT PLAN - WEEK {week}", 'F2', 13)
    pdf.add_line(50, 745, 562, 745)
    y = 728
    pdf.add_text(50, y, f"Week of: ___/___/___   Theme/Focus: _______________________________", 'F1', 9)
    y -= 18
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # Header
    pdf.add_filled_rect(50, y - 3, 512, 14, 0.85)
    pdf.add_text(55, y, "Day", 'F2', 7)
    pdf.add_text(85, y, "Post Type", 'F2', 7)
    pdf.add_text(165, y, "Topic/Pillar", 'F2', 7)
    pdf.add_text(290, y, "Caption Notes", 'F2', 7)
    pdf.add_text(430, y, "Time", 'F2', 7)
    pdf.add_text(475, y, "Posted?", 'F2', 7)
    y -= 16
    for day in days:
        pdf.add_text(55, y, day, 'F2', 7)
        pdf.add_line(85, y - 1, 160, y - 1, 0.2, 0.6)
        pdf.add_line(165, y - 1, 285, y - 1, 0.2, 0.6)
        pdf.add_line(290, y - 1, 425, y - 1, 0.2, 0.6)
        pdf.add_line(430, y - 1, 470, y - 1, 0.2, 0.6)
        pdf.add_rect(480, y - 2, 9, 9, 0.4)
        y -= 14
    y -= 8
    pdf.add_text(50, y, "HASHTAG SETS THIS WEEK:", 'F2', 9)
    y -= 14
    pdf.add_text(55, y, "Set 1: _______________________________________________________________", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Set 2: _______________________________________________________________", 'F1', 8)
    y -= 16
    pdf.add_text(50, y, "ENGAGEMENT PLAN:", 'F2', 9)
    y -= 14
    pdf.add_text(55, y, "Comment on ___ accounts/day  |  Reply to all comments within ___ hours", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "DM ___ new connections  |  Engage in ___ communities/groups", 'F1', 8)
    y -= 16
    pdf.add_text(50, y, "WEEKLY METRICS:", 'F2', 9)
    y -= 14
    pdf.add_text(55, y, "Followers start: _____  End: _____  (+___)", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Reach: _________  Engagement rate: _________%", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Best performing post: _____________________________________________", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Why it worked: ____________________________________________________", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "What to do more of: _______________________________________________", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "What to stop doing: _______________________________________________", 'F1', 8)


# Pages 19-21: Monthly Analytics Tracker (3 pages)
for month_num in range(1, 4):
    pdf.new_page()
    pdf.add_centered_text(750, f"MONTHLY ANALYTICS - MONTH {month_num}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    pdf.add_text(50, y, f"Month: _____________  Platform: _____________", 'F1', 9)
    y -= 20
    # Metrics table
    pdf.add_filled_rect(50, y - 3, 512, 14, 0.85)
    pdf.add_text(55, y, "Metric", 'F2', 8)
    pdf.add_text(200, y, "Week 1", 'F2', 8)
    pdf.add_text(275, y, "Week 2", 'F2', 8)
    pdf.add_text(350, y, "Week 3", 'F2', 8)
    pdf.add_text(425, y, "Week 4", 'F2', 8)
    pdf.add_text(500, y, "Total/Avg", 'F2', 8)
    y -= 16
    metrics = ["Followers gained", "Followers lost", "Net follower growth",
        "Total reach", "Impressions", "Profile visits", "Link clicks",
        "Engagement rate (%)", "Comments received", "DMs received",
        "Shares/Saves", "Email signups", "Revenue ($)"]
    for metric in metrics:
        pdf.add_text(55, y, metric, 'F4', 8)
        pdf.add_line(200, y - 1, 265, y - 1, 0.2, 0.6)
        pdf.add_line(275, y - 1, 340, y - 1, 0.2, 0.6)
        pdf.add_line(350, y - 1, 415, y - 1, 0.2, 0.6)
        pdf.add_line(425, y - 1, 490, y - 1, 0.2, 0.6)
        pdf.add_line(500, y - 1, 560, y - 1, 0.2, 0.6)
        y -= 14
    y -= 10
    pdf.add_text(50, y, "TOP 3 POSTS THIS MONTH:", 'F2', 9)
    y -= 14
    for i in range(3):
        pdf.add_text(55, y, f"{i+1}. Topic: _________________  Type: _________  Reach: _______  Engagement: _______", 'F1', 8)
        y -= 13
    y -= 8
    pdf.add_text(50, y, "INSIGHTS:", 'F2', 9)
    y -= 14
    pdf.add_text(55, y, "Content type that performs best: _____________________________________", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Best posting time: _________  Best posting day: _________", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Audience growth trend: [ ] Accelerating  [ ] Steady  [ ] Slowing  [ ] Declining", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Next month priority: _________________________________________________", 'F1', 8)

# Page 22: Viral Content Formula
pdf.new_page()
pdf.add_centered_text(750, "VIRAL CONTENT FORMULA BREAKDOWN", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
viral = [
    "Viral content is not random. It follows patterns:",
    "",
    "THE HOOK (first 1-3 seconds / first line):",
    "- Pattern interrupt: Say something unexpected",
    "- Curiosity gap: Make them NEED to know more",
    "- Bold claim: 'This one trick changed my business'",
    "- Question: 'Why is nobody talking about this?'",
    "- Story: 'I was broke 6 months ago. Here is what I did.'",
    "",
    "MY HOOK FORMULAS (fill in for your niche):",
    "1. 'Stop doing _____ if you want to _____'",
    "2. 'The #1 mistake _____ make is _____'",
    "3. 'Nobody told me _____ about _____'",
    "4. 'I went from _____ to _____ in _____ days'",
    "5. '_____ things I wish I knew before _____'",
    "",
    "THE VALUE (middle of content):",
    "- Teach something specific and actionable",
    "- Tell a relatable story with a lesson",
    "- Show a transformation (before/after)",
    "- Give a hot take with evidence",
    "",
    "THE CTA (call to action at the end):",
    "- Save this for later",
    "- Share with someone who needs this",
    "- Follow for more [topic]",
    "- Comment [word] for my free guide",
    "- Link in bio for [resource]",
    "",
    "SHAREABILITY FACTORS (why people share):",
    "[ ] It makes them look smart",
    "[ ] It makes them feel understood",
    "[ ] It teaches something useful",
    "[ ] It is controversial/debatable",
    "[ ] It is emotionally moving"
]
for line in viral:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 14


# Page 23: Monetization Milestone Checklist
pdf.new_page()
pdf.add_centered_text(750, "MONETIZATION MILESTONE CHECKLIST", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
monetize = [
    "Revenue is the goal. Track your monetization milestones:",
    "",
    "MILESTONE 1: FIRST $100",
    "[ ] Identified what I can sell (product/service/affiliate)",
    "[ ] Created a simple offer or link",
    "[ ] Promoted it in my content (at least 5 posts)",
    "[ ] Got my first paying customer/client",
    "Date achieved: ___/___/___  How: _______________________________",
    "",
    "MILESTONE 2: FIRST $500/MONTH",
    "[ ] Built email list to 100+ subscribers",
    "[ ] Have a consistent offer (digital product/service/course)",
    "[ ] Promote offer weekly (not just once)",
    "[ ] Getting referrals from happy customers",
    "Date achieved: ___/___/___  Revenue source: ____________________",
    "",
    "MILESTONE 3: FIRST $1,000/MONTH",
    "[ ] Multiple income streams (2-3 offers)",
    "[ ] Audience of 1000+ engaged followers",
    "[ ] Sales system (funnel/link/checkout) working consistently",
    "[ ] Brand partnerships or sponsorships inquiring",
    "Date achieved: ___/___/___  Breakdown: _________________________",
    "",
    "MILESTONE 4: FIRST $5,000/MONTH",
    "[ ] Premium offer ($500+) or high volume of lower-priced sales",
    "[ ] Audience of 5000+ or highly engaged niche audience",
    "[ ] Automated systems (email sequences, evergreen content)",
    "[ ] Hiring help (VA, editor, designer)",
    "Date achieved: ___/___/___  Breakdown: _________________________",
    "",
    "MY CURRENT MONETIZATION METHOD: ________________________________",
    "My next revenue goal: $______/month by ___/___/___"
]
for line in monetize:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 14

# Pages 24-26: Collaboration Outreach Templates (3 pages)
collab_types = [
    ("BRAND PARTNERSHIP PITCH", [
        "Subject: Partnership Opportunity - [Your Name/Brand]",
        "",
        "Hi [Brand Contact Name],",
        "",
        "My name is [Your Name] and I create content about [your niche]",
        "for [your audience size + platform]. I have been a fan of [brand]",
        "because [specific reason].",
        "",
        "I would love to explore a partnership because our audiences align:",
        "- My audience: [describe demographics and interests]",
        "- My engagement rate: [X]%",
        "- Content I envision: [specific idea for their brand]",
        "",
        "Would you be open to a quick chat about how we could work together?",
        "",
        "I have attached my media kit. Looking forward to hearing from you!",
        "",
        "Best,",
        "[Your Name]",
        "[Links to profiles]"
    ]),
    ("COLLABORATION WITH ANOTHER CREATOR", [
        "Subject: Collab Idea - [Specific Idea]",
        "",
        "Hi [Creator Name],",
        "",
        "I love your content about [specific thing they do]. Your post about",
        "[specific post] really resonated with my audience too.",
        "",
        "I was thinking we could collaborate on [specific idea]:",
        "- Format: [joint live / guest post / duet / challenge]",
        "- Topic: [something both audiences care about]",
        "- Benefit: Cross-exposure to each other's audiences",
        "",
        "My audience: [size] followers who love [topic].",
        "",
        "Would this interest you? I am flexible on format and timing!",
        "",
        "Looking forward to connecting,",
        "[Your Name]",
        "[Your handle and link]"
    ]),
    ("GUEST EXPERT PITCH (Podcast/Blog/Summit)", [
        "Subject: Guest Expert Pitch - [Your Topic]",
        "",
        "Hi [Host Name],",
        "",
        "I am a [your credential] and I help [who you help] with [what].",
        "I would love to be a guest on [show/blog name] to discuss:",
        "",
        "Topic options:",
        "1. [Specific topic with a hook] - e.g., '5 Myths About...'",
        "2. [Another topic] - e.g., 'How I Went From X to Y'",
        "3. [Third option] - e.g., 'The Biggest Mistake People Make'",
        "",
        "Why your audience would benefit:",
        "[1-2 sentences about the value you would provide]",
        "",
        "About me: [1 sentence bio + audience size + notable achievement]",
        "",
        "I am happy to promote the episode to my [X] followers as well!",
        "",
        "Thank you for your time,",
        "[Your Name, Title, Links]"
    ])
]
for collab_title, template_lines in collab_types:
    pdf.new_page()
    pdf.add_centered_text(750, collab_title, 'F2', 13)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    pdf.add_text(50, y, "Copy and customize this template:", 'F4', 9)
    y -= 16
    pdf.add_filled_rect(50, y - 5, 512, len(template_lines) * 13 + 15, 0.95)
    for tline in template_lines:
        pdf.add_text(55, y, tline, 'F3', 8)
        y -= 13
    y -= 20
    pdf.add_text(50, y, "CUSTOMIZE FOR:", 'F2', 9)
    y -= 14
    pdf.add_text(55, y, "Person/Brand: _______________________  Sent: ___/___/___", 'F1', 8)
    y -= 12
    pdf.add_text(55, y, "Response received? [ ] Yes [ ] No  Outcome: _________________________", 'F1', 8)


# Page 27: Content Batching Day Planner
pdf.new_page()
pdf.add_centered_text(750, "CONTENT BATCHING DAY PLANNER", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
batch = [
    "Batch creating = making a week (or month) of content in ONE session.",
    "This saves time, reduces daily stress, and improves quality.",
    "",
    "MY BATCHING SCHEDULE:",
    "Batch day: _____________ (choose 1 day per week or 2x per month)",
    "Time block: _____________ to _____________",
    "",
    "BATCH DAY TIMELINE:",
]
for line in batch:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 14
timeline = [
    ("9:00-9:30", "Review content calendar, gather ideas and reference posts"),
    ("9:30-10:30", "Write all captions/scripts for the week (7 posts)"),
    ("10:30-10:45", "BREAK - step away from screen"),
    ("10:45-12:00", "Film/photograph all content (batch by location/outfit)"),
    ("12:00-12:30", "LUNCH BREAK"),
    ("12:30-1:30", "Edit content (videos, photos, graphics)"),
    ("1:30-2:00", "Schedule all posts using scheduling tool"),
    ("2:00-2:30", "Research hashtags and write engagement comments"),
    ("2:30-3:00", "Plan next week's content topics"),
]
for time, task in timeline:
    pdf.add_text(55, y, time, 'F2', 8)
    pdf.add_text(140, y, task, 'F4', 8)
    y -= 14
y -= 10
pdf.add_text(50, y, "MY TOOLS:", 'F2', 9)
y -= 14
tools_list = [
    "Scheduling tool: [ ] Later [ ] Buffer [ ] Planoly [ ] Meta Suite [ ] Other: ___",
    "Editing tool: [ ] Canva [ ] CapCut [ ] InShot [ ] Lightroom [ ] Other: ___",
    "Planning tool: [ ] Notion [ ] Trello [ ] Google Sheets [ ] This book!",
]
for tool in tools_list:
    pdf.add_text(55, y, tool, 'F4', 8)
    y -= 13
y -= 10
pdf.add_text(50, y, "BATCHING CHECKLIST (before you sit down):", 'F2', 9)
y -= 14
checklist = [
    "[ ] Content ideas brainstormed (at least 7)",
    "[ ] Reference posts/trends saved for inspiration",
    "[ ] Ring light/lighting set up",
    "[ ] Phone charged and storage cleared",
    "[ ] Outfits chosen (2-3 for variety)",
    "[ ] Props/products ready",
    "[ ] Quiet space secured (no interruptions!)",
    "[ ] Snacks and water nearby"
]
for item in checklist:
    pdf.add_text(55, y, item, 'F4', 8)
    y -= 12

# Page 28: 90-Day Goal Review
pdf.new_page()
pdf.add_centered_text(750, "90-DAY GOAL REVIEW", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
review = [
    "Congratulations on completing 90 days! Review your progress:",
    "",
    "STARTING NUMBERS (Day 1):",
    "Followers: _________  Email list: _________  Revenue: $_________",
    "",
    "ENDING NUMBERS (Day 90):",
    "Followers: _________  Email list: _________  Revenue: $_________",
    "",
    "GROWTH:",
    "Followers gained: _________  (___% growth)",
    "Email subscribers gained: _________",
    "Revenue earned: $_________",
    "Posts published: _________",
    "Collaborations done: _________",
    "",
    "WINS TO CELEBRATE:",
    "1. ____________________________________________________________",
    "2. ____________________________________________________________",
    "3. ____________________________________________________________",
    "",
    "LESSONS LEARNED:",
    "What worked best: _____________________________________________",
    "What did not work: ____________________________________________",
    "What surprised me: ____________________________________________",
    "What I would do differently: __________________________________",
    "",
    "NEXT 90 DAYS - NEW GOALS:",
    "Follower goal: _________  Revenue goal: $_________",
    "New strategy to try: __________________________________________",
    "Skill to develop: ____________________________________________",
    "",
    "MY 90-DAY AFFIRMATION:",
    "'I am building something real. Consistency beats perfection.",
    "My audience is growing because I show up and provide value.'",
    "",
    "Keep going. Your next 90 days will build on everything you learned."
]
for line in review:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 14

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book135_Social_Media_90Day_Plan.pdf')
print("Book135_Social_Media_90Day_Plan.pdf created successfully!")
