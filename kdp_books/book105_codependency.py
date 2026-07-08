from pdf_utils import PDFDoc
pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(490, "BREAKING FREE FROM", 'F2', 16)
pdf.add_centered_text(468, "CODEPENDENCY", 'F2', 18)
pdf.add_centered_text(440, "A Recovery Workbook", 'F4', 13)
pdf.add_centered_text(370, "Learn to Love Yourself First", 'F4', 11)
pdf.add_centered_text(200, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(500, "BREAKING FREE FROM CODEPENDENCY", 'F2', 12)
pdf.add_centered_text(475, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)

# Page 3: What is Codependency
pdf.new_page()
pdf.add_centered_text(610, "WHAT IS CODEPENDENCY?", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
for line in [
    "Codependency is a pattern of putting others' needs so far above",
    "your own that you lose yourself in the process.",
    "",
    "CODEPENDENCY IS:",
    "- Needing to be needed",
    "- Feeling responsible for others' feelings",
    "- Difficulty identifying your own needs",
    "- Poor boundaries or no boundaries",
    "- People-pleasing at the expense of yourself",
    "- Staying in unhealthy relationships out of fear",
    "- Controlling others 'for their own good'",
    "- Confusing love with rescuing or fixing",
    "",
    "CODEPENDENCY IS NOT:",
    "- Being a caring person (healthy caring has limits)",
    "- Being in a relationship (interdependence is healthy)",
    "- A permanent identity (recovery is possible)",
    "",
    "ROOT CAUSES:",
    "- Growing up with addiction in the family",
    "- Having emotionally unavailable parents",
    "- Being parentified (caring for adults as a child)",
    "- Trauma or neglect in childhood",
    "- Learning that love = sacrifice"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 4: Self-Assessment Quiz
pdf.new_page()
pdf.add_centered_text(610, "CODEPENDENCY SELF-ASSESSMENT", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 578
pdf.add_text(50, y, "Rate each statement 1-5 (1=never, 5=always):", 'F4', 9)
y -= 15
questions = [
    "I feel responsible for other people's feelings",
    "I have difficulty saying no to people",
    "I put others' needs before my own regularly",
    "I feel guilty when I do something for myself",
    "I need approval from others to feel good",
    "I stay in relationships that hurt me",
    "I try to fix or control other people",
    "I feel anxious when others are upset with me",
    "I neglect my own needs to help others",
    "I have trouble identifying what I want",
    "I apologize even when it's not my fault",
    "I attract people who need 'saving'",
    "I fear being abandoned or alone",
    "I feel empty without someone to care for",
    "I minimize or deny my own problems",
    "I cover for others' bad behavior",
    "I struggle to make decisions alone",
    "I ignore my own pain to focus on others",
    "I define myself by my relationships",
    "I have difficulty accepting compliments"
]
for i, q in enumerate(questions):
    pdf.add_text(50, y, f"{i+1}. {q}  ___", 'F4', 9)
    y -= 14
y -= 8
pdf.add_text(50, y, "TOTAL: ___/100", 'F2', 10)
y -= 14
pdf.add_text(50, y, "20-40: Mild tendencies  41-60: Moderate  61-80: Significant  81+: Severe", 'F3', 8)


# Page 5: People-Pleasing Patterns
pdf.new_page()
pdf.add_centered_text(610, "PEOPLE-PLEASING PATTERNS", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
for line in [
    "People-pleasing feels like kindness but it's actually self-abandonment.",
    "",
    "MY PEOPLE-PLEASING BEHAVIORS:",
    "__ Saying yes when I mean no",
    "__ Doing things I don't want to do to avoid conflict",
    "__ Agreeing with opinions I don't actually hold",
    "__ Over-volunteering at work/church/school",
    "__ Apologizing for things that aren't my fault",
    "__ Suppressing my true feelings to keep peace",
    "__ Doing favors and then feeling resentful",
    "__ Changing my personality depending on who I'm with",
    "",
    "WHO DO I PEOPLE-PLEASE THE MOST?",
    "Person: _____________ Why: ____________________",
    "Person: _____________ Why: ____________________",
    "",
    "WHAT PEOPLE-PLEASING COSTS ME:",
    "Energy: _______________________________________",
    "Authenticity: __________________________________",
    "Self-respect: __________________________________",
    "Time: _________________________________________",
    "",
    "THE TRUTH: People who only love the 'pleasing' version",
    "of you don't actually love YOU."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 6: Boundary Identification
pdf.new_page()
pdf.add_centered_text(610, "BOUNDARY IDENTIFICATION WORKSHEET", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
for line in [
    "Boundaries are not walls. They are doors YOU control.",
    "",
    "TYPES OF BOUNDARIES:",
    "Physical: Personal space, touch, privacy",
    "Emotional: Not taking on others' feelings as your own",
    "Time: How much time you give to others vs yourself",
    "Material: Money, possessions, lending/giving",
    "Mental: Your right to your own opinions and thoughts",
    "",
    "WHERE I NEED STRONGER BOUNDARIES:",
    "",
    "With my partner/spouse:",
    "I allow _________________ that I need to stop allowing.",
    "",
    "With my family:",
    "I allow _________________ that I need to stop allowing.",
    "",
    "At work:",
    "I allow _________________ that I need to stop allowing.",
    "",
    "With friends:",
    "I allow _________________ that I need to stop allowing.",
    "",
    "BOUNDARY I WILL SET THIS WEEK:",
    "What: ________________________________________",
    "With whom: ____________________________________",
    "How I'll communicate it: ______________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 7: Saying No Scripts
pdf.new_page()
pdf.add_centered_text(610, "SAYING NO - 10 SCRIPTS", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
for line in [
    "Saying no is a complete sentence. But here are softer options:",
    "",
    "1. 'I appreciate you asking, but I can't commit to that.'",
    "",
    "2. 'That doesn't work for me, but thank you.'",
    "",
    "3. 'I need to check my schedule and get back to you.'",
    "   (Buys time when you freeze in the moment)",
    "",
    "4. 'I'm not available for that, but I hope it goes well.'",
    "",
    "5. 'I've already committed my time elsewhere.'",
    "",
    "6. 'I'm prioritizing my own needs right now.'",
    "",
    "7. 'No.' (That's it. No explanation needed.)",
    "",
    "8. 'I care about you AND my answer is no.'",
    "",
    "9. 'Let me think about what I can realistically offer.'",
    "",
    "10. 'I've learned that overcommitting hurts us both.'",
    "",
    "PRACTICE: Write 'No' to a current request in your life:",
    "Request: ______________________________________",
    "My response: __________________________________"
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 8: Detachment Exercises
pdf.new_page()
pdf.add_centered_text(610, "DETACHMENT EXERCISES", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
for line in [
    "Detachment means releasing what you cannot control - with LOVE.",
    "",
    "EXERCISE 1: The Responsibility Check",
    "Situation I'm stressed about: __________________",
    "Is this MY responsibility? YES / NO",
    "Can I actually control this? YES / NO",
    "If NO: What can I release? ____________________",
    "",
    "EXERCISE 2: The Loving Release",
    "'I love [person] AND I release the outcome.'",
    "'I cannot want recovery more than they do.'",
    "'Their choices are theirs. My peace is mine.'",
    "",
    "EXERCISE 3: The STOP Technique",
    "S - Stop what you are doing",
    "T - Take a breath",
    "O - Observe (is this mine to fix?)",
    "P - Proceed (with YOUR life, not theirs)",
    "",
    "WHAT I AM CHOOSING TO DETACH FROM:",
    "_______________________________________________",
    "",
    "WHAT I AM CHOOSING TO FOCUS ON INSTEAD:",
    "_______________________________________________",
    "",
    "Detachment is not abandonment. It is self-preservation."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Page 9: Self-Worth Affirmations + Healthy vs Unhealthy Relationships
pdf.new_page()
pdf.add_centered_text(610, "HEALTHY vs UNHEALTHY RELATIONSHIPS", 'F2', 13)
pdf.add_line(50, 600, 382, 600)
y = 575
for line in [
    "HEALTHY (Interdependent)     | UNHEALTHY (Codependent)",
    "-----------------------------+---------------------------",
    "Both have separate identities| One loses self in the other",
    "Both can say no              | One always gives in",
    "Feelings are shared openly   | Feelings are hidden/managed",
    "Both have outside friends    | Isolation from others",
    "Conflict = growth            | Conflict = catastrophe",
    "Both take responsibility     | One always blamed",
    "Space is respected           | Clinginess or control",
    "Love feels peaceful          | Love feels chaotic",
    "",
    "MY CURRENT RELATIONSHIPS:",
    "Relationship 1: ____________ Healthy / Unhealthy / Mixed",
    "  What needs to change: ________________________",
    "",
    "Relationship 2: ____________ Healthy / Unhealthy / Mixed",
    "  What needs to change: ________________________",
    "",
    "SELF-WORTH AFFIRMATIONS:",
    "- I am worthy of love WITHOUT earning it.",
    "- I can be loved AND have boundaries.",
    "- My needs are not too much.",
    "- I am allowed to put myself first.",
    "- I am whole on my own."
]:
    pdf.add_text(50, y, line, 'F4', 9)
    y -= 15

# Page 10: My Needs Matter + Communication (I-statements)
pdf.new_page()
pdf.add_centered_text(610, "MY NEEDS MATTER + I-STATEMENTS", 'F2', 13)
pdf.add_line(50, 600, 382, 600)
y = 575
for line in [
    "IDENTIFYING MY NEEDS (check what you've been neglecting):",
    "__ Rest and sleep       __ Fun and play",
    "__ Alone time           __ Physical touch",
    "__ Creative expression  __ Financial security",
    "__ Honest communication __ Feeling heard",
    "__ Respect              __ Freedom to choose",
    "",
    "My most neglected need: ________________________",
    "One action to meet this need today: _____________",
    "",
    "COMMUNICATION WITH I-STATEMENTS:",
    "Instead of: 'You never listen to me!'",
    "Try: 'I feel unheard when I'm interrupted.'",
    "",
    "Formula: 'I feel [emotion] when [specific behavior]",
    "because [impact]. I need [specific request].'",
    "",
    "PRACTICE:",
    "I feel __________ when you ____________________",
    "because _______________________________________.",
    "I need ________________________________________.",
    "",
    "I feel __________ when you ____________________",
    "because _______________________________________.",
    "I need ________________________________________."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15


# Page 11: Letting Go Exercises + Building Self-Identity
pdf.new_page()
pdf.add_centered_text(610, "LETTING GO & BUILDING SELF-IDENTITY", 'F2', 13)
pdf.add_line(50, 600, 382, 600)
y = 575
for line in [
    "LETTING GO EXERCISES:",
    "",
    "Things I need to let go of:",
    "- The belief that I can fix other people: ________",
    "- The need for everyone to like me: ______________",
    "- Responsibility for others' emotions: ___________",
    "- Guilt for having my own needs: ________________",
    "",
    "BUILDING MY IDENTITY (separate from others):",
    "",
    "Outside of my relationships, I am:",
    "_______________________________________________",
    "",
    "Things I enjoy doing ALONE:",
    "1. _________________ 2. _______________________",
    "3. _________________ 4. _______________________",
    "",
    "Opinions I hold that are MINE (not borrowed):",
    "_______________________________________________",
    "",
    "Goals that are mine alone (not for someone else):",
    "1. ____________________________________________",
    "2. ____________________________________________",
    "3. ____________________________________________",
    "",
    "I am learning to be complete within myself."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Pages 12-15: Weekly Boundary Practice Log (4 pages)
for week in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(610, f"WEEKLY BOUNDARY PRACTICE LOG - WEEK {week}", 'F2', 12)
    pdf.add_line(50, 598, 382, 598)
    y = 580
    for day in range(7):
        pdf.add_text(50, y, f"Day {day+1}:", 'F2', 9)
        y -= 13
        pdf.add_text(50, y, "Boundary set or maintained: ___________________", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Said NO to: __________________________________", 'F3', 8)
        y -= 12
        pdf.add_text(50, y, "Self-care action: _____ Guilt level (1-10): ____", 'F3', 8)
        y -= 15
        pdf.add_line(50, y+4, 382, y+4, 0.3, 0.7)
        y -= 8

# Page 16: Recovery Commitments
pdf.new_page()
pdf.add_centered_text(610, "MY RECOVERY COMMITMENTS", 'F2', 14)
pdf.add_line(50, 600, 382, 600)
y = 575
for line in [
    "I commit to my codependency recovery:",
    "",
    "1. I will identify and honor my own needs daily.",
    "2. I will practice saying no without guilt.",
    "3. I will not take responsibility for others' feelings.",
    "4. I will maintain boundaries even when uncomfortable.",
    "5. I will not try to fix, control, or rescue others.",
    "6. I will build an identity separate from my relationships.",
    "7. I will seek support (therapy, CoDA meetings, friends).",
    "8. I will be patient and compassionate with myself.",
    "9. I will celebrate small victories.",
    "10. I choose ME without apology.",
    "",
    "Signed: _______________________________________",
    "Date: _________________________________________",
    "",
    "RESOURCES:",
    "- CoDA (Codependents Anonymous): www.coda.org",
    "- Al-Anon (if loved one has addiction): www.al-anon.org",
    "- Melody Beattie: 'Codependent No More'",
    "- Therapy: Look for therapists specializing in codependency",
    "",
    "You are worthy of the love you keep giving away to others."
]:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book105_Codependency_Workbook.pdf')
print("Book105_Codependency_Workbook.pdf created successfully!")
