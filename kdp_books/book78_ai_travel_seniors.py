"""Book 78: AI Travel Guide for Seniors - Plan Easier, Safer, Better Trips"""
from pdf_utils import PDFDoc

doc = PDFDoc(432, 648)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 432, 648, 0.94)
doc.add_centered_text(530, "AI TRAVEL GUIDE", 'F2', 21)
doc.add_centered_text(500, "FOR SENIORS", 'F2', 21)
doc.add_centered_text(458, "Plan Easier, Safer,", 'F5', 15)
doc.add_centered_text(436, "Better Trips", 'F5', 15)
doc.add_line(110, 418, 322, 418, 2, 0.3)
doc.add_centered_text(383, "Smart Technology for", 'F1', 12)
doc.add_centered_text(361, "Confident Travelers", 'F1', 12)
doc.add_centered_text(200, "Daniel Tesfamariam", 'F2', 14)
doc.add_centered_text(175, "2024", 'F1', 11)

# Copyright page
doc.new_page()
doc.add_centered_text(500, "AI TRAVEL GUIDE FOR SENIORS", 'F2', 14)
doc.add_centered_text(475, "Plan Easier, Safer, Better Trips", 'F4', 10)
doc.add_centered_text(440, "Copyright 2024 Daniel Tesfamariam", 'F1', 10)
doc.add_centered_text(420, "All rights reserved.", 'F1', 10)
doc.add_centered_text(390, "No part of this publication may be reproduced without permission.", 'F1', 9)
doc.add_centered_text(360, "Published independently via KDP.", 'F1', 10)

