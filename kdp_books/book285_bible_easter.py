#!/usr/bin/env python3
"""Book 285 - The Easter Story: How Jesus' Love Saved the World"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc

def create_book():
    pdf = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    def draw_border(pdf, x, y, w, h, gray=0.3):
        pdf.add_rect(x, y, w, h, line_width=2, gray=gray)
        pdf.add_rect(x+3, y+3, w-6, h-6, line_width=0.5, gray=gray)

    def illus_box(pdf, y, desc, height=140):
        pdf.add_filled_rect(60, y, 492, height, gray=0.95)
        pdf.add_rect(60, y, 492, height, line_width=1.5, gray=0.4)
        pdf.add_text(70, y+height-18, "[ILLUSTRATION:", font='F2', size=10, gray=0.3)
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
    pdf.add_filled_rect(50, 580, 512, 150, gray=0.88)
    pdf.add_centered_text(700, "THE EASTER STORY", font='F2', size=28, gray=0.1)
    pdf.add_centered_text(665, "How Jesus' Love", font='F5', size=18, gray=0.2)
    pdf.add_centered_text(640, "Saved the World", font='F5', size=18, gray=0.2)
    illus_box(pdf, 330, "An empty tomb with the stone rolled away, BRILLIANT golden-white resurrection light pouring from inside. A pathway of light leads from the dark tomb to a glorious sunrise. Lilies bloom around the tomb entrance. The cross stands empty on a distant hill. The atmosphere is one of absolute victory, hope, and joy. Easter morning in all its glory!", 190)
    pdf.add_centered_text(290, "For Kids Ages 5-15", font='F2', size=14, gray=0.3)
    pdf.add_centered_text(260, "The Complete Easter Narrative Told with Love", font='F4', size=12, gray=0.4)
    pdf.add_centered_text(100, f"Written by {author}", font='F5', size=14, gray=0.2)

    # COPYRIGHT
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_text(72, 700, "THE EASTER STORY", font='F2', size=16, gray=0.1)
    pdf.add_line(72, 688, 300, 688, width=0.5, gray=0.5)
    pdf.add_text(72, 665, f"Copyright 2025 {author}. All rights reserved.", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 645, "Scripture from World English Bible (WEB) - Public Domain", font='F4', size=10, gray=0.3)
    pdf.add_text(72, 615, "Presented sensitively and age-appropriately for children.", font='F4', size=10, gray=0.3)
    pdf.add_filled_rect(60, 100, 492, 50, gray=0.92)
    pdf.add_text(72, 130, "For every child - THIS is the story that changes everything!", font='F5', size=11, gray=0.2)

    chapters = [
        {
            "title": "PALM SUNDAY",
            "chapter": "Chapter 1",
            "illustration": "Jesus riding a young donkey through the streets of Jerusalem. Crowds of joyful people line both sides, waving green palm branches. Children throw their colorful cloaks on the road. People shout and smile. Some climb trees for a better view. The golden walls of Jerusalem gleam behind. The atmosphere is pure celebration and excitement - a parade for the King!",
            "narrative": "The crowd went WILD! 'HOSANNA! Blessed is He who comes in the name of the Lord!' People ripped branches from palm trees and waved them like victory flags. Children threw their cloaks on the dusty road to make a royal carpet. Jesus rode into Jerusalem on a young donkey - humble even in triumph. The whole city buzzed: 'Who IS this?!' And the crowds shouted: 'This is Jesus, the prophet from Nazareth!' If only they knew - their shouting praise would turn to something else in just five days...",
            "verse": "The multitudes who went before him and who followed kept shouting, 'Hosanna to the son of David!' - Matthew 21:9 (WEB)",
            "reflection": "The same crowd that shouted 'Hosanna!' would soon shout 'Crucify!' Are you a fair-weather friend to Jesus, or do you follow Him always?"
        },
        {
            "title": "THE LAST SUPPER",
            "chapter": "Chapter 2",
            "illustration": "Jesus sitting at a long table with His twelve disciples in a warm, candlelit upper room. He holds bread in his hands, breaking it. A cup of wine sits before Him. The disciples lean in, listening intently. Some look confused, some emotional. Judas lurks in shadow near the end. Multiple clay oil lamps provide warm golden glow. The moment is intimate and sacred.",
            "narrative": "On Thursday evening, Jesus gathered His closest friends for one final meal together. He already knew what was coming. He knew Judas would betray Him. He knew Peter would deny Him. He knew they would ALL run away. Yet He loved them perfectly. He took bread, broke it, and said: 'This is My body, given for you.' He lifted the cup: 'This is My blood, poured out for many for the forgiveness of sins.' Then He did something that stunned them all - He knelt down and washed their dirty feet. The King of the Universe washing servant's feet. 'Love each other as I have loved you,' He said. 'No greater love exists than laying down your life for your friends.'",
            "verse": "This is my body which is given for you. Do this in memory of me. - Luke 22:19 (WEB)",
            "reflection": "Jesus served His friends even knowing they would fail Him. Can you love and serve people even when they let you down?"
        },
        {
            "title": "GARDEN OF GETHSEMANE",
            "chapter": "Chapter 3",
            "illustration": "Jesus kneeling alone under ancient gnarled olive trees in a moonlit garden. His face shows deep anguish, sweat mingling with tears. His hands grip the ground in desperate prayer. In the background, three disciples sleep curled up among the tree roots. Moonlight creates silver patterns through the leaves. The atmosphere is heavy with sorrow and spiritual battle. Distant torches flicker approaching.",
            "narrative": "After supper, Jesus led His disciples to a quiet garden on the Mount of Olives. 'Stay here and pray,' He asked. Then He walked deeper among the olive trees - alone. And there, in the darkness, Jesus faced the weight of the entire world's sin pressing down on Him. He was SO distressed that drops of blood mixed with His sweat! 'Father,' He cried, 'if there is ANY other way... take this cup from Me!' Three times He prayed this agonizing prayer. Three times He returned to find His friends sleeping. But each time He surrendered: 'Not MY will, but YOURS be done.' An angel appeared to strengthen Him. Then - torches in the distance. Judas was coming with soldiers...",
            "verse": "Not my will, but yours, be done. - Luke 22:42 (WEB)",
            "reflection": "Jesus was honest with God about His pain but still trusted God's plan. You can be honest with God about YOUR feelings too."
        },

        {
            "title": "THE TRIAL",
            "chapter": "Chapter 4",
            "illustration": "Jesus standing calm and dignified before Pontius Pilate in a Roman courtyard. Pilate sits elevated on a judgment seat looking troubled and conflicted. An angry crowd fills the courtyard below, fists raised, mouths open shouting. Roman soldiers with spears stand guard. Jesus stands perfectly still and peaceful amid the chaos. Pilate holds a basin of water, about to wash his hands.",
            "narrative": "The soldiers arrested Jesus in the garden. His friends ran away in fear. Peter followed at a distance - then denied even knowing Jesus three times before a rooster crowed! Jesus was dragged from trial to trial through the night. The Jewish leaders accused Him of blasphemy. They spit on Him. They slapped His face. At dawn, they brought Him to Pilate, the Roman governor. Pilate found no crime in Jesus! He tried to release Him. But the crowd screamed: 'CRUCIFY HIM! CRUCIFY HIM!' Pilate - a coward who feared the mob - washed his hands and handed Jesus over. An innocent man condemned by guilty people.",
            "verse": "Pilate said to them, 'What then shall I do to Jesus, who is called Christ?' They all said to him, 'Let him be crucified!' - Matthew 27:22 (WEB)",
            "reflection": "Do you follow the crowd or stand for what's right? Pilate knew Jesus was innocent but gave in to pressure. Choose courage!"
        },
        {
            "title": "THE CROSS",
            "chapter": "Chapter 5",
            "illustration": "Three wooden crosses silhouetted on a hilltop called Golgotha against a dramatically darkened sky. The middle cross where Jesus hangs is slightly larger. Dark storm clouds swirl overhead despite it being midday. A few faithful followers (including Mary and John) stand at the base weeping. The scene is solemn and heavy, but light breaks through the clouds above the cross - hope in the darkness. Handled sensitively with focus on love rather than graphic details.",
            "narrative": "This is the hardest part of the story - but also the most loving. Jesus carried His heavy cross up the hill called Golgotha. There, He was crucified between two criminals. The sky turned BLACK at noon - creation itself mourned! But even on the cross, Jesus' love shone through. He forgave His killers: 'Father, forgive them, they don't know what they're doing.' He saved the criminal beside Him: 'Today you'll be with Me in paradise.' He cared for His mother: 'John, take care of her.' Then Jesus cried: 'IT IS FINISHED!' and gave up His spirit. WHY? Because He LOVES YOU. He took the punishment for YOUR sins so you never have to. The curtain in the temple tore from top to bottom - the way to God was now OPEN!",
            "verse": "For God so loved the world, that he gave his one and only Son, that whoever believes in him should not perish, but have eternal life. - John 3:16 (WEB)",
            "reflection": "Jesus chose the cross because He loves YOU. He could have called angels to save Him, but He chose YOU instead. How does that make you feel?"
        },
        {
            "title": "THE DARK DAY",
            "chapter": "Chapter 6",
            "illustration": "The empty cross standing on the hill at sunset, with the stone tomb in the foreground. A large round stone seals the tomb entrance. Roman soldiers in full armor stand guard looking bored and nervous. The sunset casts long shadows. Everything feels heavy and still. A few flowers grow near the tomb. Saturday - the waiting day between death and resurrection.",
            "narrative": "Saturday. The worst day in history. Jesus' broken body lay wrapped in burial cloths inside a cold stone tomb. A massive stone sealed the entrance. Roman soldiers guarded it. The disciples hid behind locked doors, sobbing and terrified. Everything they'd hoped for seemed dead. Three years of miracles, teaching, and friendship - apparently ended by a cross and a tomb. They had forgotten His promise: 'I will rise again on the third day.' In those dark hours, they couldn't see what was coming. But God was working in the silence. Sometimes the darkest moments are right before the most glorious sunrise...",
            "verse": "Unless a grain of wheat falls into the earth and dies, it remains by itself alone. But if it dies, it bears much fruit. - John 12:24 (WEB)",
            "reflection": "Sometimes life has 'Saturday' moments - when everything seems hopeless. But SUNDAY IS COMING! Trust God in the waiting."
        },
        {
            "title": "THE RESURRECTION!",
            "chapter": "Chapter 7",
            "illustration": "THE MOMENT OF VICTORY: The stone tomb with the massive round stone ROLLED AWAY! BRILLIANT golden-white light EXPLODES from inside the empty tomb like a sunrise concentrated into one space! An angel in blazing white sits on the rolled stone, face shining like lightning. The grave cloths lie folded neatly inside. Women with spice jars arrive and DROP them in shock and growing JOY. Roman guards lie flat on the ground unconscious. The very first Easter sunrise paints the sky in glorious pinks, golds, and oranges!",
            "narrative": "SUNDAY MORNING! Before dawn, the earth SHOOK! An angel descended like lightning and ROLLED that massive stone away like it was nothing! The Roman guards collapsed in terror! When the women arrived at sunrise, the angel was SITTING on the stone (what confidence!) and said: 'WHY do you look for the LIVING among the DEAD? He is NOT HERE! HE IS RISEN! Just as He said!' They ran inside - EMPTY! Just folded cloths where His body had been! He wasn't stolen - He was ALIVE! Death, the ultimate enemy, had been DESTROYED! The grave couldn't hold Him! Sin was conquered! The penalty was paid! LIFE WON! This changes EVERYTHING!",
            "verse": "He is not here, for he has risen, just like he said. Come, see the place where the Lord was lying. - Matthew 28:6 (WEB)",
            "reflection": "JESUS IS ALIVE! This isn't a fairy tale - it's history! Over 500 people saw Him alive. His resurrection proves EVERYTHING He said is true!"
        },

        {
            "title": "HE IS ALIVE!",
            "chapter": "Chapter 8",
            "illustration": "The risen Jesus appearing to His disciples in a room. Thomas reaches out to touch Jesus' wounded hands, his face transforming from doubt to absolute faith and worship. Other disciples crowd around with tears of joy. Jesus smiles warmly with arms open. His hands show nail marks but His face radiates resurrection life and victory. The room fills with golden light from His presence.",
            "narrative": "Over the next forty days, Jesus appeared to His friends MANY times - proving beyond any doubt that He was truly alive! He appeared to Mary in the garden. He walked with two disciples on the road to Emmaus. He ate fish with His friends on the beach. He cooked them breakfast! He showed them His hands and side. Thomas, who doubted, touched His wounds and fell to his knees: 'My Lord and my God!' Jesus appeared to over 500 people at once! He was really, truly, physically ALIVE! He ate with them, talked with them, taught them. This was no ghost, no hallucination, no wish - this was the RISEN JESUS in the flesh!",
            "verse": "Thomas answered him, 'My Lord and my God!' Jesus said to him, 'Because you have seen me, you have believed. Blessed are those who have not seen and have believed.' - John 20:28-29 (WEB)",
            "reflection": "Thomas needed to see to believe. Jesus says those who believe WITHOUT seeing are blessed. That's YOU! Do you believe?"
        },
        {
            "title": "THE PROMISE",
            "chapter": "Chapter 9",
            "illustration": "Jesus ascending into heaven from the Mount of Olives. His feet lift off the ground as He rises toward brilliant white clouds above. His hands are outstretched in blessing over His disciples below, who look up with faces showing both awe and longing. Two angels in white stand among the disciples. The sky opens in layers of golden light. Jesus' robes billow as He ascends. It is majestic and hopeful.",
            "narrative": "After forty amazing days with His risen Lord, the disciples gathered on the Mount of Olives. Jesus gave them their mission: 'Go into ALL the world and tell EVERYONE the good news! I will be with you ALWAYS, to the very end of the age.' Then, as they watched in amazement, Jesus began to rise! Up through the air, higher and higher, until a cloud received Him from their sight! Two angels appeared: 'Why do you stand looking at the sky? This same Jesus will come back in the same way you've seen Him go!' Jesus is alive in heaven right NOW, preparing a place for everyone who believes. And one day - one glorious day - He's coming BACK!",
            "verse": "I am with you always, even to the end of the age. - Matthew 28:20 (WEB)",
            "reflection": "Jesus promised to come BACK! He also promised to be with you NOW through His Spirit. You're never alone. He's coming again!"
        },
        {
            "title": "WHAT EASTER MEANS FOR ME",
            "chapter": "Chapter 10",
            "illustration": "A diverse group of happy children from many backgrounds standing together outdoors on a bright Easter morning. Some hold Bibles, some have hands raised in praise, some hug each other. Behind them, an empty cross and empty tomb are visible on a green hill. A rainbow arches overhead. Flowers bloom everywhere. The children radiate joy, hope, and confidence. The future is bright!",
            "narrative": "So what does Easter mean for YOU? It means your sins can be completely forgiven - past, present, and future! It means death is NOT the end - you will live forever with Jesus! It means you have a friend who will NEVER leave you! It means God's power is available to help you every single day! It means you have purpose - to share this amazing news with others! It means no matter how dark life gets, SUNDAY ALWAYS COMES! If you believe that Jesus is God's Son, that He died for your sins, and that God raised Him from the dead - you are SAVED! Your story joins the greatest story ever told. Welcome to the family of God!",
            "verse": "If you will confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved. - Romans 10:9 (WEB)",
            "reflection": "Have YOU accepted Jesus? If so, you have ETERNAL LIFE! If not, today can be YOUR resurrection day! Talk to God right now!"
        }
    ]


    # RENDER CHAPTERS
    gray_vals = [0.88, 0.92, 0.95, 0.90, 0.93, 0.88, 0.97, 0.91, 0.94, 0.89]
    
    for idx, ch in enumerate(chapters):
        bg = gray_vals[idx % len(gray_vals)]
        
        # Page 1: Chapter title + Illustration + Narrative
        pdf.new_page()
        pdf.add_filled_rect(0, 700, 612, 92, gray=bg)
        pdf.add_filled_rect(40, 705, 532, 80, gray=0.97)
        draw_border(pdf, 40, 705, 532, 80, gray=0.3)
        pdf.add_centered_text(762, ch["chapter"], font='F4', size=11, gray=0.5)
        pdf.add_centered_text(738, ch["title"], font='F2', size=20, gray=0.1)
        
        illus_box(pdf, 470, ch["illustration"], 190)
        
        pdf.add_filled_rect(50, 450, 512, 8, gray=0.3)
        
        # Narrative
        pdf.add_filled_rect(50, 180, 512, 260, gray=0.97)
        pdf.add_rect(50, 180, 512, 260, line_width=0.5, gray=0.5)
        wrap(pdf, 65, 425, ch["narrative"], font='F5', size=11, mw=70)
        
        # Page 2: Verse + Reflection
        pdf.new_page()
        pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
        pdf.add_text(60, 760, ch["title"] + " - Reflection", font='F2', size=14, gray=0.2)
        pdf.add_line(60, 750, 350, 750, width=0.5, gray=0.4)
        
        # Verse box
        pdf.add_filled_rect(50, 640, 512, 90, gray=0.92)
        draw_border(pdf, 50, 640, 512, 90, gray=0.4)
        pdf.add_text(65, 715, "KEY VERSE:", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 693, ch["verse"], font='F3', size=10, mw=72)
        
        # Reflection
        pdf.add_filled_rect(50, 490, 512, 130, gray=bg)
        pdf.add_rect(50, 490, 512, 130, line_width=1, gray=0.3)
        pdf.add_text(65, 605, "REFLECTION:", font='F2', size=12, gray=0.1)
        wrap(pdf, 65, 585, ch["reflection"], font='F5', size=11, mw=70)
        
        # My Response
        pdf.add_text(60, 460, "MY RESPONSE:", font='F2', size=12, gray=0.1)
        pdf.add_text(60, 440, "What does this chapter mean to me personally?", font='F4', size=11, gray=0.3)
        for i in range(6):
            pdf.add_line(60, 410-(i*28), 550, 410-(i*28), width=0.5, gray=0.6)

    # FINAL PAGES - The Gospel Summary + Decision
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.95)
    draw_border(pdf, 40, 40, 532, 712, gray=0.2)
    pdf.add_filled_rect(60, 650, 492, 80, gray=0.88)
    pdf.add_centered_text(710, "THE GOOD NEWS IN 4 STEPS", font='F2', size=20, gray=0.1)
    pdf.add_centered_text(680, "The Easter Story Summarized", font='F4', size=12, gray=0.3)
    
    steps = [
        "1. GOD LOVES YOU! He created you and wants a relationship with you.",
        "2. SIN SEPARATES US. We all mess up and fall short of God's perfection.",
        "3. JESUS DIED FOR YOU! He took your punishment on the cross.",
        "4. BELIEVE & RECEIVE! Trust in Jesus and receive eternal life!"
    ]
    y = 610
    for i, step in enumerate(steps):
        pdf.add_filled_rect(60, y-5, 492, 35, gray=0.92 if i%2==0 else 0.97)
        pdf.add_text(75, y+8, step, font='F2', size=11, gray=0.1)
        y -= 50
    
    pdf.add_filled_rect(60, 350, 492, 60, gray=0.88)
    draw_border(pdf, 60, 350, 492, 60, gray=0.3)
    pdf.add_centered_text(390, "HE IS RISEN! HE IS RISEN INDEED!", font='F2', size=16, gray=0.1)
    pdf.add_centered_text(365, "Happy Easter - Today and Every Day!", font='F5', size=13, gray=0.3)
    
    pdf.add_centered_text(280, "If you prayed to receive Jesus today, tell someone!", font='F4', size=12, gray=0.3)
    pdf.add_centered_text(250, "Welcome to God's family!", font='F2', size=14, gray=0.2)
    
    pdf.add_text(60, 180, "Date of my decision:", font='F4', size=11, gray=0.3)
    pdf.add_line(220, 180, 400, 180, width=0.5, gray=0.5)
    pdf.add_text(60, 150, "My name:", font='F4', size=11, gray=0.3)
    pdf.add_line(150, 150, 400, 150, width=0.5, gray=0.5)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Book285_Easter_Story_Kids.pdf")
    pdf.save(output_path)
    print(f"Created: {output_path}")

if __name__ == "__main__":
    create_book()
