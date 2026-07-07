"""
Book 52: Smartphone Made Easy - A Large Print Guide for Ages 45+
KDP Interior - 8.5x11 inches (612x792 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "SMARTPHONE MADE EASY", font='F2', size=28)
    pdf.add_centered_text(575, "A Large Print Guide", font='F1', size=20)
    pdf.add_centered_text(545, "for Ages 45+", font='F1', size=20)
    pdf.add_line(150, 515, 462, 515, 2)
    pdf.add_centered_text(475, "Step-by-Step Instructions for iPhone & Android", font='F4', size=14)
    pdf.add_centered_text(445, "Big Text | Clear Steps | Easy to Follow", font='F4', size=13)
    pdf.add_centered_text(350, "By", font='F1', size=12)
    pdf.add_centered_text(320, "Daniel Tesfamariam", font='F2', size=18)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "Smartphone Made Easy - A Large Print Guide for Ages 45+", font='F2', size=12)
    pdf.add_centered_text(570, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(545, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(515, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(490, "Published via Amazon KDP", font='F1', size=10)

    # --- LESSONS ---
    lessons = [
        ("Lesson 1: Setting Up Your Phone", [
            "Step 1: Press and hold the power button on the side until the screen lights up.",
            "Step 2: Choose your language (usually English) and tap Next or Continue.",
            "Step 3: Connect to your home WiFi by selecting your network name and typing the password.",
            "Step 4: Sign in with your Apple ID (iPhone) or Google account (Android), or create one.",
            "Step 5: Set a passcode or PIN to keep your phone secure - choose something you will remember.",
            "Step 6: Choose your preferences for location, Siri/Google Assistant, and notifications.",
            "Step 7: Your phone is ready! Take a moment to look at the home screen icons.",
        ]),
        ("Lesson 2: Making Phone Calls", [
            "Step 1: Find the green Phone icon on your home screen and tap it once.",
            "Step 2: You will see a keypad with numbers. Tap the numbers of the phone number.",
            "Step 3: Press the green call button at the bottom to start the call.",
            "Step 4: Hold the phone to your ear or tap the speaker icon for speakerphone.",
            "Step 5: When finished, tap the red End Call button to hang up.",
            "Step 6: To call someone in your contacts, tap Contacts and find their name.",
            "Step 7: To redial someone, tap the Recents tab to see your call history.",
        ]),
        ("Lesson 3: Sending Text Messages", [
            "Step 1: Find the Messages icon (green with a white speech bubble) and tap it.",
            "Step 2: Tap the compose button (usually a pencil or plus sign) for a new message.",
            "Step 3: Type the person's name or phone number in the To field at the top.",
            "Step 4: Tap the text box at the bottom where it says 'Type a message'.",
            "Step 5: Use the on-screen keyboard to type your message.",
            "Step 6: Press the send button (arrow icon) when your message is ready.",
            "Step 7: Their reply will appear in the same conversation below your message.",
        ]),
        ("Lesson 4: Taking Photos", [
            "Step 1: Find the Camera app icon and tap it to open the camera.",
            "Step 2: Point your phone at what you want to photograph.",
            "Step 3: Hold the phone steady with both hands for a clear picture.",
            "Step 4: Tap the large circle button at the bottom to take the photo.",
            "Step 5: View your photo by tapping the small preview in the corner.",
            "Step 6: To switch to the front camera for selfies, tap the rotate camera icon.",
            "Step 7: All photos are saved automatically in your Photos or Gallery app.",
        ]),
        ("Lesson 5: Using WiFi", [
            "Step 1: Open Settings (the gear icon) on your phone.",
            "Step 2: Tap WiFi or Wireless & Networks.",
            "Step 3: Make sure WiFi is turned ON (toggle should be green or blue).",
            "Step 4: You will see a list of available networks. Find your home network name.",
            "Step 5: Tap your network name and enter your WiFi password carefully.",
            "Step 6: Once connected, you will see a checkmark or the WiFi symbol at the top.",
            "Step 7: Your phone will remember this network and connect automatically next time.",
        ]),
        ("Lesson 6: Downloading Apps", [
            "Step 1: Open the App Store (iPhone) or Google Play Store (Android).",
            "Step 2: Tap the Search bar at the top or bottom of the screen.",
            "Step 3: Type the name of the app you want to download.",
            "Step 4: Find the correct app in the results and tap on it.",
            "Step 5: Tap 'Get' or 'Install' to download the app to your phone.",
            "Step 6: You may need to confirm with your password or fingerprint.",
            "Step 7: The app will appear on your home screen when the download finishes.",
        ]),
        ("Lesson 7: Using Email on Your Phone", [
            "Step 1: Open the Mail or Gmail app (it looks like an envelope).",
            "Step 2: Sign in with your email address and password if prompted.",
            "Step 3: Your inbox shows all received emails - newest at the top.",
            "Step 4: Tap any email to open and read it.",
            "Step 5: To write a new email, tap the compose button (pencil or plus icon).",
            "Step 6: Enter the recipient's email, type a subject line, then write your message.",
            "Step 7: Tap Send (paper airplane icon) when your email is ready to go.",
        ]),
        ("Lesson 8: Video Calls (FaceTime & Zoom)", [
            "Step 1: For FaceTime (iPhone): Open FaceTime app and tap the person's name.",
            "Step 2: Tap the video camera icon to start a video call.",
            "Step 3: For Zoom: Download the Zoom app from your app store.",
            "Step 4: To join a Zoom meeting, tap Join and enter the Meeting ID number.",
            "Step 5: Allow camera and microphone access when prompted.",
            "Step 6: You should see yourself and the other person on screen.",
            "Step 7: Tap the red button to end the call when you are finished.",
        ]),
        ("Lesson 9: Using Maps and GPS", [
            "Step 1: Open the Maps app (Apple Maps or Google Maps).",
            "Step 2: Tap the search bar and type where you want to go.",
            "Step 3: Select the correct address from the suggestions that appear.",
            "Step 4: Tap 'Directions' to get step-by-step navigation.",
            "Step 5: Choose driving, walking, or public transport.",
            "Step 6: Tap 'Start' or 'Go' to begin turn-by-turn voice directions.",
            "Step 7: The phone will tell you when to turn - keep it in a safe holder while driving.",
        ]),
        ("Lesson 10: Social Media Basics", [
            "Step 1: Choose a platform - Facebook is popular for adults and family connections.",
            "Step 2: Download the Facebook app and create an account with your email.",
            "Step 3: Add a profile photo so friends and family can recognize you.",
            "Step 4: Search for friends and family by name and send friend requests.",
            "Step 5: Your News Feed shows posts from friends - scroll down to see more.",
            "Step 6: To post something, tap 'What's on your mind?' and type or add a photo.",
            "Step 7: Use reactions (like, love, etc.) to respond to posts from others.",
        ]),
        ("Lesson 11: Online Banking Safety", [
            "Step 1: Only download your bank's official app from the app store.",
            "Step 2: Never access banking through links in emails or text messages.",
            "Step 3: Set up fingerprint or face recognition for secure login.",
            "Step 4: Create a strong password with letters, numbers, and symbols.",
            "Step 5: Enable notifications so you get alerts for every transaction.",
            "Step 6: Always log out when you finish your banking session.",
            "Step 7: Never do banking on public WiFi - use your home network or mobile data.",
        ]),
        ("Lesson 12: Setting Alarms and Reminders", [
            "Step 1: Open the Clock app to set alarms for wake-up times.",
            "Step 2: Tap the plus sign to create a new alarm and set the time.",
            "Step 3: Choose which days the alarm should repeat (daily, weekdays, etc.).",
            "Step 4: For reminders, use the Reminders app or say 'Hey Siri, remind me'.",
            "Step 5: Set reminders for medications: 'Remind me to take pills at 8 AM'.",
            "Step 6: Calendar events can also send you alerts before appointments.",
            "Step 7: You can set multiple alarms and reminders for different needs.",
        ]),
        ("Lesson 13: Adjusting Text Size", [
            "Step 1: Open Settings on your phone.",
            "Step 2: On iPhone: tap Display & Brightness, then Text Size.",
            "Step 3: On Android: tap Display, then Font size or Display size.",
            "Step 4: Drag the slider to the right to make text larger.",
            "Step 5: Preview the text as you adjust to find your comfortable size.",
            "Step 6: You can also turn on Bold Text for easier reading.",
            "Step 7: Some apps let you zoom in by pinching outward with two fingers.",
        ]),
        ("Lesson 14: Using Voice Commands", [
            "Step 1: Activate your voice assistant: say 'Hey Siri' or 'Hey Google'.",
            "Step 2: Speak clearly and naturally - no need for special language.",
            "Step 3: Try: 'Call [name]' to make a hands-free phone call.",
            "Step 4: Try: 'Send a text to [name] saying I will be there at 3'.",
            "Step 5: Try: 'What is the weather today?' for a quick forecast.",
            "Step 6: Try: 'Set a timer for 15 minutes' when cooking.",
            "Step 7: Try: 'Navigate to [address]' for driving directions.",
        ]),
        ("Lesson 15: Saving Contacts", [
            "Step 1: Open the Phone app and tap Contacts.",
            "Step 2: Tap the plus (+) button to add a new contact.",
            "Step 3: Type the person's first and last name.",
            "Step 4: Add their phone number in the phone field.",
            "Step 5: Optionally add their email address.",
            "Step 6: Tap Save or Done to store the contact.",
            "Step 7: Now you can call or text them by name instead of remembering numbers.",
        ]),
        ("Lesson 16: Sending Photos to Family", [
            "Step 1: Open your Photos or Gallery app.",
            "Step 2: Find the photo you want to share and tap on it.",
            "Step 3: Tap the Share button (box with arrow on iPhone, three dots on Android).",
            "Step 4: Choose how to send: Messages, Email, WhatsApp, or other apps.",
            "Step 5: Select the person you want to send it to.",
            "Step 6: Add a message if you want, then tap Send.",
            "Step 7: You can select multiple photos to send at once by tapping Select first.",
        ]),
        ("Lesson 17: Using the Camera Well", [
            "Step 1: Clean your camera lens with a soft cloth before taking photos.",
            "Step 2: Hold your phone horizontally (sideways) for landscape photos.",
            "Step 3: Tap the screen where you want the camera to focus.",
            "Step 4: Make sure you have good lighting - face the light source.",
            "Step 5: Use the zoom carefully - pinch outward gently, but avoid too much zoom.",
            "Step 6: Try HDR mode for outdoor photos with bright sky and dark shadows.",
            "Step 7: For videos, tap and hold the record button or switch to Video mode.",
        ]),
        ("Lesson 18: App Store Basics", [
            "Step 1: Open the App Store (iPhone) or Play Store (Android).",
            "Step 2: Browse categories like Health, Games, News, or Social.",
            "Step 3: Read app descriptions and user reviews before downloading.",
            "Step 4: Check that the app is free or note the price before installing.",
            "Step 5: Look for the star rating - 4 stars and above is generally good.",
            "Step 6: Be careful of apps that ask for too many permissions.",
            "Step 7: To update apps, go to your profile in the store and tap Update All.",
        ]),
        ("Lesson 19: Staying Safe Online", [
            "Step 1: Never share passwords with anyone, even people claiming to be support.",
            "Step 2: Be suspicious of messages asking you to click links or verify accounts.",
            "Step 3: Use different passwords for different accounts when possible.",
            "Step 4: Keep your phone software up to date - updates include security fixes.",
            "Step 5: Only download apps from the official App Store or Play Store.",
            "Step 6: Be careful what personal information you share on social media.",
            "Step 7: If something seems too good to be true, it probably is a scam.",
        ]),
        ("Lesson 20: Managing Storage", [
            "Step 1: Check your storage: Settings > General > Storage (iPhone) or Storage (Android).",
            "Step 2: Delete apps you no longer use by holding the icon and choosing Delete.",
            "Step 3: Back up photos to the cloud (iCloud or Google Photos) then delete from phone.",
            "Step 4: Clear browser data: go to your browser settings and clear cache.",
            "Step 5: Delete old text message threads with large attachments.",
            "Step 6: Remove downloaded music or videos you have already enjoyed.",
            "Step 7: Restart your phone occasionally to free up temporary memory.",
        ]),
        ("Lesson 21: Using the Calendar", [
            "Step 1: Open the Calendar app on your phone.",
            "Step 2: Tap the plus (+) button to add a new event.",
            "Step 3: Type the event name: 'Doctor appointment' or 'Lunch with Mary'.",
            "Step 4: Set the date and time for the event.",
            "Step 5: Add a reminder alert - choose 1 hour before or 1 day before.",
            "Step 6: Add the location if helpful so you can get directions later.",
            "Step 7: Your phone will notify you before each event so you never forget.",
        ]),
        ("Lesson 22: Emergency Features", [
            "Step 1: Set up emergency contacts: Settings > Emergency SOS or Medical ID.",
            "Step 2: Add your medical information (allergies, conditions, medications).",
            "Step 3: Learn the emergency shortcut: press side button 5 times quickly (iPhone).",
            "Step 4: On Android, press power button quickly 5 times for emergency call.",
            "Step 5: Set up ICE (In Case of Emergency) contacts in your phone app.",
            "Step 6: Learn to use the flashlight for emergencies (swipe up or check control center).",
            "Step 7: Consider installing a medical alert app for additional safety.",
        ]),
        ("Lesson 23: Accessibility Settings", [
            "Step 1: Open Settings and find Accessibility (it has a person icon).",
            "Step 2: Turn on Larger Text to make everything easier to read.",
            "Step 3: Enable Bold Text for clearer letters and numbers.",
            "Step 4: Turn on Zoom for a magnifying glass you can use anywhere.",
            "Step 5: Increase touch duration if you accidentally tap things.",
            "Step 6: Turn on Spoken Content to have your phone read text aloud.",
            "Step 7: Adjust display to reduce motion and avoid dizziness from animations.",
        ]),
        ("Lesson 24: Troubleshooting Common Issues", [
            "Step 1: Phone frozen? Hold the power button for 10 seconds to force restart.",
            "Step 2: No internet? Toggle WiFi off and on in Settings, or restart your router.",
            "Step 3: App crashing? Close it completely and reopen, or delete and reinstall.",
            "Step 4: Battery draining fast? Lower screen brightness and close unused apps.",
            "Step 5: No sound? Check that the mute switch is off and volume is turned up.",
            "Step 6: Screen too dark? Adjust brightness in Settings > Display.",
            "Step 7: Still having issues? Restart your phone - this fixes most problems.",
        ]),
        ("Lesson 25: Quick Reference Card", [
            "MAKE A CALL: Phone app > Keypad > Dial number > Green button",
            "SEND A TEXT: Messages > Compose > Type name > Type message > Send",
            "TAKE A PHOTO: Camera app > Point > Tap circle button",
            "DOWNLOAD AN APP: App Store/Play Store > Search > Install",
            "SET AN ALARM: Clock app > Plus (+) > Set time > Save",
            "CHECK EMAIL: Mail/Gmail app > Tap inbox > Tap email to read",
            "VIDEO CALL: FaceTime/Zoom > Select contact > Tap video icon",
        ]),
    ]

    for title, steps in lessons:
        pdf.new_page()
        pdf.add_centered_text(740, title, font='F2', size=18)
        pdf.add_line(80, 720, 532, 720, 1)
        y = 690
        for step in steps:
            pdf.add_text(60, y, step, font='F4', size=12)
            y -= 30

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book52_Smartphone_Guide_Seniors.pdf')
    print("Book 52 created: Book52_Smartphone_Guide_Seniors.pdf")

if __name__ == '__main__':
    create_book()
