import streamlit as st
import pandas as pd
import random
from random import choice
import time
import requests
from streamlit_lottie import st_lottie



st.set_page_config(page_title='CuppaChoices', page_icon=":coffee:")




header = st.container()
question = st.container()




def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_jyhoqy6d.json")


with header:
    st.title("CuppaChoices")
    st.text("Data pulled from various websites about Starbucks drinks and how they impact mood")

with question:
    df = pd.read_csv('CoffeeMoodd.csv',)

    Tired = df['Tired']

    Happy = df['Happy']

    Anxious = df['Anxious']

    Sad = df['Sad']

    

    
    st.subheader("How ya doin? Pick ya mood, capeesh? Let me pick ya cup o Joe")
    my_bar = st.progress(0)
    
        

    c1,c2,c3,c4 = st.columns(4)
    with c1:
        Tired_BT = st.button("Tired")
    st.write(Tired_BT)
    if Tired_BT:
        st.write("Yeah, I'm tired tooh. Tooh much walking ova hea. Wake up with this, capeesh?")
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        
        st.write(random.choice(Tired.dropna()))
    
        
       
            
        

    with c2:
        Happy_BT = st.button("Happy")
    st.write(Happy_BT)
    if Happy_BT:
        st.write("You're happy? And you want to be happier? Whats tha matta with yooh? Anyway hea ya go, I guess >.>")
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        
        st.write(random.choice(Happy.dropna()))
        

    with c3:
            Anxious_BT = st.button("Anxious")
    st.write(Anxious_BT)
    if Anxious_BT:
        st.write("Anxious huh? I know a guy who knows a guy that's anxious. He drinks this")
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        
        st.write(random.choice(Happy.dropna()))

    with c4:
        Sad_BT = st.button("Sad")
    st.write(Sad_BT)
    if Sad_BT:
        st.write("I feel bad for ya, goomba. Hea, get ya self in gear with one o these. Life gets betta, trust me, kid")
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        
        st.write(random.choice(Sad.dropna()))
    left_column, right_column = st.columns(2)
    with right_column:
        st_lottie(lottie, height=250, key="coding",)