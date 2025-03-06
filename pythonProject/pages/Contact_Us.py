import streamlit as st
from send_email import send_email

st.header('Get in touch with me!')

with st.form(key = "email_forms"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent successfully! I will be in touch soon :)")

