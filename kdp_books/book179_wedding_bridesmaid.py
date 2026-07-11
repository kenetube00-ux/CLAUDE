#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(420, "THE BRIDESMAID PLANNER", 'F2', 20)
pdf.add_centered_text(385, "Your Guide to Being the Best", 'F4', 13)
pdf.add_centered_text(365, "Bridesmaid Ever", 'F4', 13)
pdf.add_centered_text(330, f"By {author}", 'F4', 11)
pdf.add_line(80, 310, 352, 310, 2)

# Page 2 - Copyright + Overview
pdf.new_page()
pdf.add_centered_text(420, f"Copyright - {author}", 'F1', 9)
pdf.add_centered_text(405, "All rights reserved.", 'F1', 9)
pdf.add_text(40, 370, "BRIDESMAID DUTIES OVERVIEW:", 'F2', 11)
duties = [
    "Help the bride with wedding planning tasks",
    "Attend dress fittings and alterations",
    "Plan and host the bridal shower",
    "Plan the bachelorette party",
    "Help with DIY projects and decorations",
    "Be available for emotional support",
    "Attend the rehearsal and rehearsal dinner",
    "Help the bride get ready on wedding day",
    "Hold bouquet during ceremony",
    "Help bustle the dress at reception",
]
y = 350
for d in duties:
    pdf.add_text(50, y, f"- {d}", 'F1', 9)
    y -= 14

# Page 3 - Budget Tracker
pdf.new_page()
pdf.add_centered_text(620, "BRIDESMAID BUDGET TRACKER", 'F2', 14)
pdf.add_line(40, 610, 392, 610, 1)
budget_items = [
    "Bridesmaid dress", "Alterations", "Shoes", "Jewelry/accessories",
    "Hair & makeup", "Bridal shower contribution", "Bachelorette contribution",
    "Wedding gift", "Travel/hotel", "Engagement party gift",
    "Rehearsal dinner outfit", "Miscellaneous"
]
y = 590
pdf.add_text(40, y, "ITEM", 'F2', 9)
pdf.add_text(200, y, "BUDGET", 'F2', 9)
pdf.add_text(280, y, "ACTUAL", 'F2', 9)
pdf.add_text(350, y, "PAID", 'F2', 9)
y -= 5
pdf.add_line(40, y, 392, y, 0.5)
y -= 15
for item in budget_items:
    pdf.add_text(40, y, item, 'F1', 8)
    pdf.add_text(200, y, "$________", 'F1', 8)
    pdf.add_text(280, y, "$________", 'F1', 8)
    pdf.add_rect(360, y-3, 10, 10)
    y -= 18
pdf.add_line(40, y, 392, y, 1)
y -= 15
pdf.add_text(40, y, "TOTAL", 'F2', 9)
pdf.add_text(200, y, "$________", 'F2', 9)
pdf.add_text(280, y, "$________", 'F2', 9)
pdf.add_text(40, y-30, "My total bridesmaid budget: $__________", 'F1', 10)
pdf.add_text(40, y-50, "Notes:", 'F1', 10)
pdf.add_line(40, y-65, 392, y-65, 0.5, 0.7)
pdf.add_line(40, y-80, 392, y-80, 0.5, 0.7)


