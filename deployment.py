import streamlit as st
import joblib

classi=joblib.load(r"C:\Users\GHANI\Titanic.pkl")
label1=joblib.load(r"C:\Users\GHANI\lb.pkl")
label2=joblib.load(r"C:\Users\GHANI\lb1.pkl")
stand=joblib.load(r"C:\Users\GHANI\st.pkl")

st.title("Titanic survivor")
st.header("Data Analysis")

pclass=st. number_input("Enter your Pclass:")
sex=st.selectbox("Select sex:",['female', 'male'])
age=st.number_input("Enter your age:") 
sibsp=st.number_input("Enter your sibsp:") 
parch=st.number_input("Enter your Parch:") 
Fare=st.number_input("Enter your Fare:")
Embarked=st. selectbox("Select Embarked:",['C','S'])

sex=label1.transform([sex])[0]
Embarked=label2.transform([Embarked])[0]

if st.button("Predict"):
    result=classi.predict(stand.transform([[pclass,sex,age,sibsp,parch,Fare,Embarked]]))[0]
    if result==0:
        st.success("Dead".format(result))
    else:
        st.success("Alive".format(result))