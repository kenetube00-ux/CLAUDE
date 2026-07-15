from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    chapters = [
        ("What Makes a Good Friend?", "A good friend is trustworthy, kind, supportive, fun, and honest. Good friends celebrate your wins, support you through hard times, keep your secrets safe, and accept you for who you are. They don't try to change you or make you feel bad about yourself. Friendship is a two-way street - you have to GIVE the qualities you want to RECEIVE.",
         "Alex and Jamie had been friends since kindergarten. When Alex didn't make the basketball team, Jamie didn't just say 'sorry.' Jamie said 'Let's practice together every day so you make it next year.' That's what a REAL friend does - they show up when things are hard, not just when things are fun.",
         ["What are your top 5 qualities in a friend?","Rate yourself: Are YOU showing those qualities to others?","Write about your best friendship moment ever"]),
        ("How to Start Conversations", "Making friends starts with talking to people! Starting conversations can feel scary, but it gets easier with practice. Try: asking questions (people love talking about themselves), making observations ('Cool shirt! Do you like that band?'), offering compliments, or sharing something about yourself. The key is genuine curiosity about the other person.",
         "Mia was the new kid AGAIN (third school in three years). This time, she had a plan. On day one, she sat next to someone reading a book she recognized: 'Is that Wings of Fire? I love that series!' That one question turned into a 30-minute conversation and a friendship that lasted years.",
         ["Practice 5 conversation starters you could use this week","Role-play: How would you start talking to someone at a new activity?","What questions could you ask to keep a conversation going?"]),
        ("Joining Groups", "Joining an existing friend group can feel intimidating, but there are strategies! Start by being friendly to everyone (not just the popular kids). Find groups with shared interests (clubs, sports, activities). Be yourself - don't pretend to be someone you're not. Show interest in what the group likes. Be patient - it takes time to become a true insider.",
         "Omar wanted to join the soccer kids at recess but felt like an outsider. Instead of waiting to be invited, he started by watching games and cheering. Then he asked 'Can I play next game?' They said yes. Within two weeks, they were saving him a spot on the team every day.",
         ["List 3 groups or activities you'd like to join","What's your strategy for joining each one?","Remember: it takes 50 hours of interaction to go from stranger to friend!"]),
        ("Handling Rejection", "Not everyone will want to be your friend, and that's OKAY. Rejection hurts, but it doesn't mean there's something wrong with you. It means that person isn't your match. There are 8 billion people on Earth - you only need a few good friends! When rejected, don't beg or change yourself. Thank them politely, feel your feelings, and move on to find YOUR people.",
         "When Leah asked a group if she could sit with them at lunch and they said 'this table is full,' it stung. She cried that night. But the next day, she sat at a different table and met Sam, who became her absolute best friend for life. Sometimes rejection is just redirection.",
         ["Write about a time rejection led to something better","How can you comfort yourself when rejection happens?","Remember: rejection is one person's opinion, not a fact about your worth"]),
        ("Being a Good Listener", "Everyone wants to feel heard. Being a good listener makes people WANT to be around you. Good listening means: making eye contact, putting your phone away, not interrupting, asking follow-up questions, and reflecting back what you heard. Don't just wait for your turn to talk - actually HEAR what they're saying.",
         "Kayla noticed her friend was talking less than usual. Instead of filling the silence with her own stories, Kayla asked: 'You seem quiet today. Is everything okay?' That simple question opened the door to a conversation that helped her friend through a really tough time.",
         ["Practice active listening: repeat back what someone says to you","Count how many times you interrupt today (try for zero!)","Ask 3 follow-up questions in your next conversation"]),
        ("Resolving Conflicts", "Even best friends fight sometimes! Conflict doesn't mean the friendship is over - it means you care enough to be honest. Healthy conflict resolution: 1) Cool down before talking. 2) Use 'I feel' statements (not 'You always...'). 3) Listen to their side. 4) Find a compromise. 5) Apologize for your part. 6) Forgive and move forward.",
         "Best friends Dante and Mateo had a huge fight when Mateo shared Dante's secret. Dante was FURIOUS. But instead of ending the friendship, Dante said: 'I feel hurt because I trusted you. Secrets are important to me.' Mateo apologized sincerely. They set new trust rules and their friendship became even stronger.",
         ["Write an 'I feel ___ when you ___' statement for a current conflict","What's your part in a recent disagreement? Own it.","Create friendship rules with your best friend"]),
        ("Dealing with Bullies", "Bullying is NOT normal conflict - it's repeated, intentional harm. If someone consistently hurts you physically, verbally, or socially, that's bullying. You should: 1) Tell a trusted adult. 2) Don't fight back (it escalates). 3) Stay with friends (safety in numbers). 4) Document what happens. 5) Know it's NOT your fault. You deserve to be safe.",
         "When kids at school started targeting Miguel with mean comments daily, he felt alone and ashamed. Finally, he told his teacher and parents. The school intervened, the behavior stopped, and Miguel learned the most important lesson: asking for help is STRENGTH, not weakness.",
         ["Know the difference: conflict (both sides) vs bullying (one-sided, repeated)","Who are 3 trusted adults you could tell if bullied?","How can you be an upstander (not bystander) when you see bullying?"]),
        ("Long-Distance Friendships", "When friends move away, it can feel like loss. But long-distance friendships CAN work with effort from both sides! Schedule regular video calls, send letters or care packages, play online games together, share memes and updates, and plan visits when possible. The friends who survive distance are often the strongest friendships of your life.",
         "When Priya's best friend moved 2,000 miles away, they were devastated. But they made a plan: video call every Sunday, text daily, watch the same shows and discuss them, and meet in person every summer. Three years later, they're still best friends - maybe even closer than before.",
         ["How could you maintain a friendship if your friend moved?","Create a long-distance friendship plan","Send a message RIGHT NOW to a friend you haven't talked to in a while"]),
        ("Online Friendship Safety", "The internet lets you connect with people worldwide, which is amazing - but also requires caution. Online safety rules: 1) Never share personal info (address, school, phone). 2) Don't meet online friends alone in person. 3) Tell an adult if someone makes you uncomfortable. 4) Remember: people online may not be who they say. 5) Be kind online - treat people as you would in person.",
         "Jayden loved playing games online and chatted with many players. When one asked for his school name and address to 'send a gift,' Jayden got a weird feeling. He told his mom, who confirmed it was a red flag. Jayden learned to trust his instincts about online interactions.",
         ["What personal information should you NEVER share online?","What would you do if an online friend asked to meet in person?","Create online safety rules you'll always follow"]),
        ("When Friendships Change", "People grow and change, and sometimes friendships grow apart. This is NORMAL and doesn't mean the friendship failed. You and your friend might develop different interests, join different groups, or simply grow in different directions. It's okay to let some friendships fade naturally while investing in ones that still bring you joy.",
         "Sara and Ruby were inseparable in 5th grade. But in 6th grade, Sara got into theater and Ruby into soccer. They drifted apart. At first Sara felt guilty. Then she realized: Ruby will always be special to her. They're just in different chapters now. Both are happy.",
         ["Think of a friendship that changed. How do you feel about it?","It's okay to outgrow friendships. What matters is gratitude for the good times.","Who are your current 'chapter' friends? Invest in them."]),
        ("Toxic vs Healthy Friendships", "Not all friendships are good for you. TOXIC friendships make you feel bad about yourself, pressure you to do wrong things, involve manipulation or control, and drain your energy. HEALTHY friendships make you feel good, respected, supported, and free to be yourself. You deserve healthy friendships. It's okay to walk away from toxic ones.",
         "Tyler's friend group pressured him to make fun of other kids to 'stay in.' It didn't feel right. After weeks of stomach aches before school, Tyler realized: friends who make you hurt others aren't friends. He walked away. It was lonely for a week - then he found better friends who liked the REAL him.",
         ["Red flags: jealousy, control, pressure, put-downs, secrets from you","Green flags: respect, support, freedom, honesty, celebration of your wins","Evaluate your friendships: are they healthy? Be honest."]),
        ("Being Your Own Best Friend", "Before you can be a great friend to others, you need to be a friend to YOURSELF. Self-friendship means: treating yourself with kindness, enjoying your own company, forgiving your mistakes, standing up for yourself, and knowing your worth even when alone. People who like themselves attract better friendships because they don't accept poor treatment.",
         "After a bad day, instead of spiraling into negativity, Zoe treated herself like she'd treat her best friend. She said 'Hey, today was rough, but you handled it. Tomorrow is fresh.' Self-compassion isn't selfish - it's necessary. Be as kind to yourself as you are to your friends.",
         ["Write yourself an encouraging letter as if from your best friend","List 10 things you like about yourself","Plan a 'self-date' - time doing something YOU love, alone and happy"]),
    ]

    title_page(doc, "THE FRIENDSHIP HANDBOOK", "How to Make, Keep & Be a Great Friend (Ages 7-12)", "12 Chapters * Stories * Skills * Role-Play Scripts * Challenges")
    copyright_page(doc, "THE FRIENDSHIP HANDBOOK")
    toc_page(doc, [c[0] for c in chapters])

    for idx, (ch_title, content, story, activities) in enumerate(chapters):
        chapter_header(doc, idx+1, ch_title)
        y = 580
        y = add_wrapped(doc, 72, y, content, 'F1', 11, 0.2)
        doc.new_page()

        doc.add_centered_text(720, f"CHAPTER {idx+1}: STORY & PRACTICE", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        doc.add_text(72, 685, "REAL-LIFE SCENARIO:", 'F2', 13, 0.1)
        y = add_wrapped(doc, 90, 665, story, 'F4', 11, 0.2)
        
        y -= 25
        doc.add_text(72, y, "YOUR ACTIVITIES:", 'F2', 13, 0.1)
        y -= 20
        for i, act in enumerate(activities):
            y = add_wrapped(doc, 90, y, f"{i+1}. {act}", 'F1', 10, 0.2, 68)
            y -= 12
        
        y -= 20
        doc.add_text(72, y, "FRIENDSHIP CHALLENGE THIS WEEK:", 'F2', 12, 0.1)
        y -= 18
        challenges = [
            "Show each friend quality to someone different this week.",
            "Start 3 conversations with people you don't usually talk to.",
            "Join one new group or activity this week.",
            "If rejected, say 'No problem!' and find someone else. Practice resilience.",
            "Practice listening without interrupting for one full day.",
            "Resolve one conflict using 'I feel' statements.",
            "Stand up for someone being treated unfairly.",
            "Send a message to a friend you haven't connected with recently.",
            "Review your online friendships. Are you being safe?",
            "Write a gratitude note to a friend from your past.",
            "Check: do your friendships energize or drain you?",
            "Spend quality time with yourself - discover what you enjoy alone.",
        ]
        doc.add_text(90, y, challenges[idx], 'F4', 10, 0.3)
        
        y -= 30
        doc.add_text(72, y, "SELF-REFLECTION:", 'F2', 12, 0.1)
        y -= 18
        doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
        y -= 16; doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
        doc.new_page()

    certificate(doc, "FRIENDSHIP CHAMPION CERTIFICATE")
    add_supplemental(doc, 'Friendship', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book339_Kids_Friendship_Guide.pdf')
    print("Book339_Kids_Friendship_Guide.pdf created successfully!")

if __name__ == "__main__":
    create_book()
