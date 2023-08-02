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
if st.button("Refresh"):
    x=db.reference("/Task").get()
    st.table(x)