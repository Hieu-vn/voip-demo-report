import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Config ---
FONT_NAME = "DejaVu Sans"
BG_COLOR = "#F7F9FC"
NODE_COLOR = "#FFFFFF"
BORDER_COLOR = "#B0BEC5"
ACCENT_COLOR = "#03A9F4"
TEXT_COLOR = "#333333"

# --- Setup ---
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_aspect('equal')
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# --- Nodes ---
nodes = {
    'User': {'pos': (2, 8), 'label': 'Người dùng', 'color': NODE_COLOR},
    'Asterisk': {'pos': (2, 5), 'label': 'HAPbx (Asterisk)', 'color': NODE_COLOR},
    'CallHandler': {'pos': (7, 8), 'label': 'Call Handler', 'color': ACCENT_COLOR, 'textcolor': 'white'},
    'STT': {'pos': (7, 6), 'label': 'Google STT', 'color': NODE_COLOR},
    'NLP': {'pos': (7, 4), 'label': 'Llama 4 Scout', 'color': NODE_COLOR},
    'TTS': {'pos': (7, 2), 'label': 'NeMo TTS Server', 'color': NODE_COLOR},
}

for name, node in nodes.items():
    ax.text(node['pos'][0], node['pos'][1], node['label'], 
            ha='center', va='center', fontname=FONT_NAME, fontsize=12,
            color=node.get('textcolor', TEXT_COLOR),
            bbox=dict(boxstyle='round,pad=0.8', fc=node['color'], ec=BORDER_COLOR, lw=1.5))

# --- Cluster ---
rect = patches.Rectangle((5, 0.5), 4.5, 9, linewidth=1, edgecolor=BORDER_COLOR, facecolor='#ECEFF1', linestyle='--', zorder=0, capstyle='round')
ax.add_patch(rect)
ax.text(7.25, 9.7, 'Lõi Xử lý AI', fontname=FONT_NAME, fontsize=14, color=TEXT_COLOR, ha='center')

# --- Arrows ---
arrows = [
    ('User', 'Asterisk', '1. Gọi'),
    ('Asterisk', 'CallHandler', '2. Bắt đầu'),
    ('CallHandler', 'STT', ''),
    ('STT', 'NLP', ''),
    ('NLP', 'TTS', ''),
    ('TTS', 'Asterisk', '3. Phản hồi'),
]

for start, end, label in arrows:
    ax.annotate(label, xy=nodes[end]['pos'], xytext=nodes[start]['pos'],
                arrowprops=dict(arrowstyle='->', color=TEXT_COLOR, lw=1.5, shrinkA=15, shrinkB=15),
                ha='center', va='center', fontname=FONT_NAME, fontsize=10)

# --- Title & Render ---
fig.suptitle("Minh họa Luồng hoạt động của AI Agent", fontsize=22, fontname=FONT_NAME, color=TEXT_COLOR, y=0.98)
plt.savefig("architecture_diagram.png", dpi=200, bbox_inches="tight")
plt.close()

print("Đã vẽ lại architecture_diagram.png theo phong cách thân thiện.")