from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"
title = "SPEAK LOVE"
subtitle = "A Communication Workbook for Couples"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(480, title, 'F2', 20)
pdf.add_centered_text(450, subtitle, 'F4', 12)
pdf.add_centered_text(380, "Practical Exercises to Transform", 'F4', 10)
pdf.add_centered_text(365, "How You Talk, Listen, and Connect", 'F4', 10)
pdf.add_centered_text(230, f"By {author}", 'F2', 12)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(500, title, 'F2', 11)
pdf.add_centered_text(470, f"Copyright 2025 {author}", 'F4', 9)
pdf.add_centered_text(455, "All rights reserved.", 'F4', 9)
pdf.add_centered_text(425, "No part of this publication may be reproduced without permission.", 'F4', 8)


# Page 3: Communication Styles Assessment
pdf.new_page()
pdf.add_centered_text(610, "COMMUNICATION STYLES ASSESSMENT", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "PARTNER A: _______________   PARTNER B: _______________", 'F2', 9)
y -= 18
pdf.add_text(40, y, "Rate each statement 1 (never) to 5 (always). Both partners answer.", 'F4', 8)
y -= 14
statements = [
    "I express my needs clearly",
    "I listen without planning my response",
    "I shut down during conflict",
    "I raise my voice when frustrated",
    "I bring up past issues during arguments",
    "I use sarcasm when hurt",
    "I validate my partner's feelings",
    "I apologize when I am wrong",
    "I give the silent treatment",
    "I check in about my partner's day",
    "I criticize my partner's character (not just behavior)",
    "I use 'I' statements instead of 'you' accusations",
]
for stmt in statements:
    pdf.add_text(45, y, stmt, 'F4', 7)
    pdf.add_text(310, y, "A:___", 'F3', 7)
    pdf.add_text(350, y, "B:___", 'F3', 7)
    y -= 12
y -= 10
pdf.add_text(40, y, "MY COMMUNICATION STYLE (circle one for each partner):", 'F2', 8)
y -= 12
pdf.add_text(45, y, "Partner A: Passive / Aggressive / Passive-Aggressive / Assertive", 'F4', 8)
y -= 12
pdf.add_text(45, y, "Partner B: Passive / Aggressive / Passive-Aggressive / Assertive", 'F4', 8)
y -= 14
pdf.add_text(40, y, "OUR BIGGEST COMMUNICATION CHALLENGE:", 'F2', 8)
y -= 12
pdf.add_line(40, y, 392, y, 0.3, 0.5)
y -= 12
pdf.add_line(40, y, 392, y, 0.3, 0.5)


