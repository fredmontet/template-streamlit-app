import streamlit as st
from lib.component import Component


def func(
    **props
):

    #############################################
    # Data Loading
    #############################################

    if 'data' in st.session_state:
        data = st.session_state.data
    else:
        st.warning("No loaded data")
        st.stop()

    #############################################
    # Data Processing
    #############################################

    # TODO

    #############################################
    # UI
    #############################################

    # TODO

sample_page = Component('sample_page', func)
