"""
Book 65: How To Start A Podcast - The Complete Beginner's Guide
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "HOW TO START A PODCAST", font='F2', size=22)
    pdf.add_centered_text(485, "The Complete Beginner's Guide", font='F1', size=14)
    pdf.add_line(80, 460, 352, 460, 2)
    pdf.add_centered_text(420, "Launch, Grow, and Monetize", font='F4', size=13)
    pdf.add_centered_text(398, "Your Show from Day One", font='F4', size=13)
    pdf.add_centered_text(330, "By", font='F1', size=12)
    pdf.add_centered_text(305, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "How To Start A Podcast", font='F2', size=11)
    pdf.add_centered_text(475, "The Complete Beginner's Guide", font='F1', size=10)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(390, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(365, "Published via Amazon KDP", font='F1', size=10)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: What is a Podcast?", [
            "A podcast is an audio show that people can listen to anytime, anywhere.",
            "Think of it like a radio show that listeners download or stream on demand.",
            "Podcasts are free to create and free for listeners to enjoy.",
            "There are over four million podcasts covering every topic imaginable.",
            "Listeners subscribe and automatically receive new episodes when published.",
            "People listen during commutes, workouts, cooking, and before sleep.",
            "Podcasts range from five-minute daily shows to three-hour conversations.",
            "You can podcast solo, with a co-host, or by interviewing guests.",
            "The barrier to entry is low: a microphone and free software is all you need.",
            "Podcasting builds deep connections with audiences unlike any other medium.",
            "Many podcasters turn their shows into full-time careers and businesses.",
            "This book will guide you from idea to published episode step by step.",
        ]),
        ("Chapter 2: Choosing Your Niche/Topic", [
            "Your niche should be specific enough to attract a dedicated audience.",
            "A show about cooking is too broad. A show about one-pot meals is better.",
            "Choose a topic you can talk about passionately for years, not months.",
            "Research existing podcasts in your topic to find gaps you can fill.",
            "The best niches combine your expertise with audience demand.",
            "Consider who your ideal listener is and what problems they have.",
            "True crime, business, comedy, health, and self-improvement are popular categories.",
            "Niche down first, then expand once you build an audience.",
            "Ask yourself: can I create fifty episodes on this topic without running out?",
            "Your unique perspective and personality make you different from competitors.",
            "Test your idea by listing twenty episode topics. If you struggle, pick another niche.",
            "The most successful podcasts solve a specific problem for a specific audience.",
        ]),
        ("Chapter 3: Naming Your Podcast", [
            "Your podcast name should clearly communicate what the show is about.",
            "Include a keyword that helps people find you when searching for your topic.",
            "Keep the name short, memorable, and easy to spell when heard aloud.",
            "Avoid inside jokes, puns, or clever names that confuse new listeners.",
            "Check that the name is not already taken on Apple Podcasts and Spotify.",
            "Search for available domain names and social media handles to match.",
            "Consider adding a subtitle that explains the show for clarity.",
            "Example: The Budget Mom: Practical Tips for Saving Money Every Day.",
            "Say the name out loud ten times. Does it feel natural and professional?",
            "Ask friends and family if the name communicates what the show is about.",
            "You can always rebrand later but it is easier to choose well from the start.",
            "Write down ten to twenty options and narrow down to your top three choices.",
        ]),
        ("Chapter 4: Equipment You Need (Budget Options)", [
            "You can start with just your smartphone and a free recording app.",
            "For better quality, the Audio-Technica ATR2100x microphone costs about 70 dollars.",
            "The Samson Q2U is another excellent budget USB microphone around 60 dollars.",
            "USB microphones plug directly into your computer with no extra equipment.",
            "A pop filter for 10-15 dollars reduces harsh sounds on letters like P and B.",
            "Use earbuds or headphones to monitor your audio while recording.",
            "Record in a quiet room with soft surfaces like carpet, curtains, and pillows.",
            "A closet full of clothes makes an excellent free recording booth.",
            "You do not need expensive soundproofing panels when starting out.",
            "A simple microphone stand or boom arm keeps the mic at mouth level.",
            "Total budget setup: under 100 dollars for professional-sounding audio.",
            "Upgrade equipment only after you have consistently published for three months.",
        ]),
        ("Chapter 5: Recording Software Setup", [
            "Audacity is free, open-source recording software for Mac and Windows.",
            "GarageBand comes free on every Mac and is beginner-friendly for podcasting.",
            "Download and install your chosen software before your first recording session.",
            "Connect your USB microphone and select it as the input device in settings.",
            "Set your recording format to WAV or AIFF for highest quality during recording.",
            "Test your levels: speak at normal volume and aim for peaks around minus 6 dB.",
            "Record a test segment and listen back to check for background noise.",
            "Close other applications that might create notification sounds while recording.",
            "Save your project file immediately so you do not lose work accidentally.",
            "Create a folder structure to organize episode recordings by number and date.",
            "For remote interviews, Riverside.fm and Zencastr record each person separately.",
            "Practice with your software before recording your actual first episode.",
        ]),
        ("Chapter 6: Recording Your First Episode", [
            "Write a simple outline with bullet points rather than a word-for-word script.",
            "Speaking from notes sounds natural while reading a script sounds robotic.",
            "Start with a brief introduction: who you are and what the show is about.",
            "Record your intro episode explaining why you started and what listeners will gain.",
            "Speak as if you are talking to one friend, not a large audience.",
            "It is normal to feel awkward at first. Everyone improves with practice.",
            "If you make a mistake, pause for three seconds then re-say the sentence.",
            "The pause makes it easy to find and remove mistakes during editing.",
            "Aim for episodes between twenty and forty-five minutes when starting.",
            "Record in a consistent position and distance from the microphone each time.",
            "Drink water before and during recording to keep your voice clear.",
            "Your first episode will not be perfect and that is completely okay.",
        ]),
        ("Chapter 7: Editing Basics", [
            "Editing removes mistakes, long pauses, and filler words from your recording.",
            "In Audacity, use the selection tool to highlight sections you want to delete.",
            "Remove obvious mistakes, ums, long silences, and off-topic tangents.",
            "Do not over-edit. Some natural pauses and imperfections sound authentic.",
            "Add your intro music at the beginning and outro music at the end.",
            "Use royalty-free music from sites like Epidemic Sound or Free Music Archive.",
            "Normalize your audio so the volume is consistent throughout the episode.",
            "Apply noise reduction to remove background hum or fan noise.",
            "Export your final file as MP3 at 128kbps which is standard for podcasts.",
            "Name your file clearly: episode number, title, and date for easy organization.",
            "Editing a thirty-minute episode typically takes sixty to ninety minutes.",
            "As you improve at recording, editing time decreases significantly.",
        ]),
        ("Chapter 8: Creating Cover Art", [
            "Your cover art is the first thing potential listeners see on podcast apps.",
            "Apple requires artwork to be 3000 by 3000 pixels in JPG or PNG format.",
            "Use bold, readable text that is visible even as a tiny thumbnail.",
            "Choose contrasting colors that stand out among other podcast covers.",
            "Include your podcast name prominently and a brief tagline if space allows.",
            "Avoid small text, busy backgrounds, or photos that are hard to see small.",
            "Canva offers free podcast cover art templates that look professional.",
            "Keep the design simple and clean. Less is more with small thumbnails.",
            "Look at top podcasts in your category for design inspiration.",
            "Your face or a relevant icon helps listeners recognize your show quickly.",
            "Hire a designer on Fiverr for 20-50 dollars if you want custom artwork.",
            "You can update your cover art later but a good first impression matters.",
        ]),
        ("Chapter 9: Choosing a Hosting Platform", [
            "A podcast host stores your audio files and delivers them to all platforms.",
            "You cannot upload directly to Apple or Spotify. You need a hosting service.",
            "Buzzsprout is beginner-friendly with a free plan for up to two hours monthly.",
            "Anchor (now Spotify for Podcasters) is completely free with unlimited hosting.",
            "Podbean offers affordable plans starting at nine dollars per month.",
            "Libsyn is an industry standard trusted by professional podcasters.",
            "Your host provides an RSS feed which is the URL that connects to all apps.",
            "Consider features like analytics, website, monetization tools, and ease of use.",
            "Upload your edited MP3 file, add episode title, description, and publish.",
            "Most hosts also generate a basic website for your podcast automatically.",
            "Reliable hosting ensures your episodes are always available to listeners.",
            "Start with a free plan and upgrade as your audience and needs grow.",
        ]),
        ("Chapter 10: Submitting to Apple/Spotify", [
            "Apple Podcasts and Spotify together reach over 80 percent of podcast listeners.",
            "Submit to Apple Podcasts through Apple Podcasts Connect at podcastsconnect.apple.com.",
            "You need an Apple ID to submit. Create a free one if you do not have one.",
            "Paste your RSS feed URL from your hosting platform into the submission form.",
            "Apple reviews new podcasts which takes between 24 hours and two weeks.",
            "For Spotify, submit through Spotify for Podcasters or your hosting platform.",
            "Most hosting platforms like Buzzsprout can submit to Spotify for you automatically.",
            "Also submit to Google Podcasts, Amazon Music, and iHeartRadio for full coverage.",
            "Have at least one episode published before submitting to directories.",
            "Some podcasters launch with three episodes so new listeners have content immediately.",
            "Once approved, your podcast is available to millions of potential listeners.",
            "Check that your show appears correctly with proper artwork and descriptions.",
        ]),
        ("Chapter 11: Writing Show Notes", [
            "Show notes are the text description that accompanies each episode.",
            "They help with discoverability since podcast apps search text, not audio.",
            "Start with a compelling one to two sentence summary of the episode topic.",
            "Include timestamps for key topics so listeners can jump to sections they want.",
            "List any resources, books, tools, or websites mentioned during the episode.",
            "Add links to your social media and website for listeners who want more.",
            "Include a call to action: subscribe, leave a review, or visit your website.",
            "Use relevant keywords naturally in your show notes for search optimization.",
            "Keep formatting simple since different apps display notes differently.",
            "Write show notes before recording to serve as your episode outline.",
            "Include guest bios and links when you have interview episodes.",
            "Good show notes take ten minutes to write and significantly boost discoverability.",
        ]),
        ("Chapter 12: Growing Your Audience", [
            "Consistency is the number one factor in podcast growth. Publish on schedule.",
            "Choose a realistic schedule: weekly is ideal but biweekly works too.",
            "Ask listeners to subscribe and leave reviews at the end of every episode.",
            "Share new episodes on all your social media platforms consistently.",
            "Create short audio or video clips from episodes to share on social media.",
            "Guest on other podcasts in your niche to reach new audiences.",
            "Invite guests who have their own audience and will share the episode.",
            "Engage with listeners through social media, email, and community groups.",
            "Collaborate with other podcasters for cross-promotion episodes.",
            "Optimize your show title and descriptions with searchable keywords.",
            "Ask listeners what topics they want covered and deliver on their requests.",
            "Growth is slow at first. Most successful podcasts took one to two years to build.",
        ]),
        ("Chapter 13: Monetization Options", [
            "Sponsorships pay you to mention products or services during your episodes.",
            "You typically need 1000-5000 downloads per episode to attract sponsors.",
            "CPM rates (cost per thousand listeners) range from 15-50 dollars for podcasts.",
            "Affiliate marketing earns commission when listeners buy through your links.",
            "Amazon Associates and other programs let you earn on product recommendations.",
            "Sell your own products or services that align with your podcast topic.",
            "Offer premium content through Patreon or Apple Podcast Subscriptions.",
            "Coaching, consulting, or courses can be marketed through your podcast.",
            "Listener donations through platforms like Buy Me a Coffee supplement income.",
            "Merchandise like t-shirts and mugs works for podcasts with loyal fan bases.",
            "Do not focus on monetization until you have a consistent audience first.",
            "Multiple small revenue streams add up to significant podcast income over time.",
        ]),
        ("Chapter 14: Interview Tips", [
            "Research your guest thoroughly before the interview. Listen to their other appearances.",
            "Prepare ten to fifteen questions but be flexible to follow interesting tangents.",
            "Start with easy warm-up questions to make your guest comfortable.",
            "Ask open-ended questions that begin with how, why, or tell me about.",
            "Listen actively and ask follow-up questions based on their answers.",
            "Avoid yes-or-no questions that kill conversation momentum.",
            "Let your guest finish speaking. Do not interrupt even if you are excited.",
            "Record a brief pre-interview chat to test audio levels and build rapport.",
            "Send guests a few topics in advance but not the exact questions.",
            "Keep the energy conversational rather than formal like a news interview.",
            "Thank your guest genuinely and make it easy for them to share the episode.",
            "Great interviews feel like fascinating conversations, not interrogations.",
        ]),
        ("Chapter 15: Your Launch Checklist", [
            "One month before: finalize your concept, name, and cover art design.",
            "Three weeks before: purchase and set up your recording equipment.",
            "Two weeks before: record and edit your first three episodes.",
            "Ten days before: set up your hosting account and upload episodes.",
            "One week before: submit your RSS feed to Apple Podcasts and Spotify.",
            "Five days before: write show notes and create social media announcements.",
            "Three days before: tell friends and family about your launch date.",
            "Launch day: publish all three episodes and announce everywhere.",
            "Ask everyone you know to subscribe, listen, and leave a review.",
            "First week: share daily on social media and engage with any feedback.",
            "First month: publish on your consistent schedule without missing a week.",
            "Celebrate your launch! Most people talk about starting but never actually do it.",
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

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book65_How_To_Start_Podcast.pdf')
    print("Book 65 created: Book65_How_To_Start_Podcast.pdf")

if __name__ == '__main__':
    create_book()
