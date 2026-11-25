import streamlit as st
import requests

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

"""
Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin.
We need to know all the inputs required by our model to make a prediction.
"""

# 1. Let's ask for:
# - island (the location where the penguin lives: Biscoe, Dream or Torgersen)
# - bill length (in mm)
# - bill depth (in mm)
# - flipper length (in mm)
# - body mass (in g)
# - sex ("Male" or "Female")
# """

location = st.text_input('Location')
bill_length = st.number_input('Bill length (in mm)')
bill_depth = st.number_input('Bill depth (in mm)')
flipper_length = st.number_input('Flipper length (in mm)')
body_mass = st.number_input('Body mass (in g)')
sex = st.text_input('Sex ("Male" or "Female")')

params = dict(island=location,
        bill_length_mm=bill_length,
        bill_depth_mm=bill_depth,
        flipper_length_mm=flipper_length,
        body_mass_g=body_mass,
        sex=sex
        )

request = requests.get(
    st.secrets["API_URL"],
    params)

result = request.json()
species = result.get("prediction")

st.markdown(f"Your penguin is from the specie {species}!")
