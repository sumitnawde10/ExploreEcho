##------Data -------##
places = [
    {
        'name': 'Paris',
        'description': "Paris, the capital of France, is renowned for its iconic landmarks, rich history, and vibrant culture. From the majestic Eiffel Tower to the artistic ambiance of Montmartre, Paris offers a tapestry of experiences for visitors. Its charming streets, world-class museums like the Louvre, and exquisite cuisine make it a dream destination for travelers from around the globe.",
        'budget': {
            'low': {'description': "Accommodation: Budget hotels, hostels, or Airbnb: $50 - $100 per night Food: Local bistros, bakeries, and street markets: $15 - $30 per day Transportation: Public transportation passes and walking: $5 - $15 per day Activities: Free attractions, parks, and self-guided tours: $0 - $20 per day Total: Approximately $70 - $165 per day"},
            'medium': {'description': "Accommodation: Mid-range hotels or vacation rentals: $100 - $200 per night Food: Moderate restaurants and occasional upscale dining: $30 - $60 per day Transportation: Metro, occasional taxis, and day trips: $15 - $30 per day Activities: Museum entrances, boat cruises, and guided tours: $20 - $50 per day Total: Approximately $165 - $340 per day"},
            'high': {'description': "Accommodation: Luxury hotels or boutique stays: $200 - $500+ per night Food: Fine dining restaurants and gourmet experiences: $80 - $200+ per day Transportation: Private transfers, taxis, and premium train tickets: $50 - $100+ per day Activities: Exclusive tours, theater shows, and private guides: $100 - $300+ per day Total: Approximately $430 - $1100+ per day"}
        },
        'season': {
            'summer': {'description': "Summer: Enjoy picnics along the Seine River, visit outdoor markets like Marché Bastille, explore the gardens of Versailles, and attend outdoor festivals and concerts."},
            'winter': {'description':"Winter: Experience the magical Christmas markets, ice skating at Hotel de Ville, admire holiday lights along Champs-Élysées, and cozy up in cafes with hot chocolate."},
            'rainy': {'description': "Rainy Season: Explore indoor attractions like the Louvre Museum, take a culinary tour of Parisian cafes, visit covered passages like Galerie Vivienne, and indulge in shopping at department stores like Galeries Lafayette."}
        }
    },
    {
        'name': 'Tokyo',
        'description': "Tokyo, the bustling capital of Japan, is a vibrant metropolis where tradition meets modernity. Its a city of contrasts, where ancient temples stand alongside futuristic skyscrapers. With a population exceeding 13 million people, Tokyo is one of the most populous cities in the world, and its metropolitan area is even larger.From the serene gardens of the Imperial Palace to the bustling streets of Shinjuku and Shibuya, Tokyo offers something for everyone. Its culinary scene is world-famous, with a plethora of Michelin-starred restaurants, cozy izakayas, and street food stalls serving up delicious dishes ranging from sushi and ramen to tempura and okonomiyaki.",
        'budget': {
            'low': {'description':"Accommodation: Luxury hotels or high-end ryokans: $250 - $500 per night, Food: Fine dining restaurants and upscale eateries: $50 - $150 per day, Transportation: Taxis, private transfers, or first-class train tickets: $50 - $100 per day, Activities: Guided tours, special exhibitions, and premium experiences: $100 - $200 per day, Total: Approximately $450 - $950 per day"
        },
            'medium': {'description':"Accommodation: Mid-range hotels or traditional guesthouses: $100 - $250 per night, Food: Casual dining, street food, and occasional nicer meals: $20 - $50 per day, Transportation: Public transportation passes and occasional taxis: $10 - $30 per day, Activities: Museum entrances, city tours, and moderate activities: $30 - $80 per day, Total: Approximately $160 - $410 per day"
        },
            'high': {'description':"Accommodation: Budget hotels, hostels, or capsule hotels: $50 - $100 per night, Food: Budget-friendly eateries, convenience stores, and cooking some meals: $10 - $20 per day, Transportation: Utilizing mainly public transportation and walking: $5 - $10 per day, Activities: Free attractions, parks, and self-guided tours: $0 - $20 per day, Total: Approximately $65 - $150 per day"
        }
        },
        'season': {
            'summer': {'description':"Escape the city heat and immerse yourself in the tranquil beauty of Shinjuku Gyoen National Garden. This expansive garden features traditional Japanese landscapes and various plant species, providing a serene retreat from the bustling streets of Tokyo."
},
            'winter': {'description':"Marvel at the winter cityscape from the observation decks of Tokyo Skytree, offering panoramic views of Tokyo Tower, Mount Fuji, and beyond.Witness the city aglow with dazzling light displays during Tokyo's winter illumination events, such as those at Shiodome Caretta, Roppongi Hills, and Yebisu Garden Place."
},
            'rainy': {'description':"Enjoy panoramic views of the city from the observation decks of the Tokyo Metropolitan Government Building. This iconic skyscraper offers stunning vistas even on rainy days, providing visitors with a memorable experience of Tokyo's skyline."
}
        }
    },
    {
        'name': 'New York',
        'description': "New York City, the cultural and financial capital of the United States, is a vibrant metropolis renowned for its iconic landmarks, diverse neighborhoods, and rich cultural scene. From the bright lights of Times Square to the greenery of Central Park and the historic charm of neighborhoods like Greenwich Village, New York offers something for everyone.",
        'budget': {
            'low': {'description': "Accommodation: Budget hotels or hostels: $100 - $200 per night, Food: Casual dining and street food: $20 - $50 per day, Transportation: Public transit and walking: $10 - $20 per day, Activities: Free attractions and parks: $0 - $20 per day."},
            'medium': {'description': "Accommodation: Mid-range hotels or vacation rentals: $200 - $400 per night, Food: Dining at a mix of restaurants: $50 - $100 per day, Transportation: Public transit and occasional taxis: $20 - $50 per day, Activities: Museums, shows, and tours: $50 - $150 per day."},
            'high': {'description': "Accommodation: Luxury hotels or boutique stays: $400 - $800 per night, Food: Fine dining and upscale experiences: $100 - $200 per day, Transportation: Private transfers and taxis: $50 - $100 per day, Activities: Premium tours and experiences: $200 - $500 per day."}
        },
        'season': {
            'summer': {'description':"Enjoy outdoor activities like picnics in Central Park, strolling along the High Line, visiting Coney Island and its beaches, attending outdoor concerts and festivals, and taking boat tours around Manhattan."},
            'winter': {'description': " Experience the magic of the holiday season with ice skating at Rockefeller Center, marveling at festive window displays along Fifth Avenue, visiting holiday markets like Bryant Park's Winter Village, catching a Broadway show, and exploring indoor attractions like museums."},
            'rainy': {'description':"Take shelter in world-class museums such as the Metropolitan Museum of Art, Museum of Modern Art (MoMA), and American Museum of Natural History. Enjoy indoor activities like shopping in iconic department stores, dining at renowned restaurants, exploring indoor markets like Chelsea Market, and catching a Broadway matinee."}
        }
    },
    {
        'name': 'London',
        'description': "London, the vibrant capital of the United Kingdom, is a city steeped in history, culture, and modernity. From iconic landmarks like Big Ben and the Tower of London to world-class museums such as the British Museum and Tate Modern, London offers a diverse range of attractions for visitors. Its bustling streets are lined with theaters, shops, and restaurants, catering to every taste and interest. With its extensive public transportation network, including the famous London Underground, exploring the city is convenient and accessible.",
        'budget': {
            'low': {'description': "Accommodation: Budget hotels, hostels, or Airbnb: £40 - £80 per night Food: Street food, budget-friendly eateries, and cooking some meals: £10 - £20 per day Transportation: Oyster card for public transportation and walking: £5 - £10 per day Activities: Free attractions, parks, and self-guided tours: £0 - £20 per day Total: Approximately £55 - £130 per day "},
            'medium': {'description': "Accommodation: Mid-range hotels or serviced apartments: £80 - £150 per night Food: Casual dining, cafes, and occasional nicer meals: £20 - £50 per day Transportation: Oyster card or occasional taxis: £10 - £30 per day Activities: Museum entrances, guided tours, and moderate activities: £30 - £80 per day Total: Approximately £140 - £310 per day"},
            'high': {'description': "Accommodation: Luxury hotels or boutique accommodations: £150 - £300+ per night Food: Fine dining restaurants and upscale eateries: £50 - £150 per day Transportation: Taxis, private transfers, or first-class train tickets: £50 - £100 per day Activities: West End shows, special exhibitions, and premium experiences: £100 - £200 per day Total: Approximately £350 - £750+ per day"}
        },
        'season': {
            'summer': {'description':"Enjoy picnics in Hyde Park, explore the Thames River on a boat tour, visit outdoor markets like Borough Market, and attend festivals like Notting Hill Carnival." },
            'winter': {'description': "Experience the festive atmosphere at Winter Wonderland in Hyde Park, go ice skating at Somerset House or the Natural History Museum, and shop at Christmas markets like Southbank Centre Winter Market."},
            'rainy': {'description':"Seek shelter in world-class museums such as the British Museum, National Gallery, or Victoria and Albert Museum, explore indoor markets like Covent Garden, and enjoy afternoon tea at iconic venues like The Ritz or The Savoy." }
        }
    },
    {
        'name': 'Sydney',
        'description': "Sydney, the vibrant capital of New South Wales, Australia, is renowned for its stunning beaches, iconic landmarks, and thriving cultural scene. With its picturesque harbor, diverse neighborhoods, and plethora of attractions, Sydney offers something for every traveler.",
        'budget': {
            'low': {'description': "Accommodation: Budget hostels or shared accommodations: $30 - $70 per night Food: Affordable eateries, street food, and cooking some meals: $10 - $30 per day Transportation: Public transportation, walking, and occasional rideshare: $5 - $15 per day Activities: Free attractions, beach visits, and self-guided tours: $0 - $20 per day Total: Approximately $45 - $135 per day"},
            'medium': {'description': "Accommodation: Mid-range hotels or serviced apartments: $80 - $150 per night Food: Casual dining, cafes, and occasional nicer meals: $30 - $60 per day Transportation: Public transportation passes and occasional taxi rides: $15 - $30 per day Activities: Museum entrances, guided tours, and moderate activities: $20 - $50 per day Total: Approximately $145 - $290 per day"},
            'high': {'description': "Accommodation: Luxury hotels or waterfront resorts: $200 - $500 per night Food: Fine dining restaurants and gourmet experiences: $80 - $200 per day Transportation: Private transfers, taxis, and luxury car rentals: $50 - $150 per day Activities: Harbor cruises, helicopter tours, and exclusive experiences: $100 - $300 per day Total: Approximately $430 - $1150 per day"}
        },
        'season': {
            'summer': {'description': "Summer (December - February): Enjoy sunbathing and swimming at Bondi Beach or Manly Beach. Take a ferry ride to explore Sydney Harbour and visit attractions like the Sydney Opera House and Sydney Harbour Bridge. Attend outdoor festivals and events, such as the Sydney Festival and New Year's Eve celebrations."},
            'winter': {'description': "Winter (June - August): Visit cultural institutions like the Art Gallery of New South Wales or the Australian Museum. Explore The Rocks district and indulge in cozy dining experiences at local cafes and restaurants. Attend the Vivid Sydney festival to witness stunning light installations and multimedia displays."},
            'rainy': {'description': "Rainy Season (March - May, September - November): Explore indoor attractions such as the SEA LIFE Sydney Aquarium or the Powerhouse Museum. Take a guided food tour to sample diverse cuisines and culinary delights. Experience the city's vibrant nightlife scene with live music and entertainment options."}
        }
    },
    {
        'name': 'Rome',
        'description': "Rome, the Eternal City, is a captivating blend of ancient history, magnificent architecture, and vibrant culture. As the capital of Italy, Rome boasts iconic landmarks, world-class museums, and delectable cuisine, making it a top destination for travelers from around the globe.",
        'budget': {
            'low': {'description': "Accommodation: Budget hotels, hostels, or guesthouses: €30 - €70 per night Food: Affordable trattorias, street food, and occasional self-catering: €10 - €30 per day Transportation: Public transportation, walking, and occasional rideshare: €5 - €15 per day Activities: Free attractions, self-guided tours, and inexpensive museum visits: €0 - €20 per day Total: Approximately €45 - €135 per day"},
            'medium': {'description':"Accommodation: Mid-range hotels or vacation rentals: €80 - €150 per night Food: Casual dining, cafes, and occasional nicer meals: €30 - €60 per day Transportation: Metro passes, taxi rides, and occasional guided tours: €15 - €30 per day Activities: Guided tours, museum entrances, and moderate experiences: €20 - €50 per day Total: Approximately €145 - €290 per day"},
            'high': {'description': "Accommodation: Luxury hotels or boutique accommodations: €200 - €500 per night Food: Fine dining restaurants, gourmet experiences, and wine tastings: €80 - €200 per dayTransportation: Private transfers, chauffeur services, and luxury car rentals: €50 - €150 per day Activities: Exclusive tours, private guides, and VIP access to attractions: €100 - €300 per day sTotal: Approximately €430 - €1150 per day"}
        },
        'season': {
            'summer': {'description': "Summer (June - August): Explore ancient ruins such as the Colosseum, Roman Forum, and Palatine Hill in the cooler mornings. Visit Vatican City and St. Peter's Basilica early to avoid crowds and heat. Enjoy outdoor dining in charming piazzas and gardens, savoring gelato and refreshing drinks."},
            'winter': {'description': "Winter (December - February): Admire the festive decorations and nativity scenes during the Christmas season. Explore indoor attractions like the Vatican Museums, Capitoline Museums, and Borghese Gallery. Indulge in hearty Roman cuisine, including pasta dishes and warming soups, at trattorias and osterias."},
            'rainy': {'description': "Rainy Season (March - May, September - November): Visit indoor markets like Mercato Centrale and Campo de' Fiori for local produce and gourmet treats. Attend cultural events and exhibitions, such as Rome's International Film Festival and art shows. Take shelter in historic churches and basilicas, marveling at their magnificent architecture and art."}
        }
    },
    {
        'name': 'Rio de Janeiro',
        'description': "Rio de Janeiro, often called The Marvelous City, is a vibrant metropolis nestled between lush mountains and beautiful beaches in Brazil. Known for its stunning natural landscapes, vibrant culture, and lively atmosphere, Rio captivates visitors from around the world.",
        'budget': {
            'low': {'description': "Accommodation: Budget hostels or guesthouses: $20 - $50 per night Food:Street food, local eateries, and cooking some meals: $10 - $20 per day Transportation: Public buses, metro, and walking: $5 - $10 per day Activities: Free attractions, beach visits, and self-guided tours: $0 - $20 per day Total: Approximately $35 - $100 per day"},
            'medium': {'description': "Accommodation: Mid-range hotels or vacation rentals: $50 - $150 per night Food: Casual dining, cafes, and occasional nicer meals: $20 - $50 per day Transportation: Taxis, rideshare, and occasional tours: $10 - $30 per day Activities: Museum entrances, guided tours, and moderate activities: $20 - $50 per day Total: Approximately $100 - $280 per day"},
            'high': {'description': "Accommodation: Luxury hotels or beachfront resorts: $150 - $500 per night Food: Fine dining restaurants and gourmet experiences: $50 - $200 per day Transportation: Private transfers, taxis, and luxury car rentals: $30 - $100 per day Activities: Boat tours, helicopter rides, and exclusive experiences: $100 - $300 per day Total: Approximately $330 - $1100 per day"}
        },
        'season': {
            'summer': {'description': "Summer (December - February): Relax on the world-famous Copacabana or Ipanema beaches and soak up the sun. Experience the vibrant energy of Rio's Carnival with parades, samba dancing, and street parties. Hike to the summit of Sugarloaf Mountain or explore the Tijuca Forest for stunning views and outdoor adventures."},
            'winter': {'description': "Winter (June - August): Take a cable car ride to the top of Sugarloaf Mountain for panoramic views of the city. Visit the iconic Christ the Redeemer statue atop Corcovado Mountain for breathtaking vistas. Explore Rio's cultural heritage with visits to museums, historic neighborhoods like Santa Teresa, and live music performances."},
            'rainy': {'description': "Rainy Season (March - May, September - November): Explore Rio's vibrant street art scene in neighborhoods like Lapa and Santa Teresa. Indulge in Brazilian cuisine at local markets, street food stalls, and traditional restaurants. Attend indoor cultural events, concerts, and theater performances to experience Rio's rich cultural diversity."}
        }
    },
    {
        'name': 'Cairo',
        'description': "Cairo, the bustling capital of Egypt, is a vibrant metropolis rich in history, culture, and heritage. From ancient pyramids and temples to bustling markets and vibrant neighborhoods, Cairo offers a captivating blend of old-world charm and modern energy.",
        'budget': {
            'low': {'description': "Accommodation: Budget hotels, hostels, or guesthouses: $20 - $50 per night Food: Street food, local eateries, and budget-friendly restaurants: $5 - $15 per day Transportation: Public buses, metro, and walking: $1 - $5 per day Activities: Visiting museums, exploring historic sites, and free attractions: $5 - $15 per day Total: Approximately $31 - $85 per day"},
            'medium': {'description': "Accommodation: Mid-range hotels or Airbnb rentals: $50 - $100 per night Food: Casual dining, traditional Egyptian cuisine, and occasional nicer meals: $15 - $30 per day Transportation: Taxis, Uber, and occasional tours: $10 - $20 per day Activities: Guided tours, Nile River cruises, and entrance fees to attractions: $20 - $50 per day Total: Approximately $95 - $200 per day"},
            'high': {'description': "Accommodation: Luxury hotels or boutique accommodations: $100 - $300+ per night Food: Fine dining restaurants, international cuisine, and gourmet experiences: $30 - $100+ per day Transportation: Private drivers, luxury car rentals, and guided tours: $50 - $150+ per day Activities: Private guided tours, exclusive experiences, and VIP access: $50 - $200+ per day Total: Approximately $230 - $750+ per day"}
        },
        'season': {
            'summer': {'description': "Summer (June - August): Explore the iconic landmarks of Cairo, such as the Pyramids of Giza, the Sphinx, and the Egyptian Museum. Take a felucca ride on the Nile River to enjoy the breeze and views of the city skyline. Visit the Khan El Khalili bazaar for shopping and experiencing the vibrant atmosphere."},
            'winter': {'description': "Winter (December - February): Take a day trip to explore the ancient wonders of Luxor and Aswan, including the Valley of the Kings and Abu Simbel temples. Enjoy a traditional Egyptian meal at a local restaurant while overlooking the Nile River. Attend cultural events and festivals, such as the Cairo International Film Festival or the Cairo Jazz Festival."},
            'rainy': {'description': "Rainy Season (Limited rainfall, mainly in winter): Visit the Coptic Cairo district to explore historic churches and religious sites, such as the Hanging Church and the Church of St. Sergius. Discover the Islamic architecture and landmarks in Old Cairo, including the Al-Azhar Mosque and the Citadel of Saladin. Indulge in Egyptian cuisine, including falafel, koshari, and traditional sweets, at local eateries and street food stalls."}
        }
    },
    {
        'name': 'India',
        'description': "India, a diverse and culturally rich country in South Asia, is known for its ancient heritage, vibrant festivals, and breathtaking landscapes. From bustling cities to serene countryside, India offers a kaleidoscope of experiences for travelers.",
        'budget': {
            'low': {'description': "Accommodation: Budget guesthouses, hostels, or homestays: $5 - $30 per night Food: Street food, local eateries, and cooking some meals: $3 - $10 per day Transportation: Public buses, trains, and shared taxis: $2 - $15 per day Activities: Visiting free attractions, exploring markets, and hiking: $0 - $10 per day Total: Approximately $10 - $65 per day"},
            'medium': {'description': "Accommodation: Mid-range hotels, guesthouses, or heritage properties: $30 - $100 per night Food: Casual dining, regional cuisine, and occasional nicer meals: $10 - $30 per day Transportation: Train travel, private taxis, and occasional flights: $15 - $50 per day Activities: Entrance fees to monuments, guided tours, and cultural experiences: $10 - $50 per day Total: Approximately $65 - $230 per day"},
            'high': {'description': "Accommodation: Luxury hotels, boutique resorts, or palace stays: $100 - $500 per night Food: Fine dining restaurants, gourmet experiences, and international cuisine: $30 - $150 per day Transportation: Private drivers, domestic flights, and luxury train journeys: $50 - $200 per day Activities: Exclusive tours, spa treatments, and personalized experiences: $50 - $300 per day Total: Approximately $230 - $1150 per day"}
        },
        'season': {
            'summer': {'description': "Summer (March - June): Explore the hill stations of Himachal Pradesh, Uttarakhand, and Kashmir to escape the heat. Attend festivals like Holi and experience cultural celebrations across the country. Visit the beaches of Goa, Kerala, and Andaman and Nicobar Islands for a coastal retreat.  "},
            'winter': {'description': "Winter (November - February): Explore the iconic landmarks of Delhi, Agra, and Jaipur on the Golden Triangle circuit. Embark on wildlife safaris in national parks such as Ranthambore and Jim Corbett. Experience the vibrant culture of Rajasthan during the Pushkar Camel Fair and Jaipur Literature Festival."},
            'rainy': {'description': "Rainy Season (July - September): Witness the lush greenery of the Western Ghats and explore hill stations like Munnar and Coorg. Visit the UNESCO World Heritage Sites of Hampi and Mahabalipuram during the monsoon. Attend traditional festivals such as Onam in Kerala and Ganesh Chaturthi in Maharashtra."}
        }
        
        
    }
]