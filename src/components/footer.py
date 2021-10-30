import streamlit as st
from lib.component import Component
from version import version


def func(
    **props
):
    st.write(f'''
    ---
    v{version} — Copyright © 2021 HEIA-FR 
    ''')

footer = Component('footer', func)
