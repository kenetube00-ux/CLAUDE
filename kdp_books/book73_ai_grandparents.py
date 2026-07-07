"""Book 73: The Grandparent's Guide to AI - Stay Connected & Relevant in a Digital World"""
from pdf_utils import PDFDoc

doc = PDFDoc(432, 648)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 432, 648, 0.94)
doc.add_centered_text(530, "THE GRANDPARENT'S", 'F2', 20)
doc.add_centered_text(500, "GUIDE TO AI", 'F2', 20)
doc.add_centered_text(460, "Stay Connected & Relevant", 'F5', 14)
doc.add_centered_text(438, "in a Digital World", 'F5', 14)
doc.add_line(100, 420, 332, 420, 2, 0.3)
doc.add_centered_text(380, "Bridge the Generation Gap", 'F1', 12)
doc.add_centered_text(358, "with Technology", 'F1', 12)
doc.add_centered_text(200, "Daniel Tesfamariam", 'F2', 14)
doc.add_centered_text(175, "2024", 'F1', 11)

# Copyright page
doc.new_page()
doc.add_centered_text(500, "THE GRANDPARENT'S GUIDE TO AI", 'F2', 13)
doc.add_centered_text(475, "Stay Connected & Relevant in a Digital World", 'F4', 10)
doc.add_centered_text(440, "Copyright 2024 Daniel Tesfamariam", 'F1', 10)
doc.add_centered_text(420, "All rights reserved.", 'F1', 10)
doc.add_centered_text(390, "No part of this publication may be reproduced without permission.", 'F1', 9)
doc.add_centered_text(360, "Published independently via KDP.", 'F1', 10)

