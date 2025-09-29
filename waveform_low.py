
import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu sóng âm rời rạc, gãy khúc
t = np.linspace(0, 2, 25)  # Ít điểm dữ liệu hơn
amplitude = np.sin(2 * np.pi * 2 * t) + np.random.uniform(-0.5, 0.5, len(t))

# Tạo hình ảnh và trục
fig, ax = plt.subplots(figsize=(8, 3))

# Vẽ đồ thị dạng bậc thang (step plot)
ax.step(t, amplitude, color="#A0A0A0", linewidth=2)

# Tô màu dưới đường sóng
ax.fill_between(t, amplitude, 0, step="pre", color="#A0A0A0", alpha=0.2)

# Xóa các chi tiết thừa
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

# Tiêu đề
fig.suptitle(
    "Giọng robot tiêu chuẩn",
    fontsize=16,
    fontname="Arial",
    color="#666666",
)

# Thiết lập nền trong suốt và lưu file
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)
plt.savefig("waveform_low.png", dpi=150, bbox_inches="tight", pad_inches=0)
plt.close()

print("Đã cập nhật và tạo waveform_low.png")
