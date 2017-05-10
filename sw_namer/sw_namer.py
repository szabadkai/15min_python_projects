# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import csv
import random
from collections import namedtuple
import json

app = Flask(__name__)
Planet = namedtuple("Planet", ["name", "gravity", "population"])

planets = []

try:
    with open('planets.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            planets.append(Planet(row))

except IOError as e:
    pass


@app.route("/planets/<n>")
@app.route("/planets")
def planets(n=1):
    return json.dumps(planets)
