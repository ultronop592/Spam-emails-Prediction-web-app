# 📧 Spam Mail Detection Web App

This project builds an accurate spam detection model to classify emails as **spam** or **ham** (not spam). It uses **TF-IDF** for feature extraction and a **Logistic Regression** classifier for prediction. The final model is deployed as an interactive web app using **Streamlit Cloud**.

---

## 🧠 Project Overview

- **Goal**: Automatically identify whether an email is spam or legitimate (ham)
- **Dataset**: SMS Spam Collection Dataset (labeled)
- **Algorithm**: Logistic Regression
- **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Tech Stack**: Python, Pandas, Scikit-learn, NLP, Streamlit

---

## 🔁 Workflow

1. **Data Collection**
   - Loaded a labeled dataset of SMS/email messages

2. **Preprocessing**
   - Lowercased text
   - Removed punctuation and stopwords
   - Tokenization and stemming

3. **Feature Extraction**
   - Applied **TF-IDF Vectorization** to convert text into numerical features

4. **Model Training**
   - Trained a **Logistic Regression** classifier using scikit-learn

5. **Evaluation**
   - **Training Accuracy**: 96.7%
   - **Test Accuracy**: 96.6%
   - Evaluated with confusion matrix and classification report

---

## 📈 Model Performance

| Metric         | Score     |
|----------------|-----------|
| Training Acc.  | 96.7%     |
| Test Acc.      | 96.6%     |
| F1-Score       | High (per class) |

---

## 🚀 Deployment (Streamlit Cloud)

### ✅ Step-by-Step Process

1. **Model Serialization**
   - Saved the trained model and **TF-IDF vectorizer** using `pickle`:
     ```python
     pickle.dump(model, open('spam_mail_model.sav', 'wb'))
     pickle.dump(vectorizer, open('vectorizer.sav', 'wb'))
     ```

2. **Build Streamlit App**
   - Created `spam_app.py` to build a web UI using Streamlit
   - Allows user to enter an email message and view prediction result

3. **Create requirements.txt**
   - Required packages:
     ```
     streamlit
     scikit-learn
     pandas
     numpy
     ```

4. **Upload to GitHub**
   - Files pushed to GitHub:
     - `spam_app.py`
     - `spam_mail_model.sav`
     - `vectorizer.sav`
     - `requirements.txt`
     - `README.md`

5. **Deploy on Streamlit Cloud**
   - Logged into [https://streamlit.io/cloud](https://streamlit.io/cloud)
   - Created a new app from the GitHub repository
   - Set:
     - Branch: `main`
     - Main file: `spam_app.py`
   - Clicked **Deploy**

6. **Access Your App**
   - The app becomes publicly accessible at:
     ```
     https://your-app-name.streamlit.app
     ```

---

## 💡 How to Use

1. Open the deployed Streamlit web app
2. Paste or type an email message
3. Click **"Check"**
4. View whether it's classified as **Spam** or **Ham**

---

## 📂 Project Structure

```
├── spam_app.py              # Streamlit web app
├── spam_mail_model.sav      # Trained logistic regression model
├── vectorizer.sav           # TF-IDF vectorizer
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
