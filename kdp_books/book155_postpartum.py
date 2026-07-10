"""Book 155: The Fourth Trimester - A Postpartum Wellness Journal for New Moms"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    doc.new_page()
    doc.add_filled_rect(0, 0, 432, 648, 0.95)
    doc.add_centered_text(430, "THE FOURTH TRIMESTER", 'F2', 20, 0)
    doc.add_centered_text(395, "A Postpartum Wellness Journal", 'F4', 14, 0.2)
    doc.add_centered_text(370, "for New Moms", 'F4', 14, 0.2)
    doc.add_centered_text(300, "You are doing amazing.", 'F4', 12, 0.3)
    doc.add_centered_text(280, "Even on the hard days.", 'F4', 12, 0.3)
    doc.add_centered_text(260, "Especially on the hard days.", 'F4', 12, 0.3)
    doc.add_centered_text(100, author, 'F2', 14, 0)

    doc.new_page()
    doc.add_centered_text(500, "THE FOURTH TRIMESTER", 'F2', 14, 0)
    doc.add_text(50, 430, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 9, 0.3)
    doc.add_text(50, 410, "If you are in crisis: PSI Helpline 1-800-944-4773", 'F2', 9, 0.3)
    doc.add_text(50, 390, "Text HOME to 741741 | In emergency call 911", 'F1', 9, 0.3)

    # Page 3: What to Expect
    doc.new_page()
    doc.add_centered_text(590, "WHAT TO EXPECT IN THE 4TH TRIMESTER", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "The first 12 weeks after birth are a massive transition. You may feel:", 'F1', 10, 0.2)
    y = 530
    feelings = ["Overwhelming love AND overwhelm", "Joy AND grief for your old life",
                "Touched out AND lonely", "Grateful AND resentful",
                "Like a superhero AND like you're failing",
                "Bonded AND disconnected", "All of these in one hour"]
    for f in feelings:
        doc.add_text(60, y, f"- {f}", 'F1', 9, 0.2)
        y -= 14
    y -= 15
    doc.add_text(50, y, "ALL of this is normal. You are not failing. You are BECOMING.", 'F2', 9, 0)
    y -= 20
    doc.add_text(50, y, "Baby's name: ______________________  Born: ___________", 'F1', 10, 0.2)
    y -= 18
    doc.add_text(50, y, "Birth story (in one line): _________________________________________", 'F1', 10, 0.2)

    # Page 4: Postpartum Mood Check
    doc.new_page()
    doc.add_centered_text(590, "POSTPARTUM MOOD CHECK", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    doc.add_text(50, 555, "Edinburgh Postnatal Depression Scale (self-screen):", 'F2', 9, 0)
    doc.add_text(50, 538, "In the past 7 days... (0=not at all, 3=most of the time)", 'F1', 9, 0.3)
    y = 515
    questions = ["I have been able to laugh and see the funny side",
                 "I have looked forward to things with enjoyment",
                 "I have blamed myself unnecessarily when things went wrong",
                 "I have been anxious or worried for no good reason",
                 "I have felt scared or panicky for no good reason",
                 "Things have been getting on top of me",
                 "I have been so unhappy that I have difficulty sleeping",
                 "I have felt sad or miserable",
                 "I have been so unhappy that I have been crying",
                 "The thought of harming myself has occurred to me"]
    for i, q in enumerate(questions):
        doc.add_text(50, y, f"{i+1}. {q}", 'F1', 8, 0.2)
        doc.add_text(340, y, "0  1  2  3", 'F1', 8, 0.3)
        y -= 14
    y -= 10
    doc.add_text(50, y, "Score: ___  (10+ = talk to your provider. 13+ = seek help now)", 'F2', 9, 0)
    y -= 14
    doc.add_text(50, y, "This is NOT diagnosis. It's a prompt to seek support if needed.", 'F1', 8, 0.3)

    # Pages 5-34: Daily Entries (30 pages, 2 per page = 60 entries)
    for page_num in range(30):
        doc.new_page()
        doc.add_text(50, 612, f"DAILY JOURNAL - Page {page_num+1}", 'F2', 8, 0.3)
        doc.add_line(50, 606, 382, 606, 0.5, 0.7)
        y = 594
        for entry in range(2):
            day_num = page_num * 2 + entry + 1
            doc.add_filled_rect(50, y+2, 332, 10, 0.9)
            doc.add_text(52, y+3, f"Day {day_num}  Date: ________", 'F2', 6, 0)
            y -= 12
            doc.add_text(50, y, "Hours slept (total, inc naps): ___  Mood (1-10): ___", 'F1', 7, 0.2)
            y -= 11
            doc.add_text(50, y, "Baby feeding: [ ]Breast [ ]Bottle [ ]Both  Approx feeds: ___", 'F1', 7, 0.2)
            y -= 11
            doc.add_text(50, y, "My meals today: B________ L________ D________ Snacks: ___", 'F1', 7, 0.2)
            y -= 11
            doc.add_text(50, y, "One thing I did for MYSELF: ____________________________________", 'F1', 7, 0.2)
            y -= 11
            doc.add_text(50, y, "Help I accepted today: __________________________________________", 'F1', 7, 0.2)
            y -= 11
            doc.add_text(50, y, "Worry I'm carrying: ____________________________________________", 'F1', 7, 0.2)
            y -= 11
            doc.add_text(50, y, "One beautiful moment: ___________________________________________", 'F1', 7, 0.2)
            y -= 18

    # Page 35: Postpartum Body Healing
    doc.new_page()
    doc.add_centered_text(590, "POSTPARTUM BODY HEALING TIMELINE", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    timeline = [
        ("Week 1-2:", "Bleeding (lochia), cramping, breast engorgement, exhaustion"),
        ("Week 3-4:", "Bleeding tapering, stitches healing, emotions stabilizing (or not)"),
        ("Week 5-6:", "6-week checkup, cleared for exercise (gentle!), may still be tired"),
        ("Month 2-3:", "Hormone shifts, hair may start falling out (normal!), finding rhythm"),
        ("Month 4-6:", "Body still recovering. Give yourself GRACE. 9 months on, 9+ months off.")
    ]
    for time, desc in timeline:
        doc.add_text(50, y, time, 'F2', 9, 0)
        y -= 14
        doc.add_text(55, y, desc, 'F1', 8, 0.3)
        y -= 20
    y -= 10
    doc.add_text(50, y, "Remember: Your body grew a human. It deserves patience, not punishment.", 'F2', 8, 0)

    # Page 36: Breastfeeding Support
    doc.new_page()
    doc.add_centered_text(590, "BREASTFEEDING SUPPORT RESOURCES", 'F2', 12, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Whether you breastfeed, pump, formula feed, or combo - you're a", 'F1', 9, 0.2)
    doc.add_text(50, y-14, "good mom. Fed is best. YOUR mental health matters too.", 'F2', 9, 0)
    y -= 35
    doc.add_text(50, y, "My lactation consultant: ________________________  Phone: __________", 'F1', 9, 0.2)
    y -= 18
    doc.add_text(50, y, "La Leche League: llli.org", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "KellyMom: kellymom.com (evidence-based BF info)", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Breastfeeding hotline: 1-800-994-9662", 'F1', 9, 0.2)
    y -= 20
    doc.add_text(50, y, "Challenges I'm having: _____________________________________________", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "___________________________________________________________________", 'F1', 9, 0.4)
    y -= 18
    doc.add_text(50, y, "Permission slip: It's okay to stop. It's okay to supplement.", 'F2', 9, 0)
    y -= 14
    doc.add_text(50, y, "Your value as a mother is NOT measured in ounces.", 'F2', 9, 0)

    # Page 37: Asking for Help Scripts
    doc.new_page()
    doc.add_centered_text(590, "ASKING FOR HELP: 5 SCRIPTS", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    scripts = [
        ("To a partner:", "'I need you to take the baby for ___ hours so I can ___.'"),
        ("To family:", "'Could you come over Tuesday? I need help with ___ / just company.'"),
        ("To a friend:", "'I'm struggling today. Can you [bring food/visit/just listen]?'"),
        ("To a professional:", "'I don't feel like myself. I think I need support.'"),
        ("To yourself:", "'I am allowed to need help. Asking doesn't make me weak.'")
    ]
    for to, script in scripts:
        doc.add_text(50, y, to, 'F2', 9, 0)
        y -= 14
        doc.add_text(55, y, script, 'F4', 9, 0.3)
        y -= 22
    y -= 15
    doc.add_text(50, y, "Accepting help is NOT failure. It takes a village.", 'F2', 9, 0)
    y -= 16
    doc.add_text(50, y, "You don't get extra points for doing it alone.", 'F4', 9, 0.3)

    # Page 38: Partner Communication
    doc.new_page()
    doc.add_centered_text(590, "PARTNER COMMUNICATION", 'F2', 14, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "What I need from my partner right now:", 'F2', 10, 0)
    y -= 18
    for i in range(4):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14
    y -= 10
    doc.add_text(50, y, "What I appreciate about my partner:", 'F2', 10, 0)
    y -= 18
    for i in range(3):
        doc.add_text(50, y, "_" * 52, 'F1', 9, 0.4)
        y -= 14
    y -= 10
    doc.add_text(50, y, "Division of labor that works for us:", 'F2', 10, 0)
    y -= 16
    doc.add_text(50, y, "Night feeds: ______________________", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Diaper duty: ______________________", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Household: ________________________", 'F1', 9, 0.2)
    y -= 14
    doc.add_text(50, y, "Emotional support: _________________", 'F1', 9, 0.2)

    # Page 39: When to Call Doctor + My Village
    doc.new_page()
    doc.add_centered_text(590, "WHEN TO CALL YOUR DOCTOR", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    doc.add_text(50, y, "Warning signs (call immediately):", 'F2', 9, 0)
    y -= 16
    warnings = ["Fever over 100.4F", "Heavy bleeding (soaking pad in 1 hr)",
                "Foul-smelling discharge", "Severe headache or vision changes",
                "Pain/redness in legs (blood clot)", "Thoughts of harming yourself or baby",
                "Chest pain or difficulty breathing", "Unable to care for yourself or baby"]
    for w in warnings:
        doc.add_text(55, y, f"- {w}", 'F1', 8, 0.2)
        y -= 12
    y -= 12
    doc.add_text(50, y, "MY VILLAGE (who helps with what):", 'F2', 10, 0)
    y -= 16
    village = ["Meals:", "Cleaning:", "Older kids:", "Errands:", "Emotional support:", "Night help:"]
    for v in village:
        doc.add_text(50, y, f"  {v} ___________________________________________________", 'F1', 8, 0.3)
        y -= 14

    # Page 40: 6-Week Recovery + Affirmation
    doc.new_page()
    doc.add_centered_text(590, "6-WEEK RECOVERY MILESTONES", 'F2', 13, 0)
    doc.add_line(50, 580, 382, 580, 1, 0.5)
    y = 555
    milestones = ["Survived the first night home", "Baby regained birth weight",
                  "Went outside (even to mailbox)", "Took a shower without rushing",
                  "Slept 3+ hours in a row", "Asked for and accepted help",
                  "Had a moment of pure joy", "Made it to 6-week checkup",
                  "Went somewhere alone (without baby)", "Laughed a real laugh"]
    for m in milestones:
        doc.add_rect(50, y-3, 8, 8)
        doc.add_text(62, y, m, 'F1', 9, 0.2)
        y -= 16
    y -= 20
    doc.add_filled_rect(50, y-5, 332, 60, 0.92)
    doc.add_centered_text(y+35, "YOU ARE DOING AMAZING", 'F2', 14, 0)
    doc.add_centered_text(y+15, "The fact that you worry about being a good mom", 'F4', 9, 0.2)
    doc.add_centered_text(y, "means you already ARE one.", 'F4', 9, 0.2)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book155_Postpartum_Wellness_Journal.pdf')
    print("Book155_Postpartum_Wellness_Journal.pdf created successfully!")

if __name__ == "__main__":
    create_book()
