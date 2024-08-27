import streamlit as st

# Set page title
st.set_page_config(page_title="UrgentProjects")
st.markdown('<h1 style="text-align: center;">UrgentProjects</h1>', unsafe_allow_html=True)

# Minimal Description
st.write("Explore the services we offer to help students and professionals succeed in their academic and career journeys.")

# Tabs for different bundles
tab1, tab2, tab3 = st.tabs(["Project Help Bundle", "Job Prep Bundle", "Coding Support Bundle"])

with tab1:
    st.header("Project Help Bundle")
    st.write("For students working on major academic projects, like final year projects or theses.")
    st.image("projecthelp.jpeg", use_column_width=True)  # Replace with your image URL or local path
    st.write("This bundle offers comprehensive support to help students create standout academic projects from concept to completion.")
    st.markdown("""
    1. **Project Prototype Design**  
       Get expert help in turning your project ideas into functional prototypes.

    2. **Custom Project Development**  
       Receive tailored assistance in developing your project with technical precision.

    3. **Technical Project Documentation Writing**  
       Ensure your project documentation meets the highest academic standards.

    4. **Project Report Creation**  
       Create detailed and polished project reports that impress evaluators.

    5. **Thesis Writing Support**  
       Get guidance on crafting a well-structured, compelling thesis.
    """)
    st.markdown('<a href="https://wa.link/mdj68a" target="_blank"><button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #008000; border: none; border-radius: 5px;">WhatsApp</button></a>', unsafe_allow_html=True)

with tab2:
    st.header("Job Prep Bundle")
    st.write("For recent graduates or final-year students preparing to enter the job market.")
    st.image("jobprep.jpg", use_column_width=True)  # Replace with your image URL or local path
    st.write("This bundle provides all the tools needed to create a professional brand and stand out in the competitive job market.")
    st.markdown("""
    1. **Resume Building**  
       Craft a resume that highlights your strengths and catches employers' attention.

    2. **Cover Letter Writing**  
       Write persuasive cover letters tailored to specific job opportunities.

    3. **Portfolio Development**  
       Showcase your skills and projects in a visually appealing portfolio.

    4. **LinkedIn Profile Optimization**  
       Enhance your LinkedIn profile to attract recruiters and networking opportunities.

    5. **Certification Guidance**  
       Get advice on which certifications can boost your career prospects.
    """)
    st.markdown('<a href="https://wa.link/mdj68a" target="_blank"><button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #008000; border: none; border-radius: 5px;">WhatsApp</button></a>', unsafe_allow_html=True)

with tab3:
    st.header("Coding Support Bundle")
    st.write("For students and graduates focused on enhancing their technical skills and visibility in the tech community.")
    st.image("codingsupport.jpg", use_column_width=True)  # Replace with your image URL or local path
    st.write("This bundle is designed to help students refine their technical work and build a strong online presence that showcases their expertise.")
    st.markdown("""
    1. **Code Review and Optimization**  
       Improve the quality and efficiency of your code with expert reviews.

    2. **Project Idea Consultation**  
       Brainstorm and refine project ideas to ensure they stand out.

    3. **GitHub Portfolio Management**  
       Organize and present your coding projects effectively on GitHub.

    4. **Technical Blog Writing**  
       Share your expertise with the community through well-crafted technical blogs.

    5. **Research Paper Assistance**  
       Get support in writing and publishing research papers in tech-related fields.
    """)
    st.markdown('<a href="https://wa.link/mdj68a" target="_blank"><button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #008000; border: none; border-radius: 5px;">WhatsApp</button></a>', unsafe_allow_html=True)

# Footer
st.write("---")
st.markdown('<p style="text-align: center;">Copyright © 2024 UrgentProjects. All rights reserved.</p>', unsafe_allow_html=True)

