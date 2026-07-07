"""
Book 69: How To Train Your Puppy - Positive Methods That Actually Work
KDP Interior - 6x9 inches (432x648 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(432, 648)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(520, "HOW TO TRAIN YOUR PUPPY", font='F2', size=22)
    pdf.add_centered_text(485, "Positive Methods That Actually Work", font='F1', size=14)
    pdf.add_line(80, 460, 352, 460, 2)
    pdf.add_centered_text(420, "Raise a Well-Behaved, Happy Dog", font='F4', size=13)
    pdf.add_centered_text(398, "Using Science-Based Training", font='F4', size=13)
    pdf.add_centered_text(330, "By", font='F1', size=12)
    pdf.add_centered_text(305, "Daniel Tesfamariam", font='F2', size=16)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(500, "How To Train Your Puppy", font='F2', size=11)
    pdf.add_centered_text(475, "Positive Methods That Actually Work", font='F1', size=10)
    pdf.add_centered_text(445, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=9)
    pdf.add_centered_text(420, "No part of this book may be reproduced without permission.", font='F1', size=9)
    pdf.add_centered_text(390, "Author: Daniel Tesfamariam", font='F2', size=10)
    pdf.add_centered_text(365, "Published via Amazon KDP", font='F1', size=10)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: Puppy-Proofing Your Home", [
            "Puppies explore the world with their mouths and will chew everything in reach.",
            "Get on your hands and knees to see your home from a puppy's eye level.",
            "Secure electrical cords with cord covers or tape them to baseboards.",
            "Move toxic plants, cleaning supplies, and medications to high shelves or locked cabinets.",
            "Pick up small items like coins, buttons, and hair ties that could be swallowed.",
            "Block access to stairs and off-limits rooms with baby gates.",
            "Remove shoes, socks, and children's toys from the floor during the puppy phase.",
            "Secure trash cans with lids or move them inside cabinets with child locks.",
            "Cover or block access to low furniture openings where puppies can get stuck.",
            "Check your yard for toxic plants, gaps in fencing, and pools without barriers.",
            "Put away any item you value that the puppy could reach and destroy.",
            "Puppy-proofing prevents accidents and protects both your belongings and your puppy.",
        ]),
        ("Chapter 2: The First Night Home", [
            "Bring your puppy home early in the day so they have time to explore before bedtime.",
            "Introduce one room at a time rather than giving access to the entire house.",
            "Take your puppy outside immediately upon arriving home for a bathroom break.",
            "Show them their food and water bowls, crate, and bed location.",
            "Keep the first day calm. Avoid overwhelming the puppy with too many new people.",
            "Children should be gentle and sit on the floor rather than chase the puppy.",
            "Place the crate in your bedroom for the first few nights so puppy hears you.",
            "Expect crying the first night. Your puppy is away from their mother and siblings.",
            "A warm water bottle wrapped in a towel mimics the warmth of littermates.",
            "A ticking clock or white noise machine can soothe a restless puppy.",
            "Take the puppy out for a bathroom break once during the night at first.",
            "The first night is hardest for both of you. It gets better within three to five days.",
        ]),
        ("Chapter 3: Crate Training Basics", [
            "A crate is not a punishment. Dogs are den animals and crates provide security.",
            "Choose a crate just large enough for your puppy to stand, turn, and lie down.",
            "Too large a crate allows the puppy to soil one end and sleep in the other.",
            "Introduce the crate gradually. Toss treats inside and let the puppy explore freely.",
            "Feed meals inside the crate so it becomes associated with positive experiences.",
            "Close the door for short periods while you sit nearby, then gradually increase time.",
            "Never use the crate as punishment or force a panicking puppy inside.",
            "Cover the crate with a blanket to create a cozy den-like environment.",
            "Young puppies should not stay crated longer than their age in months plus one hour.",
            "An eight-week-old puppy can hold it for about three hours maximum.",
            "A properly crate-trained puppy will voluntarily go to their crate for naps.",
            "Crate training makes housetraining, vet visits, and travel much easier.",
        ]),
        ("Chapter 4: Potty Training Step by Step", [
            "Take your puppy outside immediately after waking, eating, drinking, and playing.",
            "Choose one designated bathroom spot and take them there every single time.",
            "Use a consistent phrase like go potty so they learn what you are asking.",
            "Wait patiently outside for up to five minutes. Do not play until they go.",
            "Praise enthusiastically and give a small treat the instant they finish.",
            "Take puppies out every 30 to 60 minutes when awake during the early weeks.",
            "Watch for signs they need to go: sniffing, circling, squatting, or whining.",
            "If you catch them starting to go inside, interrupt gently and rush outside.",
            "Never punish accidents after the fact. Puppies cannot connect past actions to punishment.",
            "Clean indoor accidents thoroughly with enzyme cleaner to remove all odor.",
            "Regular schedule: out first thing, after meals, after naps, after play, before bed.",
            "Most puppies are reliably housetrained between four and six months with consistency.",
        ]),
        ("Chapter 5: Teaching Sit and Stay", [
            "Sit is the first and most useful command every puppy should learn.",
            "Hold a treat close to your puppy's nose and slowly move it up and back.",
            "As their nose follows the treat up, their bottom naturally lowers to the ground.",
            "The instant their bottom touches the floor, say yes and give the treat.",
            "Add the word sit only after the puppy reliably performs the motion.",
            "Practice five to ten repetitions then take a break. Short sessions work best.",
            "Once sit is solid, introduce stay by asking for sit then pausing before treating.",
            "Hold your palm up like a stop sign and say stay in a calm, firm voice.",
            "Start with just one second of stay and reward. Build duration gradually.",
            "Take one small step back. If they hold, return and reward generously.",
            "If they break the stay, simply reset without punishment and try shorter duration.",
            "Always release with a consistent word like okay or free before they move.",
        ]),
        ("Chapter 6: Teaching Come and Down", [
            "Come (recall) is the most important safety command your dog will ever learn.",
            "Start in a quiet room with minimal distractions. Crouch down and say come happily.",
            "When the puppy runs to you, celebrate like it is the best thing that ever happened.",
            "Never call your puppy to come and then do something unpleasant like crate or bath.",
            "Practice recall during play: call them, reward, then let them go play again.",
            "Use a long training leash in the yard before trusting off-leash recall.",
            "Make yourself more exciting than whatever distracted them. Use high-value treats.",
            "Down means lie all the way down with belly on the floor.",
            "From a sit, hold a treat at their nose and slowly lower it straight to the ground.",
            "When they follow the treat down and their elbows touch the floor, reward instantly.",
            "Some puppies resist down. Try luring under a low surface like your bent leg.",
            "Practice both commands daily in short two-minute sessions for best retention.",
        ]),
        ("Chapter 7: Leash Walking Without Pulling", [
            "Start leash training indoors where there are fewer distractions.",
            "Let your puppy wear the collar and leash around the house to get comfortable.",
            "Hold treats at your side and reward the puppy for walking beside you.",
            "When the leash gets tight, stop completely. Do not move forward while pulling.",
            "Wait for the puppy to look back at you or create slack, then continue walking.",
            "Reward every few steps initially when the leash stays loose.",
            "Change direction frequently to teach the puppy to pay attention to where you go.",
            "Use a front-clip harness to reduce pulling power without causing discomfort.",
            "Avoid retractable leashes which teach dogs that pulling creates more freedom.",
            "Practice in low-distraction areas before attempting busy sidewalks or parks.",
            "Sniff breaks are important. Let your puppy smell on your terms as a reward.",
            "Loose leash walking takes the most patience of any skill. Expect weeks of practice.",
        ]),
        ("Chapter 8: Bite Inhibition", [
            "All puppies bite and mouth. It is how they explore and play naturally.",
            "Your goal is to teach them that human skin is fragile and biting must be gentle.",
            "When puppy bites too hard during play, yelp sharply and immediately stop playing.",
            "Turn away and ignore the puppy for ten to fifteen seconds after a hard bite.",
            "Resume play after the brief timeout. They will learn that biting ends fun.",
            "Redirect biting to appropriate chew toys whenever their mouth goes to your skin.",
            "Keep a toy in your pocket to substitute whenever they try to mouth your hands.",
            "If yelping excites them more, simply stand up and walk away calmly.",
            "Frozen washcloths soothe teething gums and provide an appropriate chewing outlet.",
            "Never slap a puppy's nose or hold their mouth shut as this increases biting.",
            "Puppies between three and six months go through intense teething that increases mouthing.",
            "By six months, a properly trained puppy will have a very soft mouth with humans.",
        ]),
        ("Chapter 9: Socialization Guide", [
            "The critical socialization window is between 3 and 16 weeks of age.",
            "During this period, expose your puppy to as many positive experiences as possible.",
            "Introduce them to people of all ages, appearances, and body types.",
            "Let them experience different surfaces: grass, gravel, tile, metal, and carpet.",
            "Expose them to sounds: vacuum cleaners, thunder recordings, traffic, and doorbells.",
            "Introduce other vaccinated, friendly dogs for appropriate play experiences.",
            "Visit pet-friendly stores, outdoor cafes, and parks for new environments.",
            "Car rides, elevators, automatic doors, and stairs should all become normal.",
            "Always pair new experiences with treats and praise. Never force interactions.",
            "If your puppy shows fear, do not comfort excessively. Calmly redirect and try later.",
            "Puppy socialization classes provide controlled environments for learning.",
            "Under-socialized puppies often become fearful or aggressive adult dogs.",
        ]),
        ("Chapter 10: Handling Separation Anxiety", [
            "Separation anxiety causes destructive behavior, barking, and distress when alone.",
            "Prevention starts by teaching your puppy that being alone is safe and normal.",
            "Practice leaving the room for just seconds at first, then return calmly.",
            "Gradually increase the time you are out of sight over days and weeks.",
            "Make departures boring. No long emotional goodbyes or excited hellos.",
            "Give a stuffed Kong or puzzle toy only when leaving so alone time means treats.",
            "Leave the radio or television on for background noise that masks outside sounds.",
            "Exercise your puppy before leaving so they are tired and ready to rest.",
            "If anxiety is severe, never leave them longer than they can handle without panic.",
            "Build up slowly from one minute to five, to fifteen, to thirty, to an hour.",
            "Crate-trained dogs often feel more secure in their crate when you are away.",
            "Consult a veterinary behaviorist if anxiety is extreme despite gradual training.",
        ]),
        ("Chapter 11: Preventing Destructive Chewing", [
            "Chewing is normal and necessary for puppies. Your job is directing it appropriately.",
            "Provide at least three to five appropriate chew toys of different textures.",
            "Rotate chew toys every few days so they seem new and interesting.",
            "Frozen Kongs stuffed with peanut butter and kibble provide long-lasting entertainment.",
            "Bully sticks, antlers, and rubber toys satisfy the natural urge to chew.",
            "When you catch them chewing something forbidden, calmly redirect to a proper toy.",
            "Praise them enthusiastically whenever they choose to chew appropriate items.",
            "Keep tempting items like shoes, remotes, and pillows out of reach.",
            "Bitter apple spray on furniture legs and cords deters most puppies.",
            "Increased chewing often signals boredom. Add more exercise and mental stimulation.",
            "Puppies chew most intensely between three and six months during teething.",
            "Providing adequate chew outlets means they never learn to destroy your belongings.",
        ]),
        ("Chapter 12: Establishing a Routine", [
            "Dogs thrive on predictable schedules. A routine reduces anxiety and accidents.",
            "Wake up at the same time daily: immediately outside for bathroom, then breakfast.",
            "Feed meals at consistent times, usually two to three times daily for puppies.",
            "Schedule play and training sessions at regular intervals throughout the day.",
            "Midday is typically a long nap period for growing puppies. Let them rest.",
            "Afternoon includes another potty break, playtime, and a short training session.",
            "Evening walk provides exercise and mental stimulation before settling down.",
            "Last potty trip happens right before bedtime at a consistent time each night.",
            "Puppies need 18 to 20 hours of sleep per day. Do not over-stimulate them.",
            "Overtired puppies become hyperactive and bitey, similar to overtired toddlers.",
            "Enforce nap times by placing the puppy in their crate with a chew toy.",
            "Within one week of consistent routine, you will see dramatic behavior improvement.",
        ]),
        ("Chapter 13: Common Training Mistakes", [
            "Mistake one: inconsistency. All family members must use the same rules and commands.",
            "Mistake two: training sessions that are too long. Keep them under five minutes.",
            "Mistake three: punishing after the fact. Dogs cannot connect delayed consequences.",
            "Mistake four: repeating commands. Say it once. If they do not respond, help them.",
            "Mistake five: not rewarding enough. Beginners should treat every correct response.",
            "Mistake six: only training in one location. Practice commands everywhere you go.",
            "Mistake seven: expecting too much too fast. Puppies are babies with short attention.",
            "Mistake eight: using their name for punishment. Names should only be positive.",
            "Mistake nine: skipping socialization. This window closes and cannot be reopened.",
            "Mistake ten: comparing your puppy to others. Every dog learns at their own pace.",
            "Mistake eleven: stopping training once basics are learned. Training should be lifelong.",
            "Mistakes are normal. What matters is recognizing them and adjusting your approach.",
        ]),
        ("Chapter 14: When to Get Professional Help", [
            "Seek help if your puppy shows aggression toward people or other dogs.",
            "Growling, snapping, or biting that breaks skin warrants professional assessment.",
            "Extreme fear responses that do not improve with patient gradual exposure.",
            "Severe separation anxiety that causes self-harm or household destruction.",
            "If you feel frustrated, overwhelmed, or are considering rehoming your puppy.",
            "A good trainer uses positive reinforcement methods without pain or fear.",
            "Avoid any trainer who recommends choke chains, prong collars, or alpha rolls.",
            "Look for certifications like CPDT-KA, KPA, or IAABC membership.",
            "Group puppy classes provide both training guidance and valuable socialization.",
            "Private sessions are better for specific behavioral issues needing focused work.",
            "Ask your veterinarian for trainer recommendations they trust.",
            "Professional help early prevents small issues from becoming serious lifelong problems.",
        ]),
        ("Chapter 15: Training Schedule (First 8 Weeks)", [
            "Week 1: Focus on bonding, crate introduction, and establishing your routine.",
            "Take puppy out every 30 minutes when awake. Praise all outdoor eliminations.",
            "Week 2: Begin teaching sit using treat luring. Practice in three short sessions daily.",
            "Continue crate training with meals inside and brief door-closed periods.",
            "Week 3: Add the down command and begin name recognition training.",
            "Start leash familiarization indoors. Let them drag a light leash supervised.",
            "Week 4: Introduce stay for one to three seconds after sit. Begin socialization outings.",
            "Practice gentle handling: touch paws, ears, mouth daily with treats.",
            "Week 5: Begin recall training in the house. Add gentle leash walking indoors.",
            "Increase alone time gradually. Build from seconds to several minutes.",
            "Week 6: Practice all commands in new locations. Extend stay to ten seconds.",
            "Weeks 7-8: Combine commands in sequences. Increase distraction levels slowly.",
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

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book69_How_To_Train_Puppy.pdf')
    print("Book 69 created: Book69_How_To_Train_Puppy.pdf")

if __name__ == '__main__':
    create_book()
