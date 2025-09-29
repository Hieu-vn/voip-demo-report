
import streamlit as st
from datetime import datetime
import base64

# --- CONFIG ---
REPORTER_NAME = "Phạm Khắc Hiếu"
REPORTER_PHONE = "0977597088"
REPORTER_EMAIL = "phamkhachieu19@gmail.com"
COMPANY_NAME = "HPA Direct" # Thay đổi nếu cần

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Báo cáo Dự án VoIP AI Agent",
    page_icon="🤖",
    layout="wide"
)

# --- FUNCTIONS ---
def display_image(image_path, caption=""):
    """Hàm hiển thị hình ảnh từ file cục bộ."""
    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        st.image(f"data:image/png;base64,{encoded_image}", caption=caption, use_container_width=True)
    except FileNotFoundError:
        st.error(f"Lỗi: Không tìm thấy file hình ảnh '{image_path}'. Vui lòng đảm bảo file tồn tại.")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Thông tin Báo cáo")
    st.markdown(f"**Người thực hiện:**\n{REPORTER_NAME}")
    st.markdown(f"**Liên hệ:**\n📞 {REPORTER_PHONE}\n📧 {REPORTER_EMAIL}")
    st.markdown("---")
    st.info(f"**Ngày cập nhật:**\n{datetime.now().strftime('%H:%M, %d/%m/%Y')}")
    st.markdown("---")
    st.header("Về dự án")
    st.caption("Dự án xây dựng AI Agent thông minh cho tổng đài VoIP, tập trung vào trải nghiệm hội thoại tự nhiên và hiệu quả kinh doanh.")

# --- MAIN CONTENT ---

# 1. TIÊU ĐỀ VÀ TỔNG QUAN
st.title("📊 Báo cáo & Demo: Dự án VoIP AI Agent")
st.markdown(f"### Báo cáo được thực hiện bởi **{REPORTER_NAME}**")
st.markdown("---")

st.header("1. 🚀 Tổng quan: AI thay đổi cuộc chơi cho tổng đài")
st.write(f"""
Dự án này không chỉ xây dựng một tổng đài tự động, mà là một **Trợ lý AI Thông minh** thực thụ cho {COMPANY_NAME}. 
Mục tiêu là tạo ra một trải nghiệm khách hàng xuất sắc thông qua các cuộc hội thoại tự nhiên, đồng thời tối ưu hóa chi phí vận hành. 
AI Agent có khả năng nghe, hiểu và phản hồi tiếng Việt với độ trễ cực thấp, hoạt động 24/7 mà không cần can thiệp.
""")

# 2. LỢI ÍCH KINH DOANH
st.header("2. 💰 Lợi ích Kinh doanh Cốt lõi")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Tiết kiệm Chi phí")
    st.markdown("- 🤖 **Tự động hóa 80%** cuộc gọi thông thường.")
    st.markdown("- 📉 **Giảm 2-3 nhân sự** trực tổng đài mỗi ca.")
    st.markdown("- ⚡ Hoạt động **24/7** không tốn thêm chi phí ngoài giờ.")
with col2:
    st.subheader("Tăng trưởng Doanh thu")
    st.markdown("- 📞 **Không bao giờ bỏ lỡ** cuộc gọi của khách hàng tiềm năng.")
    st.markdown("- 📈 Tăng cơ hội **bán hàng và tư vấn** tự động.")
    st.markdown("- ⏱️ Phản hồi tức thì, giữ chân khách hàng hiệu quả.")
with col3:
    st.subheader("Nâng cao Trải nghiệm")
    st.markdown("- 😊 **CSAT dự kiến tăng 25%** nhờ phản hồi nhanh và chính xác.")
    st.markdown("- 🗣️ Giọng nói tự nhiên, chuyên nghiệp, mang đậm dấu ấn thương hiệu.")
    st.markdown("- 🚫 **Giảm 30% tỷ lệ cúp máy** do phải chờ đợi lâu.")

st.markdown("---")

# 3. KIẾN TRÚC HỆ THỐNG
st.header("3. 🏗️ Kiến trúc Hệ thống: Nền tảng cho sự ổn định")
st.write("""
Để dễ hình dung, hãy tưởng tượng hệ thống của chúng ta như một bộ não kỹ thuật số hoạt động theo thời gian thực:
- **Tai (Nghe):** Khi có cuộc gọi, hệ thống "nghe" luồng âm thanh ngay lập tức bằng công nghệ kết nối mới nhất của Asterisk.
- **Não (Hiểu & Suy nghĩ):** Luồng âm thanh được chuyển thành văn bản (Google STT) và đưa vào mô hình ngôn ngữ Llama 4 để "hiểu" ý định của khách hàng.
- **Miệng (Nói):** Sau khi có câu trả lời, hệ thống dùng công nghệ NeMo của NVIDIA để chuyển văn bản thành giọng nói tự nhiên và phát lại cho khách hàng.

Toàn bộ quá trình này diễn ra mượt mà với độ trễ dưới 800ms, đảm bảo cuộc hội thoại không bị gián đoạn.
""")
display_image("architecture_diagram.png", caption="Sơ đồ minh họa luồng xử lý của AI Agent")
st.markdown("---")

