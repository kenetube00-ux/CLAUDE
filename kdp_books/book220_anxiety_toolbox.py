"""Book 220: The Complete Anxiety Toolbox - 50 Evidence-Based Techniques"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.2)
    doc.add_centered_text(755, "THE COMPLETE ANXIETY", 'F2', 24, 1)
    doc.add_centered_text(725, "TOOLBOX", 'F2', 24, 1)
    doc.add_centered_text(665, "50 Evidence-Based Techniques in One Workbook", 'F4', 14, 0.3)
    doc.add_centered_text(625, "Cognitive | Physical | Behavioral | Acceptance | Lifestyle", 'F1', 11, 0.4)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    # Copyright
    doc.new_page()
    doc.add_centered_text(700, "THE COMPLETE ANXIETY TOOLBOX", 'F2', 14)
    doc.add_centered_text(675, "50 Evidence-Based Techniques in One Workbook", 'F1', 11)
    doc.add_centered_text(620, f"Copyright {author}", 'F1', 10)
    doc.add_centered_text(600, "All rights reserved.", 'F1', 10)

    # Page 3: Anxiety Profile Assessment
    doc.new_page()
    doc.add_centered_text(750, "UNDERSTANDING YOUR ANXIETY PROFILE", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = [
        "Rate each (0=never, 5=always):", "",
        "Physical symptoms: racing heart___ sweating___ trembling___ nausea___",
        "Cognitive: racing thoughts___ catastrophizing___ indecision___ rumination___",
        "Behavioral: avoidance___ reassurance-seeking___ procrastination___ checking___",
        "Emotional: dread___ irritability___ restlessness___ overwhelm___", "",
        "My primary anxiety type:",
        "[ ] Generalized (worry about everything)",
        "[ ] Social (fear of judgment)",
        "[ ] Panic (sudden intense attacks)",
        "[ ] Health (worry about illness)",
        "[ ] Specific phobia: ________________________________",
        "[ ] OCD-related (intrusive thoughts + rituals)",
        "[ ] PTSD-related (trauma responses)", "",
        "My anxiety level today (0-10): ___",
        "My average this week (0-10): ___",
        "My goal level (realistic): ___",
    ]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 18


    # 50 techniques organized by category - each gets half page
    # Cognitive (10 techniques)
    cognitive = [
        ("1. THOUGHT RECORDS", "Identify thought > evidence for/against > balanced thought",
         "When: caught in negative thinking loop"),
        ("2. DECATASTROPHIZING", "What's the worst/best/most likely? Can I cope with worst?",
         "When: imagining worst-case scenarios"),
        ("3. EVIDENCE TESTING", "What facts support this? What facts contradict it?",
         "When: believing something without proof"),
        ("4. WORRY TIME", "Schedule 15 min/day. Postpone worry until then.",
         "When: worry interrupts your day constantly"),
        ("5. COGNITIVE DEFUSION", "I notice I'm having the thought that... (observe, don't fuse)",
         "When: thoughts feel like facts"),
        ("6. REATTRIBUTION", "What else could explain this? Not everything is about me.",
         "When: personalizing or blaming yourself"),
        ("7. PROBABILITY ESTIMATION", "What's the actual % chance? (Usually <5%)",
         "When: overestimating threat likelihood"),
        ("8. RESPONSIBILITY PIE", "Divide 100% responsibility - how much is actually yours?",
         "When: taking on too much blame"),
        ("9. BEHAVIORAL EXPERIMENTS", "Test your prediction. What actually happened?",
         "When: avoiding because you predict disaster"),
        ("10. SURVEY METHOD", "Ask others: do they think/feel this too? (normalize)",
         "When: believing you're the only one struggling"),
    ]
    
    physical = [
        ("11. DIAPHRAGMATIC BREATHING", "Belly rises on inhale (4ct), falls on exhale (6ct)",
         "When: panic symptoms, racing heart"),
        ("12. 4-7-8 BREATHING", "Inhale 4, hold 7, exhale 8 counts",
         "When: can't fall asleep, pre-event anxiety"),
        ("13. PROGRESSIVE MUSCLE RELAXATION", "Tense each muscle group 5 sec, release 10 sec",
         "When: body tension, headaches, jaw clenching"),
        ("14. BODY SCAN", "Slowly scan head to toe noticing sensations without changing",
         "When: disconnected from body, floating anxiety"),
        ("15. COLD EXPOSURE", "Cold water on face/wrists activates dive reflex, slows heart",
         "When: panic attack, intense emotion, need quick reset"),
        ("16. EXERCISE PRESCRIPTION", "20 min moderate cardio = anxiety reduction for 4+ hours",
         "When: chronic tension, restlessness, rumination"),
        ("17. YOGA/STRETCHING", "Gentle poses with breath focus. Child's pose, cat-cow.",
         "When: morning anxiety, body stiffness, need grounding"),
        ("18. 5-4-3-2-1 GROUNDING", "5 see, 4 touch, 3 hear, 2 smell, 1 taste",
         "When: dissociation, derealization, panic"),
        ("19. BILATERAL STIMULATION", "Tap alternating knees, butterfly hug, walk",
         "When: stuck in distress, processing difficult emotions"),
        ("20. VAGUS NERVE ACTIVATION", "Hum, gargle, cold face, slow exhale",
         "When: fight/flight stuck on, need to activate calm"),
    ]
    
    behavioral = [
        ("21. EXPOSURE HIERARCHY", "List fears 0-10. Start at 3. Work up gradually.",
         "When: avoidance is running your life"),
        ("22. RESPONSE PREVENTION", "Feel the urge. Don't do the ritual. Wait it out.",
         "When: compulsive checking, reassurance seeking"),
        ("23. BEHAVIORAL ACTIVATION", "Schedule activities even when you don't feel like it",
         "When: avoidance + depression keeping you stuck"),
        ("24. APPROACH GOALS", "Move TOWARD what you want, not away from fear",
         "When: all your goals are avoidance-based"),
        ("25. SAFETY BEHAVIOR REDUCTION", "Drop one safety behavior at a time",
         "When: you only cope by controlling everything"),
        ("26. VALUED ACTION", "What would you do if anxiety wasn't deciding?",
         "When: anxiety is choosing your life for you"),
        ("27. SOCIAL SKILLS PRACTICE", "Script > rehearse > try in low-stakes situation",
         "When: social anxiety from skill deficit"),
        ("28. ASSERTIVENESS", "I feel___ when___ because___ I need___",
         "When: people-pleasing causes anxiety"),
        ("29. PROBLEM SOLVING", "Define problem > brainstorm > pros-cons > choose > act",
         "When: anxiety comes from unsolved real problems"),
        ("30. ACTIVITY SCHEDULING", "Plan positive activities daily. Don't wait to feel better.",
         "When: withdrawal is worsening your anxiety"),
    ]
    
    acceptance = [
        ("31. MINDFULNESS MEDITATION", "Observe thoughts like clouds. Don't chase or push away.",
         "When: daily practice to reduce baseline anxiety"),
        ("32. ACT (ACCEPTANCE)", "Make room for anxiety AND move toward values",
         "When: fighting anxiety makes it worse"),
        ("33. SELF-COMPASSION", "Treat yourself like you'd treat a friend who's struggling",
         "When: self-criticism amplifies anxiety"),
        ("34. WORRY POSTPONEMENT", "Write worry down. Promise to address at scheduled time.",
         "When: worry interrupts work/relationships"),
        ("35. ACCEPTANCE COMMITMENT", "I accept anxiety is here. I commit to ___ anyway.",
         "When: waiting to feel ready keeps you stuck"),
        ("36. RADICAL ACCEPTANCE", "This is what is. Fighting reality adds suffering.",
         "When: resisting unchangeable circumstances"),
        ("37. DISTRESS TOLERANCE", "I can feel this without acting on it. It will pass.",
         "When: urge to escape is overwhelming"),
        ("38. EMOTION SURFING", "Ride the wave. It peaks and falls. Always.",
         "When: panic/intense emotion feels permanent"),
        ("39. METACOGNITIVE AWARENESS", "Thoughts about thoughts aren't facts either.",
         "When: worry about worry (meta-worry)"),
        ("40. DEFUSION EXERCISES", "Sing the thought. Say it in funny voice. Thank your mind.",
         "When: intrusive thoughts feel powerful"),
    ]
    
    lifestyle = [
        ("41. SLEEP HYGIENE", "Consistent time, dark room, no screens 1hr before",
         "When: poor sleep worsens next-day anxiety"),
        ("42. CAFFEINE AUDIT", "Track caffeine intake. Reduce if >200mg/day.",
         "When: physical anxiety symptoms won't reduce"),
        ("43. SOCIAL CONNECTION", "Schedule 1 meaningful interaction daily",
         "When: isolation amplifies anxious thoughts"),
        ("44. NATURE EXPOSURE", "20 min in nature reduces cortisol significantly",
         "When: chronic stress, need nervous system reset"),
        ("45. GRATITUDE PRACTICE", "3 specific things daily. Rewires negativity bias.",
         "When: catastrophic thinking dominates"),
        ("46. MEDIA DIET", "Limit news to 15 min/day. Unfollow anxiety triggers.",
         "When: doom-scrolling escalates worry"),
        ("47. ROUTINE BUILDING", "Predictable routine = less decisions = less anxiety",
         "When: chaos in schedule creates overwhelm"),
        ("48. BOUNDARY SETTING", "No is a complete sentence. Overcommitment = anxiety.",
         "When: saying yes to everything burns you out"),
        ("49. VALUES CLARIFICATION", "What matters MOST? Align actions with top 5 values.",
         "When: anxiety comes from living misaligned"),
        ("50. MEANING & PURPOSE", "Find your why. Anxiety decreases when purpose is clear.",
         "When: existential anxiety, feeling directionless"),
    ]
    
    all_categories = [
        ("COGNITIVE TECHNIQUES (1-10)", cognitive),
        ("PHYSICAL TECHNIQUES (11-20)", physical),
        ("BEHAVIORAL TECHNIQUES (21-30)", behavioral),
        ("ACCEPTANCE TECHNIQUES (31-40)", acceptance),
        ("LIFESTYLE TECHNIQUES (41-50)", lifestyle),
    ]
    
    for cat_name, techniques in all_categories:
        # 2 pages per category (5 techniques per page)
        for page_idx in range(2):
            doc.new_page()
            doc.add_centered_text(760, cat_name, 'F2', 12, 0.3)
            doc.add_line(72, 750, 540, 750, 0.5, 0.3)
            y = 730
            page_techniques = techniques[page_idx*5:(page_idx+1)*5]
            for name, how, when in page_techniques:
                doc.add_text(72, y, name, 'F2', 10)
                y -= 16
                doc.add_text(90, y, f"How: {how}", 'F1', 9)
                y -= 14
                doc.add_text(90, y, f"When to use: {when}", 'F4', 9)
                y -= 16
                doc.add_text(90, y, "Practice notes:", 'F1', 8)
                doc.add_line(160, y-2, 540, y-2, 0.5, 0.5)
                y -= 14
                doc.add_line(90, y-2, 540, y-2, 0.5, 0.5)
                y -= 14
                doc.add_text(90, y, "Effectiveness (1-10): ___  Will use again? [ ] Yes [ ] No", 'F1', 8)
                y -= 25


    # My Top 10 Techniques page
    doc.new_page()
    doc.add_centered_text(755, "MY TOP 10 ANXIETY TECHNIQUES", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "After trying techniques, record your top 10 go-to tools:", 'F1', 10)
    y -= 25
    for i in range(1, 11):
        doc.add_text(72, y, f"{i}. Technique: ________________________________", 'F1', 10)
        y -= 16
        doc.add_text(100, y, "Best for (situation): ________________________________", 'F1', 9)
        y -= 16
        doc.add_text(100, y, "How quickly it works: ________________________________", 'F1', 9)
        y -= 25

    # Weekly Anxiety Tracker (4 pages)
    for week in range(1, 5):
        doc.new_page()
        doc.add_centered_text(755, f"WEEKLY ANXIETY TRACKER - WEEK {week}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in days:
            doc.add_text(72, y, f"{day}: Level ___/10  Trigger: _______________", 'F1', 9)
            y -= 14
            doc.add_text(100, y, "Technique used: _______________  Result: ___/10", 'F1', 9)
            y -= 20
        y -= 10
        doc.add_text(72, y, "Week average: ___/10  Best day: ___  Pattern noticed:", 'F1', 9)
        doc.add_line(380, y-2, 540, y-2, 0.5, 0.4)

    # My Anxiety Action Plan (final page)
    doc.new_page()
    doc.add_centered_text(755, "MY ANXIETY ACTION PLAN", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    plan_items = [
        "When anxiety is 1-3 (mild):", "  I will: ________________________________", "",
        "When anxiety is 4-6 (moderate):", "  I will: ________________________________", "",
        "When anxiety is 7-8 (severe):", "  I will: ________________________________", "",
        "When anxiety is 9-10 (crisis):", "  I will: ________________________________", "",
        "Daily prevention routine:", "  Morning: ________________________________",
        "  Afternoon: ________________________________", "  Evening: ________________________________", "",
        "Professional support:", "  Therapist: ________________________________",
        "  Psychiatrist: ________________________________",
        "  Crisis line: 988", "",
        "My commitment: ________________________________",
    ]
    for line in plan_items:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 18

    doc.save("Book220_Anxiety_Toolbox_Complete.pdf")
    print("Created: Book220_Anxiety_Toolbox_Complete.pdf")

if __name__ == "__main__":
    create_book()
