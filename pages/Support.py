import streamlit as st
from st_pages import add_page_title, hide_pages

add_page_title()

hide_pages(["Thank you"])

st.warning("#### Report a bug 👾 or request a feature ⚡")

st.markdown("#### 📬 Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/el/rusehe" method="POST" enctype="multipart/form-data">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="text" name="_subject" placeholder="Subject">
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <input type="file" class="img_btn" name="Upload Image" accept="image/png, image/jpeg">
     <br>
     <input type="hidden" name="_next" value="https://dezoomcamp.streamlit.app/Thank%20you">
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

st.markdown("---")

st.write(
    """#### Reach out to us at: Judge Colony, Khagaul, Patna- 801105""",
    unsafe_allow_html=True,
)

st.markdown("Call us at +918789335057")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""


# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
