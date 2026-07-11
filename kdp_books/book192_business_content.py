#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "THE CONTENT CREATOR", 'F2', 22)
pdf.add_centered_text(485, "BUSINESS PLAN", 'F2', 22)
pdf.add_centered_text(445, "Turn Your Passion into Profit", 'F4', 14)
pdf.add_centered_text(410, f"By {author}", 'F4', 12)
pdf.add_line(150, 390, 462, 390, 2)

# Page 2 - Copyright
pdf.new_page()
pdf.add_centered_text(500, f"Copyright - {author}", 'F1', 10)
pdf.add_centered_text(480, "All rights reserved.", 'F1', 10)

# Page 3 - Defining Your Niche
pdf.new_page()
pdf.add_centered_text(740, "DEFINING YOUR NICHE & AUDIENCE", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "What topic could you talk about for HOURS?", 'F2', 11)
pdf.add_line(50, 685, 540, 685, 0.5, 0.7)
pdf.add_text(50, 665, "What problems can you solve for people?", 'F2', 11)
pdf.add_line(50, 645, 540, 645, 0.5, 0.7)
pdf.add_text(50, 625, "MY NICHE: _________________________________________________", 'F2', 11)
pdf.add_text(50, 595, "MY IDEAL AUDIENCE:", 'F2', 12)
aud_fields = ["Age range:", "Gender:", "Location:", "Income level:",
              "Biggest problem:", "What they want:", "Where they hang out online:"]
y = 575
for f in aud_fields:
    pdf.add_text(60, y, f, 'F1', 10)
    pdf.add_line(220, y-2, 540, y-2, 0.5, 0.7)
    y -= 22
pdf.add_text(50, y-10, "My unique value (why follow ME over others?): ", 'F1', 11)
pdf.add_line(50, y-28, 540, y-28, 0.5, 0.7)
pdf.add_line(50, y-48, 540, y-48, 0.5, 0.7)

