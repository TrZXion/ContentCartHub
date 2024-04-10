import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

st.set_page_config(
    page_title="Dashboard",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="expanded",
)

show_pages(
    [
        Page("Home.py", "Home", "🏡", in_section=False),
        Page(
            "pages/Privacy_policy.py",
            "Privacy Policy",
            "🔏",
            in_section=False,
        ),
        Page("pages/TOS.py", "Terms Of Service", icon="💼", in_section=False),
        Page("pages/Support.py", "Contact", icon="📞", in_section=False),
        Page(
            "pages/Cancellation_and_Refund_policy.py",
            "Cancellation and Refund Policy",
            icon="💲",
            in_section=False,
        ),
        Page("pages/Contact_thanks.py", "Thank you", icon="💌"),
        Page("pages/About.py", "About", icon="🖼️", in_section=False),
    ]
)


hide_pages(["Thank you"])


st.title("HealthBridge: A Comprehensive  Solution")
st.write(
    "For Multimodal Disease Diagnosis, Patient Profiling, Report Generation, Appointment Scheduling, Telemedicine, and Automated Report Delivery via SMS and WhatsApp"
)
st.write(
    "Leveraging Machine Learning and Natural Language Processing for Enhanced Patient Care"
)
st.write("---")  # Adding a separator line


with st.container():
    st.write("---")
    st.header("My Project Status")
    image, text = st.columns((1, 3), gap="small")

    st.subheader(
        "Handling Authentication and Deployment using Google Cloud, Using Ngrok for Server Expose"
    )
    st.write(
        """
        Here we utilized Ngrok and Google Cloud for handling Authentication, deploying applications and exposing servers. Throughout this guide, you'll learn:
        * Deploying applications with Ngrok
        * Leveraging Google Cloud for deployment
        * Exposing servers securely
        * Integrating Google Authentication API Google OAuth2
        * Testing and verifying deployments
        """
    )
    st.markdown("[Watch the video >](https://your-youtube-video-url)")

st.subheader(
    "Utilizing Machine Learning, TensorFlow, OpenCV, and NLP in Medical Diagnosis Project with Langchain Integration"
)
st.write(
    """
    In this comprehensive project, I employed a fusion of cutting-edge technologies including Machine Learning (ML), TensorFlow, OpenCV for image processing, and Natural Language Processing (NLP), all integrated seamlessly with Langchain for secure data handling and processing. Here's an overview of how each component was utilized:

    * **Alzheimer's, Diabetes, Covid Detection:** Utilized ML algorithms to analyze medical data such as patient history, symptoms, and diagnostic tests to develop predictive models for detecting Alzheimer's disease, diabetes, and COVID-19 infections. TensorFlow was instrumental in training deep learning models for accurate diagnosis based on diverse datasets.

    * **Brain Tumor and Pneumonia Detection:** Leveraged TensorFlow and OpenCV for image processing tasks to detect brain tumors and pneumonia from medical imaging scans such as MRI and X-ray images. TensorFlow's neural networks were trained on annotated image datasets to classify abnormalities with high accuracy.

    * **Breast Cancer Detection:** Employed ML techniques to analyze mammography images and clinical data to detect signs of breast cancer. TensorFlow's convolutional neural networks (CNNs) were trained on mammography datasets, and OpenCV was used for preprocessing and feature extraction from images.

    * **Medication Review using NLP:** Integrated NLP algorithms to analyze patient reviews, medical records, and drug information to provide comprehensive medication reviews. NLP techniques such as sentiment analysis, named entity recognition (NER), and topic modeling were applied to extract insights and provide personalized medication recommendations.

    * **Langchain Integration:** Integrated Langchain into the project infrastructure to ensure secure, transparent, and decentralized handling of sensitive medical data. Langchain's blockchain-based platform facilitated secure data sharing, smart contract execution, and auditability while maintaining patient privacy and data integrity.

    This project showcases the potential of combining ML, TensorFlow, OpenCV, and NLP in medical diagnostics and treatment recommendation systems, with Langchain providing the necessary framework for secure and transparent data processing. For further details and resources, please refer to the project repository on [GitHub](https://github.com/yourusername/your-repo).
    """
)
st.markdown("[Watch the video >](https://your-youtube-video-url)")


st.subheader(
    "Utilizing Django, Python, Twilio, and WhatsApp API for Backend Development with Database Integration"
)
st.write(
    """
    In this project, I employed a combination of Django, Python, Twilio, and the WhatsApp API to develop a robust backend system with database integration, enabling seamless communication via WhatsApp. Here's an overview of how each component was utilized:

    * **Backend Development with Django:** Leveraged Django, a high-level Python web framework, to build the backend infrastructure. Django's built-in features such as ORM (Object-Relational Mapping), authentication system, and admin interface facilitated rapid development and maintenance of the backend server.

    * **Database Integration:** Integrated a database management system, such as PostgreSQL or MySQL, with Django to store and manage application data efficiently. Utilized Django's ORM to define database models and perform CRUD (Create, Read, Update, Delete) operations seamlessly.

    * **Twilio Integration:** Integrated Twilio, a cloud communications platform, to enable communication via SMS and WhatsApp. Utilized Twilio's API to send and receive messages, handle incoming requests, and automate workflows such as user authentication and notification alerts.

    * **WhatsApp API:** Leveraged the WhatsApp Business API to enable programmable interactions with users on the WhatsApp platform. Implemented features such as chatbots, notifications, and transactional messages to enhance user engagement and streamline communication processes.

    * **Python for Backend Logic:** Utilized Python scripting to implement backend logic, data processing, and business logic. Python's versatility and extensive libraries facilitated the development of custom functionalities tailored to project requirements.

    This project demonstrates the power of combining Django, Python, Twilio, and the WhatsApp API to build a scalable and feature-rich backend system with database integration. For further details and resources, please refer to the project repository on [GitHub](https://github.com/yourusername/your-repo).
    """
)
st.markdown("[Watch the video >](https://your-youtube-video-url)")
