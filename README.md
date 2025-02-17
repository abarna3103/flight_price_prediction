# Flight Price & Customer Satisfaction Prediction

# https://flightpricepredictionandcustomerstatisfaction.streamlit.app/

## 🚀 Overview
This project predicts **flight ticket prices** and **customer satisfaction levels** using **machine learning models**. It features an interactive **Streamlit web app** where users can input flight and customer details to get predictions.

## ✨ Features
- **Flight Price Prediction** 📊
  - Predicts ticket prices based on airline, route, duration, and stops.
  - Uses regression models to provide accurate estimates.
  
- **Customer Satisfaction Prediction** 😊
  - Predicts whether a passenger will be satisfied based on service ratings, travel details, and delays.
  - Uses classification models to determine satisfaction levels.

- **User-Friendly Streamlit App** 🖥️
  - Interactive UI with dropdowns, sliders, and date-time pickers.
  - Real-time price and satisfaction predictions.

## 📂 Project Structure
├── price_pred.csv                 # Cleaned dataset for flight price prediction
├── satisfication_pred.csv          # Cleaned dataset for customer satisfaction prediction
├── data_cleaning_and_processing.ipynb  # Data preprocessing notebook      
├── price_pred_app.py                    # Streamlit web application script
├── requirements.txt                     # Required dependencies
├── README.md                            # Project documentation
└── .gitignore                            # Git ignore file
```

## 📊 Machine Learning Models Used
### **Flight Price Prediction**
- **Regression Models**:
  - Linear Regression
  - K-Nearest Neighbors
  - Decision Tree
  - Random Forest
  - AdaBoost
  - Gradient Boosting

### **Customer Satisfaction Prediction**
- **Classification Models**:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - XGBoost

## 🛠️ Setup & Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/abarna3103/flight_price_prediction.git
cd flight_price_prediction
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```sh
streamlit run price_pred_app.py
```

## 🎯 Usage
- Select the **Flight Price Prediction** tab to enter airline, route, and time details.
- Select the **Customer Satisfaction Prediction** tab to enter passenger details.
- Click **Predict** to get real-time results.

## 🚀 Deployment
This app is already deployed on streamlit cloud.


---
✨ **Developed with ❤️ by [Abarna venkat]** ✨

