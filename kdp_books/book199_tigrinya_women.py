"""Book 199: STRONG IN FAITH - A Women's Devotional (Tigrinya-English)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)
    author = "Daniel Tesfamariam"

    # Title page
    pdf.add_filled_rect(0, 0, 432, 648, 0.93)
    pdf.add_centered_text(500, "STRONG IN FAITH", 'F2', 22)
    pdf.add_centered_text(472, "A Women's Devotional", 'F4', 14, 0.2)
    pdf.add_centered_text(448, "(Tigrinya-English)", 'F1', 12, 0.3)
    pdf.add_centered_text(400, "28 Daily Devotions for Women of God", 'F1', 11, 0.3)
    pdf.add_centered_text(180, f"By {author}", 'F2', 12, 0.2)

    # Copyright page
    pdf.new_page()
    pdf.add_text(50, 580, "STRONG IN FAITH - A Women's Devotional", 'F2', 11)
    pdf.add_text(50, 560, f"By {author}", 'F1', 10)
    pdf.add_text(50, 535, "Copyright 2025. All rights reserved.", 'F1', 9)
    pdf.add_text(50, 515, "Scripture from World English Bible (WEB)", 'F1', 9)
    pdf.add_text(50, 490, "Published by KIDLYTICAL Books", 'F1', 9)

    # 28 daily devotions
    devotions = [
        ("Strength", "Proverbs 31:25", "She is clothed with strength and dignity, and she laughs at the days to come.", "How does God clothe you with strength today as a woman?"),
        ("Wisdom", "James 1:5", "If any of you lacks wisdom, let him ask of God who gives generously.", "What decision do you need God's wisdom for right now?"),
        ("Love", "1 Corinthians 13:4", "Love is patient and kind. Love does not envy or boast.", "How can you show patient love in your relationships today?"),
        ("Peace", "John 14:27", "Peace I leave with you. My peace I give to you.", "Where do you need God's peace in your life right now?"),
        ("Hope", "Romans 15:13", "May the God of hope fill you with all joy and peace in believing.", "What are you hoping for? Bring it to God."),
        ("Patience", "Psalm 27:14", "Wait for the LORD. Be strong and let your heart take courage.", "What are you waiting on God for? How can you wait well?"),
        ("Joy", "Nehemiah 8:10", "The joy of the LORD is your strength.", "Find three things to be joyful about today."),
        ("Motherhood", "Psalm 127:3", "Children are a heritage from the LORD.", "How is God using your role to shape the next generation?"),
        ("Marriage", "Ecclesiastes 4:9", "Two are better than one; they have a good reward for their labor.", "How can you strengthen your marriage through prayer?"),
        ("Work", "Colossians 3:23", "Whatever you do, work heartily, as for the Lord.", "How can you honor God in your work today?"),
        ("Identity", "Psalm 139:14", "I am fearfully and wonderfully made.", "Write down three truths God says about who you are."),
        ("Community", "Hebrews 10:24-25", "Let us consider how to stir one another up to love and good works.", "Who can you encourage today?"),
        ("Strength", "Isaiah 41:10", "Fear not, for I am with you. Be not dismayed, for I am your God.", "What fear is holding you back? Give it to God."),
        ("Wisdom", "Proverbs 2:6", "For the LORD gives wisdom. From his mouth come knowledge and understanding.", "Ask God to show you His perspective on your situation."),
        ("Love", "1 John 4:19", "We love because he first loved us.", "How has God's love changed the way you love others?"),
        ("Peace", "Philippians 4:7", "The peace of God which surpasses all understanding will guard your hearts.", "What anxiety can you release to God right now?"),
        ("Hope", "Jeremiah 29:11", "For I know the plans I have for you, declares the LORD.", "Trust God's plan even when you cannot see the path."),
        ("Patience", "Galatians 6:9", "Let us not be weary in doing good, for we will reap if we do not give up.", "Where do you need perseverance in your life?"),
        ("Joy", "Psalm 16:11", "In your presence there is fullness of joy.", "Spend time in God's presence and let His joy fill you."),
        ("Motherhood", "Proverbs 22:6", "Train up a child in the way he should go.", "Pray specifically for each child in your care today."),
        ("Marriage", "Ephesians 5:33", "Let each wife respect her husband.", "How can you build up your husband with your words?"),
        ("Work", "Proverbs 31:17", "She girds herself with strength and makes her arms strong.", "You are capable. What will you accomplish today?"),
        ("Identity", "2 Corinthians 5:17", "If anyone is in Christ, she is a new creation.", "Your past does not define you. God has made you new."),
        ("Community", "Proverbs 27:17", "Iron sharpens iron, so one person sharpens another.", "Reach out to a sister in faith today."),
        ("Strength", "2 Corinthians 12:9", "My grace is sufficient for you, for my power is made perfect in weakness.", "In your weakness, God is strong. Rest in that."),
        ("Wisdom", "Proverbs 3:13", "Happy is the woman who finds wisdom.", "What has God been teaching you this month?"),
        ("Love", "Romans 8:38-39", "Nothing can separate us from the love of God.", "You are loved completely. Nothing can change that."),
        ("Peace", "Isaiah 26:3", "You will keep in perfect peace the one whose mind is fixed on you.", "Fix your mind on God today and find His peace."),
    ]

    for day, (theme, ref, verse, prompt) in enumerate(devotions, 1):
        pdf.new_page()
        pdf.add_filled_rect(40, 596, 352, 32, 0.88)
        pdf.add_centered_text(608, f"DAY {day} - {theme.upper()}", 'F2', 13)
        pdf.add_centered_text(580, ref, 'F5', 11)
        pdf.add_line(50, 572, 382, 572, 0.5, 0.6)

        # English scripture
        pdf.add_text(50, 552, "Scripture:", 'F2', 10)
        words = verse.split()
        line = ""
        y = 536
        for w in words:
            if len(line + " " + w) > 55:
                pdf.add_text(50, y, line, 'F4', 10)
                y -= 14
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(50, y, line, 'F4', 10)
            y -= 14

        # Tigrinya placeholder
        y -= 8
        pdf.add_text(50, y, "Tigrinya:", 'F2', 10)
        y -= 14
        pdf.add_text(50, y, "[Tigrinya scripture text here]", 'F3', 9, 0.4)

        # Reflection
        y -= 30
        pdf.add_text(50, y, "Reflection:", 'F2', 10)
        y -= 16
        # Wrap prompt
        words = prompt.split()
        line = ""
        for w in words:
            if len(line + " " + w) > 55:
                pdf.add_text(60, y, line, 'F1', 10)
                y -= 14
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            pdf.add_text(60, y, line, 'F1', 10)
            y -= 14

        # Writing lines
        y -= 10
        for _ in range(3):
            y -= 16
            pdf.add_line(50, y, 382, y, 0.5, 0.7)

        # Prayer
        y -= 25
        pdf.add_text(50, y, "My Prayer:", 'F2', 10)
        for _ in range(3):
            y -= 16
            pdf.add_line(50, y, 382, y, 0.5, 0.7)

        # Application
        y -= 25
        pdf.add_text(50, y, "Today I will:", 'F2', 10)
        y -= 16
        pdf.add_line(50, y, 382, y, 0.5, 0.7)

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book199_Tigrinya_Women_Devotional.pdf")
    pdf.save(output)
    print(f"Created: {output}")

if __name__ == "__main__":
    create_book()
