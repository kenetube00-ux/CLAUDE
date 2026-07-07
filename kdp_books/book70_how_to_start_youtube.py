"""
Book 70: How To Start A YouTube Channel - Grow from 0 to 1000 Subscribers
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "HOW TO START A", font='F2', size=22)
    pdf.add_centered_text(490, "YOUTUBE CHANNEL", font='F2', size=22)
    pdf.add_centered_text(455, "Grow from 0 to 1000 Subscribers", font='F1', size=14)
    pdf.add_line(80, 430, 352, 430, 2)
    pdf.add_centered_text(390, "Create Content, Build an Audience,", font='F4', size=13)
    pdf.add_centered_text(368, "and Turn Your Passion Into Income", font='F4', size=13)
    pdf.add_centered_text(300, "By", font='F1', size=12)
    pdf.add_centered_text(275, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "How To Start A YouTube Channel", font='F2', size=11)
    pdf.add_centered_text(475, "Grow from 0 to 1000 Subscribers", font='F1', size=10)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(390, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(365, "Published via Amazon KDP", font='F1', size=10)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: Why Start a YouTube Channel", [
            "YouTube has over 2 billion monthly active users watching content every day.",
            "It is the second largest search engine after Google, owned by Google itself.",
            "YouTube content is evergreen: videos you post today can earn views for years.",
            "Unlike social media posts that disappear, YouTube videos compound in value over time.",
            "You can monetize through ads, sponsorships, products, and affiliate marketing.",
            "YouTube builds authority in your niche that transfers to other business opportunities.",
            "The platform is free to use as both a creator and a viewer.",
            "Video builds trust and connection with audiences faster than any other medium.",
            "Many full-time YouTubers started as a side hobby recording in their bedrooms.",
            "A channel with 1000 subscribers can generate meaningful income and opportunities.",
            "There is still massive opportunity for new creators who bring unique perspectives.",
            "This book will get you from zero to your first 1000 subscribers systematically.",
        ]),
        ("Chapter 2: Choosing Your Niche", [
            "Your niche is the specific topic your channel consistently creates content about.",
            "Choose a niche you can create content about weekly for at least two years.",
            "Passion matters but profitability matters too. Find the intersection of both.",
            "Research existing channels in your topic. Competition validates demand exists.",
            "Look for underserved angles: specific audiences, unique formats, or fresh perspectives.",
            "Profitable niches include finance, technology, health, business, and education.",
            "Hobby niches like cooking, gaming, crafts, and fitness build loyal communities.",
            "Avoid being too broad. A cooking channel for busy parents beats a general food channel.",
            "Your niche should be specific enough to attract subscribers but broad enough for content.",
            "Study small channels (1K-10K subs) in your niche to see what works for starters.",
            "List 50 video ideas for your chosen niche. If you struggle, it may be too narrow.",
            "You can always adjust your niche later but starting focused helps algorithms recommend you.",
        ]),
        ("Chapter 3: Setting Up Your Channel", [
            "Create a Google account dedicated to your YouTube channel if you prefer separation.",
            "Go to youtube.com and click Create a Channel to start your setup process.",
            "Choose a channel name that is memorable, searchable, and reflects your content.",
            "Write a channel description explaining what you make and who it helps.",
            "Include keywords in your description that people might search for.",
            "Create a channel banner (2560 x 1440 pixels) using Canva free templates.",
            "Upload a professional-looking profile picture, ideally a clear photo of your face.",
            "Add links to your social media and website in the channel About section.",
            "Create a channel trailer: a 60-second video telling new visitors what to expect.",
            "Set up channel sections to organize your videos by topic or series.",
            "Verify your account by phone to unlock features like custom thumbnails.",
            "Complete every section of your channel setup before publishing your first video.",
        ]),
        ("Chapter 4: Equipment on a Budget", [
            "Your smartphone camera is good enough to start a YouTube channel today.",
            "Modern phones shoot in 1080p or 4K which exceeds YouTube quality requirements.",
            "Audio quality matters more than video quality. Invest in a microphone first.",
            "A lavalier (clip-on) microphone for your phone costs 15-25 dollars and sounds great.",
            "The Rode NT-USB Mini is an excellent desktop microphone for about 100 dollars.",
            "Natural window light is free and produces flattering results for talking head videos.",
            "Position yourself facing a window with the light on your face, not behind you.",
            "A ring light costs 30-50 dollars and provides consistent lighting any time of day.",
            "A simple tripod or phone mount keeps your camera steady during recording.",
            "Background matters: choose a clean, uncluttered area or use a simple backdrop.",
            "Total starter budget: under 50 dollars using your phone and a clip-on microphone.",
            "Upgrade equipment only after you have published consistently for three months.",
        ]),
        ("Chapter 5: Filming Your First Video", [
            "Your first video does not need to be perfect. It needs to exist.",
            "Choose a topic you know well so you can speak confidently without extensive prep.",
            "Write a simple outline with three to five main points you want to cover.",
            "Set up your filming space with good lighting and minimal background distractions.",
            "Frame yourself from the chest up with your eyes in the upper third of the frame.",
            "Look directly at the camera lens, not the screen, to create eye contact with viewers.",
            "Speak to one imaginary person, not an audience. This creates natural conversation.",
            "If you make a mistake, pause and re-say the sentence. Edit it out later.",
            "Keep your first video between five and ten minutes. Do not over-explain.",
            "Film a short intro, deliver your content, and end with a clear call to action.",
            "Record more footage than you need. You can always cut in editing.",
            "Hit record and start talking. The hardest part is pressing the button.",
        ]),
        ("Chapter 6: Editing Basics (Free Tools)", [
            "DaVinci Resolve is professional editing software that is completely free.",
            "iMovie comes free on Mac and is perfect for beginners with simple projects.",
            "CapCut is free on mobile and desktop with excellent auto-caption features.",
            "Import your footage, trim the beginning and end, and remove obvious mistakes.",
            "Cut out long pauses, ums, ahs, and tangents that do not add value.",
            "Add simple text on screen to emphasize key points during your video.",
            "Include background music at low volume to fill silence and add energy.",
            "Use royalty-free music from YouTube Audio Library which is free for creators.",
            "Add jump cuts to remove dead space and keep the pacing energetic.",
            "Export at 1080p resolution for the best balance of quality and file size.",
            "Editing a ten-minute video takes one to three hours when you are starting out.",
            "Speed improves dramatically with practice. Your tenth edit will be twice as fast.",
        ]),
        ("Chapter 7: Writing Titles That Get Clicks", [
            "Your title is the single biggest factor determining whether people click your video.",
            "Include the main keyword or search term at the beginning of your title.",
            "Create curiosity or promise a clear benefit that makes people want to click.",
            "Use numbers when possible: 5 Tips, 3 Mistakes, 10 Ways gives clear expectations.",
            "Keep titles under 60 characters so they display fully on all devices.",
            "Study viral videos in your niche and analyze what makes their titles compelling.",
            "How to titles work well for educational content targeting people with problems.",
            "Avoid clickbait that does not deliver. Viewers leave quickly and hurt your ranking.",
            "Test different title styles and track which ones get better click-through rates.",
            "Include emotional words: amazing, shocking, essential, complete, ultimate.",
            "Your title and thumbnail work together as a unit to convince people to click.",
            "Write five title options for each video and choose the strongest one.",
        ]),
        ("Chapter 8: Thumbnail Design Secrets", [
            "Thumbnails are the visual advertisement for every video. They must grab attention.",
            "Use a close-up face with a clear expression: surprise, excitement, or curiosity.",
            "Faces with emotions get significantly more clicks than thumbnails without faces.",
            "Add three to five words of large, bold text that complements your title.",
            "Do not repeat the exact title text. Use different words that add context.",
            "Use high-contrast colors that stand out against YouTube's white interface.",
            "Yellow, red, and bright green backgrounds perform well in testing.",
            "Keep the design simple. If it is not readable at the size of a postage stamp, simplify.",
            "Use Canva's free YouTube thumbnail templates as starting points.",
            "Maintain a consistent style across thumbnails so your content is recognizable.",
            "Look at your video page and ask: does my thumbnail stand out among competitors?",
            "A-B test thumbnails by changing them after a few days if performance is low.",
        ]),
        ("Chapter 9: YouTube SEO and Tags", [
            "YouTube SEO helps your videos appear when people search for your topic.",
            "Research keywords using YouTube search suggestions: type your topic and note suggestions.",
            "Include your main keyword in the title, description, and spoken in the video.",
            "YouTube automatically transcribes videos so mentioning keywords verbally helps ranking.",
            "Write descriptions of at least 200 words including relevant keywords naturally.",
            "Add timestamps in your description which helps both viewers and search algorithms.",
            "Use 5-10 relevant tags including your main keyword and related variations.",
            "Tags are less important than title and description but still contribute to discovery.",
            "Hashtags in your description (3-5 maximum) help categorize your content.",
            "Your first 48 hours of performance heavily influence long-term ranking.",
            "Encourage comments and engagement which signal to YouTube that your content has value.",
            "Watch time is the most important ranking factor: make content people watch completely.",
        ]),
        ("Chapter 10: Upload Schedule and Consistency", [
            "Consistency matters more than frequency. One video weekly beats random uploads.",
            "Choose a realistic schedule you can maintain for months without burning out.",
            "Publishing on the same day and time trains your audience to expect new content.",
            "YouTube rewards consistent channels with more recommendations to new viewers.",
            "Batch filming multiple videos in one session saves setup time and creates a buffer.",
            "Film two to three weeks ahead so you always have content ready to publish.",
            "Quality should never be sacrificed for quantity. One great video beats three mediocre ones.",
            "Use YouTube Studio to schedule uploads in advance for consistent publish times.",
            "Announce your schedule in your videos so viewers know when to return.",
            "If you miss a week, do not quit. Just publish the next scheduled video on time.",
            "Most successful creators started with once weekly and increased as they grew.",
            "Twelve consistent months of weekly uploads is the foundation of channel growth.",
        ]),
        ("Chapter 11: Growing Your First 100 Subscribers", [
            "Your first 100 subscribers are the hardest because you have no momentum yet.",
            "Tell everyone you know about your channel: friends, family, coworkers, classmates.",
            "Share your videos on relevant Reddit communities, forums, and Facebook groups.",
            "Comment thoughtfully on larger channels in your niche. Do not spam links.",
            "People who see your helpful comments will check your channel out of curiosity.",
            "Collaborate with other small creators for cross-promotion to each other's audiences.",
            "Answer questions on Quora and include your video link when genuinely relevant.",
            "Create short-form content (YouTube Shorts) that gets recommended more easily.",
            "Shorts can go viral and drive subscribers to your long-form content quickly.",
            "Optimize your channel page so first-time visitors immediately subscribe.",
            "Ask for subscribers at the end of every video with a specific reason to subscribe.",
            "Celebrate every milestone: first subscriber, first comment, first 10, first 50, first 100.",
        ]),
        ("Chapter 12: Engaging with Your Community", [
            "Reply to every comment on your videos, especially in the early growth phase.",
            "Responding to comments signals to YouTube that your video has active engagement.",
            "Heart comments from viewers to acknowledge them even when you cannot reply to all.",
            "Ask questions in your videos to encourage viewers to leave comments.",
            "Create community posts (polls, updates, questions) to stay visible between uploads.",
            "Use the community tab to ask what content your audience wants next.",
            "Pin a comment on each video with a question or additional resource link.",
            "Acknowledge recurring commenters by name to build personal connections.",
            "Create a Discord server or Facebook group for your most engaged viewers.",
            "Go live occasionally to interact with your audience in real time.",
            "Loyal community members become your biggest promoters who share your content.",
            "Building genuine relationships with viewers matters more than any algorithm hack.",
        ]),
        ("Chapter 13: Monetization Requirements", [
            "YouTube Partner Program requires 1000 subscribers and 4000 watch hours in 12 months.",
            "Alternatively, you need 1000 subscribers and 10 million Shorts views in 90 days.",
            "Once accepted, you earn revenue from ads that play before and during your videos.",
            "Average CPM (payment per 1000 ad views) ranges from 2 to 15 dollars depending on niche.",
            "Finance, business, and technology niches earn the highest ad revenue per view.",
            "You do not need monetization to earn money. Affiliate links work from day one.",
            "Promote relevant products in descriptions and earn commission on sales.",
            "Sponsors will approach you even before 1000 subscribers if your niche is valuable.",
            "Sell your own digital products, courses, or services to your audience.",
            "Super Chats during live streams let viewers pay to highlight their messages.",
            "Channel memberships offer monthly subscription perks to your loyal viewers.",
            "Diversify income streams so you never depend solely on YouTube ad revenue.",
        ]),
        ("Chapter 14: Avoiding Burnout", [
            "Creator burnout is real and has caused many talented YouTubers to quit permanently.",
            "Set boundaries between content creation and personal life from the beginning.",
            "Batch create content so you have a buffer and never feel behind schedule.",
            "Take planned breaks and communicate them to your audience. They will understand.",
            "Do not read negative comments obsessively. Most criticism is not constructive.",
            "Avoid comparing your growth to other creators who started at different times.",
            "Remember your original motivation for starting. Reconnect with that purpose regularly.",
            "Delegate tasks you dislike: editing, thumbnails, or descriptions can be outsourced.",
            "Celebrate small wins instead of only focusing on the subscriber count.",
            "Connect with other creators who understand the unique challenges you face.",
            "Protect your mental health. No video is worth sacrificing your well-being.",
            "Sustainable, enjoyable creation for years beats intense burnout in six months.",
        ]),
        ("Chapter 15: Your 90-Day Growth Plan", [
            "Days 1-7: Set up your channel completely. Film and publish your first two videos.",
            "Days 8-14: Publish video three and four. Share on social media and ask for feedback.",
            "Days 15-21: Analyze your first videos' analytics. Note what got the most watch time.",
            "Days 22-30: Publish videos five through eight. Begin experimenting with Shorts.",
            "Month 1 goal: 8 long-form videos published, channel fully optimized.",
            "Days 31-45: Focus on titles and thumbnails. Study what makes viewers click.",
            "Days 46-60: Engage in communities, comment on other channels, and collaborate.",
            "Month 2 goal: 12 total videos, improving quality, beginning community engagement.",
            "Days 61-75: Double down on content that performed best. Create related series.",
            "Days 76-90: Analyze all data. Refine your content strategy based on what works.",
            "Month 3 goal: 20+ videos published, clear content strategy, growing momentum.",
            "After 90 days of consistent effort, you will have a foundation for long-term growth.",
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

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book70_How_To_Start_YouTube.pdf')
    print("Book 70 created: Book70_How_To_Start_YouTube.pdf")

if __name__ == '__main__':
    create_book()
