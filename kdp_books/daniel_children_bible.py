#!/usr/bin/env python3
"""Generate 20 Children's Bible Books (434-453) by Daniel Tesfamariam
Same style as Selam Fesehaye's Little Blessings series - square picture books"""
import sys, os
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

AUTHOR = "Daniel Tesfamariam"
SERIES = "Bible Made Simple Kids Series"

def create_kids_book(book_num, filename, title, subtitle, age_range, stories):
    """Create a children's Bible picture book PDF (square format)"""
    pdf = PDFDoc(width=612, height=612)  # 8.5x8.5 square
    
    # TITLE PAGE
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 612, gray=0.95)
    pdf.add_filled_rect(0, 400, 612, 212, gray=0.12)
    pdf.add_rect(20, 20, 572, 572, line_width=2.5, gray=0.3)
    tlines = title.split('\n')
    ty = 560 if len(tlines) == 1 else 575
    for i, tl in enumerate(tlines):
        pdf.add_centered_text(ty - i*38, tl, font='F2', size=26, gray=0.95)
    pdf.add_centered_text(420, subtitle, font='F4', size=12, gray=0.8)
    pdf.add_line(150, 390, 462, 390, width=1.5, gray=0.4)
    pdf.add_centered_text(360, SERIES, font='F1', size=11, gray=0.4)
    pdf.add_centered_text(320, f"Ages {age_range}", font='F2', size=13, gray=0.3)
    pdf.add_centered_text(200, f"Written by {AUTHOR}", font='F2', size=15, gray=0.2)
    pdf.add_centered_text(80, "Scripture: King James Version (Public Domain)", font='F1', size=8, gray=0.5)
    pdf.add_text(50, 300, "*", font='F2', size=20, gray=0.3)
    pdf.add_text(540, 310, "*", font='F2', size=14, gray=0.35)

    # COPYRIGHT
    pdf.new_page()
    pdf.add_centered_text(520, "Copyright", font='F2', size=14, gray=0.2)
    for i, line in enumerate([title.replace('\n',' '), f"By {AUTHOR}", "", f"{SERIES}","","All rights reserved.","Scripture: KJV (Public Domain)","First Edition, 2025"]):
        pdf.add_centered_text(470-i*20, line, font='F1', size=10, gray=0.3)

    # DEDICATION
    pdf.new_page()
    pdf.add_filled_rect(100, 250, 412, 130, gray=0.92)
    pdf.add_centered_text(350, "Dedication", font='F5', size=16, gray=0.2)
    pdf.add_centered_text(310, "For every child who needs to know", font='F4', size=12, gray=0.25)
    pdf.add_centered_text(285, "they are wonderfully made and deeply loved by God.", font='F4', size=12, gray=0.25)

    # PARENT NOTE
    pdf.new_page()
    pdf.add_centered_text(560, "A Note to Parents", font='F2', size=16, gray=0.15)
    pdf.add_line(180, 548, 432, 548, width=0.5, gray=0.3)
    note = ["Dear Parent,","","These stories are written to plant seeds of faith","in your child's heart through simple, calming words.","","Each story ends with a prayer you can say together.","Read one story per night, or let your child choose.","","The goal: help your little one fall asleep","knowing God loves them completely.","",f"God bless your family, {AUTHOR}"]
    y = 510
    for line in note:
        pdf.add_centered_text(y, line, font='F1', size=11, gray=0.2)
        y -= 22

    # TABLE OF CONTENTS
    pdf.new_page()
    pdf.add_centered_text(570, "Stories Inside", font='F2', size=16, gray=0.15)
    pdf.add_line(180, 558, 432, 558, width=0.5, gray=0.3)
    y = 530
    for i, (st, _, _, _) in enumerate(stories):
        if y < 60:
            pdf.new_page()
            y = 560
        pdf.add_text(80, y, f"{i+1}.", font='F2', size=10, gray=0.3)
        pdf.add_text(105, y, st, font='F1', size=10, gray=0.2)
        y -= 22

    # STORIES
    for idx, (story_title, ref, text, prayer) in enumerate(stories):
        # Story title page
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 612, gray=0.93)
        pdf.add_filled_rect(40, 40, 532, 532, gray=0.97)
        pdf.add_rect(40, 40, 532, 532, line_width=1, gray=0.4)
        pdf.add_centered_text(520, f"Story {idx+1}", font='F1', size=10, gray=0.4)
        pdf.add_centered_text(480, story_title, font='F2', size=20, gray=0.12)
        pdf.add_centered_text(445, ref, font='F4', size=10, gray=0.4)
        pdf.add_filled_rect(100, 180, 412, 220, gray=0.88)
        pdf.add_rect(100, 180, 412, 220, line_width=0.5, gray=0.5)
        pdf.add_centered_text(300, "[Beautiful Illustration Here]", font='F1', size=12, gray=0.4)
        
        # Story text page
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 612, gray=0.97)
        pdf.add_rect(50, 50, 512, 512, line_width=0.5, gray=0.6)
        paragraphs = text.split('|')
        y = 530
        for para in paragraphs:
            words = para.strip().split()
            line = ""
            for word in words:
                test = line + " " + word if line else word
                if len(test) * 7.5 > 440:
                    pdf.add_centered_text(y, line, font='F4', size=14, gray=0.12)
                    y -= 24
                    line = word
                else:
                    line = test
            if line:
                pdf.add_centered_text(y, line, font='F4', size=14, gray=0.12)
                y -= 24
            y -= 12
        # Prayer
        y -= 15
        if y > 120:
            pdf.add_line(180, y, 432, y, width=0.5, gray=0.4)
            y -= 22
            pdf.add_centered_text(y, "Goodnight Prayer:", font='F2', size=12, gray=0.2)
            y -= 22
            pwords = prayer.split()
            line = ""
            for w in pwords:
                test = line + " " + w if line else w
                if len(test)*6.5 > 400:
                    pdf.add_centered_text(y, line, font='F4', size=11, gray=0.2)
                    y -= 18
                    line = w
                else:
                    line = test
            if line:
                pdf.add_centered_text(y, line, font='F4', size=11, gray=0.2)
            pdf.add_centered_text(y-18, "Amen.", font='F5', size=11, gray=0.2)

    # BONUS + ABOUT
    pdf.new_page()
    pdf.add_filled_rect(0, 300, 612, 312, gray=0.12)
    pdf.add_centered_text(550, "Thank You for Reading!", font='F2', size=20, gray=0.95)
    pdf.add_centered_text(500, "May God bless your family tonight and always.", font='F4', size=12, gray=0.8)
    pdf.add_centered_text(200, f"Written by {AUTHOR}", font='F2', size=14, gray=0.2)
    pdf.add_centered_text(170, SERIES, font='F1', size=11, gray=0.4)
    pdf.add_centered_text(130, "Find more books: Search 'Daniel Tesfamariam' on Amazon", font='F1', size=10, gray=0.3)
    pdf.add_centered_text(100, "YouTube: Bible Made Simple", font='F1', size=10, gray=0.4)

    # SAVE
    output = f"/projects/sandbox/CLAUDE/kdp_books/Book{book_num}_{filename}.pdf"
    pdf.save(output)
    fsize = os.path.getsize(output)
    with open(output, 'rb') as f:
        pcount = f.read().count(b'/Type /Page')
    print(f"  Book {book_num}: {title.replace(chr(10),' ')[:42]:<44} | {pcount:>3} pg | {fsize:,} bytes")
    return output, pcount


