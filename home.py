import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
 [
    Page("home.py", "APPLICATION OF MACHINE LEARNING", "👩‍💻"),
    Section("THE APPLICATION OF LEARNINGS"),
    Page("pages/aboutme.py", "ABOUT MYSELF", "📝", in_section=True),
    Page("pages/description.py", "DESCRIPTION", "🔐", in_section=True),
    Page("pages/itqmtlearnings.py", "LEARNINGS", "📘", in_section=True),

    Section("PROJECTS", "💾"),
    Page("pages/prediction.py", "PREDICTION", "🎨", in_section=True),
    Page("pages/sentimentemotion.py", "EMOTION ANALYZER", "🚀", in_section=True),
    Page("pages/imageclassifier.py", "IMAGE CLASSIFICATION", "🔎", in_section=True),

    Section("SOURCE CODE", "📄"),
    Page("pages/prediction_src.py", "PREDICTION SOURCE CODE", "⭐", in_section=True),
    Page("pages/sentimentemotionanalyzer_src.py", "EMOTION ANALYZER SOURCE CODE", "⭐", in_section=True),
    Page("pages/imageclassifier_src.py", "IMAGE CLASSIFICATION SOURCE CODE", "⭐", in_section=True),
]
)

hide_pages(["Thank you"])

st.header("AUSTINE KYLE BELLO BSIS 3B")
st.subheader("Final Requirements in ITEQMT")

st.markdown("---")

st.image("pict/k1.jpg")

# Display info box
st.info("⚙️This application illustrates various machine learning methods applied in quality management🤖")

# Display divider
st.markdown("---")


st.image("pict/ML2.jpg")

# Display more markdown content
st.write("""
#
Machine learning is a powerful technology that enables computers to learn and make decisions based on data patterns 
         instead of explicit programming instructions. In image classification, machine learning algorithms can be 
         trained to automatically recognize and categorize objects in images, such as determining whether a photo.
         Emotion analysis uses machine learning to interpret emotions from text or speech, allowing applications to
          understand and respond to human sentiments in online reviews or conversations. Furthermore, machine learning
          is excellent for prediction tasks, as it analyzes historical data to forecast future outcomes, such as 
         predicting customer preferences or medical diagnoses. These applications are essential because they automate
          complex processes, improve decision-making accuracy, and drive innovation in industries like healthcare,
          finance, and entertainment.
### 🌟🌟 Star the project on Github 🌟🌟 
<iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Additional custom styles
custom_styles = """
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
"""
st.markdown(custom_styles, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)