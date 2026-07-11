from pdf_utils import PDFDoc
pdf = PDFDoc(612, 792)
author = "Daniel Tesfamariam"
title = "READING COMPREHENSION WORKBOOK"
subtitle = "Grades 2-4"

# Page 1: Title
pdf.new_page()
pdf.add_centered_text(550, title, 'F2', 18)
pdf.add_centered_text(510, subtitle, 'F4', 14)
pdf.add_centered_text(400, "25 Passages with Questions", 'F4', 12)
pdf.add_centered_text(380, "to Build Reading Skills", 'F4', 12)
pdf.add_centered_text(250, f"By {author}", 'F2', 13)

# Page 2: Copyright
pdf.new_page()
pdf.add_centered_text(600, title, 'F2', 12)
pdf.add_centered_text(560, f"Copyright 2025 {author}", 'F4', 10)
pdf.add_centered_text(540, "All rights reserved.", 'F4', 10)
pdf.add_centered_text(510, "No part of this publication may be reproduced without permission.", 'F4', 9)


# 25 Reading Passages with Questions
passages = [
    ("The Amazing Octopus", [
        "The octopus is one of the smartest animals in the ocean. It has eight",
        "arms and three hearts. An octopus can change its color in less than a",
        "second to hide from enemies. It can also squeeze through tiny spaces",
        "because it has no bones. Scientists have watched octopuses open jars",
        "and solve puzzles. Some even recognize different human faces. These",
        "clever creatures live in all the world's oceans, from warm tropical",
        "waters to the cold deep sea."
    ], [
        ("What is the main idea of this passage?", "a) Octopuses are dangerous  b) Octopuses are very smart  c) Octopuses live in jars  d) Octopuses have bones"),
        ("How many hearts does an octopus have?", "a) One  b) Two  c) Three  d) Eight"),
        ("What does the word 'clever' mean in this passage?", "a) Slow  b) Smart  c) Colorful  d) Tiny"),
        ("Why can an octopus squeeze through tiny spaces?", "a) It is small  b) It has no bones  c) It changes color  d) It has eight arms"),
        ("What is your opinion: Would an octopus make a good pet? Why or why not?", ""),
    ]),
    ("Life on the Space Station", [
        "Astronauts on the International Space Station float because there is",
        "very little gravity. They have to strap themselves into sleeping bags",
        "so they do not drift away while sleeping. Eating is tricky too. Food",
        "comes in special packages, and drinks come in pouches with straws so",
        "liquids do not float around the cabin. Astronauts exercise two hours",
        "every day to keep their muscles strong. Without gravity pulling on",
        "their bodies, their muscles and bones would get weak."
    ], [
        ("What is this passage mostly about?", "a) How to become an astronaut  b) Daily life in space  c) Building space stations  d) Eating food"),
        ("Why do astronauts strap into sleeping bags?", "a) To stay warm  b) So they don't drift away  c) Because beds are uncomfortable  d) To exercise"),
        ("What does 'drift' mean in this passage?", "a) Fall down  b) Float away slowly  c) Run fast  d) Sleep deeply"),
        ("What can you infer about why astronauts exercise daily?", "a) They are bored  b) They want muscles  c) Gravity doesn't help their bodies stay strong  d) The captain makes them"),
        ("Would you like to live in space? Write why or why not.", ""),
    ]),
    ("How Thunderstorms Form", [
        "Thunderstorms need three things to form: moisture, rising warm air,",
        "and a trigger like a cold front. When warm, moist air rises quickly,",
        "it forms tall clouds called cumulonimbus clouds. Inside these clouds,",
        "water droplets and ice crash together, creating static electricity.",
        "When enough electricity builds up, it releases as lightning. The",
        "lightning heats the air so fast that it expands and creates a loud",
        "boom we call thunder. Light travels faster than sound, so we always",
        "see lightning before we hear thunder."
    ], [
        ("What three things does a thunderstorm need?", "a) Wind, rain, snow  b) Moisture, warm air, a trigger  c) Clouds, sun, cold  d) Lightning, thunder, hail"),
        ("What type of cloud makes thunderstorms?", "a) Cirrus  b) Stratus  c) Cumulonimbus  d) Fog"),
        ("What does 'expands' mean?", "a) Gets smaller  b) Gets bigger  c) Gets colder  d) Disappears"),
        ("Why do we see lightning before hearing thunder?", "a) Lightning is louder  b) Thunder is slower  c) Light travels faster than sound  d) We imagine it"),
        ("Do you think thunderstorms are scary or exciting? Explain.", ""),
    ]),
    ("The First Baseball Game", [
        "Marco was nervous for his first baseball game. He had practiced",
        "hitting and catching all summer, but playing in front of people was",
        "different. When it was his turn to bat, his hands were shaking. The",
        "first pitch flew past him. Strike one. He took a deep breath. The",
        "second pitch came, and he swung hard. Crack! The ball sailed over",
        "the shortstop's head. Marco ran to first base, his heart pounding",
        "with joy. His teammates cheered. It was just a single, but to Marco",
        "it felt like a home run."
    ], [
        ("What is the main idea of this story?", "a) Baseball is hard  b) Marco overcomes nervousness to get a hit  c) Marco hits a home run  d) Marco's team wins"),
        ("How did Marco feel before batting?", "a) Angry  b) Nervous  c) Bored  d) Sleepy"),
        ("What does 'sailed' mean in this passage?", "a) Went on a boat  b) Flew through the air  c) Fell down  d) Bounced"),
        ("Why did the hit feel like a home run to Marco?", "a) It went over the fence  b) He was proud of overcoming his fear  c) His coach said so  d) He scored a point"),
        ("Write about a time you were nervous but did something brave.", ""),
    ]),
    ("Helping the Community Garden", [
        "Every Saturday, kids from Oak Street help in the community garden.",
        "They plant vegetables like tomatoes, peppers, and beans. Mrs. Chen",
        "teaches them how to pull weeds and water the plants properly. The",
        "garden gives its food to families who need it. Last summer, the",
        "garden grew over 500 pounds of vegetables. The kids feel proud",
        "knowing their work helps feed their neighbors. They also learn where",
        "food comes from and how much work goes into growing it."
    ], [
        ("What happens every Saturday?", "a) Kids play sports  b) Kids work in a garden  c) Kids go to school  d) Kids visit Mrs. Chen's house"),
        ("Who teaches the children?", "a) Their parents  b) The principal  c) Mrs. Chen  d) A farmer"),
        ("What does 'community' mean?", "a) A school  b) A group of people living in the same area  c) A type of plant  d) A garden tool"),
        ("What can you infer about why the kids feel proud?", "a) They get paid  b) They help people who need food  c) They skip school  d) They eat the food themselves"),
        ("Would you like to work in a community garden? Why?", ""),
    ]),
]


