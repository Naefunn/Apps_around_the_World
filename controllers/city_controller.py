from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.country_controller import countries
from models.city import City

import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)


@cities_blueprint.route('/cities/new', methods = ['GET'])
def new_country():
    return render_template('cities/new.html')

# @cities_blueprint.route('/countries/<countries.id>',  methods=['POST'])
# def create_city():
#     name = request.form['name']
#     description = request.form['description']

#     city = City(name, description)
#     city_repository.save(city)
#     return redirect('/cities')
