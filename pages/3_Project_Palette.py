import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ''' Summary
# - Streamlit (`st.`): Builds interactive UI components (title, uploads, sliders).
# - OpenCV (`cv2`): Reads and processes the uploaded image.
# - KMeans (from scikit-learn): Clusters colors to find dominant shades.
# - Matplotlib (`plt`): Visualizes the extracted color palette.
# '''

st.title('Color Palette Extractor 🎨') 

# instructions 
st.markdown("### 👋 Instructions")
st.markdown("1. Upload an image (JPG or PNG).")
st.markdown("2. Use the slider to adjust the number of colors.")
st.markdown("3. View your extracted palette, generated using ***K-means clustering.***")

# users upload image files
st.markdown("### 🖼️ Upload Your Image Down Below!")
uploaded_file = st.file_uploader("Your image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # read and display image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1) # byte array -> image array
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert to rgb for display
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # extract color palette using k-means
    def extract_colors(image, num_colors=5):
        image = image.reshape((-1, 3))
        kmeans = KMeans(n_clusters=num_colors)
        kmeans.fit(image)
        return kmeans.cluster_centers_, kmeans.labels_

    # let user choose how many colors they want to extract
    num_colors = st.slider('Number of colors to extract', 2, 15, 5)
    colors, _ = extract_colors(image, num_colors)

    # plot
    def plot_palette(colors):
        plt.figure(figsize=(8, 2))
        for i, color in enumerate(colors):
            plt.fill_between([i, i+1], 0, 1, color=color/255.0)
        plt.xlim(0, len(colors))
        plt.axis('off')
        st.pyplot(plt)

    st.subheader('🌈 Your Color Palette')
    plot_palette(colors)






