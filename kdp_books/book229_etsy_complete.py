"""Book 229: The Etsy Seller's Complete Business Planner"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.15)
    doc.add_centered_text(755, "THE ETSY SELLER'S COMPLETE", 'F2', 20, 1)
    doc.add_centered_text(725, "BUSINESS PLANNER", 'F2', 22, 1)
    doc.add_centered_text(665, "Launch, Grow & Scale Your Shop", 'F4', 14, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    doc.new_page()
    doc.add_centered_text(700, "THE ETSY SELLER'S COMPLETE BUSINESS PLANNER", 'F2', 12)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # Niche Selection
    doc.new_page()
    doc.add_centered_text(750, "NICHE SELECTION WORKSHEET", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = ["My skills/interests: ________________________________",
        "Market demand (search volume): ________________________________",
        "Competition level: [ ] Low [ ] Medium [ ] High",
        "Average price point in niche: $______",
        "Profit margin potential: ____%", "",
        "Niche ideas:", "1. _________________ Demand: ___ Competition: ___",
        "2. _________________ Demand: ___ Competition: ___",
        "3. _________________ Demand: ___ Competition: ___", "",
        "CHOSEN NICHE: ________________________________",
        "Why: ________________________________",
        "Target customer: ________________________________",
        "Their problem I solve: ________________________________"]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 18

    # Competitor Research
    doc.new_page()
    doc.add_centered_text(750, "COMPETITOR RESEARCH", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 715
    for s in range(1, 6):
        doc.add_text(72, y, f"SHOP {s}: ________________________________", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Sales: _____  Reviews: _____  Price range: $___-$___", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Best seller: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "What they do well: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Gap I can fill: ________________________________", 'F1', 8)
        y -= 22

    # Product Line Planning
    doc.new_page()
    doc.add_centered_text(750, "PRODUCT LINE PLANNING", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 720
    doc.add_text(72, y, "Product", 'F2', 7)
    doc.add_text(200, y, "Cost", 'F2', 7)
    doc.add_text(245, y, "Price", 'F2', 7)
    doc.add_text(295, y, "Margin", 'F2', 7)
    doc.add_text(345, y, "Time", 'F2', 7)
    doc.add_text(395, y, "Priority", 'F2', 7)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for _ in range(20):
        y -= 18
        doc.add_line(72, y, 540, y, 0.5, 0.5)


    # Listing Optimization (10 listings)
    doc.new_page()
    doc.add_centered_text(755, "LISTING OPTIMIZATION CHECKLIST", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    for i in range(1, 6):
        doc.add_text(72, y, f"Listing {i}: ________________________________", 'F2', 9)
        y -= 13
        doc.add_text(90, y, "[ ] Title (140 chars, keywords first) [ ] 13 tags used", 'F1', 8)
        y -= 11
        doc.add_text(90, y, "[ ] 10 photos [ ] Video [ ] Description optimized [ ] Attributes", 'F1', 8)
        y -= 18
    doc.new_page()
    doc.add_centered_text(755, "LISTING OPTIMIZATION - CONTINUED", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    for i in range(6, 11):
        doc.add_text(72, y, f"Listing {i}: ________________________________", 'F2', 9)
        y -= 13
        doc.add_text(90, y, "[ ] Title (140 chars, keywords first) [ ] 13 tags used", 'F1', 8)
        y -= 11
        doc.add_text(90, y, "[ ] 10 photos [ ] Video [ ] Description optimized [ ] Attributes", 'F1', 8)
        y -= 18

    # SEO Keyword Research (5 pages)
    for pg in range(1, 6):
        doc.new_page()
        doc.add_centered_text(755, f"SEO KEYWORD RESEARCH - PRODUCT {pg}", 'F2', 12)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        doc.add_text(72, y, f"Product: ________________________________", 'F1', 10)
        y -= 22
        doc.add_text(72, y, "PRIMARY KEYWORDS (high search, high competition):", 'F2', 9)
        y -= 14
        for _ in range(5):
            doc.add_text(90, y, "________________________________  Search vol: ___  Comp: ___", 'F1', 8)
            y -= 14
        y -= 8
        doc.add_text(72, y, "LONG-TAIL KEYWORDS (specific, lower competition):", 'F2', 9)
        y -= 14
        for _ in range(5):
            doc.add_text(90, y, "________________________________  Search vol: ___  Comp: ___", 'F1', 8)
            y -= 14
        y -= 8
        doc.add_text(72, y, "SEASONAL KEYWORDS:", 'F2', 9)
        y -= 14
        for _ in range(3):
            doc.add_text(90, y, "________________________________  Best months: ___________", 'F1', 8)
            y -= 14

    # Photography + Branding
    doc.new_page()
    doc.add_centered_text(750, "PHOTOGRAPHY & SHOP BRANDING", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "PHOTOGRAPHY CHECKLIST:", 'F2', 10)
    y -= 16
    photo_items = ["[ ] Natural lighting setup", "[ ] Clean background",
        "[ ] Multiple angles (front, back, detail, scale)",
        "[ ] Lifestyle/in-use photos", "[ ] Flat lay composition",
        "[ ] Consistent editing style", "[ ] Brand color visible"]
    for item in photo_items:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 14
    y -= 15
    doc.add_text(72, y, "SHOP BRANDING:", 'F2', 10)
    y -= 16
    brand = ["Shop name: ________________________________",
        "Tagline: ________________________________",
        "Brand colors: ________________________________",
        "Logo style: ________________________________",
        "Brand voice (3 words): ________________________________",
        "About page key message: ________________________________",
        "Policies (shipping/returns): ________________________________"]
    for item in brand:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 16

    # Financial Tracker (12 monthly)
    for m_idx, month in enumerate(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]):
        doc.new_page()
        doc.add_centered_text(760, f"FINANCIAL TRACKER - {month.upper()}", 'F2', 12)
        doc.add_line(72, 748, 540, 748, 0.5, 0.3)
        y = 730
        doc.add_text(72, y, "REVENUE:", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Product sales: $______  Shipping collected: $______", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "TOTAL REVENUE: $______", 'F2', 8)
        y -= 18
        doc.add_text(72, y, "EXPENSES:", 'F2', 9)
        y -= 14
        expenses = ["Etsy fees (listing+transaction+payment)", "Supplies/materials",
                    "Shipping costs", "Packaging", "Advertising/Etsy Ads",
                    "Software/tools", "Other"]
        for exp in expenses:
            doc.add_text(90, y, f"{exp}: $______", 'F1', 8)
            y -= 12
        doc.add_text(90, y, "TOTAL EXPENSES: $______", 'F2', 8)
        y -= 18
        doc.add_filled_rect(72, y-12, 468, 18, 0.92)
        doc.add_text(80, y, "NET PROFIT: $______  Profit margin: ____%  Orders: ___", 'F2', 9)


    # Marketing Calendar
    doc.new_page()
    doc.add_centered_text(750, "MARKETING CALENDAR & STRATEGY", 'F2', 13)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    platforms = [
        ("PINTEREST", "Pins/week: ___  Boards: ___  Best times: ___"),
        ("INSTAGRAM", "Posts/week: ___  Stories/day: ___  Reels/week: ___"),
        ("TIKTOK", "Videos/week: ___  Trending sounds: ___"),
        ("EMAIL LIST", "Emails/month: ___  Lead magnet: ___________"),
        ("ETSY ADS", "Daily budget: $___  Target ROAS: ___x"),
        ("SALES/COUPONS", "Frequency: ___  Discount range: ___-___% off"),
    ]
    for platform, details in platforms:
        doc.add_text(72, y, platform, 'F2', 9)
        y -= 14
        doc.add_text(90, y, details, 'F1', 8)
        y -= 14
        doc.add_text(90, y, "Content ideas: ________________________________", 'F1', 8)
        y -= 22

    # Customer Service Scripts
    doc.new_page()
    doc.add_centered_text(750, "CUSTOMER SERVICE SCRIPTS", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    situations = [
        "1. Order confirmation / thank you",
        "2. Shipping delay notification",
        "3. Custom order inquiry response",
        "4. Refund/exchange request",
        "5. Negative review response",
        "6. Asking for a review (post-delivery)",
        "7. Out-of-stock notification",
        "8. Wholesale inquiry",
        "9. Copyright/design theft report",
        "10. General inquiry response",
    ]
    for sit in situations:
        doc.add_text(72, y, sit, 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Script: ________________________________", 'F1', 8)
        doc.add_line(130, y-2, 540, y-2, 0.5, 0.5)
        y -= 20

    # Scaling + Quarterly Review + Annual Goals + Tax
    doc.new_page()
    doc.add_centered_text(750, "SCALING & QUARTERLY REVIEW", 'F2', 13)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "SCALING CHECKLIST:", 'F2', 10)
    y -= 16
    scale = ["[ ] Consistent 10+ orders/week", "[ ] Hire help for production/shipping",
        "[ ] Expand to 50+ listings", "[ ] Add new product line",
        "[ ] Diversify to own website", "[ ] Wholesale/retail partnerships",
        "[ ] Automation tools in place"]
    for item in scale:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 14
    y -= 15
    doc.add_text(72, y, "QUARTERLY REVIEWS:", 'F2', 10)
    y -= 16
    for q in ["Q1", "Q2", "Q3", "Q4"]:
        doc.add_text(90, y, f"{q}: Revenue $______ Orders ___ Avg order $____ Top product: ________", 'F1', 8)
        y -= 14
    y -= 15
    doc.add_text(72, y, "ANNUAL GOALS:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "Revenue target: $______  Order target: ______", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "New listings target: ___  Star seller? [ ] Yes", 'F1', 9)
    y -= 20
    doc.add_text(72, y, "TAX PREPARATION:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "Keep: Etsy payments CSV, expense receipts, mileage log", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Schedule C categories: ________________________________", 'F1', 9)

    doc.save("Book229_Etsy_Business_Complete.pdf")
    print("Created: Book229_Etsy_Business_Complete.pdf")

if __name__ == "__main__":
    create_book()
