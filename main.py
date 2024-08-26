import streamlit as st

st.title("Welcome to the Band Name Generator")

city_name = st.text_input("What's the name of the city you grew up in?")
pet_name = st.text_input("What's your pet's name?")
band_name = city_name + " " + pet_name


st.write("Your band name could be " + band_name)