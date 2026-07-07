"""Book 71: AI & Healthy Aging - How Technology Can Help You Live Better After 50"""
from pdf_utils import PDFDoc

doc = PDFDoc(432, 648)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 432, 648, 0.95)
doc.add_centered_text(520, "AI & HEALTHY AGING", 'F2', 22)
doc.add_centered_text(490, "How Technology Can Help You", 'F4', 16)
doc.add_centered_text(465, "Live Better After 50", 'F4', 16)
doc.add_line(116, 450, 316, 450, 2, 0.3)
doc.add_centered_text(410, "A Practical Guide to AI-Powered", 'F1', 12)
doc.add_centered_text(390, "Health & Wellness for Older Adults", 'F1', 12)
doc.add_centered_text(200, "Daniel Tesfamariam", 'F2', 14)
doc.add_centered_text(170, "2024", 'F1', 11)

# Copyright page
doc.new_page()
doc.add_centered_text(500, "AI & HEALTHY AGING", 'F2', 14)
doc.add_centered_text(470, "How Technology Can Help You Live Better After 50", 'F4', 10)
doc.add_centered_text(430, "Copyright 2024 Daniel Tesfamariam", 'F1', 10)
doc.add_centered_text(410, "All rights reserved.", 'F1', 10)
doc.add_centered_text(380, "No part of this publication may be reproduced without permission.", 'F1', 9)
doc.add_centered_text(350, "Published independently via KDP.", 'F1', 10)
doc.add_centered_text(320, "For informational purposes only. Not medical advice.", 'F1', 9)

