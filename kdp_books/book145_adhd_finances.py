"""Book 145: ADHD Budget Planner - Finally Master Your Money"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "ADHD BUDGET PLANNER", 'F2', 22, 0)
    doc.add_centered_text(395, "Finally Master Your Money", 'F4', 16, 0.2)
    doc.add_centered_text(365, "(Neurodivergent-Friendly)", 'F1', 13, 0.3)
    doc.add_centered_text(300, "Simple Systems That Work With Your Brain", 'F1', 12, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(500, "ADHD BUDGET PLANNER", 'F2', 14, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)

    # Page 3: Why Money is Hard with ADHD
    doc.new_page()
    doc.add_centered_text(590, "WHY MONEY IS HARD WITH ADHD", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "You're not bad with money. Your brain works differently:", 'F2', 10, 0)
    y = 530
    reasons = [
        ("TIME BLINDNESS:", "Future feels abstract. 'Future me' isn't real."),
        ("IMPULSIVITY:", "See it, want it, buy it. Dopamine seeking."),
        ("OUT OF SIGHT:", "If you can't SEE the money, it doesn't exist."),
        ("OVERWHELM:", "Too many accounts/bills = shut down completely."),
        ("SHAME SPIRAL:", "Avoiding looking at the damage makes it worse."),
        ("HYPERFOCUS:", "Can spend hours researching a $20 purchase, forget rent.")
    ]
    for title, desc in reasons:
        doc.add_text(50, y, title, 'F2', 9, 0)
        doc.add_text(50, y-14, desc, 'F1', 9, 0.3)
        y -= 35
    y -= 10
    doc.add_filled_rect(50, y-5, 332, 30, 0.88)
    doc.add_text(55, y+8, "This planner uses: VISUAL + SIMPLE + AUTOMATED", 'F2', 10, 0)

    # Page 4: The ADHD Money System
    doc.new_page()
    doc.add_centered_text(590, "THE ADHD MONEY SYSTEM", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "The 3 Principles:", 'F2', 11, 0)
    y -= 22
    principles = [
        ("1. AUTOMATE:", "Set up auto-pay for everything possible. No willpower needed."),
        ("2. VISUALIZE:", "Use cash envelopes or visual trackers. Make money VISIBLE."),
        ("3. SIMPLIFY:", "5 categories max. Fewer decisions = less overwhelm.")
    ]
    for title, desc in principles:
        doc.add_text(50, y, title, 'F2', 10, 0)
        y -= 16
        doc.add_text(65, y, desc, 'F1', 9, 0.3)
        y -= 22
    y -= 15
    doc.add_text(50, y, "The 3-Account System:", 'F2', 11, 0)
    y -= 20
    accounts = [
        ("Account 1 - BILLS:", "All fixed expenses auto-pay from here. Don't touch it."),
        ("Account 2 - SPENDING:", "Your weekly 'allowance.' When it's gone, it's gone."),
        ("Account 3 - SAVINGS:", "Auto-transfer on payday. Out of sight = safe.")
    ]
    for title, desc in accounts:
        doc.add_text(50, y, title, 'F2', 9, 0)
        y -= 14
        doc.add_text(65, y, desc, 'F1', 9, 0.3)
        y -= 22

    # Page 5: Income Tracker
    doc.new_page()
    doc.add_centered_text(590, "INCOME TRACKER (SIMPLIFIED)", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Monthly take-home pay: $__________", 'F2', 10, 0)
    y -= 22
    doc.add_text(50, y, "Pay frequency: [ ] Weekly  [ ] Bi-weekly  [ ] Monthly", 'F1', 10, 0.2)
    y -= 22
    doc.add_text(50, y, "Other income: $__________  Source: __________________", 'F1', 10, 0.2)
    y -= 30
    doc.add_text(50, y, "TOTAL MONTHLY INCOME: $__________", 'F2', 12, 0)
    y -= 30
    doc.add_text(50, y, "Split it up:", 'F2', 10, 0)
    y -= 20
    doc.add_text(50, y, "Bills account (50-60%): $__________", 'F1', 10, 0.2)
    y -= 20
    doc.add_text(50, y, "Spending account (30-40%): $__________", 'F1', 10, 0.2)
    y -= 20
    doc.add_text(50, y, "Savings account (10-20%): $__________", 'F1', 10, 0.2)
    y -= 30
    doc.add_text(50, y, "Auto-transfer date (payday): ___________", 'F1', 10, 0.2)

    # Page 6: Bill Calendar
    doc.new_page()
    doc.add_centered_text(590, "BILL CALENDAR (VISUAL DUE DATES)", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_filled_rect(50, y-2, 332, 16, 0.85)
    doc.add_text(52, y, "Day", 'F2', 8, 0)
    doc.add_text(80, y, "Bill Name", 'F2', 8, 0)
    doc.add_text(200, y, "Amount", 'F2', 8, 0)
    doc.add_text(260, y, "Auto-pay?", 'F2', 8, 0)
    doc.add_text(325, y, "Paid?", 'F2', 8, 0)
    y -= 20
    for i in range(20):
        doc.add_rect(50, y-2, 332, 18)
        y -= 20
    y -= 10
    doc.add_text(50, y, "TOTAL monthly bills: $__________", 'F2', 10, 0)
    y -= 18
    doc.add_text(50, y, "TIP: Set ALL bills to auto-pay. Then forget about them!", 'F1', 9, 0.3)

    # Pages 7-18: Weekly Spending Check-In (12 pages)
    for week in range(12):
        doc.new_page()
        doc.add_centered_text(590, f"WEEKLY SPENDING CHECK-IN - Week {week+1}", 'F2', 11, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 558
        doc.add_text(50, y, f"Week of: ____________  Spending budget this week: $__________", 'F1', 9, 0.2)
        y -= 22
        doc.add_text(50, y, "ONLY 5 CATEGORIES (keep it simple!):", 'F2', 9, 0)
        y -= 18
        categories = ["Food/Groceries", "Transport/Gas", "Fun/Entertainment", "Personal/Self-care", "Other"]
        doc.add_filled_rect(50, y-2, 332, 14, 0.85)
        doc.add_text(52, y, "Category", 'F2', 7, 0)
        doc.add_text(150, y, "Budget", 'F2', 7, 0)
        doc.add_text(210, y, "Spent", 'F2', 7, 0)
        doc.add_text(265, y, "Left", 'F2', 7, 0)
        doc.add_text(315, y, "Over?", 'F2', 7, 0)
        y -= 16
        for cat in categories:
            doc.add_text(52, y, cat, 'F1', 8, 0.2)
            doc.add_text(150, y, "$_____", 'F1', 8, 0.3)
            doc.add_text(210, y, "$_____", 'F1', 8, 0.3)
            doc.add_text(265, y, "$_____", 'F1', 8, 0.3)
            doc.add_rect(320, y-2, 10, 10)
            y -= 16
        y -= 10
        doc.add_text(50, y, "Total spent: $________  Left in spending account: $________", 'F1', 9, 0.2)
        y -= 20
        doc.add_text(50, y, "Impulse purchases this week: ______________________________________", 'F1', 9, 0.2)
        y -= 18
        doc.add_text(50, y, "Do I need to adjust anything next week? ___________________________", 'F1', 9, 0.2)
        y -= 18
        doc.add_text(50, y, "Win: _____________________________________________________________", 'F1', 9, 0.2)

    # Pages 19-23: Impulse Purchase Pause (5 pages)
    for page_num in range(5):
        doc.new_page()
        doc.add_centered_text(590, f"IMPULSE PURCHASE PAUSE ({page_num+1}/5)", 'F2', 12, 0)
        doc.add_line(50, 580, 382, 580, 1, 0.5)
        y = 555
        for entry in range(2):
            doc.add_text(50, y, f"Item #{page_num*2+entry+1}:", 'F2', 10, 0.1)
            y -= 18
            doc.add_text(50, y, "What I want: _________________________________  Cost: $______", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Date I first wanted it: __________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "WAIT 48 HOURS. Then answer:", 'F2', 9, 0)
            y -= 16
            doc.add_text(50, y, "Do I still want it? [ ] Yes [ ] No [ ] Meh", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Can I actually afford it (not just 'have the money')? [ ] Yes [ ] No", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Will I still care about this in 30 days? [ ] Yes [ ] No", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Is there something I need MORE? ________________________________", 'F1', 9, 0.3)
            y -= 16
            doc.add_text(50, y, "Decision: [ ] Buy it [ ] Skip it [ ] Save for it", 'F1', 9, 0.3)
            y -= 30

    # Page 24: Subscription Audit
    doc.new_page()
    doc.add_centered_text(590, "SUBSCRIPTION AUDIT", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "List EVERY recurring charge. Be honest. Check bank statement.", 'F1', 10, 0.2)
    y = 530
    doc.add_filled_rect(50, y-2, 332, 16, 0.85)
    doc.add_text(52, y, "Subscription", 'F2', 8, 0)
    doc.add_text(170, y, "$/month", 'F2', 8, 0)
    doc.add_text(230, y, "Use it?", 'F2', 8, 0)
    doc.add_text(290, y, "Keep/Cancel", 'F2', 8, 0)
    y -= 18
    for i in range(15):
        doc.add_rect(50, y-2, 332, 16)
        y -= 18
    y -= 10
    doc.add_text(50, y, "Total subscriptions: $______/month = $______/year (!)", 'F2', 10, 0)
    y -= 18
    doc.add_text(50, y, "Savings from canceling: $______/month", 'F1', 10, 0.2)

    # Page 25: Sinking Funds Tracker
    doc.new_page()
    doc.add_centered_text(590, "SINKING FUNDS VISUAL TRACKER", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Save small amounts over time for big expenses:", 'F1', 10, 0.2)
    y = 530
    funds = ["Holiday gifts", "Car maintenance", "Medical/dental", "Vacation", "Emergency"]
    for fund in funds:
        doc.add_text(50, y, f"{fund}: Goal $______  Have $______", 'F2', 9, 0.1)
        y -= 16
        # Progress bar
        doc.add_rect(50, y-2, 250, 12)
        y -= 22

    # Page 26: Debt Snowball
    doc.new_page()
    doc.add_centered_text(590, "DEBT SNOWBALL (SIMPLIFIED)", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "List debts from SMALLEST to LARGEST. Pay minimum on all.", 'F1', 10, 0.2)
    doc.add_text(50, 537, "Throw extra at the smallest. When it's paid, roll that payment to next.", 'F1', 10, 0.2)
    y = 510
    doc.add_filled_rect(50, y-2, 332, 16, 0.85)
    doc.add_text(52, y, "Debt", 'F2', 8, 0)
    doc.add_text(150, y, "Total Owed", 'F2', 8, 0)
    doc.add_text(230, y, "Min Payment", 'F2', 8, 0)
    doc.add_text(310, y, "Paid Off!", 'F2', 8, 0)
    y -= 18
    for i in range(8):
        doc.add_rect(50, y-2, 332, 18)
        y -= 20
    y -= 10
    doc.add_text(50, y, "Total debt: $__________  Extra I can throw at smallest: $______/month", 'F1', 9, 0.2)

    # Page 27: Emergency Fund Progress
    doc.new_page()
    doc.add_centered_text(590, "EMERGENCY FUND PROGRESS BAR", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Goal: $1,000 starter emergency fund", 'F2', 10, 0)
    doc.add_text(50, 535, "Save $_____ per week/month", 'F1', 10, 0.2)
    y = 505
    doc.add_text(50, y, "Color in each $50 saved:", 'F1', 10, 0.2)
    y -= 20
    for row in range(4):
        x = 50
        for col in range(5):
            amount = row * 250 + col * 50 + 50
            doc.add_rect(x, y, 60, 25)
            doc.add_text(x+5, y+8, f"${amount}", 'F1', 8, 0.3)
            x += 65
        y -= 30
    y -= 15
    doc.add_text(50, y, "Start date: __________  Goal date: __________", 'F1', 10, 0.2)
    y -= 20
    doc.add_text(50, y, "Actual completion date: __________  CELEBRATE!", 'F2', 10, 0)

    # Page 28: Reward System
    doc.new_page()
    doc.add_centered_text(590, "REWARD SYSTEM FOR FINANCIAL WINS", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "ADHD brains need rewards! Set up treats for hitting money goals:", 'F1', 10, 0.2)
    y = 530
    rewards = [
        ("Stuck to budget for 1 week:", "______________________________"),
        ("Paid a bill on time:", "______________________________"),
        ("Resisted impulse purchase:", "______________________________"),
        ("Saved $100:", "______________________________"),
        ("Paid off a debt:", "______________________________"),
        ("Built $500 emergency fund:", "______________________________"),
        ("3 months of consistent budgeting:", "______________________________")
    ]
    for achievement, reward in rewards:
        doc.add_text(50, y, achievement, 'F2', 9, 0.1)
        y -= 16
        doc.add_text(50, y, f"  My reward: {reward}", 'F1', 9, 0.3)
        y -= 22
    y -= 10
    doc.add_text(50, y, "RULE: Rewards should NOT sabotage your financial goals!", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "Free/cheap reward ideas: picnic, movie night, sleep in, long bath", 'F1', 9, 0.3)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book145_ADHD_Budget_Planner.pdf')
    print("Book145_ADHD_Budget_Planner.pdf created successfully!")

if __name__ == "__main__":
    create_book()
