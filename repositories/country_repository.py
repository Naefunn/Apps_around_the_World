from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.user import User


def select_all():
    countries = []

    sql = "SELECT * FROM couuntries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['description'], row['id'] )
        countries.append(country)
    return countries


def save(country):
    sql = "INSERT INTO countries (name, description) VALUES (%s, %s) RETURNING ID"
    values = [country.name, country.description]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    # country.id = id
    return country