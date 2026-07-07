"""
Book 57: AI Creativity Workbook - Learn to Create with AI Tools
KDP Interior - 8.5x11 inches (612x792 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "AI CREATIVITY", font='F2', size=32)
    pdf.add_centered_text(575, "WORKBOOK", font='F2', size=28)
    pdf.add_centered_text(530, "Learn to Create with AI Tools", font='F1', size=18)
    pdf.add_line(150, 500, 462, 500, 2)
    pdf.add_centered_text(465, "20 Hands-On Lessons for Art, Writing & More", font='F4', size=14)
    pdf.add_centered_text(435, "No Experience Needed - Perfect for Ages 45+", font='F4', size=13)
    pdf.add_centered_text(350, "By", font='F1', size=12)
    pdf.add_centered_text(320, "Daniel Tesfamariam", font='F2', size=18)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "AI Creativity Workbook - Learn to Create with AI Tools", font='F2', size=12)
    pdf.add_centered_text(570, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(545, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(515, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(490, "Published via Amazon KDP", font='F1', size=10)

    # --- LESSONS ---
    lessons = [
        ("DALL-E: AI Image Generator", "DALL-E creates images from text descriptions you type.",
         "It is made by OpenAI and is free to try with limited credits.",
         ["Go to labs.openai.com and sign in with your OpenAI account.",
          "Click 'Create' and type a description of the image you want.",
          "Be specific: describe colors, style, mood, and subject.",
          "Click 'Generate' and wait about 15 seconds for your images.",
          "Choose your favorite from the options and click Download."],
         "A peaceful cottage garden with roses at sunset, watercolor style"),
        ("Midjourney: Advanced AI Art", "Midjourney creates stunning artistic images from text prompts.",
         "It works through Discord (a free chat app) and produces beautiful results.",
         ["Download Discord (free) and create an account.",
          "Go to midjourney.com and join their Discord server.",
          "Find a 'newbies' channel and type /imagine followed by your description.",
          "Wait 60 seconds for four image options to appear.",
          "Click U1-U4 to upscale your favorite, or V1-V4 for variations."],
         "A majestic mountain landscape with autumn colors, oil painting style"),
        ("ChatGPT for Creative Writing", "ChatGPT can help you write stories, poems, and creative content.",
         "It works like a collaborative writing partner who never gets tired.",
         ["Go to chat.openai.com and log into your free account.",
          "Start with: 'Help me write a short story about...' and describe your idea.",
          "Ask it to continue, change the tone, or make it longer or shorter.",
          "Request specific styles: 'Write this in the style of a fairy tale.'",
          "Copy your favorite result and edit it to add your personal voice."],
         "Write a heartwarming short story about a grandfather teaching his grandson to fish"),
        ("AI Music Generators", "AI can now compose original music in any style you choose.",
         "Tools like Suno and Udio create full songs from simple descriptions.",
         ["Visit suno.ai and create a free account.",
          "Click 'Create' and describe the music you want in plain English.",
          "Specify genre, mood, and instruments: 'peaceful jazz piano'.",
          "Wait about 30 seconds for the AI to generate your song.",
          "Listen, download, and share your creation with friends and family."],
         "A relaxing acoustic guitar melody perfect for a Sunday morning"),
        ("AI Video Tools", "AI can help you create and edit videos without professional skills.",
         "Tools like Runway and Lumen5 make video creation accessible to everyone.",
         ["Visit lumen5.com and create a free account.",
          "Choose 'Create a video' and paste in text or a blog post.",
          "The AI automatically selects matching images and creates slides.",
          "Customize colors, fonts, and music to match your style.",
          "Export and share your video on social media or with family."],
         "Create a 1-minute video slideshow of my vacation photos with relaxing music"),
        ("Canva AI Design Tools", "Canva is a free design tool that now includes powerful AI features.",
         "You can create cards, posters, social media posts, and presentations.",
         ["Go to canva.com and create a free account.",
          "Click 'Create a design' and choose your format (poster, card, etc).",
          "Use 'Magic Write' to generate text content for your design.",
          "Use 'Text to Image' to create custom artwork for your project.",
          "Download or share your finished design directly from Canva."],
         "Design a birthday party invitation with a garden theme"),
        ("AI Photo Editors", "AI photo editing tools can fix, enhance, and transform your photos.",
         "They can remove backgrounds, fix lighting, and even restore old photos.",
         ["Upload a photo to an AI editor like Pixlr.com or Fotor.com.",
          "Try 'Auto Enhance' to instantly improve colors and lighting.",
          "Use 'Remove Background' to isolate a person from their surroundings.",
          "Try 'Restore Old Photo' to fix damaged or faded vintage photos.",
          "Save your edited photo and compare it with the original."],
         "Enhance and colorize an old black and white family photo"),
        ("AI Presentation Makers", "AI can build professional presentations from just a topic or outline.",
         "Tools like Gamma.app create beautiful slides in minutes, not hours.",
         ["Visit gamma.app and sign up for a free account.",
          "Click 'Create New' and choose 'Presentation'.",
          "Type your topic and let AI generate an outline with suggested content.",
          "Review and customize each slide - change text, images, and layout.",
          "Present directly from the tool or export as a PDF."],
         "Create a 10-slide presentation about the history of my hometown"),
        ("AI Resume Builders", "AI resume tools can help you create a professional resume quickly.",
         "They suggest wording, format your experience, and optimize for job searches.",
         ["Visit an AI resume tool like resume.io or Kickresume.",
          "Enter your work history, skills, and education.",
          "Let the AI suggest improvements to your descriptions.",
          "Choose a professional template that suits your industry.",
          "Download as a PDF ready to send to potential employers."],
         "Create a resume highlighting 20 years of customer service experience"),
        ("AI Email Writers", "AI can draft professional and personal emails in seconds.",
         "Just describe what you want to say and let AI handle the wording.",
         ["Open ChatGPT or use a browser extension like Compose AI.",
          "Describe the email you need: who it is to, the topic, and the tone.",
          "Specify: formal or casual, short or detailed, friendly or professional.",
          "Review the draft and make any personal changes you want.",
          "Copy the text into your email app and send."],
         "Write a polite email to my landlord requesting a maintenance repair"),
        ("AI Recipe Generators", "AI can create custom recipes based on your ingredients and preferences.",
         "Tell it what you have in your kitchen and it will suggest what to cook.",
         ["Open ChatGPT and type what ingredients you have available.",
          "Specify dietary needs: low sodium, diabetic-friendly, vegetarian, etc.",
          "Ask for cooking time and difficulty level you prefer.",
          "Request step-by-step instructions with exact measurements.",
          "Ask for substitutions if you are missing any ingredients."],
         "Create a healthy dinner recipe using chicken, rice, and broccoli for 2 people"),
        ("AI Travel Planners", "AI can plan entire trips tailored to your interests and budget.",
         "It considers your preferences, mobility needs, and schedule.",
         ["Open ChatGPT and describe your dream trip destination and dates.",
          "Specify your budget, mobility needs, and interests.",
          "Ask for a day-by-day itinerary with specific activities.",
          "Request restaurant recommendations and booking tips.",
          "Ask about the best time to visit and what to pack."],
         "Plan a 5-day relaxing trip to Italy for a couple in their 60s who love food and history"),
        ("AI Language Tutors", "AI can teach you a new language at your own pace with infinite patience.",
         "It adapts to your level and lets you practice conversation anytime.",
         ["Open ChatGPT and say 'Teach me basic Spanish conversation'.",
          "Practice by asking it to have a simple conversation in the language.",
          "Ask it to correct your grammar and explain rules simply.",
          "Request vocabulary lists on topics you care about (travel, food, family).",
          "Practice daily for 10 minutes - consistency beats long sessions."],
         "Teach me how to order food at a restaurant in French"),
        ("AI Audiobook Creators", "AI can turn your written content into professional-sounding audiobooks.",
         "Text-to-speech has gotten remarkably natural and easy to use.",
         ["Visit an AI voice tool like ElevenLabs or NaturalReader.",
          "Paste or upload the text you want converted to audio.",
          "Choose a voice style that matches your content (warm, professional).",
          "Preview the audio and adjust speed or pronunciation if needed.",
          "Download the audio file to listen to or share."],
         "Convert my 3-page family history essay into an audiobook with a warm narrator voice"),
        ("AI Greeting Card Makers", "AI can help you design personalized greeting cards for any occasion.",
         "Combine AI-generated art with AI-written messages for unique cards.",
         ["Use Canva or a dedicated card tool with AI features.",
          "Describe the occasion and who the card is for.",
          "Let AI generate artwork or choose from suggestions.",
          "Use AI to write a heartfelt personal message inside.",
          "Print at home or order professional printing online."],
         "Design a sympathy card with a peaceful nature scene and comforting message"),
        ("AI Genealogy Tools", "AI can help you research your family history and build your family tree.",
         "It can interpret old documents and suggest research directions.",
         ["Visit a genealogy site like FamilySearch.org (free) or Ancestry.com.",
          "Enter what you know about your parents and grandparents.",
          "Use AI features to find matches in historical records automatically.",
          "Ask ChatGPT to help interpret old documents or handwriting.",
          "Build a visual family tree to share with relatives."],
         "Help me find information about my great-grandparents who came from Ireland in 1900"),
        ("AI Health Information", "AI can help you understand health topics and prepare for doctor visits.",
         "It explains medical terms simply and helps you ask better questions.",
         ["Ask ChatGPT to explain a medical condition in simple language.",
          "Request a list of questions to ask your doctor at your next visit.",
          "Ask about side effects of medications in plain English.",
          "Use AI to understand your lab results (general education only).",
          "Remember: AI provides information, not medical advice. Always consult your doctor."],
         "Explain what high cholesterol means and what questions I should ask my doctor"),
        ("AI Garden Planners", "AI can design your garden layout based on your climate and preferences.",
         "It knows what grows well together and when to plant each item.",
         ["Tell ChatGPT your location, garden size, and sunlight conditions.",
          "Describe what you want to grow: flowers, vegetables, herbs, or mixed.",
          "Ask for a planting schedule month by month.",
          "Request companion planting suggestions (which plants help each other).",
          "Ask for maintenance tips specific to your plants and region."],
         "Design a small vegetable garden for a sunny backyard in Zone 7"),
        ("AI Home Decorating", "AI can suggest interior design ideas based on your space and style.",
         "Describe your room and preferences for personalized suggestions.",
         ["Describe your room: size, current colors, natural light, and furniture.",
          "Tell the AI your style preference: modern, traditional, cozy, minimalist.",
          "Ask for color palette suggestions that work together.",
          "Request furniture arrangement ideas for better flow.",
          "Ask for budget-friendly ways to refresh a room."],
         "Suggest a cozy living room makeover for a small space with lots of books"),
        ("Final Project: Your AI Creative Portfolio", "Congratulations! You have learned 19 AI creative tools.",
         "Now create your own portfolio combining multiple tools you enjoyed.",
         ["Choose your 3 favorite AI tools from this workbook.",
          "Create one project using each of those 3 tools.",
          "Combine them: an AI image, AI writing, and AI presentation about yourself.",
          "Share your creations with a friend or family member.",
          "Keep exploring - new AI tools are released every month!"],
         "Create a personal 'About Me' page using AI art, AI writing, and AI design"),
    ]

    for i, (title, what_is, detail, steps, sample_prompt) in enumerate(lessons, 1):
        pdf.new_page()
        pdf.add_text(70, 740, f"Lesson {i}", font='F1', size=12)
        pdf.add_text(70, 715, title, font='F2', size=18)
        pdf.add_line(70, 700, 542, 700, 1)

        pdf.add_text(70, 675, f"What is it? {what_is}", font='F4', size=11)
        pdf.add_text(70, 655, detail, font='F4', size=11)

        pdf.add_text(70, 625, "How to use it:", font='F5', size=12)
        y = 605
        for step_num, step in enumerate(steps, 1):
            pdf.add_text(80, y, f"{step_num}. {step}", font='F4', size=11)
            y -= 22

        y -= 15
        pdf.add_text(70, y, "Practice prompt to try:", font='F5', size=12)
        y -= 20
        pdf.add_text(80, y, f'"{sample_prompt}"', font='F3', size=10)

        y -= 35
        pdf.add_text(70, y, "Write your own prompt:", font='F5', size=12)
        y -= 20
        for j in range(3):
            pdf.add_line(80, y, 540, y, 0.5, gray=0.5)
            y -= 22

        y -= 15
        pdf.add_text(70, y, "Paste or describe your result:", font='F5', size=12)
        y -= 5
        pdf.add_rect(80, y - 80, 460, 80, line_width=0.5, gray=0.3)

        y -= 100
        pdf.add_text(70, y, "Rate your result:   1    2    3    4    5   (circle one)", font='F1', size=11)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book57_AI_Creativity_Workbook.pdf')
    print("Book 57 created: Book57_AI_Creativity_Workbook.pdf")

if __name__ == '__main__':
    create_book()
