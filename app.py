import streamlit as st
import pickle
import requests

encoders = pickle.load(open("encoder.sav", "rb"))
url="http://localhost:8000/predict"

st.set_page_config(page_title="Flight Price Prediction", page_icon="✈️", layout="centered")

BACKGROUND_IMAGE_URL = "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1920&q=80"

st.markdown(f"""
<style>
    /* Apply background image to the main app container */
    [data-testid="stAppViewContainer"] {{
        background-image: url("{BACKGROUND_IMAGE_URL}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Add a semi-transparent background to the content area for readability */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }}

    /* Ensure compatibility with Streamlit's dark mode */
    @media (prefers-color-scheme: dark) {{
        .block-container {{
            background-color: rgba(14, 17, 23, 0.85);
        }}
    }}
</style>
""", unsafe_allow_html=True)

st.title("✈️ Flight Price Prediction")
st.write("Enter the flight details below to predict the ticket price.")
st.divider()

airlines = list(encoders["airline"].classes_)
flights = list(encoders["flight"].classes_)
source_city = list(encoders["source_city"].classes_)
departure_time = list(encoders["departure_time"].classes_)
stops = list(encoders["stops"].classes_)
arrival_time = list(encoders["arrival_time"].classes_)
destination_city = list(encoders["destination_city"].classes_)
travel_class = list(encoders["class"].classes_)

def reset_form():
    st.session_state["source"] = source_city[0]
    st.session_state["departure"] = departure_time[0]
    st.session_state["destination"] = destination_city[0]
    st.session_state["arrival"] = arrival_time[0]
    st.session_state["airline"] = airlines[0]
    st.session_state["flight"] = flights[0]
    st.session_state["stop"] = stops[0]
    st.session_state["travel"] = travel_class[0]
    st.session_state["duration"] = 2.5
    st.session_state["days_left"] = 15

if "source" not in st.session_state:
    reset_form()

st.subheader("Route Details")
col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("Source City", source_city, key="source")
    departure = st.selectbox("Departure Time", departure_time, key="departure")
with col2:
    destination = st.selectbox("Destination City", destination_city, key="destination")
    arrival = st.selectbox("Arrival Time", arrival_time, key="arrival")

st.subheader("Flight Information")
col3, col4, col5 = st.columns(3)
with col3:
    airline = st.selectbox("Airline", airlines, key="airline")
with col4:
    flight = st.selectbox("Flight Code", flights, key="flight")
with col5:
    stop = st.selectbox("Stops", stops, key="stop")

st.subheader("Ticket & Duration")
col6, col7, col8 = st.columns(3)
with col6:
    travel = st.selectbox("Travel Class", travel_class, key="travel")
with col7:
    duration = st.number_input("Duration (Hours)", min_value=0.5, max_value=50.0, step=0.25, key="duration")
with col8:
    days_left = st.number_input("Days Before Journey", min_value=1, max_value=365, key="days_left")

st.write("")

if st.button("Predict Flight Price", use_container_width=True):
    if source == destination:
        st.warning("⚠️ Source and Destination cities cannot be the same. Please change your route.")
    else:
        input_data = {
            "airline": airline,
            "flight": flight,
            "source": source,
            "departure": departure,
            "stop": stop,
            "arrival": arrival,
            "destination": destination,
            "travel": travel,
            "duration": duration,
            "days_left": days_left
        }
        response = requests.post(url,json=input_data)
        if response.status_code ==200:
            prediction=response.json()
            st.success(f"### Estimated Flight Price: ₹ {prediction["predicted_price"]}")
        else:
            st.error(f"prediction failed{response.status_code} - {response.text}")
        

        st.button("Reset Form / Clear Inputs", on_click=reset_form)