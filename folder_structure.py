
from graphviz import Digraph

# Pallete màu
BG_COLOR = "#FFFFFF"
FOLDER_COLOR = "#D1E8FF"  # Xanh nhạt cho thư mục
FILE_COLOR = "#FFFFFF"
EDGE_COLOR = "#888888"
FONT_COLOR = "#333333"
FONT_NAME = "Arial"

# Khởi tạo đồ thị
dot = Digraph(
    "Project Structure",
    graph_attr={
        "bgcolor": BG_COLOR,
        "rankdir": "TB",  # Từ trên xuống dưới
        "label": "Cấu trúc Thư mục Dự án",
        "fontsize": "20",
        "fontname": FONT_NAME,
        "fontcolor": FONT_COLOR,
    },
    node_attr={
        "fontname": FONT_NAME,
        "fontcolor": FONT_COLOR,
        "style": "filled",
        "shape": "box",
        "style": "rounded",
    },
    edge_attr={"color": EDGE_COLOR, "arrowhead": "none"},
)

# Thư mục gốc
dot.node("root", "voip-ai-agent/", fillcolor=FOLDER_COLOR)

# Các thư mục và file cấp 1
dot.node("src", "src/", fillcolor=FOLDER_COLOR)
dot.node("tts_server", "tts_server/", fillcolor=FOLDER_COLOR)
dot.node("docs", "docs/", fillcolor=FOLDER_COLOR)
dot.node("docker-compose.yml", "docker-compose.yml", shape="note", fillcolor=FILE_COLOR)

dot.edge("root", "src")
dot.edge("root", "tts_server")
dot.edge("root", "docs")
dot.edge("root", "docker-compose.yml")

# Các file và thư mục con
with dot.subgraph() as s:
    s.attr(rank="same")
    s.node("main.py", "main.py", shape="note", fillcolor=FILE_COLOR)
    s.node("core", "core/", fillcolor=FOLDER_COLOR)
    s.edge("src", "main.py")
    s.edge("src", "core")

with dot.subgraph() as s:
    s.attr(rank="same")
    s.node("server.py", "server.py", shape="note", fillcolor=FILE_COLOR)
    s.edge("tts_server", "server.py")


# Lưu file
dot.render("folder_structure", format="png", cleanup=True)
print("Đã cập nhật và tạo folder_structure.png")
