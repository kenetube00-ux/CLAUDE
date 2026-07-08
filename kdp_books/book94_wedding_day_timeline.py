"""Book 94: Wedding Day Coordinator"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.08)
    pdf.add_centered_text(520, "WEDDING DAY", 'F5', 32, 1)
    pdf.add_centered_text(480, "COORDINATOR", 'F5', 32, 1)
    pdf.add_centered_text(430, "Hour-by-Hour Timeline & Emergency Planner", 'F4', 15, 0.9)
    pdf.add_centered_text(380, "Everything You Need for the Big Day", 'F1', 13, 0.8)
    pdf.add_centered_text(355, "From Getting Ready to Grand Exit", 'F1', 13, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)

    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "Wedding Day Coordinator", 'F5', 14)
    pdf.add_centered_text(478, "Hour-by-Hour Timeline & Emergency Planner", 'F4', 11)
    pdf.add_centered_text(445, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(425, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(395, "Congratulations on your upcoming wedding!", 'F4', 10)


    # Page 1: Hour-by-Hour Timeline (6am-12pm)
    pdf.new_page()
    pdf.add_centered_text(750, "HOUR-BY-HOUR WEDDING DAY TIMELINE", 'F2', 16)
    pdf.add_centered_text(732, "Part 1: Morning (6:00 AM - 12:00 PM)", 'F4', 12)
    pdf.add_line(72, 722, 540, 722, 1, 0.3)
    y = 700
    morning_times = [
        ("6:00 AM", "Wake up, light breakfast, start hydrating"),
        ("6:30 AM", "Hair & makeup team arrives (location: _____________)"),
        ("7:00 AM", "Bride hair/makeup begins. Bridesmaids rotate."),
        ("7:30 AM", "Photographer arrives for 'getting ready' shots"),
        ("8:00 AM", "Groom & groomsmen begin getting ready (location: ________)"),
        ("8:30 AM", "Steamer/iron check all garments. Lay out accessories."),
        ("9:00 AM", "Bride: Makeup complete. Begin bridal gown dressing."),
        ("9:30 AM", "Detail shots: rings, shoes, invitation, bouquet, dress"),
        ("10:00 AM", "Bridesmaids dressed. First look with bridesmaids."),
        ("10:30 AM", "First look with bride & groom (if doing) Location: _______"),
        ("11:00 AM", "Bridal party photos (allow 45-60 minutes)"),
        ("11:30 AM", "Family formal photos (parents, grandparents, siblings)"),
        ("12:00 PM", "Break: Snacks, water, touch-up makeup, bathroom"),
    ]
    for time, task in morning_times:
        pdf.add_text(72, y, time, 'F2', 9)
        pdf.add_text(145, y, task, 'F1', 9)
        y -= 18
        pdf.add_text(145, y, "Notes: _______________________________________________", 'F1', 8)
        y -= 20

    # Page 2: Hour-by-Hour Timeline (12pm-6pm)
    pdf.new_page()
    pdf.add_centered_text(750, "HOUR-BY-HOUR WEDDING DAY TIMELINE", 'F2', 16)
    pdf.add_centered_text(732, "Part 2: Afternoon (12:00 PM - 6:00 PM)", 'F4', 12)
    pdf.add_line(72, 722, 540, 722, 1, 0.3)
    y = 700
    afternoon_times = [
        ("12:00 PM", "Lunch for bridal party (keep it light, no red sauce!)"),
        ("12:30 PM", "Venue access begins. Coordinator checks setup."),
        ("1:00 PM", "Florist delivers & arranges. Check all arrangements."),
        ("1:30 PM", "DJ/Band arrives for sound check"),
        ("2:00 PM", "Officiant arrives. Review ceremony logistics."),
        ("2:30 PM", "Guests begin arriving. Ushers in position."),
        ("3:00 PM", "Wedding party lineup. Final touch-ups."),
        ("3:15 PM", "Mothers/grandmothers seated. Candles lit."),
        ("3:25 PM", "Groom & groomsmen take positions"),
        ("3:30 PM", "CEREMONY BEGINS - Processional"),
        ("4:00 PM", "Ceremony ends. Recessional. Receiving line (optional)"),
        ("4:30 PM", "Cocktail hour for guests. Couple photos."),
        ("5:00 PM", "Bridal party joins cocktail hour. Final venue check."),
        ("5:30 PM", "Guests move to reception. DJ ready."),
    ]
    for time, task in afternoon_times:
        pdf.add_text(72, y, time, 'F2', 9)
        pdf.add_text(145, y, task, 'F1', 9)
        y -= 18
        pdf.add_text(145, y, "Notes: _______________________________________________", 'F1', 8)
        y -= 20


    # Page 3: Hour-by-Hour Timeline (6pm-midnight)
    pdf.new_page()
    pdf.add_centered_text(750, "HOUR-BY-HOUR WEDDING DAY TIMELINE", 'F2', 16)
    pdf.add_centered_text(732, "Part 3: Evening (6:00 PM - Midnight)", 'F4', 12)
    pdf.add_line(72, 722, 540, 722, 1, 0.3)
    y = 700
    evening_times = [
        ("6:00 PM", "Grand entrance! Bridal party introduced."),
        ("6:15 PM", "First dance"),
        ("6:25 PM", "Welcome speech / blessing / grace"),
        ("6:30 PM", "Dinner service begins"),
        ("7:15 PM", "Toasts & speeches begin (best man, maid of honor, parents)"),
        ("7:45 PM", "Cake cutting"),
        ("8:00 PM", "Parent dances (father-daughter, mother-son)"),
        ("8:15 PM", "Dance floor opens! Party begins."),
        ("9:00 PM", "Bouquet/garter toss (optional)"),
        ("9:30 PM", "Late-night snacks served (if applicable)"),
        ("10:00 PM", "Last call announcement (if applicable)"),
        ("10:30 PM", "Last dance"),
        ("10:45 PM", "Grand exit (sparklers, bubbles, petals, etc.)"),
        ("11:00 PM", "Vendor breakdown begins. Personal items collected."),
        ("11:30 PM", "Final venue walkthrough. Nothing left behind."),
        ("12:00 AM", "Venue must be cleared by: ___________"),
    ]
    for time, task in evening_times:
        pdf.add_text(72, y, time, 'F2', 9)
        pdf.add_text(145, y, task, 'F1', 9)
        y -= 18
        pdf.add_text(145, y, "Notes: _______________________________________________", 'F1', 8)
        y -= 18

    # Page 4: Getting Ready Schedule - Bride + Bridesmaids
    pdf.new_page()
    pdf.add_centered_text(750, "GETTING READY SCHEDULE - BRIDE & BRIDESMAIDS", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "Hair & Makeup Start Time: _________  Location: ___________________", 'F1', 10)
    y -= 20
    pdf.add_text(72, y, "Person", 'F2', 9)
    pdf.add_text(200, y, "Hair Time", 'F2', 9)
    pdf.add_text(300, y, "Makeup Time", 'F2', 9)
    pdf.add_text(420, y, "Done By", 'F2', 9)
    y -= 15
    people = ["Bride", "Maid of Honor", "Bridesmaid 1", "Bridesmaid 2",
              "Bridesmaid 3", "Bridesmaid 4", "Mother of Bride", "Mother of Groom",
              "Flower Girl", "Other: _______"]
    for p in people:
        pdf.add_text(72, y, p, 'F1', 9)
        pdf.add_line(200, y - 2, 280, y - 2, 0.5, 0.5)
        pdf.add_line(300, y - 2, 400, y - 2, 0.5, 0.5)
        pdf.add_line(420, y - 2, 510, y - 2, 0.5, 0.5)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "GETTING READY CHECKLIST:", 'F2', 10)
    y -= 16
    items = [
        "Dress steamed and hung", "All accessories laid out (jewelry, veil, shoes)",
        "Something old, new, borrowed, blue", "Emergency kit accessible",
        "Snacks & water available", "Phone chargers plugged in",
        "Music/playlist ready", "Bridesmaids gifts distributed",
        "Marriage license ready", "Rings confirmed (who has them?): __________",
    ]
    for item in items:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, item, 'F1', 9)
        y -= 18

    # Page 5: Groom's Morning Checklist
    pdf.new_page()
    pdf.add_centered_text(750, "GROOM'S MORNING CHECKLIST", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "Getting ready location: _________________________________", 'F1', 10)
    pdf.add_text(72, y - 20, "Start time: __________", 'F1', 10)
    y -= 45
    groom_items = [
        "Suit/tux picked up and inspected (no missing buttons, stains)",
        "Shoes polished and comfortable",
        "Tie/bow tie/pocket square ready",
        "Cufflinks and accessories",
        "Socks (matching!)",
        "Belt",
        "Cologne",
        "Haircut/trim (done 3-5 days before)",
        "Groomsmen gifts distributed",
        "Rings confirmed with best man",
        "Vows printed/memorized",
        "Marriage license",
        "Wallet, ID, phone, charger",
        "Hotel room key / overnight bag",
        "Officiant fee/tip envelope",
        "Vendor tip envelopes prepared",
        "Speech notes (if giving toast at rehearsal)",
        "Breath mints",
        "Breakfast eaten (not on an empty stomach!)",
        "Gift for bride (if exchanging)",
    ]
    for item in groom_items:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, item, 'F1', 9)
        y -= 20


    # Page 6-7: Photography Shot List (50+ must-have shots)
    pdf.new_page()
    pdf.add_centered_text(750, "PHOTOGRAPHY SHOT LIST - Page 1", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "GETTING READY SHOTS:", 'F2', 10)
    y -= 16
    shots_1 = [
        "Dress hanging", "Shoes detail", "Rings on invitation/flowers",
        "Bride putting on dress", "Mom zipping/buttoning dress",
        "Bride looking in mirror", "Bridesmaids reaction seeing bride",
        "Dad seeing bride first time", "Bouquet detail",
        "Groom getting ready", "Best man helping with tie",
        "Groomsmen together laughing",
    ]
    for s in shots_1:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, s, 'F1', 9)
        y -= 16
    y -= 8
    pdf.add_text(72, y, "CEREMONY SHOTS:", 'F2', 10)
    y -= 16
    shots_2 = [
        "Venue/aisle before guests arrive", "Guests arriving",
        "Groom at altar (reaction to bride)", "Each bridesmaid/groomsman walking",
        "Flower girl/ring bearer", "Bride walking with escort",
        "Bride & groom at altar (wide + close)", "Ring exchange",
        "First kiss", "Recessional (walking back together)",
        "Receiving line or exit confetti/petals",
    ]
    for s in shots_2:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, s, 'F1', 9)
        y -= 16
    y -= 8
    pdf.add_text(72, y, "FORMAL PORTRAITS:", 'F2', 10)
    y -= 16
    shots_3 = [
        "Couple alone (multiple poses/locations)",
        "Couple + full bridal party", "Bride + bridesmaids",
        "Groom + groomsmen", "Couple + bride's parents",
        "Couple + groom's parents", "Couple + all parents",
        "Couple + grandparents", "Couple + siblings",
    ]
    for s in shots_3:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, s, 'F1', 9)
        y -= 16

    pdf.new_page()
    pdf.add_centered_text(750, "PHOTOGRAPHY SHOT LIST - Page 2", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "RECEPTION SHOTS:", 'F2', 10)
    y -= 16
    shots_4 = [
        "Room/table setup before guests enter", "Place settings/centerpiece details",
        "Grand entrance", "First dance (wide + close-up)",
        "Father-daughter dance", "Mother-son dance",
        "Best man toast reaction", "Maid of honor toast",
        "Cake detail shot", "Cake cutting",
        "Bouquet toss", "Garter toss",
        "Dance floor candids", "Guest table candids",
        "Late night snack station", "Grand exit",
        "Couple's final portrait of the night",
    ]
    for s in shots_4:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, s, 'F1', 9)
        y -= 16
    y -= 8
    pdf.add_text(72, y, "ADDITIONAL MUST-HAVE SHOTS:", 'F2', 10)
    y -= 16
    for i in range(8):
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_line(90, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 18
    y -= 8
    pdf.add_text(72, y, "Photographer: _________________ Phone: _____________", 'F1', 10)
    pdf.add_text(72, y - 18, "Videographer: _________________ Phone: _____________", 'F1', 10)
    pdf.add_text(72, y - 36, "Photos delivered by (date): _____________", 'F1', 10)


    # Page 8: Ceremony Timeline
    pdf.new_page()
    pdf.add_centered_text(750, "CEREMONY TIMELINE & DETAILS", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    fields = [
        "Ceremony venue: _______________________________________________",
        "Address: _____________________________________________________",
        "Ceremony start time: __________  Doors open: __________",
        "Officiant name: _____________________ Phone: __________________",
        "",
        "PROCESSIONAL ORDER:",
        "1. ________________________________ (escorted by: _____________)",
        "2. ________________________________ (escorted by: _____________)",
        "3. ________________________________ (escorted by: _____________)",
        "4. ________________________________ (escorted by: _____________)",
        "5. ________________________________ (escorted by: _____________)",
        "6. Flower Girl: ________________ Ring Bearer: ________________",
        "7. BRIDE: _____________________ (escorted by: ________________)",
        "",
        "CEREMONY ELEMENTS:",
    ]
    for f in fields:
        pdf.add_text(72, y, f, 'F1', 10)
        y -= 17
    elements = [
        "Opening words / welcome", "Reading 1: _______________ (reader: ___________)",
        "Reading 2: _______________ (reader: ___________)", "Vows (personal / traditional)",
        "Ring exchange", "Unity ceremony (candle/sand/wine): ____________",
        "Pronouncement", "First kiss", "Presentation of couple",
        "Recessional song: _______________________________________",
    ]
    for e in elements:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, e, 'F1', 9)
        y -= 17

    # Page 9: Reception Timeline
    pdf.new_page()
    pdf.add_centered_text(750, "RECEPTION TIMELINE & DETAILS", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    pdf.add_text(72, y, "Reception venue: ______________________________________________", 'F1', 10)
    y -= 18
    pdf.add_text(72, y, "Address: _____________________________________________________", 'F1', 10)
    y -= 18
    pdf.add_text(72, y, "Cocktail hour: ________ to ________  Reception: ________ to ________", 'F1', 10)
    y -= 25
    pdf.add_text(72, y, "RECEPTION ORDER OF EVENTS:", 'F2', 11)
    y -= 18
    events = [
        ("_____:_____", "Cocktail hour begins"),
        ("_____:_____", "Guests seated for reception"),
        ("_____:_____", "Bridal party introduced (song: _________________)"),
        ("_____:_____", "Couple introduced (song: _______________________)"),
        ("_____:_____", "First dance (song: ____________________________)"),
        ("_____:_____", "Welcome speech / blessing"),
        ("_____:_____", "Dinner served"),
        ("_____:_____", "Best man toast"),
        ("_____:_____", "Maid of honor toast"),
        ("_____:_____", "Parent toast (if applicable)"),
        ("_____:_____", "Cake cutting"),
        ("_____:_____", "Father-daughter dance (song: ___________________)"),
        ("_____:_____", "Mother-son dance (song: ______________________)"),
        ("_____:_____", "Open dancing begins"),
        ("_____:_____", "Bouquet/garter toss"),
        ("_____:_____", "Last dance (song: _____________________________)"),
        ("_____:_____", "Grand exit"),
    ]
    for time, event in events:
        pdf.add_text(72, y, time, 'F3', 9)
        pdf.add_text(160, y, event, 'F1', 9)
        y -= 20

    # Page 10: Speech Order & DJ Music Requests
    pdf.new_page()
    pdf.add_centered_text(750, "SPEECH ORDER & MUSIC REQUESTS", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    pdf.add_text(72, y, "SPEECH/TOAST ORDER:", 'F2', 11)
    y -= 18
    pdf.add_text(72, y, "Order", 'F2', 9)
    pdf.add_text(120, y, "Speaker", 'F2', 9)
    pdf.add_text(280, y, "Relationship", 'F2', 9)
    pdf.add_text(420, y, "Max Time", 'F2', 9)
    y -= 15
    for i in range(6):
        pdf.add_text(72, y, f"{i+1}.", 'F2', 9)
        pdf.add_line(120, y - 2, 265, y - 2, 0.5, 0.5)
        pdf.add_line(280, y - 2, 405, y - 2, 0.5, 0.5)
        pdf.add_line(420, y - 2, 500, y - 2, 0.5, 0.5)
        y -= 22
    y -= 15
    pdf.add_text(72, y, "DJ/MUSIC REQUEST LIST:", 'F2', 11)
    y -= 18
    pdf.add_text(72, y, "DJ Name: _____________________ Phone: _________________", 'F1', 10)
    y -= 20
    pdf.add_text(72, y, "MUST PLAY:", 'F2', 10)
    y -= 15
    for i in range(6):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18
    pdf.add_text(72, y, "DO NOT PLAY:", 'F2', 10)
    y -= 15
    for i in range(4):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18


    # Page 11-12: Emergency Kit Checklist (100 items)
    pdf.new_page()
    pdf.add_centered_text(750, "WEDDING DAY EMERGENCY KIT - Page 1", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "BEAUTY & PERSONAL:", 'F2', 10)
    y -= 15
    beauty = [
        "Extra makeup (lipstick, powder, concealer)", "Makeup remover wipes",
        "Bobby pins & hair ties", "Hairspray", "Deodorant",
        "Perfume", "Breath mints/gum", "Blotting papers",
        "Cotton swabs", "Contact lens solution", "Tampons/pads",
        "Tissues", "Hand mirror", "Comb/brush",
        "Nail file & clear polish", "Toothbrush & toothpaste",
        "Floss", "Lotion/hand cream",
    ]
    for item in beauty:
        pdf.add_rect(72, y - 3, 8, 8, 0.5, 0.3)
        pdf.add_text(85, y, item, 'F1', 8)
        y -= 14
    y -= 5
    pdf.add_text(72, y, "CLOTHING & ACCESSORIES:", 'F2', 10)
    y -= 15
    clothing = [
        "Safety pins (various sizes)", "Sewing kit (needle, thread, scissors)",
        "Fashion tape (double-sided)", "Stain remover pen",
        "Steamer or wrinkle spray", "Extra earring backs",
        "Heel protectors (for grass)", "Comfortable reception shoes",
        "Nude underwear", "Strapless bra/tape", "Lint roller",
        "White chalk (for scuff marks on dress)", "Clear nail polish (for stocking runs)",
        "Shoe insoles/moleskin", "Extra cufflinks", "Extra boutonniere pins",
    ]
    for item in clothing:
        pdf.add_rect(72, y - 3, 8, 8, 0.5, 0.3)
        pdf.add_text(85, y, item, 'F1', 8)
        y -= 14

    pdf.new_page()
    pdf.add_centered_text(750, "WEDDING DAY EMERGENCY KIT - Page 2", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 720
    pdf.add_text(72, y, "HEALTH & COMFORT:", 'F2', 10)
    y -= 15
    health = [
        "Pain reliever (Advil/Tylenol)", "Antacid", "Allergy medication",
        "Band-aids (multiple sizes)", "Blister pads", "Eye drops",
        "Sunscreen", "Bug spray", "Hand sanitizer",
        "Cold water bottles", "Granola bars/snacks",
        "Electrolyte packets", "Throat lozenges",
        "Anti-nausea medication", "Epi-pen (if needed)",
    ]
    for item in health:
        pdf.add_rect(72, y - 3, 8, 8, 0.5, 0.3)
        pdf.add_text(85, y, item, 'F1', 8)
        y -= 14
    y -= 5
    pdf.add_text(72, y, "TOOLS & PRACTICAL:", 'F2', 10)
    y -= 15
    tools = [
        "Phone chargers (multiple)", "Portable battery pack",
        "Scissors", "Super glue", "Duct tape (clear)",
        "Zip ties", "Sharpie marker", "Pens (for guest book)",
        "Extra envelopes (for tips)", "Cash (small bills for tips)",
        "Umbrella(s)", "Flashlight", "Extension cord",
        "Lighter/matches (candles)", "Tape (clear & masking)",
        "Paper towels", "Trash bags", "Straws (for drinking without smudging lipstick)",
        "Towel/cloth napkin", "Bluetooth speaker (backup)",
        "Copy of vendor contracts", "Timeline copies (10+)",
        "Vendor contact list", "Seating chart backup copy",
        "Gift card reader/box for cards", "Marriage license!!",
    ]
    for item in tools:
        pdf.add_rect(72, y - 3, 8, 8, 0.5, 0.3)
        pdf.add_text(85, y, item, 'F1', 8)
        y -= 14


    # Page 13: Vendor Arrival Times
    pdf.new_page()
    pdf.add_centered_text(750, "VENDOR ARRIVAL TIMES & CONTACTS", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    vendors = [
        "Hair Stylist", "Makeup Artist", "Florist", "Photographer",
        "Videographer", "DJ / Band", "Officiant", "Caterer",
        "Baker (cake)", "Coordinator/Planner", "Limo/Transport",
        "Venue Contact", "Rental Company", "Photo Booth",
    ]
    pdf.add_text(72, y, "Vendor", 'F2', 9)
    pdf.add_text(180, y, "Name", 'F2', 9)
    pdf.add_text(310, y, "Phone", 'F2', 9)
    pdf.add_text(420, y, "Arrival", 'F2', 9)
    pdf.add_text(490, y, "End", 'F2', 9)
    y -= 15
    for v in vendors:
        pdf.add_text(72, y, v, 'F1', 8)
        pdf.add_line(180, y - 2, 295, y - 2, 0.5, 0.5)
        pdf.add_line(310, y - 2, 410, y - 2, 0.5, 0.5)
        pdf.add_line(420, y - 2, 480, y - 2, 0.5, 0.5)
        pdf.add_line(490, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22

    # Page 14: Transportation Schedule
    pdf.new_page()
    pdf.add_centered_text(750, "TRANSPORTATION SCHEDULE", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    pdf.add_text(72, y, "WHO", 'F2', 9)
    pdf.add_text(180, y, "FROM", 'F2', 9)
    pdf.add_text(300, y, "TO", 'F2', 9)
    pdf.add_text(420, y, "DEPART", 'F2', 9)
    pdf.add_text(490, y, "VEHICLE", 'F2', 9)
    y -= 15
    transports = [
        "Bride + Bridesmaids", "Groom + Groomsmen", "Parents (Bride's)",
        "Parents (Groom's)", "Bridal Party to Ceremony", "Couple to Reception",
        "Couple to Hotel", "Guests (shuttle 1)", "Guests (shuttle 2)",
    ]
    for t in transports:
        pdf.add_text(72, y, t, 'F1', 8)
        pdf.add_line(180, y - 2, 285, y - 2, 0.5, 0.5)
        pdf.add_line(300, y - 2, 405, y - 2, 0.5, 0.5)
        pdf.add_line(420, y - 2, 480, y - 2, 0.5, 0.5)
        pdf.add_line(490, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 25
    y -= 10
    pdf.add_text(72, y, "TRANSPORTATION COMPANY:", 'F2', 10)
    y -= 18
    pdf.add_text(72, y, "Company: ______________________ Phone: __________________", 'F1', 10)
    y -= 20
    pdf.add_text(72, y, "Confirmation #: _________________ Driver name: ______________", 'F1', 10)

    # Page 15: Guest Special Needs List
    pdf.new_page()
    pdf.add_centered_text(750, "GUEST SPECIAL NEEDS & ACCOMMODATIONS", 'F2', 14)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    pdf.add_text(72, y, "Guest Name", 'F2', 9)
    pdf.add_text(200, y, "Need/Accommodation", 'F2', 9)
    pdf.add_text(420, y, "Handled By", 'F2', 9)
    y -= 15
    for i in range(20):
        pdf.add_line(72, y, 185, y, 0.5, 0.5)
        pdf.add_line(200, y, 405, y, 0.5, 0.5)
        pdf.add_line(420, y, 540, y, 0.5, 0.5)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "DIETARY NEEDS: Vegetarian: ___ Vegan: ___ Gluten-free: ___ Nut allergy: ___", 'F1', 9)
    y -= 18
    pdf.add_text(72, y, "Wheelchair access needed: ___ Elderly seating: ___ Children's meals: ___", 'F1', 9)

    # Page 16: Tipping Guide
    pdf.new_page()
    pdf.add_centered_text(750, "VENDOR TIPPING GUIDE", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    pdf.add_text(72, y, "Vendor", 'F2', 9)
    pdf.add_text(200, y, "Standard Tip", 'F2', 9)
    pdf.add_text(340, y, "Amount", 'F2', 9)
    pdf.add_text(430, y, "Envelope Ready?", 'F2', 9)
    y -= 18
    tips = [
        ("Coordinator/Planner", "15-20% or $50-150"),
        ("Caterer/Chef", "15-20% of food bill"),
        ("Wait staff", "$20-50 each"),
        ("Bartenders", "10-15% of bar bill"),
        ("DJ", "10-15% or $50-150"),
        ("Band", "$25-50 per member"),
        ("Photographer", "Not expected / $50-200"),
        ("Videographer", "Not expected / $50-200"),
        ("Florist", "Not expected / $20-50"),
        ("Hair Stylist", "15-20%"),
        ("Makeup Artist", "15-20%"),
        ("Officiant", "$50-200 (donation if clergy)"),
        ("Limo Driver", "15-20% or $25-50"),
        ("Delivery drivers", "$5-20 each"),
        ("Valet", "$1-2 per car (host covers)"),
    ]
    for vendor, tip in tips:
        pdf.add_text(72, y, vendor, 'F1', 9)
        pdf.add_text(200, y, tip, 'F1', 9)
        pdf.add_line(340, y - 2, 415, y - 2, 0.5, 0.5)
        pdf.add_rect(430, y - 3, 10, 10, 0.5, 0.3)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "Total tip budget: $___________", 'F2', 10)
    pdf.add_text(72, y - 18, "Who is distributing envelopes? ___________________", 'F1', 10)


    # Page 17: Day-After Checklist
    pdf.new_page()
    pdf.add_centered_text(750, "DAY-AFTER CHECKLIST", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    y = 715
    after_items = [
        "Return rental items (tux, decor, equipment) by: __________",
        "Collect gifts/cards from venue (who is doing this? _________)",
        "Preserve bouquet (if desired) - must be done within 24 hours",
        "Return anything borrowed",
        "Send thank-you to bridal party (text is fine for now)",
        "Post a photo/update on social media (if desired)",
        "Eat leftover cake!",
        "Store dress (schedule cleaning within 1 week)",
        "Mail marriage license (if not filed at ceremony)",
        "Change name (if applicable) - start process within 1 week",
        "Write down favorite moments while fresh",
        "Consolidate all gifts in one location",
        "Check for any vendor follow-ups needed",
        "Send tip to any vendor missed at wedding",
        "Enjoy being married!",
    ]
    for item in after_items:
        pdf.add_rect(72, y - 3, 10, 10, 0.5, 0.3)
        pdf.add_text(90, y, item, 'F1', 9)
        y -= 22
    y -= 10
    pdf.add_text(72, y, "Items left at venue to retrieve:", 'F2', 10)
    y -= 18
    for i in range(5):
        pdf.add_line(72, y, 540, y, 0.5, 0.5)
        y -= 18

    # Pages 18-20: Thank-You Card Tracker (3 pages)
    for pg in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(750, f"THANK-YOU CARD TRACKER - Page {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        y = 720
        pdf.add_text(72, y, "Guest Name", 'F2', 8)
        pdf.add_text(200, y, "Gift/Amount", 'F2', 8)
        pdf.add_text(370, y, "Card Sent?", 'F2', 8)
        pdf.add_text(460, y, "Date Sent", 'F2', 8)
        y -= 14
        for i in range(30):
            pdf.add_line(72, y, 190, y, 0.5, 0.5)
            pdf.add_line(200, y, 360, y, 0.5, 0.5)
            pdf.add_rect(370, y - 4, 8, 8, 0.5, 0.3)
            pdf.add_line(460, y, 540, y, 0.5, 0.5)
            y -= 20

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book94_Wedding_Day_Coordinator.pdf')
    print("Book94_Wedding_Day_Coordinator.pdf created successfully!")

if __name__ == "__main__":
    create_book()
