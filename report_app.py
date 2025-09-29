import streamlit as st
from datetime import datetime
import base64

# Hàm hiển thị hình ảnh từ file cục bộ (giả lập, bạn thay bằng file thực tế)
def display_image(image_path, caption=""):
    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        st.image(f"data:image/png;base64,{encoded_image}", caption=caption, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"Hình ảnh '{image_path}' chưa có. Vui lòng thêm file để hiển thị.")

# Tiêu đề và thông tin cơ bản
st.title("📊 Báo cáo Chi tiết & Demo Dự án VoIP AI Agent")
st.subheader(f"Ngày cập nhật: {datetime.now().strftime('%H:%M %p, %d/%m/%Y')} (Giờ +07)")
st.write("Dự án xây dựng hệ thống AI Agent thông minh cho tổng đài VoIP, dựa trên thông tin đã cung cấp. Báo cáo này bao gồm tất cả các thành phần chi tiết, dashboard tiến độ, và demo trực quan hóa bằng hình ảnh.")

# Phần 1: Tổng quan Dự án
st.header("1. Tổng quan Dự án")
st.write("""
Dự án xây dựng một hệ thống AI Agent thông minh, có khả năng tiếp nhận và xử lý các cuộc gọi điện thoại qua nền tảng VoIP. Mục tiêu chính là cung cấp một trải nghiệm hội thoại tự nhiên, phản hồi nhanh với độ trễ thấp (dưới 800ms) và hỗ trợ đầy đủ tiếng Việt.

- **Nền tảng VoIP:** Asterisk 20 (VitalPBX) trên Debian 12.
- **Nền tảng AI:**
  - STT (Speech-to-Text): Google Cloud Speech-to-Text API (streaming).
  - NLP (Natural Language Processing): Mô hình Llama 4 Scout, chạy cục bộ.
  - TTS (Text-to-Speech): NVIDIA NeMo (FastPitch + BigVGAN), chạy trên một server riêng biệt.
- **Hạ tầng:** Server trang bị 8 GPU NVIDIA V100, hệ thống được container hóa hoàn toàn bằng Docker.
""")

# Phần 2: Kiến trúc Hệ thống
st.header("2. Kiến trúc Hệ thống")
st.write("""
Kiến trúc của dự án được thiết kế theo mô hình streaming-first, ưu tiên tốc độ và khả năng mở rộng.

- **Giao tiếp VoIP:** Sử dụng ARI (Asterisk REST Interface) thay vì AGI cũ. src/main.py kết nối tới Asterisk qua WebSocket để lắng nghe sự kiện cuộc gọi.
- **Xử lý cuộc gọi:** Mỗi cuộc gọi đến sẽ tạo một đối tượng CallHandler (src/core/call_handler.py) độc lập để quản lý toàn bộ luồng xử lý.
- **Luồng dữ liệu (Data Flow):**
  1. CallHandler trả lời cuộc gọi và yêu cầu Asterisk chuyển tiếp (fork) luồng âm thanh (RTP) đến một cổng UDP trên server.
  2. Âm thanh được stream real-time tới Google STT.
  3. Văn bản sau khi nhận dạng được gửi đến Llama 4 Scout để xử lý ý định.
  4. Phản hồi từ NLP được stream tới một NeMo TTS Server (FastAPI server độc lập) để tổng hợp giọng nói.
  5. Âm thanh được CallHandler phát lại cho người dùng, hỗ trợ ngắt lời (barge-in).
""")
display_image("architecture_diagram.png", caption="Sơ đồ kiến trúc hệ thống (giả lập, thay bằng hình thực tế nếu có)")

