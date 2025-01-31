from flask import Flask, request, render_template, redirect, url_for
from places import places

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('explore.html')

@app.route('/echo', methods=['GET'])
def func():
    return render_template('echo.html', places=places)

@app.route('/result', methods=['POST'])
def result():
    selected_place = request.form['place']
    selected_budget = request.form['budget']
    selected_season = request.form['season']
    
    place_info = None 
    for place in places:
        if place['name'].lower() == selected_place.lower():
            place_info = place
            break

    if place_info:
        # Extract budget and season information based on selected options
        budget_info = place_info['budget'].get(selected_budget)
        season_info = place_info['season'].get(selected_season)
        
        return render_template('result.html', place=place_info, budget=budget_info, season=season_info)
    else:
        return "Selected place not found in data !"


if __name__ == '__main__':
    app.run(debug=True)
