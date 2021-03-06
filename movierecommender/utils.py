from fuzzywuzzy import process
import pandas as pd
import os
import pickle


package_dir = os.path.dirname(__file__)
# put the movieId into the row index!
movies_path = package_dir + '/data/ml-latest-small/movies.csv'
movies = pd.read_csv(movies_path, index_col=0)
# put the movieId into the row index!
# movies = pd.read_csv('./data/ml-latest-small/movies.csv')
ratings_path = package_dir + '/data/ml-latest-small/ratings.csv'
ratings = pd.read_csv(ratings_path)
#ratings = pd.read_csv('./data/ml-latest-small/ratings.csv')
model_path = package_dir + '/data/movie_model.pickle'

movie_average_rating = None
movie_item_matrix = None

with open(model_path, 'rb') as file:
    model = pickle.load(file)



def lookup_movie(search_query, titles):
    """
    given a search query, uses fuzzy string matching to search for similar 
    strings in a pandas series of movie titles

    returns a list of search results. Each result is a tuple that contains 
    the title, the matching score and the movieId.
    """
    matches = process.extractBests(search_query, titles)
    # [(title, score, movieId), ...]
    return matches

if __name__ == '__main__':
    results = lookup_movie('star wars', movies['title'])
    print(results)