# Pages 4-8 - Bridal Shower Planning (5 pages)
pdf.new_page()
pdf.add_centered_text(620, "BRIDAL SHOWER - THEME & VISION", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Bride's preferences:", 'F2', 10)
pdf.add_text(40, 575, "Theme ideas: ________________________________________", 'F1', 9)
pdf.add_text(40, 558, "Color scheme: ________________________________________", 'F1', 9)
pdf.add_text(40, 541, "Venue options: ________________________________________", 'F1', 9)
pdf.add_text(40, 524, "Date/time: ________________________________________", 'F1', 9)
pdf.add_text(40, 507, "Budget per bridesmaid: $________", 'F1', 9)
pdf.add_text(40, 490, "Total budget: $________", 'F1', 9)
pdf.add_text(40, 465, "Decorations needed:", 'F2', 10)
y = 448
for i in range(8):
    pdf.add_line(50, y, 392, y, 0.5, 0.7)
    y -= 16

pdf.new_page()
pdf.add_centered_text(620, "BRIDAL SHOWER - GUEST LIST", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 595, "NAME", 'F2', 8)
pdf.add_text(180, 595, "RSVP", 'F2', 8)
pdf.add_text(230, 595, "DIETARY", 'F2', 8)
pdf.add_text(310, 595, "CONTACT", 'F2', 8)
y = 580
for i in range(30):
    pdf.add_text(40, y, f"{i+1}.", 'F1', 7)
    pdf.add_line(55, y-2, 170, y-2, 0.3, 0.7)
    pdf.add_line(180, y-2, 220, y-2, 0.3, 0.7)
    pdf.add_line(230, y-2, 300, y-2, 0.3, 0.7)
    pdf.add_line(310, y-2, 392, y-2, 0.3, 0.7)
    y -= 17

pdf.new_page()
pdf.add_centered_text(620, "BRIDAL SHOWER - MENU PLANNING", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Appetizers:", 'F2', 10)
y = 573
for i in range(4):
    pdf.add_line(50, y, 392, y, 0.5, 0.7)
    y -= 16
pdf.add_text(40, y, "Main dishes:", 'F2', 10)
y -= 15
for i in range(3):
    pdf.add_line(50, y, 392, y, 0.5, 0.7)
    y -= 16
pdf.add_text(40, y, "Desserts:", 'F2', 10)
y -= 15
for i in range(3):
    pdf.add_line(50, y, 392, y, 0.5, 0.7)
    y -= 16
pdf.add_text(40, y, "Drinks:", 'F2', 10)
y -= 15
for i in range(3):
    pdf.add_line(50, y, 392, y, 0.5, 0.7)
    y -= 16
pdf.add_text(40, y, "Catering/ordering from: _______________________", 'F1', 9)
pdf.add_text(40, y-18, "Total food budget: $_________", 'F1', 9)

pdf.new_page()
pdf.add_centered_text(620, "BRIDAL SHOWER - GAMES & ACTIVITIES", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
games = ["Bridal Bingo", "How well do you know the bride?", "Wedding dress toilet paper game",
         "Advice cards for the bride", "Ring hunt", "He said/she said",
         "Purse scavenger hunt", "Love story mad libs"]
y = 590
for g in games:
    pdf.add_rect(45, y-8, 10, 10)
    pdf.add_text(60, y-6, g, 'F1', 9)
    pdf.add_text(60, y-20, "Supplies needed: ________________________________", 'F1', 8)
    y -= 35
pdf.add_text(40, y, "Other games: ________________________________________", 'F1', 9)

pdf.new_page()
pdf.add_centered_text(620, "BRIDAL SHOWER - TIMELINE", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
timeline = [("8 weeks before:", "Book venue, set date, start guest list"),
            ("6 weeks before:", "Send invitations, order decorations"),
            ("4 weeks before:", "Plan menu, order cake, plan games"),
            ("2 weeks before:", "Confirm RSVPs, finalize details"),
            ("1 week before:", "Buy groceries, prep decorations"),
            ("Day before:", "Set up venue, prep food"),
            ("Day of:", "Arrive early, set up, enjoy!")]
y = 585
for time, task in timeline:
    pdf.add_text(40, y, time, 'F2', 9)
    pdf.add_text(150, y, task, 'F1', 9)
    pdf.add_line(40, y-12, 392, y-12, 0.3, 0.8)
    y -= 30


# Pages 9-11 - Bachelorette Party Planner (3 pages)
pdf.new_page()
pdf.add_centered_text(620, "BACHELORETTE PARTY - PLANNING", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Date: ____________  Location: ________________________", 'F1', 9)
pdf.add_text(40, 572, "Theme: ________________________________________", 'F1', 9)
pdf.add_text(40, 554, "Budget per person: $______  Total budget: $________", 'F1', 9)
pdf.add_text(40, 530, "Itinerary:", 'F2', 10)
times = ["10:00 AM", "12:00 PM", "2:00 PM", "4:00 PM", "6:00 PM", "8:00 PM", "10:00 PM"]
y = 512
for t in times:
    pdf.add_text(45, y, t, 'F1', 9)
    pdf.add_line(110, y-2, 392, y-2, 0.5, 0.7)
    y -= 20
pdf.add_text(40, y-10, "Reservations needed:", 'F2', 9)
y -= 28
for i in range(4):
    pdf.add_line(50, y, 392, y, 0.5, 0.7)
    y -= 16

pdf.new_page()
pdf.add_centered_text(620, "BACHELORETTE - ATTENDEES & COSTS", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 595, "NAME", 'F2', 8)
pdf.add_text(160, 595, "PAID?", 'F2', 8)
pdf.add_text(210, 595, "DIETARY/ALLERGIES", 'F2', 8)
pdf.add_text(340, 595, "PHONE", 'F2', 8)
y = 580
for i in range(18):
    pdf.add_text(40, y, f"{i+1}.", 'F1', 7)
    pdf.add_line(55, y-2, 155, y-2, 0.3, 0.7)
    pdf.add_rect(168, y-6, 8, 8)
    pdf.add_line(210, y-2, 335, y-2, 0.3, 0.7)
    pdf.add_line(340, y-2, 392, y-2, 0.3, 0.7)
    y -= 22

pdf.new_page()
pdf.add_centered_text(620, "BACHELORETTE - SUPPLIES & NOTES", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Supplies to buy:", 'F2', 10)
y = 573
for i in range(10):
    pdf.add_rect(45, y-8, 10, 10)
    pdf.add_line(60, y-5, 392, y-5, 0.5, 0.7)
    y -= 18
pdf.add_text(40, y-5, "Notes & Ideas:", 'F2', 10)
y -= 22
for i in range(10):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 16

# Page 12 - Dress Fitting Appointments
pdf.new_page()
pdf.add_centered_text(620, "DRESS FITTING APPOINTMENTS", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Dress shop: ________________________________________", 'F1', 9)
pdf.add_text(40, 572, "Dress style/color: __________________________________", 'F1', 9)
pdf.add_text(40, 554, "My measurements: Bust___ Waist___ Hips___ Length___", 'F1', 9)
y = 525
fittings = ["First fitting", "Second fitting", "Final fitting/pickup"]
for f in fittings:
    pdf.add_text(40, y, f"{f}:", 'F2', 10)
    y -= 15
    pdf.add_text(50, y, "Date: _______ Time: _______ Notes: __________________", 'F1', 9)
    y -= 25
pdf.add_text(40, y-10, "Shoes:", 'F2', 10)
pdf.add_text(40, y-25, "Style: _________________ Store: _________________ Cost: $_____", 'F1', 9)
pdf.add_text(40, y-50, "Accessories:", 'F2', 10)
pdf.add_text(40, y-65, "Jewelry: _________________ Hair accessories: _________________", 'F1', 9)

# Page 13 - Wedding Week Timeline
pdf.new_page()
pdf.add_centered_text(620, "WEDDING WEEK TIMELINE", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
wk_days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday (Rehearsal)", "Saturday (Wedding Day!)", "Sunday (Brunch?)"]
y = 590
for d in wk_days:
    pdf.add_text(40, y, f"{d}:", 'F2', 9)
    y -= 14
    for i in range(3):
        pdf.add_line(55, y, 392, y, 0.5, 0.7)
        y -= 14
    y -= 8

# Page 14 - Day-Of Duties
pdf.new_page()
pdf.add_centered_text(620, "DAY-OF DUTIES CHECKLIST", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
day_duties = [
    "Arrive at getting-ready location on time",
    "Help bride into dress/button up back",
    "Steam/press dress if needed",
    "Keep bride hydrated and fed",
    "Hold bride's emergency kit",
    "Line up for processional",
    "Hold bouquet during ceremony",
    "Sign witness line if needed",
    "Help bustle dress for reception",
    "Give toast/speech",
    "Help collect gifts at end of night",
    "Help bride change into going-away outfit",
    "Gather bride's belongings",
    "Return rental items next day",
]
y = 590
for d in day_duties:
    pdf.add_rect(45, y-8, 10, 10)
    pdf.add_text(60, y-6, d, 'F1', 9)
    y -= 20


# Page 15 - Emergency Kit
pdf.new_page()
pdf.add_centered_text(620, "EMERGENCY KIT FOR THE BRIDE", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
kit_items = [
    "Safety pins (various sizes)", "Sewing kit (white thread)", "Fashion tape",
    "Tide pen/stain remover", "Clear nail polish (for runs)", "Bobby pins",
    "Hair spray", "Breath mints", "Tissues", "Blotting papers",
    "Pain reliever (ibuprofen)", "Band-aids/moleskin", "Deodorant",
    "Tampons/pads", "Snacks (granola bars)", "Water bottle",
    "Phone charger", "Lip gloss/lipstick (bride's shade)", "Blister pads",
    "Antacid", "Eye drops", "Lint roller", "Scissors", "Super glue"
]
y = 590
for item in kit_items:
    pdf.add_rect(45, y-7, 9, 9)
    pdf.add_text(58, y-5, item, 'F1', 8)
    y -= 15
pdf.add_text(40, y-10, "Other items bride specifically wants:", 'F1', 9)
pdf.add_line(40, y-25, 392, y-25, 0.5, 0.7)
pdf.add_line(40, y-40, 392, y-40, 0.5, 0.7)

# Page 16 - Speech/Toast Writing Guide
pdf.new_page()
pdf.add_centered_text(620, "SPEECH & TOAST WRITING GUIDE", 'F2', 13)
pdf.add_line(40, 610, 392, 610, 1)
pdf.add_text(40, 590, "Keep it 2-4 minutes (300-500 words). Structure:", 'F1', 9)
pdf.add_text(40, 570, "1. INTRODUCE yourself & relationship to bride", 'F2', 9)
pdf.add_text(40, 555, "2. STORY - one or two fond memories", 'F2', 9)
pdf.add_text(40, 540, "3. COMPLIMENT the couple together", 'F2', 9)
pdf.add_text(40, 525, "4. TOAST - raise glass, wish them well", 'F2', 9)
pdf.add_text(40, 500, "PROMPTS:", 'F2', 10)
prompts = ["I first met [bride] when...", "What I love most about her is...",
           "When she told me about [partner], I knew because...",
           "A memory that captures who she is...",
           "Together, they are..."]
y = 483
for p in prompts:
    pdf.add_text(50, y, p, 'F4', 9)
    y -= 14
pdf.add_text(40, y-10, "MY SPEECH DRAFT:", 'F2', 10)
y -= 28
for i in range(14):
    pdf.add_line(40, y, 392, y, 0.5, 0.7)
    y -= 14

# Pages 17-20 - Gift tracking, communication, schedule, notes
for pg in range(4):
    pdf.new_page()
    titles = ["GIFT IDEAS & TRACKING", "COMMUNICATION WITH BRIDESMAIDS",
              "MY SCHEDULE - LEADING UP TO THE WEDDING", "NOTES & CONTACTS"]
    pdf.add_centered_text(620, titles[pg], 'F2', 13)
    pdf.add_line(40, 610, 392, 610, 1)
    if pg == 0:
        pdf.add_text(40, 590, "Engagement gift: _______________ Budget: $____", 'F1', 9)
        pdf.add_text(40, 572, "Bridal shower gift: _____________ Budget: $____", 'F1', 9)
        pdf.add_text(40, 554, "Wedding gift: __________________ Budget: $____", 'F1', 9)
        pdf.add_text(40, 536, "Registry info: __________________________________", 'F1', 9)
        pdf.add_text(40, 510, "Gift ideas:", 'F2', 10)
        y = 493
        for i in range(12):
            pdf.add_line(50, y, 392, y, 0.5, 0.7)
            y -= 16
    elif pg == 1:
        pdf.add_text(40, 590, "BRIDESMAID CONTACT INFO:", 'F2', 10)
        y = 570
        for i in range(6):
            pdf.add_text(40, y, f"Name: _____________________ Phone: _______________", 'F1', 9)
            pdf.add_text(40, y-14, "Email: _____________________________________", 'F1', 9)
            y -= 38
        pdf.add_text(40, y, "Group chat platform: __________________", 'F1', 9)
    elif pg == 2:
        months = ["6 months", "4 months", "3 months", "2 months",
                  "1 month", "2 weeks", "1 week", "Day before", "Wedding day"]
        y = 590
        for m in months:
            pdf.add_text(40, y, f"{m}:", 'F2', 9)
            pdf.add_line(130, y-2, 392, y-2, 0.5, 0.7)
            pdf.add_line(130, y-16, 392, y-16, 0.5, 0.7)
            y -= 38
    else:
        y = 590
        for i in range(28):
            pdf.add_line(40, y, 392, y, 0.5, 0.7)
            y -= 16

# Pages 21-25 extra content
for pg in range(5):
    pdf.new_page()
    titles = ["BRIDE'S FAVORITES & PREFERENCES", "VENDOR CONTACTS",
              "TRANSPORTATION & LOGISTICS", "MEMORIES & PHOTOS TO TAKE",
              "MY BRIDESMAID MEMORIES"]
    pdf.add_centered_text(620, titles[pg], 'F2', 13)
    pdf.add_line(40, 610, 392, 610, 1)
    y = 585
    for i in range(30):
        pdf.add_line(40, y, 392, y, 0.5, 0.7)
        y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book179_Bridesmaid_Planner.pdf')
print("Book179_Bridesmaid_Planner.pdf created successfully!")
