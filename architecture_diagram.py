from graphviz import Digraph

# --- Config ---
FONT_NAME = "DejaVu Sans"
BG_COLOR = "#FFFFFF"
NODE_FILL = "#FFFFFF"
NODE_BORDER = "#495057"
EDGE_COLOR = "#343A40"
TEXT_COLOR = "#212529"
ACCENT_COLOR = "#0D6EFD"

# --- Graph ---
dot = Digraph(
    "VoIP AI Agent Architecture",
    graph_attr={
        "bgcolor": BG_COLOR,
        "rankdir": "TB",
        "splines": "ortho",
        "nodesep": "1.0",
        "ranksep": "1.0",
        "label": "Kiến trúc Luồng Dữ liệu HAPbx AI Agent",
        "fontsize": "22",
        "fontname": FONT_NAME,
        "dpi": "200",
    },
    node_attr={"fontname": FONT_NAME, "fontcolor": TEXT_COLOR, "style": "filled", "shape": "box", "color": NODE_BORDER},
    edge_attr={"color": EDGE_COLOR, "fontname": FONT_NAME, "fontsize": "10"},
)

# --- Nodes ---
dot.node("User", "Người Dùng", shape="ellipse")
dot.node("HAPbx", "HAPbx (Asterisk)", shape="cylinder")

with dot.subgraph(name="cluster_ai_core") as c:
    c.attr(label="Lõi Xử lý AI", style="rounded", color="#ADB5BD")
    c.node("CallHandler", "Call Handler", style="filled, rounded", fillcolor=ACCENT_COLOR, fontcolor="white")
    c.node("STT", "Google STT")
    c.node("NLP", "Llama 4")
    c.node("TTS", "NVIDIA NeMo")

# --- Edges ---
dot.edge("User", "HAPbx", label="1. Gọi điện")
dot.edge("HAPbx", "CallHandler", label="2. Gửi sự kiện\ncuộc gọi (ARI)")

# Luồng xử lý audio
dot.edge("CallHandler", "STT", label="3. Bắt đầu stream\nâm thanh")
dot.edge("STT", "NLP", label="4. Gửi văn bản\nđã nhận dạng")
dot.edge("NLP", "TTS", label="5. Gửi câu trả lời\ndưới dạng văn bản")
dot.edge("TTS", "CallHandler", label="6. Gửi lại âm thanh\nđã tổng hợp")

# Luồng phát lại
dot.edge("CallHandler", "HAPbx", label="7. Yêu cầu phát lại\nâm thanh cho người dùng")

# --- Render ---
dot.render("architecture_diagram", format="png", cleanup=True)
print("Đã vẽ lại architecture_diagram.png theo phong cách trực quan, chính xác.")