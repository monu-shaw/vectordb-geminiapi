
# Movie Search with Gemini API, MongoDB Vector Search, and Streamlit UI

**Description:**

This project implements a movie search application that leverages the power of:

- **Google Gemini API:** For efficient vector embedding generation, capturing the semantic meaning of movie plots.
- **MongoDB Vector Search:** To retrieve movies with plots semantically similar to a user's search query.
- **Streamlit:** For creating a user-friendly and interactive web application.

**Features:**

- Users can enter a search query for movies.
- The application uses the Gemini API to generate a vector representation of the query.
- It then performs a vector search within MongoDB to find movies with similar plot embeddings.
- The user interface displays details of the retrieved movies, including title, plot summary (if available), and optionally, posters (if URLs are present in the data).

**Requirements:**

- Python 3.x
- Required libraries:
    - `google-generativeai` (for Gemini API)
    - `pymongo` (for MongoDB interaction)
    - `streamlit` (for web app development)

**Installation:**

1. Clone this repository.
2. Create a virtual environment (recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate.bat
   ```
3. Install the required libraries:
   ```bash
   pip install google-generativeai pymongo streamlit
   ```

**Setup:**

1. **Configure Gemini API:**
   - Obtain a Google Cloud project and enable the Gemini API.
   - Create an API key and set the environment variable `GOOGLE_API_KEY` accordingly.
2. **Connect to MongoDB:**
   - Set up a MongoDB database with a collection containing movie data. The collection should include documents with fields like `title`, `plot` (for vector search), and optionally `poster` (for image display).
   - Replace placeholders in `connection_string.py` with your MongoDB connection string and database/collection names.

**Usage:**

1. Run the application:
   ```bash
   streamlit run movie_recs.py
   ```
2. Enter a search query in the text input field and press "Enter".
3. The app will display a list of movies that semantically match your query, along with their details.
