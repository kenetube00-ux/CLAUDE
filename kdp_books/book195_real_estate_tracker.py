#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "REAL ESTATE INVESTMENT", 'F2', 22)
pdf.add_centered_text(485, "TRACKER", 'F2', 22)
pdf.add_centered_text(445, "Property Analysis, Income & Expense Log", 'F4', 13)
pdf.add_centered_text(410, f"By {author}", 'F4', 12)
pdf.add_line(150, 390, 462, 390, 2)

# Page 2 - Copyright + Strategy Overview
pdf.new_page()
pdf.add_centered_text(740, "INVESTMENT STRATEGY OVERVIEW", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, f"Copyright - {author}. All rights reserved.", 'F1', 9)
pdf.add_text(50, 685, "MY INVESTMENT STRATEGY:", 'F2', 12)
strat_fields = [
    "Investment approach (buy & hold / flip / BRRRR / wholesale):",
    "Target market/area:", "Property type (SFH / multi / commercial):",
    "Ideal purchase price range:", "Target cash-on-cash return:",
    "Target cap rate:", "Financing strategy:",
    "Number of properties goal (1 year):", "Number of properties goal (5 year):",
    "Monthly passive income goal:", "Exit strategy:",
]
y = 665
for f in strat_fields:
    pdf.add_text(50, y, f, 'F1', 10)
    pdf.add_line(50, y-14, 540, y-14, 0.5, 0.7)
    y -= 30

