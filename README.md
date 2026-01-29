# 🍽️ MealBridge

**Collecting leftovers, connecting lives.**

MealBridge is a social-impact web application designed to reduce food wastage by connecting food donors (hotels, events, functions) with receivers (NGOs, volunteers, needy communities) in real time.

---

## 🌍 Problem Statement

Every day, large quantities of perfectly edible food are wasted after events, hotels, and functions, while many people struggle to access basic meals. There is no simple, real-time platform that connects food donors with nearby receivers efficiently.

---

## 💡 Our Solution

MealBridge acts as a digital bridge between food donors and receivers:

* Donors can quickly list leftover food with essential details.
* Receivers can view available food in real time and accept it before expiry.
* Food listings automatically expire and are removed, ensuring safety and accuracy.

---

## ✨ Key Features

* 🧑‍🍳 **Donor Portal**: Add food details (hotel/event name, quantity, food type, location, expiry time, contact).
* 🤝 **Receiver Portal**: View available food, check time left, accept food.
* ⏳ **Expiry-Based Auto Removal**: Food listings disappear automatically after expiry.
* 📍 **Google Maps Location Links**: Easy navigation to food pickup location.
* 🔄 **Real-Time Status Update**: Available → Accepted.

---

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python (Flask)
* **Database**: SQLite
* **Version Control**: Git & GitHub

---

## 🏗️ Project Architecture

1. Frontend collects user input and displays data.
2. Flask backend handles routing, business logic, and database operations.
3. SQLite stores food donation details.
4. JavaScript manages timers, UI updates, and auto-refresh.

---

## 🚀 How to Run the Project Locally

### Prerequisites

* Python 3.x
* pip

### Steps

```bash
# Install dependencies
pip install flask

# Run the application
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
mealbridge/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── donor.html
│   └── receiver.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── food.jpg
```

---

## 🌱 Impact

* Reduces food wastage
* Supports NGOs and underprivileged communities
* Encourages responsible food sharing
* Scalable for cities and institutions

---

## 🔮 Future Enhancements

* Live Google Maps tracking
* SMS / WhatsApp notifications
* Volunteer and NGO onboarding
* Mobile application
* Cloud deployment

---

## 👩‍💻 Hackathon Readiness

* Working end-to-end prototype
* Clean GitHub repository
* Easy-to-understand UI
* Real-world social impact

---

## 📜 License

This project is created for educational and hackathon purposes.

---

**MealBridge – Because no good food should go to waste.** ❤️
