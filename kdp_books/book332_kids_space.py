from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    chapters = [
        ("Our Sun", [
            "The Sun is a STAR - the closest star to Earth, about 93 million miles away.",
            "It's so big that 1.3 million Earths could fit inside it!",
            "The Sun is about 4.6 billion years old - middle-aged for a star.",
            "Its surface temperature is about 10,000 degrees Fahrenheit.",
            "The core is even hotter: 27 MILLION degrees Fahrenheit!",
            "Light from the Sun takes 8 minutes and 20 seconds to reach Earth.",
            "The Sun is made mostly of hydrogen (73%) and helium (25%).",
            "Without the Sun, Earth would be a frozen, lifeless rock in space.",
            "The Sun will keep shining for about 5 billion more years.",
            "Solar flares from the Sun can disrupt electronics on Earth!",
        ], "If the Sun were a basketball, Earth would be the size of a grain of sand 100 feet away!"),
        ("Mercury & Venus", [
            "Mercury is the smallest planet and closest to the Sun.",
            "A day on Mercury (sunrise to sunrise) is 176 Earth days long!",
            "Mercury has almost no atmosphere - no protection from meteors.",
            "Temperatures swing from 800F (day) to -290F (night) on Mercury.",
            "Venus is Earth's 'twin' in size but NOTHING like Earth otherwise.",
            "Venus spins BACKWARDS compared to other planets.",
            "Venus is the hottest planet (900F) even though Mercury is closer to the Sun.",
            "Venus has crushing atmospheric pressure: 90x Earth's surface pressure.",
            "It rains sulfuric acid on Venus! (But it evaporates before hitting ground.)",
            "A year on Venus is shorter than a day on Venus!",
        ], "Venus is sometimes called Earth's evil twin - similar size but incredibly hostile to life!"),
        ("Earth & Moon", [
            "Earth is the only known planet with liquid water on its surface.",
            "Our atmosphere is 78% nitrogen, 21% oxygen, and 1% other gases.",
            "Earth's core is as hot as the surface of the Sun!",
            "The Moon is about 238,900 miles from Earth.",
            "The Moon's gravity causes our ocean tides.",
            "We always see the same side of the Moon (it's tidally locked).",
            "The Moon has no atmosphere, so footprints there last forever!",
            "Earth is the densest planet in our solar system.",
            "Our magnetic field protects us from deadly solar radiation.",
            "The Moon is slowly drifting away from Earth (1.5 inches per year).",
        ], "If Earth were the size of a basketball, the Moon would be a tennis ball 24 feet away!"),
        ("Mars: The Red Planet", [
            "Mars appears red because its surface is covered in iron oxide (rust).",
            "Mars has the largest volcano in the solar system: Olympus Mons (3x taller than Everest).",
            "A day on Mars is just 37 minutes longer than an Earth day.",
            "Mars has two tiny moons: Phobos and Deimos (Fear and Terror).",
            "Mars once had liquid water - scientists found dried-up river beds!",
            "Temperatures on Mars average about -80F (very cold!).",
            "Mars has seasons, ice caps, and dust storms that cover the entire planet.",
            "Multiple rovers (Curiosity, Perseverance) are exploring Mars right now.",
            "SpaceX and NASA plan to send humans to Mars in the 2030s.",
            "A year on Mars is about 687 Earth days.",
        ], "Mars is the most likely planet for humans to visit next. Would YOU go?"),
        ("Jupiter: King of Planets", [
            "Jupiter is so large that ALL other planets could fit inside it!",
            "The Great Red Spot is a storm bigger than Earth that has raged for 400+ years.",
            "Jupiter has at least 95 known moons!",
            "Europa (a Jupiter moon) may have a liquid ocean under its icy surface.",
            "Jupiter's magnetic field is 20,000x stronger than Earth's.",
            "A day on Jupiter is only about 10 hours (fastest spinning planet).",
            "Jupiter is mostly gas - it has no solid surface to land on.",
            "Jupiter protects Earth by catching asteroids with its huge gravity.",
            "You would weigh 2.5x more on Jupiter than on Earth.",
            "Jupiter gives off more heat than it receives from the Sun!",
        ], "Jupiter is like a giant vacuum cleaner, pulling in space rocks that might otherwise hit Earth!"),
        ("Saturn: Lord of the Rings", [
            "Saturn's rings are made of billions of pieces of ice and rock.",
            "The rings are incredibly thin - only about 30 feet thick!",
            "Saturn could float in water (if you had a big enough bathtub) - it's less dense than water.",
            "Saturn has 146 known moons (more than any other planet).",
            "Titan (Saturn's largest moon) has lakes of liquid methane.",
            "Wind speeds on Saturn can reach 1,100 mph!",
            "Saturn's rings stretch 175,000 miles wide.",
            "A year on Saturn equals 29.5 Earth years.",
            "Saturn is the flattest planet - it bulges at the equator from fast spinning.",
            "You can see Saturn's rings with a basic backyard telescope!",
        ], "Saturn's rings look solid from far away but are actually millions of separate pieces orbiting together!"),
        ("Uranus & Neptune", [
            "Uranus rotates on its SIDE - it's basically rolling around the Sun!",
            "Uranus is called an 'ice giant' (different from gas giants like Jupiter).",
            "Neptune has the strongest winds: up to 1,200 mph!",
            "Neptune was predicted by math before it was ever seen through a telescope.",
            "A year on Neptune is 165 Earth years long.",
            "Uranus has 27 known moons (all named after Shakespeare characters).",
            "Both planets appear blue/blue-green due to methane in their atmospheres.",
            "Neptune has a storm called the Great Dark Spot (similar to Jupiter's Red Spot).",
            "Uranus was the first planet discovered with a telescope (1781).",
            "It rains DIAMONDS on both Uranus and Neptune!",
        ], "These ice giants are so far from the Sun that they receive very little light and heat."),
        ("Dwarf Planets", [
            "Pluto was reclassified as a dwarf planet in 2006.",
            "Pluto is smaller than Earth's Moon!",
            "There are 5 officially recognized dwarf planets: Pluto, Eris, Ceres, Makemake, Haumea.",
            "Ceres is in the asteroid belt between Mars and Jupiter.",
            "Eris is actually more massive than Pluto.",
            "Pluto has a heart-shaped glacier made of nitrogen ice.",
            "Pluto has 5 moons - the largest is Charon.",
            "New Horizons spacecraft flew by Pluto in 2015 and sent back amazing photos.",
            "A year on Pluto is 248 Earth years!",
            "There may be hundreds more dwarf planets waiting to be discovered.",
        ], "Pluto may be small, but it has a big heart (literally - a heart-shaped feature on its surface)!"),
        ("Asteroids & Comets", [
            "Asteroids are rocky leftovers from when the solar system formed 4.6 billion years ago.",
            "Most asteroids orbit in the Asteroid Belt between Mars and Jupiter.",
            "Some asteroids are tiny (1 meter) while others are huge (530 km across).",
            "Comets are 'dirty snowballs' made of ice, dust, and rock.",
            "Comet tails always point AWAY from the Sun (blown by solar wind).",
            "The dinosaurs were likely wiped out by an asteroid 66 million years ago.",
            "NASA crashed a spacecraft into an asteroid (DART mission) to test if we could deflect one!",
            "Halley's Comet is visible from Earth every 75-76 years (next: 2061).",
            "There are over 1 million known asteroids in our solar system.",
            "Some asteroids contain valuable metals worth trillions of dollars!",
        ], "Don't worry! NASA tracks all nearby asteroids and none are currently on a collision course with Earth."),
        ("Stars & Galaxies", [
            "There are more stars in the universe than grains of sand on all Earth's beaches.",
            "Stars are born in giant clouds of gas and dust called nebulae.",
            "Our Sun is a medium-sized yellow dwarf star.",
            "The biggest known stars are 1,000+ times bigger than our Sun!",
            "When massive stars die, they explode as supernovae.",
            "Our galaxy (Milky Way) has 100-400 BILLION stars.",
            "There are about 2 TRILLION galaxies in the observable universe.",
            "The nearest galaxy to us is Andromeda (2.5 million light-years away).",
            "Galaxies come in shapes: spiral, elliptical, and irregular.",
            "The Milky Way and Andromeda will collide in about 4.5 billion years!",
        ], "When you look up at night, every single star you see is in our own Milky Way galaxy!"),
        ("Black Holes", [
            "A black hole forms when a massive star collapses after dying.",
            "Black holes have gravity SO strong that not even light can escape!",
            "The boundary around a black hole is called the event horizon.",
            "Time moves slower near a black hole (Einstein's theory proven!).",
            "The supermassive black hole at the Milky Way's center is 4 million times our Sun's mass.",
            "Black holes don't suck things in - they only affect objects that get very close.",
            "Scientists took the first photo of a black hole in 2019!",
            "If you fell into a black hole, you'd be stretched like spaghetti (spaghettification).",
            "Black holes can spin at nearly the speed of light.",
            "Miniature black holes may have existed right after the Big Bang.",
        ], "Despite their scary reputation, black holes are essential to how galaxies form and evolve!"),
        ("Space Exploration History", [
            "The Space Age began in 1957 when Russia launched Sputnik (first satellite).",
            "Yuri Gagarin became the first human in space on April 12, 1961.",
            "Neil Armstrong walked on the Moon on July 20, 1969.",
            "The Space Shuttle flew 135 missions from 1981 to 2011.",
            "The International Space Station has been continuously occupied since 2000.",
            "Mars rovers have been exploring since 1997 (Sojourner, Spirit, Opportunity, Curiosity, Perseverance).",
            "Voyager 1 (launched 1977) has left our solar system and is still sending data!",
            "The Hubble Space Telescope has taken photos for 30+ years.",
            "The James Webb Space Telescope (2021) can see the first galaxies ever formed.",
            "SpaceX made the first reusable orbital rocket in 2015.",
        ], "In just 66 years, humans went from the first powered flight to walking on the Moon!"),
        ("Life as an Astronaut", [
            "Astronauts train for YEARS before going to space.",
            "In microgravity, astronauts grow up to 2 inches taller!",
            "Astronauts exercise 2 hours daily to prevent muscle and bone loss.",
            "Water floats in space - astronauts drink from special pouches.",
            "The ISS orbits Earth every 90 minutes (16 sunrises per day!).",
            "Space food has improved - astronauts can now eat tortillas, fruit, and chocolate!",
            "Going to the bathroom in space requires special vacuum toilets.",
            "Astronauts can see Earth's city lights at night from the ISS.",
            "Space suits cost about $12 million each!",
            "Astronauts often report that seeing Earth from space changes their perspective forever.",
        ], "Astronauts say the 'Overview Effect' - seeing Earth from space - makes them appreciate our planet more."),
        ("Future of Space Travel", [
            "NASA's Artemis program aims to return humans to the Moon by 2025-2026.",
            "SpaceX plans to build a city on Mars within decades.",
            "Space tourism is already here - people can buy tickets to space!",
            "Scientists are developing faster propulsion systems for deep space travel.",
            "Space elevators (cables to orbit) could make launches much cheaper.",
            "3D printing could allow us to build structures on the Moon or Mars.",
            "Nuclear-powered rockets could cut Mars travel time from 7 months to 6 weeks.",
            "Mining asteroids for resources could make space exploration profitable.",
            "Generation ships could one day carry humans to other star systems.",
            "The James Webb Telescope might find signs of life on exoplanets.",
        ], "YOUR generation might be the one that sets foot on Mars!"),
        ("Could Aliens Exist?", [
            "There are billions of potentially habitable planets in our galaxy alone.",
            "The Drake Equation estimates millions of civilizations could exist.",
            "We've been searching for alien signals since 1960 (SETI project).",
            "Extremophiles on Earth prove life can survive in incredible conditions.",
            "Mars, Europa (Jupiter's moon), and Enceladus (Saturn's moon) might harbor microbial life.",
            "The universe is 13.8 billion years old - plenty of time for life to evolve elsewhere.",
            "The Fermi Paradox asks: If aliens exist, where is everyone?",
            "We've sent messages into space (Golden Records on Voyager spacecraft).",
            "In 2020, a possible biosignature was detected in Venus's atmosphere.",
            "Finding even microbial alien life would be the biggest discovery in human history!",
        ], "The universe is so vast that many scientists believe it's unlikely we're alone."),
    ]

    title_page(doc, "AMAZING SPACE FACTS FOR KIDS", "Everything You Want to Know About the Universe (Ages 8-14)", "15 Chapters * 150+ Mind-Blowing Facts * Activities * Quizzes")
    copyright_page(doc, "AMAZING SPACE FACTS FOR KIDS")
    toc_page(doc, [c[0] for c in chapters])

    for idx, (ch_title, facts, comparison) in enumerate(chapters):
        chapter_header(doc, idx+1, ch_title)
        y = 580
        doc.add_text(72, y, "MIND-BLOWING FACTS:", 'F2', 13, 0.1)
        y -= 25
        for i, fact in enumerate(facts):
            lines = wrap(fact, 70)
            for j, line in enumerate(lines):
                if y < 80:
                    doc.new_page()
                    y = 720
                prefix = f"{i+1}. " if j == 0 else "   "
                doc.add_text(80, y, f"{prefix}{line}", 'F1', 10, 0.2)
                y -= 17
            y -= 5
        doc.new_page()

        # Did you know + activity page
        doc.add_centered_text(720, f"CHAPTER {idx+1}: EXPLORE MORE", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        doc.add_text(72, 680, "DID YOU KNOW?", 'F2', 13, 0.1)
        y = add_wrapped(doc, 90, 658, comparison, 'F4', 11, 0.2)
        
        y -= 30
        doc.add_text(72, y, "IMAGINE THIS! (Creative Writing Prompt)", 'F2', 13, 0.1)
        y -= 20
        prompts = [
            "You wake up and the Sun has turned blue. Write about what happens on Earth.",
            "You're the first kid to visit Mercury. Describe one day there.",
            "You discover a hidden message carved on the Moon. What does it say?",
            "You're chosen for the first kid Mars mission. Write your diary entry.",
            "You can shrink down and explore Jupiter's Great Red Spot. What do you see?",
            "You find a way to walk on Saturn's rings. Describe the experience.",
            "Your spaceship crash-lands on Neptune. How do you survive?",
            "You discover a new dwarf planet. What do you name it and why?",
            "A friendly comet passes Earth and leaves a gift. What is it?",
            "You can travel to any star. Which one and why?",
            "You accidentally fall near a black hole. Describe what happens.",
            "You meet an astronaut from 1969. What questions do you ask?",
            "You're living on a Moon base in 2050. Describe your typical day.",
            "You invent a spaceship that can reach light speed. Where do you go?",
            "First contact! An alien says hello. What's your response?",
        ]
        y = add_wrapped(doc, 90, y, prompts[idx], 'F4', 11, 0.3)
        y -= 15
        for _ in range(5):
            doc.add_text(90, y, "_____________________________________________________________", 'F1', 10, 0.4)
            y -= 18

        # Quiz
        y -= 25
        doc.add_text(72, y, "QUICK QUIZ:", 'F2', 12, 0.1)
        y -= 20
        quizzes = [
            "How long does sunlight take to reach Earth? A) 8 seconds B) 8 minutes C) 8 hours",
            "Which planet spins backwards? A) Mercury B) Venus C) Mars",
            "How far is the Moon from Earth? A) 24,000 miles B) 238,900 miles C) 1 million miles",
            "What makes Mars look red? A) Paint B) Iron oxide (rust) C) Lava",
            "How many moons does Jupiter have? A) 2 B) 12 C) 95+",
            "What are Saturn's rings made of? A) Gas B) Ice and rock C) Light",
            "What rains on Uranus and Neptune? A) Water B) Diamonds C) Gold",
            "How long is a year on Pluto? A) 88 days B) 248 years C) 1 million years",
            "What wiped out the dinosaurs? A) Volcano B) Asteroid C) Disease",
            "How many galaxies are in the universe? A) 100 B) 1 million C) 2 trillion",
            "Not even ___ can escape a black hole. A) Sound B) Light C) Radio waves",
            "When did humans first walk on the Moon? A) 1959 B) 1969 C) 1979",
            "How often does the ISS orbit Earth? A) Every day B) Every 90 min C) Every week",
            "What might cut Mars travel to 6 weeks? A) Bigger engines B) Nuclear rockets C) Sails",
            "The Drake Equation estimates what? A) Star sizes B) Possible civilizations C) Distance to Mars",
        ]
        doc.add_text(90, y, quizzes[idx], 'F1', 10, 0.3)
        doc.new_page()

    # Space vocabulary
    doc.add_centered_text(720, "SPACE VOCABULARY", 'F2', 18, 0)
    vocab = [("Galaxy","A collection of billions of stars"),("Light-year","Distance light travels in one year"),("Orbit","The path an object takes around another"),("Asteroid","Rocky object orbiting the Sun"),("Nebula","A cloud of gas and dust in space"),("Supernova","An exploding star"),("Exoplanet","A planet outside our solar system"),("Gravity","Force that pulls objects toward each other")]
    y = 680
    for term, defn in vocab:
        doc.add_text(72, y, f"{term}:", 'F2', 11, 0.1)
        doc.add_text(200, y, defn, 'F1', 11, 0.3)
        y -= 30
    doc.new_page()

    certificate(doc, "SPACE EXPLORER CERTIFICATE")
    add_supplemental(doc, 'Space', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book332_Kids_Space_Encyclopedia.pdf')
    print("Book332_Kids_Space_Encyclopedia.pdf created successfully!")

if __name__ == "__main__":
    create_book()
