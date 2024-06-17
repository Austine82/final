import streamlit as st

st.title("STREAMLIT APPLICATION DESCRIPTION🧪")


st.header('APPLICATION OF MACHINE LEARNING')
st.image("./pict/L1.jfif")

with st.expander("📢EMOTION ANALYZER"):
    st.markdown("""
    #
                This app uses pre-trained machine learning models that are stored as files to figure out emotions from text you enter. 
                It's made using Streamlit, a tool for creating web apps. You can type in text, and the app will predict emotions like happiness, sadness, anger, nervousness, and fear. This helps people understand the emotions in what they've written.

                
    """, unsafe_allow_html=True)

st.header('🌻✨IMAGE CLASSIFICATION𓍢ִ໋🌷͙֒✧˚ ༘ ⋆｡')
st.image("./pict/l4.jfif")


with st.expander("ROOM IMAGE CLASSIFICATION"):
    st.markdown("""
    #
                This app uses machine learning models trained on a dataset from Kaggle to decide if a room in a picture is clean or messy. The models are saved as pickled files and included in a Streamlit web interface for simple setup.
                Users can upload room images through the app. It then analyzes the image and predicts if the room is clean or messy based on what it learned from the dataset. The interface is easy to use, so anyone can upload a picture and 
                quickly find out if the room is considered clean or messy according to the trained model."
    """, unsafe_allow_html=True)

st.header('PREDICTION')
st.image("./pict/l2.jfif")
st.image("./pict/l3.jfif")


with st.expander("🔆LUNG CANCER PREDICTOR"):
    st.markdown("""
    #
              Predicting lung cancer using datasets involves using statistical and machine learning techniques to analyze 
                large sets of data related to the disease. These datasets typically include various types of information 
                such as patient demographics, medical history, genetic markers, imaging data (like CT scans), and possibly 
                lifestyle factors.
    """, unsafe_allow_html=True)