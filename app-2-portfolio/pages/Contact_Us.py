import streamlit as st
from send_email import send_email

st.header("Contact")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message here!")
    message = f"""\
Subject: Email from {user_email}

From: {user_email}
{user_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent successfully!")