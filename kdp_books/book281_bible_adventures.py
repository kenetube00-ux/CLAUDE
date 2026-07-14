#!/usr/bin/env python3
"""Book 281 - Bible Adventures: 10 Action-Packed Stories for Brave Kids"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    def draw_border(pdf, x, y, w, h, gray=0.3):
        pdf.add_rect(x, y, w, h, line_width=2, gray=gray)
        pdf.add_rect(x+3, y+3, w-6, h-6, line_width=0.5, gray=gray)

    def illus_box(pdf, y, desc, height=110):
        pdf.add_filled_rect(60, y, 492, height, gray=0.95)
        pdf.add_rect(60, y, 492, height, line_width=1.5, gray=0.4)
        pdf.add_text(70, y+height-18, "[ACTION ILLUSTRATION:", font='F2', size=10, gray=0.3)
        words = desc.split()
        line, ly = "", y+height-33
        for w in words:
            if len(line+" "+w)>75:
                pdf.add_text(70, ly, line.strip(), font='F3', size=9, gray=0.4)
                ly -= 13; line = w
            else: line = line+" "+w if line else w
        if line: pdf.add_text(70, ly, line.strip(), font='F3', size=9, gray=0.4)
        pdf.add_text(70, ly-13, "]", font='F2', size=10, gray=0.3)

    def wrap(pdf, x, y, text, font='F4', size=11, mw=70, gray=0):
        words = text.split()
        line, cy = "", y
        for w in words:
            if len(line+" "+w)>mw:
                pdf.add_text(x, cy, line.strip(), font=font, size=size, gray=gray)
                cy -= 15; line = w
            else: line = line+" "+w if line else w
        if line: pdf.add_text(x, cy, line.strip(), font=font, size=size, gray=gray); cy -= 15
        return cy


    # TITLE PAGE
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    draw_border(pdf, 30, 30, 552, 732, gray=0.2)
    pdf.add_filled_rect(50, 590, 512, 140, gray=0.88)
    pdf.add_centered_text(700, "BIBLE ADVENTURES", font='F2', size=30, gray=0.1)
    pdf.add_centered_text(665, "10 Action-Packed Stories", font='F5', size=18, gray=0.2)
    pdf.add_centered_text(638, "for Brave Kids", font='F5', size=18, gray=0.2)
    illus_box(pdf, 370, "An epic action scene montage: Moses with staff raised as sea parts, David mid-sling against Goliath, Peter breaking free from chains with angel, Paul on a sinking ship in stormy seas, Gideon with torch blazing. Dynamic poses, movement lines, dramatic lighting. Pure adventure energy!", 160)
    pdf.add_centered_text(330, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(300, "Written in Exciting Adventure Style with Cliffhangers!", font='F4', size=11, gray=0.4)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)

    # COPYRIGHT
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "BIBLE ADVENTURES", font='F2', size=16, gray=0.1)
    pdf.add_line(72, 688, 350, 688, width=0.5, gray=0.5)
    pdf.add_text(72, 665, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 645, "Scripture from World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 50, gray=0.92)
    pdf.add_text(72, 130, "For every kid who loves adventure - the Bible is the GREATEST!", font='F5', size=11, gray=0.2)

    adventures = [
        {
            "title": "THE GREAT ESCAPE",
            "subtitle": "Moses Leads Israel Through the Red Sea",
            "illustration": "DYNAMIC ACTION: Moses at the edge of the sea, staff thrust skyward, wind blasting his robes sideways. Behind him a wall of dust from Pharaoh's charging chariots. Before him the sea begins to split with water spraying upward like an explosion. People run toward the opening. Lightning in the sky. Maximum dramatic tension!",
            "opening": "BOOM! BOOM! BOOM! The ground shook with the thunder of a thousand chariots. Two million people were TRAPPED - the sea ahead, death behind. Children screamed. Women wept. Men grabbed their families and ran toward... nothing. There was nowhere to go!",
            "action": "Moses SLAMMED his staff toward the sky. 'STAND STILL AND WATCH!' he roared over the wind. Then God's pillar of fire moved like a living wall between Israel and Egypt. The east wind hit like a hurricane - WHOOOOSH! The sea ripped apart! Water towered up on both sides like skyscrapers made of ocean! 'RUN! NOW! GO GO GO!' Moses commanded. Two million people SPRINTED through the impossible corridor of water!",
            "cliffhanger": "But Pharaoh's army followed into the gap between the water walls. Six hundred chariots thundered across the seabed. The walls began to tremble...",
            "climax": "CRAAAAAASH! At Moses' command, the walls of water COLLAPSED like a building demolition! The mightiest army on earth was swept away in seconds! On the far shore, Israel stood in stunned silence... then erupted in the greatest celebration the world had ever seen!",
            "choice": "What would YOU do if you were trapped between an army and an ocean? Would you panic or trust God?",
            "verse": "The LORD will fight for you, and you shall be still. - Exodus 14:14 (WEB)"
        },
        {
            "title": "SPY MISSION",
            "subtitle": "Joshua Sends Spies to Jericho - Rahab Helps!",
            "illustration": "Two Israelite spies in dark cloaks climbing down a rope from a window in the massive city wall of Jericho at night. Rahab leans from the window above lowering the scarlet rope. Below, torches of searching soldiers flicker in the streets. The city wall is enormous. Stars and a crescent moon above. Tension and danger everywhere.",
            "opening": "The mission: sneak into the most fortified city in the land. The risk: certain death if caught. Two of Joshua's bravest warriors crept through Jericho's gates at dusk, eyes scanning every shadow. But they'd already been spotted...",
            "action": "BANG! BANG! BANG! Soldiers pounded on Rahab's door: 'OPEN UP! We know the spies are here!' The two men froze on the rooftop where Rahab had hidden them under stalks of flax. 'They already left,' Rahab called coolly. 'You might still catch them if you hurry toward the river!' The soldiers SPRINTED away. Heart pounding, Rahab raced to the roof: 'Quick! My window faces the outer wall. I'll lower you down by rope! Promise me - when you conquer this city, save my family!'",
            "cliffhanger": "The rope swayed as they descended. Below, a patrol's torch flickered closer. One slip, one sound, and it was over...",
            "climax": "The spies hit the ground running, disappearing into the dark hills. Three days later they reported to Joshua: 'God has given us the city! The people are TERRIFIED of us!' And Rahab? When the walls fell, the scarlet cord in her window saved her entire family! Her faith made her a hero - she's even listed in Jesus' family tree!",
            "choice": "Would you risk your life to help God's people like Rahab did? What does real bravery look like?",
            "verse": "The LORD your God, he is God in heaven above and on earth beneath. - Joshua 2:11 (WEB)"
        },

        {
            "title": "NIGHT RAID",
            "subtitle": "Gideon's 300 Defeat a Massive Army",
            "illustration": "300 warriors on a dark hillside SMASHING clay jars to reveal blazing torches, blowing trumpets with full force! Below them, a panicked army of 135,000 scatters in total chaos, soldiers running into each other. Fire light reflects off terrified faces. Dynamic composition with torch sparks flying, broken pottery shards mid-air, sound effect energy!",
            "opening": "Midnight. The valley below swarmed with 135,000 enemy warriors - their camp stretched as far as the eye could see, like locusts covering the ground. Gideon looked at his tiny force: 300 men. No swords. No spears. Just clay jars, torches, and trumpets. This was either the craziest plan in military history... or God's plan.",
            "action": "Gideon raised his fist. Silence. Every man gripped his jar tighter. Then - 'FOR THE LORD AND FOR GIDEON!' SMASH! Three hundred jars EXPLODED in unison! BLAAAAM! Three hundred trumpets BLASTED! Three hundred torches BLAZED to life like a ring of fire surrounding the camp! The sleeping Midianites erupted in pure CHAOS!",
            "cliffhanger": "In the darkness and confusion, the Midianites couldn't tell friend from foe. Swords clashed against their OWN soldiers...",
            "climax": "The entire army of 135,000 turned and FLED - screaming, trampling each other, running for their lives! Three hundred men with torches and trumpets had routed one of the largest armies in the ancient world! God proved that He doesn't need big numbers. He just needs obedience!",
            "choice": "Would you volunteer for a mission with 300 against 135,000? What if God told you He'd handle it?",
            "verse": "The sword of the LORD and of Gideon! - Judges 7:20 (WEB)"
        },
        {
            "title": "GIANT SLAYER",
            "subtitle": "David Takes on Goliath",
            "illustration": "FREEZE-FRAME ACTION: David's sling at full extension, the stone just leaving the leather pouch, flying toward camera. David's face shows fierce concentration. Behind the speeding stone, Goliath's massive armored figure looms with spear raised. The two armies watch from opposing hills. Dust, movement lines, raw power in the moment!",
            "opening": "For FORTY DAYS, the giant's voice boomed across the valley like thunder: 'IS THERE NO ONE BRAVE ENOUGH TO FACE ME?' Nine feet tall. Bronze armor weighing 125 pounds. A spear like a telephone pole. Goliath was a walking tank. And every soldier in Israel was TERRIFIED.",
            "action": "A teenager stepped forward. No armor. No sword. Just a leather sling and five smooth stones from the brook. 'You come with sword and spear,' David shouted, his young voice ringing with supernatural courage, 'but I come in the name of the LORD of ARMIES!' David broke into a SPRINT toward the giant! His sling whipped in three lightning-fast circles above his head - WHOOSH WHOOSH WHOOSH!",
            "cliffhanger": "The stone flew. Time seemed to slow. Every eye in both armies tracked that single stone through the air...",
            "climax": "CRACK! The stone buried itself in Goliath's forehead! The giant's eyes went blank. His massive body swayed... and CRASHED to the earth like a falling tree! THUD! The ground shook! For one shocked second, total silence. Then Israel ERUPTED in a victory roar that shook the hills! The Philistines turned and RAN!",
            "choice": "What's YOUR Goliath - the big, scary thing that seems impossible? Are you willing to run at it with faith?",
            "verse": "The battle is the LORD's, and he will give you into our hand. - 1 Samuel 17:47 (WEB)"
        },
        {
            "title": "GREAT FLOOD",
            "subtitle": "Noah Builds the Ark While Others Laugh",
            "illustration": "Noah and his sons hammering the final planks on the massive ark as dark storm clouds roll in ominously. People in the background point and laugh, unaware of the coming disaster. Lightning flickers in approaching clouds. Animals begin arriving in pairs from every direction. The ark towers above like a wooden skyscraper. First raindrops fall.",
            "opening": "For 100 YEARS they laughed. 'Old Noah's lost his mind!' they mocked. 'Building a boat in the desert? What's RAIN?' Day after day, year after year, Noah hammered, sawed, and sealed that massive ark. His neighbors threw rotten fruit. His friends abandoned him. But Noah never stopped building.",
            "action": "Then one day, the animals came. From every direction - marching, flying, slithering, crawling - in perfect pairs! Lions walked beside lambs. Eagles flew alongside sparrows. The mockers finally fell silent as thousands of creatures filed into the ark. Then Noah's family entered. God Himself sealed the door. For seven days, nothing happened. The world held its breath...",
            "cliffhanger": "On the eighth day, the sky turned black. A sound no human had ever heard before - the roar of falling water - grew from a whisper to a THUNDERING wall of sound...",
            "climax": "EVERY fountain of the deep BURST open! Rain didn't fall - it CRASHED from the sky in sheets! In hours, rivers overflowed. In days, cities vanished. In weeks, mountains disappeared. But inside the ark? Dry. Safe. Rocking gently. God's promise held. And 371 days later, a rainbow painted the sky - God's eternal promise!",
            "choice": "Could you keep doing the right thing for 100 years while everyone laughed at you? What keeps you going?",
            "verse": "Noah did everything that God commanded him. - Genesis 6:22 (WEB)"
        },

        {
            "title": "LION TAMER",
            "subtitle": "Daniel Survives the Lion's Den",
            "illustration": "Daniel being lowered by rope into a dark stone pit while massive lions pace below with gleaming eyes. Above, the king watches with anguish. Below, as Daniel's feet touch ground, a brilliant angel materializes with sword drawn, pushing lions back. Lion eyes glow in the darkness. Dramatic top-down perspective showing the depth of the pit.",
            "opening": "The trap was set perfectly. Jealous officials tricked the king into signing a law that no one could pray to anyone but the king for 30 days. Penalty? The LION PIT. They knew Daniel prayed three times daily. They were counting on it.",
            "action": "Daniel heard about the law. He walked home. Opened his window toward Jerusalem. And PRAYED - openly, loudly, faithfully. Just like always. The officials watched from outside, grinning wickedly. 'CAUGHT YOU!' That evening, soldiers dragged Daniel before the heartbroken king. 'I cannot change my own law,' the king wept. The stone lid of the lion pit groaned open. The smell of death rose from below. ROOOAAAR!",
            "cliffhanger": "They threw Daniel in. The stone crashed shut above him. Total darkness. The sound of padding paws. Hot breath on his neck. A low growl inches from his face...",
            "climax": "FLASH! Light exploded in the pit! An angel stood with blazing wings spread wide. Every lion FROZE. Then, like house cats, they lay down at Daniel's feet. One even rested its head against him! Daniel slept peacefully all night. At dawn, the king RACED to the pit: 'DANIEL! Did your God save you?!' 'O king, live forever! God sent His angel and shut the lions' mouths!'",
            "choice": "Would you keep praying even if it meant being thrown to lions? What would it take to stop YOUR prayer life?",
            "verse": "My God sent his angel and shut the lions' mouths. - Daniel 6:22 (WEB)"
        },
        {
            "title": "FIRESTORM",
            "subtitle": "Elijah Calls Fire from Heaven",
            "illustration": "THE MOMENT: A column of divine fire BLASTING down from heaven like a laser beam striking a water-soaked stone altar on Mount Carmel! The fire is white-hot at center, orange at edges. Water vaporizes into massive steam clouds. Stones MELT. Elijah stands with arms raised triumphantly. 450 prophets of Baal cower and flee. The crowd falls on their faces. Pure power!",
            "opening": "The showdown: 1 prophet of God versus 450 prophets of Baal. The contest: build an altar, call on your god to send fire. The stakes: the losing side dies. Elijah stood alone on Mount Carmel facing the largest crowd he'd ever seen. 'How long will you waver between two gods?' he thundered. 'If the LORD is God, follow Him!'",
            "action": "The Baal prophets went first. They danced. They shouted. They cut themselves. From morning until afternoon - NOTHING. Elijah taunted them: 'SHOUT LOUDER! Maybe your god is sleeping! Or maybe he's on vacation!' Then Elijah rebuilt God's altar. He SOAKED it with water - three times! The trench overflowed. 'NOW,' Elijah prayed one simple, calm prayer...",
            "cliffhanger": "Silence. Every eye looked skyward. The water-drenched altar glistened. Was God going to answer? Had Elijah made a terrible mistake?",
            "climax": "WHOOOOOOOOM! Fire fell from heaven like a bomb! Not just regular fire - supernatural fire that consumed the sacrifice, the wood, the STONES, the soil, and ALL the water! It even licked up the water in the trench! The crowd SLAMMED to the ground screaming: 'THE LORD, HE IS GOD! THE LORD, HE IS GOD!' And then the rain came...",
            "choice": "Would you stand alone for God against 450 opponents? What gives you courage when you're outnumbered?",
            "verse": "Then the fire of the LORD fell and consumed the burnt offering. - 1 Kings 18:38 (WEB)"
        },
        {
            "title": "PRISON BREAK",
            "subtitle": "An Angel Frees Peter from Chains",
            "illustration": "Peter's prison cell glowing with supernatural light as an angel in blazing white touches his chains. The iron chains SNAP and fall to the ground in pieces. Two sleeping guards slump against walls, undisturbed. The cell door swings open by itself. Peter blinks awake in confusion, thinking it's a dream. Light radiates from the angel like a star.",
            "opening": "King Herod had already killed James. Now Peter sat in maximum-security prison - chained between two soldiers, with two more guarding the door. Sixteen soldiers total. Iron chains. Locked gates. He was scheduled for execution at dawn. But across the city, the church was praying ALL NIGHT...",
            "action": "3 AM. Suddenly - LIGHT! Blinding, supernatural light filled the cell! The soldiers didn't even flinch (supernatural sleep!). An angel STRUCK Peter's side: 'QUICK! GET UP!' Peter's chains CRASHED to the floor! 'Put on your sandals. Wrap your cloak. Follow me!' Peter stumbled after the glowing figure, sure he was dreaming. Past the first guard post - no one moved. Past the second - nothing. Then the iron gate to the city...",
            "cliffhanger": "The massive iron gate was locked, bolted, and guarded. There was no way through. But the angel kept walking straight toward it...",
            "climax": "The iron gate swung open BY ITSELF! Peter walked through into the cool night air. The angel vanished! 'This is REAL!' Peter gasped. He ran to the house where believers were praying for him. He knocked. A servant girl answered, saw Peter, and was so shocked she SLAMMED THE DOOR IN HIS FACE and ran inside screaming: 'Peter is at the door!' 'You're crazy!' they said. Meanwhile, Peter kept knocking!",
            "choice": "The church prayed and God answered! Do you believe YOUR prayers can break chains and open gates?",
            "verse": "Behold, an angel of the Lord stood by him, and a light shone in the cell. - Acts 12:7 (WEB)"
        },

        {
            "title": "SHIPWRECK",
            "subtitle": "Paul Survives a Storm at Sea",
            "illustration": "A massive ancient sailing ship being torn apart by enormous dark waves during a hurricane. Mast snaps. Sails rip. Cargo flies overboard. 276 people cling to wreckage as the ship breaks in half. Through the chaos, Paul stands calmly holding a rope, face set with faith. Lightning illuminates the terrifying scene. Green-black ocean waves tower over the ship.",
            "opening": "Fourteen days. FOURTEEN DAYS of non-stop hurricane. No sun. No stars. No hope. 276 people aboard a disintegrating ship hadn't eaten in two weeks. The sailors had thrown everything overboard. The ship groaned and cracked. Everyone had given up hope of survival. Everyone... except Paul.",
            "action": "Paul stood up in the howling wind: 'TAKE COURAGE! An angel appeared to me last night. God promised that EVERY PERSON on this ship will survive! Not one life will be lost! We WILL run aground on an island, but we WILL live!' The crew stared. Was he crazy? Then Paul did something incredible - he took bread, thanked God in front of everyone, and ATE. One by one, 275 others found courage to eat too.",
            "cliffhanger": "CRACK! The ship struck a sandbar! The bow stuck fast while the stern was RIPPED APART by the pounding surf! Soldiers drew swords to kill the prisoners (so none would escape). Paul's life hung by a thread...",
            "climax": "The centurion stopped the soldiers - he wanted to save Paul! 'EVERYONE WHO CAN SWIM - JUMP! Everyone else - grab planks and hold on!' One by one, through the crashing surf, 276 people washed ashore on the island of Malta. Every. Single. One. Alive! God's promise through Paul was fulfilled perfectly!",
            "choice": "When life feels like a 14-day hurricane, can you trust God's promise that you'll make it through?",
            "verse": "Therefore take courage, men, for I believe God that it will be just as it has been spoken to me. - Acts 27:25 (WEB)"
        },
        {
            "title": "THE EMPTY TOMB",
            "subtitle": "The Greatest Adventure: Resurrection!",
            "illustration": "THE EMPTY TOMB at sunrise - the massive stone rolled aside, BRILLIANT golden-white light pouring from inside. Roman soldiers lie unconscious on the ground. An angel in blazing white sits on the stone. Mary Magdalene arrives with spice jars and DROPS them in shock. The sunrise behind paints the sky in resurrection glory - gold, pink, orange. LIFE defeating death!",
            "opening": "It was over. Or so everyone thought. Jesus - their leader, their hope, their friend - was dead. Buried. A massive stone sealed His tomb. Roman soldiers guarded it. The disciples hid behind locked doors, shaking with fear. Three days of darkness. Three days of despair. Three days of death having the last word...",
            "action": "EARTHQUAKE! The ground SHOOK violently at dawn on Sunday. An angel descended from heaven like a bolt of lightning! His appearance was blinding white. He rolled the massive stone away with one hand! The tough Roman guards fainted like dead men! When the women arrived with burial spices, the angel said the GREATEST WORDS IN HISTORY: 'He is NOT here! HE IS RISEN! Just as He said!'",
            "cliffhanger": "But was it really true? Could death actually be defeated? The women ran to tell the disciples, but would anyone believe them?",
            "climax": "Peter and John SPRINTED to the tomb - EMPTY! Just folded grave clothes inside! Over the next 40 days, Jesus appeared to Mary, to the disciples, to 500 people at once! He ate fish! He showed His wounds! He was ALIVE! Death - the ultimate enemy - had been DESTROYED! The greatest adventure in history wasn't about fighting armies or slaying giants. It was about LIFE conquering death forever!",
            "choice": "Jesus conquered death so YOU could live forever! Have you accepted His invitation to eternal adventure?",
            "verse": "He is not here, for he has risen, just like he said. - Matthew 28:6 (WEB)"
        }
    ]


    # RENDER ADVENTURES
    gray_vals = [0.88, 0.92, 0.95, 0.90, 0.93, 0.88, 0.97, 0.91, 0.94, 0.89]
    
    for idx, adv in enumerate(adventures):
        bg = gray_vals[idx % len(gray_vals)]
        
        # Page 1: Title + Illustration + Opening
        pdf.new_page()
        pdf.add_filled_rect(0, 720, 612, 72, gray=bg)
        pdf.add_filled_rect(45, 725, 522, 60, gray=0.97)
        draw_border(pdf, 45, 725, 522, 60, gray=0.2)
        pdf.add_centered_text(762, f"Adventure {idx+1}", font='F4', size=10, gray=0.5)
        pdf.add_centered_text(742, adv["title"], font='F2', size=22, gray=0.1)
        pdf.add_centered_text(727, adv["subtitle"], font='F4', size=10, gray=0.3)
        
        illus_box(pdf, 550, adv["illustration"], 140)
        
        # Opening - exciting start
        pdf.add_filled_rect(50, 380, 512, 150, gray=0.97)
        pdf.add_rect(50, 380, 512, 150, line_width=0.5, gray=0.5)
        wrap(pdf, 60, 515, adv["opening"], font='F5', size=11, mw=72)
        
        # Accent bar
        pdf.add_filled_rect(50, 365, 512, 8, gray=0.3)
        
        # Page 2: Action + Cliffhanger
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.98)
        pdf.add_filled_rect(40, 750, 532, 5, gray=bg)
        pdf.add_text(60, 740, adv["title"] + " (THE ACTION!)", font='F2', size=14, gray=0.1)
        pdf.add_line(60, 732, 350, 732, width=1, gray=0.4)
        
        y = wrap(pdf, 60, 710, adv["action"], font='F4', size=11, mw=72)
        
        # Cliffhanger box
        y -= 20
        pdf.add_filled_rect(50, y-55, 512, 65, gray=0.88)
        draw_border(pdf, 50, y-55, 512, 65, gray=0.3)
        pdf.add_text(60, y-2, "CLIFFHANGER...", font='F2', size=12, gray=0.1)
        wrap(pdf, 60, y-20, adv["cliffhanger"], font='F5', size=11, mw=72)
        
        # Page 3: Climax + Choice + Verse
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_filled_rect(40, 720, 532, 50, gray=0.88)
        pdf.add_text(60, 745, adv["title"] + " - THE CLIMAX!", font='F2', size=14, gray=0.1)
        
        y = wrap(pdf, 60, 700, adv["climax"], font='F4', size=11, mw=72)
        
        # What Would YOU Do?
        y -= 20
        pdf.add_filled_rect(50, y-70, 512, 80, gray=bg)
        pdf.add_rect(50, y-70, 512, 80, line_width=1.5, gray=0.3)
        pdf.add_text(65, y-5, "WHAT WOULD YOU DO?", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, y-25, adv["choice"], font='F5', size=11, mw=68)
        
        # Writing lines
        y -= 100
        for i in range(3):
            pdf.add_line(60, y-(i*25), 550, y-(i*25), width=0.5, gray=0.6)
        
        # Verse at bottom
        pdf.add_filled_rect(50, 80, 512, 50, gray=0.92)
        pdf.add_text(65, 115, "ADVENTURE VERSE:", font='F2', size=10, gray=0.2)
        wrap(pdf, 65, 98, adv["verse"], font='F3', size=9, mw=75)

    # FINAL PAGE - Adventure Rank
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    pdf.add_filled_rect(40, 710, 532, 60, gray=0.88)
    draw_border(pdf, 40, 710, 532, 60, gray=0.3)
    pdf.add_centered_text(745, "YOUR ADVENTURE RANK!", font='F2', size=18, gray=0.1)
    pdf.add_centered_text(718, "Rate each adventure 1-5 stars!", font='F4', size=12, gray=0.3)
    
    y = 680
    for idx, adv in enumerate(adventures):
        pdf.add_filled_rect(50, y-5, 512, 25, gray=0.97 if idx%2==0 else 0.92)
        pdf.add_text(60, y, f"{idx+1}. {adv['title']}", font='F4', size=10, gray=0.2)
        pdf.add_text(400, y, "Stars: _____", font='F4', size=10, gray=0.4)
        y -= 30
    
    pdf.add_centered_text(350, "CONGRATULATIONS, ADVENTURER!", font='F2', size=14, gray=0.2)
    pdf.add_centered_text(320, "You've experienced 10 of the Bible's greatest adventures!", font='F4', size=11, gray=0.3)
    pdf.add_centered_text(295, "Remember: YOUR life with God is the greatest adventure of all!", font='F5', size=11, gray=0.3)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book281_Bible_Adventures_Kids.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
