from graphviz import Digraph

# --- Config ---
FONT_NAME = "DejaVu Sans"
BG_COLOR = "#FFFFFF"
NODE_FILL = "#F8F9FA"
NODE_BORDER = "#DEE2E6"
EDGE_COLOR = "#495057"
TEXT_COLOR = "#212529"
ACCENT_COLOR = "#0D6EFD"

# --- Graph ---
dot = Digraph(
    "VoIP AI Agent Architecture",
    graph_attr={
        "bgcolor": BG_COLOR,
        "rankdir": "TB",
        "splines": "curved",
        "nodesep": "1.5",
        "ranksep": "1.5",
        "label": "Luồng Hoạt Động của HAPbx AI Agent",
        "fontsize": "28",
        "fontname": FONT_NAME,
        "dpi": "200",
        "size": "12,12!",
    },
    node_attr={"fontname": FONT_NAME, "fontcolor": TEXT_COLOR, "style": "filled, rounded", "shape": "box"},
    edge_attr={"color": EDGE_COLOR, "fontname": FONT_NAME, "fontsize": "11"},
)

# --- Nodes ---
dot.node("User", "Người Dùng Cuối", fillcolor=NODE_FILL, color=NODE_BORDER)
dot.node("HAPbx", "HAPbx\n(Asterisk Platform)", shape="cylinder", fillcolor=NODE_FILL, color=NODE_BORDER)

with dot.subgraph(name="cluster_ai_core") as c:
    c.attr(label="Lõi Xử lý AI", style="rounded", color=NODE_BORDER)
    c.node("CallHandler", "Call Handler", fillcolor=ACCENT_COLOR, fontcolor="white")
    c.node("STT", "Speech-to-Text\n(Google)", fillcolor=NODE_FILL, color=NODE_BORDER)
    c.node("NLP", "Natural Language\nProcessing (Llama 4)", fillcolor=NODE_FILL, color=NODE_BORDER)
    c.node("TTS", "Text-to-Speech\n(NVIDIA NeMo)", fillcolor=NODE_FILL, color=NODE_BORDER)
    c.edge("CallHandler", "STT")
    c.edge("STT", "NLP")
    c.edge("NLP", "TTS")

# --- Edges ---
dot.edge("User", "HAPbx", label="1. Thực hiện\ncuộc gọi")
dot.edge("HAPbx", "CallHandler", label="2. Luồng âm thanh\nđược chuyển tiếp (RTP)")
dot.edge("TTS", "HAPbx", label="3. Âm thanh tổng hợp\nđược gửi lại")
dot.edge("HAPbx", "User", label="4. Người dùng\nnghe phản hồi")

# --- Render ---
dot.render("architecture_diagram", format="png", cleanup=True)
print("Đã vẽ lại architecture_diagram.png với chất lượng cao nhất.")
