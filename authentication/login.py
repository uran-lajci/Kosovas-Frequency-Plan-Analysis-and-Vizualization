from utils.general_utils import *

import streamlit as st
import hashlib

def loginForm():
    is_login_successful = False
    st.title("Login Form")

    username_field = st.text_input("Username", key="username")
    password_field = st.text_input("Password", type="password", key="password")

    if not all([username_field, password_field]):
        st.error("Username and password are required fields.")
    else:
        file_path = 'authentication/usernames_and_passwords.txt'
        hashed_password = hashlib.sha256(("salt" + password_field).encode()).hexdigest()

        if checkWordInFile(file_path, username_field + ", Password:") and checkWordInFile(file_path, ": " + hashed_password):
            is_login_successful = True
        else:
            is_login_successful = False

    if is_login_successful:
        st.success("Welcome, {}!".format(username_field))
        return True
    else:
        st.error("Invalid username or password.")
        return False