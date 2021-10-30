import streamlit as st
from lib.i18n import translations as t


def login(func=None):
    st.sidebar.header(t['login_title'][st.session_state.lang])
    username = st.sidebar.text_input(t['username'][st.session_state.lang])
    password = st.sidebar.text_input(t['password'][st.session_state.lang], type="password")
    if st.sidebar.button(t['login_cta'][st.session_state.lang],
                         on_click=save_credentials(username, password)):
        if is_authorized(username, password) is False:
            st.sidebar.error(t['login_error'][st.session_state.lang])
        if func is not None:
            func()


def logout(func=None):
    if st.sidebar.button(t['logout_cta'][st.session_state.lang], on_click=reset_credentials):
        if func is not None:
            func()


def is_authorized(username, password):
    """Returns `True` if correct password is entered."""
    if username in st.secrets["users"] and password == st.secrets["users"][username]:
        return True
    else:
        return False


def save_credentials(username, password):
    st.session_state.username = username
    st.session_state.password = password


def reset_credentials():
    st.session_state.username = ''
    st.session_state.password = ''

