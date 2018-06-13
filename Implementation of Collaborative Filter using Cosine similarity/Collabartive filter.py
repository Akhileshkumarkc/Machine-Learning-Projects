__author__ = "Akhilesh Kumar , Shurti Bidada"

#User Based Collaborative filtering to find the Rating of the  user and predicted the data

import pandas as pd
import numpy as np
import time
from debug import *
movie_position = 0
userid_position = 1



####################################################################
# Pearson Similarity is given by:
#
# similarity Pearson Co-efficent = covariance  =
# sum_xy(rxi - rxmean) (ryi - rymean) /squareroot( ( sum_xy( rxi - rmean ) sqaure) - (sumxy(ryi - ymean)square ) )
#
############################################################
def pearson_similarity():
    for i in range(len(testdf)):
        movie_k, user_i, = [int(testdf.iat[i, movie_position]), int(testdf.iat[i, userid_position])]

        # Ri
        if user_i in usrs_all:
            user_i_mean = u_mean.loc[user_i]
        else:
            user_i_mean = UserAbsMean

        # Obtain all ratings of movie k
        if movie_k in mov_all:
            #Rk
            rating_diff_js = Rating_minus.loc[:, movie_k]
            # Rjk
            users_j_no_k = rating_diff_js[rating_diff_js.isnull()].index
            # Obtain similarities of user i and users that rated movie k
            # user ith rating
            w = cor_matrix.loc[user_i, :].copy()
            # user jth rating. for K movie.
            w.loc[users_j_no_k] = None
            # find the weight.
            sum_w = w.abs().sum()

            # diff rating
            # diff rating = Weight * sum ( rate of j and k) / sum all of weights.
            if sum_w != 0:
                coll_rating = (w * rating_diff_js).sum() / sum_w
            else:
                coll_rating = 0
        else:
            coll_rating = 0
        # final rating of kth user equal to User i mean + diff rating.
        rating_ik = user_i_mean + coll_rating
        # make the rating lie between 1 and 5.
        max_bound = min(rating_ik, 5)
        min_bound = max(1,max_bound)
        round_value =  round(min_bound, 1)
        predict_values.append(round_value)

    print('Summary results Pearson Similarity:')
    testdf['predictions'] = predict_values
    print('  RMSE:', round(np.sqrt(((testdf['rating'] -
                                     testdf['predictions']) ** 2).mean()), 4))
    print('  MAE: ', round(np.mean(abs(testdf['rating'] -
                                       testdf['predictions'])), 4), '\n')
    testdf.to_csv('predictions_pearson.txt', sep=',', header=False, index=False)
def cosine_similarity_user():
    for i in range(len(testdf)):
        movie_k, user_i, = [int(testdf.iat[i, movie_position]), int(testdf.iat[i, userid_position])]

        # Ri
        if user_i in usrs_all:
            user_i_mean = u_mean.loc[user_i]
        else:
            user_i_mean = UserAbsMean

        # Obtain all ratings of movie k
        if movie_k in mov_all:
            #Rk
            rating_diff_js = Rating_minus.loc[:, movie_k]
            # Rjk
            users_j_no_k = rating_diff_js[rating_diff_js.isnull()].index
            # Obtain similarities of user i and users that rated movie k
            # user ith rating
            w = cor_matrix.loc[user_i, :].copy()
            # user jth rating. for K movie.
            w.loc[users_j_no_k] = None
            # find the weight.
            sum_w = w.abs().sum()

            # diff rating
            # diff rating = Weight * sum ( rate of j and k) / sum all of weights.
            if sum_w != 0:
                coll_rating = (w * rating_diff_js).sum() / sum_w
            else:
                coll_rating = 0
        else:
            coll_rating = 0
        # final rating of kth user equal to User i mean + diff rating.
        rating_ik = user_i_mean + coll_rating
        # make the rating lie between 1 and 5.
        max_bound = min(rating_ik, 5)
        min_bound = max(1,max_bound)
        round_value =  round(min_bound, 1)
        predict_values.append(round_value)

    print('Summary results cosine Similarity:')
    testdf['predictions'] = predict_values
    print('  RMSE:', round(np.sqrt(((testdf['rating'] -
                                     testdf['predictions']) ** 2).mean()), 4))
    print('  MAE: ', round(np.mean(abs(testdf['rating'] -
                                       testdf['predictions'])), 4), '\n')
    testdf.to_csv('predictions_pearson.txt', sep=',', header=False, index=False)
