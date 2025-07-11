import streamlit as st
from PIL import Image

# --- Page config ---
st.set_page_config(page_title="Shivam Jha | Portfolio", layout="wide")

# --- Load assets ---
img = Image.open("profile.jpg")

# --- Sidebar ---
with st.sidebar:
    st.image(img, width=180)
    st.title("Shivamkumar R. Jha")
    st.markdown("📍 Pune, Maharashtra, India")
    st.markdown("📞 +91 8605446824")
    st.markdown("✉️ [shivamjha182005@gmail.com](mailto:shivamjha182005@gmail.com)")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/shivamkumar-jha-590a47240/)")
    st.markdown("[🧑‍💻 GitHub](https://github.com/skishivam)")

    with open("resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        st.download_button(label="📄 Download Resume",
                           data=PDFbyte,
                           file_name="Shivam_Jha_Resume.pdf",
                           mime="application/pdf")

# --- Main section ---
st.title("👋 Welcome to My Portfolio")
st.markdown("""
I’m an aspiring **Data Scientist** with expertise in Python, SQL, and automation. I love solving real-world problems using data and AI.
""")

# Career Objective
st.header("🎯 Career Objective")
st.write("""
Dedicated and detail-oriented student pursuing BCA at SPPU. Passionate about data science, machine learning, and building efficient software systems.
""")

# Education
st.header("🎓 Education")
st.markdown("""
**Bachelor of Computer Applications (BCA)**  
SCOC College, Savitribai Phule Pune University (2022–2025)  
- Focus: Python, Java, SQL, Data Analysis, Web Development
""")

# Experience
st.header("🧑‍💻 Professional Experience")
st.markdown("""
**Desktop Support Intern – AlgoPlus, Pune**  
*Jan 2025 – Apr 2025*  
- Built internal automation tools using Python & Pandas  
- Supported ML model deployment for business decisions  
- 🏅 Awarded *Employee of the Month* – April 2025
""")

# Projects
st.header("🚀 Projects")

st.subheader("AI Resume Analyzer")
st.write("Python, Streamlit, OpenAI – Analyzed resumes using AI and gave job-based improvement tips.")

st.subheader("Portfolio Website")
st.write("React, Next.js, Tailwind – Professional website with resume, projects, and dark mode.")

st.subheader("User Auth System (Clerk)")
st.write("Next.js, Clerk – Google login, session management and protected routing.")

st.subheader("Cab Booking System")
st.write("Node.js, MySQL – Simulated real-time booking and trip data in a full-stack environment.")

st.subheader("Zomato Data Visualization Dashboard")
st.write("A Streamlit-based data visualization dashboard built from Zomato restaurant data. It shows insights like top cities, delivery support, rating heatmaps, and more.")
st.markdown("[🔗 GitHub Repo](https://github.com/skishivam/zomato-dashboard)")
st.markdown("[🚀 Live Demo](https://zomato-dashboard-6u93occjvjhzj5bn97vqd4.streamlit.app/)")

st.subheader("App Portfolio Website (Streamlit GUI)")
st.write("A sleek and responsive personal portfolio web app built using Streamlit. Features include interactive sidebar, resume download, and full project showcase.")
st.markdown("[🔗 GitHub Repo](https://github.com/skishivam/app-portfolio)")
st.markdown("[🚀 Live Demo](https://app-portfolio-huthmffsnatdes8xb5td3t.streamlit.app/)")

# Skills
st.header("📊 Technical Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Languages**: Python, Java, JS, C++")
    st.markdown("**Web**: HTML5, CSS3, React, Next.js")
with col2:
    st.markdown("**Databases**: MySQL, MongoDB, Firebase")
    st.markdown("**Tools**: Git, Postman, Prisma, Clerk")
with col3:
    st.markdown("**Deployment**: Vercel, Netlify, Streamlit")
    st.markdown("**Editors**: VS Code, Jupyter, Excel")

# Certifications & Awards
st.header("📚 Certifications & 🏆 Achievements")
st.markdown("""
- *Data Analytics & Data Science (DADS)* – IT Vedant  
- 🥇 *Employee of the Month*, AlgoPlus – April 2025
""")

# Footer
st.markdown("---")
st.header("📬 Get in Touch")
st.write("Email me at [shivamjha182005@gmail.com](mailto:shivamjha182005@gmail.com) or message me on LinkedIn!")
st.markdown("*Built with ❤️ using Streamlit*")
