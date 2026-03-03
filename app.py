import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "magnetic_tile_defect_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

IMG_SIZE = (128, 128)

st.title("VisionSpec-QC: Magnetic Tile Defect Detection")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = image.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        st.error("Prediction: DEFECT ❌")
    else:
        st.success("Prediction: PASS ✅")

    st.write(f"Confidence Score: {prediction:.4f}")
