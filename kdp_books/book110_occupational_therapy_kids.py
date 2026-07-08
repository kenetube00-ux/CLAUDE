from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

pdf.new_page()
pdf.add_centered_text(550, "OCCUPATIONAL THERAPY", 'F2', 18)
pdf.add_centered_text(525, "ACTIVITIES FOR KIDS", 'F2', 18)
pdf.add_centered_text(495, "Fine Motor & Sensory Workbook", 'F4', 13)
pdf.add_centered_text(400, "Home Activities to Build Skills", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 12)

pdf.new_page()
pdf.add_centered_text(600, f"Copyright 2025 {author}. All rights reserved.", 'F4', 10)
pdf.add_centered_text(575, "Consult with your child's OT for personalized recommendations.", 'F4', 9)

# Page 3: Pencil Grip Guide
pdf.new_page()
pdf.add_centered_text(750, "PENCIL GRIP GUIDE", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Proper pencil grip develops over time. Don't rush!", "",
    "DEVELOPMENTAL PROGRESSION:",
    "1. FIST GRIP (ages 1-2): Whole hand wraps around crayon",
    "2. DIGITAL PRONATE (ages 2-3): Fingers point down, wrist moves",
    "3. MODIFIED TRIPOD (ages 3-4): Thumb + 2 fingers, some wrist movement",
    "4. DYNAMIC TRIPOD (ages 4-6): Thumb + index + middle, fingers move", "",
    "THE IDEAL TRIPOD GRIP:",
    "- Pencil rests on middle finger",
    "- Thumb and index finger pinch gently",
    "- Ring and pinky fingers curl into palm for stability",
    "- Wrist is slightly extended (not bent)", "",
    "ACTIVITIES TO BUILD GRIP STRENGTH:",
    "- Tear paper into small pieces (builds pinch strength)",
    "- Squeeze play dough / theraputty",
    "- Pick up small objects with tweezers",
    "- Lacing and threading beads",
    "- Opening and closing clothespins",
    "- Spinning tops between thumb and fingers",
    "- Drawing on a vertical surface (builds wrist position)", "",
    "PENCIL GRIPS TO TRY (if needed):",
    "- Triangular grip", "- Crossover grip", "- The Pencil Grip brand"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 4: Cutting Skills
pdf.new_page()
pdf.add_centered_text(750, "CUTTING SKILLS PROGRESSION", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Scissor skills develop in a specific order:", "",
    "LEVEL 1: SNIPPING (ages 2-3)",
    "- Open/close scissors (snip play dough first!)",
    "- Single snips across paper strips",
    "- Cut fringe along edge of paper", "",
    "LEVEL 2: STRAIGHT LINES (ages 3-4)",
    "- Cut along wide straight lines (start with 1-inch paths)",
    "- Cut across a full sheet of paper",
    "- Cut between two parallel lines", "",
    "LEVEL 3: CURVED LINES (ages 4-5)",
    "- Cut gentle curves",
    "- Cut wavy lines",
    "- Cut along zigzag lines", "",
    "LEVEL 4: SHAPES (ages 5-6)",
    "- Cut out circles (hardest shape!)",
    "- Cut out squares and triangles",
    "- Cut out complex shapes", "",
    "TIPS FOR SUCCESS:",
    "- Thumb goes on top, fingers on bottom",
    "- 'Thumbs up!' position",
    "- Stabilizing hand holds and turns the paper",
    "- Use spring-loaded scissors for beginners",
    "- Practice with play dough before paper"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Pages 5-7: Tracing Paths (dotted lines)
for level in range(3):
    pdf.new_page()
    titles = ["TRACING PATHS - EASY", "TRACING PATHS - MEDIUM", "TRACING PATHS - HARD"]
    pdf.add_centered_text(750, titles[level], 'F2', 15)
    pdf.add_line(60, 738, 552, 738)
    y = 710
    pdf.add_text(60, y, "Trace along the dotted paths from START to END:", 'F2', 10)
    y -= 30
    # Draw dotted paths using short line segments
    for path in range(4):
        pdf.add_text(60, y, "START", 'F2', 8)
        pdf.add_text(520, y, "END", 'F2', 8)
        # Create dotted line effect
        for dot in range(0, 420, 8):
            pdf.add_line(95 + dot, y+2, 95 + dot + 3, y+2, 0.5, 0.4)
        y -= 15
        if level >= 1:  # curved - add wave pattern
            for dot in range(0, 420, 8):
                offset = (dot % 40 - 20) * 0.5
                pdf.add_line(95 + dot, y+2+offset, 95 + dot + 3, y+2+offset, 0.5, 0.4)
            y -= 15
        if level >= 2:  # zigzag
            for dot in range(0, 420, 8):
                offset = (dot % 30) - 15
                pdf.add_line(95 + dot, y+2+offset, 95 + dot + 3, y+2+offset, 0.5, 0.4)
            y -= 15
        y -= 40

# Page 8: Bead Pattern Copying
pdf.new_page()
pdf.add_centered_text(750, "BEAD PATTERN COPYING", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
pdf.add_text(60, y, "Copy the pattern on the left to the empty spaces on the right:", 'F2', 10)
y -= 30
patterns = ["O O X O O X", "X O O X O O", "O X O X O X", "X X O O X X", "O X X O X X"]
for i, pattern in enumerate(patterns):
    pdf.add_text(60, y, f"Pattern {i+1}:", 'F2', 10)
    y -= 18
    pdf.add_text(80, y, pattern, 'F3', 14)
    pdf.add_text(300, y, "__ __ __ __ __ __", 'F3', 14)
    y -= 30

# Page 9: Finger Strengthening
pdf.new_page()
pdf.add_centered_text(750, "FINGER STRENGTHENING EXERCISES", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Strong fingers = better handwriting, cutting, and self-care!", "",
    "PUTTY/PLAY DOUGH EXERCISES:",
    "1. Roll into a snake (palms together, forward/back)",
    "2. Pinch off small pieces (thumb + each finger)",
    "3. Poke holes with each finger individually",
    "4. Hide small beads inside, then find them",
    "5. Flatten with palm, then roll back into ball", "",
    "CLOTHESPIN ACTIVITIES:",
    "1. Clip clothespins around a paper plate edge",
    "2. Pick up cotton balls with clothespin 'tweezers'",
    "3. Clip matching colors to color cards",
    "4. Build a tower of clothespins", "",
    "EVERYDAY ACTIVITIES THAT BUILD STRENGTH:",
    "- Opening containers and jars (with help)",
    "- Squeezing sponges in the bath",
    "- Pulling apart building blocks (Lego, Duplo)",
    "- Spray bottles (watering plants!)",
    "- Hole punch (great for pinch strength!)",
    "- Tearing lettuce for salad",
    "- Peeling stickers off a sheet",
    "- Buttoning and zipping own clothes", "",
    "DAILY PRACTICE: Choose 2-3 activities, 5-10 minutes each."
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Page 10: Visual Motor + Sensory Diet
pdf.new_page()
pdf.add_centered_text(750, "SENSORY DIET BUILDER", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "A 'sensory diet' is a planned schedule of sensory activities", 
    "to help your child stay regulated throughout the day.", "",
    "ALERTING ACTIVITIES (wakes up the brain):",
    "__ Jumping on trampoline    __ Cold water on hands",
    "__ Crunchy foods            __ Bright lights",
    "__ Fast music               __ Spinning (briefly)", "",
    "CALMING ACTIVITIES (settles the brain):",
    "__ Deep pressure (bear hugs, weighted blanket)",
    "__ Slow rocking             __ Warm bath",
    "__ Quiet music              __ Dim lighting",
    "__ Chewy foods/gum          __ Proprioception (heavy work)", "",
    "HEAVY WORK (proprioceptive input - universally calming):",
    "__ Carrying groceries       __ Pushing laundry basket",
    "__ Climbing                 __ Wheelbarrow walks",
    "__ Animal walks             __ Pulling wagon",
    "__ Wall push-ups            __ Digging in sand", "",
    "MY CHILD'S SENSORY SCHEDULE:",
    "Morning: _____________________________________",
    "Before school: ________________________________",
    "After school: _________________________________",
    "Before homework: ______________________________",
    "Before bed: ___________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16


# Page 11: Self-Regulation Zones
pdf.new_page()
pdf.add_centered_text(750, "SELF-REGULATION ZONES", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Help your child identify and manage their energy levels:", "",
    "HIGH ZONE (too much energy/too fast):",
    "Feels like: silly, wild, angry, scared, out of control",
    "Tools to come DOWN: deep breaths, heavy work, quiet space,",
    "  bear hug, weighted lap pad, drink water through straw", "",
    "JUST RIGHT ZONE (ready to learn and play):",
    "Feels like: calm, focused, happy, ready",
    "This is where we want to be for learning!", "",
    "LOW ZONE (too little energy/too slow):",
    "Feels like: tired, bored, sad, sick, zoned out",
    "Tools to come UP: movement break, crunchy snack, cold water,",
    "  jumping jacks, music, bright light, fidget tool", "",
    "MY CHILD'S SIGNS FOR EACH ZONE:",
    "HIGH: ________________________________________",
    "JUST RIGHT: __________________________________",
    "LOW: __________________________________________", "",
    "TOOLS THAT WORK FOR MY CHILD:",
    "To calm down: _________________________________",
    "To wake up: __________________________________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

# Pages 12-16: Daily OT Home Program Planner (5 pages)
for week in range(1, 6):
    pdf.new_page()
    pdf.add_centered_text(750, f"DAILY OT HOME PROGRAM - WEEK {week}", 'F2', 14)
    pdf.add_line(60, 738, 552, 738)
    y = 720
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        pdf.add_text(60, y, f"{day}:", 'F2', 9)
        y -= 13
        pdf.add_text(70, y, "Fine motor activity: ___________________________", 'F3', 8)
        y -= 12
        pdf.add_text(70, y, "Gross motor/sensory: ___________________________", 'F3', 8)
        y -= 12
        pdf.add_text(70, y, "Self-care practice: ____ Duration: ____ Mood: ____", 'F3', 8)
        y -= 16
        pdf.add_line(60, y+5, 552, y+5, 0.3, 0.7)
        y -= 6

# Page 17: Progress Tracking
pdf.new_page()
pdf.add_centered_text(750, "PROGRESS TRACKING & OT GOALS", 'F2', 15)
pdf.add_line(60, 738, 552, 738)
y = 715
for line in [
    "Track your child's OT progress:", "",
    "GOAL 1: ______________________________________",
    "Start date: _______ Baseline: _________________",
    "Week 2: ____________ Week 4: _________________",
    "Week 6: ____________ Week 8: _________________", "",
    "GOAL 2: ______________________________________",
    "Start date: _______ Baseline: _________________",
    "Week 2: ____________ Week 4: _________________",
    "Week 6: ____________ Week 8: _________________", "",
    "GOAL 3: ______________________________________",
    "Start date: _______ Baseline: _________________",
    "Week 2: ____________ Week 4: _________________",
    "Week 6: ____________ Week 8: _________________", "",
    "SKILLS MASTERED (celebrate!):",
    "__ ______________________ Date: _______________",
    "__ ______________________ Date: _______________",
    "__ ______________________ Date: _______________",
    "__ ______________________ Date: _______________",
    "__ ______________________ Date: _______________"
]:
    pdf.add_text(60, y, line, 'F4', 10)
    y -= 16

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book110_OT_Activities_Kids.pdf')
print("Book110_OT_Activities_Kids.pdf created successfully!")
