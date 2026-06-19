import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("movies.csv")
data["features"] = data["genres"]
data["features"] = data["features"].fillna("")

vectorizer = TfidfVectorizer(
    stop_words = "english"
)

feature_matrix = vectorizer.fit_transform(data["features"])

similarity = cosine_similarity(feature_matrix)

joblib.dump(data, "model.pkl")
joblib.dump(similarity, "similarity.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved.")
