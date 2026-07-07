"""Book 77: AI-Powered Fitness After 50 - Smart Exercise Plans for Every Body"""
from pdf_utils import PDFDoc

doc = PDFDoc(432, 648)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 432, 648, 0.93)
doc.add_centered_text(530, "AI-POWERED FITNESS", 'F2', 20)
doc.add_centered_text(500, "AFTER 50", 'F2', 20)
doc.add_centered_text(458, "Smart Exercise Plans", 'F5', 15)
doc.add_centered_text(436, "for Every Body", 'F5', 15)
doc.add_line(110, 418, 322, 418, 2, 0.3)
doc.add_centered_text(383, "Technology-Guided Fitness", 'F1', 12)
doc.add_centered_text(361, "for Aging Bodies", 'F1', 12)
doc.add_centered_text(200, "Daniel Tesfamariam", 'F2', 14)
doc.add_centered_text(175, "2024", 'F1', 11)

# Copyright page
doc.new_page()
doc.add_centered_text(500, "AI-POWERED FITNESS AFTER 50", 'F2', 14)
doc.add_centered_text(475, "Smart Exercise Plans for Every Body", 'F4', 10)
doc.add_centered_text(440, "Copyright 2024 Daniel Tesfamariam", 'F1', 10)
doc.add_centered_text(420, "All rights reserved.", 'F1', 10)
doc.add_centered_text(390, "No part of this publication may be reproduced without permission.", 'F1', 9)
doc.add_centered_text(360, "Published independently via KDP.", 'F1', 10)
doc.add_centered_text(330, "Consult your physician before beginning any exercise program.", 'F1', 9)

