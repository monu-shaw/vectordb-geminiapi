import streamlit as st
import pymongo
import google.generativeai as genai  # Assuming google.generativeai is for Gemini API

try:
  genai.configure(api_key=st.secrets["GEMINIKEY"])
except Exception as e:
  st.error(f"Error configuring Gemini API: {e}")
  exit()

def gen_emb(text: str) -> list[float]:
  try:
    result = genai.embed_content(model="models/embedding-001", content=text)
    return result['embedding']
  except Exception as e:
    st.error(f"Error generating embedding: {e}")
    return None

client = pymongo.MongoClient(st.secrets["MONGODB"])
db = client.sample_mflix
collection = db.movies

st.title("Movie Search (MongoDB Vector Search with Gemeni API)")

def display_movies(movies):
  """Displays movie cards with title, image, and plot summary."""
  cols = st.columns(len(movies))  # Create columns for each movie
  for i, movie in enumerate(movies):
    with cols[i]:
      st.header(movie["title"])
      st.image(movie.get("poster", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTw_HeSzHfBorKS4muw4IIeVvvRgnhyO8Gn8w&usqp=CAU"), use_column_width=True)  # Stretch image across column
      st.write(movie["plot"])
      
search_term = st.text_input("Enter your search query:")

if search_term:
  try:
    query = search_term
    results = collection.aggregate([
      {"$vectorSearch": {
        "queryVector": gen_emb(query),
        "path": "plot_embedding_hf",
        "numCandidates": 100,
        "limit": 4,
        "index": "plotSemmanticSearch",
      }}
    ])
    movies = list(results)
    display_movies(movies)
  except Exception as e:
    st.error(f"An error occurred: {e}")


