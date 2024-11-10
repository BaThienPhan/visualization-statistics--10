import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu sĩ số lớp
scores = np.array([43, 45, 46, 41, 40])

# Tính giá trị trung bình
mean = np.mean(scores)

# Tính phương sai và độ lệch chuẩn
variance = np.var(scores)
std_dev = np.std(scores)

# In kết quả
print(f"Giá trị trung bình: {mean}")
print(f"Phương sai: {variance}")
print(f"Độ lệch chuẩn: {std_dev}")

# Vẽ đồ thị độ sai lệch
plt.figure(figsize=(8, 5))
plt.plot(scores, 'bo-', label='Sĩ số các lớp', markersize=8)

# Vẽ đường trung bình
plt.axhline(mean, color='r', linestyle='--', label=f'Mean = {mean}')

# Nối các điểm với đường trung bình
for i in range(len(scores)):
    plt.plot([i, i], [scores[i], mean], 'g--', alpha=0.7)  # Đoạn thẳng nối điểm với trung bình

plt.title('Đồ thị thể hiện độ sai lệch so với giá trị trung bình')
plt.xlabel('Lớp')
plt.ylabel('Sĩ số')
plt.legend()
plt.grid(True)
plt.show()
