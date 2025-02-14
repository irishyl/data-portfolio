import streamlit as st

st.set_page_config(page_title="My Projects", page_icon="📂")

st.title("📂 My Projects")

def project_card(title, description, collab=None, pdf_link=None, github_link=None, website_link=None):
    st.subheader(title)
    st.write(description)
    
    if collab:
        st.write(collab)
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if pdf_link:
            st.markdown(f"[📄 PDF]({pdf_link})", unsafe_allow_html=True)
    with col2:
        if github_link:
            st.markdown(f"[💻 GitHub]({github_link})", unsafe_allow_html=True)
    with col3:
        if website_link:
            st.markdown(f"[🌐 Website]({website_link})", unsafe_allow_html=True)
    st.divider()


# Image Color Palette Extractor
project_card(
    title="🎨 Image Color Palette Extractor",
    description="""A web app to extract color palette from image using KMeans clustering.""",
    collab=None,
    pdf_link=None,
    github_link=None,
)

# WikiArt Image Classification
project_card(
    title="🎨 WikiArt Image Classification",
    description="""This study classifies WikiArt images into ten artistic styles using CNN architectures. We leveraged AlexNet, VGG16, and ResNet50 for feature extraction and applied them in baseline models (SVM, Random Forest) and advanced transfer learning approaches. To address class imbalance, we filtered the dataset to the top 10 styles and used data augmentation to improve model robustness. Baseline models achieved 50–60% accuracy, while ResNet50 and Vision Transformers (ViT) reached 99.86% and 87.52%, respectively. ResNet50 consistently outperformed other feature extractors.""",
    collab="*with Chloe Kwon and Damini Kaushik*",
    pdf_link="https://drive.google.com/file/d/1HWvMc4z3PC7WUSEiVjZRaKLUBxPQnBeG/view?usp=sharing", 
    github_link="https://github.com/chloe-kwon/CS-GA-2565-Final-Project",
)

# Can Models Learn Human’s Helping Behavior?
project_card(
    title="🧠 Can Models Learn Human’s Helping Behavior?",
    description="""This project builds on Dr. Gureckis and Dr. Osborn Popp’s study "Moment-to-Moment Decisions of When and How to Help Another Person," which highlights the role of reciprocity in helping behaviors. We use Q-Learning and Deep Q-Learning to model and predict helping gestures, exploring how cost, resource capacity, visibility, and prior reciprocity influence decisions. Our approach compares tabular and neural network-based Q-learning models against human behavior. Preliminary results indicate that reciprocity is the strongest predictor of helping, with energy costs and resource disparities also playing significant roles. This work offers insights into the cognitive mechanisms behind altruism and advances computational models of social decision-making.""",
    collab="*with Sophie Juco, Naman Maheshwari, and Utkarsh Prakash Srivastava*",
    pdf_link="https://drive.google.com/file/d/1vb-LT3Uge1r758B33aRVAnLowot5zTT0/view?usp=sharing",  
    github_link="https://github.com/irishyl/DS-GA-PSYCH-GA_project_model_helping", 
)

# Movie Recommendation System
project_card(
    title="🎬 Movie Recommendation System",
    description="""Built a Spark-based recommendation system using 20M movie ratings. 
    Applied MinHash for user segmentation and validated similarities using statistical correlation analysis.""",
    collab="*with Bess Yang and Chloe Kwon*",
    pdf_link="https://drive.google.com/file/d/18Uhf_sqdd6jlwYGMElpFqD9gtmqkAVki/view?usp=sharing",
    github_link="https://github.com/nyu-big-data/capstone-project-cap-19"
)

st.info("More projects coming soon!")
