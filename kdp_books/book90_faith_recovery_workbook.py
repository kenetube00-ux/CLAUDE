"""Book 90: Faith-Based Addiction Recovery Workbook"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"
    
    # Recovery-focused scriptures
    scriptures = [
        "2 Corinthians 5:17 - If anyone is in Christ, the new creation has come; the old has gone.",
        "Philippians 4:13 - I can do all things through Christ who strengthens me.",
        "Isaiah 43:18-19 - Forget the former things; see, I am doing a new thing!",
        "Romans 6:6 - Our old self was crucified with him so that the body ruled by sin might be done away with.",
        "Psalm 51:10 - Create in me a pure heart, O God, and renew a steadfast spirit within me.",
        "1 Corinthians 10:13 - God is faithful; he will not let you be tempted beyond what you can bear.",
        "James 4:7 - Submit yourselves to God. Resist the devil, and he will flee from you.",
        "Romans 8:1 - There is now no condemnation for those who are in Christ Jesus.",
        "Galatians 5:1 - It is for freedom that Christ has set us free. Stand firm.",
        "Psalm 40:2 - He lifted me out of the slimy pit and set my feet on a rock.",
        "Isaiah 40:29 - He gives strength to the weary and increases the power of the weak.",
        "Jeremiah 29:11 - For I know the plans I have for you, declares the Lord, plans to prosper you.",
        "Romans 12:2 - Be transformed by the renewing of your mind.",
        "Psalm 107:14 - He brought them out of darkness and the deepest gloom and broke away their chains.",
        "John 8:36 - So if the Son sets you free, you will be free indeed.",
        "1 Peter 5:10 - The God of all grace will himself restore you and make you strong.",
        "Psalm 34:17 - The righteous cry out, and the Lord hears them; he delivers them from all troubles.",
        "Ephesians 6:10 - Be strong in the Lord and in his mighty power.",
        "Lamentations 3:22-23 - His mercies are new every morning; great is your faithfulness.",
        "2 Timothy 1:7 - God has not given us a spirit of fear, but of power, love, and a sound mind.",
        "Psalm 18:2 - The Lord is my rock, my fortress and my deliverer.",
        "Isaiah 41:13 - For I am the Lord your God who takes hold of your right hand.",
        "Romans 8:37 - In all these things we are more than conquerors through him who loved us.",
        "Psalm 32:7 - You are my hiding place; you will protect me from trouble.",
        "Proverbs 3:5-6 - Trust in the Lord with all your heart and lean not on your own understanding.",
        "Matthew 11:28 - Come to me, all you who are weary and burdened, and I will give you rest.",
        "Hebrews 12:1 - Let us throw off everything that hinders and the sin that so easily entangles.",
        "Psalm 103:12 - As far as the east is from the west, so far has he removed our sins from us.",
        "Micah 7:8 - Though I have fallen, I will rise. Though I sit in darkness, the Lord will be my light.",
        "Revelation 21:5 - He who was seated on the throne said, Behold, I am making all things new.",
    ]
    
    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.1)
    pdf.add_centered_text(430, "REDEEMED", 'F5', 28, 1)
    pdf.add_centered_text(385, "A Faith-Based Addiction", 'F4', 15, 0.9)
    pdf.add_centered_text(365, "Recovery Workbook", 'F4', 15, 0.9)

    pdf.add_centered_text(320, "30 Days of Scripture, Prayer & Accountability", 'F1', 10, 0.8)
    pdf.add_centered_text(300, "You are not your past. You are God's new creation.", 'F4', 9, 0.7)
    pdf.add_centered_text(180, author, 'F2', 12, 0.9)
    
    # Copyright page
    pdf.new_page()
    pdf.add_centered_text(430, "Redeemed: A Faith-Based Addiction Recovery Workbook", 'F2', 10)
    pdf.add_centered_text(408, f"Copyright 2024 {author}. All rights reserved.", 'F1', 9)
    pdf.add_centered_text(388, "No part of this book may be reproduced without permission.", 'F1', 8)
    pdf.add_centered_text(365, "This workbook is a companion to - not a replacement for -", 'F1', 8)
    pdf.add_centered_text(350, "professional addiction treatment and support groups.", 'F1', 8)
    pdf.add_centered_text(325, "If you are in crisis, call SAMHSA: 1-800-662-4357", 'F2', 8)
    pdf.add_centered_text(295, "Dear warrior,", 'F4', 10)
    pdf.add_centered_text(278, "The fact that you are holding this book means you are choosing", 'F4', 8)
    pdf.add_centered_text(265, "life. God sees your struggle and He is not ashamed of you.", 'F4', 8)
    pdf.add_centered_text(250, "Recovery is not a straight line - it is a daily decision.", 'F4', 8)
    pdf.add_centered_text(235, "Let this workbook walk with you, one day at a time.", 'F4', 8)
    pdf.add_centered_text(210, "You are redeemed. You are loved. You are not alone.", 'F2', 9)

    # 30 Daily Pages
    for day in range(1, 31):
        pdf.new_page()
        scripture_idx = (day - 1) % 30
        verse = scriptures[scripture_idx]
        
        # Header
        pdf.add_filled_rect(25, 610, 382, 20, 0.88)
        pdf.add_text(32, 615, f"DAY {day}", 'F2', 10)
        pdf.add_text(150, 615, "Date: ___/___/___", 'F1', 8)
        pdf.add_text(285, 615, "Days sober: _____", 'F2', 8)
        
        # Morning prayer
        y = 595
        pdf.add_text(32, y, "Morning Prayer:", 'F2', 8)
        y -= 13
        for _ in range(2):
            pdf.add_line(32, y, 400, y, 0.5, 0.5)
            y -= 13
        
        y -= 6
        # Scripture
        pdf.add_text(32, y, "Scripture for today:", 'F2', 8)
        y -= 12
        words = verse.split()
        lines = []
        current = ""
        for w in words:
            if len(current + " " + w) > 58:
                lines.append(current)
                current = w
            else:
                current = current + " " + w if current else w
        if current:
            lines.append(current)
        for line in lines:
            pdf.add_text(32, y, line, 'F4', 8)
            y -= 11
        
        y -= 8
        # Trigger risk
        pdf.add_text(32, y, "Today's trigger risk level (1-10): _____", 'F2', 8)
        y -= 16
        
        # Plan to stay strong
        pdf.add_text(32, y, "My plan to stay strong today:", 'F2', 8)
        y -= 13
        pdf.add_line(32, y, 400, y, 0.5, 0.5)
        y -= 13
        pdf.add_line(32, y, 400, y, 0.5, 0.5)
        
        y -= 16
        # People I can call
        pdf.add_text(32, y, "People I can call:", 'F2', 8)
        y -= 12
        pdf.add_text(32, y, "1.", 'F1', 8)
        pdf.add_line(45, y - 2, 200, y - 2, 0.5, 0.5)
        pdf.add_text(210, y, "2.", 'F1', 8)
        pdf.add_line(223, y - 2, 400, y - 2, 0.5, 0.5)
        
        y -= 16
        # Gratitude
        pdf.add_text(32, y, "I am grateful for:", 'F2', 8)
        y -= 12
        for i in range(3):
            pdf.add_text(32, y, f"{i+1}.", 'F1', 8)
            pdf.add_line(45, y - 2, 400, y - 2, 0.5, 0.5)
            y -= 13
        
        y -= 8
        # Service
        pdf.add_text(32, y, "How I served others today:", 'F2', 8)
        y -= 12
        pdf.add_line(32, y, 400, y, 0.5, 0.5)
        
        y -= 16
        # Evening check-in
        pdf.add_text(32, y, "Evening Check-In:", 'F2', 8)
        y -= 13
        checkins = ["Attended meeting?  Y / N", "Prayed today?  Y / N", "Reached out to someone?  Y / N"]
        for ci in checkins:
            pdf.add_text(45, y, ci, 'F1', 8)
            y -= 12
        
        y -= 10
        # Tomorrow
        pdf.add_text(32, y, "Tomorrow I commit to:", 'F2', 8)
        pdf.add_line(160, y - 2, 400, y - 2, 0.5, 0.5)

    # Milestone Pages
    milestones = [
        ("24 HOURS", "You made it through your first day. This is HUGE."),
        ("1 WEEK", "Seven days of choosing life. God is strengthening you."),
        ("30 DAYS", "A full month! Your body and mind are healing."),
        ("90 DAYS", "Three months of freedom. You are building a new life."),
        ("6 MONTHS", "Half a year redeemed. Look how far you've come."),
        ("1 YEAR", "365 days. You are living proof of God's faithfulness."),
    ]
    for milestone, message in milestones:
        pdf.new_page()
        pdf.add_filled_rect(25, 400, 382, 180, 0.9)
        pdf.add_centered_text(560, "MILESTONE CELEBRATION", 'F2', 14)
        pdf.add_centered_text(520, milestone, 'F2', 22)
        pdf.add_centered_text(480, message, 'F4', 10)
        pdf.add_text(40, 440, "Date achieved: ___/___/______", 'F1', 9)
        pdf.add_text(40, 418, "How I feel:", 'F1', 9)
        pdf.add_line(40, 404, 395, 404, 0.5, 0.5)
        pdf.add_text(40, 370, "What God has done in my life:", 'F1', 9)
        pdf.add_line(40, 356, 395, 356, 0.5, 0.5)
        pdf.add_line(40, 340, 395, 340, 0.5, 0.5)
        pdf.add_text(40, 310, "Who I want to thank:", 'F1', 9)
        pdf.add_line(40, 296, 395, 296, 0.5, 0.5)
        pdf.add_text(40, 270, "My prayer of gratitude:", 'F1', 9)
        pdf.add_line(40, 256, 395, 256, 0.5, 0.5)
        pdf.add_line(40, 240, 395, 240, 0.5, 0.5)


    # Relapse Prevention Plan
    pdf.new_page()
    pdf.add_centered_text(610, "RELAPSE PREVENTION PLAN", 'F2', 14)
    pdf.add_line(30, 600, 400, 600, 1, 0.3)
    y = 580
    rp_fields = [
        ("My triggers (people, places, emotions):", 4),
        ("Warning signs that I'm struggling:", 3),
        ("My healthy coping strategies:", 4),
        ("Scriptures I hold onto:", 3),
        ("People I will call before I use:", 3),
        ("Meetings I attend (day/time/location):", 3),
        ("If I relapse, I will immediately:", 3),
    ]
    for label, lines in rp_fields:
        pdf.add_text(32, y, label, 'F2', 8)
        y -= 12
        for _ in range(lines):
            pdf.add_line(32, y, 400, y, 0.5, 0.5)
            y -= 12
        y -= 6

    # My Support Network
    pdf.new_page()
    pdf.add_centered_text(610, "MY SUPPORT NETWORK", 'F2', 14)
    pdf.add_line(30, 600, 400, 600, 1, 0.3)
    y = 580
    network = [
        ("Sponsor:", "Name:", "Phone:"),
        ("Counselor/Therapist:", "Name:", "Phone:"),
        ("Pastor:", "Name:", "Phone:"),
        ("Accountability Partner 1:", "Name:", "Phone:"),
        ("Accountability Partner 2:", "Name:", "Phone:"),
        ("Family Support:", "Name:", "Phone:"),
        ("Crisis Hotline:", "SAMHSA:", "1-800-662-4357"),
        ("Meeting Group:", "Day/Time:", "Location:"),
    ]
    for role, field1, field2 in network:
        pdf.add_text(32, y, role, 'F2', 9)
        y -= 14
        pdf.add_text(45, y, field1, 'F1', 8)
        pdf.add_line(80, y - 2, 220, y - 2, 0.5, 0.5)
        pdf.add_text(230, y, field2, 'F1', 8)
        pdf.add_line(265, y - 2, 400, y - 2, 0.5, 0.5)
        y -= 20
    y -= 15
    pdf.add_text(32, y, "God is ALWAYS in my network. He never sleeps. He never gives up on me.", 'F4', 8)

    # Letter to My Future Sober Self
    pdf.new_page()
    pdf.add_centered_text(610, "LETTER TO MY FUTURE SOBER SELF", 'F2', 13)
    pdf.add_line(30, 600, 400, 600, 1, 0.3)
    pdf.add_text(32, 580, "Write this on a hard day. Read it on harder days.", 'F4', 9)
    pdf.add_text(32, 560, "Dear future me,", 'F4', 10)
    y = 545
    for _ in range(28):
        pdf.add_line(32, y, 400, y, 0.5, 0.5)
        y -= 16
    pdf.add_text(32, y, "With hope and love, me on ___/___/______", 'F4', 9)

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book90_Faith_Recovery_Workbook.pdf')
    print("Book90_Faith_Recovery_Workbook.pdf created successfully!")

if __name__ == "__main__":
    create_book()
