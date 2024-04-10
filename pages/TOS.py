import base64
import streamlit as st
import streamlit.components.v1 as components
from st_pages import add_page_title, hide_pages

add_page_title()

hide_pages(["Thank you"])

st.subheader("Please read on our Terms of Service! 🙌🏻")

with open("pages/TOS.html", "r") as f:
    html_content = f.read().encode("utf-8")

# Encode HTML content with base64
encoded_html = base64.b64encode(html_content).decode()

# Display HTML content
components.iframe(f"data:text/html;base64,{encoded_html}", width=900, height=12600)
