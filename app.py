import streamlit as st
import requests

def getAllBookstore() ->list:
    url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def app():
    bookstoreList = getAllBookstore()
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
    district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
    app()