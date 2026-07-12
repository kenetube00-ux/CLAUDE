"""Book 219: The ADHD Life Management System"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    # Title
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.15)
    doc.add_centered_text(755, "THE ADHD LIFE", 'F2', 26, 1)
    doc.add_centered_text(722, "MANAGEMENT SYSTEM", 'F2', 26, 1)
    doc.add_centered_text(660, "Complete Organization for Every Area of Life", 'F4', 14, 0.3)
    doc.add_centered_text(620, "Time | Space | Tasks | Money | Relationships", 'F1', 12, 0.4)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    # Copyright
    doc.new_page()
    doc.add_centered_text(700, "THE ADHD LIFE MANAGEMENT SYSTEM", 'F2', 14)
    doc.add_centered_text(670, f"Copyright {author}", 'F1', 10)
    doc.add_centered_text(650, "All rights reserved.", 'F1', 10)
    doc.add_centered_text(600, "Designed specifically for how ADHD brains actually work.", 'F4', 11)

    # Page 3: Why Traditional Systems Fail
    doc.new_page()
    doc.add_centered_text(750, "WHY TRADITIONAL SYSTEMS FAIL ADHD BRAINS", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = [
        "Traditional planners assume you have:", "",
        "  - Consistent working memory (you don't)",
        "  - Natural sense of time passing (you don't)",
        "  - Automatic prioritization (you don't)",
        "  - Built-in reward for boring tasks (you don't)",
        "  - Ability to 'just start' (executive dysfunction is real)", "",
        "This system is different because:", "",
        "  - Visual over text-heavy",
        "  - External structure replaces internal executive function",
        "  - Dopamine-friendly rewards built in",
        "  - Accommodates hyperfocus AND low-energy days",
        "  - No guilt, no 'catching up' - fresh starts daily",
        "  - Combines ALL life areas so nothing falls through cracks", "",
        "The 5-System Approach:", "",
        "  1. TIME - External clocks for internal time blindness",
        "  2. SPACE - Visual systems for out-of-sight-out-of-mind",
        "  3. TASKS - Energy-matched, dopamine-paired action lists",
        "  4. MONEY - Autopilot finances with impulse guardrails",
        "  5. RELATIONSHIPS - Social energy budgets and scripts",
    ]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 16


    # System 1: Time Management (5 pages)
    time_pages = [
        ("BODY DOUBLING PLANNER", [
            "Body doubling = having someone present while you work.", "",
            "My body doubling options:", "In-person: ________________________________",
            "Virtual: ________________________________",
            "Apps/videos: ________________________________", "",
            "Tasks that need body doubling:", "________________________________",
            "________________________________", "",
            "Schedule: Mon ___ Tue ___ Wed ___ Thu ___ Fri ___"]),
        ("TIME BLINDNESS TOOLS", [
            "My time estimation practice:", "",
            "Task: _________________ Estimated: ___ Actual: ___",
            "Task: _________________ Estimated: ___ Actual: ___",
            "Task: _________________ Estimated: ___ Actual: ___",
            "Task: _________________ Estimated: ___ Actual: ___", "",
            "Rule: Multiply my estimate by ___ (usually 2-3x)", "",
            "Visual timers I use: ________________________________",
            "Alarms set for: ________________________________"]),
        ("TRANSITION WARNINGS", [
            "Transitions are HARD. Plan for them.", "",
            "Morning transition (bed to productive):",
            "10-min warning: ___  5-min: ___  Action: ___", "",
            "Task-to-task transition:",
            "What helps me switch: ________________________________", "",
            "Leaving the house transition:",
            "Items needed (by door): ________________________________",
            "Time buffer added: ___ minutes", "",
            "Bedtime transition (screen to sleep):",
            "Wind-down routine: ________________________________"]),
        ("TIME BLOCKING (ADHD Style)", [
            "Theme days work better than hourly blocks.", "",
            "Monday theme: ________________________________",
            "Tuesday theme: ________________________________",
            "Wednesday theme: ________________________________",
            "Thursday theme: ________________________________",
            "Friday theme: ________________________________", "",
            "Non-negotiable anchors (things that MUST happen):",
            "Morning anchor: ________________________________",
            "Afternoon anchor: ________________________________",
            "Evening anchor: ________________________________"]),
        ("HYPERFOCUS MANAGEMENT", [
            "Hyperfocus is a SUPERPOWER when directed.", "",
            "My hyperfocus triggers: ________________________________",
            "Topics I easily hyperfocus on: ________________________________", "",
            "Guardrails for unproductive hyperfocus:",
            "Timer set for: ___ hours",
            "Check-in alarm every: ___ minutes",
            "Accountability partner to text: _______________", "",
            "Directing hyperfocus productively:",
            "Project to channel it into: ________________________________",
            "Best time of day for deep work: ________________________________",
            "Environment that supports focus: ________________________________"]),
    ]
    for title, content in time_pages:
        doc.new_page()
        doc.add_centered_text(755, "SYSTEM 1: TIME MANAGEMENT", 'F2', 11, 0.4)
        doc.add_centered_text(733, title, 'F2', 14)
        doc.add_line(72, 720, 540, 720, 0.5, 0.3)
        y = 695
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 18


    # System 2: Space (5 pages)
    space_pages = [
        ("DUMP ZONES", ["Designated spots where stuff lands. Not mess - systems.", "",
            "Entry dump zone (keys/wallet/bag): ________________________________",
            "Kitchen dump zone (mail/papers): ________________________________",
            "Bedroom dump zone (clothes): ________________________________",
            "Work dump zone (projects): ________________________________", "",
            "Weekly dump zone reset day: ________________________________",
            "Time needed: ___ minutes"]),
        ("LAUNCHING PADS", ["Everything you need to leave = one spot.", "",
            "Morning launch pad location: ________________________________",
            "Items always there: ________________________________",
            "________________________________", "",
            "Work launch pad: ________________________________",
            "Gym launch pad: ________________________________",
            "Errands launch pad: ________________________________"]),
        ("VISUAL CUES", ["If you can't see it, it doesn't exist.", "",
            "Clear containers for: ________________________________",
            "Open shelving for: ________________________________",
            "Whiteboard locations: ________________________________",
            "Sticky note stations: ________________________________", "",
            "Color coding system:", "Red = _____________ Blue = _____________",
            "Green = _____________ Yellow = _____________"]),
        ("15-MINUTE ROOM RESETS", ["Set timer. Do what you can. STOP when it rings.", "",
            "Kitchen reset (15 min): dishes, counters, floor",
            "Bedroom reset (15 min): bed, clothes, surfaces",
            "Bathroom reset (15 min): counter, toilet, floor",
            "Living room reset (15 min): surfaces, pillows, trash", "",
            "My reset schedule:",
            "Mon: _______ Tue: _______ Wed: _______",
            "Thu: _______ Fri: _______ Sat: _______"]),
        ("ORGANIZATION THAT WORKS", ["Simple = sustainable for ADHD.", "",
            "Rules: 1 touch (handle it once), visible, labeled, easy", "",
            "Area 1: _____________ System: _____________",
            "Area 2: _____________ System: _____________",
            "Area 3: _____________ System: _____________", "",
            "Things I will NEVER organize perfectly (let go):",
            "________________________________",
            "Good enough = ________________________________"]),
    ]
    for title, content in space_pages:
        doc.new_page()
        doc.add_centered_text(755, "SYSTEM 2: SPACE", 'F2', 11, 0.4)
        doc.add_centered_text(733, title, 'F2', 14)
        doc.add_line(72, 720, 540, 720, 0.5, 0.3)
        y = 695
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 18


    # System 3: Tasks (5 pages)
    task_pages = [
        ("2-MINUTE RULE", ["If it takes less than 2 minutes, do it NOW.", "",
            "2-minute tasks I keep putting off:",
            "________________________________", "________________________________",
            "________________________________", "________________________________", "",
            "My 2-minute wins today:", "________________________________",
            "________________________________", "________________________________"]),
        ("CONTEXT LISTS", ["Group tasks by WHERE/WHEN, not priority.", "",
            "At Computer: ________________________________",
            "________________________________",
            "On Phone: ________________________________",
            "________________________________",
            "At Store: ________________________________",
            "________________________________",
            "With Energy: ________________________________",
            "________________________________",
            "Low Energy: ________________________________",
            "________________________________"]),
        ("ENERGY MATCHING", ["Match task difficulty to energy level.", "",
            "HIGH energy tasks: ________________________________",
            "________________________________",
            "MEDIUM energy tasks: ________________________________",
            "________________________________",
            "LOW energy (zombie mode) tasks: ________________________________",
            "________________________________", "",
            "My energy pattern: Morning=___ Afternoon=___ Evening=___"]),
        ("REWARD PAIRING", ["Pair boring tasks with dopamine.", "",
            "Task: _____________ + Reward: _____________",
            "Task: _____________ + Reward: _____________",
            "Task: _____________ + Reward: _____________",
            "Task: _____________ + Reward: _____________", "",
            "My dopamine menu (healthy rewards):",
            "5-min rewards: ________________________________",
            "15-min rewards: ________________________________",
            "Big rewards: ________________________________"]),
        ("GETTING UNSTUCK", ["When executive dysfunction hits:", "",
            "[ ] Change environment (move to different room)",
            "[ ] Make task smaller (what's the TINIEST first step?)",
            "[ ] Body double (get someone present)",
            "[ ] Set timer for just 5 minutes",
            "[ ] Pair with music/podcast",
            "[ ] Use countdown (5-4-3-2-1-GO)",
            "[ ] Change the task (do something else productive)",
            "[ ] Accept: today is not the day (self-compassion)", "",
            "My personal unstuck tricks:",
            "________________________________", "________________________________"]),
    ]
    for title, content in task_pages:
        doc.new_page()
        doc.add_centered_text(755, "SYSTEM 3: TASKS", 'F2', 11, 0.4)
        doc.add_centered_text(733, title, 'F2', 14)
        doc.add_line(72, 720, 540, 720, 0.5, 0.3)
        y = 695
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 18

    # System 4: Money (5 pages)
    money_pages = [
        ("AUTO-PILOT FINANCES", ["Remove decisions. Automate everything.", "",
            "Auto-pay bills (list all): ________________________________",
            "________________________________", "________________________________",
            "Auto-transfer to savings: $____ on ___th",
            "Auto-transfer to fun money: $____ on ___th", "",
            "Accounts:", "Checking (bills): ________________________________",
            "Savings (emergency): ________________________________",
            "Fun money (impulsive spending): ________________________________"]),
        ("IMPULSE PAUSE", ["ADHD brains seek novelty. Impulse spending is dopamine.", "",
            "My impulse spending triggers: ________________________________",
            "________________________________", "",
            "The 48-Hour Rule: Want it? Wait 48 hours. Still want it?", "",
            "Item: _____________ Date wanted: ___ Still want on ___? Y/N",
            "Item: _____________ Date wanted: ___ Still want on ___? Y/N",
            "Item: _____________ Date wanted: ___ Still want on ___? Y/N",
            "Item: _____________ Date wanted: ___ Still want on ___? Y/N", "",
            "Monthly impulse budget (guilt-free): $___"]),
        ("BILL VISUAL CALENDAR", ["If it's not visible, it won't get paid.", "",
            "1st: _____________ $___   16th: _____________ $___",
            "2nd: _____________ $___   17th: _____________ $___",
            "5th: _____________ $___   20th: _____________ $___",
            "8th: _____________ $___   22nd: _____________ $___",
            "10th: _____________ $___  25th: _____________ $___",
            "12th: _____________ $___  28th: _____________ $___",
            "15th: _____________ $___  30th: _____________ $___", "",
            "Total monthly bills: $___",
            "Income: $___  Remaining: $___"]),
        ("MONEY FEELINGS", ["ADHD + money shame = avoidance. Break the cycle.", "",
            "My money story: ________________________________",
            "________________________________",
            "Shame triggers: ________________________________",
            "When I avoid finances, it's because: ________________________________", "",
            "Small money wins this week:",
            "[ ] Checked bank balance", "[ ] Paid one bill",
            "[ ] Said no to one purchase", "[ ] Moved $1 to savings", "",
            "Affirmation: I am learning. Progress, not perfection."]),
        ("SUBSCRIPTION AUDIT", ["Monthly subscriptions add up invisibly.", "",
            "Subscription: _____________ $___/mo  Keep? Y/N",
            "Subscription: _____________ $___/mo  Keep? Y/N",
            "Subscription: _____________ $___/mo  Keep? Y/N",
            "Subscription: _____________ $___/mo  Keep? Y/N",
            "Subscription: _____________ $___/mo  Keep? Y/N",
            "Subscription: _____________ $___/mo  Keep? Y/N",
            "Subscription: _____________ $___/mo  Keep? Y/N",
            "Subscription: _____________ $___/mo  Keep? Y/N", "",
            "Total: $___/mo = $___/year",
            "After audit: $___/mo = $___/year  Saved: $___"]),
    ]
    for title, content in money_pages:
        doc.new_page()
        doc.add_centered_text(755, "SYSTEM 4: MONEY", 'F2', 11, 0.4)
        doc.add_centered_text(733, title, 'F2', 14)
        doc.add_line(72, 720, 540, 720, 0.5, 0.3)
        y = 695
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 18


    # System 5: Relationships (5 pages)
    rel_pages = [
        ("SOCIAL ENERGY BUDGET", ["Social interaction costs energy. Budget it.", "",
            "My social battery capacity (1-10): ___", "",
            "Low-cost interactions: ________________________________",
            "Medium-cost: ________________________________",
            "High-cost (draining): ________________________________", "",
            "This week's social budget:", "Mon: ___ Tue: ___ Wed: ___ Thu: ___ Fri: ___",
            "Planned recovery time: ________________________________"]),
        ("COMMUNICATION TEMPLATES", ["Pre-written scripts reduce executive load.", "",
            "Running late: 'Hey! Running about ___ minutes late. So sorry!'",
            "Canceling: 'I need to reschedule. Can we do ___?'",
            "Saying no: 'I appreciate you thinking of me. I can't this time.'",
            "Apologizing: 'I'm sorry I ___. I should have ___.'",
            "Asking for help: 'I'm struggling with ___. Could you ___?'", "",
            "My custom scripts:", "________________________________",
            "________________________________", "________________________________"]),
        ("APOLOGY SCRIPTS", ["ADHD means more apologies. Have them ready.", "",
            "For forgetting: 'I'm sorry I forgot ___. It's not that I don't",
            "  care - my brain dropped it. How can I make it up to you?'", "",
            "For being late: 'I'm sorry for being late. I know your time",
            "  matters. I'm working on systems to be more punctual.'", "",
            "For interrupting: 'I'm sorry I interrupted. I got excited.",
            "  Please continue - I want to hear what you were saying.'", "",
            "For zoning out: 'I'm sorry, I drifted. Can you repeat that?",
            "  I want to give you my full attention.'", "",
            "My personalized apology:", "________________________________"]),
        ("RELATIONSHIP MAINTENANCE", ["Relationships need proactive maintenance.", "",
            "Key people & check-in schedule:",
            "_____________ : Every ___ days  Last: ___/___",
            "_____________ : Every ___ days  Last: ___/___",
            "_____________ : Every ___ days  Last: ___/___",
            "_____________ : Every ___ days  Last: ___/___",
            "_____________ : Every ___ days  Last: ___/___", "",
            "Phone reminders set? [ ] Yes",
            "Calendar blocks for social time? [ ] Yes"]),
        ("EXPLAINING ADHD TO OTHERS", ["Not excuses - education.", "",
            "To my partner: 'When I ___, it's because my brain ___.",
            "  What would help us both is ___.'", "",
            "To my boss: 'I work best when ___. Could we ___?'", "",
            "To friends: 'I might forget to text back. It's not personal.",
            "  Please don't stop inviting me.'", "",
            "My ADHD strengths to share:", "________________________________",
            "________________________________",
            "Accommodations I need:", "________________________________",
            "________________________________"]),
    ]
    for title, content in rel_pages:
        doc.new_page()
        doc.add_centered_text(755, "SYSTEM 5: RELATIONSHIPS", 'F2', 11, 0.4)
        doc.add_centered_text(733, title, 'F2', 14)
        doc.add_line(72, 720, 540, 720, 0.5, 0.3)
        y = 695
        for line in content:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 18

    # Daily Pages combining all 5 systems (10 pages)
    for day in range(1, 11):
        doc.new_page()
        doc.add_centered_text(760, f"DAILY PAGE - DAY {day}", 'F2', 13)
        doc.add_text(72, 742, "Date: ___/___/___  Energy level: ___/10", 'F1', 9)
        doc.add_line(72, 735, 540, 735, 0.5, 0.3)
        y = 715
        doc.add_text(72, y, "TIME: Today's non-negotiable anchors:", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "Morning: ___________  Afternoon: ___________  Evening: ___________", 'F1', 8)
        y -= 20
        doc.add_text(72, y, "SPACE: 15-min reset target room: ___________  Done? [ ]", 'F2', 9)
        y -= 20
        doc.add_text(72, y, "TASKS (energy-matched):", 'F2', 9)
        y -= 14
        doc.add_text(90, y, "High energy: [ ] ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Med energy:  [ ] ________________________________", 'F1', 8)
        y -= 12
        doc.add_text(90, y, "Low energy:  [ ] ________________________________", 'F1', 8)
        y -= 20
        doc.add_text(72, y, "MONEY: Did I check balance? [ ]  Impulse resisted? [ ]", 'F2', 9)
        y -= 20
        doc.add_text(72, y, "RELATIONSHIPS: Connection made today: ___________", 'F2', 9)
        y -= 20
        doc.add_text(72, y, "Reward earned: ________________________________", 'F1', 9)
        y -= 15
        doc.add_text(72, y, "Tomorrow's #1 priority: ________________________________", 'F1', 9)

    # Weekly Review (4 pages)
    for week in range(1, 5):
        doc.new_page()
        doc.add_centered_text(755, f"WEEKLY REVIEW - WEEK {week}", 'F2', 14)
        doc.add_line(72, 740, 540, 740, 0.5, 0.3)
        y = 715
        sections = [
            "TIME: Transition successes: ________________________________",
            "TIME: Where I lost time: ________________________________",
            "SPACE: Rooms reset this week: ________________________________",
            "TASKS: Completed: ___/___  Biggest win: ________________________________",
            "MONEY: Budget on track? [ ] Impulses managed? [ ]",
            "RELATIONSHIPS: Connections made: ________________________________", "",
            "What worked this week: ________________________________",
            "What to adjust: ________________________________",
            "Self-compassion note: ________________________________", "",
            "Next week's focus: ________________________________",
        ]
        for line in sections:
            doc.add_text(72, y, line, 'F1', 10)
            y -= 22

    # Monthly Reset Checklist
    doc.new_page()
    doc.add_centered_text(755, "MONTHLY RESET CHECKLIST", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    items = [
        "[ ] Review & update all auto-pays",
        "[ ] Check subscriptions - cancel unused",
        "[ ] Deep clean one dump zone",
        "[ ] Update context lists",
        "[ ] Check in with 3 important people",
        "[ ] Review time estimates - adjust multiplier",
        "[ ] Celebrate 3 wins from this month",
        "[ ] Set next month's theme days",
        "[ ] Restock launch pads",
        "[ ] Update visual calendar",
        "[ ] Body doubling schedule confirmed",
        "[ ] Rewards menu refreshed",
    ]
    for item in items:
        doc.add_text(72, y, item, 'F1', 11)
        y -= 22

    # My Personalized ADHD Manual
    doc.new_page()
    doc.add_centered_text(755, "MY PERSONALIZED ADHD MANUAL", 'F2', 14)
    doc.add_line(72, 740, 540, 740, 0.5, 0.3)
    y = 715
    prompts = [
        "My ADHD type/profile: ________________________________",
        "Medication (if applicable): ________________________________",
        "Best time of day for focus: ________________________________",
        "Worst time (don't schedule hard things): ________________________________", "",
        "My top 3 strengths: ________________________________",
        "My top 3 challenges: ________________________________", "",
        "What recharges me: ________________________________",
        "What drains me: ________________________________", "",
        "Accommodations that help:", "________________________________",
        "________________________________", "",
        "My ADHD-friendly systems that work:", "________________________________",
        "________________________________", "",
        "When I'm struggling, I will:", "________________________________",
        "________________________________", "",
        "I am not broken. I am differently wired. My ADHD is also my:",
        "________________________________",
    ]
    for line in prompts:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 20

    doc.save("Book219_ADHD_Life_System.pdf")
    print("Created: Book219_ADHD_Life_System.pdf")

if __name__ == "__main__":
    create_book()
