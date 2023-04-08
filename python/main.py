import pickle
import streamlit as st
import requests

def fetch_poster(event_id):
    full_path = f"event_poster/{event_id}.jpg"
    return full_path

def recommend(event):
    index = events[events['title'] == event].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_event_names = []
    recommended_event_posters = []
    for i in distances[1:6]:
        # fetch the event poster
        event_id = events.iloc[i[0]].id
        recommended_event_posters.append(fetch_poster(event_id))
        recommended_event_names.append(events.iloc[i[0]].title)

    return recommended_event_names,recommended_event_posters


st.header('Рекомендательная система мероприятий')
events = pickle.load(open('pkl/event_list.pkl','rb'))
similarity = pickle.load(open('pkl/similarity.pkl','rb'))

event_list = events['title'].values
selected_event = st.selectbox(
    "Напишите или выберите мероприятие из списка",
    event_list,
    label_visibility="collapsed"
)

if st.button('Показать рекомендации'):
    recommended_event_names,recommended_event_posters = recommend(selected_event)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_event_posters[0])
        st.text(recommended_event_names[0])
    with col2:
        st.image(recommended_event_posters[1])
        st.text(recommended_event_names[1])

    with col3:
        st.image(recommended_event_posters[2])
        st.text(recommended_event_names[2])
    with col4:
        st.image(recommended_event_posters[3])
        st.text(recommended_event_names[3])
    with col5:
        st.image(recommended_event_posters[4])
        st.text(recommended_event_names[4])




