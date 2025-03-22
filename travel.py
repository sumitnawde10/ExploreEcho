# Import necessary modules from Flask
from flask import Flask, request, render_template, redirect, url_for

# Import the list of places from a separate file (places.py)
from places import places

# Initialize the Flask app
app = Flask(__name__)

# route to the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('explore.html')
# route to the destination page
@app.route('/echo', methods=['GET'])
def func():
    return render_template('echo.html', places=places)
# Route: Processing User Selection and Showing Result
@app.route('/result', methods=['POST'])
def result():
     # Get user selections from the form
    selected_place = request.form['place']
    selected_budget = request.form['budget']
    selected_season = request.form['season']
    # Initialize variable to store place details
    place_info = None 
    for place in places:   # Search for the selected place in the 'places' list
        if place['name'].lower() == selected_place.lower():
            place_info = place
            break
# If the selected place exists in the dataset, extract budget and season information
    if place_info:
        # Extract budget and season information based on selected options
        budget_info = place_info['budget'].get(selected_budget)
        season_info = place_info['season'].get(selected_season)
 # Render the result page with selected details       
        return render_template('result.html', place=place_info, budget=budget_info, season=season_info)
    else:
        return "Selected place not found in data !"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
