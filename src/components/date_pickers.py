import streamlit as st
from lib.component import Component


def func(
    **props
):
    # Props unpacking
    default_start = props['default_start']
    default_stop = props['default_stop']

    # Props injection
    st.sidebar.header('Filtres')
    start = st.sidebar.date_input('Date de début',
                                  value=default_start,
                                  min_value=default_start,
                                  max_value=default_stop
                                  )
    stop = st.sidebar.date_input('Date de fin',
                                 value=default_stop,
                                 min_value=default_start,
                                 max_value=default_stop
                                 )

    return start, stop


date_pickers = Component('date_pickers', func)

