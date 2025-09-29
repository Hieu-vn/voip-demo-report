import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị
G = nx.DiGraph()

# Thêm các nút (thư mục và file)
G.add_node("root", style="filled", fillcolor="lightyellow")
G.add_node("src", style="filled", fillcolor="lightgreen")
G.add_node("main.py", style="filled", fillcolor="white")
G.add_node("core", style="filled", fillcolor="lightgreen")
G.add_node("tts_server", style="filled", fillcolor="lightyellow")
G.add_node("server.py", style="filled", fillcolor="white")
G.add_node("config", style="filled", fillcolor="lightblue")
G.add_node("data", style="filled", fillcolor="lightblue")
G.add_node("docs", style="filled", fillcolor="lightblue")
G.add_node("docker-compose.yml", style="filled", fillcolor="white")
G.add_node("Dockerfile.app", style="filled", fillcolor="white")
G.add_node("Dockerfile.tts", style="filled", fillcolor="white")

# Thêm cạnh (mối quan hệ)
G.add_edge("root", "src")
G.add_edge("src", "main.py")
G.add_edge("src", "core")
G.add_edge("root", "tts_server")
G.add_edge("tts_server", "server.py")
G.add_edge("root", "config")
G.add_edge("root", "data")
G.add_edge("root", "docs")
G.add_edge("root", "docker-compose.yml")
G.add_edge("root", "Dockerfile.app")
G.add_edge("root", "Dockerfile.tts")

# Vẽ đồ thị
pos = nx.spring_layout(G)
plt.figure(figsize=(6, 4))
nx.draw(G, pos, with_labels=True, node_color=[G.nodes[n].get("fillcolor", "lightgray") for n in G.nodes], node_shape="s", alpha=0.8)
plt.title("Cấu trúc Thư mục Dự án", fontsize=12)
plt.axis("off")

# Lưu file
plt.savefig("folder_structure.png", dpi=100, bbox_inches='tight')
plt.close()

print("Đã tạo folder_structure.png")