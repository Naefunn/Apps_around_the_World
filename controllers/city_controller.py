from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.country_repository as country_repository
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)


