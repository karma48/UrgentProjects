import streamlit as st

# Set page title
st.set_page_config(page_title="UrgentProjects")
st.markdown('<h1 style="text-align: center;">UrgentProjects Services</h1>', unsafe_allow_html=True)

# Minimal Description
st.write("Explore the services we offer to help students and professionals succeed in their academic and career journeys.")

# Tabs for different bundles
tab1, tab2, tab3 = st.tabs(["Project Help Bundle", "Job Prep Bundle", "Coding Support Bundle"])

with tab1:
    st.header("Project Help Bundle")
    st.image("projecthelp.jpeg", use_column_width=True)  # Replace with your image URL or local path
    st.write("Comprehensive support for students working on major academic projects, from concept to completion.")
    st.markdown("""
    - **Project Prototype Design**
    - **Custom Project Development**
    - **Technical Project Documentation Writing**
    - **Project Report Creation**
    - **Thesis Writing Support**
    """)
    st.markdown('<a href="https://wa.link/mdj68a" target="_blank"><button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #008000; border: none; border-radius: 5px;">WhatsApp</button></a>', unsafe_allow_html=True)

with tab2:
    st.header("Job Prep Bundle")
    st.image("jobprep.jpg", use_column_width=True)  # Replace with your image URL or local path
    st.write("Tools and guidance for recent graduates or final-year students preparing to enter the job market.")
    st.markdown("""
    - **Resume Building**
    - **Cover Letter Writing**
    - **Portfolio Development**
    - **LinkedIn Profile Optimization**
    - **Certification Guidance**
    """)
    st.markdown('<a href="https://wa.link/mdj68a" target="_blank"><button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #008000; border: none; border-radius: 5px;">WhatsApp</button></a>', unsafe_allow_html=True)

with tab3:
    st.header("Coding Support Bundle")
    st.image("codingsupport.jpg", use_column_width=True)  # Replace with your image URL or local path
    st.write("Support for enhancing technical skills and building a strong online presence in the tech community.")
    st.markdown("""
    - **Code Review and Optimization**
    - **Project Idea Consultation**
    - **GitHub Portfolio Management**
    - **Technical Blog Writing**
    - **Research Paper Assistance**
    """)
    st.markdown('<a href="https://wa.link/mdj68a" target="_blank"><button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #008000; border: none; border-radius: 5px;">WhatsApp</button></a>', unsafe_allow_html=True)

# Footer
st.write("---")
st.markdown('<p style="text-align: center;">© 2024 UrgentProjects - Empowering Your Success</p>', unsafe_allow_html=True)

