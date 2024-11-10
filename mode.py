import seaborn as sns
import matplotlib.pyplot as plt

# Dữ liệu cỡ giày của khách hàng
shoe_sizes = [38, 39, 39, 38, 40, 41, 39, 39, 38, 39, 39, 39, 40, 39, 39]

# Thiết lập kiểu nền trắng với lưới
sns.set(style="whitegrid")

# Vẽ biểu đồ cột tần số với màu sắc tùy chỉnh
plt.figure(figsize=(8, 5))
sns.countplot(x=shoe_sizes, palette="viridis")  # Sử dụng bảng màu viridis

# Thiết lập tiêu đề và nhãn với font chữ lớn và in đậm
plt.title("Biểu đồ cột tần số cỡ giày của khách hàng", fontsize=16, fontweight='bold')
plt.xlabel("Cỡ giày", fontsize=14, fontweight='bold')
plt.ylabel("Tần số", fontsize=14, fontweight='bold')

# Hiển thị biểu đồ
plt.show()
