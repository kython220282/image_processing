import streamlit as st
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

# st.set_page_config(layout="wide")

st.title('🎈 Image Processing Application')

st.write('Open source application designed to different Image processing task')
st.write('----------------')

uploaded_file = st.file_uploader("Choose a png or jpg file", type=['png', 'jpg'] )

col1, col2 = st.columns(2)
with col1:
    st.header("Image Uploaded")
    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)
        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)
    else:
        st.write("Please upload an image")


with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
