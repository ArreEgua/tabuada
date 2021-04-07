import streamlit as st
import revisao
import treinar

PAGES = {
    "Treinar": treinar,
    "Revisão": revisao

}

st.sidebar.title('Menu')
selection = st.sidebar.radio('', list(PAGES.keys()))
page = PAGES[selection]
page.app()