passages += [
    ("Why Do Leaves Change Color?", [
        "In fall, leaves turn red, orange, and yellow. But why? During summer,",
        "leaves are green because of a chemical called chlorophyll. Chlorophyll",
        "helps leaves make food from sunlight. When days get shorter in fall,",
        "trees stop making chlorophyll. Without the green color, other colors",
        "that were hidden all along can finally show through. Red and purple",
        "colors are actually made new in fall to protect the leaf. Eventually,",
        "the leaves fall off so the tree can save energy for winter."
    ], [
        ("Why are leaves green in summer?", "a) They are painted  b) Because of chlorophyll  c) Because of water  d) The sun makes them green"),
        ("When do leaves change color?", "a) Spring  b) Summer  c) Fall  d) Winter"),
        ("What does 'hidden' mean here?", "a) Lost  b) There but not seen  c) Broken  d) New"),
        ("Why do trees drop their leaves?", "a) They are dead  b) To save energy for winter  c) The wind blows them  d) Kids pull them off"),
        ("What is your favorite season and why?", ""),
    ]),
    ("The Amazing Migration of Monarch Butterflies", [
        "Every fall, millions of monarch butterflies fly south to Mexico. They",
        "travel up to 3,000 miles, which is amazing for an insect that weighs",
        "less than a paperclip. Monarchs cannot fly in cold weather, so they",
        "must reach Mexico before winter. They use the sun and Earth's magnetic",
        "field to navigate. In spring, they fly north again, but no single",
        "butterfly makes the whole trip. It takes four generations to complete",
        "the return journey. Scientists are still studying how they know where",
        "to go without ever having been there before."
    ], [
        ("What is this passage mainly about?", "a) Mexico  b) Butterflies migrating  c) How insects fly  d) Cold weather"),
        ("How far do monarchs travel?", "a) 300 miles  b) 3,000 miles  c) 30 miles  d) 30,000 miles"),
        ("What does 'navigate' mean?", "a) Eat  b) Find their way  c) Sleep  d) Fly fast"),
        ("What is surprising about the return trip north?", "a) It takes 4 generations  b) They fly at night  c) They take a bus  d) Only one butterfly goes"),
        ("If you could migrate anywhere, where would you go?", ""),
    ]),
    ("Sarah's Science Fair Project", [
        "Sarah wanted to know if plants grow better with music. She planted",
        "three bean seeds in identical pots with the same soil and water. She",
        "put one plant in silence, played classical music for the second, and",
        "played rock music for the third. After three weeks, the classical",
        "music plant was tallest. The silent plant was medium height. The rock",
        "music plant was shortest. Sarah concluded that classical music might",
        "help plants grow, but she knew she needed to test more plants to be",
        "sure her results were accurate."
    ], [
        ("What question was Sarah trying to answer?", "a) Do plants need water?  b) Do plants grow better with music?  c) What color are beans?  d) How tall do plants grow?"),
        ("How many plants did Sarah use?", "a) One  b) Two  c) Three  d) Four"),
        ("What does 'identical' mean?", "a) Different  b) Exactly the same  c) Big  d) Broken"),
        ("Why did Sarah say she needed to test more plants?", "a) She was bored  b) Three plants isn't enough to be sure  c) Her teacher told her  d) The plants died"),
        ("What experiment would YOU do for a science fair?", ""),
    ]),
    ("How Honey Is Made", [
        "Bees work very hard to make honey. A worker bee visits up to 1,500",
        "flowers in one trip to collect nectar. She stores the nectar in a",
        "special honey stomach and flies back to the hive. There, other bees",
        "chew the nectar and add enzymes that change it into honey. Then they",
        "put it in honeycomb cells and fan it with their wings to remove water.",
        "When the honey is thick enough, they seal the cell with wax. One bee",
        "makes only one-twelfth of a teaspoon of honey in its whole life."
    ], [
        ("What does a worker bee collect from flowers?", "a) Pollen  b) Nectar  c) Honey  d) Wax"),
        ("How much honey does one bee make in its lifetime?", "a) A gallon  b) A cup  c) One-twelfth teaspoon  d) One pound"),
        ("What does 'enzymes' probably mean?", "a) Special chemicals that change things  b) Colors  c) Flavors  d) Sounds"),
        ("Why do bees fan the nectar with their wings?", "a) To keep cool  b) To remove water  c) To make noise  d) For exercise"),
        ("After reading this, how do you feel about honey?", ""),
    ]),
    ("The Friendship Bracelet", [
        "Lily and Rosa had been best friends since kindergarten. When Rosa",
        "found out she was moving to a new city, both girls cried. On Rosa's",
        "last day, Lily gave her a friendship bracelet she had spent two weeks",
        "making. It had Rosa's favorite colors: purple and gold. Rosa gave Lily",
        "a matching one she had secretly made too. They promised to wear them",
        "every day and video call every weekend. Moving apart was hard, but",
        "their friendship was stronger than distance."
    ], [
        ("What is the problem in this story?", "a) They lost their bracelets  b) Rosa is moving away  c) They had a fight  d) Lily is sick"),
        ("How long did Lily spend making the bracelet?", "a) One day  b) Two weeks  c) One hour  d) Two months"),
        ("What does the word 'secretly' tell us about Rosa?", "a) She was angry  b) She wanted to surprise Lily  c) She was embarrassed  d) She forgot"),
        ("What can you infer about Lily and Rosa's friendship?", "a) It will end  b) It is very strong  c) They don't like each other  d) They just met"),
        ("Write about your best friend and why they matter to you.", ""),
    ]),
]


