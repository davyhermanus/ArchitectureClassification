uploaded_file = st.file_uploader("Choose an image of exterior or interior of the house ...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'keras_model.h5')
        if label == 0:
            st.write("The House is a type of  Mid-Century")
            elif label == 1:
                st.write("The House is a type of  Contemporer")
                elif label == 2:
                    st.write("The House is a type of  Industry")
                    elif label == 3:
                    st.write("The House is a type of  Bohemian")
                    elif label == 4:
                        st.write("The House is a type of  Rustic")
                        elif label == 5:
                            st.write("The House is a type of  Skandinaia")
                                elif label == 6:
                                    st.write("The House is a type of  Neo Classic")
                                    elif label == 7:
                                        st.write("The House is a type of  tropis")
                                        elif label == 8:
                                            st.write("The House is a type of  Modern")                               
        else:
            st.write("The House is a type of  Minimalis")
        
