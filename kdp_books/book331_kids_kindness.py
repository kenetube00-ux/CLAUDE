from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    categories = {
        "Kindness at Home": [
            ("Make Someone's Bed", "Maya noticed her little brother struggling to make his bed. Without being asked, she made it perfectly and left a smiley note on his pillow.", "Offer to make a family member's bed for them", "Cared for, loved, and supported", "Helpful, warm, and generous"),
            ("Write a Thank You Note", "Jordan wrote a note to Mom saying 'Thank you for always packing my lunch with love.' Mom kept it in her wallet forever.", "Write a heartfelt thank-you note to someone in your family", "Appreciated, valued, and seen", "Grateful, thoughtful, and connected"),
            ("Cook a Simple Meal", "At age 10, Kai decided to surprise Dad with breakfast. Cereal, toast, and orange juice - simple but made with love.", "Prepare a simple meal or snack for your family", "Cared for, surprised, and touched", "Independent, loving, and capable"),
            ("Do a Chore Without Being Asked", "Priya noticed the dishes piling up. Without a word, she washed them all. Mom came home to a clean kitchen and almost cried.", "Do a household chore before anyone asks you to", "Relieved, grateful, and proud of you", "Responsible, thoughtful, and mature"),
            ("Give a Family Member a Compliment", "Ethan told his sister 'You're really good at drawing. I wish I could draw like you.' Her face lit up for the whole day.", "Give a genuine, specific compliment to each family member today", "Valued, noticed, and encouraged", "Kind, observant, and generous"),
            ("Create a Family Fun Night", "Zoe planned game night: she chose games, made popcorn, and invited everyone. It became their new weekly tradition.", "Plan and organize a family activity night", "Connected, joyful, and together", "Creative, thoughtful, and fun"),
            ("Help with Groceries", "Marcus always helped carry groceries in, but today he also put them all away in the right places without being asked.", "Help carry AND put away groceries after shopping", "Supported, impressed, and grateful", "Strong, helpful, and attentive"),
            ("Listen to a Family Story", "When Grandpa started telling 'that old story' again, Aisha sat down, looked him in the eyes, and really listened.", "Ask an older family member to tell you a story from their childhood", "Valued, respected, and loved", "Patient, curious, and loving"),
            ("Make a Sibling Laugh", "Tyler's little sister was crying after a bad day. He did his silliest dance and made ridiculous faces until she giggled.", "Do something silly to cheer up a family member who's sad", "Lighter, happier, and comforted", "Fun, caring, and empathetic"),
            ("Share Without Being Asked", "Nora got the last cookie. She saw her brother looking at it. Without hesitation, she broke it in half and shared.", "Share something you love with a family member today", "Included, loved, and valued", "Generous, unselfish, and kind"),
        ],
        "Kindness at School": [
            ("Include Someone New", "On the first day, a new kid sat alone at lunch looking scared. Emma walked over and said 'Want to sit with us?'", "Invite someone who looks lonely to join your group", "Welcomed, relieved, and grateful", "Brave, inclusive, and warm"),
            ("Help a Struggling Classmate", "Lucas noticed his classmate couldn't understand the math problem. He quietly offered to explain it a different way.", "Offer to help a classmate who's struggling with schoolwork", "Supported, less stressed, and grateful", "Smart, patient, and generous"),
            ("Thank a Teacher", "Mia wrote her teacher a note: 'Thank you for making science fun. You're the reason I want to be a scientist.'", "Write a thank-you note to a teacher who has helped you", "Appreciated, motivated, and valued", "Grateful, thoughtful, and articulate"),
            ("Pick Up Trash on School Grounds", "Jackson spent 10 minutes of recess picking up litter. Soon, 3 other kids joined him. They made it a weekly thing.", "Spend 10 minutes cleaning up an area at your school", "Proud (of school), inspired, and cleaner environment", "Responsible, caring, and a leader"),
            ("Celebrate Someone Else's Achievement", "When Aria's classmate won the spelling bee, Aria clapped the loudest and said 'You deserved it! You studied so hard!'", "Genuinely celebrate when a classmate succeeds at something", "Encouraged, proud, and valued", "Generous, secure, and supportive"),
            ("Hold the Door Open", "Oliver held the door for his class every morning for a week. By Friday, three other kids started doing it too.", "Hold doors open for others throughout the day", "Respected and noticed", "Polite, attentive, and considerate"),
            ("Share School Supplies", "When Zara saw a classmate without a pencil (again), she quietly gave one without making a big deal about it.", "Share supplies with someone who needs them without making it awkward", "Relieved and not embarrassed", "Generous, discreet, and kind"),
            ("Sit with Someone Who's Alone", "Liam noticed a kid always eating alone. He sat down and asked about their favorite video game. A friendship began.", "Sit with someone who usually sits alone at lunch", "Included, valued, and less lonely", "Brave, compassionate, and friendly"),
            ("Write an Encouraging Note", "Chloe put anonymous sticky notes on lockers: 'You're doing great!' 'Someone is glad you exist!' Kids smiled all day.", "Write 5 anonymous encouraging notes and leave them for others", "Uplifted, surprised, and motivated", "Creative, kind, and encouraging"),
            ("Be a Good Sport", "After losing the kickball game, Aiden shook the other team's hands and said 'Great game! You guys were awesome.'", "Congratulate the other team after a game, win or lose", "Respected and admired", "Mature, graceful, and sportsmanlike"),
        ],
        "Kindness to Friends": [
            ("Remember Their Important Day", "Nora remembered her friend's piano recital and texted 'Good luck today! You'll be amazing!' before it started.", "Remember and acknowledge a friend's important event", "Supported, remembered, and cared for", "Thoughtful, attentive, and loyal"),
            ("Apologize First", "After a fight, Caleb texted first: 'I'm sorry. Our friendship means more than being right.' They made up that day.", "Be the first to apologize after a disagreement", "Relieved, valued, and respected", "Mature, humble, and brave"),
            ("Defend a Friend", "When someone made fun of Emma's friend behind her back, Emma said 'That's not cool. She's a great person.'", "Stand up for a friend who's being talked about negatively", "Protected, valued, and safe", "Loyal, brave, and principled"),
            ("Give a Thoughtful Gift", "Lucas made his friend a playlist of songs he thought they'd love. It cost nothing but showed he really knew them.", "Give a friend a thoughtful (not expensive) personalized gift", "Known, valued, and special", "Creative, thoughtful, and caring"),
            ("Keep a Secret Safe", "When a friend shared something private, Mia never told anyone. Trust is the foundation of real friendship.", "Keep your friends' secrets and private information safe", "Safe, trusted, and respected", "Trustworthy, loyal, and reliable"),
            ("Be Happy for Their Success", "Jackson's best friend made the team when Jackson didn't. Jackson said 'Dude, that's awesome!' and meant it.", "Celebrate your friend's wins without jealousy", "Supported and loved", "Secure, generous, and genuine"),
            ("Check In When They're Quiet", "Aria noticed her friend was quieter than usual. She asked privately: 'Hey, are you okay? I'm here if you want to talk.'", "Notice when a friend seems off and check on them", "Seen, cared for, and less alone", "Perceptive, empathetic, and caring"),
            ("Include Them in Plans", "Oliver always made sure his shy friend was invited. 'It's not a party without you,' he'd say.", "Make sure no friend is left out of plans or activities", "Included, valued, and wanted", "Inclusive, thoughtful, and loyal"),
            ("Help Without Expecting Anything Back", "Zara spent her Saturday helping her friend move. She didn't expect payment - just being a good friend was enough.", "Help a friend with something big without expecting a favor back", "Grateful, supported, and loved", "Selfless, generous, and dedicated"),
            ("Forgive a Mistake", "When a friend accidentally broke Liam's favorite toy, Liam said 'It's okay. Accidents happen. You're more important than stuff.'", "Forgive a friend who made a genuine mistake", "Relieved, grateful, and humbled", "Gracious, mature, and loving"),
        ],
        "Kindness to Strangers": [
            ("Smile at People", "Chloe decided to smile at every person she passed for one day. Seven people smiled back. Three said hello. One needed that smile.", "Smile at 10 people you don't know today", "Noticed, acknowledged, and uplifted", "Open, warm, and approachable"),
            ("Hold an Elevator or Door", "Aiden saw someone rushing toward the elevator and held it open. 'Thank you so much!' they said, out of breath but grateful.", "Hold doors or elevators for people behind you", "Noticed, respected, and helped", "Courteous, aware, and considerate"),
            ("Compliment a Stranger", "Nora told a woman at the store: 'I love your scarf! The color is beautiful.' The woman beamed for the rest of her shopping trip.", "Give a genuine compliment to a stranger (on something they chose)", "Flattered, happy, and seen", "Brave, kind, and observant"),
            ("Help Someone Carry Things", "Caleb saw an elderly man struggling with grocery bags and offered to carry them to his car. It took 2 minutes of his time.", "Offer to help someone who's carrying heavy things", "Relieved, grateful, and faith-in-humanity restored", "Strong, helpful, and generous"),
            ("Let Someone Go First", "At the water fountain, Emma let the younger kid go first even though she was thirsty. 'You go ahead,' she said kindly.", "Let someone go ahead of you in line today", "Surprised, respected, and grateful", "Patient, generous, and mature"),
            ("Return a Lost Item", "Lucas found a wallet in the park. Instead of keeping the money, he turned it in to the police station.", "If you find something lost, make an effort to return it", "Relieved, grateful, and amazed", "Honest, responsible, and ethical"),
            ("Say Please and Thank You Extra", "Mia made a point of looking service workers in the eye and saying 'Thank you so much, I really appreciate it.'", "Use extra-genuine please and thank you with everyone today", "Respected, valued, and seen as a person", "Polite, genuine, and respectful"),
            ("Give Away Something You Love", "Jackson had two of the same book. Instead of keeping both, he left one on a bench with a note: 'Free! Enjoy this story!'", "Give away something you own that someone else might enjoy", "Surprised, delighted, and gifted", "Generous, unattached, and giving"),
            ("Write a Positive Online Review", "Aria wrote a glowing review for a small local restaurant. The owner posted it on their wall.", "Write a positive review for a local business you like", "Appreciated, supported, and encouraged", "Supportive, helpful, and articulate"),
            ("Pick Up Litter", "Oliver spent 15 minutes picking up trash at the park. He didn't tell anyone. The park just looked better.", "Pick up litter in a public space (bring gloves!)", "Better environment for all, even if they don't know who did it", "Responsible, caring, and community-minded"),
        ],
        "Kindness to Yourself": [
            ("Take a Break Without Guilt", "After studying for 2 hours, Zara closed her books and played outside for 30 minutes. She came back refreshed and focused.", "Give yourself permission to rest when you need it", "Others see you: calm, refreshed, balanced", "Rested, recharged, and guilt-free"),
            ("Say Something Nice to Yourself", "Every morning, Liam looked in the mirror and said one nice thing: 'I'm a good friend.' It felt weird at first but helped.", "Say 3 nice things to yourself in the mirror today", "You deserve kindness from yourself too!", "Confident, self-loving, and positive"),
            ("Forgive Yourself for a Mistake", "Chloe forgot her friend's birthday. Instead of beating herself up for days, she apologized and moved on. She's human.", "Forgive yourself for something you feel guilty about", "You'll make mistakes - that's human!", "Self-compassionate, growing, and free"),
            ("Celebrate Your Own Wins", "Aiden got a B+ on a test he expected to fail. He celebrated! Not everything has to be perfect to be worth celebrating.", "Write down 5 things you're proud of this week", "Your achievements matter - notice them!", "Proud, accomplished, and self-aware"),
            ("Set a Boundary", "Nora's friend wanted to copy her homework. Nora said 'I can help you understand it, but I can't let you copy.' It was hard but right.", "Say 'no' to something that doesn't feel right, even if it's hard", "Others respect boundaries (even if surprised at first)", "Strong, self-respecting, and principled"),
            ("Try Something New", "Caleb was scared to try swimming. He signed up anyway, was terrible at first, and loved it within a month.", "Try one new thing this week that scares you a little", "Growth comes from courage!", "Brave, growing, and adventurous"),
            ("Ask for Help", "Emma was drowning in homework but afraid to seem 'dumb.' She finally asked the teacher for help. It changed everything.", "Ask for help with something you're struggling with", "Getting help is smart, not weak!", "Humble, wise, and self-aware"),
            ("Spend Time in Nature", "Lucas put down his phone and spent 30 minutes just sitting outside watching clouds. His mind felt clearer after.", "Spend 20+ minutes outside without screens today", "Nature reduces stress hormones naturally!", "Peaceful, grounded, and present"),
            ("Move Your Body for Fun", "Mia stopped thinking of exercise as punishment and started dancing in her room just for fun. Movement is joy!", "Do physical activity purely for fun (not fitness) today", "Movement releases happy chemicals in your brain!", "Joyful, energetic, and free"),
            ("Write Down Things You Love About Yourself", "Jackson made a list of 20 things he liked about himself. On bad days, he re-read it. It always helped.", "Write a list of 10+ things you love about yourself", "Self-love is the foundation of all other love!", "Self-aware, confident, and grounded"),
        ],
    }

    title_page(doc, "THE KINDNESS CHALLENGE", "50 Ways to Change the World (Ages 6-12)", "50 Challenges * Stories * Reflections * 30-Day Tracker")
    copyright_page(doc, "THE KINDNESS CHALLENGE: 50 Ways to Change the World")
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0)
    doc.add_line(180, 710, 432, 710, 1, 0.3)
    y = 680
    for cat in categories:
        doc.add_text(72, y, f"{cat} (10 Challenges)", 'F2', 13, 0.1)
        y -= 30
    doc.add_text(72, y, "30-Day Kindness Tracker", 'F4', 13, 0.2)
    y -= 25
    doc.add_text(72, y, "Kindness Journal Pages", 'F4', 13, 0.2)
    y -= 25
    doc.add_text(72, y, "Certificate of Kindness", 'F4', 13, 0.2)
    doc.new_page()

    # Intro
    doc.add_centered_text(720, "WHY KINDNESS MATTERS", 'F2', 18, 0)
    y = add_wrapped(doc, 72, 680, "Did you know that being kind actually makes YOUR brain happier? Scientists have proven that acts of kindness release feel-good chemicals in your brain. Kindness is contagious - when you're kind to one person, they're more likely to be kind to someone else. One act of kindness can create a chain reaction that touches dozens of people! This book gives you 50 specific ways to spread kindness. Each one is simple, doable, and powerful. Are you ready to change the world, one kind act at a time?", 'F4', 12, 0.2)
    doc.new_page()

    challenge_num = 0
    for cat_name, challenges in categories.items():
        # Category divider
        doc.add_filled_rect(50, 380, 512, 120, 0.9)
        doc.add_centered_text(450, cat_name.upper(), 'F2', 24, 0)
        doc.add_centered_text(410, f"Challenges {challenge_num+1}-{challenge_num+10}", 'F1', 14, 0.3)
        doc.new_page()
        
        for name, story, how_to, others_feel, you_feel in challenges:
            challenge_num += 1
            doc.add_text(72, 730, f"CHALLENGE #{challenge_num}", 'F1', 10, 0.4)
            doc.add_text(72, 708, name, 'F2', 16, 0)
            doc.add_line(72, 700, 350, 700, 1, 0.3)
            
            y = 675
            doc.add_text(72, y, "STORY:", 'F2', 11, 0.1)
            y -= 18
            y = add_wrapped(doc, 90, y, story, 'F4', 10, 0.2, 70)
            
            y -= 18
            doc.add_text(72, y, "YOUR CHALLENGE:", 'F2', 11, 0.1)
            y -= 18
            y = add_wrapped(doc, 90, y, how_to, 'F1', 10, 0.2, 70)
            
            y -= 18
            doc.add_text(72, y, f"How it makes others feel: {others_feel}", 'F1', 10, 0.3)
            y -= 18
            doc.add_text(72, y, f"How it makes YOU feel: {you_feel}", 'F1', 10, 0.3)
            
            y -= 25
            doc.add_text(72, y, "MY REFLECTION:", 'F2', 11, 0.1)
            y -= 18
            doc.add_text(90, y, "I did this on (date): _________ Here's what happened:", 'F1', 10, 0.4)
            y -= 18
            doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
            y -= 18
            doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
            
            stars = "Difficulty: * easy  ** medium  *** brave"
            doc.add_text(72, y-30, stars, 'F3', 9, 0.4)
            doc.new_page()

    # 30-day tracker
    doc.add_centered_text(720, "30-DAY KINDNESS TRACKER", 'F2', 18, 0)
    doc.add_centered_text(695, "Check off each day you do a kind act!", 'F4', 12, 0.3)
    y = 660
    for day in range(1, 31):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "KINDNESS TRACKER (continued)", 'F2', 16, 0)
            y = 690
        doc.add_text(72, y, f"Day {day:2d}: [ ] Kind act: ______________________ How I felt: __________", 'F1', 10, 0.3)
        y -= 20
    doc.new_page()

    # Journal pages
    for p in range(3):
        doc.add_centered_text(720, "KINDNESS JOURNAL", 'F2', 16, 0)
        doc.add_text(72, 690, "Date: ___________ My kind act today: _____________________________", 'F1', 11, 0.3)
        doc.add_text(72, 660, "Who was it for? __________________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 630, "What happened: ___________________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 600, "___________________________________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 570, "How they reacted: ________________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 540, "How I felt: ______________________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 510, "Will I do this again? YES / NO  Why? _____________________________", 'F1', 11, 0.3)
        doc.add_text(72, 470, "Draw or write about your kindness moment:", 'F2', 11, 0.3)
        doc.add_rect(72, 200, 468, 260, 1, 0.5)
        doc.new_page()

    certificate(doc, "KINDNESS CHAMPION CERTIFICATE")
    add_supplemental(doc, 'Kindness', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book331_Kids_Kindness_Challenge.pdf')
    print("Book331_Kids_Kindness_Challenge.pdf created successfully!")

if __name__ == "__main__":
    create_book()
