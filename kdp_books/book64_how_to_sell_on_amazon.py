"""
Book 64: How To Sell On Amazon - From Zero to Your First Sale
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "HOW TO SELL ON AMAZON", font='F2', size=22)
    pdf.add_centered_text(485, "From Zero to Your First Sale", font='F1', size=14)
    pdf.add_line(80, 460, 352, 460, 2)
    pdf.add_centered_text(420, "Build a Profitable Amazon Business", font='F4', size=13)
    pdf.add_centered_text(398, "Even If You Have No Experience", font='F4', size=13)
    pdf.add_centered_text(330, "By", font='F1', size=12)
    pdf.add_centered_text(305, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "How To Sell On Amazon", font='F2', size=11)
    pdf.add_centered_text(475, "From Zero to Your First Sale", font='F1', size=10)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(390, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(365, "Published via Amazon KDP", font='F1', size=10)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: Amazon Selling Overview", [
            "Amazon is the largest online marketplace with over 300 million active customers.",
            "Third-party sellers account for nearly sixty percent of all Amazon sales.",
            "You do not need to manufacture products. You can resell existing items.",
            "There are multiple business models: retail arbitrage, wholesale, and private label.",
            "Retail arbitrage means buying discounted items in stores and reselling on Amazon.",
            "Wholesale means buying in bulk from manufacturers at reduced prices.",
            "Private label means creating your own branded products manufactured for you.",
            "Amazon handles shipping and customer service if you use their FBA program.",
            "Average startup costs range from five hundred to three thousand dollars.",
            "Many sellers earn their first sale within two to four weeks of starting.",
            "This is a real business that requires effort, patience, and learning.",
            "This book will walk you through every step from account setup to scaling.",
        ]),
        ("Chapter 2: Individual vs Professional Accounts", [
            "Amazon offers two seller account types: Individual and Professional.",
            "Individual accounts are free monthly but charge 99 cents per item sold.",
            "Professional accounts cost 39.99 per month but have no per-item fee.",
            "If you plan to sell more than 40 items per month, go Professional.",
            "Professional accounts unlock advertising, bulk listing tools, and reports.",
            "Individual accounts cannot win the Buy Box which is where most sales happen.",
            "You can start with Individual and upgrade to Professional at any time.",
            "Both account types pay the same referral fees, usually 15 percent of price.",
            "Professional sellers can create listings for products not yet on Amazon.",
            "You need a bank account, credit card, government ID, and tax information.",
            "Amazon verifies your identity which can take a few days to complete.",
            "Choose Professional from the start if you are serious about building a business.",
        ]),
        ("Chapter 3: Finding Profitable Products", [
            "The best products to sell are lightweight, unbreakable, and priced 15-50 dollars.",
            "Avoid categories dominated by major brands like Apple or Nike.",
            "Look for products with high demand but moderate competition on Amazon.",
            "Use the Amazon Best Sellers list to identify hot-selling categories.",
            "A product selling at least ten units per day per competitor indicates good demand.",
            "Check the number of reviews on top listings. Under 500 reviews means opportunity.",
            "Avoid seasonal products unless you plan to sell multiple seasonal items.",
            "Products with room for improvement based on negative reviews are ideal.",
            "Read competitor one and two star reviews to find what customers want fixed.",
            "Tools like Jungle Scout and Helium 10 provide sales estimates for products.",
            "Never choose a product based on gut feeling alone. Use data to decide.",
            "Start with one product, learn the process, then expand to more items.",
        ]),
        ("Chapter 4: Sourcing Products", [
            "Retail arbitrage is the fastest way to start: buy clearance items and resell.",
            "Scan products using the Amazon Seller app to see selling price and fees instantly.",
            "Stores like Walmart, Target, and TJ Maxx have profitable clearance sections.",
            "Look for items priced 75 percent or more below their Amazon selling price.",
            "Wholesale sourcing means buying directly from brands at 50 percent off retail.",
            "Find wholesale suppliers at trade shows, industry directories, and online.",
            "Contact brands directly and ask for their wholesale program requirements.",
            "Private label involves finding manufacturers on Alibaba to make your product.",
            "When using Alibaba, order samples from three to five suppliers before committing.",
            "Minimum order quantities for private label are usually 500 to 1000 units.",
            "Always get product liability insurance when selling private label items.",
            "Start with arbitrage to learn Amazon, then graduate to wholesale or private label.",
        ]),
        ("Chapter 5: Creating Your Seller Account", [
            "Go to sellercentral.amazon.com and click the sign up button.",
            "Have ready: government ID, bank statement, credit card, and phone number.",
            "Amazon will verify your identity through a video call or document upload.",
            "The verification process typically takes two to five business days.",
            "Once approved, complete your seller profile with your business information.",
            "Set up your deposit method so Amazon can send you your sales revenue.",
            "Configure your shipping settings and return address in account settings.",
            "Explore Seller Central and familiarize yourself with the dashboard layout.",
            "The main sections are inventory, orders, advertising, and reports.",
            "Enable two-factor authentication to protect your seller account.",
            "Download the Amazon Seller app for managing your business on the go.",
            "Your account is now ready for you to list your first product.",
        ]),
        ("Chapter 6: Listing Your First Product", [
            "Search for your product on Amazon to see if a listing already exists.",
            "If the listing exists, click Sell on Amazon to add your offer to it.",
            "If no listing exists, create a new one with title, description, and images.",
            "Choose the correct category and subcategory for your product type.",
            "Fill in all product details: brand, size, color, material, and weight.",
            "Set your selling price competitively based on research of similar items.",
            "Determine your fulfillment method: FBA (Amazon ships) or FBM (you ship).",
            "For FBA, set your quantity and create a shipping plan to send items in.",
            "Indicate product condition accurately: new, used, refurbished, or collectible.",
            "Add your SKU number to track inventory and identify products easily.",
            "Review everything carefully before publishing. Accuracy builds trust.",
            "Your listing will be active within minutes of publishing.",
        ]),
        ("Chapter 7: Product Photography", [
            "Amazon requires the main image to have a pure white background.",
            "The product should fill at least 85 percent of the image frame.",
            "Main images cannot include text, logos, watermarks, or props.",
            "Use at least seven images: main, lifestyle, infographic, and detail shots.",
            "Lifestyle images show your product being used by real people in context.",
            "Infographic images highlight key features and dimensions with text overlays.",
            "Detail shots show texture, craftsmanship, and quality up close.",
            "Hire a photographer on Fiverr for 50-100 dollars if you cannot do it yourself.",
            "Image dimensions should be at least 2000 pixels for the zoom feature.",
            "Products with seven or more images convert significantly higher than those with fewer.",
            "Compare your images to the best sellers in your category for quality standards.",
            "Great images are your most important investment for converting browsers to buyers.",
        ]),
        ("Chapter 8: Writing Effective Bullet Points", [
            "Amazon gives you five bullet points to highlight your product benefits.",
            "Lead each bullet with a capitalized benefit header followed by details.",
            "Focus on benefits to the customer, not just features of the product.",
            "Instead of saying waterproof material say never worry about rain ruining it.",
            "Include keywords naturally in your bullets for search visibility.",
            "Address common customer objections and concerns in your bullets.",
            "Mention what is included in the package so buyers know exactly what they get.",
            "Keep bullets readable: two to three lines each, not massive paragraphs.",
            "Use the first bullet for your strongest selling point since most people read it.",
            "Include size, material, and compatibility information buyers need to decide.",
            "Study top competitors bullets and note what they emphasize.",
            "Well-written bullets can double your conversion rate from visitors to buyers.",
        ]),
        ("Chapter 9: Amazon SEO Basics", [
            "Amazon SEO is about ranking your product higher in Amazon search results.",
            "The Amazon algorithm is called A9 and it prioritizes products that sell well.",
            "Include your main keyword in the product title for maximum search visibility.",
            "Use all available backend search term fields with relevant keywords.",
            "Do not repeat words that already appear in your title in backend terms.",
            "Sales velocity is the strongest ranking factor: more sales means higher rank.",
            "Click-through rate matters: great images and titles get more clicks.",
            "Conversion rate matters: good descriptions and reviews turn clicks into sales.",
            "Use competitor product titles for keyword research inspiration.",
            "Tools like Helium 10 Cerebro show which keywords competitors rank for.",
            "Price competitively at launch to generate initial sales velocity.",
            "Amazon SEO is an ongoing process. Monitor and adjust keywords monthly.",
        ]),
        ("Chapter 10: FBA vs FBM Explained", [
            "FBA means Fulfillment by Amazon: you send inventory, they store and ship it.",
            "FBM means Fulfillment by Merchant: you store inventory and ship orders yourself.",
            "FBA products get the Prime badge which dramatically increases sales.",
            "Amazon handles all customer service and returns for FBA items.",
            "FBA fees include storage fees and fulfillment fees based on size and weight.",
            "FBM has lower fees but you handle packing, shipping, and customer service.",
            "FBM makes sense for large, heavy, or slow-selling items.",
            "FBA makes sense for small, lightweight items that sell consistently.",
            "Most successful sellers use FBA because Prime customers spend more.",
            "Long-term storage fees apply to FBA items stored over 365 days.",
            "You can use both methods simultaneously for different products.",
            "For beginners, FBA is recommended to focus on sourcing rather than shipping.",
        ]),
        ("Chapter 11: Pricing Strategies", [
            "Price your product competitively by analyzing the top ten sellers in your niche.",
            "Factor in all costs: product cost, shipping to Amazon, FBA fees, and advertising.",
            "Aim for at least 30 percent profit margin after all Amazon fees.",
            "Use the Amazon FBA Revenue Calculator to estimate your actual profit per unit.",
            "Consider launching at a lower price initially to generate reviews and sales velocity.",
            "Raise your price gradually once you have reviews and consistent sales.",
            "Monitor competitor prices regularly and adjust to stay competitive.",
            "Avoid price wars that drive profits to zero for everyone in the category.",
            "Bundle products together to create unique offers that cannot be price-compared.",
            "Offer coupons and deals through Amazon to boost conversion without lowering list price.",
            "Test different price points to find the sweet spot for maximum profit.",
            "Remember: the cheapest price does not always win. Value and reviews matter more.",
        ]),
        ("Chapter 12: Getting Your First Reviews", [
            "Reviews are critical because 90 percent of buyers read them before purchasing.",
            "Amazon Vine program lets you give free products to trusted reviewers.",
            "Request a Review button in Seller Central sends Amazon-approved review requests.",
            "Include a product insert card thanking customers and encouraging reviews.",
            "Never offer incentives, discounts, or free products in exchange for reviews.",
            "Violating review policies will get your account permanently suspended.",
            "Great products and packaging naturally generate positive reviews over time.",
            "Follow up with buyers who contact customer service to ensure satisfaction.",
            "Respond professionally to negative reviews showing you care about quality.",
            "Your first ten reviews are the hardest. After that momentum builds naturally.",
            "Products with at least 15 reviews convert significantly better than those without.",
            "Focus on product quality and customer experience as your review strategy.",
        ]),
        ("Chapter 13: Amazon PPC Ads Basics", [
            "PPC means Pay Per Click: you only pay when someone clicks your ad.",
            "Amazon advertising puts your product at the top of search results.",
            "Start with Sponsored Products automatic campaigns to discover keywords.",
            "Set a daily budget of ten to twenty dollars when starting out.",
            "Let automatic campaigns run for two weeks to gather keyword data.",
            "Then create manual campaigns targeting the keywords that converted to sales.",
            "Your advertising cost of sale (ACoS) should ideally be below 30 percent.",
            "Negative keywords prevent your ads from showing for irrelevant searches.",
            "Bid higher on keywords that are converting well and lower on poor performers.",
            "Product targeting ads show your listing on competitor product pages.",
            "Advertising is essential at launch but can be reduced once organic rank improves.",
            "Think of PPC as an investment in ranking, not just a cost of doing business.",
        ]),
        ("Chapter 14: Managing Inventory", [
            "Running out of stock kills your search ranking and takes weeks to recover.",
            "Track sales velocity and reorder before you run out, not after.",
            "Set reorder points based on lead time plus a safety buffer.",
            "If your supplier takes 30 days, reorder when you have 45 days of stock left.",
            "Use Amazon inventory planning tools to get restock recommendations.",
            "Excess inventory ties up cash and incurs long-term storage fees.",
            "Find the balance between having enough stock and not over-ordering.",
            "Seasonal products require planning months ahead for holiday demand spikes.",
            "Track your inventory performance index (IPI) score in Seller Central.",
            "A low IPI score means Amazon limits how much inventory you can send in.",
            "Consider using a third-party logistics warehouse as backup storage.",
            "Good inventory management is the difference between profit and problems.",
        ]),
        ("Chapter 15: Scaling to 6 Figures", [
            "Most sellers reach six figures by having five to ten successful products.",
            "Reinvest profits into inventory and new product launches consistently.",
            "Expand into related product categories that share your target audience.",
            "Build a brand with consistent packaging, inserts, and customer experience.",
            "Register your brand through Amazon Brand Registry for extra tools and protection.",
            "Create A-Plus Content (enhanced descriptions) to improve conversion rates.",
            "Launch new products using the exact process that worked for your first one.",
            "Hire a virtual assistant to handle routine tasks like customer messages.",
            "Use inventory management software as your catalog grows beyond ten products.",
            "Consider expanding to international Amazon marketplaces like UK, Canada, and Germany.",
            "Join Amazon seller communities to network and learn from experienced sellers.",
            "Six figures is achievable within 12-18 months with consistent effort and reinvestment.",
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

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book64_How_To_Sell_On_Amazon.pdf')
    print("Book 64 created: Book64_How_To_Sell_On_Amazon.pdf")

if __name__ == '__main__':
    create_book()
