import streamlit as st
view=[100,200,100,200]
show_raw=st.checkbox('show raw data')
if shwo_raw == True:

    st.write(' # raw data') # #을 붙이면 크기와 굵기 변화
    view
st.write('#table')
st.table(view) # 테이블
st.write('# bar graph')
st.bar_chart(view)