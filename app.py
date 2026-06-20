from fastapi import FastAPI
import joblib
from pydantic import BaseModel

class Recommendation(BaseModel):
    title: str

app = FastAPI()

data = joblib.load("model.pkl")
similarity = joblib.load("similarity.pkl")

@app.get("/")
def home():
    return { "message": "Movie recommender running." }

@app.post("/recommend")
def get_recommendations(request: Recommendation):

    title = request.title

    if title not in data["title"].values:
        return []

    index = data[data["title"] == title].index[0]

    scores = list(enumerate(similarity[index]))

    sorted_scores = sorted(scores, key = lambda x: x[1], reverse = True)

    recommendations = []
    for i in sorted_scores:
        movie_index = i[0]
        movie_title = data.iloc[movie_index]["title"]

        if movie_title.lower() == title.lower():
            continue

        recommendations.append(movie_title)

        if (len(recommendations) == 5):
            break 

    return {
        "movie": request.title,
        "recommendations": recommendations
    }
