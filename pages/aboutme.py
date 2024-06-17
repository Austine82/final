import streamlit as st

st.title("ALL ABOUT AUSTINE📌🤝")

st.markdown("---")
image_paths = ["pict/k2.jpg"]

cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)

st.header("👦BELLO, AUSTINE KYLE♛")
st.markdown("---")


# Personal Information
st.header("💪PERSONAL INFORMATION 💪")
st.write("**Name:** AUSTINE KYLE BELLO")
st.write("**Age:** 21 years old 🎂")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY 🎓")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student 💻📚")
st.write("**Hobbies:** Singing🎤 playing guitar🎸🎧 ✩♬ ₊˚.🎧⋆☾⋆⁺₊✧ ")

with st.expander("Envision my self:⬇️"):
    st.markdown("""   
    #
A decade from now, I picture myself as a successful entrepreneur. While I might not be directly using my
                 Information Systems degree, I will harness my skills in data analysis, software development,
                 and problem-solving to carve out a unique path. I envision leading a thriving business that 
                seamlessly combines my love for technology with my creative interests, possibly in digital art or 
                interactive storytelling. This venture will not only provide financial security but also leverage 
                technology to make a positive difference in people's lives.
    """, unsafe_allow_html=True)



st.header("✨ Inspirational Quotes")
st.write("1. \"Be true to yourself and live genuinely. Your soul's purpose is to shine in its own unique way. Discover your truth, stay authentic, and everything will fall into place.\" 🌟")
st.write("2. \"Success isn't about never failing; it's about getting up stronger every time you fall.\" 💪")
st.write("3. \"Life will throw many challenges your way, but never let them defeat you.\" 🌈")

st.header("🎵 Favorite Songs")
st.write("1. *\"Blinding Lights\"* 🌟")
st.write("2. *\"Levitating\"* ✨")
st.write("3. *\"Shape of You\"* 🎶")

st.header("🍽️ Favorite Foods")
st.write("1. *\"Mango Smoothie\"* 🥭")
st.write("2. *\"Chocolate Ice Cream\"* 🍫")
st.write("3. *\"Sushi\"* 🍣")






st.markdown(
    """
    <style>
    .stApp {
        background-color: #A7E6FF;
        padding: 2em;
    }
    h1, h2 {
        color: #6F4E37;
    }
    .stText {
        font-size: 1.5em;
        color: #322C2B;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### * * * Thank you for visiting my profile! * * * ")
