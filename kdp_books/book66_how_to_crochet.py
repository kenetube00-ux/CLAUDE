"""
Book 66: How To Crochet For Beginners - Learn the Basics Step by Step
KDP Interior - 8.5x11 inches (612x792 points)
"""
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)

    # --- TITLE PAGE ---
    pdf.new_page()
    pdf.add_centered_text(650, "HOW TO CROCHET", font='F2', size=28)
    pdf.add_centered_text(610, "FOR BEGINNERS", font='F2', size=24)
    pdf.add_centered_text(570, "Learn the Basics Step by Step", font='F1', size=16)
    pdf.add_line(120, 545, 492, 545, 2)
    pdf.add_centered_text(500, "Master Every Stitch from Your", font='F4', size=14)
    pdf.add_centered_text(475, "Very First Chain to Finished Projects", font='F4', size=14)
    pdf.add_centered_text(390, "By", font='F1', size=12)
    pdf.add_centered_text(360, "Daniel Tesfamariam", font='F2', size=18)

    # --- COPYRIGHT PAGE ---
    pdf.new_page()
    pdf.add_centered_text(620, "How To Crochet For Beginners", font='F2', size=12)
    pdf.add_centered_text(595, "Learn the Basics Step by Step", font='F1', size=11)
    pdf.add_centered_text(560, "Copyright 2026 Daniel Tesfamariam. All Rights Reserved.", font='F1', size=10)
    pdf.add_centered_text(535, "No part of this book may be reproduced without permission.", font='F1', size=10)
    pdf.add_centered_text(500, "Author: Daniel Tesfamariam", font='F2', size=11)
    pdf.add_centered_text(475, "Published via Amazon KDP", font='F1', size=11)

    # --- CHAPTERS ---
    chapters = [
        ("Chapter 1: What You Need to Start", [
            "Crochet requires only two things: a hook and some yarn. That is truly all.",
            "Start with a medium weight yarn, also called worsted weight or category 4.",
            "Acrylic yarn is the best choice for beginners: affordable, easy to work with, and washable.",
            "Choose a light-colored yarn so you can see your stitches clearly as you learn.",
            "A 5mm or size H/8 crochet hook pairs perfectly with medium weight yarn.",
            "Aluminum hooks are smooth and affordable. They are ideal for your first projects.",
            "You will also want a pair of scissors and a yarn needle for finishing.",
            "A stitch marker (or a safety pin) helps you track where rows begin.",
            "You can find all beginner supplies at craft stores or online for under 15 dollars.",
            "Avoid dark colored yarn, fluffy yarn, or very thin yarn when starting out.",
            "Your total investment to start crocheting is less than a single dinner out.",
            "Once you learn the basics, you will have a relaxing hobby that produces beautiful gifts.",
        ]),
        ("Chapter 2: Choosing Yarn and Hooks", [
            "Yarn comes in different weights from lace (very thin) to jumbo (very thick).",
            "The yarn label tells you everything: weight, hook size, fiber content, and yardage.",
            "Weight 4 (worsted/medium) is the standard learning weight for all beginners.",
            "Popular beginner yarn brands include Red Heart Super Saver and Caron Simply Soft.",
            "Hooks are sized by millimeters and also have letter designations.",
            "The yarn label recommends which hook size to use for best results.",
            "Larger hooks create looser, more open fabric. Smaller hooks create tighter fabric.",
            "Ergonomic hooks with cushioned handles reduce hand fatigue during long sessions.",
            "As you advance, you will explore cotton yarn, bamboo, wool, and specialty fibers.",
            "Buy one skein of light-colored worsted yarn and the matching hook to start.",
            "Do not invest in a large yarn collection until you know what you enjoy making.",
            "The relationship between yarn weight and hook size is the most important concept.",
        ]),
        ("Chapter 3: Holding the Hook and Yarn", [
            "There are two common ways to hold a crochet hook: pencil grip and knife grip.",
            "Pencil grip holds the hook like you hold a pencil, with fingers near the middle.",
            "Knife grip holds the hook overhand like holding a dinner knife while cutting.",
            "Neither way is wrong. Try both and use whichever feels more comfortable to you.",
            "Hold the hook in your dominant hand. Your other hand controls the yarn tension.",
            "Yarn tension means how tightly you hold the yarn as it feeds through your fingers.",
            "Wrap the yarn over your index finger on your non-dominant hand.",
            "Let it flow between your middle and ring fingers for gentle tension control.",
            "Too tight tension makes stitches difficult to work into on the next row.",
            "Too loose tension creates floppy, uneven fabric without good structure.",
            "Practice holding both hook and yarn before making any stitches at all.",
            "Consistent tension comes with practice. Do not worry if it feels awkward initially.",
        ]),
        ("Chapter 4: Making a Slip Knot", [
            "Every crochet project begins with a slip knot on your hook.",
            "Make a loop with your yarn, leaving a six-inch tail hanging down.",
            "Reach through the loop and pull the working yarn (the long end) partially through.",
            "This creates an adjustable loop that tightens when you pull the tail.",
            "Slide this loop onto your crochet hook and tighten gently by pulling the tail.",
            "The knot should slide freely on the hook without being too tight or loose.",
            "The loop on your hook should be snug but able to slide back and forth easily.",
            "If the knot is too tight, start over. You will make many slip knots in your life.",
            "The slip knot does not count as a stitch in your pattern.",
            "Practice making slip knots until you can do it quickly and consistently.",
            "This simple knot is the starting point for every single crochet project.",
            "Once your slip knot is on the hook, you are ready to make your first chain.",
        ]),
        ("Chapter 5: Chain Stitch", [
            "The chain stitch is the foundation of almost every crochet project.",
            "With your slip knot on the hook, wrap the yarn over the hook from back to front.",
            "This motion is called a yarn over and you will do it constantly in crochet.",
            "Pull the yarn over through the loop already on your hook. That is one chain.",
            "Repeat: yarn over, pull through. Each time creates one more chain stitch.",
            "Your chain should look like a series of connected V shapes on the front.",
            "Practice making chains until they are even and consistent in size.",
            "Count your chains by counting each V shape, not including the loop on the hook.",
            "If your chains are too tight, use a hook one size larger for the chain only.",
            "Try to keep even tension. Chains should not be so tight they pucker.",
            "Make a chain of twenty stitches and check that they all look similar.",
            "The chain is your first real stitch. Master this before moving to the next chapter.",
        ]),
        ("Chapter 6: Single Crochet", [
            "Single crochet is the most basic and most used stitch in all of crochet.",
            "Start with a foundation chain of fifteen stitches for practice.",
            "Skip the first chain from the hook and insert your hook into the second chain.",
            "Yarn over and pull through the chain only. You now have two loops on your hook.",
            "Yarn over again and pull through both loops on the hook. One single crochet complete.",
            "Insert your hook into the next chain and repeat the same two steps.",
            "Continue across the entire chain making one single crochet in each stitch.",
            "At the end of the row, chain one and turn your work to the other side.",
            "For the next row, insert your hook under both loops of each stitch below.",
            "Single crochet creates a dense, tight fabric perfect for washcloths and amigurumi.",
            "Count your stitches at the end of each row. You should have the same number.",
            "Practice rows of single crochet until you can maintain consistent stitch count.",
        ]),
        ("Chapter 7: Double Crochet", [
            "Double crochet is taller than single crochet and works up faster.",
            "Start with a foundation chain. Yarn over before inserting into the stitch.",
            "Insert your hook into the fourth chain from the hook for the first double crochet.",
            "Yarn over and pull through the chain. You now have three loops on your hook.",
            "Yarn over and pull through the first two loops. Two loops remain on the hook.",
            "Yarn over and pull through the last two loops. One double crochet is complete.",
            "The yarn over before inserting is what makes this stitch taller than single crochet.",
            "At the end of a row, chain three and turn. The chain-three counts as a stitch.",
            "Skip the first stitch and double crochet into each stitch across the row.",
            "Double crochet creates an airier fabric great for blankets, scarves, and garments.",
            "This stitch uses more yarn than single crochet because of the extra height.",
            "Once you master double crochet, you can make blankets quickly and beautifully.",
        ]),
        ("Chapter 8: Half Double Crochet", [
            "Half double crochet is between single and double crochet in height.",
            "It creates a lovely textured fabric that is slightly stretchy.",
            "Yarn over, insert your hook into the third chain from the hook.",
            "Yarn over and pull through the chain. You have three loops on your hook.",
            "Yarn over and pull through all three loops at once. That is the key difference.",
            "For double crochet you pull through two at a time. Here you pull through all three.",
            "At the end of a row, chain two and turn. The chain-two counts as a stitch.",
            "Half double crochet creates a fabric thicker than double but less dense than single.",
            "It is a popular stitch for hats, baby blankets, and cozy scarves.",
            "The slightly different texture adds visual interest compared to other basic stitches.",
            "Practice a swatch of twenty stitches and ten rows to get comfortable.",
            "You now know the three most important crochet stitches used in most patterns.",
        ]),
        ("Chapter 9: Increasing and Decreasing", [
            "Increasing means adding stitches to make your fabric wider or to shape projects.",
            "To increase, simply make two stitches in the same stitch instead of one.",
            "This is used when making hats, amigurumi, and any shaped project.",
            "Decreasing means removing stitches to make your fabric narrower.",
            "For a single crochet decrease: insert hook in next stitch, yarn over and pull up.",
            "Insert hook in the following stitch, yarn over and pull up. Three loops on hook.",
            "Yarn over and pull through all three loops. Two stitches become one.",
            "Invisible decrease works the same but inserts under front loops only for neatness.",
            "Patterns tell you exactly where to increase and decrease with abbreviations.",
            "Increases and decreases are how flat circles, spheres, and shaped items are made.",
            "A flat circle starts with a ring and increases evenly each round.",
            "Practice making a flat circle to test your increasing skills before larger projects.",
        ]),
        ("Chapter 10: Reading Patterns", [
            "Crochet patterns use standard abbreviations that are the same worldwide.",
            "CH means chain, SC means single crochet, DC means double crochet.",
            "HDC means half double crochet, SL ST means slip stitch, SK means skip.",
            "INC means increase (two stitches in one), DEC means decrease.",
            "Numbers in parentheses at the end of a row show total stitch count.",
            "Asterisks mark sections that repeat: *SC 2, INC* means repeat that sequence.",
            "Patterns specify hook size, yarn weight, and finished dimensions.",
            "Gauge is how many stitches per inch your work measures with specific yarn and hook.",
            "Always check gauge before starting a project where size matters like garments.",
            "Patterns are written either in rows (flat pieces) or rounds (circular items).",
            "Read the entire pattern once before starting to understand the overall structure.",
            "Start with patterns rated beginner or easy until you build confidence.",
        ]),
        ("Chapter 11: Making a Granny Square", [
            "The granny square is the most iconic crochet motif and a must-learn project.",
            "Start with a magic ring or chain 4 and slip stitch to form a ring.",
            "Round 1: chain 3, make 2 double crochets into the ring, chain 2.",
            "Repeat three more times: 3 double crochets into ring, chain 2. Join with slip stitch.",
            "You now have four groups of three double crochets forming a square shape.",
            "Round 2: slip stitch to the chain-2 corner space.",
            "In each corner space work: 3 DC, chain 2, 3 DC. This creates the corner.",
            "Join at the end of the round with a slip stitch to the top of chain 3.",
            "Each subsequent round adds 3 DC groups in corners and along sides.",
            "Granny squares can be made any size by adding more rounds.",
            "Join multiple granny squares together to make blankets, bags, and cardigans.",
            "This versatile motif teaches you to work in rounds and read pattern structures.",
        ]),
        ("Chapter 12: Your First Scarf Project", [
            "A scarf is the perfect first project because it only uses rows of one stitch.",
            "Choose a soft medium weight yarn in a color you love for this project.",
            "Chain 25 stitches for a scarf approximately 5 inches wide when finished.",
            "Work in double crochet for a scarf that works up quickly and drapes nicely.",
            "Row 1: double crochet in the fourth chain from hook and each chain across.",
            "Row 2: chain 3, turn. Double crochet in each stitch across. Repeat this row.",
            "Continue until your scarf reaches approximately 60 inches long or desired length.",
            "Count your stitches at the end of every few rows to catch mistakes early.",
            "If you gain or lose stitches, you are likely missing the last stitch or adding extra.",
            "Add fringe by cutting yarn lengths and looping them through the short edges.",
            "Block your finished scarf by wetting it and pinning it flat to dry for even shape.",
            "Congratulations! You have completed your first wearable crochet project.",
        ]),
        ("Chapter 13: Your First Dishcloth Project", [
            "Dishcloths are quick, useful projects that make great gifts and practice pieces.",
            "Use 100 percent cotton yarn which is absorbent and machine washable.",
            "Sugar n Cream or Lily brand cotton yarn is perfect for dishcloths.",
            "Chain 30 stitches for an approximately 8-inch square dishcloth.",
            "Work entirely in single crochet for a dense, scrubby texture ideal for dishes.",
            "Row 1: single crochet in the second chain from hook and each chain across.",
            "Row 2: chain 1, turn. Single crochet in each stitch across. Repeat this row.",
            "Continue for about 30 rows until your piece is roughly square.",
            "Fasten off by cutting the yarn and pulling the tail through the last loop.",
            "Weave in your yarn tails using a yarn needle through nearby stitches.",
            "Try making dishcloths in different colors or add stripes for variety.",
            "A dishcloth takes only one to two hours and teaches you consistent tension.",
        ]),
        ("Chapter 14: Troubleshooting Common Mistakes", [
            "Edges are uneven: you are likely missing the first or last stitch of each row.",
            "Place a stitch marker in the first stitch of each row until the habit forms.",
            "Fabric is getting wider: you are accidentally adding extra stitches somewhere.",
            "Count stitches at the end of every row until counting becomes automatic.",
            "Fabric is curling: this is normal for single crochet. Blocking usually fixes it.",
            "Stitches are too tight: relax your grip and let the yarn flow more freely.",
            "Stitches are too loose: hold yarn slightly tighter between your tension fingers.",
            "Yarn is splitting: your hook is piercing the yarn. Insert into the whole stitch.",
            "Lost your place: use a stitch marker on the current stitch before setting down work.",
            "Holes in your fabric: you are skipping stitches. Insert hook under both loops.",
            "Most beginner mistakes are solved by counting stitches and maintaining tension.",
            "Every crocheter made these same mistakes. They are a normal part of learning.",
        ]),
        ("Chapter 15: Next Steps and Resources", [
            "You now know all the fundamental stitches needed for most crochet patterns.",
            "Next stitches to learn: treble crochet, shell stitch, and bobble stitch.",
            "YouTube has thousands of free crochet tutorials showing stitches in real time.",
            "Ravelry.com is a free community with hundreds of thousands of free patterns.",
            "Start with amigurumi (stuffed animals) if you enjoy small, quick projects.",
            "Try blankets if you want a relaxing, repetitive project for watching television.",
            "Join a local crochet group or online community for support and inspiration.",
            "Challenge yourself to learn one new stitch or technique each month.",
            "Keep a project journal noting what you made, yarn used, and lessons learned.",
            "Gift your practice pieces. Handmade items are treasured by people who love you.",
            "Crochet is a lifelong skill that reduces stress and creates beautiful items.",
            "You have everything you need to begin. Pick up your hook and start creating!",
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

    pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book66_How_To_Crochet.pdf')
    print("Book 66 created: Book66_How_To_Crochet.pdf")

if __name__ == '__main__':
    create_book()
