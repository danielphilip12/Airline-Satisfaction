import streamlit as st
import pandas as pd
import plotly.express as px

import joblib

st.set_page_config(page_title="Airline Satisfaction Explorer", page_icon="🛩️")

page = st.sidebar.selectbox(
    "Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis", "Make Predictions"]
)

df = pd.read_csv("./data/cleaned_airline.csv")

if page == "Home":
    st.title("Airline Dataset Explorer")

elif page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis (EDA)")

    st.subheader("Select the type of visualization you'd like to explore:")
    eda_type = st.multiselect(
        "Visualization Options",
        ["Histograms", "Box Plots", "Scatterplots", "Count Plots"],
    )

    obj_cols = df.select_dtypes(include="object").columns.tolist()
    num_cols = df.select_dtypes(include="number").columns.tolist()

    if "Histograms" in eda_type:
        h_selected_col = st.selectbox(
            "Select a numerical column for the histogram", num_cols
        )
        group_by_col = st.selectbox("Group by", obj_cols, index=None)
        if h_selected_col and group_by_col:
            st.plotly_chart(
                px.histogram(
                    df, x=h_selected_col, color=group_by_col, barmode="overlay"
                )
            )
        elif h_selected_col:
            st.plotly_chart(px.histogram(df, x=h_selected_col))

    if "Box Plots" in eda_type:
        b_selected_col = st.selectbox(
            "Select a numerical column for the histogram", num_cols
        )
        group_by_col = st.selectbox("Group by", obj_cols, index=None)
        if b_selected_col and group_by_col:
            st.plotly_chart(
                px.box(
                    df, x=b_selected_col, color=group_by_col
                )
            )
        elif b_selected_col:
            st.plotly_chart(px.box(df, x=b_selected_col))
            
elif page == "Make Predictions":
    st.title("Make Predictions")
    
    st.subheader("Adjust the values below to make predictions on the Airline Satisfaction Dataset")
    
    rf_model = joblib.load('./models/rf.pkl')
    
     # --- CATEGORICAL ---
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    customer_type = st.selectbox(
        "Customer Type",
        ["Loyal Customer", "disloyal Customer"]
    )

    type_of_travel = st.selectbox(
        "Type of Travel",
        ["Business travel", "Personal Travel"]
    )
    
    class_map = {
    "Economy": 0,
    "Economy Plus": 1,
    "Business": 2
}

    class_label = st.selectbox(
        "Travel Class",
        options=list(class_map.keys())
    )

    class_codes = class_map[class_label]

    # --- NUMERIC ---
    age = st.number_input("Age", min_value=0, max_value=120, value=30)

    flight_distance = st.number_input(
        "Flight Distance (miles)",
        min_value=0,
        value=500
    )

    departure_delay = st.number_input(
        "Departure Delay (minutes)",
        min_value=0,
        value=0
    )

    arrival_delay = st.number_input(
        "Arrival Delay (minutes)",
        min_value=0,
        value=0
    )

    # --- SERVICE RATINGS (1–5) ---
    inflight_wifi_service = st.slider("Inflight WiFi Service", 1, 5, 3)
    departure_arrival_time_convenient = st.slider("Departure/Arrival Time Convenient", 1, 5, 3)
    ease_of_online_booking = st.slider("Ease of Online Booking", 1, 5, 3)
    gate_location = st.slider("Gate Location", 1, 5, 3)
    food_and_drink = st.slider("Food and Drink", 1, 5, 3)
    online_boarding = st.slider("Online Boarding", 1, 5, 3)
    seat_comfort = st.slider("Seat Comfort", 1, 5, 3)
    inflight_entertainment = st.slider("Inflight Entertainment", 1, 5, 3)
    on_board_service = st.slider("On-board Service", 1, 5, 3)
    leg_room_service = st.slider("Leg Room Service", 1, 5, 3)
    baggage_handling = st.slider("Baggage Handling", 1, 5, 3)
    checkin_service = st.slider("Check-in Service", 1, 5, 3)
    inflight_service = st.slider("Inflight Service", 1, 5, 3)
    cleanliness = st.slider("Cleanliness", 1, 5, 3)
        
    input_data = pd.DataFrame([{
        "gender": gender,
        "customer_type": customer_type,
        "age": age,
        "type_of_travel": type_of_travel,
        "flight_distance": flight_distance,
        "inflight_wifi_service": inflight_wifi_service,
        "departure_arrival_time_convenient": departure_arrival_time_convenient,
        "ease_of_online_booking": ease_of_online_booking,
        "gate_location": gate_location,
        "food_and_drink": food_and_drink,
        "online_boarding": online_boarding,
        "seat_comfort": seat_comfort,
        "inflight_entertainment": inflight_entertainment,
        "on_board_service": on_board_service,
        "leg_room_service": leg_room_service,
        "baggage_handling": baggage_handling,
        "checkin_service": checkin_service,
        "inflight_service": inflight_service,
        "cleanliness": cleanliness,
        "departure_delay_in_minutes": departure_delay,
        "arrival_delay_in_minutes": arrival_delay,
        "class_codes": class_codes,
        "arrival_delayed_missing": 0
    }])
    
    st.write("### Your Input Values")
    st.dataframe(input_data)
    
    prediction = rf_model.predict(input_data)[0]
    
    st.write(f"The model predicts that the satisfaction of the passenger is: **{prediction}**")