passages += [
    ("Volcanoes: Mountains of Fire", [
        "A volcano is an opening in Earth's surface where hot melted rock,",
        "called magma, pushes up from deep underground. When magma reaches the",
        "surface, it is called lava. Some volcanoes erupt with giant explosions,",
        "while others ooze lava slowly. There are about 1,500 active volcanoes",
        "on Earth. Most are along the Ring of Fire, a circle of volcanoes around",
        "the Pacific Ocean. Volcanoes can be dangerous, but they also create",
        "new land and make soil very rich for farming."
    ], [
        ("What is magma?", "a) A type of rock  b) Hot melted rock underground  c) Cold lava  d) Volcano ash"),
        ("How many active volcanoes are on Earth?", "a) 150  b) 1,500  c) 15,000  d) 15"),
        ("What does 'erupt' mean?", "a) Sleep  b) Explode or release lava  c) Grow taller  d) Cool down"),
        ("What is one GOOD thing volcanoes do?", "a) Destroy cities  b) Make rich soil  c) Create storms  d) Melt ice"),
        ("If you could visit any volcano safely, which would it be?", ""),
    ]),
    ("Training a New Puppy", [
        "Getting a new puppy is exciting, but it takes patience and hard work.",
        "Puppies need to learn basic commands like sit, stay, and come. The",
        "best way to train a puppy is with positive reinforcement. This means",
        "giving treats and praise when the puppy does something right. Yelling",
        "or punishing a puppy makes it scared, not obedient. Puppies also need",
        "to be socialized, which means meeting lots of different people and",
        "animals so they grow up friendly and confident."
    ], [
        ("What is the main idea?", "a) Puppies are cute  b) How to train a puppy  c) Dogs need food  d) Puppies sleep a lot"),
        ("What is positive reinforcement?", "a) Yelling  b) Rewarding good behavior  c) Ignoring the puppy  d) Putting puppy in timeout"),
        ("What does 'socialized' mean here?", "a) Trained to sit  b) Meeting many people and animals  c) Learning to bark  d) Going to school"),
        ("Why shouldn't you yell at a puppy?", "a) It hurts your voice  b) It makes the puppy scared  c) Puppies can't hear  d) It's too loud"),
        ("Describe your dream pet (real or imaginary).", ""),
    ]),
    ("The Water Cycle", [
        "Water on Earth is always moving in a big cycle. The sun heats water",
        "in oceans, lakes, and rivers, turning it into water vapor that rises",
        "into the air. This is called evaporation. High in the sky, the vapor",
        "cools and forms tiny water droplets in clouds. This is condensation.",
        "When clouds get too heavy with water, the droplets fall as rain or",
        "snow. This is precipitation. The water flows into streams and rivers,",
        "back to the ocean, and the cycle starts again."
    ], [
        ("What causes water to evaporate?", "a) Wind  b) The moon  c) The sun's heat  d) Fish"),
        ("What is condensation?", "a) Water falling as rain  b) Water vapor cooling into droplets  c) Water flowing in rivers  d) Water freezing"),
        ("What does 'precipitation' mean?", "a) Clouds forming  b) Water falling from clouds  c) Water evaporating  d) Rivers flowing"),
        ("What can you infer about the water cycle?", "a) It stops in winter  b) It never ends  c) It only happens in oceans  d) It requires humans"),
        ("Where does the water in your glass come from originally?", ""),
    ]),
    ("Maya's Math Mystery", [
        "Maya found a note in her library book. It said: 'Follow the clues",
        "to find the treasure. First clue: Look where stories sleep at night.'",
        "Maya thought hard. Where do stories sleep? The bookshelf! Behind the",
        "books, she found another note: 'I have hands but cannot clap.' The",
        "clock! Behind the clock was the last clue: 'I have a heart but am not",
        "alive.' Maya ran to the deck of cards in the game drawer. Inside the",
        "box was a gift card to the bookstore from her grandmother. Maya loved",
        "a good mystery almost as much as she loved books."
    ], [
        ("Who left the clues for Maya?", "a) Her friend  b) Her teacher  c) Her grandmother  d) A stranger"),
        ("What did 'where stories sleep' mean?", "a) The bed  b) The bookshelf  c) The library  d) Under the pillow"),
        ("What does 'I have hands but cannot clap' describe?", "a) A doll  b) A clock  c) A tree  d) A baby"),
        ("What can you infer about Maya?", "a) She doesn't like reading  b) She is smart and loves books  c) She is scared  d) She doesn't like her grandma"),
        ("Write your own riddle for a friend to solve.", ""),
    ]),
    ("Recycling Makes a Difference", [
        "Every day, Americans throw away enough trash to fill 63,000 garbage",
        "trucks. Much of this trash could be recycled instead. Recycling means",
        "turning old materials into new products. Aluminum cans can be recycled",
        "and back on store shelves in just 60 days. Recycling one ton of paper",
        "saves 17 trees. Glass can be recycled forever without losing quality.",
        "When we recycle, we use less energy, create less pollution, and save",
        "natural resources for the future."
    ], [
        ("How many garbage trucks of trash do Americans fill daily?", "a) 630  b) 6,300  c) 63,000  d) 630,000"),
        ("How fast can aluminum cans be recycled?", "a) 60 days  b) 60 weeks  c) 6 months  d) 6 years"),
        ("What does 'natural resources' mean?", "a) Trash  b) Things from nature we use  c) Recycling bins  d) Factories"),
        ("Why is recycling glass special?", "a) It's easy  b) It can be recycled forever  c) It's cheap  d) Kids can do it"),
        ("What do you recycle at home? What more could you do?", ""),
    ]),
]


