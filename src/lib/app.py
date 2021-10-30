import streamlit as st
from lib.page import Page
from lib.component import Component
from lib.authentication import is_authorized, login, logout


class App:

    def __init__(self):
        self.pages = {}

    def register_page(self, component: Component, **props):
        self.pages[component.name] = Page(component, **props)
        return self

    def run(self, authentication=True):

        def show_app():
            logout()
            selection = st.sidebar.selectbox('Menu',
                                             list(self.pages.keys()),
                                             index=1)
            self.pages[selection].run()

        def show_index():
            login()
            self.pages['Home'].run()

        if authentication:
            try:
                username = st.session_state['username']
                password = st.session_state['password']
                if is_authorized(username, password):
                    show_app()
                else:
                    show_index()
            except KeyError:
                show_index()
        else:
            show_app()






