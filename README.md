# 🚗 Fuel Optimization Route API (Django)

## 📌 Overview

This project is a backend API built using Django and Django REST Framework that calculates the optimal route between two locations in the USA and determines the most cost-effective fuel stops along the route.

It integrates a third-party routing service and applies optimization logic to minimize fuel costs based on distance, vehicle range, and fuel prices.

---

## 🎯 Problem Statement

Given:

* Start location (latitude, longitude)
* End location (latitude, longitude)

The API will:

* Calculate the best route between locations
* Suggest optimal fuel stops (every 500 miles)
* Select cost-effective fuel stations
* Compute total fuel cost (assuming 10 miles per gallon)

---

## ⚙️ Tech Stack

* Python 3.11
* Django 5.x
* Django REST Framework
* OpenRouteService API
* Geopy
* Python Dotenv

---

## 🏗️ Project Structure

```id="yaj6tw"
fuel_optimizer/
│
├── api/
│   ├── services/
│   │   ├── route_service.py      # Route API integration
│   │   ├── fuel_service.py       # Fuel optimization logic
│   │
│   ├── fuel_data.json            # Fuel price dataset
│   ├── fuel_data.py              # JSON loader
│   ├── views.py                  # API endpoint
│   ├── urls.py
│
├── fuel_optimizer/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── .env
├── requirements.txt
├── README.md
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```id="93hvwn"
ORS_API_KEY=your_api_key_here
```

---

## 📡 API Endpoint

### POST `/api/route/`

---

## 📥 Request Body (JSON)

### 🔹 Format

```json id="s01zpm"
{
  "start": {
    "lat": <latitude>,
    "lng": <longitude>
  },
  "end": {
    "lat": <latitude>,
    "lng": <longitude>
  }
}
```

---

### 🔹 Example

```json id="yo0kt6"
{
  "start": {"lat": 40.7128, "lng": -74.0060},
  "end": {"lat": 34.0522, "lng": -118.2437}
}
```

---

### 🔹 Field Explanation

* **start** → Starting location
* **end** → Destination location
* **lat** → Latitude (-90 to 90)
* **lng** → Longitude (-180 to 180)

---

## ⚠️ Important Notes

* Use **POST method**
* Content-Type must be **application/json**
* Do NOT manually provide distance
* Distance is calculated internally using routing API

---

## ❗ Common Errors & Solutions

### 1️⃣ Method Not Allowed (405)

```id="g9b7pw"
"detail": "Method GET not allowed"
```

👉 Cause:

* API accessed via browser (GET request)

👉 Fix:

* Use POST in Postman

---

### 2️⃣ Invalid Coordinates

```id="sckn7k"
Could not find routable point
```

👉 Cause:

* Incorrect latitude/longitude values

❌ Wrong:

```id="o6l9xr"
20.7128
```

✔ Correct:

```id="iv8c1k"
40.7128
```

---

### 3️⃣ API Key Error

```id="chj3lr"
API Error: ...
```

👉 Cause:

* Missing or invalid API key

👉 Fix:

* Check `.env`
* Restart server

---

### 4️⃣ Missing Input

```id="y3g73t"
"error": "Start and End required"
```

---

## 📤 Response Example

```json id="eprkq7"
{
  "distance_miles": 2794.13,
  "fuel_stops": [
    {
      "distance": 500,
      "station": {
        "city": "Texas",
        "price": 3.0
      }
    }
  ],
  "total_cost": 775.0,
  "route": "encoded_polyline"
}
```

---

## 🧠 Core Logic

### 1️⃣ Route Calculation

* Uses OpenRouteService API
* Returns distance and route geometry

---

### 2️⃣ Fuel Optimization

* Vehicle range = 500 miles
* Stops generated dynamically
* Selects nearest + cheapest fuel station

---

### 3️⃣ Cost Calculation

* Mileage = 10 mpg
* Fuel per stop = 50 gallons
* Total cost calculated across stops

---

## ⚡ Performance Optimization

* Caching implemented using Django cache
* Reduces repeated API calls

---

## 🧪 Testing

Use Postman:

* Method: POST
* URL: http://127.0.0.1:8000/api/route/
* Body: JSON

---

## ✔ How to Verify It Works

* Distance ≈ 2700–3000 miles
* Multiple fuel stops generated
* Total cost > 0
* Route polyline present

---

## 🚀 How to Run

```id="y2t1r7"
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🔒 Security

* API keys stored in `.env`
* Never exposed in code

---

## 💡 Future Improvements

* Real-time fuel price API
* Map visualization
* Dynamic fuel refill strategy

---

## 🎯 Key Highlights

* Real-world backend system
* External API integration
* Optimization logic
* Clean architecture

---

## 🧑‍💻 Author

Shiva Kumar

---

## 📌 Summary

This project demonstrates:

* API development
* Problem solving
* Optimization logic
* Production-level backend design

---

## ⭐ Final Note

This project goes beyond basic CRUD operations and demonstrates real-world backend engineering with optimization and external API integration.
