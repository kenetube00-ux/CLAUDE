#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(420, "DEBT FREE JOURNEY", 'F2', 18)
pdf.add_centered_text(395, "WORKBOOK", 'F2', 18)
pdf.add_centered_text(360, "The Complete Snowball Method Planner", 'F4', 12)
pdf.add_centered_text(330, f"By {author}", 'F4', 11)
pdf.add_line(80, 310, 352, 310, 2)

# Page 2 - Copyright + Your Why
pdf.new_page()
pdf.add_centered_text(620, f"Copyright - {author}", 'F1', 9)
pdf.add_centered_text(605, "All rights reserved.", 'F1', 9)

# Page 3 - Your Why
pdf.new_page()
pdf.add_centered_text(620, "YOUR WHY", 'F2', 16)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "WHY do you want to be debt free? (Write this when motivation is high)", 'F1', 9)
y = 570
for i in range(6):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 16
pdf.add_text(40, y-10, "What will life look like debt-free?", 'F2', 10)
y -= 30
for i in range(5):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 16
pdf.add_text(40, y-10, "What can I NOT do right now because of debt?", 'F2', 10)
y -= 30
for i in range(4):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 16
pdf.add_text(40, y-10, "My debt-free target date: _______________", 'F2', 10)
pdf.add_text(40, y-28, "Who am I doing this for: _______________", 'F1', 9)

# Page 4 - Total Debt Inventory
pdf.new_page()
pdf.add_centered_text(620, "TOTAL DEBT INVENTORY", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 595, "List ALL debts (be honest - every single one):", 'F1', 9)
y = 578
pdf.add_text(40, y, "Creditor", 'F2', 8)
pdf.add_text(140, y, "Balance", 'F2', 8)
pdf.add_text(200, y, "Min Pmt", 'F2', 8)
pdf.add_text(260, y, "Rate%", 'F2', 8)
pdf.add_text(310, y, "Type", 'F2', 8)
y -= 5
pdf.add_line(40, y, 392, y, 0.5)
y -= 14
for i in range(15):
    pdf.add_line(40, y, 135, y, 0.3, 0.7)
    pdf.add_text(140, y+2, "$", 'F1', 7)
    pdf.add_line(150, y, 195, y, 0.3, 0.7)
    pdf.add_text(200, y+2, "$", 'F1', 7)
    pdf.add_line(210, y, 255, y, 0.3, 0.7)
    pdf.add_line(260, y, 305, y, 0.3, 0.7)
    pdf.add_line(310, y, 392, y, 0.3, 0.7)
    y -= 16
pdf.add_line(40, y, 392, y, 1)
y -= 14
pdf.add_text(40, y, "TOTAL DEBT: $__________", 'F2', 10)
pdf.add_text(220, y, "TOTAL MINIMUM PAYMENTS: $__________", 'F2', 9)
pdf.add_text(40, y-18, "How does this number make you feel?", 'F1', 9)
pdf.add_line(40, y-32, 392, y-32, 0.5, 0.7)

# Page 5 - Debt Snowball Order
pdf.new_page()
pdf.add_centered_text(620, "DEBT SNOWBALL ORDER", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "List debts SMALLEST to LARGEST balance (ignore interest rates!):", 'F2', 9)
pdf.add_text(40, 575, "Pay minimums on everything. Attack the smallest with gazelle intensity!", 'F1', 8)
y = 555
for i in range(1, 16):
    pdf.add_text(40, y, f"{i}.", 'F2', 9)
    pdf.add_text(55, y, "___________________", 'F1', 8)
    pdf.add_text(180, y, "$_________", 'F1', 8)
    pdf.add_text(260, y, "Min: $_______", 'F1', 8)
    pdf.add_rect(350, y-5, 9, 9)
    pdf.add_text(363, y-3, "PAID!", 'F1', 7)
    y -= 18
pdf.add_text(40, y-10, "When #1 is paid, add its payment to #2. SNOWBALL!", 'F2', 9, 0.3)