chapters = [
    ("Chapter 1: Why AI Fitness Is Perfect for Older Adults", [
        "Traditional fitness programs assume a healthy 25-year-old body and one-size-fits-all approach.",
        "AI fitness adapts to your specific limitations, injuries, and health conditions.",
        "No human trainer can monitor you 24/7, but AI wearables track every step and heartbeat.",
        "AI removes the intimidation factor of gyms by providing guidance in your own home.",
        "Programs adjust automatically on days when you have less energy or more pain.",
        "AI understands that progress after 50 looks different - slower but equally meaningful.",
        "Safety is prioritized: AI stops you before you overdo it and risk injury.",
        "Your exercise history and health data create a truly personalized fitness journey.",
        "AI is infinitely patient - it never rushes you or compares you to younger people.",
        "The cost of AI fitness apps is a fraction of personal training sessions.",
        "This book shows you how to use AI to stay active, strong, and independent.",
    ]),
    ("Chapter 2: Best AI Fitness Apps for 50+", [
        "SilverSneakers GO is designed specifically for older adults with AI-adapted workouts.",
        "Fitbod uses AI to create strength training programs considering your limitations.",
        "Apple Fitness+ provides guided workouts with modifications for all ability levels.",
        "Peloton app offers low-impact options and tracks progress with AI recommendations.",
        "PEAR Personal Fitness Coach gives real-time audio coaching during exercises.",
        "Freeletics adapts bodyweight workouts to your fitness level using AI algorithms.",
        "Noom for healthy aging combines fitness, nutrition, and behavior change with AI coaching.",
        "Aaptiv provides audio-guided workouts for walking, swimming, and gentle movement.",
        "Most apps offer free trials so you can test which one feels right for you.",
        "Choose based on your preferred exercise type: walking, strength, yoga, or swimming.",
        "Start with one app and master it before trying others.",
    ]),
    ("Chapter 3: Setting Up Your AI Fitness Profile", [
        "Your AI fitness profile is the foundation of your personalized exercise program.",
        "Honestly input your age, weight, height, and current activity level for best results.",
        "List all injuries, joint replacements, and chronic conditions during setup.",
        "Specify medications that affect heart rate or energy levels for accurate monitoring.",
        "Define your goals clearly: mobility, strength, balance, weight loss, or pain reduction.",
        "Set realistic time commitments - even 10 minutes daily counts when you are starting out.",
        "Connect your wearable device (watch or tracker) for automatic data integration.",
        "Allow notifications so AI can remind you at your best times for exercise.",
        "Input your available equipment: none needed, or dumbbells, bands, chair, or pool.",
        "AI uses all this information to create a program that is safe and effective for you.",
        "Update your profile whenever something changes - the AI adjusts immediately.",
    ]),
    ("Chapter 4: AI Walking Programs - Step Tracking", [
        "Walking is the safest, most accessible exercise for adults over 50.",
        "AI step trackers set personalized daily goals based on your current fitness level.",
        "Start wherever you are - even 2000 steps daily is a valid starting point.",
        "AI gradually increases targets by 500-1000 steps per week to build safely.",
        "GPS tracking maps your routes and suggests new paths to keep walks interesting.",
        "AI identifies your natural walking speed and celebrates when it improves.",
        "Interval training AI alternates fast and slow periods for cardiovascular benefit.",
        "Weather-based AI suggests indoor walking alternatives on bad weather days.",
        "Walking buddy features connect you with others at similar pace and distance.",
        "AI correlates your walking data with sleep, mood, and energy for insights.",
        "Celebrate milestones: your first mile, your first week streak, your first 10,000 steps.",
    ]),
    ("Chapter 5: AI Yoga and Flexibility for Stiff Joints", [
        "Yoga and stretching with AI guidance reduce stiffness and improve range of motion.",
        "AI yoga apps offer chair yoga, gentle yoga, and restorative poses for limited mobility.",
        "Camera-based AI checks your form and suggests modifications for safer stretching.",
        "Morning flexibility routines counter overnight stiffness in as little as 5 minutes.",
        "AI knows which stretches help specific problem areas: hips, shoulders, back, and knees.",
        "Breathing cues from AI help you relax deeper into stretches without forcing.",
        "Progress photos taken weekly show improvements you might not feel day-to-day.",
        "AI adjusts difficulty based on how flexible you were in previous sessions.",
        "Yoga blocks, straps, and chair modifications make every pose accessible.",
        "Pain monitoring AI stops the session if it detects you are pushing too hard.",
        "Even 10 minutes of daily stretching dramatically improves quality of life over time.",
    ]),
    ("Chapter 6: AI Strength Training for Bone Health", [
        "Resistance training is essential for preventing osteoporosis and maintaining independence.",
        "AI designs strength programs using body weight, bands, or light dumbbells safely.",
        "Bone-loading exercises recommended by AI specifically target high-fracture-risk areas.",
        "AI ensures proper form to prevent injury - the most important factor in senior strength training.",
        "Programs progress gradually: more repetitions before more weight for safety.",
        "AI tracks which muscles need more work and balances your overall strength development.",
        "Functional exercises (sit-to-stand, carrying, reaching) prepare you for daily activities.",
        "Rest periods are automatically adjusted based on your recovery rate and heart data.",
        "AI prevents overtraining by monitoring workout frequency and recovery indicators.",
        "Strength gains are possible at any age - studies show improvement even in people over 90.",
        "Aim for 2-3 strength sessions per week with AI guiding every rep.",
    ]),
    ("Chapter 7: AI Balance Exercises - Fall Prevention", [
        "Falls are the leading cause of fatal and non-fatal injuries in adults over 65.",
        "AI balance programs reduce fall risk by 40 percent with consistent practice.",
        "Progressive balance challenges start with wall support and advance to free-standing.",
        "AI monitors your stability through wearable sensors and adjusts difficulty appropriately.",
        "Exercises target the three balance systems: vision, vestibular, and proprioception.",
        "Tandem walking, single-leg stands, and weight shifts improve stability systematically.",
        "AI identifies which direction you are weakest and targets exercises to correct imbalances.",
        "Reaction time training helps you catch yourself faster if you do start to fall.",
        "Environmental awareness exercises teach you to navigate obstacles confidently.",
        "Balance confidence improves as much as physical balance - both matter for fall prevention.",
        "Practice balance exercises daily, even if just for 5 minutes, for maximum benefit.",
    ]),
    ("Chapter 8: AI Swimming and Water Exercise Plans", [
        "Water exercise provides resistance without impact - ideal for arthritis and joint issues.",
        "AI swimming apps track laps, pace, and form even in the water with waterproof trackers.",
        "Water walking programs provide cardiovascular exercise with zero joint stress.",
        "AI adjusts pool exercise intensity based on water temperature and your energy level.",
        "Aqua aerobics classes guided by AI provide variety and social interaction.",
        "Buoyancy reduces effective body weight by 90 percent, allowing pain-free movement.",
        "AI tracks your pool sessions and ensures adequate frequency for health benefits.",
        "Water resistance naturally provides progressive overload as you move faster.",
        "Swimming technique AI identifies stroke improvements for efficiency and injury prevention.",
        "Many Medicare Advantage plans cover gym memberships with pool access through SilverSneakers.",
        "Even non-swimmers benefit from water walking and shallow-end exercises.",
    ]),
    ("Chapter 9: Heart Rate Zone Training with AI", [
        "Heart rate zone training ensures you exercise at the right intensity for your age and fitness.",
        "AI calculates your personal heart rate zones based on age, fitness, and medications.",
        "Zone 1 (easy) and Zone 2 (moderate) are where most seniors should exercise.",
        "Beta blockers and other medications affect heart rate - AI accounts for this.",
        "AI alerts you immediately if your heart rate goes too high during exercise.",
        "Training in the right zone maximizes cardiovascular benefit while minimizing risk.",
        "AI wearables display real-time zone information so you can adjust pace instantly.",
        "Over time, AI shows your cardiovascular fitness improving as zones shift upward.",
        "Recovery heart rate (how fast it drops after exercise) is an important fitness indicator.",
        "Talk test: if you cannot hold a conversation, AI confirms you should slow down.",
        "Heart rate zone training is the safest way to ensure exercise is helpful not harmful.",
    ]),
    ("Chapter 10: AI Recovery and Rest Day Planning", [
        "Recovery is when your body actually gets stronger - not during the exercise itself.",
        "AI analyzes sleep, heart rate variability, and activity to determine your recovery status.",
        "Rest days are programmed automatically based on your body's actual recovery data.",
        "Active recovery (gentle walking, stretching) is suggested on days between hard workouts.",
        "AI prevents the common mistake of doing too much too soon that leads to injury.",
        "Sleep quality directly affects exercise recovery - AI correlates both data streams.",
        "Hydration and nutrition reminders support recovery between exercise sessions.",
        "AI detects overtraining symptoms: persistent fatigue, elevated resting heart rate, and poor sleep.",
        "Strategic rest makes your exercise days more productive and enjoyable.",
        "Foam rolling and self-massage guidance from AI aids muscle recovery between sessions.",
        "Listen to your body and trust the AI when it says today is a rest day.",
    ]),
    ("Chapter 11: AI Nutrition for Active Aging", [
        "Exercise and nutrition work together - one without the other limits your results.",
        "AI nutrition apps calculate your needs based on activity level and fitness goals.",
        "Protein requirements increase with age and exercise: AI ensures you get enough.",
        "Pre-exercise nutrition timing optimizes your energy for better workout performance.",
        "Post-exercise nutrition within 30 minutes maximizes recovery and muscle building.",
        "AI tracks calcium and vitamin D intake crucial for bone health during strength training.",
        "Hydration calculations based on exercise intensity prevent dehydration risks.",
        "Anti-inflammatory food suggestions reduce exercise-related soreness and stiffness.",
        "AI meal plans integrate with your exercise schedule for optimal timing and nutrition.",
        "Calorie tracking ensures you fuel your activity without under or overeating.",
        "Simple swaps suggested by AI gradually improve your diet without dramatic changes.",
    ]),
    ("Chapter 12: AI Posture Correction Tools", [
        "Poor posture contributes to pain, breathing problems, and balance issues in older adults.",
        "AI posture apps use your phone camera to analyze your standing and sitting alignment.",
        "Wearable posture devices vibrate gently when you slouch, training better habits.",
        "AI identifies specific muscles that are weak or tight contributing to poor posture.",
        "Targeted exercises strengthen postural muscles for lasting improvement.",
        "Desk and sitting posture analysis helps those who spend time reading or at computers.",
        "Walking posture coaching improves gait efficiency and reduces fall risk.",
        "AI tracks postural improvements over weeks and months with photographic evidence.",
        "Better posture immediately improves breathing capacity and energy levels.",
        "Spinal mobility exercises suggested by AI prevent the forward head posture common in aging.",
        "Even small posture improvements reduce back pain and increase confidence in movement.",
    ]),
    ("Chapter 13: AI Personal Trainer Chatbots", [
        "AI trainer chatbots provide unlimited personal training guidance at zero cost.",
        "Ask any exercise question and receive an answer tailored to your age and limitations.",
        "AI trainers create custom workout plans based on your available time and equipment.",
        "They modify exercises instantly when you report pain or difficulty.",
        "Motivation messages are personalized based on your goals and progress history.",
        "AI chatbots remember all your previous conversations and exercise history.",
        "They can demonstrate exercises through video links and written descriptions.",
        "Form check guidance helps you exercise safely without an in-person trainer present.",
        "Available 24/7 - ask questions at any time without scheduling appointments.",
        "Many people feel more comfortable asking AI about limitations than admitting them to humans.",
        "Use AI chatbots as a supplement to occasional check-ins with a real exercise professional.",
    ]),
    ("Chapter 14: Wearable Tech Fitness Guide", [
        "Choosing the right wearable depends on your primary fitness goals and comfort preferences.",
        "Apple Watch offers comprehensive health and fitness tracking with excellent senior features.",
        "Fitbit provides simple, affordable tracking with a long battery life.",
        "Garmin excels at GPS tracking for walkers, hikers, and outdoor exercisers.",
        "Oura Ring offers sleep and recovery tracking in a comfortable, discreet form factor.",
        "WHOOP strap focuses on recovery and strain metrics for data-driven exercisers.",
        "Key features to prioritize: heart rate accuracy, fall detection, and ease of use.",
        "Battery life matters - choose a device you will not forget to charge frequently.",
        "Water resistance is important if you swim or prefer not removing it for showers.",
        "Start with basic features and explore advanced ones as you become comfortable.",
        "Any wearable is better than none - do not let perfect be the enemy of good.",
    ]),
    ("Chapter 15: AI Group Fitness Virtual Classes", [
        "Virtual group fitness combines the motivation of a class with the convenience of home.",
        "AI matches you with classes at your fitness level so you never feel out of place.",
        "Live classes provide real-time energy from other participants and instructors.",
        "On-demand classes let you exercise whenever your schedule and energy allow.",
        "Senior-specific virtual classes focus on appropriate intensity and modifications.",
        "Social features let you see friends who are also in the class for motivation.",
        "AI tracks your performance relative to the class and your own personal history.",
        "Low-impact dance, chair fitness, and gentle strength classes are widely available.",
        "Instructors trained in senior fitness understand limitations and provide alternatives.",
        "The accountability of a scheduled class helps maintain consistency in your routine.",
        "Try several instructors and styles until you find what makes exercise feel enjoyable.",
    ]),
    ("Chapter 16: AI Progress Tracking and Motivation", [
        "Seeing your progress is the most powerful motivation for continuing exercise.",
        "AI tracks dozens of metrics and highlights improvements you might not notice yourself.",
        "Weekly reports celebrate achievements: more steps, better sleep, improved recovery.",
        "Before and after comparisons show physical changes over months of consistent effort.",
        "Streak tracking motivates daily activity even when you do not feel like exercising.",
        "AI milestone celebrations (first 100 workouts, walking distance achievements) provide rewards.",
        "Comparison with your past self (not others) keeps motivation healthy and personal.",
        "AI predicts future progress based on current trends, giving you goals to look forward to.",
        "Social sharing options let you celebrate with family and friends who support you.",
        "Bad days and setbacks are normalized by AI - every journey has ups and downs.",
        "The data proves what you already feel: you are getting stronger, healthier, and more capable.",
    ]),
    ("Chapter 17: AI Injury Prevention", [
        "Injury prevention is more important than performance when you are over 50.",
        "AI monitors movement patterns that indicate compensation and potential injury risk.",
        "Warm-up routines generated by AI prepare specific muscles for the planned workout.",
        "Cool-down protocols prevent stiffness and promote recovery after each session.",
        "AI identifies when you are doing too much volume, intensity, or frequency.",
        "Joint-friendly exercise alternatives are suggested when impact is too high.",
        "Symmetry monitoring detects when one side is weaker, creating injury risk.",
        "Pain logging in AI apps tracks which exercises cause discomfort for future avoidance.",
        "Environmental factors (temperature, humidity, surface) are considered by smart AI programs.",
        "Recovery metrics tell you when your body is ready for the next challenge.",
        "An injury prevented is worth months of forced rest - let AI keep you safe.",
    ]),
    ("Chapter 18: Adapting Workouts with AI for Limitations", [
        "Every physical limitation has a workaround - AI helps you find it.",
        "Knee replacement: AI provides low-impact alternatives that avoid harmful movements.",
        "Hip replacement: exercises are modified to respect range-of-motion restrictions.",
        "Back pain: AI strengthens core muscles while avoiding positions that worsen pain.",
        "Shoulder injuries: upper body exercises are adapted to pain-free ranges.",
        "Arthritis: AI schedules exercise when joints are warmest and least stiff.",
        "Heart conditions: intensity is carefully controlled with continuous monitoring.",
        "Diabetes: exercise timing is coordinated with meals and medication for blood sugar safety.",
        "COPD: breathing-focused exercise and controlled intensity prevent respiratory distress.",
        "Balance disorders: exercises are adapted with support options for safety.",
        "No matter your limitation, there is always something you can do to stay active.",
    ]),
    ("Chapter 19: 12-Week AI Fitness Starter Plan", [
        "Weeks 1-2: Walk 10-15 minutes daily with step tracker. Focus on building the habit.",
        "Weeks 3-4: Add 5 minutes of gentle stretching after each walk. Try a flexibility app.",
        "Weeks 5-6: Introduce 2 strength sessions per week (bodyweight or light bands, 10 min each).",
        "Weeks 7-8: Increase walks to 20-25 minutes. Add balance exercises 3 times per week.",
        "Weeks 9-10: Try a virtual group fitness class once per week. Explore different formats.",
        "Weeks 11-12: Build your full routine: walk daily, strength 2-3x, flexibility daily, balance 3x.",
        "Listen to AI recovery recommendations - rest when your body says rest.",
        "Track your improvements weekly: steps, strength, flexibility, and energy levels.",
        "Adjust the timeline if needed - going slower is always better than getting injured.",
        "By week 12, you will have a sustainable routine that AI continues to adapt and improve.",
        "Celebrate completing 12 weeks - you have built a foundation for years of active aging.",
    ]),
    ("Chapter 20: Staying Motivated with AI Coaching", [
        "Long-term consistency matters more than short-term intensity in fitness after 50.",
        "AI coaching adapts to your motivation style: some people need encouragement, others data.",
        "Set seasonal goals: different activities for different weather and energy levels.",
        "AI connects your fitness to meaningful life goals: playing with grandchildren, traveling, independence.",
        "Variety prevents boredom - AI suggests new exercises, routes, and classes regularly.",
        "Progress plateaus are normal - AI helps you adjust without becoming discouraged.",
        "Community features connect you with others at similar stages for mutual encouragement.",
        "Reward yourself for milestones - AI can suggest appropriate celebration activities.",
        "Fitness is a gift to your future self - every workout deposits in your health bank.",
        "AI coaching never gives up on you, no matter how many times you start over.",
        "You are worth the effort. Keep moving, keep growing, keep celebrating your strength.",
    ]),
]

for title, lines in chapters:
    doc.new_page()
    doc.add_text(36, 608, title, 'F2', 12)
    doc.add_line(36, 600, 396, 600, 1, 0.4)
    y = 575
    for line in lines:
        doc.add_text(36, y, line, 'F4', 9.8)
        y -= 21

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book77_AI_Fitness_Over50.pdf")
print("Created Book77_AI_Fitness_Over50.pdf")
