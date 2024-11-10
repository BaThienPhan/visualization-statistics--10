import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dữ liệu điểm số của hai lớp A và B

import matplotlib.pyplot as plt
import seaborn as sns

# Data samples
data_1 = [2, 7, 6, 3, 9, 8, 6, 7, 9, 2, 5, 7, 5, 9, 8, 8, 7, 4, 3, 5, 5, 4, 5, 7, 7]
data_2 = [6, 7, 6, 4, 7, 9, 3, 8, 7, 5, 5, 6, 8, 7, 4, 5, 3, 10, 7, 9, 6, 7, 6, 7, 5]

# Mean and median calculations
mean_1 = sum(data_1) / len(data_1)
median_1 = sorted(data_1)[len(data_1) // 2]

mean_2 = sum(data_2) / len(data_2)
median_2 = sorted(data_2)[len(data_2) // 2]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Scatter plot for Data 1 using seaborn
sns.scatterplot(x=range(len(data_1)), y=sorted(data_1), color='skyblue', s=100, ax=axs[0])
axs[0].axhline(mean_1, color='orange', linestyle='--', label=f'Điểm trung bình = {mean_1}')
#axs[0].axhline(median_1, color='green', linestyle='--', label=f'Median = {median_1}')
axs[0].set_title("Lớp A")
axs[0].set_xlabel("Học sinh")
axs[0].set_ylabel("Value")
axs[0].legend()

# Scatter plot for Data 2 using seaborn
sns.scatterplot(x=range(len(data_2)), y=sorted(data_2), color='lightcoral', s=100, ax=axs[1])
axs[1].axhline(mean_2, color='orange', linestyle='--', label=f'Điểm trung bình  = {mean_2:.1f}')
#axs[1].axhline(median_2, color='green', linestyle='--', label=f'Median = {median_2}')
axs[1].set_title("Lớp B")
axs[1].set_xlabel("Học sinh")
axs[1].legend()

# Đặt miền giới hạn trục y của cả hai biểu đồ để chúng có cùng tỉ lệ
min_value = min(0, min(data_2))
max_value = max(max(data_1), 11)
axs[0].set_ylim(min_value, max_value)
axs[1].set_ylim(min_value, max_value)

# Căn chỉnh và hiển thị biểu đồ
plt.tight_layout()
plt.show()

