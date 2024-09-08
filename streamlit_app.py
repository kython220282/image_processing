import streamlit as st
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image
import io


st.set_page_config(layout="wide")
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
 
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Upload Image")
    uploaded_file = st.file_uploader("Choose a png or jpg file", type=['png', 'jpg'] )
    

with col2:
    st.subheader("Uploaded Image")
    if uploaded_file is not None:
        try:
            # Read the image file
            image_bytes = uploaded_file.read()
            image = Image.open(io.BytesIO(image_bytes))
           
            # Convert to numpy array
            image_array = np.array(image)
                      
            # Display original image dimensions
            st.write(f"Original dimensions: {image.width} x {image.height} pixels")
            
            # Estimate original size in inches (assuming 96 DPI)
            original_width_inches = image.width / 96
            original_height_inches = image.height / 96
            st.write(f"Original size: {original_width_inches:.2f} x {original_height_inches:.2f} inchs (at 96 DPI)")
            # Display the uploaded image
            st.image(image, use_column_width=True)
        except Exception as e:
            st.error(f"Error opening the image: {e}")
    else:
        st.write("Please upload an image")

with col3:
    st.subheader("Select processed image dimensions")
    if uploaded_file is not None:
        # Input for desired width and height in inches
        width_inches = st.number_input("Desired width (inches)", min_value=0.1, max_value=100.0, value=original_width_inches, step=0.1)
        height_inches = st.number_input("Desired height (inches)", min_value=0.1, max_value=100.0, value=original_height_inches, step=0.1)
        
        # Input for DPI
        dpi = st.number_input("DPI (dots per inch)", min_value=1, max_value=1200, value=96, step=1)
        
        # HD Sharpening amount input
        sharpen_amount = st.slider("HD Sharpening amount", min_value=0.0, max_value=2.0, value=0.0, step=0.1)

  
