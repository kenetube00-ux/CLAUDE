#!/usr/bin/env python3
from pdf_utils import PDFDoc

pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"

# Page 1 - Title
pdf.new_page()
pdf.add_centered_text(520, "ARTICULATION PRACTICE BOOK", 'F2', 22)
pdf.add_centered_text(480, "S, R, L, TH Sound Worksheets", 'F4', 14)
pdf.add_centered_text(440, f"By {author}", 'F4', 12)
pdf.add_line(150, 420, 462, 420, 2)
pdf.add_centered_text(380, "For Parents & Speech-Language Pathologists", 'F1', 11, 0.3)

# Page 2 - How to Use
pdf.new_page()
pdf.add_centered_text(740, "HOW TO USE THIS BOOK", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 705, "FOR PARENTS:", 'F2', 11)
tips_parent = ["Practice 5-10 minutes daily (short & consistent wins!)",
               "Make it fun - use games, stickers, silly voices",
               "Model the correct sound - don't ask child to repeat wrong attempts",
               "Praise effort, not just accuracy",
               "Follow your SLP's guidance on which sounds to target"]
y = 685
for t in tips_parent:
    pdf.add_text(60, y, f"- {t}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-10, "FOR SLPs:", 'F2', 11)
y -= 28
tips_slp = ["Use for homework packets and structured practice",
            "Customize by highlighting target words for each child",
            "Track accuracy percentages on the home practice pages",
            "Send home with parent instructions for each sound"]
for t in tips_slp:
    pdf.add_text(60, y, f"- {t}", 'F1', 10)
    y -= 16
pdf.add_text(50, y-15, "SOUND POSITIONS:", 'F2', 11)
y -= 33
pdf.add_text(60, y, "Initial = beginning of word (sun)", 'F1', 10)
pdf.add_text(60, y-16, "Medial = middle of word (missing)", 'F1', 10)
pdf.add_text(60, y-32, "Final = end of word (bus)", 'F1', 10)

# Helper function for sound practice pages
def make_sound_pages(sound_name, initial_words, medial_words, final_words, sentences):
    # Page 1 - Initial position
    pdf.new_page()
    pdf.add_centered_text(740, f"/{sound_name}/ SOUND - INITIAL POSITION", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, f"Words that START with /{sound_name}/:", 'F2', 11)
    y = 690
    for i, w in enumerate(initial_words):
        col = 0 if i < 10 else 1
        x = 60 + col * 250
        row_y = y - (i % 10) * 20
        pdf.add_text(x, row_y, f"{i+1}. {w}", 'F1', 10)
    y -= 210
    pdf.add_text(50, y, "Sentences with initial /{}/: ".format(sound_name), 'F2', 10)
    y -= 18
    for s in sentences[:3]:
        pdf.add_text(60, y, s, 'F1', 9)
        y -= 16
    pdf.add_text(50, y-10, "Accuracy: ___/20 = ___%", 'F1', 10)
    
    # Page 2 - Medial position
    pdf.new_page()
    pdf.add_centered_text(740, f"/{sound_name}/ SOUND - MEDIAL POSITION", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, f"Words with /{sound_name}/ in the MIDDLE:", 'F2', 11)
    y = 690
    for i, w in enumerate(medial_words):
        col = 0 if i < 10 else 1
        x = 60 + col * 250
        row_y = y - (i % 10) * 20
        pdf.add_text(x, row_y, f"{i+1}. {w}", 'F1', 10)
    y -= 210
    pdf.add_text(50, y, "Sentences with medial /{}/:".format(sound_name), 'F2', 10)
    y -= 18
    for s in sentences[3:6]:
        pdf.add_text(60, y, s, 'F1', 9)
        y -= 16
    pdf.add_text(50, y-10, "Accuracy: ___/20 = ___%", 'F1', 10)
    
    # Page 3 - Final position
    pdf.new_page()
    pdf.add_centered_text(740, f"/{sound_name}/ SOUND - FINAL POSITION", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 710, f"Words that END with /{sound_name}/:", 'F2', 11)
    y = 690
    for i, w in enumerate(final_words):
        col = 0 if i < 10 else 1
        x = 60 + col * 250
        row_y = y - (i % 10) * 20
        pdf.add_text(x, row_y, f"{i+1}. {w}", 'F1', 10)
    y -= 210
    pdf.add_text(50, y, "Sentences with final /{}/:".format(sound_name), 'F2', 10)
    y -= 18
    for s in sentences[6:9]:
        pdf.add_text(60, y, s, 'F1', 9)
        y -= 16
    pdf.add_text(50, y-10, "Accuracy: ___/20 = ___%", 'F1', 10)


# /S/ sound pages (3 pages)
make_sound_pages("S",
    ["sun", "soap", "sock", "sand", "sea", "sit", "six", "sad", "seal", "saw",
     "send", "sink", "sing", "sip", "seed", "soft", "soup", "sail", "safe", "sign"],
    ["missing", "messy", "biscuit", "basket", "pencil", "castle", "dinosaur", "eraser",
     "inside", "lesson", "muscle", "faucet", "bossy", "fossil", "bicycle", "icing",
     "iceberg", "officer", "passing", "racing"],
    ["bus", "yes", "house", "mouse", "dress", "glass", "grass", "face", "rice", "ice",
     "juice", "pass", "miss", "goose", "moose", "horse", "nurse", "purse", "kiss", "peace"],
    ["The sun is setting over the sea.", "She saw six socks on the sand.",
     "Sam sips his soup slowly.", "The messy pencil case is missing.",
     "The dinosaur fossil is inside the basket.", "My bicycle needs a new faucet.",
     "The bus passes the glass house.", "The mouse ate rice and juice.",
     "I miss my horse and goose."])

# /R/ sound pages (3 pages)
make_sound_pages("R",
    ["red", "run", "rain", "read", "rock", "ring", "road", "rope", "roof", "rug",
     "race", "rip", "rest", "rich", "ride", "roll", "room", "rose", "round", "rush"],
    ["carrot", "berry", "mirror", "parrot", "arrow", "cherry", "fairy", "pirate",
     "forest", "orange", "garage", "cereal", "zero", "giraffe", "barrel", "starry",
     "hurry", "sorry", "story", "carry"],
    ["car", "star", "door", "four", "bear", "hair", "chair", "fire", "far", "jar",
     "deer", "year", "near", "stir", "fur", "her", "sir", "roar", "store", "more"],
    ["The red rose grows in the rain.", "Run around the road and rest.",
     "The ring rolled off the roof.", "The carrot and cherry are in the mirror.",
     "The pirate carries oranges through the forest.", "The parrot tells a story in a hurry.",
     "The car is far from the star.", "Four deer are near the door.",
     "Her chair is by the fire."])

# /L/ sound pages (3 pages)
make_sound_pages("L",
    ["lamp", "leaf", "lion", "lake", "leg", "lemon", "letter", "lip", "lid", "log",
     "lock", "love", "lunch", "lizard", "ladder", "laugh", "lawn", "light", "line", "look"],
    ["balloon", "jelly", "pillow", "yellow", "hello", "dollar", "color", "tulip",
     "melon", "salad", "island", "violin", "olive", "palace", "pilot", "silly",
     "valley", "follow", "belong", "bowling"],
    ["ball", "bell", "doll", "hill", "mail", "nail", "pail", "pool", "school", "tall",
     "wall", "wheel", "cool", "seal", "meal", "feel", "full", "pull", "smile", "trail"],
    ["The lion loves lemon for lunch.", "Look at the lamp by the lake.",
     "The lizard laughed on the log.", "The yellow balloon is on the pillow.",
     "A silly pilot plays the violin.", "Hello, follow me to the palace.",
     "The ball rolled down the tall hill.", "I feel cool in the pool at school.",
     "The seal had a full meal."])

# /TH/ sound pages (3 pages)
make_sound_pages("TH",
    ["think", "three", "thumb", "thick", "thin", "throw", "thank", "thirsty", "thunder",
     "Thursday", "theater", "theme", "thing", "thorn", "thought", "thousand", "thread",
     "throne", "thud", "thermometer"],
    ["birthday", "bathtub", "toothbrush", "something", "nothing", "anything",
     "bathroom", "pathway", "python", "athlete", "author", "method", "marathon",
     "sympathy", "mathlete", "panther", "healthy", "wealthy", "stethoscope", "lethal"],
    ["bath", "math", "tooth", "both", "cloth", "health", "month", "mouth", "north",
     "south", "path", "growth", "earth", "birth", "worth", "teeth", "breath", "beneath",
     "wreath", "faith"],
    ["I think three things on Thursday.", "Thank the thirsty theater group.",
     "Throw the thick thread on the throne.", "My birthday bathtub has a toothbrush.",
     "The athlete does something in the bathroom.", "The python author has sympathy.",
     "Both teeth need a bath this month.", "The path to the north has growth.",
     "Beneath the earth is worth the faith."])

# /SH/ sound pages (3 pages)
make_sound_pages("SH",
    ["ship", "shoe", "shop", "sheep", "shell", "shark", "shirt", "shine", "shake",
     "shape", "share", "shelf", "sheet", "shed", "shift", "shadow", "shower", "shut",
     "shout", "shoulder"],
    ["fishing", "washing", "pushing", "sunshine", "mushroom", "cashew", "fashion",
     "cushion", "ocean", "machine", "tissue", "nation", "mission", "position",
     "lotion", "vacation", "motion", "station", "action", "caution"],
    ["fish", "dish", "wish", "brush", "crash", "trash", "wash", "push", "rush", "bush",
     "flash", "fresh", "splash", "squash", "leash", "finish", "vanish", "polish",
     "radish", "publish"],
    ["The ship has a shiny shell.", "Shake the shoe and share it.",
     "The shark swims in the shadow.", "We are fishing in the sunshine.",
     "The mushroom fashion is a cushion.", "Washing the machine on vacation.",
     "I wish to finish the fresh dish.", "Push the brush and polish the trash.",
     "The fish vanish in a flash splash."])

# /CH/ sound pages (3 pages)
make_sound_pages("CH",
    ["chair", "cheese", "cherry", "chicken", "child", "chin", "chip", "chocolate",
     "chop", "church", "chain", "chalk", "chance", "change", "chapter", "charge",
     "charm", "chase", "cheap", "check"],
    ["teacher", "kitchen", "ketchup", "catcher", "butcher", "richer", "pitcher",
     "orchard", "fortune", "nature", "picture", "culture", "furniture", "adventure",
     "feature", "capture", "creature", "mixture", "sculpture", "temperature"],
    ["beach", "peach", "teach", "reach", "coach", "poach", "each", "much", "such",
     "touch", "couch", "lunch", "bunch", "ranch", "branch", "crunch", "match", "watch",
     "catch", "stretch"],
    ["The child chose chocolate and cheese.", "Chase the chicken to the church.",
     "Check the chalk and change chapters.", "The teacher is in the kitchen.",
     "The catcher has ketchup on the picture.", "The creature in nature is a feature.",
     "Reach the beach and teach each one.", "Touch the couch and munch on lunch.",
     "Watch the match at the ranch."])


# Pages 21-23 - Mixed Sounds Practice (3 pages)
for pg in range(3):
    pdf.new_page()
    pdf.add_centered_text(740, f"MIXED SOUNDS PRACTICE - {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    if pg == 0:
        pdf.add_text(50, 710, "Read these sentences. Circle your target sound words:", 'F2', 10)
        mixed_sent = [
            "The red ship sailed south on Thursday.",
            "She shared three shells with the children.",
            "The teacher ran to the beach to chase the shark.",
            "Look at the shiny star on the church roof.",
            "The lion catches fish near the tall lighthouse.",
            "Charlie threw the ball to the silly seal.",
            "Rachel brushed her teeth before lunch.",
            "The cheerful sheep sat on a chair by the shore.",
        ]
        y = 688
        for s in mixed_sent:
            pdf.add_text(60, y, s, 'F1', 10)
            y -= 22
    else:
        pdf.add_text(50, 710, "MINIMAL PAIRS PRACTICE:" if pg == 1 else "CARRY-OVER READING:", 'F2', 11)
        y = 688
        if pg == 1:
            pairs = [("sun/fun", "sick/thick", "sin/shin", "sip/ship"),
                     ("red/led", "right/light", "race/lace", "raw/law"),
                     ("three/free", "thin/fin", "thought/fought", "thank/tank"),
                     ("chop/shop", "chip/ship", "chair/share", "chew/shoe")]
            for pair_group in pairs:
                for p in pair_group:
                    pdf.add_text(60, y, p, 'F3', 10)
                    y -= 18
                y -= 10
        else:
            pdf.add_text(50, 688, "Read this passage aloud. Focus on clear pronunciation:", 'F1', 10)
            passage = [
                "Last Thursday, Sarah and Charlie went to the beach.",
                "The sunshine was bright and the shore was beautiful.",
                "They searched for shells and watched three ships sail south.",
                "A cheerful seal splashed in the shallow water.",
                "Charlie threw a ball and the seal caught it with a splash!",
                "Sarah shared her lunch - cheese sandwiches and cherries.",
                "They sat on their chairs and told each other stories.",
                "What a thrilling adventure at the shore!",
            ]
            y = 666
            for line in passage:
                pdf.add_text(60, y, line, 'F4', 10)
                y -= 22
            pdf.add_text(50, y-10, "Sounds I need to work on in this passage:", 'F1', 10)
            pdf.add_line(50, y-28, 540, y-28, 0.5, 0.7)

# Pages 24-28 - Home Practice Schedule (5 pages)
for pg in range(5):
    pdf.new_page()
    pdf.add_centered_text(740, f"HOME PRACTICE LOG - WEEK {pg+1}", 'F2', 14)
    pdf.add_line(50, 730, 562, 730, 1)
    pdf.add_text(50, 715, "Child: _________________  Target sound: ___  Position: ________", 'F1', 9)
    y = 695
    pdf.add_text(50, y, "Date", 'F2', 8)
    pdf.add_text(100, y, "Sound", 'F2', 8)
    pdf.add_text(145, y, "Words Practiced", 'F2', 8)
    pdf.add_text(330, y, "Accuracy", 'F2', 8)
    pdf.add_text(400, y, "Time", 'F2', 8)
    pdf.add_text(450, y, "Parent Init", 'F2', 8)
    y -= 5
    pdf.add_line(50, y, 562, y, 0.5)
    y -= 15
    for i in range(28):
        pdf.add_line(50, y, 95, y, 0.3, 0.7)
        pdf.add_line(100, y, 140, y, 0.3, 0.7)
        pdf.add_line(145, y, 325, y, 0.3, 0.7)
        pdf.add_line(330, y, 392, y, 0.3, 0.7)
        pdf.add_line(400, y, 445, y, 0.3, 0.7)
        pdf.add_line(450, y, 530, y, 0.3, 0.7)
        y -= 15
    pdf.add_text(50, y-5, "SLP Notes: _______________________________________________", 'F1', 8)

# Pages 29-30 - Progress Celebration + Notes
pdf.new_page()
pdf.add_centered_text(740, "PROGRESS CELEBRATION!", 'F2', 16)
pdf.add_line(50, 730, 562, 730, 1)
pdf.add_text(50, 710, "Color in a star for each sound mastered!", 'F1', 11)
sounds_all = ["/S/ initial", "/S/ medial", "/S/ final",
              "/R/ initial", "/R/ medial", "/R/ final",
              "/L/ initial", "/L/ medial", "/L/ final",
              "/TH/ initial", "/TH/ medial", "/TH/ final",
              "/SH/ initial", "/SH/ medial", "/SH/ final",
              "/CH/ initial", "/CH/ medial", "/CH/ final"]
y = 688
for s in sounds_all:
    pdf.add_text(60, y, s, 'F1', 10)
    pdf.add_text(200, y, "Date mastered: ________", 'F1', 9)
    pdf.add_text(370, y, "Accuracy: ___%", 'F1', 9)
    y -= 20

pdf.new_page()
pdf.add_centered_text(740, "NOTES & GOALS", 'F2', 14)
pdf.add_line(50, 730, 562, 730, 1)
y = 710
for i in range(28):
    pdf.add_line(50, y, 562, y, 0.5, 0.7)
    y -= 22

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book190_Articulation_Practice_Book.pdf')
print("Book190_Articulation_Practice_Book.pdf created successfully!")
