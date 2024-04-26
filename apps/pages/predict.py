import streamlit as st
import joblib
from scripts.utils.utils import lemmaToken
import time

st.set_page_config(page_title='Predict')

model = joblib.load('apps/saved/model/NB_lemma_Tfidf.pkl')
tokenizer = joblib.load('apps/saved/tokenizer/tokenizer.pkl')
resTag = ['World', 'Sports', 'Business', 'Sci/Tech']

def predict(text:str):
    '''
    input : str : query of the text that will be predicted
    '''
    query = tokenizer.transform([text])
    predicted = model.predict(query)
    return predicted

st.header('News Tag Classifier')
st.subheader('Enter news heading')
st.subheader(f'Available tags {[tag for tag in resTag]}')

textInput = st.text_area('Write your news headings or title', '')

if st.button('Classify'):
    res = predict(textInput)
    with st.spinner('Wait for prediction...'):
        time.sleep(.5)
        st.write('Prediction:', resTag[res[0]])