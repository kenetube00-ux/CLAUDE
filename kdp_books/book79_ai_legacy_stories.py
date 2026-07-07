"""Book 79: Tell Your Story with AI - A Guide to Preserving Your Legacy"""
from pdf_utils import PDFDoc

doc = PDFDoc(432, 648)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 432, 648, 0.94)
doc.add_centered_text(530, "TELL YOUR STORY", 'F2', 22)
doc.add_centered_text(498, "WITH AI", 'F2', 22)
doc.add_centered_text(455, "A Guide to Preserving", 'F5', 15)
doc.add_centered_text(433, "Your Legacy", 'F5', 15)
doc.add_line(110, 415, 322, 415, 2, 0.3)
doc.add_centered_text(380, "Record, Organize & Share", 'F1', 12)
doc.add_centered_text(358, "Your Life Story", 'F1', 12)
doc.add_centered_text(200, "Daniel Tesfamariam", 'F2', 14)
doc.add_centered_text(175, "2024", 'F1', 11)

# Copyright page
doc.new_page()
doc.add_centered_text(500, "TELL YOUR STORY WITH AI", 'F2', 14)
doc.add_centered_text(475, "A Guide to Preserving Your Legacy", 'F4', 10)
doc.add_centered_text(440, "Copyright 2024 Daniel Tesfamariam", 'F1', 10)
doc.add_centered_text(420, "All rights reserved.", 'F1', 10)
doc.add_centered_text(390, "No part of this publication may be reproduced without permission.", 'F1', 9)
doc.add_centered_text(360, "Published independently via KDP.", 'F1', 10)