# Pages 6-17 - Monthly Debt Payment Tracker (12 pages)
for month in range(1, 13):
    pdf.new_page()
    pdf.add_centered_text(620, f"MONTHLY DEBT TRACKER - MONTH {month}", 'F2', 12)
    pdf.add_line(40, 610, 392, 610, 1)
    pdf.add_text(40, 595, "Month/Year: _______________  Extra $ available: $______", 'F1', 9)
    y = 575
    pdf.add_text(40, y, "Debt Name", 'F2', 7)
    pdf.add_text(140, y, "Balance", 'F2', 7)
    pdf.add_text(195, y, "Min", 'F2', 7)
    pdf.add_text(235, y, "Extra", 'F2', 7)
    pdf.add_text(280, y, "Total Paid", 'F2', 7)
    pdf.add_text(342, y, "New Bal", 'F2', 7)
    y -= 5
    pdf.add_line(40, y, 392, y, 0.5)
    y -= 13
    for i in range(12):
        pdf.add_line(40, y, 135, y, 0.3, 0.7)
        pdf.add_line(140, y, 190, y, 0.3, 0.7)
        pdf.add_line(195, y, 230, y, 0.3, 0.7)
        pdf.add_line(235, y, 275, y, 0.3, 0.7)
        pdf.add_line(280, y, 337, y, 0.3, 0.7)
        pdf.add_line(342, y, 392, y, 0.3, 0.7)
        y -= 14
    pdf.add_line(40, y, 392, y, 0.5)
    y -= 14
    pdf.add_text(40, y, "Total paid this month: $______", 'F2', 9)
    pdf.add_text(220, y, "Total debt remaining: $________", 'F2', 9)
    y -= 18
    pdf.add_text(40, y, "Debts eliminated this month: ___________________________", 'F1', 8)
    y -= 16
    pdf.add_text(40, y, "Motivation level (1-10): ___", 'F1', 8)
    pdf.add_text(200, y, "Win this month: _________________", 'F1', 8)

# Page 18 - Baby Emergency Fund
pdf.new_page()
pdf.add_centered_text(620, "BABY EMERGENCY FUND TRACKER", 'F2', 13)
pdf.add_centered_text(605, "$1,000 Starter Emergency Fund", 'F4', 10, 0.3)
pdf.add_line(40, 595, 392, 595, 1)
pdf.add_text(40, 578, "Save $1,000 as fast as possible BEFORE attacking debt.", 'F2', 9)
pdf.add_text(40, 560, "This protects you from going deeper into debt.", 'F1', 9)
y = 540
for i in range(20):
    amount = (i + 1) * 50
    pdf.add_rect(45, y-8, 10, 10)
    pdf.add_text(60, y-6, f"${amount}", 'F1', 9)
    pdf.add_text(120, y-6, f"Date saved: ____________  Source: ____________", 'F1', 8)
    y -= 18
pdf.add_text(40, y-10, "DATE COMPLETED: _______________", 'F2', 10)
pdf.add_text(40, y-28, "How I did it: ________________________________________", 'F1', 9)

# Page 19 - Spending Audit
pdf.new_page()
pdf.add_centered_text(620, "SPENDING AUDIT", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 593, "Track EVERYTHING you spend for one month:", 'F1', 9)
categories = ["Housing/Rent", "Utilities", "Groceries", "Eating out",
              "Transportation/Gas", "Insurance", "Phone/Internet",
              "Subscriptions", "Entertainment", "Clothing",
              "Personal care", "Kids expenses", "Pets", "Other"]
y = 575
for c in categories:
    pdf.add_text(40, y, c, 'F1', 8)
    pdf.add_text(160, y, "$_______", 'F1', 8)
    pdf.add_text(230, y, "Need? Y/N", 'F1', 8)
    pdf.add_text(310, y, "Cut to: $_______", 'F1', 8)
    y -= 14
pdf.add_line(40, y, 392, y, 0.5)
y -= 14
pdf.add_text(40, y, "Total monthly spending: $________", 'F2', 9)
pdf.add_text(40, y-16, "Total I can cut: $________", 'F2', 9)
pdf.add_text(40, y-32, "This extra goes to DEBT!", 'F2', 9, 0.3)

# Page 20 - Budget Cuts Brainstorm + Income Boost
pdf.new_page()
pdf.add_centered_text(620, "BUDGET CUTS & INCOME BOOSTS", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 593, "THINGS I CAN CUT (temporarily!):", 'F2', 10)
y = 575
for i in range(8):
    pdf.add_rect(45, y-7, 9, 9)
    pdf.add_line(58, y-4, 250, y-4, 0.5, 0.7)
    pdf.add_text(255, y-4, "Saves: $_____/mo", 'F1', 8)
    y -= 16
