from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    countries = [
        ("United States","North America","Washington D.C.","English","Stars & Stripes (red, white, blue, 50 stars)","331 million",["The US has 50 states spanning 6 time zones","The Grand Canyon is over 1 mile deep","Americans eat 3 billion pizzas per year","The bald eagle is the national bird","Hawaii is the only state made entirely of islands"],"Mac and cheese, hamburgers, pizza","Statue of Liberty","The world's largest economy and cultural exporter"),
        ("Canada","North America","Ottawa","English & French","Red maple leaf on white background","38 million",["Canada has more lakes than all other countries combined","Hockey is the national winter sport","Canadian coins are called 'Loonies' (they have a loon bird on them)","Canada is the 2nd largest country by area","Maple syrup production: 71% of world supply"],"Poutine (fries with gravy and cheese curds)","CN Tower in Toronto","Known for politeness, nature, and cold winters"),
        ("Mexico","North America","Mexico City","Spanish","Green, white, red with eagle and snake","128 million",["Mexico introduced chocolate, vanilla, and chilies to the world","It has 35 UNESCO World Heritage Sites","The Aztec civilization built amazing pyramids","Mexican children celebrate Dia de los Muertos","Mexico City was built on top of an ancient lake"],"Tacos, enchiladas, tamales","Chichen Itza pyramid","Rich blend of indigenous and Spanish cultures"),
        ("Brazil","South America","Brasilia","Portuguese","Green with yellow diamond and blue globe","214 million",["Brazil has the most plant species of any country","The Amazon Rainforest produces 20% of world oxygen","Soccer (football) is practically a religion here","Rio Carnival attracts 2 million people per day","Brazil is the only Portuguese-speaking country in the Americas"],"Rice and beans, feijoada, acai bowls","Christ the Redeemer statue in Rio","Home to the Amazon - the world's largest rainforest"),
        ("Argentina","South America","Buenos Aires","Spanish","Light blue and white with sun","46 million",["Argentina is the birthplace of tango dance","They have the widest avenue in the world (9 de Julio)","Beef is a major part of culture (asado/BBQ)","Patagonia has glaciers and penguins","Kids stay up very late - dinner at 10pm is normal!"],"Asado (BBQ), empanadas, dulce de leche","Iguazu Falls","A country of passion: dance, soccer, steak, and scenery"),
        ("Peru","South America","Lima","Spanish & Quechua","Red and white vertical stripes","33 million",["Machu Picchu was built by the Inca empire around 1450","Peru has 90 microclimates","Guinea pigs are pets AND food in Peru","The Amazon River starts in Peru","Peruvian food is considered among the best in the world"],"Ceviche (raw fish in citrus), lomo saltado","Machu Picchu","Ancient Inca heritage meets modern gastronomy"),
        ("Colombia","South America","Bogota","Spanish","Yellow, blue, red horizontal stripes","51 million",["Colombia is the 2nd most biodiverse country on Earth","It produces the best emeralds in the world","Coffee is a major export and cultural cornerstone","The country is named after Christopher Columbus","Colombians celebrate New Year by carrying empty suitcases around the block for travel luck"],"Bandeja paisa, arepas, empanadas","Cartagena's walled old city","Coffee, biodiversity, and vibrant culture"),
        ("United Kingdom","Europe","London","English","Union Jack (red, white, blue crosses)","67 million",["The UK includes England, Scotland, Wales, and N. Ireland","Big Ben is actually the bell, not the tower","The London Underground is the oldest subway system (1863)","Tea is the national drink (165 million cups/day!)","English is spoken as a first language in 67 countries"],"Fish and chips, full English breakfast, scones","Tower of London & Big Ben","Monarchy, literature, and tea - culture exported worldwide"),
        ("France","Europe","Paris","French","Blue, white, red vertical stripes","67 million",["The Eiffel Tower was supposed to be temporary (built in 1889)","France has over 1,500 types of cheese!","French was the language of diplomacy for centuries","Tour de France is the world's most famous bike race","More tourists visit France than any other country (90M/year)"],"Croissants, crepes, baguettes, cheese","Eiffel Tower in Paris","Art, food, fashion, and revolution shaped the modern world"),
        ("Germany","Europe","Berlin","German","Black, red, gold horizontal stripes","83 million",["Germany has over 1,500 types of sausage (wurst)","The autobahn has sections with no speed limit","Kindergarten is a German word meaning 'children's garden'","Germany is Europe's largest economy","They recycle about 56% of waste (world leader!)"],"Bratwurst, pretzels, schnitzel","Brandenburg Gate in Berlin","Engineering excellence, automotive industry, environmental leadership"),
        ("Italy","Europe","Rome","Italian","Green, white, red vertical stripes","60 million",["Rome has a 2,700-year history","Italy has 55 UNESCO World Heritage Sites (most in world!)","The Renaissance started in Florence, Italy","Pizza and pasta originated here","Italy is shaped like a boot"],"Pizza, pasta, gelato, risotto","Colosseum in Rome","Art, history, fashion, food - Italy shaped Western civilization"),
        ("Spain","Europe","Madrid","Spanish","Red, yellow, red with coat of arms","47 million",["Spanish is spoken in 20+ countries worldwide","Spain has festivals almost every week somewhere","Siesta (afternoon nap) is a tradition","La Tomatina festival throws 150,000 tomatoes!","Flamenco dance originated in southern Spain"],"Paella, tapas, churros with chocolate","La Sagrada Familia in Barcelona","Passionate culture, fiestas, and a language spoken by 580 million"),
        ("Greece","Europe","Athens","Greek","Blue and white stripes with cross","10 million",["Greece is considered the birthplace of Western civilization","The first Olympic Games were held here in 776 BC","Greek mythology influenced art and literature worldwide","There are over 6,000 Greek islands (227 inhabited)","Democracy was invented in Athens 2,500 years ago"],"Gyros, moussaka, baklava, Greek salad","Parthenon in Athens","Where democracy, philosophy, and the Olympics were born"),
        ("Norway","Europe","Oslo","Norwegian","Red with blue cross outlined in white","5 million",["Norway has over 1,000 fjords (deep ocean inlets)","In summer, the sun doesn't set for weeks (midnight sun)","Norway is one of the happiest countries in the world","Vikings originated from Norway, Sweden, and Denmark","They have more electric cars per capita than any country"],"Salmon, brunost (brown cheese), lefse","The Fjords & Northern Lights","Vikings, fjords, northern lights, and highest happiness rankings"),
        ("Egypt","Africa","Cairo","Arabic","Red, white, black with golden eagle","104 million",["The Great Pyramid is the only surviving Ancient Wonder","Ancient Egyptian civilization lasted 3,000+ years","The Nile is the longest river in Africa (4,132 miles)","Egyptians invented one of the first writing systems","Modern Egypt has 100+ million people living mostly along the Nile"],"Koshari, ful medames, falafel","The Great Pyramids of Giza","Ancient wonders meet modern Africa on the banks of the Nile"),
        ("Nigeria","Africa","Abuja","English","Green, white, green vertical stripes","218 million",["Nigeria is Africa's most populous country","Nollywood (Nigerian film) produces 2,500+ movies per year","Over 500 languages are spoken in Nigeria","Nigeria has the largest economy in Africa","Lagos is one of the fastest-growing cities in the world"],"Jollof rice, suya, puff puff","Zuma Rock near Abuja","Africa's giant: population, economy, film, and music powerhouse"),
        ("Kenya","Africa","Nairobi","English & Swahili","Black, red, green with shield and spears","54 million",["Kenya is famous for wildlife safaris (Big Five animals)","Kenyan runners dominate world marathons","The Great Rift Valley runs through Kenya","Maasai warriors are known for their jumping dances","Kenya is a leader in mobile money (M-Pesa)"],"Ugali, nyama choma (grilled meat), chai","Maasai Mara National Reserve","Safari wildlife, world-class athletes, and tech innovation"),
        ("South Africa","Africa","Pretoria/Cape Town/Bloemfontein","11 official languages!","Six colors: black, yellow, green, white, red, blue","60 million",["South Africa has THREE capital cities","Nelson Mandela spent 27 years in prison before becoming president","Table Mountain is one of the oldest mountains on Earth","They have 11 official languages!","South Africa hosted Africa's first FIFA World Cup (2010)"],"Biltong, bobotie, bunny chow","Table Mountain in Cape Town","Rainbow Nation: diverse people, landscapes, and wildlife"),
        ("Morocco","Africa","Rabat","Arabic & Berber","Red with green star","37 million",["Morocco is only 8 miles from Europe (across Gibraltar strait)","The University of Fez (founded 859 AD) is the world's oldest","Moroccan markets (souks) are famous for haggling","The Sahara Desert covers southern Morocco","Moroccan architecture features stunning tile mosaics"],"Tagine, couscous, mint tea, pastilla","Hassan II Mosque in Casablanca","Where Africa meets the Mediterranean, blending Arab and Berber cultures"),
        ("Ethiopia","Africa","Addis Ababa","Amharic","Green, yellow, red with blue circle and star","120 million",["Ethiopia has its own calendar (13 months, 7 years behind!)","It's the only African country never colonized by Europeans","Coffee was discovered here (legend of a goat herder)","Lucy, a 3.2-million-year-old human ancestor, was found here","Ethiopian food is eaten with injera (spongy flatbread) instead of utensils"],"Injera with various stews (wats), coffee ceremony","Rock-hewn churches of Lalibela","Ancient civilization, coffee birthplace, unique calendar and alphabet"),
        ("Japan","Asia","Tokyo","Japanese","White with red circle (sun)","125 million",["Japan has the world's oldest company (1,400+ years old)","There are more pets than children in Japan","Japanese trains are punctual to the SECOND","Vending machines sell everything (even soup!)","Japan has 6,852 islands"],"Sushi, ramen, tempura, mochi","Mount Fuji & Tokyo Tower","Ancient traditions meet ultra-modern technology"),
        ("China","Asia","Beijing","Mandarin Chinese","Red with 5 yellow stars","1.4 billion",["China's Great Wall is over 13,000 miles long","Chinese civilization is 5,000+ years old","They invented paper, printing, compass, and gunpowder","China has the most people of any country","Mandarin has more native speakers than any language"],"Dumplings, noodles, Peking duck, dim sum","The Great Wall of China","The world's oldest continuous civilization and rising superpower"),
        ("India","Asia","New Delhi","Hindi & English (22 official languages)","Orange, white, green with blue wheel","1.4 billion",["India has more than 2,000 ethnic groups","Bollywood makes more films than Hollywood","India invented the number zero and the game of chess","The Taj Mahal took 22 years and 20,000 workers to build","India has the world's largest vegetarian population"],"Curry, naan bread, biryani, samosas","Taj Mahal in Agra","Ancient wisdom, vibrant culture, and the world's largest democracy"),
        ("South Korea","Asia","Seoul","Korean","White with red-blue circle and black symbols","52 million",["K-Pop is a global music phenomenon","South Korea has the fastest internet in the world","Korean BBQ is a social dining experience","Taekwondo originated here","Samsung, LG, and Hyundai are all Korean companies"],"Korean BBQ, bibimbap, kimchi, tteokbokki","Gyeongbokgung Palace in Seoul","Technology leader, K-pop, K-drama, and incredible food culture"),
        ("Thailand","Asia","Bangkok","Thai","Red, white, blue stripes","72 million",["Thailand means 'Land of the Free' - never colonized","Thai boxing (Muay Thai) is the national sport","Thailand has 40,000 Buddhist temples","The King is deeply revered by Thai people","Thai massage is famous worldwide"],"Pad Thai, green curry, mango sticky rice","Grand Palace in Bangkok","The Land of Smiles: temples, tropical beaches, and amazing food"),
        ("Saudi Arabia","Asia","Riyadh","Arabic","Green with white Arabic text and sword","35 million",["Saudi Arabia has no rivers - it's mostly desert","Mecca is the holiest city in Islam (2M+ pilgrims visit yearly)","Oil was discovered here in 1938, transforming the economy","Temperatures can reach 130F (54C) in summer","NEOM, a futuristic city, is being built from scratch"],"Kabsa, shawarma, dates, Arabic coffee","Mecca & Masjid al-Haram","Oil wealth, Islamic heritage, and ambitious modernization"),
        ("Australia","Oceania","Canberra","English","Blue with Union Jack and Southern Cross stars","26 million",["Australia has animals found nowhere else (kangaroos, koalas, platypus)","The Great Barrier Reef is visible from space","Australia is both a country AND a continent","It has more sheep than people (3 sheep per person!)","Aboriginal Australians have the oldest continuous culture (65,000+ years)"],"Meat pies, Vegemite on toast, pavlova","Sydney Opera House","Unique wildlife, ancient indigenous culture, and stunning landscapes"),
        ("New Zealand","Oceania","Wellington","English & Maori","Blue with 4 red stars (Southern Cross)","5 million",["New Zealand was the first country to give women the vote (1893)","The Maori haka (war dance) is performed before rugby games","Lord of the Rings was filmed here (Middle-earth!)","New Zealand has more sheep than people (6:1 ratio)","It was the last major land mass humans settled"],"Lamb, hangi (earth oven), pavlova, fish & chips","Fiordland & Milford Sound","Adventure sports, Maori culture, and breathtaking landscapes"),
        ("Fiji","Oceania","Suva","English, Fijian, Hindi","Light blue with Union Jack and shield","900,000",["Fiji has 333 islands (only 110 inhabited)","Fijians are known as the friendliest people on Earth","Kava ceremony is an important cultural tradition","Coral reefs surround most islands","The International Date Line passes through Fiji"],"Kokoda (raw fish), lovo (earth oven), cassava","Fiji's coral reefs & beaches","Paradise islands: crystal waters, warm people, and Polynesian culture"),
    ]

    title_page(doc, "AROUND THE WORLD IN 30 COUNTRIES", "A Kid's Geography Adventure (Ages 8-14)", "30 Countries * Fun Facts * Food * Landmarks * Activities")
    copyright_page(doc, "AROUND THE WORLD IN 30 COUNTRIES")
    
    # TOC
    doc.add_centered_text(720, "TABLE OF CONTENTS", 'F2', 18, 0)
    y = 690
    for i, (name, cont, _, _, _, _, _, _, _, _) in enumerate(countries):
        if y < 80:
            doc.new_page()
            y = 720
        doc.add_text(72, y, f"{i+1}. {name} ({cont})", 'F4', 10, 0.2)
        y -= 19
    doc.new_page()

    for idx, (name, continent, capital, language, flag, pop, facts, food, landmark, culture) in enumerate(countries):
        doc.add_text(72, 730, f"COUNTRY #{idx+1}", 'F1', 10, 0.4)
        doc.add_text(72, 708, name, 'F2', 20, 0)
        doc.add_line(72, 700, 300, 700, 1, 0.3)
        
        doc.add_text(72, 678, f"Continent: {continent}", 'F1', 10, 0.2)
        doc.add_text(72, 662, f"Capital: {capital}", 'F1', 10, 0.2)
        doc.add_text(72, 646, f"Language: {language}", 'F1', 10, 0.2)
        doc.add_text(72, 630, f"Flag: {flag}", 'F1', 10, 0.2)
        doc.add_text(72, 614, f"Population: {pop}", 'F1', 10, 0.2)
        
        y = 585
        doc.add_text(72, y, "FUN FACTS:", 'F2', 11, 0.1)
        y -= 16
        for f in facts:
            lines = wrap(f, 68)
            for j, l in enumerate(lines):
                doc.add_text(85, y, f"{'* ' if j==0 else '  '}{l}", 'F1', 9, 0.2)
                y -= 14
            y -= 3
        
        y -= 10
        doc.add_text(72, y, f"Kids eat for lunch: {food}", 'F4', 10, 0.2)
        y -= 18
        doc.add_text(72, y, f"Famous landmark: {landmark}", 'F4', 10, 0.2)
        y -= 18
        y = add_wrapped(doc, 72, y, f"Cultural note: {culture}", 'F1', 10, 0.3, 70)
        
        y -= 18
        doc.add_text(72, y, f"If I visited, I would: ____________________________________________", 'F1', 10, 0.4)
        doc.new_page()

    # World quiz
    doc.add_centered_text(720, "GEOGRAPHY QUIZ", 'F2', 18, 0)
    quiz_qs = ["Which country has the most people?","What's the only continent that's also a country?","Which country invented chocolate?","Where was democracy invented?","What country has 11 official languages?","Which country is shaped like a boot?","Where do kangaroos live in the wild?","What country has the fastest internet?","Where is the Great Wall?","What country was never colonized in Africa?"]
    y = 680
    for i, q in enumerate(quiz_qs):
        doc.add_text(72, y, f"{i+1}. {q} _________________________", 'F1', 11, 0.3)
        y -= 30
    doc.new_page()

    # Passport pages
    for i in range(2):
        doc.add_centered_text(720, "MY PASSPORT STAMP PAGE", 'F2', 16, 0)
        doc.add_centered_text(695, "Stamp or draw a mark for each country you learn about!", 'F4', 11, 0.3)
        y = 660
        for row in range(5):
            for col in range(3):
                x = 72 + col * 180
                doc.add_rect(x, y-80, 150, 80, 1, 0.4)
            y -= 110
        doc.new_page()

    certificate(doc, "WORLD EXPLORER CERTIFICATE")
    add_supplemental(doc, 'Geography', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book341_Kids_World_Geography.pdf')
    print("Book341_Kids_World_Geography.pdf created successfully!")

if __name__ == "__main__":
    create_book()
