import streamlit as st
import joblib

# Load model
model = joblib.load("california_clean.joblib")

# Page settings
st.set_page_config(
    page_title="California Housing Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 California Housing Price Prediction App")
st.markdown("Enter housing details below to estimate the **median house value**.")

# Sidebar
st.sidebar.header("About")
st.sidebar.write(
"""
This app predicts **California housing prices** using a machine learning model.

Model Input Features:
- Median Income
- House Age
- Average Rooms
- Population
- Average Occupancy
- Latitude
"""
)

st.sidebar.info("Streamlit ML App")

# Input section
st.subheader("Enter Housing Features")

col1, col2, col3 = st.columns(3)

with col1:
    MedInc = st.number_input("Median Income", min_value=0.0, value=5.0)

with col2:
    HouseAge = st.number_input("House Age", min_value=0, value=20)

with col3:
    AveRooms = st.number_input("Average Rooms", min_value=0.0, value=5.0)

col4, col5, col6 = st.columns(3)

with col4:
    Population = st.number_input("Population", min_value=0, value=800)

with col5:
    AveOccup = st.number_input("Average Occupancy", min_value=0.0, value=3.0)

with col6:
    Latitude = st.number_input("Latitude", value=34.05)

st.markdown("---")

# Predict button
if st.button("Predict House Price", use_container_width=True):

    with st.spinner("Predicting..."):

        try:
            # Prepare input for model
            input_data = [[
                MedInc,
                HouseAge,
                AveRooms,
                Population,
                AveOccup,
                Latitude
            ]]

            # Make prediction
            prediction = model.predict(input_data)[0]

            st.success("Prediction Completed!")

            st.metric(
                label="Predicted House Price ($)",
                value=f"${prediction:,.2f}"
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")