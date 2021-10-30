import streamlit as st
from lib.component import Component


def func(
    **props
):
    # Introduction Image
    st.image('src/use/assets/dhn.png', width=80)
    st.write('---')


header = Component('header', func)
