"""Book 221: Small Business Finance Tracker"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.15)
    doc.add_centered_text(755, "SMALL BUSINESS", 'F2', 26, 1)
    doc.add_centered_text(722, "FINANCE TRACKER", 'F2', 26, 1)
    doc.add_centered_text(660, "Income, Expenses, Taxes & Profit All-in-One", 'F4', 14, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    # Copyright
    doc.new_page()
    doc.add_centered_text(700, "SMALL BUSINESS FINANCE TRACKER", 'F2', 14)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # Business Info Page
    doc.new_page()
    doc.add_centered_text(750, "BUSINESS INFORMATION", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    fields = [
        "Business Name: ________________________________",
        "Owner: ________________________________",
        "EIN/Tax ID: ________________________________",
        "Business Type: [ ] Sole Prop [ ] LLC [ ] S-Corp [ ] C-Corp",
        "State of Registration: ________________________________",
        "Date Started: ________________________________",
        "Fiscal Year: ________________________________",
        "Business Address: ________________________________",
        "________________________________",
        "Bank Account #: ________________________________",
        "Accountant: _________________ Phone: _____________",
        "Bookkeeper: _________________ Phone: _____________",
    ]
    for f in fields:
        doc.add_text(72, y, f, 'F1', 10)
        y -= 22


    # 12 Monthly P&L Pages
    months = ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE",
              "JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
    for month in months:
        doc.new_page()
        doc.add_centered_text(760, f"PROFIT & LOSS - {month}", 'F2', 13)
        doc.add_line(72, 748, 540, 748, 0.5, 0.3)
        y = 728
        doc.add_text(72, y, "INCOME", 'F2', 10)
        y -= 16
        income_cats = ["Product Sales", "Services", "Affiliate/Commission", "Other Income"]
        for cat in income_cats:
            doc.add_text(90, y, f"{cat}: $________", 'F1', 9)
            y -= 14
        doc.add_text(90, y, "TOTAL INCOME: $________", 'F2', 9)
        y -= 25
        doc.add_text(72, y, "EXPENSES", 'F2', 10)
        y -= 16
        expense_cats = ["Cost of Goods Sold (COGS)", "Marketing/Advertising",
                       "Software/Subscriptions", "Contractor/Freelancer",
                       "Office Supplies", "Travel/Meals", "Rent/Utilities",
                       "Insurance", "Professional Services", "Other"]
        for cat in expense_cats:
            doc.add_text(90, y, f"{cat}: $________", 'F1', 9)
            y -= 14
        doc.add_text(90, y, "TOTAL EXPENSES: $________", 'F2', 9)
        y -= 25
        doc.add_filled_rect(72, y-20, 468, 25, 0.9)
        doc.add_text(80, y, "MONTHLY SUMMARY", 'F2', 10)
        y -= 16
        doc.add_text(80, y, "Gross Revenue: $______ - Total Expenses: $______ = NET PROFIT: $______", 'F1', 9)

    # Quarterly Tax Estimation (4 pages)
    quarters = ["Q1 (Jan-Mar)", "Q2 (Apr-Jun)", "Q3 (Jul-Sep)", "Q4 (Oct-Dec)"]
    for q in quarters:
        doc.new_page()
        doc.add_centered_text(755, f"QUARTERLY TAX ESTIMATION - {q}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        lines = [
            "Gross Income this quarter: $________________",
            "Deductions this quarter: $________________",
            "Net taxable income: $________________", "",
            "Estimated tax rate: ___%",
            "Federal estimated tax: $________________",
            "State estimated tax: $________________",
            "Self-employment tax (15.3%): $________________",
            "TOTAL ESTIMATED TAX DUE: $________________", "",
            "Payment Record:",
            "Amount paid: $________  Date: ___/___/___",
            "Confirmation #: ________________",
            "Method: [ ] EFTPS [ ] Direct Pay [ ] Check", "",
            "Notes: ________________________________",
        ]
        for line in lines:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 20


    # Annual Summary Dashboard
    doc.new_page()
    doc.add_centered_text(755, "ANNUAL SUMMARY DASHBOARD", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "Year: ________", 'F1', 10)
    y -= 25
    doc.add_text(72, y, "QUARTERLY TOTALS:", 'F2', 10)
    y -= 18
    for q in ["Q1", "Q2", "Q3", "Q4"]:
        doc.add_text(90, y, f"{q}: Revenue $________ Expenses $________ Profit $________", 'F1', 9)
        y -= 16
    y -= 10
    doc.add_text(72, y, "ANNUAL TOTALS:", 'F2', 10)
    y -= 18
    doc.add_text(90, y, "Total Revenue: $________________", 'F1', 10)
    y -= 16
    doc.add_text(90, y, "Total Expenses: $________________", 'F1', 10)
    y -= 16
    doc.add_text(90, y, "Net Profit: $________________", 'F1', 10)
    y -= 16
    doc.add_text(90, y, "Profit Margin: ____%", 'F1', 10)
    y -= 16
    doc.add_text(90, y, "Total Taxes Paid: $________________", 'F1', 10)

    # Mileage Log (2 pages)
    for pg in range(1, 3):
        doc.new_page()
        doc.add_centered_text(755, f"MILEAGE LOG - PAGE {pg}", 'F2', 14)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        doc.add_text(72, y, "Date", 'F2', 8)
        doc.add_text(120, y, "From", 'F2', 8)
        doc.add_text(220, y, "To", 'F2', 8)
        doc.add_text(320, y, "Miles", 'F2', 8)
        doc.add_text(370, y, "Purpose", 'F2', 8)
        y -= 5
        doc.add_line(72, y, 540, y, 0.5, 0.3)
        for _ in range(25):
            y -= 18
            doc.add_line(72, y, 115, y, 0.5, 0.5)
            doc.add_line(120, y, 215, y, 0.5, 0.5)
            doc.add_line(220, y, 315, y, 0.5, 0.5)
            doc.add_line(320, y, 365, y, 0.5, 0.5)
            doc.add_line(370, y, 540, y, 0.5, 0.5)
        y -= 20
        doc.add_text(72, y, "Page Total Miles: ________  Rate: $0.67/mile  Deduction: $________", 'F1', 9)

    # Receipt Organization
    doc.new_page()
    doc.add_centered_text(755, "RECEIPT ORGANIZATION SYSTEM", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    lines = [
        "Digital Receipt System: [ ] Google Drive [ ] Dropbox [ ] Other: ________",
        "", "Folder Structure:",
        "  /Business_Receipts_[YEAR]/",
        "    /01_January/  /02_February/ ... /12_December/",
        "    /Categories/",
        "      /COGS/  /Marketing/  /Software/  /Travel/  /Office/", "",
        "Receipt Processing Schedule: Every _____________ (weekly recommended)", "",
        "Missing Receipts Log:",
        "Date: ___ Amount: $___ Vendor: ___________ Category: ___________",
        "Date: ___ Amount: $___ Vendor: ___________ Category: ___________",
        "Date: ___ Amount: $___ Vendor: ___________ Category: ___________",
        "Date: ___ Amount: $___ Vendor: ___________ Category: ___________",
    ]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 18

    # Accounts Receivable
    doc.new_page()
    doc.add_centered_text(755, "ACCOUNTS RECEIVABLE - INVOICES OUTSTANDING", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    doc.add_text(72, y, "Inv#", 'F2', 8)
    doc.add_text(110, y, "Client", 'F2', 8)
    doc.add_text(210, y, "Amount", 'F2', 8)
    doc.add_text(270, y, "Sent", 'F2', 8)
    doc.add_text(320, y, "Due", 'F2', 8)
    doc.add_text(370, y, "Paid?", 'F2', 8)
    doc.add_text(420, y, "Notes", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for _ in range(20):
        y -= 20
        doc.add_line(72, y, 540, y, 0.5, 0.5)

    # Accounts Payable
    doc.new_page()
    doc.add_centered_text(755, "ACCOUNTS PAYABLE - BILLS TO PAY", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    doc.add_text(72, y, "Vendor", 'F2', 8)
    doc.add_text(180, y, "Amount", 'F2', 8)
    doc.add_text(240, y, "Due Date", 'F2', 8)
    doc.add_text(310, y, "Paid?", 'F2', 8)
    doc.add_text(360, y, "Method", 'F2', 8)
    doc.add_text(430, y, "Notes", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for _ in range(20):
        y -= 20
        doc.add_line(72, y, 540, y, 0.5, 0.5)

    # Tax Deduction Checklist
    doc.new_page()
    doc.add_centered_text(755, "TAX DEDUCTION CHECKLIST BY CATEGORY", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    deductions = {
        "HOME OFFICE": ["Dedicated space sq ft: ___", "% of home: ___%", "Utilities portion: $___"],
        "VEHICLE": ["Business miles: ___", "Total miles: ___", "Business %: ___%"],
        "EDUCATION": ["Courses: $___", "Books: $___", "Conferences: $___"],
        "TECHNOLOGY": ["Computer: $___", "Phone: $___", "Software: $___"],
        "INSURANCE": ["Health (self-employed): $___", "Business: $___", "E&O: $___"],
        "RETIREMENT": ["SEP-IRA: $___", "Solo 401k: $___"],
        "MARKETING": ["Ads: $___", "Website: $___", "Business cards: $___"],
    }
    for cat, items in deductions.items():
        doc.add_text(72, y, cat, 'F2', 9)
        y -= 14
        for item in items:
            doc.add_text(90, y, f"[ ] {item}", 'F1', 8)
            y -= 12
        y -= 8

    # Year-End Tax Prep
    doc.new_page()
    doc.add_centered_text(755, "YEAR-END TAX PREPARATION WORKSHEET", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    items = [
        "[ ] All income recorded and categorized",
        "[ ] All expenses recorded with receipts",
        "[ ] Mileage log complete",
        "[ ] Home office measurements documented",
        "[ ] Quarterly estimated taxes paid (dates: ___/___/___/___)",
        "[ ] 1099s sent to contractors (if paid >$600)",
        "[ ] 1099s received from clients",
        "[ ] Inventory counted (if applicable)",
        "[ ] Depreciation schedule updated",
        "[ ] Health insurance premiums documented",
        "[ ] Retirement contributions maxed",
        "[ ] Charitable donations recorded",
        "[ ] State/local tax obligations met",
        "[ ] Final P&L generated",
        "[ ] Accountant meeting scheduled: ___/___/___",
    ]
    for item in items:
        doc.add_text(72, y, item, 'F1', 10)
        y -= 20

    doc.save("Book221_Small_Business_Finance_Tracker.pdf")
    print("Created: Book221_Small_Business_Finance_Tracker.pdf")

if __name__ == "__main__":
    create_book()
