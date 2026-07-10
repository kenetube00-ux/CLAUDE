"""Book 140: ADHD Cleaning & Home Management Planner"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"

    # Page 1: Title
    doc.new_page()
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(520, "ADHD CLEANING &", 'F2', 26, 0)
    doc.add_centered_text(485, "HOME MANAGEMENT PLANNER", 'F2', 26, 0)
    doc.add_centered_text(440, "No Shame, Just Systems", 'F4', 18, 0.2)
    doc.add_centered_text(370, "Neurodivergent-Friendly Cleaning Schedules", 'F1', 13, 0.3)
    doc.add_centered_text(345, "Room-by-Room Checklists | Habit Stacking", 'F1', 12, 0.3)
    doc.add_centered_text(325, "5-Minute Resets | 30-Day Tracker", 'F1', 12, 0.3)
    doc.add_centered_text(120, author, 'F2', 16, 0)

    # Page 2: Copyright
    doc.new_page()
    doc.add_centered_text(600, "ADHD CLEANING & HOME MANAGEMENT PLANNER", 'F2', 12, 0)
    doc.add_text(72, 500, f"Copyright (c) 2025 {author}. All rights reserved.", 'F1', 10, 0.3)
    doc.add_text(72, 480, "No part of this planner may be reproduced without permission.", 'F1', 10, 0.3)

    # Page 3: Why Cleaning is Hard with ADHD
    doc.new_page()
    doc.add_centered_text(740, "WHY CLEANING IS HARD WITH ADHD", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "If your house is messy, it's NOT because you're lazy. Here's why ADHD", 'F1', 11, 0.2)
    doc.add_text(72, 683, "makes cleaning genuinely harder:", 'F1', 11, 0.2)
    y = 655
    reasons = [
        ("Executive Dysfunction:", "Can't START tasks even when you want to"),
        ("Object Permanence:", "If you can't see it, it doesn't exist (including messes)"),
        ("Time Blindness:", "'I'll do it later' becomes never"),
        ("All-or-Nothing:", "If you can't deep clean, you do nothing"),
        ("Overwhelm:", "A messy room = 100 tasks your brain can't prioritize"),
        ("Dopamine:", "Cleaning is boring. Your brain needs stimulation."),
        ("Perfectionism:", "If it won't be PERFECT, why start?")
    ]
    for title, desc in reasons:
        doc.add_text(72, y, title, 'F2', 11, 0)
        doc.add_text(240, y, desc, 'F1', 11, 0.2)
        y -= 25
    y -= 20
    doc.add_filled_rect(72, y-5, 468, 40, 0.88)
    doc.add_text(80, y+15, "VALIDATION: Your worth is NOT determined by the state of your home.", 'F2', 11, 0)
    doc.add_text(80, y-2, "You deserve systems that work WITH your brain, not against it.", 'F2', 11, 0)

    # Page 4: Body Doubling Concept
    doc.new_page()
    doc.add_centered_text(740, "THE BODY DOUBLING CONCEPT", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Body doubling = having another person present while you do a task.", 'F1', 11, 0.2)
    doc.add_text(72, 678, "They don't need to help - just being there activates your brain.", 'F1', 11, 0.2)
    y = 645
    doc.add_text(72, y, "Options for body doubling:", 'F2', 12, 0)
    y -= 22
    options = ["Have a friend come over (they can bring their own work)",
               "Video call someone while you both clean", "Watch cleaning YouTube videos",
               "Listen to podcasts/audiobooks while cleaning", "Join an online body doubling community",
               "Use apps like Focusmate for virtual accountability"]
    for o in options:
        doc.add_text(90, y, f"- {o}", 'F1', 11, 0.2)
        y -= 20
    y -= 20
    doc.add_text(72, y, "My body doubling plan:", 'F2', 12, 0)
    y -= 22
    for i in range(4):
        doc.add_text(72, y, "_" * 70, 'F1', 11, 0.3)
        y -= 22

    # Page 5: 5-Minute Reset Method
    doc.new_page()
    doc.add_centered_text(740, "THE 5-MINUTE RESET METHOD", 'F2', 18, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 700, "Rule: You only have to clean for 5 minutes. Set a timer.", 'F2', 12, 0)
    doc.add_text(72, 675, "If you want to stop after 5 minutes, STOP. No guilt. But usually,", 'F1', 11, 0.2)
    doc.add_text(72, 658, "starting is the hardest part - and you'll keep going.", 'F1', 11, 0.2)
    y = 625
    doc.add_text(72, y, "5-MINUTE RESET CHECKLIST (do what you can!):", 'F2', 12, 0)
    y -= 22
    tasks = ["Pick up all trash and throw it away", "Put dishes in sink/dishwasher",
             "Pick up all clothes - hamper or hanger", "Clear one flat surface",
             "Take out one bag of trash/recycling"]
    for t in tasks:
        doc.add_rect(72, y-3, 12, 12)
        doc.add_text(90, y, t, 'F1', 11, 0.2)
        y -= 22
    y -= 20
    doc.add_text(72, y, "TRACKING: Color in each day you did at least one 5-min reset:", 'F2', 11, 0)
    y -= 25
    for week in range(4):
        doc.add_text(72, y, f"Week {week+1}:", 'F2', 10, 0.2)
        x = 130
        for day in range(7):
            doc.add_rect(x, y-4, 20, 20)
            x += 30
        y -= 30

    # Pages 6-13: Room-by-Room Checklists (8 rooms)
    rooms = [
        ("KITCHEN", 
         ["Wipe counters", "Load/unload dishwasher", "Take out trash", "Wipe stove top", "Quick floor sweep"],
         ["All of 5-min PLUS:", "Clean microwave inside", "Wipe cabinet fronts", "Organize one drawer", "Mop floor"],
         ["All of 15-min PLUS:", "Clean oven", "Deep clean fridge", "Scrub sink", "Organize pantry", "Clean behind appliances"]),
        ("BATHROOM",
         ["Wipe counter/sink", "Swish toilet bowl", "Hang up towels", "Toss empty bottles", "Quick mirror wipe"],
         ["All of 5-min PLUS:", "Scrub toilet fully", "Clean mirror properly", "Wipe shower walls", "Empty trash"],
         ["All of 15-min PLUS:", "Scrub grout", "Wash bath mats", "Organize under sink", "Deep clean shower", "Replace old products"]),
        ("BEDROOM",
         ["Make bed (just pull up covers!)", "Pick up floor clothes", "Clear nightstand", "Open blinds", "Quick trash pickup"],
         ["All of 5-min PLUS:", "Put away clean laundry", "Dust surfaces", "Organize one drawer", "Vacuum visible floor"],
         ["All of 15-min PLUS:", "Wash bedding", "Dust everything", "Organize closet section", "Under-bed cleanup", "Rotate mattress"]),
        ("LIVING ROOM",
         ["Pick up clutter to one pile", "Fluff pillows/straighten blankets", "Clear coffee table", "Stack remotes together", "Quick trash sweep"],
         ["All of 5-min PLUS:", "Dust TV/electronics", "Vacuum/sweep", "Put away pile from 5-min", "Wipe surfaces"],
         ["All of 15-min PLUS:", "Deep vacuum (move furniture)", "Clean windows", "Dust shelves/books", "Organize media", "Wipe baseboards"]),
        ("LAUNDRY",
         ["Start one load", "Move clothes to dryer", "Fold one basket", "Clear top of machines", "Sort dirty into piles"],
         ["All of 5-min PLUS:", "Fold AND put away", "Clean lint trap", "Wipe machines", "Sort donate pile"],
         ["All of 15-min PLUS:", "Run machine cleaner", "Deep clean behind machines", "Organize supplies", "Iron/steam what needs it", "Season closet rotation"]),
        ("HOME OFFICE",
         ["Clear desk surface", "File/toss loose papers", "Push in chair", "Close browser tabs (jk)", "Empty desk trash"],
         ["All of 5-min PLUS:", "Organize one drawer", "Wipe screen/keyboard", "Sort mail", "Cable management"],
         ["All of 15-min PLUS:", "Deep organize files", "Clean all electronics", "Shred old documents", "Reorganize supplies", "Clean chair/desk thoroughly"]),
        ("KIDS ROOM",
         ["Pick up floor toys into ONE bin", "Make bed (just covers)", "Dirty clothes to hamper", "Clear one surface", "Quick trash check"],
         ["All of 5-min PLUS:", "Sort toys into proper bins", "Dust surfaces", "Vacuum", "Put away books", "Check under bed"],
         ["All of 15-min PLUS:", "Toy purge/donate", "Wash bedding", "Organize closet", "Wipe walls/doors", "Deep clean play area"]),
        ("ENTRYWAY",
         ["Line up shoes", "Hang up coats/bags", "Clear surface clutter", "Check mail pile", "Quick floor sweep"],
         ["All of 5-min PLUS:", "Wipe door handles", "Organize shoe rack", "Sort mail properly", "Clean mirror/decor"],
         ["All of 15-min PLUS:", "Deep mop", "Clean closet", "Wash door mat", "Organize seasonal items", "Clean light fixtures"])
    ]
    for room_name, five_min, fifteen_min, deep in rooms:
        doc.new_page()
        doc.add_centered_text(740, f"ROOM: {room_name}", 'F2', 16, 0)
        doc.add_line(72, 730, 540, 730, 1, 0.5)
        y = 710
        # 5-minute column
        doc.add_text(72, y, "5-MINUTE QUICK CLEAN:", 'F2', 11, 0)
        y -= 18
        for task in five_min:
            doc.add_rect(72, y-3, 10, 10)
            doc.add_text(87, y, task, 'F1', 10, 0.2)
            y -= 16
        y -= 12
        doc.add_text(72, y, "15-MINUTE CLEAN:", 'F2', 11, 0)
        y -= 18
        for task in fifteen_min:
            doc.add_rect(72, y-3, 10, 10)
            doc.add_text(87, y, task, 'F1', 10, 0.2)
            y -= 16
        y -= 12
        doc.add_text(72, y, "DEEP CLEAN (monthly):", 'F2', 11, 0)
        y -= 18
        for task in deep:
            doc.add_rect(72, y-3, 10, 10)
            doc.add_text(87, y, task, 'F1', 10, 0.2)
            y -= 16

    # Page 14: Weekly Cleaning Schedule
    doc.new_page()
    doc.add_centered_text(740, "WEEKLY CLEANING SCHEDULE (SIMPLIFIED)", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "ONE focus area per day. That's it. Don't do more unless you WANT to.", 'F2', 11, 0)
    y = 670
    schedule = [
        ("MONDAY:", "Kitchen (15-min clean)"),
        ("TUESDAY:", "Bathrooms (15-min clean)"),
        ("WEDNESDAY:", "Laundry (wash, dry, put away)"),
        ("THURSDAY:", "Living areas (15-min clean)"),
        ("FRIDAY:", "Floors (vacuum/sweep/mop main areas)"),
        ("SATURDAY:", "Catch-up or one deep clean task"),
        ("SUNDAY:", "REST. You deserve it.")
    ]
    for day, task in schedule:
        doc.add_filled_rect(72, y-5, 468, 25, 0.92)
        doc.add_text(80, y, day, 'F2', 12, 0)
        doc.add_text(200, y, task, 'F1', 12, 0.2)
        y -= 32
    y -= 20
    doc.add_text(72, y, "REMEMBER: Done is better than perfect. A quick wipe beats no wipe.", 'F2', 11, 0)

    # Page 15: Habit Stacking
    doc.new_page()
    doc.add_centered_text(740, "HABIT STACKING FOR CHORES", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Attach a cleaning task to something you ALREADY do:", 'F1', 11, 0.2)
    y = 675
    stacks = [
        "While coffee brews -> unload dishwasher",
        "After using bathroom -> wipe counter",
        "While brushing teeth -> wipe mirror",
        "After dinner -> wipe stove and counters",
        "Before bed -> 5-minute reset in living room",
        "When laundry buzzes -> immediately switch (don't sit down!)",
        "After shower -> squeegee walls"
    ]
    for s in stacks:
        doc.add_text(90, y, f"- {s}", 'F1', 11, 0.2)
        y -= 22
    y -= 20
    doc.add_text(72, y, "MY HABIT STACKS:", 'F2', 12, 0)
    y -= 25
    for i in range(5):
        doc.add_text(72, y, f"When I __________________ -> I will __________________________________", 'F1', 11, 0.2)
        y -= 25

    # Page 16: Dopamine Pairing
    doc.new_page()
    doc.add_centered_text(740, "DOPAMINE PAIRING IDEAS", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Make cleaning less boring by pairing it with something fun:", 'F1', 11, 0.2)
    y = 675
    pairs = ["Favorite podcast + folding laundry", "Dance music + vacuuming/mopping",
             "Audiobook + organizing drawers", "Phone call with friend + tidying",
             "YouTube video + dishes", "True crime podcast + deep cleaning",
             "Reward after: 15 min clean = 15 min phone/game", "Make it a race: beat the song!"]
    for p in pairs:
        doc.add_text(90, y, f"- {p}", 'F1', 11, 0.2)
        y -= 22
    y -= 20
    doc.add_text(72, y, "MY DOPAMINE PAIRS:", 'F2', 12, 0)
    y -= 25
    for i in range(5):
        doc.add_text(72, y, f"Chore: _________________ + Fun thing: ______________________________", 'F1', 11, 0.2)
        y -= 25

    # Page 17: Monthly Maintenance
    doc.new_page()
    doc.add_centered_text(740, "MONTHLY MAINTENANCE CHECKLIST", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Once a month, pick ONE of these. Not all. ONE.", 'F2', 11, 0)
    y = 675
    monthly = ["Change/wash bedding (all beds)", "Deep clean one bathroom",
               "Clean refrigerator (toss expired items)", "Vacuum under furniture",
               "Wipe light switches and door handles", "Clean washing machine",
               "Dust ceiling fans/vents", "Organize one closet/cabinet",
               "Clean windows (just the ones you notice)", "Check/change HVAC filter",
               "Declutter one junk drawer", "Deep clean oven/microwave"]
    for m in monthly:
        doc.add_rect(72, y-3, 12, 12)
        doc.add_text(90, y, m, 'F1', 11, 0.2)
        y -= 22

    # Page 18: Emergency Guest Cleanup
    doc.new_page()
    doc.add_centered_text(740, "EMERGENCY: GUEST COMING IN 20 MINUTES!", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Don't panic. Follow this exact order:", 'F2', 12, 0)
    y = 675
    emergency = [
        ("Minutes 1-3:", "Grab a trash bag. Walk through every room. Trash everything obvious."),
        ("Minutes 4-7:", "Grab a laundry basket. Put ALL clutter in it. Shove in closet."),
        ("Minutes 8-10:", "Bathroom: wipe counter, close shower curtain, fresh towel, flush."),
        ("Minutes 11-13:", "Kitchen: load dishes in dishwasher (or hide in oven). Wipe counters."),
        ("Minutes 14-16:", "Living room: fluff pillows, straighten blankets, clear coffee table."),
        ("Minutes 17-18:", "Sweep/Swiffer main floor if visibly dirty."),
        ("Minutes 19-20:", "Light a candle. It fixes EVERYTHING. Breathe. You did it.")
    ]
    for time, task in emergency:
        doc.add_text(72, y, time, 'F2', 10, 0)
        doc.add_text(160, y, task, 'F1', 10, 0.2)
        y -= 30
    y -= 10
    doc.add_filled_rect(72, y-5, 468, 25, 0.88)
    doc.add_text(80, y, "REMEMBER: No one is inspecting your baseboards. Relax.", 'F2', 11, 0)

    # Page 19: Cleaning Playlist
    doc.new_page()
    doc.add_centered_text(740, "MY CLEANING PLAYLIST", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Music makes cleaning 10x easier. Build your ultimate cleaning playlist:", 'F1', 11, 0.2)
    y = 670
    doc.add_text(72, y, "HIGH ENERGY songs (for motivation):", 'F2', 11, 0)
    y -= 22
    for i in range(5):
        doc.add_text(72, y, f"{i+1}. ___________________________________________", 'F1', 11, 0.2)
        y -= 20
    y -= 10
    doc.add_text(72, y, "CHILL/PODCAST options (for mindless tasks):", 'F2', 11, 0)
    y -= 22
    for i in range(5):
        doc.add_text(72, y, f"{i+1}. ___________________________________________", 'F1', 11, 0.2)
        y -= 20
    y -= 10
    doc.add_text(72, y, "Tip: Make a '15-minute power clean' playlist that's exactly 15 min.", 'F2', 11, 0)
    y -= 18
    doc.add_text(72, y, "When the music stops, you stop. No guilt.", 'F1', 11, 0.2)

    # Pages 20-35: 30-Day Building Habits Tracker (spread across remaining pages)
    doc.new_page()
    doc.add_centered_text(740, "30-DAY BUILDING HABITS TRACKER", 'F2', 16, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    doc.add_text(72, 705, "Track your daily cleaning habits. Check off what you did each day.", 'F1', 11, 0.2)
    doc.add_text(72, 685, "Goal: Just do SOMETHING. Even 2 minutes counts.", 'F2', 11, 0)
    y = 655
    doc.add_filled_rect(72, y-2, 468, 18, 0.85)
    doc.add_text(75, y, "Day", 'F2', 8, 0)
    doc.add_text(110, y, "5-min reset?", 'F2', 8, 0)
    doc.add_text(200, y, "What I did", 'F2', 8, 0)
    doc.add_text(380, y, "How I feel", 'F2', 8, 0)
    y -= 22
    for day in range(1, 16):
        doc.add_text(78, y+3, str(day), 'F1', 9, 0.2)
        doc.add_rect(110, y, 15, 15)
        doc.add_rect(200, y-2, 175, 18)
        doc.add_rect(380, y-2, 100, 18)
        y -= 20

    # Page 2 of tracker
    doc.new_page()
    doc.add_centered_text(740, "30-DAY TRACKER (continued)", 'F2', 14, 0)
    doc.add_line(72, 730, 540, 730, 1, 0.5)
    y = 705
    doc.add_filled_rect(72, y-2, 468, 18, 0.85)
    doc.add_text(75, y, "Day", 'F2', 8, 0)
    doc.add_text(110, y, "5-min reset?", 'F2', 8, 0)
    doc.add_text(200, y, "What I did", 'F2', 8, 0)
    doc.add_text(380, y, "How I feel", 'F2', 8, 0)
    y -= 22
    for day in range(16, 31):
        doc.add_text(78, y+3, str(day), 'F1', 9, 0.2)
        doc.add_rect(110, y, 15, 15)
        doc.add_rect(200, y-2, 175, 18)
        doc.add_rect(380, y-2, 100, 18)
        y -= 20
    y -= 20
    doc.add_text(72, y, "CELEBRATE! You built a habit. What reward do you deserve?", 'F2', 11, 0)
    y -= 22
    doc.add_text(72, y, "___________________________________________________________________", 'F1', 11, 0.2)

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book140_ADHD_Cleaning_Schedule.pdf')
    print("Book140_ADHD_Cleaning_Schedule.pdf created successfully!")

if __name__ == "__main__":
    create_book()
