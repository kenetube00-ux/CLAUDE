from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "LLC STARTUP WORKBOOK"
subtitle = "Form Your Business & Get Organized in 30 Days"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 18)
pdf.add_centered_text(510, subtitle, 'F4', 14)
pdf.add_centered_text(400, "Step-by-Step Guide to Starting", 'F4', 12)
pdf.add_centered_text(380, "Your Business the Right Way", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 12)
pdf.add_centered_text(560, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(540, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(500, "This workbook is for educational purposes only. Consult a", 'F4', 9)
pdf.add_centered_text(487, "licensed attorney and CPA for legal and tax advice.", 'F4', 9)

# Page 3: LLC vs Sole Proprietor vs S-Corp
pdf.new_page()
pdf.add_centered_text(750, "BUSINESS STRUCTURE COMPARISON", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
lines = [
    "SOLE PROPRIETORSHIP:",
    "- No formation required (just start doing business)",
    "- YOU are the business (no legal separation)",
    "- Personal assets at risk if sued",
    "- Simple taxes (Schedule C on personal return)",
    "- Best for: Very low-risk side hustles, testing an idea",
    "",
    "LLC (Limited Liability Company):",
    "- Must file with your state (Articles of Organization)",
    "- Separates personal assets from business liability",
    "- Flexible tax options (sole prop, partnership, S-corp)",
    "- Relatively easy to set up and maintain",
    "- Best for: Most small businesses, freelancers, online businesses",
    "",
    "S-CORPORATION:",
    "- Must elect S-corp status with IRS (Form 2553)",
    "- Can save self-employment taxes if income is high enough",
    "- Requires payroll (you pay yourself a salary)",
    "- More complex recordkeeping and tax filing",
    "- Best for: Businesses with $50K+ net profit consistently",
    "",
    "WHICH DO I NEED?",
    "Making under $50K profit? --> LLC (taxed as sole prop)",
    "Making $50K-$100K+ profit? --> LLC (elect S-corp status)",
    "Multiple owners? --> LLC (multi-member) or Partnership",
    "",
    "MY CHOICE: [ ] Sole Prop [ ] LLC [ ] S-Corp",
    "Reason: ________________________________________________",
]
for line in lines:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 4: State Filing Requirements
pdf.new_page()
pdf.add_centered_text(750, "STATE FILING REQUIREMENTS", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
state_text = [
    "Every state has different LLC requirements. Research yours:",
    "",
    "MY STATE: _____________________________",
    "",
    "FILING INFORMATION:",
    "Secretary of State website: ______________________________",
    "Filing fee: $ _______",
    "Annual report fee: $ _______ (due every: _______)",
    "Processing time: _______ days/weeks",
    "Online filing available? [ ] Yes [ ] No",
    "",
    "DOCUMENTS NEEDED TO FILE:",
    "[ ] Articles of Organization (or Certificate of Formation)",
    "[ ] Registered Agent name and address",
    "[ ] Business name (confirmed available)",
    "[ ] Member/Manager names",
    "[ ] Business address",
    "[ ] Purpose of business (usually 'any lawful purpose')",
    "",
    "ONGOING REQUIREMENTS IN MY STATE:",
    "[ ] Annual report filing: Due date ___/___",
    "[ ] Business license renewal: Due date ___/___",
    "[ ] Franchise tax: Amount $ _______",
    "[ ] State tax registration",
    "[ ] Sales tax permit (if selling goods)",
    "",
    "NOTES:",
    "_________________________________________________",
    "_________________________________________________",
]
for line in state_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 5: Business Name Brainstorm
pdf.new_page()
pdf.add_centered_text(750, "BUSINESS NAME BRAINSTORM", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
name_text = [
    "BRAINSTORM CRITERIA:",
    "- Easy to spell and pronounce",
    "- Available as a domain name (.com preferred)",
    "- Available on social media platforms",
    "- Not too similar to existing businesses (check trademarks)",
    "- Available in your state (search SOS database)",
    "",
    "MY IDEAS (write at least 10):",
]
for line in name_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16
for i in range(10):
    pdf.add_text(50, y, f"{i+1}. ___________________________________________", 'F1', 10)
    y -= 18
y -= 10
pdf.add_text(50, y, "AVAILABILITY CHECK (for top 3 choices):", 'F2', 10)
y -= 18
for i in range(3):
    pdf.add_text(50, y, f"Name: _______________________", 'F1', 9)
    y -= 14
    pdf.add_text(50, y, "[ ] State available [ ] Domain available [ ] Social available [ ] Trademark clear", 'F4', 9)
    y -= 20
y -= 10
pdf.add_text(50, y, "MY FINAL BUSINESS NAME: _________________________________", 'F2', 11)

# Page 6: EIN Application
pdf.new_page()
pdf.add_centered_text(750, "EIN APPLICATION WALKTHROUGH", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
ein = [
    "An EIN (Employer Identification Number) is like a Social Security",
    "number for your business. You need one to open a bank account.",
    "",
    "HOW TO GET YOUR EIN (free, takes 5 minutes):",
    "1. Go to: irs.gov/businesses/small-businesses-self-employed/",
    "   apply-for-an-employer-identification-number-ein-online",
    "2. Click 'Apply Online Now'",
    "3. Select entity type: LLC",
    "4. Answer the questions about your business",
    "5. You'll receive your EIN IMMEDIATELY online",
    "",
    "INFORMATION YOU'LL NEED:",
    "[ ] Legal name of LLC (exactly as filed with state)",
    "[ ] Your SSN (as responsible party)",
    "[ ] Business address",
    "[ ] State where organized",
    "[ ] Date business started (or will start)",
    "[ ] Principal business activity",
    "[ ] Number of employees expected (can be 0)",
    "",
    "IMPORTANT NOTES:",
    "- This is FREE from the IRS. Never pay a third party.",
    "- Apply only AFTER your LLC is approved by the state",
    "- Keep your EIN confirmation letter forever",
    "- You can only apply M-F 7am-10pm EST online",
    "",
    "MY EIN: ____-___________",
    "Date obtained: ___/___/___",
    "Filed confirmation letter: [ ] Yes",
]
for line in ein:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 7: Operating Agreement Guide
pdf.new_page()
pdf.add_centered_text(750, "OPERATING AGREEMENT TEMPLATE GUIDE", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
oa = [
    "Even single-member LLCs need an Operating Agreement. It proves",
    "your LLC is separate from you personally (protects liability shield).",
    "",
    "KEY SECTIONS TO INCLUDE:",
    "",
    "1. COMPANY INFORMATION",
    "   Business name: _______________________________________",
    "   Address: ____________________________________________",
    "   State of formation: __________________________________",
    "   Date formed: ___/___/___",
    "   Purpose: ____________________________________________",
    "",
    "2. MEMBERSHIP (who owns what)",
    "   Member 1: __________________ Ownership: ___%",
    "   Member 2: __________________ Ownership: ___%",
    "",
    "3. MANAGEMENT STRUCTURE",
    "   [ ] Member-managed (all owners manage)",
    "   [ ] Manager-managed (designated manager)",
    "",
    "4. CAPITAL CONTRIBUTIONS",
    "   Initial investment: $__________",
    "",
    "5. PROFIT/LOSS DISTRIBUTION",
    "   How will profits be split? _________________________",
    "",
    "6. DISSOLUTION",
    "   Under what conditions can the LLC be dissolved?",
    "",
    "NOTE: Use a template or have an attorney draft this.",
    "Keep a signed copy with your business records.",
]
for line in oa:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 8: Registered Agent Selection
pdf.new_page()
pdf.add_centered_text(750, "REGISTERED AGENT SELECTION", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
ra = [
    "A Registered Agent receives legal documents on behalf of your LLC.",
    "Every state requires one. Options:",
    "",
    "OPTION 1: BE YOUR OWN REGISTERED AGENT (free)",
    "Requirements: Physical address in your state (not P.O. Box)",
    "Must be available during business hours",
    "Your address becomes PUBLIC record",
    "Best for: People with a commercial office address",
    "",
    "OPTION 2: HIRE A REGISTERED AGENT SERVICE ($50-300/year)",
    "They provide an address and forward documents to you",
    "Keeps your home address private",
    "Never miss important legal notices",
    "Best for: Home-based businesses, privacy-conscious owners",
    "",
    "MY CHOICE: [ ] Self [ ] Service",
    "",
    "IF USING A SERVICE:",
    "Company: ____________________________________________",
    "Annual cost: $_________",
    "Address provided: ____________________________________",
    "",
    "IF BEING MY OWN:",
    "Address to use: ______________________________________",
    "Available during business hours? [ ] Yes [ ] No",
]
for line in ra:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 17

# Page 9: Business Bank Account Setup
pdf.new_page()
pdf.add_centered_text(750, "BUSINESS BANK ACCOUNT SETUP", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
bank = [
    "NEVER mix personal and business money. This is how you lose",
    "your liability protection. Open a separate business account.",
    "",
    "WHAT YOU NEED TO OPEN AN ACCOUNT:",
    "[ ] EIN letter from IRS",
    "[ ] Articles of Organization (state-approved)",
    "[ ] Operating Agreement",
    "[ ] Government-issued photo ID",
    "[ ] Initial deposit (varies by bank)",
    "",
    "WHAT TO LOOK FOR IN A BUSINESS BANK:",
    "[ ] No or low monthly fees",
    "[ ] Free transactions (enough for your volume)",
    "[ ] Online banking and mobile deposit",
    "[ ] Integration with bookkeeping software",
    "[ ] Business debit card",
    "[ ] Good customer service",
    "",
    "POPULAR OPTIONS:",
    "- Local credit union (often lowest fees)",
    "- Chase Business (widespread ATMs)",
    "- Mercury/Novo (online, great for startups)",
    "- Relay (designed for small business)",
    "",
    "MY BANK: _____________________________________________",
    "Account type: [ ] Checking [ ] Savings [ ] Both",
    "Monthly fee: $____  Free transactions: ____",
    "Account opened: ___/___/___",
    "",
    "RULE: Every business dollar goes through this account.",
    "Every personal dollar stays in personal accounts.",
]
for line in bank:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 10: Bookkeeping System Setup
pdf.new_page()
pdf.add_centered_text(750, "BOOKKEEPING SYSTEM SETUP", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
books = [
    "You don't need to be an accountant. You need a SYSTEM.",
    "",
    "SIMPLE CATEGORY TRACKING (at minimum, track these):",
    "",
    "INCOME CATEGORIES:",
    "[ ] Product sales",
    "[ ] Service income",
    "[ ] Other income: ______________",
    "",
    "EXPENSE CATEGORIES:",
    "[ ] Advertising & marketing",
    "[ ] Office supplies",
    "[ ] Software & subscriptions",
    "[ ] Professional services (legal, accounting)",
    "[ ] Insurance",
    "[ ] Inventory/materials (COGS)",
    "[ ] Shipping & delivery",
    "[ ] Travel & transportation",
    "[ ] Meals (50% deductible if business-related)",
    "[ ] Education & training",
    "[ ] Home office (if applicable)",
    "[ ] Phone & internet (business portion)",
    "[ ] Bank fees & merchant fees",
    "[ ] Other: ______________",
    "",
    "BOOKKEEPING SOFTWARE:",
    "[ ] QuickBooks Self-Employed ($15/mo)",
    "[ ] Wave (free)",
    "[ ] FreshBooks ($17/mo)",
    "[ ] Spreadsheet (free but manual)",
    "",
    "My system: _________________ Set up date: ___/___/___",
]
for line in books:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 11: Tax Obligations Overview
pdf.new_page()
pdf.add_centered_text(750, "TAX OBLIGATIONS OVERVIEW", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
tax = [
    "As a business owner, taxes are YOUR responsibility. No one",
    "withholds them for you. Plan ahead or get a painful surprise.",
    "",
    "QUARTERLY ESTIMATED TAXES (due 4x/year):",
    "Q1: April 15     Q2: June 15",
    "Q3: September 15  Q4: January 15",
    "",
    "WHAT YOU OWE:",
    "- Federal income tax (your bracket: likely 22-32%)",
    "- Self-employment tax (15.3% on net profit)",
    "- State income tax (varies by state: ____%)",
    "",
    "RULE OF THUMB: Set aside 25-30% of every dollar you earn.",
    "",
    "WHERE TO SAVE TAX MONEY:",
    "Open a separate savings account JUST for taxes.",
    "Every time you get paid: transfer 30% to tax savings.",
    "",
    "MY TAX SETUP:",
    "Tax savings account at: _______________________________",
    "Percentage I'll set aside: ___%",
    "CPA/Tax preparer: ____________________________________",
    "Estimated quarterly payment: $________",
    "",
    "DEDUCTIONS TO TRACK:",
    "Every business expense reduces your taxable income.",
    "Keep ALL receipts. Use your bookkeeping software.",
    "Mileage log for business driving ($0.67/mile in 2024)",
    "",
    "IMPORTANT: Hire a CPA for your first year. It's worth it.",
]
for line in tax:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 12: Insurance Checklist
pdf.new_page()
pdf.add_centered_text(750, "BUSINESS INSURANCE CHECKLIST", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
ins = [
    "Insurance protects you when things go wrong. Consider these:",
    "",
    "GENERAL LIABILITY INSURANCE",
    "Covers: Third-party injuries, property damage, lawsuits",
    "Who needs it: Almost every business",
    "Typical cost: $30-100/month",
    "Needed? [ ] Yes [ ] No [ ] Research more",
    "",
    "PROFESSIONAL LIABILITY (E&O) INSURANCE",
    "Covers: Mistakes, negligence, failure to deliver",
    "Who needs it: Service-based businesses, consultants",
    "Typical cost: $50-150/month",
    "Needed? [ ] Yes [ ] No [ ] Research more",
    "",
    "PRODUCT LIABILITY INSURANCE",
    "Covers: If your product injures someone",
    "Who needs it: Anyone selling physical products",
    "Needed? [ ] Yes [ ] No [ ] Research more",
    "",
    "BUSINESS PROPERTY INSURANCE",
    "Covers: Equipment, inventory, office contents",
    "Needed? [ ] Yes [ ] No [ ] Research more",
    "",
    "CYBER LIABILITY INSURANCE",
    "Covers: Data breaches, cyber attacks",
    "Needed? [ ] Yes [ ] No [ ] Research more",
    "",
    "MY INSURANCE PLAN:",
    "Provider: _____________ Monthly cost: $________",
    "Coverage obtained: ___/___/___",
]
for line in ins:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 13: Business License/Permits
pdf.new_page()
pdf.add_centered_text(750, "BUSINESS LICENSES & PERMITS", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
lic = [
    "Depending on your industry and location, you may need permits:",
    "",
    "CHECK WITH THESE SOURCES:",
    "[ ] City/county clerk (local business license)",
    "[ ] State licensing board (professional licenses)",
    "[ ] Federal agencies (industry-specific: FDA, FCC, etc.)",
    "[ ] Zoning department (if home-based business)",
    "[ ] Health department (if food/beauty related)",
    "",
    "COMMON LICENSES/PERMITS BY INDUSTRY:",
    "Online business: Usually just state LLC + local license",
    "Food business: Health permits, food handler's cert",
    "Beauty/wellness: Cosmetology/massage license",
    "Construction: Contractor's license, bonding",
    "Childcare: Licensing, background checks, inspections",
    "Professional services: CPA, attorney, therapist license",
    "",
    "MY REQUIRED LICENSES/PERMITS:",
    "1. __________________ Cost: $____ Due: ___/___",
    "2. __________________ Cost: $____ Due: ___/___",
    "3. __________________ Cost: $____ Due: ___/___",
    "4. __________________ Cost: $____ Due: ___/___",
    "",
    "SALES TAX:",
    "Do I sell taxable goods/services? [ ] Yes [ ] No",
    "Sales tax permit needed? [ ] Yes [ ] No",
    "Sales tax rate in my area: ____%",
    "Remit sales tax: [ ] Monthly [ ] Quarterly [ ] Annually",
]
for line in lic:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Pages 14-15: 30-Day LLC Formation Timeline
pdf.new_page()
pdf.add_centered_text(750, "30-DAY LLC FORMATION TIMELINE", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
week1 = [
    "WEEK 1: FOUNDATION",
    "[ ] Day 1-2: Choose business structure (page 3)",
    "[ ] Day 2-3: Brainstorm and verify business name (page 5)",
    "[ ] Day 3-4: Research state requirements (page 4)",
    "[ ] Day 4-5: Choose registered agent (page 8)",
    "[ ] Day 5-7: File Articles of Organization with state",
    "",
    "WEEK 2: LEGAL SETUP",
    "[ ] Day 8-9: Wait for state approval (file expedited if available)",
    "[ ] Day 9-10: Apply for EIN (page 6)",
    "[ ] Day 10-12: Draft Operating Agreement (page 7)",
    "[ ] Day 12-14: Research insurance needs (page 12)",
    "",
    "WEEK 3: FINANCIAL SETUP",
    "[ ] Day 15-16: Open business bank account (page 9)",
    "[ ] Day 16-17: Set up bookkeeping system (page 10)",
    "[ ] Day 17-18: Set up tax savings account (page 11)",
    "[ ] Day 18-20: Research business licenses needed (page 13)",
    "[ ] Day 20-21: Apply for any required licenses/permits",
]
for line in week1:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16
y -= 5
week34 = [
    "WEEK 4: GETTING READY TO OPERATE",
    "[ ] Day 22-23: Set up business email and domain",
    "[ ] Day 23-24: Create basic website or social profiles",
    "[ ] Day 24-25: Set up invoicing/payment system",
    "[ ] Day 25-27: Order business cards/materials if needed",
    "[ ] Day 27-28: Get insurance policy in place",
    "[ ] Day 28-30: Create first marketing materials",
    "[ ] Day 30: LAUNCH! Start serving customers",
]
for line in week34:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 16: Important Documents Storage
pdf.new_page()
pdf.add_centered_text(750, "IMPORTANT DOCUMENTS CHECKLIST", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 715
docs = [
    "Keep these documents safe (both digital and physical copies):",
    "",
    "FORMATION DOCUMENTS:",
    "[ ] Articles of Organization (state-stamped copy)",
    "[ ] Operating Agreement (signed)",
    "[ ] EIN confirmation letter",
    "[ ] Business license(s)",
    "[ ] Registered agent documentation",
    "",
    "FINANCIAL DOCUMENTS:",
    "[ ] Bank account information",
    "[ ] Insurance policies",
    "[ ] Tax returns (keep 7 years)",
    "[ ] Quarterly tax payment confirmations",
    "[ ] All receipts and invoices",
    "",
    "ONGOING:",
    "[ ] Annual report filings",
    "[ ] Meeting minutes (even if just you)",
    "[ ] Contracts with clients/vendors",
    "[ ] Intellectual property registrations",
    "",
    "STORAGE LOCATIONS:",
    "Physical copies: _____________________________________",
    "Digital backup: _____________________________________",
    "(Use cloud storage: Google Drive, Dropbox, etc.)",
    "",
    "FIRST-YEAR MILESTONES:",
    "[ ] First sale/client: Date ___/___/___ Amount: $_____",
    "[ ] First $1,000 month",
    "[ ] First quarterly tax payment made",
    "[ ] First annual report filed",
    "[ ] Break-even point reached",
]
for line in docs:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 17: Estimated Costs Breakdown
pdf.new_page()
pdf.add_centered_text(750, "ESTIMATED STARTUP COSTS", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
costs = [
    "FORMATION COSTS (one-time):",
    "State filing fee:                    $________",
    "Registered agent (if using service): $________",
    "Operating agreement (if attorney):   $________",
    "Business license:                    $________",
    "Domain name:                         $________",
    "Website setup:                       $________",
    "Logo/branding:                       $________",
    "Business cards:                      $________",
    "Initial inventory/supplies:          $________",
    "                         SUBTOTAL:   $________",
    "",
    "MONTHLY RECURRING COSTS:",
    "Bookkeeping software:    $________/mo",
    "Insurance:               $________/mo",
    "Phone/internet (biz %):  $________/mo",
    "Software/subscriptions:  $________/mo",
    "Marketing/advertising:   $________/mo",
    "Other:                   $________/mo",
    "          MONTHLY TOTAL: $________/mo",
    "",
    "TO BREAK EVEN I NEED TO EARN: $________/month",
    "",
    "MY FUNDING SOURCE:",
    "[ ] Personal savings: $________",
    "[ ] Revenue from sales",
    "[ ] Loan/credit: $________",
    "[ ] Other: $________",
    "",
    "TOTAL STARTUP BUDGET: $________________",
]
for line in costs:
    pdf.add_text(50, y, line, 'F3', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book164_LLC_Startup_Workbook.pdf')
print("Book164_LLC_Startup_Workbook.pdf created successfully!")