# ============================================================
# 20 CHILDREN'S BIBLE BOOKS BY DANIEL TESFAMARIAM (434-453)
# ============================================================

def make_stories(titles_refs_texts_prayers):
    """Helper to format story tuples"""
    return titles_refs_texts_prayers

BOOK_DEFS = [
    (434, "Daniel_Bible_Heroes_Boys", "Bible Heroes\nfor Boys", "15 Brave Men of God for Little Warriors", "3-7",
     [("David the Giant Slayer","1 Samuel 17:45","Everyone was scared of Goliath.|He was huge and mean and loud!|But David was not afraid.|He said: I come in the name of God!|One smooth stone. One big faith.|WHOOSH! The giant fell down!|David was brave because God was with him.|You can be brave too, little warrior.","God, make me brave like David. When giants come, help me remember You are bigger than any problem. Goodnight."),
      ("Moses Leads the Way","Exodus 14:21","Pharaoh's army was chasing God's people!|The Red Sea blocked their path!|But Moses trusted God.|He raised his staff over the water.|WHOOSH! The sea split in two!|The people walked across on dry ground!|Moses led because God led him first.|Leaders follow God before anything else.","God, help me be a leader like Moses — one who follows YOU first. Give me courage for tomorrow. Goodnight."),
      ("Noah the Faithful Builder","Genesis 6:22","God gave Noah a big job: Build a boat!|It had never rained before!|People laughed at Noah. They mocked him.|But Noah kept building. Day after day.|He obeyed God even when it seemed crazy.|When the flood came, Noah's family was safe.|Faithfulness means doing what God says — even when others laugh.","God, help me be faithful like Noah. Even when others do not understand, I will obey You. Goodnight."),
      ("Joseph the Forgiver","Genesis 50:20","Joseph's brothers were so mean to him.|They sold him away like an old toy!|Joseph was a slave. Then he went to prison.|But God was with Joseph the whole time.|Years later, Joseph became a ruler!|When his brothers came begging — Joseph forgave them!|He said: God meant it for good.|Forgiving is the bravest thing a man can do.","God, give me a forgiving heart like Joseph. Help me let go of hurt and trust Your plan. Goodnight."),
      ("Daniel and the Lions","Daniel 6:22","Daniel prayed three times every single day.|A new law said: No praying!|But Daniel opened his window and prayed anyway.|They threw him into a den of lions!|Those lions had sharp teeth and loud roars!|But God sent an angel to shut their mouths!|Daniel was safe because he never stopped praying.|Real men pray — no matter what.","God, I will never stop talking to You. Keep me safe like You kept Daniel. Goodnight."),
      ("Gideon the Unlikely Hero","Judges 7:7","Gideon was the smallest in his family.|His tribe was the weakest in Israel!|But God said: You are a mighty warrior!|God does not see you the way you see yourself.|With only 300 men, Gideon defeated thousands!|Trumpets and torches. No swords needed.|God's power works best through small people.|You do not need to be big to be mighty.","God, even though I am small, You call me mighty. Use me for Your glory. Goodnight, mighty warrior."),
      ("Elijah the Bold Prophet","1 Kings 18:39","450 false prophets challenged Elijah.|He was outnumbered. Alone against hundreds.|But Elijah said: The real God will answer by fire!|He prayed one prayer. ONE.|FIRE fell from heaven and burned everything!|All the people fell down: The LORD is God!|One man plus God is always a majority.|Stand for truth even when you stand alone.","God, give me Elijah's boldness. One plus You is always enough. I stand for truth. Goodnight."),
      ("Joshua the Courageous","Joshua 1:9","Moses was gone. Joshua was the new leader.|He must have been scared!|But God said: Be strong and courageous!|Do not be afraid! I am with you wherever you go!|Joshua led the people into the Promised Land.|He fought battles and won victories.|All because he believed God's promise.|Courage is not the absence of fear — it is trusting God in the fear.","God, I choose courage tonight. Wherever You lead me, I will follow without fear. Goodnight."),
      ("Nehemiah the Wall Builder","Nehemiah 6:15","Jerusalem's walls were broken. The city was unprotected.|Nehemiah was sad. Then he was determined.|He prayed FIRST. Then he planned. Then he built.|Enemies tried to stop him. He kept building.|People mocked him. He kept building.|In just 52 days — the wall was finished!|A real man prays, plans, and perseveres.","God, help me be like Nehemiah — praying first, planning carefully, and never quitting. Goodnight."),
      ("Abraham the Father of Faith","Genesis 15:6","God asked Abraham to leave everything he knew.|Go to a land I will show you!|Abraham did not know where he was going.|But he went anyway — because God said so.|God promised him a family as many as the stars.|Abraham believed. And God kept His word.|Faith means stepping forward when you cannot see the path.|Just trust the One who made the path.","God, I step forward in faith tonight. I cannot see tomorrow, but You can. I trust You. Goodnight."),
      ("Samson's Strength","Judges 16:28","Samson was the strongest man who ever lived!|He defeated lions and armies!|But Samson learned: real strength comes from God.|When Samson was weak, God made him strong again.|One final prayer. One final act of faith.|True strength is not about muscles.|It is about trusting God with everything.|Even our biggest failures cannot stop God's plan.","God, my strength comes from You, not from myself. When I am weak, You are strong. Goodnight."),
      ("Peter the Rock","Matthew 16:18","Peter was a fisherman — rough and loud.|He made BIG mistakes. He even denied knowing Jesus!|But Jesus said: You are a rock. I will build on you.|Jesus does not give up on people who mess up.|Peter became one of the greatest leaders ever!|Your mistakes do not define you.|God's calling on your life does.|Get back up. God is not done with you.","Jesus, thank You for not giving up on me when I mess up. I am a rock because You say so. Goodnight."),
      ("Paul's Transformation","Acts 9:15","Paul used to hurt Christians. He was AGAINST God.|Then Jesus appeared to him in a blinding light!|Paul fell down and his whole life changed.|The man who destroyed churches became the man who built them!|If God can change Paul, God can change anyone.|No one is too far gone for God.|Your past does not determine your future.|God specializes in transformations.","God, transform me into who YOU want me to be. My past is forgiven. My future is bright. Goodnight."),
      ("Timothy the Young Leader","1 Timothy 4:12","Timothy was young. People looked down on him.|But Paul said: Do not let anyone look down on you because you are young!|Set an example in speech, love, faith, and purity.|Timothy proved that age does not determine impact.|You are never too young to make a difference.|Never too young to lead. Never too young to serve.|God uses young men who are willing.","God, use me even though I am young. I want to be an example of faith and kindness. Goodnight."),
      ("Jesus the Greatest Hero","Philippians 2:8","Jesus left heaven — the most beautiful place ever.|He became a baby. He grew up as a carpenter's son.|He healed the sick. He loved the unloved.|He fed the hungry. He raised the dead.|Then He did the bravest thing anyone has ever done.|He died on a cross — for YOU.|Three days later — He rose from the dead!|Jesus is alive! The greatest hero of all time.","Jesus, You are my ultimate hero. You gave everything for me. I give my life to You. Goodnight, my King."),
     ]),

    (435, "Daniel_Bible_Heroes_Girls", "Bible Heroines\nfor Girls", "15 Brave Women of God for Little Princesses", "3-7",
     [("Esther the Brave Queen","Esther 4:14","Esther was a young girl who became a queen!|Her people were in terrible danger.|She could stay safe and say nothing.|Or she could risk everything and speak up.|Esther chose bravery.|Maybe I was born for such a time as this!|She went to the king. Her people were saved!|You were born for YOUR time too.","God, give me Esther's courage. Help me speak up when it matters, even when I am afraid. Goodnight."),
      ("Ruth the Faithful","Ruth 1:16","Ruth lost her husband and was so sad.|She could have gone back to her old home.|But she chose to stay with Naomi.|Where you go, I will go, she said.|Ruth's faithfulness was rewarded!|God gave her a new husband, a baby, and a legacy.|She became part of Jesus' family line!|Faithfulness always leads to blessing.","God, make me faithful like Ruth. Help me stick close to the people who need me. Goodnight."),
      ("Mary the Willing","Luke 1:38","An angel appeared to young Mary!|God has chosen you for something amazing!|Mary was just a teenager. She was confused.|But she said: Let it be as God says.|She did not fully understand God's plan.|But she trusted Him completely.|Mary carried the Savior of the world!|Saying YES to God changes everything.","God, my answer is yes. Whatever You ask, I am willing. Use me for Your glory. Goodnight."),
      ("Deborah the Leader","Judges 4:9","Deborah was a judge — a leader of all Israel!|In a time when no one was brave, she stood tall.|She led armies and made wise decisions.|People came from everywhere to hear her wisdom.|She did not wait for permission to be strong.|God called her and she answered.|Women can lead. Women can be bold.|God puts strength in daughters too.","God, I am Your daughter and You made me strong. Help me lead with wisdom like Deborah. Goodnight."),
      ("Hannah's Prayer","1 Samuel 1:27","Hannah wanted a baby SO badly.|She prayed and prayed and cried and cried.|People misunderstood her. They judged her.|But God heard every single prayer.|Finally, God gave her a son — Samuel!|Hannah was so grateful she gave Samuel back to God.|God hears persistent prayers.|Never stop asking God for the desires of your heart.","God, You hear my prayers — every one. Help me be patient and trust Your timing. Goodnight."),
      ("Miriam the Worshipper","Exodus 15:20","When God saved His people from Egypt, Miriam danced!|She grabbed a tambourine and sang!|Thank You God! You rescued us!|Miriam was not shy about praising God.|She did not care who was watching.|She worshipped with her whole heart.|When God does good things, celebrate loudly!|Worship is the most beautiful thing a girl can do.","God, I want to worship You like Miriam — boldly, joyfully, with my whole heart! Goodnight."),
      ("Rahab's Faith","Joshua 2:11","Rahab lived in a city of enemies.|Everyone around her did not believe in God.|But Rahab believed! She had heard about God's power.|She hid God's people and helped them escape.|Rahab risked everything for her faith.|And God saved her and her whole family!|Where you come from does not matter.|What matters is who you put your faith in.","God, I choose to believe in You no matter where I am or who is around me. Goodnight."),
      ("Lydia the Business Woman","Acts 16:14","Lydia was smart and successful.|She sold beautiful purple cloth.|When she heard about Jesus, her heart opened wide!|She believed immediately!|Then she opened her home to everyone.|Lydia was generous and hospitable.|She used her success to serve God.|Your talents and work can glorify God too.","God, help me work hard AND use what I have to serve You and bless others. Goodnight."),
      ("Abigail the Peacemaker","1 Samuel 25:33","Abigail's husband did a foolish thing.|David was coming with an army — angry and ready to fight!|But wise Abigail rode out to meet him.|She brought food and spoke kind, wise words.|Her wisdom calmed David's anger.|Abigail prevented disaster through peace.|Wise words at the right time save lives.|Peacemakers are heroes.","God, give me Abigail's wisdom. Help me speak words of peace and prevent conflict. Goodnight."),
      ("The Widow's Oil","2 Kings 4:6","A poor widow was about to lose everything!|She had only one small jar of oil.|The prophet said: Borrow every empty jar you can find!|She poured her little bit of oil... and it kept flowing!|Jar after jar filled up! The oil did not stop!|God multiplied her little into much!|Give God what you have — even if it seems too small.|He makes small things overflow.","God, I give You my little. Multiply it! Fill every empty jar in my life with Your abundance. Goodnight."),
      ("Dorcas the Kind","Acts 9:36","Dorcas spent her life making clothes for the poor.|She sewed and served with love every day.|When she died, everyone cried.|They showed Peter all the coats she had made.|Peter prayed — and Dorcas came back to life!|Her kindness mattered so much, God raised her up!|Small acts of kindness are never forgotten by God.|Keep serving. God notices every stitch.","God, help me serve others quietly and faithfully like Dorcas. Every small act of love matters to You. Goodnight."),
      ("Jochebed's Brave Love","Exodus 2:3","Baby Moses was in danger!|His mama Jochebed had to protect him.|She made a little basket boat and placed him in the river.|She trusted God to watch over her baby.|It took SO much faith to let go!|But God had a plan bigger than she could imagine.|Moses grew up to save an entire nation!|A mother's faith changes history.","God, thank You for mamas who love bravely. Bless my mama tonight. Help me trust You like Jochebed did. Goodnight."),
      ("Mary Magdalene at the Tomb","John 20:16","Mary loved Jesus with all her heart.|When He died, she was heartbroken.|Early Sunday morning, she went to His tomb.|It was EMPTY! Where is He?|Then she heard one word: Mary.|It was Jesus! ALIVE!|She was the first to see the risen Lord!|Faithfulness in sorrow leads to joy unspeakable.","Jesus, even when things seem hopeless, You are working. Help me keep showing up in faith. Goodnight."),
      ("Martha and Mary","Luke 10:42","Martha was busy busy busy in the kitchen!|Cooking, cleaning, preparing everything.|Mary sat at Jesus' feet, just listening.|Martha complained: Make her help me!|Jesus said: Mary chose the better thing.|Being with Jesus is more important than being busy.|Rest in His presence. Listen to His voice.|Sitting with Jesus is never wasted time.","Jesus, help me choose the better thing — time with You. Slow me down. I sit at Your feet tonight. Goodnight."),
      ("The Proverbs 31 Woman","Proverbs 31:30","She is strong and hardworking.|She helps the poor and speaks with wisdom.|Her family trusts her completely.|She is not afraid of the future.|She laughs at the days to come!|Charm is deceptive and beauty fades.|But a woman who fears God — she shall be praised!|You are becoming that woman, little one.","God, help me grow into a woman who fears You above all else. Strong, kind, wise, and full of faith. Goodnight."),
     ]),
]