chapters = [
    ("Chapter 1: Why Your Story Matters", [
        "Every person who has lived has a story worth telling and worth preserving.",
        "Your experiences, wisdom, and memories are irreplaceable once they are gone.",
        "Future generations will treasure knowing where they came from and who came before.",
        "Stories connect us across time - your grandchildren's grandchildren can know you.",
        "The lessons you learned through living cannot be found in any textbook or search engine.",
        "Historical events you witnessed become personal and real through your perspective.",
        "Family traditions, recipes, and values are preserved through your storytelling.",
        "Many people wait too long to record their stories - cognitive changes make it harder over time.",
        "AI technology has made preserving your legacy easier and more accessible than ever before.",
        "You do not need to be a writer - you just need to be willing to remember and share.",
        "This book guides you through every step of capturing and sharing your unique story.",
        "Start today. Future generations are already waiting to hear from you.",
    ]),
    ("Chapter 2: AI Tools for Recording Oral Histories", [
        "Speaking your story is the most natural and comfortable way to begin preserving it.",
        "AI voice recording apps capture your words in high quality on any smartphone.",
        "Automatic transcription converts your spoken stories into written text instantly.",
        "AI cleans up verbal fillers (um, uh, you know) to create polished written versions.",
        "Cloud storage ensures your recordings are never lost even if your device is damaged.",
        "StoryWorth sends weekly email prompts that you answer by speaking into your phone.",
        "AI organizes recordings by topic, date, and family connection automatically.",
        "Voice quality enhancement AI makes even recordings in imperfect environments sound clear.",
        "You can record in short bursts: 5-10 minute sessions capture one story at a time.",
        "Speaker identification AI separates voices when recording conversations with family.",
        "Your voice itself becomes part of the legacy - the way you speak is uniquely yours.",
        "Start with a simple voice memo app and record one memory today.",
    ]),
    ("Chapter 3: Using ChatGPT to Organize Your Memories", [
        "ChatGPT helps you structure scattered memories into a coherent narrative.",
        "Start by telling it about a period of your life and it asks follow-up questions.",
        "AI helps you identify the most important themes and stories to include.",
        "It suggests chronological organization: childhood, education, career, family, retirement.",
        "Alternative structures work too: organized by lessons, by relationships, or by places.",
        "ChatGPT generates chapter outlines based on the stories you want to tell.",
        "It can expand brief memories into full scenes with sensory details you add.",
        "AI helps you connect different stories that share common themes or lessons.",
        "Writer's block disappears when AI provides specific questions about your experiences.",
        "You maintain full control - AI suggests, you decide what to include or change.",
        "The goal is your authentic voice, organized clearly for others to read and enjoy.",
        "Try this prompt: Tell me about the neighborhood where you grew up.",
    ]),
    ("Chapter 4: AI Transcription of Old Letters and Documents", [
        "Old handwritten letters, diaries, and documents hold family treasures waiting to be unlocked.",
        "AI handwriting recognition can read even faded, cursive writing from decades past.",
        "Apps like Google Lens and Microsoft Lens photograph and transcribe documents instantly.",
        "AI preserves the content in searchable digital text while originals can be safely stored.",
        "Foreign language documents are translated automatically, revealing immigrant stories.",
        "Old recipes written in grandmother's hand become typed and shareable with family.",
        "Military records, birth certificates, and immigration papers tell factual parts of your history.",
        "AI can date and authenticate old documents based on paper, ink, and writing styles.",
        "Damaged or partially legible documents are enhanced by AI for better readability.",
        "Digital preservation means these documents survive even if the originals deteriorate.",
        "Start with the most precious documents first and work your way through boxes systematically.",
        "Every letter and document is a piece of the puzzle of your family's story.",
    ]),
    ("Chapter 5: Creating AI-Assisted Memoir Chapters", [
        "AI transforms your raw memories into polished memoir chapters you can be proud of.",
        "Start with a voice recording of your memory, then let AI create a first draft.",
        "AI writing assistants add vivid details, transitions, and structure to your stories.",
        "Your voice and personality remain - AI just helps with organization and flow.",
        "Each chapter can focus on one story, one person, one period, or one lesson.",
        "AI suggests opening hooks that draw readers in and closings that leave them reflecting.",
        "Grammar and spelling are corrected automatically so you focus on the story, not mechanics.",
        "AI can match the tone you prefer: humorous, reflective, straightforward, or poetic.",
        "Multiple drafts let you refine until each chapter feels exactly right.",
        "AI creates smooth transitions between chapters for a cohesive reading experience.",
        "A completed memoir does not need to be published - it is a gift for family alone.",
        "Aim for one chapter per week and you will have a full memoir in months.",
    ]),
    ("Chapter 6: AI Photo Restoration and Organization", [
        "Old photographs are the visual anchors of your life story and family heritage.",
        "AI restoration removes scratches, stains, tears, and fading from damaged photos.",
        "Colorization AI adds realistic color to black-and-white photos from decades past.",
        "Face enhancement AI sharpens blurry faces so you can clearly see your ancestors.",
        "Resolution upscaling makes small prints large enough to display or include in books.",
        "AI organization sorts thousands of photos by date, location, and people automatically.",
        "Facial recognition groups all photos of the same person together across decades.",
        "AI identifies unlabeled photos by matching faces with known family members.",
        "Duplicate detection removes redundant scans and keeps only the best version.",
        "Metadata addition lets you tag photos with names, dates, and stories for future reference.",
        "These restored photos become the illustrations in your life story narrative.",
        "Start by scanning your most treasured photos and letting AI bring them back to life.",
    ]),
    ("Chapter 7: AI Video Creation from Old Photos", [
        "AI transforms static photos into dynamic video presentations with music and narration.",
        "Apps like Google Photos and Apple create automatic memory videos from your images.",
        "AI animation brings old photos to life with subtle facial movements and expressions.",
        "Ken Burns effect (pan and zoom) makes still images feel cinematic and engaging.",
        "AI-selected music matches the mood and era of your photos perfectly.",
        "Your voice narration can be added over the video to tell the story behind each image.",
        "Slideshow transitions are smooth and professional without any editing skills needed.",
        "Family event compilations create shareable videos for reunions and celebrations.",
        "AI generates captions and titles to identify people, places, and dates in the video.",
        "Videos can be shared via email, social media, or burned to DVDs for family members.",
        "A 3-minute family video is often more impactful than hours of unorganized photos.",
        "These videos become family heirlooms shared at gatherings for generations to come.",
    ]),
    ("Chapter 8: Building a Digital Family Archive", [
        "A digital archive preserves your family's history in an organized, accessible format.",
        "Cloud storage services keep everything safe from fire, flood, and physical deterioration.",
        "AI organizes archives by person, event, date, and topic for easy searching later.",
        "Include documents, photos, recordings, videos, and written stories in one collection.",
        "Shared access allows multiple family members to contribute and view the archive.",
        "AI backup systems ensure nothing is ever permanently lost through multiple redundancies.",
        "Family tree integration connects stories and photos to specific people in your lineage.",
        "Search functionality lets anyone find specific stories, people, or events instantly.",
        "Privacy controls determine who can see which parts of the archive.",
        "Regular addition reminders ensure the archive grows over time with new contributions.",
        "Services like Forever.com and FamilySearch provide dedicated family archive platforms.",
        "Your digital archive becomes the most valuable non-financial inheritance you can leave.",
    ]),
    ("Chapter 9: AI Genealogy Research Tools", [
        "AI has revolutionized family history research, making decades of work happen in hours.",
        "Ancestry.com and MyHeritage use AI to search billions of historical records instantly.",
        "DNA testing combined with AI reveals ethnic heritage and connects living relatives.",
        "AI reads old census records, ship manifests, and vital records in any handwriting style.",
        "Family tree AI detects connections and suggests records that might belong to your family.",
        "AI identifies historical context: what was happening in the world when your ancestors lived.",
        "Newspaper archive AI finds mentions of family members in old publications.",
        "Cemetery record AI locates burial sites and connects them to family tree data.",
        "AI suggests which records to search next based on gaps in your family knowledge.",
        "Collaborative family trees let relatives worldwide contribute what they know.",
        "The stories of your ancestors enrich your own story with depth and context.",
        "Even partial genealogy research reveals fascinating connections to history.",
    ]),
    ("Chapter 10: Writing Your Ethical Will with AI Help", [
        "An ethical will passes down your values, beliefs, and life lessons to future generations.",
        "Unlike a legal will that distributes property, an ethical will distributes wisdom.",
        "AI helps you articulate values and beliefs that may be difficult to put into words.",
        "Common topics: what you believe about family, work, faith, love, and resilience.",
        "AI prompts questions you might not think to address on your own.",
        "Lessons from hardship, failure, and loss are often the most valuable to share.",
        "Express gratitude, forgiveness, hopes, and dreams for those who come after you.",
        "AI helps you write separate letters for different family members with personalized messages.",
        "Your ethical will can include practical life advice alongside philosophical reflections.",
        "This document becomes more precious with time as descendants discover it.",
        "There is no right or wrong way to write one - just speak from your heart.",
        "AI simply helps you organize and express what is already inside you.",
    ]),
    ("Chapter 11: AI-Powered Family Cookbook Creation", [
        "Family recipes carry memories, traditions, and love in every ingredient and instruction.",
        "AI helps you document recipes that exist only in your memory or in approximate form.",
        "Voice recording while you cook captures the real way you make beloved dishes.",
        "AI converts approximate measurements (a pinch, a handful) into precise amounts.",
        "Story integration adds the history behind each recipe: who made it, when, and why.",
        "AI formatting creates beautiful recipe pages with consistent layout and clear instructions.",
        "Photo documentation of each dish creates a visual family food heritage.",
        "AI suggests organizing by meal type, occasion, season, or family tradition.",
        "Family members can add their own variations and memories to each recipe.",
        "Print-on-demand services create physical cookbooks from your digital collection.",
        "A family cookbook is one of the most used and treasured inheritance items possible.",
        "Include the imperfect recipes too - the burnt cookies have the best stories.",
    ]),
    ("Chapter 12: Recording Wisdom and Advice with AI", [
        "Your hard-earned wisdom about life, relationships, and work deserves to be heard.",
        "AI helps you organize advice by topic so recipients can find what they need when they need it.",
        "Record advice for specific life moments: first job, marriage, parenthood, grief, retirement.",
        "AI prompts bring out wisdom you have that you might not think to share unprompted.",
        "Video recording adds your facial expressions, gestures, and emotion to the advice.",
        "Short clips (1-3 minutes) are more likely to be watched than long recordings.",
        "AI can compile your advice into a book format with chapters for different life areas.",
        "Include not just what to do, but what you wish you had done differently.",
        "Humor and honesty make advice more memorable and relatable for younger generations.",
        "AI editing polishes your delivery while keeping your authentic personality intact.",
        "Your mistakes and lessons are as valuable as your successes - share both freely.",
        "Imagine a younger version of yourself receiving this advice - what would you say?",
    ]),
    ("Chapter 13: AI Audiobook Creation of Your Story", [
        "Transform your written memoir or stories into an audiobook your family can listen to.",
        "Your own voice reading your story is the most personal and precious format possible.",
        "AI audio editing removes background noise, long pauses, and verbal stumbles.",
        "Chapter markers let listeners navigate directly to stories they want to hear.",
        "AI mastering ensures consistent volume and clarity throughout the recording.",
        "Professional-sounding results are achievable with just a quiet room and your phone.",
        "AI text-to-speech can read portions if your voice becomes fatigued during recording.",
        "Music and sound effects can be added by AI to create atmosphere for your stories.",
        "Distribute via private podcast feeds, USB drives, or CDs for family members.",
        "Listeners can enjoy your stories while driving, walking, or relaxing with eyes closed.",
        "An audiobook of your life story is an extraordinary gift that technology makes simple.",
        "Record one chapter at a time - there is no rush to finish it all at once.",
    ]),
    ("Chapter 14: Sharing Your Legacy Digitally", [
        "Your preserved stories have maximum impact when they reach the people who value them.",
        "Private family websites host your archive in one easily accessible location.",
        "Email distribution of stories, one at a time, creates weekly family connection moments.",
        "Social media sharing reaches extended family you might not see in person regularly.",
        "QR codes on printed photos link to video stories and additional digital content.",
        "Family reunion presentations showcase your archive to gathered loved ones.",
        "Time-capsule features release specific letters or videos on future meaningful dates.",
        "Cloud sharing ensures your archive survives beyond your own lifetime permanently.",
        "AI helps you choose which stories to share with which audience appropriately.",
        "Children and grandchildren may share your stories further with people you never met.",
        "Your legacy grows and impacts more people as it spreads through your family tree.",
        "Digital sharing means geographic distance never prevents connection to your story.",
    ]),
    ("Chapter 15: Your Storytelling Action Plan", [
        "Week 1: Download a voice recording app and record 3 memories (any length, any topic).",
        "Week 2: Scan 10-20 of your most important old photographs using your phone.",
        "Week 3: Use ChatGPT to organize your memories into a rough outline of your story.",
        "Week 4: Write or record one complete chapter about your childhood or family of origin.",
        "Month 2: Continue recording one chapter per week. Scan more photos and documents.",
        "Month 3: Begin AI photo restoration on your most damaged and precious images.",
        "Month 4: Create a family cookbook by recording recipes and their stories.",
        "Month 5: Research your genealogy using AI tools to add ancestral context.",
        "Month 6: Compile everything into a organized digital archive with family access.",
        "Ongoing: Continue adding stories, photos, and wisdom as inspiration strikes.",
        "Remember: Imperfect preservation is infinitely better than perfect silence.",
        "Start with whatever you can, today. Your story is already being lost to time.",
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

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book79_AI_Legacy_Storytelling.pdf")
print("Created Book79_AI_Legacy_Storytelling.pdf")