# Phần 3: Cấu trúc Thư mục và Thành phần Chính
st.header("3. Cấu trúc Thư mục và Thành phần Chính")
st.write("""
- **src/:** Chứa mã nguồn chính của ứng dụng.
  - main.py: Điểm khởi đầu (entrypoint), khởi tạo và quản lý kết nối ARI.
  - **core/:** Chứa các module xử lý lõi.
    - call_handler.py: Logic xử lý chính cho mỗi cuộc gọi.
    - stt_module.py: Tích hợp với Google STT.
    - nlp_module.py: Tích hợp với mô hình Llama 4.
    - tts_module.py: Client để giao tiếp với NeMo TTS Server.
- **tts_server/:** Ứng dụng FastAPI độc lập cho việc tổng hợp giọng nói.
  - server.py: Load model NeMo (FastPitch, BigVGAN) và cung cấp API /synthesize.
- **config/:** Chứa các file cấu hình cho ứng dụng, quy tắc chuẩn hóa dữ liệu.
- **data/:** Chứa dữ liệu training, knowledge base, và các file âm thanh mẫu.
- **docs/:** Chứa tài liệu dự án (PLAN.md, README.md).
- **docker-compose.yml:** Định nghĩa các service, network và volume cho môi trường container.
- **Dockerfile.app & Dockerfile.tts:** Định nghĩa môi trường build riêng biệt cho service chính (app) và service TTS để giải quyết xung đột thư viện.
""")
display_image("folder_structure.png", caption="Cấu trúc thư mục dự án (giả lập, thay bằng hình thực tế nếu có)")

# Phần 4: Kế hoạch và Lộ trình
st.header("4. Kế hoạch và Lộ trình")
st.write("""
Tài liệu PLAN.md vạch ra một lộ trình phát triển rõ ràng, chia thành các giai đoạn:
- **Giai đoạn 0:** Ổn định nền tảng, đảm bảo hệ thống có thể build và chạy thành công với Docker. (Hoàn tất 100%)
- **Giai đoạn 1:** Xây dựng lõi đối thoại, bao gồm chuẩn hóa đầu vào tiếng Việt, quản lý trạng thái hội thoại và xử lý ngắt lời. (Tiến độ 70%)
- **Giai đoạn 2:** Tối ưu độ trễ và tích hợp cơ sở dữ liệu vector (Vector DB) để tăng cường khả năng tra cứu tri thức. (Tiến độ 0%)
- **Giai đoạn 3:** Hoàn thiện hệ thống với các tính năng an toàn (che thông tin nhạy cảm), giám sát chi tiết và xây dựng bộ test chuyên biệt cho tiếng Việt. (Tiến độ 0%)
""")
progress = st.progress(70)  # Tiến độ tổng thể dự án
st.subheader("Metrics Kinh doanh Dự kiến")
col1, col2, col3 = st.columns(3)
col1.metric("Độ trễ Phản hồi", "<800ms", "Nhanh hơn 50% tiêu chuẩn")
col2.metric("Số cuộc gọi đồng thời", "100+", "Tiết kiệm 2-3 nhân viên/ca")
col3.metric("Tăng CSAT Dự kiến", "25%", "Giảm cúp máy 30%")

# Phần 5: Phụ thuộc (Dependencies)
st.header("5. Phụ thuộc (Dependencies)")
st.write("""
Dự án quản lý các phụ thuộc phức tạp bằng cách sử dụng hai môi trường Docker riêng biệt:
- **Service `app` (Python 3.11):** Chứa các thư viện cho NLP như unsloth, transformers, llama-cpp-python, và các client cho ARI, Google STT.
- **Service `tts_server` (Python 3.10):** Chứa nemo_toolkit[tts] và các thư viện liên quan để phục vụ model TTS.

Chi tiết các phiên bản thư viện được ghim chặt trong README.md và docs/PLAN.md để đảm bảo tính ổn định.
""")
st.table({
    "Service": ["app (Python 3.11)", "tts_server (Python 3.10)"],
    "Thư viện chính": ["unsloth, transformers, llama-cpp-python, ARI client, Google STT", "nemo_toolkit[tts], FastAPI"]
})

