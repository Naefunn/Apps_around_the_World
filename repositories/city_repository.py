from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.user import User


def select(id):
    cities = []
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        city = City(row['name'], row['description'], row['country_id'], row['visited'], row['id'] )
        cities.append(city)
    return cities


def save(city):
    sql = "INSERT INTO cities (name, description, country_id, visited) VALUES (%s, %s, %s, %s) RETURNING ID"
    values = [city.name, city.description, city.country_id, city.visited]
    results = run_sql(sql, values)
    city.id = results[0]['id']
    city.id = id
    return city

def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)