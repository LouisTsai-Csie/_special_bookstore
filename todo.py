import streamlit as st

def app():
	st.header('特色書店地圖')
	st.metric('Total bookstore', 118)
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
    app()