# Phần 6: Demo Sản phẩm (Trực quan hóa bằng hình ảnh)
st.header("6. Trải nghiệm Sản phẩm AI Agent (Trực quan hóa)")
st.write("Phần này minh họa các tính năng chính bằng hình ảnh và văn bản, thay vì âm thanh thật, để dễ dàng trình bày giá trị kinh doanh.")

# Demo 1: Trải nghiệm Giọng nói Thương Hiệu
st.subheader("A. Xem Trực quan Giọng nói AI")
st.write("Nhập câu để xem cách AI sẽ xử lý và hiển thị sóng âm giả lập.")
text_input = st.text_input("Gõ câu (ví dụ: Chào mừng quý khách!)", "Chào mừng quý khách đến với [Tên công ty]!")
if st.button("Xem Trực quan"):
    st.write(f"**Câu nhập:** {text_input}")
    st.write("**Sóng âm giả lập:** AI sẽ chuyển đổi thành giọng nói tự nhiên từ NeMo TTS.")
    display_image("waveform_high.py", caption="Sóng âm chất lượng cao từ NeMo TTS")
    st.success("Đây là cách AI tạo trải nghiệm chuyên nghiệp cho khách hàng!")

# Demo 2: So sánh Chất lượng
st.subheader("B. So sánh Chất lượng (Trực quan)")
col1, col2 = st.columns(2)
with col1:
    if st.button("Xem Giọng Robot Thường"):
        st.write("**Giọng robot tiêu chuẩn:** Chất lượng thấp, không tự nhiên.")
        display_image("waveform_low.png", caption="Sóng âm giả lập giọng robot")
with col2:
    if st.button("Xem Giọng AI Dự án"):
        st.write("**Giọng AI dự án:** Chất lượng cao, tự nhiên từ NeMo TTS.")
        display_image("waveform_high.py", caption="Sóng âm giả lập giọng AI chuyên nghiệp")

# Demo 3: Mô phỏng Cuộc gọi
st.subheader("C. Mô phỏng Cuộc gọi Thực tế")
if st.button("Xem Mô phỏng"):
    st.write("**Hội thoại (Trực quan):**")
    st.write("[AI]: A-lô, [Tên công ty] xin nghe. *(Sóng âm giả lập)*")
    display_image("waveform_high.py")
    st.write("[Khách hàng]: Chào em, anh muốn hỏi về tình trạng đơn hàng.")
    st.write("[AI]: Dạ vâng. Để kiểm tra, anh vui lòng cung cấp mã đơn hàng ạ. *(Sóng âm giả lập)*")
    display_image("waveform_high.py")
    st.write("--- Kết thúc mô phỏng ---")
    st.info("Lần sau: AI sẽ tra cứu mã đơn hàng tự động với hình ảnh minh họa chi tiết!")

# Phần 7: Kết luận và Ghi chú
st.header("7. Kết luận")
st.write("""
Báo cáo này đã tổng hợp đầy đủ tất cả các thành phần dựa trên thông tin dự án đã cung cấp. Dự án đang tiến triển tốt, với nền tảng vững chắc và tiềm năng kinh doanh cao (tiết kiệm chi phí nhân sự, tăng sự hài lòng khách hàng). Demo trực quan hóa giúp minh họa giá trị mà không cần âm thanh thực tế. Tiến độ sẽ được cập nhật định kỳ, với trọng tâm tiếp theo là tích hợp Vector DB và tối ưu hóa.
""")
st.write("**Hạ tầng:** 8 GPU NVIDIA V100 | **Công nghệ chính:** Asterisk, Llama 4 Scout, NeMo TTS, Docker.")

# Footer
st.write("---")
st.write("Báo cáo bởi [Tên bạn] | Liên hệ: [Email/SĐT] | Cập nhật trực tiếp trên Streamlit. Ngày báo cáo: 28/09/2025")