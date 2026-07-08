from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(550, "SMALL BUSINESS STARTUP WORKBOOK", 'F2', 18)
pdf.add_centered_text(520, "From Idea to Launch in 90 Days", 'F4', 14)
pdf.add_centered_text(400, "Step-by-Step Planning Guide for New Entrepreneurs", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, "SMALL BUSINESS STARTUP WORKBOOK", 'F2', 12)
pdf.add_centered_text(575, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: Business Idea Validation
pdf.new_page()
pdf.add_centered_text(750, "BUSINESS IDEA VALIDATION CHECKLIST", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Before investing time and money, validate your idea:", "",
    "MY BUSINESS IDEA: _____________________________",
    "_______________________________________________", "",
    "VALIDATION CHECKLIST:",
    "__ Does this solve a real problem people have?",
    "__ Are people currently paying for solutions to this problem?",
    "__ Can I describe my ideal customer in one sentence?",
    "__ Is the market large enough to sustain a business?",
    "__ Do I have skills/knowledge in this area (or can I learn)?",
    "__ Can I start this with $5,000 or less?",
    "__ Can I test this idea before fully launching?",
    "__ Am I passionate enough to work on this for 5+ years?",
    "__ Is there room for differentiation from competitors?",
    "__ Can this generate income within 90 days?", "",
    "QUICK VALIDATION TESTS:",
    "1. Talk to 10 potential customers - would they pay for this?",
    "2. Search for competitors (competition = demand exists!)",
    "3. Create a simple landing page and measure interest",
    "4. Offer the service manually before building anything",
    "5. Pre-sell before you create the product", "",
    "Results of my validation: _______________________",
    "GO / PIVOT / STOP (circle one)"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 4: Market Research
pdf.new_page()
pdf.add_centered_text(750, "MARKET RESEARCH WORKSHEET", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "INDUSTRY OVERVIEW:",
    "Industry: ____________________________________",
    "Industry size (annual revenue): $______________",
    "Growth trend: Growing / Stable / Declining",
    "Key trends affecting this industry:", 
    "1. ____________________________________________",
    "2. ____________________________________________", "",
    "TARGET MARKET:",
    "Total addressable market (TAM): $______________",
    "Serviceable market (SAM): $____________________",
    "My realistic target (SOM): $___________________", "",
    "CUSTOMER RESEARCH (talk to real people!):",
    "Biggest pain point: ___________________________",
    "Current solution they use: _____________________",
    "What they hate about current solution: __________",
    "Price they'd pay for better solution: $__________",
    "Where they look for solutions: _________________", "",
    "INDUSTRY BARRIERS TO ENTRY:",
    "__ High startup costs    __ Licenses/regulations",
    "__ Established competitors __ Technical expertise",
    "__ Network effects       __ Brand loyalty", "",
    "My competitive advantage: ______________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 5: Target Customer Avatar
pdf.new_page()
pdf.add_centered_text(750, "TARGET CUSTOMER AVATAR", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Create a detailed profile of your IDEAL customer:", "",
    "DEMOGRAPHICS:",
    "Name (fictional): _____________________________",
    "Age: ____  Gender: ____  Location: _____________",
    "Income: $________  Education: _________________",
    "Job title: ____________________________________",
    "Family status: ________________________________", "",
    "PSYCHOGRAPHICS:",
    "Values: _______________________________________",
    "Hobbies: ______________________________________",
    "Fears: ________________________________________",
    "Goals/Dreams: _________________________________",
    "Frustrations: _________________________________", "",
    "BUYING BEHAVIOR:",
    "Where they shop: ______________________________",
    "How they research purchases: ___________________",
    "What influences their decisions: ________________",
    "Budget range for my product/service: $___________",
    "How often they'd buy: _________________________", "",
    "SOCIAL MEDIA:",
    "Platforms used: _______________________________",
    "Accounts they follow: _________________________",
    "Content they engage with: _____________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 6: Competitive Analysis
pdf.new_page()
pdf.add_centered_text(750, "COMPETITIVE ANALYSIS TEMPLATE", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in ["Analyze your top 3 competitors:", ""]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16
for comp in range(1, 4):
    pdf.add_text(60, y, f"COMPETITOR {comp}: ______________________________", 'F2', 10)
    y -= 16
    for field in ["Website: ", "Price range: $", "Strengths: ", "Weaknesses: ", "Their customers say (reviews): "]:
        pdf.add_text(70, y, f"{field}_________________________", 'F4', 9)
        y -= 14
    y -= 10
pdf.add_text(60, y, "MY DIFFERENTIATION (why choose me over them):", 'F2', 10)
y -= 16
for _ in range(3):
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 16

# Page 7: Business Model Canvas
pdf.new_page()
pdf.add_centered_text(750, "BUSINESS MODEL CANVAS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
canvas = [
    ("Key Partners:", "Who do I need to work with?"),
    ("Key Activities:", "What must I do daily to deliver value?"),
    ("Key Resources:", "What do I need (tools, people, money)?"),
    ("Value Proposition:", "What problem do I solve uniquely?"),
    ("Customer Relationships:", "How do I acquire & keep customers?"),
    ("Channels:", "How do customers find and buy from me?"),
    ("Customer Segments:", "Who exactly am I serving?"),
    ("Cost Structure:", "What are my main expenses?"),
    ("Revenue Streams:", "How exactly do I make money?")
]
for title, question in canvas:
    pdf.add_text(60, y, title, 'F2', 10)
    pdf.add_text(200, y, question, 'F4', 9)
    y -= 14
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 14
    pdf.add_line(60, y, 550, y, 0.5, 0.5)
    y -= 18

# Page 8: Revenue Model + Startup Costs
pdf.new_page()
pdf.add_centered_text(750, "REVENUE MODEL & STARTUP COSTS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "REVENUE MODEL (how will money come in?):", "",
    "__ Product sales (one-time)  __ Subscription/recurring",
    "__ Service fees              __ Commissions/affiliate",
    "__ Advertising               __ Licensing/royalties",
    "__ Freemium (free + paid upgrade)",
    "",
    "My primary revenue stream: ____________________",
    "Price point: $________________________________",
    "Sales needed monthly to cover costs: ___________",
    "Monthly revenue goal (month 3): $______________",
    "Monthly revenue goal (month 12): $_____________", "",
    "STARTUP COSTS CALCULATOR:",
    "Legal/registration fees:        $______________",
    "Website/domain/hosting:         $______________",
    "Equipment/tools:                $______________",
    "Initial inventory:              $______________",
    "Marketing/advertising:          $______________",
    "Insurance:                      $______________",
    "Software/subscriptions:         $______________",
    "Professional services:          $______________",
    "Emergency fund (3 months):      $______________",
    "                                _______________",
    "TOTAL STARTUP COSTS:            $______________",
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 9: Legal Structure + Funding
pdf.new_page()
pdf.add_centered_text(750, "LEGAL STRUCTURE & FUNDING OPTIONS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "LEGAL STRUCTURE COMPARISON:", "",
    "SOLE PROPRIETORSHIP: Simplest. You ARE the business.",
    "  Pros: Easy setup, low cost, full control",
    "  Cons: Personal liability, harder to get funding",
    "",
    "LLC (Limited Liability Company): Most popular for small biz.",
    "  Pros: Liability protection, tax flexibility, credibility",
    "  Cons: State fees, some paperwork, varies by state",
    "",
    "S-CORP: Best for higher income businesses.",
    "  Pros: Tax savings on self-employment tax, credibility",
    "  Cons: More complex, payroll required, strict rules",
    "",
    "My choice: _________________ Reason: ___________", "",
    "FUNDING OPTIONS:",
    "__ Personal savings (bootstrapping)",
    "__ Friends & family",
    "__ Small business loan (SBA)",
    "__ Business credit card",
    "__ Crowdfunding (Kickstarter, Indiegogo)",
    "__ Angel investors",
    "__ Grants (SCORE, local programs)",
    "__ Side hustle income while building",
    "",
    "My funding plan: ______________________________",
    "Amount needed: $______________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 10: Brand Identity + Business Name
pdf.new_page()
pdf.add_centered_text(750, "BUSINESS NAME & BRAND IDENTITY", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "BUSINESS NAME BRAINSTORM:", "",
    "Idea 1: ______________________ Available? Y/N",
    "Idea 2: ______________________ Available? Y/N",
    "Idea 3: ______________________ Available? Y/N",
    "Idea 4: ______________________ Available? Y/N",
    "Idea 5: ______________________ Available? Y/N",
    "",
    "CHECK: Domain available? __ Social handles available? __",
    "CHECK: Trademark search clear? __",
    "",
    "MY FINAL BUSINESS NAME: _______________________", "",
    "BRAND IDENTITY WORKSHEET:",
    "Brand personality (3 words): ___________________",
    "Brand voice (formal/casual/playful/professional): ___",
    "Colors that represent my brand: ________________",
    "Tagline/slogan: _______________________________",
    "",
    "BRAND PROMISE:",
    "We help [target customer] achieve [desired outcome]",
    "by [how we do it differently].",
    "_______________________________________________",
    "_______________________________________________", "",
    "MISSION STATEMENT:",
    "_______________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 11: Marketing Plan
pdf.new_page()
pdf.add_centered_text(750, "MARKETING PLAN TEMPLATE", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "MARKETING CHANNELS (rank by priority):", "",
    "___ Social media (which platforms: _____________)",
    "___ Content marketing (blog, YouTube, podcast)",
    "___ Email marketing",
    "___ Paid advertising (Google, Facebook, Instagram)",
    "___ SEO (search engine optimization)",
    "___ Networking & referrals",
    "___ Partnerships & collaborations",
    "___ Local community (events, flyers, local SEO)",
    "___ PR & media features",
    "",
    "MARKETING BUDGET (monthly): $__________________",
    "",
    "FIRST 90 DAYS MARKETING PRIORITIES:",
    "Month 1: _____________________________________",
    "Month 2: _____________________________________",
    "Month 3: _____________________________________", "",
    "CONTENT STRATEGY:",
    "I will create [type] content on [platform] [frequency].",
    "_______________________________________________",
    "",
    "LEAD GENERATION:",
    "Free offer/lead magnet: _______________________",
    "How I'll capture emails: ______________________",
    "Follow-up sequence: ___________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 12: Sales Funnel + Social Media Strategy
pdf.new_page()
pdf.add_centered_text(750, "SALES FUNNEL & SOCIAL MEDIA STRATEGY", 'F2', 14)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "SALES FUNNEL PLANNING:", "",
    "AWARENESS (how people discover you):",
    "_______________________________________________",
    "INTEREST (how you capture attention):",
    "_______________________________________________",
    "DECISION (how you help them choose you):",
    "_______________________________________________",
    "ACTION (how they buy/sign up):",
    "_______________________________________________",
    "RETENTION (how you keep them coming back):",
    "_______________________________________________", "",
    "SOCIAL MEDIA STRATEGY:",
    "Primary platform: ___________ Post frequency: ___x/week",
    "Secondary platform: _________ Post frequency: ___x/week",
    "",
    "Content mix: __% Educational  __% Entertaining  __% Promotional",
    "",
    "DAILY SOCIAL MEDIA TASKS (15-30 min):",
    "__ Post content             __ Reply to comments",
    "__ Engage with others' posts __ Check messages",
    "__ Share stories/reels       __ Track analytics weekly"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 13: 90-Day Launch Timeline
pdf.new_page()
pdf.add_centered_text(750, "90-DAY LAUNCH TIMELINE", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "DAYS 1-30: FOUNDATION", "",
    "Week 1: Validate idea, research market, choose legal structure",
    "Week 2: Register business, get EIN, open bank account",
    "Week 3: Build website/landing page, set up social media",
    "Week 4: Create first offer, develop pricing strategy", "",
    "DAYS 31-60: BUILD", "",
    "Week 5: Create content, build email list",
    "Week 6: Develop systems/processes, set up payment processing",
    "Week 7: Beta test with 3-5 people, gather feedback",
    "Week 8: Refine offer based on feedback, prep for launch", "",
    "DAYS 61-90: LAUNCH", "",
    "Week 9: Pre-launch buzz, email sequence, social media push",
    "Week 10: LAUNCH! Open for business officially",
    "Week 11: Gather testimonials, refine marketing",
    "Week 12: Review KPIs, plan next quarter", "",
    "MY LAUNCH DATE: ___/___/______",
    "I will celebrate by: __________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Pages 14-17: Weekly Action Planner (4 pages)
for week_set in range(4):
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEKLY ACTION PLANNER - WEEKS {week_set*3+1}-{week_set*3+3}", 'F2', 13)
    pdf.add_line(60, 738, 552, 738)
    y = 720
    for w in range(3):
        pdf.add_text(60, y, f"WEEK {week_set*3+w+1}:", 'F2', 10)
        y -= 14
        pdf.add_text(60, y, "Top 3 priorities:", 'F4', 9)
        y -= 13
        for p in range(3):
            pdf.add_text(70, y, f"{p+1}. ", 'F1', 9)
            pdf.add_line(85, y-2, 550, y-2, 0.5, 0.5)
            y -= 14
        pdf.add_text(60, y, "Revenue this week: $_____ Hours worked: _____", 'F3', 8)
        y -= 14
        pdf.add_text(60, y, "Biggest win: _____________ Biggest challenge: _____________", 'F3', 8)
        y -= 18
        pdf.add_line(60, y+5, 552, y+5, 0.3, 0.7)
        y -= 10

# Page 18: Financial Projections + KPIs
pdf.new_page()
pdf.add_centered_text(750, "FINANCIAL PROJECTIONS & KPI TRACKING", 'F2', 14)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "12-MONTH REVENUE PROJECTION:", "",
    "Month 1: $________  Month 2: $________  Month 3: $________",
    "Month 4: $________  Month 5: $________  Month 6: $________",
    "Month 7: $________  Month 8: $________  Month 9: $________",
    "Month 10: $_______ Month 11: $_______ Month 12: $_______",
    "YEAR 1 TOTAL: $___________", "",
    "KEY PERFORMANCE INDICATORS (KPIs):", "",
    "Revenue KPIs:           Goal        Actual",
    "Monthly revenue:        $________   $________",
    "Avg transaction value:  $________   $________",
    "Customer lifetime value: $________   $________", "",
    "Growth KPIs:",
    "New customers/month:    ________    ________",
    "Website visitors/month: ________    ________",
    "Email subscribers:      ________    ________",
    "Social media followers: ________    ________", "",
    "Profitability:",
    "Gross margin:           ________%",
    "Monthly expenses:       $________",
    "Break-even point:       $________ /month"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 19: Resources & Next Steps
pdf.new_page()
pdf.add_centered_text(750, "RESOURCES & NEXT STEPS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "FREE RESOURCES FOR NEW BUSINESS OWNERS:", "",
    "SCORE: Free business mentoring (score.org)",
    "SBA: Small Business Administration (sba.gov)",
    "IRS: Small Business Tax Center (irs.gov)",
    "SBDC: Small Business Development Centers (local)", "",
    "TOOLS TO GET STARTED:",
    "Website: WordPress, Shopify, Squarespace, Wix",
    "Email: Mailchimp, ConvertKit, MailerLite",
    "Accounting: Wave (free), QuickBooks, FreshBooks",
    "Social media scheduling: Buffer, Later, Hootsuite",
    "Design: Canva (free), Adobe Express",
    "Payment processing: Stripe, Square, PayPal", "",
    "MY NEXT 5 ACTIONS (do these THIS WEEK):",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "4. ____________________________________________",
    "5. ____________________________________________", "",
    "Remember: Done is better than perfect.",
    "Start messy. Refine later. The world needs your idea!"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book107_Small_Business_Workbook.pdf')
print("Book107_Small_Business_Workbook.pdf created successfully!")
