from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(550, "ZERO-BASED BUDGET WORKBOOK", 'F2', 18)
pdf.add_centered_text(520, "Give Every Dollar a Job", 'F4', 14)
pdf.add_centered_text(400, "12 Months of Zero-Based Budgeting Templates", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, "ZERO-BASED BUDGET WORKBOOK", 'F2', 12)
pdf.add_centered_text(575, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: What is Zero-Based Budgeting
pdf.new_page()
pdf.add_centered_text(750, "WHAT IS ZERO-BASED BUDGETING?", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Zero-based budgeting means: INCOME - EXPENSES = $0", "",
    "Every single dollar has a job. Nothing is left 'floating around'",
    "without a purpose. This doesn't mean you spend everything -",
    "savings and debt payoff ARE jobs for your dollars.", "",
    "THE FORMULA:",
    "Total Income - Total Expenses - Savings - Giving = $0", "",
    "WHY IT WORKS:",
    "- You tell your money where to go instead of wondering where it went",
    "- You make spending decisions BEFORE the month, not during",
    "- Every dollar is intentional",
    "- You catch overspending immediately",
    "- You prioritize what matters most", "",
    "HOW TO USE THIS WORKBOOK:",
    "1. Calculate your total monthly income",
    "2. List ALL expenses by category",
    "3. Assign dollars to each category until you hit $0",
    "4. Track actual spending throughout the month",
    "5. Adjust next month based on what you learn", "",
    "RULES:",
    "- Do the budget BEFORE the month starts",
    "- Both partners must agree (if applicable)",
    "- Adjust mid-month if needed (life happens)",
    "- The goal is progress, not perfection"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 4: Income Calculation
pdf.new_page()
pdf.add_centered_text(750, "INCOME CALCULATION WORKSHEET", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "List ALL sources of income (use TAKE-HOME pay, after taxes):", "",
    "REGULAR INCOME:",
    "Job 1 (paycheck 1): $_________ Frequency: ______",
    "Job 1 (paycheck 2): $_________ Frequency: ______",
    "Job 2: $________________ Frequency: ____________",
    "Spouse/Partner income: $_______ Frequency: ______", "",
    "ADDITIONAL INCOME:",
    "Side hustle/freelance: $________________________",
    "Child support/alimony: $________________________",
    "Government benefits: $_________________________",
    "Rental income: $______________________________",
    "Other: $______________________________________", "",
    "TOTAL MONTHLY INCOME: $_______________________", "",
    "IF IRREGULAR INCOME:",
    "Use your LOWEST month from the past 6 months as your baseline.",
    "Lowest month was: $____________________________",
    "If you earn more, put extra toward savings/debt first."
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 18

# Page 5: Fixed Expenses + Variable Expenses
pdf.new_page()
pdf.add_centered_text(750, "FIXED & VARIABLE EXPENSES", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "FIXED EXPENSES (same every month):", "",
    "Rent/Mortgage:          $________",
    "Car payment:            $________",
    "Insurance (auto):       $________",
    "Insurance (health):     $________",
    "Phone:                  $________",
    "Internet:               $________",
    "Subscriptions:          $________",
    "Childcare/tuition:      $________",
    "Minimum debt payments:  $________",
    "Other fixed:            $________",
    "TOTAL FIXED: $___________", "",
    "VARIABLE EXPENSES (change monthly):", "",
    "Groceries:              $________",
    "Gas/Transportation:     $________",
    "Utilities (electric/gas/water): $________",
    "Eating out:             $________",
    "Entertainment:          $________",
    "Clothing:               $________",
    "Personal care:          $________",
    "Household items:        $________",
    "TOTAL VARIABLE: $___________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 6: Sinking Funds + Budget Categories
pdf.new_page()
pdf.add_centered_text(750, "SINKING FUNDS PLANNER", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Sinking funds = saving monthly for expenses that come periodically.", "",
    "ANNUAL/IRREGULAR EXPENSES:        Total    Monthly Set-Aside",
    "Car registration/inspection:      $____    $____ / 12 = $____",
    "Car maintenance/repairs:          $____    $____ / 12 = $____",
    "Christmas/holidays:               $____    $____ / 12 = $____",
    "Birthdays:                        $____    $____ / 12 = $____",
    "Back to school:                   $____    $____ / 12 = $____",
    "Home maintenance:                 $____    $____ / 12 = $____",
    "Medical (copays, dental):         $____    $____ / 12 = $____",
    "Vacation:                         $____    $____ / 12 = $____",
    "Annual subscriptions:             $____    $____ / 12 = $____",
    "Property taxes (if not escrowed): $____    $____ / 12 = $____",
    "Pet expenses:                     $____    $____ / 12 = $____",
    "Other: _______________          $____    $____ / 12 = $____", "",
    "TOTAL SINKING FUNDS MONTHLY: $________________", "",
    "Keep sinking funds in a separate savings account.",
    "Label them! (Many banks allow sub-accounts or use envelopes.)"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 18

# Pages 7-18: 12 Monthly Zero-Based Budget Worksheets
months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE",
    "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
for month in months:
    pdf.new_page()
    pdf.add_centered_text(755, f"{month} ZERO-BASED BUDGET", 'F2', 14)
    pdf.add_line(60, 743, 552, 743)
    y = 728
    pdf.add_text(60, y, "INCOME:  $____________", 'F2', 10)
    y -= 18
    categories = [
        ("GIVING/TITHE:", ["Tithe", "Charity"]),
        ("SAVINGS:", ["Emergency fund", "Sinking funds", "Retirement"]),
        ("HOUSING:", ["Rent/Mortgage", "Utilities", "Phone/Internet"]),
        ("FOOD:", ["Groceries", "Eating out"]),
        ("TRANSPORTATION:", ["Gas", "Car payment", "Insurance"]),
        ("INSURANCE:", ["Health", "Life"]),
        ("PERSONAL:", ["Clothing", "Personal care", "Entertainment"]),
        ("DEBT:", ["Credit card", "Student loan", "Other"])
    ]
    for cat_name, items in categories:
        pdf.add_text(60, y, cat_name, 'F2', 9)
        y -= 13
        for item in items:
            pdf.add_text(75, y, f"{item}:  Planned $____  Actual $____", 'F3', 8)
            y -= 12
        y -= 4
    y -= 5
    pdf.add_text(60, y, "TOTAL EXPENSES: $________  INCOME - EXPENSES = $______ (should be $0)", 'F2', 9)


# Page 19: Irregular Income Planning
pdf.new_page()
pdf.add_centered_text(750, "IRREGULAR INCOME PLANNING", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "If your income varies (freelance, commission, gig work):", "",
    "STEP 1: List expenses in PRIORITY ORDER",
    "(If you only had $1000 this month, what gets paid first?)", "",
    "Priority 1: _________________ $________________",
    "Priority 2: _________________ $________________",
    "Priority 3: _________________ $________________",
    "Priority 4: _________________ $________________",
    "Priority 5: _________________ $________________",
    "Priority 6: _________________ $________________",
    "Priority 7: _________________ $________________",
    "Priority 8: _________________ $________________",
    "Priority 9: _________________ $________________",
    "Priority 10: ________________ $________________", "",
    "STEP 2: As income comes in, fund priorities top-down.",
    "Draw a line where the money runs out. Below the line waits.", "",
    "BUFFER ACCOUNT:",
    "Build a buffer of 1 month's expenses in checking.",
    "This month's income pays NEXT month's budget.",
    "Buffer goal: $________________________________",
    "Current buffer: $______________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 20: Debt Snowball Calculator
pdf.new_page()
pdf.add_centered_text(750, "DEBT SNOWBALL CALCULATOR", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "List ALL debts smallest to largest balance:", "",
    "DEBT                   BALANCE    MIN PAYMENT    RATE",
    "1. ________________   $________  $________      ___%",
    "2. ________________   $________  $________      ___%",
    "3. ________________   $________  $________      ___%",
    "4. ________________   $________  $________      ___%",
    "5. ________________   $________  $________      ___%",
    "6. ________________   $________  $________      ___%",
    "7. ________________   $________  $________      ___%", "",
    "TOTAL DEBT: $______________",
    "Total minimum payments: $______________",
    "Extra I can throw at debt monthly: $___________", "",
    "SNOWBALL METHOD:",
    "1. Pay minimums on everything",
    "2. Put ALL extra money toward smallest debt",
    "3. When #1 is paid off, roll its payment to #2",
    "4. Keep rolling until all debt is gone!", "",
    "Estimated debt-free date: _____________________", "",
    "MOTIVATION: When I'm debt-free, I will:",
    "_______________________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 21: Emergency Fund + Annual Planning + Review
pdf.new_page()
pdf.add_centered_text(750, "EMERGENCY FUND & ANNUAL PLANNING", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "EMERGENCY FUND TRACKER:", "",
    "Goal: $________________ (3-6 months of expenses)",
    "Current balance: $____________________________",
    "Monthly contribution: $________________________",
    "Target completion date: _______________________", "",
    "ANNUAL EXPENSE PLANNING:", "",
    "Jan: ___________________ Jul: ___________________",
    "Feb: ___________________ Aug: ___________________",
    "Mar: ___________________ Sep: ___________________",
    "Apr: ___________________ Oct: ___________________",
    "May: ___________________ Nov: ___________________",
    "Jun: ___________________ Dec: ___________________", "",
    "BUDGET REVIEW & ADJUSTMENT:", "",
    "What category do I consistently overspend?",
    "_______________________________________________",
    "Do I need to increase this budget or cut spending?",
    "_______________________________________________",
    "What category has money left over? Reallocate to:",
    "_______________________________________________", "",
    "Remember: A budget is not a cage. It's FREEDOM.",
    "You're telling your money where to go so it stops disappearing."
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book109b_Zero_Based_Budget.pdf')
print("Book109b_Zero_Based_Budget.pdf created successfully!")
