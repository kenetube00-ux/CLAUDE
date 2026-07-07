"""
Book 60: Large Print Tech Dictionary - 200+ Terms Explained Simply
KDP Interior - 8.5x11 inches (612x792 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "LARGE PRINT", font='F2', size=28)
    pdf.add_centered_text(575, "TECH DICTIONARY", font='F2', size=32)
    pdf.add_centered_text(530, "200+ Terms Explained Simply", font='F1', size=18)
    pdf.add_line(150, 500, 462, 500, 2)
    pdf.add_centered_text(465, "Plain English Definitions for Everyday Technology", font='F4', size=14)
    pdf.add_centered_text(435, "Large Font for Easy Reading | Perfect for Ages 45+", font='F4', size=13)
    pdf.add_centered_text(350, "By", font='F1', size=12)
    pdf.add_centered_text(320, "Daniel Tesfamariam", font='F2', size=18)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "Large Print Tech Dictionary - 200+ Terms Explained Simply", font='F2', size=12)
    pdf.add_centered_text(570, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(545, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(515, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(490, "Published via Amazon KDP", font='F1', size=10)

    # --- HOW TO USE THIS BOOK ---
    pdf.new_page()
    pdf.add_centered_text(720, "HOW TO USE THIS BOOK", font='F2', size=20)
    pdf.add_line(150, 700, 462, 700, 1)

    how_to = [
        "This dictionary is designed to help you understand technology",
        "terms you hear every day - on the news, from family, or online.",
        "",
        "Each term is explained in plain, simple English.",
        "No technical jargon. No complicated explanations.",
        "",
        "Terms are organized alphabetically so you can quickly find",
        "any word you need to look up.",
        "",
        "The large print format makes reading comfortable and easy.",
        "",
        "Keep this book next to your computer or phone for quick",
        "reference whenever you encounter an unfamiliar tech term.",
        "",
        "You do not need to read this cover to cover. Use it like",
        "a regular dictionary - look up words as you need them!",
    ]
    y = 660
    for line in how_to:
        if line == "":
            y -= 8
        else:
            pdf.add_text(80, y, line, font='F4', size=13)
            y -= 24

    # --- TERMS (200 terms, 8 per page = 25 pages) ---
    terms = [
        ("AI (Artificial Intelligence)", "Computer programs that can learn, make decisions, and solve problems - like a very smart assistant."),
        ("Algorithm", "A set of step-by-step instructions that tells a computer how to solve a problem or complete a task."),
        ("Android", "A type of operating system for smartphones made by Google. Used on Samsung, Pixel, and other phones."),
        ("App", "Short for application. A program on your phone or tablet that does a specific job, like email or maps."),
        ("Attachment", "A file (photo, document) that you send along with an email message."),
        ("Backup", "A copy of your important files stored somewhere safe in case the original is lost or damaged."),
        ("Bandwidth", "How much data can travel through your internet connection at once. More bandwidth means faster internet."),
        ("Bluetooth", "A wireless technology that connects devices over short distances, like headphones to your phone."),
        ("Bookmark", "A saved link to a website so you can find it quickly again later, like a browser's favorites list."),
        ("Browser", "The program you use to visit websites. Examples: Chrome, Safari, Firefox, or Edge."),
        ("Bug", "An error or mistake in a computer program that causes it to work incorrectly."),
        ("Cache", "Temporary files stored on your device to help websites and apps load faster next time you visit."),
        ("Chatbot", "A computer program that can have a text conversation with you, like a virtual assistant."),
        ("ChatGPT", "A popular AI tool by OpenAI that answers questions and writes text in a conversational way."),
        ("Click", "Pressing a button on your mouse or tapping on a touchscreen to select something."),
        ("Cloud", "Storing your files on the internet instead of on your device, so you can access them from anywhere."),
        ("Cookie", "A small file websites save on your computer to remember your preferences and login information."),
        ("Copy and Paste", "Copying text or images from one place and inserting them somewhere else on your device."),
        ("Cursor", "The blinking line or arrow on your screen that shows where you are typing or pointing."),
        ("Cybersecurity", "Protecting your devices, accounts, and personal information from hackers and online threats."),
        ("Dashboard", "A main screen that shows you important information at a glance, like a car's instrument panel."),
        ("Data", "Any information stored or processed by a computer - text, numbers, photos, videos, etc."),
        ("Database", "An organized collection of information stored on a computer that can be searched and sorted."),
        ("Desktop", "The main screen you see when your computer starts up, where your icons and files are displayed."),
        ("Digital", "Information stored as numbers (ones and zeros) rather than physical form. Opposite of analog."),
        ("Download", "Copying a file from the internet to your device so you can use it without being online."),
        ("Drag and Drop", "Clicking on something, holding the mouse button, moving it somewhere else, and releasing."),
        ("Email", "Electronic mail - messages sent over the internet instead of through the postal service."),
        ("Emoji", "Small pictures or symbols you can add to text messages and emails to express emotions."),
        ("Encryption", "Scrambling your data so only authorized people can read it - like a secret code for your information."),
        ("Ethernet", "A wired internet connection using a cable plugged directly into your computer for fast, stable internet."),
        ("FAQ", "Frequently Asked Questions - a list of common questions and answers about a product or service."),
        ("File", "A single item stored on your computer - could be a document, photo, video, or program."),
        ("Firewall", "A security barrier that protects your computer from unauthorized access through the internet."),
        ("Flash Drive", "A small portable device you plug into your computer's USB port to store and transfer files."),
        ("Folder", "A container on your computer that holds files, just like a physical folder holds papers."),
        ("Font", "The style and design of the letters and text displayed on your screen or in a document."),
        ("GPS", "Global Positioning System - technology in your phone that knows your exact location for maps and directions."),
        ("Graphics", "Images, pictures, and visual elements displayed on a screen."),
        ("Hacker", "Someone who breaks into computer systems illegally to steal data or cause damage."),
        ("Hard Drive", "The part of your computer that permanently stores all your files, programs, and operating system."),
        ("Hardware", "The physical parts of a computer you can touch - the screen, keyboard, mouse, and tower."),
        ("Hashtag", "A word with # in front of it used on social media to label and find posts about a topic."),
        ("HDMI", "A cable that connects your device to a TV or monitor to display video and play audio."),
        ("Homepage", "The main page of a website, or the first page your browser shows when you open it."),
        ("Hotspot", "Using your phone as a portable WiFi source so other devices can connect to the internet."),
        ("Icon", "A small picture on your screen that represents a program, file, or function you can click."),
        ("Inbox", "The main folder in your email where new messages arrive and wait to be read."),
        ("Instagram", "A social media app for sharing photos and short videos with friends and followers."),
        ("Internet", "The global network of connected computers that allows you to access websites, email, and more."),
        ("iOS", "The operating system that runs on iPhones and iPads, made by Apple."),
        ("IP Address", "A unique number assigned to your device on the internet, like a mailing address for your computer."),
        ("ISP", "Internet Service Provider - the company that provides your home internet connection (Comcast, AT&T, etc)."),
        ("JPEG", "A common format for saving photographs and images on computers and phones."),
        ("Junk Mail", "Unwanted email messages, also called spam - usually advertisements or scams."),
        ("Keyboard Shortcut", "Pressing two or more keys together to do something quickly, like Ctrl+C to copy text."),
        ("LAN", "Local Area Network - computers connected together in one location, like your home network."),
        ("Laptop", "A portable computer with a built-in screen, keyboard, and battery that you can carry around."),
        ("Link", "Clickable text or image on a website that takes you to another page or website when clicked."),
        ("Login", "Entering your username and password to access your account on a website or device."),
        ("Malware", "Harmful software designed to damage your device, steal information, or cause problems."),
        ("Memory (RAM)", "Your computer's short-term workspace that holds information while programs are running."),
        ("Menu", "A list of options or commands you can choose from in a program, usually at the top of the screen."),
        ("Modem", "A device that connects your home to the internet through your phone or cable line."),
        ("Monitor", "The screen you look at when using a desktop computer. Similar to a TV but for your computer."),
        ("Network", "Two or more computers or devices connected together to share information and resources."),
        ("Notification", "An alert or message from your phone or computer telling you about new emails, updates, or reminders."),
        ("Online", "Being connected to the internet and able to access websites, email, and other internet services."),
        ("Operating System", "The main software that runs your device - Windows, macOS, iOS, or Android."),
        ("Outbox", "The folder in email where messages wait to be sent, or recently sent messages are stored."),
        ("Password", "A secret word or phrase you type to prove your identity and access your accounts."),
        ("Password Manager", "An app that securely stores all your passwords so you only need to remember one master password."),
        ("PDF", "A file format that looks the same on any device - used for documents, forms, and ebooks."),
        ("Phishing", "A scam where criminals pretend to be a real company to trick you into giving personal information."),
        ("PIN", "Personal Identification Number - a short numeric code used to verify your identity."),
        ("Pixel", "A tiny single dot of color on your screen. Millions of pixels together create the images you see."),
        ("Platform", "A system or service where something runs - Facebook is a social media platform, for example."),
        ("Podcast", "An audio show you can listen to on your phone anytime - like radio on demand."),
        ("Pop-up", "A small window that suddenly appears on your screen, often an ad or alert."),
        ("Portal", "A website that serves as a starting point or gateway to many other services or information."),
        ("Privacy Settings", "Controls that let you choose who can see your information and activity online."),
        ("Processor", "The brain of your computer that performs calculations and runs programs."),
        ("Profile", "Your personal page on a website or app that shows your name, photo, and information."),
        ("QR Code", "A square pattern of black and white dots that your phone camera can scan to open a website."),
        ("RAM", "Random Access Memory - the fast temporary storage your computer uses while running programs."),
        ("Reboot", "Turning your device off and back on again to fix problems or complete updates."),
        ("Router", "A device that creates your home WiFi network and connects all your devices to the internet."),
        ("Scroll", "Moving up or down on a page using your mouse wheel, touchpad, or swiping on a touchscreen."),
        ("Screenshot", "A picture of exactly what is currently showing on your screen, saved as an image file."),
        ("Search Engine", "A website like Google that helps you find information on the internet by typing keywords."),
        ("Server", "A powerful computer that stores websites, emails, and data and sends them to your device when requested."),
        ("Settings", "A menu where you can change how your device or app works to suit your preferences."),
        ("Siri", "Apple's voice assistant built into iPhones and iPads. You talk to it and it helps you."),
        ("Smartphone", "A mobile phone that can run apps, browse the internet, take photos, and much more."),
        ("SMS", "Short Message Service - the technical name for regular text messages on your phone."),
        ("Social Media", "Websites and apps for connecting with people - Facebook, Instagram, Twitter, etc."),
        ("Software", "Programs and apps that tell your computer or phone what to do. Not physical - you cannot touch it."),
        ("Spam", "Unwanted messages sent in bulk, usually advertisements or scams. Common in email and texts."),
        ("Storage", "The total space on your device for saving files, photos, apps, and other data permanently."),
        ("Streaming", "Watching or listening to content over the internet in real-time without downloading it first."),
        ("Subscribe", "Signing up to receive regular content or services - like a YouTube channel or Netflix membership."),
        ("Sync", "Keeping the same files and information updated across multiple devices automatically."),
        ("Tab", "A way to have multiple web pages open at the same time in your browser, shown at the top."),
        ("Tablet", "A portable touchscreen device larger than a phone but smaller than a laptop. Like an iPad."),
        ("Tap", "Touching something on a touchscreen once with your finger to select or open it."),
        ("Text Message", "A short written message sent from one phone to another using your phone number."),
        ("Touchscreen", "A display that responds to finger touches instead of needing a mouse or keyboard."),
        ("Troubleshoot", "Finding and fixing a problem with your device or software step by step."),
        ("Two-Factor Auth", "An extra security step where you enter a code from your phone in addition to your password."),
        ("Update", "A newer version of software that fixes problems, adds features, or improves security."),
        ("Upload", "Sending a file from your device to the internet - the opposite of download."),
        ("URL", "The web address you type in your browser to go to a specific website (like www.google.com)."),
        ("USB", "Universal Serial Bus - the standard port and cable used to connect devices like flash drives and chargers."),
        ("Username", "The name you choose to identify yourself when creating an account on a website or app."),
        ("Video Call", "A phone call where you can see the other person on screen - like FaceTime or Zoom."),
        ("Virtual", "Something that exists on a computer or internet rather than in the physical world."),
        ("Virus", "A harmful program that can copy itself and damage your device or steal your information."),
        ("VPN", "Virtual Private Network - a tool that encrypts your internet connection for privacy and security."),
        ("Webcam", "A camera built into or connected to your computer for video calls and taking photos."),
        ("Website", "A collection of pages on the internet about a topic, company, or service you visit with a browser."),
        ("Widget", "A small tool on your phone's home screen that shows information at a glance without opening an app."),
        ("WiFi", "Wireless internet connection. Lets your devices connect to the internet without cables."),
        ("Window", "A rectangular area on your screen where a program or file is displayed."),
        ("Wireless", "Any technology that works without physical cables - WiFi, Bluetooth, and cellular data."),
        ("World Wide Web", "The system of websites and pages you access through the internet using a browser."),
        ("YouTube", "A free website for watching and sharing videos on any topic, owned by Google."),
        ("Zip File", "A compressed file that bundles multiple files together into one smaller package for easy sharing."),
        ("Zoom", "A popular video calling app used for meetings, family calls, and virtual gatherings."),
        ("Accessibility", "Features that make devices easier to use for people with disabilities or vision challenges."),
        ("Account", "Your personal profile on a website or service, protected by a username and password."),
        ("Address Bar", "The long box at the top of your browser where you type website addresses."),
        ("Airplane Mode", "A phone setting that turns off all wireless connections - useful during flights."),
        ("Alexa", "Amazon's voice assistant built into Echo devices. Talk to it to play music, set timers, and more."),
        ("Antivirus", "Software that protects your computer by detecting and removing harmful programs and viruses."),
        ("Battery", "The rechargeable power source inside your phone, tablet, or laptop."),
        ("Beta", "An early test version of software that is not quite finished - may have bugs."),
        ("Bing", "Microsoft's search engine - an alternative to Google for finding information online."),
        ("Block", "Preventing someone from contacting you or seeing your content on social media or messaging."),
        ("Blog", "A website where someone writes regular articles about topics they are interested in or expert about."),
        ("Buffer", "When a video pauses to load more content because your internet is too slow."),
        ("Caps Lock", "A keyboard key that makes all letters you type come out as CAPITAL LETTERS until turned off."),
        ("Cell Tower", "A tall structure that sends and receives wireless signals for your mobile phone service."),
        ("Chrome", "Google's web browser - one of the most popular programs for visiting websites."),
        ("Clipboard", "A temporary storage area where copied text or images are held until you paste them somewhere."),
        ("Contact", "A person's information (name, phone, email) saved in your phone or email address book."),
        ("CPU", "Central Processing Unit - the main chip that acts as your computer's brain, doing all the thinking."),
        ("Crash", "When a program or device suddenly stops working and may need to be restarted."),
        ("Cursor", "The blinking line showing where text will appear when you type, or the arrow you move with a mouse."),
        ("Cut", "Removing selected text or an image from one place so you can paste it somewhere else."),
        ("Dark Mode", "A display setting that uses a dark background with light text - easier on the eyes at night."),
        ("Default", "The standard setting that a device or program uses unless you change it to something else."),
        ("Delete", "Removing a file, message, or text permanently (or sending it to a recycle bin first)."),
        ("Domain", "The main part of a website's address - like google.com or amazon.com."),
        ("Double-Click", "Pressing the mouse button twice quickly to open a file or program."),
        ("DPI", "Dots Per Inch - a measure of print or screen quality. Higher DPI means sharper images."),
        ("Driver", "Software that helps your computer communicate with connected devices like printers or cameras."),
        ("Dropbox", "A cloud storage service that lets you save files online and access them from any device."),
        ("E-reader", "A device designed specifically for reading digital books, like Amazon's Kindle."),
        ("Edge", "Microsoft's web browser that comes built into Windows computers."),
        ("Export", "Saving a file in a different format or sending it to another program or device."),
        ("Extension", "A small add-on program for your browser that gives it extra features or abilities."),
        ("Facebook", "The largest social media platform for connecting with friends, family, and sharing posts."),
        ("FaceTime", "Apple's video calling app built into iPhones, iPads, and Macs for free video calls."),
        ("Feed", "A continuously updating list of posts and content from people you follow on social media."),
        ("Fiber Optic", "The fastest type of internet connection, using light through thin glass cables."),
        ("Fingerprint", "Using your fingerprint to unlock your phone or verify your identity instead of typing a password."),
        ("Format", "The way information is organized or presented. Also means to erase and prepare a storage device."),
        ("Frozen", "When your device stops responding to any input and appears stuck - usually needs a restart."),
        ("Fullscreen", "Making a video or window fill your entire screen with no borders or other programs visible."),
        ("GIF", "A short animated image that loops - often used in messages for humor or reactions."),
        ("Gigabyte", "A unit measuring storage space. A typical phone has 64-256 gigabytes for files and apps."),
        ("Google", "The most popular search engine and tech company, also makes Android phones and many free services."),
        ("Google Assistant", "Google's voice assistant. Say 'Hey Google' to ask questions and get help hands-free."),
        ("Group Chat", "A text conversation with three or more people all in the same message thread."),
        ("Guest Mode", "A limited account on a device that lets someone use it without accessing your personal data."),
        ("Home Button", "The physical or on-screen button that takes you back to your device's main screen."),
        ("Home Screen", "The first screen you see when you unlock your phone, showing your app icons and widgets."),
        ("iCloud", "Apple's cloud storage service that saves your photos, files, and backups from Apple devices."),
        ("Import", "Bringing files or data into a program from another source or device."),
        ("Internet of Things", "Everyday objects connected to the internet - smart fridges, doorbells, and thermostats."),
        ("iTunes", "Apple's media service for buying and playing music, movies, and TV shows."),
        ("Java", "A popular programming language used to build apps and websites. You might see update notifications."),
        ("Jailbreak", "Removing restrictions on a phone to install unauthorized apps - risky and not recommended."),
        ("Kindle", "Amazon's e-reader device and digital book store for buying and reading ebooks."),
        ("LinkedIn", "A social media platform focused on professional networking and job searching."),
        ("Live Stream", "Broadcasting video in real-time over the internet so viewers see it as it happens."),
        ("Location Services", "Your phone's ability to know where you are using GPS - used for maps and local searches."),
        ("Lock Screen", "The screen you see before unlocking your phone, usually showing the time and notifications."),
        ("Megabyte", "A unit of digital storage. One megabyte is about the size of one high-quality photo."),
        ("Messenger", "Facebook's messaging app for sending texts, photos, and making calls to Facebook friends."),
        ("Microsoft", "The company that makes Windows, Office (Word, Excel), and the Edge browser."),
        ("Mobile Data", "Internet connection through your cell phone carrier when you are not on WiFi."),
        ("Mouse", "The hand-held device you move on your desk to control the cursor on your computer screen."),
        ("Netflix", "A streaming service where you pay monthly to watch movies and TV shows online."),
        ("Night Mode", "A feature that reduces blue light from your screen in the evening to help you sleep better."),
        ("NFC", "Near Field Communication - tap your phone on a reader to make payments like Apple Pay."),
    ]

    # 8 terms per page = 25 pages
    terms_per_page = 8
    for page_idx in range(25):
        pdf.new_page()
        start = page_idx * terms_per_page
        end = min(start + terms_per_page, len(terms))
        page_terms = terms[start:end]

        pdf.add_centered_text(750, f"Tech Dictionary - Page {page_idx + 1}", font='F1', size=10, gray=0.4)
        pdf.add_line(70, 740, 542, 740, 0.5)

        y = 715
        for term, definition in page_terms:
            pdf.add_text(70, y, term, font='F2', size=14)
            y -= 22
            # Split definition into lines if too long
            words = definition.split()
            line = ""
            for word in words:
                if len(line + " " + word) > 75:
                    pdf.add_text(80, y, line.strip(), font='F4', size=13)
                    y -= 20
                    line = word
                else:
                    line += " " + word
            if line.strip():
                pdf.add_text(80, y, line.strip(), font='F4', size=13)
                y -= 20
            y -= 20  # Extra space between terms

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book60_Large_Print_Tech_Dictionary.pdf')
    print("Book 60 created: Book60_Large_Print_Tech_Dictionary.pdf")

if __name__ == '__main__':
    create_book()
