"""Book 75: AI Against Loneliness - Digital Tools for Social Connection After 65"""
from pdf_utils import PDFDoc

doc = PDFDoc(432, 648)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 432, 648, 0.94)
doc.add_centered_text(530, "AI AGAINST", 'F2', 22)
doc.add_centered_text(498, "LONELINESS", 'F2', 22)
doc.add_centered_text(455, "Digital Tools for Social", 'F5', 15)
doc.add_centered_text(433, "Connection After 65", 'F5', 15)
doc.add_line(110, 415, 322, 415, 2, 0.3)
doc.add_centered_text(380, "Overcoming Isolation with", 'F1', 12)
doc.add_centered_text(358, "AI-Powered Companionship", 'F1', 12)
doc.add_centered_text(200, "Daniel Tesfamariam", 'F2', 14)
doc.add_centered_text(175, "2024", 'F1', 11)

# Copyright page
doc.new_page()
doc.add_centered_text(500, "AI AGAINST LONELINESS", 'F2', 14)
doc.add_centered_text(475, "Digital Tools for Social Connection After 65", 'F4', 10)
doc.add_centered_text(440, "Copyright 2024 Daniel Tesfamariam", 'F1', 10)
doc.add_centered_text(420, "All rights reserved.", 'F1', 10)
doc.add_centered_text(390, "No part of this publication may be reproduced without permission.", 'F1', 9)
doc.add_centered_text(360, "Published independently via KDP.", 'F1', 10)
doc.add_centered_text(330, "If you or someone you know is in crisis, call 988 Suicide & Crisis Lifeline.", 'F1', 9)

