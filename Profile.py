import streamlit as st

st.set_page_config(page_title="My Data Portfolio", page_icon="❅")

st.title("👋 Welcome!")

st.markdown("""
    <h3 style='text-align: left; font-size: 36px;'>
        Hey, I'm <span style='color:#D17D98; font-weight:bold;'>Iris Lu</span> :)
    </h3>
""", unsafe_allow_html=True)

st.markdown("I'm a master’s student at NYU studying computer science with a focus in data science.")
st.markdown("From building ML models to uncovering patterns through data storytelling, I believe insight—like art—is all about perspective.")


st.markdown("""
### Contact Me
- [💼 LinkedIn](https://www.linkedin.com/in/hsinyuanlu/)
- [💻 GitHub](https://github.com/irishyl)
- [📧 Email](mailto:iris.hsinyuanlu@gmail.com)
""")

st.write("Navigate to my projects from the sidebar.")
