import streamlit as st
import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def main():
    st.title("Weather App")
    st.write("Enter a city name to get the current weather.")

    city = st.text_input("City")

    if st.button("Get Weather"):
        if city:
            weather_data = get_weather(city)
            if weather_data["cod"] == "404":
                st.write("City not found. Please enter a valid city name.")
            else:
                temperature = weather_data["main"]["temp"]
                description = weather_data["weather"][0]["description"]
                humidity = weather_data["main"]["humidity"]
                st.write("Temperature:", temperature, "°C")
                st.write("Description:", description)
                st.write("Humidity:", humidity, "%")
        else:
            st.write("Please enter a city name.")

if __name__ == "__main__":
    main()
