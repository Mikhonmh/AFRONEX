from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "16956c2253fcabae73c60b7ebc523eca"
api_url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q="

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'GET':
        return render_template("home.html")
    elif request.method == 'POST':
        city = request.form["city"]
        response = requests.get(api_url + city + "&appid=" + api_key)
        if response.status_code == 404:
            error = "City not found"
            return render_template("home.html", error=error)
        else:
            data = response.json()
            weather_icon = get_weather_icon(data["weather"][0]["main"])
            return render_template("home.html", data=data, weather_icon=weather_icon)

def get_weather_icon(weather_main):
    if weather_main == "Clouds":
        return "images/clouds.png"
    elif weather_main == "Clear":
        return "images/clear.png"
    elif weather_main == "Rain":
        return "images/rain.png"
    elif weather_main == "Drizzle":
        return "images/drizzle.png"
    elif weather_main == "Mist":
        return "images/mist.png"

if __name__ == "__main__":
    app.run(debug=True)
