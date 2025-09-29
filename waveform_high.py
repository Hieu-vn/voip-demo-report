
import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu sóng âm mượt mà, phức tạp hơn
t = np.linspace(0, 2, 1000)
amplitude = (np.sin(2 * np.pi * 2 * t) + 0.7 * np.sin(2 * np.pi * 5 * t) + 0.4 * np.sin(2 * np.pi * 12 * t))

# Tạo hình ảnh và trục
fig, ax = plt.subplots(figsize=(8, 3))

# Vẽ đường sóng
ax.plot(t, amplitude, color="#00C851", linewidth=2.5)

# Thêm hiệu ứng tô màu gradient
# Tạo một dải màu từ nhạt đến đậm
gradient = np.linspace(0.0, 1.0, 256)
gradient = np.vstack((gradient, gradient))
# Tô màu dưới đường sóng
ax.fill_between(t, amplitude, 0, where=amplitude > 0, color="#00C851", alpha=0.3, interpolate=True)
ax.fill_between(t, amplitude, 0, where=amplitude <= 0, color="#00C851", alpha=0.3, interpolate=True)

# Xóa các chi tiết thừa
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

# Tiêu đề
fig.suptitle(
    "Giọng nói AI chuyên nghiệp",
    fontsize=16,
    fontname="Arial",
    color="#333333",
)

# Thiết lập nền trong suốt và lưu file
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)
plt.savefig("waveform_high.png", dpi=150, bbox_inches="tight", pad_inches=0)
plt.close()

print("Đã cập nhật và tạo waveform_high.png")
