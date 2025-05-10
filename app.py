import streamlit as st
import plotly.express as px
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Cherry's Portfolio",
    page_icon="👋",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .profile-img {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
    }
    .section {
        padding: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 2])
with col1:
    # Replace with your image path
    st.image("profile.jpg", use_container_width=True, caption="Your Name")
with col2:
    st.title("Cherry Mathew Roy")
    st.subheader("Product Manager | UX Designer | Management Consultant | Program Manager")
    st.write("""
    Passionate professional with expertise in product management, UX design, and strategic consulting.
    Focused on creating user-centered solutions and driving organizational success.
    """)

# Navigation
st.markdown("---")
st.markdown("## Quick Navigation")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("About Me")
with col2:
    st.button("Projects")
with col3:
    st.button("Skills")
with col4:
    st.button("Contact")

# About Me Section
st.markdown("---")
st.markdown("## About Me")
st.write("""
I am a versatile professional with experience across multiple domains, including product management,
UX design, management consulting, and program management. My approach combines strategic thinking
with user-centered design principles to deliver impactful solutions.
""")

# Target Roles Section
st.markdown("---")
st.markdown("## Target Roles")

# Product Management
with st.expander("Product Manager"):
    st.write("""
    - Strategic product planning and roadmap development
    - User research and market analysis
    - Agile product development methodologies
    - Cross-functional team leadership
    - Data-driven decision making
    """)

# UX Design
with st.expander("UX Designer/Researcher"):
    st.write("""
    - User research and usability testing
    - Wireframing and prototyping
    - Information architecture
    - User journey mapping
    - Design thinking methodologies
    """)

# Management Consulting
with st.expander("Management Consultant"):
    st.write("""
    - Strategic analysis and recommendations
    - Business process optimization
    - Change management
    - Stakeholder management
    - Market research and competitive analysis
    """)

# Program Management
with st.expander("Program Manager"):
    st.write("""
    - Program planning and execution
    - Risk management
    - Resource allocation
    - Stakeholder communication
    - Performance monitoring and reporting
    """)

# Skills Section
st.markdown("---")
st.markdown("## Skills")

# Create a skills visualization
skills_data = {
    "Category": ["Product", "Design", "Consulting", "Management", "Technical"],
    "Proficiency": [90, 85, 88, 92, 75]
}

fig = px.bar(skills_data, x="Category", y="Proficiency",
             title="Skills Proficiency",
             color="Proficiency",
             color_continuous_scale="Viridis")

st.plotly_chart(fig, use_container_width=True)

# Contact Section
st.markdown("---")
st.markdown("## Contact")
st.write("""
Feel free to reach out to me for opportunities or collaborations:
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn Profile]
- GitHub: [Your GitHub Profile]
""")

# Footer
st.markdown("---")
st.markdown("© 2024 Your Name. All rights reserved.") 