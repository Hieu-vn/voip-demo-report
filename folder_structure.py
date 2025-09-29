from graphviz import Digraph

# --- Config ---
FONT_NAME = "DejaVu Sans"
BG_COLOR = "#F7F9FC"
FOLDER_COLOR = "#E3F2FD"
FILE_COLOR = "#FFFFFF"
BORDER_COLOR = "#90CAF9"
EDGE_COLOR = "#B0BEC5"

# --- Graph ---
dot = Digraph(
    "Project Structure",
    graph_attr={
        "bgcolor": BG_COLOR,
        "rankdir": "TB",
        "nodesep": "0.3",
        "ranksep": "0.5",
        "label": "Cấu trúc Thư mục Dự án Khoa học",
        "fontsize": "24",
        "fontname": FONT_NAME,
    },
    node_attr={"shape": "box", "style": "rounded,filled", "fontname": FONT_NAME, "color": BORDER_COLOR},
    edge_attr={"color": EDGE_COLOR, "arrowhead": "none"},
)

# --- Structure ---
dot.node("root", "📁 voip-ai-agent", fillcolor=FOLDER_COLOR, fontsize="14")

dot.node("src", "📁 src", fillcolor=FOLDER_COLOR)
dot.node("tts_server", "📁 tts_server", fillcolor=FOLDER_COLOR)
dot.node("docs", "📁 docs", fillcolor=FOLDER_COLOR)
dot.node("docker-compose", "📄 docker-compose.yml", shape="note", fillcolor=FILE_COLOR)

dot.edge("root", "src")
dot.edge("root", "tts_server")
dot.edge("root", "docs")
dot.edge("root", "docker-compose")

# Sub-nodes
dot.node("main.py", "📄 main.py", shape="note", fillcolor=FILE_COLOR)
dot.node("core", "📁 core", fillcolor=FOLDER_COLOR)
dot.edge("src", "main.py")
dot.edge("src", "core")

dot.node("call_handler.py", "📄 call_handler.py", shape="note", fillcolor=FILE_COLOR)
dot.edge("core", "call_handler.py")

dot.node("server.py", "📄 server.py", shape="note", fillcolor=FILE_COLOR)
dot.edge("tts_server", "server.py")

# --- Render ---
dot.render("folder_structure", format="png", cleanup=True)
print("Đã tạo lại folder_structure.png phiên bản chuyên nghiệp.")