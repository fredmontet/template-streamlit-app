import streamlit as st


def initialize(state):
    for k, v in state.items():
        if k not in st.session_state:
            st.session_state[k] = v
