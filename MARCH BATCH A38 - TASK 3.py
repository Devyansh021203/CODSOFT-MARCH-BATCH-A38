"""I have created a simple recommendation system that suggests movies to
users based on their preferences. I used the techniques like
collaborative filtering or content-based filtering to recommend movies to users.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Define some sample data: movie ratings by users
# Each row represents a user, and each column represents a movie
# The values represent the ratings (e.g., on a scale of 1 to 5)
ratings = np.array([
    [5, 4, 0, 0, 0],  # User 1
    [0, 0, 5, 4, 0],  # User 2
    [0, 0, 0, 0, 5],  # User 3
    [0, 0, 5, 0, 4],  # User 4
    [4, 5, 0, 0, 0],  # User 5
])

# Define the movies
movies = ['Jumanji', 'Salaar', 'Titanic', 'K.G.F', 'K.G.F Chapter2']

# Function to recommend movies to a user based on their preferences
def recommend_movies(user_preferences, movies, ratings):
    # Calculate the cosine similarity between the user preferences and movie ratings
    similarities = cosine_similarity([user_preferences], ratings).flatten()
    # Sort the movies based on similarity score
    recommended_movie_indices = similarities.argsort()[::-1]
    # Exclude movies that the user has already rated
    recommended_movies = [(movies[i], similarities[i]) for i in recommended_movie_indices if user_preferences[i] == 0]
    return recommended_movies

# Example: Recommend movies to User 1 based on their preferences
user_preferences = np.array([0, 0, 5, 0, 4])  # User 1's ratings
recommended_movies = recommend_movies(user_preferences, movies, ratings)
print("Recommended movies for User 4:")
for movie, similarity in recommended_movies:
    print(f"{movie} (Similarity: {similarity:.2f})")
