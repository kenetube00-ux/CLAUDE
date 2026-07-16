"""Book350: Growing Up Girl - Honest Guide to Puberty"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc()
    author = "Daniel Tesfamariam"
    
    chapters = [
        ("Your Body Is Changing (And That's Good!)",
         ["Your body is doing something incredible right now. It is growing from a girl's body into a woman's body, and that process is called puberty. It usually starts between ages 8 and 13, though every girl's timeline is different. There is no 'right' age to start.",
          "Puberty happens because your brain sends chemical signals called hormones through your body. These hormones, especially estrogen, tell your body it is time to grow and change. Think of hormones as text messages from your brain to your body parts saying 'hey, time to level up!'",
          "You might notice changes happening all at once, or they might come gradually over several years. Some girls develop earlier than their friends, some later. Both are completely normal. Your body has its own schedule and it knows exactly what it is doing.",
          "Changes you might notice: growing taller quickly, body shape changing (hips getting wider), skin becoming oilier, sweating more, new hair growing in different places, breasts beginning to develop, and eventually getting your period. All of these are signs that your amazing body is working perfectly.",
          "It is totally normal to have mixed feelings about these changes. You might feel excited one day and nervous the next. You might wish your body would hurry up or slow down. Whatever you feel is valid. This book is here to help you understand every change and feel confident through all of them."]),
        ("Breast Development",
         ["One of the first visible signs of puberty for most girls is breast development. It usually begins with small, tender bumps behind the nipples called breast buds. This can start as early as age 8 or as late as 13. One side often starts before the other, and that is completely normal!",
          "Breast development happens in stages over several years. First come the breast buds, then the area around the nipple (areola) gets larger and darker, then the breasts grow fuller. The whole process can take 3 to 5 years. There is no way to speed it up or slow it down.",
          "Every woman's breasts are different in size, shape, and color. There is no 'ideal' size. Small breasts, large breasts, and everything in between are all normal and healthy. Your breast size is determined mostly by genetics, the same way your eye color is.",
          "You might want a bra when breasts start developing, either for comfort or confidence. Sports bras and training bras are great first options. Ask a mom, aunt, or trusted woman to help you find one that fits comfortably. There is no rule about when you 'should' start wearing one.",
          "Important: breast tenderness before your period is normal. If you ever notice unusual pain, lumps, or discharge, it is okay to tell a parent or doctor. Taking care of your body is not embarrassing, it is smart."]),
        ("Body Hair",
         ["During puberty, hair starts growing in new places. Usually, it appears under your arms and in your pubic area first, then on your legs. This is completely natural and happens to every woman on earth. The hair might be thin and light at first, then become thicker and darker over time.",
          "There is no medical reason to remove body hair. It is there for protection and warmth. Whether you choose to shave, wax, or leave your body hair natural is entirely your personal choice. There is no wrong answer. Different cultures have different views on body hair.",
          "If you decide to try shaving, here are some tips: use a clean razor, always use shaving cream or soap, shave in the direction the hair grows at first, and never share razors. Ask a trusted adult to show you the first time. Small cuts are normal at first.",
          "Pubic hair is nothing to be embarrassed about. It serves an important purpose by protecting sensitive skin. It is a sign that your body is maturing normally. You never need to feel ashamed of it or compare yourself to what you see in media.",
          "Fun fact: the texture, color, and amount of body hair varies enormously between girls and is determined by genetics. Girls from different ethnic backgrounds may have more or less hair. All variations are normal and healthy."]),
        ("Skin Changes (Acne)",
         ["Those same hormones that cause puberty can also cause your skin to produce more oil. This extra oil can clog pores and cause pimples, blackheads, and breakouts. Almost every teenager gets acne to some degree. It does not mean you are dirty or doing something wrong.",
          "Basic skincare for puberty: wash your face twice daily with a gentle cleanser (not soap), do not scrub hard or pop pimples (this makes them worse and can cause scars), use oil-free moisturizer, and change your pillowcase often. These simple steps help a lot.",
          "If your acne is severe or very painful, it is okay to see a dermatologist. They have treatments that can help. Acne is a medical condition, not a character flaw. Many adults still deal with it too. You should never feel embarrassed about seeking help.",
          "What does NOT cause acne: eating chocolate, being dirty, or touching your face occasionally. What CAN make it worse: stress, not washing makeup off before bed, and hormonal changes around your period.",
          "Remember that social media photos use filters and editing. Nobody's skin is perfect all the time. Even the girls who look flawless in photos have breakouts. Acne is temporary and does not define you or your beauty."]),
        ("Growth Spurts",
         ["During puberty, you might grow several inches in just one year! This rapid growth is called a growth spurt. Girls typically have their biggest growth spurt about 1-2 years before getting their first period. You might wake up one morning and your pants are suddenly too short.",
          "Growth spurts can cause 'growing pains,' which are aches in your legs, especially at night. They are not actually caused by growing itself but by muscle fatigue from your rapidly growing bones. Stretching, warm baths, and gentle massage can help with discomfort.",
          "Your body might feel awkward during growth spurts. Your feet might grow before the rest of you, or your legs might seem disproportionally long. You might feel clumsy or trip over things more. This is temporary! Your body is adjusting to its new proportions.",
          "Girls typically reach their full adult height about 2 years after their first period begins. Most girls are close to their adult height by age 14 or 15, though some continue growing until 16 or 17. Your final height is mostly determined by genetics.",
          "During growth spurts, your body needs extra nutrition and rest. Eating well (especially calcium for bones and protein for muscles) and getting enough sleep (9-11 hours for teens) helps your body grow strong and healthy."]),
        ("Periods Explained Simply",
         ["Getting your period (also called menstruation) is a completely natural process that happens to every woman. Here is what is actually happening: each month, your uterus builds up a soft lining of tissue and blood in case a fertilized egg needs a cozy place to grow. If there is no pregnancy, the lining sheds. That shedding is your period.",
          "Most girls get their first period between ages 10 and 15. There is no way to predict exactly when yours will come, but it usually arrives about 2 years after breast development begins. You might notice a white or yellowish discharge in your underwear for several months before your first period.",
          "A typical period lasts 3 to 7 days. The blood might be bright red, dark brown, or even slightly pink. It might come out steadily or in small gushes. All of these are normal. You will probably use 3 to 6 pads or tampons per day, depending on your flow.",
          "Your first few periods might be irregular, coming randomly for the first year or two. This is normal as your body figures out its cycle. Eventually, most women develop a cycle between 21 and 35 days (measured from the first day of one period to the first day of the next).",
          "Important: getting your period does not mean anything is wrong with you. It is a sign that your body is healthy and working exactly as designed. It is not gross, shameful, or dirty. It is biology, and it is nothing to be embarrassed about."]),
        ("Period Products Guide",
         ["There are several options for managing your period, and you can choose what feels most comfortable for you. The main options are: pads (stick to your underwear), tampons (inserted inside), menstrual cups (reusable and inserted), and period underwear (absorbent underwear).",
          "Pads are the most popular choice for beginners. They stick to the inside of your underwear and absorb blood. They come in different sizes and thicknesses for light, medium, and heavy flow. Change them every 3-4 hours. Many girls start with pads before trying other options.",
          "Tampons are small cotton plugs that go inside your vagina to absorb blood before it comes out. They come with applicators for easier insertion. Always choose the lowest absorbency you need and change them every 4-8 hours. Never leave one in longer than 8 hours.",
          "Menstrual cups are small silicone cups that collect blood inside your body. They can be worn for up to 12 hours and are reusable for years. They take practice to insert and remove but are eco-friendly and economical. Many women love them once they get the hang of it.",
          "Keep an emergency kit in your backpack: a pad or tampon, an extra pair of underwear, and a small bag for disposal. Being prepared takes away the anxiety of surprise periods. Ask your school nurse where supplies are available at school."]),
        ("Cramps and PMS",
         ["Many girls experience cramps before or during their period. Cramps are caused by your uterus squeezing to shed its lining. They feel like dull aches or sharp pains in your lower belly. Some girls barely feel them while others find them quite painful. Both are normal.",
          "Ways to ease cramps: a heating pad on your lower belly, gentle exercise like walking or stretching, over-the-counter pain relief (ask a parent first), drinking warm tea, taking a warm bath, or lying in a comfortable position with your knees drawn up.",
          "PMS stands for Premenstrual Syndrome. It refers to symptoms that happen in the week before your period: mood swings, bloating, headaches, food cravings, tiredness, breast tenderness, and feeling emotional. Not every girl gets PMS, and symptoms vary widely.",
          "PMS happens because hormone levels change before your period. Eating well, exercising regularly, getting enough sleep, and reducing stress can all help manage PMS symptoms. If PMS severely affects your life, a doctor can help.",
          "It is important to track your period on a calendar or app so you can predict when PMS and cramps might happen. Knowing when to expect them helps you prepare and feel more in control. Many free apps make tracking easy and private."]),
        ("Body Odor and Hygiene",
         ["During puberty, your sweat glands become more active, especially under your arms and in your genital area. This sweat mixes with bacteria on your skin and can cause body odor. It is nothing to be ashamed of; it happens to everyone. Good hygiene manages it easily.",
          "Daily hygiene during puberty: shower or bathe daily, use deodorant or antiperspirant under your arms, wear clean underwear and clothes each day, wash your face morning and night, and keep your hair clean. These simple habits keep you feeling fresh and confident.",
          "Your vaginal area cleans itself naturally. You only need to wash the outside with warm water. Never use scented soaps, sprays, or douches inside or around your vagina. They can disrupt your natural pH balance and cause infections. Simple warm water is best.",
          "Some vaginal discharge is normal and healthy. It is your body's way of keeping itself clean. Healthy discharge is clear or slightly white and does not have a strong smell. If discharge is green, gray, smells bad, or causes itching, tell a parent or doctor.",
          "Sweating more during sports or hot weather is normal. Keep spare deodorant in your locker or bag. Wearing breathable fabrics like cotton helps reduce sweat. Remember: everybody sweats. It is how your body cools itself down."]),
        ("Emotions Rollercoaster",
         ["During puberty, hormones do not just change your body. They also affect your brain and emotions. You might feel happy one minute and want to cry the next. You might get angry at things that never bothered you before. You might feel overwhelmed, sensitive, or moody. This is all normal.",
          "Your brain is literally rewiring itself during puberty. The emotional part of your brain is developing faster than the rational part, which is why feelings can feel so HUGE and intense right now. This is not a flaw in your design. It is a feature of growing up.",
          "What helps with emotional ups and downs: getting enough sleep (seriously, this is huge), regular exercise, talking to someone you trust, writing in a journal, creative expression (art, music, dance), and being patient with yourself. You are not crazy. You are growing.",
          "It is okay to cry. It is okay to need alone time. It is okay to not know why you feel a certain way. It is okay to ask for help. Your feelings are VALID even when they do not make logical sense. Feelings do not need to be logical to be real.",
          "If you feel persistently sad, anxious, or hopeless for more than two weeks, please tell a trusted adult. Depression and anxiety can start during puberty and are treatable medical conditions, not weaknesses. Getting help is brave."]),
        ("Crushes and Feelings",
         ["During puberty, you might start feeling attracted to other people in new ways. You might develop crushes on classmates, celebrities, or even teachers. These feelings are a normal part of growing up. Some girls develop crushes early, some later, and some not for a long time. All timelines are normal.",
          "Crushes can feel overwhelming. Your heart races, you cannot stop thinking about them, you might feel nervous or giddy around them. These physical reactions are caused by chemicals in your brain, especially dopamine (the feel-good chemical). It is literally like a temporary brain storm.",
          "Having crushes does not mean you need to act on them right now. There is no rush to date, kiss, or have a boyfriend or girlfriend. You are allowed to just FEEL things without taking action. Enjoying the butterflies without pressure is perfectly fine.",
          "Some girls develop crushes on boys, some on girls, and some on both. All of these feelings are normal and valid. Your attractions might change over time as you learn more about yourself. There is no timeline for figuring this out.",
          "The most important thing about crushes and romantic feelings: you never owe anyone anything. No one has the right to pressure you. Your boundaries around your body and your feelings are always valid. Healthy relationships (even crushes) feel safe and respectful."]),
        ("Body Image",
         ["Your body is changing into shapes you might not be used to. Hips widening, breasts growing, fat redistributing. Media shows you one 'ideal' body type, but the truth is that healthy bodies come in endless varieties. Your value has nothing to do with your shape or size.",
          "The images you see in magazines, Instagram, and TV are not reality. They are filtered, edited, posed, and often surgically enhanced. Comparing your real, living, beautiful body to manufactured images will always make you feel inadequate because you are comparing reality to fantasy.",
          "Instead of focusing on how your body LOOKS, try focusing on what it CAN DO. Can it run? Dance? Hug? Create? Think? Your body is a miracle of engineering that keeps you alive and allows you to experience the world. That is what matters most.",
          "If you find yourself constantly criticizing your body, try talking to yourself the way you would talk to your best friend. Would you tell her she is ugly or fat? Of course not. Give yourself the same kindness and compassion you so easily give others.",
          "Body image struggles are incredibly common during puberty. You are not alone. But if negative thoughts about your body are taking over your life, preventing you from eating normally, or making you very sad, please talk to a trusted adult. Help is available."]),
        ("Nutrition for Growing Girls",
         ["Your body is growing rapidly during puberty and needs quality fuel. This is not about dieting or restriction. It is about giving your body what it needs to grow strong, develop properly, and have energy for all the amazing things you want to do.",
          "Key nutrients during puberty: calcium for growing bones (dairy, leafy greens, fortified foods), iron especially once periods start (red meat, spinach, beans), protein for growing muscles (chicken, fish, beans, nuts), and healthy fats for brain development (avocado, nuts, olive oil).",
          "Eating regularly is important. Skipping meals slows your metabolism and deprives your growing body of needed fuel. Aim for three meals and two snacks daily. Eat when you are hungry and stop when you are full. Your body knows what it needs.",
          "Dieting during puberty can be harmful because your body needs calories to grow and develop properly. If someone suggests you need to lose weight, talk to your doctor first. Growing bodies need MORE nutrition, not less. Health is about nourishment, not restriction.",
          "Water is essential during puberty. Aim for 6-8 glasses daily, more when active. Dehydration can worsen headaches, fatigue, and skin problems. Keep a water bottle with you and sip throughout the day. Your body and skin will thank you."]),
        ("Sleep for Teens",
         ["During puberty, your body's internal clock shifts later. You naturally want to stay up later and sleep in later. This is biology, not laziness! Your brain releases the sleep hormone melatonin later at night during puberty. Unfortunately, school start times do not adjust to match.",
          "You need 9-11 hours of sleep during puberty. Your body does its most important growing and repairing during sleep. Growth hormone is released primarily during deep sleep. Not getting enough sleep can affect your mood, grades, skin, weight, and immune system.",
          "Tips for better sleep: keep a consistent bedtime (even on weekends), stop screens 30-60 minutes before bed (blue light blocks melatonin), keep your room cool and dark, avoid caffeine after noon, and create a relaxing bedtime routine.",
          "If you cannot fall asleep: try deep breathing, progressive muscle relaxation, or listening to calm music. Write worries in a journal before bed to get them out of your head. Avoid looking at the clock because it increases anxiety about not sleeping.",
          "Sleep is not negotiable for a developing brain and body. Think of it as recharging your phone. If you only charge to 50 percent, you will not make it through the day. Give your body the full charge it needs."]),
        ("Talking to Adults About It",
         ["It can feel awkward to talk to parents or other adults about puberty, periods, or body changes. But having a trusted adult you can ask questions is important. They went through the same things and can help you navigate this time with less confusion and anxiety.",
          "If talking to a parent feels too awkward, consider: an older sister, aunt, grandmother, school nurse, coach, or family friend. It helps to start with 'I have a question about something I read' or 'Can I ask you about something private?' These openings make the conversation easier.",
          "Adults want to help you but might not know you need them unless you ask. They might be waiting for you to bring it up because they do not want to embarrass you. Someone has to go first, and it is okay if that person is you.",
          "You deserve accurate information about your body. If an adult cannot answer your question or seems uncomfortable, it is okay to ask a different adult or look for age-appropriate books and websites. Knowledge about your own body is your right.",
          "Remember: there is no question too embarrassing or too small. Every woman alive has gone through puberty. They understand. And helping you through it is one of the most important things an adult can do."])
    ]
    
    # Title page
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(640, "GROWING UP GIRL", 'F2', 30, 0.1)
    doc.add_line(150, 620, 462, 620, 2, 0.3)
    doc.add_centered_text(585, "The Honest Guide to Puberty, Periods", 'F4', 15, 0.3)
    doc.add_centered_text(562, "& Your Changing Body (Ages 9-14)", 'F4', 15, 0.3)
    doc.add_centered_text(510, "Like a cool older sister explaining things", 'F4', 12, 0.5)
    doc.add_centered_text(100, author, 'F2', 14, 0.2)
    doc.new_page()
    
    # Copyright
    doc.add_centered_text(700, "GROWING UP GIRL", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Author: {author}", 'F1', 11, 0.3)
    doc.add_text(72, 630, "Format: 8.5 x 11 inches | Kindle & Paperback", 'F1', 10, 0.4)
    doc.add_text(72, 600, "All rights reserved.", 'F1', 10, 0.4)
    doc.new_page()
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0.1)
    doc.add_line(72, 705, 540, 705, 1, 0.3)
    y = 680
    for i, (title, _) in enumerate(chapters):
        doc.add_text(72, y, f"Chapter {i+1}: {title}", 'F1', 11, 0.2)
        y -= 22
    doc.new_page()
    
    # Chapters - 5 pages each
    for i, (title, paragraphs) in enumerate(chapters):
        # Page 1-2: Main content
        doc.add_filled_rect(50, 710, 512, 50, 0.92)
        doc.add_centered_text(740, f"Chapter {i+1}", 'F1', 10, 0.5)
        doc.add_centered_text(720, title.upper(), 'F2', 16, 0.1)
        
        y = 680
        for para in paragraphs:
            words = para.split()
            lines = []
            current = ""
            for word in words:
                if len(current + " " + word) > 80:
                    lines.append(current)
                    current = word
                else:
                    current = current + " " + word if current else word
            if current:
                lines.append(current)
            
            for line in lines:
                if y < 80:
                    doc.new_page()
                    doc.add_centered_text(750, f"{title} (continued)", 'F2', 12, 0.3)
                    y = 720
                doc.add_text(72, y, line, 'F4', 11, 0.2)
                y -= 15
            y -= 12
        
        doc.new_page()
        
        # Page 3: FAQ
        doc.add_centered_text(740, f"{title} - FAQ", 'F2', 14, 0.2)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        
        doc.add_text(72, 700, "FREQUENTLY ASKED QUESTIONS:", 'F2', 12, 0.2)
        faqs = [
            ("Is this normal?", "Yes! Almost certainly. Every girl goes through puberty differently, and there is a wide range of normal. If you are ever truly concerned, ask your doctor."),
            ("When will it happen to me?", "Your body has its own timeline. Comparing yourself to friends is not helpful because everyone develops at their own pace. Trust your body."),
            ("What if mine is different from my friends?", "Bodies are wonderfully diverse. Different is not wrong. Different is just different. Celebrate what makes your body unique.")
        ]
        y = 675
        for q, a in faqs:
            doc.add_text(72, y, f"Q: {q}", 'F2', 11, 0.2)
            y -= 16
            words = a.split()
            lines = []
            current = "A: "
            for word in words:
                if len(current + " " + word) > 75:
                    lines.append(current)
                    current = "   " + word
                else:
                    current = current + " " + word
            if current:
                lines.append(current)
            for line in lines:
                doc.add_text(82, y, line, 'F4', 10, 0.3)
                y -= 14
            y -= 15
        
        # Myth Busters
        y -= 10
        doc.add_text(72, y, "MYTH BUSTERS:", 'F2', 12, 0.2)
        y -= 18
        myths = [
            "MYTH: Everyone develops at the same age. TRUTH: Normal range is huge!",
            "MYTH: You should not exercise during your period. TRUTH: Exercise helps!",
            "MYTH: Puberty changes mean something is wrong. TRUTH: It is healthy!"
        ]
        for myth in myths:
            doc.add_text(82, y, myth, 'F1', 10, 0.3)
            y -= 18
        
        # Body positivity affirmation
        y -= 20
        doc.add_filled_rect(72, y - 10, 468, 35, 0.93)
        doc.add_centered_text(y + 8, "BODY POSITIVITY AFFIRMATION:", 'F2', 10, 0.3)
        doc.add_centered_text(y - 8, "My body is changing and growing, and I love it through every stage.", 'F5', 11, 0.2)
        
        doc.new_page()
        
        # Page 4-5: Journal/Notes
        doc.add_centered_text(740, f"{title} - My Notes", 'F2', 14, 0.2)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        doc.add_text(72, 700, "Write your questions, thoughts, or feelings about this chapter:", 'F4', 11, 0.3)
        y = 675
        for j in range(20):
            doc.add_line(72, y, 540, y, 0.5, 0.75)
            y -= 25
        doc.new_page()
    
    # Final page
    doc.add_centered_text(600, "YOU ARE AMAZING", 'F2', 24, 0.1)
    doc.add_centered_text(560, "Your body is doing incredible things.", 'F4', 14, 0.3)
    doc.add_centered_text(530, "Be patient with it. Be kind to it.", 'F4', 14, 0.3)
    doc.add_centered_text(500, "It is the only one you will ever have,", 'F4', 14, 0.3)
    doc.add_centered_text(470, "and it is wonderfully, perfectly YOURS.", 'F4', 14, 0.3)
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
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book350_Girls_Puberty_Guide.pdf')
    print("Book350_Girls_Puberty_Guide.pdf created successfully!")

if __name__ == "__main__":
    create_book()
