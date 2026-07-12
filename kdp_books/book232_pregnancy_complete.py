"""Book 232: The Complete Pregnancy Journal"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(432, 648)  # 6x9
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 560, 432, 88, 0.2)
    doc.add_centered_text(605, "THE COMPLETE", 'F2', 20, 1)
    doc.add_centered_text(578, "PREGNANCY JOURNAL", 'F2', 20, 1)
    doc.add_centered_text(525, "Week by Week from Positive Test to Birth", 'F4', 11, 0.3)
    doc.add_centered_text(150, author, 'F2', 12, 0.3)

    doc.new_page()
    doc.add_centered_text(560, "THE COMPLETE PREGNANCY JOURNAL", 'F2', 11)
    doc.add_centered_text(535, f"Copyright {author}. All rights reserved.", 'F1', 9)

    # Finding Out Page
    doc.new_page()
    doc.add_centered_text(610, "MY PREGNANCY STORY BEGINS", 'F2', 13)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    prompts = ["Date I found out: ___/___/___",
        "How I found out: ________________________________",
        "My first reaction: ________________________________",
        "Who I told first: ________________________________",
        "Their reaction: ________________________________",
        "Due date: ___/___/___",
        "OB/Midwife: ________________________________",
        "Hospital/Birth center: ________________________________", "",
        "How I feel about becoming a parent:", "________________________________",
        "________________________________", "",
        "My hopes for this pregnancy:", "________________________________",
        "________________________________"]
    for p in prompts:
        doc.add_text(50, y, p, 'F1', 9)
        y -= 14

    # 40 Weekly Pages
    sizes = ["poppy seed", "sesame seed", "lentil", "blueberry", "raspberry",
             "cherry", "olive", "prune", "lime", "plum", "peach", "lemon",
             "navel orange", "apple", "avocado", "turnip", "bell pepper",
             "mango", "banana", "artichoke", "papaya", "spaghetti squash",
             "ear of corn", "cantaloupe", "cauliflower", "lettuce head",
             "zucchini", "eggplant", "butternut squash", "coconut",
             "pineapple", "honeydew", "celery bunch", "napa cabbage",
             "winter melon", "romaine lettuce", "swiss chard", "leek",
             "small pumpkin", "watermelon"]
    
    for week in range(1, 41):
        doc.new_page()
        size = sizes[week-1] if week <= len(sizes) else "baby!"
        doc.add_text(50, 615, f"WEEK {week}", 'F2', 12)
        doc.add_text(180, 615, f"Baby is the size of a {size}", 'F4', 9)
        doc.add_line(50, 605, 382, 605, 0.5, 0.3)
        y = 585
        doc.add_text(50, y, f"How far along: {week} weeks  Trimester: {'1st' if week<=13 else '2nd' if week<=26 else '3rd'}", 'F1', 8)
        y -= 14
        doc.add_text(50, y, "How I feel physically: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(50, y, "How I feel emotionally: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(50, y, "Cravings: ________________ Aversions: ________________", 'F1', 8)
        y -= 12
        doc.add_text(50, y, "Symptoms: ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(50, y, "Weight: ______  Blood pressure: ______", 'F1', 8)
        y -= 14
        doc.add_text(50, y, "Doctor visit notes:", 'F1', 8)
        y -= 12
        doc.add_line(50, y, 382, y, 0.5, 0.5)
        y -= 12
        doc.add_line(50, y, 382, y, 0.5, 0.5)
        y -= 14
        doc.add_text(50, y, "Questions for next appointment:", 'F1', 8)
        y -= 12
        doc.add_line(50, y, 382, y, 0.5, 0.5)
        y -= 14
        doc.add_text(50, y, "[ ] Bump photo taken", 'F1', 8)
        y -= 14
        doc.add_text(50, y, "Letter to baby:", 'F1', 8)
        y -= 12
        doc.add_line(50, y, 382, y, 0.5, 0.5)
        y -= 12
        doc.add_line(50, y, 382, y, 0.5, 0.5)
        y -= 12
        doc.add_line(50, y, 382, y, 0.5, 0.5)


    # Birth Preferences (2 pages)
    doc.new_page()
    doc.add_centered_text(610, "BIRTH PREFERENCES - PAGE 1", 'F2', 12)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    doc.add_text(50, 578, "(Not a rigid plan - a communication tool for your team)", 'F4', 9)
    y = 558
    prefs = ["Birth location: [ ] Hospital [ ] Birth center [ ] Home",
        "Provider: ________________________________",
        "Support people present: ________________________________", "",
        "LABOR PREFERENCES:",
        "[ ] Freedom to move and change positions",
        "[ ] Intermittent monitoring (not continuous)",
        "[ ] Dim lights and quiet environment",
        "[ ] Music/playlist prepared",
        "[ ] Hydrotherapy (tub/shower)",
        "[ ] Delayed epidural / pain med preferences: ___________",
        "[ ] Prefer to avoid induction unless medically necessary"]
    for p in prefs:
        doc.add_text(50, y, p, 'F1', 8)
        y -= 13

    doc.new_page()
    doc.add_centered_text(610, "BIRTH PREFERENCES - PAGE 2", 'F2', 12)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 578
    prefs2 = ["DELIVERY PREFERENCES:",
        "[ ] Delayed cord clamping", "[ ] Skin-to-skin immediately",
        "[ ] Partner to cut cord", "[ ] Gentle C-section preferences (if needed)",
        "[ ] Golden hour uninterrupted", "",
        "NEWBORN PREFERENCES:",
        "[ ] Breastfeeding within first hour",
        "[ ] Delay routine procedures for bonding",
        "[ ] Rooming in (baby stays with me)",
        "[ ] Vitamin K: [ ] Yes [ ] Discuss",
        "[ ] Eye ointment: [ ] Yes [ ] Discuss", "",
        "IF PLANS CHANGE:", "My priorities no matter what: ________________________________",
        "I trust my team to: ________________________________"]
    for p in prefs2:
        doc.add_text(50, y, p, 'F1', 8)
        y -= 13

    # Hospital Bag Checklist
    doc.new_page()
    doc.add_centered_text(610, "HOSPITAL BAG CHECKLIST", 'F2', 12)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    doc.add_text(50, y, "FOR ME:", 'F2', 9)
    y -= 13
    me_items = ["[ ] ID & insurance card", "[ ] Birth preferences (3 copies)",
        "[ ] Robe & slippers", "[ ] Going-home outfit (maternity size)",
        "[ ] Toiletries", "[ ] Phone charger (long cord)",
        "[ ] Pillow from home", "[ ] Snacks & drinks", "[ ] Nursing bra & pads"]
    for item in me_items:
        doc.add_text(60, y, item, 'F1', 8)
        y -= 11
    y -= 8
    doc.add_text(50, y, "FOR BABY:", 'F2', 9)
    y -= 13
    baby_items = ["[ ] Going-home outfit (newborn + 0-3 size)", "[ ] Car seat (installed!)",
        "[ ] Blanket", "[ ] Diapers & wipes", "[ ] Hat & socks"]
    for item in baby_items:
        doc.add_text(60, y, item, 'F1', 8)
        y -= 11
    y -= 8
    doc.add_text(50, y, "FOR PARTNER:", 'F2', 9)
    y -= 13
    partner = ["[ ] Change of clothes", "[ ] Snacks", "[ ] Phone charger", "[ ] Pillow"]
    for item in partner:
        doc.add_text(60, y, item, 'F1', 8)
        y -= 11

    # Baby Names + Nursery + Shower + Postpartum
    doc.new_page()
    doc.add_centered_text(610, "BABY NAME BRAINSTORM", 'F2', 12)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    doc.add_text(50, y, "Girl names:", 'F2', 9)
    y -= 14
    for _ in range(5):
        doc.add_text(60, y, "_________________ Meaning: _________________", 'F1', 8)
        y -= 12
    y -= 8
    doc.add_text(50, y, "Boy names:", 'F2', 9)
    y -= 14
    for _ in range(5):
        doc.add_text(60, y, "_________________ Meaning: _________________", 'F1', 8)
        y -= 12
    y -= 8
    doc.add_text(50, y, "Gender neutral:", 'F2', 9)
    y -= 14
    for _ in range(3):
        doc.add_text(60, y, "_________________ Meaning: _________________", 'F1', 8)
        y -= 12
    y -= 8
    doc.add_text(50, y, "OUR CHOICE: ________________________________", 'F2', 9)

    doc.new_page()
    doc.add_centered_text(610, "NURSERY & POSTPARTUM PREP", 'F2', 12)
    doc.add_line(50, 598, 382, 598, 0.5, 0.3)
    y = 575
    doc.add_text(50, y, "NURSERY PLANNING:", 'F2', 9)
    y -= 14
    nursery = ["Theme/colors: ________________________________",
        "[ ] Crib/bassinet", "[ ] Changing area", "[ ] Rocker/glider",
        "[ ] Storage/dresser", "[ ] Blackout curtains", "[ ] Sound machine"]
    for item in nursery:
        doc.add_text(60, y, item, 'F1', 8)
        y -= 12
    y -= 10
    doc.add_text(50, y, "SHOWER PLANNING:", 'F2', 9)
    y -= 14
    doc.add_text(60, y, "Date: ___  Host: ___________  Location: ___________", 'F1', 8)
    y -= 12
    doc.add_text(60, y, "Registry: ________________________________", 'F1', 8)
    y -= 16
    doc.add_text(50, y, "POSTPARTUM PREP:", 'F2', 9)
    y -= 14
    post = ["[ ] Meal prep/delivery plan", "[ ] Help scheduled (who + when)",
        "[ ] Pediatrician chosen", "[ ] Lactation consultant on file",
        "[ ] Postpartum supplies (pads, spray, etc)", "[ ] Mental health plan"]
    for item in post:
        doc.add_text(60, y, item, 'F1', 8)
        y -= 12

    doc.save("Book232_Pregnancy_Complete_Journal.pdf")
    print("Created: Book232_Pregnancy_Complete_Journal.pdf")

if __name__ == "__main__":
    create_book()
