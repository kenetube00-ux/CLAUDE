"""
Book 67: How To Grow Vegetables At Home - A Beginner's Garden Guide
KDP Interior - 8.5x11 inches (612x792 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "HOW TO GROW VEGETABLES", font='F2', size=26)
    pdf.add_centered_text(610, "AT HOME", font='F2', size=26)
    pdf.add_centered_text(570, "A Beginner's Garden Guide", font='F1', size=16)
    pdf.add_line(120, 545, 492, 545, 2)
    pdf.add_centered_text(500, "From Seed to Harvest: Everything", font='F4', size=14)
    pdf.add_centered_text(475, "You Need for a Thriving Garden", font='F4', size=14)
    pdf.add_centered_text(390, "By", font='F1', size=12)
    pdf.add_centered_text(360, "Daniel Tesfamariam", font='F2', size=18)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "How To Grow Vegetables At Home", font='F2', size=12)
    pdf.add_centered_text(595, "A Beginner's Garden Guide", font='F1', size=11)
    pdf.add_centered_text(560, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(535, "No part of this book may be reproduced without permission.", font='F1', size=10)
    pdf.add_centered_text(500, "Author: Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(475, "Published via Amazon KDP", font='F1', size=11)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: Why Grow Your Own Food", [
            "Home-grown vegetables taste dramatically better than store-bought produce.",
            "You control exactly what goes on your food: no pesticides if you choose.",
            "Growing food saves money. A single tomato plant can produce 20 pounds of tomatoes.",
            "Gardening provides gentle exercise that burns calories without feeling like work.",
            "Time spent in the garden reduces stress and improves mental health significantly.",
            "Children who garden eat more vegetables and develop a better relationship with food.",
            "You reduce your carbon footprint by eliminating transportation and packaging.",
            "Fresh vegetables harvested minutes before eating retain maximum nutrition.",
            "Gardening connects you to seasonal rhythms and teaches patience naturally.",
            "A small garden bed can produce hundreds of dollars worth of food per season.",
            "You gain food security and self-reliance by growing even a portion of your food.",
            "Starting a garden is one of the most rewarding skills you will ever develop.",
        ]),
        ("Chapter 2: Planning Your Garden Space", [
            "Most vegetables need at least six to eight hours of direct sunlight daily.",
            "Observe your yard throughout the day to identify the sunniest spots.",
            "Start small: a 4 by 4 foot raised bed is perfect for a first garden.",
            "Raised beds offer better drainage, fewer weeds, and easier access.",
            "You can also garden in containers on a patio, balcony, or driveway.",
            "Place your garden near a water source to make watering convenient.",
            "Avoid areas under large trees where roots compete for water and nutrients.",
            "South-facing locations receive the most sunlight in the northern hemisphere.",
            "Level ground prevents water from running off before soaking in.",
            "Consider proximity to your kitchen since you will harvest daily when producing.",
            "Sketch a simple map of your space noting sun exposure and dimensions.",
            "Good planning before planting prevents problems and wasted effort later.",
        ]),
        ("Chapter 3: Understanding Your Climate Zone", [
            "The USDA Hardiness Zone Map divides North America into 13 planting zones.",
            "Your zone number tells you the average minimum winter temperature in your area.",
            "Find your zone at planagrden.gov or on seed packet labels and plant tags.",
            "Your zone determines which plants survive winter and when to plant each crop.",
            "Frost dates are critical: last spring frost and first fall frost define your season.",
            "Search your city plus last frost date to find your specific dates online.",
            "Cool-season crops like lettuce and peas grow best in spring and fall.",
            "Warm-season crops like tomatoes and peppers need soil above 60 degrees.",
            "Plant cool-season crops four to six weeks before the last frost date.",
            "Plant warm-season crops two weeks after the last frost when soil is warm.",
            "Your growing season length determines which varieties to choose.",
            "Short-season gardeners should select early-maturing varieties for best results.",
        ]),
        ("Chapter 4: Soil Preparation Basics", [
            "Good soil is the single most important factor in growing healthy vegetables.",
            "Ideal garden soil is dark, crumbly, and smells earthy and fresh.",
            "Most native soil needs improvement with organic matter before planting.",
            "Compost is the best soil amendment: it improves drainage, nutrients, and structure.",
            "Add two to four inches of compost to your bed and mix into the top eight inches.",
            "For raised beds, fill with a mix of topsoil, compost, and perlite.",
            "A soil test from your local extension office reveals pH and nutrient levels.",
            "Most vegetables prefer slightly acidic to neutral soil with pH 6.0 to 7.0.",
            "Clay soil needs compost and sand to improve drainage and prevent waterlogging.",
            "Sandy soil needs compost to improve water retention and nutrient holding.",
            "Never work wet soil as this compacts it and destroys beneficial structure.",
            "Healthy soil is alive with billions of microorganisms that feed your plants.",
        ]),
        ("Chapter 5: Starting from Seeds vs Transplants", [
            "Seeds are cheaper and offer far more variety than nursery transplants.",
            "Transplants give you a head start and are easier for absolute beginners.",
            "Some crops must be direct-seeded: carrots, beans, peas, and radishes.",
            "Some crops benefit from indoor starting: tomatoes, peppers, and eggplant.",
            "Start seeds indoors six to eight weeks before your transplant date outside.",
            "Seeds need warmth, moisture, and light to germinate successfully.",
            "Use seed starting mix, not garden soil, for indoor seed starting.",
            "Place seed trays near a sunny south-facing window or under grow lights.",
            "Keep soil consistently moist but not waterlogged during germination.",
            "Harden off indoor seedlings by gradually exposing them to outdoor conditions.",
            "Move transplants outside for one hour the first day, increasing daily for a week.",
            "Direct-seeded crops are simpler: just plant the seed in the ground and water.",
        ]),
        ("Chapter 6: Easiest Vegetables for Beginners", [
            "Lettuce and salad greens grow quickly, producing harvests in just 30 days.",
            "Radishes are the fastest vegetable: ready to eat in only 25 to 30 days.",
            "Cherry tomatoes are more forgiving than large tomatoes and produce abundantly.",
            "Zucchini and summer squash grow vigorously and produce more than you can eat.",
            "Green beans are nearly foolproof. Plant seeds directly after last frost.",
            "Cucumbers climb trellises saving space and produce heavily all summer.",
            "Herbs like basil, parsley, and cilantro grow easily in gardens or pots.",
            "Peppers (sweet and hot) thrive in warm weather with minimal fuss.",
            "Kale is extremely hardy and produces leaves from spring through winter frost.",
            "Garlic is planted in fall and requires almost zero care until summer harvest.",
            "Start with three to five of these easy crops for your first garden season.",
            "Success with easy crops builds confidence for more challenging vegetables later.",
        ]),
        ("Chapter 7: Watering Properly", [
            "Most vegetables need one to two inches of water per week from rain or irrigation.",
            "Water deeply and less frequently rather than shallow daily sprinklings.",
            "Deep watering encourages roots to grow down where moisture is more consistent.",
            "Water in the morning so leaves dry during the day, preventing disease.",
            "Avoid wetting foliage. Water at the base of plants whenever possible.",
            "Drip irrigation or soaker hoses deliver water directly to roots efficiently.",
            "Mulch around plants with straw or wood chips to retain soil moisture.",
            "Stick your finger two inches into soil. If dry at that depth, water immediately.",
            "Container gardens need more frequent watering, often daily in hot weather.",
            "Wilting in afternoon heat is normal but wilting in morning means water is needed.",
            "Overwatering causes root rot which kills plants faster than underwatering.",
            "Consistent watering prevents problems like blossom end rot on tomatoes and peppers.",
        ]),
        ("Chapter 8: Fertilizing Naturally", [
            "Plants need three main nutrients: nitrogen, phosphorus, and potassium (N-P-K).",
            "Nitrogen promotes leaf growth and green color for leafy vegetables.",
            "Phosphorus supports root development and fruit production.",
            "Potassium strengthens overall plant health and disease resistance.",
            "Compost provides a balanced, slow-release supply of all essential nutrients.",
            "Add compost as a side dressing around plants every four to six weeks.",
            "Fish emulsion is an excellent liquid organic fertilizer for quick feeding.",
            "Worm castings are gentle and can be applied without risk of burning plants.",
            "Bone meal adds phosphorus for strong roots and better fruit set.",
            "Blood meal adds nitrogen for leafy greens that need extra green growth.",
            "Avoid over-fertilizing which can burn plants and create excess leaf growth.",
            "Feed the soil with organic matter and the soil will feed your plants naturally.",
        ]),
        ("Chapter 9: Dealing with Pests Organically", [
            "Prevention is the best pest management: healthy plants resist pests naturally.",
            "Inspect plants regularly so you catch pest problems before they become severe.",
            "Handpick large pests like caterpillars, slugs, and beetles into soapy water.",
            "A strong spray of water from the hose knocks off aphids and spider mites.",
            "Neem oil spray works against a wide range of soft-bodied insect pests.",
            "Diatomaceous earth sprinkled around plants deters slugs and crawling insects.",
            "Row covers physically block flying pests from reaching your plants.",
            "Companion planting with marigolds, basil, and herbs repels many common pests.",
            "Attract beneficial insects like ladybugs and lacewings that eat pest insects.",
            "Plant flowers near your garden to support beneficial predator populations.",
            "Rotating crops yearly prevents pest populations from building up in soil.",
            "Accept minor pest damage. A few holes in leaves do not ruin the harvest.",
        ]),
        ("Chapter 10: Companion Planting Guide", [
            "Companion planting pairs crops that benefit each other when grown nearby.",
            "Tomatoes grow well with basil which may improve flavor and repel pests.",
            "Carrots and onions planted together confuse each other's pest flies.",
            "Corn, beans, and squash (the three sisters) support each other symbiotically.",
            "Beans fix nitrogen that corn and squash use. Corn supports bean vines.",
            "Squash leaves shade the ground reducing weeds for all three crops.",
            "Marigolds planted throughout the garden repel nematodes and many insects.",
            "Avoid planting tomatoes near brassicas (broccoli, cabbage) as they inhibit growth.",
            "Keep fennel away from most vegetables as it suppresses their growth.",
            "Lettuce grows well in the shade of taller plants like tomatoes in summer.",
            "Radishes planted with slower crops like carrots mark rows and break up soil.",
            "Experiment with companion planting and note what works in your specific garden.",
        ]),
        ("Chapter 11: Container Gardening", [
            "Containers let you garden anywhere: patios, balconies, driveways, and porches.",
            "Almost any vegetable can grow in a container if the pot is large enough.",
            "Use pots at least 12 inches deep and wide for most vegetables.",
            "Tomatoes, peppers, and eggplant need five-gallon containers minimum.",
            "Herbs, lettuce, and radishes grow happily in smaller containers.",
            "Ensure every container has drainage holes to prevent waterlogged roots.",
            "Use potting mix, not garden soil, which is too heavy and drains poorly in pots.",
            "Containers dry out faster than ground beds so check water needs daily.",
            "Self-watering containers reduce watering frequency with built-in reservoirs.",
            "Feed container plants every two weeks since watering flushes nutrients out.",
            "Group containers together for an attractive display and easier watering.",
            "Container gardening is perfect for renters who cannot dig in-ground beds.",
        ]),
        ("Chapter 12: Vertical Gardening", [
            "Vertical gardening grows plants upward on supports to save ground space.",
            "Cucumbers, peas, beans, and small melons all climb trellises naturally.",
            "A simple trellis can be made from wood stakes and twine for under ten dollars.",
            "Cattle panels bent into arches create beautiful and productive tunnel trellises.",
            "Vertical growing improves air circulation which reduces fungal disease.",
            "Plants grown vertically receive more even sunlight on all their leaves.",
            "Harvesting is easier when fruits hang at eye level instead of ground level.",
            "Tomato cages support indeterminate tomatoes that grow six feet or taller.",
            "String trellising uses overhead strings that vines climb up naturally.",
            "Stacking raised beds or using wall planters maximizes tiny spaces.",
            "Even a blank fence or wall can support climbing vegetables with hooks and wire.",
            "Vertical gardens can triple your harvest in the same footprint of ground space.",
        ]),
        ("Chapter 13: When to Harvest", [
            "Harvest most vegetables when they are young and tender for best flavor.",
            "Zucchini tastes best at six to eight inches. Large ones become tough and seedy.",
            "Tomatoes are ready when fully colored and slightly soft to gentle pressure.",
            "Pick beans when pods snap cleanly and before seeds bulge through the skin.",
            "Lettuce can be harvested leaf by leaf or by cutting the whole head.",
            "Cut-and-come-again lettuce regrows multiple harvests from one planting.",
            "Carrots are ready when the top of the root is visible at the soil surface.",
            "Peppers can be picked green for mild flavor or left to ripen for sweeter taste.",
            "Cucumbers taste best picked young before seeds develop and skin toughens.",
            "Herbs should be harvested regularly to encourage bushy growth and prevent bolting.",
            "Morning harvest after dew dries yields the crispest, most flavorful vegetables.",
            "Regular harvesting signals plants to produce more, extending your total yield.",
        ]),
        ("Chapter 14: Storing Your Harvest", [
            "Most vegetables last longest stored in the refrigerator crisper drawer.",
            "Tomatoes should never be refrigerated as cold destroys their flavor and texture.",
            "Root vegetables like carrots and beets store for months in a cool dark place.",
            "Freezing preserves vegetables for six to twelve months with minimal effort.",
            "Blanch vegetables briefly in boiling water before freezing to preserve color.",
            "Canning allows you to store tomato sauce, pickles, and salsa for over a year.",
            "Dehydrating herbs and vegetables concentrates flavor and requires no refrigeration.",
            "Garlic and onions cure in a warm dry place for two weeks then store for months.",
            "Winter squash cures similarly and stores three to six months at room temperature.",
            "Pickling cucumbers, peppers, and green beans preserves them deliciously.",
            "Share excess harvest with neighbors, food banks, or community refrigerators.",
            "Proper storage ensures you enjoy your garden harvest long after the season ends.",
        ]),
        ("Chapter 15: Season-by-Season Calendar", [
            "Late winter: order seeds, plan your garden layout, start tomatoes indoors.",
            "Early spring: start peppers indoors, prepare beds, plant peas and greens outside.",
            "Mid spring: transplant cold-hardy crops, direct-sow beets, carrots, and radishes.",
            "Late spring: after last frost, transplant tomatoes, peppers, and plant beans.",
            "Early summer: plant squash, cucumbers, and succession-sow lettuce for continuous harvest.",
            "Midsummer: harvest heavily, water consistently, plant fall crops like kale and broccoli.",
            "Late summer: start fall lettuce, plant garlic cloves for next year's harvest.",
            "Early fall: harvest remaining warm-season crops before first frost arrives.",
            "Mid fall: plant garlic, add compost to empty beds, plant cover crops.",
            "Late fall: mulch beds heavily, clean and store tools, reflect on the season.",
            "Winter: plan next year's garden, order seeds early, repair raised beds.",
            "Each season offers gardening tasks that prepare you for the next productive cycle.",
        ]),
    ]

    page_num = 1
    for title, lines in chapters:
        pdf.new_page()
        pdf.add_centered_text(740, title, font='F2', size=16)
        pdf.add_line(70, 725, 542, 725, 1)
        y = 700
        for line in lines:
            pdf.add_text(60, y, line, font='F4', size=11)
            y -= 24
        pdf.add_centered_text(40, str(page_num), font='F1', size=10)
        page_num += 1

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book67_How_To_Grow_Vegetables.pdf')
    print("Book 67 created: Book67_How_To_Grow_Vegetables.pdf")

if __name__ == '__main__':
    create_book()
