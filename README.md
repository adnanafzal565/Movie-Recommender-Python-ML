# Movie Recommender (Python ML Project)

## Overview

This project is a simple Machine Learning-based Movie Recommendation system built using Python and Scikit-learn.  
You give it a name of movie and it will return recommended movies of that type.

## How to Run

```bash
pip3 install -r requirements.txt
python3 train.py
uvicorn app:app --reload
```

## Test 1

```bash
curl -X POST http://127.0.0.1:8000/recommend -H "Content-Type: application/json" -d '{"title": "Inception"}'
```

### Output

```bash
{"movie":"Inception","recommendations":["Sky Captain and the World of Tomorrow","Paycheck","Oblivion","Minority Report","The Maze Runner"]}
```

## Test 2

```bash
curl -X POST http://127.0.0.1:8000/recommend -H "Content-Type: application/json" -d '{"title": "The Matrix"}'
```

### Output

```bash
{"movie":"The Matrix","recommendations":["Edge of Tomorrow","The Chronicles of Riddick","RoboCop","I, Robot","Dredd"]}
```
