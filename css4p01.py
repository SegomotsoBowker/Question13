# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:58:34 2024

@author: Bouker
"""

import pandas as pd
df = pd.read_csv("C:/Users/Bouker/Project 1/movie_dataset.csv")
df_cleaned = df.dropna()
print(df)

#Question1
highest_rating = df_cleaned[df_cleaned['Rating'] == df_cleaned['Rating'].max()]
print("Highest-rating:", highest_rating['Title'].values[0])

#Question2
average_revenue = df_cleaned['Revenue (Millions)'].mean()
print("Average revenue of all movies:", average_revenue)

#Question3
average_revenue_from_2015_to_2017 = df_cleaned[(df_cleaned['Year'] >= 2015) & (df_cleaned['Year'] <= 2017)]['Revenue (Millions)'].mean()
print("Average revenue of movies from 2015 to 2017:", average_revenue_from_2015_to_2017)

#Question4
movies_2016 = df_cleaned[df_cleaned['Year'] == 2016]
num_movies_2016 = len(movies_2016)
print("Number of movies released in 2016:", num_movies_2016)


#Question5
movies_nolan = df_cleaned[df_cleaned['Director'] == 'Christopher Nolan']
num_movies_nolan = len(movies_nolan)
print("Number of movies directed by Christopher Nolan:", num_movies_nolan)


#Question6
high_rated_movies = df_cleaned[df_cleaned['Rating'] >= 8.0]
num_high_rated_movies = len(high_rated_movies)
print("Number of movies with a rating of at least 8.0:", num_high_rated_movies)

#Question7
median_rating_nolan = movies_nolan['Rating'].median()
print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan)

#Question8
year_with_highest_avg_rating = df_cleaned.groupby('Year')['Rating'].mean().idxmax()
print("Year with the highest average rating:", year_with_highest_avg_rating)

#Question9
movies_2006 = df_cleaned[df_cleaned['Year'] == 2006]
movies_2016 = df_cleaned[df_cleaned['Year'] == 2016]

percentage_increase = ((len(movies_2016) - len(movies_2006)) / len(movies_2006)) * 100
print("Percentage increase in number of movies between the years 2006 and 2016:", percentage_increase)

#Question10
from collections import Counter

all_actors = df_cleaned['Actors'].str.split(', ').sum()
most_common_actor = Counter(all_actors).most_common(1)[0][0]
print("The most common actor in all movies:", most_common_actor)

#Question11
number_unique_genres = df_cleaned['Genre'].str.split(', ').explode().nunique()
print("Number of unique genres:", number_unique_genres)

#Question12
correlation_matrix = df_cleaned.corr()
print("Correlation Matrix:")
print(correlation_matrix)






