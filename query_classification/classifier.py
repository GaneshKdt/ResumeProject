import sys
sys.path.append(r"C:\Users\Ganesh\Documents\Resume Project\query_classification\query_classification")
from helper import preprocessing
import pickle
import numpy as np
#import streamlit as st
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open('ngasce_word2vec.pkl','rb'))
rf = pickle.load(open('rf_classifier.pkl','rb'))

def query_vec(query):
    query = [word for word in query.split() if word in model.wv.index_to_key]
    return np.mean(model.wv[query], axis=0)

def binary_pred(query):
    query= preprocessing(query)
    run=True
    if query =="null":
        run=False
    if run!=False:
        query = query_vec(query)
        query = query.reshape(1, -1)
        query = rf.predict(query)
    return query[0]

def result(query):
    score = binary_pred(query)
    if score == 0 or score == "0":
        return "Academic query"
    elif score == 1 or score == "1":
        return "Course query"
    elif score == 2 or score == "2":
        return "Technical query"
    else:
        return "Invalid query"
