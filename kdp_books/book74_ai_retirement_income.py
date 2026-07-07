"""Book 74: AI Side Hustles for Retirees - Earn Extra Income Using AI Tools"""
from pdf_utils import PDFDoc

doc = PDFDoc(432, 648)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 432, 648, 0.93)
doc.add_centered_text(530, "AI SIDE HUSTLES", 'F2', 21)
doc.add_centered_text(500, "FOR RETIREES", 'F2', 21)
doc.add_centered_text(460, "Earn Extra Income", 'F5', 15)
doc.add_centered_text(438, "Using AI Tools", 'F5', 15)
doc.add_line(110, 420, 322, 420, 2, 0.3)
doc.add_centered_text(385, "Practical Ways to Monetize AI Skills", 'F1', 12)
doc.add_centered_text(363, "Without Prior Tech Experience", 'F1', 12)
doc.add_centered_text(200, "Daniel Tesfamariam", 'F2', 14)
doc.add_centered_text(175, "2024", 'F1', 11)

# Copyright page
doc.new_page()
doc.add_centered_text(500, "AI SIDE HUSTLES FOR RETIREES", 'F2', 13)
doc.add_centered_text(475, "Earn Extra Income Using AI Tools", 'F4', 10)
doc.add_centered_text(440, "Copyright 2024 Daniel Tesfamariam", 'F1', 10)
doc.add_centered_text(420, "All rights reserved.", 'F1', 10)
doc.add_centered_text(390, "No part of this publication may be reproduced without permission.", 'F1', 9)
doc.add_centered_text(360, "Published independently via KDP.", 'F1', 10)
doc.add_centered_text(330, "Income examples are illustrative. Individual results vary.", 'F1', 9)

