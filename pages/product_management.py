import streamlit as st

st.set_page_config(
    page_title="Product Management Projects - Cherry Mathew Roy",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .project-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 20px;
    }
    .project-title {
        color: #1f77b4;
        font-size: 24px;
        font-weight: bold;
    }
    .project-subtitle {
        color: #666;
        font-size: 16px;
        font-style: italic;
    }
    .achievement {
        color: #2e7d32;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("Product Management Projects")
st.markdown("---")

# DynamEye Project
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.markdown('<div class="project-title">DynamEye: AI-Powered Navigation Glasses for the Visually Impaired</div>', unsafe_allow_html=True)
st.markdown('<div class="project-subtitle">Product Development & Manager | Dec 2024 - Present</div>', unsafe_allow_html=True)
st.write("""
**Project Overview:**
Designing an innovative AI-powered assistive device to improve mobility and independence for individuals with Retinitis Pigmentosa.

**Key Responsibilities:**
- Leading product development and user testing initiatives
- Developing go-to-market strategy for affordable and accessible smart glasses
- Collaborating with industry experts on technical integration

**Technical Integration:**
- Dynamic zoom and autofocus capabilities
- Real-time navigation through reinforcement learning
- AI-powered object recognition and path planning

**Impact:**
- Enhanced mobility for visually impaired users
- Improved independence through AI assistance
- Accessible technology solution for a critical need
""")
st.markdown('</div>', unsafe_allow_html=True)

# TerrAI Project
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.markdown('<div class="project-title">TerrAI: Semantic Command Line Interface Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="project-subtitle">Product Design & Manager | Nov 2024 - Dec 2024</div>', unsafe_allow_html=True)
st.write("""
**Project Overview:**
End-to-end product design of an NLP-based CLI tool designed to simplify system monitoring through natural language processing.

**Key Achievements:**
- Defined product requirements and success metrics
- Conducted user research with 50+ system administrators
- Achieved 93% accuracy in command interpretation
- Implemented user feedback loop
- Added 15 new features based on customer needs

**Technical Implementation:**
- Natural Language Processing
- System monitoring integration
- Command interpretation engine
- User feedback system
""")
st.markdown('</div>', unsafe_allow_html=True)

# Cre8ive Nudge Project
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.markdown('<div class="project-title">Cre8ive Nudge: Digital Product & Design Consultancy</div>', unsafe_allow_html=True)
st.markdown('<div class="project-subtitle">Founder, Product Designer & Manager | Apr 2023 - Sep 2024</div>', unsafe_allow_html=True)
st.write("""
**Project Overview:**
Led product development for web and mobile apps, focusing on user engagement and business growth.

**Key Achievements:**
- Drove 300% increase in client conversions within six months
- Achieved 95% stakeholder satisfaction rate
- Generated INR 1.55 Million projected revenue growth till 2026
- Increased website traffic by 35%
- Boosted engagement by 40%

**Responsibilities:**
- Product development and roadmap definition
- Competitor analysis and market research
- UX research and usability testing
- Prototype refinement and optimization
- Brand strategy and marketing
- Design system implementation
- Content architecture
""")
st.markdown('</div>', unsafe_allow_html=True)

# Back to Home button
st.markdown("---")
if st.button("Back to Home"):
    st.switch_page("app.py") 