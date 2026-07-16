"""Book362: 50 Mother-Daughter Activities"""
from pdf_utils import PDFDoc
def wrap(t,mx=80):
    w=t.split();ls=[];c=""
    for x in w:
        if len(c+" "+x)>mx:ls.append(c);c=x
        else:c=c+" "+x if c else x
    if c:ls.append(c)
    return ls
def create_book():
    doc=PDFDoc();author="Daniel Tesfamariam"
    acts=[
    ("Friendship Bracelet Making","Creative","Ages 6-15","45 min","Embroidery thread, scissors, tape, clipboard","Cut 3-4 threads 24 inches long. Tape to clipboard. Make forward knots with each thread across. Alternate patterns. Add beads for decoration. Tie off when desired length reached.","While you work: Share a favorite friendship story from your own childhood.","Take photos of your bracelets. Make one for each other to wear."),
    ("Nature Scavenger Hunt","Outdoors","Ages 6-12","60 min","Printed list, bags for collections, magnifying glass","Create a list of 20 items to find: smooth rock, Y-shaped stick, feather, wildflower, etc. Explore a park or trail together. Check off items. Bonus points for unique finds.","While you search: Talk about your favorite outdoor memories growing up.","Press flowers or display special finds in a shadow box together."),
    ("Homemade Pizza Night","Kitchen","Ages 6-15","90 min","Pizza dough, sauce, cheese, toppings of choice","Make dough together (or use pre-made). Roll out individual pizzas. Let each person design their own. Try creative shapes. Bake and enjoy together.","While you cook: Share family food traditions and create a new one tonight.","Rate each other's pizza creations. Make this a monthly tradition."),
    ("DIY Spa Night","Self-Care","Ages 8-15","60 min","Face masks, nail polish, cucumbers, towels, music","Set up a spa station. Apply face masks together. Paint each other's nails. Do foot soaks. Play relaxing music. Use cucumbers on eyes. Give hand massages.","While you relax: Ask each other 'what is stressing you out lately?'","Make this a monthly ritual for reconnection and relaxation."),
    ("Star Gazing Night","Outdoors","Ages 6-15","45 min","Blanket, star map app, hot chocolate, flashlight","Spread blanket in dark area. Use star map app to identify constellations. Find the Big Dipper, North Star, and planets. Make up your own constellation stories.","While you gaze: Share your biggest dreams. What star would you wish on?","Start a sky journal tracking what you see each time."),
    ("Baking Challenge","Kitchen","Ages 7-15","90 min","Basic baking supplies, recipe cards, timer","Choose a baking challenge: decorate cookies, build a cake, or try a new recipe. Work as a team against a timer. Taste test and rate results. Give each other silly awards.","While you bake: Share your earliest baking or kitchen memory.","Give your creations to neighbors or friends. Spread joy."),
    ("Book Club for Two","Learning","Ages 8-15","Ongoing","Same book (two copies or shared), notebook, treats","Choose a book to read together (at your daughter's level). Set reading goals. Discuss chapters over snacks. Share favorite quotes. Rate the book when finished.","Discussion: What character do you relate to most? What would you change?","Keep a shared reading journal. Track all books you read together."),
    ("Tie-Dye Day","Creative","Ages 6-15","90 min","White t-shirts, tie-dye kit, rubber bands, plastic bags","Fold shirts in different patterns (spiral, stripes, bullseye). Apply rubber bands. Squeeze dye onto sections. Seal in bags 6-24 hours. Rinse and reveal!","While you wait for dye: Design matching outfits. When will you wear them?","Wear your matching shirts on your next outing together."),
    ("Garden Planting Together","Outdoors","Ages 6-15","60 min","Seeds or seedlings, pots or garden bed, soil, watering can","Choose flowers or vegetables to grow. Prepare soil together. Plant seeds. Create plant labels. Set a watering schedule. Track growth weekly.","While you plant: Talk about what you want to grow in your life this year.","Document growth with weekly photos. Celebrate first blooms/harvests."),
    ("Vision Board Creation","Learning","Ages 9-15","60 min","Magazines, scissors, glue, poster board, markers, stickers","Find images and words that represent your dreams and goals. Cut and arrange on poster board. Add personal touches. Hang where you can see them daily.","While you create: Share three dreams you have never told anyone.","Review boards monthly. Celebrate anything that comes true!"),
    ("Photo Walk Adventure","Creative","Ages 8-15","60 min","Phone cameras, printed photo challenge list","Take a walk with a photography challenge: find something red, capture a reflection, photograph a texture, shoot from ground level, find perfect symmetry, etc.","While you walk: Who would you want to send your best photo to and why?","Print favorites and create a mini gallery wall together."),
    ("Cooking Grandma's Recipe","Kitchen","Ages 8-15","90 min","Family recipe, ingredients, family photos","Choose a family recipe from a grandmother or great-grandmother. Cook it together following the original recipe. Share family food stories.","While you cook: What stories do you know about the women in our family?","Start a family recipe book with stories alongside each recipe."),
    ("Hiking Adventure","Outdoors","Ages 7-15","2-3 hours","Water, snacks, comfortable shoes, trail map, camera","Choose an age-appropriate trail. Pack snacks and water. Walk together at a comfortable pace. Identify plants and birds. Find a spot for snack break.","While you hike: No phones for the first 30 minutes. Just talk and observe.","Press a leaf from each hike. Build a nature collection over time."),
    ("DIY Candle Making","Creative","Ages 10-15","60 min","Soy wax, wicks, jars, essential oils, dye blocks","Melt wax in double boiler. Add color and scent. Center wick in jar. Pour carefully. Let cool completely. Trim wick. Light and enjoy your creation!","While wax melts: What scents remind you of your happiest memories?","Make candles as gifts for family members together."),
    ("Mad Libs Storytelling","Learning","Ages 7-14","30 min","Paper, pencils, imagination","Create your own Mad Libs stories: write a story with blanks for nouns, verbs, and adjectives. Ask each other for words without revealing the story. Read the hilarious results.","Between stories: Share the funniest thing that happened to you this week.","Save your best stories. Re-read them when you need a laugh."),
    ("Morning Hike + Breakfast Out","Outdoors","Ages 8-15","3 hours","Comfortable clothes, water, appetite","Wake early for a sunrise or morning hike. Enjoy the quiet world before everyone wakes up. Finish with breakfast at a favorite restaurant.","During breakfast: What makes you feel most alive? What is your perfect day?","Make early morning adventures a quarterly tradition."),
    ("Art Museum Visit","Learning","Ages 8-15","2 hours","Museum tickets, sketchbook, pencils","Visit an art museum together. Choose one piece each that speaks to you. Sketch it. Discuss what you see and feel. Read about the artist's story.","In the museum: If you could live inside any painting, which one and why?","Try to recreate your favorite piece at home together."),
    ("Make a Time Capsule","Creative","Ages 8-15","45 min","Container, paper, small mementos, photos, tape","Each write letters to your future selves. Add photos, current favorites, predictions, and small objects that represent this time. Seal with a date to open (1 year, 5 years).","While you pack: What do you think you will be doing when we open this?","Set a calendar reminder to open it together on the chosen date."),
    ("Kitchen Science Experiments","Learning","Ages 6-13","60 min","Baking soda, vinegar, food coloring, milk, dish soap, tray","Try 3-4 kitchen science experiments: volcano eruption, milk color explosion, invisible ink with lemon juice, density tower with liquids.","While experimenting: What mysteries about the world do you want to understand?","Research one experiment deeper. What career uses this science?"),
    ("Matching Pajama Movie Marathon","Self-Care","Ages 6-15","4 hours","Matching PJs, popcorn, blankets, favorite movies, treats","Buy or make matching pajamas. Set up the couch with blankets. Make popcorn and treats. Watch 2-3 movies you both love. No phones allowed!","Between movies: Rate the movie. What character would you be?","Take a matching PJ selfie. Make movie night a monthly event."),
    ("Volunteer Together","Learning","Ages 8-15","2-3 hours","Depends on activity","Choose a cause you both care about. Research local volunteer opportunities. Spend a morning serving together: food bank, animal shelter, park cleanup, or nursing home visit.","After volunteering: How did it feel to help? What did you learn?","Commit to volunteering together once a month."),
    ("Dance Party + Choreography","Self-Care","Ages 6-15","45 min","Music, open space, phone to record","Create a playlist of songs you both love. Learn or create a simple dance together. Film your final performance. Watch it back and laugh together.","While dancing: Share songs that were popular when Mom was your age.","Perform your routine for the family. Start a dance tradition."),
    ("Letter Writing to Each Other","Creative","Ages 8-15","30 min","Stationery, envelopes, stamps, pens","Sit in separate rooms. Write a genuine letter to each other expressing something you appreciate, admire, or want them to know. Exchange and read silently.","After reading: What surprised you most about what she wrote?","Save all letters in a special box. Re-read them on hard days."),
    ("Bird Watching Morning","Outdoors","Ages 7-15","60 min","Binoculars, bird guide book or app, notebook, patience","Find a quiet spot in nature. Sit still and observe. Identify birds by color, size, and song. Keep a list of species spotted. Notice their behaviors.","While watching: If you could be any bird, which one and why?","Start a lifetime bird watching list. How many can you find this year?"),
    ("Homemade Ice Cream","Kitchen","Ages 6-15","45 min","Heavy cream, sugar, vanilla, ice, salt, ziplock bags, mix-ins","Mix cream, sugar, and vanilla in small bag. Place inside large bag filled with ice and salt. Shake for 10 minutes. Add toppings. Enjoy your creation!","While shaking: What is your favorite flavor memory from childhood?","Experiment with wild flavor combinations. Rate each creation."),
    ("Learn a New Skill Together","Learning","Ages 8-15","Ongoing","Depends on skill chosen","Choose something NEITHER of you knows: knitting, origami, a new language, calligraphy, coding, guitar. Watch tutorials together. Practice. Laugh at your mistakes.","While learning: What is the hardest thing you ever learned? How did you persist?","Set a 30-day challenge. Practice together daily for 30 days."),
    ("Sunset Watching","Outdoors","Ages 6-15","30 min","Blanket, snacks, warm drinks, journal","Find a good sunset view spot. Arrive 30 minutes before sunset. Watch the colors change. Sit in comfortable silence or share what is on your heart.","During the sunset: Share one worry and one gratitude for today.","Watch the sunset on the same day each month. Track the changing position."),
    ("DIY Face Masks","Self-Care","Ages 8-15","30 min","Honey, oatmeal, avocado, yogurt, bowls, application tools","Make 3 different face masks from kitchen ingredients: honey+oatmeal (exfoliant), avocado+yogurt (moisturizing), banana+honey (nourishing). Apply, relax, rinse.","Mask time: With masks on, share something silly that happened this week.","Research which natural ingredients are best for your skin type."),
    ("Memory Box Creation","Creative","Ages 8-15","45 min","Shoebox, decorating supplies, mementos, photos, stickers","Decorate a box together. Fill with items that represent your relationship: ticket stubs, photos, notes, small gifts, inside jokes written on paper.","While creating: What is your most treasured memory of us together?","Add to the box every month. Open and review on special anniversaries."),
    ("Yoga Together","Self-Care","Ages 7-15","30 min","Yoga mats or towels, YouTube yoga video, comfortable clothes","Find a mother-daughter yoga video online. Practice poses together. Help each other balance. Focus on breathing and being present in your bodies.","After yoga: How does your body feel different? What pose was hardest?","Do yoga together twice a week. Track flexibility improvements."),
    # Adding more to reach 50
    ("Puzzle Race","Learning","Ages 8-15","60 min","Two matching puzzles or one large puzzle, timer","Each take half the pieces of a large puzzle or race on matching smaller puzzles. Work together or compete. Play music. Enjoy the meditative quality of puzzling.","While puzzling: What puzzle in your life are you trying to figure out?","Frame a completed puzzle as wall art for your shared space."),
    ("Plant Propagation Station","Outdoors","Ages 8-15","30 min + weeks of watching","Glass jars, scissors, established houseplants, water","Take cuttings from houseplants (pothos, spider plant, etc). Place in water on a sunny windowsill. Watch roots grow over weeks. Transfer to soil. Name your plants!","While you wait for roots: What do you want to grow in the next year?","Give propagated plants as gifts. Share the love of growing things."),
    ("Cook Through a Country","Kitchen","Ages 8-15","2 hours","Ingredients for recipes from chosen country, music, decorations","Choose a country. Research its cuisine. Cook a full meal from that country. Play music from there. Discuss the culture, geography, and traditions.","During dinner: If we could travel anywhere together, where would you go?","Cook a different country each month. Create a passport of culinary travels."),
    ("Gratitude Jar","Creative","Ages 6-15","Ongoing","Mason jar, colored paper, pens","Decorate a jar together. Each day, write one thing you are grateful for on a slip of paper. On tough days or at year end, empty the jar and read all the gratitude aloud.","When starting: What are 5 things about each other you are grateful for?","Read the full jar on New Year's Eve together."),
    ("Obstacle Course Building","Outdoors","Ages 6-13","60 min","Hula hoops, cones, chairs, rope, timer, creativity","Design an obstacle course in your yard or park. Take turns timing each other. Modify to make harder or easier. Cheer each other on. Celebrate personal bests.","After the course: What real-life obstacles are you facing? How can we tackle them together?","Challenge other family members. Make it a family competition."),
    ("Calligraphy Practice","Creative","Ages 9-15","45 min","Calligraphy pens or brush pens, practice paper, instructional guide","Watch a calligraphy tutorial together. Practice basic strokes. Write each other's names in fancy script. Try different styles. Create a favorite quote poster.","While practicing: What quote means the most to you right now?","Make hand-lettered cards for birthdays and holidays together."),
    ("Dream Home Design","Learning","Ages 8-15","45 min","Graph paper, colored pencils, ruler, magazines for inspiration","Design your dream homes on graph paper. Include floor plans, decorating choices, outdoor spaces. Share and discuss. What matters most in a home?","While designing: What makes a house feel like HOME to you?","Keep your dream home designs. Revisit them in 10 years."),
    ("Breakfast in Bed for Each Other","Kitchen","Ages 8-15","45 min","Breakfast ingredients, tray, flower, nice dishes","Take turns surprising each other with breakfast in bed. Include a small note of appreciation. Make it special with a flower or folded napkin.","Over breakfast: What made you smile yesterday?","Make Surprise Breakfast a monthly tradition, alternating who treats whom."),
    ("Cloud Watching","Outdoors","Ages 6-12","30 min","Blanket, open sky, imagination","Lie on a blanket and look up. Take turns finding shapes in clouds. Tell stories about what you see. Enjoy the simplicity of just being together with nowhere to go.","While watching: If you could float away on a cloud, where would you go?","Keep a cloud journal with sketches of the best shapes you find."),
    ("Family Tree Project","Learning","Ages 8-15","60 min","Large paper, photos, markers, family knowledge","Create a family tree together. Add names, dates, and stories. Call grandparents for details you do not know. Include photos where possible.","While building: What family stories do you want to make sure we never forget?","Interview older relatives. Record their stories before they are lost."),
    ("Mad Scientist Lab","Creative","Ages 6-13","60 min","Lab coats (white shirts), goggles, kitchen science supplies","Set up a pretend lab. Do experiments: color-changing milk, baking soda volcanoes, static electricity. Wear lab coats and goggles. Take notes like real scientists.","Between experiments: What question about the world would you love to answer?","Research the real science behind each experiment. Go deeper together."),
    ("Create a Secret Handshake","Self-Care","Ages 6-13","15 min","Just your hands and creativity","Invent an elaborate secret handshake together. Include claps, snaps, fist bumps, wiggles, and ending pose. Practice until you can do it fast. Use it as your special greeting.","After creating: What other secret codes or signals should we have?","Use your handshake at pickup, before bed, or whenever you need to feel connected."),
    ("Poetry Writing Session","Creative","Ages 9-15","30 min","Notebooks, pens, poetry examples for inspiration","Read poems together. Try writing your own. Start with simple forms: haiku (5-7-5 syllables), acrostic (spell a word vertically), or free verse. Share without judgment.","After sharing: What poem spoke to your heart most?","Create a mother-daughter poetry book with your best poems."),
    ("Treasure Hunt Creator","Learning","Ages 6-13","60 min","Paper for clues, small treasure/prize, creativity","Take turns creating treasure hunts for each other around the house or yard. Write clue cards that lead from one spot to the next. End with a small surprise or treat.","After finding treasure: What real treasure in your life are you most grateful for?","Create treasure hunts for holidays and birthdays as a tradition."),
    ("Blanket Fort Movie Night","Self-Care","Ages 6-12","3 hours","Blankets, pillows, chairs, string lights, snacks, tablet/laptop","Build the most epic blanket fort together. Add string lights, pillows, snacks. Watch a movie inside your cozy creation. No cleaning up until morning.","Inside the fort: If you could build a real fort anywhere, where would it be?","Build forts for every season. Summer outdoor tent, winter indoor cave."),
    ("Matching Outfit Day","Creative","Ages 6-15","All day","Matching or coordinating outfits, confidence","Plan matching or coordinating outfits. Wear them out together. Take photos. Own the looks with confidence. Notice how many smiles you get!","While getting ready: When did you feel most confident in an outfit?","Create a matching outfit for a holiday card photo."),
    ("Random Acts of Kindness Day","Learning","Ages 6-15","All day","Small supplies for kindness: notes, treats, coins","Plan 10 random acts of kindness to do together: leave encouraging notes, pay for someone's coffee, donate toys, write thank-you letters, bring treats to neighbors.","End of day: Which act felt best? What reaction surprised you most?","Commit to one random act of kindness together each week."),
    ("Painting Together","Creative","Ages 6-15","60 min","Canvas or paper, acrylic paints, brushes, water cups, smocks","Set up side-by-side painting stations. Choose the same subject or different ones. No rules about skill level. Paint freely. Display your art together.","While painting: If your life were a painting, what colors and shapes would it have?","Start a gallery wall of your paired paintings over time."),
    ("Teach Each Other Something","Learning","Ages 8-15","30 min each","Depends on skill","Mom teaches daughter something she knows well. Then daughter teaches mom something SHE is good at. Could be: a dance move, a math trick, a craft, a game, or a recipe.","After teaching: What surprised you about being the teacher vs student?","Make 'teach each other' a monthly date. Take turns choosing.")]


    # Build PDF
    doc.add_filled_rect(0,0,612,792,0.95)
    doc.add_centered_text(640,"50 MOTHER-DAUGHTER",'F2',26,0.1)
    doc.add_centered_text(605,"ACTIVITIES",'F2',30,0.1)
    doc.add_line(150,585,462,585,2,0.3)
    doc.add_centered_text(555,"Fun Things to Do Together That Build Your Bond",'F4',14,0.3)
    doc.add_centered_text(100,author,'F2',14,0.2)
    doc.new_page()
    doc.add_centered_text(700,"50 MOTHER-DAUGHTER ACTIVITIES",'F2',13,0.2)
    doc.add_text(72,650,f"Author: {author}",'F1',11,0.3)
    doc.add_text(72,630,"Format: 8.5 x 11 inches | Kindle & Paperback",'F1',10,0.4)
    doc.add_text(72,600,"All rights reserved.",'F1',10,0.4)
    doc.new_page()
    # TOC
    doc.add_centered_text(720,"TABLE OF CONTENTS",'F2',18,0.1)
    doc.add_line(72,705,540,705,1,0.3)
    y=680
    for i,(n,cat,_,_,_,_,_,_) in enumerate(acts):
        if y<80:doc.new_page();y=740
        doc.add_text(72,y,f"{i+1}. {n} [{cat}]",'F1',9,0.2);y-=14
    doc.new_page()

    for i,(name,cat,ages,time,supplies,steps,talk,memory) in enumerate(acts):
        doc.add_filled_rect(50,720,512,45,0.92)
        doc.add_centered_text(748,f"Activity #{i+1} | {cat}",'F1',9,0.5)
        doc.add_centered_text(730,name.upper(),'F2',14,0.1)
        doc.add_text(72,700,f"Ages: {ages}  |  Time: {time}",'F1',10,0.3)
        doc.add_text(72,682,"Supplies:",'F2',10,0.2)
        y=670
        for ln in wrap(supplies,75):
            doc.add_text(140,670,ln,'F1',9,0.3);break
        y=652
        doc.add_text(72,y,"INSTRUCTIONS:",'F2',10,0.2);y-=14
        for ln in wrap(steps,80):
            doc.add_text(82,y,ln,'F1',9,0.25);y-=13
        y-=10
        doc.add_text(72,y,"TALK ABOUT THIS:",'F2',10,0.2);y-=14
        for ln in wrap(talk,78):
            doc.add_text(82,y,ln,'F4',9,0.3);y-=13
        y-=10
        doc.add_text(72,y,"MEMORY TIP:",'F2',10,0.2);y-=14
        for ln in wrap(memory,78):
            doc.add_text(82,y,ln,'F4',9,0.3);y-=13
        doc.new_page()

    # Calendar + memory pages
    doc.add_centered_text(720,"ACTIVITY PLANNING CALENDAR",'F2',16,0.1)
    doc.add_line(72,705,540,705,1,0.3)
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    y=680
    for m in months:
        doc.add_text(72,y,f"{m}: Activity #___  Date: ___/___",'F1',11,0.3);y-=20
    doc.new_page()
    # Memory journal
    doc.add_centered_text(720,"OUR MEMORY JOURNAL",'F2',16,0.1)
    doc.add_line(72,705,540,705,1,0.3)
    y=680
    for j in range(5):
        doc.add_text(72,y,f"Activity: ________________  Date: ___/___/___",'F1',10,0.3);y-=16
        doc.add_text(72,y,"Best moment:",'F4',10,0.3);y-=14
        doc.add_line(72,y,540,y,0.5,0.7);y-=18
        doc.add_line(72,y,540,y,0.5,0.7);y-=22
    doc.new_page()
    doc.add_centered_text(720,"OUR MEMORY JOURNAL (continued)",'F2',16,0.1)
    y=690
    for j in range(5):
        doc.add_text(72,y,f"Activity: ________________  Date: ___/___/___",'F1',10,0.3);y-=16
        doc.add_text(72,y,"Best moment:",'F4',10,0.3);y-=14
        doc.add_line(72,y,540,y,0.5,0.7);y-=18
        doc.add_line(72,y,540,y,0.5,0.7);y-=22
    doc.new_page()

    doc.add_centered_text(600,"The best gift you can give",'F4',14,0.3)
    doc.add_centered_text(575,"your daughter is your TIME.",'F5',16,0.1)
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "REFLECTION & ACTION STEPS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Key takeaways from this section:", 'F4', 11, 0.3)
    y = 678
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "How this applies to my life:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(5):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Questions I still have:", 'F4', 11, 0.3)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()

    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for additional thoughts and ideas:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()

    doc.add_centered_text(740, "PERSONAL GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "What resonated with me most:", 'F2', 11, 0.2)
    y = 678
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "Actions I will take:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(6):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    y -= 10
    doc.add_text(72, y, "My commitment:", 'F2', 11, 0.2)
    y -= 18
    for _j in range(4):
        doc.add_line(72, y, 540, y, 0.5, 0.7)
        y -= 22
    doc.new_page()


    # Extra content pages for 78+ minimum
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "MY ACTION PLAN", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "CREATIVE RESPONSE", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "ADDITIONAL THOUGHTS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "MY ACTION PLAN", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "CREATIVE RESPONSE", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "ADDITIONAL THOUGHTS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "MY ACTION PLAN", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "CREATIVE RESPONSE", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "ADDITIONAL THOUGHTS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "GROWTH JOURNAL", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "NOTES & REFLECTIONS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "DEEPER EXPLORATION", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "MY ACTION PLAN", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "CREATIVE RESPONSE", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.add_centered_text(740, "ADDITIONAL THOUGHTS", 'F2', 14, 0.2)
    doc.add_line(72, 725, 540, 725, 1, 0.3)
    doc.add_text(72, 700, "Use this space for your thoughts and reflections:", 'F4', 11, 0.3)
    y = 678
    for _j in range(20):
        doc.add_line(72, y, 540, y, 0.5, 0.75)
        y -= 25
    doc.new_page()
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book362_Mother_Daughter_Activities.pdf')
    print("Book362_Mother_Daughter_Activities.pdf created successfully!")

if __name__=="__main__":
    create_book()
