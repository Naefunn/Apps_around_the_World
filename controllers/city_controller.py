from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.country_controller import countries
from models.city import City

import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/countries/<id>")
def city(id):
    cities = city_repository.select_by_country(id)
    countries = country_repository.select(id)
    return render_template('cities/index.html', all_cities = cities, countries = countries)


@cities_blueprint.route('/countries/<id>/new', methods = ['GET'])
def new_city(id):
    countries = country_repository.select(id)
    return render_template('/cities/new.html', countries=countries)

@cities_blueprint.route('/countries/<id>/save',  methods=['POST'])
def create_city(id):
    name = request.form['name']
    description = request.form['description']
    visited = request.form['visited']
    countries = country_repository.select(id)
    city = City(name, description, countries, visited)
    city_repository.save(city)
    return redirect(f'/countries/{id}')


# @cities_blueprint.route("/countries/<id>/delete", methods=['POST'])
# def delete_country(id):
#     city_repository.delete(id)
#     return redirect(f'/countries/{id}')
