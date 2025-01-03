from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "f84f0a9df87a4c8ea57231ae090c58a4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            try:
                response = requests.get(BASE_URL, params={
                    "q": city,
                    "appid": API_KEY,
                    "units": "metric"
                })
                print("Response Status Code:", response.status_code)
                print("Response JSON:", response.json())
                if response.status_code == 200:
                    weather_data = response.json()
                else:
                    error = f"Error {response.status_code}: {response.json().get('message', 'Unknown error')}"
            except requests.exceptions.RequestException as e:
                error = f"Request Exception: {e}"
        else:
            error = "City name cannot be empty."

    return render_template("weatherapp.html", weather_data=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