chapters = [
    ("Chapter 1: Why Retirees Should Learn AI", [
        "Retirement does not mean stopping - it means choosing how you spend your time.",
        "AI tools can turn your decades of experience into income with minimal effort.",
        "You have something younger people lack: deep expertise, patience, and wisdom.",
        "AI handles the technical heavy lifting while you provide the human insight.",
        "Many retirees earn $500 to $3000 per month using simple AI-assisted services.",
        "You work when you want, where you want, with no boss and no commute.",
        "AI skills are in high demand because most businesses are just starting to adopt them.",
        "Learning AI keeps your mind sharp while also supplementing your retirement income.",
        "You do not need to invest large amounts of money - most AI tools are free or cheap.",
        "This book shows you exactly how to start earning with AI within 30 days.",
        "Your life experience combined with AI tools is an unbeatable competitive advantage.",
    ]),
    ("Chapter 2: AI Writing for Freelance Income", [
        "AI writing tools like ChatGPT can help you produce professional content quickly.",
        "Businesses need blog posts, newsletters, product descriptions, and social media content.",
        "You provide the strategy and editing; AI generates the first draft in seconds.",
        "Freelance writers using AI can complete work 3-5 times faster than before.",
        "Platforms like Upwork and Fiverr connect you with clients seeking writing help.",
        "Typical rates: $50-200 per blog post, $500-2000 per month for regular clients.",
        "Your life experience makes you a better writer - AI just speeds up the process.",
        "Editing AI-generated text is easier than writing from scratch and pays well.",
        "Niche expertise (health, finance, travel) commands premium rates from clients.",
        "Start by offering services to local small businesses who need help with marketing.",
        "Build a portfolio with 3-5 sample pieces and you are ready to find paying clients.",
    ]),
    ("Chapter 3: Using ChatGPT to Write Ebooks", [
        "Self-publishing ebooks on Amazon KDP is one of the most accessible AI side hustles.",
        "ChatGPT helps you outline, draft, and edit books on topics you know well.",
        "Non-fiction books about your expertise (gardening, cooking, woodworking) sell steadily.",
        "AI handles formatting, table of contents, and even suggests compelling titles.",
        "You can publish a quality ebook in 1-2 weeks with AI assistance.",
        "Ebooks earn passive income - write once, sell forever with no additional work.",
        "AI cover design tools create professional book covers without graphic design skills.",
        "Price your ebooks at $2.99-9.99 and earn 35-70 percent royalty on every sale.",
        "Low-content books (journals, planners, logbooks) are even simpler to create.",
        "Research trending topics using AI to find niches with demand but low competition.",
        "Aim to publish 5-10 books and let compound royalties build your monthly income.",
    ]),
    ("Chapter 4: AI-Powered Proofreading Services", [
        "Proofreading with AI tools like Grammarly makes you faster and more accurate.",
        "Authors, students, and businesses all need affordable proofreading services.",
        "AI catches 90 percent of errors; you catch the subtle ones AI misses.",
        "This combination makes you more accurate than either humans or AI alone.",
        "Rates range from $25-50 per hour or 2-5 cents per word for proofreading.",
        "Platforms like Scribendi, ProofreadingPal, and Reedsy connect you with clients.",
        "Academic proofreading (theses, dissertations) pays premium rates year-round.",
        "AI tools learn your editing style and become faster over time with your input.",
        "You can proofread from anywhere - your couch, a coffee shop, or while traveling.",
        "Start with free practice texts online to build speed before taking paid work.",
        "This is ideal for detail-oriented retirees who enjoy reading and language.",
    ]),
    ("Chapter 5: Starting an AI-Assisted Blog", [
        "Blogs generate income through ads, affiliate links, and sponsored content over time.",
        "AI helps you write, optimize, and promote blog posts consistently.",
        "Choose a topic you love: travel for seniors, retirement tips, gardening, or cooking.",
        "AI SEO tools help your posts rank on Google where readers can find them.",
        "Write 2-3 posts per week with AI assistance - about 1-2 hours of work per post.",
        "Income typically starts after 3-6 months as your traffic grows organically.",
        "Successful bloggers earn $1000-5000 per month from ads and affiliate marketing.",
        "WordPress and AI plugins handle all the technical aspects automatically.",
        "AI-generated images and graphics make your posts more visually appealing.",
        "Email list building with AI helps you develop a loyal, returning audience.",
        "Patience is key - blogging is a slow build but provides lasting passive income.",
    ]),
    ("Chapter 6: AI Social Media Management for Businesses", [
        "Small businesses desperately need help managing their social media presence.",
        "AI tools create, schedule, and optimize social media posts automatically.",
        "You manage 3-5 local business accounts and charge $500-1500 per month each.",
        "AI generates post ideas, captions, hashtags, and even creates graphics.",
        "Scheduling tools like Buffer and Hootsuite post content at optimal times.",
        "AI analytics tell you what is working so you can improve results for clients.",
        "Local businesses (restaurants, shops, salons) are ideal first clients to approach.",
        "You do not need to be on social media yourself to manage it for others.",
        "AI handles engagement by suggesting replies to comments and messages.",
        "This work takes 5-10 hours per week and can be done entirely from home.",
        "Start by managing one account for free to build a case study, then charge for more.",
    ]),
    ("Chapter 7: Selling AI-Generated Art Prints", [
        "AI art generators like Midjourney and DALL-E create stunning images from text descriptions.",
        "Print-on-demand services (Printful, Redbubble) sell your art with no upfront inventory cost.",
        "Your artistic eye and life experience help you create images people actually want to buy.",
        "Popular categories: nature scenes, vintage styles, motivational quotes, pet portraits.",
        "Each successful design can sell hundreds of times without additional work from you.",
        "AI art for home decor, phone cases, mugs, and t-shirts reaches a global market.",
        "Etsy is the most popular platform for handmade and AI-assisted art products.",
        "Price prints at $15-50 depending on size, earning $5-25 profit per sale.",
        "Create collections around themes: seasons, holidays, hobbies, or home decor styles.",
        "AI lets you iterate rapidly - create 20 variations and sell the best ones.",
        "No artistic skill required - your creativity and curation are the real value.",
    ]),
    ("Chapter 8: AI Transcription and Captioning", [
        "AI transcription tools convert audio and video to text with high accuracy.",
        "Your job is to review and correct AI transcriptions, not type from scratch.",
        "Clients include podcasters, YouTubers, lawyers, medical professionals, and researchers.",
        "Rates range from $15-40 per audio hour, and AI makes you 4x faster than manual typing.",
        "Rev, TranscribeMe, and GoTranscript are popular platforms for finding work.",
        "AI captioning for accessibility is required by law for many organizations.",
        "You can specialize in a field where your vocabulary knowledge gives you an advantage.",
        "Medical and legal transcription pay premium rates due to specialized terminology.",
        "Work is always available since the amount of audio and video content grows daily.",
        "Flexible hours - pick up assignments when convenient and set your own schedule.",
        "This is perfect for good listeners with attention to detail and patience.",
    ]),
    ("Chapter 9: AI-Powered Virtual Assistant Services", [
        "Virtual assistants handle administrative tasks for busy professionals remotely.",
        "AI tools let you manage email, calendars, travel booking, and research much faster.",
        "Charge $25-50 per hour for AI-enhanced virtual assistant services.",
        "AI handles the routine work while you provide the judgment and personal touch.",
        "Typical tasks: email management, scheduling, data entry, and customer follow-ups.",
        "Platforms like Belay, Time Etc, and Fancy Hands connect you with clients.",
        "Your organizational skills and reliability are exactly what clients value most.",
        "Start with 5-10 hours per week and grow as you become more efficient with AI tools.",
        "AI automates repetitive tasks so you can serve more clients in less time.",
        "Many retirees find this work satisfying because it uses their professional skills.",
        "Build long-term relationships with 2-3 regular clients for stable monthly income.",
    ]),
    ("Chapter 10: Using AI for Stock Photography", [
        "AI helps you identify which types of photos sell well on stock photography sites.",
        "Even smartphone photos can sell if they fill a market need that AI identifies.",
        "Stock photo platforms like Shutterstock and Adobe Stock accept contributor images.",
        "AI editing tools enhance your photos to professional quality automatically.",
        "Popular subjects: food, nature, lifestyle, business settings, and seasonal themes.",
        "Each photo can sell hundreds of times, earning small royalties that add up over time.",
        "AI keywording tools tag your photos correctly so buyers can find them.",
        "You do not need expensive equipment - modern phones take publication-quality images.",
        "AI predicts trending topics so you can photograph what buyers will want next month.",
        "Build a portfolio of 200-500 photos for meaningful passive income.",
        "This is perfect for retirees who enjoy photography as a hobby.",
    ]),
    ("Chapter 11: AI Tutoring and Mentoring", [
        "Your expertise in any subject becomes more valuable when enhanced with AI tools.",
        "AI helps you create lesson plans, quizzes, and practice materials for students.",
        "Online tutoring platforms connect you with students worldwide seeking your knowledge.",
        "Charge $30-75 per hour for tutoring enhanced with AI-generated learning materials.",
        "AI creates personalized practice problems based on each student's weaknesses.",
        "Subjects in demand: math, science, English, test prep, and professional skills.",
        "Your patience and experience combined with AI resources make you an exceptional tutor.",
        "Video tutoring eliminates commuting - teach from your home office or living room.",
        "AI translation helps you tutor international students without language barriers.",
        "Mentoring services for younger professionals leverage your career wisdom directly.",
        "Start by offering free sessions to build reviews, then increase your rates.",
    ]),
    ("Chapter 12: AI Customer Service from Home", [
        "Many companies hire remote customer service representatives who use AI assistance.",
        "AI chatbot management means you oversee conversations the AI handles automatically.",
        "Your job is to step in when AI cannot resolve complex or sensitive issues.",
        "Companies pay $15-30 per hour for experienced customer service with AI skills.",
        "Part-time and flexible schedules are commonly available in this field.",
        "AI provides suggested responses that you review and personalize before sending.",
        "Your life experience helps you understand frustrated customers better than young staff.",
        "Training is usually provided and takes just 1-2 weeks to complete.",
        "Work for companies you already know and love - many offer remote positions.",
        "AI handles the volume; you handle the relationships and difficult conversations.",
        "This suits retirees who enjoy helping people and solving problems.",
    ]),
    ("Chapter 13: Creating Online Courses with AI Help", [
        "Your decades of expertise in any field can be packaged into an online course.",
        "AI helps you outline curriculum, create presentations, and write course scripts.",
        "Platforms like Udemy, Skillshare, and Teachable host your course and find students.",
        "Price courses at $29-199 and earn income every time someone enrolls.",
        "AI video editing tools make your recordings look professional without complex software.",
        "AI generates quizzes, worksheets, and supplementary materials for your students.",
        "Courses about hobbies, career skills, or life transitions sell extremely well.",
        "Record once and sell forever - truly passive income from your knowledge.",
        "AI marketing tools help promote your course to the right audience automatically.",
        "Student feedback helps you improve the course over time with AI-suggested updates.",
        "Start with a short course (1-2 hours) and expand based on student demand.",
    ]),
    ("Chapter 14: AI Bookkeeping for Small Businesses", [
        "AI bookkeeping tools like QuickBooks and FreshBooks automate most accounting tasks.",
        "Small businesses need someone to oversee their AI-managed financial records.",
        "Your role is to review, categorize, and ensure accuracy of AI-processed transactions.",
        "Charge $200-500 per month per client for basic bookkeeping oversight.",
        "AI categorizes expenses, generates invoices, and reconciles bank statements.",
        "Your attention to detail catches errors that AI might miss in unusual transactions.",
        "No accounting degree needed - AI handles the technical rules and calculations.",
        "Tax preparation support during busy season can earn additional income.",
        "Local small businesses prefer working with a trustworthy local bookkeeper.",
        "Serve 5-10 clients for a substantial supplementary income with flexible hours.",
        "This work is especially suitable for retirees with business or finance backgrounds.",
    ]),
    ("Chapter 15: AI-Powered Etsy and Amazon Selling", [
        "AI helps you find profitable products to sell on Etsy and Amazon marketplaces.",
        "Product research AI identifies niches with high demand and low competition.",
        "AI writing tools create compelling product descriptions that convert browsers to buyers.",
        "Print-on-demand products (mugs, shirts, posters) require zero inventory investment.",
        "AI pricing tools automatically adjust your prices to stay competitive.",
        "Keyword optimization AI helps your products appear in search results.",
        "AI customer service tools handle common buyer questions automatically.",
        "Start with a small number of products and let AI data guide your expansion.",
        "Seasonal products (holiday items, graduation gifts) provide predictable income spikes.",
        "AI inventory management prevents running out of stock or over-ordering.",
        "Many retirees build $1000-3000 monthly income from marketplace selling.",
    ]),
    ("Chapter 16: Monetizing AI Skills on Fiverr", [
        "Fiverr lets you sell specific AI-powered services starting at just five dollars.",
        "Popular services: AI writing, image creation, resume editing, and video scripts.",
        "Create service packages at different price points ($5, $25, $50, $100+).",
        "AI tools let you deliver high-quality work fast, maximizing your hourly rate.",
        "Build your reputation with small jobs, then raise prices as reviews accumulate.",
        "Niche services (AI-powered genealogy research, AI pet portraits) stand out from competition.",
        "Fiverr handles payment processing, dispute resolution, and client communication.",
        "Respond quickly to inquiries - Fiverr rewards active and responsive sellers.",
        "AI helps you manage multiple orders simultaneously without feeling overwhelmed.",
        "Top sellers on Fiverr earn $5000-10000 per month, but even part-time earns well.",
        "Start with one service you can do well, then expand your offerings over time.",
    ]),
    ("Chapter 17: AI Real Estate Analysis", [
        "AI tools analyze real estate markets to help investors make better decisions.",
        "You can offer AI-powered market analysis reports to local real estate agents.",
        "AI predicts property values, rental income potential, and neighborhood trends.",
        "Charge $100-500 per analysis report depending on complexity and detail level.",
        "Real estate investors pay well for data-driven insights that reduce their risk.",
        "AI processes public records, sales data, and demographic trends automatically.",
        "Your local knowledge combined with AI data creates uniquely valuable analysis.",
        "Property management companies need AI-assisted reporting on their portfolios.",
        "This work suits retirees with real estate experience or investment knowledge.",
        "AI tools like Zillow, Redfin, and specialized platforms provide raw data to analyze.",
        "Build relationships with 5-10 regular clients for consistent monthly income.",
    ]),
    ("Chapter 18: Tax Implications of AI Side Income", [
        "Side hustle income must be reported on your tax return regardless of amount.",
        "Self-employment tax applies when you earn over $400 per year from freelance work.",
        "Track all expenses: software subscriptions, internet, computer, and home office costs.",
        "AI accounting tools categorize deductions automatically throughout the year.",
        "Quarterly estimated tax payments prevent a large bill at tax time.",
        "Home office deduction applies if you dedicate a space exclusively to your work.",
        "AI tools (ChatGPT, Midjourney, Grammarly subscriptions) are deductible business expenses.",
        "Consider forming an LLC for liability protection once income becomes significant.",
        "AI tax software like TurboTax handles self-employment calculations easily.",
        "Keep records of all income and expenses - AI apps do this automatically.",
        "Consult a tax professional if your side income exceeds $10,000 per year.",
    ]),
    ("Chapter 19: Building Your AI Portfolio", [
        "A portfolio showcases your AI-enhanced work to attract higher-paying clients.",
        "Create a simple website using AI builders like Wix or Squarespace for free.",
        "Include 5-10 examples of your best work in your primary service area.",
        "Client testimonials (even from free initial work) build trust with new prospects.",
        "AI helps you write a compelling About page that highlights your unique experience.",
        "Update your portfolio monthly with new examples as your skills improve.",
        "LinkedIn is essential - AI helps you optimize your profile for client visibility.",
        "Case studies showing results you achieved are more powerful than samples alone.",
        "AI-generated graphics make your portfolio look professional and polished.",
        "Share your portfolio link in all proposals, emails, and social media profiles.",
        "A strong portfolio lets you charge premium rates because clients see proven quality.",
    ]),
    ("Chapter 20: 90-Day Income Launch Plan", [
        "Days 1-7: Choose one AI side hustle from this book that matches your skills and interests.",
        "Days 8-14: Learn the required AI tools. Use free tutorials on YouTube and platform guides.",
        "Days 15-21: Create 3-5 portfolio samples to demonstrate your capability.",
        "Days 22-28: Set up profiles on relevant platforms (Fiverr, Upwork, Etsy, or your website).",
        "Days 29-35: Offer your service for free or at a discount to 3 people for testimonials.",
        "Days 36-50: Begin actively pitching to potential clients or listing products for sale.",
        "Days 51-60: Refine your process based on early feedback and results.",
        "Days 61-75: Raise prices as you build confidence and positive reviews.",
        "Days 76-90: Optimize for efficiency - use AI to do more in less time.",
        "Goal: Earn your first $500 within 90 days. Many retirees achieve this in 60 days.",
        "Remember: consistency beats perfection. Show up daily and the income will follow.",
    ]),
]

for title, lines in chapters:
    doc.new_page()
    doc.add_text(36, 608, title, 'F2', 12)
    doc.add_line(36, 600, 396, 600, 1, 0.4)
    y = 575
    for line in lines:
        doc.add_text(36, y, line, 'F4', 10)
        y -= 22

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book74_AI_Retirement_Income.pdf")
print("Created Book74_AI_Retirement_Income.pdf")
