import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns 
import warnings
warnings.filterwarnings("ignore") 
sns.set_style('dark')  
#%matplotlib inline

ratings_data = pd.read_csv("ml-latest-small/ratings.csv")  

movie_names = pd.read_csv("ml-latest-small/movies.csv")  
movie_data = pd.merge(ratings_data, movie_names, on='movieId') 
(movie_data.head())
movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head() 
ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())  
ratings_mean_count.head() 
user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')  
user_movie_rating.head() 
x=input("enter movie")
forrest_gump_ratings = user_movie_rating[x] 
forrest_gump_ratings.head() 
movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])  
corr_forrest_gump.dropna(inplace=True)  
corr_forrest_gump.head()  
corr_forrest_gump.sort_values('Correlation', ascending=False).head(10)
corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])  
corr_forrest_gump.head()  
print (corr_forrest_gump[corr_forrest_gump ['rating_counts']>50].sort_values('Correlation', ascending=False).head())


#input:Forrest Gump (1994)
#input:Pocahontas (1995)