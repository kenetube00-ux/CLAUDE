from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    events = [
        ("Ancient Egypt & the Pyramids", "3000 BC", "Imagine building a 50-story structure with NO machines, NO electricity, and NO computers! That's exactly what the ancient Egyptians did. The Great Pyramid of Giza took 20 years and 100,000 workers. They invented paper (papyrus), writing (hieroglyphics), and advanced mathematics. Egyptian civilization lasted over 3,000 years!", "pyramid, pharaoh, hieroglyphics, papyrus, Nile", "Without Egypt, we might not have paper, geometry, or calendars."),
        ("Greek Democracy", "500 BC", "In ancient Athens, citizens could directly vote on laws. This was the world's first democracy! Before this, kings and dictators made all decisions. The Greeks also gave us the Olympics, philosophy (love of wisdom), theater, and the foundations of science and math. Socrates, Plato, and Aristotle shaped how we think.", "democracy, philosophy, citizen, vote, Athens", "Without Greek democracy, modern governments might all be dictatorships."),
        ("The Roman Empire", "27 BC - 476 AD", "Rome started as a tiny village and grew into the largest empire the Western world had ever seen. Romans built incredible roads (50,000 miles!), aqueducts, concrete buildings, and legal systems. Their language (Latin) evolved into Italian, Spanish, French, Portuguese, and Romanian. Roman engineering still influences us today.", "empire, republic, senate, gladiator, aqueduct", "Without Rome, we might not have roads, sewers, or modern legal systems."),
        ("The Silk Road", "130 BC - 1453 AD", "The Silk Road wasn't one road - it was a network of trade routes connecting China to Europe across 4,000 miles! Traders carried silk, spices, paper, and gunpowder. But they also carried IDEAS: religions, languages, inventions, and cultures mixed along these routes, creating a connected ancient world.", "trade, merchant, caravan, silk, spice", "Without the Silk Road, ideas and inventions would have spread much slower."),
        ("The Printing Press", "1440", "Before Gutenberg's printing press, books were copied BY HAND - taking months per book! The press could print thousands of copies quickly and cheaply. Suddenly, common people could read and learn. This led to the Scientific Revolution, the Reformation, and eventually the Enlightenment. Knowledge was no longer just for the rich.", "printing press, Gutenberg, literacy, book, knowledge", "Without the printing press, most people today would still be unable to read."),
        ("Age of Exploration", "1492", "When Columbus sailed across the Atlantic, he connected two worlds that didn't know each other existed. Soon, Europeans explored the Americas, Africa, and Asia. This brought trade and cultural exchange BUT also colonization, slavery, and disease that devastated indigenous populations. History is complicated.", "exploration, navigation, colony, indigenous, trade", "This permanently connected the Eastern and Western hemispheres."),
        ("The American Revolution", "1776", "Thirteen colonies declared independence from the most powerful empire on Earth - and won! The Declaration of Independence declared that all people have rights to life, liberty, and the pursuit of happiness. This inspired revolutions worldwide and created a new form of democratic government.", "revolution, independence, constitution, liberty, democracy", "Without this, the concept of government by the people might have died."),
        ("The French Revolution", "1789", "French citizens, starving while royalty feasted, overthrew their king. They declared that all men are equal with rights to freedom. Though the revolution turned violent, its ideas - liberty, equality, fraternity - spread across Europe and inspired democratic movements worldwide.", "revolution, guillotine, equality, citizen, rights", "This event ended the era of absolute monarchies in Europe."),
        ("The Industrial Revolution", "1760-1840", "Machines replaced hand labor. Factories replaced workshops. Cities replaced farming villages. Steam power, textile mills, and iron production transformed how humans live and work. For the first time, products could be made quickly and cheaply. But it also brought pollution, child labor, and inequality.", "factory, steam engine, manufacturing, urbanization, labor", "Without industrialization, we'd still make everything by hand."),
        ("Abolition of Slavery", "1807-1865", "For centuries, millions of Africans were kidnapped and forced into slavery. Abolitionists fought for decades to end this horror. Britain banned the slave trade in 1807. The US Civil War (1861-1865) ended American slavery. But the fight for racial equality continues to this day.", "abolition, slavery, freedom, emancipation, civil war", "This proved that terrible injustices CAN be overcome through persistence."),
        ("World War I", "1914-1918", "Called 'The Great War' and 'The War to End All Wars,' WWI involved 30+ countries and killed 20 million people. New weapons (machine guns, poison gas, tanks) made it devastating. The war redrew maps, collapsed empires, and set the stage for an even worse conflict 20 years later.", "trench, alliance, armistice, empire, weapon", "WWI showed that modern weapons made war far more destructive."),
        ("Women's Right to Vote", "1920 (US)", "For most of history, women couldn't vote, own property, or attend university. Suffragists marched, were arrested, went on hunger strikes, and fought for decades. The 19th Amendment gave American women the vote in 1920. Other countries followed. Today, women lead nations.", "suffrage, equality, vote, movement, amendment", "Without suffragists, half the population might still have no political voice."),
        ("World War II", "1939-1945", "The deadliest conflict in history killed 70-85 million people. Nazi Germany's Holocaust murdered 6 million Jews. The war ended with atomic bombs on Japan. From this horror came the United Nations, the Universal Declaration of Human Rights, and a determination: Never again.", "Holocaust, atomic bomb, D-Day, allies, fascism", "WWII created the international system designed to prevent future world wars."),
        ("Moon Landing", "1969", "On July 20, 1969, Neil Armstrong became the first human to walk on the Moon. '600 million people watched on TV as he said: That is one small step for man, one giant leap for mankind.' This proved humans can achieve the seemingly impossible when they work together.", "Apollo 11, astronaut, NASA, rocket, lunar", "This was arguably humanity's greatest technological achievement."),
        ("Civil Rights Movement", "1950s-1960s", "In America, Black people were segregated - forced to use separate schools, restaurants, and water fountains. Dr. Martin Luther King Jr. led peaceful protests demanding equal rights. The Civil Rights Act (1964) banned discrimination. Rosa Parks, the Freedom Riders, and millions of brave activists changed America.", "segregation, equality, protest, rights, peaceful", "This proved that nonviolent resistance can change unjust laws."),
        ("Fall of the Berlin Wall", "1989", "After WWII, Germany was split in two. East Germany built a wall through Berlin to stop people from escaping to freedom. For 28 years, families were separated. When the wall fell on November 9, 1989, it symbolized the end of the Cold War and the triumph of freedom.", "Cold War, communism, freedom, reunification, wall", "Without this moment, Europe might still be divided by ideology."),
        ("The Internet Revolution", "1991", "When the World Wide Web launched, nobody could have predicted how completely it would transform human civilization. Today, over 5 billion people use the internet. It changed how we communicate, learn, shop, work, and connect. Information that once took weeks to find is now available in seconds.", "internet, web, digital, connection, information", "The internet may be the most transformative invention since the printing press."),
        ("September 11, 2001", "2001", "Terrorist attacks on the World Trade Center and Pentagon killed nearly 3,000 people. This day changed global politics, airport security, and how nations fight terrorism. It showed both the worst of humanity (the attackers) and the best (the first responders who ran toward danger to save others).", "terrorism, security, heroes, first responders, unity", "This event reshaped global security and international relations."),
        ("The Smartphone Era", "2007", "When Apple released the iPhone in 2007, it put a powerful computer in everyone's pocket. Smartphones changed communication, photography, navigation, entertainment, and business. Today, most of the world carries more computing power in their hand than existed on the entire planet in 1960.", "smartphone, app, technology, mobile, communication", "Smartphones put the entire world's knowledge in your pocket."),
        ("Climate Awareness Movement", "2018-present", "Young people are leading the fight against climate change! Greta Thunberg, who was 15, started a global movement by skipping school to protest. Millions of students worldwide joined. Your generation understands that protecting the planet is the most important challenge of our time.", "climate, protest, environment, sustainability, youth", "Young people are proving that age doesn't limit your ability to change the world."),
        ("The Rise of AI", "2022-present", "Artificial Intelligence exploded into public awareness with tools like ChatGPT. AI can write, create art, drive cars, diagnose diseases, and more. This technology will reshape nearly every job and industry. Your generation will decide how to use AI wisely and ethically.", "artificial intelligence, technology, automation, ethics, future", "AI may be as transformative as electricity or the internet."),
        ("COVID-19 Pandemic", "2020-2022", "A virus spread across the entire world, changing everything overnight. Schools closed, people worked from home, and scientists created vaccines in record time. The pandemic showed how connected our world is - and how quickly humans can adapt and innovate when they must.", "pandemic, vaccine, quarantine, adaptation, science", "This showed both human vulnerability and our incredible ability to adapt."),
        ("Space Exploration's New Era", "2020s", "Private companies like SpaceX are making space travel cheaper and more accessible. NASA is returning to the Moon. Mars missions are being planned. Space tourism has begun. The kids reading this book might be the generation that lives on another planet!", "SpaceX, Mars, tourism, private space, future", "Space exploration is no longer just for governments - it's for everyone."),
        ("The Information Age", "1990s-present", "We live in the Information Age - a time when knowledge is power and it's everywhere. The ability to learn anything, connect with anyone, and create something from nothing is at your fingertips. But with great power comes great responsibility: knowing what's true matters more than ever.", "information, knowledge, media literacy, critical thinking", "Learning to think critically about information may be the most important skill today."),
        ("Your Place in History", "NOW!", "History isn't just something that happened in the past - it's happening RIGHT NOW, and YOU are part of it! The events you experience, the choices you make, and the problems you solve will be studied by future generations. What mark will you leave on history?", "future, legacy, impact, choice, action", "YOU are making history every single day. Make it count!"),
    ]

    title_page(doc, "HISTORY'S GREATEST STORIES FOR KIDS", "25 Events That Changed the World (Ages 9-14)", "25 Events * Narratives * Timelines * Discussion Questions")
    copyright_page(doc, "HISTORY'S GREATEST STORIES FOR KIDS")
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0)
    doc.add_line(180, 710, 432, 710, 1, 0.3)
    y = 685
    for i, (title, date, _, _, _) in enumerate(events):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "TABLE OF CONTENTS (continued)", 'F2', 16, 0)
            y = 690
        doc.add_text(72, y, f"{i+1}. {title} ({date})", 'F4', 11, 0.2)
        y -= 22
    doc.new_page()

    for idx, (title, date, narrative, vocab, what_if) in enumerate(events):
        # Event page 1
        chapter_header(doc, idx+1, title, f"Date: {date}")
        y = 580
        doc.add_text(72, y, "THE STORY:", 'F2', 13, 0.1)
        y -= 20
        y = add_wrapped(doc, 72, y, narrative, 'F1', 11, 0.2)
        
        y -= 25
        doc.add_text(72, y, "KEY VOCABULARY:", 'F2', 12, 0.1)
        y -= 18
        doc.add_text(90, y, vocab, 'F3', 10, 0.3)
        doc.new_page()

        # Event page 2
        doc.add_centered_text(720, f"EVENT {idx+1}: THINK DEEPER", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        
        doc.add_text(72, 680, "WHAT IF IT HADN'T HAPPENED?", 'F2', 13, 0.1)
        y = add_wrapped(doc, 90, 658, what_if, 'F4', 11, 0.3)
        
        y -= 30
        doc.add_text(72, y, "DISCUSSION QUESTIONS:", 'F2', 13, 0.1)
        y -= 20
        questions = [
            "Why do you think this event was so important?",
            "How does this event still affect your life today?",
            "What can we learn from this to make the future better?",
        ]
        for q in questions:
            doc.add_text(90, y, f"* {q}", 'F1', 11, 0.2)
            y -= 20

        y -= 20
        doc.add_text(72, y, "TIMELINE PLACEMENT:", 'F2', 12, 0.1)
        y -= 20
        doc.add_line(90, y, 530, y, 1, 0.3)
        doc.add_text(90, y-15, "Past", 'F1', 9, 0.4)
        doc.add_text(500, y-15, "Present", 'F1', 9, 0.4)
        doc.add_text(280, y+10, f"* {date}", 'F2', 10, 0.1)

        y -= 50
        doc.add_text(72, y, "MY THOUGHTS:", 'F2', 12, 0.1)
        y -= 20
        for _ in range(4):
            doc.add_text(90, y, "___________________________________________________________", 'F1', 10, 0.4)
            y -= 20
        doc.new_page()

    # Timeline overview
    doc.add_centered_text(720, "COMPLETE TIMELINE", 'F2', 18, 0)
    y = 690
    for i, (title, date, _, _, _) in enumerate(events):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "TIMELINE (continued)", 'F2', 16, 0)
            y = 690
        doc.add_text(72, y, f"{date:>12s}", 'F3', 9, 0.3)
        doc.add_text(160, y, f"{title}", 'F1', 10, 0.2)
        y -= 20
    doc.new_page()

    certificate(doc, "YOUNG HISTORIAN CERTIFICATE")
    add_supplemental(doc, 'History', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book333_Kids_World_History.pdf')
    print("Book333_Kids_World_History.pdf created successfully!")

if __name__ == "__main__":
    create_book()
