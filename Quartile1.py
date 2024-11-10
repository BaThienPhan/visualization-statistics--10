import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Dữ liệu điểm của các thí sinh
scores = [58, 74, 92, 81, 97, 88, 75, 69, 87, 69, 75, 77]

# Sắp xếp điểm số
sorted_scores = sorted(scores)

# Xác định các ngưỡng điểm phân loại mới
thresholds = [71.5, 76, 87.5]  # Các ngưỡng phân loại: Giải Tư, Ba, Nhì

# Tạo biểu đồ swarmplot với seaborn
plt.figure(figsize=(12, 6))
sns.swarmplot(x=sorted_scores, color='b', size=10)

# Đánh dấu các ngưỡng phân loại mới
plt.axvline(thresholds[0], color='orange', linestyle='--', label=f'Ngưỡng Giải Tư: {thresholds[0]}')
plt.axvline(thresholds[1], color='green', linestyle='--', label=f'Ngưỡng Giải Ba: {thresholds[1]}')
plt.axvline(thresholds[2], color='red', linestyle='--', label=f'Ngưỡng Giải Nhì: {thresholds[2]}')

# Đánh dấu các ngưỡng phân loại mới không nhãn
#plt.axvline(thresholds[0], color='orange', linestyle='--')
#plt.axvline(thresholds[1], color='green', linestyle='--')
#plt.axvline(thresholds[2], color='red', linestyle='--')

# Thiết lập giới hạn và chia đơn vị cho trục X
plt.xlim(50, 100)
plt.xticks(np.arange(50, 101, 5))  # Chia đơn vị từ 50 đến 100, cách nhau 5 đơn vị

# Đặt tiêu đề và nhãn cho các trục với kích thước chữ lớn hơn
plt.title('Phân phối điểm và các ngưỡng phân loại', fontsize=16)
plt.xlabel('Điểm', fontsize=14)
plt.ylabel('Phân phối', fontsize=14)

# Điều chỉnh kích thước chữ của nhãn trên hai trục
plt.xticks(fontsize=12, color='darkblue')
plt.yticks(fontsize=12, color='darkblue')

# Hiển thị chú thích
plt.legend(fontsize=12)
plt.show()
