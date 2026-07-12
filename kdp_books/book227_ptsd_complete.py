"""Book 227: The Complete PTSD Recovery Workbook"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.15)
    doc.add_centered_text(755, "THE COMPLETE PTSD", 'F2', 24, 1)
    doc.add_centered_text(722, "RECOVERY WORKBOOK", 'F2', 24, 1)
    doc.add_centered_text(660, "CPT, Grounding, Safety & Post-Traumatic Growth", 'F4', 13, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    doc.new_page()
    doc.add_centered_text(700, "THE COMPLETE PTSD RECOVERY WORKBOOK", 'F2', 13)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)
    doc.add_centered_text(630, "This workbook supports but does not replace professional treatment.", 'F4', 10)

    # Understanding PTSD
    doc.new_page()
    doc.add_centered_text(750, "UNDERSTANDING PTSD", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = ["PTSD can develop after experiencing or witnessing trauma.", "",
        "Types of trauma that can cause PTSD:",
        "  - Single incident (accident, assault, disaster)",
        "  - Complex/repeated (childhood abuse, domestic violence, war)",
        "  - Vicarious (first responders, therapists, witnesses)", "",
        "Core symptoms:", "  Re-experiencing: flashbacks, nightmares, intrusive thoughts",
        "  Avoidance: avoiding reminders, emotional numbing",
        "  Hyperarousal: hypervigilance, startle response, insomnia",
        "  Negative changes: beliefs about self/world, guilt, shame", "",
        "Recovery IS possible. Your brain can heal.", "This workbook uses evidence-based approaches:",
        "  - Cognitive Processing Therapy (CPT)",
        "  - Grounding techniques", "  - Safety planning",
        "  - Post-traumatic growth framework"]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Trauma Response Identification
    doc.new_page()
    doc.add_centered_text(750, "TRAUMA RESPONSE IDENTIFICATION", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    responses = [
        ("FIGHT", "Anger, irritability, controlling, rigid boundaries, perfectionism"),
        ("FLIGHT", "Anxiety, overthinking, workaholic, busy-ness, can't sit still"),
        ("FREEZE", "Dissociation, numbness, can't make decisions, zoning out, isolation"),
        ("FAWN", "People-pleasing, no boundaries, codependency, losing yourself"),
    ]
    for name, desc in responses:
        doc.add_text(72, y, name, 'F2', 11)
        y -= 16
        doc.add_text(90, y, desc, 'F1', 9)
        y -= 14
        doc.add_text(90, y, "I relate to this: [ ] Strongly [ ] Somewhat [ ] Not much", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "How it shows up for me: ________________________________", 'F1', 9)
        y -= 25
    doc.add_text(72, y, "My PRIMARY response: ________________", 'F2', 10)
    y -= 18
    doc.add_text(72, y, "My SECONDARY response: ________________", 'F2', 10)


    # Safety Plan
    doc.new_page()
    doc.add_centered_text(750, "COMPREHENSIVE SAFETY PLAN", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    plan = ["Warning signs I'm being triggered:", "________________________________",
        "________________________________", "",
        "Internal coping strategies (things I can do alone):",
        "1. ________________________________", "2. ________________________________",
        "3. ________________________________", "",
        "People/places that provide distraction:",
        "1. ______________ Phone: ______________",
        "2. ______________ Phone: ______________", "",
        "People I can ask for help:",
        "1. ______________ Phone: ______________",
        "2. ______________ Phone: ______________", "",
        "Professional resources:",
        "Therapist: ______________ Phone: ______________",
        "Crisis line: 988  |  Crisis text: Text HOME to 741741", "",
        "Making my environment safe:",
        "________________________________"]
    for line in plan:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 16

    # Grounding Techniques (15 techniques - 2 pages)
    techniques = [
        "1. 5-4-3-2-1: Name 5 see, 4 touch, 3 hear, 2 smell, 1 taste",
        "2. Cold water on face/wrists - activates dive reflex",
        "3. Name items in the room by color",
        "4. Press feet firmly into floor - feel the ground",
        "5. Hold ice cubes until they melt",
        "6. Describe your surroundings out loud in detail",
        "7. Count backward from 100 by 7s",
        "8. Name state capitals or categories (animals A-Z)",
        "9. Touch different textures - describe each one",
        "10. Smell something strong (peppermint, coffee, citrus)",
        "11. Splash cold water on face",
        "12. Clench and release fists 5 times",
        "13. Orienting: look around room slowly, name what's here",
        "14. Butterfly hug (cross arms, tap alternating shoulders)",
        "15. Say your name, age, date, location out loud",
    ]
    doc.new_page()
    doc.add_centered_text(750, "GROUNDING TECHNIQUES LIBRARY", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    for t in techniques:
        doc.add_text(72, y, t, 'F1', 9)
        y -= 16
    y -= 10
    doc.add_text(72, y, "My top 3 grounding techniques:", 'F2', 10)
    y -= 16
    for i in range(1, 4):
        doc.add_text(90, y, f"{i}. ________________________________", 'F1', 10)
        y -= 16

    doc.new_page()
    doc.add_centered_text(750, "GROUNDING PRACTICE LOG", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 715
    for _ in range(10):
        doc.add_text(72, y, "Date: ___  Trigger: ________________  Distress before: ___/10", 'F1', 9)
        y -= 14
        doc.add_text(72, y, "Technique used: ________________  Distress after: ___/10", 'F1', 9)
        y -= 14
        doc.add_text(72, y, "Time to calm: ___ min  Notes: ________________", 'F1', 9)
        y -= 22

    # Stuck Points (5 pages)
    for pg in range(1, 6):
        doc.new_page()
        doc.add_centered_text(755, f"STUCK POINTS WORKSHEET - PAGE {pg}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        doc.add_text(72, y, "Stuck points are thoughts that keep you stuck in pain.", 'F4', 10)
        y -= 20
        for s in range(1, 5):
            doc.add_text(72, y, f"Stuck Point {(pg-1)*4+s}:", 'F2', 9)
            y -= 14
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
            doc.add_text(72, y, "Category: [ ] Safety [ ] Trust [ ] Power [ ] Esteem [ ] Intimacy", 'F1', 8)
            y -= 14
            doc.add_text(72, y, "Evidence FOR this belief: ________________________________", 'F1', 8)
            y -= 14
            doc.add_text(72, y, "Evidence AGAINST: ________________________________", 'F1', 8)
            y -= 14
            doc.add_text(72, y, "Balanced thought: ________________________________", 'F1', 8)
            y -= 25

    # CPT Worksheets (5 pages)
    for pg in range(1, 6):
        doc.new_page()
        doc.add_centered_text(755, f"COGNITIVE PROCESSING WORKSHEET {pg}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        doc.add_text(72, y, "Situation/Trigger:", 'F2', 9)
        doc.add_line(170, y-2, 540, y-2, 0.5, 0.4)
        y -= 22
        doc.add_text(72, y, "Automatic thought:", 'F1', 9)
        doc.add_line(170, y-2, 540, y-2, 0.5, 0.4)
        y -= 22
        doc.add_text(72, y, "Emotion & intensity (0-100): ________________________________", 'F1', 9)
        y -= 22
        doc.add_text(72, y, "CHALLENGING QUESTIONS:", 'F2', 9)
        y -= 16
        questions = ["Is this based on facts or feelings?",
            "Am I confusing a thought with a fact?",
            "What would I tell a friend thinking this?",
            "Am I thinking in all-or-nothing terms?",
            "Am I blaming myself for something not in my control?",
            "What is the evidence this is true?",
            "What is the evidence this is NOT true?"]
        for q in questions:
            doc.add_text(90, y, q, 'F1', 8)
            y -= 12
            doc.add_line(90, y, 540, y, 0.5, 0.5)
            y -= 14
        y -= 10
        doc.add_text(72, y, "New balanced thought:", 'F2', 9)
        doc.add_line(72, y-14, 540, y-14, 0.5, 0.4)
        y -= 30
        doc.add_text(72, y, "New emotion & intensity: ________________________________", 'F1', 9)


    # ABC Worksheets (5 pages)
    for pg in range(1, 6):
        doc.new_page()
        doc.add_centered_text(755, f"ABC WORKSHEET {pg}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        for entry in range(1, 4):
            doc.add_text(72, y, f"Entry {entry}:", 'F2', 9)
            y -= 16
            doc.add_text(72, y, "A (Activating event): ________________________________", 'F1', 9)
            y -= 14
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
            doc.add_text(72, y, "B (Belief/Stuck point): ________________________________", 'F1', 9)
            y -= 14
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 16
            doc.add_text(72, y, "C (Consequence - emotion/behavior): ________________________________", 'F1', 9)
            y -= 14
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 25

    # Post-Traumatic Growth + Meaning
    doc.new_page()
    doc.add_centered_text(750, "POST-TRAUMATIC GROWTH INVENTORY", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "Growth doesn't mean the trauma was good. It means YOU are resilient.", 'F4', 10)
    y -= 22
    areas = [
        "New possibilities I see that I didn't before:",
        "How my relationships have deepened:",
        "Strength I didn't know I had:",
        "Greater appreciation for life:",
        "Spiritual/existential growth:",
    ]
    for area in areas:
        doc.add_text(72, y, area, 'F2', 9)
        y -= 14
        doc.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 14
        doc.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 22

    # Reclaiming 5 areas (5 pages)
    reclaim = [
        ("RECLAIMING SAFETY", ["I feel safe when:", "I feel unsafe when:",
            "Steps I'm taking to build safety:", "My safe place (real or imagined):",
            "People who help me feel safe:", "Safety affirmation:"]),
        ("RECLAIMING TRUST", ["People I trust:", "How I know someone is trustworthy:",
            "How trauma affected my trust:", "Small trust experiments I can try:",
            "Trust I'm rebuilding with myself:", "Trust affirmation:"]),
        ("RECLAIMING POWER/CONTROL", ["Areas where I have control:",
            "Ways I exercise healthy power:", "How trauma made me feel powerless:",
            "Empowering actions I take daily:", "Boundaries that give me power:",
            "Power affirmation:"]),
        ("RECLAIMING ESTEEM", ["Things I like about myself:", "Compliments I believe:",
            "How trauma affected my self-worth:", "Evidence I am worthy:",
            "My strengths:", "Esteem affirmation:"]),
        ("RECLAIMING INTIMACY", ["What intimacy means to me:",
            "How trauma affected closeness:", "Safe ways to be vulnerable:",
            "Boundaries I need in intimate relationships:",
            "Steps toward connection:", "Intimacy affirmation:"]),
    ]
    for title, prompts in reclaim:
        doc.new_page()
        doc.add_centered_text(750, title, 'F2', 14)
        doc.add_line(72, 738, 540, 738, 0.5, 0.3)
        y = 710
        for prompt in prompts:
            doc.add_text(72, y, prompt, 'F1', 10)
            y -= 16
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 14
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 22

    # Weekly Symptom Tracker (8 pages)
    for wk in range(1, 9):
        doc.new_page()
        doc.add_centered_text(755, f"WEEKLY SYMPTOM TRACKER - WEEK {wk}", 'F2', 12)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        for day in days:
            doc.add_text(72, y, day, 'F2', 8)
            y -= 13
            doc.add_text(90, y, "Flashbacks:___ Nightmares:___ Avoidance:___ Hypervigilance:___", 'F1', 7)
            y -= 11
            doc.add_text(90, y, "Mood(1-10):___ Sleep(hrs):___ Trigger:_______________", 'F1', 7)
            y -= 15
        y -= 5
        doc.add_text(72, y, "Skills used: ________________________________", 'F1', 9)
        y -= 14
        doc.add_text(72, y, "Overall progress this week: ________________________________", 'F1', 9)

    # Maintenance + Resources
    doc.new_page()
    doc.add_centered_text(750, "MAINTENANCE & PROFESSIONAL RESOURCES", 'F2', 13)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = ["RELAPSE PREVENTION:", "  Warning signs that I'm slipping:",
        "  ________________________________", "  ________________________________",
        "  My maintenance plan:", "  ________________________________",
        "  ________________________________", "",
        "  Triggers to continue managing:", "  ________________________________", "",
        "PROFESSIONAL RESOURCES:",
        "  Therapist: ______________ Specialty: ______________",
        "  Psychiatrist: ______________ Phone: ______________",
        "  Support group: ______________ When: ______________",
        "  Crisis line: 988", "  Veterans Crisis Line: 988 press 1",
        "  Crisis Text: HOME to 741741", "",
        "MY RECOVERY DECLARATION:",
        "  ________________________________",
        "  ________________________________"]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 16

    doc.save("Book227_PTSD_Recovery_Complete.pdf")
    print("Created: Book227_PTSD_Recovery_Complete.pdf")

if __name__ == "__main__":
    create_book()
