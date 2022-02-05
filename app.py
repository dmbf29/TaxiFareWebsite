import streamlit as st
import pandas as pd
import datetime
import requests

CSS = """
div.stButton > button:last-child {
    border-color: rgb(255, 75, 75) !important;
    color: rgb(255, 75, 75) !important;
    width: 100%;
}
div.stButton > button:last-child:hover {
    background-color: rgb(255, 75, 75) !important;
    color: rgba(255, 255, 255, 0.8) !important;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


'''
# NYC Taxi Fare Calculation
'''

columns = st.columns(3)
date = columns[0].date_input(
    "Date",
    datetime.date(2019, 7, 6))
time = columns[1].time_input('Time', datetime.time(9, 00))
count = columns[2].number_input('Passenger Count', 1)

columns = st.columns(4)

pickup_long = columns[0].number_input('Pickup Longitude', -73.950655)
pickup_lat = columns[1].number_input('Pickup Latitude', 40.783282)
dropoff_long = columns[2].number_input('Dropoff Longitude', -73.984365)
dropoff_lat = columns[3].number_input('Dropoff Latitude', 40.769802)


if st.button('Get fare'):
    url = f"https://taxi-api-qqi4hufipq-ew.a.run.app/predict?pickup_datetime={date} {time}&pickup_longitude={pickup_long}&pickup_latitude={pickup_lat}&dropoff_longitude={dropoff_long}&dropoff_latitude={dropoff_lat}&passenger_count={count}"
    response = requests.get(url).json()
    st.markdown(f"""
        ### Fare: ${round(response['fare'], 2)}
    """)
    df = pd.DataFrame([[pickup_lat, pickup_long], [dropoff_lat, dropoff_long]], columns=['lat', 'lon'])
    st.map(df)


# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
