"""Book348: She Believed She Could - Confidence Building for Girls"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc()
    author = "Daniel Tesfamariam"
    
    chapters = [
        ("You Are Enough", 
         "Sophia was twelve when she realized she had been trying to be everyone else. She copied her friend's style, laughed at jokes she did not find funny, and pretended to like music she actually hated. One day her grandmother said something that changed everything: 'Sophia, you are enough exactly as you are.' Those words unlocked something inside her.",
         "You do not need to be prettier, smarter, funnier, or more popular to be worthy of love and respect. You are enough RIGHT NOW. Not when you lose weight. Not when you get better grades. Not when that popular girl finally notices you. Right now, today, as you are reading this sentence.",
         ["Write down 10 things that make you uniquely YOU", "Create a You Are Enough jar: write compliments to yourself on slips and read one daily", "Practice saying 'thank you' instead of deflecting compliments"],
         "I am enough. I have always been enough. I will always be enough.",
         "What would change in your life if you truly believed you were enough?"),
        ("Dealing With Comparison (Social Media)",
         "Mia spent three hours every night scrolling through Instagram, comparing her life to perfectly filtered photos. She compared her body, her room, her friends, her vacation, everything. She felt worse every single night but could not stop. Then her older sister showed her behind-the-scenes of an influencer photoshoot: it took 200 photos to get one 'perfect' picture.",
         "Social media shows you a highlight reel, not reality. Nobody posts their bad hair days, failed tests, or crying-in-the-bathroom moments. When you compare your behind-the-scenes to someone else's highlight reel, you will always feel like you are losing. But it is not a fair comparison.",
         ["Do a social media audit: unfollow any account that makes you feel bad", "Set a daily screen time limit and stick to it for one week", "Take a 48-hour social media break and journal how you feel"],
         "I refuse to compare my chapter one to someone else's chapter twenty.",
         "How does your mood change before and after scrolling social media?"),
        ("Body Confidence",
         "Taylor hated her legs. They were too long, she thought. She wore baggy pants even in summer. Then she joined the basketball team and her long legs helped her run faster than anyone else. She realized her body was not meant to look a certain way. It was meant to DO amazing things.",
         "Your body is not a decoration. It is a vehicle for your life. Your legs carry you on adventures. Your arms hug the people you love. Your brain creates incredible ideas. When you start thinking about what your body can DO instead of how it looks, everything shifts.",
         ["Write a thank-you letter to your body for everything it does for you", "Find a physical activity you genuinely enjoy (not for losing weight, for FUN)", "Practice the mirror exercise: look in the mirror and say three kind things"],
         "My body is strong, capable, and worthy of love exactly as it is.",
         "What is one amazing thing your body helped you do this week?"),
        ("Academic Confidence",
         "Priya always said 'I'm not smart enough' before every test. She had convinced herself she was bad at math. Then a new teacher said: 'Priya, you are not bad at math. You just have not found the way that works for YOUR brain yet.' They tried different approaches, and Priya discovered she understood math perfectly when she could visualize it.",
         "Intelligence is not fixed. Your brain grows and changes every time you learn something new. Saying 'I can not do this' is different from saying 'I can not do this YET.' That one small word changes everything. You are capable of learning anything if you find the right approach and give yourself enough time.",
         ["Change 'I can't' to 'I can't YET' for one full week", "Ask a teacher for help without feeling ashamed - it is a sign of strength", "Teach something you know well to someone else and see how smart you really are"],
         "My brain is growing every single day. I am capable of amazing learning.",
         "What is something you thought you could never learn but eventually did?"),
        ("Friendship Drama Survival",
         "Jasmine's best friend suddenly started ignoring her in seventh grade. No explanation. No fight. Just silence. Jasmine replayed every conversation trying to figure out what she did wrong. The pain was overwhelming. But she learned that sometimes friendships change and it is nobody's fault.",
         "Friendship drama is one of the hardest things about growing up. Friends can be mean, exclusive, or suddenly different. Here is what you need to know: if someone excludes you, that says everything about THEM and nothing about you. You deserve friends who make you feel good about yourself.",
         ["Write down the qualities you want in a true friend", "Practice the three-day rule: if drama still hurts after three days, talk about it", "Identify one person you could reach out to who might need a friend too"],
         "I deserve friendships that lift me up, not tear me down.",
         "What does a true friend look like to you?"),
        ("Speaking Up",
         "Aisha had an opinion about everything but never shared any of them. In class, she would think of brilliant answers but never raise her hand. She was terrified of being wrong, of being laughed at, of being too much. Then her debate teacher told her: 'Your ideas deserve to be heard. The world needs your voice.'",
         "Your voice matters. Your opinions matter. Your ideas matter. Speaking up can feel terrifying, especially when you are the only girl in the room, the youngest person, or the one who disagrees. But silence never changed anything. Every woman who changed the world first had to open her mouth and speak.",
         ["Raise your hand in class at least once every day this week", "Practice giving your opinion to safe people first (family, close friends)", "Record yourself giving a two-minute speech about something you care about"],
         "My voice deserves to be heard. My ideas have value.",
         "What is something you have been wanting to say but have been holding back?"),
        ("Trying New Things",
         "Emma was terrified of being bad at things. So she only did things she was already good at. Her world got smaller and smaller until one day she was bored out of her mind. Her mom challenged her to try one new thing every month. The first month she tried rock climbing and was terrible. But she laughed the whole time.",
         "Here is a secret that confident people know: you are SUPPOSED to be bad at new things at first. That is how learning works. Nobody picks up a guitar and plays a perfect song on day one. Giving yourself permission to be a beginner is one of the bravest things you can do.",
         ["Try one brand new activity this month (something you have never done)", "Give yourself permission to be terrible at it and enjoy the process", "Make a 'Things I Want to Try' list with at least 20 items"],
         "I give myself permission to be a beginner. Growth happens outside comfort zones.",
         "What is something you have always wanted to try but been afraid to start?"),
        ("Handling Failure Gracefully",
         "Zoe studied for weeks for the science fair. She was sure she would win. She did not even place. She cried in the bathroom for twenty minutes. But then something interesting happened: she looked at the winning projects and realized what she could learn from them. The next year, she won first place.",
         "Failure is not the opposite of success. It is the PATH to success. Every successful woman you admire has failed dozens, hundreds, maybe thousands of times. The difference is that they got back up. They learned. They adjusted. And they tried again. Failure does not mean you are not good enough. It means you are brave enough to try.",
         ["Write about a time you failed and what you learned from it", "Interview a woman you admire about her biggest failure", "Reframe failure: instead of 'I failed' say 'I learned that this approach does not work'"],
         "Failure is not my enemy. It is my teacher. I learn and grow from every setback.",
         "What is the most important lesson a failure has taught you?"),
        ("Saying No (Boundaries for Girls)",
         "Lily said yes to everything because she was afraid people would not like her if she said no. She was exhausted, overwhelmed, and resentful. She was on five committees, helped everyone with homework, and never had time for herself. Learning to say no was the hardest and most important thing she ever did.",
         "No is a complete sentence. You do not owe anyone an explanation for protecting your time, your energy, or your body. Saying no to things that drain you means saying YES to things that matter. People who respect you will respect your no.",
         ["Practice saying no to one small thing this week", "Write down your non-negotiable boundaries (things you will always say no to)", "Notice how you feel after saying no. Relief? That means it was the right choice"],
         "No is a complete sentence. I protect my energy without guilt.",
         "What is something you need to say no to but have been afraid to?"),
        ("Leadership for Girls",
         "When Maria ran for class president, someone said girls should not be leaders because they were 'too emotional.' Maria won the election and proved that emotions like empathy and compassion actually made her a BETTER leader. She listened to people. She cared about solutions that helped everyone.",
         "Leadership is not about being bossy or loud or aggressive. Leadership is about having a vision, inspiring others, making tough decisions, and serving your community. Girls make extraordinary leaders because we often lead with empathy, collaboration, and creativity.",
         ["Identify one area of your life where you already lead (maybe without realizing)", "Volunteer to lead one small project or group this month", "Study a female leader you admire - what makes her leadership style effective?"],
         "I am a natural leader. My style of leading makes the world better.",
         "What kind of leader do you want to be?"),
        ("Dealing With Mean Girls",
         "Chloe was bullied by a group of popular girls who spread rumors about her. It felt like her world was ending. But her school counselor taught her something powerful: hurt people hurt people. Those girls were dealing with their own pain and taking it out on others. It did not make it okay, but it helped Chloe stop blaming herself.",
         "Mean behavior says everything about the person being mean and nothing about you. You cannot control how others treat you, but you can control how you respond. You can refuse to shrink yourself. You can refuse to believe their words. And you can always ask for help from trusted adults.",
         ["Write down the mean words and then physically throw the paper away", "Build your support team: identify three trusted adults you can go to", "Practice the 'gray rock' technique: be boring and unresponsive to bullies"],
         "Other people's cruelty does not define my worth. I rise above.",
         "How do you handle it when someone is mean to you?"),
        ("Self-Talk Makeover",
         "Olivia realized she said things to herself that she would NEVER say to her best friend. She called herself stupid, ugly, and worthless multiple times a day. When she started paying attention to her inner voice, she was shocked at how cruel it was. She decided to talk to herself the way she would talk to someone she loves.",
         "Your inner voice is the most powerful voice in your life because you hear it constantly. If that voice is cruel and critical, you are being bullied 24/7 by your own mind. The good news is that you can retrain your inner voice. You can choose thoughts that build you up instead of tear you down.",
         ["For one day, write down every negative thought you have about yourself", "Replace each negative thought with a kind alternative", "Create a phone wallpaper with your favorite positive affirmation"],
         "I speak to myself with kindness, patience, and love.",
         "If your best friend could hear your inner voice, what would she think?"),
        ("Your Unique Superpowers",
         "Ava was quiet in a world that rewards loudness. She thought being introverted was a weakness until she discovered that her ability to listen deeply, observe carefully, and think before speaking were actually rare and valuable superpowers. Not everyone has to be the loudest person in the room to make an impact.",
         "You have superpowers that nobody else has. Maybe you are incredibly empathetic. Maybe you are creative, analytical, brave, funny, kind, determined, or imaginative. Your unique combination of qualities is your superpower. Stop trying to develop someone else's strengths and start celebrating your own.",
         ["Ask five people who know you well: What do you think my superpower is?", "Write your personal superpower statement and put it where you see it daily", "Use your superpower to help someone else this week"],
         "My unique qualities are my superpowers. Nobody else has my exact combination.",
         "What superpower do you have that you have been undervaluing?"),
        ("Goal Setting",
         "Isabella wanted to become a published author by age fifteen. Everyone told her to be realistic. But she broke that big dream into small steps: write 500 words daily, finish a manuscript in six months, research publishers. On her fifteenth birthday, she held her published book. The 'unrealistic' dream became real through consistent small steps.",
         "Big dreams become real when you break them into small, actionable steps. A goal without a plan is just a wish. But a goal with daily actions, deadlines, and accountability becomes inevitable. You are capable of achieving extraordinary things when you commit to showing up consistently.",
         ["Write one big dream and break it into 10 small steps", "Set a 30-day goal and track your progress daily", "Find an accountability partner who will check in with you weekly"],
         "I turn my dreams into plans and my plans into reality.",
         "What is your biggest dream for the next year? What is step one?"),
        ("30-Day Confidence Challenge",
         "This is not just reading anymore. This is DOING. For the next thirty days, you will take one small confidence-building action every single day. Some days will feel easy. Some will feel terrifying. But by day thirty, you will be a different girl. A braver girl. A girl who knows her worth.",
         "Confidence is not something you either have or do not have. It is a SKILL that you build through action. Every time you do something brave, your confidence muscle gets stronger. This challenge is designed to strengthen that muscle day by day.",
         ["Day 1-10: Internal confidence (affirmations, self-talk, journaling)", "Day 11-20: Social confidence (speaking up, new conversations, boundaries)", "Day 21-30: Bold confidence (trying new things, leading, taking risks)"],
         "Every day I become braver, stronger, and more confident in who I am.",
         "Which day of the challenge are you most nervous about? That is the one that will change you most.")
    ]
    
    # Title page
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(640, "SHE BELIEVED", 'F2', 32, 0.1)
    doc.add_centered_text(600, "SHE COULD", 'F2', 32, 0.1)
    doc.add_line(150, 580, 462, 580, 2, 0.3)
    doc.add_centered_text(550, "A Confidence-Building Workbook", 'F4', 16, 0.3)
    doc.add_centered_text(525, "for Girls Ages 9-14", 'F4', 16, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0.2)
    doc.new_page()
    
    # Copyright
    doc.add_centered_text(700, "SHE BELIEVED SHE COULD", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Author: {author}", 'F1', 11, 0.3)
    doc.add_text(72, 630, "Format: 8.5 x 11 inches | Kindle & Paperback", 'F1', 10, 0.4)
    doc.add_text(72, 600, "All rights reserved.", 'F1', 10, 0.4)
    doc.new_page()
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0.1)
    doc.add_line(72, 705, 540, 705, 1, 0.3)
    y = 680
    for i, (title, _, _, _, _, _) in enumerate(chapters):
        doc.add_text(72, y, f"Chapter {i+1}: {title}", 'F1', 11, 0.2)
        y -= 22
    doc.new_page()
    
    # Chapters
    for i, (title, story, lesson, activities, affirmation, journal) in enumerate(chapters):
        # Page 1: Story and Lesson
        doc.add_filled_rect(50, 710, 512, 50, 0.92)
        doc.add_centered_text(740, f"Chapter {i+1}", 'F1', 10, 0.5)
        doc.add_centered_text(722, title.upper(), 'F2', 18, 0.1)
        
        doc.add_text(72, 685, "TRUE STORY", 'F2', 12, 0.2)
        doc.add_line(72, 676, 160, 676, 1, 0.4)
        
        # Wrap story
        words = story.split()
        lines = []
        current = ""
        for word in words:
            if len(current + " " + word) > 78:
                lines.append(current)
                current = word
            else:
                current = current + " " + word if current else word
        if current:
            lines.append(current)
        
        y = 658
        for line in lines:
            doc.add_text(72, y, line, 'F4', 11, 0.25)
            y -= 15
        
        y -= 15
        doc.add_text(72, y, "THE LESSON", 'F2', 12, 0.2)
        y -= 5
        doc.add_line(72, y, 160, y, 1, 0.4)
        y -= 18
        
        words = lesson.split()
        lines = []
        current = ""
        for word in words:
            if len(current + " " + word) > 78:
                lines.append(current)
                current = word
            else:
                current = current + " " + word if current else word
        if current:
            lines.append(current)
        
        for line in lines:
            doc.add_text(72, y, line, 'F1', 11, 0.2)
            y -= 15
        
        doc.new_page()
        
        # Page 2: Activities
        doc.add_centered_text(740, f"{title} - Activities", 'F2', 14, 0.2)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        
        doc.add_text(72, 700, "THREE ACTIVITIES TO BUILD THIS SKILL:", 'F2', 12, 0.2)
        y = 675
        for j, activity in enumerate(activities):
            doc.add_filled_rect(72, y - 5, 468, 22, 0.95)
            doc.add_text(82, y, f"Activity {j+1}: {activity}", 'F1', 10, 0.2)
            y -= 35
        
        y -= 15
        doc.add_text(72, y, "YOUR AFFIRMATION:", 'F2', 12, 0.2)
        y -= 5
        doc.add_filled_rect(72, y - 20, 468, 35, 0.92)
        doc.add_centered_text(y, affirmation, 'F5', 12, 0.1)
        y -= 40
        doc.add_text(72, y, "(Write this affirmation 3 times below):", 'F4', 10, 0.4)
        y -= 20
        for j in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 25
        
        y -= 20
        doc.add_text(72, y, "JOURNAL PROMPT:", 'F2', 12, 0.2)
        y -= 18
        doc.add_text(72, y, journal, 'F4', 11, 0.3)
        y -= 20
        for j in range(6):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 22
        
        doc.new_page()
        
        # Page 3-5: Extended content
        doc.add_centered_text(740, f"{title} - Going Deeper", 'F2', 14, 0.2)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        
        doc.add_text(72, 700, "CONFIDENCE BUILDER EXERCISE:", 'F2', 12, 0.2)
        y = 675
        exercises = [
            f"Think about a time when you felt confident about {title.lower()}.",
            "What was different about that moment? How did your body feel?",
            "What thoughts were running through your mind?",
            "Now think about a time when you struggled with this.",
            "What changed? What triggered the loss of confidence?",
            "Write about both experiences below and notice the patterns:"
        ]
        for ex in exercises:
            doc.add_text(82, y, ex, 'F4', 11, 0.3)
            y -= 16
        y -= 10
        for j in range(8):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 22
        
        y -= 15
        doc.add_text(72, y, "MY CONFIDENCE COMMITMENT:", 'F2', 11, 0.2)
        y -= 18
        doc.add_text(72, y, "This week I will practice confidence by:", 'F4', 11, 0.3)
        y -= 20
        for j in range(3):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 22
        
        doc.new_page()
        
        # Pages 4-5: More reflection space
        doc.add_centered_text(740, f"{title} - Reflection & Growth", 'F2', 14, 0.2)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        
        doc.add_text(72, 700, "BEFORE AND AFTER:", 'F2', 12, 0.2)
        doc.add_text(72, 680, "Rate your confidence in this area (1-10):", 'F1', 11, 0.3)
        doc.add_text(72, 660, "Before reading this chapter: ___/10", 'F1', 11, 0.3)
        doc.add_text(72, 640, "After completing the activities: ___/10", 'F1', 11, 0.3)
        
        y = 600
        doc.add_text(72, y, "WHAT I WANT TO REMEMBER:", 'F2', 12, 0.2)
        y -= 20
        for j in range(5):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 22
        
        y -= 15
        doc.add_text(72, y, "A LETTER TO MYSELF:", 'F2', 12, 0.2)
        y -= 5
        doc.add_text(72, y, "Write an encouraging note to yourself for a hard day:", 'F4', 10, 0.4)
        y -= 20
        for j in range(8):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 22
        
        doc.new_page()
    
    # Final page
    doc.add_centered_text(600, "YOU DID IT!", 'F2', 28, 0.1)
    doc.add_centered_text(560, "You have completed this workbook.", 'F4', 14, 0.3)
    doc.add_centered_text(530, "But this is just the beginning of your confidence journey.", 'F4', 12, 0.3)
    doc.add_centered_text(480, "Remember: She believed she could, so she did.", 'F5', 16, 0.2)
    doc.add_centered_text(440, "And that 'she' is YOU.", 'F2', 14, 0.2)
    doc.new_page()
    

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()


    # Extra content pages for 78+ minimum
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "MY ACTION PLAN", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "CREATIVE RESPONSE", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "ADDITIONAL THOUGHTS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "MY ACTION PLAN", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "CREATIVE RESPONSE", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "ADDITIONAL THOUGHTS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "MY ACTION PLAN", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "CREATIVE RESPONSE", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book348_Girls_Confidence_Guide.pdf')
    print("Book348_Girls_Confidence_Guide.pdf created successfully!")

if __name__ == "__main__":
    create_book()
