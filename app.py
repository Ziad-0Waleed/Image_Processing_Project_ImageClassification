import streamlit as st
import numpy as np
from keras.preprocessing.image import load_img
from keras.models import load_model

import matplotlib.pyplot as plt

# Load the trained model
model = load_model('model.h5')  # Replace with the path to your saved model

# Streamlit app
st.title("Dog vs Cat Classifier")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess the image
    img = load_img(uploaded_file, target_size=(128, 128))
    img_array = np.array(img) / 255.0  # Normalize the image
    img_array = img_array.reshape(1, 128, 128, 3)  # Reshape for prediction

    # Make prediction
    pred = model.predict(img_array)
    label = "Dog" if pred[0] > 0.5 else "Cat"
    
    # Display the result
    st.write(f"Prediction: {label}")
    
    # Optionally, display the confidence score
    st.write(f"Confidence: {pred[0][0]:.2f}")