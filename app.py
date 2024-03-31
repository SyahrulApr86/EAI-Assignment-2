from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/daily_summary', methods=['GET'])
def daily_summary():
    date = request.args.get('date')
    if not date:
        return render_template('select_date.html')
    else:
        lat = '-6.364393516159703'
        lon = '106.82869342169275'
        tz = '+07:00'
        appid = os.getenv('OPENWEATHERMAP_API_KEY')
        url = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date}&tz={tz}&appid={appid}"
        response = requests.get(url)
        weather_data = response.json()
        return render_template('daily_summary.html', weather=weather_data, date=date)

@app.route('/cat', methods=['GET'])
def get_cat():
    api_key = os.getenv('THE_CAT_API_KEY')
    headers = {'x-api-key': api_key}
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url, headers=headers).json()[0]

    return render_template('cat.html', cat=response)

if __name__ == '__main__':
    app.run(debug=True)