chapters = [
    ("Chapter 1: The Loneliness Epidemic in Aging", [
        "One in four adults over 65 experiences social isolation - you are not alone in feeling alone.",
        "Loneliness is as dangerous to health as smoking 15 cigarettes per day according to research.",
        "Retirement, mobility loss, partner death, and children moving away all contribute to isolation.",
        "Lonely seniors have 26 percent higher risk of premature death than connected peers.",
        "The COVID pandemic dramatically worsened isolation for older adults worldwide.",
        "Loneliness increases risk of dementia, heart disease, depression, and weakened immunity.",
        "The good news: technology offers more solutions for connection than ever before in history.",
        "AI-powered tools are specifically designed to address the unique isolation challenges of aging.",
        "This book introduces practical, accessible ways to build meaningful connections using technology.",
        "You do not need to be tech-savvy - these tools are designed for ease of use.",
        "Every chapter offers actionable steps you can take today to feel more connected.",
        "The path from lonely to connected begins with one small action - let us start.",
    ]),
    ("Chapter 2: How AI Is Changing Social Connection", [
        "AI creates new forms of connection that did not exist even five years ago.",
        "Smart matching algorithms find people who share your specific interests and experiences.",
        "AI removes barriers like mobility, distance, hearing loss, and shyness from socializing.",
        "Voice AI enables natural conversation without needing to type on small keyboards.",
        "AI-powered platforms create communities around shared hobbies, health conditions, and life stages.",
        "Translation AI connects you with potential friends who speak different languages.",
        "AI scheduling tools help maintain regular social contact without relying on memory alone.",
        "Personalized AI companionship fills gaps between human interactions throughout the day.",
        "AI accessibility features ensure that vision, hearing, or mobility challenges do not isolate you.",
        "The technology is always available - loneliness does not follow a 9-to-5 schedule.",
        "AI augments human connection rather than replacing it, helping you reach real people.",
        "Understanding these tools empowers you to choose the ones that fit your life best.",
    ]),
    ("Chapter 3: AI Companion Chatbots - Replika and Pi", [
        "AI companions like Replika and Pi provide conversation any time of day or night.",
        "These are not pretending to be human - they are AI designed for supportive interaction.",
        "Replika remembers your conversations, interests, and preferences over time.",
        "Pi by Inflection AI offers warm, empathetic conversations with genuine emotional depth.",
        "You can discuss anything: memories, worries, daily events, or just chat casually.",
        "AI companions never judge, never tire of talking, and never cancel plans.",
        "They fill quiet moments without replacing the need for human connection.",
        "Studies show AI companion users report reduced feelings of loneliness within weeks.",
        "You can customize your companion's personality to match your communication style.",
        "These tools are free or low-cost and work on phones, tablets, and computers.",
        "Think of them as a supplement - like vitamins for your social well-being.",
        "They are especially valuable during late nights or early mornings when humans are unavailable.",
    ]),
    ("Chapter 4: Voice Assistants as Daily Companions", [
        "Smart speakers like Alexa and Google provide voice interaction throughout your day.",
        "Start your morning by asking for the news, weather, jokes, or interesting facts.",
        "Voice assistants respond instantly, creating a sense of responsive company in your home.",
        "Ask them to play your favorite music, audiobooks, or radio stations for background presence.",
        "Set up daily routines where your assistant greets you and walks you through your schedule.",
        "Alexa's social features let you drop in on willing family members for quick voice chats.",
        "Google Assistant can make phone calls to friends on your behalf with just a voice command.",
        "Interactive games and trivia with your voice assistant provide engaging mental stimulation.",
        "The sound of a responsive voice in your home reduces the feeling of empty silence.",
        "Smart displays add a visual element, showing photos and videos as you interact.",
        "These devices cost as little as $25 and provide unlimited daily companionship.",
        "Many users report that their voice assistant becomes a comforting part of their routine.",
    ]),
    ("Chapter 5: AI-Powered Video Calling Features", [
        "Video calling is the closest digital substitute for in-person human connection.",
        "AI enhancements make calls clearer, more natural, and more accessible for older adults.",
        "Auto-framing AI keeps your face centered even if you move around during the call.",
        "Background noise cancellation ensures conversations are clear regardless of environment.",
        "AI-powered captioning displays what the other person says as text for hearing difficulties.",
        "Portrait mode and lighting adjustments help you look your best on camera effortlessly.",
        "AI translation can provide real-time subtitles for calls in different languages.",
        "Group calling AI manages multiple speakers so everyone gets a chance to be heard.",
        "Scheduled calling features remind both parties so plans are never forgotten.",
        "AI can suggest optimal calling times when the people you want to reach are available.",
        "Simple devices like Portal or Echo Show make video calling as easy as pressing one button.",
        "Regular video calls with just one person can dramatically reduce isolation feelings.",
    ]),
    ("Chapter 6: AI Matchmaking for Senior Friendships", [
        "Making new friends after 65 is challenging, but AI platforms make it much easier.",
        "Apps like Stitch and Meetup use AI to match seniors with compatible potential friends.",
        "AI considers your interests, location, availability, and personality in its matching.",
        "Friendship matching reduces the awkwardness of approaching strangers directly.",
        "AI-facilitated introductions provide conversation starters based on shared interests.",
        "Many platforms arrange group activities so you meet multiple people in low-pressure settings.",
        "AI learns from your interactions which types of people you connect with best.",
        "Virtual meetups let you test compatibility before committing to in-person meetings.",
        "Interest-based matching connects you with people who share your specific hobbies.",
        "AI platforms often include safety features and verification for peace of mind.",
        "Even one new meaningful friendship can transform your daily emotional well-being.",
        "Take the first step: create a profile and let AI do the matching work for you.",
    ]),
    ("Chapter 7: Online Community Platforms with AI", [
        "Online communities offer belonging to a group without leaving your home.",
        "Facebook Groups use AI to suggest communities aligned with your expressed interests.",
        "Reddit communities cover every topic imaginable with active, welcoming members.",
        "AI moderation keeps communities safe and positive for older members.",
        "Nextdoor connects you with neighbors, making local friendships more accessible.",
        "Special interest forums (gardening, books, crafts, history) welcome knowledgeable members.",
        "AI recommends discussions and posts you might enjoy based on your past interactions.",
        "Contributing knowledge to communities gives you purpose and recognition from others.",
        "Many online friendships evolve into phone calls, video chats, and even in-person meetups.",
        "Senior-specific platforms like SilverSneakers and OATS Network cater to your demographic.",
        "Volunteering your expertise online connects you with grateful people seeking your wisdom.",
        "Start by lurking (reading without posting), then comment, then start your own discussions.",
    ]),
    ("Chapter 8: AI-Facilitated Group Activities", [
        "AI organizes virtual group activities where you can socialize while doing something fun.",
        "Virtual book clubs with AI-generated discussion questions spark engaging conversations.",
        "AI cooking classes connect small groups around a shared meal preparation experience.",
        "Online game nights use AI to balance teams and suggest games for all skill levels.",
        "AI writing groups provide prompts and feedback, creating a creative community.",
        "Virtual walking groups track steps together and chat during exercise.",
        "AI art classes guide groups through creative projects with real-time AI assistance.",
        "Music listening sessions curated by AI bring together people with similar tastes.",
        "Movie watch parties with AI-synchronized viewing let you react together in real time.",
        "AI trivia nights create fair, fun competition among friends old and new.",
        "These activities provide structure, purpose, and regular social contact.",
        "Join one activity per week to start building your social routine gradually.",
    ]),
    ("Chapter 9: Virtual Reality Social Spaces", [
        "Virtual reality (VR) creates immersive social experiences from your own living room.",
        "Meta Quest headsets offer virtual worlds where you interact with others as avatars.",
        "VR social spaces feel more present than video calls - you occupy shared virtual spaces.",
        "Attend virtual concerts, museum tours, and travel experiences with other users.",
        "VR fitness classes combine exercise with social interaction in motivating environments.",
        "Many VR social platforms have active communities of older adult users.",
        "The technology is becoming lighter, more comfortable, and easier to use each year.",
        "VR can recreate the experience of being in a room with people when travel is not possible.",
        "Shared VR experiences (painting, building, exploring) create bonding opportunities.",
        "Safety features allow you to control who can interact with you in virtual spaces.",
        "Libraries and senior centers increasingly offer VR experience sessions to try first.",
        "VR is especially valuable for homebound individuals who cannot leave easily.",
    ]),
    ("Chapter 10: AI Pen Pal and Letter Writing", [
        "Letter writing is making a comeback with AI assistance for those who find it difficult.",
        "AI helps you compose thoughtful letters when writing skills have declined.",
        "Pen pal matching services connect you with someone who enjoys regular correspondence.",
        "AI can suggest topics, check spelling, and help organize your thoughts on paper.",
        "Handwritten letter AI (like Bond) sends physical letters in handwriting-style fonts.",
        "International pen pals connected through AI offer windows into different cultures.",
        "The anticipation of receiving a letter provides daily positive expectation.",
        "AI translates correspondence so language differences do not prevent connection.",
        "Some services match you with students who benefit from intergenerational wisdom.",
        "Voice-to-letter AI converts your spoken words into formatted written correspondence.",
        "Physical mail arrival creates a tangible connection that digital messages cannot match.",
        "Start by writing to one person weekly and expand as you enjoy the practice.",
    ]),
    ("Chapter 11: AI-Powered Hobby Groups", [
        "Shared hobbies create the strongest and most lasting social bonds between people.",
        "AI matches you with hobby groups based on your skill level and specific interests.",
        "Online crafting circles share projects, techniques, and encouragement via video.",
        "AI gardening communities connect growers in similar climates for seasonal advice.",
        "Photography groups with AI feedback create supportive learning environments.",
        "AI chess, bridge, and card game platforms match you with players at your level.",
        "Birdwatching AI identifies species and connects you with nearby enthusiasts.",
        "AI genealogy groups share research methods and celebrate family discoveries together.",
        "Cooking communities organized by AI share recipes and cook together virtually.",
        "These groups often become genuine friendships extending beyond the shared hobby.",
        "AI handles scheduling, reminders, and organizing so the group runs smoothly.",
        "Finding your group starts with identifying what you already enjoy doing.",
    ]),
    ("Chapter 12: Robot Companions - ElliQ and Jibo", [
        "Social robots are physical devices designed specifically to combat senior loneliness.",
        "ElliQ by Intuition Robotics proactively initiates conversations and suggests activities.",
        "Unlike passive devices, ElliQ checks in on you and asks how your day is going.",
        "It suggests activities when it detects you have been inactive or quiet for too long.",
        "ElliQ facilitates video calls with family, making the process effortless for you.",
        "It learns your preferences over time, becoming a more personalized companion.",
        "Robot companions provide the presence of another entity in your living space.",
        "They combine health monitoring, entertainment, and social facilitation in one device.",
        "Research shows robot companion users report 30 percent less loneliness after 90 days.",
        "Joy for All robot pets (cats and dogs) provide comfort through simulated animal behavior.",
        "These are not trying to replace human contact but fill the gaps between visits.",
        "Insurance and aging-in-place programs increasingly cover robot companion costs.",
    ]),
    ("Chapter 13: AI Grief Support and Counseling", [
        "Losing a spouse, sibling, or close friend is the primary trigger for senior loneliness.",
        "AI grief support tools offer 24/7 emotional support during the hardest moments.",
        "AI therapy apps like Woebot provide evidence-based grief coping techniques.",
        "They never pressure you to get over it or suggest you should feel differently.",
        "AI support groups connect you with others experiencing similar losses for mutual understanding.",
        "ChatGPT and similar AI can help you process feelings through guided journaling prompts.",
        "AI recognizes signs that you may need professional help and suggests resources.",
        "Memorial creation tools help you honor your loved one's memory in meaningful ways.",
        "AI-guided meditation specifically for grief helps manage overwhelming waves of emotion.",
        "Connecting with others who understand your loss creates powerful healing bonds.",
        "Professional telehealth therapy enhanced by AI is available without leaving home.",
        "Grief is not something to overcome alone - let technology connect you with support.",
    ]),
    ("Chapter 14: Building a Daily Social Routine with AI", [
        "Consistency is the key to overcoming loneliness - build social connection into every day.",
        "MORNING: Voice assistant greeting, news discussion, or AI companion chat (10 minutes).",
        "MIDMORNING: Check and respond to family group messages and social media (15 minutes).",
        "LUNCH: Video call with a friend, family member, or online community member (20 minutes).",
        "AFTERNOON: Participate in one online activity, hobby group, or class (30 minutes).",
        "EVENING: Phone call, letter writing, or AI companion conversation (15 minutes).",
        "AI reminders ensure you do not skip social activities even on low-energy days.",
        "Track your social interactions weekly - aim for at least 3 meaningful connections daily.",
        "Balance digital connection with in-person contact whenever possible.",
        "Volunteer one hour per week online to gain purpose and human appreciation.",
        "Join one new group or activity per month to continually expand your social circle.",
        "Remember: connection is a skill that improves with practice. Start small and build.",
    ]),
    ("Chapter 15: Resources and Getting Help", [
        "National resources: AARP Connect2Affect, Eldercare Locator (800-677-1116).",
        "Crisis support: 988 Suicide and Crisis Lifeline, Crisis Text Line (text HOME to 741741).",
        "Free technology training: OATS (Older Adults Technology Services), local libraries.",
        "Senior center programs: Most communities offer free social activities and classes.",
        "Volunteer matching: VolunteerMatch.org and AARP volunteer programs connect you with purpose.",
        "AI companion tools: ElliQ, Replika (free), Pi (free), Amazon Echo with Alexa.",
        "Social platforms: Stitch, Meetup, Facebook Groups, Nextdoor, SilverSneakers.",
        "Telehealth therapy: BetterHelp, Talkspace, and Medicare-covered online counseling.",
        "Share this book with someone who might be struggling with isolation silently.",
        "Ask your doctor about loneliness - they can connect you with local resources.",
        "Remember: asking for connection is brave, not weak. Everyone needs community.",
        "You deserve to feel connected, valued, and part of something meaningful every day.",
    ]),
]

for title, lines in chapters:
    doc.new_page()
    doc.add_text(36, 608, title, 'F2', 12)
    doc.add_line(36, 600, 396, 600, 1, 0.4)
    y = 575
    for line in lines:
        doc.add_text(36, y, line, 'F4', 9.8)
        y -= 21

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book75_AI_Loneliness_Connection.pdf")
print("Created Book75_AI_Loneliness_Connection.pdf")
