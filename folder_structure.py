import matplotlib.pyplot as plt

# --- Config ---
FONT_NAME = "DejaVu Sans"
TEXT_COLOR = "#333333"

# --- Data ---
structure = [
    (0, "voip-ai-agent/"),
    (1, "src/"),
    (2, "main.py"),
    (2, "core/"),
    (3, "call_handler.py"),
    (1, "tts_server/"),
    (2, "server.py"),
    (1, "docker-compose.yml"),
    (1, "docs/"),
]

# --- Setup ---
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')

# --- Draw ---
y_pos = 1.0
for level, text in structure:
    prefix = "└── "
    if level > 0:
        prefix = "│   " * (level - 1) + "├── "
    
    display_text = f"{prefix}{text}"
    
    ax.text(0.1, y_pos, display_text, ha='left', va='center', fontname=FONT_NAME, fontsize=14, color=TEXT_COLOR, family='monospace')
    y_pos -= 0.1

# --- Title & Render ---
fig.suptitle("Cấu trúc Thư mục Dự án", fontsize=20, fontname=FONT_NAME, color=TEXT_COLOR, y=0.98)
ax.set_ylim(0, 1.1)
plt.savefig("folder_structure.png", dpi=200, bbox_inches="tight")
plt.close()

print("Đã vẽ lại folder_structure.png theo phong cách thân thiện.")