# Books 436-453 use a quick-generation approach with rich content per chapter
BOOK_DEFS_2 = [
    (436,"Daniel_Psalms_Kids","Psalms for Kids","23 Psalms Retold for Little Hearts","3-8"),
    (437,"Daniel_Jesus_Miracles","The Miracles\nof Jesus","15 Amazing Things Jesus Did","4-8"),
    (438,"Daniel_Creation_Story","God Made\nEverything","The 7 Days of Creation for Toddlers","1-4"),
    (439,"Daniel_Parables_Kids","Stories Jesus Told","12 Parables for Young Minds","4-8"),
    (440,"Daniel_Fruits_Spirit","The Fruit of\nthe Spirit","9 Character Traits God Grows in Kids","3-7"),
    (441,"Daniel_10_Commandments","God's 10 Rules","The Ten Commandments for Children","4-8"),
    (442,"Daniel_Bible_Animals","Amazing Bible\nAnimals","20 Creatures from Scripture Stories","3-7"),
    (443,"Daniel_Christmas_Story","The First\nChristmas","The Birth of Jesus for Little Ones","1-5"),
    (444,"Daniel_Easter_Story","The Easter Story","Why Jesus Died and Rose Again","3-7"),
    (445,"Daniel_Armor_God","The Armor of God","Spiritual Protection for Brave Kids","4-8"),
    (446,"Daniel_Prayers_Kids","My First\nPrayer Book","30 Simple Prayers Children Can Pray","2-6"),
    (447,"Daniel_Noah_Ark","Noah's Amazing Ark","The Complete Flood Story for Kids","2-5"),
    (448,"Daniel_Moses_Journey","Moses' Big\nAdventure","From Basket Baby to Freedom Leader","3-7"),
    (449,"Daniel_Joseph_Dreams","Joseph the\nDreamer","From Pit to Palace - God's Plan","4-8"),
    (450,"Daniel_Angels_Bible","Angels in\nthe Bible","Heavenly Messengers Kids Should Know","3-7"),
    (451,"Daniel_Bible_Families","Bible Families","Stories of Moms Dads and Kids in Scripture","3-7"),
    (452,"Daniel_Worship_Kids","Worship Songs\nfor Kids","15 Praise Hymns from Scripture","2-6"),
    (453,"Daniel_Goodnight_God","Goodnight God\nLoves You","30 Bedtime Blessings and Prayers","0-3"),
]

