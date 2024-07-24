"""
This module runs a Streamlit app for displaying recipes.
"""
import streamlit as st
import requests
from dotenv import load_dotenv

def get_recipes():
    """
    This module runs a Streamlit app for displaying recipes.
    """

    try:
        res = requests.get(
          f"https://api.spoonacular.com/recipes/complexSearch?apiKey={apiKey}&query={query}",
          timeout=5000
        )
        data = res.json()

        for item in data["results"]:
            st.write(item["title"])

    except Exception as e:
        st.write(f"Something went wrong: {e}")



load_dotenv()
API_KEY = "a508d888595c4a4fa2cb44a0fed80c69"

st.write("Search Recipes")
query = st.text_input("Query")

if st.button("Search"):
    get_recipes()
