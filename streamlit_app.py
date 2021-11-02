import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek

st.success('Witaj w aplikacji!')
st.balloons()

# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('English to German translator')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

st.header('Aplikacja tłumacząca zdania napisane w języku angielskim na język niemiecki')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

col1, col2, col3 = st.columns(3)

with col1:
    st.write('')

with col2:
    st.image('data:image/png;base64,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')

with col3:
    st.write('')

st.subheader('O aplikacji')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

st.write('Aplikacja korzysta z biblioteki hugginface')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

st.write('Korzystamy z następującego pipeline:')
st.code('pipeline("translation_en_to_de")', language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji


st.header('English to German translator')

import streamlit as st
import json
from transformers import pipeline

text = st.text_area(label="Wpisz tekst w polu poniżej:")
translation = pipeline("translation_en_to_de")
translated = translation(text)
#[{'translation_text': 'hi'}]
y = json.dumps(translated)
z = json.loads(y)
#st.info(translated)
st.info(z[0]["translation_text"])
st.success("Success!")

bol1, bol2, bol3 = st.columns(3)

with bol1:
    st.write('')

with bol2:
    st.write('')
    
with bol3:
    st.write('🐞 Kamil Suchojad s19063')


