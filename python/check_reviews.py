from imdb import IMDb

ia = IMDb()
movie_id = '0133093'  # Example: The Matrix IMDb ID
movie_reviews = ia.get_movie_reviews(movie_id)

if movie_reviews and 'reviews' in movie_reviews:
    for review in movie_reviews['reviews'][:3]: # Print first 3 reviews
        print(f"Author: {review['author']}")
        print(f"Title: {review['title']}")
        print(f"Content: {review['content'][:150]}...") # Truncate content
        print("-" * 20)
# This script fetches and prints reviews for a specific movie using the IMDbPY library.

