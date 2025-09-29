import matplotlib.pyplot as plt
import numpy as np

# --- Data ---
t = np.linspace(0, 2.5, 2000)
amplitude = (np.sin(t * 2 * np.pi) * 0.8 + np.sin(t * 5 * np.pi) * 0.4 + np.sin(t * 12 * np.pi) * 0.2)

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 4))

# Vẽ đường sóng chính
ax.plot(t, amplitude, color="#007BFF", linewidth=2)

# Hiệu ứng tô màu
ax.fill_between(t, amplitude, 0, color="#007BFF", alpha=0.1)

# Xóa tất cả các chi tiết thừa
ax.set_ylim([-1.5, 1.5])
ax.set_axis_off()

# Tiêu đề
fig.suptitle(
    "Giọng nói AI Chất lượng cao",
    fontsize=20,
    fontname="DejaVu Sans",
    color="#212529",
    y=0.98
)

# --- Render ---
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)
plt.savefig("waveform_high.png", dpi=200, bbox_inches="tight", pad_inches=0.1)
plt.close()

print("Đã tạo lại waveform_high.png phiên bản chuyên nghiệp.")