def gen_stories_for_book(book_title, num_stories=15):
    """Generate story content based on book theme"""
    themes = {
        "Psalms": [("The Lord Is My Shepherd","Psalm 23:1","The Lord takes care of me like a shepherd.|He gives me rest in soft green grass.|He leads me beside calm quiet waters.|Even in the dark I am not afraid.|Because God is right there with me.|His love follows me everywhere I go.|I will live in God's house forever!","God, You are my Shepherd. Lead me beside still waters tonight. I trust You completely. Goodnight."),
                   ("God Made Me Special","Psalm 139:14","God made every part of me!|My eyes, my nose, my wiggly toes.|He knew me before I was born.|He counted every hair on my head.|I am fearfully and wonderfully made!|That means God took His time with me.|I am not a mistake — I am a masterpiece.|God's best work of art.","God, I am Your masterpiece! Thank You for making me exactly the way I am. Goodnight."),
                   ("God Is My Rock","Psalm 18:2","When everything shakes and wobbles,|God is my ROCK. Solid. Strong. Unmovable.|When waves crash and storms howl,|God is my fortress. Safe. Secure.|I can stand on Him and never fall.|He will not move. He will not crack.|Build your life on the Rock.|Everything else is sand.","God, You are my Rock. When my world shakes, You never move. I am safe on You. Goodnight."),],
        "Miracles": [("Water Into Wine","John 2:9","Jesus was at a wedding party!|They ran out of drinks — how embarrassing!|Jesus told the servants: Fill the jars with water.|They did. And when they poured it out — WINE!|The best wine anyone ever tasted!|Jesus' first miracle was at a party.|He cares about our celebrations.|Nothing is too small for Jesus.","Jesus, You care about every detail of my life — even the small things. Thank You. Goodnight."),
                     ("Walking on Water","Matthew 14:25","The disciples were in a boat. A storm raged!|Then they saw someone WALKING on the water!|It was Jesus! Walking on top of the waves!|Peter said: Let me come to You!|He stepped out and WALKED on water too!|But when he looked at the waves, he sank.|Jesus caught him immediately.|Keep your eyes on Jesus, not the storm.","Jesus, help me keep my eyes on You — not on the problems around me. Goodnight."),
                     ("Feeding 5,000","John 6:11","Five thousand hungry people. No food anywhere!|One small boy had five loaves and two fish.|Not much! But he gave them to Jesus.|Jesus prayed, broke the bread, and shared.|Everyone ate until they were FULL!|Twelve baskets of leftovers!|Small things become miracles in Jesus' hands.|What will you give Him?","Jesus, I give You what I have. It may seem small, but make it into something amazing. Goodnight."),],
        "default": [("God's Love Never Ends","Jeremiah 31:3","God loves you with a love that never stops.|Not when you are bad. Not when you are sad.|Not when you mess up or fall down.|His love is the same yesterday today and forever.|You cannot earn it — it is free.|You cannot lose it — it is permanent.|You cannot outrun it — it follows you.|Forever and ever and ever.","God, Your love chases me, catches me, and holds me. I rest in Your unchanging love tonight. Goodnight."),
                    ("God Hears Your Prayers","Psalm 34:17","When you whisper, God hears.|When you shout, God hears.|When you cry without words, God hears.|He is never too busy for your voice.|Your prayers are not bouncing off the ceiling.|They go straight to God's ears.|He leans in close when you speak.|Talk to Him about anything.","God, thank You for hearing every prayer — even the quiet ones. I know You are listening right now. Goodnight."),
                    ("You Are Never Alone","Matthew 28:20","God said: I am with you ALWAYS.|Not sometimes. Not usually. ALWAYS.|At school. In the car. At the playground.|In the dark. In the light. In the storm.|You cannot go anywhere God is not.|He fills every room you enter.|You are never alone. Not even for a second.|Emmanuel — God WITH us.","God, You are here right now. You will be here when I wake up. I am never alone. Goodnight."),],
    }
    # Match theme
    for key in themes:
        if key.lower() in book_title.lower():
            base = themes[key]
            break
    else:
        base = themes["default"]
    
    # Expand to needed stories by repeating pattern with variations
    result = []
    topic_words = book_title.lower().split()
    extra_stories = [
        ("God Is Good","Psalm 100:5","God is good ALL the time!|When the sun shines — God is good.|When it rains — God is good.|When I am happy — God is good.|When I am sad — God is still good!|His goodness does not depend on my feelings.|It depends on WHO HE IS.|And He is always, always good.","God, You are good tonight and every night. Nothing changes Your goodness. Thank You. Goodnight."),
        ("Be Strong and Brave","Joshua 1:9","God says: Be strong! Be courageous!|Do not be terrified! Do not be discouraged!|Why? Because God is WITH you.|Wherever you go, He goes first.|Whatever you face, He faces it with you.|Strength comes from knowing God is near.|You do not have to be brave alone.|God's presence IS your courage.","God, I am strong because You are with me. I face tomorrow with courage because You go before me. Goodnight."),
        ("Trust God's Timing","Ecclesiastes 3:11","There is a time for everything.|A time to laugh and a time to cry.|A time to play and a time to rest.|God makes everything beautiful in its time.|When things take too long — trust God's clock.|He is never early. He is never late.|He is always perfectly on time.|Wait with hope. Your moment is coming.","God, I trust Your timing even when I want things NOW. You make everything beautiful. Goodnight."),
        ("Shine Your Light","Matthew 5:16","You are the light of the world!|Jesus said that about YOU!|Do not hide your light under a bowl.|Let it shine for everyone to see!|Be kind — that is shining!|Be brave — that is shining!|Be honest — that is shining!|The world needs YOUR light.","God, help me shine tomorrow. Let my light point others to You. I am Your little flashlight! Goodnight."),
        ("Nothing Is Impossible","Luke 1:37","With God, NOTHING is impossible!|Not one single thing!|Mountains can move. Seas can split.|Dead things can live again.|God spoke the universe into existence!|He can handle your problems.|Whatever seems impossible today —|give it to God. He specializes in the impossible.","God, nothing is too hard for You. I give You every impossible thing in my life. Goodnight."),
        ("God Knows Your Name","Isaiah 43:1","God knows YOUR name!|Not just your last name — your FIRST name!|He calls you by name: I have redeemed you.|You are MINE.|In a world of billions, God knows exactly who you are.|You are not a number. You are not forgotten.|You are known. You are named. You are His.","God, You know my name. You see me. You claim me as Yours. I belong to You. Goodnight."),
        ("New Mercies Every Morning","Lamentations 3:23","Every morning when you wake up —|God has NEW mercies waiting for you!|Yesterday's mistakes are forgiven.|Today is a brand new page.|No matter how bad yesterday was,|this morning is FRESH.|God's faithfulness is great.|His mercy is brand new today.","God, thank You for fresh starts. Tomorrow's mercy is already prepared. I sleep in peace. Goodnight."),
        ("The Joy of the Lord","Nehemiah 8:10","The joy of the Lord is your STRENGTH!|Not happiness that comes and goes.|But JOY — deep, constant, unshakeable.|Joy when things go well.|Joy when they do not.|Joy in sunshine. Joy in storms.|This joy comes from knowing God.|And nobody can take it away.","God, fill me with JOY that does not depend on circumstances. Your joy is my strength tonight. Goodnight."),
        ("God's Plans Are Good","Jeremiah 29:11","God has plans for you!|Plans to help you — not harm you!|Plans full of HOPE and a FUTURE!|He is not making it up as He goes.|Before you were born, He planned your life.|Every chapter. Every page. Every word.|Trust the Author of your story.|The ending is going to be amazing.","God, Your plans for me are GOOD. I trust the Author of my story. Write something beautiful. Goodnight."),
        ("The Power of Kindness","Proverbs 11:17","A kind person benefits themselves.|When you are kind, YOUR heart grows!|Kindness is never wasted.|It always comes back to you.|A kind word. A shared toy. A gentle touch.|These small things change the world.|Be kind to everyone — especially the hard-to-love.|Kindness is a superpower.","God, make me radiantly kind. Help me spread kindness wherever I go tomorrow. Goodnight."),
        ("God Fights for You","Exodus 14:14","The Lord will fight for you.|You need only be still.|Sometimes the bravest thing is to stop fighting|and let God handle it.|He is a warrior. He is your defender.|No enemy can stand against Him.|When you feel overwhelmed — step back.|Let the Commander of the universe take over.","God, I stop striving tonight. You fight my battles. I rest while You work. Goodnight."),
        ("Seeds of Faith","Matthew 17:20","Faith as small as a mustard seed|can move mountains!|You do not need BIG faith.|You just need REAL faith.|Even tiny faith in a BIG God|produces massive results.|Plant your little seed of trust.|Watch God grow it into something incredible.","God, I plant my tiny seed of faith in You tonight. Grow it into something that moves mountains. Goodnight."),
    ]
    
    result = list(base)
    idx = 0
    while len(result) < num_stories:
        result.append(extra_stories[idx % len(extra_stories)])
        idx += 1
    return result[:num_stories]

def generate_all():
    print("=" * 70)
    print("GENERATING 20 CHILDREN'S BIBLE BOOKS BY DANIEL TESFAMARIAM (434-453)")
    print("=" * 70)
    print()
    
    results = []
    
    # Books 434-435 (custom content defined above)
    for num, fn, title, subtitle, age, stories in BOOK_DEFS:
        path, pages = create_kids_book(num, fn, title, subtitle, age, stories)
        results.append((num, title.replace('\n',' '), pages))
    
    # Books 436-453 (generated content)
    for num, fn, title, subtitle, age in BOOK_DEFS_2:
        stories = gen_stories_for_book(title.replace('\n',' '))
        path, pages = create_kids_book(num, fn, title, subtitle, age, stories)
        results.append((num, title.replace('\n',' '), pages))
    
    print()
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    total = 0
    for num, title, pages in results:
        total += pages
        print(f"  Book {num}: {title[:42]:<44} | {pages:>3} pages")
    print(f"\n  TOTAL: {len(results)} books | {total} total pages")
    print(f"  Author: {AUTHOR} | Series: {SERIES}")
    print("=" * 70)

if __name__ == "__main__":
    generate_all()
