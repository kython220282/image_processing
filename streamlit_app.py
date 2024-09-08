import streamlit as st
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image
import io


def scale_image_inches(image, width_inches, height_inches, dpi):
    # Calculate target dimensions in pixels
    width_pixels = int(width_inches * dpi)
    height_pixels = int(height_inches * dpi)
    
    # Resize the image
    return cv2.resize(image, (width_pixels, height_pixels), interpolation=cv2.INTER_LINEAR)

def hd_sharpen(image, amount):
    image_f = image.astype(float) / 255.0
    blurred = cv2.GaussianBlur(image_f, (0, 0), 3)
    unsharp_mask = image_f - blurred
    sharpened = image_f + amount * unsharp_mask
    sharpened = np.clip(sharpened, 0, 1)
    return (sharpened * 255).astype(np.uint8)



st.title('🎈 Image Processing Application')

st.write('Open source application designed to different Image processing task')
st.write('----------------')

col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Choose a png or jpg file", type=['png', 'jpg'] )
with col2:
    st.write("Select processed image dimensions")
    
st.write('----------------')

col1, col2 = st.columns(2)
with col1:
    st.header("Uploaded Image")
    if uploaded_file is not None:
        try:
            # Read the image file
            image_bytes = uploaded_file.read()
            image = Image.open(io.BytesIO(image_bytes))
            # Convert to numpy array
            image_array = np.array(image)
            # Display the uploaded image
            st.image(image, caption='Uploaded Image', use_column_width=True)
            
            # Display original image dimensions
            st.write(f"Original dimensions: {image.width} x {image.height} pixels")
            
            # Estimate original size in inches (assuming 96 DPI)
            original_width_inches = image.width / 96
            original_height_inches = image.height / 96
            st.write(f"Original size: {original_width_inches:.2f} x {original_height_inches:.2f} inchs (at 96 DPI)")
        except Exception as e:
            st.error(f"Error opening the image: {e}")
    else:
        st.write("Please upload an image")

with col2:
    st.header("Processed Image")
  