# Chapter content
chapters = [
    ("Chapter 1: How AI Is Revolutionizing Senior Healthcare", [
        "Artificial intelligence is transforming how older adults manage their health.",
        "AI systems can now detect patterns in health data that humans often miss.",
        "From early disease detection to personalized treatment plans, AI helps seniors stay healthier.",
        "Hospitals use AI to reduce wait times and improve diagnosis accuracy for elderly patients.",
        "AI-powered apps can monitor vital signs continuously without requiring doctor visits.",
        "Machine learning algorithms predict health risks before symptoms even appear.",
        "Seniors can now access specialist-level insights from the comfort of their homes.",
        "AI is making preventive care more accessible and affordable for everyone over 50.",
        "The technology adapts to each individual, creating truly personalized health strategies.",
        "This book will show you exactly how to harness these tools for your benefit.",
        "No technical expertise is needed - just a willingness to try something new.",
    ]),
    ("Chapter 2: AI Wearables for Health Monitoring", [
        "Smart watches like Apple Watch and Fitbit use AI to track your health 24/7.",
        "These devices monitor heart rate, blood oxygen, sleep quality, and activity levels.",
        "AI algorithms detect irregular heartbeats (AFib) that could indicate stroke risk.",
        "Fall detection features automatically alert emergency contacts if you take a tumble.",
        "Blood oxygen monitoring helps identify breathing issues while you sleep.",
        "Step counting and exercise tracking motivate you to stay active each day.",
        "Temperature sensors can flag early signs of illness before you feel symptoms.",
        "The AI learns your baseline health patterns and alerts you to any changes.",
        "Many devices now offer ECG capabilities that were once only available in clinics.",
        "Setting up is simple: charge the device, download the app, and wear it daily.",
        "Most health data syncs automatically to share with your doctor at appointments.",
    ]),
    ("Chapter 3: AI Fall Detection Technology", [
        "Falls are the leading cause of injury for adults over 65, but AI can help prevent them.",
        "Smart sensors placed around your home can detect unusual movement patterns.",
        "Wearable devices recognize the motion signature of a fall and call for help automatically.",
        "AI cameras (with privacy settings) can monitor balance and gait changes over time.",
        "Some systems learn your daily routine and alert caregivers if something seems wrong.",
        "Smart flooring with pressure sensors can detect falls even without wearable devices.",
        "AI can analyze your walking pattern to predict fall risk before an incident occurs.",
        "Automatic alerts go to family members or emergency services within seconds of a fall.",
        "These systems work even if you are unconscious or unable to press a button.",
        "Many systems are covered by Medicare or supplemental insurance plans.",
        "Installation is typically simple and non-invasive for most home environments.",
    ]),
    ("Chapter 4: AI Medication Reminders and Management", [
        "Managing multiple medications is challenging, but AI makes it much easier.",
        "Smart pill dispensers release the right medication at the right time automatically.",
        "AI apps send reminders to your phone, smartwatch, or smart speaker when it is time.",
        "Some systems photograph each pill to verify you are taking the correct medication.",
        "AI can flag dangerous drug interactions that even pharmacists might overlook.",
        "Automatic refill alerts ensure you never run out of essential medications.",
        "Voice assistants like Alexa can remind you verbally throughout the day.",
        "AI tracks your adherence patterns and adjusts reminder timing for better compliance.",
        "Caregivers receive notifications if a dose is missed, enabling remote monitoring.",
        "Many smart dispensers lock to prevent accidental double-dosing.",
        "These tools reduce medication errors by up to 90 percent in clinical studies.",
    ]),
    ("Chapter 5: AI-Powered Telehealth Explained", [
        "Telehealth lets you see a doctor from home, and AI makes it even more effective.",
        "AI symptom checkers help you describe your issues clearly before the appointment.",
        "During video visits, AI can analyze your skin, eyes, and breathing patterns.",
        "AI transcribes your appointment so you do not forget important instructions.",
        "After the visit, AI sends personalized follow-up reminders and care instructions.",
        "Many telehealth platforms now offer 24/7 AI triage for non-emergency questions.",
        "AI helps match you with the right specialist based on your symptoms and history.",
        "Virtual waiting rooms use AI to estimate actual wait times accurately.",
        "AI-powered translation makes telehealth accessible in any language.",
        "Most Medicare plans now cover telehealth visits, making them free or low-cost.",
        "Setting up telehealth requires just a smartphone, tablet, or computer with a camera.",
    ]),
    ("Chapter 6: Voice AI for Daily Health Check-Ins", [
        "Smart speakers can conduct daily health check-ins using just your voice.",
        "Simply say good morning and answer a few questions about how you are feeling.",
        "AI voice analysis can detect changes in mood, cognition, and even respiratory health.",
        "These check-ins take less than two minutes but provide valuable trend data over time.",
        "If the AI detects concerning changes, it can alert your doctor or family members.",
        "Voice AI remembers your medications, allergies, and health history for context.",
        "You can ask health questions anytime and get evidence-based answers instantly.",
        "Daily check-ins help track chronic conditions like diabetes or heart disease.",
        "The AI learns your voice patterns and becomes more accurate over time.",
        "No typing, no screens needed - just natural conversation with your device.",
        "Popular options include Amazon Alexa health skills and Google Health routines.",
    ]),
    ("Chapter 7: AI Nutrition Apps for Seniors", [
        "AI nutrition apps create personalized meal plans based on your health needs.",
        "Simply photograph your meal and the AI identifies foods and calculates nutrition.",
        "Apps adjust recommendations for conditions like diabetes, heart disease, or arthritis.",
        "AI considers your medications when suggesting foods to avoid dangerous interactions.",
        "Grocery list generators create shopping lists based on your weekly meal plan.",
        "Recipe modifications make favorite dishes healthier without sacrificing taste.",
        "AI tracks hydration and reminds you to drink water throughout the day.",
        "Some apps connect with your wearable to adjust calorie needs based on activity.",
        "Voice-controlled features let you log meals without typing or complex navigation.",
        "AI learns your food preferences over time and suggests meals you will actually enjoy.",
        "Many apps offer large-print modes and simplified interfaces for easier reading.",
    ]),
    ("Chapter 8: AI Exercise Programs for Aging Bodies", [
        "AI fitness apps create exercise routines specifically designed for older bodies.",
        "Programs adapt automatically based on your mobility, pain levels, and energy.",
        "AI watches your form through your phone camera and corrects movements in real time.",
        "Low-impact exercises are prioritized to protect joints while building strength.",
        "Balance-focused routines help prevent falls with progressively harder challenges.",
        "AI adjusts intensity based on your heart rate data from connected wearables.",
        "Chair exercises and seated routines are available for those with limited mobility.",
        "Progress tracking shows improvements in strength, flexibility, and endurance.",
        "AI sends motivation and reminders at optimal times based on your energy patterns.",
        "Many programs include guided stretching for morning stiffness and joint pain.",
        "Social features let you exercise virtually with friends for accountability.",
    ]),
    ("Chapter 9: AI Mental Health Tools", [
        "AI-powered apps help track mood patterns and identify triggers for anxiety or depression.",
        "Daily mood logging takes seconds but reveals important patterns over weeks and months.",
        "AI chatbots offer cognitive behavioral therapy techniques available 24/7.",
        "Guided meditation and breathing exercises are personalized to your stress levels.",
        "AI detects subtle language changes that may indicate worsening mental health.",
        "Sleep tracking integration helps connect rest quality with emotional well-being.",
        "Gratitude journaling prompts are generated based on what resonates with you personally.",
        "AI can suggest when professional help might be beneficial based on your patterns.",
        "Social connection reminders help combat isolation that affects mental health.",
        "Many apps offer free versions that provide substantial support without cost.",
        "Privacy-focused designs ensure your mental health data remains confidential.",
    ]),
    ("Chapter 10: AI for Managing Chronic Conditions", [
        "AI excels at managing ongoing health conditions like diabetes, COPD, and hypertension.",
        "Continuous glucose monitors with AI predict blood sugar trends hours in advance.",
        "AI blood pressure apps help identify patterns and triggers for high readings.",
        "Asthma and COPD patients benefit from AI air quality alerts and breathing coaches.",
        "Arthritis management apps use AI to correlate flare-ups with weather and activity.",
        "AI pain tracking helps doctors understand your condition between appointments.",
        "Heart failure patients benefit from AI weight and fluid monitoring at home.",
        "AI medication optimization suggests timing adjustments for better symptom control.",
        "Remote patient monitoring sends data directly to your healthcare team automatically.",
        "AI identifies when a condition is worsening before you notice symptoms yourself.",
        "These tools reduce emergency room visits by catching problems early.",
    ]),
    ("Chapter 11: AI Hearing Aids and Vision Tools", [
        "Modern hearing aids use AI to adapt to different environments automatically.",
        "AI separates speech from background noise, making conversations clearer in crowds.",
        "Smart glasses with AI can read text aloud, recognize faces, and describe scenes.",
        "AI-powered magnification apps turn your phone into a powerful reading aid.",
        "Hearing aid AI learns your preferences for different locations over time.",
        "Real-time captioning AI displays what people say as text on your phone.",
        "AI can translate foreign languages through your hearing aids in real time.",
        "Vision AI helps identify medications, read mail, and navigate unfamiliar spaces.",
        "Tinnitus management uses AI-generated sound therapy customized to your frequencies.",
        "Many AI hearing solutions cost a fraction of traditional hearing aids.",
        "Setup assistance is available through most audiology offices or online support.",
    ]),
    ("Chapter 12: AI Sleep Tracking for Better Rest", [
        "AI sleep trackers analyze your sleep stages, breathing, and movement all night.",
        "Smart mattress pads detect restlessness and automatically adjust temperature.",
        "AI identifies patterns that disrupt your sleep, like caffeine timing or screen use.",
        "Personalized sleep coaching suggests optimal bedtimes based on your circadian rhythm.",
        "Snoring detection with AI can identify potential sleep apnea for medical follow-up.",
        "Smart alarm features wake you during light sleep so you feel more refreshed.",
        "AI correlates sleep quality with daytime energy, mood, and cognitive performance.",
        "White noise and soundscapes are generated by AI based on what helps you most.",
        "Sleep reports can be shared with your doctor to discuss insomnia treatments.",
        "Medication timing suggestions help avoid drugs that interfere with sleep.",
        "Most trackers work passively - just place them near your bed and they do the rest.",
    ]),
    ("Chapter 13: Robot Companions for Elderly", [
        "Social robots like ElliQ and Jibo provide companionship and reduce loneliness.",
        "These AI companions initiate conversations, tell jokes, and share interesting facts.",
        "Robot pets (like Joy for All cats and dogs) provide comfort without care demands.",
        "AI companions remind you of appointments, medications, and important dates.",
        "Some robots facilitate video calls with family, making connection effortless.",
        "AI learns your interests and suggests activities, music, and conversation topics.",
        "Companion robots can detect changes in routine that might indicate health issues.",
        "They encourage physical activity with gentle suggestions and movement games.",
        "Many robots are designed to be non-intimidating with friendly faces and voices.",
        "Research shows robot companions measurably reduce depression and anxiety in seniors.",
        "Costs range from affordable robot pets to more advanced interactive companions.",
    ]),
    ("Chapter 14: AI-Powered Emergency Alerts", [
        "Medical alert systems with AI go far beyond the traditional help button pendant.",
        "AI detects falls, unusual inactivity, and changes in daily patterns automatically.",
        "Smart home sensors know if you have not opened the refrigerator or left bed all day.",
        "GPS-enabled devices track location if you become lost or disoriented outdoors.",
        "AI triages the situation to determine if emergency services or family should be called.",
        "Voice-activated alerts work even when you cannot reach a button or phone.",
        "AI can communicate your medical history to first responders en route to help you.",
        "Two-way communication lets you speak with operators without holding a phone.",
        "Battery life on modern devices lasts days or weeks without charging.",
        "Waterproof designs mean protection even in the shower where many falls occur.",
        "Monthly monitoring costs have decreased significantly with AI automation.",
    ]),
    ("Chapter 15: Smart Home AI for Aging in Place", [
        "Smart home technology helps you stay independent in your own home longer.",
        "Voice-controlled lights, thermostats, and locks eliminate the need to reach switches.",
        "AI learns your daily schedule and automates routines like morning lights and coffee.",
        "Smart door locks let family members check that your home is secure remotely.",
        "AI-powered cameras can detect unusual activity while respecting your privacy.",
        "Automated blinds and curtains adjust throughout the day without physical effort.",
        "Smart stove monitors turn off burners if left unattended for too long.",
        "Water leak sensors alert you immediately to prevent damage and mold.",
        "AI manages heating and cooling for comfort while reducing energy bills.",
        "Video doorbells let you see and speak with visitors without going to the door.",
        "Most smart home devices work together and can be controlled with simple voice commands.",
    ]),
    ("Chapter 16: AI for Managing Doctor Appointments", [
        "AI scheduling tools find appointment times that work with your routine and energy levels.",
        "Virtual assistants prepare questions to ask your doctor before each visit.",
        "AI summarizes your recent health data into a concise report for your physician.",
        "Appointment reminders include preparation instructions like fasting requirements.",
        "After visits, AI helps you understand and remember what the doctor recommended.",
        "Medication changes are tracked and explained in simple, clear language.",
        "AI coordinates between multiple specialists to avoid scheduling conflicts.",
        "Transportation booking through AI ensures you have a ride to every appointment.",
        "Follow-up task reminders ensure you complete labs, imaging, or referrals on time.",
        "AI can identify if you are due for preventive screenings like colonoscopies or mammograms.",
        "Digital health records accessible through AI make switching doctors much easier.",
    ]),
    ("Chapter 17: AI Brain Training Apps", [
        "Brain training apps use AI to create personalized cognitive exercise programs.",
        "Games adapt difficulty in real time to keep you challenged but not frustrated.",
        "AI tracks improvements in memory, attention, processing speed, and problem-solving.",
        "Daily sessions of just 10-15 minutes show measurable cognitive benefits over time.",
        "Apps like Lumosity, Elevate, and Peak use neuroscience-backed AI algorithms.",
        "Word games, math puzzles, and pattern recognition exercises strengthen different skills.",
        "AI identifies your weakest cognitive areas and focuses training where you need it most.",
        "Progress reports show how you compare to others your age and your own past performance.",
        "Social features let you compete with friends, adding motivation and fun.",
        "Reminder notifications ensure you maintain a consistent training schedule.",
        "Many apps offer free basic versions with optional premium upgrades.",
    ]),
    ("Chapter 18: AI and Loneliness Prevention", [
        "Social isolation affects one in four adults over 65, but AI offers new solutions.",
        "AI-powered platforms match seniors with similar interests for virtual meetups.",
        "Chatbots provide daily conversation when human interaction is not available.",
        "AI detects signs of isolation by monitoring communication patterns and activity.",
        "Virtual community spaces use AI to facilitate group discussions and shared activities.",
        "AI-powered calling services provide regular check-in calls with trained volunteers.",
        "Interest-based AI matching connects you with others who share your hobbies.",
        "AI translation removes language barriers from international friendships.",
        "Video calling AI enhances connections by improving audio and video quality.",
        "AI suggests local events, classes, and groups based on your interests and abilities.",
        "Regular social interaction tracked by AI helps maintain cognitive health.",
    ]),
    ("Chapter 19: Future of AI in Senior Care", [
        "AI technology for seniors is advancing rapidly with exciting innovations ahead.",
        "Diagnostic AI will become more accurate than human doctors for many conditions.",
        "Robot assistants will help with physical tasks like cooking and cleaning.",
        "AI-powered exoskeletons may restore mobility for those with physical limitations.",
        "Personalized medicine using AI will tailor treatments to your unique genetics.",
        "Virtual reality therapy will treat pain, anxiety, and cognitive decline.",
        "AI-powered autonomous vehicles will restore transportation independence.",
        "Brain-computer interfaces may help those with severe communication challenges.",
        "Predictive AI will identify health problems years before they develop.",
        "Home care robots will provide round-the-clock assistance affordably.",
        "The goal is always the same: more independence, better health, greater joy.",
    ]),
    ("Chapter 20: Getting Started Checklist", [
        "Start with just one AI tool - do not try to adopt everything at once.",
        "Choose a health-related goal: better sleep, more exercise, or medication management.",
        "Get a basic smartwatch or fitness tracker as your entry point to AI health tools.",
        "Set up a voice assistant (Alexa, Google, or Siri) in your main living space.",
        "Download one health app and use it daily for two weeks before adding more.",
        "Ask a family member or friend to help with initial setup if technology feels overwhelming.",
        "Schedule a telehealth appointment to experience virtual healthcare firsthand.",
        "Join an online community for seniors exploring technology to share tips and encouragement.",
        "Set realistic expectations - AI is a tool to help, not a replacement for human care.",
        "Review your progress monthly and add new tools as you become more comfortable.",
        "Remember: every expert was once a beginner. You can do this at your own pace.",
    ]),
]

for title, lines in chapters:
    doc.new_page()
    doc.add_text(40, 608, title, 'F2', 13)
    doc.add_line(40, 600, 392, 600, 1, 0.4)
    y = 575
    for line in lines:
        doc.add_text(40, y, line, 'F4', 10.5)
        y -= 22

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book71_AI_Health_Guide_Aging.pdf")
print("Created Book71_AI_Health_Guide_Aging.pdf")
