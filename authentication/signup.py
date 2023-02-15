from utils.general_utils import *

import streamlit as st
import hashlib

def getSignupForm():
    st.title("Signup Form")
    username_field = st.text_input("Username", key="rusername")
    password_field = st.text_input("Password", type="password", key="rpassword")
    password_confirm_field = st.text_input("Confirm Password", type="password", key="password_confirm")
    
    if not all([username_field,password_field,password_confirm_field]):
        st.error("All fields are required.")
    elif password_field != password_confirm_field:
        st.error("Passwords do not match.")
    else:
        file_path = 'authentication/usernames_and_passwords.txt'

        if checkWordInFile(file_path, username_field) and checkWordInFile(file_path, password_field):
            is_signup_successful = False
        else:
            is_signup_successful = True

        if is_signup_successful:
            with open("authentication/usernames_and_passwords.txt", "a") as f:
                hashed_password = hashlib.sha256(("salt" + password_field).encode()).hexdigest()
                f.write("\nUsername: {}, Password: {}".format(username_field, hashed_password))
            st.success("Account created for {}!".format(username_field))
        else:
            st.error("Sorry, there was a problem creating the account.")