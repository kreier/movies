from imdbinfo import search_title, get_movie, get_name, get_season_episodes, get_reviews, get_trivia


# Get movie details
movie = get_movie("tt0133093")  # or 'tt0133093'
print(movie.title, movie.year, movie.rating)

# Get movie kind:
print(movie.kind)  # movie, tvSeries, tvMiniSeries, tvMovie, tvEpisode, tvSpecial, tvShort, short, videoGame, video, musicVideo, podcastEpisode, podcastSeries
print(movie.is_series())  # False

# Get person details
person = get_name("nm0000206")  # or '0000206' 
print(person.name, person.birth_date)
