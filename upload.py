import streamlit as st 
import firebase_admin
import pandas as pd 
from firebase_admin import auth 
from firebase_admin import credentials
import firebase_admin
from firebase_admin import firestore
import time 

stream = ['Medical', 'Non-Medical', 'Other']
classOption = ['9', '10', '11', '12', 'Dropper']

creds = credentials.Certificate("counseling-b30aa-firebase-adminsdk-uamom-90e1db5d4e.json")
try:
    firebase_admin.get_app()
except ValueError:
    print('error')
    firebase_admin.initialize_app(creds)
global db
db = firestore.client()

def upload_question(stream, batch, question, answer) :
    payload = {
        'stream' : stream,
        'batch' : batch, 
        'question' : question,
        'answer' : answer
    } 

    docRef = db.collection(f'{stream}').document(f'{batch}-{time.time()}')
    docRef.set(payload)



st.title('Counselling session questions')

st.write('Please enter the details about the session.')

col11, col12 = st.columns(2)

stream = col11.selectbox('Select Stream', stream)
batch = col12.selectbox('Select Batch', classOption)


question = st.text_area('Enter the question.')

answer = st.text_area('Enter your answer.')

if st.button('Submit'):
    upload_question(stream,batch,question,answer)
    st.success('Question uploaded!')
