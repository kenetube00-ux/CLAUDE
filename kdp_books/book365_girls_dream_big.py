"""Book365: Dream Big, Girl! - Goal-Setting & Manifestation Journal"""
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

    # Title page
    doc.add_filled_rect(0,0,612,792,0.95)
    doc.add_centered_text(640,"DREAM BIG, GIRL!",'F2',30,0.1)
    doc.add_line(150,620,462,620,2,0.3)
    doc.add_centered_text(585,"A Goal-Setting & Manifestation Journal",'F4',15,0.3)
    doc.add_centered_text(560,"for Girls Ages 10-15",'F4',15,0.3)
    doc.add_centered_text(100,author,'F2',14,0.2)
    doc.new_page()
    doc.add_centered_text(700,"DREAM BIG, GIRL!",'F2',14,0.2)
    doc.add_text(72,650,f"Author: {author}",'F1',11,0.3)
    doc.add_text(72,630,"Format: 8.5 x 11 inches | Kindle & Paperback",'F1',10,0.4)
    doc.add_text(72,600,"All rights reserved.",'F1',10,0.4)
    doc.new_page()
    # TOC
    doc.add_centered_text(720,"TABLE OF CONTENTS",'F2',18,0.1)
    doc.add_line(72,705,540,705,1,0.3)
    sections=["Vision Board Planning (5 pages)","Goal-Setting Framework (5 pages)","Monthly Goals - January through December (48 pages)","Year-End Review (5 pages)","Dream Journal (10 pages)","Affirmation Cards (3 pages)","Letter to Future Me (2 pages)","Certificate of Achievement (1 page)"]
    y=680
    for s in sections:
        doc.add_text(72,y,f"- {s}",'F1',12,0.2);y-=22
    doc.new_page()

    # VISION BOARD PLANNING (5 pages)
    doc.add_centered_text(720,"VISION BOARD PLANNING",'F2',20,0.1)
    doc.add_line(150,705,462,705,1,0.3)
    intro="A vision board is a visual representation of your dreams and goals. It helps your brain focus on what you want to create in your life. When you see your goals every day, your subconscious mind works toward them even when you are not actively thinking about it."
    y=680
    for ln in wrap(intro,80):
        doc.add_text(72,y,ln,'F4',11,0.2);y-=15
    y-=15
    doc.add_text(72,y,"CATEGORIES FOR YOUR VISION BOARD:",'F2',12,0.2);y-=18
    cats=["Education & Learning","Health & Body","Friendships & Relationships","Creativity & Hobbies","Career & Purpose","Travel & Experiences","Personal Growth","Giving Back"]
    for cat in cats:
        doc.add_text(92,y,f"- {cat}",'F1',11,0.3);y-=16
    doc.new_page()

    for pg in range(4):
        doc.add_centered_text(740,"VISION BOARD BRAINSTORM",'F2',14,0.2)
        doc.add_line(72,725,540,725,1,0.3)
        prompts_vb=[
            ("My dream life looks like:","Describe in detail your ideal future."),
            ("Images I want to find:","What pictures represent my dreams?"),
            ("Words and quotes that inspire me:","What phrases fire me up?"),
            ("People who represent my goals:","Who has the life I want to build?")]
        p=prompts_vb[pg]
        doc.add_text(72,700,p[0],'F2',12,0.2)
        doc.add_text(72,682,p[1],'F4',10,0.4)
        y=660
        for j in range(16):
            doc.add_line(72,y,540,y,0.5,0.7);y-=22
        doc.new_page()

    # GOAL-SETTING FRAMEWORK (5 pages)
    doc.add_centered_text(720,"GOAL-SETTING FRAMEWORK",'F2',20,0.1)
    doc.add_line(150,705,462,705,1,0.3)
    framework="Great goals are SMART: Specific (exactly what you want), Measurable (how you will track progress), Achievable (challenging but possible), Relevant (matters to YOU not others), and Time-bound (has a deadline). This framework turns wishes into plans."
    y=680
    for ln in wrap(framework,80):
        doc.add_text(72,y,ln,'F4',11,0.2);y-=15
    y-=20
    doc.add_text(72,y,"MY BIG DREAMS (no filter, no limits):",'F2',12,0.2);y-=18
    for j in range(8):
        doc.add_text(72,y,f"{j+1}.",'F1',10,0.3)
        doc.add_line(92,y,540,y,0.5,0.7);y-=22
    doc.new_page()

    # More framework pages
    for area in ["EDUCATION GOALS","HEALTH & WELLNESS GOALS","RELATIONSHIP GOALS","CREATIVITY GOALS"]:
        doc.add_centered_text(740,area,'F2',14,0.2)
        doc.add_line(72,725,540,725,1,0.3)
        doc.add_text(72,700,"My SMART goal:",'F2',11,0.2)
        doc.add_line(72,680,540,680,0.5,0.7)
        doc.add_text(72,655,"Why this matters to me:",'F2',11,0.2)
        doc.add_line(72,635,540,635,0.5,0.7)
        doc.add_text(72,610,"Steps to achieve it:",'F2',11,0.2)
        y=590
        for j in range(5):
            doc.add_text(72,y,f"Step {j+1}:",'F1',10,0.3);doc.add_line(120,y,540,y,0.5,0.7);y-=22
        doc.add_text(72,y,"Deadline:",'F2',10,0.3);doc.add_line(130,y,300,y,0.5,0.7);y-=25
        doc.add_text(72,y,"How I will celebrate achieving this:",'F2',10,0.3);y-=18
        doc.add_line(72,y,540,y,0.5,0.7)
        doc.new_page()

    # MONTHLY GOALS (12 months x 4 pages = 48 pages)
    month_names=["January","February","March","April","May","June","July","August","September","October","November","December"]
    for m_idx,month in enumerate(month_names):
        # Page 1: Monthly goal
        doc.add_filled_rect(50,720,512,45,0.92)
        doc.add_centered_text(748,f"Month {m_idx+1}",'F1',9,0.5)
        doc.add_centered_text(730,month.upper(),'F2',18,0.1)
        doc.add_text(72,695,"THIS MONTH'S BIG GOAL:",'F2',12,0.2)
        doc.add_line(72,675,540,675,0.5,0.5)
        doc.add_line(72,650,540,650,0.5,0.5)
        doc.add_text(72,625,"Why this goal matters to me:",'F2',10,0.3)
        doc.add_line(72,605,540,605,0.5,0.7)
        doc.add_text(72,580,"What success looks like:",'F2',10,0.3)
        doc.add_line(72,560,540,560,0.5,0.7)
        doc.add_text(72,535,"Potential obstacles:",'F2',10,0.3)
        doc.add_line(72,515,540,515,0.5,0.7)
        doc.add_text(72,490,"My plan to overcome them:",'F2',10,0.3)
        doc.add_line(72,470,540,470,0.5,0.7)
        doc.new_page()
        # Page 2: Weekly action steps
        doc.add_centered_text(740,f"{month} - Weekly Action Steps",'F2',14,0.2)
        doc.add_line(72,725,540,725,1,0.3)
        for wk in range(1,5):
            y_start=725-wk*150
            doc.add_text(72,y_start,f"WEEK {wk}:",'F2',11,0.2)
            doc.add_text(72,y_start-16,"Action step:",'F1',10,0.3)
            doc.add_line(160,y_start-16,540,y_start-16,0.5,0.7)
            doc.add_text(72,y_start-36,"Done? [ ] Yes  [ ] No  Progress: ___/10",'F1',10,0.4)
            doc.add_text(72,y_start-56,"Notes:",'F1',10,0.3)
            doc.add_line(120,y_start-56,540,y_start-56,0.5,0.7)
        doc.new_page()
        # Page 3: Reflection
        doc.add_centered_text(740,f"{month} - Monthly Reflection",'F2',14,0.2)
        doc.add_line(72,725,540,725,1,0.3)
        doc.add_text(72,700,"Did I achieve my goal? [ ] Yes [ ] Partially [ ] Not yet",'F1',11,0.3)
        doc.add_text(72,675,"What went well:",'F2',10,0.3)
        y=655
        for j in range(3):
            doc.add_line(72,y,540,y,0.5,0.7);y-=22
        doc.add_text(72,y,"What I learned:",'F2',10,0.3);y-=18
        for j in range(3):
            doc.add_line(72,y,540,y,0.5,0.7);y-=22
        doc.add_text(72,y,"What I will do differently next month:",'F2',10,0.3);y-=18
        for j in range(3):
            doc.add_line(72,y,540,y,0.5,0.7);y-=22
        doc.new_page()
        # Page 4: Celebration
        doc.add_centered_text(740,f"{month} - Celebrate!",'F2',14,0.2)
        doc.add_line(72,725,540,725,1,0.3)
        doc.add_text(72,700,"Wins this month (big and small):",'F2',11,0.2)
        y=678
        for j in range(5):
            doc.add_text(72,y,f"{j+1}.",'F1',10,0.3);doc.add_line(92,y,540,y,0.5,0.7);y-=22
        y-=10
        doc.add_text(72,y,"How I am celebrating:",'F2',10,0.3);y-=18
        doc.add_line(72,y,540,y,0.5,0.7);y-=25
        doc.add_text(72,y,"Gratitude for this month:",'F2',10,0.3);y-=18
        for j in range(3):
            doc.add_line(72,y,540,y,0.5,0.7);y-=22
        doc.add_filled_rect(72,y-5,468,25,0.93)
        doc.add_centered_text(y+5,"Every step forward counts. Keep going, girl!",'F5',10,0.2)
        doc.new_page()


    # YEAR-END REVIEW (5 pages)
    doc.add_centered_text(720,"YEAR-END REVIEW",'F2',20,0.1)
    doc.add_line(150,705,462,705,1,0.3)
    doc.add_text(72,680,"Look back at your year of goal-setting. Celebrate how far you have come!",'F4',12,0.3)
    doc.add_text(72,650,"Goals I ACHIEVED:",'F2',12,0.2)
    y=630
    for j in range(5):
        doc.add_line(72,y,540,y,0.5,0.7);y-=22
    doc.add_text(72,y,"Goals still in progress:",'F2',12,0.2);y-=18
    for j in range(3):
        doc.add_line(72,y,540,y,0.5,0.7);y-=22
    doc.add_text(72,y,"Biggest surprise of the year:",'F2',12,0.2);y-=18
    doc.add_line(72,y,540,y,0.5,0.7)
    doc.new_page()
    for pg in range(4):
        titles_yr=["My Biggest Growth This Year","Obstacles I Overcame","What I Am Most Proud Of","Goals for Next Year"]
        doc.add_centered_text(740,titles_yr[pg],'F2',14,0.2)
        doc.add_line(72,725,540,725,1,0.3)
        y=700
        for j in range(18):
            doc.add_line(72,y,540,y,0.5,0.7);y-=22
        doc.new_page()

    # DREAM JOURNAL (10 pages)
    doc.add_centered_text(720,"DREAM JOURNAL",'F2',20,0.1)
    doc.add_line(150,705,462,705,1,0.3)
    doc.add_text(72,680,"Use these pages to write freely about your biggest dreams.",'F4',12,0.3)
    doc.add_text(72,655,"No limits. No judgment. Just pure imagination.",'F4',12,0.3)
    doc.new_page()
    for pg in range(9):
        doc.add_centered_text(750,"Dream Journal",'F2',12,0.3)
        y=725
        for j in range(22):
            doc.add_line(72,y,540,y,0.5,0.75);y-=25
        doc.new_page()

    # AFFIRMATION CARDS (3 pages)
    doc.add_centered_text(720,"AFFIRMATION CARDS",'F2',18,0.1)
    doc.add_line(150,705,462,705,1,0.3)
    doc.add_text(72,680,"Cut these out and place where you will see them daily:",'F4',11,0.3)
    affs=["I am capable of achieving anything I set my mind to.","My dreams are valid and worth pursuing.","I am brave enough to try new things.","Failure is just feedback. I learn and grow.","I deserve success and happiness.","My unique gifts make the world better.","I am worthy of my biggest dreams.","Every day I get closer to my goals.","I trust myself to make good decisions.","Obstacles make me stronger and smarter.","I am the author of my own story.","My potential is limitless."]
    y=655
    for j,aff in enumerate(affs):
        doc.add_rect(72,y-5,468,22,0.5,0.3)
        doc.add_centered_text(y+3,aff,'F5',10,0.2)
        y-=28
        if y<80:
            doc.new_page()
            doc.add_centered_text(740,"AFFIRMATION CARDS (cont.)",'F2',14,0.2)
            y=710
    doc.new_page()

    # Extra affirmation page
    doc.add_centered_text(740,"CREATE YOUR OWN AFFIRMATIONS",'F2',14,0.2)
    doc.add_line(72,725,540,725,1,0.3)
    y=700
    for j in range(10):
        doc.add_rect(72,y-5,468,22,0.5,0.3)
        y-=28
    doc.new_page()

    # LETTER TO FUTURE ME (2 pages)
    doc.add_centered_text(720,"LETTER TO FUTURE ME",'F2',18,0.1)
    doc.add_line(150,705,462,705,1,0.3)
    doc.add_text(72,680,"Write a letter to yourself 5 years from now:",'F4',12,0.3)
    doc.add_text(72,660,"Dear Future Me,",'F5',12,0.2)
    y=640
    for j in range(18):
        doc.add_line(72,y,540,y,0.5,0.7);y-=22
    doc.new_page()
    doc.add_centered_text(750,"Letter to Future Me (continued)",'F2',12,0.3)
    y=725
    for j in range(18):
        doc.add_line(72,y,540,y,0.5,0.7);y-=22
    doc.add_text(72,y,"With love and belief,  ___________________",'F4',12,0.3)
    y-=20
    doc.add_text(72,y,"Date: ___/___/___    Seal and open on: ___/___/___",'F1',10,0.4)
    doc.new_page()

    # CERTIFICATE
    doc.add_rect(50,100,512,600,2,0.2)
    doc.add_rect(60,110,492,580,1,0.4)
    doc.add_centered_text(620,"CERTIFICATE OF ACHIEVEMENT",'F2',22,0.1)
    doc.add_line(150,600,462,600,1.5,0.3)
    doc.add_centered_text(560,"This certifies that",'F4',14,0.3)
    doc.add_line(200,530,412,530,0.5,0.4)
    doc.add_centered_text(515,"(your name)",'F1',9,0.5)
    doc.add_centered_text(480,"has completed the Dream Big, Girl! journal",'F4',13,0.3)
    doc.add_centered_text(455,"and demonstrated extraordinary courage,",'F4',13,0.3)
    doc.add_centered_text(430,"determination, and commitment to her dreams.",'F4',13,0.3)
    doc.add_centered_text(380,"SHE IS UNSTOPPABLE.",'F2',16,0.1)
    doc.add_text(150,320,"Date: _______________",'F1',11,0.3)
    doc.add_text(350,320,"Signature: _______________",'F1',11,0.3)
    doc.add_centered_text(260,"Dream big. Work hard. Never give up.",'F5',12,0.3)
    doc.new_page()

    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book365_Girls_Dream_Big.pdf')
    print("Book365_Girls_Dream_Big.pdf created successfully!")

if __name__=="__main__":
    create_book()
