#!/usr/bin/env python3
"""Book 285 - The Easter Story: How Jesus' Love Saved the World"""
import random, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_utils import PDFDoc
random.seed(285)
TITLE = "THE EASTER STORY"
SUBTITLE = "How Jesus' Love Saved the World"
AUTHOR = "Daniel Tesfamariam"
FILENAME = "Book285_Easter_Story_Kids.pdf"
chapters = [
    {"title": "Palm Sunday - The King Arrives", "verse": "Hosanna! Blessed is he who comes in the name of the Lord! - Mark 11:9 (WEB)",
     "p1": "It was a beautiful Sunday morning in spring. Jesus and His disciples were approaching Jerusalem for the Passover festival. Huge crowds were gathering because everyone had heard about Jesus' miracles. Jesus sent two disciples ahead to bring a young donkey that had never been ridden. He climbed on and began riding toward the great city as thousands cheered along the road.",
     "p2": "The crowd went wild with joy! People spread their cloaks on the road like a carpet for royalty. Others cut palm branches from trees and waved them high, shouting 'HOSANNA! Blessed is He who comes in the name of the Lord!' Children sang. Adults wept with joy. The entire city buzzed with excitement. Could this be the promised King who would save Israel? The noise of celebration echoed off the ancient walls of Jerusalem.",
     "words": ["PALM", "HOSANNA", "DONKEY", "KING", "CROWD", "SUNDAY", "PRAISE", "BRANCHES"]},
    {"title": "The Last Supper", "verse": "This is my body which is given for you. Do this in memory of me. - Luke 22:19 (WEB)",
     "p1": "On Thursday evening, Jesus gathered His twelve closest friends for a special Passover meal in an upper room. He knew this would be their last meal together before the cross. With tender love, Jesus washed each disciple's dirty feet - the job of the lowest servant! He was showing them that true greatness means serving others, even in the humblest ways.",
     "p2": "During the meal, Jesus took bread, gave thanks, broke it, and said, 'This is my body, given for you.' Then He took a cup of wine saying, 'This cup is the new covenant in my blood, poured out for the forgiveness of sins.' He was telling them that He would give His own life to save the world. Jesus also revealed that one of the twelve would betray Him. The disciples were shocked and heartbroken.",
     "words": ["SUPPER", "BREAD", "WINE", "SERVE", "WASH", "FEET", "REMEMBER", "LOVE"]},
    {"title": "The Garden of Gethsemane", "verse": "Not my will, but yours, be done. - Luke 22:42 (WEB)",
     "p1": "After supper, Jesus went to a garden called Gethsemane to pray. He was deeply troubled, knowing the terrible suffering ahead. He asked Peter, James, and John to stay awake and pray with Him. Then He went a little further, fell face-down on the ground, and prayed with such intensity that His sweat became like drops of blood falling to the ground.",
     "p2": "Three times Jesus cried out, 'Father, if it is possible, take this cup of suffering from me!' He was not afraid to be honest with God about His pain. But each time He added the most powerful words ever prayed: 'Nevertheless, not MY will, but YOUR will be done.' He chose obedience over comfort. An angel came from heaven to strengthen Him. His friends fell asleep, unable to stay awake during His darkest hour.",
     "words": ["GARDEN", "PRAYER", "NIGHT", "SWEAT", "KNEEL", "FATHER", "WILL", "TRUST"]},
    {"title": "The Trial", "verse": "He was despised and rejected by men. - Isaiah 53:3 (WEB)",
     "p1": "Judas arrived in the garden with soldiers and betrayed Jesus with a kiss. Jesus was arrested and dragged before the religious leaders for an illegal nighttime trial. Witnesses told lies about Him. They spit in His face and hit Him with their fists. Peter, watching from a distance, denied knowing Jesus three times before the rooster crowed, just as Jesus had predicted.",
     "p2": "In the morning, Jesus was brought before the Roman governor Pilate. Pilate found no crime worthy of death but the crowd demanded crucifixion. He offered to release one prisoner - the crowd chose a criminal named Barabbas instead of Jesus! Pilate washed his hands and handed Jesus over to be beaten. Roman soldiers whipped His back, jammed a crown of thorns onto His head, and mocked Him as a fake king. Yet Jesus endured it all silently, like a lamb led to slaughter.",
     "words": ["TRIAL", "JUDAS", "PETER", "PILATE", "CROWN", "THORNS", "SILENT", "LAMB"]},

    {"title": "The Cross - The Greatest Love", "verse": "Father, forgive them, for they don't know what they are doing. - Luke 23:34 (WEB)",
     "p1": "Jesus carried His heavy wooden cross through the streets of Jerusalem while crowds watched. His body was weak from the beatings. A man named Simon was forced to help carry the cross. At a hill called Golgotha, they nailed Jesus to the cross. Even in His worst pain, Jesus' first words were of forgiveness: 'Father, forgive them, for they don't know what they are doing.'",
     "p2": "For six hours Jesus hung on the cross. Darkness covered the land for three hours. Jesus spoke seven times from the cross - forgiving, comforting, and trusting His Father. He was not dying as a helpless victim - He was CHOOSING to give His life as payment for the sins of the whole world. Finally He cried, 'It is finished!' and breathed His last. The temple curtain tore in two. A Roman soldier whispered, 'Truly this was the Son of God.'",
     "words": ["CROSS", "FORGIVE", "LOVE", "FINISH", "DARK", "CURTAIN", "SON", "SAVE"]},
    {"title": "The Dark Day - Saturday", "verse": "Weeping may last for the night, but joy comes in the morning. - Psalm 30:5 (WEB)",
     "p1": "Saturday was the darkest, saddest day the disciples had ever known. Their beloved teacher and friend was dead. Joseph of Arimathea had placed Jesus' body in a new tomb carved from rock and rolled a massive stone across the entrance. Roman soldiers stood guard. To the disciples, hiding behind locked doors in fear, all hope seemed lost forever. They wept and wondered if everything Jesus promised was gone.",
     "p2": "But they did not know what was happening in the spiritual realm! The Bible tells us Jesus descended and proclaimed victory over death itself. The enemy thought he had won by killing Jesus - but it was actually GOD'S plan all along! What looked like the darkest defeat was actually setting up the greatest victory in cosmic history. Sometimes our darkest Saturdays are just the space between the cross and the resurrection.",
     "words": ["TOMB", "STONE", "DARK", "TEARS", "WAIT", "HOPE", "GUARD", "SEALED"]},
    {"title": "THE RESURRECTION - He is Alive!", "verse": "He is not here, for he has risen! - Matthew 28:6 (WEB)",
     "p1": "Very early on Sunday morning, while it was still dark, women went to the tomb carrying burial spices. The ground SHOOK with a violent earthquake! An angel descended from heaven like lightning and rolled away the massive stone as easily as a pebble! The trained Roman soldiers fainted in terror. When the women arrived, they saw the stone was moved and the tomb was OPEN!",
     "p2": "Heart pounding, they peered inside. The burial cloths were there, neatly folded - but Jesus' body was GONE! An angel in dazzling white spoke: 'Do not be afraid! You are looking for Jesus who was crucified. HE IS NOT HERE - HE IS RISEN, just as He said!' Then Jesus Himself appeared to Mary Magdalene! She grabbed His feet - He was REAL! Alive! Solid! The same Jesus, now gloriously resurrected! Death had been DEFEATED forever!",
     "words": ["RISEN", "ALIVE", "EMPTY", "ANGEL", "SUNDAY", "STONE", "GLORY", "HOPE"]},
    {"title": "He is Alive! - Appearances", "verse": "He showed himself alive by many proofs over forty days. - Acts 1:3 (WEB)",
     "p1": "Over the next forty days, Jesus appeared to hundreds of people, proving He was truly alive! He appeared to the women at the tomb. He walked with two disciples on the road to Emmaus. He appeared in the locked upper room where the disciples hid - passing through solid walls! He cooked breakfast on the beach for Peter and the others. He let Thomas touch His nail-scarred hands to prove it was really Him.",
     "p2": "Jesus was not a ghost - He ate food, talked, walked, and could be touched. But His body was transformed - He could appear and disappear, pass through walls, and would never die again. Over 500 people saw Him alive at one time! He taught His disciples for forty days about God's kingdom and gave them their mission: 'Go into all the world and tell everyone the good news!' Then He ascended to heaven in a cloud with a promise to return one day.",
     "words": ["APPEAR", "PROOF", "TOUCH", "THOMAS", "REAL", "BODY", "FORTY", "MISSION"]},
    {"title": "The Promise - What Easter Means", "verse": "Because I live, you will live also. - John 14:19 (WEB)",
     "p1": "Easter is not just about what happened 2000 years ago - it is about what it means for YOU today! Because Jesus rose from the dead, He proved that death is not the end. He conquered the grave! And He promises that everyone who believes in Him will also be raised to eternal life. 'Because I live, you will live also!' This is the greatest promise ever made - and it is backed by an empty tomb!",
     "p2": "Easter means that no matter what you face - fear, sadness, sickness, or loss - there is ALWAYS hope. If God can raise Jesus from the dead, He can bring dead things back to life in YOUR world too. Dead dreams, dead hope, broken relationships - God specializes in resurrection! Every Sunday Christians celebrate Easter because it is the foundation of everything we believe. Jesus is alive, and because He lives, we can face tomorrow without fear.",
     "words": ["PROMISE", "ETERNAL", "LIFE", "BELIEVE", "HOPE", "VICTORY", "FUTURE", "ALIVE"]},
    {"title": "What Easter Means For Me", "verse": "If you confess that Jesus is Lord and believe God raised him, you will be saved. - Romans 10:9 (WEB)",
     "p1": "The Easter story is an invitation. Jesus did not just die and rise for people long ago - He did it for YOU, personally! He knows your name, your fears, your dreams. He invites you to believe that He is alive and to follow Him. It does not require being perfect or having all the answers. It just takes an honest heart that says, 'Jesus, I believe in you. Help me live for you.'",
     "p2": "When you accept Jesus' gift of love, everything changes. Your sins are forgiven - completely! You become a child of God with eternal life. The same power that raised Jesus from the dead lives inside YOU! You have a purpose, a future, and a hope that nothing can destroy. THAT is what Easter means - not chocolate bunnies or painted eggs, but the incredible reality that LOVE conquered death, and that love is offered to every person on earth!",
     "words": ["BELIEVE", "FOLLOW", "FORGIVE", "NEW", "HEART", "LOVE", "SAVED", "YOURS"]}
]


