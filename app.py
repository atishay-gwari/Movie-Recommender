import streamlit as st
import pickle
import pandas as pd
import requests

def poster(movie_id):
    data=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=f0361dfd925cd2bc239e3c611c1f736c&language=en-US".format(movie_id)')
    data=data.json()
    # print(data)
    poster_path=data['poster_path']
    path="https://image.tmdb.org/t/p/w500/"+poster_path
    return path


def recommender(movie):
    index_movie = movies[movies['title'] == movie].index[0]
    distances = similarity[index_movie]
    movielist=sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    #reverse done to get in descending order
    recommended_movie=[]
    recommended_movie_posters=[]
    for i in movielist:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch p[oster]
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(poster(movie_id))
    return recommended_movie,recommended_movie_posters



movies = pickle.load(open('movies.pkl','rb'))
similarity= pickle.load(open('similarity.pkl','rb'))
movies_list = movies['title'].values


st.title('Movie Recommender System')


selected_movie=st.selectbox('What movies would you want to search?' , movies_list)





if st.button(' Recommend '):
    recommended_movie,recommended_movie_posters = recommender(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie[4])
        st.image(recommended_movie_posters[4])