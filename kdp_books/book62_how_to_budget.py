"""
Book 62: How To Budget Your Money - A Simple Guide to Financial Freedom
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "HOW TO BUDGET YOUR MONEY", font='F2', size=22)
    pdf.add_centered_text(485, "A Simple Guide to Financial Freedom", font='F1', size=14)
    pdf.add_line(80, 460, 352, 460, 2)
    pdf.add_centered_text(420, "Take Control of Your Finances", font='F4', size=13)
    pdf.add_centered_text(398, "and Build the Life You Want", font='F4', size=13)
    pdf.add_centered_text(330, "By", font='F1', size=12)
    pdf.add_centered_text(305, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "How To Budget Your Money", font='F2', size=11)
    pdf.add_centered_text(475, "A Simple Guide to Financial Freedom", font='F1', size=10)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(390, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(365, "Published via Amazon KDP", font='F1', size=10)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: Why Budgeting Matters", [
            "A budget is simply a plan for how you will spend your money each month.",
            "Without a budget, money disappears and you wonder where it all went.",
            "Budgeting is not about restriction. It is about giving yourself permission.",
            "When you budget, you decide in advance what matters most to you.",
            "Studies show that people who budget save three times more than those who do not.",
            "A budget reduces financial stress and arguments about money in relationships.",
            "It helps you avoid debt by ensuring you spend less than you earn.",
            "Budgeting gives you clarity about your true financial situation.",
            "You cannot build wealth without knowing where your money goes.",
            "Even high-income earners go broke without a spending plan.",
            "A budget is your roadmap to financial goals like retirement or a home.",
            "The good news: budgeting is simple once you learn the basic principles.",
        ]),
        ("Chapter 2: The 50/30/20 Rule Explained", [
            "The 50/30/20 rule is the simplest budgeting framework ever created.",
            "Fifty percent of your after-tax income goes to needs like rent and food.",
            "Thirty percent goes to wants like entertainment, dining out, and hobbies.",
            "Twenty percent goes to savings and debt repayment above minimums.",
            "Needs are things you must pay: housing, utilities, insurance, groceries.",
            "Wants are things you enjoy but could live without temporarily.",
            "The savings category includes emergency fund, retirement, and extra debt payments.",
            "If your needs exceed 50 percent, look for ways to reduce housing or car costs.",
            "This rule works as a starting point but adjust percentages to your situation.",
            "Someone with high debt might do 50/20/30 with more going to debt.",
            "The key insight: pay yourself first by automating savings before spending.",
            "Track your spending for one month to see how your current habits compare.",
        ]),
        ("Chapter 3: Tracking Your Income", [
            "Write down every source of income you receive each month.",
            "Include your primary job salary or wages after taxes are taken out.",
            "Add side hustle income, freelance work, or gig economy earnings.",
            "Include investment dividends, rental income, or interest payments.",
            "Count child support, alimony, or government benefits you receive.",
            "For irregular income, calculate your average monthly earnings over six months.",
            "Knowing your exact take-home pay is the foundation of any budget.",
            "Many people overestimate their income by confusing gross and net pay.",
            "Net pay is what actually hits your bank account after deductions.",
            "If paid biweekly, remember you get two extra paychecks per year.",
            "Update your income tracking whenever you get a raise or lose income.",
            "Accurate income tracking prevents you from budgeting money you do not have.",
        ]),
        ("Chapter 4: Listing All Expenses", [
            "Gather your bank statements and credit card bills from the last three months.",
            "Start with fixed expenses that stay the same: rent, car payment, insurance.",
            "Then list variable expenses that change: groceries, gas, utilities, dining out.",
            "Do not forget periodic expenses: annual subscriptions, car registration, gifts.",
            "Divide annual and quarterly expenses by twelve to get the monthly amount.",
            "Check for forgotten subscriptions you signed up for and never cancelled.",
            "The average American has twelve paid subscriptions they may not all need.",
            "Categorize expenses into needs, wants, and savings to see the big picture.",
            "Be completely honest. Include every coffee, snack, and impulse purchase.",
            "Use your bank app to categorize transactions automatically if available.",
            "Most people are surprised to discover they spend more than they thought.",
            "This exercise alone often reveals hundreds in unnecessary spending.",
        ]),
        ("Chapter 5: Creating Your First Budget", [
            "Start by writing your total monthly income at the top of a page.",
            "List all your expense categories below with estimated amounts for each.",
            "Subtract total expenses from total income. The result should be zero or positive.",
            "If negative, you are spending more than you earn and must cut something.",
            "Assign every dollar a job so nothing is left unaccounted for.",
            "This is called zero-based budgeting and it is extremely effective.",
            "Use categories that make sense for your life, not generic templates.",
            "Include a small miscellaneous category for unexpected small expenses.",
            "Build in some buffer for categories that fluctuate like groceries.",
            "Write your budget on paper, a spreadsheet, or a budgeting app.",
            "Review and adjust your budget weekly for the first few months.",
            "A budget is a living document that improves each month as you learn.",
        ]),
        ("Chapter 6: Cutting Unnecessary Spending", [
            "Cancel subscriptions you have not used in the last thirty days.",
            "Negotiate your phone, internet, and insurance bills. Call and ask for discounts.",
            "Cook at home more often. Restaurant meals cost five times more than homemade.",
            "Use the 24-hour rule: wait a day before any purchase over fifty dollars.",
            "Unsubscribe from marketing emails that tempt you to buy things you do not need.",
            "Switch to generic brands for groceries, medicine, and cleaning products.",
            "Use the library instead of buying books, magazines, and movies.",
            "Carpool, bike, or use public transit to reduce transportation costs.",
            "Make coffee at home instead of buying five-dollar drinks daily.",
            "Shop with a list and stick to it to avoid impulse purchases.",
            "Find free entertainment: parks, hiking, community events, and free museums.",
            "Small daily savings of five dollars add up to over eighteen hundred per year.",
        ]),
        ("Chapter 7: Building an Emergency Fund", [
            "An emergency fund is money set aside for unexpected expenses only.",
            "Start with a goal of one thousand dollars as your starter emergency fund.",
            "Then build toward three to six months of essential living expenses.",
            "Keep emergency money in a high-yield savings account separate from checking.",
            "This prevents you from accidentally spending your safety net.",
            "Emergencies include job loss, medical bills, car repairs, and home fixes.",
            "Sales, vacations, and new gadgets are not emergencies.",
            "Automate weekly or biweekly transfers to your emergency savings account.",
            "Even twenty-five dollars per week builds to thirteen hundred in a year.",
            "Having an emergency fund prevents you from going into debt when life happens.",
            "Sixty percent of Americans cannot cover a four hundred dollar emergency.",
            "Your emergency fund is your financial foundation. Build it before investing.",
        ]),
        ("Chapter 8: Paying Off Debt (Snowball Method)", [
            "The debt snowball method pays off debts from smallest to largest balance.",
            "List all debts with their balances, minimum payments, and interest rates.",
            "Make minimum payments on all debts except the smallest one.",
            "Throw every extra dollar at the smallest debt until it is completely gone.",
            "Once the smallest debt is paid off, add its payment to the next smallest.",
            "This creates a snowball effect as your payment amount grows with each debt.",
            "The psychological wins of paying off small debts keep you motivated.",
            "Some people prefer the avalanche method which targets highest interest first.",
            "The avalanche saves more money mathematically but the snowball keeps you going.",
            "Stop using credit cards while paying off debt to avoid digging deeper.",
            "Celebrate each paid-off debt to maintain momentum and motivation.",
            "Most people can become debt-free in two to five years with focused effort.",
        ]),
        ("Chapter 9: Saving for Retirement", [
            "Start saving for retirement as early as possible due to compound interest.",
            "If your employer offers a 401k match, contribute at least enough to get it.",
            "A company match is free money. Not taking it is leaving your pay on the table.",
            "After the match, consider a Roth IRA for tax-free growth on your money.",
            "Aim to save fifteen percent of your gross income for retirement.",
            "If you cannot do fifteen percent now, start with what you can and increase yearly.",
            "Compound interest means your money earns money on top of money it already earned.",
            "Starting at 25 with two hundred monthly can yield over half a million by 65.",
            "Starting at 35 requires nearly double the monthly amount for the same result.",
            "Choose low-cost index funds that track the entire market for simplicity.",
            "Do not try to time the market. Consistent investing over time always wins.",
            "Retirement savings should be automated so you never have to think about it.",
        ]),
        ("Chapter 10: Budgeting for Irregular Income", [
            "Irregular income includes freelance, commission, seasonal, and gig work.",
            "Calculate your average monthly income from the past six to twelve months.",
            "Build a larger emergency fund of six months since income is unpredictable.",
            "Budget based on your lowest earning month to ensure you can always cover bills.",
            "In high-earning months, save the surplus in a buffer account.",
            "Draw from the buffer during low-income months to smooth out fluctuations.",
            "Prioritize needs first: pay essential bills before anything else.",
            "Create a priority list of expenses ranked from most to least important.",
            "When income is low, work down the list until the money runs out.",
            "Avoid lifestyle inflation during good months. Save the excess instead.",
            "Consider diversifying income streams to reduce reliance on one source.",
            "Irregular income makes budgeting harder but even more essential.",
        ]),
        ("Chapter 11: Budgeting as a Couple", [
            "Money is the number one cause of conflict in relationships.",
            "Schedule regular money dates to discuss finances together without judgment.",
            "Decide whether to combine all money, keep separate, or use a hybrid system.",
            "A hybrid approach works well: shared account for bills, personal accounts for fun.",
            "Set a spending threshold where either partner must consult the other first.",
            "Be transparent about debts, income, and financial goals with each other.",
            "Assign money roles based on strengths: who pays bills, who tracks spending.",
            "Create shared financial goals like a vacation, home, or debt payoff.",
            "Respect different money personalities. One may be a saver and one a spender.",
            "Compromise is key. Both partners should have some guilt-free spending money.",
            "Review your budget together monthly and adjust as life changes.",
            "Working as a team on money builds trust and strengthens your relationship.",
        ]),
        ("Chapter 12: Teaching Kids About Money", [
            "Start teaching money basics as early as age three or four.",
            "Use three jars labeled Save, Spend, and Give for young children.",
            "Give age-appropriate allowance tied to completing household chores.",
            "Let children make spending mistakes with small amounts to learn consequences.",
            "Take kids grocery shopping and show them how to compare prices.",
            "Open a savings account for children and show them interest growing.",
            "Teach teens about compound interest using simple examples and charts.",
            "Involve teenagers in family budget discussions appropriate for their age.",
            "Help teens earn their own money through babysitting, lawn care, or tutoring.",
            "Discuss wants versus needs regularly in everyday situations.",
            "Model good financial behavior because children learn from what they see.",
            "Teaching kids about money is one of the greatest gifts you can give them.",
        ]),
        ("Chapter 13: Apps and Tools That Help", [
            "Mint is a free app that connects to your accounts and categorizes spending.",
            "YNAB (You Need A Budget) teaches zero-based budgeting with excellent support.",
            "EveryDollar is a simple drag-and-drop budgeting app by Dave Ramsey.",
            "Personal Capital is best for tracking investments and net worth.",
            "Goodbudget uses the digital envelope system for couples budgeting together.",
            "A simple spreadsheet in Google Sheets or Excel works perfectly fine too.",
            "The best tool is the one you will actually use consistently.",
            "Set up automatic bill payments to avoid late fees and missed payments.",
            "Use your bank app to set up alerts for low balances and large purchases.",
            "Cash envelope system works for people who overspend with cards.",
            "Try a few different apps to find what matches your style.",
            "Technology makes budgeting faster but the principles remain the same.",
        ]),
        ("Chapter 14: Common Budgeting Mistakes", [
            "Mistake one: making your budget too restrictive with zero fun money.",
            "Mistake two: not tracking small purchases that add up significantly.",
            "Mistake three: forgetting irregular expenses like car maintenance and gifts.",
            "Mistake four: giving up after one bad month instead of adjusting.",
            "Mistake five: not involving your partner in the budgeting process.",
            "Mistake six: budgeting based on gross income instead of take-home pay.",
            "Mistake seven: not having a miscellaneous category for unexpected costs.",
            "Mistake eight: comparing your budget to others instead of your own goals.",
            "Mistake nine: treating the budget as a set-it-and-forget-it document.",
            "Mistake ten: not celebrating small wins and progress along the way.",
            "Every budgeter makes mistakes. The key is to learn and adjust each month.",
            "Progress over perfection. A imperfect budget beats no budget every time.",
        ]),
        ("Chapter 15: Your 30-Day Action Plan", [
            "Day 1: Calculate your exact monthly take-home income from all sources.",
            "Days 2-3: Review three months of bank and credit card statements.",
            "Days 4-5: List and categorize every recurring expense you have.",
            "Day 6: Cancel at least two subscriptions or services you do not use.",
            "Day 7: Create your first monthly budget using the 50/30/20 framework.",
            "Days 8-14: Track every single purchase you make, no matter how small.",
            "Day 15: Review your tracking and adjust budget categories as needed.",
            "Days 16-18: Set up automatic transfers to savings, even if just 25 dollars.",
            "Days 19-21: Call one bill provider and negotiate a lower rate.",
            "Days 22-25: Open a separate high-yield savings account for emergencies.",
            "Days 26-28: Research and choose a budgeting app or system that fits you.",
            "Days 29-30: Review your progress, celebrate wins, and plan next month.",
        ]),
    ]

    page_num = 1
    for title, lines in chapters:
        pdf.new_page()
        pdf.add_centered_text(600, title, font='F2', size=16)
        pdf.add_line(60, 585, 372, 585, 1)
        y = 560
        for line in lines:
            pdf.add_text(50, y, line, font='F4', size=11)
            y -= 22
        pdf.add_centered_text(30, str(page_num), font='F1', size=10)
        page_num += 1

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book62_How_To_Budget.pdf')
    print("Book 62 created: Book62_How_To_Budget.pdf")

if __name__ == '__main__':
    create_book()
