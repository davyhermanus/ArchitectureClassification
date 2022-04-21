import streamlit as st
st.title("Image Classification with Google's Teachable Machine")
st.header("Arhictecture Image Classification")
st.text("Upload an image of house for classification")
from img_classification import teachable_machine_classification
uploaded_file = st.file_uploader("Choose a brain MRI ...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded MRI.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'brain_tumor_classification.h5')
        if label == 0:
            st.write("The MRI scan has a brain tumor")
        else:
            st.write("The MRI scan is healthy")