# Page 4 - Content Pillar Strategy
pdf.new_page()
pdf.add_centered_text(740, "CONTENT PILLAR STRATEGY", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Choose 3-5 content pillars (main topics you create around):", 'F1', 10)
for pillar in range(1, 6):
    y_start = 695 - (pillar - 1) * 115
    pdf.add_text(50, y_start, f"PILLAR {pillar}: _________________________", 'F2', 10)
    y = y_start - 16
    for i in range(4):
        pdf.add_text(65, y, f"Idea {i+1}: _______________________________________", 'F1', 9)
        y -= 14

# Page 5 - Platform Selection
pdf.new_page()
pdf.add_centered_text(740, "PLATFORM SELECTION MATRIX", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
platforms = [("YouTube", "Long-form video, evergreen, high ad rev"),
             ("TikTok", "Short video, viral potential, young demo"),
             ("Instagram", "Visual, reels+stories, brand partnerships"),
             ("Podcast", "Audio, deep connection, sponsorships"),
             ("Blog/SEO", "Written, evergreen, affiliate income"),
             ("Newsletter", "Owned audience, highest conversion"),
             ("Twitter/X", "Thought leadership, networking"),
             ("Pinterest", "Visual search, drives blog traffic")]
y = 708
pdf.add_text(50, y, "Platform", 'F2', 9)
pdf.add_text(130, y, "Best For", 'F2', 9)
pdf.add_text(400, y, "Priority?", 'F2', 9)
y -= 5
pdf.add_line(50, y, 562, y, 0.5)
y -= 15
for plat, best in platforms:
    pdf.add_text(50, y, plat, 'F2', 9)
    pdf.add_text(130, y, best, 'F1', 9)
    pdf.add_text(400, y, "1  2  3  N/A", 'F1', 8)
    y -= 20
pdf.add_text(50, y-15, "MY PRIMARY PLATFORM: _______________________", 'F2', 11)
pdf.add_text(50, y-35, "MY SECONDARY PLATFORM: _____________________", 'F2', 11)
pdf.add_text(50, y-55, "MY REPURPOSING STRATEGY: ____________________", 'F1', 10)
pdf.add_line(50, y-72, 540, y-72, 0.5, 0.7)


# Page 6 - Monetization Roadmap
pdf.new_page()
pdf.add_centered_text(740, "MONETIZATION ROADMAP", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Multiple income streams = financial stability:", 'F1', 11)
streams = [
    ("Ad Revenue", "1K+ subs/4K hrs (YT), 10K followers (IG)", "$____/mo goal"),
    ("Sponsorships", "Media kit ready, 5K+ engaged followers", "$____/mo goal"),
    ("Digital Products", "Ebooks, courses, templates, presets", "$____/mo goal"),
    ("Services", "Coaching, consulting, freelance", "$____/mo goal"),
    ("Affiliate Marketing", "Recommend products you love for commission", "$____/mo goal"),
    ("Memberships", "Patreon, paid newsletter, community", "$____/mo goal"),
]
y = 688
for stream, req, goal in streams:
    pdf.add_text(50, y, stream, 'F2', 10)
    pdf.add_text(50, y-14, f"Requires: {req}", 'F1', 8)
    pdf.add_text(420, y, goal, 'F1', 9)
    y -= 35
pdf.add_line(50, y, 562, y, 1)
pdf.add_text(50, y-15, "TOTAL MONTHLY INCOME GOAL: $__________", 'F2', 11)
pdf.add_text(50, y-35, "Timeline to reach goal: __________", 'F1', 10)

# Page 7 - Media Kit Builder
pdf.new_page()
pdf.add_centered_text(740, "MEDIA KIT BUILDER", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Your media kit = your resume for brand deals. Include:", 'F1', 10)
mk_fields = ["Bio (2-3 sentences about you & your brand):", "",
             "Audience demographics:", "  Age: ___ Gender: ___ Location: ___",
             "Platform stats:", "  YouTube: ___ subs  Instagram: ___ followers",
             "  TikTok: ___ followers  Email list: ___ subscribers",
             "Average engagement rate: ___%",
             "Past brand collaborations:", "", "",
             "Types of content you offer:", "", "",
             "Starting rates:", "  Sponsored post: $___",
             "  Video integration: $___", "  Story/reel: $___",
             "Contact email: _______________"]
y = 690
for f in mk_fields:
    if f:
        pdf.add_text(50, y, f, 'F1', 10)
    y -= 16

# Page 8 - Rate Card Calculator
pdf.new_page()
pdf.add_centered_text(740, "RATE CARD CALCULATOR", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "General formula: $10-25 per 1,000 followers (varies by niche)", 'F1', 10)
pdf.add_text(50, 685, "MY RATES:", 'F2', 12)
rates = [
    "Instagram feed post: $________",
    "Instagram reel: $________",
    "Instagram story (set of 3): $________",
    "YouTube dedicated video: $________",
    "YouTube integration (60 sec): $________",
    "TikTok video: $________",
    "Blog post: $________",
    "Newsletter mention: $________",
    "Bundle deal (multi-platform): $________",
    "Whitelisting/usage rights (+___% per month): $________",
]
y = 665
for r in rates:
    pdf.add_text(60, y, r, 'F1', 10)
    y -= 20
pdf.add_text(50, y-10, "Notes: Rates increase with exclusivity, usage rights, & complexity", 'F1', 9, 0.4)

# Page 9 - Brand Pitch Templates
pdf.new_page()
pdf.add_centered_text(740, "BRAND PITCH EMAIL TEMPLATES", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "TEMPLATE 1: Cold Pitch to Brand", 'F2', 11)
pitch1 = [
    "Subject: Collaboration Opportunity - [Your Name] x [Brand]",
    "Hi [Brand Name] team,",
    "I'm [name], a [niche] content creator with [stats].",
    "I've been a fan of [brand] because [genuine reason].",
    "I'd love to collaborate on [specific idea].",
    "My audience of [number] would love [product] because [reason].",
    "[Link to media kit]. Looking forward to connecting!",
]
y = 688
for line in pitch1:
    pdf.add_text(60, y, line, 'F4', 9)
    y -= 14
pdf.add_text(50, y-10, "TEMPLATE 2: Responding to Brand Offer", 'F2', 11)
y -= 28
pitch2 = ["Thank you for reaching out! I'd love to work together.",
           "For this type of content, my rate is $[rate].",
           "This includes [deliverables]. Timeline: [dates].",
           "Happy to discuss further. Here's my media kit: [link]"]
for line in pitch2:
    pdf.add_text(60, y, line, 'F4', 9)
    y -= 14
pdf.add_text(50, y-10, "TEMPLATE 3: Negotiating Higher", 'F2', 11)
y -= 28
pitch3 = ["Thank you for the offer of $[amount].",
           "Based on my engagement rate of [X%] and deliverables requested,",
           "my rate for this scope would be $[your rate].",
           "I'm happy to adjust scope if budget is firm."]
for line in pitch3:
    pdf.add_text(60, y, line, 'F4', 9)
    y -= 14


# Page 10 - Income Goal Setting
pdf.new_page()
pdf.add_centered_text(740, "INCOME GOAL SETTING", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Monthly Income Goal: $__________", 'F2', 12)
pdf.add_text(50, 688, "Quarterly Income Goal: $__________", 'F2', 12)
pdf.add_text(50, 666, "Annual Income Goal: $__________", 'F2', 12)
pdf.add_text(50, 636, "INCOME BREAKDOWN (how will I reach my monthly goal?):", 'F2', 11)
y = 614
sources = ["Ad revenue:", "Sponsorships:", "Digital products:",
           "Services:", "Affiliate:", "Other:"]
for s in sources:
    pdf.add_text(60, y, s, 'F1', 10)
    pdf.add_text(180, y, "$_____ /month", 'F1', 10)
    y -= 22
pdf.add_text(50, y-10, "MILESTONES:", 'F2', 11)
y -= 30
milestones_c = ["First $100 month", "First $500 month", "First $1,000 month",
                "First $2,500 month", "First $5,000 month", "First $10,000 month",
                "Replace full-time income"]
for m in milestones_c:
    pdf.add_rect(55, y-8, 10, 10)
    pdf.add_text(70, y-6, m, 'F1', 10)
    pdf.add_text(300, y-6, "Date: ____________", 'F1', 9)
    y -= 20

# Pages 11-12 - Content Batching + Workflow
for pg in range(2):
    pdf.new_page()
    titles = ["CONTENT BATCHING SYSTEM", "WORKFLOW & TOOLS SETUP"]
    pdf.add_centered_text(740, titles[pg], 'F2', 16)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 0:
        pdf.add_text(50, 710, "Batch content in blocks to avoid daily content scramble:", 'F1', 10)
        pdf.add_text(50, 685, "MY BATCHING SCHEDULE:", 'F2', 11)
        batch_days = [("Monday:", "Ideation & scripting"), ("Tuesday:", "Filming/recording"),
                      ("Wednesday:", "Editing"), ("Thursday:", "Scheduling & captions"),
                      ("Friday:", "Engagement & community")]
        y = 665
        for day, task in batch_days:
            pdf.add_text(60, y, day, 'F2', 10)
            pdf.add_text(140, y, task, 'F1', 10)
            pdf.add_line(280, y-2, 540, y-2, 0.5, 0.7)
            y -= 22
        pdf.add_text(50, y-10, "How many pieces per batch: ___", 'F1', 11)
        pdf.add_text(50, y-30, "Batch frequency: Weekly / Bi-weekly / Monthly", 'F1', 11)
    else:
        pdf.add_text(50, 710, "MY TOOLS:", 'F2', 11)
        tools = ["Filming/recording:", "Editing:", "Scheduling:",
                 "Graphics/thumbnails:", "Email marketing:", "Analytics:",
                 "Project management:", "File storage:"]
        y = 690
        for t in tools:
            pdf.add_text(60, y, t, 'F1', 10)
            pdf.add_line(210, y-2, 540, y-2, 0.5, 0.7)
            y -= 22

# Page 13 - Legal Basics
pdf.new_page()
pdf.add_centered_text(740, "LEGAL BASICS", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
legal = [
    ("Business Structure:", "Sole Prop / LLC / S-Corp  (Get an LLC!)"),
    ("EIN:", "Free from IRS.gov - needed for brand deals"),
    ("Business bank account:", "Keep personal & business separate"),
    ("Quarterly taxes:", "Set aside 25-30% of income"),
    ("Contracts:", "ALWAYS use a contract for brand deals"),
    ("FTC disclosure:", "Must disclose all sponsored/affiliate content"),
    ("Music licensing:", "Use royalty-free or licensed music only"),
    ("Trademark:", "Protect your brand name if growing"),
]
y = 710
for item, note in legal:
    pdf.add_rect(55, y-8, 10, 10)
    pdf.add_text(70, y-6, item, 'F2', 10)
    pdf.add_text(70, y-20, note, 'F1', 9)
    y -= 35

# Pages 14-17 - Weekly Content Planning (4 pages)
for week in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(740, f"WEEKLY CONTENT PLAN - WEEK {week}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 715, "Week of: _______________  Theme: _______________", 'F1', 10)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    y = 693
    for day in days:
        pdf.add_text(50, y, day, 'F2', 9)
        pdf.add_text(80, y, "Platform:_______", 'F1', 8)
        pdf.add_text(175, y, "Type:_______", 'F1', 8)
        pdf.add_text(270, y, "Topic:__________________", 'F1', 8)
        pdf.add_text(450, y, "Done?", 'F1', 8)
        pdf.add_rect(480, y-5, 9, 9)
        pdf.add_line(50, y-12, 562, y-12, 0.3, 0.8)
        y -= 28
    pdf.add_text(50, y-5, "Goals this week: ________________________________________", 'F1', 9)
    pdf.add_text(50, y-22, "Results: ________________________________________________", 'F1', 9)
    pdf.add_text(50, y-39, "Lessons learned: ________________________________________", 'F1', 9)

# Page 18 - Revenue Tracker
pdf.new_page()
pdf.add_centered_text(740, "REVENUE TRACKER", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
y = 710
pdf.add_text(50, y, "Month", 'F2', 8)
pdf.add_text(100, y, "Ads", 'F2', 8)
pdf.add_text(150, y, "Sponsors", 'F2', 8)
pdf.add_text(215, y, "Products", 'F2', 8)
pdf.add_text(280, y, "Services", 'F2', 8)
pdf.add_text(345, y, "Affiliate", 'F2', 8)
pdf.add_text(405, y, "Other", 'F2', 8)
pdf.add_text(460, y, "TOTAL", 'F2', 8)
y -= 5
pdf.add_line(50, y, 562, y, 0.5)
y -= 15
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for m in months:
    pdf.add_text(50, y, m, 'F1', 8)
    pdf.add_text(100, y, "$___", 'F1', 8)
    pdf.add_text(150, y, "$___", 'F1', 8)
    pdf.add_text(215, y, "$___", 'F1', 8)
    pdf.add_text(280, y, "$___", 'F1', 8)
    pdf.add_text(345, y, "$___", 'F1', 8)
    pdf.add_text(405, y, "$___", 'F1', 8)
    pdf.add_text(460, y, "$___", 'F2', 8)
    y -= 18
pdf.add_line(50, y, 562, y, 1)
pdf.add_text(50, y-15, "ANNUAL TOTAL: $__________", 'F2', 11)

# Pages 19-25 - 12-Month Growth Plan + extras
remaining = ["12-MONTH GROWTH PLAN", "ANALYTICS THAT MATTER",
             "BRAND PARTNERSHIPS LOG", "CONTENT IDEAS BANK",
             "COLLABORATION TRACKER", "MY CREATOR VISION",
             "QUARTERLY REVIEW"]
for pg, t in enumerate(remaining):
    pdf.new_page()
    pdf.add_centered_text(740, t, 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 0:
        quarters = ["Q1 (Months 1-3):", "Q2 (Months 4-6):",
                    "Q3 (Months 7-9):", "Q4 (Months 10-12):"]
        y = 710
        for q in quarters:
            pdf.add_text(50, y, q, 'F2', 10)
            y -= 15
            pdf.add_text(60, y, "Focus: __________________________________________", 'F1', 9)
            y -= 15
            pdf.add_text(60, y, "Follower goal: _________  Revenue goal: $_________", 'F1', 9)
            y -= 15
            pdf.add_text(60, y, "Content frequency: _________  Key action: _________", 'F1', 9)
            y -= 25
    else:
        y = 710
        for i in range(28):
            pdf.add_line(50, y, 562, y, 0.5, 0.7)
            y -= 22

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book192_Content_Creator_Business_Plan.pdf')
print("Book192_Content_Creator_Business_Plan.pdf created successfully!")
