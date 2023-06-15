import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('diabetes.sav', 'rb'))

st.title('Prediksi Pengidap Penyakit Diabetes')

col1, col2, col3 = st.columns(3)

with col1:Pregnancies = st.number_input('Kehamilan')
with col2:Glucose = st.number_input('Glukosa')
with col3:BloodPressure = st.number_input('Tekanan Darah')
with col1:SkinThickness = st.number_input('Ketebalan Kulit')
with col2:Insulin = st.number_input('Insulin')
with col3:BMI = st.number_input('BMI')
with col1:DiabetesPedigreeFunction = st.number_input('Silsilah Diabetes')
with col2:Age = st.number_input('Umur')

predict = ''

if st.button('Prediksi Pengidap Penyakit Diabetes'):
    predict = model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
    if (predict[0]==0):
        predict = 'Pasien bukan pengidap penyakit diabetes'
    else:
        predict = 'Pasien adalah pengidap penyakit diabetes'
        
st.success(predict)