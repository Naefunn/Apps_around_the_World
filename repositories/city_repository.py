from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.user import User
import repositories.country_repository as country_repository

def select_by_country(country_id):
    cities = []
    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country_id]
    results = run_sql(sql, values)
    for row in results:
        city = City(row['name'], row['description'], row['country_id'], row['visited'], row['id'] )
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        city = City(result['name'], result['description'], result['country_id'], result['visited'], result['id'] )
    return city


def save(city):
    sql = "INSERT INTO cities (name, description, country_id, visited) VALUES (%s, %s, %s, %s) RETURNING ID"
    values = [city.name, city.description, city.country_id.id, city.visited]
    results = run_sql(sql, values) 
    id = results[0]['id']
    city.id = id
    

def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def show_visited():
    cities = []
    sql = "SELECT * FROM cities WHERE visited = true"
    results = run_sql(sql)
    for row in results:
        city = City(row['name'], row['description'], row['visited'], row['id'] )
        cities.append(city)
    return cities

def show_not_visited():
    cities = []
    sql = "SELECT * FROM cities WHERE visited = false"
    results = run_sql(sql)
    for row in results:
        city = City(row['name'], row['description'], row['visited'], row['id'] )
        cities.append(city)
    return cities