pdf.add_text(40, y-10, "WAYS TO EARN MORE:", 'F2', 10)
y -= 28
income_ideas = ["Sell stuff (garage sale, Facebook marketplace)",
                "Side gig (DoorDash, Uber, freelance)",
                "Overtime at work", "Part-time second job",
                "Sell skills (tutoring, lawn care, pet sitting)"]
for idea in income_ideas:
    pdf.add_text(50, y, f"- {idea}", 'F1', 8)
    y -= 14
pdf.add_text(40, y-10, "My income boost plan: ___________________________", 'F1', 9)
pdf.add_text(40, y-26, "Expected extra per month: $_______", 'F1', 9)


# Page 21 - Celebration Milestones
pdf.new_page()
pdf.add_centered_text(620, "CELEBRATION MILESTONES", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Celebrate each win (free or cheap - don't go back into debt!):", 'F1', 9)
milestones = [
    "Emergency fund complete ($1,000)", "First debt PAID OFF!",
    "Second debt paid off", "Third debt paid off",
    "50% of debts eliminated", "All consumer debt gone",
    "All debt gone except mortgage", "COMPLETELY DEBT FREE!"
]
y = 570
for m in milestones:
    pdf.add_rect(45, y-7, 10, 10)
    pdf.add_text(60, y-5, m, 'F1', 9)
    pdf.add_text(60, y-18, "Date: _______ How I celebrated: _________________", 'F1', 8)
    y -= 34

# Pages 22-30 remaining
remaining_titles = ["GAZELLE INTENSITY", "DEBT-FREE DATE CALCULATOR",
                    "MY DEBT-FREE SCREAM", "FINANCIAL PEACE VISION",
                    "MONTHLY BUDGET TEMPLATE", "MONTHLY BUDGET TEMPLATE",
                    "SIDE HUSTLE INCOME LOG", "PROGRESS GRAPH", "NOTES & REFLECTIONS"]
for pg, t in enumerate(remaining_titles):
    pdf.new_page()
    pdf.add_centered_text(620, t, 'F2', 13)
    pdf.add_line(40, 610, 392, 610, 1)
    if pg == 0:  # Gazelle intensity
        pdf.add_text(40, 590, "Live like no one else so later you can LIVE like no one else.", 'F5', 10, 0.3)
        pdf.add_text(40, 565, "GAZELLE INTENSITY COMMITMENTS:", 'F2', 10)
        commitments = ["No restaurants until debt-free", "No new clothes (thrift only)",
                       "Cancel all subscriptions", "Sell the car (buy beater)",
                       "No vacations (staycation only)", "Pack lunch every day",
                       "Say no to every non-essential expense"]
        y = 545
        for c in commitments:
            pdf.add_rect(45, y-7, 9, 9)
            pdf.add_text(58, y-5, c, 'F1', 9)
            y -= 16
        pdf.add_text(40, y-10, "My personal gazelle commitments:", 'F2', 9)
        y -= 28
        for i in range(5):
            pdf.add_line(40, y, 392, y, 0.5, 0.7)
            y -= 14
    elif pg == 2:  # Debt-free scream
        pdf.add_centered_text(450, "I'M DEBT FREE!", 'F2', 24)
        pdf.add_centered_text(410, "Date: _______________", 'F1', 12)
        pdf.add_centered_text(380, "Total debt paid off: $___________", 'F1', 12)
        pdf.add_centered_text(350, "Time it took: ___________", 'F1', 12)
        pdf.add_centered_text(310, "How I feel:", 'F2', 12)
        y = 285
        for i in range(6):
            pdf.add_line(80, y, 352, y, 0.5, 0.7)
            y -= 16
        pdf.add_centered_text(y-10, "I DID IT!", 'F2', 18)
    else:
        y = 585
        for i in range(30):
            pdf.add_line(40, y, 392, y, 0.5, 0.7)
            y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book188_Debt_Free_Workbook.pdf')
print("Book188_Debt_Free_Workbook.pdf created successfully!")
