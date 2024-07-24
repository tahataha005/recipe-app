import streamlit as st
import requests
import os
from dotenv import load_dotenv

def fetchRecipes():
  res = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?apiKey={apiKey}&query={query}", )
  data = res.json()

  for item in data["results"]:
    st.write(item["title"])


load_dotenv()
apiKey = os.getenv('API_KEY')

st.write("Search Recipes")
query = st.text_input("Query")

if st.button("Search"):
  fetchRecipes()
