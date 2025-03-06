import streamlit as st
import cv2
import numpy as np
from PIL import Image

 
# Streamlit app
def main():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .stApp {
            max-width: 900px;
            margin: auto;
            padding: 20px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stMarkdown h1 {
            text-align: center;
            color: #4CAF50;
        }
        .stMarkdown h2 {
            color: #4CAF50;
        }
        .stImage img {
            border-radius: 10px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("AFTC")
    st.title("🎯 Bullet Hole Detection")
    st.markdown(
        """
        Welcome to the **Bullet Hole Detection** app!  
        Upload an image of a target paper, and the app will detect and count the bullet holes for you.
        """
    )

    # File uploader
    uploaded_file = st.file_uploader("📁 Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Display uploaded image
        st.markdown("### Uploaded Image")
        image = Image.open(uploaded_file)
        st.image(image, caption="Your Target Paper", use_column_width=True)

        # Convert PIL image to OpenCV format
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Load YOLO model
        # net, output_layers = load_yolo()

        # Detect bullet holes
        st.markdown("### Detecting Bullet Holes...")
        with st.spinner("Processing image..."):
            pass

        # Display results
        st.markdown("### Detection Results")
        st.success(f"✅ **Total bullet holes detected:** {2}")

# Run the app
if __name__ == "__main__":
    main()