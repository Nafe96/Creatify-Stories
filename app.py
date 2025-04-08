import streamlit as st
import requests

st.set_page_config(page_title="Story Generator", page_icon="📖")
st.title(" Creatify Stories")
st.write("Start a story and let the AI continue it with creativity!")

# 📥 User Inputs
starter = st.text_area("Enter your starting sentence")

genre = st.selectbox("Choose a genre", ["Simple","Fantasy", "Adventure", "Horror", "Mystery", "Romance", "Comedy"])

character = st.text_input("Main character name (optional)")

audience = st.selectbox("Target audience", ["Kids", "Teens", "Adults"])

# 🎬 Story Generation Trigger
if st.button("Generate Story"):
    if not starter:
        st.warning("Please enter a starting sentence!")
    else:
        with st.spinner("Generating your story..."):
            try:
                res = requests.post("http://localhost:8000/generate-story", json={
                    "starter": starter,
                    "genre": genre,
                    "character": character,
                    "audience": audience
                })
                
                data = res.json()
                if "error" in data:
                    st.error(f"Backend Error: {data['error']}")
                else:
                    story = data["story"]
                    st.markdown("### ✨ Here's your story:")
                    st.markdown(story)
                    
            except Exception as e:
                st.error(f"Something went wrong: {e}")