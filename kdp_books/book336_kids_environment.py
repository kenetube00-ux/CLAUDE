from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    categories = {
        "Reduce Waste": [
            ("Use a Reusable Water Bottle","Plastic bottles take 450 years to decompose. Using a reusable bottle saves ~167 plastic bottles per person per year!","Fill a reusable bottle each morning instead of buying plastic ones.","Saves 167 bottles/year from landfills per person"),
            ("Bring Reusable Bags Shopping","8 million tons of plastic end up in oceans yearly. Plastic bags are a major contributor. One reusable bag replaces 700 plastic bags in its lifetime!","Keep reusable bags in the car or by the door.","Prevents hundreds of bags from entering oceans"),
            ("Start Composting","Food waste in landfills creates methane (a greenhouse gas 80x worse than CO2). Composting turns food scraps into rich soil instead.","Set up a small compost bin for fruit/veggie scraps.","Reduces methane emissions and creates free fertilizer"),
            ("Refuse Single-Use Straws","500 million straws are used daily in the US alone. They can't be recycled and harm sea turtles and marine life.","Say 'no straw please' or carry a reusable one.","Protects marine life from plastic ingestion"),
            ("Fix Things Instead of Replacing","We throw away 50 million tons of electronics yearly. Many items can be repaired instead of discarded. This saves resources and money!","Before throwing something away, try to repair it or find a new use.","Reduces electronic waste and saves resources"),
            ("Use Both Sides of Paper","Paper production destroys forests and uses massive amounts of water and energy. Using both sides cuts paper consumption in half.","Always use both sides of paper. Use scrap paper for notes.","Saves trees and reduces deforestation"),
            ("Pack Waste-Free Lunches","School lunches create enormous amounts of daily trash from wrappers, bags, and disposable containers.","Use reusable containers, cloth napkins, and real utensils.","Eliminates hundreds of pieces of trash per year"),
            ("Donate Instead of Trash","Many items we throw away are still perfectly useful to someone else. Donating extends the life of products.","Before throwing anything away, ask: could someone else use this?","Keeps usable items out of landfills"),
            ("Buy Less Stuff","Manufacturing new products requires energy, water, and raw materials. The best waste is waste never created in the first place.","Before buying, ask: Do I really NEED this? Will I use it long-term?","Reduces manufacturing demand and resource extraction"),
            ("Learn to Recycle Properly","Contaminated recycling (wrong items in bins) means entire loads go to landfill. Knowing what CAN be recycled matters!","Learn your local recycling rules. Clean containers before recycling.","Ensures recyclables actually get recycled"),
        ],
        "Save Energy": [
            ("Turn Off Lights","Lighting accounts for 15% of household electricity. Leaving lights on in empty rooms wastes energy produced by burning fossil fuels.","Make it a habit: leave a room, flip the switch.","Saves electricity and reduces carbon emissions"),
            ("Unplug Chargers","Chargers plugged in with nothing attached still draw 'phantom' energy. This wastes billions of kilowatt-hours yearly worldwide.","Unplug chargers, TVs, and devices when not in use.","Eliminates phantom energy waste"),
            ("Use Natural Light","Opening curtains instead of flipping switches saves electricity AND boosts your mood (sunlight increases serotonin!).","Open blinds and curtains during daytime. Work near windows.","Saves electricity and improves mental health"),
            ("Take Shorter Showers","Heating water is energy-intensive. A 5-minute shower uses 10 gallons; a 10-minute shower uses 20. Cutting back helps!","Time your showers - aim for 5 minutes or less.","Saves water AND the energy used to heat it"),
            ("Wash Clothes in Cold Water","90% of washing machine energy goes to heating water. Cold water cleans just as well for most loads.","Ask parents to switch to cold water washes.","Reduces energy use by up to 90% per load"),
            ("Air Dry Instead of Machine Dry","Dryers use massive energy. Line-drying or rack-drying uses zero energy and makes clothes last longer.","Hang clothes to dry when weather allows.","Saves significant electricity per load"),
            ("Close the Fridge Quickly","Every second the fridge is open, cold air escapes and the motor must work harder. Decide what you want BEFORE opening.","Know what you want before opening the fridge door.","Reduces energy waste from refrigeration"),
            ("Use LED Bulbs","LED bulbs use 75% less energy than incandescent and last 25x longer. One LED saves $80 in electricity over its lifetime.","Help parents switch all bulbs to LED.","Dramatic electricity savings with better light"),
            ("Walk or Bike Short Distances","Cars produce the most CO2 per person per mile for short trips. Walking or biking produces zero emissions and keeps you healthy.","For trips under 1 mile, walk or bike instead of driving.","Zero emissions plus free exercise"),
            ("Plant a Tree","One tree absorbs about 48 pounds of CO2 per year and produces enough oxygen for 2 people. Trees also cool surrounding areas.","Plant a tree in your yard or participate in a tree-planting event.","Absorbs CO2, produces oxygen, provides shade"),
        ],
        "Protect Water": [
            ("Turn Off Tap While Brushing","Leaving the tap running while brushing wastes 4 gallons per session. That's 2,920 gallons per person per year!","Wet brush, turn off water, brush, turn on to rinse.","Saves nearly 3,000 gallons per person per year"),
            ("Fix Dripping Faucets","One dripping faucet wastes over 3,000 gallons per year! That's enough water for 180 showers.","Tell parents about any dripping faucets in your home.","Prevents thousands of gallons of waste"),
            ("Use a Rain Barrel","Collecting rainwater for gardens reduces demand on treated water supplies. One rain barrel can save 1,300 gallons per year.","Help set up a rain barrel to collect water for the garden.","Saves treated water for actual drinking/bathing needs"),
            ("Don't Pour Chemicals Down Drains","Paints, oils, and cleaners pollute waterways. Storm drains go directly to rivers and oceans without treatment.","Dispose of chemicals properly at designated facilities.","Prevents water pollution in rivers and oceans"),
            ("Take Navy Showers","Navy showers: wet down, turn off water, soap up, turn on to rinse. Uses 3 gallons vs 20 for a regular shower.","Try the Navy shower method a few times per week.","Saves up to 85% of shower water"),
            ("Water Gardens in Early Morning","Watering midday means much water evaporates before reaching roots. Early morning watering is 25% more efficient.","Water plants before 10 AM or after 6 PM.","Reduces water waste from evaporation"),
            ("Use a Dishwasher (Full Loads)","Full dishwashers actually use LESS water than hand-washing. But only run when completely full for maximum efficiency.","Wait until dishwasher is full before running it.","Uses less water than hand-washing when full"),
            ("Report Water Pollution","If you see pollution in local water, report it! Oil, trash, and chemicals in streams harm entire ecosystems.","Learn who to call about water pollution in your area.","Protects local waterways and wildlife"),
            ("Learn Where Your Water Comes From","Understanding your water source creates connection and responsibility. Is it a river, lake, aquifer, or reservoir?","Research: where does YOUR tap water come from?","Knowledge creates appreciation and motivation to conserve"),
            ("Reduce Meat Consumption","Producing 1 pound of beef requires 1,800 gallons of water! Even one meat-free day per week makes a huge difference.","Try 'Meatless Monday' - one day per week without meat.","Saves thousands of gallons of water per year"),
        ],
        "Help Animals": [
            ("Build a Bird Feeder","Habitat loss means birds struggle to find food, especially in winter. A simple feeder can support dozens of birds.","Make a bird feeder from a pine cone, peanut butter, and seeds.","Provides vital nutrition for local bird populations"),
            ("Don't Use Pesticides","Pesticides kill 'pest' insects but also kill bees, butterflies, and beneficial insects that pollinate our food crops.","Encourage chemical-free gardening. Use natural pest control.","Protects pollinators that grow 75% of our food"),
            ("Keep Cats Indoors","Outdoor cats kill an estimated 2.4 BILLION birds per year in the US alone. Indoor cats live longer and safer lives too.","If you have a cat, keep it indoors or build a 'catio.'","Protects billions of birds and small wildlife"),
            ("Reduce Balloon Releases","Released balloons travel hundreds of miles then fall as litter. Marine animals mistake them for food and die.","Never release balloons outdoors. Use bubbles instead!","Prevents wildlife from ingesting deadly balloon litter"),
            ("Create Wildlife Habitat","Simple things like brush piles, native plants, and water sources create homes for insects, birds, and small mammals.","Create a small wildlife-friendly area in your yard.","Provides shelter and food for local wildlife"),
            ("Participate in Citizen Science","Apps like iNaturalist let you document wildlife sightings. Scientists use this data to track species and identify problems.","Download a nature ID app and document wildlife you see.","Contributes real scientific data for conservation"),
            ("Don't Buy Wild Animals as Pets","The exotic pet trade captures millions of animals from the wild. Many die during transport. Adopt, don't shop!","Choose domestic pets. Never buy wild-caught animals.","Reduces demand for wildlife trafficking"),
            ("Cut Plastic Rings","Six-pack rings and other plastic loops strangle birds, turtles, and marine mammals. Always cut them before disposing.","Cut ALL loops in plastic packaging before throwing away.","Prevents entanglement injuries and deaths"),
            ("Support Local Wildlife Rescues","Wildlife rehabilitation centers care for injured animals and release them back to nature. They need volunteers and donations.","Visit or volunteer at a local wildlife rescue center.","Helps injured animals recover and return to the wild"),
            ("Learn About Endangered Species","There are over 40,000 species threatened with extinction. Knowledge creates empathy and action.","Research 5 endangered species. What threatens them? How can you help?","Awareness leads to action and conservation support"),
        ],
        "Spread Awareness": [
            ("Start an Eco-Club at School","Organized groups have more impact than individuals. A school eco-club can implement changes across the whole school.","Gather friends and start an environmental club at school.","Multiplies impact through group action"),
            ("Make Educational Posters","Visual reminders help everyone remember to be eco-friendly. Place posters near light switches, trash cans, and faucets.","Create and display environmental reminder posters at school/home.","Constant visual reminders change daily habits"),
            ("Write to Local Leaders","Politicians respond to constituent concerns. A thoughtful letter from a kid can be especially powerful and moving.","Write a letter to your mayor about an environmental issue.","Influences policy decisions at the local level"),
            ("Share on Social Media","Social media reaches thousands instantly. Sharing environmental facts and tips spreads awareness exponentially.","Share one environmental fact or tip on social media weekly.","Reaches peers and amplifies the message"),
            ("Organize a Community Cleanup","Visible action inspires others. Community cleanups beautify areas AND raise awareness about littering and waste.","Organize a park or beach cleanup with friends and family.","Beautifies community and inspires others to care"),
            ("Teach Younger Kids","Kids teaching kids is powerful. Younger children look up to older ones and absorb their values.","Teach younger siblings or neighbors one eco-friendly habit.","Creates environmental awareness in the next generation"),
            ("Watch and Share Documentaries","Films about nature and environment create emotional connection. Recommend ones that moved you.","Watch an environmental documentary and discuss it with family.","Creates emotional investment in environmental protection"),
            ("Calculate Your Carbon Footprint","Online calculators show your personal environmental impact. Knowing your footprint helps you reduce it strategically.","Use an online calculator to measure your family's carbon footprint.","Creates awareness of personal impact and reduction targets"),
            ("Support Eco-Friendly Businesses","Where you spend money is a vote. Supporting green businesses encourages more businesses to be sustainable.","Research which brands are environmentally responsible. Choose them.","Market pressure pushes all businesses toward sustainability"),
            ("Make a Family Green Pledge","Committing together as a family creates accountability and makes changes stick. Written pledges are more effective.","Create a family environmental pledge with specific commitments.","Whole-family commitment amplifies individual actions"),
        ],
    }

    title_page(doc, "KIDS SAVING THE PLANET", "50 Ways You Can Help the Environment (Ages 7-13)", "50 Actions * Impact Data * Family Challenges * 30-Day Tracker")
    copyright_page(doc, "KIDS SAVING THE PLANET: 50 Ways You Can Help")
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0)
    y = 680
    for cat in categories:
        doc.add_text(72, y, f"{cat} (10 Actions)", 'F2', 13, 0.1)
        y -= 30
    doc.add_text(72, y, "30-Day Eco-Challenge Tracker", 'F4', 12, 0.2)
    doc.add_text(72, y-25, "My Environmental Pledge", 'F4', 12, 0.2)
    doc.new_page()

    # Climate intro
    doc.add_centered_text(720, "CLIMATE CHANGE EXPLAINED (Simply!)", 'F2', 16, 0)
    doc.add_line(150, 710, 462, 710, 1, 0.3)
    y = add_wrapped(doc, 72, 680, "Earth is getting warmer because of gases (like CO2) we put in the air by burning fossil fuels (coal, oil, gas). These gases act like a blanket, trapping heat. This causes ice to melt, seas to rise, and weather to become more extreme. The good news? WE can fix this! Every action matters. Small changes by millions of people create HUGE impact. You are not too young to make a difference - in fact, YOUR generation may be the one that saves the planet!", 'F4', 12, 0.2)
    doc.new_page()

    action_num = 0
    for cat_name, actions in categories.items():
        doc.add_filled_rect(50, 380, 512, 100, 0.9)
        doc.add_centered_text(440, cat_name.upper(), 'F2', 22, 0)
        doc.add_centered_text(400, f"Actions {action_num+1}-{action_num+10}", 'F1', 12, 0.3)
        doc.new_page()
        
        for name, why, how, impact in actions:
            action_num += 1
            doc.add_text(72, 730, f"ACTION #{action_num}", 'F1', 10, 0.4)
            doc.add_text(72, 710, name, 'F2', 16, 0)
            doc.add_line(72, 702, 400, 702, 1, 0.3)
            
            y = 680
            doc.add_text(72, y, "WHY IT MATTERS:", 'F2', 11, 0.1)
            y -= 18
            y = add_wrapped(doc, 90, y, why, 'F4', 10, 0.2, 68)
            
            y -= 15
            doc.add_text(72, y, "HOW TO DO IT:", 'F2', 11, 0.1)
            y -= 18
            y = add_wrapped(doc, 90, y, how, 'F1', 10, 0.2, 68)
            
            y -= 15
            doc.add_text(72, y, "YOUR IMPACT:", 'F2', 11, 0.1)
            y -= 18
            y = add_wrapped(doc, 90, y, impact, 'F1', 10, 0.3, 68)
            
            y -= 20
            doc.add_text(72, y, "FAMILY CHALLENGE:", 'F2', 11, 0.1)
            y -= 18
            doc.add_text(90, y, "Get your whole family to try this for one week. Track results!", 'F4', 10, 0.3)
            
            y -= 25
            doc.add_text(72, y, "[ ] I completed this action!  Date: _________", 'F1', 10, 0.4)
            doc.new_page()

    # 30-day tracker
    doc.add_centered_text(720, "30-DAY ECO-CHALLENGE TRACKER", 'F2', 16, 0)
    y = 690
    for day in range(1, 31):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "ECO-TRACKER (continued)", 'F2', 14, 0)
            y = 700
        doc.add_text(72, y, f"Day {day:2d}: [ ] Action: _________________________ Impact: ________________", 'F1', 9, 0.3)
        y -= 19
    doc.new_page()

    # Pledge page
    doc.add_centered_text(720, "MY ENVIRONMENTAL PLEDGE", 'F2', 18, 0)
    doc.add_filled_rect(50, 300, 512, 380, 0.95)
    doc.add_rect(60, 310, 492, 360, 2, 0.3)
    doc.add_centered_text(640, "I, ______________________________, pledge to:", 'F4', 13, 0.2)
    y = 600
    for i in range(5):
        doc.add_text(100, y, f"{i+1}. ___________________________________________________", 'F1', 11, 0.4)
        y -= 35
    doc.add_centered_text(420, "I will do my part to protect our planet every day.", 'F4', 12, 0.2)
    doc.add_centered_text(380, "Signed: ___________________ Date: ___________", 'F1', 11, 0.3)
    doc.new_page()

    certificate(doc, "PLANET PROTECTOR CERTIFICATE")
    add_supplemental(doc, 'Environment', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book336_Kids_Save_Planet.pdf')
    print("Book336_Kids_Save_Planet.pdf created successfully!")

if __name__ == "__main__":
    create_book()
