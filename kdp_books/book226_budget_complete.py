"""Book 226: The Complete Budget System"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.2)
    doc.add_centered_text(755, "THE COMPLETE", 'F2', 26, 1)
    doc.add_centered_text(722, "BUDGET SYSTEM", 'F2', 26, 1)
    doc.add_centered_text(660, "Zero-Based Budget, Debt Payoff, Savings & Financial Goals", 'F4', 12, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    doc.new_page()
    doc.add_centered_text(700, "THE COMPLETE BUDGET SYSTEM", 'F2', 14)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # Financial Overview
    doc.new_page()
    doc.add_centered_text(750, "FINANCIAL OVERVIEW", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = ["INCOME SOURCES:", "  Job 1: $______/month", "  Job 2: $______/month",
        "  Side hustle: $______/month", "  Other: $______/month",
        "  TOTAL MONTHLY INCOME: $______", "",
        "DEBTS:", "  Debt 1: _____________ Balance: $______ Min payment: $______",
        "  Debt 2: _____________ Balance: $______ Min payment: $______",
        "  Debt 3: _____________ Balance: $______ Min payment: $______",
        "  Debt 4: _____________ Balance: $______ Min payment: $______",
        "  TOTAL DEBT: $______", "",
        "NET WORTH:", "  Assets (savings/investments/property): $______",
        "  Minus total debt: -$______",
        "  NET WORTH: $______", "  Date calculated: ___/___/___"]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 16


    # 12 Monthly Zero-Based Budget Pages
    months = ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE",
              "JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
    for month in months:
        doc.new_page()
        doc.add_centered_text(760, f"ZERO-BASED BUDGET - {month}", 'F2', 12)
        doc.add_text(72, 745, "Income: $________", 'F1', 9)
        doc.add_text(250, 745, "Every dollar has a job. Income - All Categories = $0", 'F4', 8)
        doc.add_line(72, 738, 540, 738, 0.5, 0.3)
        y = 722
        categories = [
            ("GIVING", ["Tithe/Church", "Charity"]),
            ("SAVINGS", ["Emergency Fund", "Retirement", "Other Savings"]),
            ("HOUSING", ["Mortgage/Rent", "Utilities", "Insurance", "Maintenance"]),
            ("FOOD", ["Groceries", "Restaurants"]),
            ("TRANSPORTATION", ["Car Payment", "Gas", "Insurance", "Maintenance"]),
            ("PERSONAL", ["Clothing", "Phone", "Subscriptions", "Fun Money"]),
            ("DEBT PAYMENTS", ["Extra debt payment"]),
        ]
        for cat_name, items in categories:
            doc.add_text(72, y, cat_name, 'F2', 8)
            doc.add_text(350, y, "Planned", 'F2', 7)
            doc.add_text(420, y, "Actual", 'F2', 7)
            doc.add_text(485, y, "Diff", 'F2', 7)
            y -= 12
            for item in items:
                doc.add_text(90, y, item, 'F1', 7)
                doc.add_text(350, y, "$_____", 'F1', 7)
                doc.add_text(420, y, "$_____", 'F1', 7)
                doc.add_text(485, y, "$_____", 'F1', 7)
                y -= 11
            y -= 6
        doc.add_line(72, y+3, 540, y+3, 0.5, 0.3)
        doc.add_text(72, y-5, "TOTAL EXPENSES: $______  REMAINING (should = $0): $______", 'F2', 9)

    # Debt Snowball Tracker
    doc.new_page()
    doc.add_centered_text(755, "DEBT SNOWBALL TRACKER", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "List debts smallest to largest balance:", 'F4', 10)
    y -= 20
    doc.add_text(72, y, "Debt Name", 'F2', 8)
    doc.add_text(190, y, "Balance", 'F2', 8)
    doc.add_text(260, y, "Rate", 'F2', 8)
    doc.add_text(305, y, "Min Pmt", 'F2', 8)
    doc.add_text(375, y, "Extra Pmt", 'F2', 8)
    doc.add_text(450, y, "Payoff Date", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for _ in range(10):
        y -= 22
        doc.add_line(72, y, 185, y, 0.5, 0.5)
        doc.add_line(190, y, 255, y, 0.5, 0.5)
        doc.add_line(260, y, 300, y, 0.5, 0.5)
        doc.add_line(305, y, 370, y, 0.5, 0.5)
        doc.add_line(375, y, 445, y, 0.5, 0.5)
        doc.add_line(450, y, 540, y, 0.5, 0.5)
    y -= 25
    doc.add_text(72, y, "Total debt: $______  Monthly payment total: $______", 'F1', 10)
    y -= 16
    doc.add_text(72, y, "Debt-free target date: ___/___/___", 'F2', 10)

    # Sinking Funds Planner
    doc.new_page()
    doc.add_centered_text(755, "SINKING FUNDS PLANNER", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "Save monthly for predictable expenses:", 'F4', 10)
    y -= 22
    funds = ["Christmas/Gifts", "Car Maintenance", "Medical/Dental", "Vacation",
             "Home Repairs", "Insurance (annual)", "Back to School", "Birthday Parties",
             "Pet Expenses", "Technology Replacement", "Clothing", "Emergency Buffer"]
    doc.add_text(72, y, "Fund", 'F2', 8)
    doc.add_text(220, y, "Goal $", 'F2', 8)
    doc.add_text(290, y, "By When", 'F2', 8)
    doc.add_text(365, y, "Monthly $", 'F2', 8)
    doc.add_text(445, y, "Saved $", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for fund in funds:
        y -= 20
        doc.add_text(72, y, fund, 'F1', 9)
        doc.add_text(220, y, "$_____", 'F1', 9)
        doc.add_text(290, y, "___/___", 'F1', 9)
        doc.add_text(365, y, "$_____", 'F1', 9)
        doc.add_text(445, y, "$_____", 'F1', 9)


    # Emergency Fund Progress
    doc.new_page()
    doc.add_centered_text(755, "EMERGENCY FUND PROGRESS", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    lines = ["Step 1: Calculate 6 months of essential expenses:", "",
        "  Rent/mortgage: $______ x 6 = $______",
        "  Utilities: $______ x 6 = $______",
        "  Food: $______ x 6 = $______",
        "  Insurance: $______ x 6 = $______",
        "  Transportation: $______ x 6 = $______",
        "  Minimum debt payments: $______ x 6 = $______",
        "  Other essentials: $______ x 6 = $______", "",
        "  TOTAL 6-MONTH EMERGENCY FUND GOAL: $______", "",
        "Step 2: Monthly contribution: $______",
        "Step 3: Target completion date: ___/___/___", "",
        "PROGRESS:", "  Month 1: $______  Month 2: $______  Month 3: $______",
        "  Month 4: $______  Month 5: $______  Month 6: $______",
        "  Month 7: $______  Month 8: $______  Month 9: $______",
        "  Month 10: $______ Month 11: $______ Month 12: $______"]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Savings Goals
    doc.new_page()
    doc.add_centered_text(755, "SAVINGS GOALS TRACKER", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    for g in range(1, 6):
        doc.add_text(72, y, f"GOAL {g}: ________________________________", 'F2', 10)
        y -= 16
        doc.add_text(90, y, "Amount needed: $______  By when: ___/___/___", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Monthly savings: $______  Current total: $______", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Progress: |____|____|____|____|____|____|____|____|____|____|", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "           10%  20%  30%  40%  50%  60%  70%  80%  90% 100%", 'F3', 7)
        y -= 25

    # Bill Calendar
    doc.new_page()
    doc.add_centered_text(755, "ANNUAL BILL CALENDAR", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    doc.add_text(72, y, "Date", 'F2', 8)
    doc.add_text(110, y, "Bill", 'F2', 8)
    doc.add_text(250, y, "Amount", 'F2', 8)
    doc.add_text(315, y, "Auto?", 'F2', 8)
    doc.add_text(365, y, "Account", 'F2', 8)
    doc.add_text(450, y, "Paid", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for _ in range(25):
        y -= 18
        doc.add_line(72, y, 540, y, 0.5, 0.5)

    # Subscription Audit
    doc.new_page()
    doc.add_centered_text(755, "SUBSCRIPTION AUDIT", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    doc.add_text(72, y, "Service", 'F2', 8)
    doc.add_text(220, y, "Cost/mo", 'F2', 8)
    doc.add_text(290, y, "Annual", 'F2', 8)
    doc.add_text(355, y, "Use Often?", 'F2', 8)
    doc.add_text(435, y, "Keep/Cancel", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for _ in range(20):
        y -= 20
        doc.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    doc.add_text(72, y, "Total monthly: $______  Total annual: $______  After audit: $______/mo", 'F2', 9)

    # Weekly Spending Tracker (12 pages)
    for wk in range(1, 13):
        doc.new_page()
        doc.add_centered_text(760, f"WEEKLY SPENDING - WEEK {wk}", 'F2', 12)
        doc.add_line(72, 748, 540, 748, 0.5, 0.3)
        y = 730
        days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        for day in days:
            doc.add_text(72, y, day, 'F2', 8)
            y -= 13
            for _ in range(3):
                doc.add_text(100, y, "Item: _____________ $_____ Category: _________", 'F1', 7)
                y -= 11
            y -= 5
        doc.add_text(72, y, "Weekly total: $______  Budget remaining: $______", 'F2', 9)

    # Net Worth Tracker (quarterly) + Annual Review + Goals
    doc.new_page()
    doc.add_centered_text(755, "NET WORTH TRACKER & ANNUAL REVIEW", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "QUARTERLY NET WORTH:", 'F2', 10)
    y -= 18
    for q in ["Q1", "Q2", "Q3", "Q4"]:
        doc.add_text(90, y, f"{q}: Assets $______ - Debts $______ = Net Worth $______", 'F1', 9)
        y -= 16
    y -= 15
    doc.add_text(72, y, "ANNUAL FINANCIAL REVIEW:", 'F2', 10)
    y -= 16
    review = ["Total earned this year: $______",
        "Total saved this year: $______  (___% of income)",
        "Total debt paid off: $______",
        "Net worth change: +/- $______",
        "Biggest financial win: ________________________________",
        "Biggest challenge: ________________________________"]
    for item in review:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 16
    y -= 15
    doc.add_text(72, y, "FINANCIAL GOALS NEXT YEAR:", 'F2', 10)
    y -= 16
    for i in range(1, 6):
        doc.add_text(90, y, f"{i}. ________________________________", 'F1', 9)
        y -= 16

    doc.save("Book226_Budget_Planner_Complete.pdf")
    print("Created: Book226_Budget_Planner_Complete.pdf")

if __name__ == "__main__":
    create_book()
