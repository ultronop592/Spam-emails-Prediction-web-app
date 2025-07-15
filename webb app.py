# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 15:21:32 2025

@author: sraja
"""


import pickle 
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer  


loaded_model = pickle.load(open('C:/Users/sraja/Downloads/Spam mail project/spam_mail_model.sav', 'rb'))
vectorizer = pickle.load(open('C:/Users/sraja/Downloads/Spam mail project/vectorizer.sav', 'rb'))

# creating for a predictive system
def spam_mail_prediction(input_mail):
   # converting text to feature vector
   input_data_feature = vectorizer.transform([input_mail])

# making prediction
   prediction = loaded_model.predict(input_data_feature)
   print(prediction)

   if (prediction[0]==1):
      return 'ham mail'

   else:
     return 'spam mail'
     
     
     

def main():
    #giving title 
    st.title('Spam EMAILS PREDICTION WEB APP')
    st.write("Check if your email message is spam or not using machine learning.")
    
    # giving the details
   # text input for the email body
    message = st.text_input('Enter the email content here:')

    if st.button('Test for Spam'):
        if message.strip() == "":
            st.error("Please enter some text before testing.")
        else:
            # call the function and display its return value
            result = spam_mail_prediction(message)
            st.success(f"Prediction: **{result}**")

if __name__ == '__main__':
    main()