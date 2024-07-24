import os
import streamlit as st
import requests
from dotenv import load_dotenv

def get_recipes():
    try:
        res = requests.get(
          f"https://api.spoonacular.com/recipes/complexSearch?apiKey={apiKey}&query={query}"
        )
        data = res.json()

        for item in data["results"]:
            st.write(item["title"])

    except:
        st.write("Something went wrong")



load_dotenv()
apiKey = os.getenv('API_KEY')

st.write("Search Recipes")
query = st.text_input("Query")

if st.button("Search"):
    get_recipes()
