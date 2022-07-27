
from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.user import User


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['description'], row['visited'], row['id'] )
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        country = Country(row['name'], row['description'], row['visited'], row['id'] )
    return country


def save(country):
    sql = "INSERT INTO countries (name, description, visited) VALUES (%s, %s, %s) RETURNING ID"
    values = [country.name, country.description, country.visited]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    country.id = id
    return country

def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (name, description, visited) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.description, country.visited, country.id]
    run_sql(sql, values)
