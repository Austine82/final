import streamlit as st
import pickle
from nltk.classify import NaiveBayesClassifier

# Set the title of the Streamlit app
st.title("(づ ᴗ _ᴗ)づ♡ EMOTION DETECTOR (づ ᴗ _ᴗ)づ♡")

# Input for the user to enter their message
message = st.text_input("Express how you feel today: 😊")

# Load the pre-trained sentiment analysis model
filename = 'pages/kyle.sav'
with open(filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

def word_features(words):
    return dict([(word, True) for word in words])

# Function to classify emotion based on the message
def sayFeeling():
    if message:
        message_tone = loaded_model.classify(word_features(message.split()))

        if message_tone == 'Happy':
            st.write("You are feeling happy 🤭.")
        elif message_tone == 'Scared':
            st.write("Your Feelings are valid ❤️‍🔥.")
        elif message_tone == 'Angry':
            st.write("You are feeling angry 😠.")
        elif message_tone == 'Nervous':
            st.write("You are feeling nervous 😰.")
        else:
            st.write("You are feeling sad 🥺.")
    else:
        st.write("Please enter a message to analyze what you feel.")

if st.button('Say it'):
    sayFeeling()
