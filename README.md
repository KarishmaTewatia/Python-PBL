# 🌦️ Smart Weather Dashboard

A Python-based interactive weather monitoring dashboard built using **Streamlit** and **OpenWeatherMap API**.  
The project provides real-time weather updates, weekly forecasts, temperature trend visualization, weather alerts, and simple machine learning-based temperature prediction.

---

# 🎯 Objective

The objective of this project is to create an interactive weather monitoring system that:

- Fetches real-time weather data
- Displays weekly weather forecast
- Visualizes temperature trends
- Predicts future temperature
- Provides alerts for extreme weather conditions

This project is related to **SDG 13 – Climate Action**, as it promotes awareness about weather conditions and climate monitoring.

---

# 🚀 Features

## ✅ Real-Time Weather Monitoring
Displays:
- Temperature
- Humidity
- Wind Speed
- Weather Condition

---

## ✅ Weekly Weather Forecast
Shows:
- Day-wise forecast
- Date
- Weather condition
- Temperature

---

## ✅ Interactive Dashboard
Built using Streamlit with:
- Clean UI
- Column layout
- Sidebar
- Weather icons

---

## ✅ Temperature Trend Graph
Visual representation of weekly temperature changes using Matplotlib.

---

## ✅ Weather Alerts
Displays alerts for:
- Heatwaves
- Cold weather conditions

---

## ✅ Machine Learning Prediction
Uses Linear Regression to predict the next day's temperature based on forecast data.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application framework |
| OpenWeatherMap API | Weather data source |
| Requests | API communication |
| Matplotlib | Graph plotting |
| Scikit-learn | Machine learning prediction |

---

# 📂 Project Structure

```text
project-folder/
│
├── app.py
├── README.md
```

---

# ⚙️ Installation

## Step 1: Clone or Download the Project

Download the project files to your system.

---

## Step 2: Install Required Libraries

Run the following command in terminal:

```bash
pip3 install streamlit requests matplotlib scikit-learn
```

---

# 🔑 API Setup

1. Create an account on OpenWeatherMap
2. Generate your API key
3. Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual API key inside `app.py`

---

# ▶️ Running the Project

Run the following command:

```bash
python3 -m streamlit run app.py
```

The application will automatically open in your browser.

---

# 📊 How It Works

1. User enters city name
2. API request is sent to OpenWeatherMap
3. JSON weather data is received
4. Current weather is displayed
5. Forecast data is processed day-wise
6. Temperature graph is generated
7. Linear Regression predicts future temperature
8. Alerts are shown for extreme conditions

---

# 🧠 Machine Learning Used

The project uses:
- **Linear Regression**

Purpose:
- Predict next day's temperature using available forecast trend data.

---

# 🌍 SDG 13 Connection

This project supports:

## **SDG 13 – Climate Action**

By:
- Promoting climate awareness
- Monitoring weather conditions
- Providing forecast insights
- Encouraging data-driven environmental understanding

---

# 🔥 Future Improvements

Possible future enhancements:
- Dark mode
- Weather maps
- Rainfall prediction
- Air Quality Index (AQI)
- Location auto-detection
- Mobile responsiveness

---

# 🎤 Viva Explanation (Short)

> “This project is a smart weather dashboard that fetches real-time and forecast weather data using APIs, visualizes trends, predicts future temperature using machine learning, and provides alerts for extreme weather conditions.”

---

# 👨‍💻 Developed Using

- Python
- Streamlit
- OpenWeatherMap API

---

# ❤️ Conclusion

The Smart Weather Dashboard successfully demonstrates:
- API integration
- Data processing
- Visualization
- Web development
- Basic machine learning concepts

It transforms a simple weather monitoring script into an interactive and intelligent analytical dashboard.
