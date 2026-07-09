from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "SENSORY ACTIVITIES WORKBOOK"
subtitle = "For Kids with Autism & Sensory Processing Needs"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 18)
pdf.add_centered_text(515, subtitle, 'F4', 13)
pdf.add_centered_text(440, "Practical Activities, Sensory Diets, and Tracking Tools", 'F4', 11)
pdf.add_centered_text(420, "for Parents, Therapists, and Educators", 'F4', 11)
pdf.add_centered_text(280, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 11)
pdf.add_centered_text(570, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(550, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "This workbook is for educational purposes only and does not", 'F4', 9)
pdf.add_centered_text(496, "replace professional occupational therapy evaluation or treatment.", 'F4', 9)

# Page 3: Understanding Sensory Processing
pdf.new_page()
pdf.add_centered_text(750, "UNDERSTANDING SENSORY PROCESSING", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
lines = [
    "Every moment, our brains receive information from our senses and",
    "decide how to respond. For children with Sensory Processing Disorder",
    "(SPD) or autism, this system works differently.",
    "",
    "WHAT IS SENSORY PROCESSING?",
    "The brain's ability to receive, organize, and respond to sensory input.",
    "When this system is not working well, children may be:",
    "",
    "SENSORY SEEKING (Hypo-sensitive / Under-responsive):",
    "- Craves intense input (spinning, crashing, loud noises)",
    "- Seems to never get enough stimulation",
    "- May appear hyperactive or 'wild'",
    "- Has high pain tolerance",
    "",
    "SENSORY AVOIDING (Hyper-sensitive / Over-responsive):",
    "- Overwhelmed by sounds, textures, lights, or movements",
    "- May cover ears, refuse certain foods, avoid touch",
    "- Can seem anxious, rigid, or have frequent meltdowns",
    "- Has low pain tolerance",
    "",
    "MIXED PATTERN:",
    "- Many children are seekers in SOME areas and avoiders in others",
    "- The same child may crave deep pressure but hate light touch",
    "",
    "KEY PRINCIPLE: Behavior is COMMUNICATION.",
    "When a child is 'misbehaving,' they may be telling you their sensory",
    "needs are not being met. This workbook helps you understand and meet",
    "those needs proactively."
]
for line in lines:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 16

# Page 4: The 8 Sensory Systems
pdf.new_page()
pdf.add_centered_text(750, "THE 8 SENSORY SYSTEMS EXPLAINED", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
systems = [
    ("1. VISUAL (Sight)", "Processing light, color, movement, and spatial information"),
    ("2. AUDITORY (Hearing)", "Processing sounds, volume, tone, and auditory patterns"),
    ("3. TACTILE (Touch)", "Processing textures, temperature, pressure, and pain"),
    ("4. GUSTATORY (Taste)", "Processing flavors, textures, and temperatures of food"),
    ("5. OLFACTORY (Smell)", "Processing odors and scents in the environment"),
    ("6. VESTIBULAR (Balance/Movement)", "Processing head position, gravity, and motion (inner ear)"),
    ("7. PROPRIOCEPTIVE (Body Awareness)", "Processing input from muscles and joints about body position"),
    ("8. INTEROCEPTION (Internal Signals)", "Processing internal body signals (hunger, bathroom, temperature)")
]
for name, description in systems:
    pdf.add_text(50, y, name, 'F2', 10)
    y -= 14
    pdf.add_text(60, y, description, 'F4', 9)
    y -= 14
    pdf.add_text(60, y, "My child is:  [ ] Seeking  [ ] Avoiding  [ ] Mixed  [ ] Typical", 'F1', 8)
    y -= 12
    pdf.add_text(60, y, "Signs I notice: ________________________________________________", 'F1', 8)
    y -= 20

# Page 5: Sensory Profile Worksheet
pdf.new_page()
pdf.add_centered_text(750, "SENSORY PROFILE WORKSHEET", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Child's Name: __________________  Age: ___  Date: ___/___/___", 'F2', 10)
y -= 20
pdf.add_text(50, y, "Rate each area: 1=Under-responsive  3=Typical  5=Over-responsive", 'F4', 10)
y -= 20
profile_items = [
    ("TOUCH", ["Light touch (being brushed against)", "Clothing textures (tags, seams)", "Messy play (paint, glue, sand)", "Haircuts/nail trimming", "Hugs/physical affection"]),
    ("SOUND", ["Loud environments (cafeteria, assemblies)", "Unexpected sounds (alarms, dogs)", "Background noise", "Specific sounds (chewing, humming)", "Music volume preference"]),
    ("MOVEMENT", ["Swings/spinning", "Car rides", "Climbing/heights", "Being upside down", "Sitting still"]),
    ("VISUAL", ["Bright lights/fluorescents", "Busy visual environments", "Screen time tolerance", "Eye contact", "Finding objects in clutter"]),
]
for system_name, items in profile_items:
    pdf.add_text(50, y, system_name, 'F2', 9)
    y -= 13
    for item in items:
        pdf.add_text(60, y, f"{item}:", 'F4', 8)
        pdf.add_text(300, y, "1   2   3   4   5", 'F3', 8)
        y -= 12
    y -= 8

# Page 6: Sensory Diet Builder
pdf.new_page()
pdf.add_centered_text(750, "SENSORY DIET BUILDER", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "A 'sensory diet' is a personalized plan of activities throughout the day", 'F4', 10)
y -= 14
pdf.add_text(50, y, "to keep your child regulated. Fill in activities for each time period.", 'F4', 10)
y -= 25
times_of_day = [
    ("MORNING ROUTINE (before school)", 5),
    ("SCHOOL DAY (request from teacher/therapist)", 4),
    ("AFTER SCHOOL (transition home)", 5),
    ("EVENING (before bed)", 4)
]
for period, num_slots in times_of_day:
    pdf.add_filled_rect(50, y - 3, 512, 14, 0.9)
    pdf.add_text(55, y, period, 'F2', 10)
    y -= 18
    for s in range(num_slots):
        pdf.add_text(60, y, f"Activity {s+1}:", 'F1', 9)
        pdf.add_line(120, y - 2, 360, y - 2, 0.3, 0.5)
        pdf.add_text(370, y, "System:", 'F1', 8)
        pdf.add_line(405, y - 2, 562, y - 2, 0.3, 0.5)
        y -= 14
    y -= 12
y -= 5
pdf.add_text(50, y, "CALMING ACTIVITIES (for overstimulation):", 'F2', 9)
y -= 14
pdf.add_text(60, y, "1. ________________________  2. ________________________  3. ________________________", 'F1', 8)
y -= 14
pdf.add_text(50, y, "ALERTING ACTIVITIES (for under-arousal):", 'F2', 9)
y -= 14
pdf.add_text(60, y, "1. ________________________  2. ________________________  3. ________________________", 'F1', 8)

# Pages 7-21: 15 Activity Instruction Pages
activities = [
    ("HEAVY WORK OBSTACLE COURSE", "Proprioceptive", ["Couch cushions or pillows", "A laundry basket with books inside", "A blanket for crawling under", "Tape for floor markers", "Timer (optional)"],
     ["Set up pillows as 'mountains' to climb over", "Place laundry basket at one end to push or pull across room", "Lay blanket as a tunnel to army-crawl through", "Mark spots on floor for jumping (frog jumps, star jumps)", "Have child complete course 3-5 times, varying speed"],
     "Add weighted backpack for extra input. Reduce steps if overwhelmed. Time the course for motivation."),
    ("SENSORY BIN EXPLORATION", "Tactile", ["Large plastic bin", "Base material (rice, beans, water beads, or kinetic sand)", "Small toys or objects to find", "Scoops, cups, funnels", "Towel for cleanup"],
     ["Fill bin with chosen base material (start with dry if tactile-sensitive)", "Hide 5-10 small objects in the material", "Have child find objects using only their hands", "Name each object found and sort by category", "Allow free exploration for 5-10 minutes after structured activity"],
     "For avoiders: start with tools (spoons) before hands. Offer a towel nearby. Never force."),
    ("DEEP PRESSURE BURRITO ROLL", "Proprioceptive + Tactile", ["Large blanket or yoga mat", "Pillows for 'toppings'", "Soft music (optional)", "Timer"],
     ["Lay blanket flat on floor", "Have child lie at one end, arms at sides", "Roll them snugly in blanket (not covering face)", "Add pillow 'toppings' with gentle pressure on top", "Hold for 30-60 seconds, ask 'more pressure or less?'"],
     "Never cover face. Let child unroll themselves. Great for calming before transitions."),
    ("SPINNING & VESTIBULAR PLAY", "Vestibular", ["Sit-and-spin toy, office chair, or swing", "Timer", "Mat for safety", "Bucket (some children feel nauseous)", "Calm-down space nearby"],
     ["Start with SLOW spinning (10-15 seconds)", "Spin in ONE direction, then pause 30 seconds", "Observe child's response (eyes, balance, mood)", "If seeking: gradually increase duration", "If avoiding: try linear movement (rocking) first"],
     "Watch for nausea, pale skin, or glazed eyes - stop immediately. Vestibular input is POWERFUL."),
    ("ORAL MOTOR ACTIVITIES", "Gustatory + Proprioceptive", ["Chewy tube or food-safe chew toy", "Thick smoothie with straw", "Crunchy snacks (carrots, pretzels)", "Bubble blowing supplies", "Vibrating toothbrush (optional)"],
     ["Start with blowing bubbles (3 minutes of sustained blowing)", "Offer crunchy snack and encourage loud crunching", "Have child drink thick smoothie through thin straw", "Practice 'mouth exercises': pucker, smile, tongue push-ups", "End with chewing activity (chewy tube or gum) for 2 minutes"],
     "Oral seekers may chew clothing/objects - redirect to appropriate chewies. Check for food allergies."),
    ("WEIGHTED LAP PAD TIME", "Proprioceptive", ["Weighted lap pad (1-2 lbs for young children)", "Calm activity (coloring, puzzles)", "Timer set for 15-20 minutes", "Comfortable seating", "Soft background music (optional)"],
     ["Place weighted pad on child's lap during seated activity", "Set timer for 15-20 minutes maximum", "Observe if child becomes calmer and more focused", "Remove if child pushes it away or seems uncomfortable", "Use during homework, meals, or circle time"],
     "Weight should be ~10% of child's body weight. Remove every 20 min. Never use on chest/face."),
    ("WATER PLAY STATION", "Tactile + Visual", ["Plastic bins (various sizes)", "Warm and cool water", "Cups, funnels, turkey baster", "Sponges and washcloths", "Food coloring (optional)", "Towels and smock"],
     ["Fill bins with different temperature water", "Provide tools for pouring and squeezing", "Add food coloring for visual interest", "Practice squeezing sponges (hand strength)", "Allow free exploration with gradually messier materials"],
     "Start with tools if tactile-defensive. Gradually introduce hands. Warm water is calming, cool is alerting."),
    ("BODY SOCK ACTIVITIES", "Proprioceptive + Vestibular", ["Body sock (lycra sensory sack)", "Open floor space", "Soft music or audiobook", "Visual timer"],
     ["Help child step into body sock", "Stretch into shapes (star, ball, airplane)", "Practice slow movements inside sock", "Play 'freeze' game - move then hold still", "Use for calming: lie still inside for 2-3 minutes"],
     "Supervise at all times. Ensure face opening is always accessible. Great for body awareness."),
    ("SOUND EXPLORATION", "Auditory", ["Various noise makers (bells, drums, shakers)", "Noise-canceling headphones (for breaks)", "Recording device (phone)", "Quiet space available", "Visual timer"],
     ["Start in quiet environment", "Introduce ONE sound at a time, from soft to loud", "Let child control the volume (they make the sound)", "Practice identifying sounds with eyes closed", "End with quiet time or preferred calming sound"],
     "For sound-sensitive kids: always give warning before sounds. Allow headphones. Never force."),
    ("PROPRIOCEPTIVE WALL PUSHES", "Proprioceptive", ["A wall (any sturdy wall)", "Timer", "Visual instruction card", "Stickers for reward (optional)", "None - can do anywhere!"],
     ["Stand arm's length from wall", "Place both palms flat on wall at shoulder height", "Push HARD for 10 seconds (like trying to push wall down)", "Rest 5 seconds, repeat 5-10 times", "Try with back against wall, pushing with shoulders"],
     "Great for calming before transitions. Can be done at school, home, or stores. No equipment needed!"),
    ("TEXTURE COLLAGE ART", "Tactile + Visual", ["Various texture materials (sandpaper, cotton, foil, fabric)", "Glue stick and liquid glue", "Cardstock or thick paper", "Scissors (supervised)", "Labels for naming textures"],
     ["Lay out texture samples for child to explore", "Ask child to sort: 'like touching' vs 'do not like touching'", "Choose 5+ textures to glue onto paper", "Label each texture with a describing word", "Display finished art - celebrate brave touching!"],
     "Never force touching. Use tweezers for textures child dislikes. Process matters more than product."),
    ("BALANCE BEAM WALKING", "Vestibular + Proprioceptive", ["Painter's tape (for floor line)", "Low balance beam or 2x4 board", "Beanbags to carry", "Pillows alongside for safety", "Preferred music"],
     ["Start with tape line on floor (widest, easiest)", "Walk forward, backward, and sideways", "Add challenge: carry beanbag on head", "Progress to raised beam (only 2-3 inches off ground)", "End with 'statue' balance on one foot (count how long)"],
     "Always spot the child. Start LOW and wide. Barefoot provides more sensory feedback."),
    ("FIDGET AND FOCUS TOOLS", "Tactile + Proprioceptive", ["Various fidgets (putty, spinner, tangle)", "Resistance bands for chair legs", "Wobble cushion for seating", "Velcro strip under desk", "Checklist for tracking focus"],
     ["Introduce ONE fidget tool at a time", "Teach rules: fidget helps focus, not distract", "Try tool during quiet work time (10 minutes)", "Rate: Did this help me focus? Yes / A little / No", "Rotate tools weekly to maintain novelty"],
     "Fidgets should be silent and non-distracting to others. Remove if it becomes a toy instead of a tool."),
    ("CALMING YOGA POSES", "Vestibular + Proprioceptive + Interoception", ["Yoga mat or soft surface", "Visual pose cards", "Calm music", "Timer (hold each pose 30 seconds)", "Stuffed animal for breathing buddy"],
     ["Start with deep breaths (place stuffed animal on belly to watch it rise)", "Child's pose: curl into ball, forehead on floor (60 seconds)", "Cat-cow: arch and round back slowly (5 times)", "Tree pose: balance on one foot (30 seconds each side)", "End in savasana: lie flat, breathe, eyes closed (2 minutes)"],
     "Use visual cards for non-readers. Keep sessions SHORT (5-10 min). Do consistently same time daily."),
    ("SENSORY WALK / NATURE EXPLORATION", "All 8 Systems!", ["Shoes appropriate for terrain", "Collection bag", "Magnifying glass (optional)", "Camera/phone for photos", "Sensory checklist to fill out"],
     ["Walk slowly - this is NOT exercise, it is exploring", "Stop and notice: 5 things I see, 4 I hear, 3 I feel, 2 I smell, 1 I taste", "Collect natural items with different textures", "Walk on different surfaces: grass, gravel, mulch, concrete", "End with sitting quietly in nature for 2 minutes"],
     "Follow child's pace and interests. Bring preferred snack and water. Have exit plan if overwhelmed.")
]

for act_idx, (act_name, system, materials, steps, modifications) in enumerate(activities):
    pdf.new_page()
    pdf.add_centered_text(750, f"ACTIVITY {act_idx+1}: {act_name}", 'F2', 13)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    pdf.add_text(50, y, f"Sensory System Targeted: {system}", 'F2', 10)
    y -= 20
    pdf.add_text(50, y, "MATERIALS NEEDED:", 'F2', 10)
    y -= 14
    for mat in materials:
        pdf.add_text(60, y, f"- {mat}", 'F4', 9)
        y -= 12
    y -= 10
    pdf.add_text(50, y, "STEP-BY-STEP INSTRUCTIONS:", 'F2', 10)
    y -= 14
    for s_idx, step in enumerate(steps):
        pdf.add_text(60, y, f"{s_idx+1}. {step}", 'F4', 9)
        y -= 12
    y -= 10
    pdf.add_text(50, y, "MODIFICATIONS:", 'F2', 10)
    y -= 14
    # Wrap modification text
    mod_text = modifications
    while len(mod_text) > 78:
        split = mod_text[:78].rfind(' ')
        pdf.add_text(60, y, mod_text[:split], 'F4', 9)
        mod_text = mod_text[split+1:]
        y -= 12
    pdf.add_text(60, y, mod_text, 'F4', 9)
    y -= 20
    pdf.add_text(50, y, "OBSERVATIONS / NOTES:", 'F2', 10)
    y -= 14
    pdf.add_text(50, y, "Date tried: ___/___/___   Duration: ______ minutes", 'F1', 9)
    y -= 14
    pdf.add_text(50, y, "Child's response:  [ ] Loved it  [ ] Tolerated it  [ ] Refused  [ ] Meltdown", 'F1', 9)
    y -= 14
    pdf.add_text(50, y, "Regulation level BEFORE (1-5): ___   AFTER (1-5): ___", 'F1', 9)
    y -= 14
    pdf.add_text(50, y, "Notes:", 'F1', 9)
    pdf.add_line(85, y - 2, 562, y - 2, 0.3, 0.5)
    y -= 14
    pdf.add_line(50, y - 2, 562, y - 2, 0.3, 0.5)

# Page 22: Calm-Down Corner Setup Guide
pdf.new_page()
pdf.add_centered_text(750, "CALM-DOWN CORNER SETUP GUIDE", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
calm_text = [
    "Every child needs a SAFE SPACE to regulate. A calm-down corner is",
    "not punishment - it is a tool for self-regulation.",
    "",
    "LOCATION REQUIREMENTS:",
    "- Quiet area away from high-traffic zones",
    "- Low lighting (lamp instead of overhead fluorescents)",
    "- Enclosed feeling (tent, canopy, or corner with cushions)",
    "- Visible to adults (safety) but feels private to child",
    "",
    "ESSENTIAL ITEMS (check off as you gather):",
]
for line in calm_text:
    pdf.add_text(50, y, line, 'F4', 10)
    y -= 14
items_checklist = [
    "Soft seating (beanbag, cushion, or weighted blanket)",
    "Noise-canceling headphones",
    "Fidget tools (putty, tangle, stress ball)",
    "Visual timer (so child knows when to try returning)",
    "Feelings chart or emotion cards",
    "Breathing technique visual (poster or card)",
    "Favorite calming book or magazine",
    "Weighted stuffed animal or lap pad",
    "Dim lamp or fairy lights",
    "Sensory bottle (glitter jar to watch settle)"
]
for item in items_checklist:
    pdf.add_rect(60, y - 2, 9, 9, 0.4)
    pdf.add_text(74, y, item, 'F4', 9)
    y -= 14
y -= 10
pdf.add_text(50, y, "RULES FOR THE CALM-DOWN CORNER:", 'F2', 10)
y -= 14
rules = [
    "1. Anyone can use it anytime (it is NOT time-out)",
    "2. You can ask to go, or an adult can suggest it",
    "3. Stay until your body feels calm (use the visual timer)",
    "4. Take care of the items inside",
    "5. One person at a time"
]
for rule in rules:
    pdf.add_text(60, y, rule, 'F4', 9)
    y -= 13

# Page 23: Sensory Break Request Cards
pdf.new_page()
pdf.add_centered_text(750, "SENSORY BREAK REQUEST CARDS", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Cut out these cards for your child to use when they need a sensory break.", 'F4', 10)
y -= 14
pdf.add_text(50, y, "Laminate for durability. Teach child to hand card to adult.", 'F4', 10)
y -= 30
cards = [
    ("I NEED A BREAK", "My body feels too much right now. I need to go to my calm space."),
    ("I NEED TO MOVE", "My body needs to move. Can I take a movement break?"),
    ("IT IS TOO LOUD", "The sounds are too much. Can I use my headphones or go somewhere quiet?"),
    ("I NEED A SQUEEZE", "My body needs deep pressure. Can I have a hug or use my weighted blanket?"),
    ("I FEEL OVERWHELMED", "Everything feels like too much. I need help calming down."),
    ("I NEED A FIDGET", "My hands need something to do. Can I use my fidget tool?"),
    ("I NEED A DRINK/SNACK", "My body might need fuel. Can I have water or a crunchy snack?"),
    ("I AM DOING OKAY!", "My body feels regulated right now! I am ready to work/play.")
]
for card_title, card_text in cards:
    pdf.add_rect(50, y - 5, 512, 55, 1, 0)
    pdf.add_text(60, y + 35, card_title, 'F2', 12)
    pdf.add_text(60, y + 15, card_text, 'F4', 9)
    y -= 70

# Pages 24-27: Weekly Sensory Log (4 pages)
for log_week in range(1, 5):
    pdf.new_page()
    pdf.add_centered_text(750, f"WEEKLY SENSORY LOG - WEEK {log_week}", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 720
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        pdf.add_filled_rect(50, y - 3, 512, 14, 0.92)
        pdf.add_text(55, y, day, 'F2', 9)
        y -= 16
        pdf.add_text(55, y, "Morning regulation (1-5): ___  Activities used: _______________________", 'F1', 8)
        y -= 12
        pdf.add_text(55, y, "Afternoon regulation (1-5): ___ Meltdowns/shutdowns: ___  Trigger: ______", 'F1', 8)
        y -= 12
        pdf.add_text(55, y, "Evening regulation (1-5): ___  What helped: __________________________", 'F1', 8)
        y -= 12
        pdf.add_text(55, y, "Sleep quality: Good / Fair / Poor   Notes: ___________________________", 'F1', 8)
        y -= 18

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book125_Sensory_Activities_Workbook.pdf')
print("Book125_Sensory_Activities_Workbook.pdf created successfully!")
