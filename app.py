import requests
import streamlit as st

st.title("Weather application")

api_key = '58f64f6810ed20ff8aeca702f748ddb1'

user_input = st.text_input("Enter city: ")

if st.button('Submit'):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        st.error("No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp_fahrenheit = weather_data.json()['main']['temp']
        temp_celsius = round((temp_fahrenheit - 32) * 5 / 9)

        st.success(f"The weather in {user_input} is: {weather}")
        st.success(f"The temperature in {user_input} is: {temp_celsius}ºC")
