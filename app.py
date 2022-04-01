import requests
from flask import Flask, render_template
from db.data import get_taxes
from api import generate_json
import json

app = Flask(__name__)

@app.route('/api/all')
def api_app():
    return generate_json(get_taxes())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes')
def recipes():

    reqUrl = "https://api.spoonacular.com/recipes/complexSearch?apiKey=de9eefef5b62421fbc904960928291be&equipment=pan"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

    return render_template('recipes.html', recipes=json.loads(response.text))

if __name__ == '__main__':
    app.run(debug=True)