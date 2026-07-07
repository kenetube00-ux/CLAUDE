"""Book 72: AI for Memory & Brain Health - Keep Your Mind Sharp After 60"""
from pdf_utils import PDFDoc

doc = PDFDoc(612, 792)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 612, 792, 0.95)
doc.add_centered_text(650, "AI FOR MEMORY &", 'F2', 26)
doc.add_centered_text(615, "BRAIN HEALTH", 'F2', 26)
doc.add_centered_text(570, "Keep Your Mind Sharp After 60", 'F5', 18)
doc.add_line(156, 550, 456, 550, 2, 0.3)
doc.add_centered_text(510, "Activities, Exercises & AI Tools", 'F1', 14)
doc.add_centered_text(485, "for Cognitive Wellness", 'F1', 14)
doc.add_centered_text(250, "Daniel Tesfamariam", 'F2', 16)
doc.add_centered_text(220, "2024", 'F1', 12)

# Copyright page
doc.new_page()
doc.add_centered_text(650, "AI FOR MEMORY & BRAIN HEALTH", 'F2', 14)
doc.add_centered_text(620, "Keep Your Mind Sharp After 60", 'F4', 11)
doc.add_centered_text(580, "Copyright 2024 Daniel Tesfamariam", 'F1', 10)
doc.add_centered_text(560, "All rights reserved.", 'F1', 10)
doc.add_centered_text(530, "No part of this book may be reproduced without written permission.", 'F1', 9)
doc.add_centered_text(500, "Published independently via KDP.", 'F1', 10)
doc.add_centered_text(470, "This book is for informational purposes. Consult a healthcare provider", 'F1', 9)
doc.add_centered_text(455, "for medical advice regarding cognitive health.", 'F1', 9)

