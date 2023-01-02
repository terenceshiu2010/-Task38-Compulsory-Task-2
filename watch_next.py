import spacy

en_core_web_md = "C:/Users/User/AppData/Local/Programs/Python/Python311/Lib/" \
                 "site-packages/en_core_web_md/en_core_web_md-3.4.1"

planet_Hulk_description = " Will he save their world or destroy it? When the Hulk becomes too dangerous " \
                          "for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space " \
                          "to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet " \
                          "Sakaar where he is sold into slavery and trained as a gladiator."

nlp = spacy.load(en_core_web_md)


def next_movie(desc):
    similarity_score = []

    # Open movie.txt and read the file content
    with open("movies.txt", "r") as f:
        contents = f.readlines()

    # Tokenize the description of the watched movie
    watched_moive = nlp(desc)

    # Each line in the movie.txt file represent a move and its description
    for movie in contents:
        movie_name = movie.strip("\n").split(" :")[0]
        movie_description = movie.strip("\n").split(" :")[1]
        # Test similarity for each movie's description and the watched moive's description
        similarity = nlp(movie_description).similarity(watched_moive)
        # Add each similarity result and moive name into similarity_score list
        similarity_score.append([similarity, movie_name, movie_description])

    # Return the movie name with the highest similarity
    return max(similarity_score)[1]


print(f"User would watch '{next_movie(planet_Hulk_description)}' next")
