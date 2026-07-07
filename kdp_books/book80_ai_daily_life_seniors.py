"""Book 80: AI in Daily Life - 50 Ways Seniors Use AI Every Day (Large Print)"""
from pdf_utils import PDFDoc

doc = PDFDoc(612, 792)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.94)
doc.add_centered_text(650, "AI IN DAILY LIFE", 'F2', 28)
doc.add_centered_text(605, "50 Ways Seniors Use", 'F5', 20)
doc.add_centered_text(575, "AI Every Day", 'F5', 20)
doc.add_line(156, 555, 456, 555, 2, 0.3)
doc.add_centered_text(515, "LARGE PRINT EDITION", 'F2', 16)
doc.add_centered_text(480, "Easy-to-Read Guide for", 'F1', 14)
doc.add_centered_text(455, "Everyday Technology", 'F1', 14)
doc.add_centered_text(260, "Daniel Tesfamariam", 'F2', 16)
doc.add_centered_text(230, "2024", 'F1', 13)

# Copyright page
doc.new_page()
doc.add_centered_text(650, "AI IN DAILY LIFE", 'F2', 16)
doc.add_centered_text(620, "50 Ways Seniors Use AI Every Day", 'F4', 13)
doc.add_centered_text(575, "Copyright 2024 Daniel Tesfamariam", 'F1', 12)
doc.add_centered_text(550, "All rights reserved.", 'F1', 12)
doc.add_centered_text(515, "No part of this publication may be reproduced", 'F1', 11)
doc.add_centered_text(495, "without written permission.", 'F1', 11)
doc.add_centered_text(460, "Published independently via KDP.", 'F1', 12)
doc.add_centered_text(425, "Large Print Edition - 13pt font for easy reading", 'F1', 11)

