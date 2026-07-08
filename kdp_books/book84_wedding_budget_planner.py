"""Book 84: Wedding Budget Planner"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title page
    pdf.add_filled_rect(0, 0, 612, 792, 0.08)
    pdf.add_centered_text(520, "THE COMPLETE", 'F5', 24, 1)
    pdf.add_centered_text(480, "WEDDING PLANNER", 'F5', 28, 1)
    pdf.add_centered_text(430, "Budget Tracker, Vendor Contacts & Timeline", 'F4', 14, 0.9)
    pdf.add_centered_text(380, "Everything you need to plan your perfect day", 'F1', 12, 0.8)
    pdf.add_centered_text(350, "without the financial stress", 'F1', 12, 0.8)
    pdf.add_centered_text(200, author, 'F2', 14, 0.9)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(500, "The Complete Wedding Planner", 'F2', 13)
    pdf.add_centered_text(478, "Budget Tracker, Vendor Contacts & Timeline", 'F4', 10)
    pdf.add_centered_text(448, f"Copyright 2024 {author}. All rights reserved.", 'F1', 10)
    pdf.add_centered_text(428, "No part of this book may be reproduced without permission.", 'F1', 9)
    pdf.add_centered_text(395, "CONGRATULATIONS ON YOUR ENGAGEMENT!", 'F2', 12)
    pdf.add_centered_text(370, "This planner will help you track every dollar and detail.", 'F1', 10)
    
    # Budget Overview page
    pdf.new_page()
    pdf.add_centered_text(750, "WEDDING BUDGET OVERVIEW", 'F2', 18)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    pdf.add_text(72, 710, "Wedding Date: ___/___/______", 'F1', 11)
    pdf.add_text(350, 710, "Venue: _________________________", 'F1', 11)
    pdf.add_text(72, 680, "TOTAL WEDDING BUDGET:", 'F2', 13)
    pdf.add_text(280, 680, "$ _______________", 'F2', 13)
    y = 645
    sources = [
        "Bride's Family Contribution:",
        "Groom's Family Contribution:",
        "Couple's Contribution:",
        "Other (gifts, savings):",
    ]
    for src in sources:
        pdf.add_text(90, y, src, 'F1', 11)
        pdf.add_text(300, y, "$ _______________", 'F1', 11)
        y -= 28
    
    pdf.add_line(72, y, 540, y, 1, 0.3)
    y -= 25
    pdf.add_text(72, y, "BUDGET ALLOCATION SUMMARY:", 'F2', 12)
    y -= 22
    categories = [
        "Venue & Rentals", "Catering & Bar", "Photography", "Videography",
        "Flowers & Decor", "Music/DJ/Band", "Wedding Dress & Alterations",
        "Groom's Attire", "Bridesmaids/Groomsmen", "Invitations & Stationery",
        "Cake & Desserts", "Transportation", "Favors & Gifts",
        "Honeymoon", "Miscellaneous"
    ]
    pdf.add_text(72, y, "Category", 'F2', 9)
    pdf.add_text(220, y, "Estimated", 'F2', 9)
    pdf.add_text(310, y, "Actual", 'F2', 9)
    pdf.add_text(400, y, "Difference", 'F2', 9)
    y -= 16
    for cat in categories:
        pdf.add_text(72, y, cat, 'F1', 9)
        pdf.add_text(220, y, "$________", 'F1', 9)
        pdf.add_text(310, y, "$________", 'F1', 9)
        pdf.add_text(400, y, "$________", 'F1', 9)
        y -= 18
    pdf.add_line(72, y, 540, y, 1, 0.3)
    y -= 18
    pdf.add_text(72, y, "TOTALS:", 'F2', 10)
    pdf.add_text(220, y, "$________", 'F2', 10)
    pdf.add_text(310, y, "$________", 'F2', 10)
    pdf.add_text(400, y, "$________", 'F2', 10)

    # 15 Budget Category Pages
    for cat in categories:
        pdf.new_page()
        pdf.add_filled_rect(50, 745, 512, 30, 0.88)
        pdf.add_text(60, 753, f"BUDGET: {cat.upper()}", 'F2', 14)
        
        y = 720
        fields = [
            ("Estimated Budget:", "$_______________"),
            ("Actual Cost:", "$_______________"),
            ("Deposit Paid:", "$_______________"),
            ("Balance Due:", "$_______________"),
            ("Due Date:", "___/___/______"),
        ]
        for label, val in fields:
            pdf.add_text(72, y, label, 'F1', 10)
            pdf.add_text(200, y, val, 'F1', 10)
            y -= 22
        
        y -= 10
        pdf.add_text(72, y, "VENDOR INFORMATION:", 'F2', 11)
        y -= 20
        vendor_fields = [
            "Company Name:", "Contact Person:", "Phone:", "Email:",
            "Address:", "Website:", "Contract Signed (Y/N):", "Insurance Verified (Y/N):"
        ]
        for vf in vendor_fields:
            pdf.add_text(72, y, vf, 'F1', 10)
            pdf.add_line(200, y - 2, 540, y - 2, 0.5, 0.5)
            y -= 22
        
        y -= 10
        pdf.add_text(72, y, "PAYMENT SCHEDULE:", 'F2', 11)
        y -= 18
        pdf.add_text(72, y, "Date", 'F2', 9)
        pdf.add_text(170, y, "Amount", 'F2', 9)
        pdf.add_text(270, y, "Method", 'F2', 9)
        pdf.add_text(370, y, "Confirmed", 'F2', 9)
        y -= 16
        for _ in range(4):
            pdf.add_line(72, y, 155, y, 0.5, 0.5)
            pdf.add_line(170, y, 255, y, 0.5, 0.5)
            pdf.add_line(270, y, 355, y, 0.5, 0.5)
            pdf.add_line(370, y, 440, y, 0.5, 0.5)
            y -= 22
        
        y -= 10
        pdf.add_text(72, y, "NOTES:", 'F2', 10)
        y -= 18
        for _ in range(5):
            pdf.add_line(72, y, 540, y, 0.5, 0.5)
            y -= 18

    # Guest List Tracker (3 pages)
    for pg in range(1, 4):
        pdf.new_page()
        pdf.add_centered_text(750, f"GUEST LIST TRACKER - Page {pg}", 'F2', 14)
        pdf.add_line(72, 740, 540, 740, 1, 0.3)
        headers = ["#", "Guest Name", "RSVP", "Meal", "Gift Rcvd", "TY Sent"]
        xs = [72, 90, 260, 320, 385, 460, 530]
        y = 718
        for i, h in enumerate(headers):
            pdf.add_text(xs[i], y, h, 'F2', 8)
        y -= 15
        start_num = (pg - 1) * 25 + 1
        for row in range(25):
            num = start_num + row
            pdf.add_text(72, y, f"{num}", 'F1', 8)
            pdf.add_line(90, y - 2, 255, y - 2, 0.5, 0.5)
            pdf.add_text(265, y, "Y/N", 'F1', 7)
            pdf.add_line(320, y - 2, 375, y - 2, 0.5, 0.5)
            pdf.add_rect(395, y - 3, 7, 7, 0.5, 0.3)
            pdf.add_rect(470, y - 3, 7, 7, 0.5, 0.3)
            y -= 25

    # Timeline Checklist (12 months)
    pdf.new_page()
    pdf.add_centered_text(750, "WEDDING TIMELINE CHECKLIST", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    timeline = [
        ("12 MONTHS OUT", ["Set budget", "Book venue", "Choose wedding party", "Start guest list"]),
        ("9 MONTHS OUT", ["Book photographer/videographer", "Shop for dress", "Book DJ/band", "Send save-the-dates"]),
        ("6 MONTHS OUT", ["Book florist", "Order invitations", "Plan honeymoon", "Register for gifts"]),
        ("4 MONTHS OUT", ["Book transportation", "Order cake", "Plan rehearsal dinner", "Buy wedding bands"]),
        ("2 MONTHS OUT", ["Mail invitations", "Final dress fitting", "Confirm all vendors", "Write vows"]),
        ("1 MONTH OUT", ["Get marriage license", "Final guest count", "Create seating chart", "Confirm timeline"]),
        ("1 WEEK OUT", ["Final payments", "Pack for honeymoon", "Rehearsal", "Delegate day-of tasks"]),
    ]
    y = 715
    for period, tasks in timeline:
        pdf.add_text(72, y, period, 'F2', 10)
        y -= 15
        for task in tasks:
            pdf.add_rect(90, y - 2, 7, 7, 0.5, 0.3)
            pdf.add_text(103, y, task, 'F1', 9)
            y -= 14
        y -= 8

    # Vendor Comparison page
    pdf.new_page()
    pdf.add_centered_text(750, "VENDOR COMPARISON", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    pdf.add_text(72, 715, "Category: _________________________", 'F1', 11)
    comp_headers = ["Criteria", "Vendor 1", "Vendor 2", "Vendor 3"]
    xs_c = [72, 200, 320, 440]
    y = 690
    for i, h in enumerate(comp_headers):
        pdf.add_text(xs_c[i], y, h, 'F2', 9)
    y -= 18
    criteria = ["Name", "Price", "Availability", "Style/Quality", "Reviews", "Includes", "Cancellation", "Travel fee", "Experience", "Gut feeling"]
    for c in criteria:
        pdf.add_text(72, y, c, 'F1', 9)
        for x in xs_c[1:]:
            pdf.add_line(x, y - 2, x + 100, y - 2, 0.5, 0.5)
        y -= 25
    pdf.add_text(72, y - 10, "CHOSEN VENDOR: ___________________________", 'F2', 11)
    pdf.add_text(72, y - 30, "Reason: ___________________________________________________", 'F1', 10)

    # Day-of Timeline
    pdf.new_page()
    pdf.add_centered_text(750, "DAY-OF TIMELINE", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    pdf.add_text(72, 715, "Wedding Date: ___/___/______", 'F1', 11)
    y = 690
    pdf.add_text(72, y, "Time", 'F2', 9)
    pdf.add_text(140, y, "Activity", 'F2', 9)
    pdf.add_text(400, y, "Person Responsible", 'F2', 9)
    y -= 18
    for _ in range(25):
        pdf.add_line(72, y, 130, y, 0.5, 0.5)
        pdf.add_line(140, y, 390, y, 0.5, 0.5)
        pdf.add_line(400, y, 540, y, 0.5, 0.5)
        y -= 22

    # Emergency Contacts
    pdf.new_page()
    pdf.add_centered_text(750, "EMERGENCY CONTACTS", 'F2', 16)
    pdf.add_line(72, 740, 540, 740, 1, 0.3)
    contacts = [
        "Wedding Planner/Coordinator", "Maid of Honor", "Best Man",
        "Venue Manager", "Caterer", "Photographer", "DJ/Band",
        "Florist", "Transportation", "Hair Stylist", "Makeup Artist",
        "Officiant", "Baker/Cake", "Emergency Contact (Family)"
    ]
    y = 715
    for contact in contacts:
        pdf.add_text(72, y, f"{contact}:", 'F2', 9)
        y -= 15
        pdf.add_text(90, y, "Name:", 'F1', 8)
        pdf.add_line(125, y - 2, 280, y - 2, 0.5, 0.5)
        pdf.add_text(290, y, "Phone:", 'F1', 8)
        pdf.add_line(325, y - 2, 540, y - 2, 0.5, 0.5)
        y -= 22

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book84_Wedding_Budget_Planner.pdf')
    print("Book84_Wedding_Budget_Planner.pdf created successfully!")

if __name__ == "__main__":
    create_book()
