import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png",)


with col2:
    st.title("Ashmith Maddala")
    content = """
    Hi, I'm Ashmith! I am an aspiring AI/ML engineer passionate about solving real-world problems using computer vision and deep learning. Currently, I am in my third year of undergraduate studies and actively working on research and projects to strengthen my expertise in AI and data science.

    I am particularly interested in AI-powered code generation and developing innovative solutions that push the boundaries of automation. Beyond research, I enjoy building scalable AI applications, exploring new technologies, and contributing to open-source projects. My goal is to pursue a master's degree in AI/ML, publish impactful research, and make meaningful contributions to the field.

    When I'm not coding, you can find me learning about API development, working on my portfolio, or exploring new advancements in deep learning. Feel free to connect with me!
    
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[1:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
    for index, row in df[1:10].iterrows():
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
