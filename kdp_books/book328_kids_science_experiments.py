from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    experiments = {
        "Chemistry": [
            ("Baking Soda Volcano", "Easy", "10 min", ["Baking soda","Vinegar","Food coloring","Dish soap","Container"], ["Place container on a tray","Add 2 tbsp baking soda","Add a drop of dish soap","Add food coloring","Pour in vinegar and watch!"], "The acetic acid in vinegar reacts with sodium bicarbonate to produce carbon dioxide gas. The bubbles create the eruption effect."),
            ("Invisible Ink", "Easy", "15 min", ["Lemon juice","Cotton swab","White paper","Lamp or iron"], ["Squeeze lemon juice into a cup","Dip cotton swab in juice","Write a secret message on paper","Let it dry completely","Hold paper near warm lamp to reveal"], "Lemon juice is an organic substance that oxidizes when heated. The heat breaks down the compounds, turning them brown."),
            ("Color Changing Milk", "Easy", "10 min", ["Whole milk","Food coloring","Dish soap","Plate","Cotton swab"], ["Pour milk onto a plate","Add drops of different food colors","Dip cotton swab in dish soap","Touch the swab to the milk center","Watch colors dance and swirl!"], "Dish soap breaks down fat molecules in milk. This creates movement that carries the food coloring in beautiful patterns."),
            ("Homemade Slime", "Medium", "20 min", ["White glue","Borax","Water","Food coloring","Bowl"], ["Mix 1/2 cup glue with 1/2 cup water","Add food coloring and stir","In another cup mix 1 tsp borax with 1 cup warm water","Slowly add borax solution to glue mixture","Knead until slime forms"], "Borax creates cross-links between the polymer chains in glue. This turns the liquid glue into a stretchy solid-like substance."),
            ("Crystal Growing", "Medium", "3 days", ["Sugar or salt","Hot water","Jar","String","Pencil"], ["Heat water until very hot (adult help)","Stir in sugar until no more dissolves","Pour solution into jar","Hang string from pencil across jar top","Wait 3-7 days for crystals to form"], "As water evaporates, dissolved molecules come together in an orderly pattern. This repeated pattern creates the geometric crystal shape."),
            ("Density Tower", "Easy", "15 min", ["Honey","Corn syrup","Dish soap","Water","Vegetable oil","Rubbing alcohol","Tall glass"], ["Pour honey into glass first","Slowly add corn syrup","Add dish soap carefully","Pour water very slowly","Add vegetable oil","Top with rubbing alcohol"], "Each liquid has a different density (weight per volume). Heavier liquids sink below lighter ones, creating distinct layers."),
            ("pH Testing with Cabbage", "Medium", "25 min", ["Red cabbage","Hot water","Clear cups","Lemon juice","Baking soda","Vinegar","Soap"], ["Chop cabbage and soak in hot water 10 min","Strain purple liquid into cups","Add different household liquids to each cup","Observe color changes","Record which are acids and which are bases"], "Red cabbage contains anthocyanin, a natural pH indicator. It turns red in acids, purple in neutral, and green-blue in bases."),
            ("Elephant Toothpaste", "Medium", "15 min", ["Hydrogen peroxide 3%","Yeast","Warm water","Dish soap","Food coloring","Bottle"], ["Pour hydrogen peroxide into bottle","Add food coloring and dish soap","Mix yeast with warm water in a cup","Pour yeast mixture into bottle quickly","Stand back and watch the foam!"], "Yeast contains catalase enzyme that rapidly breaks down hydrogen peroxide into water and oxygen gas. The soap traps oxygen in foam."),
            ("Penny Cleaning", "Easy", "10 min", ["Dirty pennies","Vinegar","Salt","Cup","Paper towels"], ["Mix 1/4 cup vinegar with 1 tsp salt","Drop dirty pennies into solution","Wait 30 seconds","Remove and rinse with water","Compare to uncleaned pennies"], "The acid in vinegar dissolves copper oxide (the dark coating). Salt makes the acid stronger. The result is shiny clean copper."),
            ("CO2 Balloon Inflator", "Easy", "10 min", ["Balloon","Baking soda","Vinegar","Empty bottle","Funnel"], ["Pour vinegar into the bottle (1/3 full)","Use funnel to put baking soda in balloon","Stretch balloon opening over bottle top","Lift balloon so soda falls into vinegar","Watch balloon inflate with CO2 gas"], "Baking soda and vinegar react to produce carbon dioxide gas. The gas expands and fills the balloon, inflating it without blowing."),
        ],
        "Physics": [
            ("Static Electricity Butterfly", "Easy", "10 min", ["Tissue paper","Balloon","Scissors","Wool cloth"], ["Cut tissue paper into butterfly shape","Blow up balloon and tie it","Rub balloon vigorously on wool","Hold balloon near tissue butterfly","Watch it fly up to the balloon!"], "Rubbing creates static electricity by transferring electrons. The charged balloon attracts the neutral tissue paper through electrostatic force."),
            ("Egg Drop Challenge", "Hard", "30 min", ["Raw egg","Straws","Tape","Cotton balls","Plastic bags","Newspaper"], ["Design a container to protect the egg","Use materials to cushion and slow the fall","Build your contraption around the egg","Drop from increasing heights","Redesign if egg breaks!"], "The goal is to reduce impact force by increasing deceleration time. Soft materials absorb energy and distribute force over more area."),
            ("Bernoulli Ball Float", "Easy", "5 min", ["Hair dryer","Ping pong ball","Funnel optional"], ["Turn hair dryer on high pointing up","Place ping pong ball in air stream","Let go - it floats!","Tilt dryer slowly - ball stays","Try with different sized balls"], "Fast-moving air has lower pressure than still air (Bernoulli's principle). The ball stays centered because surrounding higher pressure pushes it back."),
            ("Magnet Exploration", "Easy", "20 min", ["Bar magnet","Various objects (metal/non-metal)","Paper clips","Paper","Compass"], ["Test which objects are attracted to magnet","Try magnet through paper and cardboard","Make a chain of paper clips","Observe compass needle near magnet","Map the magnetic field with iron filings"], "Magnets attract ferromagnetic materials (iron, nickel, cobalt). Magnetic fields can pass through non-magnetic materials like paper."),
            ("Simple Catapult", "Medium", "20 min", ["Popsicle sticks (10)","Rubber bands","Plastic spoon","Pompom or marshmallow"], ["Stack 8 sticks and rubber band both ends","Place 1 stick perpendicular on top","Rubber band the crossing point","Attach spoon to top stick","Load pompom and launch!"], "The bent stick stores elastic potential energy. When released, it converts to kinetic energy, launching the projectile in an arc."),
            ("Light Refraction Rainbow", "Easy", "10 min", ["Glass of water","White paper","Sunlight or flashlight","Mirror optional"], ["Fill glass with water completely","Place on edge of table in sunlight","Position white paper on floor below","Adjust until rainbow appears on paper","Identify all 7 colors of the spectrum"], "White light contains all colors. Water bends (refracts) each color at slightly different angles, separating them into a visible spectrum."),
            ("Pendulum Waves", "Medium", "25 min", ["String (different lengths)","Nuts or washers","Ruler or dowel","Tape","Stopwatch"], ["Cut 5 strings of slightly different lengths","Tie a nut to each string end","Attach all strings to a ruler","Pull all back equally and release together","Watch the mesmerizing wave patterns"], "Pendulum period depends on length. Different lengths swing at different rates, creating beautiful wave patterns that shift over time."),
            ("Sound Vibration Viewer", "Easy", "10 min", ["Plastic wrap","Bowl or cup","Rice or salt grains","Speaker or pan"], ["Stretch plastic wrap tightly over bowl","Place rice grains on top","Hold near speaker playing music","Watch grains dance to the beat","Try different volumes and pitches"], "Sound is vibration traveling through air. These vibrations hit the plastic wrap, making it vibrate too, which bounces the rice grains."),
            ("Inertia Tablecloth Trick", "Medium", "15 min", ["Smooth cloth","Plastic plate","Plastic cup (empty)","Smooth table"], ["Place cloth on smooth table edge","Put plastic plate on cloth","Place empty cup on plate","Grab cloth edge firmly","Pull straight down FAST (not out)"], "Objects at rest tend to stay at rest (Newton's First Law). Pulling fast means friction doesn't have time to transfer enough force to move dishes."),
            ("Paper Airplane Science", "Easy", "20 min", ["Paper (various types)","Tape measure","Timer","Notebook"], ["Fold 5 different airplane designs","Throw each 3 times and measure distance","Record which flies farthest","Modify wings and test again","Find what makes the best flyer"], "Four forces act on planes: thrust, drag, lift, and gravity. Wing shape and angle determine how air flows, affecting lift and distance."),
        ],
        "Biology": [
            ("Seed Germination Lab", "Easy", "7 days", ["Bean seeds","Paper towels","Plastic bags","Water","Tape"], ["Wet paper towel (damp not soaking)","Place 3 seeds on towel","Put towel in plastic bag (leave open)","Tape to sunny window","Record growth daily for 1 week"], "Seeds contain an embryo plant and food supply. Water activates enzymes that break down stored food, giving energy for the sprout to grow."),
            ("Build a Terrarium", "Medium", "30 min", ["Clear jar or bottle","Small rocks","Charcoal","Potting soil","Small plants","Water spray"], ["Layer rocks at bottom (1 inch)","Add thin charcoal layer","Add 2-3 inches of soil","Plant small plants carefully","Spray with water and seal"], "Terrariums are miniature ecosystems. Water evaporates, condenses on walls, and falls back like rain. Plants produce oxygen and recycle CO2."),
            ("Celery Color Transport", "Easy", "24 hours", ["Celery stalks with leaves","Food coloring","Clear glasses","Water","Knife (adult help)"], ["Fill glasses with water and add food color","Cut celery bottom at angle","Place stalks in colored water","Wait 24 hours","Cut stalk open to see colored tubes"], "Plants transport water through xylem tubes (like tiny straws). Capillary action and transpiration pull water up from roots to leaves."),
            ("Yeast Alive Experiment", "Easy", "15 min", ["Active dry yeast","Warm water","Sugar","Balloon","Empty bottle"], ["Add warm water to bottle","Stir in 1 packet of yeast","Add 1 tbsp sugar","Stretch balloon over bottle top","Watch balloon inflate over 15 minutes"], "Yeast are living single-celled fungi. They eat sugar and produce carbon dioxide gas and alcohol through fermentation. The gas inflates the balloon."),
            ("Fingerprint Detective", "Easy", "20 min", ["Inkpad or pencil graphite","Clear tape","White paper","Magnifying glass","Index cards"], ["Press finger on inkpad or penciled paper","Press finger onto white paper clearly","Use magnifying glass to examine patterns","Compare prints from all 10 fingers","Classify as loop, whorl, or arch"], "Fingerprints form before birth and never change. The three main patterns are loops (60%), whorls (35%), and arches (5%). No two are identical."),
            ("Owl Pellet Dissection", "Medium", "30 min", ["Owl pellet (buy online)","Toothpicks","Tweezers","Paper plate","Bone chart"], ["Soak pellet in water 10 minutes","Gently pull apart with toothpicks","Separate fur/feathers from bones","Identify bones using chart","Reconstruct the prey skeleton"], "Owls swallow prey whole. They cannot digest bones, fur, and feathers. These form a pellet that the owl regurgitates. It reveals what they ate."),
            ("Mold Bread Experiment", "Easy", "7 days", ["Bread slices (no preservatives)","Plastic bags","Water","Labels","Dark place"], ["Put dry bread in one sealed bag","Put damp bread in another sealed bag","Label and put both in dark warm spot","Check daily without opening","Record mold growth differences"], "Mold is a fungus that needs moisture, warmth, food, and darkness to grow. The wet bread provides ideal conditions for rapid mold colonization."),
            ("Heart Rate Explorer", "Easy", "15 min", ["Stopwatch or timer","Notebook","Pencil","Jump rope optional"], ["Find your pulse (wrist or neck)","Count beats for 15 sec, multiply by 4","Record resting heart rate","Do jumping jacks for 1 minute","Immediately measure again and compare"], "Your heart pumps faster during exercise to deliver more oxygen to working muscles. Fit people's hearts recover to resting rate faster."),
            ("Photosynthesis Test", "Medium", "3 days", ["Plant with large leaves","Aluminum foil","Tape","Sunlight"], ["Cover half of one leaf with foil","Tape foil securely in place","Leave plant in sunlight for 3 days","Remove foil and compare leaf halves","Covered half will be lighter/yellow"], "Plants need light to make food (photosynthesis). Without light, chlorophyll breaks down and the leaf cannot produce glucose for energy."),
            ("DNA Extraction", "Medium", "20 min", ["Strawberry","Dish soap","Salt","Rubbing alcohol (cold)","Plastic bag","Coffee filter","Cup"], ["Mash strawberry in sealed bag","Add soap and salt solution","Filter through coffee filter into cup","Slowly pour cold alcohol on top","Watch white stringy DNA appear!"], "Soap breaks open cell membranes. Salt clumps proteins. DNA is less dense than alcohol, so it rises and becomes visible as white strands."),
        ],
        "Earth Science": [
            ("Rock Cycle in a Cup", "Easy", "20 min", ["Crayon shavings (3 colors)","Aluminum foil","Warm water","Cup","Wax paper"], ["Shave crayons into small pieces by color","Layer shavings in foil cup (sediment)","Press hard with thumb (sedimentary rock)","Place in warm water to soften (metamorphic)","Melt fully and cool (igneous rock)"], "The rock cycle shows how rocks transform. Pressure creates sedimentary, heat and pressure make metamorphic, and melting/cooling creates igneous."),
            ("Earthquake Simulator", "Easy", "15 min", ["Jello (made and set)","Building blocks or sugar cubes","Plate","Table"], ["Make jello in a flat pan and let set","Build structures on top of jello","Gently shake the pan","Observe which buildings fall first","Redesign buildings to withstand shaking"], "Earthquakes happen when tectonic plates move suddenly. Soft ground (like jello) amplifies shaking. Wider, lower buildings are more stable."),
            ("Cloud in a Bottle", "Medium", "10 min", ["Clear plastic bottle","Warm water","Match (adult help)","Flashlight"], ["Add small amount of warm water to bottle","Squeeze and release bottle a few times","Have adult light match and drop in bottle","Squeeze bottle hard then release quickly","Shine flashlight to see cloud form"], "Clouds form when water vapor condenses on particles. Squeezing changes pressure and temperature, causing condensation on smoke particles."),
            ("Water Cycle in a Bag", "Easy", "2 days", ["Ziplock bag","Water","Blue food coloring","Tape","Sunny window"], ["Add water with blue food coloring to bag","Seal bag tightly","Tape to sunny window","Observe over 1-2 days","See evaporation and condensation!"], "The sun heats water causing evaporation. Water vapor rises, cools on the bag's surface, condenses into droplets, and drips back down like rain."),
            ("Soil Layers Jar", "Easy", "24 hours", ["Clear jar with lid","Garden soil","Water","Spoon"], ["Fill jar 1/3 with soil","Add water to nearly full","Put lid on and shake vigorously","Let sit undisturbed for 24 hours","Observe layers: gravel, sand, silt, clay"], "Different soil particles have different sizes and weights. Heavy particles (gravel, sand) settle first. Light particles (silt, clay) settle last."),
            ("Fossil Making", "Easy", "24 hours", ["Clay or plaster of paris","Shells, leaves, toy dinosaurs","Petroleum jelly","Container","Water"], ["Coat objects in petroleum jelly","Press objects into flattened clay","Remove objects carefully","Let clay dry 24 hours","Observe your fossil impressions!"], "Real fossils form when organisms are buried in sediment. Over millions of years, minerals replace organic material, preserving the shape."),
            ("Wind Direction Finder", "Easy", "20 min", ["Straw","Pin","Pencil with eraser","Construction paper","Compass"], ["Cut arrow point and tail from paper","Tape to straw ends (tail bigger)","Push pin through straw center into eraser","Find north with compass","Place outside and observe wind direction"], "Wind vanes point INTO the wind. The larger tail catches wind and pushes away, making the arrow point toward the wind source direction."),
            ("Mini Water Filter", "Medium", "25 min", ["Plastic bottle (cut in half)","Sand","Gravel","Cotton balls","Dirty water","Cup"], ["Place cotton in bottle neck (upside down)","Add layer of sand","Add layer of gravel","Pour dirty water through slowly","Collect filtered water in cup below"], "Filtration removes particles by size. Gravel catches large debris, sand catches smaller particles, and cotton catches finest particles."),
            ("Erosion Experiment", "Easy", "15 min", ["3 trays or pans","Soil","Grass or leaves","Rocks","Watering can"], ["Fill trays with soil (bare, grass-covered, rocky)","Tilt all trays at same angle","Pour equal water on each","Observe which erodes most","Measure soil in runoff water"], "Plant roots hold soil in place. Bare soil erodes fastest. This is why deforestation leads to landslides and why farmers plant cover crops."),
            ("Weather Station", "Medium", "30 min", ["Jar","Balloon","Straw","Tape","Ruler","Notebook"], ["Cut balloon and stretch over jar opening","Tape straw horizontally on balloon surface","Mark a scale on paper behind straw","Record straw position daily","Compare to weather reports"], "This is a simple barometer. Air pressure pushes on the balloon. High pressure pushes it down (straw up). Low pressure lets it rise (straw down)."),
        ],
        "Engineering": [
            ("Bridge Building Challenge", "Medium", "30 min", ["Popsicle sticks","White glue","String","Small weights","Cups"], ["Design a bridge to span 12 inches","Build using only sticks and glue","Let glue dry completely","Place bridge across two cups","Add weights until it breaks - record max"], "Triangles are the strongest shape in engineering. Distributing weight across multiple points and using tension members increases bridge strength."),
            ("Balloon Rocket Car", "Easy", "15 min", ["Balloon","Straw","Tape","Cardboard","Bottle caps","Skewers"], ["Cut cardboard rectangle for car body","Push skewers through for axles","Attach bottle cap wheels","Tape straw on top, insert balloon end","Blow up balloon and release to race!"], "Newton's Third Law: every action has an equal opposite reaction. Air rushing backward out of the balloon pushes the car forward."),
            ("Spaghetti Tower", "Easy", "20 min", ["Dry spaghetti","Marshmallows","Tape measure","Timer"], ["Use marshmallows to connect spaghetti","Build the tallest tower possible in 15 min","Tower must stand on its own","Measure height when time is up","What design worked best?"], "Tall structures need wide bases for stability. Triangular bracing prevents buckling. The center of gravity must stay over the base."),
            ("Rubber Band Helicopter", "Medium", "20 min", ["Paper","Rubber band","Paper clip","Scissors","Pencil"], ["Cut paper strip 1x8 inches","Fold in half and bend ends opposite ways","Attach paper clip at fold","Hook rubber band to paper clip","Wind rubber band and release!"], "The twisted rubber band stores elastic potential energy. When released, it spins the paper blades. Angled blades push air down, creating lift."),
            ("Water Wheel Generator", "Medium", "25 min", ["Plastic cups (small)","Cardboard circle","Pencil or dowel","Water jug","Tape","String"], ["Tape small cups around cardboard circle edge","Push pencil through center as axle","Tie string to axle with small weight","Hold under running water","Watch wheel spin and lift the weight!"], "Flowing water has kinetic energy. The wheel converts this into rotational energy. Real hydroelectric dams use this principle to generate electricity."),
            ("Newspaper Table", "Easy", "15 min", ["Newspaper","Tape","Scissors","Heavy book for testing"], ["Roll newspaper sheets into tight tubes","Tape tubes securely","Build a table structure with tube legs","Add flat newspaper top","Test how much weight it holds"], "Tubes are much stronger than flat sheets because they resist bending in all directions. This is why bones and pipes are cylindrical."),
            ("Zip Line Engineering", "Easy", "15 min", ["String or fishing line","Straw","Tape","Small toy figure","Two high/low points"], ["Tie string between two points (angled)","Thread straw onto string","Tape toy figure to straw","Release from high end","Observe speed and adjust angle"], "Gravity pulls objects downhill along the line. Steeper angles mean more speed. Friction between straw and string slows the rider."),
            ("Parachute Design", "Easy", "20 min", ["Plastic bags","String","Small toy","Scissors","Tape","Stopwatch"], ["Cut squares of different sizes from bags","Attach 4 equal strings to corners","Tie strings to small toy","Drop from same height","Time each - which falls slowest?"], "Parachutes work by increasing air resistance (drag). Larger surface area catches more air, creating more drag and slower descent."),
            ("Marble Run Builder", "Medium", "30 min", ["Cardboard tubes","Tape","Scissors","Box","Marble"], ["Cut tubes in half lengthwise for tracks","Tape tracks inside box at angles","Create turns and drops","Test marble from top","Redesign until marble reaches bottom"], "Gravity accelerates the marble downhill. Angles and curves change the direction of momentum. Friction slows it on flat sections."),
            ("Straw Rocket Launcher", "Easy", "15 min", ["Paper","Straws (2 sizes)","Tape","Scissors","Clay"], ["Roll paper tightly around larger straw","Tape paper tube and seal one end with clay","Slide paper rocket over smaller straw","Blow hard into smaller straw","Measure how far rocket flies!"], "Your breath creates air pressure inside the straw. This pressure pushes the sealed rocket off the end. The clay adds mass for stability."),
        ],
    }

    title_page(doc, "50 AWESOME SCIENCE EXPERIMENTS FOR KIDS", "Easy Projects You Can Do at Home (Ages 7-12)", "Chemistry * Physics * Biology * Earth Science * Engineering")
    copyright_page(doc, "50 AWESOME SCIENCE EXPERIMENTS FOR KIDS")
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0)
    doc.add_line(180, 710, 432, 710, 1, 0.3)
    y = 680
    for cat in experiments:
        doc.add_text(72, y, f"{cat} Experiments (10)", 'F2', 13, 0.1)
        y -= 30
    doc.new_page()

    # Safety page
    doc.add_centered_text(720, "SAFETY FIRST!", 'F2', 20, 0)
    doc.add_line(200, 710, 412, 710, 1, 0.3)
    rules = [
        "1. Always have an adult nearby when doing experiments",
        "2. Wear safety goggles if working with liquids",
        "3. Never taste or eat experiment materials",
        "4. Work in a well-ventilated area",
        "5. Clean up your workspace when finished",
        "6. Read ALL instructions before starting",
        "7. If something goes wrong, tell an adult immediately",
        "8. Wash your hands after every experiment",
    ]
    y = 670
    for r in rules:
        doc.add_text(72, y, r, 'F1', 13, 0.2)
        y -= 35
    doc.new_page()

    # Experiments
    exp_num = 0
    for category, exps in experiments.items():
        # Category divider
        doc.add_filled_rect(50, 350, 512, 150, 0.9)
        doc.add_centered_text(440, f"{category.upper()} EXPERIMENTS", 'F2', 24, 0)
        doc.add_centered_text(400, f"Experiments {exp_num+1}-{exp_num+10}", 'F1', 14, 0.3)
        doc.new_page()
        
        for name, diff, time, materials, steps, science in exps:
            exp_num += 1
            # Experiment page
            doc.add_text(72, 730, f"EXPERIMENT #{exp_num}", 'F1', 10, 0.4)
            doc.add_text(72, 710, name, 'F2', 18, 0)
            doc.add_line(72, 703, 400, 703, 1, 0.3)
            
            doc.add_text(72, 680, f"Difficulty: {diff}", 'F1', 11, 0.3)
            doc.add_text(250, 680, f"Time: {time}", 'F1', 11, 0.3)
            
            # Materials
            doc.add_text(72, 650, "MATERIALS:", 'F2', 12, 0.1)
            y = 632
            for m in materials:
                doc.add_text(90, y, f"* {m}", 'F1', 10, 0.2)
                y -= 16
            
            # Steps
            y -= 10
            doc.add_text(72, y, "STEPS:", 'F2', 12, 0.1)
            y -= 18
            for i, s in enumerate(steps):
                lines = wrap(s, 65)
                for j, l in enumerate(lines):
                    if y < 80:
                        doc.new_page()
                        y = 720
                    prefix = f"{i+1}. " if j == 0 else "   "
                    doc.add_text(90, y, f"{prefix}{l}", 'F1', 10, 0.2)
                    y -= 16
            
            # Science
            y -= 15
            if y < 120:
                doc.new_page()
                y = 720
            doc.add_text(72, y, "THE SCIENCE BEHIND IT:", 'F2', 12, 0.1)
            y -= 18
            for l in wrap(science, 70):
                if y < 80:
                    doc.new_page()
                    y = 720
                doc.add_text(90, y, l, 'F4', 10, 0.2)
                y -= 16
            
            # Observation space
            y -= 15
            if y < 100:
                doc.new_page()
                y = 720
            doc.add_text(72, y, "WHAT DID YOU OBSERVE?", 'F2', 11, 0.1)
            y -= 18
            doc.add_text(90, y, "________________________________________________________", 'F1', 10, 0.4)
            y -= 18
            doc.add_text(90, y, "________________________________________________________", 'F1', 10, 0.4)
            
            doc.new_page()

    # Science journal pages
    for pg in range(3):
        doc.add_centered_text(720, "MY EXPERIMENT JOURNAL", 'F2', 16, 0)
        doc.add_text(72, 690, "Experiment Name: _____________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 660, "Date: _______________  Hypothesis: ___________________________", 'F1', 11, 0.3)
        doc.add_text(72, 630, "What happened: _______________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 610, "_______________________________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 580, "Was my hypothesis correct?  YES  /  NO", 'F1', 11, 0.3)
        doc.add_text(72, 550, "What I learned: ______________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 530, "_______________________________________________________________", 'F1', 11, 0.3)
        doc.add_text(72, 500, "Draw your results:", 'F2', 11, 0.3)
        doc.add_rect(72, 250, 468, 240, 1, 0.5)
        doc.new_page()

    certificate(doc, "YOUNG SCIENTIST CERTIFICATE")
    add_supplemental(doc, 'Science', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book328_Kids_Science_Experiments.pdf')
    print("Book328_Kids_Science_Experiments.pdf created successfully!")

if __name__ == "__main__":
    create_book()
