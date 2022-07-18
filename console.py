import pdb
from models.city import City
from models.user import User
from models.country import Country

import repositories.city_repository as city_repository
import repositories.user_repository as user_repository
import repositories.country_repository as country_repository


country1 = Country('Spain', "Spain, a country on Europe's Iberian Peninsula, includes 17 autonomous regions with diverse geography and cultures.")
country_repository.save(country1)