chapters = [
    ("Chapter 1: How AI Is Changing Travel for Seniors", [
        "Travel after retirement should be the adventure of a lifetime, not a source of anxiety.",
        "AI removes the most stressful parts of travel: planning, language, and unexpected problems.",
        "Smart apps now handle everything from booking to navigation to emergency assistance.",
        "AI considers your specific needs: mobility, health, dietary restrictions, and pace preferences.",
        "Trip planning that once took weeks of research now takes minutes with AI assistance.",
        "Real-time AI translation eliminates the language barrier in any country on Earth.",
        "AI-powered travel has made solo travel safer and more accessible for older adults.",
        "Health monitoring continues seamlessly when you travel with wearable AI devices.",
        "Budget optimization AI finds better deals than even experienced travel agents.",
        "This book covers every AI tool you need for confident, enjoyable travel at any age.",
        "The world is waiting for you - AI just makes getting there easier.",
    ]),
    ("Chapter 2: AI Trip Planners That Consider Mobility", [
        "AI trip planners like TripIt, Google Travel, and Wonderplan consider your physical needs.",
        "Input your walking tolerance and the AI plans itineraries with appropriate pacing.",
        "Rest stop scheduling ensures you never push too far without a chance to sit.",
        "Elevator and escalator locations are flagged for destinations with many stairs.",
        "AI identifies wheelchair-accessible routes, attractions, and transportation options.",
        "Hotel rooms are filtered by floor level, bathroom accessibility, and bed height.",
        "Activity timing considers your energy patterns - demanding sites in the morning, rest after lunch.",
        "AI builds buffer time between activities so you are never rushed or stressed.",
        "Terrain difficulty ratings help you decide which excursions suit your ability level.",
        "Alternative activities are suggested for days when energy is lower than expected.",
        "These planners learn your preferences with each trip and improve recommendations over time.",
    ]),
    ("Chapter 3: Accessibility-Focused AI Booking", [
        "AI booking platforms filter specifically for accessibility needs you specify once.",
        "Wheelchair accessible rooms with roll-in showers are identified automatically.",
        "Flight booking AI selects seats with extra legroom and easy aisle access.",
        "Airport assistance (wheelchair, guide) is requested automatically during booking.",
        "Cruise cabin selection considers proximity to elevators and medical facilities.",
        "Restaurant booking AI identifies establishments with step-free entry and accessible restrooms.",
        "AI reviews for accessibility are sourced from other travelers with similar needs.",
        "Transfer services with vehicle accessibility are arranged in advance at each destination.",
        "Attraction booking confirms accessibility accommodations before you arrive.",
        "AI stores your needs profile so you enter requirements once and they apply everywhere.",
        "Accessible travel is not limited travel - AI helps you do everything others do.",
    ]),
    ("Chapter 4: AI Language Translation on the Go", [
        "AI translation apps eliminate the biggest barrier to international travel for seniors.",
        "Google Translate offers real-time conversation translation in over 130 languages.",
        "Camera translation reads signs, menus, and labels by pointing your phone at them.",
        "Offline translation works without internet - essential in areas with poor connectivity.",
        "AI earbuds like Google Pixel Buds translate spoken language in real time.",
        "Restaurant menus are translated with explanations of unfamiliar dishes and ingredients.",
        "Medical vocabulary translation ensures you can communicate health needs in emergencies.",
        "AI pronunciation guides help you attempt common phrases that locals appreciate.",
        "Currency and measurement conversions happen automatically within translation apps.",
        "Cultural context is included so you understand not just words but appropriate behavior.",
        "With AI translation, every country becomes accessible regardless of language skills.",
    ]),
    ("Chapter 5: AI Health Preparation for Travel", [
        "AI helps you prepare medically for travel so health concerns do not become emergencies.",
        "Medication management AI creates travel-adjusted schedules for time zone changes.",
        "AI identifies required and recommended vaccinations for your destination months ahead.",
        "Health card generation AI creates cards listing conditions, medications, and allergies.",
        "AI translates your medical information into the language of your destination country.",
        "Travel insurance comparison AI finds policies that cover your pre-existing conditions.",
        "AI identifies hospitals, clinics, and pharmacies near every stop on your itinerary.",
        "Altitude, climate, and air quality AI assessments flag destinations that might cause problems.",
        "Packing lists for medical supplies are generated based on trip length and destination.",
        "AI connects you with telehealth services in your destination's timezone if needed.",
        "Preparation reduces risk and anxiety - AI makes thorough preparation effortless.",
    ]),
    ("Chapter 6: AI Packing Assistants", [
        "AI packing apps create customized lists based on your destination, duration, and activities.",
        "Weather forecast integration suggests exactly what clothing to bring for each day.",
        "AI reminds you of frequently forgotten items specific to your needs (medications, chargers).",
        "Weight and size optimization helps you pack light while having everything you need.",
        "AI suggests versatile clothing that works across multiple activities and weather conditions.",
        "Medication checklists ensure you pack sufficient supplies plus emergency extras.",
        "Technology packing lists include adapters, chargers, and devices for your destination.",
        "AI creates a re-pack checklist for return travel so nothing gets left in hotel rooms.",
        "Carry-on versus checked bag decisions are optimized for airline rules and your mobility.",
        "AI learns from past trips what you actually used and adjusts future recommendations.",
        "A well-packed bag reduces physical strain and stress throughout your entire trip.",
    ]),
    ("Chapter 7: AI Navigation for Unfamiliar Cities", [
        "Getting lost in a new city is stressful, but AI navigation makes it nearly impossible.",
        "Google Maps and Apple Maps provide turn-by-turn walking directions with voice guidance.",
        "AI selects pedestrian-friendly routes that avoid steep hills, stairs, and construction.",
        "Public transportation AI explains how to use buses, trains, and metros in any city.",
        "Offline maps work without internet so you are never stranded without directions.",
        "AI estimates walking time based on your personal pace, not average adult speed.",
        "Indoor navigation AI guides you through airports, malls, and large buildings.",
        "AI identifies safe, well-lit routes for evening walks in unfamiliar areas.",
        "Ride-sharing apps (Uber/Lyft) with AI navigation bring a car to your exact location.",
        "AI alerts you when you are heading the wrong direction before you walk too far.",
        "Confidence in navigation transforms how much you enjoy exploring new places.",
    ]),
    ("Chapter 8: AI Restaurant Finders for Dietary Needs", [
        "Finding safe restaurants with dietary restrictions is no longer a travel challenge.",
        "AI filters restaurants by specific dietary needs: gluten-free, low-sodium, diabetic-friendly.",
        "Allergy information AI identifies dishes safe for your specific food allergies.",
        "AI translates menu items and explains ingredients in dishes from other cuisines.",
        "Reviews from other travelers with similar dietary needs help you choose confidently.",
        "AI suggests what to order at each restaurant based on your health requirements.",
        "Proximity-based search finds suitable restaurants near your current location instantly.",
        "Reservation AI books tables and communicates your dietary needs to the restaurant.",
        "Meal timing suggestions align with medication schedules and blood sugar management.",
        "AI identifies grocery stores and markets for preparing simple meals in rental accommodations.",
        "Good food is essential to enjoying travel - AI ensures you never compromise on safety.",
    ]),
    ("Chapter 9: AI Emergency Assistance Abroad", [
        "AI emergency tools provide critical support when problems occur far from home.",
        "Emergency translation AI communicates your medical needs in any language instantly.",
        "SOS features on smartphones contact local emergency services with one button press.",
        "AI identifies the nearest hospital with relevant specialty care for your condition.",
        "Embassy and consulate location AI provides contact information for your country's offices.",
        "Medical alert devices work internationally with global cellular connectivity.",
        "AI travel insurance apps file claims instantly with photos and translated documentation.",
        "Emergency contact notification AI alerts your family immediately if something happens.",
        "AI stores critical documents (passport, insurance, prescriptions) securely in the cloud.",
        "Lost item tracking AI helps recover bags, wallets, and devices when misplaced.",
        "Preparation for emergencies means they are less likely and less stressful if they occur.",
    ]),
    ("Chapter 10: AI Travel Insurance Comparison", [
        "Travel insurance is essential for seniors and AI helps find the best coverage.",
        "AI compares dozens of policies simultaneously, filtering for your specific needs.",
        "Pre-existing condition coverage is identified and compared across all providers.",
        "Trip cancellation protection is evaluated based on common senior-specific scenarios.",
        "Medical evacuation coverage levels are compared for your destination's distance and risk.",
        "AI reads the fine print and flags exclusions you might miss in complex policies.",
        "Cancel-for-any-reason options are highlighted for maximum flexibility.",
        "Price comparisons show the same coverage at different price points across providers.",
        "AI recommends coverage levels based on your trip value, destination, and health status.",
        "Filing claims is simplified with AI that guides you through documentation requirements.",
        "Adequate insurance transforms anxiety into confidence for every trip you take.",
    ]),
    ("Chapter 11: AI Photo and Journal Tools", [
        "AI travel photography tools help you capture and preserve trip memories beautifully.",
        "Camera AI automatically adjusts settings for perfect photos in any lighting condition.",
        "AI removes unwanted tourists from your scenic photos after you take them.",
        "Night mode AI creates clear photos in low light without flash disturbing others.",
        "AI photo organization sorts your trip images by location, date, and who is in them.",
        "Voice journaling AI transcribes your daily observations into a written travel diary.",
        "AI creates daily highlight reels of your best photos set to music automatically.",
        "Photo book creation AI designs professional albums you can order upon returning home.",
        "AI enhances photos taken in challenging conditions: fog, rain, or harsh sunlight.",
        "GPS tagging on photos creates a map of exactly where each memory was made.",
        "These memories become more precious with time - AI ensures they are captured beautifully.",
    ]),
    ("Chapter 12: AI Group Trip Coordination", [
        "Traveling with friends, family, or groups requires coordination that AI handles expertly.",
        "Shared itinerary apps keep everyone on the same page with real-time updates.",
        "AI expense splitting calculates who owes what without awkward money conversations.",
        "Group vote features let everyone weigh in on restaurants, activities, and destinations.",
        "AI schedules free time and group activities to balance together time with independence.",
        "Accommodation AI finds properties that suit the entire group's needs and preferences.",
        "Communication channels keep the group connected without overwhelming message volume.",
        "AI coordinates different mobility levels so no one is left behind or forced to hurry.",
        "Group photo AI ensures everyone is included in pictures throughout the trip.",
        "Emergency information for all group members is accessible to trip organizers.",
        "Group travel creates the best memories - AI handles the logistics that usually cause friction.",
    ]),
    ("Chapter 13: Budget-Friendly AI Travel Hacks", [
        "AI finds travel deals that save hundreds or thousands of dollars per trip.",
        "Price prediction AI tells you the best time to book flights for lowest fares.",
        "Hotel comparison AI searches dozens of sites simultaneously for the best rates.",
        "Senior discount aggregation AI finds deals specifically for travelers over 55.",
        "Off-peak travel AI identifies when popular destinations are cheaper and less crowded.",
        "AI loyalty program optimization ensures you earn and redeem points effectively.",
        "Currency exchange AI finds the best rates and advises when to convert money.",
        "Free activity AI identifies museums, parks, and attractions with no admission cost.",
        "Meal deal AI finds happy hours, senior specials, and affordable local restaurants.",
        "Package deal comparison shows when bundled flights and hotels save money.",
        "Smart budgeting does not mean sacrificing experience - AI helps you get more for less.",
    ]),
    ("Chapter 14: Top AI Travel Apps Reviewed", [
        "Google Maps: The most comprehensive navigation with transit and walking directions.",
        "TripIt: Automatically organizes all booking confirmations into one clean itinerary.",
        "Google Translate: Real-time translation of text, speech, and images in 130+ languages.",
        "Hopper: AI price prediction for flights tells you when to buy for best savings.",
        "PackPoint: AI-powered packing list generator based on weather and planned activities.",
        "XE Currency: Real-time currency conversion with offline functionality.",
        "Sitata: AI travel health advisor covering vaccinations, alerts, and medical facilities.",
        "GeoSure: AI safety ratings for neighborhoods in cities worldwide.",
        "Flighty: Real-time flight tracking with delay predictions and gate change alerts.",
        "Trail Wallet: AI budget tracking designed specifically for travelers.",
        "Download these before your trip and take time to learn each one at home first.",
    ]),
    ("Chapter 15: Your Pre-Trip AI Checklist", [
        "8 weeks before: Research destination with AI, check visa and vaccination requirements.",
        "6 weeks before: Book flights and accommodation using AI comparison tools.",
        "4 weeks before: Purchase travel insurance with AI-recommended coverage levels.",
        "3 weeks before: Schedule health check-up and get required vaccinations.",
        "2 weeks before: Create AI packing list and begin gathering items.",
        "1 week before: Download all AI travel apps, save offline maps, charge devices.",
        "3 days before: Confirm all bookings, share itinerary with family, pack medications.",
        "1 day before: Final packing check with AI list, charge all electronics fully.",
        "Travel day: Activate AI navigation, enable emergency features, enjoy the journey.",
        "During trip: Use AI daily for translation, navigation, health monitoring, and photo capture.",
        "After trip: Let AI organize photos, create a journal, and start planning the next adventure.",
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

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book78_AI_Travel_Seniors.pdf")
print("Created Book78_AI_Travel_Seniors.pdf")
