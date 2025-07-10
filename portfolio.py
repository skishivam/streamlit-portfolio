
import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Shivamkumar R. Jha | Portfolio", layout="wide")

# Load assets
img = Image.open("profile.jpg")

# Sidebar with links
st.sidebar.image(img, width=150)
st.sidebar.title("Shivamkumar R. Jha")
st.sidebar.markdown("📍 Pune, Maharashtra, India")
st.sidebar.markdown("+91 8605446824")
st.sidebar.markdown("[✉️ Email](mailto:shivamjha182005@gmail.com)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/shivamkumar-jha-590a47240/) | [GitHub](https://github.com/skishivam)")
st.sidebar.download_button("📄 Download Resume", "C:\Projects\Streamlit portfolio\shivamkumar-Ramanand--jha-FlowCV-Resume-20250708 (1).pdf", mime="application/pdf")

# Main header
st.title("👋 Welcome to My Portfolio")
st.markdown("""
**Aspiring Data Scientist** with strong foundations in programming, data analysis, and web development. Passionate about creating AI, ML, and automation solutions.
""")

# Career Objective
st.header("🎯 Career Objective")
st.write("""
Aspiring Data Scientist skilled in Python, Java, SQL, and web development. Eager to tackle real-world challenges using AI, ML, and automation.
""")

# Education
st.header("🎓 Education")
st.markdown("""
**Bachelor of Computer Applications (BCA)**  
SCOC College, Savitribai Phule Pune University (August 2022 – June 2025), Pune, India  
Core subjects: Python, Java, SQL, Data Analysis, Web Development.
""")

# Experience
st.header("🧑‍💻 Professional Experience")
st.markdown("""
**Desktop Support Intern**, AlgoPlus, Pune (Jan 2025 – Apr 2025)  
- Built data workflows and automation tools using Python and Pandas  
- Developed ML models to optimize business operations  
- Awarded *Employee of the Month – April 2025*
""")

# Projects
st.header("🚀 Projects")
st.markdown("""
**AI Resume Analyzer**  
- Tech: Python, Streamlit, OpenAI API  
- Description: Scans resumes and gives keyword & clarity suggestions.

**Portfolio Website**  
- Tech: React.js, Next.js, Tailwind CSS, Vercel  
- Features: Dark mode, project mockups, contact form.

**User Authentication with Clerk Auth**  
- Tech: Next.js, Tailwind, Clerk  
- Description: Secure signup/login flow with Google OAuth.

**Cab Booking System**  
- Tech: Node.js, Express.js, MySQL  
- Description: Full-stack app simulating ride-booking with DB integration.
""")

# Skills
st.header("📊 Technical Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("- **Languages:** Python, Java, JavaScript, C++")
    st.markdown("- **Web:** HTML5, CSS3, React.js, Next.js, Tailwind CSS")
with col2:
    st.markdown("- **Databases:** MySQL, MongoDB, Firebase")
    st.markdown("- **Tools:** Express.js, Prisma, Clerk, Git, Postman")
with col3:
    st.markdown("- **Deployment:** Vercel, Netlify, Streamlit")
    st.markdown("- **IDE:** VS Code, Excel")

# Certifications & Achievements
st.header("📚 Certifications & 🏆 Achievements")
st.markdown("""
- *Data Analytics & Data Science (DADS)* – IT Vedant, Pune  
- 🥇 *Employee of the Month*, AlgoPlus – April 2025
""")

# Footer & Contact
st.markdown("---")
st.markdown("📫 Feel free to reach out via email or LinkedIn!")
st.markdown("Built with ❤️ using Streamlit")
