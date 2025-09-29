from graphviz import Digraph

# --- Config ---
FONT_NAME = "DejaVu Sans"
BG_COLOR = "#F7F9FC"
NODE_COLOR = "#FFFFFF"
BORDER_COLOR = "#B0BEC5"
EDGE_COLOR = "#607D8B"
CLUSTER_BG_COLOR = "#ECEFF1"
ACCENT_COLOR = "#03A9F4"

# --- Graph ---
dot = Digraph(
    "VoIP AI Agent Architecture",
    graph_attr={
        "bgcolor": BG_COLOR,
        "rankdir": "TB",
        "splines": "ortho",
        "nodesep": "1.2",
        "ranksep": "1.2",
        "label": "Kiến trúc Luồng Dữ liệu VoIP AI Agent",
        "fontsize": "24",
        "fontname": FONT_NAME,
    },
)

# --- Nodes & Clusters ---
with dot.subgraph(name="cluster_input") as c:
    c.attr(label="Đầu vào", style="rounded", bgcolor=CLUSTER_BG_COLOR)
    c.node("User", "👤\nNgười Dùng Cuối", shape="box", style="rounded,filled", fillcolor=NODE_COLOR, color=BORDER_COLOR)
    c.node("Asterisk", "📞\nAsterisk Server", shape="cylinder", fillcolor=NODE_COLOR, color=BORDER_COLOR)

with dot.subgraph(name="cluster_ai_core") as c:
    c.attr(label="Lõi Xử lý AI (Streaming)", style="rounded", bgcolor=CLUSTER_BG_COLOR)
    c.node("CallHandler", "Call Handler", shape="box", style="rounded,filled", fillcolor=ACCENT_COLOR, fontcolor="white")
    c.node("STT", "Google STT", shape="box", style="rounded,filled", fillcolor=NODE_COLOR, color=BORDER_COLOR)
    c.node("NLP", "Llama 4 Scout", shape="box", style="rounded,filled", fillcolor=NODE_COLOR, color=BORDER_COLOR)
    c.node("TTS", "NeMo TTS Server", shape="box", style="rounded,filled", fillcolor=NODE_COLOR, color=BORDER_COLOR)
    c.edge("CallHandler", "STT", label="Audio")
    c.edge("STT", "NLP", label="Text")
    c.edge("NLP", "TTS", label="Response")

# --- Edges ---
dot.edge("User", "Asterisk", label="1. Gọi điện")
dot.edge("Asterisk", "CallHandler", label="2. Bắt đầu cuộc gọi (ARI)")
dot.edge("TTS", "Asterisk", label="3. Phát âm thanh")
dot.edge("Asterisk", "User", label="4. Phản hồi")

# --- Render ---
dot.render("architecture_diagram", format="png", cleanup=True)
print("Đã tạo lại architecture_diagram.png phiên bản chuyên nghiệp.")