passages += [
    ("The History of Pizza", [
        "Pizza as we know it started in Naples, Italy, in the 1700s. Poor",
        "people needed cheap food they could eat quickly. They put tomatoes,",
        "cheese, and olive oil on flat bread and baked it in hot ovens. In",
        "1889, a baker made a special pizza for Queen Margherita with tomato,",
        "mozzarella, and basil - the colors of the Italian flag. It was named",
        "Pizza Margherita. Italian immigrants brought pizza to America in the",
        "early 1900s. Today, Americans eat about 3 billion pizzas every year."
    ], [
        ("Where did modern pizza begin?", "a) America  b) France  c) Naples, Italy  d) China"),
        ("Why did poor people like pizza?", "a) It was healthy  b) It was cheap and fast  c) Queens ate it  d) It was new"),
        ("What does 'immigrants' mean?", "a) Bakers  b) People who move to a new country  c) Pizza lovers  d) Italians"),
        ("Why was Pizza Margherita special?", "a) It was big  b) It used flag colors  c) It was free  d) It had meat"),
        ("Describe your perfect pizza (be creative!).", ""),
    ]),
    ("Teamwork on the Soccer Field", [
        "Carlos wanted to score all the goals himself. He never passed the",
        "ball to his teammates. Game after game, the other team would steal",
        "the ball from him because he was always surrounded. His coach sat him",
        "down and said, 'One great player can't beat five good defenders. But",
        "five players working together can beat anyone.' In the next game,",
        "Carlos passed to Maria, who passed to James, who scored. Carlos",
        "finally understood: the best players make their whole team better."
    ], [
        ("What was Carlos's problem?", "a) He couldn't kick  b) He never passed the ball  c) He was too slow  d) He was injured"),
        ("What lesson did the coach teach?", "a) Practice more  b) Teamwork beats one person  c) Score more goals  d) Run faster"),
        ("What does 'defenders' mean?", "a) Coaches  b) Players who stop the other team  c) Referees  d) Fans"),
        ("How did Carlos change?", "a) He quit  b) He started passing  c) He became goalie  d) He scored alone"),
        ("Write about a time teamwork helped you accomplish something.", ""),
    ]),
    ("Living in the Desert", [
        "Deserts are dry places that get less than 10 inches of rain per year.",
        "Even though deserts seem empty, many animals live there. Kangaroo rats",
        "never need to drink water - they get moisture from seeds they eat.",
        "Camels store fat in their humps for energy when food is scarce. Many",
        "desert animals are nocturnal, meaning they sleep during the hot day",
        "and come out at cool night. Desert plants like cactus store water in",
        "their thick stems and have spines instead of leaves to prevent water",
        "loss."
    ], [
        ("How much rain does a desert get?", "a) More than 10 inches  b) Less than 10 inches  c) No rain ever  d) 100 inches"),
        ("How do kangaroo rats get water?", "a) They drink from rivers  b) From seeds they eat  c) From rain  d) From cactus"),
        ("What does 'nocturnal' mean?", "a) Active during the day  b) Active at night  c) Always sleeping  d) Living underground"),
        ("Why do cactus plants have spines instead of leaves?", "a) To look pretty  b) To hurt animals  c) To prevent water loss  d) To grow taller"),
        ("What desert animal do you find most interesting? Why?", ""),
    ]),
    ("The Kindness Chain", [
        "One morning, a woman paid for the coffee of the stranger behind her",
        "in line. That stranger was so surprised that he paid for the next",
        "person's order. The chain of kindness continued for 47 people that",
        "day at the coffee shop. When the story was on the news, people all",
        "over town started doing random acts of kindness. A boy mowed his",
        "neighbor's lawn. A girl shared her lunch with a new student. Small",
        "acts of kindness can create big waves of happiness."
    ], [
        ("How did the kindness chain start?", "a) A boy mowed a lawn  b) A woman paid for a stranger's coffee  c) Someone was on the news  d) A girl shared lunch"),
        ("How many people kept the chain going?", "a) 7  b) 17  c) 47  d) 470"),
        ("What does 'random acts of kindness' mean?", "a) Planned events  b) Nice things done for strangers unexpectedly  c) Paying for everything  d) Being kind only to friends"),
        ("What effect did the news story have?", "a) Nothing  b) People started being kind too  c) People were angry  d) The coffee shop closed"),
        ("Write about a kind thing someone did for you or you did for someone.", ""),
    ]),
    ("Astronaut Mae Jemison", [
        "Mae Jemison became the first African American woman to travel to",
        "space in 1992. Before becoming an astronaut, she was a doctor who",
        "served in the Peace Corps in West Africa. She speaks four languages:",
        "English, Japanese, Russian, and Swahili. After leaving NASA, she",
        "started a company to use technology to help people in developing",
        "countries. Jemison says she was inspired by the character Lt. Uhura",
        "from Star Trek. She proves that you can achieve anything if you work",
        "hard and never give up on your dreams."
    ], [
        ("What record did Mae Jemison set?", "a) First woman in space  b) First African American woman in space  c) First doctor in space  d) First person on Mars"),
        ("How many languages does she speak?", "a) Two  b) Three  c) Four  d) Five"),
        ("What does 'inspired' mean?", "a) Scared  b) Motivated or encouraged  c) Confused  d) Bored"),
        ("What can you infer about Mae Jemison's personality?", "a) She gives up easily  b) She is determined and hardworking  c) She only likes space  d) She is shy"),
        ("Who inspires YOU to do great things? Why?", ""),
    ]),
]

