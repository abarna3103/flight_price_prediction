import streamlit as st
import pandas as pd
import numpy as np
import datetime

def load_data():
    try:
        price_df = pd.read_csv("price_pred.csv")
        satisfaction_df = pd.read_csv("satisfication_pred.csv")
        return price_df, satisfaction_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

def main():
    st.set_page_config(page_title="Flight & Customer Satisfaction Prediction", layout="wide")

    # Custom CSS for Styling
    st.markdown(
        """
        <style>
            .big-title { font-size: 32px; font-weight: bold; color: #ff4b4b; }
            .sub-title { font-size: 18px; color: #4b4b4b; }
            .stButton>button { background-color: #ff4b4b; color: white; border-radius: 10px; }
            .stTextInput>div>div>input, .stSelectbox>div>div>select { border: 2px solid #ff4b4b; }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<p class="big-title">✈️ Flight Price & 👤 Customer Satisfaction Prediction</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Predict flight prices and customer satisfaction trends using interactive inputs.</p>', unsafe_allow_html=True)
    
    price_df, satisfaction_df = load_data()
    if price_df is None or satisfaction_df is None:
        st.error("Error loading datasets.")
        return
    
    tab1, tab2 = st.tabs(["Flight Price Prediction", "Customer Satisfaction Prediction"])
    
    with tab1:
        st.header("✈️ Flight Price Prediction")
        col1, col2 = st.columns(2)
        
        with col1:
            airline_columns = [col.replace("Airline_", "") for col in price_df.columns if col.startswith("Airline_")]
            airline = st.selectbox("Select Airline", options=sorted(airline_columns))
            source_columns = [col.replace("Source_", "") for col in price_df.columns if col.startswith("Source_")]
            source = st.selectbox("Select Source", options=sorted(source_columns))
            destination_columns = [col.replace("Destination_", "") for col in price_df.columns if col.startswith("Destination_")]
            destination = st.selectbox("Select Destination", options=sorted(destination_columns))
            total_stops = st.selectbox("Number of Stops", options=sorted(price_df['Total_Stops'].unique()))
        
        with col2:
            date = st.date_input("Date of Journey", min_value=datetime.date(2019, 1, 1))
            dep_time = st.time_input("Departure Time")
            arr_time = st.time_input("Arrival Time")
            duration = (datetime.datetime.combine(datetime.date.today(), arr_time) -
                        datetime.datetime.combine(datetime.date.today(), dep_time)).seconds // 60
        
        if st.button("Predict Price"):
            try:
                base_price = 5000
                base_price += total_stops * 1000
                base_price += duration * 2
                price_prediction = base_price * (1 + (dep_time.hour - 12) * 0.02)
                st.success(f"Predicted Flight Price: ₹{price_prediction:,.2f}")
            except Exception as e:
                st.error(f"Error in prediction: {e}")
    
    with tab2:
        st.header("👤 Customer Satisfaction Prediction")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.number_input("Age", min_value=int(satisfaction_df['Age'].min()),
                                  max_value=int(satisfaction_df['Age'].max()), value=30)
            flight_distance = st.number_input("Flight Distance", 
                                             min_value=int(satisfaction_df['Flight Distance'].min()),
                                             max_value=int(satisfaction_df['Flight Distance'].max()), value=500)
            travel_type_columns = [col.replace("Type_of_Travel_", "") for col in satisfaction_df.columns if col.startswith("Type_of_Travel_")]
            travel_type = st.selectbox("Type of Travel", options=sorted(travel_type_columns))
        
        with col2:
            wifi_service = st.slider("Inflight Wifi Service", 0, 5, 3)
            online_booking = st.slider("Ease of Online Booking", 0, 5, 3)
            food_drink = st.slider("Food and Drink", 0, 5, 3)
            seat_comfort = st.slider("Seat Comfort", 0, 5, 3)
        
        with col3:
            entertainment = st.slider("Inflight Entertainment", 0, 5, 3)
            cleanliness = st.slider("Cleanliness", 0, 5, 3)
            departure_delay = st.number_input("Departure Delay (minutes)", min_value=0, value=0)
            arrival_delay = st.number_input("Arrival Delay (minutes)", min_value=0, value=0)
        
        if st.button("Predict Satisfaction"):
            try:
                service_score = (wifi_service + online_booking + food_drink + seat_comfort + 
                                entertainment + cleanliness) / 30
                delay_impact = (departure_delay + arrival_delay) / 1000
                final_satisfaction_score = service_score - delay_impact
                result = "Satisfied" if final_satisfaction_score > 0.6 else "Not Satisfied"
                st.success(f"Predicted Customer Satisfaction: {result}")
            except Exception as e:
                st.error(f"Error in prediction: {e}")

if __name__ == "__main__":
    main()
