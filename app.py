import streamlit as st
import requests

def getAllBookstore() ->list:
    url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items) ->list:
    optionList = []
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList

def app():
    bookstoreList = getAllBookstore()
    countyOption = getCountyOption(bookstoreList)
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption) 
    district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
    app()