# Pages 4-6: Active Listening Exercises (3 pages)
for listen_page in range(1, 4):
    pdf.new_page()
    pdf.add_centered_text(610, f"ACTIVE LISTENING EXERCISE {listen_page}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    if listen_page == 1:
        intro_lines = [
            "Active listening means hearing to UNDERSTAND, not to RESPOND.",
            "Rules: Speaker talks 2 min. Listener ONLY listens (no interrupting).",
            "Then listener reflects: 'What I heard you say is...'",
            "Speaker confirms: 'Yes, that is right' or 'Actually, what I meant is...'",
            ""
        ]
        for line in intro_lines:
            pdf.add_text(40, y, line, 'F4', 8)
            y -= 12
    for exercise in range(2):
        ex_num = (listen_page - 1) * 2 + exercise + 1
        pdf.add_filled_rect(40, y - 3, 352, 190, 0.95)
        pdf.add_rect(40, y - 3, 352, 190, 0.5, 0.5)
        pdf.add_text(45, y + 173, f"PRACTICE #{ex_num}", 'F2', 9)
        pdf.add_text(45, y + 158, "SPEAKER (circle): Partner A / Partner B", 'F1', 8)
        pdf.add_text(45, y + 143, "Topic to share (choose something non-threatening):", 'F1', 8)
        pdf.add_line(45, y + 129, 385, y + 129, 0.3, 0.5)
        pdf.add_text(45, y + 114, "LISTENER reflection (what I heard you say is...):", 'F1', 8)
        pdf.add_line(45, y + 100, 385, y + 100, 0.3, 0.5)
        pdf.add_line(45, y + 86, 385, y + 86, 0.3, 0.5)
        pdf.add_text(45, y + 70, "Speaker: Did they get it right?  [ ] Yes  [ ] Close  [ ] No", 'F1', 8)
        pdf.add_text(45, y + 55, "What I wish they had heard:", 'F1', 8)
        pdf.add_line(45, y + 41, 385, y + 41, 0.3, 0.5)
        pdf.add_text(45, y + 26, "How did it feel to be truly listened to? (1-10): ___", 'F1', 8)
        pdf.add_text(45, y + 11, "How did it feel to listen without responding? (1-10): ___", 'F1', 8)
        y -= 205


# Pages 7-11: I-Statement Practice Sheets (5 pages)
for i_page in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(610, f"I-STATEMENT PRACTICE - PAGE {i_page}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    if i_page == 1:
        pdf.add_text(40, y, "Formula: 'When [situation], I feel [emotion], because [reason].", 'F2', 8)
        y -= 11
        pdf.add_text(40, y, "I need [request].'", 'F2', 8)
        y -= 11
        pdf.add_text(40, y, "WRONG: 'You never help around the house!'", 'F4', 8)
        y -= 11
        pdf.add_text(40, y, "RIGHT: 'When dishes pile up, I feel overwhelmed, because I feel", 'F4', 8)
        y -= 11
        pdf.add_text(40, y, "alone in managing our home. I need us to divide chores.'", 'F4', 8)
        y -= 16
    for entry in range(3):
        entry_num = (i_page - 1) * 3 + entry + 1
        pdf.add_filled_rect(40, y - 3, 352, 135, 0.95)
        pdf.add_rect(40, y - 3, 352, 135, 0.5, 0.5)
        pdf.add_text(45, y + 118, f"SITUATION #{entry_num}", 'F2', 8)
        pdf.add_text(45, y + 104, "When: ________________________________________________", 'F1', 8)
        pdf.add_text(45, y + 90, "I feel: ________________________________________________", 'F1', 8)
        pdf.add_text(45, y + 76, "Because: ______________________________________________", 'F1', 8)
        pdf.add_text(45, y + 62, "I need: ________________________________________________", 'F1', 8)
        pdf.add_text(45, y + 44, "Full I-Statement (put it all together):", 'F2', 7)
        pdf.add_line(45, y + 30, 385, y + 30, 0.3, 0.5)
        pdf.add_line(45, y + 16, 385, y + 16, 0.3, 0.5)
        pdf.add_text(45, y + 2, "Partner response: 'I hear you. What I can do is...'", 'F1', 7)
        pdf.add_line(270, y, 385, y, 0.3, 0.5)
        y -= 150


# Pages 12-16: Conflict De-escalation Scripts (5 scenarios)
scenarios = [
    ("FINANCES - 'You spent too much again'",
     "Instead of: 'You are so irresponsible with money!'",
     "Try: 'I feel anxious when unexpected charges appear. Can we look at our budget together this weekend?'"),
    ("PARENTING - 'You undermined me in front of the kids'",
     "Instead of: 'You always make me the bad guy!'",
     "Try: 'I felt unsupported when my decision was changed in front of the kids. Can we agree to discuss parenting decisions privately first?'"),
    ("HOUSEHOLD - 'You never help around here'",
     "Instead of: 'I do EVERYTHING and you just sit there!'",
     "Try: 'I feel overwhelmed by the amount of housework. I need us to create a fair system together. When can we talk about it?'"),
    ("INTIMACY - 'You never want to be close to me'",
     "Instead of: 'You obviously do not find me attractive anymore.'",
     "Try: 'I miss feeling close to you. I feel disconnected when we go a long time without physical affection. What do you need to feel more connected?'"),
    ("IN-LAWS - 'Your mother is too involved in our life'",
     "Instead of: 'Your mother is controlling and you let her!'",
     "Try: 'I feel our marriage needs more privacy. When your mom weighs in on our decisions, I feel like we are not a team. Can we set boundaries together?'")
]
for s_idx, (scenario_title, wrong, right) in enumerate(scenarios):
    pdf.new_page()
    pdf.add_centered_text(610, f"DE-ESCALATION SCRIPT {s_idx+1}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    pdf.add_text(40, y, f"SCENARIO: {scenario_title}", 'F2', 9)
    y -= 16
    pdf.add_text(40, y, wrong, 'F4', 8)
    y -= 14
    # Wrap right text
    right_text = right
    while len(right_text) > 60:
        split = right_text[:60].rfind(' ')
        pdf.add_text(40, y, right_text[:split], 'F4', 8)
        right_text = right_text[split+1:]
        y -= 11
    pdf.add_text(40, y, right_text, 'F4', 8)
    y -= 20
    pdf.add_text(40, y, "YOUR TURN - Write your own script for this scenario:", 'F2', 8)
    y -= 14
    pdf.add_text(40, y, "What usually happens in our version of this conflict:", 'F1', 8)
    y -= 12
    for _ in range(3):
        pdf.add_line(40, y, 392, y, 0.3, 0.5)
        y -= 12
    y -= 6
    pdf.add_text(40, y, "My de-escalating response:", 'F1', 8)
    y -= 12
    for _ in range(3):
        pdf.add_line(40, y, 392, y, 0.3, 0.5)
        y -= 12
    y -= 6
    pdf.add_text(40, y, "My partner's de-escalating response:", 'F1', 8)
    y -= 12
    for _ in range(3):
        pdf.add_line(40, y, 392, y, 0.3, 0.5)
        y -= 12
    y -= 6
    pdf.add_text(40, y, "Our agreed solution:", 'F1', 8)
    y -= 12
    for _ in range(3):
        pdf.add_line(40, y, 392, y, 0.3, 0.5)
        y -= 12


# Page 17: Repair Attempts Menu
pdf.new_page()
pdf.add_centered_text(610, "REPAIR ATTEMPTS MENU", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Repair attempts are phrases that de-escalate conflict.", 'F4', 8)
y -= 11
pdf.add_text(40, y, "Use them when a conversation is getting heated.", 'F4', 8)
y -= 16
repairs = [
    "1. 'I am getting flooded. Can we take a 20-minute break?'",
    "2. 'I am sorry. That came out wrong. Let me try again.'",
    "3. 'I can see your point.'",
    "4. 'We are on the same team here.'",
    "5. 'I love you even when we disagree.'",
    "6. 'Can we start over?'",
    "7. 'Tell me what you need right now.'",
    "8. 'I am feeling defensive. Give me a moment.'",
    "9. 'You are more important to me than being right.'",
    "10. 'I hear you. I may not agree yet, but I hear you.'",
    "11. 'What can I do right now to help?'",
    "12. 'I am scared this will turn into a fight.'",
    "13. 'Can we agree to disagree on this one?'",
    "14. 'I appreciate you telling me how you feel.'",
    "15. 'Please be gentle with me right now.'",
    "16. 'I want to understand. Say more about that.'",
    "17. 'Let us find a compromise we both can live with.'",
    "18. 'I was wrong. I am sorry.'",
    "19. 'Can I have a do-over?'",
    "20. 'One thing I love about you is...'",
]
for repair in repairs:
    pdf.add_text(45, y, repair, 'F4', 8)
    y -= 12
y -= 8
pdf.add_text(40, y, "OUR TOP 5 REPAIR PHRASES (circle favorites above):", 'F2', 8)
y -= 12
for i in range(5):
    pdf.add_text(45, y, f"{i+1}. _________________________________________________", 'F1', 8)
    y -= 12

# Pages 18-22: Weekly Check-in Template (5 pages)
for checkin in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(610, f"WEEKLY CHECK-IN - WEEK {checkin}", 'F2', 13)
    pdf.add_line(40, 600, 392, 600)
    y = 580
    pdf.add_text(40, y, "Date: ___/___/___  Set aside 20 min. No phones. Face each other.", 'F1', 8)
    y -= 16
    pdf.add_text(40, y, "ROSES (good things this week):", 'F2', 9)
    y -= 13
    pdf.add_text(45, y, "Partner A:", 'F1', 8)
    pdf.add_line(95, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 12
    pdf.add_line(45, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 14
    pdf.add_text(45, y, "Partner B:", 'F1', 8)
    pdf.add_line(95, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 12
    pdf.add_line(45, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 16
    pdf.add_text(40, y, "THORNS (challenges this week):", 'F2', 9)
    y -= 13
    pdf.add_text(45, y, "Partner A:", 'F1', 8)
    pdf.add_line(95, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 12
    pdf.add_line(45, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 14
    pdf.add_text(45, y, "Partner B:", 'F1', 8)
    pdf.add_line(95, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 12
    pdf.add_line(45, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 16
    pdf.add_text(40, y, "BUDS (things to look forward to):", 'F2', 9)
    y -= 13
    pdf.add_text(45, y, "Together:", 'F1', 8)
    pdf.add_line(85, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 14
    pdf.add_text(40, y, "APPRECIATION (one specific thing I appreciated about you):", 'F2', 8)
    y -= 13
    pdf.add_text(45, y, "A to B:", 'F1', 8)
    pdf.add_line(80, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 12
    pdf.add_text(45, y, "B to A:", 'F1', 8)
    pdf.add_line(80, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 16
    pdf.add_text(40, y, "NEEDS (one thing I need from you next week):", 'F2', 8)
    y -= 13
    pdf.add_text(45, y, "A:", 'F1', 8)
    pdf.add_line(55, y - 2, 392, y - 2, 0.3, 0.5)
    y -= 12
    pdf.add_text(45, y, "B:", 'F1', 8)
    pdf.add_line(55, y - 2, 392, y - 2, 0.3, 0.5)


# Page 23: Appreciation Practice (7 days)
pdf.new_page()
pdf.add_centered_text(610, "7-DAY APPRECIATION PRACTICE", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Every day for 7 days, tell your partner ONE specific thing", 'F4', 8)
y -= 11
pdf.add_text(40, y, "you appreciate about them. Write it here AND say it out loud.", 'F4', 8)
y -= 18
for day in range(1, 8):
    pdf.add_text(40, y, f"Day {day}  Date: ___/___/___", 'F2', 8)
    y -= 12
    pdf.add_text(45, y, "I appreciate: _____________________________________________", 'F1', 8)
    pdf.add_text(45, y - 12, "Their reaction: ___________________________________________", 'F1', 8)
    y -= 30
    pdf.add_line(40, y + 5, 392, y + 5, 0.2, 0.7)
    y -= 8
y -= 5
pdf.add_text(40, y, "After 7 days, how has our connection changed?", 'F2', 8)
y -= 12
pdf.add_line(40, y, 392, y, 0.3, 0.5)
y -= 12
pdf.add_line(40, y, 392, y, 0.3, 0.5)

# Page 24: Love Language Discovery
pdf.new_page()
pdf.add_centered_text(610, "LOVE LANGUAGE DISCOVERY", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "Rank each love language 1-5 (1 = most important to you):", 'F4', 8)
y -= 16
languages = ["Words of Affirmation (compliments, encouragement, 'I love you')",
    "Quality Time (undivided attention, being together, date nights)",
    "Physical Touch (hugs, holding hands, physical closeness)",
    "Acts of Service (doing helpful things, taking tasks off their plate)",
    "Receiving Gifts (thoughtful presents, tokens of love, surprises)"]
pdf.add_text(40, y, "PARTNER A:", 'F2', 9)
y -= 13
for lang in languages:
    pdf.add_text(45, y, f"___ {lang}", 'F4', 7)
    y -= 11
y -= 10
pdf.add_text(40, y, "PARTNER B:", 'F2', 9)
y -= 13
for lang in languages:
    pdf.add_text(45, y, f"___ {lang}", 'F4', 7)
    y -= 11
y -= 10
pdf.add_text(40, y, "DISCUSSION:", 'F2', 9)
y -= 12
pdf.add_text(45, y, "My #1 love language is: _______________________________________", 'F1', 8)
y -= 12
pdf.add_text(45, y, "I feel most loved when you: ___________________________________", 'F1', 8)
y -= 12
pdf.add_text(45, y, "I feel LEAST loved when you: __________________________________", 'F1', 8)
y -= 12
pdf.add_text(45, y, "One way to speak my language this week: ________________________", 'F1', 8)

# Page 25: Emotional Bid Response Tracker
pdf.new_page()
pdf.add_centered_text(610, "EMOTIONAL BID RESPONSE TRACKER", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "An 'emotional bid' is any attempt to connect (a touch, question,", 'F4', 8)
y -= 11
pdf.add_text(40, y, "comment, or look). You can TURN TOWARD, TURN AWAY, or TURN AGAINST.", 'F4', 8)
y -= 16
pdf.add_text(40, y, "Track your responses for one week:", 'F2', 8)
y -= 14
for day in range(1, 8):
    pdf.add_text(40, y, f"Day {day}", 'F2', 8)
    y -= 11
    pdf.add_text(45, y, "Bid made by: A / B  What they did/said: _______________________", 'F1', 7)
    y -= 10
    pdf.add_text(45, y, "Response: [ ] Turned toward (engaged)  [ ] Turned away (ignored)  [ ] Against (snapped)", 'F1', 7)
    y -= 14
y -= 6
pdf.add_text(40, y, "TOTALS: Turned toward: ___  Away: ___  Against: ___", 'F2', 8)
y -= 12
pdf.add_text(40, y, "Goal: Turn toward 80%+ of bids. This builds trust over time.", 'F4', 8)

# Page 26: Our Communication Agreements
pdf.new_page()
pdf.add_centered_text(610, "OUR COMMUNICATION AGREEMENTS", 'F2', 13)
pdf.add_line(40, 600, 392, 600)
y = 580
pdf.add_text(40, y, "We agree to the following rules for how we communicate:", 'F4', 9)
y -= 18
agreements = [
    "1. We will not use contempt (eye-rolling, mocking, name-calling)",
    "2. We will take a time-out when either of us is flooded",
    "3. Our time-out signal is: _____________________________________",
    "4. We will use 'I' statements instead of 'you' accusations",
    "5. We will not bring up past issues that have been resolved",
    "6. We will not argue in front of our children",
    "7. We will have a weekly check-in on: __________________________",
    "8. We will express appreciation daily",
    "9. We will assume positive intent before reacting",
    "10. We will _________________________________________________",
    "11. We will _________________________________________________",
    "12. We will _________________________________________________",
]
for agmt in agreements:
    pdf.add_text(40, y, agmt, 'F4', 8)
    y -= 14
y -= 10
pdf.add_text(40, y, "Signed:", 'F2', 9)
y -= 14
pdf.add_text(40, y, "Partner A: _________________________  Date: ___/___/___", 'F4', 8)
y -= 14
pdf.add_text(40, y, "Partner B: _________________________  Date: ___/___/___", 'F4', 8)

# Page 27: Date Night Conversation Starters (50 questions)
pdf.new_page()
pdf.add_centered_text(610, "DATE NIGHT CONVERSATION STARTERS", 'F2', 12)
pdf.add_line(40, 600, 392, 600)
y = 583
pdf.add_text(40, y, "50 questions to deepen connection. Pick 2-3 per date night.", 'F4', 8)
y -= 14
questions_list = [
    "1. What is your happiest memory of us?",
    "2. What are you most looking forward to?",
    "3. When do you feel most loved by me?",
    "4. What is a dream you have not told me?",
    "5. What is something new you want to try?",
    "6. How can I better support you right now?",
    "7. What do you wish we did more of together?",
    "8. What attracted you to me at first?",
    "9. What is your biggest worry right now?",
    "10. Where do you see us in 10 years?",
    "11. What is one thing I do that makes you smile?",
    "12. What is something small I could do daily?",
    "13. What does 'home' mean to you?",
    "14. What is your favorite way to relax?",
    "15. What would your perfect day look like?",
    "16. What is a childhood memory that shaped you?",
    "17. How do you want to grow as a person?",
    "18. What scares you most about the future?",
    "19. What makes you feel most alive?",
    "20. What is something you admire about me?",
    "21. If money was not an issue, what would change?",
    "22. What tradition should we start?",
    "23. What is the best gift I ever gave you?",
    "24. How do you want to be loved when sad?",
    "25. What is a goal we should pursue together?",
    "26. What song reminds you of us?",
    "27. What is your love language today?",
    "28. What do you need more of from me?",
    "29. What adventure should we plan?",
    "30. What have I taught you about life?",
    "31. What is your proudest moment?",
    "32. What do you value most in our relationship?",
    "33. What makes you feel safe with me?",
    "34. What is something you want to forgive?",
    "35. What legacy do we want to leave?",
    "36. What is your favorite thing about our home?",
    "37. How can we laugh more together?",
    "38. What is something I do not know about you?",
    "39. What makes our relationship unique?",
    "40. What is the hardest thing about being married?",
    "41. What is the best thing about being married?",
    "42. What is a fear you want to overcome?",
    "43. How do you want to celebrate our anniversary?",
    "44. What do you need more patience with?",
    "45. What is something kind someone did recently?",
    "46. What are you grateful for today?",
    "47. What do you want to be remembered for?",
    "48. How can we serve others together?",
    "49. What surprised you about marriage?",
    "50. Why do you still choose me every day?"
]
for q in questions_list:
    pdf.add_text(42, y, q, 'F4', 7)
    y -= 10

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book134_Couples_Communication_Workbook.pdf')
print("Book134_Couples_Communication_Workbook.pdf created successfully!")
