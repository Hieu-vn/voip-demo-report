import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu sóng âm gợn sóng
t = np.linspace(0, 1, 500)
amplitude = np.sin(2 * np.pi * 2 * t) + 0.8 * np.sin(2 * np.pi * 4 * t)
amplitude += np.random.normal(0, 0.5, len(t))  # Thêm nhiễu lớn để trông tệ

# Thiết lập hình ảnh
plt.figure(figsize=(6, 2))
plt.plot(t, amplitude, color='gray', linewidth=1, alpha=0.7)
plt.title("Robot - Chất lượng thấp", fontsize=12, color='gray')
plt.xlabel("Thời gian (s)")
plt.ylabel("Biên độ")
plt.grid(True, linestyle='--', alpha=0.5)
plt.ylim(-3, 3)

# Lưu file
plt.savefig("waveform_low.png", dpi=100, bbox_inches='tight')
plt.close()

print("Đã tạo waveform_low.png")