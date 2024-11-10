import matplotlib.pyplot as plt
import seaborn as sns

# Data samples
data_1 = [5, 7, 8, 6, 5, 5, 6]
data_2 = [5, 7, 8, 6, 5, 5, 50]

# Mean and median calculations
mean_1 = sum(data_1) / len(data_1)
median_1 = sorted(data_1)[len(data_1) // 2]

mean_2 = sum(data_2) / len(data_2)
median_2 = sorted(data_2)[len(data_2) // 2]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Scatter plot for Data 1 using seaborn
sns.scatterplot(x=range(len(data_1)), y=sorted(data_1), color='skyblue', s=100, ax=axs[0])
axs[0].axhline(mean_1, color='orange', linestyle='--', label=f'Mean = {mean_1}')
axs[0].axhline(median_1, color='green', linestyle='--', label=f'Median = {median_1}')
axs[0].set_title("Công ty A (No Outliers)")
axs[0].set_xlabel("Nhân viên")
axs[0].set_ylabel("Value")
axs[0].legend()

# Scatter plot for Data 2 using seaborn
sns.scatterplot(x=range(len(data_2)), y=sorted(data_2), color='lightcoral', s=100, ax=axs[1])
axs[1].axhline(mean_2, color='orange', linestyle='--', label=f'Mean = {mean_2:.1f}')
axs[1].axhline(median_2, color='green', linestyle='--', label=f'Median = {median_2}')
axs[1].set_title("Công ty B (With Outlier)")
axs[1].set_xlabel("Nhân viên")
axs[1].legend()

# Đặt miền giới hạn trục y của cả hai biểu đồ để chúng có cùng tỉ lệ
min_value = min(0, min(data_2))
max_value = max(max(data_1), 60)
axs[0].set_ylim(min_value, max_value)
axs[1].set_ylim(min_value, max_value)

plt.tight_layout()
plt.show()
