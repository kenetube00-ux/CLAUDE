from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "100 CHATGPT PROMPTS FOR EVERYDAY LIFE"
subtitle = "A Guide for Adults 50+"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 16)
pdf.add_centered_text(515, subtitle, 'F4', 14)
pdf.add_centered_text(440, "Simple, Practical Prompts You Can Copy and Paste", 'F4', 11)
pdf.add_centered_text(420, "No Tech Experience Needed", 'F4', 11)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 11)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: How to Use ChatGPT Intro
pdf.new_page()
pdf.add_centered_text(750, "HOW TO USE CHATGPT", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
intro = [
    "WHAT IS CHATGPT?",
    "ChatGPT is a free AI assistant you can talk to by typing. Think of",
    "it like texting a very knowledgeable friend who is available 24/7.",
    "",
    "HOW TO GET STARTED:",
    "1. Go to chat.openai.com on your computer or phone",
    "2. Create a free account (just need an email address)",
    "3. You will see a text box - that is where you type your 'prompt'",
    "4. Type your question or request and press Enter",
    "5. ChatGPT will respond in seconds!",
    "",
    "TIPS FOR BEST RESULTS:",
    "- Be specific: 'Give me a recipe for chicken soup' works better",
    "  than just 'food ideas'",
    "- Give context: 'I have diabetes' helps it tailor health advice",
    "- Ask follow-ups: Say 'Make it simpler' or 'Give me more detail'",
    "- It is a conversation: You can keep asking questions",
    "- Copy and paste: You can copy prompts from this book directly",
    "",
    "IMPORTANT REMINDERS:",
    "- ChatGPT can make mistakes - always verify important information",
    "- Never share passwords, Social Security numbers, or bank info",
    "- It is not a doctor - use health info as a starting point only",
    "- It cannot access the internet in real-time (no current news)",
    "- You can start a new conversation anytime",
    "",
    "HOW TO USE THIS BOOK:",
    "Each prompt is written in BOLD - type it exactly as shown.",
    "'Why this helps' explains what you will get back.",
    "'My result' space is for you to write notes about what worked."
]
for line in intro:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Pages 4-28: 25 pages with 4 prompts each = 100 prompts
all_prompts = [
    # HEALTH (10)
    ("Health", "Explain what my cholesterol numbers mean in simple terms. My total is 220, HDL is 45, LDL is 150, triglycerides are 180.", "Helps you understand lab results before your doctor visit."),
    ("Health", "I take metformin and lisinopril. What foods should I avoid and why?", "Alerts you to food-drug interactions to discuss with your pharmacist."),
    ("Health", "Create a gentle 20-minute morning exercise routine for a 65-year-old with bad knees.", "Gives you safe exercises tailored to your limitations."),
    ("Health", "What questions should I ask my doctor about my upcoming knee replacement surgery?", "Helps you prepare for appointments so you do not forget important questions."),
    ("Health", "Explain the difference between a stroke and a heart attack. What are the warning signs of each?", "Helps you recognize emergencies and act fast."),
    ("Health", "I was just diagnosed with Type 2 diabetes. Explain it to me like I am new to this and scared.", "Gives you a compassionate, easy-to-understand overview."),
    ("Health", "What are 10 ways to lower blood pressure naturally without medication?", "Gives you lifestyle changes to discuss with your doctor."),
    ("Health", "I have trouble sleeping. Give me a step-by-step bedtime routine for better sleep.", "Provides evidence-based sleep hygiene tips."),
    ("Health", "Create a weekly meal plan for someone trying to lower cholesterol. Simple recipes only.", "Gives you a heart-healthy eating plan with easy meals."),
    ("Health", "What supplements are recommended for women over 60? What does each one do?", "Helps you understand common supplements before asking your doctor."),
    # COOKING (10)
    ("Cooking", "Give me 5 easy dinner recipes using only ingredients I can find at any grocery store. I cook for two people.", "Simple weeknight meals without specialty ingredients."),
    ("Cooking", "I have chicken, rice, and broccoli. What can I make? Give me 3 different recipes.", "Uses what you already have - no extra shopping needed."),
    ("Cooking", "Convert this recipe to a slow cooker version: [paste any recipe]. How long should I cook it?", "Turns any recipe into an easy set-and-forget meal."),
    ("Cooking", "I need to cook for my grandkids ages 4-10. Give me 5 healthy meals kids actually like.", "Kid-friendly meals that are still nutritious."),
    ("Cooking", "Create a grocery list for one week of anti-inflammatory meals for two people.", "Organized shopping list for a specific health goal."),
    ("Cooking", "I am hosting Thanksgiving for 12 people. Create a timeline for cooking everything so it is all ready at 3pm.", "Step-by-step cooking schedule so nothing burns or is late."),
    ("Cooking", "What can I substitute for eggs in baking? I have an egg allergy.", "Gives you multiple substitution options with amounts."),
    ("Cooking", "Give me 10 healthy snack ideas that do not require cooking and are good for diabetics.", "Quick grab-and-go options that will not spike blood sugar."),
    ("Cooking", "I just got an Instant Pot. Give me 5 beginner recipes with exact step-by-step instructions.", "Easy starter recipes for new kitchen gadgets."),
    ("Cooking", "Create a freezer meal plan. Give me 10 meals I can prep on Sunday and freeze for the month.", "Batch cooking to save time and energy."),
    # TRAVEL (10)
    ("Travel", "I am a 60-year-old traveling solo for the first time. Give me safety tips and a packing checklist.", "Confidence-building advice for independent travel."),
    ("Travel", "Plan a 7-day road trip from Chicago to the Grand Canyon. Include stops, hotels budget, and things to see.", "Complete trip itinerary without hours of research."),
    ("Travel", "What are the best travel insurance options for seniors? What should the policy include?", "Helps you compare coverage before you buy."),
    ("Travel", "I want to visit my grandkids in another state. Help me find the cheapest way to fly. What days and times are cheapest?", "Money-saving flight booking strategies."),
    ("Travel", "Create a packing list for a 10-day cruise. Include formal nights and shore excursions.", "Comprehensive list so you do not forget anything."),
    ("Travel", "I have mobility issues. Suggest 5 vacation destinations that are wheelchair accessible and beautiful.", "Travel options that accommodate physical limitations."),
    ("Travel", "Write an email to a hotel asking about accessibility, early check-in, and room location preferences.", "Professional communication you can copy and send."),
    ("Travel", "What documents do I need to travel internationally? I have not left the country in 20 years.", "Updated travel requirement checklist."),
    ("Travel", "Suggest 5 all-inclusive resorts for a couple in their 60s who want relaxation, not partying.", "Age-appropriate vacation recommendations."),
    ("Travel", "Help me create a road trip budget. We are driving 2000 miles over 5 days with 2 people.", "Realistic cost breakdown for planning."),
    # FAMILY (10)
    ("Family", "Help me write a letter to my adult child who I have a strained relationship with.", "Gives you a thoughtful starting point for reconciliation."),
    ("Family", "I am helping raise my grandchildren. Give me tips for setting boundaries with their parents.", "Practical guidance for a complex family situation."),
    ("Family", "Write a birthday message for my 5-year-old granddaughter that I can put in a card.", "Sweet, age-appropriate messages when words do not come easily."),
    ("Family", "My spouse was just diagnosed with dementia. What should I expect and how can I prepare?", "Compassionate overview of what lies ahead."),
    ("Family", "Help me plan a family reunion for 30 people. Include activities for all ages.", "Organized event plan covering logistics and fun."),
    ("Family", "I want to write my life story for my grandchildren. Give me 20 prompts to get started.", "Memoir-writing prompts to preserve your legacy."),
    ("Family", "My teenager is being bullied. How should I handle this as a grandparent?", "Guidance on supporting without overstepping."),
    ("Family", "Write a prayer I can say at our family dinner gathering.", "A heartfelt blessing you can personalize."),
    ("Family", "Help me create a family tree template. What information should I collect from relatives?", "Genealogy project structure to get started."),
    ("Family", "My aging parent needs more help. How do I start the conversation about assisted living?", "Sensitive conversation starters for a difficult topic."),
    # MONEY (10)
    ("Money", "Explain Social Security benefits to me. When should I start collecting and why?", "Plain-language explanation of a complex decision."),
    ("Money", "I am retiring next year. Create a monthly budget template for living on a fixed income.", "Financial planning tool for retirement."),
    ("Money", "What are the safest investments for someone over 60 who cannot afford to lose money?", "Conservative investment overview to discuss with advisor."),
    ("Money", "Help me write a letter disputing a charge on my credit card statement.", "Professional dispute letter you can send as-is."),
    ("Money", "Explain Medicare Parts A, B, C, and D. What does each cover?", "Clear breakdown of confusing healthcare coverage."),
    ("Money", "I think I am being scammed. They called saying my Social Security was compromised. What should I do?", "Immediate steps to protect yourself from fraud."),
    ("Money", "Create a list of all the bills and subscriptions I should review to save money each month.", "Identifies hidden expenses you may have forgotten."),
    ("Money", "What tax deductions are available for retirees? I want to lower my tax bill.", "Tax-saving strategies to discuss with your accountant."),
    ("Money", "Help me understand my pension options: lump sum vs monthly payments. What factors matter?", "Decision framework for a major financial choice."),
    ("Money", "I want to leave money to my grandchildren for college. What are the best options?", "Education savings overview (529 plans, trusts, etc)."),
    # HOME (10)
    ("Home", "My bathroom faucet is dripping. Give me step-by-step instructions to fix it myself.", "DIY repair guide that can save you a plumber visit."),
    ("Home", "Create a seasonal home maintenance checklist organized by month.", "Prevents costly repairs by catching issues early."),
    ("Home", "I want to downsize from a 4-bedroom house. Give me a room-by-room decluttering plan.", "Manageable approach to an overwhelming task."),
    ("Home", "What smart home devices would make life easier for a senior living alone?", "Technology recommendations for safety and convenience."),
    ("Home", "Help me write a listing description to sell my home. 3 bed, 2 bath, large yard, quiet neighborhood.", "Professional real estate copy without an agent."),
    ("Home", "I am hiring a contractor to redo my kitchen. What questions should I ask before signing a contract?", "Protects you from common renovation problems."),
    ("Home", "Create an emergency preparedness kit list for a retired couple.", "Comprehensive disaster readiness checklist."),
    ("Home", "What plants are easy to grow indoors with low light? I want to brighten my apartment.", "Low-maintenance houseplant recommendations."),
    ("Home", "I just moved to a new town. How can I meet people and make friends at age 65?", "Practical community connection strategies."),
    ("Home", "Help me organize my important documents. What papers do I need and where should I keep them?", "Filing system for wills, insurance, medical records, etc."),
    # HOBBIES (10)
    ("Hobbies", "I want to start painting but have never held a brush. Give me a complete beginner guide.", "Step-by-step hobby introduction with supply list."),
    ("Hobbies", "Suggest 10 hobbies for someone with arthritis in their hands. I need gentle activities.", "Activity ideas that accommodate physical limitations."),
    ("Hobbies", "I am starting a vegetable garden. What should I plant this month in zone 7?", "Seasonal gardening advice for your specific location."),
    ("Hobbies", "Give me a list of 20 books for someone who loves historical fiction and mystery.", "Personalized reading recommendations."),
    ("Hobbies", "I want to learn guitar at age 62. Is it too late? Give me a 30-day beginner plan.", "Encouraging learning plan proving it is never too late."),
    ("Hobbies", "Help me start a blog about my retirement adventures. What platform and steps?", "Technical guide in simple language."),
    ("Hobbies", "I collect coins. Help me catalog my collection and estimate values.", "Organizing framework for your collection."),
    ("Hobbies", "Create a photography challenge for beginners. 30 days of simple photo prompts.", "Daily creative inspiration with no fancy equipment needed."),
    ("Hobbies", "I want to volunteer but do not know where to start. Suggest options for a retired teacher.", "Meaningful volunteer opportunities matched to your skills."),
    ("Hobbies", "Teach me basic bird watching. What equipment do I need and how do I identify birds?", "Nature hobby introduction with practical tips."),
    # WRITING (10)
    ("Writing", "Help me write a thank-you note for the nurse who took great care of me in the hospital.", "Heartfelt gratitude expressed professionally."),
    ("Writing", "I want to write a eulogy for my mother. Help me with an outline and some opening lines.", "Compassionate structure for a difficult task."),
    ("Writing", "Write a complaint letter to my internet company about poor service. Be firm but polite.", "Effective consumer advocacy letter."),
    ("Writing", "Help me write my obituary in advance so my family does not have to do it during grief.", "Practical pre-planning that eases future burden."),
    ("Writing", "Create a template for a holiday newsletter to send to friends and family.", "Annual update format that is warm and interesting."),
    ("Writing", "Help me write a review for the restaurant where we had our anniversary dinner.", "Well-written review supporting a local business."),
    ("Writing", "I need to write a letter to my congressman about [issue]. Help me be persuasive.", "Civic engagement template for making your voice heard."),
    ("Writing", "Help me update my resume. I am 63 and looking for part-time work after retirement.", "Age-appropriate resume for the modern job market."),
    ("Writing", "Write an email to my doctor asking about switching medications due to side effects.", "Clear medical communication that gets results."),
    ("Writing", "Help me write a heartfelt wedding toast for my granddaughter.", "Memorable speech that balances humor and love."),
    # LEARNING (10)
    ("Learning", "Explain how to use Zoom for video calls. Step by step, assume I know nothing.", "Technology tutorial in plain language."),
    ("Learning", "I want to understand the stock market. Explain it like I am brand new to investing.", "Financial literacy without the jargon."),
    ("Learning", "Teach me how to spot fake news and misinformation online.", "Critical thinking skills for the digital age."),
    ("Learning", "Explain climate change in simple terms. What is actually happening and what can I do?", "Clear science explanation without political spin."),
    ("Learning", "I want to learn Spanish. Create a 30-day plan for an absolute beginner.", "Structured language learning you can do at home."),
    ("Learning", "How does my smartphone work? Explain the basics of apps, settings, and storage.", "Tech literacy for your everyday device."),
    ("Learning", "Explain artificial intelligence in simple terms. Should I be worried about it?", "Balanced, non-scary overview of AI."),
    ("Learning", "Teach me how to use online banking safely. What are the security steps?", "Digital finance confidence with safety focus."),
    ("Learning", "What are podcasts and how do I listen to them? Suggest 5 for someone over 50.", "New media introduction with recommendations."),
    ("Learning", "I want to understand my grandkids better. Explain their generation's culture to me.", "Bridge the generational gap with understanding."),
    # DAILY LIFE (10)
    ("Daily Life", "Create a morning routine for a retired person that gives structure without stress.", "Healthy daily habits for purposeful retirement."),
    ("Daily Life", "I am lonely since my spouse passed. Give me 10 practical ideas to feel less isolated.", "Compassionate action steps for a difficult time."),
    ("Daily Life", "Help me set up an automated pill reminder system. I keep forgetting my medications.", "Practical solution for medication adherence."),
    ("Daily Life", "I have too many passwords. Explain how to manage them safely and simply.", "Digital security without the overwhelm."),
    ("Daily Life", "My energy is low in the afternoon. What are natural ways to boost energy after 60?", "Health-conscious energy solutions."),
    ("Daily Life", "Help me write a daily schedule that includes exercise, social time, and purpose.", "Balanced retirement day structure."),
    ("Daily Life", "I am moving closer to my children. Create a moving checklist organized by weeks.", "Stress-reducing relocation plan."),
    ("Daily Life", "What are the best apps for seniors? Suggest ones for health, social, brain games, and safety.", "Curated technology recommendations."),
    ("Daily Life", "Help me plan my week. I have 3 doctor appointments, grocery shopping, and my book club.", "Weekly planning assistance for busy schedules."),
    ("Daily Life", "I want to create an advance directive and living will. What decisions do I need to make?", "End-of-life planning guidance for peace of mind."),
]

# 25 pages, 4 prompts per page
for page_idx in range(25):
    pdf.new_page()
    page_prompts = all_prompts[page_idx * 4 : (page_idx + 1) * 4]
    # Determine category for page header
    category = page_prompts[0][0]
    pdf.add_text(50, 755, f"CATEGORY: {category.upper()}", 'F2', 10)
    pdf.add_line(50, 747, 562, 747)
    y = 730
    for prompt_idx, (cat, prompt_text, why_helps) in enumerate(page_prompts):
        prompt_num = page_idx * 4 + prompt_idx + 1
        pdf.add_text(50, y, f"PROMPT #{prompt_num}", 'F2', 9)
        y -= 14
        # Wrap prompt text in bold
        remaining = prompt_text
        while len(remaining) > 72:
            split = remaining[:72].rfind(' ')
            if split == -1:
                split = 72
            pdf.add_text(55, y, remaining[:split], 'F2', 9)
            remaining = remaining[split+1:]
            y -= 12
        pdf.add_text(55, y, remaining, 'F2', 9)
        y -= 14
        pdf.add_text(55, y, f"Why this helps: {why_helps}", 'F4', 8)
        y -= 14
        pdf.add_text(55, y, "My result:", 'F1', 8)
        pdf.add_line(100, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 12
        pdf.add_line(55, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 18

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book132_ChatGPT_Prompt_Guide_Seniors.pdf')
print("Book132_ChatGPT_Prompt_Guide_Seniors.pdf created successfully!")
