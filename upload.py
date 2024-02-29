import streamlit as st
import os

# Display a subheader
st.subheader("Upload your PDF files")

# Allow users to upload PDF files
uploaded_files = st.file_uploader("Choose PDF file(s)", accept_multiple_files=True)
print(uploaded_files)
# Define directory to save the uploaded files
upload_dir = "uploads"

# Create the upload directory if it doesn't exist
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

# Process the uploaded PDF files if any
if uploaded_files:
    print("here")
    for file in uploaded_files:
        # Save the file to the upload directory
        file_path = os.path.join(upload_dir, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getvalue())
        
        # Display confirmation message
        st.write(f"File '{file.name}' saved successfully!")
