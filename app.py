```python
import streamlit as st
import json
import os

# File để lưu trữ mật khẩu
PASSWORD_FILE = "passwords.json"

# Hàm load dữ liệu từ file
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

# Hàm lưu dữ liệu vào file
def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as f:
        json.dump(passwords, f, indent=4)

# Giao diện
st.set_page_config(page_title="Quản lý mật khẩu", page_icon="🔑")

st.title("🔑 Ứng dụng quản lý mật khẩu")
st.write("Lưu trữ mật khẩu an toàn ngay trên Streamlit + GitHub.")

# Load dữ liệu hiện tại
passwords = load_passwords()

# Tabs
tab1, tab2, tab3 = st.tabs(["➕ Thêm mật khẩu", "📖 Xem mật khẩu", "❌ Xóa mật khẩu"])

with tab1:
    st.subheader("➕ Thêm mật khẩu mới")
    site = st.text_input("Tên dịch vụ / website")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")

    if st.button("Lưu"):
        if site and username and password:
            passwords[site] = {"username": username, "password": password}
            save_passwords(passwords)
            st.success(f"✅ Đã lưu mật khẩu cho {site}")
        else:
            st.error("❌ Vui lòng nhập đủ thông tin.")

with tab2:
    st.subheader("📖 Danh sách mật khẩu đã lưu")
    if passwords:
        for site, info in passwords.items():
            with st.expander(site):
                st.write(f"👤 Tên đăng nhập: `{info['username']}`")
                st.write(f"🔑 Mật khẩu: `{info['password']}`")
    else:
        st.info("⚠️ Chưa có mật khẩu nào được lưu.")

with tab3:
    st.subheader("❌ Xóa mật khẩu")
    if passwords:
        site_to_delete = st.selectbox("Chọn dịch vụ cần xóa", list(passwords.keys()))
        if st.button("Xóa"):
            del passwords[site_to_delete]
            save_passwords(passwords)
            st.success(f"✅ Đã xóa mật khẩu của {site_to_delete}")
    else:
        st.info("⚠️ Không có mật khẩu nào để xóa.")
```