# Chapter content - mix of instruction and exercises
chapters = [
    ("Lesson 1: How AI Helps Brain Health", [
        "Your brain can grow new neural connections at any age - this is called neuroplasticity.",
        "AI technology accelerates brain training by adapting to your exact cognitive level.",
        "Unlike static puzzles, AI exercises get harder as you improve and easier when you struggle.",
        "Research shows that targeted cognitive training can delay age-related mental decline.",
        "AI tracks subtle improvements that you might not notice but are scientifically significant.",
        "The combination of novelty, challenge, and reward is exactly what your brain needs to thrive.",
        "AI brain health tools work best when combined with physical exercise and social interaction.",
        "Even 10 minutes of daily AI-guided brain exercise produces measurable results in 8 weeks.",
        "This book provides both instruction and hands-on exercises to keep your mind engaged.",
        "Each chapter includes AI tools to try and activities to complete right in these pages.",
        "Let us begin your journey to a sharper, more resilient mind at any age.",
    ]),
    ("Lesson 2: Top AI Brain Training Apps Reviewed", [
        "Lumosity is the most popular brain training app with 100 million users worldwide.",
        "It offers games targeting memory, attention, flexibility, speed, and problem-solving.",
        "Elevate focuses on language skills including reading, writing, and speaking abilities.",
        "Peak provides over 40 brain games developed with neuroscientists and universities.",
        "CogniFit offers scientifically validated assessments and personalized training programs.",
        "BrainHQ was developed by Posit Science and has strong clinical research backing.",
        "EXERCISE: Write down three cognitive areas you want to improve below.",
        "Area 1: ________________________________________________",
        "Area 2: ________________________________________________",
        "Area 3: ________________________________________________",
        "Based on your goals, I recommend starting with the app that targets your weakest area.",
    ]),
    ("Lesson 3: Setting Up Lumosity and Elevate", [
        "Step 1: Open your phone's app store (Apple App Store or Google Play Store).",
        "Step 2: Search for Lumosity and tap Install or Get to download it for free.",
        "Step 3: Create an account using your email address and choose a password.",
        "Step 4: Complete the initial assessment - this takes about 10 minutes.",
        "Step 5: The AI will create your personalized training program automatically.",
        "For Elevate: Follow the same steps but search for Elevate instead.",
        "Elevate asks about your profession and goals to customize your experience.",
        "Set a daily reminder for the same time each day to build a consistent habit.",
        "EXERCISE: Check off each step as you complete it for one app:",
        "[ ] Downloaded  [ ] Account created  [ ] Assessment done  [ ] Reminder set",
        "Tip: Start with just 5 minutes per day and gradually increase to 15 minutes.",
    ]),
    ("Lesson 4: AI Memory Games Explained", [
        "Memory games work by challenging your brain's ability to store and retrieve information.",
        "AI memory games use spaced repetition - showing items just before you would forget them.",
        "Pattern matching games strengthen working memory, which declines most with age.",
        "Spatial memory games help you remember where things are located in your environment.",
        "Name-face association games directly improve your ability to remember people's names.",
        "AI adjusts the number of items, complexity, and speed based on your performance.",
        "EXERCISE: Quick memory test - study these items for 30 seconds then cover them:",
        "Apple, Blue Car, Wooden Chair, Silver Key, Red Book, Green Hat, Gold Ring",
        "Now cover the line above and write what you remember:",
        "_______________________________________________________________",
        "Practice this exercise daily with different items to strengthen recall.",
    ]),
    ("Lesson 5: Using ChatGPT for Mental Stimulation", [
        "ChatGPT is a free AI tool that can provide unlimited mental stimulation and conversation.",
        "Ask it to create custom trivia questions about topics you love - history, science, or music.",
        "Request word puzzles, riddles, or brain teasers at your preferred difficulty level.",
        "Use it to learn something new every day - ask it to explain one interesting fact.",
        "Have conversations about books, movies, or current events to exercise verbal skills.",
        "Ask ChatGPT to quiz you on vocabulary words to strengthen language processing.",
        "Request it to create a story starter that you complete - creative writing exercises the brain.",
        "Use it to practice mental math by asking for progressively harder arithmetic problems.",
        "EXERCISE: Try this prompt with ChatGPT or write your answer here:",
        "Prompt: Give me 5 trivia questions about the 1960s.",
        "Write your answers: ____________________________________________",
    ]),
    ("Lesson 6: AI-Powered Puzzles and Trivia", [
        "AI-generated puzzles are unique every time, so your brain cannot rely on memorized solutions.",
        "Apps like Wordle use AI-like algorithms to select challenging words at the right level.",
        "AI trivia apps like Trivia Crack adapt question difficulty to your knowledge areas.",
        "Crossword generators with AI create puzzles themed around your personal interests.",
        "Sudoku apps with AI hints teach you new solving strategies as you play.",
        "EXERCISE: Complete this word association chain - each word must connect to the previous:",
        "Ocean > _____ > _____ > _____ > _____ > Mountain",
        "EXERCISE: How many words can you make from the letters in TECHNOLOGY?",
        "_______________________________________________________________",
        "_______________________________________________________________",
        "Challenge yourself to find at least 15 words. AI word games build this exact skill.",
    ]),
    ("Lesson 7: Digital Brain Exercises", [
        "Digital exercises combine visual, auditory, and problem-solving skills simultaneously.",
        "Dual-task training (doing two things at once) builds cognitive reserve against decline.",
        "AI apps track reaction time improvements - faster responses indicate healthier neural pathways.",
        "Visual processing exercises help you notice details and process information quickly.",
        "Attention exercises train you to focus on relevant information while ignoring distractions.",
        "EXERCISE: Count backward from 100 by 7s as fast as you can. Write your answers:",
        "100, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___",
        "EXERCISE: Name a fruit for every letter of the alphabet:",
        "A:___ B:___ C:___ D:___ E:___ F:___ G:___ H:___ I:___ J:___",
        "K:___ L:___ M:___ N:___ O:___ P:___ Q:___ R:___ S:___ T:___",
        "These exercises activate multiple brain regions and strengthen neural connections.",
    ]),
    ("Lesson 8: AI Music Therapy for Memory", [
        "Music activates more brain areas simultaneously than almost any other activity.",
        "AI music therapy apps select songs from your youth to trigger powerful memories.",
        "Familiar melodies can unlock memories even in people with moderate dementia.",
        "AI creates personalized playlists based on your age, preferences, and mood.",
        "Rhythm exercises improve coordination between both brain hemispheres.",
        "Learning to recognize melodies strengthens auditory processing and attention.",
        "AI apps like Music Memos can identify songs you hum but cannot quite remember.",
        "Singing along to music exercises language, memory, and emotional brain centers together.",
        "Research shows 30 minutes of music daily significantly reduces cognitive decline risk.",
        "EXERCISE: List 5 songs that bring back vivid memories from your past:",
        "1:_______ 2:_______ 3:_______ 4:_______ 5:_______",
    ]),
    ("Lesson 9: AI Photo Recognition for Memory Triggers", [
        "Looking at photographs activates the hippocampus - your brain's memory center.",
        "AI photo apps can organize thousands of old photos by faces, places, and dates.",
        "Google Photos and Apple Photos use AI to create memory slideshows automatically.",
        "Reviewing photos regularly strengthens the neural pathways associated with those memories.",
        "AI can colorize old black-and-white photos, making memories feel more vivid and real.",
        "Face recognition AI helps you identify people in old group photos you may have forgotten.",
        "AI can even enhance blurry or damaged photos so details become clearer.",
        "Creating digital photo albums with AI narration exercises organizational thinking.",
        "EXERCISE: Find 3 old photos and write one memory each photo triggers:",
        "Photo 1 memory: ____________________________________________",
        "Photo 2 memory: ____________________________________________",
        "Photo 3 memory: ____________________________________________",
    ]),
    ("Lesson 10: Using AI to Write Memoirs", [
        "Writing your life story is one of the most powerful brain exercises available.",
        "Memoir writing activates memory retrieval, language, creativity, and emotional processing.",
        "AI tools like ChatGPT can help you organize memories into compelling chapters.",
        "Voice-to-text AI lets you speak your stories instead of typing them out.",
        "AI can suggest prompts when you feel stuck - asking questions you had not considered.",
        "Grammar and spelling AI ensures your writing is polished without you worrying about errors.",
        "Structuring memories chronologically exercises your temporal reasoning skills.",
        "EXERCISE: Write a brief paragraph about your earliest childhood memory:",
        "_______________________________________________________________",
        "_______________________________________________________________",
        "Tip: AI can help expand any paragraph into a full chapter with guided questions.",
    ]),
    ("Lesson 11: AI Language Learning for Brain Plasticity", [
        "Learning a new language is the gold standard of brain exercises at any age.",
        "Bilingual people develop dementia 4-5 years later than monolingual people on average.",
        "AI apps like Duolingo adapt lessons perfectly to your learning speed and style.",
        "Speech recognition AI provides instant pronunciation feedback without embarrassment.",
        "AI tutors are infinitely patient - they never judge and always encourage progress.",
        "Even 5 minutes daily of language practice creates new neural connections.",
        "AI tracks which words you forget and reviews them at optimal intervals.",
        "Conversation AI lets you practice speaking in a low-pressure environment.",
        "EXERCISE: Learn these 5 words in a new language using an AI app today:",
        "Hello, Thank you, Goodbye, Please, Friend",
        "Language chosen: _________ Words practiced: [ ] Yes [ ] Not yet",
    ]),
    ("Lesson 12: AI Meditation for Cognitive Health", [
        "Meditation physically changes your brain - increasing gray matter in memory areas.",
        "AI meditation apps personalize sessions based on your stress level and available time.",
        "Apps like Calm and Headspace use AI to recommend the perfect meditation for today.",
        "Guided breathing exercises reduce cortisol, which damages brain cells over time.",
        "Body scan meditations improve interoception - awareness of internal body signals.",
        "AI tracks your meditation consistency and shows how it correlates with mood and sleep.",
        "Even 5 minutes of daily meditation shows measurable brain benefits after 8 weeks.",
        "AI-generated soundscapes adapt in real time to your breathing and heart rate.",
        "Mindfulness strengthens your prefrontal cortex - the brain's executive control center.",
        "EXERCISE: Close your eyes and count 10 slow breaths. Notice how you feel after.",
        "Before: stressed/calm/neutral (circle one). After: stressed/calm/neutral (circle one).",
    ]),
    ("Lesson 13: Daily AI Brain Routine - Morning Checklist", [
        "A consistent daily routine is the most important factor in brain health maintenance.",
        "MORNING ROUTINE (15 minutes total for maximum cognitive benefit):",
        "[ ] 1. Voice check-in with smart speaker (ask for today's date, weather, news - 2 min)",
        "[ ] 2. Brain training app session - complete one daily challenge (5 min)",
        "[ ] 3. AI language lesson - learn one new phrase in your target language (3 min)",
        "[ ] 4. Memory exercise - recall 3 things from yesterday in detail (2 min)",
        "[ ] 5. AI meditation - one guided breathing session (3 min)",
        "EVENING ROUTINE (10 minutes):",
        "[ ] 1. Journal three things you learned today using voice-to-text AI (3 min)",
        "[ ] 2. AI puzzle or trivia game (5 min)",
        "[ ] 3. Plan tomorrow by telling your AI assistant your schedule (2 min)",
        "Consistency matters more than intensity. Do a little every single day.",
    ]),
    ("Lesson 14: AI Tools for Early Dementia Detection", [
        "AI can detect cognitive changes years before traditional tests catch them.",
        "Speech pattern analysis AI identifies subtle language changes indicating decline.",
        "Typing speed and accuracy monitoring reveals early cognitive processing changes.",
        "AI game performance tracking shows trends invisible to casual observation.",
        "Eye tracking AI can detect attention and memory problems through gaze patterns.",
        "Digital cognitive assessments can be taken at home and shared with your doctor.",
        "AI differentiates between normal aging forgetfulness and concerning decline patterns.",
        "Early detection allows early intervention, which dramatically slows progression.",
        "Regular AI cognitive testing creates a baseline that makes changes easier to spot.",
        "IMPORTANT: These tools support but do not replace professional medical assessment.",
        "Discuss any concerns with your doctor, who can order formal neuropsychological testing.",
    ]),
    ("Lesson 15: AI Reminder Systems for Forgetfulness", [
        "AI reminders go far beyond simple alarms - they understand context and importance.",
        "Location-based reminders trigger when you arrive somewhere (bring list to grocery store).",
        "AI learns which reminders you dismiss and adjusts timing for better effectiveness.",
        "Multi-modal reminders use voice, text, and visual alerts to ensure you notice them.",
        "AI assistants can remind you of people's names before social events.",
        "Smart home AI reminds you to turn off the stove, lock doors, and close windows.",
        "Calendar AI suggests optimal times for activities based on your energy patterns.",
        "Routine reminders help maintain healthy habits like hydration and medication.",
        "EXERCISE: Set up 3 AI reminders today for things you commonly forget:",
        "Reminder 1: ________________________________________________",
        "Reminder 2: ________________________________________________",
        "Reminder 3: ________________________________________________",
    ]),
    ("Lesson 16: AI Social Connection Tools", [
        "Social interaction is proven to protect against cognitive decline more than any single activity.",
        "AI-powered video calling improves audio and visual quality for clearer conversations.",
        "Smart displays like Echo Show and Google Nest Hub make video calling effortless.",
        "AI can automatically start scheduled calls with family so you never forget to connect.",
        "Social AI platforms match you with conversation partners who share your interests.",
        "Group video features let you see and talk with multiple family members at once.",
        "AI transcription during calls helps if you have difficulty hearing every word.",
        "Photo sharing AI sends daily family photos to a dedicated digital frame automatically.",
        "AI scheduling helps coordinate group activities and family gatherings.",
        "EXERCISE: Schedule 3 social calls this week using your AI assistant:",
        "Call 1: _____ with _____ Call 2: _____ with _____ Call 3: _____ with _____",
    ]),
    ("Lesson 17: AI Reading Assistants", [
        "Reading is one of the best activities for maintaining cognitive health as you age.",
        "AI reading assistants can adjust font size, contrast, and spacing for easier reading.",
        "Text-to-speech AI reads books and articles aloud in natural-sounding voices.",
        "AI summarizes long articles so you get key information without fatigue.",
        "Speed reading apps use AI to help you read faster while maintaining comprehension.",
        "AI can explain complex vocabulary and concepts as you read unfamiliar material.",
        "Audiobook apps with AI adjust reading speed and can repeat sections on request.",
        "Book recommendation AI suggests titles based on your reading history and interests.",
        "Reading comprehension exercises through AI apps build critical thinking skills.",
        "EXERCISE: Read one article today and write a 2-sentence summary here:",
        "_______________________________________________________________",
    ]),
    ("Lesson 18: Nutrition AI for Brain Foods", [
        "Your diet directly impacts brain health - certain foods support cognitive function.",
        "AI nutrition apps identify brain-healthy foods and help you eat more of them.",
        "The MIND diet (Mediterranean-DASH Intervention for Neurodegenerative Delay) is best for brain health.",
        "Key brain foods: berries, leafy greens, nuts, olive oil, fish, and whole grains.",
        "AI meal planners can create weekly menus focused on cognitive-boosting nutrients.",
        "Omega-3 fatty acids, found in fish and walnuts, are essential for brain cell membranes.",
        "Antioxidant-rich foods (blueberries, dark chocolate) protect neurons from damage.",
        "AI apps track your intake of brain-critical nutrients like B12, folate, and vitamin D.",
        "Hydration tracking AI reminds you to drink water - even mild dehydration impairs thinking.",
        "EXERCISE: Plan 3 brain-healthy meals using these ingredients:",
        "Breakfast:_______ Lunch:_______ Dinner:_______",
    ]),
    ("Lesson 19: 30-Day AI Brain Challenge Plan", [
        "This 30-day plan builds daily habits that measurably improve cognitive function.",
        "Week 1 (Days 1-7): Download and begin daily brain training app sessions (5 min/day).",
        "Week 1 also: Set up AI reminders for all medications and appointments.",
        "Week 2 (Days 8-14): Add AI language learning - practice 5 minutes per day.",
        "Week 2 also: Begin AI-guided meditation - 3 minutes each morning.",
        "Week 3 (Days 15-21): Start AI-powered physical exercise program (walking with tracker).",
        "Week 3 also: Use AI nutrition app to add one brain-healthy food per day.",
        "Week 4 (Days 22-28): Add social connection - one AI-facilitated call per day.",
        "Week 4 also: Begin AI memoir writing - record one memory per day with voice AI.",
        "Days 29-30: Review your progress, celebrate improvements, and plan month 2.",
        "TRACKING: Mark each completed day below with a check or X.",
    ]),
    ("Lesson 20: Resources and Next Steps", [
        "You have completed the AI for Memory and Brain Health program - congratulations!",
        "Continue your daily brain routine for maximum long-term cognitive benefits.",
        "Recommended free apps: Lumosity, Duolingo, Calm (free version), Google Photos.",
        "Recommended devices: Any smartwatch, a smart speaker, and a tablet for brain games.",
        "Share this knowledge with friends - social learning strengthens both your brains.",
        "Schedule a cognitive assessment with your doctor to establish a formal baseline.",
        "Join online communities: AARP Brain Health, Alzheimer's Association, BrainHQ community.",
        "Keep challenging yourself - when something becomes easy, increase the difficulty.",
        "Physical exercise remains the single best thing you can do for brain health overall.",
        "Remember: It is never too late to start. Your brain can grow at any age.",
        "Thank you for investing in your cognitive health. Keep your mind sharp and active!",
    ]),
]

for title, lines in chapters:
    doc.new_page()
    doc.add_text(50, 740, title, 'F2', 15)
    doc.add_line(50, 730, 562, 730, 1, 0.4)
    y = 700
    for line in lines:
        doc.add_text(50, y, line, 'F4', 11)
        y -= 26

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book72_AI_Memory_Brain_Health.pdf")
print("Created Book72_AI_Memory_Brain_Health.pdf")
