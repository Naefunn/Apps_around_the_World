from flask import Flask, render_template, request, redirect
from flask import Blueprint



cities_blueprint = Blueprint("cities", __name__)