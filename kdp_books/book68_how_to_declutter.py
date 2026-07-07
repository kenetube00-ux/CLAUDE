"""
Book 68: How To Declutter Your Home - Room by Room Minimalist Guide
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "HOW TO DECLUTTER", font='F2', size=24)
    pdf.add_centered_text(485, "YOUR HOME", font='F2', size=24)
    pdf.add_centered_text(450, "Room by Room Minimalist Guide", font='F1', size=14)
    pdf.add_line(80, 425, 352, 425, 2)
    pdf.add_centered_text(385, "Create Calm, Organized Spaces", font='F4', size=13)
    pdf.add_centered_text(363, "That Bring You Joy and Peace", font='F4', size=13)
    pdf.add_centered_text(300, "By", font='F1', size=12)
    pdf.add_centered_text(275, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "How To Declutter Your Home", font='F2', size=11)
    pdf.add_centered_text(475, "Room by Room Minimalist Guide", font='F1', size=10)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(390, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(365, "Published via Amazon KDP", font='F1', size=10)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: The Psychology of Clutter", [
            "Clutter is not just a physical problem. It affects your mental health daily.",
            "Studies show cluttered spaces increase cortisol, the stress hormone, in your body.",
            "Visual clutter competes for your attention and reduces your ability to focus.",
            "People in cluttered homes report higher levels of anxiety and depression.",
            "Clutter often represents unmade decisions that weigh on your subconscious mind.",
            "We keep things out of guilt, fear, or a sense of obligation to the past.",
            "Sunk cost fallacy makes us keep things because we spent money on them.",
            "The just in case mentality fills our homes with items we never actually use.",
            "Clutter accumulates slowly over years until it feels overwhelming.",
            "Understanding why you hold onto things is the first step to letting go.",
            "You are not your stuff. Your memories exist in your heart, not in objects.",
            "A clear space creates a clear mind and room for what truly matters to you.",
        ]),
        ("Chapter 2: Getting Started Mindset", [
            "Start with the understanding that decluttering is a process, not a single event.",
            "Do not try to declutter your entire home in one weekend. You will burn out.",
            "Begin with a small area like a single drawer to build momentum and confidence.",
            "Set a timer for 15 minutes and declutter until it rings. Then stop or continue.",
            "Progress over perfection. Done imperfectly is better than never started.",
            "You will not regret getting rid of things. Research shows people feel relief.",
            "Take before and after photos to motivate yourself and track your progress.",
            "Enlist a supportive friend or family member if you need accountability.",
            "Avoid buying organizing products before decluttering. Reduce first, then organize.",
            "Expect emotional resistance. It is normal to feel attached to belongings.",
            "Remind yourself that someone else could benefit from items you never use.",
            "You deserve to live in a space that supports your current life and goals.",
        ]),
        ("Chapter 3: The 4-Box Method", [
            "Get four boxes or bags and label them: Keep, Donate, Trash, and Relocate.",
            "Every single item you touch must go into one of these four categories.",
            "Keep means the item earns its place in the room and you use it regularly.",
            "Donate means the item is in good condition but no longer serves your life.",
            "Trash means the item is broken, expired, stained, or cannot be given away.",
            "Relocate means the item belongs in a different room of your home.",
            "Handle each item only once. Pick it up, decide, place it in a box, move on.",
            "If you hesitate more than five seconds, ask: have I used this in the past year?",
            "If the answer is no and it has no sentimental value, it goes in donate or trash.",
            "At the end of each session, immediately take donate bags to your car.",
            "Take trash bags out right away so items do not creep back into your home.",
            "The 4-box method removes decision fatigue by simplifying your choices.",
        ]),
        ("Chapter 4: Decluttering the Kitchen", [
            "Start with expired food in the pantry, fridge, and freezer. Toss without guilt.",
            "Remove duplicate utensils. You do not need four spatulas and six wooden spoons.",
            "Donate gadgets you used once or never: bread makers, fondue sets, and specialty pans.",
            "Keep only the dishes and glasses your household actually uses daily.",
            "Clear countertops of appliances you use less than once a week.",
            "Consolidate food storage containers and match lids. Recycle orphaned pieces.",
            "Remove expired spices which lose potency after two to three years.",
            "Donate cookbooks you never open. Most recipes are available free online now.",
            "Keep one good set of pots and pans and donate cheap duplicates.",
            "Organize the junk drawer by removing true junk and keeping only functional items.",
            "Toss stained dish towels, worn sponges, and chipped mugs or plates.",
            "A clean, clear kitchen makes cooking enjoyable rather than stressful.",
        ]),
        ("Chapter 5: Decluttering the Bedroom", [
            "Your bedroom should be a peaceful retreat for rest and relaxation only.",
            "Remove anything that does not support sleep: work papers, exercise equipment, clutter.",
            "Clear nightstands to only essentials: lamp, book, water glass, and phone charger.",
            "Under the bed should be empty or contain only one flat storage container.",
            "Remove excess decorative pillows that you toss on the floor every night anyway.",
            "Pare down to two sets of sheets per bed. You only need one on and one washing.",
            "Donate extra blankets and comforters you have not used in over a year.",
            "Clear dresser tops of accumulated items that have no specific home.",
            "Remove old magazines, mail, and papers that have accumulated in the bedroom.",
            "Keep bedroom surfaces clear and you will sleep better and feel calmer.",
            "A minimalist bedroom with less visual stimulation promotes deeper rest.",
            "Your bedroom should make you feel relaxed the moment you walk in.",
        ]),
        ("Chapter 6: Decluttering the Bathroom", [
            "Check expiration dates on all medications and dispose of expired ones safely.",
            "Makeup expires: mascara after 3 months, foundation after 12, lipstick after 18.",
            "Toss old toothbrushes, dried-out nail polish, and rusty razors immediately.",
            "Remove sample-size products you collected from hotels but never use.",
            "Keep only products you use in your current routine, not aspirational purchases.",
            "Consolidate half-used bottles of the same product into one container.",
            "Donate unopened, unexpired products to local shelters that accept toiletries.",
            "Remove excess towels. Keep two bath towels and two hand towels per person.",
            "Clear the shower of bottles you have not touched in the last month.",
            "Organize under the sink by removing products and keeping only what you use.",
            "A decluttered bathroom feels like a spa and your morning routine becomes faster.",
            "Clean bathrooms are easier to maintain when there are fewer items to move.",
        ]),
        ("Chapter 7: Decluttering the Living Room", [
            "The living room should invite relaxation and connection, not visual chaos.",
            "Remove magazines and newspapers older than one month. Recycle them today.",
            "Assess decorative items: do they bring joy or just collect dust?",
            "Keep surfaces mostly clear with only one or two meaningful decorative pieces.",
            "Remove DVDs, CDs, and books you have watched, listened to, or read already.",
            "Donate board games, puzzles, and toys that no one has played in over a year.",
            "Corral remote controls, chargers, and small items in one attractive basket.",
            "Remove throw pillows and blankets beyond what you actually use for comfort.",
            "Assess furniture: does every piece serve a purpose and fit the space?",
            "Remove items that belong in other rooms and put them where they go.",
            "Clear entertainment center surfaces and hide cords for a clean look.",
            "A simplified living room feels larger, calmer, and more welcoming to guests.",
        ]),
        ("Chapter 8: Decluttering the Closet", [
            "Remove everything from your closet and only put back items you truly wear.",
            "If you have not worn something in 12 months, donate it regardless of condition.",
            "Try the hanger trick: turn all hangers backward, flip forward when worn.",
            "After six months, donate everything still on backward-facing hangers.",
            "Keep only clothes that fit your current body, not your aspirational size.",
            "Donate duplicates. You do not need fifteen white t-shirts or eight black pants.",
            "Remove clothes with stains, holes, or missing buttons that you never repair.",
            "Keep a small capsule wardrobe of pieces that mix and match easily.",
            "Organize remaining clothes by category: tops, bottoms, dresses, outerwear.",
            "Donate shoes that hurt your feet no matter how much they cost originally.",
            "A streamlined closet makes getting dressed in the morning fast and enjoyable.",
            "You will feel like you have more clothes when you can actually see everything.",
        ]),
        ("Chapter 9: Decluttering Paper and Mail", [
            "Paper clutter is one of the most common and most stressful forms of clutter.",
            "Immediately recycle junk mail at the door before it enters your living space.",
            "Unsubscribe from catalogs and switch to paperless billing for all accounts.",
            "Shred documents with personal information before recycling them.",
            "Keep only: tax documents (7 years), vital records, active insurance policies.",
            "Create a simple filing system: Action, Reference, and Archive categories.",
            "Action holds items needing response: bills to pay, forms to complete.",
            "Process the Action folder weekly so it never becomes an overwhelming pile.",
            "Scan important documents and store digital copies as backup.",
            "Children's artwork can be photographed and then rotate a few displayed pieces.",
            "Designate one spot as the paper landing zone and process it weekly.",
            "Once you control paper flow, your surfaces stay clear with minimal effort.",
        ]),
        ("Chapter 10: Digital Decluttering", [
            "Digital clutter causes the same mental fog as physical clutter in your space.",
            "Unsubscribe from email newsletters you never read using unroll.me or manually.",
            "Delete apps you have not opened in the last thirty days from your phone.",
            "Organize your phone home screen to show only apps you use daily.",
            "Delete blurry, duplicate, and unflattering photos from your camera roll.",
            "Organize remaining photos into albums by year or event for easy finding.",
            "Clear your computer desktop by filing documents into organized folders.",
            "Empty your downloads folder which likely contains hundreds of forgotten files.",
            "Review and delete old bookmarks, saved articles you will never read, and dead links.",
            "Organize your files into a simple folder structure: Work, Personal, Finance.",
            "Turn off non-essential notifications that interrupt your focus throughout the day.",
            "A clean digital environment reduces decision fatigue just like a clean room.",
        ]),
        ("Chapter 11: Decluttering with Kids", [
            "Involve children in the process. Let them make decisions about their own items.",
            "Make it fun: play music, set timers, and turn decluttering into a game.",
            "Start with obviously broken or outgrown toys that the child no longer plays with.",
            "Use the one-in-one-out rule: a new toy means an old toy gets donated.",
            "Rotate toys by storing some and swapping them every few weeks for freshness.",
            "Children only play with a fraction of their toys. Fewer options reduce overwhelm.",
            "Donate gently used items together so children see others benefiting.",
            "Do not declutter kids items secretly. They notice and lose trust.",
            "Create easy organization systems children can maintain independently.",
            "Keep toy storage at child height so cleanup is simple and expected.",
            "Art projects can be photographed, displayed temporarily, then recycled.",
            "Children who learn to declutter develop lifelong organizational skills.",
        ]),
        ("Chapter 12: What to Do with Unwanted Items", [
            "Donate usable items to thrift stores like Goodwill, Salvation Army, or local charities.",
            "Many charities offer free home pickup for large donations. Schedule online.",
            "Sell valuable items on Facebook Marketplace, Craigslist, or Poshmark.",
            "Host a garage sale for a quick way to clear many items at once.",
            "Give items to specific people you know would appreciate and use them.",
            "Buy Nothing groups on Facebook connect you with local neighbors who want items.",
            "Freecycle.org lets you post free items for local pickup by people who need them.",
            "Recycle electronics at dedicated e-waste collection events or retailers.",
            "Textile recycling accepts clothing too worn for donation.",
            "Hazardous items like paint and chemicals go to community collection events.",
            "Do not let the decision of where to send items stop you from decluttering.",
            "Speed matters: get items out of your home within 48 hours of deciding to let go.",
        ]),
        ("Chapter 13: Maintaining a Clutter-Free Home", [
            "Maintaining is easier than the initial declutter if you build simple habits.",
            "Do a ten-minute tidy every evening: put everything back in its designated spot.",
            "Process mail daily: recycle junk, file important items, pay or schedule bills.",
            "Make your bed every morning. This one habit sets a tone for the entire day.",
            "Clean as you go: put things away immediately rather than setting them down.",
            "Do a weekly fifteen-minute sweep of each room to catch accumulation early.",
            "Schedule seasonal thirty-minute declutter sessions for each room quarterly.",
            "Assign a home for every item in your house. If it has no home, it is clutter.",
            "Reset your home to its baseline state before going to bed each night.",
            "Involve all household members in maintaining shared spaces equally.",
            "Habits take 30 to 60 days to form. Be patient and consistent with yourself.",
            "A maintained home gives you freedom, calm, and more time for what you love.",
        ]),
        ("Chapter 14: The One-In-One-Out Rule", [
            "This simple rule prevents clutter from ever building up again after decluttering.",
            "When one new item enters your home, one similar item must leave.",
            "Buy a new shirt? Donate an old one you no longer wear or love.",
            "Receive a gift? Release something you own that serves the same purpose.",
            "This forces intentional purchasing: is this item worth removing something else?",
            "The rule applies to books, clothes, kitchen items, decorations, and toys.",
            "Over time you naturally become more selective about what you bring in.",
            "Quality replaces quantity. You buy fewer but better items that last longer.",
            "Keep a donation bag in your closet to add items to throughout the month.",
            "When the bag is full, drop it off at your nearest donation center immediately.",
            "This rule is especially powerful for families with children who receive many gifts.",
            "One-in-one-out transforms decluttering from a big project to an effortless lifestyle.",
        ]),
        ("Chapter 15: Your 30-Day Declutter Challenge", [
            "Day 1: Declutter your wallet or purse. Remove old receipts and expired cards.",
            "Day 2: Clear one kitchen drawer completely. Keep only daily-use items.",
            "Day 3: Go through your medicine cabinet. Discard expired items.",
            "Day 4: Unsubscribe from 10 email newsletters you never read.",
            "Day 5: Declutter your car. Remove trash, unused items, and unnecessary weight.",
            "Day 6: Tackle one closet shelf. Remove items you have not used in a year.",
            "Day 7: Clear your nightstand. Keep only sleep-related essentials.",
            "Day 8: Declutter kitchen countertops. Store or donate counter appliances rarely used.",
            "Day 9: Go through your book collection. Donate books you will not reread.",
            "Day 10: Delete 50 photos from your phone that are blurry or duplicates.",
            "Days 11-20: Tackle one room per day using the 4-box method for 30 minutes.",
            "Days 21-30: Maintain what you have cleared and do one final sweep of each space.",
        ]),
    ]

    page_num = 1
    for title, lines in chapters:
        pdf.new_page()
        pdf.add_centered_text(600, title, font='F2', size=16)
        pdf.add_line(60, 585, 372, 585, 1)
        y = 560
        for line in lines:
            pdf.add_text(50, y, line, font='F4', size=11)
            y -= 22
        pdf.add_centered_text(30, str(page_num), font='F1', size=10)
        page_num += 1

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book68_How_To_Declutter.pdf')
    print("Book 68 created: Book68_How_To_Declutter.pdf")

if __name__ == '__main__':
    create_book()
