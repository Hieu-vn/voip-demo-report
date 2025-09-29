import matplotlib.pyplot as plt
import numpy as np

# --- Data ---
t = np.linspace(0, 2.5, 15) # Rất ít điểm dữ liệu
amplitude = np.sin(t * 2 * np.pi)

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 4))

# Vẽ các điểm dữ liệu rời rạc
ax.plot(t, amplitude, 'o', color="#6c757d", markersize=5)

# Vẽ đường gãy khúc nối các điểm
ax.step(t, amplitude, where='mid', color="#6c757d", linestyle='--', linewidth=1.5)

# Hiệu ứng tô màu
ax.fill_between(t, amplitude, 0, where=amplitude > 0, color="#6c757d", alpha=0.1, step='mid')
ax.fill_between(t, amplitude, 0, where=amplitude <= 0, color="#6c757d", alpha=0.1, step='mid')

# Xóa tất cả các chi tiết thừa
ax.set_ylim([-1.5, 1.5])
ax.set_axis_off()

# Tiêu đề
fig.suptitle(
    "Giọng Robot Tiêu chuẩn",
    fontsize=20,
    fontname="DejaVu Sans",
    color="#6c757d",
    y=0.98
)

# --- Render ---
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)
plt.savefig("waveform_low.png", dpi=200, bbox_inches="tight", pad_inches=0.1)
plt.close()

print("Đã tạo lại waveform_low.png phiên bản chuyên nghiệp.")