# Generate passage pages
answers = []
for i, (ptitle, ptext, questions) in enumerate(passages):
    pdf.new_page()
    pdf.add_centered_text(750, f"PASSAGE {i+1}: {ptitle}", 'F2', 13)
    pdf.add_line(50, 740, 562, 740)
    y = 718
    for line in ptext:
        pdf.add_text(50, y, line, 'F4', 10.5)
        y -= 15
    y -= 15
    pdf.add_line(50, y+5, 562, y+5, 0.5, 0.5)
    y -= 10
    pdf.add_text(50, y, "QUESTIONS:", 'F2', 11)
    y -= 18
    q_answers = []
    for qi, (q, opts) in enumerate(questions):
        pdf.add_text(50, y, f"{qi+1}. {q}", 'F1', 10)
        y -= 15
        if opts:
            pdf.add_text(65, y, opts, 'F4', 9)
            y -= 14
            q_answers.append(opts.split("  ")[1].split(")")[0] + ")" if qi < 4 else "Open-ended")
        else:
            q_answers.append("Open-ended")
        pdf.add_line(65, y, 560, y, 0.3, 0.7)
        y -= 14
        if qi == 4:
            pdf.add_line(65, y, 560, y, 0.3, 0.7)
            y -= 14
    answers.append((ptitle, q_answers))


