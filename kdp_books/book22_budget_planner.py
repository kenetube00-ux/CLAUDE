"""
Book 22: MONTHLY BUDGET PLANNER - Take Control of Your Money
KDP Interior - 6x9 inches (432x648 points)
Title page + copyright + 12 monthly budget sheets + 12 expense tracker pages + savings goal page
"""
from pdf_utils import PDFDoc

def create_budget_planner():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(530, "MONTHLY", font='F2', size=26)
    pdf.add_centered_text(495, "BUDGET PLANNER", font='F2', size=26)
    pdf.add_line(100, 475, 332, 475, 2)
    pdf.add_centered_text(450, "Take Control of Your Money", font='F4', size=14)
    pdf.add_centered_text(390, "Track Income & Expenses", font='F1', size=11)
    pdf.add_centered_text(368, "12 Monthly Budget Worksheets", font='F1', size=11)
    pdf.add_centered_text(346, "Expense Tracking & Savings Goals", font='F1', size=11)
    pdf.add_centered_text(270, "By", font='F1', size=11)
    pdf.add_centered_text(248, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "MONTHLY BUDGET PLANNER", font='F2', size=12)
    pdf.add_centered_text(498, "Take Control of Your Money", font='F1', size=10)
    pdf.add_centered_text(470, "By Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(435, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(415, "ISBN: _______________", font='F1', size=9)
    pdf.add_centered_text(395, "Published via Amazon KDP", font='F1', size=9)

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # --- 12 MONTHLY BUDGET SHEETS ---
    for month_idx, month in enumerate(months):
        pdf.new_page()
        pdf.add_text(60, 615, f"{month.upper()} BUDGET", font='F2', size=14)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 580
        # Income Section
        pdf.add_text(60, y, "INCOME", font='F2', size=11)
        y -= 20
        income_items = ["Salary/Wages", "Side Hustle", "Other Income"]
        for item in income_items:
            pdf.add_text(70, y, item, font='F1', size=9)
            pdf.add_text(200, y, "$", font='F1', size=9)
            pdf.add_line(210, y - 2, 300, y - 2, 0.3, gray=0.5)
            y -= 18
        pdf.add_text(70, y, "TOTAL INCOME", font='F2', size=9)
        pdf.add_text(200, y, "$", font='F2', size=9)
        pdf.add_line(210, y - 2, 300, y - 2, 0.5)
        y -= 30

        # Expenses Section
        pdf.add_text(60, y, "EXPENSES", font='F2', size=11)
        pdf.add_text(230, y, "Budget", font='F2', size=9)
        pdf.add_text(310, y, "Actual", font='F2', size=9)
        y -= 20
        expense_items = ["Housing/Rent", "Utilities", "Food/Groceries", "Transportation",
                        "Insurance", "Entertainment", "Savings", "Debt Payments"]
        for item in expense_items:
            pdf.add_text(70, y, item, font='F1', size=9)
            pdf.add_text(220, y, "$", font='F1', size=9)
            pdf.add_line(230, y - 2, 295, y - 2, 0.3, gray=0.5)
            pdf.add_text(305, y, "$", font='F1', size=9)
            pdf.add_line(315, y - 2, 372, y - 2, 0.3, gray=0.5)
            y -= 18
        pdf.add_line(60, y + 5, 372, y + 5, 0.5)
        pdf.add_text(70, y - 8, "TOTAL EXPENSES", font='F2', size=9)
        pdf.add_text(220, y - 8, "$", font='F2', size=9)
        pdf.add_line(230, y - 10, 295, y - 10, 0.5)
        pdf.add_text(305, y - 8, "$", font='F2', size=9)
        pdf.add_line(315, y - 10, 372, y - 10, 0.5)
        y -= 35

        # Summary
        pdf.add_text(60, y, "SUMMARY", font='F2', size=11)
        y -= 20
        pdf.add_text(70, y, "Total Income:", font='F1', size=9)
        pdf.add_text(200, y, "$", font='F1', size=9)
        pdf.add_line(210, y - 2, 300, y - 2, 0.3, gray=0.5)
        y -= 18
        pdf.add_text(70, y, "Total Expenses:", font='F1', size=9)
        pdf.add_text(200, y, "$", font='F1', size=9)
        pdf.add_line(210, y - 2, 300, y - 2, 0.3, gray=0.5)
        y -= 18
        pdf.add_text(70, y, "Remaining:", font='F2', size=9)
        pdf.add_text(200, y, "$", font='F2', size=9)
        pdf.add_line(210, y - 2, 300, y - 2, 0.5)

        pdf.add_centered_text(30, f"- {month_idx + 3} -", font='F1', size=8)

    # --- 12 EXPENSE TRACKER PAGES ---
    for month_idx, month in enumerate(months):
        pdf.new_page()
        pdf.add_text(60, 615, f"{month.upper()} - EXPENSE TRACKER", font='F2', size=12)
        pdf.add_line(60, 603, 372, 603, 0.8)

        y = 582
        # Column headers
        pdf.add_text(60, y, "Date", font='F2', size=8)
        pdf.add_text(105, y, "Description", font='F2', size=8)
        pdf.add_text(235, y, "Category", font='F2', size=8)
        pdf.add_text(320, y, "Amount", font='F2', size=8)
        pdf.add_line(60, y - 5, 372, y - 5, 0.5)
        y -= 18

        # 25 rows
        for row in range(25):
            pdf.add_line(60, y, 95, y, 0.3, gray=0.5)
            pdf.add_line(105, y, 225, y, 0.3, gray=0.5)
            pdf.add_line(235, y, 310, y, 0.3, gray=0.5)
            pdf.add_line(320, y, 372, y, 0.3, gray=0.5)
            y -= 20

        # Total
        pdf.add_text(235, y, "TOTAL:", font='F2', size=9)
        pdf.add_text(320, y, "$", font='F2', size=9)
        pdf.add_line(330, y - 2, 372, y - 2, 0.5)

        pdf.add_centered_text(30, f"- {month_idx + 15} -", font='F1', size=8)

    # --- SAVINGS GOAL PAGE ---
    pdf.new_page()
    pdf.add_text(60, 615, "SAVINGS GOALS", font='F2', size=14)
    pdf.add_line(60, 603, 372, 603, 0.8)

    y = 575
    for goal in range(5):
        pdf.add_text(60, y, f"Goal #{goal + 1}:", font='F2', size=10)
        pdf.add_line(115, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22
        pdf.add_text(70, y, "Target Amount: $", font='F1', size=9)
        pdf.add_line(160, y - 2, 250, y - 2, 0.3, gray=0.5)
        pdf.add_text(260, y, "Deadline:", font='F1', size=9)
        pdf.add_line(305, y - 2, 372, y - 2, 0.3, gray=0.5)
        y -= 22
        pdf.add_text(70, y, "Monthly Savings Needed: $", font='F1', size=9)
        pdf.add_line(210, y - 2, 300, y - 2, 0.3, gray=0.5)
        y -= 22
        pdf.add_text(70, y, "Progress:", font='F1', size=9)
        # Progress bar outline
        pdf.add_rect(120, y - 3, 200, 12, 0.4)
        y -= 35

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book22_Monthly_Budget_Planner.pdf')
    print("Book 22 created: Book22_Monthly_Budget_Planner.pdf")

if __name__ == '__main__':
    create_budget_planner()
