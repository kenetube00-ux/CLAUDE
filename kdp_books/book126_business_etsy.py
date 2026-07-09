from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "THE ETSY BUSINESS WORKBOOK"
subtitle = "From First Listing to Full-Time Income"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, title, 'F2', 15)
pdf.add_centered_text(450, subtitle, 'F4', 12)
pdf.add_centered_text(380, "A Step-by-Step Planner for Building", 'F4', 10)
pdf.add_centered_text(365, "Your Profitable Etsy Shop", 'F4', 10)
pdf.add_centered_text(230, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, title, 'F2', 10)
pdf.add_centered_text(470, f"Copyright 2025 {author}", 'F4', 9)
pdf.add_centered_text(455, "All rights reserved.", 'F4', 9)
pdf.add_centered_text(425, "No part of this publication may be reproduced without permission.", 'F4', 8)

# Page 3: Finding Your Niche Worksheet
pdf.new_page()
pdf.add_centered_text(610, "FINDING YOUR NICHE WORKSHEET", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
niche = [
    "The best Etsy niches sit at the intersection of 3 things:",
    "1. What you ENJOY making  2. What you are SKILLED at  3. What SELLS",
    "",
    "BRAINSTORM - What I enjoy making/creating:",
    "1. ____________________________  2. ____________________________",
    "3. ____________________________  4. ____________________________",
    "",
    "MARKET RESEARCH - Search Etsy for each idea above:",
    "Idea 1: # of results ______  Avg price $______  Reviews on top items ______",
    "Idea 2: # of results ______  Avg price $______  Reviews on top items ______",
    "Idea 3: # of results ______  Avg price $______  Reviews on top items ______",
    "Idea 4: # of results ______  Avg price $______  Reviews on top items ______",
    "",
    "SWEET SPOT: High demand (many reviews) + NOT oversaturated + good price",
    "",
    "My chosen niche: _______________________________________________",
    "My unique angle (what makes mine different): ____________________",
    "_______________________________________________________________",
    "My target customer: ____________________________________________",
    "Problem I solve for them: ______________________________________"
]
for line in niche:
    pdf.add_text(40, y, line, 'F4', 9)
    y -= 14

# Page 4: Product Research Template
pdf.new_page()
pdf.add_centered_text(610, "PRODUCT RESEARCH TEMPLATE", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Research 5 top-selling competitors in your niche:", 'F4', 9)
y -= 18
for comp in range(5):
    pdf.add_filled_rect(40, y - 3, 352, 85, 0.95)
    pdf.add_rect(40, y - 3, 352, 85, 0.5, 0.5)
    pdf.add_text(45, y + 68, f"COMPETITOR {comp+1}", 'F2', 9)
    pdf.add_text(45, y + 54, "Shop name: __________________  # Sales: ________", 'F1', 8)
    pdf.add_text(45, y + 40, "Best seller: ________________  Price: $________", 'F1', 8)
    pdf.add_text(45, y + 26, "What customers love (read reviews): ____________________", 'F1', 8)
    pdf.add_text(45, y + 12, "What customers complain about: _________________________", 'F1', 8)
    pdf.add_text(45, y - 2, "How I can do it BETTER: ________________________________", 'F1', 8)
    y -= 100

# Page 5: Pricing Calculator
pdf.new_page()
pdf.add_centered_text(610, "PRICING CALCULATOR", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Pricing formula: Materials + Labor + Fees + Profit = Price", 'F2', 9)
y -= 20
for prod in range(3):
    pdf.add_text(40, y, f"PRODUCT {prod+1}: _________________________________", 'F2', 9)
    y -= 15
    pricing_lines = [
        "Materials cost: $________",
        "Labor (hours ___ x $___/hr): $________",
        "Packaging/shipping materials: $________",
        "Etsy listing fee ($0.20): $0.20",
        "Etsy transaction fee (6.5%): $________",
        "Payment processing (3% + $0.25): $________",
        "Etsy ads (if used, 15% of sale): $________",
        "TOTAL COSTS: $________",
        "Desired profit margin (_____%): $________",
        "FINAL PRICE: $________",
        "Competitor average price: $________  [ ] Competitive? Y/N",
    ]
    for pl in pricing_lines:
        pdf.add_text(50, y, pl, 'F1', 8)
        y -= 12
    y -= 12

# Page 6: SEO Keyword Research Worksheet
pdf.new_page()
pdf.add_centered_text(610, "SEO KEYWORD RESEARCH WORKSHEET", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Etsy SEO = being found in search. You get 13 TAGS per listing.", 'F4', 9)
y -= 14
pdf.add_text(40, y, "Use long-tail keywords (2-3 words) that describe your item.", 'F4', 9)
y -= 20
for listing in range(2):
    pdf.add_text(40, y, f"LISTING {listing+1}: _________________________________", 'F2', 9)
    y -= 15
    pdf.add_text(40, y, "Search terms customers would type:", 'F1', 8)
    y -= 12
    for tag in range(13):
        col = tag % 2
        if col == 0:
            pdf.add_text(50, y, f"Tag {tag+1}: _________________________", 'F3', 7)
        else:
            pdf.add_text(220, y, f"Tag {tag+1}: _________________________", 'F3', 7)
            y -= 12
    if 13 % 2 == 1:
        y -= 12
    y -= 12
    pdf.add_text(50, y, "Title (front-load best keywords): _______________________________", 'F1', 8)
    y -= 18

# Page 7: Listing Creation Template
pdf.new_page()
pdf.add_centered_text(610, "LISTING CREATION TEMPLATE", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
listing_template = [
    "LISTING TITLE (140 chars max, best keywords first):",
    "_______________________________________________________________",
    "",
    "PHOTOS CHECKLIST:",
    "[ ] Main photo (clean, bright, shows full product)",
    "[ ] Lifestyle photo (product in use)",
    "[ ] Scale photo (shows size clearly)",
    "[ ] Detail/texture close-up",
    "[ ] Packaging photo",
    "[ ] Size chart or comparison",
    "[ ] Process/behind-the-scenes",
    "[ ] Text overlay with key features",
    "[ ] Video (up to 15 seconds)",
    "",
    "DESCRIPTION FORMULA:",
    "Paragraph 1: Hook - What problem does this solve?",
    "_______________________________________________________________",
    "Paragraph 2: Features & details",
    "_______________________________________________________________",
    "Paragraph 3: Size/dimensions/materials",
    "_______________________________________________________________",
    "Paragraph 4: Shipping & processing time",
    "_______________________________________________________________",
    "Paragraph 5: Call to action + shop policies",
    "_______________________________________________________________",
    "",
    "Category: ____________  Price: $________  Quantity: ________",
    "Processing time: ________ days  Shipping: [ ] Free [ ] Calculated"
]
for line in listing_template:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 8: Shop Branding Worksheet
pdf.new_page()
pdf.add_centered_text(610, "SHOP BRANDING WORKSHEET", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
branding = [
    "SHOP NAME: ____________________________________________________",
    "(Available on Etsy? [ ] Yes [ ] No  Backup: ___________________)",
    "",
    "BRAND PERSONALITY (circle 3-5 words):",
    "Playful / Elegant / Minimalist / Rustic / Modern / Luxurious /",
    "Whimsical / Earthy / Bold / Sophisticated / Cozy / Professional",
    "",
    "COLOR PALETTE (choose 3-5 colors):",
    "Primary: ____________  Secondary: ____________  Accent: ____________",
    "",
    "FONTS:",
    "Headings: ___________________  Body: ___________________",
    "",
    "MY BRAND STORY (why I started this shop):",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "_______________________________________________________________",
    "",
    "TARGET CUSTOMER AVATAR:",
    "Name: __________  Age: _____  Gender: __________",
    "Interests: _________________________________________________",
    "Where they shop: ___________________________________________",
    "What they value: ___________________________________________",
    "Price sensitivity: Low / Medium / High",
    "",
    "MY UNIQUE SELLING PROPOSITION (USP):",
    "'I help [target customer] get [benefit] through [your product]'",
    "_______________________________________________________________"
]
for line in branding:
    pdf.add_text(40, y, line, 'F4', 9)
    y -= 14

# Page 9: Photography Checklist
pdf.new_page()
pdf.add_centered_text(610, "PRODUCT PHOTOGRAPHY CHECKLIST", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
photo_text = [
    "Great photos = more sales. Follow this checklist for every product:",
    "",
    "SETUP:",
    "[ ] Natural light (near window, no direct sun)",
    "[ ] Clean background (white poster board or styled flat-lay)",
    "[ ] Tripod or stable surface (no blurry photos!)",
    "[ ] Props that match brand aesthetic (not distracting)",
    "[ ] Product clean and lint-free",
    "",
    "SHOT LIST (aim for 8-10 photos per listing):",
    "[ ] Front view - full product, clean background",
    "[ ] Back view - show all details",
    "[ ] Close-up - texture, quality, craftsmanship",
    "[ ] Scale shot - next to ruler, hand, or common object",
    "[ ] In-use / lifestyle shot",
    "[ ] Packaging - how it arrives",
    "[ ] Multiple color/variation options",
    "[ ] Flat-lay with coordinating items",
    "[ ] Detail of any customization options",
    "[ ] Infographic with dimensions/features",
    "",
    "EDITING:",
    "[ ] Brightness/contrast adjusted (bright but not washed out)",
    "[ ] White balance corrected (true colors)",
    "[ ] Cropped consistently (square or 4:3)",
    "[ ] Watermark added (optional, subtle if used)",
    "[ ] Saved at high resolution",
    "",
    "TIP: Batch photograph! Do all products same day, same setup."
]
for line in photo_text:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 10: Financial Tracker
pdf.new_page()
pdf.add_centered_text(610, "MONTHLY FINANCIAL TRACKER", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Month: ____________  Year: ________", 'F2', 9)
y -= 18
pdf.add_filled_rect(40, y - 3, 352, 14, 0.85)
pdf.add_text(45, y, "Category", 'F2', 8)
pdf.add_text(200, y, "Amount", 'F2', 8)
pdf.add_text(280, y, "Notes", 'F2', 8)
y -= 16
revenue_items = ["Total Sales Revenue", "Number of Orders", "Average Order Value"]
expense_items = ["Materials/Supplies", "Etsy Fees (listing + transaction)", "Payment Processing Fees",
    "Shipping Costs", "Packaging Materials", "Advertising/Etsy Ads", "Tools/Software", "Other Expenses"]
summary_items = ["TOTAL REVENUE", "TOTAL EXPENSES", "NET PROFIT", "Profit Margin (%)"]
pdf.add_text(45, y, "REVENUE", 'F2', 8)
y -= 12
for item in revenue_items:
    pdf.add_text(50, y, item, 'F4', 8)
    pdf.add_text(200, y, "$________", 'F3', 7)
    pdf.add_line(270, y - 1, 390, y - 1, 0.2, 0.6)
    y -= 12
y -= 6
pdf.add_text(45, y, "EXPENSES", 'F2', 8)
y -= 12
for item in expense_items:
    pdf.add_text(50, y, item, 'F4', 8)
    pdf.add_text(200, y, "$________", 'F3', 7)
    pdf.add_line(270, y - 1, 390, y - 1, 0.2, 0.6)
    y -= 12
y -= 6
pdf.add_line(40, y + 3, 392, y + 3, 1, 0)
for item in summary_items:
    pdf.add_text(50, y, item, 'F2', 8)
    pdf.add_text(200, y, "$________", 'F3', 7)
    y -= 12

# Page 11: Marketing Plan
pdf.new_page()
pdf.add_centered_text(610, "MARKETING PLAN", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
marketing = [
    "PINTEREST STRATEGY (top traffic source for Etsy):",
    "  Account: ___________________  Boards created: _____",
    "  Pinning schedule: _____ pins/day  Best times: _______",
    "  Keywords for pin descriptions: _________________________",
    "",
    "INSTAGRAM STRATEGY:",
    "  Account: @___________________  Posting: ___x/week",
    "  Content mix: ___% product, ___% behind scenes, ___% educational",
    "  Hashtag groups saved: [ ] Yes",
    "  Reels/video content plan: ________________________________",
    "",
    "EMAIL LIST:",
    "  Platform (Mailchimp/ConvertKit): _________________________",
    "  Lead magnet (freebie to attract subscribers): _____________",
    "  Email frequency: Weekly / Bi-weekly / Monthly",
    "  Content: New products / Sales / Tips / Behind the scenes",
    "",
    "ETSY ADS BUDGET:",
    "  Daily budget: $________",
    "  Only advertise listings with: [ ] Good reviews [ ] High margins",
    "  Review ad performance: Weekly / Monthly",
    "",
    "COLLABORATIONS / CROSS-PROMOTION:",
    "  Complementary shops to partner with: _____________________",
    "  Influencer outreach plan: ________________________________",
]
for line in marketing:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Page 12: Customer Service Scripts
pdf.new_page()
pdf.add_centered_text(610, "CUSTOMER SERVICE SCRIPTS", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
scripts = [
    "RESPONSE TO POSITIVE REVIEW:",
    "'Thank you so much, [Name]! I am thrilled you love your [product].",
    "Your kind words made my day! Enjoy, and I am here if you ever need",
    "anything. ~ [Your name]'",
    "",
    "RESPONSE TO NEGATIVE REVIEW:",
    "'I am so sorry your experience was not what you expected, [Name].",
    "I would love to make this right. Please message me directly so we",
    "can find a solution. Your satisfaction matters to me.'",
    "",
    "SHIPPING DELAY MESSAGE:",
    "'Hi [Name], Thank you for your order! I wanted to let you know",
    "that [reason] may add 1-2 days to processing. Your item will ship",
    "by [date]. I appreciate your patience!'",
    "",
    "CUSTOM ORDER INQUIRY:",
    "'Hi [Name]! Thank you for reaching out about a custom order.",
    "I would love to help! Here are a few questions: [questions].",
    "Custom orders typically take [X] days and start at $[X].",
    "Let me know if you would like to proceed!'",
    "",
    "OUT OF STOCK / DISCONTINUED:",
    "'Hi [Name], Thank you for your interest in [product]! Unfortunately",
    "this item is currently out of stock. I expect it back by [date].",
    "Would you like me to message you when it is available?'"
]
for line in scripts:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 12

# Page 13: Scaling Checklist
pdf.new_page()
pdf.add_centered_text(610, "SCALING YOUR ETSY BUSINESS", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
scaling = [
    "WHEN TO SCALE (check all that apply):",
    "[ ] Consistently selling 20+ items/month",
    "[ ] Getting repeat customers",
    "[ ] Can not keep up with demand",
    "[ ] Want to quit day job",
    "[ ] Have systems in place for fulfillment",
    "",
    "SCALING STRATEGIES:",
    "[ ] Expand product line (add variations/sizes/colors)",
    "[ ] Raise prices (test 10-20% increase)",
    "[ ] Hire help (VA, production assistant, shipper)",
    "[ ] Batch production (make 50 at once vs 1 at a time)",
    "[ ] Add digital products (higher margin, no shipping)",
    "[ ] Open second sales channel (website, Amazon Handmade)",
    "[ ] Wholesale to local shops",
    "[ ] Offer bundles and gift sets",
    "",
    "SYSTEMS TO BUILD BEFORE SCALING:",
    "[ ] Inventory tracking system",
    "[ ] Standard operating procedures (SOPs) for each task",
    "[ ] Financial tracking (separate business bank account)",
    "[ ] Customer service templates",
    "[ ] Shipping station and supplies stocked",
    "[ ] Time tracking (know your hourly rate)",
    "",
    "MY NEXT SCALING STEP: ________________________________________",
    "By when: ___/___/___  Resources needed: ________________________"
]
for line in scaling:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

# Pages 14-19: Monthly Goal Setting (6 pages)
for month in range(1, 7):
    pdf.new_page()
    pdf.add_centered_text(610, f"MONTHLY GOALS - MONTH {month}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    pdf.add_text(40, y, f"Month: _____________  Year: ________", 'F1', 9)
    y -= 20
    pdf.add_text(40, y, "REVENUE GOAL: $________  ORDERS GOAL: ________", 'F2', 9)
    y -= 16
    pdf.add_text(40, y, "NEW LISTINGS GOAL: ________  REVIEWS GOAL: ________", 'F2', 9)
    y -= 20
    pdf.add_text(40, y, "TOP 3 PRIORITIES THIS MONTH:", 'F2', 9)
    y -= 14
    for i in range(3):
        pdf.add_text(45, y, f"{i+1}.", 'F1', 9)
        pdf.add_line(55, y - 2, 392, y - 2, 0.3, 0.5)
        y -= 16
    y -= 10
    pdf.add_text(40, y, "WEEKLY ACTION ITEMS:", 'F2', 9)
    y -= 14
    for week in range(4):
        pdf.add_text(45, y, f"Week {week+1}:", 'F2', 8)
        y -= 12
        for _ in range(3):
            pdf.add_rect(55, y - 2, 8, 8, 0.4)
            pdf.add_text(67, y, "________________________________", 'F1', 8)
            y -= 12
        y -= 6
    y -= 8
    pdf.add_text(40, y, "END OF MONTH REVIEW:", 'F2', 9)
    y -= 14
    pdf.add_text(45, y, "Revenue achieved: $______  Orders: ______  New listings: ______", 'F1', 8)
    y -= 12
    pdf.add_text(45, y, "What worked: _______________________________________________", 'F1', 8)
    y -= 12
    pdf.add_text(45, y, "What to improve: ___________________________________________", 'F1', 8)
    y -= 12
    pdf.add_text(45, y, "Next month focus: __________________________________________", 'F1', 8)

# Page 20: 90-Day Launch Plan
pdf.new_page()
pdf.add_centered_text(610, "90-DAY LAUNCH PLAN", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
launch = [
    "DAYS 1-30: FOUNDATION",
    "[ ] Set up Etsy shop (banner, bio, policies)",
    "[ ] Complete branding worksheet",
    "[ ] Create first 10 listings with optimized SEO",
    "[ ] Set up social media accounts (Instagram + Pinterest)",
    "[ ] Photograph all current products",
    "[ ] Set up financial tracking system",
    "[ ] Join 3 Etsy seller Facebook groups",
    "",
    "DAYS 31-60: GROWTH",
    "[ ] Add 10 more listings (goal: 20 total)",
    "[ ] Get first 5 sales (offer opening sale discount)",
    "[ ] Start Etsy ads ($1-2/day budget)",
    "[ ] Post daily on Pinterest (5+ pins)",
    "[ ] Begin email list with lead magnet",
    "[ ] Reach out to 5 potential collaborators",
    "[ ] Analyze which listings perform best",
    "",
    "DAYS 61-90: OPTIMIZATION",
    "[ ] Add 10 more listings (goal: 30 total)",
    "[ ] Optimize underperforming listings (new photos/tags)",
    "[ ] Request reviews from happy customers",
    "[ ] Launch seasonal or trending product",
    "[ ] Calculate true profit margins",
    "[ ] Plan next 90 days based on data",
    "[ ] Celebrate your progress!",
    "",
    "90-DAY REVENUE TARGET: $________",
    "Actual revenue achieved: $________"
]
for line in launch:
    pdf.add_text(40, y, line, 'F4', 8)
    y -= 13

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book126_Etsy_Business_Workbook.pdf')
print("Book126_Etsy_Business_Workbook.pdf created successfully!")
