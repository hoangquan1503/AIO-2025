import streamlit as st
st.title("Ứng dụng quản lý công việc")
lst = dict()
name = st.text_input("Nhập tên công việc")
priority = st.slider("Chọn mức độ ưu tiên",1,5)
status = st.selectbox("Trạng thái công việc",["Đã làm","Chưa làm","Đang làm"])

if st.button(f"Thêm công việc "):
    lst["Tên"] = name
    lst["Mức độ ưu tiên"] = priority
    lst["Trạng thái"] = status
st.write(lst)
if st.button("Xóa công việc"):
    lst.clear()