# Answer Key Pages (3 pages)
answer_data = [
    ("The Amazing Octopus", ["b", "c", "b", "b"]),
    ("Life on the Space Station", ["b", "b", "b", "c"]),
    ("How Thunderstorms Form", ["b", "c", "b", "c"]),
    ("The First Baseball Game", ["b", "b", "b", "b"]),
    ("Helping the Community Garden", ["b", "c", "b", "b"]),
    ("Why Do Leaves Change Color?", ["b", "c", "b", "b"]),
    ("The Amazing Migration of Monarch Butterflies", ["b", "b", "b", "a"]),
    ("Sarah's Science Fair Project", ["b", "c", "b", "b"]),
    ("How Honey Is Made", ["b", "c", "a", "b"]),
    ("The Friendship Bracelet", ["b", "b", "b", "b"]),
    ("Volcanoes: Mountains of Fire", ["b", "b", "b", "b"]),
    ("Training a New Puppy", ["b", "b", "b", "b"]),
    ("The Water Cycle", ["c", "b", "b", "b"]),
    ("Maya's Math Mystery", ["c", "b", "b", "b"]),
    ("Recycling Makes a Difference", ["c", "a", "b", "b"]),
    ("The History of Pizza", ["c", "b", "b", "b"]),
    ("Teamwork on the Soccer Field", ["b", "b", "b", "b"]),
    ("Living in the Desert", ["b", "b", "b", "c"]),
    ("The Kindness Chain", ["b", "c", "b", "b"]),
    ("Astronaut Mae Jemison", ["b", "c", "b", "b"]),
]

