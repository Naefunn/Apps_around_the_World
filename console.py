import pdb
from models.city import City
from models.user import User
from models.country import Country

import repositories.city_repository as city_repository
import repositories.user_repository as user_repository
import repositories.country_repository as country_repository


country1 = Country('Spain', "a country on Europe's Iberian Peninsula, includes 17 autonomous regions with diverse geography and cultures.")
country_repository.save(country1)

country2 = Country('France', " a country in Western Europe, encompasses medieval cities, alpine villages and Mediterranean beaches. Paris, its capital, is famed for its fashion houses, classical art museums including the Louvre and monuments like the Eiffel Tower.")
country_repository.save(country2)

# country3 = Country('Germany', "a Western European country with a landscape of forests, rivers, mountain ranges and North Sea beaches. It has over 2 millennia of history. Berlin, its capital, is home to art and nightlife scenes, the Brandenburg Gate and many sites relating to WWII.")
# country_repository.save(country3)

city1 = City('Seville', "Seville is the capital and largest city of the Spanish autonomous community of Andalusia and the province of Seville.", 1 )
city_repository.save(city1)

city2 = City('Paris', "Paris is one of the most beautiful cities in the world. It is known worldwide for the Louvre Museum, Notre-Dame cathedral, and the Eiffel tower.", 2)
city_repository.save(city2)

# city3 = City('Berlin', "Berlin, Germany's capital, dates to the 13th century.", 3)
# city_repository.save(city3)

