from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.user import User


def select(country_id):
    cities = []

    sql = "SELECT * from cities where country_id = %s"
    values = [country_id]
    results = run_sql(sql)
    

    for row in results:
        city = City(row['name'], row['description'], row['country_id'], row['id'] )
        cities.append(city)
    return cities


def save(city):
    sql = "INSERT INTO cities (name, description, country_id) VALUES (%s, %s, %s) RETURNING ID"
    values = [city.name, city.description, city.country_id]
    results = run_sql(sql, values)
    city.id = results[0]['id']
    city.id = id
    return city

def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)