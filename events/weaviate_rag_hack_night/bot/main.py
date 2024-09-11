import requests
import re
import writer as wf
import writer.ai
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()

# # Welcome to Writer Framework! 
# # This template is a starting point for your AI apps.
# # More documentation is available at https://dev.writer.com/framework

# Initialize the state
wf.init_state({
    "my_app": {
        "title": "Movie Review Bot"
    },
    "posts": "",
    "topic": "movie reviews",
    "message": "",
    "movie_name": "Watchmen",
    "image": ""
})

def preprocess_movie_name(movie_name):
    return movie_name.lower().replace(" ", "_")



def fetch_movie_reviews(movie_name):
    movie_name = preprocess_movie_name(movie_name)
   
    api_key = os.getenv('API_KEY');
    url = f"https://api.diffbot.com/v3/article?url=https://www.rottentomatoes.com/m/{movie_name}&token={api_key}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {f"Diffbot failed this time... Error {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def fetch_movie_reviews(movie_name):
    movie_name = preprocess_movie_name(movie_name)
   
    api_key = "35d01f97a261a67102c0e74e51111487"  
    url = f"https://api.diffbot.com/v3/article?url=https://www.rottentomatoes.com/m/{movie_name}&token={api_key}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {f"Diffbot failed this time... Error {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def split_reviews(review_text):
    review_pattern = r'([A-Za-z\s.]+)\s([A-Za-z\s.]+)\s(.*?)(?:\sRated: ([A-Za-z0-9+/.]+))?\s•\s([A-Za-z\s0-9,]+)\sFull Review'
    matches = re.findall(review_pattern, review_text)
    reviews_list = []
    
    for match in matches:
        reviewer_and_source = f"{match[0].strip()} ({match[1].strip()})"
        content = f"{reviewer_and_source}: {match[2].strip()}"
        rating = match[3].strip() if match[3] else "No rating"
        date = match[4].strip()
        
        reviews_list.append({
            'content': content,
            'rating': rating,
            'date': date
        })
    return reviews_list


def handle_button_click(state):
    state["message"] = f"Diffbot is scraping {state['movie_name']} on rotten tomatoes"
    

    movie_reviews = fetch_movie_reviews(state["movie_name"])
    
    if "error" in movie_reviews:
        state["posts"] = f"Error: {movie_reviews['error']}"
    else:
        title = movie_reviews.get("objects", [{}])[0].get("title", "Unknown Movie")
        reviews = movie_reviews.get("objects", [{}])[0].get("text", "No reviews available.")
        image_url = movie_reviews.get("objects", [{}])[0].get("images", [{}])[0].get("url", "")

        split_review_data = split_reviews(reviews)
        
        formatted_reviews = ""
        for review in split_review_data:
            formatted_reviews += f"Date: {review['date']}\n"
            formatted_reviews += f"Rating: {review['rating']}\n"
            formatted_reviews += f"Review: {review['content']}\n"
            formatted_reviews += "-" * 50 + "\n"
        
        state["posts"] = f"{formatted_reviews}"
        state["image"] = image_url

    state["message"] = ""

def on_user_search_movie(state, movie_name):
    state["movie_name"] = movie_name
    handle_button_click(state)