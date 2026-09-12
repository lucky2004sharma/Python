movies = []

while True:
    movie = input("Add movie (or 'stop'): ")

    if movie == "stop":
        break

    movies.append(movie)

print("\nYour Watchlist:")

for movie in movies:
    print(movie)