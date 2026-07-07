"""
Book 56: Internet Safety for Seniors - Protect Yourself Online
KDP Interior - 8.5x11 inches (612x792 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "INTERNET SAFETY", font='F2', size=32)
    pdf.add_centered_text(575, "FOR SENIORS", font='F2', size=28)
    pdf.add_centered_text(530, "Protect Yourself Online", font='F1', size=18)
    pdf.add_line(150, 500, 462, 500, 2)
    pdf.add_centered_text(465, "A Plain-English Guide to Staying Safe", font='F4', size=14)
    pdf.add_centered_text(435, "on the Internet, Email, and Social Media", font='F4', size=13)
    pdf.add_centered_text(350, "By", font='F1', size=12)
    pdf.add_centered_text(320, "Daniel Tesfamariam", font='F2', size=18)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(600, "Internet Safety for Seniors - Protect Yourself Online", font='F2', size=12)
    pdf.add_centered_text(570, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(545, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(515, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(490, "Published via Amazon KDP", font='F1', size=10)

    # --- TOPICS ---
    topics = [
        ("Topic 1: Recognizing Scam Emails", [
            "- Look for misspellings and poor grammar in the email.",
            "- Check the sender's email address carefully - scammers use fake addresses.",
            "- Be suspicious of urgent language like 'Act now!' or 'Your account is locked!'",
            "- Never click links in emails from unknown senders.",
            "- Hover over links to see where they really go before clicking.",
            "- Legitimate companies will never ask for your password by email.",
            "- If an email offers money or prizes you did not enter to win, it is a scam.",
            "- When in doubt, call the company directly using the number on their website.",
            "- Forward suspicious emails to the company's fraud department.",
            "- Delete scam emails - do not reply or unsubscribe (this confirms your address).",
        ]),
        ("Topic 2: Creating Strong Passwords", [
            "- Use at least 12 characters - longer is always stronger.",
            "- Mix uppercase letters, lowercase letters, numbers, and symbols.",
            "- Never use personal information like birthdays, pet names, or addresses.",
            "- Avoid common words like 'password', '123456', or 'qwerty'.",
            "- Use a different password for each important account.",
            "- Consider using a passphrase: 'My-Dog-Loves-Walks-At-7pm!' is very strong.",
            "- Write passwords in a secure physical notebook kept in a safe place.",
            "- Consider a password manager app to remember all your passwords.",
            "- Change passwords immediately if you suspect any account was compromised.",
            "- Never share passwords with anyone, even family members for shared accounts.",
        ]),
        ("Topic 3: Safe Online Shopping", [
            "- Only shop on websites that show a padlock icon in the browser address bar.",
            "- Look for 'https://' at the beginning of the web address (the 's' means secure).",
            "- Stick to well-known retailers like Amazon, Walmart, and Target online.",
            "- Read customer reviews before buying from unfamiliar sellers.",
            "- Use a credit card instead of debit card for better fraud protection.",
            "- Never save your credit card information on websites you rarely use.",
            "- Be wary of deals that seem too good to be true - they usually are.",
            "- Check the return policy before purchasing anything.",
            "- Keep records of all online purchases and confirmation emails.",
            "- Monitor your bank statements weekly for unauthorized charges.",
        ]),
        ("Topic 4: Social Media Privacy", [
            "- Set your profile to 'Friends Only' so strangers cannot see your posts.",
            "- Never post your home address, phone number, or daily schedule.",
            "- Be careful about posting vacation photos while you are away from home.",
            "- Do not accept friend requests from people you do not know in real life.",
            "- Review your privacy settings at least every few months.",
            "- Be cautious about quizzes that ask personal questions (maiden name, first pet).",
            "- Never share photos of financial documents, IDs, or boarding passes.",
            "- Remember that anything you post online can be seen by anyone eventually.",
            "- Turn off location sharing on posts so people cannot track where you are.",
            "- If someone you know is acting strange online, call them - their account may be hacked.",
        ]),
        ("Topic 5: Spotting Fake Websites", [
            "- Check the web address carefully - scammers use similar-looking URLs.",
            "- Look for misspellings in the website name (amaz0n.com instead of amazon.com).",
            "- Legitimate websites have professional design without broken images.",
            "- Check if the website has a physical address and phone number listed.",
            "- Search the company name plus 'scam' or 'reviews' to check reputation.",
            "- Be suspicious of websites that only accept wire transfers or gift cards.",
            "- Look for a privacy policy and terms of service at the bottom of the page.",
            "- If a website pops up saying your computer is infected, close it immediately.",
            "- Bookmark your important websites so you always go to the real one.",
            "- When in doubt, type the web address yourself rather than clicking a link.",
        ]),
        ("Topic 6: Two-Factor Authentication Explained", [
            "- Two-factor authentication (2FA) adds a second layer of security to your accounts.",
            "- Even if someone steals your password, they cannot get in without the second factor.",
            "- The most common second factor is a code sent to your phone by text message.",
            "- When you log in, you enter your password then the code from your phone.",
            "- Enable 2FA on your email, bank, and social media accounts first.",
            "- Some services use an app like Google Authenticator instead of text messages.",
            "- Keep a backup phone number or recovery codes in case you lose your phone.",
            "- 2FA takes an extra 10 seconds but makes your account much more secure.",
            "- Most banks and email providers offer 2FA in their security settings.",
            "- Think of 2FA like a double lock on your front door - extra protection.",
        ]),
        ("Topic 7: Protecting Personal Information", [
            "- Never share your Social Security number online or by email.",
            "- Be cautious about what personal details you post on social media.",
            "- Shred physical mail that contains personal or financial information.",
            "- Do not give personal information to callers who contact you first.",
            "- Legitimate organizations already have your info - they will not ask for it again.",
            "- Be careful filling out online forms - only provide required information.",
            "- Check your credit report annually for accounts you did not open.",
            "- Use a separate email address for signing up for newsletters and promotions.",
            "- Be wary of free WiFi that asks for personal details to connect.",
            "- Review which apps on your phone have access to your contacts and photos.",
        ]),
        ("Topic 8: Public WiFi Dangers", [
            "- Public WiFi in cafes, airports, and hotels is not secure.",
            "- Hackers can see what you do on public WiFi if it is not encrypted.",
            "- Never access your bank account or make purchases on public WiFi.",
            "- Turn off automatic WiFi connection on your phone in public places.",
            "- If you must use public WiFi, use a VPN (Virtual Private Network) for protection.",
            "- Verify the network name with staff - hackers create fake hotspots.",
            "- A fake hotspot might be named 'Free_Airport_WiFi' to trick you.",
            "- Use your phone's mobile data instead of public WiFi for sensitive tasks.",
            "- Forget public networks after using them so your phone does not reconnect.",
            "- At home, make sure your own WiFi has a strong password to prevent unauthorized access.",
        ]),
        ("Topic 9: Recognizing Phone Scams", [
            "- If a caller says you owe money and must pay immediately, it is a scam.",
            "- The IRS and government agencies communicate by mail, not threatening phone calls.",
            "- Never give credit card or bank information to someone who calls you.",
            "- Scammers can fake caller ID to show a real company's phone number.",
            "- If someone claims to be from your bank, hang up and call the number on your card.",
            "- Be suspicious of calls saying a grandchild is in trouble and needs money.",
            "- Never pay anything with gift cards - this is always a scam method.",
            "- Register your number on the Do Not Call list at donotcall.gov.",
            "- Let unknown numbers go to voicemail - legitimate callers leave messages.",
            "- Report scam calls to the FTC at reportfraud.ftc.gov.",
        ]),
        ("Topic 10: Keeping Devices Updated", [
            "- Software updates fix security holes that hackers can exploit.",
            "- Turn on automatic updates for your phone, tablet, and computer.",
            "- On iPhone: Settings > General > Software Update > Automatic Updates.",
            "- On Android: Settings > System > System Update.",
            "- On Windows: Settings > Update & Security > Windows Update.",
            "- Update your web browser regularly - it is your gateway to the internet.",
            "- Update apps from the App Store or Play Store at least weekly.",
            "- Restart your devices after updates to complete the installation.",
            "- Old devices that no longer receive updates should be replaced.",
            "- Updates may add new features too, not just security fixes.",
        ]),
        ("Topic 11: Safe Video Calling", [
            "- Only accept video calls from people you know and trust.",
            "- Make sure your background does not show personal information or valuables.",
            "- Use meeting passwords when hosting video calls on Zoom or similar.",
            "- Do not share meeting links on social media - use direct invitations.",
            "- Mute your microphone when not speaking to prevent accidental sharing.",
            "- Be aware that others can take screenshots during video calls.",
            "- Keep your video calling software updated to the latest version.",
            "- Cover your camera with tape or a cover when not using video calls.",
            "- If an unknown person joins your call, remove them immediately.",
            "- Use the waiting room feature so you can approve who joins.",
        ]),
        ("Topic 12: Avoiding Malware", [
            "- Malware is harmful software that can damage your device or steal data.",
            "- Never download software from pop-up ads or unknown websites.",
            "- Only download apps from official app stores (Apple App Store, Google Play).",
            "- Do not open email attachments from unknown senders.",
            "- Install antivirus software and keep it updated on your computer.",
            "- Be cautious of free software that seems too good to be true.",
            "- If your device suddenly runs slowly, it might have malware.",
            "- Pop-ups saying 'Your computer is infected, call this number' are themselves scams.",
            "- Regularly back up your important files to an external drive or cloud.",
            "- If you think you have malware, disconnect from the internet and run a scan.",
        ]),
        ("Topic 13: Protecting Financial Info Online", [
            "- Only use your bank's official app or website for online banking.",
            "- Look for the padlock icon and 'https://' before entering financial details.",
            "- Set up account alerts for any transaction over a small amount like $25.",
            "- Check your bank and credit card statements at least weekly.",
            "- Never email financial information like account numbers or tax forms.",
            "- Use strong, unique passwords for all financial accounts.",
            "- Enable two-factor authentication on all bank and investment accounts.",
            "- Be suspicious of emails claiming to be from your bank asking you to log in.",
            "- Bookmark your bank's website and always use that bookmark to visit.",
            "- Consider freezing your credit if you do not plan to apply for new loans.",
        ]),
        ("Topic 14: Recognizing Deepfakes", [
            "- Deepfakes are fake videos or audio made with AI to look real.",
            "- They can make it look like someone said something they never did.",
            "- Be skeptical of shocking videos shared on social media.",
            "- Look for unnatural facial movements or lip syncing that seems off.",
            "- Check if the content appears on legitimate news sources.",
            "- Scammers may use AI voice cloning to impersonate family members.",
            "- If a family member calls asking for money, verify by calling them back.",
            "- Establish a family code word that only real members would know.",
            "- Video quality that looks slightly blurry or waxy may be a deepfake.",
            "- When in doubt, verify information through multiple trusted sources.",
        ]),
        ("Topic 15: Safe App Downloads", [
            "- Only download apps from Apple App Store or Google Play Store.",
            "- Read the app description and check the developer's name carefully.",
            "- Look at the star rating and read recent reviews from other users.",
            "- Check what permissions the app requests - a flashlight does not need your contacts.",
            "- Be suspicious of apps with very few downloads or reviews.",
            "- Avoid apps that promise free versions of things that normally cost money.",
            "- Delete apps you no longer use - they can still access your data.",
            "- Keep all apps updated to get the latest security patches.",
            "- If an app asks for too much personal information, do not use it.",
            "- Stick to well-known apps recommended by people you trust.",
        ]),
        ("Topic 16: Email Safety Tips", [
            "- Do not open attachments from people you do not know.",
            "- Be suspicious of emails with generic greetings like 'Dear Customer'.",
            "- Legitimate companies will address you by your actual name.",
            "- Never click 'unsubscribe' in spam emails - it confirms your address is active.",
            "- Check the sender's full email address, not just the display name.",
            "- Be wary of emails creating urgency: 'Your account expires in 24 hours!'",
            "- When in doubt, go directly to the company's website instead of clicking links.",
            "- Mark spam emails as spam so your email learns to filter them.",
            "- Use separate email addresses for personal and promotional sign-ups.",
            "- Enable your email's spam filter and check spam folder occasionally for real mail.",
        ]),
        ("Topic 17: What to Do If You Are Hacked", [
            "- Change your passwords immediately, starting with email and banking.",
            "- Enable two-factor authentication on all important accounts.",
            "- Check your bank accounts for unauthorized transactions.",
            "- Contact your bank immediately if you see charges you did not make.",
            "- Run a full antivirus scan on your computer and phone.",
            "- Check if your email is sending messages you did not write.",
            "- Notify your contacts that your account was compromised.",
            "- Place a fraud alert on your credit reports through the three bureaus.",
            "- File a report with the FTC at identitytheft.gov if your identity was stolen.",
            "- Consider getting professional help from your device manufacturer or a tech expert.",
        ]),
        ("Topic 18: Protecting Grandchildren Online", [
            "- Talk to grandchildren about never sharing personal info with strangers online.",
            "- Help parents set up parental controls on devices grandchildren use.",
            "- Know which apps and games grandchildren are using.",
            "- Be a safe person they can come to if something online makes them uncomfortable.",
            "- Do not post photos of grandchildren with identifying information.",
            "- Avoid posting their school name, team, or regular schedule.",
            "- Teach them that not everyone online is who they say they are.",
            "- Encourage open conversations about their online experiences.",
            "- Learn about the platforms they use so you can guide them.",
            "- Set a good example by practicing safe internet habits yourself.",
        ]),
        ("Topic 19: Reporting Scams", [
            "- Report internet fraud to the FTC at reportfraud.ftc.gov.",
            "- Report email scams by forwarding to spam@uce.gov.",
            "- Report phone scams to the FTC and your phone carrier.",
            "- Contact your local police for scams involving financial loss.",
            "- Report identity theft at identitytheft.gov for a recovery plan.",
            "- Notify your bank immediately if financial accounts are compromised.",
            "- Report social media scams using the platform's report feature.",
            "- Save evidence: screenshots of messages, emails, and phone numbers used.",
            "- Warn friends and family about scams you encounter.",
            "- Do not feel embarrassed - scammers are professionals who trick millions of people.",
        ]),
        ("Topic 20: Quick Reference Safety Checklist", [
            "[ ] I use strong, unique passwords for every important account.",
            "[ ] I have two-factor authentication enabled on email and banking.",
            "[ ] I keep all my devices and apps updated with the latest software.",
            "[ ] I never click links in suspicious emails or text messages.",
            "[ ] I do not share personal information with unknown callers.",
            "[ ] I check my bank statements regularly for unauthorized charges.",
            "[ ] I only download apps from official app stores.",
            "[ ] I do not use public WiFi for banking or shopping.",
            "[ ] I have antivirus software installed and updated on my computer.",
            "[ ] I know who to call if I think I have been scammed (bank, FTC, police).",
        ]),
    ]

    for title, tips in topics:
        pdf.new_page()
        pdf.add_centered_text(740, title, font='F2', size=18)
        pdf.add_line(80, 720, 532, 720, 1)
        y = 690
        for tip in tips:
            pdf.add_text(70, y, tip, font='F4', size=12)
            y -= 30

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book56_Internet_Safety_Guide.pdf')
    print("Book 56 created: Book56_Internet_Safety_Guide.pdf")

if __name__ == '__main__':
    create_book()
