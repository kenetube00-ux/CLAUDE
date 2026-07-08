from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(490, "FREELANCER INCOME", 'F2', 16)
pdf.add_centered_text(468, "& TAX TRACKER", 'F2', 16)
pdf.add_centered_text(435, "Organize Your Self-Employment Finances", 'F4', 12)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(500, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)
pdf.add_centered_text(475, "This is not tax advice. Consult a CPA for your situation.", 'F4', 9)

# Page 3: Business Information
pdf.new_page()
pdf.add_centered_text(610, "BUSINESS INFORMATION", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "Business name: ________________________________",
    "Business type: Sole Prop / LLC / S-Corp",
    "EIN: __________________________________________",
    "State tax ID: _________________________________",
    "Business start date: __________________________",
    "Industry: _____________________________________", "",
    "BANK ACCOUNTS:",
    "Business checking: ____________________________",
    "Business savings: _____________________________",
    "Tax savings account: __________________________", "",
    "PROFESSIONALS:",
    "CPA/Accountant: ______________ Phone: _________",
    "Bookkeeper: __________________ Phone: _________",
    "Attorney: ____________________ Phone: _________", "",
    "TAX FILING STATUS: ___________________________",
    "Estimated tax bracket: ________________________",
    "State income tax rate: ________________________", "",
    "IMPORTANT: Set aside 25-30% of income for taxes.",
    "Put it in a separate account immediately when paid."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Pages 4-15: Monthly Income Tracker (12 pages)
months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE",
    "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
for month in months:
    pdf.new_page()
    pdf.add_centered_text(618, f"INCOME TRACKER - {month}", 'F2', 12)
    pdf.add_line(50, 608, 382, 608)
    y = 592
    pdf.add_text(50, y, "Client/Project          Invoice#   Amount    Date Paid  Platform", 'F2', 7)
    y -= 5
    pdf.add_line(50, y, 382, y, 0.5)
    y -= 12
    for i in range(15):
        pdf.add_text(50, y, "___________________  ______  $______  ___/___  ________", 'F3', 7)
        y -= 13
    y -= 8
    pdf.add_text(50, y, f"TOTAL {month} INCOME: $___________", 'F2', 9)
    y -= 15
    pdf.add_text(50, y, f"Tax set aside (30%): $___________", 'F2', 9)


# Pages 16-19: Quarterly Tax Estimation (4 pages)
quarters = [("Q1 (Jan-Mar)", "April 15"), ("Q2 (Apr-May)", "June 15"),
    ("Q3 (Jun-Aug)", "September 15"), ("Q4 (Sep-Dec)", "January 15")]
for q_name, due in quarters:
    pdf.new_page()
    pdf.add_centered_text(610, f"QUARTERLY TAX ESTIMATION - {q_name}", 'F2', 12)
    pdf.add_line(50, 598, 382, 598)
    y = 575
    for line in [
        f"DUE DATE: {due}", "",
        "GROSS INCOME this quarter:       $___________",
        "Deductible expenses:             -$___________",
        "NET INCOME (taxable):             $___________", "",
        "ESTIMATED TAX CALCULATION:",
        "Federal self-employment tax (15.3%): $________",
        "Federal income tax (est. bracket):   $________",
        "State income tax:                    $________",
        "TOTAL ESTIMATED TAX:                 $________", "",
        "Amount already set aside:            $________",
        "Additional amount needed:            $________", "",
        "PAYMENT CONFIRMATION:",
        "Date paid: ___/___/___",
        "Amount paid: $___________",
        "Payment method: EFTPS / Direct Pay / Check",
        "Confirmation #: ___________________________"
    ]:
        pdf.add_text(50, y, line, 'F4', 10)
        y -= 16

# Page 20: Deductible Expenses
pdf.new_page()
pdf.add_centered_text(610, "DEDUCTIBLE EXPENSES TRACKER", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "Track expenses by category (keep ALL receipts!):", "",
    "HOME OFFICE (sq ft method or simplified $5/sq ft):",
    "Total home sq ft: _____ Office sq ft: _____ = ___%",
    "Annual amount: $___________", "",
    "EQUIPMENT/SUPPLIES: $_________ (computer, printer, desk)",
    "SOFTWARE/SUBSCRIPTIONS: $_____ (Adobe, Zoom, etc.)",
    "PHONE/INTERNET (business %): $________________",
    "PROFESSIONAL DEVELOPMENT: $_____ (courses, books)",
    "TRAVEL: $_____ (flights, hotels, meals at 50%)",
    "HEALTH INSURANCE PREMIUMS: $___________________",
    "RETIREMENT CONTRIBUTIONS: $____________________",
    "ADVERTISING/MARKETING: $_______________________",
    "PROFESSIONAL SERVICES: $______ (CPA, legal, VA)",
    "MEALS (business, 50%): $_______________________",
    "OTHER: ________________________________________", "",
    "TOTAL ANNUAL DEDUCTIONS: $_____________________", "",
    "MILEAGE LOG: Standard rate or actual expenses",
    "Date    From/To    Miles    Purpose",
]:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 13

# Pages 21-22: 1099 Tracking + Annual Summary
pdf.new_page()
pdf.add_centered_text(610, "1099 TRACKING & ANNUAL SUMMARY", 'F2', 13)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "CLIENTS WHO WILL SEND 1099-NEC (paid you $600+):", "",
    "Client: _____________________ Expected: $______",
    "Client: _____________________ Expected: $______",
    "Client: _____________________ Expected: $______",
    "Client: _____________________ Expected: $______",
    "Client: _____________________ Expected: $______",
    "Client: _____________________ Expected: $______", "",
    "ANNUAL INCOME SUMMARY:",
    "Total gross income: $__________________________",
    "Total deductions: $____________________________",
    "Net profit (Schedule C): $______________________",
    "Total tax paid (quarterly): $___________________",
    "Refund / Amount owed: $_______________________", "",
    "TAX PREP CHECKLIST:",
    "__ All 1099s received (by Jan 31)",
    "__ Mileage log complete",
    "__ Home office calculation done",
    "__ Receipts organized by category",
    "__ Health insurance premiums documented",
    "__ Retirement contributions recorded",
    "__ Business bank statements reconciled"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14

# Page 23: Important Tax Dates + Retirement
pdf.new_page()
pdf.add_centered_text(610, "TAX DATES & RETIREMENT", 'F2', 14)
pdf.add_line(50, 598, 382, 598)
y = 575
for line in [
    "IMPORTANT TAX DATES:", "",
    "January 15: Q4 estimated tax due",
    "January 31: 1099s should arrive from clients",
    "April 15: Q1 estimated tax + annual return due",
    "June 15: Q2 estimated tax due",
    "September 15: Q3 estimated tax due",
    "October 15: Extended return due (if filed extension)", "",
    "RETIREMENT OPTIONS FOR SELF-EMPLOYED:", "",
    "SEP-IRA: Contribute up to 25% of net income (max ~$69K)",
    "  - Easy to set up, flexible contributions",
    "  - Can fund until tax filing deadline", "",
    "SOLO 401(k): Higher contribution limits",
    "  - Employee + employer contributions",
    "  - More paperwork but more savings potential", "",
    "MY RETIREMENT PLAN:",
    "Account type: _________________________________",
    "Annual contribution goal: $____________________",
    "Monthly set-aside: $___________________________", "",
    "Pay yourself first. Even $100/month grows significantly."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book117_Freelancer_Income_Tax.pdf')
print("Book117_Freelancer_Income_Tax.pdf created successfully!")
