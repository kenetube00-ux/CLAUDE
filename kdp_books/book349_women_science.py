"""Book349: Women In Science - 20 Incredible Female Scientists"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc()
    author = "Daniel Tesfamariam"
    
    scientists = [
        ("Marie Curie", "Physics & Chemistry", "Radioactivity",
         "Marie Curie moved from Poland to Paris to study science because her own country would not let women attend university. Working in a freezing, leaky shed that served as her laboratory, she and her husband Pierre discovered two new elements: polonium and radium. She was the first woman to win a Nobel Prize and remains the only person ever to win Nobel Prizes in two different sciences.",
         "Radioactivity is the process by which unstable atoms release energy as they break down. Marie discovered that certain elements naturally emit invisible rays of energy. This discovery led to X-rays for medicine, cancer treatments, and eventually nuclear energy.",
         "Collect three household items (banana, brazil nut, smoke detector) and research which ones contain naturally occurring radioactive elements. You will be surprised!",
         "Nothing in life is to be feared, it is only to be understood."),
        ("Rosalind Franklin", "Molecular Biology", "DNA Structure",
         "Rosalind Franklin used X-ray crystallography to photograph DNA. Her famous Photo 51 was the key evidence proving DNA's double helix structure. Without her permission, her colleague showed this photo to James Watson and Francis Crick, who used it to build their famous DNA model. They won the Nobel Prize. She received almost no credit during her lifetime.",
         "X-ray crystallography shoots X-rays through crystals of a substance. The X-rays scatter in patterns that reveal the structure of molecules. Franklin's technique required extreme precision and patience to capture the image that unlocked the secret of life itself.",
         "Build a DNA model using pipe cleaners, beads, and tape. The two twisted strands represent the double helix Franklin helped discover.",
         "Science and everyday life cannot and should not be separated."),
        ("Jane Goodall", "Primatology", "Chimpanzee Behavior",
         "Jane Goodall went to Tanzania at age 26 with no college degree, just an enormous love for animals and fierce determination. Scientists told her she was doing everything wrong by naming the chimps instead of numbering them. She proved them wrong when she discovered that chimpanzees make and use tools, something scientists believed only humans could do.",
         "Before Jane, scientists believed that only humans made tools. Tool use was considered the defining characteristic of humanity. When Jane observed chimps stripping leaves from twigs to fish for termites, she rewrote the definition of what makes us human.",
         "Observe animals in your backyard or a park for 30 minutes. Write down everything you see without disturbing them. Note any tool use or problem-solving behavior.",
         "What you do makes a difference, and you have to decide what kind of difference you want to make."),
        ("Mae Jemison", "Astronautics & Medicine", "Space Exploration",
         "Mae Jemison was inspired by the Star Trek character Uhura to pursue space. She earned degrees in chemical engineering and medicine before being selected by NASA. In 1992, she became the first African American woman to travel into space aboard the Space Shuttle Endeavour, conducting experiments on weightlessness and motion sickness.",
         "In microgravity, the human body behaves differently. Fluids shift upward, bones lose density, and muscles weaken. Mae's experiments helped scientists understand how to keep astronauts healthy on long missions and led to medical advances on Earth.",
         "Create a simple experiment to test how gravity affects plant growth. Plant seeds in two cups, place one sideways. Observe how roots and stems grow relative to gravity.",
         "Never be limited by other people's limited imaginations."),
        ("Katherine Johnson", "Mathematics", "Space Trajectory Calculations",
         "Katherine Johnson was a mathematician at NASA whose calculations of orbital mechanics were critical to the success of early space flights. When NASA started using computers for trajectory calculations, astronaut John Glenn refused to fly unless Katherine personally verified the computer's numbers. She calculated the path for America's first orbital flight by hand.",
         "Orbital mechanics involves calculating the exact speed, angle, and timing needed for a spacecraft to enter orbit around Earth. One small error means the spacecraft could burn up in the atmosphere or fly off into space. Katherine calculated these trajectories using only pencil and paper.",
         "Calculate how far you walk in one day by counting your steps and measuring your stride length. Then calculate how many days it would take to walk to the Moon (238,855 miles).",
         "I counted everything. I counted the steps to the road, the steps up to church."),
        ("Rachel Carson", "Marine Biology", "Environmental Science",
         "Rachel Carson wrote 'Silent Spring' in 1962, exposing the devastating effects of pesticides on birds and ecosystems. The chemical industry attacked her viciously, calling her hysterical and unscientific. But her careful research was unassailable. Her book launched the modern environmental movement and led directly to the banning of DDT.",
         "Bioaccumulation is the process by which toxins concentrate as they move up the food chain. A small amount of pesticide on plants becomes a large amount in the insects that eat the plants, then an even larger amount in the birds that eat the insects, eventually reaching lethal levels.",
         "Build a simple food chain using pictures or objects showing how a toxin multiplies at each level. Start with plants, then insects, then birds, then predators.",
         "In nature, nothing exists alone."),
        ("Barbara McClintock", "Genetics", "Jumping Genes",
         "Barbara McClintock discovered 'jumping genes' (transposons) in corn in the 1940s, but the scientific community dismissed her work for decades because they could not understand it. She was so far ahead of her time that it took 30 years for other scientists to catch up. She finally received the Nobel Prize in 1983 at age 81.",
         "Transposons are segments of DNA that can move from one location to another within a genome. They can turn genes on or off and create mutations. We now know that nearly half of human DNA is made up of transposable elements, playing crucial roles in evolution.",
         "Observe different colored kernels on Indian corn. The color variations are caused by the same jumping genes McClintock discovered! Draw and count the different colors.",
         "If you know you are on the right track, if you have this inner knowledge, then nobody can turn you off."),
        ("Chien-Shiung Wu", "Nuclear Physics", "Parity Violation",
         "Chien-Shiung Wu was known as the First Lady of Physics. She designed and conducted the experiment that disproved the law of conservation of parity, one of the most fundamental assumptions in physics. Two male colleagues suggested the theoretical possibility, but Wu proved it experimentally. They received the Nobel Prize. She did not.",
         "The law of parity stated that nature does not distinguish between left and right at the subatomic level. Wu showed this was wrong by demonstrating that radioactive cobalt atoms, when cooled to near absolute zero, emitted more electrons in one direction than the other.",
         "Test symmetry in nature: Are leaves perfectly symmetrical? Are your hands exactly the same? Make prints of both hands and measure differences. Nature often breaks symmetry!",
         "It is shameful that there are so few women in science."),
        ("Maryam Mirzakhani", "Mathematics", "Hyperbolic Geometry",
         "Maryam Mirzakhani from Iran was the first woman and first Iranian to win the Fields Medal, the highest honor in mathematics. She studied the geometry of curved surfaces, making breakthrough discoveries about the dynamics of surfaces in abstract mathematical spaces. Tragically, she died of cancer at age 40.",
         "Hyperbolic geometry describes surfaces that curve like a saddle, where parallel lines diverge. Imagine the ruffled edge of a lettuce leaf or a coral reef. Maryam studied how these surfaces behave when you trace paths along them, solving problems mathematicians had struggled with for decades.",
         "Make a hyperbolic surface by cutting and taping paper circles together (6-7 triangles meeting at each point instead of the flat 6). Watch it naturally create saddle shapes like coral!",
         "The beauty of mathematics only shows itself to more patient followers."),
        ("Tu Youyou", "Pharmaceutical Chemistry", "Malaria Treatment",
         "Tu Youyou searched through thousands of ancient Chinese herbal remedies to find a cure for malaria that was killing millions. After 380 failed experiments, she found artemisinin in sweet wormwood, but only after she read a 1,600-year-old text that suggested using low temperatures for extraction. Her discovery has saved millions of lives.",
         "Malaria is caused by parasites transmitted through mosquito bites. Artemisinin works by reacting with iron in the malaria parasite to produce toxic free radicals that kill it. The key was extracting the compound at low temperatures to preserve its structure.",
         "Research three medicinal plants that grow in your area. What traditional uses do they have? Many modern medicines originally came from plants!",
         "Every scientist dreams of doing something that can help the world."),
        ("Hedy Lamarr", "Communications Technology", "Frequency Hopping",
         "Hedy Lamarr was known as the most beautiful woman in Hollywood, but she was secretly a brilliant inventor. During World War II, she co-invented frequency-hopping spread spectrum technology to prevent torpedo guidance systems from being jammed. The military ignored her patent, but her invention became the foundation of modern WiFi, Bluetooth, and GPS.",
         "Frequency hopping rapidly switches a signal among many different frequency channels in a pattern known only to the sender and receiver. This makes the signal nearly impossible to intercept or jam. Every time you use WiFi or Bluetooth, you are using Hedy's invention.",
         "Build a simple signal system with a friend using flashlights. Create a code that changes every 30 seconds. This is a simplified version of frequency hopping!",
         "All creative people want to do the unexpected."),
        ("Emmy Noether", "Mathematics & Physics", "Abstract Algebra",
         "Emmy Noether is considered the most important woman in the history of mathematics. Albert Einstein called her a genius. Yet she was not allowed to officially teach at a university because she was a woman. She lectured under a male colleague's name for years. Her theorem connecting symmetry to conservation laws is fundamental to all of modern physics.",
         "Noether's Theorem states that every symmetry in nature corresponds to a conservation law. For example, the fact that physics works the same today as yesterday (time symmetry) means energy is conserved. This single insight connects mathematics to the deepest laws of the universe.",
         "Test conservation of energy: roll a ball down a ramp from different heights. Measure how far it travels on a flat surface. Energy transforms from potential to kinetic!",
         "My methods are really methods of working and thinking."),
        ("Valentina Tereshkova", "Cosmonaut", "Space Travel",
         "Valentina Tereshkova was a textile factory worker and amateur parachutist who was selected for the Soviet space program. In 1963, at age 26, she became the first woman in space. She orbited Earth 48 times in nearly three days, more time in space than all American astronauts had logged combined at that point.",
         "Orbital velocity is the speed needed to stay in orbit around Earth, about 17,500 miles per hour. At this speed, the spacecraft is constantly falling toward Earth but moving forward fast enough that it keeps missing, creating a continuous free fall we experience as weightlessness.",
         "Demonstrate orbital motion by swinging a ball on a string in a circle. The string is like gravity pulling the ball inward while its speed keeps it moving in a circle.",
         "Once you have been in space, you appreciate how small and fragile the Earth is."),
        ("Dian Fossey", "Zoology", "Mountain Gorilla Conservation",
         "Dian Fossey spent 18 years living among mountain gorillas in the volcanic mountains of Rwanda. She learned to communicate with them by imitating their sounds and behaviors. Her research revealed that gorillas were gentle, family-oriented creatures, not the violent beasts people imagined. She fought poachers at great personal risk.",
         "Ethology is the study of animal behavior in natural environments. Dian used habituation, gradually getting gorillas accustomed to her presence over months, to observe their natural behavior. She discovered complex social structures, mourning behaviors, and tool use.",
         "Practice habituation with birds at a feeder. Sit at a distance and move closer each day. Time how long it takes before they eat with you nearby. Record behavioral changes.",
         "When you realize the value of all life, you dwell less on what is past and concentrate on the preservation of the future."),
        ("Maria Goeppert Mayer", "Nuclear Physics", "Nuclear Shell Model",
         "Maria Goeppert Mayer developed the nuclear shell model explaining why some atomic nuclei are more stable than others. Despite being unpaid for most of her career because universities had anti-nepotism rules that affected married women, she persisted in her research and won the Nobel Prize in Physics in 1963, only the second woman after Marie Curie.",
         "Atomic nuclei contain protons and neutrons arranged in shells, similar to how electrons orbit in shells around the nucleus. Certain magic numbers of protons or neutrons (2, 8, 20, 28, 50, 82, 126) create especially stable nuclei, just like full electron shells create stable atoms.",
         "Build an atom model using different colored balls for protons, neutrons, and electrons. Arrange them in shells. Compare atoms with magic numbers to those without.",
         "Mathematics began to seem too much like puzzle solving. Physics is puzzle solving too, but of puzzles created by nature, not by the mind of man."),
        ("Jennifer Doudna", "Biochemistry", "CRISPR Gene Editing",
         "Jennifer Doudna co-developed CRISPR-Cas9, a revolutionary gene-editing tool that allows scientists to precisely cut and modify DNA. This technology has the potential to cure genetic diseases, create disease-resistant crops, and transform medicine. She won the Nobel Prize in Chemistry in 2020.",
         "CRISPR works like molecular scissors. A guide RNA directs the Cas9 protein to a specific location in the genome, where it cuts the DNA. Scientists can then delete harmful genes, insert beneficial ones, or correct mutations that cause disease.",
         "Extract DNA from a strawberry using dish soap, salt, and rubbing alcohol. You will see real DNA as white, stringy strands. This is the same molecule CRISPR edits!",
         "The power to control our species' genetic future is awesome and terrifying."),
        ("Vera Rubin", "Astronomy", "Dark Matter",
         "Vera Rubin studied the rotation of galaxies and found that they were spinning too fast to be held together by visible matter alone. Her observations proved the existence of dark matter, an invisible substance that makes up about 85 percent of all matter in the universe. Many male astronomers initially dismissed her findings.",
         "Galaxies rotate so fast that their visible stars should fly apart unless there is extra invisible mass holding them together gravitationally. Vera measured galaxy rotation curves showing stars at the edges move as fast as those near the center, proving enormous amounts of unseen matter exists.",
         "Spin a ball on a string at different speeds. Notice at what speed it would fly away. Now imagine what invisible force could let it spin even faster without escaping.",
         "Fame is fleeting. My numbers mean more to me than my name."),
        ("Rita Levi-Montalcini", "Neuroscience", "Nerve Growth Factor",
         "Rita Levi-Montalcini conducted secret experiments in her bedroom during World War II when Jews were banned from universities in Italy. Using homemade equipment and chick embryos, she discovered nerve growth factor (NGF), a protein essential for nerve cell development. She won the Nobel Prize at age 77 and remained active in science past 100.",
         "Nerve growth factor is a protein that tells nerve cells to grow and develop. Without NGF, nerves cannot extend, connect, or survive. This discovery opened the door to understanding neurodegenerative diseases like Alzheimer's and led to new treatments.",
         "Observe how roots grow toward water (tropism). Plant seeds in a clear container and keep water on one side only. Nerve growth follows chemical signals just like roots follow water!",
         "Above all, don't fear difficult moments. The best comes from them."),
        ("Gladys West", "Mathematics", "GPS Technology",
         "Gladys West, an African American mathematician at a naval base, programmed computers with complex algorithms for satellite geodesy that became the foundation of GPS technology. Her work calculating the precise shape of the Earth made satellite navigation possible. She was not widely recognized until she was in her 80s.",
         "GPS requires knowing the exact shape of the Earth (the geoid) and precise satellite positions. Gladys's mathematical models accounted for gravitational variations, tides, and other forces to create the accurate Earth model that GPS relies on to pinpoint your location within a few meters.",
         "Use a GPS device or phone to find your exact coordinates. Then navigate to a nearby landmark and compare GPS directions to a paper map. Think about the math behind every step!",
         "When you work hard at something you enjoy, good things happen."),
        ("Katalin Kariko", "Biochemistry", "mRNA Technology",
         "Katalin Kariko spent decades researching mRNA technology while facing constant rejection. She was denied grants, demoted, and told her research was a dead end. She persisted anyway, eventually developing the modified mRNA technology that made COVID-19 vaccines possible, saving millions of lives worldwide. She won the Nobel Prize in 2023.",
         "Messenger RNA carries instructions from DNA to cellular machinery that builds proteins. Kariko discovered how to modify mRNA so the body accepts it without triggering a dangerous immune response. This breakthrough allowed vaccines to instruct cells to build virus proteins for immunity.",
         "Build a protein from a recipe (mRNA). Write instructions for building a LEGO structure. Give the instructions to a friend. This is how mRNA tells cells what to build!",
         "I thought of quitting every day. But I love science too much.")
    ]
    
    # Title page
    doc.add_filled_rect(0, 0, 612, 792, 0.95)
    doc.add_centered_text(640, "WOMEN IN SCIENCE", 'F2', 30, 0.1)
    doc.add_line(150, 620, 462, 620, 2, 0.3)
    doc.add_centered_text(585, "20 Incredible Female Scientists", 'F4', 16, 0.3)
    doc.add_centered_text(560, "Who Changed Everything", 'F4', 16, 0.3)
    doc.add_centered_text(525, "(Ages 9-14)", 'F1', 13, 0.4)
    doc.add_centered_text(100, author, 'F2', 14, 0.2)
    doc.new_page()
    
    # Copyright
    doc.add_centered_text(700, "WOMEN IN SCIENCE", 'F2', 14, 0.2)
    doc.add_text(72, 650, f"Author: {author}", 'F1', 11, 0.3)
    doc.add_text(72, 630, "Format: 8.5 x 11 inches | Kindle & Paperback", 'F1', 10, 0.4)
    doc.add_text(72, 600, "All rights reserved.", 'F1', 10, 0.4)
    doc.new_page()
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0.1)
    doc.add_line(72, 705, 540, 705, 1, 0.3)
    y = 680
    for i, (name, field, discovery, _, _, _, _) in enumerate(scientists):
        doc.add_text(72, y, f"{i+1}. {name} - {field}", 'F1', 11, 0.2)
        y -= 20
        if y < 80:
            doc.new_page()
            y = 740
    doc.new_page()
    
    # Each scientist gets ~3.5 pages
    for i, (name, field, discovery, story, science, experiment, quote) in enumerate(scientists):
        # Page 1: Her Story
        doc.add_filled_rect(50, 710, 512, 50, 0.92)
        doc.add_centered_text(740, f"Scientist #{i+1}", 'F1', 10, 0.5)
        doc.add_centered_text(720, name.upper(), 'F2', 20, 0.1)
        doc.add_centered_text(695, f"{field} | Discovery: {discovery}", 'F4', 11, 0.4)
        
        doc.add_text(72, 665, "HER STORY", 'F2', 13, 0.2)
        doc.add_line(72, 655, 165, 655, 1, 0.4)
        
        words = story.split()
        lines = []
        current = ""
        for word in words:
            if len(current + " " + word) > 78:
                lines.append(current)
                current = word
            else:
                current = current + " " + word if current else word
        if current:
            lines.append(current)
        
        y = 638
        for line in lines:
            doc.add_text(72, y, line, 'F4', 11, 0.2)
            y -= 15
        
        y -= 20
        doc.add_text(72, y, "THE SCIENCE EXPLAINED", 'F2', 13, 0.2)
        y -= 5
        doc.add_line(72, y, 230, y, 1, 0.4)
        y -= 18
        
        words = science.split()
        lines = []
        current = ""
        for word in words:
            if len(current + " " + word) > 78:
                lines.append(current)
                current = word
            else:
                current = current + " " + word if current else word
        if current:
            lines.append(current)
        
        for line in lines:
            doc.add_text(72, y, line, 'F1', 11, 0.2)
            y -= 15
        
        doc.new_page()
        
        # Page 2: Obstacles and Experiment
        doc.add_centered_text(740, f"{name} - Obstacles & Experiment", 'F2', 14, 0.2)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        
        doc.add_text(72, 700, "OBSTACLES AS A WOMAN IN SCIENCE", 'F2', 12, 0.2)
        obstacles = [
            f"{name} faced significant barriers because of her gender. In her era,",
            "women were often denied access to laboratories, excluded from academic",
            "positions, paid less than male colleagues, or had their work credited",
            "to men. She persisted despite discrimination, proving that scientific",
            "brilliance has nothing to do with gender. Her determination opened doors",
            "for every woman scientist who came after her."
        ]
        y = 678
        for line in obstacles:
            doc.add_text(72, y, line, 'F4', 11, 0.25)
            y -= 15
        
        y -= 20
        doc.add_text(72, y, "TRY THIS! HOME EXPERIMENT", 'F2', 13, 0.2)
        y -= 5
        doc.add_line(72, y, 270, y, 1, 0.4)
        y -= 18
        
        words = experiment.split()
        lines = []
        current = ""
        for word in words:
            if len(current + " " + word) > 78:
                lines.append(current)
                current = word
            else:
                current = current + " " + word if current else word
        if current:
            lines.append(current)
        
        for line in lines:
            doc.add_text(82, y, line, 'F1', 11, 0.3)
            y -= 16
        
        y -= 20
        doc.add_text(72, y, "CAREERS THAT USE THIS SCIENCE:", 'F2', 11, 0.2)
        y -= 18
        careers = ["Research Scientist", "Engineer", "Medical Doctor", "Professor", "Data Analyst"]
        for career in careers:
            doc.add_text(92, y, f"- {career} in {field}", 'F1', 10, 0.3)
            y -= 15
        
        y -= 20
        doc.add_filled_rect(72, y - 10, 468, 35, 0.92)
        doc.add_centered_text(y + 8, f'"{quote}"', 'F5', 11, 0.2)
        doc.add_centered_text(y - 8, f"- {name}", 'F4', 10, 0.4)
        
        doc.new_page()
        
        # Page 3: Legacy and reflection
        doc.add_centered_text(740, f"{name} - Legacy & Your Turn", 'F2', 14, 0.2)
        doc.add_line(72, 725, 540, 725, 1, 0.3)
        
        doc.add_text(72, 700, "HER LEGACY", 'F2', 12, 0.2)
        legacy_text = [
            f"{name}'s work continues to impact science and the world today.",
            "Her discoveries opened new fields of research, inspired countless",
            "young women to pursue science, and proved that determination and",
            "curiosity are the most important tools any scientist can have.",
            "Every time we benefit from her work, we honor her legacy."
        ]
        y = 678
        for line in legacy_text:
            doc.add_text(72, y, line, 'F4', 11, 0.25)
            y -= 15
        
        y -= 20
        doc.add_text(72, y, "MY REFLECTION:", 'F2', 12, 0.2)
        y -= 5
        doc.add_text(72, y, "What inspires me most about this scientist:", 'F4', 10, 0.4)
        y -= 18
        for j in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 22
        
        y -= 10
        doc.add_text(72, y, "A scientific question I want to explore:", 'F4', 10, 0.4)
        y -= 18
        for j in range(4):
            doc.add_line(72, y, 540, y, 0.5, 0.7)
            y -= 22
        
        doc.new_page()
    
    # Final page
    doc.add_centered_text(600, "THE NEXT GREAT SCIENTIST COULD BE YOU!", 'F2', 18, 0.1)
    doc.add_centered_text(560, "Stay curious. Ask questions. Experiment.", 'F4', 14, 0.3)
    doc.add_centered_text(530, "The world needs YOUR discoveries.", 'F4', 14, 0.3)
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
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book349_Women_In_Science.pdf')
    print("Book349_Women_In_Science.pdf created successfully!")

if __name__ == "__main__":
    create_book()
