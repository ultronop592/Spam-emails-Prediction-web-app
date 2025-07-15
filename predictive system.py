# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 13:14:03 2025

@author: sraja
"""

import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer  
 

loaded_model = pickle.load(open('C:/Users/sraja/Downloads/Spam mail project/spam_mail_model.sav', 'rb'))
vectorizer = pickle.load(open('C:/Users/sraja/Downloads/Spam mail project/vectorizer.sav', 'rb'))

# predictive system
input_mail = ("SIX chances to win CASH! From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply Reply HL 4 info"
)




# converting text to feature vector
input_data_feature = vectorizer.transform([input_mail])

# making prediction
prediction = loaded_model.predict(input_data_feature)
print(prediction)

if (prediction[0]==1):
  print('Ham mail')

else:
  print('Spam mail')