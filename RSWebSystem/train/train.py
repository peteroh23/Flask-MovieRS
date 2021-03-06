from __future__ import (absolute_import, division, print_function,unicode_literals)
from surprise import Dataset
from surprise import AlgoBase
from surprise import SVD, SlopeOne, CoClustering, BaselineOnly, KNNBasic
from surprise import PredictionImpossible
from surprise import Reader
from surprise.model_selection import train_test_split, cross_validate, KFold
import numpy as np
import pandas as pd
from six import iteritems
import heapq
from random import *
from collections import defaultdict


# loading the movie-lens dataset

ratings_base = pd.read_csv('ml-latest-small/ratings.csv', sep=',', encoding='latin-1')


items = pd.read_csv('ml-latest-small/movies.csv', sep = ',', encoding = 'latin-1')

movie = items['title']

# top-N recommendation for specific user
def get_top_n(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


def movies():
    list1 = []
    while len(list1) < 20:
            newUserItem = randrange(1,9126)

            if newUserItem not in list1:
                list1.append(newUserItem)
    return list1


def recommend(movieList, userRatings):

    ratings_base = pd.read_csv('ml-latest-small/ratings.csv', sep=',', encoding='latin-1')


    items = pd.read_csv('ml-latest-small/movies.csv', sep = ',', encoding = 'latin-1')

    movie = items['title']

    for i in range(20):
        movieID = movieList[i]
        rating = float(userRatings[i])
        newRatingData = {'userId': [672], 'movieId': [movieID], 'rating': [rating], 'timestamp': [randrange(1260759131, 1280759131)]}
        newRating = pd.DataFrame(data = newRatingData)
        ratings_base = ratings_base.append(newRating)

    
    list1 = []
    while len(list1) < 20:
            newUserItem = randrange(1,9126)

            if newUserItem not in list1:
                list1.append(newUserItem)

    for i in range(10):
        movieID = list1[i]
        movieName = movie[movieID]
        newRatingData = {'userId': [672], 'movieId': [movieID], 'rating': [3.0], 'timestamp': [randrange(1260759131, 1280759131)]}
        newRating = pd.DataFrame(data = newRatingData)
        ratings_base = ratings_base.append(newRating)
    
        
    #converting pandas dataframe to Surprise data
    ratings_dict = {'itemId': list(ratings_base.movieId),
                    'userId': list(ratings_base.userId),
                    'rating': list(ratings_base.rating)}

    df = pd.DataFrame(ratings_dict)

    reader = Reader(rating_scale = (0.5,5.0))

    data = Dataset.load_from_df(df[['userId', 'itemId','rating']], reader)


    #training and testing dataset
    trainset, testset = train_test_split(data)


    ###################predictions using K-NN

    algo = KNNBasic()
    algo.fit(trainset)

    predictions = algo.test(testset)
    dictMovies = get_top_n(predictions)
    topMovies = dictMovies.get(672)

    list2 = []

    for i in range(5):

        movieRecc = topMovies[i]
        movieRawID = movieRecc[0]
        movieName = movie[movieRawID]
        list2.append(movieName)

    #return strings of top 5 movie titles
    return list2










"""


#################predictions using BaselineOnly
print('')
print('Making recommendations...')
print('')

algo4 = BaselineOnly()
algo4.fit(trainset)

predictions4 = algo4.test(testset)
dictMovies4 = get_top_n(predictions4)
topMovies4 = dictMovies4.get(672)
"""

"""
#model dumping
file_name = 'BaselineModelDump'
dump.dump(file_name, algo=algo4)

#to reload dump
_, loaded_algo = dump.load(file_name)
predictions_loaded_algo = loaded_algo.test(testset)
"""
"""
print('')
print('Here are the top 5 recommendations based on Baseline algorithm! ')

for i in range(5):

    movieRecc4 = topMovies4[i]
    movieRawID4 = movieRecc4[0]
    movieName4 = movie[movieRawID4]
    print(str(i+1) + '. ' + movieName4 )

"""

"""
######################predicitons using Matrix-Factorization
print('')
print('Making more recommendations...')

algo1 = SVD()
algo1.fit(trainset)

predictions1 = algo1.test(testset)
dictMovies1 = get_top_n(predictions1)
topMovies1 = dictMovies1.get(672)
"""


"""
#model dumping
file_name1 = 'MFModelDump'
dump.dump(file_name1, algo=algo1)

#to reload dump
_, loaded_algo1 = dump.load(file_name)
predictions_loaded_algo1 = loaded_algo.test(testset)
"""
"""

print('')
print('Here are the top 5 recommendations based on Matrix-Factorization! ')

for i in range(5):

    movieRecc1 = topMovies1[i]
    movieRawID1 = movieRecc1[0]
    movieName1 = movie[movieRawID1]
    print(str(i+1) + '. ' + movieName1 )
"""

"""
#################predictions using Slope-One
print('')
print('Making more recommendations...')


algo2 = SlopeOne()
algo2.fit(trainset)

predictions2 = algo2.test(testset)
dictMovies2 = get_top_n(predictions2)
topMovies2 = dictMovies2.get(672)
"""

"""
#model dumping
file_name3 = 'SlopeOneModelDump'
dump.dump(file_name3, algo=algo2)

# to reload dump
_, loaded_algo3 = dump.load(file_name)
predictions_loaded_algo3 = loaded_algo.test(testset)
"""
"""
print('')
print('Here are the top 5 recommendations based on Slope-One! ')

for i in range(5):

    movieRecc2 = topMovies2[i]
    movieRawID2 = movieRecc2[0]
    movieName2 = movie[movieRawID2]
    print(str(i+1) + '. ' + movieName2 )


#############predictions using Co-Clustering
print('')
print('Making more recommendations...')


algo3 = CoClustering()
algo3.fit(trainset)

predictions3 = algo3.test(testset)
dictMovies3 = get_top_n(predictions3)
topMovies3 = dictMovies3.get(672)
"""

"""
#model dumping
file_name4 = 'CoClusterModelDump'
dump.dump(file_name4, algo=algo3)

#to reload dump
_, loaded_algo4 = dump.load(file_name)
predictions_loaded_algo4 = loaded_algo.test(testset)
"""
"""
print('')
print('Here are the top 5 recommendations based on Co-Clustering! ')

for i in range(5):

    movieRecc3 = topMovies3[i]
    movieRawID3 = movieRecc3[0]
    movieName3 = movie[movieRawID3]
    print(str(i+1) + '. ' + movieName3 )
"""


"""
##################Evaluations of Algorithms: Precision and Recall

# precision and recall for Baseline Algo
#kf = KFold(n_splits=5)

#for trainset, testset in kf.split(data):

precisions, recalls = precision_recall_at_k(predictions4, k=5, threshold=4)
precisions1, recalls1 = precision_recall_at_k(predictions1, k=5, threshold=4)
precisions2, recalls2 = precision_recall_at_k(predictions, k=5, threshold=4)
precisions3, recalls3 = precision_recall_at_k(predictions2, k=5, threshold=4)
precisions4, recalls4 = precision_recall_at_k(predictions3, k=5, threshold=4)

# Precision and recall can then be averaged over all users
print('')
print('Evaluations for all the algorithms used in this system:')

print('')
print('Precision and Recall for Baseline Algorithm')

x = sum(prec for prec in precisions4.values()) / len(precisions4)
y = sum(rec for rec in recalls4.values()) / len(recalls4)
print(x)
print(y)

print('')
print('Precision and Recall for Matrix-Factorization')

x1 = sum(prec for prec in precisions1.values()) / len(precisions1)
y1 = sum(rec for rec in recalls1.values()) / len(recalls1)
print(x1)
print(y1)

print('')
print('Precision and Recall for K-NN')

x2 = sum(prec for prec in precisions.values()) / len(precisions)
y2 = sum(rec for rec in recalls.values()) / len(recalls)
print(x2)
print(y2)

print('')
print('Precision and Recall for Slope-One')

x3 = sum(prec for prec in precisions2.values()) / len(precisions2)
y3 = sum(rec for rec in recalls2.values()) / len(recalls2)
print(x3)
print(y3)

print('')
print('Precision and Recall for Co-Clustering')

x4 = sum(prec for prec in precisions3.values()) / len(precisions3)
y4 = sum(rec for rec in recalls3.values()) / len(recalls3)
print(x4)
print(y4)


listPrecision = [x, x1, x2, x3, x4]
listRecall = [y, y1, y2, y3, y4]
listNames = ['Baseline Algorithm', 'Matrix-Factorization', 'K-NN', 'Slope-One', 'Co-Clustering']

# z is the index of the highest precision and q is the index of the highest recall
z = 0
q = 0

for i in range(1, 5):
    num1 = listPrecision[i]
    num2 = listPrecision[z]
    num3 = listRecall[i]
    num4 = listRecall[q]

    if (num1 > num2):
        z = i
    if (num3 > num4):
        q = i

print('')
print (str(listNames[z]) + ' had the highest precision: ' + str(listPrecision[z]))
print(str(listNames[q]) + ' had the highest recall: ' + str(listRecall[q]))


print('')
print('Thanks for using this movie recommender system. Goodbye!')
print('')
"""