from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    chapters = [
        ("What Is Leadership?", "Leadership isn't about being the boss, the loudest, or the most popular. Real leadership is about making things better for everyone around you. A leader is someone who sees a problem and takes action, inspires others to do their best, and serves the people they lead. You don't need a title or a position to be a leader - you just need to care and act.",
         "Marley, age 11, noticed younger kids at recess had nobody to play with. She started a 'Recess Buddies' program where older kids invited younger ones to join games. Soon, 15 other kids volunteered as buddies. Marley didn't wait for permission - she saw a need and filled it.",
         "What would YOU do: You notice a new student looks lost on their first day. A) Wait for a teacher to help B) Walk over and offer to show them around C) Hope someone else does it"),
        ("Types of Leaders", "There are many styles of leadership! SERVANT leaders put others first. VISIONARY leaders see the future and inspire others. DEMOCRATIC leaders involve everyone in decisions. COACHING leaders help others grow. QUIET leaders lead by example without fanfare. No style is 'best' - great leaders adapt their style to what's needed.",
         "At age 10, Ryan Hreljac learned that people in Africa didn't have clean water. He raised $70 doing chores to build ONE well. His small start inspired others - his foundation has now built 1,300+ water projects serving 1 million people! He's a visionary servant leader.",
         "What's YOUR leadership style? Think about how you naturally help others. Do you take charge, support quietly, include everyone, or inspire with ideas?"),
        ("Communication Skills", "Great leaders are great communicators! This means speaking clearly, writing well, AND listening deeply. Communication isn't just about talking - it's about making sure your message is understood. Good communicators use simple words, tell stories, make eye contact, and check that others understand. They adjust how they communicate based on who they're talking to.",
         "Jaylen, 12, wanted to convince his principal to start a school garden. He didn't just ask - he prepared! He researched benefits, created a presentation, and even brought sample plants. His clear communication convinced the principal in one meeting. The garden is now the school's pride.",
         "Practice: Explain a complicated topic (like how WiFi works) to a 5-year-old. If they understand, you're communicating like a leader!"),
        ("Listening Is a Superpower", "Most people listen to reply. Leaders listen to UNDERSTAND. Active listening means: giving full attention, not interrupting, asking follow-up questions, and making the speaker feel heard. When people feel truly listened to, they trust you more, share more openly, and follow your lead willingly. Listening is the most underrated leadership skill!",
         "Aisha was class president. Instead of just making decisions, she held weekly 'listening lunches' where any student could share concerns. She took notes and acted on what she heard. Students said they felt more connected to school because someone was actually LISTENING.",
         "Try this: In your next conversation, don't think about what you'll say next. Just focus entirely on understanding the other person. Notice how different it feels."),
        ("Making Decisions", "Leaders must make decisions - sometimes tough ones! Good decision-making involves: gathering information, considering different perspectives, thinking about consequences, making a choice, and taking responsibility for the outcome. You won't always be right, but making a thoughtful decision is always better than making no decision at all.",
         "Marcus, 13, was team captain. With 30 seconds left and his team down by one point, he had to decide: pass to the best player (who was closely guarded) or give the ball to a less experienced player who was wide open. He chose trust over talent - the open player scored! Good decision under pressure.",
         "Decision framework: 1) What are my options? 2) What happens with each choice? 3) Who is affected? 4) What feels RIGHT? 5) Decide and own it."),
        ("Handling Disagreements", "Conflict is normal and can actually make teams BETTER when handled well. Leaders don't avoid conflict - they manage it. This means: staying calm, hearing all sides, finding common ground, and working toward solutions where everyone wins something. The goal isn't 'winning' an argument - it's finding the best path forward for everyone.",
         "When two groups in Sophia's club wanted different field trip locations, she didn't pick a side. She said 'Let's list what each place offers and find one that has what BOTH groups want.' They found a place that satisfied everyone. Win-win!",
         "Conflict resolution steps: 1) Stay calm 2) Let each side speak 3) Find common ground 4) Brainstorm solutions together 5) Agree on a plan"),
        ("Team Building", "No leader succeeds alone. Great leaders build strong teams by: recognizing everyone's unique strengths, giving people roles that match their talents, creating a safe environment for ideas, celebrating wins together, and supporting each other through challenges. A team is stronger than any individual.",
         "When Noah directed the school play, he didn't just assign roles. He asked everyone: 'What are you BEST at?' Some wanted to act, others to build sets, paint, handle sound, or organize. By matching people to their strengths, the play was the best the school had ever seen.",
         "Team activity: List 5 friends and their unique strengths. How would you build a dream team for a project using each person's best skill?"),
        ("Being Responsible", "Responsible leaders do what they say they'll do, show up on time, admit mistakes, and take ownership of outcomes - good or bad. Responsibility means others can COUNT on you. It's built slowly through consistent actions and lost quickly through broken promises. Being responsible earns trust, and trust is a leader's most valuable currency.",
         "Elena promised to organize the charity fundraiser. When problems arose (the venue cancelled, a performer got sick), she didn't blame others or give up. She found solutions and delivered. People learned they could rely on her completely. That's responsibility.",
         "Rate yourself 1-10: Do people count on you? Do you follow through? Do you admit mistakes? Where can you improve?"),
        ("Leading by Example", "The most powerful leadership tool is YOUR OWN BEHAVIOR. People don't follow what you say - they follow what you DO. If you want your team to work hard, you work hardest. If you want kindness, you're the kindest. If you want honesty, you're the most honest. Leading by example means your actions match your words every single day.",
         "Coach Thompson never asked his players to do anything he wouldn't do. He ran every drill with them. He arrived first and left last. He admitted his own mistakes openly. His team didn't just respect him - they gave 100% because HE gave 100%.",
         "This week's challenge: Identify one behavior you want to see in others. Model it yourself consistently for 7 days. Watch what happens."),
        ("Courage to Stand Alone", "Sometimes leadership means standing up for what's right even when nobody supports you. This is the hardest kind of leadership. It might mean speaking against bullying when bystanders are silent, admitting an unpopular truth, or defending someone who can't defend themselves. Courage isn't the absence of fear - it's acting despite fear.",
         "When everyone laughed at the new kid's accent, Zara didn't join in. She said clearly: 'That's not funny. How would you feel?' The laughter stopped. It was uncomfortable for a moment, but several kids later thanked her privately. One brave voice changed the group.",
         "Reflect: When have you stayed silent when you should have spoken? What held you back? What would you do differently now?"),
        ("Serving Others", "The greatest leaders serve. They don't lead for power, fame, or control - they lead to make life better for others. Servant leadership means: putting others' needs first, lifting people up, sharing credit, and measuring success by how much you've helped. The most respected leaders in history were servants.",
         "Every Saturday, 13-year-old James organized neighborhood cleanups. He didn't do it for attention - he did it because he loved his community. He brought supplies, thanked every volunteer personally, and made sure everyone felt valued. People followed him because he genuinely served them.",
         "Service challenge: Do something this week to serve someone with NO recognition expected. How does it feel to give without getting credit?"),
        ("Your Leadership Plan", "You now have the tools to be an amazing leader! But knowledge without action is useless. Great leaders set goals, make plans, and take consistent action. Your leadership journey starts today - not someday in the future. You don't need to be perfect; you just need to start. What kind of leader will you be?",
         "Every great leader started exactly where you are right now. They were kids who decided to make a difference. MLK was organizing at 15. Malala spoke up at 11. Greta started her movement at 15. YOUR time is NOW.",
         "Create your plan: 1) What's one problem I want to solve? 2) Who do I need on my team? 3) What's my first step? 4) When will I start? (Answer: TODAY!)"),
    ]

    title_page(doc, "KIDS CAN LEAD", "How to Be a Leader at Any Age (Ages 9-14)", "12 Chapters * True Stories * Leadership Skills * Weekly Challenges")
    copyright_page(doc, "KIDS CAN LEAD: How to Be a Leader at Any Age")
    toc_page(doc, [c[0] for c in chapters])

    for idx, (ch_title, content, story, activity) in enumerate(chapters):
        chapter_header(doc, idx+1, ch_title)
        y = 580
        y = add_wrapped(doc, 72, y, content, 'F1', 11, 0.2)
        doc.new_page()

        # Story + activity page
        doc.add_centered_text(720, f"CHAPTER {idx+1}: YOUNG LEADER STORY", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        y = 685
        y = add_wrapped(doc, 72, y, story, 'F4', 11, 0.2)
        
        y -= 30
        doc.add_text(72, y, "YOUR LEADERSHIP CHALLENGE:", 'F2', 13, 0.1)
        y -= 20
        y = add_wrapped(doc, 90, y, activity, 'F1', 11, 0.2)
        
        y -= 30
        doc.add_text(72, y, "SELF-ASSESSMENT:", 'F2', 12, 0.1)
        y -= 20
        skills = ["Communication", "Listening", "Decision-making", "Responsibility", "Courage"]
        for sk in skills:
            doc.add_text(90, y, f"{sk}: 1 -- 2 -- 3 -- 4 -- 5 -- 6 -- 7 -- 8 -- 9 -- 10", 'F1', 10, 0.3)
            y -= 18

        y -= 20
        doc.add_text(72, y, "MY LEADERSHIP GOAL THIS WEEK:", 'F2', 12, 0.1)
        y -= 20
        doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
        y -= 18
        doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
        doc.new_page()

    # Leadership qualities summary
    doc.add_centered_text(720, "THE 12 QUALITIES OF A GREAT LEADER", 'F2', 16, 0)
    qualities = ["Vision - Sees what could be better", "Communication - Shares ideas clearly", "Listening - Truly hears others", "Decision-making - Chooses wisely under pressure", "Conflict resolution - Turns problems into solutions", "Team building - Brings out the best in people", "Responsibility - Follows through on commitments", "Integrity - Does right even when no one watches", "Courage - Acts despite fear", "Service - Puts others first", "Humility - Shares credit, takes blame", "Action - Starts TODAY, not someday"]
    y = 685
    for i, q in enumerate(qualities):
        doc.add_text(72, y, f"{i+1:2d}. {q}", 'F1', 11, 0.2)
        y -= 25
    doc.new_page()

    certificate(doc, "YOUNG LEADER CERTIFICATE")
    add_supplemental(doc, 'Leadership', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book335_Kids_Leadership.pdf')
    print("Book335_Kids_Leadership.pdf created successfully!")

if __name__ == "__main__":
    create_book()
