import streamlit as st
import firebase_admin
from firebase_admin import db,credentials

#Authentication to Firebase
try:
    app = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate("cropdata.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://cropdata-3413b-default-rtdb.firebaseio.com/"})


st.title("Share my Work 📖")

a=st.text_input("Task:")
d=st.text_input("Date:")

if st.button("Submit"):
    st.write("Task: {}".format(a))
    st.write("Submit on: {}".format(d))
    st.success('Submitted')

    #Storage
    fire={"Task":a,"Date":d}
    db.reference("/Task").push().set(fire)