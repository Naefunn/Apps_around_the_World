from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

@countries_blueprint.route("/countries/<id>")
def city(id):
    cities = city_repository.select(id)
    return render_template('cities/index.html', cities = cities)
