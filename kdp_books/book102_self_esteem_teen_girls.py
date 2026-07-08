from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, "I AM ENOUGH", 'F2', 22)
pdf.add_centered_text(450, "A Self-Esteem Workbook for Teen Girls", 'F4', 13)
pdf.add_centered_text(350, "Discover Your Worth, Build Confidence,", 'F4', 11)
pdf.add_centered_text(335, "and Embrace the Amazing Girl You Are", 'F4', 11)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, "I AM ENOUGH", 'F2', 12)
pdf.add_centered_text(480, "A Self-Esteem Workbook for Teen Girls", 'F4', 10)
pdf.add_centered_text(450, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(430, "All rights reserved.", 'F4', 10)

# Page 3: Who Am I - Identity Page
pdf.new_page()
pdf.add_centered_text(610, "WHO AM I?", 'F2', 16)
pdf.add_line(50, 600, 382, 600)
y = 575
identity = [
    "You are more than your grades. More than your looks. More than",
    "what anyone thinks of you. Let's discover who you REALLY are.",
    "",
    "My name is: ____________________________________",
    "I am _____ years old.",
    "Three words my best friend would use to describe me:",
    "1. _____________ 2. _____________ 3. _____________",
    "",
    "Things I love to do (not for anyone else, just for ME):",
    "_______________________________________________",
    "_______________________________________________",
    "",
    "I feel happiest when: __________________________",
    "I feel proud of myself when: ___________________",
    "Something unique about me that nobody else has: ",
    "_______________________________________________",
    "",
    "If I could change the world, I would: __________",
    "_______________________________________________",
    "",
    "The person I want to become: ___________________",
    "_______________________________________________",
    "",
    "Remember: You don't have to be perfect to be WORTHY."
]
for line in identity:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16


# Page 4: My Strengths List
pdf.new_page()
pdf.add_centered_text(610, "MY STRENGTHS LIST", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
pdf.add_text(50, y, "Circle or check the strengths that describe you:", 'F4', 10)
y -= 20
strengths = ["Kind", "Creative", "Brave", "Funny", "Smart", "Loyal", "Honest",
    "Hardworking", "Patient", "Caring", "Adventurous", "Determined", "Artistic",
    "Musical", "Athletic", "Organized", "Good listener", "Compassionate",
    "Curious", "Resilient", "Generous", "Thoughtful", "Independent", "Flexible"]
for i, s in enumerate(strengths):
    col = i % 3
    row = i // 3
    pdf.add_rect(55 + col*125, y - row*20 - 2, 10, 10, 0.5)
    pdf.add_text(72 + col*125, y - row*20, s, 'F4', 9)
y -= (len(strengths)//3 + 1) * 20 + 10
pdf.add_text(50, y, "My TOP 5 strengths (these are my superpowers!):", 'F2', 10)
y -= 20
for i in range(5):
    pdf.add_text(50, y, f"{i+1}. ", 'F1', 10)
    pdf.add_line(65, y-2, 380, y-2, 0.5, 0.5)
    y -= 22

# Page 5: Challenging Negative Self-Talk
pdf.new_page()
pdf.add_centered_text(610, "CHALLENGING NEGATIVE SELF-TALK", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
selftalk = [
    "That mean voice in your head? It's NOT telling the truth.",
    "Let's talk back to it!",
    "",
    "NEGATIVE THOUGHT: 'I'm not pretty enough'",
    "TRUTH: Beauty comes in infinite forms. My worth is not",
    "determined by how I look. I am so much more than my appearance.",
    "",
    "NEGATIVE THOUGHT: 'Nobody likes me'",
    "TRUTH: I have people who care. Not everyone has to like me,",
    "and that's okay. I like myself, and that matters most.",
    "",
    "NEGATIVE THOUGHT: 'I'm so stupid'",
    "TRUTH: Making mistakes means I'm learning. Intelligence shows",
    "up in many ways. I am capable and growing every day.",
    "",
    "NOW YOUR TURN:",
    "Negative thought I often have: _________________",
    "_______________________________________________",
    "The TRUTH to replace it: ______________________",
    "_______________________________________________",
    "",
    "Negative thought I often have: _________________",
    "_______________________________________________",
    "The TRUTH to replace it: ______________________",
    "_______________________________________________"
]
for line in selftalk:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 6: Social Media vs Reality
pdf.new_page()
pdf.add_centered_text(610, "SOCIAL MEDIA vs REALITY", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
social = [
    "What you see on social media is a HIGHLIGHT REEL, not real life.",
    "",
    "THINGS TO REMEMBER:",
    "- Filters change how people actually look",
    "- People only post their best moments",
    "- Likes and followers do NOT equal worth",
    "- Comparison is the thief of joy",
    "- Most influencers feel insecure too",
    "",
    "MY SOCIAL MEDIA REALITY CHECK:",
    "How much time do I spend on social media daily? ___ hours",
    "How do I FEEL after scrolling? (circle one)",
    "  Happy / Inspired / Neutral / Anxious / Sad / Jealous",
    "",
    "Accounts that make me feel BAD about myself:",
    "_______________________________________________",
    "Action: UNFOLLOW or MUTE them today!",
    "",
    "Accounts that INSPIRE and UPLIFT me:",
    "_______________________________________________",
    "Action: Follow MORE accounts like these!",
    "",
    "MY BOUNDARIES:",
    "- I will limit social media to ___ minutes/day",
    "- I will not check social media before ___am",
    "- I will not check social media after ___pm",
    "- I will never read comments on [topic] posts"
]
for line in social:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 7: Body Positivity Exercises
pdf.new_page()
pdf.add_centered_text(610, "BODY POSITIVITY EXERCISES", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
body_pos = [
    "Your body is not an ornament. It is an INSTRUMENT.",
    "",
    "EXERCISE 1: Thank Your Body",
    "Write 5 things your body DOES for you (not how it looks):",
    "1. My legs let me ______________________________",
    "2. My arms let me ______________________________",
    "3. My brain lets me _____________________________",
    "4. My heart lets me _____________________________",
    "5. My voice lets me _____________________________",
    "",
    "EXERCISE 2: Mirror Talk",
    "Look in the mirror and say 3 kind things to yourself.",
    "Not about your looks - about who you ARE.",
    "I say: ________________________________________",
    "I say: ________________________________________",
    "I say: ________________________________________",
    "",
    "EXERCISE 3: Body Neutral Statement",
    "Instead of 'I love my body' or 'I hate my body', try:",
    "'My body is ___________ and that is okay.'",
    "'Today my body helped me ___________________.'",
    "",
    "EXERCISE 4: Media Literacy",
    "Name 3 ways ads/media try to make you feel bad about",
    "your body so you'll BUY something:",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________"
]
for line in body_pos:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 8: Boundary Setting Scripts
pdf.new_page()
pdf.add_centered_text(610, "BOUNDARY SETTING SCRIPTS", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
boundary_text = [
    "Saying NO is not mean. It's SELF-RESPECT.",
    "",
    "When someone pressures you to do something you don't want:",
    "'No thanks, I'm good.' (You don't owe an explanation!)",
    "",
    "When a friend is being toxic or mean:",
    "'I don't like it when you talk to me that way. Please stop.'",
    "",
    "When someone shares your secrets:",
    "'That was private and it hurt that you shared it. I need to",
    "trust that what I tell you stays between us.'",
    "",
    "When someone comments on your body:",
    "'My body is not up for discussion.'",
    "",
    "When you feel pressured in a relationship:",
    "'I'm not ready for that and if you respect me, you'll wait.'",
    "",
    "When adults dismiss your feelings:",
    "'My feelings are real and valid even if you don't understand.'",
    "",
    "PRACTICE: Write a boundary you need to set:",
    "With who: _____________________________________",
    "About what: ___________________________________",
    "I will say: ___________________________________",
    "_______________________________________________"
]
for line in boundary_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 9: Dealing with Comparison
pdf.new_page()
pdf.add_centered_text(610, "DEALING WITH COMPARISON", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
compare_text = [
    "Comparison steals your joy. Here's how to fight back:",
    "",
    "TRUTH BOMB: When you compare your behind-the-scenes to",
    "someone else's highlight reel, you will ALWAYS lose.",
    "",
    "When I catch myself comparing, I will:",
    "1. Notice it: 'There I go again, comparing...'",
    "2. Redirect: 'What am I grateful for RIGHT NOW?'",
    "3. Celebrate them: 'Good for her! Her win is not my loss.'",
    "4. Remember: 'We are on different paths and timelines.'",
    "",
    "People I tend to compare myself to:",
    "_______________________________________________",
    "What comparing costs me (energy, joy, confidence):",
    "_______________________________________________",
    "",
    "MY UNIQUE PATH:",
    "Something I can do that they can't: _____________",
    "A challenge I've overcome: _____________________",
    "A goal only I can achieve: _____________________",
    "",
    "MANTRA: 'I am not behind. I am not ahead.",
    "I am exactly where I need to be.'"
]
for line in compare_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 10: My Values Identification
pdf.new_page()
pdf.add_centered_text(610, "MY VALUES IDENTIFICATION", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
pdf.add_text(50, y, "Values are what matter most to YOU (not what others expect).", 'F4', 10)
y -= 15
pdf.add_text(50, y, "Circle your TOP 5 values:", 'F4', 10)
y -= 20
values = ["Honesty", "Family", "Creativity", "Adventure", "Kindness", "Education",
    "Faith", "Freedom", "Friendship", "Health", "Fun", "Justice",
    "Love", "Nature", "Peace", "Courage", "Growth", "Service"]
for i, v in enumerate(values):
    col = i % 3
    row = i // 3
    pdf.add_text(60 + col*125, y - row*20, v, 'F4', 10)
y -= (len(values)//3 + 1) * 20
pdf.add_text(50, y, "My TOP 5 values are:", 'F2', 10)
y -= 20
for i in range(5):
    pdf.add_text(50, y, f"{i+1}. ", 'F1', 10)
    pdf.add_line(65, y-2, 380, y-2, 0.5, 0.5)
    y -= 22
y -= 10
pdf.add_text(50, y, "How I will live these values this week:", 'F2', 10)
y -= 18
for i in range(3):
    pdf.add_line(50, y-2, 380, y-2, 0.5, 0.5)
    y -= 20

# Page 11: Confidence Boosters
pdf.new_page()
pdf.add_centered_text(610, "CONFIDENCE BOOSTERS", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
conf = [
    "Confidence is not 'I'm the best.' It's 'I'm enough.'",
    "",
    "30 WAYS TO BUILD CONFIDENCE THIS WEEK:",
    "1. Stand up straight (posture changes how you feel!)",
    "2. Make eye contact when talking to people",
    "3. Compliment someone else genuinely",
    "4. Try something new (even if you're bad at it)",
    "5. Speak up in class (your ideas matter)",
    "6. Wear something that makes YOU feel good",
    "7. Say 'thank you' instead of 'sorry'",
    "8. Set a small goal and achieve it TODAY",
    "9. Help someone who needs it",
    "10. Write down 3 things you did well today",
    "11. Stop apologizing for existing",
    "12. Take up space (sit wide, speak loud)",
    "13. Say your opinion even if others disagree",
    "14. Accept a compliment (just say 'thank you!')",
    "15. Do something alone (movie, cafe, walk)",
    "16. Learn a new skill from YouTube",
    "17. Celebrate a small win",
    "18. Ask for what you need",
    "19. Walk away from drama",
    "20. Choose yourself first (not selfish = necessary)"
]
for line in conf:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 12: Positive Affirmation Creation
pdf.new_page()
pdf.add_centered_text(610, "CREATE YOUR OWN AFFIRMATIONS", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
affirm = [
    "Affirmations rewire your brain. Say them daily, even if you",
    "don't believe them yet. Your brain will catch up!",
    "",
    "HOW TO WRITE POWERFUL AFFIRMATIONS:",
    "- Start with 'I am...' or 'I have...' or 'I can...'",
    "- Keep them positive (what you ARE, not what you're NOT)",
    "- Make them present tense (as if it's already true)",
    "- Make them specific to YOUR life",
    "",
    "EXAMPLES TO INSPIRE YOU:",
    "- I am worthy of love and respect",
    "- I am getting stronger every day",
    "- I have unique gifts to offer the world",
    "- I can do hard things",
    "- I am allowed to take up space",
    "",
    "NOW CREATE YOUR OWN (at least 5):",
    "1. I am ______________________________________",
    "2. I am ______________________________________",
    "3. I have ____________________________________",
    "4. I can _____________________________________",
    "5. I deserve __________________________________",
    "6. ___________________________________________",
    "7. ___________________________________________",
    "",
    "Tip: Write your favorites on sticky notes for your mirror!"
]
for line in affirm:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 13: Friendship Quality Assessment
pdf.new_page()
pdf.add_centered_text(610, "FRIENDSHIP QUALITY ASSESSMENT", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
friend = [
    "Not all friendships are equal. Some lift you up, others drain you.",
    "",
    "HEALTHY FRIENDSHIP SIGNS:",
    "- They celebrate your wins (no jealousy)",
    "- They respect your boundaries",
    "- You can be yourself around them",
    "- They keep your secrets safe",
    "- You feel BETTER after hanging out",
    "",
    "TOXIC FRIENDSHIP SIGNS:",
    "- They gossip about you behind your back",
    "- They make you feel bad about yourself",
    "- Everything is about THEM",
    "- They pressure you to do things you don't want",
    "- You feel DRAINED after hanging out",
    "",
    "MY FRIENDSHIP INVENTORY:",
    "Friend 1: _____________ Healthy / Toxic / Mixed",
    "Friend 2: _____________ Healthy / Toxic / Mixed",
    "Friend 3: _____________ Healthy / Toxic / Mixed",
    "Friend 4: _____________ Healthy / Toxic / Mixed",
    "",
    "One friendship I need to invest MORE in: ________",
    "One friendship I may need to step BACK from: ____",
    "A quality I want to bring to my friendships: _____"
]
for line in friend:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 14: Goal Setting with Self-Compassion
pdf.new_page()
pdf.add_centered_text(610, "GOAL SETTING WITH SELF-COMPASSION", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
goals = [
    "Goals should EXCITE you, not stress you out.",
    "Set goals from a place of growth, not 'not good enough.'",
    "",
    "ACADEMIC GOAL:",
    "What I want to achieve: ________________________",
    "First small step: _____________________________",
    "If I struggle, I will tell myself: ______________",
    "",
    "PERSONAL GOAL:",
    "What I want to achieve: ________________________",
    "First small step: _____________________________",
    "If I struggle, I will tell myself: ______________",
    "",
    "SOCIAL GOAL:",
    "What I want to achieve: ________________________",
    "First small step: _____________________________",
    "If I struggle, I will tell myself: ______________",
    "",
    "SELF-COMPASSION REMINDERS:",
    "- Progress over perfection, always",
    "- Mistakes are proof that I'm trying",
    "- I deserve the same kindness I give others",
    "- Resting is not quitting",
    "- I can try again tomorrow"
]
for line in goals:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 15: My Support Team
pdf.new_page()
pdf.add_centered_text(610, "MY SUPPORT TEAM", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
support = [
    "You don't have to do life alone. Who has your back?",
    "",
    "WHEN I FEEL SAD, I can talk to:",
    "Name: _________________ How to reach them: _____",
    "",
    "WHEN I FEEL SCARED, I can talk to:",
    "Name: _________________ How to reach them: _____",
    "",
    "WHEN I FEEL ANGRY, I can talk to:",
    "Name: _________________ How to reach them: _____",
    "",
    "WHEN I NEED ADVICE, I can talk to:",
    "Name: _________________ How to reach them: _____",
    "",
    "WHEN I JUST NEED TO LAUGH, I can call:",
    "Name: _________________ How to reach them: _____",
    "",
    "PROFESSIONAL SUPPORT:",
    "School counselor: ______________________________",
    "Therapist: ____________________________________",
    "Crisis text line: Text HOME to 741741",
    "",
    "Remember: Asking for help is BRAVE, not weak."
]
for line in support:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16


# Pages 16-25: Daily Affirmation Pages (10 pages)
affirmations_list = [
    "I am worthy of love exactly as I am.",
    "My voice matters and deserves to be heard.",
    "I am brave enough to be imperfect.",
    "I choose to be kind to myself today.",
    "I am growing into the woman I'm meant to be.",
    "My feelings are valid and important.",
    "I deserve good things without earning them.",
    "I am enough - not too much, not too little.",
    "Today I choose myself without guilt.",
    "I am a work in progress and that is beautiful."
]
for i, aff in enumerate(affirmations_list):
    pdf.new_page()
    pdf.add_centered_text(450, f"Day {i+1}", 'F1', 11, 0.4)
    pdf.add_centered_text(400, aff, 'F5', 13)
    pdf.add_line(80, 385, 352, 385, 0.5, 0.5)
    y = 350
    pdf.add_text(50, y, "How does this affirmation make me feel?", 'F2', 10)
    y -= 18
    for _ in range(3):
        pdf.add_line(50, y, 380, y, 0.5, 0.6)
        y -= 18
    y -= 10
    pdf.add_text(50, y, "One way I will live this truth today:", 'F2', 10)
    y -= 18
    for _ in range(3):
        pdf.add_line(50, y, 380, y, 0.5, 0.6)
        y -= 18
    y -= 10
    pdf.add_text(50, y, "Tonight's reflection - Did I honor myself today?", 'F2', 10)
    y -= 18
    for _ in range(4):
        pdf.add_line(50, y, 380, y, 0.5, 0.6)
        y -= 18

# Page 26: My Letter to Myself
pdf.new_page()
pdf.add_centered_text(610, "A LETTER TO MYSELF", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
pdf.add_text(50, y, "Write a letter to yourself. Be kind. Be honest. Be proud.", 'F4', 10)
y -= 25
pdf.add_text(50, y, "Dear Me,", 'F5', 11)
y -= 20
for _ in range(25):
    pdf.add_line(50, y, 380, y, 0.5, 0.6)
    y -= 18
y -= 10
pdf.add_text(50, y, "With love and pride,", 'F5', 11)
y -= 18
pdf.add_line(50, y, 200, y, 0.5, 0.5)

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book102_Self_Esteem_Teen_Girls.pdf')
print("Book102_Self_Esteem_Teen_Girls.pdf created successfully!")