# 50 AI uses, 2 per page = 25 pages
ai_uses = [
    # Morning Routine (1-5)
    ("AI Smart Alarm Clock", [
        "AI alarm clocks learn your sleep cycles and wake you at the lightest sleep phase.",
        "You wake up feeling refreshed instead of groggy because the timing is optimized.",
        "Set up: Use your smartphone's built-in alarm with Smart Wake features enabled.",
        "Most phones have this built in - check Sleep settings in your clock app.",
    ]),
    ("AI Weather Forecasting", [
        "AI weather apps give hour-by-hour predictions so you know when to walk or stay in.",
        "They learn your location and send alerts before rain, extreme heat, or cold arrives.",
        "Set up: Download a weather app and allow location access for personalized forecasts.",
        "Say 'Hey Siri/Alexa, what is the weather today?' for instant voice updates.",
    ]),
    ("AI News Summary", [
        "AI reads hundreds of articles and gives you a quick summary of what matters today.",
        "You choose topics you care about and AI filters out everything else.",
        "Set up: Ask your voice assistant for a news briefing each morning.",
        "Apps like Apple News and Google News use AI to personalize your daily reading.",
    ]),
    ("AI Coffee and Appliance Scheduling", [
        "Smart plugs with AI learn when you wake up and start your coffee automatically.",
        "AI schedules appliances to turn on and off based on your daily routine patterns.",
        "Set up: Buy a smart plug, connect it to WiFi, and set your coffee maker schedule.",
        "Voice command: 'Alexa, start my morning routine' can trigger multiple devices.",
    ]),
    ("AI Morning Health Check", [
        "Smart watches show your overnight health data: heart rate, sleep quality, blood oxygen.",
        "AI analyzes trends and alerts you if something looks different from your normal.",
        "Set up: Wear your smartwatch to sleep and check the health app each morning.",
        "This 30-second check gives you valuable health awareness to start every day.",
    ]),
    # Health (6-10)
    ("AI Medication Reminders", [
        "AI sends customized reminders for each medication at exactly the right time.",
        "It adjusts for time zones when you travel and reminds you about refills too.",
        "Set up: Use your phone's reminder app or a dedicated med reminder like Medisafe.",
        "Voice assistants can also remind you: 'Alexa, remind me to take pills at 8 AM.'",
    ]),
    ("AI Doctor Appointment Booking", [
        "AI scheduling tools find appointment times that work with your routine and energy.",
        "Some systems handle rescheduling and send preparation instructions automatically.",
        "Set up: Check if your doctor's office offers an online portal with scheduling.",
        "AI assistants can add appointments to your calendar and remind you the day before.",
    ]),
    ("AI Exercise Guidance", [
        "AI fitness apps create gentle exercise routines based on your abilities and goals.",
        "They adjust difficulty daily based on how you are feeling and your recent activity.",
        "Set up: Download a fitness app designed for seniors like SilverSneakers GO.",
        "Start with just 5-10 minutes daily and let the AI gradually increase over time.",
    ]),
    ("AI Heart Rate Monitoring", [
        "Smartwatches track your heart rate continuously and alert you to irregularities.",
        "AI detects patterns like AFib that could indicate serious health risks early.",
        "Set up: Enable heart health notifications in your smartwatch settings.",
        "Share your heart data with your doctor at your next appointment for review.",
    ]),
    ("AI Sleep Tracking", [
        "AI monitors your sleep stages, breathing, and movement to improve rest quality.",
        "It suggests optimal bedtimes and identifies factors disrupting your sleep.",
        "Set up: Use your smartwatch's sleep mode or a bedside device like Hatch.",
        "AI sleep reports show trends over weeks helping you and your doctor find solutions.",
    ]),
    # Communication (11-15)
    ("AI Email Writing Assistant", [
        "AI helps you write clear, polished emails by suggesting better wording and fixing errors.",
        "It can draft replies to common messages saving you time and mental effort.",
        "Set up: Gmail has built-in Smart Compose and Smart Reply features activated automatically.",
        "For longer emails, ask ChatGPT to help you draft or revise your message.",
    ]),
    ("AI Video Calling Enhancement", [
        "AI improves video call quality by adjusting lighting, reducing noise, and centering your face.",
        "Background blur hides your room so you do not need to tidy up before calls.",
        "Set up: FaceTime, Zoom, and Google Meet all include these AI features automatically.",
        "Good lighting from a window in front of you plus AI enhancement equals great calls.",
    ]),
    ("AI Social Media Assistance", [
        "AI curates your social media feed to show posts from people you actually care about.",
        "It filters out negative content and highlights updates from family and close friends.",
        "Set up: Mark posts as 'favorites' from people you want to see more frequently.",
        "AI also suggests birthday reminders and helps you comment on family posts.",
    ]),
    ("AI Voice-to-Text Messaging", [
        "AI converts your spoken words into text messages so you never have to type on tiny keys.",
        "It learns your speech patterns and gets more accurate with every message you send.",
        "Set up: Tap the microphone icon on your keyboard and speak your message naturally.",
        "Available in every messaging app on both iPhone and Android devices.",
    ]),
    ("AI Language Translation for Calls", [
        "AI translates your phone conversations in real time when speaking with someone in another language.",
        "This helps you stay connected with family members who speak different languages.",
        "Set up: Google Translate app has a conversation mode for live two-way translation.",
        "AI earbuds can translate speech directly into your ear during in-person conversations.",
    ]),
    # Entertainment (16-20)
    ("AI Music Recommendations", [
        "AI learns the music you love and creates personalized playlists just for you.",
        "It finds new songs similar to your favorites and music from your younger years.",
        "Set up: Use Spotify, Apple Music, or YouTube Music and like songs you enjoy.",
        "Say 'Play music I like' to your smart speaker for an AI-curated listening experience.",
    ]),
    ("AI Audiobook Narration", [
        "AI reads any book aloud in natural-sounding voices so you can listen instead of reading.",
        "Speed adjustment and bookmark features make listening comfortable and convenient.",
        "Set up: Apps like Audible and Libby (free from your library) offer thousands of titles.",
        "AI text-to-speech on your phone can also read articles and emails aloud to you.",
    ]),
    ("AI TV and Movie Recommendations", [
        "AI learns your viewing preferences and suggests shows and movies you will enjoy.",
        "It saves you from scrolling endlessly by offering personalized top picks.",
        "Set up: Rate shows you watch on Netflix, Amazon, or your streaming service.",
        "The more you rate, the better AI understands your taste and improves suggestions.",
    ]),
    ("AI Podcast Discovery", [
        "AI finds podcasts on topics you love and suggests new episodes matched to your interests.",
        "It can speed up or slow down narration and skip ahead through introductions.",
        "Set up: Use Apple Podcasts, Spotify, or Google Podcasts and subscribe to shows you like.",
        "Ask your smart speaker: 'Play a podcast about history' and AI finds one for you.",
    ]),
    ("AI Photo Enhancement", [
        "AI automatically improves your photos by adjusting brightness, contrast, and sharpness.",
        "It removes red eye, smooths lighting, and makes colors more vivid with one tap.",
        "Set up: Open any photo in your phone's gallery and tap Edit or Enhance.",
        "AI works instantly - no photography knowledge needed for professional-looking results.",
    ]),
    # Shopping (21-25)
    ("AI Grocery List Creation", [
        "AI learns your household patterns and suggests grocery items before you run out.",
        "Voice-add to your list anytime: 'Alexa, add milk to my shopping list.'",
        "Set up: Use a shared list app like AnyList or your voice assistant's built-in list.",
        "AI-powered apps can even arrange your list by store aisle for efficient shopping.",
    ]),
    ("AI Gift Recommendations", [
        "AI suggests thoughtful gifts based on the recipient's age, interests, and your budget.",
        "It tracks birthdays and reminds you to shop in advance so you are never caught off guard.",
        "Set up: Ask ChatGPT for gift ideas by describing the person and the occasion.",
        "Amazon's AI recommendations also improve as you browse and purchase over time.",
    ]),
    ("AI Price Comparison Shopping", [
        "AI compares prices across dozens of stores instantly to find you the best deal.",
        "Price tracking AI alerts you when items you want go on sale or drop in price.",
        "Set up: Use browser extensions like Honey or apps like ShopSavvy for automatic comparison.",
        "Save money effortlessly by letting AI find the lowest price before you buy.",
    ]),
    ("AI Grocery Delivery Scheduling", [
        "AI-powered delivery services bring groceries to your door at your preferred time.",
        "Order tracking AI tells you exactly when your delivery will arrive in real time.",
        "Set up: Create an account on Instacart, Walmart Grocery, or Amazon Fresh.",
        "AI remembers your past orders making reordering your regular items quick and easy.",
    ]),
    ("AI Product Reviews Summary", [
        "AI reads hundreds of product reviews and summarizes the key pros and cons for you.",
        "You get the important information without reading dozens of individual opinions.",
        "Set up: Look for AI-generated review summaries on Amazon and other retail sites.",
        "ChatGPT can also summarize reviews if you paste them and ask for key takeaways.",
    ]),
    # Home (26-30)
    ("AI Thermostat Control", [
        "Smart thermostats learn your temperature preferences and adjust automatically.",
        "AI saves money by reducing heating and cooling when you are asleep or away.",
        "Set up: Install a Nest or Ecobee thermostat (or ask a handyman to help).",
        "Voice control: 'Set temperature to 72 degrees' adjusts comfort instantly.",
    ]),
    ("AI Smart Lighting", [
        "AI lights turn on and off automatically based on your daily routine and movement.",
        "They dim gradually at bedtime and brighten slowly in the morning for gentle transitions.",
        "Set up: Replace regular bulbs with smart bulbs and connect them to your WiFi.",
        "Voice control means you never need to walk to a switch in the dark again.",
    ]),
    ("AI Home Security", [
        "AI cameras distinguish between family members, delivery people, animals, and strangers.",
        "You only get alerts for genuine security concerns, not every passing car or squirrel.",
        "Set up: Install a video doorbell like Ring and download the companion app.",
        "AI lets you see and speak with visitors from anywhere through your phone.",
    ]),
    ("AI Robot Vacuum", [
        "Robot vacuums with AI map your home and clean efficiently without getting stuck.",
        "They learn your floor plan, avoid obstacles, and clean on a schedule you set.",
        "Set up: Place the charging station, turn it on, and let it learn your home layout.",
        "Schedule cleaning for when you are out or say 'Alexa, start the vacuum.'",
    ]),
    ("AI Leak and Hazard Detection", [
        "Smart sensors detect water leaks, smoke, and carbon monoxide and alert you immediately.",
        "AI learns normal patterns and only alerts you to genuine hazards, reducing false alarms.",
        "Set up: Place water sensors near washing machines, water heaters, and under sinks.",
        "Alerts go directly to your phone so you know immediately, even when away from home.",
    ]),
    # Finance (31-35)
    ("AI Banking Fraud Detection", [
        "AI monitors your bank accounts and credit cards for suspicious or unusual transactions.",
        "You get instant alerts if someone tries to use your information fraudulently.",
        "Set up: Enable transaction notifications in your banking app's security settings.",
        "AI catches fraud faster than you could by checking statements manually.",
    ]),
    ("AI Bill Payment Automation", [
        "AI schedules and pays bills automatically so you never miss a due date or pay late fees.",
        "It learns your bills, amounts, and timing and handles everything consistently.",
        "Set up: Enroll in autopay through your bank or each billing company's website.",
        "AI budgeting apps track all bills and alert you before any payment occurs.",
    ]),
    ("AI Scam Call Detection", [
        "AI identifies likely scam calls and warns you before you answer or blocks them entirely.",
        "It recognizes patterns used by fraudsters targeting older adults specifically.",
        "Set up: Enable your phone's built-in spam filter in call settings.",
        "Apps like Truecaller and RoboKiller provide additional AI scam protection.",
    ]),
    ("AI Budget Tracking", [
        "AI categorizes your spending automatically and shows exactly where your money goes.",
        "It creates visual charts making it easy to see if spending is on track this month.",
        "Set up: Connect your bank accounts to an app like Mint or your bank's built-in tools.",
        "AI alerts you if spending in any category seems unusually high compared to normal.",
    ]),
    ("AI Tax Preparation Help", [
        "AI tax software guides you through filing step by step with plain language explanations.",
        "It finds deductions you might miss and checks for errors before you submit.",
        "Set up: Use TurboTax, H&R Block, or similar AI-powered tax software at filing time.",
        "AI remembers last year's information so each year filing gets faster and easier.",
    ]),
    # Learning (36-40)
    ("AI Language Learning", [
        "AI apps like Duolingo teach you a new language in bite-sized daily lessons of 5 minutes.",
        "They adapt to your pace, repeat what you forget, and celebrate your progress.",
        "Set up: Download Duolingo (free), choose a language, and complete one lesson daily.",
        "Learning a new language keeps your brain sharp and opens doors to new cultures.",
    ]),
    ("AI Hobby Discovery", [
        "AI suggests new hobbies based on your existing interests, abilities, and available time.",
        "It connects you with online communities, tutorials, and resources for getting started.",
        "Set up: Ask ChatGPT to suggest hobbies based on what you currently enjoy doing.",
        "YouTube's AI also recommends tutorials for creative hobbies you might love.",
    ]),
    ("AI Online Course Recommendations", [
        "AI finds free and paid online courses perfectly matched to what you want to learn.",
        "Courses on everything from painting to astronomy to cooking are available at your pace.",
        "Set up: Browse Coursera, Udemy, or YouTube and AI suggests classes based on interests.",
        "Many library cards provide free access to learning platforms like LinkedIn Learning.",
    ]),
    ("AI Reading Assistant", [
        "AI adjusts text size, spacing, and contrast to make reading comfortable for your eyes.",
        "It can read aloud any text on your screen when your eyes need a rest.",
        "Set up: Enable accessibility settings on your device for larger text and voice reading.",
        "AI summarizes long articles into key points when you do not have time to read everything.",
    ]),
    ("AI Trivia and Brain Games", [
        "AI-powered brain games adapt to your skill level keeping you challenged but not frustrated.",
        "Daily games exercise memory, vocabulary, math, and problem-solving skills.",
        "Set up: Download Lumosity, Wordle, or similar brain training apps for daily practice.",
        "Just 10 minutes per day of brain games helps maintain cognitive sharpness.",
    ]),
    # Safety (41-45)
    ("AI Fall Detection", [
        "Smartwatches detect falls automatically and can call emergency services if you do not respond.",
        "AI learns the difference between a fall and normal quick movements to avoid false alarms.",
        "Set up: Enable fall detection in your Apple Watch or similar smartwatch settings.",
        "This feature works even if you are unconscious and cannot press a button for help.",
    ]),
    ("AI Emergency SOS", [
        "Pressing a button (or automatic detection) sends your location to emergency services and family.",
        "AI transmits your medical information to first responders while help is on the way.",
        "Set up: Configure Emergency SOS on your phone with your emergency contacts and medical ID.",
        "Test the feature (with local dispatch awareness) so you know how it works.",
    ]),
    ("AI Safe Driving Assistance", [
        "AI in modern cars helps with lane keeping, blind spot warnings, and collision avoidance.",
        "Navigation AI finds the safest routes and alerts you to road hazards ahead.",
        "Set up: Use your car's built-in safety features or download a driving safety app.",
        "AI navigation also finds the easiest parking spots and reminds you where you parked.",
    ]),
    ("AI Wandering Prevention", [
        "GPS tracking with AI alerts family if someone with memory issues leaves a safe area.",
        "Geofencing creates invisible boundaries that trigger notifications when crossed.",
        "Set up: Use a GPS tracker (watch, pendant, or shoe clip) with companion app.",
        "AI distinguishes between normal outings and potentially dangerous wandering patterns.",
    ]),
    ("AI Neighborhood Safety Alerts", [
        "AI monitors your neighborhood for safety concerns and sends relevant alerts.",
        "It filters to show only information that actually affects your immediate area.",
        "Set up: Join Nextdoor or enable local alerts on your community's app.",
        "AI helps you make informed decisions about when and where to walk or drive.",
    ]),
    # Planning (46-50)
    ("AI Calendar Management", [
        "AI calendars learn your routine and help schedule appointments at your best energy times.",
        "Conflicts are detected automatically and alternative times are suggested.",
        "Set up: Use Google Calendar or Apple Calendar and add all recurring events.",
        "Voice scheduling: 'Hey Siri, add doctor appointment next Tuesday at 10 AM.'",
    ]),
    ("AI Daily Reminders", [
        "AI sends timely reminders for everything from watering plants to calling a friend.",
        "It learns the best time to remind you based on when you actually complete tasks.",
        "Set up: Use your phone's reminder app or voice assistant for all recurring tasks.",
        "Location-based reminders trigger when you arrive somewhere: remember the milk at the store.",
    ]),
    ("AI To-Do List Prioritization", [
        "AI organizes your tasks by importance and deadline so you always know what to do first.",
        "It breaks large projects into small, manageable steps that feel achievable.",
        "Set up: Use a to-do app like Todoist or Apple Reminders to list your tasks.",
        "AI suggests when to schedule each task based on your available time and energy.",
    ]),
    ("AI Meal Planning", [
        "AI creates weekly meal plans considering your dietary needs, preferences, and what is in stock.",
        "It generates shopping lists and can even suggest simple recipes for leftover ingredients.",
        "Set up: Try a meal planning app like Mealime or ask ChatGPT for a weekly meal plan.",
        "AI reduces the daily stress of deciding what to eat by planning ahead.",
    ]),
    ("AI Daily Routine Automation", [
        "AI coordinates all your smart devices into seamless morning, daytime, and evening routines.",
        "One voice command or scheduled trigger sets off a chain of helpful automated actions.",
        "Set up: Create routines in your Alexa, Google, or Apple Home app linking multiple devices.",
        "Example: 'Good morning' turns on lights, starts coffee, reads weather, and plays news.",
    ]),
]

# 2 AI uses per page = 25 pages
for i in range(0, 50, 2):
    doc.new_page()
    # First AI use
    num1 = i + 1
    title1, lines1 = ai_uses[i]
    doc.add_text(50, 740, f"{num1}. AI Use: {title1}", 'F2', 14)
    doc.add_line(50, 730, 562, 730, 0.5, 0.5)
    y = 705
    for line in lines1:
        doc.add_text(50, y, line, 'F4', 13)
        y -= 28

    # Separator
    doc.add_line(50, y - 10, 562, y - 10, 1, 0.3)

    # Second AI use
    num2 = i + 2
    title2, lines2 = ai_uses[i + 1]
    y -= 40
    doc.add_text(50, y, f"{num2}. AI Use: {title2}", 'F2', 14)
    y -= 12
    doc.add_line(50, y, 562, y, 0.5, 0.5)
    y -= 25
    for line in lines2:
        doc.add_text(50, y, line, 'F4', 13)
        y -= 28

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book80_AI_Daily_Life_Seniors.pdf")
print("Created Book80_AI_Daily_Life_Seniors.pdf")
