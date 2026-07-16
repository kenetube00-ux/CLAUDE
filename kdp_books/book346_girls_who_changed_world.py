"""Book346: Girls Who Changed The World - 25 True Stories of Amazing Women"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc()
    author = "Daniel Tesfamariam"
    
    women = [
        ("Malala Yousafzai", "Education Activist", 11, "Pakistan",
         "Malala Yousafzai grew up in the Swat Valley of Pakistan where the Taliban had banned girls from attending school. Even as a young girl, Malala knew that education was her right. At just eleven years old, she began writing a blog for the BBC about life under Taliban rule and her desire to go to school. Her courage made her a target, and in 2012, a gunman shot her on her school bus. Miraculously, she survived and became even more determined to fight for girls' education worldwide.",
         "Became the youngest Nobel Peace Prize laureate at age 17. Founded the Malala Fund which has invested millions in education programs. Her advocacy has helped millions of girls access education globally.",
         "One child, one teacher, one book, one pen can change the world."),
        ("Greta Thunberg", "Climate Activist", 15, "Sweden",
         "Greta Thunberg was just fifteen when she decided to skip school on Fridays to protest outside the Swedish parliament about climate change. She sat alone with a hand-painted sign that read 'School Strike for Climate.' Many people thought she was too young to make a difference, but Greta knew that her generation's future was at stake. Her solitary protest sparked a global movement.",
         "Inspired millions of young people worldwide to join Fridays for Future. Addressed world leaders at the United Nations. Named Time Person of the Year 2019. Changed global conversations about climate urgency.",
         "You are never too small to make a difference."),
        ("Ruby Bridges", "Civil Rights Pioneer", 6, "USA",
         "In 1960, six-year-old Ruby Bridges walked into William Frantz Elementary School in New Orleans, becoming the first African American child to integrate an all-white school in the South. Federal marshals escorted her past screaming protesters. Inside, she sat alone in a classroom because white parents had pulled their children out. Ruby showed up every single day with remarkable courage.",
         "Her bravery helped pave the way for school desegregation across America. She later became a civil rights activist and author, inspiring generations to stand against racism.",
         "Don't follow the path. Go where there is no path and begin the trail."),
        ("Anne Frank", "Diarist & Writer", 13, "Netherlands",
         "Anne Frank received a diary for her thirteenth birthday in 1942, just weeks before her Jewish family went into hiding from the Nazis in a secret annex in Amsterdam. For two years, Anne wrote about her fears, dreams, and observations about human nature. Despite living in terror, her writing showed remarkable wisdom, humor, and hope for humanity.",
         "Her diary, published after the war, has been translated into over 70 languages and has sold more than 30 million copies. It remains one of the most powerful testimonies of the Holocaust.",
         "How wonderful it is that nobody need wait a single moment before starting to improve the world."),
        ("Marie Curie", "Scientist", 10, "Poland",
         "Marie Curie showed extraordinary intellectual curiosity from age ten, excelling in every subject despite facing discrimination as a woman in science. Born in Poland, she moved to Paris to study because Polish universities did not admit women. She worked tirelessly in a cold, leaky laboratory, often forgetting to eat as she pursued her research on radioactivity.",
         "First woman to win a Nobel Prize. First person to win Nobel Prizes in two different sciences (Physics and Chemistry). Discovered two elements: polonium and radium. Pioneered research on radioactivity.",
         "Nothing in life is to be feared, it is only to be understood."),
        ("Jane Goodall", "Primatologist", 10, "England",
         "Jane Goodall dreamed of living with animals in Africa from the time she was ten years old. Without a college degree, she traveled to Tanzania at age 26 to study chimpanzees. Scientists told her she was doing research wrong, but Jane trusted her own observations. She gave the chimps names instead of numbers and discovered that they used tools.",
         "Revolutionized our understanding of primates. Proved that chimpanzees make and use tools. Founded the Jane Goodall Institute. Became one of the world's most important conservationists.",
         "What you do makes a difference, and you have to decide what kind of difference you want to make."),
        ("Harriet Tubman", "Freedom Fighter", 12, "USA",
         "Harriet Tubman was born into slavery and endured terrible cruelty from a very young age. At twelve, she was hit in the head by an iron weight thrown by an overseer, causing lifelong seizures and headaches. Despite this, she escaped slavery and then made thirteen dangerous trips back to the South on the Underground Railroad to free others.",
         "Led approximately 70 enslaved people to freedom. Served as a spy and scout for the Union Army during the Civil War. Never lost a single passenger on the Underground Railroad.",
         "Every great dream begins with a dreamer. Always remember, you have the strength and patience to reach for the stars."),
        ("Frida Kahlo", "Artist", 6, "Mexico",
         "Frida Kahlo contracted polio at age six, which left one leg shorter than the other. At eighteen, a terrible bus accident broke her spine, collarbone, ribs, and pelvis. During her long recovery, she began painting self-portraits. Frida turned her pain into powerful art that expressed her Mexican heritage, her physical suffering, and her fierce independence.",
         "Created 143 paintings, 55 of which are self-portraits. Became one of the most recognized artists of the 20th century. Her work celebrates Mexican culture and challenges beauty standards.",
         "Feet, what do I need you for when I have wings to fly?"),
        ("Amelia Earhart", "Aviator", 10, "USA",
         "Amelia Earhart saw her first airplane at age ten and was unimpressed. But when she took her first airplane ride at twenty-three, everything changed. She saved money from odd jobs to pay for flying lessons and bought her first plane, a bright yellow biplane she named 'The Canary.' People told her flying was not for women. She flew anyway.",
         "First woman to fly solo across the Atlantic Ocean. Set multiple speed and distance records. Inspired generations of female pilots and adventurers.",
         "The most effective way to do it is to do it."),
        ("Rosa Parks", "Civil Rights Activist", 11, "USA",
         "Rosa Parks grew up in Alabama during a time of extreme racial segregation. From age eleven, she attended a school for African American girls where she learned about dignity and self-respect. On December 1, 1955, Rosa refused to give up her bus seat to a white passenger in Montgomery, Alabama. Her quiet act of defiance changed American history.",
         "Her arrest sparked the Montgomery Bus Boycott, which lasted 381 days. This led to a Supreme Court ruling that bus segregation was unconstitutional. She is known as the Mother of the Civil Rights Movement.",
         "Each person must live their life as a model for others."),
        ("Serena Williams", "Tennis Champion", 4, "USA",
         "Serena Williams started playing tennis at age four on cracked public courts in Compton, California, trained by her father who had no tennis background. People doubted that a Black girl from a tough neighborhood could succeed in a sport dominated by wealthy white players. Serena proved them all wrong with her powerful serve and fierce determination.",
         "Won 23 Grand Slam singles titles. Held the number one ranking for 319 weeks. Won four Olympic gold medals. Changed the face of tennis forever.",
         "I really think a champion is defined not by their wins but by how they can recover when they fall."),
        ("Emma Watson", "Actress & Activist", 9, "England",
         "Emma Watson was cast as Hermione Granger in Harry Potter at age nine, becoming one of the most famous child actresses in the world. But instead of just enjoying fame, Emma used her platform for good. She studied at Brown University and became a UN Women Goodwill Ambassador, launching the HeForShe campaign for gender equality.",
         "Launched HeForShe campaign reaching millions. Advocates for sustainable fashion. Uses her fame to promote education and gender equality worldwide.",
         "If not me, who? If not now, when?"),
        ("Temple Grandin", "Animal Scientist", 4, "USA",
         "Temple Grandin was diagnosed with autism at age four, and doctors told her mother she would never speak. Temple saw the world differently from other children, thinking in pictures rather than words. She was bullied and struggled socially, but her unique way of thinking gave her an extraordinary ability to understand how animals feel and think.",
         "Revolutionized the livestock industry with humane animal handling systems. Became a professor of animal science. Her work proved that autism can be a superpower, not just a limitation.",
         "The world needs all types of minds."),
        ("Wangari Maathai", "Environmentalist", 8, "Kenya",
         "Wangari Maathai grew up in rural Kenya surrounded by lush forests and clean rivers. As she grew older, she watched forests being cut down and rivers drying up. She decided to fight back by planting trees. People laughed at her simple solution, but Wangari knew that trees meant life for her community. She organized women across Kenya to plant trees together.",
         "Founded the Green Belt Movement which planted over 51 million trees. First African woman to receive the Nobel Peace Prize. Proved that environmental action and women's empowerment go hand in hand.",
         "It is the little things citizens do. That is what will make the difference."),
        ("Maya Angelou", "Writer & Poet", 8, "USA",
         "Maya Angelou stopped speaking for five years after experiencing trauma at age eight. During her silence, she read voraciously and fell in love with language. When she finally found her voice again, it was powerful beyond measure. She became one of America's greatest writers, using her words to heal, inspire, and demand justice.",
         "Wrote seven autobiographies and numerous poetry collections. Recited her poem at a presidential inauguration. Received the Presidential Medal of Freedom.",
         "There is no greater agony than bearing an untold story inside you."),
        ("Mother Teresa", "Humanitarian", 12, "Albania",
         "Agnes Gonxha Bojaxhiu felt called to help the poor from age twelve. She left her family in Albania at eighteen to become a nun in India. In the slums of Calcutta, she saw suffering that most people looked away from. Instead of looking away, she reached out her hands and served the poorest of the poor for decades.",
         "Founded the Missionaries of Charity which operates in over 130 countries. Received the Nobel Peace Prize. Served millions of poor, sick, and dying people.",
         "If you cannot feed a hundred people, then feed just one."),
        ("Florence Nightingale", "Nursing Pioneer", 12, "England",
         "Florence Nightingale knew from age twelve that she wanted to help sick people, but her wealthy family was horrified. Nursing was considered dirty work unsuitable for a lady. Florence studied in secret and eventually traveled to the Crimean War where she found soldiers dying in filthy hospitals. She transformed nursing from a disrespected trade into a noble profession.",
         "Reduced the death rate in military hospitals from 42% to 2%. Founded the first professional nursing school. Her methods of statistical analysis changed healthcare forever.",
         "I attribute my success to this: I never gave or took any excuse."),
        ("Cleopatra", "Queen of Egypt", 14, "Egypt",
         "Cleopatra became co-ruler of Egypt at just fourteen years old in a world where women rarely held power. She was not just beautiful as legends suggest; she was brilliant. She spoke nine languages, was educated in mathematics and philosophy, and used her intelligence to lead one of the ancient world's greatest civilizations.",
         "Ruled Egypt for nearly two decades. Spoke nine languages fluently. Was one of the most powerful women in ancient history. Built alliances that protected her nation.",
         "I will not be triumphed over."),
        ("Joan of Arc", "Military Leader", 13, "France",
         "Joan of Arc was a peasant girl in medieval France who began hearing voices at age thirteen telling her to help save France from English occupation. At seventeen, she convinced the French king to give her an army. Wearing armor and riding into battle, this teenage girl led French troops to victory and changed the course of European history.",
         "Led the French army to several important victories during the Hundred Years War. Helped Charles VII become King of France. Became a symbol of French unity and courage.",
         "I am not afraid. I was born to do this."),
        ("Simone Biles", "Gymnast", 6, "USA",
         "Simone Biles entered foster care as a young child and was adopted by her grandparents at age six. She discovered gymnastics on a field trip and immediately showed extraordinary talent. Despite growing up in difficult circumstances, Simone's dedication and fearlessness made her the greatest gymnast in history. She also showed incredible bravery by prioritizing her mental health.",
         "Most decorated gymnast in history with 32 Olympic and World Championship medals. Has four gymnastics moves named after her. Advocated for athletes' mental health.",
         "I am not the next Usain Bolt or Michael Phelps. I am the first Simone Biles."),
        ("Misty Copeland", "Ballerina", 13, "USA",
         "Misty Copeland did not start ballet until age thirteen, which most people said was far too late. She lived in a motel with her mother and five siblings. Dance experts said her body was wrong for ballet, that she was too muscular, too short, and too curvy. Misty refused to change herself to fit ballet; instead, she changed ballet to include her.",
         "First African American woman to be named principal dancer at American Ballet Theatre. Broke barriers in a traditionally exclusive art form. Inspired countless young girls of color to pursue ballet.",
         "Anything is possible when you work hard and never give up."),
        ("Ada Lovelace", "Computer Pioneer", 12, "England",
         "Ada Lovelace lived in the 1800s when women were expected to do needlework, not mathematics. But Ada was fascinated by machines and numbers from age twelve. When she met inventor Charles Babbage and saw his mechanical computing machine, she immediately understood its potential. She wrote what is considered the first computer program ever created.",
         "Wrote the first computer algorithm. Envisioned that computers could do more than just calculate numbers. Is considered the first computer programmer in history.",
         "That brain of mine is something more than merely mortal."),
        ("Oprah Winfrey", "Media Mogul", 6, "USA",
         "Oprah Winfrey was born into poverty in rural Mississippi and faced abuse and hardship as a child. At age six, she was already reading and showed a gift for public speaking. Despite every obstacle, she worked her way from a local radio job to building one of the most successful media empires in history. She turned her pain into purpose.",
         "Built a billion-dollar media empire. Her book club influenced millions of readers. First African American female billionaire. Inspired millions through her authentic storytelling.",
         "Turn your wounds into wisdom."),
        ("Malala Fund Work", "Global Education", 17, "Worldwide",
         "After surviving the Taliban attack, Malala did not retreat into safety. Instead, she amplified her mission. She founded the Malala Fund, spoke at the United Nations, and wrote her memoir 'I Am Malala.' She graduated from Oxford University and continues to travel the world advocating for every girl's right to twelve years of free education.",
         "The Malala Fund works in eight countries. Has invested in education advocates worldwide. Continues to be the world's leading voice for girls' education.",
         "We realize the importance of our voices only when we are silenced."),
        ("Michelle Obama", "Former First Lady", 10, "USA",
         "Michelle Obama grew up on the South Side of Chicago in a small apartment. From age ten, she was determined to prove she belonged in every room she entered. Teachers told her she was not Princeton material, but she applied anyway and graduated with honors. As First Lady, she used her platform to champion education, healthy living, and girls' empowerment worldwide.",
         "Launched Let Girls Learn initiative reaching millions globally. Started the Reach Higher initiative for college access. Her memoir 'Becoming' sold over 17 million copies.",
         "There is no limit to what we, as women, can accomplish.")
    ]
    
    # Title page
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(620, "GIRLS WHO CHANGED", 'F2', 30, 0.1)
    doc.add_centered_text(580, "THE WORLD", 'F2', 30, 0.1)
    doc.add_centered_text(530, "25 True Stories of Amazing Women", 'F4', 18, 0.3)
    doc.add_centered_text(500, "Who Started Young (Ages 8-14)", 'F4', 18, 0.3)
    doc.add_line(150, 480, 462, 480, 2, 0.3)
    doc.add_centered_text(440, "Stories of Courage, Determination & Change", 'F4', 14, 0.4)
    doc.add_centered_text(100, author, 'F2', 14, 0.2)
    doc.add_centered_text(70, "For every girl who dares to dream big", 'F4', 12, 0.5)
    doc.new_page()
    
    # Copyright page
    doc.add_centered_text(700, "GIRLS WHO CHANGED THE WORLD", 'F2', 14, 0.2)
    doc.add_centered_text(670, "25 True Stories of Amazing Women Who Started Young", 'F1', 11, 0.3)
    doc.add_text(72, 620, f"Author: {author}", 'F1', 11, 0.3)
    doc.add_text(72, 600, "Format: 8.5 x 11 inches (612 x 792 points)", 'F1', 10, 0.4)
    doc.add_text(72, 580, "Available as Kindle eBook and Amazon Paperback", 'F1', 10, 0.4)
    doc.add_text(72, 550, "All rights reserved. No part of this publication may be", 'F1', 10, 0.4)
    doc.add_text(72, 535, "reproduced without written permission from the publisher.", 'F1', 10, 0.4)
    doc.new_page()
    
    # Table of Contents
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0.1)
    doc.add_line(72, 705, 540, 705, 1, 0.3)
    y = 680
    for i, (name, field, age, country, _, _, _) in enumerate(women):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "TABLE OF CONTENTS (continued)", 'F2', 14, 0.2)
            y = 690
        doc.add_text(72, y, f"{i+1}. {name}", 'F2', 11, 0.2)
        doc.add_text(350, y, f"{field} - Started at age {age}", 'F1', 10, 0.4)
        y -= 22
    doc.new_page()
    
    # Introduction
    doc.add_centered_text(720, "INTRODUCTION", 'F2', 20, 0.1)
    doc.add_line(200, 705, 412, 705, 1, 0.3)
    intro_text = [
        "Dear Reader,",
        "",
        "You hold in your hands the stories of twenty-five extraordinary women who",
        "changed the world. But here is a secret: when they started, they were just",
        "girls. Girls like you. Girls who had big dreams, faced big obstacles, and",
        "made big choices that transformed not just their own lives, but the lives",
        "of millions around the world.",
        "",
        "Some of these women were told they were too young, too poor, too different,",
        "or simply 'just a girl.' They heard 'no' more times than they could count.",
        "But they kept going. They let their dreams be bigger than their doubts.",
        "",
        "As you read each story, ask yourself: What do I have in common with her?",
        "What obstacles am I facing that she faced too? What can I learn from her",
        "courage? Because here is the truth: the next girl who changes the world",
        "might be you.",
        "",
        "These stories are your stories too. They belong to every girl who has ever",
        "been told she cannot do something, every girl who has felt different, every",
        "girl who knows in her heart that she is meant for something great.",
        "",
        "Are you ready to be inspired? Let's begin.",
        "",
        "With love and belief in you,",
        f"{author}"
    ]
    y = 670
    for line in intro_text:
        if line == "":
            y -= 12
        else:
            doc.add_text(72, y, line, 'F4', 12, 0.2)
            y -= 18
    doc.new_page()
    
    # Each woman gets 3 pages
    for i, (name, field, age, country, story, accomplishments, quote) in enumerate(women):
        # Page 1: Her Story
        doc.add_filled_rect(50, 700, 512, 60, 0.92)
        doc.add_centered_text(740, f"Chapter {i+1}", 'F1', 11, 0.5)
        doc.add_centered_text(718, name.upper(), 'F2', 22, 0.1)
        doc.add_centered_text(695, f"{field} | Started at age {age} | {country}", 'F4', 12, 0.4)
        
        doc.add_text(72, 660, "HER STORY", 'F2', 14, 0.2)
        doc.add_line(72, 650, 200, 650, 1, 0.3)
        
        # Wrap story text
        words = story.split()
        lines = []
        current = ""
        for word in words:
            if len(current + " " + word) > 75:
                lines.append(current)
                current = word
            else:
                current = current + " " + word if current else word
        if current:
            lines.append(current)
        
        y = 630
        for line in lines:
            doc.add_text(72, y, line, 'F4', 11, 0.2)
            y -= 16
        
        # What She Accomplished
        y -= 15
        doc.add_text(72, y, "WHAT SHE ACCOMPLISHED", 'F2', 13, 0.2)
        y -= 5
        doc.add_line(72, y, 250, y, 1, 0.3)
        y -= 20
        
        acc_words = accomplishments.split()
        acc_lines = []
        current = ""
        for word in acc_words:
            if len(current + " " + word) > 75:
                acc_lines.append(current)
                current = word
            else:
                current = current + " " + word if current else word
        if current:
            acc_lines.append(current)
        
        for line in acc_lines:
            doc.add_text(72, y, line, 'F1', 11, 0.3)
            y -= 16
        
        # Age she started
        y -= 15
        doc.add_filled_rect(72, y - 5, 468, 25, 0.93)
        doc.add_text(82, y, f"She started making a difference at age {age}. You can start today!", 'F2', 11, 0.2)
        
        doc.new_page()
        
        # Page 2: Lessons & Discussion
        doc.add_centered_text(740, f"{name} - Lessons & Reflection", 'F2', 16, 0.1)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        
        doc.add_text(72, 695, "OBSTACLES SHE OVERCAME", 'F2', 13, 0.2)
        obstacles_text = [
            f"{name} faced incredible challenges on her journey. She was told she could not",
            f"succeed because of her gender, her age, her background, or her circumstances.",
            f"In {country}, she faced barriers that would have stopped most people. But she",
            "refused to let others define her limits. She turned every obstacle into",
            "fuel for her determination and every 'no' into motivation to try harder."
        ]
        y = 670
        for line in obstacles_text:
            doc.add_text(72, y, line, 'F4', 11, 0.2)
            y -= 16
        
        y -= 20
        doc.add_text(72, y, "WHAT I CAN LEARN FROM HER", 'F2', 13, 0.2)
        y -= 20
        lessons = [
            "1. Courage means being afraid but doing it anyway",
            "2. Your age does not limit your ability to make a difference",
            "3. Obstacles are opportunities in disguise",
            "4. One person really can change the world",
            "5. Your unique perspective is your greatest strength"
        ]
        for lesson in lessons:
            doc.add_text(82, y, lesson, 'F1', 11, 0.2)
            y -= 18
        
        y -= 20
        doc.add_text(72, y, "DISCUSSION QUESTIONS", 'F2', 13, 0.2)
        y -= 20
        questions = [
            f"1. What quality of {name}'s do you admire most? Why?",
            f"2. How would you have handled the obstacles she faced?",
            "3. What issue in your community could you take action on today?",
            "4. Who in your life reminds you of this woman? Why?"
        ]
        for q in questions:
            doc.add_text(82, y, q, 'F1', 11, 0.3)
            y -= 20
        
        y -= 20
        doc.add_filled_rect(72, y - 10, 468, 40, 0.92)
        doc.add_centered_text(y + 10, f'"{quote}"', 'F5', 12, 0.2)
        doc.add_centered_text(y - 5, f"- {name}", 'F4', 10, 0.4)
        
        doc.new_page()
        
        # Page 3: Activity & Journal
        doc.add_centered_text(740, f"{name} - Your Turn!", 'F2', 16, 0.1)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        
        doc.add_text(72, 695, "MY REFLECTION", 'F2', 13, 0.2)
        doc.add_text(72, 670, "After reading this story, write your thoughts below:", 'F4', 11, 0.3)
        y = 650
        for j in range(6):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 25
        
        y -= 15
        doc.add_text(72, y, "IF I COULD TALK TO HER, I WOULD SAY:", 'F2', 12, 0.2)
        y -= 20
        for j in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 25
        
        y -= 15
        doc.add_text(72, y, "MY ACTION PLAN", 'F2', 12, 0.2)
        y -= 5
        doc.add_text(72, y, "Inspired by this story, one thing I will do this week:", 'F4', 11, 0.3)
        y -= 20
        for j in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 25
        
        y -= 15
        doc.add_rect(72, y - 50, 468, 55, 1, 0.3)
        doc.add_centered_text(y - 10, "Remember: She was once a girl just like you.", 'F5', 13, 0.2)
        doc.add_centered_text(y - 30, "Your story is still being written. Make it amazing!", 'F4', 11, 0.3)
        
        doc.new_page()
    
    # Final pages - Conclusion
    doc.add_centered_text(700, "YOU CAN CHANGE THE WORLD TOO", 'F2', 20, 0.1)
    doc.add_line(150, 685, 462, 685, 2, 0.3)
    conclusion = [
        "You have now read the stories of twenty-five incredible women who changed",
        "the world. Each one started as a girl with a dream. Each one faced people",
        "who said it could not be done. And each one proved them wrong.",
        "",
        "Now it is your turn. What will YOUR story be?",
        "",
        "Maybe you will cure a disease, fight for justice, create beautiful art,",
        "or invent something the world has never seen. Maybe you will be the person",
        "who changes everything for your community, your country, or the world.",
        "",
        "Remember these lessons from the women you have met in this book:",
        "",
        "  - You are never too young to start",
        "  - Your voice matters",
        "  - Obstacles make you stronger",
        "  - Being different is your superpower",
        "  - One person CAN change the world",
        "  - That person can be YOU",
        "",
        "Dream big, work hard, be kind, and never give up.",
        "",
        "The world is waiting for YOUR story."
    ]
    y = 655
    for line in conclusion:
        if line == "":
            y -= 12
        else:
            doc.add_text(72, y, line, 'F4', 12, 0.2)
            y -= 18
    doc.new_page()
    
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book346_Girls_Who_Changed_World.pdf')
    print("Book346_Girls_Who_Changed_World.pdf created successfully!")

if __name__ == "__main__":
    create_book()
