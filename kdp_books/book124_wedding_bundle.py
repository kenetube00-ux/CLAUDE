from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "THE ULTIMATE WEDDING PLANNING BUNDLE"
subtitle = "Everything You Need in One Book"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 17)
pdf.add_centered_text(515, subtitle, 'F4', 14)
pdf.add_centered_text(440, "Budget | Vendors | Guest List | Timeline | Checklists", 'F4', 11)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 11)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)

# Page 3: Budget Master Sheet
pdf.new_page()
pdf.add_centered_text(750, "WEDDING BUDGET MASTER SHEET", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 720
pdf.add_text(50, y, "TOTAL WEDDING BUDGET: $______________", 'F2', 12)
y -= 25
# Header
pdf.add_filled_rect(50, y - 3, 512, 16, 0.85)
pdf.add_text(55, y, "Category", 'F2', 9)
pdf.add_text(220, y, "Estimated", 'F2', 9)
pdf.add_text(310, y, "Actual", 'F2', 9)
pdf.add_text(390, y, "Deposit", 'F2', 9)
pdf.add_text(460, y, "Balance", 'F2', 9)
pdf.add_text(530, y, "Paid?", 'F2', 9)
y -= 18
categories = [
    "Venue (Ceremony)", "Venue (Reception)", "Catering/Food", "Bar/Drinks",
    "Photography", "Videography", "Flowers/Decor", "DJ/Band/Music",
    "Wedding Cake/Desserts", "Officiant", "Wedding Dress/Alterations",
    "Groom's Attire", "Bridal Party Gifts", "Invitations/Stationery",
    "Hair & Makeup", "Transportation", "Rings", "Honeymoon",
    "Wedding Planner/Coordinator", "Miscellaneous/Emergency Fund"
]
for cat in categories:
    pdf.add_text(55, y, cat, 'F4', 8)
    pdf.add_text(220, y, "$________", 'F3', 8)
    pdf.add_text(310, y, "$________", 'F3', 8)
    pdf.add_text(390, y, "$________", 'F3', 8)
    pdf.add_text(460, y, "$________", 'F3', 8)
    pdf.add_rect(540, y - 2, 10, 10, 0.5)
    y -= 16
    pdf.add_line(50, y + 5, 562, y + 5, 0.2, 0.8)
y -= 10
pdf.add_line(50, y + 5, 562, y + 5, 1, 0)
pdf.add_text(55, y - 8, "TOTALS:", 'F2', 9)
pdf.add_text(220, y - 8, "$________", 'F2', 9)
pdf.add_text(310, y - 8, "$________", 'F2', 9)
pdf.add_text(390, y - 8, "$________", 'F2', 9)
pdf.add_text(460, y - 8, "$________", 'F2', 9)

# Pages 4-6: Vendor Contact Pages (3 pages)
vendors_pages = [
    [("Ceremony Venue", ["Contact:", "Phone:", "Email:", "Cost:", "Deposit:", "Balance Due:", "Notes:"]),
     ("Reception Venue", ["Contact:", "Phone:", "Email:", "Cost:", "Deposit:", "Balance Due:", "Notes:"]),
     ("Caterer", ["Contact:", "Phone:", "Email:", "Cost per plate:", "Min guests:", "Deposit:", "Notes:"])],
    [("Photographer", ["Contact:", "Phone:", "Email:", "Package:", "Hours:", "Cost:", "Notes:"]),
     ("Videographer", ["Contact:", "Phone:", "Email:", "Package:", "Hours:", "Cost:", "Notes:"]),
     ("Florist", ["Contact:", "Phone:", "Email:", "Cost:", "Delivery time:", "Deposit:", "Notes:"])],
    [("DJ/Band", ["Contact:", "Phone:", "Email:", "Hours:", "Cost:", "Equipment included:", "Notes:"]),
     ("Cake/Dessert", ["Contact:", "Phone:", "Email:", "Flavors:", "Servings:", "Cost:", "Notes:"]),
     ("Officiant", ["Contact:", "Phone:", "Email:", "Cost:", "Rehearsal date:", "License needed:", "Notes:"])]
]
for page_vendors in vendors_pages:
    pdf.new_page()
    pdf.add_centered_text(750, "VENDOR CONTACT INFORMATION", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    for vendor_name, fields in page_vendors:
        pdf.add_filled_rect(50, y - 3, 512, 16, 0.9)
        pdf.add_text(55, y, vendor_name.upper(), 'F2', 10)
        y -= 20
        for field in fields:
            pdf.add_text(60, y, field, 'F1', 9)
            pdf.add_line(140, y - 2, 562, y - 2, 0.3, 0.5)
            y -= 14
        y -= 15

# Pages 7-10: Guest List (4 pages, ~50 guests each = 200 total)
for gl_page in range(1, 5):
    pdf.new_page()
    start_num = (gl_page - 1) * 50 + 1
    end_num = gl_page * 50
    pdf.add_centered_text(750, f"GUEST LIST - GUESTS {start_num}-{end_num}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 722
    # Header
    pdf.add_filled_rect(50, y - 3, 512, 14, 0.85)
    pdf.add_text(52, y, "#", 'F2', 7)
    pdf.add_text(65, y, "Name", 'F2', 7)
    pdf.add_text(185, y, "Address", 'F2', 7)
    pdf.add_text(330, y, "RSVP", 'F2', 7)
    pdf.add_text(370, y, "Meal", 'F2', 7)
    pdf.add_text(415, y, "+1?", 'F2', 7)
    pdf.add_text(450, y, "Gift", 'F2', 7)
    pdf.add_text(500, y, "TY Sent", 'F2', 7)
    y -= 14
    for g in range(50):
        guest_num = start_num + g
        pdf.add_text(52, y, f"{guest_num}", 'F3', 6)
        pdf.add_line(65, y - 1, 180, y - 1, 0.2, 0.6)
        pdf.add_line(185, y - 1, 325, y - 1, 0.2, 0.6)
        pdf.add_text(330, y, "Y/N", 'F3', 6)
        pdf.add_text(370, y, "___", 'F3', 6)
        pdf.add_text(415, y, "Y/N", 'F3', 6)
        pdf.add_rect(455, y - 1, 8, 8, 0.3)
        pdf.add_rect(505, y - 1, 8, 8, 0.3)
        y -= 13

# Pages 11-12: 12-Month Countdown Checklist (2 pages)
pdf.new_page()
pdf.add_centered_text(750, "12-MONTH COUNTDOWN CHECKLIST", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 720
months_1 = {
    "12 MONTHS BEFORE": ["Set budget", "Create guest list draft", "Book ceremony venue", "Book reception venue", "Start researching vendors", "Choose wedding party"],
    "10-11 MONTHS BEFORE": ["Book photographer", "Book videographer", "Book caterer", "Book DJ/band", "Start dress shopping", "Choose wedding colors/theme"],
    "8-9 MONTHS BEFORE": ["Order wedding dress", "Book florist", "Book officiant", "Send save-the-dates", "Plan honeymoon", "Book hotel room blocks"],
    "6-7 MONTHS BEFORE": ["Order invitations", "Book cake baker", "Book hair & makeup", "Register for gifts", "Plan rehearsal dinner", "Book transportation"]
}
for month_label, tasks in months_1.items():
    pdf.add_text(50, y, month_label, 'F2', 10)
    y -= 14
    for task in tasks:
        pdf.add_rect(60, y - 2, 9, 9, 0.4)
        pdf.add_text(74, y, task, 'F4', 9)
        y -= 13
    y -= 10

pdf.new_page()
pdf.add_centered_text(750, "12-MONTH COUNTDOWN (continued)", 'F2', 14)
pdf.add_line(50, 740, 562, 740)
y = 720
months_2 = {
    "4-5 MONTHS BEFORE": ["Final dress fitting", "Order groom/gridal party attire", "Finalize menu", "Plan ceremony details", "Buy wedding bands", "Confirm all vendor contracts"],
    "2-3 MONTHS BEFORE": ["Mail invitations", "Finalize seating chart", "Write vows", "Get marriage license", "Final venue walkthrough", "Confirm honeymoon reservations"],
    "1 MONTH BEFORE": ["Final RSVP deadline", "Give final count to caterer", "Confirm all vendors", "Break in wedding shoes", "Finalize day-of timeline", "Prepare emergency kit"],
    "1 WEEK BEFORE": ["Confirm all details with vendors", "Pack for honeymoon", "Prepare tips/final payments", "Rehearsal & rehearsal dinner", "Delegate day-of tasks", "REST and hydrate!"],
    "DAY OF": ["Eat breakfast!", "Follow your timeline", "Delegate problems to coordinator", "Be present and enjoy every moment", "MARRY THE LOVE OF YOUR LIFE!", "Celebrate!"]
}
for month_label, tasks in months_2.items():
    pdf.add_text(50, y, month_label, 'F2', 10)
    y -= 14
    for task in tasks:
        pdf.add_rect(60, y - 2, 9, 9, 0.4)
        pdf.add_text(74, y, task, 'F4', 9)
        y -= 13
    y -= 10

# Pages 13-14: Seating Chart Planner (2 pages)
for seat_page in range(1, 3):
    pdf.new_page()
    pdf.add_centered_text(750, f"SEATING CHART PLANNER - PAGE {seat_page}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    tables_start = (seat_page - 1) * 8 + 1
    for t in range(8):
        table_num = tables_start + t
        pdf.add_filled_rect(50, y - 5, 512, 72, 0.95)
        pdf.add_rect(50, y - 5, 512, 72, 0.5, 0.5)
        pdf.add_text(55, y + 52, f"TABLE {table_num}    Size: ___ guests    Location: _______________", 'F2', 9)
        pdf.add_text(55, y + 36, "Guests: _______________________________________________________________", 'F1', 8)
        pdf.add_text(55, y + 22, "_______________________________________________________________", 'F1', 8)
        pdf.add_text(55, y + 8, "Notes (dietary/relationships): __________________________________________", 'F1', 8)
        y -= 85

# Page 15: Day-of Timeline
pdf.new_page()
pdf.add_centered_text(750, "DAY-OF TIMELINE", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 720
pdf.add_text(50, y, "Wedding Date: ___/___/___", 'F2', 11)
y -= 20
times = [
    "6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM",
    "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM",
    "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM",
    "12:00 AM"
]
for time in times:
    pdf.add_text(50, y, time, 'F2', 9)
    pdf.add_line(115, y - 2, 562, y - 2, 0.3, 0.5)
    y -= 14
    pdf.add_text(115, y, "Who:", 'F1', 8)
    pdf.add_line(140, y - 2, 300, y - 2, 0.2, 0.6)
    pdf.add_text(310, y, "Where:", 'F1', 8)
    pdf.add_line(345, y - 2, 562, y - 2, 0.2, 0.6)
    y -= 16

# Page 16: Bridal Party Info
pdf.new_page()
pdf.add_centered_text(750, "BRIDAL PARTY INFORMATION", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "BRIDESMAIDS:", 'F2', 12)
y -= 18
for i in range(6):
    pdf.add_text(55, y, f"{i+1}. Name:", 'F1', 9)
    pdf.add_line(105, y - 2, 300, y - 2, 0.3, 0.5)
    pdf.add_text(310, y, "Phone:", 'F1', 9)
    pdf.add_line(345, y - 2, 562, y - 2, 0.3, 0.5)
    y -= 14
    pdf.add_text(70, y, "Dress size:", 'F1', 8)
    pdf.add_line(120, y - 2, 200, y - 2, 0.2, 0.6)
    pdf.add_text(210, y, "Shoe size:", 'F1', 8)
    pdf.add_line(260, y - 2, 320, y - 2, 0.2, 0.6)
    y -= 18
y -= 10
pdf.add_text(50, y, "GROOMSMEN:", 'F2', 12)
y -= 18
for i in range(6):
    pdf.add_text(55, y, f"{i+1}. Name:", 'F1', 9)
    pdf.add_line(105, y - 2, 300, y - 2, 0.3, 0.5)
    pdf.add_text(310, y, "Phone:", 'F1', 9)
    pdf.add_line(345, y - 2, 562, y - 2, 0.3, 0.5)
    y -= 14
    pdf.add_text(70, y, "Suit size:", 'F1', 8)
    pdf.add_line(115, y - 2, 200, y - 2, 0.2, 0.6)
    pdf.add_text(210, y, "Shoe size:", 'F1', 8)
    pdf.add_line(260, y - 2, 320, y - 2, 0.2, 0.6)
    y -= 18
y -= 10
pdf.add_text(50, y, "OTHER KEY PEOPLE:", 'F2', 10)
y -= 14
roles = ["Maid of Honor:", "Best Man:", "Flower Girl:", "Ring Bearer:", "Usher 1:", "Usher 2:"]
for role in roles:
    pdf.add_text(60, y, role, 'F1', 9)
    pdf.add_line(140, y - 2, 562, y - 2, 0.3, 0.5)
    y -= 14

# Page 17: Honeymoon Planner
pdf.new_page()
pdf.add_centered_text(750, "HONEYMOON PLANNER", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
honey = [
    "Destination: ___________________________________________________",
    "Departure Date: ___/___/___    Return Date: ___/___/___",
    "Budget: $_______________",
    "",
    "FLIGHTS:",
    "  Outbound: Airline _________ Flight # _______ Time _______",
    "  Return:   Airline _________ Flight # _______ Time _______",
    "  Confirmation #: ______________________________________________",
    "",
    "ACCOMMODATION:",
    "  Hotel/Resort: ________________________________________________",
    "  Address: _____________________________________________________",
    "  Confirmation #: ______________________________________________",
    "  Check-in: _______ Check-out: _______",
    "",
    "TRANSPORTATION:",
    "  Airport transfer: ____________________________________________",
    "  Rental car: __________________________________________________",
    "",
    "ACTIVITIES PLANNED:",
    "  Day 1: _______________________________________________________",
    "  Day 2: _______________________________________________________",
    "  Day 3: _______________________________________________________",
    "  Day 4: _______________________________________________________",
    "  Day 5: _______________________________________________________",
    "  Day 6: _______________________________________________________",
    "  Day 7: _______________________________________________________",
    "",
    "PACKING CHECKLIST:",
    "  [ ] Passports/IDs    [ ] Tickets/confirmations    [ ] Medications",
    "  [ ] Sunscreen        [ ] Camera/charger           [ ] Cash/cards",
    "  [ ] Swimwear         [ ] Formal outfit            [ ] Comfortable shoes",
    "",
    "NOTES: ________________________________________________________",
]
for line in honey:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 15

# Pages 18-19: Wedding Vow Writing (2 pages)
for vow_page, person in enumerate(["BRIDE", "GROOM"], 1):
    pdf.new_page()
    pdf.add_centered_text(750, f"WEDDING VOW WRITING - {person}", 'F2', 16)
    pdf.add_line(50, 740, 562, 740)
    y = 710
    pdf.add_text(50, y, "Use these prompts to write your personal vows:", 'F4', 11)
    y -= 25
    prompts = [
        "When I first knew I loved you:",
        "What I admire most about you:",
        "My promise for the hard times:",
        "My promise for the good times:",
        "The life I want to build with you:",
    ]
    for prompt in prompts:
        pdf.add_text(50, y, prompt, 'F2', 10)
        y -= 16
        for _ in range(3):
            pdf.add_line(60, y, 562, y, 0.3, 0.5)
            y -= 14
        y -= 10
    y -= 10
    pdf.add_text(50, y, "MY FINAL VOWS (what I will say):", 'F2', 11)
    y -= 18
    for _ in range(10):
        pdf.add_line(60, y, 562, y, 0.3, 0.5)
        y -= 16

# Page 20: Menu Selection Worksheet
pdf.new_page()
pdf.add_centered_text(750, "MENU SELECTION WORKSHEET", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Caterer: _____________________  Tasting Date: ___/___/___", 'F2', 10)
y -= 25
sections = ["COCKTAIL HOUR", "APPETIZERS", "SALAD/SOUP", "ENTREE OPTIONS", "SIDES", "DESSERT", "BAR/DRINKS"]
for section in sections:
    pdf.add_filled_rect(50, y - 3, 512, 14, 0.9)
    pdf.add_text(55, y, section, 'F2', 9)
    y -= 18
    for _ in range(3):
        pdf.add_text(60, y, "Option:", 'F1', 8)
        pdf.add_line(95, y - 2, 350, y - 2, 0.3, 0.5)
        pdf.add_text(360, y, "Cost:", 'F1', 8)
        pdf.add_line(390, y - 2, 450, y - 2, 0.3, 0.5)
        pdf.add_rect(460, y - 2, 9, 9, 0.4)
        pdf.add_text(474, y, "Selected", 'F1', 7)
        y -= 13
    y -= 8
y -= 5
pdf.add_text(50, y, "Dietary accommodations needed: _________________________________________", 'F1', 9)
y -= 14
pdf.add_text(50, y, "Total food/beverage cost: $______________", 'F1', 9)

# Page 21: Music Request List
pdf.new_page()
pdf.add_centered_text(750, "MUSIC REQUEST LIST", 'F2', 16)
pdf.add_line(50, 740, 562, 740)
y = 715
music_sections = [
    ("CEREMONY MUSIC", ["Processional (bridal party):", "Bride's entrance:", "During ceremony:", "Recessional:"]),
    ("RECEPTION - SPECIAL DANCES", ["First dance (song/artist):", "Father-daughter dance:", "Mother-son dance:", "Last dance:"]),
    ("MUST-PLAY LIST", [f"Song {i+1}: ___________________ Artist: ___________________" for i in range(8)]),
    ("DO-NOT-PLAY LIST", [f"Song {i+1}: ___________________ Artist: ___________________" for i in range(5)])
]
for section_title, items in music_sections:
    pdf.add_text(50, y, section_title, 'F2', 11)
    y -= 16
    for item in items:
        pdf.add_text(60, y, item, 'F4', 9)
        if ":" in item and "___" not in item:
            pdf.add_line(230, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 14
    y -= 12

# Pages 22-24: Thank You Tracker (3 pages)
for ty_page in range(1, 4):
    pdf.new_page()
    start = (ty_page - 1) * 25 + 1
    pdf.add_centered_text(750, f"THANK YOU TRACKER - PAGE {ty_page}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 722
    pdf.add_filled_rect(50, y - 3, 512, 14, 0.85)
    pdf.add_text(55, y, "#", 'F2', 7)
    pdf.add_text(70, y, "Name", 'F2', 7)
    pdf.add_text(200, y, "Gift Received", 'F2', 7)
    pdf.add_text(350, y, "Note Sent", 'F2', 7)
    pdf.add_text(420, y, "Date Sent", 'F2', 7)
    pdf.add_text(500, y, "Notes", 'F2', 7)
    y -= 14
    for i in range(25):
        num = start + i
        pdf.add_text(55, y, f"{num}", 'F3', 7)
        pdf.add_line(70, y - 1, 195, y - 1, 0.2, 0.6)
        pdf.add_line(200, y - 1, 340, y - 1, 0.2, 0.6)
        pdf.add_rect(360, y - 1, 8, 8, 0.3)
        pdf.add_line(420, y - 1, 490, y - 1, 0.2, 0.6)
        pdf.add_line(500, y - 1, 560, y - 1, 0.2, 0.6)
        y -= 14

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book124_Wedding_Planning_Bundle.pdf')
print("Book124_Wedding_Planning_Bundle.pdf created successfully!")
