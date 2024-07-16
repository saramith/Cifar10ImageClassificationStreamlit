import streamlit as st
from src.evaluate import evaluate_model
from src.predict import predict_image
import os

# Title of the app
st.title("Model Evaluation and Prediction")

# Sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select a page:", ["Evaluate", "Predict"])

if option == "Evaluate":
    st.header("Evaluate Model")
    # Button to call the evaluate function
    if st.button("Evaluate"):
        result = evaluate_model()
        st.write(f"{result}")

elif option == "Predict":
    st.header("Predict Image")
    # File uploader widget
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary directory
        temp_dir = "upload_folder"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.write(f"File uploaded successfully: {uploaded_file.name}")
        
        # Call predict_image function with the uploaded image path
        result = predict_image(file_path)
        
        # Display prediction result
        st.write("Prediction result:")
        st.json(result)

# Run the Streamlit app
# To run this app, save it as a .py file and run `streamlit run filename.py` in the terminal.
