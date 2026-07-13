# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:37:00 2026

@author: hp
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
import re 
import nltk 
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')

port_stem = PorterStemmer()
model = pickle.load(open("trained_model.sav", 'rb'))
vectorizer = pickle.load(open("vectorizer.sav", 'rb'))

def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stopwords.words('english')]
    stemmed_content = " ".join(stemmed_content)
    return stemmed_content


def prediction(content):
    
    
    stemmed_user = stemming(content)
    vectorized_user = vectorizer.transform([stemmed_user])
    prediction = model.predict(vectorized_user)
    
    if prediction[0] == 0:
        return "Mail Is Legit"
    else:
        return "Mail Is Spam"


def main():
    st.title("Mail Spam Detector Web App")
    
    user_input = st.text_input("Enter The Content Of Mail")
    res = ''
    
    if st.button("Check Results"):
        res = prediction(user_input)
    
    st.success(res)

if __name__ == "__main__":
    main()
    