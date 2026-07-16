"""Book358: Game Changers - 25 Women Athletes Who Broke Every Barrier"""
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
    athletes=[
        ("Serena Williams","Tennis","23 Grand Slam singles titles","Started on cracked public courts in Compton, California at age 4. Her father coached her with no tennis background. She faced racism and body-shaming throughout her career but became the greatest tennis player of all time with her powerful serve and fierce determination.","People called her too muscular, too aggressive, and questioned her femininity. She responded by winning everything and redefining what a champion looks like.","I really think a champion is defined not by their wins but by how they can recover when they fall.","Practice one skill for 30 minutes today, no matter how basic it seems."),
        ("Simone Biles","Gymnastics","32 Olympic and World Championship medals","Entered foster care as a young child and was adopted by her grandparents. Discovered gymnastics on a daycare field trip. Has four gymnastics moves named after her and is widely considered the greatest gymnast in history.","Faced pressure to perform despite mental health struggles. At the 2020 Olympics, she prioritized her wellbeing over medals, showing true strength means knowing your limits.","I am not the next Usain Bolt or Michael Phelps. I am the first Simone Biles.","Try a new physical challenge today. Celebrate attempting it regardless of outcome."),
        ("Megan Rapinoe","Soccer","2x World Cup Champion","Led the US Women's National Team while fighting for equal pay. She was vocal about social justice, LGBTQ+ rights, and gender equality, using her platform to demand change both on and off the field.","Faced backlash for kneeling during the national anthem and for demanding equal pay. She never backed down, eventually winning the equal pay lawsuit.","We need to be better. We have to love more and hate less.","Stand up for something you believe in today, even in a small way."),
        ("Billie Jean King","Tennis","39 Grand Slam titles","Won the famous Battle of the Sexes match against Bobby Riggs in 1973, watched by 90 million people. She fought tirelessly for equal prize money in tennis and founded the Women's Sports Foundation.","In 1973, female athletes earned a fraction of what men earned. Billie Jean proved women's sports deserved equal respect and compensation.","Champions keep playing until they get it right.","Learn about the history of women's fight for equal pay in your favorite sport."),
        ("Wilma Rudolph","Track & Field","3 Olympic Gold Medals (1960)","Had polio as a child and wore a leg brace until age 12. Doctors said she would never walk normally. She became the fastest woman in the world, winning three gold medals at the 1960 Rome Olympics.","Overcame childhood polio, poverty, and racial segregation in the American South to become an Olympic champion.","Never underestimate the power of dreams and the influence of the human spirit.","If you face a physical challenge, work around it. What CAN your body do?"),
        ("Nadia Comaneci","Gymnastics","First perfect 10 in Olympic history","At the 1976 Montreal Olympics, 14-year-old Nadia scored the first perfect 10 ever in Olympic gymnastics. The scoreboard could not display it because nobody imagined a perfect score was possible.","Growing up in communist Romania with limited resources, she trained in basic facilities yet achieved perfection on the world stage.","I do not run away from a challenge because I am afraid. I run toward it.","Set a personal standard of excellence in one activity today. Aim for YOUR best."),
        ("Mia Hamm","Soccer","2x Olympic Gold, 2x World Cup","Scored 158 international goals, a record that stood for years. She transformed women's soccer in America and proved that women's sports could draw massive audiences and inspire millions.","Played in an era when women's soccer received almost no media coverage or funding. She built the sport's popularity through sheer excellence.","I am building a fire, and every day I train I add more fuel.","Practice your sport or activity with the intensity of someone building a legacy."),
        ("Florence Griffith-Joyner","Track & Field","3 Olympic Golds, world record holder","Set the 100m and 200m world records in 1988 that STILL stand today. Known as Flo-Jo, she was as famous for her style (one-legged racing suits, long decorated nails) as for her speed.","People tried to attribute her success to drugs (she was never found to use them). She proved you can be feminine and fierce simultaneously.","When anyone tells me I can not do something, I am just not listening anymore.","Express your personal style boldly today while pursuing excellence."),
        ("Venus Williams","Tennis","7 Grand Slam singles titles","Along with sister Serena, she transformed tennis from a country club sport to one of athletic power and Black excellence. She fought for equal prize money at Wimbledon and won that battle in 2007.","Faced racism from crowds, media, and opponents throughout her career. Continued to compete at the highest level for over two decades.","I do not focus on what I am up against. I focus on my goals.","Set a goal that others might say is too ambitious. Write it down. Start."),
        ("Ronda Rousey","MMA/Wrestling","First UFC Women's Champion","Became the first American woman to earn an Olympic medal in judo, then became the first UFC Women's Bantamweight Champion. She proved that women could headline combat sports and draw massive audiences.","Was told women's fighting was not marketable and should not exist. She made it the most watched division in UFC.","I have this one term for people who are fake. I call them round people.","Do not let anyone tell you that your interest is not appropriate for your gender."),
        ("Naomi Osaka","Tennis","4 Grand Slam titles","Became the first Asian player to be ranked number one. She opened conversations about athlete mental health by withdrawing from the French Open, prioritizing her wellbeing over competition.","Faced criticism for protecting her mental health but started a global conversation about the pressure athletes face.","It is okay to not be okay.","Check in with yourself today. How are you REALLY feeling?"),
        ("Katie Ledecky","Swimming","7 Olympic Gold Medals","Dominates distance freestyle swimming like no one before her. She often finishes entire body lengths ahead of competitors. She continued competing while earning her Stanford degree.","In a sport obsessed with physical perfection, Katie wins through determination, work ethic, and love of the process.","There are no shortcuts in life or swimming. You get what you put in.","Put in extra effort on something today. Five more minutes of practice."),
        ("Chloe Kim","Snowboarding","2x Olympic Gold (halfpipe)","Won her first Olympic gold at 17, then tweeted about wanting ice cream between runs. She brought joy and authenticity to a sport that takes itself very seriously, while being the most dominant athlete in it.","As a Korean-American, she represents diversity in a predominantly white sport. She handles pressure with humor and grace.","I just want to have fun and be the best that I can be.","Approach your next challenge with joy rather than pressure."),
        ("Aly Raisman","Gymnastics","6 Olympic medals","Captain of the gold-medal US Olympic gymnastics teams in 2012 and 2016. Later became a powerful advocate for abuse survivors, speaking publicly about her experiences to protect future athletes.","Used her platform to expose abuse in gymnastics and fight for systemic change to protect young athletes.","I am not a victim. I am a survivor.","If you see something wrong, speak up. Your voice can protect others."),
        ("Misty Copeland","Ballet","First Black principal dancer at ABT","Did not start ballet until age 13 (most start at 3-4). Was told her body was wrong for ballet. She became the first African American woman to be principal dancer at American Ballet Theatre in its 75-year history.","Faced constant criticism about her body type, skin color, and late start. She transformed ballet's narrow definition of beauty.","Anything is possible when you work hard and never give up.","Start something new today regardless of whether it is the 'right' time."),
        ("Diana Taurasi","Basketball","5 Olympic Golds, 3 WNBA titles","Considered the greatest women's basketball player of all time. She played professionally for over 20 years and scored more points than any player in WNBA history.","Despite being the GOAT of women's basketball, she earns a fraction of what mediocre male players make. She advocates for pay equity.","If you think you are done, you always have at least 40 percent left.","Push beyond what you think your limit is today."),
        ("Alex Morgan","Soccer","Olympic Gold, World Cup Champion","Co-captain of the US Women's National Team and one of the faces of women's soccer worldwide. She balanced motherhood and elite competition, returning to play after having her daughter.","Fought for equal pay while performing at the highest level and becoming a mother, proving women can have both.","Be so good they cannot ignore you.","Work on your weakest skill today. That is where growth happens."),
        ("Allyson Felix","Track & Field","11 Olympic medals (most by any US track athlete)","Won more Olympic medals than any American track athlete, male or female. She advocated for better maternal protections for sponsored athletes after Nike cut her pay during pregnancy.","Her fight against Nike's treatment of pregnant athletes changed industry policy and protected future athlete-mothers.","My hustle is different. I know what I am fighting for.","Advocate for a policy change that would help others, not just yourself."),
        ("Lindsey Vonn","Skiing","Olympic Gold, 82 World Cup wins","Won more World Cup races than any female skier in history. She pushed to compete against men, believing gender should not limit athletic potential.","Suffered numerous injuries that would have ended most careers. She returned from each one to compete at the highest level.","I was told that I would never be what I wanted to be. So I went out and showed them.","Choose to be resilient today. What setback can you come back from?"),
        ("Sue Bird","Basketball","4 Olympic Golds, 4 WNBA titles","One of the greatest point guards in basketball history with one of the longest careers. She used her platform to advocate for social justice and LGBTQ+ visibility in sports.","Played at the highest level for over 20 years while being openly gay, breaking barriers for LGBTQ+ athletes.","Be who you are. It gives other people permission to do the same.","Be authentic today. Do not hide any part of who you are."),
        ("Danica Patrick","Auto Racing","First woman to lead at Indy and Daytona","The most successful woman in the history of American open-wheel and stock car racing. She led the Indianapolis 500 and won an IndyCar Series race, breaking barriers in a male-dominated sport.","Faced constant sexism and dismissal in motorsports. She earned respect through performance, not by asking for it.","I am so driven. I wish I could bottle it up and sell it.","Enter a space where you are the only girl. Own it. Belong there."),
        ("Bethany Hamilton","Surfing","Professional surfer after losing arm to shark","Lost her arm to a shark attack at age 13 and returned to professional surfing just one month later. She adapted her technique and continued to compete against two-armed surfers at the highest level.","Rather than letting a life-altering injury define her, she redefined what was possible with determination and creativity.","Courage does not mean you do not get afraid. It means you do not let fear stop you.","Face one fear today. It does not have to be big. Just face it."),
        ("Jessica Ennis-Hill","Heptathlon","Olympic Gold, World Champion","Dominated the heptathlon (seven events in two days) and won Olympic gold at her home London Olympics in 2012. She returned to win World Championship gold after becoming a mother.","Excelled at seven different athletic disciplines simultaneously while facing immense national pressure as the face of the home Olympics.","Even if you are on the right track, you will get run over if you just sit there.","Try being good at multiple things. You do not have to choose just one."),
        ("Claressa Shields","Boxing","2x Olympic Gold, undisputed champion","First American boxer (male or female) to win consecutive Olympic gold medals. She became undisputed champion in three weight classes and is considered the greatest female boxer of all time.","Grew up in Flint, Michigan amid poverty and violence. She used boxing as her way out and became the best in the world.","I believe in myself more than you could ever doubt me.","Believe in yourself more fiercely today than anyone doubts you."),
        ("Eileen Gu","Skiing/Freestyle","3 Olympic medals, youngest gold in freestyle","At 18, won gold in freeski big air with a trick she had never attempted in competition. She balances modeling, Stanford, and being the most dominant freestyle skier in the world.","Represents a new generation of multi-talented athletes who refuse to be defined by a single identity or pursuit.","Why not me? I do not think of limits.","Ask yourself 'why not me?' about something you have been wanting to try.")]


    # Build PDF
    doc.add_filled_rect(0,0,612,792,0.95)
    doc.add_centered_text(640,"GAME CHANGERS",'F2',32,0.1)
    doc.add_line(150,620,462,620,2,0.3)
    doc.add_centered_text(585,"25 Women Athletes Who Broke",'F4',16,0.3)
    doc.add_centered_text(560,"Every Barrier (Ages 8-14)",'F4',16,0.3)
    doc.add_centered_text(100,author,'F2',14,0.2)
    doc.new_page()
    doc.add_centered_text(700,"GAME CHANGERS",'F2',14,0.2)
    doc.add_text(72,650,f"Author: {author}",'F1',11,0.3)
    doc.add_text(72,630,"Format: 8.5 x 11 inches | Kindle & Paperback",'F1',10,0.4)
    doc.add_text(72,600,"All rights reserved.",'F1',10,0.4)
    doc.new_page()
    # TOC
    doc.add_centered_text(720,"TABLE OF CONTENTS",'F2',18,0.1)
    doc.add_line(72,705,540,705,1,0.3)
    y=680
    for i,(n,s,_,_,_,_,_) in enumerate(athletes):
        if y<80:doc.new_page();y=740
        doc.add_text(72,y,f"{i+1}. {n} - {s}",'F1',10,0.2);y-=17
    doc.new_page()

    for i,(name,sport,records,story,discrimination,quote,challenge) in enumerate(athletes):
        # Page 1
        doc.add_filled_rect(50,710,512,50,0.92)
        doc.add_centered_text(740,f"Athlete #{i+1} | {sport}",'F1',10,0.5)
        doc.add_centered_text(720,name.upper(),'F2',18,0.1)
        doc.add_centered_text(695,records,'F4',10,0.4)
        doc.add_text(72,665,"HER STORY",'F2',12,0.2)
        y=648
        for ln in wrap(story,80):
            doc.add_text(72,y,ln,'F4',11,0.2);y-=15
        y-=15
        doc.add_text(72,y,"HOW SHE CHANGED THE GAME",'F2',11,0.2);y-=15
        for ln in wrap(discrimination,80):
            doc.add_text(72,y,ln,'F1',10,0.25);y-=14
        y-=15
        doc.add_filled_rect(72,y-10,468,30,0.93)
        doc.add_centered_text(y+5,f'"{quote}"','F5',10,0.2)
        doc.new_page()
        # Page 2
        doc.add_centered_text(740,f"{name} - Your Sports Challenge",'F2',14,0.2)
        doc.add_line(72,725,540,725,1,0.3)
        doc.add_text(72,700,"YOUR CHALLENGE:",'F2',11,0.2)
        y=680
        for ln in wrap(challenge,80):
            doc.add_text(82,y,ln,'F4',11,0.3);y-=15
        y-=20
        doc.add_text(72,y,"What I admire most about this athlete:",'F2',10,0.3);y-=18
        for j in range(4):
            doc.add_line(72,y,540,y,0.5,0.7);y-=22
        y-=10
        doc.add_text(72,y,"How she inspires my own athletic goals:",'F2',10,0.3);y-=18
        for j in range(4):
            doc.add_line(72,y,540,y,0.5,0.7);y-=22
        doc.new_page()
        # Page 3
        doc.add_centered_text(740,f"{name} - Reflection",'F2',14,0.2)
        doc.add_line(72,725,540,725,1,0.3)
        doc.add_text(72,700,"My sports/fitness goals inspired by this athlete:",'F4',11,0.3)
        y=678
        for j in range(10):
            doc.add_line(72,y,540,y,0.5,0.7);y-=22
        doc.new_page()

    doc.add_centered_text(600,"GAME ON!",'F2',24,0.1)
    doc.add_centered_text(560,"Play hard. Break barriers. Change the game.",'F4',13,0.3)
    doc.new_page()
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book358_Women_In_Sports.pdf')
    print("Book358_Women_In_Sports.pdf created successfully!")

if __name__=="__main__":
    create_book()
