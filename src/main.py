import streamlit as st

from lib.app import App
from lib.component import Component

from components.footer import footer

from pages.index.ui import index
from pages.sample_page.ui import sample_page

#############################################
# Config
#############################################

st.set_page_config(layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'lang' not in st.session_state:
    st.session_state['lang'] = 'en'

#############################################
# Data
#############################################

DATA = f'src/use/tmp/data'

#############################################
# Pages
#############################################

index_page = Component('Home')\
    .add_child(index)\
    .add_child(footer)

loader_page = Component('Sample page') \
    .add_child(sample_page) \
    .add_child(footer)

#############################################
# App
#############################################

app = App() \
    .register_page(index_page) \
    .register_page(loader_page)

app.run(authentication=True)
