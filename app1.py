import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
from collections import OrderedDict

# ---------------- CONFIG ----------------
API_KEY = "491d3e9f2b446ba09c5471cc53a02315"

st.set_page_config(page_title="Smart Weather Dashboard", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Settings")
st.sidebar.write("🌦️ Weather Dashboard")
st.sidebar.write("📊 Forecast + Prediction")

# ---------------- MAIN ----------------
st.title("🌦️ Smart Weather Dashboard")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    if city.strip() == "":
        st.warning("Please enter a city name")
        st.stop()

    # API URLs
    current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    current = requests.get(current_url).json()
    forecast = requests.get(forecast_url).json()

    # ---------------- ERROR ----------------
    if str(current.get("cod")) != "200":
        st.error("❌ City not found or API error")
        st.stop()

    # ---------------- CURRENT WEATHER ----------------
    st.subheader("📍 Current Weather")

    col1, col2, col3 = st.columns(3)

    col1.metric("🌡️ Temperature", f"{current['main']['temp']} °C")
    col2.metric("💧 Humidity", f"{current['main']['humidity']}%")
    col3.metric("💨 Wind Speed", f"{current['wind']['speed']} m/s")

    st.write("☁️ Condition:", current["weather"][0]["description"])

    # Coordinates
    st.write(f"📍 Location: Lat {current['coord']['lat']}, Lon {current['coord']['lon']}")

    # ---------------- ALERTS ----------------
    temp_now = current['main']['temp']

    if temp_now > 40:
        st.error("🔥 Heatwave Alert!")
    elif temp_now < 5:
        st.warning("❄️ Cold Wave Alert!")

    # ---------------- FORECAST FIXED ----------------
    st.subheader("📅 Weekly Forecast")

    daily_data = OrderedDict()

    for item in forecast["list"]:
        date = item["dt_txt"].split(" ")[0]

        if date not in daily_data:
            daily_data[date] = item

        if len(daily_data) == 7:
            break

    cols = st.columns(len(daily_data))

    temps = []
    days = []

    i = 0

    for date, data in daily_data.items():
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        day_name = date_obj.strftime("%A")
        date_str = date_obj.strftime("%d %b")

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        # Icons
        if "cloud" in condition:
            icon = "☁️"
        elif "rain" in condition:
            icon = "🌧️"
        elif "clear" in condition:
            icon = "☀️"
        else:
            icon = "🌤️"

        temps.append(temp)
        days.append(day_name)

        with cols[i]:
            st.markdown(f"### {day_name}")
            st.write(date_str)
            st.write(f"{icon} {condition}")
            st.write(f"🌡️ {temp} °C")

        i += 1

    # ---------------- GRAPH ----------------
    st.subheader("📊 Temperature Trend")

    plt.figure()
    plt.plot(days, temps, marker='o')
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.title("Weekly Temperature Trend")

    st.pyplot(plt)

    # ---------------- PREDICTION ----------------
    st.subheader("🔮 Prediction")

    X = np.arange(len(temps)).reshape(-1, 1)
    y = np.array(temps)

    model = LinearRegression()
    model.fit(X, y)

    next_temp = model.predict([[len(temps)]])

    st.success(f"Predicted Next Day Temperature: {next_temp[0]:.2f} °C")

# ---------------- FOOTER ----------------
st.markdown("---")
st.write("Built with ❤️ using Streamlit")