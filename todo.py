<<<<<<< HEAD
import streamlit as st

def app():
	st.header('特色書店地圖')
	st.metric('Total bookstore', 118)
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
    app()
=======
def getAllBookstore() ->list:
	url = '' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response = request.get(url, headers=headers)
	# 將 response 轉換成 json 格式
	# 回傳值

def app():
	# 呼叫 getAllBookstore 函式並將其賦值給變數 bookstoreList
    st.header('特色書店地圖')
	st.metric('Total bookstore', 118) # 將 118 替換成書店的數量
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])
>>>>>>> ab6c1290cff07c264c4be616302a25e66c92b0e9
