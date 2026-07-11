#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "HELPING YOUR ANXIOUS CHILD", 'F2', 20)
pdf.add_centered_text(485, "A Workbook for Parents", 'F4', 14)
pdf.add_centered_text(445, f"By {author}", 'F4', 12)
pdf.add_line(150, 425, 462, 425, 2)

# Page 2 - Copyright
pdf.new_page()
pdf.add_centered_text(500, f"Copyright - {author}", 'F1', 10)
pdf.add_centered_text(480, "All rights reserved.", 'F1', 10)
pdf.add_centered_text(450, "This workbook is for educational purposes.", 'F1', 10)
pdf.add_centered_text(430, "Consult a child psychologist for clinical guidance.", 'F1', 10)

# Page 3 - Understanding Child Anxiety
pdf.new_page()
pdf.add_centered_text(740, "UNDERSTANDING CHILD ANXIETY", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Anxiety is the #1 mental health issue in children (affects 1 in 8).", 'F1', 11)
pdf.add_text(50, 685, "It's NOT something kids grow out of without help.", 'F1', 11)
pdf.add_text(50, 655, "TYPES OF CHILDHOOD ANXIETY:", 'F2', 12)
types = [("Separation anxiety:", "Fear of being away from parents"),
         ("Social anxiety:", "Fear of judgment, embarrassment, peers"),
         ("Generalized anxiety:", "Worry about everything (grades, health, safety)"),
         ("Specific phobias:", "Intense fear of specific things (dogs, storms, needles)"),
         ("Selective mutism:", "Can't speak in certain settings despite talking at home")]
y = 630
for name, desc in types:
    pdf.add_text(60, y, name, 'F2', 10)
    pdf.add_text(210, y, desc, 'F1', 10)
    y -= 20
pdf.add_text(50, y-10, "SIGNS YOUR CHILD MAY HAVE ANXIETY:", 'F2', 11)
y -= 30
signs = ["Frequent stomachaches/headaches", "Avoids new situations or activities",
         "Asks 'what if' questions constantly", "Cries, clings, or has meltdowns before events",
         "Has trouble sleeping or needs you present to sleep",
         "Seeks constant reassurance", "Is a perfectionist",
         "Has outbursts that seem disproportionate"]
for s in signs:
    pdf.add_text(60, y, f"- {s}", 'F1', 10)
    y -= 16

# Page 4 - How Accommodation Makes It Worse
pdf.new_page()
pdf.add_centered_text(740, "HOW ACCOMMODATION MAKES ANXIETY GROW", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "ACCOMMODATION = changing YOUR behavior to reduce your child's anxiety.", 'F1', 11)
pdf.add_text(50, 680, "Examples:", 'F2', 11)
examples = ["Letting them stay home from school because they're anxious",
            "Speaking for them so they don't have to",
            "Sleeping in their room every night",
            "Avoiding all situations that trigger their anxiety",
            "Answering the same reassurance question 20 times",
            "Doing things for them they could do (ordering food, etc.)"]
y = 660
for e in examples:
    pdf.add_text(60, y, f"- {e}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-10, "WHY THIS BACKFIRES:", 'F2', 11)
y -= 30
reasons_a = ["It teaches: 'You CAN'T handle this' (confirms their fear)",
             "It prevents them from learning they CAN cope",
             "Anxiety's world shrinks - needs MORE accommodation over time",
             "It's exhausting for the whole family"]
for r in reasons_a:
    pdf.add_text(60, y, f"- {r}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-15, "MY CURRENT ACCOMMODATIONS (be honest):", 'F2', 11)
y -= 35
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20


# Page 5 - The BRAVE Approach
pdf.new_page()
pdf.add_centered_text(740, "THE BRAVE APPROACH", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "Gradual exposure helps your child learn they CAN handle hard things.", 'F1', 11)
brave = [
    ("B - Be understanding:", "Validate their feelings first. 'I see you're scared.'"),
    ("R - Reduce accommodation:", "Gradually stop doing things that maintain anxiety."),
    ("A - Approach the fear:", "Help them face fears in small steps (exposure ladder)."),
    ("V - Validate courage:", "'That was hard and you did it!' Praise bravery."),
    ("E - Expect setbacks:", "Progress isn't linear. Bad days don't erase progress."),
]
y = 680
for letter, desc in brave:
    pdf.add_text(60, y, letter, 'F2', 10)
    pdf.add_text(60, y-16, desc, 'F1', 10)
    y -= 40
pdf.add_text(50, y, "KEY PRINCIPLE: Your child needs to FEEL the anxiety and learn it passes.", 'F2', 10, 0.3)
pdf.add_text(50, y-20, "We can't remove all anxiety. We can build their confidence to cope.", 'F1', 10)

# Page 6 - Exposure Ladder
pdf.new_page()
pdf.add_centered_text(740, "CREATING AN EXPOSURE LADDER", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "WITH your child, list feared situations from least to most scary:", 'F1', 11)
pdf.add_text(50, 688, "My child's fear: ___________________________________________", 'F2', 11)
y = 660
for i in range(10, 0, -1):
    pdf.add_text(50, y, f"Step {i} (Fear rating {i*10}%):", 'F2', 9)
    pdf.add_line(200, y-2, 540, y-2, 0.5, 0.7)
    y -= 25
pdf.add_text(50, y-10, "Start at the BOTTOM. Don't move up until current step feels easy.", 'F2', 9, 0.3)
pdf.add_text(50, y-28, "Reward for each step completed: __________________________", 'F1', 10)

# Page 7 - Scripts for Anxious Moments
pdf.new_page()
pdf.add_centered_text(740, "SCRIPTS FOR ANXIOUS MOMENTS", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "What to SAY (and not say) when your child is anxious:", 'F2', 11)
scripts = [
    ("INSTEAD OF: 'There's nothing to worry about.'",
     "TRY: 'I see you're worried. What's your brain telling you?'"),
    ("INSTEAD OF: 'You'll be fine, stop being silly.'",
     "TRY: 'This feels hard right now. I believe you can do hard things.'"),
    ("INSTEAD OF: 'Okay, you don't have to go.'",
     "TRY: 'I know you're scared. Let's figure out how to do this together.'"),
    ("INSTEAD OF: 'What's wrong with you?'",
     "TRY: 'Your worry brain is being loud today. What can we do?'"),
]
y = 685
for bad, good in scripts:
    pdf.add_text(55, y, bad, 'F1', 9)
    pdf.add_text(55, y-14, good, 'F5', 9)
    y -= 38
pdf.add_text(50, y-5, "UNIVERSAL SCRIPTS:", 'F2', 10)
y -= 22
uni = ["'I'm right here with you.'",
       "'Your brain is sending a false alarm. You're safe.'",
       "'What's the worst that could happen? Could you handle it?'",
       "'Remember when you were scared of ___ and you did it anyway?'",
       "'I love you AND I know you can do this.'"]
for u in uni:
    pdf.add_text(60, y, u, 'F4', 9)
    y -= 15

# Pages 8-17 - Scenario Scripts (10 scenarios, 1 per page)
scenarios = [
    ("SCHOOL REFUSAL", ["Child says: 'I can't go to school. My stomach hurts.'",
     "Validate: 'I know mornings feel hard. Your body shows anxiety in your tummy.'",
     "Redirect: 'We're still going. What can we do to make the drive easier?'",
     "Plan: Walk them in? Meet teacher? Start with half day?",
     "Reward: 'After school today, you choose what we do together.'"]),
    ("SEPARATION ANXIETY", ["Child says: 'Don't leave me! What if something happens?'",
     "Validate: 'You love me and don't want me to go. I always come back.'",
     "Redirect: 'Let's make a plan. When will I be back? What will you do?'",
     "Plan: Transitional object? Practice short separations first.",
     "Reward: 'When I come back, we'll have special time together.'"]),
    ("SOCIAL ANXIETY", ["Child says: 'I don't want to go to the party. Nobody likes me.'",
     "Validate: 'Meeting people can feel scary. That's normal.'",
     "Redirect: 'What's one person you feel okay around?'",
     "Plan: Arrive early? Bring a friend? Leave after 30 min?",
     "Reward: 'You're building your brave muscles!'"]),
    ("MEDICAL/DOCTOR FEAR", ["Child says: 'I'm NOT getting a shot! NO!'",
     "Validate: 'Shots aren't fun. It's okay to feel nervous.'",
     "Redirect: 'It will hurt for 3 seconds. Then it's done. You can squeeze my hand.'",
     "Plan: Numbing cream? Count to 3? Look away? Breathe?",
     "Reward: Pick a treat after. Sticker chart for medical bravery."]),
    ("SLEEP ANXIETY", ["Child says: 'I can't sleep alone. What if a bad guy comes?'",
     "Validate: 'The dark can feel scary. Your brain imagines things at night.'",
     "Redirect: 'Our house is locked. You are safe. Let's make a sleep plan.'",
     "Plan: Gradual withdrawal? Nightlight? Check-in after 5 min?",
     "Reward: 'Every night you stay in bed earns a star!'"]),
    ("STORM/WEATHER FEAR", ["Child says: 'There's a storm coming! We're going to die!'",
     "Validate: 'Storms can be loud and scary. I understand.'",
     "Redirect: 'We are safe inside. Our house protects us. Let's count between thunder.'",
     "Plan: Create a storm kit? Learn about weather? Practice during mild storms.",
     "Reward: 'You were so brave! You used your coping skills!'"]),
    ("DOG/ANIMAL FEAR", ["Child says: 'That dog is going to bite me!'",
     "Validate: 'Some dogs look big and scary. Most are friendly.'",
     "Redirect: 'We can stay at this distance. Would you like to watch from here?'",
     "Plan: Gradual exposure - pictures, videos, calm dogs at distance, closer.",
     "Reward: 'You stayed calm near the dog! That took courage!'"]),
    ("GERM/CONTAMINATION FEAR", ["Child says: 'I need to wash my hands again! There are germs!'",
     "Validate: 'I know germs worry you. Your brain is being extra cautious.'",
     "Redirect: 'You already washed. Your hands are clean enough. We're moving on.'",
     "Plan: Limit washes per day? Delay washing by 5 min?",
     "Reward: 'You resisted the urge! Your brave brain is growing!'"]),
    ("PERFORMANCE/TEST ANXIETY", ["Child says: 'I'm going to fail! I can't do it!'",
     "Validate: 'Tests can feel stressful. It makes sense you're nervous.'",
     "Redirect: 'What's the worst that could happen? Could you handle that?'",
     "Plan: Study plan? Practice tests? Breathing before test?",
     "Reward: Focus on effort, not grade. 'You showed up and tried!'"]),
    ("NEW SITUATIONS", ["Child says: 'I'm not going. I don't know anyone there.'",
     "Validate: 'New places feel uncomfortable. That's normal.'",
     "Redirect: 'Remember last time you tried something new? How did it turn out?'",
     "Plan: Preview the place? Bring comfort item? Go for just 15 min?",
     "Reward: 'You expanded your world today! How do you feel now?'"]),
]
for title, lines in scenarios:
    pdf.new_page()
    pdf.add_centered_text(740, title, 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    y = 710
    for line in lines:
        pdf.add_text(55, y, line, 'F1', 9)
        y -= 18
    pdf.add_text(50, y-10, "MY NOTES FOR THIS SITUATION:", 'F2', 10)
    y -= 28
    for i in range(6):
        pdf.add_line(50, y, 540, y, 0.5, 0.7)
        y -= 18
    pdf.add_text(50, y-5, "Exposure steps we'll try:", 'F2', 9)
    y -= 20
    for i in range(4):
        pdf.add_text(50, y, f"{i+1}.", 'F1', 9)
        pdf.add_line(65, y-2, 540, y-2, 0.5, 0.7)
        y -= 18


# Page 18 - Reward System
pdf.new_page()
pdf.add_centered_text(740, "REWARD SYSTEM SETUP", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Rewards motivate brave behavior. NOT bribery - it's reinforcement!", 'F1', 10)
pdf.add_text(50, 685, "REWARD IDEAS (free or low-cost):", 'F2', 11)
rewards = ["Extra screen time (15 min)", "Stay up 15 min later",
           "Choose tonight's dinner", "Special one-on-one time",
           "Pick a family activity", "Sticker/star on chart",
           "Small toy/treat (after accumulating stars)",
           "Friend sleepover", "Skip a chore"]
y = 665
for r in rewards:
    pdf.add_text(60, y, f"- {r}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-10, "MY CHILD'S REWARD CHART:", 'F2', 11)
y -= 30
pdf.add_text(50, y, "Brave behavior:", 'F1', 10)
pdf.add_line(150, y-2, 540, y-2, 0.5, 0.7)
y -= 20
pdf.add_text(50, y, "Stars needed for small reward: ___  Big reward: ___", 'F1', 10)
y -= 20
pdf.add_text(50, y, "Small reward: _____________  Big reward: _____________", 'F1', 10)

# Page 19 - My Child's Anxiety Profile
pdf.new_page()
pdf.add_centered_text(740, "MY CHILD'S ANXIETY PROFILE", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Child's name: _________________  Age: ___", 'F1', 11)
pdf.add_text(50, 685, "TRIGGERS (what makes them anxious):", 'F2', 11)
y = 665
for i in range(4):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "EARLY WARNING SIGNS (how I can tell anxiety is rising):", 'F2', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "WHAT HELPS (coping that works for my child):", 'F2', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "WHAT MAKES IT WORSE:", 'F2', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20
pdf.add_text(50, y, "Current accommodations to reduce:", 'F2', 11)
y -= 20
for i in range(3):
    pdf.add_line(60, y, 540, y, 0.5, 0.7)
    y -= 20

# Pages 20-24 - Weekly Progress Tracker (5 pages)
for week in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(740, f"WEEKLY PROGRESS - WEEK {week}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    y = 712
    for day in days:
        pdf.add_text(50, y, day, 'F2', 8)
        pdf.add_text(80, y, "Exposure tried:_________________", 'F1', 7)
        pdf.add_text(265, y, "Child response:_____________", 'F1', 7)
        pdf.add_text(440, y, "Coaching used:________", 'F1', 7)
        pdf.add_line(50, y-10, 562, y-10, 0.3, 0.8)
        y -= 26
    pdf.add_text(50, y-5, "Brave moments this week:", 'F2', 9)
    pdf.add_line(50, y-18, 540, y-18, 0.5, 0.7)
    pdf.add_text(50, y-33, "Accommodations reduced:", 'F2', 9)
    pdf.add_line(50, y-46, 540, y-46, 0.5, 0.7)
    pdf.add_text(50, y-61, "What's working:", 'F2', 9)
    pdf.add_line(50, y-74, 540, y-74, 0.5, 0.7)
    pdf.add_text(50, y-89, "What needs adjustment:", 'F2', 9)
    pdf.add_line(50, y-102, 540, y-102, 0.5, 0.7)

# Pages 25-30 remaining
rest_titles = ["WHEN TO PUSH VS WHEN TO COMFORT", "SCHOOL ANXIETY ACTION PLAN",
               "COMMUNICATING WITH TEACHERS", "PROFESSIONAL HELP DECISION GUIDE",
               "PARENT SELF-CARE", "YOUR ANXIOUS CHILD IS BRAVE"]
for pg, t in enumerate(rest_titles):
    pdf.new_page()
    pdf.add_centered_text(740, t, 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 0:
        pdf.add_text(50, 710, "PUSH (encourage exposure) WHEN:", 'F2', 11)
        push = ["They've done this before successfully", "The fear is out of proportion to risk",
                "Avoidance is growing/spreading", "They can articulate the fear (it's not a meltdown)"]
        y = 690
        for p in push:
            pdf.add_text(60, y, f"- {p}", 'F1', 10)
            y -= 16
        pdf.add_text(50, y-10, "COMFORT (step back) WHEN:", 'F2', 11)
        y -= 28
        comfort = ["They're in full meltdown (can't think rationally)",
                   "There IS a real safety concern", "They're already overwhelmed from other stressors",
                   "They haven't been taught coping skills yet"]
        for c in comfort:
            pdf.add_text(60, y, f"- {c}", 'F1', 10)
            y -= 16
    elif pg == 4:  # Parent self-care
        pdf.add_text(50, 710, "Your anxiety matters too. Parenting an anxious child is exhausting.", 'F4', 10, 0.3)
        pdf.add_text(50, 685, "REMINDERS FOR YOU:", 'F2', 11)
        reminders = ["You are not causing your child's anxiety.",
                     "You can't love anxiety away (it needs skills, not just comfort).",
                     "Your own anxiety management models coping for your child.",
                     "It's okay to ask for help - for them AND for you.",
                     "Progress takes time. You're doing better than you think."]
        y = 665
        for r in reminders:
            pdf.add_text(60, y, f"- {r}", 'F1', 10)
            y -= 18
        pdf.add_text(50, y-10, "My self-care plan:", 'F2', 11)
        y -= 30
        for i in range(5):
            pdf.add_line(60, y, 540, y, 0.5, 0.7)
            y -= 20
    elif pg == 5:  # Closing
        pdf.add_centered_text(500, "Your anxious child is also", 'F4', 14)
        pdf.add_centered_text(475, "a BRAVE child.", 'F2', 16)
        pdf.add_centered_text(435, "Every time they face a fear,", 'F4', 12, 0.3)
        pdf.add_centered_text(415, "even imperfectly, they are growing.", 'F4', 12, 0.3)
        pdf.add_centered_text(385, "And you are the parent", 'F4', 12, 0.3)
        pdf.add_centered_text(365, "helping them find their courage.", 'F4', 12, 0.3)
        pdf.add_centered_text(325, "That matters more than you know.", 'F2', 12, 0.3)
    else:
        y = 710
        for i in range(28):
            pdf.add_line(50, y, 562, y, 0.5, 0.7)
            y -= 22

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book194_Anxious_Kids_Parent_Guide.pdf')
print("Book194_Anxious_Kids_Parent_Guide.pdf created successfully!")
