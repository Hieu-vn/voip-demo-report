import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu sóng âm mượt mà
t = np.linspace(0, 1, 1000)
amplitude = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)
amplitude += np.random.normal(0, 0.1, len(t))  # Thêm nhiễu nhỏ để tự nhiên

# Thiết lập hình ảnh
plt.figure(figsize=(6, 2))
plt.plot(t, amplitude, color='green', linewidth=2)
plt.title("NeMo TTS - Giọng tự nhiên", fontsize=12, color='green')
plt.xlabel("Thời gian (s)")
plt.ylabel("Biên độ")
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-2, 2)

# Lưu file
plt.savefig("waveform_high.png", dpi=100, bbox_inches='tight')
plt.close()

print("Đã tạo waveform_high.png")