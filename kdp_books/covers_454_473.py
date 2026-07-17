import sys, os
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

os.makedirs('/projects/sandbox/CLAUDE/BOOK_COVERS', exist_ok=True)

# Square children's book covers for Books 454-473
covers = [
    (454, "Daniel_Kindness_Bible", "Bible Stories\nAbout Kindness", "15 Tales of Love and Compassion", ["15 Kindness Stories","Bible Characters","Ages 3-7","Bedtime Prayers","Illustration Placeholders"], 0.18),
    (455, "Daniel_Courage_Bible", "Bible Stories\nAbout Courage", "15 Tales of Bravery for Little Hearts", ["15 Courage Stories","Bible Heroes","Ages 3-7","Bedtime Prayers","Read-Aloud Format"], 0.14),
    (456, "Daniel_Faith_Bible", "Bible Stories\nAbout Faith", "15 Tales of Trust and Belief", ["15 Faith Stories","Scripture Based","Ages 3-7","Bedtime Prayers","Family Devotional"], 0.22),
    (457, "Daniel_Love_Bible", "Bible Stories\nAbout Love", "15 Tales of God's Amazing Love", ["15 Love Stories","God's Character","Ages 2-6","Bedtime Prayers","Gentle & Calming"], 0.16),
    (458, "Daniel_Prayer_Bible", "Bible Stories\nAbout Prayer", "15 Powerful Prayer Stories", ["15 Prayer Stories","Models of Prayer","Ages 3-7","Guided Prayers","Scripture Memory"], 0.20),
    (459, "Daniel_Forgiveness_Bible", "Bible Stories About\nForgiveness", "15 Tales of Grace and Mercy", ["15 Forgiveness Tales","Grace Lessons","Ages 4-8","Bedtime Prayers","Heart Healing"], 0.25),
    (460, "Daniel_Worship_Bible", "Bible Stories\nAbout Worship", "15 Tales of Praise and Joy", ["15 Worship Stories","Songs of Praise","Ages 3-7","Bedtime Prayers","Joyful Spirit"], 0.13),
    (461, "Daniel_Obedience_Bible", "Bible Stories About\nObedience", "15 Tales of Following God", ["15 Obedience Stories","God's Commands","Ages 3-7","Bedtime Prayers","Character Building"], 0.28),
    (462, "Daniel_Bible_Kings", "Kings of\nthe Bible", "15 Stories of Rulers and Kingdoms", ["15 King Stories","Power & Humility","Ages 4-8","Bedtime Prayers","Leadership Lessons"], 0.15),
    (463, "Daniel_Bible_Prophets", "Prophets of\nthe Bible", "15 Messengers God Sent", ["15 Prophet Stories","God's Messengers","Ages 4-8","Bedtime Prayers","Hearing God's Voice"], 0.30),
    (464, "Daniel_Bible_Promises", "God's Promises\nfor Kids", "15 Unbreakable Promises", ["15 Promises","Never Broken","Ages 3-7","Bedtime Prayers","Memory Verses"], 0.12),
    (465, "Daniel_Bible_Helpers", "Helpers in\nthe Bible", "15 Stories of Servants", ["15 Helper Stories","Serving Others","Ages 3-7","Bedtime Prayers","Kindness in Action"], 0.24),
    (466, "Daniel_Bedtime_Blessings", "Bedtime Blessings\nfrom the Bible", "30 Nighttime Scriptures", ["30 Blessings","Calming Scriptures","Ages 1-4","Nighttime Prayers","Sweet Dreams"], 0.17),
    (467, "Daniel_Bible_Adventures", "Bible Adventures\nfor Kids", "15 Exciting Journeys of Faith", ["15 Adventures","Action Packed","Ages 4-8","Bedtime Prayers","Exciting Faith"], 0.21),
    (468, "Daniel_Bible_Joy", "Bible Stories\nAbout Joy", "15 Tales of Happiness from God", ["15 Joy Stories","God's Happiness","Ages 3-7","Bedtime Prayers","Cheerful Spirit"], 0.14),
    (469, "Daniel_Bible_Peace", "Bible Stories\nAbout Peace", "15 Calming Tales from Scripture", ["15 Peace Stories","Calm & Still","Ages 2-6","Bedtime Prayers","Restful Sleep"], 0.19),
    (470, "Daniel_Bible_Patience", "Bible Stories About\nPatience", "15 Tales of Waiting on God", ["15 Patience Stories","God's Timing","Ages 3-7","Bedtime Prayers","Trust & Wait"], 0.26),
    (471, "Daniel_Bible_Sharing", "Bible Stories About\nSharing", "15 Tales of Generosity", ["15 Sharing Stories","Generosity","Ages 2-6","Bedtime Prayers","Giving Hearts"], 0.15),
    (472, "Daniel_Bible_Friendship", "Bible Stories About\nFriendship", "15 Tales of Godly Friends", ["15 Friendship Tales","True Friends","Ages 3-7","Bedtime Prayers","Loyal Love"], 0.23),
    (473, "Daniel_Bible_Thankfulness", "Bible Stories About\nThankfulness", "15 Tales of Gratitude", ["15 Gratitude Tales","Thankful Hearts","Ages 2-6","Bedtime Prayers","Praise & Thanks"], 0.16),
]

