import streamlit as st
from lib.component import Component


def func(
    **props
):
    # props unpacking
    title = props['title']
    plot = props['plot']
    text = props['text']

    # props injection
    with st.expander(title):
        row_3 = st.container()
    with row_3:
        col1, col2 = st.columns(2)
        with col1:
            plot()
        with col2:
            st.markdown(text)


foldable_plot = Component('foldable_plot', func)
