"""Book 302: WOMEN OF THE BIBLE IN STAINED GLASS - Large Print Coloring Book for Seniors"""
import random
from pdf_utils import PDFDoc

random.seed(302)

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    women = [
        ("Eve", "The First Woman", "Genesis 3:20", "Mother of all living. Created by God from Adam's rib to be his companion and equal partner in tending the garden."),
        ("Sarah", "Mother of Nations", "Genesis 21:6", "Abraham's wife who laughed at God's promise but bore Isaac at age 90, proving nothing is impossible with God."),
        ("Hagar", "Seen by God", "Genesis 16:13", "An Egyptian servant who fled into the wilderness and discovered God sees the forgotten and alone."),
        ("Rebekah", "Chosen Bride", "Genesis 24:67", "Showed kindness to a stranger's camels and became the answer to a servant's prayer for Isaac's bride."),
        ("Rachel", "Beloved Wife", "Genesis 29:20", "Jacob worked 14 years for her hand because of his great love. Mother of Joseph and Benjamin."),
        ("Miriam", "Worship Leader", "Exodus 15:20", "Moses' sister who watched over him as a baby and later led Israel's women in worship after the Red Sea crossing."),
        ("Rahab", "Faithful Outsider", "Joshua 2:11", "A Canaanite woman who chose faith over fear, hid Israel's spies, and became part of Jesus' lineage."),
        ("Deborah", "Judge and Leader", "Judges 4:4", "A prophetess who judged Israel and led the nation to military victory with courage and wisdom."),
        ("Ruth", "Loyal Daughter", "Ruth 1:16", "A Moabite widow whose devotion to her mother-in-law Naomi became a story of redemption and love."),
        ("Hannah", "Prayerful Mother", "1 Samuel 1:27", "Prayed desperately for a child, vowed him to God, and became mother of the prophet Samuel."),
        ("Abigail", "Wise Peacemaker", "1 Samuel 25:33", "Intervened with wisdom and humility to prevent David from bloodshed, later becoming his wife."),
        ("Esther", "Brave Queen", "Esther 4:14", "A Jewish orphan who became queen and risked death to save her people: 'for such a time as this.'"),
        ("Naomi", "Redeemed Sufferer", "Ruth 4:14-15", "Lost her husband and sons but was restored through Ruth's loyalty and the birth of grandson Obed."),
        ("Mary, Mother of Jesus", "Favored One", "Luke 1:38", "A young virgin who said 'yes' to God's impossible plan and carried the Savior of the world."),
        ("Elizabeth", "Faithful Waiter", "Luke 1:45", "Barren for decades but blessed in old age with John the Baptist, the forerunner of Christ."),
        ("Anna", "Temple Prophet", "Luke 2:37-38", "An 84-year-old widow who prayed in the temple daily and recognized baby Jesus as the Messiah."),
        ("Mary Magdalene", "Devoted Follower", "John 20:16", "Delivered from seven demons, she became Christ's faithful follower and first witness of the resurrection."),
        ("Martha", "Faithful Server", "John 11:27", "Known for busy serving, she made one of the boldest faith declarations: 'Thou art the Christ.'"),
        ("Mary of Bethany", "Worshipper", "John 12:3", "Anointed Jesus' feet with costly perfume in an extravagant act of worship and devotion."),
        ("The Woman at the Well", "Evangelist", "John 4:29", "A Samaritan outcast who met Jesus at a well and became the first evangelist to her entire town."),
        ("Dorcas/Tabitha", "Charitable Saint", "Acts 9:36", "Known for good works and charity, she was raised from the dead by Peter's prayer."),
        ("Lydia", "First European Convert", "Acts 16:14", "A businesswoman whose heart God opened. She became the first Christian convert in Europe."),
        ("Priscilla", "Teacher", "Acts 18:26", "Alongside her husband Aquila, she taught and mentored leaders in the early church."),
        ("Jochebed", "Brave Mother", "Exodus 2:3", "Moses' mother who defied Pharaoh's order and set her baby afloat to save his life."),
        ("Leah", "Unloved but Blessed", "Genesis 29:35", "Though unloved by Jacob, God blessed her with many children including Judah, ancestor of Jesus."),
        ("The Shunammite Woman", "Generous Host", "2 Kings 4:10", "Built a room for the prophet Elisha and was rewarded with a son, then saw him raised from death."),
        ("Lois and Eunice", "Faith Trainers", "2 Timothy 1:5", "Timothy's grandmother and mother who passed genuine faith to the next generation."),
        ("Phoebe", "Church Servant", "Romans 16:1", "Commended by Paul as a servant of the church and a helper of many."),
        ("The Widow with Two Mites", "Generous Giver", "Mark 12:42-44", "Gave all she had - two small coins - and Jesus said she gave more than all the rich."),
        ("The Virtuous Woman", "Proverbs 31 Woman", "Proverbs 31:30", "A woman who fears the Lord, works diligently, speaks wisdom, and is praised by her family."),
    ]
    
    # Title page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.93)
    doc.add_rect(30, 30, 552, 732, 3, 0.2)
    doc.add_rect(40, 40, 532, 712, 1, 0.5)
    doc.add_centered_text(700, "WOMEN OF THE BIBLE", 'F2', 24, 0.1)
    doc.add_centered_text(670, "IN STAINED GLASS", 'F2', 24, 0.1)
    doc.add_centered_text(635, "Large Print Coloring Book for Seniors", 'F4', 14, 0.3)
    doc.add_filled_rect(120, 350, 372, 200, 0.88)
    doc.add_rect(120, 350, 372, 200, 2, 0.3)
    doc.add_centered_text(500, "[ILLUSTRATION: stained glass window", 'F3', 10, 0.4)
    doc.add_centered_text(485, "depicting woman with flowing robes", 'F3', 10, 0.4)
    doc.add_centered_text(470, "in rich jewel-tone outlines]", 'F3', 10, 0.4)
    doc.add_centered_text(220, "30 Women | 30 Stories | Bold Simple Outlines", 'F1', 11, 0.35)
    doc.add_centered_text(110, author, 'F2', 18, 0.2)
    
    # Copyright
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.97)
    doc.add_rect(50, 50, 512, 692, 1, 0.5)
    doc.add_centered_text(700, "WOMEN OF THE BIBLE IN STAINED GLASS", 'F2', 12, 0.2)
    doc.add_text(72, 640, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 12, 0.2)
    doc.add_text(72, 610, "Scripture from King James Version (Public Domain).", 'F1', 11, 0.3)
    doc.add_text(72, 580, "LARGE PRINT for comfortable reading.", 'F2', 12, 0.2)
    doc.add_text(72, 550, "Bold, simple outlines designed for seniors.", 'F1', 12, 0.3)
    doc.add_text(72, 520, "Published by KDP Amazon", 'F1', 12, 0.3)
    
    # Coloring tips
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "COLORING TIPS FOR STAINED GLASS", 'F2', 16, 0.1)
    y = 680
    tips = [
        "Stained glass coloring is easy and beautiful!",
        "",
        "TIPS FOR BEST RESULTS:",
        "",
        "1. Use BOLD, bright colors - stained glass is vibrant!",
        "",
        "2. Color with even pressure for smooth fills",
        "",
        "3. Leave the thick black outlines uncolored",
        "   (they represent the lead between glass pieces)",
        "",
        "4. Try colored pencils, gel pens, or markers",
        "",
        "5. Don't worry about staying perfectly in the lines",
        "",
        "6. Consider using metallic gold/silver for borders",
        "",
        "7. Work in good lighting for comfortable coloring",
        "",
        "SUGGESTED TOOLS:",
        "  - Colored pencils (easiest to control)",
        "  - Gel pens (vibrant colors)",
        "  - Fine-tip markers (bold effect)",
    ]
    for line in tips:
        if line.startswith("TIPS") or line.startswith("SUGGESTED") or line.startswith("Stained"):
            doc.add_text(72, y, line, 'F2', 14, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 14, 0.25)
        y -= 22
    
    # Intro page
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.94)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(720, "ABOUT THIS BOOK", 'F2', 16, 0.1)
    y = 680
    about = [
        "The Bible is full of remarkable women.",
        "",
        "Women of faith, courage, wisdom, and strength.",
        "Women who changed history, saved nations,",
        "raised leaders, and walked with God.",
        "",
        "This coloring book honors 30 of these women",
        "in beautiful stained glass style artwork.",
        "",
        "Each woman has TWO pages:",
        "  1. A COLORING PAGE in stained glass style",
        "     with bold, simple outlines",
        "  2. A STORY PAGE with her name, verse,",
        "     and a brief biography in LARGE PRINT",
        "",
        "Color at your own pace. Read her story.",
        "Let these women of faith inspire your own.",
    ]
    for line in about:
        if line.startswith("The Bible") or line.startswith("Color"):
            doc.add_text(72, y, line, 'F5', 14, 0.1)
        else:
            doc.add_text(72, y, line, 'F4', 14, 0.25)
        y -= 24
    
    # 30 women - coloring + story
    for i, (name, title, ref, bio) in enumerate(women):
        # Coloring page
        doc.new_page()
        fill = 0.95 + random.uniform(0, 0.02)
        doc.add_filled_rect(0, 0, 612, 792, fill)
        # Stained glass border (thick lines)
        doc.add_rect(20, 20, 572, 752, 4, 0.1)
        doc.add_rect(30, 30, 552, 732, 2, 0.2)
        # Inner stained glass panels
        doc.add_line(30, 680, 582, 680, 3, 0.15)
        doc.add_line(30, 100, 582, 100, 3, 0.15)
        # Arch at top
        doc.add_line(156, 762, 156, 680, 2, 0.15)
        doc.add_line(306, 762, 306, 680, 2, 0.15)
        doc.add_line(456, 762, 456, 680, 2, 0.15)
        
        doc.add_centered_text(730, name.upper(), 'F2', 16, 0.1)
        doc.add_centered_text(700, title, 'F4', 12, 0.3)
        
        # Main illustration area
        doc.add_filled_rect(60, 140, 492, 520, 0.97)
        doc.add_rect(60, 140, 492, 520, 3, 0.1)
        # Stained glass sections
        doc.add_line(306, 140, 306, 660, 2, 0.15)
        doc.add_line(60, 400, 552, 400, 2, 0.15)
        doc.add_centered_text(500, f"[ILLUSTRATION: Stained glass depiction of {name}", 'F3', 10, 0.3)
        doc.add_centered_text(480, f"in bold simple outlines suitable for coloring.", 'F3', 10, 0.3)
        doc.add_centered_text(460, f"Scene from her story: {title}]", 'F3', 10, 0.3)
        
        # Bottom panel
        doc.add_centered_text(60, ref, 'F4', 12, 0.3)
        
        # Story page
        doc.new_page()
        fill2 = 0.93 + random.uniform(0, 0.04)
        doc.add_filled_rect(0, 0, 612, 792, fill2)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        
        doc.add_centered_text(720, name.upper(), 'F2', 22, 0.1)
        doc.add_centered_text(690, title, 'F4', 16, 0.25)
        doc.add_centered_text(660, ref, 'F1', 14, 0.35)
        doc.add_line(150, 650, 462, 650, 1, 0.4)
        
        # Bio in large print
        y = 620
        words = bio.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) > 45:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        for ln in lines:
            doc.add_text(72, y, ln, 'F4', 16, 0.2)
            y -= 28
        
        y -= 30
        doc.add_text(72, y, "WHAT WE LEARN FROM HER:", 'F2', 14, 0.15)
        y -= 28
        lessons = {
            "Eve": "God created women with purpose and dignity.",
            "Sarah": "God keeps His promises, even when they seem impossible.",
            "Hagar": "God sees those the world forgets.",
            "Rebekah": "Small acts of kindness can change your destiny.",
            "Rachel": "God's timing is worth waiting for.",
            "Miriam": "Worship is our response to God's faithfulness.",
            "Rahab": "Faith can change your entire family line.",
            "Deborah": "God calls women to lead with courage.",
            "Ruth": "Loyalty and love are rewarded by God.",
            "Hannah": "Desperate prayers reach God's ears.",
        }
        lesson = lessons.get(name, "Her faith inspires us to trust God in every season.")
        doc.add_text(72, y, lesson, 'F4', 14, 0.25)
    
    # Bonus: All 30 women summary
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "ALL 30 WOMEN AT A GLANCE", 'F2', 14, 0.1)
    y = 705
    for nm, title, ref, _ in women[:15]:
        doc.add_text(72, y, f"{nm} - {title} ({ref})", 'F1', 9, 0.3)
        y -= 16
    
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.92)
    doc.add_rect(40, 40, 532, 712, 2, 0.3)
    doc.add_centered_text(730, "ALL 30 WOMEN (continued)", 'F2', 14, 0.1)
    y = 705
    for nm, title, ref, _ in women[15:]:
        doc.add_text(72, y, f"{nm} - {title} ({ref})", 'F1', 9, 0.3)
        y -= 16
    
    # Extra pages to reach 72+
    extras_302 = ["MY FAVORITE WOMEN OF FAITH", "COLORING NOTES", "PRAYERS INSPIRED BY THESE WOMEN",
                  "WOMEN OF FAITH IN MY LIFE", "LESSONS I LEARNED", "MY FAITH STORY"]
    for et in extras_302:
        doc.new_page()
        doc.add_filled_rect(0, 0, 612, 792, 0.93)
        doc.add_rect(40, 40, 532, 712, 2, 0.3)
        doc.add_centered_text(730, et, 'F2', 14, 0.1)
        doc.add_line(130, 725, 482, 725, 1, 0.4)
        y = 695
        for _ in range(28):
            doc.add_line(72, y, 540, y, 0.5, 0.6)
            y -= 22

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book302_Stained_Glass_Women_Bible.pdf')
    print("Book302_Stained_Glass_Women_Bible.pdf created successfully!")

if __name__ == "__main__":
    create_book()