def generate_word_search(words):
    grid=[[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)] for _ in range(10)]
    for word in words[:8]:
        word=word.upper()
        for _ in range(50):
            d=random.choice([(0,1),(1,0),(1,1)]); r=random.randint(0,max(0,9-len(word)*d[0])); c=random.randint(0,max(0,9-len(word)*d[1]))
            if r+len(word)*d[0]>10 or c+len(word)*d[1]>10: continue
            for i,ch in enumerate(word): grid[r+i*d[0]][c+i*d[1]]=ch
            break
    return grid
def wrap_text(text,mx=75):
    wds=text.split(); lines=[]; cur=""
    for w in wds:
        if len(cur)+len(w)+1<=mx: cur+=(" " if cur else "")+w
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def build_pdf():
    pdf=PDFDoc(); pc=0
    pdf.new_page(); pc+=1
    pdf.add_filled_rect(50,650,512,100,0.85)
    pdf.add_centered_text(720,TITLE,'F2',28,0); pdf.add_centered_text(690,SUBTITLE,'F4',14,0.2)
    pdf.add_centered_text(660,"Written and Illustrated by",'F4',12,0.3); pdf.add_centered_text(640,AUTHOR,'F2',16,0)
    pdf.add_rect(100,200,412,380,2,0.3)
    pdf.add_centered_text(420,"[ILLUSTRATION: Empty tomb with sunrise,",'F3',10,0.4)
    pdf.add_centered_text(405,"rolled stone, angel, and glowing light of hope]",'F3',10,0.4)
    pdf.add_centered_text(100,"The greatest love story ever told!",'F4',12,0.3)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(700,TITLE,'F2',16,0)
    pdf.add_text(72,600,f"Written by {AUTHOR}",'F4',11,0.2)
    pdf.add_text(72,580,"Copyright 2025. All Rights Reserved.",'F4',10,0.3)
    pdf.add_text(72,550,"Scripture: World English Bible (WEB) - Public Domain.",'F4',10,0.3)
    pdf.add_text(72,520,"For children ages 6-12. Published by Kingdom Kids Publishing",'F4',10,0.3)
    pdf.add_text(72,440,"Dedication: For every child who needs to know how much God loves them!",'F4',10,0.2)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"TABLE OF CONTENTS",'F2',18,0); pdf.add_line(150,720,462,720,1,0.3); y=680
    for i,ch in enumerate(chapters): pdf.add_text(72,y,f"Chapter {i+1}: {ch['title']}",'F4',12,0.1); y-=28
    pdf.add_text(72,y-10,"Quiz / Vocabulary / Journal / Certificate / Bonus",'F4',10,0.3)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(730,"HOW TO USE THIS BOOK",'F2',18,0); pdf.add_line(150,720,462,720,1,0.3)
    intro=["Welcome to the most IMPORTANT story in all of history!","This is the story of Easter - how Jesus' love saved the world.","",
        "Each chapter has SIX pages:","  1-2. The story beautifully told",
        "  3. Full-page illustration","  4. Bible verse + reflection + prayer",
        "  5. Activity (word search)","  6. Drawing page","",
        "This story has hard parts and glorious parts.","It is okay to feel sad during the cross chapters -",
        "because the RESURRECTION is coming! Just keep reading!","",
        "Easter is real. Jesus is alive. And He loves YOU!"]
    y=680
    for l in intro: pdf.add_text(72,y,l,'F4',11,0.15); y-=22


    # 10 chapters x 6 pages = 60 pages
    for idx, ch in enumerate(chapters):
        # P1: Story part 1
        pdf.new_page(); pc+=1
        pdf.add_filled_rect(50,700,512,60,0.88)
        pdf.add_centered_text(735,f"Chapter {idx+1}",'F1',10,0.4)
        pdf.add_centered_text(715,ch['title'].upper(),'F2',16,0)
        pdf.add_line(72,690,540,690,0.5,0.4); y=665
        for line in wrap_text(ch['p1'],78): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=20
        pdf.add_rect(72,y-200,468,200,1.5,0.3)
        pdf.add_centered_text(y-80,f"[ILLUSTRATION: {ch['title']}",'F3',10,0.4)
        pdf.add_centered_text(y-100,"dramatic Easter scene with emotion and light]",'F3',10,0.4)
        # P2: Story part 2
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"{ch['title']} (continued)",'F2',14,0.1)
        pdf.add_line(72,740,540,740,0.5,0.4); y=710
        for line in wrap_text(ch['p2'],78): pdf.add_text(72,y,line,'F4',11,0.1); y-=20
        y-=20
        pdf.add_filled_rect(72,y-35,468,40,0.9)
        pdf.add_centered_text(y-8,"KEY VERSE:",'F2',10,0.2)
        pdf.add_centered_text(y-25,ch['verse'],'F5',10,0)
        y-=60
        pdf.add_rect(72,y-220,468,210,1.5,0.3)
        pdf.add_centered_text(y-90,f"[ILLUSTRATION: {ch['title']} continued -",'F3',10,0.4)
        pdf.add_centered_text(y-110,"powerful emotional scene]",'F3',10,0.4)
        # P3: Full illustration
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,ch['title'].upper(),'F2',18,0)
        pdf.add_rect(50,80,512,640,2,0.3)
        pdf.add_centered_text(420,f"[FULL-PAGE ILLUSTRATION: {ch['title']}",'F3',11,0.4)
        pdf.add_centered_text(400,"detailed, emotional Easter artwork]",'F3',11,0.4)
        # P4: Reflection + Prayer
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"REFLECTION & PRAYER",'F2',16,0); pdf.add_line(150,740,462,740,1,0.3)
        pdf.add_filled_rect(72,690,468,35,0.9)
        pdf.add_centered_text(712,ch['verse'],'F5',10,0)
        qs=["1. What happened in this chapter that stands out to you?",
            "2. How does this chapter show Jesus' love?",
            "3. What does this mean for your life today?"]
        y=660
        for q in qs:
            pdf.add_text(72,y,q,'F2',10,0.1); y-=18
            for _ in range(3): pdf.add_line(90,y,530,y,0.5,0.6); y-=18
            y-=10
        pdf.add_filled_rect(72,y-100,468,110,0.92)
        pdf.add_centered_text(y-5,"MY PRAYER",'F2',12,0.1)
        pdf.add_text(80,y-22,"Dear Jesus, after reading this chapter I want to say...",'F4',10,0.2)
        for i in range(4): pdf.add_line(80,y-42-i*18,520,y-42-i*18,0.5,0.6)
        # P5: Word search
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"EASTER ACTIVITY",'F2',16,0)
        pdf.add_text(72,720,f"Word Search - {ch['title']}",'F4',11,0.2)
        grid=generate_word_search(ch['words']); y=680
        for row in grid: pdf.add_centered_text(y,"   ".join(row),'F3',14,0.1); y-=24
        y-=15; pdf.add_text(72,y,"Words: "+"  ".join(ch['words']),'F3',9,0.2)
        y-=35; pdf.add_text(72,y,"In your own words, summarize this chapter:",'F2',10,0.1)
        for _ in range(4): y-=22; pdf.add_line(72,y,540,y,0.5,0.6)
        # P6: Drawing
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,"DRAW THIS CHAPTER",'F2',16,0)
        pdf.add_text(72,720,f"Draw your picture of: {ch['title']}",'F4',11,0.2)
        pdf.add_rect(72,300,468,400,1.5,0.3)
        pdf.add_text(72,275,"What is the most important thing about this chapter?",'F2',10,0.1)
        y=250
        for _ in range(4): pdf.add_line(72,y,540,y,0.5,0.6); y-=20


    # Quiz (2 pages)
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"EASTER QUIZ - Part 1",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs=[("1. What did people wave on Palm Sunday?","a) Flags  b) Palm branches  c) Flowers"),
        ("2. What did Jesus wash at the Last Supper?","a) Dishes  b) Hands  c) Feet"),
        ("3. Where did Jesus pray before His arrest?","a) Temple  b) Gethsemane  c) Mountain"),
        ("4. Who betrayed Jesus with a kiss?","a) Peter  b) Judas  c) Thomas"),
        ("5. What did Jesus say on the cross about His enemies?","a) Punish them  b) Forgive them  c) Forget them")]
    y=700
    for q,o in qs: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"EASTER QUIZ - Part 2",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    qs2=[("6. How long was the land dark during crucifixion?","a) 1 hour  b) 3 hours  c) 6 hours"),
         ("7. Who found the empty tomb first?","a) Peter  b) The women  c) John"),
         ("8. How many days did Jesus appear after resurrection?","a) 3  b) 7  c) 40"),
         ("9. How many people saw Jesus alive at once?","a) 12  b) 100  c) Over 500"),
         ("10. What does Easter prove about death?","a) It is final  b) It is conquered  c) It is scary")]
    y=700
    for q,o in qs2: pdf.add_text(72,y,q,'F2',11,0.1); y-=22; pdf.add_text(100,y,o,'F4',10,0.2); y-=35
    pdf.add_text(72,y-20,"Answers: 1b, 2c, 3b, 4b, 5b, 6b, 7b, 8c, 9c, 10b",'F3',9,0.4)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"VOCABULARY",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    vocab=[("Resurrection","Coming back to life after dying"),("Crucifixion","Being put to death on a cross"),
           ("Salvation","Being saved from sin and death"),("Atonement","Payment for sin through sacrifice"),
           ("Redemption","Being bought back from slavery to sin"),("Gospel","The good news about Jesus"),
           ("Grace","God's undeserved love and forgiveness"),("Covenant","A sacred promise between God and people"),
           ("Hosanna","Save us! - a cry of praise"),("Eternal","Lasting forever, without end")]
    y=710
    for w,d in vocab: pdf.add_text(72,y,f"{w}:",'F2',11,0.1); pdf.add_text(210,y,d,'F4',10,0.2); y-=28

    prompts=["What the cross means to me personally...","How the resurrection gives me hope...",
             "A letter to Jesus about Easter...","How I will share the Easter story with others..."]
    for j in range(4):
        pdf.new_page(); pc+=1
        pdf.add_centered_text(750,f"MY EASTER JOURNAL - Page {j+1}",'F2',16,0)
        pdf.add_text(72,710,prompts[j],'F5',12,0.2); y=680
        for _ in range(24): pdf.add_line(72,y,540,y,0.5,0.7); y-=25

    pdf.new_page(); pc+=1
    pdf.add_rect(50,50,512,692,3,0.2); pdf.add_rect(60,60,492,672,1.5,0.4)
    pdf.add_centered_text(680,"CERTIFICATE OF COMPLETION",'F2',22,0)
    pdf.add_centered_text(640,"This certifies that",'F4',14,0.2)
    pdf.add_line(180,600,432,600,1,0.3)
    pdf.add_centered_text(540,"has read the complete Easter story in",'F4',12,0.2)
    pdf.add_centered_text(510,TITLE,'F2',16,0)
    pdf.add_centered_text(470,"and knows that Jesus is ALIVE!",'F4',12,0.2)
    pdf.add_centered_text(400,"Date: _______________",'F4',12,0.3)
    pdf.add_centered_text(280,"\"He is risen! He is risen indeed!\" - Luke 24:6",'F5',14,0.1)

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS",'F2',18,0); y=690
    for i,ch in enumerate(chapters[:5]):
        pdf.add_rect(72,y-55,468,55,1,0.3); pdf.add_text(80,y-15,f"Card {i+1}: {ch['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,ch['verse'],'F4',9,0.2); y-=65
    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MEMORY VERSE CARDS (cont.)",'F2',18,0); y=700
    for i,ch in enumerate(chapters[5:]):
        pdf.add_rect(72,y-55,468,55,1,0.3); pdf.add_text(80,y-15,f"Card {i+6}: {ch['title']}",'F2',9,0.1)
        pdf.add_text(80,y-35,ch['verse'],'F4',9,0.2); y-=65

    pdf.new_page(); pc+=1
    pdf.add_centered_text(750,"MY EASTER COMMITMENT",'F2',18,0); pdf.add_line(150,740,462,740,1,0.3)
    pdf.add_text(72,710,"Because Jesus died and rose again for me, I choose to:",'F4',11,0.2); y=680
    commitments=["Believe that Jesus is alive and loves me","Follow Jesus every day of my life",
                 "Tell others about the Easter story","Forgive people who hurt me, like Jesus forgave",
                 "Live with hope because death is defeated","Trust God even in my darkest days"]
    for c in commitments:
        pdf.add_rect(72,y-3,15,15,0.5,0.3); pdf.add_text(95,y,c,'F4',10,0.15); y-=28
    y-=20; pdf.add_text(72,y,"Name: ",'F2',11,0.1); pdf.add_line(130,y-2,400,y-2,0.5,0.6)
    y-=30; pdf.add_text(72,y,"Date: ",'F2',11,0.1); pdf.add_line(130,y-2,300,y-2,0.5,0.6)
    y-=40; pdf.add_text(72,y,"My prayer:",'F2',11,0.1); y-=22
    for _ in range(5): pdf.add_line(72,y,540,y,0.5,0.6); y-=20

    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),FILENAME)
    pdf.save(out); print(f"Generated {FILENAME} with {pc} pages"); return pc
if __name__=="__main__": build_pdf()