# 4. LỘ TRÌNH DỰ ÁN
st.header("4. 🗺️ Lộ trình Dự án (Trực quan)")
st.write("Dự án được chia thành các giai đoạn rõ ràng để đảm bảo tiến độ và chất lượng.")

# Giai đoạn 0
st.write("##### Giai đoạn 0: Nền tảng & Môi trường")
st.progress(100)
st.markdown("✅ **Trạng thái:** Hoàn tất. Hệ thống đã có thể build và chạy ổn định.")

# Giai đoạn 1
st.write("##### Giai đoạn 1: Xây dựng Lõi hội thoại")
st.progress(70)
st.markdown("⏳ **Trạng thái:** Đang thực hiện. Đã hoàn thành xử lý ngắt lời, đang tinh chỉnh chuẩn hóa tiếng Việt.")

# Giai đoạn 2
st.write("##### Giai đoạn 2: Tối ưu & Tăng cường Tri thức")
st.progress(0)
st.markdown("⏸️ **Trạng thái:** Chưa bắt đầu. Sẽ tích hợp VectorDB để AI có 'trí nhớ' và tra cứu thông tin sản phẩm.")

st.markdown("---")

# 5. DEMO TRẢI NGHIỆM
st.header("5. ✨ Demo Trải nghiệm Giọng nói (Trực quan)")
st.write("Phần này minh họa sự khác biệt về chất lượng giọng nói, yếu tố then chốt tạo nên trải nghiệm chuyên nghiệp.")

st.subheader("So sánh Chất lượng Giọng nói")
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("#### Giọng Robot Tiêu chuẩn")
    st.caption("Chất lượng thấp, thiếu tự nhiên, thường gặp ở các tổng đài cũ.")
    display_image("waveform_low.png")

with col_b:
    st.markdown("#### Giọng AI của Dự án")
    st.caption("Chất lượng cao, tự nhiên, truyền cảm nhờ công nghệ NVIDIA NeMo.")
    display_image("waveform_high.png")

st.info("💡 **Insight:** Giọng nói chất lượng cao không chỉ giúp khách hàng dễ nghe hơn mà còn nâng cao đáng kể uy tín và hình ảnh thương hiệu của công ty.")
st.markdown("---")

# 6. THÔNG TIN KỸ THUẬT & KẾT LUẬN
st.header("6. 🔧 Thông tin Kỹ thuật & Kết luận")

with st.expander("Xem chi tiết về Công nghệ & Cấu trúc Thư mục"):
    st.write("""
    **Công nghệ sử dụng:**
    - **VoIP:** HAPbx (Nền tảng Asterisk 20)
    - **Nền tảng AI:** Google STT, Llama 4 Scout, NVIDIA NeMo (FastPitch + BigVGAN)
    - **Hạ tầng:** Docker, 8x NVIDIA V100

    **Cấu trúc thư mục:** Dự án được tổ chức một cách khoa học, tách biệt rõ ràng giữa các thành phần để dễ dàng bảo trì và nâng cấp.
    """)
    display_image("folder_structure.png", caption="Cấu trúc thư mục được tổ chức chuyên nghiệp")


st.subheader("Kết luận & Đề xuất")


st.success(f"""
**Báo cáo bởi:** {REPORTER_NAME}

Dự án VoIP AI Agent đã hoàn thành các giai đoạn nền tảng quan trọng và đang đi đúng lộ trình. Các thử nghiệm ban đầu cho thấy tiềm năng to lớn trong việc **cải thiện hiệu suất kinh doanh** và **mang lại trải nghiệm vượt trội** cho khách hàng.

**Đề xuất các bước tiếp theo:**
1.  Hoàn thiện Giai đoạn 1 trong tuần tới.
2.  Tổ chức một buổi demo "live" với kịch bản thực tế.
3.  Phê duyệt kế hoạch cho Giai đoạn 2 (Tích hợp VectorDB).

Xin cảm ơn sự quan tâm và chỉ đạo của ban lãnh đạo.
""")
