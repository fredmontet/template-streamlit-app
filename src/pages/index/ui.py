import streamlit as st
from lib.component import Component


def func(
        **props
):
    #############################################
    # Data Processing
    #############################################

    # TODO

    #############################################
    # UI
    #############################################

    # Description
    row_1 = st.container()
    with row_1:
        col1, col2 = st.columns(2)
        with col1:
            st.title('Streamlit App Template')
            st.subheader('All you need to start fast')
            st.write('''
                If you want to make a data app even faster than with Streamlit
                itself, go with this template. It gives you : 
                
                  - a React inspired structure
                  - some basic components
                  - global state management
                  - authentication that can be enabled with a boolean
 
                Have a good day!                     
            ''')
        with col2:
            st.empty()


index = Component('Home', func)