# Pages 3-7 - Property Analysis Worksheets (5 pages)
for prop in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(740, f"PROPERTY ANALYSIS - #{prop}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 715, "Address: ___________________________________________________", 'F1', 10)
    pdf.add_text(50, 695, "Type: SFH / Duplex / Triplex / Quad / Other:___", 'F1', 9)
    pdf.add_text(350, 695, "Beds:___ Baths:___ SqFt:___", 'F1', 9)
    pdf.add_text(50, 670, "PURCHASE:", 'F2', 11)
    pdf.add_text(60, 653, "Asking price: $________  Offer: $________  Final: $________", 'F1', 9)
    pdf.add_text(60, 636, "Closing costs: $________  Repairs needed: $________", 'F1', 9)
    pdf.add_text(60, 619, "Total investment: $________  Down payment: $________", 'F1', 9)
    pdf.add_text(60, 602, "Loan amount: $________  Rate: ____%  Term: ___ yrs", 'F1', 9)
    pdf.add_text(60, 585, "Monthly mortgage (PITI): $________", 'F1', 9)
    pdf.add_text(50, 560, "INCOME:", 'F2', 11)
    pdf.add_text(60, 543, "Monthly rent: $________  Other income: $________", 'F1', 9)
    pdf.add_text(60, 526, "Gross monthly income: $________", 'F1', 9)
    pdf.add_text(50, 501, "EXPENSES (monthly):", 'F2', 11)
    expenses = [("Mortgage:", "$_____"), ("Insurance:", "$_____"),
                ("Taxes:", "$_____"), ("HOA:", "$_____"),
                ("Maintenance (10%):", "$_____"), ("Vacancy (8%):", "$_____"),
                ("CapEx (5%):", "$_____"), ("Property mgmt:", "$_____"),
                ("Utilities (if paying):", "$_____")]
    y = 484
    for i, (exp, amt) in enumerate(expenses):
        col = 0 if i < 5 else 1
        row = i if i < 5 else i - 5
        x = 60 + col * 260
        pdf.add_text(x, y - row * 16, f"{exp} {amt}", 'F1', 9)
    y -= 85
    pdf.add_text(60, y, "Total monthly expenses: $________", 'F2', 9)
    pdf.add_text(50, y-22, "RETURNS:", 'F2', 11)
    pdf.add_text(60, y-38, "Monthly cash flow: $______  Annual: $______", 'F1', 9)
    pdf.add_text(60, y-54, "Cash-on-cash return: ____%  Cap rate: ____%", 'F1', 9)
    pdf.add_text(60, y-70, "ARV: $________  Equity after repairs: $________", 'F1', 9)
    pdf.add_text(60, y-86, "BUY? YES / NO  Notes: _______________________", 'F2', 9)


# Pages 8-13 - Rental Income Tracker (6 pages)
for pg in range(6):
    pdf.new_page()
    pdf.add_centered_text(740, f"RENTAL INCOME TRACKER - PAGE {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 715, "Property: ___________________________________", 'F1', 10)
    y = 695
    pdf.add_text(50, y, "Month", 'F2', 8)
    pdf.add_text(110, y, "Rent Due", 'F2', 8)
    pdf.add_text(175, y, "Collected", 'F2', 8)
    pdf.add_text(245, y, "Date Paid", 'F2', 8)
    pdf.add_text(320, y, "Late Fee", 'F2', 8)
    pdf.add_text(385, y, "Vacancy?", 'F2', 8)
    pdf.add_text(450, y, "Notes", 'F2', 8)
    y -= 5
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 15
    for i in range(24):
        pdf.add_line(50, y, 105, y, 0.3, 0.7)
        pdf.add_line(110, y, 170, y, 0.3, 0.7)
        pdf.add_line(175, y, 240, y, 0.3, 0.7)
        pdf.add_line(245, y, 315, y, 0.3, 0.7)
        pdf.add_line(320, y, 380, y, 0.3, 0.7)
        pdf.add_line(385, y, 445, y, 0.3, 0.7)
        pdf.add_line(450, y, 562, y, 0.3, 0.7)
        y -= 16
    pdf.add_text(50, y-5, "Total collected: $______  Vacancy rate: ___%", 'F1', 9)

# Pages 14-19 - Expense Log (6 pages)
for pg in range(6):
    pdf.new_page()
    pdf.add_centered_text(740, f"EXPENSE LOG - PAGE {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 715, "Property: ___________________________________", 'F1', 10)
    y = 695
    pdf.add_text(50, y, "Date", 'F2', 8)
    pdf.add_text(105, y, "Property", 'F2', 8)
    pdf.add_text(185, y, "Category", 'F2', 8)
    pdf.add_text(275, y, "Amount", 'F2', 8)
    pdf.add_text(340, y, "Vendor", 'F2', 8)
    pdf.add_text(430, y, "Notes", 'F2', 8)
    y -= 5
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 15
    for i in range(28):
        pdf.add_line(50, y, 100, y, 0.3, 0.7)
        pdf.add_line(105, y, 180, y, 0.3, 0.7)
        pdf.add_line(185, y, 270, y, 0.3, 0.7)
        pdf.add_line(275, y, 335, y, 0.3, 0.7)
        pdf.add_line(340, y, 425, y, 0.3, 0.7)
        pdf.add_line(430, y, 562, y, 0.3, 0.7)
        y -= 15
    pdf.add_text(50, y-5, "Page total: $________", 'F2', 9)
    pdf.add_text(200, y-5, "Categories: Repair/Maint/CapEx/Insurance/Tax/Util/Mgmt/Legal/Other", 'F1', 7)

# Pages 20-22 - Mortgage Payment Tracker (3 pages)
for pg in range(3):
    pdf.new_page()
    pdf.add_centered_text(740, f"MORTGAGE PAYMENT TRACKER - {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 715, "Property: _____________ Lender: _____________", 'F1', 10)
    pdf.add_text(50, 698, "Loan #: _____________ Rate: ____% Original balance: $_________", 'F1', 9)
    y = 678
    pdf.add_text(50, y, "Month", 'F2', 7)
    pdf.add_text(105, y, "Payment", 'F2', 7)
    pdf.add_text(165, y, "Principal", 'F2', 7)
    pdf.add_text(230, y, "Interest", 'F2', 7)
    pdf.add_text(295, y, "Escrow", 'F2', 7)
    pdf.add_text(355, y, "Extra", 'F2', 7)
    pdf.add_text(405, y, "Balance", 'F2', 7)
    pdf.add_text(475, y, "Date Paid", 'F2', 7)
    y -= 5
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 13
    for i in range(24):
        pdf.add_line(50, y, 100, y, 0.3, 0.7)
        pdf.add_line(105, y, 160, y, 0.3, 0.7)
        pdf.add_line(165, y, 225, y, 0.3, 0.7)
        pdf.add_line(230, y, 290, y, 0.3, 0.7)
        pdf.add_line(295, y, 350, y, 0.3, 0.7)
        pdf.add_line(355, y, 400, y, 0.3, 0.7)
        pdf.add_line(405, y, 470, y, 0.3, 0.7)
        pdf.add_line(475, y, 562, y, 0.3, 0.7)
        y -= 14


# Pages 23-27 - Tenant Information (5 pages)
for pg in range(5):
    pdf.new_page()
    pdf.add_centered_text(740, f"TENANT INFORMATION - UNIT {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, "Property: ________________________________________________", 'F1', 10)
    pdf.add_text(50, 688, "Unit/Address: _____________________________________________", 'F1', 10)
    t_fields = [
        "Tenant name:", "Co-tenant:", "Phone:", "Email:",
        "Employer:", "Emergency contact:", "Emergency phone:",
        "Lease start:", "Lease end:", "Monthly rent: $",
        "Security deposit: $", "Pet deposit: $", "Pets (type/breed):",
        "Vehicles (make/model/plate):", "Move-in condition noted: Y/N",
    ]
    y = 665
    for f in t_fields:
        pdf.add_text(50, y, f, 'F1', 9)
        pdf.add_line(220, y-2, 540, y-2, 0.5, 0.7)
        y -= 20
    pdf.add_text(50, y-5, "Lease renewal notes:", 'F1', 9)
    pdf.add_line(50, y-20, 540, y-20, 0.5, 0.7)
    pdf.add_line(50, y-38, 540, y-38, 0.5, 0.7)

# Pages 28-30 - Maintenance Log, Annual P&L, Tax Deductions, Portfolio
# Page 28 - Maintenance Request Log
pdf.new_page()
pdf.add_centered_text(740, "MAINTENANCE REQUEST LOG", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
y = 712
pdf.add_text(50, y, "Date", 'F2', 7)
pdf.add_text(100, y, "Property/Unit", 'F2', 7)
pdf.add_text(195, y, "Issue", 'F2', 7)
pdf.add_text(320, y, "Vendor", 'F2', 7)
pdf.add_text(400, y, "Cost", 'F2', 7)
pdf.add_text(450, y, "Status", 'F2', 7)
pdf.add_text(510, y, "Resolved", 'F2', 7)
y -= 5
pdf.add_line(50, y, 562, y, 0.5)
y -= 13
for i in range(30):
    pdf.add_line(50, y, 95, y, 0.3, 0.7)
    pdf.add_line(100, y, 190, y, 0.3, 0.7)
    pdf.add_line(195, y, 315, y, 0.3, 0.7)
    pdf.add_line(320, y, 395, y, 0.3, 0.7)
    pdf.add_line(400, y, 445, y, 0.3, 0.7)
    pdf.add_line(450, y, 505, y, 0.3, 0.7)
    pdf.add_line(510, y, 562, y, 0.3, 0.7)
    y -= 14

# Page 29 - Annual P&L + Tax Deductions
pdf.new_page()
pdf.add_centered_text(740, "ANNUAL P&L SUMMARY", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 715, "Year: _______  Property: _________________________", 'F1', 10)
pdf.add_text(50, 690, "INCOME:", 'F2', 11)
income_items = ["Gross rental income:", "Late fees:", "Other income:", "TOTAL INCOME:"]
y = 670
for item in income_items:
    pdf.add_text(60, y, item, 'F1', 10)
    pdf.add_text(300, y, "$____________", 'F1', 10)
    y -= 18
pdf.add_text(50, y-5, "EXPENSES:", 'F2', 11)
y -= 22
exp_items = ["Mortgage interest:", "Insurance:", "Property taxes:", "Repairs & maintenance:",
             "Property management:", "Utilities:", "Legal/professional:", "Advertising:",
             "Travel:", "Depreciation:", "TOTAL EXPENSES:"]
for item in exp_items:
    pdf.add_text(60, y, item, 'F1', 10)
    pdf.add_text(300, y, "$____________", 'F1', 10)
    y -= 16
pdf.add_line(50, y, 400, y, 1)
y -= 18
pdf.add_text(50, y, "NET OPERATING INCOME:", 'F2', 11)
pdf.add_text(300, y, "$____________", 'F2', 11)
y -= 20
pdf.add_text(50, y, "TAX DEDUCTION CHECKLIST:", 'F2', 11)
y -= 18
deductions = ["Mortgage interest", "Property taxes", "Insurance premiums",
              "Repairs & maintenance", "Depreciation", "Travel to properties",
              "Home office (if applicable)", "Professional services", "Advertising"]
for d in deductions:
    pdf.add_rect(55, y-7, 9, 9)
    pdf.add_text(70, y-5, d, 'F1', 9)
    y -= 14

# Page 30 - Portfolio Dashboard
pdf.new_page()
pdf.add_centered_text(740, "PORTFOLIO OVERVIEW DASHBOARD", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Date: _____________  Total properties: ___", 'F1', 10)
y = 688
pdf.add_text(50, y, "Property", 'F2', 8)
pdf.add_text(160, y, "Value", 'F2', 8)
pdf.add_text(220, y, "Owed", 'F2', 8)
pdf.add_text(280, y, "Equity", 'F2', 8)
pdf.add_text(340, y, "Rent", 'F2', 8)
pdf.add_text(395, y, "Expenses", 'F2', 8)
pdf.add_text(460, y, "Cash Flow", 'F2', 8)
pdf.add_text(530, y, "ROI%", 'F2', 8)
y -= 5
pdf.add_line(50, y, 562, y, 0.5)
y -= 15
for i in range(10):
    pdf.add_line(50, y, 155, y, 0.3, 0.7)
    pdf.add_line(160, y, 215, y, 0.3, 0.7)
    pdf.add_line(220, y, 275, y, 0.3, 0.7)
    pdf.add_line(280, y, 335, y, 0.3, 0.7)
    pdf.add_line(340, y, 390, y, 0.3, 0.7)
    pdf.add_line(395, y, 455, y, 0.3, 0.7)
    pdf.add_line(460, y, 525, y, 0.3, 0.7)
    pdf.add_line(530, y, 562, y, 0.3, 0.7)
    y -= 18
pdf.add_line(50, y, 562, y, 1)
y -= 18
pdf.add_text(50, y, "TOTALS:", 'F2', 10)
pdf.add_text(160, y, "$________", 'F2', 9)
pdf.add_text(220, y, "$________", 'F2', 9)
pdf.add_text(280, y, "$________", 'F2', 9)
pdf.add_text(340, y, "$________", 'F2', 9)
pdf.add_text(395, y, "$________", 'F2', 9)
pdf.add_text(460, y, "$________", 'F2', 9)
y -= 30
pdf.add_text(50, y, "Total monthly passive income: $__________", 'F2', 11)
pdf.add_text(50, y-20, "Total equity: $__________", 'F2', 11)
pdf.add_text(50, y-40, "Net worth from real estate: $__________", 'F2', 11)
pdf.add_text(50, y-70, "Next property target: ___________________________________", 'F1', 10)
pdf.add_text(50, y-90, "Annual portfolio growth goal: __________________________", 'F1', 10)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book195_Real_Estate_Investment_Tracker.pdf')
print("Book195_Real_Estate_Investment_Tracker.pdf created successfully!")