for page in range(3):
    pdf.new_page()
    pdf.add_centered_text(750, f"ANSWER KEY (Page {page+1})", 'F2', 14)
    pdf.add_line(50, 740, 562, 740)
    y = 718
    start_idx = page * 9 if page < 2 else 18
    end_idx = min(start_idx + 9, len(answer_data)) if page < 2 else len(answer_data)
    for idx in range(start_idx, end_idx):
        ptitle, ans = answer_data[idx]
        pdf.add_text(50, y, f"Passage {idx+1}: {ptitle}", 'F2', 9)
        y -= 14
        pdf.add_text(60, y, f"1.{ans[0]}  2.{ans[1]}  3.{ans[2]}  4.{ans[3]}  5. Open-ended", 'F3', 9)
        y -= 20

# Reading Strategies Tips Page
pdf.new_page()
pdf.add_centered_text(750, "READING STRATEGIES TIPS", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
tips = [
    "BEFORE READING:",
    "- Look at the title. What do you think it will be about?",
    "- Look for pictures or bold words for clues",
    "- Think about what you already know about this topic",
    "",
    "DURING READING:",
    "- If you don't know a word, read the sentence around it for clues",
    "- Ask yourself: 'What just happened? What might happen next?'",
    "- Make pictures in your mind as you read",
    "- Reread parts that are confusing (that's totally okay!)",
    "",
    "AFTER READING:",
    "- Retell the passage in your own words",
    "- What was the MAIN IDEA (the big point)?",
    "- What are the DETAILS (the smaller facts)?",
    "- How does this connect to things you already know?",
    "",
    "QUESTION TYPES EXPLAINED:",
    "- Main Idea: What is the passage mostly about?",
    "- Detail: Find a specific fact in the passage",
    "- Vocabulary: Use clues in the sentence to figure out a word",
    "- Inference: What can you figure out that isn't directly stated?",
    "- Opinion: There's no wrong answer - just explain your thinking!",
]
for line in tips:
    pdf.add_text(50, y, line, 'F4', 10.5)
    y -= 17

# Books I Want to Read Page
pdf.new_page()
pdf.add_centered_text(750, "BOOKS I WANT TO READ", 'F2', 15)
pdf.add_line(50, 740, 562, 740)
y = 715
pdf.add_text(50, y, "Keep a list of books that sound interesting to you!", 'F4', 10.5)
y -= 25
for i in range(25):
    pdf.add_text(50, y, f"{i+1}.", 'F1', 10)
    pdf.add_line(75, y-2, 400, y-2, 0.5, 0.5)
    pdf.add_text(410, y, "Read? [ ]", 'F1', 9)
    pdf.add_text(470, y, "Rating: ___/5", 'F1', 9)
    y -= 22

pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book162_Reading_Comprehension_Workbook.pdf')
print("Book162_Reading_Comprehension_Workbook.pdf created successfully!")
