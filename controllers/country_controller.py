from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)


@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')

@countries_blueprint.route('/countries/new', methods = ['GET'])
def new_country():
    return render_template('countries/new.html')

@countries_blueprint.route("/countries",  methods=['POST'])
def create_country():
    name = request.form['name']
    description = request.form['description']
    country     = Country(name, description)
    country_repository.save(country)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', countries = country)

@countries_blueprint.route('/countries/<id>/edit', methods=['POST'])
def update_country(id):
    name = request.form['name']
    description = request.form['description']
    country = country_repository.select(id)
    country.name = name
    country.description = description
    country_repository.update(country)
    return redirect('/countries')
