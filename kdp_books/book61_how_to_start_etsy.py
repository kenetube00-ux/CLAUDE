"""
Book 61: How To Start An Etsy Shop - A Step-by-Step Guide for Beginners
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "HOW TO START AN ETSY SHOP", font='F2', size=22)
    pdf.add_centered_text(485, "A Step-by-Step Guide for Beginners", font='F1', size=14)
    pdf.add_line(80, 460, 352, 460, 2)
    pdf.add_centered_text(420, "Turn Your Creativity Into a", font='F4', size=13)
    pdf.add_centered_text(398, "Thriving Online Business", font='F4', size=13)
    pdf.add_centered_text(330, "By", font='F1', size=12)
    pdf.add_centered_text(305, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "How To Start An Etsy Shop", font='F2', size=11)
    pdf.add_centered_text(475, "A Step-by-Step Guide for Beginners", font='F1', size=10)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(390, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(365, "Published via Amazon KDP", font='F1', size=10)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: What is Etsy?", [
            "Etsy is an online marketplace focused on handmade, vintage, and craft items.",
            "Founded in 2005, it now has over 90 million active buyers worldwide.",
            "Unlike Amazon, Etsy shoppers specifically seek unique and creative products.",
            "You can sell physical goods, digital downloads, or vintage items over 20 years old.",
            "Popular categories include jewelry, home decor, art prints, and personalized gifts.",
            "Etsy charges a small listing fee of $0.20 per item plus a transaction fee.",
            "The platform handles payments so you do not need your own payment processor.",
            "Many sellers start as a side hustle and grow into full-time businesses.",
            "You do not need a business license to start but check your local laws.",
            "Etsy provides built-in traffic so you do not need to build your own website.",
            "Millions of people earn a living selling on Etsy from their homes.",
            "This book will guide you from zero to your first sale step by step.",
        ]),
        ("Chapter 2: Setting Up Your Account", [
            "Go to etsy.com and click the Sell on Etsy button to begin registration.",
            "You will need a valid email address, your name, and your country.",
            "Choose your shop language and currency based on your target market.",
            "Etsy will ask you to name your shop which must be unique on the platform.",
            "Your shop name should be memorable, easy to spell, and reflect your brand.",
            "Avoid numbers and special characters that make your name hard to remember.",
            "Set up your payment method to receive funds via direct deposit or PayPal.",
            "Add a billing method so Etsy can charge listing and transaction fees.",
            "Complete your shop profile with a photo and a compelling bio about yourself.",
            "Write your shop announcement to greet visitors and explain what you sell.",
            "Set your shop policies including shipping times, returns, and exchanges.",
            "Verify your identity if prompted to build trust with potential buyers.",
        ]),
        ("Chapter 3: Choosing a Niche", [
            "A niche is a specific category of products you specialize in selling.",
            "Successful Etsy shops focus on one area rather than selling everything.",
            "Research trending niches by browsing Etsy bestsellers and social media.",
            "Consider your skills, hobbies, and passions when choosing your niche.",
            "Look for niches with demand but not overwhelming competition.",
            "Digital products like printables and templates have zero shipping costs.",
            "Personalized items like custom name jewelry consistently sell well.",
            "Wedding items have high demand and buyers willing to pay premium prices.",
            "Pet products are a growing niche with passionate buyers.",
            "Use Etsy search to see how many results appear for your product ideas.",
            "Check if top sellers in your niche have many sales proving demand exists.",
            "Start narrow and expand later once you understand your customers.",
        ]),
        ("Chapter 4: Product Photography Tips", [
            "Great photos are the number one factor in getting Etsy sales.",
            "Use natural light by photographing near a large window during daytime.",
            "A white poster board makes an affordable clean background for products.",
            "Take photos from multiple angles: front, back, side, and detail shots.",
            "Include a photo showing scale so buyers understand the actual size.",
            "Lifestyle photos showing your product in use dramatically increase sales.",
            "Use your smartphone camera which is perfectly adequate for Etsy photos.",
            "Keep backgrounds clean and uncluttered so the product is the focus.",
            "Edit photos for brightness and contrast using free apps like Snapseed.",
            "Etsy allows up to 10 photos per listing so use all available slots.",
            "Your first photo is the thumbnail shoppers see in search results.",
            "Consistent photo style across listings makes your shop look professional.",
        ]),
        ("Chapter 5: Writing Listings That Sell", [
            "Your listing title should include keywords buyers actually search for.",
            "Front-load the most important keywords at the beginning of your title.",
            "Write descriptions that answer every question a buyer might have.",
            "Include dimensions, materials, colors, and care instructions clearly.",
            "Use bullet points or short paragraphs so descriptions are easy to scan.",
            "Tell a story about your product to create an emotional connection.",
            "Mention the problem your product solves or the joy it brings.",
            "Include information about customization options and how to request them.",
            "Address common concerns like shipping time and packaging in descriptions.",
            "Use all 13 keyword tags Etsy gives you for each listing.",
            "Update listings regularly as Etsy favors recently refreshed content.",
            "Study bestselling competitors to learn what their descriptions include.",
        ]),
        ("Chapter 6: Pricing Your Products", [
            "Many new sellers underprice their work which leads to burnout and failure.",
            "Calculate your costs: materials, packaging, shipping supplies, and Etsy fees.",
            "Add your time at a fair hourly rate even if this is a hobby.",
            "The basic formula is: materials plus labor plus overhead times two.",
            "Research what competitors charge for similar items in your niche.",
            "Factor in Etsy fees: listing fee, transaction fee, and payment processing.",
            "Free shipping often increases sales so consider building it into your price.",
            "Offer multiple price points with basic and premium versions of products.",
            "Do not compete solely on price as this is a race to the bottom.",
            "Raise prices gradually as you gain reviews and establish your brand.",
            "Test different price points to find what converts best for your items.",
            "Remember that buyers on Etsy expect to pay more for handmade quality.",
        ]),
        ("Chapter 7: Shipping Basics", [
            "Choose between flat rate shipping and calculated shipping by weight.",
            "USPS, UPS, and FedEx all offer competitive rates for small packages.",
            "Etsy provides discounted shipping labels you can print at home.",
            "Invest in a small postal scale to weigh packages accurately.",
            "Stock up on shipping supplies: boxes, mailers, bubble wrap, and tape.",
            "Set realistic processing times you can consistently meet.",
            "Always add tracking numbers so both you and buyers can follow packages.",
            "Consider offering free shipping on orders over a certain amount.",
            "International shipping opens your market but adds complexity and cost.",
            "Package items securely with extra protection for fragile products.",
            "Include a thank you note or small freebie to delight your customers.",
            "Ship on time or early to build a reputation for reliability.",
        ]),
        ("Chapter 8: Etsy SEO Keywords", [
            "SEO means Search Engine Optimization and helps buyers find your listings.",
            "Etsy search works differently from Google so learn its specific rules.",
            "Use long-tail keywords that describe exactly what your product is.",
            "Think like a buyer: what words would they type to find your item?",
            "Use all 13 tags per listing and make each one a unique phrase.",
            "Your title, tags, categories, and attributes all affect search ranking.",
            "Etsy also considers listing quality score based on clicks and purchases.",
            "Renew listings strategically as freshly renewed items get a temporary boost.",
            "Use Etsy search bar suggestions to discover what people are searching.",
            "Tools like eRank and Marmalead help you research keyword competition.",
            "Avoid single-word tags as they are too broad and competitive.",
            "Update your keywords seasonally to capture holiday and trending searches.",
        ]),
        ("Chapter 9: Customer Service Tips", [
            "Respond to all messages within 24 hours to maintain your response rate.",
            "Be friendly, professional, and helpful even with difficult customers.",
            "Answer questions thoroughly to prevent misunderstandings before purchase.",
            "Set clear expectations in your listings to reduce customer service issues.",
            "Handle complaints gracefully as one bad review can hurt your shop.",
            "Offer solutions like replacements or refunds when problems arise.",
            "Follow up after delivery to ensure customers are satisfied.",
            "A five-star review is worth more than any single sale in the long run.",
            "Create FAQ sections in your listings for common questions.",
            "Personalize your communication so customers feel valued and special.",
            "Use saved replies for common questions to save time without losing quality.",
            "Happy customers become repeat buyers and recommend you to friends.",
        ]),
        ("Chapter 10: Marketing Your Shop", [
            "Pinterest is the most effective social platform for driving Etsy traffic.",
            "Create pins linking to your listings with beautiful product images.",
            "Instagram works well for behind-the-scenes content and building connection.",
            "Use relevant hashtags on social media to reach potential customers.",
            "Email marketing lets you notify past customers about new products.",
            "Etsy Ads can boost visibility but start with a small daily budget.",
            "Collaborate with other Etsy sellers for cross-promotion opportunities.",
            "Run seasonal sales and promotions to boost traffic during slower periods.",
            "Create gift guides featuring your products for holidays and occasions.",
            "Engage in Etsy teams and forums to network with other sellers.",
            "Blogging about your craft process attracts people interested in your niche.",
            "Consistency matters more than perfection in your marketing efforts.",
        ]),
        ("Chapter 11: Managing Finances", [
            "Keep your business finances separate from personal accounts.",
            "Open a dedicated bank account for your Etsy income and expenses.",
            "Track every expense including materials, shipping, and Etsy fees.",
            "Save receipts for tax deductions related to your business.",
            "Set aside 25 to 30 percent of profits for taxes if you are in the US.",
            "Use accounting software like Wave (free) or QuickBooks to track finances.",
            "Understand that Etsy deposits payments on a regular schedule.",
            "Review your Etsy payment account regularly for accuracy.",
            "Calculate your true profit after all fees, materials, and time investment.",
            "Reinvest some profits back into your business for growth.",
            "Consult a tax professional once your income becomes significant.",
            "Plan for seasonal fluctuations in income throughout the year.",
        ]),
        ("Chapter 12: Scaling Your Business", [
            "Scaling means growing your revenue without proportionally increasing work.",
            "Identify your bestselling items and create variations of those products.",
            "Streamline your production process to make items faster.",
            "Consider hiring help for packaging, shipping, or production tasks.",
            "Batch similar tasks together for efficiency in your workflow.",
            "Add digital products that can be sold unlimited times with no extra work.",
            "Expand to complementary product lines that appeal to existing customers.",
            "Raise prices as demand grows rather than trying to sell more at low prices.",
            "Invest in better tools and equipment to improve production speed.",
            "Consider expanding to other platforms like your own website or Amazon Handmade.",
            "Automate repetitive tasks like social media posting and inventory tracking.",
            "Set revenue goals and create action plans to reach each milestone.",
        ]),
        ("Chapter 13: Common Mistakes to Avoid", [
            "Do not open your shop with only one or two listings. Aim for at least 20.",
            "Avoid copying other sellers as Etsy can suspend shops for infringement.",
            "Do not use trademarked terms or characters without proper licensing.",
            "Never ignore customer messages as this hurts your shop ranking.",
            "Avoid underpricing your products just to make quick sales.",
            "Do not skip product photography and use stock images instead.",
            "Avoid generic titles and descriptions that do not include keywords.",
            "Do not give up after one month. Most shops take 3-6 months to gain traction.",
            "Never buy fake reviews as Etsy will permanently ban your shop.",
            "Avoid overpromising on shipping times you cannot consistently meet.",
            "Do not neglect your shop after initial setup. Regular updates matter.",
            "Avoid trying to sell everything. Focus on your niche and do it well.",
        ]),
        ("Chapter 14: Legal Basics (Taxes/Licenses)", [
            "Check your local city and state requirements for business licenses.",
            "A sole proprietorship is the simplest business structure to start with.",
            "You may need a sales tax permit depending on your state.",
            "Report all Etsy income on your tax return even if you do not get a 1099.",
            "Home business deductions can include a portion of rent and utilities.",
            "Keep records of all business expenses for at least seven years.",
            "Consider liability insurance especially if you sell consumable products.",
            "Understand intellectual property laws to protect your designs.",
            "Trademark your brand name if you plan to grow significantly.",
            "Consult a local small business development center for free guidance.",
            "Many cities have free workshops for new entrepreneurs on legal basics.",
            "Start simple and add legal protections as your business grows.",
        ]),
        ("Chapter 15: Your First 30-Day Plan", [
            "Days 1-3: Research your niche and study successful shops in that category.",
            "Days 4-5: Set up your Etsy account and complete all shop profile sections.",
            "Days 6-10: Create your first 10 products or designs for your shop.",
            "Days 11-13: Photograph all products with multiple angles and good lighting.",
            "Days 14-16: Write compelling listings with keyword-rich titles and descriptions.",
            "Days 17-18: Set up shipping profiles and pricing for all your items.",
            "Day 19: Publish all listings and make your shop officially open.",
            "Days 20-22: Set up social media accounts (Pinterest and Instagram minimum).",
            "Days 23-25: Create and post content driving traffic to your Etsy shop.",
            "Days 26-28: Add 5-10 more listings. More listings means more visibility.",
            "Days 29-30: Review analytics, adjust keywords, and plan next month.",
            "Celebrate your progress! Most people never take the first step at all.",
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

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book61_How_To_Start_Etsy.pdf')
    print("Book 61 created: Book61_How_To_Start_Etsy.pdf")

if __name__ == '__main__':
    create_book()
