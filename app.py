import numpy as np
from tensorflow.keras.models import load_model
import streamlit as st
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('tokenizer.pkl','rb') as file:
    tokenizer = pickle.load(file)
model = load_model('model.h5')

st.title('Twitter sentiment analysis using RNN')
tweet=st.text_area('Enter tweet: ')

if st.button('Predict Sentiment') and tweet.strip():
    sequences=tokenizer.texts_to_sequences([tweet])
    sequences=pad_sequences(sequences,padding = 'pre',maxlen=166)


    prediction = model.predict(sequences, verbose=0)[0]

    predicted_class = np.argmax(prediction)

    sentiment_map = {
        0: 'Negative',
        1: 'Neutral',
        2: 'Positive'
    }

    st.write("Prediction probabilities:")

    for i, sentiment in sentiment_map.items():
        st.write(f"{sentiment}: {prediction[i]:.4f}")

    st.success(
        f"Predicted sentiment: {sentiment_map[predicted_class]}"
    )