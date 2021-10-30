import streamlit as st
from lib.component import Component


def func(
    **props
):
    # Props unpacking
    options = props['options']

    # Props injection
    st.sidebar.header('Sous-station')
    option = st.sidebar.selectbox('Sélectionnez une sous-station', options)

    return option

selector = Component('selector', func)


