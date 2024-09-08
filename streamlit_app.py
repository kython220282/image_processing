import streamlit as st
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

st.title('🎈 Image Processing Application')

st.write('Open source application designed to different Image processing task')
st.write('----------------')

uploaded_file = st.file_uploader("Choose a png or jpg file", type=['png', 'jpg'] )

col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
