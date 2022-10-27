def getBookstoreInfo(items):
	expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        # 用 st.write 呈現書店的 Introduction
        expander.subheader('Address')
        # 用 st.write 呈現書店的 Address
        expander.subheader('Open Time')
        # 用 st.write 呈現書店的 Open Time
	expander.subheader('Email')
	# 用 st.write 呈現書店的 Email
        # 將該 expander 放到 expanderList 中
    return expanderList

def app():
	bookstoreList = getAllBookstore()

	countyOption = getCountyOption(bookstoreList)
	
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	districtOption = getDistrictOption(bookstoreList, county)
	district = st.multiselect('請選擇區域', districtOption) 
	
	specificBookstore = getSpecificBookstore(bookstoreList, county, district)
	num = len(specificBookstore)
	st.write(f'總共有{num}項結果', num)
	
	# 呼叫 getBookstoreInfo 並將回傳值賦值給變數 bookstoreInfo
