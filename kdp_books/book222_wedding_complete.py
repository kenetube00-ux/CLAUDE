"""Book 222: The Complete Wedding Planner"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.2)
    doc.add_centered_text(755, "THE COMPLETE", 'F2', 24, 1)
    doc.add_centered_text(722, "WEDDING PLANNER", 'F2', 24, 1)
    doc.add_centered_text(660, "From Engagement to Honeymoon", 'F4', 16, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    # Copyright
    doc.new_page()
    doc.add_centered_text(700, "THE COMPLETE WEDDING PLANNER", 'F2', 14)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # Our Engagement Story
    doc.new_page()
    doc.add_centered_text(750, "OUR ENGAGEMENT STORY", 'F2', 16)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    prompts = ["Date of engagement: ___/___/___", "Location: ________________________________",
        "How it happened:", "________________________________", "________________________________",
        "________________________________", "", "How I felt:", "________________________________",
        "First person we told: ________________________________",
        "Engagement photo location: ________________________________", "",
        "Wedding date chosen: ___/___/___",
        "Venue: ________________________________",
        "Theme/colors: ________________________________",
        "Guest count (estimated): ___",
        "Budget: $________________"]
    for p in prompts:
        doc.add_text(72, y, p, 'F1', 10)
        y -= 20


    # 12-month countdown checklist (2 pages)
    countdown = [
        ("12 MONTHS", ["[ ] Set budget", "[ ] Book venue", "[ ] Choose wedding party", "[ ] Start guest list", "[ ] Book photographer"]),
        ("10 MONTHS", ["[ ] Book caterer", "[ ] Book DJ/band", "[ ] Shop for dress", "[ ] Choose officiant", "[ ] Book florist"]),
        ("8 MONTHS", ["[ ] Send save-the-dates", "[ ] Book videographer", "[ ] Plan honeymoon", "[ ] Register for gifts", "[ ] Book hotel block"]),
        ("6 MONTHS", ["[ ] Order invitations", "[ ] Book cake baker", "[ ] Plan ceremony", "[ ] Arrange transportation", "[ ] Buy wedding bands"]),
        ("4 MONTHS", ["[ ] Mail invitations", "[ ] Final dress fitting", "[ ] Plan rehearsal dinner", "[ ] Write vows", "[ ] Book hair/makeup"]),
        ("2 MONTHS", ["[ ] Final guest count", "[ ] Seating chart", "[ ] Confirm all vendors", "[ ] Get marriage license", "[ ] Plan day-of timeline"]),
        ("1 MONTH", ["[ ] Final fittings", "[ ] Break in shoes", "[ ] Confirm honeymoon", "[ ] Prepare payments", "[ ] Pack emergency kit"]),
        ("1 WEEK", ["[ ] Rehearsal dinner", "[ ] Give timeline to party", "[ ] Confirm rides", "[ ] Pack for honeymoon", "[ ] Relax and enjoy!"]),
    ]
    for pg in range(2):
        doc.new_page()
        doc.add_centered_text(755, "WEDDING COUNTDOWN CHECKLIST", 'F2', 14)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        items = countdown[pg*4:(pg+1)*4]
        for period, tasks in items:
            doc.add_text(72, y, period, 'F2', 11)
            y -= 16
            for task in tasks:
                doc.add_text(90, y, task, 'F1', 9)
                y -= 14
            y -= 15

    # Master Budget (2 pages)
    budget_cats = [
        ("Venue/Rentals", "$_____"), ("Catering/Bar", "$_____"), ("Photography", "$_____"),
        ("Videography", "$_____"), ("Florist/Decor", "$_____"), ("DJ/Music", "$_____"),
        ("Wedding Dress", "$_____"), ("Groom Attire", "$_____"), ("Cake/Desserts", "$_____"),
        ("Invitations/Paper", "$_____"), ("Officiant", "$_____"), ("Hair/Makeup", "$_____"),
        ("Transportation", "$_____"), ("Favors", "$_____"), ("Gifts (party)", "$_____"),
        ("Rings", "$_____"), ("Rehearsal Dinner", "$_____"), ("Honeymoon", "$_____"),
        ("Marriage License", "$_____"), ("Tips/Gratuities", "$_____"),
        ("Alterations", "$_____"), ("Hotel Block", "$_____"),
        ("Welcome Bags", "$_____"), ("Day-of Coordinator", "$_____"),
        ("Contingency (10%)", "$_____"),
    ]
    for pg in range(2):
        doc.new_page()
        doc.add_centered_text(755, f"MASTER BUDGET WORKSHEET - PAGE {pg+1}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        doc.add_text(72, y, "Category", 'F2', 9)
        doc.add_text(220, y, "Estimated", 'F2', 9)
        doc.add_text(300, y, "Actual", 'F2', 9)
        doc.add_text(375, y, "Deposit", 'F2', 9)
        doc.add_text(445, y, "Balance", 'F2', 9)
        doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
        items = budget_cats[pg*13:(pg+1)*13]
        for cat, _ in items:
            y -= 20
            doc.add_text(72, y, cat, 'F1', 9)
            doc.add_text(220, y, "$_______", 'F1', 9)
            doc.add_text(300, y, "$_______", 'F1', 9)
            doc.add_text(375, y, "$_______", 'F1', 9)
            doc.add_text(445, y, "$_______", 'F1', 9)
        if pg == 1:
            y -= 30
            doc.add_text(72, y, "TOTAL BUDGET: $________  TOTAL SPENT: $________  REMAINING: $________", 'F2', 10)


    # Venue Comparison
    doc.new_page()
    doc.add_centered_text(755, "VENUE COMPARISON WORKSHEET", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    for v in range(1, 6):
        doc.add_text(72, y, f"VENUE {v}: ________________________________", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Capacity: ___ Cost: $_____ Indoor/Outdoor: ___ Available: ___", 'F1', 8)
        y -= 14
        doc.add_text(90, y, "Pros: ____________________  Cons: ____________________", 'F1', 8)
        y -= 20

    # Vendor Comparison (8 vendors - 2 pages)
    vendors = ["Catering", "Photographer", "Videographer", "Florist", "DJ/Band", "Cake", "Dress Shop", "Rentals"]
    for pg in range(2):
        doc.new_page()
        doc.add_centered_text(755, "VENDOR COMPARISON", 'F2', 14)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        for v in vendors[pg*4:(pg+1)*4]:
            doc.add_text(72, y, f"{v.upper()}", 'F2', 10)
            y -= 16
            for opt in range(1, 4):
                doc.add_text(90, y, f"Option {opt}: ____________ Price: $_____ Rating: ___/5", 'F1', 8)
                y -= 13
            doc.add_text(90, y, "CHOSEN: ____________ Deposit paid: ___/___/___", 'F1', 8)
            y -= 22

    # Guest List Manager (4 pages for 250 guests)
    for pg in range(1, 5):
        doc.new_page()
        doc.add_centered_text(760, f"GUEST LIST - PAGE {pg}", 'F2', 13)
        doc.add_line(72, 748, 540, 748, 0.5, 0.3)
        y = 732
        doc.add_text(72, y, "#", 'F2', 7)
        doc.add_text(85, y, "Name", 'F2', 7)
        doc.add_text(195, y, "RSVP", 'F2', 7)
        doc.add_text(230, y, "Meal", 'F2', 7)
        doc.add_text(270, y, "Table", 'F2', 7)
        doc.add_text(305, y, "Gift", 'F2', 7)
        doc.add_text(370, y, "Thank You", 'F2', 7)
        doc.add_text(430, y, "Address", 'F2', 7)
        doc.add_line(72, y-4, 540, y-4, 0.5, 0.3)
        start = (pg-1)*63 + 1
        for i in range(start, min(start+30, 251)):
            y -= 14
            doc.add_text(72, y, f"{i}", 'F3', 7)
            doc.add_line(85, y-2, 540, y-2, 0.5, 0.6)

    # Seating Chart (2 pages)
    for pg in range(1, 3):
        doc.new_page()
        doc.add_centered_text(755, f"SEATING CHART - PAGE {pg}", 'F2', 14)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 720
        start_table = (pg-1)*8 + 1
        for t in range(start_table, start_table+8):
            doc.add_text(72, y, f"TABLE {t} (capacity: ___)", 'F2', 9)
            y -= 14
            doc.add_text(90, y, "Guests: ________________________________", 'F1', 8)
            y -= 12
            doc.add_text(90, y, "________________________________", 'F1', 8)
            y -= 18

    # Menu Selection
    doc.new_page()
    doc.add_centered_text(755, "MENU SELECTION WORKSHEET", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    courses = ["Appetizers", "Salad", "Entree Option 1", "Entree Option 2",
               "Entree Option 3 (vegetarian)", "Dessert", "Late Night Snack"]
    for c in courses:
        doc.add_text(72, y, f"{c}: ________________________________", 'F2', 10)
        y -= 20
    y -= 10
    doc.add_text(72, y, "Bar: [ ] Open  [ ] Limited  [ ] Cash  [ ] Wine & Beer Only", 'F1', 10)
    y -= 18
    doc.add_text(72, y, "Signature cocktail: ________________________________", 'F1', 10)
    y -= 18
    doc.add_text(72, y, "Dietary restrictions noted: ________________________________", 'F1', 10)


    # Day-of Timeline
    doc.new_page()
    doc.add_centered_text(755, "DAY-OF TIMELINE", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 720
    times = [("6:00 AM", "Wake up / breakfast"), ("7:00 AM", "Hair & makeup begins"),
        ("9:00 AM", "Photographer arrives"), ("10:00 AM", "Get dressed"),
        ("11:00 AM", "First look photos"), ("12:00 PM", "Bridal party photos"),
        ("1:00 PM", "Guests arrive"), ("1:30 PM", "Ceremony begins"),
        ("2:00 PM", "Ceremony ends / cocktail hour"), ("3:00 PM", "Reception begins"),
        ("3:30 PM", "First dance"), ("4:00 PM", "Dinner served"),
        ("5:00 PM", "Toasts & speeches"), ("5:30 PM", "Cake cutting"),
        ("6:00 PM", "Dancing / open floor"), ("8:00 PM", "Bouquet/garter toss"),
        ("9:00 PM", "Last dance"), ("9:30 PM", "Grand exit"),
        ("10:00 PM", "Vendor pack-up"), ("11:00 PM", "After party (optional)")]
    for time, activity in times:
        doc.add_text(72, y, f"{time}  {activity}: ________________________________", 'F1', 9)
        y -= 16

    # Wedding Party Info
    doc.new_page()
    doc.add_centered_text(755, "WEDDING PARTY INFORMATION", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    roles = ["Maid/Matron of Honor", "Bridesmaid 1", "Bridesmaid 2", "Bridesmaid 3",
             "Best Man", "Groomsman 1", "Groomsman 2", "Groomsman 3",
             "Flower Girl", "Ring Bearer"]
    for role in roles:
        doc.add_text(72, y, f"{role}: ______________ Phone: ______________", 'F1', 9)
        y -= 18

    # Ceremony Script Planning
    doc.new_page()
    doc.add_centered_text(755, "CEREMONY SCRIPT PLANNING", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 710
    elements = ["Processional music: ________________________________",
        "Welcome/Opening words: ________________________________",
        "Reading 1 (by ___): ________________________________",
        "Reading 2 (by ___): ________________________________",
        "Vows: [ ] Traditional [ ] Personal [ ] Mix",
        "Ring exchange words: ________________________________",
        "Unity ceremony: [ ] Candle [ ] Sand [ ] Wine [ ] None [ ] Other: ___",
        "Pronouncement: ________________________________",
        "First kiss!",
        "Recessional music: ________________________________",
        "Officiant: ________________ Phone: ________________"]
    for e in elements:
        doc.add_text(72, y, e, 'F1', 10)
        y -= 22

    # Vow Writing (2 pages)
    for partner in ["PARTNER 1", "PARTNER 2"]:
        doc.new_page()
        doc.add_centered_text(755, f"VOW WRITING - {partner}", 'F2', 14)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 710
        doc.add_text(72, y, "Prompts to inspire your vows:", 'F4', 10)
        y -= 20
        prompts = ["When I first knew I loved you:", "What I admire most about you:",
            "My promise to you:", "How you make me a better person:",
            "What our future looks like to me:"]
        for p in prompts:
            doc.add_text(72, y, p, 'F1', 9)
            y -= 14
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 14
            doc.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 20
        doc.add_text(72, y, "Final vows (write here):", 'F2', 10)
        y -= 15
        for _ in range(8):
            doc.add_line(72, y, 540, y, 0.5, 0.4)
            y -= 18

    # Reception Planning
    doc.new_page()
    doc.add_centered_text(755, "RECEPTION PLANNING", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 710
    items = ["First dance song: ________________________________",
        "Father-daughter song: ________________________________",
        "Mother-son song: ________________________________",
        "Must-play list: ________________________________",
        "Do-not-play list: ________________________________",
        "Toast order: 1.___ 2.___ 3.___ 4.___",
        "Special dances: ________________________________",
        "Photo booth: [ ] Yes [ ] No  Props: ________________________________",
        "Guest book alternative: ________________________________",
        "Centerpieces: ________________________________",
        "Table numbers/names: ________________________________"]
    for item in items:
        doc.add_text(72, y, item, 'F1', 10)
        y -= 22

    # Honeymoon (2 pages)
    for pg in range(1, 3):
        doc.new_page()
        doc.add_centered_text(755, f"HONEYMOON PLANNER - PAGE {pg}", 'F2', 14)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 710
        if pg == 1:
            items = ["Destination: ________________________________",
                "Dates: ___/___ to ___/___  Duration: ___ nights",
                "Flight info: ________________________________",
                "Hotel/Resort: ________________________________",
                "Confirmation #: ________________________________",
                "Budget: $________________",
                "Activities planned:", "________________________________",
                "________________________________", "________________________________",
                "Restaurants to try:", "________________________________",
                "Packing list:", "________________________________", "________________________________"]
        else:
            items = ["Travel documents needed:", "[ ] Passport (exp: ___/___/___)",
                "[ ] Visa", "[ ] Travel insurance", "[ ] Vaccination records",
                "[ ] Copies of all docs (digital + paper)", "",
                "Pet/house sitter: ________________ Phone: ___________",
                "Mail hold: ___/___ to ___/___",
                "Out-of-office set: [ ] Yes", "",
                "Post-honeymoon:", "Return flight: ________________________________",
                "Ride from airport: ________________________________"]
        for item in items:
            doc.add_text(72, y, item, 'F1', 10)
            y -= 20

    # Thank You Card Tracker (3 pages)
    for pg in range(1, 4):
        doc.new_page()
        doc.add_centered_text(755, f"THANK YOU CARD TRACKER - PAGE {pg}", 'F2', 13)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 725
        doc.add_text(72, y, "Name", 'F2', 8)
        doc.add_text(190, y, "Gift", 'F2', 8)
        doc.add_text(350, y, "Card Sent", 'F2', 8)
        doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
        for _ in range(25):
            y -= 16
            doc.add_line(72, y, 185, y, 0.5, 0.5)
            doc.add_line(190, y, 345, y, 0.5, 0.5)
            doc.add_line(350, y, 430, y, 0.5, 0.5)

    # Marriage License + Emergency Kit
    doc.new_page()
    doc.add_centered_text(755, "MARRIAGE LICENSE & EMERGENCY KIT", 'F2', 13)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    doc.add_text(72, y, "MARRIAGE LICENSE CHECKLIST:", 'F2', 10)
    y -= 16
    lic = ["[ ] Check county requirements", "[ ] Required documents: ________________________________",
        "[ ] Waiting period: ___ days", "[ ] Fee: $___",
        "[ ] Appointment date: ___/___/___", "[ ] Witnesses needed: ___",
        "[ ] License obtained: ___/___/___", "[ ] Return signed license by: ___/___/___"]
    for item in lic:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 14
    y -= 15
    doc.add_text(72, y, "EMERGENCY KIT CHECKLIST:", 'F2', 10)
    y -= 16
    kit = ["[ ] Sewing kit", "[ ] Safety pins", "[ ] Tide pen", "[ ] Bobby pins",
        "[ ] Clear nail polish", "[ ] Band-aids", "[ ] Pain reliever",
        "[ ] Breath mints", "[ ] Tissues", "[ ] Phone charger",
        "[ ] Snacks", "[ ] Water bottles", "[ ] Deodorant", "[ ] Blotting papers"]
    for item in kit:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 13

    doc.save("Book222_Wedding_Planning_Complete.pdf")
    print("Created: Book222_Wedding_Planning_Complete.pdf")

if __name__ == "__main__":
    create_book()
