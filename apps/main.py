import streamlit as st
from scripts.utils.utils import checkDependencies

def main():
    st.set_page_config(page_title='Home')
    checkDependencies()
    st.title('News Tag Classifier')

if __name__ == '__main__':
    main()