def create_cover(book_num, filename, title, subtitle, features, accent_gray):
    pdf = PDFDoc(width=612, height=612)  # 8.5x8.5 square
    pdf.new_page()
    
    # Background
    pdf.add_filled_rect(0, 0, 612, 612, gray=0.94)
    # Top accent band
    pdf.add_filled_rect(0, 420, 612, 192, gray=accent_gray)
    # Double border
    pdf.add_rect(15, 15, 582, 582, line_width=2.5, gray=0.25)
    pdf.add_rect(22, 22, 568, 568, line_width=0.8, gray=0.45)
    # Series banner
    pdf.add_filled_rect(150, 585, 312, 18, gray=0.25)
    pdf.add_text(160, 589, "Bible Made Simple Kids Series", font='F1', size=9, gray=0.9)
    # Decorative stars
    pdf.add_text(45, 560, "*", font='F2', size=18, gray=0.35)
    pdf.add_text(545, 565, "*", font='F2', size=14, gray=0.35)
    pdf.add_text(70, 440, "*", font='F2', size=12, gray=0.4)
    pdf.add_text(525, 445, "*", font='F2', size=10, gray=0.4)
    pdf.add_text(50, 100, "*", font='F2', size=10, gray=0.35)
    pdf.add_text(540, 90, "*", font='F2', size=14, gray=0.35)
    
    # Title
    tlines = title.split('\n')
    ty = 555 if len(tlines) <= 2 else 565
    for i, tl in enumerate(tlines):
        yp = ty - i*38
        if accent_gray < 0.20:
            pdf.add_centered_text(yp, tl, font='F2', size=28, gray=0.95)
        else:
            pdf.add_centered_text(yp, tl, font='F2', size=28, gray=0.0)
    
    # Subtitle
    if accent_gray < 0.20:
        pdf.add_centered_text(430, subtitle, font='F4', size=12, gray=0.8)
    else:
        pdf.add_centered_text(430, subtitle, font='F4', size=12, gray=0.1)
    
    # Divider
    pdf.add_line(150, 405, 462, 405, width=1.5, gray=0.35)
    
    # Features
    pdf.add_centered_text(380, "Inside This Book:", font='F2', size=10, gray=0.25)
    for i, feat in enumerate(features):
        y = 355 - i*24
        pdf.add_text(175, y, "*", font='F2', size=10, gray=0.3)
        pdf.add_text(192, y, feat, font='F1', size=10, gray=0.18)
    
    # Bottom band
    pdf.add_filled_rect(0, 30, 612, 55, gray=accent_gray)
    # Author
    if accent_gray < 0.20:
        pdf.add_centered_text(52, "DANIEL TESFAMARIAM", font='F2', size=15, gray=0.95)
    else:
        pdf.add_centered_text(52, "DANIEL TESFAMARIAM", font='F2', size=15, gray=0.0)
    
    # Corner decorations
    pdf.add_line(30, 580, 60, 580, width=1.5, gray=0.35)
    pdf.add_line(30, 580, 30, 550, width=1.5, gray=0.35)
    pdf.add_line(552, 580, 582, 580, width=1.5, gray=0.35)
    pdf.add_line(582, 580, 582, 550, width=1.5, gray=0.35)
    pdf.add_line(30, 95, 60, 95, width=1.5, gray=0.35)
    pdf.add_line(30, 95, 30, 125, width=1.5, gray=0.35)
    pdf.add_line(552, 95, 582, 95, width=1.5, gray=0.35)
    pdf.add_line(582, 95, 582, 125, width=1.5, gray=0.35)
    
    # Book number + tagline
    pdf.add_text(540, 35, f"#{book_num}", font='F3', size=7, gray=0.5)
    pdf.add_centered_text(110, "Planting Seeds of Faith in Young Hearts", font='F4', size=9, gray=0.4)
    
    # Age badge
    age_text = [f for f in features if "Ages" in f]
    if age_text:
        pdf.add_filled_rect(480, 95, 90, 22, gray=0.25)
        pdf.add_text(490, 99, age_text[0], font='F2', size=9, gray=0.9)
    
    output = f"/projects/sandbox/CLAUDE/BOOK_COVERS/Cover{book_num}_{filename}.pdf"
    pdf.save(output)
    return output

print("=" * 70)
print("GENERATING COVERS FOR BOOKS 454-473 (Daniel Tesfamariam)")
print("=" * 70)

for data in covers:
    path = create_cover(*data)
    size = os.path.getsize(path)
    print(f"  Cover {data[0]}: {data[2].split(chr(10))[0][:35]:<37} ({size:,} bytes)")

print(f"\n{'=' * 70}")
print(f"ALL 20 COVERS CREATED SUCCESSFULLY!")
print("=" * 70)
