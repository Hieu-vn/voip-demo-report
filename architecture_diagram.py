

from graphviz import Digraph

# Pallete màu chuyên nghiệp
BG_COLOR = "#FFFFFF"
CLUSTER_BG_COLOR = "#F4F4F4"
NODE_COLOR = "#E0E0E0"
EDGE_COLOR = "#888888"
FONT_COLOR = "#333333"
FONT_NAME = "Arial"

# Khởi tạo đồ thị
dot = Digraph(
    "VoIP AI Agent Architecture",
    graph_attr={
        "bgcolor": BG_COLOR,
        "rankdir": "LR",
        "splines": "ortho",
        "label": "Kiến trúc Hệ thống VoIP AI Agent",
        "fontsize": "20",
        "fontname": FONT_NAME,
        "fontcolor": FONT_COLOR,
    },
    node_attr={"fontname": FONT_NAME, "fontcolor": FONT_COLOR, "style": "filled"},
    edge_attr={"color": EDGE_COLOR},
)

# Các thành phần bên ngoài
dot.node(
    "Asterisk",
    label="📞 Asterisk 20\n(VoIP Platform)",
    shape="cylinder",
    fillcolor=NODE_COLOR,
)
dot.node(
    "User",
    label="👤 Người dùng",
    shape="box",
    style="filled",
    fillcolor="#D1E8FF",
)

# Cụm xử lý lõi AI
with dot.subgraph(
    name="cluster_ai_core",
    graph_attr={
        "label": "✨ AI Core (Streaming)",
        "bgcolor": CLUSTER_BG_COLOR,
        "style": "rounded",
    },
) as c:
    c.node(
        "CallHandler",
        label="Call Handler",
        shape="box",
        fillcolor=NODE_COLOR,
    )
    c.node("STT", label="Google STT", shape="box", fillcolor=NODE_COLOR)
    c.node("NLP", label="Llama 4 Scout", shape="box", fillcolor=NODE_COLOR)
    c.node("TTS", label="NeMo TTS Server", shape="box", fillcolor=NODE_COLOR)

    # Luồng dữ liệu trong lõi AI
    c.edge("CallHandler", "STT")
    c.edge("STT", "NLP")
    c.edge("NLP", "TTS")


# Kết nối các thành phần
dot.edge("User", "Asterisk", label="Cuộc gọi đến")
dot.edge("Asterisk", "CallHandler", label="Fork RTP Stream")
dot.edge("TTS", "User", label="Phản hồi âm thanh")


# Lưu file
dot.render("architecture_diagram", format="png", cleanup=True)
print("Đã cập nhật và tạo architecture_diagram.png")
