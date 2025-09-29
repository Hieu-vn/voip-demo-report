
from graphviz import Digraph

# --- Config ---
FONT_NAME = "DejaVu Sans"
BG_COLOR = "#FFFFFF"
FOLDER_FILL = "#F8F9FA"
FILE_FILL = "#FFFFFF"
BORDER_COLOR = "#DEE2E6"
EDGE_COLOR = "#ADB5BD"
TEXT_COLOR = "#212529"

# --- Graph ---
dot = Digraph(
    "Project Structure",
    graph_attr={
        "bgcolor": BG_COLOR,
        "rankdir": "TB",
        "nodesep": "0.5",
        "ranksep": "0.8",
        "label": "Cấu trúc Thư mục Dự án",
        "fontsize": "28",
        "fontname": FONT_NAME,
        "dpi": "200",
        "size": "10,10!",
    },
    node_attr={"style": "filled", "fontname": FONT_NAME, "fontcolor": TEXT_COLOR, "color": BORDER_COLOR},
    edge_attr={"color": EDGE_COLOR, "arrowhead": "none"},
)

# --- Structure ---
dot.node("root", "voip-ai-agent", shape="folder", fillcolor=FOLDER_FILL, fontsize="14")

# Cấp 1
dot.node("src", "src", shape="folder", fillcolor=FOLDER_FILL)
dot.node("tts_server", "tts_server", shape="folder", fillcolor=FOLDER_FILL)
dot.node("docker-compose", "docker-compose.yml", shape="note", fillcolor=FILE_FILL)
dot.node("readme", "README.md", shape="note", fillcolor=FILE_FILL)

dot.edge("root", "src")
dot.edge("root", "tts_server")
dot.edge("root", "docker-compose")
dot.edge("root", "readme")

# Cấp 2
dot.node("main.py", "main.py", shape="note", fillcolor=FILE_FILL)
dot.node("core", "core", shape="folder", fillcolor=FOLDER_FILL)
dot.edge("src", "main.py")
dot.edge("src", "core")

dot.node("server.py", "server.py", shape="note", fillcolor=FILE_FILL)
dot.edge("tts_server", "server.py")

# Cấp 3
dot.node("call_handler.py", "call_handler.py", shape="note", fillcolor=FILE_FILL)
dot.edge("core", "call_handler.py")

# --- Render ---
dot.render("folder_structure", format="png", cleanup=True)
print("Đã vẽ lại folder_structure.png với chất lượng cao nhất.")