chapters = [
    ("Chapter 1: Why AI Matters for Grandparents", [
        "Your grandchildren are growing up in a world where AI is as common as electricity.",
        "Understanding AI helps you connect with younger generations on their level.",
        "AI is not about replacing human relationships - it is about enhancing them.",
        "Grandparents who use technology stay more connected with far-away family members.",
        "AI tools can make your daily life easier, safer, and more enjoyable.",
        "You do not need to become a technology expert - just learn what helps you most.",
        "Many AI tools are designed specifically with older adults in mind.",
        "This book will guide you step by step through the most useful AI tools available.",
        "Each chapter focuses on practical ways AI improves your relationship with family.",
        "By the end, you will feel confident using technology to stay connected and relevant.",
        "Your life experience combined with AI knowledge makes you uniquely valuable.",
    ]),
    ("Chapter 2: Understanding What AI Can Do", [
        "AI is software that can learn, recognize patterns, and make decisions like a human would.",
        "When you ask Siri a question, that is AI processing your voice and finding an answer.",
        "When Netflix suggests a show you might like, that is AI learning your preferences.",
        "AI is not a robot - it is the intelligence behind the apps and devices you already use.",
        "AI can understand and generate human language, recognize faces, and predict what you need.",
        "It gets better over time by learning from millions of interactions with people.",
        "AI cannot feel emotions, but it can recognize and respond to yours appropriately.",
        "Most AI tools are designed to be as simple as having a conversation.",
        "You have probably already used AI without knowing it - search engines use AI constantly.",
        "The key is learning which AI tools solve your specific needs and desires.",
        "Think of AI as a very smart assistant that never gets tired and is always available.",
    ]),
    ("Chapter 3: Using Siri and Alexa to Stay Connected", [
        "Voice assistants like Siri and Alexa let you do things by simply speaking out loud.",
        "Say Hey Siri, call my granddaughter and it dials her number instantly.",
        "Ask Alexa to send a message to your son and dictate it without touching a screen.",
        "Set reminders for grandchildren's birthdays, games, recitals, and school events.",
        "Ask your assistant to show photos from last Christmas or your grandchild's birthday.",
        "Drop-in features let you check on family members with a quick voice connection.",
        "Play your grandchild's favorite songs or stories when they visit your home.",
        "Voice assistants can read audiobooks, play podcasts, and answer questions hands-free.",
        "You can add items to a shared family shopping list just by speaking.",
        "Smart displays show video during calls so you can see your family while talking.",
        "Setup takes about 10 minutes and a family member can help you get started today.",
    ]),
    ("Chapter 4: Video Calling Grandchildren - AI Enhanced", [
        "Modern video calling uses AI to improve picture quality and reduce background noise.",
        "FaceTime, Zoom, and Google Meet all use AI to keep your face centered and well-lit.",
        "AI background blur hides a messy room so you do not have to worry about tidying up.",
        "Auto-framing AI zooms in and out to keep everyone visible during group calls.",
        "Noise cancellation AI removes barking dogs, traffic, and other distracting sounds.",
        "You can add fun AI filters and effects that grandchildren love during calls.",
        "Recording features let you save special moments from video calls to watch later.",
        "Schedule regular video dates - even 10 minutes weekly keeps your bond strong.",
        "Share your screen to show photos, read a book together, or do a puzzle as a team.",
        "AI caption features help if you have difficulty hearing what grandchildren are saying.",
        "Tip: Natural light from a window in front of you makes you look best on camera.",
    ]),
    ("Chapter 5: AI Photo Sharing Made Easy", [
        "AI makes sharing photos with family effortless and automatic.",
        "Google Photos and Apple Photos automatically organize images by person, place, and date.",
        "Shared albums let the whole family add photos that everyone can see instantly.",
        "AI creates automatic highlight reels of your best photos set to music.",
        "Digital photo frames like Aura receive photos from family members wirelessly.",
        "You can email photos to certain frames - no app needed, just send from your email.",
        "AI identifies your grandchildren in photos and groups all their pictures together.",
        "Memory features surface old photos on their anniversary, creating daily surprises.",
        "Live photos capture a few seconds of video, making still images come alive.",
        "Unlimited free storage is available on several platforms for your photo collection.",
        "Family members anywhere in the world can add photos to your shared collection.",
    ]),
    ("Chapter 6: Creating AI-Powered Family Albums", [
        "AI transforms your scattered photos into beautiful, organized family albums.",
        "Apps like Chatbooks and Mixbook use AI to select your best photos automatically.",
        "AI removes blurry, duplicate, and poorly lit photos from your collection.",
        "Photo books can be ordered directly from your phone and delivered to your door.",
        "AI suggests layouts, backgrounds, and designs that make your photos look professional.",
        "Create themed albums: holidays, vacations, milestones, or one for each grandchild.",
        "AI-enhanced photos fix red eye, brighten dark images, and improve color quality.",
        "Video montages with AI editing combine clips into polished family movies.",
        "AI can restore and colorize old black-and-white family photos beautifully.",
        "These make wonderful gifts for grandchildren - your family history in print.",
        "Start with your phone photos and let the AI organize everything for you.",
    ]),
    ("Chapter 7: Using ChatGPT to Help with Homework", [
        "ChatGPT is a free AI tutor that can help you help your grandchildren with schoolwork.",
        "It explains math problems step by step in ways that are easy to understand.",
        "Ask it to explain any science concept at any grade level you need.",
        "It can help write essay outlines, check grammar, and suggest improvements.",
        "Use it to quiz grandchildren on vocabulary, history dates, or multiplication tables.",
        "ChatGPT generates practice problems for any subject at any difficulty level.",
        "It never loses patience and can explain the same concept ten different ways.",
        "You become the homework hero without needing to remember everything from school.",
        "Ask it to make learning fun with games, riddles, and stories about any subject.",
        "Important: Teach grandchildren to use AI as a learning tool, not to cheat.",
        "The goal is understanding, not just getting the right answer on paper.",
    ]),
    ("Chapter 8: AI Games to Play with Grandchildren", [
        "AI-powered games create shared experiences across generations and distances.",
        "Multiplayer word games like Words with Friends let you play remotely with family.",
        "AI trivia apps create custom quizzes about topics your whole family enjoys.",
        "Drawing games with AI (like Quick Draw) are hilarious for all ages.",
        "AI story generators create interactive adventures you can play together.",
        "Virtual scavenger hunts use AI image recognition for fun at-home competitions.",
        "AI chess and checkers apps adjust difficulty so grandparents and kids can both compete.",
        "Collaborative puzzle apps let you work together on the same puzzle remotely.",
        "AI music games identify songs you hum - perfect for guess-that-tune competitions.",
        "Video calling games like charades use AI scoring for fair and fun play.",
        "Playing together, even digitally, strengthens your emotional bond significantly.",
    ]),
    ("Chapter 9: AI Translation for Multilingual Families", [
        "Many families span multiple languages - AI translation removes communication barriers.",
        "Google Translate can instantly translate between over 100 languages for free.",
        "Camera translation lets you point your phone at text and see it in your language.",
        "Real-time conversation translation lets two people speak different languages naturally.",
        "AI earbuds can translate spoken language in real time during conversations.",
        "Text message translation helps you write and read messages in any language.",
        "Video call translation is improving rapidly with AI subtitle capabilities.",
        "Help grandchildren learn your native language with AI pronunciation practice.",
        "Share cultural stories and recipes even when grandchildren speak a different language.",
        "AI preserves the meaning and emotion of your words across language barriers.",
        "Technology finally makes multilingual family connection feel natural and easy.",
    ]),
    ("Chapter 10: AI-Powered Family History Research", [
        "AI genealogy tools have revolutionized how families discover their heritage.",
        "Ancestry and MyHeritage use AI to search billions of records for your family connections.",
        "AI can read old handwritten documents that are nearly impossible to decipher manually.",
        "DNA testing combined with AI reveals ethnic backgrounds and finds living relatives.",
        "AI matches your family tree with historical records, photos, and even newspapers.",
        "Collaborative family trees let everyone contribute what they know about relatives.",
        "AI can animate old photos of ancestors, showing what they looked like in motion.",
        "Record the family stories you know before they are lost - AI helps preserve them.",
        "Grandchildren love discovering their roots - make it a family project together.",
        "AI helps organize family documents, letters, and photos into a searchable archive.",
        "Your knowledge of family history combined with AI research creates an invaluable gift.",
    ]),
    ("Chapter 11: Teaching Grandchildren About AI Safety", [
        "As a grandparent, you play a key role in teaching digital wisdom to young ones.",
        "Help grandchildren understand that not everything AI creates is true or accurate.",
        "Teach them to verify AI-generated information with trusted sources.",
        "Discuss privacy: explain why they should not share personal details with AI chatbots.",
        "AI-generated images and videos (deepfakes) can look real but be completely fake.",
        "Help them understand that AI should be a tool, not a replacement for critical thinking.",
        "Set healthy boundaries around screen time and AI interaction for children.",
        "Teach them that AI learns from what people put online - so be careful what you share.",
        "Discuss how AI recommendations can create bubbles that limit perspectives.",
        "Model healthy technology use yourself - showing balance is the best teaching tool.",
        "Open conversations about AI build trust and keep communication flowing.",
    ]),
    ("Chapter 12: AI Gift-Finding for Grandchildren", [
        "AI shopping assistants help you find perfect gifts that grandchildren actually want.",
        "Amazon and Google AI analyze interests to suggest age-appropriate gifts.",
        "AI chatbots can help you understand trending toys and technologies children love.",
        "Price comparison AI finds the best deals across multiple stores automatically.",
        "Wish list features let grandchildren share what they want without awkward conversations.",
        "AI suggests educational gifts that are also fun - combining learning with play.",
        "Subscription box AI recommends monthly surprises tailored to each child's interests.",
        "AI can help you create personalized gifts like custom books with their name.",
        "Set AI price alerts for expensive items so you buy when prices drop.",
        "AI reminds you of birthdays, sizes, and preferences so you never forget details.",
        "The thought and effort you put in matters most - AI just helps you execute better.",
    ]),
    ("Chapter 13: Virtual Presence Robots", [
        "Telepresence robots let you be virtually present in your grandchild's home.",
        "These robots have a screen showing your face and wheels so you can move around.",
        "You control the robot from your tablet or computer - it goes where you direct it.",
        "Attend school events, birthday parties, or just hang out in the living room remotely.",
        "Some robots are affordable alternatives to frequent long-distance travel.",
        "They give you a physical presence that video calls simply cannot provide.",
        "Grandchildren can interact with the robot naturally, showing you toys and artwork.",
        "The robot can follow a child around, creating a more natural visit experience.",
        "Privacy controls ensure the robot only operates when activated by both parties.",
        "This technology is especially valuable for grandparents with mobility limitations.",
        "As costs decrease, virtual presence is becoming accessible to more families.",
    ]),
    ("Chapter 14: AI Storytelling Tools", [
        "AI helps you create amazing bedtime stories customized for each grandchild.",
        "AI story generators include your grandchild's name, interests, and friends as characters.",
        "You can create stories about family traditions, making them more engaging for children.",
        "AI illustrates your stories with custom artwork matching your narrative.",
        "Record your voice reading the story so grandchildren can listen anytime they miss you.",
        "Interactive AI stories let grandchildren choose what happens next in the adventure.",
        "Create a series of stories featuring a character you and your grandchild design together.",
        "AI can translate your stories into different languages for bilingual grandchildren.",
        "Print your AI-assisted stories into real books as gifts for special occasions.",
        "These personalized stories become family treasures passed down through generations.",
        "Your wisdom and values woven into stories teach children in the most memorable way.",
    ]),
    ("Chapter 15: Recording Family Stories with AI", [
        "Your memories and stories are irreplaceable treasures that should be preserved.",
        "AI voice recording apps transcribe your spoken stories into written text automatically.",
        "StoryWorth and similar services send weekly questions to prompt your memories.",
        "AI helps organize scattered memories into a chronological family narrative.",
        "Video recording with AI editing turns your stories into polished family documentaries.",
        "AI can enhance audio quality of old recordings you may have on cassettes or VHS.",
        "Collaborative platforms let multiple family members add their perspectives.",
        "AI creates beautiful layouts for printed memory books from your recordings.",
        "Your recipes, advice, and life lessons are preserved for future generations.",
        "Grandchildren in the future will treasure hearing your voice and your wisdom.",
        "Start today - record just one story and let AI help you build from there.",
    ]),
    ("Chapter 16: AI Health Monitoring for Peace of Mind", [
        "AI health monitoring gives both you and your family peace of mind about your safety.",
        "Wearable devices track heart rate, activity, and sleep without any effort from you.",
        "Family members can check your activity data to know you are doing well.",
        "AI alerts go to your children if anything unusual is detected in your health patterns.",
        "This reduces worry calls while keeping everyone informed about your well-being.",
        "Smart home sensors confirm your daily routine is normal without being invasive.",
        "GPS features in smartwatches provide location sharing for additional safety.",
        "AI health reports can be shared with your doctor before appointments.",
        "These tools help you maintain independence while giving family confidence.",
        "The technology is discreet - no one needs to know you are being monitored.",
        "Peace of mind benefits everyone: you stay independent, family stays informed.",
    ]),
    ("Chapter 17: Sharing Wisdom Through AI-Assisted Writing", [
        "Your life experience contains wisdom that younger generations desperately need.",
        "AI writing assistants help you organize thoughts into clear, compelling messages.",
        "Write letters to grandchildren for milestone moments: graduation, wedding, first job.",
        "AI helps polish your writing without changing your authentic voice and personality.",
        "Create a wisdom journal - one piece of advice per day for a year.",
        "AI can help you write a book about your career, hobbies, or areas of expertise.",
        "Blog platforms with AI make sharing your perspectives with the world simple.",
        "Voice-to-text means you can write by speaking naturally rather than typing.",
        "AI grammar tools ensure your message is clear without requiring perfect spelling.",
        "Your unique perspective from decades of experience is more valuable than you realize.",
        "Future generations will be grateful you took the time to preserve your wisdom.",
    ]),
    ("Chapter 18: AI and Family Group Chats", [
        "Family group chats keep everyone connected but can be overwhelming without AI help.",
        "AI organizes messages by topic so you can follow conversations that interest you.",
        "Smart replies suggest quick responses so you can stay engaged without much typing.",
        "AI transcribes voice messages for when you prefer reading over listening.",
        "Photo and video AI in chats automatically saves important shared memories.",
        "AI notification settings help you see important messages without constant buzzing.",
        "Emoji and sticker suggestions from AI help you express yourself in modern chat culture.",
        "AI translation in group chats helps multilingual families communicate seamlessly.",
        "Scheduling AI within group chats helps coordinate family gatherings efficiently.",
        "Tips: mute non-essential chats, star important messages, and check in daily.",
        "Your participation in family chats shows grandchildren you are engaged in their lives.",
    ]),
    ("Chapter 19: Bridging the Generation Gap with Technology", [
        "Technology does not have to be a barrier - it can be a bridge between generations.",
        "Ask grandchildren to teach you about their favorite apps and games.",
        "Teaching is reversed - they teach you technology, you teach them life wisdom.",
        "Shared streaming accounts let you watch the same shows and discuss them together.",
        "Gaming together online creates shared experiences regardless of physical distance.",
        "Learning AI together as a team makes both generations more comfortable with it.",
        "Social media (used wisely) lets you see and participate in daily family life.",
        "AI creation tools let you make art, music, and stories together across distances.",
        "Your willingness to try new technology earns immense respect from younger family.",
        "The effort itself - not perfection - shows your grandchildren that you care.",
        "Every generation has something to teach and something to learn from the others.",
    ]),
    ("Chapter 20: Your First Week Plan", [
        "Day 1: Ask a family member to help you set up one voice assistant in your home.",
        "Day 2: Make a video call to a grandchild - practice for just 5 minutes.",
        "Day 3: Set up a shared photo album and add 3 favorite family photos.",
        "Day 4: Try asking your voice assistant 5 questions about anything you are curious about.",
        "Day 5: Send a voice message to a family group chat sharing a brief memory or thought.",
        "Day 6: Download one AI game and play it with or against a family member.",
        "Day 7: Schedule a regular weekly video call with at least one grandchild.",
        "Remember: You do not need to master everything in one week or even one month.",
        "Celebrate each small success - every step forward is meaningful progress.",
        "Ask for help when you need it - your family wants to help you connect.",
        "You are now officially a tech-savvy grandparent. Keep going and stay curious!",
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

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book73_AI_Guide_Grandparents.pdf")
print("Created Book73_AI_Guide_Grandparents.pdf")
