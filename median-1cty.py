import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Thu nhập của các thành viên (5 nhân viên và 1 giám đốc)
income = [4, 4, 4, 4, 4, 20]

# Tính thu nhập trung bình và trung vị
mean_income = np.mean(income)
median_income = np.median(income)

# Vẽ biểu đồ swarmplot
sns.swarmplot(data=income, color='blue', size=8, alpha=0.6)

# Vẽ đường trung bình
plt.axhline(y=mean_income, color='red', linestyle='--', label=f'Trung bình: {mean_income:.2f} triệu đồng')

# Vẽ đường trung vị
plt.axhline(y=median_income, color='green', linestyle='-.', label=f'Trung vị: {median_income} triệu đồng')

# Thêm tiêu đề và nhãn
plt.title('Thu nhập của các thành viên trong công ty')
plt.ylabel('Thu nhập (triệu đồng)')
plt.legend()

# Hiển thị biểu đồ
plt.show()
