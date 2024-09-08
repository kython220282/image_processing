import streamlit as st
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

st.title('🎈 Image Processing Application')

st.write('Open source application designed to different Image processing task')
st.write('----------------')

uploaded_file = st.file_uploader("Choose a png or jpg file", type=['png', 'jpg'] )

col1, col2 = st.columns(2)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
