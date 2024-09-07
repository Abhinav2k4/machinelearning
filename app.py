import streamlit as st
import pickle
import pandas as pd
import requests

def fetch(movie_id):
    res=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c16a3b0ae7619799141635a98de1fbe0&language=en-US'.format(movie_id))
    data=res.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

mvsdict=pickle.load(open('mvslist','rb'))
movies=pd.DataFrame(mvsdict)
simil=pickle.load(open('sim.pkl','rb'))


def recommend(movie):
    ind=movies[movies['title']==movie].index[0]
    dist=simil[ind]
    movies_list=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
    reco=[]
    pos=[]
    for i in movies_list:
        reco.append(movies.iloc[i[0]].title)
        pos.append(fetch(movies.iloc[i[0]].id))
    return reco,pos


st.title('MOVIE RECOMMENDER SYSTEM')
option = st.selectbox(
    "state a movie for recommendation:",
    (movies['title'].values)
)

if st.button("Recommend"):
    names,posters=recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])



