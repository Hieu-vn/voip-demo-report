from graphviz import Digraph

# Tạo đồ thị
dot = Digraph(comment="Kiến trúc Hệ thống VoIP AI Agent")

# Thêm các nút (thành phần)
dot.node("Asterisk", "Asterisk 20 (VitalPBX)")
dot.node("CallHandler", "CallHandler")
dot.node("STT", "Google STT")
dot.node("NLP", "Llama 4 Scout")
dot.node("TTS", "NeMo TTS Server")
dot.node("Output", "Phát lại âm thanh")

# Thêm cạnh (luồng dữ liệu)
dot.edge("Asterisk", "CallHandler")
dot.edge("CallHandler", "STT")
dot.edge("STT", "NLP")
dot.edge("NLP", "TTS")
dot.edge("TTS", "Output")

# Thiết lập kiểu dáng
dot.attr(rankdir="LR")  # Hiển thị từ trái sang phải
dot.attr("node", shape="box", style="filled", fillcolor="lightblue")
dot.attr(label="Streaming-first, độ trễ <800ms", fontname="Arial")

# Lưu file
dot.render("architecture_diagram", format="png", cleanup=True)
print("Đã tạo architecture_diagram.png")