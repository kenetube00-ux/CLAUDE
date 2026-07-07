"""
Book 51: AI For Beginners - A Simple Guide for Adults Over 45
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "AI FOR BEGINNERS", font='F2', size=26)
    pdf.add_centered_text(480, "A Simple Guide for", font='F1', size=16)
    pdf.add_centered_text(455, "Adults Over 45", font='F1', size=16)
    pdf.add_line(100, 430, 332, 430, 2)
    pdf.add_centered_text(390, "Everything You Need to Know About", font='F4', size=13)
    pdf.add_centered_text(370, "Artificial Intelligence - Explained Simply", font='F4', size=13)
    pdf.add_centered_text(300, "By", font='F1', size=12)
    pdf.add_centered_text(275, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "AI For Beginners - A Simple Guide for Adults Over 45", font='F2', size=11)
    pdf.add_centered_text(470, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(445, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(415, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(390, "Published via Amazon KDP", font='F1', size=10)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: What is AI?", [
            "Artificial Intelligence, or AI, is simply a computer program that can",
            "learn and make decisions, much like how you learn from experience.",
            "Think of it as a very smart assistant that gets better over time.",
            "AI is not a robot or a person - it is software running on computers.",
            "You already use AI every day without knowing it. When your email",
            "filters spam, that is AI working. When your phone suggests words",
            "as you type, that is AI too. It spots patterns and makes guesses.",
            "AI learns from huge amounts of information, called data. The more",
            "data it processes, the better it gets at its job. It is like how you",
            "get better at cooking the more recipes you try.",
            "The good news: you do not need to be technical to benefit from AI.",
            "This book will show you exactly how to use it in plain English.",
        ]),
        ("Chapter 2: How AI Works (Simple Explanation)", [
            "AI works by looking at thousands of examples and finding patterns.",
            "Imagine teaching a child to recognize cats: you show many cat photos.",
            "Eventually the child knows what a cat looks like. AI does the same.",
            "There are three basic steps: input, processing, and output.",
            "Input is the information you give the AI, like a question or photo.",
            "Processing is when the AI compares your input to what it has learned.",
            "Output is the answer or action the AI gives back to you.",
            "AI does not actually think or feel - it calculates probabilities.",
            "It figures out the most likely correct answer based on its training.",
            "Modern AI is trained on billions of text examples from the internet.",
            "This is why it can write, answer questions, and hold conversations.",
            "You do not need to understand the math - just know it finds patterns.",
        ]),
        ("Chapter 3: AI in Your Daily Life (Siri, Alexa, Netflix)", [
            "You are probably already using AI without realizing it every day.",
            "Siri on your iPhone and Alexa on Amazon devices are AI assistants.",
            "They listen to your voice, understand your words, and respond.",
            "Netflix uses AI to suggest movies and shows you might enjoy.",
            "It looks at what you have watched before and finds similar content.",
            "Google Maps uses AI to find the fastest route and predict traffic.",
            "Your email spam filter is AI that learns what junk mail looks like.",
            "Facebook and Instagram use AI to decide which posts to show you.",
            "Online shopping sites use AI to recommend products you might like.",
            "Even your smartphone camera uses AI to improve your photos.",
            "Banks use AI to detect fraud on your credit card automatically.",
            "The weather app on your phone uses AI to make better predictions.",
        ]),
        ("Chapter 4: ChatGPT Explained Simply", [
            "ChatGPT is an AI tool made by a company called OpenAI.",
            "It is like having a conversation with a very knowledgeable assistant.",
            "You type a question or request, and it types back an answer.",
            "It was trained by reading billions of pages of text from books and websites.",
            "This is why it can discuss almost any topic in a helpful way.",
            "ChatGPT does not search the internet - it uses what it already learned.",
            "Think of it like asking a friend who has read every book in the library.",
            "It can write emails, explain things simply, give advice, and more.",
            "It is free to use at chat.openai.com with a basic account.",
            "You do not need to download anything - it works in your web browser.",
            "ChatGPT is not perfect. It can sometimes give wrong information.",
            "Always double-check important facts, especially about health or money.",
            "Despite its limits, it is an incredibly useful tool for everyday tasks.",
        ]),
        ("Chapter 5: How to Use ChatGPT Step by Step", [
            "Step 1: Open your web browser (Chrome, Safari, or Firefox).",
            "Step 2: Go to chat.openai.com and click Sign Up for a free account.",
            "Step 3: Enter your email and create a password, then verify your email.",
            "Step 4: Once logged in, you will see a text box at the bottom.",
            "Step 5: Type your question or request in plain English and press Enter.",
            "The key to good results is being specific with your requests.",
            "Instead of asking 'tell me about cooking', try 'give me a simple",
            "recipe for chicken soup that takes less than 30 minutes'.",
            "You can ask follow-up questions - ChatGPT remembers the conversation.",
            "If you do not like an answer, say 'try again' or 'explain it simpler'.",
            "You can start a new conversation anytime by clicking New Chat.",
            "Practice makes perfect - the more you use it, the easier it gets.",
        ]),
        ("Chapter 6: AI & Your Job - Should You Worry?", [
            "Many people worry that AI will take their jobs. Let us look at facts.",
            "AI is best at repetitive tasks: data entry, sorting, basic analysis.",
            "Jobs that require human touch, creativity, and empathy are safer.",
            "Healthcare workers, teachers, counselors, and tradespeople are in demand.",
            "AI is more likely to change jobs than eliminate them completely.",
            "Think of how ATMs changed banking but did not eliminate all tellers.",
            "The best approach is to learn how to work alongside AI tools.",
            "People who use AI to do their jobs better will be most successful.",
            "If you are retired or near retirement, AI is more of a helper than threat.",
            "It can help you manage finances, stay healthy, and stay connected.",
            "For those still working, learning basic AI tools is a smart investment.",
            "Remember: AI is a tool, like a calculator. It helps humans do more.",
        ]),
        ("Chapter 7: AI in Healthcare", [
            "AI is making healthcare better and more accessible for everyone.",
            "Doctors use AI to read X-rays and catch diseases earlier.",
            "AI can spot patterns in medical images that humans might miss.",
            "Some apps use AI to check symptoms before you visit the doctor.",
            "AI helps pharmacies check for dangerous drug interactions.",
            "Wearable devices like Apple Watch use AI to monitor heart rhythms.",
            "AI chatbots can answer basic health questions at any time of day.",
            "Researchers use AI to develop new medicines faster than before.",
            "AI helps hospitals schedule appointments and reduce wait times.",
            "Important: AI should support your doctor, not replace them.",
            "Always consult a real doctor for serious health concerns.",
            "AI health tools work best as a first step, not a final answer.",
        ]),
        ("Chapter 8: AI for Shopping & Recommendations", [
            "When Amazon suggests products you might like, that is AI at work.",
            "AI looks at what you bought before and what similar people bought.",
            "This is called a recommendation engine and most big stores use it.",
            "Price comparison tools use AI to find the best deals automatically.",
            "Some AI tools can predict when prices will drop so you can wait.",
            "Grocery delivery apps use AI to suggest items based on past orders.",
            "AI chatbots on shopping websites can help you find what you need.",
            "Review summaries powered by AI help you make faster decisions.",
            "AI can help you set budget alerts and track spending patterns.",
            "Be aware that AI recommendations are designed to make you buy more.",
            "Use AI shopping tools to your advantage but stick to your budget.",
            "AI is especially helpful for comparing products and reading reviews.",
        ]),
        ("Chapter 9: Is AI Safe? Privacy & Security", [
            "AI safety is a valid concern. Here is what you should know.",
            "AI tools collect data about you to improve their services.",
            "Be careful what personal information you share with AI chatbots.",
            "Never give AI tools your passwords, Social Security number, or PINs.",
            "Most reputable AI companies have privacy policies - read them.",
            "Your conversations with ChatGPT may be used to improve the system.",
            "You can usually opt out of data sharing in the settings.",
            "AI can be used by scammers to write convincing fake emails.",
            "Be extra cautious of emails or calls that seem too good to be true.",
            "The same rules apply: never click suspicious links or share personal info.",
            "Overall, AI is safe to use if you follow basic internet safety rules.",
            "Think of AI like any tool - it is safe when used responsibly.",
        ]),
        ("Chapter 10: AI Art & Writing Tools", [
            "AI can now create images, write stories, and compose music.",
            "Tools like DALL-E and Midjourney create images from text descriptions.",
            "You type 'a sunset over mountains' and AI generates that picture.",
            "AI writing tools can help you draft emails, letters, and stories.",
            "Grammarly uses AI to fix spelling and improve your writing style.",
            "AI cannot truly be creative - it remixes patterns from existing work.",
            "These tools are great for getting started or overcoming writer's block.",
            "You can use AI art for greeting cards, social media, or just fun.",
            "AI writing tools save time on everyday communications.",
            "Many people use AI to help write thank you notes or invitations.",
            "The key is to use AI as a starting point and add your personal touch.",
            "AI art and writing tools are free or low cost and easy to learn.",
        ]),
        ("Chapter 11: Using AI to Save Time", [
            "One of the biggest benefits of AI is saving you time every day.",
            "AI can summarize long articles or emails in seconds.",
            "It can draft replies to messages so you just need to review and send.",
            "AI calendar tools can schedule meetings and set reminders for you.",
            "Voice assistants can set timers, make calls, and send texts hands-free.",
            "AI can help you organize photos by automatically tagging faces and places.",
            "Meal planning AI tools can create weekly menus based on your preferences.",
            "AI translation tools let you communicate in any language instantly.",
            "Smart home AI can automate lights, temperature, and security.",
            "AI can read web pages aloud to you while you do other things.",
            "The average person can save 1-2 hours daily using AI tools effectively.",
            "Start with one AI tool and add more as you get comfortable.",
        ]),
        ("Chapter 12: AI vs Human Intelligence", [
            "AI and human brains work very differently despite some similarities.",
            "AI is faster at math, data analysis, and pattern recognition.",
            "Humans are better at creativity, empathy, common sense, and judgment.",
            "AI cannot truly understand emotions or have personal experiences.",
            "A computer can beat a chess champion but cannot comfort a sad friend.",
            "AI has no consciousness, feelings, or desires of its own.",
            "It processes information but does not understand meaning the way we do.",
            "AI cannot learn from a single example like humans often can.",
            "Humans can adapt to completely new situations. AI struggles with this.",
            "The best results come from humans and AI working together.",
            "AI handles the tedious parts while humans make the important decisions.",
            "Think of AI as a powerful tool that extends your own abilities.",
        ]),
        ("Chapter 13: Common AI Myths Debunked", [
            "Myth 1: AI will become conscious and take over the world.",
            "Reality: Current AI has no consciousness or desires. It is just math.",
            "Myth 2: AI is always right and you can trust everything it says.",
            "Reality: AI makes mistakes and can give outdated or wrong information.",
            "Myth 3: AI will replace all human jobs within a few years.",
            "Reality: AI changes jobs more than it eliminates them completely.",
            "Myth 4: You need to be a computer expert to use AI.",
            "Reality: Modern AI tools are designed to be used by everyday people.",
            "Myth 5: AI is too expensive for regular people to use.",
            "Reality: Many powerful AI tools are completely free to use.",
            "Myth 6: AI can read your mind or know everything about you.",
            "Reality: AI only knows what data it has been given or trained on.",
            "Do not let myths stop you from exploring these helpful tools.",
        ]),
        ("Chapter 14: AI for Grandparents", [
            "AI can help you stay connected with grandchildren in wonderful ways.",
            "Use AI to help write fun stories featuring your grandchildren as characters.",
            "AI can suggest age-appropriate activities for grandkids of any age.",
            "Video call AI features can add fun filters that kids love.",
            "AI can help you learn the latest games and trends kids enjoy.",
            "Use AI to create personalized quizzes or scavenger hunts for visits.",
            "AI translation tools help if grandchildren speak a different language.",
            "AI can help you find and order perfect gifts based on their interests.",
            "Use AI to plan fun outings by asking for local activity suggestions.",
            "AI can help you stay current on topics so you can relate to them.",
            "You can use AI to create photo books and memory collections easily.",
            "Being tech-savvy makes you an even more amazing grandparent.",
        ]),
        ("Chapter 15: Smart Home Devices Explained", [
            "Smart home devices are gadgets that connect to the internet and respond to you.",
            "The most popular are Amazon Echo (Alexa) and Google Nest (Google Assistant).",
            "These devices sit in your home and listen for a wake word like 'Alexa'.",
            "You can ask them to play music, set timers, read news, and answer questions.",
            "Smart lights can be controlled by voice - say 'turn off the lights'.",
            "Smart thermostats learn your schedule and save money on heating and cooling.",
            "Smart doorbells let you see who is at your door from your phone.",
            "Smart plugs let you turn any device on or off with your voice.",
            "These devices are easy to set up - usually just plug in and connect to WiFi.",
            "Privacy tip: you can mute the microphone when not using voice features.",
            "Smart home devices can make daily life easier, especially as we age.",
            "Start with one device and add more as you see how helpful they are.",
        ]),
        ("Chapter 16: Voice Assistants Guide", [
            "Voice assistants let you control your phone and devices just by talking.",
            "The main ones are Siri (Apple), Alexa (Amazon), and Google Assistant.",
            "To use Siri, say 'Hey Siri' or press and hold the side button on iPhone.",
            "To use Alexa, say 'Alexa' followed by your request.",
            "To use Google Assistant, say 'Hey Google' or 'OK Google'.",
            "You can ask them to make phone calls: 'Call my daughter'.",
            "They can send texts: 'Send a message to John saying I will be late'.",
            "They set reminders: 'Remind me to take my medicine at 8 PM'.",
            "They play music: 'Play relaxing jazz music' or 'Play Frank Sinatra'.",
            "They answer questions: 'What is the weather tomorrow?'",
            "They can even tell jokes or play trivia games to pass the time.",
            "Speak naturally and clearly - you do not need special commands.",
        ]),
        ("Chapter 17: AI & Your Finances", [
            "AI is changing how we manage money, mostly for the better.",
            "Banks use AI to detect fraudulent transactions on your accounts.",
            "If someone steals your card info, AI often catches it before you do.",
            "Budgeting apps like Mint use AI to categorize your spending automatically.",
            "AI can analyze your bills and suggest where you could save money.",
            "Robo-advisors use AI to manage investments at lower costs than human advisors.",
            "AI tools can help you compare insurance rates and find better deals.",
            "Tax preparation software uses AI to find deductions you might miss.",
            "Be cautious: never give AI tools direct access to your bank accounts.",
            "Use AI financial tools for information and planning, not direct control.",
            "AI cannot predict the stock market - be wary of anyone who claims this.",
            "The best approach: use AI for financial education and organization.",
        ]),
        ("Chapter 18: Future of AI (Simple Predictions)", [
            "AI will continue to get better and more useful in the coming years.",
            "Healthcare AI will help diagnose diseases earlier and more accurately.",
            "Self-driving cars will become more common but it will take many years.",
            "AI assistants will become more conversational and helpful over time.",
            "Education will be personalized - AI tutors that adapt to each student.",
            "Translation will improve so language barriers nearly disappear.",
            "AI will help scientists solve big problems like climate change.",
            "More jobs will involve working alongside AI as a helpful partner.",
            "AI tools will become simpler and easier for everyone to use.",
            "Privacy protections and AI regulations will continue to develop.",
            "The pace of change may feel fast but you can learn at your own speed.",
            "The most important thing is to stay curious and keep learning.",
        ]),
        ("Chapter 19: Glossary of AI Terms", [
            "AI (Artificial Intelligence): Computer programs that can learn and decide.",
            "Algorithm: A set of instructions that tells a computer what to do.",
            "Chatbot: An AI program you can have a text conversation with.",
            "ChatGPT: A popular AI chatbot made by OpenAI.",
            "Data: Information that AI uses to learn, like text, images, or numbers.",
            "Deep Learning: A type of AI that uses layered networks to find patterns.",
            "Machine Learning: AI that improves automatically with more experience.",
            "Natural Language: Regular human language, as opposed to computer code.",
            "Neural Network: An AI system loosely inspired by the human brain.",
            "Prompt: The question or instruction you give to an AI tool.",
            "Training: The process of teaching AI using large amounts of data.",
            "Voice Assistant: AI that responds to spoken commands (Siri, Alexa).",
            "Large Language Model: The type of AI behind ChatGPT and similar tools.",
        ]),
        ("Chapter 20: Resources & Next Steps", [
            "Congratulations! You now understand the basics of AI.",
            "Here are your next steps to start using AI confidently:",
            "1. Create a free ChatGPT account at chat.openai.com",
            "2. Try asking ChatGPT one simple question every day for a week.",
            "3. Explore the voice assistant on your phone (Siri or Google).",
            "4. Ask a family member to help you set up a smart home device.",
            "5. Visit your local library - many offer free technology classes.",
            "Free resources: YouTube has thousands of beginner AI tutorials.",
            "AARP offers technology guides specifically for adults over 50.",
            "Your local senior center may offer computer and AI classes.",
            "Remember: there is no rush. Learn at your own comfortable pace.",
            "The most important thing is to stay curious and not be afraid to try.",
            "You have already taken the biggest step by reading this book!",
        ]),
    ]

    for title, lines in chapters:
        pdf.new_page()
        pdf.add_centered_text(600, title, font='F2', size=16)
        pdf.add_line(60, 585, 372, 585, 1)
        y = 560
        for line in lines:
            pdf.add_text(50, y, line, font='F4', size=11)
            y -= 22

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book51_AI_Beginners_Guide.pdf')
    print("Book 51 created: Book51_AI_Beginners_Guide.pdf")

if __name__ == '__main__':
    create_book()
