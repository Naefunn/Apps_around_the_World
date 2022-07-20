import pdb
from models.city import City
from models.user import User
from models.country import Country

import repositories.city_repository as city_repository
import repositories.user_repository as user_repository
import repositories.country_repository as country_repository


country1 = Country('Spain', "I want to visit spain to see Barcelona and Madrid", False)
country_repository.save(country1)

country2 = Country('France', " I want to visit France to experience Paris and Lyon.", False)
country_repository.save(country2)

# country3 = Country('Germany', "a Western European country with a landscape of forests, rivers, mountain ranges and North Sea beaches. It has over 2 millennia of history. Berlin, its capital, is home to art and nightlife scenes, the Brandenburg Gate and many sites relating to WWII.")
# country_repository.save(country3)