def cosine_similarity():
    for i in range(len(testdf)):
        movie_k, user_i, = [int(testdf.iat[i, movie_position]), int(testdf.iat[i, userid_position])]

        # Rk
        # Obtain all ratings of all user i
        if user_i in usrs_all:
            # Ri
            rating_sum_ls = rating_sum.iloc[user_i,:]
            # Rki
            movie_l_no_i = rating_sum_ls[rating_sum_ls.isnull()]
            # Obtain similarities of movie K and movie l that rated by user i
            # movie kth rating
            w = cor_matrix_m.loc[movie_k, :].copy()
            # movie lth rating. for i movie.
            w.loc[movie_l_no_i] = None
            # find the weight.
            sum_w = w.abs().sum()


            if sum_w != 0:
                coll_rating = (w * rating_sum_ls).sum() / sum_w
            else:
                coll_rating = 0
        else:
            coll_rating = 0
        # final rating of ith user  equal to for k th movie mean K + diff rating.
        rating_il = coll_rating
        # make the rating lie between 1 and 5.
        max_bound = min(rating_il, 5)
        min_bound = max(1, max_bound)
        round_value = round(min_bound, 1)
        predict_values.append(round_value)

    print('Summary results Pearson Similarity:')
    testdf['predictions'] = predict_values
    print('  RMSE:', round(np.sqrt(((testdf['rating'] -
                                     testdf['predictions']) ** 2).mean()), 4))
    print('  MAE: ', round(np.mean(abs(testdf['rating'] -
                                       testdf['predictions'])), 4), '\n')
    testdf.to_csv('predictions_cosine.txt', sep=',', header=False, index=False)


def itemBased():
    global PivTabUMI, cor_matrix_m, rating_sum
    PivTabUMI = traindf.pivot(index='userid', columns='movieid',
                              values='rating')
    cor_matrix_m = PivTabUMI.corr().fillna(0)
    print('Building predictions')
    rating_sum = PivTabUMI.count(axis=1)
    print("Print Pivot table")
    print(PivTabUMI)
    PivTabUMI.describe()
    print("rating_diff Matrix")
    print(rating_sum)
    cosine_similarity()


if __name__ == "__main__":

    print("Performing Collaborative Filtering for NetFlix Dataset")

    start = time.time()
    DataSetDict = {}
    DataSetDict['traindata'] = 'data/training.txt'
    DataSetDict['testdata'] = 'data/testing.txt'
    #train Dataset
    traindf = pd.read_csv(DataSetDict['traindata'], header=None, names =['movieid', 'userid', 'rating'])
    testdf = pd.read_csv(DataSetDict['testdata'], header=None, names =['movieid', 'userid', 'rating'])


    print ('Generating Pearson Similarity Matrix ')

    PivTabUMI = traindf.pivot(index ='userid', columns ='movieid',

                              values = 'rating')
    print("**************************Pivot Table of Userid with movie id with rating sample.********************************")
    print(PivTabUMI.head(5))
    print("**************************Pivot Table End.********************************")
    #user mean.
    u_mean = PivTabUMI.mean(axis = 1)

    # co -relation Matrix for the User i with User j
    # with na values as 0.
    # obtained by pivotting the Correlation Matrix.
    # for dummy means


    cor_matrix = PivTabUMI.T.corr().fillna(0)

    print ('Executing the Rating Algorithm')


    #  calculating (user ith rating - mean Ri of user rating.)
    Rating_minus = PivTabUMI.sub(PivTabUMI.mean(axis=1), axis=0)
    PivTabUMI.describe()
    predict_values = []
    UserAbsMean = u_mean.mean()
    usrs_all = u_mean.index
    mov_all = Rating_minus.columns


    pearson_similarity()

    Rating_minus = PivTabUMI.mul(1, axis=0)
    PivTabUMI.describe()
    predict_values = []
    UserAbsMean = u_mean.mean()
    usrs_all = u_mean.index
    mov_all = Rating_minus.columns
    cosine_similarity_user()

    #itemBased()
    print ('Total time taken : ', time.time() - start)

''' ========================================================================'''