from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    careers = {
        "Science & Tech": [
            ("Software Engineer","Write code that powers apps, websites, and games","Bachelor's degree (4 years)","$80K-$200K+","Problem-solving, logic, coding, teamwork","Alex starts each morning reviewing code. Then she joins a team meeting to plan new features for their app used by 10 million people. She spends the afternoon coding, testing, and debugging. It's like solving puzzles all day!","Do you enjoy logic puzzles and building things?"),
            ("Video Game Developer","Create the games millions of people play daily","Bachelor's degree or self-taught","$60K-$150K+","Coding, creativity, art, storytelling","Jamal's team is creating a new adventure game. He codes character movements, designs game physics, and tests levels. He gets to play games as 'research' and his ideas become virtual worlds!","Do you love games AND want to know how they're made?"),
            ("Data Scientist","Find patterns and insights in massive amounts of data","Master's degree typical","$90K-$170K+","Math, statistics, coding, curiosity","Maya analyzes data from millions of users to find patterns. Today she discovered that people who exercise more also read more. Companies use her insights to make better decisions.","Do you like math, patterns, and solving mysteries?"),
            ("Cybersecurity Expert","Protect computers and networks from hackers","Bachelor's + certifications","$80K-$160K+","Problem-solving, attention to detail","River is a digital guardian. Today he found a vulnerability in the company's system before hackers could exploit it. He feels like a superhero protecting millions of people's data!","Do you like finding weaknesses and solving security puzzles?"),
            ("Robotics Engineer","Design and build robots for various purposes","Bachelor's/Master's in engineering","$75K-$150K+","Engineering, coding, creativity, mechanics","Priya just programmed a robot arm to perform surgery more precisely than human hands. She combines mechanical design, electronics, and code to create machines that help people.","Do you enjoy building things and making them move?"),
            ("AI Researcher","Teach computers to learn and think","PhD often required","$100K-$250K+","Math, coding, research, patience","Dr. Chen is training an AI to detect diseases from X-rays. Today his system correctly identified a condition that doctors missed. AI research is literally saving lives!","Do you wonder how brains work and want to recreate that in machines?"),
            ("Space Scientist","Study planets, stars, and the universe","PhD in astrophysics/astronomy","$70K-$130K+","Physics, math, observation, patience","Tonight, Dr. Amara points a telescope at a newly discovered exoplanet. She analyzes its atmosphere for signs of water. Could there be life there? That question drives her every day.","Do you stare at stars and wonder what's out there?"),
            ("Biomedical Engineer","Create medical devices that save lives","Bachelor's/Master's degree","$70K-$140K+","Biology, engineering, problem-solving","Oscar designed a prosthetic hand that responds to muscle signals. When he saw a child use it to pick up a ball for the first time, it was the greatest moment of his career.","Do you want to combine engineering and helping people?"),
            ("Environmental Scientist","Study and protect the environment","Bachelor's/Master's degree","$60K-$110K+","Biology, chemistry, fieldwork, data","Sage collects water samples from rivers, analyzes pollution levels, and advises companies on reducing their environmental impact. Her work keeps ecosystems healthy for future generations.","Do you care deeply about nature and want to protect it?"),
            ("UX Designer","Design how people interact with technology","Bachelor's degree or bootcamp","$70K-$150K+","Empathy, creativity, psychology, design","Kai observes how real people use an app, then redesigns confusing parts. Good UX design means technology works so naturally you don't even notice the design - it just WORKS.","Do you notice when apps are frustrating? Want to fix that?"),
        ],
        "Health & Medicine": [
            ("Doctor (Physician)","Diagnose and treat illnesses, save lives","Medical school (8+ years after high school)","$200K-$400K+","Science, empathy, decision-making, stamina","Dr. Rivera starts rounds at 7 AM, checking on patients. She diagnoses a rare condition, prescribes treatment, and sees the relief in a family's eyes. Long days, but nothing compares to helping people heal.","Do you want to solve body mysteries and help people?"),
            ("Nurse","Provide direct patient care and support","Nursing degree (2-4 years)","$55K-$120K+","Compassion, multitasking, science, calm under pressure","Marcus monitors patients, administers medication, comforts worried families, and catches a subtle change in a patient's condition that saves their life. Nurses are healthcare heroes.","Do you want to care for people directly every day?"),
            ("Veterinarian","Doctor for animals of all kinds","Vet school (8 years total)","$80K-$150K+","Animal love, science, problem-solving","Dr. Patel just performed surgery on a golden retriever, gave vaccines to a kitten, and advised a farmer about horse nutrition. Every day brings different animals and different challenges!","Do you love animals and want to keep them healthy?"),
            ("Physical Therapist","Help people recover movement after injuries","Doctoral degree (7 years)","$70K-$100K+","Patience, anatomy, motivation, hands-on","Jordan helps a teenager walk again after a car accident. Every session shows small progress. In 6 months, his patient runs again. PT is about celebrating incremental victories.","Do you enjoy exercise science and motivating people?"),
            ("Pharmacist","Expert on medications and their effects","PharmD degree (6-8 years)","$100K-$140K+","Chemistry, attention to detail, communication","Lin checks prescriptions for interactions, counsels patients on side effects, and catches a dangerous drug combination before it reaches a patient. Pharmacists prevent harm daily.","Do you like chemistry and helping people understand medicine?"),
            ("Mental Health Counselor","Help people overcome emotional challenges","Master's degree (6 years)","$50K-$90K+","Empathy, listening, patience, boundaries","Dr. Obi helps a teenager work through anxiety using evidence-based techniques. Over weeks, she watches her client transform from fearful to confident. Changing lives through conversation.","Do you naturally listen to others and want to help them feel better?"),
            ("Dentist","Care for teeth, gums, and oral health","Dental school (8 years)","$150K-$250K+","Precision, steady hands, people skills","Dr. Kim makes nervous kids laugh while fixing cavities. She also transforms smiles with braces and saves teeth from extraction. A healthy smile changes a person's whole confidence!","Do you like detail work with your hands and helping people smile?"),
            ("Surgeon","Perform operations to fix injuries and diseases","Medical school + residency (12+ years)","$300K-$600K+","Steady hands, focus, stamina, precision","Dr. Zhang performs a 4-hour brain surgery with absolute focus. One millimeter matters. The patient wakes up cancer-free. Years of training for moments that define lives.","Can you stay focused under extreme pressure for hours?"),
        ],
        "Creative Arts": [
            ("Author/Writer","Create stories, articles, or books","No specific degree required","$30K-$150K+ (varies hugely)","Creativity, discipline, storytelling, persistence","Emma writes for 4 hours each morning. She's drafting her third novel. Yesterday she got fan mail from a kid who said her book was their favorite. Writing is lonely work with magical rewards.","Do you love stories and have ideas you MUST share?"),
            ("Graphic Designer","Create visual content for brands and media","Bachelor's degree or self-taught","$45K-$100K+","Creativity, software skills, communication","Zion just designed a logo that will be seen by millions. He chooses colors, typography, and layouts that make brands instantly recognizable. Every visual you see was designed by someone like him.","Do you love visual art and making things look amazing?"),
            ("Musician/Composer","Create and perform music","Varies: self-taught to conservatory","$30K-$200K+ (varies)","Musical talent, practice, creativity, performance","Aria composes music for a Netflix show. She translates emotions into melodies. When viewers feel something during a scene, it's often her music creating that feeling.","Does music move you? Do you hear melodies in your head?"),
            ("Architect","Design buildings and spaces where people live and work","Bachelor's + Master's (5-7 years)","$70K-$130K+","Creativity, math, physics, visualization","Marco just unveiled his design for a new children's hospital. Every room is designed to make sick kids feel safe and happy. Architecture shapes how people FEEL about spaces.","Do you draw buildings and imagine new spaces?"),
            ("Film Director","Guide the creative vision of movies and shows","Film school or experience","$50K-$500K+ (varies hugely)","Vision, leadership, storytelling, persistence","Riya shouts 'Action!' and watches her vision come to life. She directs actors, chooses camera angles, and crafts emotional moments. A 2-hour movie takes 2 years to make!","Do you see stories in your head like movies? Want to make them real?"),
            ("Animator","Bring characters and stories to life through animation","Bachelor's degree or self-taught","$50K-$120K+","Art, technology, storytelling, patience","Felix spent 6 months animating a 3-minute sequence. Frame by frame, he brought a character to life. When audiences laugh at his character's expression, all those hours feel worth it.","Do you love drawing AND technology? Want characters to MOVE?"),
            ("Fashion Designer","Create clothing and accessories","Fashion school or self-taught","$40K-$150K+","Creativity, sewing, trends, business","Ava sketched a dress design at age 12. Now her clothing line is sold in stores. She combines art, culture, and functionality to create wearable art that makes people feel confident.","Do you redesign outfits in your head and notice clothing details?"),
            ("Photographer","Capture moments and tell stories through images","Self-taught or degree","$35K-$100K+","Eye for composition, technical skill, patience","Noah photographs wildlife, waiting hours for the perfect shot. One photo of a rare bird in flight wins an award and appears in National Geographic. Patience + skill = magic.","Do you see the world in frames? Notice light and shadow?"),
        ],
        "Business & Law": [
            ("Entrepreneur","Start and run your own business","No degree required (but helps!)","$0-$Unlimited","Risk-taking, creativity, persistence, leadership","At 22, Sofia started her company from her dorm room. At 30, she employs 50 people. Every day is different: sales, hiring, product design, strategy. No boss - but enormous responsibility.","Do you see problems and immediately think of solutions to sell?"),
            ("Lawyer","Advocate for clients and uphold justice","Law school (7 years after high school)","$80K-$300K+","Logic, persuasion, reading, research","Aisha argues her case before a judge. She spent weeks researching precedents. Today, her client is found not guilty. Justice served. The law is a tool for protecting people's rights.","Do you love arguing, research, and fighting for fairness?"),
            ("Marketing Manager","Help companies connect with customers","Bachelor's degree","$60K-$130K+","Creativity, data analysis, communication","Jake plans a campaign to launch a new product. He combines creative ads, social media, and data to reach the right people with the right message. When sales soar, his strategy worked!","Do you notice what makes you want to buy things?"),
            ("Financial Advisor","Help people manage and grow their money","Bachelor's + certifications","$60K-$150K+","Math, people skills, ethics, patience","Zara helps a family plan for their kids' college education. She creates investment strategies that grow wealth over time. Her advice literally shapes families' futures.","Are you good with money and enjoy helping people plan?"),
            ("Real Estate Agent","Help people buy, sell, and rent properties","License (varies by state)","$40K-$150K+","People skills, negotiation, local knowledge","Terrence just helped a family find their dream home. He negotiated the price down $15,000 and guided them through the complex process. He changes lives one home at a time.","Do you like houses, people, and negotiating deals?"),
            ("Teacher","Educate and inspire the next generation","Bachelor's degree + certification","$40K-$80K+","Patience, communication, creativity, knowledge","Ms. Williams watches a struggling student finally understand fractions. That 'lightbulb moment' is why she teaches. She's shaping 30 futures every single year.","Do you love explaining things and seeing people learn?"),
            ("CEO / Business Executive","Lead an entire company or organization","MBA often helpful","$100K-$500K+","Leadership, strategy, decision-making","After years of climbing the ladder, David leads a company of 5,000 employees. He sets the vision, makes tough calls, and is responsible for thousands of livelihoods.","Are you a natural leader who thinks big-picture?"),
            ("Journalist","Investigate and report news and stories","Bachelor's in journalism","$40K-$100K+","Writing, curiosity, ethics, persistence","Kira investigates a story about pollution in her city. Her published article leads to cleanup and policy change. Journalism holds power accountable and informs citizens.","Are you curious, love writing, and want to uncover truth?"),
        ],
        "Service & Active": [
            ("Firefighter","Protect communities from fires and emergencies","Training academy","$45K-$90K+","Bravery, physical fitness, teamwork, calm","When the alarm sounds, Captain Rodriguez leads her team into a burning building. They rescue a family and contain the blaze. Danger is real, but so is the purpose.","Are you brave, physically fit, and want to save lives?"),
            ("Police Officer","Protect communities and uphold the law","Police academy training","$45K-$90K+","Integrity, physical fitness, communication","Officer Tanaka walks his neighborhood beat, knowing everyone by name. He helps a lost child, de-escalates a dispute, and makes his community feel safe. Good policing is service.","Do you want to protect people and maintain justice?"),
            ("Chef","Create culinary experiences in restaurants","Culinary school or apprenticeship","$35K-$100K+","Creativity, palate, management, stamina","Chef Amara creates a new seasonal menu. She tastes, adjusts, and perfects each dish. When diners close their eyes and smile at the first bite, that's her art speaking.","Do you love cooking, flavors, and feeding people happiness?"),
            ("Pilot","Fly aircraft carrying passengers or cargo","Flight school + licenses","$80K-$200K+","Spatial awareness, calm, training, math","Captain Okonkwo guides a 747 carrying 400 passengers across the Atlantic. The sunrise from 35,000 feet never gets old. Flying is freedom, responsibility, and precision.","Do you dream of flight and love the feeling of being in the sky?"),
            ("Marine Biologist","Study ocean life and marine ecosystems","Master's/PhD","$50K-$100K+","Marine science, diving, research, patience","Dr. Nakamura dives into a coral reef to study fish populations. She discovers a new species! Her research helps protect oceans that produce 50% of Earth's oxygen.","Do you love the ocean and want to understand its creatures?"),
            ("Professional Athlete","Compete in sports at the highest level","Years of training","$50K-$Millions","Athletic talent, discipline, mental toughness","Serena trains 6 hours daily: 3 hours practice, 2 hours fitness, 1 hour mental preparation. On game day, all that preparation comes together in moments of pure excellence.","Are you exceptionally talented at a sport AND willing to sacrifice for it?"),
            ("Park Ranger","Protect and manage natural parks and forests","Bachelor's degree helpful","$35K-$70K+","Outdoor skills, education, conservation","Ranger Crow starts each day hiking through ancient forests, monitoring wildlife, educating visitors, and protecting land that will exist long after her. Nature is both her office and her purpose.","Do you love being outdoors and want to protect wild places?"),
            ("Social Worker","Help people and families overcome challenges","Master's degree","$45K-$75K+","Empathy, resilience, advocacy, boundaries","Carmen helps a family access housing, therapy, and food assistance. She advocates for children in court. Social work is emotionally demanding but profoundly meaningful.","Do you want to fight for vulnerable people and create change?"),
        ],
    }

    title_page(doc, "WHAT DO YOU WANT TO BE?", "50 Amazing Careers Explored for Kids (Ages 9-14)", "50 Careers * Day-in-the-Life * Skills Quiz * Career Plan")
    copyright_page(doc, "WHAT DO YOU WANT TO BE? 50 Amazing Careers")
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0)
    y = 685
    for cat in careers:
        doc.add_text(72, y, f"{cat}", 'F2', 12, 0.1)
        y -= 22
    doc.add_text(72, y, "Skills Assessment Quiz", 'F4', 12, 0.2); y -= 22
    doc.add_text(72, y, "My Dream Job Page", 'F4', 12, 0.2); y -= 22
    doc.add_text(72, y, "Career Action Plan", 'F4', 12, 0.2)
    doc.new_page()

    career_num = 0
    for cat_name, cat_careers in careers.items():
        doc.add_filled_rect(50, 380, 512, 100, 0.9)
        doc.add_centered_text(440, cat_name.upper(), 'F2', 20, 0)
        doc.new_page()
        
        for title, desc, edu, salary, skills, story, quiz in cat_careers:
            career_num += 1
            doc.add_text(72, 730, f"CAREER #{career_num}", 'F1', 10, 0.4)
            doc.add_text(72, 708, title, 'F2', 16, 0)
            doc.add_line(72, 700, 350, 700, 1, 0.3)
            doc.add_text(72, 682, desc, 'F4', 10, 0.2)
            
            y = 655
            doc.add_text(72, y, f"Education: {edu}", 'F1', 9, 0.3)
            y -= 15
            doc.add_text(72, y, f"Salary Range: {salary}", 'F1', 9, 0.3)
            y -= 15
            doc.add_text(72, y, f"Key Skills: {skills}", 'F1', 9, 0.3)
            
            y -= 22
            doc.add_text(72, y, "A DAY IN THE LIFE:", 'F2', 10, 0.1)
            y -= 16
            y = add_wrapped(doc, 90, y, story, 'F4', 9, 0.2, 68)
            
            y -= 15
            doc.add_text(72, y, f"IS THIS FOR ME? {quiz}", 'F2', 9, 0.1)
            y -= 18
            doc.add_text(90, y, "My answer (circle): DEFINITELY  /  MAYBE  /  NOT FOR ME", 'F1', 9, 0.4)
            doc.new_page()

    # Skills quiz
    doc.add_centered_text(720, "SKILLS ASSESSMENT QUIZ", 'F2', 16, 0)
    doc.add_centered_text(695, "Rate yourself 1-5 on each skill:", 'F4', 11, 0.3)
    skills_list = ["Problem-solving","Creativity","Math/Numbers","Working with people","Physical activity","Writing/Communication","Science/Research","Leadership","Technology","Helping others","Attention to detail","Working with hands"]
    y = 665
    for sk in skills_list:
        doc.add_text(72, y, f"{sk}: 1 --- 2 --- 3 --- 4 --- 5", 'F1', 10, 0.3)
        y -= 22
    doc.new_page()

    # Dream job page
    doc.add_centered_text(720, "MY DREAM JOB", 'F2', 18, 0)
    fields = ["My dream career:","Why this excites me:","Skills I already have:","Skills I need to develop:","My first step toward this career:","Who I could talk to or shadow:","My backup career idea:"]
    y = 680
    for f in fields:
        doc.add_text(72, y, f"{f} _____________________________________________", 'F1', 11, 0.3)
        y -= 40
    doc.new_page()

    certificate(doc, "FUTURE CAREER EXPLORER CERTIFICATE")
    add_supplemental(doc, 'Careers', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book344_Kids_Career_Explorer.pdf')
    print("Book344_Kids_Career_Explorer.pdf created successfully!")

if __name__ == "__main__":
    create_book()
