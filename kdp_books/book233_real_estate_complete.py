"""Book 233: The Real Estate Investor's Workbook"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.15)
    doc.add_centered_text(755, "THE REAL ESTATE INVESTOR'S", 'F2', 20, 1)
    doc.add_centered_text(725, "WORKBOOK", 'F2', 24, 1)
    doc.add_centered_text(665, "Analyze, Acquire & Manage Rental Properties", 'F4', 13, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    doc.new_page()
    doc.add_centered_text(700, "THE REAL ESTATE INVESTOR'S WORKBOOK", 'F2', 13)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # Investment Strategy
    doc.new_page()
    doc.add_centered_text(750, "INVESTMENT STRATEGY DEFINITION", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = ["Strategy: [ ] Buy & Hold [ ] BRRRR [ ] Fix & Flip [ ] Wholesale [ ] STR",
        "Property type: [ ] SFH [ ] Multi-family [ ] Commercial [ ] Mixed",
        "Target market(s): ________________________________",
        "Investment criteria:", "  Min cash flow: $___/door/month",
        "  Min cash-on-cash return: ___%", "  Max purchase price: $___",
        "  Max rehab budget: $___", "",
        "5-year goal: ___ properties, $___ monthly cash flow",
        "Financing strategy: [ ] Conventional [ ] FHA [ ] DSCR [ ] Private [ ] Seller",
        "Available capital: $___", "Pre-approval amount: $___",
        "Team members:", "  Realtor: ________________________________",
        "  Lender: ________________________________",
        "  Contractor: ________________________________",
        "  Property manager: ________________________________"]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Market Analysis (3 areas)
    doc.new_page()
    doc.add_centered_text(750, "MARKET ANALYSIS - COMPARISON", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 715
    for area in range(1, 4):
        doc.add_text(72, y, f"MARKET {area}: ________________________________", 'F2', 10)
        y -= 16
        metrics = ["Population growth: ___%", "Job growth: ___%",
            "Median home price: $___", "Median rent: $___",
            "Price-to-rent ratio: ___", "Vacancy rate: ___%",
            "Crime trend: [ ] Improving [ ] Stable [ ] Declining",
            "School rating: ___/10"]
        for m in metrics:
            doc.add_text(90, y, m, 'F1', 8)
            y -= 12
        y -= 15


    # Property Analysis Worksheets (10 pages)
    for prop in range(1, 11):
        doc.new_page()
        doc.add_centered_text(760, f"PROPERTY ANALYSIS #{prop}", 'F2', 12)
        doc.add_line(72, 748, 540, 748, 0.5, 0.3)
        y = 730
        doc.add_text(72, y, "Address: ________________________________", 'F1', 9)
        y -= 14
        doc.add_text(72, y, "Asking price: $______  Beds: ___  Baths: ___  Sq ft: ____  Year: ____", 'F1', 9)
        y -= 16
        doc.add_text(72, y, "NUMBERS:", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Estimated repairs: $______", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "After Repair Value (ARV): $______", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Monthly rent estimate: $______", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Vacancy rate: ___%  ($______/mo)", 'F1', 8)
        y -= 14
        doc.add_text(72, y, "MONTHLY EXPENSES:", 'F2', 9)
        y -= 14
        expenses = ["Mortgage (P&I): $______", "Taxes: $______", "Insurance: $______",
                   "Maintenance (5%): $______", "CapEx reserve (5%): $______",
                   "Property mgmt (10%): $______", "Vacancy (8%): $______",
                   "TOTAL EXPENSES: $______"]
        for exp in expenses:
            doc.add_text(90, y, exp, 'F1', 8)
            y -= 11
        y -= 10
        doc.add_filled_rect(72, y-15, 468, 20, 0.92)
        doc.add_text(80, y, "CASH FLOW: $______/mo  ROI: ____%  Cap Rate: ____%", 'F2', 9)
        y -= 22
        doc.add_text(72, y, "Decision: [ ] BUY [ ] PASS  Reason: ________________________________", 'F1', 9)

    # Offer Calculation + Due Diligence + Rehab Budget
    doc.new_page()
    doc.add_centered_text(750, "OFFER CALCULATION & DUE DILIGENCE", 'F2', 13)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "OFFER CALCULATION:", 'F2', 10)
    y -= 16
    calc = ["ARV: $______  x 70% = $______",
        "Minus repairs: - $______", "Maximum Offer: $______",
        "My offer: $______  Contingencies: ________________________________"]
    for c in calc:
        doc.add_text(90, y, c, 'F1', 9)
        y -= 16
    y -= 15
    doc.add_text(72, y, "DUE DILIGENCE CHECKLIST:", 'F2', 10)
    y -= 16
    dd = ["[ ] Home inspection", "[ ] Roof inspection", "[ ] Sewer scope",
        "[ ] Termite inspection", "[ ] Title search", "[ ] Survey",
        "[ ] HOA docs reviewed", "[ ] Rent comps verified",
        "[ ] Property tax history", "[ ] Insurance quote obtained"]
    for item in dd:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 14

    doc.new_page()
    doc.add_centered_text(750, "REHAB BUDGET TEMPLATE", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "Property: ________________________________", 'F1', 10)
    y -= 20
    categories = ["Kitchen", "Bathrooms", "Flooring", "Paint (int/ext)",
                  "Roof", "HVAC", "Plumbing", "Electrical", "Windows/Doors",
                  "Landscaping", "Driveway/Exterior", "Permits", "Contingency (15%)"]
    doc.add_text(72, y, "Category", 'F2', 8)
    doc.add_text(220, y, "Estimated", 'F2', 8)
    doc.add_text(310, y, "Actual", 'F2', 8)
    doc.add_text(395, y, "Notes", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for cat in categories:
        y -= 20
        doc.add_text(72, y, cat, 'F1', 9)
        doc.add_text(220, y, "$_______", 'F1', 9)
        doc.add_text(310, y, "$_______", 'F1', 9)
        doc.add_line(395, y-2, 540, y-2, 0.5, 0.5)
    y -= 25
    doc.add_text(72, y, "TOTAL REHAB: Estimated $______  Actual $______", 'F2', 10)

    # Tenant Screening + Lease + Property Mgmt (6 pages)
    doc.new_page()
    doc.add_centered_text(750, "TENANT SCREENING CHECKLIST", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Applicant: ________________________________", 'F1', 10)
    y -= 18
    screening = ["[ ] Application received  Date: ___/___",
        "[ ] Income verification (3x rent = $___/mo needed)",
        "  Verified income: $___/mo  Ratio: ___x", "[ ] Credit check  Score: ___",
        "[ ] Background check  Clear? [ ] Yes [ ] No",
        "[ ] Eviction history  Clear? [ ] Yes [ ] No",
        "[ ] Landlord references (2):",
        "  Ref 1: _____________ Rating: ___/5",
        "  Ref 2: _____________ Rating: ___/5",
        "[ ] Employment verification", "",
        "DECISION: [ ] APPROVED [ ] DENIED  Reason: ________________",
        "Lease start: ___/___  Rent: $___  Deposit: $___"]
    for item in screening:
        doc.add_text(72, y, item, 'F1', 9)
        y -= 16

    doc.new_page()
    doc.add_centered_text(750, "LEASE AGREEMENT TRACKING", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 720
    for t in range(1, 9):
        doc.add_text(72, y, f"Tenant {t}: _____________ Unit: ___ Rent: $___", 'F2', 8)
        y -= 12
        doc.add_text(90, y, "Lease: ___/___ to ___/___  Deposit: $___  Pet dep: $___", 'F1', 7)
        y -= 12
        doc.add_text(90, y, "Renewal date: ___/___  Increase to: $___", 'F1', 7)
        y -= 18

    # Property Management Monthly Reports (6 pages)
    for pg in range(1, 7):
        doc.new_page()
        doc.add_centered_text(755, f"PROPERTY MANAGEMENT REPORT - PROPERTY {pg}", 'F2', 11)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        doc.add_text(72, y, "Address: ________________________________", 'F1', 9)
        y -= 16
        doc.add_text(72, y, "Month: ________  Year: ________", 'F1', 9)
        y -= 20
        doc.add_text(72, y, "INCOME:", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Rent collected: $___  Late fees: $___  Other: $___  TOTAL: $___", 'F1', 8)
        y -= 18
        doc.add_text(72, y, "EXPENSES:", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Mortgage: $___  Tax: $___  Insurance: $___  Mgmt: $___", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Maintenance: $___  Utilities: $___  Other: $___  TOTAL: $___", 'F1', 8)
        y -= 18
        doc.add_text(72, y, "NET CASH FLOW: $___", 'F2', 9)
        y -= 20
        doc.add_text(72, y, "MAINTENANCE:", 'F1', 9)
        y -= 12
        doc.add_text(90, y, "Work orders: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "________________________________", 'F1', 8)
        y -= 18
        doc.add_text(72, y, "VACANCY: Days vacant ___ Showing scheduled? [ ]", 'F1', 9)
        y -= 18
        doc.add_text(72, y, "Notes: ________________________________", 'F1', 9)


    # Portfolio Dashboard + Tax + 1031 + Exit
    doc.new_page()
    doc.add_centered_text(750, "PORTFOLIO PERFORMANCE & TAX", 'F2', 13)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "QUARTERLY PORTFOLIO DASHBOARD:", 'F2', 10)
    y -= 18
    doc.add_text(72, y, "Property", 'F2', 8)
    doc.add_text(200, y, "Value", 'F2', 8)
    doc.add_text(265, y, "Equity", 'F2', 8)
    doc.add_text(330, y, "Cash Flow", 'F2', 8)
    doc.add_text(410, y, "ROI", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for _ in range(6):
        y -= 18
        doc.add_line(72, y, 540, y, 0.5, 0.5)
    y -= 20
    doc.add_text(72, y, "Total portfolio value: $___  Total equity: $___", 'F2', 9)
    y -= 14
    doc.add_text(72, y, "Total monthly cash flow: $___  Total annual ROI: ___%", 'F2', 9)
    y -= 25
    doc.add_text(72, y, "TAX DEDUCTION LOG:", 'F2', 10)
    y -= 16
    deductions = ["Mortgage interest", "Property taxes", "Insurance",
        "Repairs & maintenance", "Depreciation", "Travel (property visits)",
        "Home office", "Professional services"]
    for d in deductions:
        doc.add_text(90, y, f"{d}: $______", 'F1', 8)
        y -= 12
    y -= 15
    doc.add_text(72, y, "1031 EXCHANGE PLANNER:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "Property to sell: _______________ Value: $___", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "45-day ID deadline: ___/___  180-day close deadline: ___/___", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Replacement properties identified: ________________________________", 'F1', 9)
    y -= 20
    doc.add_text(72, y, "EXIT STRATEGY:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "[ ] Hold forever [ ] Sell at $___  [ ] 1031 into larger [ ] Owner finance", 'F1', 9)

    doc.save("Book233_Real_Estate_Investor_Workbook.pdf")
    print("Created: Book233_Real_Estate_Investor_Workbook.pdf")

if __name__ == "__main__":
    create_book()
